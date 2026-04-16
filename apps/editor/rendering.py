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

See EDITOR_SCHEMA_BLUEPRINT §7 read-path for the model.
"""
from __future__ import annotations

import copy
from typing import Any

from apps.editor.schema import get_structured_shapes
from apps.projects.models import CustomerProject


def apply_project_overrides(
    project: CustomerProject,
    content: dict[str, Any],
    theme: dict[str, str],
) -> tuple[dict[str, Any], dict[str, str]]:
    """Return (merged_content, merged_theme) with project overrides applied.

    - `content` is the catalog-side registry block (site + pages + per-page keys).
    - `theme` is the catalog-side tokens dict (primary/secondary/accent/fonts).
    The returned tuple is deep-copied so callers can mutate freely.
    """
    merged_content = copy.deepcopy(content)
    merged_theme = dict(theme)

    shapes = get_structured_shapes(project.source_archetype)
    for row in project.content_overrides.all():
        _apply_override(merged_content, row.key_path, row.value_decoded, shapes)

    tokens = getattr(project, "tokens", None)
    if tokens is not None:
        merged_theme.update(tokens.as_theme_overlay())

    return merged_content, merged_theme


def _apply_override(
    tree: dict[str, Any],
    key_path: str,
    value: Any,
    shapes: dict[str, dict[str, Any]],
) -> None:
    """Apply a single override row to the baseline tree.

    Three branches:
    - The key_path matches a list-prefix in ``shapes`` → splice into
      the baseline list at the right (row, column) cell.
    - Otherwise → walk the dict-only path and set the leaf, creating
      nothing along the way (so a typoed override never invents
      structure that the skin would then crash trying to render).
    """
    parts = key_path.split(".")

    list_prefix_len = _find_list_prefix(parts, shapes)
    if list_prefix_len is not None:
        _apply_indexed(tree, parts, list_prefix_len, value, shapes)
        return

    _apply_dict_path(tree, parts, value)


def _find_list_prefix(
    parts: list[str], shapes: dict[str, dict[str, Any]],
) -> int | None:
    """Length of the longest prefix in ``parts`` that names a list path.

    Returns the *segment count* of the prefix, not a string length.
    Walks longest-first so a nested list (none today, but guarded for
    Phase A.3) prefers the deeper match.
    """
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
) -> None:
    list_path = ".".join(parts[:list_prefix_len])
    shape = shapes[list_path]

    # Walk dicts down to the parent of the list, then resolve the list itself.
    parent = tree
    for seg in parts[: list_prefix_len - 1]:
        if not isinstance(parent, dict):
            return
        parent = parent.get(seg)
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
    try:
        idx = int(remaining[0])
    except ValueError:
        return
    if idx < 0 or idx >= len(target_list):
        return

    kind = shape["kind"]

    if kind == "scalar":
        if len(remaining) != 1:
            return
        target_list[idx] = value
        return

    # tuple / dict → need an explicit column at remaining[1]
    if len(remaining) != 2:
        return
    col = remaining[1]

    if kind == "tuple":
        order = shape.get("tuple_order") or []
        if col not in order:
            return
        col_idx = order.index(col)
        original = target_list[idx]
        if not isinstance(original, (list, tuple)):
            return
        if col_idx >= len(original):
            return
        new_row = list(original)
        new_row[col_idx] = value
        target_list[idx] = new_row
        return

    if kind == "dict":
        item = target_list[idx]
        if not isinstance(item, dict):
            return
        # Limit writes to the schema-declared columns so a typo can never
        # poison a dict with garbage keys the skin doesn't expect.
        allowed = {name for name, _spec in shape.get("cols") or []}
        if col not in allowed:
            return
        item[col] = value
        return


def _apply_dict_path(tree: dict[str, Any], parts: list[str], value: Any) -> None:
    """Set a leaf inside a baseline dict tree.

    Strict: every intermediate segment must exist as a dict. We never
    invent structure — if the path doesn't already resolve, the
    override is silently dropped at apply time. Validation upstream
    (validate_key_path) is the layer that prevents bogus paths from
    ever being stored.
    """
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
