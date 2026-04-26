# summary · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` · IT-only · pass 1 of a planned 3-pass closure
**Run-ISO**: `20260426T0907Z`
**Branch**: `phase-x4-solaria-controlled-reentry-pass1`
**Aggregator**: `release-gatekeeper` (Claude Opus 4.7)
**Pass-1 verdict**: **APPROVED-PASS-1** (NOT `APPROVED-PUBLIC-LIVE`).

---

## §1 · One-paragraph summary

Solaria pass 1 re-introduces the Wave 2 Pilot #2 IT content tree (paused at `e8f38b5` + palette polarity-fix at `6b70d56`) into the GO-bar corporate-suite archetype on a fresh controlled-reentry branch. Seven files touched (~1150 LOC added, 947 of which are the IT content tree; 0 deletions; 0 edits to apps/editor / apps/projects / apps/commerce / models / migrations / urls / views / skin folder). Solaria seeds at `tier=draft` so the public catalog count remains 21. Build-time gates pass: `corporate_suite.E001` (palette `#2B2A28` luminance 0.024 contrast 12.56 AAA), `corporate_suite.E002 / E003` (Pexels-only `business-coaching` 6-URL canonical pool). Tests stay at 171 / 171 OK in 2.438 s. The 7-cell live walk under reduced-motion emulation produces 0 BLOCKING / 0 REQUIRED on every cell. The aggregator's Layer 1 (18 blocking overrides) clears 0 / 18 triggered. The aggregate score is 4.67 / 5; the only sub-floor reading is D14 = 3 due to the intentional IT-only scope per binding D-102 cadence — the closure path is pass 2 (4 locale trees + walks) and pass 3 (full 5-locale × 6-page × 4-viewport matrix + tier flip + cascade).

## §2 · Field-proof for the AP8 pipeline

The Fiscus AP8 first run (P1C) was the bootstrap pass — every report shape produced for the first time, the editor-fixer leg exercised on a real defect (mp-back focus-visible whitelist), the gatekeeper aggregator producing the first PASS verdict using blocking overrides not average-score optimism. **Pass 1 on Solaria is the second AP8 instance, on a NOT-yet-shipped template.** Three things this run validates that Fiscus could not:

1. **The pipeline runs identically on a third corporate-suite enrollee** — every report shape exists, every check has a result, every § deviation is logged at the right altitude. No new prompt was authored to accommodate Solaria; the Fiscus-first-run prompts produced Solaria-pass-1 output without modification.
2. **The build-time gates protect a never-shipped template at re-entry time** — the Solaria Commit A `#F7F3EC` cream-as-primary regression class IS contract-blocked by `corporate_suite.E001`, but the pass-1 SEED_TEMPLATES entry uses the Commit B fix `#2B2A28`, so the gate is silent (correct outcome).
3. **The R-SOL rule grid is operational** — every R-SOL-1 → R-SOL-15 rule has a recorded pass-1 status (re-entry narrative §3). R-SOL-7 (port hygiene), R-SOL-10 (O7 citation), R-SOL-11 (D-054 reciprocal triangulation), R-SOL-12 (palette gate), R-SOL-13 (Pexels-only NOT grandfathered) are all green.

## §3 · Three real value-adds the pass-1 run surfaced

1. **The default-motion screenshot capture mechanism gap surfaces uniformly on every long-form page**, NOT just on the Fiscus retro-walk. Switching to `page.emulateMedia({reducedMotion: 'reduce'})` for `fullPage: true` captures is the right archetype-level browser-walker convention. (Same § deviation 3 as the GO reassessment §2.2 — pass-1 confirms the issue is archetype-wide, not Fiscus-specific.)
2. **The CS-BLOCK-17 (extended) palette-safety patch carries through to a third enrollee with zero per-template tuning** — the Solaria nav, KPI band, CTA, and footer all paint `--on-dark` cream on Solaria's `#2B2A28` primary at 12.56 AAA, the same ratio Pragma + Fiscus produce on their respective primaries. **The contract is shape-checked by the live walk, not by visual inspection alone.**
3. **The Pragma-side D-054 docstring stayed valid** at re-entry time — the P1D refresh that made Pragma + Fiscus three-template-ready (vs Solaria-as-placeholder) holds without further edit because Solaria's own docstring at `e8f38b5` already encodes the reciprocal 10-gate vs both siblings. **R-SOL-11 satisfied with zero pass-1 docstring edits.** This is the strongest evidence yet that the three-template-ready triangulation is a durable cross-template shape, not a one-shot per-enrollment chore.

