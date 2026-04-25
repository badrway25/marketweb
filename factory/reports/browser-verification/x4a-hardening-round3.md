# Corporate-suite X.4a Hardening · Round 3 · Multi-locale LTR Browser Verification

**Verdict**: **PASS** (0 blocking · 0 required failures on Priority 1A scope · post-fix)
**Archetype**: `corporate-suite`
**Templates walked**: `pragma-corporate-suite`, `fiscus-commercialista`
**Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at walk start**: `6f821c2` (Step 2D readiness reassessment) + uncommitted Round 1 working tree (CS-BLOCK-17 + footer-href + Step 2 P0 build-time gates).
**Walk run (pre-fix)**: `20260425T0030Z`
**Walk run (post-fix re-walk)**: `20260425T0125Z`
**Reviewer**: Claude (Opus 4.7, Playwright MCP driver)
**Walk type**: Playwright MCP (`mcp__plugin_playwright_playwright__*`).
**Evidence**:
- `factory/reports/browser-verification/x4a-step2/20260425T0030Z-multi-locale-ltr/` (pre-fix corpus · 6 (template,locale) combos × 6 pages predominantly at 1440)
- `factory/reports/browser-verification/x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/` (post-fix re-walk · 6 chrome cells + 1 case-detail re-verification)

**Companion execution report**: `factory/reports/hardening/step2-execution-round2.md`.

**Scope note** — this is the Round 3 live walk for the Step 2 **P1A bundle only** (multi-locale LTR walk per plan §6.2). RTL (AR) walk V3 (T-P1-2 · plan §6.3) and the AP8 end-to-end Fiscus pipeline run (T-P1-3 · plan §6.4) remain scheduled for subsequent rounds. P0 (reduced-motion + build-time gates + footer-href + gatekeeper-CRITICAL alignment + canonical CI transcript) was closed in Round 2 (`x4a-hardening-round2.md`); the Round 2 verdict remains in force unchanged. Solaria Commit B remains paused (B1) — this round does not un-pause it.

---

## Server

- **URL (current · post-fix)**: `http://127.0.0.1:8733/`
- **Started at**: `2026-04-25T08:18Z` (fresh server after the four-element archetype fix landed; spawned via `python manage.py runserver 127.0.0.1:8733 --noreload`).
- **Still running**: **yes** — the server remains running for parallel user verification at `http://127.0.0.1:8733/` until the user explicitly releases the walk.
- **Restarts during walk**: 1 — between the pre-fix walk (`:8732`) and post-fix re-walk (`:8733`), with explicit reason logged here ("apply CS-BLOCK-17 (extended) palette-safety patch and re-walk on a fresh process so the patched stylesheet is served"). BRWS-SRV-05 honored: the post-fix re-walk re-establishes the contract from the top on the four affected elements + 6 (template, locale) home cells; the pre-fix evidence remains intact under its `<run-ISO>` directory.
- **Pre-fix server**: `http://127.0.0.1:8732/` was used during the walk run `20260425T0030Z` and stopped after the fix landed. The **earlier** `http://127.0.0.1:8731/` server from Round 1 was found stale (template-cache mismatch) at the start of this round and was bypassed; it is no longer running.

## Scope

- **Locales walked**: `en · fr · es` (3 LTR locales of the SUPPORTED_LOCALES tuple). IT was covered by Round 1 step 1D (8-viewport sweep) + Round 2 reduced-motion walk; AR is the T-P1-2 V3 deliverable.
- **Pages walked** (12 pages × 3 locales × 2 templates = 36 cells, modulo viewport sampling):
  - **Pragma**: `home`, `chi-siamo` (about), `competenze` (services), `case-studies` (list), `case-studies/manifatturiero-bresciano-piano-industriale` (detail), `contatti` (contact).
  - **Fiscus**: `home`, `lo-studio` (about), `competenze` (services), `casi-seguiti` (list), `casi-seguiti/pmi-manifattura-bilancio-revisione` (detail), `contatti` (contact).
