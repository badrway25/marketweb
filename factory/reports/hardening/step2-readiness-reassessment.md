# Corporate-suite Factory Hardening · Step 2 · Readiness reassessment (post Round 1)

**Phase**: X.4a · **Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at reassessment**: `709b54c` (Round 1 committed) — direct descendant of `0727aad` (Step 1D closure) + `576aa58` (Step 2 plan) + `709b54c` (Round 1 execution).
**Working tree**: clean.
**Reassessment run-ISO**: `20260424T2346Z+reassess`.
**Reviewer**: Claude (Opus 4.7). Evidence-only read; no application-code modifications; all writes confined to `factory/*`.
**Solaria status**: Commit B remains paused per binding user instruction. Nothing in this reassessment un-pauses it.

---

## Inputs consulted

- `factory/reports/hardening/step2-followup-plan.md` — Step 2 narrative plan (§10 exit-criteria ladder binding here).
- `factory/reports/hardening/step2-followup-checklist.md` — operational punch list.
- `factory/reports/hardening/step2-execution-round1.md` — Round 1 execution report.
- `factory/reports/browser-verification/x4a-hardening-round2.md` — Round 2 live walk (P0-4 + P0-5 side-check).
- `factory/reports/hardening/step1-readiness-verdict.md` — **NOT PRESENT ON DISK** at any visited tip. The plan §0 already flagged the absence and reconstructed the No-Go rationale from Step 1 report deferrals and `template-inventory.md §7`. This reassessment inherits that reconstruction; it does not attempt to author the missing predecessor artefact retroactively.
- `factory/standards/*.md` — all six (design · imagery · browser-rubric · blocking-rules · quality-scorecard · multi-agent-sop).
- `factory/references/*.md` — `template-inventory.md` (especially §7 systemic preconditions), `anti-pattern-library.md` (AP1–AP12), `pattern-library.md`.
- `factory/agents/*.md` — all ten prompts, with particular attention to `release-gatekeeper.md §1 / §3.1 / §4` post-edit.

Evidence physically verified on disk during this reassessment:

- `factory/reports/hardening/step2-ci/check-clean-20260424T2345Z.log` ✓
- `factory/reports/hardening/step2-ci/check-failing-palette-20260424T2345Z.log` ✓
- `factory/reports/hardening/step2-ci/check-failing-imagery-20260424T2345Z.log` ✓
- `factory/reports/hardening/step2-ci/test-run-20260424T2346Z.txt` ✓
- `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/verdict.md` ✓
- `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/screenshots/*.png` — 12 files ✓
- Git: commit `709b54c` carries Round 1 code + docs + evidence atomically.

---

## 1 · What Priority 1 (P0) gaps were actually closed

The plan's P0 bundle has six tasks (T-P0-1 through T-P0-6). Every one of them is green with named filesystem artefacts under `factory/reports/`. Each row below cites the precise reason-for-No-Go it resolves (R1–R8 from plan §1).

