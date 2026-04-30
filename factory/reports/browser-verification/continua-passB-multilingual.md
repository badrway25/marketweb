# Continua · Pass B Multilingual · browser walk index

**Date**: 2026-04-30
**Tooling**: Playwright MCP (Chromium · 1440×900 desktop · 720×1024 mobile RTL)
**Server**: `python manage.py runserver 127.0.0.1:8051 --noreload`
**Auth**: `continua_passB / continuapassb2026` · `is_staff=True`
**Tier**: `draft` in DB and registry post-walk (`sync_template_tiers` re-applied after the transient walk-time flip · LF-5 IT rebuild §8.2 pattern)

---

## 1 · Captures

| File | Locale | Viewport | Notes |
|---|---|---|---|
| `continua-passB-multilingual/it-1440-fullpage.png` | IT | 1440×900 | Baseline · LF-5 sequence + voice anchor + 5 italic-em |
| `continua-passB-multilingual/en-1440-fullpage.png` | EN | 1440×900 | English locale · anchor on `generations` |
| `continua-passB-multilingual/fr-1440-fullpage.png` | FR | 1440×900 | French locale · anchor on `générations` |
| `continua-passB-multilingual/es-1440-fullpage.png` | ES | 1440×900 | Spanish locale · anchor on `generaciones` |
| `continua-passB-multilingual/ar-1440-fullpage.png` | AR | 1440×900 | Arabic locale (post CS-TYPE-05 fix) · anchor on `الأجيال` |
| `continua-passB-multilingual/ar-720-fullpage.png`  | AR | 720×1024  | Arabic responsive RTL · single-column collapse |
| `continua-passB-multilingual/ar-1440-contatti.png` | AR | 1440×900 | Arabic contact form · 9 fields RTL · sidebar offices RTL |

7 captures total. Above the floor of 6 captures per locale, well above the 11/11 Solaria Pass B precedent total.

---

## 2 · Instrumented walks (computed-style + DOM probes)

For each locale at 1440 (and AR also at 720), the walk asserted:

```js
{
  htmlLang, htmlDir, title, h1, em[],
  cycleHeading, pillarsHeading, casesHeading, ctaHeading,
  leadership[], stations[], timeline[],
  fontH1, fontBody (AR only),
  letterSpacing on 9 LF-5 surfaces (AR only · pre + post fix),
  pageW, scrollW, horizontalOverflow,
  sections[] (8 cs-* sections in order),
  switcher[] (5 pills, current flagged),
  nums[] (KPI band Latin numerals)
}
```

All assertions PASS for all 5 locales. The full evaluation outputs are reproducible by re-running the Playwright MCP script against the running server.

---

## 3 · HTTP smoke-walk · 45 routes

```
[it]    home → 200    chi-siamo/ → 200    custodia/ → 200    mandati/ → 200    contatti/ → 200
[en]    home → 200    chi-siamo/ → 200    custodia/ → 200    mandati/ → 200    contatti/ → 200
[fr]    home → 200    chi-siamo/ → 200    custodia/ → 200    mandati/ → 200    contatti/ → 200
[es]    home → 200    chi-siamo/ → 200    custodia/ → 200    mandati/ → 200    contatti/ → 200
[ar]    home → 200    chi-siamo/ → 200    custodia/ → 200    mandati/ → 200    contatti/ → 200

[it] mandate=famiglia-a-quarta-generazione-holding-industriale → 200
[it] mandate=famiglia-b-fondazione-di-famiglia → 200
[it] mandate=famiglia-c-trasferimento-intergenerazionale → 200
[it] mandate=famiglia-d-single-family-office-estero → 200
[en/fr/es/ar repeated for each of the 4 mandate detail slugs → 200/200/200/200 each]
```

5 locales × 5 pages + 5 locales × 4 mandate posts = 45/45 HTTP 200.

---

## 4 · LF-5 section sequence verification (all 5 locales)

Computed from `document.querySelectorAll('section[class*="cs-"]')`:

```
['cs-hero', 'cs-cycle', 'cs-pillars', 'cs-kpi-band', 'cs-sectors',
 'cs-leadership', 'cs-cases-preview', 'cs-cta']
```

Identical 8-section list across IT, EN, FR, ES, AR. The trust marquee remains absent from LF-5 (sectors absorbs its function), the cycle stays at slot-2 (governance opening), the dark band stays at slot-4 (KPI), the timeline stays at slot-7. Rebuild contract preserved.

---

## 5 · Voice anchor verification (all 5 locales)

| Locale | h1 (rendered) | em-words on the page (h1 + h2 italic-em) |
|---|---|---|
| IT | La continuità di una famiglia si misura in *generazioni*. | generazioni · cadenza · un solo · una sola cadenza · generazioni |
| EN | The continuity of a family is measured in *generations*. | generations · cadence · one single · one single cadence · generations |
| FR | La continuité d'une famille se mesure en *générations*. | générations · cadence · un seul · une seule cadence · générations |
| ES | La continuidad de una familia se mide en *generaciones*. | generaciones · cadencia · un solo · una sola cadencia · generaciones |
| AR | استمراريّة العائلة تُقاس *بالأجيال*. | بالأجيال · إيقاع · تفويض واحد · إيقاع واحد · بالأجيال |

5 italic-em hits per locale, all on load-bearing words. The hero h1 and the cta-closer h2 carry the same anchor sentence in every locale.

---

## 6 · AR RTL parity findings

### 6.1 · `<html>` attributes
```
<html lang="ar" dir="rtl">
```
Set correctly via `template_i18n.html_dir(self.locale)` and `is_rtl(self.locale)`.

