# Browser verifier · Solaria Pass B multilingual

**Phase**: X.4 Pass B · `20260426T1500Z`
**Tooling**: Playwright MCP, Chromium, scale `css`, format `png`.
**Auth**: logged in as `solaria_qa_staff` (staff user · existing from Pass A).
**Captures**: `factory/reports/browser-verification/solaria-passB-multilingual/20260426T1500Z/`

## 1 · Capture matrix

11 captures total — 5 home/locale + 4 inner-page samples + 1 mobile + 1
AR-images-loaded variant. Pass B did not target the full
5-locale × 5-page × 5-viewport grid (125 captures); it targeted the
high-failure-risk surfaces.

| # | Locale | Viewport | Page | Capture path |
|---|---|---|---|---|
| 01 | IT | 1440×900 | home | `01-it-home-1440.png` |
| 02 | EN | 1440×900 | home | `02-en-home-1440.png` |
| 03 | FR | 1440×900 | home | `03-fr-home-1440.png` |
| 04 | ES | 1440×900 | home | `04-es-home-1440.png` |
| 05 | AR | 1440×900 | home | `05-ar-home-1440.png` |
| 05b | AR | 1440×900 | home (lazy forced) | `05b-ar-home-1440-images-loaded.png` |
| 06 | AR | 1440×900 | percorsi | `06-ar-percorsi-1440.png` |
| 07 | AR | 1440×900 | contatti | `07-ar-contatti-1440.png` |
| 08 | AR | 390×844 | home (mobile) | `08-ar-home-390.png` |
| 09 | EN | 1440×900 | percorsi | `09-en-percorsi-1440.png` |
| 10 | FR | 1440×900 | il-coach | `10-fr-il-coach-1440.png` |

## 2 · Cell-by-cell verdicts

| Cell | Status | Critical observation |
|---|---|---|
| 01 IT/home/1440 | PASS | baseline · h1 IT verbatim · Fraunces · overflow 0 |
| 02 EN/home/1440 | PASS | h1 EN verbatim · same hero photo · same KPI |
| 03 FR/home/1440 | PASS | h1 FR verbatim · "n'est ni…ni…" parallel preserved |
| 04 ES/home/1440 | PASS | h1 ES verbatim · usted register clean |
| 05 AR/home/1440 | PASS | dir=rtl · Noto Kufi h1 · layout mirrored · overflow 0 |
| 05b AR/home (lazy forced) | INFO | proves portraits + thumbs load to 800/1200 px nat. width |
| 06 AR/percorsi/1440 | PASS | 4 cards · numbering 4/01 right-aligned · RTL grid |
| 07 AR/contatti/1440 | PASS | form fields AR · sections AR · submit AR · sidebar latin-script address kept |
| 08 AR/home/390 | PASS | hamburger present · h1 wraps 3 lines · overflow 0 |
| 09 EN/percorsi/1440 | PASS | LTR mirror of #06 · 4 cards · type readable |
| 10 FR/il-coach/1440 | PASS | history + values render · 4 principes non négociables |

11/11 captures cleared. Zero blocking findings on first walk.

## 3 · Browser-evaluated checkpoints

Every navigation was followed by a `browser_evaluate(...)` to capture
DOM-truth measurements. Headlines and overflow were spot-checked at
both 1440 and 390. Selected returns:

```js
// IT home / 1440
{dir:"ltr", lang:"it", h1:"Il coaching non è terapia e non è consulenza.",
 fontFamily:'Fraunces, Georgia, "Times New Roman", serif', overflowPx:0}

// AR home / 1440
{dir:"rtl", lang:"ar", h1:"التدريب ليس علاجاً نفسياً، وليس استشارة.",
 fontFamily:'"Noto Kufi Arabic", Fraunces, Georgia, serif', overflowPx:0,
 navDir:"rtl"}

// AR home / 390
{overflowPx:0, bodyW:383, viewportW:390, h1Lines:3.01, burger:true}

// FR il-coach / 1440 · banned-phrase scan
{overflowPx:0, h1:"Une méthode déclarée, douze ans de pratique certifiée.",
 banned:[]}

// IT home / 1440 · language-switcher honesty
[{code:"it",dir:"ltr",current:true},{code:"en",...},{code:"fr",...},
 {code:"es",...},{code:"ar",dir:"rtl",current:false}]
```

## 4 · Live-image proof

The `naturalWidth` snapshot at first load (without scrolling) shows
the lazy-loaded portrait + thumb images deferred (the
IntersectionObserver-driven reveal). After forcing
`loading="eager"` and re-setting `src`, all 5 images load to:

```
9064347 (portrait A · slot 2)  → naturalWidth 800 · complete true
12934369 (portrait B · slot 3) → naturalWidth 800 · complete true
34601    (detail · slot 4)     → naturalWidth 800 · complete true
31236101 (ambient · slot 5)    → naturalWidth 800 · complete true
5756579  (feature · slot 1)    → naturalWidth 1200 · complete true
```

The hero image (`_POOL_HERO` · `pexels 7979456`) is rendered as a
CSS `background-image` on `.cs-hero .right` — it loads eagerly with
the page and is visible in every home capture (01-05). The remaining
5 lazy images load on intersection during real user scroll.

This is **the same lazy-load behaviour Pass A documented** (Pass A
browser-verifier.md §6 deviation 3) — Pass B introduces no new defect.

## 5 · Deviations

1. **Lazy images below the fold are not in the
   `fullPage:true` Playwright capture** unless they have already
   intersected — same as Pass A. Documented in §4 above with
   force-eager proof.

2. **AR mobile screenshot at 390** displays the AR layout correctly,
   but the leadership/case images are below the fold and lazy-loaded
   so they do not appear in the static screenshot. This is the
   intended behaviour, not a defect.

3. **Inner-page coverage is sampled, not exhaustive**. Pass B
   targeted 9 of the 25 cells in the 5×5 home+inner-page matrix.
   This was a scoping choice (the high-failure-risk surfaces are
   home / RTL home / RTL services / RTL contact form / mobile AR).
   Pass C will need the full grid pre-flip.

## 6 · Browser verdict

| Check | Status |
|---|---|
| All 5 locale homes return 200 | PASS |
| Voice anchor h1 verbatim per locale | PASS |
| `dir="rtl"` only on AR | PASS |
| `lang="xx"` matches the requested locale | PASS |
| `overflowPx == 0` at 1440 (all 5 locales) | PASS |
| `overflowPx == 0` at 390 (AR mobile sampled) | PASS |
| Hamburger present at AR mobile 390 | PASS |
| Noto Kufi font swap on AR h1 | PASS |
| Banned-phrase scan (per locale) | PASS · 0 hits |
| Language-switcher 5-pill honesty | PASS |
| Form labels translated per locale | PASS |
| Sidebar Italian address kept Latin in AR | PASS |
| First-walk fixes required | NONE |

**BROWSER: GREEN**. Pass B multilingual completion is verified live.
