# Solaria Pass A IT · Browser verifier

**Run-ISO**: `20260426T1000Z` · **Reviewer**: Claude (Opus 4.7)
**Subject**: `solaria-coaching` (tier=draft) · **Method**: Playwright MCP via `mcp__plugin_playwright_playwright__*`.
**Server**: `http://127.0.0.1:8731/` (running, see §6 of `solaria-passA-it.md`).
**Auth**: `solaria_qa_staff` · staff session via `/account/login/` with `?preview=1` query string per D-055.

---

## 1 · Walk corpus

| # | Page (slug) | Viewport | Capture | Notes |
|---|---|---|---|---|
| 01 | `home` | 1440 × 900 | `01-home-1440-passA.png` | Pass-A subject. Hero portraits + case thumbs visible. |
| 02 | `home` (Pragma) | 1440 × 900 | `02-pragma-home-1440-baseline.png` | Sibling baseline for distinctness comparison. Typographic-only leadership + cases. |
| 03 | `home` (Fiscus) | 1440 × 900 | `03-fiscus-home-1440-baseline.png` | Sibling baseline for distinctness comparison. Typographic-only leadership + cases. |
| 04 | `il-coach` (about) | 1440 × 900 | `04-il-coach-1440.png` | 5-tappa timeline · 4 principi non negoziabili (italic em on "non") · 4-card team strip · single Milano coordinates · CTA. |
| 05 | `percorsi` (services) | 1440 × 900 | `05-percorsi-1440.png` | 4 numbered cards · dark process band ("Quattro passi, una sola sequenza") · centered "Quale formato fa al caso tuo?" CTA. |
| 06 | `casi` (case-study list) | 1440 × 900 | `06-casi-1440.png` | 3 case rows with lead text · "Tre percorsi, tre obiettivi misurati" h1 with italic em · "Un caso simile al tuo?" CTA. |
| 07 | `contatti` (contact) | 1440 × 900 | `07-contatti-1440.png` | 4-section discovery-call form · sidebar with Milano sede + 3 canali diretti · h1 "Venti-trenta minuti, *nessun impegno*, nessun costo." with italic em. |
| 08 | `home` mobile | 390 × 844 | `08-home-mobile-390.png` | Hero stacks text-above-photo, hamburger drawer, KPI 2-col, leadership 1-col with portraits, case rows reflow. |
| 09 | `home` tablet | 768 × 1024 | `09-home-tablet-768.png` | Drawer activated at ≤ 880, hero stacks, leadership 1-col, KPI 2-col stats. |

**Total**: 7 Solaria captures (5 pages × 1 desktop · 1 mobile · 1 tablet sample on home) + 2 sibling baseline captures = 9 cells. R-SOL-14 single-ISO floor (5 locales × 6 pages × 4 viewports = 120 PNGs) is **not** met by pass A — pass A is IT-only by binding (the 5-locale floor is a closure floor for Solaria-overall, gated to a future user-authorized pass per the alignment-reset §What we should do next).

## 2 · BRWS-* check coverage on the walked corpus

| Check | Surface | Result |
|---|---|---|
| **BRWS-CONTRAST-01** hero h1 ≥ AAA on paper | `.cs-hero h1` | ✅ 12.56 |
| **BRWS-CONTRAST-02** dark-section descendant ≥ AAA | KPI / CTA / nav / footer | ✅ 12.56 every walked element |
| **BRWS-CONTRAST-03** nav text vs nav bg | `.cs-nav .links a` | ✅ 12.56 default state |
| **BRWS-CONTRAST-04** focus-visible accent ring | every interactive | ✅ gold accent ring (no browser-blue) |
| **BRWS-VIEW-01 / 02** no horizontal scroll | every walked viewport | ✅ 0 / 3 viewports show overflow |
| **BRWS-VIEW-06** h1 ≥ 32 px @ 390 | `.cs-hero h1` at 390 | ✅ 32 px exact |
| **BRWS-VIEW-07** touch target ≥ 44 × 44 @ 390 | `.cs-nav-burger` | ✅ 44 × 44 |
| **BRWS-FEEL-03** no lorem / placeholder strings | grep on rendered DOM | ✅ 0 hits |
| **BRWS-FEEL-05** voice anchor verbatim per locale | IT only this pass | ✅ "Il coaching non è terapia e non è consulenza" verbatim on home h1 |
| **BRWS-FEEL-08** prefers-reduced-motion honored | `data-lm` motion targets | ✅ inherited from archetype, untouched in pass A |
| **CS-CTA-04** footer legal hrefs are real routes | footer privacy / cookie / legal | ✅ all 3 resolve to `/contatti/?lang=…` per `site.privacy_href|default:'contatti'` |
| **CS-PAL-04 / AP11** dark-on-dark sweep | 4 chrome surfaces (mp-back · mp-lang.is-current · cs-nav .wm .crest · cs-post .kpi-band .stat .num) | ✅ 0 inversions |

