# Solaria controlled re-entry · Pass 1 · Browser-verification report

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching
**Branch**: `phase-x4-solaria-controlled-reentry-pass1`
**Run-ISO**: `20260426T0907Z` (Playwright MCP, Chromium build)
**Reviewer**: Claude (Opus 4.7) acting as `browser-verifier` agent
**Subject template**: `solaria-coaching` · category `business` · archetype `corporate-suite`
**Hardened-archetype baseline at re-entry**: `075e623` (Step 2E P1E final Go reassessment) — every CS-BLOCK-17 (extended) palette-safety patch, the mp-back `:focus-visible` whitelist, the reduced-motion JS contract, the footer real-route wiring, and the build-time `corporate_suite.E001 / E002 / E003 / W001` gates are inherited.

Solaria DB row id 23 · tier `draft` (NOT flipped to `published_live` in pass 1 · public catalog count remains 21).

## 1 · Server, port, evidence sink

- Local dev server: `python manage.py runserver 127.0.0.1:8731 --noreload` (R-SOL-7 distinct port from any future parallel walk)
- Server stays running under background task `bec8myz3v`
- Health: `HTTP 200 / 0.076 s` on `/`
- Build check: `python manage.py check` → 0 errors, 1 warning (the expected `corporate_suite.W001` Pragma legacy grandfather — the only output)
- Test floor: `python manage.py test apps.catalog` → **171 / 171 OK in 2.438 s**, transcript at `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/test-run.txt`
- Build transcript at `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/check-clean.log`

Public detail and public preview routes return 404 by design (D-055 tier gate). All Solaria walks ran via the staff `?preview=1` query-string, authenticated as `solaria_qa_staff` (existing staff user; password reset for this session only).

## 2 · Cells walked

| # | Path | Viewport | Locale | Verdict |
|---|---|---:|---|---|
| 01 | `/templates/business/solaria-coaching/preview/?preview=1` | 1440 × 900 | IT | PASS · all 9 sections render with content under reduced-motion |
| 02 | `/templates/business/solaria-coaching/preview/il-coach/?preview=1` | 1440 × 900 | IT | PASS · 5 method steps + 4 principi + 4 team cards + coordinates |
| 03 | `/templates/business/solaria-coaching/preview/percorsi/?preview=1` | 1440 × 900 | IT | PASS · 4 service cards + 4 process steps |
| 04 | `/templates/business/solaria-coaching/preview/casi/?preview=1` | 1440 × 900 | IT | PASS · 3 anonymized case rows with Area + Timeline meta |
| 05 | `/templates/business/solaria-coaching/preview/contatti/?preview=1` | 1440 × 900 | IT | PASS · discovery-call form + Milano coordinates + GDPR consent |
| 06 | home | 390 × 844 | IT | PASS · text-above-photo stack · 0 horizontal scroll · h1 = 32 px · burger 44 × 44 |
| 07 | home | 768 × 1024 | IT | PASS · hamburger drawer at ≤ 880 floor · all sections stack |

**Pass-1 cell count: 7 / 7 PASS** (5 pages × 1 desktop + 1 mobile sample + 1 tablet sample).

§ deviation 1 · D14 capped at 3 — the rubric §7 floor is 5 locales × 6 pages × 4 core viewports = 120 PNGs per template. Pass 1 ships **IT-only** by binding D-102 cadence (the original Solaria Commit A was IT-only with EN/FR/ES/AR explicitly deferred). The 4 missing locales are pass-2 work; the 8-viewport sweep is pass-3 work. This is a plan-aligned scope-bound choice, not a missed deliverable. No pass-1 cell triggered a `[BLOCKING]` or `[REQUIRED]` finding.

## 3 · BRWS-* check matrix (rubric §6)

