# Skill usage policy

The vendored design-intelligence skills (`design-orchestrator/skills/`) and the harness-level skills (`SkillUI`, `design`, `design-system`, `ui-styling`, etc.) are powerful but undisciplined sources of design recommendations. This policy prevents three failure modes:

1. **Skill sprawl** — running every command on every template, producing volumes of advice and very few shipped templates.
2. **Skill-as-standard** — citing a skill's recommendation as if it bound the team, when only `factory/standards/*.md` binds.
3. **Stylistic drift** — different templates pulling in different skills' aesthetic biases until the catalog loses its house identity.

The rule throughout: **skills inform · standards bind**.

---

## 1 · Core now · optional later

| Skill | Status | Where it lives | Used by |
|---|---|---|---|
| **Impeccable** | **Core now** | `design-orchestrator/skills/impeccable/` | Pre-build shape · post-build polish/critique/audit · surgical lifts |
| **taste-skill** (default sub-skill) | **Core now** (light use) | `design-orchestrator/skills/taste-skill/` | Pre-build premium tone reference · anti-slop framing |
| **ui-ux-pro-max** | **Core now** (lookup only) | `design-orchestrator/skills/ui-ux-pro-max/` | Pre-build palette / typography / pattern lookup |
| **frontend-design** (Anthropic skill) | **Optional later** | Harness-level | If/when a clean-slate component build needs scaffolding |
| **design** / **design-system** (harness skills) | **Optional later** | Harness-level | Brand identity, slide decks, mockup generation — not template work |
| **ui-styling** | **Optional later** | Harness-level | shadcn/Tailwind component work — out of scope for current Bootstrap+SCSS stack |
| **banner-design** / **slides** / **brand** | **Out of scope** | Harness-level | Adjacent design work, not the template factory |
| **SkillUI** (and similar broad-surface skills) | **Optional later** | Harness-level | Only when a specific gap appears that the three core skills do not cover |
| **taste-skill alternates** (gpt-taste, soft, minimalist, brutalist, etc.) | **Optional later** | `design-orchestrator/skills/taste-skill/skills/` | Specific archetype lookups (e.g. minimalist for editorial-grid; soft for wellness) |

The policy is intentionally narrow today. Adding a skill to "core now" is a decision recorded in `NEXT_STEPS.md`, not an in-pass improvisation.

---

## 2 · The decision tree · which skill, when

### Pre-build · I need to shape the design direction

```
Is there a clear cluster invariant + sibling triangulation already?
  yes → /impeccable shape (structure-then-build)
        + ui-ux-pro-max search for typography pairing
        + taste-skill (default) for premium tone reference
  no  → first fill DISTINCTNESS_RULES.md §3 cluster invariant for this cluster
        then re-enter the tree
```

### Pre-build · I need a palette direction

```
ui-ux-pro-max: search domain=color, query="<cluster> <tone> palette"
  → returns candidate palettes
  → cross-check against sibling adjacency (DISTINCTNESS_RULES §1, axis 2)
  → pick the most differentiated viable option
```

### Pre-build · I need a typography pairing

```
ui-ux-pro-max: search domain=typography, query="<cluster> <tone>"
  → returns Google-Fonts-grounded pairings
  → for AR-RTL: cross-check that an Arabic-capable family is included or that a swap rule exists
```

### Pre-build · I need to pick an art-direction baseline

```
Cluster tone:
  institutional/professional → taste-skill (default) + minimalist for editorial moments
  warm/sensorial             → soft-skill + selective taste-skill
  editorial-grid portfolio   → minimalist-skill + selective taste-skill
  cinematic photography      → taste-skill + image-to-code as reference frame
  experimental / brutalist   → out of scope for current catalog (cluster invariants forbid)
```

### During-build · the standards do not resolve a micro-decision

```
Reach for the narrowest Impeccable command for that micro-decision:
  motion behaviour       → /impeccable animate (advisory)
  micro-interaction copy → /impeccable clarify
  edge-case handling     → /impeccable harden
  empty-state framing    → /impeccable onboard
```

Default: pause the build and re-engage the planner. Do not invent during build.

### Post-build · I need to verify and polish

```
1. /impeccable critique  → hierarchy / clarity / emotional-resonance review
2. /impeccable audit     → a11y / performance / responsive technical review
3. /impeccable polish    → final pass + design-system alignment
```

Then surgical lifts only if a specific dimension is weak. **Never run the full surface.**

### Post-build · the template feels generic

