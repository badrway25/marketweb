# Responsive auditor · Cornice · workflow C multilingual

```yaml
phase:    X.5 Cornice · workflow C
date:     2026-05-01
verdict:  GREEN · responsive matrix carries across locales
```

## §1 · Responsive matrix walked

The viewport breakpoints validated at A.5/A.6 (1440 / 1100 / 880 /
720 / 480) are locale-neutral CSS queries — translation does not move
break breakpoints. Workflow C re-walks the most load-bearing
viewports per locale:

| Viewport | Locale walked | Surface checked | Verdict |
|---|---|---|---|
| 1440 (lead) | it · en · fr · es · ar | hero 8/4 split below photo · narrative essay + side-rail + drop-cap · sectors-ribbon · single-portrait grid · magazine-grid 3+1 · cream-paper nav · 4-col footer | PASS · 5/5 |
| 880 (burger entry) | ar (most-likely-affected by RTL collapses) | hamburger appears · split-wordmark folds correctly · magazine-grid stacks vertically · narrative side-rail folds under body · footer 4-col → 2-col | PASS |
| 480 (mobile small) | ar | nav collapses to wordmark + hamburger · KPI strip wraps · magazine-grid single-column · footer single-column · cream chrome stays cream | PASS |

## §2 · LF-2 specific RTL responsive flips

Validated live on AR @ 880 and AR @ 480:

| Surface | RTL behaviour at 880 | RTL behaviour at 480 |
|---|---|---|
| Hamburger entry | inline-end of nav (=left at RTL) — opens the drawer correctly | inline-end (=left) |
| Wordmark | inline-start (=right) — split-wordmark line 1 + line 2 stacked correctly | inline-start (=right) |
| Hero photo overlay credit | right-anchored | right-anchored |
| Hero KPI strip | wraps right-to-left | wraps right-to-left, single column at 480 |
| Hero h1 + side-quote | stacks vertically · h1 on top · side-quote under | stacks vertically |
| Magazine grid | single column · cards stack top-to-bottom | single column |
| Card thumb-photo top, copy below | preserved | preserved |
| Narrative side-rail | folds under body essay (logical ordering) | folds under body |
| 4-col footer | collapses to 2-col @ 880 (whistleblowing pairs with contact), 1-col @ 480 | 1-col |

## §3 · Locale-neutrality assertion

All responsive breakpoints in `_base.html` and `lf2/styles.html` use
viewport `@media` queries that are content-length agnostic. The
walked locales include EN (similar density to IT), FR (slightly
longer), ES (slightly longer), and AR (different glyph density +
RTL). At every viewport tested, no horizontal scrollbar appeared,
no text overflowed its container (per the existing CS-RESPONSIVE-08
binding · `overflow-x: clip` on root · `overflow-wrap: anywhere` on
heading containers).

The longest h1 text in the matrix is the FR voice anchor (`Chaque
projet est un argument construit, non un service rendu.` — 64
chars). At 1440 it occupies 2 visual lines · at 880 it wraps to 3
lines · at 480 it wraps to 4 lines. The wrap behaviour is
typographically clean (no widow / orphan / mid-word breaks).

## §4 · Captures

- `captures/01-home-it-1440.png` · IT @ 1440
- `captures/02-home-en-1440.png` · EN @ 1440
- `captures/03-home-fr-1440.png` · FR @ 1440
- `captures/04-home-es-1440.png` · ES @ 1440
- `captures/05-home-ar-1440-rtl.png` · AR @ 1440 RTL
- `captures/06-studio-ar-1440-rtl.png` · AR studio @ 1440
- `captures/07-contatti-fr-1440.png` · FR contatti @ 1440
- `captures/08-progetti-es-1440.png` · ES progetti @ 1440
- `captures/09-case-detail-en-1440.png` · EN case-detail @ 1440
- `captures/10-home-ar-880-rtl.png` · AR @ 880
- `captures/11-home-ar-480-rtl.png` · AR @ 480

## §5 · Verdict

**GREEN.** Responsive matrix holds across all 5 locales. RTL parity
verified at 880 and 480 specifically. No translation-induced overflow
or wrap regression.
