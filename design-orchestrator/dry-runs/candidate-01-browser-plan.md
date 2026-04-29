# Candidate-01 · Browser-live review plan · DRY RUN

**Status**: dry-run · the walk-plan a real workflow A.7 + workflow C.4 would execute
**Reference rubric**: `factory/standards/corporate-suite-browser-rubric.md`
**Canonical gate doc**: `design-orchestrator/BROWSER_QUALITY_GATE.md`
**Anti-pattern**: `factory/references/anti-pattern-library.md`
**Walk artefact root** (would-be): `factory/reports/browser-verification/continua-stewardship/`

The walk is the SHIP SIGNAL. CLI green is a lower bound. If Continua were real, no flip from `draft` to `published_live` happens until everything below is on file.

---

## 1 · Pages × locales × viewports

### Pages (CS-BROWSER-01 · cluster scope)
1. `home` — `/templates/continua-stewardship/live/`
2. `about` — `/templates/continua-stewardship/live/chi-siamo/` (timeline opener · NOT wall-of-text · CS-COMP-06)
3. `services` — `/templates/continua-stewardship/live/custodia/` (4 pillars expanded)
4. `case_study_list` — `/templates/continua-stewardship/live/mandati/`
5. `case_study_detail` — `/templates/continua-stewardship/live/mandati/<slug>/` (with `continuity-context` slot)
6. `contact` — `/templates/continua-stewardship/live/contatti/` (form gate · scope + orizzonte + struttura)

### Locales
- **Workflow A (initial draft)**: `[it]` only · D-102 cadence
- **Workflow C (multilingual rollout)**: `[en, fr, es, ar]` added in a separate pass per `template-multilingual-orchestrator.md`
- **Total scope at LIVE flip**: 5 locales × 6 pages = 30 page surfaces

### Viewports (CS-RESPONSIVE-02)
6 viewports per page:
- `1920` desktop wide
- `1440` desktop standard
- `1280` desktop narrow (object-led hero crop risk)
- `1024` tablet landscape (chrome compaction edge)
- `768` tablet portrait (footer pre-stack)
- `390` mobile (hero stacking · CS-HERO-07 · footer 1-col · CS-FOOT-05)

**Total captures at full rollout** (all locales · all pages · all viewports + RTL parity walk):
- Workflow A: 6 pages × 6 viewports × 1 locale = **36 captures** (IT)
- Workflow C: 6 pages × 6 viewports × 4 locales = **144 captures** (EN/FR/ES/AR)
- AR RTL parity walk: extra 6 captures focused on logical-property correctness
- Reduced-motion walk: 1 page × 1 viewport × 1 locale × `prefers-reduced-motion: reduce` = 1 capture (additional)
- **Workflow A total**: 36 + 1 = **37**
- **Cumulative at LIVE flip**: 37 + 144 + 6 = **187 captures**

---

## 2 · Per-viewport premium checks

| Viewport | Critical premium check | Likely failure mode | Pass criterion |
|---|---|---|---|
| 1920 | Hero 55/45 split keeps generous left-column whitespace · KPI band reads as one editorial line | KPI band stretches and tabular numerals misalign | Padding 100×72 holds · KPIs aligned via `font-variant-numeric: tabular-nums` · accent count ≤ 3 per viewport (CS-PAL-05) |
| 1440 | Object-led hero photo crops to keep brass-cabinet detail in frame | Photo crop chops the brass focal | Brass detail stays in middle 40% of right column · DoF on brass intact |
| 1280 | First narrow desktop · pillars 4-up still reads spaced | Pillars compress to 4 thin columns · text wraps awkwardly | Each pillar card has min-width sufficient for 2-line h3 |
| 1024 | Tablet landscape · navbar 5 links + locale + CTA all visible | Locale pill collapses behind hamburger | Either 5 links + locale + CTA all fit OR drawer triggered cleanly |
| 768 | Tablet portrait · footer not yet 1-col · governance-cycle 3 cells stack to 2+1 | Mid-strip cells overflow horizontally | No horizontal scroll · cells stack via flex-wrap / grid auto-fit |
| 390 | Hero stacks to single column (CS-HERO-07) · footer 1-col (CS-FOOT-05) · drawer hamburger active (X.4a step1d hardening) | Hero stays horizontal (cluster R2 fault line) · drawer fails to open | Hero `grid-template-columns: 1fr` at ≤720 · footer 1-col · drawer opens on tap with `:focus-visible` brass ring |

