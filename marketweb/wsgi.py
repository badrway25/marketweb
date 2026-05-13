"""
WSGI config for marketweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Sprint 0 · T1+T2+T3: WSGI defaults to the prod profile because
# every real deployment goes through this entry point. The dev
# profile is reserved for `manage.py runserver`. Override via env
# only for atypical setups (e.g. running the WSGI app under a dev
# WSGI server like werkzeug for debugging).
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketweb.settings.prod')

application = get_wsgi_application()
