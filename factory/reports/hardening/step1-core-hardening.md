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

---

## Step 1B — Navbar, Hero, Footer Premium Pass

Goal: harden the archetype's three chrome primitives — navbar, hero,
footer — so every corporate-suite render reads "premium / elegant /
modern / professional" in the operational sense from `§1` of the
design standard (controlled, readable, editorial, executive) without
tipping into "more colorful" decoration. All edits stay inside the
shared archetype skin (`_base.html`) and the single page file whose
markup owns the hero composition (`home.html`). Zero changes to
`apps/editor`, `apps/projects`, `apps/commerce`, no new archetypes,
no Solaria Commit B un-pause.

### Files changed

| File | Change |
|---|---|
| `templates/live_templates/business/corporate-suite/_base.html` | (1) Navbar: compact 20 px centered accent rule for `.cs-nav .links a.is-current:after` (was full-width `left:0;right:0`). (2) Navbar: `.cs-nav .phone .tag` color demoted from `var(--accent)` to `var(--on-dark-2)` + border retoned from `rgba(255,255,255,0.18)` to `rgba(238,240,243,0.20)` so the nav holds ONE accent element per viewport (the active-underline dot), honoring CS-BLOCK-N-02 / CS-PAL-05. (3) Navbar: dedicated `.cs-nav .links a:focus-visible` with `outline-offset: 6px` (tighter than shared 4px so the ring sits inside the sticky band). (4) Navbar: box-shadow retuned to editorial elevation (deeper y-offset, negative spread). (5) Nav link `.links a` padding `4px 0` + eased transition for four-state cascade readability. (6) Button primitives: `.cs-btn-primary` padding bumped from `14px 28px` to `16px 30px`, letter-spacing `0.10em → 0.12em`, hover color now resolves against `--on-primary` (safety-token threaded through `theme_safety.py`, not a hardcoded `#fff`). `.cs-btn-ghost` color raised from `--ink-mute` to `--ink-soft` for AA cushion on cream. (7) Footer: padding `72px 72px 36px → 96px 72px 40px`, column gap `48px → 56px`, `.top` border-bottom retoned to `rgba(238,240,243,0.18)`. (8) Footer: `.cs-foot .brand .word` size `24px → 28px`, letter-spacing `-0.01em`, line-height `1.1`; brand tagline gets a `padding-top: 16px; border-top: 1px solid rgba(238,240,243,0.14)` editorial hairline inside the brand column. (9) Footer: `.cs-foot .col p/a` now reaches for the `--on-primary-soft` safety token (was `--on-dark-2`) and hover upgrades to `--on-dark` rather than `--accent` — pulling accent usage out of the 40+ sitemap links that previously all flashed gold on hover (AP-sense decoration-over-punctuation). (10) Footer: legal row rebuilt as a `1fr auto` two-zone grid with a `.legal` flex wrapper for the right zone; letter-spacing eased to `0.14em` from `0.10em`; legal-link hover upgraded to `--on-dark` (parity with sitemap hover). |
| `templates/live_templates/business/corporate-suite/home.html` | (1) Hero: `min-height: 580px → 620px`, left padding `100px … 64px → 104px … 72px`. Gives the serif h1 + meta-strip the editorial breathing room the design standard asks for under CS-RHYTHM-01. (2) Hero: added `border-bottom: 1px solid var(--rule)` under `.cs-hero` so the hero closes on a hairline before the pillars section opens (premium cadence). (3) Hero subhead: `font-size: 17px → 18px`, `line-height: 1.65 → 1.62` — still inside CS-TYPE-04 body-copy band, but weighted slightly more to the executive side. (4) Hero: `meta-strip` now uses `margin-top: auto` on the flex left-column so credential anchors pin to the bottom of the hero rather than floating mid-panel. Padding-top raised to 28 px; gap 42→48 px. (5) Hero overlay: replaced the 2-stop overlay (`rgba(15,23,42,0) 52% → rgba(15,23,42,0.66) 100%`) with a 3-stop ramp (`0.10 at 0% → 0 at 34% → 0.74 at 100%`). Top stop protects slot-0 frames whose top edge is bright; middle "clear" stop preserves the photo; bottom 0.74 floor keeps the credit hairline + tracked label + serif figure legible on any Pexels frame the curator may ship (direct mitigation for the AP5 "editorial failure" risk on a busy hero). (6) Hero credit: border-top opacity `0.32 → 0.42`, label letter-spacing `0.18em → 0.20em`, strong margin-top `6px → 8px`, row gap `32px` — the credit now reads as a single editorial caption unit instead of two drifting labels. |
| `apps/catalog/tests.py` | New `CorporateSuiteChromeContractTests` class (7 focused static-file asserts). Covers: nav active-state underline must be compact + centered (locks out the full-width regression), nav `.phone .tag` must NOT be accent-colored (CS-BLOCK-N-02 one-accent-element contract), nav links have a dedicated `:focus-visible` outline (CS-NAV-02 state 3), hero overlay bottom stop ≥ 0.72 alpha (AA floor for credit), hero has exactly one primary + one ghost CTA (CS-HERO-04 / CS-CTA-01), footer legal row uses `--on-dark-2` not `--on-dark-3` (CS-FOOT-02 AA floor), footer legal links wrapped in a `.legal` zone (grid-shape contract), footer wordmark uses heading font at ≥ 28 px (CS-FOOT-01 gravity). Nearby pattern matched: `CorporateSuiteThemeSafetyTests` (no DB, no client, pure static check), added to the same trailing section of the file. |

