#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Sprint 0 · T1+T2+T3: settings split. The default profile for
    # `manage.py` (runserver, makemigrations, migrate, test, ...) is
    # the dev profile so a fresh checkout works without env setup.
    # Override at the shell level when needed:
    #   $env:DJANGO_SETTINGS_MODULE = "marketweb.settings.prod"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketweb.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