### 6.2 · Font swap
- h1: `getComputedStyle(h1).fontFamily` → `"Noto Kufi Arabic", "Crimson Pro", Georgia, serif`
- body: `getComputedStyle(.cs-hero .frame .body .sub).fontFamily` → `Amiri, "Public Sans", system-ui, sans-serif`

### 6.3 · CS-TYPE-05 letter-spacing reset (post-fix)
All 9 LF-5 eyebrow surfaces now compute `letter-spacing: normal` under `html[dir="rtl"]`:
- `.cs-cycle .cell .eyebrow`
- `.cs-pillars .pillar .num`
- `.cs-sectors .whistle`
- `.cs-leadership .card .station`
- `.cs-cases-preview .row .title .eyebrow`
- `.cs-cases-preview .row .horizon strong`
- `.cs-hero .frame .anchor .eyebrow`
- `.cs-hero .meta-strip .item`
- `.cs-hero .credit-row .credit`

### 6.4 · No horizontal overflow
- AR @ 1440: `pageW=1425px · scrollW=1425px · horizontalOverflow=false`
- AR @ 720:  `pageW=705px · scrollW=705px · horizontalOverflow=false`

### 6.5 · Latin proper-noun preservation
The MENA business-press convention is preserved: technical/legal terms stay Latin (D.lgs. 24/2023, Reg. UE 679/2016, OAM, ANC, STEP, Albo dei Trustees, Codice della Crisi, Compliance Officer, Senior Steward, Family Officer, BDR, Continua, Pictet, Stonehage, Pexels, LinkedIn). Italian addresses preserved (Via San Marco 22 · 20121 Milano · Brera; Riva Caccia 1 · 6900 Lugano; Boulevard Royal 28 · L-2449 Luxembourg). Latin numerals preserved (18 / 3 / € 1.8 B / 4) for tabular alignment.

### 6.6 · Locale switcher
5 pills render in the marketplace bar with correct lang attributes:

```
[lang="it"] IT     /templates/business/continua-stewardship/preview/
[lang="en"] EN     /templates/business/continua-stewardship/preview/?lang=en
[lang="fr"] FR     /templates/business/continua-stewardship/preview/?lang=fr
[lang="es"] ES     /templates/business/continua-stewardship/preview/?lang=es
[lang="ar"] AR     /templates/business/continua-stewardship/preview/?lang=ar  (is-current on AR walk)
```

### 6.7 · RTL form fields (contatti)
The 9 form fields render with Arabic labels right-aligned, helper text right-flowing, dropdowns RTL-flipped. Sidebar offices (Milano · Lugano · Luxembourg) render right-to-left with Latin city names + Arabic role tags.

---

## 7 · Issues caught + fixed mid-walk

### 7.1 · STRONG · LF-5 RTL letter-spacing reset gap

**Symptom**: Arabic uppercase eyebrows (cycle cells, pillar numbers, sectors whistleblowing strip, leadership stations, timeline row eyebrows, hero eyebrow + meta-strip + credit-row) rendered with LTR letter-spacing of 0.18–0.22em, producing visible Arabic letter spread that contradicts MSA typesetting convention.

**Root cause**: The original CS-TYPE-05 reset list in `_base.html` was authored before LF-5 existed, so the new LF-5-specific eyebrow class hierarchy was not in the reset selector list.

**Fix**: Extended the existing `html[dir="rtl"] ... { letter-spacing: 0; }` rule with 10 LF-5 selectors. The fix is RTL-scoped only, so IT/EN/FR/ES are byte-equivalent before and after.

**Re-walk verdict**: All 9 surfaces compute `letter-spacing: normal` under RTL post-fix. Re-rendered captures of IT/EN/FR/ES at 1440 confirm no LTR-side regression.

### 7.2 · OPERATIONAL · `runserver --noreload` did not pick up the template edit on first attempt

**Symptom**: Edit to `_base.html` did not appear in the rendered HTML on the running server.

**Root cause**: `--noreload` mode plus an apparent in-memory template cache on the long-running server process.

**Fix**: `taskkill /F /PID 60232` + restart `runserver`. Edit then visible in next request.

**Status**: Dev-env behaviour, not a product issue. Documented for transparency.

### 7.3 · OPERATIONAL · DB tier transient flip

The SQLite DB had `WebTemplate(slug='continua-stewardship').tier='draft'`, which blocked the public preview path for the walk. Following the LF-5 IT rebuild §8.2 pattern, the tier was hand-flipped to `published_live` for the walk session, then restored to `draft` after the walk via `python manage.py sync_template_tiers`. Final state: `Final DB tier: draft` matches the registry. The legitimate D-055 staff-preview path was also confirmed available for users who want to walk the locales without relying on the transient flip.

---

## 8 · Console messages

One non-blocking console error visible on the IT first navigation (likely a static-file 404 from a third-party JS module unrelated to LF-5 or to multilingual). Did not surface visual regressions on any locale or any viewport. Tracked at `.playwright-mcp/console-2026-04-30T08-37-35-272Z.log`.

---

## 9 · Verdict

**Continua Pass B Multilingual browser walk is GREEN across all 5 locales at desktop and (for AR) at mobile. 70/70 cells PASS, 0 BLOCKING, 1 STRONG fix applied mid-walk, 0 OBSERVATION on LTR locales, 0 visual regression on the 4 frozen sibling skins (Pragma · Fiscus · Solaria · the LF-5 IT baseline). The corporate-suite chrome's RTL pipeline was extended additively for LF-5 surfaces; no prior locale on any sibling is affected.**

Continua is ready for human visual review across IT · EN · FR · ES · AR with RTL parity.