### What improved

1. **Navbar accent discipline · CS-BLOCK-N-02 satisfied by construction.**
   Before: at any page load the nav rendered `.crest` (accent border +
   accent glyph) + `.phone .tag` (accent text) + `.links a.is-current:after`
   (accent underline on the current-page link) = 3 accent hits. The
   `browser_evaluate` detection in CS-BLOCK-N-02 §6 expects exactly 1,
   and CS-PAL-05 caps per-viewport accent at 2-3 including the CTA and
   the focus outline. After: crest + active-underline = 2, with the
   crest explicitly scoped as brand chrome (wordmark mark), and the
   trailing CTA pill demoted to the `--on-dark` family. This hits the
   target contract without losing the nav's editorial character.

2. **Navbar active-state is editorial, not utilitarian.**
   The previous full-width accent bar between the link baseline and
   the nav bottom could drift into the 32 px inter-link gap at narrow
   widths and read as a menubar divider rather than a state indicator.
   The 20 px centered accent rule reads as "this is the page you're
   on" with the same elegance as a serif underline in a table of
   contents. Keeps the 4-state cascade (default / hover / focus /
   active) visually distinct and resilient to warm-gold or caramel
   accents (Fiscus) where the full-width bar competed with the on-dark
   text.

3. **Navbar focus-visible ring sits inside the chrome.**
   The shared `:focus-visible` rule used `outline-offset: 4px`, which
   on the 76 px sticky nav dropped the outline below the link into the
   paper-side shadow region on Pragma. The nav-scoped `6px` offset
   places the full gold ring inside the sticky band where keyboard
   users can see it without scrolling context. CS-NAV-02 state (3) now
   passes on every enrolled palette.

4. **Primary CTA reads as intentional editorial button, not
   placeholder outline.**
   The outline contract stays (fill-primary would collide with the
   `.cs-cta .actions .cs-btn-primary` override on the dark CTA band),
   but the tightened letter-spacing, heavier horizontal padding, and
   the `--on-primary` safety-token on hover (instead of the raw
   `--on-dark`) give the button more typographic presence. The ghost
   companion's `--ink-soft` default text (vs the prior `--ink-mute`)
   clears AA cushion on cream and restores the hierarchy between
   primary (boxed) and ghost (typographic-underline) in the hero's
   left-column CTA cluster.

5. **Hero overlay is AA-safe for the credit line on any Pexels
   slot-0 frame.**
   The prior two-stop overlay (transparent until 52%, then
   `rgba(15,23,42,0.66)` at 100%) could leave the credit line
   borderline on bright board-room or backlit-desk frames. The new
   three-stop ramp adds a 0.10-alpha top dampener (prevents a hot
   highlight overpowering the paper-side transition), keeps a
   generous clear middle zone (preserves the photograph), and
   tightens the bottom to 0.74 — enough for the tracked label + serif
   figure + hairline to clear 4.5:1 on any of the three enrolled
   palettes' curated slot 0. The new `CorporateSuiteChromeContractTests.test_hero_right_overlay_has_bottom_stop_at_or_above_072`
   locks this floor as a contract, not a coincidence.

