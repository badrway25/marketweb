# Corporate-suite · post-Cornice cluster state

**Status**: operational state report · post-flip consolidation
**Date**: 2026-05-01
**Scope**: corporate-suite archetype only · documentation/governance pass · zero application code, registry, or tier change

**Inputs read**:
- Cornice pipeline reports: `factory/reports/cornice/cornice-{a5-it-build,a6-it-review-lock,workflowC-multilingual,workflowD-release-decision,public-flip}.md`
- Memory checkpoint: `phase_x5_cornice_public_flip.md`
- Family governance: `factory/reports/hardening/corporate-suite-layout-{divergence-plan,variance-rules,family-matrix,family-backfill}.md`
- Orchestrator references: `design-orchestrator/references/internal-baselines/corporate-suite-{distinctness-matrix,reference-pack,layout-family-assignment}.md` · `continua-lf5-migration-brief.md`
- Live state: `TEMPLATE_REGISTRY.json` · `MEMORY.md`

**Companions** (written in the same pass):
- `design-orchestrator/references/internal-baselines/corporate-suite-live-family-map.md`
- `design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md`
- `factory/reports/hardening/post-cornice-next-candidate-readiness.md`

---

## §1 · The actual cluster state right now

Five corporate-suite siblings live at `tier=published_live`, in 5 distinct layout families, in 5 locales each (IT/EN/FR/ES/AR + AR RTL).

| # | Sibling | Slug | Family | Sub-cluster | First-30-second read |
|---|---|---|---|---|---|
| 1 | **Pragma** | `pragma-corporate-suite` | **LF-1 · Boardroom Vertical** | corporate advisory · multi-partner | "an established advisory boutique · we're being interviewed for a board mandate" |
| 2 | **Cornice** | `cornice-architettura` | **LF-2 · Editorial Spread** | architecture studio · single-principal editorial-led | "a studio that builds arguments, not buildings as services" |
| 3 | **Fiscus** | `fiscus-commercialista` | **LF-3 · Compliance Calendar** | commercialista presidio · revisione legale | "a serious tax studio · we'd entrust our books to them" |
| 4 | **Solaria** | `solaria-coaching` | **LF-4 · Manifesto-First** | executive coaching · single-coach method-declared | "a calm, methodical coach · we'd refer a colleague to them" |
| 5 | **Continua** | `continua-stewardship` | **LF-5 · Stewardship Object-Hero** | stewardship · family-office · custodial | "a stewardship-grade firm · we'd entrust generational continuity to them" |

Catalog distribution: **24 published_live / 0 draft** (5 corporate-suite + 19 other archetypes from the closed A.6→A.17b enrollment program). Tests: **545/546** (the same pre-existing booking-flag failure documented since the Continua passes; classified in §6 below). Anonymous 45-route smoke per sibling: **45/45 200**. Frozen-sibling regression after each flip: **0/4 drift**.

Five LF slots populated. **LF-6** (Rail-Side Chrome) reserved for 6th–7th. **LF-{NEW}** open for any candidate that does not fit LF-1..LF-6.

---

## §2 · What is now solved vs the original problem

The original problem documented at the layout-divergence plan §1–§2 was: "four corporate-suite siblings all pass the 5-axis distinctness matrix at 4–5/5 yet still read as four palette skins of one master template." Wireframes overlaid at >90% identical bounding boxes. Differentiation lived **inside** cells (copy in `<div class="meta-strip">`, label in `<section class="cs-cycle">`) but the DOM shell was singular.

That problem is structurally solved. Concretely:

| Original sameness vector (S1–S12 of the divergence plan) | State now |
|---|---|
| **S1** · One shared `home.html` with hardcoded section order | **CLOSED**. Five distinct `_layouts/{lf1,lf2,lf3,lf4,lf5}/home.html` files, dispatched by registry `layout_family`. Each sibling renders a different section sequence (A, B, A+slot4, C, D). |
| **S2** · 55/45 hero split as cluster invariant | **PARTIALLY CLOSED**. Three siblings still ship 55/45 (LF-1/LF-3/LF-4 — that is the family choice, not a constraint), but LF-2 ships `stacked-editorial` and LF-5 ships `object-overlay`. The hero is no longer monomorphic. |
| **S3** · Hero meta-strip as horizontal `(label, value)` tuple | **PARTIALLY CLOSED**. LF-1/LF-3/LF-4 still use it (each with a distinct composition); LF-2 promotes the KPI tuple **into the hero photo overlay** (no separate strip); LF-5 splits the credit into two top-corner overlays. The shape is no longer the only place differentiation can land. |
| **S4** · Pillars as 3–4 col `auto-fit` numbered grid | **CLOSED**. LF-1/LF-3 = numbered-grid · LF-4 = manifesto-replacement · LF-2 = essay-with-anchors · LF-5 = 2×2-with-image. Four pillar treatments shipped. |
| **S5** · Dark KPI band always at section position 3 | **CLOSED**. LF-1/LF-3 = band-at-3 · LF-4 = band-at-5 · LF-5 = band-at-4 · LF-2 = hero-overlay (no dark band on home). Four KPI placements shipped — one of them with zero dark bands on home, which validated the family-level demotion of CS-TONE-03. |
| **S6** · Sectors ribbon + trust marquee always together | **CLOSED**. LF-2 drops the trust marquee (sectors-ribbon absorbs the trust function) · LF-5 drops it too (the sectors band carries whistleblowing surface) · LF-4 drops trust into the sponsor-coverage list. The double-ribbon fingerprint no longer holds. |
| **S7** · Leadership block always rendered | **CLOSED**. LF-4 = `absent` (single-coach firm) · LF-2 = `single-portrait-feature` · LF-5 = `pillar-photo` (environmental portraits) · LF-1/LF-3 = `typographic-grid` (3 vs 4 cards). Four leadership treatments shipped. |
| **S8** · Cases preview always `list-row` with thumb | **CLOSED**. LF-1/LF-3/LF-4 = list-row · LF-5 = timeline · LF-2 = magazine-grid (3+1). Three case-preview shapes. |
| **S9** · CTA closer always a dark band | **PARTIALLY CLOSED**. LF-1/LF-3/LF-4/LF-5 ship a dark CTA band (cluster-invariant for those families); LF-2 ships a hairline-bordered **cream** CTA band. The cream-on-cream closer is now expressible. |
| **S10** · Sticky-top primary navbar with phone-right | **CLOSED**. LF-1/LF-3/LF-4 = sticky-top · LF-5 = condensed-minimal-top (64px · no phone-right) · LF-2 = split-wordmark-top with cream nav and filled-rust trailing CTA. Three nav geometries. |
| **S11** · 3-column footer | **CLOSED**. LF-1/LF-3/LF-4 = 3-col · LF-2 + LF-5 = 4-col-with-whistleblowing (D.lgs. 24/2023 promoted from legal-row to a column). Two footer structures. |
| **S12** · All siblings use the same `cs-*` class names | **STILL TRUE BY DESIGN**. The `cs-` prefix is the cluster's editorial-isolation contract (CS-COMP-07). Class names are shared; **DOM scaffold is no longer shared**, which is what mattered. |

Net effect: a 1920px wireframe overlay between any two of the five siblings now diverges by ≥30% bounding-box surface area (B-LAYOUT-1 gate). Pair-wise L1–L9 distinctness scoring (count of dimensions different):

| Pair | L1–L9 differences |
|---|---|
| Pragma (LF-1) vs Cornice (LF-2) | **9/9** |
| Pragma (LF-1) vs Fiscus (LF-3) | 2/9 (still a known weak pair — see §4) |
| Pragma (LF-1) vs Solaria (LF-4) | 5/9 |
| Pragma (LF-1) vs Continua (LF-5) | **9/9** |
| Cornice (LF-2) vs Fiscus (LF-3) | 9/9 |
| Cornice (LF-2) vs Solaria (LF-4) | 8/9 (L3=absent shared) |
| Cornice (LF-2) vs Continua (LF-5) | 8/9 (L9=4-col-with-whistleblowing shared, distinct content) |
| Fiscus (LF-3) vs Solaria (LF-4) | 5/9 |
| Fiscus (LF-3) vs Continua (LF-5) | 8/9 |
| Solaria (LF-4) vs Continua (LF-5) | 8/9 |

9 of 10 pairs ≥5/9. One pair (Pragma↔Fiscus 2/9) remains the cluster's structural weak link — surfaced by the divergence plan §10 Step 7 and explicitly deferred at every subsequent pass.

