from django.db.models import Count, Prefetch, Q, QuerySet
from django.shortcuts import get_object_or_404

from apps.catalog.models import Category, TemplateAsset, WebTemplate


def get_active_categories() -> QuerySet[Category]:
    return Category.objects.filter(is_active=True)


def get_active_categories_with_counts() -> QuerySet[Category]:
    return (
        Category.objects.filter(is_active=True)
        .annotate(template_count=Count("templates", filter=_published_filter()))
    )


def _preview_only_prefetch() -> Prefetch:
    """Prefetch only the canonical preview assets — smaller payload than
    prefetching every asset kind, and it drops straight into
    ``WebTemplate.preview_asset`` (which iterates the prefetched cache)."""
    return Prefetch(
        "assets",
        queryset=TemplateAsset.objects.filter(
            asset_type=TemplateAsset.AssetType.PREVIEW
        ).order_by("order", "pk"),
    )


def get_published_templates() -> QuerySet[WebTemplate]:
    return (
        WebTemplate.objects.filter(status=WebTemplate.Status.PUBLISHED)
        .select_related("category", "brand")
        .prefetch_related(_preview_only_prefetch())
    )


def get_featured_templates(limit: int = 6) -> QuerySet[WebTemplate]:
    return get_published_templates().filter(featured=True)[:limit]


def get_templates_by_category(category_slug: str) -> tuple[Category, QuerySet[WebTemplate]]:
    category = get_object_or_404(Category, slug=category_slug, is_active=True)
    templates = get_published_templates().filter(category=category)
    return category, templates


def get_template_detail(category_slug: str, template_slug: str) -> WebTemplate:
    return get_object_or_404(
        WebTemplate.objects.select_related("category", "brand").prefetch_related("tags", "assets"),
        slug=template_slug,
        category__slug=category_slug,
        status=WebTemplate.Status.PUBLISHED,
    )


def get_related_templates(template: WebTemplate, limit: int = 3) -> QuerySet[WebTemplate]:
    return (
        get_published_templates()
        .filter(category=template.category)
        .exclude(pk=template.pk)[:limit]
    )


# ── Listing page: combined search / sort / filter ──────────────

SORT_OPTIONS = {
    "recent": "-created_at",
    "price_asc": "price",
    "price_desc": "-price",
    "name": "name",
}

SORT_LABELS = {
    "recent": "Più Recenti",
    "price_asc": "Prezzo: basso → alto",
    "price_desc": "Prezzo: alto → basso",
    "name": "Nome A–Z",
}


def get_listing_templates(
    *,
    category_slug: str | None = None,
    search_query: str | None = None,
    sort_by: str = "recent",
) -> tuple[Category | None, QuerySet[WebTemplate]]:
    """Filtered, searched, and sorted templates for the listing page."""
    qs = get_published_templates()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug, is_active=True)
        qs = qs.filter(category=category)

    if search_query:
        qs = qs.filter(
            Q(name__icontains=search_query)
            | Q(short_description__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(brand__brand_name__icontains=search_query)
        )

    order_field = SORT_OPTIONS.get(sort_by, "-created_at")
    qs = qs.order_by(order_field)

    return category, qs


def _published_filter():
    return Q(templates__status=WebTemplate.Status.PUBLISHED)
