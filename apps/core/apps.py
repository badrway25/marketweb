from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
    verbose_name = "Core"

    def ready(self):
        # T31 · wire the audit log signal receivers after the app
        # registry is fully populated. ``apps.core.audit`` imports
        # models lazily so this hook is safe inside ready().
        from apps.core import audit
        audit.connect_signals()