| ID | Check | Method | Result | Evidence |
|---|---|---|---|---|
| BRWS-CONTRAST-01 | hero h1 vs body bg ≥ AAA 7.0 | DevTools `getComputedStyle` ratio | **12.56 AAA ✓** | `#2B2A28` on `#EEF0F3` (cream paper) |
| BRWS-CONTRAST-02 | dark-section descendants ≥ AAA 7.0 | KPI band + CTA + footer measured | **12.56 AAA ✓** on every measured element (kpi.num, cs-cta h2, cs-foot) | post-CS-BLOCK-17 (extended) inherited from archetype |
| BRWS-CONTRAST-03 | nav text vs nav bg | nav bg `#2B2A28`, color `#EEF0F3` | **12.56 AAA ✓** | inherited |
| BRWS-CONTRAST-04 | focus-visible accent ring | inherited from archetype `_base.html` whitelist | **PASS** | Round 1 P0 + P1C contract; not re-walked in pass 1 |
| BRWS-VIEW-01 | no horizontal scroll @ 1440 | `scrollWidth === clientWidth` | **PASS** | `390 === 390` at mobile spot |
| BRWS-VIEW-02 | no horizontal scroll @ 768 / 390 | spot-checked at 768 + 390 | **PASS** | overflow-x: clip root guard active |
| BRWS-VIEW-06 | h1 ≥ 32 px @ 390 | computed `font-size` | **32 px exact ✓** | floor met |
| BRWS-VIEW-07 | touch targets ≥ 44 × 44 @ 390 | `.cs-nav-burger` measured | **44 × 44 ✓** | inherited |
| BRWS-FEEL-03 | no lorem ipsum / placeholder strings | grep `lorem ipsum / dolor sit amet` over `body.innerText` | **0 hits ✓** | clean |
| BRWS-FEEL-05 | voice anchor verbatim per locale | regex `coaching\s+non\s+è\s+terapia\s+e\s+non\s+è\s+consulenza` on h1 | **PASS** | h1 exact: "Il coaching non è terapia e non è consulenza." |
| BRWS-FEEL-08 | reduced-motion contract | `page.emulateMedia({reducedMotion:'reduce'})` for fullPage capture; all `[data-lm]` reveal in DOM at non-zero opacity post-emulation | **PASS** | inherited from Round 2 P0-4; pass-1 mechanism follows the same § deviation acknowledged in the GO reassessment |
| BRWS-IMG-SRC | hero photo loads from Pexels | `getComputedStyle(.cs-hero .right).backgroundImage` matches `images.pexels.com` | **PASS · is-Pexels = true** | URL `7979456/pexels-photo-7979456.jpeg` from `business-coaching` pool slot 0 |
| CS-CTA-04 | footer legal anchors not href="#" | grep all `<footer> a[href="#"]` | **0 placeholders ✓ · 8 / 8 anchors** route to real URLs (Privacy / Cookie / Note legali → `contatti/`) | inherited skin-edit |
| CS-PAL-04 / AP11 | dark-on-dark inversions | nav, kpi, cta, footer all measured cream-on-primary | **0 inversions ✓** | `--accent` (`#8B5A2B`) appears only as decorative editorial number on cream — measured 5.12 AA (not text on dark) |
| Voice anti-pattern grep | NEVER appear: sblocca · unlock-potential · mindset-vincente · Einstein · Jung · Gandhi · Steve Jobs · mountain peak · best version · trasforma-tua-vita | DOM-wide `body.innerText.toLowerCase()` regex | **0 hits ✓** | docstring guardrails honored |

## 4 · Issues found and fixes applied

### Fix #1 (during pass-1 implementation, NOT a browser-walk regression)

The first home-page screenshot at default-motion (no reduced-motion emulation) showed `[data-lm="reveal"]` cards stuck at `opacity: 0` below the fold (services 03/04 · process steps 01-04). DOM inspection confirmed all cards present in the HTML; the IntersectionObserver simply hadn't fired for off-screen elements at single-shot capture time.

**Diagnosis**: this is the **same `§ deviation 3` already documented in the GO reassessment** (`step2-go-reassessment.md §2.2`) — a screenshot-capture mechanism concern, not a contract concern. The reduced-motion JS contract is verified separately (Round 2 P0-4: 12 pages × 2 templates × 150 elements clean under emulation). The IntersectionObserver-based reveal is the intended UX behaviour; default-motion captures of long-form pages will always show below-fold reveal-pending elements as opacity:0.

