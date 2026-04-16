"""Write-path services for customer projects.

Every mutation goes through a service — views never touch the models
directly. This keeps the DNA-lock + field-whitelist + revision
bookkeeping centralised and keeps views thin.
"""
from __future__ import annotations

from typing import Any, Iterable

from django.db import transaction
from django.utils import timezone

from apps.catalog import template_content
from apps.catalog.models import WebTemplate
from apps.catalog.template_dna import get_dna
from apps.editor.schema import (
    DESIGN_TOKEN_FIELDS,
    InvalidEditableField,
    is_supported_archetype,
    validate_key_path,
    validate_value,
)
from apps.projects.models import (
    CustomerProject,
    ProjectContent,
    ProjectDesignTokens,
    ProjectRevision,
)


# ---------------------------------------------------------------------------
# Create
# ---------------------------------------------------------------------------

class UnsupportedTemplate(Exception):
    """The source template's archetype is not yet wired to the editor."""


@transaction.atomic
def create_project_from_template(
    *,
    owner,
    template: WebTemplate,
    name: str | None = None,
    locale: str = "it",
) -> CustomerProject:
    """Clone a published_live template into a fresh CustomerProject.

    - Seeds ProjectDesignTokens from the template's brand palette + DNA font_pairing.
    - Does NOT copy the content tree — the overlay is sparse-diff by design
      (EDITOR_SCHEMA_BLUEPRINT §7 read-path). An empty overrides table renders
      exactly the baseline preview.
    - Writes a SEED revision so the initial state is snapshot-able.
    """
    if template.tier != WebTemplate.Tier.PUBLISHED_LIVE:
        raise UnsupportedTemplate(
            f"Template '{template.slug}' is {template.tier} — only "
            f"published_live templates can seed a project in Foundation v1."
        )

    dna = get_dna(template.slug)
    if not dna:
        raise UnsupportedTemplate(
            f"Template '{template.slug}' has no DNA entry."
        )
    archetype = dna["archetype"]
    if not is_supported_archetype(archetype):
        raise UnsupportedTemplate(
            f"Archetype '{archetype}' is not yet supported by the editor "
            f"(Phase A.1 scope: agency-creative-studio only)."
        )

    content = template_content.get_content(template.slug, locale)
    if not content:
        raise UnsupportedTemplate(
            f"Template '{template.slug}' has no content registry."
        )

    default_name = name or f"{template.name} · bozza personale"

    project = CustomerProject.objects.create(
        owner=owner,
        source_template=template,
        source_archetype=archetype,
        source_category_slug=template.category.slug,
        name=default_name,
        locale=locale,
    )

    # Seed tokens from brand palette + DNA font_pairing.
    palette = (template.brand.palette or {}) if hasattr(template, "brand") else {}
    heading_font, body_font = dna["font_pairing"]
    ProjectDesignTokens.objects.create(
        project=project,
        palette_primary=palette.get("primary",   "#0f172a"),
        palette_secondary=palette.get("secondary", "#f1f5f9"),
        palette_accent=palette.get("accent",    "#f59e0b"),
        heading_font=heading_font,
        body_font=body_font,
    )

    ProjectRevision.objects.create(
        project=project,
        reason=ProjectRevision.Reason.SEED,
        label="Seed iniziale",
        snapshot=_build_snapshot(project),
        created_by=owner,
    )

    return project


# ---------------------------------------------------------------------------
# Edit
# ---------------------------------------------------------------------------

@transaction.atomic
def save_content_edits(
    *,
    project: CustomerProject,
    edits: dict[str, Any],
    editor,
) -> list[str]:
    """Persist a batch of content overrides.

    Silently ignores empty overrides (value equal to baseline). Raises
    ``InvalidEditableField`` if any edit targets a DNA-locked key. The
    full batch commits atomically — either all writes stick or the
    transaction rolls back.

    Returns the list of key_paths that were actually written (changed
    from the previous value).
    """
    archetype = project.source_archetype
    baseline = template_content.get_content(project.source_template.slug, project.locale) or {}

    touched: list[str] = []
    for key_path, raw_value in edits.items():
        validate_key_path(archetype, key_path)
        cleaned = validate_value(archetype, key_path, raw_value)

        baseline_value = _resolve_path(baseline, key_path)

        # A value equal to baseline is persisted as "delete override" —
        # keeps the overrides table sparse and lets upstream DNA
        # polish flow through to the customer automatically.
        if _normalise(cleaned) == _normalise(baseline_value):
            ProjectContent.objects.filter(project=project, key_path=key_path).delete()
            touched.append(key_path)
            continue

        existing = ProjectContent.objects.filter(project=project, key_path=key_path).first()
        if existing is None:
            row = ProjectContent(project=project, key_path=key_path)
            row.set_value(cleaned)
            row.save()
            touched.append(key_path)
        elif _normalise(existing.value_decoded) != _normalise(cleaned):
            existing.set_value(cleaned)
            existing.save(update_fields=["value_json", "updated_at"])
            touched.append(key_path)

    if touched:
        project.save(update_fields=["updated_at"])
    return touched


