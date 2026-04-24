# Corporate-suite Factory Hardening · Step 2 · Follow-up checklist

**Phase**: X.4a · **Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Companion document**: `factory/reports/hardening/step2-followup-plan.md` (narrative plan · this file is the operational punch list).
**Baseline**: tip `0727aad` (Step 1D closed).
**Binding constraints** (carried from the plan):

- No Solaria Commit B un-pause under any item in this checklist.
- No edits to `apps/editor`, `apps/projects`, `apps/commerce`.
- No new archetypes.
- All writes stay under `factory/*` or inside the `corporate-suite` archetype surface (skin + page files) or the `apps/catalog/` archetype-gated helpers (`theme_safety.py`, `imagery_policy.py`, and any new archetype-gated check module).
- Every checklist item that claims completion MUST have a filesystem artifact under `factory/reports/` (commit hash + evidence path).

Completion symbols: `[ ]` pending · `[~]` in-flight · `[x]` done · `[!]` blocked (see notes).

---

## 0 · Preflight · on branch `phase-x4a-corporate-factory-hardening-followup`

- [ ] **0.1** Confirm branch tip matches expected baseline (`0727aad`) or a direct descendant.
- [ ] **0.2** Confirm `git status` is clean except the two Step 2 planning files (`factory/reports/hardening/step2-followup-plan.md`, this file).
- [ ] **0.3** Confirm `python manage.py check` exits 0 on the hardening-followup branch tip (transcript NOT required yet — this is a preflight smoke only).
- [ ] **0.4** Confirm no stray `.pyc` / editor-swap files under `apps/catalog/` that could leak into a P0 commit.

---

## 1 · Reasons for No-Go (reference · for reviewer cross-check)

This section is a read-only reference restating §1 of the plan. Do not mark items here.

- R1 · Browser walk coverage is IT LTR only (≈ 6 % of rubric surface).
- R2 · Systemic preconditions from `template-inventory.md §7` are partially open (AP8, AP10, AP12, AP3 soft, gatekeeper D3/D9 fix).
- R3 · Palette + imagery contracts are runtime-only (`UserWarning`); no build-time fail surface.
- R4 · `.cs-foot` `href="#"` placeholders on enrolled templates; ghost CTA touch-target waiver on mobile.
- R5 · `LEGACY_EXEMPT_KEYS = {business-corporate}` (Pragma legacy Unsplash).
- R6 · Multi-agent pipeline has not run end-to-end once under populated prompts.
- R7 · Gatekeeper agent prompt CRITICAL list mismatches the scorecard (`D9` vs `D3`).
- R8 · No canonical dated test transcript at the hardening-followup branch tip.

---

## 2 · P0 · unblocks "ready to plan un-pause"

### 2.1 · T-P0-1 · Build-time palette gate

- [ ] **T-P0-1.a** Design: choose implementation surface — `django.core.checks.register` in `apps/catalog/apps.py` (ready event) OR a dedicated `apps/catalog/management/commands/check_corporate_suite_palettes.py`. Both are acceptable; the `checks.register` path has the advantage of firing on every `manage.py check` invocation automatically.
- [ ] **T-P0-1.b** Implementation: wire `theme_safety.is_primary_safe_on_cream` over every enrolled slug whose `archetype == "corporate-suite"`. Emit a `django.core.checks.Error` (severity `ERROR`) per offending slug. Return `[]` if all pass.
- [ ] **T-P0-1.c** Tests: add a focused test class (pattern: `CorporateSuiteThemeSafetyTests`) that asserts (i) green on Pragma + Fiscus, (ii) `Error` raised against the known-bad Solaria pre-fix palette `#F7F3EC` (temp-injected via `override_settings` or a palette-dict fixture).
- [ ] **T-P0-1.d** Verify: `python manage.py check apps.catalog -v 2` exits 0 on clean state; synthetic palette injection exits non-zero with the expected `Error` id.
- [ ] **T-P0-1.e** Evidence: capture transcripts `factory/reports/hardening/step2-ci/palette-gate-clean-<ISO>.log` and `.../palette-gate-failing-<ISO>.log`.
- [ ] **T-P0-1.f** Commit (`C-P0-1`): `apps/catalog/{theme_safety.py,checks.py,apps.py,tests.py}` + evidence files. Message: `X.4a step2 P0-1: promote corporate-suite palette safety to django.core.checks`.

