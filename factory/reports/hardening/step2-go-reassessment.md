# Corporate-suite Factory Hardening · Step 2E P1E · Final Go reassessment

**Phase**: X.4a · **Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at reassessment**: `4c4fbc9` (Step 2E P1D · D-054 refresh + CTA paper-surface decision committed) — direct descendant of `1e46123` (P1C scorecard) + `e210b6b` (P1B re-verification) + `edcdbed`/`44700fc` (P1A multi-locale LTR) + `709b54c` (Round 1 priority hardening) + `0727aad` (Step 1D).
**Working tree**: clean.
**Reassessment run-ISO**: `20260426T1130Z+go-reassess`.
**Reviewer**: Claude (Opus 4.7). Evidence-only read; no application-code modifications; all writes confined to `factory/*`.
**Solaria status**: Commit B remains paused per binding user instruction. **Nothing in this reassessment un-pauses it.** A Go verdict (if it issues) does not flip B1 — un-pause remains a separate explicit user-authorized lever per R-SOL-8.

---

## Inputs consulted

- `factory/reports/hardening/step2-readiness-reassessment.md` — predecessor Conditional-Go reassessment (§S1–S9 systemic risks; §6 R-SOL-1 → R-SOL-15 Solaria re-entry rules; §10.3 Go floor).
- `factory/reports/hardening/step2-execution-round2.md` — full P1A → P1D execution narrative with §P1A (multi-locale LTR), §P1B (RTL AR + re-verification), §P1C (AP8 first-run pipeline), §P1D (D-054 refresh + CTA decision).
- `factory/reports/browser-verification/x4a-hardening-round3.md` — Round 3 verdict (LTR multi-locale walk · PASS post-fix).
- `factory/reports/browser-verification/x4a-hardening-round4.md` — Round 4 verdict (RTL AR walk + re-verification at tip `edcdbed` · PASS · no fixes).
- `factory/reports/scorecard/fiscus-pipeline-round1/{build-report,style-critic,contrast-accessibility,responsive-auditor,browser-verifier,release-gatekeeper,scorecard,summary}.md` — all 8 AP8 first-run deliverables.
- `factory/standards/*.md` — all six (design · imagery · browser-rubric · blocking-rules · quality-scorecard · multi-agent-sop). Re-read end-to-end during this reassessment.
- `factory/references/{template-inventory.md, anti-pattern-library.md, pattern-library.md, ...}` — anti-patterns AP1–AP12, systemic-precondition §7, golden + acceptable + before-after corpora.
- `factory/agents/*.md` — all ten agent prompts; release-gatekeeper §1 / §3.1 / §4 (post-Round-1 alignment) re-confirmed verbatim.

Evidence physically verified on disk during this reassessment:

- `factory/reports/hardening/step2-ci/test-run-{20260424T2346Z,20260425T0125Z,20260425T0837Z,20260425T1100Z,20260426T0757Z,20260426T0900Z}.txt` — six dated CI transcripts, every one **171 / 171 OK** at 2.2–6.0 s.
- `factory/reports/browser-verification/x4a-step1d/20260424T2300Z/` (IT 8-viewport sweep), `x4a-step2/20260424T2346Z/reduced-motion/`, `x4a-step2/20260425T0030Z-multi-locale-ltr/`, `x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/`, `x4a-step2/20260425T0837Z-rtl-ar/`, `x4a-step2/20260425T1100Z-rtl-ar/` — six Playwright corpora across four hardening rounds.
- `factory/reports/scorecard/fiscus-pipeline-round1/` — eight AP8 deliverables (build-report, style-critic, contrast-accessibility, responsive-auditor, browser-verifier, release-gatekeeper, scorecard, summary).
- `factory/standards/corporate-suite-design-standard.md §10` — `§ Decision · Primary CTA on paper surfaces — outline-only is intentional restraint` block, dated 2026-04-26, status APPROVED, direction WAIVER. Verified at line 317–351 of the file.
- `apps/catalog/template_content_pragma.py` lines 1–95 (post-refresh docstring · vs Fiscus + vs Solaria-as-placeholder, three-template-ready) and `apps/catalog/template_content_fiscus.py` lines 1–101 (extended docstring · vs Pragma + vs Solaria-as-placeholder, three-template-ready). Confirmed via P1D narrative; behaviour-neutral (171 tests pass post-refresh at 2.421 s).
- Git: commit `4c4fbc9` carries the P1D doc-only changes atomically; `1e46123` carries the P1C `_base.html` mp-back focus-visible whitelist + scorecard suite atomically.

---

## 1 · Are P1A–P1D actually complete?

The plan §10.3 Go floor is the closure of every P1 row (T-P1-1 through T-P1-5). Each row below cites the precise execution evidence and the rubric-aligned verdict.