@transaction.atomic
def save_design_token_edits(
    *,
    project: CustomerProject,
    token_edits: dict[str, Any],
) -> list[str]:
    """Persist changes to palette/font fields on ProjectDesignTokens."""
    tokens = project.tokens
    touched: list[str] = []
    for field, raw_value in token_edits.items():
        spec = DESIGN_TOKEN_FIELDS.get(field)
        if spec is None:
            raise InvalidEditableField(f"Unknown design token '{field}'.")
        cleaned = _validate_token(spec, raw_value)
        if getattr(tokens, field) != cleaned:
            setattr(tokens, field, cleaned)
            touched.append(field)
    if touched:
        tokens.save()
        project.save(update_fields=["updated_at"])
    return touched


# ---------------------------------------------------------------------------
# Publish / revise
# ---------------------------------------------------------------------------

@transaction.atomic
def publish_project(*, project: CustomerProject, editor) -> CustomerProject:
    ProjectRevision.objects.create(
        project=project,
        reason=ProjectRevision.Reason.PUBLISH,
        label="Pubblicazione",
        snapshot=_build_snapshot(project),
        created_by=editor,
    )
    project.status = CustomerProject.Status.PUBLISHED
    project.last_published_at = timezone.now()
    project.save(update_fields=["status", "last_published_at", "updated_at"])
    return project


@transaction.atomic
def unpublish_project(*, project: CustomerProject, editor) -> CustomerProject:
    ProjectRevision.objects.create(
        project=project,
        reason=ProjectRevision.Reason.UNPUBLISH,
        label="Riportato in bozza",
        snapshot=_build_snapshot(project),
        created_by=editor,
    )
    project.status = CustomerProject.Status.DRAFT
    project.save(update_fields=["status", "updated_at"])
    return project


@transaction.atomic
def take_manual_revision(*, project: CustomerProject, editor, label: str = "") -> ProjectRevision:
    return ProjectRevision.objects.create(
        project=project,
        reason=ProjectRevision.Reason.MANUAL,
        label=label or "Salvataggio manuale",
        snapshot=_build_snapshot(project),
        created_by=editor,
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _build_snapshot(project: CustomerProject) -> dict[str, Any]:
    """Serialise the project's full override state.

    Always queries content + tokens fresh — the caller's view may hold a
    prefetched `content_overrides` cache from the GET phase of the same
    request, and using that cache here would snapshot the pre-save state.
    """
    tokens = ProjectDesignTokens.objects.get(project=project)
    rows = ProjectContent.objects.filter(project=project)
    content = {row.key_path: row.value_decoded for row in rows}
    return {
        "name": project.name,
        "locale": project.locale,
        "status": project.status,
        "tokens": {
            "palette_primary": tokens.palette_primary,
            "palette_secondary": tokens.palette_secondary,
            "palette_accent": tokens.palette_accent,
            "heading_font": tokens.heading_font,
            "body_font": tokens.body_font,
        },
        "content": content,
    }


def _resolve_path(tree: dict[str, Any], key_path: str) -> Any:
    cursor: Any = tree
    for segment in key_path.split("."):
        if not isinstance(cursor, dict):
            return None
        cursor = cursor.get(segment)
        if cursor is None:
            return None
    return cursor


def _normalise(value: Any) -> Any:
    """Strip strings so trailing whitespace doesn't mask equality."""
    if isinstance(value, str):
        return value.strip()
    return value


def _validate_token(spec: dict[str, Any], value: Any) -> str:
    if spec["type"] == "color":
        if not isinstance(value, str) or not value.startswith("#") or len(value) not in (4, 7, 9):
            raise InvalidEditableField(f"{value!r} is not a valid hex colour.")
        return value
    if spec["type"] == "select":
        choices = spec.get("choices") or []
        if value not in choices:
            raise InvalidEditableField(f"{value!r} is not in the curated list.")
        return value
    return value


def resolve_path_in_baseline(project: CustomerProject, key_path: str) -> Any:
    """Convenience used by the editor UI to show the original value."""
    baseline = template_content.get_content(project.source_template.slug, project.locale) or {}
    return _resolve_path(baseline, key_path)


def current_value_for(project: CustomerProject, key_path: str) -> Any:
    """Value the editor should prefill: override if present, else baseline."""
    override = next(
        (row for row in project.content_overrides.all() if row.key_path == key_path),
        None,
    )
    if override is not None:
        return override.value_decoded
    return resolve_path_in_baseline(project, key_path)


def iter_editable_templates() -> Iterable[WebTemplate]:
    """All published_live templates whose archetype is supported."""
    from apps.catalog.template_dna import get_dna as _get_dna

    qs = WebTemplate.objects.filter(
        tier=WebTemplate.Tier.PUBLISHED_LIVE,
    ).select_related("category", "brand").order_by("category__name", "name")
    for t in qs:
        dna = _get_dna(t.slug)
        if dna and is_supported_archetype(dna["archetype"]):
            yield t
