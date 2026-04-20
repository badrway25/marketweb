from django.db.models import Count, Prefetch, Q, QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from apps.catalog.models import (
    Category,
    ProfessionCluster,
    TemplateAsset,
    VisualStyle,
    WebTemplate,
)


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
    cluster_slugs: list[str] | None = None,
    style_slugs: list[str] | None = None,
    price_tiers: list[str] | None = None,
    feature_flags: list[str] | None = None,
    use_case_slugs: list[str] | None = None,
    audience_slugs: list[str] | None = None,
) -> tuple[Category | None, QuerySet[WebTemplate]]:
    """Filtered, searched, and sorted templates for the listing page.

    Backward-compatible: existing callers that pass only the legacy
    kwargs (``category_slug``, ``search_query``, ``sort_by``,
    ``include_drafts``) get identical behaviour. X.2 adds six new
    keyword-only filters driven by the taxonomy v2 metadata:

    - ``cluster_slugs``   — profession cluster filter (OR-join)
    - ``style_slugs``     — visual style filter (OR-join)
    - ``price_tiers``     — price tier filter (OR-join)
    - ``feature_flags``   — boolean feature filter (AND-join · every
      flag must be True on the matching row)
    - ``use_case_slugs``  — JSONField ``__contains`` match (AND-join)
    - ``audience_slugs``  — JSONField ``__contains`` match (AND-join)

    ``feature_flags`` accepts string names from ``FEATURE_FLAG_LABELS``
    (the allowed set below). Unknown names are silently dropped to
    keep URL-driven filters resilient to typos without 500-ing.
    """
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
            | Q(search_keywords__icontains=search_query)
            | Q(profession_cluster__name__icontains=search_query)
        )

    if cluster_slugs:
        qs = qs.filter(profession_cluster__slug__in=cluster_slugs)
    if style_slugs:
        qs = qs.filter(visual_style__slug__in=style_slugs)
    if price_tiers:
        qs = qs.filter(price_tier__in=price_tiers)
    if feature_flags:
        # Only flags declared in FEATURE_FLAG_LABELS are honored;
        # unknown names are dropped silently.
        for flag in feature_flags:
            if flag in FEATURE_FLAG_LABELS:
                qs = qs.filter(**{flag: True})
    if use_case_slugs:
        qs = _filter_json_list_and(qs, "use_cases", use_case_slugs)
    if audience_slugs:
        qs = _filter_json_list_and(qs, "audience", audience_slugs)

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


# ── X.2 Commit 4 · taxonomy discovery helpers ─────────────────────


def _filter_json_list_and(
    qs: QuerySet[WebTemplate],
    field_name: str,
    required_values: list[str],
) -> QuerySet[WebTemplate]:
    """Portable AND-join filter for JSON list fields.

    PostgreSQL JSONField supports ``__contains`` natively; SQLite does
    not (``NotSupportedError`` at query compile). The catalog runs the
    MVP on PostgreSQL in production but on SQLite for the test suite,
    so X.2 Commit 4 uses a Python-side filter: fetch the filtered base
    queryset's ids + JSON field, then narrow the queryset to ids that
    carry every required value. For the current catalog (20 rows · 200
    target) this stays well under a 100ms budget; a future Wave 3+
    optimization can swap in a native DB lookup behind the same helper
    signature without touching callers.
    """
    if not required_values:
        return qs
    required = set(required_values)
    matched_ids = [
        row["id"]
        for row in qs.values("id", field_name)
        if required.issubset(set(row[field_name] or []))
    ]
    return qs.filter(id__in=matched_ids)




# Feature flags exposed as a discovery facet. Keys are the model field
# names (used verbatim in ``filter(**{flag: True})``); values are the
# IT-locale labels rendered in the sidebar. Central constant so the
# view + facet counts + filter validation share one source of truth.
FEATURE_FLAG_LABELS: dict[str, str] = {
    "has_shop":     "Shop / ecommerce",
    "has_booking":  "Prenotazioni",
    "has_portfolio": "Portfolio",
    "has_blog":     "Blog / journal",
    "has_video":    "Video",
    "has_rtl":      "Lingua araba (RTL)",
    "is_multi_page": "Multi-pagina",
}


