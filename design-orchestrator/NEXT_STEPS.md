# Next steps

This is the action plan that turns the rest of the folder from prose into a working orchestrator. It is intentionally short — three concrete actions to take next, in order; everything else is deferred until the manual loop has stabilised.

---

## 0 · State as of 2026-04-29

- Corporate-suite reference pack and distinctness matrix: **on file** (`design-orchestrator/references/internal-baselines/`).
- First orchestrator dry run: **complete** (`design-orchestrator/dry-runs/candidate-01-*` · target `continua-stewardship` · 4th corporate-suite · family-office variant).
- Dry-run hardening pass: **complete** (this commit) · five micro-gates added at intake / A.2 / A.2.5 (`workflows/pre-build-quick-checks.md`):
  1. Cluster reference-pack availability precondition
  2. Sibling palette warmth/coolness conflict warning
  3. Imagery feasibility quick-search (pre-A.3)
  4. Content-volume estimate
  5. "Remove the studio name" pre-test (intake AND brief §10)
- **Ready for: the first real corporate-suite build.** Likely candidate: `continua-stewardship` (the dry-run target was already vetted on paper).
- **NOT ready for**: real builds in any other cluster (medical-specialist, restaurant, portfolio, ecommerce, real-estate, law, agency, startup-saas, medical-other) — those clusters do not have reference packs or distinctness matrices on file. Intake §0.5 HALTS those builds until their packs exist.

---

## 1 · Adoption order

1. **Read the folder once** — `README.md` → `ORCHESTRATOR.md` (including §6 anti-drift) → `TEMPLATE_FACTORY_MODEL.md` → `SKILL_USAGE_POLICY.md` → `BROWSER_QUALITY_GATE.md` → `DISTINCTNESS_RULES.md` + `DESIGN_SYSTEM_WORKFLOW.md` + `AGENT_ROSTER.md` + `workflows/pre-build-quick-checks.md` on demand. ~35 min total.
2. **Run the first real corporate-suite build** — likely `continua-stewardship` (the dry-run candidate). Use `prompts/template-orchestrator-master.md` end-to-end · clear all five pre-build quick-checks at intake · do not skip A.2.5.
3. **Capture the friction** — at the end of that pass, write a one-paragraph note: which step felt redundant, which felt missing, which of the five new pre-build checks caught (or failed to catch) a defect that would otherwise have shipped. That note is the input to the next revision of this folder.
4. **Revise once · then run the next pass** — refine the docs based on real friction, not speculative friction. Two passes between revisions is the cadence; revising every pass is process-spiral.
5. **Defer everything else** — see §3 below.

**Cluster expansion rule**: before the second cluster (medical-specialist · restaurant · etc.) gets its first real template build, run a one-off pass that produces that cluster's `reference-pack.md` and `distinctness-matrix.md` (same shape as the corporate-suite pair). The first real build in that cluster does not start before its pack lands. This is enforced by intake §0.5 HALT.

---

## 2 · The first three concrete actions

### Action 1 · Run the next template pass through `TEMPLATE_FACTORY_MODEL.md` workflow A end-to-end

- Pick the next corporate-suite enrollee or the next Solaria sub-pass.
- Open `TEMPLATE_FACTORY_MODEL.md §3` and follow it literally.
- Do not skip the pre-build shape pass (`DESIGN_SYSTEM_WORKFLOW.md §2`).
- Do not skip the distinctness matrix (`DISTINCTNESS_RULES.md §2`).
- Do not skip the user-handshake (`BROWSER_QUALITY_GATE.md §6`).
- At the end, write the friction note (above).

This is the action that proves the layer works. Without it, everything else is theoretical.

### Action 2 · Write the per-cluster reference sheet for corporate-suite

A short page (≤1 screen) that pre-loads, for the corporate-suite cluster:
- The cluster invariant (cribbed from `DISTINCTNESS_RULES.md §3`).
- Three Pro Max search queries that consistently return useful palette / typography / pattern results for this cluster.
- Three Impeccable commands that are most worth running on this cluster (by past usefulness).
- The three sibling templates new entrants triangulate against by default.

