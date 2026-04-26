# responsive-auditor · Solaria controlled re-entry pass 1

**Subject**: `solaria-coaching` · IT-only at pass 1
**Run-ISO**: `20260426T0907Z`
**Reporter**: Claude (Opus 4.7) acting as `responsive-auditor` with hard-veto authority on O2 / O3.
**Method**: Playwright MCP `browser_resize` + `browser_evaluate` + `browser_take_screenshot`. Reduced-motion emulation active for fullPage captures.

---

## §1 · Viewport coverage in pass 1

| Viewport | Pages walked | Evidence |
|---:|---:|---|
| 1440 × 900 (desktop) | 5 / 5 | `screenshots/rm/01-home-…` … `05-contatti-…` |
| 768 × 1024 (tablet) | 1 / 5 (home spot) | `screenshots/rm/07-home-768-it-rm.png` |
| 390 × 844 (mobile) | 1 / 5 (home spot) | `screenshots/rm/06-home-390-it-rm.png` |

§ deviation 1 · Pass 1 walks **2 sample viewports + 1 floor desktop**, NOT the rubric §6 8-viewport sweep. Pass 3 will add 1920 + 1280 + 1100 + 1024 + 880 + 720 + 640 + 480 sweep when the archetype's 8-breakpoint matrix locks. This is plan-aligned per the controlled-reentry §1 framing — pass 1 ships IT-only + 3-viewport spot; pass 2 + 3 close the matrix.

## §2 · BRWS-VIEW-01 / 02 — no horizontal scroll

| Viewport | `scrollWidth` | `clientWidth` | overflow-x | Result |
|---:|---:|---:|---|---|
| 390 × 844 (home) | 390 | 390 | **0 px** | **PASS** |
| 768 × 1024 (home) | 768 | 768 | **0 px** | **PASS · spot** |
| 1440 × 900 (home/about/services/cases/contact) | 1440 | 1440 | **0 px** | **PASS · all 5 pages** (full-page screenshots show no horizontal overflow band) |

`html { overflow-x: clip }` root guard active (inherited from Step 1D). Zero horizontal-scroll occurrences across the 7 cells walked.

## §3 · BRWS-VIEW-06 — h1 ≥ 32 px @ 390

| Page | h1 font-size @ 390 | Result |
|---|---:|---|
| home | **32 px exact** | **PASS** (CS-RESPONSIVE-03 floor met) |

The home `--fs-hero` archetype variable resolves to 64 px @ ≥ 880 and steps down to 36 px @ ≤ 720 → 32 px @ ≤ 480 per the `home.html @media (max-width: 720px) { .cs-hero .left h1 { line-height: 1.1; max-width: none; } }` block. Solaria's hero text uses the same scale. **No Solaria-specific override.**

## §4 · BRWS-VIEW-07 — touch targets ≥ 44 × 44 @ 390

| Element | Width × Height @ 390 | Result |
|---|---:|---|
| `.cs-nav-burger` | **44 × 44** | **PASS** |
| `.cs-hero .left .cs-btn-primary` | min-height: 44px (per `@media (max-width: 720px)` rule) | **PASS** by computed-style declaration |
| `.cs-cta .actions .cs-btn-primary` | min-height: 44px (same rule) | **PASS** |

(`.mp-lang a.mp-lang-pill` returned no nodes — the marketplace bar's language pills are not present in the inner-preview chrome at this viewport.)

## §5 · Hamburger drawer at ≤ 880 px (CS-RESPONSIVE-04 inherited)

768 × 1024 (tablet) home capture confirms:
- Hamburger button visible at top-right of `.cs-nav`.
- Section list collapses (drawer closed at first paint, no CSS-only chord active).
- All 9 home sections render in single-column stack below.
- Photo right-pane stacks below text-left pane (CS-HERO-07 stack-at-≤720 honored).

## §6 · `cs-services .grid` and `cs-process .grid` collapse breakpoints

Solaria's `percorsi` page exercises 4 service cards + 4 process steps:
- Default `.cs-services .grid: 1fr 1fr` (2 columns × 2 rows for 4 cards) — **all 4 visible at 1440** (`screenshots/rm/03-percorsi-1440-it-rm.png`).
- `@media (max-width: 880px) { .cs-services .grid { grid-template-columns: 1fr } }` — single column at mobile.
- `.cs-process .grid: repeat(4, 1fr)` (4 columns at desktop) → `repeat(2, 1fr)` at ≤ 1100 → `1fr` at ≤ 720.

**All 4 process steps render under reduced-motion emulation** (`screenshots/rm/03-percorsi-1440-it-rm.png` middle band visibly populated with "01 Discovery call · 02 Contratto iniziale · 03 Percorso regolare · 04 Chiusura & follow-up").

## §7 · About-page timeline rendering

`il-coach` (about) has a 5-step `.cs-history .timeline` (5 method tappe). At 1440 × 900 the timeline renders as `display: grid` with `.step` items at `display: contents` (so the year-cell + body-cell sit on the parent grid). All 5 steps visible at the desktop capture and at the 1440 walked cell — **no missing steps**.

## §8 · O2 / O3 hard-veto

- **O2** (any horizontal scroll surviving on a walked cell): **CLEAR.** 0 / 7 cells.
- **O3** (any below-fold reveal stuck at opacity-0 under reduced-motion emulation, indicating a JS contract regression): **CLEAR.** Pass-1 captures all use reduced-motion emulation; every walked page renders every reveal-card visible. The default-motion behaviour (off-screen elements opacity:0 at static-capture time) is the archetype's intended IntersectionObserver UX, NOT a regression.

## §9 · Verdict

**PASS** at the 3-viewport sample walked in pass 1.

D13 capped at 4 due to § deviation 1 (3-viewport sample vs the rubric's 8-viewport floor). Every walked viewport is clean. Pass-3 will lift D13 to 5 by adding the full 8-breakpoint sweep at every locale.

The hardened archetype's responsive contracts (overflow-x:clip root guard, hamburger drawer at ≤880, h1 ≥32 px floor, touch-target ≥44×44, single-column stack at ≤720) carry through Solaria's content tree without a single Solaria-specific responsive defect.
