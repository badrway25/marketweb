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
        # X.3 Commit 5 · post NOT NULL flip: profession_cluster + visual_style
        # are required at INSERT. The helper wires the class-level fixture
        # cluster + style by default so existing tests keep testing metadata
        # defaults on a VALID row shape. Override via kwargs when a test
        # needs a specific cluster/style.
        defaults = {
            "name": "Test Template",
            "slug": "test-template",
            "category": self.category,
            "description": "Test description.",
            "price": Decimal("0.00"),
            "profession_cluster": self.cluster,
            "visual_style": self.style,
        }
        defaults.update(overrides)
        return WebTemplate.objects.create(**defaults)

    def test_new_fields_default_values_match_migration_contract(self):
        tpl = self._make_template()
        # X.3 Commit 5: FKs are now required · helper wires them.
        self.assertIsNotNone(tpl.profession_cluster)
        self.assertIsNotNone(tpl.visual_style)
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


# ── X.2 Commit 3 · backfill + seed_templates metadata integration ──

import importlib  # noqa: E402

from apps.catalog.management.commands.seed_templates import (  # noqa: E402
    TEMPLATE_METADATA as SEED_TEMPLATE_METADATA,
)

# The migration file name starts with a digit ("0004_..."), so a plain
# ``from apps.catalog.migrations.0004_... import ...`` is a syntax
# error. ``importlib.import_module`` accepts arbitrary dotted paths and
# is the canonical way to reach migration-level constants from a test.
_backfill_module = importlib.import_module(
    "apps.catalog.migrations.0004_taxonomy_v2_backfill"
)
BACKFILL_TEMPLATE_METADATA = _backfill_module.TEMPLATE_METADATA
BACKFILL_FEATURE_FLAG_FIELDS = _backfill_module._FEATURE_FLAG_FIELDS


class BackfillContractTests(TestCase):
    """Locks the dict-level contract between the migration and the seed.

    The data migration inlines ``TEMPLATE_METADATA`` (frozen at migration
    authoring time) while ``seed_templates.TEMPLATE_METADATA`` remains
    the live source of truth for fresh seeds. These tests assert they
    stay in sync — a drift would produce different end-states for a
    production DB (migration path) vs a CI / fresh DB (seed path).
    """

    def test_backfill_dict_and_seed_templates_dict_match(self):
        # Wave 2 contract (Phase X.4): the backfill migration
        # (``0004_taxonomy_v2_backfill``) is FROZEN at the 20 MVP
        # slugs it shipped with. The seed dict grows each wave as
        # new templates land. The invariant therefore shifts from
        # "exact set equality" to "backfill keys ⊆ seed keys and
        # metadata matches on the common slugs". This keeps fresh
        # DB seed runs identical to migrated DB end-state for every
        # MVP slug, while letting Wave-2+ pilots extend the seed
        # without rewriting history.
        backfill_slugs = set(BACKFILL_TEMPLATE_METADATA.keys())
        seed_slugs = set(SEED_TEMPLATE_METADATA.keys())
        missing_from_seed = backfill_slugs - seed_slugs
        self.assertEqual(
            missing_from_seed,
            set(),
            f"Backfill-only slugs not present in seed: {missing_from_seed}. "
            f"Every migration slug must remain seedable so fresh DBs "
            f"converge to the same end-state as migrated ones.",
        )
        for slug in backfill_slugs:
            seed_md = SEED_TEMPLATE_METADATA[slug]
            migration_md = BACKFILL_TEMPLATE_METADATA[slug]
            self.assertEqual(
                seed_md,
                migration_md,
                f"Metadata drift on '{slug}' between migration 0004 and "
                f"seed_templates — both must declare identical fields.",
            )

    def test_backfill_covers_exactly_twenty_templates(self):
        # Backfill dict stays frozen at 20 (the MVP slugs from X.2).
        # Seed dict grows with each Wave — at least 20 + however
        # many Wave 2 pilots have merged. No upper bound asserted
        # here; Wave cadence tests enforce their own counts.
        self.assertEqual(len(BACKFILL_TEMPLATE_METADATA), 20)
        self.assertGreaterEqual(len(SEED_TEMPLATE_METADATA), 20)

    def test_feature_flag_field_list_is_consistent(self):
        # Both definitions expose the same tuple order so iteration
        # stays deterministic across forward + reverse paths.
        self.assertEqual(
            BACKFILL_FEATURE_FLAG_FIELDS,
            (
                "has_shop",
                "has_booking",
                "has_portfolio",
                "has_blog",
                "has_video",
                "has_rtl",
                "is_multi_page",
            ),
        )


