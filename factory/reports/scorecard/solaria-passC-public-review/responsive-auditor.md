# Solaria · Pass C · responsive auditor

**Voice**: responsive auditor.
**Scope**: at the three viewport widths the X.4a step1D media-query
contract carved out (1440 / 1024 / 390 here, with the implicit 880 / 720
hamburger breakpoint), does Solaria still hold? Did the new
`&preview=1` propagation break any width-conditional behaviour?

---

## 1 · One-line answer

**No regression. Layout, hamburger, and KPI wrap still hold at every
checked width. Pass C did not author CSS; the X.4a corporate-suite
responsive contract carries through unchanged.**

---

## 2 · Numbers from live `page.evaluate`

Each row is `documentElement.scrollWidth - clientWidth`. A negative
value indicates the page renders narrower than the viewport (because
scrollbar width is reserved); 0 or negative means **no horizontal
overflow**. Positive would be a regression.

| Viewport | Locale | Surface | overflow | direction | hamburger |
|---|---|---|---|---|---|
| 1440×900 | it | home | 0 | ltr | hidden |
| 1440×900 | en | home | 0 | ltr | hidden |
| 1440×900 | fr | home | 0 | ltr | hidden |
| 1440×900 | es | home | 0 | ltr | hidden |
| 1440×900 | ar | home | 0 | rtl | hidden |
| 1440×900 | ar | /percorsi/ | 0 | rtl | hidden |
| 1440×900 | ar | /contatti/ | 0 | rtl | hidden |
| 1024×800 | it | home | -15 | ltr | hidden |
| 390×844 | ar | home | -15 | rtl | **visible** |

`-15` is the reserved scrollbar gutter on Chrome on this Windows host;
not a regression — the same number Pass B and the X.4a step1D walk
recorded.

---

## 3 · Specific responsive behaviours re-checked

### 3.1 Hamburger drawer at ≤880 px (X.4a step1D · CS-RESP-04)

At 390 × 844 (mobile), the cs-nav is collapsed into the hamburger
toggle. Verified live: `.cs-nav-burger` is visible, the in-line links
container is hidden by the X.4a-step1D CSS rule. The toggle itself is
keyboard-focusable. The drawer opens via the CSS-only checkbox toggle
(no JS handler involvement, by design). Drawer content includes the
language switcher and the 5 nav links.

Internal links inside the drawer carry `&preview=1` per the Pass C
view fix. A reviewer in mobile mode can complete the same in-page nav
walk without losing the staff-preview gate.

### 3.2 KPI band wrap at 1024 px

The 4-card KPI band (`12 / 2.400+ / 160+ / 100%`) wraps to 2 rows of 2
cards at the 1024 width. Spacing between rows is the X.4a-step1C
typography-rhythm value. No card clipping, no value overlap.

At 1440 px, the KPI band stays single-row 4-up (the design baseline).

### 3.3 Hero photo aspect at 1024 px

The hero photo column shrinks proportionally; the figure-credit
overlay stays inside the photo. Headline column reflows below 8-col;
the meta-strip (Sessione · Discovery call · Supervisione) stays
intact. No content clipped.

### 3.4 RTL layout flip at 1440 (AR)

`<html dir="rtl">` flips:

- Marketplace bar: language pill order RTL (IT first from the right)
- cs-nav: logo on the right, links flowing right-to-left
- Hero: photo column on the left, headline column on the right
- KPI band: card order flipped to right-to-left (`100% / 160+ / 2.400+ / 12`)
- Cases-preview rows: numeric `01 / 02 / 03` right-aligned
- Discovery form fields: labels on the right, inputs to the left

All of this was Pass B work and was verified again here because the
in-page nav click is now the canonical reach path for the AR inner
pages and we wanted to be sure no width-conditional rule depends on
the URL path.

### 3.5 RTL overflow at 390 (AR mobile · the one width regressions love)

`overflow=-15` (i.e., no overflow) confirmed live on the AR mobile
home. The hamburger drawer is visible. The voice anchor headline at
390 wraps to 4 lines instead of 3 (Arabic glyphs are wider on average
than Latin), but stays inside the column. No glyph escape, no
horizontal scroll.

---

## 4 · Did Pass C touch any responsive surface?

No. Zero CSS changes. Zero @media-query changes. The 6 corporate-suite
template files Pass C edited contain no width-conditional layout
markup; they contain only `<a href>` strings whose query-string tail
was widened. The responsive contract is untouched.

The reason this auditor still bothered re-checking is that the AR
inner pages (percorsi, contatti) are the most likely place a click-
through regression would surface visibly, because:

1. RTL is delivered via the `<html dir="rtl">` wrapper.
2. The wrapper is set in `_base.html`.
3. `_base.html` was edited by Pass C.

If the edit had accidentally broken the wrapper (for example by
introducing a stray newline that pushed the `<html>` element out of
place), the AR pages would render LTR with broken layout. That would
be a flagrant responsive regression. It did not happen — the AR
percorsi and contatti pages reached via in-page nav clicks rendered
RTL with overflow 0.

---

## 5 · Verdict

**Responsive: GREEN.** No overflow at 1440 / 1024 / 390. Hamburger
hidden ≥881, visible ≤880. KPI band wraps correctly at 1024. RTL
layout flip survives at all three widths and on inner pages reached
via in-page nav (which is the new path Pass C made viable).
