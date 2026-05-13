"""T37 · browser-side security headers baseline.

This module owns three security headers that Django's
``SecurityMiddleware`` does **not** ship out of the box:

  - ``Content-Security-Policy``       — XSS-mitigation + exfiltration cap.
  - ``Permissions-Policy``            — opt out of powerful browser features.
  - ``Cross-Origin-Resource-Policy``  — restrict who can embed our static
    resources cross-origin.
  - ``X-Permitted-Cross-Domain-Policies`` — Flash/PDF cross-domain
    policy lockdown (low-impact today, zero cost).

The Django-shipped headers (``X-Content-Type-Options``,
``Referrer-Policy``, ``Cross-Origin-Opener-Policy``,
``X-Frame-Options``, HSTS in prod) continue to come from
``django.middleware.security.SecurityMiddleware`` +
``XFrameOptionsMiddleware`` — this module adds the four headers
that are missing from that out-of-the-box surface.

Why a single module (and not split between base/dev/prod)
---------------------------------------------------------
The header values themselves are environment-agnostic — the
allowlisted CDN / font / Stripe domains do not differ between
dev and prod. Defining them once and applying them via a single
middleware in both profiles means:

  - A developer sees CSP violations in their browser console
    locally, BEFORE a deploy. The legacy "CSP enforced only in
    prod" pattern produces production-only surprises.
  - The headers are exercised by the same Django test client
    used for the rest of the suite, so a CSP-breaking template
    change is caught by CI.

CSP shape rationale
-------------------
The current frontend uses inline ``style="..."`` attributes,
inline event handlers (``onchange="this.form.submit()"``), and
inline ``<script>`` blocks across roughly fifteen templates.
Migrating those to nonce-based CSP would mean editing every
template + wiring a per-request nonce processor — explicitly
out-of-scope for this baseline (T37 brief).

The pragmatic CSP therefore includes ``'unsafe-inline'`` for both
``script-src`` and ``style-src``. This concession is real and
documented: an inline-XSS payload smuggled into one of those
inline contexts still executes. What the CSP *does* protect
against, even with ``'unsafe-inline'``:

  - External script injection: ``<script src="https://evil/x.js">``
    is blocked because evil/ is not in the allowlist.
  - Form action redirection: ``<form action="https://evil/...">``
    is blocked by ``form-action 'self'``.
  - Clickjacking: ``frame-ancestors 'none'`` blocks iframe
    embedding (redundant with X-Frame-Options DENY in prod, but
    modern browsers prefer the CSP form).
  - ``<base href="...">`` injection: ``base-uri 'self'`` blocks
    redirection of relative URLs to an attacker origin.
  - Plugin abuse: ``object-src 'none'`` blocks Flash/ActiveX.
  - Data exfiltration via fetch/XHR/WebSocket: ``connect-src``
    is constrained to ``'self'`` + ``api.stripe.com``. An XSS
    that runs inline can still call ``fetch('https://evil/...')``
    — but the browser blocks the connection. Useful even against
    inline XSS for the most common "exfiltrate the session
    cookie" payload.

Removing ``'unsafe-inline'`` from ``style-src`` would break:
  - ``templates/commerce/dashboard/*.html``  (~20+ ``style="..."`` attrs)
  - ``templates/catalog/template_detail.html``  (style="..." on hero)
  - ``templates/commerce/skins/*/product.html``  (``style="background-image:url(...)"``)

Removing ``'unsafe-inline'`` from ``script-src`` would break:
  - ``templates/commerce/payment/stripe.html``  (inline Stripe init IIFE)
  - ``templates/commerce/skins/*/product.html``  (inline cart-add scripts)
  - ``templates/projects/project_editor.html``  (inline editor bootstrap)
  - ``templates/commerce/dashboard/*.html``      (``onclick=`` / ``onchange=``)
  - several ``live_templates/*/*.html`` storefront skins

Both concessions are scoped — the *origins* of scripts and
styles still must come from the allowlist (``'self'``, jsdelivr,
Google Fonts, Stripe). An attacker who manages to inject
``<script src="evil.com/...">`` is still blocked at the browser.

External origins allowlisted (audited from real templates)
----------------------------------------------------------
- ``https://cdn.jsdelivr.net``  — Bootstrap 5.3 CSS + JS,
  Bootstrap Icons CSS (used by ``templates/base.html``).
- ``https://fonts.googleapis.com``  — Google Fonts CSS endpoint
  (used by ``templates/base.html`` <link>).
- ``https://fonts.gstatic.com``  — Google Fonts WOFF2 binaries.
- ``https://js.stripe.com``  — Stripe.js v3 + Stripe Elements
  iframe (used by ``templates/commerce/payment/stripe.html``).
- ``https://api.stripe.com``  — Stripe Elements XHR target
  (PaymentIntent confirm).

``img-src`` deliberately allows ``https:`` (no host pin) because
the marketplace renders template preview images from arbitrary
upstream URLs (the ``TemplateAsset`` ``image_url`` field is
free-form text in the editor). Pinning ``img-src`` to a small
set would require an image-proxy redesign — out of scope.

Permissions-Policy shape
------------------------
Opts out of every powerful browser API the project does not use.
``payment=()`` blocks the Payment Request API on this origin —
the Stripe Elements iframe inside ``payment/stripe.html`` does
NOT use Payment Request API for card payments (it uses
``stripe.confirmPayment(...)`` directly), so blocking the parent
API is safe. If Apple Pay / Google Pay via Payment Request API
is added later, relax to
``payment=(self "https://js.stripe.com")``.

``interest-cohort=()`` opts out of the legacy FLoC API;
``browsing-topics=()`` opts out of its successor Topics API
(Chrome's third-party ad-tech replacement for FLoC).

Cross-Origin-Resource-Policy
----------------------------
``same-origin`` on responses prevents another origin from
embedding our static resources (CSS/JS/images) via
``<img>`` / ``<script>`` / ``<link>`` tags when their page
specifies Cross-Origin-Embedder-Policy (Spectre-mitigation
context). Low-impact today because we serve few cross-origin
embeds, but a free defense-in-depth layer.
"""
from __future__ import annotations


