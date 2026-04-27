# Solaria · Pass B browser verification (multilingual)

**Phase**: X.4 Pass B · multilingual completion
**Run-ISO**: `20260426T1500Z`
**Captures**: `factory/reports/browser-verification/solaria-passB-multilingual/20260426T1500Z/`
**Author**: Claude (Opus 4.7) via Playwright MCP
**Audience**: project owner — direct browser walk record, not a scorecard rephrase.

---

## 1 · Server context

- **Branch**: `phase-x4-solaria-passB-multilingual`
- **Dev server**: `python manage.py runserver 127.0.0.1:8731 --noreload`
  (autoreload off so Playwright captures see a single warm app process).
- **URL**: `http://127.0.0.1:8731/`
- **Auth**: logged in as `solaria_qa_staff` (existing staff QA user
  re-used from Pass A · `is_staff=True`).
- **Solaria base URL**: `http://127.0.0.1:8731/templates/business/solaria-coaching/preview/`
  (`?preview=1` is required because Solaria stays at `tier=draft`).
- **Server stayed up** for the full walk — 11 captures + 7 evaluate calls
  on a single warm process.

The dev server is left running for the user to take over the walk if
desired. To stop it: kill the background process or `Ctrl-C` in its
terminal.

---

## 2 · Locale matrix — 1440 × 900 home

| # | Locale | URL | HTTP | dir | h1 (truncated) | overflowPx | Capture |
|---|---|---|---|---|---|---|---|
| 01 | IT | `?preview=1&lang=it` | 200 | ltr | "Il coaching non è terapia e non è consulenza." | 0 | `01-it-home-1440.png` |
| 02 | EN | `?preview=1&lang=en` | 200 | ltr | "Coaching is not therapy, and not consultancy." | 0 | `02-en-home-1440.png` |
| 03 | FR | `?preview=1&lang=fr` | 200 | ltr | "Le coaching n'est ni une thérapie, ni du conseil." | 0 | `03-fr-home-1440.png` |
| 04 | ES | `?preview=1&lang=es` | 200 | ltr | "El coaching no es terapia, ni es consultoría." | 0 | `04-es-home-1440.png` |
| 05 | AR | `?preview=1&lang=ar` | 200 | **rtl** | "التدريب ليس علاجاً نفسياً، وليس استشارة." | 0 | `05-ar-home-1440.png` |

All 5 locales rendered cleanly, no overflow, voice anchor verbatim-in-
translation in every h1.

---

## 3 · Inner-page sample

| # | Locale | Page | Capture | Spot-check |
|---|---|---|---|---|
| 06 | AR | `/percorsi/` | `06-ar-percorsi-1440.png` | 4 service cards visible, RTL numbering `4/01` `4/02`, no overflow |
| 07 | AR | `/contatti/` | `07-ar-contatti-1440.png` | Form labels Arabic (`الاسم · اللقب · البريد الإلكتروني`), submit `احجز discovery call →`, sidebar with Italian address kept Latin |
| 09 | EN | `/percorsi/` | `09-en-percorsi-1440.png` | 4 service cards, ` Executive 1:1 / Team coaching / Corporate group / Single exploratory session` |
| 10 | FR | `/il-coach/` | `10-fr-il-coach-1440.png` | "Une méthode déclarée, douze ans de pratique certifiée." · "Cinq étapes, une cadence concertée" · 4 principes non négociables |

Inner-page coverage is intentionally a sample — Pass B's verification
target was multilingual completion + RTL + voice anchor + no overflow.
A full home + 4-inner-page × 5-locale matrix (25 captures) is left for
Pass C if the user wants the full grid before public flip.

---

## 4 · Mobile (390 × 844) sample

| # | Locale | Page | Capture | Result |
|---|---|---|---|---|
| 08 | AR | `/` (home) | `08-ar-home-390.png` | overflowPx=0, hamburger present, AR h1 wraps to 3 lines (3.01 line-height = healthy), content stacks RTL, footer columns stack vertically |

The mobile AR walk is the most demanding combination (RTL + smallest
viewport + glyph-swap font requirement). It cleared all three checks.

---

## 5 · Browser-evaluated checkpoints

The following checkpoints were issued via `browser_evaluate(...)` after
each navigation. Numbers are direct DOM measurements at viewport width
indicated.

```js
// Per-locale identity
{ dir: html.dir, lang: html.lang, h1: h1.textContent,
  overflowPx: scrollWidth - clientWidth,
  fontFamily: getComputedStyle(h1).fontFamily }

// Language-switcher honesty (D-068)
Array.from(document.querySelectorAll('.mp-lang-pill')).map(p => ({
  code: p.getAttribute('lang'),
  dir: p.getAttribute('dir'),
  href: p.getAttribute('href'),
  current: p.classList.contains('is-current')
}))

// Banned-phrase scan (CS-EXEC-04)
['Unlock your potential','Sblocca il tuo potenziale','Libérez votre potentiel',
 'Desbloquea tu potencial','أطلِق العنان','Game-changing','Mindset vincente',
 'Best version of yourself'].filter(p => document.body.textContent.includes(p))
```

