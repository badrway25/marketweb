"""Catalog app tests.

X.2 Commit 1 · initial coverage for ``ProfessionCluster``, ``VisualStyle``,
and the additive metadata layer on ``WebTemplate``. No selectors, views,
or templates are exercised here — those land in later X.2 commits.

X.2 Commit 2 · focused coverage for the two seed management commands
(``seed_visual_styles`` + ``seed_profession_clusters``). Exercises the
idempotency contract + representative-sample slug/category mapping.

Scope per commit binding:
- Every new model has __str__, ordering, uniqueness, default-value tests.
- Every new WebTemplate field has a default-value test so the nullable-
  then-NOT-NULL migration path stays safe.
- Admin registration is asserted at import-time so a regression on the
  admin.py wiring surfaces before the public catalog UX is built.
- Every seed command is tested for: fresh-run count, second-run
  idempotency, representative sample mapping.
"""

from decimal import Decimal
from io import StringIO

from django.contrib import admin as djadmin
from django.core.management import call_command
from django.db import IntegrityError, transaction
from django.test import TestCase

from apps.catalog.management.commands.seed_profession_clusters import (
    EXTRA_CATEGORIES,
    PROFESSION_CLUSTERS,
)
from apps.catalog.management.commands.seed_visual_styles import VISUAL_STYLES
from apps.catalog.models import (
    Category,
    ProfessionCluster,
    VisualStyle,
    WebTemplate,
)


class ProfessionClusterTests(TestCase):
    """Shape + behaviour of the ProfessionCluster model."""

    @classmethod
    def setUpTestData(cls):
        cls.agency = Category.objects.create(name="Agency", slug="agency", order=1)
        cls.business = Category.objects.create(
            name="Business", slug="business", order=2
        )

    def test_str_includes_category_name(self):
        cluster = ProfessionCluster.objects.create(
            name="Creative", category=self.agency
        )
        self.assertEqual(str(cluster), "Creative (Agency)")

    def test_slug_auto_generated_from_name(self):
        cluster = ProfessionCluster.objects.create(
            name="Digital Growth", category=self.agency
        )
        self.assertEqual(cluster.slug, "digital-growth")

    def test_slug_is_globally_unique(self):
        ProfessionCluster.objects.create(
            name="Creative", slug="creative", category=self.agency
        )
        with self.assertRaises(IntegrityError), transaction.atomic():
            # Second cluster cannot reuse the slug even across categories.
            ProfessionCluster.objects.create(
                name="Creative", slug="creative", category=self.business
            )

    def test_defaults_are_sensible(self):
        cluster = ProfessionCluster.objects.create(
            name="Corporate", category=self.business
        )
        self.assertEqual(cluster.description, "")
        self.assertEqual(cluster.icon, "")
        self.assertEqual(cluster.order, 0)
        self.assertTrue(cluster.is_active)
        self.assertEqual(cluster.search_aliases, "")

    def test_ordering_by_category_order_then_cluster_order_then_name(self):
        # business.order=2 is higher than agency.order=1 → agency clusters
        # should come first regardless of cluster.order.
        biz_a = ProfessionCluster.objects.create(
            name="Alpha", category=self.business, order=0
        )
        ag_z = ProfessionCluster.objects.create(
            name="Zeta", category=self.agency, order=10
        )
        ag_b = ProfessionCluster.objects.create(
            name="Beta", category=self.agency, order=0
        )
        ordered = list(ProfessionCluster.objects.all())
        self.assertEqual(ordered, [ag_b, ag_z, biz_a])

    def test_category_reverse_accessor_is_profession_clusters(self):
        ProfessionCluster.objects.create(name="Creative", category=self.agency)
        ProfessionCluster.objects.create(name="Freelance", category=self.agency)
        self.assertEqual(self.agency.profession_clusters.count(), 2)


