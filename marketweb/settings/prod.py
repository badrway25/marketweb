"""Production settings for marketweb (Sprint 0 · T1+T2+T3).

Hardening posture:

- DEBUG OFF (cannot be flipped without explicitly setting DJANGO_DEBUG=1).
- SECRET_KEY required from env (raises ImproperlyConfigured if missing).
- ALLOWED_HOSTS required from env (refuses the wildcard ``*``).
- Full ``SECURE_*`` preset (HSTS 1 year, SSL redirect, secure cookies,
  no sniff, no XSS legacy header, strict referrer policy, X-Frame-Options
  DENY).
- DATABASE configured via ``DATABASE_*`` env (PostgreSQL recommended).
- Email via SMTP env vars; falls back to console backend with a runtime
  warning when SMTP is missing — this keeps a misconfigured prod from
  500-ing the password-reset flow but is loudly visible in logs.
- Stripe stub fallback OFF unless explicitly opted into via env.
- LOGGING upgraded to JSON-friendly key=value lines so a log shipper
  (Loki, Datadog, CloudWatch, ...) can parse without a custom formatter.

Out of scope for this Sprint
----------------------------
- CDN / object storage for static + media (deployment-shape decision).
- Rate limiting (django-ratelimit / axes) — Sprint 2.
- 2FA on /admin (django-otp) — Sprint 2.

Wired by later passes
---------------------
- Sentry SDK observability — wired by T19 (2026-05-10) via
  ``marketweb/sentry.py::init_sentry_if_dsn_set``. Init fires only
  when ``SENTRY_DSN`` is set in the env; dev/CI/local stay dormant.
- WhiteNoise static-file serving — wired by T22 (2026-05-10) so
  gunicorn alone can serve ``/static/`` with cache headers + gzip
  in prod, without nginx in front. Dev path untouched (Django's
  ``runserver`` keeps autoserving statics).

Cross-references
----------------
- ``factory/reports/execution-2026-05-10/SPRINT0_T1_T2_T3_DEPLOYABLE_BASELINE.md``
- ``.env.example`` at the repo root
- ``manage.py check --deploy`` validates this profile.
"""
from __future__ import annotations

from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F401,F403
from .base import MIDDLEWARE as _BASE_MIDDLEWARE, env, BASE_DIR

# ---------------------------------------------------------------------------
# Core toggles · all required from env, no silent dev fallback
# ---------------------------------------------------------------------------

# Default OFF; flipping back on requires an explicit env override and is
# discouraged outside short-lived investigations.
DEBUG = env("DJANGO_DEBUG", "0", cast=bool)

# Hard-fail on a missing prod secret. The base helper raises
# ImproperlyConfigured with a precise message.
SECRET_KEY = env("DJANGO_SECRET_KEY", required=True)

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", required=True, cast=list)
if "*" in ALLOWED_HOSTS:
    raise ImproperlyConfigured(
        "ALLOWED_HOSTS must not contain the wildcard '*' in production. "
        "List the real public hostnames explicitly (comma-separated)."
    )

# CSRF_TRUSTED_ORIGINS is required as soon as the public hostname is
# served behind HTTPS — ALL https POST forms (admin login, signup, etc.)
# break without it. Required in prod.
CSRF_TRUSTED_ORIGINS = env("DJANGO_CSRF_TRUSTED_ORIGINS", required=True, cast=list)


# ---------------------------------------------------------------------------
# SECURE_* preset · WCAG-style hardening floor
# ---------------------------------------------------------------------------

# Tell Django it's behind a proxy that already terminated TLS; the
# canonical setup uses an X-Forwarded-Proto header from nginx / Traefik /
# the load balancer.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env("DJANGO_SECURE_SSL_REDIRECT", "1", cast=bool)

# 1 year HSTS, includeSubDomains, preload-eligible. Override via env if
# the deploy is not yet on a stable HTTPS hostname (set
# DJANGO_SECURE_HSTS_SECONDS=0 the first day, then ramp up).
SECURE_HSTS_SECONDS = env("DJANGO_SECURE_HSTS_SECONDS", "31536000", cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", "1", cast=bool
)
SECURE_HSTS_PRELOAD = env("DJANGO_SECURE_HSTS_PRELOAD", "1", cast=bool)

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"

# Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # Django requires the CSRF cookie to be JS-readable for the {% csrf_token %} JS pattern; tag-rendered forms still work.
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

# Clickjacking
X_FRAME_OPTIONS = "DENY"


# ---------------------------------------------------------------------------
# Database · env-driven; PostgreSQL strongly recommended in prod
# ---------------------------------------------------------------------------
#
# Two ways to configure:
#
#  1. Granular: DATABASE_ENGINE / NAME / USER / PASSWORD / HOST / PORT
#     (default ENGINE = postgresql, default PORT = 5432).
#  2. Fall back to SQLite at BASE_DIR/db.sqlite3 only if NO Postgres env
#     var is supplied AND DJANGO_ALLOW_SQLITE_PROD=1 is explicitly set —
#     this keeps a forgotten-env prod boot from silently writing to a
#     local SQLite file on the container's ephemeral disk.

if env("DATABASE_NAME"):
    DATABASES = {
        "default": {
            "ENGINE": env("DATABASE_ENGINE", "django.db.backends.postgresql"),
            "NAME": env("DATABASE_NAME", required=True),
            "USER": env("DATABASE_USER", ""),
            "PASSWORD": env("DATABASE_PASSWORD", ""),
            "HOST": env("DATABASE_HOST", "127.0.0.1"),
            "PORT": env("DATABASE_PORT", "5432"),
            "CONN_MAX_AGE": env("DATABASE_CONN_MAX_AGE", "60", cast=int),
        }
    }