**Anti-pattern detector run on every viewport**:
- AP1 palette polarity (cream-on-cream collapse) — Solaria's incident
- AP2 hero stays horizontal at ≤720 — cluster R2 fault line
- AP4/AP5 imagery-semantic mismatch — object-led hero crop incoherence at 1280/1024
- AP7 `--primary-2` hardcoded — must NOT appear in Continua's skin
- AP11 dark-on-dark pockets in KPI band or CTA-closer
- AP12 reduced-motion JS wiring regression
- E1 focus-ring branding regression (must show brass, not browser-default blue)

---

## 3 · Per-page premium checks

### Home
- Hero h1 italic falls on `generazioni` only (one em-wrap · CS-TYPE-02)
- Hero credit overlay reads `Custodi del mandato · Iscrizione Albo Trustees` (NOT `Direzione, Anno fondazione`)
- Stewardship-horizon-strip below CTA shows three cells with tabular numerals
- Pillars 4-up shows `Custodia patrimoniale / Governance familiare / Successione strutturata / Compliance fiduciaria` — exact verb-style headings
- KPI band (the ONE dark band) shows 4 stats with `font-variant-numeric: tabular-nums`
- Governance-cycle-strip cells render: `Cadenza CdF · 4 riunioni / anno` · `Audit di continuità · annuale` · `Patto familiare · revisione triennale`
- Sectors-ribbon labelled `Profili familiari` (NOT `Settori di intervento`)
- Leadership cards photo-present · 3 stewards · ages clearly differ across cards
- Cases section labelled `Mandati in continuità` · each card carries duration marker
- CTA-closer dark band restates voice anchor verbatim · single filled-brass CTA
- Editor affordances confirmed hidden (no `[click-to-edit]` halos · CS-MARKET-01)

### About (`chi-siamo`)
- Opens with timeline (NOT a wall-of-text "Our Story" · CS-COMP-06)
- Voice anchor restated · em-word preserved
- Senior + co-steward portraits at slot 2/3 visible
- Whistleblowing link in footer reads as legal-row first-class element

### Services (`custodia`)
- 4 pillars expanded into discrete sections · each section uses unique imagery surface (slot 1 / 4 / 5 / hero crop)
- No two adjacent expanded sections share function (CS-RHYTHM-04)

### Case study list (`mandati`)
- 4 anonymized mandates · each card has duration marker + scope segment + audit cadence label
- "Riconoscimenti istituzionali" trust band visible (NOT "Aziende sponsor recenti")

### Case study detail (`mandati/<slug>/`)
- KPI strip + narrative + `continuity-context` slot + `next-mandate` (4-section detail order · differs from Pragma/Fiscus's 4-section · matches Solaria's 4-section count but new slot content)
- `continuity-context` slot shows multi-year timeline + 3+ governance milestones (anonymized)
- Voice anchor restated at section closer

### Contact (`contatti`)
- Form layout: form-left + coordinates-right · stacks at 880px (CS-COMP-05)
- Form fields: scope familiare (textarea) · orizzonte temporale (select · 5y/10y/25y/multi-gen) · struttura attuale (select · 5 options)
- NO P.IVA + CF fields (Fiscus collision avoided)
- CTA on form button reads `Avvia un dialogo di mandato`
- Coordinates panel shows whistleblowing link prominent

---

## 4 · Contrast checks (CS-PAL-01 · CS-HERO-03 · `:focus-visible`)

