# Causa retrofit slice 01 · scorecard summary

```yaml
report_type:        scorecard summary (Causa retrofit slice 01 ·
                    Phase X.7d.02 · companion to
                    factory/reports/hardening/causa-retrofit-slice-01.md)
date:               2026-05-05
agent:              orchestrator-side scorecard aggregator
slice:              R1 (CTA Apri-X → Sottometti-X · IT-only)
                    + R4 (NAV-1 sticky-condensed-on-scroll · 84→64px)
                    + R6 (EVID-5 provenance-tooltip on hero photo)
companion files:
  - factory/reports/hardening/causa-retrofit-slice-01.md (the slice)
  - factory/reports/browser-verification/causa-retrofit-slice-01.md
  - factory/reports/hardening/anti-clone-2.0-rules.md (the rule book)
  - factory/reports/hardening/lf2-family-internal-variance-rules.md
    (AC-V1..V5 binding)
status_tag:         GREEN · all gates clean · subsequent slice ready
verdict:            slice ships at all gates · Causa is anti-clone
                    2.0 COMPLIANT vs Cornice
```

## §1 · Per-gate scorecard

| Gate | Result | Evidence |
|---|---|---|
| **Tests** | ✅ 546/546 OK | `python manage.py test --verbosity 0` |
| **Anti-clone 2.0 score · Cornice ↔ Causa** | ✅ 23/54 → **27/54** (+4 · 28/54 with R7 paper-credit) | `causa-retrofit-slice-01.md §3` |
| **Critical-axis veto · CTA (axis 13)** | ✅ FAIL → **PASS** (1 → 2) | R1 Sottometti-X verbatim |
| **Critical-axis veto · motion (axis 18)** | ✅ FAIL → **PASS** (1 → 2) | R4 NAV-1 + slice-00 KPI-2 = 2 named patterns |
| **Critical-axis veto · imagery (axis 17)** | ✅ FAIL → **PASS** (1 → 2) | R6 EVID-5 provenance-tooltip |
| **Critical-axis veto · voice (axis 12)** | ✅ unchanged at 3 | `evidenza` ladder vs `argomento` ladder |
| **Critical-axis veto · subject (axis 2)** | ✅ unchanged at 2 | Liverpool empty courtroom vs Bologna portico |
| **AC-V1 within-cell sub-variants ≥3** | ✅ 1 → **3** (KPI-2 + NAV-1 + EVID-5) | `lf2-family-internal-variance-rules.md §4 AC-V1` |
| **AC-V2 portrait composition ≥2 axes** | ✅ unchanged · A.5b shipped | seated reading codex vs seated drafting blueprints (≥2 axes diverge) |
| **AC-V3 CTA verb-class divergence** | ✅ open → **CLAIMED** (Sottometti-X) | open-class registry per `lf2-family-internal-variance-rules.md §4 AC-V3` |
| **AC-V4 KPI cell semantic-class ≥1 cell** | ✅ unchanged · already cleared | year-range `31 anni` distinct from Cornice's `38 menzioni` publication-anchored |
| **CS-LAYOUT-* family invariants** | ✅ no L-cell flipped | LF-2 cells preserved · LF-1/LF-3/LF-4/LF-5 untouched |
| **CS-EXEC-01 voice anchor** | ✅ unchanged | hero h1 + CTA closer h2 still ship `evidenza` cluster anchor |
| **CS-IMG-SRC-01 Pexels-only** | ✅ unchanged | imagery URLs not touched |
| **CS-PAL-01 contrast** | ✅ unchanged | palette tokens not touched |
| **CS-RHYTHM-01 padding** | ✅ unchanged | 100×72 padding · max-width 1400px preserved |
| **CS-NAV-* navbar polarity** | ✅ unchanged | LF-2 cream-paper polarity preserved · NAV-1 shrink scoped under data-attribute |
| **CS-MOTION-INV-01 reduced-motion** | ✅ honored | global `lm-reduced` short-circuit at JS `init()` · CSS `body.lm-reduced` overrides pin static heights / visibility |
| **CS-MOTION-INV-02 no decorative motion** | ✅ no decorative motion | NAV-1 shrink is functional (compact density on scroll) · EVID-5 reveal is informational (provenance metadata) |
| **CS-MOTION-INV-03 no manipulative SaaS** | ✅ no manipulative motion | no urgency · no countdown · no scroll-jacking |
| **CS-MOTION-INV-05 one-time-per-session** | n/a for NAV-1/EVID-5 (continuous-scroll behaviors are NOT one-shot) · KPI-2 (slice-00) preserves its one-shot semantics |
| **CS-MOTION-INV-06 no scroll-jacking** | ✅ no scroll-jacking | NAV-1 listener is rAF-throttled `passive: true` · scroll velocity unchanged · scroll-bar not touched |
| **CS-MOTION-INV-07 no autoplay carousels** | ✅ unchanged | no carousels |
| **Browser walk · 6 corporate-suite siblings** | ✅ 6/6 correct | server-side body data-attributes match each declared `motion_profile` |
| **Frozen-sibling regression · Cornice** | ✅ 0 unexplained drift | 5 IT routes 200 anon + 5-locale 200 anon · "Apri un fascicolo" verbatim · no new motion flags on body |
| **Frozen-sibling regression · Pragma/Fiscus/Solaria/Continua** | ✅ 0 unexplained drift | 4/4 home 200 anon · NO new motion flags · NO provenance markup |
| **Causa draft-gate** | ✅ 404 anonymous · 200 staff × 5 routes | tier=draft preserved · no public flip |
| **Catalog public listing** | ✅ causa-legale absent | draft state preserved |
| **Home counter** | ✅ "24+" unchanged | no public-flip · no count change |
| **R1 CTA verbatim** | ✅ 5/5 Causa pages with "Sottometti" · 0/5 with "Apri un parere" | walker `_walk_slice01.py` |