### 2.2 · T-P0-2 · Build-time imagery-policy gate

- [ ] **T-P0-2.a** Design: wrap `enforce_corporate_suite_imagery_policy` in the same `checks.register` or `manage.py` management-command pattern as T-P0-1.
- [ ] **T-P0-2.b** Implementation: iterate every registered key in `CORPORATE_SUITE_POOL_KEYS`, subtract `LEGACY_EXEMPT_KEYS`, check each URL's host is `images.pexels.com`, fail on any mismatch.
- [ ] **T-P0-2.c** Tests: `CorporateSuiteImageryPolicyTests` extension — green on Fiscus, green on Pragma (legacy-exempt), red when a synthetic non-Pexels URL is injected into a non-exempt pool.
- [ ] **T-P0-2.d** Verify: `python manage.py check apps.catalog -v 2` exits 0 on the current state (Pragma silent via legacy exemption, Fiscus compliant).
- [ ] **T-P0-2.e** Evidence: `factory/reports/hardening/step2-ci/imagery-gate-clean-<ISO>.log` + `.../imagery-gate-failing-<ISO>.log`.
- [ ] **T-P0-2.f** Commit (`C-P0-2`): `apps/catalog/{imagery_policy.py,checks.py,tests.py}` + evidence files. Message: `X.4a step2 P0-2: promote corporate-suite imagery policy to django.core.checks`.

### 2.3 · T-P0-3 · Release-gatekeeper CRITICAL list alignment

- [ ] **T-P0-3.a** Read: `factory/agents/release-gatekeeper.md §1` — current CRITICAL list `(D1, D2, D4, D9, D10, D11, D12, D13, D14)`.
- [ ] **T-P0-3.b** Cross-check authoritative: `factory/standards/corporate-suite-quality-scorecard.md §3` and `§5` and `§6` — authoritative list `(D1, D2, D3, D4, D10, D11, D12, D13, D14)`.
- [ ] **T-P0-3.c** Edit: swap `D9` for `D3` in the gatekeeper prompt. Confirm no other section of the prompt references the old list.
- [ ] **T-P0-3.d** Commit (`C-P0-3`): `factory/agents/release-gatekeeper.md`. Message: `X.4a step2 P0-3: align release-gatekeeper CRITICAL list with scorecard §3`.

### 2.4 · T-P0-4 · AP12 reduced-motion walk V1

- [ ] **T-P0-4.a** Start dev server on a deterministic port (e.g. `127.0.0.1:8731`). Record URL in `walk-log.md`.
- [ ] **T-P0-4.b** Create evidence directory `factory/reports/browser-verification/x4a-step2/<run-ISO>/reduced-motion/`.
- [ ] **T-P0-4.c** Playwright: `browser_emulate_media` with `reducedMotion: 'reduce'`.
- [ ] **T-P0-4.d** Walk Pragma home + about + services + case-study list + case-study detail + contact, at 1440 × 900 only. Capture full-page screenshot per page.
- [ ] **T-P0-4.e** Walk Fiscus home + about + services + case-study list + case-study detail + contact, same viewport. Capture.
- [ ] **T-P0-4.f** Confirm per page: no `[data-lm]` element at `opacity: 0`; no `transform: translateY(24px)` stuck; console clean apart from favicon 404.
- [ ] **T-P0-4.g** Write `verdict.md` conformant to `corporate-suite-browser-rubric.md §11`. Verdict: PASS / BORDERLINE / FAIL.
- [ ] **T-P0-4.h** If FAIL: escalate to `template-editor-fixer` to audit `static/js/live-motion.js` for `matchMedia('(prefers-reduced-motion: reduce)')` branch; re-walk at fresh `<run-ISO>`.
- [ ] **T-P0-4.i** Commit (`C-P0-4`): evidence tree only — no code in this commit unless an editor-fixer diff was required (then a separate rework commit precedes this one).

### 2.5 · T-P0-5 · Footer `href="#"` resolution