elif env("DJANGO_ALLOW_SQLITE_PROD", "0", cast=bool):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    raise ImproperlyConfigured(
        "Production database is not configured. Set DATABASE_NAME (and "
        "DATABASE_USER / DATABASE_PASSWORD / DATABASE_HOST as needed) "
        "in the environment, or — for a one-off SQLite-on-disk prod "
        "(strongly discouraged) — set DJANGO_ALLOW_SQLITE_PROD=1."
    )


# ---------------------------------------------------------------------------
# Email · SMTP via env; loudly degrade to console if SMTP host missing
# ---------------------------------------------------------------------------

if env("EMAIL_HOST"):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env("EMAIL_HOST", required=True)
    EMAIL_PORT = env("EMAIL_PORT", "587", cast=int)
    EMAIL_HOST_USER = env("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", "")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS", "1", cast=bool)
    EMAIL_USE_SSL = env("EMAIL_USE_SSL", "0", cast=bool)
    DEFAULT_FROM_EMAIL = env(
        "DEFAULT_FROM_EMAIL", "noreply@marketweb.local"
    )
else:
    # Visible-in-logs fallback so a misconfigured deploy does not 500
    # the password-reset flow on day 1, but the operator sees the
    # warning immediately.
    import logging
    logging.getLogger("django").warning(
        "EMAIL_HOST is not set in production — falling back to "
        "console.EmailBackend (emails will NOT be delivered)."
    )
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# ---------------------------------------------------------------------------
# Stripe stub fallback · default OFF in prod (silent stub = silent loss)
# ---------------------------------------------------------------------------

# Override the dev default so a missing STRIPE_SECRET_KEY in prod is a
# hard error in the dispatcher rather than a silently-stubbed payment.
STRIPE_ALLOW_STUB_FALLBACK = env(
    "STRIPE_ALLOW_STUB_FALLBACK", "0", cast=bool
)


# ---------------------------------------------------------------------------
# LOGGING · key=value lines, INFO root, WARNING for noisy Django subloggers
# ---------------------------------------------------------------------------
#
# Format chosen to be parseable by Loki/Promtail, Datadog, CloudWatch
# Logs Insights without a custom regex. Switch to JSONFormatter (e.g.
# python-json-logger) when introducing structlog — Sprint 2 scope.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "kv": {
            "format": (
                "ts={asctime} level={levelname} logger={name} "
                "msg=\"{message}\""
            ),
            "style": "{",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "kv",
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
        "django.db.backends": {
            "handlers": ["console"],
            "level": env("DJANGO_DB_LOG_LEVEL", "WARNING"),
            "propagate": False,
        },
        # T32 · audit alert emissions. Use INFO so the WARN-level
        # alerts emitted by ``apps.core.audit._emit_alert`` land in
        # the console handler regardless of the root level.
        "marketweb.audit": {
            "handlers": ["console"],
            "level": env("AUDIT_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}


# ---------------------------------------------------------------------------
# Static files · WhiteNoise (T22 · 2026-05-10)
# ---------------------------------------------------------------------------
#
# WhiteNoise lets gunicorn alone serve `/static/` with proper cache
# headers + gzip compression — so a deploy does not need nginx /
# Traefik in front just to serve CSS/JS. The middleware is inserted
# IMMEDIATELY AFTER `SecurityMiddleware` (per WhiteNoise docs) so
# every static-file response also goes through the SECURE_* headers.
#
# Storage backend: `CompressedStaticFilesStorage` ships gzip-encoded
# variants alongside originals (no manifest / hashed filenames). The
# manifest variant (`CompressedManifestStaticFilesStorage`) would
# require running `collectstatic` against the prod profile at build
# time — which means SECRET_KEY + ALLOWED_HOSTS env at build time.
# Out of scope for this baseline. Promotable later when the deploy
# pipeline can supply prod env to the image build step.
#
# Dev path is NOT touched — `dev.py` keeps the base MIDDLEWARE and
# Django's `runserver` static autoserver continues to work without
# any `collectstatic` step.

MIDDLEWARE = [
    _BASE_MIDDLEWARE[0],  # django.middleware.security.SecurityMiddleware
    # T37 · keep SecurityHeadersMiddleware ABOVE WhiteNoise so that
    # static-file responses (which short-circuit in WhiteNoise and
    # never reach the bottom of the chain) ALSO receive the CSP /
    # Permissions-Policy / CORP / X-Permitted-Cross-Domain-Policies
    # headers on their way out. Without this position, /static/*.css
    # would ship without those four headers in prod.
    _BASE_MIDDLEWARE[1],  # marketweb.security_headers.SecurityHeadersMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *_BASE_MIDDLEWARE[2:],
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Bump the cache lifetime for hashed asset paths. Without manifest
# the filenames are NOT hashed, so leave this at the WhiteNoise default
# (`max_age=60` for non-immutable files) instead of long-lived caching
# that would lock users on a stale CSS/JS after a deploy.
WHITENOISE_MAX_AGE = env("WHITENOISE_MAX_AGE", "60", cast=int)


# ---------------------------------------------------------------------------
# Observability · Sentry SDK (T19 · 2026-05-10)
# ---------------------------------------------------------------------------
#
# Init is gated by SENTRY_DSN. With no DSN the helper is a no-op and
# returns False — dev/CI/local stay dormant. With a DSN it calls
# sentry_sdk.init with the DjangoIntegration and a small set of
# env-driven tunables (environment / release / sample rates / PII).
# Failures (missing SDK, bad DSN) degrade to a single WARNING log
# line and do NOT break the boot — observability is not critical-path.
#
# Tunables documented in `.env.example` and in
# `marketweb/sentry.py::init_sentry_if_dsn_set`.

from marketweb.sentry import init_sentry_if_dsn_set as _init_sentry  # noqa: E402

_init_sentry(env)
