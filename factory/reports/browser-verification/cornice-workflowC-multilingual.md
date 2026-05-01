# Cornice · workflow C · browser verification (5 locales · Playwright MCP)

```yaml
report_type:        browser-verification
phase:              X.5 · Cornice · workflow C (multilingual rollout)
date:               2026-05-01
browser:            Playwright MCP (Chromium engine)
server:             http://127.0.0.1:8052/ (runserver 8052 --noreload)
auth:               cornice_review · staff · superuser · ?preview=1 query
locales_walked:     it · en · fr · es · ar (5/5)
viewports_walked:   1440 (lead) · 880 (burger entry) · 480 (mobile small)
captures:           factory/reports/browser-verification/cornice-workflowC-multilingual/captures/
                    11 PNGs (5 home @ 1440 + 1 studio AR + 1 contatti FR
                    + 1 progetti ES + 1 case-detail EN + AR @ 880 + AR @ 480)
verdict:            5-LOCALE WALK PASS · 0 review-blocking · 0 chrome-consistency · 0 editorial-rhythm
sibling_regression: 0/4 (Pragma · Fiscus · Solaria · Continua all 200 anon × 5 locales)
```

---

## §1 · Walk shape

| Step | URL | Locale | Viewport | Asserted | Capture |
|---|---|---|---|---|---|
| 1 | `/preview/?preview=1` | it | 1440 | h1 verbatim · em on argomento · cream nav · 4 magazine cards | 01-home-it-1440.png |
| 2 | `/preview/?lang=en&preview=1` | en | 1440 | h1 verbatim EN · em on argument · cream nav · 4 cards · CTA closer matches h1 | 02-home-en-1440.png |
| 3 | `/preview/?lang=fr&preview=1` | fr | 1440 | h1 verbatim FR · em on argument · cream nav · 4 cards | 03-home-fr-1440.png |
| 4 | `/preview/?lang=es&preview=1` | es | 1440 | h1 verbatim ES · em on argumento · cream nav · 4 cards | 04-home-es-1440.png |
| 5 | `/preview/?lang=ar&preview=1` | ar | 1440 | dir=rtl · h1 verbatim AR · em on حُجَّة · cream nav · Naskh heading font · Amiri body · Latin wordmark + Latin Marta Roveri preserved | 05-home-ar-1440-rtl.png |
| 6 | `/preview/studio/?lang=ar&preview=1` | ar | 1440 | RTL studio · history list · values · team · 4-col footer with whistleblowing column · D.lgs. 24/2023 reference preserved | 06-studio-ar-1440-rtl.png |
| 7 | `/preview/contatti/?lang=fr&preview=1` | fr | 1440 | French form labels · select options · consent text · 4-col footer · whistleblowing column | 07-contatti-fr-1440.png |
| 8 | `/preview/progetti/?lang=es&preview=1` | es | 1440 | Spanish list-page intro · cases lead | 08-progetti-es-1440.png |
| 9 | `/preview/progetti/biblioteca-pietrasanta-concorso/?lang=en&preview=1` | en | 1440 | English case-detail · breadcrumb · meta strip · KPI tuple · 3 sections · lead-partner Marta Roveri · team strip · next-dossier link | 09-case-detail-en-1440.png |
| 10 | `/preview/?lang=ar&preview=1` | ar | 880 | hamburger entry · stacked grid · RTL flow preserved | 10-home-ar-880-rtl.png |
| 11 | `/preview/?lang=ar&preview=1` | ar | 480 | mobile single-column · KPI strip wraps · cream chrome stays cream | 11-home-ar-480-rtl.png |

---

## §2 · DOM probes (live values · 5 locales)

The walk probed every locale's home for the load-bearing surfaces
flagged by intake §17 (sibling-collision audit) and planner-brief §6
(distinctness scoring). Live values:

### IT
```
html.lang             = "it"
html.dir              = "ltr"
body.className        = "cs-lf-lf-2 lm-ready"
nav.className         = "cs-nav cs-nav--lf2"
nav.bg                = rgb(238, 240, 243)  [paper · LF-2 cream]
hero.h1               = "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."
hero.eyebrow          = "STUDIO DI ARCHITETTURA · MILANO · DAL 2008"
hero.side_quote       = "L'architettura buona si <em>argomenta</em> — non si dimostra, non si vende, non si decora."
leadership.h2         = "Marta <em>Roveri</em>"
nav_links             = ["Lo studio","Archivio","Servizi","Progetti","Contatti"]
magazine.card_count   = 4
```