- [ ] **T-P0-5.a** Inventory: grep `_base.html` and the 6 page files for `href="#"`. Confirm only the 3 footer legal slots (privacy, cookie, legal) match + confirm no accidental new ones.
- [ ] **T-P0-5.b** Choose wiring strategy: either `site.privacy_url` / `site.cookie_url` / `site.legal_url` on the site-config primitive OR `{% url %}` tags to existing i18n legal pages. Document choice under `factory/reports/hardening/step2-ci/footer-href-decision.md`.
- [ ] **T-P0-5.c** Edit `_base.html` footer block only. No structural markup change. No non-footer touch.
- [ ] **T-P0-5.d** If new site-config fields are introduced, add them under `apps.core` (site-config primitive scope) with migration + test. If reusing existing fields, skip this step.
- [ ] **T-P0-5.e** Static tests: extend `CorporateSuiteChromeContractTests` — `.cs-foot .bot .legal a` must not contain `href="#"`.
- [ ] **T-P0-5.f** Live spot-check in dev server: Pragma footer at 1440 × 900, click each legal link, confirm it resolves to a real page (no 404).
- [ ] **T-P0-5.g** Commit (`C-P0-5`): skin + tests + evidence. Message: `X.4a step2 P0-5: resolve footer legal href placeholders to real routes`.

### 2.6 · T-P0-6 · Canonical dated test transcript

- [ ] **T-P0-6.a** Confirm branch tip includes commits C-P0-1 through C-P0-5 (or their counterparts if sequencing shifted).
- [ ] **T-P0-6.b** Execute: `python manage.py test apps.catalog -v 2 > factory/reports/hardening/step2-ci/test-run-<ISO>.txt 2>&1`.
- [ ] **T-P0-6.c** Inspect transcript: every `CorporateSuite*Tests` class must run and pass. Count must match expected (Step 1 baseline was 28 new tests in the Corporate-suite cluster; Step 2 additions land this number higher).
- [ ] **T-P0-6.d** Commit (`C-P0-6`): transcript file only. Message: `X.4a step2 P0-6: canonical apps.catalog CI transcript at hardening-followup tip`.

### 2.7 · P0 closure gate (must clear before any P1 work starts)

- [ ] **P0-GATE-1** All 6 P0 commits landed on `phase-x4a-corporate-factory-hardening-followup`.
- [ ] **P0-GATE-2** All P0 evidence files present under `factory/reports/hardening/step2-ci/` and `factory/reports/browser-verification/x4a-step2/`.
- [ ] **P0-GATE-3** Reduced-motion walk V1 verdict = PASS.
- [ ] **P0-GATE-4** Gatekeeper prompt CRITICAL list = `(D1, D2, D3, D4, D10, D11, D12, D13, D14)`.
- [ ] **P0-GATE-5** Palette check produces Error on injected `#F7F3EC`; imagery check produces Error on injected non-Pexels URL.
- [ ] **P0-GATE-6** `release-gatekeeper` writes `factory/reports/hardening/step2-conditional-go.md` citing each row above. Verdict: **Conditional-Go**.

---

## 3 · P1 · unblocks Solaria Commit B re-entry

### 3.1 · T-P1-1 · Multi-locale LTR walk V2 (EN · FR · ES)

- [ ] **T-P1-1.a** Preflight: P0-GATE-6 is green; dev server running; `browser-verifier` agent brief is populated with the walk scope (2 templates × 3 locales × 6 pages × 8 viewports).
- [ ] **T-P1-1.b** Evidence dir `factory/reports/browser-verification/x4a-step2/<run-ISO>/multi-locale-ltr/`.
- [ ] **T-P1-1.c** Walk Pragma EN · 6 pages · 8 viewports. Capture 4 core viewports per page (wide / std / tablet-portrait / small-phone). 24 screenshots minimum.
- [ ] **T-P1-1.d** Walk Pragma FR · same.
- [ ] **T-P1-1.e** Walk Pragma ES · same.
- [ ] **T-P1-1.f** Walk Fiscus EN · same.
- [ ] **T-P1-1.g** Walk Fiscus FR · same.
- [ ] **T-P1-1.h** Walk Fiscus ES · same.
- [ ] **T-P1-1.i** Per locale: `copy-translation-agent` verifies BRWS-FEEL-05 voice anchor rendered verbatim on hero + footer + any CTA band.
- [ ] **T-P1-1.j** Per locale: `contrast-accessibility-auditor` records BRWS-CONTRAST-01/02/03/04 ratios at 1440 × 900.
- [ ] **T-P1-1.k** Per locale: `responsive-auditor` verifies no horizontal scroll at any viewport; nav drawer engages at ≤ 880; hero stacks at ≤ 720.
- [ ] **T-P1-1.l** Write `verdict.md`. Exit criterion: 0 `[BLOCKING]`, 0 `[REQUIRED]` across 3 locales × 2 templates.
- [ ] **T-P1-1.m** Commit (`C-P1-1`): evidence tree only. Message: `X.4a step2 P1-1: multi-locale LTR walk V2 (EN·FR·ES) passes rubric`.

