"""Corporate-suite mechanical contrast audit (Phase X.4b · AP-4 pass 1).

Scope
-----
This module closes the AP-4 "palette-contrast invariant mechanically
enforced" item from the pre-Solaria-Commit-B closure set
(``factory/references/anti-pattern-library.md §0``). Until this pass,
DS-16 ("never use ``--accent`` as text against ``--primary``") and the
companion BO-08 scorecard override existed only as **prose** in the
factory standards — caught by AG-6 Contrast Auditor *during a live
browser walk*, never by unit tests, ``manage.py check``, or CI.

Two complementary mechanical checks ship here:

1. **Per-palette numeric audit** (``audit_enrolled_palettes``). Every
   enrolled corporate-suite palette is fed through a WCAG 2.1 ratio
   calculation for the canonical (foreground × background) pairs the
   archetype actually uses. Gating threshold for *body* text:
   ``WCAG_AA_BODY = 4.5``; for *large* (≥18 pt or ≥14 pt bold)
   text: ``WCAG_AA_LARGE = 3.0``; for purely decorative non-text use
   (≤2 px rules, focus outlines, icon glyphs not communicating
   information): ``WCAG_DECORATIVE = 3.0``.

2. **Static CSS scanner** (``audit_chrome_for_ap4``). The corporate-
   suite live skin paints text via ``color: var(--accent)`` in a
   handful of selectors whose ancestor is a *dark* band (``.cs-nav``,
   ``.cs-section.dark``, ``.cs-kpi-band``, ``.cs-cta``, ``.cs-foot``,
   ``.cs-foot-col--whistleblowing``). The list of currently shipped
   selectors is pinned in ``KNOWN_AP4_BASELINE_SELECTORS`` — any *new*
   selector that paints accent-text on a dark band surfaces as a
   regression. The scanner walks every chrome HTML file under
   ``templates/live_templates/business/corporate-suite/`` plus the
   per-layout-family folders ``_layouts/lf*/styles.html``.

Why detection, not remediation, in pass 1
-----------------------------------------
Per the X.4b task brief: "Be conservative: do not redesign the
templates, only strengthen contrast detection/enforcement. Preserve
published siblings visually unless a real contrast defect requires a
minimal fix." The four already-shipped chrome selectors that render
accent-text on dark bands fail for Fiscus / Solaria / Cornice / Causa
palettes — that is a pre-existing, *acknowledged* defect documented as
``LEGACY_AP4_PALETTE_EXEMPT_SLUGS`` and recorded in the X.4a
``factory/reports/scorecard/<slug>/contrast-accessibility.md`` audits.
A subsequent pass (AP-4 pass 2) lifts the four selectors onto a new
``--accent-text-on-primary-safe`` token that auto-degrades to
``--on-dark`` for palettes that fail the floor — that is *remediation*
work and stays out of this pass to keep the surface area small.

What pass 1 *does* mechanically catch (the "regressions of interest")
---------------------------------------------------------------------
- A *new* corporate-suite palette enrollment whose accent fails the
  AA body floor on its primary (E004 Error).
- A *new* CSS rule painting ``color: var(--accent)`` on a selector
  whose context names a known dark-band class, beyond the four
  pinned baseline selectors (E005 Error).
- A pinned baseline selector that has been *removed* from the chrome
  (W004 Warning — invites the human author to delete the now-stale
  baseline entry, otherwise the regression guard remains effective).

What still belongs in browser verification
------------------------------------------
The mechanical checks above bind to the **declared** color tokens and
the **static** CSS rules. They do NOT — and cannot, without a
headless browser — verify:

- Hero credit-ribbon contrast against a particular Pexels frame
  (depends on the photograph, not the CSS); covered by AG-6 §3.6
  hero seven-gate plus the BR-23 hero-photo overlay floor in the
  browser rubric.
- The actual *rendered* RGB after gradient compositing, blend modes,
  or image overlay on a live DOM; covered by AG-6 §3.3 dark-section
  child contrast (Playwright-driven).
- Focus-visible accent vs background under hover/active state cycles;
  covered by AG-6 §3.5 focus-visible walk.
- The reduced-motion + blur regression cells captured by the BR-21
  / BR-27 viewport matrix.

Cross-references
----------------
- ``factory/standards/corporate-suite-design-standard.md`` §DS-15 / DS-16
- ``factory/standards/corporate-suite-blocking-rules.md`` §BLOCK-11
- ``factory/standards/corporate-suite-quality-scorecard.md`` §BO-08
- ``factory/standards/corporate-suite-browser-rubric.md`` §BR-20
- ``factory/agents/contrast-accessibility-auditor.md`` §3.2 / §3.3
- ``factory/references/anti-pattern-library.md`` §AP-4
- ``apps/catalog/theme_safety.py`` — sibling validator (CS-PAL-01).
- ``apps/catalog/imagery_policy.py`` — sibling validator (CS-IMG-SRC-01).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Iterator

from apps.catalog.theme_safety import contrast_ratio, hex_to_rgb

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CORPORATE_SUITE_ARCHETYPE = "corporate-suite"

# WCAG 2.1 floors. Body text == "small text" in WCAG vocabulary.
WCAG_AA_BODY = 4.5
WCAG_AA_LARGE = 3.0
WCAG_DECORATIVE = 3.0
WCAG_AAA_BODY = 7.0

# CSS class names that paint a dark band (background == ``var(--primary)`` or
# a near-primary surface). Any text rendered as a descendant of these
# classes is composited against ``--primary`` for contrast purposes.
DARK_BAND_CLASSES = (
    ".cs-nav",
    ".cs-section.dark",
    ".cs-kpi-band",
    ".cs-cta",
    ".cs-foot",
    ".cs-foot-col--whistleblowing",
)

# AP-4 pass 2 (2026-05-10) drained this baseline: the six chrome
# selectors below previously painted ``color: var(--accent)`` as text on
# a dark band and were tracked as the documented AP-4 trap. Pass 2
# lifted each onto the new ``--accent-text-on-primary-safe`` CSS custom
# property (resolved by ``apps.catalog.theme_safety``). The selectors
# now render via the safe-degrading token; the regression guard below
# (E005) therefore protects against any *new* dark-band accent-text
# selector being introduced — the pinned baseline is intentionally
# empty so the guard is fully active.
#
# NB: a single CSS rule may carry several comma-separated selectors —
# the scanner emits ONE entry per source-line declaration, with the
# selector text normalised (whitespace collapsed) so a future re-format
# does not silently invalidate the baseline match.
KNOWN_AP4_BASELINE_SELECTORS: frozenset[str] = frozenset()

# AP-4 pass 2 (2026-05-10) drained this exemption: the five legacy
# palettes whose accent fails the AA body floor on their primary
# (Fiscus / Solaria / Cornice / Causa / Continua) no longer render
# accent-text on dark bands — the chrome lift switched the six
# baseline selectors onto ``--accent-text-on-primary-safe``, which
# theme_safety degrades to ``var(--on-dark)`` for any palette whose
# accent fails the floor. The italic emphasis on those palettes now
# reads cream-on-dark instead of unreadable accent-on-dark.
#
# The frozenset is intentionally empty post-pass-2; instead the new
# ``CHROME_SAFE_DEGRADES_ACCENT_ON_DARK`` flag below records that the
# chrome itself now safe-degrades, and ``audit_enrolled_palettes``
# uses the flag to mark every failing palette as ``is_legacy_exempt
# = True`` (i.e. "the chrome handles this case"). A palette whose
# accent fails AND the chrome does NOT safe-degrade (e.g. a future
# regression) would be a hard E004 error.
LEGACY_AP4_PALETTE_EXEMPT_SLUGS: frozenset[str] = frozenset()

# AP-4 pass 2 invariant: as long as the chrome consumes
# ``--accent-text-on-primary-safe`` for every dark-band accent-text
# rule, every enrolled palette with a failing accent ratio is rendered
# legibly via the cream fallback. Setting this False would re-arm the
# E004 hard error path for failing palettes — only flip when a future
# pass moves the chrome away from the safe-degrading token.
CHROME_SAFE_DEGRADES_ACCENT_ON_DARK = True


# ---------------------------------------------------------------------------
# Per-palette ratio audit
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PaletteContrastReport:
    """Numeric audit of every canonical pair an enrolled palette uses.

    Tier vocabulary maps directly to the rule citations:

    - ``accent_on_primary``   — DS-16 / BO-08 / BLOCK-11 (text floor 4.5)
    - ``secondary_on_primary``— DS-15 / BLOCK-11 (text floor 4.5; tags + KPI numerals)
    - ``accent_on_paper``     — DS-15 (italic emphasis, arrow glyph)
    - ``accent_on_paper_2``   — DS-15 (alt cards, sectors band)

    The dataclass is frozen so callers can safely embed it inside test
    fixtures or check findings without aliasing risk.
    """

    slug: str
    primary: str
    secondary: str
    accent: str
    paper: str = "#EEF0F3"
    paper_2: str = "#F5F6F8"

    accent_on_primary: float = 0.0
    secondary_on_primary: float = 0.0
    accent_on_paper: float = 0.0
    accent_on_paper_2: float = 0.0
    secondary_on_paper: float = 0.0

    @property
    def accent_text_on_primary_passes_aa(self) -> bool:
        return self.accent_on_primary >= WCAG_AA_BODY

    @property
    def accent_decorative_on_primary_passes(self) -> bool:
        return self.accent_on_primary >= WCAG_DECORATIVE

    @property
    def secondary_text_on_primary_passes_aa(self) -> bool:
        return self.secondary_on_primary >= WCAG_AA_BODY


def palette_pair_audit(
    slug: str,
    palette: dict[str, str],
    *,
    paper_hex: str = "#EEF0F3",
    paper_2_hex: str = "#F5F6F8",
) -> PaletteContrastReport:
    """Compute every (foreground × background) ratio the corporate-suite
    archetype actually paints, for ``palette`` (``primary`` / ``secondary``
    / ``accent`` keys required).

    Returns a :class:`PaletteContrastReport`. Never raises — invalid hex
    values fall through as ``1.0`` ratios so the caller can surface them
    as defects without a 500 response on the live preview path.
    """
    primary = palette.get("primary") or "#0F172A"
    secondary = palette.get("secondary") or "#94A3B8"
    accent = palette.get("accent") or "#C8A44E"

    def _safe(fg: str, bg: str) -> float:
        try:
            return round(contrast_ratio(fg, bg), 2)
        except (ValueError, TypeError):
            return 1.0

    return PaletteContrastReport(
        slug=slug,
        primary=primary,
        secondary=secondary,
        accent=accent,
        paper=paper_hex,
        paper_2=paper_2_hex,
        accent_on_primary=_safe(accent, primary),
        secondary_on_primary=_safe(secondary, primary),
        accent_on_paper=_safe(accent, paper_hex),
        accent_on_paper_2=_safe(accent, paper_2_hex),
        secondary_on_paper=_safe(secondary, paper_hex),
    )


def is_accent_text_safe_on_primary(accent_hex: str, primary_hex: str) -> bool:
    """Single-purpose decision used by the build-time check.

    Returns True iff ``contrast_ratio(accent, primary) ≥ WCAG_AA_BODY``.
    A False result + ``color: var(--accent)`` rendered as text on the
    dark band == the AP-4 trap.
    """
    try:
        return contrast_ratio(accent_hex, primary_hex) >= WCAG_AA_BODY
    except (ValueError, TypeError):
        return False


# ---------------------------------------------------------------------------
# CSS scanner — small, deliberate, regex-only
# ---------------------------------------------------------------------------

# Regex matches a single rule of the form ``selector { body }``. The
# selector pattern is deliberately greedy *up to* the next ``{`` so a
# multi-selector list ("a, b, c") stays whole. We tolerate
# pre/post-rule comments by anchoring on the brace pairs only.
_RULE_RE = re.compile(r"([^{}/]+?)\{([^{}]*)\}", re.DOTALL)

# Inside a rule body, "color: var(--accent)" is the AP-4 fingerprint.
# Border / outline / background / fill use of accent are not text and
# are explicitly out of scope (decorative — DS-15 sub-clause).
#
# The lookbehind requires the property name to start at a real
# declaration boundary (rule-body start ``\A``, after ``;``, or after
# ``{``) so ``border-color: var(--accent)``, ``outline-color: var(--accent)``,
# ``background-color: var(--accent)``, ``border-bottom-color: var(--accent)``
# do NOT match. Whitespace between the boundary and ``color`` is
# tolerated so vertically-formatted rules still parse.
_ACCENT_TEXT_DECL_RE = re.compile(
    r"(?:\A|[;{])\s*color\s*:\s*var\s*\(\s*--accent\s*\)"
)

# Strip ``/* ... */`` comments out of a CSS body before fingerprint
# matching so an explanatory comment that quotes ``color: var(--accent)``
# (e.g. ``Was 'color: var(--accent)'``) does not create a false-positive
# regression hit for a rule whose actual ``color`` declaration is safe.
_CSS_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)


@dataclass(frozen=True)
class CssAccentFinding:
    """A single CSS rule that paints ``color: var(--accent)`` and whose
    selector context names a dark-band class.
    """

    file_path: str
    selector: str
    line_no: int

    @property
    def normalised_selector(self) -> str:
        """Whitespace-collapsed selector text used for baseline comparison."""
        return _normalise_selector(self.selector)


def _normalise_selector(selector: str) -> str:
    """Collapse whitespace + strip outer comment markers so a future
    formatting tweak does not silently break a baseline match.
    """
    cleaned = re.sub(r"/\*.*?\*/", "", selector, flags=re.DOTALL)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _class_token_present(needle: str, haystack: str) -> bool:
    """Return True iff ``haystack`` contains the CSS class token
    ``needle`` with proper class-boundary handling.

    A naive substring match would treat ``.cs-cta-cream`` as if it
    contained ``.cs-cta`` — but ``.cs-cta-cream`` is a separate (cream-
    band, light-surface) class. The boundary characters that legally
    end a CSS class identifier are: end-of-string, whitespace, ``,``,
    ``>``, ``+``, ``~``, ``.``, ``#``, ``[``, ``:``, ``)``.
    """
    pos = 0
    while True:
        idx = haystack.find(needle, pos)
        if idx == -1:
            return False
        end = idx + len(needle)
        next_char = haystack[end] if end < len(haystack) else ""
        if next_char == "" or next_char in " \t\n,>+~.#[:)" :
            return True
        pos = end


def _selector_touches_dark_band(selector: str) -> bool:
    """Return True iff any token of the (possibly comma-separated)
    selector list contains a known dark-band class with proper class-
    boundary handling.

    A single ``var(--accent)`` rule may legitimately apply to multiple
    selectors, e.g. ``.cs-kpi-band em, .cs-cta em, .cs-foot em`` —
    presence of *any* dark-band token marks the rule as AP-4-relevant.
    """
    norm = _normalise_selector(selector)
    return any(_class_token_present(klass, norm) for klass in DARK_BAND_CLASSES)


def parse_css_rules(css_text: str) -> Iterator[tuple[str, str, int]]:
    """Yield ``(selector, body, line_no)`` for every CSS rule in ``css_text``.

    Best-effort regex parser. Skips rules whose body contains a nested
    brace (e.g. ``@media`` blocks) on the first pass — those are
    flattened by recursing into the inner text.
    """
    line_offsets = [m.start() for m in re.finditer(r"\n", css_text)]

    def _line_for(pos: int) -> int:
        # Binary-search-free: line offsets are typically small (≤ a few
        # thousand) for our chrome files; linear scan is fast enough and
        # keeps the implementation transparent.
        n = 1
        for off in line_offsets:
            if off >= pos:
                return n
            n += 1
        return n

    # First pass: walk top-level rules and recurse into @media-style
    # blocks. The regex below specifically excludes rules whose body
    # contains another opening brace — those are handled by the
    # recursive _flatten step.
    def _walk(text: str, base_pos: int) -> Iterator[tuple[str, str, int]]:
        pos = 0
        while pos < len(text):
            # Find the next opening brace.
            brace = text.find("{", pos)
            if brace == -1:
                return
            # Find the matching closing brace, accounting for nesting.
            depth = 1
            scan = brace + 1
            while scan < len(text) and depth > 0:
                ch = text[scan]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                scan += 1
            if depth != 0:
                # Unbalanced — give up on the rest of the buffer.
                return
            selector = text[pos:brace].strip()
            body = text[brace + 1 : scan - 1]
            line_no = _line_for(base_pos + brace)
            # If the body contains another brace, this is a wrapper
            # block (@media, @supports, ...). Recurse into the body to
            # surface its inner rules with their selectors intact.
            if "{" in body:
                yield from _walk(body, base_pos + brace + 1)
            else:
                yield selector, body, line_no
            pos = scan

    yield from _walk(css_text, 0)


def find_accent_text_on_dark_in_css(
    css_text: str, *, file_path: str = "<inline>"
) -> list[CssAccentFinding]:
    """Return every ``color: var(--accent)`` rule whose selector touches a
    dark-band class.

    The body match is deliberately strict ("color: var(--accent)") — we
    do NOT flag ``border-color: var(--accent)``, ``background:
    var(--accent)``, ``outline-color: var(--accent)`` or arbitrary
    ``var(--accent)`` references in shadows / gradients. Those are
    decorative uses sanctioned by DS-15.
    """
    findings: list[CssAccentFinding] = []
    for selector, body, line_no in parse_css_rules(css_text):
        # Strip CSS comments before fingerprint matching so a comment
        # that quotes ``color: var(--accent)`` (explanatory: "Was
        # `color: var(--accent)`. Failed Fiscus contrast...") does not
        # raise a false-positive regression on a rule whose actual
        # color declaration is safe.
        body_no_comments = _CSS_COMMENT_RE.sub("", body)
        if not _ACCENT_TEXT_DECL_RE.search(body_no_comments):
            continue
        if not _selector_touches_dark_band(selector):
            continue
        findings.append(
            CssAccentFinding(
                file_path=file_path,
                selector=_normalise_selector(selector),
                line_no=line_no,
            )
        )
    return findings


# ---------------------------------------------------------------------------
# Chrome enumeration + audit
# ---------------------------------------------------------------------------

def _chrome_root() -> Path:
    """Return ``Path(BASE_DIR) / 'templates' / 'live_templates' / 'business' / 'corporate-suite'``.

    Resolved lazily so the module imports cleanly outside Django (e.g.
    from a standalone unittest invocation that bypasses Django bootstrap).
    """
    from django.conf import settings

    return Path(settings.BASE_DIR) / "templates" / "live_templates" / "business" / "corporate-suite"


def iter_corporate_suite_chrome_files(root: Path | None = None) -> Iterator[Path]:
    """Yield every HTML file that contributes to the corporate-suite live
    chrome contrast surface.

    Order is deterministic so test output is stable: ``_base.html`` first,
    then per-layout-family ``_layouts/lf*/styles.html`` in lexical order.
    """
    base = root if root is not None else _chrome_root()
    base_html = base / "_base.html"
    if base_html.exists():
        yield base_html
    layouts = base / "_layouts"
    if layouts.exists():
        for child in sorted(layouts.iterdir()):
            styles = child / "styles.html"
            if styles.exists():
                yield styles


@dataclass
class ChromeAuditReport:
    """Aggregate of every CSS finding across the corporate-suite chrome."""

    findings: list[CssAccentFinding] = field(default_factory=list)
    files_scanned: list[str] = field(default_factory=list)

    @property
    def selectors_seen(self) -> set[str]:
        return {f.normalised_selector for f in self.findings}

    @property
    def regressions(self) -> list[CssAccentFinding]:
        """Findings whose selector is NOT pinned in the baseline."""
        return [
            f for f in self.findings
            if f.normalised_selector not in KNOWN_AP4_BASELINE_SELECTORS
        ]

    @property
    def baseline_misses(self) -> set[str]:
        """Baseline selectors no longer present in the scanned chrome —
        these warrant a baseline cleanup once the fix lands.
        """
        return KNOWN_AP4_BASELINE_SELECTORS - self.selectors_seen


def audit_chrome_for_ap4(root: Path | None = None) -> ChromeAuditReport:
    """Walk every corporate-suite chrome HTML file and return a
    :class:`ChromeAuditReport` enumerating accent-text-on-dark rules.

    Caller (the Django check or a unit test) compares ``regressions`` to
    fail/pass and ``baseline_misses`` to suggest baseline cleanup.
    """
    report = ChromeAuditReport()
    for path in iter_corporate_suite_chrome_files(root):
        report.files_scanned.append(str(path))
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        report.findings.extend(
            find_accent_text_on_dark_in_css(text, file_path=str(path))
        )
    return report


# ---------------------------------------------------------------------------
# Per-palette enrollment audit (consumed by the Django check)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class EnrolledPaletteFinding:
    """One enrolled corporate-suite palette's accent-on-primary verdict."""

    slug: str
    primary: str
    accent: str
    accent_on_primary: float
    passes_aa_text_floor: bool
    is_legacy_exempt: bool

    @property
    def severity(self) -> str:
        if self.passes_aa_text_floor:
            return "ok"
        return "warning" if self.is_legacy_exempt else "error"


