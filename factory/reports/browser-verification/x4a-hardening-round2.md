# Corporate-suite X.4a Hardening · Round 2 · Browser Verification

**Verdict**: **PASS** (0 blocking · 0 required failures on Priority 1 scope)
**Archetype**: `corporate-suite`
**Templates walked**: `pragma-corporate-suite`, `fiscus-commercialista`
**Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at walk start**: `0727aad` (Step 1D closed) + uncommitted Step 2 Round 1 working tree.
**Walk run**: `20260424T2346Z`
**Reviewer**: Claude (Opus 4.7, Playwright MCP driver)
**Walk type**: Playwright MCP (`mcp__plugin_playwright_playwright__*`).
**Evidence**: `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/`

**Scope note** — this is the Round 2 live walk for the Step 2 **P0 bundle only**. The walk is the P0-4 reduced-motion audit that §6.1 of the follow-up plan specifies, with piggyback verification of the P0-5 footer-href fix at the same viewport. Full multi-locale (P1-1) and RTL (P1-2) walks remain scheduled for a subsequent round.

---

## Server

- **URL**: `http://127.0.0.1:8731/`
- **Started at**: 2026-04-24T23:45Z (background task `bsvroh9h4`).
- **Still running**: **yes** — the server remains running; parallel user verification at the same URL is welcome.
- **Restarts during walk**: 0.

## Scope

- **Locale walked**: `it` (primary). This round is scoped to P0-4 reduced-motion JS verification per §6.1; EN / FR / ES / AR live walks are the P1-1 / P1-2 deliverables and are not in Round 2.
- **Pages walked** (12 total):
  - **Pragma**: `home`, `chi-siamo` (about), `competenze` (services), `case-studies` (list), `case-studies/manifatturiero-bresciano-piano-industriale` (detail), `contatti` (contact).
  - **Fiscus**: `home`, `lo-studio` (about), `competenze` (services), `casi-seguiti` (list), `casi-seguiti/pmi-manifattura-bilancio-revisione` (detail), `contatti` (contact).
- **Viewports walked**: 1440 × 900 only. Motion is a JS contract, not a layout one — §6.1 prescribes a single viewport and the rationale holds.
- **Screenshots captured**: 12 full-page PNGs under `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/screenshots/`.

## Reduced-motion emulation

- **Mechanism**: `await page.emulateMedia({ reducedMotion: 'reduce' })` applied via `browser_run_code` to the Playwright context.
- **Live confirmation per page**: `window.matchMedia('(prefers-reduced-motion: reduce)').matches === true` on every `browser_evaluate` sample.
- **Contract under test**: every `[data-lm]` reveal element must render with its final opacity (≥ 0.99) and final transform applied at page-ready under reduced-motion — no stuck opacity-0, no stuck `translateY(24px)`.

## Summary counts

```
[BLOCKING] · P0-4 BRWS-FEEL-08      total:  1   failed: 0
[STRONG]   · P0-4 BRWS-FEEL-07      total:  1   failed: 0
[REQUIRED] · P0-5 CS-CTA-04 footer   total:  1   failed: 0 (side check)
```

## Per-page measurements

| Template | Page | `[data-lm]` total | Stuck opacity-0 | Console errors | Footer legal hrefs real-route | Verdict |
|---|---|---|---|---|---|---|
| Pragma | home                          | 26 | 0 | 0 | 3/3 | PASS |
| Pragma | chi-siamo                     | 24 | 0 | 0 | 3/3 | PASS |
| Pragma | competenze                    | 13 | 0 | 0 | 3/3 | PASS |
| Pragma | case-studies                  |  5 | 0 | 0 | 3/3 | PASS |
| Pragma | case-studies/manifatturiero…  |  7 | 0 | 0 | 3/3 | PASS |
| Pragma | contatti                      |  0 | 0 | 0 | 3/3 | PASS |
| Fiscus | home                          | 26 | 0 | 0 | 3/3 | PASS |
| Fiscus | lo-studio                     | 24 | 0 | 0 | 3/3 | PASS |
| Fiscus | competenze                    | 13 | 0 | 0 | 3/3 | PASS |
| Fiscus | casi-seguiti                  |  5 | 0 | 0 | 3/3 | PASS |
| Fiscus | casi-seguiti/pmi-manifattura… |  7 | 0 | 0 | 3/3 | PASS |
| Fiscus | contatti                      |  0 | 0 | 0 | 3/3 | PASS |
| **Totals** | **12 pages / 2 templates** | **150** | **0** | **0** | **36/36** | **PASS** |

## Rubric checks that ran

### BRWS-FEEL-08 (strong · prefers-reduced-motion respected) — **PASS**

Every `[data-lm]` element on every walked page renders with final opacity ≥ 0.99 under `prefers-reduced-motion: reduce`. Validated with:

```js
Array.from(document.querySelectorAll('[data-lm]'))
  .filter(el => parseFloat(getComputedStyle(el).opacity || '1') < 0.99)
  .length   // 0 on every page
```

The `_base.html:563-565` `@media (prefers-reduced-motion: reduce)` block and `static/js/live-motion.js` `matchMedia` branch jointly close the AP12 precondition. No page required an instant-finalize fallback visually — all elements reach final state immediately.

### BRWS-FEEL-07 (strong · console clean) — **PASS**

0 JS errors across 12 page loads. The dev-only `favicon.ico` 404 is the only artefact (rubric-waived). No uncaught exceptions from `live-motion.js`, `live-media.js`, `live-forms.js`, or the bridge script set under reduced-motion.

