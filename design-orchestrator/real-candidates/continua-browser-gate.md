# Continua · Browser-live gate · REAL CANDIDATE

**Status**: real candidate · final browser-live gate · the workflow A.7 + workflow C.4 walk plan that gates Commit A and Commit B
**Reference rubric**: `factory/standards/corporate-suite-browser-rubric.md`
**Canonical gate doc**: `design-orchestrator/BROWSER_QUALITY_GATE.md`
**Anti-pattern library**: `factory/references/anti-pattern-library.md`
**Companion files**: `continua-intake.md` · `continua-build-brief.md` · `continua-distinctness-proof.md`
**Walk artefact root** (would-be): `factory/reports/browser-verification/continua-stewardship/`
**Promotion path on first build**: this file → `factory/reports/corporate-suite/continua-stewardship/walk-plan.md`

The walk is the ship signal. CLI green is a lower bound. No flip from `draft` to `published_live` happens until everything below is on file. Solaria's `e8f38b5` defect (1148 lines · 506 tests passing · cream-on-cream h1 on the live page) is the failure mode this gate exists to prevent.

---

## 1 · Pages × locales × viewports

### Pages (CS-BROWSER-01 · cluster scope)

| # | Page | URL (live) | What it must render |
|---|---|---|---|
| 1 | `home` | `/templates/continua-stewardship/live/` | full home · 8-section sequence per build-brief §6 |
| 2 | `about` | `/templates/continua-stewardship/live/chi-siamo/` | timeline opener (NOT wall-of-text · CS-COMP-06) |
| 3 | `services` | `/templates/continua-stewardship/live/custodia/` | 4 pillars expanded into discrete sections |
| 4 | `case_study_list` | `/templates/continua-stewardship/live/mandati/` | 4 mandates · "Mandati in continuità" label |
| 5 | `case_study_detail` | `/templates/continua-stewardship/live/mandati/<slug>/` | kpi-strip + narrative + `continuity-context` + `next-mandate` |
| 6 | `contact` | `/templates/continua-stewardship/live/contatti/` | form-left + coordinates-right · scope + orizzonte + struttura |

### Locales

- **Workflow A (initial draft)**: `[it]` only · D-102 cadence
- **Workflow C (multilingual rollout)**: `[en, fr, es, ar]` added in a separate pass per `template-multilingual-orchestrator.md`
- **Total scope at LIVE flip**: 5 locales × 6 pages = 30 page surfaces

### Viewports (CS-RESPONSIVE-02)

6 viewports per page:
- `1920` desktop wide
- `1440` desktop standard
- `1280` desktop narrow (object-led hero crop risk · Risk 2 verification)
- `1024` tablet landscape (chrome compaction edge)
- `768` tablet portrait (footer pre-stack · governance-cycle re-stack)
- `390` mobile (hero stacking · CS-HERO-07 · footer 1-col · CS-FOOT-05)

### Capture totals

| Pass | Captures |
|---|---|
| Workflow A · IT walk | 6 pages × 6 viewports = **36** |
| Workflow A · reduced-motion sweep | 1 page × 1 viewport × 1 locale = **1** |
| **Workflow A subtotal** | **37** |
| Workflow C · EN/FR/ES walks | 6 pages × 6 viewports × 3 locales = **108** |
| Workflow C · AR walk | 6 pages × 6 viewports × 1 locale = **36** |
| Workflow C · AR RTL parity walk | extra 6 captures focused on logical-property correctness |
| **Workflow C subtotal** | **150** |
| **Cumulative at LIVE flip** | **187 captures** |

---

## 2 · Per-viewport premium checks

