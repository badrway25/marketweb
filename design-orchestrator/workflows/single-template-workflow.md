# Single template workflow

The concise lifecycle for one template, idea → release decision. This is the operational checklist for a single workflow A pass on one new template, plus the followup C and release pass.

For batch processing, see `batch-template-workflow.md`. For improving an existing template, see `template-edit-orchestrator.md`. For multilingual rollout of an existing IT template, see `template-multilingual-orchestrator.md`.

---

## 0 · The full lifecycle in one diagram

```
idea
 │
 ▼
intake checklist filled         (template-intake-checklist.md)
 │
 ▼
master orchestrator pass        (template-orchestrator-master.md)
 │
 │   A.1 intake → A.2 plan → A.3 pack → A.4 copy → A.5 build →
 │   A.6 critique → A.7 walk → (A.8 fix?) → A.9 aggregate
 │
 ▼
Commit A landed                 tier=draft · IT-only · live URL openable
 │
 ▼
multilingual orchestrator pass  (template-multilingual-orchestrator.md)
 │
 │   C.1 pre-flight → C.2 translate → C.3 build → C.4 per-locale walks → C.5 aggregate
 │
 ▼
all locales walked PASS
 │
 ▼
release decision orchestrator   (release-decision-orchestrator.md)
 │
 │   gates 1-10 · user handshake · gatekeeper scorecard
 │
 ▼
SHIP → tier=published_live      (or HOLD → re-route to A / B / C)
 │
 ▼
regression-watch surface        (BROWSER_QUALITY_GATE.md §7)
```

Total elapsed time per template: ~1-2 working days for the IT pass plus ~1 day for multilingual plus ~½ day for release-decision evidence assembly and handshake. Faster than this is a sign the gates were skipped.

---

## 1 · The five sessions of one template

A single template typically spans 5 distinct Claude Code sessions (or focused work blocks if batched). Treating them as separate sessions enforces the role boundaries in `AGENT_ROSTER.md §2`.

| # | Session | Prompt to paste | Output |
|---|---|---|---|
| 1 | Intake + plan + pack | `template-orchestrator-master.md` (steps A.1-A.3) | intake.md · planner-brief.md · pack file |
| 2 | Copy + build | `template-orchestrator-master.md` (steps A.4-A.5) | IT locale tree · DNA entry · CLI green · live IT URL |
| 3 | Critique + walk + (fix?) + aggregate | `template-orchestrator-master.md` (steps A.6-A.9) | three critique reports · walk verdict · scorecard · Commit A |
| 4 | Multilingual rollout | `template-multilingual-orchestrator.md` (full pass) | per-locale copy · per-locale walks · multilingual-summary.md |
| 5 | Release decision | `release-decision-orchestrator.md` (full pass) | release-decision.md · user-handshake · tier flip OR documented hold |

Sessions 1-3 are a single workflow A pass split for working-memory reasons, NOT a relaxation of the agent boundary discipline. Sessions 4 and 5 are separate workflows by design.

---

## 2 · The gates, in order, as a checklist

For each template you walk through, every box must be checked before the next box can be addressed. This is the operational version of the gate sequence from the master orchestrator prompt.

### Pre-build gates
- [ ] Intake checklist filled · all fields answered · no blanks
- [ ] Two nearest siblings named unambiguously
- [ ] User constraints captured · explicit must-have / must-avoid
- [ ] Cluster reference pack and distinctness matrix read (corporate-suite is the only cluster with these on file today; for any other cluster, build the pack FIRST per intake §0.5)
- [ ] **Pre-build quick-checks** all clear (`workflows/pre-build-quick-checks.md`):
  - [ ] §1 cluster reference-pack precondition: CONTINUE (or USER-WAIVER recorded)
  - [ ] §2 palette warmth/coolness grid: PASS (0-1 cell overlap vs every sibling)
  - [ ] §3 imagery feasibility quick-search: GO (every slot ≥ 5 plausible candidates)
  - [ ] §4 content-volume estimate: CONTINUE (inside cluster typical range, no beat > 50%)
  - [ ] §5 "remove the studio name" pre-test: PASS at intake §3.2 AND at planner brief §10
- [ ] Planner brief filled to schema · §10 single-page summary coherent
- [ ] Distinctness matrix scored ≥ 4/5 vs every existing sibling
- [ ] AI-slop red-flag check clear
- [ ] Imagery feasibility re-confirmed at A.2.5 against the brief's expanded subjects
- [ ] Imagery pack drafted · curator-approved · 6 Pexels URLs
- [ ] Cross-cluster URL grep clean

### Build gates
- [ ] IT copy authored from voice anchor verbatim · em-word preserved
- [ ] Skin built · CSS uses cluster prefix · logical properties for RTL
- [ ] CLI green: `python manage.py test apps.catalog` + suite + `generate_previews`
- [ ] IT live URL openable · home + ≥ 1 secondary page · zero console errors
- [ ] Known cluster fault lines addressed (`reference-pack §3 R1-R7`)

### Verification gates
- [ ] Style critique against design standard · 0 open `[BLOCKING]`
- [ ] Contrast/accessibility report PASS at all viewports
- [ ] Responsive report PASS at all viewports · no horizontal scroll · footer stacks at 720
- [ ] IT walk verdict PASS · 6+ captures on file
- [ ] Editor-only affordances confirmed hidden on `/live/`

