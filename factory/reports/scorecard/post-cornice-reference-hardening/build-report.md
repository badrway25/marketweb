# Build-report · post-Cornice reference hardening · 2026-05-03

**Verdict**: GREEN · documentation hardening pass complete · 6 files edited (5 docs + 1 test) · 0 source code changes
**Branch**: `phase-x5-post-cornice-reference-hardening`
**Predecessor**: post-Cornice public flip (`phase_x5_cornice_public_flip.md` · 2026-05-01)
**Scope**: P1 (5-col reference refresh) · P2 (Pragma↔Fiscus § decision) · P3 (booking-flag re-cohort) · P4 (smoke + 1920px regression) — full post-Cornice next-candidate-readiness checklist.

---

## 1 · What was built

Not a feature build. This is a **governance hardening pass** that closes the documentation-layer drift identified by `factory/reports/hardening/corporate-suite-post-cornice-state.md` and recommended in `factory/reports/hardening/post-cornice-next-candidate-readiness.md`. The "build" here is a coherent set of edits to existing reference / standards / test files.

### Files edited (8 total · 5 documentation refreshes + 1 test fix + 2 factory-side companion edits)

| # | File | Phase | Type | Δ |
|---|---|---|---|---|
| 1 | `design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md` | P1 | Full rewrite (3-col → 5-col) | +12 dimensions × 2 added columns + § decision summary at §4 + extended MUST-NOT-repeat lines |
| 2 | `design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md` | P1 | Full rewrite (3-col → 5-col) | +Cornice + Continua "best move · don't copy" entries + family-scope flags on §2 patterns + 5-pack imagery rhythm + 5-row typography + 5-variant section pacing + 5-variant chrome + 5-col §10 quick-lookup + §11 paragraph |
| 3 | `design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md` | P1 | Full rewrite (pre-Cornice → post-Cornice) | +Cornice LF-2 active row + Continua LF-5 active row · superseded LF-3 row preserved · 5-row §1 + 5×5 §5 pair scoring · §6 LF-1..LF-5 TAKEN · §8 6th-sibling intake precondition checklist |
| 4 | `factory/reports/hardening/corporate-suite-layout-family-matrix.md` | P1 + P2 | Surgical edits | §2 occupancy: Continua LF-5 + Cornice LF-2 active rows added · superseded annotated · §2 pair scoring rebuilt as live 10-pair table · §3 open territory updated · §4 forbidden tuples added LF-2 + L1+L2+L7 sub-tuple extended · **§6 Pragma↔Fiscus § decision appended (Option C)** |
| 5 | `factory/reports/hardening/corporate-suite-layout-variance-rules.md` | P2 | CS-LAYOUT-12 wording update | Rule reworded · in-family near-occupant exception clause + single-exception ladder + currently-filed annotation |
| 6 | `apps/catalog/tests.py:656-688` | P3 | 1 slug add + comment expand | `continua-stewardship` added to `booking_slugs` set · explanatory comment expanded to classify Wave-2 stewardship cohort + explicit Cornice-NOT-included note |
| 7 | `factory/reports/hardening/post-cornice-reference-hardening.md` | P1+P2+P3+P4 (this pass) | New file | Full hardening report (this pass's outputs) |
| 8 | `factory/reports/browser-verification/post-cornice-reference-hardening.md` | P4 | New file | Smoke + 1920px capture report + AR Naskh/Kufi isolation re-probe |

Plus 5 PNG captures under `factory/reports/browser-verification/post-cornice-reference-hardening/captures/`.

### Files explicitly NOT touched
- `apps/editor/` · `apps/projects/` · `apps/commerce/` (per task constraint).
- `_layouts/{lf1..lf5}/home.html` · any chrome partial · `_base.html`.
- `TEMPLATE_REGISTRY.json` · any seed file (`apps/catalog/management/commands/seed_templates.py`) · any migration · any per-sibling `template_content_*.py` module.
- `MEMORY.md` (the orchestrator's auto-memory · governance pass does not warrant a checkpoint pointer at this time; the user can request one).

---

## 2 · Why these edits, and not others

### Why P1 was a full rewrite of the 3 orchestrator files (not surgical edits)
The 3-column structure was load-bearing across 12 dimensions × 5 sections of each file. A surgical "add 2 columns to existing rows" approach would have left dozens of MUST-NOT-repeat lines, prose paragraphs, and quick-lookup tables internally inconsistent. A full rewrite is cheaper and produces a coherent v2 in one pass. The source-of-truth for the rewrite is `corporate-suite-live-family-map.md` + `cornice-lf2-reference-pack.md` + per-sibling planner-briefs — no original analysis required, just operational synthesis.

### Why P2 was a § decision filed in 4 places (not 1)
The § decision is the kind of governance fact that must surface at every gate the next intake reads. Filing it once (e.g., only in the variance-rules CS-LAYOUT-12 wording) would mean a planner reading the orchestrator-side distinctness matrix or layout-family assignment would see the rule applied without seeing the exception named — the appearance of a silent waiver, which is exactly what the task forbids. Filing it in 4 cross-referenced places (factory matrix §6 + variance rules §2 + orchestrator distinctness matrix §4 + orchestrator family assignment §5) ensures every reader at every gate sees the same § decision with the same rationale.

### Why P3 was a re-cohort, not a seed revert
The seed (`apps/catalog/management/commands/seed_templates.py:443`) sets Continua's `has_booking=True` because Wave-2 design intent considered the family-office mandate-dialogue structurally booking-shaped (custody-onboard form). Reverting the seed would erase a deliberate design decision made at Continua's enrollment. Re-cohorting the test (adding `continua-stewardship` to the assertion's enumerated set) preserves the design intent and corrects the wrong piece (the test cohort enumeration was incomplete · the seed and design intent were always correct). The fix is the smallest correct intervention.

### Why P4 was Playwright captures + curl smoke (not full A.7 walk)
The hardening pass introduced no source changes to any rendered surface. A full A.7 walk would re-run the responsive matrix, internal-link reachability, contrast accessibility, and per-sibling scorecard — all of which already passed at the Cornice public-flip walk and would pass identically here (because nothing changed). Playwright captures + 45-route smoke + AR Naskh/Kufi probe are sufficient to confirm zero regression — and they did.

---

## 3 · Pre-existing risks acknowledged (carried forward · not addressed by this pass)

Per the post-cornice-state.md §4 weak list and the post-cornice-next-candidate-readiness.md §5 explicit out-of-scope list:

- **Pragma Unsplash retro-curation** (W001 grandfather warning · still fires on every `sync_template_tiers`).
- **`?preview=1` propagation cleanup** (benign no-op pass-through · chrome still propagates the flag).
- **Retirement protocol design** (no sibling needs retirement).
- **`WebTemplate.layout_family` write-path enforcement** (planner-trust today).
- **Imagery URL pool reorganization at 5+ pools** (curator scout time grows linearly).

None of these block the 6th sibling. They are queued for separate workstreams.

---

## 4 · Server status

- Command: `python manage.py runserver 127.0.0.1:8052 --noreload`
- URL/port: **`http://127.0.0.1:8052/`** · port **8052**
- Status: background process ID `bwxn80945` · still running · left up per task constraint for user-side post-hardening verification.

---

## 5 · Build-time check

`sync_template_tiers` reports `0 tier(s) updated. Catalog distribution: 24 published_live / 0 draft.` after the pass — confirming no tier flip introduced. The standing `(corporate_suite.W001) corporate-suite imagery pool 'business-corporate' is grandfathered…` warning is preserved (Pragma Unsplash legacy · documented in §3 above as out of scope).

---

## 6 · Outcome

GREEN. P1 + P2 + P3 + P4 closed. The 6th-sibling intake's precondition checklist (per `post-cornice-next-candidate-readiness.md §10`) is fully satisfied. The pass introduced **zero source changes** to any rendered surface — only documentation refresh + 1 test cohort fix.