The original objective ("a scalable factory for many premium, modern, elegant, professional, clearly distinct templates") is no longer aspirational at the cluster level — five distinct templates ship. The remaining question is whether the **process** that produced them is repeatable at the 6th, 7th, 8th sibling.

---

## §3 · What the process actually proved twice

The Continua and Cornice public flips are the cluster's first two end-to-end runs of the full pipeline:

```
intake → planner-brief → A.5 IT-only build → A.6 review-lock → user-handshake →
workflow C multilingual (5 locales) → workflow D release-decision (HOLD on doubt) →
user-handshake → public flip cascade → live anon
```

Both runs landed under the same operational shape:
- **Tier flip cascade** is documented to the line in `release-gatekeeper.md §6` and re-applied verbatim per sibling. Continua: 7 literal swaps + sync. Cornice: 7 literal swaps + sync + 1 fallback re-binding (Pragma's category-fallback `limit=3 → 4` because Cornice is the 2nd addition to Pragma's classic-serif style pool).
- **Trust counter** (`templates_live`) inherits from a live DB filter at `apps/pages/views.py:94`; the rendered string moves from `23+` to `24+` with **zero source/template edits**.
- **Frozen-sibling regression** is run on every sibling on every flip — 0/4 drift in both cases.
- **Pre-existing booking-flag failure** survives unchanged; classified in §6 as orthogonal noise, not a flip blocker.
- **User-handshake gate** held both times (R-SOL-8 / SOP §5.4 / CS-BLOCK-13 / D-102 cadence). HOLD-on-doubt is now a ratified contract, not a one-off.

This is the part the cluster genuinely earned: the next sibling's public flip is a **recipe**, not a discovery.

---

## §4 · What is strong vs what is weak

### Strong (carries forward as proven contracts)

1. **Layout-family system as a first-class differentiation axis.** L1–L9 dimensions are not just declared — they are observed at walk-time (B-LAYOUT-1/2/3 gates) and the system has now demonstrated five distinct DOM scaffolds living side-by-side without skin-leakage.
2. **Selector-scoped chrome variation** (`body.cs-lf-lf-2`, `body.cs-lf-lf-5`). LF-2 introduced a Naskh AR h1 swap inside `body.cs-lf-lf-2`; the live walk **and** the post-flip Continua AR h1 probe both confirm zero leakage into LF-5. Family-scoped overrides are byte-equivalent on out-of-family siblings.
3. **Voice anchor verbatim across 5 locales.** Five anchors cleared the contract:
   - Pragma (decisional gravity) · Fiscus (presidio scadenze) · Solaria (terapia/consulenza contrast pair · 2 ems) · Continua (`generazioni → generations / générations / generaciones / الأجيال`) · Cornice (`argomento → argument / argumento / حُجَّة`).
   - The em-noun travels with the sense, not the cognate, in every locale. Translator briefs work.
4. **Multilingual rollout cadence.** Solaria → Continua → Cornice walked the same 1→5 locale extension on top of an IT-locked draft, with the AR Naskh-vs-Kufi decision now a per-LF concern (Kufi for LF-1/LF-3/LF-4/LF-5 cluster-default · Naskh for LF-2 editorial register). The process is reproducible.
5. **Public-flip cascade as a documented playbook.** Both flips applied the same 7-literal + sync-command + fallback-re-binding shape. The next flip can read `release-gatekeeper.md §6` and execute without re-discovery.
6. **0 px frozen-sibling regression discipline.** Continua's LF-5 rebuild + Cornice's LF-2 introduction both shipped with **0/4 wireframe drift on the rest of the cluster**. The layout-router refactor in `_layouts/{lf1..lf5}/home.html` has held under two real layout additions.
7. **No app-domain spillage.** Five sibling rollouts and not one of them touched `apps/editor`, `apps/projects`, `apps/commerce`. The archetype boundary is real.
8. **Editor program A.6 → A.17b closed (2026-04-20).** 19 archetypes enrolled on the editor side, 9/9 families closed, D-099 sentinel retirement binding, 375/375 + 834/834. The corporate-suite cluster is layered on top of a closed editor pipeline — no editor refactor pressure on the next corporate-suite sibling.

### Weak (real debt, named and bounded)