# Hardcoded role discovery map: slug → ordered tuple of cluster slugs
# the role spans. Used by ``/templates/for-role/<slug>/`` and by the
# homepage role-grid (Commit 5). Kept as a module-level constant — no
# new model table — per the X.2 plan (minimal metadata model first).
ROLE_DISCOVERY: dict[str, dict] = {
    "avvocati": {
        "label": "Per avvocati",
        "description": "Studi legali tradizionali, moderni, notai e commercialisti.",
        "clusters": ("classic-law", "modern-law-tech", "notary-commercialista"),
    },
    "medici": {
        "label": "Per medici",
        "description": "Specialisti, cliniche, wellness, pediatria, dentisti, veterinari.",
        "clusters": (
            "specialist", "multi-clinic", "wellness-holistic",
            "family-pediatric", "dental", "veterinary",
        ),
    },
    "ristoratori": {
        "label": "Per ristoratori",
        "description": "Dal fine dining alla trattoria, dal bar al bakery.",
        "clusters": (
            "fine-dining", "trattoria", "street-casual",
            "bar-bistrot", "bakery-pasticceria",
        ),
    },
    "startup": {
        "label": "Per startup",
        "description": "Landing SaaS, prodotti tech, growth studio e corporate.",
        "clusters": ("saas-landing", "digital-growth", "corporate"),
    },
    "fotografi": {
        "label": "Per fotografi",
        "description": "Portfolio cinematic per fotografi di moda, architettura, fine-art.",
        "clusters": ("photographer", "videomaker"),
    },
    "designer": {
        "label": "Per designer",
        "description": "Portfolio editoriali per graphic designer, art director, illustratori.",
        "clusters": ("designer-editorial", "illustrator", "creative"),
    },
    "artigiani": {
        "label": "Per artigiani",
        "description": "Atelier, botteghe, maker e artigiani con vendita online.",
        "clusters": ("artisan-workshop", "jewelry"),
    },
    "ecommerce": {
        "label": "Per negozi online",
        "description": "Atelier artigiani, maison fashion, boutique vino e gioielli.",
        "clusters": (
            "artisan-workshop", "fashion-editorial",
            "wine-food-boutique", "jewelry",
        ),
    },
    "agenzie": {
        "label": "Per agenzie",
        "description": "Agenzie creative, digital, PR, studi indipendenti.",
        "clusters": ("creative", "digital-growth", "pr-comms", "freelance"),
    },
    "immobiliari": {
        "label": "Per agenzie immobiliari",
        "description": "Immobiliare mass-market, luxury, commerciale.",
        "clusters": (
            "real-estate-mass-market",
            "real-estate-luxury",
            "real-estate-commercial",
        ),
    },
}


# Use-case discovery index. Populated as a mapping of slug → (label,
# description) so ``/templates/for-use-case/<slug>/`` can resolve a
# pretty label without a new model. The underlying match is a
# ``WebTemplate.use_cases`` JSONField ``__contains`` lookup — same as
# the listing-page filter.
USE_CASE_DISCOVERY: dict[str, dict] = {
    "sell-online": {
        "label": "Vendere online",
        "description": "Template con shop integrato, carrello e pagina prodotto editoriale.",
    },
    "reservations": {
        "label": "Prendere prenotazioni",
        "description": "Ristoranti, wellness e attività con booking integrato.",
    },
    "appointment-booking": {
        "label": "Gestire appuntamenti medici",
        "description": "Studi medici, cliniche e specialisti con prenotazione visita.",
    },
    "consultation-booking": {
        "label": "Prenotare consulenze",
        "description": "Avvocati, commercialisti, coach con form di richiesta consulenza.",
    },
    "show-portfolio": {
        "label": "Mostrare portfolio",
        "description": "Designer, fotografi, agenzie con portfolio cinematografico.",
    },
    "generate-leads": {
        "label": "Generare lead qualificati",
        "description": "Agenzie, B2B, SaaS con funnel di lead capture.",
    },
    "menu-online": {
        "label": "Pubblicare menu digitale",
        "description": "Ristoranti, pizzerie, bakery con menu multipagina.",
    },
    "property-listings": {
        "label": "Mostrare immobili",
        "description": "Agenzie immobiliari con listing, filtri e schede proprietà.",
    },
    "product-launch": {
        "label": "Lanciare un prodotto",
        "description": "Landing SaaS e lancio prodotto con pricing chiaro e demo.",
    },
    "brand-storytelling": {
        "label": "Raccontare un brand",
        "description": "Template editoriali per raccontare storia, valori, metodo.",
    },
}


def get_templates_by_cluster(
    cluster_slug: str,
    include_drafts: bool = False,
) -> tuple[ProfessionCluster, QuerySet[WebTemplate]]:
    """Resolve a profession cluster and its published templates.

    Mirrors ``get_templates_by_category`` but at the cluster
    granularity. 404s on unknown or inactive clusters.
    """
    cluster = get_object_or_404(
        ProfessionCluster, slug=cluster_slug, is_active=True
    )
    templates = get_published_templates(include_drafts).filter(
        profession_cluster=cluster
    )
    return cluster, templates


def get_templates_by_role(
    role_slug: str,
    include_drafts: bool = False,
) -> tuple[dict, QuerySet[WebTemplate]]:
    """Resolve a role-discovery slug to its label + templates queryset.

    The role slug indexes ``ROLE_DISCOVERY``; the resolved cluster list
    is used to filter the published queryset (OR-join across clusters).
    404s on unknown roles.
    """
    role = ROLE_DISCOVERY.get(role_slug)
    if role is None:
        raise Http404(f"Unknown role: {role_slug!r}.")
    templates = get_published_templates(include_drafts).filter(
        profession_cluster__slug__in=role["clusters"]
    )
    return {"slug": role_slug, **role}, templates