| P0 task | Reason-for-No-Go resolved | Closure grade | Evidence on disk |
|---|---|---|---|
| **T-P0-1** build-time palette gate (`django.core.checks.Error`, id `corporate_suite.E001`) | **R3** (palette runtime → build-time) | **Archetype-grade** — known-bad Solaria prefix palette `#F7F3EC` now fails `manage.py check`; `CorporateSuiteBuildTimeCheckTests` asserts the red path. | `check-clean-*.log` + `check-failing-palette-*.log` + test transcript lines under `CorporateSuiteBuildTimeCheckTests` |
| **T-P0-2** build-time imagery-policy gate (ids `E002` error · `E003` error · `W001` legacy warning) | **R3** (imagery runtime → build-time) · partial **R5** visibility | **Archetype-grade** with one caveat — the Pragma `business-corporate` pool is surfaced as `W001` **warning**, not error, by explicit design (plan §4 item 3). Injected non-Pexels URL in a non-exempt pool fires `E002`. | `check-clean-*.log` (1 W001 line) + `check-failing-imagery-*.log` (1 E002 line) |
| **T-P0-3** gatekeeper CRITICAL list alignment (D9 → D3) | **R7** | **Archetype-grade** — four edit sites in `release-gatekeeper.md` now emit `(D1, D2, D3, D4, D10, D11, D12, D13, D14)`, matching `corporate-suite-quality-scorecard.md §3 / §5 / §6` verbatim. Grep-confirmed during this reassessment at `release-gatekeeper.md:23,69-79,145-146,234`. | prompt diff under commit `709b54c` |
| **T-P0-4** AP12 reduced-motion walk V1 | **R6 (partial)** — JS-side reduced-motion contract | **Archetype-grade for the JS contract** — 150 `[data-lm]` elements across 12 pages × 2 templates, 0 stuck opacity-0, 0 console errors. Reduced-motion emulation confirmed live via `matchMedia` on every page. | `x4a-step2/20260424T2346Z/reduced-motion/{verdict.md, screenshots/*.png}` (12 PNG) |
| **T-P0-5** footer `href="#"` resolution (CS-CTA-04) | **R4 (first half)** — footer legal placeholders | **Archetype-grade** — skin edit in `_base.html` wires the 3 anchors to `{% url 'catalog:live_template_page' %}` with optional per-site override slugs; static test `CorporateSuiteChromeContractTests.test_footer_legal_hrefs_are_not_placeholder_hashes` pins the contract; 36 / 36 anchors live-verified across the 12 walked pages. | Round 1 report §"Files changed" + walk verdict per-page 3/3 column |
| **T-P0-6** canonical dated CI transcript | **R8** | **Archetype-grade** — `python manage.py test apps.catalog -v 2` → **171 OK · 2.213 s**. Class-line counts match the Round 1 report (8+18+6+8+7 across the five `CorporateSuite*Tests` families, new footer-href test included). | `step2-ci/test-run-20260424T2346Z.txt` |

**Net effect on the No-Go rationale** (plan §1):

- **R3 fully closed.** Both archetype-level contracts are now enforced at `manage.py check` exit code, not just live-render `UserWarning`.
- **R4 half closed.** Footer `href="#"` gone; the ghost-CTA touch-target waiver survives as a standing deviation (P2 decision, not P0 scope).
- **R6 partially closed.** AP12's JS-side contract is live-verified at 1440 × 900 on both enrolled templates. The AP8 end-to-end multi-agent pipeline run remains un-done (that is a P1 item).
- **R7 fully closed.**
- **R8 fully closed.**
- **R1 is NOT closed** by P0 by design — full-rubric coverage was never a P0 deliverable. Plan §6.1 explicitly scopes P0-4 to 1440 × 900 × IT because motion is a JS contract not a layout one.
- **R2 is partially closed.** Three of seven `template-inventory.md §7` systemic items (AP1, AP2, AP7) closed in Step 1; R3-closure here lifts AP1 and AP3-enforcement from runtime to CI. AP8, AP10, and the hard precondition form of AP12 (`⚠`-tagged end-to-end verification) remain open as P1 work.
- **R5 is unchanged.** `LEGACY_EXEMPT_KEYS = {business-corporate}` still holds; the Pexels retro-pack (T-P2-1) is a deferrable-past-Solaria item per plan §5.

---

## 2 · What systemic risks remain

Grouped by risk class. The gates in force for each row are cited.

### S1 · Rubric coverage gap is still vast (R1 variant · §5 matrix)

The combined Step 1D + Round 2 walks cover:

- Step 1D (IT · LTR): 8 viewports × 6 pages × 2 templates at the responsive pass.
- Round 2 P0-4 (IT · LTR): 1 viewport × 6 pages × 2 templates with reduced-motion emulation.

`corporate-suite-browser-rubric.md §5-§7` defines the per-template walk as **5 locales × 6 pages × 8 viewports = 240 cells** with a floor of **120 screenshots per template** (5 × 6 × 4 core viewports). Two templates = **240 baseline screenshots minimum** to meet the rubric's per-template floor × 2. The current walk evidence covers **1 of 5 locales** on the full viewport matrix and **1 of 5 locales** for the JS-contract slice — roughly **one fifth** of the rubric's locale bar, and **zero** of the RTL bar. BRWS-FEEL-05 (voice anchor verbatim across all 5 locales) has not been live-verified for 4 of the 5 locales.

