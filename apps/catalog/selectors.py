from django.db.models import Count, Prefetch, Q, QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.catalog.models import Category, TemplateAsset, WebTemplate


# ── Tier gate (D-055, Session 20) ───────────────────────────────
#
# Every public-facing selector routes through ``_public_tier_filter`` so
# the live/draft cut is enforced in exactly one place. Views pass
# ``include_drafts=True`` only when the caller has already authenticated
# as staff AND opted in via ``?preview=1`` — see ``_staff_preview_mode``
# in ``apps.catalog.views``. Non-staff requests can never reach the
# draft slice.

PUBLIC_TIER = WebTemplate.Tier.PUBLISHED_LIVE


def _public_tier_filter(include_drafts: bool = False) -> Q:
    """Q expression that gates a queryset on the public tier rule.

    Combines the legacy ``status='published'`` gate with the new
    ``tier='published_live'`` gate from D-055. Passing
    ``include_drafts=True`` relaxes ONLY the tier gate — the
    ``status='published'`` gate still applies so archived or review
    templates never leak through the staff preview path.
    """
    q = Q(status=WebTemplate.Status.PUBLISHED)
    if not include_drafts:
        q &= Q(tier=PUBLIC_TIER)
    return q


def get_active_categories() -> QuerySet[Category]:
    return Category.objects.filter(is_active=True)


def get_active_categories_with_counts(
    include_drafts: bool = False,
) -> QuerySet[Category]:
    """Categories with a `template_count` annotation honoring the tier gate.

    When ``include_drafts`` is False (the default) the count reflects
    ONLY templates visible in the public catalog — a category whose
    only sibling is ``draft`` reports zero, which is exactly the
    signal the empty-state UI needs.
    """
    return Category.objects.filter(is_active=True).annotate(
        template_count=Count(
            "templates",
            filter=_published_filter(include_drafts=include_drafts),
        )
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


def get_published_templates(
    include_drafts: bool = False,
) -> QuerySet[WebTemplate]:
    return (
        WebTemplate.objects.filter(_public_tier_filter(include_drafts))
        .select_related("category", "brand")
        .prefetch_related(_preview_only_prefetch())
    )


def get_featured_templates(
    limit: int = 6, include_drafts: bool = False
) -> list[WebTemplate]:
    """Homepage featured pool.

    Prefers templates explicitly flagged ``featured=True``, but always
    backfills the remaining slots from the rest of the live pool
    (ordered by ``-featured, order, -created_at`` per the model Meta)
    up to ``limit``. This keeps the homepage from visibly shrinking to
    a single card during the tier migration: the live pool is already
    curated by the D-055 gate, so every published_live template is
    worth a slot when featured ones run short.
    """
    live = get_published_templates(include_drafts)
    featured_pool = list(live.filter(featured=True)[:limit])
    if len(featured_pool) >= limit:
        return featured_pool

    seen = {t.pk for t in featured_pool}
    backfill = live.exclude(pk__in=seen)[: limit - len(featured_pool)]
    return featured_pool + list(backfill)


def get_templates_by_category(
    category_slug: str, include_drafts: bool = False
) -> tuple[Category, QuerySet[WebTemplate]]:
    category = get_object_or_404(Category, slug=category_slug, is_active=True)
    templates = get_published_templates(include_drafts).filter(category=category)
    return category, templates


def get_template_detail(
    category_slug: str,
    template_slug: str,
    include_drafts: bool = False,
) -> WebTemplate:
    """Fetch a template by (category_slug, slug), honoring the tier gate.

    Draft templates 404 on public access — the binary gate from D-055
    applies here identically to listing pages. Raising ``Http404``
    manually keeps the behaviour identical to the previous
    ``get_object_or_404`` call whether the slug is missing, archived,
    or draft.
    """
    qs = (
        WebTemplate.objects.select_related("category", "brand")
        .prefetch_related("tags", "assets")
        .filter(_public_tier_filter(include_drafts))
        .filter(slug=template_slug, category__slug=category_slug)
    )
    obj = qs.first()
    if obj is None:
        raise Http404("Template not found.")
    return obj


def get_related_templates(
    template: WebTemplate, limit: int = 3, include_drafts: bool = False
) -> QuerySet[WebTemplate]:
    return (
        get_published_templates(include_drafts)
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
    include_drafts: bool = False,
) -> tuple[Category | None, QuerySet[WebTemplate]]:
    """Filtered, searched, and sorted templates for the listing page."""
    qs = get_published_templates(include_drafts)
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


def _published_filter(include_drafts: bool = False):
    """Relation-traversal version of ``_public_tier_filter`` used by
    the Count annotation on Category (filters ``templates__status`` /
    ``templates__tier``)."""
    q = Q(templates__status=WebTemplate.Status.PUBLISHED)
    if not include_drafts:
        q &= Q(templates__tier=PUBLIC_TIER)
    return q
