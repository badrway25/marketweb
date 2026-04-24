# Corporate-suite Factory Hardening · Step 2 · Execution Round 1

**Phase**: X.4a · **Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at execution start**: `0727aad` (Step 1D closed).
**Run-ISO**: `20260424T2346Z`
**Driver**: Claude (Opus 4.7, Playwright MCP for live walk).
**Scope**: Priority 1 (P0) tasks from `factory/reports/hardening/step2-followup-plan.md §3`. P1 / P2 NOT executed — P0 gate is a prerequisite per the plan's "Never squash P0 and P1" sequencing rule.
**Binding constraints honoured**: no edits to `apps/editor`, `apps/projects`, `apps/commerce`; no new archetypes; no Solaria Commit B un-pause; every write stays under `factory/*` or the `corporate-suite` archetype surface + the `apps/catalog/*` archetype-gated helpers.

---

## Priority 1 tasks executed

### T-P0-1 · Build-time palette gate (CS-PAL-01 → `django.core.checks.Error`) — **DONE**

- New module `apps/catalog/checks.py`:
  - `check_corporate_suite_palettes(app_configs, **kwargs)` iterates every enrolled corporate-suite slug from `SEED_TEMPLATES` (paired with `TEMPLATE_DNA` for archetype filter), runs `theme_safety.is_primary_safe_on_cream`, and emits `django.core.checks.Error` with id `corporate_suite.E001` on failure.
  - Paired `check_corporate_suite_imagery` for T-P0-2 (see below).
- `apps/catalog/apps.py` `ready()` registers both checks via `django.core.checks.register(…, Tags.compatibility)`. They run on every `manage.py check` + `manage.py test`.
- Evidence:
  - Clean run: `factory/reports/hardening/step2-ci/check-clean-20260424T2345Z.log` — 0 errors on enrolled state (Pragma `#1E293B` + Fiscus `#1F2937` both pass).
  - Failing run (Solaria bug palette `#F7F3EC` injected): `factory/reports/hardening/step2-ci/check-failing-palette-20260424T2345Z.log` — `[corporate_suite.E001] corporate-suite template '__solaria-prefix-bug__' ships an unsafe primary '#F7F3EC' (luminance=0.8993, contrast-vs-cream=1.01)`. Known-bad palette is now build-time fatal.

### T-P0-2 · Build-time imagery-policy gate (CS-IMG-SRC-01 → `django.core.checks.Error`) — **DONE**

- `check_corporate_suite_imagery` (same module) iterates `CORPORATE_SUITE_POOL_KEYS`, skips unregistered keys, emits:
  - `corporate_suite.E002` (Error) for any non-Pexels URL in a non-legacy-exempt pool;
  - `corporate_suite.E003` (Error) for non-canonical pool shape;
  - `corporate_suite.W001` (Warning) for the grandfathered `business-corporate` pool (Pragma) so the O7 precondition stays visible without blocking CI.
- Evidence:
  - Clean run captured the W001 Pragma grandfather line (0 errors, 1 warning).
  - Failing run (Unsplash URL injected into `business-coaching`): `factory/reports/hardening/step2-ci/check-failing-imagery-20260424T2345Z.log` — `ERROR [corporate_suite.E002] corporate-suite imagery pool 'business-coaching' ships 1 non-Pexels url(s)`. Gate fires as specified.

### T-P0-3 · Release-gatekeeper CRITICAL list alignment — **DONE**

- `factory/agents/release-gatekeeper.md` edited at three call sites to match the authoritative list in `factory/standards/corporate-suite-quality-scorecard.md §3/§5/§6` — `D9` (Imagery quality, non-critical) swapped for `D3` (Modern professionalism, critical):
  - §1 one-liner CRITICAL list.
  - §3.1 Layer-2 critical-dimension floor sample table (D3 row promoted to CRITICAL; D9 row moved to non-critical with ≥ 3 floor).
  - §4 ship-criteria checklist rows (both "CRITICAL all ≥ 4" and "non-critical all ≥ 3" lines).
- Final CRITICAL list: `(D1, D2, D3, D4, D10, D11, D12, D13, D14)` — matches scorecard.

### T-P0-4 · AP12 reduced-motion walk V1 via Playwright MCP — **DONE**

