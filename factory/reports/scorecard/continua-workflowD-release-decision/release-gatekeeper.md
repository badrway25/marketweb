# Release-gatekeeper · Continua Workflow D Release Decision · 2026-04-30

**Verdict**: HOLD public flip · `tier=draft` preserved · `release-ready in principle`, **not** `flip now`
**Aggregate**: 4.97 / 5 · 0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new
**Branch**: `phase-x4-continua-workflowD-release-decision`
**Run timestamp**: 2026-04-30
**Status tag**: APPROVED-PENDING-HANDSHAKE

---

## 1 · Decision

**HOLD public flip.** Tier remains `draft` in DB and registry.

The technical work is complete. Layer 1 (overrides), Layer 2 (critical floors), and Layer 3 (aggregate) all clear with margin. The cluster's release contract requires one additional element that the technical pipeline cannot provide: the user parallel-verification handshake (CS-BLOCK-13 / O13 · cluster R-SOL-8 · SOP §5.4 · D-102 cadence). Until that handshake lands in the conversation, the gatekeeper holds.

This is the conservative reading of the task constraint **"if there is any meaningful doubt, HOLD wins"** — but the doubt here is not a defect doubt; it is a process doubt. The cluster-wide rule that the user must walk the live preview themselves before LIVE flip is the entire point of the corporate-suite SOP §5.4 handshake; auto-flipping on technical greenness would short-circuit it.

---

## 2 · Layer 1 · Blocking-override review

| # | Override | Triggered? | Source agent | Evidence |
|---|---|---|---|---|
| O1  | h1..h5 distance < 120 OR WCAG < 4.5 | NO | contrast-accessibility | walk §5 · h1 ≈ 11–13:1 · KPI / CTA / nav 11.03:1 |
| O2  | Horizontal scrollbar at any viewport | NO | responsive | walk §2 (1440 1425=1425) + §3.4 (AR 720 705=705) |
| O3  | Hero / nav fail to stack at ≤ 720 | NO | responsive | LF-5 IT rebuild §7 + Pass B AR-720 capture |
| O4  | Imagery URL 404 on live | NO | imagery-curator | LF-5 IT rebuild §6 + Pass B §10 (45/45 routes 200) |
| O5  | Imagery 3-second semantic fail | NO | imagery-curator | Pass 1 §6 (slot 0 re-curate) + IT 1440 capture |
| O6  | Imagery mood vs voice anchor | NO | imagery-curator | Pass 1 §3 (room-architectural stewardship) |
| O7  | Non-Pexels URL on a new pilot | NO | imagery-curator | LF-5 IT rebuild §6 + Pass B §10 (8 Pexels IDs) |
| O8  | Editor affordance on `/preview/` | NO | style-critic | Pass B walk · `cs-lf-lf-5 lm-ready` body class |
| O9  | Lorem ipsum / placeholders | NO | style-critic / copy-live | Pass B `style-critic.md` |
| O10 | Fake certifications | NO | copy-live | OAM · ANC · Albo dei Trustees · STEP · D.lgs. 24/2023 (real) |
| O11 | Voice anchor missing in any locale | NO | copy-live | walk §3.1 (5/5 locales verbatim-in-translation) |
| O12 | D-054 10-gate triangulation absent | NO | copy-live | `continua-distinctness-proof.md` 5/5 vs Pragma · Fiscus · Solaria |
| O13 | Walk URL + port not recorded | **half-met** | gatekeeper | URL recorded (`http://127.0.0.1:8051/`) · **user confirmation pending** |
| O14 | Walk missing any rubric viewport | NO | browser-verifier | LF-5 IT rebuild 1920/1440/1100/720/480 + Pass B + this pass |
| O15 | Evidence directory incomplete | NO | browser-verifier | Aggregate ≥120 captures + measurements + walk-log files in 4 prior packets |
| O16 | Nav polarity broken / >1 accent | NO | style-critic | regression-walk §2 (nav background = `--primary`, single brass underline) |
| O17 | Dark-on-dark in `.dark` sections | NO | contrast | walk §5 (KPI/CTA/nav 11.03:1 ≥ 7.0 AAA) |
| O18 | No live walk | NO | browser-verifier | This pass performed a live walk · 5 locales × 1440 + AR 720 |

**0 / 18 overrides triggered.** O13's "URL recorded" half is met; the "user confirmation" half is the handshake described above and is the reason the gatekeeper holds.

## 3 · Layer 2 · Critical-dimension floor review

