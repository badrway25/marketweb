"""Base Django settings shared between dev and prod (Sprint 0 · T1+T2+T3).

Anything that is genuinely environment-agnostic lives here. Anything
that toggles between dev and prod (DEBUG, SECRET_KEY fallback, secure
cookies, DB, logging) is decided in ``dev.py`` or ``prod.py``.

Reading environment variables
-----------------------------
The ``env(...)`` helper below is intentionally tiny — no third-party
dependency added in this Sprint. It supports:

    env("KEY")                                  # str or None
    env("KEY", "fallback")                      # str fallback
    env("KEY", required=True)                   # raise if missing
    env("DEBUG", "0", cast=bool)                # bool("1"/"true"/"yes"/"on")
    env("ALLOWED_HOSTS", "", cast=list)         # comma-split list
    env("PORT", "8000", cast=int)               # int
    env("SAMPLE_RATE", "0.1", cast=float)       # float (T19 · Sentry tunables)

Cross-references
----------------
- ``factory/reports/execution-2026-05-10/SPRINT0_T1_T2_T3_DEPLOYABLE_BASELINE.md``
- ``.env.example`` at the repo root
"""
from __future__ import annotations

import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

# ---------------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------------

# settings/base.py → settings/ → marketweb/ → repo root
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ---------------------------------------------------------------------------
# Tiny env helper (zero dependencies)
# ---------------------------------------------------------------------------

_BOOL_TRUE = {"1", "true", "yes", "on", "y", "t"}
_BOOL_FALSE = {"0", "false", "no", "off", "n", "f", ""}


def env(key, default=None, *, required=False, cast=str):
    """Read ``key`` from the process environment.

    - ``default``  — fallback value when the key is unset.
    - ``required`` — raise ``ImproperlyConfigured`` when the key is unset
                     AND no fallback is provided. Use in prod for secrets.
    - ``cast``     — ``str`` (default), ``bool``, ``int``, ``float``, or
                     ``list`` (comma-separated, whitespace-stripped).
    """
    raw = os.environ.get(key)
    if raw is None or raw == "":
        if required and default is None:
            raise ImproperlyConfigured(
                f"Required environment variable {key!r} is not set. "
                "Either export it (e.g. via your .env loader, the shell, "
                "or the deployment secret manager) or pass a default."
            )
        raw = default
    if raw is None:
        return None
    if cast is bool:
        s = str(raw).strip().lower()
        if s in _BOOL_TRUE:
            return True
        if s in _BOOL_FALSE:
            return False
        raise ImproperlyConfigured(
            f"Environment variable {key!r} expected a boolean "
            f"(1/0/true/false/yes/no/on/off), got {raw!r}."
        )
    if cast is list:
        return [s.strip() for s in str(raw).split(",") if s.strip()]
    if cast is int:
        return int(raw)
    if cast is float:
        return float(raw)
    return str(raw)


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

# SECRET_KEY and DEBUG are intentionally NOT defined here — both are
# decided per-profile (dev provides a clearly-marked fallback, prod
# requires the env var to be set). ALLOWED_HOSTS is handled the same way.

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # T43 · Django Sitemaps framework powers /sitemap.xml. Stdlib —
    # no extra dependency. The actual sitemap classes live in
    # ``apps.catalog.sitemaps`` and are wired by ``marketweb/urls.py``.
    "django.contrib.sitemaps",
    # Third-party
    "rest_framework",
    "drf_spectacular",
    "django_filters",
    "crispy_forms",
    "crispy_bootstrap5",
    "axes",  # T23 · brute-force protection on /admin/ + /account/login/
    # T27 · admin 2FA · TOTP second factor on /admin/. The `django_otp`
    # core ships the `Device` abstraction + middleware; `otp_totp` is
    # the RFC-6238 plugin used by every standard authenticator app
    # (Google Authenticator, Authy, 1Password, Bitwarden, ...).
    # Customer-facing 2FA stays out-of-scope here.
    "django_otp",
    "django_otp.plugins.otp_totp",
    # Local apps
    "apps.core",
    "apps.accounts",
    "apps.catalog",
    "apps.editor",
    "apps.projects",
    "apps.commerce",
    "apps.pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # T37 · browser-side hardening — sets Content-Security-Policy,
    # Permissions-Policy, Cross-Origin-Resource-Policy and
    # X-Permitted-Cross-Domain-Policies on every response. Positioned
    # immediately after SecurityMiddleware so the same response is
    # touched by both layers (Django's SECURE_* preset + the headers
    # Django does not ship out of the box). Dev and prod both pick
    # this up — the CSP / Permissions values are environment-agnostic.
    "marketweb.security_headers.SecurityHeadersMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # T27 · django-otp · MUST come immediately after Auth so the
    # OTPMiddleware can decorate `request.user` with `is_verified()`
    # for OTPAdminSite.has_permission to evaluate the second factor.
    # Affects only the admin gate — public auth flow is unaffected
    # because customer views never call `is_verified()`.
    "django_otp.middleware.OTPMiddleware",
    # T29 · cap the OTP-verified state lifetime on /admin/ (default
    # 8h via OTP_ADMIN_REVERIFY_SECONDS env). MUST come AFTER
    # OTPMiddleware so it sees `user.is_verified()` resolved.
    "marketweb.middleware.AdminOtpReverifyMiddleware",
    # T31 · push request.user + IP into a thread-local so signal-
    # driven audit log receivers can attribute mutations to the
    # acting admin. MUST come AFTER AuthenticationMiddleware (which
    # sets request.user) and BEFORE any middleware that mutates
    # tracked models on its way to the view (currently none, but
    # the position is the correct invariant).
    "apps.core.middleware.AuditContextMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # T25 · branded 405 rewrite. Sits AFTER the auth/session/messages
    # stack so the rendered template can use {% url %}, request.user,
    # and the messages framework — and BEFORE axes so a 405 emitted
    # downstream still gets branded (axes only short-circuits on a
    # different code path).
    "marketweb.middleware.BrandedMethodNotAllowedMiddleware",
    # T23 · django-axes — MUST be last so an already-locked attempt
    # short-circuits before reaching any view (per axes docs).
    "axes.middleware.AxesMiddleware",
]