| Viewport | Critical premium check | Likely failure mode | Pass criterion |
|---|---|---|---|
| 1920 | Hero 55/45 split keeps generous left-column whitespace · KPI band reads as one editorial line · 5 brass touchpoints visible (Risk 1 mitigation) | KPI band stretches and tabular numerals misalign · brass touchpoints disappear into pine | Padding 100×72 holds · KPIs aligned via `font-variant-numeric: tabular-nums` · accent count ≤ 3 per viewport (CS-PAL-05) · brass visible at: trailing nav CTA + focus ring + KPI eyebrow tints + pillar underline + cta-closer fill |
| 1440 | Object-led hero photo crops to keep brass-lamp + book detail in frame | Photo crop chops the focal | Lamp + book stays in middle 40% of right column · DoF on lamp/book intact |
| 1280 | First narrow desktop · pillars 4-up still reads spaced · object-led hero coherent (Risk 2 verification) | Pillars compress to 4 thin columns · text wraps awkwardly · hero crop pulls into desk-task framing | Each pillar card has min-width sufficient for 2-line h3 · hero crop keeps room-architectural framing (shelves still readable in soft focus) |
| 1024 | Tablet landscape · navbar 5 links + locale + CTA all visible · governance-cycle 3 cells still horizontal | Locale pill collapses behind hamburger · cycle-strip cells overflow | Either 5 links + locale + CTA all fit OR drawer triggered cleanly · cycle-strip cells stack via flex-wrap with no horizontal scroll |
| 768 | Tablet portrait · footer not yet 1-col · governance-cycle 3 cells stack to 2+1 · leadership 3-card row visible | Mid-strip cells overflow · leadership demographics blur | No horizontal scroll · cells stack via flex-wrap / grid auto-fit · leadership card portraits readable at card-size 320×320 |
| 390 | Hero stacks to single column (CS-HERO-07) · footer 1-col (CS-FOOT-05) · drawer hamburger active (X.4a step1d hardening) | Hero stays horizontal (cluster R2 fault line) · drawer fails to open · object-led hero crops too tight | Hero `grid-template-columns: 1fr` at ≤720 · footer 1-col · drawer opens on tap with `:focus-visible` brass ring · hero photo retains brass focal element |

### Anti-pattern detector run on every viewport

- **AP1** palette polarity (cream-on-cream collapse) — Solaria's incident class
- **AP2** hero stays horizontal at ≤720 — cluster R2 fault line · MUST be addressed BEFORE first build
- **AP4 / AP5** imagery-semantic mismatch — object-led hero crop incoherence at 1280/1024 (Risk 2)
- **AP7** `--primary-2` hardcoded — must NOT appear in Continua's skin
- **AP11** dark-on-dark pockets in KPI band or CTA-closer
- **AP12** reduced-motion JS wiring regression
- **E1** focus-ring branding regression (must show brass, not browser-default blue)

---

## 3 · Per-page premium checks

### Home (`/live/`)

- **Hero**: h1 italic falls on `generazioni` only (one em-wrap · CS-TYPE-02). Hero credit overlay reads `Custodi del mandato · Iscrizione Albo Trustees` (NOT `Direzione, Anno fondazione`).
- **Hero meta-strip**: stewardship-horizon-strip below CTA shows three cells with tabular numerals.
- **Pillars 4-up**: shows `Custodia patrimoniale / Governance familiare / Successione strutturata / Compliance fiduciaria` — exact verb-style headings · brass underline visible on focus.
- **KPI band** (the ONE dark band): shows 4 stats with `font-variant-numeric: tabular-nums` · brass eyebrow tints render.
- **Governance-cycle-strip** (the differentiator beat): three cells, cream paper, render the (eyebrow · figure · context-line) triple — Risk 5 mitigation: each cell shows label + figure + context-line, NOT label + figure alone.
- **Sectors-ribbon**: labelled `Profili familiari` (NOT `Settori di intervento`).
- **Leadership cards**: photo-present · 3 stewards · ages clearly differ across cards · 3 distinct demographics readable at 1920 / 1280 / 768 (Risk 4 verification).
- **Cases section**: labelled `Mandati in continuità` · each card carries duration marker (`4ª generazione · da 12 anni`).
- **CTA-closer**: dark band restates voice anchor verbatim · single filled-brass CTA · the only filled CTA on cream/dark distinct from the outline-only hero CTA.
- **Editor affordances**: confirmed hidden (no `[click-to-edit]` halos · CS-MARKET-01).

### About (`/live/chi-siamo/`)

- Opens with `timeline` (NOT a wall-of-text "Our Story" · CS-COMP-06).
- Voice anchor restated · em-word preserved.
- Senior + co-steward portraits at slot 2/3 visible.
- Whistleblowing link in footer reads as legal-row first-class element.

### Services (`/live/custodia/`)

- 4 pillars expanded into discrete sections · each section uses unique imagery surface (slot 1 / 4 / 5 / hero crop).
- No two adjacent expanded sections share function (CS-RHYTHM-04).