- Evidence directory: `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/`.
- 12 full-page screenshots (Pragma + Fiscus × 6 pages each @ 1440 × 900) + `verdict.md`.
- `page.emulateMedia({ reducedMotion: 'reduce' })` applied at context level; confirmed active live via `window.matchMedia` on each page.
- Result: **PASS** · 0 stuck `[data-lm]` across 150 motion elements / 12 pages / 2 templates. Console clean (favicon 404 only).

### T-P0-5 · Footer `href="#"` resolution (CS-CTA-04) — **DONE**

- `templates/live_templates/business/corporate-suite/_base.html` footer legal row: 3 `href="#"` placeholders replaced with `{% url 'catalog:live_template_page' … %}` wiring resolving to the `contatti` page by default, overrideable per-template via optional `site.privacy_href` / `site.cookie_href` / `site.legal_href` slug fields. Locale query-string preserved (`?lang=<locale>` when not default).
- New static test in `apps/catalog/tests.py` (`CorporateSuiteChromeContractTests.test_footer_legal_hrefs_are_not_placeholder_hashes`) asserts (a) no `href="#"` inside `<span class="legal">`, (b) exactly 3 anchors, (c) each uses `live_template_page` resolver.
- Live spot-check: every one of the 12 walked pages renders the footer with real routes (see walk `verdict.md`).

### T-P0-6 · Canonical dated test transcript — **DONE**

- `factory/reports/hardening/step2-ci/test-run-20260424T2346Z.txt` — full `python manage.py test apps.catalog -v 2` transcript at the hardening-followup tip.
- **171 tests · OK · 2.213 s**. 40 `CorporateSuite*Tests` lines present:
  - `CorporateSuiteThemeSafetyTests`     · 8 (unchanged from Step 1A).
  - `CorporateSuiteChromeContractTests`  · 18 (+1 from Step 2 P0-5 footer-href contract).
  - `CorporateSuiteImageryPolicyTests`   · 6 (unchanged from Step 1C).
  - `CorporateSuiteRhythmContractTests`  · 8 (unchanged from Step 1C).
  - `CorporateSuiteBuildTimeCheckTests`  · 7 new (P0-1 / P0-2 registration + green + injected-red contracts).

---

## Files changed

```
Code (archetype-level, within factory scope)
  apps/catalog/checks.py                                    (new · ~160 loc · checks module)
  apps/catalog/apps.py                                      (+ ready() register block)
  apps/catalog/tests.py                                     (+ 8 tests: 7 BuildTimeCheck + 1 footer-href)
  templates/live_templates/business/corporate-suite/_base.html  (footer legal row · 3 anchors)

Docs / factory-tree
  factory/agents/release-gatekeeper.md                      (CRITICAL list D9→D3 · 4 edit sites)

Evidence
  factory/reports/hardening/step2-ci/check-clean-20260424T2345Z.log
  factory/reports/hardening/step2-ci/check-failing-palette-20260424T2345Z.log
  factory/reports/hardening/step2-ci/check-failing-imagery-20260424T2345Z.log
  factory/reports/hardening/step2-ci/test-run-20260424T2346Z.txt
  factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/
      ├── verdict.md
      └── screenshots/  (12 PNG, full-page, 1440×900, reduced-motion emulated)
  factory/reports/hardening/step2-execution-round1.md       (this file)
  factory/reports/browser-verification/x4a-hardening-round2.md
```

No touches to `apps/editor`, `apps/projects`, `apps/commerce`. No new archetypes. No Solaria-scope activity. No migrations. No new routes / views.

---

## Live browser verification evidence

- **Server**: `http://127.0.0.1:8731/` (background task `bsvroh9h4`). Server remains running for parallel user verification.
- **Driver**: Playwright MCP (`mcp__plugin_playwright_playwright__*`).
- **Reduced-motion emulation**: `page.emulateMedia({ reducedMotion: 'reduce' })` applied to context; verified live via `matchMedia('(prefers-reduced-motion: reduce)').matches === true` on every page.
- **Viewport matrix**: 1440 × 900 (per plan §6.1 — motion is a JS contract, not a layout one).
- **Pages walked**: 12 (Pragma home / chi-siamo / competenze / case-studies / case-studies/manifatturiero-bresciano-piano-industriale / contatti; Fiscus home / lo-studio / competenze / casi-seguiti / casi-seguiti/pmi-manifattura-bilancio-revisione / contatti).
- **`[data-lm]` stuck-invisible cases**: **0 / 150**.
- **JS errors in console**: **0** (favicon 404 waived).
- **Footer legal hrefs rendered**: **36 / 36 real-route anchors** (zero `href="#"` placeholders).
- **T-P0-5 side-check**: visible in each screenshot — "PRIVACY · COOKIE · NOTE LEGALI" anchors on the footer's legal row resolve to the contatti page.

