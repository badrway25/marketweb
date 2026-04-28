# Distinctness rules

The user's goal is **hundreds of templates, all clearly different from each other.** That is the hard constraint distinctness rules exist to enforce. A premium template that looks like another premium template is a regression even if both score 5/5 on the quality scorecard individually.

This document is the operational checklist the orchestrator runs **before** any new sibling lands in a cluster. It is also the checklist that an edit pass uses when the diagnosis is "this template feels like its neighbour."

---

## 1 · The five differentiation axes

A new template must be clearly different from every existing sibling in its cluster on **at least four of the five axes below**. Three or fewer axes of differentiation = collision = block the draft-landing.

| # | Axis | What "different" means |
|---|---|---|
| 1 | **Voice / positioning** | The voice anchor sentence is semantically distinct. Two siblings cannot both anchor on "trust" or both on "craft" without one being scoped narrower. |
| 2 | **Palette identity** | The dominant hue family + accent family is not adjacent to any sibling's. Adjacency = same hue family AND same lightness band. Two greens are fine if one is forest-deep and one is pale-mint; two mid-greens collide. |
| 3 | **Imagery profile** | Subject + mood + crop convention. Two restaurants both leading with "warm overhead pasta close-up" collide. One overhead, one stylised plating portrait, one rustic table-wide is the cluster shape. |
| 4 | **Typographic system** | Heading family + body family + scale + emphasis convention. Sibling templates may share a body family (especially within a cluster's tone) but must differ on heading family OR italic-vs-uppercase emphasis OR letter-spacing identity. |
| 5 | **Visual surface / structural rhythm** | Hero shape, dark-band placement, section count, motion profile, density. Two siblings cannot both be "alternating dark/light bands with KPI center band" without an explicit waiver. |

Four of five passes. Three or fewer fails. The triangulation matrix in `factory/standards/corporate-suite-design-standard.md` and the planner's D-054 sibling triangulation are the inputs for filling out this matrix.

---

## 2 · The triangulation matrix

For every new template, the planner produces a matrix that scores this template versus *each* existing sibling on the five axes:

```
                  | Axis 1 | Axis 2 | Axis 3 | Axis 4 | Axis 5 | Axes-different |
Sibling: Pragma   |   ✓    |   ✓    |   ✓    |   ✓    |   ✗    |       4/5       |
Sibling: Fiscus   |   ✓    |   ✓    |   ✓    |   ✗    |   ✓    |       4/5       |
Sibling: Solaria  |   ✓    |   ✓    |   ✓    |   ✓    |   ✓    |       5/5       |
```

A row scoring 3/5 or worse blocks the pass. The planner re-spec's the offending axes and resubmits.

The matrix is part of the planner deliverable (`SOP §3.1`). The orchestrator does not approve the plan without it.

---

## 3 · Cluster-level distinctness contract

Each cluster carries an additional cluster-level invariant that protects the cluster's identity against any one sibling drifting:

| Cluster | Invariant |
|---|---|
| corporate-suite | Institutional-advisory tone · serif heading + sans body · one dark band per home · gold/emerald/warm-earth accent vocabulary · no SaaS-marketing CTAs. |
| medical-specialist | Clinical-warm tone · trust signals (credentials) · calm imagery (no clinical-equipment macro shots unless brand requires) · no "transformation" before/after framing without consent context. |
| restaurant | Sensorial copy · imagery foregrounded · menu/price-list legible · no aspirational lifestyle shots dominating. |
| portfolio | Editorial grid OR cinematic full-bleed · creator's voice not the platform's · imagery is the protagonist · UI recedes. |
| ecommerce | Product-clarity and price-trust dominate · imagery serves product, not lifestyle · CTA hierarchy is buy-first. |
| real-estate | Property-first imagery · location proof · honest area/price disclosure · no "luxury for everyone" linguistic flattening. |
| law | Restraint · serif typography · gold/burgundy/navy palettes · no marketing hyperbole. |
| agency | Self-aware design · case-study density · the agency's own voice · imagery oscillates between work-shown and team-shown. |
| startup-saas | Crisp clarity · technical confidence · imagery often UI-of-product · CTA-first hierarchy. |
| medical-other | Calm-warmth balance · varies by sub-cluster (clinic vs wellness vs family). |

A new sibling that violates its cluster invariant collides with the *cluster identity*, not just a sibling. That is also a block.

---

## 4 · Distinctness enforcement timing

| Phase | What is checked | By whom |
|---|---|---|
| Plan (workflow A.2) | Triangulation matrix · cluster invariant. | Orchestrator gates the plan. |
| Pack (A.3) | Imagery profile · subject/mood overlap with siblings. | Imagery-curator self-checks · orchestrator audits. |
| Critique (A.6) | Style-critic compares the rendered DOM against the closest two siblings, not just against the standard. | Style-critic · escalates collisions to orchestrator. |
| Walk (A.7) | The browser walk includes a side-by-side viewport check against the nearest sibling's live URL. | Browser-verifier. |
| Edit pass (workflow B) | If the diagnosis is "feels like sibling X," re-run the matrix. | Orchestrator. |

Distinctness is not checked once. It is checked at every gate and at every workflow that could erode it.

---

## 5 · The colliding-sibling escalation

When the matrix shows 3/5 or worse against an existing sibling, three options exist:

1. **Re-spec this template** — change palette / imagery / voice anchor. Most common outcome.
2. **Re-scope an existing sibling** — only when the existing sibling is itself drifting from the cluster invariant and the new template would represent the cluster's correct identity. Requires explicit user decision; not the orchestrator's call.
3. **Demote one to a variant** — if two siblings are inevitably similar (e.g. two corporate-suite "boutique law/finance advisor" templates), one is reclassified as a *variant* of the other and they share base assets while differentiating on a single axis. Documented in the planner brief.

Option 1 is the default. Options 2 and 3 are exceptions.

---

## 6 · The "looks like AI-generated SaaS" red flag

Hundreds of premium templates that all look like they came out of the same generic AI model is the catastrophic failure mode. The Impeccable skill catalogues this anti-pattern set explicitly (Inter font · purple gradients · cards-in-cards · gray-on-colored-bg). Pro Max similarly carries 161 reasoning rules including anti-pattern flags.

**Operational rule:** if a template's first impression matches any of the listed AI-slop tells, it is treated as a 0/5 on Axis 4 or 5 regardless of how the matrix scores it. The Impeccable detector and `factory/references/anti-pattern-library.md` are the canonical lists.

---

## 7 · Distinctness vs creative freedom

This document is not a tax on creativity. It is an asymmetry: the cost of two indistinguishable templates is felt by every future template (the catalog looks generic), the cost of one outlier template is contained. Therefore the bar pushes toward differentiation, not toward a house style.

The cluster invariants in §3 protect the cluster identity. Within those, the planner is encouraged to take the more differentiated of two viable options at every fork. Default to bold; the standards will pull anything actually broken back to safe.
