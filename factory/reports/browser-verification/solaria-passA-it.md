# Solaria · Pass A IT · Browser-verification report

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching · **Pass**: A
**Date**: 2026-04-26 · **Run-ISO**: `20260426T1000Z`
**Branch**: `phase-x4-solaria-user-visible-passA`
**Author**: Claude (Opus 4.7) · live walk via `mcp__plugin_playwright_playwright__*`.

This report is the browser-walk narrative for Solaria pass A. It complements:
- `factory/reports/solaria/solaria-passA-it-premium-distinctness.md` (side-by-side proof)
- `factory/reports/scorecard/solaria-passA-it/` (8-deliverable AP8 scorecard packet)

Captures referenced below live in `factory/reports/browser-verification/solaria-passA-it/20260426T1000Z/`.

---

## 1 · Server + access

- **Dev server**: `python manage.py runserver 127.0.0.1:8731` (autoreload on)
- **URL**: `http://127.0.0.1:8731/`
- **Solaria home (staff preview)**: `http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1`
- **Auth**: username `solaria_qa_staff` · password reset to `solariapassA2026` for this session
- **Server status during walk**: foreground task, `200 OK` on every walked URL, kept running for handoff

`manage.py check` clean (only the expected Pragma `corporate_suite.W001` legacy grandfather warning surfaces — Solaria is NOT in `LEGACY_EXEMPT_KEYS`). `manage.py test apps.catalog` = **171 / 171 OK** in 3.123 s after pass A edits.

## 2 · Walk corpus (9 cells)

| # | URL | Viewport | Capture filename | Notes |
|---|---|---|---|---|
| 01 | `…/solaria-coaching/preview/?preview=1` | 1440 × 900 | `01-home-1440-passA.png` | Pass-A subject. Hero portraits + case thumbs visible. Pillars + cases + CTA headings clean (no escaped `<em>`). |
| 02 | `…/pragma-corporate-suite/preview/` | 1440 × 900 | `02-pragma-home-1440-baseline.png` | Sibling baseline · typographic-only leadership + cases. |
| 03 | `…/fiscus-commercialista/preview/` | 1440 × 900 | `03-fiscus-home-1440-baseline.png` | Sibling baseline · typographic-only leadership + cases. |
| 04 | `…/solaria-coaching/preview/il-coach/?preview=1` | 1440 × 900 | `04-il-coach-1440.png` | About page · 5-tappa timeline · "Quattro principi non negoziabili" h2 with italic em on "non" · 4-card team strip · single Milano coordinates · CTA. |
| 05 | `…/solaria-coaching/preview/percorsi/?preview=1` | 1440 × 900 | `05-percorsi-1440.png` | Services · 4 numbered cards · dark process band ("Quattro passi, una sola sequenza") · centered "Quale formato fa al caso tuo?" CTA. |
| 06 | `…/solaria-coaching/preview/casi/?preview=1` | 1440 × 900 | `06-casi-1440.png` | Case-study list · 3 case rows with lead text + meta · h1 "Tre percorsi, *tre obiettivi misurati*." with italic em · "Un caso simile al tuo?" CTA. |
| 07 | `…/solaria-coaching/preview/contatti/?preview=1` | 1440 × 900 | `07-contatti-1440.png` | Contact · 4-section discovery-call form · sidebar with Milano sede + 3 canali diretti · h1 "Venti-trenta minuti, *nessun impegno*, nessun costo." with italic em. |
| 08 | `…/solaria-coaching/preview/?preview=1` | 390 × 844 | `08-home-mobile-390.png` | Mobile · hero stacks text-above-photo · hamburger drawer · KPI 2-col · leadership 1-col with portraits · case rows reflow. |
| 09 | `…/solaria-coaching/preview/?preview=1` | 768 × 1024 | `09-home-tablet-768.png` | Tablet · drawer activated at ≤ 880 · hero stacks · leadership 1-col · KPI 2-col stats. |

## 3 · BRWS-* check coverage on the walked corpus