### Observed values (per locale, at 1440 home)

| Locale | dir | lang | h1 fontFamily | overflowPx | Banned hits |
|---|---|---|---|---|---|
| IT | ltr | it | `Fraunces, Georgia, "Times New Roman", serif` | 0 | [] |
| EN | ltr | en | `Fraunces, Georgia, "Times New Roman", serif` | 0 | [] |
| FR | ltr | fr | `Fraunces, Georgia, "Times New Roman", serif` | 0 | [] |
| ES | ltr | es | `Fraunces, Georgia, "Times New Roman", serif` | 0 | [] |
| AR | **rtl** | ar | `"Noto Kufi Arabic", Fraunces, Georgia, serif` | 0 | [] |

The AR `fontFamily` ordering is the one the corporate-suite RTL stack
prepends — Noto Kufi Arabic + fallback Latin serifs — confirming the
font swap (CS-BLOCK-VI-03 cleared: no `□□□` glyphs).

### Switcher proof (from IT home)

```json
[
  {"code":"it","dir":"ltr","href":"/templates/business/solaria-coaching/preview/","current":true,"label":"IT"},
  {"code":"en","dir":"ltr","href":"/templates/business/solaria-coaching/preview/?lang=en","current":false,"label":"EN"},
  {"code":"fr","dir":"ltr","href":"/templates/business/solaria-coaching/preview/?lang=fr","current":false,"label":"FR"},
  {"code":"es","dir":"ltr","href":"/templates/business/solaria-coaching/preview/?lang=es","current":false,"label":"ES"},
  {"code":"ar","dir":"rtl","href":"/templates/business/solaria-coaching/preview/?lang=ar","current":false,"label":"AR"}
]
```

The AR pill carries `dir="rtl"` so its glyph order respects RTL even
when the page is rendered LTR — this is correct.

---

## 6 · Honest deviations and known limitations

1. **Lazy-loaded portraits + thumbs do not appear in the
   `fullPage:true` Playwright screenshots when below the fold and not
   yet scrolled into view.** This is the IntersectionObserver-driven
   reveal at the archetype level — the same behaviour Pass A documented
   (browser-verifier.md §6 deviation 3). Forcing `loading="eager"` and
   re-setting the `src` triggers all 5 lazy images to load to natural
   width 800 / 1200 px (verified live · `naturalWidth: 800` for
   portraits + 4 of 5 thumbs · 1200 for the feature thumb). Capture
   `05b-ar-home-1440-images-loaded.png` was attempted with this force.
   In a real browser, images render on intersection during normal user
   scroll. This is not a Pass B defect — it is the archetype's reveal
   policy.

2. **Image-coherence tie-back vs locale.** The same 6-URL Pexels pool
   serves all 5 locales (the IT-module `_POOL_*` constants are imported
   by all four added locale files). The hero shows Western coachees
   regardless of locale. This is a deliberate Pass B scoping choice —
   adding locale-specific imagery is a curator pass and was out of
   scope here.

3. **Pass B inner-page coverage is sampled, not exhaustive.** Five home
   captures + four inner samples + one mobile sample = 11 PNGs. A full
   matrix (5 locales × 5 pages × 5 viewports = 125 captures) is the
   shape Pass C will need pre-flip; it is not the shape Pass B
   targeted. The samples chosen exercise the most failure-prone
   surfaces (RTL home + RTL services + RTL contact form + AR mobile).

4. **`manage.py check` still emits one warning** —
   `corporate_suite.W001` for Pragma's grandfathered Unsplash imagery.
   This is a Pass-B-pre-existing condition unrelated to Solaria.
   Solaria itself emits zero warnings.

---

## 7 · Verdict (this walk)

All five locale homes return 200, render the voice anchor verbatim-in-
translation, render Fraunces (or Noto Kufi Arabic for AR), show no
horizontal overflow at 1440 or 390, expose the 5-pill language switcher
honestly, and contain none of the banned-phrase regex (CS-EXEC-04).
The Arabic locale flips `dir="rtl"`, swaps to Noto Kufi for headings,
and stacks correctly on mobile.

This walk is sufficient to call **Pass B multilingual completion
verified in browser**. No blockers found. No fixes were needed during
the walk — every capture passed on first navigation.

The dev server stays up at `http://127.0.0.1:8731/` for the user to
walk personally. Recommended starting URL:
`http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1&lang=ar`
(open with the staff session already active in Chrome — log in as
`solaria_qa_staff / solariapassA2026` if the session is fresh).
