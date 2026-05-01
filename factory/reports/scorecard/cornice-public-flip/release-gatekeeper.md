# Release-gatekeeper · Cornice Public Flip · 2026-05-01

**Verdict**: GREEN · `tier=draft → published_live` · APPLIED · cascade closed
**Branch**: `phase-x5-cornice-public-flip`
**Predecessor**: workflow D `release-gatekeeper.md` (HOLD · APPROVED-PENDING-HANDSHAKE)
**Trigger**: explicit user authorization in this conversation (2026-05-01)
**Aggregate**: 4.97 / 5 (workflow D · unchanged at flip · no fresh scoring required)

---

## 1 · Decision

**APPLY public flip.** The user provided the parallel-verification handshake
required by SOP §5.4 / R-SOL-8 / D-102 / CS-BLOCK-13. The workflow D §6
cascade was applied verbatim. Cornice is now `tier=published_live` in both
the registry and the DB.

## 2 · Cascade applied (vs. workflow D §6 plan)

| # | Step | Plan (workflow D) | Actual | Verdict |
|---|---|---|---|---|
| 1 | Registry flip | `tier: draft → published_live` on Cornice row · `tier_reason` rewrite | Applied · 1 line tier flip + tier_reason rewritten to consolidate workflow A.5 → D + flip audit trail | ✓ |
| 2 | DB sync | `python manage.py sync_template_tiers` propagates registry → DB · 23 → 24 live | Executed · `cornice-architettura: draft -> published_live` · 24 live / 0 draft | ✓ |
| 3 | Trust counter | search for `23+`/`23` literals; bump to `24+`/`24` per Continua precedent (~7 bumps) | 7 explicit-literal bumps in `apps/catalog/tests.py` (L824, L862, L868, L1134, L1141, L1554, L1556) · the home-rendered `23+` is fully dynamic from DB filter so no template/view edit was needed | ✓ |
| 4 | Tier-fact tests | re-run corporate-suite contract tests; expect Cornice in live count | Re-ran full suite: **545/546 PASS** · same single pre-existing booking-flag failure as workflow D baseline · Cornice now appears in live counts as expected | ✓ |
| 5 | Cluster smoke | catalog-card reachability + 5/5 Cornice locale routes anonymous (formerly 404, now 200) + 546 test suite | 45/45 anonymous routes 200 (5 locales × 5 pages + 5 locales × 4 case-detail) · 4/4 frozen siblings 200 anon · 545/546 tests | ✓ |
| 6 | MEMORY rollup | append `phase_x5_cornice_workflowD_public_flip.md` checkpoint pointer · promote workflow C from CURRENT to RECENT · bump baseline pointer to 24-template live catalog | Applied as `phase_x5_cornice_public_flip.md` (matches established naming pattern from `phase_x4_continua_public_flip.md`) · MEMORY.md index updated · workflow C promoted to RECENT | ✓ |
| 7 | Public visit verification | anonymous probes show 200 / slug-present / locale-switcher / AR RTL working anon | All 4 captures + DOM probes confirm anon reachability · Cornice slug × 5 in catalog HTML · home counter `24+` · AR `dir=rtl` + Naskh h1 · 0/4 frozen-sibling regression | ✓ |
| 8 | Server | record shutdown timestamp | Server kept running at `http://127.0.0.1:8052/` for any user-side post-flip verification (no shutdown — left up per task constraint "keep server running and report URL/port") | n/a (left up) |

## 3 · Additional re-binding (not in workflow D plan, but applied)

`apps/catalog/tests.py · test_pragma_falls_back_gracefully` (L1265) was bumped
from default `limit=3` to explicit `limit=4`. Reason: with Cornice live, the
style-layer (`classic-serif`) returns 3 corporate-suite siblings (Continua +
Cornice + Lex) so Elevate is bumped from the 3-slot default. The test asserts
both Lex AND Elevate must surface as proof of layered fallback (cluster →
style → category) — bumping the limit preserves the test's intent. The UI
surface that consumes this selector still defaults to 3 slots and is
unchanged. This is the kind of "negative test re-binding" workflow D §6.7
explicitly anticipated.

## 4 · Layer-1 / Layer-2 / Layer-3 (post-flip · re-bound)

The workflow D scoring was not re-issued (the public flip does not change the
visual product · only the tier-gate). All 18 blocking overrides remain NO,
all 9 critical dimensions remain ≥ 4, aggregate remains 4.97/5. The flip's
own observability is verified via:

- **L1**: O18 "no live walk" — cleared by the 4-capture anon walk in
  `browser-verifier.md`
- **L1**: O13 "walk URL + port not recorded" — cleared (URL `http://127.0.0.1:8052/`
  + port recorded in build-report §7 + browser-verifier §1)
- **L1**: O2 "horizontal scrollbar" — cleared at IT 1440 (1425 ≤ 1440) and AR 1440 (1425 ≤ 1440)
- **L2**: D14 browser live verification — cleared (4 distinct anon walks added
  to the 4 prior staff walks across A.5/A.6/C/D)
- **L3**: aggregate ≥ 4.3 — preserved at 4.97 (no regression introduced by the flip)

## 5 · Risk register at landing

| Risk | Pre-flip | Post-flip |
|---|---|---|
| Tier flip breaks anonymous catalog | n/a | MITIGATED · 45/45 anon routes 200 · catalog header `6 template disponibili` · slug × 5 in HTML |
| Trust counter doesn't update | n/a | MITIGATED · home renders `24+` from live DB filter · zero template edit |
| Registry/DB drift | n/a | MITIGATED · `sync_template_tiers` reports 1 row updated · post-flip query = 24 live / 0 draft |
| Tier-fact tests fail post-flip | EXPECTED | MITIGATED · 7 explicit-literal bumps + 1 related-templates re-binding · suite at 545/546 (same pre-existing failure) |
| AR Naskh swap leaks across LF families | LOW | MITIGATED · Continua LF-5 AR h1 still `Noto Kufi Arabic` (zero leakage) · selector-scoped to `body.cs-lf-lf-2` |
| Frozen-sibling regression | LOW | MITIGATED · Pragma/Fiscus/Solaria/Continua all 200 anon |
| Pre-existing booking-flag test | LOW | DOCUMENTED · same Continua-related failure as workflow D · zero new regressions |
| LEGACY_EXEMPT_KEYS warning | LOW | DOCUMENTED · `(corporate_suite.W001)` is the same advisory observed at every prior corporate-suite pass · AP3 retro-curation backlog · not a flip blocker |

No HIGH/MEDIUM risk active post-flip. Two LOW items (booking-flag failure +
W001 advisory) are documented carry-overs · not introduced by the flip.

## 6 · Server / route status (handed back to orchestrator · live · post-flip)

```
server:                 python manage.py runserver 127.0.0.1:8052 --noreload
URL prefix:             http://127.0.0.1:8052/
template root URL:      /templates/business/cornice-architettura/preview/
9 routes × 5 locales = 45 ANONYMOUS routes (all 200, no ?preview=1 needed):
  IT  /preview/ (and /studio/ /servizi/ /progetti/ /contatti/ + 4 case-detail slugs)
  EN  ?lang=en  on every route above
  FR  ?lang=fr  on every route above
  ES  ?lang=es  on every route above
  AR  ?lang=ar  on every route above (dir=rtl · Naskh h1)
tier:                   published_live (anonymous: 200 · ?preview=1: 200 no-op)
catalog count:          24 published_live + 0 draft = 24 total

frozen siblings (all 200 anonymous):
  - /templates/business/pragma-corporate-suite/preview/       LF-1
  - /templates/business/fiscus-commercialista/preview/        LF-3
  - /templates/business/solaria-coaching/preview/             LF-4
  - /templates/business/continua-stewardship/preview/         LF-5

corporate-suite cluster: 5 live siblings (was 4) · all 5 LF slots populated
                         (Pragma LF-1 · Cornice LF-2 · Fiscus LF-3 · Solaria LF-4 · Continua LF-5)

test suite:             546 tests · 545 pass · 1 pre-existing failure
                        (test_medical_and_restaurant_templates_have_booking_flag
                         · Continua-related · pre-dating Cornice · UNRELATED to the flip)
```

The dev server stays open at port 8052 for any user-side post-flip review.

## 7 · Verdict

**APPLIED · GREEN.** Cornice's public-flip is fully observable to anonymous
visitors. The workflow D §6 cascade landed verbatim with one anticipated
related-templates test re-binding. The corporate-suite cluster ships 5 live
siblings with all 5 LF slots populated. The X.5 Cornice pipeline (workflow
A.5 → A.6 → C → D → public flip) is closed.
