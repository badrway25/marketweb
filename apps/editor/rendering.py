"""Project preview rendering — overlay customer overrides on catalog content.

The catalog `LiveTemplateView` composes a context dict from the static
template_content + DNA. When a request carries ``?project=<uuid>``,
this module overlays the project's ProjectContent rows + the
ProjectDesignTokens row on top of that context, producing a context
that still matches the shape the skins expect — so no skin changes
are required for Foundation v1.

A.2.6b: indexed-row paths (``studio.facts.0.label``,
``contatti.channels.2.value``, ...) are spliced into the baseline
list parents at apply time. Tuples become lists at the column slot
that gets edited (the skin iteration ``for year, title, body in
studio.timeline_rows`` keeps unpacking identically — a 3-element
list unpacks like a 3-element tuple). Dicts and plain-string lists
update in place. See ``apps.editor.schema.STRUCTURED_FIELD_SHAPES``
for the per-list contract.

A.3a: mutable lists (currently ``studio.facts`` + ``studio.partners``)
carry an additional ``__meta__`` sentinel override that describes the
structural mutation — which baseline rows were removed and which uid
rows were added. We materialize the effective list BEFORE applying
cell overrides so per-cell paths land on the right row regardless of
add/remove order. Baseline row indices in cell paths stay stable: a
cell override `.2.name` means "the row that was at baseline position 2",
which may now sit at a different effective-list position after a row
earlier in the list was removed. Added-row cells use an uid prefix:
`.a0.name`, `.a1.name`, etc.

See EDITOR_SCHEMA_BLUEPRINT §7 read-path for the model.
"""
from __future__ import annotations

import copy
from typing import Any

from apps.editor.schema import (
    META_KEY,
    decode_locale_key,
    get_structured_shapes,
    is_uid,
)
from apps.projects.models import CustomerProject


def apply_project_overrides(
    project: CustomerProject,
    content: dict[str, Any],
    theme: dict[str, str],
    locale: str | None = None,
) -> tuple[dict[str, Any], dict[str, str]]:
    """Return (merged_content, merged_theme) with project overrides applied.

    - `content` is the catalog-side registry block (site + pages + per-page keys).
    - `theme` is the catalog-side tokens dict (primary/secondary/accent/fonts).
    - `locale` (A.7 Step 1) is the target render locale. When provided,
      per-locale override rows keyed ``@<code>:<path>`` are applied only
      when ``code == locale``; other locales' rows are skipped. Global
      (unprefixed) rows always apply. A ``None`` locale falls back to
      ``project.locale`` so legacy callers keep working.

    The returned tuple is deep-copied so callers can mutate freely.

    A.3a: two-phase pass. Mutable lists are rebuilt from their
    ``__meta__`` sentinel first so later cell overrides land on the
    correct effective-list position.
    """
    merged_content = copy.deepcopy(content)
    merged_theme = dict(theme)

    target_locale = locale or project.locale or "it"

    shapes = get_structured_shapes(project.source_archetype)
    all_overrides = list(project.content_overrides.all())

    # A.7 Step 1 — split rows by their locale prefix. Rows keyed to a
    # locale other than the render target are dropped here so they
    # never reach the splicer. When both a plain row and a target-
    # locale row exist for the same bare path, the target-locale row
    # wins — per-locale edits supersede legacy shared overrides.
    plain_rows: dict[str, Any] = {}
    locale_rows: dict[str, Any] = {}
    for row in all_overrides:
        row_locale, bare_path = decode_locale_key(row.key_path)
        if row_locale is None:
            plain_rows[bare_path] = row.value_decoded
        elif row_locale == target_locale:
            locale_rows[bare_path] = row.value_decoded
    scoped_rows: list[tuple[str, Any]] = list({
        **plain_rows, **locale_rows,
    }.items())

    # Phase A — materialize mutable lists and compute path-resolution
    # maps. Must happen BEFORE any cell override is applied so splicing
    # does not land on the pre-mutation list.
    list_maps: dict[str, dict[str, Any]] = {}
    for bare_path, value in scoped_rows:
        list_path = _extract_meta_list_path(bare_path)
        if list_path is None:
            continue
        shape = shapes.get(list_path)
        if not shape or not shape.get("mutable"):
            continue
        if not isinstance(value, dict):
            continue
        _materialize_mutable_list(merged_content, list_path, shape, value, list_maps)

    # Phase B — apply cell overrides, routing through list_maps for
    # mutable-list paths so (baseline idx) → (effective pos) and
    # (uid) → (effective pos) resolve correctly.
    for bare_path, value in scoped_rows:
        if _extract_meta_list_path(bare_path) is not None:
            continue
        _apply_override(merged_content, bare_path, value, shapes, list_maps)

    tokens = getattr(project, "tokens", None)
    if tokens is not None:
        merged_theme.update(tokens.as_theme_overlay())

    return merged_content, merged_theme


