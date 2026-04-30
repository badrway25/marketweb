# Continua LF-5 · responsive-auditor

**Verdict**: PASS · 0 BLOCKING · 0 REQUIRED · 0 STRONG
**Date**: 2026-04-29 · IT-only walk
**Breakpoints walked**: 1920 · 1440 · 1100 · 720 · 480

The audit walks LF-5 at five breakpoints and confirms the family's responsive matrix lives entirely inside `_layouts/lf5/styles.html` without leaking into LF-1's matrix in `_base.html` (which Pragma/Fiscus/Solaria still run).

---

## 1 · 1920 · desktop reference

Captures: `continua-1920-fullpage-lf5-final.png` · section bounding boxes recorded in `walk-log.md`.

- Hero photo full-bleed at 1905px wide, min-height 720px. Frame 2-col (1.4fr/1fr) anchor + body. Credit overlays at 56/72px padding from corners.
- Cycle slot-2 cream paper · head 0.45fr/1fr · 3-col cell grid.
- Pillars 2×2 matrix · cream paper-2 background · each cell on white paper-3.
- KPI band slot-4 · pine full-bleed · 0.9fr + 4-col stat row.
- Sectors band slot-5 · cream paper-2 ribbon · 8 sector tags + whistleblowing eyebrow far-right.
- Leadership 3-col with 4:5 portrait above body.
- Timeline 116px year + 1fr title + 220px horizon + 60px arrow · 1px primary rail.
- CTA closer pine · 1fr/0.6fr.
- Footer 4-col 1.4fr/1fr/1fr/1fr · whistleblowing column at slot 4.

All 8 LF-5 sections render at the declared geometry. Body class `cs-lf-lf-5 lm-ready`.

## 2 · 1440 · narrow desktop

Captures: `continua-1440-fullpage-lf5.png`.

- Hero photo + frame + meta-strip preserved at 1440 (object-overlay holds).
- Cycle 3-col grid preserved at 1440.
- Pillars 2×2 matrix preserved at 1440 (matrix gap 64px → cells stay legible).
- KPI band 0.9fr + 4-col preserved.
- Leadership 3-col preserved.
- Timeline columns preserved.
- 4-col footer preserved.

No layout regressions at 1440.

## 3 · 1100 · large tablet

Captures: `continua-1100-fullpage-lf5.png`.

- Hero `min-height: 600px` · frame **stacks** to 1-col (anchor above body). Credit overlays still in two corners.
- Cycle head stacks to 1-col · cells go single-column with bottom rules.
- Pillars matrix collapses to 1-col (4 pillars stacked).
- KPI band heading stacks above 2-col stat row, padding 0 24px.
- Sectors band: whistleblowing eyebrow loses left-border + auto-margin · stacks below sectors.
- Leadership grid 2-col (third card wraps to second row).
- Timeline rail collapses (`:before` hidden); rows use 80px year + 1fr title + 56px arrow; horizon column hidden at 1100.
- CTA wrap stacks 1fr; actions go horizontal flex.
- Footer columns 1.4fr/1fr/1fr · whistleblowing column wraps to grid-column 1/-1 with top rule.

Critical-content reachability holds: timeline year + title + arrow remain readable.

## 4 · 720 · mobile

Captures: `continua-720-fullpage-lf5.png`.

- Hero `position: relative` photo at `aspect-ratio: 4/5` (portrait) · credit-row stacks vertically at top of photo · frame becomes a full-width primary-bg block below the photo (so AAA contrast on h1 holds without depending on photo luminance).
- Hero meta-strip 22px padding · 18px gap · flex-wrap.
- Cycle 1-col cells.
- Pillars 1-col matrix · `grid-template-columns: 56px 1fr` (icon + body) · padding 32 28 28.
- KPI band 1fr 1fr 2x2 with even cells alternating right-border. Heading 22px.
- Sectors row gap 14px · 10px font.
- Leadership 1-col.
- Timeline `64px year + 1fr title + 36px arrow` · year size 26px · title 16px.
- CTA wrap stacks; actions flex-direction column · `min-height: 44px` enforced on primary CTA (CS-CTA-01 touch target floor).
- Footer 1-col with whistleblowing column reflowed · single grid-column.