ROOT_URLCONF = "marketweb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "marketweb.wsgi.application"
ASGI_APPLICATION = "marketweb.asgi.application"


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

AUTH_USER_MODEL = "accounts.User"

# Phase A.1b (D-087): customer-facing auth lives under /account/.
LOGIN_URL = "/account/login/"
LOGIN_REDIRECT_URL = "/projects/"
LOGOUT_REDIRECT_URL = "/"


# ---------------------------------------------------------------------------
# Auth backends · T23 (django-axes brute-force gate)
# ---------------------------------------------------------------------------
#
# AxesStandaloneBackend MUST come FIRST so failed attempts get
# tracked + locked-out attempts get rejected before the model
# backend ever runs. ModelBackend stays as the actual credentials
# verifier on the unlocked path.

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesStandaloneBackend",
    "django.contrib.auth.backends.ModelBackend",
]


# ---------------------------------------------------------------------------
# django-axes policy · T23 (2026-05-10)
# ---------------------------------------------------------------------------
#
# Threshold: AXES_FAILURE_LIMIT failed attempts within
# AXES_RESET_COOL_OFF_ON_FAILURE_FOR window → lockout for
# AXES_COOLOFF_TIME hours. Lockout key is the (IP, username) pair
# so a hot-lobby IP (corporate proxy, NAT) does not lock out
# every coworker because of one attacker.
#
# Successful login resets the counter for that key (RESET_ON_SUCCESS).
#
# Defaults: 5 failures → 1 hour lockout. Tunable via env so the
# operator can tighten in prod (e.g. 3 / 6h) without a redeploy.

import sys as _sys

# Auto-disable inside `manage.py test` runs. The Django test client
# calls `authenticate()` without a request, which AxesStandaloneBackend
# reasonably refuses (it needs the request for IP/UA tracking). The
# standard axes idiom is to disable in tests; the lockout policy is
# instead exercised by a dedicated integration test that does post a
# real client request (see `apps/core/tests.py::AxesLockoutTests`).
_RUNNING_TESTS = "test" in _sys.argv or "pytest" in _sys.argv[0]

AXES_ENABLED = env("AXES_ENABLED", "1", cast=bool) and not _RUNNING_TESTS
AXES_FAILURE_LIMIT = env("AXES_FAILURE_LIMIT", "5", cast=int)
AXES_COOLOFF_TIME = env("AXES_COOLOFF_TIME_HOURS", "1", cast=int)
# T26 · branded HTTP 429 lockout page (axes renders this when the
# request is NOT an XHR). The XHR/AJAX path stays JSON (axes checks
# X-Requested-With before falling through to the template — see
# axes/helpers.py::get_lockout_response). Status code, Allow header
# behaviour and the (ip, username) policy from T23 are untouched.
AXES_LOCKOUT_TEMPLATE = "axes_lockout.html"


# ---------------------------------------------------------------------------
# T29 · OTP session re-verification policy (admin only)
# ---------------------------------------------------------------------------
#
# Cap on the OTP-verified state lifetime on /admin/ requests, INDEPENDENT
# of SESSION_COOKIE_AGE. After this many seconds the user is forced to
# re-enter password + TOTP even though their auth session is still valid.
#
# Default 8 hours (one work-day). Tunable via env so a deploy in a
# more sensitive context can tighten without a code change (e.g. set
# OTP_ADMIN_REVERIFY_SECONDS=3600 for 1h re-prompts).
#
# Implementation: marketweb.middleware.AdminOtpReverifyMiddleware + a
# stamp written by `_stamp_otp_login` on the user_logged_in signal.

