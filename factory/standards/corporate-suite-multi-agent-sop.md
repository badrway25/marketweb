# Corporate-suite Multi-Agent Standard Operating Procedure

**Phase**: X.4a · Corporate-suite Factory Hardening · **Date**: 2026-04-22
**Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Scope**: factory files only · no `apps/editor`, `apps/projects`, `apps/commerce` changes · no new archetypes · Solaria Commit B remains paused per binding user instruction.
**Inputs**:
- `factory/reports/audits/corporate-suite-audit-master.md`
- `factory/standards/corporate-suite-design-standard.md`
- `factory/standards/corporate-suite-imagery-standard.md`
- `factory/standards/corporate-suite-browser-rubric.md`
- `factory/standards/corporate-suite-quality-scorecard.md`
- `factory/standards/corporate-suite-blocking-rules.md`
- `factory/references/pattern-library.md`, `factory/references/anti-pattern-library.md`, `factory/references/template-inventory.md`
**Audience**: every Claude Code agent (and every human reviewer acting as one) that participates in producing a corporate-suite template — from planning through draft-landing (Commit A) through LIVE flip (Commit B). This file is the canonical answer to the questions **"who does what, in what order, with what evidence, and who signs what?"**

This SOP is the operational layer. The design standard says **what** premium means. The imagery standard says **what** imagery qualifies. The browser rubric says **how** to verify. The scorecard says **how** to score. The blocking-rules say **what is not allowed to ship**. This document says **how the work is split across agents so that no single template ever again ships a Solaria-class defect because one person tried to do everything in one pass.**

---

## 0 · How to use this document

1. **The SOP is prescriptive, not advisory.** Every production run on this archetype follows this flow. Deviations must be logged under `§ deviation` in the release-gatekeeper's final report, with a written justification.
2. **Agent names are 1:1 with file stubs** under `factory/agents/`. When this SOP refers to an agent, it refers to a concrete prompt file that will be populated in a follow-up step — the SOP is what those prompt files will encode as the agent's mission.
3. **No single agent signs off the whole template.** Each agent has a narrow remit (§2) and a narrow deliverable (§3). The release-gatekeeper is the only agent allowed to merge multiple dimensions into a final verdict, and it does so by aggregation, not by re-doing the work.
4. **Every agent report uses the §6 standard schema.** Uniform reports make aggregation mechanical and make automation straightforward.
5. **Browser verification is the ship gate, not a nice-to-have.** The browser-verifier agent runs last among the observation agents, and its rubric verdict is the single source of truth every downstream scoring agent cites.
6. **Pexels-only is non-negotiable** for new pilots. The imagery-curator agent enforces it at pack time; the browser-verifier agent re-verifies it on the live render; the release-gatekeeper refuses the flip if any non-Pexels URL appears on a new template (Pragma legacy exception tracked separately).
7. **When in doubt, escalate or block.** The cost of a false pass is a shipped Solaria-class defect; the cost of a false block is one extra walk. Asymmetry favors blocking.

---

## 1 · Operating premise · why this SOP exists

### 1.1 · The single-template one-by-one anti-pattern

Pre-factory, corporate-suite templates were produced by one author doing all the work — palette selection, copy authoring, imagery sourcing, skin integration, preview regeneration, and manual review — then handed straight to the user. Solaria's `e8f38b5` commit is the canonical outcome: 1148 lines of content shipped, 506/506 tests passed, `generate_previews` succeeded, and every `h1..h5` on every page rendered cream-on-cream. The defect was caught by a 30-minute browser walk, not by any of the ~650 automated checks.

This SOP exists to prevent that class of failure at scale. It does so by:

- **Splitting the work across 10 agents** with narrow, non-overlapping responsibilities, so no one agent can simultaneously author the palette and verify the palette's contrast against the headline color.
- **Placing the browser verification agent downstream of the build agents** and giving its verdict binding force over the other agents' deliverables.
- **Making the release-gatekeeper a pure aggregator** of evidence produced upstream, not an all-in-one author-reviewer.
- **Requiring a standard report schema** so aggregation is mechanical and auditable rather than narrative and negotiable.

### 1.2 · What "scalable template production without lowering quality" means

Scalability here is NOT "produce more templates per week." It is "produce each template through a pipeline where every invariant is enforced by a specialist, the evidence is captured, and the final verdict is defensible to a second reviewer who wasn't in the room." The pipeline must hold as Wave 3 / Wave 4 pilots land and as the backlog of retro-fits (Pragma Pexels repack, responsive breakpoint pass) closes.

### 1.3 · Alignment with the D-102 two-commit cadence

- **Commit A · draft-landing**: the template lands on the integration branch with `TEMPLATE_REGISTRY.json` at `draft`. Commit A clears when the PR introduces zero `[BLOCKING]` defects under `corporate-suite-blocking-rules.md`.
- **Commit B · LIVE flip**: the template flips to `published_live`. Commit B clears when the full rubric walk PASSes, the scorecard clears Layer 1 / 2 / 3, and the user parallel-verification handshake completes.

The SOP handoffs in §4 below are built around this split.

---

## 2 · Agent roster · 10 agents · narrow missions

Every agent below maps to a stub file at `factory/agents/<slug>.md`. Missions are deliberately narrow so boundaries are clear and so no agent re-does another agent's work.

| # | Agent | Stub file | One-line mission | Upstream or downstream |
|:-:|---|---|---|---|
| 1 | **Template Planner** | `template-planner.md` | Turn a pilot brief into a buildable plan — cluster, voice anchor, palette spec, sibling D-054 triangulation, imagery direction, scope of locales. | Upstream (pre-code) |
| 2 | **Imagery Curator** | `imagery-curator.md` | Produce the Pexels pack + 6-slot pool selection · subject, mood, and license audit · no copy authoring. | Upstream (pre-code) |
| 3 | **Copy/Translation Agent** | `copy-translation-agent.md` | Author IT copy against the curated pack and voice anchor · translate to EN/FR/ES/AR with anchor verbatim · no palette or skin edits. | Upstream (pre-code) |
| 4 | **Template Builder** | `template-builder.md` | Wire content + imagery + palette into `preview_imagery.py`, `template_dna.py`, `seed_templates.py`, locale trees · run the CLI green set · no content invention. | Build |
| 5 | **Style Critic** | `style-critic.md` | Review the rendered DOM against design-standard §1-§12 — tone, typography, rhythm, density, CTA hierarchy, no-template-showcase — on the live server. | Downstream (observation) |
| 6 | **Contrast & Accessibility Agent** | `contrast-accessibility-auditor.md` | Enforce CS-PAL-01 / CS-PAL-04 / CS-HERO-03 / focus-visible / reduced-motion — measured on the live DOM. | Downstream (observation) |
| 7 | **Responsive Auditor** | `responsive-auditor.md` | Drive the §5 viewport matrix via Playwright MCP · no-horizontal-scroll · breakpoint behavior · touch targets · RTL parity. | Downstream (observation) |
| 8 | **Browser Verification Agent** | `browser-verifier.md` | Run the full Playwright MCP walk per `corporate-suite-browser-rubric.md` · produce the rubric verdict that every other observation agent cites. | Downstream (ship gate) |
| 9 | **Template Editor/Fixer** | `template-editor-fixer.md` | Apply remediation edits on FAIL or BORDERLINE verdicts · narrowest possible diff · re-run CI + rebuild for the next walk. | Rework |
| 10 | **Release Gatekeeper** | `release-gatekeeper.md` | Aggregate the rubric verdict + per-dimension sub-scorecards into the `corporate-suite-quality-scorecard.md` final scorecard · apply Layer 1 / 2 / 3 logic · drive the user parallel-verification handshake · act on the verdict (flip or block). | Gate (final) |