### Numeric contrast targets
| Surface pair | WCAG target | Computed |
|---|---|---|
| h1 (pine `#0F3A30`) on cream paper (`#F4ECDB`) | AAA (≥ 7:1) on hero | ≈ 13.2:1 ✓ (computed-style verification at A.6 contrast report) |
| body (ink `#1F2A2C`) on cream | AAA (≥ 7:1) | ≈ 14.8:1 ✓ |
| KPI band — cream type on pine | AA (≥ 4.5:1) for figures | ≈ 11.5:1 ✓ |
| Brass accent (`#B0875E`) on pine — focus ring + CTA fill in dark | AA (≥ 4.5:1) for stroke | requires verification at A.6 (estimated ≈ 4.8:1; if marginal, darken brass or thicken focus ring) |
| Pewter secondary (`#5A6E78`) on cream — eyebrow labels | AA (≥ 4.5:1) | requires verification (estimated ≈ 5.3:1) |

### `:focus-visible` walk
- Tab through navbar from skip-link → 5 nav links → locale-pill links → trailing CTA
- Every interactive element shows brass ring (2px outline · 4px offset) — never browser-default blue
- Tab through hero CTA → meta-strip if interactive → first pillar card
- Tab through form fields on contatti — every input shows brass ring on cream background

### Reduced-motion walk
- `@media (prefers-reduced-motion: reduce)` on
- All `[data-lm]` staggered reveals → static
- Marquee → static (no horizontal drift)
- Hero text fade-in → instant
- Confirm zero JS-driven motion remains active

### Dark-on-dark pocket scan (AP11)
- KPI band: cream type on pine — passes
- CTA-closer dark band: confirm CTA label reads cream on pine, brass border on pine — no element accidentally inherits primary-on-primary
- Footer: cream type on pine — passes; check secondary footer text (legal row) doesn't inherit a darker variant

---

## 5 · Imagery coherence checks (live DOM, not pack metadata)

The pack is approved at A.3 against 1600px reference. The walk re-verifies the rendered crops at the actual rendered viewport.

| Slot | Live-DOM check | Failure mode |
|---|---|---|
| Slot 0 hero | Brass key + cabinet detail still readable as "stewardship object" at 1280 / 1024 / 768 / 390 crops | Crop loses brass focal · reads as "generic warm interior" |
| Slot 1 feature | Open ledger + bookmark ribbon on about.html hero band still reads as "working archive" | Compressed below recognisability at 768 |
| Slots 2/3 portraits | Senior 60s steward visibly older than co-steward 40s · diversity reads at card-size 320×320 crop | Card crop pulls so close that age/diversity blurs |
| Slot 4 detail | Wax-seal letterhead crisp, ribbon visible, no brand text leaks | Detail at thumbnail size loses ceremonial reading |
| Slot 5 ambient | Slate stairwell + brass handrail at dusk reads as "building of substance" not "stairwell, generic" | Crop loses handrail · reads as generic stairwell stock |

**Pexels-only audit on live DOM** (CS-IMG-SRC-01 · BROWSER_QUALITY_GATE §5):
- DevTools → Network → filter Img → confirm every image URL resolves to `images.pexels.com/photos/...`
- No CDN-laundering · no embedded thumbnails from elsewhere
- No Unsplash carve-out (Pragma legacy is the ONLY exception · Continua is new = Pexels-only)

**Cross-cluster URL grep on the live render**:
- For each rendered URL: grep against `business-corporate`, `business-fiscal`, `business-coaching`, and any other cluster pool that exists at flip time
- Zero overlap permitted (CS-IMG-SRC-04)

**Subject coherence test**: open every page at every viewport. For each image, ask "would this still be the right photo here if you were building this template from scratch?" — a no answer is a `[REQUIRED]` finding.

---

## 6 · Multilingual checks

### Per-locale walk pages
Each of EN / FR / ES / AR walks all 6 pages at all 6 viewports — same matrix as IT. The Solaria Pass B precedent (11/11 captures · 0 fixes mid-walk) is the bar.

### Voice anchor per-locale verification
Each locale's hero h1 reads the verbatim translated anchor with italic on the equivalent of `generazioni`:

| Locale | Expected h1 | Em-word |
|---|---|---|
| IT | `La continuità di una famiglia si misura in <em>generazioni</em>.` | `generazioni` |
| EN | `A family's continuity is measured in <em>generations</em>.` | `generations` |
| FR | `La continuité d'une famille se mesure en <em>générations</em>.` | `générations` |
| ES | `La continuidad de una familia se mide en <em>generaciones</em>.` | `generaciones` |
| AR | `استمرارية العائلة تُقاس بـ<em>الأجيال</em>.` | `الأجيال` (italic substitute via Kufi weight or oblique fallback) |

**Walk verifies**: `<em>` wraps the correct word in every locale (translator did not move it to a different word — the F2 / CS-EXEC-01 risk Solaria flagged).

### AR RTL parity walk (additional 6 captures)
- `dir="rtl"` on `<html>` confirmed
- Layout flips correctly via logical properties (no duplicated CSS) — CS-RESPONSIVE-08
- Heading swaps to Noto Kufi Arabic — CS-TYPE-06
- Body swaps to Amiri — CS-TYPE-06
- Latin wordmark "Continua" preserved in navbar + footer — CS-NAV-06 / CS-FOOT-03
- Tabular numerals on KPIs render Latin digits (Western Arabic numerals) for cluster consistency — CS-TYPE-03
- Letter-spacing on uppercase eyebrow labels resets to 0 (CS-TYPE-05 RTL reset 0.22em → 0)
- Locale switcher pill works with `lang+dir` per link — CS-NAV-03

### Per-locale form gate
The `/contatti/` form select options translate per locale:
- IT: 5y / 10y / 25y / multi-generazionale
- EN: 5y / 10y / 25y / multi-generational
- FR: 5 ans / 10 ans / 25 ans / multi-générationnel
- ES: 5 años / 10 años / 25 años / multi-generacional
- AR: ٥ سنوات / ١٠ سنوات / ٢٥ سنة / متعدد الأجيال (or Western Arabic numerals if cluster convention is Western digits — confirm at terminology lock)

### Whistleblowing link per-locale
- IT: "Whistleblowing"
- EN: "Whistleblowing"
- FR: "Lanceur d'alerte"
- ES: "Canal de denuncia"
- AR: "الإبلاغ عن المخالفات"

All 5 routes return 200 in staff session (Solaria Pass C precedent — internal-link 200 audit closed the `&preview=1` leak). Walk runs the same 200-audit grep pre-flight.

---

## 7 · Release-gate expectations

The orchestrator will not request Commit B (LIVE flip) until ALL of the following are TRUE on file. (Commit A — `tier=draft` IT-only — has a narrower set; the LIVE flip is the binding gate.)

### Layer 1 · CLI + standards (precondition only)
- [ ] `python manage.py test apps.catalog` — green
- [ ] `python manage.py test apps` — green (full suite)
- [ ] `generate_previews` — succeeds for `continua-stewardship`
- [ ] `scripts/check_imagery_pack.py` (or equivalent) — pack passes
- [ ] Pexels-only grep on the pack file — clean
- [ ] Cross-cluster URL grep on the pack — clean

### Layer 2 · Critique + walk (the ship signal)
- [ ] Style-critique against `corporate-suite-design-standard.md` — 0 open `[BLOCKING]`
- [ ] Contrast/accessibility report at all 6 viewports · all 5 locales — PASS
- [ ] Responsive report at all 6 viewports — no horizontal scroll · footer stacks at 720
- [ ] IT walk verdict — PASS · 36 captures on file · `walk-it.md` complete
- [ ] EN walk verdict — PASS
- [ ] FR walk verdict — PASS
- [ ] ES walk verdict — PASS
- [ ] AR walk verdict — PASS · RTL parity captures + 6 additional
- [ ] Reduced-motion verdict — PASS
- [ ] Editor affordances confirmed hidden across home + 5 secondary on `/live/` (CS-MARKET-01)
- [ ] AI-slop red-flag detector clear (`reference-pack §9` — 13 items)

