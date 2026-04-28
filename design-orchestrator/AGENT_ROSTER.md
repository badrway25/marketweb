# Agent roster

The 10 factory agents are defined in `factory/agents/*.md`. This file is a **pointer index** at orchestrator altitude — it does not redefine those agents, and it adds one role the factory does not contain: the orchestrator itself.

For every agent below, the prompt-file content (mission · inputs · outputs · standard report schema) lives in `factory/agents/<slug>.md`. The orchestrator role lives only in `design-orchestrator/`.

---

## 1 · The 11 roles

| # | Role | File / location | Phase | What the orchestrator routes to it |
|---|---|---|---|---|
| 0 | **Orchestrator** | `design-orchestrator/ORCHESTRATOR.md` (this folder) | All | Brief intake · routing · gates · evidence aggregation. Does not author. |
| 1 | **Template Planner** | `factory/agents/template-planner.md` | Pre-code | Cluster · voice anchor · palette spec · sibling triangulation · imagery direction · scope. |
| 2 | **Imagery Curator** | `factory/agents/imagery-curator.md` | Pre-code | Pexels-only pack · 6-slot pool selection · per-URL metadata. No copy. |
| 3 | **Copy / Translation Agent** | `factory/agents/copy-translation-agent.md` | Pre-code (IT) · post-build (EN/FR/ES/AR) | IT copy from voice anchor · translations with anchor preserved verbatim. No palette / skin edits. |
| 4 | **Template Builder** | `factory/agents/template-builder.md` | Build | Wire content + imagery + palette into skin · DNA · seeds · locale trees. CLI green. No content invention. |
| 5 | **Style Critic** | `factory/agents/style-critic.md` | Critique (parallel) | Tone · typography · rhythm · density · CTA hierarchy · no-template-showcase against design standard. |
| 6 | **Contrast & Accessibility Auditor** | `factory/agents/contrast-accessibility-auditor.md` | Critique (parallel) | CS-PAL-01/04 · CS-HERO-03 · focus-visible · reduced-motion on live DOM. |
| 7 | **Responsive Auditor** | `factory/agents/responsive-auditor.md` | Critique (parallel) | Viewport matrix via Playwright MCP · no-horizontal-scroll · breakpoint behaviour · touch targets · RTL parity. |
| 8 | **Browser Verifier** | `factory/agents/browser-verifier.md` | Ship gate | The full Playwright MCP walk per the cluster's browser rubric. The verdict every other agent cites. |
| 9 | **Template Editor / Fixer** | `factory/agents/template-editor-fixer.md` | Rework | Narrowest-possible-diff fixes on FAIL/BORDERLINE verdicts. Re-runs CI + rebuild for next walk. |
| 10 | **Release Gatekeeper** | `factory/agents/release-gatekeeper.md` | Gate (final) | Aggregate rubric verdict + per-dimension sub-scorecards into the cluster scorecard · drive user-handshake · flip or block. |

---

## 2 · Hard boundaries (recap from `SOP §2.1`)

These prevent the Solaria-class "author-reviews-their-own-palette" failure mode. Listed here so the orchestrator can refuse a routing that violates them:

- **Planner does NOT author copy.** It hands voice-anchor + palette + imagery direction downstream.
- **Imagery-curator does NOT author copy or edit the skin.** Only the pack + pool selection.
- **Copy/translation does NOT touch palette or skin.** Only locale trees.
- **Builder does NOT invent content.** It wires what came upstream.
- **Style-critic / contrast-auditor / responsive-auditor do NOT edit the template.** They report; fixer edits.
- **Browser-verifier does NOT edit either.** It only verifies.
- **Editor-fixer does NOT widen scope.** Diagnosed surface only.
- **Gatekeeper does NOT re-do upstream work.** It aggregates evidence and applies layer logic.
- **Orchestrator does NOT author anything.** It routes, gates, aggregates.

A routing that asks any agent to do work outside its remit is rejected by the orchestrator and re-split into the correct two routings.

---

## 3 · The orchestrator role · what is in `design-orchestrator/`, what is not

| Concern | Where it lives |
|---|---|
| Orchestrator responsibilities | `ORCHESTRATOR.md` |
| What the orchestrator must never become | `ORCHESTRATOR.md §6` |
| Three canonical workflows | `TEMPLATE_FACTORY_MODEL.md` |
| Distinctness gate | `DISTINCTNESS_RULES.md` |
| Browser ship gate | `BROWSER_QUALITY_GATE.md` |
| Pre/during/post-build design passes | `DESIGN_SYSTEM_WORKFLOW.md` |
| Skill choice | `SKILL_USAGE_POLICY.md` |
| The 10 agents themselves | `factory/agents/*.md` (pointer above) |
| The standards each agent reads | `factory/standards/*.md` |

The orchestrator role is intentionally not given a `factory/agents/orchestrator.md` stub today. The role is currently a human, and elevating it into a stub before the manual loop has stabilised would be premature.

---

## 4 · Future agents · explicitly out of scope today

Documented here only so they are not improvised under pressure:

- **Distinctness auditor** — would automate the matrix in `DISTINCTNESS_RULES.md §2`. Today the planner produces it; auditor formalisation waits until ≥6 siblings per cluster make manual checks error-prone.
- **Per-cluster planner specialists** — the single template-planner is sufficient for the present catalog size. Specialists earn a separate file when a cluster's planning shape diverges materially (likely at ecommerce or portfolio scale).
- **Live regression watcher** — would run a periodic re-walk against published templates. Today this is manual (workflow B triggered on report).
- **Localisation specialist** — copy-translation-agent covers locales today. A specialist may emerge when AR or other RTL languages need terminology-deep translation passes.
- **Performance auditor** — currently folded into Impeccable's `audit` command + manual Lighthouse spot-checks. A dedicated agent waits until performance regressions become recurrent.

Each future agent is a candidate for `factory/agents/` only when the manual loop has produced ≥3 instances where its absence demonstrably caused a slowdown or a defect.
