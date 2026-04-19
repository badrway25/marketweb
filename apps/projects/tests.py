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
        # `startup-saas-landing` (Elevate) has not been enrolled in
        # _ARCHETYPE_SCHEMAS yet — Elevate still hits the
        # UnsupportedTemplate guard. A.17 rotated the outside-gate
        # reference from Aura (agency-digital-studio · now enrolled ·
        # CLOSES agency-secondary family) to Elevate (startup-saas-
        # landing · still out). Elevate is the LAST non-enrolled
        # archetype — A.17b will close startup-saas family with a
        # single-template phase and retire this gate altogether.
        # Swap this slug when `startup-saas-landing` receives editor
        # support (or migrate this test to a null-slug sentinel once
        # the catalog reaches 20/20 enrolled).
        elevate = WebTemplate.objects.get(slug="elevate-startup-landing")
        with self.assertRaises(services.UnsupportedTemplate):
            services.create_project_from_template(owner=self.owner, template=elevate)

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
        # `startup-saas-landing` (Elevate) is the current outside-gate
        # reference (A.17 rotated it from `agency-digital-studio`/Aura
        # which is now enrolled · CLOSES agency-secondary family).
        self.assertFalse(is_supported_archetype("startup-saas-landing"))

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
        # `startup-saas-landing` (Elevate) is the current outside-gate
        # reference (A.17 rotated it from `agency-digital-studio`/Aura
        # which is now enrolled · CLOSES agency-secondary family).
        self.assertFalse(is_translatable("startup-saas-landing", "home.headline"))
        self.assertEqual(supported_locales("startup-saas-landing"), [])

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
        family. (Pixel `cinematic-photographer` was the A.13b phase;
        that test lives below.)

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

    # ------------------------------------------------------------------
    # A.13b · Pixel (cinematic-photographer · portfolio family)
    # ------------------------------------------------------------------

    def test_a13b_pixel_archetype_registered(self):
        """``cinematic-photographer`` joins the schema + baseline +
        gate registries as 10th enrolled archetype, closing the
        portfolio family opened in A.13 with Chiara. Same staged
        dedicated-schema progression pattern as real-estate
        (A.12+A.12b). Chiara (`editorial-designer-grid`) must stay
        enrolled — A.13b is additive.
        """
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("cinematic-photographer", _ARCHETYPE_SCHEMAS)
        self.assertEqual(
            _ARCHETYPE_BASELINE_TEMPLATE["cinematic-photographer"],
            ("pixel-portfolio-fotografico", "it"),
        )
        self.assertIn("cinematic-photographer", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("cinematic-photographer"))
        # Chiara (editorial-designer-grid) must STAY enrolled.
        self.assertIn("editorial-designer-grid", _ARCHETYPE_SCHEMAS)
        self.assertIn("editorial-designer-grid", _MULTILOCALE_ENABLED_ARCHETYPES)
        # All 8 pre-A.13 archetypes still enrolled — A.13b is additive.
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent", "mass-market",
                    "ultra-luxury-cinematic"):
            self.assertIn(arc, _ARCHETYPE_SCHEMAS,
                          f"{arc} must remain enrolled after A.13b Pixel joins")
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} must keep multi-locale gate after A.13b")

    def test_a13b_pixel_out_guard_was_removed_from_chiara_tests(self):
        """USER-IMPOSED GUARDRAIL · verifies controlled removal of the
        Pixel-out guard that lived in A.13 Chiara tests.

        The proof is indirect but airtight: if the Pixel-out assertions
        had been left in place while Pixel joined the gate, the Chiara
        tests (`test_a13_chiara_archetype_registered` +
        `test_a13_chiara_full_multilocale_lifecycle_end_to_end`) would
        fail at the ``assertNotIn("cinematic-photographer", ...)`` step
        because Pixel IS now in both gate sets. A green run of those
        two Chiara tests implies the guard was removed correctly. This
        test makes the implication explicit by checking the gate state
        the Chiara tests now rely on: Pixel MUST be in
        `_ARCHETYPE_SCHEMAS` AND in `_MULTILOCALE_ENABLED_ARCHETYPES`
        AND Chiara MUST still be in both.

        Mirror of A.12b `test_a12b_villa_out_guard_was_removed_from_casa_tests`.
        """
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        self.assertIn("cinematic-photographer", _ARCHETYPE_SCHEMAS,
                      "Pixel must be in _ARCHETYPE_SCHEMAS post-A.13b")
        self.assertIn("cinematic-photographer", _MULTILOCALE_ENABLED_ARCHETYPES,
                      "Pixel must be in _MULTILOCALE_ENABLED_ARCHETYPES post-A.13b")
        self.assertIn("editorial-designer-grid", _ARCHETYPE_SCHEMAS,
                      "Chiara must still be in _ARCHETYPE_SCHEMAS post-A.13b")
        self.assertIn("editorial-designer-grid", _MULTILOCALE_ENABLED_ARCHETYPES,
                      "Chiara must still be in _MULTILOCALE_ENABLED_ARCHETYPES post-A.13b")

    def test_a13b_pixel_schema_shape_covers_all_pages(self):
        """The Pixel schema must surface groups for every Pixel page
        slug (home + serie + biografia + pubblicazioni + contatti)
        plus chrome-level groups (page='*'). The novel `series_list`
        and `publications` page kinds are plain string identifiers —
        no view dispatch."""
        groups = iter_groups("cinematic-photographer")
        self.assertGreaterEqual(len(groups), 8)
        pages = {g.get("page") for g in groups}
        for slug in ("*", "home", "serie", "biografia",
                     "pubblicazioni", "contatti"):
            self.assertIn(slug, pages,
                          f"Pixel schema missing page slug {slug!r}")

    def test_a13b_pixel_is_translatable_text_fields(self):
        """Scalar copy fields distributed across every Pixel page +
        chrome."""
        from apps.editor.schema import is_translatable
        arc = "cinematic-photographer"
        distributed_paths = (
            # home
            "home.headline",
            "home.subhead",
            "home.filmstrip_heading",
            "home.about_excerpt",
            "home.cta_heading",
            # serie (novel series_list kind)
            "serie.headline",
            "serie.subhead",
            "serie.index_intro",
            "serie.cta_heading",
            # biografia
            "biografia.headline",
            "biografia.subhead",
            "biografia.statement_heading",
            "biografia.kit_heading",
            "biografia.timeline_heading",
            # pubblicazioni (novel publications kind)
            "pubblicazioni.headline",
            "pubblicazioni.subhead",
            "pubblicazioni.press_heading",
            "pubblicazioni.exhibitions_heading",
            "pubblicazioni.awards_heading",
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
            "site.foot_kit",
            "site.nav_cta",
        )
        for path in distributed_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be translatable on cinematic-photographer",
            )

    def test_a13b_pixel_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Pixel — same
        contract as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "cinematic-photographer"
        for path in ("site.logo_word", "site.logo_initial",
                     "site.phone", "site.email",
                     "site.address", "site.license"):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must remain a global override on Pixel",
            )

    def test_a13b_pixel_hero_image_scalar_exposed(self):
        """USER-IMPOSED GUARDRAIL · `home.hero_image` IS exposed as a
        scalar image field (the only editable image surface in A.13b
        first wave).

        Positive assertion: `get_field_spec` returns a spec with
        `type="image"` for `home.hero_image`. No image-in-dict-row
        is exposed on Pixel in A.13b (unlike Chiara's
        `home.featured_works.items[].image` at deep path 2 levels).
        All image cells that exist in the registry (`posts[*].cover_image`)
        live under `posts` which stays registry-only — see the
        complex-shape exclusion test.
        """
        from apps.editor.schema import get_field_spec
        arc = "cinematic-photographer"
        spec = get_field_spec(arc, "home.hero_image")
        self.assertIsNotNone(spec,
                             "home.hero_image must be reachable via get_field_spec")
        self.assertEqual(
            spec.get("type"), "image",
            f"home.hero_image must carry type='image' (got {spec.get('type')!r})",
        )

    def test_a13b_pixel_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL · complex-shape exclusion test.

        Four categories of complex registry shapes must stay OUT of
        Pixel's editor perimeter (6th uniform enforcement across
        Lex/Juris/Casa/Villa/Chiara/Pixel):

        (1) **Per-series `posts` entries** (3 series detail records)
            INCLUDING the `posts[].cover_image` image col which must
            never reach the editor. This is the explicit
            detail-page-out policy enforcement for Pixel. Same
            perimeter policy applied to Lex `notabili`, Juris
            `insights`, Casa `posts`, Villa `posts`, Chiara `posts`.

        (2) Flat list-of-str containers:
              - `serie.filters` (5 filter pills)
              - `biografia.statement_paragraphs` (5 bio paragraphs)
              - `site.kit_footer_rows` (3 footer kit rows)

        (3) Form structure blocks:
              - `contatti.form_fields` + `contatti.form_sections`
                + `contatti.upload_field`

        Every path listed must fail `validate_key_path`.
        """
        from apps.editor.schema import validate_key_path
        arc = "cinematic-photographer"
        validate_rejects = [
            # (1) per-series posts entries (incl. cover_image explicit)
            "posts",
            "posts.0.title",
            "posts.0.lead",
            "posts.0.sections",
            "posts.0.gallery",
            "posts.0.print_meta",
            "posts.0.exif_credits",
            "posts.0.cover_image",  # image col that must stay registry-only
            "posts.1.cover_image",
            "posts.2.cover_image",
            "posts.2.next_label",
            # (2) flat list-of-str containers
            "serie.filters",
            "serie.filters.0",
            "biografia.statement_paragraphs",
            "biografia.statement_paragraphs.0",
            "site.kit_footer_rows",
            "site.kit_footer_rows.0",
            # (3) form structure blocks
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
                msg=f"{path} MUST be rejected by validate_key_path on cinematic-photographer",
            ):
                validate_key_path(arc, path)

    def test_a13b_pixel_structured_list_cells_are_global(self):
        """The 10 readonly indexed lists on Pixel stay global at cell
        level — text cols exposed via STRUCTURED_FIELD_SHAPES are
        customer-editable but never per-locale."""
        from apps.editor.schema import is_translatable
        arc = "cinematic-photographer"
        cell_paths = (
            "home.hero_credit_cells.0.label",
            "home.hero_credit_cells.3.value",
            "home.filmstrip.0.title",
            "home.filmstrip.3.discipline",
            "home.publications.0.outlet",
            "home.publications.2.period",
            "biografia.kit.0.model",
            "biografia.kit.3.body",
            "biografia.timeline.0.year",
            "biografia.timeline.11.body",
            "pubblicazioni.press.0.year",
            "pubblicazioni.press.7.outlet",
            "pubblicazioni.exhibitions.0.title",
            "pubblicazioni.exhibitions.5.period",
            "pubblicazioni.awards.0.title",
            "pubblicazioni.awards.5.subject",
            "contatti.channels.0.label",
            "contatti.channels.3.note",
            "site.exif_footer.0.label",
            "site.exif_footer.3.value",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Pixel",
            )

    def test_a13b_pixel_supported_locales_returns_canonical_five(self):
        """Pixel ships the canonical 5-locale set. Step-0 audit
        confirmed PERFECT parity (154 keys × 5 locales, zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("cinematic-photographer"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a13b_ninefold_regression_after_pixel_joins(self):
        """Regression guard: adding Pixel to gate + schemas must not
        disturb ANY of the nine pre-existing enrollments (Vertex +
        Pragma + Gusto + specialist + classic-gold + modern-transparent
        + mass-market + ultra-luxury-cinematic + editorial-designer-grid)."""
        from apps.editor.schema import is_translatable, supported_locales
        for arc in ("agency-creative-studio", "corporate-suite",
                    "fine-dining", "specialist", "classic-gold",
                    "modern-transparent", "mass-market",
                    "ultra-luxury-cinematic", "editorial-designer-grid"):
            self.assertTrue(
                is_translatable(arc, "home.headline"),
                f"{arc} home.headline must stay translatable",
            )
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must keep the canonical 5-locale set",
            )

    def test_a13b_pixel_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8/A.9/A.10/A.11/A.12/A.12b/A.13 integration
        guardrail — the Pixel ``cinematic-photographer/_base.html``
        must integrate the three bridge points together on the `.cp-*`
        skin: (1) preview-bridge.js conditional on ``preview_project``,
        (2) ``<title>`` honors ``site.logo_word``, (3) ``<body>``
        carries the ``mw-is-editor-preview`` guard class when inside
        the editor."""
        pixel = WebTemplate.objects.get(slug="pixel-portfolio-fotografico")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/portfolio/pixel-portfolio-fotografico/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=pixel)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A13b Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/portfolio/pixel-portfolio-fotografico/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A13b Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.14 · Sapore (trattoria-warm · restaurant-continuation family ·
    # first template) enrollment — Step 1 contract. OPENS the family
    # via staged dedicated-schema progression (mirror of real-estate
    # A.12+A.12b and portfolio A.13+A.13b). Brace (`street-modern`)
    # stays OUT until A.14b; the dual Brace-out guard at registration-
    # time + runtime (inside the lifecycle test) will be removed in A.14b
    # with a symmetric contract test. Menu rows stay INSIDE perimeter
    # as deep-path tuple cells (`menu.sections.{i}.dishes`) — novel
    # shape registered via 5 separate STRUCTURED_FIELD_SHAPES entries.
    # Sapore ships no posts list, so there are no `posts.*` paths in
    # the complex-shape exclusion guardrail (the absence is structural,
    # not a perimeter decision).
    # ------------------------------------------------------------------

    def test_a14_sapore_archetype_registered(self):
        """`trattoria-warm` is in the supported-archetype registry and
        the multi-locale gate. Pre-A.14 archetypes must all remain
        enrolled. (Brace-out guard was lifted in A.14b when Brace
        joined — see `test_a14b_brace_out_guard_was_removed_from_sapore_tests`
        for the contract that verifies the inversion.)"""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        # Sapore IS in.
        self.assertIn("trattoria-warm", _ARCHETYPE_SCHEMAS)
        self.assertIn("trattoria-warm", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("trattoria-warm", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("trattoria-warm"))
        baseline_slug, baseline_locale = _ARCHETYPE_BASELINE_TEMPLATE["trattoria-warm"]
        self.assertEqual(baseline_slug, "sapore-trattoria-pizzeria")
        self.assertEqual(baseline_locale, "it")

        # 10 pre-A.14 archetypes still enrolled (tenfold regression).
        for pre_slug in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
        ):
            self.assertIn(pre_slug, _ARCHETYPE_SCHEMAS, f"{pre_slug} lost enrollment")
            self.assertIn(pre_slug, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{pre_slug} lost multi-locale")

    def test_a14_sapore_schema_shape_covers_all_pages(self):
        """Sapore groups span the 6 page slugs + `*` chrome. Novel page
        kinds `signature` (forno page) and `events` (eventi page) are
        plain string identifiers in the registry — no view dispatches on
        them; they're just informational labels."""
        from apps.editor.schema import iter_groups
        groups = iter_groups("trattoria-warm")
        pages = {g.get("page") for g in groups}
        # Must cover chrome + home + 4 secondary pages.
        for expected in ("*", "home", "menu", "storia", "forno", "eventi", "contatti"):
            self.assertIn(expected, pages,
                          f"Sapore schema missing page `{expected}` coverage")

    def test_a14_sapore_is_translatable_text_fields(self):
        """A distributed sample of Sapore translatable paths — one per
        page — must classify as translatable. Mirrors the A.10/A.11/
        A.12/A.12b/A.13/A.13b pattern."""
        from apps.editor.schema import is_translatable
        arc = "trattoria-warm"
        translatable_paths = (
            # home
            "home.eyebrow", "home.headline", "home.intro",
            "home.chalkboard_heading", "home.family_heading",
            "home.forno_heading", "home.forno_text", "home.tavolata_heading",
            "home.cta_heading", "home.cta_intro",
            # menu (scalar)
            "menu.eyebrow", "menu.headline", "menu.wine_house_heading",
            # storia
            "storia.eyebrow", "storia.headline", "storia.intro",
            "storia.values_heading",
            # forno
            "forno.eyebrow", "forno.headline", "forno.pizza_heading",
            "forno.forno_story_heading", "forno.forno_story_text_1",
            # eventi
            "eventi.eyebrow", "eventi.headline", "eventi.birthday_heading",
            "eventi.contact_heading",
            # contatti
            "contatti.headline", "contatti.form_heading",
        )
        for path in translatable_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must classify as translatable on Sapore",
            )

    def test_a14_sapore_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Sapore — same
        contract as every previously-enrolled archetype. Non-text fields
        (url type `site.whatsapp_link`, select type `site.nav_cta_href`)
        are also global by type classification."""
        from apps.editor.schema import is_translatable
        arc = "trattoria-warm"
        for path in (
            "site.logo_word", "site.logo_initial",
            "site.phone", "site.email",
            "site.address", "site.license",
            "site.whatsapp_link",    # url type → global by type
            "site.nav_cta_href",     # select type → global by type
        ):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Sapore",
            )

    def test_a14_sapore_hero_image_scalar_exposed(self):
        """USER-IMPOSED GUARDRAIL: positive `get_field_spec` on
        `home.hero_image` returning `type=image`. The 7 top-level scalar
        image fields must all expose as image widgets in the sidebar."""
        from apps.editor.schema import get_field_spec
        arc = "trattoria-warm"
        image_scalars = (
            "home.hero_image",
            "home.forno_image",
            "home.tavolata_image",
            "storia.photo_image",
            "forno.forno_story_image",
            "forno.dough_image",
            "eventi.birthday_image",
        )
        for path in image_scalars:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Sapore schema")
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must expose as type=image",
            )

    def test_a14_sapore_image_cols_in_dict_rows_exposed(self):
        """USER-IMPOSED GUARDRAIL: positive `get_field_spec` on
        `home.family.0.portrait` and `storia.family.0.portrait` —
        image-in-dict-row pattern (Vertex A.3a/A.4 precedent). Both
        family lists carry a `portrait` col with type=image that must
        expose at cell level (baseline rows 0..2)."""
        from apps.editor.schema import get_field_spec, get_list_shape
        arc = "trattoria-warm"

        for list_path in ("home.family", "storia.family"):
            shape = get_list_shape(arc, list_path)
            self.assertIsNotNone(shape, f"{list_path} shape missing")
            self.assertEqual(shape.get("kind"), "dict")
            cols_dict = dict(shape.get("cols") or [])
            self.assertIn("portrait", cols_dict,
                          f"{list_path} must carry a `portrait` image col")
            self.assertEqual(cols_dict["portrait"].get("type"), "image")

            # Baseline rows 0..2 each expose `portrait` as type=image.
            for i in range(3):
                cell = get_field_spec(arc, f"{list_path}.{i}.portrait")
                self.assertIsNotNone(
                    cell, f"{list_path}.{i}.portrait missing from schema",
                )
                self.assertEqual(
                    cell.get("type"), "image",
                    f"{list_path}.{i}.portrait must expose as type=image",
                )

    def test_a14_sapore_menu_deep_path_cells_exposed(self):
        """USER-IMPOSED GUARDRAIL: menu rows stay INSIDE the perimeter.
        Each section's `dishes` tuple (name/desc/price) is registered at
        deep path `menu.sections.{i}.dishes` so `get_field_spec` must
        resolve first + last dishes of first + last section. Novel
        shape: tuple-list nested inside a dict-list parent. Handled by
        the A.14 extension to `_resolve_path` (list numeric indexing)."""
        from apps.editor.schema import get_field_spec
        arc = "trattoria-warm"
        # Section content sizes (verified Step-0): 7/7/6/5/5 dishes.
        first_section_first_dish = [
            ("menu.sections.0.dishes.0.name",  "text"),
            ("menu.sections.0.dishes.0.desc",  "textarea"),
            ("menu.sections.0.dishes.0.price", "text"),
        ]
        last_section_last_dish = [
            ("menu.sections.4.dishes.4.name",  "text"),   # section 4 has 5 dishes (0..4)
            ("menu.sections.4.dishes.4.desc",  "textarea"),
            ("menu.sections.4.dishes.4.price", "text"),
        ]
        # Spot-check the last dish of the largest sections (7 dishes at
        # indices 0..6).
        biggest_section_last_dish = [
            ("menu.sections.0.dishes.6.name",  "text"),
            ("menu.sections.1.dishes.6.price","text"),
        ]
        for path, expected_type in (
            first_section_first_dish
            + last_section_last_dish
            + biggest_section_last_dish
        ):
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — deep-path menu cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

        # Parent dict-list cells (`menu.sections.{i}.label` + `heading`)
        # also expose — the parent is `menu.sections` registered as
        # dict with label+heading cols (dishes col intentionally omitted
        # at parent level).
        for path in ("menu.sections.0.label", "menu.sections.4.heading"):
            self.assertIsNotNone(get_field_spec(arc, path),
                                 f"{path} parent cell missing")

    def test_a14_sapore_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL: complex shapes and registry-only
        paths stay outside the perimeter — `validate_key_path` rejects
        them with `InvalidEditableField`. Sapore ships NO posts list so
        posts.* paths are rejected structurally (no editable registration
        of any kind), but they're still included here to lock the
        cross-archetype policy."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "trattoria-warm"
        rejected_paths = (
            # Form structure (consistent policy)
            "contatti.form_sections",
            "contatti.form_fields",
            "contatti.form_sections.0.fields",
            "contatti.form_fields.0.name",
            # Flat list-of-str containers
            "storia.story",
            "storia.story.0",
            "contatti.occasion_options",
            "contatti.occasion_options.0",
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            # Top-level navigation index
            "pages",
            "pages.0.slug",
            # Posts list — Sapore ships no posts, but the policy still
            # applies (6-archetype uniform enforcement).
            "posts",
            "posts.0.title",
            "posts.0.cover_image",
        )
        for path in rejected_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Sapore must reject complex-shape path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a14_sapore_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text cell on Sapore stays global
        (non-translatable), including the novel deep-path menu cells.
        Image cells (portrait) are also global — image overrides never
        per-locale per D-098."""
        from apps.editor.schema import is_translatable
        arc = "trattoria-warm"
        cell_paths = (
            # home parent lists
            "home.family.0.name",
            "home.family.2.blurb",
            "home.family.0.portrait",     # image cell · stays global
            "home.reviews.0.quote",
            "home.reviews.2.author",
            "home.facts.0.label",
            "home.facts.2.value",
            "home.chalkboard_days.0.day",
            "home.chalkboard_days.4.note",
            "home.hours_rows.0.days",
            "home.hours_rows.2.hours",
            # menu parent dict-list
            "menu.sections.0.label",
            "menu.sections.4.heading",
            # menu deep-path tuple cells (novel shape)
            "menu.sections.0.dishes.0.name",
            "menu.sections.0.dishes.0.price",
            "menu.sections.4.dishes.4.name",
            "menu.sections.4.dishes.4.price",
            # storia parent lists
            "storia.timeline.0.year",
            "storia.timeline.2.desc",
            "storia.family.0.name",
            "storia.family.0.portrait",   # image cell · stays global
            "storia.values.0.title",
            "storia.values.3.desc",
            # forno parent lists
            "forno.pizza_signatures.0.name",
            "forno.pizza_signatures.3.price",
            "forno.pasta_signatures.0.name",
            "forno.pasta_signatures.3.price",
            "forno.producers.0.name",
            "forno.producers.4.ingredient",
            # eventi parent lists
            "eventi.experiences.0.title",
            "eventi.experiences.2.menu",
            "eventi.experiences.0.wine",
            # contatti parent lists
            "contatti.transport.0.mode",
            "contatti.transport.3.note",
            "contatti.hours_table.0.days",
            "contatti.hours_table.3.hours",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Sapore",
            )

    def test_a14_sapore_supported_locales_returns_canonical_five(self):
        """Sapore ships the canonical 5-locale set. Step-0 audit confirmed
        5-locale parity PERFECT (224 keys × 5 locales, zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("trattoria-warm"),
            ["it", "en", "fr", "es", "ar"],
        )
        # Outside-gate reference: startup-saas-landing (Elevate) after
        # A.17 rotated it from agency-digital-studio/Aura (now enrolled
        # · CLOSES agency-secondary family).
        self.assertEqual(supported_locales("startup-saas-landing"), [])

    def test_a14_tenfold_regression_after_sapore_joins(self):
        """Regression guard: the 10 pre-A.14 archetype classifications
        are unchanged after `trattoria-warm` joins the gate."""
        from apps.editor.schema import (
            is_translatable, supported_locales, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        pre_a14 = (
            "agency-creative-studio",
            "corporate-suite",
            "fine-dining",
            "specialist",
            "classic-gold",
            "modern-transparent",
            "mass-market",
            "ultra-luxury-cinematic",
            "editorial-designer-grid",
            "cinematic-photographer",
        )
        for arc in pre_a14:
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} lost multi-locale enrollment")
            # Sanity — each still returns the canonical five locales.
            self.assertEqual(
                supported_locales(arc), ["it", "en", "fr", "es", "ar"],
                f"{arc} supported_locales regressed",
            )
        # Vertex + Pragma + Gusto still classify home.headline as
        # translatable · logo_word as global (stable spot-check).
        for arc in ("agency-creative-studio", "corporate-suite", "fine-dining"):
            self.assertTrue(is_translatable(arc, "home.headline"),
                            f"{arc} home.headline regressed")
            self.assertFalse(is_translatable(arc, "site.logo_word"),
                             f"{arc} site.logo_word regressed")

    def test_a14_sapore_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.8/A.9/A.10/A.11/A.12/A.12b/A.13/A.13b
        integration guardrail — the Sapore `restaurant/trattoria-warm/_base.html`
        must integrate the three bridge points together on the `.tw-*`
        skin: (1) preview-bridge.js conditional on ``preview_project``,
        (2) ``<title>`` honors ``site.logo_word``, (3) ``<body>`` carries
        the ``mw-is-editor-preview`` guard class when inside the editor."""
        sapore = WebTemplate.objects.get(slug="sapore-trattoria-pizzeria")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/restaurant/sapore-trattoria-pizzeria/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=sapore)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A14 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/restaurant/sapore-trattoria-pizzeria/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A14 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.14b · Brace (street-modern · restaurant-continuation family ·
    # second template) enrollment — Step 1 contract. CLOSES the
    # restaurant-continuation family opened in A.14. Third staged
    # dedicated-schema closure (after real-estate A.12+A.12b and
    # portfolio A.13+A.13b). Zero new infrastructure required: menu
    # rows via deep-path dict-in-dict-list parent (Chiara precedent),
    # ordina routes lines via deep-path tuple-in-dict-list parent
    # (Sapore precedent via A.14 Step 2 render-side f66ac24 fix).
    # ------------------------------------------------------------------

    def test_a14b_brace_archetype_registered(self):
        """`street-modern` joins the supported-archetype registry and
        the multi-locale gate. All 11 pre-A.14b archetypes (incl. Sapore)
        must still be enrolled (eleven-fold regression)."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        self.assertIn("street-modern", _ARCHETYPE_SCHEMAS)
        self.assertIn("street-modern", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("street-modern", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("street-modern"))
        baseline_slug, baseline_locale = _ARCHETYPE_BASELINE_TEMPLATE["street-modern"]
        self.assertEqual(baseline_slug, "brace-street-food-lab")
        self.assertEqual(baseline_locale, "it")

        # 11 pre-A.14b archetypes still enrolled.
        for pre_slug in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm",
        ):
            self.assertIn(pre_slug, _ARCHETYPE_SCHEMAS, f"{pre_slug} lost enrollment")
            self.assertIn(pre_slug, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{pre_slug} lost multi-locale")

    def test_a14b_brace_out_guard_was_removed_from_sapore_tests(self):
        """USER-IMPOSED SYMMETRIC GUARDRAIL · mirror of A.12b Villa-out-
        removed and A.13b Pixel-out-removed contracts. Verifies that the
        Brace-out guards that lived in the A.14 Sapore tests (both
        registration-time inside `test_a14_sapore_archetype_registered`
        AND runtime at end-of-lifecycle-test) were correctly inverted
        when Brace joined, rather than forgotten. Silent regression on
        the inversion cannot happen."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        # Brace IS now in all three registries.
        self.assertIn("street-modern", _ARCHETYPE_SCHEMAS,
                      "Brace (street-modern) must be IN after A.14b")
        self.assertIn("street-modern", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("street-modern", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("street-modern"))

        # Sapore still enrolled (the archetype whose tests used to host
        # the Brace-out guard).
        self.assertIn("trattoria-warm", _ARCHETYPE_SCHEMAS,
                      "Sapore must stay enrolled after Brace joins")
        self.assertIn("trattoria-warm", _MULTILOCALE_ENABLED_ARCHETYPES)

    def test_a14b_brace_schema_shape_covers_all_pages(self):
        """Brace groups span the 6 page slugs + `*` chrome. Novel page
        kind `order` (ordina page) is a plain string identifier in the
        registry — no view dispatch."""
        from apps.editor.schema import iter_groups
        groups = iter_groups("street-modern")
        pages = {g.get("page") for g in groups}
        for expected in ("*", "home", "menu", "lab", "moments", "ordina", "contatti"):
            self.assertIn(expected, pages,
                          f"Brace schema missing page `{expected}` coverage")

    def test_a14b_brace_is_translatable_text_fields(self):
        """A distributed sample of Brace translatable paths — one per
        page — must classify as translatable."""
        from apps.editor.schema import is_translatable
        arc = "street-modern"
        translatable_paths = (
            # home
            "home.eyebrow", "home.headline", "home.intro",
            "home.hero_badge_label", "home.counter_label",
            "home.menu_strip_heading", "home.manifesto_heading",
            "home.crew_heading", "home.atmo_heading", "home.final_heading",
            # menu
            "menu.eyebrow", "menu.headline", "menu.intro",
            "menu.producers_heading",
            # lab
            "lab.eyebrow", "lab.headline", "lab.intro",
            "lab.manifesto_label", "lab.process_heading",
            # moments
            "moments.eyebrow", "moments.headline",
            "moments.featured_quote", "moments.featured_author",
            # ordina
            "ordina.eyebrow", "ordina.headline", "ordina.intro",
            "ordina.routes_heading", "ordina.partners_heading",
            "ordina.faq_heading",
            # contatti
            "contatti.headline", "contatti.jobs_heading",
            "contatti.form_heading",
        )
        for path in translatable_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must classify as translatable on Brace",
            )

    def test_a14b_brace_branding_and_contact_universals_are_global(self):
        """Shared global-text paths + typed fields (url/select) stay
        global on Brace — same contract as every previously-enrolled
        archetype."""
        from apps.editor.schema import is_translatable
        arc = "street-modern"
        for path in (
            "site.logo_word", "site.logo_initial",
            "site.phone", "site.email",
            "site.address", "site.license",
            "site.whatsapp_link",   # url type
            "site.nav_cta_href",    # select type
            "site.instagram_link",  # url type
            "site.tiktok_link",     # url type
        ):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Brace",
            )

    def test_a14b_brace_hero_image_scalars_exposed(self):
        """USER-IMPOSED GUARDRAIL: positive `get_field_spec` on the 3
        top-level scalar image fields (home.hero_image, lab.hero_image,
        moments.featured_image) returning `type=image`."""
        from apps.editor.schema import get_field_spec
        arc = "street-modern"
        for path in ("home.hero_image", "lab.hero_image", "moments.featured_image"):
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Brace schema")
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must expose as type=image",
            )

    def test_a14b_brace_image_cols_in_dict_rows_shallow_exposed(self):
        """USER-IMPOSED GUARDRAIL: 5 shallow image-in-dict-row lists
        (home.menu_strip_items, home.crew, home.atmo_strip, lab.crew,
        moments.grid) expose their image/portrait cells with
        `type=image`. Image-in-dict-row pattern (Vertex A.3a/A.4
        precedent + Villa A.12b precedent + Chiara A.13 precedent +
        Sapore A.14 precedent) · fifth archetype to exercise it."""
        from apps.editor.schema import get_field_spec
        arc = "street-modern"
        image_cell_paths = (
            "home.menu_strip_items.0.image",
            "home.menu_strip_items.5.image",   # last of 6
            "home.crew.0.portrait",
            "home.crew.2.portrait",
            "home.atmo_strip.0.image",
            "home.atmo_strip.2.image",
            "lab.crew.0.portrait",
            "lab.crew.3.portrait",             # last of 4
            "moments.grid.0.image",
            "moments.grid.5.image",            # last of 6
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec, f"{path} missing from Brace schema",
            )
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must expose as type=image",
            )

    def test_a14b_brace_menu_items_deep_path_image_exposed(self):
        """USER-IMPOSED GUARDRAIL · **nodo principale A.14b Step 0**:
        `menu.sections.{0..4}.items[].image` resolves at deep path
        2 levels (dict-in-dict-list parent shape · Chiara precedent).
        Each of the 5 sections registers a separate shape entry; first +
        last dish of first + last section must all expose `type=image`.
        Section sizes verified Step 0: 4/4/4/4/3."""
        from apps.editor.schema import get_field_spec
        arc = "street-modern"
        # First section, first dish — all 5 cols.
        first_section_first_dish = (
            ("menu.sections.0.items.0.name",  "text"),
            ("menu.sections.0.items.0.desc",  "textarea"),
            ("menu.sections.0.items.0.price", "text"),
            ("menu.sections.0.items.0.tag",   "text"),
            ("menu.sections.0.items.0.image", "image"),
        )
        # Last section (size 3), last dish index 2 — all 5 cols.
        last_section_last_dish = (
            ("menu.sections.4.items.2.name",  "text"),
            ("menu.sections.4.items.2.desc",  "textarea"),
            ("menu.sections.4.items.2.price", "text"),
            ("menu.sections.4.items.2.tag",   "text"),
            ("menu.sections.4.items.2.image", "image"),
        )
        # Largest sections (0..3, size 4) · last dish index 3.
        biggest_section_last_dish = (
            ("menu.sections.0.items.3.image", "image"),
            ("menu.sections.3.items.3.price", "text"),
        )
        for path, expected_type in (
            first_section_first_dish
            + last_section_last_dish
            + biggest_section_last_dish
        ):
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — deep-path menu item cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

    def test_a14b_brace_ordina_routes_deep_path_tuple_exposed(self):
        """USER-IMPOSED GUARDRAIL · **correction di ipotesi Step 0
        audit**: `ordina.routes.{0..2}.lines` expose tuple cells at
        deep path 2 levels (tuple-in-dict-list parent shape · Sapore
        precedent via A.14 f66ac24 render fix). Each of the 3 routes
        registers a separate shape entry; first + last line of first +
        last route must expose cols `label`/`value`. Initial hypothesis
        was OUT; audit demonstrated editorial value (address/phone/
        partner-names)."""
        from apps.editor.schema import get_field_spec
        arc = "street-modern"
        for path in (
            "ordina.routes.0.lines.0.label",
            "ordina.routes.0.lines.0.value",
            "ordina.routes.0.lines.2.label",   # last of 3
            "ordina.routes.0.lines.2.value",
            "ordina.routes.2.lines.0.label",   # last route, first line
            "ordina.routes.2.lines.2.value",   # last route, last line
        ):
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — deep-path route line cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), "text",
                f"{path} type mismatch (expected text)",
            )

    def test_a14b_brace_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL: complex shapes + registry-only paths
        stay outside the perimeter. Brace ships NO form structures
        (smaller out-policy set than Sapore) and NO posts list (same as
        Sapore · detail-page policy structurally inapplicable)."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "street-modern"
        rejected_paths = (
            # Flat list-of-str containers
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "home.manifesto_paragraphs",
            "home.manifesto_paragraphs.0",
            "moments.categories",
            "moments.categories.0",
            # Col-level exclusions (structural identifiers / routing flags)
            "menu.sections.0.id",
            "menu.sections.4.id",
            "moments.grid.0.filename",
            "moments.grid.5.filename",
            "ordina.routes.0.id",
            "ordina.routes.0.cta_kind",
            "ordina.routes.2.cta_kind",
            "contatti.channels.0.icon",
            "contatti.channels.0.kind",
            "contatti.channels.2.kind",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
        )
        for path in rejected_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Brace must reject complex-shape path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a14b_brace_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text/image cell on Brace stays
        global (non-translatable), including the novel deep-path menu
        items (dict-in-dict-list) and ordina routes lines (tuple-in-
        dict-list). Image cells are also global per D-098."""
        from apps.editor.schema import is_translatable
        arc = "street-modern"
        cell_paths = (
            # home parent lists
            "home.stats.0.value",
            "home.stats.3.label",
            "home.menu_strip_items.0.name",
            "home.menu_strip_items.5.price",
            "home.menu_strip_items.0.image",   # image cell
            "home.delivery_partners.0.name",
            "home.delivery_partners.3.eta",
            "home.crew.0.name",
            "home.crew.2.portrait",            # image cell
            "home.atmo_strip.0.cap",
            "home.atmo_strip.2.image",         # image cell
            # menu parent dict-list
            "menu.sections.0.label",
            "menu.sections.4.title",
            # menu deep-path dict-in-dict-list cells (novel shape)
            "menu.sections.0.items.0.name",
            "menu.sections.0.items.0.image",   # image cell
            "menu.sections.4.items.2.price",
            "menu.sections.4.items.2.image",   # image cell
            # menu.producers
            "menu.producers.0.name",
            "menu.producers.2.role",
            # lab parent lists
            "lab.manifesto_paragraphs.0.title",
            "lab.manifesto_paragraphs.3.text",
            "lab.process.0.num",
            "lab.process.2.desc",
            "lab.crew.0.name",
            "lab.crew.3.portrait",             # image cell
            "lab.values.0.title",
            "lab.values.3.desc",
            "lab.kitchen_specs.0.value",
            "lab.kitchen_specs.5.label",
            # moments.grid
            "moments.grid.0.cap",
            "moments.grid.5.image",            # image cell
            # ordina parent + nested
            "ordina.routes.0.title",
            "ordina.routes.2.cta_label",
            # ordina deep-path tuple cells (novel shape)
            "ordina.routes.0.lines.0.label",
            "ordina.routes.0.lines.2.value",
            "ordina.routes.2.lines.2.label",
            # ordina other lists
            "ordina.partners.0.name",
            "ordina.partners.3.zone",
            "ordina.hours_rows.0.day",
            "ordina.hours_rows.6.hours",
            "ordina.faq.0.q",
            "ordina.faq.3.a",
            # contatti lists
            "contatti.channels.0.label",
            "contatti.channels.2.value",
            "contatti.hours_rows.0.days",
            "contatti.transport_rows.0.mode",
            "contatti.jobs.0.role",
            "contatti.social.0.platform",
            "contatti.social.1.href",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Brace",
            )

    def test_a14b_brace_supported_locales_returns_canonical_five(self):
        """Brace ships the canonical 5-locale set. Step-0 audit
        confirmed 5-locale parity PERFECT (273 keys × 5 locales)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("street-modern"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a14b_brace_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the integration guardrail — Brace
        `restaurant/street-modern/_base.html` must integrate the three
        bridge points together on the `.sm-*` skin: (1) preview-bridge.js
        conditional on ``preview_project``, (2) ``<title>`` honors
        ``site.logo_word``, (3) ``<body>`` carries the
        ``mw-is-editor-preview`` guard class when inside the editor."""
        brace = WebTemplate.objects.get(slug="brace-street-food-lab")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/restaurant/brace-street-food-lab/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=brace)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A14b Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/restaurant/brace-street-food-lab/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A14b Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.15 · Bottega (artisan-workshop · ecommerce family · first
    # template) enrollment — Step 1 contract. OPENS the ecommerce family
    # via staged dedicated-schema progression (fourth staged opening
    # after real-estate · portfolio · restaurant-continuation). Luxe
    # (`fashion-editorial`) stays OUT until A.15b. Editor edits ONLY
    # template_content registry (presentational demo showcase) · zero
    # touches to apps.commerce (real catalog state · seller dashboard
    # scope). 14 readonly indexed list entries · tutti parent-level.
    # ------------------------------------------------------------------

    def test_a15_bottega_archetype_registered(self):
        """`artisan-workshop` joins the supported-archetype registry and
        the multi-locale gate. All 12 pre-A.15 archetypes must still be
        enrolled (twelve-fold regression). Luxe-out guard removed in
        A.15b via symmetric inversion — see
        `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        self.assertIn("artisan-workshop", _ARCHETYPE_SCHEMAS)
        self.assertIn("artisan-workshop", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("artisan-workshop", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("artisan-workshop"))
        baseline_slug, baseline_locale = _ARCHETYPE_BASELINE_TEMPLATE["artisan-workshop"]
        self.assertEqual(baseline_slug, "bottega-shop-artigianale")
        self.assertEqual(baseline_locale, "it")

        # 12 pre-A.15 archetypes still enrolled.
        for pre_slug in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
        ):
            self.assertIn(pre_slug, _ARCHETYPE_SCHEMAS, f"{pre_slug} lost enrollment")
            self.assertIn(pre_slug, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{pre_slug} lost multi-locale")

    def test_a15_bottega_schema_shape_covers_all_pages(self):
        """Bottega groups span the 6 page slugs + `*` chrome. Three
        novel page kinds (`shop`, `product`, `journal`) · plain string
        identifiers · no view dispatch."""
        from apps.editor.schema import iter_groups
        groups = iter_groups("artisan-workshop")
        pages = {g.get("page") for g in groups}
        for expected in ("*", "home", "shop", "product", "atelier", "journal", "contatti"):
            self.assertIn(expected, pages,
                          f"Bottega schema missing page `{expected}` coverage")

    def test_a15_bottega_is_translatable_text_fields(self):
        """Distributed sample of Bottega translatable paths — one per
        page — must classify as translatable."""
        from apps.editor.schema import is_translatable
        arc = "artisan-workshop"
        translatable_paths = (
            # home
            "home.eyebrow", "home.headline", "home.intro",
            "home.stamp_heading", "home.latest_heading",
            "home.makers_heading", "home.makers_intro",
            "home.provenance_heading", "home.care_heading",
            "home.cta_heading",
            # shop
            "shop.eyebrow", "shop.headline", "shop.intro",
            "shop.footer_note",
            # product
            "product.name", "product.subtitle", "product.intro",
            "product.artisan_bio", "product.care_intro",
            "product.provenance_heading",
            # atelier
            "atelier.eyebrow", "atelier.headline", "atelier.intro",
            "atelier.founder_heading", "atelier.mission_heading",
            "atelier.visit_heading",
            # journal
            "journal.eyebrow", "journal.headline", "journal.intro",
            # contatti
            "contatti.headline", "contatti.intro",
        )
        for path in translatable_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must classify as translatable on Bottega",
            )

    def test_a15_bottega_branding_and_contact_universals_are_global(self):
        """Shared global-text paths + typed fields stay global on
        Bottega — same contract as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "artisan-workshop"
        for path in (
            "site.logo_word", "site.logo_initial",
            "site.phone", "site.email",
            "site.address", "site.license",
            "site.whatsapp_link",  # url type
        ):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Bottega",
            )

    def test_a15_bottega_nested_dict_scalar_images_exposed(self):
        """USER-IMPOSED GUARDRAIL: nested-dict scalar image fields
        expose as type=image. Bottega has no top-level hero image
        (artisan-workshop is typographic-led DNA · Session 42) — only
        2 nested-dict scalar images: `product.artisan_portrait` and
        `atelier.founder_portrait` · Chiara `studio.founder.image`
        precedent shape."""
        from apps.editor.schema import get_field_spec
        arc = "artisan-workshop"
        for path in ("product.artisan_portrait", "atelier.founder_portrait"):
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Bottega schema")
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must expose as type=image",
            )

    def test_a15_bottega_image_cols_in_dict_rows_shallow_exposed(self):
        """USER-IMPOSED GUARDRAIL: 4 shallow image-in-dict-row lists
        (home.latest_items · home.makers · shop.products · product.related_items)
        expose their image/portrait cells with `type=image`. Image-in-
        dict-row pattern is now at 6+ precedents. shop.products covers
        9 demo product cards · first+middle+last tested."""
        from apps.editor.schema import get_field_spec
        arc = "artisan-workshop"
        image_cell_paths = (
            "home.latest_items.0.image",
            "home.latest_items.3.image",         # last of 4
            "home.makers.0.portrait",
            "home.makers.3.portrait",            # last of 4
            "shop.products.0.image",
            "shop.products.4.image",             # middle of 9
            "shop.products.8.image",             # last of 9
            "product.related_items.0.image",
            "product.related_items.2.image",     # last of 3
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec, f"{path} missing from Bottega schema",
            )
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must expose as type=image",
            )

    def test_a15_bottega_visible_catalog_fields_kept_in(self):
        """Stringent IN call per user Step 1 guidance: values like
        `n`/`edition`/`icon` that LOOK technical but are editorial
        visible content (customer-facing catalog numbering) must stay
        IN. 'N° 042' / '3 / 8' / 'Esaurito' / '01' are visible badges
        that a customer would typically edit — same category as Sapore
        forno.pizza_signatures.n (roman numeral visible counter). OUT
        only truly-structural cols (id slugs · available bool flag)."""
        from apps.editor.schema import get_field_spec
        arc = "artisan-workshop"
        # These are editorial visible — IN.
        visible_editorial = (
            ("shop.products.0.n",           "text"),
            ("shop.products.0.edition",     "text"),
            ("shop.products.0.tag",         "text"),
            ("home.latest_items.0.n",       "text"),
            ("home.latest_items.0.edition", "text"),
            ("home.latest_items.0.tag",     "text"),
            ("home.provenance_items.0.icon","text"),
            ("atelier.process_steps.0.n",   "text"),
            ("journal.entries.0.n",         "text"),
            ("product.related_items.0.n",   "text"),
        )
        for path, expected_type in visible_editorial:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — editorial-visible cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

    def test_a15_bottega_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL: complex shapes + structural identifiers
        stay outside the perimeter. Bottega ships NO posts (empty · same
        as Sapore · Brace · structural absence · detail-page policy stays
        at 6-archetype uniform enforcement)."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "artisan-workshop"
        rejected_paths = (
            # Flat list-of-str containers
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "site.stockists_rows",
            "site.stockists_rows.0",
            "home.press_items",
            "home.press_items.0",
            "shop.filter_groups",
            "shop.filter_groups.0.options",
            "shop.filter_groups.0.options.0",
            "shop.sort_options",
            "product.gallery",
            "product.gallery.0",
            "product.size_options",
            "contatti.card_hours_rows",
            "contatti.card_hours_rows.0",
            # Form structure
            "contatti.form_fields",
            # Navigation + posts (empty)
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
            # Col-level exclusions (structural identifiers · slug + flag)
            "shop.products.0.id",
            "shop.products.8.id",
            "shop.products.0.available",
            "home.latest_items.0.id",
            "home.latest_items.3.id",
            "product.related_items.0.id",
        )
        for path in rejected_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Bottega must reject complex-shape path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a15_bottega_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text/image cell on Bottega
        stays global (non-translatable), including visible catalog
        numbering (`n`/`edition`/`icon`) and image cells (portraits +
        product photos · D-098 per-locale image out-of-scope)."""
        from apps.editor.schema import is_translatable
        arc = "artisan-workshop"
        cell_paths = (
            # home.latest_items (4 rows · 8 cols · image col)
            "home.latest_items.0.name",
            "home.latest_items.3.price",
            "home.latest_items.0.image",   # image cell
            # home.makers (4 rows · 6 cols · portrait col)
            "home.makers.0.name",
            "home.makers.3.quote",
            "home.makers.2.portrait",      # image cell
            # home.provenance_items (3 rows · 4 cols)
            "home.provenance_items.0.icon",
            "home.provenance_items.2.desc",
            # home.stamp_rows (4 rows · 2 cols · tuple)
            "home.stamp_rows.0.label",
            "home.stamp_rows.3.value",
            # home.care_items (4 rows · 2 cols · tuple)
            "home.care_items.0.label",
            "home.care_items.3.value",
            # shop.products (9 rows · 9 cols IN · image col)
            "shop.products.0.name",
            "shop.products.8.price",
            "shop.products.0.n",
            "shop.products.4.edition",
            "shop.products.7.tag",
            "shop.products.5.image",       # image cell
            # product.info_rows (tuple 8)
            "product.info_rows.0.label",
            "product.info_rows.7.value",
            # product.care_items (tuple 4)
            "product.care_items.0.label",
            # product.provenance_steps (tuple 4 · 3 cols)
            "product.provenance_steps.0.step",
            "product.provenance_steps.3.desc",
            # product.related_items (3 rows · 5 cols · image col)
            "product.related_items.0.name",
            "product.related_items.2.image", # image cell
            # atelier.process_steps (5 rows · 5 cols)
            "atelier.process_steps.0.n",
            "atelier.process_steps.4.desc",
            # atelier.numbers_items (tuple 4)
            "atelier.numbers_items.0.value",
            "atelier.numbers_items.3.label",
            # journal.entries (6 rows · 5 cols)
            "journal.entries.0.n",
            "journal.entries.5.excerpt",
            # contatti.faq_items (4 rows · 2 cols)
            "contatti.faq_items.0.q",
            "contatti.faq_items.3.a",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Bottega",
            )

    def test_a15_bottega_supported_locales_returns_canonical_five(self):
        """Bottega ships the canonical 5-locale set. Step-0 audit
        confirmed 5-locale parity PERFECT (236 keys × 5 · zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("artisan-workshop"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a15_twelvefold_regression_after_bottega_joins(self):
        """Regression guard: the 12 pre-A.15 archetype classifications
        are unchanged after `artisan-workshop` joins the gate."""
        from apps.editor.schema import (
            is_translatable, supported_locales, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        pre_a15 = (
            "agency-creative-studio",
            "corporate-suite",
            "fine-dining",
            "specialist",
            "classic-gold",
            "modern-transparent",
            "mass-market",
            "ultra-luxury-cinematic",
            "editorial-designer-grid",
            "cinematic-photographer",
            "trattoria-warm",
            "street-modern",
        )
        for arc in pre_a15:
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} lost multi-locale enrollment")
            self.assertEqual(
                supported_locales(arc), ["it", "en", "fr", "es", "ar"],
                f"{arc} supported_locales regressed",
            )

    def test_a15_bottega_commerce_admin_boundary(self):
        """USER-IMPOSED LIGHT guardrail: the editor schema for Bottega
        must not leak into `apps.commerce` model paths. This is a LIGHT
        smoke test, not an architectural check — it verifies that the
        schema stays scoped to the registry content (template_content
        prefixes: home/shop/product/atelier/journal/contatti/site) and
        no field references apps.commerce model namespaces (e.g.
        `storefront.`, `cart.`, `variant.`, `order.`, `payment_intent.`).
        The real boundary is architectural: LiveTemplateView does not
        import apps.commerce — this test just blindates that the schema
        author didn't mistakenly add commerce-state paths."""
        from apps.editor.schema import iter_editable_fields
        arc = "artisan-workshop"
        commerce_model_prefixes = (
            "storefront.", "cart.", "variant.", "order.",
            "payment_intent.", "checkout.", "storefront_member.",
        )
        for path, _spec in iter_editable_fields(arc):
            for prefix in commerce_model_prefixes:
                self.assertFalse(
                    path.startswith(prefix),
                    f"Editor schema leaks into apps.commerce namespace: "
                    f"field `{path}` starts with `{prefix}` — editor must "
                    f"stay on template_content registry only"
                )

    def test_a15_bottega_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the integration guardrail — Bottega
        `ecommerce/artisan-workshop/_base.html` must integrate the three
        bridge points together on the `.aw-*` skin: (1) preview-bridge.js
        conditional on ``preview_project``, (2) ``<title>`` honors
        ``site.logo_word``, (3) ``<body>`` carries ``mw-is-editor-preview``
        guard class when inside the editor."""
        bottega = WebTemplate.objects.get(slug="bottega-shop-artigianale")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/ecommerce/bottega-shop-artigianale/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=bottega)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A15 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/ecommerce/bottega-shop-artigianale/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A15 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.15b · Luxe (fashion-editorial · ecommerce family · second
    # template) enrollment — Step 1 contract. CLOSES the ecommerce
    # family opened by A.15 Bottega · fourth staged dedicated-schema
    # closure (after real-estate + portfolio + restaurant-continuation).
    # Boundary editor-vs-commerce-admin preserved. 17 readonly indexed
    # list entries · tutti parent-level. 31 image surfaces ALL RENDERED
    # (photographically editorial DNA · no storage-only split).
    # ------------------------------------------------------------------

    def test_a15b_luxe_archetype_registered(self):
        """`fashion-editorial` joins the supported-archetype registry and
        the multi-locale gate. All 13 pre-A.15b archetypes (including
        Bottega) must still be enrolled (thirteen-fold regression)."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        self.assertIn("fashion-editorial", _ARCHETYPE_SCHEMAS)
        self.assertIn("fashion-editorial", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("fashion-editorial", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("fashion-editorial"))
        baseline_slug, baseline_locale = _ARCHETYPE_BASELINE_TEMPLATE["fashion-editorial"]
        self.assertEqual(baseline_slug, "luxe-fashion-store")
        self.assertEqual(baseline_locale, "it")

        # 13 pre-A.15b archetypes (12 pre-A.15 + Bottega) still enrolled.
        for pre_slug in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop",
        ):
            self.assertIn(pre_slug, _ARCHETYPE_SCHEMAS, f"{pre_slug} lost enrollment")
            self.assertIn(pre_slug, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{pre_slug} lost multi-locale")

    def test_a15b_luxe_out_guard_was_removed_from_bottega_tests(self):
        """USER-IMPOSED SYMMETRIC GUARDRAIL · 4th precedent after
        Villa-out (A.12b) · Pixel-out (A.13b) · Brace-out (A.14b).
        Verifies that the Luxe-out guards that lived in the A.15 Bottega
        tests (both registration-time inside
        `test_a15_bottega_archetype_registered` AND runtime start AND
        runtime end-of-lifecycle) were correctly inverted when Luxe
        joined, rather than forgotten. Silent regression on the
        inversion cannot happen."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        # Luxe IS now in all three registries.
        self.assertIn("fashion-editorial", _ARCHETYPE_SCHEMAS,
                      "Luxe (fashion-editorial) must be IN after A.15b")
        self.assertIn("fashion-editorial", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("fashion-editorial", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("fashion-editorial"))

        # Bottega still enrolled (the archetype whose tests used to host
        # the Luxe-out dual guard).
        self.assertIn("artisan-workshop", _ARCHETYPE_SCHEMAS,
                      "Bottega must stay enrolled after Luxe joins")
        self.assertIn("artisan-workshop", _MULTILOCALE_ENABLED_ARCHETYPES)

    def test_a15b_luxe_schema_shape_covers_all_pages(self):
        """Luxe groups span the 6 page slugs + `*` chrome. Two novel
        page kinds (`collection`, `lookbook`) · plain string identifiers ·
        no view dispatch."""
        from apps.editor.schema import iter_groups
        groups = iter_groups("fashion-editorial")
        pages = {g.get("page") for g in groups}
        for expected in ("*", "home", "collezione", "product", "maison", "lookbook", "contatti"):
            self.assertIn(expected, pages,
                          f"Luxe schema missing page `{expected}` coverage")

    def test_a15b_luxe_is_translatable_text_fields(self):
        """Distributed sample of Luxe translatable paths — one per
        page — must classify as translatable."""
        from apps.editor.schema import is_translatable
        arc = "fashion-editorial"
        translatable_paths = (
            # home
            "home.eyebrow", "home.headline", "home.intro",
            "home.manifesto_heading", "home.manifesto_text",
            "home.lookbook_teaser_heading", "home.drop_heading",
            "home.private_heading",
            # collezione
            "collezione.eyebrow", "collezione.headline", "collezione.intro",
            "collezione.footer_note",
            # product
            "product.name", "product.subtitle", "product.intro",
            "product.atelier_text", "product.care_intro",
            "product.provenance_heading",
            # maison
            "maison.eyebrow", "maison.headline", "maison.intro",
            "maison.statement_heading", "maison.direction_text",
            "maison.press_heading", "maison.visit_heading",
            # lookbook
            "lookbook.eyebrow", "lookbook.headline", "lookbook.intro",
            "lookbook.pullquote", "lookbook.notes_intro",
            "lookbook.shop_heading",
            # contatti
            "contatti.headline", "contatti.intro",
        )
        for path in translatable_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must classify as translatable on Luxe",
            )

    def test_a15b_luxe_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Luxe — same contract
        as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "fashion-editorial"
        for path in (
            "site.logo_word", "site.logo_initial",
            "site.phone", "site.email",
            "site.address", "site.license",
        ):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Luxe",
            )

    def test_a15b_luxe_scalar_and_nested_dict_images_exposed(self):
        """USER-IMPOSED GUARDRAIL: Luxe ships 1 scalar top-level image
        (`home.cover_image` · rendered full-bleed cover) + 2 nested-dict
        scalar images (`product.atelier_portrait` · `maison.direction_portrait`).
        All three expose as type=image. Luxe has NO storage-only image
        distinction (unlike Bottega · editorial DNA renders every
        surface)."""
        from apps.editor.schema import get_field_spec
        arc = "fashion-editorial"
        scalar_image_paths = (
            "home.cover_image",
            "product.atelier_portrait",
            "maison.direction_portrait",
        )
        for path in scalar_image_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Luxe schema")
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must expose as type=image",
            )

    def test_a15b_luxe_image_cols_in_dict_rows_shallow_exposed(self):
        """USER-IMPOSED GUARDRAIL: 6 shallow image-in-dict-row lists
        (home.tiles · home.lookbook_teaser_tiles · collezione.products ·
        product.related_items · maison.ateliers · lookbook.looks) expose
        their image cells with `type=image`. 30 image cells total ·
        first+middle+last sampled per list."""
        from apps.editor.schema import get_field_spec
        arc = "fashion-editorial"
        image_cell_paths = (
            # home.tiles · 4 items
            "home.tiles.0.image",
            "home.tiles.3.image",                      # last of 4
            # home.lookbook_teaser_tiles · 3 items
            "home.lookbook_teaser_tiles.0.image",
            "home.lookbook_teaser_tiles.2.image",      # last of 3
            # collezione.products · 9 items
            "collezione.products.0.image",
            "collezione.products.4.image",             # middle of 9
            "collezione.products.8.image",             # last of 9
            # product.related_items · 3 items
            "product.related_items.0.image",
            "product.related_items.2.image",           # last of 3
            # maison.ateliers · 3 items
            "maison.ateliers.0.image",
            "maison.ateliers.2.image",                 # last of 3
            # lookbook.looks · 6 items
            "lookbook.looks.0.image",
            "lookbook.looks.2.image",                  # middle
            "lookbook.looks.5.image",                  # last of 6
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec, f"{path} missing from Luxe schema",
            )
            self.assertEqual(
                spec.get("type"), "image",
                f"{path} must expose as type=image",
            )

    def test_a15b_luxe_visible_catalog_fields_kept_in(self):
        """Stringent IN call per user Step 1 guidance: values like
        `drop`/`n`/`tag` that LOOK technical but are editorial visible
        content (customer-facing catalog numbering + editorial badges)
        must stay IN. 'Drop 01 · Spring 26' / 'Look 03' / 'Lista
        d'attesa' are visible badges a customer would typically edit —
        same category as Bottega shop.products.edition. OUT only truly-
        structural cols (id slugs · available bool flag)."""
        from apps.editor.schema import get_field_spec
        arc = "fashion-editorial"
        # These are editorial visible — IN.
        visible_editorial = (
            # drop_label on cards (editorial drop badge)
            ("collezione.products.0.drop", "text"),
            ("collezione.products.4.drop", "text"),
            # n (Look number display badge)
            ("collezione.products.0.n",    "text"),
            ("product.related_items.0.n",  "text"),
            ("lookbook.looks.0.n",         "text"),
            # tag (editorial badge)
            ("collezione.products.0.tag",  "text"),
            ("collezione.products.6.tag",  "text"),
            ("home.tiles.0.tag",           "text"),
        )
        for path, expected_type in visible_editorial:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — editorial-visible cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

    def test_a15b_luxe_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL: complex shapes + structural identifiers
        stay outside the perimeter. Luxe ships NO posts (empty · same
        structural absence as Bottega/Sapore/Brace · detail-page policy
        stays at 6-archetype uniform enforcement)."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "fashion-editorial"
        rejected_paths = (
            # Flat list-of-str containers
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "site.office_rows",
            "site.office_rows.0",
            "home.press_items",
            "home.press_items.0",
            "collezione.filter_groups",
            "collezione.filter_groups.0.options",
            "collezione.filter_groups.0.options.0",
            "collezione.sort_options",
            "collezione.sort_options.0",
            "product.gallery",
            "product.gallery.0",
            "product.size_options",
            "product.size_options.0",
            "product.color_options",
            "product.color_options.0",
            # Form structure
            "contatti.form_fields",
            "contatti.form_fields.0.name",
            # Navigation + posts (empty)
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
            # Col-level exclusions (structural identifiers · slug + flag)
            "collezione.products.0.id",
            "collezione.products.8.id",
            "collezione.products.0.available",
            "collezione.products.7.available",
            "home.tiles.0.id",
            "home.tiles.3.id",
            "product.related_items.0.id",
            "product.related_items.2.id",
        )
        for path in rejected_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Luxe must reject complex-shape path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a15b_luxe_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text/image cell on Luxe stays
        global (non-translatable), including visible catalog numbering
        (`drop`/`n`/`tag`) and image cells (6 image-in-dict-row lists ·
        D-098 per-locale image out-of-scope)."""
        from apps.editor.schema import is_translatable
        arc = "fashion-editorial"
        cell_paths = (
            # home.tiles (4 rows · 4 cols · image col)
            "home.tiles.0.name",
            "home.tiles.3.price",
            "home.tiles.0.image",          # image cell
            # home.atelier_numbers (tuple 4 · 2 cols)
            "home.atelier_numbers.0.value",
            "home.atelier_numbers.3.label",
            # home.lookbook_teaser_tiles (dict 3 · 3 cols · image col)
            "home.lookbook_teaser_tiles.0.title",
            "home.lookbook_teaser_tiles.2.credit",
            "home.lookbook_teaser_tiles.1.image",   # image cell
            # home.drop_metadata (tuple 4 · 2 cols)
            "home.drop_metadata.0.label",
            "home.drop_metadata.3.value",
            # collezione.products (9 rows · 7 cols IN · image col)
            "collezione.products.0.name",
            "collezione.products.8.price",
            "collezione.products.0.n",
            "collezione.products.4.drop",
            "collezione.products.7.tag",
            "collezione.products.5.image",  # image cell
            # product.info_rows (tuple 8 · 2 cols)
            "product.info_rows.0.label",
            "product.info_rows.7.value",
            # product.care_items (tuple 4 · 2 cols)
            "product.care_items.0.label",
            # product.provenance_steps (tuple 4 · 3 cols)
            "product.provenance_steps.0.n",
            "product.provenance_steps.3.desc",
            # product.related_items (3 rows · 5 cols · image col)
            "product.related_items.0.name",
            "product.related_items.2.image",   # image cell
            # maison.ateliers (3 rows · 7 cols · image col)
            "maison.ateliers.0.city",
            "maison.ateliers.2.team",
            "maison.ateliers.1.image",         # image cell
            # maison.press_items (5 rows · 4 cols · text only)
            "maison.press_items.0.magazine",
            "maison.press_items.4.byline",
            # maison.numbers_items (tuple 4 · 2 cols)
            "maison.numbers_items.0.value",
            "maison.numbers_items.3.label",
            # lookbook.credits_rows (tuple 8 · 2 cols)
            "lookbook.credits_rows.0.label",
            "lookbook.credits_rows.7.value",
            # lookbook.looks (6 rows · 5 cols · image col)
            "lookbook.looks.0.title",
            "lookbook.looks.5.outfit",
            "lookbook.looks.3.image",          # image cell
            # lookbook.notes_items (dict 3 · 2 cols)
            "lookbook.notes_items.0.label",
            "lookbook.notes_items.2.text",
            # contatti.maison_cards (3 rows · 5 cols)
            "contatti.maison_cards.0.city",
            "contatti.maison_cards.2.hours",
            # contatti.faq_items (4 rows · 2 cols)
            "contatti.faq_items.0.q",
            "contatti.faq_items.3.a",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Luxe",
            )

    def test_a15b_luxe_supported_locales_returns_canonical_five(self):
        """Luxe ships the canonical 5-locale set. Step-0 audit confirmed
        5-locale parity PERFECT (259 keys × 5 · zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("fashion-editorial"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a15b_thirteenfold_regression_after_luxe_joins(self):
        """Regression guard: the 13 pre-A.15b archetype classifications
        (12 pre-A.15 + Bottega) are unchanged after `fashion-editorial`
        joins the gate."""
        from apps.editor.schema import (
            is_translatable, supported_locales, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        pre_a15b = (
            "agency-creative-studio",
            "corporate-suite",
            "fine-dining",
            "specialist",
            "classic-gold",
            "modern-transparent",
            "mass-market",
            "ultra-luxury-cinematic",
            "editorial-designer-grid",
            "cinematic-photographer",
            "trattoria-warm",
            "street-modern",
            "artisan-workshop",
        )
        for arc in pre_a15b:
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} lost multi-locale enrollment")
            self.assertEqual(
                supported_locales(arc), ["it", "en", "fr", "es", "ar"],
                f"{arc} supported_locales regressed",
            )

    def test_a15b_luxe_commerce_admin_boundary(self):
        """USER-IMPOSED LIGHT guardrail (same shape as Bottega A.15):
        the editor schema for Luxe must not leak into `apps.commerce`
        model paths. Schema stays scoped to the registry content
        (template_content prefixes: home/collezione/product/maison/
        lookbook/contatti/site) and no field references apps.commerce
        model namespaces. Real boundary is architectural
        (LiveTemplateView does not import apps.commerce) — this test
        just blindates that the schema author didn't mistakenly add
        commerce-state paths."""
        from apps.editor.schema import iter_editable_fields
        arc = "fashion-editorial"
        commerce_model_prefixes = (
            "storefront.", "cart.", "variant.", "order.",
            "payment_intent.", "checkout.", "storefront_member.",
        )
        for path, _spec in iter_editable_fields(arc):
            for prefix in commerce_model_prefixes:
                self.assertFalse(
                    path.startswith(prefix),
                    f"Editor schema leaks into apps.commerce namespace: "
                    f"field `{path}` starts with `{prefix}` — editor must "
                    f"stay on template_content registry only"
                )

    def test_a15b_luxe_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.15 Bottega bridge-guard — Luxe
        `ecommerce/fashion-editorial/_base.html` must integrate the three
        bridge points together on the `.fe-*` skin: (1) preview-bridge.js
        conditional on ``preview_project``, (2) ``<title>`` honors
        ``site.logo_word``, (3) ``<body>`` carries ``mw-is-editor-preview``
        guard class when inside the editor."""
        luxe = WebTemplate.objects.get(slug="luxe-fashion-store")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/ecommerce/luxe-fashion-store/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=luxe)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A15b Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/ecommerce/luxe-fashion-store/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A15b Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.16 · Salute (clinic · medical-other family · first template)
    # enrollment — Step 1 contract. OPENS the medical-other family via
    # staged dedicated-schema progression extended to **3-phase variant**
    # (A.16 Salute · A.16b Benessere · A.16c Famiglia). First 3-template
    # staged progression. Dual-out guard planted for BOTH `wellness` +
    # `family` (removed in A.16b + A.16c respectively). 16 readonly
    # indexed list entries · tutti parent-level · ZERO deep-path.
    # ------------------------------------------------------------------

    def test_a16_salute_archetype_registered(self):
        """`clinic` joins the supported-archetype registry and the
        multi-locale gate. Benessere (`wellness`) + Famiglia (`family`)
        stay OUT at BOTH layers (registration-time here · runtime inside
        the lifecycle test end-of-test guard). All 14 pre-A.16 archetypes
        must still be enrolled (fourteen-fold regression)."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        self.assertIn("clinic", _ARCHETYPE_SCHEMAS)
        self.assertIn("clinic", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("clinic", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("clinic"))
        baseline_slug, baseline_locale = _ARCHETYPE_BASELINE_TEMPLATE["clinic"]
        self.assertEqual(baseline_slug, "salute-studio-medico")
        self.assertEqual(baseline_locale, "it")

        # DUAL-OUT GUARD fully removed in A.16b + A.16c:
        # - Wellness-out guard removed in A.16b · see
        #   `test_a16b_benessere_out_guard_was_removed_from_salute_tests`
        # - Family-out guard removed in A.16c · see
        #   `test_a16c_family_out_guard_was_removed_from_salute_tests`
        # Medical-other family OFFICIALLY CLOSED after A.16c · 5th
        # staged dedicated-schema family closure (after real-estate +
        # portfolio + restaurant-continuation + ecommerce + medical-other).

        # 14 pre-A.16 archetypes still enrolled.
        for pre_slug in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop", "fashion-editorial",
        ):
            self.assertIn(pre_slug, _ARCHETYPE_SCHEMAS, f"{pre_slug} lost enrollment")
            self.assertIn(pre_slug, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{pre_slug} lost multi-locale")

    def test_a16_salute_schema_shape_covers_all_pages(self):
        """Salute groups span the 7 page slugs + `*` chrome. Two novel
        page kinds (`prevention` + `appointment`) · plain string
        identifiers · no view dispatch."""
        from apps.editor.schema import iter_groups
        groups = iter_groups("clinic")
        pages = {g.get("page") for g in groups}
        for expected in ("*", "home", "studio", "servizi", "prevenzione", "medici", "contatti", "prenota"):
            self.assertIn(expected, pages,
                          f"Salute schema missing page `{expected}` coverage")

    def test_a16_salute_is_translatable_text_fields(self):
        """Distributed sample of Salute translatable paths — one per
        page — must classify as translatable."""
        from apps.editor.schema import is_translatable
        arc = "clinic"
        translatable_paths = (
            # home
            "home.eyebrow", "home.headline", "home.subhead",
            "home.specialties_heading", "home.journey_heading",
            "home.prevenzione_heading", "home.team_heading",
            "home.partners_heading", "home.trust_note",
            # studio
            "studio.eyebrow", "studio.headline", "studio.intro",
            "studio.values_heading", "studio.photo_heading",
            "studio.photo_body", "studio.timeline_heading",
            # servizi
            "servizi.eyebrow", "servizi.headline", "servizi.intro",
            "servizi.svc_heading", "servizi.faq_heading",
            # prevenzione
            "prevenzione.eyebrow", "prevenzione.headline",
            "prevenzione.intro", "prevenzione.pack_heading",
            "prevenzione.how_heading",
            # medici
            "medici.eyebrow", "medici.headline", "medici.intro",
            "medici.footnote_body",
            # contatti
            "contatti.headline", "contatti.intro",
            "contatti.form_title", "contatti.form_intro",
            # prenota
            "prenota.eyebrow", "prenota.headline", "prenota.intro",
            "prenota.help_title", "prenota.alt_body",
        )
        for path in translatable_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must classify as translatable on Salute",
            )

    def test_a16_salute_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Salute — same contract
        as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "clinic"
        for path in (
            "site.logo_word", "site.logo_initial",
            "site.phone", "site.email",
            "site.address", "site.license",
        ):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Salute",
            )

    def test_a16_salute_scalar_and_image_in_dict_rows_exposed(self):
        """USER-IMPOSED GUARDRAIL: Salute ships 1 scalar top-level image
        (`studio.photo_src` · about page photo · RENDERED) + 14 image
        cells across 2 image-in-dict-row lists (`home.team_ribbon_people[].avatar`
        × 8 + `medici.doctors[].portrait` × 6). All 15 image surfaces
        rendered (specialist-family precedent)."""
        from apps.editor.schema import get_field_spec
        arc = "clinic"
        scalar_image_paths = ("studio.photo_src",)
        for path in scalar_image_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Salute schema")
            self.assertEqual(spec.get("type"), "image",
                             f"{path} must expose as type=image")
        image_cell_paths = (
            # home.team_ribbon_people × 8 (avatar col)
            "home.team_ribbon_people.0.avatar",
            "home.team_ribbon_people.7.avatar",     # last of 8
            # medici.doctors × 6 (portrait col)
            "medici.doctors.0.portrait",
            "medici.doctors.5.portrait",            # last of 6
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Salute schema")
            self.assertEqual(spec.get("type"), "image",
                             f"{path} must expose as type=image")

    def test_a16_salute_visible_catalog_fields_kept_in(self):
        """Stringent IN call (audit-driven · precedent chain Sapore→
        Brace→Bottega→Luxe→**Salute**): visible editorial numbering
        (`num` on journey/how/help steps) + customer-facing badge text
        (`popular_label`) stay IN. OUT only truly-structural (bool flag
        `is_popular`) and truly-technical (raw `icon_svg` XML)."""
        from apps.editor.schema import get_field_spec
        arc = "clinic"
        visible_editorial = (
            ("home.journey_steps.0.num",        "text"),
            ("home.journey_steps.3.num",        "text"),
            ("prevenzione.how_steps.0.num",     "text"),
            ("prevenzione.packages.0.popular_label", "text"),
            ("prenota.help_steps.0.num",        "text"),
        )
        for path, expected_type in visible_editorial:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — editorial-visible cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

    def test_a16_salute_raw_svg_fields_excluded(self):
        """USER-IMPOSED GUARDRAIL · NOVEL 5th OUT CATEGORY PRECEDENT:
        Salute ships 18 raw `icon_svg` fields (inline SVG XML markup in
        `home.specialties[]` × 8 + `servizi.services[]` × 10). These are
        technical content carrying raw XML — unsafe as plain text input
        for customers, poor UX, and outside the editor widget contract.
        **OUT col-level** via STRUCTURED_FIELD_SHAPES col exclusion (not
        added to the cols list for either shape). Verified by:
        (a) `get_field_spec` returning None on representative deep paths
        (b) `validate_key_path` raising for the same paths."""
        from apps.editor.schema import (
            get_field_spec, validate_key_path, InvalidEditableField,
        )
        arc = "clinic"
        raw_svg_paths = (
            "home.specialties.0.icon_svg",
            "home.specialties.7.icon_svg",          # last of 8
            "servizi.services.0.icon_svg",
            "servizi.services.9.icon_svg",          # last of 10
        )
        for path in raw_svg_paths:
            self.assertIsNone(
                get_field_spec(arc, path),
                f"{path} must NOT expose as an editable cell (raw SVG OUT)",
            )
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Salute must reject raw-SVG path via validate_key_path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a16_salute_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL: complex shapes + structural identifiers
        + bool flags + nested list-of-str stay outside the perimeter.
        Salute ships NO posts (empty · same structural absence as Bottega/
        Luxe/Sapore/Brace · detail-page policy stays at 6-archetype
        uniform enforcement count)."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "clinic"
        rejected_paths = (
            # Flat list-of-str containers
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "site.foot_extra_rows",
            "site.foot_extra_rows.0",
            "home.partners",
            "home.partners.0",
            "prenota.trust",
            "prenota.trust.0",
            # Form structures (Juris/Gusto/Bottega/Luxe precedent)
            "contatti.form_fields",
            "contatti.form_fields.0.name",
            "prenota.form_fields",
            "prenota.form_fields.0.name",
            "prenota.form_sections",
            "prenota.form_sections.0.num",
            # Nested list-of-str inside dict rows (Juris precedent)
            "servizi.services.0.items",
            "servizi.services.0.items.0",
            "prevenzione.packages.0.includes",
            "prevenzione.packages.0.includes.0",
            "home.prevenzione_cards.0.includes",
            "home.prevenzione_cards.0.includes.0",
            "medici.doctors.0.tags",
            "medici.doctors.0.tags.0",
            # Col-level bool flag (Luxe available precedent · preserves
            # popular_label text editability · no bool field type support)
            "prevenzione.packages.0.is_popular",
            # Raw SVG (5th OUT category precedent · separate test covers in depth)
            "home.specialties.0.icon_svg",
            "servizi.services.0.icon_svg",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
        )
        for path in rejected_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Salute must reject complex-shape path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a16_salute_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text/image cell on Salute stays
        global (non-translatable · D-098 per-locale image out-of-scope)."""
        from apps.editor.schema import is_translatable
        arc = "clinic"
        cell_paths = (
            # home.stats (tuple 3 · 2 cols)
            "home.stats.0.value",
            "home.stats.2.label",
            # home.stats_strip (tuple 4 · 2 cols)
            "home.stats_strip.0.value",
            "home.stats_strip.3.label",
            # home.specialties (8 rows · 3 cols IN)
            "home.specialties.0.title",
            "home.specialties.7.blurb",
            # home.journey_steps (4 rows · num IN)
            "home.journey_steps.0.num",
            "home.journey_steps.3.body",
            # home.prevenzione_cards (3 rows · 8 cols IN)
            "home.prevenzione_cards.0.title",
            "home.prevenzione_cards.2.price",
            # home.team_ribbon_people (8 rows · 3 cols · image)
            "home.team_ribbon_people.0.name",
            "home.team_ribbon_people.7.avatar",   # image cell
            # studio.values (4 rows · 2 cols)
            "studio.values.0.title",
            "studio.values.3.body",
            # studio.timeline (4 rows · 3 cols)
            "studio.timeline.0.year",
            "studio.timeline.3.body",
            # servizi.services (10 rows · 4 cols IN)
            "servizi.services.0.title",
            "servizi.services.9.price",
            # servizi.faqs (tuple 3 · 2 cols)
            "servizi.faqs.0.q",
            "servizi.faqs.2.a",
            # prevenzione.packages (3 rows · 9 cols IN · includes popular_label)
            "prevenzione.packages.0.title",
            "prevenzione.packages.2.cta",
            "prevenzione.packages.0.popular_label",
            # prevenzione.how_steps (4 rows · 3 cols · num IN)
            "prevenzione.how_steps.0.num",
            "prevenzione.how_steps.3.body",
            # medici.doctors (6 rows · 4 cols IN · image)
            "medici.doctors.0.name",
            "medici.doctors.5.portrait",            # image cell
            # contatti.hours_table (tuple 4 · 2 cols)
            "contatti.hours_table.0.day",
            "contatti.hours_table.3.value",
            # contatti.access (4 rows · 3 cols)
            "contatti.access.0.icon",
            "contatti.access.3.body",
            # prenota.help_steps (4 rows · 3 cols · num IN)
            "prenota.help_steps.0.num",
            "prenota.help_steps.3.body",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Salute",
            )

    def test_a16_salute_supported_locales_returns_canonical_five(self):
        """Salute ships the canonical 5-locale set. Step-0 audit confirmed
        5-locale parity PERFECT (576 keys × 5 · zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("clinic"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a16_fourteenfold_regression_after_salute_joins(self):
        """Regression guard: the 14 pre-A.16 archetype classifications
        are unchanged after `clinic` joins the gate."""
        from apps.editor.schema import (
            is_translatable, supported_locales, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        pre_a16 = (
            "agency-creative-studio",
            "corporate-suite",
            "fine-dining",
            "specialist",
            "classic-gold",
            "modern-transparent",
            "mass-market",
            "ultra-luxury-cinematic",
            "editorial-designer-grid",
            "cinematic-photographer",
            "trattoria-warm",
            "street-modern",
            "artisan-workshop",
            "fashion-editorial",
        )
        for arc in pre_a16:
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} lost multi-locale enrollment")
            self.assertEqual(
                supported_locales(arc), ["it", "en", "fr", "es", "ar"],
                f"{arc} supported_locales regressed",
            )

    def test_a16_salute_clinic_admin_boundary(self):
        """USER-IMPOSED LIGHT guardrail (mirrors A.15/A.15b commerce
        boundary shape): the editor schema for Salute must not leak
        into pseudo-admin / data-like model paths. Schema stays scoped
        to the registry content (template_content prefixes:
        home/studio/servizi/prevenzione/medici/contatti/prenota/site).
        This is a LIGHT smoke test · blindates that the schema author
        didn't accidentally add scheduler-state / booking-state / patient-
        record-like paths."""
        from apps.editor.schema import iter_editable_fields
        arc = "clinic"
        admin_model_prefixes = (
            "appointment.", "booking.", "patient.", "scheduler.",
            "calendar_slot.", "medical_record.", "prescription.",
        )
        for path, _spec in iter_editable_fields(arc):
            for prefix in admin_model_prefixes:
                self.assertFalse(
                    path.startswith(prefix),
                    f"Editor schema leaks into pseudo-admin namespace: "
                    f"field `{path}` starts with `{prefix}` — editor must "
                    f"stay on template_content registry only"
                )

    def test_a16_salute_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.15/A.15b bridge-guard — Salute
        `medical/clinic/_base.html` must integrate the three bridge
        points together on the `.cl-*` skin: (1) preview-bridge.js
        conditional on ``preview_project``, (2) ``<title>`` honors
        ``site.logo_word``, (3) ``<body>`` carries ``mw-is-editor-preview``
        guard class when inside the editor."""
        salute = WebTemplate.objects.get(slug="salute-studio-medico")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/medical/salute-studio-medico/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=salute)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A16 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/medical/salute-studio-medico/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A16 Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.16b · Benessere (wellness · medical-other family · second
    # template · MIDDLE phase of 3-phase staged progression) enrollment
    # — Step 1 contract. Removes wellness-out guard half of the dual-
    # out planted in A.16 (family-out PRESERVED for A.16c closer).
    # First time guard removal applies twice from a single opener
    # (sub-recipe extends from 1-removal to 2-removal phase · 5th
    # precedent of guard removal pattern after Villa/Pixel/Brace/Luxe).
    # 17 readonly indexed list entries · tutti parent-level · ZERO
    # deep-path. 19 image surfaces all rendered. DEFERRED novel shape:
    # home.ambients tuple-with-image (first-wave OUT · whole list).
    # ------------------------------------------------------------------

    def test_a16b_benessere_archetype_registered(self):
        """`wellness` joins the supported-archetype registry and the
        multi-locale gate. Famiglia (`family`) stays OUT at BOTH layers
        (registration-time here · runtime inside the A.16 Salute lifecycle
        test end-of-test guard · A.16c closer). Salute still enrolled.
        All 15 pre-A.16b archetypes (including Salute) must still be
        enrolled (fifteen-fold regression)."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        self.assertIn("wellness", _ARCHETYPE_SCHEMAS)
        self.assertIn("wellness", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("wellness", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("wellness"))
        baseline_slug, baseline_locale = _ARCHETYPE_BASELINE_TEMPLATE["wellness"]
        self.assertEqual(baseline_slug, "benessere-centro-olistico")
        self.assertEqual(baseline_locale, "it")

        # Family-out guard removed in A.16c · medical-other family CLOSED.
        # See `test_a16c_family_out_guard_was_removed_from_salute_tests`
        # for the 6th precedent of guard removal pattern.

        # 15 pre-A.16b archetypes still enrolled (14 pre-A.16 + Salute).
        for pre_slug in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop", "fashion-editorial",
            "clinic",
        ):
            self.assertIn(pre_slug, _ARCHETYPE_SCHEMAS, f"{pre_slug} lost enrollment")
            self.assertIn(pre_slug, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{pre_slug} lost multi-locale")

    def test_a16b_benessere_out_guard_was_removed_from_salute_tests(self):
        """USER-IMPOSED SYMMETRIC GUARDRAIL · 5th precedent after
        Villa/Pixel/Brace/Luxe · first time guard removal applies
        twice from a single opener (A.16 Salute planted DUAL-OUT GUARD
        for wellness + family · A.16b removes wellness-out ·
        A.16c will remove family-out). Verifies wellness-out guard
        removed from A.16 Salute tests (registration-time + lifecycle
        start + lifecycle end · 3 locations total) while family-out
        guard PRESERVED unchanged."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        # Benessere IS now in all three registries.
        self.assertIn("wellness", _ARCHETYPE_SCHEMAS,
                      "Benessere (wellness) must be IN after A.16b")
        self.assertIn("wellness", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("wellness", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("wellness"))

        # Salute still enrolled (the archetype whose tests hosted the
        # dual-out guard).
        self.assertIn("clinic", _ARCHETYPE_SCHEMAS,
                      "Salute must stay enrolled after Benessere joins")
        self.assertIn("clinic", _MULTILOCALE_ENABLED_ARCHETYPES)

        # Famiglia enrolled in A.16c · medical-other family CLOSED.
        # Original test preserved family-out guard · updated after A.16c.
        self.assertIn("family", _ARCHETYPE_SCHEMAS,
                      "Famiglia must be enrolled after A.16c closer")
        self.assertIn("family", _MULTILOCALE_ENABLED_ARCHETYPES)

    def test_a16b_benessere_schema_shape_covers_all_pages(self):
        """Benessere groups span the 7 page slugs + `*` chrome. One
        novel page kind (`gallery` · ambienti page) + shared `appointment`
        kind with Salute · plain string identifiers · no view dispatch."""
        from apps.editor.schema import iter_groups
        groups = iter_groups("wellness")
        pages = {g.get("page") for g in groups}
        for expected in ("*", "home", "filosofia", "rituali", "ambienti", "professionisti", "contatti", "prenota"):
            self.assertIn(expected, pages,
                          f"Benessere schema missing page `{expected}` coverage")

    def test_a16b_benessere_is_translatable_text_fields(self):
        """Distributed sample of Benessere translatable paths — one per
        page — must classify as translatable."""
        from apps.editor.schema import is_translatable
        arc = "wellness"
        translatable_paths = (
            # home
            "home.eyebrow", "home.headline", "home.subhead",
            "home.manifesto", "home.rituali_heading",
            "home.benefits_heading", "home.ambients_heading",
            "home.therapists_heading", "home.journey_heading",
            "home.calendar_heading",
            # filosofia
            "filosofia.eyebrow", "filosofia.headline", "filosofia.intro",
            "filosofia.timeline_heading", "filosofia.cta_heading",
            # rituali
            "rituali.eyebrow", "rituali.headline", "rituali.intro",
            "rituali.advice_heading", "rituali.packages_heading",
            "rituali.cta_heading",
            # ambienti
            "ambienti.eyebrow", "ambienti.headline", "ambienti.intro",
            "ambienti.cta_heading",
            # professionisti
            "professionisti.eyebrow", "professionisti.headline",
            "professionisti.intro", "professionisti.philo_quote",
            # contatti
            "contatti.headline", "contatti.intro",
            "contatti.form_intro", "contatti.hours_heading",
            # prenota
            "prenota.eyebrow", "prenota.headline", "prenota.intro",
            "prenota.calendar_heading", "prenota.form_title",
        )
        for path in translatable_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must classify as translatable on Benessere",
            )

    def test_a16b_benessere_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Benessere — same
        contract as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "wellness"
        for path in (
            "site.logo_word", "site.logo_initial",
            "site.phone", "site.email",
            "site.address", "site.license",
        ):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Benessere",
            )

    def test_a16b_benessere_scalar_and_image_in_dict_rows_exposed(self):
        """USER-IMPOSED GUARDRAIL: Benessere ships 3 scalar top-level
        images (`home.hero_image` + `filosofia.photo_image` +
        `contatti.map_image`) + 16 image cells across 3 image-in-dict-row
        lists (`ambienti.rooms[].image` × 8 + `home.therapists_trio[].portrait`
        × 3 + `professionisti.people[].portrait` × 5). All 19 image
        surfaces rendered (editorial olistico skin · no storage-only
        split)."""
        from apps.editor.schema import get_field_spec
        arc = "wellness"
        scalar_image_paths = (
            "home.hero_image",
            "filosofia.photo_image",
            "contatti.map_image",
        )
        for path in scalar_image_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Benessere schema")
            self.assertEqual(spec.get("type"), "image",
                             f"{path} must expose as type=image")
        image_cell_paths = (
            # ambienti.rooms × 8 (image col)
            "ambienti.rooms.0.image",
            "ambienti.rooms.7.image",                     # last of 8
            # home.therapists_trio × 3 (portrait col)
            "home.therapists_trio.0.portrait",
            "home.therapists_trio.2.portrait",            # last of 3
            # professionisti.people × 5 (portrait col)
            "professionisti.people.0.portrait",
            "professionisti.people.4.portrait",           # last of 5
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Benessere schema")
            self.assertEqual(spec.get("type"), "image",
                             f"{path} must expose as type=image")

    def test_a16b_benessere_visible_catalog_fields_kept_in(self):
        """Stringent IN call (audit-driven · 6th archetype precedent
        chain after Sapore/Brace/Bottega/Luxe/Salute): visible editorial
        calendar labels (`day`/`num`/`month` on both calendar lists) +
        step numbering (`num` on journey) + typographic init (`init`
        on pillars) + editorial category tag (`tag` on packages) stay
        IN. OUT only truly-scheduler-state (`has_slots`/`soldout` bool
        flags) and nested list-of-str (`slots`/`includes`/`tags`)."""
        from apps.editor.schema import get_field_spec
        arc = "wellness"
        visible_editorial = (
            ("home.calendar.0.day",             "text"),
            ("home.calendar.6.month",           "text"),
            ("prenota.calendar.0.num",          "text"),
            ("home.journey.0.num",              "text"),
            ("filosofia.pillars.0.init",        "text"),
            ("rituali.packages.0.tag",          "text"),
            ("rituali.packages.1.tag",          "text"),
        )
        for path, expected_type in visible_editorial:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — editorial-visible cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

    def test_a16b_benessere_calendar_bool_flags_excluded(self):
        """NOVEL Benessere-specific · re-application of Luxe `available`
        + Salute `is_popular` precedent: 4 bool flag cols OUT on both
        calendar lists (scheduler-state-like · not editorial content).
        Adding a bool field type would be a horizontal feature affecting
        every archetype with bool fields — resisted. Verified by
        `get_field_spec` returning None + `validate_key_path` raising."""
        from apps.editor.schema import (
            get_field_spec, validate_key_path, InvalidEditableField,
        )
        arc = "wellness"
        bool_flag_paths = (
            "home.calendar.0.has_slots",
            "home.calendar.0.soldout",
            "home.calendar.6.has_slots",
            "home.calendar.6.soldout",
            "prenota.calendar.0.has_slots",
            "prenota.calendar.0.soldout",
            "prenota.calendar.6.has_slots",
            "prenota.calendar.6.soldout",
        )
        for path in bool_flag_paths:
            self.assertIsNone(
                get_field_spec(arc, path),
                f"{path} must NOT expose as an editable cell (bool flag OUT)",
            )
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Benessere must reject bool-flag path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a16b_benessere_nested_str_lists_excluded(self):
        """Nested list-of-str inside dict rows (Juris precedent re-
        application): `slots` × 2 calendars · `includes` on packages ·
        `tags` on people · `interest_options` inside the non-standard
        contatti.form_fields nested dict. All OUT col-level (calendar
        slots as parent-walk path · others as direct col exclusion).
        `contatti.form_fields` as a whole is OUT via uniform form-
        structure policy (Juris/Gusto/Bottega/Luxe/Salute precedent)."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "wellness"
        nested_str_paths = (
            "home.calendar.0.slots",
            "home.calendar.0.slots.0",
            "prenota.calendar.0.slots",
            "prenota.calendar.0.slots.0",
            "rituali.packages.0.includes",
            "rituali.packages.0.includes.0",
            "professionisti.people.0.tags",
            "professionisti.people.0.tags.0",
            "contatti.form_fields",
            "contatti.form_fields.interest_label",
            "contatti.form_fields.interest_options",
            "contatti.form_fields.interest_options.0",
        )
        for path in nested_str_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Benessere must reject nested str-list path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a16b_benessere_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL: complex shapes stay outside the
        perimeter. Benessere ships NO posts (empty · same structural
        absence as Salute/Bottega/Luxe/Sapore/Brace · detail-page policy
        stays at 6-archetype uniform enforcement count)."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "wellness"
        rejected_paths = (
            # Flat list-of-str containers
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "home.hero_meta",
            "home.hero_meta.0",
            "home.press",
            "home.press.0",
            "prenota.why",
            "prenota.why.0",
            # Form structures (contatti.form_placeholders + form_helpers +
            # form_fields all nested-dict · prenota.form_fields list-of-
            # dict · prenota.form_sections list-of-dict)
            "contatti.form_placeholders",
            "contatti.form_placeholders.name",
            "contatti.form_helpers",
            "contatti.form_helpers.email",
            "prenota.form_fields",
            "prenota.form_fields.0.name",
            "prenota.form_sections",
            "prenota.form_sections.0.num",
            # DEFERRED novel shape (home.ambients tuple-with-image · 4
            # tiles · zero precedent · first-wave OUT via schema omission)
            "home.ambients",
            "home.ambients.0",
            "home.ambients.0.0",
            "home.ambients.3",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
        )
        for path in rejected_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Benessere must reject complex-shape path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a16b_benessere_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text/image cell on Benessere
        stays global (non-translatable · D-098 per-locale image out-of-
        scope)."""
        from apps.editor.schema import is_translatable
        arc = "wellness"
        cell_paths = (
            # site.socials (tuple 3 · 2 cols)
            "site.socials.0.label",
            "site.socials.2.url",
            # home.rituali (tuple 4 · 3 cols)
            "home.rituali.0.name",
            "home.rituali.3.price",
            # home.benefits (tuple 3 · 2 cols)
            "home.benefits.0.title",
            "home.benefits.2.body",
            # home.therapists_trio (dict 3 · 4 cols · portrait image)
            "home.therapists_trio.0.name",
            "home.therapists_trio.2.portrait",       # image cell
            # home.journey (dict 4 · 3 cols · num IN)
            "home.journey.0.num",
            "home.journey.3.body",
            # home.calendar (dict 7 · 3 cols IN: day/num/month)
            "home.calendar.0.day",
            "home.calendar.6.month",
            # filosofia.pillars (dict 3 · init/title/body)
            "filosofia.pillars.0.init",
            "filosofia.pillars.2.body",
            # filosofia.timeline (dict 4 · 3 cols)
            "filosofia.timeline.0.year",
            "filosofia.timeline.3.body",
            # rituali.treatments (dict 10 · 4 cols)
            "rituali.treatments.0.name",
            "rituali.treatments.9.price",
            # rituali.advice (dict 3 · 2 cols)
            "rituali.advice.0.title",
            "rituali.advice.2.body",
            # rituali.packages (dict 2 · 6 cols IN)
            "rituali.packages.0.tag",
            "rituali.packages.1.cta",
            # ambienti.rooms (dict 8 · 5 cols · image col)
            "ambienti.rooms.0.title",
            "ambienti.rooms.7.image",                # image cell
            # professionisti.people (dict 5 · 5 cols IN · portrait)
            "professionisti.people.0.name",
            "professionisti.people.4.portrait",      # image cell
            # contatti.blocks (dict 4 · 3 cols)
            "contatti.blocks.0.label",
            "contatti.blocks.3.sub",
            # contatti.access (dict 3 · 2 cols)
            "contatti.access.0.mode",
            "contatti.access.2.text",
            # contatti.hours (dict 7 · 2 cols)
            "contatti.hours.0.day",
            "contatti.hours.6.value",
            # prenota.calendar (dict 7 · 3 cols IN: day/num/month)
            "prenota.calendar.0.day",
            "prenota.calendar.6.month",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Benessere",
            )

    def test_a16b_benessere_supported_locales_returns_canonical_five(self):
        """Benessere ships the canonical 5-locale set. Step-0 audit
        confirmed 5-locale parity PERFECT (546 keys × 5 · zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("wellness"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a16b_fifteenfold_regression_after_benessere_joins(self):
        """Regression guard: the 15 pre-A.16b archetype classifications
        (14 pre-A.16 + Salute) are unchanged after `wellness` joins the
        gate."""
        from apps.editor.schema import (
            is_translatable, supported_locales, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        pre_a16b = (
            "agency-creative-studio",
            "corporate-suite",
            "fine-dining",
            "specialist",
            "classic-gold",
            "modern-transparent",
            "mass-market",
            "ultra-luxury-cinematic",
            "editorial-designer-grid",
            "cinematic-photographer",
            "trattoria-warm",
            "street-modern",
            "artisan-workshop",
            "fashion-editorial",
            "clinic",
        )
        for arc in pre_a16b:
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} lost multi-locale enrollment")
            self.assertEqual(
                supported_locales(arc), ["it", "en", "fr", "es", "ar"],
                f"{arc} supported_locales regressed",
            )

    def test_a16b_benessere_clinic_admin_boundary(self):
        """USER-IMPOSED LIGHT guardrail (mirrors A.16 Salute clinic-admin
        boundary): the editor schema for Benessere must not leak into
        pseudo-admin / scheduler-state / data-like model paths. Schema
        stays scoped to the registry content (template_content prefixes:
        home/filosofia/rituali/ambienti/professionisti/contatti/prenota/site).
        Light smoke test · blindates that the schema author didn't
        accidentally add scheduler/booking/patient/calendar-slot paths."""
        from apps.editor.schema import iter_editable_fields
        arc = "wellness"
        admin_model_prefixes = (
            "appointment.", "booking.", "patient.", "scheduler.",
            "calendar_slot.", "medical_record.", "prescription.",
        )
        for path, _spec in iter_editable_fields(arc):
            for prefix in admin_model_prefixes:
                self.assertFalse(
                    path.startswith(prefix),
                    f"Editor schema leaks into pseudo-admin namespace: "
                    f"field `{path}` starts with `{prefix}` — editor must "
                    f"stay on template_content registry only"
                )

    def test_a16b_benessere_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.16 Salute bridge-guard — Benessere
        `medical/wellness/_base.html` must integrate the three bridge
        points together on the `.we-*` skin: (1) preview-bridge.js
        conditional on ``preview_project``, (2) ``<title>`` honors
        ``site.logo_word``, (3) ``<body>`` carries ``mw-is-editor-preview``
        guard class when inside the editor."""
        benessere = WebTemplate.objects.get(slug="benessere-centro-olistico")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/medical/benessere-centro-olistico/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=benessere)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A16b Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/medical/benessere-centro-olistico/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A16b Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.16c · Famiglia (family · medical-other family · third template ·
    # CLOSER phase of 3-phase staged progression) enrollment — Step 1
    # contract. **CLOSES the medical-other family** · removes family-out
    # guard residuo from A.16 Salute tests (6th precedent of guard
    # removal pattern · completes the 2-removal-phase sub-recipe variant
    # established in A.16b). 5th staged dedicated-schema family closure
    # (after real-estate + portfolio + restaurant-continuation + ecommerce).
    # 20 readonly indexed list entries · **4 DEEP-PATH** crescita.topics.
    # {0..3}.items (Sapore menu.sections.{i}.dishes precedent mirror ·
    # f66ac24 render-side fix mechanical reuse). 16 image surfaces all
    # rendered. Novel col name `src` on home.gallery (mechanical reuse).
    # Zero raw SVG · zero bool flags · NO form_fields list-of-dict
    # (form as flat scalars · simpler OUT policy than Benessere).
    # ------------------------------------------------------------------

    def test_a16c_family_archetype_registered(self):
        """`family` joins the supported-archetype registry and the
        multi-locale gate. All 16 pre-A.16c archetypes (including Salute
        + Benessere) must still be enrolled (sixteen-fold regression).
        Medical-other family CLOSED · no out-guard active."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        self.assertIn("family", _ARCHETYPE_SCHEMAS)
        self.assertIn("family", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("family", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("family"))
        baseline_slug, baseline_locale = _ARCHETYPE_BASELINE_TEMPLATE["family"]
        self.assertEqual(baseline_slug, "famiglia-pediatria")
        self.assertEqual(baseline_locale, "it")

        # 16 pre-A.16c archetypes still enrolled (14 pre-A.16 + Salute + Benessere).
        for pre_slug in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop", "fashion-editorial",
            "clinic", "wellness",
        ):
            self.assertIn(pre_slug, _ARCHETYPE_SCHEMAS, f"{pre_slug} lost enrollment")
            self.assertIn(pre_slug, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{pre_slug} lost multi-locale")

    def test_a16c_family_out_guard_was_removed_from_salute_tests(self):
        """USER-IMPOSED SYMMETRIC GUARDRAIL · **6th precedent** after
        Villa/Pixel/Brace/Luxe/Wellness · **CLOSES the 2-removal-phase
        sub-recipe** established in A.16b. First 3-phase staged
        progression completes (A.16 Salute planted DUAL-OUT GUARD for
        wellness + family · A.16b removed wellness-out · A.16c removes
        family-out · medical-other family OFFICIALLY CLOSED).
        Sub-recipe pattern generalizes from "one-opener-one-closer"
        (2-phase) to "one-opener-two-closers" (3-phase) · both variants
        preserve D-098 invariant."""
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS, _ARCHETYPE_BASELINE_TEMPLATE,
            _MULTILOCALE_ENABLED_ARCHETYPES, is_supported_archetype,
        )
        # Family IS now in all three registries
        self.assertIn("family", _ARCHETYPE_SCHEMAS,
                      "Famiglia (family) must be IN after A.16c")
        self.assertIn("family", _ARCHETYPE_BASELINE_TEMPLATE)
        self.assertIn("family", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("family"))

        # Salute + Benessere still enrolled (medical-other family CLOSED)
        for sibling in ("clinic", "wellness"):
            self.assertIn(sibling, _ARCHETYPE_SCHEMAS,
                          f"{sibling} must stay enrolled after Famiglia closes the family")
            self.assertIn(sibling, _MULTILOCALE_ENABLED_ARCHETYPES)

    def test_a16c_medical_other_family_closed(self):
        """USER-IMPOSED GUARDRAIL: medical-other family CLOSED ·
        all 3 archetypes IN (clinic + wellness + family) · no out-guard
        active. 5th staged dedicated-schema family closure (after
        real-estate + portfolio + restaurant-continuation + ecommerce)."""
        from apps.editor.schema import _ARCHETYPE_SCHEMAS, _MULTILOCALE_ENABLED_ARCHETYPES
        for arc in ("clinic", "wellness", "family"):
            self.assertIn(arc, _ARCHETYPE_SCHEMAS,
                          f"{arc} must be enrolled · medical-other CLOSED")
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} must be multi-locale · medical-other CLOSED")

    def test_a16c_family_schema_shape_covers_all_pages(self):
        """Famiglia groups span the 6 page slugs + `*` chrome. Novel
        `faq` kind (crescita page) · NO `appointment` kind · plain
        string identifiers · no view dispatch."""
        from apps.editor.schema import iter_groups
        groups = iter_groups("family")
        pages = {g.get("page") for g in groups}
        for expected in ("*", "home", "studio", "visite", "crescita", "pediatre", "contatti"):
            self.assertIn(expected, pages,
                          f"Famiglia schema missing page `{expected}` coverage")

    def test_a16c_family_is_translatable_text_fields(self):
        """Distributed sample of Famiglia translatable paths — one per
        page — must classify as translatable."""
        from apps.editor.schema import is_translatable
        arc = "family"
        translatable_paths = (
            # home
            "home.eyebrow", "home.headline", "home.subhead",
            "home.team_heading", "home.journey_heading",
            "home.faq_heading", "home.gallery_heading",
            "home.urgency_title", "home.urgency_text",
            "home.cta_heading",
            # studio
            "studio.eyebrow", "studio.headline", "studio.intro",
            "studio.history_heading", "studio.cta_heading",
            # visite
            "visite.eyebrow", "visite.headline", "visite.intro",
            "visite.tips_heading", "visite.cta_heading",
            # crescita
            "crescita.eyebrow", "crescita.headline", "crescita.intro",
            "crescita.materials_heading", "crescita.cta_heading",
            # pediatre
            "pediatre.eyebrow", "pediatre.headline", "pediatre.intro",
            "pediatre.extra_text",
            # contatti
            "contatti.headline", "contatti.intro",
            "contatti.form_title", "contatti.form_intro",
        )
        for path in translatable_paths:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must classify as translatable on Famiglia",
            )

    def test_a16c_family_branding_and_contact_universals_are_global(self):
        """Shared global-text paths stay global on Famiglia — same
        contract as every previously-enrolled archetype."""
        from apps.editor.schema import is_translatable
        arc = "family"
        for path in (
            "site.logo_word", "site.logo_initial",
            "site.phone", "site.email",
            "site.address", "site.license",
            "site.whatsapp_link",   # url type · precedent
        ):
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Famiglia",
            )

    def test_a16c_family_scalar_and_image_in_dict_rows_exposed(self):
        """USER-IMPOSED GUARDRAIL: Famiglia ships 3 scalar top-level
        images (`home.hero_image` + `studio.studio_image` +
        `contatti.map_image`) + 13 image cells across 3 image-in-dict-row
        lists (`home.doctors[].portrait` × 4 + `home.gallery[].src` × 5 +
        `pediatre.doctors[].portrait` × 4). Novel col name `src` on
        home.gallery. All 16 image surfaces rendered (pediatric skin ·
        no storage-only split)."""
        from apps.editor.schema import get_field_spec
        arc = "family"
        scalar_image_paths = (
            "home.hero_image",
            "studio.studio_image",
            "contatti.map_image",
        )
        for path in scalar_image_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Famiglia schema")
            self.assertEqual(spec.get("type"), "image",
                             f"{path} must expose as type=image")
        image_cell_paths = (
            # home.doctors × 4 (portrait col)
            "home.doctors.0.portrait",
            "home.doctors.3.portrait",
            # home.gallery × 5 (NOVEL `src` col name)
            "home.gallery.0.src",
            "home.gallery.4.src",
            # pediatre.doctors × 4 (portrait col)
            "pediatre.doctors.0.portrait",
            "pediatre.doctors.3.portrait",
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Famiglia schema")
            self.assertEqual(spec.get("type"), "image",
                             f"{path} must expose as type=image")

    def test_a16c_family_deep_path_crescita_topics_items_exposed(self):
        """USER-IMPOSED GUARDRAIL (NOVEL for Famiglia · Sapore precedent
        mirror): `crescita.topics[].items` is tuple-in-dict-list deep-
        path · registered as 4 separate STRUCTURED_FIELD_SHAPES entries
        mirroring Sapore `menu.sections.{0..4}.dishes` pattern.
        Mechanical reuse of f66ac24 render-side contract-alignment fix ·
        zero new infra needed. Verified via:
        (a) All 4 deep-path entries registered in STRUCTURED_FIELD_SHAPES
        (b) Sample cells (q/a positional) resolvable via `get_field_spec`
            through both list indexes (topic index + item index)
        (c) Each deep-path shape is `tuple` kind with `tuple_order: [q,a]`
        """
        from apps.editor.schema import STRUCTURED_FIELD_SHAPES, get_field_spec
        arc = "family"
        shapes = STRUCTURED_FIELD_SHAPES.get(arc, {})
        # (a) 4 deep-path entries registered
        for i in range(4):
            key = f"crescita.topics.{i}.items"
            self.assertIn(key, shapes, f"{key} must be registered deep-path shape")
            shape = shapes[key]
            # (c) tuple kind + tuple_order
            self.assertEqual(shape.get("kind"), "tuple",
                             f"{key} must be tuple kind")
            self.assertEqual(shape.get("tuple_order"), ["q", "a"],
                             f"{key} must have tuple_order [q, a]")
        # (b) sample cells resolvable
        sample_cells = (
            ("crescita.topics.0.items.0.q", "text"),
            ("crescita.topics.0.items.0.a", "textarea"),
            ("crescita.topics.0.items.3.q", "text"),    # last of 4 tuples
            ("crescita.topics.3.items.0.q", "text"),    # last of 4 topics
            ("crescita.topics.3.items.3.a", "textarea"),
        )
        for path, expected_type in sample_cells:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} deep-path cell missing from Famiglia schema")
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

    def test_a16c_family_visible_catalog_fields_kept_in(self):
        """Stringent IN call (audit-driven · 7th archetype precedent
        chain after Sapore/Brace/Bottega/Luxe/Salute/Benessere):
        visible editorial numbering/labels stay IN. Famiglia brings
        `meta` (area label), `tag`, `exp_label`/`exp_value`, `wa_label`,
        `age` (range label), and icon text-refs as editorial visible
        IN candidates."""
        from apps.editor.schema import get_field_spec
        arc = "family"
        visible_editorial = (
            ("crescita.topics.0.meta",       "text"),
            ("crescita.topics.3.meta",       "text"),
            ("crescita.topics.0.icon",       "text"),
            ("home.age_groups.0.range",      "text"),
            ("home.journey_steps.0.age",     "text"),
            ("home.doctors.0.wa_label",      "text"),
            ("pediatre.doctors.0.tag",       "text"),
            ("pediatre.doctors.0.exp_label", "text"),
            ("pediatre.doctors.0.exp_value", "text"),
            ("pediatre.doctors.0.wa_label",  "text"),
            ("home.trust_items.0.icon",      "text"),
            ("contatti.travel.0.icon",       "text"),
        )
        for path, expected_type in visible_editorial:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(
                spec,
                f"{path} missing — editorial-visible cell must be editable",
            )
            self.assertEqual(
                spec.get("type"), expected_type,
                f"{path} type mismatch (expected {expected_type})",
            )

    def test_a16c_family_complex_shapes_excluded_from_perimeter(self):
        """USER-IMPOSED GUARDRAIL: complex shapes stay outside the
        perimeter. Famiglia ships NO posts (empty · structural absence ·
        detail-page policy stays at 6-archetype uniform enforcement)."""
        from apps.editor.schema import validate_key_path, InvalidEditableField
        arc = "family"
        rejected_paths = (
            # Flat list-of-str
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "contatti.reason_options",
            "contatti.reason_options.0",
            # Form-related nested-dicts (Juris/Gusto/Bottega/Luxe/Salute/Benessere precedent)
            "contatti.form_placeholders",
            "contatti.form_placeholders.parent_name",
            "contatti.form_helpers",
            "contatti.form_helpers.email",
            # Nested list-of-str inside dict rows (Juris precedent)
            "home.age_groups.0.items",
            "home.age_groups.0.items.0",
            "pediatre.doctors.0.specs",
            "pediatre.doctors.0.specs.0",
            # Deep-path parent `items` col (OUT at parent · IN via 4 sub-path shape entries)
            "crescita.topics.0.items.keyword",  # non-existent subkey sanity
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
        )
        for path in rejected_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Famiglia must reject complex-shape path: {path}",
            ):
                validate_key_path(arc, path)

    def test_a16c_family_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text/image cell on Famiglia
        stays global (non-translatable · D-098 per-locale image out-of-
        scope · including deep-path cells `crescita.topics.{i}.items.{j}.{q,a}`)."""
        from apps.editor.schema import is_translatable
        arc = "family"
        cell_paths = (
            # home.trust_items (dict 3 · 2 cols)
            "home.trust_items.0.icon",
            "home.trust_items.2.label",
            # home.age_groups (dict 3 · 4 cols IN)
            "home.age_groups.0.range",
            "home.age_groups.2.blurb",
            # home.doctors (dict 4 · 5 cols · portrait image)
            "home.doctors.0.name",
            "home.doctors.3.portrait",                 # image cell
            # home.journey_steps (dict 5 · 3 cols)
            "home.journey_steps.0.age",
            "home.journey_steps.4.desc",
            # home.faq (tuple 8 · 2 cols)
            "home.faq.0.q",
            "home.faq.7.a",
            # home.gallery (dict 5 · 2 cols · src image · novel col name)
            "home.gallery.0.cap",
            "home.gallery.4.src",                      # image cell · novel col
            # home.hours (tuple 4 · 2 cols)
            "home.hours.0.day",
            "home.hours.3.value",
            # studio.values (dict 4 · 3 cols)
            "studio.values.0.title",
            "studio.values.3.desc",
            # studio.history (tuple 4 · 2 cols)
            "studio.history.0.year",
            "studio.history.3.desc",
            # visite.visits (dict 8 · 7 cols)
            "visite.visits.0.title",
            "visite.visits.7.desc",
            # visite.tips (dict 3 · 2 cols)
            "visite.tips.0.title",
            "visite.tips.2.text",
            # crescita.topics (parent dict 4 · 4 cols IN)
            "crescita.topics.0.meta",
            "crescita.topics.3.title",
            # crescita.topics.{i}.items (deep-path tuple · 4 × 4 × 2 = 32 cells)
            "crescita.topics.0.items.0.q",             # deep-path cell
            "crescita.topics.0.items.3.a",             # deep-path last tuple
            "crescita.topics.3.items.0.q",             # deep-path last topic
            "crescita.topics.3.items.3.a",
            # crescita.materials (dict 3 · 4 cols)
            "crescita.materials.0.title",
            "crescita.materials.2.dl_label",
            # pediatre.doctors (dict 4 · 8 cols IN · portrait)
            "pediatre.doctors.0.name",
            "pediatre.doctors.3.portrait",             # image cell
            # contatti.travel (dict 3 · 3 cols)
            "contatti.travel.0.icon",
            "contatti.travel.2.text",
            # contatti.hours (tuple 4 · 2 cols)
            "contatti.hours.0.day",
            "contatti.hours.3.value",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Famiglia",
            )

    def test_a16c_family_supported_locales_returns_canonical_five(self):
        """Famiglia ships the canonical 5-locale set. Step-0 audit
        confirmed 5-locale parity PERFECT (376 keys × 5 · zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("family"),
            ["it", "en", "fr", "es", "ar"],
        )

    def test_a16c_sixteenfold_regression_after_family_joins(self):
        """Regression guard: the 16 pre-A.16c archetype classifications
        (14 pre-A.16 + Salute + Benessere) are unchanged after `family`
        joins the gate."""
        from apps.editor.schema import (
            is_translatable, supported_locales, _MULTILOCALE_ENABLED_ARCHETYPES,
        )
        pre_a16c = (
            "agency-creative-studio",
            "corporate-suite",
            "fine-dining",
            "specialist",
            "classic-gold",
            "modern-transparent",
            "mass-market",
            "ultra-luxury-cinematic",
            "editorial-designer-grid",
            "cinematic-photographer",
            "trattoria-warm",
            "street-modern",
            "artisan-workshop",
            "fashion-editorial",
            "clinic",
            "wellness",
        )
        for arc in pre_a16c:
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} lost multi-locale enrollment")
            self.assertEqual(
                supported_locales(arc), ["it", "en", "fr", "es", "ar"],
                f"{arc} supported_locales regressed",
            )

    def test_a16c_family_clinic_admin_boundary(self):
        """USER-IMPOSED LIGHT guardrail (mirrors A.16/A.16b clinic-admin
        boundary · 3rd medical-other archetype to confirm boundary
        uniform across the family): the editor schema for Famiglia must
        not leak into scheduler/booking/patient/calendar-slot/etc.
        namespaces. Schema stays scoped to the registry content
        (template_content prefixes: home/studio/visite/crescita/pediatre/
        contatti/site)."""
        from apps.editor.schema import iter_editable_fields
        arc = "family"
        admin_model_prefixes = (
            "appointment.", "booking.", "patient.", "scheduler.",
            "calendar_slot.", "medical_record.", "prescription.",
        )
        for path, _spec in iter_editable_fields(arc):
            for prefix in admin_model_prefixes:
                self.assertFalse(
                    path.startswith(prefix),
                    f"Editor schema leaks into pseudo-admin namespace: "
                    f"field `{path}` starts with `{prefix}` — editor must "
                    f"stay on template_content registry only"
                )

    def test_a16c_family_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.16/A.16b bridge-guard — Famiglia
        `medical/family/_base.html` must integrate the three bridge
        points together on the `.fm-*` skin: (1) preview-bridge.js
        conditional on ``preview_project``, (2) ``<title>`` honors
        ``site.logo_word``, (3) ``<body>`` carries ``mw-is-editor-preview``
        guard class when inside the editor."""
        famiglia = WebTemplate.objects.get(slug="famiglia-pediatria")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/medical/famiglia-pediatria/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=famiglia)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A16c Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/medical/famiglia-pediatria/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A16c Bridge Check", body_proj)
        self.assertIn('<body class="mw-is-editor-preview"', body_proj)

    # ------------------------------------------------------------------
    # A.17 · Aura (agency-digital-studio · agency-secondary family ·
    # single-template closure) enrollment — Step 1 contract.
    # **CLOSES the agency-secondary family** (single-template · first
    # single-template family closure with a single phase). 6th family
    # closed (after law · medical-specialist · real-estate · portfolio ·
    # restaurant-continuation · ecommerce · medical-other — reaching 8
    # families closed total · only startup-saas remains for A.17b).
    # 18 readonly indexed list entries · 12 image-in-dict-row cells ·
    # zero deep-path · zero scalar top-level image · zero novel shape.
    # Posts list (6 project_detail records) stays registry-only · 7th
    # uniform enforcement of the per-item content policy. Form-scaffolding
    # on brief page OUT entire (step1/2/3 · labels · placeholders ·
    # scope_options · slots) · 5th form-structure OUT precedent.
    # ------------------------------------------------------------------

    def test_a17_aura_archetype_registered(self):
        """`agency-digital-studio` joins the supported-archetype registry
        and the multi-locale gate. All 17 pre-A.17 archetypes must still
        be enrolled (seventeen-fold regression).
        """
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS,
            _MULTILOCALE_ENABLED_ARCHETYPES,
            is_supported_archetype,
            supported_locales,
        )
        self.assertIn("agency-digital-studio", _ARCHETYPE_SCHEMAS)
        self.assertIn("agency-digital-studio", _MULTILOCALE_ENABLED_ARCHETYPES)
        self.assertTrue(is_supported_archetype("agency-digital-studio"))
        self.assertEqual(
            supported_locales("agency-digital-studio"),
            ["it", "en", "fr", "es", "ar"],
        )
        # 17 pre-A.17 archetypes still enrolled.
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop", "fashion-editorial",
            "clinic", "wellness", "family",
        ):
            self.assertIn(arc, _ARCHETYPE_SCHEMAS,
                          f"{arc} must stay enrolled after A.17 Aura joins")
            self.assertIn(arc, _MULTILOCALE_ENABLED_ARCHETYPES,
                          f"{arc} must stay in multi-locale gate after A.17")

    def test_a17_aura_out_guard_was_removed_from_prior_tests(self):
        """A.17 rotates the outside-gate fixture from `agency-digital-
        studio`/Aura (now enrolled · CLOSES agency-secondary family) to
        `startup-saas-landing`/Elevate (LAST non-enrolled archetype ·
        will close with A.17b). Verifies the 7 rotated call-sites no
        longer name Aura as outside-gate (7th precedent of guard removal
        pattern · extends 6-precedent chain from A.16c).
        """
        from apps.editor.schema import is_supported_archetype, is_translatable, supported_locales
        # Aura must be IN after A.17.
        self.assertTrue(is_supported_archetype("agency-digital-studio"),
                        "Aura must be enrolled after A.17 closer")
        self.assertTrue(is_translatable("agency-digital-studio", "home.headline"))
        self.assertEqual(
            supported_locales("agency-digital-studio"),
            ["it", "en", "fr", "es", "ar"],
        )
        # Elevate is the new outside-gate reference.
        self.assertFalse(is_supported_archetype("startup-saas-landing"))
        self.assertFalse(is_translatable("startup-saas-landing", "home.headline"))
        self.assertEqual(supported_locales("startup-saas-landing"), [])

    def test_a17_agency_secondary_family_closed(self):
        """A.17 CLOSES agency-secondary family with a single phase ·
        first single-template family closure precedent. Vertex sits in
        agency-creative-studio (primary) · Aura in agency-digital-
        studio (secondary) · both now editable. 8 families closed
        total after A.17 (law · medical-specialist · real-estate ·
        portfolio · restaurant-continuation · ecommerce · medical-other
        · agency-secondary)."""
        from apps.editor.schema import _ARCHETYPE_SCHEMAS
        # Both agency archetypes enrolled.
        self.assertIn("agency-creative-studio", _ARCHETYPE_SCHEMAS,
                      "Vertex (agency-creative-studio) must stay enrolled")
        self.assertIn("agency-digital-studio", _ARCHETYPE_SCHEMAS,
                      "Aura (agency-digital-studio) must be enrolled after A.17")

    def test_a17_aura_schema_shape_covers_all_pages(self):
        """Aura schema surfaces at least one group for every customer-
        facing page (9 groups · one per page region + overlapping
        chrome/console/home_bands trio)."""
        from apps.editor.schema import _ARCHETYPE_SCHEMAS
        schema = _ARCHETYPE_SCHEMAS["agency-digital-studio"]
        group_ids = {g["id"] for g in schema}
        for expected in (
            "brand", "hero_home", "console_home", "home_bands",
            "studio_page", "capabilities_page", "lavori_page",
            "sprint_page", "brief_page",
        ):
            self.assertIn(expected, group_ids,
                          f"Aura schema missing expected group `{expected}`")

    def test_a17_aura_is_translatable_text_fields(self):
        """Customer-editable text fields that are NOT under a structured
        list are per-locale-translatable. Universals (logo · phone ·
        email · address · license) stay global."""
        from apps.editor.schema import is_translatable
        arc = "agency-digital-studio"
        translatable_samples = (
            "home.headline",
            "home.intro",
            "home.console.primary_label",
            "studio.standfirst",
            "capabilities.headline",
            "lavori.velocity_body",
            "sprint.standfirst",
            "brief.async_body",
        )
        for path in translatable_samples:
            self.assertTrue(
                is_translatable(arc, path),
                f"{path} must be per-locale translatable on Aura",
            )

    def test_a17_aura_branding_and_contact_universals_are_global(self):
        """site.* universals in _GLOBAL_TEXT_PATHS stay plain-key global
        (D-098 policy · 18 enrolled archetypes uniform). Select-type
        routing fields (inquiry_page_slug) also stay global by virtue
        of their non-translatable field type."""
        from apps.editor.schema import is_translatable
        arc = "agency-digital-studio"
        global_paths = (
            # _GLOBAL_TEXT_PATHS entries (force plain-key regardless of
            # text-type classification)
            "site.logo_word",
            "site.phone",
            "site.email",
            "site.address",
            "site.license",
            # Select type · not translatable by field-type rule
            "site.inquiry_page_slug",
            "home.primary_href",
            "home.secondary_href",
        )
        for path in global_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} must stay global on Aura",
            )

    def test_a17_aura_image_cells_in_dict_rows_exposed(self):
        """USER-IMPOSED GUARDRAIL: Aura ships 12 image cells across 3
        image-in-dict-row lists (no scalar top-level · no deep-path):
          • home.work_cards[].cover      × 3 rows
          • studio.team[].portrait       × 3 rows
          • lavori.projects[].cover      × 6 rows
        All 12 image cells rendered via `.au-*` skin. Posts cover_image
        × 6 stays registry-only (7th uniform enforcement of per-item
        content policy)."""
        from apps.editor.schema import get_field_spec
        arc = "agency-digital-studio"
        image_cell_paths = (
            # home.work_cards × 3 (cover col)
            "home.work_cards.0.cover",
            "home.work_cards.2.cover",
            # studio.team × 3 (portrait col)
            "studio.team.0.portrait",
            "studio.team.2.portrait",
            # lavori.projects × 6 (cover col)
            "lavori.projects.0.cover",
            "lavori.projects.5.cover",
        )
        for path in image_cell_paths:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Aura schema")
            self.assertEqual(spec.get("type"), "image",
                             f"{path} must expose as type=image")

    def test_a17_aura_visible_catalog_fields_kept_in(self):
        """Stringent IN call (audit-driven · 8th archetype precedent
        chain): visible editorial technical-looking labels stay IN.
        Aura brings `foot_boot_line`, `foot_current_sprint`, `sprint_chip`
        (navbar chip), `output` tag on home.sprints rows (editorial
        `OUT · brief + backlog`), `tagline` on sprint.sprints (editorial
        `// output: ...`), `deliverables_label`, `scope_label`."""
        from apps.editor.schema import get_field_spec, validate_key_path
        arc = "agency-digital-studio"
        visible_editorial = (
            "site.foot_boot_line",
            "site.foot_current_sprint",
            "site.sprint_chip",
            "site.foot_shiplog_label",
            "site.foot_studio_label",
            "site.foot_stack_label",
            # Structured-list cells (IN col-level)
            "home.sprints.0.output",
            "sprint.sprints.0.tagline",
            "sprint.sprints.0.deliverables_label",
            "capabilities.capabilities.0.scope_label",
        )
        for path in visible_editorial:
            spec = get_field_spec(arc, path)
            self.assertIsNotNone(spec, f"{path} missing from Aura schema")
            # Must also pass validate_key_path (IN perimeter).
            validate_key_path(arc, path)

    def test_a17_aura_brief_slots_kept_out_explicit(self):
        """**AUDIT-BINDING · explicit A.17 Step 0 decision**:
        `brief.slots` is OUT entire · form-structure scaffolding ·
        5th form-structure OUT precedent after Gusto/Juris/Casa/Villa.

        Rationale: the tuple `(id, label)` holds a form-option-value
        `id` (structural form-schema · e.g. "mon10") and an editorial
        label ("Lun · 10:00"). Despite the label being customer-visible,
        the LIST IDENTITY — which days/hours are offered — is a form-
        schema concern requiring a calendar integration, not a customer
        copy edit. Enforced by:
          (a) `brief.slots` is NOT registered in STRUCTURED_FIELD_SHAPES
              (list-level OUT · no per-cell editor exposure)
          (b) `brief.slots` + sub-paths raise InvalidEditableField
          (c) Sibling form-structure containers (step1/2/3 · labels ·
              placeholders · scope_options) are similarly OUT entire
        """
        from apps.editor.schema import (
            STRUCTURED_FIELD_SHAPES,
            InvalidEditableField,
            validate_key_path,
        )
        arc = "agency-digital-studio"
        # (a) slots NOT registered as structured-list shape
        shapes = STRUCTURED_FIELD_SHAPES.get(arc, {})
        self.assertNotIn("brief.slots", shapes,
                         "brief.slots must stay OUT entire · 5th form-structure precedent")
        # (b) slots + sub-paths raise InvalidEditableField
        for out_path in (
            "brief.slots",
            "brief.slots.0",
            "brief.slots.0.0",          # tuple id
            "brief.slots.0.1",          # tuple label
            "brief.slots.0.id",         # defensive alias
            "brief.slots.0.label",      # defensive alias
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"brief.slots path must stay rejected: {out_path}",
            ):
                validate_key_path(arc, out_path)
        # (c) sibling form-structure containers OUT entire
        for out_path in (
            "brief.step1",
            "brief.step1.title",
            "brief.step2",
            "brief.step3",
            "brief.labels",
            "brief.labels.name",
            "brief.placeholders",
            "brief.placeholders.brief",
            "brief.scope_options",
            "brief.scope_options.0",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"brief form-structure path must stay rejected: {out_path}",
            ):
                validate_key_path(arc, out_path)

    def test_a17_aura_complex_shapes_excluded_from_perimeter(self):
        """Nested list-of-str inside dict rows, flat list-of-str, and
        registry-only posts list all rejected by validate_key_path ·
        6-archetype nested-list-of-str precedent chain + 7th uniform
        enforcement of per-item content policy (posts)."""
        from apps.editor.schema import InvalidEditableField, validate_key_path
        arc = "agency-digital-studio"
        out_paths = (
            # Nested list-of-str inside dict rows (Juris precedent · OUT col-level)
            "home.capab_cards.0.tags",
            "home.capab_cards.0.tags.0",
            "home.work_cards.0.stack",
            "home.work_cards.0.stack.0",
            "studio.team.0.stack",
            "capabilities.capabilities.0.scope",
            "capabilities.capabilities.0.scope.0",
            "capabilities.capabilities.0.stack",
            "capabilities.engagement_tiles.0.includes",
            # Nested list-of-tuple kpi inside lavori.projects (no sub-list kind)
            "lavori.projects.0.kpi",
            "lavori.projects.0.kpi.0",
            # bool flag `featured` on engagement_tiles (OUT-category)
            "capabilities.engagement_tiles.0.featured",
            # Flat list-of-str · OUT entire
            "site.foot_stack_marquee",
            "site.foot_stack_marquee.0",
            "site.foot_stack_rows",
            "site.foot_stack_rows.0",
            "studio.story_paragraphs",
            "studio.story_paragraphs.0",
            "lavori.tabs",
            "lavori.tabs.0",
            "brief.scope_options",
            "brief.scope_options.0",
            # Structural slug identifiers (router refs) · OUT
            "home.work_cards.0.slug",
            "lavori.projects.0.slug",
            # Deliverables nested list-of-str · OUT col-level
            "sprint.sprints.0.deliverables",
            "sprint.sprints.0.deliverables.0",
            # Posts registry-only · 7th uniform enforcement
            "posts",
            "posts.0",
            "posts.0.title",
            "posts.0.cover_image",
            "posts.0.problem_paragraphs",
            "posts.0.timeline_steps",
            # Pages list + DNA-locked
            "pages",
            "pages.0.slug",
        )
        for path in out_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Aura OUT path must stay rejected: {path}",
            ):
                validate_key_path(arc, path)

    def test_a17_aura_structured_list_cells_are_global(self):
        """Every STRUCTURED_FIELD_SHAPES text/image cell on Aura stays
        global (non-translatable · D-098 structured-list policy · 18
        enrolled archetypes uniform · zero deep-path for Aura)."""
        from apps.editor.schema import is_translatable
        arc = "agency-digital-studio"
        cell_paths = (
            # site.foot_shiplog_rows (tuple 6 · 3 cols)
            "site.foot_shiplog_rows.0.date",
            "site.foot_shiplog_rows.5.desc",
            # home.hero_metrics (tuple 3 · 2 cols)
            "home.hero_metrics.0.num",
            "home.hero_metrics.2.label",
            # home.console.kpi (tuple 4 · 2 cols · nested under console dict)
            "home.console.kpi.0.num",
            "home.console.kpi.3.label",
            # home.capab_cards (dict 4 · 3 cols IN)
            "home.capab_cards.0.id",
            "home.capab_cards.3.body",
            # home.sprints (dict 4 · 5 cols IN incl output stringent)
            "home.sprints.0.id",
            "home.sprints.3.output",
            # home.work_cards (dict 3 · 5 cols · cover image)
            "home.work_cards.0.title",
            "home.work_cards.2.cover",
            # home.metric_strip (tuple 4 · 3 cols)
            "home.metric_strip.0.num",
            "home.metric_strip.3.note",
            # studio.facts (tuple 4 · 3 cols)
            "studio.facts.0.num",
            "studio.facts.3.note",
            # studio.team (dict 3 · 4 cols · portrait image)
            "studio.team.0.name",
            "studio.team.2.portrait",
            # studio.values (tuple 4 · 3 cols)
            "studio.values.0.id",
            "studio.values.3.body",
            # capabilities.capabilities (dict 4 · 5 cols IN · scope/stack excluded)
            "capabilities.capabilities.0.id",
            "capabilities.capabilities.3.scope_label",
            # capabilities.engagement_tiles (dict 3 · 4 cols IN)
            "capabilities.engagement_tiles.0.title",
            "capabilities.engagement_tiles.2.body",
            # lavori.projects (dict 6 · 7 cols · cover image · slug/kpi excluded)
            "lavori.projects.0.id",
            "lavori.projects.5.cover",
            # lavori.velocity_stats (tuple 4 · 2 cols)
            "lavori.velocity_stats.0.num",
            "lavori.velocity_stats.3.label",
            # sprint.sprints (dict 4 · 6 cols IN · deliverables excluded)
            "sprint.sprints.0.tagline",
            "sprint.sprints.3.deliverables_label",
            # sprint.mindset_cards (dict 3 · 3 cols)
            "sprint.mindset_cards.0.title",
            "sprint.mindset_cards.2.body",
            # sprint.stack_tiles (dict 8 · 2 cols)
            "sprint.stack_tiles.0.category",
            "sprint.stack_tiles.7.list",
            # brief.response_rows (tuple 4 · 2 cols)
            "brief.response_rows.0.label",
            "brief.response_rows.3.value",
        )
        for path in cell_paths:
            self.assertFalse(
                is_translatable(arc, path),
                f"{path} structured-list cell must stay global on Aura",
            )

    def test_a17_aura_supported_locales_returns_canonical_five(self):
        """Aura ships the canonical 5-locale set. Step-0 audit confirmed
        5-locale parity PERFECT (544 keys × 5 locales · zero gaps)."""
        from apps.editor.schema import supported_locales
        self.assertEqual(
            supported_locales("agency-digital-studio"),
            ["it", "en", "fr", "es", "ar"],
        )
        # Outside-gate reference: startup-saas-landing (Elevate)
        # after A.17 rotated it from agency-digital-studio/Aura
        # (now enrolled · CLOSES agency-secondary family).
        self.assertEqual(supported_locales("startup-saas-landing"), [])

    def test_a17_seventeenfold_regression_after_aura_joins(self):
        """Enrolling Aura must not affect the pre-A.17 17 archetypes.
        Sample spot-checks across each family:
        - agency-creative-studio (Vertex · A.6 · agency-primary)
        - corporate-suite (Pragma · A.7b · business)
        - fine-dining (Gusto · A.8 · restaurant-primary)
        - specialist (Cardio+Derm shared · A.9 · medical-specialist CLOSED)
        - classic-gold + modern-transparent (A.10+A.11 · law CLOSED)
        - mass-market + ultra-luxury-cinematic (A.12+A.12b · real-estate CLOSED)
        - editorial-designer-grid + cinematic-photographer (A.13+A.13b · portfolio CLOSED)
        - trattoria-warm + street-modern (A.14+A.14b · restaurant-continuation CLOSED)
        - artisan-workshop + fashion-editorial (A.15+A.15b · ecommerce CLOSED)
        - clinic + wellness + family (A.16+A.16b+A.16c · medical-other CLOSED)
        """
        from apps.editor.schema import (
            _ARCHETYPE_SCHEMAS,
            is_supported_archetype,
            is_translatable,
            supported_locales,
        )
        samples = (
            ("agency-creative-studio",   "home.headline",    "vertex-creative-agency"),
            ("corporate-suite",          "home.headline",    "pragma-corporate-suite"),
            ("fine-dining",              "home.headline",    "gusto-fine-dining"),
            ("specialist",               "home.headline",    "cardio-studio-specialistico"),
            ("classic-gold",             "home.headline",    "lex-studio-legale"),
            ("modern-transparent",       "home.headline",    "juris-avvocato-moderno"),
            ("mass-market",              "home.headline",    "casa-agenzia-immobiliare"),
            ("ultra-luxury-cinematic",   "home.headline",    "villa-immobili-lusso"),
            ("editorial-designer-grid",  "home.headline",    "chiara-portfolio-creativo"),
            ("cinematic-photographer",   "home.headline",    "pixel-portfolio-fotografico"),
            ("trattoria-warm",           "home.headline",    "sapore-trattoria-pizzeria"),
            ("street-modern",            "home.headline",    "brace-street-food-lab"),
            ("artisan-workshop",         "home.headline",    "bottega-artisan-workshop"),
            ("fashion-editorial",        "home.headline",    "luxe-boutique-fashion"),
            ("clinic",                   "home.headline",    "salute-studio-medico"),
            ("wellness",                 "home.headline",    "benessere-centro-olistico"),
            ("family",                   "home.headline",    "famiglia-pediatria"),
        )
        for arc, path, slug in samples:
            self.assertIn(arc, _ARCHETYPE_SCHEMAS,
                          f"{arc} (slug {slug}) must stay enrolled after A.17")
            self.assertTrue(is_supported_archetype(arc))
            self.assertTrue(is_translatable(arc, path),
                            f"{arc}.{path} must stay translatable after A.17")
            self.assertEqual(
                supported_locales(arc),
                ["it", "en", "fr", "es", "ar"],
                f"{arc} must stay in 5-locale gate after A.17",
            )

    def test_a17_aura_posts_stay_registry_only(self):
        """USER-IMPOSED GUARDRAIL: Aura's posts list (6 project_detail
        records · cover_image × 6) stays registry-only · 7th uniform
        enforcement of the per-item content policy (after Chiara +
        Pixel + Sapore + Brace + Bottega + Luxe). Project_detail kind
        is served via `lavori/<slug>/` from posts[] but the detail
        content is NOT exposed in the editor. This keeps detail-page
        editing deferred until a horizontal feature lifts the policy
        across the 7-archetype chain in one shot."""
        from apps.editor.schema import InvalidEditableField, validate_key_path
        arc = "agency-digital-studio"
        posts_paths = (
            "posts",
            "posts.0",
            "posts.0.title",
            "posts.0.client",
            "posts.0.cover_image",
            "posts.0.problem_heading",
            "posts.0.problem_paragraphs",
            "posts.0.solution_heading",
            "posts.0.timeline_steps",
            "posts.0.results_stats",
            "posts.0.quote",
            "posts.5.cover_image",      # last of 6 posts
        )
        for path in posts_paths:
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Aura posts-registry path must stay rejected: {path}",
            ):
                validate_key_path(arc, path)

    def test_a17_aura_preview_bridge_injected_only_with_preview_project(self):
        """Mirror of the A.16/A.16b/A.16c bridge-guard — Aura
        `agency/agency-digital-studio/_base.html` must integrate the
        three bridge points together on the `.au-*` skin:
        (1) preview-bridge.js conditional on ``preview_project``,
        (2) ``<title>`` honors ``site.logo_word``,
        (3) ``<body>`` carries ``mw-is-editor-preview`` guard class
            when inside the editor iframe."""
        aura = WebTemplate.objects.get(slug="aura-digital-studio")
        # ── 1. Bare public preview (no project) ───────────────────
        self.client.logout()
        r_bare = self.client.get("/templates/agency/aura-digital-studio/preview/")
        self.assertEqual(r_bare.status_code, 200)
        body_bare = r_bare.content.decode("utf-8", "ignore")
        self.assertNotIn("editor/preview-bridge.js", body_bare)
        import re as _re
        body_tag = _re.search(r"<body[^>]*>", body_bare)
        self.assertIsNotNone(body_tag)
        self.assertNotIn("mw-is-editor-preview", body_tag.group(0))

        # ── 2. Editor-embedded preview (with project) ─────────────
        self.client.login(username="owner", password="x")
        p = services.create_project_from_template(owner=self.owner, template=aura)
        services.save_content_edits(
            project=p, editor=self.owner,
            edits={"site.logo_word": "A17 Bridge Check"},
        )
        r_proj = self.client.get(
            f"/templates/agency/aura-digital-studio/preview/?project={p.uuid}"
        )
        self.assertEqual(r_proj.status_code, 200)
        body_proj = r_proj.content.decode("utf-8", "ignore")
        self.assertIn("editor/preview-bridge.js", body_proj)
        self.assertIn("<title>A17 Bridge Check", body_proj)
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
        # `startup-saas-landing` (Elevate) is the current outside-gate
        # reference (A.17 rotated it from `agency-digital-studio`/Aura
        # which is now enrolled · CLOSES agency-secondary family).
        self.assertEqual(supported_locales("startup-saas-landing"), [])

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
        # elevate-startup-landing (startup-saas-landing archetype) is
        # not yet enrolled. A.17 rotated the outside-gate reference
        # from Aura (agency-digital-studio · now enrolled · CLOSES
        # agency-secondary) to Elevate (startup-saas-landing · still
        # out · LAST non-enrolled archetype). Swap when `startup-saas-
        # landing` receives editor support (A.17b).
        r = self.client.get("/projects/start/?template=elevate-startup-landing")
        self.assertEqual(r.status_code, 302)
        # Either /templates/business/elevate-startup-landing/ or template_list — both accept.
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

    # ------------------------------------------------------------------
    # A.13 · Step 2 — Chiara (editorial-designer-grid) lifecycle HTTP
    # cross-cutting · covers scalar nested-dict image + image-in-dict-row
    # at deep path 2 levels (third precedent after Vertex + Villa).
    # Posts/detail-page editing stays registry-only per consistent
    # perimeter policy applied to Lex/Juris/Casa/Villa.
    # ------------------------------------------------------------------

    def test_a13_chiara_full_multilocale_lifecycle_end_to_end(self):
        """Mirror of the A.12b Villa lifecycle, adapted to Chiara's
        image surface shape:

        1. customer edits IT / EN / FR on a Chiara translatable path
        2. customer edits a global TEXT path (site.logo_word)
        3. customer edits a SCALAR IMAGE field nested inside a parent
           dict (studio.founder.image · Vertex home.cover.image
           precedent)
        4. customer edits an IMAGE CELL inside a list-of-dict at DEEP
           PATH 2 levels (home.featured_works.items.0.image · third
           precedent after Vertex studio.partners[].portrait and
           Villa home.signature/territories/advisors[].image)
        5. unedited locales (ES · AR) fall back to the authored registry
        6. project publishes · second user visits every public preview
           locale and sees the correct content + both image overrides
        7. owner reopens the editor per locale and the sidebar prefill
           matches buffer for that locale

        AR response head must carry ``<html dir="rtl" lang="ar">`` on
        the `.ed-*` skin (the prefix collides with the editor sidebar
        namespace but lives in a different DOM tree · no functional
        conflict · verified Step-0). **Posts/detail-page editing is NOT
        exercised here** — it's a coherent perimeter decision
        consistent with Lex/Juris/Casa/Villa per-item content policy,
        deferred to a future horizontal phase if customer signal emerges.
        The Pixel-out runtime guard that lived here until A.13 was
        removed in A.13b together with Pixel's own registrations.
        """
        import json as _json

        chiara = WebTemplate.objects.get(slug="chiara-portfolio-creativo")
        p = services.create_project_from_template(owner=self.owner, template=chiara)

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
            ("it", "Forme Chiara walk IT <em>A13Chiara</em>."),
            ("en", "Forms Chiara walk EN <em>A13ChiaraEN</em>."),
            ("fr", "Formes Chiara walk FR <em>A13ChiaraFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])
        r = autosave("en", {"site.logo_word": "A13ChiaraBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 3. Scalar image override (nested-dict scalar · Vertex
        # `home.cover.image` precedent) ────────────────────────────
        # `studio.founder.image` lives inside the `studio.founder`
        # parent dict — Vertex `home.cover.image` shape. Image fields
        # are classified NON-translatable so the override persists with
        # a plain key regardless of the request locale tag.
        IMG_FOUNDER = "https://walk-chiara.example/img/founder-A13.jpg"
        r = autosave("it", {"studio.founder.image": IMG_FOUNDER})
        self.assertEqual(r.status_code, 200)
        self.assertIn("studio.founder.image", r.json()["content_keys"])

        # ── 4. Image-in-dict-row override at DEEP PATH 2 levels ────
        # `home.featured_works.items.0.image` — third precedent of
        # image-in-dict-row after Vertex studio.partners[].portrait
        # and Villa home.signature/territories/advisors[].image.
        # Path is 2 levels deep through the `home.featured_works`
        # parent dict. `_resolve_path` walks any depth.
        IMG_FEATURED0 = "https://walk-chiara.example/img/featured-row0-A13.jpg"
        r = autosave("it", {"home.featured_works.items.0.image": IMG_FEATURED0})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.featured_works.items.0.image", r.json()["content_keys"])

        # Storage keys: 3 @<locale>:home.headline (per-locale) + 3
        # plain-keyed globals (logo + 2 images including the deep-path
        # image cell). No leak of image overrides into @<locale>:
        # namespace · no plain-key leak for home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("studio.founder.image", keys)
        self.assertIn("home.featured_works.items.0.image", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@it:studio.founder.image", keys)
        self.assertNotIn("@it:home.featured_works.items.0.image", keys)
        self.assertNotIn("@en:site.logo_word", keys)

        # ── 5. publish ────────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 6. second user sees the right thing on every locale ───
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            # page=None fetches home via live_template_home; page='studio'
            # etc. fetches a specific sub-page. Images live on different
            # pages (home.featured_works on home, studio.founder on
            # studio), so image assertions need page-specific fetches.
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/portfolio/chiara-portfolio-creativo/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override visible, EN/FR markers absent.
        # Global logo + home-scoped image (featured_works) visible.
        body_it = preview_body("it")
        self.assertIn("Chiara walk IT", body_it)
        self.assertIn("A13Chiara", body_it)
        self.assertNotIn("A13ChiaraEN", body_it)
        self.assertNotIn("A13ChiaraFR", body_it)
        self.assertIn("A13ChiaraBrand", body_it)
        # home.featured_works.items.0.image is a home-scoped asset.
        self.assertIn(IMG_FEATURED0, body_it)

        # IT render (studio page) — studio.founder.image visible here.
        body_it_studio = preview_body("it", page="studio")
        self.assertIn("A13ChiaraBrand", body_it_studio)
        self.assertIn(IMG_FOUNDER, body_it_studio)

        # EN render (home)
        body_en = preview_body("en")
        self.assertIn("Chiara walk EN", body_en)
        self.assertIn("A13ChiaraEN", body_en)
        self.assertNotIn("Chiara walk IT", body_en)
        self.assertIn("A13ChiaraBrand", body_en)
        self.assertIn(IMG_FEATURED0, body_en)
        # Studio-scoped image check on EN studio page.
        body_en_studio = preview_body("en", page="studio")
        self.assertIn(IMG_FOUNDER, body_en_studio)

        # FR render (home) + studio spot check
        body_fr = preview_body("fr")
        self.assertIn("Chiara walk FR", body_fr)
        self.assertIn("A13ChiaraFR", body_fr)
        self.assertIn("A13ChiaraBrand", body_fr)
        self.assertIn(IMG_FEATURED0, body_fr)
        body_fr_studio = preview_body("fr", page="studio")
        self.assertIn(IMG_FOUNDER, body_fr_studio)

        # Unedited locales — authored text fallback + global images universal.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Chiara walk IT", body)
            self.assertNotIn("Chiara walk EN", body)
            self.assertNotIn("Chiara walk FR", body)
            self.assertIn("A13ChiaraBrand", body)
            # Home-scoped image override persists across unedited locales.
            self.assertIn(IMG_FEATURED0, body)
            # Studio-scoped image override on studio page too.
            body_studio = preview_body(locale, page="studio")
            self.assertIn(IMG_FOUNDER, body_studio)
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Chiara home",
                )

        # AR preview (home) — `.ed-*` skin must emit ``<html dir="rtl" lang="ar">``.
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
            ("it", "Chiara walk IT"),
            ("en", "Chiara walk EN"),
            ("fr", "Chiara walk FR"),
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
        self.assertIsNotNone(logo_field, "site.logo_word missing from Chiara editor")
        self.assertEqual(logo_field["value"], "A13ChiaraBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        # Nested-dict scalar image: overridden universally, not translatable.
        founder_img_field = find_field_by_key(r_es.context["groups"], "studio.founder.image")
        self.assertIsNotNone(founder_img_field,
                             "studio.founder.image missing from Chiara editor")
        self.assertEqual(founder_img_field["value"], IMG_FOUNDER)
        self.assertTrue(founder_img_field["is_overridden"])
        self.assertFalse(founder_img_field["translatable"])

    # ------------------------------------------------------------------
    # A.13b · Step 2 — Pixel (cinematic-photographer) lifecycle HTTP
    # cross-cutting · closes portfolio family via D-098 staged
    # dedicated-schema progression (Chiara open in A.13 · Pixel closes
    # in A.13b). Single top-level scalar image (home.hero_image) ·
    # posts/series_detail stay registry-only per consistent perimeter
    # policy shared with Lex/Juris/Casa/Villa/Chiara.
    # ------------------------------------------------------------------

    def test_a13b_pixel_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Pixel enrollment:

        1. customer edits IT / EN / FR on a Pixel translatable path
           (home.headline)
        2. customer edits a global TEXT path (site.logo_word) via EN
           autosave — storage MUST be plain-keyed (no @en: prefix)
        3. customer edits the single scalar IMAGE field
           (home.hero_image · top-level scalar, NOT nested-dict like
           Chiara studio.founder.image) — storage MUST be plain-keyed
           (no @<locale>: prefix on image overrides)
        4. project publishes via services.publish_project
        5. second user visits every public preview locale:
           - IT/EN/FR render their locale override + global logo + image
           - ES/AR fall back to the authored registry text, still see
             the global logo + image override (images are universal)
           - AR response head carries ``<html dir="rtl" lang="ar">``
             on the ``.cp-*`` skin
        6. owner reopens the editor per locale; sidebar prefill matches
           the buffer for that locale on home.headline and shows
           site.logo_word + home.hero_image as universal overrides
        7. perimeter invariants double-checked at the end of the walk:
           Chiara stays enrolled, posts.* and series_detail stay
           rejected by validate_key_path (5-archetype uniform policy).

        Explicitly NOT exercised here: posts override (perimeter OUT),
        repeater mutations (Pixel lists are all readonly), image
        per-locale (out of scope D-098), editor JS/CSS shell touches.
        """
        import json as _json

        pixel = WebTemplate.objects.get(slug="pixel-portfolio-fotografico")
        p = services.create_project_from_template(owner=self.owner, template=pixel)

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

        # ── 1. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Luce Pixel walk IT <em>A13bPixel</em>."),
            ("en", "Light Pixel walk EN <em>A13bPixelEN</em>."),
            ("fr", "Lumière Pixel walk FR <em>A13bPixelFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 2. global plain-keyed text — site.logo_word via EN ────
        # Image/global scalars must NOT pick up the @en: prefix even
        # when written inside an EN-tagged autosave.
        r = autosave("en", {"site.logo_word": "A13bPixelBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 3. scalar image override — home.hero_image ────────────
        # Top-level scalar image (Villa home.cover_image shape, not
        # Chiara nested-dict studio.founder.image shape). Images are
        # classified NON-translatable — persistence is plain-keyed
        # regardless of the request-tagged locale.
        IMG_HERO = "https://walk-pixel.example/img/hero-A13b.jpg"
        r = autosave("it", {"home.hero_image": IMG_HERO})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.hero_image", r.json()["content_keys"])

        # Storage shape: 3 @<locale>:home.headline + 2 plain-keyed
        # globals (logo + hero image). Zero @<locale>: on the image
        # path; zero @en: on the logo path; zero plain-key leak on
        # home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("home.hero_image", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        self.assertNotIn("@it:home.hero_image", keys)
        self.assertNotIn("@en:home.hero_image", keys)
        self.assertNotIn("@fr:home.hero_image", keys)
        self.assertNotIn("@es:home.hero_image", keys)
        self.assertNotIn("@ar:home.hero_image", keys)

        # ── 4. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 5. second user on every public preview locale ────────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/portfolio/pixel-portfolio-fotografico/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override visible, EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Pixel walk IT", body_it)
        self.assertIn("A13bPixel", body_it)
        self.assertNotIn("A13bPixelEN", body_it)
        self.assertNotIn("A13bPixelFR", body_it)
        self.assertIn("A13bPixelBrand", body_it)
        self.assertIn(IMG_HERO, body_it)

        # EN render (home)
        body_en = preview_body("en")
        self.assertIn("Pixel walk EN", body_en)
        self.assertIn("A13bPixelEN", body_en)
        self.assertNotIn("Pixel walk IT", body_en)
        self.assertIn("A13bPixelBrand", body_en)
        self.assertIn(IMG_HERO, body_en)

        # FR render (home)
        body_fr = preview_body("fr")
        self.assertIn("Pixel walk FR", body_fr)
        self.assertIn("A13bPixelFR", body_fr)
        self.assertIn("A13bPixelBrand", body_fr)
        self.assertIn(IMG_HERO, body_fr)

        # Unedited locales (ES · AR) — authored registry fallback on
        # translatable text + global logo + global image still visible.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Pixel walk IT", body)
            self.assertNotIn("Pixel walk EN", body)
            self.assertNotIn("Pixel walk FR", body)
            self.assertIn("A13bPixelBrand", body)
            self.assertIn(IMG_HERO, body)
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Pixel home",
                )

        # AR preview (home) — `.cp-*` skin must emit
        # ``<html dir="rtl" lang="ar">`` (38 mature RTL rules already
        # shipped with the published_live skin · verified Step-0).
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 6. owner reopens the editor on each locale ───────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Pixel walk IT"),
            ("en", "Pixel walk EN"),
            ("fr", "Pixel walk FR"),
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

        # Global text: overridden universally, not translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Pixel editor")
        self.assertEqual(logo_field["value"], "A13bPixelBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        # Scalar image: overridden universally, not translatable.
        hero_field = find_field_by_key(r_es.context["groups"], "home.hero_image")
        self.assertIsNotNone(hero_field, "home.hero_image missing from Pixel editor")
        self.assertEqual(hero_field["value"], IMG_HERO)
        self.assertTrue(hero_field["is_overridden"])
        self.assertFalse(hero_field["translatable"])

        # ── 7. perimeter invariants re-checked end-of-test ───────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            InvalidEditableField,
            validate_key_path,
        )
        # Chiara enrollment must persist past Pixel lifecycle.
        self.assertIn("editorial-designer-grid", _ENABLED,
                      "Chiara enrollment must persist past Pixel lifecycle")
        # Posts / series_detail stay registry-only — 5-archetype
        # uniform perimeter policy consistent with Lex/Juris/Casa/
        # Villa/Chiara. Writes under these paths must be rejected by
        # validate_key_path at the schema layer.
        for out_path in (
            "posts.0.title",
            "posts.0.cover_image",
            "posts.1.cover_image",
            "posts.2.cover_image",
            "posts.0.lead",
            "posts.0.gallery.0",
        ):
            with self.assertRaises(InvalidEditableField,
                                   msg=f"Pixel posts path must be rejected: {out_path}"):
                validate_key_path("cinematic-photographer", out_path)

    # ------------------------------------------------------------------
    # A.14 · Step 2 — Sapore (trattoria-warm) lifecycle HTTP
    # cross-cutting · OPENED the restaurant-continuation family via
    # staged dedicated-schema progression. Brace (street-modern) joined
    # the gate in A.14b — the Brace-out runtime guard that lived at the
    # end of this test was removed and its inversion is contract-tested
    # by `test_a14b_brace_out_guard_was_removed_from_sapore_tests`.
    # Novel shape exercise: deep-path menu-cell override on
    # `menu.sections.0.dishes.0.name` (tuple-in-dict-list parent).
    # Sapore ships no posts list, so the complex-shape exclusion at
    # end-of-test focuses on form/story/options/hours_footer paths.
    # ------------------------------------------------------------------

    def test_a14_sapore_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Sapore enrollment:

        1. customer edits IT / EN / FR on a Sapore translatable path
           (home.headline)
        2. customer edits a global TEXT path (site.logo_word) via EN
           autosave — storage MUST be plain-keyed (no @en: prefix)
        3. customer edits the single-top-level-scalar IMAGE field
           (home.hero_image) — storage MUST be plain-keyed across all
           5 locales (5× explicit assertNotIn on @<locale>: prefix)
        4. customer edits a DEEP-PATH MENU CELL on the novel nested
           tuple-in-dict-list shape (menu.sections.0.dishes.0.name) —
           storage MUST be plain-keyed (no @<locale>: prefix on menu
           cells) AND the override MUST apply end-to-end at render
           time (proves the A.14 `_resolve_path` + `_apply_indexed`
           list-index extensions work in production, not just at
           contract level — user-imposed blindatura).
        5. project publishes via services.publish_project
        6. second user visits every public preview locale:
           - IT/EN/FR render their locale override + global logo + hero
             image + menu dish override (home + menu pages both)
           - ES/AR fall back to the authored registry text, still see
             the global logo + hero image + menu dish override
             (images + menu cells are universal)
           - AR response head carries ``<html dir="rtl" lang="ar">``
             on the ``.tw-*`` skin (18 RTL rules shipped since D-078
             Session 48 Sapore rollout)
        7. owner reopens the editor per locale; sidebar prefill matches
           the buffer for that locale on home.headline and shows
           site.logo_word + home.hero_image as universal overrides
        8. perimeter invariants double-checked at the end of the walk:
           10 pre-A.14 archetypes still enrolled; complex-shape paths
           (form_sections, form_fields, occasion_options, storia.story,
           site.hours_footer_rows, pages) stay rejected by
           validate_key_path. (Brace-out runtime guard was lifted in
           A.14b — see companion symmetric-removal contract test.)

        Explicitly NOT exercised here: Brace editor work, coverage
        expansion, mutable rows, image per-locale, browser walk
        (Step 3), helper/infra touches beyond what Step 1 already
        introduced.
        """
        import json as _json

        sapore = WebTemplate.objects.get(slug="sapore-trattoria-pizzeria")
        p = services.create_project_from_template(owner=self.owner, template=sapore)

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

        # ── 1. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Walk IT Sapore <em>A14Piatto</em>."),
            ("en", "Walk EN Sapore <em>A14PiattoEN</em>."),
            ("fr", "Walk FR Sapore <em>A14PiattoFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 2. global plain-keyed text — site.logo_word via EN ────
        # Global text must NOT pick up the @en: prefix even when written
        # inside an EN-tagged autosave.
        r = autosave("en", {"site.logo_word": "A14SaporeBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 3. scalar image override — home.hero_image ────────────
        # Top-level scalar image (Pragma / Pixel single-scalar-image
        # pattern). Images are classified NON-translatable —
        # persistence is plain-keyed regardless of the request-tagged
        # locale.
        IMG_HERO = "https://walk-sapore.example/img/hero-A14.jpg"
        r = autosave("it", {"home.hero_image": IMG_HERO})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.hero_image", r.json()["content_keys"])

        # ── 4. deep-path menu cell — menu.sections.0.dishes.0.name ─
        # NOVEL shape: tuple-in-dict-list parent. This exercises both
        # the A.14 `_resolve_path` extension (schema side · Step 1) AND
        # the A.14 `_apply_indexed` parent-walk extension (rendering
        # side · Step 2) — if either fails, the override persists but
        # never reaches the customer's preview, which is exactly what
        # the user-imposed "blindato bene a runtime" guardrail targets.
        DISH_NAME = "Walk Piatto A14"
        r = autosave("it", {"menu.sections.0.dishes.0.name": DISH_NAME})
        self.assertEqual(r.status_code, 200)
        self.assertIn("menu.sections.0.dishes.0.name", r.json()["content_keys"])

        # Storage shape: 3 @<locale>:home.headline + 3 plain-keyed
        # globals (logo + hero image + deep-path menu cell). Zero
        # @<locale>: on image/menu-cell paths; zero @en: on logo;
        # zero plain-key leak on home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("home.hero_image", keys)
        self.assertIn("menu.sections.0.dishes.0.name", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        # Image override plain-keyed across all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:home.hero_image", keys,
                             f"home.hero_image must NEVER be @{loc}:-prefixed")
        # Menu cell plain-keyed across all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:menu.sections.0.dishes.0.name", keys,
                             f"menu cell must NEVER be @{loc}:-prefixed")

        # ── 5. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 6. second user on every public preview locale ────────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            # page=None fetches home; page='menu' etc. fetches a
            # specific sub-page. The menu override is menu-page-scoped,
            # so menu assertions need the menu page fetch.
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/restaurant/sapore-trattoria-pizzeria/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override visible, EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Walk IT Sapore", body_it)
        self.assertIn("A14Piatto", body_it)
        self.assertNotIn("A14PiattoEN", body_it)
        self.assertNotIn("A14PiattoFR", body_it)
        self.assertIn("A14SaporeBrand", body_it)
        self.assertIn(IMG_HERO, body_it)

        # IT render (menu page) — menu cell override visible +
        # universal globals.
        body_it_menu = preview_body("it", page="menu")
        self.assertIn("A14SaporeBrand", body_it_menu)
        self.assertIn(DISH_NAME, body_it_menu,
                      "menu cell override must render on menu page IT")
        # Other dishes (not overridden) still show the authored names
        # as sanity check that the splicer didn't wipe the row.
        self.assertIn("Carciofo alla giudia", body_it_menu)

        # EN render (home + menu)
        body_en = preview_body("en")
        self.assertIn("Walk EN Sapore", body_en)
        self.assertIn("A14PiattoEN", body_en)
        self.assertNotIn("Walk IT Sapore", body_en)
        self.assertIn("A14SaporeBrand", body_en)
        self.assertIn(IMG_HERO, body_en)
        body_en_menu = preview_body("en", page="menu")
        self.assertIn(DISH_NAME, body_en_menu,
                      "menu cell override is global · must render on EN menu")

        # FR render (home + menu spot check)
        body_fr = preview_body("fr")
        self.assertIn("Walk FR Sapore", body_fr)
        self.assertIn("A14PiattoFR", body_fr)
        self.assertIn("A14SaporeBrand", body_fr)
        self.assertIn(IMG_HERO, body_fr)
        body_fr_menu = preview_body("fr", page="menu")
        self.assertIn(DISH_NAME, body_fr_menu)

        # Unedited locales — authored text fallback + global chrome +
        # image + menu cell override all universal.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Walk IT Sapore", body)
            self.assertNotIn("Walk EN Sapore", body)
            self.assertNotIn("Walk FR Sapore", body)
            self.assertIn("A14SaporeBrand", body)
            self.assertIn(IMG_HERO, body)
            body_menu = preview_body(locale, page="menu")
            self.assertIn(DISH_NAME, body_menu,
                          f"menu cell override must render universally on {locale} menu")
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Sapore home",
                )

        # AR preview (home) — `.tw-*` skin must emit
        # ``<html dir="rtl" lang="ar">`` (18 mature RTL rules shipped
        # since Session 48 D-078 Sapore rollout · verified Step-0).
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 7. owner reopens the editor on each locale ───────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Walk IT Sapore"),
            ("en", "Walk EN Sapore"),
            ("fr", "Walk FR Sapore"),
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

        # Global text: overridden universally, not translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Sapore editor")
        self.assertEqual(logo_field["value"], "A14SaporeBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        # Scalar image: overridden universally, not translatable.
        hero_field = find_field_by_key(r_es.context["groups"], "home.hero_image")
        self.assertIsNotNone(hero_field, "home.hero_image missing from Sapore editor")
        self.assertEqual(hero_field["value"], IMG_HERO)
        self.assertTrue(hero_field["is_overridden"])
        self.assertFalse(hero_field["translatable"])

        # ── 8. perimeter invariants re-checked end-of-test ───────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            InvalidEditableField,
            validate_key_path,
        )
        # 10 pre-A.14 archetypes still enrolled (runtime tenfold check).
        # The Brace-out dual guard that lived here during A.14 was
        # removed in A.14b — its inversion is contract-tested by
        # `test_a14b_brace_out_guard_was_removed_from_sapore_tests`.
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
        ):
            self.assertIn(arc, _ENABLED, f"{arc} lost enrollment mid-lifecycle")
        # Complex-shape paths stay rejected — re-verified runtime at
        # end-of-test so a silent schema drift mid-phase is caught.
        for out_path in (
            "contatti.form_sections",
            "contatti.form_sections.0.fields",
            "contatti.form_fields",
            "contatti.form_fields.0.name",
            "contatti.occasion_options",
            "contatti.occasion_options.0",
            "storia.story",
            "storia.story.0",
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "pages",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Sapore complex-shape path must stay rejected: {out_path}",
            ):
                validate_key_path("trattoria-warm", out_path)

    # ------------------------------------------------------------------
    # A.14b · Step 2 — Brace (street-modern) lifecycle HTTP cross-cutting
    # · CLOSES the restaurant-continuation family opened in A.14 with
    # Sapore. Third staged dedicated-schema closure (after real-estate
    # A.12+A.12b and portfolio A.13+A.13b). Exercises BOTH deep-path
    # shapes end-to-end:
    #   - `menu.sections.{i}.items[].image` (dict-in-dict-list parent ·
    #     Chiara A.13 precedent)
    #   - `ordina.routes.{i}.lines[].value` (tuple-in-dict-list parent ·
    #     Sapore A.14 precedent via f66ac24 render-side fix)
    # Brace ships zero posts list + zero form structures — complex-shape
    # exclusion at end-of-test focuses on flat list-of-str (manifesto
    # paragraphs, hours footer, categories) + navigation + posts guard.
    # ------------------------------------------------------------------

    def test_a14b_brace_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Brace enrollment:

        1. customer edits IT / EN / FR on a Brace translatable path
           (home.headline)
        2. customer edits a global TEXT path (site.logo_word) via EN
           autosave — storage MUST be plain-keyed (no @en: prefix)
        3. customer edits a top-level scalar IMAGE field
           (home.hero_image) — storage MUST be plain-keyed across all
           5 locales (5× explicit assertNotIn on @<locale>: prefix)
        4. customer edits a DEEP-PATH MENU CELL image on the dict-in-
           dict-list parent shape (menu.sections.0.items.0.image) —
           storage MUST be plain-keyed (5× assertNotIn) AND the
           override MUST render end-to-end on the menu page in all 5
           public-preview locales (user-imposed runtime blindatura ·
           Chiara-precedent shape, mechanical reuse)
        5. customer edits a DEEP-PATH ORDINA ROUTE LINE VALUE on the
           tuple-in-dict-list parent shape (ordina.routes.0.lines.0.value)
           — storage MUST be plain-keyed (5× assertNotIn) AND the
           override MUST render end-to-end on the ordina page in all 5
           public-preview locales (Sapore-precedent shape via A.14
           f66ac24 render-side fix · mechanical reuse)
        6. project publishes via services.publish_project
        7. second user visits every public preview locale:
           - IT/EN/FR render their locale override + global logo + hero
             image + menu dish image override + ordina line override
           - ES/AR fall back to the authored registry text, still see
             the global logo + hero image + menu dish image + ordina
             line override (images + deep-path cells are universal)
           - AR response head carries ``<html dir="rtl" lang="ar">`` on
             the ``.sm-*`` skin (24 RTL rules in Brace _base.html)
        8. owner reopens the editor per locale; sidebar prefill matches
           the buffer for that locale on home.headline and shows
           site.logo_word + home.hero_image as universal overrides
        9. perimeter invariants double-checked at the end of the walk:
           Brace (street-modern) IS enrolled in both gates at runtime
           (opposite assertion vs the former Brace-out guard),
           Sapore (trattoria-warm) still enrolled (verifies the Sapore-
           out-guard was not accidentally introduced in A.14b),
           complex-shape paths (home.manifesto_paragraphs, moments.categories,
           site.hours_footer_rows, pages, posts) stay rejected by
           validate_key_path.

        Explicitly NOT exercised here: browser walk (Step 3), coverage
        expansion, mutable rows, image per-locale, further infra
        touches. Zero production-code changes in this Step 2 commit.
        """
        import json as _json

        brace = WebTemplate.objects.get(slug="brace-street-food-lab")
        p = services.create_project_from_template(owner=self.owner, template=brace)

        # ── 0. perimeter invariants verified at TEST START ────────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            _ARCHETYPE_SCHEMAS as _SCHEMAS,
            InvalidEditableField,
            validate_key_path,
        )
        self.assertIn("street-modern", _SCHEMAS,
                      "Brace (street-modern) must be enrolled at lifecycle start")
        self.assertIn("street-modern", _ENABLED,
                      "Brace (street-modern) must be in multi-locale gate at start")
        self.assertIn("trattoria-warm", _SCHEMAS,
                      "Sapore (trattoria-warm) must still be enrolled at start")
        self.assertIn("trattoria-warm", _ENABLED)

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

        # ── 1. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Walk IT Brace <em>A14bLine</em>."),
            ("en", "Walk EN Brace <em>A14bLineEN</em>."),
            ("fr", "Walk FR Brace <em>A14bLineFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 2. global plain-keyed text — site.logo_word via EN ────
        r = autosave("en", {"site.logo_word": "A14bBraceBrand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 3. scalar image override — home.hero_image ────────────
        IMG_HERO = "https://walk-brace.example/img/hero-A14b.jpg"
        r = autosave("it", {"home.hero_image": IMG_HERO})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.hero_image", r.json()["content_keys"])

        # ── 4. deep-path MENU image override on dict-in-dict-list ─
        # `menu.sections.0.items.0.image` — Chiara precedent shape.
        # Proves the A.14 render-side fix (commit f66ac24) also applies
        # to dict-in-dict-list parent walks (not just tuple-in-dict-list
        # which was exercised by Sapore).
        IMG_DISH = "https://walk-brace.example/img/dish-A14b.jpg"
        r = autosave("it", {"menu.sections.0.items.0.image": IMG_DISH})
        self.assertEqual(r.status_code, 200)
        self.assertIn("menu.sections.0.items.0.image", r.json()["content_keys"])

        # ── 5. deep-path ORDINA route line override on tuple-in-dict-list ─
        # `ordina.routes.0.lines.0.value` — Sapore precedent shape
        # (tuple-in-dict-list parent). Mechanical reuse of A.14 infra.
        LINE_VALUE = "A14b Walk Indirizzo Bologna"
        r = autosave("it", {"ordina.routes.0.lines.0.value": LINE_VALUE})
        self.assertEqual(r.status_code, 200)
        self.assertIn("ordina.routes.0.lines.0.value", r.json()["content_keys"])

        # Storage shape: 3 @<locale>:home.headline + 4 plain-keyed
        # globals (logo + hero image + menu deep-path image + ordina
        # deep-path tuple value). Zero @<locale>: on image or deep-path
        # cell paths; zero @en: on logo; zero plain-key leak on
        # home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("home.hero_image", keys)
        self.assertIn("menu.sections.0.items.0.image", keys)
        self.assertIn("ordina.routes.0.lines.0.value", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        # Image override plain-keyed across all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:home.hero_image", keys,
                             f"home.hero_image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:menu.sections.0.items.0.image", keys,
                             f"deep-path menu image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:ordina.routes.0.lines.0.value", keys,
                             f"deep-path route line value must NEVER be @{loc}:-prefixed")

        # ── 6. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 7. second user on every public preview locale ────────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/restaurant/brace-street-food-lab/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override visible, EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Walk IT Brace", body_it)
        self.assertIn("A14bLine", body_it)
        self.assertNotIn("A14bLineEN", body_it)
        self.assertNotIn("A14bLineFR", body_it)
        self.assertIn("A14bBraceBrand", body_it)
        self.assertIn(IMG_HERO, body_it)

        # IT render (menu page) — menu deep-path image override visible
        # + universal globals. Also check that other dishes in section 0
        # still render the authored image (proves splicer touched ONLY
        # the .0.0 cell without corrupting other rows).
        body_it_menu = preview_body("it", page="menu")
        self.assertIn("A14bBraceBrand", body_it_menu)
        self.assertIn(IMG_DISH, body_it_menu,
                      "menu deep-path image override must render on menu page IT")

        # IT render (ordina page) — ordina deep-path tuple value visible
        # + universal globals.
        body_it_ordina = preview_body("it", page="ordina")
        self.assertIn("A14bBraceBrand", body_it_ordina)
        self.assertIn(LINE_VALUE, body_it_ordina,
                      "ordina deep-path route line value must render on ordina page IT")

        # EN render (home + menu + ordina)
        body_en = preview_body("en")
        self.assertIn("Walk EN Brace", body_en)
        self.assertIn("A14bLineEN", body_en)
        self.assertNotIn("Walk IT Brace", body_en)
        self.assertIn("A14bBraceBrand", body_en)
        self.assertIn(IMG_HERO, body_en)
        body_en_menu = preview_body("en", page="menu")
        self.assertIn(IMG_DISH, body_en_menu,
                      "menu deep-path image override is global · must render on EN menu")
        body_en_ordina = preview_body("en", page="ordina")
        self.assertIn(LINE_VALUE, body_en_ordina,
                      "ordina deep-path value is global · must render on EN ordina")

        # FR render
        body_fr = preview_body("fr")
        self.assertIn("Walk FR Brace", body_fr)
        self.assertIn("A14bLineFR", body_fr)
        self.assertIn("A14bBraceBrand", body_fr)
        self.assertIn(IMG_HERO, body_fr)
        body_fr_menu = preview_body("fr", page="menu")
        self.assertIn(IMG_DISH, body_fr_menu)
        body_fr_ordina = preview_body("fr", page="ordina")
        self.assertIn(LINE_VALUE, body_fr_ordina)

        # Unedited locales — authored text fallback + global chrome +
        # image + deep-path cells all universal.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Walk IT Brace", body)
            self.assertNotIn("Walk EN Brace", body)
            self.assertNotIn("Walk FR Brace", body)
            self.assertIn("A14bBraceBrand", body)
            self.assertIn(IMG_HERO, body)
            body_menu = preview_body(locale, page="menu")
            self.assertIn(IMG_DISH, body_menu,
                          f"menu deep-path image must render universally on {locale} menu")
            body_ordina = preview_body(locale, page="ordina")
            self.assertIn(LINE_VALUE, body_ordina,
                          f"ordina deep-path value must render universally on {locale} ordina")
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Brace home",
                )

        # AR preview (home) — `.sm-*` skin must emit
        # ``<html dir="rtl" lang="ar">`` (24 mature RTL rules verified
        # Step 0).
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 8. owner reopens the editor on each locale ───────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Walk IT Brace"),
            ("en", "Walk EN Brace"),
            ("fr", "Walk FR Brace"),
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

        # Global text: overridden universally, not translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Brace editor")
        self.assertEqual(logo_field["value"], "A14bBraceBrand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        # Scalar image: overridden universally, not translatable.
        hero_field = find_field_by_key(r_es.context["groups"], "home.hero_image")
        self.assertIsNotNone(hero_field, "home.hero_image missing from Brace editor")
        self.assertEqual(hero_field["value"], IMG_HERO)
        self.assertTrue(hero_field["is_overridden"])
        self.assertFalse(hero_field["translatable"])

        # ── 9. perimeter invariants re-checked end-of-test ───────
        # Brace enrolled on BOTH gates at end-of-test (opposite of the
        # former Brace-out guard in the A.14 Sapore lifecycle).
        self.assertIn("street-modern", _SCHEMAS,
                      "Brace must still be enrolled at end-of-lifecycle")
        self.assertIn("street-modern", _ENABLED,
                      "Brace must still be in multi-locale gate at end")
        # Sapore (trattoria-warm) still enrolled (no accidental removal).
        self.assertIn("trattoria-warm", _SCHEMAS,
                      "Sapore enrollment must persist past Brace lifecycle")
        self.assertIn("trattoria-warm", _ENABLED)
        # 10 pre-A.14 archetypes also still enrolled (eleven-fold with
        # Sapore · 12-fold including Brace itself).
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
        ):
            self.assertIn(arc, _ENABLED, f"{arc} lost enrollment mid-lifecycle")
        # Complex-shape paths stay rejected — re-verified runtime at
        # end-of-test so a silent schema drift mid-phase is caught.
        for out_path in (
            # Flat list-of-str containers
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "home.manifesto_paragraphs",
            "home.manifesto_paragraphs.0",
            "moments.categories",
            "moments.categories.0",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
            # Col-level exclusions (structural identifiers / routing flags)
            "menu.sections.0.id",
            "moments.grid.0.filename",
            "ordina.routes.0.cta_kind",
            "contatti.channels.0.icon",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Brace complex-shape path must stay rejected: {out_path}",
            ):
                validate_key_path("street-modern", out_path)

    # ------------------------------------------------------------------
    # A.15 · Step 2 — Bottega (artisan-workshop) lifecycle HTTP
    # cross-cutting · OPENS the ecommerce family via staged dedicated-
    # schema progression · fourth staged opening (after real-estate /
    # portfolio / restaurant-continuation). Luxe (fashion-editorial)
    # stays OUT until A.15b — runtime Luxe-out guard re-checked at
    # start AND end of the test. Exercises THREE image-in-dict-row
    # shapes end-to-end with explicit neighbor preservation:
    #   - home.makers[].portrait (4 artisan portraits · home page)
    #   - shop.products[].image (9 demo product cards · shop page)
    #   - product.artisan_portrait (nested-dict scalar · product page)
    # Boundary editor-vs-commerce-admin re-verified end-of-test by
    # rejecting sensitive OUT paths including flat list-of-str + form
    # structures + empty posts.
    # ------------------------------------------------------------------

    def test_a15_bottega_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Bottega enrollment.

        IMPORTANT skin note (documented · NOT a bug): Bottega's
        artisan-workshop skin treats most portrait-like surfaces as
        **typographic stamps** (Session 42 D-073 DNA-honest conversion:
        artisan-workshop was always meant to be typographic-led, not
        portrait-led). Fields `home.makers[].portrait`,
        `product.artisan_portrait`, `atelier.founder_portrait` are
        exposed in the editor sidebar (future skin variants / customer
        swap · data preserved in registry) but are NOT rendered by the
        current `.aw-*` skin. The ACTUALLY-RENDERED image surfaces are
        the PRODUCT thumbnails in dict-rows:
          - `home.latest_items[].image` (home page)
          - `shop.products[].image` (shop page)
          - `product.related_items[].image` (product page)
        So the lifecycle test blindates:
          - STORAGE plain-key for ALL 3 user-asked paths
            (product.artisan_portrait · shop.products.0.image ·
            home.makers.0.portrait) · 5× assertNotIn each · covers the
            full per-locale contract regardless of skin rendering
          - RENDER visibility on public preview ONLY on paths that the
            current skin actually renders
            (shop.products.0.image + home.latest_items.0.image +
            product.related_items.0.image · 3 distinct image-in-dict-row
            list shapes including home.latest_items with a col set
            different from shop.products so the "second list shape"
            ask is covered)

        Phases:
        1. perimeter invariants at TEST START — Bottega in gate · Luxe
           out of gate
        2. customer edits IT / EN / FR on home.headline
        3. customer edits global site.logo_word via EN — plain-keyed
           no @en: prefix
        4. customer edits NESTED-DICT scalar `product.artisan_portrait`
           (storage blindatura only · not rendered in typographic skin)
           — 5× assertNotIn @<locale>:
        5. customer edits IMAGE-IN-DICT-ROW `shop.products.0.image`
           — 5× assertNotIn + render on public shop page all 5 locales
        6. customer edits IMAGE-IN-DICT-ROW `home.makers.0.portrait`
           (storage blindatura only · not rendered · typographic stamp)
           — 5× assertNotIn
        6b. customer edits IMAGE-IN-DICT-ROW `home.latest_items.0.image`
           (SECOND list shape distinct from shop.products · different
           col set) — 5× assertNotIn + render on public home page all
           5 locales
        6c. customer edits IMAGE-IN-DICT-ROW `product.related_items.0.image`
           (THIRD list shape · product-page scoped) — 5× assertNotIn
           + render on public product page all 5 locales
        7. publish
        8. second user visits home + shop + product on all 5 locales
        9. AR response head carries ``<html dir="rtl" lang="ar">`` on
           the `.aw-*` skin
        10. owner reopens the editor per locale · prefill + universals
        11. perimeter invariants re-checked end-of-test:
            - Bottega + 12 pre-A.15 archetypes still enrolled
            - Sensitive OUT paths REJECTED (shop.filter_groups.0.options
              · product.gallery · product.size_options · contatti.form_fields
              · pages · posts + col-level: shop.products.0.id ·
              shop.products.0.available)
            (Luxe-out dual guard removed in A.15b via symmetric inversion;
             see `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`.)

        Explicitly NOT exercised here: browser walk (Step 3), Luxe
        editor work, coverage expansion, mutable rows, image per-
        locale, apps.commerce touches. Zero production-code changes.
        """
        import json as _json

        bottega = WebTemplate.objects.get(slug="bottega-shop-artigianale")
        p = services.create_project_from_template(owner=self.owner, template=bottega)

        # ── 1. perimeter invariants at TEST START ────────────────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            _ARCHETYPE_SCHEMAS as _SCHEMAS,
            InvalidEditableField,
            validate_key_path,
        )
        self.assertIn("artisan-workshop", _SCHEMAS,
                      "Bottega must be enrolled at lifecycle start")
        self.assertIn("artisan-workshop", _ENABLED,
                      "Bottega must be in multi-locale gate at start")
        # Luxe-out start/end guards removed in A.15b · see
        # `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`.

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

        # ── 2. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Walk IT Bottega <em>A15ArtisanLine</em>."),
            ("en", "Walk EN Bottega <em>A15ArtisanLineEN</em>."),
            ("fr", "Walk FR Bottega <em>A15ArtisanLineFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 3. global plain-keyed text — site.logo_word via EN ────
        r = autosave("en", {"site.logo_word": "A15 Bottega Walk Brand"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 4. nested-dict scalar image — product.artisan_portrait ─
        # Chiara `studio.founder.image` precedent shape. Image fields
        # NEVER per-locale.
        IMG_ARTISAN = "https://walk-bottega.example/img/artisan-A15.jpg"
        r = autosave("it", {"product.artisan_portrait": IMG_ARTISAN})
        self.assertEqual(r.status_code, 200)
        self.assertIn("product.artisan_portrait", r.json()["content_keys"])

        # ── 5. image-in-dict-row on shop.products (demo catalog) ──
        # 9-item dict listing · image col · first row .0.image
        IMG_PRODUCT = "https://walk-bottega.example/img/product-A15.jpg"
        r = autosave("it", {"shop.products.0.image": IMG_PRODUCT})
        self.assertEqual(r.status_code, 200)
        self.assertIn("shop.products.0.image", r.json()["content_keys"])

        # ── 6. image-in-dict-row on home.makers (STORAGE blindatura) ─
        # 4 artisan portraits · dict with portrait col · NOT rendered
        # by the typographic-first artisan-workshop skin (Session 42
        # DNA-honest crest-mark treatment) but still exposed in the
        # editor sidebar · storage contract must still be clean.
        IMG_MAKER = "https://walk-bottega.example/img/maker-A15.jpg"
        r = autosave("it", {"home.makers.0.portrait": IMG_MAKER})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.makers.0.portrait", r.json()["content_keys"])

        # ── 6b. image-in-dict-row on home.latest_items (rendered) ─
        # 4 product cards · dict with image col · DIFFERENT col set
        # from shop.products (n/name/meta/place/price/edition/tag/image
        # vs n/name/artisan/place/meta/price/edition/tag/image). Second
        # image-in-dict-row list shape to blindate end-to-end on home
        # page render (covers user's "second list shape" ask via a
        # path the typographic skin actually renders).
        IMG_LATEST = "https://walk-bottega.example/img/latest-A15.jpg"
        r = autosave("it", {"home.latest_items.0.image": IMG_LATEST})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.latest_items.0.image", r.json()["content_keys"])

        # ── 6c. image-in-dict-row on product.related_items (rendered) ─
        # Third distinct list shape (cols n/name/meta/price/image) ·
        # product-page-scoped · fourth image surface in this lifecycle.
        IMG_RELATED = "https://walk-bottega.example/img/related-A15.jpg"
        r = autosave("it", {"product.related_items.0.image": IMG_RELATED})
        self.assertEqual(r.status_code, 200)
        self.assertIn("product.related_items.0.image", r.json()["content_keys"])

        # Storage shape: 3 @<locale>:home.headline + 6 plain-keyed
        # globals (logo + 5 image paths: product.artisan_portrait +
        # shop.products.0.image + home.makers.0.portrait +
        # home.latest_items.0.image + product.related_items.0.image).
        # Zero @<locale>: on any image path across all 5 locales;
        # zero @en: on logo; zero plain-key leak on home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("product.artisan_portrait", keys)
        self.assertIn("shop.products.0.image", keys)
        self.assertIn("home.makers.0.portrait", keys)
        self.assertIn("home.latest_items.0.image", keys)
        self.assertIn("product.related_items.0.image", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        # All 5 image paths plain-keyed across all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:product.artisan_portrait", keys,
                             f"product.artisan_portrait must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:shop.products.0.image", keys,
                             f"shop.products.0.image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:home.makers.0.portrait", keys,
                             f"home.makers.0.portrait must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:home.latest_items.0.image", keys,
                             f"home.latest_items.0.image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:product.related_items.0.image", keys,
                             f"product.related_items.0.image must NEVER be @{loc}:-prefixed")

        # ── 7. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 8. second user on every public preview locale ────────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/ecommerce/bottega-shop-artigianale/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override + global logo +
        # home.latest_items.0.image override visible (product thumb
        # on home page · ACTUALLY rendered by the typographic skin).
        # EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Walk IT Bottega", body_it)
        self.assertIn("A15ArtisanLine", body_it)
        self.assertNotIn("A15ArtisanLineEN", body_it)
        self.assertNotIn("A15ArtisanLineFR", body_it)
        self.assertIn("A15 Bottega Walk Brand", body_it)
        self.assertIn(IMG_LATEST, body_it,
                      "home.latest_items.0.image override must render on home page IT")

        # IT render (shop page) — shop.products.0.image override visible
        # + universal logo.
        body_it_shop = preview_body("it", page="shop")
        self.assertIn("A15 Bottega Walk Brand", body_it_shop)
        self.assertIn(IMG_PRODUCT, body_it_shop,
                      "shop.products.0.image override must render on shop page IT")

        # IT render (product page) — product.related_items.0.image
        # override visible + universal logo. Note: product.artisan_portrait
        # override is STORED correctly but NOT rendered by the typographic
        # skin (documented in test docstring).
        body_it_product = preview_body("it", page="product")
        self.assertIn("A15 Bottega Walk Brand", body_it_product)
        self.assertIn(IMG_RELATED, body_it_product,
                      "product.related_items.0.image override must render on product page IT")

        # EN render spans home + shop + product
        body_en = preview_body("en")
        self.assertIn("Walk EN Bottega", body_en)
        self.assertIn("A15ArtisanLineEN", body_en)
        self.assertNotIn("Walk IT Bottega", body_en)
        self.assertIn("A15 Bottega Walk Brand", body_en)
        self.assertIn(IMG_LATEST, body_en)
        body_en_shop = preview_body("en", page="shop")
        self.assertIn(IMG_PRODUCT, body_en_shop)
        body_en_product = preview_body("en", page="product")
        self.assertIn(IMG_RELATED, body_en_product)

        # FR render spans home + shop + product
        body_fr = preview_body("fr")
        self.assertIn("Walk FR Bottega", body_fr)
        self.assertIn("A15ArtisanLineFR", body_fr)
        self.assertIn("A15 Bottega Walk Brand", body_fr)
        self.assertIn(IMG_LATEST, body_fr)
        body_fr_shop = preview_body("fr", page="shop")
        self.assertIn(IMG_PRODUCT, body_fr_shop)
        body_fr_product = preview_body("fr", page="product")
        self.assertIn(IMG_RELATED, body_fr_product)

        # Unedited locales — authored fallback on translatable text +
        # universals preserved across home + shop + product.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Walk IT Bottega", body)
            self.assertNotIn("Walk EN Bottega", body)
            self.assertNotIn("Walk FR Bottega", body)
            self.assertIn("A15 Bottega Walk Brand", body)
            self.assertIn(IMG_LATEST, body,
                          f"home.latest_items.0.image must render universally on {locale} home")
            body_shop = preview_body(locale, page="shop")
            self.assertIn(IMG_PRODUCT, body_shop,
                          f"shop.products.0.image must render universally on {locale} shop")
            body_product = preview_body(locale, page="product")
            self.assertIn(IMG_RELATED, body_product,
                          f"product.related_items.0.image must render universally on {locale} product")
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Bottega home",
                )

        # AR preview (home) — `.aw-*` skin must emit
        # ``<html dir="rtl" lang="ar">`` (31 mature RTL rules verified
        # Step 0).
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 9. owner reopens the editor on each locale ───────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Walk IT Bottega"),
            ("en", "Walk EN Bottega"),
            ("fr", "Walk FR Bottega"),
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

        # Global text + nested-dict scalar image: overridden universally,
        # not translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Bottega editor")
        self.assertEqual(logo_field["value"], "A15 Bottega Walk Brand")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        artisan_field = find_field_by_key(r_es.context["groups"], "product.artisan_portrait")
        self.assertIsNotNone(artisan_field, "product.artisan_portrait missing from Bottega editor")
        self.assertEqual(artisan_field["value"], IMG_ARTISAN)
        self.assertTrue(artisan_field["is_overridden"])
        self.assertFalse(artisan_field["translatable"])

        # ── 10. perimeter invariants re-checked end-of-test ──────
        # Luxe-out end-of-test guard removed in A.15b via symmetric
        # inversion — see `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`.
        # Bottega still enrolled (no accidental removal).
        self.assertIn("artisan-workshop", _SCHEMAS,
                      "Bottega enrollment must persist through lifecycle")
        self.assertIn("artisan-workshop", _ENABLED)
        # 12 pre-A.15 archetypes also still enrolled.
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
        ):
            self.assertIn(arc, _ENABLED, f"{arc} lost enrollment mid-lifecycle")
        # Sensitive OUT paths stay rejected — re-verified runtime at
        # end-of-test per user guidance.
        for out_path in (
            # Nested list-of-str inside dict rows
            "shop.filter_groups.0.options",
            "shop.filter_groups.0.options.0",
            # Flat list-of-str on product page (gallery + size_options)
            "product.gallery",
            "product.gallery.0",
            "product.size_options",
            "product.size_options.0",
            # Form structure
            "contatti.form_fields",
            "contatti.form_fields.0.name",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
            # Col-level exclusions (structural identifiers)
            "shop.products.0.id",
            "shop.products.0.available",
            "home.latest_items.0.id",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Bottega complex-shape path must stay rejected: {out_path}",
            ):
                validate_key_path("artisan-workshop", out_path)

    # ------------------------------------------------------------------
    # A.15b · Step 2 — Luxe (fashion-editorial) lifecycle HTTP cross-
    # cutting · CLOSES the ecommerce family opened by A.15 Bottega ·
    # fourth staged dedicated-schema closure (after real-estate +
    # portfolio + restaurant-continuation + ecommerce). Luxe IN +
    # Bottega still IN re-verified at start AND end of the test.
    # Exercises the FULL image surface taxonomy end-to-end:
    #   - home.cover_image (scalar top-level · rendered on home page)
    #   - product.atelier_portrait (nested-dict scalar · rendered on
    #     product page)
    #   - maison.direction_portrait (nested-dict scalar · rendered on
    #     maison page)
    #   - collezione.products.0.image (image-in-dict-row · rendered on
    #     collezione page)
    #   - lookbook.looks.0.image (image-in-dict-row · rendered on
    #     lookbook page · different list shape and page from products)
    # All 5 image paths plain-keyed across all 5 locales (D-098 image
    # per-locale out-of-scope · editorial DNA has zero storage-only
    # split · every image surface renders).
    # ------------------------------------------------------------------

    def test_a15b_luxe_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Luxe enrollment.

        Unlike Bottega (typographic skin · rendered/storage-only split),
        Luxe is photographically editorial DNA — every image surface
        the editor exposes is actually rendered by the `.fe-*` skin. So
        this test blindates both storage shape (plain-key globals for
        all 5 image paths) AND render visibility on the public preview
        for every image surface it exercises.

        Phases:
        1. perimeter invariants at TEST START — Luxe IN + Bottega
           still IN
        2. customer edits IT / EN / FR on home.headline
        3. customer edits global site.logo_word via EN — plain-keyed
           no @en: prefix
        4. customer edits SCALAR top-level `home.cover_image`
           (rendered hero on home page) — 5× assertNotIn @<locale>:
           + render on home page all 5 locales
        5. customer edits NESTED-DICT scalar `product.atelier_portrait`
           (rendered portrait on product page) — 5× assertNotIn
           + render on product page all 5 locales
        6. customer edits NESTED-DICT scalar `maison.direction_portrait`
           (rendered portrait on maison page) — 5× assertNotIn
           + render on maison page all 5 locales
        7. customer edits IMAGE-IN-DICT-ROW `collezione.products.0.image`
           (9-item catalog listing · image col) — 5× assertNotIn
           + render on collezione page all 5 locales
        8. customer edits IMAGE-IN-DICT-ROW `lookbook.looks.0.image`
           (6-item editorial grid · DIFFERENT list shape and page from
           products) — 5× assertNotIn + render on lookbook page all
           5 locales
        9. publish
        10. second user visits home + product + maison + collezione +
            lookbook on all 5 locales
        11. AR response head carries ``<html dir="rtl" lang="ar">`` on
            the `.fe-*` skin
        12. owner reopens the editor per locale · prefill + universals
        13. perimeter invariants re-checked end-of-test:
            - Luxe + Bottega still enrolled (no accidental removal)
            - 12 pre-A.15 archetypes still enrolled
            - Sensitive OUT paths REJECTED
              (collezione.filter_groups.0.options · collezione.sort_options
              · product.gallery · product.size_options · product.color_options
              · contatti.form_fields · pages · posts + col-level:
              collezione.products.0.id · collezione.products.0.available ·
              home.tiles.0.id)

        Explicitly NOT exercised here: browser walk (Step 3), coverage
        expansion, mutable rows, image per-locale, apps.commerce
        touches. Zero production-code changes.
        """
        import json as _json

        luxe = WebTemplate.objects.get(slug="luxe-fashion-store")
        p = services.create_project_from_template(owner=self.owner, template=luxe)

        # ── 1. perimeter invariants at TEST START ────────────────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            _ARCHETYPE_SCHEMAS as _SCHEMAS,
            InvalidEditableField,
            validate_key_path,
        )
        self.assertIn("fashion-editorial", _SCHEMAS,
                      "Luxe must be enrolled at lifecycle start")
        self.assertIn("fashion-editorial", _ENABLED,
                      "Luxe must be in multi-locale gate at start")
        # Bottega still IN at start (no accidental removal).
        self.assertIn("artisan-workshop", _SCHEMAS,
                      "Bottega must still be enrolled at Luxe lifecycle start")
        self.assertIn("artisan-workshop", _ENABLED,
                      "Bottega must still be in multi-locale gate at start")

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

        # ── 2. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Walk IT Luxe <em>A15bFashionLine</em>."),
            ("en", "Walk EN Luxe <em>A15bFashionLineEN</em>."),
            ("fr", "Walk FR Luxe <em>A15bFashionLineFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 3. global plain-keyed text — site.logo_word via EN ────
        r = autosave("en", {"site.logo_word": "A15b Luxe Walk Maison"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 4. scalar top-level image — home.cover_image ─────────
        # Rendered as full-bleed hero cover on home page.
        IMG_COVER = "https://walk-luxe.example/img/cover-A15b.jpg"
        r = autosave("it", {"home.cover_image": IMG_COVER})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.cover_image", r.json()["content_keys"])

        # ── 5. nested-dict scalar — product.atelier_portrait ──────
        IMG_ATELIER = "https://walk-luxe.example/img/atelier-A15b.jpg"
        r = autosave("it", {"product.atelier_portrait": IMG_ATELIER})
        self.assertEqual(r.status_code, 200)
        self.assertIn("product.atelier_portrait", r.json()["content_keys"])

        # ── 6. nested-dict scalar — maison.direction_portrait ─────
        IMG_DIRECTION = "https://walk-luxe.example/img/direction-A15b.jpg"
        r = autosave("it", {"maison.direction_portrait": IMG_DIRECTION})
        self.assertEqual(r.status_code, 200)
        self.assertIn("maison.direction_portrait", r.json()["content_keys"])

        # ── 7. image-in-dict-row collezione.products (demo catalog) ─
        # 9-item dict listing · image col · first row .0.image.
        IMG_PRODUCT = "https://walk-luxe.example/img/product-A15b.jpg"
        r = autosave("it", {"collezione.products.0.image": IMG_PRODUCT})
        self.assertEqual(r.status_code, 200)
        self.assertIn("collezione.products.0.image", r.json()["content_keys"])

        # ── 8. image-in-dict-row lookbook.looks (editorial grid) ───
        # 6-item dict listing · image col · DIFFERENT list shape from
        # products (cols n/title/outfit/credit/image vs n/name/meta/
        # drop/price/tag/image) · DIFFERENT page from collezione.
        IMG_LOOK = "https://walk-luxe.example/img/look-A15b.jpg"
        r = autosave("it", {"lookbook.looks.0.image": IMG_LOOK})
        self.assertEqual(r.status_code, 200)
        self.assertIn("lookbook.looks.0.image", r.json()["content_keys"])

        # Storage shape: 3 @<locale>:home.headline + 6 plain-keyed
        # globals (logo + 5 image paths). Zero @<locale>: on any image
        # path across all 5 locales; zero @en: on logo; zero plain-key
        # leak on home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("home.cover_image", keys)
        self.assertIn("product.atelier_portrait", keys)
        self.assertIn("maison.direction_portrait", keys)
        self.assertIn("collezione.products.0.image", keys)
        self.assertIn("lookbook.looks.0.image", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        # All 5 image paths plain-keyed across all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:home.cover_image", keys,
                             f"home.cover_image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:product.atelier_portrait", keys,
                             f"product.atelier_portrait must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:maison.direction_portrait", keys,
                             f"maison.direction_portrait must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:collezione.products.0.image", keys,
                             f"collezione.products.0.image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:lookbook.looks.0.image", keys,
                             f"lookbook.looks.0.image must NEVER be @{loc}:-prefixed")

        # ── 9. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 10. second user on every public preview locale ───────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/ecommerce/luxe-fashion-store/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override + global logo + home.cover_image
        # override visible. EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Walk IT Luxe", body_it)
        self.assertIn("A15bFashionLine", body_it)
        self.assertNotIn("A15bFashionLineEN", body_it)
        self.assertNotIn("A15bFashionLineFR", body_it)
        self.assertIn("A15b Luxe Walk Maison", body_it)
        self.assertIn(IMG_COVER, body_it,
                      "home.cover_image override must render on home page IT")

        # IT render (collezione) — collezione.products.0.image override
        # visible + universal logo.
        body_it_coll = preview_body("it", page="collezione")
        self.assertIn("A15b Luxe Walk Maison", body_it_coll)
        self.assertIn(IMG_PRODUCT, body_it_coll,
                      "collezione.products.0.image override must render on collezione page IT")

        # IT render (product) — product.atelier_portrait override
        # visible + universal logo.
        body_it_product = preview_body("it", page="product")
        self.assertIn("A15b Luxe Walk Maison", body_it_product)
        self.assertIn(IMG_ATELIER, body_it_product,
                      "product.atelier_portrait override must render on product page IT")

        # IT render (maison) — maison.direction_portrait override visible.
        body_it_maison = preview_body("it", page="maison")
        self.assertIn("A15b Luxe Walk Maison", body_it_maison)
        self.assertIn(IMG_DIRECTION, body_it_maison,
                      "maison.direction_portrait override must render on maison page IT")

        # IT render (lookbook) — lookbook.looks.0.image override visible.
        body_it_lb = preview_body("it", page="lookbook")
        self.assertIn("A15b Luxe Walk Maison", body_it_lb)
        self.assertIn(IMG_LOOK, body_it_lb,
                      "lookbook.looks.0.image override must render on lookbook page IT")

        # EN render spans home + all 4 image pages
        body_en = preview_body("en")
        self.assertIn("Walk EN Luxe", body_en)
        self.assertIn("A15bFashionLineEN", body_en)
        self.assertNotIn("Walk IT Luxe", body_en)
        self.assertIn("A15b Luxe Walk Maison", body_en)
        self.assertIn(IMG_COVER, body_en)
        self.assertIn(IMG_PRODUCT, preview_body("en", page="collezione"))
        self.assertIn(IMG_ATELIER, preview_body("en", page="product"))
        self.assertIn(IMG_DIRECTION, preview_body("en", page="maison"))
        self.assertIn(IMG_LOOK, preview_body("en", page="lookbook"))

        # FR render spans home + all 4 image pages
        body_fr = preview_body("fr")
        self.assertIn("Walk FR Luxe", body_fr)
        self.assertIn("A15bFashionLineFR", body_fr)
        self.assertIn("A15b Luxe Walk Maison", body_fr)
        self.assertIn(IMG_COVER, body_fr)
        self.assertIn(IMG_PRODUCT, preview_body("fr", page="collezione"))
        self.assertIn(IMG_ATELIER, preview_body("fr", page="product"))
        self.assertIn(IMG_DIRECTION, preview_body("fr", page="maison"))
        self.assertIn(IMG_LOOK, preview_body("fr", page="lookbook"))

        # Unedited locales — authored fallback on translatable text +
        # universals preserved across home + all 4 image pages.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Walk IT Luxe", body)
            self.assertNotIn("Walk EN Luxe", body)
            self.assertNotIn("Walk FR Luxe", body)
            self.assertIn("A15b Luxe Walk Maison", body)
            self.assertIn(IMG_COVER, body,
                          f"home.cover_image must render universally on {locale} home")
            body_coll = preview_body(locale, page="collezione")
            self.assertIn(IMG_PRODUCT, body_coll,
                          f"collezione.products.0.image must render universally on {locale} collezione")
            body_product = preview_body(locale, page="product")
            self.assertIn(IMG_ATELIER, body_product,
                          f"product.atelier_portrait must render universally on {locale} product")
            body_maison = preview_body(locale, page="maison")
            self.assertIn(IMG_DIRECTION, body_maison,
                          f"maison.direction_portrait must render universally on {locale} maison")
            body_lb = preview_body(locale, page="lookbook")
            self.assertIn(IMG_LOOK, body_lb,
                          f"lookbook.looks.0.image must render universally on {locale} lookbook")
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Luxe home",
                )

        # ── 11. AR preview (home) — `.fe-*` skin RTL invariant ────
        # 21 mature RTL rules verified Step 0.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 12. owner reopens the editor on each locale ──────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Walk IT Luxe"),
            ("en", "Walk EN Luxe"),
            ("fr", "Walk FR Luxe"),
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

        # Global text + all 3 scalar-image surfaces: overridden
        # universally, not translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Luxe editor")
        self.assertEqual(logo_field["value"], "A15b Luxe Walk Maison")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        cover_field = find_field_by_key(r_es.context["groups"], "home.cover_image")
        self.assertIsNotNone(cover_field, "home.cover_image missing from Luxe editor")
        self.assertEqual(cover_field["value"], IMG_COVER)
        self.assertTrue(cover_field["is_overridden"])
        self.assertFalse(cover_field["translatable"])

        atelier_field = find_field_by_key(r_es.context["groups"], "product.atelier_portrait")
        self.assertIsNotNone(atelier_field, "product.atelier_portrait missing from Luxe editor")
        self.assertEqual(atelier_field["value"], IMG_ATELIER)
        self.assertTrue(atelier_field["is_overridden"])
        self.assertFalse(atelier_field["translatable"])

        direction_field = find_field_by_key(r_es.context["groups"], "maison.direction_portrait")
        self.assertIsNotNone(direction_field, "maison.direction_portrait missing from Luxe editor")
        self.assertEqual(direction_field["value"], IMG_DIRECTION)
        self.assertTrue(direction_field["is_overridden"])
        self.assertFalse(direction_field["translatable"])

        # ── 13. perimeter invariants re-checked end-of-test ──────
        # Luxe + Bottega still enrolled.
        self.assertIn("fashion-editorial", _SCHEMAS,
                      "Luxe enrollment must persist through lifecycle")
        self.assertIn("fashion-editorial", _ENABLED)
        self.assertIn("artisan-workshop", _SCHEMAS,
                      "Bottega enrollment must persist through Luxe lifecycle")
        self.assertIn("artisan-workshop", _ENABLED)
        # 12 pre-A.15 archetypes also still enrolled.
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
        ):
            self.assertIn(arc, _ENABLED, f"{arc} lost enrollment mid-lifecycle")
        # Sensitive OUT paths stay rejected — re-verified runtime at
        # end-of-test per user guidance.
        for out_path in (
            # Nested list-of-str inside dict rows
            "collezione.filter_groups.0.options",
            "collezione.filter_groups.0.options.0",
            # Flat list-of-str on collezione / product pages
            "collezione.sort_options",
            "collezione.sort_options.0",
            "product.gallery",
            "product.gallery.0",
            "product.size_options",
            "product.size_options.0",
            "product.color_options",
            "product.color_options.0",
            # Form structure
            "contatti.form_fields",
            "contatti.form_fields.0.name",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
            # Col-level exclusions (structural identifiers)
            "collezione.products.0.id",
            "collezione.products.0.available",
            "home.tiles.0.id",
            "product.related_items.0.id",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Luxe complex-shape path must stay rejected: {out_path}",
            ):
                validate_key_path("fashion-editorial", out_path)

    # ------------------------------------------------------------------
    # A.16 · Step 2 — Salute (clinic) lifecycle HTTP cross-cutting ·
    # OPENS the medical-other family via staged dedicated-schema
    # progression extended to 3-phase variant (A.16 Salute opener ·
    # A.16b Benessere middle · A.16c Famiglia closer · medical-other
    # family CLOSED post-A.16c). First 3-template staged progression.
    # DUAL-OUT GUARD fully removed in A.16b + A.16c:
    # - Wellness-out removed in A.16b via
    #   `test_a16b_benessere_out_guard_was_removed_from_salute_tests`.
    # - Family-out removed in A.16c via
    #   `test_a16c_family_out_guard_was_removed_from_salute_tests`.
    # Exercises 3 image surfaces end-to-end:
    #   - studio.photo_src (scalar top-level · rendered on studio page)
    #   - home.team_ribbon_people.0.avatar (image-in-dict-row · rendered
    #     on home page · 8-row team ribbon)
    #   - medici.doctors.0.portrait (image-in-dict-row · rendered on
    #     medici page · 6-row doctor grid · DIFFERENT list shape AND
    #     DIFFERENT page from team_ribbon_people)
    # All 3 image paths plain-keyed across all 5 locales (D-098 image
    # per-locale out-of-scope).
    # ------------------------------------------------------------------

    def test_a16_salute_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Salute enrollment.

        Salute's `.cl-*` skin renders ALL 15 image surfaces (specialist-
        family precedent · no storage-only split unlike Bottega). This
        test blindates both storage shape (plain-key globals for 3 image
        paths) AND render visibility on the public preview for each
        image surface across 5 locales × 3 pages.

        Phases:
        1. perimeter invariants at TEST START — Salute IN (DUAL-OUT
           GUARD fully removed post-A.16c · medical-other CLOSED)
        2. customer edits IT / EN / FR on home.headline
        3. customer edits global site.logo_word via EN — plain-keyed
           no @en: prefix
        4. customer edits SCALAR top-level `studio.photo_src`
           (rendered photo on studio page) — 5× assertNotIn @<locale>:
           + render on studio page all 5 locales
        5. customer edits IMAGE-IN-DICT-ROW `home.team_ribbon_people.0.avatar`
           (8-row team ribbon · home page) — 5× assertNotIn + render
           on home page all 5 locales
        6. customer edits IMAGE-IN-DICT-ROW `medici.doctors.0.portrait`
           (6-row doctor grid · medici page · DIFFERENT list shape AND
           page from team_ribbon_people) — 5× assertNotIn + render
           on medici page all 5 locales
        7. publish
        8. second user visits home + studio + medici on all 5 locales
        9. AR response head carries ``<html dir="rtl" lang="ar">`` on
           the `.cl-*` skin
        10. owner reopens the editor per locale · prefill + universals
        11. perimeter invariants re-checked end-of-test:
            - Salute + 14 pre-A.16 archetypes still enrolled
            - Medical-other family CLOSED post-A.16c · DUAL-OUT GUARD
              fully consumed (wellness-out removed in A.16b ·
              family-out removed in A.16c · sub-recipe 2-removal-phase
              variant complete · 5th staged dedicated-schema closure
              after real-estate + portfolio + restaurant-continuation +
              ecommerce)
            - Sensitive OUT paths REJECTED (raw icon_svg + bool
              is_popular + nested includes/items/tags + form structures
              + flat str-lists + pages + posts)

        Explicitly NOT exercised here: browser walk (Step 3), Benessere/
        Famiglia editor work, coverage expansion, mutable rows, image
        per-locale, apps.commerce / clinic-admin touches. Zero production-
        code changes.
        """
        import json as _json

        salute = WebTemplate.objects.get(slug="salute-studio-medico")
        p = services.create_project_from_template(owner=self.owner, template=salute)

        # ── 1. perimeter invariants at TEST START ────────────────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            _ARCHETYPE_SCHEMAS as _SCHEMAS,
            InvalidEditableField,
            validate_key_path,
        )
        self.assertIn("clinic", _SCHEMAS,
                      "Salute must be enrolled at lifecycle start")
        self.assertIn("clinic", _ENABLED,
                      "Salute must be in multi-locale gate at start")
        # DUAL-OUT GUARD fully removed in A.16b + A.16c:
        # - Wellness-out guard removed in A.16b via symmetric inversion —
        #   see `test_a16b_benessere_out_guard_was_removed_from_salute_tests`.
        # - Family-out guard removed in A.16c via symmetric inversion —
        #   see `test_a16c_family_out_guard_was_removed_from_salute_tests`.
        # Medical-other family OFFICIALLY CLOSED after A.16c.

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

        # ── 2. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Walk IT Salute <em>A16ClinicLine</em>."),
            ("en", "Walk EN Salute <em>A16ClinicLineEN</em>."),
            ("fr", "Walk FR Salute <em>A16ClinicLineFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 3. global plain-keyed text — site.logo_word via EN ────
        r = autosave("en", {"site.logo_word": "A16 Salute Walk Studio"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 4. scalar top-level image — studio.photo_src ─────────
        # Rendered as photo block on studio page.
        IMG_PHOTO = "https://walk-salute.example/img/photo-A16.jpg"
        r = autosave("it", {"studio.photo_src": IMG_PHOTO})
        self.assertEqual(r.status_code, 200)
        self.assertIn("studio.photo_src", r.json()["content_keys"])

        # ── 5. image-in-dict-row team_ribbon_people (home page) ───
        # 8-row team ribbon · avatar col · first row .0.avatar.
        IMG_AVATAR = "https://walk-salute.example/img/avatar-A16.jpg"
        r = autosave("it", {"home.team_ribbon_people.0.avatar": IMG_AVATAR})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.team_ribbon_people.0.avatar", r.json()["content_keys"])

        # ── 6. image-in-dict-row medici.doctors (medici page) ─────
        # 6-row doctor grid · portrait col · DIFFERENT list shape from
        # team_ribbon_people (cols name/role/credentials/portrait vs
        # name/specialty/avatar) AND DIFFERENT page (medici vs home).
        IMG_PORTRAIT = "https://walk-salute.example/img/portrait-A16.jpg"
        r = autosave("it", {"medici.doctors.0.portrait": IMG_PORTRAIT})
        self.assertEqual(r.status_code, 200)
        self.assertIn("medici.doctors.0.portrait", r.json()["content_keys"])

        # Storage shape: 3 @<locale>:home.headline + 4 plain-keyed
        # globals (logo + 3 image paths). Zero @<locale>: on any image
        # path across all 5 locales; zero @en: on logo; zero plain-key
        # leak on home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("studio.photo_src", keys)
        self.assertIn("home.team_ribbon_people.0.avatar", keys)
        self.assertIn("medici.doctors.0.portrait", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        # All 3 image paths plain-keyed across all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:studio.photo_src", keys,
                             f"studio.photo_src must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:home.team_ribbon_people.0.avatar", keys,
                             f"home.team_ribbon_people.0.avatar must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:medici.doctors.0.portrait", keys,
                             f"medici.doctors.0.portrait must NEVER be @{loc}:-prefixed")

        # ── 7. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 8. second user on every public preview locale ────────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/medical/salute-studio-medico/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override + global logo +
        # home.team_ribbon_people.0.avatar override visible. EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Walk IT Salute", body_it)
        self.assertIn("A16ClinicLine", body_it)
        self.assertNotIn("A16ClinicLineEN", body_it)
        self.assertNotIn("A16ClinicLineFR", body_it)
        self.assertIn("A16 Salute Walk Studio", body_it)
        self.assertIn(IMG_AVATAR, body_it,
                      "home.team_ribbon_people.0.avatar override must render on home page IT")

        # IT render (studio) — studio.photo_src override visible +
        # universal logo.
        body_it_studio = preview_body("it", page="studio")
        self.assertIn("A16 Salute Walk Studio", body_it_studio)
        self.assertIn(IMG_PHOTO, body_it_studio,
                      "studio.photo_src override must render on studio page IT")

        # IT render (medici) — medici.doctors.0.portrait override visible.
        body_it_medici = preview_body("it", page="medici")
        self.assertIn("A16 Salute Walk Studio", body_it_medici)
        self.assertIn(IMG_PORTRAIT, body_it_medici,
                      "medici.doctors.0.portrait override must render on medici page IT")

        # EN render spans home + studio + medici
        body_en = preview_body("en")
        self.assertIn("Walk EN Salute", body_en)
        self.assertIn("A16ClinicLineEN", body_en)
        self.assertNotIn("Walk IT Salute", body_en)
        self.assertIn("A16 Salute Walk Studio", body_en)
        self.assertIn(IMG_AVATAR, body_en)
        self.assertIn(IMG_PHOTO, preview_body("en", page="studio"))
        self.assertIn(IMG_PORTRAIT, preview_body("en", page="medici"))

        # FR render spans home + studio + medici
        body_fr = preview_body("fr")
        self.assertIn("Walk FR Salute", body_fr)
        self.assertIn("A16ClinicLineFR", body_fr)
        self.assertIn("A16 Salute Walk Studio", body_fr)
        self.assertIn(IMG_AVATAR, body_fr)
        self.assertIn(IMG_PHOTO, preview_body("fr", page="studio"))
        self.assertIn(IMG_PORTRAIT, preview_body("fr", page="medici"))

        # Unedited locales — authored fallback on translatable text +
        # universals preserved across home + studio + medici.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Walk IT Salute", body)
            self.assertNotIn("Walk EN Salute", body)
            self.assertNotIn("Walk FR Salute", body)
            self.assertIn("A16 Salute Walk Studio", body)
            self.assertIn(IMG_AVATAR, body,
                          f"home.team_ribbon_people.0.avatar must render universally on {locale} home")
            body_studio = preview_body(locale, page="studio")
            self.assertIn(IMG_PHOTO, body_studio,
                          f"studio.photo_src must render universally on {locale} studio")
            body_medici = preview_body(locale, page="medici")
            self.assertIn(IMG_PORTRAIT, body_medici,
                          f"medici.doctors.0.portrait must render universally on {locale} medici")
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Salute home",
                )

        # ── 9. AR preview (home) — `.cl-*` skin RTL invariant ────
        # 18 mature RTL rules verified Step 0.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 10. owner reopens the editor on each locale ──────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Walk IT Salute"),
            ("en", "Walk EN Salute"),
            ("fr", "Walk FR Salute"),
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

        # Global text + scalar image: overridden universally,
        # not translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Salute editor")
        self.assertEqual(logo_field["value"], "A16 Salute Walk Studio")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        photo_field = find_field_by_key(r_es.context["groups"], "studio.photo_src")
        self.assertIsNotNone(photo_field, "studio.photo_src missing from Salute editor")
        self.assertEqual(photo_field["value"], IMG_PHOTO)
        self.assertTrue(photo_field["is_overridden"])
        self.assertFalse(photo_field["translatable"])

        # ── 11. perimeter invariants re-checked end-of-test ──────
        # DUAL-OUT GUARD fully removed in A.16b + A.16c · medical-other
        # family OFFICIALLY CLOSED. Sub-recipe 2-removal-phase variant
        # (first 3-template staged progression) completed.
        # - Wellness-out guard removed in A.16b via
        #   `test_a16b_benessere_out_guard_was_removed_from_salute_tests`
        # - Family-out guard removed in A.16c via
        #   `test_a16c_family_out_guard_was_removed_from_salute_tests`
        # Salute still enrolled (no accidental removal).
        self.assertIn("clinic", _SCHEMAS,
                      "Salute enrollment must persist through lifecycle")
        self.assertIn("clinic", _ENABLED)
        # 14 pre-A.16 archetypes also still enrolled.
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop", "fashion-editorial",
        ):
            self.assertIn(arc, _ENABLED, f"{arc} lost enrollment mid-lifecycle")
        # Sensitive OUT paths stay rejected — re-verified runtime at
        # end-of-test per user guidance.
        for out_path in (
            # Raw SVG OUT (5th OUT category precedent)
            "home.specialties.0.icon_svg",
            "home.specialties.7.icon_svg",
            "servizi.services.0.icon_svg",
            "servizi.services.9.icon_svg",
            # Bool flag OUT (Luxe available precedent)
            "prevenzione.packages.0.is_popular",
            # Nested list-of-str inside dict rows (Juris precedent)
            "servizi.services.0.items",
            "servizi.services.0.items.0",
            "prevenzione.packages.0.includes",
            "prevenzione.packages.0.includes.0",
            "home.prevenzione_cards.0.includes",
            "medici.doctors.0.tags",
            "medici.doctors.0.tags.0",
            # Form structures (Juris/Gusto/Bottega/Luxe precedent)
            "contatti.form_fields",
            "contatti.form_fields.0.name",
            "prenota.form_fields",
            "prenota.form_fields.0.name",
            "prenota.form_sections",
            "prenota.form_sections.0.num",
            # Flat list-of-str
            "site.hours_footer_rows",
            "site.foot_extra_rows",
            "home.partners",
            "prenota.trust",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Salute complex-shape path must stay rejected: {out_path}",
            ):
                validate_key_path("clinic", out_path)

    # ------------------------------------------------------------------
    # A.16b · Step 2 — Benessere (wellness) lifecycle HTTP cross-
    # cutting · MIDDLE phase of the medical-other 3-phase staged
    # dedicated-schema progression (A.16 Salute opener · A.16b Benessere
    # middle · A.16c Famiglia closer). Exercises 3 image surfaces end-
    # to-end across 3 distinct pages:
    #   - home.hero_image (scalar top-level · rendered hero on home)
    #   - ambienti.rooms.0.image (image-in-dict-row · rendered on
    #     novel `gallery` page · 8-row largest image list)
    #   - professionisti.people.0.portrait (image-in-dict-row ·
    #     rendered on team page · DIFFERENT list + DIFFERENT page
    #     from ambienti.rooms)
    # All 3 image paths plain-keyed across all 5 locales (D-098 image
    # per-locale out-of-scope). DUAL-OUT GUARD fully removed post-A.16c
    # (wellness-out removed in A.16b · family-out removed in A.16c ·
    # medical-other family CLOSED · first 3-template staged progression
    # complete).
    # ------------------------------------------------------------------

    def test_a16b_benessere_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Benessere enrollment.

        Benessere's `.we-*` skin renders ALL 19 image surfaces (editorial
        olistico skin · no storage-only split · same profile as Luxe/
        Salute). This test blindates both storage shape (plain-key
        globals for 3 image paths) AND render visibility on the public
        preview for each image surface across 5 locales × 3 pages ·
        including the **novel `gallery` page kind** (ambienti).

        Phases:
        1. perimeter invariants at TEST START — Benessere IN +
           Salute still IN (DUAL-OUT GUARD fully removed post-A.16c ·
           medical-other family CLOSED · sub-recipe 2-removal-phase
           variant complete)
        2. customer edits IT / EN / FR on home.headline
        3. customer edits global site.logo_word via EN — plain-keyed
           no @en: prefix
        4. customer edits SCALAR top-level `home.hero_image`
           (rendered hero on home page) — 5× assertNotIn @<locale>:
           + render on home page all 5 locales
        5. customer edits IMAGE-IN-DICT-ROW `ambienti.rooms.0.image`
           (8-row largest image list · novel `gallery` page kind) —
           5× assertNotIn + render on ambienti page all 5 locales
        6. customer edits IMAGE-IN-DICT-ROW `professionisti.people.0.portrait`
           (5-row doctor-like portrait grid · DIFFERENT list + DIFFERENT
           page from ambienti.rooms) — 5× assertNotIn + render
           on professionisti page all 5 locales
        7. publish
        8. second user visits home + ambienti + professionisti on all
           5 locales
        9. AR response head carries ``<html dir="rtl" lang="ar">`` on
           the `.we-*` skin
        10. owner reopens the editor per locale · prefill + universals
        11. perimeter invariants re-checked end-of-test:
            - Benessere + Salute + 14 pre-A.16 archetypes still enrolled
            - Medical-other family CLOSED post-A.16c · DUAL-OUT GUARD
              fully consumed (wellness-out removed in A.16b ·
              family-out removed in A.16c · sub-recipe 2-removal-phase
              variant complete)
            - Sensitive OUT paths REJECTED (calendar bool flags × 4 +
              nested str-lists × 4 + form structures × 5 + home.ambients
              tuple-with-image × 3 + flat str-lists × 4 + pages/posts × 2)

        Explicitly NOT exercised here: browser walk (Step 3), coverage
        expansion, home.ambients tuple-with-image (deferred), mutable
        rows, image per-locale, apps.commerce / clinic-admin touches.
        Zero production-code changes.
        """
        import json as _json

        benessere = WebTemplate.objects.get(slug="benessere-centro-olistico")
        p = services.create_project_from_template(owner=self.owner, template=benessere)

        # ── 1. perimeter invariants at TEST START ────────────────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            _ARCHETYPE_SCHEMAS as _SCHEMAS,
            InvalidEditableField,
            validate_key_path,
        )
        self.assertIn("wellness", _SCHEMAS,
                      "Benessere must be enrolled at lifecycle start")
        self.assertIn("wellness", _ENABLED,
                      "Benessere must be in multi-locale gate at start")
        # Salute still IN at start (no accidental removal).
        self.assertIn("clinic", _SCHEMAS,
                      "Salute must still be enrolled at Benessere lifecycle start")
        self.assertIn("clinic", _ENABLED,
                      "Salute must still be in multi-locale gate at start")
        # Family-out guard removed in A.16c · medical-other family CLOSED ·
        # see `test_a16c_family_out_guard_was_removed_from_salute_tests`.

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

        # ── 2. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Walk IT Benessere <em>A16bWellnessLine</em>."),
            ("en", "Walk EN Benessere <em>A16bWellnessLineEN</em>."),
            ("fr", "Walk FR Benessere <em>A16bWellnessLineFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 3. global plain-keyed text — site.logo_word via EN ────
        r = autosave("en", {"site.logo_word": "A16b Benessere Walk Studio"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 4. scalar top-level image — home.hero_image ──────────
        # Rendered as hero figure on home page.
        IMG_HERO = "https://walk-benessere.example/img/hero-A16b.jpg"
        r = autosave("it", {"home.hero_image": IMG_HERO})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.hero_image", r.json()["content_keys"])

        # ── 5. image-in-dict-row ambienti.rooms (novel gallery page) ─
        # 8-row largest image list · image col · first row .0.image ·
        # rendered on novel `gallery` page kind (ambienti page).
        IMG_ROOM = "https://walk-benessere.example/img/room-A16b.jpg"
        r = autosave("it", {"ambienti.rooms.0.image": IMG_ROOM})
        self.assertEqual(r.status_code, 200)
        self.assertIn("ambienti.rooms.0.image", r.json()["content_keys"])

        # ── 6. image-in-dict-row professionisti.people (team page) ─
        # 5-row portrait grid · DIFFERENT list shape from ambienti.rooms
        # (cols name/role/portrait/bio/quote vs span/tag/title/sub/image)
        # AND DIFFERENT page from ambienti (team vs gallery).
        IMG_PORTRAIT = "https://walk-benessere.example/img/portrait-A16b.jpg"
        r = autosave("it", {"professionisti.people.0.portrait": IMG_PORTRAIT})
        self.assertEqual(r.status_code, 200)
        self.assertIn("professionisti.people.0.portrait", r.json()["content_keys"])

        # Storage shape: 3 @<locale>:home.headline + 4 plain-keyed
        # globals (logo + 3 image paths). Zero @<locale>: on any image
        # path across all 5 locales; zero @en: on logo; zero plain-key
        # leak on home.headline.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        self.assertIn("site.logo_word", keys)
        self.assertIn("home.hero_image", keys)
        self.assertIn("ambienti.rooms.0.image", keys)
        self.assertIn("professionisti.people.0.portrait", keys)
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        # All 3 image paths plain-keyed across all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:home.hero_image", keys,
                             f"home.hero_image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:ambienti.rooms.0.image", keys,
                             f"ambienti.rooms.0.image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:professionisti.people.0.portrait", keys,
                             f"professionisti.people.0.portrait must NEVER be @{loc}:-prefixed")

        # ── 7. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 8. second user on every public preview locale ────────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/medical/benessere-centro-olistico/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override + global logo + home.hero_image
        # override visible. EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Walk IT Benessere", body_it)
        self.assertIn("A16bWellnessLine", body_it)
        self.assertNotIn("A16bWellnessLineEN", body_it)
        self.assertNotIn("A16bWellnessLineFR", body_it)
        self.assertIn("A16b Benessere Walk Studio", body_it)
        self.assertIn(IMG_HERO, body_it,
                      "home.hero_image override must render on home page IT")

        # IT render (ambienti · novel gallery page) — ambienti.rooms.0.image
        # override visible + universal logo.
        body_it_ambienti = preview_body("it", page="ambienti")
        self.assertIn("A16b Benessere Walk Studio", body_it_ambienti)
        self.assertIn(IMG_ROOM, body_it_ambienti,
                      "ambienti.rooms.0.image override must render on ambienti (gallery) page IT")

        # IT render (professionisti · team page) — professionisti.people.0.portrait
        # override visible.
        body_it_team = preview_body("it", page="professionisti")
        self.assertIn("A16b Benessere Walk Studio", body_it_team)
        self.assertIn(IMG_PORTRAIT, body_it_team,
                      "professionisti.people.0.portrait override must render on professionisti page IT")

        # EN render spans home + ambienti + professionisti
        body_en = preview_body("en")
        self.assertIn("Walk EN Benessere", body_en)
        self.assertIn("A16bWellnessLineEN", body_en)
        self.assertNotIn("Walk IT Benessere", body_en)
        self.assertIn("A16b Benessere Walk Studio", body_en)
        self.assertIn(IMG_HERO, body_en)
        self.assertIn(IMG_ROOM, preview_body("en", page="ambienti"))
        self.assertIn(IMG_PORTRAIT, preview_body("en", page="professionisti"))

        # FR render spans home + ambienti + professionisti
        body_fr = preview_body("fr")
        self.assertIn("Walk FR Benessere", body_fr)
        self.assertIn("A16bWellnessLineFR", body_fr)
        self.assertIn("A16b Benessere Walk Studio", body_fr)
        self.assertIn(IMG_HERO, body_fr)
        self.assertIn(IMG_ROOM, preview_body("fr", page="ambienti"))
        self.assertIn(IMG_PORTRAIT, preview_body("fr", page="professionisti"))

        # Unedited locales — authored fallback on translatable text +
        # universals preserved across home + ambienti + professionisti.
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Walk IT Benessere", body)
            self.assertNotIn("Walk EN Benessere", body)
            self.assertNotIn("Walk FR Benessere", body)
            self.assertIn("A16b Benessere Walk Studio", body)
            self.assertIn(IMG_HERO, body,
                          f"home.hero_image must render universally on {locale} home")
            body_ambienti = preview_body(locale, page="ambienti")
            self.assertIn(IMG_ROOM, body_ambienti,
                          f"ambienti.rooms.0.image must render universally on {locale} ambienti")
            body_team = preview_body(locale, page="professionisti")
            self.assertIn(IMG_PORTRAIT, body_team,
                          f"professionisti.people.0.portrait must render universally on {locale} professionisti")
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Benessere home",
                )

        # ── 9. AR preview (home) — `.we-*` skin RTL invariant ────
        # 13 mature RTL rules verified Step 0.
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 10. owner reopens the editor on each locale ──────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Walk IT Benessere"),
            ("en", "Walk EN Benessere"),
            ("fr", "Walk FR Benessere"),
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

        # Global text + scalar hero image: overridden universally, not
        # translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Benessere editor")
        self.assertEqual(logo_field["value"], "A16b Benessere Walk Studio")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        hero_field = find_field_by_key(r_es.context["groups"], "home.hero_image")
        self.assertIsNotNone(hero_field, "home.hero_image missing from Benessere editor")
        self.assertEqual(hero_field["value"], IMG_HERO)
        self.assertTrue(hero_field["is_overridden"])
        self.assertFalse(hero_field["translatable"])

        # ── 11. perimeter invariants re-checked end-of-test ──────
        # Family-out guard removed in A.16c · medical-other family CLOSED ·
        # see `test_a16c_family_out_guard_was_removed_from_salute_tests`.
        # Benessere + Salute still enrolled (no accidental removal).
        self.assertIn("wellness", _SCHEMAS,
                      "Benessere enrollment must persist through lifecycle")
        self.assertIn("wellness", _ENABLED)
        self.assertIn("clinic", _SCHEMAS,
                      "Salute enrollment must persist through Benessere lifecycle")
        self.assertIn("clinic", _ENABLED)
        # 14 pre-A.16 archetypes also still enrolled.
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop", "fashion-editorial",
        ):
            self.assertIn(arc, _ENABLED, f"{arc} lost enrollment mid-lifecycle")
        # Sensitive OUT paths stay rejected — re-verified runtime at
        # end-of-test per user guidance.
        for out_path in (
            # Calendar bool flags OUT (Luxe available + Salute is_popular precedent)
            "home.calendar.0.has_slots",
            "home.calendar.0.soldout",
            "prenota.calendar.0.has_slots",
            "prenota.calendar.0.soldout",
            # Nested list-of-str inside dict rows (Juris precedent)
            "home.calendar.0.slots",
            "prenota.calendar.0.slots",
            "rituali.packages.0.includes",
            "professionisti.people.0.tags",
            # Form structures (Juris/Gusto/Bottega/Luxe/Salute precedent)
            "contatti.form_placeholders",
            "contatti.form_helpers",
            "contatti.form_fields",
            "contatti.form_fields.interest_options",
            "prenota.form_fields",
            "prenota.form_fields.0.name",
            "prenota.form_sections",
            # DEFERRED novel shape (home.ambients tuple-with-image)
            "home.ambients",
            "home.ambients.0",
            "home.ambients.0.0",
            # Flat list-of-str
            "site.hours_footer_rows",
            "home.hero_meta",
            "home.press",
            "prenota.why",
            # Top-level navigation + empty posts
            "pages",
            "posts",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Benessere complex-shape path must stay rejected: {out_path}",
            ):
                validate_key_path("wellness", out_path)

    # ------------------------------------------------------------------
    # A.16c · Step 2 — Famiglia (family) lifecycle HTTP cross-cutting ·
    # CLOSER phase of the medical-other 3-phase staged dedicated-schema
    # progression (A.16 Salute opener · A.16b Benessere middle · A.16c
    # Famiglia closer · medical-other family CLOSED). Exercises 4
    # surfaces end-to-end across 3 distinct pages:
    #   - home.hero_image (scalar top-level · rendered hero on home)
    #   - home.gallery.0.src (image-in-dict-row · NOVEL `src` col name ·
    #     rendered on home · same page as hero but different list)
    #   - pediatre.doctors.0.portrait (image-in-dict-row · rendered on
    #     pediatre page · DIFFERENT list + DIFFERENT page)
    #   - **crescita.topics.0.items.0.q** (DEEP-PATH text override ·
    #     rendered on crescita FAQ page · Sapore precedent mirror ·
    #     mechanical reuse of f66ac24 render-side fix · novel-for-
    #     Famiglia surface)
    # All 3 image paths plain-keyed across all 5 locales (D-098 image
    # per-locale out-of-scope). Deep-path text cell translatable via
    # `@<locale>:` storage (verified via direct autosave · rendered
    # end-to-end on public crescita page). **ALL 3 MEDICAL-OTHER
    # ARCHETYPES IN** (clinic + wellness + family) at start AND end of
    # test (medical-other family CLOSED · dual-out guard fully removed).
    # ------------------------------------------------------------------

    def test_a16c_family_full_multilocale_lifecycle_end_to_end(self):
        """End-to-end HTTP lifecycle for the Famiglia enrollment.

        Famiglia's `.fm-*` skin renders ALL 16 image surfaces + the
        deep-path crescita topics Q&A cells (pediatric skin · no
        storage-only split). This test blindates both storage shape
        (plain-key globals for 3 image paths + per-locale for deep-path
        text cell) AND render visibility on the public preview for
        each surface across 5 locales × 3 pages · including the
        **novel deep-path tuple-in-dict-list editing** (Sapore precedent
        mirror · mechanical reuse of f66ac24).

        Phases:
        1. perimeter invariants at TEST START — ALL 3 medical-other
           archetypes IN (clinic + wellness + family · medical-other
           family CLOSED post-A.16c · DUAL-OUT GUARD fully removed)
        2. customer edits IT / EN / FR on home.headline
        3. customer edits global site.logo_word via EN — plain-keyed
           no @en: prefix
        4. customer edits SCALAR top-level `home.hero_image`
           (rendered hero on home page) — 5× assertNotIn @<locale>:
           + render on home page all 5 locales
        5. customer edits IMAGE-IN-DICT-ROW `home.gallery.0.src`
           (5-row gallery · NOVEL `src` col name · same home page as
           hero but different list shape) — 5× assertNotIn + render
           on home page all 5 locales
        6. customer edits IMAGE-IN-DICT-ROW `pediatre.doctors.0.portrait`
           (4-row doctor grid · DIFFERENT list + DIFFERENT page from
           gallery) — 5× assertNotIn + render on pediatre page all 5
           locales
        7. customer edits **DEEP-PATH** `crescita.topics.0.items.0.q`
           (Sapore precedent mirror · tuple-in-dict-list cell · global
           plain-key · non-translatable per D-098 structured-list
           policy · same as all STRUCTURED_FIELD_SHAPES cells) — single
           plain-key override · renders universally across 5 locales
           on crescita page
        8. publish
        9. second user visits home + pediatre + crescita on all 5
           locales
        10. AR response head carries ``<html dir="rtl" lang="ar">`` on
            the `.fm-*` skin (6 RTL rules · lowest of enrolled ·
            skin-level check only)
        11. owner reopens the editor per locale · prefill + universals
        12. perimeter invariants re-checked end-of-test:
            - ALL 3 medical-other (clinic + wellness + family) IN
              (medical-other family CLOSED · DUAL-OUT GUARD fully
              consumed · sub-recipe 2-removal-phase variant complete)
            - 14 pre-A.16 archetypes still enrolled
            - Sensitive OUT paths REJECTED (form structures · flat
              str-lists · nested str-lists · deep-path parent col ·
              pages · posts)

        Explicitly NOT exercised here: browser walk (Step 3), Aura/
        Elevate editor work, coverage expansion, mutable rows, image
        per-locale, apps.commerce / clinic-admin touches, home.ambients
        novel shape widening (deferred from A.16b). Zero production-
        code changes.
        """
        import json as _json

        famiglia = WebTemplate.objects.get(slug="famiglia-pediatria")
        p = services.create_project_from_template(owner=self.owner, template=famiglia)

        # ── 1. perimeter invariants at TEST START ────────────────
        from apps.editor.schema import (
            _MULTILOCALE_ENABLED_ARCHETYPES as _ENABLED,
            _ARCHETYPE_SCHEMAS as _SCHEMAS,
            InvalidEditableField,
            validate_key_path,
        )
        # Medical-other family CLOSED · all 3 archetypes IN.
        for arc in ("clinic", "wellness", "family"):
            self.assertIn(arc, _SCHEMAS,
                          f"{arc} must be enrolled at lifecycle start · medical-other CLOSED")
            self.assertIn(arc, _ENABLED,
                          f"{arc} must be in multi-locale gate at start · medical-other CLOSED")

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

        # ── 2. three translatable locales on home.headline ────────
        for locale, headline in (
            ("it", "Walk IT Famiglia <em>A16cFamilyLine</em>."),
            ("en", "Walk EN Famiglia <em>A16cFamilyLineEN</em>."),
            ("fr", "Walk FR Famiglia <em>A16cFamilyLineFR</em>."),
        ):
            r = autosave(locale, {"home.headline": headline})
            self.assertEqual(r.status_code, 200)
            self.assertIn(f"@{locale}:home.headline", r.json()["content_keys"])

        # ── 3. global plain-keyed text — site.logo_word via EN ────
        r = autosave("en", {"site.logo_word": "A16c Famiglia Walk Studio"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("site.logo_word", r.json()["content_keys"])

        # ── 4. scalar top-level image — home.hero_image ──────────
        IMG_HERO = "https://walk-famiglia.example/img/hero-A16c.jpg"
        r = autosave("it", {"home.hero_image": IMG_HERO})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.hero_image", r.json()["content_keys"])

        # ── 5. image-in-dict-row home.gallery (NOVEL `src` col) ──
        # 5-row gallery · NOVEL col name `src` (vs prior image/portrait/
        # avatar across 14 enrolled archetypes) · same home page as
        # hero_image but DIFFERENT list shape.
        IMG_GALLERY = "https://walk-famiglia.example/img/gallery-A16c.jpg"
        r = autosave("it", {"home.gallery.0.src": IMG_GALLERY})
        self.assertEqual(r.status_code, 200)
        self.assertIn("home.gallery.0.src", r.json()["content_keys"])

        # ── 6. image-in-dict-row pediatre.doctors (team page) ────
        # 4-row doctor grid · DIFFERENT list shape from home.gallery
        # (cols name/role/tag/bio/exp_label/exp_value/wa_label/portrait
        # vs cap/src) AND DIFFERENT page (pediatre vs home).
        IMG_PORTRAIT = "https://walk-famiglia.example/img/portrait-A16c.jpg"
        r = autosave("it", {"pediatre.doctors.0.portrait": IMG_PORTRAIT})
        self.assertEqual(r.status_code, 200)
        self.assertIn("pediatre.doctors.0.portrait", r.json()["content_keys"])

        # ── 7. DEEP-PATH text override — crescita.topics.0.items.0.q
        # First deep-path override in Famiglia context · Sapore
        # precedent mirror (menu.sections.{i}.dishes pattern) ·
        # mechanical reuse of f66ac24 render-side fix. Deep-path cells
        # inside STRUCTURED_FIELD_SHAPES are GLOBAL (plain-keyed · non-
        # translatable per D-098 policy · same as Sapore dish cells
        # and every other structured-list cell). Single override
        # applies universally to all 5 locales. Rendered via faq.html
        # `{% for q, a in topic.items %}` skin loop.
        Q_OVERRIDE = "Walk · deep-path Q override A16c?"
        r = autosave("it", {"crescita.topics.0.items.0.q": Q_OVERRIDE})
        self.assertEqual(r.status_code, 200, "Deep-path autosave failed")
        self.assertIn("crescita.topics.0.items.0.q",
                      r.json()["content_keys"])

        # Storage shape verification.
        keys = set(p.content_overrides.values_list("key_path", flat=True))
        # Translatable per-locale
        self.assertIn("@it:home.headline", keys)
        self.assertIn("@en:home.headline", keys)
        self.assertIn("@fr:home.headline", keys)
        # Plain-keyed globals (incl. deep-path cell · structured-list
        # policy · Sapore precedent)
        self.assertIn("site.logo_word", keys)
        self.assertIn("home.hero_image", keys)
        self.assertIn("home.gallery.0.src", keys)
        self.assertIn("pediatre.doctors.0.portrait", keys)
        self.assertIn("crescita.topics.0.items.0.q", keys)
        # Zero plain-key leak on translatable paths · zero @<locale>
        # leak on structured-list cells
        self.assertNotIn("home.headline", keys)
        self.assertNotIn("@en:site.logo_word", keys)
        # All 3 image paths + deep-path text cell plain-keyed across
        # all 5 locales.
        for loc in ("it", "en", "fr", "es", "ar"):
            self.assertNotIn(f"@{loc}:home.hero_image", keys,
                             f"home.hero_image must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:home.gallery.0.src", keys,
                             f"home.gallery.0.src must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:pediatre.doctors.0.portrait", keys,
                             f"pediatre.doctors.0.portrait must NEVER be @{loc}:-prefixed")
            self.assertNotIn(f"@{loc}:crescita.topics.0.items.0.q", keys,
                             f"deep-path cell must NEVER be @{loc}:-prefixed · structured-list policy")

        # ── 8. publish ───────────────────────────────────────────
        services.publish_project(project=p, editor=self.owner)
        p.refresh_from_db()
        self.assertEqual(p.status, CustomerProject.Status.PUBLISHED)

        # ── 9. second user on every public preview locale ────────
        self.client.logout()
        self.client.login(username="other", password="x")

        def preview_body(locale, page=None):
            suffix = f"{page}/" if page else ""
            url = (
                f"/templates/medical/famiglia-pediatria/preview/"
                f"{suffix}?project={p.uuid}&lang={locale}"
            )
            r = self.client.get(url)
            self.assertEqual(r.status_code, 200)
            return r.content.decode("utf-8", "ignore")

        # IT render (home) — IT override + global logo + home.hero_image
        # + home.gallery.0.src overrides visible. EN/FR absent.
        body_it = preview_body("it")
        self.assertIn("Walk IT Famiglia", body_it)
        self.assertIn("A16cFamilyLine", body_it)
        self.assertNotIn("A16cFamilyLineEN", body_it)
        self.assertNotIn("A16cFamilyLineFR", body_it)
        self.assertIn("A16c Famiglia Walk Studio", body_it)
        self.assertIn(IMG_HERO, body_it,
                      "home.hero_image override must render on home page IT")
        self.assertIn(IMG_GALLERY, body_it,
                      "home.gallery.0.src override must render on home page IT (novel src col)")

        # IT render (pediatre) — pediatre.doctors.0.portrait override.
        body_it_pediatre = preview_body("it", page="pediatre")
        self.assertIn("A16c Famiglia Walk Studio", body_it_pediatre)
        self.assertIn(IMG_PORTRAIT, body_it_pediatre,
                      "pediatre.doctors.0.portrait override must render on pediatre page IT")

        # IT render (crescita · novel FAQ page) — DEEP-PATH override
        # visible in faq.html Q&A loop. Universal logo + single global
        # Q override (plain-keyed · renders universally on all 5 locales).
        body_it_crescita = preview_body("it", page="crescita")
        self.assertIn("A16c Famiglia Walk Studio", body_it_crescita)
        self.assertIn(Q_OVERRIDE, body_it_crescita,
                      "crescita.topics.0.items.0.q override must render "
                      "on crescita FAQ page · DEEP-PATH end-to-end · Sapore "
                      "precedent mirror · f66ac24 mechanical reuse")

        # EN render spans home + pediatre + crescita
        body_en = preview_body("en")
        self.assertIn("Walk EN Famiglia", body_en)
        self.assertIn("A16cFamilyLineEN", body_en)
        self.assertNotIn("Walk IT Famiglia", body_en)
        self.assertIn("A16c Famiglia Walk Studio", body_en)
        self.assertIn(IMG_HERO, body_en)
        self.assertIn(IMG_GALLERY, body_en)
        self.assertIn(IMG_PORTRAIT, preview_body("en", page="pediatre"))
        # Deep-path override renders universally (plain-key global) —
        # visible on EN locale too (no per-locale scoping).
        self.assertIn(Q_OVERRIDE, preview_body("en", page="crescita"),
                      "crescita deep-path override universal on EN (plain-key)")

        # FR render spans home + pediatre + crescita
        body_fr = preview_body("fr")
        self.assertIn("Walk FR Famiglia", body_fr)
        self.assertIn("A16cFamilyLineFR", body_fr)
        self.assertIn("A16c Famiglia Walk Studio", body_fr)
        self.assertIn(IMG_HERO, body_fr)
        self.assertIn(IMG_GALLERY, body_fr)
        self.assertIn(IMG_PORTRAIT, preview_body("fr", page="pediatre"))
        self.assertIn(Q_OVERRIDE, preview_body("fr", page="crescita"),
                      "crescita deep-path override universal on FR (plain-key)")

        # Unedited locales — authored fallback on translatable text +
        # universals preserved across home + pediatre + crescita.
        # Deep-path global override renders universally on ES + AR too
        # (plain-key · no per-locale scoping).
        from apps.catalog import template_content as _tc
        for locale in ("es", "ar"):
            body = preview_body(locale)
            self.assertNotIn("Walk IT Famiglia", body)
            self.assertNotIn("Walk EN Famiglia", body)
            self.assertNotIn("Walk FR Famiglia", body)
            self.assertIn("A16c Famiglia Walk Studio", body)
            self.assertIn(IMG_HERO, body,
                          f"home.hero_image must render universally on {locale} home")
            self.assertIn(IMG_GALLERY, body,
                          f"home.gallery.0.src must render universally on {locale} home")
            body_pediatre = preview_body(locale, page="pediatre")
            self.assertIn(IMG_PORTRAIT, body_pediatre,
                          f"pediatre.doctors.0.portrait must render universally on {locale} pediatre")
            body_crescita = preview_body(locale, page="crescita")
            # Deep-path override renders universally (plain-key global).
            self.assertIn(Q_OVERRIDE, body_crescita,
                          f"crescita deep-path override universal on {locale} (plain-key)")
            authored = _tc.get_content(p.source_template.slug, locale) or {}
            stable = (authored.get("home", {}).get("headline") or "")
            stable = stable.replace("<em>", "").replace("</em>", "")
            first_word = stable.split()[0] if stable else ""
            if first_word:
                self.assertIn(
                    first_word, body,
                    f"{locale} authored fallback not visible on Famiglia home",
                )

        # ── 10. AR preview (home) — `.fm-*` skin RTL invariant ────
        # 6 RTL rules (lowest of enrolled archetypes · validated Session
        # 51 · visual polish deferrable to future maintenance).
        import re as _re
        body_ar = preview_body("ar")
        html_tag_ar = _re.search(r"<html[^>]*>", body_ar)
        self.assertIsNotNone(html_tag_ar)
        self.assertIn('dir="rtl"', html_tag_ar.group(0))
        self.assertIn('lang="ar"', html_tag_ar.group(0))

        # ── 11. owner reopens the editor on each locale ──────────
        self.client.logout()
        self.client.login(username="owner", password="x")

        def find_field_by_key(groups, key):
            for g in groups:
                for f in g["fields"]:
                    if f["key"] == key:
                        return f
            return None

        for locale, expected_substring in (
            ("it", "Walk IT Famiglia"),
            ("en", "Walk EN Famiglia"),
            ("fr", "Walk FR Famiglia"),
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

        # Global text + scalar hero image: overridden universally, not
        # translatable.
        logo_field = find_field_by_key(r_es.context["groups"], "site.logo_word")
        self.assertIsNotNone(logo_field, "site.logo_word missing from Famiglia editor")
        self.assertEqual(logo_field["value"], "A16c Famiglia Walk Studio")
        self.assertTrue(logo_field["is_overridden"])
        self.assertFalse(logo_field["translatable"])

        hero_field = find_field_by_key(r_es.context["groups"], "home.hero_image")
        self.assertIsNotNone(hero_field, "home.hero_image missing from Famiglia editor")
        self.assertEqual(hero_field["value"], IMG_HERO)
        self.assertTrue(hero_field["is_overridden"])
        self.assertFalse(hero_field["translatable"])

        # ── 12. perimeter invariants re-checked end-of-test ──────
        # Medical-other family CLOSED · ALL 3 archetypes IN.
        for arc in ("clinic", "wellness", "family"):
            self.assertIn(arc, _SCHEMAS,
                          f"{arc} enrollment must persist through lifecycle · medical-other CLOSED")
            self.assertIn(arc, _ENABLED)
        # 14 pre-A.16 archetypes also still enrolled.
        for arc in (
            "agency-creative-studio", "corporate-suite", "fine-dining",
            "specialist", "classic-gold", "modern-transparent",
            "mass-market", "ultra-luxury-cinematic",
            "editorial-designer-grid", "cinematic-photographer",
            "trattoria-warm", "street-modern",
            "artisan-workshop", "fashion-editorial",
        ):
            self.assertIn(arc, _ENABLED, f"{arc} lost enrollment mid-lifecycle")
        # Sensitive OUT paths stay rejected — re-verified runtime at
        # end-of-test per user guidance.
        for out_path in (
            # Flat list-of-str
            "site.hours_footer_rows",
            "site.hours_footer_rows.0",
            "contatti.reason_options",
            "contatti.reason_options.0",
            # Nested list-of-str inside dict rows (Juris precedent)
            "home.age_groups.0.items",
            "home.age_groups.0.items.0",
            "home.age_groups.2.items.2",
            "pediatre.doctors.0.specs",
            "pediatre.doctors.0.specs.0",
            "pediatre.doctors.3.specs.2",
            # Form-related nested-dicts (Juris/Gusto/Bottega/Luxe/Salute/Benessere precedent)
            "contatti.form_placeholders",
            "contatti.form_placeholders.parent_name",
            "contatti.form_placeholders.email",
            "contatti.form_helpers",
            "contatti.form_helpers.email",
            # Top-level navigation + empty posts
            "pages",
            "pages.0.slug",
            "posts",
            "posts.0.title",
        ):
            with self.assertRaises(
                InvalidEditableField,
                msg=f"Famiglia complex-shape path must stay rejected: {out_path}",
            ):
                validate_key_path("family", out_path)

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