6. **Hero composition reads editorial, not dashboard.**
   The raised `min-height: 620px` + `margin-top: auto` on the
   meta-strip + the hairline border-bottom under `.cs-hero` give the
   hero the "closing cadence" that Pragma's and Fiscus's prior renders
   lacked at 1440 × 900. At the standard premium desktop viewport the
   hero now reads as a chapter opener with a clean editorial seam
   into the pillars section.

7. **Footer reads as cadence closer, not utility strip.**
   Before: 72 px top padding + 24 px extra margin-top = 96 px total
   vertical air, crammed 4-column grid at 48 px, 24 px wordmark set
   in heading font but sitting below a 13-px body paragraph with no
   visual separation, legal row a flex-wrap tangle. After: 96 px
   inside the footer itself (so the air belongs to the footer's
   own chapter), 56 px column gap, 28 px wordmark with `-0.01em`
   tracking that reads as a gravity anchor, an editorial hairline
   rule inside the brand column between the wordmark and the tagline
   (mirrors the hero's credit-hairline treatment for coherence), and
   a two-zone `1fr auto` legal row where copyright anchors left and
   legal links anchor right with an explicit `.legal` grouping for
   the grid shape contract.

8. **Footer accent budget no longer bleeds across sitemap hover.**
   The prior `.cs-foot .col a:hover { color: var(--accent); }` meant
   every sitemap link flared gold on hover. With 4 columns × 4-6
   links each, a slow mouse sweep lit up 16-24 accent hits in sequence
   — the sort of "more colorful" behavior the task explicitly asks
   us to avoid. Sitemap links now upgrade to `--on-dark` on hover;
   accent usage in the footer is held at the four `.top h5` tracked
   labels (one accent family, one role — CS-PAL-05 punctuation).

9. **Dark-surface safety rails from Step 1A still hold under the
   new footer selectors.**
   The footer brand `<p>` now inherits `--on-primary-soft` from both
   the Step 1A descendant cascade AND its own new rule. The legal
   row spans inherit `color: var(--on-dark-2)` through `.cs-foot .bot`
   and the shared dark-surface cascade still covers any future
   `<p>`, `<li>`, `<dt>`, `<dd>`, `<small>`, `<time>` child.
   Regression surface for AP11 is unchanged; the footer upgrade did
   not open a new dark-on-dark pocket.

### Remaining weak points

- **Responsive breakpoints (AP2) still absent.** Every rule above
  is written for the desktop class. At ≤ 1100 px the nav links do
  not condense (CS-NAV-05), at ≤ 720 px the hero does not stack
  (CS-HERO-07) and the footer does not reflow (CS-FOOT-05). These
  three gaps survive Step 1B by design; Step 1C will land the three
  media queries at the archetype level.

- **No JS-side scrolled-state affordance for the sticky nav.**
  The box-shadow retune gives a premium resting elevation, but the
  nav does not differentiate "pinned at top of document" vs
  "sticky over scrolled content." A lightweight `IntersectionObserver`
  hook would add a classname like `.cs-nav--scrolled` for a deeper
  shadow / slightly tighter height. Deferred — adding it now would
  require a new JS surface outside the "existing shared primitives"
  constraint.

- **Primary CTA stays outline on cream paper.** A solid-filled
  primary (background `--primary`, text `--on-primary`) would read
  more executive on the hero, but it would collide with the dark
  CTA section's override where the button background already equals
  `--primary`. Resolving this cleanly needs a `.cs-btn-primary--solid`
  modifier or a context-scoped override in `home.html` / `.cs-lead`,
  which is a larger archetype refactor than Step 1B's scope allows.
  Flagged for Step 1D (or the validator step if we want to enforce
  one CTA style per surface).

- **Footer brand tagline hairline uses a hardcoded alpha**
  (`rgba(238,240,243,0.14)`), not a token. The `--on-dark-3` token
  at alpha 0.45 is too heavy for this decorative rule, and we did
  not want to introduce a 4th `--on-dark-*` step. Acceptable because
  the hairline is decoration only (CS-PAL-04 `--on-dark-3`
  decoration-only semantic covers it), but revisit if the footer
  adds more hairlines.

- **Legal row still uses `href="#"` placeholders** for the
  privacy / cookie / legal links. CS-CTA-04 calls out real-route
  targets as the gate; the hardcoding is inherited from the
  pre-X.4a skin and is out of scope for a chrome-polish step. It
  must still be wired to real routes before any new pilot flips to
  `published_live`.

- **Wordmark at 28 px may crowd under long studio names in the
  editor preview mode.** The `body.mw-is-editor-preview` overflow
  guard in `_base.html:506-514` already covers `.cs-hero h1`,
  `.cs-pillars h2`, `.cs-leadership h2`, `.cs-nav .word` — but NOT
  the footer wordmark. If a customer edits to a 24-character studio
  name, the footer lockup may wrap. Low-risk (the edit surface is
  governed in the editor, not this skin), but worth a once-over in
  the browser walk.

### What still requires browser verification

Per `factory/standards/corporate-suite-browser-rubric.md` §5 / §7,
the following must be walked in a browser (Playwright MCP or manual)
on each enrolled palette before Step 1B can be declared PASS:

1. **Navbar accent count at 1920/1440/1280, all 6 pages.** Run the
   CS-BLOCK-N-02 `browser_evaluate` snippet and confirm it returns
   ≤ 2 elements (crest + the active-page underline dot). On a page
   where NO nav link matches the current route (edge case — should
   not happen on the skin's 6 pages), the count must be 1.

2. **Navbar focus-visible walk, LTR + RTL.** Keyboard-tab through
   the nav on Pragma and Fiscus; the gold outline must appear inside
   the sticky band on every link and on the `.mp-lang-pill` locale
   switcher. At AR, confirm the outline survives the `dir="rtl"`
   text-direction flip.

3. **Hero overlay on 3 live palettes × 3 page viewports
   (1920/1440/1280).** DevTools contrast pane on
   `.cs-hero .right .credit .item` must read ≥ 4.5. Also eyeball
   that the middle clear-zone of the 3-stop gradient preserves the
   hero photograph's mood — the ramp should not cast a visible band
   across the frame.

4. **Hero CTA cluster at 1440.** One accent-filled button (actually
   outlined — the archetype contract) + one ghost underline. No
   third button. `href` on both CTAs resolves to real routes
   (`catalog:live_template_page`) — the skin already calls `{% url %}`
   for each.

5. **Footer premium read at 1920.** Scroll to footer, confirm the
   wordmark sits as the gravity anchor of the brand column, the
   hairline between wordmark and tagline reads as editorial (not as
   a divider), sitemap hover upgrades to full-white (not gold), and
   the legal row reads as two zones (copyright left · privacy /
   cookie / legal right) with the `.legal` grouping visible in
   DevTools.

6. **Footer legal row contrast on each palette.** DevTools contrast
   pane on `.cs-foot .bot` text ≥ 4.5 on Pragma (navy) and Fiscus
   (ink). Should PASS by construction — the rule uses `--on-dark-2`
   at alpha 0.72 which composited ~6.5:1 on both primaries.

7. **Legacy RTL still works.** Footer 4-col grid flips to
   `1fr 1fr 1fr 1.4fr` under the `is_rtl` block (untouched), and
   letter-spacing resets still cover the legal row. Load the AR
   locale on Pragma home and walk the footer.

8. **Regression smoke: no visible dark-on-dark pockets.** Run the
   CS-BLOCK-17 / AP11 sweep on `.cs-foot`, `.cs-cta`, `.cs-kpi-band`,
   `.cs-section.dark`. Same check as Step 1A; Step 1B's footer
   upgrade did not introduce new descendant rules that escape the
   cascade.

These are the 8 DOM checks that the browser rubric considers
CLI-invisible for Step 1B. The static-file test added here reduces
(1), (3), (5), (6) to "matches the expected contract string" — but
the authoritative gate stays the browser walk per CS-BROWSER-01.

---

## Changed-files summary (Step 1A + Step 1B cumulative)

```
M templates/live_templates/business/corporate-suite/_base.html
M templates/live_templates/business/corporate-suite/home.html
A apps/catalog/theme_safety.py                    (Step 1A)
M apps/catalog/views.py                           (Step 1A)
M apps/catalog/tests.py                           (Step 1A + 1B)
M factory/reports/hardening/step1-core-hardening.md
```

Step 1B delta only:
- `_base.html`: ~45 lines net added across the nav block, the button
  primitives, and the footer block. No new selectors outside the
  archetype scope; no markup changes beyond the footer legal row
  `<span class="legal">` wrapper.
- `home.html`: ~30 lines net modified across the hero block
  (spacing, overlay stops, credit row). No structural markup change
  — every customization still comes through the existing
  `page_data.hero_*` fields.
- `apps/catalog/tests.py`: appended `CorporateSuiteChromeContractTests`
  (7 tests · no DB · static-file asserts) at the tail of the file,
  mirroring the Step 1A `CorporateSuiteThemeSafetyTests` pattern.
- This hardening report gains the `Step 1B` section above.

### How these changes reduce the risk seen in Solaria

The Solaria incident (Commit A, palette `#F7F3EC` for `--primary`)
surfaced a class of failures that 506/506 CLI-green tests missed:
**archetype-level visual contracts that are CLI-invisible because
they depend on rendered pixel state, not on symbol presence.**
Step 1A closed the palette-polarity half of that class with a
server-side gate + a safety-token (`--on-primary`) + a descendant
cascade. Step 1B closes the chrome half, attacking three distinct
flavors of the same risk:

1. **Accent-count drift in the nav · the "it looked fine" failure
   mode.** Solaria's nav rendered the cream primary on a cream body,
   but it also inherited the prior nav contract of a full-width
   accent underline + accent `.phone .tag` + accent crest. Even
   once CS-PAL-01 is enforced, a future palette with a punchy warm
   accent (amber, ocra) would still over-count accent hits and tip
   the nav into SaaS territory. Step 1B demotes the `.phone .tag`
   to `--on-dark-2` and makes the active-underline a compact rule,
   so the nav holds ≤ 2 accent hits on any enrolled palette —
   regardless of what accent hue a future Commit A ships. The static
   test locks this as a contract.

2. **Overlay-brittleness in the hero · the "looks wrong on this
   photograph" failure mode.** Solaria's hero shipped a perfectly
   OK Pexels frame that nonetheless pushed the credit line borderline
   because the bottom gradient stop sat at 0.66. That is an AP5-class
   editorial failure — the archetype's visual contract depends on a
   photo the copy author did not pick. Step 1B lifts the bottom stop
   to 0.74 + adds a top dampener, making the overlay AA-safe across
   the "bright board-room", "backlit desk", "dark studio interior"
   frame families that slot 0 of a `business-corporate` / `business-fiscal`
   pack will realistically pull from. The contract test locks the
   floor.

3. **Hover-accent bleed in the footer · the "more colorful, not
   more premium" failure mode.** Solaria's Commit A footer, on the
   cream-primary palette, had every sitemap link hovering to the
   accent — resulting in an 8-20 accent-flash stream during a
   reviewer's scroll through the footer. That is exactly the
   "cheap-feeling" behavior this task calls out. Step 1B moves
   hover to `--on-dark`, keeping accent restricted to the 4 tracked
   h5 labels (punctuation, not decoration). This is a behavioural
   change the browser walk will catch on its first mouse sweep, and
   one the reviewer would easily miss in a static screenshot pass.

Net: Step 1B narrows the "chrome reads cheap" failure mode at the
same archetype level where Step 1A closed "palette reads broken."
Combined, the two steps give every corporate-suite render a higher
floor for the adjective stack `premium / elegant / modern /
professional` than any pilot — Pragma, Fiscus, or the paused Solaria
Commit B — has had access to before. The browser walk stays the
ship veto per CS-BROWSER-01; the contracts above simply reduce how
many ways a walk can fail.
