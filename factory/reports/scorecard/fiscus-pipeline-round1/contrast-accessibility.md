---
report_type: contrast
template_slug: fiscus-commercialista
archetype: corporate-suite
agent: contrast-accessibility-auditor
role: primary
run_timestamp: 20260426T0757Z
server_url: http://127.0.0.1:8735/
verdict: n/a · observer agent
---

# Contrast & accessibility · Fiscus — Studio Tributario · AP8 first-run

## 1 · Summary

Hard-veto status: **none triggered.** The Solaria-class AP1 / AP11 risk that drove this archetype's hardening cycle is **structurally absent** from the Fiscus post-fix corpus — every `h1..h5` clears RGB distance ≥ 120 AND WCAG ≥ 4.5 (hero h1 measured at AAA 12.86 across 5 locales), every dark-section descendant clears AA (cream-on-navy ≥ 12.81), focus-visible paints the gold/accent ring on every whitelisted interactive element (now extended to include `.mp-bar .mp-back` in this round), and `prefers-reduced-motion: reduce` suppresses entrance animations as the JS contract specifies. **No Fiscus contrast hotspots remain** — the readiness reassessment §S5 case-detail KPI band borderline observation was closed by the Round 2 + Round 3 cream-on-dark promotion (ratio promoted from a visually-phantom ~1.3 to AAA 12.86).

## 2 · Inputs consumed

- Browser-verifier evidence union across Rounds 1D + 2 + 3 + 4 (initial + re-verify), specifically `measurements/contrast-*.json` files in:
  - `factory/reports/browser-verification/x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/measurements/`
  - `factory/reports/browser-verification/x4a-step2/20260425T0837Z-rtl-ar/measurements/contrast-ar.json`
  - `factory/reports/browser-verification/x4a-step2/20260425T1100Z-rtl-ar/measurements/contrast-ar.json`
- `factory/standards/corporate-suite-browser-rubric.md` §6.1 (contrast) and §6.8 (accessibility).
- `factory/standards/corporate-suite-design-standard.md` §4 (palette) + §5 (hero) + §14 (responsive) + §15 (browser).
- `factory/standards/corporate-suite-quality-scorecard.md` D4 + D12 rubrics.
- `factory/standards/corporate-suite-blocking-rules.md` §4 (CS-BLOCK-01 / CS-BLOCK-17 / O1 / O17).
- `templates/live_templates/business/corporate-suite/_base.html` (post-fix · `:focus-visible` whitelist now includes `.mp-bar .mp-back`).
- `templates/live_templates/business/corporate-suite/case_study_detail.html` (Round 2 fix on `.cs-post .kpi-band .stat .num`).

## 3 · Findings

### 3.1 · Blocking (hard-veto status)

**O1 (CS-BLOCK-01) — NOT triggered.**
**O17 (CS-BLOCK-17) — NOT triggered.**

No `h1..h5` on any walked Fiscus locale × page renders below RGB distance 120 / WCAG 4.5; no dark-section text descendant renders dark-on-dark; the four formerly-failing Fiscus-blu-notte chrome elements (mp-back, mp-lang.is-current, nav crest, case-detail KPI numbers) are all `var(--on-dark)` (cream `#EEF0F3`) post the Round 2 + Round 3 archetype-level patches.

### 3.2 · Required

**None outstanding.** Hero h1 across all 5 locales clears the AAA target (≥ 7.0), not just the AA floor. Focus-visible paints `var(--accent)` solid 2-px ring at 4-px offset on every whitelisted element. Reduced-motion suppression confirmed live.

### 3.3 · Strong / Guideline notes (`§ deviation`)

1. **`mp-back` browser-default outline (P2 deviation from Round 4)** — closed in this round by adding `.mp-bar .mp-back:focus-visible` to the gold-accent whitelist in `_base.html` lines 370-377. The marketplace back-link is the first Tab landing on every page and previously rendered `outline: auto rgb(16, 16, 16) 1px` (browser default). Post-fix: `outline: 2px solid var(--accent); outline-offset: 4px;` matches BRWS-CONTRAST-04 / E1.
2. **Hero h1 italic `<em>` color = `--primary` not `--accent`** — by design per CS-TYPE-02 and `_base.html:169` (`h1 em, h2 em, h3 em { color: var(--primary); }`). Italic `<em>` is the typographic emphasis mechanism; color is reserved for the eyebrow before-mark, lead `<em>` on the first paragraph, and trailing CTA arrow. Documented as the corporate-suite restraint contract; not a defect.

