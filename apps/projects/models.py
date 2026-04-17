"""Customer project models — Phase A.1 editor foundation.

A `CustomerProject` is a user's personalisation of a published_live
WebTemplate. The project owns a sparse set of content overrides
(ProjectContent, key-path flat storage) and a single design-tokens
row (ProjectDesignTokens) that overlay the static content registry +
DNA at render time. Revisions snapshot the full override state on
publish or explicit save-as-revision.

Scope for Foundation v1 (D-085 / Phase A.1):
- Single locale (IT) per project. Multi-locale is Phase A.7.
- Only whitelisted key_paths per archetype can be written
  (enforced at the service layer, see apps.editor.schema).
- Tier is draft | published (local to the customer, not catalog tier).
"""
from __future__ import annotations

import json
import uuid
from typing import Any

from django.conf import settings
from django.db import models

from apps.core.models import TimestampedModel


class CustomerProject(TimestampedModel):
    """A customer's personalisation of a published_live template."""

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_projects",
    )
    # PROTECT — deleting a template while a project exists would strand
    # the overrides against an archetype that no longer has a content
    # registry seed. Protect surfaces the dependency explicitly.
    source_template = models.ForeignKey(
        "catalog.WebTemplate",
        on_delete=models.PROTECT,
        related_name="customer_projects",
    )
    # Snapshot the archetype slug at fork time so that a catalog-side
    # DNA rewrite cannot silently invalidate an in-flight project. The
    # renderer always trusts the project's snapshot over the live DNA.
    source_archetype = models.CharField(max_length=80)
    source_category_slug = models.CharField(max_length=80)
    name = models.CharField(max_length=120)
    locale = models.CharField(
        max_length=5,
        default="it",
        help_text="Foundation v1: only 'it' supported. Multi-locale is Phase A.7.",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        db_index=True,
    )
    last_published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-updated_at"]
        indexes = [
            models.Index(fields=["owner", "status"]),
        ]

    def __str__(self) -> str:
        return f"{self.name} ({self.owner.username})"

    @property
    def preview_url_base(self) -> str:
        """Catalog live-preview URL for the HOME page (with ?project=).

        The project preview piggybacks on the existing catalog route so
        we do not have to modify any skin template. The renderer detects
        the `project` query param and overlays content + tokens.
        """
        return self.preview_url_for_page("home")

    @property
    def preview_url_path(self) -> str:
        """Raw preview path WITHOUT page segment or query string.

        Shape: ``/templates/<cat>/<slug>/preview/``. The editor JS
        appends the page slug and query params client-side, so we
        don't have to pass every page variant in the context.
        """
        return (
            f"/templates/{self.source_category_slug}/"
            f"{self.source_template.slug}/preview/"
        )

    def preview_url_for_page(
        self, page_slug: str | None, locale: str | None = None,
    ) -> str:
        """Preview URL for a specific page of this project's template.

        Home is the implicit default (no trailing segment) to match the
        catalog URL pattern ``<cat>/<slug>/preview/``. Other pages get
        ``<cat>/<slug>/preview/<page>/``. The ``?project=<uuid>`` query
        is always appended so the renderer applies the customer overlay.

        A.7 Step 2: when ``locale`` is provided, ``&lang=<code>`` is
        appended so the catalog router picks the per-locale authored
        content and the overlay filter (``apply_project_overrides``)
        applies only the matching-locale rows.
        """
        base = self.preview_url_path
        if page_slug and page_slug != "home":
            base += f"{page_slug}/"
        url = f"{base}?project={self.uuid}"
        if locale:
            url += f"&lang={locale}"
        return url

    def get_overrides_dict(self, locale: str | None = None) -> dict[str, Any]:
        """Return a nested dict of all content overrides for a locale.

        key_path 'site.phone' -> {'site': {'phone': '...'}}

        A.7 Step 1: rows keyed ``@<code>:<path>`` (per-locale overrides)
        are applied only when ``code`` matches the target locale; other
        locales are filtered out. Plain rows (no prefix) always apply.
        When both a plain row and a target-locale row exist for the same
        bare path, the target-locale row supersedes. Caching is keyed on
        the locale so repeat calls for the same target are cheap.

        Callers that don't care about locale (pre-A.7 code paths) can
        omit the parameter; the project's seed locale is used.
        """
        from apps.editor.schema import decode_locale_key
        target_locale = locale or self.locale or "it"
        cache = getattr(self, "_overrides_cache", None)
        if isinstance(cache, dict) and cache.get("_locale") == target_locale:
            return cache["tree"]

        plain_rows: dict[str, Any] = {}
        locale_rows: dict[str, Any] = {}
        for row in self.content_overrides.all():
            row_locale, bare_path = decode_locale_key(row.key_path)
            if row_locale is None:
                plain_rows[bare_path] = row.value_decoded
            elif row_locale == target_locale:
                locale_rows[bare_path] = row.value_decoded

        tree: dict[str, Any] = {}
        for bare_path, value in {**plain_rows, **locale_rows}.items():
            _set_nested(tree, bare_path, value)
        self._overrides_cache = {"_locale": target_locale, "tree": tree}
        return tree


