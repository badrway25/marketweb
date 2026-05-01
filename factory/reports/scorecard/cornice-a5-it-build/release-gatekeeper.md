# Release-gatekeeper panel · Cornice A.5 IT build

```yaml
panel:           release-gatekeeper
template_slug:   cornice-architettura
phase:           X.5 · A.5 build (PRE-multilingual · PRE-public-flip)
date:            2026-05-01
verdict:         PASS-WITH-HOLD-FOR-USER-HANDSHAKE
score:           4.6/5
gate_decision:   READY-FOR-IT-USER-REVIEW · NOT-READY-FOR-PUBLIC-FLIP
```

## Gate evaluation

The release-gatekeeper aggregates the 4 prior panels (build, style, contrast, responsive, browser) plus its own posture-check on tier semantics, locale coverage, and test-suite regression.

### Tier semantics

| Check | Status |
|---|---|
| `tier=draft` recorded in TEMPLATE_REGISTRY.json | YES |
| WebTemplate row `layout_family=LF-2` | YES |
| Anonymous catalog at `/templates/business/` shows 0 hits for `cornice-architettura` | YES (0 hits) |
| Staff catalog with `?preview=1` shows 5 hits for cornice slug (card + nav + price etc.) | YES (5 hits) |
| Staff preview reaches all 6 IT routes (200) | YES |
| Anonymous direct URL access returns 404 | YES |

D-055 staff-preview gate semantics intact. CS-MARKET-01 editor-preview body class guard inherited.

### Locale coverage

| Locale | Authored | Falls back to | Status |
|---|---|---|---|
| it | YES (CORNICE_CONTENT_IT) | — | DONE |
| en | NO | IT (per workflow C deferred) | PLANNED for workflow C |
| fr | NO | IT | PLANNED for workflow C |
| es | NO | IT | PLANNED for workflow C |
| ar | NO | IT | PLANNED for workflow C |

Per the task scope, IT-only at this build pass. Workflow C lands EN/FR/ES/AR + AR RTL on user-handshake GO.

### Distinctness verdict

5/5 vs every existing sibling on the planner-brief 5-axis matrix (voice · palette · hero geometry · hero subject · cases shape). 8/9 or 9/9 layout-distinctness.

### Imagery contract

| Check | Status |
|---|---|
| `business-architecture` pool registered | YES |
| 6 primary slots present in canonical [hero, feature, portrait, portrait, detail, ambient] order | YES |
| All 10 URLs (6 primary + 4 magazine extras) on `images.pexels.com` | YES |
| Cross-cluster grep against business-corporate / business-fiscal / business-coaching / business-stewardship | CLEAN at A.3 curator entry (0/26 IDs overlap) |
| Hero `w=1600` + feature `w=1200` + slots 2-5 `w=800` | YES |

CS-IMG-SRC-01 (Pexels-only) PASS · CS-IMG-POOL-01 (canonical 6-slot) PASS · CS-IMG-SRC-04 (cross-cluster grep clean) PASS.

### Test-suite regression

```
Ran 546 tests in 173.370s
FAILED (failures=1)
```

The 1 failure is `apps.catalog.tests.FreshSeedChainBackfillTests.test_medical_and_restaurant_templates_have_booking_flag` — a pre-existing test failure related to Continua's `has_booking=True` flag in the `business` cluster. The test expects ONLY medical+restaurant+lawyer+wave-2 templates to have booking flags; Continua flips the count.

This is the "545/546" pre-existing failure documented in the v15 baseline memory. **Cornice does not introduce new failures.** Cornice has `has_booking=False` (architecture-firm doesn't ship a consultation-booking widget; it ships a project-brief form gate at `/contatti/`).

### Frozen sibling regression

| Sibling | Verdict |
|---|---|
| Pragma (LF-1) | NO REGRESSION |
| Fiscus (LF-3) | NO REGRESSION |
| Solaria (LF-4) | NO REGRESSION |
| Continua (LF-5) | NO REGRESSION |

All 4 captured visually unchanged from v15 baseline.

## Aggregate panel scores

| Panel | Score |
|---|---|
| build-report | 5.0/5 |
| style-critic | 4.7/5 |
| contrast-accessibility | 4.6/5 |
| responsive-auditor | 4.6/5 |
| browser-verifier | 4.7/5 |
| release-gatekeeper | (this) 4.6/5 |
| **6-panel mean** | **4.7/5** |

Mean ≥ 4.50 floor. Distinctness ≥ 4/5. Layout-distinctness ≥ 4/9. All blocking checks clear. The pre-existing booking-flag failure is unrelated and documented as carry-over from the v15 baseline.

## Open `[BLOCKING]` findings

**0 / 18 blocking findings open.**

## Decision

```
PASS for IT-user-review handshake.
HOLD on public flip (workflow D) until:
  1. User signs off on IT walk
  2. Workflow C lands EN/FR/ES/AR + AR RTL
  3. AR Naskh-vs-Kufi heading-font decision per planner-brief §11
  4. /pubblicazioni/ page authored OR officially deferred to phase-2
  5. Re-run distinctness + contrast + responsive across all 5 locales
  6. Re-bind voice anchor verbatim-in-translation across 5 locales
```

The user-handshake is the next gate. Per `intake.md §10`, this is the first LF-2 occupant — the review cost is higher than typical. A HOLD here is more likely than for a 5th+ in an established sub-cluster.

## Score: 4.6/5

Gatekeeper aggregator clears. IT pass is ready for human visual review. Public flip is held by design until workflow D post-multilingual + post-handshake.
