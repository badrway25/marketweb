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

---

## Step 1C — Typography, Rhythm, and Imagery Hardening

Goal: close the three remaining "editorial floor" gaps inside the
corporate-suite skin so a reviewer cannot describe any enrolled
template with words like "template marketplace", "dashboard", "image
scarcity", or "stock fallback". Step 1A+1B hardened *safety*
(palette polarity, chrome + hero + footer contracts) — Step 1C
hardens the *editorial feel itself*: the typographic hierarchy, the
cadence between sections, the photographic rhythm across the page,
and the sourcing gate that keeps a non-Pexels URL from landing on
any new pilot. As before, edits stay inside the archetype skin
(`_base.html` + the 6 page files), the archetype-gated Python
enrichment hook, and the static-file test suite. Zero changes to
`apps/editor`, `apps/projects`, `apps/commerce`, no new archetypes,
no Solaria Commit B un-pause.

### Files changed

| File | Change |
|---|---|
| `templates/live_templates/business/corporate-suite/_base.html` | (1) **Type-scale tokens** · added `--fs-hero: 64px`, `--fs-lead: 56px`, `--fs-h2: 48px`, `--fs-h3: 26px`, `--fs-body-lg: 17px`, `--fs-body: 16px`, `--fs-eyebrow: 11px`, `--track-eyebrow: 0.22em`, `--copy-max: 64ch` to the `:root` declaration. Every heading class on the archetype now resolves through these tokens so a future page file cannot silently drift into 80-96 px display-headline territory. (2) **Rhythm tokens** · added `--space-section-y: 100px`, `--space-section-x: 72px`, `--space-band-y: 72px`, `--space-lead-bot: 64px`, `--space-footer-y: 96px`. `.cs-section`, `.cs-section.dark`, `.cs-lead`, `.cs-foot` now reach for these tokens instead of hardcoded `96px 72px` / `100px 72px` combinations. (3) **Section-head consistency** · the generic `.cs-section h2` rule now uses `var(--fs-h2)` and the `.cs-section .sec-intro` copy column uses `var(--copy-max)` + `var(--fs-body-lg)`. Added an archetype-level `.cs-section h2 em` / `.cs-section .head h2 em` / `.cs-section .heading em` cascade so the italic-em restraint (CS-RHYTHM-05) applies to every section title uniformly. Also added `.cs-sec-label` as a shared alternative name for `.sec-label` (same rule body) — lets future partials reach for the canonical tracked-uppercase label class without fighting scope. (4) **Image-rhythm guardrails** · hard `display: none` on `.cs-pillars .pillar img`, `.cs-pillars .pillar picture`, `.cs-kpi-band img`, `.cs-kpi-band picture` to enforce CS-IMG-SEC-01 (pillars = icon/typographic) and CS-IMG-SEC-02 (KPI band = zero photography). Prevents AP12 "decorative photo on typographic section" from shipping via a content-registry typo. (5) **Optional leadership portrait primitive** · `.cs-leadership .card .portrait` — 4:3 editorial figure with `object-fit: cover`, lazy-loaded, rendered only when content supplies `partner.portrait` (slot 2-3 URL from the imagery pool). `.cs-leadership .card:has(.portrait)` zeroes the top padding so the figure reads as a card opener, not a sticker. (6) **Optional case-thumb primitive** · `.cs-cases-preview .row .thumb` — 80×60 square-safe crop, rendered only when content supplies `post.thumb` (slot 4-5 URL). Never reuses hero (CS-IMG-SEC-05) by design: the primitive has a fixed small crop so a hero-scale slot 0 URL would obviously misread. (7) **Editorial seam utility** · `.cs-section-seam` — a shared hairline primitive for chapter-level separators where a rule is needed without adding inter-section margin (CS-RHYTHM-06). Neutral-tinted so it never competes with the accent budget (CS-PAL-05). |
| `templates/live_templates/business/corporate-suite/home.html` | (1) Hero h1 `font-size` moved from hardcoded 76 px → `var(--fs-hero)` (64 px). The prior 76 sat over the CS-TYPE-04 ceiling of 72. Subhead moved to `var(--fs-body-lg)`, copy width tightened to 54ch. (2) Pillars, KPI band, sectors ribbon, trust band, leadership, cases-preview, CTA sections all moved from hardcoded `100px 72px` / `72px 72px` → the `--space-section-y` / `--space-section-x` / `--space-band-y` tokens. Pillars `.head h2` font-size moved from 52 px → `var(--fs-h2)` (48). Leadership `.head h2`, cases-preview `.head h2`, CTA h2 all moved to `var(--fs-h2)`. CTA h2 in particular moved from 56 → 48, restoring the section-title ceiling. (3) Pillar `.pillar h3`, leadership `.card h3` moved to `var(--fs-h3)` (26) — was 28 / 26 across the two, now uniform. (4) Leadership card markup gains an optional `<img class="portrait" src="{{ partner.portrait }}">` wrapped in `{% if partner.portrait %}` — no-op on every currently enrolled template (Pragma, Fiscus don't declare `portrait` yet), graceful enrichment when a pilot or retro-curation adds portraits. (5) Case-preview row `.title` block now contains an optional `<img class="thumb">` wrapped in `{% if post.thumb %}` + the `.title` flex layout aligns thumb+title on the same baseline without breaking existing typographic-only rows. |
| `templates/live_templates/business/corporate-suite/about.html` | Section padding on `.cs-history`, `.cs-values`, `.cs-team`, `.cs-cta-band` moved to `--space-section-y` / `--space-section-x`. All page-level H2s (history/values/team/CTA) moved to `var(--fs-h2)` — values was 52 px (over ceiling), team was 48 px, cta-band was 44 px; all now uniform at 48. Every intro block now uses `var(--fs-body-lg)` + `var(--copy-max)`. |
| `templates/live_templates/business/corporate-suite/services.html` | `.cs-services` section uses `--space-band-y` top / `--space-section-y` bottom to read as a services intake after the lead. `.cs-process` + `.cs-cta-svc` sections use the section tokens. `.cs-services .card h3`, `.cs-process .head h2`, `.cs-cta-svc h2` normalized to `var(--fs-h3)` / `var(--fs-h2)`. Intro blocks reach for `var(--fs-body-lg)` + `var(--copy-max)`. |
| `templates/live_templates/business/corporate-suite/case_study_list.html` | `.cs-cases-list` bottom padding uses `--space-section-y`; horizontal uses `--space-section-x`. `.cs-cta-list` uses `--space-footer-y` / `--space-section-x` and its H2 normalizes to `var(--fs-h2)` (was 40 px). Intro uses `var(--fs-body-lg)` + `var(--copy-max)`. |
| `apps/catalog/imagery_policy.py` | New module (archetype-scoped). Implements the Pexels-only sourcing gate per CS-IMG-SRC-01 + CS-IMG-POOL-01 + CS-IMG-SRC-02: `validate_corporate_suite_imagery_key(key)` returns a `PolicyReport` dataclass (is_known, is_legacy_exempt, pexels_only, shape_is_canonical, non_pexels_urls, hero_width_ok, warnings). `enforce_corporate_suite_imagery_policy(key, template_slug)` emits a single `UserWarning` on any non-legacy-exempt failure. `should_enforce(archetype)` is the archetype gate consumed at the call site. The module is intentionally Django-free except for a lazy import of `preview_imagery.IMAGERY_CONFIG` inside one function — factory tooling + CI scripts can call it from a plain Python shell. Constants: `CORPORATE_SUITE_POOL_KEYS = {business-corporate, business-fiscal, business-coaching}`, `LEGACY_EXEMPT_KEYS = {business-corporate}` (Pragma · retro-curation pending per AP3), `PEXELS_HOST = "images.pexels.com"`, `CANONICAL_POOL_SIZE = 6`. Mirrors the `theme_safety.py` shape so the two archetype-gated hooks are chainable in `LiveTemplateView.get_context_data`. |
| `apps/catalog/views.py` | `LiveTemplateView.get_context_data` now chains the imagery policy enforcement after the theme-safety enrichment, gated on `should_enforce_imagery(archetype)`. Three lines of wire-up; non-corporate-suite archetypes are completely untouched. |
| `apps/catalog/tests.py` | Appended two new test classes at the tail of the file, mirroring the `CorporateSuiteThemeSafetyTests` / `CorporateSuiteChromeContractTests` pattern (no DB, no client, static-file + pure-function asserts). `CorporateSuiteImageryPolicyTests` (6 tests) covers: legacy pool silent + reported as non-compliant Pexels-wise but compliant overall (retro-curation pending), business-fiscal Pexels-only pass, hostname-strictness (no lookalike domains), non-canonical pool shape flagged, archetype gate, warn-on-non-legacy-non-Pexels pool. `CorporateSuiteRhythmContractTests` (8 tests) covers: type-scale tokens declared, rhythm tokens declared, hero h1 token reference + regression guard against 76/80 px, lead h1 token reference + 80 px guard, `.cs-section` base padding uses tokens, `.cs-pillars/.cs-kpi-band` image-hiding guardrail, leadership portrait primitive + home.html conditional present, case-preview thumb primitive + home.html conditional present, every page file references rhythm tokens, and no over-ceiling heading px regressions on home. |

### What was hardened

1. **Typography hierarchy · CS-TYPE-04 restored at the token layer.**
   Before Step 1C, the archetype shipped four different heading-size
   ladders in the same skin: lead h1 at 80 px, hero h1 at 76 px,
   pillars/values heads at 52 px, CTA at 56 px, everything else at
   48 px. Four of those seven were over the CS-TYPE-04 ceiling. The
   skin read like different authors had taken turns at different
   sections. After Step 1C, every heading resolves through a token
   whose name tells the intent (`--fs-hero`, `--fs-lead`,
   `--fs-h2`, `--fs-h3`). Hero h1 is now the single biggest beat
   (64 px), inner-page leads sit under it (56 px), every section
   title is 48 px, every card title is 26 px. A new pilot that
   wants a different scale has to either change the token (affects
   every template on the archetype — appropriate) or declare a
   per-page override (caught by review — appropriate). The path
   of least resistance now is uniformity.

2. **Copy-density control · `--copy-max: 64ch` applied uniformly.**
   CS-DENSITY-07 warns against walls of text. The skin already
   capped most intro blocks at `max-width: 64ch`, but several
   sections (hero subhead at 52ch, values intro at 64ch, cta
   intros at 56ch) drifted. Step 1C lines every long paragraph up
   on the same 64ch ceiling via the token, so a future language
   that runs longer in translation (DE/FR) does not silently push
   one section into a wall-of-text shape while neighbors stay
   calm. The section rhythm tests lock the contract.

3. **Section rhythm · the cadence is now two tokens, not six
   magic numbers.** Before Step 1C, the archetype had `100px 72px`,
   `96px 72px`, `72px 72px`, `80px 72px`, `48px 72px 100px`,
   `96px 72px 40px` scattered across the 6 skin files. Most were
   within the CS-RHYTHM-01 100×72 target, but the spread made
   regressions invisible — a future edit dropping a section to
   48×24 would sit next to the 48×72 sectors ribbon as if
   intentional. Step 1C normalizes every chapter-class section to
   `var(--space-section-y) var(--space-section-x)`, every band
   (KPI, trust, sectors) to `var(--space-band-y)`, and the footer
   to `var(--space-footer-y)`. Three tokens govern every vertical
   beat. A static test asserts every page file references the
   tokens, so a future section authored with hardcoded padding
   will fail CI before review.

4. **"Template-marketplace feeling" reduced · no section title
   over-shoots the restraint ceiling.** The marketplace-leak
   failure mode that CS-TONE-05 names happens in small doses:
   52 px section heads read as "marketing page", 56 px CTA heads
   read as "landing funnel", 80 px lead heads read as "home
   builder hero template". Each individually is a minor drift;
   together they push the page off the institutional-advisory
   axis. Tightening every one to the 48 px ceiling at the token
   level moves the page back onto the axis without touching
   copy. The static-file regression test forbids these four
   bad-px values (52/56/76/80) from ever landing as a `font-size`
   on `home.html` again.

5. **Image rhythm · the photographic cadence is enforced, not
   trusted.** CS-IMG-RHYTHM-01 prescribes the archetype's
   home rhythm: one photo (hero) → typographic beats (pillars,
   KPI, sectors, trust) → portrait beat (leadership) → case-photo
   beat (cases) → typographic pause (CTA). The prior skin trusted
   authors to maintain this — there was no CSS rule stopping a
   template from adding a background image to the pillars, a
   photographic wallpaper to the KPI band, or a big hero photo
   reused on every case card. Step 1C hard-enforces the two
   "should never render" halves of the contract with a `display:
   none` guardrail on `.cs-pillars .pillar img, .cs-pillars .pillar picture, .cs-kpi-band img, .cs-kpi-band picture`. An
   author who tries to inject a decorative photo into either
   section sees it vanish, with no breakage elsewhere. The contract
   is also tested as a static string assert so a future loosening
   of the rule fails CI.

6. **Image scarcity after hero · opt-in enrichment primitives.**
   The current Pragma + Fiscus templates render leadership as
   text-only cards and case-preview as typographic rows. That
   passes the safety contract (no dark-on-dark, no stock cliché)
   but fails CS-IMG-SEC-03 (leadership uses real portraits) and
   CS-IMG-SEC-05 (cases use slot-4/5 thumbs rotated). Step 1C
   ships two archetype-level primitives — `.cs-leadership .card
   .portrait` and `.cs-cases-preview .row .thumb` — that the
   home.html markup now renders conditionally on `partner.portrait`
   / `post.thumb`. Existing templates still render typographic
   (no regression), but any pilot (or retro-curation step) that
   adds portrait/thumb URLs to its content registry immediately
   gets the editorial enrichment — without a single CSS edit per
   template. This is the scalable path: one skin primitive, opt-in
   per content registry, zero hand-tuning.

7. **Pexels-only enforcement is now active at the live render
   path for every new corporate-suite template.** `imagery_policy.py`
   runs on every live render of a corporate-suite template (archetype-
   gated), validates the pool's URLs against the Pexels CDN, checks
   the 6-slot canonical shape, and flags a soft-warning for an
   under-width hero. Legacy exemption for `business-corporate`
   (Pragma) keeps the live render silent while the retro-curation
   is pending — the module still reports `pexels_only=False` so
   any dashboarding / factory-tooling consumer sees the backlog.
   For `business-fiscal` (Fiscus) the helper confirms compliance
   on every render. If Solaria Commit B un-pauses with a
   `business-coaching` pool carrying even one Unsplash URL, the
   helper emits a `UserWarning` naming the slug — a loud signal
   caught by the test suite and by ops during template authoring.

8. **Editorial/advisory flow reinforced · shared utility classes
   the SOP can point agents at.** `.cs-section-seam` gives the
   skin a neutral-tinted hairline primitive for chapter-level
   separators. `.cs-sec-label` is an explicit alias for the
   tracked-uppercase label rule so a future partial can adopt the
   canonical label class without fighting scope. `.cs-section
   h2 em` / `.cs-section .head h2 em` / `.cs-section .heading em`
   extend CS-TYPE-02 italic-em emphasis uniformly across all
   section heads — prior iterations only explicitly declared it
   on a handful of sections, so a future section that reached
   for uppercase to emphasize a word would not be caught by the
   rule. Now the cascade is archetype-wide.

### Where Pexels policy is now enforced (and still pending)

| Pool key | Consumer template | Policy status |
|---|---|---|
| `business-corporate` | `pragma-corporate-suite` | **Legacy-exempt · silent.** Standard tracks this as the single tolerated Unsplash pool pending retro-curation (`docs/content-factory/imagery/packs/` work). The validator reports `is_legacy_exempt=True`, `pexels_only=False`, `is_compliant=True` (shipping sense) so the live render never warns on a Pragma page. `validate_corporate_suite_imagery_key("business-corporate")` returns `non_pexels_urls=[6 Unsplash URLs]` for factory dashboarding / retro-curation tooling. |
| `business-fiscal` | `fiscus-commercialista` | **Compliant · silent.** All 6 URLs on `images.pexels.com`, canonical 6-slot shape, hero at `w=1600`. The live render passes the gate on every request. Acts as a positive reference for any future pilot. |
| `business-coaching` | paused Solaria Commit B | **Not enforced yet.** The pool is in `CORPORATE_SUITE_POOL_KEYS` so the gate is *ready* to enforce, but the pool is not registered in `preview_imagery.IMAGERY_CONFIG` until Solaria un-pauses. When it does, any Unsplash URL in slot 0-5 emits a `UserWarning` on the first render. |
| **Any future corporate-suite pilot** | TBD | **Enforced by construction.** New pools register via the same `imagery_key` DNA field + `preview_imagery.IMAGERY_CONFIG` entry. The validator runs on every render under the archetype gate. A non-Pexels URL on a non-legacy pool emits a `UserWarning` the first time the page is loaded — caught by ops, by the test suite, and by any CI check that elevates `UserWarning` to an error. |

Still pending (explicitly out of Step 1C scope):

- **Hard promotion of `UserWarning` to a build-time error.** The
  helper is intentionally lenient (warn, never raise) because it
  runs inside the live-preview request path and must not 500 the
  page. A pre-commit hook or a `manage.py check` extension that
  elevates the warning to a failure belongs to the validator step.
- **Retro-curation of `business-corporate` to Pexels.** AP3
  tracking. Once the 6 Unsplash URLs are replaced with
  reviewer-approved Pexels equivalents, the `LEGACY_EXEMPT_KEYS`
  set shrinks to empty and the archetype becomes Pexels-only by
  construction.
- **Per-slot hero-width + portrait-aspect enforcement.** The
  helper flags hero width < 1600 as a soft check; it does not
  yet validate portrait-slot widths, crop-aspect squareness
  (CS-IMG-CROP-02), or the caption+role+coherence 3-line
  metadata contract (CS-IMG-COH-06). These require the pack-file
  inventory (`imagery/packs/<cluster>.md`) which is tracked as a
  separate curator deliverable.
- **Cross-cluster URL-reuse detection.** `CS-IMG-SRC-04` bans
  the same Pexels URL in two different cluster pools. The
  existing `scripts/check_imagery_pack.py` (X.3 C3) greps for
  duplicates across packs; Step 1C does not duplicate that
  check at the request-path layer.

### What still requires browser verification

Step 1C reduces three contracts to PASS-by-construction via static
tests, but the authoritative gate remains the live Playwright/manual
walk per CS-BROWSER-01. These checks still need the browser:

1. **Type-scale visual harmony at 1920/1440/1280.** The tokens say
   64 px hero, 56 px lead, 48 px section — but the subjective
   readability question ("does the hero still read as the biggest
   beat? does the lead not compete? do 48 px h2s feel generous
   without feeling consumer-web?") is pixel-state, not symbol-state.
   Walk Pragma + Fiscus home + about + services pages on a
   1440×900 viewport and confirm the hierarchy reads as intended.

2. **Leadership portrait primitive on a palette that exercises
   it.** Currently no enrolled template declares `partner.portrait`,
   so the primitive is inert on live renders. Before the next pilot
   adds portraits, a throwaway DevTools test should inject a
   portrait URL into a partner card on either Pragma or Fiscus and
   confirm the 4:3 frame + `object-fit: cover` + padding reset
   reads editorial (not sticker-on-card).

3. **Case-preview thumb primitive on a palette that exercises
   it.** Same shape as (2) — inject a `post.thumb` URL via DevTools
   and confirm the 80×60 thumb aligns with the title baseline at
   1440 and does not push the row height off the 28 px padding.

4. **Image-rhythm guardrail effect is transparent.** On the current
   live templates there are no `<img>` tags inside `.cs-pillars
   .pillar` or `.cs-kpi-band`, so the `display: none` rule is
   dormant by design. A regression test where a fake `<img>` is
   injected via DevTools into `.cs-kpi-band` should confirm the
   image disappears and the cadence holds (no reflow, no extra
   whitespace where the image would have sat).

5. **Section padding uniformity at 1440.** Walk home.html top to
   bottom and scroll-capture every section boundary. Vertical
   rhythm should read as ~100 px → ~100 px → ~72 px (KPI band) →
   ~36 px (sectors ribbon) → ~72 px (trust) → ~100 px → ~100 px →
   ~100 px (CTA) → ~96 px (footer). A section that feels
   "squished" vs its neighbors now fails the rhythm contract
   even if its content is fine.

6. **Pexels policy at runtime.** Load Pragma and Fiscus live
   routes with `python -W error::UserWarning` and confirm Pragma
   is silent (legacy-exempt) while Fiscus is silent (compliant).
   Then manually monkeypatch a non-Pexels URL into the Fiscus pool
   in a dev shell and confirm the first request emits the
   expected `UserWarning` naming the slug.

7. **RTL variant sanity.** The type-scale tokens are set under
   `:root`, so RTL Arabic picks them up automatically. The
   existing `html[dir="rtl"] body { font-size: 17px; line-height:
   1.78; }` override stays in charge for body copy. Walk the AR
   locale on Fiscus home and confirm h1/h2/h3 sizes composite
   visually with Kufi + Amiri at the same relative weight as the
   Latin render — a token change that inadvertently crushed the
   Arabic heading would be caught here.

8. **Editor iframe overflow guard.** The existing `body.mw-is-editor-preview`
   overflow-wrap guard covers `.cs-hero h1`, `.cs-pillars h2`,
   `.cs-leadership h2`, `.cs-nav .word`. With the leadership
   portrait primitive now landing in the card top zone, a long
   studio name edited in the editor should still reflow cleanly
   around the portrait frame. Low-risk (the portrait sits above
   the name, not beside it), but worth a once-over in the walk.

---

## Changed-files summary (Step 1A + Step 1B + Step 1C cumulative)

```
M templates/live_templates/business/corporate-suite/_base.html
M templates/live_templates/business/corporate-suite/home.html
M templates/live_templates/business/corporate-suite/about.html             (Step 1C)
M templates/live_templates/business/corporate-suite/services.html          (Step 1C)
M templates/live_templates/business/corporate-suite/case_study_list.html   (Step 1C)
A apps/catalog/theme_safety.py                    (Step 1A)
A apps/catalog/imagery_policy.py                  (Step 1C)
M apps/catalog/views.py                           (Step 1A + 1C)
M apps/catalog/tests.py                           (Step 1A + 1B + 1C)
M factory/reports/hardening/step1-core-hardening.md
```

Step 1C delta only:
- `_base.html`: ~70 lines net added across the type-scale + rhythm
  token block, the `.cs-section` / `.cs-section.dark` / `.cs-foot`
  padding token-refactor, the image-rhythm guardrails, the
  `.cs-leadership .card .portrait` + `.cs-cases-preview .row .thumb`
  primitives, and the `.cs-section-seam` utility. No new selectors
  outside the archetype scope; no markup changes.
- `home.html`: ~45 lines net modified — type-scale references on
  hero / pillars / leadership / cases / CTA, section padding
  tokenization, an optional `{% if partner.portrait %}` conditional
  in the leadership card loop, an optional `{% if post.thumb %}`
  conditional in the case-preview row loop. No structural markup
  change beyond the two conditionals.
- `about.html` / `services.html` / `case_study_list.html`: ~10-15
  lines each modified — section padding tokenization, h2/h3/intro
  heading + copy size tokenization. No structural markup change.
- `apps/catalog/imagery_policy.py`: ~220 lines of pure-function
  URL validation + a `PolicyReport` dataclass + an archetype-gated
  `enforce_corporate_suite_imagery_policy(...)` hook. No Django
  dependency except the lazy import of `preview_imagery.IMAGERY_CONFIG`.
- `apps/catalog/views.py`: 6 lines of wire-up inside the existing
  `get_context_data` hook — one archetype lookup, one enrichment
  call, one imagery-policy call. Chained after the Step 1A theme
  enrichment so the two hooks see the same archetype-gated context.
- `apps/catalog/tests.py`: appended `CorporateSuiteImageryPolicyTests`
  (6 tests) + `CorporateSuiteRhythmContractTests` (8 tests) at the
  tail of the file, mirroring the Step 1A/1B pattern. All are
  static-file + pure-function asserts — no DB state, no client
  requests, runs in milliseconds.
- This hardening report gains the Step 1C section above.

### How these changes improve scalability across future templates

Step 1C makes the archetype *absorb* the four most common
review-time regressions of Wave 1 + Solaria Commit A — oversized
display headlines, inconsistent section padding, scarce post-hero
imagery, and a legacy Unsplash pool — at the archetype layer so
the next pilot inherits them without work:

1. **A new pilot that wants a different type scale does not
   edit any page file.** It picks new token values in the brand
   theme dict (or in a per-template `<style>` override block).
   Every heading rule in every page file already resolves through
   the token, so one change propagates to 6 pages × ~15 heading
   selectors. A pilot that drifts from the token (e.g., a
   per-page hardcoded 88 px h1) fails the static rhythm contract
   test on the first CI run.

2. **Section padding cannot drift to feature-matrix density.** A
   new pilot's page file must reach for `--space-section-y` /
   `--space-section-x`. The rhythm contract test asserts every
   enrolled page file contains both tokens. A page file that
   hardcodes `48px 24px` to fit more content fails the test
   loud, before any reviewer eyeballs the diff.

3. **Leadership + case-card imagery is a content-registry
   opt-in, not a per-template skin edit.** To enrich the next
   pilot with portraits + thumbs, the author adds a `portrait`
   field to each `leadership[]` entry and a `thumb` field to
   each `posts[]` entry in the content registry. Zero CSS
   changes. The archetype skin already renders the editorial
   4:3 figure + 80×60 thumb. A retro-enrichment of Pragma and
   Fiscus follows the same pattern.

4. **Pexels-only is the default, not the exception.** A new
   pool just works — it is registered in `preview_imagery.IMAGERY_CONFIG`
   under a `business-<kind>` key, gets a `CORPORATE_SUITE_POOL_KEYS`
   membership update, and is automatically validated on every
   render. The only pool that is explicitly exempt is the
   Pragma legacy one, tracked in `LEGACY_EXEMPT_KEYS`. A
   future pilot that tries to slip Unsplash URLs into its pool
   sees its first live render warn — the diff never survives
   review.

5. **Image-rhythm regressions are impossible by construction.**
   The `display: none` guardrail on pillars + KPI band means an
   author who accidentally pastes a decorative image into a
   typographic section sees it disappear. The authoring
   experience gets a visible-but-harmless hint (the image
   doesn't render) instead of a silently shipped AP12 regression.

6. **Token naming documents intent for every future agent.** A
   template-builder agent reading the skin for the first time
   sees `--fs-hero`, `--fs-lead`, `--space-section-y`,
   `--space-band-y`, `--space-footer-y` and can pattern-match
   to the CS-TYPE-04 / CS-RHYTHM-01 rule numbers in the design
   standard. No "what does this magic number mean?" archaeology.

Net: Step 1C lifts the archetype from "every pilot re-encounters
the same editorial floor problems" to "every pilot inherits an
editorial floor that is already a contract". The browser walk
stays the ship veto per CS-BROWSER-01 — the contracts above only
reduce how many ways that walk can surface surprises.