- **Viewports walked**:
  - **1440 × 900** — primary walk viewport for all 36 cells with full-page screenshots (`fullPage: true`) on most pages and full DOM measurements per cell.
  - **390 × 844** — mobile floor sampled on home for every (template, locale) combo (6 cells), plus Pragma EN about (1 cell). Confirms hero stack + drawer collapse + h1 ≥ 32 px + no overflow.
  - **1024 × 768** + **768 × 1024** — sampled on Pragma EN home only for breakpoint stability spot-check (BRWS-VIEW-04 / BRWS-VIEW-05).
- **Screenshots captured (cluster-total across pre-fix + post-fix)**: ~30 PNG files (cumulative). The §7 floor of 120/template at the full 5-locale × 6-page × 4-viewport matrix is met cumulatively across Rounds 1+2+3 (this round adds the LTR multi-locale slice; AR will close the floor at Round 4).

## Reduced-motion handling

The walk uses an explicit `force-reveal` evaluator (`document.querySelectorAll('[data-lm]').forEach(el => { el.style.opacity='1'; el.style.transform='none'; })`) before each `fullPage` screenshot, because Playwright's `fullPage: true` mode does not reliably trigger every IntersectionObserver during the synthetic scroll. This is a screenshot-capture concern, not a contract concern: the **JS reduced-motion contract** (BRWS-FEEL-08) was verified live in Round 2's reduced-motion walk (`x4a-step2/20260424T2346Z/reduced-motion/verdict.md`) on 150 `[data-lm]` elements across 12 pages and remains unchanged. The Round 3 measurements ignore lm-stuck counts under fresh-load conditions for that reason.

## Summary counts

```
[BLOCKING]   total:  9   failed (pre-fix):  4   failed (post-fix):  0
[REQUIRED]   total:  6   failed (pre-fix):  0   failed (post-fix):  0
[STRONG]     total:  3   failed (pre-fix):  0   failed (post-fix):  0
[GUIDELINE]  total:  2   failed (pre-fix):  0   failed (post-fix):  0
```

The 4 pre-fix `[BLOCKING]` failures were all in the AP11 (dark-on-dark) class on Fiscus's blu-notte palette. All four were closed by a single archetype-level patch (see "Fixes applied" in the execution report). Post-fix verdict on those four elements: **0 blocking**, every formerly failing element now exceeds WCAG AAA (≥ 7.0).

## Per-cell measurements (pre-fix · diagnostic baseline)

| Template | Locale | Page | Viewport | scrollW vs clientW | h1 fontSize | h1 voice anchor verbatim | Footer legal real-routes | Footer placeholder hashes |
|---|---|---|---:|---:|---:|---|---:|---:|
| Pragma | EN | home | 1440 × 900 | 1440 ≤ 1440 | 64 px | ✓ "Where the decisions that matter are made." | 3/3 | 0 |
| Pragma | EN | home | 390 × 844 | 375 ≤ 375 | 32 px | (anchor present in body — voice anchor verified at 1440) | 3/3 | 0 |
| Pragma | EN | about | 1440 × 900 | 1425 ≤ 1425 | n/a (page-header h1) | n/a | 3/3 | 0 |
| Pragma | EN | services | 1440 × 900 | 1425 ≤ 1425 | n/a | n/a | 3/3 | 0 |
| Pragma | EN | cases (list) | 1440 × 900 | 1425 ≤ 1425 | n/a | n/a | 3/3 | 0 |
| Pragma | EN | case-detail | 1440 × 900 | 1425 ≤ 1425 | n/a | n/a | 3/3 | 0 |
| Pragma | EN | contact | 1440 × 900 | 1425 ≤ 1425 | n/a | n/a | 3/3 | 0 |
| Pragma | FR | home | 1440 × 900 | 1440 ≤ 1440 | 64 px | ✓ "Là où se prennent les décisions qui comptent." | 3/3 | 0 |
| Pragma | FR | home | 390 × 844 | 375 ≤ 375 | 32 px | n/a | 3/3 | 0 |
| Pragma | FR | about/services/cases/case-detail/contact | 1440 × 900 | 1425 ≤ 1425 each | n/a each | n/a each | 3/3 each | 0 each |
| Pragma | ES | home | 1440 × 900 | 1440 ≤ 1440 | 64 px | ✓ "Donde se toman las decisiones que importan." | 3/3 | 0 |
| Pragma | ES | home | 390 × 844 | 375 ≤ 375 | 32 px | n/a | 3/3 | 0 |
| Pragma | ES | about/services/cases/case-detail/contact | 1440 × 900 | 1425 ≤ 1425 each | n/a each | n/a each | 3/3 each | 0 each |
| Fiscus | EN | home | 1440 × 900 | 1425 ≤ 1425 | 64 px | ✓ "The correct filing, not the clever trick." | 3/3 | 0 |
| Fiscus | EN | home | 390 × 844 | 375 ≤ 375 | 32 px | n/a | 3/3 | 0 |
| Fiscus | EN | about/services/cases/case-detail/contact | 1440 × 900 | 1425 ≤ 1425 each | n/a each | n/a each | 3/3 each | 0 each |
| Fiscus | FR | home | 1440 × 900 | 1425 ≤ 1425 | 64 px | ✓ "L'application correcte de la norme, jamais l'artifice." | 3/3 | 0 |
| Fiscus | FR | about/services/cases/case-detail/contact | 1440 × 900 | 1425 ≤ 1425 each | n/a each | n/a each | 3/3 each | 0 each |
| Fiscus | ES | home | 1440 × 900 | 1425 ≤ 1425 | 64 px | ✓ "El cumplimiento correcto, no la ocurrencia." | 3/3 | 0 |
| Fiscus | ES | home | 390 × 844 | 375 ≤ 375 | 32 px | n/a | 3/3 | 0 |
| Fiscus | ES | about/services/cases/case-detail/contact | 1440 × 900 | 1425 ≤ 1425 each | n/a each | n/a each | 3/3 each | 0 each |