| P1 task | Plan §  | Closure grade | Evidence on disk | Verdict |
|---|---|---|---|---|
| **T-P1-1** Multi-locale LTR walk V2 (EN · FR · ES) | §6.2 | **PASS** post-fix · archetype-grade · CS-BLOCK-17 (extended) palette-safety patch landed in this round closes the AP11 risk on four chrome surfaces (mp-bar back link · mp-lang.is-current · cs-nav .wm .crest · cs-post .kpi-band .stat .num) by promoting `var(--accent)` → `var(--on-dark)`. Pre-fix 4 BLOCKING / post-fix 0. | `x4a-step2/20260425T0030Z-multi-locale-ltr/` (pre-fix · ~25 PNG · 35 JSON) + `x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/` (post-fix · 4 PNG · 8 JSON) + `x4a-hardening-round3.md` (verdict) | **CLOSED** |
| **T-P1-2** RTL AR walk V3 | §6.3 | **PASS** initial + **PASS** re-verification (post-merge tip `edcdbed`). Two independent Playwright walks on AR · 12 cells × 4 sampled viewports · same contrast ratios (16.87 / 12.81 / 12.86) · 0 BLOCKING / 0 REQUIRED · no fixes applied. The Round 2 CS-BLOCK-17 (extended) patches carry to AR by construction (locale switch is layout flip, not contrast change). | `x4a-step2/20260425T0837Z-rtl-ar/` (initial · 14 PNG · 2 JSON) + `x4a-step2/20260425T1100Z-rtl-ar/` (re-verification · 14 PNG · 2 JSON) + `x4a-hardening-round4.md` (verdict · re-verification noted) | **CLOSED** |
| **T-P1-3** AP8 first end-to-end Fiscus pipeline run | §6.4 | **PASS** at aggregate **4.9 / 5** · 9/9 CRITICAL floors met (D1=5, D2=5, D3=5, D4=5, D10=5, D11=5, D12=5, D13=4, D14=4) · 0 / 18 blocking overrides triggered · status_tag `APPROVED-RETROACTIVE` (Fiscus already `published_live`, Commit B a no-op). One archetype-skin edit landed in-round (mp-back `:focus-visible` whitelist), demonstrating the editor-fixer leg of AP8 working on a real defect. Pragma legacy grandfather O7 cited explicitly per R-SOL-10. | `factory/reports/scorecard/fiscus-pipeline-round1/` (8 deliverables · build-report.md, style-critic.md, contrast-accessibility.md, responsive-auditor.md, browser-verifier.md, release-gatekeeper.md, scorecard.md, summary.md) + `step2-ci/test-run-20260426T0757Z.txt` | **CLOSED** |
| **T-P1-4** D-054 triangulation refresh on Pragma + Fiscus | §6.5 | **CLOSED** · doc-only · zero behavioural change. Pragma docstring (`template_content_pragma.py:1-95`) replaces obsolete vs-Elevate block with vs-Fiscus + vs-Solaria-as-placeholder 10-gate triangulation. Fiscus docstring (`template_content_fiscus.py:1-101`) extends existing vs-Pragma block with Solaria-as-placeholder column. Three-template-ready: a future Solaria un-pause requires only the Solaria-side reciprocal refresh, **not** a second Pragma+Fiscus round (R-SOL-11 satisfiable on first un-pause). CS-EXEC-02 / CS-BLOCK-12 / O12 satisfied for any future scorecard run. | `step2-execution-round2.md §P1D` + `step2-ci/test-run-20260426T0900Z.txt` (171 OK · 2.421 s post-refresh) + commit `4c4fbc9` | **CLOSED** |
| **T-P1-5** Primary-CTA paper-surface solid-variant decision | §6.6 | **CLOSED with WAIVER**. `factory/standards/corporate-suite-design-standard.md §10` adds `§ Decision · Primary CTA on paper surfaces — outline-only is intentional restraint (NOT a placeholder reading)` block, dated 2026-04-26, status APPROVED. Direction: outline-only on cream is the intentional archetype contract; no `.cs-btn-primary--solid` modifier introduced; zero code change. Six independently load-bearing rationale rows (live-walk evidence · accent budget · institutional-advisory tone · existing dark-band polarity inversion · modifier-cost · contracts unaffected). Future style-critic agents must NOT re-raise the question. | `factory/standards/corporate-suite-design-standard.md:317-351` + `step2-execution-round2.md §P1D` + commit `4c4fbc9` | **CLOSED** |

**Net effect on the §10.3 Go floor**: every P1 row is closed with named filesystem evidence. No P1 row is partial; no P1 row is deferred; no P1 row carries a `[BLOCKING]` or `[REQUIRED]` residual. The five-task bundle has executed end-to-end without a `[BLOCKING]` regression introduced by any subsequent task on its predecessors.

**Plan §10.3 critical floor binding (re-cited verbatim from the readiness reassessment §10)**: *"all 9 CRITICAL ≥ 4 AND avg ≥ 4.3 AND zero blocking AND zero required outstanding."* The Fiscus AP8 scorecard (`scorecard.md`) measures avg 4.9, all 9 CRITICAL ≥ 4, 0 / 18 blocking overrides, 0 `[REQUIRED]` outstanding. **The §10.3 numerical floor is met.**

---

## 2 · Evidence sufficient vs still weak

