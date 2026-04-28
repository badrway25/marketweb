# ORCHESTRATOR

This document defines what the *orchestrator role* is responsible for, what the *individual agents* are responsible for, and the bright line between the two. It also encodes the anti-drift rules that keep this system from collapsing into a documentation-heavy program with weak visual output.

---

## 1 · What the orchestrator is

**Today the orchestrator is a human role: Badr, working through Claude Code sessions.** The role exists whether or not anyone calls it that. This document makes the responsibilities of the role explicit so they can be discharged consistently and, eventually, partially automated.

The orchestrator is the **routing, gating, and aggregation** layer. It does not *do the work*. It decides who does the work, in what order, against which standard, and refuses to flip a template that has not cleared the ship gate.

The orchestrator's three core questions on every pass:
1. **What** is being produced (cluster · archetype · scope · locales)?
2. **Who** is producing each piece (which factory agent · which skill assists each agent)?
3. **What evidence** does each piece need to produce so the next agent can act, and so the gatekeeper can aggregate at the end?

If those three are answered before the first line of code is written, the pass will not slide into Solaria-mode.

---

## 2 · Orchestrator responsibilities

The orchestrator owns:

| Responsibility | What it looks like in practice |
|---|---|
| **Brief intake** | Receive a request ("add restaurant template X" / "fix Solaria EN distinctness" / "roll Vertex to AR"). Translate into archetype · cluster · scope · locales · D-102 commit posture. |
| **Routing** | Decide which factory agent runs next. Decide which skill (Impeccable / Taste / Pro Max / SkillUI) the agent reaches for. Refuse routes that skip the planner or the browser-verifier. |
| **Standard selection** | Point each agent at the canonical standard for the cluster (e.g. corporate-suite agents read `factory/standards/corporate-suite-*.md`; future clusters get their own standards before enrollment). |
| **Distinctness gate** | Before a sibling lands, run the `DISTINCTNESS_RULES.md` checklist against all existing siblings in the cluster. Block draft-landing if a triangulation collision is detected. |
| **Browser gate** | Block any flip from `draft` to `published_live` until the browser-verifier verdict and the multi-locale walk evidence are on file. See `BROWSER_QUALITY_GATE.md`. |
| **Pexels gate** | Refuse pack approval and refuse LIVE flip if any non-Pexels imagery URL appears on a new template. Pragma legacy is the only documented exception. |
| **Evidence aggregation** | Hand the release-gatekeeper agent the consolidated evidence pack: planner brief, imagery pack, copy + translation diff, builder CLI summary, style-critic report, contrast report, responsive report, browser rubric verdict. |
| **Anti-drift enforcement** | Periodically check that this layer is not growing prose faster than templates. See §6. |

The orchestrator does **not** own:
- Authoring copy, palettes, imagery, skin code, or translations.
- Running the browser walk personally (the browser-verifier agent does · see `BROWSER_QUALITY_GATE.md`).
- Writing scorecards from scratch (the gatekeeper aggregates against `factory/standards/corporate-suite-quality-scorecard.md`).
- Inventing new design rules at run time. New rules go into `factory/standards/*.md` *before* a pass uses them.

---

## 3 · Orchestrator vs agent · the bright line

| Concern | Orchestrator | Agents |
|---|---|---|
| Decides *what is built* | Yes (scope, archetype, locales) | No |
| Decides *who builds it* | Yes (routing) | No |
| *Builds it* | No | Yes (per their narrow remit in `factory/agents/*.md`) |
| Decides *what passes* | Aggregates · escalates · refuses | Each agent passes/fails its own dimension only |
| Authorizes flip to LIVE | Drives the user-handshake; refuses on missing evidence | Gatekeeper agent prepares the verdict; orchestrator carries the request to the user |
| Edits a standard | Proposes changes between passes | Never edits standards mid-pass |
| Writes a memory | Yes, when a pass closes | No |

Every confusion about "who decides X?" should be resolved by checking this table. If a row does not exist for the question, the answer is: **the standard decides** (look up `factory/standards/`).

---

## 4 · Minimum Viable Orchestrator (MVO) · today

The MVO is what we operate with today. It is deliberately small:

1. **Nine docs in `design-orchestrator/`** (this folder).
2. **One human in the orchestrator role** (Badr).
3. **The 10 factory agents** invoked one Claude Code session per agent, or batched into a single session that explicitly switches voices and emits the standard report schema between phases.
4. **The three canonical workflows** in `TEMPLATE_FACTORY_MODEL.md` are the only routings that exist. Anything else is an exception and must be justified.
5. **Manual evidence aggregation** — the gatekeeper section of the final report is filled in by hand (or by a single Claude session given all upstream reports).
6. **Vendored skills** (Impeccable, Taste, UI UX Pro Max) used as advisory tools, never as standards.

What the MVO explicitly does NOT include:
- No autonomous agent loops.
- No VoltAgent runtime.
- No CI hook that blocks merges based on this layer (the existing test suite + factory agents already do that).
- No cross-cluster generalisation. Today these rules are enforced strictly on corporate-suite (where the standards are written) and applied as best-effort on other clusters until each cluster has its own standards file.

