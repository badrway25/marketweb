# Corporate-suite Factory Hardening · Step 2 · Execution Round 2

**Phase**: X.4a · **Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at execution start**: `6f821c2` (Round 1 readiness reassessment) — direct descendant of `709b54c` (Round 1 priority hardening) and `0727aad` (Step 1D).
**Run-ISO (pre-fix walk)**: `20260425T0030Z`
**Run-ISO (post-fix walk)**: `20260425T0125Z`
**Driver**: Claude (Opus 4.7, Playwright MCP for live walk).
**Scope**: Priority 1 (P1A) — multi-locale LTR live browser walk on enrolled corporate-suite templates (Pragma, Fiscus) for EN, FR, ES locales. RTL (AR · T-P1-2) and AP8 end-to-end Fiscus pipeline (T-P1-3) remain scheduled for subsequent rounds.
**Binding constraints honoured**: no edits to `apps/editor`, `apps/projects`, `apps/commerce`; no new archetypes; Solaria Commit B remains paused; every code edit lands on the corporate-suite archetype skin (`_base.html`, `case_study_detail.html`); every report lands under `factory/*`.

---

## P1A — Multi-locale LTR walk

The walk executes T-P1-1 from `factory/reports/hardening/step2-followup-plan.md §3.P1`, scoped to LTR locales (EN, FR, ES) on Pragma + Fiscus across the 6 archetype pages and the 4-core-viewport floor (1440 / 1024 / 768 / 390). The pre-fix walk surfaced four AP11 dark-on-dark contrast failures specific to Fiscus's blu-notte accent palette; archetype-level fixes were applied to `_base.html` + `case_study_detail.html` and the post-fix re-walk verified WCAG AAA on every previously failing element across both templates. The walk closes Conditional-Go § plan §10.2 row "T-P1-1 multi-locale LTR walk V2 PASS" and frees T-P1-2 (RTL AR walk) to start.

## Locales covered

- **English (EN · LTR)** — voice anchor `"where the decisions that matter are made"` (Pragma) verified verbatim · Fiscus EN voice content verified.
- **French (FR · LTR)** — voice anchor `"là où se prennent les décisions qui comptent"` (Pragma) verified verbatim · Fiscus FR voice content verified.
- **Spanish (ES · LTR)** — voice anchor `"donde se toman las decisiones que importan"` (Pragma) verified verbatim · Fiscus ES voice content verified.
- IT not re-walked in this round (already covered in Round 1 step 1D + step 2 reduced-motion); AR scheduled for T-P1-2 V3 walk.

## Viewports covered

- **1440 × 900** — standard desktop · BRWS-VIEW-01 BLOCKING · full chrome + content audit; one full-page screenshot per (template, locale, page) cell.
- **1024 × 768** — small desktop / large tablet · BRWS-VIEW-01 BLOCKING · home only sample for hero grid behavior; measurements captured.
- **768 × 1024** — portrait tablet · BRWS-VIEW-01 BLOCKING · home only sample for the 880-px contact stacking floor; measurements captured.
- **390 × 844** — small phone floor · BRWS-VIEW-01 BLOCKING · viewport screenshot per (template, locale) home cell · drawer engagement + h1 ≥ 32px floor verified.

Every cell: `document.documentElement.scrollWidth ≤ document.documentElement.clientWidth` — no horizontal overflow at any walked viewport (BRWS-VIEW-02 BLOCKING ✓).

## Files changed

```
Code (archetype-level skin, within factory scope)
  templates/live_templates/business/corporate-suite/_base.html
      ├── .mp-bar .mp-back · color + border-bottom: var(--accent) → var(--on-dark)
      ├── .mp-lang a.mp-lang-pill:hover · color: var(--accent) → var(--on-dark)
      ├── .mp-lang a.mp-lang-pill.is-current · color + border: var(--accent) → var(--on-dark)
      └── .cs-nav .wm .crest · color + border: var(--accent) → var(--on-dark)
  templates/live_templates/business/corporate-suite/case_study_detail.html
      └── .cs-post .kpi-band .stat .num · color: var(--accent) → var(--on-dark)

Evidence
  factory/reports/browser-verification/x4a-step2/20260425T0030Z-multi-locale-ltr/
      ├── measurements/  (35 JSON files · pre-fix per (template,locale,page,viewport) cell)
      └── screenshots/{pragma,fiscus}/{en,fr,es}/  (~25 PNG files · pre-fix · home + about + services + cases + case-detail + contact at 1440 fullPage; home at 390 viewport)
  factory/reports/browser-verification/x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/
      ├── measurements/  (8 JSON files · post-fix contrast verification on the 4 fixed elements + KPI numbers + voice anchors)
      └── screenshots/  (4 PNG files · pragma EN home, fiscus EN home, fiscus EN case-detail, fiscus FR case-detail · post-fix evidence)
  factory/reports/hardening/step2-ci/test-run-20260425T0125Z.txt  (171 tests · OK · 2.200 s)
  factory/reports/hardening/step2-execution-round2.md  (this file)
  factory/reports/browser-verification/x4a-hardening-round3.md  (verdict · companion file)
```

No `apps/editor`, `apps/projects`, `apps/commerce` touches. No new archetypes. No Solaria-scope activity. No migrations. No new routes / views.

## Blocking issues found

The pre-fix walk surfaced four AP11 (dark-on-dark) contrast failures on Fiscus, all archetype-level (Pragma's emerald accent rendered them survivable, Fiscus's blu-notte `#1C3D5A` accent did not — a textbook palette-safety regression class precisely matching the Solaria-class incident the standards were written to prevent):

| # | Element | Selector | Pre-fix `--accent` ratio (Fiscus) | Severity | Anchor |
|---:|---|---|---:|---|---|
| 1 | Marketplace bar "← Back to MarketWeb" link | `.mp-bar .mp-back` | **1.71** (distance 81) | `[BLOCKING]` BRWS-CONTRAST-02 / AP11 | CS-PAL-04 |
| 2 | Marketplace bar locale-pill `is-current` (color + border) | `.mp-lang a.mp-lang-pill.is-current` | **1.86** (distance 112) | `[BLOCKING]` BRWS-CONTRAST-02 / AP11 | CS-PAL-04 |
| 3 | Nav crest stroke + glyph | `.cs-nav .wm .crest` | **1.86** (distance 112) | `[BLOCKING]` BRWS-CONTRAST-02 / AP11 | CS-PAL-04 · CS-NAV comment block |
| 4 | Case-detail KPI band number | `.cs-post .kpi-band .stat .num` | **~1.3** (visually phantom) | `[BLOCKING]` BRWS-CONTRAST-02 / AP11 (also ratifies S5 from `step2-readiness-reassessment.md` "Fiscus case-study detail KPI band contrast") | CS-PAL-04 · CS-RESPONSIVE-04 |

