# Responsive auditor · Solaria Pass B multilingual

**Phase**: X.4 Pass B · `20260426T1500Z`
**Scope**: layout fit / overflow / breakpoint behaviour across 5 locales.

## 1 · What Pass B did NOT change

Pass B added content only — no CSS edits, no breakpoint media-query
changes, no template edits. The corporate-suite responsive
infrastructure (X.4a step 1D `@media 1280 / 1100 / 880 / 720 / 480`
+ CSS-only hamburger drawer at ≤880 + `overflow-x: clip` root guard)
is unchanged. Solaria inherits all of it for every locale.

## 2 · Per-locale overflow proof at 1440 × 900

Live `browser_evaluate(() => document.documentElement.scrollWidth -
document.documentElement.clientWidth)` after navigation:

| Locale | Page | Viewport | overflowPx |
|---|---|---|---|
| IT | `/` (home) | 1440 × 900 | **0** |
| EN | `/` (home) | 1440 × 900 | **0** |
| FR | `/` (home) | 1440 × 900 | **0** |
| ES | `/` (home) | 1440 × 900 | **0** |
| AR | `/` (home) | 1440 × 900 | **0** |
| AR | `/percorsi/` | 1440 × 900 | **0** |
| AR | `/contatti/` | 1440 × 900 | **0** |
| EN | `/percorsi/` | 1440 × 900 | **0** |
| FR | `/il-coach/` | 1440 × 900 | **0** |

No locale drives layout overflow at 1440. The X.4a step 1D root guard
(`html { overflow-x: clip }`) provides a defensive backstop, but the
Solaria layout reaches the floor on its own — overflow is zero, not
clipped.

## 3 · Mobile breakpoint check at 390 × 844

The most demanding combination — Arabic + 390 px viewport — was
verified live:

```js
{ overflowPx: 0, bodyW: 383, viewportW: 390,
  h1Lines: 3.01, burger: true }
```

- **overflowPx = 0**: zero horizontal overflow at the iPhone-13/14
  viewport.
- **bodyW = 383, viewportW = 390**: the body is narrower than the
  viewport (no overflow even when the body is fully laid out).
- **h1Lines = 3.01**: the AR h1 wraps to 3 lines at 390 px. This is
  healthy — the CS-HERO-05 floor (`<= 4 lines at 390 px`) is met with
  margin.
- **burger: true**: the CSS-only hamburger drawer is present (X.4a
  step 1D) at the AR mobile breakpoint, exactly like LTR locales.

Capture `08-ar-home-390.png` shows the full mobile AR page stacked
correctly: nav bar with hamburger + logo + locale pills, hero h1
wrapping to 3 lines, hero photo full-width below the headline, KPI
band stacked, sectors ribbon stacked, leadership cards stacked,
trust band stacked, CTA band stacked, footer columns stacked
vertically.

## 4 · Typography fit across locales

The four added locales add more or fewer characters than the IT
source per string, depending on language compactness. Nothing
overflows because the corporate-suite layout uses fluid widths (max
72ch) and `text-wrap: balance` on h1/h2.

Spot-check of representative h1 widths at 1440 px:

| Locale | h1 char count | wrap behaviour | result |
|---|---|---|---|
| IT | 47 chars | 2 lines · balanced | clean |
| EN | 50 chars | 2 lines · balanced | clean |
| FR | 53 chars | 2 lines · balanced | clean |
| ES | 50 chars | 2 lines · balanced | clean |
| AR | 41 chars (RTL counted) | 2 lines · RTL balanced | clean |

No locale drives the h1 onto a fourth line at 1440 px. Fraunces (and
Noto Kufi for AR) scale reads well at the archetype's display size
(`clamp(2.6rem, 6vw, 4.4rem)`).

## 5 · KPI numeral alignment

The KPI band uses `font-variant-numeric: tabular-nums` (X.4a
step 1C) so figures align across locales:

```
12       2,400+    160+    100%       (EN)
12       2.400+    160+    100%       (IT/ES)
12       2 400+    160+    100 %      (FR)
12       2.400+    160+    100%       (AR · Latin digits)
```

The narrow no-break-space in FR (`2 400+`) and the AR Latin-digit
choice both keep the column gutter stable — no ragged figures. This
is the same convention every other corporate-suite sibling uses.

## 6 · Service-card grid (`/percorsi/`)

The 4-card services grid was sampled at 1440 in EN + AR:

| Locale | columns | card height variance | overflow |
|---|---|---|---|
| EN | 2 × 2 | within ±8 px | none |
| AR | 2 × 2 (RTL) | within ±8 px | none |

The grid uses `grid-template-columns: repeat(2, minmax(0, 1fr))` with
`row-gap: 32px`. AR cards mirror correctly (card 4/01 is on the right,
card 4/02 on the left, etc.) — verified in `06-ar-percorsi-1440.png`.

## 7 · Form (`/contatti/`)

The 9-field discovery-call form was sampled at 1440 in AR. All form
fields render with full Arabic labels, the section headings (4 of
them) render right-aligned, the upload-zone primary text and link
render Arabic, the submit button renders right-aligned with a left-
pointing arrow that respects RTL flow. Capture
`07-ar-contatti-1440.png` is the proof.

## 8 · Responsive verdict

| Check | Status |
|---|---|
| 1440 × 900 overflow (all 5 locales) | PASS · 0 px |
| 390 × 844 AR overflow | PASS · 0 px |
| Mobile hamburger AR | PASS · `burger: true` |
| AR h1 wraps to ≤ 4 lines at 390 px | PASS · 3.01 lines |
| Service-card grid AR mirror | PASS |
| Form fields AR mirror + label render | PASS |
| Tabular numerals across locales | PASS · inherited from archetype |
| Footer 4-column stack at mobile | PASS · inherited from archetype |

**RESPONSIVE: GREEN**. The Pass-A responsive baseline (X.4a step 1D)
holds across all 4 added locales, including the most-demanding AR-mobile combination.
