"""Catalog app tests.

X.2 Commit 1 · initial coverage for ``ProfessionCluster``, ``VisualStyle``,
and the additive metadata layer on ``WebTemplate``. No selectors, views,
or templates are exercised here — those land in later X.2 commits.

Scope per commit binding:
- Every new model has __str__, ordering, uniqueness, default-value tests.
- Every new WebTemplate field has a default-value test so the nullable-
  then-NOT-NULL migration path stays safe.
- Admin registration is asserted at import-time so a regression on the
  admin.py wiring surfaces before the public catalog UX is built.
"""

from decimal import Decimal

from django.contrib import admin as djadmin
from django.db import IntegrityError, transaction
from django.test import TestCase

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