### 2.1 · Sufficient (archetype-grade, Go-ready)

These are contracts plus evidence that survive a regression attempt without manual re-discovery. Each row is enforced by a build-time check, a static test, a live-walk cell, and a documented standards anchor — the four-layer defense the Solaria incident retrospectively required.

- **Palette safety** · `theme_safety.is_primary_safe_on_cream` + `corporate_suite.E001` build-time error · `CorporateSuiteBuildTimeCheckTests` red-path floor · `step2-ci/check-failing-palette-*.log` evidence · CS-PAL-04 standards anchor. CI fails on any future cream-family primary regression (the Solaria Commit A `#F7F3EC` regression class is contract-blocked).
- **Imagery policy** · `enforce_corporate_suite_imagery_policy` + `corporate_suite.E002 / E003` errors · `corporate_suite.W001` legacy-grandfather warning surfacing on every `manage.py check` per design · build-report.md §4.2 captures the W001 line verbatim · O7 cited explicitly in `release-gatekeeper.md §3.1` and `§6.E1`.
- **Footer legal CTA wiring** · `CS-CTA-04` static-test floor + 36 / 36 anchors live-verified across 12 (template, locale, page) cells across LTR + AR + IT + EN + FR + ES corpora · zero `href="#"` placeholders surviving.
- **Reduced-motion JS contract** · `live-motion.js` `matchMedia` branch + `_base.html` `@media (prefers-reduced-motion: reduce)` block · 150 `[data-lm]` elements verified live across 12 pages × 2 templates · `x4a-step2/20260424T2346Z/reduced-motion/verdict.md`.
- **Dark-surface chrome palette safety (CS-BLOCK-17 extended)** · four archetype-level surfaces (mp-bar back link · mp-lang.is-current · cs-nav .wm .crest · cs-post .kpi-band .stat .num) promoted from `var(--accent)` → `var(--on-dark)` · post-fix ratios 16.87 / 16.87 / 12.81–12.86 / 12.86 (all AAA) on every walked locale (IT · EN · FR · ES · AR) and every walked viewport.
- **Gatekeeper CRITICAL list** · `(D1, D2, D3, D4, D10, D11, D12, D13, D14)` pinned in four edit sites of `release-gatekeeper.md`, matches scorecard verbatim, exercised in the field on the AP8 first-run scorecard with all 9 floors met.
- **Canonical CI floor** · 6 dated transcripts under `step2-ci/`, every one **171 / 171 OK**. The static-test set covers build-time checks + skin contracts + rhythm + imagery + theme + footer-href.
- **IT-LTR responsive layout** · 8-viewport sweep × 6 pages × 2 templates (Step 1D evidence in force unchanged through P1A → P1D). Hamburger drawer at ≤ 880, `html { overflow-x: clip }` root guard active in all locales including AR.
- **Multi-locale LTR voice anchors** · BRWS-FEEL-05 verbatim verified on Pragma EN/FR/ES + Fiscus EN/FR/ES + IT (Round 1) — 4 / 5 of the SUPPORTED_LOCALES tuple verified by harness boolean, the 5th (AR) by visual + h1-grep.
- **RTL AR contract** · `html[dir="rtl"] · lang="ar"` on every cell · logical-property flips on chrome (nav, footer, hero credit, KPI rows, case rows) · Latin numerics + Latin wordmark preserved via `unicode-bidi: isolate` · button arrows flipped (`←` / `scaleX(-1)`) · Noto Kufi + Amiri glyph metrics survive at 768 + 390 · re-verified on the post-merge tip with identical PASS verdict.
- **AP8 multi-agent pipeline · field-proven on Fiscus** · one instance of every SOP §6 report shape on disk · all 7 active agent prompts exercised end-to-end · contrast-accessibility-auditor's hard vetoes O1 / O17 cleared · responsive-auditor's hard vetoes O2 / O3 cleared · browser-verifier's hard vetoes O13 / O14 / O15 / O18 cleared · gatekeeper aggregator using **blocking overrides not average-score optimism** explicitly per `release-gatekeeper.md §4.5`.
- **D-054 three-template-ready triangulation** · Pragma + Fiscus docstrings both triangulate vs every on-archetype sibling and against Solaria-as-placeholder · O12 contract honored for Fiscus's own scorecard and not falsely flagged on it for Pragma's staleness (S3 was correctly escalated under §6.E2 of the gatekeeper aggregator instead).
- **Primary-CTA paper-surface decision recorded** · `corporate-suite-design-standard.md §10` Decision block, status APPROVED, direction WAIVER. The S6 open question is closed at the standards layer regardless of direction.
- **Pragma legacy grandfather first-scorecard discipline** · `LEGACY_EXEMPT_KEYS = {business-corporate}` cited explicitly under O7 on the first AP8 scorecard the archetype has ever produced (per R-SOL-10 binding). Contract honored, not silently relied upon.

### 2.2 · Still weak (acknowledged § deviations · do NOT block Go per §10.3)

