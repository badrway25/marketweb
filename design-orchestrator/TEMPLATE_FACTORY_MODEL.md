# Template factory model

The factory model is already encoded in `factory/standards/corporate-suite-multi-agent-sop.md`. This document does **not** restate it. It does three things the SOP does not:

1. Generalises the corporate-suite factory shape to the rest of the catalog.
2. Defines the three canonical workflows (new template · edit pass · multilingual rollout) at the orchestrator's altitude.
3. Names the minimum evidence each workflow must produce before the next workflow can begin.

Read `factory/standards/corporate-suite-multi-agent-sop.md` first. This document references its sections by tag (e.g. `SOP §4.2`).

---

## 1 · The factory spine

Every template, in every cluster, traverses the same nine roles in the same order. This is the spine; specific clusters add or substitute *standards*, never *roles*.

```
intake → plan → pack → copy → build → critique → walk → fix? → aggregate
  ↑       ↑      ↑      ↑      ↑        ↑        ↑      ↑        ↑
  orch  T-PLN  IMG-C  CPY-T  T-BLD  STY+CTR+RSP  BR-V  T-EDF   REL-GK
```

Roles map 1:1 to `factory/agents/*.md`. The orchestrator role sits above the spine and never collapses into it.

### What is fixed across clusters

- The nine roles, their order, and their narrow remits.
- The standard report schema (`SOP §6`).
- The two-commit cadence (`SOP §1.3`): Commit A draft-landing → Commit B LIVE flip.
- Browser-walk-as-ship-gate (`SOP §1.1`).
- Pexels-only on new templates (`SOP §0.6`).
- Distinctness gate before draft-landing (this folder · `DISTINCTNESS_RULES.md`).

### What varies across clusters

- The standards file the planner / critic / gatekeeper read. Today only corporate-suite has a complete set under `factory/standards/`. Other clusters fall back to corporate-suite as a baseline plus archetype-specific deltas captured in the planner's brief, until they earn their own standards file.
- The voice-anchor rule (corporate-suite is institutional-advisory; restaurant is sensorial; medical is clinical-warm; etc.).
- The imagery profile (G1-G3 patterns from the imagery standard generalise; specific subjects/moods are cluster-specific).
- The viewport matrix sometimes adds a cluster-specific breakpoint (e.g. ecommerce often needs a 1024 product-grid breakpoint).

---

## 2 · How a new cluster earns its standards

Today's reality: corporate-suite has the only full standards set. The rest of the catalog operates on corporate-suite-as-baseline plus archetype memory. That works for the current size; it does not scale to "hundreds of templates."

The path to per-cluster standards (deferred work, see `NEXT_STEPS.md`):

1. The cluster's first three siblings are produced under corporate-suite-baseline + per-template deviations logged.
2. After the third sibling, the orchestrator extracts the recurring deviations into a candidate `factory/standards/<cluster>-design-standard.md` skeleton.
3. The candidate is reviewed against the three siblings as a regression test (does it explain why each one passed?).
4. If yes, the standard is promoted and subsequent siblings in that cluster are produced against it directly.

This sequence is **not** in scope for the present pass. Naming it here so the orchestrator does not improvise it under pressure.

---

## 3 · Canonical workflow A · one new template

Use case: a brand-new sibling in an existing cluster (e.g. another corporate-suite, a fourth restaurant). For brand-new clusters, see §2 first.

### A.1 · Intake (orchestrator · ~5 min)

Inputs: user brief or roadmap entry.
Outputs: a one-page intake note answering:
- Cluster · archetype · proposed brand name.
- Locales (always start IT-only · D-102 cadence).
- Two siblings nearest in palette/imagery/voice for triangulation.
- Any explicit user constraint or "must avoid" item.

### A.2 · Plan (template-planner · ~30 min)

Inputs: intake note · `factory/standards/<cluster>-design-standard.md` · existing siblings.
Outputs (per `SOP §3` deliverable schema):
- Voice anchor (verbatim sentence).
- Palette spec (named tokens · adjacency-cleared against siblings).
- D-054 triangulation matrix (this template vs every existing sibling on palette · voice · imagery · structure).
- Imagery direction (subject · mood · 6-slot pool intent).
- Scope: pages · components · expected line budget.

