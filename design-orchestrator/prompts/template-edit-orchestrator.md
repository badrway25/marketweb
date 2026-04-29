# Template edit orchestrator prompt

**Use this prompt to improve an existing template without losing its identity.**
Paste it verbatim into a Claude Code session at the start of a workflow B pass. Replace the bracketed `<…>` slots in §0. This prompt is binding for the pass — anything that conflicts with it (a skill suggestion, a habit from the build pass, an instinct to "tidy while you're in there") is rejected.

Edit passes are seductive. They feel small, scoped, contained. They become Solaria-class when one "small" edit cascades into untested surfaces. The rule throughout: **walk before plan, scope-lock before edit, narrowest diff possible**.

---

## 0 · Run-time slots (fill before first turn)

```
template_slug:           <existing template slug>
cluster:                 <cluster name>
current_tier:            <draft | review-ready | published_live>
locales_affected:        <subset of [it, en, fr, es, ar]>
defect_summary:          <one sentence: what is wrong and where>
defect_source:           <user report | regression watch | new standards rule | reviewer feedback>
report_root:             factory/reports/<archetype>/<template_slug>/edit-<YYYY-MM-DD>/
last_walk_verdict_path:  <path to most recent rubric verdict on file>
last_walk_age_days:      <integer · if >30, walk re-runs at B.1>
```

---

## 1 · Mandatory inputs (read in order)

1. `design-orchestrator/ORCHESTRATOR.md §6` — anti-drift rules. Re-read every pass.
2. `design-orchestrator/TEMPLATE_FACTORY_MODEL.md §4` — workflow B canonical sequence.
3. `design-orchestrator/BROWSER_QUALITY_GATE.md §7` — post-LIVE regression watch.
4. `design-orchestrator/SKILL_USAGE_POLICY.md §2` — surgical-lift decision tree (the section "Post-build · the template feels generic").
5. The cluster's `factory/standards/<cluster>-blocking-rules.md` and `<cluster>-design-standard.md` — the rule IDs your diagnosis must cite.
6. The template's most recent planner brief at `factory/reports/<archetype>/<template_slug>/planner-brief.md` — to re-anchor on the original identity.
7. The template's most recent walk verdict — to know what was last verified PASS.
8. `corporate-suite-distinctness-matrix.md §1.1-§1.12` (or cluster equivalent) — to confirm the edit will not collapse this template into a sibling.

---

## 2 · Diagnose the issue class (this is the single most important step)

Before any edit, classify the defect into exactly ONE of three classes. The class determines who fixes it, what surface is allowed to change, and what the fixed version is verified against.

### Class I · Archetype-level issue

The defect is in the cluster's shared skin / chrome / contract. Every sibling in the cluster either has it or would have it on the next build.

**Examples:**
- `--primary-2` hardcoded in `_base.html` (`reference-pack §3 R1`)
- `<720px` hero stack missing across the cluster (`reference-pack §3 R2`)
- Footer does not stack at 720px (CS-FOOT-05 missing)
- `body.mw-is-editor-preview` guard absent in a chrome partial (CS-MARKET-01 family)
- A new `[BLOCKING]` rule was added to the standard and existing siblings now violate it

**Routing:** this is a workflow A on the chrome / shared partial. Open it as such — it inherits A's full gate set on every affected sibling. Do NOT smuggle a chrome change into a single-template edit pass; the test surface is too narrow to catch the cluster-wide effects.

**Verification:** every existing published sibling re-walks on the touched surface before any flip. The cluster's regression-watch obligation (`BROWSER_QUALITY_GATE.md §7`) binds.

### Class II · Sibling-specific issue

The defect is unique to this template OR a property this template shares with one specific other sibling. The fix must NOT erode this template's distinctness vs the cluster.

**Examples:**
- The hero meta-strip on this template happens to read like Pragma's KPI tuple under translation
- This template's palette drifted into Solaria adjacency in a recent imagery refresh
- The voice anchor here echoes another sibling's after a copy-edit pass
- Two adjacent sections share function (CS-RHYTHM-04) because this template added a beat that another sibling already owns

**Routing:** workflow B as documented in `TEMPLATE_FACTORY_MODEL.md §4`, but B.1 includes a re-run of `corporate-suite-distinctness-matrix.md` for this template specifically. The fix is judged on TWO axes simultaneously: does it close the defect AND does it preserve / restore distinctness scores ≥ 4/5 vs every sibling.

**Verification:** post-fix walk re-checks the failing rule IDs AND re-scores the matrix. If the fix closes the rule but lowers a matrix axis to ≤ 3/5, the fix is rejected — the cure became a new collision.

### Class III · Template-local issue