### EN
```
html.lang             = "en"
html.dir              = "ltr"
nav.bg                = rgb(238, 240, 243)
hero.h1               = "Every project is a built <em>argument</em>, not a service rendered."
hero.side_quote       = "Good architecture is <em>argued</em> — not demonstrated, not sold, not decorated."
leadership.h2         = "Marta <em>Roveri</em>"
nav_links             = ["The studio","Archive","Practice","Projects","Contact"]
cta_closer.h2         = "Every project is a built <em>argument</em>, not a service rendered."   [verbatim with hero.h1]
card1.h3              = "Civic library · the argument is the <em>geometry</em> of the module"
card2.h3              = "Via Volpe — six apartments on a narrow <em>lot</em>"
card3.h3              = "Palazzo Lignari — the courtyard as a civic <em>argument</em>"
card4.h3              = "The cornice of the <em>minor</em> façade — a critical note"
```

### FR
```
hero.h1               = "Chaque projet est un <em>argument</em> construit, non un service rendu."
hero.side_quote       = "La bonne architecture <em>s'argumente</em> — elle ne se démontre pas, ne se vend pas, ne se décore pas."
nav_links             = ["L'agence","Archive","Pratique","Projets","Contact"]
cta_closer.h2         = "Chaque projet est un <em>argument</em> construit, non un service rendu."   [verbatim]
card1.h3              = "Bibliothèque civique · l'argument est la <em>géométrie</em> du module"
card2.h3              = "Via Volpe — six logements sur <em>lot</em> étroit"
card3.h3              = "Palazzo Lignari — la cour comme <em>argument</em> civil"
card4.h3              = "La corniche de la façade <em>secondaire</em> — une note critique"
```

### ES
```
hero.h1               = "Cada proyecto es un <em>argumento</em> construido, no un servicio prestado."
hero.side_quote       = "La buena arquitectura se <em>argumenta</em> — no se demuestra, no se vende, no se decora."
nav_links             = ["El estudio","Archivo","Práctica","Proyectos","Contacto"]
cta_closer.h2         = "Cada proyecto es un <em>argumento</em> construido, no un servicio prestado."   [verbatim]
card1.h3              = "Biblioteca cívica · el argumento es la <em>geometría</em> del módulo"
card2.h3              = "Via Volpe — seis viviendas en <em>parcela</em> estrecha"
card3.h3              = "Palazzo Lignari — el patio como <em>argumento</em> cívico"
card4.h3              = "La cornisa de la fachada <em>menor</em> — una nota crítica"
```

### AR
```
html.lang             = "ar"
html.dir              = "rtl"
body.className        = "cs-lf-lf-2 lm-ready"
nav.className         = "cs-nav cs-nav--lf2"
nav.bg                = rgb(238, 240, 243)        [LF-2 cream · same as LTR]
h1.fontFamily         = "Noto Naskh Arabic", "Cormorant Garamond", Georgia, serif
                        [LF-2-specific Naskh swap · planner-brief §11 resolved]
body.fontFamily       = Amiri, "Source Sans 3", system-ui, sans-serif
                        [cluster default body font preserved]
hero.h1               = "كلّ مشروع <em>حُجَّة</em> مبنيّة، لا خدمة مُسداة."
hero.side_quote       = "العمارة الجيّدة <em>تُحاجَج</em> — لا تُبرهَن، ولا تُباع، ولا تُزيَّن."
leadership.h2         = "Marta <em>Roveri</em>"   [Latin script preserved · CS-NAV-06]
nav_links             = ["الاستوديو","الأرشيف","الممارسة","المشاريع","تواصل"]
cta_closer.h2         = "كلّ مشروع <em>حُجَّة</em> مبنيّة، لا خدمة مُسداة."   [verbatim]
card1.h3              = "مكتبة عامّة · الحُجَّة هي <em>هندسة</em> الوحدة"
card2.h3              = "Via Volpe — ست شقق على <em>قطعة</em> ضيّقة"
                        [Latin proper noun Via Volpe preserved]
card3.h3              = "Palazzo Lignari — الفناء بوصفه <em>حُجَّة</em> مدنيّة"
                        [Latin proper noun Palazzo Lignari preserved]
card4.h3              = "إفريز الواجهة <em>الثانويّة</em> — ملاحظة نقديّة"
```

---

## §3 · AR RTL parity walk (16 surfaces)

