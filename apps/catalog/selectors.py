from django.db.models import Count, QuerySet
from django.shortcuts import get_object_or_404

from apps.catalog.models import Category, WebTemplate


def get_active_categories() -> QuerySet[Category]:
    return Category.objects.filter(is_active=True)


def get_active_categories_with_counts() -> QuerySet[Category]:
    return (
        Category.objects.filter(is_active=True)
        .annotate(template_count=Count("templates", filter=__published_filter()))
    )


def get_published_templates() -> QuerySet[WebTemplate]:
    return (
        WebTemplate.objects.filter(status=WebTemplate.Status.PUBLISHED)
        .select_related("category", "brand")
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


def __published_filter():
    from django.db.models import Q
    return Q(templates__status=WebTemplate.Status.PUBLISHED)
