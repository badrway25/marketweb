"""Sentry SDK init helper · T19 observability baseline (2026-05-10).

Single responsibility: read ``SENTRY_DSN`` + a tiny set of tunables
from the environment, call ``sentry_sdk.init`` with safe defaults,
and return ``True`` if init actually happened. Returns ``False``
(silently) when no DSN is set — the path taken in dev, CI, local
manage.py runs, and any prod boot that has not opted into Sentry yet.

Why a separate module
---------------------
The init lives here, not inline in ``settings/prod.py``, so it can be
(1) unit-tested without import side effects (see
``apps/core/tests.py::SentryInitTests``), (2) reused if a future
non-Django entrypoint wants Sentry (custom cron, celery worker,
one-off ``manage.py`` command).

T34 · audit log → Sentry breadcrumbs (2026-05-11)
-------------------------------------------------
Sentry-SDK ships a ``LoggingIntegration`` in its default integration
set. The default config (``level=INFO``, ``event_level=ERROR``)
already turns every WARN-level ``marketweb.audit`` line (T32 alert
receiver, T33 decorator failure path) into a Sentry breadcrumb
attached to the in-flight Hub scope. T34 makes that contract
**explicit and pinned**:

- We pass an explicit ``LoggingIntegration(level=WARNING,
  event_level=ERROR)`` — narrower than the default ``INFO`` level
  so the breadcrumb stream stays lean (no routine INFO chatter from
  ``django.db.backends`` etc. lands as a breadcrumb).
- The T32 ``_emit_alert`` receiver passes an ``extra={...}`` dict
  on its ``logger.warning(...)`` call. The standard
  ``BreadcrumbHandler._extra_from_record`` forwards every non-builtin
  LogRecord attribute into the breadcrumb's ``data`` dict — so the
  Sentry UI shows structured fields (``audit_action``,
  ``audit_actor``, ``audit_target``, ``audit_changes``,
  ``audit_request_ip``) instead of a flat-text message only.

Failure mode
------------
Never raises. If ``sentry-sdk`` is not installed, the helper logs a
``WARNING`` once and returns ``False``. A misconfigured DSN does not
break the boot — Sentry is observability, not a critical-path
dependency.

Cross-references
----------------
- ``marketweb/settings/prod.py`` calls this helper at module load.
- ``.env.example`` documents every ``SENTRY_*`` var.
- ``factory/reports/execution-2026-05-10/T19_SENTRY_SDK_OBSERVABILITY.md``
  is the closure receipt.
- ``factory/reports/execution-2026-05-10/T34_SENTRY_AUDIT_BREADCRUMBS.md``
  is the T34 closure receipt.
"""
from __future__ import annotations

import logging
from typing import Callable

logger = logging.getLogger(__name__)


def init_sentry_if_dsn_set(env: Callable) -> bool:
    """Init Sentry when ``SENTRY_DSN`` is set in the environment.

    Returns ``True`` if init was called, ``False`` otherwise. Never
    raises — failures degrade to a single ``WARNING`` log line.

    Parameters
    ----------
    env : callable
        The ``env(key, default, *, required, cast)`` helper from
        ``marketweb.settings.base``. Passed in (instead of imported)
        so this module stays Django-free for testing.

    Tunables (all read via ``env``):

    - ``SENTRY_DSN``                     · empty disables init (default)
    - ``SENTRY_ENVIRONMENT``             · default ``"production"``
    - ``SENTRY_RELEASE``                 · default unset → SDK auto-detect
    - ``SENTRY_TRACES_SAMPLE_RATE``      · default ``0.0`` (errors-only)
    - ``SENTRY_PROFILES_SAMPLE_RATE``    · default ``0.0`` (no profiling)
    - ``SENTRY_SEND_DEFAULT_PII``        · default ``0`` (privacy)
    """
    dsn = env("SENTRY_DSN", "")
    if not dsn:
        return False

    try:
        import sentry_sdk
        from sentry_sdk.integrations.django import DjangoIntegration
        from sentry_sdk.integrations.logging import LoggingIntegration
    except ImportError:
        logger.warning(
            "SENTRY_DSN is set but sentry-sdk is not installed; "
            "skipping Sentry init. Install via "
            "`pip install sentry-sdk[django]`."
        )
        return False

    # T34 · pin LoggingIntegration explicitly so a future sentry-sdk
    # release that flips the default cannot silently widen our
    # breadcrumb stream. WARNING is the lowest level that produces a
    # breadcrumb (so the T32 ``audit_alert`` lines + the T33
    # decorator's defensive warnings both land in Sentry forensics);
    # ERROR is the lowest level that fires a full Sentry event (so
    # ``logger.error(...)`` from anywhere in the codebase keeps the
    # same "send to Sentry" semantics as today).
    logging_integration = LoggingIntegration(
        level=logging.WARNING,
        event_level=logging.ERROR,
    )

    sentry_sdk.init(
        dsn=dsn,
        integrations=[DjangoIntegration(), logging_integration],
        environment=env("SENTRY_ENVIRONMENT", "production"),
        # An empty release string makes the SDK fall back to its own
        # git/version detection; pass None to make that fallback explicit.
        release=env("SENTRY_RELEASE", "") or None,
        traces_sample_rate=env("SENTRY_TRACES_SAMPLE_RATE", "0.0", cast=float),
        profiles_sample_rate=env("SENTRY_PROFILES_SAMPLE_RATE", "0.0", cast=float),
        send_default_pii=env("SENTRY_SEND_DEFAULT_PII", "0", cast=bool),
    )
    return True
