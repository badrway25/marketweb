# Release decision orchestrator prompt

**Use this prompt to decide a template's release tier: keep at `draft` · move to `review-ready` · flip to `published_live`.**
Paste it verbatim at the start of a release decision pass. Replace the bracketed `<…>` slots in §0. This is a separate pass from workflow A (which lands `draft`) and workflow C (which adds locales). Releasing is a deliberate decision; it never piggybacks on a build session.

The orchestrator's stance here is conservative. The cost of a premature flip is felt by every visitor of every page that template generates; the cost of a held flip is one extra pass. The asymmetry pushes every borderline call toward HOLD.

---

## 0 · Run-time slots (fill before first turn)

```
template_slug:                <existing template slug>
cluster:                      <cluster name>
current_tier:                 <draft | review-ready>
proposed_tier:                <review-ready | published_live>
locales_in_scope:             <subset of [it, en, fr, es, ar]>
report_root:                  factory/reports/<archetype>/<template_slug>/release-<YYYY-MM-DD>/
last_walk_per_locale:         <map locale → walk verdict path · age in days>
last_critique_paths:          <style · contrast · responsive>
last_scorecard_path:          <factory/reports/scorecard/<template_slug>/scorecard.md>
distinctness_matrix_status:   <current row in corporate-suite-distinctness-matrix.md §1>
user_handshake_path:          <existing handshake artefact, if any>
known_open_issues:            <list of every open finding · severity · file>
```

---

## 1 · The three tiers, what each one means

The terms have specific operational meanings. Read these before deciding.

### `draft`
- Default after a successful workflow A pass (D-102 cadence).
- Visible internally / staff sessions / preview routes. NOT visible to public visitors.
- Editor-only affordances may still leak (though they should not).
- Single-locale acceptable (typically IT-only).
- Walk verdict: PASS at IT.
- Open issues: any severity allowed except open `[BLOCKING]`.
- Implication: the template is real, but the team has not yet committed to it as a public artefact.

### `review-ready`
- Internal/staff sessions only, but with the explicit framing of "we believe this is shippable; we are seeking the user-handshake before flipping."
- All locales in scope have walked PASS.
- Cross-cluster grep confirms Pexels-only on every live render.
- Distinctness matrix re-confirms the template is still ≥ 4/5 vs every sibling.
- Editor-only affordances confirmed hidden on `/live/`.
- The user has not yet signed off; the gatekeeper has.
- Implication: this is the holding state between "we built it" and "we ship it." Most templates spend at least one cycle here.

### `published_live`
- Public-visitor visible.
- All locales in scope have walked PASS within 30 days.
- The user has signed off via the parallel-verification handshake (`BROWSER_QUALITY_GATE.md §6`).
- The gatekeeper has stamped Layer 1 / 2 / 3 on the scorecard.
- Pexels-only audit on the LIVE render passed (not just the pack file).
- The cluster's `[BLOCKING]` rule set has zero open findings.
- Implication: the template is part of the public catalog and inherits the regression-watch obligation (`BROWSER_QUALITY_GATE.md §7`) on every subsequent edit.

---

## 2 · Mandatory inputs

1. `design-orchestrator/BROWSER_QUALITY_GATE.md` — the entire file. Re-read every release pass. Especially §1, §3, §6, §7.
2. `design-orchestrator/ORCHESTRATOR.md §6` — the anti-drift list. Especially rules 3, 4, 8, 10.
3. `design-orchestrator/DISTINCTNESS_RULES.md §4` — distinctness is checked at the edit-pass gate; here we re-confirm it has not silently moved since the last walk.
4. The template's full report tree at `factory/reports/<archetype>/<template_slug>/`.
5. The cluster's blocking-rules file `factory/standards/<cluster>-blocking-rules.md`.
6. The cluster's scorecard template `factory/standards/<cluster>-quality-scorecard.md`.
7. The current `MEMORY.md` baseline pointer to confirm no recent precedent changes the bar.

---

## 3 · The decision tree (run in order · stop at first HOLD)

Walk this top-to-bottom. The first HOLD wins. Do not "average" findings across cells.

### Step 1 · Are all cluster `[BLOCKING]` rules satisfied?

For every rule ID in `factory/standards/<cluster>-blocking-rules.md`, the latest critique / walk verdict for the affected locale shows zero open findings of that severity.

- ZERO open `[BLOCKING]` → continue
- ANY open `[BLOCKING]` → HOLD at current tier · route to workflow B on the failing rule

### Step 2 · Are the per-locale walks fresh and PASS?