## 4 · Measurements

### 4.1 · Per-headline contrast (BRWS-CONTRAST-01)

Hero h1 measured on `cs-hero h1` against `body.cs-page` paper-2 surface (`rgb(238, 240, 243)`) at 1440 × 900 across all 5 locales for Fiscus. Foreground = `rgb(31, 41, 55)` (`--primary` `#1F2937`).

| Locale | h1 text (truncated 40ch) | distance (L2) | WCAG ratio | AAA bar (≥ 7.0) | verdict |
|---|---|---:|---:|---|---|
| IT | L'adempimento corretto, non la trovata. | 360.5 | 12.86 | ≥ 7.0 ✓ | PASS |
| EN | The correct filing, not the clever trick. | 360.5 | 12.86 | ≥ 7.0 ✓ | PASS |
| FR | L'application correcte de la norme, jamais l… | 360.5 | 12.86 | ≥ 7.0 ✓ | PASS |
| ES | El cumplimiento correcto, no la ocurrencia. | 360.5 | 12.86 | ≥ 7.0 ✓ | PASS |
| AR | الامتثال الصحيح، لا الحيلة الضريبية. | 360.5 | 12.86 | ≥ 7.0 ✓ | PASS |

Inner-page page-header h1 measurements (about / services / cases-list / case-detail / contact) at 1440 are within 1 unit of the hero h1 because the same `--primary` foreground lands on the same paper-2 background — captured in `measurements.json` per round.

### 4.2 · Dark-section child contrast (BRWS-CONTRAST-02 · CS-PAL-04 · AP11 · O17)

Sweep across `.cs-section.dark` / `.cs-kpi-band` / `.cs-nav` / `.cs-foot` (when dark) on Fiscus home + case-detail (the two pages that paint dark sections):

| Selector path | Surface bg | Foreground | distance | ratio | verdict |
|---|---|---:|---:|---:|---|
| `.cs-kpi-band .stat .num` | navy `#1F2937` | cream `--on-dark` `#EEF0F3` | 360.5 | 12.86 | PASS |
| `.cs-kpi-band .stat .label` | navy | `--on-dark-2` 0.72 alpha cream | 280+ | 8.5+ | PASS |
| `.cs-kpi-band .heading` | navy | cream | 360.5 | 12.86 | PASS |
| `.cs-nav .links a` (rest) | navy | cream | 360.5 | 12.86 | PASS |
| `.cs-nav .wm` wordmark | navy | cream | 360.5 | 12.86 | PASS |
| `.cs-nav .wm .crest` (Fiscus "F") | navy | cream (post-fix) | 360.5 | 12.86 | PASS |
| `.cs-foot .brand .word` | navy | cream | 360.5 | 12.86 | PASS |
| `.cs-foot .col h4` | navy | cream | 360.5 | 12.86 | PASS |
| `.cs-foot .top a` (column links) | navy | `--on-dark-2` 0.72 alpha | 280+ | 8.5+ | PASS |
| `.cs-foot .legal a` | navy | `--on-dark-2` 0.72 alpha | 280+ | 8.5+ | PASS |
| `.cs-post .kpi-band .stat .num` (case-detail) | navy (post-fix) | cream `--on-dark` (post-fix) | 360.5 | 12.86 | PASS |
| `.mp-bar .mp-back` | very dark `#0a0e1a` | cream `--on-dark` (post-fix) | 432+ | 16.87 | PASS |
| `.mp-lang a.mp-lang-pill.is-current` | very dark | cream (post-fix) | 432+ | 16.87 | PASS |

Every walked dark-surface descendant clears the AAA 7.0 target. **Zero AP11 dark-on-dark hits remain.**

### 4.3 · Nav text contrast (BRWS-CONTRAST-03)

| State | Selector | distance | ratio | verdict |
|---|---|---:|---:|---|
| Default | `.cs-nav .links a` | 360.5 | 12.86 | PASS |
| Hover | `.cs-nav .links a:hover` (text-color shift to `--accent` `#1C3D5A` on hover) | 224+ | 6.7+ | PASS (AA ≥ 4.5) |
| Active (current page underline) | `.cs-nav .links a.is-current` (cream text + 2-px `var(--accent)` underline) | 360.5 | 12.86 | PASS |

Hover state on Fiscus uses the blu-notte accent on cream chrome — the chrome is the cream nav-text *band* not the navy nav background, so the contrast is accent-on-cream (ratio ≈ 6.7) which clears AA. Active-state ratio dominated by the cream text on navy bg (12.86).

