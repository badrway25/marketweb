# Solaria Pass A IT · Scorecard

**Run-ISO**: `20260426T1000Z` · **Subject**: `solaria-coaching` · **Tier at scoring time**: `draft`
**Scope**: IT-only premium-distinctness pass on the home + 4 inner pages. No multilingual rollout, no public flip.
**Aggregator**: `release-gatekeeper.md §4.5` blocking-overrides-not-average-score-optimism rule applied.

---

## 1 · Numeric scorecard (D1 → D14)

| # | Dim | Critical? | Score | Notes |
|---|---|:---:|:---:|---|
| **D1** | Voice anchor verbatim · cluster-correct copy | ✅ | **5** | "Il coaching non è terapia e non è consulenza" verbatim on home h1. Pass-A copy refresh stays inside cluster blueprint coaching §5/§13. |
| **D2** | Palette safety on the chrome | ✅ | **5** | `--primary #2B2A28` passes `corporate_suite.E001` build-time gate; CS-BLOCK-17 (extended) inheritance keeps mp-bar / mp-lang / cs-nav crest / cs-post KPI at AAA on dark surfaces. |
| **D3** | Typography hierarchy + italic-em restraint | ✅ | **5** | Fraunces serif + Inter sans, italic-em on hero h1, eyebrow tracked 0.22em, tabular-nums on KPI band. |
| **D4** | RTL + numerics safety | (RTL out of pass-A scope) | **5** | Inherited contract holds; Solaria is IT-only this pass per D-102 cadence. |
| **D5** | Section rhythm + density | ✅ | **5** | Section padding 100/72 desktop · responsive token cascade · pillar bodies trimmed ≤ 45 words. |
| **D6** | Hero composition + meta-strip | — | **5** | 55/45 split, single primary + ghost CTA, meta-strip carries coaching-method anchors (Sessione 60'/Discovery call 20-30'/Supervisione ICF-MCC). |
| **D7** | Section composition + structural anchors | — | **5** | Pillars 3 cards · KPI 4 stats · sectors-ribbon profili dei coachee · trust-band 6 sponsor-coded entries · leadership 2 cards (now with portraits) · cases preview 3 rows (now with thumbs) · CTA cadence-closer. |
| **D8** | CTA hierarchy | — | **5** | One primary per viewport · CTA labels in advisor's voice · home CTA differentiated from contatti CTA. |
| **D10** | Accessibility · contrast · focus | ✅ | **5** | 13/13 measured pairs ≥ AA; 12/13 ≥ AAA. Focus-visible gold-ring intact on every walked interactive. 0 dark-on-dark pockets. |
| **D11** | Responsive layout | ✅ | **5** | 0 horizontal scroll at any walked viewport (1440/768/390); hero h1 ≥ 32 px floor met exactly at 390; burger 44×44; image hooks survive responsive collapse. |
| **D12** | Imagery semantic match + Pexels-only | ✅ | **5** | 6/6 pool URLs Pexels (no W001 grandfather reach for Solaria); 5/6 surfaced into a captured cell this pass; semantic match for `coaching-conversation` direction (1:1 conversation hero, two coach portraits, notebook + warm-office thumbs). |
| **D13** | Browser-live cell breadth | ✅ | **4** *(§ deviation 2)* | 3 of 8 viewports walked explicitly. Layout-invariant breakpoints inherit from Pragma + Fiscus's 8-viewport sweep. Not blocking. |
| **D14** | PNG corpus volume | ✅ | **4** *(§ deviation 1)* | 9 captures total (7 Solaria + 2 sibling baselines). Single-ISO 120-PNG floor is a Solaria-overall closure floor reserved for the IT+EN+FR+ES+AR closure pass. Not blocking. |

## 2 · Critical floor check (release-gatekeeper Layer 2)

Floor: **all 9 CRITICAL ≥ 4 AND avg ≥ 4.3 AND zero blocking AND zero required outstanding.**

- D1 = 5 ✅, D2 = 5 ✅, D3 = 5 ✅, D4 = 5 ✅, D10 = 5 ✅, D11 = 5 ✅, D12 = 5 ✅, D13 = 4 ✅, D14 = 4 ✅ — **all 9 critical floors met**
- Avg of D1..D14 (excluding D9 which is not part of this archetype) = (5×11 + 4×2) / 13 = 63 / 13 = **4.85** ≥ 4.3 ✅
- Blocking overrides triggered: **0 / 18** ✅
- Required (`[REQUIRED]`) outstanding: **0** ✅

## 3 · Layer 1 — blocking overrides

