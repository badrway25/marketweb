# Corporate-suite layout variance rules

**Status**: rule book v1 · **Date**: 2026-04-29
**Scope**: corporate-suite archetype only.
**Companion files**: `corporate-suite-layout-divergence-plan.md` (the why) · `corporate-suite-layout-family-matrix.md` (the slotting per family).
**Cross-references**: `factory/standards/corporate-suite-design-standard.md` (CS-* rule IDs) · `factory/standards/corporate-suite-blocking-rules.md` (CS-BLOCK-*) · `factory/standards/corporate-suite-browser-rubric.md` (BRWS-*) · `design-orchestrator/DISTINCTNESS_RULES.md`.

This file is the operational rule book. Every rule has an ID, a severity, an enforcement gate, an evidence-pointer pattern, and a failure mode. The plan justifies the rules. This file binds them.

---

## 0 · Severity ladder

Same ladder as the existing standards layer.

| Tier | Meaning | Where it gates |
|---|---|---|
| **[BLOCKING]** | Merge-blocker. Walk-fail. No waiver without a § decision. | Build · Walk · Release-gatekeeper. |
| **[REQUIRED]** | Walk-fail. Waiver only with § decision recorded in the design-standard. | Walk · Release-gatekeeper. |
| **[STRONG]** | Critique-flag. Re-spec preferred but not blocking. | Style-critic · Plan re-spec. |
| **[GUIDELINE]** | Style preference. Documented for cluster cohesion. | Plan-time annotation only. |

Every CS-LAYOUT-* rule below carries one tier. The tier is what the orchestrator reads when deciding whether a draft passes a gate.

---

## 1 · The nine layout dimensions (CS-LAYOUT-01..09)