# ---------------------------------------------------------------------------
# A.3a · mutable-list materialization
# ---------------------------------------------------------------------------

def _extract_meta_list_path(key_path: str) -> str | None:
    """Return the list_path if ``key_path`` is a structural meta sentinel,
    otherwise ``None``. ``"studio.partners.__meta__"`` → ``"studio.partners"``.
    """
    suffix = "." + META_KEY
    if key_path.endswith(suffix):
        return key_path[: -len(suffix)]
    return None


def _shape_default_row(shape: dict[str, Any]) -> Any:
    """Zero-value row for a new (added) row in a mutable list.

    Tuple → list of empty strings in ``tuple_order``.
    Dict  → dict with each declared col set to empty string.
    Scalar → empty string.
    """
    kind = shape.get("kind")
    if kind == "tuple":
        return ["" for _ in shape.get("tuple_order") or []]
    if kind == "dict":
        return {name: "" for name, _spec in shape.get("cols") or []}
    return ""


def compute_default_order(
    baseline_len: int,
    removed: set[int] | list[int] | None,
    added: list[dict[str, Any]] | None,
) -> list[str]:
    """A.3b · the canonical ordering when ``meta.order`` is absent.

    Baseline survivors appear first in ascending index order, then
    added uid rows appear in declaration order. Segments are strings
    (int-as-str for baseline, uid literal for added) so the downstream
    ``order`` array has a uniform element type.

    Services use this to normalize sparse-diff (``order == default``
    strips the field from ``__meta__``) and rendering uses it as a
    safe fallback when ``meta.order`` is malformed or absent.
    """
    removed_set = set(removed or [])
    out: list[str] = [
        str(i) for i in range(baseline_len) if i not in removed_set
    ]
    for entry in added or []:
        if not isinstance(entry, dict):
            continue
        uid = entry.get("uid")
        if isinstance(uid, str) and is_uid(uid):
            out.append(uid)
    return out


def _valid_order_or_default(
    meta: dict[str, Any],
    baseline_len: int,
    removed: set[int],
    added: list[dict[str, Any]],
) -> list[str]:
    """Return ``meta.order`` if it's a valid permutation of the
    expected segment set, otherwise the default order.

    Validation is strict: set equality of segments. Missing or extra
    entries trigger the fallback — the renderer never crashes on a
    malformed meta (defensive), while the service layer remains the
    authoritative guard via explicit validation.
    """
    default = compute_default_order(baseline_len, removed, added)
    raw = meta.get("order")
    if not isinstance(raw, list):
        return default
    cleaned = [s for s in raw if isinstance(s, str)]
    if set(cleaned) == set(default) and len(cleaned) == len(default):
        return cleaned
    return default


def _materialize_mutable_list(
    tree: dict[str, Any],
    list_path: str,
    shape: dict[str, Any],
    meta: dict[str, Any],
    list_maps: dict[str, dict[str, Any]],
) -> None:
    """Rebuild the effective list in-place and record position maps.

    A.3a shape: baseline list filtered by ``meta["removed"]``, uid rows
    from ``meta["added"]`` appended. A.3b extension: ``meta["order"]``
    (when present and valid) rearranges the resulting segments into a
    custom display sequence. Baseline indices never change value — only
    their position in the effective list. Two maps are produced for
    Phase B cell-override application:

    - ``baseline_idx_to_pos`` — baseline row index → position in the
      effective list (or missing if removed).
    - ``uid_to_pos`` — added-row uid → position in the effective list.
    """
    parts = list_path.split(".")
    parent = _walk_to_parent(tree, parts)
    if parent is None:
        return
    last = parts[-1]
    baseline = parent.get(last)
    if not isinstance(baseline, list):
        return

    removed_raw = meta.get("removed") or []
    added_raw = [
        e for e in (meta.get("added") or [])
        if isinstance(e, dict) and isinstance(e.get("uid"), str) and is_uid(e["uid"])
    ]
    removed = {i for i in removed_raw if isinstance(i, int) and 0 <= i < len(baseline)}

    order = _valid_order_or_default(meta, len(baseline), removed, added_raw)

    uid_by_segment = {entry["uid"] for entry in added_raw}

    effective: list[Any] = []
    baseline_idx_to_pos: dict[int, int] = {}
    uid_to_pos: dict[str, int] = {}
    for segment in order:
        if segment in uid_by_segment:
            uid_to_pos[segment] = len(effective)
            effective.append(_shape_default_row(shape))
            continue
        # Otherwise: int-as-str baseline index
        try:
            idx = int(segment)
        except ValueError:
            continue
        if idx < 0 or idx >= len(baseline) or idx in removed:
            continue
        baseline_idx_to_pos[idx] = len(effective)
        effective.append(copy.deepcopy(baseline[idx]))

    parent[last] = effective
    list_maps[list_path] = {
        "baseline_idx_to_pos": baseline_idx_to_pos,
        "uid_to_pos": uid_to_pos,
    }