### Case study list (`/live/mandati/`)

- 4 anonymized mandates · each card carries duration marker + scope segment + audit cadence label.
- "Riconoscimenti istituzionali" trust band visible (NOT "Aziende sponsor recenti").

### Case study detail (`/live/mandati/<slug>/`)

- Detail-page order: kpi-strip + narrative + `continuity-context` + `next-mandate` (4-section detail order · differs from Pragma/Fiscus's 4-section · matches Solaria's 4-section count but new slot content).
- `continuity-context` slot shows multi-year timeline + 3+ governance milestones (anonymized).
- Voice anchor restated at section closer.

### Contact (`/live/contatti/`)

- Form layout: form-left + coordinates-right · stacks at 880px (CS-COMP-05).
- Form fields: scope familiare (textarea) · orizzonte temporale (select · 5y/10y/25y/multi-gen) · struttura attuale (select · 5 options).
- NO P.IVA + CF fields (Fiscus collision avoided).
- CTA on form button reads `Avvia un dialogo di mandato`.
- Coordinates panel shows whistleblowing link prominent.

---

## 4 · Contrast checks (CS-PAL-01 · CS-HERO-03 · `:focus-visible`)

### Numeric contrast targets

| Surface pair | WCAG target | Computed estimate |
|---|---|---|
| h1 (pine `#0F3A30`) on cream paper (`#F4ECDB`) | AAA (≥ 7:1) on hero | ≈ 13.2:1 ✓ (computed-style verification at A.6 contrast report) |
| body (ink `#1F2A2C`) on cream | AAA (≥ 7:1) | ≈ 14.8:1 ✓ |
| KPI band — cream type on pine | AA (≥ 4.5:1) for figures | ≈ 11.5:1 ✓ |
| Brass accent (`#B0875E`) on pine — focus ring + CTA fill in dark | AA (≥ 4.5:1) for stroke | requires verification at A.6 (estimated ≈ 4.8:1; if marginal, darken brass or thicken focus ring per Risk 1 fallback) |
| Pewter secondary (`#5A6E78`) on cream — eyebrow labels | AA (≥ 4.5:1) | requires verification (estimated ≈ 5.3:1) |
| Brass eyebrow tints on pine — KPI band labels | AA (≥ 4.5:1) | requires verification at A.6; may need brass darkening for the eyebrow specifically |

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

- **KPI band**: cream type on pine — passes
- **CTA-closer dark band**: confirm CTA label reads cream on pine, brass border on pine — no element accidentally inherits primary-on-primary
- **Footer**: cream type on pine — passes; check secondary footer text (legal row) doesn't inherit a darker variant

---

## 5 · Imagery coherence checks (live DOM, not pack metadata)

The pack is approved at A.3 against 1600px reference. The walk re-verifies the rendered crops at the actual rendered viewport.

| Slot | Live-DOM check | Failure mode | Mitigation reference |
|---|---|---|---|
| Slot 0 hero | Brass lamp + single-book detail still readable as "stewardship object" at 1280 / 1024 / 768 / 390 crops | Crop loses brass focal · reads as "generic warm interior" | Risk 2 mitigation · build-brief §4 rejection rules |
| Slot 1 feature | Open ledger + bookmark ribbon on about.html hero band still reads as "working archive" | Compressed below recognisability at 768 | A.3 curator subject coherence note |
| Slots 2/3 portraits | Senior 60s steward visibly older than co-steward 40s · diversity reads at card-size 320×320 crop | Card crop pulls so close that age/diversity blurs | Risk 4 mitigation · build-brief §10 demographic triple |
| Slot 4 detail | Wax-seal letterhead crisp, ribbon visible, no brand text leaks | Detail at thumbnail size loses ceremonial reading | A.3 curator subject coherence note |
| Slot 5 ambient | Slate stairwell + brass handrail at dusk reads as "building of substance" not "stairwell, generic" | Crop loses handrail · reads as generic stairwell stock | A.3 curator caveat (CAUTION at intake §6.5 — narrow pool · curator authorised first viable swap) |

### Pexels-only audit on live DOM