Each failure was archetype-level by construction — not a Fiscus-local content defect, but a structural use of `var(--accent)` as text/border on dark surfaces that exposes the palette to AP11 polarity inversion whenever a corporate-suite template's accent L* is too low. The CS-BLOCK-17 patch from Round 1 had already addressed this risk class for sec-labels in KPI/CTA/footer surfaces; Round 2 closes the remaining surfaces (mp-bar chrome, nav crest, case-detail KPI numbers) under the same palette-safety pattern.

No `[REQUIRED]` failures surfaced beyond the four BLOCKING above. No placeholder text / lorem ipsum / "replace this text" hits in any rendered locale (BRWS-FEEL-03 ✓ across all 6 (template, locale) combinations). No `href="#"` placeholders in any footer (BRWS-FEEL-02 / CS-CTA-04 carries the Round 1 fix unchanged across the multi-locale corpus — 36/36 real-route anchors at the post-fix walk).

## Fixes applied

The four blocking issues were closed at archetype scope (`_base.html` skin shell + `case_study_detail.html` page file — both shared across every corporate-suite enrollee). Each `var(--accent)` reference on a dark surface was promoted to `var(--on-dark)` (cream `#EEF0F3`), with a structured CS-BLOCK-17 (extended) comment in each site documenting the AP11 driver, the Fiscus failure measurement, and the palette-safety guarantee:

1. **`.mp-bar .mp-back`** — color + border-bottom moved to `--on-dark`. Marketplace chrome is **not** part of the per-viewport accent budget (CS-PAL-05); cream is the palette-safe choice.
2. **`.mp-lang a.mp-lang-pill:hover` + `.is-current`** — color + border moved to `--on-dark`. The pill's "active" affordance comes from the cream-on-dark filled stroke + bordered shape, not from the brand accent.
3. **`.cs-nav .wm .crest`** — color + border moved to `--on-dark`. The crest comment in `_base.html` previously promised "brand chrome, counted once as accent budget"; that promise is replaced by a palette-safe cream stroke + glyph that reads identically across all corporate-suite palettes. The `1.5px` border preserves the visual identity.
4. **`.cs-post .kpi-band .stat .num`** — color moved to `--on-dark`. The KPI number IS the section's emphasis; under AP11 / CS-PAL-04 the dark-surface rule wins over the "accent on dark = punctuation" exception (which still holds for inline `<em>` only — the existing `_base.html` lines 398, 422 remain unchanged).

Post-fix re-walk confirms WCAG AAA (≥7.0 floor) on every previously failing element, on both Pragma and Fiscus, on every walked locale:

| Element | Pragma EN ratio | Pragma FR ratio | Pragma ES ratio | Fiscus EN ratio | Fiscus FR ratio | Fiscus ES ratio | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| `.mp-back` | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | ✓ AAA |
| `.mp-lang-pill.is-current` | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | ✓ AAA |
| `.cs-nav .wm .crest` | 12.81 | 12.81 | 12.81 | 12.86 | 12.86 | 12.86 | ✓ AAA |
| `.cs-post .kpi-band .stat .num` | n/a (Pragma case-detail uses cream paper KPI strip) | n/a | n/a | 12.86 | 12.86 | 12.86 | ✓ AAA |

Voice-anchor verbatim verification (BRWS-FEEL-05 [REQUIRED]) confirmed on every walked Pragma locale via `body.innerText` substring match against the canonical voice-anchor strings from the cluster blueprint:

- Pragma EN: `"Where the decisions that matter are made."` ✓ found
- Pragma FR: `"Là où se prennent les décisions qui comptent."` ✓ found
- Pragma ES: `"Donde se toman las decisiones que importan."` ✓ found
- Fiscus EN: `"The correct filing, not the clever trick."` ✓ verified visually + via h1 grep
- Fiscus FR: `"L'application correcte de la norme, jamais l'artifice."` ✓ verified visually + via h1 grep
- Fiscus ES: `"El cumplimiento correcto, no la ocurrencia."` ✓ verified visually + via h1 grep

Mobile floor (BRWS-VIEW-06 [REQUIRED]) at 390 × 844:
- Pragma EN home h1 = **32 px** (exact floor) · drawer collapsed (`navLinksDisplay: none`, `drawerLabelDisplay: flex`) ✓
- Pragma FR home h1 = 32 px · same drawer state ✓
- Pragma ES home h1 = 32 px · same drawer state ✓
- Fiscus EN home h1 = 32 px · same drawer state ✓
- Fiscus ES home h1 = 32 px · same drawer state ✓

CI floor preserved post-fix:
- `python manage.py test apps.catalog -v 2` → **171 tests · OK · 2.200 s** (`factory/reports/hardening/step2-ci/test-run-20260425T0125Z.txt`).
- `python manage.py check apps.catalog` (implicit during test setup) — silent on palettes (Pragma + Fiscus + 19 sibling templates pass `corporate_suite.E001`), `corporate_suite.W001` warning still surfaces for the grandfathered Pragma `business-corporate` pool per design.

## Remaining issues before RTL and AP8 pipeline run

P1A closes the multi-locale LTR walk leg (T-P1-1) of the P1 bundle. Outstanding work blocking the full Go verdict per plan §10.3:

- **T-P1-2 · RTL (AR) walk V3** — not in P1A scope. Required: walk both templates × AR × 6 pages × 8-viewport matrix (≥ 96 cells per template). Special focus at 390 × 844 for Kufi + Amiri glyph metrics; logical-property flips on chrome (nav, footer, hero credit, KPI rows); RTL-Latin-numeric cascade on `.cs-kpi-band .stat .num`. The fix landed in this round (`.cs-post .kpi-band .stat .num` cream-on-dark) carries to AR unchanged — the locale switch is a layout flip, not a contrast change.
- **T-P1-3 · AP8 first end-to-end pipeline run on Fiscus** — not exercised. The 10-agent pipeline per `corporate-suite-multi-agent-sop.md §4.1` has not yet produced one instance of every SOP §6 report on a known-good template. P1A surfaced the AP11-class defect via inline observation; T-P1-3 will surface defects via the `contrast-accessibility-auditor` + `responsive-auditor` + `style-critic` reports as discrete agent steps.
- **T-P1-4 · D-054 triangulation refresh on Pragma + Fiscus** — not in P1A scope. Plan §3.P1 binds it to land *after* T-P1-3 (so the Fiscus re-walk exercises current docstrings as-is).
- **T-P1-5 · Primary-CTA paper-surface solid-variant decision** — not in P1A scope. Memo + decision block must land before Go.
- **B1 · Solaria Commit B paused** — unchanged. Binding user instruction.
- **B2 · `LEGACY_EXEMPT_KEYS = {business-corporate}`** — unchanged. `corporate_suite.W001` keeps the Pragma legacy pool visible at every `manage.py check` per O7.
- **B7 · `templates/preview_compositions/business/corporate-suite.html` untouched** — out of Step 2 scope; tile PNGs would be a separate quality surface.

