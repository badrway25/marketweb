"""Development settings for marketweb (Sprint 0 · T1+T2+T3).

Defaults the project's behavior to "local laptop, no env file required":
DEBUG on, dev-only SECRET_KEY fallback (clearly marked), permissive
ALLOWED_HOSTS for localhost + testserver, console email backend,
SQLite at ``BASE_DIR/db.sqlite3``.

Override anything via environment variables documented in
``.env.example`` at the repo root.
"""
from __future__ import annotations

import warnings

from .base import *  # noqa: F401,F403
from .base import env

# ---------------------------------------------------------------------------
# Core toggles · env-driven with dev-safe fallbacks
# ---------------------------------------------------------------------------

# DEBUG is True by default in dev. Set DJANGO_DEBUG=0 to mimic prod
# behaviour locally (e.g. when sanity-checking error pages).
DEBUG = env("DJANGO_DEBUG", "1", cast=bool)

# SECRET_KEY: read from env first; fall back to a clearly-marked
# DEV-ONLY value. The fallback exists so a fresh checkout can `runserver`
# without any setup, but the prefix makes it obvious in logs / debug
# pages that this MUST be replaced before any deploy.
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    "django-insecure-dev-only-secret-do-not-use-in-prod",
)
if SECRET_KEY.startswith("django-insecure-dev-only-"):
    warnings.warn(
        "Using the dev-only SECRET_KEY fallback. Set DJANGO_SECRET_KEY "
        "in your environment before any non-local run.",
        RuntimeWarning,
        stacklevel=2,
    )

# ALLOWED_HOSTS: env-driven, with the canonical localhost + testserver
# entries pre-included so `runserver` and the Django test client both
# work out of the box.
ALLOWED_HOSTS = list({
    *env("DJANGO_ALLOWED_HOSTS", "", cast=list),
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "testserver",
})


# ---------------------------------------------------------------------------
# Cookies / sessions · stay relaxed in dev so http://127.0.0.1 still works
# ---------------------------------------------------------------------------

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0
SECURE_PROXY_SSL_HEADER = None

# CSRF_TRUSTED_ORIGINS: empty by default in dev. Extend via env when
# testing against a different origin (e.g. a tunnel or Docker host).
CSRF_TRUSTED_ORIGINS = env("DJANGO_CSRF_TRUSTED_ORIGINS", "", cast=list)


# ---------------------------------------------------------------------------
# Email · console-print in dev so signup / password-reset don't try SMTP
# ---------------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