### 3.2 · T-P1-2 · RTL (AR) walk V3

- [ ] **T-P1-2.a** Evidence dir `factory/reports/browser-verification/x4a-step2/<run-ISO>/rtl-ar/`.
- [ ] **T-P1-2.b** Walk Pragma AR · 6 pages · 8 viewports. Special attention at 390 × 844 (Kufi + Amiri glyph width at the hero h1 32-px token).
- [ ] **T-P1-2.c** Walk Fiscus AR · same.
- [ ] **T-P1-2.d** For each page: confirm `html[dir="rtl"]`; confirm logical-property flips hold on nav, footer, hero credit, KPI band, case rows.
- [ ] **T-P1-2.e** Confirm numeric columns under `.cs-kpi-band .stat .num` keep Latin digits (RTL-Latin-numeric cascade).
- [ ] **T-P1-2.f** Confirm focus-visible gold outline survives `dir="rtl"` on nav links, primary CTA, locale pills.
- [ ] **T-P1-2.g** Confirm no horizontal scroll at any viewport (token stack is direction-invariant; this is the live check).
- [ ] **T-P1-2.h** Write `verdict.md`. Exit: 0 `[BLOCKING]`, 0 `[REQUIRED]`.
- [ ] **T-P1-2.i** Commit (`C-P1-2`): evidence tree only. Message: `X.4a step2 P1-2: RTL (AR) walk V3 passes rubric across full matrix`.

### 3.3 · T-P1-3 · AP8 end-to-end Fiscus re-walk

- [ ] **T-P1-3.a** Convene the 10-agent pipeline per `corporate-suite-multi-agent-sop.md §4.1`, scoped to Fiscus IT re-walk (all 6 pages).
- [ ] **T-P1-3.b** `template-planner` retro read: produce `factory/reports/plans/fiscus-commercialista/<run-ISO>-planner-retro.md` citing Fiscus's D-054 triangulation state (will later be refreshed in T-P1-4).
- [ ] **T-P1-3.c** `imagery-curator` reviewer pass on the existing `docs/content-factory/imagery/packs/financial-services.md` — produce `factory/reports/imagery/fiscus-commercialista/<run-ISO>-curator-reviewer.md`.
- [ ] **T-P1-3.d** `copy-translation-agent` live re-read: confirm 5/5 locales render the voice anchor verbatim — `factory/reports/copy/fiscus-commercialista/<run-ISO>-copy-verbatim.md`.
- [ ] **T-P1-3.e** `template-builder` CI re-run: `python manage.py test apps` green; `primary L*` reported; Pexels-only grep = 0 matches. `factory/reports/build/fiscus-commercialista/<run-ISO>-build-report.md`.
- [ ] **T-P1-3.f** `style-critic` walk: `factory/reports/scorecard/fiscus-commercialista/<run-ISO>-style-critic.md`.
- [ ] **T-P1-3.g** `contrast-accessibility-auditor` walk: `factory/reports/scorecard/fiscus-commercialista/<run-ISO>-contrast.md`.
- [ ] **T-P1-3.h** `responsive-auditor` walk: `factory/reports/scorecard/fiscus-commercialista/<run-ISO>-responsive.md`.
- [ ] **T-P1-3.i** `browser-verifier` runs the full Playwright walk (subsumes V2/V3 where scope overlaps): `factory/reports/browser-verification/fiscus-commercialista/<run-ISO>/verdict.md`.
- [ ] **T-P1-3.j** `template-editor-fixer` loop (only if any upstream FAIL) — minimal-diff remediation, then re-walk at fresh `<run-ISO>`.
- [ ] **T-P1-3.k** `release-gatekeeper` aggregates: `factory/reports/scorecard/fiscus-commercialista/<run-ISO>-scorecard.md` with Layer 1/2/3 verdict + user parallel-verification handshake prompt.
- [ ] **T-P1-3.l** Commit (`C-P1-3`): `factory/reports/{plans,imagery,copy,build,scorecard,browser-verification}/fiscus-commercialista/...`. Message: `X.4a step2 P1-3: AP8 closes — first end-to-end pipeline run on Fiscus passes`.

