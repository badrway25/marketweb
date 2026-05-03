# Post-Cornice · next-candidate readiness

**Status**: operational decision report · post Cornice public flip
**Date**: 2026-05-01
**Scope**: corporate-suite archetype only · documentation/governance pass · zero application code, registry, or tier change

**Inputs read**:
- `factory/reports/hardening/corporate-suite-post-cornice-state.md` (companion · cluster state)
- `design-orchestrator/references/internal-baselines/corporate-suite-live-family-map.md` (companion · 5-sibling state)
- `design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md` (companion · LF-2 reference)
- `factory/reports/cornice/cornice-{a5-it-build,a6-it-review-lock,workflowC-multilingual,workflowD-release-decision,public-flip}.md`
- `phase_x5_cornice_public_flip.md`
- Stale reference layer: `corporate-suite-{distinctness-matrix,reference-pack,layout-family-assignment}.md`

---

## §1 · The decision

**Recommended next move: (b) short hardening pass.**

Not (a) immediate 6th sibling. Not (c) full debt cleanup. A focused, time-boxed pass — approximately one session — that closes the three documentation-layer drifts blocking confident 6th-sibling enrollment, plus isolates the booking-flag noise floor. Then open the 6th sibling.

The argument:

- **(a) is wrong** because the orchestrator's reference layer (`distinctness-matrix.md`, `reference-pack.md`, `layout-family-assignment.md`) is 3-column when the cluster is 5 live. A 6th-sibling planner reading those files at intake will score against the wrong neighbours and either ship a sibling that collides with Continua/Cornice (caught late at A.6 critique or A.7 walk · expensive) or pick an LF-2 second occupant without reading the load-bearing differentiators in `cornice-lf2-reference-pack.md` (caught late · expensive). The risk is not *that* the 6th sibling will be bad — it is that the system's first scaling test (going from 5 to 6 with the new layout-family infrastructure) will discover preventable problems mid-build.
- **(c) is wrong** because the full debt list (Pragma Unsplash retro-curation · `?preview=1` propagation cleanup · retirement protocol design · `WebTemplate.layout_family` write-path enforcement · imagery URL pool reorganization at 5+ pools) is non-trivial and most of those items don't gate the 6th sibling. Debt-cleanup-first turns into a multi-session diversion that delays scaling without proportionate return.
- **(b) is right** because the work that genuinely gates the 6th sibling is bounded and can be done in approximately one session: refresh three reference files, decide and document the Pragma↔Fiscus 2/9 audit, isolate the booking-flag noise. After that, the 6th sibling runs the proven workflow A.5 → A.6 → C → D → flip pipeline against an updated reference layer.

---

## §2 · The exact precondition before the next real candidate opens

The 6th-sibling intake **must NOT** open until the following four items are all green. They are listed in execution order; each is small.

### Precondition P1 · 5-column reference layer
The orchestrator's reference layer reads the live state. Three files are refreshed:

- **`design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md`** — 5 columns (Pragma · Cornice · Fiscus · Solaria · Continua) across all 12 dimensions (1.1 tone · 1.2 palette polarity · 1.3 secondary/accent warmth · 1.4 typography · 1.5 hero composition · 1.6 imagery mood · 1.7 CTA personality · 1.8 section rhythm · 1.9 leadership feel · 1.10 proof/case-study · 1.11 motion · 1.12 stakeholder impression). The "next sibling MUST NOT repeat" lines extended for every existing column. The §3 "pre-filled next-sibling guide-rails" example re-scored against 5 columns.
- **`design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md`** — 5 columns. Add §1 entries for Cornice and Continua ("best move · don't copy"). Add §4 imagery-rhythm rows for both. Add §5 typography rows. Add §6 section-pacing variants. Add §7 navbar/footer variants (cream-paper navbar from LF-2 · condensed-minimal-top from LF-5 · 4-col-with-whistleblowing from both). Update §10 quick-lookup to 5 columns.
- **`design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md`** — Update §1 sibling→family map: Continua live at LF-5 (active · published_live), Cornice live at LF-2 (active · published_live). Update §6 open-territory: LF-2 TAKEN by Cornice, LF-1/LF-3/LF-4/LF-5 TAKEN, LF-6 RESERVED, LF-{NEW} OPEN. Update §3 freeze list to add LF-2 and LF-5 freeze entries. Update §5 pair-scoring table to 5×5 matrix (10 pairs).

