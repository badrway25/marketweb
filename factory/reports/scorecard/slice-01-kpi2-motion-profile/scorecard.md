# Slice 01 · KPI-2 + motion_profile · scorecard

```yaml
report_type:        scorecard summary (slice 01)
date:               2026-05-05
agent:              orchestrator-side scorecard aggregator
slice:              Phase X.7d.01 · `motion_profile` DNA + KPI-2 count-up-on-view
companion files:
  - factory/reports/hardening/premium-dynamic-implementation-slice-01.md
  - factory/reports/browser-verification/slice-01-kpi2-motion-profile.md
status_tag:         GREEN · safe to leave shipped · subsequent slice ready
verdict:            slice ships at all gates clean
```

## §1 · Per-gate scorecard

| Gate | Result | Evidence |
|---|---|---|
| **Tests** | ✅ 546/546 OK | full test suite | `python manage.py test --verbosity 0` |
| **CS-LAYOUT-* family invariants** | ✅ no L-cell flipped | Cornice + Causa retain LF-2 cells verbatim · Continua retains LF-5 verbatim |
| **CS-EXEC-01 voice anchor** | ✅ unchanged | hero h1 + CTA closer h2 still ship the cluster's anchor sentence per locale |
| **CS-IMG-SRC-01 Pexels-only** | ✅ unchanged | imagery not touched |
| **CS-PAL-01 contrast** | ✅ unchanged | palette tokens not touched |
| **CS-RHYTHM-01 padding** | ✅ unchanged | 100×72 padding · max-width 1400px preserved |
| **CS-NAV-* navbar polarity** | ✅ unchanged | navbar geometry · chrome polarity · locale switcher unchanged |
| **CS-MOTION-INV-01 reduced-motion** | ✅ honored | global `lm-reduced` short-circuit at `init()` unchanged · per-template gate fires only after global gate cleared |
| **CS-MOTION-INV-02 no decorative motion** | ✅ no new decorative motion | KPI-2 count-up is semantic (the figure announces itself by ticking) · documented purpose |
| **CS-MOTION-INV-03 no manipulative SaaS** | ✅ no new manipulative motion | count-up does not push conversion · no urgency · no countdown |
| **CS-MOTION-INV-05 one-time-per-session** | ✅ honored | IntersectionObserver unobserves on first intersect · pre-existing JS pattern · slice does not modify |
| **CS-MOTION-INV-06 no scroll-jacking** | ✅ no scroll-jacking | counter is intersection-based · scroll velocity unchanged |
| **CS-MOTION-INV-07 no autoplay carousels** | ✅ unchanged | no carousels added |
| **Browser walk · 6 siblings** | ✅ 6/6 correct | server-side render + live JS counter activation matches each declared `motion_profile` |
| **Frozen-sibling regression** | ✅ 0 unexplained drift | every byte delta explained by intentional slice changes (data-attributes + LF-2 cell tokens + comments) |
| **Causa draft-gate** | ✅ 404 anonymous · 200 staff × 9 routes | tier=draft preserved · no public flip |
| **Catalog public listing** | ✅ causa-legale absent | draft state preserved |
| **Home counter** | ✅ "24+" unchanged | no public-flip · no count change |
| **Anti-clone 2.0 score** | ✅ Cornice↔Causa pair improves from 21/54 to 23/54 | axis 7 +1 (KPI placement sub-variant) · axis 18 +1 (one new pattern enabled in Causa) |

## §2 · Slice-scope discipline

| Constraint | Status |
|---|---|
| No apps/editor edits | ✅ confirmed |
| No apps/projects edits | ✅ confirmed (data-attribute approach used to avoid editing brittle test) |
| No apps/commerce edits | ✅ confirmed |
| No new sibling | ✅ confirmed (6 corporate-suite siblings unchanged in count) |
| No tier change | ✅ confirmed |
| No registry change | ✅ confirmed (TEMPLATE_REGISTRY.json untouched) |
| Single slice scope | ✅ confirmed (one `motion_profile` DNA dimension + one pattern · KPI-2) |
| Reusable infrastructure | ✅ confirmed (`MOTION_PROFILES` dict has space for NAV-1, EVID-3, TIME-3, MICRO-2, etc. flags · subsequent slices extend it) |