def _iter_enrolled_corporate_suite_brands() -> Iterator[tuple[str, dict[str, str]]]:
    """Yield ``(slug, palette_dict)`` for every enrolled corporate-suite
    template, sourcing palettes from ``SEED_TEMPLATES`` × ``TEMPLATE_DNA``
    (mirrors the existing pattern in ``apps.catalog.checks``).

    Deferred imports so this module loads cleanly during ``apps.ready``
    bootstrap.
    """
    from apps.catalog.management.commands.seed_templates import SEED_TEMPLATES
    from apps.catalog.template_dna import TEMPLATE_DNA

    for entry in SEED_TEMPLATES:
        slug = entry.get("slug")
        dna = TEMPLATE_DNA.get(slug) if slug else None
        if not dna or dna.get("archetype") != CORPORATE_SUITE_ARCHETYPE:
            continue
        brand = entry.get("brand") or {}
        palette = brand.get("palette") or {}
        if not palette.get("primary"):
            continue
        yield slug, palette


def audit_enrolled_palettes() -> list[EnrolledPaletteFinding]:
    """Return one :class:`EnrolledPaletteFinding` per enrolled palette,
    annotated with whether it passes the accent-text-on-primary floor and
    whether it sits on the documented legacy exemption list.

    Stable ordering: by slug.
    """
    findings: list[EnrolledPaletteFinding] = []
    for slug, palette in _iter_enrolled_corporate_suite_brands():
        primary = palette["primary"]
        accent = palette.get("accent") or "#C8A44E"
        try:
            ratio = round(contrast_ratio(accent, primary), 2)
        except (ValueError, TypeError):
            ratio = 1.0
        passes = ratio >= WCAG_AA_BODY
        # AP-4 pass 2 semantics: a palette is "legacy exempt" iff either
        #   (a) it's on the documented LEGACY frozenset (post-pass-2
        #       empty by default — kept as opt-in for future regressions),
        #   OR
        #   (b) the chrome itself safe-degrades accent-text on dark via
        #       --accent-text-on-primary-safe. A failing palette is then
        #       rendered legibly cream-on-dark and is informational, not
        #       an error.
        is_exempt = (
            slug in LEGACY_AP4_PALETTE_EXEMPT_SLUGS
            or (not passes and CHROME_SAFE_DEGRADES_ACCENT_ON_DARK)
        )
        findings.append(
            EnrolledPaletteFinding(
                slug=slug,
                primary=primary,
                accent=accent,
                accent_on_primary=ratio,
                passes_aa_text_floor=passes,
                is_legacy_exempt=is_exempt,
            )
        )
    findings.sort(key=lambda f: f.slug)
    return findings


