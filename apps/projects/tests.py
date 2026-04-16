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
        # A.2.6a: contatti rollout brings ~23 new fields → guard ≥85.
        self.assertGreaterEqual(len(data), 85)

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