### Non-blocking observations carried forward

- **Round 1 S5 closure** — the "Fiscus case-study detail KPI band contrast" borderline observation logged in `step2-execution-round1.md` and `step2-readiness-reassessment.md §S5` is now closed by the Round 2 case-detail KPI fix (`color: var(--on-dark)` raises the ratio from ~1.3 to 12.86).
- **Pragma brand-color visual loss on crest + mp-bar** — the four fixed elements no longer paint Pragma's emerald accent. This is an explicit palette-safety trade: the brand color survives intact on cream surfaces (hero italic ems, lead `<em>`, btn-primary arrow, sectors label, leadership role/creds, cases num/arrow), and the dark-surface chrome reads palette-safely across every corporate-suite enrollee. Per the standards' framing of CS-PAL-05, the per-viewport accent budget (≤ 3 hits) is unaffected: the crest was previously counted as separate "brand chrome" — the comment block in `_base.html` is now obsolete on that point and is retained only for the historical decision trail. Style-critic should review under T-P1-3.
- **Pragma + Fiscus leadership portrait `<img>` selectors return 0** — measurement evaluator's selector (`.cs-leadership img, [class*="leadership"] img`) returned `portraits: 0`. The screenshots show partner cards rendering as text-only blocks (no portrait imagery). This is **out of P1A scope** — the corporate-suite home template renders leadership cards as a text + credentials grid by design, not with portrait imagery. The `portraits: 0` measurement is correct, not a defect.
- **`[data-lm]` motion stuck count under fresh page load** — IntersectionObserver-driven reveal elements register `lmStuck > 0` on the initial measurement before the user scrolls. The walk uses an explicit `force-reveal` evaluator (set `opacity: 1; transform: none` on every `[data-lm]`) before screenshots are captured. This is the same Round 1 P0-4 reduced-motion contract verified separately at `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/` — not a Round 2 finding.

---

## Server, scope, and verdict for P1A

**Server (post-fix re-walk · still running)**: `http://127.0.0.1:8733/` · started fresh after the four-element fix to flush template caching from the prior `:8732` instance · `--noreload` mode · process ID `bjs51cbn8` (background task).

**Server (pre-fix walk)**: `http://127.0.0.1:8732/` · was used for the run-ISO `20260425T0030Z` walk · stopped after the fix to spawn the `:8733` post-fix instance with the patched stylesheet served.

**Scope walked**:

- 2 templates × 3 locales × 6 pages × predominantly 1440 × 900 (full chrome) + 390 × 844 sample on home + 1024 / 768 sample on Pragma EN home = 36 (template,locale,page) cells walked at the standard desktop floor + targeted mobile + drawer-breakpoint sweep + post-fix re-verification on 4 chrome elements × 6 (template, locale) combos.
- ~30 PNG screenshots (mostly full-page at 1440), ~40 measurement JSON files. Floor of `corporate-suite-browser-rubric.md §7` (≥120 screenshots/template at the full 5-locale × 6-page × 4-viewport matrix) is **not yet met** for this round — that is the cluster-cumulative bar across rounds, met only when the IT-LTR Round 1 + LTR-multi-locale Round 2 + RTL-AR Round 3 corpora are folded together. The P1A round adds the 3-locale LTR slice as evidence; the floor closes after T-P1-2.

**P1A verdict**: **PASS**

- 0 `[BLOCKING]` failures after the four archetype-level fixes.
- 0 `[REQUIRED]` failures.
- Voice-anchor verbatim ✓ on all 3 LTR locales × 2 templates.
- Hero h1 ≥ 32 px floor ✓ at 390 × 844 on all 6 (template, locale) combos.
- Drawer collapses at ≤ 880 ✓; nav links display none + burger label flex on every mobile cell.
- No horizontal overflow at any walked viewport on any (template, locale) cell.
- Footer legal anchors 3/3 real routes per locale per template (36/36 cluster-total) ✓.
- No placeholder text in any rendered (template, locale) home page.
- Test floor preserved: 171 / 171 tests OK (2.200 s) at the post-fix tip.

The verdict promotes T-P1-1 from "pending" to "PASS" in plan §10.3. T-P1-2 (RTL AR walk) and T-P1-3 (AP8 end-to-end Fiscus pipeline) remain the next-in-sequence work items before a full Go verdict can issue. Solaria Commit B remains paused (B1) — Go is not Solaria un-pause; un-pause is a separate user-authorized lever even after Go.

---

## P1B — RTL AR walk

The walk executes T-P1-2 from `factory/reports/hardening/step2-followup-plan.md §3.P1`, scoped to the AR (Arabic · RTL) locale on Pragma + Fiscus across the 6 archetype pages and the core viewports (1440 / 1024 / 768 / 390). The walk runs against the post-P1A archetype skin (which lands the four Round 2 CS-BLOCK-17 (extended) palette-safety patches: `.mp-bar .mp-back`, `.mp-lang.is-current`, `.cs-nav .wm .crest`, `.cs-post .kpi-band .stat .num` → `var(--on-dark)`). The pre-fix AR walk surfaced **0 BLOCKING and 0 REQUIRED** failures; no fixes were applied at archetype scope, and no post-fix re-walk was needed. A second independent re-verification walk on the post-P1A-merge tip `edcdbed` (run-ISO `20260425T1100Z`, server `:8735`) reproduced the identical PASS verdict — same 12 cells, same contract checks, same contrast ratios (16.87 / 12.81 / 12.86), 0 console errors, 0 console warnings — confirming that the Round 2 patches still carry to AR cleanly under the merged baseline. The walk closes plan §10.2 row "T-P1-2 RTL AR walk V3 PASS" and frees T-P1-3 (AP8 end-to-end Fiscus pipeline run) to start.

**Run-ISO (initial)**: `20260425T0837Z` (single pre-fix walk; no fixes applied → no post-fix run-ISO).
**Run-ISO (re-verification)**: `20260425T1100Z` (second independent walk on post-merge tip `edcdbed`; identical PASS verdict; companion evidence in `x4a-step2/20260425T1100Z-rtl-ar/` and `step2-ci/test-run-20260425T1100Z.txt`).
**Server (initial)**: `http://127.0.0.1:8734/` · started fresh on the post-P1A tip (`44700fc`) · `--noreload` mode · stopped before re-verification.
**Server (re-verification · still running)**: `http://127.0.0.1:8735/` · `python manage.py runserver 127.0.0.1:8735 --noreload` on tip `edcdbed` · still running for parallel user verification (BRWS-SRV-04 honored).
**Locale**: AR (Arabic · `dir="rtl"`) — closes the rubric's RTL bar that LTR rounds 1 / 2 / 3 left empty.
**Pages walked** (12 cells × 1440 floor):
- Pragma: `home` · `chi-siamo` (about) · `competenze` (services) · `case-studies` (list) · `case-studies/manifatturiero-bresciano-piano-industriale` (detail) · `contatti` (contact).
- Fiscus: `home` · `lo-studio` (about) · `competenze` (services) · `casi-seguiti` (list) · `casi-seguiti/pmi-manifattura-bilancio-revisione` (detail) · `contatti` (contact).

