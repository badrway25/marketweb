# Pre-build quick-checks

Five lightweight micro-gates that close concrete weaknesses surfaced by the first orchestrator dry run (`design-orchestrator/dry-runs/candidate-01-*`). Each check fires BEFORE the planner-brief sign-off (A.2) or BEFORE the imagery pack commits (A.3) — i.e. before any artefact that is expensive to undo.

Companion files: `template-intake-checklist.md` (where these checks land in the intake form) · `template-orchestrator-master.md` (where these checks gate A.1 → A.3) · `single-template-workflow.md` and `batch-template-workflow.md` (where they appear as checkboxes in the operational lists).

This file is the canonical source for the five checks. The other files reference it; this is where the procedure lives.

---

## Check 1 · Reference-pack availability (cluster precondition)

**When**: at A.1, before intake sign-off.

**Procedure**:
1. Read `cluster` from intake §1.
2. Confirm both files exist:
   - `design-orchestrator/references/internal-baselines/<cluster>-reference-pack.md`
   - `design-orchestrator/references/internal-baselines/<cluster>-distinctness-matrix.md`

**Outcome**:
- Both exist → continue.
- Cluster is `corporate-suite` and both exist → continue.
- Cluster is anything else and EITHER file is missing → **HALT the pass**. The orchestrator cannot triangulate against a per-cluster pack it does not have. Surface the gap, route to "build the cluster's reference pack and distinctness matrix first" (one-off pass · same shape as the corporate-suite pack), and resume the template pass after.
- A user-signed waiver to proceed without the cluster pack is the only exception. The waiver is recorded in `<report_root>/intake.md §1` verbatim and the planner brief inherits the gap as a known risk.

**Why this matters**: the dry run on Continua succeeded because corporate-suite has a complete reference pack and distinctness matrix. Other clusters do not. Running A.2 → A.7 against a missing pack produces planner briefs that score themselves against an empty grid — distinctness collisions land in the live render rather than at A.2.

**Risk closed**: "we built a medical / restaurant / agency template against the corporate-suite pack and shipped a sibling clone."

---

## Check 2 · Sibling palette warmth/coolness conflict warning

**When**: at A.1 §3 (`palette_intent`), before intake sign-off.

**Procedure**:
1. For the proposed palette, classify each role on a tiny grid:

   | Role | Warm / Cool / Neutral |
   |---|---|
   | primary | warm · cool · neutral |
   | secondary | warm · cool · neutral |
   | accent | warm · cool · neutral |

2. For each existing sibling in the cluster, fill the same grid (read it off the sibling's `template_dna.py` and the cluster reference pack §4).
3. Compare cell-by-cell. If the proposed grid matches ANY sibling's grid on ≥ 2 of the 3 roles, raise a `[PALETTE WARMTH COLLISION]` flag in intake §3.

**Outcome**:
- 0 or 1 cells overlap with each sibling → continue.
- 2 or 3 cells overlap with any sibling → **RESPEC**. The palette intent is too close in temperature topology even if the hex values differ. Re-shape the warmth strategy (e.g. flip secondary cool→warm) before continuing.

**Why this matters**: hex-level distinctness can pass while temperature-topology distinctness fails. Two cool-primary + cool-secondary + warm-accent palettes read as siblings on the live page even when the hexes are 30° apart on the colour wheel. The dry run surfaced this risk vs Pragma; the temperature grid catches it explicitly.

**Risk closed**: "the new template's palette is unique by hex but reads as the same family as Pragma / Fiscus / Solaria at first glance."

---

## Check 3 · Imagery feasibility quick-search (pre-A.3)

**When**: AFTER planner-brief sign-off (A.2) and BEFORE the imagery curator commits any URL (A.3 entry).

**Procedure** (~5 minutes, the orchestrator runs this; the curator does the full pack work after):

1. From the planner brief §6 imagery direction, list the 6 declared slot subjects (hero · feature · portrait-pair · ambient · detail · closer).
2. For each subject, run ONE Pexels search using the most concrete keyword phrase (e.g. "private library reading room brass key cabinet" not "stewardship vibes").
3. Count the plausible candidates on the first results page (a candidate is plausible if subject + composition + license type are all viable; do not commit URLs yet).

**Outcome**:
- Every slot returns ≥ 5 plausible candidates → **GO for A.3**. The pack is feasible.
- One slot returns 3–4 candidates → **CAUTION**. Continue to A.3 but flag the slot as "narrow pool — accept the curator's first viable swap if the lead candidate fails cross-cluster grep".
- Any slot returns ≤ 2 candidates → **RESPEC**. The imagery direction is too narrow for Pexels-only sourcing. The planner brief returns to A.2 with a softer subject for that slot. Do NOT proceed to A.3 with an infeasible slot — the curator will spend an hour discovering the gap, then the brief returns to A.2 anyway.

**Why this matters**: the dry run declared a "stewardship archive cabinet · brass key · single bound register · no people" hero — concrete and distinct, but Pexels-thin on that exact composition. Discovering Pexels-thinness at A.3 (after copy starts) costs more than discovering it at A.2.5. Five minutes of search beats a half-day of pack rework.

**Risk closed**: "the planner declared a beautiful imagery direction that the Pexels-only constraint cannot satisfy."

---

## Check 4 · Content-volume estimate

**When**: at A.1 §7 (section rhythm), before intake sign-off. Becomes a section in the planner brief at A.2.

**Procedure**: estimate the home-page word budget per beat. Use the cluster's existing siblings as the benchmark (read 1-2 siblings' rendered home pages and count rough word counts).

