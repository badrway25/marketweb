# Corporate-suite Factory Hardening · Step 1 · Core hardening report

**Phase**: X.4a · **Branch**: `phase-x4a-corporate-factory-hardening-core`
**Scope constraint**: factory + corporate-suite archetype files only. Zero
`apps/editor`, `apps/projects`, `apps/commerce` changes. No new archetypes.
Solaria Commit B remains paused per the binding user instruction quoted in
`factory/reports/audits/corporate-suite-audit-master.md` §7.

---

## Step 1A — Contrast & Palette Safety

Goal: close the palette-polarity / contrast half of the `AP1` + `AP11`
systemic risk surfaced by the audit, without touching the responsive,
imagery, or motion gaps (those land in later Step 1 sub-steps).

### Files changed

| File | Change |
|---|---|
| `templates/live_templates/business/corporate-suite/_base.html` | (1) Retire the dead `--primary-2: #2c3e6b` declaration (AP7). (2) Introduce `--on-primary` + `--on-primary-soft` safety tokens plumbed from `theme.on_primary`. (3) Swap the navbar `.is-current` accent-text with an accent underline (CS-NAV-02 active-state fix). (4) Add a dark-surface descendant cascade covering `.cs-section.dark`, `.cs-kpi-band`, `.cs-cta`, `.cs-foot` so future `<p>/<li>/<dt>/<dd>/<small>/<time>` descendants default to `--on-primary-soft` instead of body `--ink` (AP11 safety net). (5) Upgrade the footer legal row from the alpha-0.45 `--on-dark-3` (fails AA) to alpha-0.72 `--on-dark-2` for AA compliance (CS-FOOT-02 legibility). |
| `apps/catalog/theme_safety.py` | New module (archetype-scoped). Implements the WCAG relative-luminance + contrast-ratio math, a `is_primary_safe_on_cream` gate keyed to the CS-PAL-01 thresholds (L\* ≤ 40 via luminance ≤ 0.12 + AAA 7:1 contrast vs cream paper), and an `enrich_corporate_suite_theme` function that threads derived safety tokens (`on_primary`, `primary_is_safe`, `primary_contrast`, `accent_on_primary_contrast`) into the theme dict and emits a `UserWarning` when the primary fails the gate. Intentionally lenient (warn, never raise) because it runs inside the live-preview request path. |
| `apps/catalog/views.py` | Wire the safety helper into `LiveTemplateView.get_context_data` after `apply_project_overrides`, gated on the archetype being `corporate-suite` (via `theme_safety.should_enrich`). No-op for every non-corporate-suite archetype. Zero behaviour change for templates that pass the gate; the warning surfaces during authoring + in the test suite. |
| `apps/catalog/tests.py` | New `CorporateSuiteThemeSafetyTests` block (7 focused unit tests). Covers: WCAG math invariants (luminance monotonic, contrast symmetric and bounded at 21:1), positive gate for Pragma + Fiscus, negative gate against the Solaria Commit A bug palette (`#F7F3EC`), enrichment no-ops for passing palettes, `UserWarning` emitted for failing palettes, archetype scoping for `should_enrich`, and the "never raise on invalid hex" contract. Nearby patterns used: module-level test classes with `TestCase`, no DB state. |

### What was hardened

1. **Palette-safety guardrails (CS-PAL-01 server-side layer)** — a WCAG
   luminance + AAA-contrast gate runs every corporate-suite render and
   emits a `UserWarning` whenever a primary exceeds `L ≈ 0.12` or falls
   below 7:1 vs cream paper. All three currently enrolled palettes pass
   (Pragma 12.81:1, Fiscus 12.86:1, Solaria post-fix 12.56:1) and the
   Solaria Commit A bug palette (`#F7F3EC`, 1.01:1) fails loudly. This
   layer is complementary to — not a replacement for — the Contrast
   Auditor agent + live browser walk that the standards define as the
   authoritative gate. It catches regressions before the walk even
   starts, without ever 500-ing the page for a legacy palette.

2. **`--on-primary` safety rail** — the archetype now has a canonical
   foreground token for every element painted on `var(--primary)`. The
   helper defaults it to cream (`#F7F4EC`) regardless of whether the
   primary passes the gate, so inverted surfaces remain *renderable*
   even in the presence of a bad palette. New dark-surface child
   elements should reach for `--on-primary` / `--on-primary-soft` rather
   than a hardcoded `#fff`.

