# Template orchestrator master prompt

**Use this prompt to create one new premium template, end-to-end, against the cluster standards.**
Paste it verbatim into a Claude Code session at the start of a workflow A pass. Replace the bracketed `<…>` slots in §0 with the real values from the user's brief or roadmap entry. Do not edit anything below §0 inline; deviations go in the per-pass report, not in the prompt.

This prompt is the binding contract for the pass. If a step here conflicts with anything you read at run time (a skill's recommendation, a habit from a prior session, an LLM training-data instinct), this prompt and the standards it references win.

---

## 0 · Run-time slots (fill before first turn)

```
template_slug:          <kebab-case-slug>
studio_name:            <brand name, single word preferred>
cluster:                <corporate-suite | medical-specialist | restaurant | portfolio | ecommerce | real-estate | law | agency | startup-saas | medical-other>
sub_cluster_label:      <one-phrase variant, e.g. "studio notarile">
audience_profile:       <1-2 sentences>
nearest_two_siblings:   <existing template names in this cluster nearest in palette/imagery/voice>
user_constraints:       <explicit must-have / must-avoid>
initial_locale:         it
initial_tier:           draft
report_root:            factory/reports/<archetype>/<template_slug>/
```

A blank slot is an unanswered question. Do not start work with a blank slot.

---

## 1 · Mandatory inputs (read in order, do not skip)

Before any tool call beyond reading, you MUST have read:

1. `design-orchestrator/ORCHESTRATOR.md` — orchestrator role, anti-drift list, the user's original goal restated in §7. Re-read §6.
2. `design-orchestrator/DISTINCTNESS_RULES.md` — the 4-of-5-axes gate and the cluster invariants table.
3. `design-orchestrator/BROWSER_QUALITY_GATE.md` — what blocks a flip and what the walk must produce.
4. `design-orchestrator/TEMPLATE_FACTORY_MODEL.md §3` — the nine-role spine for workflow A.
5. `design-orchestrator/SKILL_USAGE_POLICY.md` — what to load, when, and what to refuse.
6. `design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md` — what is already taken in this cluster (use the cluster's pack when one exists; corporate-suite is the only one today, others fall back to it as baseline).
7. `design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md` — the row-by-row matrix you will fill at A.2.
8. `design-orchestrator/references/internal-baselines/next-template-brief-schema.md` — the planner-brief contract you will use at A.2.
9. The cluster's standards under `factory/standards/<cluster>-*.md` — design, imagery, browser-rubric, blocking, scorecard, multi-agent-sop. Today only `corporate-suite-*` is complete; for other clusters, read corporate-suite + the cluster's `factory/cluster_blueprints/<cluster>.md` (if present) + the existing siblings' DNA entries.
10. The two nearest siblings' content modules and DNA entries.
11. The current `MEMORY.md` baseline pointer to confirm the catalog state has not moved.

If any of (1)-(11) is missing or unreadable, stop and surface the gap. Do not improvise.

---

## 2 · The non-negotiable anchors

These bind every step of the pass. They cannot be relaxed by any agent or skill.

| Anchor | What it means at this layer |
|---|---|
| **Distinct design DNA** | Palette · heading serif · hero meta-strip composition · voice anchor · structural moves all score ≥ 4/5 vs every existing sibling on the matrix in `corporate-suite-distinctness-matrix.md §1`. |
| **Distinct imagery DNA** | 6-slot Pexels pool, zero URL overlap with any other cluster pool (CS-IMG-SRC-04 grep · cross-cluster), distinct subject + mood + density + color-temperature from every sibling. |
| **Distinct section rhythm** | Mid-strip composition is freshly invented (not KPI tuple, not fiscal-calendar, not percorso-cadenza, not any sibling's). Section order differs from every sibling's home order on at least one beat. |
| **Premium visible outcome** | Generous padding (CS-RHYTHM-01) · serif italic-em emphasis (CS-TYPE-02) · one dark band (CS-TONE-03) · outline-on-cream + filled-on-dark CTA polarity (CS-CTA-01) · `:focus-visible` gold ring (CS-NAV-02) · tabular numerals (CS-TYPE-03) · zero AI-slop tells (`corporate-suite-reference-pack.md §9`). |
| **Browser-live validation** | Every gate verdict is grounded in the live DOM at the cluster's viewport matrix, not in screenshots, not in CLI green. The browser walk is the ship signal (`BROWSER_QUALITY_GATE.md §1`). |
| **Release-gate evidence** | Planner brief · pack file · copy diff · build CLI summary · style-critic + contrast + responsive reports · per-locale walk verdicts · scorecard · user-handshake · Pexels-only audit. All on file before any flip request. |

These six together are the pass. Drop any one and the pass is incomplete.

---

## 3 · The pass · nine roles, one path

You will not author across roles. You will route to one role, wait for its report, gate it, then route to the next. The orchestrator does not collapse into the agents (`AGENT_ROSTER.md §2`). For each step below, the canonical agent file is in `factory/agents/<slug>.md`; read it before invoking.

### A.1 · Intake (you · ~5 min)

Output: a one-page intake note at `<report_root>/intake.md`. Fill the slots in §0 above plus:
- two siblings nearest in palette/imagery/voice (for triangulation)
- "this template is NOT" — three explicit anti-positions referencing existing siblings
- planned locale list (start IT-only · D-102 cadence)
- planned scope (pages · components · expected line budget)

Gate: the intake note exists, every slot is answered, and `nearest_two_siblings` is populated. If you cannot name the two nearest siblings without ambiguity, the cluster is too thin — fall back to corporate-suite as baseline and document the gap.

### A.2 · Plan (template-planner · ~30 min)

Inputs: intake note · cluster reference pack · distinctness matrix · brief schema · cluster design standard.
Output: a planner brief at `<report_root>/planner-brief.md` filled to the schema in `next-template-brief-schema.md` §1-§10. Not part of the brief = blank slot = no sign-off.

Skills loaded for this step (per `SKILL_USAGE_POLICY.md §2`):
- `/impeccable shape` (one invocation, structure-then-build)
- `ui-ux-pro-max` searches: typography pairing, palette family, anti-pattern check
- `taste-skill` (default) for premium-tone reference

Gate: the brief's §6 distinctness scores all read ≥ 4/5 vs every existing sibling, the brief's §10 single-page summary is coherent and orchestrator-readable, and the AI-slop red-flag check is YES (clear). Any blank or vague field, any score < 4/5, any unwaivered hard prohibition (schema §2.1) → re-spec. Do not relax the gate.

### A.3 · Pack (imagery-curator · ~30-60 min)

Inputs: planner brief · cluster imagery standard.
Output: a pack file at `docs/content-factory/imagery/packs/<imagery_key>.md` plus a curator report at `<report_root>/pack-report.md`.

Gate: 6 slots, all `images.pexels.com/photos/...` URLs, zero URL overlap with any other cluster's pool (run the cross-cluster grep before claiming the pack passes), every slot has subject + mood + coherence-note + license metadata, hero subject is NOT one of the existing siblings' hero subjects, ambient slot is NOT a bookshelf if Fiscus already took it, portrait pair has visible diversity. The curator self-checks; you re-confirm; only then proceed.

### A.4 · Copy (copy-translation · IT only · ~30-60 min)

Inputs: planner brief (voice anchor verbatim · em-word identified) · pack file (so caption/alt copy can reference real subjects).
Output: IT locale tree at the seed path the cluster's `seed_templates.py` expects · the `template_dna.py` entry filled · a copy-diff report at `<report_root>/copy-it.md` with the voice anchor quoted and the em-word called out for translators.

Gate: voice anchor is verbatim from the brief, em-word is exactly the load-bearing word the brief named, no lorem ipsum / "Replace this text" / "Your headline here" anywhere (CS-MARKET-02/03), no marketing hyperbole banlist hits (CS-EXEC-04), credentials cited are real (CS-EXEC-03).

### A.5 · Build (template-builder · ~30-90 min)

Inputs: copy + pack + palette spec.
Output: skin under `apps/catalog/...`, DNA + seed + preview-imagery updates, CLI green (`python manage.py test apps.catalog` + the existing test suite + `generate_previews`), one openable IT live URL.

Gate: the suite is green and the live URL renders the full home + at least one secondary page without console errors. CSS uses the cluster prefix (`cs-` for corporate-suite, the cluster equivalent elsewhere). Logical properties for RTL readiness (CS-RESPONSIVE-08). Reduced-motion path implemented (`@media (prefers-reduced-motion: reduce)`). The known cluster fault lines from the reference pack §3 are addressed (e.g. `--primary-2` not introduced; `<720px` hero stack present).

### A.6 · Critique (style-critic + contrast-accessibility + responsive · in parallel · ~30 min total)

Inputs: live IT URL.
Outputs (per `SOP §6` schema, three reports at `<report_root>/critique-{style,contrast,responsive}.md`):
- Style critique against the design standard's `[BLOCKING]` and `[REQUIRED]` rules.
- Contrast report (CS-PAL-01/04 · CS-HERO-03 · `:focus-visible` · reduced-motion).
- Responsive report (full viewport matrix · no-horizontal-scroll · breakpoint behaviour · touch targets).

Skills loaded: `/impeccable critique` and `/impeccable audit` (cite findings against rule IDs, never against the skill's own vocabulary). Anti-pattern detector run against §9 of the cluster reference pack.

Gate: zero `[BLOCKING]` findings open. `[REQUIRED]` findings either fixed in A.8 or covered by an explicit `§ deviation` note in the planner brief.

### A.7 · Walk (browser-verifier · ~30 min · IT)

Inputs: live URL · cluster browser rubric.
Output: rubric verdict at `<report_root>/walk-it.md` with per-cell evidence (screenshots in `factory/reports/browser-verification/<template_slug>/it/`, DOM snippets, computed-style notes where contrast is at issue).

Gate: PASS authorises Commit A draft-landing. BORDERLINE → A.8 fix on the borderline cells, no scope expansion. FAIL with `[BLOCKING]` → A.8 fix; cannot land draft. No verdict on file → no flip ever, period.

### A.8 · Fix (template-editor-fixer · only on FAIL/BORDERLINE)

Narrowest possible diff, scope-locked to the failed cells. Does NOT author new content. Re-runs A.6 + A.7 on the affected dimension only. If the diff widens past the diagnosed surfaces, the pass is re-classified as workflow A and re-inherits its gates (this is the scope-creep trap; refuse to ship around it).

### A.9 · Aggregate (release-gatekeeper · then orchestrator · ~30 min)

Inputs: every report from A.2 - A.8.
Output: filled `corporate-suite-quality-scorecard.md` (or per-cluster equivalent) at `<report_root>/scorecard.md` · user-handshake artefact at `<report_root>/user-handshake.md` · a one-page commit summary citing every report.

Gate: ALL of the following true before requesting Commit A:
- planner-brief §6 scores ≥ 4/5 vs every existing sibling
- pack passes the cross-cluster URL grep
- copy contains the voice anchor verbatim, em-word preserved
- CLI suite green
- critique reports show 0 open `[BLOCKING]`
- walk verdict PASS
- scorecard layers 1/2/3 stamped
- AI-slop red-flag check clear

Commit A merges to integration with `TEMPLATE_REGISTRY.json` at `tier=draft`. Commit B (LIVE flip) is a SEPARATE pass — see `release-decision-orchestrator.md`.

---

## 4 · Stop conditions (the pass HALTS, not just slows)

The pass stops at any of the following. Stop means: do not proceed to the next role. Surface the condition. Do not patch around it.

1. **Distinctness collision · ≤ 3/5 vs any existing sibling.** Re-spec at A.2 or earlier. Do not let the build phase "fix it later" — by then the design is committed.
2. **Pack contains a non-Pexels URL on a new template.** No exception. The Pragma legacy is the only documented carve-out; no second exception without a user-signed waiver.
3. **Voice anchor authored in the build step.** If the anchor is not in the planner brief verbatim, the brief is incomplete. Return to A.2.
4. **A single session has authored copy AND palette AND imagery AND skin AND its own review.** This is Solaria-class by construction (`ORCHESTRATOR.md §6 rule 4`). Split the work or refuse to ship.
5. **Mid-pass invention of a new design rule.** New rules go into `factory/standards/` BETWEEN passes (`ORCHESTRATOR.md §6 rule 5`). Mid-pass is drift.
6. **A `[BLOCKING]` finding ignored or downgraded.** Blocking is blocking. The standard's rule ID does not move because the pass is tight on time.
7. **No browser walk verdict on file at A.9.** No verdict, no flip. No "we'll catch it post-flip." (`BROWSER_QUALITY_GATE.md §3`.)
8. **Skill recommendation cited as binding.** Skills inform; standards bind (`SKILL_USAGE_POLICY.md §3 rule 1`). Re-express any skill finding against a rule ID before it counts.
9. **The pass closes with more docs than visible product.** If the diff is mostly under `design-orchestrator/` or `factory/reports/` and the catalog has no new openable live URL, the pass was a process pass, not a product pass (`ORCHESTRATOR.md §6 rule 1`). Two consecutive process passes is a misallocation signal.
10. **The pass tries to ship multiple locales.** Workflow A is IT-only (D-102). EN/FR/ES/AR are workflow C — see `template-multilingual-orchestrator.md`.

When you stop, write the stop condition + cause + proposed re-route into `<report_root>/stop-<date>.md`. The next session reads it.

---

## 5 · What counts as failure even if tests are green

This is the Solaria lesson. CLI green is a lower bound, not a ship signal. The pass FAILS even with 506/506 / 834/834 / generate_previews succeeding if any of these are true on the live render.

1. **The hero h1 reads cream-on-cream, gold-on-gold, or any near-monochrome combination at ≤ 4.5:1 contrast.** CS-HERO-03 / CS-PAL-01. Tests do not see contrast.
2. **The page reads as a sibling rename.** First-30-second stakeholder summary is plausibly Pragma's, Fiscus's, or Solaria's (`corporate-suite-distinctness-matrix.md §1.12`). Distinct on paper, indistinct on impression.
3. **The hero photo is on the live page but renders as the wrong subject at the rendered crop.** Pack-approved at 1600px, broken at the actual viewport. `BROWSER_QUALITY_GATE.md §5.2`.
4. **A non-Pexels URL slipped into the live DOM.** `BROWSER_QUALITY_GATE.md §5.1`. Tests do not check the source domain.
5. **The voice anchor is on the page but the em-wrap is on the wrong word.** Translator picked a different word than the brief's em-word. `corporate-suite-reference-pack.md §3 R7`.
6. **Two adjacent sections share function** (CS-RHYTHM-04). Both decorative, both proof-bands, both CTAs. Rhythm flattens; the page reads as a list.
7. **Three or more accent uses per viewport** (CS-PAL-05). Accent inflation reads SaaS even when each individual use is "correct."
8. **AI-slop tells survive critique.** Inter on h1, purple gradient, cards-in-cards, gray-on-colored-bg, "Get started free" CTA, mountain-peak hero, Einstein quote. The detector list in the cluster reference pack §9 is the canonical fail set.
9. **Editor-only affordances leak into `/live/`** (CS-MARKET-01). The `body.mw-is-editor-preview` guard is missing somewhere in the chrome.
10. **Mobile (≤ 720px) shows horizontal scroll, hero is still horizontal, or footer does not stack.** CS-RESPONSIVE-01 · CS-HERO-07 · CS-FOOT-05. The cluster has historical fault lines here (`reference-pack §3 R2`).
11. **Locale switcher does not change `lang` and `dir` on the link** (CS-NAV-03). Tests do not click locale links; the walk does.
12. **The page survives the "remove the studio name" test as a generic.** If you delete the studio name and the page works as ANY firm in the cluster, it is a generic, not a sibling. CS-TONE-05 / `reference-pack §8`.

A green CLI plus any one of these = FAIL. Surface it as a `[BLOCKING]` finding at A.6 or A.7, do not merge to draft, and route to A.8.

---

## 6 · What the next sibling must not repeat

Read this section EVERY pass. It is the cumulative anti-clone list, populated from every prior sibling. The list is monotonic — items are added when a sibling lands, never removed. The cluster's reference pack §1 and the distinctness matrix §1.1-§1.12 are the canonical source.

For corporate-suite as of 2026-04-29 the binding "must not repeat" set is:

**Tone / voice anchor**
- Pragma's "decisional gravity" framing
- Fiscus's "presidio + scadenze-first" framing
- Solaria's "non-terapia non-consulenza" bounded-method framing
- Two em-wraps in a heading unless the anchor is a contrast pair (Solaria's exception, not the default)

**Palette**
- Slate-blue + emerald family (Pragma adjacency)
- Warm-neutral + gold + blu-notte family (Fiscus adjacency)
- Warm-carbon + ocra + caramel family (Solaria adjacency)
- A second blue+gold combination (Fiscus has it)
- Bright pure red/orange/yellow at full saturation (reads SaaS)

**Typography**
- Inter as body sans (taken twice — Pragma + Solaria — third use collapses the cluster)
- IBM Plex Sans body (Fiscus)
- Merriweather, IBM Plex Serif, Fraunces as heading
- Montserrat, Poppins, Raleway on headings (CS-TYPE-01)

**Hero composition**
- 55/45 hero shape change (the silhouette is a cluster invariant — keep it)
- Pragma's KPI tuple as meta-strip
- Fiscus's fiscal-calendar-strip
- Solaria's percorso-cadenza-strip
- `(Direzione, Anno fondazione)` as the hero credit overlay (used twice)

**Imagery**
- Boardroom long-table hero (Pragma)
- Tidy desk + documents hero (Fiscus)
- 1:1 conversation hero (Solaria)
- Bookshelf as ambient slot (Fiscus took it)
- Two 30s Caucasian portraits as slots 2-3 (Solaria already)
- Any URL appearing in `business-corporate`, `business-fiscal`, `business-coaching` (cross-cluster grep · CS-IMG-SRC-04)

**CTA**
- "Fissa una call privata" / "Primo appuntamento" / "Prenota una discovery call"
- "Get started free" / "Sign up now" / "Iscriviti gratis" (CS-CTA-02)
- A form gate asking for both P.IVA + CF (Fiscus's intake shape)

**Section rhythm**
- Pragma's exact section order (no mid-strip + leadership present)
- Fiscus's `fiscal-calendar` mid-strip
- Solaria's `manifesto` opener replacing pillars AND/OR `method-cadenza` mid-strip
- KPI count > 4 or < 3 · pillar count > 4 or < 3 (CS-DENSITY-04 / 02)
- Wall-of-text "Our Story" opener (CS-COMP-06)

**Leadership / proof**
- Pragma / Fiscus / Solaria credential vocabularies verbatim
- Any fake credential (CS-EXEC-03)
- "Casi seguiti" / "Casi anonimizzati" / "Case studies" as cases-list label without fresh framing
- Solaria's "Aziende sponsor recenti" trust-band label

**For other clusters** (medical-specialist, restaurant, portfolio, ecommerce, real-estate, law, agency, startup-saas, medical-other): until a per-cluster reference pack exists, the existing siblings' DNA entries + the corporate-suite list above (where structurally equivalent) are the must-not-repeat set. The first task in any new-cluster pass is to extract the cluster's must-not-repeat list from existing siblings before A.2 begins.

When this pass closes, append this template's distinguishing claims to the cluster's reference pack §1 and distinctness matrix §1.1-§1.12 so the NEXT sibling reads them as must-not-repeat. The list is the cluster's monotonic memory.

---

## 7 · Reporting cadence (what you write back to the user, when)

- After A.1: 1 paragraph · "intake landed, planning starting, gates lined up."
- After A.2: 1 paragraph · brief sign-off summary from `next-template-brief-schema.md §10`. If gate fails, surface specific failing scores.
- After A.3: 1 paragraph · "pack approved · 6 Pexels URLs · cross-cluster grep clean · curator report at <path>."
- After A.5: 1 paragraph · "build green · CLI 375/375 · IT live URL openable at <url>."
- After A.7: 3-6 lines · walk verdict + per-cell summary + screenshot directory.
- After A.9: the user-handshake document · contains the evidence pack and asks ship-or-hold for Commit A.

No essay-length status updates between steps. The reports ARE the durable record (`TEMPLATE_FACTORY_MODEL.md §6`); the chat output is the routing.

---

## 8 · One-paragraph closing reminder

The user's goal is hundreds of customizable templates, all clearly different from each other, premium · elegant · modern · professional · dynamic · browser-live verified · scalable without quality loss (`ORCHESTRATOR.md §7`). This prompt exists to make that goal more likely on this one pass. If you find yourself producing more docs than openable live URLs, citing skills as binding, mid-pass-inventing rules, or relaxing a gate "just for this template," you are drifting. Stop, surface, re-route. The standards and the live walk are the two things that survive a tight calendar; everything else is negotiable.
