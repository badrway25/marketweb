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
        # trattoria-warm has not been enrolled in _ARCHETYPE_SCHEMAS yet —
        # Sapore still hits the UnsupportedTemplate guard. Swap this slug
        # when trattoria-warm gets an editor schema of its own.
        sapore = WebTemplate.objects.get(slug="sapore-trattoria-pizzeria")
        with self.assertRaises(services.UnsupportedTemplate):
            services.create_project_from_template(owner=self.owner, template=sapore)

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
        # Sanity — an unsupported archetype still rejects.
        self.assertFalse(is_supported_archetype("trattoria-warm"))

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

    # ------------------------------------------------------------------
    # A.7b · Pragma multi-locale enrollment — Step 0 contract
    # ------------------------------------------------------------------

    def test_a7b_pragma_is_translatable_text_fields(self):
        """Pragma scalar copy fields must classify as translatable after
        A.7b enrollment. The sample deliberately distributes paths across
        every Pragma page (home · chi-siamo · competenze · case-studies ·
        contatti/footer) so the gate can't pass by covering only ``home``."""
        from apps.editor.schema import is_translatable
        arc = "corporate-suite"
        distributed_paths = (
            # home — hero + bands
            "home.headline",
            "home.intro",
            "home.pillars_intro",
            # chi-siamo
            "chi-siamo.intro",
            "chi-siamo.history_heading",
            # competenze
            "competenze.headline",
            "competenze.cta_intro",
            # case-studies
            "case-studies.intro",
            "case-studies.cta_primary",
            # contatti chrome (site.* customer-copy universals)
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on Pragma after A.7b",
            )

    def test_a7b_pragma_branding_and_contact_universals_are_global(self):
        """Identity + per-row contact universals (logo, phone, email,
        address, license, logo_initial) stay global on Pragma like they
        do on Vertex — shared ``_GLOBAL_TEXT_PATHS`` set."""
        from apps.editor.schema import is_translatable
        arc = "corporate-suite"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Pragma",
            )

    def test_a7b_pragma_non_text_fields_are_global(self):
        """Pragma image + select fields always stay global — only
        text/textarea/richtext may be translatable."""
        from apps.editor.schema import is_translatable
        arc = "corporate-suite"
        self.assertFalse(is_translatable(arc, "home.hero_image"))     # image
        self.assertFalse(is_translatable(arc, "home.primary_href"))   # select
        self.assertFalse(is_translatable(arc, "home.cta_primary_href"))

    def test_a7b_pragma_structured_list_cells_are_global(self):
        """The 3 readonly indexed lists on Pragma (pillars · kpi_strip ·
        leadership) stay global at cell level — A.7 family explicitly
        excludes repeater content from per-locale editing."""
        from apps.editor.schema import is_translatable
        arc = "corporate-suite"
        for path in ("home.pillars.0.title", "home.pillars.0.body",
                     "home.kpi_strip.0.number", "home.kpi_strip.0.label",
                     "home.leadership.0.name", "home.leadership.0.role",
                     "home.leadership.0.bio"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Pragma",
            )

    def test_a7b_pragma_supported_locales_returns_canonical_five(self):
        """Pragma now ships the canonical 5-locale set exposed by the
        editor context — same shape as Vertex."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("corporate-suite"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a7b_vertex_still_enrolled_after_pragma_joins(self):
        """Regression guard: adding Pragma to the gate must not disturb
        the Vertex classification or supported-locales contract."""
        from apps.editor.schema import is_translatable, supported_locales
        self.assertTrue(is_translatable("agency-creative-studio", "home.headline"))
        self.assertFalse(is_translatable("agency-creative-studio", "site.logo_word"))
        self.assertEqual(
            supported_locales("agency-creative-studio"),
            ["it", "en", "fr", "es", "ar"],
        )
        # Archetype outside the gate still returns False + empty list.
        self.assertFalse(is_translatable("trattoria-warm", "home.headline"))
        self.assertEqual(supported_locales("trattoria-warm"), [])

    # ------------------------------------------------------------------
    # A.8 · Gusto fine-dining enrollment — Step 1 contract
    # ------------------------------------------------------------------

    def test_a8_gusto_archetype_registered(self):
        """``fine-dining`` joins the schema + baseline template + gate
        registries alongside the pre-existing Vertex / Pragma entries."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("fine-dining", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["fine-dining"],
            ("gusto-fine-dining", "it"),
        )
        self.assertIn("fine-dining", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("fine-dining"))

    def test_a8_gusto_schema_shape_covers_all_pages(self):
        """The Gusto schema must surface at least one group per Gusto
        page slug (home + filosofia + menu + atmosfera + diario +
        prenota) plus chrome-level groups (page='*')."""
        groups = iter_groups("fine-dining")
        self.assertGreaterEqual(len(groups), 10)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "filosofia", "menu",
                     "atmosfera", "diario", "prenota"):
            self.assertIn(slug, pages,
                          f"Gusto schema missing page slug {slug!r}")

    def test_a8_gusto_is_translatable_text_fields(self):
        """Scalar copy fields distributed across all 5 Gusto pages +
        chrome — the gate must not pass by covering only ``home``."""
        from apps.editor.schema import is_translatable
        arc = "fine-dining"
        distributed_paths = (
            # home — hero + editorial bands
            "home.headline",
            "home.manifesto",
            "home.ingredienti.heading",
            "home.chef.bio",
            "home.produttori.intro",
            # filosofia
            "filosofia.intro",
            "filosofia.values_heading",
            # menu
            "menu.headline",
            "menu.wine_intro",
            # atmosfera
            "atmosfera.intro",
            "atmosfera.cta_quote",
            # diario
            "diario.headline",
            # prenota
            "prenota.intro",
            "prenota.concierge.bio",
            # chrome site.* customer-copy universals
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
            "site.copyright",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on Gusto",
            )

    def test_a8_gusto_branding_and_contact_universals_are_global(self):
        """Identity + per-row contact universals stay global on Gusto —
        same shared ``_GLOBAL_TEXT_PATHS`` set used by Vertex + Pragma."""
        from apps.editor.schema import is_translatable
        arc = "fine-dining"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email", "site.address"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Gusto",
            )

    def test_a8_gusto_non_text_fields_are_global(self):
        """Image + select fields on Gusto always stay global — only
        text/textarea/richtext can be flagged translatable."""
        from apps.editor.schema import is_translatable
        arc = "fine-dining"
        # Scalar image fields
        self.assertFalse(is_translatable(arc, "home.ingredienti.image"))
        self.assertFalse(is_translatable(arc, "filosofia.filosofia_image"))
        # Select (page-slug choice) fields
        self.assertFalse(is_translatable(arc, "home.primary_href"))
        self.assertFalse(is_translatable(arc, "home.secondary_href"))
        self.assertFalse(is_translatable(arc, "home.stagione.cta_href"))
        self.assertFalse(is_translatable(arc, "home.private_dining.cta_href"))

    def test_a8_gusto_structured_list_cells_are_global(self):
        """The 3 readonly indexed lists on Gusto (signature_courses,
        menu.courses, produttori.items) stay global at cell level. The
        ``portrait`` column on produttori is intentionally NOT exposed
        in the dict shape — customer cannot reach it through the editor."""
        from apps.editor.schema import is_translatable, get_list_shape
        arc = "fine-dining"
        for path in ("home.signature_courses.0.title",
                     "home.signature_courses.0.detail",
                     "menu.courses.0.title",
                     "menu.courses.7.wine",
                     "home.produttori.items.0.name",
                     "home.produttori.items.0.blurb"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Gusto",
            )
        # portrait must NOT appear among produttori cols (readonly at
        # registry level, invisible to the editor service layer).
        shape = get_list_shape(arc, "home.produttori.items")
        self.assertIsNotNone(shape)
        col_names = {name for name, _spec in (shape.get("cols") or [])}
        self.assertNotIn("portrait", col_names,
                         "Gusto producers dict must NOT expose portrait as an editable col")

    def test_a8_vertex_and_pragma_still_enrolled_after_gusto_joins(self):
        """Regression guard: adding Gusto to gate + schemas must not
        disturb the Vertex or Pragma classifications."""
        from apps.editor.schema import is_translatable, supported_locales
        # Vertex intact
        self.assertTrue(is_translatable("agency-creative-studio", "home.headline"))
        self.assertEqual(
            supported_locales("agency-creative-studio"),
            ["it", "en", "fr", "es", "ar"],
        )
        # Pragma intact
        self.assertTrue(is_translatable("corporate-suite", "home.headline"))
        self.assertEqual(
            supported_locales("corporate-suite"),
            ["it", "en", "fr", "es", "ar"],
        )
        # Gusto now enrolled alongside them
        self.assertEqual(
            supported_locales("fine-dining"),
            ["it", "en", "fr", "es", "ar"],
        )

    # ------------------------------------------------------------------
    # A.9 · medical-specialist enrollment (Cardio + Derm · shared schema)
    # ------------------------------------------------------------------

    def test_a9_specialist_archetype_registered(self):
        """``specialist`` joins the schema + baseline template + gate
        registries. Baseline anchors Cardio (i18n pilot template) but
        the schema is shared with Derm via the DNA archetype slug."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("specialist", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["specialist"],
            ("cardio-studio-specialistico", "it"),
        )
        self.assertIn("specialist", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("specialist"))

    def test_a9_specialist_schema_shape_covers_all_shared_pages(self):
        """The specialist schema must surface groups for every shared
        Cardio/Derm page (home + studio + visite + medici + pubblicazioni
        + contatti + richiedi-visita) plus chrome-level groups."""
        groups = iter_groups("specialist")
        self.assertGreaterEqual(len(groups), 11)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "studio", "visite", "medici",
                     "pubblicazioni", "contatti", "richiedi-visita"):
            self.assertIn(slug, pages,
                          f"specialist schema missing page slug {slug!r}")

    def test_a9_specialist_is_translatable_text_fields(self):
        """Scalar copy fields distributed across every shared page +
        chrome. Uses only paths present on BOTH Cardio and Derm so the
        test passes independently of which template is instantiated."""
        from apps.editor.schema import is_translatable
        arc = "specialist"
        distributed_paths = (
            # hero_home + home bands
            "home.headline",
            "home.intro",
            "home.manifesto",
            "home.signature_visits_heading",
            "home.chief.bio",
            # studio
            "studio.intro",
            "studio.values_heading",
            # visite
            "visite.headline",
            "visite.footnote",
            # medici
            "medici.intro",
            # pubblicazioni
            "pubblicazioni.headline",
            # contatti
            "contatti.intro",
            "contatti.form_intro",
            # richiedi-visita
            "richiedi-visita.process_heading",
            "richiedi-visita.consent",
            # chrome site.*
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on specialist",
            )

    def test_a9_specialist_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on specialist, same
        contract as Vertex / Pragma / Gusto."""
        from apps.editor.schema import is_translatable
        arc = "specialist"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on specialist",
            )

    def test_a9_specialist_non_text_fields_are_global(self):
        """Image + select fields on specialist always stay global."""
        from apps.editor.schema import is_translatable
        arc = "specialist"
        # Scalar image fields
        self.assertFalse(is_translatable(arc, "home.chief.portrait"))
        self.assertFalse(is_translatable(arc, "studio.studio_image"))
        self.assertFalse(is_translatable(arc, "visite.service_image"))
        self.assertFalse(is_translatable(arc, "pubblicazioni.lead_image"))
        # Select (page-slug choice) fields
        self.assertFalse(is_translatable(arc, "home.primary_href"))
        self.assertFalse(is_translatable(arc, "home.secondary_href"))

    def test_a9_specialist_structured_list_cells_are_global(self):
        """The 6 readonly indexed lists on specialist stay global at
        cell level. The ``portrait`` column on medici.doctors is
        intentionally NOT exposed in the dict shape cols (same pattern
        as Gusto produttori.items)."""
        from apps.editor.schema import is_translatable, get_list_shape
        arc = "specialist"
        for path in ("home.facts.0.label",
                     "home.signature_visits.0.title",
                     "medici.doctors.0.name",
                     "medici.doctors.0.bio",
                     "studio.history.0.title",
                     "studio.values.0.body",
                     "visite.treatments.0.title",
                     "visite.treatments.5.duration"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on specialist",
            )
        # portrait must NOT appear among medici.doctors cols (stays
        # readonly at the registry level).
        shape = get_list_shape(arc, "medici.doctors")
        self.assertIsNotNone(shape)
        col_names = {name for name, _spec in (shape.get("cols") or [])}
        self.assertNotIn("portrait", col_names,
                         "specialist medici.doctors dict must NOT expose portrait as an editable col")

    def test_a9_specialist_divergent_premium_sections_excluded(self):
        """User-imposed guardrail (A.9 planning rifinitura): the D-064
        Session-30 premium-section split between Cardio and Derm must
        stay OUT of the shared schema in the A.8 first wave. Neither
        Cardio-only sub-blocks (anchor_nav · insurance · location ·
        percorso · tecnologie) nor Derm-only sub-blocks (before_after ·
        credentials · editorial_feed · gallery_strip · trattamenti_tabs)
        should be writable through the editor in A.9. Each block's
        authored registry keeps rendering unchanged.

        Protects against a future coverage pass re-introducing them by
        mistake while building out the shared schema.
        """
        from apps.editor.schema import (
            is_translatable, validate_key_path, InvalidEditableField,
            get_list_shape, _ARCHETYPE_SCHEMAS,
        )
        arc = "specialist"

        # Paths drawn from the audit: scalar keys + known leaf keys
        # inside the 10 divergent sub-blocks. The full sub-block roots
        # (home.insurance, home.trattamenti_tabs etc.) are NOT valid
        # whitelist entries on their own, but we also test their
        # ``.items``/``.label``/``.heading`` leaves to catch a future
        # edit that tries to expose them piecewise.
        cardio_only_paths = (
            "home.anchor_nav",
            "home.insurance.label",
            "home.insurance.items",
            "home.location.heading",
            "home.location.intro",
            "home.location.map_fallback_image",
            "home.percorso.label",
            "home.percorso.heading",
            "home.percorso.steps",
            "home.tecnologie.label",
            "home.tecnologie.heading",
            "home.tecnologie.items",
        )
        derm_only_paths = (
            "home.before_after.label",
            "home.before_after.heading",
            "home.credentials.label",
            "home.credentials.items",
            "home.editorial_feed.label",
            "home.editorial_feed.items",
            "home.gallery_strip.label",
            "home.gallery_strip.images",
            "home.trattamenti_tabs.label",
            "home.trattamenti_tabs.heading",
            "home.trattamenti_tabs.tabs",
        )

        # (a) is_translatable MUST return False for every divergent
        # path — none of them sit on the translatable whitelist.
        for path in cardio_only_paths + derm_only_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} (divergent premium section) must NOT be translatable in A.9",
            )

        # (b) validate_key_path MUST raise InvalidEditableField for
        # every divergent path — customer autosave can't target them.
        for path in cardio_only_paths + derm_only_paths:
            with self.assertRaises(InvalidEditableField,
                                    msg=f"{path} must reject validate_key_path"):
                validate_key_path(arc, path)

        # (c) None of the divergent list paths may appear in
        # STRUCTURED_FIELD_SHAPES['specialist'] as readonly lists.
        divergent_list_paths = (
            "home.anchor_nav", "home.insurance.items", "home.percorso.steps",
            "home.tecnologie.items", "home.location.details",
            "home.before_after", "home.credentials.items",
            "home.editorial_feed.items", "home.gallery_strip.images",
            "home.trattamenti_tabs.tabs",
        )
        for list_path in divergent_list_paths:
            self.assertIsNone(
                get_list_shape(arc, list_path),
                f"{list_path} must NOT be in STRUCTURED_FIELD_SHAPES['specialist']",
            )

        # (d) No sidebar group ``id`` may hint at a divergent block —
        # purely defensive; an authoring mistake would typically
        # surface at (a)/(b) first but this catches a future sidebar
        # group added without corresponding fields.
        schema_ids = {g["id"] for g in _ARCHETYPE_SCHEMAS[arc]}
        for banned in ("home_anchor_nav", "home_insurance", "home_location",
                       "home_percorso", "home_tecnologie",
                       "home_before_after", "home_credentials",
                       "home_editorial_feed", "home_gallery_strip",
                       "home_trattamenti_tabs"):
            self.assertNotIn(banned, schema_ids,
                             f"sidebar group {banned!r} must not exist in A.9 first wave")

    def test_a9_specialist_supported_locales_returns_canonical_five(self):
        """specialist ships the canonical 5-locale set, same as Vertex /
        Pragma / Gusto."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("specialist"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a9_vertex_pragma_gusto_still_enrolled_after_specialist_joins(self):
        """Triple regression guard: adding specialist to gate + schemas
        must not disturb any of the 3 pre-existing enrollments."""
        from apps.editor.schema import is_translatable, supported_locales
        for arc in ("agency-creative-studio", "corporate-suite", "fine-dining"):
            self.assertTrue(is_translatable(arc, "home.headline"),
                             f"{arc} home.headline must stay translatable")
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must keep the canonical 5-locale set",
            )

    def test_a9_specialist_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8 Gusto integration guardrail — the specialist
        ``_base.html`` must integrate the three bridge points together:
        (1) preview-bridge.js conditional on ``preview_project``, (2)
        ``<title>`` honors ``site.logo_word``, (3) ``<body>`` carries
        the ``mw-is-editor-preview`` guard class when inside the editor.
        Validated on Cardio (specialist archetype uses the same
        _base.html for Derm)."""
        cardio = WebTemplate.objects.get(slug="cardio-studio-specialistico")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/medical/cardio-studio-specialistico/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=cardio)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A9 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/medical/cardio-studio-specialistico/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A9 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.10 · Lex (classic-gold archetype · law family) enrollment
    # ------------------------------------------------------------------

    def test_a10_lex_archetype_registered(self):
        """``classic-gold`` joins the schema + baseline template + gate
        registries. (Juris `modern-transparent` was the A.11 phase; that
        test lives below.)"""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("classic-gold", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["classic-gold"],
            ("lex-studio-legale", "it"),
        )
        self.assertIn("classic-gold", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("classic-gold"))

    def test_a10_lex_schema_shape_covers_all_pages(self):
        """The Lex schema must surface groups for every Lex page slug
        (home + studio + pratiche + avvocati + notabili + contatti)
        plus chrome-level groups (page='*')."""
        groups = iter_groups("classic-gold")
        self.assertGreaterEqual(len(groups), 9)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "studio", "pratiche", "avvocati",
                     "notabili", "contatti"):
            self.assertIn(slug, pages,
                          f"Lex schema missing page slug {slug!r}")

    def test_a10_lex_is_translatable_text_fields(self):
        """Scalar copy fields distributed across every Lex page + chrome.
        Uses only paths present on Lex so a future Juris enrollment
        doesn't accidentally make this test drift."""
        from apps.editor.schema import is_translatable
        arc = "classic-gold"
        distributed_paths = (
            # home — hero + bands
            "home.headline",
            "home.intro",
            "home.practice_heading",
            "home.partners_heading",
            "home.cta_heading",
            # studio
            "studio.intro",
            "studio.history_heading",
            "studio.values_heading",
            # pratiche
            "pratiche.headline",
            "pratiche.process_heading",
            # avvocati
            "avvocati.intro",
            "avvocati.lawyer_foro_label",
            # notabili
            "notabili.headline",
            # contatti
            "contatti.intro",
            "contatti.form_heading",
            "contatti.footnote",
            # chrome site.* customer-copy universals
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
            "site.case_lead_label",
            "site.foot_studio",
            "site.nav_cta",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on classic-gold",
            )

    def test_a10_lex_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Lex — same contract
        as Vertex / Pragma / Gusto / specialist."""
        from apps.editor.schema import is_translatable
        arc = "classic-gold"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Lex",
            )

    def test_a10_lex_non_text_fields_are_global(self):
        """Image + select fields on Lex always stay global."""
        from apps.editor.schema import is_translatable
        arc = "classic-gold"
        # Scalar image field (Lex ships exactly one: notabili.lead_image)
        self.assertFalse(is_translatable(arc, "notabili.lead_image"))
        # Select (page-slug choice) fields
        self.assertFalse(is_translatable(arc, "home.primary_href"))
        self.assertFalse(is_translatable(arc, "home.secondary_href"))
        self.assertFalse(is_translatable(arc, "home.cta_primary_href"))
        self.assertFalse(is_translatable(arc, "home.cta_secondary_href"))
        self.assertFalse(is_translatable(arc, "studio.cta_primary_href"))
        self.assertFalse(is_translatable(arc, "pratiche.cta_primary_href"))

    def test_a10_lex_structured_list_cells_are_global(self):
        """The 6 readonly indexed lists on Lex stay global at cell level.
        Lex ships no portrait fields anywhere in the registry, so no
        col-exclusion is required (unlike Gusto produttori.items and
        specialist medici.doctors). The ``scope`` nested list-of-str
        inside ``pratiche.services`` rows is intentionally NOT exposed
        in the dict shape cols — stays registry-only."""
        from apps.editor.schema import is_translatable, get_list_shape
        arc = "classic-gold"
        for path in ("avvocati.lawyers.0.name",
                     "avvocati.lawyers.13.bio",
                     "pratiche.services.0.title",
                     "pratiche.services.0.blurb",
                     "pratiche.services.11.jurisdiction",
                     "pratiche.process.0.title",
                     "studio.history.0.title",
                     "studio.values.0.body",
                     "contatti.offices.0.city",
                     "contatti.offices.1.phone"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Lex",
            )
        # pratiche.services: `scope` (list-of-str bullet points) must NOT
        # appear in the dict shape cols (bullet points stay registry-only).
        services_shape = get_list_shape(arc, "pratiche.services")
        self.assertIsNotNone(services_shape)
        col_names = {name for name, _spec in (services_shape.get("cols") or [])}
        self.assertNotIn("scope", col_names,
                         "classic-gold pratiche.services must NOT expose scope as an editable col")

    def test_a10_lex_supported_locales_returns_canonical_five(self):
        """Lex ships the canonical 5-locale set, same as Vertex / Pragma
        / Gusto / specialist. Lex is the cleanest content registry
        audited so far — zero IT-only parity gaps even on form_fields /
        form_sections / upload_field."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("classic-gold"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a10_quadruple_regression_after_lex_joins(self):
        """Regression guard: adding Lex to gate + schemas must not
        disturb ANY of the four pre-existing enrollments (Vertex +
        Pragma + Gusto + specialist)."""
        from apps.editor.schema import is_translatable, supported_locales
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist"):
            self.assertTrue(
                is_translatable(arc, "home.headline"),
                f"{arc} home.headline must stay translatable",
            )
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must keep the canonical 5-locale set",
            )

    def test_a10_lex_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8/A.9 integration guardrail — the Lex
        ``classic-gold/_base.html`` must integrate the three bridge
        points together: (1) preview-bridge.js conditional on
        ``preview_project``, (2) ``<title>`` honors ``site.logo_word``,
        (3) ``<body>`` carries the ``mw-is-editor-preview`` guard class
        when inside the editor."""
        lex = WebTemplate.objects.get(slug="lex-studio-legale")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/lawyer/lex-studio-legale/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=lex)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A10 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/lawyer/lex-studio-legale/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A10 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.11 · Juris (modern-transparent archetype · law family) enrollment
    # ------------------------------------------------------------------

    def test_a11_juris_archetype_registered(self):
        """``modern-transparent`` joins the schema + baseline template +
        gate registries as 5th enrolled archetype. Classic-gold (Lex)
        remains enrolled — A.11 must not displace A.10 from the gate."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("modern-transparent", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["modern-transparent"],
            ("juris-avvocato-moderno", "it"),
        )
        self.assertIn("modern-transparent", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("modern-transparent"))
        # Lex / classic-gold must STAY enrolled — A.11 is additive, not a
        # replacement of A.10.
        self.assertIn("classic-gold", _ARCHETYPE_SCHEMAS)
        self.assertIn("classic-gold", _MULTILOCALE_ENABLED_ARCHETYPES)

    def test_a11_juris_schema_shape_covers_all_pages(self):
        """The Juris schema must surface groups for every Juris page slug
        (home + approccio + servizi + settori + insights + contatti)
        plus chrome-level groups (page='*')."""
        groups = iter_groups("modern-transparent")
        self.assertGreaterEqual(len(groups), 9)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "approccio", "servizi", "settori",
                     "insights", "contatti"):
            self.assertIn(slug, pages,
                          f"Juris schema missing page slug {slug!r}")

    def test_a11_juris_is_translatable_text_fields(self):
        """Scalar copy fields distributed across every Juris page +
        chrome. Uses only paths present on Juris so Lex / specialist /
        Gusto / Pragma / Vertex schemas don't accidentally drift into
        this test."""
        from apps.editor.schema import is_translatable
        arc = "modern-transparent"
        distributed_paths = (
            # home — hero + bands
            "home.headline",
            "home.intro",
            "home.sprint_chip",
            "home.sectors_heading",
            "home.process_heading",
            "home.metric_heading",
            "home.insights_heading",
            "home.cta_heading",
            # approccio
            "approccio.intro",
            "approccio.manifesto_heading",
            "approccio.story_heading",
            "approccio.dashboard_heading",
            # servizi
            "servizi.headline",
            "servizi.process_heading",
            "servizi.faq_heading",
            "servizi.svc_duration_label",
            # settori
            "settori.headline",
            "settori.team_intro",
            # insights
            "insights.headline",
            "insights.posts_intro",
            # contatti
            "contatti.intro",
            "contatti.form_heading",
            "contatti.slot_value",
            "contatti.footnote",
            # chrome site.* customer-copy universals
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
            "site.foot_studio",
            "site.nav_cta",
            "site.post_author_label",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on modern-transparent",
            )

    def test_a11_juris_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Juris — same contract
        as Vertex / Pragma / Gusto / specialist / Lex."""
        from apps.editor.schema import is_translatable
        arc = "modern-transparent"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Juris",
            )

    def test_a11_juris_schema_contains_zero_image_fields(self):
        """USER-IMPOSED GUARDRAIL · zero-image assertion strong.

        Juris advisory-modern DNA explicitly rejects founder portraits /
        case photos / hero illustrations. The schema must contain ZERO
        fields of ``type: "image"`` across every group + subgroup. Same
        must hold for STRUCTURED_FIELD_SHAPES["modern-transparent"]: no
        col can expose an image widget.

        This guard is the explicit contract that prevents scope creep
        into the pictorial layer on future A.11+ maintenance."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, STRUCTURED_FIELD_SHAPES,
        )
        arc = "modern-transparent"
        # 1. Scan every group + subgroup in the flat archetype schema.
        offenders: list[str] = []
        for group in _ARCHETYPE_SCHEMAS[arc]:
            for key, spec in group.get("fields", []) or []:
                if spec.get("type") == "image":
                    offenders.append(f"group={group['id']} key={key}")
            for sub in group.get("subgroups", []) or []:
                for key, spec in sub.get("fields", []) or []:
                    if spec.get("type") == "image":
                        offenders.append(
                            f"group={group['id']} subgroup={sub['label']} key={key}"
                        )
        # 2. Scan every col of every readonly indexed list.
        for list_path, shape in (STRUCTURED_FIELD_SHAPES.get(arc) or {}).items():
            for col_name, spec in shape.get("cols") or []:
                if spec.get("type") == "image":
                    offenders.append(
                        f"list={list_path} col={col_name}"
                    )
            if shape.get("cell_spec", {}).get("type") == "image":
                offenders.append(f"list={list_path} cell_spec")
        self.assertEqual(
            offenders, [],
            "modern-transparent schema MUST contain zero image fields; "
            f"found: {offenders}",
        )

    def test_a11_juris_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL · complex-shape exclusion test.

        Four categories of complex registry shapes must stay OUT of the
        editor perimeter for A.11 (scope creep prevention while writing
        the schema):

        (1) ``approccio.dashboard_mock`` — nested dict with URL +
            columns + cards (novel shape, not mappable to tuple/dict).
        (2) ``home.trust_logos`` — flat list of str (marquee wordmarks).
            ``insights.topics`` is a similar list-of-str (filter pills).
        (3) Nested list-of-str cells inside dict rows:
              - ``servizi.services[*].deliverables``
              - ``settori.sectors[*].pain_points``
              - ``settori.sectors[*].signals``
              - ``settori.sectors[*].legal_ops`` (the BULLET LIST, not
                the scalar partner-name col of the same key name)
            These four must NOT appear in the parent list's dict-shape
            ``cols`` (same exclusion policy as Lex
            ``pratiche.services[*].scope``).
        (4) Every path in (1)-(3) must fail ``validate_key_path`` so the
            autosave endpoint cannot persist an override on them even if
            a crafted payload reaches the service layer."""
        from apps.editor.schema import (
            STRUCTURED_FIELD_SHAPES, get_list_shape, validate_key_path,
        )
        arc = "modern-transparent"

        # (1) dashboard_mock must not be in the schema nor the list shapes
        validate_rejects = [
            "approccio.dashboard_mock",
            "approccio.dashboard_mock.columns.0.label",
            "approccio.dashboard_mock.columns.0.cards.0.title",
            # (2) flat list-of-str containers
            "home.trust_logos",
            "home.trust_logos.0",
            "insights.topics",
            "insights.topics.0",
            # (3) nested bullet-list cells inside dict rows
            "servizi.services.0.deliverables",
            "servizi.services.0.deliverables.0",
            "settori.sectors.0.pain_points",
            "settori.sectors.0.pain_points.0",
            "settori.sectors.0.signals",
            "settori.sectors.0.signals.0",
        ]
        for path in validate_rejects:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"{path} MUST be rejected by validate_key_path on modern-transparent",
            ):
                validate_key_path(arc, path)

        # (3bis) servizi.services cols must NOT expose `deliverables`
        services_shape = get_list_shape(arc, "servizi.services")
        self.assertIsNotNone(services_shape)
        services_cols = {name for name, _spec in services_shape.get("cols") or []}
        self.assertNotIn(
            "deliverables", services_cols,
            "modern-transparent servizi.services MUST NOT expose deliverables "
            "(nested bullet list — stays registry-only)",
        )

        # (3ter) settori.sectors cols must NOT expose the 3 bullet lists.
        # The `legal_ops` SCALAR col (partner-name string) IS allowed —
        # it's the per-row person, not the list of bullet points. The
        # list-of-str `legal_ops` at ``settori.sectors.*.legal_ops.<idx>``
        # is rejected by validate_key_path above since no further shape
        # descends from a scalar text col.
        sectors_shape = get_list_shape(arc, "settori.sectors")
        self.assertIsNotNone(sectors_shape)
        sectors_cols = {name for name, _spec in sectors_shape.get("cols") or []}
        for forbidden in ("pain_points", "signals"):
            self.assertNotIn(
                forbidden, sectors_cols,
                f"modern-transparent settori.sectors MUST NOT expose "
                f"{forbidden!r} (nested bullet list — stays registry-only)",
            )

    def test_a11_juris_structured_list_cells_are_global(self):
        """The 6 readonly indexed lists on Juris stay global at cell
        level — text cols exposed via STRUCTURED_FIELD_SHAPES are
        customer-editable but never per-locale (same contract as every
        other enrolled archetype)."""
        from apps.editor.schema import is_translatable
        arc = "modern-transparent"
        cell_paths = (
            "approccio.founders.0.name",
            "approccio.founders.1.bio",
            "approccio.story.0.title",
            "approccio.story.4.body",
            "approccio.manifesto.0.title",
            "approccio.manifesto.3.body",
            "servizi.services.0.title",
            "servizi.services.0.blurb",
            "servizi.services.6.engagement",
            "settori.sectors.0.title",
            "settori.sectors.5.case_snippet",
            "settori.sectors.0.partner",
            "settori.team.0.name",
            "settori.team.9.email",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Juris",
            )

    def test_a11_juris_supported_locales_returns_canonical_five(self):
        """Juris ships the canonical 5-locale set, same as every other
        enrolled archetype. Audit confirmed zero IT-only parity gaps."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("modern-transparent"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a11_quintuple_regression_after_juris_joins(self):
        """Regression guard: adding Juris to gate + schemas must not
        disturb ANY of the five pre-existing enrollments (Vertex +
        Pragma + Gusto + specialist + Lex/classic-gold)."""
        from apps.editor.schema import is_translatable, supported_locales
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold"):
            self.assertTrue(
                is_translatable(arc, "home.headline"),
                f"{arc} home.headline must stay translatable",
            )
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must keep the canonical 5-locale set",
            )

    def test_a11_juris_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8/A.9/A.10 integration guardrail — the Juris
        ``modern-transparent/_base.html`` must integrate the three
        bridge points together: (1) preview-bridge.js conditional on
        ``preview_project``, (2) ``<title>`` honors ``site.logo_word``,
        (3) ``<body>`` carries the ``mw-is-editor-preview`` guard class
        when inside the editor."""
        juris = WebTemplate.objects.get(slug="juris-avvocato-moderno")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/lawyer/juris-avvocato-moderno/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=juris)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A11 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/lawyer/juris-avvocato-moderno/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A11 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.12 · Casa (mass-market archetype · real-estate family) enrollment
    # ------------------------------------------------------------------

    def test_a12_casa_archetype_registered(self):
        """``mass-market`` joins the schema + baseline template + gate
        registries as 7th enrolled archetype. Villa (``ultra-luxury-
        cinematic``) stays explicitly OUT — it is a distinct archetype
        and will be enrolled separately as A.12b with its own schema +
        skin bridge + lifecycle test. The guard here mirrors the A.10
        Lex pattern of explicitly locking a sibling archetype out of
        the gate."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("mass-market", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["mass-market"],
            ("casa-agenzia-immobiliare", "it"),
        )
        self.assertIn("mass-market", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("mass-market"))
        # A.12b · Villa (ultra-luxury-cinematic) has joined the gate;
        # the Villa-out guard that used to live here is now the
        # responsibility of `test_a12b_villa_archetype_registered`
        # which asserts Villa IN + Casa still IN. The Casa-must-stay
        # regression guard below is preserved.
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent"):
            self.assertIn(arc, _ARCHETYPE_SCHEMAS)
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES)

    def test_a12_casa_schema_shape_covers_all_pages(self):
        """The Casa schema must surface groups for every Casa page slug
        (home + immobili + quartieri + agenzia + valutazione + contatti)
        plus chrome-level groups (page='*')."""
        groups = iter_groups("mass-market")
        self.assertGreaterEqual(len(groups), 10)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "immobili", "quartieri", "agenzia",
                     "valutazione", "contatti"):
            self.assertIn(slug, pages,
                          f"Casa schema missing page slug {slug!r}")

    def test_a12_casa_is_translatable_text_fields(self):
        """Scalar copy fields distributed across every Casa page +
        chrome. Uses only paths present on Casa so neither Lex nor
        Juris nor any other schema accidentally drifts into this test."""
        from apps.editor.schema import is_translatable
        arc = "mass-market"
        distributed_paths = (
            # home — hero + search widget + bands
            "home.headline",
            "home.intro",
            "home.search_widget.label",
            "home.search_widget.location_label",
            "home.search_widget.location_value",
            "home.search_widget.cta",
            "home.featured_heading",
            "home.neighborhoods_heading",
            "home.stats_heading",
            "home.agents_heading",
            "home.valuation_heading",
            "home.testimonial_quote",
            # immobili
            "immobili.headline",
            "immobili.filter_label",
            "immobili.map_heading",
            # quartieri
            "quartieri.headline",
            "quartieri.guides_heading",
            "quartieri.faq_heading",
            # agenzia
            "agenzia.headline",
            "agenzia.agents_heading",
            "agenzia.facts_heading",
            # valutazione
            "valutazione.headline",
            "valutazione.how_it_works_heading",
            "valutazione.form_heading",
            "valutazione.form_consent",
            # contatti
            "contatti.headline",
            "contatti.offices_heading",
            "contatti.channels_heading",
            # chrome site.* + tile labels
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
            "site.foot_studio",
            "site.nav_cta",
            "site.tile_rooms_label",
            "site.energy_class_label",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on mass-market",
            )

    def test_a12_casa_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Casa — same contract
        as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "mass-market"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Casa",
            )

    def test_a12_casa_schema_contains_zero_image_fields(self):
        """USER-IMPOSED GUARDRAIL · zero-image assertion strong.

        Casa is the second zero-image archetype after Juris (A.11).
        The mass-market DNA doesn't ship any image / portrait / photo
        fields in the registry (verified by the A.12 Step-0 audit:
        Casa.IT has zero image-like scalars across all pages, contra
        Villa.IT which has 26). The schema must contain ZERO fields of
        ``type: "image"`` across every group + subgroup. Same holds
        for STRUCTURED_FIELD_SHAPES["mass-market"]: no col or
        cell_spec can expose an image widget.

        This guard locks the DNA constraint into the test layer and
        prevents scope creep into the pictorial layer on future A.12+
        maintenance."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, STRUCTURED_FIELD_SHAPES,
        )
        arc = "mass-market"
        offenders: list[str] = []
        for group in _ARCHETYPE_SCHEMAS[arc]:
            for key, spec in group.get("fields", []) or []:
                if spec.get("type") == "image":
                    offenders.append(f"group={group['id']} key={key}")
            for sub in group.get("subgroups", []) or []:
                for key, spec in sub.get("fields", []) or []:
                    if spec.get("type") == "image":
                        offenders.append(
                            f"group={group['id']} subgroup={sub['label']} key={key}"
                        )
        for list_path, shape in (STRUCTURED_FIELD_SHAPES.get(arc) or {}).items():
            for col_name, spec in shape.get("cols") or []:
                if spec.get("type") == "image":
                    offenders.append(f"list={list_path} col={col_name}")
            if shape.get("cell_spec", {}).get("type") == "image":
                offenders.append(f"list={list_path} cell_spec")
        self.assertEqual(
            offenders, [],
            "mass-market schema MUST contain zero image fields; "
            f"found: {offenders}",
        )

    def test_a12_casa_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL · complex-shape exclusion test.

        Three categories of complex registry shapes must stay OUT of
        the Casa editor perimeter (scope creep prevention while writing
        the schema):

        (1) Flat list-of-str containers:
              - ``home.search_widget.popular_tags`` (popular search
                suggestion wordmarks)
              - ``immobili.filters`` (11 filter pills)
              - ``immobili.sort_options`` (4 sort order labels)
            All same exclusion policy as Juris ``home.trust_logos`` +
            ``insights.topics``.

        (2) Form structure blocks:
              - ``valutazione.form_fields`` + ``form_sections``
              - ``contatti.form_fields`` + ``form_sections``
            Same policy as Gusto / specialist / Lex / Juris.

        (3) Property-detail entries under ``posts`` (12 property
            records with per-property copy like Lex ``notabili``
            posts). Stays registry-only — detail-page editing is NOT
            in A.12 scope.

        Every path listed must fail ``validate_key_path`` so the
        autosave endpoint cannot persist an override on them even if
        a crafted payload reaches the service layer."""
        from apps.editor.schema import validate_key_path
        arc = "mass-market"
        validate_rejects = [
            # (1) flat list-of-str containers
            "home.search_widget.popular_tags",
            "home.search_widget.popular_tags.0",
            "immobili.filters",
            "immobili.filters.0",
            "immobili.sort_options",
            "immobili.sort_options.0",
            # (2) form structure blocks
            "valutazione.form_fields",
            "valutazione.form_fields.0.name",
            "valutazione.form_sections",
            "valutazione.form_sections.0.title",
            "contatti.form_fields",
            "contatti.form_fields.0.label",
            "contatti.form_sections",
            # (3) property-detail entries
            "posts",
            "posts.0.title",
            "posts.0.price",
            "posts.0.description",
        ]
        for path in validate_rejects:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"{path} MUST be rejected by validate_key_path on mass-market",
            ):
                validate_key_path(arc, path)

    def test_a12_casa_structured_list_cells_are_global(self):
        """The 15 readonly indexed lists on Casa stay global at cell
        level — text cols exposed via STRUCTURED_FIELD_SHAPES are
        customer-editable but never per-locale (same contract as every
        other enrolled archetype)."""
        from apps.editor.schema import is_translatable
        arc = "mass-market"
        cell_paths = (
            # home lists
            "home.featured_listings.0.title",
            "home.featured_listings.3.price",
            "home.neighborhoods.0.name",
            "home.neighborhoods.5.tagline",
            "home.stats.0.number",
            "home.stats.3.label",
            "home.agents_preview.0.name",
            "home.valuation_proof.0.value",
            # immobili
            "immobili.map_cells.0.area",
            # quartieri
            "quartieri.guides.0.name",
            "quartieri.guides.7.description",
            "quartieri.faq.0.question",
            # agenzia
            "agenzia.agents.0.name",
            "agenzia.agents.8.email",
            "agenzia.facts.0.number",
            # valutazione
            "valutazione.how_it_works.0.title",
            "valutazione.proof.0.value",
            "valutazione.faq.3.answer",
            # contatti
            "contatti.channels.0.label",
            "contatti.offices.0.name",
            "contatti.offices.1.address",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Casa",
            )

    def test_a12_casa_supported_locales_returns_canonical_five(self):
        """Casa ships the canonical 5-locale set, same as every other
        enrolled archetype. Step-0 audit confirmed zero IT-only parity
        gaps (215 keys × 5 locales, perfect parity)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("mass-market"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a12_sextuple_regression_after_casa_joins(self):
        """Regression guard: adding Casa to gate + schemas must not
        disturb ANY of the six pre-existing enrollments (Vertex +
        Pragma + Gusto + specialist + classic-gold + modern-
        transparent)."""
        from apps.editor.schema import is_translatable, supported_locales
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent"):
            self.assertTrue(
                is_translatable(arc, "home.headline"),
                f"{arc} home.headline must stay translatable",
            )
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must keep the canonical 5-locale set",
            )

    def test_a12_casa_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8/A.9/A.10/A.11 integration guardrail — the
        Casa ``mass-market/_base.html`` must integrate the three bridge
        points together: (1) preview-bridge.js conditional on
        ``preview_project``, (2) ``<title>`` honors ``site.logo_word``,
        (3) ``<body>`` carries the ``mw-is-editor-preview`` guard class
        when inside the editor."""
        casa = WebTemplate.objects.get(slug="casa-agenzia-immobiliare")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/real-estate/casa-agenzia-immobiliare/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=casa)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A12 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/real-estate/casa-agenzia-immobiliare/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A12 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.12b · Villa (ultra-luxury-cinematic archetype · real-estate family)
    # ------------------------------------------------------------------

    def test_a12b_villa_archetype_registered(self):
        """``ultra-luxury-cinematic`` joins the schema + baseline template
        + gate registries as 8th enrolled archetype, closing the
        real-estate family opened in A.12 with Casa.

        This test also **verifies the controlled removal of the
        Villa-out guard** that lived in `test_a12_casa_archetype_registered`
        until A.12 · the Villa-absence assertions were dropped in A.12b
        (the runtime Villa-out assertion inside the Casa lifecycle test
        was also removed). Casa (mass-market) must stay enrolled — A.12b
        is additive.
        """
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("ultra-luxury-cinematic", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["ultra-luxury-cinematic"],
            ("villa-immobili-lusso", "it"),
        )
        self.assertIn("ultra-luxury-cinematic", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("ultra-luxury-cinematic"))
        # Casa (mass-market) must STAY enrolled — A.12b is additive.
        self.assertIn("mass-market", _ARCHETYPE_SCHEMAS)
        self.assertIn("mass-market", _MULTILOCALE_ENABLED_ARCHETYPES)
        # All 6 pre-Casa archetypes still enrolled.
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent"):
            self.assertIn(arc, _ARCHETYPE_SCHEMAS)
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES)

    def test_a12b_villa_out_guard_was_removed_from_casa_tests(self):
        """USER-IMPOSED GUARDRAIL · verifies controlled removal of the
        Villa-out guard that lived in A.12 Casa tests.

        The proof is indirect but airtight: if the Villa-out assertions
        had been left in place while Villa joined the gate, the Casa
        tests (`test_a12_casa_archetype_registered` +
        `test_a12_casa_full_multilocale_lifecycle_end_to_end`) would
        fail at the ``assertNotIn("ultra-luxury-cinematic", ...)`` step
        because Villa IS now in both gate sets. Therefore a green run
        of those two Casa tests implies the guard was removed
        correctly. This test makes that implication explicit by
        checking the gate state the Casa tests now rely on: Villa MUST
        be in `_ARCHETYPE_SCHEMAS` AND in `_MULTILOCALE_ENABLED_ARCHETYPES`
        AND Casa MUST still be in both."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("ultra-luxury-cinematic", _ARCHETYPE_SCHEMAS,
                      "Villa must be in _ARCHETYPE_SCHEMAS post-A.12b")
        self.assertIn("ultra-luxury-cinematic", _MULTILOCALE_ENABLED_ARCHETYPES,
                      "Villa must be in _MULTILOCALE_ENABLED_ARCHETYPES post-A.12b")
        self.assertIn("mass-market", _ARCHETYPE_SCHEMAS,
                      "Casa must still be in _ARCHETYPE_SCHEMAS post-A.12b")
        self.assertIn("mass-market", _MULTILOCALE_ENABLED_ARCHETYPES,
                      "Casa must still be in _MULTILOCALE_ENABLED_ARCHETYPES post-A.12b")

    def test_a12b_villa_schema_shape_covers_all_pages(self):
        """The Villa schema must surface groups for every Villa page slug
        (home + collezione + territorio + studio + esperienza + concierge)
        plus chrome-level groups (page='*')."""
        groups = iter_groups("ultra-luxury-cinematic")
        self.assertGreaterEqual(len(groups), 10)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "collezione", "territorio", "studio",
                     "esperienza", "concierge"):
            self.assertIn(slug, pages,
                          f"Villa schema missing page slug {slug!r}")

    def test_a12b_villa_is_translatable_text_fields(self):
        """Scalar copy fields distributed across every Villa page +
        chrome. Uses only paths present on Villa so no sibling schema
        drifts into this test."""
        from apps.editor.schema import is_translatable
        arc = "ultra-luxury-cinematic"
        distributed_paths = (
            # home hero + bands
            "home.headline",
            "home.sub",
            "home.hero_series_note",
            "home.signature_heading",
            "home.advisor_bio",
            "home.numbers_heading",
            "home.private_heading",
            # collezione
            "collezione.headline",
            "collezione.posts_intro",
            # territorio
            "territorio.headline",
            "territorio.territories_intro",
            "territorio.stats_heading",
            # studio
            "studio.headline",
            "studio.director_bio",
            "studio.advisors_intro",
            # esperienza
            "esperienza.headline",
            "esperienza.process_heading",
            "esperienza.faq_heading",
            # concierge
            "concierge.headline",
            "concierge.intro",
            "concierge.form_section_intro",
            "concierge.press_contact_text",
            # chrome + tile labels
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
            "site.foot_studio",
            "site.nav_cta",
            "site.dossier_label",
            "site.provenance_label",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on ultra-luxury-cinematic",
            )

    def test_a12b_villa_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Villa — same contract
        as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "ultra-luxury-cinematic"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Villa",
            )

    def test_a12b_villa_image_cols_in_dict_shapes_exposed(self):
        """USER-IMPOSED GUARDRAIL · image cols are IN the perimeter
        (opposite contract of the zero-image guards on Juris/Casa).

        Villa's DNA is cinematographic luxury — the imagery IS the
        editorial content. The image-in-dict-row pattern is not novel
        (Vertex `studio.partners.portrait` has shipped since A.3a/A.4),
        but A.12b is the second archetype to use it. This test asserts
        each of the expected image surfaces IS reachable through the
        schema:

        (1) 4 scalar image fields on flat groups:
              - home.cover_image · home.advisor_portrait
              - studio.director_portrait · collezione.lead_image
        (2) 3 image cols inside dict rows (non-mutable lists):
              - home.signature.0.image (sample row 0)
              - territorio.territories.0.image
              - studio.advisors.0.portrait

        Per-row image override paths resolve to a spec with
        `type == "image"` via `get_field_spec`. This is the positive
        mirror of the Juris/Casa zero-image guards.
        """
        from apps.editor.schema import get_field_spec, get_list_shape
        arc = "ultra-luxury-cinematic"
        # (1) Scalar image fields
        scalar_image_paths = (
            "home.cover_image",
            "home.advisor_portrait",
            "studio.director_portrait",
            "collezione.lead_image",
        )
        for path in scalar_image_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"scalar image field {path} must be exposed")
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must carry type='image' (got {spec.get('type')!r})",
            )
        # (2) Image cols inside dict rows (baseline row 0 sample)
        image_cell_paths = (
            "home.signature.0.image",
            "territorio.territories.0.image",
            "studio.advisors.0.portrait",
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"image cell {path} must be reachable via get_field_spec",
            )
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} cell spec must carry type='image' (got {spec.get('type')!r})",
            )
        # (3) The dict shapes must ACTUALLY have the image col in their
        # cols list (shape-level check complementary to the cell-level
        # check above).
        for list_path, expected_col in (
            ("home.signature", "image"),
            ("territorio.territories", "image"),
            ("studio.advisors", "portrait"),
        ):
            shape = get_list_shape(arc, list_path)
            self.assertIsNotNone(shape)
            cols_by_name = {name: spec for name, spec in (shape.get("cols") or [])}
            self.assertIn(
                expected_col, cols_by_name,
                f"{list_path} shape cols must include image col {expected_col!r}",
            )
            self.assertEqual(
                cols_by_name[expected_col].get("type"), "image",
                f"{list_path}.{expected_col} col must be type='image'",
            )

    def test_a12b_villa_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL · complex-shape exclusion test.

        Four categories of complex registry shapes must stay OUT of
        Villa's editor perimeter (scope creep prevention):

        (1) Nested list-of-str inside dict rows:
              - `collezione.filter_groups[].options` (8 filter options
                per group)
              - `concierge.form_fields[].options` (4 form select
                options per field)
            Same exclusion policy as Juris `deliverables`.

        (2) Flat list-of-str containers:
              - `home.territory` (7 territory wordmarks)
              - `home.press_items` (5 press wordmarks)
              - `collezione.sort_options` (4 sort options)
              - `site.hours_footer_rows` / `site.offices_footer_rows`
                / `site.office_rows` (footer rows)
            Same policy as Juris `trust_logos`/`topics` and Casa
            `immobili.filters`/`sort_options`.

        (3) Form structure blocks:
              - `concierge.form_fields` list + its nested dict rows
            Same policy as every prior archetype.

        (4) Per-post `posts` entries (8 blog post records with image
            col). Stays registry-only — same policy as Lex notabili,
            Juris insights, Casa posts.

        Every path listed must fail `validate_key_path`.
        """
        from apps.editor.schema import validate_key_path
        arc = "ultra-luxury-cinematic"
        validate_rejects = [
            # (1) nested list-of-str inside dict rows
            "collezione.filter_groups.0.options",
            "collezione.filter_groups.0.options.0",
            "concierge.form_fields.0.options",
            "concierge.form_fields.0.options.0",
            # (2) flat list-of-str containers
            "home.territory",
            "home.territory.0",
            "home.press_items",
            "home.press_items.0",
            "collezione.sort_options",
            "collezione.sort_options.0",
            "site.hours_footer_rows",
            "site.offices_footer_rows",
            "site.office_rows",
            # (3) form structure blocks
            "concierge.form_fields",
            "concierge.form_fields.0.name",
            "concierge.form_fields.0.label",
            # (4) per-post posts entries (including post image col)
            "posts",
            "posts.0.title",
            "posts.0.image",
            "posts.0.body",
        ]
        for path in validate_rejects:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"{path} MUST be rejected by validate_key_path on ultra-luxury-cinematic",
            ):
                validate_key_path(arc, path)

    def test_a12b_villa_structured_list_cells_are_global(self):
        """The 14 readonly indexed lists on Villa stay global at cell
        level — text AND image cells both non-translatable (per-row
        image override is universal, never per-locale)."""
        from apps.editor.schema import is_translatable
        arc = "ultra-luxury-cinematic"
        cell_paths = (
            # text cells
            "home.signature.0.title",
            "home.signature.3.territorio",
            "home.hero_credit_cells.0.label",
            "home.numbers.0.label",
            "collezione.filter_groups.0.label",
            "territorio.territories.0.name",
            "territorio.territories.5.history",
            "studio.advisors.0.name",
            "studio.advisors.3.bio",
            "studio.press_items.0.magazine",
            "esperienza.process.4.title",
            "esperienza.faq_items.5.a",
            "concierge.offices.0.city",
            "concierge.offices.2.address",
            # image cells (per-row image override stays global too)
            "home.signature.0.image",
            "territorio.territories.0.image",
            "studio.advisors.0.portrait",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Villa",
            )

    def test_a12b_villa_supported_locales_returns_canonical_five(self):
        """Villa ships the canonical 5-locale set. Step-0 audit
        confirmed PERFECT parity (185 keys × 5 locales, zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("ultra-luxury-cinematic"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a12b_septuple_regression_after_villa_joins(self):
        """Regression guard: adding Villa to gate + schemas must not
        disturb ANY of the seven pre-existing enrollments (Vertex +
        Pragma + Gusto + specialist + classic-gold + modern-transparent
        + mass-market)."""
        from apps.editor.schema import is_translatable, supported_locales
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent", "mass-market"):
            self.assertTrue(
                is_translatable(arc, "home.headline"),
                f"{arc} home.headline must stay translatable",
            )
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must keep the canonical 5-locale set",
            )

    def test_a12b_villa_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8/A.9/A.10/A.11/A.12 integration guardrail —
        the Villa ``ultra-luxury-cinematic/_base.html`` must integrate
        the three bridge points together on the `.vp-*` skin:
        (1) preview-bridge.js conditional on ``preview_project``,
        (2) ``<title>`` honors ``site.logo_word``,
        (3) ``<body>`` carries the ``mw-is-editor-preview`` guard class
        when inside the editor."""
        villa = WebTemplate.objects.get(slug="villa-immobili-lusso")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/real-estate/villa-immobili-lusso/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=villa)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A12b Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/real-estate/villa-immobili-lusso/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A12b Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.13 · Chiara (editorial-designer-grid · portfolio family)
    # ------------------------------------------------------------------

    def test_a13_chiara_archetype_registered(self):
        """``editorial-designer-grid`` joins the schema + baseline +
        gate registries as 9th enrolled archetype, opening the portfolio
        family. Pixel (`cinematic-photographer`) stays explicitly OUT —
        guard mirror of the A.12 Villa-out pattern, will be removed in
        A.13b together with Pixel's own registrations.

        All 8 previous archetypes (incl. Casa + Villa from real-estate
        family closure) must remain enrolled — A.13 is additive.
        """
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("editorial-designer-grid", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["editorial-designer-grid"],
            ("chiara-portfolio-creativo", "it"),
        )
        self.assertIn("editorial-designer-grid", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("editorial-designer-grid"))
        # Pixel-out guard — explicit assertion that Pixel stays out
        # until A.13b. Removed in A.13b together with Pixel's own
        # registrations (registration-time + lifecycle runtime).
        self.assertNotIn("cinematic-photographer", _ARCHETYPE_SCHEMAS,
                         "Pixel must stay out of _ARCHETYPE_SCHEMAS until A.13b")
        self.assertNotIn("cinematic-photographer", _MULTILOCALE_ENABLED_ARCHETYPES,
                         "Pixel must stay out of _MULTILOCALE_ENABLED_ARCHETYPES until A.13b")
        # All 8 pre-existing archetypes still enrolled — A.13 is additive.
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent", "mass-market",
                    "ultra-luxury-cinematic"):
            self.assertIn(arc, _ARCHETYPE_SCHEMAS,
                          f"{arc} must remain enrolled after A.13 Chiara joins")
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} must keep multi-locale gate after A.13")

    def test_a13_chiara_schema_shape_covers_all_pages(self):
        """The Chiara schema must surface groups for every Chiara page
        slug (home + studio + lavoro + processo + contatti) plus
        chrome-level groups (page='*'). The novel `processo` page kind
        is just a string identifier — no view dispatch on it."""
        groups = iter_groups("editorial-designer-grid")
        self.assertGreaterEqual(len(groups), 8)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "studio", "lavoro", "processo", "contatti"):
            self.assertIn(slug, pages,
                          f"Chiara schema missing page slug {slug!r}")

    def test_a13_chiara_is_translatable_text_fields(self):
        """Scalar copy fields distributed across every Chiara page +
        chrome. Uses only paths present on Chiara so no sibling schema
        drifts into this test."""
        from apps.editor.schema import is_translatable
        arc = "editorial-designer-grid"
        distributed_paths = (
            # home hero + ledger
            "home.headline",
            "home.intro",
            "home.ledger_heading",
            "home.featured_works.heading",
            "home.commissions_heading",
            "home.cta_heading",
            # studio
            "studio.headline",
            "studio.founder.bio",
            "studio.team_intro",
            "studio.principles_intro",
            # lavoro
            "lavoro.headline",
            "lavoro.ledger_intro",
            "lavoro.cta_heading",
            # processo (novel page kind)
            "processo.headline",
            "processo.process_heading",
            "processo.capabilities_intro",
            # contatti
            "contatti.headline",
            "contatti.form_consent",
            "contatti.studio_address",
            "contatti.footnote",
            # chrome site.*
            "site.tag",
            "site.hours_compact",
            "site.footer_intro",
            "site.foot_studio",
            "site.foot_clients",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on editorial-designer-grid",
            )

    def test_a13_chiara_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Chiara — same
        contract as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "editorial-designer-grid"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Chiara",
            )

    def test_a13_chiara_image_cols_in_dict_shapes_exposed(self):
        """USER-IMPOSED GUARDRAIL · image cols are IN the perimeter
        (positive mirror of zero-image guards on Juris/Casa).

        Chiara is the THIRD precedent of image-in-dict-row exposure
        after Vertex `studio.partners[].portrait` (A.3a/A.4) and Villa
        `home.signature/territories/advisors[].image` (A.12b). Chiara's
        case has the additional novelty of a **deep path 2 levels**
        through the `home.featured_works` parent dict:
        `home.featured_works.items[].image`.

        Triple verification per user request:
          (1) Positive `get_field_spec` for the deep image path
          (2) Shape-level check: the image col exists in the cols
              list of the indexed shape
          (3) Plus the scalar nested-dict image
              `studio.founder.image` (Vertex `home.cover.image`
              precedent) returns spec with type=image.
        """
        from apps.editor.schema import get_field_spec, get_list_shape
        arc = "editorial-designer-grid"

        # (1) Scalar image field nested inside parent dict
        spec_founder = get_field_spec(arc, "studio.founder.image")
        self.assertIsNotNone(spec_founder,
                             "studio.founder.image must be reachable via get_field_spec")
        self.assertEqual(
            spec_founder.get("type"), "image",
            f"studio.founder.image must be type=image (got {spec_founder.get('type')!r})",
        )

        # (2) Image cell at deep path 2 levels (positive get_field_spec)
        deep_paths = (
            "home.featured_works.items.0.image",
            "home.featured_works.items.3.image",  # last row
        )
        for path in deep_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"deep image cell {path} must be reachable via get_field_spec",
            )
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} cell spec must be type=image (got {spec.get('type')!r})",
            )

        # (3) Shape-level check: the indexed list `home.featured_works.items`
        # exists in STRUCTURED_FIELD_SHAPES and includes the `image` col
        # in its cols list with type=image.
        shape = get_list_shape(arc, "home.featured_works.items")
        self.assertIsNotNone(
            shape,
            "home.featured_works.items shape must be registered in STRUCTURED_FIELD_SHAPES",
        )
        cols_by_name = {name: spec for name, spec in (shape.get("cols") or [])}
        self.assertIn(
            "image", cols_by_name,
            "home.featured_works.items cols must include image col",
        )
        self.assertEqual(
            cols_by_name["image"].get("type"), "image",
            "home.featured_works.items.image col must be type=image",
        )

    def test_a13_chiara_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL · complex-shape exclusion test.

        Five categories of complex registry shapes must stay OUT of
        Chiara's editor perimeter:

        (1) Per-project `posts` entries (3 project detail records,
            including `posts[].sections` rich nested body) — DETAIL-PAGE
            EDITING IS OUT OF A.13 SCOPE per the consistent perimeter
            policy applied to Lex `notabili` / Juris `insights` / Casa
            `posts` / Villa `posts`. This is a **coherent perimeter
            decision**, not a missing feature.
        (2) Nested list-of-str inside dict rows:
              - `studio.founder.credentials` (6 credentials list inside
                the founder dict)
              - `processo.capabilities_full[].scope` (capability scope
                bullets · same exclusion policy as Juris `deliverables`)
        (3) Flat list-of-str containers:
              - `home.clients` (8 client wordmarks · same as Juris
                `trust_logos` · Casa `popular_tags`)
              - `lavoro.filters` (6 filter pills · same as Casa
                `immobili.filters`)
        (4) Form structure blocks:
              - `contatti.form_fields` + `contatti.form_sections`
                + `contatti.upload_field`

        Every path listed must fail `validate_key_path`.
        """
        from apps.editor.schema import validate_key_path
        arc = "editorial-designer-grid"
        validate_rejects = [
            # (1) per-project posts entries (deep paths must reject)
            "posts",
            "posts.0.title",
            "posts.0.lead",
            "posts.0.sections",
            "posts.0.summary",
            "posts.0.deliverables",
            "posts.0.credits",
            "posts.2.next_label",
            # (2) nested list-of-str inside dict rows
            "studio.founder.credentials",
            "studio.founder.credentials.0",
            "processo.capabilities_full.0.scope",
            "processo.capabilities_full.0.scope.0",
            # (3) flat list-of-str containers
            "home.clients",
            "home.clients.0",
            "lavoro.filters",
            "lavoro.filters.0",
            # (4) form structure blocks
            "contatti.form_fields",
            "contatti.form_fields.0.name",
            "contatti.form_sections",
            "contatti.form_sections.0.title",
            "contatti.upload_field",
            "contatti.upload_field.label",
        ]
        for path in validate_rejects:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"{path} MUST be rejected by validate_key_path on editorial-designer-grid",
            ):
                validate_key_path(arc, path)

    def test_a13_chiara_structured_list_cells_are_global(self):
        """Text + image cells on Chiara's 11 readonly indexed lists
        stay global at cell level (image override stays universal,
        never per-locale)."""
        from apps.editor.schema import is_translatable
        arc = "editorial-designer-grid"
        cell_paths = (
            # text cells
            "home.ledger_rows.0.title",
            "home.ledger_rows.5.year",
            "home.capabilities.0.title",
            "home.commissions.2.blurb",
            "home.press.0.year",
            "home.press.2.honor",
            "studio.team.0.name",
            "studio.team.5.bio",
            "studio.principles.0.title",
            "studio.press_full.0.outlet",
            "studio.press_full.7.work",
            "processo.process.0.title",
            "processo.process.4.body",
            "processo.capabilities_full.0.title",
            "contatti.channels.0.label",
            # image cells (deep path 2 levels) — image overrides global too
            "home.featured_works.items.0.image",
            "home.featured_works.items.3.image",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Chiara",
            )

    def test_a13_chiara_supported_locales_returns_canonical_five(self):
        """Chiara ships the canonical 5-locale set. Step-0 audit
        confirmed PERFECT parity (164 keys × 5 locales · zero gaps)
        plus the Session 37 D-070 Chiara perfection pass already
        ships AR RTL CSS block + Amiri/Noto Kufi font load."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("editorial-designer-grid"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a13_octuple_regression_after_chiara_joins(self):
        """Regression guard: adding Chiara to gate + schemas must not
        disturb ANY of the eight pre-existing enrollments (Vertex +
        Pragma + Gusto + specialist + classic-gold + modern-transparent
        + mass-market + ultra-luxury-cinematic)."""
        from apps.editor.schema import is_translatable, supported_locales
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent", "mass-market",
                    "ultra-luxury-cinematic"):
            self.assertTrue(
                is_translatable(arc, "home.headline"),
                f"{arc} home.headline must stay translatable",
            )
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must keep the canonical 5-locale set",
            )

    def test_a13_chiara_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8/A.9/A.10/A.11/A.12/A.12b integration
        guardrail — the Chiara ``editorial-designer-grid/_base.html``
        must integrate the three bridge points together on the `.ed-*`
        skin: (1) preview-bridge.js conditional on ``preview_project``,
        (2) ``<title>`` honors ``site.logo_word``, (3) ``<body>``
        carries the ``mw-is-editor-preview`` guard class when inside
        the editor."""
        chiara = WebTemplate.objects.get(slug="chiara-portfolio-creativo")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/portfolio/chiara-portfolio-creativo/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=chiara)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A13 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/portfolio/chiara-portfolio-creativo/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A13 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    def test_a8_gusto_preview_bridge_injected_only_with_preview_project(self):
        """Guardrail user-imposed (A.8 Step 1 rifinitura): the Gusto
        `_base.html` must integrate three bridge points together:

        (1) preview-bridge.js injected ONLY when ``preview_project`` is
            set (inside the editor iframe) — never on the bare public
            preview;
        (2) ``<title>`` honors ``site.logo_word`` override via
            ``|default:brand.brand_name``;
        (3) ``<body>`` carries ``mw-is-editor-preview`` guard class
            whenever ``preview_project`` is truthy.

        This is the one test that locks the integration shape — any
        future regression that silently reverts any of the three points
        trips this guard instead of failing on a subtle browser walk.
        """
        gusto = WebTemplate.objects.get(slug="gusto-fine-dining")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/restaurant/gusto-fine-dining/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        # The guard CSS rules mention ``body.mw-is-editor-preview`` inside
        # <style>, which is fine. What must NOT happen: the <body> tag
        # itself carrying the class. Check the opening <body ...> span
        # specifically.
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=gusto)
        # Override logo_word so the title regression is measurable
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A8 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/restaurant/gusto-fine-dining/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        # (1) bridge injected
        self.assertIn("editor/preview-bridge.js", body_proj)
        # (2) title honours site.logo_word override
        self.assertIn("<title>A8 Bridge Check", body_proj)
        # (3) body guard class present
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

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
        self.assertEqual(supported_locales("trattoria-warm"), [])

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
        # sapore-trattoria-pizzeria (trattoria-warm archetype) is not yet
        # enrolled. Swap when that archetype receives editor support.
        r = self.client.get("/projects/start/?template=sapore-trattoria-pizzeria")
        self.assertEqual(r.status_code, 302)
        # Either /templates/restaurant/sapore-trattoria-pizzeria/ or template_list — both accept.
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

    # ------------------------------------------------------------------
    # A.7 · Step 4 — cross-cutting lifecycle + regression guard
    # ------------------------------------------------------------------

    def test_a7_step4_vertex_full_multilocale_lifecycle_end_to_end(self):
        """Single HTTP-level test locking the full customer path across
        five locales on Vertex:

        1. customer edits IT / EN / FR scalar translatable paths
        2. customer edits a global path (site.logo_word)
        3. unedited locales (ES · AR) must fall back to the authored
           registry — never to another locale's customer override
        4. project publishes · second user visits /preview/?lang=<code>
           for every locale and sees exactly what the first customer
           intended — zero cross-locale leak
        5. owner reopens ``/editor/?lang=<code>`` and the sidebar
           prefill matches the buffer for that locale.
        """
        import json as _json
        p = services.create_project_from_template(owner=self.owner, template=self.vertex)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global ──────────
        for locale, headline in (
            ("it", "Idee che <em>resistono</em> (IT)."),
            ("en", "Ideas that <em>endure</em> (EN)."),
            ("fr", "Des idées qui <em>durent</em> (FR)."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        r = autosave("en", {"site.logo_word": "A7Brand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # Storage keys check: three @<locale>:home.headline rows +
        # one plain site.logo_word row. No EN override bleeds into
        # an IT key or vice versa.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("home.headline", keys)       # no plain-key leak
        self.assertNotIn("@en:site.logo_word", keys)  # no global→locale leak

        # ── 3. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 4. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/agency/vertex-creative-agency/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render: IT override visible, EN/FR markers absent.
        body_it = preview_body("it")
        self.assertIn("resistono", body_it)
        self.assertNotIn("endure (EN)", body_it)
        self.assertNotIn("durent (FR)", body_it)
        self.assertIn("A7Brand", body_it)

        # EN render: EN override visible, IT/FR markers absent.
        body_en = preview_body("en")
        self.assertIn("endure", body_en)
        self.assertIn("Ideas that", body_en)
        self.assertNotIn("resistono (IT)", body_en)
        self.assertNotIn("durent (FR)", body_en)
        self.assertIn("A7Brand", body_en)

        # FR render: FR override visible.
        body_fr = preview_body("fr")
        self.assertIn("durent", body_fr)
        self.assertNotIn("resistono (IT)", body_fr)
        self.assertNotIn("endure (EN)", body_fr)
        self.assertIn("A7Brand", body_fr)

        # Unedited locales — must fall back to the authored registry
        # for the headline (no customer override leaks from IT/EN/FR)
        # while still picking up the GLOBAL logo override.
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("resistono (IT)", body)
            self.assertNotIn("endure (EN)", body)
            self.assertNotIn("durent (FR)", body)
            self.assertIn("A7Brand", body)
            # Authored registry for the unedited locale must be present.
            authored = (
                template_content.get_content(p.source_template.slug, locale) or {}
            )
            authored_headline_bits = authored.get("home", {}).get("headline") or ""
            # The authored headline may contain <em> tags; check a stable
            # substring by stripping them first.
            stable = authored_headline_bits.replace("<em>", "").replace("</em>", "")
            # Pick a stable word fragment that survives the skin's render.
            first_stable_word = stable.split()[0] if stable else ""
            if first_stable_word:
                self.assertIn(first_stable_word, body,
                              f"{locale} authored fallback not visible")

        # ── 5. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        for locale, expected_headline in (
            ("it", "resistono"),
            ("en", "Ideas that"),
            ("fr", "durent"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            hero = next(g for g in r.context["groups"] if g["id"] == "hero")
            headline_field = next(
                f for f in hero["fields"] if f["key"] == "home.headline"
            )
            self.assertIn(
                expected_headline, headline_field["value"],
                f"editor prefill for locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale (ES): no override → authored baseline prefill.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        hero_es = next(g for g in r_es.context["groups"] if g["id"] == "hero")
        headline_es = next(f for f in hero_es["fields"] if f["key"] == "home.headline")
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])
        # Global field is still overridden universally.
        brand_es = next(g for g in r_es.context["groups"] if g["id"] == "brand")
        logo_field = next(f for f in brand_es["fields"] if f["key"] == "site.logo_word")
        self.assertEqual(logo_field["value"], "A7Brand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

    # ------------------------------------------------------------------
    # A.7b · Step 1 — Pragma lifecycle HTTP cross-cutting
    # ------------------------------------------------------------------

    def test_a7b_pragma_full_multilocale_lifecycle_end_to_end(self):
        """Mirror of the Vertex Step-4 lifecycle, adapted to Pragma.

        1. customer edits IT / EN / FR on a Pragma translatable path
        2. customer edits a global path (site.logo_word)
        3. unedited locales (ES · AR) must fall back to the authored
           registry — NEVER to another locale's customer override
        4. project publishes · second user visits the public preview for
           every locale and sees exactly the right content
        5. owner reopens the editor on each locale and the sidebar
           prefill matches the buffer for that locale.

        Locks D-098 at HTTP layer on the second enrolled archetype.
        Also asserts ``<html dir="rtl">`` on the AR preview response so
        Step 2 browser walk doesn't have to rediscover the skin-level
        RTL contract.
        """
        import json as _json
        pragma = WebTemplate.objects.get(slug="pragma-corporate-suite")
        p = services.create_project_from_template(owner=self.owner, template=pragma)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global ──────────
        for locale, headline in (
            ("it", "Consulenza <em>che dura</em> (IT A7b)."),
            ("en", "Advisory that <em>endures</em> (EN A7b)."),
            ("fr", "Conseil qui <em>dure</em> (FR A7b)."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        # Global edit — note the client passes locale="en" on purpose:
        # the server must classify site.logo_word as global and ignore
        # the locale tag, persisting plain-keyed.
        r = autosave("en", {"site.logo_word": "A7bBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # Storage keys check: three @<locale>:home.headline rows + one
        # plain site.logo_word row. Gate holds at the write layer — no
        # EN override leaks into an IT key; no global→locale leak.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("home.headline", keys)       # no plain-key leak
        self.assertNotIn("@en:site.logo_word", keys)  # no global→locale leak

        # ── 3. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 4. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/business/pragma-corporate-suite/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore"), r

        # IT render: IT override visible, EN/FR markers absent.
        body_it, _ = preview_body("it")
        self.assertIn("Consulenza", body_it)
        self.assertIn("che dura", body_it)
        self.assertNotIn("endures (EN A7b)", body_it)
        self.assertNotIn("dure (FR A7b)", body_it)
        self.assertIn("A7bBrand", body_it)

        # EN render: EN override visible, IT/FR markers absent.
        body_en, _ = preview_body("en")
        self.assertIn("Advisory that", body_en)
        self.assertIn("endures", body_en)
        self.assertNotIn("Consulenza", body_en)
        self.assertNotIn("dure (FR A7b)", body_en)
        self.assertIn("A7bBrand", body_en)

        # FR render: FR override visible.
        body_fr, _ = preview_body("fr")
        self.assertIn("Conseil qui", body_fr)
        self.assertIn("dure", body_fr)
        self.assertNotIn("Consulenza", body_fr)
        self.assertNotIn("Advisory that", body_fr)
        self.assertIn("A7bBrand", body_fr)

        # Unedited locales — must fall back to the authored registry
        # (no customer headline leak from IT/EN/FR) while still
        # carrying the global logo override.
        for locale in ("es", "ar"):
            body, _ = preview_body(locale)
            self.assertNotIn("Consulenza", body)
            self.assertNotIn("Advisory that", body)
            self.assertNotIn("Conseil qui", body)
            self.assertIn("A7bBrand", body)
            # Authored registry for the unedited locale must flow
            # through. Pick a stable substring from the authored
            # headline (strip <em> tags first so it survives the skin).
            from apps.catalog import template_content as _tc
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Pragma",
                )

        # AR preview — the skin must render the RTL document direction
        # so the Step 2 browser walk inherits a green baseline for RTL.
        body_ar, _ = preview_body("ar")
        self.assertIn('dir="rtl"', body_ar)

        # ── 5. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_headline_field(groups):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == "home.headline":
                        return f
            self.fail("home.headline field missing from Pragma editor groups")

        for locale, expected_substring in (
            ("it", "che dura"),
            ("en", "Advisory that"),
            ("fr", "Conseil qui"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            self.assertEqual(
                r.context["supported_locales"],
                ["it", "en", "fr", "es", "ar"],
            )
            headline_field = find_headline_field(r.context["groups"])
            self.assertIn(
                expected_substring, headline_field["value"],
                f"editor prefill for locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale (ES): no override → authored baseline prefill.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        headline_es = find_headline_field(r_es.context["groups"])
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])
        # Global field: overridden universally across all locales, not
        # translatable (same contract as Vertex).
        logo_field = None
        for g in r_es.context["groups"]:
            for f in g["fields"]:
                if f["key"] == "site.logo_word":
                    logo_field = f
                    break
        self.assertIsNotNone(logo_field, "site.logo_word missing from Pragma editor")
        self.assertEqual(logo_field["value"], "A7bBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

    # ------------------------------------------------------------------
    # A.8 · Step 2 — Gusto lifecycle HTTP cross-cutting
    # ------------------------------------------------------------------

    def test_a8_gusto_full_multilocale_lifecycle_end_to_end(self):
        """Mirror of the A.7b Pragma lifecycle, adapted to Gusto on the
        new ``fine-dining`` archetype.

        1. customer edits IT / EN / FR on a Gusto translatable path
        2. customer edits a global path (site.logo_word)
        3. unedited locales (ES · AR) fall back to the authored registry —
           NEVER to another locale's customer override
        4. project publishes · second user visits every public preview
           locale and sees the correct content
        5. owner reopens the editor per locale and the sidebar prefill
           matches the buffer for that locale.

        Also asserts ``<html dir="rtl">`` on the AR preview HEAD so
        Step 3 browser walk inherits a green baseline for RTL rendering
        on the ``.fd-*`` skin. Vertex + Pragma regression is implicit
        via the full suite staying green.
        """
        import json as _json
        gusto = WebTemplate.objects.get(slug="gusto-fine-dining")
        p = services.create_project_from_template(owner=self.owner, template=gusto)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global ──────────
        for locale, headline in (
            ("it", "Una cena <em>che dura</em> (IT A8)."),
            ("en", "A dinner that <em>endures</em> (EN A8)."),
            ("fr", "Un dîner qui <em>dure</em> (FR A8)."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        # Global edit — the client passes locale="en" on purpose: the
        # server must classify site.logo_word as global and ignore the
        # locale tag, persisting plain-keyed.
        r = autosave("en", {"site.logo_word": "A8GustoBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # Storage keys check: three @<locale>:home.headline rows + one
        # plain site.logo_word row. Gate holds at the write layer.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("home.headline", keys)       # no plain-key leak
        self.assertNotIn("@en:site.logo_word", keys)  # no global→locale leak

        # ── 3. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 4. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/restaurant/gusto-fine-dining/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render: IT override visible, EN/FR markers absent.
        body_it = preview_body("it")
        self.assertIn("che dura", body_it)
        self.assertIn("Una cena", body_it)
        self.assertNotIn("endures (EN A8)", body_it)
        self.assertNotIn("dure (FR A8)", body_it)
        self.assertIn("A8GustoBrand", body_it)

        # EN render: EN override visible, IT/FR markers absent.
        body_en = preview_body("en")
        self.assertIn("A dinner that", body_en)
        self.assertIn("endures", body_en)
        self.assertNotIn("Una cena", body_en)
        self.assertNotIn("dure (FR A8)", body_en)
        self.assertIn("A8GustoBrand", body_en)

        # FR render: FR override visible.
        body_fr = preview_body("fr")
        self.assertIn("Un dîner qui", body_fr)
        self.assertIn("dure", body_fr)
        self.assertNotIn("Una cena", body_fr)
        self.assertNotIn("A dinner that", body_fr)
        self.assertIn("A8GustoBrand", body_fr)

        # Unedited locales — must fall back to the authored registry
        # (no customer headline leak from IT/EN/FR) while still
        # carrying the global logo override.
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Una cena", body)
            self.assertNotIn("A dinner that", body)
            self.assertNotIn("Un dîner qui", body)
            self.assertIn("A8GustoBrand", body)
            # Authored registry for the unedited locale must flow through.
            from apps.catalog import template_content as _tc
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Gusto",
                )

        # AR preview — the ``.fd-*`` skin must emit ``<html dir="rtl">``
        # on the document root so RTL rendering works inside the editor
        # iframe. Pillow check on the opening <html ...> tag only, to
        # avoid matching pill-level ``dir="rtl"`` on language switchers.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 5. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_headline_field(groups):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == "home.headline":
                        return f
            self.fail("home.headline field missing from Gusto editor groups")

        for locale, expected_substring in (
            ("it", "che dura"),
            ("en", "A dinner that"),
            ("fr", "Un dîner qui"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            self.assertEqual(
                r.context["supported_locales"],
                ["it", "en", "fr", "es", "ar"],
            )
            headline_field = find_headline_field(r.context["groups"])
            self.assertIn(
                expected_substring, headline_field["value"],
                f"editor prefill for locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale (ES): no override → authored baseline prefill.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        headline_es = find_headline_field(r_es.context["groups"])
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])
        # Global field: overridden universally, not translatable — same
        # contract as Vertex + Pragma.
        logo_field = None
        for g in r_es.context["groups"]:
            for f in g["fields"]:
                if f["key"] == "site.logo_word":
                    logo_field = f
                    break
        self.assertIsNotNone(logo_field, "site.logo_word missing from Gusto editor")
        self.assertEqual(logo_field["value"], "A8GustoBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

    # ------------------------------------------------------------------
    # A.9 · Step 2 — Cardio + Derm lifecycle HTTP cross-cutting
    # ------------------------------------------------------------------
    #
    # Two distinct tests — one per specialist-archetype template — so a
    # regression that hits Cardio but not Derm (or vice versa) surfaces
    # with a clean name. Both use the shared helper _run_specialist_lifecycle
    # to avoid duplicating 180 LOC of assertions.

    def _run_specialist_lifecycle(self, template_slug, marker, brand):
        """Shared body for Cardio + Derm lifecycle tests.

        ``marker`` goes into the IT/EN/FR headline overrides so the
        cross-locale-leak assertions can distinguish the two flows when
        a test run persists across both.
        ``brand`` is the global logo override — verified universal
        across all 5 public preview locales.
        """
        import json as _json
        tmpl = WebTemplate.objects.get(slug=template_slug)
        p = services.create_project_from_template(owner=self.owner, template=tmpl)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global ──────────
        for locale, headline in (
            ("it", f"Una clinica <em>che ascolta</em> ({marker} IT)."),
            ("en", f"A clinic that <em>listens</em> ({marker} EN)."),
            ("fr", f"Une clinique qui <em>écoute</em> ({marker} FR)."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        r = autosave("en", {"site.logo_word": brand})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("home.headline", keys)       # no plain-key leak
        self.assertNotIn("@en:site.logo_word", keys)  # no global→locale leak

        # ── 3. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 4. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/medical/{template_slug}/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render — IT override visible, EN/FR markers absent.
        body_it = preview_body("it")
        self.assertIn("che ascolta", body_it)
        self.assertIn(f"({marker} IT)", body_it)
        self.assertNotIn(f"({marker} EN)", body_it)
        self.assertNotIn(f"({marker} FR)", body_it)
        self.assertIn(brand, body_it)

        # EN render — EN override visible, IT/FR markers absent.
        body_en = preview_body("en")
        self.assertIn("listens", body_en)
        self.assertIn(f"({marker} EN)", body_en)
        self.assertNotIn(f"({marker} IT)", body_en)
        self.assertNotIn(f"({marker} FR)", body_en)
        self.assertIn(brand, body_en)

        # FR render — FR override visible, IT/EN markers absent.
        body_fr = preview_body("fr")
        self.assertIn("écoute", body_fr)
        self.assertIn(f"({marker} FR)", body_fr)
        self.assertNotIn(f"({marker} IT)", body_fr)
        self.assertNotIn(f"({marker} EN)", body_fr)
        self.assertIn(brand, body_fr)

        # Unedited locales — authored fallback + global logo visible.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn(f"({marker} IT)", body)
            self.assertNotIn(f"({marker} EN)", body)
            self.assertNotIn(f"({marker} FR)", body)
            self.assertIn(brand, body)
            authored = _tc.get_content(template_slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on {template_slug}",
                )

        # AR preview — `.sp-*` skin must render `<html dir="rtl" lang="ar">`.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 5. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_headline_field(groups):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == "home.headline":
                        return f
            self.fail(f"home.headline missing from {template_slug} editor groups")

        for locale, expected_substring in (
            ("it", f"({marker} IT)"),
            ("en", f"({marker} EN)"),
            ("fr", f"({marker} FR)"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            self.assertEqual(
                r.context["supported_locales"],
                ["it", "en", "fr", "es", "ar"],
            )
            headline_field = find_headline_field(r.context["groups"])
            self.assertIn(
                expected_substring, headline_field["value"],
                f"editor prefill {template_slug} locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale ES: authored baseline prefill, is_overridden=False.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        headline_es = find_headline_field(r_es.context["groups"])
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])
        # Global field stays overridden universally.
        logo_field = None
        for g in r_es.context["groups"]:
            for f in g["fields"]:
                if f["key"] == "site.logo_word":
                    logo_field = f
                    break
        self.assertIsNotNone(
            logo_field, f"site.logo_word missing from {template_slug} editor",
        )
        self.assertEqual(logo_field["value"], brand)
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

    def test_a9_cardio_full_multilocale_lifecycle_end_to_end(self):
        """Lifecycle HTTP cross-cutting on Cardio — first of the two
        specialist templates. Distinct marker + brand so a regression
        test running both back-to-back keeps the diagnostic surface
        isolated per template."""
        self._run_specialist_lifecycle(
            template_slug="cardio-studio-specialistico",
            marker="A9Cardio",
            brand="A9CardioBrand",
        )

    def test_a9_derm_full_multilocale_lifecycle_end_to_end(self):
        """Lifecycle HTTP cross-cutting on Derm — second template of the
        shared specialist archetype. Proves one schema registers both
        templates editable end-to-end without per-template branching."""
        self._run_specialist_lifecycle(
            template_slug="dermatologia-elite-roma",
            marker="A9Derm",
            brand="A9DermBrand",
        )

    # ------------------------------------------------------------------
    # A.10 · Step 2 — Lex (classic-gold) lifecycle HTTP cross-cutting
    # ------------------------------------------------------------------

    def test_a10_lex_full_multilocale_lifecycle_end_to_end(self):
        """Mirror of the A.7b Pragma / A.8 Gusto / A.9 specialist-single
        lifecycle, adapted to Lex (classic-gold archetype · law family).

        1. customer edits IT / EN / FR on a Lex translatable path
        2. customer edits a global path (site.logo_word)
        3. unedited locales (ES · AR) fall back to the authored registry —
           NEVER to another locale's customer override
        4. project publishes · second user visits every public preview
           locale and sees the correct content
        5. owner reopens the editor per locale and the sidebar prefill
           matches the buffer for that locale.

        AR response head must carry ``<html dir="rtl" lang="ar">`` so the
        Step 3 browser walk inherits a green baseline for RTL on the
        ``.lx-*`` skin. Juris (modern-transparent) is NOT exercised
        here — it belongs to A.10b.
        """
        import json as _json
        lex = WebTemplate.objects.get(slug="lex-studio-legale")
        p = services.create_project_from_template(owner=self.owner, template=lex)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global ──────────
        for locale, headline in (
            ("it", "Uno studio <em>di lungo corso</em> (A10Lex IT)."),
            ("en", "A firm <em>built to endure</em> (A10Lex EN)."),
            ("fr", "Un cabinet <em>qui dure</em> (A10Lex FR)."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        # Global edit — locale tag on the request is ignored because
        # site.logo_word is classified global.
        r = autosave("en", {"site.logo_word": "A10LexBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # Storage keys: three @<locale>:home.headline + one plain
        # site.logo_word. No plain-key leak, no global→locale leak.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)

        # ── 3. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 4. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/lawyer/lex-studio-legale/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render — IT override visible, EN/FR markers absent.
        body_it = preview_body("it")
        self.assertIn("di lungo corso", body_it)
        self.assertIn("(A10Lex IT)", body_it)
        self.assertNotIn("(A10Lex EN)", body_it)
        self.assertNotIn("(A10Lex FR)", body_it)
        self.assertIn("A10LexBrand", body_it)

        # EN render — EN override visible, IT/FR markers absent.
        body_en = preview_body("en")
        self.assertIn("built to endure", body_en)
        self.assertIn("(A10Lex EN)", body_en)
        self.assertNotIn("(A10Lex IT)", body_en)
        self.assertNotIn("(A10Lex FR)", body_en)
        self.assertIn("A10LexBrand", body_en)

        # FR render — FR override visible.
        body_fr = preview_body("fr")
        self.assertIn("qui dure", body_fr)
        self.assertIn("(A10Lex FR)", body_fr)
        self.assertNotIn("(A10Lex IT)", body_fr)
        self.assertNotIn("(A10Lex EN)", body_fr)
        self.assertIn("A10LexBrand", body_fr)

        # Unedited locales — authored fallback + global logo universal.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("(A10Lex IT)", body)
            self.assertNotIn("(A10Lex EN)", body)
            self.assertNotIn("(A10Lex FR)", body)
            self.assertIn("A10LexBrand", body)
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Lex",
                )

        # AR preview — `.lx-*` skin must emit ``<html dir="rtl" lang="ar">``.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 5. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_headline_field(groups):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == "home.headline":
                        return f
            self.fail("home.headline field missing from Lex editor groups")

        for locale, expected_substring in (
            ("it", "di lungo corso"),
            ("en", "built to endure"),
            ("fr", "qui dure"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            self.assertEqual(
                r.context["supported_locales"],
                ["it", "en", "fr", "es", "ar"],
            )
            headline_field = find_headline_field(r.context["groups"])
            self.assertIn(
                expected_substring, headline_field["value"],
                f"editor prefill for locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale (ES): no override → authored baseline prefill.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        headline_es = find_headline_field(r_es.context["groups"])
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])
        # Global field: overridden universally, not translatable.
        logo_field = None
        for g in r_es.context["groups"]:
            for f in g["fields"]:
                if f["key"] == "site.logo_word":
                    logo_field = f
                    break
        self.assertIsNotNone(logo_field, "site.logo_word missing from Lex editor")
        self.assertEqual(logo_field["value"], "A10LexBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

    # ------------------------------------------------------------------
    # A.11 · Step 2 — Juris (modern-transparent) lifecycle HTTP cross-cutting
    # ------------------------------------------------------------------

    def test_a11_juris_full_multilocale_lifecycle_end_to_end(self):
        """Mirror of the A.7b Pragma / A.8 Gusto / A.9 specialist-single /
        A.10 Lex lifecycle, adapted to Juris (modern-transparent archetype
        · second template of the law family).

        1. customer edits IT / EN / FR on a Juris translatable path
        2. customer edits a global path (site.logo_word)
        3. unedited locales (ES · AR) fall back to the authored registry —
           NEVER to another locale's customer override
        4. project publishes · second user visits every public preview
           locale and sees the correct content
        5. owner reopens the editor per locale and the sidebar prefill
           matches the buffer for that locale.

        AR response head must carry ``<html dir="rtl" lang="ar">`` so the
        ``.jr-*`` skin inherits a green baseline for RTL. Lex
        (classic-gold) is NOT re-exercised here — the A.10 lifecycle test
        already covers it.
        """
        import json as _json
        juris = WebTemplate.objects.get(slug="juris-avvocato-moderno")
        p = services.create_project_from_template(owner=self.owner, template=juris)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global ──────────
        for locale, headline in (
            ("it", "Il diritto, <em>dalla tua parte</em> (A11Juris IT)."),
            ("en", "The law, <em>on your side</em> (A11Juris EN)."),
            ("fr", "Le droit, <em>de votre côté</em> (A11Juris FR)."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        # Global edit — locale tag on the request is ignored because
        # site.logo_word is classified global.
        r = autosave("en", {"site.logo_word": "A11JurisBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # Storage keys: three @<locale>:home.headline + one plain
        # site.logo_word. No plain-key leak, no global→locale leak.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)

        # ── 3. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 4. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/lawyer/juris-avvocato-moderno/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render — IT override visible, EN/FR markers absent.
        body_it = preview_body("it")
        self.assertIn("dalla tua parte", body_it)
        self.assertIn("(A11Juris IT)", body_it)
        self.assertNotIn("(A11Juris EN)", body_it)
        self.assertNotIn("(A11Juris FR)", body_it)
        self.assertIn("A11JurisBrand", body_it)

        # EN render — EN override visible, IT/FR markers absent.
        body_en = preview_body("en")
        self.assertIn("on your side", body_en)
        self.assertIn("(A11Juris EN)", body_en)
        self.assertNotIn("(A11Juris IT)", body_en)
        self.assertNotIn("(A11Juris FR)", body_en)
        self.assertIn("A11JurisBrand", body_en)

        # FR render — FR override visible.
        body_fr = preview_body("fr")
        self.assertIn("de votre côté", body_fr)
        self.assertIn("(A11Juris FR)", body_fr)
        self.assertNotIn("(A11Juris IT)", body_fr)
        self.assertNotIn("(A11Juris EN)", body_fr)
        self.assertIn("A11JurisBrand", body_fr)

        # Unedited locales — authored fallback + global logo universal.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("(A11Juris IT)", body)
            self.assertNotIn("(A11Juris EN)", body)
            self.assertNotIn("(A11Juris FR)", body)
            self.assertIn("A11JurisBrand", body)
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Juris",
                )

        # AR preview — `.jr-*` skin must emit ``<html dir="rtl" lang="ar">``.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 5. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_headline_field(groups):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == "home.headline":
                        return f
            self.fail("home.headline field missing from Juris editor groups")

        for locale, expected_substring in (
            ("it", "dalla tua parte"),
            ("en", "on your side"),
            ("fr", "de votre côté"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            self.assertEqual(
                r.context["supported_locales"],
                ["it", "en", "fr", "es", "ar"],
            )
            headline_field = find_headline_field(r.context["groups"])
            self.assertIn(
                expected_substring, headline_field["value"],
                f"editor prefill for locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale (ES): no override → authored baseline prefill.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        headline_es = find_headline_field(r_es.context["groups"])
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])
        # Global field: overridden universally, not translatable.
        logo_field = None
        for g in r_es.context["groups"]:
            for f in g["fields"]:
                if f["key"] == "site.logo_word":
                    logo_field = f
                    break
        self.assertIsNotNone(logo_field, "site.logo_word missing from Juris editor")
        self.assertEqual(logo_field["value"], "A11JurisBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

    # ------------------------------------------------------------------
    # A.12 · Step 2 — Casa (mass-market) lifecycle HTTP cross-cutting
    # ------------------------------------------------------------------

    def test_a12_casa_full_multilocale_lifecycle_end_to_end(self):
        """Mirror of the A.7b Pragma / A.8 Gusto / A.9 specialist-single /
        A.10 Lex / A.11 Juris lifecycle, adapted to Casa (mass-market
        archetype · first template of the real-estate family).

        1. customer edits IT / EN / FR on a Casa translatable path
        2. customer edits a global path (site.logo_word)
        3. unedited locales (ES · AR) fall back to the authored registry —
           NEVER to another locale's customer override
        4. project publishes · second user visits every public preview
           locale and sees the correct content
        5. owner reopens the editor per locale and the sidebar prefill
           matches the buffer for that locale.

        AR response head must carry ``<html dir="rtl" lang="ar">`` so the
        ``.dm-*`` skin inherits a green baseline for RTL. Villa
        (ultra-luxury-cinematic) has joined the gate in A.12b; the
        runtime Villa-out assertion that used to live here has been
        removed now that Villa is enrolled with its own lifecycle test.
        """
        import json as _json

        casa = WebTemplate.objects.get(slug="casa-agenzia-immobiliare")
        p = services.create_project_from_template(owner=self.owner, template=casa)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global ──────────
        for locale, headline in (
            ("it", "La casa <em>giusta</em> (A12Casa IT)."),
            ("en", "The home <em>that fits</em> (A12Casa EN)."),
            ("fr", "La maison <em>qui vous ressemble</em> (A12Casa FR)."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        # Global edit — locale tag on the request is ignored because
        # site.logo_word is classified global.
        r = autosave("en", {"site.logo_word": "A12CasaBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # Storage keys: three @<locale>:home.headline + one plain
        # site.logo_word. No plain-key leak, no global→locale leak.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)

        # ── 3. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 4. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/real-estate/casa-agenzia-immobiliare/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render — IT override visible, EN/FR markers absent.
        body_it = preview_body("it")
        self.assertIn("casa <em>giusta</em>", body_it)
        self.assertIn("(A12Casa IT)", body_it)
        self.assertNotIn("(A12Casa EN)", body_it)
        self.assertNotIn("(A12Casa FR)", body_it)
        self.assertIn("A12CasaBrand", body_it)

        # EN render — EN override visible, IT/FR markers absent.
        body_en = preview_body("en")
        self.assertIn("that fits", body_en)
        self.assertIn("(A12Casa EN)", body_en)
        self.assertNotIn("(A12Casa IT)", body_en)
        self.assertNotIn("(A12Casa FR)", body_en)
        self.assertIn("A12CasaBrand", body_en)

        # FR render — FR override visible.
        body_fr = preview_body("fr")
        self.assertIn("qui vous ressemble", body_fr)
        self.assertIn("(A12Casa FR)", body_fr)
        self.assertNotIn("(A12Casa IT)", body_fr)
        self.assertNotIn("(A12Casa EN)", body_fr)
        self.assertIn("A12CasaBrand", body_fr)

        # Unedited locales — authored fallback + global logo universal.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("(A12Casa IT)", body)
            self.assertNotIn("(A12Casa EN)", body)
            self.assertNotIn("(A12Casa FR)", body)
            self.assertIn("A12CasaBrand", body)
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Casa",
                )

        # AR preview — `.dm-*` skin must emit ``<html dir="rtl" lang="ar">``.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 5. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_headline_field(groups):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == "home.headline":
                        return f
            self.fail("home.headline field missing from Casa editor groups")

        for locale, expected_substring in (
            ("it", "giusta"),
            ("en", "that fits"),
            ("fr", "qui vous ressemble"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            self.assertEqual(
                r.context["supported_locales"],
                ["it", "en", "fr", "es", "ar"],
            )
            headline_field = find_headline_field(r.context["groups"])
            self.assertIn(
                expected_substring, headline_field["value"],
                f"editor prefill for locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale (ES): no override → authored baseline prefill.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        headline_es = find_headline_field(r_es.context["groups"])
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])
        # Global field: overridden universally, not translatable.
        logo_field = None
        for g in r_es.context["groups"]:
            for f in g["fields"]:
                if f["key"] == "site.logo_word":
                    logo_field = f
                    break
        self.assertIsNotNone(logo_field, "site.logo_word missing from Casa editor")
        self.assertEqual(logo_field["value"], "A12CasaBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

    # ------------------------------------------------------------------
    # A.12b · Step 2 — Villa (ultra-luxury-cinematic) lifecycle HTTP
    # cross-cutting · includes scalar image override + image-in-dict-row
    # override coverage (Villa is the second archetype to expose image
    # cols inside dict rows, after Vertex studio.partners.portrait).
    # ------------------------------------------------------------------

    def test_a12b_villa_full_multilocale_lifecycle_end_to_end(self):
        """Mirror of the A.12 Casa lifecycle, enriched to cover Villa's
        image-handling surface:

        1. customer edits IT / EN / FR on a Villa translatable path
        2. customer edits a global TEXT path (site.logo_word)
        3. customer edits a SCALAR IMAGE field (home.cover_image)
        4. customer edits an IMAGE CELL inside a dict row
           (home.signature.0.image) — this is the A.12b-specific
           surface that mirrors Vertex studio.partners[].portrait
        5. unedited locales (ES · AR) fall back to the authored registry
        6. project publishes · second user visits every public preview
           locale and sees the correct content
        7. owner reopens the editor per locale and the sidebar prefill
           matches the buffer for that locale — translatable (per-locale)
           AND image overrides (plain-keyed, universal).

        AR response head must carry ``<html dir="rtl" lang="ar">`` on
        the `.vp-*` skin. **Casa (mass-market) must remain enrolled +
        intact** throughout — asserted at the start as a runtime guard.
        """
        import json as _json
        from apps.editor.schema import _MULTILOCALE_ENABLED_ARCHETYPES

        # Casa guard — must stay enrolled throughout A.12b.
        self.assertIn("mass-market", _MULTILOCALE_ENABLED_ARCHETYPES,
                      "Casa must remain enrolled during A.12b lifecycle")

        villa = WebTemplate.objects.get(slug="villa-immobili-lusso")
        p = services.create_project_from_template(owner=self.owner, template=villa)

        def autosave(locale, content, tokens=None):
            return self.client.post(
                f"/projects/{p.uuid}/autosave/",
                data=_json.dumps({
                    "locale": locale,
                    "content": content,
                    "tokens": tokens or {},
                }),
                content_type="application/json",
            )

        # ── 1-2. three translatable locales + one global text ─────
        for locale, headline in (
            ("it", "Dimore Villa walk IT <em>A12bVilla</em>."),
            ("en", "Signature Villa walk EN <em>A12bVillaEN</em>."),
            ("fr", "Demeures Villa walk FR <em>A12bVillaFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        r = autosave("en", {"site.logo_word": "A12bVillaBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 3. Scalar image override (home.cover_image) ───────────
        # Image fields are classified NON-translatable (type != text/
        # textarea/richtext) so the override is persisted with a plain
        # key regardless of the locale on the request.
        IMG_COVER = "https://images.pexels.com/photos/9999001/cover-A12b.jpg"
        r = autosave("it", {"home.cover_image": IMG_COVER})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.cover_image", r.json()["content_keys"])

        # ── 4. Image cell inside dict row (home.signature.0.image) ─
        # This is the A.12b-specific coverage: image col inside a
        # list-of-dict row. Same widget infra as Vertex
        # studio.partners[].portrait, production since A.3a/A.4.
        IMG_SIG = "https://images.pexels.com/photos/9999002/signature-row0.jpg"
        r = autosave("it", {"home.signature.0.image": IMG_SIG})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.signature.0.image", r.json()["content_keys"])

        # Storage keys: three @<locale>:home.headline (per-locale) +
        # three plain-keyed globals (logo + 2 images). No leak of image
        # overrides into @<locale>: namespace · no plain-key leak for
        # home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("home.cover_image", keys)
        self.assertIn("home.signature.0.image", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@it:home.cover_image", keys)
        self.assertNotIn("@it:home.signature.0.image", keys)
        self.assertNotIn("@en:site.logo_word", keys)

        # ── 5. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 6. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale):
            url = (
                f"/templates/real-estate/villa-immobili-lusso/preview/"
                f"?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render — IT override visible, EN/FR markers absent.
        body_it = preview_body("it")
        self.assertIn("Villa walk IT", body_it)
        self.assertIn("A12bVilla", body_it)
        self.assertNotIn("A12bVillaEN", body_it)
        self.assertNotIn("A12bVillaFR", body_it)
        self.assertIn("A12bVillaBrand", body_it)
        # Image overrides are universal — both must appear in IT render.
        self.assertIn(IMG_COVER, body_it)
        self.assertIn(IMG_SIG, body_it)

        # EN render
        body_en = preview_body("en")
        self.assertIn("Villa walk EN", body_en)
        self.assertIn("A12bVillaEN", body_en)
        self.assertNotIn("Villa walk IT", body_en)
        self.assertIn("A12bVillaBrand", body_en)
        self.assertIn(IMG_COVER, body_en)
        self.assertIn(IMG_SIG, body_en)

        # FR render
        body_fr = preview_body("fr")
        self.assertIn("Villa walk FR", body_fr)
        self.assertIn("A12bVillaFR", body_fr)
        self.assertIn("A12bVillaBrand", body_fr)
        self.assertIn(IMG_COVER, body_fr)
        self.assertIn(IMG_SIG, body_fr)

        # Unedited locales — authored text fallback + global images universal.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Villa walk IT", body)
            self.assertNotIn("Villa walk EN", body)
            self.assertNotIn("Villa walk FR", body)
            self.assertIn("A12bVillaBrand", body)
            # Image overrides must still appear (global · universal).
            self.assertIn(IMG_COVER, body)
            self.assertIn(IMG_SIG, body)
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Villa",
                )

        # AR preview — `.vp-*` skin must emit ``<html dir="rtl" lang="ar">``.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 7. owner reopens the editor on each locale ────────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Villa walk IT"),
            ("en", "Villa walk EN"),
            ("fr", "Villa walk FR"),
        ):
            r = self.client.get(f"/projects/{p.uuid}/editor/?lang={locale}")
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.context["active_locale"], locale)
            self.assertEqual(
                r.context["supported_locales"],
                ["it", "en", "fr", "es", "ar"],
            )
            headline_field = find_field_by_key(r.context["groups"], "home.headline")
            self.assertIsNotNone(headline_field)
            self.assertIn(
                expected_substring, headline_field["value"],
                f"editor prefill for locale={locale} missed expected text",
            )
            self.assertTrue(headline_field["is_overridden"])
            self.assertTrue(headline_field["translatable"])

        # Unedited locale (ES): no override → authored baseline prefill.
        r_es = self.client.get(f"/projects/{p.uuid}/editor/?lang=es")
        self.assertEqual(r_es.context["active_locale"], "es")
        headline_es = find_field_by_key(r_es.context["groups"], "home.headline")
        self.assertIsNotNone(headline_es)
        self.assertFalse(headline_es["is_overridden"])
        self.assertTrue(headline_es["translatable"])

        # Global text field: overridden universally, not translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Villa editor")
        self.assertEqual(logo_field["value"], "A12bVillaBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        # Scalar image field: overridden universally, not translatable.
        cover_field = find_field_by_key(r_es.context["groups"], "home.cover_image")
        self.assertIsNotNone(cover_field, "home.cover_image missing from Villa editor")
        self.assertEqual(cover_field["value"], IMG_COVER)
        self.assertTrue(cover_field["is_overridden"])
        self.assertFalse(cover_field["translatable"])

        # Casa guard (re-check end-of-test) — must still be enrolled.
        self.assertIn("mass-market", _MULTILOCALE_ENABLED_ARCHETYPES,
                      "Casa enrollment must persist past Villa lifecycle")

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