class VisualStyleTests(TestCase):
    """Shape + behaviour of the VisualStyle model."""

    def test_str_is_label(self):
        style = VisualStyle.objects.create(
            slug="editorial-warm", label="Editorial warm"
        )
        self.assertEqual(str(style), "Editorial warm")

    def test_slug_is_unique(self):
        VisualStyle.objects.create(slug="editorial-warm", label="Editorial warm")
        with self.assertRaises(IntegrityError), transaction.atomic():
            VisualStyle.objects.create(
                slug="editorial-warm", label="Duplicate attempt"
            )

    def test_ordering_by_order_then_slug(self):
        b = VisualStyle.objects.create(slug="b-style", label="B", order=2)
        a2 = VisualStyle.objects.create(slug="a-style-2", label="A2", order=1)
        a1 = VisualStyle.objects.create(slug="a-style-1", label="A1", order=1)
        self.assertEqual(list(VisualStyle.objects.all()), [a1, a2, b])

    def test_defaults_are_sensible(self):
        style = VisualStyle.objects.create(
            slug="minimal-light", label="Minimal light"
        )
        self.assertEqual(style.palette_family, "")
        self.assertEqual(style.typography_stack, "")
        self.assertEqual(style.density_profile, "")
        self.assertEqual(style.badge, "")
        self.assertEqual(style.order, 0)
        self.assertTrue(style.is_active)


class WebTemplateMetadataTests(TestCase):
    """Additive metadata columns on WebTemplate (X.2 Commit 1).

    Every new field defaults to a safe value so the migration can land
    on a populated catalog without touching existing rows. Commit 3
    will backfill these fields; this test locks the default contract.
    """

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Restaurant", slug="restaurant", order=3
        )
        cls.cluster = ProfessionCluster.objects.create(
            name="Fine dining",
            slug="fine-dining",
            category=cls.category,
            search_aliases="chef stellato haute-cuisine ristorante-gourmet",
        )
        cls.style = VisualStyle.objects.create(
            slug="editorial-warm",
            label="Editorial warm",
            palette_family="warm",
            typography_stack="serif-editorial",
            density_profile="editorial-sparse",
        )

    def _make_template(self, **overrides) -> WebTemplate:
        defaults = {
            "name": "Test Template",
            "slug": "test-template",
            "category": self.category,
            "description": "Test description.",
            "price": Decimal("0.00"),
        }
        defaults.update(overrides)
        return WebTemplate.objects.create(**defaults)

    def test_new_fields_default_values_match_migration_contract(self):
        tpl = self._make_template()
        # Nullable FKs default to None during the backfill window.
        self.assertIsNone(tpl.profession_cluster)
        self.assertIsNone(tpl.visual_style)
        # Open-ended list metadata defaults to empty list.
        self.assertEqual(tpl.use_cases, [])
        self.assertEqual(tpl.audience, [])
        # Search + price tier default to empty / null.
        self.assertEqual(tpl.search_keywords, "")
        self.assertIsNone(tpl.price_tier)
        # All 7 feature flags default to False.
        self.assertFalse(tpl.has_shop)
        self.assertFalse(tpl.has_booking)
        self.assertFalse(tpl.has_portfolio)
        self.assertFalse(tpl.has_blog)
        self.assertFalse(tpl.has_video)
        self.assertFalse(tpl.has_rtl)
        self.assertFalse(tpl.is_multi_page)

    def test_profession_cluster_reverse_accessor_and_related_name(self):
        tpl = self._make_template(profession_cluster=self.cluster)
        self.assertEqual(list(self.cluster.templates.all()), [tpl])

    def test_visual_style_reverse_accessor_and_related_name(self):
        tpl = self._make_template(visual_style=self.style)
        self.assertEqual(list(self.style.templates.all()), [tpl])

    def test_price_tier_accepts_valid_choice(self):
        tpl = self._make_template(price_tier=WebTemplate.PriceTier.PREMIUM)
        tpl.refresh_from_db()
        self.assertEqual(tpl.price_tier, "premium")

    def test_price_tier_choices_are_free_standard_premium(self):
        labels = {v for v, _ in WebTemplate.PriceTier.choices}
        self.assertEqual(labels, {"free", "standard", "premium"})

    def test_json_fields_accept_list_payloads(self):
        tpl = self._make_template(
            use_cases=["online-ordering", "reservations"],
            audience=["smb", "agency"],
        )
        tpl.refresh_from_db()
        self.assertEqual(tpl.use_cases, ["online-ordering", "reservations"])
        self.assertEqual(tpl.audience, ["smb", "agency"])

    def test_feature_flags_roundtrip(self):
        tpl = self._make_template(
            has_shop=True,
            has_booking=True,
            has_portfolio=True,
            has_blog=True,
            has_video=True,
            has_rtl=True,
            is_multi_page=True,
        )
        tpl.refresh_from_db()
        self.assertTrue(tpl.has_shop)
        self.assertTrue(tpl.has_booking)
        self.assertTrue(tpl.has_portfolio)
        self.assertTrue(tpl.has_blog)
        self.assertTrue(tpl.has_video)
        self.assertTrue(tpl.has_rtl)
        self.assertTrue(tpl.is_multi_page)

    def test_legacy_category_fk_still_required(self):
        # ``category`` is NOT touched by X.2 Commit 1. Creating a template
        # without a category must still fail — the field stays non-null.
        with self.assertRaises(IntegrityError), transaction.atomic():
            WebTemplate.objects.create(
                name="No Category", slug="no-category", description=""
            )

    def test_cluster_category_and_template_category_can_be_consistent(self):
        tpl = self._make_template(profession_cluster=self.cluster)
        # Commit 3 backfill will guarantee this invariant for the 20
        # existing rows. Commit 1 only asserts the shape supports it.
        self.assertEqual(tpl.category_id, tpl.profession_cluster.category_id)


