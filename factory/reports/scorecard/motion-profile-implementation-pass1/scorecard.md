# Scorecard · motion_profile DNA · implementation pass 1

```yaml
phase:           X.7b · motion_profile DNA · implementation pass 1
date:            2026-05-06
verdict:         GREEN · 9/9 cells PASS · 0 blocking · 0 axis demoted
                 · zero apps/editor / apps/projects / apps/commerce edits
                 · zero new templates opened · zero public tier flips
companion:       factory/reports/hardening/motion-profile-implementation-pass1.md
                 factory/reports/browser-verification/motion-profile-implementation-pass1.md
```

---

## §1 · Workflow gate scorecard

| # | gate | check | weight | result |
|---|---|---|---|---|
| 1 | A.0 territory-scout | scout-side declaration of motion_profile per cluster (paper plan + catalog reference already present · this pass adds 2 wired flags) | shoulder | ✓ PASS |
| 2 | A.1 intake | brief schema requires `motion_profile` per cluster's allowed-set · planner-side rejection on out-of-set declaration | shoulder | ✓ PASS |
| 3 | A.2 plan | axis-18 scoring rubric operational · 11/15 corporate-suite pairs clear v2.0 critical-axis veto floor 2 · 4 grandfathered (Pragma/Fiscus/Solaria trio) | shoulder | ✓ PASS |
| 4 | A.5 build | 5 source files edited · ~175 net lines added · 0 reverted · 7 wired bundle flags emit through CS chrome | load-bearing | ✓ PASS |
| 5 | A.6 review-lock | anti-tacky red-lines AT-G1-2 · AT-G2C-4 · AT-G6-2 · AT-X1 · AT-X2 · AT-X3 · AT-X4 · AT-X5 walked · all encoded as CSS variable values | load-bearing | ✓ PASS |
| 6 | Workflow C/D walk · default-motion | 12/12 walk cells PASS · cinematic-fade gate fires correctly when armed · card-lift gate fires correctly when armed · 6 frozen siblings byte-equivalent | load-bearing | ✓ PASS |
| 7 | Workflow C/D walk · reduced-motion | 3-layer guarantee verified (JS root short-circuit + `body.lm-reduced` class + `@media (prefers-reduced-motion: reduce)` native query) · both new gates degrade to fully-visible static under reduced-motion | load-bearing | ✓ PASS |
| 8 | Workflow D flip · scorecard | axis-18 distinctness scoring unchanged · zero new flag emitted on any frozen sibling · 6 corporate-suite pair scores preserved (no v2.0 veto regression) | load-bearing | ✓ PASS |
| 9 | regression boundary | 546/546 Django tests PASS (baseline 546/546) · 6 frozen CS siblings byte-equivalent on body data-attribute set · Causa slice-01/02 5-flag bundle preserved | hard-floor | ✓ PASS |

**9/9 PASS** · zero blocking · zero axis demoted.

---

## §2 · Visible-distinctness scorecard (motion-profile-dna-plan §7 axis 18)

| sibling pair | profile pair | flag-count delta | axis 18 score | v2.0 veto |
|---|---|---|---|---|
| Pragma ↔ Cornice | g3 ↔ g2 | 1 ↔ 0 | 2 | ✓ |
| Pragma ↔ Causa | g3 ↔ g2-counter | 1 ↔ 5 | 2 | ✓ |
| Pragma ↔ Fiscus | g3 ↔ g3 | 1 ↔ 1 | 0 | grandfathered |
| Pragma ↔ Solaria | g3 ↔ g3 | 1 ↔ 1 | 0 | grandfathered |
| Pragma ↔ Continua | g3 ↔ g4 | 1 ↔ 0 | 2 | ✓ |
| Cornice ↔ Causa | g2 ↔ g2-counter | 0 ↔ 5 | 2 (post-slice-02) | ✓ |
| Cornice ↔ Fiscus | g2 ↔ g3 | 0 ↔ 1 | 2 | ✓ |
| Cornice ↔ Solaria | g2 ↔ g3 | 0 ↔ 1 | 2 | ✓ |
| Cornice ↔ Continua | g2 ↔ g4 | 0 ↔ 0 | 1 (S6 cluster-tropes signal · grandfathered for now) | (S6) |
| Causa ↔ Fiscus | g2-counter ↔ g3 | 5 ↔ 1 | 2 | ✓ |
| Causa ↔ Solaria | g2-counter ↔ g3 | 5 ↔ 1 | 2 | ✓ |
| Causa ↔ Continua | g2-counter ↔ g4 | 5 ↔ 0 | 2 | ✓ |
| Fiscus ↔ Solaria | g3 ↔ g3 | 1 ↔ 1 | 0 | grandfathered |
| Fiscus ↔ Continua | g3 ↔ g4 | 1 ↔ 0 | 2 | ✓ |
| Solaria ↔ Continua | g3 ↔ g4 | 1 ↔ 0 | 2 | ✓ |