- DevTools → Network → filter Img → confirm every image URL resolves to `images.pexels.com/photos/...`
- No CDN-laundering · no embedded thumbnails from elsewhere
- No Unsplash carve-out (Pragma legacy is the ONLY exception · Continua is new = Pexels-only)
- (CS-IMG-SRC-01 · `BROWSER_QUALITY_GATE §5.1`)

### Cross-cluster URL grep on the live render

- For each rendered URL: grep against `business-corporate`, `business-fiscal`, `business-coaching`, and any other cluster pool that exists at flip time
- Zero overlap permitted (CS-IMG-SRC-04)

### Subject coherence test

Open every page at every viewport. For each image, ask "would this still be the right photo here if you were building this template from scratch?" — a no answer is a `[REQUIRED]` finding.

### "Remove the studio name" live test (CS-TONE-05)

Reviewer reads the home with the Continua wordmark hidden (DevTools `display: none` on `.cs-wordmark`). The page must still read as a real stewardship family office, NOT as a generic "premium firm." If the swap collapses the page into a generic, route to `master §5.12` `[BLOCKING]` and A.8 fix or A.2 re-spec.

---

## 6 · Multilingual checks (workflow C only · IT pass at workflow A does not gate on these)

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
| AR | `استمرارية العائلة تُقاس بـ<em>الأجيال</em>.` | `الأجيال` (italic substitute via Kufi weight or oblique fallback — convention confirmed at workflow C pre-flight) |

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

The `/contatti/` form select options translate per locale per `continua-build-brief.md §11`:
- IT: 5 anni / 10 anni / 25 anni / multi-generazionale
- EN: 5 years / 10 years / 25 years / multi-generational
- FR: 5 ans / 10 ans / 25 ans / multi-générationnel
- ES: 5 años / 10 años / 25 años / multi-generacional
- AR: ٥ سنوات / ١٠ سنوات / ٢٥ سنة / متعدد الأجيال (digit convention confirmed at workflow C pre-flight)

### Whistleblowing link per-locale

- IT: "Whistleblowing"
- EN: "Whistleblowing"
- FR: "Lanceur d'alerte"
- ES: "Canal de denuncia"
- AR: "الإبلاغ عن المخالفات"

All 5 routes return 200 in staff session (Solaria Pass C precedent — internal-link 200 audit closed the `&preview=1` leak). Walk runs the same 200-audit grep pre-flight.

### Cross-locale internal-link 200 audit

Every IT home → 11 internal links must resolve to 200 in staff session. This is the Solaria Pass C precedent: closed the `&preview=1` leak across 6 corporate-suite chrome files + 1 view (20 hrefs) so 11/11 internal links from IT home → 200 in staff session. The Continua walk runs the same audit pre-flight on workflow C entry.

---

## 7 · Mitigation verification (the 5 risks from `continua-distinctness-proof.md §5`)

These are the load-bearing live checks. Each maps to a Risk in the distinctness proof and to a fallback move if the live render does not pass.

| Risk | Live verification | Pass criterion | Fallback if FAIL |
|---|---|---|---|
| **R1 · Pragma palette echo** | At 1920 / 1280 / 720, count brass touchpoints visible in viewport. Side-by-side compare with Pragma at 1920. | ≥ 5 brass touchpoints render at 1920 first scroll · brass distinguishable from pine + cream at 1280 + 720 · side-by-side stakeholder reading distinguishes Continua as "pine + brass stewardship" vs Pragma as "navy + emerald advisory" | proof §5 R1 fallback ladder: brass saturation +6% → add 6th brass touchpoint at pillars divider → A.2 re-spec on palette (do NOT change pine/brass families) |
| **R2 · Fiscus hero adjacency** | Open hero photo at 1280 + 1024. Confirm: zero documents > 1, zero laptop/keyboard, zero eyeglasses-on-paper visible at any viewport. Confirm room-architectural framing survives the crop. | Hero crop at every viewport reads as room-architectural · single book + lamp focal · shelves visible in soft focus | proof §5 R2 fallback ladder: re-curate slot_0 only → reframe crop via object-position → escalate slot 5 to hero (last resort) |
| **R3 · Stakeholder one-liner adjacency** | "Remove the studio name" test on home page (DevTools wordmark hidden). Read the first scroll vocabulary. | Live page reads as "family office governing across generations" — NOT as "any premium institutional firm." Family vocabulary fires in ≥ 3 surfaces in first scroll (h1 + meta-strip + at least one pillar h3 or sectors-ribbon label). | proof §5 R3 fallback: A.4 narrow copy-fix to push "famiglia / generazioni / Consiglio di Famiglia" to fire in first 3 surfaces · sectors-ribbon label sharpening |
| **R4 · Solaria leadership-photo adjacency** | At 1920 / 1280 / 768, view leadership 3-card row. Confirm 3 distinct demographics readable. | 3 cards span 40s · 50s · 60s + at least 2 visible genders + at least 3 visible ethnicities at every viewport | proof §5 R4 fallback: re-curate slot_2 + slot_3 only · add demographic eyebrow microcopy ("Senior Steward · 35 anni di mandato") · do NOT drop leadership block · do NOT go typographic-only |
| **R5 · Mid-strip cadence framing** | At every viewport with governance-cycle-strip visible, confirm each of 3 cells renders the (eyebrow · figure · context-line) triple, not (label · figure). | Each cell shows: brass eyebrow label ("Cadenza CdF") + figure ("4 riunioni / anno") + context-line ("calendario di governance condiviso con la famiglia") · context-line readable at 1280 + 768 | proof §5 R5 fallback: A.4 narrow copy-fix to expand context-lines · A.5 narrow CSS edit to give cycle-strip distinct visual register · do NOT drop the mid-strip · do NOT collapse to KPI tuple |

