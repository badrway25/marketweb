# Corporate-suite Quality Scorecard · fiscus-commercialista

**Verdict**: **PASS**
**Template**: `fiscus-commercialista` · Fiscus — Studio Tributario · corporate-suite
**Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip**: `e210b6b` + 1 archetype-skin edit (`_base.html` mp-back focus-visible whitelist · this round)
**Walk run**: `20260426T0757Z` (aggregator timestamp; underlying browser corpus runs `20260424T2300Z` · `20260424T2346Z` · `20260425T0030Z` · `20260425T0125Z` · `20260425T0837Z` · `20260425T1100Z`)
**Scored by**: Claude (Opus 4.7) · acting as release-gatekeeper aggregator per `factory/agents/release-gatekeeper.md`
**Related rubric verdicts**:
- `factory/reports/browser-verification/x4a-step1d/20260424T2300Z/` (IT 8-viewport)
- `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/verdict.md` (reduced-motion JS contract)
- `factory/reports/browser-verification/x4a-hardening-round3.md` (LTR multi-locale · Round 3)
- `factory/reports/browser-verification/x4a-hardening-round4.md` (RTL AR · Round 4 + re-verification)

> **Framing**: this is the **first end-to-end AP8 multi-agent pipeline run** ever performed on the corporate-suite archetype (T-P1-3 · plan §6.4). Fiscus is the known-good already-shipped template chosen as the bootstrap subject. **Fiscus is already at `tier: published_live` from Session 80**; the PASS verdict here means *the pipeline produced a clean scorecard against the existing live state*, not *a new template just shipped*. No registry edit is pending in this round.

## Layer 1 · Blocking overrides

- [x] O1  Contrast — h1..h5 distance ≥ 120 & AA ≥ 4.5 on every page × locale
- [x] O2  No horizontal scroll at any §5 matrix viewport
- [x] O3  Hero stacks + nav collapses at ≤ 720 px
- [x] O4  All imagery URLs resolve (zero 404s)
- [x] O5  Imagery passes 3-second subject check on every slot
- [x] O6  Imagery mood underlines voice anchor (no contradiction)
- [x] O7  Every URL is Pexels (Pragma legacy Unsplash on `business-corporate` is the documented `LEGACY_EXEMPT_KEYS` exception · cited explicitly per R-SOL-10)
- [x] O8  No editor affordances on `/live/` route
- [x] O9  No lorem ipsum / "Replace this text" / "Your headline here"
- [x] O10 No fake certifications in leadership
- [x] O11 Voice anchor verbatim across 5/5 locales
- [x] O12 D-054 10-gate triangulated in module docstring (Fiscus 10/10 vs Pragma · Pragma-side staleness vs Fiscus tracked under T-P1-4)
- [x] O13 Dev-server URL + port recorded in every walk's verdict + walk-log
- [x] O14 Full §5 viewport matrix walked (cluster-cumulative across rounds)
- [x] O15 Evidence directory complete · cluster-cumulative ≥ 120 PNGs · per-template Fiscus PNG count `§ deviation`
- [x] O16 Navbar bg = `--primary` AND ≤ 1 accent CTA in nav
- [x] O17 Dark-section child text AA ≥ 4.5 with RGB distance ≥ 120
- [x] O18 Live browser walk performed (5 distinct Playwright MCP walks across 4 hardening rounds)

**Blocking overrides triggered**: **NONE.** Layer 1 CLEAR.

## Layer 2 · Critical-dimension floors

| # | Dimension | Score | Critical? | Floor met (≥ 4)? |
|:-:|---|:-:|:-:|:-:|
| D1 | Premium feel | 5 | ✓ | yes |
| D2 | Elegance | 5 | ✓ | yes |
| D3 | Modern professionalism | 5 | ✓ | yes |
| D4 | Hero readability | 5 | ✓ | yes |
| D10 | Imagery coherence | 5 | ✓ | yes |
| D11 | Pexels-only compliance | 5 | ✓ | yes |
| D12 | Contrast safety | 5 | ✓ | yes |
| D13 | Responsive quality | 4 | ✓ | yes |
| D14 | Browser live verification quality | 4 | ✓ | yes |

**Critical floors**: 9/9 met. Layer 2 CLEAR.

## Layer 3 · All 15 dimensions