def hex_distance(a_hex: str, b_hex: str) -> float:
    """Euclidean RGB distance between two hex colors. Used by AG-6 §3.2
    "RGB distance ≥ 120" hard-veto language; exposed here so the test
    suite can lock the math even when no Playwright walk is in flight.
    """
    try:
        ar, ag, ab = hex_to_rgb(a_hex)
        br, bg, bb = hex_to_rgb(b_hex)
    except (ValueError, TypeError):
        return 0.0
    return ((ar - br) ** 2 + (ag - bg) ** 2 + (ab - bb) ** 2) ** 0.5


def should_audit(archetype: str | None) -> bool:
    """Whether the AP-4 mechanical audit should run for this archetype."""
    return archetype == CORPORATE_SUITE_ARCHETYPE


__all__ = [
    "CORPORATE_SUITE_ARCHETYPE",
    "WCAG_AA_BODY",
    "WCAG_AA_LARGE",
    "WCAG_DECORATIVE",
    "WCAG_AAA_BODY",
    "DARK_BAND_CLASSES",
    "KNOWN_AP4_BASELINE_SELECTORS",
    "LEGACY_AP4_PALETTE_EXEMPT_SLUGS",
    "PaletteContrastReport",
    "CssAccentFinding",
    "ChromeAuditReport",
    "EnrolledPaletteFinding",
    "palette_pair_audit",
    "is_accent_text_safe_on_primary",
    "parse_css_rules",
    "find_accent_text_on_dark_in_css",
    "iter_corporate_suite_chrome_files",
    "audit_chrome_for_ap4",
    "audit_enrolled_palettes",
    "hex_distance",
    "should_audit",
]
