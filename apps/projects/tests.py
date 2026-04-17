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
from apps.projects.models import CustomerProject, ProjectContent


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
        # A.7 Step 1: translatable overrides persist under @<locale>: keys
        # in storage. Snapshots capture the storage shape verbatim so a
        # restore round-trip is lossless across all 5 locales.
        self.assertIn("@it:home.eyebrow", rev.snapshot["content"])

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

    # ------------------------------------------------------------------
    # A.5 · orphan asset GC contract tests
    # ------------------------------------------------------------------

    def _a5_make_asset(self, project, minutes_ago=0):
        """Factory: a ProjectAsset with a real 8×8 PNG on disk.
        `minutes_ago` backdates created_at for grace-period testing.
        """
        from django.core.files.uploadedfile import SimpleUploadedFile
        from datetime import timedelta
        from django.utils import timezone as _tz
        png = self._make_png_bytes()
        f = SimpleUploadedFile("a.png", png, content_type="image/png")
        asset = services.upload_asset(project=project, uploaded_file=f, editor=self.owner)
        if minutes_ago:
            new_ts = _tz.now() - timedelta(minutes=minutes_ago)
            from apps.projects.models import ProjectAsset
            ProjectAsset.objects.filter(pk=asset.pk).update(created_at=new_ts)
            asset.refresh_from_db()
        return asset

    def test_a5_gc_orphan_asset_found_when_unreferenced(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        asset = self._a5_make_asset(p, minutes_ago=60 * 48)  # 2 days old
        orphans = services.find_unreferenced_assets(grace_hours=24)
        self.assertIn(asset, orphans)

    def test_a5_gc_ignores_referenced_asset(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        asset = self._a5_make_asset(p, minutes_ago=60 * 48)
        # Reference the asset from a real image field override
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.partners.0.portrait": asset.file.url},
        )
        orphans = services.find_unreferenced_assets(grace_hours=24)
        self.assertNotIn(asset, orphans)

    def test_a5_gc_ignores_asset_inside_grace_window(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # Asset just created (inside default 24h grace) and not referenced
        asset = self._a5_make_asset(p, minutes_ago=0)
        orphans = services.find_unreferenced_assets(grace_hours=24)
        self.assertNotIn(asset, orphans)

    def test_a5_gc_custom_grace_hours_override(self):
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        asset = self._a5_make_asset(p, minutes_ago=0)
        # Grace=0 means even a just-created asset is considered.
        orphans = services.find_unreferenced_assets(grace_hours=0)
        self.assertIn(asset, orphans)

    def test_a5_gc_project_scope_filters_correctly(self):
        p_a = services.create_project_from_template(owner=self.owner, template=self.vertex)
        p_b = services.create_project_from_template(owner=self.other, template=self.vertex)
        asset_a = self._a5_make_asset(p_a, minutes_ago=60 * 48)
        asset_b = self._a5_make_asset(p_b, minutes_ago=60 * 48)
        # Project-A scope: only asset_a must appear
        orphans_a = services.find_unreferenced_assets(project=p_a, grace_hours=24)
        self.assertIn(asset_a, orphans_a)
        self.assertNotIn(asset_b, orphans_a)
        # Project-B scope: only asset_b
        orphans_b = services.find_unreferenced_assets(project=p_b, grace_hours=24)
        self.assertIn(asset_b, orphans_b)
        self.assertNotIn(asset_a, orphans_b)

    def test_a5_gc_revision_snapshot_counts_as_reference(self):
        """Asset referenced only in a historical ProjectRevision
        snapshot must still be protected — a publish trail is
        reference-worthy state."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        asset = self._a5_make_asset(p, minutes_ago=60 * 48)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.partners.0.portrait": asset.file.url},
        )
        services.publish_project(project=p, editor=self.owner)
        # Replace the live override so the asset URL is no longer live
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.partners.0.portrait": "https://other.example.com/new.png"},
        )
        # live ProjectContent no longer contains asset.file.url, but
        # ProjectRevision.snapshot (from publish) does → protected
        orphans = services.find_unreferenced_assets(grace_hours=24)
        self.assertNotIn(asset, orphans)

    def test_a5_gc_dry_run_counts_but_does_not_delete(self):
        import os
        from apps.projects.models import ProjectAsset
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        asset = self._a5_make_asset(p, minutes_ago=60 * 48)
        file_path = asset.file.path
        asset_pk = asset.pk
        self.assertTrue(os.path.exists(file_path))
        stats = services.delete_unreferenced_assets([asset], dry_run=True)
        self.assertEqual(stats["scanned"], 1)
        self.assertEqual(stats["deleted"], 0)
        self.assertGreater(stats["bytes_freed"], 0)  # projected
        # Row + file both still there
        self.assertTrue(ProjectAsset.objects.filter(pk=asset_pk).exists())
        self.assertTrue(os.path.exists(file_path))

    def test_a5_gc_command_default_dry_run(self):
        """`manage.py gc_project_assets` without --apply must announce
        DRY-RUN mode and leave the orphan asset in place."""
        import os
        from io import StringIO
        from django.core.management import call_command
        from apps.projects.models import ProjectAsset
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        asset = self._a5_make_asset(p, minutes_ago=60 * 48)
        file_path = asset.file.path
        asset_pk = asset.pk

        out = StringIO()
        call_command("gc_project_assets", stdout=out)
        output = out.getvalue()
        self.assertIn("DRY-RUN", output)
        self.assertIn("Candidate orphans found: 1", output)
        self.assertIn("No changes made", output)
        # Not actually deleted
        self.assertTrue(ProjectAsset.objects.filter(pk=asset_pk).exists())
        self.assertTrue(os.path.exists(file_path))

    def test_a5_gc_command_apply_actually_deletes(self):
        """`manage.py gc_project_assets --apply` removes file + row."""
        import os
        from io import StringIO
        from django.core.management import call_command
        from apps.projects.models import ProjectAsset
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        asset = self._a5_make_asset(p, minutes_ago=60 * 48)
        file_path = asset.file.path
        asset_pk = asset.pk

        out = StringIO()
        call_command("gc_project_assets", "--apply", stdout=out)
        output = out.getvalue()
        self.assertIn("APPLY", output)
        self.assertIn("Deleted: 1 / 1", output)
        # Row gone
        self.assertFalse(ProjectAsset.objects.filter(pk=asset_pk).exists())
        # File gone
        self.assertFalse(os.path.exists(file_path))

    def test_a5_gc_end_to_end_lifecycle(self):
        """A.5 integration lock — walk the full orphan lifecycle:

        1. Upload two assets.
        2. Reference asset_A in an image field.
        3. Reference asset_B in the SAME image field, orphaning A.
        4. Both assets still inside default grace window → dry-run
           returns empty list (protection holds).
        5. Backdate asset_A's created_at past the grace window →
           dry-run now picks it up as the single candidate.
        6. --apply through the command removes asset_A's file + row;
           asset_B (still referenced) is left alone.
        """
        import os
        from io import StringIO
        from datetime import timedelta
        from django.utils import timezone as _tz
        from django.core.management import call_command
        from apps.projects.models import ProjectAsset

        p = services.create_project_from_template(owner=self.owner, template=self.vertex)

        asset_a = self._a5_make_asset(p, minutes_ago=0)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.partners.0.portrait": asset_a.file.url},
        )
        asset_b = self._a5_make_asset(p, minutes_ago=0)
        # Replace the reference — A becomes orphan, B takes its place
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"studio.partners.0.portrait": asset_b.file.url},
        )

        # (4) Both inside default 24h grace → no candidates
        orphans_fresh = services.find_unreferenced_assets(grace_hours=24)
        self.assertEqual(orphans_fresh, [])

        # (5) Backdate asset_A created_at so grace filter exposes it
        ProjectAsset.objects.filter(pk=asset_a.pk).update(
            created_at=_tz.now() - timedelta(hours=48),
        )
        orphans_backdated = services.find_unreferenced_assets(grace_hours=24)
        self.assertEqual(len(orphans_backdated), 1)
        self.assertEqual(orphans_backdated[0].pk, asset_a.pk)
        # asset_b must NOT appear — still referenced
        self.assertNotIn(asset_b, orphans_backdated)

        # (6) Apply via command removes A, leaves B intact
        a_path = asset_a.file.path
        b_path = asset_b.file.path
        self.assertTrue(os.path.exists(a_path))
        self.assertTrue(os.path.exists(b_path))
        out = StringIO()
        call_command("gc_project_assets", "--apply", stdout=out)
        output = out.getvalue()
        self.assertIn("Deleted: 1 / 1", output)
        self.assertFalse(ProjectAsset.objects.filter(pk=asset_a.pk).exists())
        self.assertFalse(os.path.exists(a_path))
        # Sibling asset protected
        self.assertTrue(ProjectAsset.objects.filter(pk=asset_b.pk).exists())
        self.assertTrue(os.path.exists(b_path))

    # ------------------------------------------------------------------
    # A.6 · Pragma (corporate-suite) second-archetype support
    # ------------------------------------------------------------------

    def test_a6_pragma_archetype_registered(self):
        """`corporate-suite` must now appear in the supported-archetype
        registry alongside `agency-creative-studio`."""
        from apps.editor.schema import _ARCHETYPE_SCHEMAS
        self.assertIn("corporate-suite", _ARCHETYPE_SCHEMAS)
        self.assertTrue(is_supported_archetype("corporate-suite"))
        self.assertTrue(is_supported_archetype("agency-creative-studio"))
        # Sanity — a third unsupported archetype still rejects.
        self.assertFalse(is_supported_archetype("fine-dining"))

    def test_a6_pragma_schema_shape_covers_core_pages(self):
        """The Pragma schema must surface groups for every customer-
        editable page kind plus chrome-level groups (page="*")."""
        groups = iter_groups("corporate-suite")
        self.assertGreaterEqual(len(groups), 7)
        pages = {g.get("page") for g in groups}
        # Must cover: chrome + the five Pragma page slugs. Pragma
        # uses Italian slugs (chi-siamo / competenze / case-studies)
        # which must match the page metadata verbatim so the JS
        # page-aware navigation sees the same string as iframe path.
        self.assertIn("*", pages)
        self.assertIn("home", pages)
        self.assertIn("chi-siamo", pages)
        self.assertIn("competenze", pages)
        self.assertIn("case-studies", pages)
        # Every group must declare icon + region
        for g in groups:
            with self.subTest(group=g["id"]):
                self.assertIn("icon", g)
                self.assertIn("region", g)

    def test_a6_pragma_validate_key_path_accepts_whitelist_rejects_outside(self):
        arc = "corporate-suite"
        # Whitelisted
        validate_key_path(arc, "site.logo_word")
        validate_key_path(arc, "home.headline")
        validate_key_path(arc, "home.hero_image")
        validate_key_path(arc, "chi-siamo.intro")
        validate_key_path(arc, "competenze.headline")
        validate_key_path(arc, "case-studies.cta_primary")
        validate_key_path(arc, "home.pillars.0.title")  # indexed cell
        validate_key_path(arc, "home.leadership.1.name")
        # Off-whitelist paths must reject
        with self.assertRaises(InvalidEditableField):
            validate_key_path(arc, "home.mystery_field")
        with self.assertRaises(InvalidEditableField):
            # Vertex path on Pragma
            validate_key_path(arc, "studio.partners.0.name")
        with self.assertRaises(InvalidEditableField):
            # Structural section_order is DNA-locked per D-054
            validate_key_path(arc, "section_order")

    def test_a6_pragma_indexed_lists_are_readonly_not_mutable(self):
        """A.6 ships 3 indexed lists on Pragma but NONE are mutable.
        Row add/remove/move must be rejected; cell edits still work."""
        from apps.editor.schema import STRUCTURED_FIELD_SHAPES, is_mutable_list
        arc = "corporate-suite"
        shapes = STRUCTURED_FIELD_SHAPES[arc]
        expected = {"home.pillars", "home.kpi_strip", "home.leadership"}
        self.assertEqual(set(shapes.keys()), expected)
        for path in expected:
            with self.subTest(path=path):
                self.assertFalse(shapes[path].get("mutable", False),
                                 f"{path} must not be mutable in A.6")
                self.assertFalse(is_mutable_list(arc, path))

    def test_a6_pragma_customize_start_creates_editable_project(self):
        """Public customize entry must land the customer inside the
        editor when the template's archetype is now supported."""
        pragma = WebTemplate.objects.get(slug="pragma-corporate-suite")
        p = services.create_project_from_template(owner=self.owner, template=pragma)
        self.assertEqual(p.source_archetype, "corporate-suite")
        # The project's baseline resolution must pick up Pragma's IT content,
        # so baseline-side of sparse-diff is wired correctly.
        baseline = services.resolve_path_in_baseline(p, "site.logo_word")
        self.assertEqual(baseline, "Pragma Advisors")

    def test_a6_vertex_editor_unchanged(self):
        """Regression guard: the agency-creative-studio schema must stay
        at its A.3c shape (4 mutable lists, 15 curated groups)."""
        from apps.editor.schema import STRUCTURED_FIELD_SHAPES
        arc = "agency-creative-studio"
        mutable = {
            path for path, shape in STRUCTURED_FIELD_SHAPES[arc].items()
            if shape.get("mutable")
        }
        self.assertEqual(mutable, {
            "studio.facts", "studio.partners",
            "studio.timeline_rows", "contatti.channels",
        })
        # Vertex still has 14 curated + 18 indexed = 32 groups when
        # meta_by_path is absent (baseline mode).
        vertex_groups = iter_groups(arc)
        self.assertEqual(len(vertex_groups), 32)

    # ------------------------------------------------------------------
    # A.7 · Multi-locale editor — Step 0 contract
    # ------------------------------------------------------------------

    def test_a7_vertex_text_field_is_translatable(self):
        """Scalar copy fields on Vertex — headline, intro, eyebrow, CTA
        labels — must be flagged translatable so Step 1 routes them into
        by_locale overlays."""
        from apps.editor.schema import is_translatable
        arc = "agency-creative-studio"
        for path in ("home.headline", "home.eyebrow",
                     "studio.standfirst", "manifesto.standfirst",
                     "site.tag", "site.availability",
                     "site.hours_compact", "site.footer_intro"):
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on Vertex",
            )

    def test_a7_vertex_branding_and_contact_universals_are_global(self):
        """Logo + per-row universals (phone, email, address, license,
        logo_initial) stay global even though they are text-typed —
        identity and contact data don't change per language."""
        from apps.editor.schema import is_translatable
        arc = "agency-creative-studio"
        for path in ("site.logo_word", "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Vertex",
            )

    def test_a7_vertex_non_text_fields_are_global(self):
        """Image · URL · select · color · font fields are always global —
        only text/textarea/richtext can be flagged translatable."""
        from apps.editor.schema import is_translatable
        arc = "agency-creative-studio"
        self.assertFalse(is_translatable(arc, "home.cover.image"))          # image
        self.assertFalse(is_translatable(arc, "site.inquiry_page_slug"))    # select

    def test_a7_vertex_repeater_cells_are_global(self):
        """Repeater row content stays global — the A.7 first wave freezes
        both baseline-indexed cells and added-row uid cells out of the
        multi-locale overlay. Translatable repeater row copy is a later
        phase if customer demand emerges."""
        from apps.editor.schema import is_translatable
        arc = "agency-creative-studio"
        # Baseline-indexed cell (text-typed inside studio.facts list)
        self.assertFalse(is_translatable(arc, "studio.facts.0.label"))
        # Added-row uid cell on a mutable list
        self.assertFalse(is_translatable(arc, "studio.partners.a0.name"))
        # Bare list root path — not a scalar field either way
        self.assertFalse(is_translatable(arc, "studio.facts"))

    def test_a7_pragma_is_not_multilocale_enabled_in_first_wave(self):
        """A.7 ships Vertex only. Pragma copy must classify as global for
        every path until A.7b opts it in — protects the overlay shape
        from leaking into a second archetype prematurely."""
        from apps.editor.schema import is_translatable, supported_locales
        arc = "corporate-suite"
        # Even clearly-copy paths must return False on Pragma
        for path in ("home.headline", "home.eyebrow",
                     "chi-siamo.intro", "competenze.headline"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} on Pragma must stay global in A.7 first wave",
            )
        self.assertEqual(supported_locales(arc), [])

    def test_a7_supported_locales_for_vertex_returns_canonical_five(self):
        """supported_locales is the contract Step 2 + editor_ctx will
        consume to render the sidebar pill strip. Vertex — the first
        enrolled archetype — returns exactly it/en/fr/es/ar."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("agency-creative-studio"),
            ["it", "en", "fr", "es", "ar"],
        )
        # Unknown archetype returns empty list, never raises.
        self.assertEqual(supported_locales("fine-dining"), [])

    def test_a7_is_translatable_unknown_path_and_archetype_return_false(self):
        """Defensive contract: unknown paths and archetypes return False
        cleanly instead of raising — the helper is consulted from hot
        paths in autosave + rendering, it must never error on stale
        input."""
        from apps.editor.schema import is_translatable
        self.assertFalse(is_translatable("agency-creative-studio",
                                          "nowhere.not.real"))
        self.assertFalse(is_translatable("no-such-archetype",
                                          "home.headline"))

    # ------------------------------------------------------------------
    # A.7 · Step 1 — per-locale save/load service layer
    # ------------------------------------------------------------------

    def test_a7_step1_translatable_edit_persists_under_locale_key(self):
        """A translatable edit must land on the ``@<locale>:`` storage
        shape so edits in locale A never touch the buffer for locale B."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"home.headline": "Ideas endure."},
        )
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@en:home.headline", keys)
        self.assertNotIn("home.headline", keys)

    def test_a7_step1_global_edit_keeps_plain_storage_key(self):
        """Non-translatable (global) edits must NOT carry a locale
        prefix — a single row applies to every render locale."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # site.logo_word is explicitly flagged global in Step 0
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"site.logo_word": "MyBrand"},
        )
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        self.assertNotIn("@it:site.logo_word", keys)

    def test_a7_step1_save_in_locale_a_does_not_touch_locale_b(self):
        """Saving the same translatable path in two locales creates two
        independent rows — neither overwrites nor deletes the other."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner, locale="it",
            edits={"home.headline": "Le idee <em>resistono</em>."},
        )
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"home.headline": "Ideas endure."},
        )
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertEqual(keys, {"@it:home.headline", "@en:home.headline"})
        # Values resolved per locale through the reader contract
        it_tree = p.get_overrides_dict(locale="it")
        en_tree = p.get_overrides_dict(locale="en")
        self.assertEqual(it_tree["home"]["headline"], "Le idee <em>resistono</em>.")
        self.assertEqual(en_tree["home"]["headline"], "Ideas endure.")

    def test_a7_step1_unedited_locales_fall_back_to_authored_baseline(self):
        """Rendering a locale with no customer overrides for a
        translatable path must fall back cleanly to the authored
        registry value — NO cross-locale customer override leak."""
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner, locale="it",
            edits={"home.headline": "Custom IT headline."},
        )
        # Render EN: the customer never edited the EN headline, so the
        # EN authored registry value must flow through unchanged.
        en_baseline = template_content.get_content(p.source_template.slug, "en")
        en_authored_headline = en_baseline["home"]["headline"]
        merged, _ = apply_project_overrides(p, en_baseline, {}, locale="en")
        self.assertEqual(merged["home"]["headline"], en_authored_headline)
        # IT render receives the customer override.
        it_baseline = template_content.get_content(p.source_template.slug, "it")
        merged_it, _ = apply_project_overrides(p, it_baseline, {}, locale="it")
        self.assertEqual(merged_it["home"]["headline"], "Custom IT headline.")

    def test_a7_step1_sparse_diff_is_locale_scoped(self):
        """Writing a value equal to the authored baseline FOR THAT
        LOCALE must delete the ``@<locale>:`` row, mirroring the
        pre-A.7 sparse-diff contract but scoped per locale."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        en_authored = template_content.get_content(
            p.source_template.slug, "en",
        )["home"]["headline"]
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"home.headline": "Temporary EN headline."},
        )
        self.assertEqual(
            p.content_overrides.filter(key_path="@en:home.headline").count(), 1,
        )
        # Reset to baseline — row must drop.
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"home.headline": en_authored},
        )
        self.assertEqual(
            p.content_overrides.filter(key_path="@en:home.headline").count(), 0,
        )

    def test_a7_step1_global_edit_applies_to_every_locale_render(self):
        """A global override must show up in every locale render — one
        row, one value, every render locale."""
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "MyBrand"},
        )
        for locale in ("it", "en", "fr", "es", "ar"):
            baseline = template_content.get_content(p.source_template.slug, locale)
            merged, _ = apply_project_overrides(p, baseline, {}, locale=locale)
            self.assertEqual(
                merged["site"]["logo_word"], "MyBrand",
                f"global override must apply to locale={locale}",
            )

    def test_a7_step1_legacy_plain_row_on_translatable_path_still_renders(self):
        """Backward compat: a ProjectContent row with a plain (no locale
        prefix) key on a translatable path — simulating a legacy pre-A.7
        customer project — must still render across all locales until
        a per-locale edit supersedes it."""
        from apps.editor.rendering import apply_project_overrides
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        # Inject a legacy row directly, bypassing the A.7 save service.
        row = ProjectContent(
            project=p, key_path="home.headline",
        )
        row.set_value("Legacy override")
        row.save()
        for locale in ("it", "en", "fr", "es", "ar"):
            baseline = template_content.get_content(p.source_template.slug, locale)
            merged, _ = apply_project_overrides(p, baseline, {}, locale=locale)
            self.assertEqual(merged["home"]["headline"], "Legacy override")
        # Now save a per-locale override in EN only — EN render must
        # supersede the legacy row; other locales keep the legacy value.
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"home.headline": "New EN headline"},
        )
        en_baseline = template_content.get_content(p.source_template.slug, "en")
        merged_en, _ = apply_project_overrides(p, en_baseline, {}, locale="en")
        self.assertEqual(merged_en["home"]["headline"], "New EN headline")
        fr_baseline = template_content.get_content(p.source_template.slug, "fr")
        merged_fr, _ = apply_project_overrides(p, fr_baseline, {}, locale="fr")
        self.assertEqual(merged_fr["home"]["headline"], "Legacy override")

    def test_a7_step1_translatable_edit_without_locale_defaults_to_project_locale(self):
        """Pre-A.7 callers (existing tests + legacy call sites) that
        don't pass ``locale`` must still work: translatable edits land
        under the project's seed locale (``it`` by default)."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.headline": "Senza locale esplicito."},
        )
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertNotIn("home.headline", keys)

    def test_a7_step1_unsupported_locale_is_rejected(self):
        """A translatable edit for a locale outside the archetype's
        supported set must raise — avoids silently persisting rows
        the renderer will never see."""
        from apps.projects.services import UnsupportedLocale
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        with self.assertRaises(UnsupportedLocale):
            services.save_content_edits(
                project=p, editor=self.owner, locale="ja",
                edits={"home.headline": "日本語"},
            )

    def test_a7_step1_pragma_save_still_uses_plain_keys(self):
        """Pragma is not yet enrolled in multi-locale. Saves on Pragma
        must keep the pre-A.7 plain-key shape — regression guard that
        the translatable gate really holds at the write layer."""
        pragma = WebTemplate.objects.get(slug="pragma-corporate-suite")
        p = services.create_project_from_template(owner=self.owner, template=pragma)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.headline": "Pragma override."},
        )
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("home.headline", keys)
        self.assertFalse(any(k.startswith("@") for k in keys),
                         f"Pragma rows must stay plain-keyed; got {keys}")

    # ------------------------------------------------------------------
    # A.7 · Step 2 — autosave + editor context locale-aware (service)
    # ------------------------------------------------------------------

    def test_a7_step2_current_value_for_loads_the_locale_buffer(self):
        """``current_value_for(project, path, locale=L)`` returns the EN
        override when present, otherwise the EN authored baseline — i.e.
        the sidebar prefill matches the active editing locale."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"home.headline": "Ideas endure."},
        )
        # EN buffer: customer override
        self.assertEqual(
            services.current_value_for(p, "home.headline", locale="en"),
            "Ideas endure.",
        )
        # FR buffer: no override → authored baseline (never the IT/EN override)
        fr_authored = template_content.get_content(
            p.source_template.slug, "fr",
        )["home"]["headline"]
        self.assertEqual(
            services.current_value_for(p, "home.headline", locale="fr"),
            fr_authored,
        )

    def test_a7_step2_resolve_path_in_baseline_is_locale_scoped(self):
        """``resolve_path_in_baseline`` for a translatable path returns
        the authored value of the requested locale, not project.locale."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        en_authored = template_content.get_content(
            p.source_template.slug, "en",
        )["home"]["headline"]
        self.assertEqual(
            services.resolve_path_in_baseline(p, "home.headline", locale="en"),
            en_authored,
        )

    def test_a7_step2_preview_url_carries_lang_param(self):
        """``preview_url_for_page(..., locale=X)`` embeds ``&lang=X``
        so the iframe picks the right authored registry + overlay."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        url = p.preview_url_for_page("home", locale="en")
        self.assertIn(f"project={p.uuid}", url)
        self.assertIn("&lang=en", url)
        # Non-home page still formats correctly.
        self.assertIn("&lang=ar", p.preview_url_for_page("studio", locale="ar"))
        # Omitting locale preserves the pre-A.7 shape (no lang param).
        self.assertNotIn("lang=", p.preview_url_for_page("home"))

    def test_snapshot_reflects_post_save_state(self):
        """Regression: prefetched cache must not freeze the snapshot pre-save."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        list(p.content_overrides.all())  # prime prefetch cache
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"home.eyebrow": "post-save"},
        )
        rev = services.take_manual_revision(project=p, editor=self.owner, label="smoke")
        # A.7 Step 1: translatable paths live under @<locale>: in storage.
        self.assertIn("@it:home.eyebrow", rev.snapshot["content"])


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

    def test_a4_uploaded_image_persists_across_reload_and_publish(self):
        """A.4 cross-cutting lock — upload → write URL into image field →
        reopen editor → publish → public preview of another viewer:
        the uploaded /media/... URL must survive every hop without
        being rewritten or lost.
        """
        from django.core.files.uploadedfile import SimpleUploadedFile
        # 1. Create a fresh project + upload via the service layer
        #    (the endpoint is already covered by the HTTP happy-path
        #    test; here we focus on the downstream persistence).
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        png = self._make_png_bytes_http()
        f = SimpleUploadedFile("portrait.png", png, content_type="image/png")
        r = self.client.post(f"/projects/{p.uuid}/assets/upload/", {"file": f})
        self.assertEqual(r.status_code, 200)
        uploaded_url = r.json()["url"]
        self.assertTrue(uploaded_url.startswith("/media/project-assets/"))

        # 2. Write the URL into a real image field via the autosave
        #    endpoint so the full validate_value pipeline runs.
        r2 = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data='{"content":{"studio.partners.0.portrait":"' + uploaded_url + '"},"tokens":{}}',
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(r2.status_code, 200)
        self.assertTrue(r2.json()["ok"])

        # 3. Reopen editor — the URL must prefill the field input.
        r3 = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r3.status_code, 200)
        self.assertIn(uploaded_url, r3.content.decode("utf-8", "ignore"))

        # 4. Publish + another (logged-in) viewer requests the live
        #    preview — uploaded URL must appear in the rendered HTML.
        services.publish_project(project=p, editor=self.owner)
        self.client.logout()
        self.client.login(username="other", password="x")
        r4 = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/studio/?project={p.uuid}"
        )
        self.assertEqual(r4.status_code, 200)
        self.assertIn(uploaded_url, r4.content.decode("utf-8", "ignore"))

    def test_a4_uploaded_image_persists_on_home_cover_image_field(self):
        """A.4 complementary lock — the persistence contract must hold
        on BOTH image fields in the schema, not only the portrait one
        already covered by
        test_a4_uploaded_image_persists_across_reload_and_publish.

        ``home.cover.image`` is a different path shape (dict-nested on
        the home page, not a repeater dict column) so it exercises a
        distinct branch of the rendering pipeline. One end-to-end hop
        is enough: upload → autosave → public preview of home.
        """
        from django.core.files.uploadedfile import SimpleUploadedFile
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        png = self._make_png_bytes_http()
        f = SimpleUploadedFile("cover.png", png, content_type="image/png")
        r = self.client.post(f"/projects/{p.uuid}/assets/upload/", {"file": f})
        self.assertEqual(r.status_code, 200)
        uploaded_url = r.json()["url"]

        r2 = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data='{"content":{"home.cover.image":"' + uploaded_url + '"},"tokens":{}}',
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(r2.status_code, 200)
        self.assertTrue(r2.json()["ok"])

        services.publish_project(project=p, editor=self.owner)
        self.client.logout()
        self.client.login(username="other", password="x")
        r3 = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/?project={p.uuid}"
        )
        self.assertEqual(r3.status_code, 200)
        self.assertIn(uploaded_url, r3.content.decode("utf-8", "ignore"))

    def test_a6_pragma_preview_title_reflects_logo_word_override(self):
        """A.6 mirror of A.2.7 L1: overriding site.logo_word must
        propagate to the iframe <title>, not stay locked to the
        catalog brand. Proves the skin title-fix was wired."""
        pragma = WebTemplate.objects.get(slug="pragma-corporate-suite")
        p = services.create_project_from_template(owner=self.owner, template=pragma)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "Atelier Pragma"},
        )
        r = self.client.get(
            f"/templates/business/pragma-corporate-suite/preview/?project={p.uuid}"
        )
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        title_start = body.index("<title>")
        title_end = body.index("</title>", title_start)
        title = body[title_start + len("<title>"):title_end]
        self.assertIn("Atelier Pragma", title)
        self.assertNotIn("Pragma Advisors", title)

    def test_a6_pragma_editor_ctx_exposes_sidebar_and_palette(self):
        """The project editor GET for a Pragma project must render the
        Pragma schema (all 7 groups · icon + region + page-aware
        markers) and expose the palette index with Pragma field keys."""
        pragma = WebTemplate.objects.get(slug="pragma-corporate-suite")
        p = services.create_project_from_template(owner=self.owner, template=pragma)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        # Group markup wired — one data-group-id per Pragma schema group
        for group_id in ("brand", "hero_board", "home_bands", "about_page",
                         "services_page", "cases_page", "contact_info"):
            self.assertIn(f'data-group-id="{group_id}"', body,
                          f"Pragma group '{group_id}' missing from editor markup.")
        # Page-aware data-ed-page attributes at least for home + chrome
        self.assertIn('data-ed-page="home"', body)
        self.assertIn('data-ed-page="*"', body)
        # Palette index JSON carries Pragma-specific field keys
        self.assertIn('"key": "site.logo_word"', body)
        self.assertIn('"key": "home.headline"', body)
        self.assertIn('"key": "home.hero_image"', body)
        # Preview URL points at Pragma, not Vertex
        self.assertIn("/templates/business/pragma-corporate-suite/preview/", body)

    def test_a6_pragma_editor_preview_injects_editor_bridge(self):
        """When the live preview is requested with ?project=<uuid>, the
        Pragma skin must inject preview-bridge.js and mark the body as
        editor-embedded (so the marketplace top strip is hidden)."""
        pragma = WebTemplate.objects.get(slug="pragma-corporate-suite")
        p = services.create_project_from_template(owner=self.owner, template=pragma)
        # With project → bridge injected, body class applied
        r = self.client.get(
            f"/templates/business/pragma-corporate-suite/preview/?project={p.uuid}"
        )
        body = r.content.decode("utf-8", "ignore")
        self.assertIn('editor/preview-bridge.js', body)
        # Check the body class attribute specifically — the CSS rule
        # body.mw-is-editor-preview { ... } also contains the literal
        # string, so match on the <body class="..."> pattern only.
        self.assertIn('<body class="mw-is-editor-preview"', body)
        # Without project → bridge absent, body class absent (public view)
        r2 = self.client.get("/templates/business/pragma-corporate-suite/preview/")
        body2 = r2.content.decode("utf-8", "ignore")
        self.assertNotIn('editor/preview-bridge.js', body2)
        self.assertNotIn('<body class="mw-is-editor-preview"', body2)

    def test_a6_pragma_full_editing_lifecycle_end_to_end(self):
        """A.6 cross-cutting integration lock — walk the four-hop
        customer flow at the HTTP boundary so a future refactor of any
        single piece (schema / rendering / view / autosave / validator)
        cannot silently drop a Pragma override along the way.

        upload image → autosave writes scalar override + image URL →
        GET editor reopens with both prefilled → publish then fetch the
        public preview as a second user → all overrides visible.
        """
        from django.core.files.uploadedfile import SimpleUploadedFile
        pragma = WebTemplate.objects.get(slug="pragma-corporate-suite")
        p = services.create_project_from_template(owner=self.owner, template=pragma)

        # (1) Upload a real image for home.hero_image
        png = self._make_png_bytes_http()
        f = SimpleUploadedFile("pragma-board.png", png, content_type="image/png")
        r = self.client.post(f"/projects/{p.uuid}/assets/upload/", {"file": f})
        self.assertEqual(r.status_code, 200)
        uploaded_url = r.json()["url"]
        self.assertTrue(uploaded_url.startswith("/media/project-assets/"))

        # (2) Autosave a scalar (home.headline) + the uploaded image URL
        edits_payload = (
            '{"content": {'
            f'"home.headline": "Decisioni riservate <em>che contano</em>",'
            f'"home.hero_image": "{uploaded_url}",'
            f'"site.logo_word": "Pragma Test"'
            '}, "tokens": {}}'
        )
        r2 = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data=edits_payload,
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(r2.status_code, 200)
        self.assertTrue(r2.json()["ok"])

        # (3) Reopen editor — all three overrides prefill the UI
        r3 = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r3.status_code, 200)
        body3 = r3.content.decode("utf-8", "ignore")
        self.assertIn("Decisioni riservate", body3)
        self.assertIn(uploaded_url, body3)
        self.assertIn("Pragma Test", body3)

        # (4) Publish, then a second authenticated user hits the public
        #     preview and must see every override rendered.
        services.publish_project(project=p, editor=self.owner)
        self.client.logout()
        self.client.login(username="other", password="x")
        r4 = self.client.get(
            f"/templates/business/pragma-corporate-suite/preview/?project={p.uuid}"
        )
        self.assertEqual(r4.status_code, 200)
        body4 = r4.content.decode("utf-8", "ignore")
        self.assertIn("Decisioni riservate", body4)
        self.assertIn(uploaded_url, body4)
        # Title override flows through the skin fix from Step 1
        title_start = body4.index("<title>")
        title_end = body4.index("</title>", title_start)
        self.assertIn("Pragma Test", body4[title_start:title_end])

    def test_a6_vertex_editor_still_ships_after_pragma_lands(self):
        """Regression guard at the HTTP layer: Vertex editor must keep
        rendering its 4 mutable lists + 284 fields even after the
        second archetype (Pragma) is registered."""
        vertex = WebTemplate.objects.get(slug="vertex-creative-agency")
        p = services.create_project_from_template(owner=self.owner, template=vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        body = r.content.decode("utf-8", "ignore")
        # Vertex-specific sidebar IDs all still present
        for group_id in ("hero", "studio", "contatti", "contact_info", "design"):
            self.assertIn(f'data-group-id="{group_id}"', body)
        # All four Vertex mutable lists still carry the repeater marker
        for list_path in ("studio.facts", "studio.partners",
                           "studio.timeline_rows", "contatti.channels"):
            self.assertIn(f'data-ed-list-path="{list_path}"', body)

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

    # ------------------------------------------------------------------
    # A.7 · Step 2 — HTTP surface for locale-aware editor + autosave
    # ------------------------------------------------------------------

    def test_a7_step2_editor_without_lang_defaults_to_project_locale(self):
        """No ``?lang=`` on the editor URL → active_locale is the
        project's seed locale (``it``). Values prefill from the IT
        authored registry (or IT override), not another language."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context["active_locale"], "it")
        # Supported locales exposed in context for Step 3 UI.
        self.assertEqual(
            r.context["supported_locales"], ["it", "en", "fr", "es", "ar"],
        )

    def test_a7_step2_editor_with_lang_en_loads_english_values(self):
        """``?lang=en`` switches the editor context + value materialisation
        to the EN buffer: authored EN value when no override, customer
        EN override when present."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        services.save_content_edits(
            project=p, editor=self.owner, locale="en",
            edits={"home.headline": "EN customer headline."},
        )
        r = self.client.get(f"/projects/{p.uuid}/editor/?lang=en")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context["active_locale"], "en")
        # Sidebar field for home.headline must surface the EN override.
        hero_group = next(g for g in r.context["groups"] if g["id"] == "hero")
        headline_field = next(
            f for f in hero_group["fields"] if f["key"] == "home.headline"
        )
        self.assertEqual(headline_field["value"], "EN customer headline.")
        self.assertTrue(headline_field["translatable"])
        self.assertTrue(headline_field["is_overridden"])
        # Preview URL carries ?lang=en so the iframe renders English.
        self.assertIn("lang=en", r.context["preview_url"])

    def test_a7_step2_editor_with_unknown_lang_falls_back_silently(self):
        """Unknown or unsupported lang values must not 500 or 404 —
        the editor falls back to ``project.locale`` silently."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/?lang=ja")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context["active_locale"], "it")

    def test_a7_step2_autosave_with_locale_routes_to_locale_key(self):
        """Autosave JSON with ``locale: 'en'`` persists translatable
        content under ``@en:<path>`` so IT/FR/ES/AR buffers stay clean."""
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data=_json.dumps({
                "locale": "en",
                "content": {"home.headline": "Endpoint EN headline."},
                "tokens": {},
            }),
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertTrue(body["ok"])
        self.assertIn("@en:home.headline", body["content_keys"])
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@en:home.headline", keys)
        self.assertNotIn("@it:home.headline", keys)

    def test_a7_step2_autosave_global_field_ignores_locale_param(self):
        """A global field in the autosave payload still persists as a
        plain row even when the request body includes ``locale``."""
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data=_json.dumps({
                "locale": "en",
                "content": {"site.logo_word": "UniBrand"},
                "tokens": {},
            }),
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 200)
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("site.logo_word", keys)
        self.assertFalse(any(k.startswith("@") and k.endswith(":site.logo_word")
                             for k in keys))

    def test_a7_step2_autosave_rejects_unsupported_locale(self):
        """Autosave with a locale outside the archetype's enrolled set
        returns a clean 400 instead of persisting an unreachable row."""
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data=_json.dumps({
                "locale": "ja",
                "content": {"home.headline": "日本語"},
                "tokens": {},
            }),
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 400)
        body = r.json()
        self.assertFalse(body["ok"])

    def test_a7_step2_autosave_without_locale_defaults_to_project_locale(self):
        """Legacy autosave payload (no ``locale`` key) keeps working:
        translatable edits default to the project's seed locale."""
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data=_json.dumps({
                "content": {"home.headline": "Legacy payload."},
                "tokens": {},
            }),
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 200)
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)

    # ------------------------------------------------------------------
    # A.7 · Step 3 — editor UI wiring (markup contract)
    # ------------------------------------------------------------------

    def test_a7_step3_translatable_field_renders_per_lingua_badge(self):
        """Translatable content fields must render the per-lingua marker
        + data-ed-translatable flag. Global fields must NOT — the
        customer needs a visual cue to tell them apart."""
        import re as _re
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/?lang=en")
        body = r.content.decode("utf-8", "ignore")
        # Translatable field: opening <div class="ed-field ..."> must
        # carry is-translatable + data-ed-translatable, and the next ~600
        # chars (head region) must contain the per-lingua label.
        translatable_open = _re.search(
            r'<div class="ed-field([^"]*)"[^>]*data-ed-key="home\.headline"[^>]*>',
            body,
        )
        self.assertIsNotNone(translatable_open, "home.headline field not rendered")
        self.assertIn('is-translatable', translatable_open.group(1))
        self.assertIn('data-ed-translatable="1"', translatable_open.group(0))
        head_window = body[translatable_open.end():translatable_open.end() + 600]
        self.assertIn('per lingua', head_window)
        # Global field: opening div must NOT carry the translatable
        # flags, and the next 400 chars must NOT contain the badge text.
        global_open = _re.search(
            r'<div class="ed-field([^"]*)"[^>]*data-ed-key="site\.logo_word"[^>]*>',
            body,
        )
        self.assertIsNotNone(global_open, "site.logo_word field not rendered")
        self.assertNotIn('is-translatable', global_open.group(1))
        self.assertNotIn('data-ed-translatable', global_open.group(0))
        head_global = body[global_open.end():global_open.end() + 400]
        self.assertNotIn('per lingua', head_global)

    def test_a7_step3_locale_switcher_label_signals_edit_and_preview(self):
        """With multi-locale enrolled, the sidebar header must read
        "Lingua attiva" (edit+preview) rather than "Lingua anteprima"
        (preview-only) — signal that the switch changes what you edit."""
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        r = self.client.get(f"/projects/{p.uuid}/editor/")
        body = r.content.decode("utf-8", "ignore")
        self.assertIn("Lingua attiva", body)
        self.assertIn('data-ed-lang="it"', body)
        self.assertIn('data-ed-lang="en"', body)
        self.assertIn('data-ed-lang="ar"', body)

    def test_a7_step2_preview_follows_active_locale_end_to_end(self):
        """Saving EN via autosave + fetching the preview with ``?lang=en``
        returns the EN override on HTML; fetching ``?lang=it`` returns
        the IT authored baseline (no EN leak)."""
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)
        self.client.post(
            f"/projects/{p.uuid}/autosave/",
            data=_json.dumps({
                "locale": "en",
                "content": {"home.headline": "Preview EN lives here."},
                "tokens": {},
            }),
            content_type="application/json",
        )
        r_en = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/"
            f"?project={p.uuid}&lang=en"
        )
        body_en = r_en.content.decode("utf-8", "ignore")
        self.assertIn("Preview EN lives here.", body_en)
        r_it = self.client.get(
            f"/templates/agency/vertex-creative-agency/preview/"
            f"?project={p.uuid}&lang=it"
        )
        body_it = r_it.content.decode("utf-8", "ignore")
        self.assertNotIn("Preview EN lives here.", body_it)