| # | Dimension | Score | Evidence (rubric tag · measurement · screenshot) | Notes |
|:-:|---|:-:|---|---|
| D1 | Premium feel | 5 | BRWS-FEEL-01 · `style-critic.md` §5 · `x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/screenshots/` | Reads as a real Milan commercialista boutique; accent ≤ 2 per fold; editorial fiscal-desk imagery; zero affordances |
| D2 | Elegance | 5 | BRWS-RHYTHM-05 · BRWS-HERO-05 · `style-critic.md` §5 | Italic `<em>` discipline; zero uppercase h2; 100×72 padding; one dark band per home |
| D3 | Modern professionalism | 5 | BRWS-FEEL-05 · BRWS-FEEL-06 · `contrast-accessibility.md` §4.4 · `build-report.md` §4.5/4.6 | 5/5 voice-anchor verbatim; ODCEC/Cassazionista verifiable; gold focus-visible (incl. mp-back fix); D-054 10/10 in Fiscus docstring |
| D4 | Hero readability | 5 | BRWS-CONTRAST-01 · BRWS-READ-01 · `contrast-accessibility.md` §4.1 | h1 AAA 12.86 across 5 locales; 55/45 split; stacks 1fr ≤ 720; h1 64 px desktop / 32 px mobile |
| D5 | Navbar quality | 5 | BRWS-NAV-01..04 · `style-critic.md` §5 | Bg = `--primary` `rgb(31,41,55)`; 1 accent CTA trailing; 4 distinct states with gold focus ring; condense @ 1024 / drawer @ ≤ 880 |
| D6 | Footer quality | 5 | BRWS-FOOT-01..05 · `style-critic.md` §5 | 3-col desktop; legal row + ODCEC whistleblowing; RTL Latin wordmark + numerics; stacks 1-col @ 720 |
| D7 | Typography hierarchy | 5 | BRWS-HERO-05 · BRWS-READ-04 · BRWS-READ-05 · `style-critic.md` §5 | IBM Plex Serif + IBM Plex Sans; italic `<em>` on every headline; tabular-nums on KPI band; Kufi+Amiri swap under RTL |
| D8 | Spacing rhythm | 5 | BRWS-RHYTHM-01..05 · `style-critic.md` §5 | `100×72; max-width 1400; margin 0 auto`; home section order pinned; 1 dark band at position 3; never adjacent |
| D9 | Imagery quality | 5 | BRWS-IMG-01 · BRWS-IMG-08 · `browser-verifier.md` §4.4 | 6/6 200; resolution floors met (hero 1600w, feature 1200w, portrait 800w); editorial fiscal-desk reading |
| D10 | Imagery coherence | 5 | BRWS-IMG-03 · BRWS-IMG-04 · `release-gatekeeper.md` §3.1 | 3-second subject = commercialista-desk + tax-document + advisor-portrait; mood underlines voice anchor; zero cross-cluster URL reuse |
| D11 | Pexels-only compliance | 5 | BRWS-IMG-02 · `build-report.md` §4.3 | Fiscus `business-fiscal` 0 non-Pexels; pack records carry photographer + id + resolution per CS-IMG-SRC-02 |
| D12 | Contrast safety | 5 | BRWS-CONTRAST-01..04 · `contrast-accessibility.md` §4.1-4.4 | Hero AAA on 5 locales; dark-section descendants ≥ 12.86; nav AA all states; gold focus ring; **zero AP1/AP11 risk surfaces post-fix** |
| D13 | Responsive quality | 4 | BRWS-VIEW-01..07 · BRWS-RESP-01..07 · `responsive-auditor.md` §5 | 8 viewports walked at IT (Step 1D); 4 of 8 at EN/FR/ES/AR (`§ deviation` plan §6.5); 0 overflow across ~50 cells; hero stacks 1fr ≤ 720; drawer @ ≤ 880; touch ≥ 44 |
| D14 | Browser live verification quality | 4 | BRWS-EVID-01..06 · BRWS-SRV-01..05 · `browser-verifier.md` §5 | Playwright MCP walks across 4 rounds; URL+port per round; cluster-cumulative §7 floor met; per-template Fiscus PNG ~30 < 120 (`§ deviation` 1) |
| D15 | Text/image coherence | 5 | BRWS-IMG-04 · BRWS-FEEL-05 · BRWS-ALIGN-01 · `release-gatekeeper.md` §3.1 | Voice anchor 5/5 verbatim; credentials-to-imagery cross-check passes; RTL alignment reverses correctly (D3 logical-property flips) |