## §3 · What improved (visible · dynamic · customizable)

### Visibly improved
- Causa hero overlay KPI tuple `28 · 14 · 31` now animates count-up on
  viewport entry (1400ms ease-out) → distinguishes Causa from Cornice on
  the most prominent KPI surface.
- Continua KPI band `18 · 3 · €1.8 B · 4` now renders statically →
  aligns with stewardship register (longitudinal mandate-trajectory feel
  reinforced by stillness).

### More dynamic
- Cornice ↔ Causa pair: axis 7 (KPI placement) +1 · axis 18 (motion +
  page choreography) +1 · pair 21/54 → 23/54.
- Cluster's motion vocabulary expanded from 1 implicit unnamed default
  to 7 explicitly enumerated profiles (G1-G6 + G2-editorial-counter
  sub-variant).

### More customizable
- `motion_profile` is now a first-class DNA field, ready for Phase X.7c
  editor slice to expose as a Layer-B preset picker (`minimal · standard
  · expressive` per `template-personalization-architecture.md §5`).
- Per-pattern flags (`kpi_animate` today; `nav_condense_on_scroll` ·
  `hero_parallax` · etc. in subsequent slices) form the data shape that
  end-user toggles will manipulate at Phase X.7c.5.

## §4 · Open follow-ups (queued · NOT blocking this slice)

| Item | Severity | Pass |
|---|---|---|
| Causa CTA inflection shift (R1) | retrofit · resolves CTA critical-axis veto | X.7d.02 |
| Causa NAV-1 sticky-condensed (R4) | retrofit | X.7d.03 |
| Causa EVID-5 provenance-tooltip (R6) | retrofit | X.7d.04 |
| Causa EVID-3 case-citation-pop (R2) | retrofit · resolves case-axis floor | X.7d.05 |
| Causa TIME-3 chronological-tick (R3) | retrofit · resolves motion critical-axis veto fully | X.7d.06 |
| LF-2 family variance rules formalisation | rule book (paper) · prevents future LF-2 3rd-occupant trap | X.7d.07 |
| Phase X.7a · ship 1 new cluster at hardening parity | cluster-level S6 resolution · audit gap #1 | X.7a |
| Phase X.7b · extend `motion_profile` bundle (NAV-1 / EVID-3 / TIME-3 / MICRO-2 flags) | infrastructure | X.7b |
| Phase X.7c · editor-side palette/font/motion preset picker (Layer B) | customer-facing customization | X.7c |

## §5 · Final verdict

```
PHASE X.7d SLICE 01 · KPI-2 + MOTION_PROFILE · SCORECARD
═══════════════════════════════════════════════════════════════════════════

Slice scope:                    NARROW · 5 files · 65 lines added
Tests:                          546/546 OK · zero new failures
Live render:                    6/6 siblings render correct motion_profile
                                + correct kpi-animate behavior · all
                                IntersectionObserver gates fire as declared
Frozen-sibling regression:      0 unexplained drift
Anti-clone 2.0 score:           Cornice↔Causa pair 21/54 → 23/54 (+2)
Cluster contract:               every CS-LAYOUT-* / CS-PAL-* / CS-NAV-* /
                                CS-MOTION-INV-* invariant preserved
Customization readiness:        DNA dimension shipped · ready for X.7c
                                editor slice to expose

Behavior changes:               2 of 6 siblings (DELIBERATE · documented)
                                · Continua KPI band stops animating (G4
                                  stewardship-register-prefers-stillness fix)
                                · Causa KPI overlay starts animating (within-
                                  family differentiator vs Cornice · retrofit
                                  R5)

Behavior preserved:             4 of 6 siblings unchanged
                                · Pragma · Cornice · Fiscus · Solaria

Apps untouched per scope:       editor · projects · commerce all 0 lines
                                changed

Verdict:                        ✓ SLICE PASSES · safe to leave shipped
                                · audit gap #2 motion infrastructure now
                                  product-side reality
                                · retrofit plan R5 fully shipped
                                · 5 more retrofit slices queued under same
                                  playbook
                                · cluster ready for the next product pass
                                  (recommend X.7d.02 R1 CTA inflection
                                  shift · 1 string × 5 locales)
```