1. **Pragma ↔ Fiscus = 2/9 layout distinctness.** The cluster's structural blind spot. Pragma and Fiscus differ on L2 (`A` vs `A+slot4`) and L3 (`absent` vs `slot-4`) only. Their wireframes are near-identical at 1920px. The divergence plan §10 Step 7 deferred this audit; every subsequent pass deferred it again. **It is now overdue.**
2. **Distinctness matrix is 3-column.** `corporate-suite-distinctness-matrix.md` (2026-04-28) only enumerates Pragma · Fiscus · Solaria. Continua and Cornice are not in the table. Any planner using the matrix at 6th-sibling intake will score against the wrong 3 columns and pass siblings through the gate that should be re-spec'd. **Operationally stale.**
3. **Reference pack is 3-column.** `corporate-suite-reference-pack.md` (2026-04-28) is in the same state. "What each current template does best" lists Pragma + Fiscus + Solaria; Continua's stewardship moves and Cornice's editorial moves are absent. Same staleness, same blast radius.
4. **Layout-family assignment file lists Continua as "pending migration to LF-5".** `corporate-suite-layout-family-assignment.md` (2026-04-29) was written before the Continua LF-5 rebuild + the Cornice LF-2 enrollment. It says Continua is `Superseded — pending migration to LF-5` and "LF-2 is open for the 5th sibling." Reality: Continua is live at LF-5 and Cornice is live at LF-2. **The orchestrator's own reference layer disagrees with the live state.**
5. **Continua LF-5 multilingual brief was projected, then walked differently.** The migration brief (2026-04-29) projected an IT-only LF-5 rebuild followed by deferred multilingual. In practice, Continua walked through workflow C multilingual + workflow D public flip. The brief is now retrospective context, not a forward plan, but it is still filed as a live brief. **Doc-state mismatch.**
6. **Pre-existing booking-flag failure.** `test_medical_and_restaurant_templates_have_booking_flag` has failed across **every Continua and Cornice pass**. It does not block any pipeline (zero new regressions claim is intact each time) but the noise floor is wrong: 545/546 reads worse than 545/545 to anyone scanning CI. The assertion needs to be either re-cohorted (Continua added to a new "wave-2 booking-shaped" set) or the seed reverted. **Untouched at every flip on purpose.**
7. **`?preview=1` legacy flag is now a no-op pass-through.** Working as intended (corporate-suite-case-parent-fix closed the propagation work) but it is still surfacing in URL query strings throughout staff-session navigation. It is benign, but it is debt — the chrome should not propagate flags that have no effect.
8. **`business-corporate` Unsplash imagery pool grandfathered.** Pragma still ships on Unsplash (`(corporate_suite.W001)` warning fires on every `sync_template_tiers` run). CS-IMG-SRC-01 mandates Pexels-only. Pragma is the cluster's only retro-curation backlog item.

The "Strong" list is what the next sibling **inherits**. The "Weak" list is what the next sibling **either fixes first or discovers when its own walk hits the same gap**.

---

## §5 · Top systemic risks remaining

Ordered by how likely they are to bite a 6th-sibling planner if the orchestrator opens enrollment without a hardening pass first.

### R1 · Stale reference layer (3-column matrix vs 5 live siblings)
**Surfaces**: `corporate-suite-distinctness-matrix.md` · `corporate-suite-reference-pack.md` · `corporate-suite-layout-family-assignment.md`.
**Failure mode**: a 6th-sibling intake that scores against the 3-column matrix may pass at 4–5/5 vs Pragma/Fiscus/Solaria but collide at ≤3/5 against Continua or Cornice. The collision will only surface at A.6 critique or A.7 walk — late, expensive.
**Likelihood**: high. The matrix is the planner's first read at intake.
**Cost if hit**: 1 re-spec + 1 imagery scout pass + 1 copy re-author = approximately a workflow A.2 → A.5 redo.

### R2 · Pragma ↔ Fiscus 2/9 layout collision unresolved
**Surfaces**: `corporate-suite-layout-family-matrix.md §2` · `corporate-suite-layout-family-assignment.md §5` · divergence plan §10 Step 7.
**Failure mode**: the cluster's own scoring rule (CS-LAYOUT-12 ≥4/9 between any pair) is in violation. A new sibling that lands at 3/9 vs Pragma OR 3/9 vs Fiscus (using one of the open LF-2/LF-{NEW} territories) inherits the same weakness, and now the cluster has two 2/9 pairs instead of one. The gate keeps tightening on new siblings while the original weak pair never gets re-binned.
**Likelihood**: medium-high. LF-6 reserved (Rail-Side Chrome) is the only natural 6th-sibling slot if the planner picks an audit-led methodology firm. If the planner instead picks something LF-1-shaped, the matrix re-fires with 2/9 vs Pragma.
**Cost if hit**: a forced Pragma OR Fiscus L7/L9 migration mid-cluster with regression risk on two live siblings.

