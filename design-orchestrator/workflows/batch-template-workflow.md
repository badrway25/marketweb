# Batch template workflow

How to process many templates in an orderly queue without collapsing into sibling clones, generic stock output, or one-template-at-a-time serial execution that never reaches the catalog scale the user is targeting.

This workflow sits ABOVE the single-template prompts (`template-orchestrator-master.md`, `template-edit-orchestrator.md`, `template-multilingual-orchestrator.md`, `release-decision-orchestrator.md`). It does not replace them. It schedules them.

The user's goal is hundreds of customizable templates. Batch is how that goal becomes operationally reachable; sibling-clone risk is how it most easily fails.

---

## 0 · When to use this workflow

Use batch workflow when:
- Three or more templates are queued (e.g. closing out a cluster · expanding into a new sub-cluster · seasonal rollout).
- A new cluster is being opened and 3-6 siblings need to land in sequence.
- A standards change requires re-walking ≥ 5 published templates.

Do NOT use batch for:
- One-off premium-grade flagship templates (use single-template-workflow instead).
- The first sibling in a brand-new cluster (cluster invariants need to land first; batch them in only after the first is shipped).
- Edit passes (always single-template; an edit batch is a misclassification of either a chrome workflow A or a series of unrelated B passes).

---

## 1 · The eight phases of a batch

A batch flows through eight phases. Each phase has its own gate; the batch does not advance until the gate passes for every template in scope. Phases are sequential at the BATCH level (you do not start phase 4 while phase 3 is still open) but contain controlled parallelism INSIDE the phase (see §3).

```
1. Intake               → all briefs collected · cluster slot assigned
2. Prioritisation       → sequence locked · most distinct first
3. Distinctness gating  → every brief scored vs siblings · no plan starts before clears
4. Design generation    → planner briefs filled · skin / DNA / palette decided
5. Imagery              → packs curated · cross-cluster URL grep clean
6. Browser verification → IT walks per template · no flip yet
7. Multilingual         → workflow C per template · per-locale walks
8. Release decision     → release-decision-orchestrator per template
```

Each phase's exit gate is a binary: every template in scope clears, or the batch holds at this phase.

---

## 2 · Per-phase definition

### Phase 1 · Intake

**Input:** the user's roadmap entry or batch brief naming N templates.
**Tool per template:** `design-orchestrator/workflows/template-intake-checklist.md` filled to completion.

**Per template, output:**
- `factory/reports/<archetype>/<template_slug>/intake.md` with every checklist field answered
- `nearest_two_siblings` field populated and unambiguous
- All five pre-build quick-checks (`design-orchestrator/workflows/pre-build-quick-checks.md`) resolved at intake: §0.5 reference-pack precondition · §3.1 palette warmth grid · §3.2 studio-name swap · §6.5 imagery feasibility · §7.1 content-volume estimate

**Batch-level output:**
- `factory/reports/batches/<batch_id>/intake-roster.md` listing every template, its cluster, its sub-cluster, its nearest siblings, any user constraints, AND the five pre-build quick-check verdicts per template (so the batch sees at-a-glance which templates are GO vs RESPEC vs HALT)

**Cluster precondition for the whole batch**: if the batch covers a non-corporate-suite cluster, every template in scope HALTS at intake §0.5 until that cluster's reference pack and distinctness matrix are on file. The batch's first action becomes "build the cluster's pack" (one-off pass, ~half day), then the templates resume intake. Do not run a multi-template batch in a cluster without its pack — distinctness collisions compound non-linearly across siblings designed against an empty grid.

**Exit gate:** every template has a complete intake checklist on file with all five pre-build quick-checks PASS / GO / CONTINUE. No blanks. Any template stuck at HALT or RESPEC after one re-spec attempt is removed from this batch and queued for clarification.

### Phase 2 · Prioritisation

**Input:** the intake roster.
**Output:** an ordered sequence at `factory/reports/batches/<batch_id>/sequence.md`.

**Sequencing rule (this is the load-bearing decision of the entire batch):**

Order templates such that **the most distinctness-constrained template lands first**, the next most-constrained second, and the least-constrained last. The reason: distinctness is monotonically harder as the cluster fills. If you build the easy-to-differentiate template first and the hard-to-differentiate template last, the last one inherits a tighter budget than the first one had — but that is the right shape, because the cluster's "must not repeat" list grew between them.

**The wrong sequence** is "easiest first, hardest last" if that means the hardest is differentiated against six prior siblings instead of three. Build the hardest cases EARLY when the cluster is thin and they have room.

**Operational test:** for each template, count how many existing siblings (including ones earlier in this batch) it must differentiate against. Sort ascending — the template with the fewest constraints goes first.

**Exit gate:** the sequence is locked. New templates added to the batch after sequence-lock either land at the END of the existing sequence or trigger a re-prioritisation pass.

### Phase 3 · Distinctness gating

**Input:** the locked sequence.
**Per template, sequentially in the locked order:**
- Run `template-orchestrator-master.md §A.2` only · produce the planner brief
- Score against every existing sibling AND every prior template in this batch
- All `axes_different` ≥ 4/5 → continue
- Any score ≤ 3/5 → re-spec this template OR delay it to a later batch

