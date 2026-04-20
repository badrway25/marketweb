from django.contrib import admin

from apps.catalog.models import (
    Category,
    ProfessionCluster,
    Tag,
    TemplateAsset,
    TemplateBrand,
    VisualStyle,
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


@admin.register(ProfessionCluster)
class ProfessionClusterAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "slug", "order", "is_active", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("name", "slug", "search_aliases")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order", "is_active")
    list_select_related = ("category",)


@admin.register(VisualStyle)
class VisualStyleAdmin(admin.ModelAdmin):
    list_display = (
        "label",
        "slug",
        "palette_family",
        "typography_stack",
        "density_profile",
        "badge",
        "order",
        "is_active",
    )
    list_filter = ("palette_family", "typography_stack", "is_active")
    search_fields = ("slug", "label", "palette_family", "typography_stack")
    list_editable = ("order", "is_active")


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
        "profession_cluster",
        "visual_style",
        "price_tier",
        "tier",
        "status",
        "featured",
        "order",
    )
    list_filter = (
        "tier",
        "status",
        "category",
        "profession_cluster",
        "visual_style",
        "price_tier",
        "has_shop",
        "has_booking",
        "has_portfolio",
        "has_rtl",
        "is_multi_page",
        "is_free",
        "featured",
    )
    search_fields = ("name", "slug", "description", "search_keywords")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("tier", "status", "featured", "order")
    list_select_related = ("category", "profession_cluster", "visual_style")
    filter_horizontal = ("tags",)
    inlines = [TemplateBrandInline, TemplateAssetInline]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "category",
                    "description",
                    "short_description",
                ),
            },
        ),
        (
            "Catalog taxonomy (X.2)",
            {
                "fields": (
                    "profession_cluster",
                    "visual_style",
                    "price_tier",
                    "audience",
                    "use_cases",
                    "search_keywords",
                ),
                "description": (
                    "Additive taxonomy + search metadata introduced in X.2 "
                    "Commit 1. Nullable during the backfill window; "
                    "`profession_cluster` and `visual_style` will be "
                    "flipped to required in a later commit once Commit 3 "
                    "backfill validates across environments."
                ),
            },
        ),
        (
            "Feature facets (X.2)",
            {
                "fields": (
                    "has_shop",
                    "has_booking",
                    "has_portfolio",
                    "has_blog",
                    "has_video",
                    "has_rtl",
                    "is_multi_page",
                ),
            },
        ),
        (
            "Public tier + status",
            {
                "fields": ("tier", "status", "featured", "order"),
            },
        ),
        (
            "Commerce + preview",
            {
                "fields": (
                    "price",
                    "is_free",
                    "preview_url",
                    "demo_url",
                    "tags",
                ),
            },
        ),
    )


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