The CS-NAV-05 hamburger drawer takes over at ≤880 (inherited from `_base.html`). At 720px the drawer is engaged; LF-5 nav `padding: 12px 20px`; wordmark 18px.

**Whistleblowing column: surfaced on mobile.** The column reflows under the contact column with a top hairline rule, preserving all four legibility rules (eyebrow + body + email + policy link). CS-FOOT-02 holds.

## 5 · 480 · small phone

Captures: `continua-480-fullpage-lf5.png`.

- Hero credit-row 18 16 0 padding · frame 24 16 28 padding · meta-strip 18 16.
- Pillars 48px icon + 1fr · padding 24 18.
- KPI band 1-col with bottom rules.
- Timeline 56px year + 1fr title + 28px arrow · year 22px.

CS-RESPONSIVE-03 hero h1 floor (≥32px at ≤480) holds: `--fs-hero` cascades to 32px at the 480 breakpoint via the `_base.html` `--fs-hero: 32px` override. CS-RESPONSIVE-06 touch target floor (≥44px) holds on hero CTA + locale pills (inherited from cluster).

## 6 · Whistleblowing column reachability matrix

| Breakpoint | Channel column visible? | Email link reachable? | Policy link reachable? | Legal-row whistleblowing link visible? |
|---|---|---|---|---|
| 1920 | yes (4-col) | yes | yes | yes |
| 1440 | yes (4-col) | yes | yes | yes |
| 1100 | yes (wrapped to row) | yes | yes | yes |
| 720  | yes (1-col) | yes | yes | yes |
| 480  | yes (1-col) | yes | yes | yes |

CS-FOOT-02 (D.lgs. 24/2023 channel surfaced) holds at every breakpoint.

## 7 · Hamburger drawer

Engages at ≤880 (cluster invariant inherited from `_base.html`). LF-5 condensed-minimal-top nav at desktop (64px height) stacks into the same drawer below 880. The drawer carries:

- Wordmark
- 5 page links
- Phone block — **suppressed on LF-5** (`{% if template.layout_family != "LF-5" %}` guard at `_base.html:1056`)

Drawer touch targets ≥44px (CS-RESPONSIVE-06). Drawer focus traversal: burger toggle → 5 link rows → close (re-toggle).

## 8 · Layout matrix at-a-glance

| Section | 1920 | 1440 | 1100 | 720 | 480 |
|---|---|---|---|---|---|
| cs-hero | object-overlay 720px | 720px | 600px stacked | 4:5 photo + primary-bg frame | same · tighter padding |
| cs-cycle | 3-col grid | 3-col | 1-col cells | 1-col | 1-col |
| cs-pillars matrix | 2×2 | 2×2 | 1-col | 1-col compact | 1-col compact |
| cs-kpi-band | 0.9fr + 4 stats | same | heading-row + 2-col stats | 2x2 grid | 1-col |
| cs-sectors | row + far-right whistle | same | whistle wraps | mobile row | mobile row |
| cs-leadership | 3-col 4:5 portraits | same | 2-col | 1-col | 1-col |
| cs-cases-preview timeline | 116/1fr/220/60 | same | 80/1fr/56 (horizon hidden) | 64/1fr/36 | 56/1fr/28 |
| cs-cta | 1fr/0.6fr | same | 1-col | 1-col stacked | 1-col stacked |
| cs-foot 4-col | 1.4/1/1/1 | same | 1.4/1/1 + whistle wraps | 1-col | 1-col |

## 9 · Reduced-motion + reduced-data

- `prefers-reduced-motion: reduce` zeroes button transitions and `data-lm` reveals (cluster `_base.html` rule).
- Hero photo loaded as a CSS `background-image` URL — Pexels cache-busted query but no `<picture>` srcset; future imagery hardening pass should add `<picture>` with WebP/AVIF + multiple widths to satisfy reduced-data accessibility.

## 10 · Verdict summary

- 0 BLOCKING.
- All 5 breakpoints render correctly with the LF-5 family at the declared geometry.
- Hamburger drawer engages at the cluster's 880 breakpoint.
- Whistleblowing channel reachable at every breakpoint (CS-FOOT-02 holds).
- Hero h1 AAA contrast holds at every breakpoint (the dark plate fallback at 720 ensures cream-on-primary at minimum).
- Touch targets ≥44px on the hero/CTA primary clusters at ≤720.

**Approve at the responsive matrix.**
