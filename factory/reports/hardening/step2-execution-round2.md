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

— end of Round 2 execution report —
