from django.contrib import admin

from apps.projects.models import (
    CustomerProject,
    ProjectContent,
    ProjectDesignTokens,
    ProjectRevision,
)


class ProjectContentInline(admin.TabularInline):
    model = ProjectContent
    extra = 0
    fields = ("key_path", "value_json", "updated_at")
    readonly_fields = ("updated_at",)


class ProjectDesignTokensInline(admin.StackedInline):
    model = ProjectDesignTokens
    extra = 0
    can_delete = False


@admin.register(CustomerProject)
class CustomerProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "source_template", "status", "locale", "updated_at")
    list_filter = ("status", "locale", "source_category_slug")
    search_fields = ("name", "owner__username", "source_template__slug")
    readonly_fields = ("uuid", "created_at", "updated_at", "last_published_at")
    inlines = [ProjectDesignTokensInline, ProjectContentInline]


@admin.register(ProjectRevision)
class ProjectRevisionAdmin(admin.ModelAdmin):
    list_display = ("project", "reason", "label", "created_by", "created_at")
    list_filter = ("reason",)
    search_fields = ("project__name", "label")
    readonly_fields = ("snapshot", "created_at", "updated_at")