**Skill assist:** `/impeccable shape` for structure-before-code framing. `taste-skill` (default sub-skill) for premium tone reference. Pro Max search for palette / typography pairing lookup.

**Gate:** the orchestrator will not approve the plan if the triangulation matrix shows any cell where this template is indistinguishable from an existing sibling (see `DISTINCTNESS_RULES.md §3`).

### A.3 · Pack (imagery-curator · ~30-60 min)

Inputs: planner brief · `factory/standards/<cluster>-imagery-standard.md`.
Outputs:
- Pexels-only pack file with per-URL metadata (subject · role · coherence note · license confirmation).
- 6-slot pool selection.

**Gate:** orchestrator refuses any pack containing non-Pexels URLs on new templates. No exceptions.

### A.4 · Copy (copy-translation · IT first · ~30-60 min)

Inputs: planner brief · curated pack.
Outputs:
- IT locale tree complete · voice anchor verbatim where prescribed.
- No translations yet (those happen after build proves IT works).

### A.5 · Build (template-builder · ~30-90 min)

Inputs: copy + pack + palette spec.
Outputs:
- Wired skin in `apps/catalog/...` skin module.
- `template_dna.py` / `seed_templates.py` / `preview_imagery.py` updated.
- CLI green: `python manage.py test apps.catalog` + the existing test suite + `generate_previews`.
- IT live URL openable in browser.

### A.6 · Critique (style-critic + contrast-accessibility + responsive · parallel · ~30 min total)

Inputs: live IT URL.
Outputs (parallel · per `SOP §6` schema):
- Style critique against design standard `[BLOCKING]` and `[REQUIRED]` rules.
- Contrast report (CS-PAL-01 / 04, hero-03, focus-visible, reduced-motion).
- Responsive report (viewport matrix · no horizontal scroll · touch targets).

**Skill assist:** `/impeccable audit` for accessibility + `/impeccable critique` for hierarchy/clarity — both cite their findings against the standards' rule IDs, not in their own vocabulary.

### A.7 · Walk (browser-verifier · IT · ~30 min)

Inputs: live URL · `factory/standards/<cluster>-browser-rubric.md`.
Outputs: rubric verdict (PASS · BORDERLINE · FAIL) with per-cell evidence.

**Gate:** if FAIL or BORDERLINE → §A.8 Fix. If PASS → Commit A draft-landing is authorized.

### A.8 · Fix (template-editor-fixer · only on FAIL/BORDERLINE)

Narrowest possible diff. Re-runs §A.6 + §A.7 on the affected dimension. Does not author new content.

### A.9 · Aggregate (release-gatekeeper + orchestrator)

Inputs: every report from §A.2 - §A.7 (and §A.8 if it ran).
Outputs:
- Filled `corporate-suite-quality-scorecard.md` (or per-cluster equivalent).
- User-handshake document.
- Decision: Commit A merged to integration branch with `TEMPLATE_REGISTRY.json` at `draft`.

Commit B (LIVE flip) is a separate pass. See `BROWSER_QUALITY_GATE.md` for what Commit B requires beyond Commit A.

---

## 4 · Canonical workflow B · one edit / improvement pass

Use case: an existing template shows a defect (Solaria-class regression · contrast issue · imagery weakness · copy update · palette refresh).

### B.1 · Diagnose (orchestrator + style-critic + browser-verifier · live walk first)

Reverse the build order: **walk before plan**. The diagnose step produces a report listing exactly which standards' rules fail and on which surfaces.

Outputs:
- A short diagnostic note: rule ID(s) failed · pages affected · locales affected · severity (`[BLOCKING]` / `[REQUIRED]` / `[STRONG]`).
- Decision: is this an edit pass or does it need re-planning?

### B.2 · Scope-lock (orchestrator · 5 min)

