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
    META_KEY,
    InvalidEditableField,
    get_list_shape,
    is_mutable_list,
    is_supported_archetype,
    validate_key_path,
    validate_value,
)
from apps.projects.models import (
    CustomerProject,
    ProjectAsset,
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
def get_or_create_project_for_template(
    *,
    owner,
    template: WebTemplate,
    locale: str = "it",
) -> tuple[CustomerProject, bool]:
    """Return the user's existing project for this template, or create one.

    Phase A.1b customer-facing rule (D-087): a customer gets ONE
    active project per (owner, source_template). The entry point from
    the catalog treats "Personalizza" as "open my workspace for this
    template" rather than "fork a new draft every time I click".

    Motivation: matches Wix/Squarespace mental model and removes the
    "which draft is mine?" confusion we'd otherwise ship on first
    launch. Multi-draft is a later opt-in — when we have a richer
    dashboard to disambiguate them.

    Returns (project, created_bool).
    """
    existing = (
        CustomerProject.objects
        .filter(owner=owner, source_template=template)
        .order_by("-updated_at")
        .first()
    )
    if existing is not None:
        return existing, False
    project = create_project_from_template(
        owner=owner, template=template, locale=locale,
    )
    return project, True


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

        baseline_value = _resolve_path(baseline, key_path, archetype)

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


def _resolve_path(
    tree: dict[str, Any],
    key_path: str,
    archetype: str | None = None,
) -> Any:
    """Walk a dotted path, including numeric/tuple-column segments.

    A.2.6b: indexed paths like ``studio.facts.0.label`` need three
    kinds of step:
    - dict key (``studio``, ``facts``)
    - list index (``0``)
    - tuple-column name (``label`` → tuple position 1) — only when the
      preceding list is a tuple-shaped list per
      ``STRUCTURED_FIELD_SHAPES``. ``archetype`` lets us perform the
      column-name → tuple-index lookup; if omitted we fall back to
      dict/list walking only (good enough for scalar/dict lists).

    The splicer in ``apps.editor.rendering`` does the same dance at
    apply time; this helper is the read-side counterpart used by the
    editor sidebar (prefill values) and by ``save_content_edits``
    (delete-on-baseline-equality sparse-diff).
    """
    shapes: dict[str, Any] = {}
    if archetype:
        try:
            from apps.editor.schema import get_structured_shapes
            shapes = get_structured_shapes(archetype)
        except Exception:
            shapes = {}

    parts = key_path.split(".")
    cursor: Any = tree
    walked: list[str] = []
    for segment in parts:
        if isinstance(cursor, dict):
            cursor = cursor.get(segment)
        elif isinstance(cursor, list):
            try:
                idx = int(segment)
            except ValueError:
                return None
            if idx < 0 or idx >= len(cursor):
                return None
            cursor = cursor[idx]
        elif isinstance(cursor, tuple):
            # Tuple cell — translate the column name via the shape that
            # described the parent list (the path two segments back).
            list_path = ".".join(walked[:-1])
            shape = shapes.get(list_path)
            if not shape or shape.get("kind") != "tuple":
                return None
            order = shape.get("tuple_order") or []
            if segment not in order:
                return None
            col_idx = order.index(segment)
            if col_idx >= len(cursor):
                return None
            cursor = cursor[col_idx]
        else:
            return None
        walked.append(segment)
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
    return _resolve_path(baseline, key_path, project.source_archetype)


def current_value_for(project: CustomerProject, key_path: str) -> Any:
    """Value the editor should prefill: override if present, else baseline."""
    override = next(
        (row for row in project.content_overrides.all() if row.key_path == key_path),
        None,
    )
    if override is not None:
        return override.value_decoded
    return resolve_path_in_baseline(project, key_path)


# ---------------------------------------------------------------------------
# A.3a · True repeater interactions (add/remove row on mutable lists)
# ---------------------------------------------------------------------------

class UnsupportedMutation(Exception):
    """The list_path is not opted-in to add/remove (``mutable=False``)."""


class RowLimitReached(Exception):
    """Row add/remove would violate the list's min/max row bounds."""

    def __init__(self, kind: str, limit: int):
        super().__init__(f"Row limit reached: {kind} = {limit}")
        self.kind = kind  # "min" or "max"
        self.limit = limit


def _empty_meta() -> dict[str, Any]:
    return {"removed": [], "added": []}


def get_list_meta(project: CustomerProject, list_path: str) -> dict[str, Any]:
    """Return the project's structural meta for a mutable list (or empty).

    The structural record lives at ``<list_path>.__meta__``; when absent
    the list is in its baseline shape. Never raises — callers consuming
    this for rendering or UI decisions want a permissive default.

    A.3b: when present, the ``order`` field (array of segment strings)
    is passed through verbatim so rendering + services can honor it.
    """
    row = ProjectContent.objects.filter(
        project=project, key_path=f"{list_path}.{META_KEY}",
    ).first()
    if row is None:
        return _empty_meta()
    value = row.value_decoded
    if not isinstance(value, dict):
        return _empty_meta()
    removed = [i for i in (value.get("removed") or []) if isinstance(i, int)]
    added = [
        {"uid": e["uid"]} for e in (value.get("added") or [])
        if isinstance(e, dict) and isinstance(e.get("uid"), str)
    ]
    out: dict[str, Any] = {"removed": removed, "added": added}
    raw_order = value.get("order")
    if isinstance(raw_order, list):
        order = [s for s in raw_order if isinstance(s, str)]
        if order:
            out["order"] = order
    return out


def _baseline_list_length(project: CustomerProject, list_path: str) -> int:
    """Row count of the baseline list in the catalog registry."""
    baseline = template_content.get_content(project.source_template.slug, project.locale) or {}
    cursor: Any = baseline
    for seg in list_path.split("."):
        if not isinstance(cursor, dict):
            return 0
        cursor = cursor.get(seg)
    return len(cursor) if isinstance(cursor, list) else 0


def _effective_length(baseline_len: int, meta: dict[str, Any]) -> int:
    """Effective row count after applying removed + added from meta."""
    removed = set(meta.get("removed") or [])
    kept = sum(1 for i in range(baseline_len) if i not in removed)
    return kept + len(meta.get("added") or [])


def _next_uid(meta: dict[str, Any]) -> str:
    """Monotonic uid sequence: a0, a1, a2, … Never recycled — an uid
    that was removed + re-added stays distinct so stale cell overrides
    can never collide with a new row.
    """
    existing = meta.get("added") or []
    n = 0
    for entry in existing:
        uid = entry.get("uid") if isinstance(entry, dict) else None
        if isinstance(uid, str) and uid.startswith("a"):
            try:
                n = max(n, int(uid[1:]) + 1)
            except ValueError:
                continue
    return f"a{n}"


def _persist_meta(project: CustomerProject, list_path: str, meta: dict[str, Any]) -> None:
    """Write the meta sentinel — or delete the record when meta is
    fully empty so sparse-diff stays clean. A.3b: a custom ``order``
    counts as meaningful state and keeps the record alive even if
    ``removed`` and ``added`` are empty (a reorder without add/remove
    is still a non-default mutation).
    """
    key = f"{list_path}.{META_KEY}"
    has_state = (
        bool(meta.get("removed"))
        or bool(meta.get("added"))
        or bool(meta.get("order"))
    )
    if not has_state:
        ProjectContent.objects.filter(project=project, key_path=key).delete()
        return
    row, _ = ProjectContent.objects.get_or_create(project=project, key_path=key)
    row.set_value(meta)
    row.save()


def _cascade_delete_cell_overrides(
    project: CustomerProject, list_path: str, segment: str,
) -> None:
    """Delete every cell override keyed under ``<list_path>.<segment>.``.

    Used when a row disappears (baseline remove or added-row revert) so
    orphan cells never linger. ``segment`` may be a baseline integer
    index (``"2"``) or an added-row uid (``"a3"``).
    """
    prefix = f"{list_path}.{segment}."
    ProjectContent.objects.filter(
        project=project, key_path__startswith=prefix,
    ).delete()


@transaction.atomic
def add_row(
    *, project: CustomerProject, list_path: str, editor,
) -> dict[str, Any]:
    """Append a new row to a mutable list.

    Raises ``UnsupportedMutation`` if the list is not mutable, and
    ``RowLimitReached("max", ...)`` if the effective length is already
    at the max_rows bound. Returns a summary dict with the new uid +
    the updated meta + the new effective length.
    """
    archetype = project.source_archetype
    if not is_mutable_list(archetype, list_path):
        raise UnsupportedMutation(
            f"List '{list_path}' is not mutable for archetype '{archetype}'."
        )
    shape = get_list_shape(archetype, list_path)
    max_rows = shape.get("max_rows", 10)

    meta = get_list_meta(project, list_path)
    baseline_len = _baseline_list_length(project, list_path)
    current_len = _effective_length(baseline_len, meta)
    if current_len >= max_rows:
        raise RowLimitReached("max", max_rows)

    uid = _next_uid(meta)
    existing_added = list(meta.get("added") or [])
    existing_added.append({"uid": uid})
    meta["added"] = existing_added
    # A.3b — if a custom order is already persisted, append the new uid
    # at the end so the customer's previous arrangement survives. The
    # new row still lands at the bottom visually; the customer can move
    # it afterwards.
    if "order" in meta and isinstance(meta["order"], list):
        meta["order"] = list(meta["order"]) + [uid]
    _persist_meta(project, list_path, meta)
    project.save(update_fields=["updated_at"])
    return {"uid": uid, "meta": meta, "effective_length": current_len + 1}


def _current_order(
    baseline_len: int, meta: dict[str, Any],
) -> list[str]:
    """Return the list of segments that describe the effective row
    sequence, honoring ``meta.order`` when valid, otherwise deriving
    the canonical default (baseline survivors ascending + added in
    declaration order). Mirror of ``rendering.compute_default_order``.
    """
    from apps.editor.rendering import compute_default_order
    removed = meta.get("removed") or []
    added = [
        e for e in (meta.get("added") or [])
        if isinstance(e, dict) and isinstance(e.get("uid"), str)
    ]
    default = compute_default_order(baseline_len, removed, added)
    raw = meta.get("order")
    if isinstance(raw, list):
        cleaned = [s for s in raw if isinstance(s, str)]
        if set(cleaned) == set(default) and len(cleaned) == len(default):
            return cleaned
    return default


@transaction.atomic
def move_row(
    *, project: CustomerProject, list_path: str,
    segment: str, direction: str, editor,
) -> dict[str, Any]:
    """A.3b — swap a row one position up or down in the effective list.

    ``segment`` is the row identity as used by the sidebar:
    ``"<int>"`` for a baseline row, or an ``"aN"`` uid for an added
    row. ``direction`` is ``"up"`` or ``"down"``.

    Raises:
    - ``UnsupportedMutation`` if the list is not ``mutable``.
    - ``InvalidEditableField`` on malformed segment / direction or
      if the segment is not present in the current effective order.
    - ``RowLimitReached("boundary", pos)`` when the move would cross
      the first/last row of the effective list.

    The new ``order`` is compared to the canonical default: when they
    match, ``order`` is stripped from ``__meta__`` so sparse-diff stays
    clean (the list is back to its baseline-plus-added sequence).
    """
    archetype = project.source_archetype
    if not is_mutable_list(archetype, list_path):
        raise UnsupportedMutation(
            f"List '{list_path}' is not mutable for archetype '{archetype}'."
        )
    if direction not in ("up", "down"):
        raise InvalidEditableField(
            f"direction must be 'up' or 'down', got {direction!r}."
        )
    if not isinstance(segment, str) or not segment:
        raise InvalidEditableField(f"segment must be a non-empty string.")

    meta = get_list_meta(project, list_path)
    baseline_len = _baseline_list_length(project, list_path)
    order = list(_current_order(baseline_len, meta))

    try:
        pos = order.index(segment)
    except ValueError:
        raise InvalidEditableField(
            f"Segment {segment!r} is not present in '{list_path}'."
        )

    if direction == "up":
        if pos == 0:
            raise RowLimitReached("boundary", pos)
        swap_with = pos - 1
    else:
        if pos >= len(order) - 1:
            raise RowLimitReached("boundary", pos)
        swap_with = pos + 1

    order[pos], order[swap_with] = order[swap_with], order[pos]

    # Sparse-diff normalize: if the new order matches the canonical
    # default, drop the field. Otherwise persist it inside meta.
    from apps.editor.rendering import compute_default_order
    default = compute_default_order(
        baseline_len,
        meta.get("removed") or [],
        [e for e in (meta.get("added") or []) if isinstance(e, dict)],
    )
    new_meta = dict(meta)
    if order == default:
        new_meta.pop("order", None)
    else:
        new_meta["order"] = order

    _persist_meta(project, list_path, new_meta)
    project.save(update_fields=["updated_at"])
    return {"order": order, "effective_length": len(order)}


@transaction.atomic
def remove_row(
    *, project: CustomerProject, list_path: str,
    index: int | None = None, uid: str | None = None,
    editor,
) -> dict[str, Any]:
    """Remove a row from a mutable list.

    Exactly one of ``index`` (baseline int index) or ``uid`` (added row)
    must be supplied. Cell overrides under the removed row are
    cascade-deleted so no orphan records remain.

    Raises ``UnsupportedMutation`` for non-mutable lists, and
    ``RowLimitReached("min", ...)`` when the effective length is already
    at the min_rows bound.
    """
    if (index is None) == (uid is None):
        raise ValueError("remove_row requires exactly one of index/uid.")

    archetype = project.source_archetype
    if not is_mutable_list(archetype, list_path):
        raise UnsupportedMutation(
            f"List '{list_path}' is not mutable for archetype '{archetype}'."
        )
    shape = get_list_shape(archetype, list_path)
    min_rows = shape.get("min_rows", 1)

    meta = get_list_meta(project, list_path)
    baseline_len = _baseline_list_length(project, list_path)
    current_len = _effective_length(baseline_len, meta)
    if current_len <= min_rows:
        raise RowLimitReached("min", min_rows)

    if index is not None:
        if not isinstance(index, int) or index < 0 or index >= baseline_len:
            raise InvalidEditableField(
                f"Baseline index {index} out of range for '{list_path}'."
            )
        if index in (meta.get("removed") or []):
            raise InvalidEditableField(
                f"Baseline row {index} is already removed from '{list_path}'."
            )
        existing_removed = list(meta.get("removed") or [])
        existing_removed.append(index)
        meta["removed"] = existing_removed
        dropped_segment = str(index)
        _cascade_delete_cell_overrides(project, list_path, dropped_segment)
    else:
        added = list(meta.get("added") or [])
        new_added = [e for e in added if e.get("uid") != uid]
        if len(new_added) == len(added):
            raise InvalidEditableField(
                f"Added-row uid {uid!r} is not present on '{list_path}'."
            )
        meta["added"] = new_added
        dropped_segment = uid
        _cascade_delete_cell_overrides(project, list_path, uid)

    # A.3b — keep order[] in sync by pruning the dropped segment. If
    # pruning leaves the array equal to the canonical default, strip
    # order so sparse-diff stays clean.
    if "order" in meta and isinstance(meta["order"], list):
        pruned = [s for s in meta["order"] if s != dropped_segment]
        from apps.editor.rendering import compute_default_order
        default = compute_default_order(
            baseline_len, meta.get("removed") or [], meta.get("added") or [],
        )
        if pruned == default:
            meta.pop("order")
        else:
            meta["order"] = pruned

    _persist_meta(project, list_path, meta)
    project.save(update_fields=["updated_at"])
    return {"meta": meta, "effective_length": current_len - 1}


# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# A.4 · customer image upload
# ---------------------------------------------------------------------------

ALLOWED_ASSET_MIME = {"image/jpeg", "image/png", "image/webp"}
MAX_ASSET_SIZE_BYTES = 2 * 1024 * 1024  # 2 MB


class AssetTooLarge(Exception):
    """Uploaded file exceeds the server-side size cap."""

    def __init__(self, size_bytes: int, limit_bytes: int):
        super().__init__(f"Asset size {size_bytes} exceeds limit {limit_bytes}.")
        self.size_bytes = size_bytes
        self.limit_bytes = limit_bytes


class AssetMimeRejected(Exception):
    """Uploaded content-type is not on the whitelist."""

    def __init__(self, content_type: str):
        super().__init__(f"Content-type {content_type!r} is not allowed.")
        self.content_type = content_type


class AssetInvalid(Exception):
    """Uploaded file is malformed (Pillow verify failed)."""


@transaction.atomic
def upload_asset(
    *, project: CustomerProject, uploaded_file, editor,
) -> ProjectAsset:
    """Persist an image uploaded by the customer.

    - ``uploaded_file`` is a Django ``UploadedFile`` coming from
      ``request.FILES["file"]``.
    - Size is capped at 2 MB server-side so a large payload can never
      slip through the request.FILES limit.
    - Content-type is whitelisted to jpg/png/webp.
    - After saving, ``Pillow.Image.verify()`` is called to ensure the
      bytes actually form a valid image (catches MIME spoofing).
    - Orphan assets (uploaded but not referenced by any content
      override) are acceptable in A.4 — cleanup is Phase A.5 scope.
    """
    size = getattr(uploaded_file, "size", None)
    if size is None or size > MAX_ASSET_SIZE_BYTES:
        raise AssetTooLarge(size or 0, MAX_ASSET_SIZE_BYTES)
    content_type = (getattr(uploaded_file, "content_type", "") or "").lower()
    if content_type not in ALLOWED_ASSET_MIME:
        raise AssetMimeRejected(content_type)

    asset = ProjectAsset(
        project=project,
        file=uploaded_file,
        content_type=content_type,
        size_bytes=size,
        uploaded_by=editor,
    )
    asset.save()

    # Defense against MIME spoofing: the declared content_type passed
    # the whitelist, but the bytes might not actually be an image.
    # Pillow.verify() reads the header without loading pixels.
    try:
        from PIL import Image
        with Image.open(asset.file.path) as img:
            img.verify()
    except Exception as exc:  # Pillow raises various exception types
        # Django FileField.delete() detaches + removes the file when
        # save=False; chained with the row delete so neither the DB
        # row nor the on-disk file survives a rejected spoof attempt.
        asset.file.delete(save=False)
        asset.delete()
        raise AssetInvalid(f"File is not a valid image: {exc}")

    return asset


# ---------------------------------------------------------------------------


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
