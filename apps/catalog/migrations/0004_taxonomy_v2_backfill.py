"""Data migration · backfill taxonomy v2 metadata on the 20 MVP templates.

X.2 Commit 3. The preceding schema migration (0003) added nullable FKs
(``profession_cluster``, ``visual_style``) plus the additive metadata
columns (``use_cases``, ``audience``, ``price_tier``, ``search_keywords``,
``has_shop``, ``has_booking``, ``has_portfolio``, ``has_blog``,
``has_video``, ``has_rtl``, ``is_multi_page``). This migration populates
those columns for every one of the 20 MVP templates in the catalog.

**Execution contract.**

On a freshly-migrated empty database (CI test DB, local clean env) this
migration runs with zero ``WebTemplate`` rows — nothing to backfill —
and exits cleanly. Seed data lands afterwards via the idempotent
``seed_categories`` → ``seed_visual_styles`` → ``seed_profession_clusters``
→ ``seed_templates`` chain; the latter now carries the same taxonomy v2
metadata inline (see ``seed_templates.TEMPLATE_METADATA``), so fresh
seeds produce the same end-state as a backfilled existing DB.

On an existing database (the current production-like baseline that
already carries the 20 MVP ``WebTemplate`` rows created before X.2
landed), this migration resolves the 20 slugs in ``TEMPLATE_METADATA``
below, loads the associated ``ProfessionCluster`` / ``VisualStyle``
rows by slug, and writes the full metadata bundle on each row. The
``WebTemplate.category`` FK is intentionally left untouched — it is
preserved across the backfill so existing URL patterns and selectors
keep working without a reseed.

**Fail-loud contract.** Cluster + style slugs are resolved with an
explicit ``.get()`` lookup; if a seed row is missing (typically because
``seed_visual_styles`` or ``seed_profession_clusters`` has not yet been
run), the migration raises and the backfill aborts rather than silently
landing NULL FKs. This is deliberate — nullable-first is honored at the
schema level, but the backfill itself must be all-or-nothing per
template row.

**Reversibility.** A reverse migration resets ``profession_cluster`` and
``visual_style`` to NULL, clears ``price_tier``, and resets the seven
boolean feature-flag columns to their model defaults (``False``). The
JSON-list fields (``use_cases``, ``audience``) revert to ``[]``;
``search_keywords`` reverts to ``""``. This keeps the schema migration
0003 standalone-rollbackable without dropping additive columns.
"""

from django.db import migrations


# ── 20 MVP templates · exact taxonomy v2 mapping ───────────────────
#
# This dict is the canonical backfill table for the 20 ``published_live``
# templates seeded by ``seed_templates``. The same mapping is embedded
# in the ``seed_templates`` command under ``TEMPLATE_METADATA`` so
# fresh seeds produce identical state. The two definitions are kept in
# sync by ``test_backfill_dict_and_seed_templates_dict_match`` in the
# catalog test suite.
#
# ``cluster``  — slug in ``ProfessionCluster``
# ``style``    — slug in ``VisualStyle``
# ``price_tier`` — choice in ``WebTemplate.PriceTier``
# Feature flags reflect the current skin behavior (Session 36 media
# hardening + Session 47 Pexels adoption) at the X.2 baseline.

