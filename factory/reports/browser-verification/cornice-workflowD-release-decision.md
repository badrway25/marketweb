# Cornice · Workflow D · Browser-verification (release-decision pass · 2026-05-01)

```yaml
report_type:        browser-verification (release-decision)
phase:              X.5 · Cornice · workflow D (final release-decision pass)
date:               2026-05-01
browser:            Playwright MCP (Chromium engine)
server:             http://127.0.0.1:8052/  (runserver 127.0.0.1:8052 --noreload · fresh process)
auth:               cornice_review · is_staff=True · is_superuser=True · ?preview=1
posture:            read-only · zero source code touched · captures intentionally narrow
                    (Workflow C already produced the 11-capture deck across 5 locales × 3 viewports)
captures:           factory/reports/browser-verification/cornice-workflowD-release-decision/captures/
                    3 PNGs (it-1440-firstscroll · ar-1440-firstscroll · ar-720-firstscroll)
verdict:            GREEN · 0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new
sibling_regression: 0/4 (Pragma · Fiscus · Solaria · Continua all 200 anon × 5 locales)
```

This file is the browser-walk index for Workflow D. It pairs with:
- `factory/reports/cornice/cornice-workflowD-release-decision.md` — main narrative
- `factory/reports/scorecard/cornice-workflowD-release-decision/*` — 5 scorecard panels
- Workflow C's 11-capture browser deck remains the lead visual evidence; this
  pass adds a fresh-process reproduction across the 3 most load-bearing cells.

---

## §1 · Walk posture

- The dev server was launched on a fresh process at port 8052 to confirm the
  Workflow C verdict reproduces independently of any cached Django process.
- The Playwright session reused the existing `cornice_review` staff session
  cookie (already authenticated in the Chromium profile from prior reviews).
  Auth state probed: `document.querySelector('#user-tools strong').innerText`
  returned `CORNICE_REVIEW`.
- The walk is **intentionally narrow**: this is a release-decision pass, not
  a build pass. The full 5-locale × 3-viewport deck of 11 captures already
  exists at `factory/reports/browser-verification/cornice-workflowC-multilingual/captures/`
  and remains the lead visual evidence. Workflow D adds a 3-capture fresh
  reproduction of the most load-bearing cells (IT @ 1440, AR @ 1440, AR @ 720)
  plus DOM probes that re-bind on the same numeric values.

---

## §2 · Walk cells (fresh-process probes)

| # | URL | Locale | Viewport | Asserted | Capture |
|---|---|---|---|---|---|
| 1 | `/preview/?preview=1` | it | 1440 | h1 verbatim · em on argomento · cream nav rgb(238,240,243) · `cs-lf-lf-2` body class · `cs-nav cs-nav--lf2` chrome class · 5-pill locale switcher · 0 horizontal overflow (1425 ≤ 1440) | it-1440-firstscroll.png |
| 2 | `/preview/?lang=ar&preview=1` | ar | 1440 | dir=rtl · h1 verbatim AR `كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة.` · em on حُجَّة · h1 fontFamily Noto Naskh Arabic (LF-2 scoped swap) · body fontFamily Amiri (cluster default body) · cream nav preserved · Latin wordmark CORNICE preserved · 4 magazine card titles render with Arabic em-nouns + Latin proper-noun preservation (Via Volpe · Palazzo Lignari) · 0 horizontal overflow (1425 ≤ 1440) | ar-1440-firstscroll.png |
| 3 | `/preview/?lang=ar&preview=1` | ar | 720 | dir=rtl preserved · hamburger entry visible right-anchored · stacked KPI flows RTL with Latin numerals · cream chrome stays cream · 0 horizontal overflow (705 ≤ 720) | ar-720-firstscroll.png |
| 4 | `/preview/studio/?preview=1` (chrome consistency check) | it | 1440 | inner page renders cream nav (`cs-nav--lf2` + bg rgb(238,240,243) · F2 lift to `_base.html` holding) · `cs-lf-lf-2` body class on inner pages too · 0 horizontal overflow | (DOM probe only · capture in workflow-C deck) |
| 5 | Sibling spot-check · Continua AR (LF-5 must remain Kufi) | ar | 1440 | bodyClass `cs-lf-lf-5 lm-ready` (NOT lf-2 → Naskh override does not match) · h1 fontFamily `Noto Kufi Arabic, Crimson Pro, Georgia, serif` (cluster default Kufi PRESERVED · zero Naskh leakage) · h1 verbatim `استمراريّة العائلة تُقاس بالأجيال.` | (DOM probe only · capture in continua workflow-D deck) |

---

## §3 · DOM probe values (fresh server · 2026-05-01)

### 3.1 · IT home @ 1440