**11/15 pair scores ≥ 2** (cleared v2.0 critical-axis-veto floor) ·
**4/15 grandfathered** (Pragma/Fiscus/Solaria trio identical g3 + 1-flag
bundle · documented in design-standard §19 · NO new sibling may join) ·
**0/15 regressions** introduced by this pass.

---

## §3 · Wired-flag inventory (after this pass)

| flag | pattern (library §) | wired | profiles opt-in | siblings actually firing today |
|---|---|---|---|---|
| `kpi_animate` | KPI-2 (§2.1) | ✓ slice 01 | g2-editorial-counter · g3-institutional · g5-sprint-console | Pragma · Fiscus · Solaria · Causa |
| `nav_condense_on_scroll` | NAV-1 (§2.7) | ✓ retrofit slice 01 | g2-editorial-counter | Causa |
| `evid5_provenance` | EVID-5 (§2.3) | ✓ retrofit slice 01 | g2-editorial-counter | Causa |
| `evid3_citation` | EVID-3 (§2.3) | ✓ retrofit slice 02 | g2-editorial-counter | Causa |
| `time3_chronotick` | TIME-3 (§2.6) | ✓ retrofit slice 02 | g2-editorial-counter | Causa |
| **`card_lift_restrained`** | MICRO-2 (§2.5) | **✓ pass 1 (this slice)** | **(none today · safe-pool reservation for g1/g3/g5 future intakes)** | **(none)** |
| **`cinematic_fade`** | MEDIA-1 (§2.4) | **✓ pass 1 (this slice)** | **g6-cinematic** | **(none today · ready for Phase X.7a Pixel/Villa/Vertex/Luxe brief)** |

7 flags wired total · 0 paper-extended-but-un-wired regressions.

5 flags still paper-only (un-wired): `hero_parallax` · `gallery_snap` ·
`cursor_vignette` · `magnetic_button` · `nav_hide_on_scroll_down` ·
`scroll_progress_bar` · `live_data_kpi`.

---

## §4 · Test-suite delta

| baseline | post-pass | delta |
|---|---|---|
| 546/546 PASS · 0 fails | 546/546 PASS · 0 fails | 0 |

---

## §5 · Reduced-motion guarantee scorecard

| layer | mechanism | tested | result |
|---|---|---|---|
| 1 | JS root short-circuit at `init()` line 50-60 (the `lm-reduced` class is added; `setupCinematicFade()` runs AFTER this short-circuit · never executes) | ✓ | PASS |
| 2 | `body.lm-reduced[data-motion-card-lift="1"]` · `body.lm-reduced[data-motion-cinematic-fade="1"]` rules clear opacity / transform / filter / box-shadow / transition with `!important` | ✓ | PASS |
| 3 | `@media (prefers-reduced-motion: reduce)` rules clear the same properties for any client whose JS never executed | ✓ | PASS |

3/3 layers verified · belt + braces + suspenders.

---

## §6 · Frozen-sibling parity scorecard

| sibling | category | tier | profile | flag count | byte-equivalent on body? |
|---|---|---|---|---|---|
| pragma-corporate-suite | business | live | g3-institutional | 1 (kpi-animate) | ✓ |
| cornice-architettura | business | live | g2-editorial | 0 | ✓ |
| fiscus-commercialista | business | live | g3-institutional | 1 (kpi-animate) | ✓ |
| solaria-coaching | business | live | g3-institutional | 1 (kpi-animate) | ✓ |
| continua-stewardship | business | live | g4-stewardship | 0 | ✓ |
| causa-legale | business | draft | g2-editorial-counter | 5 (kpi-animate · nav-condense · evid5 · evid3 · time3) | ✓ |

6/6 byte-equivalent on body data-attribute set.

---

## §7 · Verdict

**GREEN** · ratify · ship.

motion_profile DNA elevation passes from PAPER-RATIFIED to CODE-VERIFIABLE.
Two new bundle-flag gates (MICRO-2 card-lift + MEDIA-1 cinematic-fade)
are wired with full reduced-motion guarantee. Zero frozen-sibling
regression. 546/546 tests still PASS.

The system is ready to bind future intakes that pick `g6-cinematic` or
flip `card_lift_restrained` on a g1/g3/g5 sibling. The recommended next
step (per implementation report §13) is option **B · Causa workflow C
multilingual**, which closes the LF-2 cell-pair voice + motion contract
at cluster level.