**Implication**: the archetype cannot claim full-rubric Go while the Playwright evidence set remains IT-only on the LTR side and empty on the AR side. This is the single largest systemic gap between Conditional-Go and Go.

### S2 · Multi-agent pipeline has still never run end-to-end once (AP8 · R6 residual)

Round 1 was executed by a single operator (Claude) exercising the observation-agent contracts inline. No `build-report.md`, no `style-critic.md`, no `contrast-accessibility.md`, no `responsive-auditor.md`, no per-template `verdict.md` issued from `browser-verifier` as a discrete agent step, no aggregated `scorecard.md` from `release-gatekeeper`. The SOP §4.1 pipeline-definition → pipeline-usage transition has not happened. A first end-to-end run on a **known-good** template (Fiscus) is T-P1-3 in the plan; it is a hard precondition for Solaria (plan §4 item 2).

**Implication**: the pipeline exists as prompts and standards but has not been exercised. The first time it runs will surface prompt gaps — per plan §9 those gaps become Step 3 work. Running it first on **Solaria** (with 4 new locales × 240 walk cells) compounds risk; the plan's binding sequence of "Fiscus re-walk before Solaria re-entry" stands.

### S3 · D-054 triangulation drift (AP10)

Pragma + Fiscus module-docstring triangulations were authored when each template had exactly one on-archetype sibling. Solaria un-pause would make the archetype three-template, which `CS-EXEC-02 / CS-BLOCK-12 / O12` require to be triangulated against **every** sibling. Docstring content on `template_content_pragma.py` + `template_content_fiscus.py` is stale. T-P1-4 is a planner-driven content-only refresh; zero skin edits; untouched by Round 1.

**Implication**: if Solaria re-enters before T-P1-4 lands, the first gatekeeper run on Solaria would cite a sibling whose docstring does not reciprocate the triangulation — CS-BLOCK-12 trip.

### S4 · Pragma legacy Unsplash grandfather (AP3 soft · R5)

`LEGACY_EXEMPT_KEYS = {'business-corporate'}` still holds. The P0-2 build-time imagery gate is silent-at-warning on Pragma by design (`corporate_suite.W001` surfaces but does not block CI). Plan §5 marks T-P2-1 deferrable-past-Solaria **provided** the gatekeeper explicitly calls the grandfather out under `O7` in the Solaria scorecard. No scorecard yet exists to test that discipline.

**Implication**: the grandfather is load-bearing by design, not by neglect — but the enforcement of "gatekeeper must cite it" is a contract that has not yet been exercised once. First exercise is T-P1-3 (Fiscus re-walk) where the same contract lands, exactly per plan sequencing.

### S5 · Fiscus case-study detail KPI band contrast (D12 candidate defect)

Round 2 flagged a visually low-contrast reading at the bottom `.cs-kpi-band` on `casi-seguiti/pmi-manifattura-bilancio-revisione`. It is not a reduced-motion defect; it renders the same without emulation. It is a standing spot that the P1 `contrast-accessibility-auditor` walk must quantify with DevTools sampling. **Not** a P0 blocker; tracked as a P1 input, and carried here so a future reader cannot claim it was missed.

### S6 · Primary-CTA paper-surface solid-variant decision (T-P1-5)

Step 1B flagged this, Step 1D did not touch it, Round 1 did not address it. The current outline-only primary CTA on cream surfaces reads as "placeholder" per style-critic observation. Decision-point-before-implementation: either adopt `.cs-btn-primary--solid` or waiver the outline-only reading as intentional. Either outcome ships a `§ decision` block in `factory/standards/corporate-suite-design-standard.md`. Unresolved.

### S7 · Ghost CTA 44×44 mobile touch-target (T-P2-3 · standing waiver)

Current waiver under `CS-CTA-03` ("ghost = typographic link, not button") is load-bearing and defensible. But the decision to make the waiver permanent or promote the CTA is still open. This is P2 (deferrable-past-Solaria) and not a systemic blocker — however, any inbound reviewer applying `blocking-rules.md §9` fresh would flag it as a deviation worth documenting, so it stays called-out here.