def _walk_to_parent(tree: dict[str, Any], parts: list[str]) -> dict[str, Any] | None:
    cursor: Any = tree
    for seg in parts[:-1]:
        if not isinstance(cursor, dict):
            return None
        cursor = cursor.get(seg)
        if cursor is None:
            return None
    return cursor if isinstance(cursor, dict) else None


# ---------------------------------------------------------------------------
# Cell override apply (A.2.6b shape, extended with uid + list_maps)
# ---------------------------------------------------------------------------

def _apply_override(
    tree: dict[str, Any],
    key_path: str,
    value: Any,
    shapes: dict[str, dict[str, Any]],
    list_maps: dict[str, dict[str, Any]],
) -> None:
    parts = key_path.split(".")
    list_prefix_len = _find_list_prefix(parts, shapes)
    if list_prefix_len is not None:
        _apply_indexed(tree, parts, list_prefix_len, value, shapes, list_maps)
        return
    _apply_dict_path(tree, parts, value)


def _find_list_prefix(
    parts: list[str], shapes: dict[str, dict[str, Any]],
) -> int | None:
    for cut in range(len(parts) - 1, 0, -1):
        candidate = ".".join(parts[:cut])
        if candidate in shapes:
            return cut
    return None


def _apply_indexed(
    tree: dict[str, Any],
    parts: list[str],
    list_prefix_len: int,
    value: Any,
    shapes: dict[str, dict[str, Any]],
    list_maps: dict[str, dict[str, Any]],
) -> None:
    list_path = ".".join(parts[:list_prefix_len])
    shape = shapes[list_path]

    # A.14 · parent walk supports numeric-index into lists (mirror of
    # ``apps.projects.services._resolve_path`` and the A.14 extension to
    # ``schema._resolve_path``). Sapore's menu rows are registered at
    # deep paths like ``menu.sections.0.dishes`` — the parent chain
    # crosses a dict-list at ``menu.sections`` and the '0' segment
    # indexes into it. Backwards-compat: a dict parent still walks via
    # ``parent.get(seg)`` so all 10 pre-A.14 archetypes stay unchanged.
    parent: Any = tree
    for seg in parts[: list_prefix_len - 1]:
        if isinstance(parent, dict):
            parent = parent.get(seg)
        elif isinstance(parent, list):
            try:
                idx = int(seg)
            except ValueError:
                return
            if idx < 0 or idx >= len(parent):
                return
            parent = parent[idx]
        else:
            return
        if parent is None:
            return
    last_segment = parts[list_prefix_len - 1]
    if not isinstance(parent, dict):
        return
    target_list = parent.get(last_segment)
    if not isinstance(target_list, list):
        return

    remaining = parts[list_prefix_len:]
    if not remaining:
        return  # bare ``studio.facts`` is locked — see LOCKED_KEYS_NOTE

    # A.3a — resolve the first-segment to an effective-list position.
    first = remaining[0]
    list_map = list_maps.get(list_path)
    if list_map is not None:
        # Mutable list: consult the pre-computed maps.
        if first in list_map["uid_to_pos"]:
            pos = list_map["uid_to_pos"][first]
        else:
            try:
                baseline_idx = int(first)
            except ValueError:
                return
            pos = list_map["baseline_idx_to_pos"].get(baseline_idx)
            if pos is None:
                return  # row was removed; orphan override, ignore
    else:
        # Legacy path (A.2.6b): non-mutable list or mutable list with
        # no meta (= no structural mutation yet). Baseline index equals
        # effective position.
        try:
            pos = int(first)
        except ValueError:
            return
        if pos < 0 or pos >= len(target_list):
            return

    kind = shape["kind"]

    if kind == "scalar":
        if len(remaining) != 1:
            return
        if pos < 0 or pos >= len(target_list):
            return
        target_list[pos] = value
        return

    # tuple / dict → need an explicit column at remaining[1]
    if len(remaining) != 2:
        return
    col = remaining[1]
    if pos < 0 or pos >= len(target_list):
        return

    if kind == "tuple":
        order = shape.get("tuple_order") or []
        if col not in order:
            return
        col_idx = order.index(col)
        original = target_list[pos]
        if not isinstance(original, (list, tuple)):
            return
        if col_idx >= len(original):
            return
        new_row = list(original)
        new_row[col_idx] = value
        target_list[pos] = new_row
        return

    if kind == "dict":
        item = target_list[pos]
        if not isinstance(item, dict):
            return
        allowed = {name for name, _spec in shape.get("cols") or []}
        if col not in allowed:
            return
        item[col] = value
        return


def _apply_dict_path(tree: dict[str, Any], parts: list[str], value: Any) -> None:
    cursor: Any = tree
    for seg in parts[:-1]:
        if not isinstance(cursor, dict):
            return
        nxt = cursor.get(seg)
        if not isinstance(nxt, dict):
            return
        cursor = nxt
    if isinstance(cursor, dict):
        cursor[parts[-1]] = value