TEMPLATE_METADATA = {
    "vertex-creative-agency": {
        "cluster": "creative",
        "style": "editorial-warm",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "generate-leads", "brand-identity"],
        "audience": ["agency", "studio"],
        "search_keywords": (
            "agenzia creativa brand design portfolio case-study studio creative"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "aura-digital-studio": {
        "cluster": "digital-growth",
        "style": "dashboard-dark",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "generate-leads", "growth-tech"],
        "audience": ["agency", "studio"],
        "search_keywords": (
            "agenzia digital growth performance sprint studio tech midnight"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "pragma-corporate-suite": {
        "cluster": "corporate",
        "style": "classic-serif",
        "price_tier": "standard",
        "use_cases": ["corporate-presence", "generate-leads", "b2b-credibility"],
        "audience": ["enterprise", "smb"],
        "search_keywords": (
            "corporate azienda istituzionale b2b enterprise consulenza business"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "elevate-startup-landing": {
        "cluster": "saas-landing",
        "style": "dashboard-dark",
        "price_tier": "premium",
        "use_cases": ["product-launch", "generate-leads", "demo-bookings"],
        "audience": ["smb", "enterprise"],
        "search_keywords": (
            "saas startup prodotto landing pricing demo b2b tech"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "gusto-fine-dining": {
        "cluster": "fine-dining",
        "style": "editorial-warm",
        "price_tier": "premium",
        "use_cases": ["reservations", "menu-online", "brand-storytelling"],
        "audience": ["smb"],
        "search_keywords": (
            "ristorante stellato chef fine-dining gourmet haute-cuisine prenotazione"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "sapore-trattoria-pizzeria": {
        "cluster": "trattoria",
        "style": "editorial-warm",
        "price_tier": "standard",
        "use_cases": ["reservations", "menu-online", "local-presence"],
        "audience": ["smb", "freelance"],
        "search_keywords": (
            "trattoria pizzeria osteria menu tradizionale regionale prenotazione"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "brace-street-food-lab": {
        "cluster": "street-casual",
        "style": "bold-display",
        "price_tier": "standard",
        "use_cases": ["online-ordering", "menu-online", "brand-youth"],
        "audience": ["smb"],
        "search_keywords": (
            "street-food burger casual cloud-kitchen ordering pickup lab"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "salute-studio-medico": {
        "cluster": "multi-clinic",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": [
            "appointment-booking",
            "patient-info",
            "professional-credibility",
        ],
        "audience": ["smb", "studio"],
        "search_keywords": (
            "clinica poliambulatorio medicina-generale visita prenotazione ambulatorio"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "benessere-centro-olistico": {
        "cluster": "wellness-holistic",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": ["appointment-booking", "wellness-brand", "retreats-booking"],
        "audience": ["smb", "studio"],
        "search_keywords": (
            "olistico wellness benessere nutrizione naturopatia retreat trattamenti"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "famiglia-pediatria": {
        "cluster": "family-pediatric",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": ["appointment-booking", "family-trust", "pediatric-brand"],
        "audience": ["studio", "smb"],
        "search_keywords": (
            "pediatria famiglia bambini pediatra visita ginecologia"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "cardio-studio-specialistico": {
        "cluster": "specialist",
        "style": "minimal-light",
        "price_tier": "premium",
        "use_cases": [
            "appointment-booking",
            "specialist-credibility",
            "medical-authority",
        ],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "cardiologo cuore specialista studio-medico visita-specialistica"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "dermatologia-elite-roma": {
        "cluster": "specialist",
        "style": "minimal-light",
        "price_tier": "premium",
        "use_cases": [
            "appointment-booking",
            "specialist-credibility",
            "aesthetic-services",
        ],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "dermatologo pelle estetica specialista roma visita-dermatologica"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "lex-studio-legale": {
        "cluster": "classic-law",
        "style": "classic-serif",
        "price_tier": "premium",
        "use_cases": ["consultation-booking", "case-studies", "legal-authority"],
        "audience": ["studio", "smb"],
        "search_keywords": (
            "avvocato studio-legale civile penale commerciale consulenza-legale"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "juris-avvocato-moderno": {
        "cluster": "modern-law-tech",
        "style": "minimal-mono",
        "price_tier": "premium",
        "use_cases": ["consultation-booking", "legal-tech-brand", "modern-law"],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "avvocato moderno ip startup diritto-tech privacy gdpr consulenza"
        ),
        "has_shop": False,
        "has_booking": True,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "casa-agenzia-immobiliare": {
        "cluster": "real-estate-mass-market",
        "style": "minimal-light",
        "price_tier": "standard",
        "use_cases": ["property-listings", "lead-capture", "local-real-estate"],
        "audience": ["smb"],
        "search_keywords": (
            "immobiliare agenzia casa appartamento affitto vendita ricerca-casa"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "villa-immobili-lusso": {
        "cluster": "real-estate-luxury",
        "style": "cinematic-fullbleed",
        "price_tier": "premium",
        "use_cases": ["luxury-listings", "premium-brand", "lead-capture"],
        "audience": ["smb", "agency"],
        "search_keywords": (
            "villa lusso immobili-lusso prestigio proprietà-esclusive luxury-estate"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "chiara-portfolio-creativo": {
        "cluster": "designer-editorial",
        "style": "editorial-warm",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "attract-clients", "editorial-brand"],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "designer portfolio editoriale graphic-designer art-direction brand-identity"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "pixel-portfolio-fotografico": {
        "cluster": "photographer",
        "style": "cinematic-fullbleed",
        "price_tier": "premium",
        "use_cases": ["show-portfolio", "attract-clients", "cinematic-brand"],
        "audience": ["freelance", "studio"],
        "search_keywords": (
            "fotografo portfolio cinematic fine-art ritratto architettura serie"
        ),
        "has_shop": False,
        "has_booking": False,
        "has_portfolio": True,
        "has_blog": False,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "bottega-shop-artigianale": {
        "cluster": "artisan-workshop",
        "style": "typographic-first",
        "price_tier": "premium",
        "use_cases": ["sell-online", "brand-storytelling", "artisan-identity"],
        "audience": ["smb", "freelance"],
        "search_keywords": (
            "artigiano bottega atelier maker tipografico editoriale vendita-online journal"
        ),
        "has_shop": True,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": False,
        "has_rtl": True,
        "is_multi_page": True,
    },
    "luxe-fashion-store": {
        "cluster": "fashion-editorial",
        "style": "magazine-hybrid",
        "price_tier": "premium",
        "use_cases": ["sell-online", "luxury-brand", "lookbook-campaigns"],
        "audience": ["smb", "enterprise"],
        "search_keywords": (
            "fashion moda maison luxury lookbook editoriale concept-store vendita-online"
        ),
        "has_shop": True,
        "has_booking": False,
        "has_portfolio": False,
        "has_blog": True,
        "has_video": True,
        "has_rtl": True,
        "is_multi_page": True,
    },
}

# Feature-flag boolean column names in the exact order they land on the
# WebTemplate model. Used by both the forward-write loop and the reverse
# reset to avoid key-name drift between ``TEMPLATE_METADATA`` and the
# model's column list.
_FEATURE_FLAG_FIELDS = (
    "has_shop",
    "has_booking",
    "has_portfolio",
    "has_blog",
    "has_video",
    "has_rtl",
    "is_multi_page",
)


def _backfill_taxonomy_v2(apps, schema_editor):
    """Populate taxonomy v2 metadata on the 20 MVP templates.

    Runs per the contract documented in the module docstring: no-op on
    empty databases, full write on databases that already carry the 20
    MVP slugs. Missing cluster/style seed rows cause a loud failure.
    """
    WebTemplate = apps.get_model("catalog", "WebTemplate")
    ProfessionCluster = apps.get_model("catalog", "ProfessionCluster")
    VisualStyle = apps.get_model("catalog", "VisualStyle")

    templates = list(WebTemplate.objects.filter(slug__in=TEMPLATE_METADATA.keys()))
    if not templates:
        # Fresh database · nothing to backfill. Seed chain will apply
        # the same metadata via seed_templates.TEMPLATE_METADATA.
        return

    # Fail loud if the seed rows are missing. get() raises DoesNotExist
    # with a clear message pointing at the offending slug.
    cluster_map = {c.slug: c for c in ProfessionCluster.objects.all()}
    style_map = {s.slug: s for s in VisualStyle.objects.all()}

    for tpl in templates:
        md = TEMPLATE_METADATA[tpl.slug]

        try:
            cluster = cluster_map[md["cluster"]]
        except KeyError as exc:
            raise RuntimeError(
                f"Backfill missing ProfessionCluster '{md['cluster']}' "
                f"required by template '{tpl.slug}'. Run "
                f"`manage.py seed_profession_clusters` before applying "
                f"migration 0004_taxonomy_v2_backfill."
            ) from exc
        try:
            style = style_map[md["style"]]
        except KeyError as exc:
            raise RuntimeError(
                f"Backfill missing VisualStyle '{md['style']}' required "
                f"by template '{tpl.slug}'. Run `manage.py "
                f"seed_visual_styles` before applying migration "
                f"0004_taxonomy_v2_backfill."
            ) from exc

        tpl.profession_cluster = cluster
        tpl.visual_style = style
        tpl.use_cases = list(md["use_cases"])
        tpl.audience = list(md["audience"])
        tpl.price_tier = md["price_tier"]
        tpl.search_keywords = md["search_keywords"]
        for flag in _FEATURE_FLAG_FIELDS:
            setattr(tpl, flag, md[flag])
        tpl.save(
            update_fields=[
                "profession_cluster",
                "visual_style",
                "use_cases",
                "audience",
                "price_tier",
                "search_keywords",
                *_FEATURE_FLAG_FIELDS,
                "updated_at",
            ]
        )


def _reverse_taxonomy_v2(apps, schema_editor):
    """Reset the 20 MVP template rows to pre-backfill defaults.

    Schema migration 0003 stays standalone-rollbackable after this:
    the additive columns keep their defaults (empty list / empty string
    / False / None) so dropping them in 0003's reverse plan doesn't
    require a separate cleanup pass.
    """
    WebTemplate = apps.get_model("catalog", "WebTemplate")
    templates = WebTemplate.objects.filter(slug__in=TEMPLATE_METADATA.keys())
    for tpl in templates:
        tpl.profession_cluster = None
        tpl.visual_style = None
        tpl.use_cases = []
        tpl.audience = []
        tpl.price_tier = None
        tpl.search_keywords = ""
        for flag in _FEATURE_FLAG_FIELDS:
            setattr(tpl, flag, False)
        tpl.save(
            update_fields=[
                "profession_cluster",
                "visual_style",
                "use_cases",
                "audience",
                "price_tier",
                "search_keywords",
                *_FEATURE_FLAG_FIELDS,
                "updated_at",
            ]
        )


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_taxonomy_v2_schema"),
    ]

    operations = [
        migrations.RunPython(
            _backfill_taxonomy_v2,
            reverse_code=_reverse_taxonomy_v2,
        ),
    ]