For every locale in `locales_in_scope`:
- Walk verdict on file is PASS (not BORDERLINE, not FAIL)
- Walk age ≤ 30 days

If `proposed_tier == published_live` and any locale's walk is older than 30 days OR not PASS:
- HOLD · re-walk that locale · re-evaluate

If `proposed_tier == review-ready` and any locale walk is missing or non-PASS:
- HOLD · the rollout is incomplete · close workflow C first

### Step 3 · Does the live DOM still match the planner brief?

Open the live URL in every locale. Compare against the planner brief's §10 single-page summary. If any of the 12 distinctness matrix dimensions reads differently than the brief described:
- Investigate whether an edit pass moved the dimension intentionally (planner sign-off required) or accidentally (unauthorised drift)
- Unauthorised drift → HOLD · open workflow B (issue class II) on the drifted dimension
- Authorised move → confirm the matrix re-score and continue

### Step 4 · Is distinctness still ≥ 4/5 vs every existing sibling?

Re-fill this template's row in `corporate-suite-distinctness-matrix.md §1.1-§1.12`. Re-score against every sibling.
- Every sibling shows ≥ 4/5 → continue
- Any sibling shows ≤ 3/5 → HOLD · the template has collided since draft-landing · workflow B (issue class II) is required

### Step 5 · Is the live imagery Pexels-only on every locale?

Run the Pexels-only audit on the live DOM (not just the pack file · `BROWSER_QUALITY_GATE.md §5`). Every image URL traces to `images.pexels.com/photos/...`.

- All Pexels → continue
- Any non-Pexels (and template is not the Pragma legacy carve-out) → HOLD · imagery substitution required before flip

### Step 6 · Are editor-only affordances confirmed hidden on `/live/`?

Walk the live URL with the `body.mw-is-editor-preview` guard NOT applied. Click-to-edit halos, region highlights, editor-toolbar leak, and any other in-editor affordance must be invisible (CS-MARKET-01 · CS-MARKET-04).

- Confirmed hidden across home + secondary pages → continue
- Any leak detected → HOLD · workflow B on the chrome partial (issue class I)

### Step 7 · Does the AI-slop red-flag check pass on the live render?

Run the detector list (`corporate-suite-reference-pack.md §9` for corporate-suite; the cluster equivalent for other clusters) against the live DOM:
- No Inter on h1, no purple gradients, no cards-in-cards, no gray-on-colored-bg, no "Get started free", no Einstein quotes, no mountain-peak hero, no fake "Trusted by 10,000+", no "Made with Marketweb" footer
- Run on every locale that is in scope

- All clear → continue
- Any tell present → HOLD · workflow B on the offending element

### Step 8 · Has the user signed off via the parallel-verification handshake?

ONLY checked when `proposed_tier == published_live`. The user (Badr) does the parallel walk and signs the artefact at `<report_root>/user-handshake.md`. The orchestrator does NOT simulate this; it presents the evidence pack and waits.