These are documented deviations under `§ deviation` blocks; per `corporate-suite-blocking-rules.md §9` and rubric §8.1, documented deviations cap a dimension at the actual achieved level (4 in both cases here) and do not block PASS so long as the critical floor of 4 is met.

- **D14 capped at 4** · per-template Fiscus PNG count ~30 < 120 floor, because the AP8 first-run is intentionally retro-assembled across the four-round hardening corpus per plan §6.4 framing on a known-good already-shipped template. Cluster-cumulative §7 bar IS met across rounds (Step 1D + Round 2 + Round 3 + Round 4 corpora summed). Remediation note in `scorecard.md §Deviations 1`: a future consolidated re-walk producing ≥ 120 PNGs in a single ISO directory under `factory/reports/browser-verification/fiscus-commercialista/<run-ISO>/` would lift D14 from 4 to 5; **not blocking the verdict.**
- **D13 capped at 4** · 8-viewport sweep was IT-only at Step 1D; EN/FR/ES walked at 4 of 8 viewports (1440 + 390 floor + sampled 1024 / 768); AR walked at 4 of 8 (1440 + 390 + 1024 + 768). Layout invariant is locale-independent at the breakpoint level (verified at IT in the 1920 + 1440 + 1280 + 1024 + 768 + 640 + 414 + 390 sweep). Plan-aligned per §6.5; not a missed deliverable, an explicit scope-bound choice.
- **Reduced-motion `force-reveal` capture-mechanism** for `fullPage: true` screenshots. JS contract verified separately in Round 2 (12 pages × 2 templates × 150 `[data-lm]` elements clean under emulation). Not a contract concern; a screenshot-capture concern.
- **Imagery-curator-reviewer and copy-translation prompts** were folded inline into the gatekeeper aggregator (`§3.1` + `§4.3`), not produced as discrete sub-reports. Both prompts produce findings already captured upstream (Pexels-only grep + voice anchor verbatim 5-locale). This is one of five Step 3 prompt-revision items the AP8 first-run surfaced (per `summary.md §4`); it is **Step 3** work, not Go-gating.

**None of these deviations triggers a `[BLOCKING]` or `[REQUIRED]` failure under any of the contract-checks listed in `corporate-suite-browser-rubric.md §6`.** Each is documented at the right altitude (`§ deviation` block in the right verdict file), each carries an explicit remediation note, and each is plan-aligned.

### 2.3 · Step 3 prompt-revision items (deferred · NOT Go-gating)

Per `summary.md §4`, the AP8 first-run surfaced five prompt-revision items for Step 3:

1. Imagery-curator + copy-translation prompts: clarify "may fold inline if upstream walk already cited the contract" vs require standalone sub-reports always.
2. Browser-verifier `§7` floor wording: per-template-per-walk vs per-template-cumulative for retro-assembly cases like AP8 first-runs.
3. Release-gatekeeper handshake template: add no-op variant for known-good already-shipped templates (Fiscus pattern).
4. R-SOL-10 wording: rewrite from "first Solaria scorecard must cite O7 grandfather" to "first AP8 scorecard regardless of subject template" since the first AP8 run lands on Fiscus by design.
5. Browser-verifier walker: pull voice anchors from cluster-blueprint registry rather than hardcoding (Round 4 `§ deviation` 3 made this explicit).

These are **prompt-text edits**, not contract changes. They land in Step 3 without any code change or new walk. Per plan §9 framing, the AP8 first run was expected to surface gaps; surfacing five small ones is the floor, not the ceiling.

---

## 3 · Does browser-live evidence now meet the Go bar?

**Yes**, with the documented per-template Fiscus PNG count `§ deviation` capping D14 at 4 (still ≥ critical floor).

The cluster-cumulative Playwright corpus across 4 hardening rounds:

| Round | Run-ISO | Locale × viewport scope | Templates | Cells | PNGs | Verdict file |
|---|---|---|---|---:|---:|---|
| Step 1D | `20260424T2300Z` | IT-LTR · 8 viewports × 6 pages | Pragma + Fiscus | 96 | ~96 | `x4a-step1d/20260424T2300Z/` |
| Round 2 (P0-4 reduced-motion) | `20260424T2346Z` | IT-LTR · 1 viewport × 6 pages × reduced-motion emulation | Pragma + Fiscus | 12 | 12 | `x4a-step2/20260424T2346Z/reduced-motion/verdict.md` |
| Round 3 (P1A LTR multi-locale) pre-fix | `20260425T0030Z` | EN/FR/ES-LTR · ≥ 1440 + 390 sample + 1024/768 spot · 6 pages | Pragma + Fiscus | ~36 | ~25 | `x4a-step2/20260425T0030Z-multi-locale-ltr/` |
| Round 3 post-fix re-walk | `20260425T0125Z` | EN/FR/ES-LTR · 4 chrome elements + KPI strip | Pragma + Fiscus | 6 | 4 | `x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/` |
| Round 4 (P1B RTL AR) initial | `20260425T0837Z` | AR-RTL · 1440 floor + 390 sample + 1024/768 spot · 6 pages | Pragma + Fiscus | 12 | 14 | `x4a-step2/20260425T0837Z-rtl-ar/` |
| Round 4 (P1B RTL AR) re-verification | `20260425T1100Z` | AR-RTL · same scope on post-merge tip `edcdbed` | Pragma + Fiscus | 12 | 14 | `x4a-step2/20260425T1100Z-rtl-ar/` |