class AdminRegistrationTests(TestCase):
    """Admin wiring smoke — registration + list_display sanity."""

    def test_profession_cluster_registered(self):
        self.assertIn(ProfessionCluster, djadmin.site._registry)

    def test_visual_style_registered(self):
        self.assertIn(VisualStyle, djadmin.site._registry)

    def test_webtemplate_admin_surfaces_new_taxonomy_fields(self):
        admin_instance = djadmin.site._registry[WebTemplate]
        list_display = admin_instance.list_display
        self.assertIn("profession_cluster", list_display)
        self.assertIn("visual_style", list_display)
        self.assertIn("price_tier", list_display)

    def test_webtemplate_admin_feature_flags_in_list_filter(self):
        admin_instance = djadmin.site._registry[WebTemplate]
        list_filter = admin_instance.list_filter
        # Verify at least the three load-bearing feature filters are
        # exposed as sidebar facets on the Django admin.
        self.assertIn("has_shop", list_filter)
        self.assertIn("has_booking", list_filter)
        self.assertIn("has_rtl", list_filter)


# ── X.2 Commit 2 · seed management command coverage ──────────────


class SeedVisualStylesCommandTests(TestCase):
    """``seed_visual_styles`` creates 12 rows and is idempotent."""

    def _run(self):
        out = StringIO()
        call_command("seed_visual_styles", stdout=out)
        return out.getvalue()

    def test_first_run_creates_twelve_styles(self):
        self.assertEqual(VisualStyle.objects.count(), 0)
        output = self._run()
        self.assertEqual(VisualStyle.objects.count(), 12)
        self.assertIn("12 visual styles created", output)

    def test_second_run_is_idempotent(self):
        self._run()
        self.assertEqual(VisualStyle.objects.count(), 12)
        output = self._run()
        self.assertEqual(VisualStyle.objects.count(), 12)
        self.assertIn("0 visual styles created", output)
        self.assertIn("12 already existed", output)

    def test_seed_constant_declares_exactly_twelve_styles(self):
        # Guardrail against accidental drift between the seed constant
        # and the Commit 2 contract (12 base styles).
        self.assertEqual(len(VISUAL_STYLES), 12)
        slugs = [s["slug"] for s in VISUAL_STYLES]
        self.assertEqual(len(slugs), len(set(slugs)), "slugs must be unique")

    def test_representative_sample_mapping(self):
        self._run()
        editorial_warm = VisualStyle.objects.get(slug="editorial-warm")
        self.assertEqual(editorial_warm.label, "Editorial warm")
        self.assertEqual(editorial_warm.palette_family, "warm")
        self.assertEqual(editorial_warm.typography_stack, "serif-editorial")
        self.assertEqual(editorial_warm.density_profile, "editorial-sparse")

        dashboard_dark = VisualStyle.objects.get(slug="dashboard-dark")
        self.assertEqual(dashboard_dark.palette_family, "dark")
        self.assertEqual(dashboard_dark.density_profile, "dashboard-dense")

        cinematic = VisualStyle.objects.get(slug="cinematic-fullbleed")
        self.assertEqual(cinematic.density_profile, "fullbleed-cinematic")