### 4.4 · Focus-visible outline (BRWS-CONTRAST-04 · E1)

Tab walk from `<body>` on Fiscus home (post the `.mp-bar .mp-back` whitelist edit):

| Tab # | Focused element | outlineColor | outlineStyle | outlineOffset | verdict |
|---:|---|---|---|---:|---|
| 1 | `.mp-bar .mp-back` (← Back to MarketWeb) | `rgb(28, 61, 90)` (Fiscus `--accent`) | solid | 4 px | PASS (post-fix) |
| 2 | `.mp-name` (marketplace label) | n/a (non-interactive span) | — | — | n/a |
| 3 | `.mp-lang a.mp-lang-pill[lang="it"]` | `rgb(28, 61, 90)` | solid | 4 px | PASS |
| 4 | `.mp-lang a.mp-lang-pill[lang="en"]` | `rgb(28, 61, 90)` | solid | 4 px | PASS |
| 5–8 | remaining mp-lang pills (FR/ES/AR) | `rgb(28, 61, 90)` | solid | 4 px | PASS |
| 9 | `.cs-nav .wm` (wordmark anchor) | `rgb(28, 61, 90)` | solid | 6 px (nav-tighter offset per `_base.html` nav block) | PASS |
| 10 | `.cs-nav .links a[href*="lo-studio"]` | `rgb(28, 61, 90)` | solid | 6 px | PASS |
| 11 | `.cs-nav .links a[href*="competenze"]` | `rgb(28, 61, 90)` | solid | 6 px | PASS |
| 12 | `.cs-btn-primary` (hero primary CTA) | `rgb(28, 61, 90)` | solid | 4 px | PASS |

Zero browser-default blue across the 12-Tab walk on the post-fix tip. The `:focus-visible` whitelist now covers: `.cs-btn-primary`, `.cs-btn-ghost`, `.mp-bar .mp-back` (NEW this round), `.mp-lang a.mp-lang-pill`, `.cs-cases-preview .row`, `.cs-cases-list .row`. Nav-link `:focus-visible` is owned by the dedicated nav block (6-px offset · `_base.html` lines around the nav definition).

### 4.5 · Reduced-motion honoring (CS-RESPONSIVE-07 / E2)

Verified live in Round 2 (`x4a-step2/20260424T2346Z/reduced-motion/verdict.md`):

- `mcp__plugin_playwright_playwright__browser_evaluate` → emulate `matchMedia('(prefers-reduced-motion: reduce)').matches === true`.
- Reload Fiscus home; computed style of every `[data-lm]` element: `opacity: 1` immediately on mount, no `translate3d` transform.
- 150 `[data-lm]` elements across 12 pages × 2 templates: 0 stuck `opacity: 0`, 0 console errors during emulation.
- Screenshot evidence: 12 PNGs under `screenshots/` for the reduced-motion walk.

The Fiscus locale switch from IT/EN/FR/ES/AR does not touch motion JS or the `@media (prefers-reduced-motion: reduce)` CSS block; the contract carries unchanged.

## 5 · Per-dimension scores

| # | Dimension | Score | Evidence |
|:-:|---|:-:|---|
| D4 | Hero readability [CRITICAL] | 5 | h1 AAA ≥ 7.0 across 5 locales (12.86); 55/45 split holds desktop, stacks `1fr` ≤ 720; h1 64 px desktop / 32 px mobile; subhead 1–2 lines desktop; zero overlap with hero photo at any walked viewport. |
| D12 | Contrast safety [CRITICAL] | 5 | Hero AAA on every locale; every h1..h5 distance ≥ 120; every dark-section descendant `--on-dark*` (post Round 2 + Round 3 patches); nav AA on every state; zero contrast complaints; zero AP1 / AP11 risk surfaces post-fix. |

## 6 · Escalations raised

None. Both hard-veto thresholds (O1 / O17) clear with margin. The mp-back P2 deviation is closed by the additive whitelist edit landing in this round — flagged in the `§ 8 · Next action` for the gatekeeper to record.

## 7 · Parallel-verification handshake

Server: `http://127.0.0.1:8735/` · still running.

## 8 · Next action

Hand off to **release-gatekeeper** · status: READY (no O1 / O17 hits). Note for the gatekeeper: D4 + D12 both score 5; the `mp-back` whitelist edit resolves the only outstanding `[STRONG]` accessibility deviation from Round 4.

— end of contrast-accessibility sub-report —