**Per template, output:**
- `<report_root>/planner-brief.md` (full schema)
- The triangulation matrix appended

**Batch-level output:**
- `factory/reports/batches/<batch_id>/distinctness-summary.md` — one row per template · matrix scores · GO / RESPEC / DELAY

**Exit gate:** every template in the sequence is GO. Any template still at RESPEC after one re-spec attempt is removed from this batch.

**Why phase 3 is sequential, not parallel:** if two templates in the same cluster are designed in parallel without seeing each other, they easily produce overlapping palettes / hero meta-strips / voice anchors. Sequential planning means each new brief reads the prior briefs in this batch as if they were already shipped siblings.

### Phase 4 · Design generation

**Input:** GO planner briefs from phase 3.
**Per template:**
- Skin module created or shared with cluster baseline
- DNA entry filled
- Palette tokens defined and matrix-cleared
- Section rhythm specified

**Parallelism allowed:** YES, but ONLY because phase 3 already enforced distinctness. The skin work itself does not collide between templates if the briefs were sequentially de-conflicted upstream.

**Limit:** no more than 3 templates in active design at once per cluster, because the skin partials are shared and merge conflicts grow non-linearly.

**Exit gate:** every template's skin compiles, every DNA entry is registered, every palette is recorded in `corporate-suite-distinctness-matrix.md` (or cluster equivalent) so subsequent templates in the batch see it.

### Phase 5 · Imagery

**Input:** GO planner briefs · DNA entries.
**Per template:** the imagery pack workflow from `template-orchestrator-master.md §A.3`, preceded by the imagery feasibility re-confirm at `template-orchestrator-master.md §A.2.5` (the orchestrator runs ONE Pexels search per declared subject and counts plausible candidates BEFORE the curator commits anything · `pre-build-quick-checks.md §3`).

**Parallelism allowed:** YES, but with a hard discipline:
- A.2.5 feasibility re-confirm runs PER TEMPLATE before that template enters curator hands · any slot ≤ 2 candidates returns to A.2 · do not parallel-curate a template whose subjects the orchestrator has not feasibility-cleared
- BEFORE the curator commits any URL, run the cross-cluster URL grep against EVERY existing pool AND every other pack-in-flight in this batch
- The grep has to be re-run AFTER each pack is committed, before the next pack commits
- If two in-flight packs picked the same Pexels URL, the second-pack curator picks a different URL · no exceptions

**The unsafe parallelism here:** designing two packs in the same cluster simultaneously without grep coordination. They pick the same hero photo, or the same ambient bookshelf, or the same portrait — and only one of them notices.

**Exit gate:** every template's pack is curator-approved AND the cross-cluster grep is clean across all packs in this batch AND across all existing pools. No URL appears twice.

### Phase 6 · Browser verification (IT walks)

**Input:** built templates · live IT URLs.
**Per template:** workflow A.6 (critique) + A.7 (walk) per `template-orchestrator-master.md`.

**Parallelism allowed:** the critique is parallel by design (style + contrast + responsive run in parallel for one template). Across templates, run two walks in parallel at most — beyond that, the human reviewer (or the agent) loses the per-template attention that catches Solaria-class regressions.

**Exit gate:** every template has a PASS walk verdict on file at IT. Any FAIL or BORDERLINE → workflow B before the template moves to phase 7.

### Phase 7 · Multilingual rollout

**Input:** PASS-walked IT templates.
**Per template:** the full `template-multilingual-orchestrator.md` pass.

**Parallelism allowed:** ONE multilingual pass per cluster at a time. Reason: the AR walk specifically interacts with the cluster's chrome (RTL readiness · logical properties · font swap), and parallel AR walks on different templates in the same cluster mask each other's chrome regressions.

Across clusters, parallel multilingual passes are safe (different chrome surfaces).

**Exit gate:** every template has per-locale walks PASS for every locale in scope. AR specifically passes the RTL parity walk.

### Phase 8 · Release decision

**Input:** every template ready for tier flip.
**Per template:** the full `release-decision-orchestrator.md` pass.

**Parallelism allowed:** the gates are parallel-safe (each template is evaluated independently). The user-handshake is sequential by definition (one user, one walk per template).

**Pacing discipline:** do not present 10 templates to the user for handshake on the same day. The user-handshake quality drops as fatigue accumulates. Three templates per handshake session is the upper bound that survived the Solaria precedent without rushing.

**Exit gate:** every template has a release-decision document on file (SHIP or HOLD). Templates flipped to `published_live` enter the regression-watch surface.

---

## 3 · Where parallelism is safe and where it is dangerous

A summary table for quick reference.