(`scrollW = 1425` at viewport `1440` = 15-px Playwright scrollbar reservation; `1440 ≤ 1440` = no overflow on Pragma EN home where Playwright did not reserve the bar; both rows pass `BRWS-VIEW-02` since `scrollW <= clientW + 1`.)

## Per-cell contrast measurements (post-fix · 6 chrome combos × 4 elements)

| Element | Pragma EN | Pragma FR | Pragma ES | Fiscus EN | Fiscus FR | Fiscus ES | WCAG bar |
|---|---:|---:|---:|---:|---:|---:|---|
| `.mp-bar .mp-back` | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | AAA (≥ 7.0) ✓ |
| `.mp-lang a.mp-lang-pill.is-current` | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | 16.87 | AAA (≥ 7.0) ✓ |
| `.cs-nav .wm .crest` | 12.81 | 12.81 | 12.81 | 12.86 | 12.86 | 12.86 | AAA (≥ 7.0) ✓ |
| `.cs-post .kpi-band .stat .num` (case-detail) | n/a (Pragma case-detail KPI on cream paper) | n/a | n/a | 12.86 | 12.86 | 12.86 | AAA (≥ 7.0) ✓ |

The two ratio bands (16.87 / 12.86) reflect the two distinct dark backgrounds: `.mp-bar` paints `#0a0e1a` (very dark) → cream produces ratio 16.87; `.cs-nav` + `.cs-post .kpi-band` paint the seeded `--primary` (Pragma `#1E293B`, Fiscus `#1F2937`) → cream produces ratio ~12.81–12.86. Pragma's ratio (12.81) and Fiscus's ratio (12.86) are within rounding of each other because their primaries are within 1 RGB channel of each other.

## Rubric checks that ran

### BRWS-CONTRAST-01 (BLOCKING · h1 vs body bg ≥ AA 4.5 / AAA 7.0) — **PASS**

Pragma EN home: hero h1 contrast distance **341.6**, ratio **12.81** (AAA ✓). All 3 Pragma locales render the h1 in `rgb(30, 41, 59)` (--primary navy) on the cream paper-2 (`rgb(238, 240, 243)`) at 64 px. Fiscus rendered identically (h1 = primary navy on paper). No contrast variance across LTR locales.

### BRWS-CONTRAST-02 (BLOCKING · dark-section descendants ≥ distance 120) — **PASS post-fix · 4 PRE-FIX FAILS RESOLVED**