## §4 · § deviations the pass-1 run surfaces (forward-going work)

These are tracked deferrals, NOT pass-1 blockers.

1. **D14 = 3 by IT-only scope** — pass 2 lands EN/FR/ES/AR (lifts D14 to ~4); pass 3 closes the full matrix (lifts to 5).
2. **D13 = 4 by 3-viewport sample** — pass 3 will add the full 8-viewport sweep at every locale (lifts to 5).
3. **Reduced-motion force-reveal capture-mechanism** — same archetype-level concern from GO reassessment; the pass-1 walker uses `emulateMedia` workaround. Step 3 prompt-revision can either codify this in the browser-verifier prompt or introduce a `?force-reveal=1` URL flag.
4. **Pragma legacy grandfather (O7)** — cited verbatim per R-SOL-10. The retro-curation backlog (T-P2-1) remains deferrable-past-Solaria per plan §5.
5. **`imagery-curator-reviewer` + `copy-translation` prompts folded inline into the gatekeeper aggregator** — same Step 3 prompt-revision item from the Fiscus AP8 first run. Not pass-1-gating.

## §5 · Files changed in pass 1

```
M  TEMPLATE_REGISTRY.json                                ( +~30 lines, Solaria entry · tier=draft · post-fix palette)
M  apps/catalog/management/commands/seed_templates.py    ( +~75 lines, TEMPLATE_METADATA + SEED_TEMPLATES rows)
M  apps/catalog/preview_imagery.py                       ( +~20 lines, business-coaching 6-URL Pexels pool)
M  apps/catalog/template_content.py                      ( +~10 lines, SOLARIA_CONTENT_IT import + dict entry)
M  apps/catalog/template_dna.py                          ( +~65 lines, solaria-coaching DNA on corporate-suite)
M  apps/catalog/tests.py                                 ( +2 lines, solaria-coaching in booking_slugs)
A  apps/catalog/template_content_solaria.py              (NEW · 949 lines · IT content tree from e8f38b5)
A  factory/reports/browser-verification/solaria-pass1/   (browser walk evidence: 7 PNGs · check-clean.log · test-run.txt)
A  factory/reports/browser-verification/solaria-pass1.md (browser-verifier report)
A  factory/reports/scorecard/solaria-pass1/              (8 AP8 scorecard deliverables)
A  factory/reports/solaria/solaria-reentry-pass1.md      (narrative report)
```

## §6 · What pass 1 unblocks vs what it does NOT unblock

### Unblocks
- **Pass 2 authorization decision** — user can now decide whether to authorize the EN/FR/ES/AR locale-tree authoring + walks, or hold pass-1 for a review window first.
- **Solaria reviewability** — the IT walk is reviewable end-to-end via `?preview=1` on the running dev server (port 8731). `solaria_qa_staff` user has the password reset for this session.
- **Three-template AP8 pipeline confidence** — the Fiscus first-run pipeline produces Solaria pass-1 output without modification, which is the strongest field signal that the corporate-suite archetype scales to N enrollees.

### Does NOT unblock
- **Solaria public-live** — tier flip to `published_live` requires pass-3 closure (full rubric matrix + cascade test updates + smoke expansion + PNG regen).
- **A fourth corporate-suite enrollment** — the archetype enrollment program A.6 → A.17b is officially CLOSED per `MEMORY.md`. Solaria is the resumption of an already-admitted third enrollee, NOT new enrollment work.
- **The cluster-cumulative D14 carve-out** that Fiscus's retro-AP8-first-run was reserved for — Solaria does not inherit that, by R-SOL-14 binding ("the single-ISO floor for Solaria is the strict floor").

## §7 · Final summary verdict

**Pass 1 is ready for review.** The hardened corporate-suite archetype absorbs Solaria as the third enrollee with zero archetype-level edit, zero build-time gate failure, zero test regression, zero console error, and zero Solaria-specific browser defect. The single sub-floor dimension (D14) is intentional and plan-aligned. The R-SOL grid is operationally green. The AP8 pipeline produces all 8 report shapes on second exercise without prompt modification.

The dev server stays running (port 8731). The user's pass-1 acceptance handshake is the next lever; pass-2 authorization is the user's separate decision per R-SOL-8.