OTP_ADMIN_REVERIFY_SECONDS = env("OTP_ADMIN_REVERIFY_SECONDS", "28800", cast=int)


# ---------------------------------------------------------------------------
# T32 · Audit log retention + alerting policy
# ---------------------------------------------------------------------------
#
# Retention: ``python manage.py prune_audit_log`` deletes AuditLogEntry
# rows whose ``timestamp`` is older than N days. Default 365 (one year)
# — enough to cover a typical compliance review window without letting
# the table grow unbounded. Tunable via ``AUDIT_LOG_RETENTION_DAYS``.
#
# Alerting: when an AuditLogEntry with ``action in {role_changed,
# deleted}`` is written, the receiver in ``apps.core.audit`` emits
#  - a WARNING line via the ``marketweb.audit`` logger
#    (the prod LOGGING config picks it up via the kv formatter), AND
#  - an email to ``AUDIT_ALERT_RECIPIENTS`` (empty list = no email,
#    the dev default; set in prod via env to enable).
#
# ``AUDIT_ALERTS_ENABLED`` is a kill-switch for tests / break-glass
# scenarios; default ON.

AUDIT_LOG_RETENTION_DAYS = env("AUDIT_LOG_RETENTION_DAYS", "365", cast=int)
AUDIT_ALERT_RECIPIENTS = env("AUDIT_ALERT_RECIPIENTS", "", cast=list)
AUDIT_ALERTS_ENABLED = env("AUDIT_ALERTS_ENABLED", "1", cast=bool)


# ---------------------------------------------------------------------------
# T38 · Backup baseline
# ---------------------------------------------------------------------------
#
# ``python manage.py backup_db`` writes a timestamped DB dump under
# ``BACKUP_DIR`` and prunes older files to keep at most
# ``BACKUP_KEEP_COUNT``. Both knobs are env-tunable so a deploy can
# point at a mounted volume (``/var/backups/marketweb``) and a
# different retention without code changes.

BACKUP_DIR = env("BACKUP_DIR", str(BASE_DIR / "backups"))
BACKUP_KEEP_COUNT = env("BACKUP_KEEP_COUNT", "7", cast=int)
# Nested list = COMBO key per (ip_address, username). Without
# nesting, axes 7.x treats the list as OR — any of the keys
# tripping its own count is enough to lock out, which would let
# one attacker block every user behind a NAT IP.
AXES_LOCKOUT_PARAMETERS = [["ip_address", "username"]]
AXES_RESET_ON_SUCCESS = True
# Surface the lockout in logs without spamming the regular logger.
AXES_VERBOSE = env("AXES_VERBOSE", "1", cast=bool)
# Honour standard reverse-proxy headers when set (so the lockout
# key is the real client IP, not the proxy IP). Empty in dev =
# remote_addr; set in prod when behind nginx/Traefik/load balancer.
AXES_IPWARE_PROXY_COUNT = env("AXES_IPWARE_PROXY_COUNT", "0", cast=int)

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ---------------------------------------------------------------------------
# Internationalization
# ---------------------------------------------------------------------------

LANGUAGE_CODE = "it"
TIME_ZONE = "Europe/Rome"
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------------------------
# Static / media
# ---------------------------------------------------------------------------

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ---------------------------------------------------------------------------
# Django REST Framework + drf-spectacular
# ---------------------------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "MarketWeb API",
    "DESCRIPTION": "API for the MarketWeb template marketplace",
    "VERSION": "0.1.0",
}


# ---------------------------------------------------------------------------
# Crispy Forms
# ---------------------------------------------------------------------------

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# ---------------------------------------------------------------------------
# Stripe (env-driven, optional in dev)
# ---------------------------------------------------------------------------
#
# Stripe is optional. Storefronts configured with payment_provider
# = "stripe" use real Stripe PaymentIntents when STRIPE_SECRET_KEY is
# set; otherwise apps/commerce/payments.py falls back to the stub
# provider gracefully (see PaymentIntent.payload.stub_fallback).

STRIPE_SECRET_KEY      = env("STRIPE_SECRET_KEY", "")
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_WEBHOOK_SECRET  = env("STRIPE_WEBHOOK_SECRET", "")
# Default True (dev-friendly). In prod set STRIPE_ALLOW_STUB_FALLBACK=0
# so a missing real key is a hard error instead of a silent stub.
STRIPE_ALLOW_STUB_FALLBACK = env("STRIPE_ALLOW_STUB_FALLBACK", "1", cast=bool)


# ---------------------------------------------------------------------------
# Database default (dev-friendly: SQLite). Overridden in prod via env.
# ---------------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------------------------
# Email (dev-safe default; prod overrides to SMTP)
# ---------------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", "noreply@marketweb.local")


# ---------------------------------------------------------------------------
# Logging baseline (overridden / extended in prod)
# ---------------------------------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "compact": {
            "format": "{asctime} {levelname:7} {name}: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "compact",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": env("DJANGO_LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}
