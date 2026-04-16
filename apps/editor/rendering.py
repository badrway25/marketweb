"""Project preview rendering — overlay customer overrides on catalog content.

The catalog `LiveTemplateView` composes a context dict from the static
template_content + DNA. When a request carries ``?project=<uuid>``,
this module overlays the project's ProjectContent rows + the
ProjectDesignTokens row on top of that context, producing a context
that still matches the shape the skins expect — so no skin changes
are required for Foundation v1.

See EDITOR_SCHEMA_BLUEPRINT §7 read-path for the model.
"""
from __future__ import annotations

import copy
from typing import Any

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

    overrides = project.get_overrides_dict()
    if overrides:
        _deep_merge(merged_content, overrides)

    tokens = getattr(project, "tokens", None)
    if tokens is not None:
        merged_theme.update(tokens.as_theme_overlay())

    return merged_content, merged_theme


def _deep_merge(target: dict[str, Any], patch: dict[str, Any]) -> None:
    """In-place recursive merge. Scalar / list values replace wholesale."""
    for key, patch_value in patch.items():
        if isinstance(patch_value, dict) and isinstance(target.get(key), dict):
            _deep_merge(target[key], patch_value)
        else:
            target[key] = patch_value
