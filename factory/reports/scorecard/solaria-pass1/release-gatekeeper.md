# release-gatekeeper · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` · IT-only at pass 1
**Run-ISO**: `20260426T0907Z`
**Reporter**: Claude (Opus 4.7) acting as `release-gatekeeper` aggregator.
**Inputs**: `build-report.md`, `style-critic.md`, `contrast-accessibility.md`, `responsive-auditor.md`, `browser-verifier.md`, plus the standalone `factory/reports/browser-verification/solaria-pass1.md` and the canonical evidence sink `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/`.
**Layer logic**: `release-gatekeeper.md §4.5` — blocking overrides, NOT average-score optimism.

---

## §1 · CRITICAL list at run

`(D1, D2, D3, D4, D10, D11, D12, D13, D14)` — same 9 CRITICAL dimensions as the Fiscus AP8 first run. All 9 must score ≥ 4 (per plan §10.3 Go floor); aggregate avg must be ≥ 4.3; zero blocking overrides outstanding; zero required outstanding.

## §2 · Layer 1 — blocking-override sweep (18 overrides)

| # | Override | Result | Evidence |
|---|---|---|---|
| O1 | AAA body floor on dark-section primary text | **CLEAR** | `contrast-accessibility.md §3` (12.56 on every measured) |
| O2 | Horizontal scroll on any walked cell | **CLEAR** | `responsive-auditor.md §2` (0 / 7) |
| O3 | Reveal-card stuck opacity 0 under reduced-motion | **CLEAR** | `browser-verifier.md §3 · O15` |
| O4 | Lorem ipsum / placeholder string in DOM | **CLEAR** | `build-report.md §5` (0 hits) |
| O5 | `var(--accent)` text/border on dark chrome | **CLEAR** | inherited CS-BLOCK-17 (extended) |
| O6 | Voice anti-pattern surfacing in any walked cell | **CLEAR** | 13-pattern grep, 0 hits |
| **O7** | First Solaria scorecard must cite Pragma legacy grandfather | **CITED** below in §3.1 — see also §6 · E1 |
| O8 | Footer href="#" placeholder | **CLEAR** | 8 / 8 anchors real-route |
| O9 | Touch target < 44 × 44 on any mobile interactive | **CLEAR** | `responsive-auditor.md §4` |
| O10 | Hero h1 < 32 px @ 390 | **CLEAR** | 32 px exact |
| O11 | Build-time `corporate_suite.E001` (palette) firing | **CLEAR** | `check-clean.log` (0 errors) |
| **O12** | D-054 triangulation stale (any sibling docstring not three-template-ready) | **CLEAR** | inherited from P1D refresh + Solaria's own `e8f38b5` docstring already encodes reciprocal 10-gate vs Pragma + Fiscus |
| O13 | Console error introduced by subject template | **CLEAR** | only marketplace `favicon.ico` 404, pre-existing |
| O14 | Failed network request for in-pool imagery | **CLEAR** | hero photo loads |
| O15 | (= O3) | **CLEAR** | |
| O16 | Build-time `corporate_suite.E002 / E003` (imagery) firing | **CLEAR** | 0 errors on `check` |
| O17 | Same as O5 (chrome accent on dark) — auditor restatement | **CLEAR** | hard-veto auditor explicitly cleared |
| O18 | Page-data placeholder leaking (`{{ page_data.foo }}` literal in DOM) | **CLEAR** | zero unrendered tokens |

**Layer 1 verdict: 0 / 18 blocking overrides triggered.** Layer 2 evaluation proceeds.

### §3.1 · O7 explicit citation (R-SOL-10 binding)

`apps/catalog/imagery_policy.py:81-83`:

```python
LEGACY_EXEMPT_KEYS: frozenset[str] = frozenset({
    "business-corporate",
})
```

The `business-corporate` (Pragma) imagery pool is grandfathered under `LEGACY_EXEMPT_KEYS` pending AP3 retro-curation. The Solaria pass-1 build transcript surfaces `corporate_suite.W001` as the SOLE warning on every `manage.py check`:

```
business-corporate: (corporate_suite.W001) corporate-suite imagery pool 'business-corporate' is grandfathered under LEGACY_EXEMPT_KEYS and ships 6 non-Pexels url(s) pending AP3 retro-curation. The archetype accepts this; the gatekeeper must cite it explicitly (O7 precondition).
```

**Citation honored.** Solaria itself is **NOT** in `LEGACY_EXEMPT_KEYS`; the `business-coaching` pool ships 6 / 6 Pexels URLs and is enforced by build-time error, not warning. The grandfather contract applies to Pragma alone.

## §3 · Layer 2 — CRITICAL floor sweep

| Dim | Floor | Solaria pass-1 | Result |
|---|---:|---:|---|
| D1 · Editorial typography | 4 | **5** | ✓ |
| D2 · Restraint over density | 4 | **5** | ✓ |
| D3 · Color discipline / palette polarity | 4 | **5** | ✓ |
| D4 · Editorial structure / page rhythm | 4 | **5** | ✓ (5 page-kinds, no improvisation) |
| D10 · Voice anchors + anti-pattern hygiene | 4 | **5** | ✓ |
| D11 · Imagery direction + Pexels-only | 4 | **5** | ✓ |
| D12 · Contrast / accessibility | 4 | **5** | ✓ (12.56 AAA on every primary) |
| D13 · Responsive-layout invariants | 4 | **4** | ✓ § deviation: 3-viewport sample vs 8-viewport sweep |
| D14 · Browser-walk corpus per template | 4 | **3** | **§ deviation** |

§ deviation on D14 — the dimension scores **3 / 5** at pass 1 due to the IT-only single-locale capture (7 PNGs vs the 120-floor for full-rubric closure). Pass 1 is IT-only by binding D-102 cadence; the cap is plan-aligned, not a missed deliverable. **D14 = 3 IS BELOW THE CRITICAL FLOOR OF 4.** Layer 2 surfaces this as a Layer 2 finding.

### §3.2 · How to read the D14 = 3 reading

The plan §10.3 Go floor is `all 9 CRITICAL ≥ 4 AND avg ≥ 4.3 AND zero blocking AND zero required outstanding`. **At a strict reading, D14 = 3 means pass 1 does NOT clear the GO floor.**

This is **intentional and explicitly scoped** by the controlled-reentry framing:

- Pass 1 is the FIRST controlled re-entry pass, not closure.
- Pass 1 ships IT-only by D-102 cadence binding (the original Commit A was IT-only).
- The full-rubric matrix (5 locales × 6 pages × 4 viewports = 120+ PNGs in single ISO) is **R-SOL-14**'s closure floor for **Solaria-overall**, not for the first pass.
- Pass 2 lands EN/FR/ES/AR (D14 climbs to ~4 with 4-locale × 6-page × 1-viewport sample).
- Pass 3 closes on the full rubric matrix (D14 climbs to 5).

**Pass-1 gatekeeper verdict is NOT "ship Solaria public-live."** Pass-1 verdict is "Solaria pass-1 is ready for review and pass-2 authorization." Tier flip to `published_live` requires pass-3 closure.

## §4 · Layer 3 — required-outstanding sweep

Zero `[REQUIRED]` outstanding. The 4 walks across X.4a (Step 1D + Round 2-4 + Fiscus AP8 + Solaria pass-1) leave no unresolved required items.

## §5 · Aggregate score

```
D1   D2   D3   D4   D10  D11  D12  D13  D14
 5    5    5    5    5    5    5    4    3
```

**Avg = (5+5+5+5+5+5+5+4+3) / 9 = 42 / 9 = 4.67.**

vs Plan §10.3 floor of avg ≥ 4.3: **PASS on average.**
vs Plan §10.3 floor of all 9 CRITICAL ≥ 4: **D14 = 3 DOES NOT CLEAR.**

## §6 · § deviation log (entered at the right altitude)

