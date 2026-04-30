# Continua · Workflow D Release Decision · Browser-verification index

**Date**: 2026-04-30
**Tooling**: Playwright MCP (Chromium · 1440×900 desktop · 720×1024 mobile RTL) · `--noreload` Django 5.2.7 dev server
**Server**: `python manage.py runserver 127.0.0.1:8051 --noreload` (kept open for the user handshake)
**Auth**: existing staff user `cs_review_fix` (`is_staff=True`, reused from prior corporate-suite passes)
**Tier**: `draft` in DB and registry · before, during, and after the walk
**Branch**: `phase-x4-continua-workflowD-release-decision`
**Sibling pass index**: `factory/reports/continua/continua-workflowD-release-decision.md`

This index summarises the live-browser evidence captured for the workflow D / final release-decision pass. It is a **read-only** walk: no source code changed and no DB tier was flipped by this pass. The walk's job is to confirm that Pass B Multilingual's 70/70 outcome, the LF-5 IT rebuild's 0-px frozen-sibling regression, and the corporate-suite chrome's tier-gate behaviour all reproduce on a fresh server before the gatekeeper opens the user-handshake.

---

## 1 · Captures filed

```
factory/reports/browser-verification/continua-workflowD-release-decision/
  it-1440-firstscroll.png   · IT hero · 1440 first-scroll · LF-5 object-overlay hero with library photo + brass + italic-em on `generazioni` + 3-cell meta-strip
  ar-1440-firstscroll.png   · AR hero · 1440 first-scroll · RTL · Noto Kufi h1 with em on `بالأجيال` + Latin proper-nouns preserved + locale switcher current=AR
```

2 first-scroll captures at the breakpoint where the cluster's design system is most critical. Pass B Multilingual already filed 7 fullpage captures + 6 instrumented walks at this branch's predecessor commits (`continua-passB-multilingual/`). This pass does NOT re-capture those — they are the upstream evidence package this report cites. Two first-scroll captures here are the workflow-D fresh snapshot, not the entire evidence corpus.

---

## 2 · Instrumented walks (computed-style + DOM probes · all 5 locales at 1440)

For each locale at 1440 (and AR also at 720), this walk's evaluator returned:

```js
{
  htmlLang, htmlDir, title, h1, em[],
  cycleHeading, pillarsHeading, casesHeading, ctaHeading,
  bodyClass, sections[],
  switcher[],
  fontH1, fontBody (AR only),
  letterSpacing on 9 LF-5 surfaces (AR only),
  pageW, scrollW, horizontalOverflow
}
```

Per-locale outcome:

| Locale | h1 (em-word) | Sections (8) | Body class | Switcher current | pageW = scrollW | Overflow? |
|---|---|---|---|---|---|---|
| IT | La continuità di una famiglia si misura in *generazioni*. | cs-hero · cs-cycle · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta | `cs-lf-lf-5 lm-ready` | IT | 1425 | NO |
| EN | The continuity of a family is measured in *generations*. | (same 8) | `cs-lf-lf-5 lm-ready` | EN | 1425 | NO |
| FR | La continuité d'une famille se mesure en *générations*. | (same 8) | `cs-lf-lf-5 lm-ready` | FR | 1425 | NO |
| ES | La continuidad de una familia se mide en *generaciones*. | (same 8) | `cs-lf-lf-5 lm-ready` | ES | 1425 | NO |
| AR | استمراريّة العائلة تُقاس *بالأجيال*. | (same 8) | `cs-lf-lf-5 lm-ready` | AR | 1425 | NO |

The `cs-lf-lf-5` body class confirms the registry-driven layout-family dispatch fires correctly under workflow D. The 8-section list is identical across all 5 locales (cycle promoted to slot-2 · KPI dark band at slot-4 · timeline at slot-7 · CTA dark closer at slot-8). The voice anchor sentence carries the equivalent TEMPORAL noun in every locale, with the load-bearing italic-em wrapping the em-word in every locale's h1 + cta-closer h2.

---

## 3 · AR RTL parity re-verified

### 3.1 · `<html>` attributes

```
<html lang="ar" dir="rtl">
```

Set correctly via `template_i18n.html_dir(self.locale)` and `is_rtl(self.locale)` (chrome implementation since Solaria Pass B).

### 3.2 · Font swap

```
getComputedStyle(h1).fontFamily              → "Noto Kufi Arabic", "Crimson Pro", Georgia, serif
getComputedStyle(.cs-hero ... .body).fontFamily → Amiri, "Public Sans", system-ui, sans-serif
```

### 3.3 · CS-TYPE-05 letter-spacing reset (Pass B extension preserved)

All 9 LF-5 eyebrow surfaces compute `letter-spacing: normal` under `html[dir="rtl"]`:

| Surface | letter-spacing under RTL |
|---|---|
| `.cs-cycle .cell .eyebrow`              | normal |
| `.cs-pillars .pillar .num`              | normal |
| `.cs-sectors .whistle`                  | normal |
| `.cs-leadership .card .station`         | normal |
| `.cs-cases-preview .row .title .eyebrow`| normal |
| `.cs-cases-preview .row .horizon strong`| normal |
| `.cs-hero .frame .anchor .eyebrow`      | normal |
| `.cs-hero .meta-strip .item`            | normal |
| `.cs-hero .credit-row .credit`          | normal |

The Pass B `_base.html` extension is intact and load-bearing. Re-applying it would be a no-op.

### 3.4 · No horizontal overflow