**Reference budget for corporate-suite** (from Pragma · Fiscus · Solaria averages):

| Beat | Approx. word count | Notes |
|---|---|---|
| Hero h1 + sub | 25-45 | one sentence with em-wrap + one-line stance |
| Hero meta-strip (3 cells × label+value) | 30-60 | tabular numerals on values |
| Pillars (3 or 4 × title+body) | 240-400 | 60-100 words per pillar body |
| KPI band (3 or 4 × label+value+caption) | 60-120 | concise, no marketing copy |
| Mid-strip (3 cells × label+body) | 120-240 | the differentiator beat |
| Sectors / vertical-list | 80-160 | label + one-line caption per sector |
| Leadership block (if present) | 120-240 | name + role + 1-line bio per leader |
| Cases / proof block | 240-400 | 3 cases × ~100w each |
| CTA closer | 40-80 | restates voice anchor + form gate |
| **Total home (rendered text)** | **1500-2500** | ranges by archetype variant |

Other clusters: extrapolate from the cluster's siblings; if the cluster is thin, fall back to the corporate-suite range with a 20% adjustment for verticality (restaurant tends shorter; medical-specialist tends longer).

**Outcome**:
- Estimate falls inside the cluster's typical range → continue.
- Estimate < 70% of cluster floor → **RESPEC**. The page will read sparse and editorial-thin against siblings; rhythm flattens.
- Estimate > 130% of cluster ceiling → **RESPEC**. The page will read as a wall-of-text and trip CS-COMP-06.
- Estimate inside range BUT skewed (one beat takes > 50% of total) → **RESPEC** that beat. Two adjacent sections with similar function violates CS-RHYTHM-04.

**Why this matters**: copy authoring at A.4 inherits whatever volume the brief implied. Discovering at A.7 walk that the page reads sparse or top-heavy means re-authoring copy, not just patching css. The estimate at intake locks the working envelope.

**Risk closed**: "the IT walk passed but the page reads sparse · top-heavy · or as a wall-of-text because nobody estimated the budget upstream."

---

## Check 5 · "Remove the studio name" pre-test (early proceduralization)

**When**: at A.1 §3 (`stakeholder_first_30s_read`) AND at A.2 (planner brief §10 single-page summary). The test runs TWICE — once on intake claims, once on planner expansion.

The same test appears in `template-orchestrator-master.md §5.12` as a fail-state at the live page. This check pulls it forward so the design fails it on paper, not on screen.

**Procedure**: write the `stakeholder_first_30s_read` (intake §3) THREE times in the intake file:

```
A · with the studio name as written
    "Continua is the family-office that custodies a family's
     patrimony across generations, not market cycles."

B · with the studio name removed
    "[___] is the family-office that custodies a family's
     patrimony across generations, not market cycles."

C · with the studio name swapped for a generic cluster placeholder
    "Acme Family Office is the family-office that custodies
     a family's patrimony across generations, not market cycles."
```

**Outcome**:
- Versions B and C still uniquely describe THIS template (not the generic cluster · not Pragma · not Fiscus · not Solaria) → **PASS**. The identity is in the structure, not in the brand-name lift.
- Version B or C reads as a generic family-office description that any sibling could claim → **RESPEC**. The differentiation is leaning on the brand name. The voice anchor, palette, hero meta-strip, or section rhythm has to do more lifting before A.2 sign-off.

The same test is re-run on the planner brief §10 single-page summary at A.2 sign-off. If §10 fails the swap, the brief returns to re-spec — even if every numeric distinctness score is ≥ 4/5.

**Why this matters**: the live-page version of this test (master §5.12) catches generics post-build, when fixing them is a re-author pass. Running it on the intake claim and on the brief summary catches the same problem on paper, when fixing it is one rewrite of one paragraph.

**Risk closed**: "the brief scored ≥ 4/5 on every axis but the page reads as a generic family-office firm because the differentiation lived in the studio name and adjectives, not in the structure."

---

## Use checklist

The orchestrator runs all five checks. The intake checklist (`template-intake-checklist.md` §3, §6, §7, §13) cites them. The master prompt (`template-orchestrator-master.md §3 A.1`, `§3 A.2`, `§3 A.2.5`) gates on them. The operational workflows (`single-template-workflow.md §2 pre-build gates`, `batch-template-workflow.md §2 phase 1/2/5`) treat them as required boxes.

Total time cost: ~15 minutes of orchestrator work for all five checks combined. Each one closes a specific failure mode the dry run surfaced. None is theoretical; each routes RESPEC vs continue with a concrete trigger.