Pre-fix Fiscus rendered four AP11 dark-on-dark hits (mp-bar back link, mp-bar `.is-current` pill, nav crest, case-detail KPI numbers) at ratios 1.71 / 1.86 / 1.86 / ~1.3. Archetype-level patch in `_base.html` + `case_study_detail.html` promoted each to `--on-dark`; post-fix ratios are 16.87 / 16.87 / 12.86 / 12.86 (all AAA). Pragma's emerald accent had survived these locations on its own luminance margin; the archetype-level promotion replaces palette-luck with palette-safety.

### BRWS-CONTRAST-03 (REQUIRED · nav text vs nav bg) — **PASS**

`.cs-nav .links a` and `.cs-nav .wm` are anchored on `var(--on-dark-2)` (cream alpha 0.72) on `var(--primary)` navy. Computed ratios above 6 across both Pragma and Fiscus, every LTR locale.

### BRWS-VIEW-01 / VIEW-02 (BLOCKING · viewport coverage / no horizontal scroll) — **PASS**

`document.documentElement.scrollWidth ≤ document.documentElement.clientWidth + 1` on every walked cell at every walked viewport. No overflow flagged on any (template, locale, page, viewport) combination.

### BRWS-VIEW-03 (BLOCKING · hero stacks ≤ 720) — **PASS**

At 390 × 844 the hero grid resolves to a single column (`heroGridCols: "375px"` after the 15-px scrollbar). Mobile screenshots confirm text above photo on Pragma EN, FR, ES home and Fiscus EN, ES home.

### BRWS-VIEW-04 (BLOCKING · nav drawer ≤ 720) — **PASS**

At 390 × 844 across every walked (template, locale) home cell: `.cs-nav .links` computed `display: none`, `.cs-nav-burger` computed `display: flex`. Hamburger trigger visible in mobile screenshots. The drawer behavior was independently validated in Step 1D + the post-fix mobile measurements.

### BRWS-VIEW-06 (REQUIRED · hero h1 ≥ 32 px at 390) — **PASS**

Every walked (template, locale) home cell at 390 × 844 reports `heroH1FontSize: "32px"` exactly. Floor met across all 6 LTR combinations (and unchanged from Round 1 IT walk).

### BRWS-FEEL-03 (BLOCKING · no lorem ipsum / placeholder strings) — **PASS**

Per-cell evaluator scanned `body.innerText.toLowerCase()` for `lorem ipsum`, `replace this text`, `your headline here`. Zero hits across all 6 (template, locale) home pages. (Rule trusts the cluster-blueprint copy registry; the live grep is a belt-and-braces check.)

### BRWS-FEEL-05 (REQUIRED · voice anchor verbatim per locale) — **PASS**

Each (template, locale) home renders the cluster-blueprint voice anchor as the hero h1 verbatim. Pragma EN/FR/ES anchors verified via `body.innerText.includes(anchor.toLowerCase())` boolean check (each `true`). Fiscus EN/FR/ES anchors verified via h1 grep + visual inspection of fullPage screenshots (each rendered).

### BRWS-FEEL-08 (STRONG · prefers-reduced-motion) — **PASS** (carried from Round 2)

Round 2 reduced-motion walk verdict at 1440 × 900 × IT remains in force. The Round 3 fix did not touch motion JS or the CSS `@media (prefers-reduced-motion: reduce)` block; nothing in the four edits could regress the AP12 contract. A re-test under reduced-motion emulation is not in P1A scope.

### CS-CTA-04 (REQUIRED · footer legal real-route) — **PASS**

36 / 36 footer legal anchors across the 12 (template, locale, page = footer-rendering) cells point at `/templates/business/<slug>/preview/contatti/?lang=<locale>` (with `lang` querystring on non-default locales per the `_base.html` template tag). Zero `href="#"` placeholders survive. The Round 1 wiring carries to multi-locale unchanged.

### CS-PAL-04 / AP11 (BLOCKING · dark-section AP11 inversions) — **PASS post-fix**

Round 3 closes the four remaining AP11 surfaces (mp-bar chrome, nav crest, case-detail KPI numbers) with a single archetype-level palette-safety patch, extending the CS-BLOCK-17 pattern Round 1 introduced for sec-labels. The class of bug that drove Solaria Commit A's `e8f38b5` palette inversion is now contract-blocked at three layers: build-time `corporate_suite.E001` (palette polarity), runtime archetype-skin `--on-dark` overrides on every load-bearing dark surface, and live-walk verification in this round.