---

## 8 · Release-gate expectations (the binding gate for Commit B)

The orchestrator will NOT request Commit B (LIVE flip) until ALL of the following are TRUE on file. (Commit A — `tier=draft` IT-only — has a narrower set; the LIVE flip is the binding gate.)

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
- [ ] All 5 mitigation verifications (§7 above) — PASS
- [ ] "Remove the studio name" live test (§5) — PASS
- [ ] Cross-locale internal-link 200 audit — clean

### Layer 3 · Aggregation + handshake

- [ ] Scorecard filled · Layer 1/2/3 stamped · grade ≥ 4.50/5
- [ ] User-handshake artefact filed · binary SHIP/HOLD answered SHIP
- [ ] Distinctness re-confirmed at flip time — still ≥ 4/5 vs every sibling
- [ ] Live DOM matches build brief (no drift introduced post-A.5)
- [ ] Pexels-only re-confirmed on live render at every locale
- [ ] No deviation note (`§ deviation`) flags an unresolved `[BLOCKING]` rule
- [ ] No conservative override invoked

### Walk freshness gate

- All walk verdicts ≤ 30 days old at flip time (`BROWSER_QUALITY_GATE §3`)
- If a verdict is stale, re-walk the affected locale before the orchestrator requests Commit B

---

## 9 · Stop conditions during the walk (HALT, not slow)

Per `template-orchestrator-master.md §4`. Any of (1-10) → orchestrator does NOT request Commit B. Period.

1. **Distinctness collision discovered live** (≤ 3/5 vs any sibling · matrix re-test on render) → workflow B re-spec
2. **Non-Pexels URL on live render** → workflow B fix · NO LIVE flip
3. **Hero h1 cream-on-cream or any near-mono ≤ 4.5:1** → `[BLOCKING]` · workflow B
4. **Two adjacent sections share function** → workflow B
5. **AI-slop tell visible** (Inter on h1 / purple gradient / cards-in-cards / etc.) → workflow B
6. **Editor affordance leaks into `/live/`** → workflow B
7. **Mobile ≤ 720 shows horizontal scroll OR hero still horizontal** → workflow B
8. **Locale switcher does not change `lang` + `dir`** → workflow B
9. **AR RTL layout requires duplicate CSS instead of logical properties** → workflow B
10. **"Remove the studio name" test fails** (page reads as a generic) → workflow B re-spec

### Continua-specific stop conditions (in addition to the 10 above)

11. **Brass accent NOT visible at ≥ 3 touchpoints at 1920** (Risk 1 mitigation fail beyond the fallback ladder) → workflow B re-spec on palette
12. **Hero photo shows > 1 document, any laptop, or any visible human** (Risk 2 build-brief §4 rejection rule violated) → workflow B narrow A.3 re-curate
13. **Leadership 3-card row reads as same-demographic at any viewport** (Risk 4 mitigation fail) → workflow B narrow A.3 re-curate slot_2 + slot_3
14. **Mid-strip cells render (label · figure) only, dropping the context-line** (Risk 5 mitigation fail) → workflow B narrow A.4 + A.5 fix
15. **Voice anchor `<em>` wraps a non-temporal word** (translator regression on workflow C) → workflow B narrow A.4 fix on the offending locale