Filed under `design-orchestrator/cluster-sheets/corporate-suite.md`. The same file format will later be replicated for medical, restaurant, portfolio, etc. — but only after each cluster has had ≥3 passes through this layer.

### Action 3 · Add a single-line entry to `AGENT_HANDOFF.md` pointing at this folder

`AGENT_HANDOFF.md` is the cross-session anchor. One line — "**Design coordination layer**: see `design-orchestrator/README.md`. Use `TEMPLATE_FACTORY_MODEL.md` for the three canonical workflows; `BROWSER_QUALITY_GATE.md` for ship gate." — is enough. The folder is then discoverable by every future Claude Code session without anyone having to remember to open it.

---

## 3 · What waits until later

Each of these is a real, visible improvement. None is in scope today. Each waits for the trigger noted.

| Deferred work | Trigger to start |
|---|---|
| **Per-cluster standards files** under `factory/standards/<cluster>-{design,imagery,...}.md` | When the second cluster needs distinct standards from corporate-suite (likely medical-specialist or restaurant). |
| **Per-cluster reference sheets** under `design-orchestrator/cluster-sheets/` | When corporate-suite has had ≥3 passes through this layer (Action 2 above gives us cluster-sheet #1; the next two reuse the format). |
| **Automated brief → agent routing** (small dispatcher script) | When ≥3 templates are in flight at once — manual routing becomes the bottleneck around then. |
| **Automated distinctness matrix** | When sibling count in any cluster crosses ~6 (we are already there for corporate-suite if Solaria counts; consider this trigger met when the next collision is missed manually). |
| **Live regression watcher** (periodic re-walks against published templates) | When ≥1 LIVE regression slips through that a periodic walk would have caught. |
| **VoltAgent or equivalent runtime** | When manual session-orchestration is demonstrably the bottleneck — not before. The `my-voltagent-app/` folder on disk is exploration · not adoption. |
| **CI hook tying this layer to merges** | Never, unless a strong case is made. The factory agents and existing test suite already gate merges; adding another gate creates ceremony without preventing more defects. |
| **Dedicated orchestrator agent file** under `factory/agents/orchestrator.md` | When the human orchestrator role has stabilised across ≥10 passes and the routings become mechanical enough to encode. |
| **Performance auditor agent** | When performance regressions become recurrent. Currently folded into Impeccable `audit`. |
| **Localisation specialist agent** | When AR (or another RTL language) develops terminology depth that the copy-translation agent can no longer cover in a single pass. |
| **Skill expansion** beyond Impeccable / taste-skill / Pro Max | Only with a recorded decision in this file under §4 below. Skills are a vector for stylistic drift. |

---

## 4 · Decisions log (additive · append-only)

Each entry: date · decision · rationale.

- **2026-04-29 · five pre-build quick-checks codified** in `workflows/pre-build-quick-checks.md` and wired into intake checklist (§0.5 / §3.1 / §3.2 / §6.5 / §7.1) · master prompt (A.1 / A.2 / A.2.5 / §6 cluster note / §4 stop conditions 11-12) · single-template-workflow (§2 pre-build gates · §4 stop points 6-8) · batch-template-workflow (phase 1 cluster precondition · phase 5 feasibility re-confirm) · skill-usage-policy (pre-build A.2.5 note). Rationale: first dry run on `continua-stewardship` exposed five concrete weaknesses that would have shown up at A.7 walk if not gated upstream. Cost: ~15 min orchestrator time at intake. Closes: cross-cluster pack drift · hex-distinct-temp-identical palettes · Pexels-thin imagery directions · sparse/wall/skewed content rhythms · brand-name-leaning differentiation.

---

## 5 · The single sentence that prevents drift

If a proposed change to this folder does not make the user's original goal more likely (hundreds of customizable templates · all clearly different · premium · browser-live verified · scalable without quality loss), it does not belong here.