### CS-CTA-04 (required · footer legal CTA-adjacent real-route) — **PASS** (side check)

The P0-5 fix is live on the walked tree. Every footer renders with 3 anchors inside `<span class="legal">`, each resolving via `{% url 'catalog:live_template_page' template.category.slug template.slug 'contatti' %}`. Zero `href="#"` placeholders remain. Visible in every screenshot as "PRIVACY · COOKIE · NOTE LEGALI" pointing to the contatti page. This closes the standing CS-CTA-04 defect R4 called out in the Step 2 plan §1.

## Parallel P0 evidence captured during the walk

- `manage.py check catalog -v 2` on the working-tree: silent on palettes (Pragma + Fiscus pass); `corporate_suite.W001` visible for the grandfathered `business-corporate` pool. Transcript at `factory/reports/hardening/step2-ci/check-clean-20260424T2345Z.log`.
- Injected known-bad state: `#F7F3EC` primary on an injected corporate-suite slug → `corporate_suite.E001` error surfaces and `findings` is non-empty. Transcript at `.../step2-ci/check-failing-palette-20260424T2345Z.log`.
- Injected non-Pexels URL into the Solaria-reserved `business-coaching` pool → `corporate_suite.E002` error surfaces. Transcript at `.../step2-ci/check-failing-imagery-20260424T2345Z.log`.
- `python manage.py test apps.catalog -v 2` → 171 tests · OK · 2.213 s. Transcript at `.../step2-ci/test-run-20260424T2346Z.txt`.

## Issues found in Round 2

**Inside Priority 1 scope**: 0 issues. Nothing required a fix + re-walk loop inside P0.

**Side-observation carried into a future round (D12 candidate)**: the Fiscus case-study detail KPI band (bottom of `casi-seguiti/pmi-manifattura-bilancio-revisione`) reads visually low-contrast under reduced-motion. This is not a reduced-motion defect — the same band renders the same way without emulation — but a P1 contrast-accessibility walk should quantify the ratio with DevTools sampling. Tracked in the Round 1 execution report's "Borderline live-walk observation" section.

## Deviations (§ deviation)

1. **Multi-locale live walks (EN · FR · ES) not executed this round.** Scheduled as T-P1-1 per plan §3.P1. Rationale: the P0 gate completes without a multi-locale walk; P1 is a separate gate.
2. **RTL (AR) live walk not executed this round.** Scheduled as T-P1-2 per plan §3.P1. Same rationale.
3. **Viewport sweep limited to 1440 × 900 only.** Per plan §6.1 — the P0-4 walk targets a JS-side contract; the 8-viewport sweep is P1-1 / P1-2 scope.

All three deviations are explicit plan-aligned scoping, not unacknowledged gaps.

## Imagery walk summary

No imagery-walk results new to Round 2. The Step 1C / 1D imagery-pool findings stand unchanged:

| Pool key | Template | URLs 200 / 6 | Host policy | Build-time gate |
|---|---|---|---|---|
| `business-corporate` | Pragma | 6/6 | 6 non-Pexels (LEGACY_EXEMPT) | `corporate_suite.W001` (visible Warning, non-blocking per design) |
| `business-fiscal`    | Fiscus | 6/6 | Pexels-only | silent (no finding) |

## Responsive walk summary

Not re-run in Round 2 — Step 1D Round 1 walked the full 8-viewport matrix (IT LTR) and that evidence stands. Round 2 takes it as given (`phase-x4a-step1d/20260424T2300Z`).

## Console summary

- **JS errors**: **0** across 12 pages (favicon 404 waived).
- **Warnings**: **0**.

## Verdict

**PASS** on Priority 1 (P0) scope. The archetype clears every P0 exit criterion in plan §10.2:

- T-P0-1 through T-P0-6 all green + evidenced.
- Canonical dated test transcript captured (171 · OK).
- Reduced-motion walk V1 passes with BRWS-FEEL-08 green on both templates.
- Gatekeeper CRITICAL list aligned with scorecard authoritative list.

The archetype has moved from **No-Go** (Round 1 tip `0727aad`) to a **Conditional-Go**-eligible state: the P0 bundle that pinned the gate is clear with build-time fail surface now in place. The Round 2 walk validates that promotion from runtime `UserWarning` to build-time `Error` did not introduce new rendering defects.

## Parallel-verification handshake

The dev server remains at **http://127.0.0.1:8731/** and stays running until the user confirms parallel verification or explicitly releases the walk. Recommended parallel checks:

- Load `http://127.0.0.1:8731/templates/business/pragma-corporate-suite/preview/` and `http://127.0.0.1:8731/templates/business/fiscus-commercialista/preview/` in a local browser; enable "Reduce motion" at the OS level (macOS System Preferences → Accessibility → Display → Reduce motion; Windows Settings → Ease of Access → Display → Show animations in Windows). Confirm no stuck invisible panels.
- Click the three footer legal links on both templates; confirm they resolve to the contatti page (not a `#` anchor re-hash).
- Run `python manage.py check catalog -v 2` locally; confirm a `corporate_suite.W001` warning line on the legacy Pragma pool and 0 errors.
- Optional: temporarily edit one of the palettes in `apps/catalog/management/commands/seed_templates.py` to `#F7F3EC` (DO NOT commit), re-run `manage.py check catalog`, confirm non-zero exit with `corporate_suite.E001`, then revert.

— end of Round 2 verdict —
