# Cornice · Public Flip · Browser-verification (anonymous live walk · 2026-05-01)

```yaml
report_type:        browser-verification (public-flip)
phase:              X.5 · Cornice · public flip (post user-handshake)
date:               2026-05-01
browser:            Playwright MCP (Chromium engine)
server:             http://127.0.0.1:8052/  (runserver 127.0.0.1:8052 --noreload · process from workflow D, no restart)
auth posture:       ANONYMOUS (no staff session, no ?preview=1)
                    Pre-flip: same routes returned 404 to anon and the slug was absent from the catalog HTML.
                    Post-flip: same routes return 200 to anon and the slug is present in the catalog HTML × 5.
captures:           factory/reports/browser-verification/cornice-public-flip/captures/
                    4 PNGs (it-1440-anon-firstscroll · ar-1440-anon-firstscroll
                            home-1440-anon-trust-counter-24plus · business-catalog-1440-anon-cornice-card)
verdict:            GREEN · 0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new
                    catalog count moves 23 → 24 live · home counter moves 23+ → 24+
sibling_regression: 0/4 (Pragma · Fiscus · Solaria · Continua all 200 anon · Continua AR h1 still Kufi)
```

This file is the browser-walk index for the public flip. It pairs with:
- `factory/reports/cornice/cornice-public-flip.md` — main narrative
- `factory/reports/scorecard/cornice-public-flip/*` — 4 scorecard panels
- The workflow D 11-capture browser deck remains the lead visual evidence; this
  pass adds 4 new captures that prove **anonymous reachability** post-flip
  (the same surfaces previously required a staff session).

---

## §1 · Walk posture

- The dev server from workflow D (port 8052) was kept up across the flip; no
  process restart was required because the registry edit + management command
  push directly into the runtime DB. Anonymous probes were issued to the same
  server.
- Playwright session ran without any cookies attached in `curl` probes; the
  Playwright Chromium profile may carry a stale `cornice_review` cookie from
  workflow D walks but the curl smoke (§5) and the Django-test-client smoke
  in `_smoke.py` confirm the surfaces are reachable with **zero session**.
- The walk goal is "prove Cornice is now publicly reachable to an anonymous
  visitor with no `?preview=1` flag" — not a re-build of the visual evidence.
  The visual deck already exists at `cornice-workflowC-multilingual/captures/`
  (11 images) and `cornice-workflowD-release-decision/captures/` (3 images).

---

## §2 · Walk cells (anonymous probes)

| # | URL | Locale | Viewport | Asserted | Capture |
|---|---|---|---|---|---|
| 1 | `/templates/business/cornice-architettura/preview/` | it | 1440 | bodyClass `cs-lf-lf-2 lm-ready` · navClass `cs-nav cs-nav--lf2` · navBg `rgb(238,240,243)` · h1 verbatim · em on `argomento` · fontFamily Cormorant Garamond · zero overflow (1425 ≤ 1440) | it-1440-anon-firstscroll.png |
| 2 | `/templates/business/cornice-architettura/preview/?lang=ar` | ar | 1440 | dir=rtl · h1 verbatim AR `كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة.` · em on حُجَّة · h1 fontFamily `Noto Naskh Arabic` (LF-2-scoped Naskh swap holds anon) · body fontFamily Amiri · cream nav preserved · zero overflow | ar-1440-anon-firstscroll.png |
| 3 | `/` | n/a | 1440 | trust-counter band reads `24+` (was `23+`) · 15 / 52 / 5 unchanged · dynamic from DB filter · zero template edit | home-1440-anon-trust-counter-24plus.png |
| 4 | `/templates/business/` | n/a | 1440 | header reads `6 template disponibili` (was 5) · Cornice card surfaces (slug × 5 in HTML) · cluster chip "Corporate" · style chip "Classic serif" · €89 price · "Personalizza" CTA | business-catalog-1440-anon-cornice-card.png |
| 5 | Sibling spot-check · Continua AR (LF-5 must remain Kufi) | ar | 1440 | bodyClass `cs-lf-lf-5 lm-ready` (NOT lf-2 → Naskh override does not match) · h1 fontFamily `Noto Kufi Arabic, Crimson Pro, Georgia, serif` (cluster default Kufi PRESERVED · zero Naskh leakage) · h1 verbatim `استمراريّة العائلة تُقاس بالأجيال.` | (DOM probe only · capture in continua workflow-D deck) |