### S8 · Preview-composition HTML untouched

`templates/preview_compositions/business/corporate-suite.html` (313 lines, 0 media queries) is formally out of Step 1 and Step 2 scope (constraint B7 in plan §8). Tile PNGs could present a quality surface regression under a full preview-tile audit. This is not a P0 or P1 blocker; it is a standing scope boundary.

### S9 · Gatekeeper agent prompt never invoked

The CRITICAL list is now correct, but nothing has **run** `release-gatekeeper` yet on this archetype. The prompt's first real exercise is T-P1-3. Until that happens, every Step 2 `manage.py check` exit-code claim rests on the build-time checks, not on the aggregated multi-dimensional scorecard the agent is designed to emit. That is fine for Conditional-Go per §10.2 but not for Go per §10.3.

---

## 3 · Is browser-live evidence now strong enough?

**Evidence strength depends on the question being asked.**

- **For Conditional-Go (plan §10.2)**: yes. The P0-4 reduced-motion walk meets the scoped specification exactly — 1 viewport, 1 locale, 12 pages, reduced-motion emulation confirmed live, 0 blocking / 0 required failures, 150 `[data-lm]` elements all landing with final opacity. The Step 1D IT-LTR 8-viewport sweep remains valid and underwrites the layout contract. The P0-5 footer-href side-check adds 36 / 36 real-route anchors as live-verified data. This is enough browser-live evidence to promote the archetype from No-Go to Conditional-Go.

- **For Go (plan §10.3) / Solaria Commit B re-entry**: **no**. The rubric §5–§7 bar requires 5 locales × 6 pages × 4 core viewports per template (≥ 120 screenshots/template, 240/cluster) and an AP8 end-to-end Fiscus scorecard. The current Playwright corpus is:
  - `x4a-step1d/20260424T2300Z/` — IT LTR, 8 viewports × 6 pages × 2 templates (responsive focus).
  - `x4a-step2/20260424T2346Z/reduced-motion/` — IT LTR, 1 viewport × 6 pages × 2 templates (JS-motion focus).

  Summed, that is **~2 × 52** IT-LTR cells — roughly a fifth of the per-template locale bar, zero of the RTL bar, zero of the AP8 pipeline scorecard evidence. BRWS-FEEL-05 (voice anchor verbatim across 5 locales) is unverified on 4 / 5 locales.

**Verdict for this section**: browser-live evidence is **necessary but not sufficient** for Go. It is **sufficient** for Conditional-Go. The delta to Go is the P1 bundle (walks V2 + V3 + AP8 Fiscus scorecard). Nothing smaller than that closes the gap.

---

## 4 · What is now archetype-grade vs still fragile

### Archetype-grade (promoted from Step 1 or Round 1)

These are contracts + evidence that would survive a regression attempt without manual re-discovery.

- **Palette safety**: `theme_safety.is_primary_safe_on_cream` + `corporate_suite.E001` build-time error. CI will fail on any fourth corporate-suite template that reintroduces a cream-family primary.
- **Imagery policy** (non-legacy pools): `enforce_corporate_suite_imagery_policy` + `corporate_suite.E002/E003` errors. CI fails on a non-Pexels URL outside the grandfather.
- **Legacy grandfather visibility**: `corporate_suite.W001` surfaces `business-corporate` on every `manage.py check` — the grandfather can no longer be forgotten silently.
- **Footer legal CTA wiring**: `CS-CTA-04` now has a static-test floor + live-walk floor on both enrolled templates.
- **Reduced-motion JS contract**: `live-motion.js` `matchMedia` branch + `_base.html` `@media (prefers-reduced-motion: reduce)` block, verified live on 150 `[data-lm]` hooks across 12 pages.
- **Gatekeeper CRITICAL list**: `(D1, D2, D3, D4, D10, D11, D12, D13, D14)` pinned in four edit sites, matches scorecard.
- **Canonical CI transcript**: 171 OK, 2.213 s, dated and retained under `step2-ci/`.
- **IT-LTR responsive layout** (carried from Step 1D): 8-viewport sweep × 6 pages × 2 templates, no horizontal scroll, hamburger drawer at ≤ 880.
- **Static-test set at 40 `CorporateSuite*Tests` lines**: build-time checks + skin contracts + rhythm + imagery + theme, all green at the branch tip.