### 2.1 · Hard boundaries between roles

These are not suggestions. They prevent the Solaria-class "author-reviews-their-own-palette" failure mode.

- **Planner does NOT author copy.** The planner hands the voice anchor, palette spec, imagery direction and D-054 triangulation to downstream agents. It does not write the IT copy itself.
- **Imagery Curator does NOT author copy or edit the skin.** The curator's only deliverable is a reviewer-approved pack + a 6-slot pool selection, with caption/role/coherence metadata per URL.
- **Copy/Translation Agent does NOT pick imagery or palette.** It works against a pack and a palette that are already reviewer-approved.
- **Template Builder does NOT invent content.** It wires what the Planner/Curator/Copy agents produced. If the builder spots a missing field, it escalates back, not fills-in.
- **Style Critic, Contrast Agent, Responsive Auditor, Browser Verifier do NOT edit code.** They observe, measure, and report. If a fix is needed, they hand off to the Template Editor/Fixer.
- **Template Editor/Fixer does NOT judge its own fix.** After editing it re-runs the relevant observation agents via a fresh walk; the Editor/Fixer itself cannot sign off.
- **Release Gatekeeper does NOT re-do observation work or re-measure evidence.** It aggregates what the observation agents produced and applies the §4/§5/§6 logic in the scorecard. Its judgment is confined to `[STRONG]` deviations (with written justification) and escalations to the user.

### 2.2 · Who owns which scorecard dimensions

Maps the agents above to the 15 quality-scorecard dimensions (`corporate-suite-quality-scorecard.md` §3). The **release-gatekeeper reads and totals; it does not score.**

| Scorecard dimension | Primary agent | Secondary / cross-check |
|---|---|---|
| D1 · Premium feel | Style Critic | Browser Verifier (evidence), Imagery Curator (rendered pool) |
| D2 · Elegance | Style Critic | — |
| D3 · Modern professionalism | Style Critic + Copy/Translation Agent | Contrast & Accessibility Agent (focus / motion) |
| D4 · Hero readability | Contrast & Accessibility Agent | Responsive Auditor (viewport shape), Style Critic (composition) |
| D5 · Navbar quality | Style Critic | Contrast & Accessibility Agent (focus, AA), Responsive Auditor (collapse) |
| D6 · Footer quality | Style Critic | Copy/Translation Agent (legal links per cluster), Responsive Auditor (stack) |
| D7 · Typography hierarchy | Style Critic | Copy/Translation Agent (italic `<em>` discipline across locales) |
| D8 · Spacing rhythm | Style Critic | Responsive Auditor (padding at breakpoints) |
| D9 · Imagery quality | Imagery Curator | Browser Verifier (rendered resolution) |
| D10 · Imagery coherence | Imagery Curator | Browser Verifier (3-second check on live DOM), Copy/Translation Agent (anchor-to-pack alignment) |
| D11 · Pexels-only compliance | Imagery Curator | Template Builder (seed wiring), Browser Verifier (live src audit) |
| D12 · Contrast safety | Contrast & Accessibility Agent | Browser Verifier (evidence) |
| D13 · Responsive quality | Responsive Auditor | Browser Verifier (viewport coverage proof) |
| D14 · Browser live verification quality | Browser Verifier | Release Gatekeeper (evidence completeness gate) |
| D15 · Text/image coherence | Copy/Translation Agent + Imagery Curator | Style Critic (anchor-imagery read) |

---

## 3 · Per-agent inputs, outputs, and tools

Every agent's contract below is **what it reads, what it must produce, and which tools are allowed**. No freeform outputs; every deliverable lands in a well-known path and uses the §6 report schema.

### 3.1 · Template Planner

- **Mission**: produce the pilot brief that every downstream agent works against. One pilot = one brief.
- **Required inputs**:
  - Cluster blueprint (`docs/content-factory/cluster_blueprints/<cluster>.md`).
  - Sibling template modules on this archetype (Pragma + Fiscus + Solaria today) for D-054 triangulation.
  - `corporate-suite-design-standard.md` §1 (premium/elegant/modern/professional criteria) + §4 (palette) + §12 (executive).
  - `factory/references/pattern-library.md` and `factory/references/anti-pattern-library.md`.
- **Required outputs** (all placed under `factory/reports/plans/<template-slug>/`):
  1. `brief.md` — cluster + voice anchor + palette spec (dark primary L\* ≤ 40 vs cream · secondary + accent as D-054 vector) + imagery direction + scope of locales + page-by-page section plan.
  2. `d-054-triangulation.md` — 10-gate differentiation of the new pilot against EVERY sibling (Pragma, Fiscus, Solaria), not just one. Required by CS-EXEC-02 / CS-BLOCK-12.
  3. `open-questions.md` — any clarifications the user must resolve before downstream agents start.
- **Tool surface**: Read, Grep, Glob, WebSearch (for verifying public credentials vocabulary per cluster). NO file writes outside `factory/reports/plans/`. NO edits to `apps/*`.
- **Handoff signal**: `brief.md` labeled `Status: APPROVED (user)` on its frontmatter. Without user sign-off the Curator and Copy agents do not start.
- **Boundaries**: does not author copy; does not select URLs; does not edit the skin.

### 3.2 · Imagery Curator

- **Mission**: deliver a reviewer-approved Pexels pack + 6-slot pool selection that will survive the browser walk's 3-second semantic check.
- **Required inputs**:
  - `brief.md` (voice anchor, imagery direction, cluster).
  - `corporate-suite-imagery-standard.md` in full (especially §1 Pexels-only, §2 6-slot pool, §3 coherence rules, §13 stock-look diagnostic).
  - `docs/content-factory/imagery/CURATION_PROTOCOL.md` and `docs/content-factory/imagery/blacklist.md`.
  - The other corporate-suite pools (`business-corporate`, `business-fiscal`, `business-coaching`) for cross-cluster dedup (CS-IMG-SRC-04).
