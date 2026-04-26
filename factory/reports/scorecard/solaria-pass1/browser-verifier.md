# browser-verifier · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` · IT-only at pass 1
**Run-ISO**: `20260426T0907Z`
**Reporter**: Claude (Opus 4.7) acting as `browser-verifier` with hard-veto authority on O13 / O14 / O15 / O18.
**Server**: `python manage.py runserver 127.0.0.1:8731 --noreload` (R-SOL-7 distinct port)
**Auth**: staff `solaria_qa_staff` + `?preview=1` query-string (D-055 staff-preview pattern).

This file is the agent-leg companion to `factory/reports/browser-verification/solaria-pass1.md` (the canonical browser-walk narrative). Both reference the same evidence sink at `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/`.

---

## §1 · Cells walked (pass-1 corpus)

| # | Path (preview · ?preview=1) | Viewport | Locale | Verdict |
|---|---|---:|---|---|
| 01 | `…/preview/` (home) | 1440 × 900 | IT | **PASS** |
| 02 | `…/preview/il-coach/` | 1440 × 900 | IT | **PASS** |
| 03 | `…/preview/percorsi/` | 1440 × 900 | IT | **PASS** |
| 04 | `…/preview/casi/` | 1440 × 900 | IT | **PASS** |
| 05 | `…/preview/contatti/` | 1440 × 900 | IT | **PASS** |
| 06 | `…/preview/` (home) | 390 × 844 | IT | **PASS** |
| 07 | `…/preview/` (home) | 768 × 1024 | IT | **PASS** |

**7 / 7 PASS · 0 BLOCKING · 0 REQUIRED.**

## §2 · BRWS-* check matrix (full table also in `browser-verification/solaria-pass1.md §3`)

| ID | Result | Source |
|---|---|---|
| BRWS-CONTRAST-01 hero h1 vs body | **AAA 12.56 ✓** | `contrast-accessibility.md §1` |
| BRWS-CONTRAST-02 dark-section descendants | **AAA 12.56 ✓** | `contrast-accessibility.md §2` |
| BRWS-CONTRAST-03 nav text vs nav bg | **AAA 12.56 ✓** | `contrast-accessibility.md §7` |
| BRWS-CONTRAST-04 focus-visible accent ring | **PASS** (inherited) | `contrast-accessibility.md §5` |
| BRWS-VIEW-01 / 02 no horizontal scroll | **PASS** (0 / 7 cells) | `responsive-auditor.md §2` |
| BRWS-VIEW-06 h1 ≥ 32 px @ 390 | **PASS** (32 px exact) | `responsive-auditor.md §3` |
| BRWS-VIEW-07 touch targets ≥ 44 × 44 @ 390 | **PASS** (`cs-nav-burger` 44 × 44) | `responsive-auditor.md §4` |
| BRWS-FEEL-03 no lorem ipsum / placeholder | **0 hits ✓** | `build-report.md §5` |
| BRWS-FEEL-05 voice anchor verbatim | **PASS · IT** | `build-report.md §4.3` |
| BRWS-FEEL-08 reduced-motion contract | **PASS** under emulation | `contrast-accessibility.md §6` |
| BRWS-IMG-SRC hero photo from Pexels | **is-Pexels = true ✓** | `browser-verification/solaria-pass1.md §3` |
| CS-CTA-04 footer real-route wiring | **8 / 8 anchors non-`#` ✓** | `browser-verification/solaria-pass1.md §3` |
| CS-PAL-04 / AP11 dark-on-dark inversion | **0 inversions ✓** | inherited |
| Voice anti-pattern grep | **0 hits ✓** (13 patterns) | `build-report.md §5` |

## §3 · O13 / O14 / O15 / O18 hard-veto authority

- **O13** (any console error introduced by the subject template): **CLEAR.** The 1 console error logged across the entire walk is `favicon.ico 404`, a marketplace-shell artefact pre-existing on every X.4a hardening corpus (Round 3, Round 4, P1C). Not Solaria-specific.
- **O14** (any failed network request for an in-pool imagery URL): **CLEAR.** Hero photo from `business-coaching` slot 0 (`pexels.com/photos/7979456`) loads successfully (verified via `getComputedStyle(.cs-hero .right).backgroundImage`).
- **O15** (any `[data-lm]` element stuck at opacity 0 under reduced-motion emulation): **CLEAR.** All 5 IT pages render every reveal card visible under emulation.
- **O18** (any rendered page-data placeholder leaking — `{{ page_data.foo }}` literal in DOM): **CLEAR.** Zero unrendered template tokens detected.

## §4 · Server preservation

The dev server stays running under background task `bec8myz3v` for the duration of pass 1 and beyond. R-SOL-7 distinct-port hygiene is honored (port 8731 reserved for the Solaria controlled-reentry walk; no parallel walks contended).

## §5 · Console + network summary

```
$ browser_console_messages level=error all=true
Total messages: 0 (Errors: 0, Warnings: 0)
Returning 1 message for level "error"
[ERROR] Failed to load resource: 404 @ http://127.0.0.1:8731/favicon.ico:0
```

The single error is the marketplace-shell `favicon.ico` 404, NOT Solaria-introduced. Network requests for the hero Pexels photo are 200 OK (verified by visual paint and the Pexels URL appearing in computed `background-image`).

## §6 · Reduced-motion capture mechanism (§ deviation acknowledged)

Initial home capture at default-motion showed services 03 / 04 + all 4 process steps stuck at opacity 0 (off-screen at single-shot capture; IntersectionObserver hadn't fired). DOM inspection confirmed every card present in the HTML; the issue is screenshot-capture mechanism, NOT a contract regression.

**Mechanism switch**: `page.emulateMedia({reducedMotion: 'reduce'})` set before each `fullPage: true` capture. Under emulation the `live-motion.js matchMedia` branch sets every `[data-lm]` element to its final state immediately — same behaviour Round 2 P0-4 verified clean on Pragma + Fiscus.

This is the **same `§ deviation 3` already documented in `step2-go-reassessment.md §2.2`** ("Reduced-motion `force-reveal` capture-mechanism for `fullPage: true` screenshots") — archetype-level, not Solaria-specific.

The `screenshots/01-home-1440-it.png` (default-motion, opacity-0 cards visible below fold) is kept for transparency; the canonical `screenshots/rm/01-…` … `05-…` set is the pass-1 evidence.

## §7 · § deviation summary (for gatekeeper aggregation)

1. **D14 capped at 3** — pass-1 ships 7 PNGs (5 IT pages × 1 desktop + 2 mobile/tablet samples). The rubric §7 floor is 120+ PNGs per template in a single ISO directory across 5 locales × 6 pages × 4 core viewports. Pass 1 is IT-only by binding D-102 cadence; pass 2 lands EN/FR/ES/AR; pass 3 closes the matrix. Plan-aligned.
2. **D13 capped at 4** — 3-viewport sample (1440 + 768 + 390) vs the 8-viewport sweep. Layout invariant is locale-independent at the breakpoint level (verified at IT in the archetype's Step 1D 8-viewport sweep on Pragma + Fiscus). Pass 3 will add the full sweep on Solaria.
3. **Reduced-motion `force-reveal` capture-mechanism** — same as archetype-level § deviation 3 from the GO reassessment. NOT a Solaria-introduced concern.

## §8 · Browser-verifier verdict

**PASS** at 7 / 7 walked cells with 3 documented deviations, all plan-aligned, NONE pushing any rubric dimension below the critical floor of 4.