### R3 · Booking-flag failure noise floor
**Surfaces**: `apps/catalog/tests.py · test_medical_and_restaurant_templates_have_booking_flag` · Continua seed `has_booking=True`.
**Failure mode**: the failing test masks a real regression. CI has shown red on 545/546 since the Continua passes started; a future regression that lands the suite at 544/546 may be missed because the noise floor is non-zero.
**Likelihood**: low (the failure mode is well-understood) but the cost of missing a regression behind it is high.
**Cost if hit**: undetected regression ships to live.

### R4 · No `layout_family` gate on `WebTemplate` write paths
**Surfaces**: `apps/catalog/migrations/000x_add_layout_family.py` (when it landed) · `apps/catalog/template_dna.py` per-sibling.
**Failure mode**: the 6th-sibling enrollment could in principle skip the `layout_family` field assignment and the renderer would fall through to LF-1 silently (today's dispatcher behaviour). The system trusts the planner to set the field.
**Likelihood**: low (planner-brief explicitly fills it) but real if the next sibling is built by a less-experienced agent.
**Cost if hit**: silent layout-family collapse to LF-1 — exactly the original problem this work eliminated.

### R5 · LF-2 cream nav + LF-2 cream CTA closer set a precedent
**Surfaces**: `_layouts/lf2/styles.html` · `_base.html` LF-2 nav variant.
**Failure mode**: LF-2 demoted CS-TONE-03 (one dark band per home) at the family level by shipping zero dark bands on home (KPI lives in hero overlay; CTA closer is cream). This is documented and intentional. But future siblings may invoke "LF-2 set the precedent" to demote CS-TONE-03 in families where the rule still holds.
**Likelihood**: medium. The argument is plausible but wrong: LF-2's demotion is family-scoped, not cluster-scoped.
**Cost if hit**: a new sibling with no dark band on home in a non-LF-2 family — collapse of the cluster's editorial-punctuation discipline.

### R6 · Imagery URL pool collision risk grows non-linearly
**Surfaces**: `apps/catalog/preview_imagery.py` · `business-{corporate,fiscal,coaching,architecture,stewardship}` pools · CS-IMG-SRC-04 zero-overlap grep.
**Failure mode**: with 5 live pools, the union covers 30+ Pexels URLs. The 6th sibling's curator must clear against all 30+. Curator scout passes are linear in URL count today; the collision-check is constant-time but the scout time grows.
**Likelihood**: certain (each new sibling expands the union). The risk is that a curator misses a URL collision and the grep catches it late.
**Cost if hit**: imagery re-scout mid-build (1 day).

### R7 · `?preview=1` legacy flag still in propagated URLs
**Surfaces**: corporate-suite chrome · `apps/catalog/views.py` `cases_parent_slug` resolver was the last fix.
**Failure mode**: benign today (no-op pass-through after public flip). But the chrome is still propagating it; if a future view changes the staff-preview gate behaviour, the propagated flag could re-acquire meaning unexpectedly.
**Likelihood**: low.
**Cost if hit**: subtle staff-only URL leakage into anonymous shared links.

### R8 · The cluster has no documented retirement protocol
**Surfaces**: none.
**Failure mode**: the system has documented enrollment (intake → A.5 → A.6 → C → D → flip), enforcement (rubric), and migration (Continua LF-3 → LF-5), but **no retirement protocol**. If a sibling ever needs to be unpublished (e.g., Pragma's Unsplash debt forces a withdrawal pending re-curation), there is no documented sequence.
**Likelihood**: low in the short term.
**Cost if hit**: ad-hoc retirement, ad-hoc test cascade, ad-hoc tier_reason rewrite.

R1 + R2 + R3 are the three the next workstream should resolve before the 6th sibling opens. R4–R8 can ride the next sibling's normal workflow.

---

## §6 · Booking-flag failure · classification

`test_medical_and_restaurant_templates_have_booking_flag` fails because Continua's seed carries `has_booking=True` (Wave-2 design intent — family-office mandate-dialogue is booking-shaped) but the test enumerates the medical/restaurant/lawyer/W2-booking exact slug-set. Continua is not a member of any of those families, so set difference reads `Items in the first set but not the second: 'continua-stewardship'`.

**Classification**: **isolation candidate, NOT a 6th-sibling blocker**.

- It does not affect any sibling's render, build, walk, anonymous reachability, or flip cascade.
- It has been observed across **8 consecutive corporate-suite passes** (Continua A.4 → A.5 → A.6 → C → D → flip · Cornice A.5 → A.6 → C → D → flip) and has produced **zero new failures** on any of them.
- Its presence is a noise-floor problem (CI reads 545/546 instead of 545/545 / 546/546), not a correctness problem.

**Recommended action** (in the next hardening pass, NOT inside the next sibling's enrollment):

Either:
- (a) Re-cohort the assertion to enumerate "Wave-2 booking-shaped" templates explicitly and add `continua-stewardship` to the included set; OR
- (b) Revert the Continua seed to `has_booking=False` and document the design intent change.

Option (a) is preferred because the design intent (family-office mandate-dialogue is booking-shaped) was deliberate at Wave-2 design. The assertion's cohort, not the seed, is wrong.

**This work is decoupled from the 6th-sibling enrollment.** It can be done in any 30-minute slot. It should not be done inside an enrollment because that bundles unrelated test-cohort work with feature work and pollutes the flip cascade.

---

## §7 · Are we ready to scale to a 6th sibling?

Verdict: **the system is technically ready · the documentation layer is not.**

Technical readiness checklist:
- [x] Layout-family dispatcher `_layouts/{lf1..lf5}/home.html` works under two real additions (LF-2 Cornice · LF-5 Continua).
- [x] LF-2 + LF-5 + LF-{NEW} + LF-6 reserved territory is enumerated.
- [x] Workflow A.5 → A.6 → C → D → flip pipeline ran end-to-end **twice in a row** (Continua, Cornice) with the same recipe.
- [x] Frozen-sibling regression discipline holds (0/4 drift on the most recent flip).
- [x] User-handshake gate is ratified (R-SOL-8 / SOP §5.4 / CS-BLOCK-13 / D-102).
- [x] Selector-scoped chrome variation (`body.cs-lf-lf-2`) does not leak into out-of-family siblings.
- [x] Public-flip cascade is documented to the line in `release-gatekeeper.md §6`.

Documentation readiness checklist:
- [ ] **Distinctness matrix updated to 5 columns** (Pragma · Cornice · Fiscus · Solaria · Continua). Currently 3.
- [ ] **Reference pack updated to 5 columns**. Currently 3.
- [ ] **Layout-family assignment file updated to reflect live state** (Continua = LF-5 active · Cornice = LF-2 active, both `published_live`). Currently shows Continua as "pending migration to LF-5" and LF-2 as "OPEN for 5th sibling".
- [ ] **Pragma ↔ Fiscus 2/9 audit decision** filed (either re-bin one of them on L7/L9, or formally accept the score with a § decision and document the reason).
- [ ] **Booking-flag noise** isolated.
- [ ] **6th-sibling intake template** verified to score against the 5-column matrix, not the 3-column.

The technical pipeline says "yes." The documentation layer says "if the planner reads what is on disk today, they will pick a 6th sibling that collides with Continua or Cornice without realising it."

**Going to 6th right now risks repeating the original problem, not because the layout-family system is wrong but because the operational reference layer is stale.** The fix is not deep — it is a focused document-refresh pass scoped to roughly 4 files. See `post-cornice-next-candidate-readiness.md` for the recommended next-step sequence.

---

## §8 · Is the current process good enough, or is it drifting?

**The process is good enough at the recipe level. It is drifting at the reference layer.**

What the process gets right:
- The pipeline (intake → A.5 → A.6 → C → D → flip) is reproducible. Two consecutive end-to-end runs without re-discovery.
- The HOLD-on-doubt gate is ratified — neither flip skipped the user handshake.
- The frozen-sibling regression discipline is enforced and held.
- The L1–L9 family declaration prevents skin-only differentiation collapse at the structural layer.

What the process is drifting on:
- The **reference layer** that the planner reads at intake (`distinctness-matrix.md`, `reference-pack.md`, `layout-family-assignment.md`) is updated **less often than siblings ship**. Three of the four files in scope today are 3 days stale relative to the live state.
- The **booking-flag failure** has been classified-and-deferred at every flip. That is correct in isolation but cumulatively it normalises a non-zero noise floor.
- The **Pragma ↔ Fiscus 2/9 score** has been deferred at every pass since the divergence plan. Each deferral is rational; the pattern of deferrals is the drift.

The drift is documentation-layer drift, not engineering-layer drift. **It is exactly the kind of debt that compounds quietly until the next intake reads the wrong document and a sibling ships into the wrong family slot.** A short hardening pass closes it before it does any damage. The detail is in `post-cornice-next-candidate-readiness.md`.

---

## §9 · Anchor to the original objective

The user's stated objective at the start of this work was:

> "a scalable factory for many premium, modern, elegant, professional, clearly distinct templates."

State per dimension:

- **Many**: 24 live templates · 5 in the corporate-suite cluster, 19 across other archetypes · the editor program closed at 19 archetypes · the corporate-suite cluster has open LF-2 (now occupied), LF-6 (reserved), and LF-{NEW}. The factory has demonstrated it can keep adding without breaking what shipped.
- **Premium**: every shipped sibling cleared `corporate-suite-quality-scorecard.md` Layer-1/2/3 with aggregate ≥4.50, 0 BLOCKING, ≤3 STRONG. The "premium = generous restraint + serif italic-em + cream paper + Pexels editorial photography + Latin wordmark + RTL parity" contract holds across all five.
- **Modern**: CSS custom properties · logical RTL properties · `:focus-visible` gold ring · `prefers-reduced-motion` honoured · 5 viewports verified (1920/1440/1280/1100/880/720/480).
- **Elegant**: serif heading + sans body + italic-`<em>` emphasis + one dark band per home (LF-2's family-level demotion explicitly justified) + cream paper baseline + 100×72 padding.
- **Professional**: real albo IDs · real ODCEC/ICF/OAPPC/MIBAC credentials · Lei-register Italian · zero hyperbole bank · zero "Get started free" CTAs.
- **Clearly distinct**: 9 of 10 sibling pairs ≥5/9 layout-distinctness. 1 pair (Pragma↔Fiscus) at 2/9 — known weak, tracked, untreated.
- **Scalable**: the public-flip cascade is a recipe. The layout-family system is the right abstraction. The reference layer is the bottleneck — fix that and the factory throughput equals the cost of one sibling's content + imagery, not one sibling's exploration.

The objective is not "achieved and shut" — it is "validated as the right framing, with one identified bottleneck (the reference layer) blocking continued throughput." A short hardening pass dissolves the bottleneck.

---

## §10 · Final state summary

```
corporate-suite cluster · 5 siblings live · 5 LF slots populated:

  Pragma     LF-1 · Boardroom Vertical          · advisory                 · published_live
  Cornice    LF-2 · Editorial Spread             · architecture studio      · published_live
  Fiscus     LF-3 · Compliance Calendar          · commercialista           · published_live
  Solaria    LF-4 · Manifesto-First              · executive coaching       · published_live
  Continua   LF-5 · Stewardship Object-Hero      · stewardship/family-office · published_live

  LF-6 · Rail-Side Chrome                        · RESERVED · 6th–7th sibling
  LF-{NEW}                                       · OPEN     · planner-declared addendum

Catalog: 24 live / 0 draft · tests 545/546 (booking-flag pre-existing) · smoke 45/45 ×5

Solved: structural sameness · skin-only differentiation collapse · single shared home.html ·
        empty-grid leadership debt · multilingual rollout cadence · public-flip recipe.

Strong: layout-family system · selector-scoped chrome variation · voice-anchor verbatim ·
        public-flip cascade · 0px frozen-sibling regression · user-handshake gate.

Weak:   3-column distinctness matrix · 3-column reference pack · stale family-assignment file ·
        Pragma↔Fiscus 2/9 layout pair · booking-flag noise floor · `?preview=1` propagation ·
        Pragma Unsplash grandfather · no retirement protocol.

Next:   Short hardening pass on the documentation layer + Pragma↔Fiscus decision +
        booking-flag isolation, BEFORE 6th sibling enrollment opens.
        Detail in post-cornice-next-candidate-readiness.md.
```