Each dimension below has:
- A **name** (the L# from the divergence plan).
- An **enumerated value set** — the legal classifications. New values are added by orchestrator decision; siblings may not invent values inline.
- A **default** — what unfamilied home would render.
- A **family-scoped** flag — true means the dimension is chosen per layout family; false means archetype-shared and never varies.

### CS-LAYOUT-01 [REQUIRED] · Hero geometry (L1)
- **Values**: `split-55-45` · `stacked-editorial` · `object-overlay` · `side-rail-photo` · `type-only`.
- **Default**: `split-55-45` (current cluster shape).
- **Family-scoped**: yes. Each layout family declares one hero geometry.
- **Interaction with CS-HERO-01**: CS-HERO-01 is hereby **demoted from BLOCKING to REQUIRED-at-family-level**. The "55/45 split serif L + photo R" is no longer the cluster invariant — it is LF-1's hero geometry. Other families declare different geometries. The cluster invariant is only that the hero is the first section and is editorial-grade (CS-HERO-02 stays BLOCKING).
- **Failure mode**: a sibling silently inherits LF-1's split when the planner did not declare LF-1. Catch at B-LAYOUT-3 classification.
- **Evidence**: `home.html` first section's grid/flex template. Wireframe capture at 1920px.

### CS-LAYOUT-02 [REQUIRED] · Section sequence (L2)
- **Values**: per-family ordered list of `<section class="cs-*">` names, declared in the family matrix.
- **Default**: LF-1's `cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta`.
- **Family-scoped**: yes.
- **Interaction with CS-RHYTHM-02**: CS-RHYTHM-02 is **demoted from REQUIRED to REQUIRED-at-family-level**. The cluster no longer fixes one home order; the family does. CS-RHYTHM-04 ("no two adjacent sections share function") stays REQUIRED at archetype level.
- **Failure mode**: section list collides with another sibling's (B-LAYOUT-2 fails).
- **Evidence**: `document.querySelectorAll('section[class*="cs-"]')` enumeration on the live home, recorded in `walk-log.md`.

### CS-LAYOUT-03 [REQUIRED] · Mid-strip differentiator slot (L3)
- **Values**: `absent` · `slot-2` · `slot-4` · `slot-5` · `slot-6` · `slot-2+slot-4` (multi-cell families).
- **Default**: `absent`.
- **Family-scoped**: yes.
- **Composition**: the mid-strip is the family's named cadence cell — calendar-cadence (LF-3), method-cadenza (LF-4), governance-cycle (LF-5). It is what the user remembers as "what makes this firm different."
- **Failure mode**: two siblings claim the same slot AND the same cell shape (e.g., two siblings both shipping a `cs-cycle` at slot-4). Catch at distinctness-matrix re-fill.
- **Evidence**: `home.html` line range of the mid-strip section, plus the cell's eyebrow + figure + context shape.

### CS-LAYOUT-04 [REQUIRED] · Pillars treatment (L4)
- **Values**: `numbered-grid` · `vertical-stagger` · `2x2-with-image` · `essay-with-anchors` · `side-quote-with-cards` · `manifesto-replacement` · `4-pillar-matrix` · `absent`.
- **Default**: `numbered-grid`.
- **Family-scoped**: yes.
- **Interaction with CS-DENSITY-02**: card count constraint (3 or 4, never 6) stays archetype-shared. Visual treatment is the family's choice.
- **Failure mode**: two siblings render the same numbered-grid AND the same card shape AND the same number of pillars. Catch at wireframe overlay (B-LAYOUT-1).
- **Evidence**: `home.html` `cs-pillars .grid` template and child structure.

### CS-LAYOUT-05 [REQUIRED] · KPI placement (L5)
- **Values**: `hero-overlay` · `band-at-3` · `band-at-4` · `band-at-5` · `band-at-closer` · `narrative-prose-replacement`.
- **Default**: `band-at-3`.
- **Family-scoped**: yes.
- **Interaction with CS-RHYTHM-03 / CS-TONE-03**: the **one dark band per home** archetype invariant stays. The position of that dark band is the family's choice. If the family elects `narrative-prose-replacement` (LF-2), it loses the dark band and must compensate by placing the dark band on the `cs-cta` closer (CS-CTA-05 already covers that).
- **Failure mode**: a family declares `narrative-prose-replacement` AND a non-dark `cs-cta` closer — zero dark bands on home. Catch at CS-TONE-03 audit during walk.
- **Evidence**: `home.html` section order + each section's `background` token.

### CS-LAYOUT-06 [REQUIRED] · Leadership presence (L6)
- **Values**: `absent` · `typographic-grid` · `photo-grid` · `single-portrait-feature` · `pillar-photo`.
- **Default**: `typographic-grid`.
- **Family-scoped**: yes.
- **Interaction with CS-DENSITY-05**: the 3–6 person count constraint (when leadership is present) stays archetype-shared. The presence/absence and visual treatment are the family's choice.
- **Failure mode**: a sibling ships an **empty** leadership grid because its registry list is empty (current Solaria-style debt). Catch by enforcing that `cs-leadership` only renders when L6 ≠ `absent`.
- **Evidence**: `home.html` presence/structure of `<section class="cs-leadership">`.

### CS-LAYOUT-07 [REQUIRED] · Cases-preview shape (L7)
- **Values**: `list-row` · `magazine-grid` · `timeline` · `collage-3+1` · `single-feature + sub-list` · `gallery-strip`.
- **Default**: `list-row`.
- **Family-scoped**: yes.
- **Interaction with CS-DENSITY-06**: the 3–6 case count on home stays archetype-shared.
- **Failure mode**: two siblings render the same shape with the same field order (number · title · category · year · arrow). Catch at wireframe overlay.
- **Evidence**: `home.html` `cs-cases-preview` template.

### CS-LAYOUT-08 [STRONG] · Navbar geometry (L8)
- **Values**: `sticky-top` · `side-rail` · `drawer-only` · `split-wordmark-top` · `condensed-minimal-top`.
- **Default**: `sticky-top`.
- **Family-scoped**: yes.
- **Interaction with CS-NAV-01**: CS-NAV-01 is **demoted from BLOCKING to STRONG-at-family-level**. The primary-background polarity (CS-BLOCK-16) stays BLOCKING — no family may render a non-`--primary`-background nav. The geometry of the nav, however, is family-scoped.
- **STRONG** rather than REQUIRED because navbar geometry change carries a heavy responsive matrix re-walk cost; the orchestrator may approve a family that stays at `sticky-top` if the L1+L2+L7 differences already buy enough wireframe distinctness.
- **Failure mode**: a non-`sticky-top` family ships without re-walking the responsive matrix at 1920/1440/1280/1024/768/640/414/390 (CS-RESPONSIVE-02).
- **Evidence**: `_base.html` `<nav class="cs-nav">` line range + responsive screenshots.

### CS-LAYOUT-09 [REQUIRED] · Footer structure (L9)
- **Values**: `3-col` · `4-col-with-whistleblowing` · `2-col-stacked` · `full-bleed-crest` · `condensed-single-row`.
- **Default**: `3-col`.
- **Family-scoped**: yes.
- **Interaction with CS-FOOT-01 / CS-FOOT-02 / CS-FOOT-05**: the legal-row contents (CS-FOOT-02 — copyright + P.IVA + privacy + cookie + whistleblowing where applicable) stay archetype-shared. The column count and visual structure are the family's choice. CS-FOOT-05 (≤720px collapse) stays REQUIRED at archetype level.
- **Failure mode**: a layout family that requires whistleblowing legal surfacing (LF-5 stewardship · LF-3 commercialista) ships a `condensed-single-row` footer that drops the whistleblowing channel. Catch at CS-FOOT-02 audit.
- **Evidence**: `_base.html` `<footer class="cs-foot">` line range.

---

## 2 · The variance contract (CS-LAYOUT-10..14)

Rules that bind the nine dimensions together into a layout-family identity.

### CS-LAYOUT-10 [BLOCKING] · A new sibling MUST declare a layout family at intake
- The planner brief at workflow A.2 names one of `LF-1` · `LF-2` · `LF-3` · `LF-4` · `LF-5` · `LF-6` · or `LF-{NEW}` and justifies the choice.
- For `LF-{NEW}`, the planner files an addendum to `corporate-suite-layout-family-matrix.md` declaring the L1–L9 tuple, the professional fit, and what the family is reserved for.
- **Failure mode**: a brief lands without a layout family. The orchestrator halts the build at intake §0.5.

### CS-LAYOUT-11 [BLOCKING] · No two siblings may share a layout family
- After Pragma=LF-1, Fiscus=LF-3, Solaria=LF-4, Continua=LF-5, those four families are TAKEN. The next sibling claims LF-2, LF-6, or `LF-{NEW}`.
- Reuse of an occupied family is permitted **only** under DISTINCTNESS_RULES §5 option 3 (variant demotion), which requires explicit user approval and shared base assets.
- **Failure mode**: two siblings both claiming LF-3. Catch at distinctness-matrix re-fill (column collision).

### CS-LAYOUT-12 [BLOCKING] · Sibling pairs must differ on ≥4 of 9 layout dimensions
- For every existing sibling, the new sibling's L1–L9 tuple must differ on ≥4 of 9 dimensions. The two-sibling pair otherwise scores layout-collision regardless of how the skin axes score.
- This is the layout analogue of the existing 4-of-5-axes rule in DISTINCTNESS_RULES §1.
- **Failure mode**: a new sibling shares 7 of 9 layout dimensions with Pragma. Plan re-spec required.

### CS-LAYOUT-13 [BLOCKING] · Sibling pairs MUST differ on at least one of L1, L2, L7
- L1 (hero), L2 (section sequence), L7 (cases-preview shape) are the three highest-leverage wireframe-difference dimensions. At least one of these three MUST differ between any two siblings.
- This rule prevents "diff on small dimensions only" — e.g., differing on footer + leadership + nav-condensed but staying same on hero + section order + cases shape, which would still produce the >90% bounding-box overlap the cluster is fixing.
- **Failure mode**: two siblings share `(split-55-45, A, list-row)` and only differ on dimensions 4–9. Plan re-spec required.

### CS-LAYOUT-14 [BLOCKING] · Layout family declared at intake MUST match the live render
- The B-LAYOUT-3 classification at walk time MUST equal the planner-declared layout family. Drift between declared and rendered is a build defect.
- **Failure mode**: planner declares LF-5, builder renders LF-3 with cosmetic LF-5 elements. Walk fails.

---

## 3 · What MUST stay archetype-shared (CS-LAYOUT-20..22)

These are the cluster invariants that no layout family may override. They protect the cluster's brand identity against family-level drift.

### CS-LAYOUT-20 [BLOCKING] · The brand contract is shared across all layout families
The following CS-* rules remain archetype-shared and are inherited verbatim by every layout family. A family that needs to break one of these is not a corporate-suite family — it should be planned in a different cluster.

| Domain | Rule IDs | Summary |
|---|---|---|
| Typography | CS-TYPE-01 · CS-TYPE-02 · CS-TYPE-04 · CS-TYPE-05 · CS-TYPE-06 | Serif heading + sans body · italic-`<em>` emphasis only · scale ceilings · eyebrow tracking · RTL Noto Kufi swap. |
| Palette | CS-PAL-01 · CS-PAL-04 · CS-PAL-05 · CS-PAL-06 | h1 AAA on cream · dark-section descendant contrast · accent budget ≤3 hits per viewport · nav background = `--primary`. |
| Hero baseline | CS-HERO-02 · CS-HERO-03 · CS-HERO-05 · CS-HERO-07 | Editorial photography (not stock) · h1 AAA contrast · subhead ≤35 words · ≤720px stack. |
| Imagery | CS-IMG-SRC-01 · CS-IMG-SRC-04 · CS-IMG-COH-01 · CS-IMG-COH-02 | Pexels-only · zero URL overlap across siblings · 3-second subject check · mood matches voice. |
| Locale + RTL | CS-NAV-03 · CS-NAV-06 · CS-FOOT-03 · CS-EXEC-01 / F2 | Locale-pill switcher · Latin wordmark + numerics in RTL · voice anchor verbatim across 5 locales. |
| Section rhythm | CS-RHYTHM-01 · CS-RHYTHM-04 · CS-RHYTHM-06 | 100×72 padding · no adjacent function-duplicates · padding IS the rhythm (no extra section margins). |
| Density | CS-DENSITY-01 · CS-DENSITY-02 · CS-DENSITY-04 · CS-DENSITY-05 · CS-DENSITY-06 · CS-DENSITY-07 | Hero copy floors/ceilings · pillar count 3–4 · KPI count 3–4 · leadership 3–6 · cases 3–6 on home · no walls of text. |
| Dark-band economy | CS-TONE-03 / CS-RHYTHM-03 | One dark band per home (or zero — when family elects `narrative-prose-replacement` at L5, the closer must hold the dark beat). |
| Motion | (cluster invariant per `corporate-suite-distinctness-matrix.md §1.11`) | Low motion · staggered reveals · slow marquee · `prefers-reduced-motion` honored. No layout family adds hero video, parallax beyond `[data-lm]`, or scroll-jacking. |
| Editor isolation | CS-MARKET-01 / `body.mw-is-editor-preview` guard | Editor click-to-edit affordances do not leak into `/live/`. |
| CTA contract | CS-CTA-01 · CS-CTA-02 · CS-CTA-03 · CS-CTA-04 | One primary per viewport · advisor-voice CTA copy · ghost/outline secondary · real route hrefs. |
| Focus | CS-NAV-02 / E1 | Gold `:focus-visible` ring on every interactive (2px outline + 4px offset). |
| Whistleblowing | CS-FOOT-02 (where required) | D.lgs. 24/2023 channel surfaced for advisory/commercialista/law/stewardship sub-clusters regardless of footer column count. |

A layout family that proposes a deviation from any CS-LAYOUT-20 row triggers a § decision review. Approvals are recorded in the design-standard like any other waiver.

### CS-LAYOUT-21 [BLOCKING] · Class prefix `cs-*` is shared across layout families
Every section in every layout family uses `class="cs-{name}"`. This is what keeps style-critic side-by-side comparisons coherent across families and what allows the responsive matrix to share `_base.html` tokens.
- **Failure mode**: LF-2 renames `cs-pillars` to `cs-narrative-band`. Block at the build review.

### CS-LAYOUT-22 [REQUIRED] · Layout family is declared in the registry
The `WebTemplate` row carries a `layout_family` column (or equivalent registry field) populated at seed time. The shared `home.html` shell or its router uses this to dispatch.
- **Failure mode**: a sibling renders the wrong layout family because the registry field is missing. Catch at B-LAYOUT-3 classification.

---

## 4 · Failure modes catalogue

Named failure modes the rules above are designed to catch. Each carries a diagnostic so the walk-verifier can label evidence quickly.

### F-LAYOUT-01 · Skin-only differentiation collapse
- **Symptom**: two siblings overlay at >90% bounding-box surface area (B-LAYOUT-1 fail).
- **Cause**: same layout family applied with different palette + copy + imagery.
- **Trigger rule**: CS-LAYOUT-11 / CS-LAYOUT-12 / CS-LAYOUT-13.
- **Action**: re-spec the colliding sibling into a different layout family.

### F-LAYOUT-02 · Empty-section debt
- **Symptom**: a `<section>` renders with an empty card grid because its content registry list is empty (current Solaria-style debt; current cs-leadership when leadership list is empty).
- **Cause**: section is unconditionally rendered; layout family does not omit it.
- **Trigger rule**: CS-LAYOUT-06 (when `absent` is the family's choice).
- **Action**: gate the section render on the layout family's L6 value.

### F-LAYOUT-03 · Slot-collision in mid-strip
- **Symptom**: two siblings ship a `cs-cycle`-shaped section at slot-4 with three `(eyebrow, figure, context)` cells (current Fiscus + Continua state).
- **Cause**: shared mid-strip slot + shared cell shape + different copy.
- **Trigger rule**: CS-LAYOUT-03 + CS-LAYOUT-12.
- **Action**: move one sibling's mid-strip to a different slot AND/OR change the cell shape (LF-5 promotes cycle to slot-2 and reshapes context to a horizon-context paragraph).

### F-LAYOUT-04 · Hero-geometry monoculture
- **Symptom**: every sibling renders 55/45 split serif-L + photo-R.
- **Cause**: CS-HERO-01 was BLOCKING for the whole cluster.
- **Trigger rule**: CS-LAYOUT-01 (now REQUIRED-at-family-level).
- **Action**: at least one new sibling per cluster-quarter ships a non-`split-55-45` hero geometry.

### F-LAYOUT-05 · Cases-shape monoculture
- **Symptom**: every sibling renders `list-row` cases preview.
- **Cause**: shared `home.html` template; only `list-row` is implemented.
- **Trigger rule**: CS-LAYOUT-07.
- **Action**: ship `magazine-grid` (LF-2), `timeline` (LF-5), `collage-3+1` (LF-6) implementations.

### F-LAYOUT-06 · Layout-family drift between intake and walk
- **Symptom**: planner declared LF-5 but live render classifies as LF-3 with LF-5 copy.
- **Cause**: builder did not implement the L1/L2/L7 changes; only changed copy/imagery.
- **Trigger rule**: CS-LAYOUT-14.
- **Action**: walk fails. Builder returns to A.4. Style-critic flags the layout-implementation gap.

### F-LAYOUT-07 · Whistleblowing surface dropped by a condensed footer
- **Symptom**: family elects `condensed-single-row` footer and the legal row drops the whistleblowing link.
- **Cause**: footer compaction removed the legal-row cell that hosted whistleblowing.
- **Trigger rule**: CS-LAYOUT-09 + CS-FOOT-02.
- **Action**: family must either reject `condensed-single-row` for this sibling OR adjust the family's footer template to keep whistleblowing in the condensed row.

### F-LAYOUT-08 · Zero dark bands on home
- **Symptom**: family elected `narrative-prose-replacement` at L5 AND a cream-paper closer.
- **Cause**: dark-band economy (CS-TONE-03) requires one dark band; the family must place the dark beat somewhere.
- **Trigger rule**: CS-LAYOUT-05 + CS-LAYOUT-20 (cluster invariant).
- **Action**: family must move the dark band to the closer (`cs-cta` dark) or to a slot-X mid-strip.

### F-LAYOUT-09 · Sticky-top inheritance under a side-rail family
- **Symptom**: family declared `side-rail` at L8 but `_base.html` still renders the sticky-top nav.
- **Cause**: navbar geometry not actually swapped; only declared.
- **Trigger rule**: CS-LAYOUT-08 + CS-LAYOUT-14.
- **Action**: walk fails.

### F-LAYOUT-10 · Manifesto-replacement without omitted leadership
- **Symptom**: LF-4 ships the manifesto replacing pillars but still renders an empty leadership card grid.
- **Cause**: L4 was changed but L6 was not — partial layout-family implementation.
- **Trigger rule**: CS-LAYOUT-04 + CS-LAYOUT-06 + CS-LAYOUT-14.
- **Action**: builder closes the L6 gap (omit leadership), or the family declaration is wrong and must be re-spec.

---

## 5 · Walk-verifier rule additions (B-LAYOUT-1..3)

Codified for `factory/standards/corporate-suite-browser-rubric.md`. These three new rubric lines are added to §5 (the verification matrix) and §6 (evidence requirements).

### B-LAYOUT-1 [BLOCKING] · Wireframe overlay compare
**At every walk**, capture a layout-only outline of `home.html` at 1920px. Each `<section>` rendered as a coloured rectangle with `class` name and bounding box, no copy/photos/colour. The capture is automatic via a `walk_layout_overlay()` helper in the walk script.

The capture overlays against every existing sibling's wireframe pair (LF-1 vs the new sibling, LF-3 vs new, LF-4 vs new, LF-5 vs new, etc).

- **Pass condition**: ≥30% of total bounding-box surface area differs from each sibling.
- **Fail condition**: ≥90% identical bounding boxes against any sibling. → CS-LAYOUT-12 / F-LAYOUT-01.
- **Evidence file**: `_compare-{sibling}-1920-wireframe.png` (one per sibling pair, in addition to the existing `_compare-{sibling}-1920.png` skin capture).

### B-LAYOUT-2 [BLOCKING] · DOM-section list compare
**At every walk**, enumerate `document.querySelectorAll('section[class*="cs-"]')` on the live home and record the ordered list of class names in `walk-log.md`.

- **Pass condition**: section list differs by ≥2 entries (insertions + deletions + re-orderings) from every existing sibling.
- **Fail condition**: identical list to an existing sibling. → CS-LAYOUT-11.
- **Evidence file**: `walk-log.md §section-list` block.

### B-LAYOUT-3 [REQUIRED] · Layout-dimension classification
**At walk start**, the verifier classifies the new sibling along all nine L1–L9 axes using the value sets in CS-LAYOUT-01..09. The classification is recorded as a row appended to `corporate-suite-layout-family-matrix.md`.

- **Pass condition**: classification matches the planner-declared layout family AND no two siblings share the full L1–L9 tuple AND ≥4 of 9 layout dimensions differ vs every existing sibling.
- **Fail condition**: classification drift from the declared family OR exact L1–L9 collision OR <4 dimensions differ. → CS-LAYOUT-12 / CS-LAYOUT-14 / F-LAYOUT-06.
- **Evidence file**: `walk-log.md §layout-classification` block + an updated `corporate-suite-layout-family-matrix.md` row.

---

## 6 · How rules apply at each workflow gate

| Workflow gate | Rules enforced | Evidence written |
|---|---|---|
| A.1 intake | CS-LAYOUT-10 · CS-LAYOUT-11 · CS-LAYOUT-13 | Brief declares layout family + L1–L9 tuple. |
| A.2 plan | CS-LAYOUT-12 · CS-LAYOUT-13 | Plan re-spec on collision. Distinctness matrix updated to project the new column. |
| A.3 pack | CS-LAYOUT-20 (imagery row only) | Pexels pack avoids URL overlap. |
| A.4 build | CS-LAYOUT-01..09 · CS-LAYOUT-21 · CS-LAYOUT-22 | DOM matches family declaration. `cs-*` prefix maintained. Registry row carries `layout_family`. |
| A.6 critique | All CS-LAYOUT-* | Style-critic does the side-by-side wireframe overlay and flags any F-LAYOUT-* trigger. |
| A.7 walk | All CS-LAYOUT-* + B-LAYOUT-1/2/3 | Walk evidence directory holds wireframe captures + section-list logs + classification row. |
| B edit-pass | CS-LAYOUT-12 + B-LAYOUT-1 + B-LAYOUT-3 | Re-classify after any layout-touching edit. |
| Release-gatekeeper | CS-LAYOUT-10..14 + B-LAYOUT-3 | Final verdict references the layout family slot the sibling occupies. |

The rule set is monotonic — once a layout family is occupied (e.g., LF-3 = Fiscus), future siblings inherit the prohibition. The cluster's open territory shrinks by one family per landing.

---

## 7 · Open questions deferred to the next pass

These are decisions the rule book deliberately defers to keep this hardening pass scoped.

1. **Does the shared `home.html` get split into `_layouts/{lf1..lf5}/home.html` or stay one file with template-tag dispatch?** The plan recommends split; the build pass decides. Documented when Step 3 of the divergence plan executes.
2. **Where does `layout_family` live on the registry — `WebTemplate` column, `template_dna.py` field, or both?** Both, likely. Decided at Step 2.
3. **Does LF-2 ship `condensed-minimal-top` or `split-wordmark-top` at L8?** The matrix defaults LF-2 to `split-wordmark-top`; the LF-2 build pass may re-spec.
4. **Does LF-6 actually ship `side-rail` or stay reserved indefinitely?** LF-6 is held as a reserved slot until a real candidate enrolls; the matrix declares its tuple so the slot exists, but no sibling occupies it yet.
5. **Cross-cluster impact**: does the layout-family system port to medical-specialist, restaurant, portfolio, etc.? Out of scope for this hardening; addressed when the second cluster reference-pack lands per `design-orchestrator/NEXT_STEPS.md §1`.

These are not blockers for this hardening; they are the natural next decisions once the rules are codified.