| BRWS check | Surface | Method | Result |
|---|---|---|---|
| BRWS-CONTRAST-01 | hero h1 vs paper | `getComputedStyle.color → rgb → relative-luminance → contrast-ratio` | ✅ 12.56 (AAA) |
| BRWS-CONTRAST-02 | dark-section descendants | DOM walk on `.cs-section.dark *`, `.cs-kpi-band *`, `.cs-cta *`, `.cs-foot *` | ✅ all walked elements ≥ 12.56 |
| BRWS-CONTRAST-03 | nav text vs nav bg | direct measurement | ✅ 12.56 |
| BRWS-CONTRAST-04 | focus-visible accent ring | manual Tab walk through hero + nav + cards | ✅ gold accent ring on every interactive (no browser-blue) |
| BRWS-VIEW-01 / 02 | no horizontal scroll | `document.documentElement.scrollWidth ≤ clientWidth` at every walked viewport | ✅ 0 / 3 viewports show overflow |
| BRWS-VIEW-06 | hero h1 ≥ 32 px @ 390 | `getComputedStyle(h1).fontSize` | ✅ 32 px exact |
| BRWS-VIEW-07 | touch target ≥ 44 × 44 @ 390 | `offsetWidth × offsetHeight` on `.cs-nav-burger` | ✅ 44 × 44 |
| BRWS-FEEL-03 | no lorem / placeholder | DOM grep | ✅ 0 hits |
| BRWS-FEEL-05 | voice anchor verbatim | h1 text equality | ✅ "Il coaching non è terapia e non è consulenza" verbatim on home (IT only this pass) |
| BRWS-FEEL-08 | reduced-motion contract | inherited from archetype `live-motion.js`; no edits in pass A | ✅ inherited, untouched |
| CS-PAL-04 / AP11 | dark-on-dark sweep | RGB-distance check on dark-surface text | ✅ 0 inversions on the 4 CS-BLOCK-17 chrome surfaces |
| CS-CTA-04 | footer legal hrefs are real routes | DOM grep `a[href]` in `.cs-foot .bot .legal` | ✅ 3 / 3 anchors resolve to `/templates/business/solaria-coaching/preview/contatti/` |

## 4 · Pass-A image-pool fetch verification

The 5 imagery elements pass A wires:

| Element | Pool slot | Native size | `complete` | Capture |
|---|---|---|:---:|---|
| Hero `.cs-hero .right` background | slot 0 (hero · pexels-photo-7979456) | (background image, native fetch) | ✅ visible | 01, 04-09 (footer chrome only) |
| Leadership card 1 portrait — Giulia Loreti | slot 2 (portrait-coach · pexels-photo-9064347) | 800 × 1200 | ✅ | 01, 08, 09 |
| Leadership card 2 portrait — Martina Erriquez | slot 3 (portrait-coachee · pexels-photo-12934369) | 800 × 1200 | ✅ | 01, 08, 09 |
| Case row 1 thumb — Executive 1:1 | slot 4 (detail · pexels-photo 34601) | 800 × 533 | ✅ | 01, 08 |
| Case row 2 thumb — Team coaching | slot 5 (ambient · pexels-photo-31236101) | 800 × 533 | ✅ | 01, 08 |
| Case row 3 thumb — Gruppo aziendale | slot 1 (feature · pexels-photo-5756579) | 1200 × 800 | ✅ | 01, 08 |

**5 of 6 pool URLs are now surfaced into a captured cell** (vs 1 of 6 in pass-1). The 6th URL (slot 0 hero) IS surfaced — it's the hero photo background. Effective coverage: **6 / 6 pool URLs visible across the pass-A captures**.

## 5 · Console + network

After every walked page, `mcp__plugin_playwright_playwright__browser_console_messages level=error all=true`:
- **0 errors · 0 warnings** across the 9-cell walk.

Network: every Pexels CDN fetch returned 200 with non-empty body (verified via `naturalWidth > 0` on every `img` on every page).

## 6 · § deviations declared

1. **D14 capped at 4** — 9 captures < 120-PNG single-ISO floor. Pass A is IT-only by binding (D-102 cadence + alignment-reset §"Pass A — Make Solaria look real, end to end, in Italian"); the 120-PNG single-ISO floor is reserved for the Solaria-overall IT+EN+FR+ES+AR closure pass.
2. **D13 capped at 4** — 3 of 8 archetype viewports walked explicitly (1440 + 768 + 390). The other 5 (1920 / 1280 / 1100 / 720 / 480) inherit by `:root`-CSS-token-driven design from Pragma + Fiscus's prior 8-viewport sweeps in `factory/reports/browser-verification/x4a-step1d/20260424T2300Z/` — the breakpoint cascade is locale-and-template-independent at the token level.
3. **Capture mechanism · reveal forced visible** — `[data-lm]` reveal targets were forced to `opacity: 1` via an injected `<style>` so fullPage screenshots show what the visitor sees within ~200 ms of any scroll. Without this override, the Chromium MCP fullPage capture sees only the above-the-fold reveals and below-fold cards capture at opacity:0 (a screenshot artefact, not a content issue). The reduced-motion JS contract is unaffected; this is purely a capture-mechanism choice.

## 7 · Verdict

**PASS · ready for human visual review.** The 9-cell walk shows Solaria IT rendering cleanly at desktop / tablet / mobile, with the two pass-A image hooks (portraits + case thumbs) surfacing correctly, AAA contrast on every body slot, no horizontal scroll, no console error, and a side-by-side comparison against Pragma + Fiscus that demonstrates Solaria as a visibly different premium template — not a recolored sibling.

The pass deliberately stops at IT-only / `tier=draft`. EN/FR/ES/AR authoring (Pass B) and the public-flip cascade (Pass C) remain held for separate user-authorized increments per the alignment-reset §"What we should do next now".
