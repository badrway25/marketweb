# Design system workflow

How premium quality is enforced **before** a template is built and **after** it is built. The factory standards (`factory/standards/*.md`) say *what* premium means. This document says *when* during the lifecycle the design-intelligence skills are applied to keep the work above the bar.

---

## 1 · The lifecycle

```
brief → SHAPE → plan → pack → copy → BUILD → critique → walk → POLISH → flip
         ─┬─                          ─┬─                       ─┬─
       (pre-build           (during-build              (post-build
        design pass)         design pass)               design pass)
```

Three design passes, three different skill loads, three different outputs. None is optional. The mistake to avoid is thinking design is "what happens during build." It happens before, during, and after.

---

## 2 · Pre-build design pass · SHAPE

**Goal:** decide the template's design identity *before* the planner finalises the brief, so the planner brief is grounded in a deliberate design direction rather than emerging from random skin choices later.

**When:** between intake (workflow A.1) and plan (workflow A.2).

**Inputs:**
- Cluster identity (from `DISTINCTNESS_RULES.md §3`).
- Two or three existing siblings in the cluster.
- The user's brief (any constraint, any "must avoid").

**Process:**
1. **Reach for `/impeccable shape`** — its purpose is exactly this: shape-then-build. Output is a structural brief: hero shape, section sequence, visual rhythm, motion intent.
2. **Reach for `taste-skill`** as a *premium tone reference* — not as the rule book. Its anti-slop direction filters obvious AI tells from the candidate direction.
3. **Reach for `ui-ux-pro-max`** in lookup mode — search for typography pairings appropriate to the cluster's tone, palette suggestions for the product type, anti-patterns to avoid.
4. **Compare against `factory/standards/<cluster>-design-standard.md`** — if there is a conflict between the standard and the skill output, the standard wins.

**Output:** a one-page design direction note that the planner consumes. Captures: hero shape, palette intent, typographic system, motion profile, structural rhythm, three explicit "this template is NOT" anti-positions.

**Anti-pattern to avoid:** going through the full Impeccable command surface (23 commands) on every template. The `/impeccable shape` output plus a single Pro Max search is sufficient pre-build.

---

## 3 · During-build design pass

**Goal:** keep design choices coherent while the template-builder agent is wiring code.

**When:** during workflow A.5 (build).

**Process:**
The during-build pass is *passive*. The factory standards do the binding. The skills are not loaded here unless the builder hits a specific micro-decision the standards do not resolve (e.g. "how should this CTA hover state animate?" → `/impeccable animate` for guidance, then implement against the standard's `prefers-reduced-motion` rule).

**Hard rule:** the builder does not invent palette decisions, typography decisions, or motion decisions during build. If a decision is missing, the build pauses and the planner is re-engaged. This prevents Solaria-class drift where build-time decisions accumulate without review.

---

## 4 · Post-build design pass · POLISH

**Goal:** elevate from "implementation correct" to "premium feel," and surface any defect the standards-based critics did not catch.

**When:** after critique (A.6) and before browser walk (A.7), and again after walk if the verdict is BORDERLINE.

**Process · in this order:**

1. **`/impeccable critique`** on the live URL. Output: hierarchy / clarity / emotional-resonance review. Findings are translated into edit instructions or accepted as conscious choices.
2. **`/impeccable audit`** on the live URL. Output: a11y / performance / responsive technical findings. Findings cite the standards' rule IDs (CS-PAL-*, CS-HERO-*, etc.) wherever possible.
3. **`/impeccable polish`** as the final pass. Design system alignment + shipping readiness.
4. **Surgical lifts** as needed:
   - `/impeccable typeset` — only if typography looks generic.
   - `/impeccable layout` — only if rhythm is off.
   - `/impeccable colorize` — only if accent application is timid (advisory only · standards bind).
   - `/impeccable bolder` — only if the template reads bland for its cluster.
   - `/impeccable quieter` — only if it overdesigns relative to the cluster's restraint.
   - `/impeccable delight` — only if the cluster supports it (corporate-suite is restraint; portfolio supports more).

**Hard rules:**
- Findings from skills are *advisory*. Standards are *binding*. Where a skill recommends something the standards forbid, the standard wins and the recommendation is rejected with a one-line note.
- Surgical lifts are surgical. Each lift edits one dimension. Lifting all five at once is a rebuild and inherits workflow A's gates.
- Polish is not a license to expand scope. The surface set in the brief is the surface set polished.

---

## 5 · Three-layer quality scorecard alignment

The factory's `corporate-suite-quality-scorecard.md` runs three layers (typography · imagery+palette · motion+responsive). The design-system passes line up with the layers:

| Layer | Pre-build sets the intent | Post-build verifies and polishes |
|---|---|---|
| Layer 1 · Typography | Pro Max font-pairing search · Impeccable typeset reference | `/impeccable typeset` (if needed) · style-critic verdict against typography rules |
| Layer 2 · Imagery + Palette | Pro Max palette search · imagery-curator's pack | Style-critic + contrast-auditor against `CS-PAL-*` and imagery standard |
| Layer 3 · Motion + Responsive | `/impeccable animate` reference (advisory) · responsive intent in shape | `/impeccable polish` + responsive-auditor walk |

Both layers' inputs (pre-build) and verifications (post-build) must close before LIVE flip. A template that passed the layers but did no pre-build pass is at risk of looking generic; a template that did the pre-build pass but skipped post-build polish is at risk of shipping unfinished. Both passes happen.

---

## 6 · How quality enforcement scales

The current pipeline produces one template at the Solaria-grade bar per pass. To scale to hundreds without diluting:

1. **Standardise the pre-build shape note format.** A predictable one-pager that any planner can fill out in 30 minutes; this prevents "design from scratch" on every template.
2. **Build a per-cluster reference sheet** (later, deferred work) that pre-loads the cluster invariant + the cluster-appropriate Impeccable / Pro Max queries. Reduces decision load per template.
3. **Keep the post-build polish surgical.** The temptation under volume is to skip polish; the corrective is the opposite — polish stays mandatory but surgical lifts replace whole-template re-passes.
4. **Treat the live URL as the canonical artifact.** Not screenshots, not PRs, not test outputs. The live URL is what every quality skill operates on, and it is what the orchestrator routes the next agent to.

Scale comes from sharper routing, not from skipping passes.

---

## 7 · Anti-patterns specific to this layer

- **"The skill said so" as justification.** Skills are advisory. Standards bind. If the only justification for a design choice is an Impeccable command's recommendation, the choice is unjustified.
- **Running every Impeccable command on every template.** Twenty-three commands times one hundred templates is process-bloat. The shape + critique + audit + polish quartet is sufficient on most passes.
- **Substituting Pro Max output for planner reasoning.** Pro Max returns reference data; the planner still has to think. A planner brief that is just a copy-paste of a Pro Max search result is not a brief.
- **Polishing during build.** Polish is post-build. Mid-build polish blurs the build/critique boundary and produces untracked design choices.
- **Re-running pre-build shape on edit passes.** Edit passes do workflow B, not workflow A. Re-shaping during an edit is a scope-creep tell.