| Phase | Parallel within batch | Parallel within cluster | Hazard if violated |
|---|---|---|---|
| Intake | safe | safe | none |
| Prioritisation | n/a (one decision) | n/a | none |
| Distinctness gating | UNSAFE | UNSAFE | parallel briefs collide on palette / hero / voice |
| Design generation | safe (≤ 3 per cluster) | limited | merge conflicts on skin partials |
| Imagery | safe with grep discipline | UNSAFE without grep | duplicate Pexels URLs across packs |
| IT walks | safe (≤ 2 walkers) | safe | reviewer fatigue · missed regressions |
| Multilingual | safe across clusters | UNSAFE within cluster | parallel AR walks mask chrome regressions |
| Release decision | safe (gates) · sequential (handshake) | safe | user-handshake fatigue |

The pattern: planning and identity-decisions are SEQUENTIAL across templates in the same cluster. Skin and pack work is PARALLEL with grep / merge discipline. Browser walks are PARALLEL with reviewer-attention discipline. Release decisions are PARALLEL on gates, SEQUENTIAL on user handshake.

---

## 4 · Stop conditions for the entire batch

The batch HALTS (not just one template) at any of these:

1. **Three or more templates in the batch fail distinctness gating.** This is a signal that the cluster is too saturated for this batch's scope. Re-scope the batch before continuing.
2. **Two consecutive templates in the same cluster collide on palette OR hero photography.** The phase-3 sequential discipline broke down. Pause the batch, audit phase 3, restart from the sequence-lock.
3. **The cross-cluster URL grep finds a duplicate.** A pack from an earlier sibling and a pack-in-flight overlap. Pause, fix the in-flight pack, re-grep, continue.
4. **A walk in phase 6 reveals a Class I (chrome) issue.** The chrome is not where this batch fixes it. Open a separate workflow A on chrome. Pause this batch until the chrome lands and the affected templates re-walk.
5. **A standards file changes mid-batch.** No template uses the new rule until every existing template in the batch is audited against it. Standards changes are between-batch, not within-batch (`ORCHESTRATOR.md §6 rule 5`).
6. **The user requests the batch be expedited past a gate.** Unless the gate is the conservative-override gate at release decision step 10, do not relax. The Solaria precedent is what the gates exist to prevent.
7. **The batch produces more docs than openable live URLs.** This is the anti-drift signal at batch scale. If a batch report tree contains 50 reports and the catalog has 0 new templates, the batch was a process pass.

When the batch halts, write the stop into `factory/reports/batches/<batch_id>/stop-<date>.md`.

---

## 5 · Batch reporting cadence

The batch produces three artefacts the user reads at well-defined points:

- **At sequence-lock (end of phase 2):** the prioritised sequence + the cluster-saturation note. One paragraph.
- **At distinctness summary (end of phase 3):** GO / RESPEC / DELAY per template + matrix scores. Half a page.
- **At batch close (end of phase 8):** the per-template SHIP / HOLD outcome + the regression-watch surface added to the published catalog. One page.

Between artefacts, status pings are minimal — every template's individual report tree is the durable record. The batch artefacts are the routing-and-aggregation layer.

---

## 6 · Common batch failure modes and the corrective

### Failure mode A · "We did six templates and they all look like the cluster's house style."

The phase-3 distinctness gating was relaxed. The "must not repeat" list was treated as advisory. Each subsequent sibling inherited not just the prior siblings' bans but the prior siblings' biases.

**Corrective:** re-fill the matrix for the most recent six templates. The ones scoring ≤ 4/5 against any sibling are workflow B candidates (issue class II). Run them through edit passes before opening a new batch in the same cluster.

### Failure mode B · "The pack curator picked the same hero photo for two templates."

The phase-5 grep was not re-run between in-flight packs. Discipline broke.

**Corrective:** the second pack swaps the duplicate URL. The grep becomes mandatory between EVERY pack-commit, not just at phase entry.

### Failure mode C · "The AR walk failed on two different templates with the same chrome bug."

A Class I chrome issue surfaced as a Class II/III on multiple templates. Each fix attempt was scoped to the template, not the chrome.

**Corrective:** stop the batch's phase 7. Open a workflow A on the chrome. Re-walk every affected template after the chrome lands.

### Failure mode D · "Six templates queued at release decision and the user signed all six in one sitting."

The handshake-fatigue threshold was breached. Some templates received less attention than they would have alone.

**Corrective:** structure release-decision passes at three-per-session maximum. The fourth template waits for the next session.

### Failure mode E · "We promoted three templates to `published_live` in one batch and one of them regressed within a week."

The regression-watch surface grew faster than the team's bandwidth to monitor it. The batch shipped at the speed of building, not the speed of supporting.

**Corrective:** stagger LIVE flips. Three flips per week is a soft ceiling until the regression-watch tooling is more mature than today's manual `BROWSER_QUALITY_GATE.md §7` cadence.

---

## 7 · Closing reminder

The batch workflow exists to make the user's "hundreds of templates" goal reachable, not to dilute the per-template quality bar. Every gate from the single-template prompts is preserved here; the batch only adds inter-template coordination on top. If a batch starts feeling fast because gates are being skipped, it is failing — even if the velocity feels good in the moment. The Solaria precedent stands at the batch level too: missing a gate cost more time than running it would have.