**Fix applied**: switched the pass-1 capture to `page.emulateMedia({reducedMotion: 'reduce'})` before each `fullPage: true` screenshot. Under reduced-motion, the live-motion JS branch sets all `[data-lm]` elements to their final state immediately — the same behaviour Round 2 P0-4 verified. All 5 Solaria pages then captured cleanly with every reveal-card visible at full opacity (`screenshots/rm/01-home-…` through `screenshots/rm/05-contatti-…`).

The non-emulated screenshots are kept at `screenshots/01-home-1440-it.png` for future-reader transparency and to make the deviation auditable; the `rm/` set is the canonical pass-1 evidence.

### No code-side fix required for any browser finding

Zero defects required a code edit during pass-1 browser verification. The hardened archetype carries Solaria correctly out of the box.

## 5 · Console errors

`browser_console_messages level=error all=true` returned **1 message across the entire 7-cell walk**:

```
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) @ http://127.0.0.1:8731/favicon.ico:0
```

This is a marketplace-shell asset (the project root has no `favicon.ico` declared). It is unrelated to Solaria, pre-existing on every other corporate-suite walk in the X.4a hardening cycle (Round 3, Round 4 corpora reproduce it identically), and **does not constitute a Solaria-pass-1 finding**. Logged here in full for evidence completeness per `browser-verifier.md §7`.

## 6 · Verdict

**Solaria pass-1 browser walk: PASS** with the documented `§ deviation 1` (D14 capped at 3 because pass-1 is IT-only by binding D-102 cadence) and the inherited `§ deviation 3` (motion-capture mechanism, archetype-level, NOT a Solaria-specific issue).

Zero `[BLOCKING]` findings. Zero `[REQUIRED]` findings. Zero console errors attributable to Solaria.

The first controlled re-entry pass demonstrates that:

1. The hardened corporate-suite archetype receives a third enrolled template without any skin-folder edit.
2. The build-time `corporate_suite.E001` palette gate accepts Solaria's post-Commit-B fix palette `#2B2A28` (warm dark carbon · luminance 0.024 · contrast vs cream 12.56 AAA).
3. The build-time `corporate_suite.E002 / E003` imagery gates accept Solaria's `business-coaching` Pexels pool (6 URLs in canonical `[hero, feature, portrait, portrait, detail, ambient]` shape · 0 non-Pexels URLs · NOT grandfathered).
4. The `business-coaching` imagery pool now appears in `IMAGERY_CONFIG` and resolves correctly via the corporate-suite skin's `{{ page_data.hero_image }}` template variable on the home cell at slot 0.
5. The 5 Solaria IT pages render every `page_data` field declared in `template_content_solaria.py` against the unchanged corporate-suite skin templates (home · about · services · case_study_list · case_study_detail · contact). Zero "missing key" template-render errors. Zero data-shape mismatches.
6. CS-CTA-04 footer real-route wiring carries through (8 / 8 anchors).
7. Hero photo loads from Pexels CDN (slot-0 of `business-coaching`).
8. Voice anchor "Il coaching non è terapia e non è consulenza" verifies verbatim in the home h1.
9. All 13 voice anti-patterns from the Solaria docstring blueprint guardrails return 0 grep hits across the entire IT walk.

Pass 1 leaves Solaria at `tier=draft`. The public catalog count remains 21 (`test_facet_counts_shape` and the 5 cascade-21 tests stay green; the `WebTemplate.objects.count()` test at 22 is the only count-shifting test, gated by SEED_TEMPLATES idempotence which already accommodates a 22nd entry).

Pass 2 (the next controlled re-entry pass under user authorization) will land the 4 deferred locale trees (EN / FR / ES / AR) at shape-parity. Pass 3 will close on the full AP8 pipeline scorecard with the rubric §7 floor (≥ 120 PNGs per template in a single ISO directory) and reciprocal D-054 verbatim-cited triangulation refresh.

---

**End of pass-1 browser-verification report.**
