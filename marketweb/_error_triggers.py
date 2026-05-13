"""Env-gated trigger views for the user-facing error templates (T24).

Purpose
-------
Render the branded ``templates/400.html``, ``templates/403.html`` and
``templates/500.html`` pages on demand so an operator can smoke-check
them in a real browser without having to engineer a CSRF failure,
hand-craft a ``Host:`` header, or wait for an actual exception in a
view.

These triggers exist ONLY when ``DJANGO_T24_TRIGGERS=1`` is set in
the process environment. With the env var unset (the prod default)
the URLs are NOT mounted at all — there is zero exposure for real
traffic. Reverse-side: a deploy that wants to re-verify the error
surface after a CSS regression flips the flag, hits three URLs, and
flips it back.

Wired in
--------
``marketweb/urls.py`` — the conditional ``if env("DJANGO_T24_TRIGGERS")``
block that ``include``s the patterns below.

NOT a public contract
---------------------
The path prefix ``__error/`` is internal. Do not link to it from
the marketplace UI, do not include it in sitemaps, do not document
it externally.
"""
from __future__ import annotations

from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.urls import path
from django.views.csrf import csrf_failure
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST


def trigger_400(request):
    """Raise SuspiciousOperation → Django renders templates/400.html."""
    raise SuspiciousOperation("T24 · synthetic 400 for branded-template smoke check.")


def trigger_403(request):
    """Raise PermissionDenied → Django renders templates/403.html."""
    raise PermissionDenied("T24 · synthetic 403 for branded-template smoke check.")


def trigger_500(request):
    """Raise an unhandled exception → Django renders templates/500.html."""
    raise RuntimeError("T24 · synthetic 500 for branded-template smoke check.")


def trigger_csrf(request):
    """Call the project's CSRF failure view directly → renders templates/403_csrf.html.

    T25 · this is a GET-friendly shortcut for smoke-checking the
    branded CSRF page. The real production trigger is "POST without
    a valid CSRF token to any CSRF-protected form" — we call the same
    view function here with a deterministic reason so the rendered
    HTML matches what users would see in the wild.
    """
    return csrf_failure(request, reason="T25 · synthetic CSRF failure for smoke check.")


@csrf_protect
@require_POST
def trigger_405(request):
    """T25 · GET-405 trigger for the branded 405 response.

    ``@require_POST`` returns an ``HttpResponseNotAllowed(["POST"])``
    when the method is GET (or anything else). The branded-405
    middleware rewrites that response body to ``templates/405.html``.
    """
    return None  # @require_POST short-circuits before this line is reached on GET.


urlpatterns = [
    path("400/", trigger_400, name="t24-trigger-400"),
    path("403/", trigger_403, name="t24-trigger-403"),
    path("500/", trigger_500, name="t24-trigger-500"),
    path("csrf/", trigger_csrf, name="t25-trigger-csrf"),
    path("405/", trigger_405, name="t25-trigger-405"),
]