### 3.4 · T-P1-4 · AP10 D-054 triangulation refresh

- [ ] **T-P1-4.a** `template-planner` drafts refreshed module-docstring triangulation for Pragma — triangulating against Fiscus (and, if un-paused later, Solaria). 10 dimensions per `CS-EXEC-02`.
- [ ] **T-P1-4.b** `template-planner` drafts refreshed module-docstring triangulation for Fiscus — triangulating against Pragma (and Solaria when un-paused).
- [ ] **T-P1-4.c** Apply to `apps/catalog/template_content_pragma.py` and `apps/catalog/template_content_fiscus.py` — docstring only; no content changes.
- [ ] **T-P1-4.d** `style-critic` confirms the refreshed docstrings read as triangulations, not summaries.
- [ ] **T-P1-4.e** Commit (`C-P1-4`): Message: `X.4a step2 P1-4: AP10 closes — refresh D-054 triangulation on Pragma+Fiscus`.

### 3.5 · T-P1-5 · Primary-CTA paper-surface solid-variant decision

- [ ] **T-P1-5.a** `style-critic` drafts a recommendation memo under `factory/reports/hardening/step2-ci/primary-cta-paper-decision.md` — adopt `.cs-btn-primary--solid` OR keep outline; reason; samples.
- [ ] **T-P1-5.b** Document the decision in `factory/standards/corporate-suite-design-standard.md` as a `§ decision` block dated today.
- [ ] **T-P1-5.c** If adopted: `template-editor-fixer` implements the modifier in `_base.html`; `home.html` hero opts in via a `--solid` class on the primary CTA. Static test asserts the modifier's presence on the hero CTA.
- [ ] **T-P1-5.d** If rejected: close the item in `template-inventory.md §7` or corresponding tracker with the rejection rationale.
- [ ] **T-P1-5.e** Commit (`C-P1-5`): per branch chosen. Message: `X.4a step2 P1-5: primary-CTA paper-surface decision recorded`.

### 3.6 · P1 closure gate (must clear before Go verdict)

- [ ] **P1-GATE-1** All 5 P1 commits landed.
- [ ] **P1-GATE-2** V2 verdict = PASS on 2 templates × 3 locales.
- [ ] **P1-GATE-3** V3 verdict = PASS on 2 templates × AR.
- [ ] **P1-GATE-4** Fiscus end-to-end scorecard issued by `release-gatekeeper`, Layer 1/2/3 clear.
- [ ] **P1-GATE-5** Parallel-verification handshake with user signed.
- [ ] **P1-GATE-6** `release-gatekeeper` writes `factory/reports/hardening/step2-go.md`. Verdict: **Go — archetype ready for Solaria Commit B re-entry subject to explicit user un-pause**.

---

## 4 · P2 · deferrable past Solaria re-entry

Items below do NOT gate Solaria Commit B. They MUST close before the archetype's **fourth** pilot.

### 4.1 · T-P2-1 · AP3 Pragma Pexels retro-pack

- [ ] **T-P2-1.a** `imagery-curator` (primary pass) produces `docs/content-factory/imagery/packs/business-corporate.md` per `CS-IMG-COH-06` 3-line-record schema.
- [ ] **T-P2-1.b** `imagery-curator` (reviewer pass) re-runs the Pexels-host grep + license audit.
- [ ] **T-P2-1.c** `template-editor-fixer` swaps the 6 URLs in `apps/catalog/preview_imagery.py` (slot order preserved; subject/mood parity with legacy pool).
- [ ] **T-P2-1.d** Shrink `LEGACY_EXEMPT_KEYS` in `apps/catalog/imagery_policy.py` to `set()`.
- [ ] **T-P2-1.e** Re-walk Pragma home × 1440 × 900 to confirm subject/mood parity.
- [ ] **T-P2-1.f** Commit (`C-P2-1`): pack + `preview_imagery.py` + `imagery_policy.py` + evidence.

### 4.2 · T-P2-2 · Pack-file 3-line metadata + crop validator uplift