### Still fragile (gating work for Go)

- **Multi-locale (EN · FR · ES) live walks**: no evidence. T-P1-1 deliverable.
- **RTL (AR) live walk**: no evidence. T-P1-2 deliverable. Especially load-bearing at 390 × 844 for Kufi + Amiri glyph metrics.
- **AP8 end-to-end pipeline run**: never done. T-P1-3 deliverable. First instance of every SOP §6 report schema + the aggregated `release-gatekeeper` scorecard.
- **D-054 triangulation**: stale on Pragma + Fiscus for a three-template future. T-P1-4 deliverable.
- **Primary-CTA paper-surface decision**: unresolved. T-P1-5 deliverable (documented decision regardless of direction).
- **Pragma Pexels retro-pack**: grandfather in place; deferrable-past-Solaria per plan §5 but must be cited on first gatekeeper scorecard. T-P2-1 deliverable.
- **Ghost CTA 44 × 44 touch-target**: standing waiver; decision deferred to T-P2-3.
- **Fiscus KPI band D12 candidate**: tracked for P1 contrast audit; not quantified yet.
- **Preview-composition HTML + tile PNGs**: out of X.4a scope by constraint; fragility, not regression.
- **`release-gatekeeper` prompt itself**: correct on paper, untested in the field until T-P1-3.

---

## 5 · Explicit verdict

**CONDITIONAL GO**, per plan §10.2.

Basis (each row required):

- Every P0 task closed with evidence (T-P0-1 … T-P0-6) ✓
- Canonical dated test transcript captured at the hardening-followup tip (`test-run-20260424T2346Z.txt`) ✓
- Reduced-motion walk V1 PASS on both enrolled templates (`x4a-step2/20260424T2346Z/reduced-motion/verdict.md`) ✓
- Gatekeeper agent prompt CRITICAL list matches the authoritative scorecard list ✓

Conditional Go unblocks **Step 2 P1 work**. It does **not** un-pause Solaria Commit B. Plan §10.2 is explicit: *"The verdict is Conditional-Go, not Go — it unblocks Step 2 P1 work but does not un-pause Solaria."*

A full **Go** verdict requires the P1 bundle (T-P1-1 through T-P1-5) to close with the walk-evidence structure in plan §6.2 / §6.3 / §6.4. Only at Go does Solaria Commit B become eligible for user-authorized un-pause.

**This is NOT a No-Go.** The Round 2 live walk and the P0 build-time gate transcripts are load-bearing; re-doing Round 1 would produce no new information.

---

## 6 · Strict rules for controlled Solaria re-entry (conditional-go scope)

> **Solaria Commit B re-entry is NOT authorized under Conditional Go.** It is authorized only at Go (§10.3) **plus** explicit user un-pause instruction.

The rules below therefore take two forms: (a) rules that apply **during** Step 2 P1 execution so Solaria cannot accidentally be un-paused, and (b) rules that will apply **when** Solaria re-enters after Go issues.

### 6.1 · During Step 2 P1 execution (binding now)

- **R-SOL-1 · No Solaria-scope planner activity.** T-P1-1 / T-P1-2 Playwright walks address Pragma + Fiscus only. The `browser-verifier` scope brief must not list any Solaria page or locale.
- **R-SOL-2 · No Solaria branch rebasing / merging.** `phase-x4-wave2-solaria-coaching-v1` stays untouched on its local state. No pull into `phase-x4a-corporate-factory-hardening-followup`.
- **R-SOL-3 · No Solaria content files edited.** `apps/catalog/template_content_solaria*.py` (if they exist) untouched. T-P1-4 refresh touches Pragma + Fiscus docstrings only.
- **R-SOL-4 · No Solaria palette / imagery / schema edits.** Build-time checks are now errors; any Solaria content surface change would fail `manage.py check` before review, which is the gate's purpose.
- **R-SOL-5 · Constraint B3 stays in force.** Zero edits to `apps/editor`, `apps/projects`, `apps/commerce` through P1.
- **R-SOL-6 · Constraint B4 stays in force.** No new archetypes introduced during Step 2.
- **R-SOL-7 · Parallel-walk hygiene.** If V2 / V3 run in overlapping sessions, they must use distinct dev-server ports (`:8731`, `:8732`, …) per constraint B8. Evidence sets must not collide.