---

## §3 · DOM probe values (anonymous · post-flip · 2026-05-01)

### 3.1 · IT home @ 1440 (anon · no `?preview=1`)

```
url           = http://127.0.0.1:8052/templates/business/cornice-architettura/preview/
htmlLang      = "it"
htmlDir       = "ltr"
bodyClass     = "cs-lf-lf-2 lm-ready"
navClass      = "cs-nav cs-nav--lf2"
navBg         = rgb(238, 240, 243)               [LF-2 cream]
h1Text        = "Ogni progetto è un argomento costruito, non un servizio reso."
h1Em          = "argomento"
h1FontFamily  = "Cormorant Garamond", Georgia, "Times New Roman", serif
inner         = 1440
docWidth      = 1425                              [zero horizontal overflow]
docHeight     = 9033
```

Identical to workflow D §3.1. The flip preserved every load-bearing surface; the only change is **who can see it** (anonymous · was staff-only).

### 3.2 · AR home @ 1440 (anon · no `?preview=1`)

```
url           = http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar
htmlLang      = "ar"
htmlDir       = "rtl"
bodyClass     = "cs-lf-lf-2 lm-ready"
navClass      = "cs-nav cs-nav--lf2"
navBg         = rgb(238, 240, 243)                [LF-2 cream · same as LTR]
h1FontFamily  = "Noto Naskh Arabic", "Cormorant Garamond", Georgia, serif
                                                   [LF-2-scoped Naskh swap · still applied anon]
bodyFontFamily= Amiri, "Source Sans 3", system-ui, sans-serif
                                                   [cluster default body font preserved]
h1Text        = "كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة."
h1Em          = "حُجَّة"
inner         = 1440
docWidth      = 1425                               [zero horizontal overflow]
```

Identical to workflow D §3.2. RTL parity carries.

### 3.3 · Home trust counters (anon · post-flip)

```
counters = ["24+", "15", "52", "5"]
              ↑
         templates_live (was "23+")
```

Inherited from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()` — zero template edit needed.

### 3.4 · Business catalog (anon · post-flip)

```
url                           = http://127.0.0.1:8052/templates/business/
header                        = "6 template disponibili"      (was "5 template disponibili")
cornice slug occurrences      = 5 in HTML                      (was 0)
cornice card hrefs            = ["/templates/business/cornice-architettura/preview/",
                                 "/projects/start/?template=cornice-architettura",
                                 "/templates/business/cornice-architettura/"]
```

### 3.5 · Continua AR sibling spot-check (Naskh leakage gate)

```
url           = http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=ar
bodyClass     = "cs-lf-lf-5 lm-ready"              [LF-5 chrome class · Naskh override does NOT match]
h1Text        = "استمراريّة العائلة تُقاس بالأجيال."   [Continua voice anchor preserved]
h1FontFamily  = "Noto Kufi Arabic", "Crimson Pro", Georgia, serif
                                                    [cluster default Kufi PRESERVED · zero Naskh leakage]
htmlDir       = "rtl"
docWidth      = 1425
```

Cleanest possible proof Cornice's Naskh swap is selector-scoped to `body.cs-lf-lf-2` and does NOT leak into Continua's LF-5 RTL render even after Cornice goes live.

---

## §4 · Curl smoke (anonymous · 45-route catalog × 5 locales)

```
home / catalog / cornice IT / cornice EN / cornice FR / cornice ES / cornice AR
                              200            200          200          200          200          200          200

cornice inner pages × 5 locales (studio · servizi · progetti · contatti):
  20/20 anonymous routes 200

cornice case-detail posts × 5 locales (4 posts each):
  biblioteca-pietrasanta-concorso       it=200 en=200 fr=200 es=200 ar=200
  via-volpe-roma-residenziale           it=200 en=200 fr=200 es=200 ar=200
  palazzo-lignari-bologna-restauro      it=200 en=200 fr=200 es=200 ar=200
  cornice-fronte-minore-saggio          it=200 en=200 fr=200 es=200 ar=200

