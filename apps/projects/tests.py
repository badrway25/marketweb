"""Editor Foundation v1 unit tests."""
from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from django.core.management import call_command
from apps.catalog import template_content
from apps.catalog.models import WebTemplate
from apps.editor.schema import (
    InvalidEditableField,
    get_field_spec,
    is_supported_archetype,
    iter_groups,
    validate_key_path,
    validate_value,
)
from apps.projects import services
from apps.projects.models import CustomerProject


User = get_user_model()


def _seed_catalog():
    call_command("seed_categories", verbosity=0)
    call_command("seed_templates", verbosity=0)
    call_command("sync_template_tiers", verbosity=0)


class FoundationModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        _seed_catalog()
        cls.owner = User.objects.create_user("owner", password="x")
        cls.other = User.objects.create_user("other", password="x")
        cls.vertex = WebTemplate.objects.get(slug="vertex-creative-agency")

    def test_create_project_seeds_tokens_and_revision(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        self.assertEqual(p.source_archetype, "agency-creative-studio")
        self.assertEqual(p.source_category_slug, "agency")
        self.assertEqual(p.status, CustomerProject.Status.DRAFT)
        self.assertIsNotNone(p.tokens)
        self.assertEqual(p.revisions.count(), 1)

    def test_unsupported_archetype_raises(self):
        gusto = WebTemplate.objects.get(slug="gusto-fine-dining")
        with self.assertRaises(services.UnsupportedTemplate):
            services.create_project_from_template(owner=self.owner, template=gusto)

    def test_schema_locks_non_whitelisted_keys(self):
        self.assertTrue(is_supported_archetype("agency-creative-studio"))
        validate_key_path("agency-creative-studio", "home.headline")
        with self.assertRaises(InvalidEditableField):
            validate_key_path("agency-creative-studio", "home.capab_items")
        with self.assertRaises(InvalidEditableField):
            validate_key_path("agency-creative-studio", "section_order")

    def test_schema_value_validators(self):
        validate_value("agency-creative-studio", "home.primary_href", "contatti")
        with self.assertRaises(InvalidEditableField):
            validate_value("agency-creative-studio", "home.primary_href", "not-a-page")
        spec = get_field_spec("agency-creative-studio", "home.intro")
        self.assertEqual(spec["type"], "textarea")

    def test_save_edits_creates_then_updates_then_clears(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.headline": "Primo scatto <em>editoriale</em>."},
        )
        self.assertEqual(p.content_overrides.count(), 1)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.headline": "Secondo scatto."},
        )
        self.assertEqual(p.content_overrides.count(), 1)
        from apps.catalog import template_content
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.headline": baseline["home"]["headline"]},
        )
        self.assertEqual(p.content_overrides.count(), 0)

    def test_publish_transitions_and_snapshots(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.eyebrow": "Progetto cliente"},
        )
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)
        rev = p.revisions.filter(reason="publish").first()
        self.assertIn("home.eyebrow", rev.snapshot["content"])

    def test_schema_groups_declare_valid_page(self):
        """A.2.5: every group must carry a `page` slug matching the
        template's authored pages list (or `*` for chrome)."""
        vertex_pages = {
            p["slug"]
            for p in template_content.get_content("vertex-creative-agency", "it")["pages"]
        }
        allowed = vertex_pages | {"*"}
        for group in iter_groups("agency-creative-studio"):
            with self.subTest(group=group["id"]):
                self.assertIn("page", group,
                              f"Group '{group['id']}' missing 'page' key.")
                self.assertIn(group["page"], allowed,
                              f"Group '{group['id']}' page='{group['page']}' "
                              f"not in {sorted(allowed)}.")

    def test_preview_url_for_page_shapes(self):
        """A.2.5: preview URL builder handles home implicitly and adds
        the page segment for non-home pages, always with ?project=."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        self.assertEqual(
            p.preview_url_for_page("home"),
            f"/templates/agency/vertex-creative-agency/preview/?project={p.uuid}",
        )
        self.assertEqual(
            p.preview_url_for_page("studio"),
            f"/templates/agency/vertex-creative-agency/preview/studio/?project={p.uuid}",
        )
        self.assertEqual(
            p.preview_url_for_page(None),
            f"/templates/agency/vertex-creative-agency/preview/?project={p.uuid}",
        )
        self.assertEqual(
            p.preview_url_path,
            "/templates/agency/vertex-creative-agency/preview/",
        )

    def test_dict_path_overrides_merge_into_baseline_dict(self):
        """A.2.6a: a leaf override into a dict-shaped registry slot
        (e.g. contatti.labels.name) must merge into the baseline dict
        without wiping sibling keys."""
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                "contatti.labels.name":  "Nome completo",
                "contatti.labels.email": "Indirizzo email",
            },
        )
        tree = p.get_overrides_dict()
        self.assertEqual(tree["contatti"]["labels"]["name"],  "Nome completo")
        self.assertEqual(tree["contatti"]["labels"]["email"], "Indirizzo email")

        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        self.assertEqual(merged["contatti"]["labels"]["name"],  "Nome completo")
        self.assertEqual(merged["contatti"]["labels"]["email"], "Indirizzo email")
        # Sibling keys not overridden remain at baseline.
        self.assertEqual(merged["contatti"]["labels"]["role"],   "Ruolo nell'organizzazione")
        self.assertEqual(merged["contatti"]["labels"]["budget"], "Banda di budget indicativa")

    def test_a26a_contatti_scalar_fields_whitelisted(self):
        """A.2.6a: the 23 new contatti scalar / dict-key fields are
        whitelisted for write."""
        new_paths = [
            "contatti.form_submit_label",
            "contatti.form_submit_note",
            "contatti.labels.name",
            "contatti.labels.role",
            "contatti.labels.company",
            "contatti.labels.email",
            "contatti.labels.discipline",
            "contatti.labels.budget",
            "contatti.labels.brief",
            "contatti.placeholders.name",
            "contatti.placeholders.role",
            "contatti.placeholders.company",
            "contatti.placeholders.email",
            "contatti.placeholders.brief",
            "contatti.direct_label",
            "contatti.direct_heading",
            "contatti.studio_label",
            "contatti.reply_label",
            "contatti.reply_heading",
            "contatti.reply_body",
            "contatti.channels_label",
            "contatti.promise_label",
            "contatti.promise_heading",
        ]
        for path in new_paths:
            with self.subTest(path=path):
                validate_key_path("agency-creative-studio", path)
                self.assertIsNotNone(get_field_spec("agency-creative-studio", path))

    # ── A.2.6b · Indexed-row contract ───────────────────────────────

    def test_a26b_schema_size_meets_target(self):
        """A.2.6b: indexed-row contract must lift the editable-field
        count to at least 250 (target band 260-280, +5 design tokens
        on top in the editor surface)."""
        from apps.editor.schema import iter_editable_fields, iter_groups
        fields = iter_editable_fields("agency-creative-studio")
        groups = iter_groups("agency-creative-studio")
        self.assertGreaterEqual(len(fields), 250,
            f"Field coverage regressed below A.2.6b floor: {len(fields)}")
        # 14 curated + 18 indexed list groups = 32.
        self.assertGreaterEqual(len(groups), 32)

    def test_a26b_tuple_cell_splice_preserves_siblings(self):
        """A.2.6b: editing studio.facts.0.label must update only the
        target cell — other columns of row 0 and other rows stay at
        baseline."""
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                "studio.facts.0.label":  "anni di attività dello studio",
                "studio.facts.2.number": "12",
            },
        )
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        facts = merged["studio"]["facts"]
        # Row 0: label changed, number / sub preserved.
        self.assertEqual(facts[0][0], "8")  # number col untouched
        self.assertEqual(facts[0][1], "anni di attività dello studio")
        self.assertEqual(facts[0][2], "Fondato nel 2018 a Milano")
        # Row 1: fully baseline.
        self.assertEqual(facts[1][0], "42")
        self.assertEqual(facts[1][1], "progetti in archivio")
        # Row 2: number changed, label / sub preserved.
        self.assertEqual(facts[2][0], "12")
        self.assertEqual(facts[2][1], "collaboratori")
        # Row count unchanged — repeater cannot add rows in A.2.6.
        self.assertEqual(len(facts), 4)

    def test_a26b_dict_cell_splice_preserves_siblings(self):
        """A.2.6b: editing studio.partners.1.name must update only
        that key — other keys of partner 1 and other partners stay at
        baseline."""
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.partners.1.name": "Tommaso B. Boeri"},
        )
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        partners = merged["studio"]["partners"]
        self.assertEqual(partners[1]["name"], "Tommaso B. Boeri")
        self.assertEqual(partners[1]["role"], "Co-fondatore · Direttore artistico")
        # Other partners untouched.
        self.assertEqual(partners[0]["name"], "Margherita Serafini")
        self.assertEqual(partners[2]["name"], "Ilaria Ferri")

    def test_a26b_scalar_list_cell_splice_preserves_siblings(self):
        """A.2.6b: editing home.press_publications.2 (a plain string
        list) must update only that index."""
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.press_publications.2": "Apartamento"},
        )
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        pubs = merged["home"]["press_publications"]
        self.assertEqual(pubs[2], "Apartamento")
        self.assertEqual(pubs[0], "Monocle")  # untouched
        self.assertEqual(pubs[1], "Domus")    # untouched
        self.assertEqual(len(pubs), 8)        # row count preserved

    def test_a26b_indexed_paths_validate(self):
        """A.2.6b: every indexed cell of every shaped list is a
        whitelisted key, and out-of-range / unknown-column / locked
        column writes are rejected."""
        from apps.editor.schema import (
            STRUCTURED_FIELD_SHAPES, get_field_spec,
        )
        # Sample: one cell per list at row 0, plus a known-locked column.
        sampling = [
            "home.ledger_rows.0.title",
            "home.capab_items.0.title",
            "home.press_publications.0",
            "home.manifesto_principles.0.title",
            "studio.facts.0.number",
            "studio.partners.0.name",
            "studio.timeline_rows.0.year",
            "capacita.disciplines.0.title",
            "capacita.engagement_tiles.0.title",
            "lavori.filters.0",
            "lavori.projects.0.title",
            "lavori.archive_stats.0.number",
            "manifesto.phases.0.title",
            "manifesto.principles.0.title",
            "manifesto.promise_stats.0.number",
            "contatti.discipline_options.0",
            "contatti.budget_bands.0.label",
            "contatti.channels.0.value",
        ]
        # All 18 lists must contribute an editable cell.
        self.assertEqual(len(sampling), len(STRUCTURED_FIELD_SHAPES["agency-creative-studio"]))
        for path in sampling:
            with self.subTest(path=path):
                validate_key_path("agency-creative-studio", path)
                self.assertIsNotNone(get_field_spec("agency-creative-studio", path))
        # Locked tuple columns (slug, num) stay rejected.
        for locked in [
            "home.ledger_rows.0.slug",        # route slug column
            "home.ledger_rows.0.discipline",  # not exposed in A.2.6b
            "lavori.projects.0.slug",         # route slug
            "lavori.projects.0.index",        # ordinal
            "studio.partners.0.creds",        # nested list, not exposed
            "manifesto.phases.0.deliverables",# nested list
            "contatti.budget_bands.0.slug",   # locked
        ]:
            with self.subTest(path=locked):
                with self.assertRaises(InvalidEditableField):
                    validate_key_path("agency-creative-studio", locked)
        # Whole-list overwrite still locked even though cells are open.
        with self.assertRaises(InvalidEditableField):
            validate_key_path("agency-creative-studio", "studio.facts")
        with self.assertRaises(InvalidEditableField):
            validate_key_path("agency-creative-studio", "lavori.projects")

    def test_a26b_indexed_out_of_range_rejected(self):
        """A.2.6b: write to a row beyond the baseline length must
        raise InvalidEditableField."""
        # studio.facts has 4 baseline rows → index 4+ is out of range.
        with self.assertRaises(InvalidEditableField):
            validate_key_path("agency-creative-studio", "studio.facts.4.label")
        with self.assertRaises(InvalidEditableField):
            validate_key_path("agency-creative-studio", "studio.partners.7.name")

    def test_a26b_indexed_baseline_resolves_for_all_three_shapes(self):
        """A.2.6b: the editor sidebar prefills inputs with the
        baseline value when no override is present. The resolver must
        therefore walk through list indices AND translate tuple-column
        names back to tuple positions."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # Tuple column (studio.facts is a tuple list, "label" is col 1)
        self.assertEqual(
            services.resolve_path_in_baseline(p, "studio.facts.0.label"),
            "anni di attività",
        )
        # Dict-list column (studio.partners[1].name)
        self.assertEqual(
            services.resolve_path_in_baseline(p, "studio.partners.1.name"),
            "Tommaso Boeri",
        )
        # Scalar list cell (home.press_publications[0])
        self.assertEqual(
            services.resolve_path_in_baseline(p, "home.press_publications.0"),
            "Monocle",
        )
        # Out-of-range gracefully returns None (does not crash).
        self.assertIsNone(services.resolve_path_in_baseline(p, "studio.facts.99.label"))

    def test_a26b_indexed_sparse_diff_deletes_row_on_baseline_match(self):
        """A.2.6b: writing the baseline value back into an indexed
        cell must drop the override row (sparse-diff). Critical so a
        customer who 'undoes' an edit doesn't leave dead overrides
        behind that block future DNA polish."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # First, override studio.facts.0.label.
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.facts.0.label": "Mutato per test"},
        )
        self.assertEqual(p.content_overrides.filter(key_path="studio.facts.0.label").count(), 1)
        # Now write the baseline value back. The row should be deleted.
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.facts.0.label": "anni di attività"},
        )
        self.assertEqual(p.content_overrides.filter(key_path="studio.facts.0.label").count(), 0)

    def test_a26b_indexed_save_then_render_end_to_end(self):
        """A.2.6b: save four indexed edits, render preview HTML, and
        assert all four overlay strings appear (and the locked
        columns remain at baseline)."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                "studio.facts.0.label":         "anni di indipendenza",
                "lavori.projects.2.title":      "Manuale di marca rinnovato",
                "contatti.channels.0.value":    "studio@walker.test",
                "home.press_publications.0":    "Apartamento Magazine",
            },
        )
        # Use the rendering function directly so we don't need the HTTP layer.
        from apps.editor.rendering import apply_project_overrides
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        # Tuple cell
        self.assertEqual(merged["studio"]["facts"][0][1], "anni di indipendenza")
        # Dict cell
        self.assertEqual(merged["lavori"]["projects"][2]["title"], "Manuale di marca rinnovato")
        # Tuple cell (channels)
        self.assertEqual(merged["contatti"]["channels"][0][1], "studio@walker.test")
        # Scalar list cell
        self.assertEqual(merged["home"]["press_publications"][0], "Apartamento Magazine")
        # Locked column (lavori.projects.2.slug) untouched at baseline.
        self.assertEqual(merged["lavori"]["projects"][2]["slug"], "maison-gentiluomo-manuale")

    def test_a26a_baseline_lookup_resolves_dict_paths(self):
        """A.2.6a: baseline resolver walks through dict slots, so the
        sparse-diff equality check (override == baseline ⇒ delete) works
        for dict-key paths."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        baseline_value = services.resolve_path_in_baseline(p, "contatti.labels.email")
        self.assertEqual(baseline_value, "Email di contatto")
        # Setting the same value as baseline should NOT create a row.
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"contatti.labels.email": baseline_value},
        )
        self.assertEqual(p.content_overrides.count(), 0)

    # ------------------------------------------------------------------
    # A.3a · True repeater contract tests (Step 0 — design + math only,
    # no UI, no HTTP endpoint). All cases use the two lists opted-in to
    # mutability: studio.facts (tuple, min=1, max=8) and studio.partners
    # (dict, min=2, max=8).
    # ------------------------------------------------------------------

    def test_a3a_mutable_flag_whitelists_four_lists(self):
        """A.3a + A.3c: studio.facts, studio.partners, contatti.channels
        and studio.timeline_rows may accept add/remove/reorder. The
        other indexed lists stay locked."""
        from apps.editor.schema import STRUCTURED_FIELD_SHAPES, is_mutable_list
        arc = "agency-creative-studio"
        mutable = {
            path for path, shape in STRUCTURED_FIELD_SHAPES[arc].items()
            if shape.get("mutable")
        }
        self.assertEqual(mutable, {
            "studio.facts",
            "studio.partners",
            "contatti.channels",
            "studio.timeline_rows",
        })
        # Sanity — representative non-mutable lists still reject
        for path in ("manifesto.phases", "lavori.projects", "home.ledger_rows"):
            self.assertFalse(is_mutable_list(arc, path))

    def test_a3a_add_row_appends_uid_to_meta(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r1 = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        r2 = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        r3 = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        self.assertEqual(r1["uid"], "a0")
        self.assertEqual(r2["uid"], "a1")
        self.assertEqual(r3["uid"], "a2")
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta["added"], [{"uid": "a0"}, {"uid": "a1"}, {"uid": "a2"}])
        self.assertEqual(meta["removed"], [])

    def test_a3a_remove_baseline_row_records_index_in_removed(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.remove_row(
            project=p, list_path="studio.partners", index=1, editor=self.owner,
        )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta["removed"], [1])
        self.assertEqual(meta["added"], [])

    def test_a3a_remove_added_row_pops_uid_from_added(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        services.remove_row(
            project=p, list_path="studio.partners", uid="a0", editor=self.owner,
        )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta["added"], [{"uid": "a1"}])

    def test_a3a_effective_list_excludes_removed_and_includes_added(self):
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.remove_row(
            project=p, list_path="studio.partners", index=1, editor=self.owner,
        )
        services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        partners = merged["studio"]["partners"]
        # baseline had 3 partners; remove 1 + add 2 = 4 effective rows
        self.assertEqual(len(partners), 4)
        # First row keeps baseline[0] content
        self.assertEqual(partners[0]["name"], "Margherita Serafini")
        # Second row is baseline[2] (Ilaria Ferri, the third original partner)
        self.assertEqual(partners[1]["name"], "Ilaria Ferri")
        # Two trailing rows are shape-default for added uids
        self.assertEqual(partners[2], {"name": "", "role": "", "bio": "", "portrait": ""})
        self.assertEqual(partners[3], {"name": "", "role": "", "bio": "", "portrait": ""})

    def test_a3a_cell_override_on_added_row_lands_in_effective_position(self):
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        uid = r["uid"]
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={f"studio.partners.{uid}.name": "Luca Arrighi"},
        )
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        partners = merged["studio"]["partners"]
        self.assertEqual(len(partners), 4)
        self.assertEqual(partners[3]["name"], "Luca Arrighi")

    def test_a3a_remove_baseline_cascades_cell_overrides(self):
        """When a baseline row is removed, every ProjectContent under
        its cell prefix must be deleted so no orphan records survive."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                "studio.partners.1.name": "Nome personalizzato",
                "studio.partners.1.bio":  "Bio personalizzata",
                "studio.partners.0.name": "Altro partner",   # unrelated baseline 0
            },
        )
        self.assertEqual(p.content_overrides.filter(key_path__startswith="studio.partners.1.").count(), 2)
        services.remove_row(
            project=p, list_path="studio.partners", index=1, editor=self.owner,
        )
        # Cascade: both cells on baseline row 1 are gone
        self.assertEqual(p.content_overrides.filter(key_path__startswith="studio.partners.1.").count(), 0)
        # Unrelated override on baseline row 0 is untouched
        self.assertEqual(
            p.content_overrides.filter(key_path="studio.partners.0.name").count(), 1,
        )

    def test_a3a_min_rows_guard_rejects_last_remove(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # studio.partners has 3 baseline rows; min=2 → only 1 removal allowed.
        services.remove_row(
            project=p, list_path="studio.partners", index=0, editor=self.owner,
        )
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.remove_row(
                project=p, list_path="studio.partners", index=1, editor=self.owner,
            )
        self.assertEqual(ctx.exception.kind, "min")
        self.assertEqual(ctx.exception.limit, 2)

    def test_a3a_max_rows_guard_rejects_over_limit_add(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # studio.facts baseline=4, max=8 → 4 adds before blocking the 5th.
        for _ in range(4):
            services.add_row(project=p, list_path="studio.facts", editor=self.owner)
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.add_row(project=p, list_path="studio.facts", editor=self.owner)
        self.assertEqual(ctx.exception.kind, "max")
        self.assertEqual(ctx.exception.limit, 8)

    def test_a3a_non_mutable_list_rejects_row_ops(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        with self.assertRaises(services.UnsupportedMutation):
            services.add_row(project=p, list_path="manifesto.phases", editor=self.owner)
        with self.assertRaises(services.UnsupportedMutation):
            services.remove_row(
                project=p, list_path="lavori.projects", index=0, editor=self.owner,
            )

    def test_a3a_sparse_diff_preserved_when_meta_becomes_empty(self):
        """Add a row then remove it — meta should persist empty → no record."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = services.add_row(project=p, list_path="studio.facts", editor=self.owner)
        self.assertEqual(
            p.content_overrides.filter(key_path="studio.facts.__meta__").count(), 1,
        )
        services.remove_row(
            project=p, list_path="studio.facts", uid=r["uid"], editor=self.owner,
        )
        # Meta back to baseline → no row left in the overrides table
        self.assertEqual(
            p.content_overrides.filter(key_path="studio.facts.__meta__").count(), 0,
        )

    def test_a3a_ordering_is_stable_across_add_remove_reopen(self):
        """A.3a step 4 — effective list ordering must be deterministic
        and survive a full reopen:
        - baseline rows appear in their original numerical order
          (minus any ``removed``)
        - added rows appear AFTER all surviving baseline rows, in the
          declaration order of ``added[]``
        - uids are never recycled; a0 can't be reused after being
          removed and re-added.
        """
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)

        # Remove baseline partner at index 0, then add 2 rows, then
        # remove the first added (a0), then add another one.
        services.remove_row(project=p, list_path="studio.partners", index=0, editor=self.owner)
        r1 = services.add_row(project=p, list_path="studio.partners", editor=self.owner)  # a0
        r2 = services.add_row(project=p, list_path="studio.partners", editor=self.owner)  # a1
        services.remove_row(project=p, list_path="studio.partners", uid=r1["uid"], editor=self.owner)
        r3 = services.add_row(project=p, list_path="studio.partners", editor=self.owner)  # a2, never a0

        self.assertEqual(r1["uid"], "a0")
        self.assertEqual(r2["uid"], "a1")
        self.assertEqual(r3["uid"], "a2")  # monotonic, never recycled

        # Name the survivors so we can check order by content.
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                "studio.partners.1.name": "baseline-1-renamed",  # survives (baseline idx 1)
                "studio.partners.2.name": "baseline-2-renamed",  # survives (baseline idx 2)
                "studio.partners.a1.name": "added-a1",           # first surviving added
                "studio.partners.a2.name": "added-a2",           # second surviving added
            },
        )

        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        names = [row["name"] for row in merged["studio"]["partners"]]
        # Baseline rows keep their relative order; added follow; a0 gone.
        self.assertEqual(names, [
            "baseline-1-renamed",
            "baseline-2-renamed",
            "added-a1",
            "added-a2",
        ])

        # Simulate reopen — fetch meta fresh from the DB.
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta["removed"], [0])
        self.assertEqual([e["uid"] for e in meta["added"]], ["a1", "a2"])

    def test_a3a_published_preserves_repeater_state_for_other_viewers(self):
        """After publish, a second user hitting the public preview must
        see the customer's effective list (with removed baseline rows
        filtered + added rows appended)."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.remove_row(
            project=p, list_path="studio.facts", index=0, editor=self.owner,
        )
        r = services.add_row(project=p, list_path="studio.facts", editor=self.owner)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={f"studio.facts.{r['uid']}.number": "999"},
        )
        services.publish_project(project=p, editor=self.owner)

        self.client.logout()
        self.client.login(username="other", password="x")
        resp = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/studio/?project={p.uuid}"
        )
        body = resp.content.decode("utf-8", "ignore")
        # baseline[0] label "anni di attività" must be gone
        self.assertNotIn("anni di attività", body)
        # Added row's number must appear
        self.assertIn("999", body)

    # ------------------------------------------------------------------
    # A.3b · Reorder-only contract tests (Step 0 — no UI, no HTTP).
    # ------------------------------------------------------------------

    def test_a3b_default_order_derives_from_baseline_plus_added(self):
        from apps.editor.rendering import compute_default_order
        self.assertEqual(
            compute_default_order(3, [], []),
            ["0", "1", "2"],
        )
        self.assertEqual(
            compute_default_order(3, [1], []),
            ["0", "2"],
        )
        self.assertEqual(
            compute_default_order(3, [], [{"uid": "a0"}, {"uid": "a1"}]),
            ["0", "1", "2", "a0", "a1"],
        )
        self.assertEqual(
            compute_default_order(3, [0], [{"uid": "a0"}]),
            ["1", "2", "a0"],
        )

    def test_a3b_move_up_baseline_row_swaps_with_previous(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # studio.partners baseline length 3 → default order ["0","1","2"]
        services.move_row(
            project=p, list_path="studio.partners",
            segment="1", direction="up", editor=self.owner,
        )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta.get("order"), ["1", "0", "2"])

    def test_a3b_move_down_baseline_row_swaps_with_next(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.move_row(
            project=p, list_path="studio.partners",
            segment="0", direction="down", editor=self.owner,
        )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta.get("order"), ["1", "0", "2"])

    def test_a3b_move_added_row_above_baseline_row(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        # Default after add: ["0","1","2","a0"], effective len 4
        # Move a0 up three times to land it at position 0
        for _ in range(3):
            services.move_row(
                project=p, list_path="studio.partners",
                segment=r["uid"], direction="up", editor=self.owner,
            )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta.get("order"), ["a0", "0", "1", "2"])

    def test_a3b_move_up_rejects_at_first_position(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.move_row(
                project=p, list_path="studio.partners",
                segment="0", direction="up", editor=self.owner,
            )
        self.assertEqual(ctx.exception.kind, "boundary")

    def test_a3b_move_down_rejects_at_last_position(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.move_row(
                project=p, list_path="studio.partners",
                segment="2", direction="down", editor=self.owner,
            )
        self.assertEqual(ctx.exception.kind, "boundary")

    def test_a3b_move_rejects_non_mutable_list(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        with self.assertRaises(services.UnsupportedMutation):
            services.move_row(
                project=p, list_path="manifesto.phases",
                segment="0", direction="down", editor=self.owner,
            )

    def test_a3b_move_rejects_missing_segment(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        with self.assertRaises(InvalidEditableField):
            # baseline len 3 → "5" not present
            services.move_row(
                project=p, list_path="studio.partners",
                segment="5", direction="up", editor=self.owner,
            )
        with self.assertRaises(InvalidEditableField):
            services.move_row(
                project=p, list_path="studio.partners",
                segment="a99", direction="up", editor=self.owner,
            )
        with self.assertRaises(InvalidEditableField):
            services.move_row(
                project=p, list_path="studio.partners",
                segment="1", direction="sideways", editor=self.owner,
            )

    def test_a3b_sparse_diff_strips_order_when_default_restored(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # Down then up → back to default, `order` field must be stripped.
        services.move_row(
            project=p, list_path="studio.partners",
            segment="0", direction="down", editor=self.owner,
        )
        # Intermediate state: order present
        meta1 = services.get_list_meta(p, "studio.partners")
        self.assertIn("order", meta1)
        services.move_row(
            project=p, list_path="studio.partners",
            segment="0", direction="up", editor=self.owner,
        )
        meta2 = services.get_list_meta(p, "studio.partners")
        self.assertNotIn("order", meta2)
        # Full meta restoration → record deleted entirely.
        self.assertEqual(
            p.content_overrides.filter(key_path="studio.partners.__meta__").count(),
            0,
        )

    def test_a3b_cell_overrides_preserved_after_move(self):
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        uid = r["uid"]
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                "studio.partners.2.name":     "Baseline2-renamed",
                f"studio.partners.{uid}.name": "Added-name",
            },
        )
        # Move baseline "2" up two positions; move added uid up once.
        services.move_row(
            project=p, list_path="studio.partners",
            segment="2", direction="up", editor=self.owner,
        )
        services.move_row(
            project=p, list_path="studio.partners",
            segment="2", direction="up", editor=self.owner,
        )
        services.move_row(
            project=p, list_path="studio.partners",
            segment=uid, direction="up", editor=self.owner,
        )
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        names = [r["name"] for r in merged["studio"]["partners"]]
        # Expected order after "2" up×2 + a0 up×1 = ["2","0","a0","1"]:
        #   pos 0 = baseline[2] with override → "Baseline2-renamed"
        #   pos 1 = baseline[0]               → "Margherita Serafini"
        #   pos 2 = added uid a0              → "Added-name"
        #   pos 3 = baseline[1]               → "Tommaso Boeri"
        self.assertEqual(names[0], "Baseline2-renamed")
        self.assertEqual(names[1], "Margherita Serafini")
        self.assertEqual(names[2], "Added-name")
        self.assertEqual(names[3], "Tommaso Boeri")

    def test_a3b_published_overlay_reflects_reorder_for_other_viewer(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.move_row(
            project=p, list_path="studio.facts",
            segment="0", direction="down", editor=self.owner,
        )
        services.move_row(
            project=p, list_path="studio.facts",
            segment="0", direction="down", editor=self.owner,
        )
        # Effective default ["0","1","2","3"] → after 2 downs on "0":
        # ["1","2","0","3"]
        services.publish_project(project=p, editor=self.owner)
        self.client.logout()
        self.client.login(username="other", password="x")
        r = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/studio/?project={p.uuid}"
        )
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        # Find relative ordering of the 4 baseline numbers; baseline idx
        # 0 ("8") must appear AFTER baseline idx 2 ("6") in the body.
        pos_8 = body.find(">8<")
        pos_42 = body.find(">42<")
        pos_6 = body.find(">6<")
        self.assertGreater(pos_8, pos_42)
        self.assertGreater(pos_8, pos_6)

    def test_a3b_custom_order_survives_subsequent_add(self):
        """After a reorder, adding a new row must append the uid to the
        existing order rather than discard the custom sequence."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.move_row(
            project=p, list_path="studio.partners",
            segment="0", direction="down", editor=self.owner,
        )
        # meta.order is now ["1","0","2"]
        r = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta.get("order"), ["1", "0", "2", r["uid"]])

    def test_a3b_custom_order_survives_subsequent_remove(self):
        """Removing a row (baseline idx or uid) must also drop that
        segment from order[], and strip order back to default when the
        remaining sequence is canonical."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # Reorder: move baseline 2 to position 0 → order ["2","0","1"]
        services.move_row(
            project=p, list_path="studio.partners",
            segment="2", direction="up", editor=self.owner,
        )
        services.move_row(
            project=p, list_path="studio.partners",
            segment="2", direction="up", editor=self.owner,
        )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta.get("order"), ["2", "0", "1"])
        # Remove baseline 0 → order must become ["2","1"]
        services.remove_row(
            project=p, list_path="studio.partners",
            index=0, editor=self.owner,
        )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertEqual(meta.get("order"), ["2", "1"])

    def test_a3b_custom_order_strips_when_remove_makes_it_default(self):
        """If pruning a segment leaves the order equal to the canonical
        default, order must be stripped from meta (sparse-diff)."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # Add then reorder the added row to the top
        r = services.add_row(project=p, list_path="studio.partners", editor=self.owner)
        uid = r["uid"]
        # Default was ["0","1","2","a0"]; move a0 up 3 times → ["a0","0","1","2"]
        for _ in range(3):
            services.move_row(
                project=p, list_path="studio.partners",
                segment=uid, direction="up", editor=self.owner,
            )
        # Now remove a0 → remaining ["0","1","2"] which equals default
        services.remove_row(
            project=p, list_path="studio.partners",
            uid=uid, editor=self.owner,
        )
        meta = services.get_list_meta(p, "studio.partners")
        self.assertNotIn("order", meta)

    # ------------------------------------------------------------------
    # A.3c · widen repeater to contatti.channels. Schema-only
    # activation; the plumbing from A.3a+A.3b handles the rest.
    # ------------------------------------------------------------------

    def test_a3c_channels_add_remove_move_smoke(self):
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = services.add_row(project=p, list_path="contatti.channels", editor=self.owner)
        uid = r["uid"]
        self.assertEqual(r["effective_length"], 7)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                f"contatti.channels.{uid}.label": "WhatsApp",
                f"contatti.channels.{uid}.value": "+39 333 0000000",
            },
        )
        for _ in range(2):
            services.move_row(
                project=p, list_path="contatti.channels",
                segment=uid, direction="up", editor=self.owner,
            )
        services.remove_row(
            project=p, list_path="contatti.channels",
            index=3, editor=self.owner,
        )
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        channels = merged["contatti"]["channels"]
        self.assertEqual(len(channels), 6)
        joined = [(row[0], row[1]) for row in channels]
        self.assertIn(("WhatsApp", "+39 333 0000000"), joined)
        self.assertNotIn("LinkedIn", [r[0] for r in joined])

    def test_a3c_channels_boundaries(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        for idx in range(5):
            services.remove_row(
                project=p, list_path="contatti.channels",
                index=idx, editor=self.owner,
            )
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.remove_row(
                project=p, list_path="contatti.channels",
                index=5, editor=self.owner,
            )
        self.assertEqual(ctx.exception.kind, "min")
        self.assertEqual(ctx.exception.limit, 1)

        p2 = services.create_project_from_template(owner=self.other, template=self.vertex)
        for _ in range(4):
            services.add_row(project=p2, list_path="contatti.channels", editor=self.other)
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.add_row(project=p2, list_path="contatti.channels", editor=self.other)
        self.assertEqual(ctx.exception.kind, "max")
        self.assertEqual(ctx.exception.limit, 10)

    def test_a3c_timeline_rows_add_remove_move_smoke(self):
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = services.add_row(project=p, list_path="studio.timeline_rows", editor=self.owner)
        uid = r["uid"]
        self.assertEqual(r["effective_length"], 7)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={
                f"studio.timeline_rows.{uid}.year":  "2027",
                f"studio.timeline_rows.{uid}.title": "Secondo studio a Roma",
                f"studio.timeline_rows.{uid}.body":  "Apertura della sede sud.",
            },
        )
        for _ in range(5):
            services.move_row(
                project=p, list_path="studio.timeline_rows",
                segment=uid, direction="up", editor=self.owner,
            )
        services.move_row(
            project=p, list_path="studio.timeline_rows",
            segment="0", direction="down", editor=self.owner,
        )
        services.remove_row(
            project=p, list_path="studio.timeline_rows",
            index=1, editor=self.owner,
        )
        baseline = template_content.get_content(p.source_template.slug, p.locale)
        merged, _ = apply_project_overrides(p, baseline, {})
        rows = merged["studio"]["timeline_rows"]
        self.assertEqual(len(rows), 6)
        years = [r[0] for r in rows]
        self.assertIn("2027", years)
        self.assertNotIn("2020", years)

    def test_a3c_timeline_rows_boundaries(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        for idx in range(4):
            services.remove_row(
                project=p, list_path="studio.timeline_rows",
                index=idx, editor=self.owner,
            )
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.remove_row(
                project=p, list_path="studio.timeline_rows",
                index=4, editor=self.owner,
            )
        self.assertEqual(ctx.exception.kind, "min")
        self.assertEqual(ctx.exception.limit, 2)

        p2 = services.create_project_from_template(owner=self.other, template=self.vertex)
        for _ in range(4):
            services.add_row(project=p2, list_path="studio.timeline_rows", editor=self.other)
        with self.assertRaises(services.RowLimitReached) as ctx:
            services.add_row(project=p2, list_path="studio.timeline_rows", editor=self.other)
        self.assertEqual(ctx.exception.kind, "max")
        self.assertEqual(ctx.exception.limit, 10)

    def test_a3a_uid_path_validates_only_on_mutable_lists(self):
        """validate_key_path accepts uid cell paths on mutable lists
        and rejects them on still-locked lists."""
        arc = "agency-creative-studio"
        validate_key_path(arc, "studio.partners.a0.name")
        validate_key_path(arc, "studio.facts.a3.label")
        # A.3c: contatti.channels + studio.timeline_rows now mutable
        validate_key_path(arc, "contatti.channels.a0.value")
        validate_key_path(arc, "studio.timeline_rows.a0.year")
        # Still-locked list must reject uid cell paths
        with self.assertRaises(InvalidEditableField):
            validate_key_path(arc, "manifesto.phases.a0.title")
        with self.assertRaises(InvalidEditableField):
            # Bad uid shape (no digits)
            validate_key_path(arc, "studio.partners.ax.name")
        with self.assertRaises(InvalidEditableField):
            # Unknown column on a mutable list
            validate_key_path(arc, "studio.partners.a0.mystery")

    # ------------------------------------------------------------------
    # A.4 · customer image upload — contract tests (Step 0, no UI).
    # ------------------------------------------------------------------

    def _make_png_bytes(self, size_px: int = 8) -> bytes:
        """Render a tiny valid PNG with Pillow so the upload test path
        exercises a real image header, not a fake blob."""
        from io import BytesIO
        from PIL import Image
        buf = BytesIO()
        img = Image.new("RGB", (size_px, size_px), (128, 64, 200))
        img.save(buf, format="PNG")
        return buf.getvalue()

    def _make_jpeg_bytes(self, size_px: int = 8) -> bytes:
        from io import BytesIO
        from PIL import Image
        buf = BytesIO()
        Image.new("RGB", (size_px, size_px), (200, 64, 128)).save(buf, format="JPEG")
        return buf.getvalue()

    def _make_webp_bytes(self, size_px: int = 8) -> bytes:
        from io import BytesIO
        from PIL import Image
        buf = BytesIO()
        Image.new("RGB", (size_px, size_px), (64, 200, 128)).save(buf, format="WEBP")
        return buf.getvalue()

    def test_a4_validate_value_accepts_media_relative_url(self):
        """A.4: an image field override must accept the /media/... URL
        produced by the upload endpoint. Without this the autosave
        round-trip right after an upload would 400 on image fields."""
        arc = "agency-creative-studio"
        key = "home.cover.image"
        # http + https + data + media all accepted
        validate_value(arc, key, "https://cdn.example.com/a.png")
        validate_value(arc, key, "http://cdn.example.com/a.png")
        validate_value(arc, key, "data:image/png;base64,iVBORw0KGgo=")
        validate_value(arc, key, "/media/project-assets/abc/xyz.png")
        # Raw paths + non-image schemes still rejected
        with self.assertRaises(InvalidEditableField):
            validate_value(arc, key, "/not-media/evil.png")
        with self.assertRaises(InvalidEditableField):
            validate_value(arc, key, "javascript:alert(1)")

    def test_a4_project_asset_upload_happy_path_png(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        from apps.projects.models import ProjectAsset
        import os
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        png = self._make_png_bytes()
        f = SimpleUploadedFile("photo.png", png, content_type="image/png")
        asset = services.upload_asset(project=p, uploaded_file=f, editor=self.owner)
        self.assertIsInstance(asset, ProjectAsset)
        self.assertEqual(asset.content_type, "image/png")
        self.assertEqual(asset.size_bytes, len(png))
        self.assertTrue(os.path.exists(asset.file.path))
        # File path convention: project-assets/<project-uuid>/<uuid>.png
        self.assertIn(str(p.uuid), asset.file.name)
        self.assertTrue(asset.file.name.endswith(".png"))

    def test_a4_project_asset_upload_happy_path_jpeg(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        jpg = self._make_jpeg_bytes()
        f = SimpleUploadedFile("photo.jpg", jpg, content_type="image/jpeg")
        asset = services.upload_asset(project=p, uploaded_file=f, editor=self.owner)
        self.assertEqual(asset.content_type, "image/jpeg")
        self.assertTrue(asset.file.name.endswith(".jpg"))

    def test_a4_project_asset_upload_happy_path_webp(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        webp = self._make_webp_bytes()
        f = SimpleUploadedFile("photo.webp", webp, content_type="image/webp")
        asset = services.upload_asset(project=p, uploaded_file=f, editor=self.owner)
        self.assertEqual(asset.content_type, "image/webp")
        self.assertTrue(asset.file.name.endswith(".webp"))

    def test_a4_project_asset_upload_rejects_oversized(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # 3 MB payload — just over the 2 MB cap
        oversized = b"\x89PNG\r\n\x1a\n" + b"\x00" * (3 * 1024 * 1024)
        f = SimpleUploadedFile("big.png", oversized, content_type="image/png")
        with self.assertRaises(services.AssetTooLarge) as ctx:
            services.upload_asset(project=p, uploaded_file=f, editor=self.owner)
        self.assertEqual(ctx.exception.limit_bytes, 2 * 1024 * 1024)

    def test_a4_project_asset_upload_rejects_unsupported_mime(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        for ct, name in [("image/gif", "a.gif"), ("image/svg+xml", "a.svg"),
                         ("application/pdf", "a.pdf"), ("text/plain", "a.txt")]:
            f = SimpleUploadedFile(name, b"dummy", content_type=ct)
            with self.assertRaises(services.AssetMimeRejected):
                services.upload_asset(project=p, uploaded_file=f, editor=self.owner)

    def test_a4_project_asset_upload_rejects_corrupt_image(self):
        """File with correct mime/ext but byte payload that is not an
        image is rejected by the Pillow.verify() check AFTER save; the
        file + row are both cleaned up before raising."""
        from django.core.files.uploadedfile import SimpleUploadedFile
        from apps.projects.models import ProjectAsset
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        f = SimpleUploadedFile("fake.png", b"NOT AN IMAGE", content_type="image/png")
        with self.assertRaises(services.AssetInvalid):
            services.upload_asset(project=p, uploaded_file=f, editor=self.owner)
        # No orphan row left behind
        self.assertEqual(ProjectAsset.objects.filter(project=p).count(), 0)

    def test_a4_editor_ctx_exposes_asset_upload_url(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        self.client.force_login(self.owner)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("assetUploadUrl", body)
        # `escapejs` escapes forward slashes, so assert on the uuid +
        # "assets" + "upload" tokens rather than the raw URL.
        self.assertIn(str(p.uuid), body)
        self.assertIn("assets", body)
        self.assertIn("upload", body)

    def test_snapshot_reflects_post_save_state(self):
        """Regression: prefetched cache must not freeze the snapshot pre-save."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        list(p.content_overrides.all())  # prime prefetch cache
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.eyebrow": "post-save"},
        )
        rev = services.take_manual_revision(project=p, editor=self.owner, label="smoke")
        self.assertIn("home.eyebrow", rev.snapshot["content"])


class FoundationHttpTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        _seed_catalog()
        cls.owner = User.objects.create_user("owner", password="x")
        cls.other = User.objects.create_user("other", password="x")
        cls.vertex = WebTemplate.objects.get(slug="vertex-creative-agency")

    def setUp(self):
        self.client.login(username="owner", password="x")

    def test_list_requires_auth(self):
        self.client.logout()
        r = self.client.get("/projects/")
        self.assertEqual(r.status_code, 302)
        # D-087: customer surface bounces to the branded /account/login/,
        # not the staff /admin/login/.
        self.assertIn("/account/login/", r["Location"])

    def test_create_then_edit_then_preview(self):
        r = self.client.post("/projects/new/", {"template_slug": "vertex-creative-agency"})
        self.assertEqual(r.status_code, 302)
        uuid = r["Location"].split("/")[-3]

        import json as _json
        r = self.client.post(
            f"/projects/{uuid}/autosave/",
            data=_json.dumps({
                "content": {
                    "site.logo_word": "HTTP Test Studio",
                    "home.headline":  "Test <em>overlay</em>",
                },
                "tokens": {
                    "palette_primary":   "#123456",
                    "palette_secondary": "#abcdef",
                    "palette_accent":    "#ff00aa",
                    "heading_font":      "Playfair Display",
                    "body_font":         "Inter",
                },
            }),
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertTrue(body["ok"])

        r = self.client.get(f"/templates/agency/vertex-creative-agency/preview/?project={uuid}")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("HTTP Test Studio", body)
        self.assertIn("Test <em>overlay</em>", body)
        self.assertIn("#123456", body)
        self.assertIn("Playfair Display", body)

        r = self.client.get("/templates/agency/vertex-creative-agency/preview/")
        body = r.content.decode("utf-8", "ignore")
        self.assertNotIn("HTTP Test Studio", body)
        self.assertIn("Vertex Studio", body)

    def test_cross_owner_editor_404(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        self.client.logout()
        self.client.login(username="other", password="x")
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 404)

    def test_draft_overlay_hidden_from_non_owner(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "Draft-Only Studio"},
        )
        self.client.logout()
        self.client.login(username="other", password="x")
        r = self.client.get(f"/templates/agency/vertex-creative-agency/preview/?project={p.uuid}")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertNotIn("Draft-Only Studio", body)
        self.assertIn("Vertex Studio", body)

    def test_customize_start_anon_redirects_to_login_with_next(self):
        """Phase A.1b: Personalizza click while anon must preserve ?template."""
        self.client.logout()
        r = self.client.get("/projects/start/?template=vertex-creative-agency")
        self.assertEqual(r.status_code, 302)
        self.assertIn("/account/login/", r["Location"])
        # The next= param must carry the original template slug (URL-encoded).
        from urllib.parse import unquote
        self.assertIn(
            "template=vertex-creative-agency",
            unquote(r["Location"]),
        )

    def test_customize_start_auth_creates_project_and_redirects_to_editor(self):
        r = self.client.get("/projects/start/?template=vertex-creative-agency")
        self.assertEqual(r.status_code, 302)
        self.assertIn("/editor/", r["Location"])
        project = CustomerProject.objects.filter(owner=self.owner).first()
        self.assertIsNotNone(project)

    def test_customize_start_auth_reuses_existing_project(self):
        """Second click on Personalizza for the same template must reopen, not fork."""
        first = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get("/projects/start/?template=vertex-creative-agency")
        self.assertEqual(r.status_code, 302)
        self.assertIn(str(first.uuid), r["Location"])
        self.assertEqual(
            CustomerProject.objects.filter(owner=self.owner).count(),
            1,
        )

    def test_customize_start_unknown_template_redirects_to_catalog(self):
        r = self.client.get("/projects/start/?template=does-not-exist")
        self.assertEqual(r.status_code, 302)
        self.assertIn("/templates/", r["Location"])

    def test_customize_start_unsupported_archetype_redirects_to_detail(self):
        """Templates without editor support bounce to detail with an info message."""
        r = self.client.get("/projects/start/?template=gusto-fine-dining")
        self.assertEqual(r.status_code, 302)
        # Either /templates/restaurant/gusto-fine-dining/ or template_list — both accept.
        self.assertIn("/templates/", r["Location"])

    def test_autosave_endpoint_rejects_locked_keys(self):
        """D-088: autosave must reject DNA-locked paths with 400."""
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data=_json.dumps({"content": {"home.ledger_rows": []}, "tokens": {}}),
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 400)

    def test_baseline_preview_ignores_overrides(self):
        """D-088: ?baseline=1 must render the original regardless of project overrides."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "Edited Studio"},
        )
        r = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/?project={p.uuid}&baseline=1"
        )
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Vertex Studio", body)
        self.assertNotIn("Edited Studio", body)

    def test_a28_editor_copy_has_no_phase_jargon(self):
        """A.2.8 Step 4: customer-facing strings served by the editor
        view must not leak internal project jargon (Phase A.x, D-054,
        DNA-locked, repeater widget, 10-gate matrix). The test locks
        the microcopy clean so future edits don't regress it."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        body = r.content.decode("utf-8", "ignore")
        for jargon in ("Phase A", "D-054", "DNA-locked", "repeater widget",
                       "10-gate", "archetipo-driven"):
            self.assertNotIn(jargon, body,
                f"Customer-facing editor body must not contain {jargon!r}")

    def test_a28_indexed_group_help_is_customer_friendly(self):
        """A.2.8 Step 4: the schema-generated help for indexed-row
        groups must be customer-friendly — no 'Phase A.3' reference,
        no 'repeater widget' term."""
        groups = iter_groups("agency-creative-studio")
        indexed = [g for g in groups if g.get("id", "").startswith("idx__")]
        self.assertTrue(indexed, "expected at least one indexed group for Vertex")
        for g in indexed:
            help_text = g.get("help", "")
            self.assertNotIn("Phase", help_text)
            self.assertNotIn("widget", help_text)
            self.assertNotIn("repeater", help_text)

    def test_a28_editor_renders_group_toggle_all_control(self):
        """A.2.8 Step 3: the sidebar head must expose a single
        collapse-all / expand-all button that the JS wires to toggle
        every accordion's is-open state. Markup-level smoke only; the
        actual aggregate-state logic is covered by the browser walk."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("data-ed-group-toggle-all", body)
        # Initial icon class reflects the "some groups open" state that
        # the default-open-at-mount logic guarantees.
        self.assertIn("bi-chevron-contract", body)

    def test_a28_editor_exposes_mweditor_jump_field_public_api(self):
        """A.2.8 Step 1: the editor JS must expose `jumpField` on the
        `window.MWEditor` object so A.3 repeater + devtools + test
        harness can jump to a field without going through the palette."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        # The JS file is served via {% static %} — read it directly to
        # lock the export shape.
        with open("static/editor/live-editor.js", encoding="utf-8") as f:
            js = f.read()
        # Function must be declared
        self.assertIn("function jumpField(", js)
        # Function must be on the MWEditor export object
        self.assertRegex(js, r"window\.MWEditor\s*=\s*\{[^}]*jumpField")
        # Legacy name must be gone so palette + click delegates can't
        # silently diverge from the public contract.
        self.assertNotIn("jumpToField", js)

    def test_a27_live_template_title_reflects_logo_word_override(self):
        """A.2.7 L1: the iframe <title> must read site.logo_word so an
        override of the brand word is visible in the browser tab and
        not just in the navbar."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "Atelier Prova"},
        )
        r = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/?project={p.uuid}"
        )
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        title_start = body.index("<title>")
        title_end = body.index("</title>", title_start)
        title = body[title_start + len("<title>"): title_end]
        self.assertIn("Atelier Prova", title)
        self.assertNotIn("Vertex Studio", title)

    def test_snapshot_endpoint_creates_revision(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        before = p.revisions.count()
        r = self.client.post(f"/projects/{p.uuid}/snapshot/",
                             HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.json()["ok"])
        p.refresh_from_db()
        self.assertEqual(p.revisions.count(), before + 1)

    def test_editor_renders_palette_index(self):
        """A.2.5 palette search: editor GET must ship a JSON index
        with every field (content + tokens), with keywords surfaced
        for fuzzy-friendly client-side ranking."""
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")

        # Palette skeleton + trigger present
        self.assertIn('id="ed-palette"', body)
        self.assertIn('data-ed-open-palette', body)
        self.assertIn('id="ed-palette-input"', body)
        self.assertIn('id="ed-palette-index"', body)

        # Extract the JSON payload from the <script type="application/json">
        marker = 'id="ed-palette-index" type="application/json">'
        idx = body.index(marker) + len(marker)
        end = body.index("</script>", idx)
        # Undo the "</" -> "<\/" neutralisation we apply server-side
        raw = body[idx:end].replace("<\\/", "</")
        data = _json.loads(raw)
        self.assertIsInstance(data, list)
        # A.2.6b: indexed-row contract pushes the palette index past
        # 250 (target band 260-280, +5 design tokens on top).
        self.assertGreaterEqual(len(data), 250)

        keys = {row["key"] for row in data}
        # Mix of content + design-token keys must be indexed
        self.assertIn("home.headline", keys)
        self.assertIn("site.email", keys)
        self.assertIn("contatti.form_heading", keys)
        self.assertIn("palette_primary", keys)
        self.assertIn("heading_font", keys)
        # A.2.6a: new contatti scalar / dict-key fields surface in palette.
        self.assertIn("contatti.labels.name", keys)
        self.assertIn("contatti.placeholders.email", keys)
        self.assertIn("contatti.form_submit_label", keys)
        self.assertIn("contatti.reply_body", keys)
        self.assertIn("contatti.promise_heading", keys)
        # A.2.6b: indexed-row cells (one per shape kind) surface in palette.
        self.assertIn("studio.facts.0.label", keys)         # tuple
        self.assertIn("studio.partners.0.name", keys)       # dict
        self.assertIn("home.press_publications.0", keys)    # scalar list
        self.assertIn("contatti.channels.5.value", keys)    # tail row of tuple list

        # Context metadata travels with each row
        row = next(r for r in data if r["key"] == "home.headline")
        self.assertEqual(row["page"], "home")
        self.assertEqual(row["page_label"], "Studio")  # Vertex home label
        self.assertEqual(row["group_id"], "hero")
        self.assertEqual(row["kind"], "content")
        self.assertIn("titolo", row["keywords"])

        # Tokens carry synthetic keywords so "colori" / "font" / "palette"
        # all route to the design group
        color_row = next(r for r in data if r["key"] == "palette_primary")
        self.assertEqual(color_row["kind"], "token")
        self.assertEqual(color_row["page"], "*")
        self.assertIn("colori", color_row["keywords"])
        self.assertIn("font", color_row["keywords"])

    def _make_png_bytes_http(self):
        from io import BytesIO
        from PIL import Image
        buf = BytesIO()
        Image.new("RGB", (4, 4), (128, 64, 200)).save(buf, format="PNG")
        return buf.getvalue()

    def test_a4_asset_upload_endpoint_happy_path(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        from apps.projects.models import ProjectAsset
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        png = self._make_png_bytes_http()
        f = SimpleUploadedFile("photo.png", png, content_type="image/png")
        r = self.client.post(f"/projects/{p.uuid}/assets/upload/", {"file": f})
        self.assertEqual(r.status_code, 200)
        data = r.json()
        self.assertTrue(data["ok"])
        self.assertIn("asset_id", data)
        self.assertTrue(data["url"].startswith("/media/project-assets/"))
        self.assertEqual(data["content_type"], "image/png")
        self.assertEqual(ProjectAsset.objects.filter(project=p).count(), 1)

    def test_a4_asset_upload_endpoint_rejects_foreign_owner(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        png = self._make_png_bytes_http()
        # Log in as "other" and try to upload to owner's project.
        self.client.logout()
        self.client.login(username="other", password="x")
        f = SimpleUploadedFile("photo.png", png, content_type="image/png")
        r = self.client.post(f"/projects/{p.uuid}/assets/upload/", {"file": f})
        self.assertEqual(r.status_code, 404)

    def test_a4_asset_upload_endpoint_rejects_oversized(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        big = b"\x89PNG\r\n\x1a\n" + b"\x00" * (3 * 1024 * 1024)
        f = SimpleUploadedFile("big.png", big, content_type="image/png")
        r = self.client.post(f"/projects/{p.uuid}/assets/upload/", {"file": f})
        self.assertEqual(r.status_code, 413)
        data = r.json()
        self.assertFalse(data["ok"])
        self.assertEqual(data["limit_bytes"], 2 * 1024 * 1024)

    def test_a3c_editor_markup_exposes_repeater_affordances_only_on_mutable(self):
        """A.3c polish — cross-cutting integration: the editor HTTP
        response must emit the `data-ed-mutable="1"` + `[data-ed-list-path]`
        markers on exactly the four mutable lists, and must NOT emit
        them on any other indexed group. Guards against a future edit
        that flips mutable=True on a list without intention.
        """
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        # All four mutable lists must surface their list_path marker.
        for path in (
            "studio.facts", "studio.partners",
            "contatti.channels", "studio.timeline_rows",
        ):
            self.assertIn(f'data-ed-list-path="{path}"', body,
                          f"Mutable list '{path}' missing from editor markup.")
        # Representative still-locked lists must NOT carry the marker.
        for path in (
            "manifesto.phases", "lavori.projects",
            "home.ledger_rows", "capacita.disciplines",
        ):
            self.assertNotIn(f'data-ed-list-path="{path}"', body,
                             f"Non-mutable list '{path}' leaked repeater markup.")

    def test_editor_renders_data_ed_page_metadata(self):
        """A.2.5: GET editor must expose page-aware group attributes
        so the JS can route iframe navigation on focus."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        # Home-bound group: hero
        self.assertIn('data-group-id="hero"', body)
        self.assertIn('data-ed-page="home"', body)
        # Subpage group: studio
        self.assertIn('data-group-id="studio"', body)
        self.assertIn('data-ed-page="studio"', body)
        # Chrome-bound group: contact_info (footer, cross-page)
        self.assertIn('data-group-id="contact_info"', body)
        self.assertIn('data-ed-page="*"', body)
        # Config block carries the raw base path + uuid + pages list
        self.assertIn("previewBasePath", body)
        self.assertIn(
            "/templates/agency/vertex-creative-agency/preview/",
            body,
        )
        self.assertIn("availablePages", body)
        # Every declared page slug for this template appears in the list
        for slug in ("home", "studio", "capacita", "lavori", "manifesto", "contatti"):
            self.assertIn(f'"{slug}"', body)

    def test_published_overlay_visible_to_other_user(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "Published Studio"},
        )
        services.publish_project(project=p, editor=self.owner)
        self.client.logout()
        self.client.login(username="other", password="x")
        r = self.client.get(f"/templates/agency/vertex-creative-agency/preview/?project={p.uuid}")
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Published Studio", body)
