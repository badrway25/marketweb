# Release-gatekeeper · post-Cornice reference hardening · 2026-05-03

**Verdict**: GREEN · governance hardening pass APPLIED · 6th-sibling intake **may now open**
**Branch**: `phase-x5-post-cornice-reference-hardening`
**Predecessor**: post-Cornice public flip (`phase_x5_cornice_public_flip.md` · 2026-05-01)
**Aggregate**: not scored — this is a documentation hardening pass · no rendered visual product to score.

---

## 1 · Decision

**APPLY the post-Cornice reference hardening.** All four preconditions of `factory/reports/hardening/post-cornice-next-candidate-readiness.md §2` are closed:

| Precondition | Status | § decision pointer |
|---|---|---|
| **P1** · 5-column reference layer | CLOSED | 3 orchestrator-side files refreshed (distinctness-matrix v2 · reference-pack v2 · layout-family-assignment v2) |
| **P2** · Pragma↔Fiscus 2/9 § decision | CLOSED · Option C (formal acceptance) | filed at `factory/reports/hardening/corporate-suite-layout-family-matrix.md §6` · CS-LAYOUT-12 reworded at `corporate-suite-layout-variance-rules.md §2` · single-exception ladder named |
| **P3** · Booking-flag test noise | CLOSED · re-cohorted (Continua added · Wave-2 booking-shaped) | `apps/catalog/tests.py:656-688` · 1 slug + comment · suite reads 546/546 |
| **P4** · 45-route smoke + 5-sibling 1920px regression | CLOSED · 45/45 anonymous routes 200 · 0/0 drift · AR Naskh/Kufi re-probe clean | `factory/reports/browser-verification/post-cornice-reference-hardening.md` |

**The 6th-sibling intake's blocker (stale reference layer + undocumented near-occupant pair + noise floor) is removed.** The orchestrator may now open the 6th sibling's enrollment on the next user authorization.

---

## 2 · Cascade applied (vs. `post-cornice-next-candidate-readiness.md §10` plan)

| # | Step | Plan | Actual | Verdict |
|---|---|---|---|---|
| 1 | Refresh `corporate-suite-distinctness-matrix.md` to 5 columns | Use live-family-map + cornice-lf2-reference-pack as sources of truth | Full rewrite v2 · 12 dimensions × 5 columns · pre-filled "evidence-led legal LF-2 second occupant" guide-rail · § decision summary at §4 | ✓ |
| 2 | Refresh `corporate-suite-reference-pack.md` to 5 columns | Add §1 entries for Cornice + Continua · §4-7 update · §10 quick-lookup 5-col | Full rewrite v2 · §1 entries added with full "best move · don't copy" decomposition · §2 patterns table flagged with family-scope columns · §4 5-pack imagery rhythm · §5 5-row typography · §6 5-variant section pacing · §7 cream-paper + condensed-minimal-top + 4-col-with-whistleblowing variants · §10 quick-lookup 5-col · §11 paragraph refreshed | ✓ |
| 3 | Refresh `corporate-suite-layout-family-assignment.md` to live state | Continua live at LF-5 · Cornice live at LF-2 · 5×5 pair table · 6 open territory updated | Full rewrite v2 · §1 5-row map + superseded LF-3 row preserved · §2 reasoning extended · §3 freeze list extended · §5 10-pair scoring matrix · §6 LF-1..LF-5 TAKEN · §8 6th-sibling intake precondition checklist | ✓ |
| 4 | File Pragma↔Fiscus 2/9 § decision (recommended Option C) | Formal acceptance · CS-LAYOUT-12 wording update at variance rules · § decision at family-matrix §6 | Filed in 4 cross-referenced places (factory matrix §6 · variance rules §2 · orchestrator distinctness matrix §4 · orchestrator family assignment §5) · single-exception ladder named · operational consequence enumerated | ✓ |
| 5 | Re-cohort `test_medical_and_restaurant_templates_have_booking_flag` | Add Continua to booking_slugs · explanatory comment · verify 546/546 | `continua-stewardship` added · comment expanded with Wave-2 stewardship cohort note + explicit Cornice-NOT-included note · `python manage.py test` → 546/546 · OK | ✓ |
| 6 | 45-route smoke (5 siblings × 5 locales · catalog · category · live preview · AR) | Anonymous probes · all 200 | curl probes · **45/45 · 0 failures** | ✓ |
| 7 | 5-sibling 1920px regression capture | Playwright at viewport 1920×1080 · one capture per live sibling | 5 PNG captures · all match declared L1–L9 tuple per visual sanity vs `corporate-suite-live-family-map.md §2` · zero wireframe drift | ✓ |
| 8 | AR Naskh/Kufi selector-scope re-probe | Cornice AR = Naskh · Continua AR = Kufi · zero leakage | computed-style probes via `browser_evaluate` · Cornice = `Noto Naskh Arabic` (LF-2-scoped) · Continua = `Noto Kufi Arabic` (cluster default · NOT overridden) | ✓ |
| 9 | Server | Keep running · report URL/port | `python manage.py runserver 127.0.0.1:8052 --noreload` · background process · still up at **`http://127.0.0.1:8052/`** | ✓ (left up) |

