"""
ASGI config for marketweb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Sprint 0 · T1+T2+T3: ASGI defaults to the prod profile (same
# rationale as wsgi.py). Override via env when running locally
# under daphne/uvicorn for debugging.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketweb.settings.prod')

application = get_asgi_application()
