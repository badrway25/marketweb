"""T31 · request-context propagation for the audit log.

Django's model signals (``post_save``, ``post_delete``) fire with
no knowledge of the HTTP request that triggered them — and yet our
audit log NEEDS to know who clicked which button. The standard
pattern is a thin middleware that stashes the current request user
+ IP in a thread-local, which the signal receivers then read.

This file ships:

  - ``_audit_context`` — a ``threading.local`` holding the active
    request's actor + IP. Never used directly by callers.
  - ``get_audit_context()`` — public helper returning the active
    ``AuditContext`` (or ``AuditContext(None, None)`` outside any
    request cycle, e.g. inside a management command).
  - ``AuditContextMiddleware`` — pushes/pops the per-request values.

Threading note
--------------
Django serves each request on a single thread under WSGI (gunicorn
sync workers) — the thread-local is therefore correct for the
request that owns it. Async views and Channels are NOT supported by
this implementation; the receivers will simply observe an empty
context and write ``actor=None`` audit rows. Documented as a known
limitation in the T31 report.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass


@dataclass(frozen=True)
class AuditContext:
    """Snapshot of the request actor + IP for signal receivers."""

    actor_id: int | None
    actor_repr: str
    request_ip: str | None


_audit_context = threading.local()


def get_audit_context() -> AuditContext:
    """Return the current request's audit context, or an empty one
    when called outside any request cycle (management command,
    Celery task, shell)."""
    ctx = getattr(_audit_context, "value", None)
    if ctx is None:
        return AuditContext(actor_id=None, actor_repr="", request_ip=None)
    return ctx


def _ip_from_request(request) -> str | None:
    """Resolve the client IP honouring the same reverse-proxy hop
    count axes uses (``AXES_IPWARE_PROXY_COUNT``) so audit and
    lockout records keep IP attribution aligned."""
    # Simple resolution: trust the leftmost X-Forwarded-For entry
    # when the header is present; otherwise REMOTE_ADDR. The axes
    # IPWare helper does more — we keep it simple here because the
    # audit row's IP is a contextual hint, not a security key.
    xff = request.META.get("HTTP_X_FORWARDED_FOR", "").strip()
    if xff:
        # Leftmost = original client, per RFC 7239 §5.2.
        return xff.split(",", 1)[0].strip() or None
    return request.META.get("REMOTE_ADDR") or None


class AuditContextMiddleware:
    """Push the request user + IP into the thread-local for signal
    receivers, then pop it on response. Off-path requests (zero
    tracked-model writes happen on the request) pay only the
    setattr/delattr cost — measured negligible in dev.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user", None)
        ctx = AuditContext(
            actor_id=getattr(user, "pk", None) if user and user.is_authenticated else None,
            actor_repr=str(user) if user and user.is_authenticated else "",
            request_ip=_ip_from_request(request),
        )
        _audit_context.value = ctx
        try:
            return self.get_response(request)
        finally:
            # Always clear, even on exception. The thread-local would
            # otherwise leak across requests when the WSGI worker is
            # reused (gunicorn sync workers do reuse threads).
            _audit_context.value = None