# ---------------------------------------------------------------------------
# CSP — content security policy
# ---------------------------------------------------------------------------

_CSP_DIRECTIVES: tuple[tuple[str, str], ...] = (
    ("default-src", "'self'"),
    (
        "script-src",
        # 'unsafe-inline' is the pragmatic concession (see module docstring).
        # The host allowlist still blocks external script injection.
        "'self' 'unsafe-inline' https://cdn.jsdelivr.net https://js.stripe.com",
    ),
    (
        "style-src",
        # 'unsafe-inline' here covers BOTH inline <style> blocks AND
        # the inline style="..." attributes used across dashboards.
        "'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net",
    ),
    (
        "font-src",
        # https://cdn.jsdelivr.net covers Bootstrap Icons — its CSS at
        # https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.min.css
        # references the WOFF2 file via a *relative* URL (`src: url("fonts/...")`)
        # which the browser resolves against the stylesheet's origin (jsdelivr).
        # Without this entry the icon glyphs render as empty boxes — verified
        # live in Chrome during T37 verification.
        "'self' https://fonts.gstatic.com https://cdn.jsdelivr.net data:",
    ),
    (
        "img-src",
        # https: (no host pin) on purpose — template preview images
        # come from arbitrary user-supplied URLs in TemplateAsset.
        "'self' data: https:",
    ),
    (
        "connect-src",
        # Self for our own XHR; api.stripe.com for Stripe.confirmPayment.
        "'self' https://api.stripe.com",
    ),
    (
        "frame-src",
        # 'self' covers the editor's live preview iframe — the editor at
        # /projects/<uuid>/editor/ embeds /templates/<cat>/<slug>/preview/
        # via an <iframe class="ed-frame">, same-origin. Without 'self'
        # here CSP blocks the iframe and the editor canvas renders empty
        # (regression caught during T40 first-run walkthrough — see
        # T40 report §1).
        # https://js.stripe.com covers Stripe Elements (Stripe Checkout
        # renders its card form inside an iframe served by Stripe).
        "'self' https://js.stripe.com",
    ),
    # Clickjacking — modern equivalent of X-Frame-Options SAMEORIGIN.
    # 'self' (not 'none') because the editor at /projects/<uuid>/editor/
    # embeds its OWN preview at /templates/<cat>/<slug>/preview/?project=...
    # as a same-origin <iframe>; 'none' here would block that embed
    # (regression caught during T40 first-run walkthrough — see
    # T40 report §1). Cross-origin embedding from third-party sites
    # remains blocked, which is the actual clickjacking threat.
    ("frame-ancestors", "'self'"),
    # <base> injection mitigation.
    ("base-uri", "'self'"),
    # Forms can only post to our own origin.
    ("form-action", "'self'"),
    # No Flash / ActiveX / generic plugin embeds.
    ("object-src", "'none'"),
)

CSP_HEADER: str = "; ".join(f"{d} {v}" for d, v in _CSP_DIRECTIVES)


# ---------------------------------------------------------------------------
# Permissions-Policy — opt out of powerful browser features
# ---------------------------------------------------------------------------

_PERMISSIONS_POLICY_FEATURES: tuple[tuple[str, str], ...] = (
    # Sensor / capture APIs
    ("accelerometer", "()"),
    ("camera", "()"),
    ("geolocation", "()"),
    ("gyroscope", "()"),
    ("magnetometer", "()"),
    ("microphone", "()"),
    ("usb", "()"),
    # Payment Request API — Stripe iframe handles payments via its
    # own postMessage protocol, not this API. Relax to
    # `(self "https://js.stripe.com")` if Apple Pay / Google Pay
    # via Payment Request is enabled later.
    ("payment", "()"),
    # Ad-tech / cohort APIs (FLoC + Topics)
    ("interest-cohort", "()"),
    ("browsing-topics", "()"),
)

PERMISSIONS_POLICY_HEADER: str = ", ".join(
    f"{feat}={value}" for feat, value in _PERMISSIONS_POLICY_FEATURES
)


# ---------------------------------------------------------------------------
# Cross-Origin-Resource-Policy + X-Permitted-Cross-Domain-Policies
# ---------------------------------------------------------------------------

CROSS_ORIGIN_RESOURCE_POLICY_HEADER: str = "same-origin"
PERMITTED_CROSS_DOMAIN_POLICIES_HEADER: str = "none"


# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------

class SecurityHeadersMiddleware:
    """Set the four T37 browser-side headers on every response.

    Uses ``response.headers.setdefault(...)`` so a view that
    intentionally overrides one of these (e.g. a future endpoint
    that needs a tighter ``Content-Security-Policy``) wins. The
    rest of the project never sets these today, so the defaults
    apply everywhere.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.headers.setdefault("Content-Security-Policy", CSP_HEADER)
        response.headers.setdefault("Permissions-Policy", PERMISSIONS_POLICY_HEADER)
        response.headers.setdefault(
            "Cross-Origin-Resource-Policy",
            CROSS_ORIGIN_RESOURCE_POLICY_HEADER,
        )
        response.headers.setdefault(
            "X-Permitted-Cross-Domain-Policies",
            PERMITTED_CROSS_DOMAIN_POLICIES_HEADER,
        )
        return response