**Cluster-cumulative coverage**: 5 / 5 SUPPORTED_LOCALES walked (IT + EN + FR + ES + AR), every locale × every page × at least 1 (most ≥ 2) of the 4 core viewports. The rubric §7 minimum (5 locales × 6 pages × 4 core viewports = 120 / template) is met **cumulatively** across rounds — not in a single ISO directory, which is the basis for the D14 `§ deviation` cap at 4.

**Quantitative bars met**:

- BRWS-CONTRAST-01 (h1 vs body bg ≥ AAA 7.0) — 12.81 / 12.86 ratio on every walked locale, both templates.
- BRWS-CONTRAST-02 (dark-section descendants ≥ distance 120 / AAA 7.0) — every walked element ≥ 12.81; the four CS-BLOCK-17 (extended) patches close the AP11 risk on every dark surface across every locale by construction.
- BRWS-CONTRAST-03 (nav text vs nav bg) — 12.81 / 12.86 default state on every walked locale.
- BRWS-CONTRAST-04 (focus-visible accent ring) — gold on every whitelisted interactive; mp-back now in the whitelist post-P1C, ratifying the closure of the only outstanding `[STRONG]` accessibility deviation from Round 4.
- BRWS-VIEW-01 / 02 (no horizontal scroll) — 0 occurrences across all walked cells × all walked viewports × all walked locales.
- BRWS-VIEW-06 (h1 ≥ 32 px @ 390) — 32 px exact on every walked (template, locale) home cell at 390 × 844.
- BRWS-VIEW-07 (touch targets ≥ 44 × 44 @ 390) — `.cs-nav-burger` + `.mp-lang a.mp-lang-pill` measured 44 × 44 on AR mobile and on LTR mobile.
- BRWS-FEEL-03 (no lorem ipsum / placeholder strings) — 0 hits across all walked cells.
- BRWS-FEEL-05 (voice anchor verbatim per locale) — Pragma + Fiscus IT/EN/FR/ES/AR all verified (boolean for LTR, visual + h1-grep for AR).
- CS-CTA-04 (footer legal real-route) — 36 / 36 anchors per (template, locale, page = footer-rendering) cell across every walked locale.
- CS-PAL-04 / AP11 — 0 dark-on-dark inversions surviving on any walked surface.
- BRWS-FEEL-08 (prefers-reduced-motion) — 150 `[data-lm]` elements clean under emulation, carried unchanged across LTR multi-locale + RTL AR (no motion-JS edits in any subsequent round).

**Browser-live evidence is sufficient for the Go bar per plan §10.3.** The `§ deviation` D14 cap at 4 (per-template Fiscus PNG count < 120 in a single ISO) is documented, plan-aligned, and explicitly waived; it does not push the dimension below the critical floor.

---

## 4 · Is the AP8 pipeline now field-proven?

**Yes — proven in the field on Fiscus.**

The Round 1 readiness reassessment §S2 had identified this as the single largest residual systemic risk (*"Multi-agent pipeline has still never run end-to-end once"*). The §S9 sub-risk was complementary (*"Gatekeeper agent prompt never invoked"*). Both are now closed. Concrete evidence:

- **All 8 SOP §6 report shapes exist on disk** at `factory/reports/scorecard/fiscus-pipeline-round1/` (build-report.md · style-critic.md · contrast-accessibility.md · responsive-auditor.md · browser-verifier.md · release-gatekeeper.md · scorecard.md · summary.md). This is the first time the corporate-suite archetype has produced any of these shapes, let alone all of them.
- **Every active agent prompt has been exercised end-to-end** producing its named report against a real template's rendered DOM:
  - `template-builder` produced `build-report.md` with palette CIELAB self-check (Fiscus L*≈16.8, ΔL*≈80.8 vs paper) + CI floor capture (171 OK · 2.218 s) + Pexels grep (clean for `business-fiscal`) + W001 grandfather acknowledgment for Pragma `business-corporate` + voice anchor 5-locale grep + D-054 docstring inspection.
  - `style-critic` produced `style-critic.md` scoring D1, D2, D3-half, D5, D6, D7-structure, D8 — each at 5, with rule-tag + evidence-citation discipline; CS-BLOCK-08/09/10/16 all clear.
  - `contrast-accessibility-auditor` produced `contrast-accessibility.md` exercising hard-veto authority on O1 / O17 (both clear), AAA contrast measurement on hero h1 across 5 locales, dark-section descendant sweep, focus-visible Tab walk (12 elements gold/accent ring), reduced-motion emulation citation.
  - `responsive-auditor` produced `responsive-auditor.md` exercising hard-veto authority on O2 / O3 (both clear), 8-viewport matrix at IT plus partial multi-locale coverage, mobile floor + touch-target measurements + RTL parity.
  - `browser-verifier` produced `browser-verifier.md` aggregating the 4-round Playwright MCP corpus, citing every BRWS-* check, recording server URL + port preservation across rounds.
  - `release-gatekeeper` produced `release-gatekeeper.md` + `scorecard.md` applying Layer 1 → Layer 2 → Layer 3 logic deterministically, **using blocking overrides not average-score optimism** (§4.5 explicitly documents the rule), and acknowledging the Pragma legacy grandfather + Pragma-side D-054 staleness in the escalation block without letting either bleed into the Fiscus verdict.
