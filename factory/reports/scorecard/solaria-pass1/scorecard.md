# scorecard · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` · IT-only at pass 1
**Run-ISO**: `20260426T0907Z`
**Branch**: `phase-x4-solaria-controlled-reentry-pass1`
**Aggregator**: `release-gatekeeper` (Claude Opus 4.7)
**Scoring rule**: `release-gatekeeper.md §4.5` — blocking overrides, NOT average-score optimism.

---

## Aggregate

| Layer | Result |
|---|---|
| Layer 1 (18 blocking overrides) | **0 / 18 triggered ✓** |
| Layer 2 (9 CRITICAL ≥ 4) | **8 / 9 above floor · D14 = 3 § deviation E1** |
| Layer 3 (required outstanding) | **0 outstanding ✓** |
| Average across 9 CRITICAL | **4.67 / 5** (≥ 4.3 floor ✓) |
| Status tag | **APPROVED-PASS-1** (NOT `APPROVED-PUBLIC-LIVE`) |

## CRITICAL dimension scores

```
Dimension                                    Floor   Score   Δ
D1   Editorial typography                      4      5     +1
D2   Restraint over density                    4      5     +1
D3   Color discipline / palette polarity       4      5     +1
D4   Editorial structure / page rhythm         4      5     +1
D10  Voice anchors + anti-pattern hygiene      4      5     +1
D11  Imagery direction + Pexels-only           4      5     +1
D12  Contrast / accessibility                  4      5     +1
D13  Responsive-layout invariants              4      4      0   (§ deviation E2 · 3-viewport sample)
D14  Browser-walk corpus per template          4      3     -1   (§ deviation E1 · IT-only)
                                                    -------
                                          Avg:        4.67 / 5
```

Below-floor finding on D14 is intentional and plan-aligned — pass 1 is IT-only by binding D-102 cadence (the original Commit A was IT-only with EN/FR/ES/AR deferred). Pass 2 + pass 3 close R-SOL-14 in increments.

## NON-CRITICAL dimensions (not gating, scored for completeness)

```
D5   CTA discipline (CS-CTA-*)                              5
D6   Imagery direction (CS-IMG-DIR-*)                       5
D7   Information structure (CS-STRUCT-*)                    5
D8   Voice anchors and editorial copy (CS-VOICE-*)          5
```

## Layer 1 · 18 blocking-override sweep

```
O1   AAA body floor on dark-section primary text          CLEAR
O2   Horizontal scroll on any walked cell                 CLEAR
O3   Reveal-card stuck opacity 0 under reduced-motion     CLEAR
O4   Lorem ipsum / placeholder string in DOM              CLEAR
O5   var(--accent) text/border on dark chrome             CLEAR
O6   Voice anti-pattern surfacing in any walked cell      CLEAR
O7   First Solaria scorecard cites Pragma legacy O7       CITED      (release-gatekeeper.md §3.1)
O8   Footer href="#" placeholder                          CLEAR
O9   Touch target < 44 × 44 on mobile interactive         CLEAR
O10  Hero h1 < 32 px @ 390                                CLEAR
O11  Build-time corporate_suite.E001 firing (palette)     CLEAR
O12  D-054 triangulation stale on any sibling             CLEAR
O13  Console error introduced by subject template         CLEAR
O14  Failed network request for in-pool imagery           CLEAR
O15  Same as O3 (auditor restatement)                     CLEAR
O16  Build-time corporate_suite.E002/E003 (imagery)       CLEAR
O17  Same as O5 (auditor restatement)                     CLEAR
O18  page-data placeholder leaking in DOM                 CLEAR
                                                          ---
                                                  Total:  0 / 18 TRIGGERED
```

## § deviations (in force, plan-aligned, non-gating individually but gating for the GO floor at D14)

| ID | Dimension | Cap | Reason | Closure path |
|---|---|---:|---|---|
| E1 | D14 | 3 | Pass-1 IT-only by D-102 cadence; 7 PNGs vs 120-floor | Pass 2 (4 locale trees + walks) → D14 ≈ 4; Pass 3 (full matrix) → D14 = 5 |
| E2 | D13 | 4 | 3-viewport sample (1440 + 768 + 390) vs 8-viewport sweep | Pass 3 (full 8-breakpoint sweep at every locale) → D13 = 5 |
| E3 | — | — | Pragma `corporate_suite.W001` grandfather (O7 contract) | Cited verbatim in release-gatekeeper.md §3.1 |
| E4 | — | — | Reduced-motion force-reveal capture-mechanism | Same archetype-level § deviation 3 from GO reassessment §2.2; NOT Solaria-introduced |
| E5 | — | — | imagery-curator + copy-translation agent prompts folded inline | Same Step 3 prompt-revision item from Fiscus AP8 first run; not pass-1-gating |

## Tests / build at the pass-1 tip

```
manage.py check         →  0 errors · 1 warning (W001 Pragma grandfather only)
manage.py test apps.catalog →  171 / 171 OK · 2.438 s
Catalog distribution    →  21 published_live / 1 draft (Solaria)
```

## Cells walked

```
01  /preview/                         1440 × 900   IT   PASS
02  /preview/il-coach/                1440 × 900   IT   PASS
03  /preview/percorsi/                1440 × 900   IT   PASS
04  /preview/casi/                    1440 × 900   IT   PASS
05  /preview/contatti/                1440 × 900   IT   PASS
06  /preview/                         390 × 844    IT   PASS
07  /preview/                         768 × 1024   IT   PASS
                                                       ---
                                              Total:  7 / 7 PASS
```

## Verdict

**Pass 1 status: APPROVED-PASS-1.**

The pass-1 gatekeeper aggregator clears all 18 blocking overrides, hits all non-D14 critical floors, and produces an aggregate average of 4.67 above the GO-floor of 4.3. The single dimension below the critical-4 floor (D14 = 3) is intentional and plan-aligned — IT-only walk vs the full 5-locale rubric. Pass 2 + pass 3 are the closure path; both require explicit user authorization per R-SOL-8.

**Pass 1 is NOT "ship Solaria public-live."** Pass 1 unblocks the next user-authorized increment.