class SeedProfessionClustersCommandTests(TestCase):
    """``seed_profession_clusters`` creates 52 rows + ensures 7 extra macro-
    categories, and is idempotent across re-runs.
    """

    @classmethod
    def setUpTestData(cls):
        # Seed the 8 MVP macro-categories via the canonical command so
        # the cluster-seed resolves their FK targets. The 7 extra ones
        # are ensured inline by the cluster-seed command itself.
        call_command("seed_categories", stdout=StringIO())

    def _run(self):
        out = StringIO()
        call_command("seed_profession_clusters", stdout=out)
        return out.getvalue()

    def test_first_run_creates_fifty_two_clusters(self):
        # Pre-seed: 8 MVP categories exist, 0 clusters.
        self.assertEqual(Category.objects.count(), 8)
        self.assertEqual(ProfessionCluster.objects.count(), 0)
        output = self._run()
        self.assertEqual(ProfessionCluster.objects.count(), 52)
        self.assertIn("52 profession clusters created", output)

    def test_first_run_creates_seven_extra_macro_categories(self):
        # 8 MVP + 7 extra = 15 total macro-categories post-run.
        self._run()
        self.assertEqual(Category.objects.count(), 15)
        for extra in EXTRA_CATEGORIES:
            self.assertTrue(
                Category.objects.filter(slug=extra["slug"]).exists(),
                f"Expected extra macro-category {extra['slug']} to be seeded.",
            )

    def test_second_run_is_idempotent(self):
        self._run()
        self.assertEqual(ProfessionCluster.objects.count(), 52)
        self.assertEqual(Category.objects.count(), 15)
        output = self._run()
        self.assertEqual(ProfessionCluster.objects.count(), 52)
        self.assertEqual(Category.objects.count(), 15)
        self.assertIn("0 profession clusters created", output)
        self.assertIn("52 already existed", output)

    def test_seed_constant_declares_exactly_fifty_two_clusters(self):
        # Guardrail against accidental drift between the seed constant
        # and the X.1/X.2 52-cluster taxonomy contract.
        self.assertEqual(len(PROFESSION_CLUSTERS), 52)
        slugs = [c["slug"] for c in PROFESSION_CLUSTERS]
        self.assertEqual(len(slugs), len(set(slugs)), "cluster slugs must be unique")

    def test_extra_categories_constant_declares_exactly_seven(self):
        self.assertEqual(len(EXTRA_CATEGORIES), 7)

    def test_representative_sample_cluster_to_category_mapping(self):
        self._run()
        # Restaurant → fine-dining (existing MVP category)
        fine_dining = ProfessionCluster.objects.get(slug="fine-dining")
        self.assertEqual(fine_dining.category.slug, "restaurant")
        self.assertEqual(fine_dining.name, "Fine dining")
        self.assertIn("stellato", fine_dining.search_aliases)

        # Medical → specialist
        specialist = ProfessionCluster.objects.get(slug="specialist")
        self.assertEqual(specialist.category.slug, "medical")

        # Legacy category slug is 'lawyer' (not 'law') — the cluster
        # seed must honor it, otherwise the FK resolves to None and
        # the cluster is skipped.
        classic_law = ProfessionCluster.objects.get(slug="classic-law")
        self.assertEqual(classic_law.category.slug, "lawyer")

        # Inline-created extra category → fitness cluster
        gym = ProfessionCluster.objects.get(slug="gym-functional")
        self.assertEqual(gym.category.slug, "fitness")

        # Nonprofit (another inline extra category)
        charity = ProfessionCluster.objects.get(slug="charity-foundation")
        self.assertEqual(charity.category.slug, "nonprofit")

    def test_cluster_counts_per_category_match_taxonomy_contract(self):
        # Locks the X.1 taxonomy distribution so a future edit to the
        # PROFESSION_CLUSTERS constant cannot silently drift the per-
        # category split.
        self._run()
        expected = {
            "agency": 4,
            "business": 5,
            "restaurant": 5,
            "medical": 6,
            "lawyer": 3,
            "real-estate": 3,
            "portfolio": 4,
            "ecommerce": 4,
            "education": 3,
            "events": 2,
            "travel": 3,
            "fitness": 3,
            "construction": 3,
            "beauty": 2,
            "nonprofit": 2,
        }
        for slug, count in expected.items():
            actual = ProfessionCluster.objects.filter(
                category__slug=slug
            ).count()
            self.assertEqual(
                actual,
                count,
                f"Expected {count} clusters in '{slug}', got {actual}.",
            )
        self.assertEqual(sum(expected.values()), 52)