class ProjectContent(TimestampedModel):
    """One content override field for a project.

    Stored flat as (project, key_path, value) — per EDITOR_SCHEMA_BLUEPRINT
    §7. key_path is a dotted path into the content tree (e.g. 'site.phone',
    'home.headline', 'home.primary_cta'). `value` is JSON-encoded to
    preserve types (string, list, dict, number).
    """

    project = models.ForeignKey(
        CustomerProject,
        on_delete=models.CASCADE,
        related_name="content_overrides",
    )
    key_path = models.CharField(
        max_length=200,
        help_text="Dotted path into the content tree, e.g. 'home.headline'.",
    )
    value_json = models.TextField(
        help_text="JSON-encoded override value (text, list, dict, number).",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["project", "key_path"],
                name="uniq_project_content_keypath",
            ),
        ]
        ordering = ["key_path"]

    def __str__(self) -> str:
        return f"{self.project.name} · {self.key_path}"

    @property
    def value_decoded(self) -> Any:
        try:
            return json.loads(self.value_json)
        except (ValueError, TypeError):
            return self.value_json

    def set_value(self, value: Any) -> None:
        self.value_json = json.dumps(value, ensure_ascii=False)


class ProjectDesignTokens(TimestampedModel):
    """CSS design-token overlay for a project (palette + fonts).

    A deliberately small MVP set for Foundation v1 — palette (3 colours)
    + heading/body font family. Future phases add: radius, icon_pack,
    image_treatment, motion_profile, density. See
    EDITOR_SCHEMA_BLUEPRINT §2.
    """

    # Curated Google Font families — the same list that
    # EDITOR_SCHEMA_BLUEPRINT §2 locks as the whitelist.
    CURATED_FONTS = [
        "Inter",
        "Plus Jakarta Sans",
        "Cormorant Garamond",
        "Bodoni Moda",
        "Playfair Display",
        "Lato",
        "Big Shoulders Display",
        "Archivo",
        "Syne",
        "Manrope",
        "Merriweather",
        "Libre Baskerville",
        "Nunito Sans",
        "Quicksand",
        "Space Grotesk",
        "DM Sans",
        "Poppins",
        "Montserrat",
        "Work Sans",
        "Fraunces",
    ]

    project = models.OneToOneField(
        CustomerProject,
        on_delete=models.CASCADE,
        related_name="tokens",
    )
    palette_primary = models.CharField(max_length=9, default="#0f172a")
    palette_secondary = models.CharField(max_length=9, default="#f1f5f9")
    palette_accent = models.CharField(max_length=9, default="#f59e0b")
    heading_font = models.CharField(max_length=60, default="Space Grotesk")
    body_font = models.CharField(max_length=60, default="Inter")

    class Meta:
        verbose_name = "Project design tokens"
        verbose_name_plural = "Project design tokens"

    def __str__(self) -> str:
        return f"Tokens · {self.project.name}"

    def as_theme_overlay(self) -> dict[str, str]:
        """Return a dict matching LiveTemplateView's `theme` context shape."""
        return {
            "primary": self.palette_primary,
            "secondary": self.palette_secondary,
            "accent": self.palette_accent,
            "heading_font": self.heading_font,
            "body_font": self.body_font,
        }