### §6 · E1 · D14 capped at 3 — IT-only by D-102 cadence (R-SOL-14 partial)

The pass-1 framing is "first controlled re-entry pass, IT-only, scope-bound by D-102 cadence." The original Solaria Commit A on `phase-x4-wave2-solaria-coaching-v1` was IT-only with EN/FR/ES/AR explicitly deferred to Commit B; Commit B was paused; the user un-pause authorizes resumption but explicitly as PASS 1, not full closure.

**Closure path:**
- Pass 2 — author EN/FR/ES/AR locale trees + walk 4 of them (lifts D14 to ~4).
- Pass 3 — full 5-locale × 6-page × 4-core-viewport matrix in a single ISO directory (lifts D14 to 5) + tier flip + smoke expansion + 6 cascade-test updates.

The user authorization message names "pass 1 only"; pass 2 + pass 3 are subsequent user-authorized increments per **R-SOL-8**.

**Pass-1 gatekeeper-status_tag: `APPROVED-PASS-1` · NOT `APPROVED-PUBLIC-LIVE`.**

### §6 · E2 · D13 capped at 4 — 3-viewport sample

The 1440 + 768 + 390 sample is sufficient for IT-only walk (the layout invariants are locale-independent at the breakpoint level; the archetype's Step 1D 8-viewport sweep on Pragma + Fiscus established the matrix once for the cluster). Pass-3 will lift D13 to 5 with the full 8-viewport sweep.

### §6 · E3 · `corporate_suite.W001` Pragma legacy grandfather (O7)

Cited verbatim in `§3.1` above. The grandfather contract is honored, not silently relied upon. Solaria itself is NOT grandfathered.

### §6 · E4 · Reduced-motion `force-reveal` capture-mechanism

Same archetype-level § deviation 3 from `step2-go-reassessment.md §2.2`. NOT a Solaria-introduced concern. Pass-1 captures use `page.emulateMedia({reducedMotion: 'reduce'})` for `fullPage` shots.

### §6 · E5 · `imagery-curator-reviewer` and `copy-translation` agent prompts

Both folded inline into this gatekeeper aggregator (`§3.1` Pexels-only grep + R-SOL-13 enforcement; `§style-critic.md §6` voice-anchor verbatim grep). Same Step 3 prompt-revision item identified by the Fiscus AP8 first run; not pass-1-gating.

## §7 · Final verdict

**Pass 1 status: APPROVED-PASS-1.**

The hardened corporate-suite archetype absorbs Solaria as the third enrollee with **zero archetype-level skin edits, zero build-time gate failures, zero test regressions, zero console errors attributable to Solaria, and zero Solaria-specific browser defects across 7 walked cells**.

The single dimension below the critical floor (D14 = 3) is **intentional and plan-aligned** — pass 1 is IT-only by binding D-102 cadence, with pass 2 + pass 3 as the closure path under further user authorization.

**Pass-1 verdict is NOT "ship Solaria public-live."** Pass-1 unblocks pass-2 work (EN/FR/ES/AR locale authoring + multi-locale walks). Pass-3 closes the full rubric matrix and the tier flip.

**Pass-1 deliverables:**
- 8 AP8 scorecard files at `factory/reports/scorecard/solaria-pass1/`
- 1 narrative report at `factory/reports/solaria/solaria-reentry-pass1.md`
- 1 browser-verification report at `factory/reports/browser-verification/solaria-pass1.md`
- 7 PNGs at `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/screenshots/rm/`
- 1 default-motion PNG at `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/screenshots/01-home-1440-it.png` (kept for transparency)
- 2 build transcripts (`check-clean.log` + `test-run.txt`)
- 7 source-code files updated under `apps/catalog/` and 1 under root (`TEMPLATE_REGISTRY.json`)

Pass-1 is **ready for user review and pass-2 authorization decision**. The gatekeeper handshake awaits the user's signed acceptance; per **R-SOL-15**, any user-flagged finding loops via `template-editor-fixer` → re-walk on the same pass-1 server, NOT via pause-and-fix-offline.