- **Required outputs**:
  1. `docs/content-factory/imagery/packs/<cluster>.md` — 20-40 candidate URLs, each with photographer + pexels-id + resolution + 1-line semantic caption + slot role + coherence justification (CS-IMG-COH-06).
  2. `factory/reports/imagery/<template-slug>/pool-selection.md` — the 6-slot selection keyed by role, with URLs + license proof + dedup grep result.
  3. `factory/reports/imagery/<template-slug>/curator-report.md` (uses §6 report schema) — summary of the audit: 3-second check results per URL, mood-to-anchor read per URL, cross-cluster dedup result, Pexels-only confirmation.
- **Tool surface**: Read, Grep, Glob, WebFetch (to open Pexels URLs), Write (pack + reports only). MUST NOT touch `apps/catalog/preview_imagery.py` directly — the Template Builder wires the pool from the pack.
- **Pexels-only enforcement**: every URL must hit `images.pexels.com`. The curator's report explicitly runs `grep -E 'unsplash|shutterstock|getty|adobestock'` against its own pack and reports `0 matches` or the agent blocks itself. This is the first enforcement layer of CS-BLOCK-07.
- **Reviewer ≠ curator** (CS-IMG-SRC-05): a second pass by a peer reviewer (another run of the Curator agent with `role: reviewer`) must sign off the pack before Copy starts.
- **Boundaries**: does not author copy; does not pick the palette; does not edit the skin or `preview_imagery.py`.

### 3.3 · Copy/Translation Agent

- **Mission**: author the IT copy against the pack + brief, and translate to EN/FR/ES/AR with the voice anchor preserved verbatim.
- **Required inputs**:
  - `brief.md` + `d-054-triangulation.md` from the Planner.
  - `pool-selection.md` + `curator-report.md` from the Imagery Curator.
  - Cluster blueprint §4 (terminology dictionary) and §5 (voice anchor).
  - `corporate-suite-design-standard.md` §12 (executive / corporate premium feel), §13 (no-template-marketplace rules), §9 (density), §10 (CTA hierarchy).
- **Required outputs**:
  1. `apps/catalog/template_content_<name>.py` (IT-primary) — with the D-054 10-gate block in the module docstring enumerating ALL sibling diffs (CS-BLOCK-12).
  2. Four locale files: `template_content_<name>_{en,fr,es,ar}.py` — voice anchor translated faithfully, terminology dictionary respected.
  3. `factory/reports/copy/<template-slug>/copy-report.md` (§6 schema) — voice anchor presence per locale, banned-phrase grep results (CS-EXEC-04), credential vocabulary audit, D-054 triangulation check.
- **Tool surface**: Read, Grep, Glob, Edit/Write under `apps/catalog/template_content_<name>*.py` only. NO edits to templates, skin, palettes, or imagery wiring.
- **Boundaries**: does not pick or change images; does not edit the palette; does not touch the skin.

### 3.4 · Template Builder

- **Mission**: wire content + imagery + palette into the repo so that `manage.py check`, `manage.py test apps.catalog`, `manage.py test apps`, `scripts/check_imagery_pack.py`, and `generate_previews` all run green.
- **Required inputs**:
  - `brief.md` (palette spec, page plan).
  - `pool-selection.md` (the 6 URLs to write into `preview_imagery.py`).
  - `template_content_<name>*.py` (already authored by Copy).
  - `corporate-suite-design-standard.md` §4 (palette token rules, CS-PAL-01..06).
  - `corporate-suite-blocking-rules.md` §3 (the 18 hard blockers).
- **Required outputs**:
  1. Edits to `apps/catalog/preview_imagery.py` (new pool keyed `business-<kind>`, CS-IMG-POOL-01 shape).
  2. Edits to `apps/catalog/template_dna.py` (new DNA row) and `apps/catalog/management/commands/seed_templates.py` (palette row) respecting the dark-primary rule.
  3. Edits to `apps/catalog/TEMPLATE_REGISTRY.json` at `draft` tier (Commit A).
  4. Locale tree + static asset registration as needed.
  5. `factory/reports/build/<template-slug>/build-report.md` (§6 schema) — CI-green evidence: `manage.py check` 0 issues · `manage.py test apps.catalog` pass · `manage.py test apps` pass · `scripts/check_imagery_pack.py` pass · `generate_previews` pass · palette-dark-check scripted grep.
- **Tool surface**: Read, Grep, Edit/Write on `apps/catalog/*` (limited to the files above), Bash (CI runs), Write for the build report.
- **Palette polarity self-check** (CS-BLOCK-01 first defense): the builder computes L\* of `primary` vs the cream paper token and refuses to advance the template past `draft` if L\* > 40. Output: `build-report.md` line `primary L*: <value> · PASS/FAIL`.
- **Boundaries**: does not author or rewrite content; does not pick imagery; does not edit the shared skin (`_base.html` + page files) — skin edits belong to a separate hardening pass. Does not flip the registry to `published_live` — that is the Release Gatekeeper's call.

### 3.5 · Style Critic

- **Mission**: observe the rendered DOM against `corporate-suite-design-standard.md` §1–§12, and produce a sub-scorecard for the dimensions listed in §2.2.
- **Required inputs**:
  - The live dev server URL + port (provided by the Browser Verifier at walk-start).
  - The rubric's captured evidence directory (`factory/reports/browser-verification/<slug>/<run-timestamp>/`).
  - `corporate-suite-design-standard.md` + §16 DO/DON'T + §18 rule index.
- **Required outputs**:
  1. `factory/reports/critic/<template-slug>/<run-timestamp>/style-critic-report.md` (§6 schema).
  2. Per-dimension scores for D1 (Premium feel), D2 (Elegance), D3 (Modern professionalism — shared with Copy/Translation), D5 (Navbar), D6 (Footer), D7 (Typography), D8 (Spacing rhythm).
  3. Flagged anti-pattern hits keyed by AP-number (AP4 / AP5 / AP9 / AP10 / AP11 as applicable).