Rubric verdict on the P0-4 walk: **PASS** (0 `[BLOCKING]`, 0 `[REQUIRED]` failures). Full detail in `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/verdict.md`.

---

## Remaining blockers after Round 1

### Inside P0 scope · residual items to close the P0 gate

- **P0-GATE-1** — commits `C-P0-1` … `C-P0-6` not yet landed on the branch; this execution round produced the evidence + code diffs in a single working tree. Sequencing per plan §7: split into commits before calling the P0 gate closed. **Not a blocker for the Round 1 execution report itself**; the user/owner decides when to commit.
- **P0-GATE-6** — `release-gatekeeper` has not yet authored `factory/reports/hardening/step2-conditional-go.md`. The aggregator step is scheduled after commits land.

### Outside P0 scope · pre-existing, tracked

- **B1** — Solaria Commit B remains paused (binding user instruction). Unchanged.
- **B2** — `LEGACY_EXEMPT_KEYS = {business-corporate}` still holds. The new imagery-gate `corporate_suite.W001` warning keeps it visible on every `manage.py check` run (O7 precondition satisfied).
- **B7** — `templates/preview_compositions/business/corporate-suite.html` untouched (out of Step 2 scope).
- **P1 bundle** — T-P1-1 (multi-locale LTR walk), T-P1-2 (RTL AR walk), T-P1-3 (AP8 end-to-end Fiscus pipeline), T-P1-4 (D-054 triangulation refresh), T-P1-5 (primary-CTA paper-surface solid-variant decision) remain open. Required before Solaria Commit B re-entry per §4 of the plan.
- **P2 bundle** — T-P2-1 (Pragma Pexels retro-pack), T-P2-2 (pack metadata validator), T-P2-3 (ghost CTA touch-target), T-P2-4 (URL-reuse request-path check), T-P2-5 (sticky-nav scrolled-state). Deferrable past Solaria per plan §5.

### Borderline live-walk observation (tracked, not P0 scope)

- **Fiscus case-study detail KPI band contrast** — the bottom `.cs-kpi-band` on `casi-seguiti/pmi-manifattura-bilancio-revisione` reads as visually low-contrast (digits + captions on the dark navy). This is a D12 (Contrast safety) spot worth a formal contrast audit during the P1 walk. Not a reduced-motion defect; tracked here so the P1 browser-verifier picks it up.

---

## Recommendation: another hardening round or readiness reassessment

**Recommendation**: **Readiness reassessment is justified**, upgrading from **No-Go** (tip `0727aad`) to **Conditional-Go** per the plan §10.2 definition. All six P0 tasks are green with artefacts:

| §10.2 condition | State after Round 1 |
|---|---|
| Every P0 task green (T-P0-1 … T-P0-6) | ✅ all 6 executed + evidenced |
| Canonical test transcript at the hardening-followup branch tip | ✅ `step2-ci/test-run-20260424T2346Z.txt` · 171 OK |
| Reduced-motion walk V1 PASS with BRWS-FEEL-08 green on both LIVE templates | ✅ `verdict.md` · 12/12 PASS · 0 stuck |
| Gatekeeper agent prompt CRITICAL list matches the scorecard | ✅ `(D1, D2, D3, D4, D10, D11, D12, D13, D14)` |

The blocker on the full **Go** verdict (§10.3) is the P1 bundle, not any residual P0 item. A second hardening round — focused on P1 — is justified and recommended; it does **not** require an interstitial P0 re-run.

**Not recommended yet**: issuing the "Go" verdict, un-pausing Solaria Commit B, or propagating corporate-suite contracts to sibling archetypes (per plan §5 + binding B3/B4).

— end of Round 1 execution report —