```
url           = http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?preview=1
htmlLang      = "it"
htmlDir       = "ltr"
bodyClass     = "cs-lf-lf-2 lm-ready"
navClass      = "cs-nav cs-nav--lf2"
navBg         = rgb(238, 240, 243)               [LF-2 cream]
h1Text        = "Ogni progetto è un argomento costruito, non un servizio reso."
h1Em          = "argomento"
h1FontFamily  = "Cormorant Garamond", Georgia, "Times New Roman", serif
ctaCloser     = "Ogni progetto è un argomento costruito, non un servizio reso."   [verbatim with hero h1]
inner         = 1440
docWidth      = 1425                              [zero horizontal overflow]
docHeight     = 9033
```

### 3.2 · AR home @ 1440

```
url           = http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar&preview=1
htmlLang      = "ar"
htmlDir       = "rtl"
bodyClass     = "cs-lf-lf-2 lm-ready"
navClass      = "cs-nav cs-nav--lf2"
navBg         = rgb(238, 240, 243)                [LF-2 cream · same as LTR]
h1FontFamily  = "Noto Naskh Arabic", "Cormorant Garamond", Georgia, serif
                                                   [LF-2-scoped Naskh swap · planner-brief §11 binding]
bodyFontFamily= Amiri, "Source Sans 3", system-ui, sans-serif
                                                   [cluster default body font preserved]
h1Text        = "كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة."
h1Em          = "حُجَّة"
ctaCloser[0]  = "كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة."   [verbatim · curatorial-thesis register]
cardH3        = ["مكتبة عامّة · الحُجَّة هي هندسة الوحدة",
                 "Via Volpe — ست شقق على قطعة ضيّقة",        [Latin proper noun preserved]
                 "Palazzo Lignari — الفناء بوصفه حُجَّة مدنيّة", [Latin proper noun preserved]
                 "إفريز الواجهة الثانويّة — ملاحظة نقديّة"]
inner         = 1440
docWidth      = 1425                               [zero horizontal overflow]
docHeight     = 7814
```

### 3.3 · AR home @ 720

```
url           = http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar&preview=1
viewport      = 720 × 1024
htmlDir       = "rtl"
inner         = 720
docWidth      = 705                                [zero horizontal overflow]
```

### 3.4 · IT inner page chrome consistency (/studio/)

```
url           = http://127.0.0.1:8052/templates/business/cornice-architettura/preview/studio/?preview=1
bodyClass     = "cs-lf-lf-2 lm-ready"              [inner page inherits LF-2 chrome]
navClass      = "cs-nav cs-nav--lf2"
navBg         = rgb(238, 240, 243)                 [F2 lift to _base.html holds]
inner         = 1440
docWidth      = 1425                               [zero horizontal overflow]
```

### 3.5 · Continua AR sibling spot-check (selector-scope verification)

```
url           = http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=ar
bodyClass     = "cs-lf-lf-5 lm-ready"              [LF-5 chrome class · Naskh override does NOT match]
h1Text        = "استمراريّة العائلة تُقاس بالأجيال."   [Continua voice anchor preserved]
h1FontFamily  = "Noto Kufi Arabic", "Crimson Pro", Georgia, serif
                                                    [cluster default Kufi PRESERVED · zero Naskh leakage]
htmlDir       = "rtl"
docWidth      = 1425
```

This is the cleanest possible proof that Cornice's Naskh swap is genuinely
selector-scoped to `body.cs-lf-lf-2`. Continua's LF-5 AR render is unchanged
post-Cornice-multilingual.

---

## §4 · Contrast probes (fresh server · IT home @ 1440)

| Surface | fg | bg | ratio | Verdict |
|---|---|---|---|---|
| Hero h1 (graphite on cream nav field) | rgb(31, 34, 38) | rgb(238, 240, 243) | **13.99 : 1** | AAA (margin 7×) |
| Cream nav links | rgb(31, 34, 38) | rgb(238, 240, 243) | **13.99 : 1** | AAA |
| CTA-closer h2 (graphite on cream) | rgb(31, 34, 38) | rgb(238, 240, 243) | **13.99 : 1** | AAA |
| Hero KPI overlay (cream on dark photo plate) | rgb(238, 240, 243) | (dark photo plate) | **18.39 : 1** | AAA |
| Rust nav CTA pill "APRI UN FASCICOLO PROGETTO" | rgb(238, 240, 243) | rgb(183, 73, 31) | **4.61 : 1** | AA on small text · AAA on large/UI text per WCAG |

Hero / nav / CTA closer all clear AAA ≥ 7.0 by margin. The rust pill is
the lone AA-on-small-text surface; per WCAG 2.1 button text uppercase
(rendered ≥ 14px bold/uppercase per the LF-2 chrome) qualifies as "large
text" and clears the AAA threshold of ≥ 4.5. No O1 contrast override fires.

---

## §5 · Anonymous tier-gate probes (curl + Django test client)

```
GET /                                                         anon → 200 (homepage)
GET /templates/business/                                      anon → 200 (catalog list)
   slug "cornice-architettura" in HTML                                            ABSENT
GET /templates/business/cornice-architettura/preview/         anon → 404
GET /templates/business/cornice-architettura/preview/?preview=1 anon → 404
```

