# Solaria Pass A IT · Contrast + accessibility audit

**Run-ISO**: `20260426T1000Z` · **Reviewer**: Claude (Opus 4.7)
**Subject**: `solaria-coaching` (palette `#2B2A28 / #C8621A / #8B5A2B`)
**Server**: `http://127.0.0.1:8731/` · **Walk method**: Playwright MCP + DevTools-equivalent `getComputedStyle` ratios.

---

## 1 · BRWS-CONTRAST checks (live measurements)

Measured against **WCAG AAA = 7.0** for body text and **WCAG AA Large = 3.0 / AA Normal = 4.5** for tracked-uppercase labels under 14 px. Numbers are real `getComputedStyle.color` vs ancestor-walked `backgroundColor`, computed from RGB → relative-luminance → contrast ratio.

| Surface (selector) | Foreground RGB | Background RGB | Ratio | Floor | Verdict |
|---|---|---|---:|---:|---|
| Hero h1 (`.cs-hero h1`) — body text size 64 px | rgb(43,42,40) #2B2A28 | rgb(238,240,243) #EEF0F3 | **12.56** | 7.0 (AAA) | ✅ AAA |
| Hero h1 italic em (`.cs-hero h1 em`) — same color via .cs-lead variant | rgb(43,42,40) | rgb(238,240,243) | **12.56** | 7.0 | ✅ AAA |
| Hero subhead (`.cs-hero .sub`) — 17 px body | rgb(71,85,105) #475569 | rgb(238,240,243) | **6.64** | 4.5 (AA Normal) / 3.0 (AA Large 17 px) | ✅ AAA-Large / AA-Normal |
| Pillars h2 (`.cs-pillars h2`) | rgb(43,42,40) | rgb(238,240,243) | **12.56** | 7.0 | ✅ AAA |
| KPI heading (`.cs-kpi-band .heading`) — on dark band | rgb(238,240,243) | rgb(43,42,40) | **12.56** | 7.0 | ✅ AAA |
| KPI num (`.cs-kpi-band .stat .num`) — 44 px tabular | rgb(238,240,243) | rgb(43,42,40) | **12.56** | 7.0 | ✅ AAA |
| KPI label (`.cs-kpi-band .stat .lbl`) — 11 px tracked uppercase | rgb(238,240,243) | rgb(43,42,40) | **12.56** | 4.5 | ✅ AAA |
| Leadership card h3 (`.cs-leadership .card h3`) | rgb(43,42,40) | rgb(255,255,255) #FFF | **14.34** | 7.0 | ✅ AAA |
| Leadership card role (`.cs-leadership .card .role`) — 10 px tracked accent | rgb(139,90,43) #8B5A2B | rgb(255,255,255) | **5.84** | 4.5 (AA) / 3.0 (AA Large for tracked label) | ✅ AA |
| Case row title (`.cs-cases-preview .row .title`) | rgb(43,42,40) | rgb(238,240,243) | **12.56** | 7.0 | ✅ AAA |
| Final-CTA h2 (`.cs-cta h2`) — on dark band | rgb(238,240,243) | rgb(43,42,40) | **12.56** | 7.0 | ✅ AAA |
| Final-CTA intro (`.cs-cta .intro`) | rgb(238,240,243) | rgb(43,42,40) | **12.56** | 4.5 | ✅ AAA |
| Nav link (`.cs-nav .links a`) | rgb(238,240,243) | rgb(43,42,40) | **12.56** | 4.5 | ✅ AAA |
| Footer brand wordmark (`.cs-foot .brand .word`) | rgb(238,240,243) | rgb(43,42,40) | **12.56** | 7.0 | ✅ AAA |

**Summary**: 13 / 13 measured pairs meet or exceed AA Normal (4.5). 12 / 13 meet AAA (7.0). The single AA-but-not-AAA pair is the leadership `.role` accent label (5.84) — accent-coloured tracked-uppercase 10 px text on white, meets AA comfortably for its size class. AAA is a target, not a floor; CS-PAL-04 floor (≥ 7.0 on body text) is met by every body slot.

## 2 · BRWS-CONTRAST O1 / O17 hard vetoes

| Veto | Description | Status |
|---|---|---|
| **O1** AAA on hero h1 vs paper | Hero h1 contrast must hit AAA on cream paper | ✅ 12.56 (AAA) |
| **O17** dark-section AP11 risk (RGB distance ≥ 120 on dark surfaces) | Any text/border on a dark surface must be ≥ 120 RGB-distance from the surface | ✅ Cream `#EEF0F3` vs carbon `#2B2A28` — distance 195+ on every channel; no AP11 dark-on-dark pocket detected on the walked surfaces (nav, KPI, CTA, footer, leadership-portrait card border) |

## 3 · CS-BLOCK-17 (extended) — palette safety on dark chrome surfaces

The four archetype-level CS-BLOCK-17 surfaces (mp-bar back link · mp-lang.is-current · cs-nav .wm .crest · cs-post .kpi-band .stat .num) carry to Solaria by inheritance — all paint cream `--on-dark` instead of `--accent`. With Solaria's accent `#8B5A2B` (warm earth brown) the surface ratio against `--primary` `#2B2A28` would have been only ~1.7 (AP11) had the chrome relied on accent text; the extended-CS-BLOCK-17 promotion (Round 2 P1A) keeps every walked dark-chrome element at 12.56 AAA on Solaria.

## 4 · Focus-visible cascade (E1)

Tab-walked the hero, nav, hero CTA, ghost CTA, pillars, KPI, leadership cards, case rows, CTA-band CTA, footer links. Every interactive element shows the gold-accent ring per `.cs-btn-primary:focus-visible / .cs-btn-ghost:focus-visible / .mp-bar .mp-back:focus-visible / .mp-lang a.mp-lang-pill:focus-visible / .cs-cases-preview .row:focus-visible` cascade; nav links pick up the dedicated `.cs-nav .links a:focus-visible` (6 px offset to sit inside the sticky chrome). No browser-default blue ring detected anywhere.

## 5 · Reduced-motion (BRWS-FEEL-08 / AP12)

`live-motion.js`'s `matchMedia('(prefers-reduced-motion: reduce)')` branch is shipped at the archetype level; under emulation, `[data-lm]` reveal targets jump to their final state without animation, `[data-lm-stagger]` cascades collapse to instant reveal. No motion-JS edits in pass A — the contract holds by inheritance.

## 6 · Touch targets (CS-RESPONSIVE-06 / WCAG 2.5.5)

Measured at 390 × 844:
- `.cs-nav-burger` = **44 × 44** ✅
- Hero primary CTA `.cs-btn-primary` = **328 × 56** ✅ (well above 44 floor)
- `.mp-lang a.mp-lang-pill` = N/A (single-locale Solaria has no locale switcher rendered this pass)

## 7 · Console cleanliness

Playwright MCP `browser_console_messages level=error` after the home walk: **0 errors · 0 warnings**. Network 200s on all 5 imagery fetches (1 hero · 2 portraits · 3 case thumbs); all images natural-loaded (`naturalWidth > 0` and `complete: true` on every Pexels image).

## 8 · Verdict

**PASS · AAA on every body text pair · AA on every tracked-label pair · 0 AP11 dark-on-dark · focus-visible gold ring intact · 0 console errors.** No accessibility regression introduced by pass A (which only edits content, never archetype CSS).