The defect lives entirely inside this template's own surfaces (its content module, its DNA entry, its specific copy/imagery slots). It does not implicate the cluster, does not implicate any other sibling, and does not change the template's identity.

**Examples:**
- A typo in IT copy
- A locale tree missing one credential value
- A specific image slot's URL returns 404 (replace within the same Pexels coherence band)
- A KPI figure was wrong and needs correcting (with verification of the new figure's source)
- A specific page's contrast violation tied to one element

**Routing:** workflow B, narrowest diff. No cluster-wide implication, no distinctness re-score required (but verify the matrix did not move as a side effect).

**Verification:** post-fix walk re-checks the failing surface only. The fixed verdict is appended to the template's report tree without invalidating the prior walk.

---

## 3 · The pass · workflow B steps with the issue-class hooked in

### B.1 · Diagnose (orchestrator + style-critic + browser-verifier · live walk first · ~30 min)

Output a short diagnostic note at `<report_root>/diagnose.md` with:
- The defect, in one sentence.
- The issue class (I, II, or III) with rationale citing specific rule IDs / matrix cells.
- Pages affected · locales affected · severity (`[BLOCKING]` / `[REQUIRED]` / `[STRONG]`).
- The "is this an edit pass or does it need re-planning?" verdict.
- For Class II: a fresh `corporate-suite-distinctness-matrix.md` row for this template, scored against every existing sibling, BEFORE the edit.

If `last_walk_age_days > 30` OR `current_tier == published_live`, the diagnose step re-runs the walk on the affected surface fresh. Stale verdicts do not satisfy the gate (`BROWSER_QUALITY_GATE.md §3`).

### B.2 · Scope-lock (orchestrator · 5 min)

Output a scope statement at `<report_root>/scope-lock.md`:
- The exact file(s) that will change. Listed by path. Anything not on the list is out of bounds.
- The specific rule IDs and matrix cells that will be re-tested afterwards.
- Whether this can ship under the existing brand identity (`scope=local`) or requires planner re-engagement (`scope=identity-touching` → upgrade to workflow A).

The scope-lock is the brake. An edit that touches more than the listed files becomes workflow A and inherits its full gates (`TEMPLATE_FACTORY_MODEL.md §4 anti-drift trap`). Refusing to widen scope is the entire point of this step. If a fixer comes back saying "I need to also touch X", the answer is either:
- "X is not in the diagnosis · open a separate edit pass for X", OR
- "X reveals a Class I issue · this is now a chrome workflow A pass."

### B.3 · Edit (template-editor-fixer · narrowest diff · ~variable)

Inputs: scope-lock note · planner brief (to re-anchor identity) · cluster standard (to cite rule IDs).
Output: minimal diff · CLI green · live URL still openable at the same path.

Skill assists allowed (advisory only · `SKILL_USAGE_POLICY.md §2`):
- Typography problem → `/impeccable typeset`
- Layout / spacing problem → `/impeccable layout`
- Contrast / color problem → `/impeccable colorize` (advisory · CS-PAL-* binds)
- Excessive boldness for the cluster → `/impeccable quieter`
- Excessive blandness for the cluster → `/impeccable bolder`
- Final polish before re-walk → `/impeccable polish` (one invocation, surgical, do not run the full surface)

**Never** run all of these on the same pass. One surgical lift per dimension. Five lifts at once = rebuild = workflow A.

### B.4 · Re-walk (browser-verifier · same locales as diagnosis · scoped)

The re-walk targets the failed rule IDs from B.1 specifically. It does NOT re-walk the entire surface unless the fix touched chrome (which makes it Class I, which makes it workflow A).

Output: scoped verdict at `<report_root>/walk-edit.md`. Per-cell evidence on the previously failing cells. Confirmation that previously-passing cells were not regressed.

For Class II: the post-edit distinctness matrix is re-scored. If any axis dropped to ≤ 3/5, the edit is rejected even if the original defect closed.

### B.5 · Aggregate (release-gatekeeper + orchestrator)

Inputs: diagnose · scope-lock · edit diff · walk-edit · (for Class II) re-scored matrix.
Output: `<report_root>/edit-summary.md` with:
- The defect · the class · the diff · the verified rule IDs that now pass
- Any side-effects observed and their resolution
- The user-handshake artefact (only if the original template was at `published_live` — hot-fix flips need a fresh handshake)

If the template was at `draft`, this is just an iteration of workflow A and the next pass is the eventual flip request. If the template was at `published_live`, the gatekeeper authorises a hot-fix flip after the user handshake. If the template was at `review-ready`, the edit re-positions it as `draft` if any `[BLOCKING]` was found, otherwise stays at `review-ready`.

---

## 4 · Stop conditions

The edit pass HALTS at any of these:

1. **The diagnosis cannot pick exactly one issue class.** If it could be Class I or Class II, the safer routing is Class I (workflow A on chrome). If it could be Class II or Class III, the safer routing is Class II. Ambiguity defaults to the wider gate, never the narrower.
2. **The scope-lock is rejected by the fixer ("I need to touch X too").** Reopen at B.2; do not let the fixer widen unilaterally.
3. **The diff touches the cluster chrome.** Stop the edit pass; open a workflow A on the chrome. Cluster-wide changes do not ride a single-template pass.
4. **A skill is recommending edits the standard forbids.** Standards bind. `SKILL_USAGE_POLICY.md §3 rule 1`.
5. **Class II fix closes the defect but lowers a distinctness axis to ≤ 3/5.** The cure is a new collision. Re-spec or escalate to workflow A re-plan.
6. **Last walk is older than 30 days AND the fixer wants to ship without a fresh walk.** No verdict, no flip (`BROWSER_QUALITY_GATE.md §3`).
7. **The template was `published_live` and the hot-fix attempt would touch ≥ 3 dimensions.** Three-dimension hot-fixes are rebuilds; revert to draft and run workflow A.
8. **The edit pass closed and produced no openable live URL change.** Edit-pass-as-process is a drift signal. Real defects produce visible diffs.

When you stop, write the stop condition into `<report_root>/stop-<date>.md`. Surface to user.

---

## 5 · What over-editing looks like (refuse it)

These are the patterns that destroy distinctness while feeling like polish:

- **"While I'm in here, I'll also..."** Touching surfaces outside the scope-lock. The cure is harder to undo than the defect.
- **Replacing the voice anchor "to make it cleaner."** The anchor is identity (CS-EXEC-01). It does not get edited in a B pass without a planner re-engagement.
- **Refreshing the imagery pack "to make it more premium."** Pack changes are workflow A on the imagery dimension; they shift mood and density and require the matrix re-score.
- **Tightening padding "to fit more on screen."** Generous padding IS the rhythm (CS-RHYTHM-01). Compressing it is the most common silent quality loss (`reference-pack §2`).
- **Swapping the heading serif "for a more modern feel."** The heading serif is on the matrix (axis 4). Swapping it during an edit is an identity change.
- **Adding a sixth pillar / fifth KPI "for richness."** CS-DENSITY-02 / 04 cap these. The rule is the cap.
- **Migrating from outline-on-cream to filled-on-cream CTAs "for clarity."** Already ratified (CS-CTA-01 § decision). Do not re-litigate per pass.
- **Running every Impeccable command on the page "for thoroughness."** The full surface produces volumes; one surgical lift per dimension is the policy (`DESIGN_SYSTEM_WORKFLOW.md §7`).
- **Promoting a `[STRONG]` to `[BLOCKING]` because the diff is small.** Severity is set by the standard, not by the convenience of the moment.

When in doubt: smaller diff. The Solaria precedent — and most B.4 borderline-to-pass moves — favoured the surgical edit over the refresh.

---

## 6 · What "preserve identity" concretely means

Identity for a corporate-suite template is the matrix row in `corporate-suite-distinctness-matrix.md §1.1-§1.12`: tone label · palette polarity · accent warmth · typography personality · hero meta-strip composition · imagery direction · CTA personality · section rhythm · leadership feel · proof style · motion feel · stakeholder impression. Twelve cells. The edit pass MUST end with the same twelve cells reading the same way (or a single cell intentionally moved with planner sign-off).

Operational test before merging:
- Open the template's planner brief.
- Open the live URL.
- Ask "is this still the template described in the brief?"
- If yes, ship. If "kind of," reject the edit. "Kind of" is the Solaria-grade fail under polish framing.

---

## 7 · Reporting cadence

- After B.1: 1 paragraph · the issue class verdict + the rule IDs at fault + scope intent.
- After B.2: 1 paragraph · scope-lock confirmed, files listed.
- After B.3: 1 paragraph · diff stats + CLI status + live URL still openable.
- After B.4: 3-6 lines · re-walk verdict + per-cell summary + (Class II) matrix re-score.
- After B.5: edit-summary.md path + flip request (if applicable) + user-handshake.

The reports are the durable record. The chat output is the routing.

---

## 8 · Closing reminder

Edit passes preserve the catalog's quality compounding. Done well, they keep templates ageing gracefully and let the cluster absorb new standards rules without rebuilds. Done badly, they erode identity one "while-I'm-in-here" at a time. The discipline is not in the diff — it is in the scope-lock at B.2 and the "is this still the template?" check at B.6. Hold both, and an edit pass closes faster than the rebuild it replaced.