### Aggregation gates (Commit A)
- [ ] Scorecard filled · Layer 1 / 2 / 3 stamped · grade ≥ 4.50/5
- [ ] Reports tree complete at `factory/reports/<archetype>/<template_slug>/`
- [ ] `TEMPLATE_REGISTRY.json` updated to `tier=draft`
- [ ] Commit A merged to integration branch

### Multilingual gates
- [ ] Pre-flight 8 checks PASS
- [ ] Voice anchor preserved per-locale on equivalent em-word
- [ ] All target locales translated · credentials per locale verified
- [ ] AR Kufi/Amiri swap working on live render
- [ ] Per-locale walks PASS · AR has the RTL parity walk
- [ ] Cross-locale Pexels-only re-confirmed on live DOM

### Release gates
- [ ] All cluster `[BLOCKING]` rules satisfied
- [ ] Walks fresh (≤ 30 days) · PASS on every locale in scope
- [ ] Live DOM still matches planner brief
- [ ] Distinctness still ≥ 4/5 vs every sibling
- [ ] Pexels-only on live render · all locales
- [ ] Editor affordances hidden across home + secondary pages
- [ ] AI-slop red flags clear on every locale
- [ ] User-handshake signed SHIP
- [ ] Gatekeeper scorecard stamped · all three layers PASS
- [ ] Conservative override not invoked

The 40+ checkboxes look like a lot. They are. The Solaria precedent showed what happens when 5-10 of them are silently skipped. The single-template workflow is what makes the gates feel routine instead of heavy.

---

## 3 · Per-stage reporting

The reports written at each stage become the durable record. Every report has a canonical home:

```
factory/reports/<archetype>/<template_slug>/
  intake.md
  planner-brief.md                 (filled to next-template-brief-schema.md)
  pack-report.md
  copy-it.md
  build-summary.md
  critique-style.md
  critique-contrast.md
  critique-responsive.md
  walk-it.md
  scorecard.md
  user-handshake.md
  multilingual-<YYYY-MM-DD>/
    preflight.md
    copy-en.md  copy-fr.md  copy-es.md  copy-ar.md
    walk-en.md  walk-fr.md  walk-es.md  walk-ar.md
    multilingual-summary.md
  release-<YYYY-MM-DD>/
    release-decision.md
  edit-<YYYY-MM-DD>/                (one per workflow B pass on this template)
    diagnose.md
    scope-lock.md
    walk-edit.md
    edit-summary.md

factory/reports/browser-verification/<template_slug>/
  it/<YYYY-MM-DD>/<captures>
  en/<YYYY-MM-DD>/<captures>
  fr/<YYYY-MM-DD>/<captures>
  es/<YYYY-MM-DD>/<captures>
  ar/<YYYY-MM-DD>/<captures>
```

When a future pass touches this template (edit · re-walk · regression), this tree is what it reads. Treat it as the template's permanent file, not as session scratch.

---

## 4 · Common single-template stop points

The single-template lifecycle most commonly halts at:

1. **A.2 distinctness re-spec.** The planner brief comes back with a 3/5 score against an existing sibling. Re-spec the offending dimensions (palette, hero meta-strip, voice anchor — typically one of these is the culprit). One re-spec round is normal; two means the cluster is too saturated for this slot and the template needs re-scoping.

2. **A.3 cross-cluster grep failure.** The curator picked a Pexels URL that already lives in another cluster's pool. The fix is one URL swap; the lesson is that curators must run the grep BEFORE committing.

3. **A.7 walk BORDERLINE on contrast.** Most common single defect. CS-HERO-03 / CS-PAL-01 fail on a specific viewport. Workflow A.8 fix is narrow. Re-walk on the one viewport.

4. **C.4 AR walk RTL parity miss.** The chrome was not as RTL-ready as pre-flight thought. Pause C, open A on chrome, re-enter C when chrome lands. AR is the most expensive locale to half-ship.

5. **Release step 8 user-handshake HOLD.** The user sees the live page and notices something the rubric did not flag. Per the conservative-default policy, this HOLD is recorded without justification and routes to the appropriate B pass.

6. **Intake §0.5 HALT (cluster reference pack missing).** Cluster ≠ corporate-suite and the pack/matrix is not on file. Intake stops; the next pass builds the cluster's reference pack first.

7. **Intake §3.1 palette warmth grid RESPEC.** Hex distinct but warmth topology overlaps a sibling on ≥ 2 roles. Re-shape secondary or accent temperature before continuing.

8. **Intake §6.5 imagery feasibility RESPEC.** A slot returns ≤ 2 plausible Pexels candidates on the orchestrator's quick search. Soften that slot's subject at A.2 before A.3.

These eight account for the majority of stops; if a template stops at a different point, look first at whether the upstream gate was actually run with discipline.

---

## 5 · Closing reminder

A single template traverses ~9 roles, produces ~15 reports, and clears ~40 gates before reaching `published_live` in 5 locales. That cadence is what produced the Solaria-grade and Pragma-grade and Fiscus-grade templates the cluster ships today. Faster than this is the failure mode that produced the Solaria `e8f38b5` defect — 1148 lines, 506 tests passing, every heading rendered cream-on-cream. The 30 minutes the browser walk would have spent caught what 650 automated checks did not. This workflow's job is to make those 30 minutes routine.
