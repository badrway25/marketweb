"""Project-level middleware.

This module hosts two unrelated middlewares + one signal handler:

  - ``BrandedMethodNotAllowedMiddleware``  (T25 · 405 polish)
  - ``AdminOtpReverifyMiddleware``         (T29 · 2FA session policy)
  - ``_stamp_otp_login`` signal listener   (T29 · timestamp the OTP login)

T29 · 2026-05-11 — AdminOtpReverifyMiddleware
==============================================

After T27 the ``/admin/`` gate requires password + TOTP, BUT
django-otp keeps the verified state alive for the entire session
lifetime (default ``SESSION_COOKIE_AGE`` = 2 weeks). A stolen or
exfiltrated session cookie within that window bypasses the 2FA
factor entirely.

This middleware enforces a tighter ceiling — INDEPENDENT of
``SESSION_COOKIE_AGE`` — on the OTP-verified state for admin
requests. After ``OTP_ADMIN_REVERIFY_SECONDS`` (default 8h, env
``OTP_ADMIN_REVERIFY_SECONDS``) the user is forced to re-enter
password + TOTP, even though their auth session is still valid.

Mechanism
---------
On successful login through the OTP-aware admin form, django-otp
fires ``user_logged_in`` and stores ``otp_device_id`` in the
session. We listen on the same signal and stamp
``otp_verified_at = int(time.time())``.

The middleware runs AFTER ``OTPMiddleware``. For requests under
``/admin/`` (excluding ``/admin/login/`` and ``/admin/logout/`` so
we don't redirect-loop ourselves), if the OTP verified-at stamp is
absent or older than the max-age:

  1. Pop ``otp_device_id`` from the session   → next request
     evaluates ``is_verified()`` as False.
  2. Pop ``otp_verified_at`` from the session.
  3. Reset ``user.otp_device = None``         → the CURRENT request
     also fails ``is_verified()`` (defeats the lazy-loaded user
     cache from OTPMiddleware so admin.has_permission returns
     False on this request, not the next).

The ``_auth_user_id`` session key is preserved on purpose: the user
stays authenticated (logged in), they just lost the OTP factor.
The admin redirect lands on ``/admin/login/`` where they re-enter
both credentials (the form runs ``authenticate()`` which re-checks
the password, so credential rotation is not skipped).

What this does NOT do
---------------------
- Force re-login of customer-facing ``/account/login/`` sessions.
  T29 is admin-only by design (path-prefixed at ``/admin/``).
- Touch ``SESSION_COOKIE_AGE`` (which would impact customers).
- Override Django's logout behaviour. ``/admin/logout/`` already
  flushes the session, which clears every key including our stamp.

T25 · 2026-05-11 — BrandedMethodNotAllowedMiddleware
=====================================================

Django has no ``handler405`` and ``HttpResponseNotAllowed`` is a bare
response class with an empty body. The user-facing surface for a 405
is therefore literally a blank viewport — worse than every other
error code in the family. This middleware closes that gap by
rewriting the response body to ``templates/405.html`` when:

  1. The downstream view returned status_code == 405, AND
  2. The request looks HTML-bound (Accept header contains text/html
     or '*/*' and the path is NOT under ``/api/``).

The ``Allow`` response header is preserved (RFC 9110 §15.5.6 — a 405
MUST advertise the methods the resource accepts). Status code stays
405. Content-Length is recomputed.

Why not a custom ``handler405``?
--------------------------------
Django's URL conf supports ``handler400 / 403 / 404 / 500`` but NOT
``handler405``. The 405 response is created directly by the view
decorator (``require_POST``, ``require_http_methods``, CBV ``http_method_not_allowed``)
and never enters ``django.core.handlers.exception.response_for_exception``.
A post-response middleware is the canonical interception point.

Why not a custom 405 response class?
------------------------------------
Would require touching every view + every CBV in the project to swap
``HttpResponseNotAllowed`` for a branded variant. The middleware
approach is one file and zero view edits.

API / JSON paths
----------------
Requests under ``/api/`` are left untouched — DRF emits its own
``Response({"detail": ..., "status_code": 405})`` JSON which clients
parse programmatically. Rewriting that to HTML would be a real
behavior break.

T20+T21 / T24 coherence
-----------------------
The rendered template uses the same ``.mw-error`` pattern as
``templates/400.html``, ``templates/403.html``, ``templates/404.html``
— same pill, headline, lead, CTAs. Coherence is template-side; the
middleware is purely the delivery mechanism.
"""
from __future__ import annotations

import logging
import time

from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.template import loader

from django_otp import DEVICE_ID_SESSION_KEY


logger = logging.getLogger("marketweb.middleware")


# ---------------------------------------------------------------------------
# T29 · OTP session re-verification policy
# ---------------------------------------------------------------------------

#: Session key holding the unix-epoch seconds of the last successful
#: OTP verification. Read + written by ``AdminOtpReverifyMiddleware``
#: and the ``_stamp_otp_login`` signal listener.
OTP_VERIFIED_AT_SESSION_KEY = "otp_verified_at"

