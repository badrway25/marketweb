"""Corporate-suite palette safety helpers (Phase X.4a Step 1A).

Scope
-----
This module only knows about the *corporate-suite* archetype. Other
archetypes have their own polarity conventions (e.g. the editorial-grid
portfolio archetype is light-primary by design); running these checks
against them would generate false positives.

What the helper enforces
------------------------
CS-PAL-01 [BLOCKING] · `--primary` is the dark foreground token. On the
cream body paper the archetype uses (`#F7F4EC` / `#EEF0F3`), the primary
hex must pass one of the WCAG luminance gates:

    - L*  ≤ 40 (roughly: max-channel ≤ 80 on a neutral hue)
    - Contrast ratio ≥ 7.0  against cream paper (AAA for h1–h5 text)

When the skin runs with a light primary, every h1/h2/h3 on the cream
paper silently renders invisible (Solaria `e8f38b5` → `6b70d56` incident).
Test suites never caught it. The layered defense is:

    1. Builder L* self-check (template author)
    2. Pre-render Python audit (this module) — emits warnings, never raises
    3. Contrast auditor + live browser walk (ship gate)

This Step 1A layer is intentionally *lenient*: it WARNS but never raises,
because it runs inside the live-preview request path and must not 500 the
page for a legacy palette. Promotion of the warning into a hard block
belongs to a later step once every in-repo corporate-suite palette has
been audited.

Outputs
-------
`enrich_corporate_suite_theme(theme)` returns the theme dict augmented
with derived safety tokens:

    {
        "primary":            "<unchanged>",
        "secondary":          "<unchanged>",
        "accent":             "<unchanged>",
        "heading_font":       "<unchanged>",
        "body_font":           "<unchanged>",
        # ── derived safety tokens ──────────────────────────
        "on_primary":         "#F7F4EC" | "#0F172A",
        "primary_is_safe":    True | False,
        "primary_contrast":   float (ratio vs cream paper),
        "accent_on_primary_contrast": float,
    }

These are consumed by `_base.html` and downstream page files if they wish
to branch on `theme.primary_is_safe`.
"""
from __future__ import annotations

import warnings

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CORPORATE_SUITE_ARCHETYPE = "corporate-suite"

# Body paper convention across the archetype. Match the value declared in
# `_base.html` under `--paper` (the actual rendered page background) when
# inferring text contrast. The design standard cites `#F7F4EC` cream —
# keep the lookup aware of both the current skin default and the canonical
# standard value; we run the check against the lighter of the two so a
# failing palette fails conservatively.
SKIN_PAPER_HEX = "#EEF0F3"
STANDARD_CREAM_HEX = "#F7F4EC"

# AA / AAA contrast floors per WCAG 2.1.
WCAG_AA_BODY = 4.5
WCAG_AAA_BODY = 7.0

# Luminance ceiling that approximates L* ≤ 40 in CIELAB on a neutral hue.
# We use relative luminance (WCAG) because that is what contrast ratios
# build on; the CIELAB L* threshold maps to Y ≈ 0.1241.
PRIMARY_MAX_LUMINANCE = 0.12


# ---------------------------------------------------------------------------
# Color math
# ---------------------------------------------------------------------------

def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """Parse `#RRGGBB` or `#RGB` to an (R, G, B) tuple of 0–255 ints."""
    h = (hex_str or "").lstrip("#").strip()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid hex color: {hex_str!r}")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _srgb_channel(c: int) -> float:
    v = c / 255.0
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_str: str) -> float:
    """Relative luminance per WCAG 2.1 §1.4.3 (0.0 – 1.0)."""
    r, g, b = hex_to_rgb(hex_str)
    return (
        0.2126 * _srgb_channel(r)
        + 0.7152 * _srgb_channel(g)
        + 0.0722 * _srgb_channel(b)
    )


def contrast_ratio(fg_hex: str, bg_hex: str) -> float:
    """WCAG contrast ratio between two hex colors (1.0 – 21.0)."""
    l1 = relative_luminance(fg_hex)
    l2 = relative_luminance(bg_hex)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)


# ---------------------------------------------------------------------------
# Corporate-suite specific checks
# ---------------------------------------------------------------------------

def is_primary_safe_on_cream(primary_hex: str) -> tuple[bool, float, float]:
    """Return (is_safe, luminance, contrast_ratio_vs_cream) for the given
    `--primary`. Runs against the lighter of the two canonical papers so a
    borderline primary fails against whichever paper the skin is actually
    painting with.
    """
    try:
        lum = relative_luminance(primary_hex)
    except ValueError:
        return False, 1.0, 1.0
    ratio_skin = contrast_ratio(primary_hex, SKIN_PAPER_HEX)
    ratio_cream = contrast_ratio(primary_hex, STANDARD_CREAM_HEX)
    worst_ratio = min(ratio_skin, ratio_cream)
    is_safe = lum <= PRIMARY_MAX_LUMINANCE and worst_ratio >= WCAG_AAA_BODY
    return is_safe, lum, worst_ratio


def enrich_corporate_suite_theme(
    theme: dict[str, str],
    *,
    template_slug: str | None = None,
    warn: bool = True,
) -> dict[str, str]:
    """Return a new theme dict with derived safety tokens merged in.

    Always returns a dict (never raises for a legacy palette). If the
    supplied primary fails the CS-PAL-01 gate AND `warn=True`, emits a
    `UserWarning` naming the offending palette — caught by the test suite
    or by ops during template authoring.

    The input dict is not mutated. Unknown keys are copied through.
    """
    out = dict(theme)
    primary = out.get("primary") or "#0F172A"
    accent = out.get("accent") or "#C8A44E"

    is_safe, lum, primary_contrast = is_primary_safe_on_cream(primary)
    try:
        accent_on_primary = contrast_ratio(accent, primary)
    except ValueError:
        accent_on_primary = 1.0

    # `--on-primary` is always cream on the corporate-suite archetype: the
    # convention is dark-foreground on cream paper, so the inverted
    # surfaces (navbar, KPI band, CTA, footer) read cream-on-primary. If
    # the primary fails the gate we still return cream to keep the
    # template *renderable* (otherwise every inverted surface would lose
    # its foreground), but we emit a warning so the defect surfaces.
    out["on_primary"] = "#F7F4EC"
    out["primary_is_safe"] = is_safe
    out["primary_luminance"] = round(lum, 4)
    out["primary_contrast"] = round(primary_contrast, 2)
    out["accent_on_primary_contrast"] = round(accent_on_primary, 2)

    if warn and not is_safe:
        slug_suffix = f" for template {template_slug!r}" if template_slug else ""
        warnings.warn(
            (
                "corporate-suite palette safety check failed"
                f"{slug_suffix}: primary={primary!r} luminance={lum:.4f} "
                f"contrast-vs-cream={primary_contrast:.2f}. "
                "CS-PAL-01 requires a dark primary "
                f"(luminance ≤ {PRIMARY_MAX_LUMINANCE} and contrast ≥ "
                f"{WCAG_AAA_BODY}:1 vs cream paper). "
                "The skin will still render with cream on primary, but "
                "h1/h2/h3 on the body paper may be unreadable."
            ),
            UserWarning,
            stacklevel=2,
        )

    return out


def should_enrich(archetype: str | None) -> bool:
    """Whether the theme-safety enrichment should run for this archetype."""
    return archetype == CORPORATE_SUITE_ARCHETYPE
