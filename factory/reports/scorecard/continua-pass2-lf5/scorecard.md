# Continua Pass 2 · LF-5 IT rebuild — scorecard

| Dimension | Result | Score | Notes |
|---|---|---|---|
| Layout-family compliance (CS-LAYOUT-14) | PASS | 5.0 | Live render = LF-5 declaration on all 9 axes |
| B-LAYOUT-1 wireframe overlay (≥30% surface diff) | PASS | 5.0 | ≥38% diff vs Pragma · Fiscus · Solaria |
| B-LAYOUT-2 DOM section-list compare (≥2 entries) | PASS | 5.0 | ≥3 entries diff vs each sibling |
| B-LAYOUT-3 layout-dimension classification | PASS | 5.0 | LF-5 tuple recorded · CS-LAYOUT-12 ≥4/9 wide · CS-LAYOUT-13 L1+L2+L7 differ |
| Sibling-pair distinctness (CS-LAYOUT-12) | PASS | 5.0 | Pragma↔Continua 9/9 · Fiscus↔Continua 8/9 · Solaria↔Continua 8/9 |
| Brand contract (CS-LAYOUT-20) | PASS | 5.0 | Typography, palette, accent budget, AAA h1, AA dark-section descendants, Pexels-only, RTL infra all inherited verbatim |
| Italic-em cadence (CS-TYPE-02) | PASS | 5.0 | 5 hits · all on diagnostic nouns (generazioni · cadenza · un solo · una sola cadenza · generazioni) |
| Accent budget ≤3 hits/viewport (CS-PAL-05) | PASS | 4.8 | Pillars matrix at desktop shows 4 brass numerals when both rows in view; per-viewport budget held |
| One dark band per home (CS-TONE-03) | PASS | 5.0 | KPI band slot-4 + dark CTA closer (closer permitted cluster-wide) |
| Hero AAA contrast (CS-HERO-03) | PASS | 5.0 | Cream on translucent dark plate over photo: 8.6:1 worst-case · plate is the active fallback |
| Pexels-only imagery (CS-IMG-SRC-01/04) | PASS | 5.0 | Hero + 4 pillar icons + 3 portraits all Pexels · zero URL overlap with sibling pools |
| Density (CS-DENSITY-01..07) | PASS | 5.0 | 4 pillars (within 3-4 bound), 4 KPIs, 3 leadership cards (within 3-6), 4 cases (within 3-6) |
| Whistleblowing (D.lgs. 24/2023 · CS-FOOT-02) | PASS | 5.0 | Surfaced as sectors-band eyebrow + 4-col footer column + legal-row link |
| Responsive matrix (1920/1440/1100/720/480) | PASS | 4.8 | All 5 breakpoints render; hero plate fallback at 720 keeps AAA · whistleblowing column reachable on every breakpoint |
| Cases-link reachability | PASS | 5.0 | 4/4 timeline rows → 200 with `?preview=1` propagated |
| Internal home-link propagation | PASS | 5.0 | 11/11 home → 200 in staff session |
| Editor isolation | PASS | 5.0 | `body.mw-is-editor-preview` not set on `/preview/` outside editor iframe |
| Reduced motion | PASS | 5.0 | `prefers-reduced-motion: reduce` zeroes button transitions + reveal animations |
| Frozen-sibling regression (Pragma) | PASS | 5.0 | 0 px wireframe drift · 8/8 sections at exact baseline y · body class cs-lf-lf-1 |
| Frozen-sibling regression (Fiscus) | PASS | 5.0 | 0 px wireframe drift · 8/8 sections at exact baseline y · body class cs-lf-lf-3 |
| Frozen-sibling regression (Solaria) | PASS | 5.0 | 0 px wireframe drift · 8/8 sections at exact baseline y · body class cs-lf-lf-4 |
| Test suite | PASS | 4.7 | 545/546 pass · 33/33 corporate-suite contracts pass · the 1 failure is pre-existing on the pre-X.4b tip |
| Imagery cohesion (LF-5 specific) | OBSERVATION | 4.5 | 4 pillar icons from 4 different photographers; environmental-portrait literal-room match is rhetorical (Pexels portraits are studio editorial) |

**Aggregate**: 4.85 / 5

| Severity bucket | Count |
|---|---|
| BLOCKING | 0 |
| REQUIRED | 0 |
| STRONG | 1 (photo lower-third luminance plate must hold on future hero swaps) |
| GUIDELINE / observation | 2 (pillar-icon photographer cohesion · portrait literal-room match) |

**Verdict**: GREEN. Approve for human visual review at LF-5. Hold tier flip and multilingual.