- [ ] **T-P2-2.a** Extend `imagery_policy.py` to read the pack file under `docs/content-factory/imagery/packs/<cluster>.md` and parse the 3-line per-URL records.
- [ ] **T-P2-2.b** Assert `CS-IMG-COH-06` (caption + role + coherence statement) per URL.
- [ ] **T-P2-2.c** Assert `CS-IMG-CROP-02` crop-aspect contract per slot (hero 16:9 or 4:3; portraits 4:5; detail 1:1; etc.).
- [ ] **T-P2-2.d** Soft-warn until pack is present; hard-fail for clusters with a declared-present pack.
- [ ] **T-P2-2.e** Tests extend `CorporateSuiteImageryPolicyTests`.
- [ ] **T-P2-2.f** Commit (`C-P2-2`).

### 4.3 · T-P2-3 · Ghost CTA touch-target decision

- [ ] **T-P2-3.a** `style-critic` drafts recommendation memo.
- [ ] **T-P2-3.b** If waiver made permanent: add a footnote to `CS-CTA-03` codifying the ghost = text-link exception; update `corporate-suite-browser-rubric.md §6` to explicitly exclude ghost primitives from the 44 × 44 check.
- [ ] **T-P2-3.c** If promoted: add a mobile-viewport padding rule lifting the ghost CTA to 44 × 44 without changing desktop visuals.
- [ ] **T-P2-3.d** Commit (`C-P2-3`).

### 4.4 · T-P2-4 · Cross-cluster URL-reuse at request-path layer

- [ ] **T-P2-4.a** Extend `imagery_policy.py` to index URLs across pools and fail on duplicate across different cluster keys.
- [ ] **T-P2-4.b** Tests extend `CorporateSuiteImageryPolicyTests`.
- [ ] **T-P2-4.c** Commit (`C-P2-4`).

### 4.5 · T-P2-5 · Sticky-nav scrolled-state affordance

- [ ] **T-P2-5.a** Design: IntersectionObserver sentinel at top of document, toggling `.cs-nav--scrolled`.
- [ ] **T-P2-5.b** Implementation: `static/js/corporate-suite-nav.js` (archetype-scoped); hook from `_base.html` `<script>` block at end of body.
- [ ] **T-P2-5.c** CSS: `.cs-nav--scrolled` deeper shadow + tighter height.
- [ ] **T-P2-5.d** Walk: confirm transition, confirm `prefers-reduced-motion: reduce` disables the transition without disabling the class.
- [ ] **T-P2-5.e** Commit (`C-P2-5`).

---

## 5 · Blocking conditions (reference · not action items)

Each row stays in force throughout Step 2. Mark them with a `[!]` only if discovered violated during execution (which would itself be a blocker for Step 2 closure).

- [ ] **B1** Solaria Commit B paused (binding user instruction). Confirmed in-force.
- [ ] **B2** `LEGACY_EXEMPT_KEYS = {business-corporate}` acknowledged in every gatekeeper run (`O7`).
- [ ] **B3** No `apps/editor`, `apps/projects`, `apps/commerce` edits executed during Step 2. Verified at P0 gate and at P1 gate via grep on commit diff paths.
- [ ] **B4** No new archetypes introduced. Verified at each gate.
- [ ] **B5** Every walk has `verdict.md` at `corporate-suite-browser-rubric.md §11` conformance.
- [ ] **B6** No palette hex edit on any enrolled template without planner re-approval loop.
- [ ] **B7** `preview_compositions/business/corporate-suite.html` untouched unless a specific rubric failure required it (with change documented in deviation).
- [ ] **B8** Parallel walks never share the same dev-server port.

---

## 6 · Exit criteria mapping (No-Go → Conditional-Go → Go)

- [ ] **EXIT-NO-GO-CONFIRM** · current state documented at `factory/reports/hardening/step2-followup-plan.md §10.1`.
- [ ] **EXIT-COND-GO** — issued when §2.7 (P0 gate) is fully green.
- [ ] **EXIT-GO** — issued when §3.6 (P1 gate) is fully green.

Neither exit verdict un-pauses Solaria on its own. User must explicitly authorize Solaria Commit B re-entry after EXIT-GO.

---

## 7 · Verdict for this checklist

**Current status**: all items pending. No P0 work started.
**Next action**: execute §2.1 (T-P0-1 build-time palette gate) on the `phase-x4a-corporate-factory-hardening-followup` branch, under the `template-builder` agent, with `release-gatekeeper` verifying scorecard integration. Produce evidence before committing.
**No Solaria-scope activity authorized until EXIT-GO issues per §6 + explicit user un-pause.**

— end of Step 2 follow-up checklist —