### 6.2 · At and after Go (will apply once Go issues)

- **R-SOL-8 · User un-pause is a separate discrete instruction.** A Go verdict does not trigger un-pause. Solaria Commit B re-enters only after an explicit user authorization message.
- **R-SOL-9 · Solaria enters the **same** 10-agent pipeline that passed on Fiscus in T-P1-3.** No shortcut path; the pipeline that has been exercised once on a known-good template is the pipeline Solaria must clear.
- **R-SOL-10 · First Solaria scorecard must cite `O7` grandfather explicitly.** If `LEGACY_EXEMPT_KEYS` still contains `business-corporate` at that point, the `release-gatekeeper` scorecard must quote the exemption line verbatim. This is the rubric-discipline test for the grandfather arrangement.
- **R-SOL-11 · Solaria must refresh its own D-054 triangulation.** Planner briefs must triangulate against both Pragma and Fiscus with the **refreshed** docstrings from T-P1-4.
- **R-SOL-12 · Solaria palette must pass `corporate_suite.E001` build-time check.** The Solaria Commit A bug palette `#F7F3EC` was the whole reason for the gate. First Solaria walk must run `manage.py check apps.catalog` and capture the green transcript under `factory/reports/build/solaria-*/`.
- **R-SOL-13 · Solaria imagery pool must be Pexels-only.** Solaria is **not** grandfathered. Any non-Pexels URL fires `corporate_suite.E002` and stops the walk.
- **R-SOL-14 · Solaria must pass the full rubric matrix it inherits.** 5 locales × 6 pages × 4 core viewports (≥ 120 screenshots); BRWS-FEEL-05 verbatim on each locale; reduced-motion walk at 1440 × 900.
- **R-SOL-15 · Any failure in Solaria's first walk loops via `template-editor-fixer` → re-walk, not via "pause + fix offline".** The pipeline is the pipeline; the loop is the loop.

---

## 7 · What must still be validated live (to move Conditional Go → Go)

The five P1 tasks, with the live-validation focus each one delivers.

### 7.1 · T-P1-1 · Multi-locale LTR walk V2 (EN · FR · ES)

- Pragma + Fiscus × 3 locales × 6 pages × ≥ 4 core viewports = **≥ 144 screenshots per template, 288 cluster-total**.
- Checks from `browser-rubric.md §6`: BRWS-FEEL-05 voice anchor verbatim per locale; BRWS-CONTRAST-01..04 at 1440 × 900 per locale; BRWS-RESP-01..07 at the full viewport sweep per locale; BRWS-NAV-01..06 on the drawer breakpoint per locale.
- Exit: 0 `[BLOCKING]`, 0 `[REQUIRED]`, all deviations logged.
- Evidence: `factory/reports/browser-verification/x4a-step2/<run-ISO>/multi-locale-ltr/`.

### 7.2 · T-P1-2 · RTL (AR) walk V3

- Pragma + Fiscus × AR × 6 pages × ≥ 4 core viewports = **≥ 48 screenshots per template, 96 cluster-total**; 8-viewport sweep optimal.
- Checks: `html[dir="rtl"]` confirmation; logical-property flips on nav + footer + hero credit + KPI + case rows; `.cs-kpi-band .stat .num` keeps Latin digits; focus-visible gold outline survives `dir="rtl"`; no horizontal scroll; Noto Kufi / Amiri metrics do not overflow nav at 768 or 390.
- Exit: 0 `[BLOCKING]`, 0 `[REQUIRED]`.
- Evidence: `factory/reports/browser-verification/x4a-step2/<run-ISO>/rtl-ar/`.

