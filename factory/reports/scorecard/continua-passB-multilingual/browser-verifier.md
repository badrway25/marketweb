# Browser verifier · Continua Pass B Multilingual · 2026-04-30

## 1 · Per-locale verdicts

### IT (baseline · 1440)

```
htmlLang: "it" · htmlDir: "ltr" · bodyClass: "cs-lf-lf-5 lm-ready"
title: "Continua — Lo studio"
h1: "La continuità di una famiglia si misura in generazioni."
em: ["generazioni"]
sections: ["cs-hero","cs-cycle","cs-pillars","cs-kpi-band","cs-sectors","cs-leadership","cs-cases-preview","cs-cta"]
horizontalOverflow: false (1425 = 1425)
```

**Verdict: PASS** — LF-5 sequence intact, voice anchor + em on `generazioni`, no overflow, body class `cs-lf-lf-5` exposes the family-scoped layout for any future scoped CSS rule.

### EN (1440)

```
htmlLang: "en" · htmlDir: "ltr"
title: "Continua — The practice"
h1: "The continuity of a family is measured in generations."
em (h1+h2): ["generations","cadence","one single","one single cadence","generations"]
cycleHeading:    "Continuity keeps a cadence, not a deadline."
pillarsHeading:  "Four practices, one single mandate"
casesHeading:    "Four mandates, four generations, one single cadence."
ctaHeading:      "The continuity of a family is measured in generations."
stations:  ["ARCHIVE ROOM · BRERA","COUNCIL TABLE · PRINCIPAL OFFICE","COMPLIANCE STUDIO · DOCUMENTARY CUSTODY"]
timeline:  4 entries · slug parity preserved (ar-side identical slugs)
sections (8): identical to IT
horizontalOverflow: false
```

**Verdict: PASS** — Native English equivalent of IT register · em-word travels on `generations` · 5 italic-em hits · stations natural · LF-5 sequence intact.

### FR (1440)

```
htmlLang: "fr" · htmlDir: "ltr"
title: "Continua — Le cabinet"
h1: "La continuité d'une famille se mesure en générations."
em: ["générations","cadence","un seul","une seule cadence","générations"]
cycleHeading:    "La continuité a une cadence, pas une échéance."
pillarsHeading:  "Quatre piliers, un seul mandat"
casesHeading:    "Quatre mandats, quatre générations, une seule cadence."
ctaHeading:      "La continuité d'une famille se mesure en générations."
stations:  ["SALLE DES ARCHIVES · BRERA","TABLE DU CONSEIL · SIÈGE PRINCIPAL","CABINET DE CONFORMITÉ · GARDE DOCUMENTAIRE"]
sections (8): identical to IT
horizontalOverflow: false
```

**Verdict: PASS** — Mirabaud/Edmond institutional register · em-word travels on `générations` · ordinal `4ᵉ` honoured.

### ES (1440)

```
htmlLang: "es" · htmlDir: "ltr"
title: "Continua — El despacho"
h1: "La continuidad de una familia se mide en generaciones."
em: ["generaciones","cadencia","un solo","una sola cadencia","generaciones"]
cycleHeading:    "La continuidad tiene una cadencia, no un plazo."
pillarsHeading:  "Cuatro pilares, un solo mandato"
casesHeading:    "Cuatro mandatos, cuatro generaciones, una sola cadencia."
ctaHeading:      "La continuidad de una familia se mide en generaciones."
stations:  ["SALA DEL ARCHIVO · BRERA","MESA DEL CONSEJO · SEDE PRINCIPAL","DESPACHO DE CUMPLIMIENTO · CUSTODIA DOCUMENTAL"]
sections (8): identical to IT
horizontalOverflow: false
```

**Verdict: PASS** — Banque Pictet España register · em-word travels on `generaciones` · ordinal `4ª` honoured · `€ 1.800 M` in Spanish numeric convention.

### AR (1440 · post-fix)

