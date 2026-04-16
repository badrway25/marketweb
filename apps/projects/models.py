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
        """Catalog live-preview URL extended with ?project=<uuid>.

        The project preview piggybacks on the existing catalog route so
        we do not have to modify any skin template. The renderer detects
        the `project` query param and overlays content + tokens.
        """
        return (
            f"/templates/{self.source_category_slug}/"
            f"{self.source_template.slug}/preview/"
            f"?project={self.uuid}"
        )

    def get_overrides_dict(self) -> dict[str, Any]:
        """Return a nested dict of all content overrides.

        key_path 'site.phone' -> {'site': {'phone': '...'}}
        """
        overrides = getattr(self, "_overrides_cache", None)
        if overrides is not None:
            return overrides
        tree: dict[str, Any] = {}
        for row in self.content_overrides.all():
            _set_nested(tree, row.key_path, row.value_decoded)
        self._overrides_cache = tree
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
