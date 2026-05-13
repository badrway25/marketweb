# Sprint 0 · T5 · Docker baseline (single-stage, intentionally simple).
#
# Goal of this image: a working production-shaped runtime — gunicorn
# behind whatever the deploy puts in front of it (nginx / Traefik /
# load balancer that terminates TLS and forwards X-Forwarded-Proto).
# Defaults match the prod settings module (`marketweb.settings.prod`)
# wired in `marketweb/wsgi.py` by Sprint 0 · T1+T2+T3.
#
# What this image is NOT:
# - A multi-stage / distroless / scratch image (premature optimisation
#   for a project this size; revisit when the image cost matters).
# - A full DevOps platform (no s6-overlay / supervisord / cron baked
#   in — celery + celery-beat are present in the codebase but Sprint
#   2 scope per `marketweb/settings/prod.py:21-24`).
# - The dev environment (use `manage.py runserver` directly with the
#   dev settings — same `requirements.txt`, no container needed).
#
# Local usage (smoke):
#   docker build -t marketweb:dev .
#   docker run --rm -p 8000:8000 \
#     -e DJANGO_SETTINGS_MODULE=marketweb.settings.dev \
#     marketweb:dev python manage.py runserver 0.0.0.0:8000
#
# Compose usage (prod-shaped local stack):
#   cp .env.example .env  # fill DJANGO_SECRET_KEY + DB_*
#   docker compose up --build

FROM python:3.13-slim AS app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# System libs needed at *runtime* by the wheels we install:
#   - libjpeg62-turbo + zlib1g · Pillow image decoders
# psycopg[binary] bundles libpq inside its wheel — no libpq-dev needed
# at build time, no libpq5 needed at runtime.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libjpeg62-turbo \
        zlib1g \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Cache-friendly: deps install layer is invalidated only when
# requirements.txt changes.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# App code last so a code-only edit re-uses the deps layer.
COPY . .

# T22 · collectstatic at build time so the image ships with
# /app/staticfiles/ pre-populated (plus .gz precompressed variants
# from WhiteNoise's CompressedStaticFilesStorage). Run under the
# prod profile so the WhiteNoise storage backend wired in
# marketweb/settings/prod.py is the one actually used.
#
# The synthetic env below is ONLY enough to make `marketweb.settings.prod`
# importable at build time (the prod profile raises ImproperlyConfigured
# on missing SECRET_KEY / ALLOWED_HOSTS / CSRF_TRUSTED_ORIGINS). The
# values are throwaway and never reach runtime.
RUN DJANGO_SETTINGS_MODULE=marketweb.settings.prod \
    DJANGO_SECRET_KEY=collectstatic-build-time-throwaway-key \
    DJANGO_ALLOWED_HOSTS=build.localhost \
    DJANGO_CSRF_TRUSTED_ORIGINS=https://build.localhost \
    DJANGO_ALLOW_SQLITE_PROD=1 \
    DJANGO_SECURE_SSL_REDIRECT=0 \
    DJANGO_SECURE_HSTS_SECONDS=0 \
    python manage.py collectstatic --noinput --clear

# Non-root user — small but correct hygiene.
RUN useradd --create-home --uid 1000 app \
    && chown -R app:app /app
USER app

EXPOSE 8000

# Default entrypoint: gunicorn with the prod profile (per wsgi.py).
# Override with `docker run … python manage.py …` for one-offs.
CMD ["gunicorn", "marketweb.wsgi:application", \
     "--bind=0.0.0.0:8000", \
     "--workers=3", \
     "--access-logfile=-", \
     "--error-logfile=-"]