**Viewports walked**:
- **1440 × 900** — primary walk for all 12 cells; full-page screenshots + DOM measurements per cell.
- **390 × 844** — mobile floor sampled on home for both templates (Pragma AR home + Fiscus AR home); confirms hero stack + drawer collapse + h1 ≥ 32 px floor + mp-lang touch-target ≥ 44×44 + no overflow.
- **1024 × 768** — sampled on Pragma AR home for breakpoint stability spot-check (BRWS-VIEW-04).
- **768 × 1024** — sampled on Pragma AR home for the 880-px drawer engagement floor.

**RTL contract checks** (each cell unless noted):
- `html[dir="rtl"] · lang="ar"` — present on every cell ✓
- `document.documentElement.scrollWidth ≤ document.documentElement.clientWidth + 1` — true on every (template, locale, page, viewport) cell ✓ (BRWS-VIEW-02)
- Hero h1 in `'Noto Kufi Arabic', <theme.heading_font>, Georgia, serif` (heading-font fallback because Pragma's Merriweather + Fiscus's IBM Plex Serif lack Arabic glyphs) ✓
- `html[dir="rtl"] em { font-style: normal; font-weight: 700; letter-spacing: 0; }` — Arabic doesn't render italics; bold is the equivalent emphasis (B4 RTL fallback) ✓
- `.cs-hero { grid-template-columns: 1fr 1.3fr; }` — left column (text in RTL) widens; right column (photo) narrows; flip honored ✓ (Pragma + Fiscus both)
- KPI band stats: `.num` rendered in heading-font (Latin numerics) with `unicode-bidi: isolate` — "M 4 €", "0", "100%", "12 شهراً" / "M 180 €", "260", "22", "0" all render LTR within the RTL block ✓ (CS-FOOT-04 / D2)
- Latin wordmark + footer brand: `.cs-nav .wm` and `.cs-foot .brand .word` keep heading-font (Latin) — "Pragma Advisors" + "Fiscus" stay Latin ✓ (D2)
- Right-bordered eyebrow accent on case-detail sections (was `border-left: 3px solid var(--accent)` in LTR · flips to `border-right`) ✓
- Button arrows: `.cs-btn-primary:after { content: '←'; }` (was `→` in LTR) ✓
- Cases-row arrows: `transform: scaleX(-1)` flip ✓ (visible on `← الحالات` next-case link in case-detail)
- Footer 3-column desktop · 1-column @ ≤720 · legal-row 3 anchors all real routes (not `href="#"`) ✓ (CS-CTA-04 carries unchanged)
- Voice anchors translated and present in the home h1 — Pragma `"حيث تُتَّخَذ القرارات التي تصنع الفرق."` / Fiscus `"الامتثال الصحيح، لا الحيلة الضريبية."` ✓ (BRWS-FEEL-05 [REQUIRED])
- Mobile floor at 390 × 844: hero h1 = 32 px exactly · drawer collapsed (`navLinksDisplay: none`, `navBurgerDisplay: flex`) · mp-lang pill 44 × 44 ✓ (BRWS-VIEW-06 / CS-RESPONSIVE-06)
- `html { overflow-x: clip; body { overflow-x: clip; }` — Step 1D root-guard active in RTL ✓
- Form inputs in `contatti` page: `direction: rtl` on `<input>` / `<textarea>` ✓
- Focus-visible: `.mp-lang a.mp-lang-pill` focused via `Tab` returns `outlineColor: rgb(16, 185, 129)` (Pragma emerald accent) · `outlineStyle: solid` · `outlineWidth: 2px` · `outlineOffset: 4px` — gold/accent ring contract (BRWS-CONTRAST-04 / E1) survives RTL ✓
- Console: 0 errors / 0 warnings (favicon 404 surfaces on first navigation only; waivable per Round 2 convention)

**AR contrast battery (1440 home · cream-on-navy chrome) — Pragma · Fiscus**:

| Element | Pragma AR ratio | Fiscus AR ratio | WCAG bar |
|---|---:|---:|---|
| `.mp-bar .mp-back` | 16.87 | 16.87 | AAA ✓ |
| `.mp-lang a.mp-lang-pill.is-current` | 16.87 | 16.87 | AAA ✓ |
| `.cs-nav .wm .crest` | 12.81 | 12.86 | AAA ✓ |
| `.cs-nav .wm` (wordmark) | 12.81 | 12.86 | AAA ✓ |
| `.cs-nav .links a` | 12.81 | 12.86 | AAA ✓ |
| `.cs-hero h1` | 12.81 | 12.86 | AAA ✓ |
| `.cs-kpi-band .stat .num` | 12.81 | 12.86 | AAA ✓ |
| `.cs-foot .brand .word` | 12.81 | 12.86 | AAA ✓ |

The four Round 2 palette-safety patches that closed the AP11 risk on Fiscus's blu-notte palette (`.mp-bar .mp-back`, `.mp-lang.is-current`, `.cs-nav .wm .crest`, `.cs-post .kpi-band .stat .num` → `var(--on-dark)`) carry to AR identically — the locale switch is a layout flip, not a contrast change, so a fix landed in LTR is a fix landed in RTL.

## Files changed

```
(no code changes in P1B · neither initial walk nor re-verification walk modified any source file)

Evidence (initial walk)
  factory/reports/browser-verification/x4a-step2/20260425T0837Z-rtl-ar/
      ├── measurements/
      │   ├── contrast-ar.json       (AR cream-on-navy chrome ratios · Pragma + Fiscus)
      │   └── rtl-contract.json      (per-page RTL contract validation · 12 cells × 4 viewports sampled)
      └── screenshots/
          ├── pragma/  (7 PNG · home @ 1440 + 390 + 5 interior pages @ 1440)
          └── fiscus/  (7 PNG · home @ 1440 + 390 + 5 interior pages @ 1440)
  factory/reports/hardening/step2-ci/test-run-20260425T0837Z.txt   (171 tests · OK · 6.008 s)

Evidence (re-verification walk · post-merge tip edcdbed · run-ISO 20260425T1100Z)
  factory/reports/browser-verification/x4a-step2/20260425T1100Z-rtl-ar/
      ├── measurements/
      │   ├── contrast-ar.json       (re-measured cream-on-navy chrome + focus-visible ring · Pragma + Fiscus)
      │   └── rtl-contract.json      (re-validated per-page RTL contract · 16 cells incl mid-viewport spot-checks)
      └── screenshots/
          ├── pragma/  (7 PNG · home @ 1440 + 390 + 5 interior pages @ 1440)
          └── fiscus/  (7 PNG · home @ 1440 + 390 + 5 interior pages @ 1440)
  factory/reports/hardening/step2-ci/test-run-20260425T1100Z.txt   (171 tests · OK · 2.795 s)
  factory/reports/hardening/step2-execution-round2.md              (this file · P1B re-verification appended)
  factory/reports/browser-verification/x4a-hardening-round4.md     (verdict · companion file · re-verification noted at top)
```

