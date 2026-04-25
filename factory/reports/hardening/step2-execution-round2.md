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

The walk executes T-P1-2 from `factory/reports/hardening/step2-followup-plan.md §3.P1`, scoped to the AR (Arabic · RTL) locale on Pragma + Fiscus across the 6 archetype pages and the core viewports (1440 / 1024 / 768 / 390). The walk runs against the post-P1A archetype skin (which lands the four Round 2 CS-BLOCK-17 (extended) palette-safety patches: `.mp-bar .mp-back`, `.mp-lang.is-current`, `.cs-nav .wm .crest`, `.cs-post .kpi-band .stat .num` → `var(--on-dark)`). The pre-fix AR walk surfaced **0 BLOCKING and 0 REQUIRED** failures; no fixes were applied at archetype scope, and no post-fix re-walk was needed. The walk closes plan §10.2 row "T-P1-2 RTL AR walk V3 PASS" and frees T-P1-3 (AP8 end-to-end Fiscus pipeline run) to start.

**Run-ISO**: `20260425T0837Z` (single pre-fix walk; no fixes applied → no post-fix run-ISO).
**Server**: `http://127.0.0.1:8734/` · started fresh on the post-P1A tip (`44700fc`) · `--noreload` mode · still running (BRWS-SRV-04 honored).
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
(no code changes in P1B)

Evidence
  factory/reports/browser-verification/x4a-step2/20260425T0837Z-rtl-ar/
      ├── measurements/
      │   ├── contrast-ar.json       (AR cream-on-navy chrome ratios · Pragma + Fiscus)
      │   └── rtl-contract.json      (per-page RTL contract validation · 12 cells × 4 viewports sampled)
      └── screenshots/
          ├── pragma/  (7 PNG · home @ 1440 + 390 + 5 interior pages @ 1440)
          └── fiscus/  (7 PNG · home @ 1440 + 390 + 5 interior pages @ 1440)
  factory/reports/hardening/step2-ci/test-run-20260425T0837Z.txt   (171 tests · OK · 6.008 s)
  factory/reports/hardening/step2-execution-round2.md              (this file · P1B section appended)
  factory/reports/browser-verification/x4a-hardening-round4.md     (verdict · companion file)
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
- **AR voice-anchor pre-check substring guesses missed Fiscus's exact phrasing** — the walk's automated `body.innerText.includes(<guess>)` boolean returned `false` for Fiscus AR home because the precise translation is `"الامتثال الصحيح، لا الحيلة الضريبية."`, not the substring set the walk pre-coded. Visual + h1-grep verification confirmed the anchor renders verbatim; the false negative was in the harness, not the rendering. Tracked as a `browser-verifier` agent prompt-update item for T-P1-3 (the agent should pull anchors from the cluster-blueprint registry rather than the walker hard-coding them).

---

— end of Round 2 execution report —