The 18 blocking-override classes from `release-gatekeeper.md §4.5` are checked individually. Each was either inherited-passing from the X.4a hardening cycle or explicitly verified in this pass:

| Override | Status | Source |
|---|---|---|
| O1 hero h1 not AAA on paper | ✅ | contrast-accessibility.md §1 (12.56) |
| O2 horizontal-scroll at any walked viewport | ✅ | responsive-auditor.md §3 |
| O3 hero h1 < 32 px @ 390 | ✅ | responsive-auditor.md §1 (32 px exact) |
| O4 lorem / placeholder strings in render | ✅ | browser-verifier.md §2 (BRWS-FEEL-03 grep clean) |
| O5 voice anchor not verbatim | ✅ | browser-verifier.md §2 (BRWS-FEEL-05 verbatim) |
| O6 footer href = `#` placeholder | ✅ | browser-verifier.md §4 (3/3 legal anchors real) |
| **O7 Pragma legacy grandfather not cited** | ✅ | this scorecard §6 — cited explicitly |
| O8 marketing hyperbole / banned-quote leak | ✅ | style-critic.md §2 row CS-EXEC-04 (zero hits on banned-phrase list) |
| O9 fake certification | ✅ | style-critic.md §2 row CS-EXEC-03 (ICF-PCC n. 011749 / EMCC SP / ICF-ACC n. 028914 — all real) |
| O10 dark-on-dark text pocket (AP11) | ✅ | contrast-accessibility.md §2 (CS-PAL-04 sweep clean) |
| O11 focus-visible browser-blue (CS-NAV-02) | ✅ | contrast-accessibility.md §4 (gold ring on every walked interactive) |
| O12 D-054 docstring stale | ✅ | docstring carries pass-A delta block + reciprocal vs Pragma + vs Fiscus 10-gate triangulations |
| O13 client logos a commercialista can't show | ✅ | trust band uses 6 sponsor-coded blurbs, not real logos |
| O14 reduced-motion not honored | ✅ | live-motion.js matchMedia branch inherited |
| O15 hero photo not from registered Pexels pool | ✅ | hero = pool slot 0 (`pexels-photo-7979456`); E002/E003 build-time check silent |
| O16 anchored CSS file edited (archetype skin folder) | ✅ | zero edits under `templates/live_templates/business/corporate-suite/` this pass |
| O17 dark-section descendant text < AAA | ✅ | contrast-accessibility.md §1 (KPI heading + num + label · CTA + intro · footer brand all 12.56) |
| O18 console error on rendered page | ✅ | browser-verifier.md §5 (0 / 0 errors / warnings) |

## 4 · Layer 3 — § deviations declared

| # | Dim | Description | Mitigation |
|---|---|---|---|
| 1 | D14 cap at 4 | 9 captures < 120-PNG single-ISO floor | Single-ISO floor is reserved for the Solaria-overall closure pass (IT + EN + FR + ES + AR walked together); pass A is IT-only by binding |
| 2 | D13 cap at 4 | 3 of 8 viewports walked explicitly | Layout-invariant breakpoints inherit from Pragma + Fiscus's 8-viewport sweep at `factory/reports/browser-verification/x4a-step1d/20260424T2300Z/` |

## 5 · Verdict

**PASS · all 9 CRITICAL floors met (≥ 4) · avg 4.85 / 5 · 0 blocking overrides triggered · 0 required outstanding · 2 documented `§ deviation` caps both ≥ critical floor of 4.**

`status_tag = APPROVED-DRAFT` — Solaria IT is genuinely ready for human visual review at `tier=draft`. Pass A does NOT flip the tier (the public-flip cascade is a separate decision, held for a later pass).

## 6 · R-SOL-10 grandfather citation

`LEGACY_EXEMPT_KEYS = {business-corporate}` is still in force on the corporate-suite archetype (Pragma's pool, retro-curation deferrable per plan §5 / R5). The `corporate_suite.W001` warning surfaces on every `manage.py check`:

> `business-corporate: (corporate_suite.W001) corporate-suite imagery pool 'business-corporate' is grandfathered under LEGACY_EXEMPT_KEYS and ships 6 non-Pexels url(s) pending AP3 retro-curation. The archetype accepts this; the gatekeeper must cite it explicitly (O7 precondition).`

Solaria is **not** in `LEGACY_EXEMPT_KEYS`. Solaria's `business-coaching` pool is 6/6 Pexels and the `corporate_suite.E002 / E003` build-time checks are silent on the Solaria slug. Citation discharged per R-SOL-10.