Outputs: a scope statement that says explicitly:
- Which file(s) will change.
- Which standards rules will be re-tested afterwards.
- Whether the change can ship under the existing brand identity or requires planner re-engagement.

This step exists to prevent edit passes from quietly turning into rebuilds. **An edit pass that touches more than the diagnosed surfaces becomes a workflow A pass and inherits all its gates.**

### B.3 · Edit (template-editor-fixer · narrowest diff)

Inputs: scope-lock note.
Outputs: minimal diff · CLI green · live URL still openable.

**Skill assist (selective):**
- Typography problem → `/impeccable typeset`.
- Layout/spacing problem → `/impeccable layout`.
- Contrast/color problem → `/impeccable colorize` *as advisory only*; the binding rule is the standard's `CS-PAL-*`.
- Excessive boldness → `/impeccable quieter`. Excessive blandness → `/impeccable bolder`.
- Final polish before re-walk → `/impeccable polish`.

### B.4 · Re-walk (browser-verifier · same locales as diagnosis)

Same rubric verdict as workflow A.7. Specifically re-tests the failed rules from B.1.

### B.5 · Aggregate (release-gatekeeper + orchestrator)

If the original template was already at `published_live`, the gatekeeper authorises a hot-fix flip after the user handshake. If it was at `draft`, this is just an iteration of workflow A.

**Anti-drift trap:** edit passes are seductive because they feel small. They become Solaria-class when one "small" edit cascades into untested surfaces. The scope-lock in §B.2 is the discipline that prevents this.

---

## 5 · Canonical workflow C · one multilingual rollout

Use case: an IT-only template needs to ship in additional locales (typically EN, FR, ES, AR with RTL).

This is the workflow Solaria's Pass B exercised (`MEMORY.md` → `phase_x4_solaria_passB_multilingual.md`). It is the easiest workflow to underestimate and the easiest to break the voice anchor on.

### C.1 · Pre-flight (orchestrator · 5 min)

Inputs: live IT template at `draft` or `published_live`.
Verify:
- IT walk verdict on file and ≤30 days old.
- Voice anchor sentence captured verbatim in the planner brief.
- Imagery pack already locale-agnostic (no IT-specific text baked into images).
- For AR specifically: skin already supports `dir=rtl` via logical properties; if not, this is a workflow A pass on the skin first.

### C.2 · Translate (copy-translation · per-locale · sequential or parallel)

Inputs: IT locale tree · voice anchor · cluster terminology rules.
Outputs:
- One locale tree per target locale.
- Voice anchor preserved verbatim or with the documented translation pattern (Solaria Pass B precedent).
- For AR: terminology vetted by the cluster's terminology guide.

**Skill assist:** Pro Max for typography pairing per locale (e.g. AR Noto Kufi h1 swap). Impeccable is *not* used for translation; translations are not a design problem.

### C.3 · Build (template-builder · light)

Inputs: locale trees.
Outputs: locale trees seeded · `seed_templates.py` updated · CLI green · live URLs openable in every locale.

### C.4 · Per-locale walks (browser-verifier · one walk per locale)

Each locale gets its own rubric verdict. AR specifically gets the RTL parity walk. The orchestrator does not approve the rollout until **every** locale walk passes.

The Solaria precedent is the canonical example: 11/11 captures across IT/EN/FR/ES/AR with 0 fixes mid-walk is the bar.

### C.5 · Aggregate (release-gatekeeper + orchestrator)

Scorecard with per-locale rows. User-handshake. Flip decision per locale (it is acceptable to flip IT/EN/FR/ES while holding AR for one more pass if AR alone is the failure).

---

## 6 · Evidence retention

Every workflow ends with reports. Retention rules:

- Workflow A reports → `factory/reports/<archetype>/<template-slug>/...`.
- Workflow B reports → `factory/reports/<archetype>/<template-slug>/edit-<date>.md`.
- Workflow C reports → `factory/reports/<archetype>/<template-slug>/multilingual-<date>.md`.

The reports are the orchestrator's only durable memory. They are what allows the next pass to triangulate against this one without re-doing the analysis.
