# Master scorecard · Cornice A.5 IT build

```yaml
report:           master-scorecard
template_slug:    cornice-architettura
phase:            X.5 · A.5 build (IT-only · pre-multilingual · pre-public-flip)
date:             2026-05-01
mean_score:       4.65/5
verdict:          PASS · ready for human visual review
```

## Panel-by-panel scores

| Panel | File | Score | Status |
|---|---|---|---|
| Build | `build-report.md` | 5.0 / 5 | PASS |
| Style-critic | `style-critic.md` | 4.7 / 5 | PASS |
| Contrast + accessibility | `contrast-accessibility.md` | 4.6 / 5 | PASS |
| Responsive auditor | `responsive-auditor.md` | 4.6 / 5 | PASS |
| Browser-verifier | `browser-verifier.md` | 4.7 / 5 | PASS |
| Release-gatekeeper | `release-gatekeeper.md` | 4.6 / 5 | PASS |
| **6-panel mean** | | **4.65 / 5** | **PASS** (floor 4.50) |

## Critical-dimension scoring

The cluster's 9 critical review dimensions (intake.md §10):

| Dimension | Score | Notes |
|---|---:|---|
| L1-L9 layout classification matches LF-2 row | 5.0 | every slot matches |
| Wireframe variance vs siblings ≥30% per pair | 5.0 | 9/9 or 8/9 distinct |
| Hero KPI overlay legible at 1920/1280/720 | 4.5 | KPI tuple visible at every viewport (after in-walk position fix) |
| Palette adjacency vs Continua resolved by surface deployment | 5.0 | rust on display surfaces · brass-only-in-chrome separation visible |
| Imagery distinctness vs Continua at 1280/1024 | 5.0 | exterior architectural vs interior reading-room — subject-class read at 1 second |
| Voice anchor preservation (one em-word) | 5.0 | 12/12 surfaces honor CS-TYPE-02 |
| Single portrait reads environmental not headshot | 4.5 | senior architect with drafting tools + working posture · borderline at very-tight crops, holds at 1280 |
| "Remove studio name" test on live render | 4.5 | sub-cluster vocabulary lands 11+ Tier 1/2 hits in first scroll |
| Whistleblowing column visible in 4-col footer | 5.0 | column-level surface rendered at all viewports |

**Mean critical-dimension score: 4.83 / 5** (well above 4.0 floor per intake §10).

## Blocking-finding count

`0 / 18` blocking findings open.

## Distinctness scores (planner-brief §15)

| vs sibling | 5-axis | layout-9-cell |
|---|---|---|
| Pragma (LF-1) | 5/5 | 9/9 |
| Fiscus (LF-3) | 5/5 | 9/9 |
| Solaria (LF-4) | 5/5 | 8/9 |
| Continua (LF-5) | 5/5 | 8/9 |

Distinctness gate (≥4/5) PASS. Layout-distinctness gate (CS-LAYOUT-12 ≥4/9) PASS by wide margin.

## Test-suite regression

`545 / 546 tests pass`. The single failure is the pre-existing booking-flag test (Continua-related), documented in the v15 baseline memory as "sole failure pre-existing booking-flag · unrelated".

## Frozen-sibling regression

`0 / 4 siblings regressed`. All 4 captured visually unchanged.

## Open questions for user-handshake

1. Does the LF-2 stacked-editorial hero feel sufficiently distinct from Continua's library reading-room hero at 1280 + 720?
2. Does the single-portrait masthead read environmental, NOT LinkedIn headshot, at 1280 + 768?
3. Does the 3+1 magazine grid land editorially, NOT as a generic gallery?
4. Does the cream-paper navbar feel right for the editorial-curatorial register, or should LF-2 ship a primary-bg variant?
5. Are the architectural-vocabulary density and the 3-time `argomento` motif reading as serious-editorial, NOT gatekeepy or repetitive?

## Verdict

```
PASS · 4.65 / 5
0 / 18 blocking findings
9 critical dimensions average 4.83 / 5
0 frozen-sibling regressions
545 / 546 tests pass (1 pre-existing · unrelated)

NEXT GATE: user-handshake on IT visual review
THEN:      workflow C (EN/FR/ES/AR + AR RTL)
THEN:      workflow D (public flip · tier=draft → tier=published_live)
```

The user-handshake is the binding next step. Workflow C (multilingual) and workflow D (public flip) are held until user GO.
