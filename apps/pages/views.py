from django.urls import reverse
from django.views.generic import TemplateView

from apps.catalog import selectors
from apps.catalog.models import (
    Category,
    ProfessionCluster,
    WebTemplate,
)


# X.2 Commit 5 · curated subsets surfaced on the homepage. Keeping
# these as module-level constants lets a future Wave 3 editor tweak
# which roles/use-cases appear above the fold without reshaping the
# discovery model. Slugs must resolve in ROLE_DISCOVERY /
# USE_CASE_DISCOVERY; missing entries are dropped silently so an
# operator can rename a slug without an immediate render break.
HOME_ROLE_SLUGS = (
    "avvocati",
    "medici",
    "ristoratori",
    "startup",
    "fotografi",
    "artigiani",
    "agenzie",
    "immobiliari",
)

HOME_USE_CASE_SLUGS = (
    "sell-online",
    "reservations",
    "appointment-booking",
    "show-portfolio",
    "generate-leads",
    "brand-storytelling",
)

# The catalog has authored content for these 5 canonical locales
# across every enrolled archetype — see D-098 topology + Session 29
# / 41 / 51 rollout records. Surfaced on the trust strip so the
# homepage reflects the real editor footprint rather than a
# hardcoded marketing number.
CATALOG_LOCALES = ("it", "en", "fr", "es", "ar")


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # ── Existing context (pre-X.2 Commit 5) ────────────────────
        ctx["categories"] = selectors.get_active_categories_with_counts()
        ctx["featured_templates"] = selectors.get_featured_templates(limit=6)

        # ── X.2 Commit 5 · taxonomy-driven discovery context ──────
        ctx["search_typeahead_url"] = reverse("catalog:search_typeahead")
        ctx["catalog_list_url"] = reverse("catalog:template_list")

        # Role discovery cards · curated subset of ROLE_DISCOVERY.
        # Rendered only if the slug resolves, so a registry rename
        # degrades gracefully rather than 500-ing the homepage.
        ctx["home_roles"] = [
            {
                "slug": slug,
                "label": selectors.ROLE_DISCOVERY[slug]["label"],
                "description": selectors.ROLE_DISCOVERY[slug]["description"],
                "url": reverse(
                    "catalog:role_discovery", kwargs={"role_slug": slug}
                ),
            }
            for slug in HOME_ROLE_SLUGS
            if slug in selectors.ROLE_DISCOVERY
        ]

        # Use-case discovery cards · curated subset of USE_CASE_DISCOVERY.
        ctx["home_use_cases"] = [
            {
                "slug": slug,
                "label": selectors.USE_CASE_DISCOVERY[slug]["label"],
                "description": selectors.USE_CASE_DISCOVERY[slug]["description"],
                "url": reverse(
                    "catalog:use_case_discovery",
                    kwargs={"use_case_slug": slug},
                ),
            }
            for slug in HOME_USE_CASE_SLUGS
            if slug in selectors.USE_CASE_DISCOVERY
        ]

        # Trust counters · live from the DB so the hero numbers stay
        # honest as the catalog grows. Falls back to 0 on an empty DB
        # (e.g. a dev env pre-seed) without raising.
        ctx["trust_counters"] = {
            "templates_live": WebTemplate.objects.filter(
                tier=WebTemplate.Tier.PUBLISHED_LIVE
            ).count(),
            "categories_active": Category.objects.filter(is_active=True).count(),
            "clusters_active": ProfessionCluster.objects.filter(
                is_active=True
            ).count(),
            "locales_supported": len(CATALOG_LOCALES),
        }

        return ctx