---

## 10 · The walk artefact tree

```
factory/reports/browser-verification/continua-stewardship/
  it/<YYYY-MM-DD>/
    home-1920.png · home-1440.png · home-1280.png · home-1024.png · home-768.png · home-390.png
    about-* · services-* · case-list-* · case-detail-* · contact-*  (× 6 viewports)
    walk-log-it.md
    contrast-it.md
    responsive-it.md
    style-critique-it.md
    reduced-motion-it.md
    mitigation-verification-it.md  (the 5 risks · pass/fail per risk)
  en/<YYYY-MM-DD>/  · same tree
  fr/<YYYY-MM-DD>/  · same tree
  es/<YYYY-MM-DD>/  · same tree
  ar/<YYYY-MM-DD>/  · same tree + rtl-parity-ar.md (6 extra captures)

factory/reports/corporate-suite/continua-stewardship/
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
  multilingual-<YYYY-MM-DD>/
    preflight.md
    copy-en.md · copy-fr.md · copy-es.md · copy-ar.md
    walk-en.md · walk-fr.md · walk-es.md · walk-ar.md
    multilingual-summary.md
  release-<YYYY-MM-DD>/
    release-decision.md
```

This tree is the template's PERMANENT FILE per `single-template-workflow.md §3`. It is not session scratch.

---

## 11 · Release-decision checks (Commit B gate)

The release-decision-orchestrator runs gates 1-10 plus a user handshake and a gatekeeper scorecard. Continua-specific bindings:

- **Gate 1 (rubric grade)**: scorecard ≥ 4.50/5 (4.67/5 is precedent · target)
- **Gate 2 (blocking findings)**: 0/N open · all `[BLOCKING]` resolved
- **Gate 3 (locale walks)**: 5/5 PASS (IT + EN + FR + ES + AR)
- **Gate 4 (RTL parity)**: AR RTL parity walk PASS (6 extra captures on file)
- **Gate 5 (Pexels-only on live)**: re-grep at flip time across all 5 locales · clean
- **Gate 6 (cross-cluster URL grep on live)**: clean against `business-corporate` · `business-fiscal` · `business-coaching`
- **Gate 7 (distinctness re-confirmed)**: matrix re-test at flip time · still ≥ 4/5 vs every sibling (Pragma · Fiscus · Solaria)
- **Gate 8 (user handshake)**: SHIP / HOLD recorded with screencast evidence pack
- **Gate 9 (gatekeeper scorecard)**: countersigned by release-gatekeeper agent
- **Gate 10 (conservative override)**: NOT invoked (any HOLD without justification holds the flip)
- **Gate 11 (Continua mitigation re-test)**: all 5 mitigation verifications from §7 above re-confirmed at flip time

A HOLD on any gate routes back to the appropriate workflow (A re-spec / B narrow fix / C narrow re-walk). The orchestrator does not patch around a HOLD.

---

## 12 · One-paragraph summary of the gate

If Continua were a real candidate building today, the orchestrator would block any LIVE flip until: 6 pages × 6 viewports × 5 locales (with an extra AR RTL parity walk + reduced-motion sweep) produce 187 captures across 5 locales; every walk verdict files PASS against the cluster rubric; the contrast / responsive / style-critique / Pexels-only / cross-cluster-grep / AI-slop / "remove-studio-name" / editor-affordance-on-live / form-gate-translation / focus-ring-brass-not-blue / dark-on-dark / AR-logical-properties / heading-italic-on-correct-em-word / mid-strip-cell-stack-at-720 checks all clear; the 5 Continua-specific mitigation verifications (Risks 1-5 from the distinctness proof) PASS at the live render; the scorecard reads ≥ 4.50/5 across Layers 1-2-3; the user signs the handshake binary SHIP. Any single failure routes back through workflow B narrowly, no scope expansion, re-walk on the affected dimension only. The 30 minutes the walk takes is the 30 minutes that would have caught Solaria's cream-on-cream defect — non-negotiable.