3. **Safer accent usage on navbar** — the `.cs-nav .links a.is-current`
   active state no longer swaps link text to the accent hue (which fails
   CS-NAV-02 and collapses to borderline AA on warm-gold / caramel
   accents). The state is now signalled by an accent underline dot while
   the text stays at `--on-dark`, preserving the four-state cascade
   (default / hover / focus / active) independently of the accent
   lightness.

4. **Dark-surface descendant cascade (AP11 prevention)** — any new
   `<p>`, `<li>`, `<dt>`, `<dd>`, `<small>`, `<time>` added to
   `.cs-section.dark`, `.cs-kpi-band`, `.cs-cta`, `.cs-foot` inherits
   `--on-primary-soft` by default. Existing explicit rules in `home.html`
   and sibling page files retain priority; this is purely a safety net
   against the "forgot to declare color, defaulted to `var(--ink)`"
   failure mode that silently paints dark-on-dark.

5. **Footer legal-row contrast (CS-FOOT-02 legibility)** — the
   `.cs-foot .bot` copyright / P.IVA / privacy strip moved from
   `--on-dark-3` (alpha 0.45, composited ≈ 2.8:1 on a navy primary —
   fails AA for body text even at the tracked-uppercase target) to
   `--on-dark-2` (alpha 0.72, AA-safe). Hover remains `var(--accent)`.

6. **AP7 dead-code retirement** — the archetype-wide hardcoded
   `--primary-2: #2c3e6b;` navy (0 consumers per the audit grep) is
   removed. A comment at the declaration block preserves the rationale
   and explicitly forbids a fourth brand color, matching CS-PAL-03.

7. **Tightened semantic for the `--on-dark-*` family** — a comment
   block at the `:root` declaration documents that `--on-dark-3`
   (alpha 0.45) is for *decoration only* (rules, dividers, legend
   dots), never body copy. This locks down a class of quiet regressions
   where authors use `--on-dark-3` for "subtle label" text that then
   fails AA in production.

### What risks remain (for later Step 1 sub-steps and the browser walk)

- **Responsive breakpoints (AP2)** are untouched in Step 1A by design.
  `_base.html` still has zero real `@media` blocks; the hero does not
  stack on 720 px, the nav does not collapse at 1100 px, and the footer
  does not reflow. The `factory/reports/hardening/step1-core-hardening.md`
  Step 1B section will own that diff.

- **AP12 `prefers-reduced-motion` coverage** for the 45 `[data-lm]`
  hooks across 6 pages is still only honored for the corporate button
  transitions. The JS-side audit belongs to Step 1C.

- **`--on-dark-3` for KPI stat labels** (`home.html:121`) is preserved
  for now. The small tracked-uppercase label on a dark navy sits at
  ~3:1 — borderline for CS-FOOT-02-class rules but arguably in the
  "decorative tier" the tightened semantic now permits. Flagged for the
  browser walk to verify on the three live palettes.

- **Accent-on-dark contrast floor** is reported (`accent_on_primary_contrast`)
  but not gated. Pragma's emerald (`#10B981`) on navy scores 5.77:1
  (AA large, AAA no). Fiscus's warm gold (`#B58F4A`) on ink is tighter.
  The helper exposes the number so a future step can add an AA floor;
  doing so now would risk false positives on palettes that only use the
  accent as punctuation (CS-PAL-05).

- **Pragma legacy imagery (AP3)** is a separate hardening track;
  Step 1A does not touch `preview_imagery.py`.

- **Pre-commit / CI palette gate** is still pending. The live-render
  layer emits a `UserWarning`; promoting that to a build-time failure
  (e.g., a `ruff` rule or a dedicated management command run in CI)
  belongs to the validator step.

- **Solaria Commit B remains paused.** Step 1A closes a precondition
  but not all of them.

### What still requires browser verification

Per `factory/standards/corporate-suite-browser-rubric.md` §5/§7, the
following must be walked in a browser before any of the three LIVE
templates (Pragma, Fiscus) flip or re-flip on the hardened skin:

1. **Navbar active state at 1920/1440/1280** — the new accent-underline
   dot must be visually obvious on both Pragma (emerald underline on
   navy) and Fiscus (warm-gold underline on ink). Screenshot each
   locale-×-viewport cell into `factory/reports/browser-verification/<slug>/<run>/nav-active.png`.