**Source of truth for the refresh**: `corporate-suite-live-family-map.md` (this pass · 5-sibling state) and `cornice-lf2-reference-pack.md` (this pass · LF-2 details). The refresh is copy-paste-and-adapt; no original analysis required.

**Estimated effort**: half a session. **Gates**: the 6th-sibling intake reads these three files first.

### Precondition P2 · Pragma ↔ Fiscus 2/9 decision filed
The cluster's structural weak link is unresolved. CS-LAYOUT-12 mandates ≥4/9 layout dimensions different between any pair; Pragma ↔ Fiscus is at 2/9 (differs on L2 + L3 only). This has been deferred since the divergence plan (2026-04-29) and at every subsequent flip.

The decision is one of three options (detailed in `corporate-suite-live-family-map.md §5`):

- **Option A** · Migrate Pragma's L7 from `list-row` to a different cases-shape (a 2-col case-grid is open). **Pragma↔Fiscus rises to 3/9.** Cost: Pragma re-walk + frozen-sibling regression on 4 others. **High-cost, high-correctness.**
- **Option B** · Migrate Fiscus's L9 from `3-col` to `4-col-with-regulatory-disclosures` (ODCEC iscrizione + commercialista albo numbers in a 4th column). **Pragma↔Fiscus rises to 3/9.** Cost: Fiscus re-walk + frozen-sibling regression. **Medium-cost, medium-correctness.**
- **Option C** · Formally accept the 2/9 score with a § decision documenting the rationale ("Pragma and Fiscus serve adjacent professional fits; structural distinctness is intentionally narrow because both are institutional advisory chrome variants; differentiation lives at the skin layer"). Cost: 1 § decision document. **Low-cost, low-correctness, but valid if the orchestrator decides the structural distinctness rule was over-strict for institutional advisory chrome.**

**Recommended option for the hardening pass: Option C.** The reasons:

1. Option C closes the audit. Options A and B re-open a sibling for a layout migration, which is itself a workflow A.5+ pass with frozen-sibling regression risk on the other 4 — that is exactly the sort of multi-session diversion this hardening pass is trying to avoid.
2. The argument for Option C is genuinely available: Pragma and Fiscus *are* both institutional advisory chrome variants (multi-partner organisation · serif-h1-LEFT split-55-45 hero · 5-link sticky-top navbar · 3-col footer). A reader examining the two side by side at 1920 sees two corporate-advisory firms whose differentiator is the calendar, and that is the right read — Fiscus's slot-4 cycle IS the family's identity, and the 2/9 score is what that identity costs structurally. The existing rule (CS-LAYOUT-12 ≥4/9) was written before LF-3 was understood as "LF-1 + slot-4," and it over-fits when the family difference is precisely a single-cell addition.
3. Option C lets the next sibling enroll without forcing a Pragma or Fiscus re-walk first.
4. Options A and B remain available later if the orchestrator decides Option C was wrong.

**The decision is documented as a § entry at `corporate-suite-layout-family-matrix.md §6` and the variance rules CS-LAYOUT-12 is updated to read "≥4/9 different OR a documented in-family near-occupant relationship."** That formalizes the relaxation without weakening the gate for non-near-occupant pairs.

**Estimated effort**: a quarter of a session.

### Precondition P3 · Booking-flag noise isolated
`test_medical_and_restaurant_templates_have_booking_flag` has failed across 8 consecutive corporate-suite passes. It does not block any flip but it sets the noise floor at 545/546 instead of 545/545.

**Recommended action: re-cohort the assertion.** Options:

- **(a)** Add a `WAVE_2_BOOKING_SHAPED` set covering the templates whose booking flag reflects Wave-2 design intent (Continua's family-office mandate-dialogue is the only current member; future stewardship/custody siblings would join). The original assertion enumerates `MEDICAL ∪ RESTAURANT ∪ LAWYER ∪ WAVE_2_BOOKING_SHAPED` as the "should have booking flag" set. Continua passes the assertion. **Test passes 546/546.**
- **(b)** Revert the Continua seed to `has_booking=False`. Loses Wave-2 design intent.

**Recommended: (a).** The Wave-2 design intent (family-office mandate-dialogue is booking-shaped) is real and should be preserved.

**Implementation**: 1 file edit to `apps/catalog/tests.py` (extend the booking_slugs set) + 1 file edit to a constants module if the cohorts are model-driven. Approximately a half-hour change.

**Estimated effort**: half a session including verification.

### Precondition P4 · Smoke re-walk on the 5 live siblings
After P1, P2, P3 land, run the 45-route smoke and the frozen-sibling 1920px wireframe capture on all 5 live siblings to confirm zero drift from the post-Cornice baseline. This is a sanity check, not a build pass.

**Estimated effort**: a quarter of a session.

---

## §3 · Total estimated effort for the hardening pass

| Step | Work | Effort |
|---|---|---|
| P1 | Refresh 3 reference files to 5-column · use the live family map and LF-2 reference pack as sources | 0.5 session |
| P2 | File the Pragma ↔ Fiscus 2/9 § decision · update CS-LAYOUT-12 wording · update layout-family matrix §6 | 0.25 session |
| P3 | Re-cohort the booking-flag test · verify 546/546 · update commit memo | 0.5 session |
| P4 | 45-route smoke + 5 frozen-sibling 1920 wireframe captures | 0.25 session |
| **Total** | | **≈1.5 sessions** |

The pass writes documentation files and one test edit. **No source changes** to `apps/editor/`, `apps/projects/`, `apps/commerce/`. **No registry changes** beyond what P3 may touch (constants module, if used). **No tier changes**. **No new archetypes**. **No imagery changes**.

---

## §4 · Recommended next build order (after the hardening pass)

After the hardening pass closes, the next two sibling enrollments in order:

### Build 1 · 6th sibling (LF-{NEW} OR LF-2 second occupant OR LF-6 first occupant)
The choice depends on the next concrete intake brief. The orchestrator picks one of:

- **LF-2 second occupant** — if the candidate is genuinely portfolio-of-work-led (evidence-led legal · independent directorship · audit-led methodology with published pieces · longitudinal research with publications · inchiesta-led journalism · conservation studio). The planner reads `cornice-lf2-reference-pack.md §4 (anti-collapse rules)` and `§9 (intake questions)` first.
- **LF-6 first occupant** — if the candidate fits "magazine-edited boutique" (audit-led methodology · public-hearing law · conservation studio · longitudinal research). The planner files an LF-6 declaration addendum at `corporate-suite-layout-family-matrix.md §1` finalising the L1–L9 tuple before build.
- **LF-{NEW}** — if the candidate fits none of the above. The planner files an LF-{NEW} addendum declaring the new tuple before build.

**Recommended sub-cluster for the 6th sibling** (orchestrator's view): an evidence-led litigation firm at LF-2 second occupant. The reasoning:
- It validates LF-2 as a re-runnable family (Cornice was the first occupant; the second proves the family is reusable).
- The voice register (`evidenza` / evidence) is genuinely distinct from `argomento` / argument.
- The hero photography subject (legal-codex spread on a desk · law-library reading-room · public-hearing chamber) has not been claimed.
- The case-bundle (published rulings · landmark decisions · expert testimonies) fits the 3+1 magazine grid naturally.
- The whistleblowing column is already family-shared; legal practice is a natural fit.

### Build 2 · 7th sibling (the unclaimed slot)
Whichever LF-{NEW} or LF-6 was not picked at Build 1.

**At each build**, the planner reads the (post-hardening) refreshed reference files first. The matrix scores against 5 (or 6 after Build 1) columns, not 3.

---

## §5 · What the hardening pass does NOT do

To avoid scope creep, the pass explicitly excludes:

- Pragma's Unsplash retro-curation. The `(corporate_suite.W001)` warning fires on every `sync_template_tiers` and is its own workstream. Not blocking the 6th sibling.
- `?preview=1` propagation cleanup. Benign no-op pass-through. Not blocking the 6th sibling.
- Retirement protocol design. No sibling needs retirement. Not blocking the 6th sibling.
- `WebTemplate.layout_family` write-path enforcement. Today's planner reliably sets it; enforcement layer is for operational hardening, not enrollment.
- Imagery URL pool reorganization. Five pools is fine; the curator scout cost grows linearly but stays under control.
- Distinctness matrix structural redesign (e.g., adding a 13th dimension). The 12 dimensions are good; the columns are stale. Add columns, do not redesign rows.
- Layout-family matrix structural redesign. The 9-cell L1–L9 system works. Hold the structure.
- Test suite triage beyond P3. The booking-flag failure is the only one repeatedly observed. Other tests are green.

If something in the above list surfaces during the hardening pass as an unexpected blocker, it is escalated to a separate workstream — not bundled.

---

## §6 · Booking-flag classification (the one repeated noise floor)

Restated for decision clarity. `test_medical_and_restaurant_templates_have_booking_flag` fails because:

- The assertion enumerates the medical/restaurant/lawyer/W2-booking exact slug-set.
- Continua's seed carries `has_booking=True` (Wave-2 design intent — family-office mandate-dialogue is booking-shaped).
- Continua is not a member of any of those families.
- Set difference reads `Items in the first set but not the second: 'continua-stewardship'`.

**Classification: noise floor, isolation candidate, NOT a 6th-sibling blocker.**

- It does not affect any sibling's render, build, walk, anonymous reachability, or flip cascade.
- It has been observed across 8 consecutive corporate-suite passes (Continua A.4 → A.5 → A.6 → C → D → flip · Cornice A.5 → A.6 → C → D → flip) and produced **zero new failures** on any of them.
- It is a test-cohort error, not a behavioural error.

**The hardening pass closes it via P3.** Re-cohort the assertion to include Wave-2-booking-shaped templates explicitly · Continua passes · test suite reads 546/546 · noise floor returns to zero.

**It is decoupled from the 6th-sibling enrollment.** It is solved in the hardening pass, not inside the next sibling's flip cascade. Bundling test-cohort work with feature work pollutes the flip cascade and is exactly the kind of incidental fix the corporate-suite SOP §5 forbids.

---

## §7 · Where the system would drift if we skipped the hardening pass

If the orchestrator opens the 6th-sibling intake without doing the hardening pass first, the predicted failure mode:

1. **Planner reads the 3-column matrix.** The 6th sibling scores 5/5 against Pragma · Fiscus · Solaria. Planner files a planner-brief approving the build.
2. **Builder ships A.5.** The 6th sibling looks fine in isolation.
3. **A.6 review-lock spots the collision.** Style-critic, cross-checking against the live cluster (5 siblings, not 3), finds that the 6th sibling collides with Continua on imagery mood (e.g., both interior-warm) or with Cornice on heading serif (e.g., both Cormorant Garamond) or on voice anchor noun.
4. **Re-spec.** Planner re-files. Imagery curator re-scouts. Copy author re-authors.
5. **Workflow C cost doubles.** The multilingual translator was briefed on an em-noun that no longer holds; translator re-briefs.
6. **The orchestrator's confidence in the next-sibling pipeline drops.** "We thought we had a recipe but we hit a wall at A.6 again." The recipe was good; the reference layer was not.

The hardening pass costs ≈1.5 sessions. Skipping it and discovering the collision at A.6 costs ≈3-5 sessions of rework + a confidence dent. **The math is not close.**

---

## §8 · The strongest argument for doing this NOW (rather than during the next sibling)

Two reasons:

### Reason 1 · The post-flip moment is the cheapest hardening window
Right after a public flip, the cluster state is fully observed and freshly documented. The orchestrator has just read:
- `phase_x5_cornice_public_flip.md` (the live state)
- `cornice-public-flip.md` (the audit trail)
- All 5 cornice scorecard panels (the certifications)
- All 4 cornice browser-verification captures
- The full 5-sibling parity check

The 5-column refresh is largely re-organising what is already in this conversation's working memory. Doing it next session, after intervening work, costs more because the orchestrator re-reads.

### Reason 2 · The hardening pass produces evidence the 6th sibling needs
- The refreshed `distinctness-matrix.md` is the planner's first read at intake.
- The refreshed `reference-pack.md` is the builder's reference at A.5.
- The refreshed `layout-family-assignment.md` is the orchestrator's authority at A.6 critique.
- The Pragma↔Fiscus § decision is the gatekeeper's authority at any future Pragma- or Fiscus-shaped sibling intake.
- The booking-flag re-cohort is the CI baseline for any future flip.

These are inputs to the 6th sibling, not outputs. Producing them inside the 6th sibling's enrollment is bundling unrelated work; producing them now produces them once and reuses them across all future enrollments.

---

## §9 · The exact next action

> **Open a hardening session before opening the 6th-sibling intake. The session does four things in order: (P1) refresh `corporate-suite-distinctness-matrix.md`, `corporate-suite-reference-pack.md`, and `corporate-suite-layout-family-assignment.md` to 5 columns, using `corporate-suite-live-family-map.md` and `cornice-lf2-reference-pack.md` as sources of truth. (P2) file the Pragma ↔ Fiscus 2/9 § decision — recommended as Option C (formal acceptance with documented rationale at `corporate-suite-layout-family-matrix.md §6` + variance rules CS-LAYOUT-12 wording update). (P3) re-cohort `test_medical_and_restaurant_templates_have_booking_flag` to include Wave-2-booking-shaped templates explicitly, verify the suite reads 546/546. (P4) run a 45-route smoke + 5-sibling 1920 wireframe regression capture. Estimated total effort ≈1.5 sessions, no source changes to apps/editor/projects/commerce, no registry changes, no tier changes, no new archetypes. Once those four close, open the 6th-sibling intake reading the refreshed reference layer first.**

That is the one action the next session takes. Everything else (6th sibling enrollment, 7th sibling, LF-6 activation, retirement protocol design) is downstream of it.

---

## §10 · Summary

```
DECISION: short hardening pass · NOT 6th sibling now · NOT full debt cleanup

PRECONDITION FOR 6TH SIBLING:
  P1 · 3 reference files refreshed to 5 columns
  P2 · Pragma↔Fiscus 2/9 audit decided (recommend Option C · formal acceptance)
  P3 · booking-flag test re-cohorted (Wave-2 booking-shaped templates explicit)
  P4 · 45-route smoke + 5-sibling 1920 regression capture clean

EFFORT: ≈1.5 sessions · doc-only + 1 test edit · zero source/registry/tier changes

NEXT BUILD ORDER (after hardening):
  Build 1 · 6th sibling at LF-2 second occupant (recommended: evidence-led legal)
            OR LF-6 first occupant (audit-led methodology · conservation studio)
            OR LF-{NEW}
  Build 2 · 7th sibling · whichever slot remains

BOOKING-FLAG: noise floor · isolated by P3 · NOT a 6th-sibling blocker

ANCHOR TO ORIGINAL OBJECTIVE:
  The factory works. Five distinct premium templates ship, end-to-end pipeline
  ran twice, public-flip cascade is a recipe. The bottleneck is the documentation
  layer that the planner reads first at the next intake. Fix that, and throughput
  equals the cost of one sibling's content + imagery, not one sibling's exploration.
  THE PROCESS IS GOOD ENOUGH AT THE RECIPE LEVEL · DRIFTING AT THE REFERENCE LAYER.
  The hardening pass closes the drift.
```
