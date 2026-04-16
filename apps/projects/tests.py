"""Editor Foundation v1 unit tests."""
from __future__ import annotations

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from django.core.management import call_command
from apps.catalog.models import WebTemplate
from apps.editor.schema import (
    InvalidEditableField,
    get_field_spec,
    is_supported_archetype,
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

        r = self.client.post(f"/projects/{uuid}/editor/", {
            "content__site.logo_word": "HTTP Test Studio",
            "content__home.headline": "Test <em>overlay</em>",
            "token__palette_primary": "#123456",
            "token__palette_secondary": "#abcdef",
            "token__palette_accent": "#ff00aa",
            "token__heading_font": "Playfair Display",
            "token__body_font": "Inter",
        })
        self.assertEqual(r.status_code, 302)

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
