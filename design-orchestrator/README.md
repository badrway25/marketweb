# design-orchestrator

**What this folder is:** the lightweight coordination layer that keeps premium template production aligned as the catalog scales from ~20 templates today toward hundreds. It is the *operational* answer to the question "how do we keep producing Solaria-grade templates without sliding back into one-author-does-everything mode?"

**What this folder is NOT:**
- Not a replacement for `factory/standards/*.md`. Those are the rule books. This folder routes work to them.
- Not a new application. No `apps/*` code is touched here.
- Not a process-heavy program. Nine short docs · zero pipelines · zero new infra.
- Not a VoltAgent migration plan. VoltAgent is referenced as a future direction (see `NEXT_STEPS.md`), not the current source of truth.

**Audience:** the human orchestrator (Badr today) and any agent session that participates in producing a template. Every file here is meant to be opened *during* a real production pass, not read once and forgotten.

---

## Why this exists right now

The editor enrollment program (A.6 → A.17b) closed 2026-04-20 with all 19 archetypes editable. The factory layer caught up under Phase X.4a and proved itself in the X.4 Solaria controlled re-entry. We are now at the inflection point where the next bottleneck is not "can we land a template" but "can we land *N* templates that are clearly different from each other, premium, and browser-verified — without the quality bar drifting?"

Two failure modes are equally dangerous:
1. **Quality drift** — back to single-author Solaria-class shipping. The factory standards already prevent this on corporate-suite. The orchestrator's job is to make that prevention apply uniformly to every cluster.
2. **Process drift** — slipping into a meta-process spiral where we write more documents than templates. The anti-drift section in `ORCHESTRATOR.md` is the explicit guardrail.

This folder sits between the standards (the *what*) and the agents (the *who*) and answers the *when, in what order, with what skill*.

---

## How the layers fit together

```
factory/standards/*.md          ← invariants: design, imagery, browser rubric, scorecard, blocking
       ↑ enforces
factory/agents/*.md             ← 10 narrow-mission agent stubs (planner → gatekeeper)
       ↑ executes
design-orchestrator/*.md        ← THIS LAYER: routing, skill choice, quality gates, anti-drift
       ↑ uses
design-orchestrator/skills/     ← vendored design-intelligence: impeccable, taste-skill, ui-ux-pro-max
```

The standards say what premium means. The agents say who does what. This layer says when to call which agent, when to reach for which skill, and when to refuse to ship. The skills are inputs, never the source of truth.

---

## File map

| File | When you open it |
|---|---|
| `README.md` | First read. Layer overview and the rule for what NOT to put here. |
| `ORCHESTRATOR.md` | Whenever you are about to coordinate a template pass. Defines orchestrator vs agent responsibilities, plus the **anti-drift section** "What this system must never become". |
| `TEMPLATE_FACTORY_MODEL.md` | When planning a new template, an edit pass, or a multilingual rollout. Contains the three canonical workflows. |
| `DISTINCTNESS_RULES.md` | Before a sibling lands. Enforces clear differentiation across templates inside a cluster. |
| `DESIGN_SYSTEM_WORKFLOW.md` | When you need to know *when* to apply Impeccable / Taste / Pro Max in the design lifecycle (pre-build · during · post-build). |
| `BROWSER_QUALITY_GATE.md` | Before any flip from `draft` to `published_live`. The ship gate. |
| `AGENT_ROSTER.md` | When choosing which agent runs next. Pointer index over `factory/agents/*.md` plus the orchestrator's own remit. |
| `SKILL_USAGE_POLICY.md` | When you have a design problem and are unsure which of Impeccable / Taste / Pro Max / SkillUI to reach for. |
| `NEXT_STEPS.md` | After this read. Adoption order, first 3 actions, what waits. |

---

## Skills already on disk (vendored)

These live under `design-orchestrator/skills/` and are usable today.

| Skill | Source | Used for |
|---|---|---|
| **impeccable** | 1 skill / 23 commands · `/impeccable {shape, audit, critique, polish, …}` | Pre-build shape, post-build polish/audit/critique, surgical lifts (`bolder`, `quieter`, `typeset`, `layout`, `colorize`, `delight`). The most heavily-used skill in this layer. |
| **taste-skill** | Multiple sub-skills (taste, soft, minimalist, redesign, image-to-code) | Premium reference framing, anti-slop guidance, image-first priming. Used as a *taste reference* before code, not as the rule book. |
| **ui-ux-pro-max** | BM25 search over 161 reasoning rules · 67 styles · palettes · font pairings · UX guidelines | Lookup tool. "What font pairing for editorial-grid?" "Which palettes work for clinical?" Read-only domain knowledge. |

`SkillUI` and adjacent environment-level skills (`design`, `design-system`, `ui-styling`, `banner-design`, `slides`, `brand`) are available in the harness and are documented in `SKILL_USAGE_POLICY.md`. They are **secondary** to the three vendored above and to `factory/standards/`.

---

## What this folder must never duplicate

Do not copy content from `factory/standards/*.md` here. Reference by path. The standards are versioned and enforced by the factory agents; if this folder restates them, the two will drift.

Do not copy content from `factory/agents/*.md` here. `AGENT_ROSTER.md` is a pointer index, not a redefinition.

Do not copy skill documentation here. The skills' own READMEs and SKILL.md files in `design-orchestrator/skills/*/` are the source of truth for how each skill works internally. `SKILL_USAGE_POLICY.md` only answers *when to reach for which skill*, not *how the skill operates*.

---

## Reading order on first adoption

1. `README.md` (this file)
2. `ORCHESTRATOR.md` — read all of it, including the anti-drift section
3. `TEMPLATE_FACTORY_MODEL.md` — focus on the three canonical workflows
4. `SKILL_USAGE_POLICY.md` — internalize the when-to-use table
5. `BROWSER_QUALITY_GATE.md` — short, ship-critical
6. `DISTINCTNESS_RULES.md`, `DESIGN_SYSTEM_WORKFLOW.md`, `AGENT_ROSTER.md` — reference on demand
7. `NEXT_STEPS.md` — pick the first three actions

Total reading time on first adoption: ~30 minutes.