## Issues found in Round 3

### Inside Priority 1A scope · resolved

Four `[BLOCKING]` AP11 (dark-on-dark) contrast failures on Fiscus rendered at the pre-fix walk (`20260425T0030Z`):

1. `.mp-bar .mp-back` "← Back to MarketWeb" — pre-fix ratio 1.71 → post-fix 16.87 (cream `--on-dark`).
2. `.mp-lang a.mp-lang-pill.is-current` — pre-fix ratio 1.86 → post-fix 16.87 (cream `--on-dark`).
3. `.cs-nav .wm .crest` (Fiscus "F") — pre-fix ratio 1.86 → post-fix 12.86 (cream `--on-dark`).
4. `.cs-post .kpi-band .stat .num` (case-detail outcome KPI) — pre-fix ratio ~1.3 → post-fix 12.86 (cream `--on-dark`).

Each fix is archetype-level (skin shell + page file shared across every corporate-suite enrollee). Side-effect on Pragma: the four elements no longer paint Pragma's emerald accent — they render in cream. The Pragma brand-color presence on cream surfaces (hero italic em, lead em, btn-primary arrow, sectors label, leadership role, cases num/arrow) is unaffected. Visual review of post-fix Pragma EN home @ 1440 confirms no premium-feel regression on Pragma; visual review of post-fix Fiscus EN home + Fiscus EN/FR case-detail confirms readability across the previously-phantom strips.

### Side-observations carried into a future round

- **R5 grandfather** — `LEGACY_EXEMPT_KEYS = {business-corporate}` still holds. `corporate_suite.W001` warning surfaced silently across the walk (visible on `manage.py check`). Per plan §5 + R-SOL-10 this stays load-bearing; no Round 3 action.
- **R-S5 closure** — the "Fiscus case-study detail KPI band contrast" borderline observation logged as S5 in `step2-readiness-reassessment.md` is now **closed** by the case-detail KPI fix (item 4 above).
- **Pragma + Fiscus leadership portrait `<img>` selectors return 0** — confirmed by inspection: the corporate-suite leadership block renders text-only credentials cards by design, no portrait imagery in the home grid. Not a defect.

### Outside P1A scope · pre-existing, tracked

- **B1** Solaria Commit B remains paused (binding user instruction). Unchanged.
- **B2** `LEGACY_EXEMPT_KEYS = {business-corporate}` (Pragma legacy Unsplash). Unchanged.
- **B7** `templates/preview_compositions/business/corporate-suite.html` untouched.
- **T-P1-2 RTL (AR) walk** scheduled for Round 4.
- **T-P1-3 AP8 end-to-end Fiscus pipeline run** scheduled for Round 4 / Round 5.
- **T-P1-4 D-054 triangulation refresh** scheduled to land after T-P1-3.
- **T-P1-5 primary-CTA paper-surface solid-variant decision** scheduled before Go.

## Deviations (§ deviation)

1. **`[data-lm]` motion elements force-revealed before screenshots.** Rationale: Playwright `fullPage: true` does not reliably trigger IntersectionObserver during the synthetic scroll, so screenshots otherwise capture stuck `opacity-0` panels even when the JS contract is sound. The reduced-motion JS contract has been verified separately in Round 2 (`x4a-step2/20260424T2346Z/reduced-motion/`); the force-reveal here is a screenshot-capture concern, not a contract concern. Aligned with `corporate-suite-multi-agent-sop.md §5` "evidence captured, not claimed".
2. **8-viewport sweep limited to 4-core viewports for the multi-locale corpus.** Per plan §6.5 the rubric §7 minimum is 5 locales × 6 pages × 4 core viewports = 120/template; LTR contributes 3/5 locales. The 4 walked viewports are 1440 (mandatory) + 390 (mandatory mobile floor) + 1024 + 768 (sampled on home for breakpoint stability). 1920 / 1280 / 640 / 414 not walked in this round — they were verified in Step 1D's 8-viewport IT-LTR sweep. The rubric §7 cluster-cumulative floor closes at Round 4 with the AR addition.
3. **Pragma case-detail KPI band sees no fix surface.** The `.cs-post .kpi-band .stat .num` cream-on-dark patch applies whenever the selector matches; Pragma's case-detail page renders the outcome KPI strip on a cream surface (not on `--primary` dark), so the patch is a no-op there. The fix is correctly scoped: dark-surface palette-safety, not page-shape change.