- **Tool surface**: Read (evidence dir), Grep (content files), and MCP browser tools for spot-checks only (`mcp__plugin_playwright_playwright__browser_snapshot`, `browser_evaluate`). No code edits.
- **Boundaries**: does not run the full rubric matrix (that is the Browser Verifier's job); does not score contrast, responsive, or imagery dimensions (those agents own them).

### 3.6 · Contrast & Accessibility Agent

- **Mission**: enforce the contrast invariants (CS-PAL-01, CS-PAL-04, CS-HERO-03), focus-visible discipline (CS-NAV-02 / E1), and reduced-motion honoring (CS-RESPONSIVE-07 / E2) on the live DOM.
- **Required inputs**:
  - Dev server URL + port.
  - Rubric evidence directory (especially `measurements.json` keyed by BRWS-CONTRAST-01..04).
  - `corporate-suite-browser-rubric.md` §6.1 and §6.8.
  - `corporate-suite-quality-scorecard.md` D4 and D12 rubrics.
- **Required outputs**:
  1. `factory/reports/contrast/<template-slug>/<run-timestamp>/contrast-report.md` (§6 schema) with:
     - RGB distance and WCAG ratio for every `h1..h5` on every page × every locale.
     - Same measurements for every text descendant of `.cs-section.dark`, `.cs-kpi-band`, `.cs-nav`, `.cs-foot`.
     - Keyboard Tab-walk results for `:focus-visible` outline color/offset on the first ~12 focusables per page.
     - Reduced-motion emulation result (entrance animations suppressed).
  2. Scores for D4 (Hero readability) and D12 (Contrast safety).
- **Tool surface**: `mcp__plugin_playwright_playwright__browser_evaluate`, `browser_press_key`, `browser_take_screenshot`. No code edits.
- **Hard veto**: any `h1..h5` with distance < 120 OR WCAG < 4.5 = automatic **FAIL · Override O1** in the final scorecard; the agent states that explicitly in its report so the gatekeeper short-circuits correctly.

### 3.7 · Responsive Auditor

- **Mission**: drive the full viewport matrix (1920 / 1440 / 1280 / 1024 / 768 / 640 / 414 / 390 per `corporate-suite-browser-rubric.md` §5) and enforce CS-RESPONSIVE-01..08.
- **Required inputs**:
  - Dev server URL + port.
  - `corporate-suite-browser-rubric.md` §5 + §6.8 + §10.2.
  - `corporate-suite-quality-scorecard.md` D13 rubric.
- **Required outputs**:
  1. `factory/reports/responsive/<template-slug>/<run-timestamp>/responsive-report.md` (§6 schema) with:
     - Per-viewport `scrollWidth` vs `clientWidth` on every page × every locale (BRWS-VIEW-02).
     - Hero `grid-template-columns` at 1920 / 1440 / 1280 / 390 (BRWS-HERO-01 / VIEW-03).
     - Nav collapse state at 1024 / 768 / 414 (BRWS-VIEW-04).
     - Contact form stack at ≤ 880 (BRWS-VIEW-05).
     - Hero h1 `font-size` at 390 (BRWS-VIEW-06).
     - Touch-target dimensions at 390 (BRWS-VIEW-07).
     - RTL parity at 1440 / 768 / 390 (BRWS-RESP-07).
  2. Score for D13 (Responsive quality).
- **Tool surface**: `mcp__plugin_playwright_playwright__browser_resize`, `browser_evaluate`, `browser_take_screenshot`. No code edits.
- **Hard veto**: any horizontal scrollbar at any matrix viewport = **FAIL · Override O2**; hero not stacking or nav not collapsing at ≤ 720 = **FAIL · Override O3**.

### 3.8 · Browser Verification Agent

- **Mission**: run the full `corporate-suite-browser-rubric.md` walk end to end via Playwright MCP, capture evidence, and produce the `verdict.md` that every other observation agent cites.
- **Required inputs**:
  - Successful Template Builder `build-report.md` (CI green + palette self-check PASS) — the walk never runs on a template that has not passed the CI floor (CS-BROWSER-03).
  - `corporate-suite-browser-rubric.md` in full (the operational script).
  - `corporate-suite-blocking-rules.md` §3 (the 18 hard blockers to cross-check against).
- **Required outputs** (per rubric §7 / §11):
  1. Evidence directory `factory/reports/browser-verification/<template-slug>/<run-timestamp>/`:
     - `verdict.md` using the rubric §11 template exactly.
     - `walk-log.md` opening with `Server: http://127.0.0.1:<port>/ · Started at: <ISO-8601>` and every MCP call chronologically.
     - `screenshots/<locale>/<page>/<WIDTHxHEIGHT>.png` · at least 120 PNGs (5 locales × 6 pages × 4 core viewports).
     - `measurements.json` keyed by rubric tag (`BRWS-CONTRAST-01`, `BRWS-VIEW-02`, …).
     - `console.log` per page.
  2. Score for D14 (Browser live verification quality).
- **Tool surface**: **Playwright MCP required** — the full `mcp__plugin_playwright_playwright__*` surface (or the documented `mcp__claude-in-chrome__*` equivalent per BRWS-TOOL-01). No code edits.
- **Mandatory preconditions** (walk refuses to start if any is missing):
  1. Dev server running on a deterministic port; URL + port recorded in `walk-log.md` top line.
  2. Test suite green on the branch (`manage.py test apps` + `manage.py test apps.catalog`).
  3. `scripts/check_imagery_pack.py` green.
  4. Evidence directory created with `screenshots/` subtree.
  5. Playwright MCP session open.
- **Mandatory post-conditions**:
  1. `verdict.md` written with one of PASS / BORDERLINE / FAIL.
  2. Server left running (BRWS-SRV-04) so the user can parallel-verify.
  3. No in-place edits to the evidence directory after the verdict is written (BRWS-EVID-06).
- **Hard veto**: missing URL + port in the verdict = **FAIL · Override O13**; missing any matrix viewport = **FAIL · Override O14**; incomplete evidence directory = **FAIL · Override O15**; no walk performed at all = **FAIL · Override O18**.

### 3.9 · Template Editor/Fixer

- **Mission**: apply the narrowest possible remediation edit(s) when a walk returns FAIL or BORDERLINE, so a fresh walk can re-verify.
- **Required inputs**:
  - Previous walk `verdict.md` — the list of blocking/required failures with evidence anchors.
  - The quality scorecard's remediation block (if written).
  - All upstream artifacts (brief, pack, copy, build report) for context.
- **Required outputs**:
  1. Minimal diff to `apps/catalog/*` OR to the content modules (NOT to the shared skin unless the failing rule is explicitly an archetype-wide invariant and the fix is authorized by the user). For this phase, editor-fixer does NOT touch `apps/editor`, `apps/projects`, `apps/commerce`, or `templates/live_templates/business/corporate-suite/*` files; archetype-wide skin hardening is a separate step.
  2. `factory/reports/fix/<template-slug>/<run-timestamp>/fix-report.md` (§6 schema) — each change mapped to the blocking/required item it resolves, with a re-run of the CI floor.
- **Tool surface**: Read, Grep, Edit/Write on `apps/catalog/*` and the content modules only, Bash (CI verification).
- **Hard boundaries**:
  - Fixer **never signs off its own fix.** It triggers a new walk at a fresh `<run-timestamp>` before the Release Gatekeeper can re-score.
  - Fixer **never patches a prior verdict in place** (BRWS-EVID-06).
  - Fixer **never bypasses CI** — the fix must clear the CI floor before the Browser Verifier picks it up.
  - Fixer **does NOT continue Solaria Commit B** — Solaria's EN/FR/ES/AR authoring remains paused per binding user instruction.

### 3.10 · Release Gatekeeper

- **Mission**: aggregate the upstream evidence + sub-scorecards into the final `corporate-suite-quality-scorecard.md` artifact, apply Layer 1 / 2 / 3 logic, drive the user parallel-verification handshake, and act on the verdict (flip `TEMPLATE_REGISTRY.json` or block).
- **Required inputs**:
  - Browser Verifier's `verdict.md` and full evidence directory.
  - Style Critic, Contrast Agent, Responsive Auditor, Imagery Curator, Copy/Translation Agent sub-scorecard reports.
  - `corporate-suite-quality-scorecard.md` §4 (overrides) + §5 (critical floors) + §6 (aggregate).
  - `corporate-suite-blocking-rules.md` §19 (merge-vs-follow-up decision matrix).
- **Required outputs**:
  1. `factory/reports/quality-scorecards/<template-slug>/<run-timestamp>-scorecard.md` (per scorecard §7 template).
  2. User parallel-verification handshake block with the live server URL + port.
  3. On PASS: a Commit B diff flipping `TEMPLATE_REGISTRY.json` for this slug from `draft` to `published_live`, waiting on user confirmation of parallel verification.
  4. On BORDERLINE / FAIL: a remediation punch-list keyed by override ID or dimension ID, handed to the Template Editor/Fixer for a new branch pass.
- **Tool surface**: Read, Write (scorecard), Grep, very narrow Edit on `TEMPLATE_REGISTRY.json` for Commit B only, after user confirmation. No rework of observation evidence.
- **Hard boundaries**:
  - Gatekeeper **never grants `[BLOCKING]` waivers unilaterally.** Waivers go to the user.
  - Gatekeeper **never re-measures evidence.** It cites what the observation agents produced.
  - Gatekeeper **never edits a prior scorecard.** A new walk produces a new scorecard at a fresh `<run-timestamp>`.
  - Gatekeeper **never flips LIVE without the user parallel-verification handshake** — the user opens the live URL in their own browser and confirms before the registry flip.

---

## 4 · Handoff order · the end-to-end pipeline

The pipeline is linear with two gated merge points (Commit A and Commit B). Each arrow below is a handoff; the receiving agent does not start until the sending agent's deliverable exists at its named path and the gate signal is present.

### 4.1 · Pipeline diagram

```
        ┌───────────────────────────────────────────────────┐
        │                  Commit A pre-work                │
        ├───────────────────────────────────────────────────┤
 [1] Template Planner
       │   brief.md · d-054-triangulation.md
       │   (user approves brief)
       ▼
 [2] Imagery Curator  ──(pack)──►  Imagery Curator (reviewer pass)
       │   packs/<cluster>.md · pool-selection.md · curator-report.md
       ▼
 [3] Copy / Translation Agent
       │   template_content_<name>*.py · copy-report.md
       ▼
 [4] Template Builder  ──(CI floor)──►  build-report.md  (palette L* ≤ 40)
       │
       ├─── Gate 1 · Commit A landing ───────────────────────
       │    PR opens; draft-tier in TEMPLATE_REGISTRY.json.
       │    merge allowed when no [BLOCKING] defect is introduced by this diff.
       │
        ┌───────────────────────────────────────────────────┐
        │               Commit B pre-flip work              │
        ├───────────────────────────────────────────────────┤
 [5] Browser Verification Agent  (starts the dev server · records URL + port)
       │   full Playwright MCP walk · evidence dir · verdict.md
       ▼
 [6] Observation agents, in parallel against the rubric evidence:
       │   ├── Style Critic           → style-critic-report.md
       │   ├── Contrast & Accessibility → contrast-report.md
       │   ├── Responsive Auditor      → responsive-report.md
       │   ├── Imagery Curator (re-read against live DOM) → imagery-live-report.md
       │   └── Copy/Translation Agent (anchor audit across 5 locales) → copy-live-audit.md
       ▼
 [7] Release Gatekeeper (aggregation)
       │   corporate-suite quality scorecard · Layer 1 / 2 / 3 verdict
       │
       ├── verdict FAIL or BORDERLINE ──►  [8] Template Editor/Fixer
       │                                     │  minimal diff · re-run CI
       │                                     ▼
       │                                  back to [5] fresh timestamp walk
       │
       └── verdict PASS ─────────────────►  [9] User parallel-verification handshake
                                              │  (open live URL in user's browser)
                                              ▼
                                            Commit B: flip TEMPLATE_REGISTRY.json
                                            from draft → published_live
```

### 4.2 · Gate signals (what a receiving agent looks for)

| Handoff | Receiving agent requires | Where to find it |
|---|---|---|
| Planner → Curator | `brief.md` with `Status: APPROVED (user)` | `factory/reports/plans/<slug>/brief.md` |
| Curator → Copy | `curator-report.md` + `pool-selection.md` with `Reviewer: LGTM` line | `factory/reports/imagery/<slug>/` |
| Copy → Builder | All 5 locale files present + `copy-report.md` with `Voice anchor: verbatim 5/5` | `apps/catalog/template_content_<name>*.py` + `factory/reports/copy/<slug>/` |
| Builder → Verifier | `build-report.md` with `CI: PASS · palette L*: <= 40 · PASS` | `factory/reports/build/<slug>/build-report.md` |
| Verifier → observers | `verdict.md` with PASS or BORDERLINE or FAIL (never missing) + evidence dir complete | `factory/reports/browser-verification/<slug>/<run-timestamp>/` |
| Observers → Gatekeeper | All 5 per-dimension sub-reports present | `factory/reports/{critic,contrast,responsive,imagery,copy}/<slug>/<run-timestamp>/` |
| Gatekeeper → User | Scorecard with `Verdict: PASS` + live server URL + port | `factory/reports/quality-scorecards/<slug>/<run-timestamp>-scorecard.md` |
| Gatekeeper → Editor/Fixer | Scorecard with `Verdict: BORDERLINE` or `FAIL` + remediation punch-list | same path |
| Editor/Fixer → Verifier | `fix-report.md` with CI green + explicit `Addresses: O<n>, D<m>` mapping | `factory/reports/fix/<slug>/<run-timestamp>/fix-report.md` |

### 4.3 · Parallelism rules

- **Pre-Commit-A (steps 1-4)**: mostly sequential. The Planner must finish before Curator. Curator's pack must be reviewer-approved before Copy starts. Copy must finish before Builder.
- **Post-Commit-A observation (step 6)**: **the five observation agents run in parallel** against the same rubric evidence. Parallelism is safe because they observe, not edit. This is where the SOP earns its scalability — five narrow specialists working from the same screenshots.
- **Rework loop (steps 8 → 5)**: always sequential. A fix requires a fresh walk at a fresh timestamp; you cannot parallelize a fix with its own verification.

### 4.4 · What the pipeline deliberately forbids

- **No agent starts before its input deliverable is present and tagged.** If Copy starts without a reviewer-approved pack, the Curator's work is implicitly bypassed — this is the single-template-one-by-one anti-pattern returning.
- **No shortcut from Builder straight to Gatekeeper** (skipping the walk). CS-BLOCK-18 / Override O18 makes "test-only ship" an automatic FAIL.
- **No in-place patch to a failing verdict.** Steps 8 → 5 create a fresh `<run-timestamp>` directory each time.
- **No LIVE flip without the user parallel-verification handshake.** The Gatekeeper hands off the live URL; the user confirms; only then the registry flips.

---

## 5 · Escalation rules · rework loop · final gate

### 5.1 · Escalation chain

```
Specialist agent  →  Release Gatekeeper  →  User
                  ↑                       ↑
                  second reviewer         (final call on [BLOCKING] waivers,
                  (peer pass on subjective  archetype-wide skin decisions,
                   checks)                  and any Solaria-class pause lift)
```

- **Specialist agent** (Planner / Curator / Copy / Builder / Style Critic / Contrast / Responsive / Browser Verifier / Editor/Fixer): runs its contract, surfaces defects in its §6 report, proposes a severity tag (`[BLOCKING]` / `[REQUIRED]` / `[STRONG]` / `[GUIDELINE]`).
- **Second reviewer** (another run of the same agent type with `role: reviewer`, or a peer agent):
  - Imagery 3-second subject checks (CS-IMG-COH-01 / BRWS-IMG-03) — subjective → always a second pass.
  - "Reads as a template showcase" style-critic calls (CS-TONE-05 / BRWS-FEEL-01) — subjective → always a second pass.
  - Tiebreak on any `[BLOCKING]` vs `[REQUIRED]` ambiguity the first reviewer flags.
- **Release Gatekeeper**: aggregates; applies scorecard §4/§5/§6; writes the final artifact. Can grant waivers on `[STRONG]` items only, with `§ deviation` justification.
- **User**: final call on any waiver for a `[BLOCKING]` rule · final call on archetype-wide skin fixes that exceed the narrow-diff scope · final call on un-pausing Solaria Commit B (currently paused by binding instruction).

### 5.2 · When to escalate

Escalate when ANY of the following:

1. **Ambiguous severity** — a reviewer cannot decide between `[BLOCKING]` and `[REQUIRED]`. Default to the stricter tag and escalate.
2. **Blocking-rule waiver requested** — any author/agent argues an exception to one of the 18 hard blockers. Only the user may waive.
3. **Detection disputed** — two reviewers disagree on a subjective check (3-second imagery, template-showcase read). Invoke a third reviewer; if still tied, reject (cost asymmetry).
4. **Latent-on-main defect touched by unrelated PR** — e.g., a PR lands near Pragma's legacy Unsplash pool. Do not silently inherit the grandfathered exception; escalate so the Gatekeeper records the contact.
5. **Borderline evidence** — e.g., 1-pixel horizontal scroll at 640px due to scrollbar rendering artifact. Gatekeeper decides; if still ambiguous, reject.
6. **Scope creep** — an agent is asked to edit outside its narrow remit (e.g., Style Critic asked to fix a CSS token). Refuse and escalate to Gatekeeper, which either re-scopes to the Template Editor/Fixer or escalates to the user for archetype-wide work.

### 5.3 · Rework loop (FAIL / BORDERLINE → fresh walk)

The rework loop is the mechanism that prevents "ship and fix later" on this archetype.

1. **Release Gatekeeper writes the scorecard with `Verdict: FAIL` or `Verdict: BORDERLINE`** and a remediation punch-list keyed by override ID (O1-O18) or dimension ID (D1-D15).
2. **Template Editor/Fixer reads the punch-list** and applies the narrowest possible diff. Each change cites the override/dimension it resolves in the commit message and in `fix-report.md`.
3. **CI floor re-runs** (`manage.py check`, `manage.py test apps`, `manage.py test apps.catalog`, `scripts/check_imagery_pack.py`, `generate_previews`). A red CI floor aborts the loop — the fix is wrong.
4. **Browser Verifier runs a fresh walk at a new `<run-timestamp>`**. The old evidence directory is preserved for audit (BRWS-EVID-06); the new one is the source of truth for the next scoring pass.
5. **Observation agents re-run in parallel** against the new walk's evidence.
6. **Release Gatekeeper re-aggregates** and writes a new scorecard (at the new `<run-timestamp>`). If PASS, the final gate proceeds; if not, the loop repeats.

Bounded effort: if the rework loop runs more than **two iterations** without reaching PASS, the Gatekeeper escalates to the user to decide whether the template should be paused (Solaria-class) rather than continue chasing regressions.

### 5.4 · Final gate · user parallel-verification handshake

The final gate is NOT the scorecard. It is the user opening the live server URL in their own browser, walking the same pages the agents walked, and explicitly confirming.

**Operational sequence**:

1. Release Gatekeeper writes the scorecard with `Verdict: PASS` and the block:
   ```
   ## Parallel-verification handshake

   The dev server remains at `http://127.0.0.1:<port>/`.
   User: please open this URL in your own browser and confirm visual parity
   with the walk evidence before the registry flip proceeds.
   ```
2. Browser Verifier keeps the dev server running (BRWS-SRV-04). No shutdowns, no restarts.
3. Agents go idle pending user confirmation. No further tool calls; no proactive re-verification.
4. User opens the live URL, inspects the home page and any locale / viewport they want to spot-check.
5. User types explicit approval in the conversation (e.g., "confirmed · proceed with Commit B"). Only then does the Gatekeeper execute the `TEMPLATE_REGISTRY.json` edit and the Commit B diff.
6. On user approval, the server is released (the Gatekeeper or the Verifier shuts it down with a logged line).

**What the final gate refuses**:

- A scorecard PASS without the handshake block → **block the flip**. No silent flips.
- A handshake without a recorded URL + port → **block the flip** (CS-BLOCK-13 / Override O13).
- A user "looks fine, ship it" message sent BEFORE the Gatekeeper produced a scorecard → **not a flip signal**; the Gatekeeper waits for its own artifact to exist first.
- A partial confirmation ("the IT home looks good, haven't checked others") → **not a flip signal** unless the Gatekeeper re-scopes the walk down or the user explicitly releases the rest.

---

## 6 · Standard report schema · every agent uses this

Uniform reports are what make aggregation mechanical. Every agent deliverable uses the schema below, at the path stated in §3. Agents who produce code (Builder, Editor/Fixer, Copy/Translation) ALSO produce a report of this shape — the code is the artifact, the report is the evidence.

### 6.1 · Required top-matter (YAML-ish, copied verbatim)

```markdown
---
report_type: <planner | curator | copy | build | critic | contrast | responsive | imagery-live | verifier | fix | scorecard>
template_slug: <slug>                       # e.g. solaria-coaching
archetype: corporate-suite
agent: <agent-name>                          # e.g. responsive-auditor
role: <primary | reviewer>                   # reviewer pass uses role: reviewer
run_timestamp: <ISO-8601 basic · YYYYMMDDThhmmssZ>
branch: <branch-name>
baseline_tip: <commit-hash>                  # e.g. 3074b00
inputs:
  - <path to each input artifact or standard consumed>
outputs:
  - <path to each artifact this report anchors>
server_url: <http://127.0.0.1:<port>/ · or "n/a · offline agent">
server_started_at: <ISO-8601 · or "n/a">
verdict: <PASS | BORDERLINE | FAIL | n/a>    # n/a for upstream authoring agents (planner, curator, copy, builder)
status_tag: <APPROVED | LGTM | DRAFT | NEEDS-REWORK | BLOCKED>
---
```

Rules:

- **`server_url` is MANDATORY for every observation agent** (critic, contrast, responsive, verifier, imagery-live, copy-live). A report from an observation agent without `server_url` is rejected.
- **`verdict` must be `n/a` for upstream authoring agents.** Those agents do not produce verdicts; they produce inputs. `status_tag` carries their state.
- **`status_tag: LGTM`** is reserved for reviewer-role passes (Imagery Curator reviewer pass, second-reviewer tiebreaks).

### 6.2 · Required body sections (ordered · every report has all of them)

```markdown
# <report_type> Report · <template-slug> · <agent> · <run_timestamp>

## 1 · Summary (one sentence)

<one-sentence summary: what this agent did and what it produced>

## 2 · Inputs consumed

<bullet list of exact paths read, with a 1-line "what I used it for">

## 3 · Findings

### 3.1 · Blocking

<one block per [BLOCKING] finding, OR "— none —">
- Tag: <CS-BLOCK-NN | O<n> | BRWS-XXX | CS-*>
- Observed: <one-line raw finding, with numbers>
- Evidence: <screenshot path, measurements.json key, grep output, diff anchor>
- Incident anchor: <AP* or "—">
- Proposed severity: [BLOCKING]
- Proposed remediation: <one line>

### 3.2 · Required

<same block shape for [REQUIRED] findings, OR "— none —">

### 3.3 · Strong / Guideline notes

<bulleted list with severity tag per bullet, OR "— none —">

## 4 · Measurements (machine-readable)

<code block with raw numbers, computed styles, counts — the fields the scorecard will cite>
```

(Example fields per agent:)

- **Contrast Agent**: RGB distances, WCAG ratios, focus outline RGB.
- **Responsive Auditor**: `scrollWidth`/`clientWidth` pairs per viewport, hero `grid-template-columns`, h1 `font-size` at 390, touch-target bounding boxes.
- **Imagery Curator**: per-URL photographer + id + resolution + caption + role + coherence + Pexels-host confirm.
- **Template Builder**: CI results, palette L\* value, seed row diff stats.

```markdown
## 5 · Per-dimension scores (observation agents only)

<table rows for the D1-D15 dimensions this agent owns per §2.2; each row cites evidence>

| Dimension | Score (0-5) | Evidence (rubric tag · screenshot · measurement) | Notes |
|---|:-:|---|---|

## 6 · Escalations raised

<list of any ambiguous severity calls, subjective-check tiebreaks requested, or waiver requests — OR "— none —">

## 7 · Parallel-verification handshake (observation agents)

<for agents that touched the live server: restate server URL + port + "still running" state>

## 8 · Next action

<one of:>
- Hand off to <next agent> · path: <deliverable path> · status: <READY | BLOCKED>
- Request rework by <agent> on items: <list>
- Escalate to release-gatekeeper: <reason>
- Escalate to user: <reason>

— end of report —
```

### 6.3 · Aggregation-friendly conventions

- **Tags are uppercase-with-dashes** (`CS-PAL-01`, `BRWS-CONTRAST-01`, `CS-BLOCK-05`, `O7`, `AP4`, `D12`). No prose-only findings.
- **Every finding cites at least one evidence artifact path** (screenshot, measurement key, grep output, diff anchor). A finding without evidence is rejected.
- **No finding spans multiple dimensions** — if a defect implicates D4 AND D12, it is reported twice, once under each dimension's owner, so the Gatekeeper can tally cleanly.
- **Severity proposals are explicit**, not implied. `Proposed severity: [BLOCKING]` — no "I think this is bad" prose.

---

## 7 · Enforcement of non-negotiable constraints

### 7.1 · Browser verification is central

- The Browser Verifier is the **only agent** authorized to produce the rubric verdict that downstream scoring cites.
- Every downstream scoring agent MUST cite the rubric `measurements.json` + `screenshots/` for its evidence. "I eyeballed it" is not a valid citation.
- The release gatekeeper MUST refuse to flip LIVE when the rubric verdict is not PASS.
- No agent may bypass the Browser Verifier by claiming the CLI floor is enough (AP8 · CS-BLOCK-18 · Override O18).

### 7.2 · Playwright MCP required

- The Browser Verifier MUST drive the walk via `mcp__plugin_playwright_playwright__*` (or the documented `mcp__claude-in-chrome__*` equivalent per BRWS-TOOL-01). Headless screenshot scripts outside MCP are not accepted as primary evidence.
- The Contrast Agent, Responsive Auditor, and Style Critic use the same MCP surface for their spot checks, targeting the SAME running dev server the Browser Verifier started. No one starts a second server.
- A manual walk (real Chrome + DevTools) is allowed ONLY with an explicit `§ deviation` note in the verdict explaining why MCP was unavailable, and the evidence bar is unchanged.

### 7.3 · Pexels-only for new pilots

- Imagery Curator's primary pass: every URL is `images.pexels.com`; `grep -E 'unsplash|shutterstock|getty|adobestock'` returns 0 matches; report lists the grep command and its result.
- Imagery Curator's reviewer pass: same grep, independently.
- Template Builder: same grep on the post-wire `preview_imagery.py` block.
- Browser Verifier: on the live render, every rendered `<img>.src` on a new pilot must hit `images.pexels.com` (or be a `/media/` URL sourced from a Pexels pack via the customer-upload path; those are out of scope for new pilots on this archetype).
- Release Gatekeeper: refuses the flip on any non-Pexels URL for a new pilot. Pragma's legacy Unsplash pool is the SINGLE tolerated exception and is explicitly acknowledged in the scorecard's Layer 1 checklist.

### 7.4 · No single agent does everything

- The roster (§2) splits the pipeline into 10 narrow missions with explicit boundaries (§2.1).
- A prompt file under `factory/agents/` must refuse to take on work outside its remit — e.g., the Style Critic prompt must refuse to edit CSS, the Imagery Curator prompt must refuse to author copy.
- The Release Gatekeeper is an aggregator, not a super-agent. Its judgment is confined to `[STRONG]` deviations and to escalations.

### 7.5 · Live server · URL · port · real browser checks

- The Browser Verifier starts the dev server on a deterministic port (BRWS-SRV-01), records the URL in the first line of `walk-log.md` (BRWS-SRV-02), keeps the server running throughout (BRWS-SRV-04), and does not shut it down until the user has confirmed parallel verification (§5.4).
- Every observation agent's report restates the URL + port under `server_url` in top-matter and under §7 `Parallel-verification handshake`.
- The Release Gatekeeper's scorecard carries the same URL + port in its handshake block and refuses to flip without it.
- **"The walk ran" is not a claim without URL + port in the verdict.** Phantom walks are rejected; the template is re-walked.

### 7.6 · Out-of-scope guardrails (do not touch this release)

- **No edits outside `factory/*`** during this hardening phase EXCEPT what a Builder or Copy agent legitimately produces within `apps/catalog/template_content_*.py`, `apps/catalog/preview_imagery.py`, `apps/catalog/template_dna.py`, `apps/catalog/management/commands/seed_templates.py`, `apps/catalog/TEMPLATE_REGISTRY.json`. No agent touches `apps/editor`, `apps/projects`, `apps/commerce`, or the shared skin files (`templates/live_templates/business/corporate-suite/*.html`).
- **No continuation of Solaria Commit B** — Solaria's EN/FR/ES/AR authoring remains paused on branch `phase-x4-wave2-solaria-coaching-v1` at `6b70d56`. The Copy/Translation Agent MUST refuse a task that targets Solaria's non-IT locales until the user explicitly un-pauses. This SOP does not grant that un-pause.
- **No palette-validator code change** this pass — palette L\* check is enforced by the Builder's self-check and by the Browser Verifier's live walk until a pre-commit validator lands in a later hardening step.

---

## 8 · Automation-readiness · how this SOP plugs into future tooling

This SOP is written to be executed today by Claude Code agents invoked manually, AND to serve as the contract for later automation. The following properties make both work:

- **Stable filesystem contracts**: every artifact has a canonical path. Automation scripts can read `factory/reports/browser-verification/<slug>/<latest-run-timestamp>/verdict.md` without discovery logic.
- **Deterministic agent roster**: 10 slugs match 10 prompt files under `factory/agents/`. A dispatcher that reads a pilot brief can fire agents in order, read their reports, and decide the next step.
- **Uniform report schema (§6)**: YAML-ish top-matter + tagged findings + machine-readable measurements make aggregation mechanical. A single script can roll up 5 sub-reports into a scorecard.
- **Tag-based evidence citations**: every finding cites a rule tag (`CS-*`, `BRWS-*`, `CS-BLOCK-*`, `O<n>`, `D<n>`, `AP<n>`). Automation can join findings across reports by tag.
- **Explicit gate signals (§4.2)**: each handoff has a named file, a named `status_tag`, and a named gate. A scheduler can watch for the gate and release the next agent.
- **Fresh-timestamp rework** (§5.3): immutable evidence directories mean automation never needs conflict-resolution; it appends a new timestamp directory.
- **No hidden state**: every decision trail is a file on disk. No agent carries "memory" the next agent cannot reconstruct from artifacts.

---

## 9 · What this SOP deliberately does NOT do

- **Does not replace the design / imagery / rubric / scorecard / blocking standards.** Those define rules. This document defines who applies which rule, when, and how handoffs are recorded.
- **Does not grant any agent the authority to waive a `[BLOCKING]` rule.** Only the user can.
- **Does not expand agent scope beyond `factory/*` plus the narrow `apps/catalog/*` authoring surface listed in §7.6.** Archetype-wide skin hardening (responsive breakpoints, reduced-motion JS, palette validator) remains a separate, explicitly scoped step.
- **Does not un-pause Solaria Commit B.** Solaria's non-IT locales remain paused per binding user instruction until the hardening pass closes.
- **Does not allow the release-gatekeeper to act as a super-reviewer.** Its authority is bounded: aggregate, apply Layer 1/2/3 logic, request user handshake, flip on user approval.
- **Does not assume CLI green is sufficient.** Every flow here treats CI green as a precondition for the browser walk, never as a ship signal.

---

## 10 · Summary

### 10.1 · The workflow in one sentence

> **Planner briefs → Curator packs → Copy authors → Builder wires + CI-greens → Browser Verifier walks and records evidence at a reported URL + port → five observation agents score dimensions in parallel against that evidence → Release Gatekeeper aggregates into the quality scorecard → user confirms parallel verification in their own browser → only then does the registry flip from `draft` to `published_live`.**

### 10.2 · Key gate points (in order)

1. **Planner user-approval gate** — the brief is signed by the user before any code or pack work begins. Prevents Curator and Copy from chasing an unapproved direction.
2. **Curator reviewer-approval gate** — second pass on the Pexels pack before Copy starts. Prevents Session-31-class subject mismatches from flowing downstream.
3. **Builder CI + palette self-check gate** — `manage.py` green + palette L\* ≤ 40 recorded, BEFORE the walk starts. Solaria's `e8f38b5` would have tripped the palette self-check here and never reached the walk.
4. **Browser Verifier evidence gate** — server URL + port recorded · full §5 viewport matrix × 5 locales × 6 pages walked · `verdict.md` written · evidence directory complete. Without this, no downstream scoring is valid.
5. **Release Gatekeeper Layer 1 / 2 / 3 gate** — zero blocking overrides · all 9 CRITICAL dimensions ≥ 4 · all 6 non-critical ≥ 3 · aggregate average ≥ 4.3 · zero `[REQUIRED]` outstanding. Any failure = BORDERLINE or FAIL, not PASS.
6. **User parallel-verification handshake** — user opens the live URL in their own browser and explicitly confirms before the registry flip. No silent flips.

### 10.3 · How this SOP enables scalable template production without lowering quality

- **Specialization beats polymathy.** Ten narrow agents each doing one thing well is more reliable than one agent doing everything in one pass — the exact failure shape Solaria demonstrated.
- **Observation is decoupled from authoring.** The five observation agents (Style Critic, Contrast, Responsive, Browser Verifier, Imagery Curator on the live pass) cannot edit the code they review. They cannot mark their own homework.
- **Evidence is frozen per walk.** Immutable `<run-timestamp>` directories mean a BORDERLINE/FAIL remediation cannot quietly reshape prior evidence; every iteration is auditable.
- **Aggregation is mechanical.** The Release Gatekeeper applies Layer 1 / 2 / 3 scorecard logic to tagged findings — no narrative judgment, no averaging-away of a weak critical dimension.
- **Browser verification has the veto.** CLI green can never be enough; the walk is the ship gate, and Playwright MCP + reported URL + port makes the walk reproducible.
- **Parallel observation = throughput.** Steps 5 → 6 parallelize across five observation agents working from the same evidence dir, so the slowest path is one walk + one aggregation, not five sequential reviews.
- **User parallel-verification is the final human gate.** Quality is not "the agents said PASS"; it is "the user looked at the live render and agreed." The server-still-running discipline (BRWS-SRV-04) preserves that gate as a first-class step.

The SOP does not make producing a template faster in wall-clock terms — it makes each produced template defensibly shippable. Scalability comes from repeatability: every pilot passes through the same 10-agent pipeline, against the same standards, with the same report schema, producing the same audit trail. When Wave 3 and Wave 4 pilots land, they land on rails that already caught a Solaria-class defect before it shipped.

— end of SOP —