### 7.3 · T-P1-3 · AP8 first end-to-end pipeline run on Fiscus

- Full 10-agent sequence per SOP §4.1: planner retro → curator reviewer → copy-translation verbatim → builder CI → style-critic → contrast-accessibility → responsive → browser-verifier → (editor-fixer loop if needed) → release-gatekeeper aggregation.
- One instance of every SOP §6 report schema lands on disk.
- Including a contrast sample for the Fiscus KPI band defect candidate S5.
- Exit: `release-gatekeeper` issues scorecard Layer 1 / 2 / 3 clear, parallel-verification handshake signed by the user.
- Evidence: `factory/reports/{plans,imagery,copy,build,scorecard,browser-verification}/fiscus-commercialista/<run-ISO>/...`.

### 7.4 · T-P1-4 · D-054 triangulation refresh (Pragma + Fiscus)

- Planner-driven module-docstring update in `template_content_pragma.py` + `template_content_fiscus.py`. Zero content changes.
- Each docstring triangulates against the other sibling **and** against Solaria-as-placeholder so the shape is three-template-ready for the un-pause.
- Style-critic reads both docstrings and confirms triangulation phrasing, not summary phrasing.
- Must land **after** T-P1-3 (the Fiscus re-walk exercises current-state docstrings as-is; refreshing before the re-walk conflates two signals).

### 7.5 · T-P1-5 · Primary-CTA paper-surface solid-variant decision

- Style-critic memo → design-standard `§ decision` block → optional skin-edit + static-test if adopted.
- Non-negotiable: a decision must exist in the standards file regardless of direction.

### 7.6 · Live-validation sampling summary

Minimum Playwright-cell count the P1 walks add to the corpus:

- V2: **≥ 288** cells (2 templates × 3 locales × 6 pages × 4 core viewports, floor).
- V3: **≥ 96** cells (2 templates × 1 locale × 6 pages × 4+ core viewports, floor).
- V4 (P1-3 browser-verifier leg): overlap with V2/V3 for Fiscus locales; incremental cells are 0 if they execute first, else re-validation.

Rubric floor for the cluster post-Go: **≥ 120 screenshots per template × 2 = 240 minimum**. Target with the P1 bundle: **~384 screenshots** with the current Round-1 IT-LTR screenshot count folded in. The floor is clearable.

---

## 8 · Do the P0 outputs themselves require rework?

Reviewed for self-consistency against the standards; **no rework required**.

- `corporate_suite.E001/E002/E003/W001` ids align with `blocking-rules.md §21` ID-space convention (dotted lowercase with a 4-char code). Warning vs Error split matches plan §3 T-P0-2 spec.
- `CorporateSuiteBuildTimeCheckTests` covers green path and injected red path — the test's red-path assertion is the specific contract that protects the Solaria `#F7F3EC` regression class.
- `CorporateSuiteChromeContractTests.test_footer_legal_hrefs_are_not_placeholder_hashes` contract matches `CS-CTA-04` wording.
- `release-gatekeeper.md` final CRITICAL list reads `(D1, D2, D3, D4, D10, D11, D12, D13, D14)` verbatim at §1 / §3.1 / §4; no lingering `D9` reference as CRITICAL.
- Round 2 `verdict.md` structure conforms to `browser-rubric.md §11` template (walk run, server, scope, counts, per-page measurements, per-check pass/fail with evidence, verdict).

If at any point a reviewer re-opens one of the Round 1 artefacts and finds a contradiction, the remediation is a **delta** via `template-editor-fixer` followed by a re-run — not a re-do of Round 1.

---

## 9 · Final verdict · plain language

**Controlled Solaria re-entry is NOT yet justified.** The archetype has moved from No-Go to Conditional Go, which unblocks the P1 bundle but not Solaria. Another follow-up hardening round — **Round 2 focused on the P1 bundle** (multi-locale LTR walk, RTL AR walk, AP8 end-to-end Fiscus pipeline run, D-054 triangulation refresh, primary-CTA paper-surface decision) — is required first, followed by a Go verdict per plan §10.3 and then an explicit user un-pause of Solaria Commit B.

— end of Step 2 readiness reassessment —