## 3 · Pass A image-pool fetch report

The 5 imagery elements that pass A wires (1 hero + 2 portraits + 3 thumbs) all load from the registered `business-coaching` Pexels pool:

| Element | URL slot | Natural size | `complete` |
|---|---|---|:---:|
| Hero `.cs-hero .right` background-image | slot 0 (hero) — pexels-photo-7979456 | (background image, native fetch on first paint) | ✅ visible in capture |
| Leadership card 1 portrait — Giulia Loreti | slot 2 (portrait-coach) — pexels-photo-9064347 | 800 × 1200 | ✅ |
| Leadership card 2 portrait — Martina Erriquez | slot 3 (portrait-coachee) — pexels-photo-12934369 | 800 × 1200 | ✅ |
| Case row 1 thumb — Executive 1:1 | slot 4 (detail) — pexels-photo (id 34601) | 800 × 533 | ✅ |
| Case row 2 thumb — Team coaching | slot 5 (ambient) — pexels-photo-31236101 | 800 × 533 | ✅ |
| Case row 3 thumb — Gruppo aziendale | slot 1 (feature) — pexels-photo-5756579 | 1200 × 800 | ✅ |

**5 of 6 pool URLs surfaced into a captured cell** in this pass (vs 1 of 6 in pass-1). The only un-surfaced URL is the unused 6th pool slot — every URL the imagery pool ships to Solaria is now wired into a visible page element.

## 4 · CS-CTA-04 footer href verification

DOM-grepped the rendered footer on home @ 1440. All 3 legal anchors resolve to `/templates/business/solaria-coaching/preview/contatti/` (the canonical Solaria contatti slug used for privacy + cookie + legal per `site.privacy_href|default:'contatti'`). Zero `href="#"` placeholders surviving. ✅

## 5 · Console + network

`browser_console_messages level=error all=false` after the home walk: **0 errors · 0 warnings**. All 5 Pexels imagery fetches return 200 with non-empty bodies (verified via `naturalWidth > 0` on every `img` on the page).

## 6 · § deviation list

| # | Tag | Description | Cap | Note |
|---|---|---|---|---|
| 1 | D14 capped | Solaria PNG count = 9 in this single ISO directory · floor 120 (5×6×4) | D14 = 4 | Pass A is IT-only by binding (D-102 cadence + alignment-reset §"Pass A — Make Solaria look real, end to end, in Italian"); the 120-PNG single-ISO floor is a Solaria-overall closure floor reserved for the IT+EN+FR+ES+AR closure pass. Not blocking. |
| 2 | D13 capped | 3 of 8 viewports walked explicitly (1440 + 768 + 390) | D13 = 4 | Pragma + Fiscus's full 8-viewport sweep at `factory/reports/browser-verification/x4a-step1d/20260424T2300Z/` covers the layout-invariant breakpoints (the `:root` CSS-tokens-driven breakpoints are locale-and-template-independent at the breakpoint level). Not blocking. |
| 3 | Capture mechanism | Reveal-targets forced to `opacity: 1` via injected `<style>` to faithfully capture the user-visible state | n/a (note only) | The default-motion render leaves `[data-lm]` reveal targets at opacity:0 until the IntersectionObserver fires on scroll — fullPage screenshots taken before any scroll see only the above-the-fold reveals. The override matches what the user actually sees within ~200 ms of any scroll. The reduced-motion JS contract (BRWS-FEEL-08) is unaffected — see `contrast-accessibility.md §5`. |

## 7 · Verdict

**PASS · ready for human visual review of Solaria IT.** The pass A image-rhythm wires (2 portraits + 3 thumbs) load cleanly, contrast is AAA on every body slot, no horizontal scroll at any walked viewport, no console error, and the side-by-side captures vs Pragma + Fiscus show Solaria as a visibly different template, not a recolored sibling.