## §2 · Slice-scope discipline

| Constraint | Status |
|---|---|
| No `apps/editor/*` edits | ✅ confirmed |
| No `apps/projects/*` edits | ✅ confirmed |
| No `apps/commerce/*` edits | ✅ confirmed |
| No new sibling | ✅ confirmed (6 corporate-suite siblings unchanged in count) |
| No tier change | ✅ confirmed (Causa stays tier=draft) |
| No registry change | ✅ confirmed (`TEMPLATE_REGISTRY.json` untouched) |
| No LF migration | ✅ confirmed (Causa stays LF-2) |
| No multilingual widening | ✅ confirmed (IT-only · workflow C still HELD) |
| Profile-gated extension | ✅ confirmed (`MOTION_PROFILES` extended with `nav_condense_on_scroll` + `evid5_provenance` flags · `g2-editorial-counter` is the only profile opting in to either) |
| Reduced-motion safe | ✅ confirmed (CSS overrides under `body.lm-reduced` · JS short-circuits when `lm-reduced` set) |
| Reusable infrastructure | ✅ confirmed (`MOTION_PROFILES` dict has space for additional flags · slice 02 R2 EVID-3 + R3 TIME-3 will extend it) |

## §3 · What improved (visible · dynamic · personalization-ready)

### Visibly improved (vs slice-00 state)
- Causa CTA pill at every page reads `SOTTOMETTI UN PARERE PRELIMINARE`
  (transactional verb-class) · Cornice's `APRI UN FASCICOLO PROGETTO`
  remains the LF-2 1st-occupant claim · the verb-class divergence is
  visible at every page-touchpoint of both templates.
- Causa LF-2 nav shrinks 84→64px at 240px scroll · wordmark eases
  22→18px · subtitle dims 0.7 opacity · Cornice nav stays static.