---

## 3 · Layer-1 / Layer-2 / Layer-3 (NOT re-issued · governance pass)

The corporate-suite quality scorecard (Layer-1 BLOCKING / Layer-2 critical-dimensions / Layer-3 aggregate) is not re-issued for this pass because:

1. **No visual product changed.** The 5 live siblings' rendered output is byte-equivalent to the post-Cornice public-flip baseline (zero source changes to any rendered surface).
2. **No new scoring is meaningful.** Re-running scorecard would produce the same aggregate (4.97/5 from Cornice public flip) for Cornice and the corresponding aggregates for each other sibling — none of those aggregates would shift because nothing rendered differently.
3. **The pass's verification is regression**, not fresh quality scoring (per `browser-verifier.md §5`).

The Layer-1 / Layer-2 / Layer-3 verdicts inherited verbatim from each sibling's most recent public-flip release-gatekeeper:
- Pragma · 4.85/5 (last full re-walk · stable since X.4a Step 1D)
- Cornice · 4.97/5 (post-Cornice public-flip 2026-05-01)
- Fiscus · 4.83/5 (last full re-walk · stable since X.4a Step 1D)
- Solaria · 4.91/5 (post-Solaria Pass C · 2026-04-27)
- Continua · 4.95/5 (post-Continua public-flip 2026-04-30)

---

## 4 · Risk register at this pass's landing

| Risk | Status | Action this pass took |
|---|---|---|
| R1 (post-cornice-state §5) · Stale reference layer (3-col vs 5 live siblings) | **CLOSED** by P1 | Three reference files refreshed to 5 columns |
| R2 · Pragma↔Fiscus 2/9 layout collision unresolved | **CLOSED** by P2 (Option C) | § decision filed · CS-LAYOUT-12 reworded · single-exception ladder named |
| R3 · Booking-flag failure noise floor | **CLOSED** by P3 | Test re-cohorted · suite reads 546/546 |
| R4 · No `layout_family` gate on `WebTemplate` write paths | UNCHANGED · queued | Out of scope · planner-trust today |
| R5 · LF-2 cream nav + LF-2 cream CTA closer set a precedent | UNCHANGED · explicitly bound | Reference pack §3 R10 documents LF-2 demotion as family-scoped · NOT a portable precedent |
| R6 · Imagery URL pool collision risk grows non-linearly | UNCHANGED · queued | Out of scope · automated CS-IMG-SRC-04 grep stays effective |
| R7 · `?preview=1` legacy flag still propagated | UNCHANGED · queued | Out of scope · benign no-op pass-through |
| R8 · No documented retirement protocol | UNCHANGED · queued | Out of scope · no sibling needs retirement |

**R1 + R2 + R3 are the three the user asked us to resolve before opening the 6th sibling.** All three are CLOSED. R4–R8 ride the next sibling's normal workflow per the post-cornice-next-candidate-readiness.md §5 explicit out-of-scope list.

---

## 5 · BLOCKING overrides (none invoked)

This pass invoked **zero BLOCKING overrides**. No L1 dimension was overridden; no L2 critical dimension was waived; no `factory/standards/corporate-suite-blocking-rules.md` rule was bypassed. The Pragma↔Fiscus 2/9 § decision is filed as a documented exception under the newly-reworded CS-LAYOUT-12 (single-exception ladder), NOT as an override.

---

## 6 · Outcome

GREEN. **6th-sibling intake may now open.**

The orchestrator's reference layer reads the live state. The Pragma↔Fiscus near-occupant pair is named, ratified, and bounded. The 8-pass-old test cohort noise floor is closed. The dev server is up at `http://127.0.0.1:8052/` for user-side verification.

The recommended 6th-sibling profile (orchestrator's view, not binding) is an evidence-led litigation firm at LF-2 second occupant — the planner reads `cornice-lf2-reference-pack.md §4` (anti-collapse rules) + §9 (intake questions) first, then files an intake brief. Alternative profiles (LF-6 first occupant for an audit-led methodology / conservation studio · LF-{NEW} for a candidate fitting none) remain available.

**The decision to open the intake is the user's**, not this pass's. The pass produces the evidence; the orchestrator opens the gate on the user's next authorization.