#: Default ceiling (seconds) on the OTP-verified state lifetime for
#: ``/admin/`` requests. Overridden by ``OTP_ADMIN_REVERIFY_SECONDS``
#: in settings. 8 hours = one work-day; tunable per deploy.
DEFAULT_OTP_ADMIN_REVERIFY_SECONDS = 28800


def _stamp_otp_login(sender, request, user, **kwargs):
    """T29 · stamp the timestamp of an OTP-verified login.

    The ``user_logged_in`` signal fires every time
    ``django.contrib.auth.login`` runs. django-otp listens on the
    same signal and writes ``otp_device_id`` to the session if the
    user has an ``otp_device`` attribute (set by an OTP-aware form).

    Right after that, we stamp the time. The reverify middleware
    reads this value to decide when to require a fresh second factor.

    Customer-facing logins (no ``otp_device`` set, no
    ``otp_device_id`` in session) are no-ops — the stamp is only
    relevant for OTP-verified sessions.
    """
    if request is None:
        return
    if not hasattr(request, "session"):
        return
    if request.session.get(DEVICE_ID_SESSION_KEY):
        request.session[OTP_VERIFIED_AT_SESSION_KEY] = int(time.time())


user_logged_in.connect(_stamp_otp_login, dispatch_uid="t29_stamp_otp_login")


class AdminOtpReverifyMiddleware:
    """T29 · cap the OTP-verified state lifetime on ``/admin/`` requests.

    See the module docstring for the full mechanism. The middleware
    is path-scoped: only requests under ``/admin/`` are gated, and
    ``/admin/login/`` / ``/admin/logout/`` are exempted so the
    re-authentication flow itself works.
    """

    PATH_PREFIX = "/admin/"
    EXEMPT_PATHS = ("/admin/login/", "/admin/logout/")

    def __init__(self, get_response):
        self.get_response = get_response
        self.max_age = int(
            getattr(
                settings,
                "OTP_ADMIN_REVERIFY_SECONDS",
                DEFAULT_OTP_ADMIN_REVERIFY_SECONDS,
            )
        )

    def __call__(self, request):
        path = request.path
        # Off-path → no-op. Login / logout exempt so we don't loop.
        if path.startswith(self.PATH_PREFIX) and path not in self.EXEMPT_PATHS:
            user = getattr(request, "user", None)
            # The SimpleLazyObject from OTPMiddleware resolves on
            # attribute access. is_authenticated triggers resolution
            # cheaply (no extra DB query when the user is unauthenticated).
            if (
                user is not None
                and user.is_authenticated
                and callable(getattr(user, "is_verified", None))
                and user.is_verified()
            ):
                stamp = request.session.get(OTP_VERIFIED_AT_SESSION_KEY)
                now = int(time.time())
                expired = (stamp is None) or (now - int(stamp) > self.max_age)
                if expired:
                    # Clear the OTP-verified state from both the
                    # session AND the in-memory user. Keep
                    # ``_auth_user_id`` — auth login stays valid; only
                    # the second factor expires.
                    request.session.pop(DEVICE_ID_SESSION_KEY, None)
                    request.session.pop(OTP_VERIFIED_AT_SESSION_KEY, None)
                    user.otp_device = None
                    # ``is_verified()`` reads ``otp_device`` (see
                    # django_otp.middleware.is_verified), so the line
                    # above is enough to make it return False on the
                    # rest of this request — admin.has_permission
                    # downstream will redirect to /admin/login/.

        return self.get_response(request)


class BrandedMethodNotAllowedMiddleware:
    """Rewrite 405 responses to use ``templates/405.html`` for browsers."""

    TEMPLATE_NAME = "405.html"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code != 405:
            return response
        if not self._is_html_request(request):
            return response
        # Already branded (e.g. a future view sets its own custom body)
        # — leave it alone. We only rewrite Django's default empty body.
        if response.content and b"mw-error" in response.content:
            return response

        try:
            template = loader.get_template(self.TEMPLATE_NAME)
        except Exception as exc:
            # The branded template is missing or broken; fall back to
            # Django's empty-body 405 so we don't make a 500 out of a 405.
            # Log so an operator notices in the kv log stream instead of
            # silently shipping a blank page.
            logger.warning(
                "BrandedMethodNotAllowedMiddleware: template load failed "
                "for %r — falling back to Django's empty 405 body. error=%s",
                self.TEMPLATE_NAME, exc,
            )
            return response

        allowed_methods = response.get("Allow", "")
        ctx = {
            "request": request,
            "allowed_methods": [m.strip() for m in allowed_methods.split(",") if m.strip()],
        }

        rendered = template.render(ctx, request=request)
        # Keep the original status + the Allow header (RFC 9110 §15.5.6).
        response.content = rendered.encode("utf-8")
        response["Content-Type"] = "text/html; charset=utf-8"
        response["Content-Length"] = str(len(response.content))
        return response

    @staticmethod
    def _is_html_request(request):
        """True when the request is browser-bound (HTML / wildcard accept)
        and not under the JSON API surface."""
        if request.path.startswith("/api/"):
            return False
        accept = request.META.get("HTTP_ACCEPT", "")
        if not accept:
            # Most browsers send Accept; if absent we err on the side of
            # branding (server-to-server pings rarely 405).
            return True
        return "text/html" in accept or "*/*" in accept