The MVO is sufficient to produce one Solaria-grade template per pass. That is the present bar.

---

## 5 · Full orchestrator · later

The full orchestrator emerges over multiple passes, not in one rewrite. Likely shape:

| Capability | Trigger to graduate from MVO | Probable mechanism |
|---|---|---|
| Per-cluster standards files | When the second cluster needs its own design standard distinct from corporate-suite | `factory/standards/<cluster>-{design,imagery,browser-rubric,scorecard,blocking,multi-agent-sop}.md` |
| Automated brief → agent routing | When ≥3 templates are in flight at once | A small dispatcher script that reads a brief YAML and emits the per-agent prompt files |
| Automated distinctness audit | When sibling count in a cluster crosses ~6 and manual triangulation becomes error-prone | A script that compares palette tokens, voice anchor, hero shape, motion profile across siblings and flags collisions |
| Automated browser walk evidence pack | When ≥1 multilingual rollout per week | Playwright MCP scripted walk per locale with the rubric checklist mechanically encoded |
| VoltAgent or equivalent runtime | When manual session-orchestration becomes the bottleneck (not before) | TypeScript runtime under `design-orchestrator/runtime/` driving the factory agents · still bound by the standards |

None of these are in scope today. Each is added only when the manual MVO has become demonstrably the slowest step, not on speculation.

---

## 6 · What this system must never become

This is the explicit anti-drift section. It is short on purpose.

1. **It must never become more prose than templates.** If the document count in `design-orchestrator/` grows in a pass while the catalog template count or quality does not, the pass was a process pass, not a product pass. Two consecutive process passes is a signal that the orchestrator role is being misused.
2. **It must never duplicate `factory/standards/*.md`.** Standards are the rule book. This layer routes work to them. Duplication causes drift, drift causes regressions, regressions caused Solaria.
3. **It must never replace browser-live verification with rubrics-on-paper.** Every `[BLOCKING]` rule in `factory/standards/` exists because a green CLI is a lower bound, not a ship signal. The orchestrator refuses any flip lacking a live walk verdict — see `BROWSER_QUALITY_GATE.md`.
4. **It must never authorize a single-author template.** If one session authored copy *and* imagery *and* palette *and* skin *and* its own review, the result is a Solaria-class candidate by construction. The orchestrator splits the work or refuses to ship.
5. **It must never invent a new design rule mid-pass.** New rules go into `factory/standards/` between passes, with rationale. Mid-pass invention skips the review of the rule itself.
6. **It must never weaken the Pexels-only policy on new templates.** Pragma legacy is the only documented exception; no second exception is granted without an explicit user-signed waiver.
7. **It must never expand the skill surface beyond the three vendored skills + the standards-bound agents** without an explicit decision in `NEXT_STEPS.md`. New skills are a vector for stylistic drift; the existing surface is already broader than what we use on a typical pass.
8. **It must never substitute autonomy for accountability.** Even when steps later become automated (§5), the user-handshake at LIVE flip remains. Automation must produce evidence the user can read in under five minutes; otherwise it's drift.
9. **It must never become a VoltAgent migration.** VoltAgent is referenced as a possible future runtime. Treating "let's port to VoltAgent" as the orchestrator's purpose is a meta-process trap.
10. **It must never silence the user's original goal.** That goal is restated in §7 below. If a pass closes without measurable progress against it, the pass was misallocated regardless of how clean its reports were.

If you cannot tell whether a proposed change violates one of these ten, default to no.

---

## 7 · The user's original goal · restated

The orchestrator exists to serve this, not the reverse:

> Hundreds of customizable templates · all clearly different from each other · premium · elegant · modern · professional · dynamic · browser-live verified · scalable without quality loss.

Every routing decision, every gate, every doc in this folder is justified iff it makes that goal more likely. Anything that doesn't, gets cut.

---

## 8 · Operating cadence

A typical pass is:

1. **Intake** (orchestrator) — ~5 min. Brief → archetype · cluster · scope · locales.
2. **Plan** (template-planner agent) — ~30 min. Output: voice anchor, palette spec, sibling triangulation, imagery direction.
3. **Pack** (imagery-curator agent) — ~30-60 min. Output: Pexels-only pack with metadata.
4. **Copy** (copy-translation agent) — IT first then locales. Output: locale trees with anchor verbatim.
5. **Build** (template-builder agent) — wire content + skin + previews. Output: CLI green set.
6. **Critique** (style-critic + contrast-accessibility + responsive auditors in parallel) — DOM-based reviews.
7. **Browser walk** (browser-verifier agent) — the ship gate. Multi-locale, RTL included for AR.
8. **Fix** (template-editor-fixer agent) — only if critique or walk failed. Narrowest possible diff.
9. **Aggregate** (release-gatekeeper agent + orchestrator) — scorecard, user-handshake, flip or hold.

Each step ends with a report. The orchestrator does not start the next step until the previous report is on file.