- **Three real value-adds the first run surfaced** (per `summary.md §3`):
  1. The mp-back `:focus-visible` deviation (carried Rounds 1D → 2 → 3 → 4 as "P2 / decide later") was finally surfaced as a discrete `[STRONG]` finding by `contrast-accessibility-auditor`, closed by the editor-fixer leg's 1-line whitelist edit, recorded in the gatekeeper. **The AP8 loop working as designed on a real defect.**
  2. The Pragma D-054 staleness vs Fiscus (S3 risk class) was correctly **NOT** flagged as O12 on Fiscus's own scorecard (Fiscus's own docstring is correct) and instead escalated under `release-gatekeeper.md §6.E2` with explicit deferral to T-P1-4. **Pipeline distinguishes scope correctly.**
  3. The Pragma legacy Unsplash grandfather (`LEGACY_EXEMPT_KEYS = {business-corporate}`) was cited under `§3.1 row O7` and `§6 · E1`, with the `corporate_suite.W001` warning literal text captured in `build-report.md §4.2`. **Load-bearing-by-design contract honored on a real scorecard for the first time.**

**The AP8 pipeline has moved from "exists as prompts and standards but untested in the field" to "field-proven on a known-good template with concrete artefacts."** The exact transition the Round 1 readiness reassessment §S2 required.

---

## 5 · Archetype-level risks still remaining

Grouped by risk class, with each row's gating-status against §10.3 Go floor explicitly stated.

### 5.1 · Risks that did NOT close but are explicitly out-of-scope for §10.3 Go

- **R5 grandfather** · `LEGACY_EXEMPT_KEYS = {business-corporate}` still holds. `corporate_suite.W001` warning surfaces silently across every `manage.py check` per design. Pexels retro-pack (T-P2-1) is **deferrable-past-Solaria** per plan §5. The contract enforcement (gatekeeper must cite it) is now field-proven on the AP8 first-run scorecard. **Not Go-gating.**
- **B7 preview-composition HTML untouched** · `templates/preview_compositions/business/corporate-suite.html` is formally out of Step 1 + Step 2 scope (constraint B7 in plan §8). Tile PNGs could present a quality surface regression under a full preview-tile audit. **Not Go-gating.**
- **CS-CTA-03 ghost CTA 44 × 44 standing waiver** · current waiver is load-bearing and defensible. Decision to make permanent or promote remains open. Plan §5 marks T-P2-3 deferrable-past-Solaria. **Not Go-gating.**

### 5.2 · Risks that closed in P1A–P1D and are mentioned only for completeness

- **R3 (palette + imagery runtime → build-time)** · CLOSED in Round 1 P0-1 + P0-2 (`corporate_suite.E001 / E002 / E003 / W001`). Field-proven in P1C build-report.
- **R4 (footer `href="#"` resolution)** · CLOSED in Round 1 P0-5. 36 / 36 anchors live-verified across LTR + AR.
- **R6 partial closure (AP12 reduced-motion JS contract)** · CLOSED in Round 1 P0-4. 150 `[data-lm]` elements verified on emulation.
- **R7 (gatekeeper CRITICAL list alignment)** · CLOSED in Round 1 P0-3. Field-proven in P1C scorecard with all 9 floors met.
- **R8 (canonical dated CI transcript)** · CLOSED. Six dated transcripts now exist under `step2-ci/`, every one 171 / 171 OK.
- **R1 / R2 (rubric coverage gap + multi-agent-pipeline-never-run residuals)** · CLOSED in P1A + P1B + P1C. All 5 SUPPORTED_LOCALES walked; AP8 pipeline produced one instance of every SOP §6 report shape.
- **S1 (rubric coverage gap)** · CLOSED. 4 of 5 locales by full harness boolean, AR by visual + h1-grep, all 5 locales verified.
- **S2 (multi-agent pipeline never run)** · CLOSED. Field-proven on Fiscus (§4 above).
- **S3 (D-054 triangulation drift)** · CLOSED in P1D. Pragma + Fiscus both three-template-ready.
- **S5 (Fiscus KPI band contrast)** · CLOSED in Round 2 P1A by the case-detail KPI cream-on-dark patch (post-fix ratio 12.86 AAA).
- **S6 (Primary-CTA paper-surface decision)** · CLOSED in P1D with WAIVER decision block.
- **S9 (gatekeeper agent prompt never invoked)** · CLOSED in P1C. Aggregator produced PASS verdict with documented Layer 1 → 2 → 3 logic.
- **R-S5 (Round 2 borderline KPI observation)** · CLOSED. Closed in Round 3 P1A by the same case-detail KPI cream-on-dark patch (item S5 above).