### Layer 3 · Aggregation + handshake
- [ ] Scorecard filled · Layer 1/2/3 stamped · grade ≥ 4.50/5
- [ ] User-handshake artefact filed · binary SHIP/HOLD answered SHIP
- [ ] Distinctness re-confirmed at flip time — still ≥ 4/5 vs every sibling
- [ ] Live DOM matches planner brief (no drift introduced post-A.5)
- [ ] Pexels-only re-confirmed on live render at every locale
- [ ] No deviation note (`§ deviation`) flags an unresolved `[BLOCKING]` rule
- [ ] No conservative override invoked

### Walk freshness gate
- All walk verdicts ≤ 30 days old at flip time (`BROWSER_QUALITY_GATE §3`)
- If a verdict is stale, re-walk the affected locale before the orchestrator requests Commit B

### Stop conditions during the walk (HALT, not slow)
Per `template-orchestrator-master.md §4`:
1. Distinctness collision discovered live (≤ 3/5 vs any sibling) → workflow B re-spec
2. Non-Pexels URL on live render → workflow B fix · NO LIVE flip
3. Hero h1 cream-on-cream or any near-mono ≤ 4.5:1 → `[BLOCKING]` · workflow B
4. Two adjacent sections share function → workflow B
5. AI-slop tell visible (Inter on h1 / purple gradient / cards-in-cards / etc.) → workflow B
6. Editor affordance leaks into `/live/` → workflow B
7. Mobile ≤ 720 shows horizontal scroll OR hero still horizontal → workflow B
8. Locale switcher does not change `lang` + `dir` → workflow B
9. AR RTL layout requires duplicate CSS instead of logical properties → workflow B
10. "Remove the studio name" test fails (page reads as a generic) → workflow B re-spec

Any of (1-10) → orchestrator does NOT request Commit B. Period.

---

## 8 · The walk artefact tree (would-be)

```
factory/reports/browser-verification/continua-stewardship/
  it/2026-MM-DD/
    home-1920.png · home-1440.png · home-1280.png · home-1024.png · home-768.png · home-390.png
    about-* · services-* · case-list-* · case-detail-* · contact-*  (× 6 viewports)
    walk-log-it.md
    contrast-it.md
    responsive-it.md
    style-critique-it.md
    reduced-motion-it.md
  en/2026-MM-DD/  · same tree
  fr/2026-MM-DD/  · same tree
  es/2026-MM-DD/  · same tree
  ar/2026-MM-DD/  · same tree + rtl-parity-ar.md (6 extra captures)

factory/reports/<archetype>/continua-stewardship/
  intake.md
  planner-brief.md
  pack-report.md
  copy-it.md
  build-summary.md
  critique-style.md
  critique-contrast.md
  critique-responsive.md
  walk-it.md
  scorecard.md
  user-handshake.md
  multilingual-2026-MM-DD/
    preflight.md
    copy-en.md · copy-fr.md · copy-es.md · copy-ar.md
    walk-en.md · walk-fr.md · walk-es.md · walk-ar.md
    multilingual-summary.md
  release-2026-MM-DD/
    release-decision.md
```

This tree is the template's PERMANENT FILE per `single-template-workflow.md §3`. It is not session scratch.

---

## 9 · One-paragraph summary of the walk plan

If `continua-stewardship` were a real candidate, the orchestrator would block any LIVE flip until: 6 pages × 6 viewports × 5 locales (with an extra AR RTL parity walk + reduced-motion sweep) produce 187 captures across 5 locales, every walk verdict files PASS against the cluster rubric, the contrast / responsive / style-critique / Pexels-only / cross-cluster-grep / AI-slop / "remove-studio-name" / editor-affordance-on-live / form-gate-translation / focus-ring-brass-not-blue / dark-on-dark / AR-logical-properties / heading-italic-on-correct-em-word / mid-strip-cell-stack-at-720 checks all clear, the scorecard reads ≥ 4.50/5 across Layers 1-2-3, and the user signs the handshake binary SHIP. Any single failure routes back through workflow B narrowly, no scope expansion, re-walk on the affected dimension only. The 30 minutes the walk takes is the 30 minutes that would have caught Solaria's cream-on-cream defect — non-negotiable.