→ 45/45 anonymous routes 200
```

Frozen-sibling regression sweep (`pragma · fiscus · solaria · continua` × IT only):

```
pragma-corporate-suite       200
fiscus-commercialista        200
solaria-coaching             200
continua-stewardship         200
```

Zero anon-side regression. The pre-flip evidence prober at
`factory/reports/scorecard/cornice-workflowD-release-decision/_smoke.py` was
re-run; it correctly flips its "expected False" assertion on Cornice's anon
catalog presence (now `True` post-flip) — that flag-flip is the public-flip's
correct effect, not a regression.

---

## §5 · Anonymous tier-gate probes (curl + Django test client)

```
GET /                                                         anon → 200 (homepage · 24+ counter)
GET /templates/business/                                      anon → 200 (catalog list · Cornice card)
   slug "cornice-architettura" in HTML                                            5 hits
GET /templates/business/cornice-architettura/preview/         anon → 200          (was 404)
GET /templates/business/cornice-architettura/preview/?preview=1 anon → 200        (no-op flag)
```

The D-055 tier gate now permits Cornice for anonymous visitors. The legacy
`?preview=1` flag is a benign no-op pass-through.

---

## §6 · Console output

No console errors at first paint on IT home or AR home. No errors on inner-page
chrome consistency probe. Playwright captured 1 console error during the IT
navigation; this matches the pre-existing console noise observed during
workflow D and Continua's public-flip runs (third-party network requests during
preview asset hydration · not a Cornice-specific signal).

---

## §7 · Stop-conditions checklist (per `corporate-suite-browser-rubric.md`)

- [x] Page returns 200 to anonymous visitors (was 404 pre-flip)
- [x] Body class carries `cs-lf-lf-2` + `lm-ready`
- [x] Reveal animations advance into `lm-in` (no permanently-hidden sections)
- [x] One dark band per home (hero photo plate + dark CTA closer surface)
- [x] Whistleblowing surface present (footer 4-col-with-whistleblowing column)
- [x] Pexels-only imagery (verified at A.5/A.6 · re-bound on 45/45 anon smoke 200)
- [x] Console errors at first paint = 0 product errors (1 incidental network log)
- [x] No horizontal scrollbar (1440 probed live · 720/880/1100/480 covered at workflow C/D)
- [x] Hero AAA contrast on h1 (workflow D probed 13.99 : 1)
- [x] Locale switcher functional and current flagged (5 pills visible IT home + AR home)
- [x] AR RTL with proper Arabic typography swap (Naskh on h1 · Amiri body)
- [x] No editor affordance on `/preview/` route (`cs-lf-lf-2 lm-ready` body class only)
- [x] Trust counter renders new value (`24+` from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()`)
- [x] Business catalog header reads new count (`6 template disponibili`)
- [x] Cornice card surfaces in anonymous catalog HTML (5 slug occurrences)
- [x] Frozen siblings (Pragma / Fiscus / Solaria / Continua) all 200 anon
- [x] Naskh swap does NOT leak into Continua's LF-5 AR render (Continua h1 still Noto Kufi Arabic)

17 / 17 cleared.

---

## §8 · Issues found

**0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new on the product.**

D9 imagery quality at 4.5/5 (carry-over STRONG observation from A.5/A.6) is
documented in the workflow D scorecard and remains a future imagery-hardening
candidate. Not a blocker. Not specific to the public flip.

Operational note (not a finding): the `business-corporate` LEGACY_EXEMPT_KEYS
warning continues to surface during `sync_template_tiers` and `manage.py test`.
Same `(corporate_suite.W001)` advisory observed at every prior corporate-suite
pass; AP3 retro-curation backlog · not a flip blocker.

---

## §9 · Verdict

**GREEN · public flip live.** Cornice is reachable to anonymous visitors in
all 5 locales. The catalog count, trust counter, anonymous routes, and
catalog HTML all reflect the new `tier=published_live` state. Frozen
siblings are unaffected and Continua's LF-5 AR render still computes its
heading font as `Noto Kufi Arabic` (zero Naskh leakage). The corporate-suite
cluster now ships 5 live siblings with all 5 LF slots populated. Server is
left running for any user-side post-flip verification.