2. **Dark-surface descendant cascade on home KPI + CTA band** — inject a
   throwaway `<p>Test copy</p>` inside `.cs-kpi-band` via DevTools and
   confirm the computed `color` resolves to the `--on-primary-soft`
   token, not `#0f172a`. Repeat inside `.cs-cta`.

3. **Footer legal row legibility** — DevTools contrast pane on
   `.cs-foot .bot` text must now read ≥ 4.5 on both enrolled palettes.

4. **AAA hero h1 on cream paper** — the primary-safety helper says
   Pragma 12.81:1, Fiscus 12.86:1. Confirm the DevTools contrast pane
   agrees on `.cs-lead h1` + `.cs-hero .left h1`.

5. **Focus-visible gold outline** — keyboard-tab through the navbar and
   the primary CTA on each of the three live locales; the outline must
   still appear under the new active-underline state without visual
   conflict.

6. **Legacy palette warning surfaces** — run `python manage.py test apps.catalog.tests.CorporateSuiteThemeSafetyTests` and inspect the
   captured `UserWarning` to ensure the CS-PAL-01 message is emitted
   with the offending slug.

These are the 6 DOM checks that the browser rubric considered
CLI-invisible under Step 0. Step 1A now reduces checks (2) and (3) to
PASS-by-construction on the three enrolled palettes, but the walk is
still the veto per CS-BROWSER-01 / AP8.

---

## Changed-files summary

```
M templates/live_templates/business/corporate-suite/_base.html
A apps/catalog/theme_safety.py
M apps/catalog/views.py
M apps/catalog/tests.py
M factory/reports/hardening/step1-core-hardening.md
```

- `_base.html` hardening is five targeted edits inside the existing
  `:root` + `.cs-nav` + `.cs-section.dark` + `.cs-foot .bot` cascades.
  No new selectors outside the archetype scope, no structural layout
  changes, no markup changes.
- `apps/catalog/theme_safety.py` is ~180 lines of pure-function color
  math + archetype-gated enrichment. No Django dependency; importable
  standalone for factory tooling (CI, scorecards, auditor agents).
- `apps/catalog/views.py` adds 3 lines of wire-up inside the existing
  `get_context_data` hook, guarded by `should_enrich(...)` so every
  non-corporate-suite render is untouched.
- `apps/catalog/tests.py` appends a single new `TestCase` class at the
  tail of the file — follows the nearby "module-level TestCase, no DB
  state" pattern used by `SeedVisualStylesCommandTests` and friends.
- The hardening report itself lands in the factory tree next to the
  audit master.

### Why the changes are archetype-level, not template-local

Every one of these edits lives in code that Pragma, Fiscus, and Solaria
(paused) share — `templates/live_templates/business/corporate-suite/_base.html`
is the single CSS surface all three templates extend, and
`apps/catalog/views.py` is the single view that renders every
corporate-suite live URL regardless of slug. The Python helper is keyed
on `archetype == "corporate-suite"`, which is a DNA-level property
(`template_dna.py`), not a template-level property.

As a result:

- A regression that re-introduces a cream primary on a future fourth
  corporate-suite template would fail the same CS-PAL-01 gate without
  the author needing to wire anything in.
- The `--on-primary` token, the navbar active-underline, the
  dark-surface descendant cascade, and the footer legal-row upgrade all
  apply to every page file (`home.html`, `about.html`, `services.html`,
  `case_study_list.html`, `case_study_detail.html`, `contact.html`)
  because they inherit the `_base.html` `<style>` block.
- No template-local `home.html`-style fix could have closed AP11 at the
  archetype level; the descendant cascade in `_base.html` is the only
  place that catches every *future* dark-surface child across the skin.
- The alternative — copy-pasting the same safety rules into each of
  Pragma's, Fiscus's, and Solaria's (future) skins — is exactly the
  anti-pattern AP10 (palette differentiation drift) shows up as on the
  copy side. Keeping the safety rails at the archetype level keeps the
  contract identical across siblings and honors D-054's "siblings
  differentiate on palette + imagery + copy, never on safety
  infrastructure".

Step 1B (responsive breakpoints) and Step 1C (`prefers-reduced-motion`
JS audit) are queued; both will similarly land at the archetype level
for the same reason.