```
First check Impeccable's anti-pattern detector on the live page (impeccable detect)
Then identify the dimension:
  bland / underdesigned    → /impeccable bolder
  over-decorated / loud    → /impeccable quieter
  weak typography          → /impeccable typeset
  poor visual rhythm       → /impeccable layout
  timid color application  → /impeccable colorize  (advisory only · CS-PAL-* binds)
  joyless                  → /impeccable delight   (cluster permitting)
```

### Post-build · the template feels like another sibling

This is a `DISTINCTNESS_RULES.md` problem, not a skill problem. Re-run the matrix in `DISTINCTNESS_RULES §2`. Skills cannot fix collisions; replan can.

### Multilingual rollout · per-locale design tweaks

Pro Max only · for typography pairings per locale (e.g. Noto Kufi h1 swap for AR). Translations are not a design problem; do not load Impeccable on a translation pass.

---

## 3 · Hard rules across all skills

1. **Standards bind. Skills inform.** When a skill's recommendation conflicts with `factory/standards/<cluster>-design-standard.md`, the standard wins. The recommendation is rejected with a one-line note in the report.
2. **Cite by rule ID, not skill output.** A finding such as "`/impeccable audit` flagged hero contrast" must be re-expressed as "`CS-HERO-03` violation, evidence: ..." in the agent report. The standard is the language; the skill is the detector.
3. **One pre-build pass · one post-build pass.** Not three of each. The three workflows in `TEMPLATE_FACTORY_MODEL.md` allocate one pre-build pass (in plan) and one post-build pass (between critique and walk).
4. **Pexels-only is non-negotiable.** No skill recommendation can override the imagery standard. If a skill recommends a non-Pexels source visualisation, that part of its recommendation is silently dropped.
5. **No skill replaces the browser walk.** Impeccable's audit is excellent and does not substitute for `BROWSER_QUALITY_GATE.md`.
6. **Skills are loaded per pass, not per template.** Reach for a skill when a specific decision needs it. Do not preload the full skill surface and walk the catalogue.
7. **Stylistic alignment trumps stylistic novelty.** When a skill suggests an aesthetic move that would diverge from the cluster's invariant, the move is rejected even if it would score higher on a generic taste meter.

---

## 4 · How `SkillUI` and adjacent harness skills fit

The harness exposes broader surfaces (`design`, `design-system`, `ui-styling`, `banner-design`, `slides`, `brand`, `frontend-design`, `mcp-server-dev:*`, `code-review:*`, `taste-skill`, `ui-ux-pro-max`, etc.). They are present and usable. The orchestrator's stance:

- **`ui-ux-pro-max`** at the harness level === the same skill vendored under `design-orchestrator/skills/`. Use either; outputs are equivalent.
- **`taste-skill`** at the harness level === same.
- **`design`** / **`design-system`** at the harness level — useful for **brand identity work** (logos, CIP, slide decks, mockup-stage explorations). Out of scope for template-factory work; the templates are not the brand of the marketplace, they are products of it.
- **`ui-styling`** — shadcn/Tailwind oriented. The catalog is Bootstrap + SCSS. Not used today.
- **`banner-design`**, **`slides`**, **`brand`** — adjacent marketing/asset work. May be relevant for marketplace-side assets later; not for templates.
- **`frontend-design`** (Anthropic skill) — generic frontend scaffolding. Optional later if a clean-slate component needs initial shaping outside the template factory.
- **`code-review:*`** — engineering review skill, used for engineering passes (apps/* changes), not template-factory passes.
- **`mcp-server-dev:*`** — orthogonal to template factory entirely.

When in doubt, default to the three core-now skills. Reach to harness-level skills only when a specific named gap exists.

---

## 5 · Skill usage in agent reports

When an agent invokes a skill during its phase, the report records:

```
Skill used:        /impeccable critique
Phase invoked:     post-build (workflow A.6)
Decisions taken:   <bulleted, with rule IDs from the standard>
Decisions deferred: <bulleted, with rationale>
Recommendations rejected: <bulleted, with one-line "conflicts with X" rationale>
```

This makes skill use auditable. Future passes can see which skill genuinely produced binding decisions and which produced noise. After ~10 passes the data should let the orchestrator prune the policy further.

---

## 6 · Failure mode · "the model already knows"

A common LLM-side failure is the agent skipping the skill load and reasoning from training-data design instincts. This produces the predictable AI-slop set Impeccable was created to fight: Inter font, purple gradients, cards-in-cards, gray-on-colored-bg. Two correctives:

1. The orchestrator routing **names the skill explicitly** in the agent prompt ("call `/impeccable shape` first, then proceed"). Implicit reaches do not happen.
2. After the agent returns, the orchestrator **diff-checks the output against the AI-slop list** (manually or via the Impeccable detector on the rendered page). Any tell shipped is a workflow B candidate.