**Overall average**: (5×13 + 4×2) / 15 = **73 / 15 ≈ 4.87 → 4.9** (rounded to one decimal · arithmetic mean · unweighted)

## Aggregate gate

- CRITICAL dims all ≥ 4? **yes**
- Non-critical dims all ≥ 3? **yes**
- Overall average ≥ 4.3? **yes · 4.9**
- `[REQUIRED]` failures outstanding (per rubric verdict)? **0**
- `[STRONG]` deviations documented in `§ deviation`? **yes · 3 listed below**

## Verdict computation

- Layer 1 (blocking overrides): **clear**
- Layer 2 (critical floors): **clear**
- Layer 3 (aggregate): **PASS** per §6.1
- **Final verdict**: **PASS**

## Evidence pointers

- Build report: `factory/reports/scorecard/fiscus-pipeline-round1/build-report.md`
- Sub-scorecards (5):
  - `factory/reports/scorecard/fiscus-pipeline-round1/style-critic.md`
  - `factory/reports/scorecard/fiscus-pipeline-round1/contrast-accessibility.md`
  - `factory/reports/scorecard/fiscus-pipeline-round1/responsive-auditor.md`
  - `factory/reports/scorecard/fiscus-pipeline-round1/browser-verifier.md`
  - imagery-curator + copy-translation findings folded inline into `release-gatekeeper.md` §3.1 + §4.3
- Release-gatekeeper aggregation: `factory/reports/scorecard/fiscus-pipeline-round1/release-gatekeeper.md`
- Browser corpus (cluster-cumulative across 4 hardening rounds):
  - `factory/reports/browser-verification/x4a-step1d/20260424T2300Z/`
  - `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/`
  - `factory/reports/browser-verification/x4a-step2/20260425T0030Z-multi-locale-ltr/`
  - `factory/reports/browser-verification/x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/`
  - `factory/reports/browser-verification/x4a-step2/20260425T0837Z-rtl-ar/`
  - `factory/reports/browser-verification/x4a-step2/20260425T1100Z-rtl-ar/`
- CI floor at post-fix tip: `factory/reports/hardening/step2-ci/test-run-20260426T0757Z.txt` (171/171 OK · 2.218 s)
- Dev server: `http://127.0.0.1:8735/` · still running (Round 4 re-verification process · BRWS-SRV-04 honored)

## Remediation (if BORDERLINE or FAIL)

n/a · PASS.

## Deviations (PASS · waived `[STRONG]` findings)

1. **Per-template Fiscus screenshot count ~30 < 120 floor** (D14 cap at 4). Justification: AP8 first-run is intentionally retro-assembled across the four-round hardening corpus per plan §6.4 framing on a known-good already-shipped template. Cluster-cumulative §7 bar IS met across rounds. Remediation note: a future consolidated re-walk on a single ISO with ≥ 120 PNG would lift D14 to 5; not blocking the verdict.
2. **8-viewport sweep was IT-only at Step 1D** (D13 cap at 4). EN/FR/ES walked at 4 of 8 viewports (1440 + 390 floor + sampled 1024/768); AR walked at 4 of 8 (1440 + 390 + 1024 + 768). Layout invariant is locale-independent at the breakpoint level (verified at IT in 1920+1440+1280+1024+768+640+414+390 sweep). Plan-aligned per §6.5.
3. **Reduced-motion `force-reveal` capture-mechanism** for `fullPage: true` screenshots. JS contract verified separately in Round 2 (12 pages × 2 templates × 150 `[data-lm]` elements clean under `prefers-reduced-motion: reduce` emulation). Not a contract concern.

## Parallel-verification handshake

Dev server remains at `http://127.0.0.1:8735/` for user parallel verification.

> **User**: please open this URL in your own browser and confirm visual parity with the walk evidence (recommended spot-checks listed in `release-gatekeeper.md` §7).
>
> **Note**: Fiscus is **already** at `tier: published_live` from Session 80 (2026-04-20). The PASS verdict here is the **AP8 first-run scorecard against the existing live state** — no tier flip is pending; Commit B is a no-op for this template. The handshake is preserved for parity-of-process.

This scorecard is **draft** until user parallel verification, then **immutable**.

— end of scorecard —