| Surface | LTR (IT) behaviour | RTL (AR) behaviour | Verdict |
|---|---|---|---|
| `<html dir>` | `ltr` | `rtl` | PASS |
| Heading font | Cormorant Garamond | Noto Naskh Arabic (LF-2-scoped swap · NOT cluster default Kufi) | PASS · planner-brief §11 binding |
| Body font | Source Sans 3 | Amiri | PASS · cluster default |
| Em rendering on h1 | rust italic | rust bold (CS-TYPE-05 reset · italics hostile to Arabic · bold conveys same emphasis) | PASS |
| Hero photo overlay credit-line | left-anchored | right-anchored (logical-property layer + explicit `right: 56px` LF-2 RTL block) | PASS |
| Hero KPI strip 3-tuple | flows left-to-right (47 / 18 / 6) | flows right-to-left, Latin numerals preserved | PASS |
| Hero 8/4 split | h1 inline-start, side-quote inline-end | h1 inline-start (=right), side-quote inline-end (=left) — flips correctly | PASS |
| Narrative drop-cap | rust drop-cap floats inline-start | drop-cap floats inline-start (now right) — letter is `ا` (alif) instead of `L` | PASS |
| Narrative side-rail | inline-end of body column | inline-end of body column — flips correctly | PASS |
| Sectors-ribbon · 12 typologies | flows left-to-right with `·` separators | flows right-to-left · Arabic-language sector names · Latin separators preserved | PASS |
| Leadership single-portrait grid | photo left, body right | photo right, body left — flips via grid direction | PASS |
| Magazine-grid 3+1 | hero card left (8-col), 3 small right | hero card right, 3 small left — `direction: rtl` on `.grid` | PASS |
| Magazine card content | photo top, copy below in flex column | same · text right-aligned · em-bold preserved | PASS |
| Nav wordmark | left-anchored split-wordmark | right-anchored split-wordmark · Latin "CORNICE / studio di architettura" preserved (CS-NAV-06) | PASS |
| Nav links + CTA pill | left-cluster + right-pill | right-cluster + left-pill, `letter-spacing: 0` (CS-TYPE-05 reset) | PASS |
| 4-col footer with whistleblowing | leftmost = studio · whistleblowing rightmost | rightmost = studio · whistleblowing leftmost — flips correctly · D.lgs. 24/2023 + email Latin preserved | PASS |

**16/16 RTL parity surfaces.** Zero broken layouts, zero typographical
hostility. The Naskh heading swap is the editorially correct choice —
the live render reads as an Arabic-language architectural-publication
masthead, not as a Pictet/Continua family-office display masthead.

---

## §4 · Frozen-sibling regression check

### Anonymous HTTP probe (all routes)

```
pragma-corporate-suite       it : 200    en : 200    fr : 200    es : 200    ar : 200
fiscus-commercialista        it : 200    en : 200    fr : 200    es : 200    ar : 200
solaria-coaching             it : 200    en : 200    fr : 200    es : 200    ar : 200
continua-stewardship         it : 200    en : 200    fr : 200    es : 200    ar : 200
```

