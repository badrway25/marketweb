# Browser-verifier · Cornice Public Flip · 2026-05-01

**Tool**: Playwright MCP (Chromium engine)
**Server**: `http://127.0.0.1:8052/`
**Auth posture**: ANONYMOUS (no staff session, no `?preview=1`)
**Captures**: `factory/reports/browser-verification/cornice-public-flip/captures/` (4 PNGs)
**Verdict**: GREEN · 0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new

---

## 1 · Walk goal

Prove Cornice is now publicly reachable to an anonymous visitor in all 5
locales after the registry flip + DB sync. The visual evidence deck (11
captures) already exists at workflow C; this pass adds 4 anonymous-posture
captures that prove the **tier-gate change**, not the visual rendering.

## 2 · Captures (4 PNGs)

| File | URL | Locale | Posture | Asserts |
|---|---|---|---|---|
| `it-1440-anon-firstscroll.png` | `/templates/business/cornice-architettura/preview/` | it | anon | LF-2 chrome rendering · cream nav · h1 hero stack · KPI overlay on dark photo · zero overflow · was 404 pre-flip, now 200 anon |
| `ar-1440-anon-firstscroll.png` | `/templates/business/cornice-architettura/preview/?lang=ar` | ar | anon | RTL flow preserved · LF-2 cream nav preserved · Latin wordmark CORNICE preserved · hero KPI flows RTL · Naskh h1 typography preserved anonymously |
| `home-1440-anon-trust-counter-24plus.png` | `/` | n/a | anon | trust band reads `24+ template premium` (was `23+`) · 15 / 52 / 5 unchanged · live-bound from DB filter |
| `business-catalog-1440-anon-cornice-card.png` | `/templates/business/` | n/a | anon | header reads `6 template disponibili` (was 5) · Cornice card surfaces with €89 price + Corporate cluster chip + Classic-serif style chip + "Personalizza" CTA |

## 3 · DOM probes (anonymous · post-flip)

### 3.1 · IT home @ 1440

```yaml
url:           http://127.0.0.1:8052/templates/business/cornice-architettura/preview/
htmlLang:      it
htmlDir:       ltr
bodyClass:     "cs-lf-lf-2 lm-ready"
navClass:      "cs-nav cs-nav--lf2"
navBg:         rgb(238, 240, 243)               # LF-2 cream
h1Text:        "Ogni progetto è un argomento costruito, non un servizio reso."
h1Em:          "argomento"
h1FontFamily:  '"Cormorant Garamond", Georgia, "Times New Roman", serif'
inner:         1440
docWidth:      1425                              # zero horizontal overflow
docHeight:     9033
```

### 3.2 · AR home @ 1440

```yaml
url:           http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar
htmlLang:      ar
htmlDir:       rtl
bodyClass:     "cs-lf-lf-2 lm-ready"
navClass:      "cs-nav cs-nav--lf2"
navBg:         rgb(238, 240, 243)                # LF-2 cream · same as LTR
h1Text:        "كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة."
h1Em:          "حُجَّة"
h1FontFamily:  '"Noto Naskh Arabic", "Cormorant Garamond", Georgia, serif'
                                                  # LF-2-scoped Naskh swap (planner-brief §11)
                                                  # still applied anonymously
bodyFontFamily: 'Amiri, "Source Sans 3", system-ui, sans-serif'
inner:         1440
docWidth:      1425                               # zero horizontal overflow
```

### 3.3 · Home page trust counters

```yaml
counters: ["24+", "15", "52", "5"]
                ↑
           templates_live  (was "23+")
```

### 3.4 · Business catalog (anonymous)

```yaml
header:           "6 template disponibili"      # was "5 template disponibili"
cornice_in_html:  5 occurrences                  # was 0
cornice_hrefs:
  - /templates/business/cornice-architettura/preview/
  - /projects/start/?template=cornice-architettura
  - /templates/business/cornice-architettura/
```

### 3.5 · Continua AR (Naskh leakage gate · sibling spot-check)

```yaml
url:           http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=ar
bodyClass:     "cs-lf-lf-5 lm-ready"          # LF-5 chrome class (NOT lf-2 → Naskh swap does NOT match)
h1Text:        "استمراريّة العائلة تُقاس بالأجيال."
h1FontFamily:  '"Noto Kufi Arabic", "Crimson Pro", Georgia, serif'
                                                # cluster default Kufi PRESERVED · zero leakage
htmlDir:       rtl
docWidth:      1425
```

The single most load-bearing leakage check: Continua's LF-5 AR render still
computes its h1 to `Noto Kufi Arabic`. Cornice's LF-2-scoped Naskh swap is
genuinely scoped to `body.cs-lf-lf-2` and does NOT spread to the rest of the
RTL family.

## 4 · Anonymous route smoke (45/45)

```
Cornice public routes — ANONYMOUS:
  IT  home + studio + servizi + progetti + contatti                     5/5  200
  EN  home + studio + servizi + progetti + contatti                     5/5  200
  FR  home + studio + servizi + progetti + contatti                     5/5  200
  ES  home + studio + servizi + progetti + contatti                     5/5  200
  AR  home + studio + servizi + progetti + contatti                     5/5  200

  IT  4 case-detail posts                                               4/4  200
  EN  4 case-detail posts                                               4/4  200
  FR  4 case-detail posts                                               4/4  200
  ES  4 case-detail posts                                               4/4  200
  AR  4 case-detail posts                                               4/4  200

→ 45 / 45 anonymous routes 200
```

Frozen-sibling regression (anonymous · IT only):

```
pragma-corporate-suite       200    (LF-1)
fiscus-commercialista        200    (LF-3)
solaria-coaching             200    (LF-4)
continua-stewardship         200    (LF-5)

→ 4 / 4 frozen siblings 200
```

## 5 · Console output

No product console errors at first paint on IT or AR. Playwright captured 1
incidental console error during the IT navigation (matches workflow D
baseline · third-party network log on preview asset hydration · not Cornice-
specific).

## 6 · Stop-conditions (anonymous-posture)

- [x] Page returns 200 to anonymous visitors (was 404)
- [x] Body class carries `cs-lf-lf-2` + `lm-ready`
- [x] Trust counter renders `24+` (was `23+`)
- [x] Catalog header reads `6 template disponibili` (was 5)
- [x] Cornice card surfaces in anonymous catalog HTML (5 slug occurrences)
- [x] AR `html lang/dir` = `ar/rtl`
- [x] AR h1 fontFamily = `Noto Naskh Arabic, Cormorant Garamond, ...`
- [x] AR body fontFamily = `Amiri, "Source Sans 3", ...`
- [x] Zero horizontal overflow (1425 ≤ 1440)
- [x] Continua AR h1 still `Noto Kufi Arabic` (zero Naskh leakage)
- [x] Pragma / Fiscus / Solaria / Continua all 200 anon
- [x] No editor affordance on `/preview/` (`cs-lf-lf-2 lm-ready` body only)

12 / 12 cleared.

## 7 · Verdict

**GREEN.** Anonymous reachability live-verified across 5 locales × 9 routes
(home + 4 inner + 4 case-detail = 9 per locale × 5 = 45 routes). Trust
counter and catalog header reflect the new live count. Selector-scoped
Naskh swap holds without leaking. Frozen siblings unaffected. Public flip
is fully observable to anonymous visitors.
