"""Admin registrations for the audit log surfaces (T31).

Exposes two read-only admins so operators can answer the
"who-did-what-when" questions from the standard ``/admin/`` UI:

  - ``LogEntry`` (Django built-in) — automatic admin-site action
    history. Django writes to this transparently whenever a
    ``ModelAdmin`` add/change/delete is performed. Pre-T31 the
    table existed but was not navigable.
  - ``AuditLogEntry`` (T31, defined in ``apps.core.models``) —
    project-side audit log driven by post-save / post-delete
    signals on the small set of TRACKED_MODELS. Captures BOTH
    admin-site actions AND programmatic mutations (services-layer,
    management commands).

Both admins are read-only — including for superusers. The intent
is "tamper-resistant by default". Deleting an audit row requires
either a direct DB statement or temporarily removing the
``has_delete_permission = lambda *a, **kw: False`` override.
"""
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from apps.core.models import AuditLogEntry


# ---------------------------------------------------------------------------
# AuditLogEntry · T31 audit feed for sensitive models
# ---------------------------------------------------------------------------

@admin.register(AuditLogEntry)
class AuditLogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "timestamp",
        "actor_repr",
        "action",
        "target_content_type",
        "target_repr",
        "request_ip",
    )
    list_filter = ("action", "target_content_type", "timestamp")
    search_fields = ("actor_repr", "target_repr", "target_object_id", "request_ip")
    date_hierarchy = "timestamp"
    ordering = ("-timestamp",)

    # The audit table is append-only by design. No add / change /
    # delete from the admin UI — view-only via has_view_permission
    # so the changelist + detail render WITHOUT save buttons.
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        # Any authenticated staff member can READ the audit log.
        # The change form renders in read-only mode (no save buttons)
        # because has_change_permission is False.
        return request.user.is_authenticated and request.user.is_staff

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields] + ["target"]

    def save_model(self, request, obj, form, change):  # pragma: no cover
        # Belt-and-braces: even if has_change_permission is ever
        # relaxed, the admin save path stays read-only.
        raise PermissionError(
            "AuditLogEntry is append-only and cannot be modified from the admin."
        )


# ---------------------------------------------------------------------------
# LogEntry · Django built-in admin-site action history
# ---------------------------------------------------------------------------

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "action_time",
        "user",
        "content_type",
        "object_repr",
        "action_flag",
        "change_message",
    )
    list_filter = ("action_flag", "content_type", "action_time")
    search_fields = ("user__username", "object_repr", "change_message")
    date_hierarchy = "action_time"
    ordering = ("-action_time",)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_authenticated and request.user.is_staff

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]