The evidence pack contains:
- The rubric verdict file per locale
- 6-12 captures per locale (hero · KPI band · CTA · footer · the section the cluster's standard most often regresses on)
- The scorecard with Layer 1 / 2 / 3 stamped
- Any `§ deviation` notes the gatekeeper logged
- The Pexels-only confirmation on the live DOM

- User signs SHIP → continue to Step 9
- User signs HOLD or does not sign → HOLD at current tier · the user's HOLD does not require justification but it is recorded

If `proposed_tier == review-ready`, this step is skipped (review-ready does not require user handshake — it is the state in which we ASK for one).

### Step 9 · Has the gatekeeper stamped the scorecard?

The release-gatekeeper agent fills the cluster's scorecard with the three layers (typography · imagery+palette · motion+responsive) and stamps each as PASS / BORDERLINE / FAIL with rationale.

- All three layers PASS · overall ≥ 4.50/5 (≥ 4.67/5 is precedent) → flip authorised
- Any layer BORDERLINE or FAIL · or overall < 4.50/5 → HOLD

### Step 10 · Final orchestrator gate · the conservative override

Even with all 9 steps green, the orchestrator may HOLD if:
- The template was draft-landed within the past 24 hours and has not been live-walked under fresh eyes
- The template is the FIRST in a new cluster (cluster invariant has not been validated against the standard yet)
- A new `[BLOCKING]` rule was added to the standard since the last walk, regardless of whether existing siblings have been audited against it
- The pass that built this template was a single-author pass (one session authored copy + palette + imagery + skin + review · `ORCHESTRATOR.md §6 rule 4`)
- The user previously held this template at this same tier in a recent pass and the diagnosed defect was not specifically addressed

These overrides are conservative on purpose. The cost of one extra pass is small; the cost of a regression is loud.

---

## 4 · The output

Output a release-decision document at `<report_root>/release-decision.md` containing:

```
RELEASE DECISION · <template_slug> · <proposed_tier>
====================================================

Decision:                 <SHIP | HOLD>
Decided by:               orchestrator
Decided on:               <YYYY-MM-DD>

Step-by-step gates:
  1. [BLOCKING] rules:           <PASS | FAIL · reason>
  2. Walks fresh + PASS:         <PASS | FAIL · reason>
  3. Live DOM vs brief:          <PASS | FAIL · reason>
  4. Distinctness ≥ 4/5:         <PASS | FAIL · reason>
  5. Pexels-only on live:        <PASS | FAIL · reason>
  6. Editor affordances hidden:  <PASS | FAIL · reason>
  7. AI-slop red flags clear:    <PASS | FAIL · reason>
  8. User handshake (LIVE only): <SIGNED · SHIP | SIGNED · HOLD | not requested>
  9. Scorecard stamped:          <PASS · grade · 0/N blocking · Y/Y locales | FAIL · reason>
 10. Conservative override:      <invoked · reason | not invoked>

If SHIP:
  Tier flipping from <current_tier> to <proposed_tier> on locales <list>
  TEMPLATE_REGISTRY.json updated · sync_template_tiers run · regression-watch obligation now binding

If HOLD:
  Cause:                <one sentence}
  Routing:              <workflow A | workflow B | workflow C · agent · scope>
  Re-evaluation date:   <when the next release pass would be appropriate>

Evidence pack inventory:
  Walks:                <per locale · path>
  Captures:             <directory · count per locale>
  Critiques:            <three paths>
  Scorecard:            <path>
  Distinctness matrix:  <path · re-scored on <date>>
  User handshake:       <path | n/a>
```

The document is the durable record of the decision. It is read at the next release pass on this template.

---

## 5 · Stop conditions

The release pass HALTS at any of these:

1. **A required input file is missing.** The walk · the critiques · the scorecard · the planner brief. Missing input = missing evidence = HOLD.
2. **The template has had no walk in the last 30 days.** Re-walk first. No verdict, no flip.
3. **An open `[BLOCKING]` finding.** Severity is set by the standard, not by the convenience of the moment.
4. **The user signs HOLD on the handshake.** No justification needed. The orchestrator does not negotiate.
5. **A skill recommendation is being treated as a release signal.** Skills inform; standards bind. No skill output is a flip authorisation.
6. **The decision feels rushed.** If the orchestrator cannot articulate WHY each of the 10 steps PASSES in one sentence, the gate has not been run with discipline. Re-walk it.

When you stop, write the stop into `<report_root>/release-stop-<date>.md`. Surface to user.

---

## 6 · Conservative-by-default rationale

Why this prompt is risk-averse:

- **Visible failure compounds.** A regression on a published template is felt by every subsequent visitor and erodes trust in the catalog as a whole. A hold delays one template by hours or days.
- **Standards are a lower bound, not a ceiling.** Passing every rule does not guarantee premium feel. The orchestrator's judgment exists to catch what the rules cannot.
- **The user's handshake is the irreplaceable signal.** Automation can verify rules; only the user verifies whether the page MATCHES THE INTENT. Skipping or rushing this is a Solaria-class shortcut.
- **The pass that built this template was upstream of the release decision.** A weak build cannot be rescued by a release pass. Better to identify "this needs a workflow B before we flip" than to flip a borderline candidate.
- **Hold is reversible. Flip is harder to reverse.** A hold-then-flip later costs one extra pass. A flip-then-rollback costs every visitor between flip and rollback.

The asymmetry is deliberate. Every borderline call defaults to HOLD.

---

## 7 · Reporting cadence

- After Step 1-9: short status updates as each gate is run · 1-2 lines each.
- After Step 10: the full `release-decision.md` document.
- If HOLD: explicit routing to the next workflow that closes the gap (A · B · C with scope).
- If SHIP: confirmation of the tier flip · the registry update · the regression-watch obligation.

---

## 8 · Closing reminder

A premium catalog is not a catalog of premium individual templates. It is a catalog of templates that REMAIN premium under public scrutiny, that DO NOT regress as the cluster grows, that DO NOT collapse into siblinghood under translation. The release decision is where all of that gets stress-tested in advance of the public seeing the page. The orchestrator's role here is not to ship faster — it is to ship only what survives the scrutiny that has already been priced into every standards rule. When in doubt, hold. The next pass is closer than the regression rollback would be.