- Causa hero photo gains a hover/focus-revealed provenance panel
  (Pexels · CC0 · St George's Hall, Liverpool) · Cornice has only a
  static credit-line.
- Reduced-motion clients see the panel pinned visible · NAV-1 pinned
  at full height · KPI-2 static (final value).

### More dynamic
- Cornice ↔ Causa pair: 23/54 → 27/54 (+4 · or 28/54 with R7 credit)
- Critical-axis vetoes: 4 of 5 PASSED → **5 of 5 PASSED**
- AC-V1 sub-variants: 1 → **3** (clears the LF-2 within-family floor)
- 3 visible behavior changes on Causa · 0 on every other sibling

### More customizable / personalization-ready
- `MOTION_PROFILES` extended with two new per-pattern flags
  (`nav_condense_on_scroll` · `evid5_provenance`) — both ready for
  Phase X.7c editor exposure as Layer-B preset toggles.
- AC-V3 CTA verb-class registry now has Causa's claim recorded
  (`Sottometti-X` taken in LF-2) so a future 3rd LF-2 occupant intake
  is correctly bound at A.1 planner brief.
- Two-pair scoring matrix infrastructure (used to compute the score
  raises in §3 of the slice file) is in paper form for any future
  LF-2 3rd-occupant intake to inherit.

## §4 · Open follow-ups (queued · NOT blocking this slice)

| Item | Severity | Pass |
|---|---|---|
| Causa EVID-3 case-citation-pop on magazine cards (R2) | retrofit · raises axis 9 cases-preview floor | X.7d slice 02 |
| Causa TIME-3 chronological-tick in narrative (R3) | retrofit · adds 4th sub-variant + saturates axis 18 | X.7d slice 02 |
| Causa workflow C multilingual (1 → 5 locales) | tier=draft 5-locale propagation · CTA verb-class parity check | Phase X.6 step 6 (separate brief) |
| Causa workflow D public flip | tier=draft → tier=published_live · cascade undoing | Phase X.6 step 7 (separate brief · after workflow C) |
| LF-2 family variance rules formalisation | already shipped via `lf2-family-internal-variance-rules.md` (X.7e ratification) · this slice satisfies AC-V1..V4 in the rendered cluster layer | DONE |
| Phase X.7a · ship 1 new cluster at hardening parity | cluster-level S6 resolution · audit gap #1 | Phase X.7a (multi-session) |
| Phase X.7b · extend `motion_profile` bundle | infrastructure (additional flags as new patterns ship) | per-slice extension as needed |
| Phase X.7c · editor-side palette/font/motion preset picker | customer-facing customization · Layer B | Phase X.7c (separate brief) |
| 7th corporate-suite sibling intake | system not ready until R2/R3 land OR Phase X.7b motion_profile DNA expansion | Phase X.7e+ |

## §5 · Final verdict

```
PHASE X.7d.02 · CAUSA RETROFIT SLICE 01 (R1 + R4 + R6) · SCORECARD
═══════════════════════════════════════════════════════════════════════════

Slice scope:                    NARROW · 7 files · ~205 lines added
Tests:                          546/546 OK · zero new failures
Live walk:                      62/62 PASS · zero frozen-sibling regression
Anti-clone 2.0 score:           Cornice ↔ Causa pair 23/54 → 27/54 (+4)
                                · 28/54 with R7 portrait paper-credit
Critical-axis vetoes:           5 of 5 PASSED (was 2 of 5 · slice clears
                                CTA + motion + imagery in one pass)
AC-V1 sub-variants:             1 → 3 (KPI-2 + NAV-1 + EVID-5 · floor met)
AC-V3 CTA verb-class:           OPEN → CLAIMED by Causa (Sottometti-X)
Cluster contract:               every CS-LAYOUT-* / CS-PAL-* / CS-NAV-* /
                                CS-MOTION-INV-* invariant preserved
Customization readiness:        2 new per-pattern flags shipped · ready
                                for X.7c editor slice to expose

Behavior changes:               1 of 6 siblings (DELIBERATE · documented)
                                · Causa hero photo gains provenance hover
                                · Causa LF-2 nav shrinks on scroll
                                · Causa CTA verb-class shifts to
                                  Sottometti-X across all IT pages

Behavior preserved:             5 of 6 siblings unchanged
                                · Pragma · Cornice · Fiscus · Solaria ·
                                  Continua

Apps untouched per scope:       editor · projects · commerce all 0 lines
                                changed · TEMPLATE_REGISTRY.json untouched

Verdict:                        ✓ SLICE PASSES · safe to leave shipped
                                · all 5 critical-axis vetoes PASSED
                                · within-family threshold cleared
                                · Causa is anti-clone 2.0 COMPLIANT vs
                                  Cornice in the rendered-cluster layer
                                · LF-2 multi-occupancy SAFE in both
                                  paper-and-process and rendered layers
                                · 7th sibling readiness still requires
                                  Phase X.7b motion_profile DNA expansion
                                  OR slice 02 (R2 + R3) before opening
                                · cluster ready for next product pass:
                                  slice 02 (R2 EVID-3 + R3 TIME-3) OR
                                  workflow C multilingual (Causa 1→5)
```