| D# | Dim | CRITICAL? | Score | Floor | Met? | Source |
|---|---|---|---|---|---|---|
| D1  | Premium feel | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild scorecard `style-critic.md` + workflow-D §3 of release decision |
| D2  | Elegance | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild scorecard `style-critic.md` |
| D3  | Modern professionalism | ✓ | 5 | ≥ 4 | YES | Pass B `style-critic.md` (5/5 locale register guides) |
| D4  | Hero readability | ✓ | 5 | ≥ 4 | YES | walk §5 (≥11:1 AAA) |
| D5  | Navbar quality | — | 5 | ≥ 3 | YES | regression-walk §2 (cs-nav cs-nav--lf5 64px LF-5-correct) |
| D6  | Footer quality | — | 5 | ≥ 3 | YES | LF-5 IT rebuild §3 (4-col-with-whistleblowing) |
| D7  | Typography hierarchy | — | 5 | ≥ 3 | YES | Pass B `style-critic.md` (5 italic-em / locale · 4 fonts active under AR) |
| D8  | Spacing rhythm | — | 5 | ≥ 3 | YES | LF-5 IT rebuild §7 (`--space-section-y/x` per CS-RHYTHM-01) |
| D9  | Imagery quality | — | 4.5 | ≥ 3 | YES | LF-5 IT rebuild scorecard (pillar icons grayscale-flattened from 4 photographers · STRONG observation only) |
| D10 | Imagery coherence | ✓ | 5 | ≥ 4 | YES | Pass 1 §6 + Pass B §10 (`_POOL_*` substitution structurally impossible) |
| D11 | Pexels-only compliance | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild §6 (8 Pexels IDs · zero non-Pexels) |
| D12 | Contrast safety | ✓ | 5 | ≥ 4 | YES | walk §5 + Pass B `contrast-accessibility.md` |
| D13 | Responsive quality | ✓ | 5 | ≥ 4 | YES | LF-5 IT rebuild §7 (1920/1440/1100/720/480) + AR 1440/720 · zero overflow |
| D14 | Browser live verification quality | ✓ | 5 | ≥ 4 | YES | regression-walk + LF-5 IT rebuild + Pass B + this pass = 4 distinct walks |
| D15 | Text/image coherence | — | 5 | ≥ 3 | YES | Pass B `style-critic.md` (multi-generational tone preserved 5/5 locales) |

**All 9 CRITICAL dimensions ≥ 4: YES.** All 6 non-critical dimensions ≥ 3: YES. Aggregate (mean of 15) = (5+5+5+5+5+5+5+5+4.5+5+5+5+5+5+5)/15 = **4.97 / 5**.

## 4 · Layer 3 · Aggregate

| Gate | Threshold | Actual | Met? |
|---|---|---|---|
| Overall average | ≥ 4.3 | 4.97 | YES (margin 0.67) |
| `[BLOCKING]` outstanding | 0 | 0 | YES |
| `[REQUIRED]` outstanding | 0 | 0 | YES |
| All 9 CRITICAL ≥ 4 | required | all = 5 | YES |
| All 6 non-critical ≥ 3 | required | min = 4.5 | YES |
| Evidence directory | complete | ≥120 captures across 4 walk packets + 70 cells × 5 locales instrumented + 45-route smoke | YES |
| Server URL + port recorded | required | `http://127.0.0.1:8051/` | YES |

Per `corporate-suite-quality-scorecard.md §6.1`: this profile maps to **PASS · reference class** (the "all 15 at 5" row), modulo the handshake.

## 5 · Per-locale flip-decision matrix

| Locale | Walk verdict | BLOCKING | Anchor preserved? | RTL parity? | Recommended |
|---|---|---|---|---|---|
| IT | PASS | 0 | ✓ generazioni | n/a | flip-eligible at workflow D handshake |
| EN | PASS | 0 | ✓ generations | n/a | flip-eligible at workflow D handshake |
| FR | PASS | 0 | ✓ générations | n/a | flip-eligible at workflow D handshake |
| ES | PASS | 0 | ✓ generaciones | n/a | flip-eligible at workflow D handshake |
| AR | PASS | 0 | ✓ بالأجيال | ✓ | flip-eligible at workflow D handshake |

5 locales · 5 PASS · 0 BLOCKING. The flip can land on all 5 simultaneously when the user authorizes — there is no held-locale subset.

## 6 · Pass-D / public-flip cascade (documented to the line)

When the user authorizes, the gatekeeper applies, in order:

1. **Registry flip** — single-line `Edit` on `TEMPLATE_REGISTRY.json` line 337: `"tier": "draft"` → `"tier": "published_live"`.
2. **DB sync** — `python manage.py sync_template_tiers` propagates registry → DB. Distribution moves 22 published_live / 1 draft → 23 published_live / 0 draft.
3. **Trust counter** — locate the marketplace counter string `22+` (or equivalent) used on `/templates/business/` and bump to `23+`. (Check before editing — the registry-derived count may already be authoritative.)
4. **Tier-fact tests** — re-run the 6 corporate-suite contract tests that scan tier-fact (Pass B `release-gatekeeper.md §4.3`); expect Continua now in the live count, not the draft count. If any test hard-codes "5 corporate-suite live siblings" expect to bump it to 6.
5. **Cluster smoke** — re-run the 23/23 catalog-card reachability smoke + the full 546/546 test suite + the 5/5 Continua locale routes. The pre-existing booking-flag failure is the only allowed deviation.
6. **MEMORY.md roll-up** — append a `phase_x4_continua_workflowD_release_decision.md` checkpoint pointer; promote `phase_x4_continua_passB_multilingual.md` from CURRENT to RECENT; update the CURRENT baseline pointer line to reflect the 23-template live catalog.
7. **Public visit verification** — anonymous probes after the flip should show: `/templates/business/continua-stewardship/preview/` → 200 (not 404); slug present in `/templates/business/` HTML; locale switcher visible to anon; `?lang=ar` AR RTL working anon. Negative tests too: any test that asserts Continua is *absent* from the live catalog must be revised.
8. **Server shutdown** — record the shutdown timestamp on this scorecard.

The flip is 1 file edit + 1 management command + 1 trust-counter edit + 1 MEMORY rollup + 1 cluster smoke. Not complex. The reason the flip is held is the handshake, not the work.

## 7 · Risk register

| Risk | Severity | Mitigation status |
|---|---|---|
| Voice anchor lost on a translation | HIGH | MITIGATED · 5/5 verbatim-in-translation (walk §3.1) |
| LF-5 layout reshapes under RTL | HIGH | MITIGATED · DOM verified identical across 5 locales · zero overflow at every viewport |
| Arabic typography breaks (Latin tracking) | MEDIUM | MITIGATED · CS-TYPE-05 reset live-verified (walk §3.3) |
| Cross-locale imagery substitution | MEDIUM | MITIGATED · `_POOL_*` constants make substitution structurally impossible |
| `?preview=1` leak across locale switcher | MEDIUM | MITIGATED · staff-preview-aware href generation works on all 5 locale pills |
| Anonymous catalog leak after tier-flip prep | LOW | MITIGATED · slug is absent from `/templates/business/` HTML at draft tier |
| Pre-existing booking-flag test failure | LOW | DOCUMENTED · out of scope (pre-dates Continua · independent feature surface) |
| Sibling regression (Pragma · Fiscus · Solaria) | LOW | MITIGATED · 0 px drift per regression-walk §3 |
| Pillar-icon photographer cohesion | LOW (D9 STRONG) | DOCUMENTED · grayscale flattens to monochrome · imagery-hardening pass deferred |
| Hero `<picture>` + srcset not introduced | LOW | DOCUMENTED · imagery-hardening pass deferred · not blocking |
| Pragma↔Fiscus 2/9 layout-distinctness | LOW | DOCUMENTED · cluster audit deferred · does not affect Continua's 8–9/9 distinctness |

No HIGH or MEDIUM risk left active. Two LOW items (pillar-icon cohesion + `<picture>`) are documented for the next imagery-hardening pass.

## 8 · Parallel-verification handshake block

The dev server remains at **http://127.0.0.1:8051/**. URLs to walk:

```
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?preview=1            (IT)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=en&preview=1    (EN)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=fr&preview=1    (FR)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=es&preview=1    (ES)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=ar&preview=1    (AR · RTL)
```

User: please open these URLs in your own browser (logged in as `cs_review_fix` or any `is_staff=True` account) and confirm visual parity with the walk evidence before the registry flip proceeds. On confirmation ("confirmed · proceed with Commit B" or equivalent), the gatekeeper applies the §6 cascade.

## 9 · Pending Commit B diff (NOT applied)

```diff
--- TEMPLATE_REGISTRY.json
+++ TEMPLATE_REGISTRY.json
@@ -334,7 +334,7 @@
       "price": 89,
       "featured": false,
       "status": "draft",
-      "tier": "draft",
+      "tier": "published_live",
       "tier_reason": "Phase X.4 design-orchestrator first real candidate ..."
```

Single-line edit. **NOT applied.** Awaits user explicit confirmation in the conversation per SOP §5.4 / gatekeeper §3.2.

## 10 · Verdict

**APPROVED-PENDING-HANDSHAKE.** Continua workflow D is release-ready in principle (4.97/5 · 0 overrides · all critical floors met · all evidence packages complete). The flip is held until the user explicitly authorizes parallel-verification confirmation in the conversation. Server is kept running. Tier is preserved at `draft`.

If meaningful doubt arises during the user walk, the gatekeeper holds. If the walk lands clean, the §6 cascade is documented to the line so the flip ships without re-discovery.