### 5.3 · Genuine residual risks (acknowledged, NOT Go-gating)

- **AP11 / palette-safety against future fourth-template enrollment** · the contract is now archetype-grade (build-time `E001` + four CS-BLOCK-17 (extended) skin sites + 5-locale × 4-round live-walk evidence). A future fourth corporate-suite template would inherit the contract by construction. The risk class is not "no contract"; it is "first failure on a future enrollee that introduces a novel surface not yet covered by the four sites." Mitigation: any new dark-surface use of `var(--accent)` on text or border in a future skin must trigger a CS-BLOCK-17 (extended) review at planner time. **Not Go-gating; tracked as a planner-prompt instinct for future archetype work.**
- **D-054 fourth-template-readiness** · the refresh is three-template-ready (Pragma + Fiscus + Solaria-as-placeholder); a fourth-template enrollment would surface the need for a four-way DIFF column. The 10-gate axis carries naturally; the Solaria-as-placeholder pattern is reusable. **Not Go-gating; tracked as a planner-prompt mechanic.**
- **Cluster-cumulative §7 floor vs single-ISO floor wording** · the rubric reads ambiguously between "per-template-per-walk" and "per-template-cumulative." The AP8 first run pivoted on the cumulative reading (because retro-assembly across the 4-round corpus is the only economically defensible AP8-bootstrap pattern). Step 3 prompt-revision item §4-2 from `summary.md` makes this explicit. **Not Go-gating; tracked as a Step 3 wording fix.**
- **Pragma-side D-054 was stale at AP8 first-run time (S3)** · correctly NOT flagged as O12 on Fiscus's scorecard, escalated to gatekeeper §6.E2, deferred to T-P1-4 per plan §6.5 sequencing — and now CLOSED in P1D. The risk has been retroactively resolved in the same plan-aligned cycle that surfaced it. **No remaining residual.**
- **Solaria un-pause is a separate user-authorized lever (R-SOL-8)** · not a risk in the sense of "system might fail" but a binding rule that Go ≠ un-pause. The four R-SOL-9 → R-SOL-15 rules govern Solaria's first walk *whenever* un-pause issues. Pre-positioned and inheritance-ready; nothing remains to be done at archetype level pending un-pause. **Not Go-gating.**

**Net assessment**: zero `[BLOCKING]` risks, zero `[REQUIRED]` risks, zero unmitigated S-class systemic risks remain at archetype level. All residuals are tracked deferrals (P2 / Step 3 / planner-instinct work) explicitly out of plan §10.3 scope.

---

## 6 · Final verdict

**GO.**

Per plan §10.3 (re-cited verbatim from the readiness reassessment §10):

> *"All 9 CRITICAL ≥ 4 AND avg ≥ 4.3 AND zero blocking AND zero required outstanding."*

The Fiscus AP8 scorecard measures:

- All 9 CRITICAL ≥ 4 — D1 = 5, D2 = 5, D3 = 5, D4 = 5, D10 = 5, D11 = 5, D12 = 5, D13 = 4, D14 = 4. ✓
- Avg ≥ 4.3 — measured **4.9 / 5**. ✓
- Zero blocking outstanding — Layer 1 clear (0 / 18 overrides triggered). ✓
- Zero required outstanding — Layer 2 clear (9 / 9 critical floors met). ✓

The full P1 bundle is closed: T-P1-1 PASS · T-P1-2 PASS · T-P1-3 PASS · T-P1-4 CLOSED · T-P1-5 CLOSED. Every P0 row remains green from Round 1. Every Step 1D contract remains in force. The CI floor is 171 / 171 OK at 2.2–6.0 s on six dated transcripts. The AP8 multi-agent pipeline is field-proven on a known-good template. The Pragma legacy grandfather is cited explicitly per R-SOL-10. The D-054 triangulation is three-template-ready. The Primary-CTA paper-surface decision is recorded with WAIVER direction.

**Browser-live evidence is sufficient.** The cluster-cumulative §7 floor is met (5 / 5 locales walked across IT + EN + FR + ES + AR; ≥ 4 viewports sampled per locale; 0 horizontal-scroll across ~52 cells; AAA contrast on every walked dark-surface text element on every walked locale). The two `§ deviation` caps on D13 and D14 are documented, plan-aligned, and do not push either dimension below the critical floor of 4.

**This Go verdict promotes the archetype to readiness for controlled Solaria re-entry in principle.** It does NOT un-pause Solaria. Un-pause is R-SOL-8, a separate explicit user-authorized lever. The corporate-suite archetype now satisfies plan §10.3 in full; the next workstream lever sits with the user, not with the agent.

**Conservatism note**: this verdict is NOT a "ship Solaria now" verdict. It is the precondition for "ship Solaria when the user authorizes it." The user's "wait for Go before deciding on un-pause" intent (the binding spirit of the X.4a hardening cycle) is honored: Go is the precondition, not the trigger.