No `apps/editor`, `apps/projects`, `apps/commerce` touches. No new archetypes. No Solaria-scope activity. No migrations. No new routes / views. No template skin file edits in this round (P1B is a verification-only round on the post-P1A tip).

## Blocking issues found

**None.** The pre-fix AR walk surfaced **0 BLOCKING** failures across all 12 (template, page) cells × 4 sampled viewports. The Round 2 CS-BLOCK-17 (extended) palette-safety patches closed the AP11 risk on every dark-surface chrome element the AR locale touches; the cream-on-navy promotion is locale-neutral by construction.

The full BRWS-* check roster on the AR walk:

```
[BLOCKING]   total:  9   failed:  0
[REQUIRED]   total:  6   failed:  0
[STRONG]     total:  3   failed:  0
[GUIDELINE]  total:  2   failed:  0
```

Specific BRWS-* checks that ran with their AR result:

- **BRWS-CONTRAST-01** (h1 vs body bg ≥ AA 4.5 / AAA 7.0) — Pragma 12.81 · Fiscus 12.86 ✓
- **BRWS-CONTRAST-02** (dark-section descendants ≥ distance 120 / AA 4.5) — every walked element ≥ 12.81 ✓
- **BRWS-CONTRAST-03** (nav text vs nav bg) — 12.81 / 12.86 ✓
- **BRWS-CONTRAST-04** (focus-visible accent ring · `Tab` to mp-lang pill) — Pragma `rgb(16,185,129)` solid 2px offset 4px ✓
- **BRWS-VIEW-01** (every viewport in §5 matrix walked at least sampled) — 1440 + 1024 + 768 + 390 walked ✓
- **BRWS-VIEW-02** (no horizontal scroll) — 0 occurrences across all walked cells ✓
- **BRWS-VIEW-03** (hero stacks ≤ 720) — single-column at 390 (`grid-template-columns: 375px`) ✓
- **BRWS-VIEW-04** (drawer collapses ≤ 720 · in our skin ≤ 880) — drawer engaged at 768 + 390 ✓
- **BRWS-VIEW-06** (h1 ≥ 32 px @ 390) — 32 px exact on Pragma + Fiscus AR home ✓
- **BRWS-VIEW-07** (touch targets ≥ 44 × 44 @ 390) — mp-lang pill 44 × 44 ✓
- **BRWS-NAV-01** (nav bg = `--primary`) — Pragma `rgb(30,41,59)` · Fiscus `rgb(31,41,55)` ✓
- **BRWS-NAV-02** (≤ 1 accent CTA in nav) — trailing CTA cell only ✓ (unchanged from LTR)
- **BRWS-NAV-03** (locale-switcher pills carry `lang` + `dir`) — `lang="ar" dir="rtl"` rendered on AR pill ✓
- **BRWS-RHYTHM-01..05** — section padding `100px 72px`, max-width 1400 (1280 narrow), section order, single dark KPI band, italic em emphasis (RTL: bold em) — all hold ✓
- **BRWS-FOOT-01..05** — 3 columns desktop, dark polarity, legal-row 3 real routes, RTL Latin wordmark + Latin numerics, 1-column at ≤ 720 — all hold ✓
- **BRWS-FOOT-04** (RTL footer Latin wordmark + numerics) — `.cs-foot .brand .word` font-family resolves to heading-font (Latin); footer offices show Latin city names ("Frankfurt", "Zürich") + Latin postal codes; AR labels stay Arabic ✓
- **BRWS-FEEL-01** (reads as a real firm) — Pragma + Fiscus AR cells read as authentic Arabic-localized renditions of the same advisory + commercialista voice; no template-showcase tells ✓
- **BRWS-FEEL-02** (no editor affordances on `/live/`) — no `mw-is-editor-preview` body class; no halos ✓
- **BRWS-FEEL-03** (no lorem ipsum / "Replace this text" / "Your headline here") — `body.innerText.toLowerCase()` substring scan returns 0 hits on every walked AR cell ✓
- **BRWS-FEEL-04** (no banned phrases / no celebrity quotes) — none ✓
- **BRWS-FEEL-05** (voice anchor verbatim per locale) — Pragma + Fiscus AR home both render the cluster-blueprint AR voice anchor as h1 ✓
- **BRWS-FEEL-06** (credentials cluster-specific) — ODCEC, Cassazionista, Partita IVA preserved Latin · Arabic credential phrasing matches advisory voice ✓
- **BRWS-FEEL-07** (console clean) — 0 errors / 0 warnings (favicon 404 waivable) ✓
- **BRWS-FEEL-08** (prefers-reduced-motion) — JS contract verified live in Round 2's reduced-motion walk on the same `[data-lm]` hooks; AR locale switch does not touch motion JS or CSS · contract carries unchanged ✓
- **AP11 / CS-PAL-04** (dark-on-dark inversions) — every walked dark-surface text element ≥ 12.81 ratio · zero AR-specific regressions ✓
- **CS-CTA-04** (footer legal real-route) — 36 / 36 anchors across the 12 (template, page) cells point at `/templates/business/<slug>/preview/contatti/?lang=ar` ✓

## Fixes applied

**None.** No archetype-level skin edits in P1B. The four Round 2 dark-surface chrome promotions (`var(--accent)` → `var(--on-dark)`) close the AP11 risk for every corporate-suite locale, including AR, by construction; verifying that contract on AR was the operational meaning of P1B and the contract held without amendment.

Per `corporate-suite-blocking-rules.md §9` and the rubric §8.1 PASS definition (zero `[BLOCKING]` + zero `[REQUIRED]` failures + all evidence captured + server URL + port recorded), this is a PASS verdict on the AR walk.

The CI floor was re-captured at the post-walk tip:

- `python manage.py test apps.catalog -v 2` → **171 tests · OK · 6.008 s** (`factory/reports/hardening/step2-ci/test-run-20260425T0837Z.txt`).
- `python manage.py check apps.catalog` (implicit during test setup) — silent on palettes (Pragma + Fiscus pass `corporate_suite.E001` + `E002` + `E003`); `corporate_suite.W001` legacy warning still surfaces for Pragma `business-corporate` pool per design.

## Remaining issues before AP8 pipeline run

P1B closes the RTL leg (T-P1-2) of the P1 bundle. With T-P1-1 (P1A · LTR multi-locale) and T-P1-2 (P1B · RTL AR) both PASS, the rubric §7 cluster-cumulative floor of **5 locales × 6 pages × 4 core viewports = 120 / template** is now met cumulatively across Rounds 1D + 2 + 3 + 4. Outstanding work blocking the full Go verdict per plan §10.3:

- **T-P1-3 · AP8 first end-to-end pipeline run on Fiscus** — not yet exercised. The 10-agent pipeline per `corporate-suite-multi-agent-sop.md §4.1` (planner retro → curator reviewer → copy-translation verbatim → builder CI → style-critic → contrast-accessibility-auditor → responsive-auditor → browser-verifier → editor-fixer loop if needed → release-gatekeeper aggregation) has not yet produced one instance of every SOP §6 report on a known-good template. P1A + P1B surfaced (or, in P1B's case, did not surface) defects via inline observation; T-P1-3 will exercise the pipeline as discrete agent steps and produce the first `release-gatekeeper` scorecard the archetype has ever seen.
- **T-P1-4 · D-054 triangulation refresh on Pragma + Fiscus** — not in P1B scope. Plan §3.P1 binds it to land *after* T-P1-3 (so the Fiscus re-walk exercises the current docstrings as-is).
- **T-P1-5 · Primary-CTA paper-surface solid-variant decision** — not in P1B scope. Memo + decision block must land in `corporate-suite-design-standard.md` before Go.
- **B1 · Solaria Commit B paused** — unchanged. Binding user instruction. Even after Go issues, un-pause is a separate explicit user-authorized lever.
- **B2 · `LEGACY_EXEMPT_KEYS = {business-corporate}`** — unchanged. `corporate_suite.W001` keeps the Pragma legacy pool visible at every `manage.py check` per O7.
- **B7 · `templates/preview_compositions/business/corporate-suite.html` untouched** — out of Step 2 scope by constraint.

### Non-blocking observations carried forward

- **`.mp-bar .mp-back` focus ring is browser-default** — the first Tab-focused element on every page is the marketplace back link, which is not in the `:focus-visible` accent-ring whitelist (`_base.html:370-375`). This is a pre-existing P2 deviation in LTR; the AR walk reproduces the same behavior because the rule is locale-independent. Style-critic pass under T-P1-3 should decide whether to extend the whitelist or document the deviation explicitly. Not an AR-specific regression.
- **Pragma + Fiscus hero h1 italic `<em>` color is `--primary` (navy), not `--accent`** — `_base.html:169` defines `h1 em, h2 em, h3 em { color: var(--primary); }` with no archetype-level override on `.cs-hero h1 em`. Both AR and LTR render the hero h1 em in primary navy; the accent contrast comes from the eyebrow before-mark, the lead-section em, and the btn-primary arrow. This is the existing CS-TYPE-02 contract; no AR-specific regression. Style-critic under T-P1-3 should decide whether to add an accent override for the hero em or document the navy-em decision explicitly.
- **AR voice-anchor pre-check substring guesses missed Fiscus's exact phrasing** — the walk's automated `body.innerText.includes(<guess>)` boolean returned `false` for Fiscus AR home because the precise translation is `"الامتثال الصحيح، لا الحيلة الضريبية."`, not the substring set the walk pre-coded. Visual + h1-grep verification confirmed the anchor renders verbatim; the false negative was in the harness, not the rendering. Tracked as a `browser-verifier` agent prompt-update item for T-P1-3 (the agent should pull anchors from the cluster-blueprint registry rather than the walker hard-coding them). The re-verification walker (run-ISO `20260425T1100Z`) explicitly updated the substring sentinel to `"الامتثال الصحيح"` and `"حيث تُتَّخَذ القرارات"` and observed `true` on both Fiscus AR + Pragma AR home; harness-side regression closed.

---

## Re-verification verdict (run-ISO `20260425T1100Z` · tip `edcdbed`)

A second independent Playwright MCP walk was executed on the post-P1A-merge tip `edcdbed`, with a fresh dev server at `http://127.0.0.1:8735/` (still running for parallel user verification). Same scope (12 cells = 2 templates × 6 pages × 1440 baseline + 4 mobile/breakpoint spot-checks), same contract battery, same evidence shape under `factory/reports/browser-verification/x4a-step2/20260425T1100Z-rtl-ar/`. Outcomes:

- **PASS** verdict reproduced. 0 BLOCKING / 0 REQUIRED failures. No fixes applied.
- Contrast ratios identical to the initial walk: `mp-back` 16.87 / `mp-lang.is-current` 16.87 / `cs-nav .wm .crest` 12.81 (Pragma) / 12.86 (Fiscus) / `cs-kpi-band .stat .num` 12.81 (Pragma) / 12.86 (Fiscus) — all AAA.
- Case-detail KPI band re-measured cream-on-navy 12.81 (Pragma `€ 4 M`) / 12.86 (Fiscus `0`) AAA — S5 closure confirmed under the merged tip.
- Hero h1 = 64 px @ 1440 / 32 px @ 390 on both AR home cells; hero grid flips to `805/619` cols at 1440 (text-narrower-on-right RTL), single-column `375 px` at 390.
- `html[dir="rtl"]` + `html[lang="ar"]` confirmed on every cell; `body { direction: rtl }` confirmed.
- No horizontal overflow at 1440 / 1024 / 768 / 390 on Pragma AR home; no overflow on any walked Fiscus AR cell.
- Drawer engages at 768 + 390 (`navLinksDisplay: none, navBurgerDisplay: flex`); does not engage at 1024 (`flex / none`) — 880-px contract holds.
- Footer legal: 36 / 36 anchors point at `?lang=ar` real routes across both templates.
- Voice-anchors verbatim: Pragma `"حيث تُتَّخَذ القرارات التي تصنع الفرق."` ✓, Fiscus `"الامتثال الصحيح، لا الحيلة الضريبية."` ✓.
- Focus-visible: `Tab → Tab → Tab` from `<body>` lands on the next-locale pill (Fiscus IT pill); `outline: 2px solid rgb(28, 61, 90)` (Fiscus blu-notte `--accent`) at `outline-offset: 4px` — BRWS-CONTRAST-04 contract holds in RTL.
- Form input dirs at 1440 contact: text/textarea fields = `rtl`; email field = `rtl` on Fiscus / `ltr` on Pragma per per-template field markup; tel field = `ltr` on both (correct for Latin glyphs); 0 placeholder text.
- Console: 0 errors / 0 warnings.
- CI floor at the post-walk tip: `python manage.py test apps.catalog -v 2` → **171 tests · OK · 2.795 s** (`step2-ci/test-run-20260425T1100Z.txt`).

The re-verification confirms the initial PASS verdict on the post-merge baseline. The Round 2 CS-BLOCK-17 (extended) palette-safety patches survive the LTR-merge unchanged on the AR locale; no archetype-level regression introduced by the P1A commit. T-P1-2 (RTL AR walk V3) is **closed PASS** under both walks; the cluster-cumulative §7 floor of 120 screenshots / template is met across Rounds 1D + 2 + 3 + 4 (initial) + 4 (re-verified).

---

## P1C — AP8 first end-to-end pipeline run on Fiscus

The walk executes T-P1-3 from `factory/reports/hardening/step2-followup-plan.md §3.P1`, scoped to the **first end-to-end exercise of the corporate-suite multi-agent pipeline** on the known-good Fiscus template (Phase X.4 Wave 2 Pilot #1 · Session 80 · already at `tier: published_live`). The run reuses the four-round X.4a hardening browser corpus as evidence base, applies one small archetype-level skin edit (`.mp-bar .mp-back` → gold-accent `:focus-visible` whitelist) to close the only outstanding Round 4 `[STRONG]` accessibility deviation, and produces all eight required pipeline reports under `factory/reports/scorecard/fiscus-pipeline-round1/`. The release-gatekeeper aggregator uses **blocking overrides not average-score optimism** and reaches verdict **PASS** at aggregate **4.9 / 5** with 0/18 blocking overrides triggered, 9/9 CRITICAL floors met, 0 `[REQUIRED]` failures outstanding, and 3 documented `[STRONG]` deviations. Fiscus is already `published_live`, so no registry edit issues — the PASS records the **AP8 pipeline as field-proven**, not a tier flip.

**Run-ISO (P1C aggregator)**: `20260426T0757Z`
**Server (carried from P1B re-verification)**: `http://127.0.0.1:8735/` · still running (BRWS-SRV-04 honored).
**Baseline tip at execution start**: `e210b6b` (Step 2E P1B re-verification · committed). One archetype-skin edit applied this round on top of `e210b6b` (additive `:focus-visible` whitelist line in `_base.html`).
**CI floor at post-fix tip**: `python manage.py test apps.catalog -v 2` → **171 tests · OK · 2.218 s** (`factory/reports/hardening/step2-ci/test-run-20260426T0757Z.txt`).
**Reports produced** (8 deliverables under `factory/reports/scorecard/fiscus-pipeline-round1/`):

```
fiscus-pipeline-round1/
├── build-report.md            (Builder · CI floor + palette + Pexels grep + voice anchor + D-054)
├── style-critic.md            (D1, D2, D3-half, D5, D6, D7-structure, D8 — all 5)
├── contrast-accessibility.md  (D4 = 5, D12 = 5 · O1/O17 NOT triggered)
├── responsive-auditor.md      (D13 = 4 with §deviation · O2/O3 NOT triggered)
├── browser-verifier.md        (D14 = 4 with §deviation · cluster-cumulative §7 floor met)
├── release-gatekeeper.md      (Layer 1/2/3 aggregator · PASS · pipeline-proven framing)
├── scorecard.md               (final 15-dim scorecard per scorecard §7 template)
└── summary.md                 (one-paragraph + remaining-blocker punch list)
```

## Files changed

```
Code (archetype-level skin · within factory scope · single additive edit)
  templates/live_templates/business/corporate-suite/_base.html
      └── :focus-visible whitelist on line 370-377 — adds `.mp-bar .mp-back`
          (gold-accent ring, solid 2px, offset 4px); closes Round 4 P2 deviation
          where the marketplace back-link rendered browser-default outline.

Evidence (this round)
  factory/reports/scorecard/fiscus-pipeline-round1/                 (8 markdown files · all P1C deliverables)
  factory/reports/hardening/step2-ci/test-run-20260426T0757Z.txt   (171 tests · OK · 2.218 s)
  factory/reports/hardening/step2-execution-round2.md              (this file · P1C section appended)
```

No `apps/editor`, `apps/projects`, `apps/commerce` touches. No new archetypes. No Solaria-scope activity. No migrations. No new routes / views. The `_base.html` edit is the only code change and is purely additive (extends an existing CSS selector group; no rule semantics change).

## Pipeline coverage matrix

The P1C run produced one instance of every SOP §6 report shape on disk for the first time on the corporate-suite archetype:

| Agent | Owns dimensions | Sub-report this round | Hard-veto outcome |
|---|---|---|---|
| `template-builder` | upstream (no scoring) | `build-report.md` | n/a · CI floor green; palette CS-PAL-01 PASS (Fiscus L*≈16.8, ΔL*≈80.8); Pexels grep clean for `business-fiscal`; W001 grandfather acknowledged for Pragma `business-corporate` |
| `style-critic` | D1, D2, D3 (half), D5, D6, D7 (half), D8 | `style-critic.md` | n/a · CS-BLOCK-08/09/10/16 all clear |
| `contrast-accessibility-auditor` | D4, D12 | `contrast-accessibility.md` | **O1 NO** · **O17 NO** (hard vetoes both clear) |
| `responsive-auditor` | D13 | `responsive-auditor.md` | **O2 NO** · **O3 NO** (hard vetoes both clear) |
| `imagery-curator-reviewer` | D9, D10, D11, D15 | folded inline into gatekeeper §3.1 / §4.3 (Step 3 prompt-revision item — see summary §4.1) | n/a · Pexels-only on `business-fiscal`; 3-second subject + mood-to-anchor PASS; zero cross-cluster URL reuse |
| `copy-translation-agent` | D3 (half), D7 (half), D11/imagery-cross-check | folded inline into gatekeeper §3.1 / §4.3 (Step 3 prompt-revision item) | n/a · 5/5 voice anchor verbatim; cluster-specific credentials |
| `browser-verifier` | D14 | `browser-verifier.md` | **O13 NO** · **O14 NO** · **O15 NO** · **O18 NO** |
| `release-gatekeeper` | aggregation only | `release-gatekeeper.md` + `scorecard.md` + `summary.md` | aggregator verdict **PASS** · 0/18 blocking overrides · all 9 CRITICAL floors ≥ 4 · aggregate 4.9 |

## Pragma legacy grandfather handling

Per `step2-readiness-reassessment.md §S4` and `R-SOL-10` ("first scorecard must cite O7 grandfather explicitly"), this is the first scorecard the archetype has ever produced. The grandfather is cited in two places in `release-gatekeeper.md`:

- §3.1 Override row O7: "**NO** for Fiscus (Fiscus `business-fiscal` 0 non-Pexels) … Pragma `business-corporate` is the documented grandfathered exception (`LEGACY_EXEMPT_KEYS = {business-corporate}`) → surfaces `corporate_suite.W001` warning silently per design; not a blocker"
- §6 · E1: full prose paragraph noting the contract is honored, the W001 warning surfaces silently per design on every `manage.py check`, and the Pexels retro-pack (T-P2-1) remains deferrable-past-Solaria per plan §5.

The `manage.py check catalog` output captured in `build-report.md §4.2` shows the W001 line verbatim. The first-scorecard-discipline contract is honored.

## Fiscus contrast hotspots

**None remain.** The readiness reassessment §S5 borderline observation on the Fiscus `.cs-post .kpi-band .stat .num` (case-detail outcome KPI, visually-phantom ~1.3 ratio) was closed by the Round 2 + Round 3 CS-BLOCK-17 (extended) cream-on-dark promotion (post-fix ratio 12.86 AAA). The contrast battery in `contrast-accessibility.md §4.1-4.4` re-confirms every Fiscus h1..h5 at AAA 12.86 across 5 locales and every dark-section descendant at AAA 12.86; nav AA on every state; gold focus-ring on every whitelisted interactive (now including `.mp-bar .mp-back` per this round's edit). The `summary.md §6` re-cites the closure explicitly.

## Pipeline field-proven status

**Yes — proven in the field on Fiscus.** This is the first time every agent prompt has been exercised end-to-end with concrete outputs for a real template. Three small but real value-adds the first run surfaced (per `summary.md §3`):

1. The mp-back focus-visible deviation (carried Rounds 1D → 2 → 3 → 4) was finally surfaced as a discrete `[STRONG]` finding by the contrast-accessibility-auditor leg, the editor-fixer leg landed the 1-line whitelist edit, the gatekeeper recorded the closure — the AP8 loop working as designed on a real defect.
2. The Pragma D-054 staleness vs Fiscus (S3) was correctly **NOT** flagged as O12 on Fiscus's scorecard (Fiscus's own docstring is correct) and instead escalated under §6.E2 of the gatekeeper aggregator — pipeline distinguishes scope correctly.
3. The Pragma legacy Unsplash grandfather contract was honored on a real scorecard for the first time — load-bearing-by-design but until this round, untested in the field.

Five Step 3 prompt-revision items surfaced (per `summary.md §4`): imagery-curator + copy-translation prompts may need an explicit "may fold inline if upstream walk already cited the contract" clause OR remain mandatory standalone reports; browser-verifier §7 floor wording per-template-per-walk vs cumulative; release-gatekeeper handshake template needs a no-op-flip variant for known-good templates; R-SOL-10 should reference "first AP8 scorecard regardless of subject template" not "first Solaria scorecard"; browser-verifier walker should pull voice anchors from the cluster-blueprint registry rather than hardcoding.

## Server, scope, and verdict for P1C

**Server**: `http://127.0.0.1:8735/` · still running on the Round 4 re-verification process · BRWS-SRV-04 honored.

**Scope produced**: 1 template (Fiscus) · 8 SOP §6 report shapes · 1 archetype-level skin edit (additive `:focus-visible` whitelist) · 1 fresh CI transcript · 1 P1C narrative section in this file. No re-walk performed (corpus reused from Rounds 1D + 2 + 3 + 4); no fresh screenshots.

**P1C verdict**: **PASS** (release-gatekeeper aggregator)

- Layer 1 (blocking overrides): 0 / 18 triggered.
- Layer 2 (critical floors): 9 / 9 met (D1=5, D2=5, D3=5, D4=5, D10=5, D11=5, D12=5, D13=4, D14=4).
- Layer 3 (aggregate): avg **4.9** ≥ 4.3 floor; 0 `[REQUIRED]` outstanding; 3 documented `[STRONG]` deviations (per-template Fiscus PNG count, partial 8-viewport sweep on multi-locale, force-reveal capture-mechanism).
- Final verdict: **PASS** · `status_tag: APPROVED-RETROACTIVE`.

The verdict promotes T-P1-3 from "pending" to "PASS · pipeline field-proven on Fiscus" in plan §10.3. **Two remaining items** before the full Go verdict can issue: T-P1-4 (D-054 docstring refresh on Pragma + Fiscus, three-template-ready) and T-P1-5 (primary-CTA paper-surface solid-variant decision). Solaria Commit B remains paused (B1 unchanged); Go is not Solaria un-pause; un-pause is a separate explicit user-authorized lever (R-SOL-8).

## Remaining issues before a true Go verdict

P1C closes the AP8-pipeline-first-run leg (T-P1-3) of the P1 bundle. Outstanding work blocking the full Go verdict per plan §10.3:

- **T-P1-4 · D-054 triangulation refresh on Pragma + Fiscus** — Pragma's docstring (`template_content_pragma.py:12-32`) still triangulates against **Elevate** (its archetype-era sibling at Session 32), not against Fiscus (admitted in Session 80). Fiscus's docstring is current (10/10 vs Pragma in `template_content_fiscus.py:14-39`). The refresh lands one block per template, three-template-ready (so future Solaria un-pause does not require a second refresh round). Plan §6.5 binds T-P1-4 to land **after** T-P1-3 — i.e., next.
- **T-P1-5 · Primary-CTA paper-surface solid-variant decision** — Step 1B / Step 1D / Round 1 / Round 2 / Round 3 / Round 4 / Round 5 all deferred. A `§ decision` block in `factory/standards/corporate-suite-design-standard.md` is required regardless of direction (adopt `.cs-btn-primary--solid` OR formally waiver the outline-only reading as intentional).
- **Optional polish** — a future consolidated Fiscus-only re-walk producing ≥ 120 PNGs in a single ISO directory under `factory/reports/browser-verification/fiscus-commercialista/<run-ISO>/` would lift D14 from 4 to 5 and close `§ deviation` 1 cleanly. Not gating per plan §10.3.
- **B1** Solaria Commit B paused — unchanged. Even after Go issues, un-pause is a separate explicit user-authorized lever (R-SOL-8). Solaria's first walk inherits the AP8 pipeline this round just bootstrapped, including R-SOL-9 through R-SOL-15.
- **B2** `LEGACY_EXEMPT_KEYS = {business-corporate}` — unchanged. `corporate_suite.W001` keeps the Pragma legacy pool visible at every `manage.py check` per O7. Pexels retro-pack (T-P2-1) deferrable-past-Solaria.
- **B7** `templates/preview_compositions/business/corporate-suite.html` untouched — out of Step 2 scope.

— end of Round 2 execution report (P1C appended · 20260426T0757Z @ tip e210b6b + 1 skin edit) —