def get_templates_by_use_case(
    use_case_slug: str,
    include_drafts: bool = False,
) -> tuple[dict, QuerySet[WebTemplate]]:
    """Resolve a use-case discovery slug to its label + templates.

    The use-case slug indexes ``USE_CASE_DISCOVERY`` for the label +
    description; the underlying match is a ``use_cases__contains``
    lookup on the WebTemplate JSONField. 404s on unknown use cases.
    """
    use_case = USE_CASE_DISCOVERY.get(use_case_slug)
    if use_case is None:
        raise Http404(f"Unknown use case: {use_case_slug!r}.")
    base_qs = get_published_templates(include_drafts)
    templates = _filter_json_list_and(base_qs, "use_cases", [use_case_slug])
    return {"slug": use_case_slug, **use_case}, templates


def get_facet_counts(qs: QuerySet[WebTemplate]) -> dict:
    """Aggregate facet counts for the current filtered queryset.

    Keeps the shape minimal and deterministic: one dict per facet
    group, keyed by slug/name, valued by row count. The sidebar
    consumes this directly to render `(42)` counts next to each filter
    option.

    Feature flags use the model-field names as keys (``has_shop``,
    ``has_booking``, ...); clusters + styles use slugs; price tiers
    use the string-choice values (``free`` / ``standard`` / ``premium``).
    """
    # ``order_by()`` is stripped before ``values().annotate()`` because
    # any ordering column is otherwise appended to GROUP BY, which
    # over-splits the aggregation buckets (e.g. a cluster with 2 rows
    # ordered by created_at would report 2 × count=1 instead of
    # 1 × count=2).
    base = qs.order_by()
    cluster_counts = {
        row["profession_cluster__slug"]: row["n"]
        for row in base.exclude(profession_cluster__isnull=True)
        .values("profession_cluster__slug")
        .annotate(n=Count("id"))
    }
    style_counts = {
        row["visual_style__slug"]: row["n"]
        for row in base.exclude(visual_style__isnull=True)
        .values("visual_style__slug")
        .annotate(n=Count("id"))
    }
    price_counts = {
        row["price_tier"]: row["n"]
        for row in base.exclude(price_tier__isnull=True)
        .values("price_tier")
        .annotate(n=Count("id"))
    }
    feature_counts = {
        flag: qs.filter(**{flag: True}).count()
        for flag in FEATURE_FLAG_LABELS
    }
    return {
        "clusters": cluster_counts,
        "styles":   style_counts,
        "price_tiers": price_counts,
        "features": feature_counts,
        "total": qs.count(),
    }


def search_templates_typeahead(
    q: str,
    limit: int = 8,
    include_drafts: bool = False,
) -> dict:
    """Deterministic typeahead response for the hero search bar.

    Returns three pools (templates / clusters / roles) · each limited
    to ``limit`` rows · matched via ILIKE (``__icontains``) on the
    canonical search surfaces:

    - ``WebTemplate``: ``name``, ``search_keywords``, ``brand.brand_name``
    - ``ProfessionCluster``: ``name``, ``search_aliases``
    - ``ROLE_DISCOVERY``: ``label`` (Python substring · case-insensitive)

    Empty or single-char ``q`` returns empty pools — the client-side
    typeahead ignores these responses rather than surfacing everything.
    """
    out = {"q": q, "templates": [], "clusters": [], "roles": []}
    q = (q or "").strip()
    if len(q) < 2:
        return out

    tpl_qs = (
        get_published_templates(include_drafts)
        .filter(
            Q(name__icontains=q)
            | Q(search_keywords__icontains=q)
            | Q(brand__brand_name__icontains=q)
            | Q(profession_cluster__name__icontains=q)
            | Q(profession_cluster__search_aliases__icontains=q)
        )
        .distinct()
        .select_related("category", "profession_cluster")[:limit]
    )
    out["templates"] = [
        {
            "slug": t.slug,
            "name": t.name,
            "cluster": t.profession_cluster.name if t.profession_cluster else None,
            "category": t.category.slug,
            "detail_url": f"/templates/{t.category.slug}/{t.slug}/",
        }
        for t in tpl_qs
    ]

    cluster_qs = (
        ProfessionCluster.objects.filter(is_active=True)
        .filter(Q(name__icontains=q) | Q(search_aliases__icontains=q))
        .select_related("category")[:limit]
    )
    out["clusters"] = [
        {
            "slug": c.slug,
            "name": c.name,
            "category": c.category.slug,
            "detail_url": f"/templates/clusters/{c.slug}/",
        }
        for c in cluster_qs
    ]

    q_lower = q.lower()
    out["roles"] = [
        {
            "slug": rslug,
            "label": r["label"],
            "detail_url": f"/templates/for-role/{rslug}/",
        }
        for rslug, r in ROLE_DISCOVERY.items()
        if q_lower in r["label"].lower() or q_lower in rslug
    ][:limit]

    return out


def get_all_visual_styles() -> QuerySet[VisualStyle]:
    """Return active visual styles ordered for the sidebar facet."""
    return VisualStyle.objects.filter(is_active=True)


def get_active_profession_clusters() -> QuerySet[ProfessionCluster]:
    """Return active profession clusters for facet + discovery pages."""
    return ProfessionCluster.objects.filter(is_active=True).select_related("category")