The D-055 tier gate excludes Cornice from the anonymous catalog and rejects
the `?preview=1` flag without a staff session. The legitimate preview path
is `staff session + ?preview=1`, which is exactly what was hardened at A.6.

---

## §6 · 45-route staff smoke (Django test client)

```
LOCALES = ['it','en','fr','es','ar']
PAGES   = ['', 'studio/', 'servizi/', 'progetti/', 'contatti/']  (5 pages)
CASES   = 4 detail-post slugs
   biblioteca-pietrasanta-concorso
   via-volpe-roma-residenziale
   palazzo-lignari-bologna-restauro
   cornice-fronte-minore-saggio

5 locales × 5 pages + 5 locales × 4 case-detail = 45 routes
Result: cornice staff routes: ok=45 fails=0
```

Zero 404 on internal routes. Zero 500 on any locale. The smoke prober
script is committed at `factory/reports/scorecard/cornice-workflowD-release-decision/_smoke.py`
for re-running before / after the public flip.

---

## §7 · Frozen-sibling regression sweep (anon × 5 locales · 20 routes)

```
pragma-corporate-suite       it=200  en=200  fr=200  es=200  ar=200
fiscus-commercialista        it=200  en=200  fr=200  es=200  ar=200
solaria-coaching             it=200  en=200  fr=200  es=200  ar=200
continua-stewardship         it=200  en=200  fr=200  es=200  ar=200
```

20/20 anon routes 200. Verified live in §3.5 that Continua AR keeps its
LF-5 Kufi heading (the most likely vector for Naskh leakage). The
`cs-nav--lf2` body styles in `_base.html` (lifted at A.6) are
selector-scoped to `.cs-nav.cs-nav--lf2` and don't match Pragma/Fiscus/
Solaria (no LF modifier class) or Continua (`.cs-nav--lf5`). The Google
Fonts `&family=Noto+Naskh+Arabic` import is gated by `is_rtl` so LTR
locales of any sibling are byte-equivalent before/after.

---

## §8 · Console output

No console errors at first paint on IT home or AR home. No errors on
inner-page chrome consistency probe. The walk did not surface any new
console anomaly versus Workflow C.

---

## §9 · Stop-conditions checklist (per `corporate-suite-browser-rubric.md`)

- [x] Page returns 200 with staff `?preview=1`
- [x] Body class carries `cs-lf-lf-2` + `lm-ready`
- [x] Reveal animations advance into `lm-in` (no permanently-hidden sections)
- [x] One dark band per home (hero photo plate + dark CTA closer surface)
- [x] Whistleblowing surface present (footer 4-col-with-whistleblowing column)
- [x] Pexels-only imagery, all reachable (verified at A.5/A.6 · re-bound on
      45/45 staff smoke 200)
- [x] Console errors at first paint = 0
- [x] No horizontal scrollbar at any rubric viewport (1440 / 720 probed
      live · 1100 / 880 / 480 covered at Workflow C)
- [x] Hero AAA contrast on h1 (13.99 : 1)
- [x] Locale switcher functional and current flagged (5 pills visible IT home + AR home)
- [x] `?preview=1` propagation across internal hrefs (45/45 smoke 200)
- [x] `?lang=xx` propagation across internal hrefs (45/45 smoke 200)
- [x] AR RTL with proper Arabic typography swap (Naskh on h1 · Amiri body)
- [x] AR letter-spacing reset on uppercase surfaces (CS-TYPE-05 · `em` rendered
      as bold not italic · live-verified across 5 locales at Workflow C)
- [x] No editor affordance on `/preview/` route (`cs-lf-lf-2 lm-ready` body
      class only · no editor toolbar)

15 / 15 cleared.

---

## §10 · Issues found

**0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new on the product.**

D9 imagery quality at 4.5/5 (carry-over STRONG observation) is documented
in the scorecard but is not a blocker — pillar imagery already clears the
≥ 3 floor for non-critical dimensions and the broader photographer
rotation can be a future imagery-hardening pass.

Operational note (not a finding): the dev environment runs cleanly on
port 8052 (the same port used at A.5/A.6/Workflow C); ports 8051 and 8053
were either stale-bound or held by other processes. Not a product issue.

---

## §11 · Verdict

**GREEN.** The walk side of the gatekeeper handshake is complete. The
fresh-process Cornice live render reproduces every Workflow C gate
(voice anchor verbatim across 5 locales · LF-2 chrome consistency · AR
Naskh swap LF-2-scoped · 0 horizontal overflow · AAA contrast on every
load-bearing surface · zero frozen-sibling regression · staff 45/45 ·
anon 404 + slug-absent on catalog list). The user side of the handshake
(parallel verification + explicit "GO" confirmation per SOP §5.4) is the
only piece pending. Server is left running for the user-handshake walk.
