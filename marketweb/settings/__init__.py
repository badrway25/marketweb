"""Settings package for marketweb (Sprint 0 · T1+T2+T3).

Three real settings modules:

- ``base``  — shared Django configuration; reads SECRET_KEY / DEBUG /
              ALLOWED_HOSTS / database / Stripe from the environment via
              the ``env(...)`` helper. Never imported directly — pick
              ``dev`` or ``prod``.
- ``dev``   — local development defaults: DEBUG on, SQLite, console email,
              dev-only SECRET_KEY fallback. Used by ``manage.py`` by
              default.
- ``prod``  — production hardening: DEBUG off, SECRET_KEY required from
              env, ALLOWED_HOSTS required, full ``SECURE_*`` preset,
              database from env, structured LOGGING. Used by ``wsgi.py``
              and ``asgi.py``.

Backwards compatibility
-----------------------
Several pre-existing entry points (``smoke_*.py`` at the repo root,
``factory/reports/scorecard/*/_smoke.py``) hard-code
``DJANGO_SETTINGS_MODULE = "marketweb.settings"`` (the old monolithic
module). To preserve them without a sweeping edit, this package's
``__init__`` re-exports the dev module by default:

    from .dev import *  # noqa: F401,F403

That means importing ``marketweb.settings`` continues to behave like the
old dev-flavored monolith. New code (and the entry points updated by
this Sprint) targets ``marketweb.settings.dev`` or
``marketweb.settings.prod`` explicitly.
"""
from __future__ import annotations

# Re-export the dev profile so legacy entry points that import
# ``marketweb.settings`` directly keep working without changes.
from .dev import *  # noqa: F401,F403