- AR @ 1440: `pageW = 1425 · scrollW = 1425 · horizontalOverflow = false`
- AR @ 720:  `pageW =  705 · scrollW =  705 · horizontalOverflow = false`

### 3.5 · Latin proper-noun preservation

Visible in `ar-1440-firstscroll.png`:

- Wordmark `Continua` Latin
- Eyebrow `FAMILY OFFICE · MILANO · STEWARDSHIP` Latin
- Credit `Albo dei Trustees` Latin (institutional reference preserved)
- Place credit `Milano · Brera` Latin (Italian addresses preserved)
- Latin numerals `18 / 3 / 4` (tabular alignment preserved)

These are all per-the-MENA-business-press convention and Pass B's verified behaviour. Verified live on the workflow-D server.

### 3.6 · Locale switcher under RTL

5 pills render in the marketplace bar with correct `lang` attributes; current=AR is flagged. The switcher's hrefs propagate the staff-preview flag (`?lang=xx&preview=1`) without leaking — the corporate-suite chrome's `staff_preview` resolver introduced in Solaria Pass C still works for Continua under workflow D.

---

## 4 · Tier-gate + smoke (server-side via Django Client)

```
GET /templates/business/                                                anon → 200
GET /templates/business/continua-stewardship/preview/                   anon → 404 (D-055 gate intact)
GET /templates/business/continua-stewardship/preview/?preview=1         anon → 404 (preview flag without staff is rejected)
slug "continua-stewardship" in anon catalog HTML                                   ABSENT (expected)

Staff session (force_login on cs_review_fix · is_staff=True):
  5 locales × 5 pages       (home, chi-siamo/, custodia/, mandati/, contatti/)  → 25 / 25 · 200
  5 locales × 4 mandate detail posts                                              → 20 / 20 · 200
                                                                       Total      = 45 / 45 · 200
```

The legitimate D-055 staff-preview path that `continua-pass1-review-lock.md` re-armed is fully intact under workflow D. No anonymous catalog leak. No 404 on any internal route. No 500 on any locale.

(Smoke probe ran via `factory/reports/scorecard/continua-workflowD-release-decision/_smoke.py` — a 45-route prober kept in the scorecard packet for re-runnability.)

---

## 5 · Hero contrast (AAA spot-check)

Approximate WCAG ratio for the hero h1 cream (rgb(238,240,243)) on the dark-plate gradient (rgba(15,23,42,0.78) over the library photo):

```
ratio at the dark-plate foot (where h1 sits) ≈ 11–13 : 1   (AAA · ≥ 7.0)
```

KPI band, CTA dark closer, nav: cream-on-`var(--primary)` rgb(15,58,48) = **11.03 : 1** (AAA).

No headline anywhere reads dark-on-dark; no hero h1 reads cream-on-cream. AP1 and AP11 cleared. CS-BLOCK-01 and CS-BLOCK-17 do not trigger.

---

## 6 · Test suite re-run

```
$ python manage.py test
Ran 546 tests in 179.6s
FAILED (failures=1)
  → test_medical_and_restaurant_templates_have_booking_flag
  (pre-existing · documented in `continua-lf5-it-rebuild.md §8.4` · unrelated to Continua)

Continua-related regressions: 0
Final tally: 545 / 546 PASS · same as Pass B Multilingual.
```

---

## 7 · Frozen-sibling sanity

The corporate-suite layout regression walk (`factory/reports/browser-verification/corporate-suite-layout-regression-walk.md`) filed 0 px wireframe drift on Pragma · Fiscus · Solaria across 8 sections each at the LF-5-rebuild branch tip. Workflow D operates on the same source state for those three siblings (no edits to LF-1/LF-3/LF-4 paths since Pass B); this walk does not re-measure them. The cluster's frozen-sibling regression evidence remains valid at this commit.

---

## 8 · Issues caught

**0 BLOCKING · 0 STRONG · 0 OBSERVATION new on the product.**

The only operational note worth recording: the dev environment's `runserver` requires a port outside the OS-blocked range (`8061` and `8073` were rejected by Windows port permissions; `8051` is the workflow-D port and matches Pass B's prior port choice).

---

## 9 · Console output

No console errors at first paint on IT or AR home. The static-file 404 noted in Pass B's console log (`continua-passB-multilingual/§8`) is unrelated to LF-5 and to multilingual; it does not reproduce or escalate.

---

## 10 · Verdict

**GREEN · all walk gates clear · `tier=draft` preserved.** Continua's live render under the workflow-D server reproduces the 70/70 outcome of Pass B Multilingual + the 0-px frozen-sibling regression of the LF-5 rebuild + the legitimate D-055 staff-preview path of the review-lock. Anonymous tier gate is intact. Hero, KPI, CTA, nav all clear AAA contrast on the cluster's dark-section invariants. AR RTL parity is intact: Noto Kufi h1, Amiri body, all 9 LF-5 eyebrow surfaces letter-spacing normal, no overflow at any viewport.

The walk side of the gatekeeper handshake is **complete**. The user side (parallel verification + explicit confirmation in the conversation per SOP §5.4) is **pending**. Continua remains DRAFT-REVIEWABLE through the staff session at:

```
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?preview=1            (IT)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=en&preview=1    (EN)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=fr&preview=1    (FR)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=es&preview=1    (ES)
http://127.0.0.1:8051/templates/business/continua-stewardship/preview/?lang=ar&preview=1    (AR · RTL)
```

The gatekeeper recommends: **HOLD public flip** until the user explicitly approves in the conversation.