class ProjectRevision(TimestampedModel):
    """Snapshot of a project's override state at a point in time.

    Foundation v1: snapshot-on-publish + snapshot-on-explicit-save.
    Full undo/diff tooling is Phase A.2+. The shape is already rich
    enough to ground a future revision browser.
    """

    class Reason(models.TextChoices):
        MANUAL = "manual", "Manual save"
        PUBLISH = "publish", "Before publish"
        UNPUBLISH = "unpublish", "Before unpublish"
        SEED = "seed", "Initial seed"

    project = models.ForeignKey(
        CustomerProject,
        on_delete=models.CASCADE,
        related_name="revisions",
    )
    reason = models.CharField(
        max_length=20,
        choices=Reason.choices,
        default=Reason.MANUAL,
    )
    label = models.CharField(max_length=120, blank=True)
    # Full snapshot — content overrides + tokens — as JSON. A single
    # row restores the project exactly. We keep it denormalised because
    # a revision is read as an atomic unit, never queried per-field.
    snapshot = models.JSONField(default=dict, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="project_revisions",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Rev {self.pk} · {self.project.name} · {self.reason}"


def _asset_upload_path(instance: "ProjectAsset", filename: str) -> str:
    """Upload path for ``ProjectAsset.file``.

    Filename is generated server-side from a uuid + the extension
    inferred from the content_type so that the customer never
    controls the on-disk path (defense against path traversal /
    clobbering). Layout:

        media/project-assets/<project-uuid>/<asset-uuid>.<ext>
    """
    mime = (instance.content_type or "").lower()
    ext_by_mime = {
        "image/jpeg": "jpg",
        "image/png":  "png",
        "image/webp": "webp",
    }
    ext = ext_by_mime.get(mime, "bin")
    return f"project-assets/{instance.project.uuid}/{uuid.uuid4().hex}.{ext}"


class ProjectAsset(TimestampedModel):
    """A file (currently: image) uploaded by the customer for a project.

    A.4 scope: shell minimale. The asset is persisted on MEDIA_ROOT
    under ``project-assets/<project-uuid>/<uuid>.<ext>`` and its public
    URL is returned to the editor, which writes it into the image
    field's ProjectContent override via the normal autosave pipeline.

    There is NO link field between ProjectAsset and ProjectContent —
    the URL travels through content as plain string. Orphan assets
    (uploaded then unused because the customer reset the field or
    uploaded a replacement) are acceptable in A.4; a GC job is
    Phase A.5 scope.
    """

    project = models.ForeignKey(
        CustomerProject,
        on_delete=models.CASCADE,
        related_name="assets",
    )
    file = models.FileField(upload_to=_asset_upload_path)
    content_type = models.CharField(max_length=64)
    size_bytes = models.PositiveIntegerField()
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Asset #{self.pk} · {self.project.name} · {self.content_type}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _set_nested(tree: dict[str, Any], key_path: str, value: Any) -> None:
    """Write `value` into `tree` at the dotted `key_path`."""
    parts = key_path.split(".")
    cursor = tree
    for segment in parts[:-1]:
        nxt = cursor.get(segment)
        if not isinstance(nxt, dict):
            nxt = {}
            cursor[segment] = nxt
        cursor = nxt
    cursor[parts[-1]] = value