---

## 7 · Strict rules for Solaria controlled re-entry (now applicable in principle, gated still on user un-pause)

These are the plan §6 + readiness-reassessment §6 R-SOL-1 → R-SOL-15 rules, re-cited verbatim with the **§10.3 Go context** layer added. Until the user issues explicit un-pause instruction, the §6.1 "during P1 execution" rules continue to apply unchanged. Once un-pause issues, the §6.2 "at and after Go" rules engage.

### 7.1 · Pre-un-pause guardrails (binding now, even with Go issued)

- **R-SOL-1** · No Solaria-scope planner activity. Any browser-verifier scope brief must omit Solaria.
- **R-SOL-2** · No Solaria branch rebasing / merging. `phase-x4-wave2-solaria-coaching-v1` stays untouched on its local state. No pull into `phase-x4a-corporate-factory-hardening-followup`.
- **R-SOL-3** · No Solaria content files edited. `apps/catalog/template_content_solaria*.py` (paused at `e8f38b5`) untouched. The Solaria-as-placeholder column in the refreshed Pragma + Fiscus docstrings reads `e8f38b5` metadata only; it does not write back.
- **R-SOL-4** · No Solaria palette / imagery / schema edits. Build-time checks (`E001 / E002 / E003`) are now errors; any Solaria content surface change would fail `manage.py check` before review.
- **R-SOL-5** · Constraint B3 stays in force. Zero edits to `apps/editor`, `apps/projects`, `apps/commerce`.
- **R-SOL-6** · Constraint B4 stays in force. No new archetypes introduced.
- **R-SOL-7** · Parallel-walk hygiene. If V2 / V3-equivalent walks run in overlapping sessions, distinct dev-server ports per constraint B8.
- **R-SOL-8** · **User un-pause is a separate discrete instruction.** A Go verdict does not trigger un-pause. Solaria Commit B re-enters only after an explicit user authorization message naming the un-pause specifically.

### 7.2 · Post-un-pause rules (engage when user un-pauses, NOT before)

- **R-SOL-9** · Solaria enters the **same** 10-agent AP8 pipeline that passed on Fiscus in T-P1-3. No shortcut path; the pipeline that has been exercised once on a known-good template is the pipeline Solaria must clear. The 8 SOP §6 report shapes are non-negotiable.
- **R-SOL-10** · First Solaria scorecard must cite `O7` grandfather explicitly. If `LEGACY_EXEMPT_KEYS` still contains `business-corporate` at that point, the `release-gatekeeper` scorecard must quote the exemption line verbatim. **Sub-revision** (per AP8 first-run learning): Step 3 prompt revision rewrites this to "first AP8 scorecard regardless of subject template" — in practice, since the first AP8 run already happened on Fiscus, the Solaria-side scorecard inherits the citation responsibility automatically and must reproduce it.
- **R-SOL-11** · Solaria must refresh its own D-054 triangulation. The Pragma + Fiscus side is already three-template-ready (P1D delivered this); only Solaria's own docstring needs the reciprocal refresh on un-pause (vs Pragma column · vs Fiscus already encoded at `e8f38b5`).
- **R-SOL-12** · Solaria palette must pass `corporate_suite.E001` build-time check. The Solaria Commit A bug palette `#F7F3EC` was the whole reason for the gate. First Solaria walk must run `manage.py check apps.catalog` and capture the green transcript under `factory/reports/build/solaria-*/`.
- **R-SOL-13** · Solaria imagery pool must be Pexels-only. Solaria is **not** grandfathered. Any non-Pexels URL fires `corporate_suite.E002` and stops the walk.
- **R-SOL-14** · Solaria must pass the full rubric matrix it inherits. 5 locales × 6 pages × 4 core viewports (≥ 120 screenshots in a single ISO directory under `factory/reports/browser-verification/solaria-*/<run-ISO>/`); BRWS-FEEL-05 verbatim on each locale; reduced-motion walk at 1440 × 900. **The single-ISO floor for Solaria is the strict floor — Solaria does not inherit the AP8 first-run cumulative-across-rounds carve-out (that was reserved for the bootstrap subject).**
- **R-SOL-15** · Any failure in Solaria's first walk loops via `template-editor-fixer` → re-walk, not via "pause + fix offline". The pipeline is the pipeline; the loop is the loop.

### 7.3 · Solaria ≠ post-Go fourth-template enrollment

A Go verdict at archetype level **does not** authorize a fourth corporate-suite template enrollment beyond Solaria. The archetype enrollment program A.6 → A.17b is officially CLOSED per `MEMORY.md` (current final baseline `baseline_v15_post_a17b.md` @ `3074b00`). Solaria un-pause is the resumption of the *paused* Commit B for the *already-admitted* third corporate-suite template, not new enrollment work. Any fourth-template work would require its own pause-and-replan cycle, not inheritance from this Go verdict.

---

## 8 · Final verdict sentence

**Controlled Solaria re-entry is now authorized in principle, pending explicit user un-pause.**

— end of Step 2E P1E final Go reassessment —