```
htmlLang: "ar" · htmlDir: "rtl"
title: "Continua — المكتب"
h1: "استمراريّة العائلة تُقاس بالأجيال."
em: ["بالأجيال","إيقاع","تفويض واحد","إيقاع واحد","بالأجيال"]
cycleHeading:    "للاستمراريّة إيقاع، لا موعدٌ نهائي."
pillarsHeading:  "أربعة محاور، تفويض واحد"
casesHeading:    "أربعة تفويضات، أربعة أجيال، إيقاع واحد."
ctaHeading:      "استمراريّة العائلة تُقاس بالأجيال."
stations:  ["قاعة الأرشيف · BRERA","طاولة المجلس · المقر الرئيسي","مكتب الامتثال · الحفظ الوثائقي"]
fontH1:    "Noto Kufi Arabic", "Crimson Pro", Georgia, serif
fontBody:  Amiri, "Public Sans", system-ui, sans-serif
KPI nums:  ["18","3","€ 1.8 B","4"] (Latin numerals preserved)
sections (8): identical to IT
horizontalOverflow: false
```

**Verdict: PASS** — Formal MSA / الفصحى register · em-word travels on `بالأجيال` · Latin proper nouns preserved (BRERA · Compliance · STEP · D.lgs.) · Latin numerals preserved · LF-5 sequence intact under RTL flip.

### AR (720 · responsive RTL)

```
pageW: 705 · scrollW: 705 · horizontalOverflow: false
LF-5 sections collapse: pillars 1-col · KPI 2x2 · leadership 1-col · timeline single-axis
Hamburger drawer engaged at ≤880 · whistleblowing column reachable in collapsed footer
```

**Verdict: PASS** — Mobile RTL collapse correct · no overflow · all content reachable.

### AR (1440 · contatti page)

```
h1: "خمس وأربعون دقيقة، جدول أعمال عائلي، دون التزام."
9 form labels: ["الاسم","اللقب","بريد إلكتروني سرّي","هاتف مباشر","النواة العائلية","الدور في العائلة","الأفق الزمني","الهيكل الحالي","النطاق العائلي"]
submitLabel: "ابدأ حواراً تفويضياً  →"  (arrow flipped via html[dir="rtl"] .cs-btn-primary:after { content: '←'; })
horizontalOverflow: false
```

**Verdict: PASS** — RTL form flow correct · 9 fields with right-aligned labels · helper text right-flowing · sidebar offices + channels RTL · whistleblowing channel surfaced.

## 2 · Locale switcher (CS-NAV-03)

5 pills render in the marketplace bar with correct lang attributes on every locale's home:

```
[lang="it"] IT  /templates/business/continua-stewardship/preview/
[lang="en"] EN  /templates/business/continua-stewardship/preview/?lang=en
[lang="fr"] FR  /templates/business/continua-stewardship/preview/?lang=fr
[lang="es"] ES  /templates/business/continua-stewardship/preview/?lang=es
[lang="ar"] AR  /templates/business/continua-stewardship/preview/?lang=ar
```

The current locale is flagged with `is-current`. Lang attributes are correct per pill. Hrefs propagate the staff-preview gate when active.

## 3 · `?preview=1` propagation across nav/footer (CS-LINK)

The corporate-suite chrome's staff-preview-aware href generation continues to work across all 5 locales — no Pass B regression. Internal links correctly carry both `?lang=xx` (when not at default) and `&preview=1` (when staff session) without dropping either flag on any nav, footer, marketplace bar, locale switcher, or in-page anchor link.

## 4 · Cases timeline `cases_parent_slug` resolution

The home cases-preview band correctly resolves the `mandati` parent slug (per the X.4 corporate-suite case-parent-fix · `home.html:660` reads `cases_parent_slug` from context, not the literal string `'case-studies'`). All 4 timeline rows on every locale's home reach `case_study_detail` at `/preview/mandati/<slug>/?lang=xx&preview=1` → 200.

## 5 · 45-route HTTP smoke walk

```
5 locales × (home + chi-siamo + custodia + mandati + contatti + 4 mandate-detail posts)
= 5 × 9 = 45 routes
Result: 45/45 → 200
```

## 6 · Verdict

Browser verifier GREEN across all 5 locales. The 14-cell walk × 5 locales = 70/70 PASS · 0 BLOCKING · 1 STRONG fix applied mid-walk (CS-TYPE-05 RTL reset extension) · 0 OBSERVATION on LTR locales · 7 captures filed · 6 instrumented evaluations recorded.