class FreshSeedChainBackfillTests(TestCase):
    """End-to-end seed chain → backfill via seed_templates metadata.

    Mirrors the path a CI / fresh-env run takes: migrations apply
    (including the 0004 data migration, which is a no-op on an empty
    DB), then the four seed commands run in order. Locks the 20-MVP
    invariant + category preservation + sample slug→cluster/style
    mapping + sample feature-flag and price-tier wiring.
    """

    @classmethod
    def setUpTestData(cls):
        call_command("seed_categories", stdout=StringIO())
        call_command("seed_visual_styles", stdout=StringIO())
        call_command("seed_profession_clusters", stdout=StringIO())
        call_command("seed_templates", stdout=StringIO())

    def test_seeded_template_count_matches_seed_metadata(self):
        # 20 MVP templates + Wave 2 pilots merged to date. The exact
        # count is derived from SEED_TEMPLATE_METADATA so Wave 2
        # additions bump the expected count automatically, while
        # still guarding against silent catalog drift (each seed
        # entry must correspond to exactly one DB row).
        self.assertEqual(
            WebTemplate.objects.count(),
            len(SEED_TEMPLATE_METADATA),
            "Seeded DB row count must match seed metadata length — "
            "one metadata entry per template, no duplicates, no gaps.",
        )

    def test_every_mvp_template_has_profession_cluster(self):
        missing = list(
            WebTemplate.objects.filter(profession_cluster__isnull=True).values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(
            missing,
            [],
            f"Every MVP template must carry a profession_cluster; missing on: {missing}.",
        )

    def test_every_mvp_template_has_visual_style(self):
        missing = list(
            WebTemplate.objects.filter(visual_style__isnull=True).values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(
            missing,
            [],
            f"Every MVP template must carry a visual_style; missing on: {missing}.",
        )

    def test_template_category_preserved_across_backfill(self):
        # The seed_templates entries hardcode the legacy category FK;
        # taxonomy v2 is additive so each ``category_slug`` in the
        # seed list must match the persisted FK (no silent rewrite).
        from apps.catalog.management.commands.seed_templates import SEED_TEMPLATES

        for entry in SEED_TEMPLATES:
            tpl = WebTemplate.objects.get(slug=entry["slug"])
            self.assertEqual(
                tpl.category.slug,
                entry["category_slug"],
                f"Category drift on {entry['slug']}: expected "
                f"{entry['category_slug']!r}, got {tpl.category.slug!r}.",
            )

    def test_cluster_category_matches_template_category(self):
        # Invariant: the ProfessionCluster a template points to must
        # live under the same macro-category as the template itself.
        for tpl in WebTemplate.objects.all():
            self.assertEqual(
                tpl.profession_cluster.category_id,
                tpl.category_id,
                f"Cluster/category mismatch on '{tpl.slug}': cluster "
                f"is in {tpl.profession_cluster.category.slug!r}, "
                f"template is in {tpl.category.slug!r}.",
            )

    def test_representative_mapping_vertex_creative_editorial_warm(self):
        vertex = WebTemplate.objects.get(slug="vertex-creative-agency")
        self.assertEqual(vertex.profession_cluster.slug, "creative")
        self.assertEqual(vertex.visual_style.slug, "editorial-warm")
        self.assertEqual(vertex.price_tier, WebTemplate.PriceTier.PREMIUM)
        self.assertTrue(vertex.has_portfolio)
        self.assertFalse(vertex.has_shop)

    def test_representative_mapping_bottega_artisan_typographic_first(self):
        bottega = WebTemplate.objects.get(slug="bottega-shop-artigianale")
        self.assertEqual(bottega.profession_cluster.slug, "artisan-workshop")
        self.assertEqual(bottega.visual_style.slug, "typographic-first")
        self.assertEqual(bottega.price_tier, WebTemplate.PriceTier.PREMIUM)
        self.assertTrue(bottega.has_shop)
        self.assertTrue(bottega.has_blog)
        self.assertFalse(bottega.has_video)

    def test_representative_mapping_luxe_fashion_magazine_hybrid(self):
        luxe = WebTemplate.objects.get(slug="luxe-fashion-store")
        self.assertEqual(luxe.profession_cluster.slug, "fashion-editorial")
        self.assertEqual(luxe.visual_style.slug, "magazine-hybrid")
        self.assertTrue(luxe.has_shop)
        self.assertTrue(luxe.has_blog)
        self.assertTrue(luxe.has_video)
        self.assertTrue(luxe.has_rtl)
        self.assertIn("luxury-brand", luxe.use_cases)

    def test_specialist_cluster_is_shared_by_cardio_and_derm(self):
        # A.9 invariant preserved through taxonomy v2: a single cluster
        # slug can carry two templates (shared-schema archetype).
        cardio = WebTemplate.objects.get(slug="cardio-studio-specialistico")
        derm = WebTemplate.objects.get(slug="dermatologia-elite-roma")
        self.assertEqual(cardio.profession_cluster.slug, "specialist")
        self.assertEqual(derm.profession_cluster.slug, "specialist")
        self.assertEqual(
            cardio.profession_cluster_id, derm.profession_cluster_id
        )

    def test_medical_and_restaurant_templates_have_booking_flag(self):
        # Feature-flag sanity on medical + restaurant + lawyer + Wave 2
        # `consultation-booking` templates. Booking is the discovery-
        # relevant feature for all four groups. New Wave 2 booking
        # templates register here as they land.
        booking_slugs = {
            "salute-studio-medico",
            "benessere-centro-olistico",
            "famiglia-pediatria",
            "cardio-studio-specialistico",
            "dermatologia-elite-roma",
            "gusto-fine-dining",
            "sapore-trattoria-pizzeria",
            "brace-street-food-lab",
            "lex-studio-legale",
            "juris-avvocato-moderno",
            # Wave 2 Pilot #1 — Fiscus (appointment-request CTA)
            "fiscus-commercialista",
        }
        actual = set(
            WebTemplate.objects.filter(has_booking=True).values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(
            actual,
            booking_slugs,
            "has_booking=True expected on medical + restaurant + lawyer "
            "+ Wave 2 booking-enabled templates.",
        )

    def test_ecommerce_templates_have_shop_flag(self):
        shop_slugs = {"bottega-shop-artigianale", "luxe-fashion-store"}
        actual = set(
            WebTemplate.objects.filter(has_shop=True).values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(actual, shop_slugs)

    def test_all_mvp_templates_are_rtl_enabled(self):
        # D-098 / program-closure invariant: every enrolled archetype
        # (MVP + Wave 2) ships real RTL. The expected count tracks the
        # seed metadata length so Wave 2 additions don't drift the
        # assertion each merge — the invariant is "has_rtl is the
        # catalog-wide default", not "has_rtl is a magic 20".
        self.assertEqual(
            WebTemplate.objects.filter(has_rtl=True).count(),
            len(SEED_TEMPLATE_METADATA),
        )

    def test_all_mvp_templates_are_multi_page(self):
        self.assertEqual(
            WebTemplate.objects.filter(is_multi_page=True).count(),
            len(SEED_TEMPLATE_METADATA),
        )

    def test_search_keywords_populated_for_every_template(self):
        empty = list(
            WebTemplate.objects.filter(search_keywords="").values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(
            empty,
            [],
            f"Every MVP template must carry non-empty search_keywords; "
            f"missing on: {empty}.",
        )

    def test_price_tier_populated_for_every_template(self):
        null_rows = list(
            WebTemplate.objects.filter(price_tier__isnull=True).values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(
            null_rows,
            [],
            f"Every MVP template must carry a price_tier; missing on: "
            f"{null_rows}.",
        )

    def test_second_seed_run_is_idempotent(self):
        # Re-seeding must not duplicate templates + must not overwrite
        # metadata (we only apply metadata on create).
        call_command("seed_templates", stdout=StringIO())
        self.assertEqual(
            WebTemplate.objects.count(),
            len(SEED_TEMPLATE_METADATA),
        )
        # Sanity: metadata still intact after the repeat run.
        vertex = WebTemplate.objects.get(slug="vertex-creative-agency")
        self.assertEqual(vertex.visual_style.slug, "editorial-warm")


# ── X.2 Commit 4 · discovery selectors + views ────────────────────

import json  # noqa: E402

from apps.catalog import selectors  # noqa: E402


class _SeededCatalogMixin:
    """Runs the full seed chain so discovery tests have a populated DB."""

    @classmethod
    def setUpTestData(cls):
        call_command("seed_categories", stdout=StringIO())
        call_command("seed_visual_styles", stdout=StringIO())
        call_command("seed_profession_clusters", stdout=StringIO())
        call_command("seed_templates", stdout=StringIO())


class DiscoverySelectorTests(_SeededCatalogMixin, TestCase):
    """Coverage for selectors extended in X.2 Commit 4."""

    def test_listing_filter_by_cluster(self):
        _, qs = selectors.get_listing_templates(cluster_slugs=["fine-dining"])
        slugs = list(qs.values_list("slug", flat=True))
        self.assertEqual(slugs, ["gusto-fine-dining"])

    def test_listing_filter_by_multiple_clusters(self):
        _, qs = selectors.get_listing_templates(
            cluster_slugs=["fine-dining", "trattoria"]
        )
        self.assertEqual(
            set(qs.values_list("slug", flat=True)),
            {"gusto-fine-dining", "sapore-trattoria-pizzeria"},
        )

    def test_listing_filter_by_style(self):
        _, qs = selectors.get_listing_templates(
            style_slugs=["cinematic-fullbleed"]
        )
        self.assertEqual(
            set(qs.values_list("slug", flat=True)),
            {"villa-immobili-lusso", "pixel-portfolio-fotografico"},
        )

    def test_listing_filter_by_price_tier(self):
        _, qs = selectors.get_listing_templates(price_tiers=["standard"])
        # Standard tier templates (per X.2 mapping): Pragma + Sapore +
        # Brace + Salute + Benessere + Famiglia + Casa.
        self.assertEqual(qs.count(), 7)
        self.assertIn("pragma-corporate-suite", qs.values_list("slug", flat=True))

    def test_listing_filter_by_feature_flag_has_shop(self):
        _, qs = selectors.get_listing_templates(feature_flags=["has_shop"])
        self.assertEqual(
            set(qs.values_list("slug", flat=True)),
            {"bottega-shop-artigianale", "luxe-fashion-store"},
        )

    def test_listing_filter_by_unknown_feature_flag_is_ignored(self):
        # Unknown flag names are silently dropped — URL-driven filters
        # should stay resilient to typos without 500-ing.
        _, qs = selectors.get_listing_templates(
            feature_flags=["has_does_not_exist"]
        )
        self.assertEqual(qs.count(), 20)

    def test_listing_filter_by_use_case(self):
        _, qs = selectors.get_listing_templates(
            use_case_slugs=["appointment-booking"]
        )
        # Medical + specialist templates carry appointment-booking.
        slugs = set(qs.values_list("slug", flat=True))
        self.assertIn("salute-studio-medico", slugs)
        self.assertIn("cardio-studio-specialistico", slugs)
        self.assertNotIn("bottega-shop-artigianale", slugs)

    def test_listing_filter_by_audience(self):
        _, qs = selectors.get_listing_templates(audience_slugs=["enterprise"])
        slugs = set(qs.values_list("slug", flat=True))
        self.assertIn("pragma-corporate-suite", slugs)
        self.assertIn("elevate-startup-landing", slugs)

    def test_listing_feature_flags_are_and_joined(self):
        # Bottega carries has_shop=True + has_blog=True; Luxe too.
        # Cardio has has_booking=True but has_shop=False so it drops.
        _, qs = selectors.get_listing_templates(
            feature_flags=["has_shop", "has_blog"]
        )
        self.assertEqual(
            set(qs.values_list("slug", flat=True)),
            {"bottega-shop-artigianale", "luxe-fashion-store"},
        )

    def test_facet_counts_shape(self):
        _, qs = selectors.get_listing_templates()
        counts = selectors.get_facet_counts(qs)
        self.assertIn("clusters", counts)
        self.assertIn("styles", counts)
        self.assertIn("price_tiers", counts)
        self.assertIn("features", counts)
        self.assertIn("total", counts)
        self.assertEqual(counts["total"], 20)
        # Sanity spot-checks on a few counts.
        self.assertEqual(counts["clusters"].get("specialist"), 2)
        self.assertEqual(counts["price_tiers"].get("standard"), 7)
        self.assertEqual(counts["features"].get("has_rtl"), 20)
        self.assertEqual(counts["features"].get("has_shop"), 2)

    def test_typeahead_empty_query_returns_empty_pools(self):
        payload = selectors.search_templates_typeahead("")
        self.assertEqual(payload["templates"], [])
        self.assertEqual(payload["clusters"], [])
        self.assertEqual(payload["roles"], [])

    def test_typeahead_single_char_returns_empty_pools(self):
        payload = selectors.search_templates_typeahead("a")
        self.assertEqual(payload["templates"], [])

    def test_typeahead_matches_cluster_alias(self):
        payload = selectors.search_templates_typeahead("stellato")
        cluster_slugs = [c["slug"] for c in payload["clusters"]]
        self.assertIn("fine-dining", cluster_slugs)

    def test_typeahead_matches_template_name(self):
        payload = selectors.search_templates_typeahead("vertex")
        template_slugs = [t["slug"] for t in payload["templates"]]
        self.assertIn("vertex-creative-agency", template_slugs)

    def test_typeahead_matches_role_label(self):
        payload = selectors.search_templates_typeahead("avvocat")
        role_slugs = [r["slug"] for r in payload["roles"]]
        self.assertIn("avvocati", role_slugs)

    def test_get_templates_by_cluster(self):
        cluster, qs = selectors.get_templates_by_cluster("specialist")
        self.assertEqual(cluster.slug, "specialist")
        self.assertEqual(
            set(qs.values_list("slug", flat=True)),
            {"cardio-studio-specialistico", "dermatologia-elite-roma"},
        )

    def test_get_templates_by_cluster_404_on_unknown(self):
        with self.assertRaises(Http404):
            selectors.get_templates_by_cluster("does-not-exist-cluster")

    def test_get_templates_by_role(self):
        role, qs = selectors.get_templates_by_role("avvocati")
        self.assertEqual(role["slug"], "avvocati")
        self.assertEqual(
            set(qs.values_list("slug", flat=True)),
            {"lex-studio-legale", "juris-avvocato-moderno"},
        )

    def test_get_templates_by_role_404_on_unknown(self):
        with self.assertRaises(Http404):
            selectors.get_templates_by_role("unknown-role")

    def test_get_templates_by_use_case(self):
        use_case, qs = selectors.get_templates_by_use_case("sell-online")
        self.assertEqual(use_case["slug"], "sell-online")
        self.assertEqual(
            set(qs.values_list("slug", flat=True)),
            {"bottega-shop-artigianale", "luxe-fashion-store"},
        )

    def test_get_templates_by_use_case_404_on_unknown(self):
        with self.assertRaises(Http404):
            selectors.get_templates_by_use_case("unknown-use-case")


class DiscoveryViewTests(_SeededCatalogMixin, TestCase):
    """HTTP coverage for X.2 Commit 4 views + legacy routes."""

    def test_legacy_template_list_200(self):
        r = self.client.get("/templates/")
        self.assertEqual(r.status_code, 200)

    def test_legacy_category_listing_200(self):
        r = self.client.get("/templates/restaurant/")
        self.assertEqual(r.status_code, 200)

    def test_legacy_template_detail_200(self):
        r = self.client.get("/templates/restaurant/gusto-fine-dining/")
        self.assertEqual(r.status_code, 200)

    def test_legacy_template_detail_exposes_pills(self):
        r = self.client.get("/templates/restaurant/gusto-fine-dining/")
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Fine dining", body)          # cluster pill
        self.assertIn("Editorial warm", body)       # visual style pill
        self.assertIn("Premium", body)              # price tier pill label

    def test_listing_filter_by_cluster_query_string(self):
        r = self.client.get("/templates/?cluster=fine-dining")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Gusto", body)
        self.assertNotIn("Bottega", body)

    def test_listing_filter_by_feature_query_string(self):
        r = self.client.get("/templates/?feature=has_shop")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Bottega", body)
        self.assertIn("Luxe", body)
        self.assertNotIn("Vertex Studio", body)

    def test_typeahead_endpoint_returns_json(self):
        r = self.client.get("/templates/search/typeahead/?q=fine")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r["Content-Type"], "application/json")
        payload = json.loads(r.content)
        self.assertIn("templates", payload)
        self.assertIn("clusters", payload)
        self.assertIn("roles", payload)

    def test_typeahead_endpoint_empty_query_200(self):
        r = self.client.get("/templates/search/typeahead/?q=")
        self.assertEqual(r.status_code, 200)
        payload = json.loads(r.content)
        self.assertEqual(payload["templates"], [])

    def test_typeahead_endpoint_clamps_limit(self):
        r = self.client.get("/templates/search/typeahead/?q=agenzia&limit=200")
        self.assertEqual(r.status_code, 200)

    def test_cluster_detail_200(self):
        r = self.client.get("/templates/clusters/fine-dining/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Fine dining", body)
        self.assertIn("Gusto", body)

    def test_cluster_detail_404_on_unknown(self):
        r = self.client.get("/templates/clusters/does-not-exist/")
        self.assertEqual(r.status_code, 404)

    def test_role_discovery_200(self):
        r = self.client.get("/templates/for-role/avvocati/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Per avvocati", body)
        self.assertIn("Lex", body)

    def test_role_discovery_404_on_unknown(self):
        r = self.client.get("/templates/for-role/nonexistent-role/")
        self.assertEqual(r.status_code, 404)

    def test_use_case_discovery_200(self):
        r = self.client.get("/templates/for-use-case/sell-online/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Vendere online", body)
        self.assertIn("Bottega", body)
        self.assertIn("Luxe", body)

    def test_use_case_discovery_404_on_unknown(self):
        r = self.client.get("/templates/for-use-case/unknown/")
        self.assertEqual(r.status_code, 404)

    def test_fixed_prefix_paths_resolve_before_category_catchall(self):
        # The URL routing invariant: `clusters/`, `search/`, `for-role/`
        # and `for-use-case/` MUST resolve to their dedicated views,
        # not to the category-listing catch-all.
        # If resolution drifted, the assert below would return 404
        # from the category lookup inside the listing view.
        urls = [
            "/templates/clusters/fine-dining/",
            "/templates/search/typeahead/?q=fine",
            "/templates/for-role/avvocati/",
            "/templates/for-use-case/sell-online/",
        ]
        for url in urls:
            r = self.client.get(url)
            self.assertEqual(
                r.status_code,
                200,
                f"Fixed prefix path {url} must resolve to its dedicated "
                f"view — URL ordering drift detected.",
            )

    def test_editor_untouched_invariant(self):
        # X.2 Commit 4 scope guard: catalog discovery must not have
        # imported anything from apps.editor (the enrollment program
        # is closed — D-099 binding). A breakage here means a view
        # reached outside its approved scope.
        import apps.catalog.views as cat_views
        import apps.catalog.selectors as cat_selectors
        self.assertFalse(
            hasattr(cat_views, "apply_project_overrides")
            and cat_views.apply_project_overrides.__module__ != "apps.editor.rendering",
            "Catalog views must import apply_project_overrides from "
            "apps.editor.rendering verbatim — not reimplement it.",
        )
        # The selectors layer must not have grown an editor dependency.
        self.assertNotIn("editor", cat_selectors.__file__)


# Ensure Http404 is imported for the test suite (used by selector 404 tests).
from django.http import Http404  # noqa: E402


# ── X.2 Commit 5 · homepage discovery context + render ────────────


class HomepageDiscoveryTests(_SeededCatalogMixin, TestCase):
    """Homepage (``/``) must render the X.2 discovery surface end-to-end.

    Locks the context wiring (search-typeahead URL, role cards,
    use-case cards, trust counters) and the rendered-HTML shape so a
    future template edit that drops a block fails loudly instead of
    silently shrinking the hero.
    """

    def setUp(self):
        self.response = self.client.get("/")

    def test_home_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_exposes_typeahead_endpoint_hook(self):
        # The hero search form must wire the typeahead root + point at
        # the taxonomy-typeahead URL introduced in Commit 4. typeahead.js
        # is loaded via a <script src="..."> tag at the bottom of the
        # page and binds to any input inside a ``data-typeahead-root``
        # node — assert both signals are in the rendered HTML.
        body = self.response.content.decode("utf-8", "ignore")
        self.assertIn("data-typeahead-root", body)
        self.assertIn("/static/js/typeahead.js", body)

    def test_home_search_form_submits_to_catalog_listing(self):
        body = self.response.content.decode("utf-8", "ignore")
        self.assertIn('action="/templates/"', body)
        self.assertIn('name="q"', body)

    def test_home_includes_role_discovery_entries(self):
        # At least the 6 canonical roles (avvocati · medici · ristoratori
        # · startup · fotografi · artigiani) must appear in the rendered
        # HTML as linked role-discovery cards.
        ctx = self.response.context
        role_slugs = {role["slug"] for role in ctx["home_roles"]}
        for slug in ("avvocati", "medici", "ristoratori", "startup",
                     "fotografi", "artigiani"):
            self.assertIn(
                slug,
                role_slugs,
                f"Homepage role grid must expose '{slug}' role card.",
            )
        body = self.response.content.decode("utf-8", "ignore")
        self.assertIn("/templates/for-role/avvocati/", body)
        self.assertIn("/templates/for-role/medici/", body)

    def test_home_includes_use_case_entries(self):
        ctx = self.response.context
        uc_slugs = {uc["slug"] for uc in ctx["home_use_cases"]}
        for slug in ("sell-online", "reservations", "appointment-booking",
                     "show-portfolio", "generate-leads"):
            self.assertIn(
                slug,
                uc_slugs,
                f"Homepage use-case grid must expose '{slug}' card.",
            )
        body = self.response.content.decode("utf-8", "ignore")
        self.assertIn("/templates/for-use-case/sell-online/", body)
        self.assertIn("/templates/for-use-case/show-portfolio/", body)

    def test_home_trust_counters_are_live_from_db(self):
        counters = self.response.context["trust_counters"]
        # Seeded DB: 20 MVP templates all published_live, 15 macro-
        # categories (8 MVP + 7 extras from seed_profession_clusters),
        # 52 profession clusters, 5 canonical locales.
        self.assertEqual(counters["templates_live"], 20)
        self.assertEqual(counters["categories_active"], 15)
        self.assertEqual(counters["clusters_active"], 52)
        self.assertEqual(counters["locales_supported"], 5)

    def test_home_trust_counters_render_in_html(self):
        body = self.response.content.decode("utf-8", "ignore")
        self.assertIn("20+", body)   # templates_live
        self.assertIn("52", body)    # clusters_active
        self.assertIn("professioni", body)
        self.assertIn("RTL", body)

    def test_home_features_featured_templates(self):
        ctx = self.response.context
        featured = list(ctx["featured_templates"])
        self.assertGreater(len(featured), 0, "Featured pool must be non-empty on seeded DB.")
        body = self.response.content.decode("utf-8", "ignore")
        # At least one featured template name should surface in the
        # rendered card grid.
        self.assertTrue(
            any(tpl.name in body for tpl in featured),
            "At least one featured template name must appear on the rendered homepage.",
        )

    def test_home_exposes_how_it_works_anchor(self):
        body = self.response.content.decode("utf-8", "ignore")
        self.assertIn('id="come-funziona"', body)
        self.assertIn("Scegli", body)
        self.assertIn("Personalizza", body)
        self.assertIn("Pubblica", body)

    def test_home_category_chips_point_to_catalog_routes(self):
        body = self.response.content.decode("utf-8", "ignore")
        # Each category link must point to the catalog per-category
        # listing URL — spot-check 2 MVP slugs.
        self.assertIn("/templates/agency/", body)
        self.assertIn("/templates/restaurant/", body)


class HomepageEmptyDbSafetyTests(TestCase):
    """Homepage must not 500 when the DB is empty (fresh dev env · pre-seed).

    Locks the ``or []`` / counter fallback contract in the view: trust
    counters render 0, discovery grids render empty, and the legacy
    featured pool returns an empty list. No seed chain runs in
    ``setUpTestData`` — this is the empty-DB invariant.
    """

    def test_home_200_on_empty_db(self):
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)

    def test_home_trust_counters_zero_on_empty_db(self):
        r = self.client.get("/")
        c = r.context["trust_counters"]
        self.assertEqual(c["templates_live"], 0)
        self.assertEqual(c["categories_active"], 0)
        self.assertEqual(c["clusters_active"], 0)
        self.assertEqual(c["locales_supported"], 5)


class HomepageScopeInvariantTests(TestCase):
    """X.2 Commit 5 scope guard: editor + catalog internals untouched."""

    def test_pages_views_does_not_import_editor(self):
        import apps.pages.views as pv
        src = open(pv.__file__, "r", encoding="utf-8").read()
        self.assertNotIn("apps.editor", src)
        self.assertNotIn("apps.projects", src)
        self.assertNotIn("apps.commerce", src)

    def test_home_template_does_not_reach_into_live_templates(self):
        # The homepage must not render archetype live_templates paths —
        # those belong to /templates/<cat>/<slug>/preview/.
        from django.template import engines
        django_engine = engines["django"]
        src = django_engine.get_template("pages/home.html").template.source
        self.assertNotIn("live_templates/", src)
        self.assertNotIn("editor/preview-bridge", src)


# ── X.3 Commit 4 · taxonomy-driven related-templates selector ─────


class RelatedTemplatesTaxonomyTests(_SeededCatalogMixin, TestCase):
    """``get_related_templates`` honors the layered priority contract:
    same-cluster → same-style → same-category, exclude-self, distinct,
    deterministic, ``limit`` respected.
    """

    def _related_slugs(self, slug, limit=3, include_drafts=False):
        tpl = WebTemplate.objects.get(slug=slug)
        return [
            t.slug
            for t in selectors.get_related_templates(
                tpl, limit=limit, include_drafts=include_drafts
            )
        ]

    def test_same_cluster_priority_cardio_returns_derm_first(self):
        """Cardio + Derm share cluster `specialist` · Derm must be first."""
        slugs = self._related_slugs("cardio-studio-specialistico")
        self.assertGreater(len(slugs), 0)
        self.assertEqual(slugs[0], "dermatologia-elite-roma")

    def test_same_cluster_priority_derm_returns_cardio_first(self):
        """Symmetry · Derm's related starts with Cardio (same cluster)."""
        slugs = self._related_slugs("dermatologia-elite-roma")
        self.assertGreater(len(slugs), 0)
        self.assertEqual(slugs[0], "cardio-studio-specialistico")

    def test_same_style_fallback_when_cluster_is_singleton(self):
        """Villa's cluster `real-estate-luxury` is singleton; its style
        `cinematic-fullbleed` is shared with Pixel · style layer must fire."""
        slugs = self._related_slugs("villa-immobili-lusso")
        self.assertIn(
            "pixel-portfolio-fotografico",
            slugs,
            f"expected Pixel via style layer, got {slugs}",
        )

    def test_same_category_fallback_luxe_includes_bottega(self):
        """Luxe's cluster singleton + style singleton · category `ecommerce`
        contains Bottega → fallback to category layer must pick it up."""
        slugs = self._related_slugs("luxe-fashion-store")
        self.assertIn(
            "bottega-shop-artigianale",
            slugs,
            f"expected Bottega via category layer, got {slugs}",
        )

    def test_pragma_falls_back_gracefully(self):
        """Pragma's cluster `corporate` has only Pragma; style
        `classic-serif` includes Lex; category `business` has Elevate.
        Should return Lex + Elevate (no errors, no empties)."""
        slugs = self._related_slugs("pragma-corporate-suite")
        self.assertGreater(len(slugs), 0)
        self.assertIn("lex-studio-legale", slugs)
        self.assertIn("elevate-startup-landing", slugs)

    def test_exclude_self_invariant(self):
        """Every related set must never contain the source template itself."""
        for slug in WebTemplate.objects.values_list("slug", flat=True):
            slugs = self._related_slugs(slug, limit=3)
            self.assertNotIn(
                slug,
                slugs,
                f"{slug} appeared in its own related set",
            )

    def test_distinct_no_duplicate_slugs(self):
        """A template in cluster+style+category intersection must appear
        at most once · the layered union de-duplicates."""
        for slug in WebTemplate.objects.values_list("slug", flat=True):
            slugs = self._related_slugs(slug, limit=5)
            self.assertEqual(
                len(slugs),
                len(set(slugs)),
                f"duplicate slug in related set for {slug}: {slugs}",
            )

    def test_limit_respected(self):
        """Returned set never exceeds the requested limit."""
        for limit in (0, 1, 3, 5, 10):
            slugs = self._related_slugs("cardio-studio-specialistico", limit=limit)
            self.assertLessEqual(
                len(slugs),
                limit,
                f"limit {limit} violated: got {len(slugs)}",
            )

    def test_limit_zero_returns_empty(self):
        slugs = self._related_slugs("cardio-studio-specialistico", limit=0)
        self.assertEqual(slugs, [])

    def test_deterministic_across_repeated_calls(self):
        """Two consecutive calls with the same args must return the same
        slug order · no randomness allowed."""
        for slug in (
            "cardio-studio-specialistico",
            "luxe-fashion-store",
            "pragma-corporate-suite",
            "vertex-creative-agency",
        ):
            a = self._related_slugs(slug, limit=3)
            b = self._related_slugs(slug, limit=3)
            self.assertEqual(a, b, f"non-deterministic order for {slug}: {a} != {b}")

    def test_include_drafts_false_respected(self):
        """Draft tier templates MUST NOT appear in related results when
        ``include_drafts=False`` (default)."""
        # Demote Derm to draft to prove the gate.
        derm = WebTemplate.objects.get(slug="dermatologia-elite-roma")
        derm.tier = WebTemplate.Tier.DRAFT
        derm.save(update_fields=["tier"])
        try:
            slugs = self._related_slugs("cardio-studio-specialistico")
            self.assertNotIn(
                "dermatologia-elite-roma",
                slugs,
                "draft Derm must not surface with include_drafts=False",
            )
        finally:
            derm.tier = WebTemplate.Tier.PUBLISHED_LIVE
            derm.save(update_fields=["tier"])

    def test_include_drafts_true_widens_pool(self):
        """With ``include_drafts=True`` (staff preview path), drafts are
        visible in the related set."""
        derm = WebTemplate.objects.get(slug="dermatologia-elite-roma")
        derm.tier = WebTemplate.Tier.DRAFT
        derm.save(update_fields=["tier"])
        try:
            slugs = self._related_slugs(
                "cardio-studio-specialistico", include_drafts=True
            )
            self.assertIn(
                "dermatologia-elite-roma",
                slugs,
                "draft Derm must surface with include_drafts=True",
            )
        finally:
            derm.tier = WebTemplate.Tier.PUBLISHED_LIVE
            derm.save(update_fields=["tier"])

    def test_layer_ordering_cluster_beats_style_beats_category(self):
        """Explicit layer-priority sanity · with a fully-populated catalog
        the cluster layer is drained first, style second, category third.
        Vertex: cluster `creative` is singleton (only Vertex); style
        `editorial-warm` is shared with Gusto/Sapore/Chiara; category
        `agency` contains Aura. Expected order: style siblings before
        category fallback (Aura)."""
        slugs = self._related_slugs("vertex-creative-agency", limit=4)
        # Aura (same category, not same style) should be AFTER at least
        # one style sibling (editorial-warm: Gusto / Sapore / Chiara).
        style_siblings = {
            "gusto-fine-dining",
            "sapore-trattoria-pizzeria",
            "chiara-portfolio-creativo",
        }
        earliest_style_idx = min(
            (slugs.index(s) for s in slugs if s in style_siblings),
            default=None,
        )
        if "aura-digital-studio" in slugs and earliest_style_idx is not None:
            self.assertLess(
                earliest_style_idx,
                slugs.index("aura-digital-studio"),
                f"style siblings must come before category fallback: {slugs}",
            )

    def test_return_shape_is_iterable_with_webtemplate_attrs(self):
        """Regression guard · views/templates iterate the result and read
        ``.name``, ``.slug``, ``.category``, ``.brand`` — the refactor
        changed QuerySet → list but the contract must hold."""
        tpl = WebTemplate.objects.get(slug="cardio-studio-specialistico")
        related = selectors.get_related_templates(tpl, limit=3)
        for r in related:
            self.assertIsInstance(r, WebTemplate)
            self.assertTrue(r.slug)
            self.assertTrue(r.name)
            self.assertTrue(r.category)

    def test_template_without_taxonomy_falls_back_to_category(self):
        """Defensive: the selector still walks the category fallback
        path when ``profession_cluster`` / ``visual_style`` are absent
        on the query source. Simulated via an in-memory WebTemplate
        that is NOT persisted — persisting a FK-less row would fail
        post-X.3 Commit 5 (NOT NULL flip)."""
        source = WebTemplate.objects.get(slug="vertex-creative-agency")
        # In-memory copy with stripped taxonomy · NEVER .save()ed.
        ghost = WebTemplate(
            pk=source.pk,
            name=source.name,
            slug=source.slug,
            category=source.category,
            description=source.description,
            profession_cluster_id=None,
            visual_style_id=None,
        )
        slugs = [
            t.slug
            for t in selectors.get_related_templates(ghost, limit=3)
        ]
        self.assertGreater(
            len(slugs),
            0,
            "template without taxonomy must still get category fallback",
        )
        for s in slugs:
            sibling = WebTemplate.objects.get(slug=s)
            self.assertEqual(sibling.category_id, ghost.category_id)


# ── X.3 Commit 5 · NOT NULL flip on profession_cluster + visual_style


class TaxonomyNotNullContractTests(_SeededCatalogMixin, TestCase):
    """After X.3 Commit 5, every WebTemplate row carries a
    ``profession_cluster`` and a ``visual_style`` FK by schema law.
    The NOT NULL flip is a trivial schema migration (0005) safe on
    the MVP 20-row catalog because X.2 Commit 3 backfilled all rows.
    """

    def test_all_seeded_templates_have_profession_cluster(self):
        missing = list(
            WebTemplate.objects.filter(profession_cluster__isnull=True).values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(
            missing,
            [],
            f"post-flip invariant: no template may have NULL "
            f"profession_cluster · missing on {missing}",
        )

    def test_all_seeded_templates_have_visual_style(self):
        missing = list(
            WebTemplate.objects.filter(visual_style__isnull=True).values_list(
                "slug", flat=True
            )
        )
        self.assertEqual(
            missing,
            [],
            f"post-flip invariant: no template may have NULL "
            f"visual_style · missing on {missing}",
        )

    def test_seeded_count_unchanged_by_migration(self):
        """No seeded row may be lost by migration 0005's NOT NULL
        flip. Count is derived from seed metadata so Wave 2 additions
        (which extend the seed but not the historical migration)
        don't require manual test updates."""
        self.assertEqual(
            WebTemplate.objects.count(),
            len(SEED_TEMPLATE_METADATA),
        )

    def test_cluster_category_invariant_preserved(self):
        """cluster.category == template.category · holds post-flip."""
        for tpl in WebTemplate.objects.all():
            self.assertEqual(
                tpl.profession_cluster.category_id,
                tpl.category_id,
                f"cluster/category mismatch on {tpl.slug}",
            )

    def test_create_without_profession_cluster_raises(self):
        """Creating a WebTemplate without profession_cluster must fail
        at the DB layer (IntegrityError) now that the column is NOT
        NULL. Use ``.objects.create`` which performs the INSERT."""
        category = Category.objects.get(slug="business")
        style = VisualStyle.objects.get(slug="dashboard-dark")
        with self.assertRaises(IntegrityError), transaction.atomic():
            WebTemplate.objects.create(
                name="Ghost No Cluster",
                slug="ghost-no-cluster",
                category=category,
                description="ghost",
                visual_style=style,
                # profession_cluster intentionally omitted
            )

    def test_create_without_visual_style_raises(self):
        category = Category.objects.get(slug="business")
        cluster = ProfessionCluster.objects.get(slug="corporate")
        with self.assertRaises(IntegrityError), transaction.atomic():
            WebTemplate.objects.create(
                name="Ghost No Style",
                slug="ghost-no-style",
                category=category,
                description="ghost",
                profession_cluster=cluster,
                # visual_style intentionally omitted
            )

    def test_create_with_both_fks_succeeds(self):
        """Positive control · ensures the flip didn't over-tighten."""
        category = Category.objects.get(slug="business")
        cluster = ProfessionCluster.objects.get(slug="corporate")
        style = VisualStyle.objects.get(slug="dashboard-dark")
        tpl = WebTemplate.objects.create(
            name="Ghost Complete",
            slug="ghost-complete",
            category=category,
            description="ghost",
            profession_cluster=cluster,
            visual_style=style,
        )
        self.assertEqual(tpl.profession_cluster, cluster)
        self.assertEqual(tpl.visual_style, style)

    def test_category_fk_still_required_unchanged(self):
        """X.3 Commit 5 does NOT touch ``category`` · legacy FK still
        required, behaviour identical to pre-flip."""
        with self.assertRaises(IntegrityError), transaction.atomic():
            WebTemplate.objects.create(
                name="Ghost No Category",
                slug="ghost-no-category",
                description="ghost",
                # category intentionally omitted
            )

    def test_model_field_declarations_reflect_not_null(self):
        """The model definition itself must carry null=False on both
        FKs · guards against a future revert that silently re-loosens
        the contract without a corresponding migration."""
        pc_field = WebTemplate._meta.get_field("profession_cluster")
        vs_field = WebTemplate._meta.get_field("visual_style")
        self.assertFalse(pc_field.null, "profession_cluster must be null=False")
        self.assertFalse(vs_field.null, "visual_style must be null=False")

    def test_discovery_surfaces_no_regression(self):
        """End-to-end smoke at the selector level: the 3 X.2 Commit 4
        discovery helpers still work post-flip (no code path regressed
        against the NULL-is-possible assumption that was removed)."""
        _, qs = selectors.get_listing_templates()
        self.assertEqual(qs.count(), 20)
        counts = selectors.get_facet_counts(qs)
        self.assertEqual(counts["total"], 20)
        self.assertGreater(len(counts["clusters"]), 0)
        self.assertGreater(len(counts["styles"]), 0)

    def test_migration_0005_is_schema_only(self):
        """Guardrail · migration 0005 must contain only AlterField
        operations · no data migration / RunPython / RunSQL crept in."""
        import importlib

        mig = importlib.import_module(
            "apps.catalog.migrations.0005_taxonomy_v2_not_null"
        )
        for op in mig.Migration.operations:
            self.assertEqual(
                type(op).__name__,
                "AlterField",
                f"migration 0005 op {op} must be AlterField (schema-only)",
            )
