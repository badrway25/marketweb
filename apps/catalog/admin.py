from django.contrib import admin

from apps.catalog.models import (
    Category,
    Tag,
    TemplateAsset,
    TemplateBrand,
    WebTemplate,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order", "is_active")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class TemplateBrandInline(admin.StackedInline):
    model = TemplateBrand
    extra = 0
    max_num = 1


class TemplateAssetInline(admin.TabularInline):
    model = TemplateAsset
    extra = 1
    fields = ("file", "asset_type", "alt_text", "order")


@admin.register(WebTemplate)
class WebTemplateAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "tier",
        "status",
        "price",
        "is_free",
        "featured",
        "order",
        "created_at",
    )
    list_filter = ("tier", "status", "category", "is_free", "featured")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("tier", "status", "featured", "order")
    filter_horizontal = ("tags",)
    inlines = [TemplateBrandInline, TemplateAssetInline]


@admin.register(TemplateBrand)
class TemplateBrandAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "template", "tagline", "personality")
    search_fields = ("brand_name", "template__name")
    list_filter = ("personality",)


@admin.register(TemplateAsset)
class TemplateAssetAdmin(admin.ModelAdmin):
    list_display = ("template", "asset_type", "order", "created_at")
    list_filter = ("asset_type",)
    search_fields = ("template__name", "alt_text")