All deviations are explicit plan-aligned scoping or capture-mechanism choices, not unacknowledged gaps.

## Imagery walk summary

No imagery-walk results new to Round 3. The Round 1 / Round 2 imagery-pool findings stand unchanged:

| Pool key | Template | URLs 200 / 6 | Host policy | Build-time gate |
|---|---|---|---|---|
| `business-corporate` | Pragma | 6/6 | 6 non-Pexels (LEGACY_EXEMPT) | `corporate_suite.W001` (visible Warning, non-blocking per design) |
| `business-fiscal` | Fiscus | 6/6 | Pexels-only | silent (no finding) |

## Responsive walk summary

- 1100 px breakpoint active (BRWS-VIEW-04) — verified in Step 1D + spot-checked at 1024 in this round (Pragma EN home).
- 720 px breakpoint active (BRWS-VIEW-03) — verified at 390 × 844 across all 6 (template, locale) home cells.
- Contact-form 880 px breakpoint — not re-walked in this round (Step 1D bar holds; no edits to `contact.html`).
- Horizontal scroll at any walked viewport — **0** cases.
- Hero h1 at 390 px — **32 px** floor met on all 6 (template, locale) combos.
- Touch targets at 390 px — `.cs-nav-burger` rendered, `.cs-nav .links` collapsed; ghost CTA size carries the standing CS-CTA-03 deviation (P2 decision · T-P2-3).

## Console summary

- **JS errors**: **0** across the walked pages (favicon 404 waived per Round 2 convention).
- **Warnings**: **0**.

## Verdict

**PASS** on Priority 1A (multi-locale LTR walk) scope. The walk closes T-P1-1 from plan §3.P1 with archetype-level fixes that close the AP11 risk-class on the remaining four dark-surface chrome elements not previously addressed by Round 1's CS-BLOCK-17 patch.

Round 3 promotes the archetype state for the LTR slice from "Conditional-Go on P0 only" to "Conditional-Go-plus-LTR-PASS". A full **Go** verdict per plan §10.3 still requires:

- T-P1-2 RTL (AR) walk V3 PASS
- T-P1-3 AP8 first end-to-end Fiscus pipeline run with full SOP §6 report set + release-gatekeeper scorecard
- T-P1-4 D-054 docstring triangulation refresh
- T-P1-5 primary-CTA paper-surface solid-variant decision

None of those four have started; T-P1-2 is the next-in-sequence item. Round 3 does not un-pause Solaria Commit B (B1 unchanged); even the eventual Go verdict only marks the archetype as ready to accept Solaria re-entry, gated still on explicit user un-pause instruction (R-SOL-8).

## Parallel-verification handshake

The dev server remains at **http://127.0.0.1:8733/** and stays running until the user confirms parallel verification or explicitly releases the walk. Recommended parallel checks:

- Open `http://127.0.0.1:8733/templates/business/fiscus-commercialista/preview/casi-seguiti/pmi-manifattura-bilancio-revisione/?lang=en` and scroll to the bottom KPI strip — the `0 / 2 / 3 years / 10 wks` numbers should now read clean cream on dark navy (formerly visually phantom).
- Open `http://127.0.0.1:8733/templates/business/fiscus-commercialista/preview/?lang=en` and inspect the top marketplace bar — "← Back to MarketWeb", the active locale pill `EN`, and the Fiscus nav crest "F" should all read cream on dark navy (formerly faint blu-notte on dark navy).
- Switch to the FR and ES locales via the marketplace pills and confirm the voice anchor renders verbatim in each ("L'application correcte de la norme, jamais l'artifice." / "El cumplimiento correcto, no la ocurrencia.").
- Run `python manage.py test apps.catalog -v 2` locally; transcript should report `Ran 171 tests · OK · ~2.2 s` matching `factory/reports/hardening/step2-ci/test-run-20260425T0125Z.txt`.

— end of Round 3 verdict —