All 20 frozen-sibling routes return 200 anonymous (each sibling is
already at tier=published_live · the LF-2 changes don't cross-cut).

### Visual spot-check on LF-5 Continua AR (most likely affected by font import)

```
url:                  /templates/business/continua-stewardship/preview/?lang=ar
html.lang             = "ar"
html.dir              = "rtl"
body.className        = "cs-lf-lf-5 lm-ready"
                        [LF-5 chrome class · NOT lf-2 · so the Naskh
                         override `body.cs-lf-lf-2` selector does not match]
hero.h1               = "استمراريّة العائلة تُقاس <em>بالأجيال</em>."
                        [Continua voice anchor preserved verbatim]
hero.h1.fontFamily    = "Noto Kufi Arabic", "Crimson Pro", Georgia, serif
                        [cluster-default Kufi preserved · NO Naskh leakage]
```

### Visual spot-check on LF-1 Pragma IT

```
url:                  /templates/business/pragma-corporate-suite/preview/
hero.h1               = "Dove si prendono le decisioni <em>che contano</em>."
hero.eyebrow          = "Advisory corporate · Milano · Francoforte · Zurigo"
nav.bg                = rgb(30, 41, 59)   [navy · LF-1 cluster default · NOT Cornice cream]
```

**Frozen-sibling verdict: 0/4 regression.**

---

## §5 · Distinctness verdict outside Italian

Translation work is the single most likely vector for "voice flatten"
into a generic corporate/advisory register. The walk asserted that
Cornice in EN/FR/ES/AR continues to read architecturally — not
generic corporate-advisory — at every load-bearing surface.

| Locale | Editorial-curatorial register check | Anti-flatten verdict |
|---|---|---|
| EN | "built argument" · "monographic series" · "stratigraphies" · "DAStU co-publication" · "MIBAC qualification" · "Soprintendenza filings" · "minor façade" · "cornice as civic device" | Architecture-press register PRESERVED · NOT business-advisory PASS |
| FR | "argument construit" · "collection monographique" · "stratigraphies" · "DAStU co-édition" · "qualification MIBAC" · "Soprintendenza" · "façade secondaire" · "corniche comme dispositif civil" | AMC / L'Architecture d'Aujourd'hui register PRESERVED PASS |
| ES | "argumento construido" · "colección monográfica" · "estratigrafías" · "coedición DAStU" · "cualificación MIBAC" · "Soprintendenza" · "fachada menor" · "cornisa como dispositivo cívico" | Arquitectura Viva / El Croquis register PRESERVED PASS |
| AR | "حُجَّة مبنيّة" · "السلسلة المونوغرافيّة" · "الطبقات الجيولوجيّة" · "DAStU co-edition" · "تأهيل MIBAC" · "Soprintendenza" · "الواجهة الثانويّة" · "الإفريز بوصفه أداة مدنيّة" | MENA architectural-press register PRESERVED · NOT Pictet-style family-office PASS |

The Italian normative refs (D.lgs., MIBAC, OAPPC, CNAPPC, PRG,
Soprintendenza, DAStU) survive untranslated in every locale's body
copy AND footer column, anchoring Cornice as a Milan-based studio in
every locale.

**Distinctness verdict outside Italian: PASS in 5/5 locales.**

---

## §6 · Editorial-spread integrity verdict

The two LF-2 load-bearing cells (single-portrait L6 + magazine-grid
L7) were re-walked at 1440 in all 5 locales:

### Single-portrait L6 (leadership)

| Locale | Eyebrow | h2 | Role subhead | Bio first sentence |
|---|---|---|---|---|
| IT | STUDIO FOUNDER · ARCHITETTA | Marta <em>Roveri</em> | fondatrice · responsabile editoriale dei fascicoli | Marta Roveri ha aperto Cornice nel 2008... |
| EN | STUDIO FOUNDER · ARCHITECT | Marta <em>Roveri</em> | founder · editorial lead on the dossiers | Marta Roveri opened Cornice in 2008... |
| FR | FONDATRICE DE L'AGENCE · ARCHITECTE | Marta <em>Roveri</em> | fondatrice · responsable éditoriale des fascicules | Marta Roveri a ouvert Cornice en 2008... |
| ES | FUNDADORA DEL ESTUDIO · ARQUITECTA | Marta <em>Roveri</em> | fundadora · responsable editorial de los fascículos | Marta Roveri abrió Cornice en 2008... |
| AR | مؤسِّسة الاستوديو · معماريّة | Marta <em>Roveri</em> | مؤسِّسة · مسؤولة تحرير الكرّاسات | افتَتَحَت Marta Roveri استوديو Cornice سنة 2008... |

The portrait↔copy gender agreement (Marta Roveri · feminine
gendered) is preserved in every locale. The leadership cell is
visually identical across locales — the photo, caption, h2 with em-
on-Roveri, role subhead, 2-paragraph bio, and 4-credentials list all
render at the same rhythm.

### Magazine-grid L7 (3+1 cases)

| Locale | Hero card photo dominance | 4 card titles render | Em-words distinct per card |
|---|---|---|---|
| IT | dominant photo (post-A.6 F3 fix) | 4/4 | geometria · lotto · argomento · minore |
| EN | dominant photo | 4/4 | geometry · lot · argument · minor |
| FR | dominant photo | 4/4 | géométrie · lot · argument · secondaire |
| ES | dominant photo | 4/4 | geometría · parcela · argumento · menor |
| AR | dominant photo · grid direction RTL | 4/4 | هندسة · قطعة · حُجَّة · الثانويّة |

Editorial-spread feel preserved in every locale. Card foot baselines
align between hero column and 3-card stack column at 1440 (same as
A.6 F3 verified) — locale-neutral CSS fix carries across locales.

---

## §7 · Verdict

| Cell | Verdict |
|---|---|
| 5 locales authored | PASS · all keys mirrored, all values translated |
| Voice anchor verbatim recurrence (h1 + CTA closer) | PASS · 5/5 locales |
| Em-noun preservation across magazine cards | PASS · 5/5 locales · 4 distinct em-nouns each |
| LF-2 layout shape preserved | PASS · zero edits to lf2/styles.html or lf2/content.html |
| LF-2 chrome (cream nav · 4-col footer) consistent across all 5 locales | PASS · cs-nav--lf2 active on all routes |
| AR Naskh-vs-Kufi decision | RESOLVED · Naskh on heading · Amiri on body · Latin wordmark + Latin Roveri preserved |
| AR RTL parity (16 surfaces) | PASS · 16/16 |
| Responsive at 880 + 480 | PASS · AR included |
| Frozen-sibling regression | NO REGRESSION · 0/4 · 20/20 routes 200 anon |
| Distinctness outside Italian | PASS · architectural register preserved in EN/FR/ES/AR |
| Test suite | 545/546 (same pre-existing failure as A.6) |
| tier=draft preserved | PASS · catalog still 23 published_live + 1 draft = 24 |

**Workflow C browser-verification verdict: GREEN · review-ready · public flip held.**
