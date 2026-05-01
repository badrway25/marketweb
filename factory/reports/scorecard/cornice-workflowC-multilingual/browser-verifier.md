# Browser verifier · Cornice · workflow C multilingual

```yaml
phase:        X.5 Cornice · workflow C
date:         2026-05-01
browser:      Playwright MCP (Chromium engine)
server:       http://127.0.0.1:8052/ (runserver --noreload)
auth:         cornice_review · staff · superuser · ?preview=1
verdict:      PASS · 5-locale walk · 0 review-blocking
```

This panel is a delta-only summary; full walk evidence + DOM probes
live in `factory/reports/browser-verification/cornice-workflowC-multilingual.md`.

## §1 · Probe matrix

| Locale | Home @ 1440 | Inner page walked | Viewport extras | h1 verbatim | LF-2 cream nav active | Body class `cs-lf-lf-2` | Voice anchor verbatim recurrence (h1 + CTA) |
|---|---|---|---|---|---|---|---|
| IT | YES | (A.6 baseline) | — | YES | YES | YES | YES |
| EN | YES | case-detail biblioteca-pietrasanta | — | YES | YES | YES | YES |
| FR | YES | contatti (form labels + consent + footer) | — | YES | YES | YES | YES |
| ES | YES | progetti (list page · trailing CTA) | — | YES | YES | YES | YES |
| AR | YES | studio (about · history · team · footer) | 880 + 480 | YES | YES (cream RGB unchanged at LTR ratio) | YES | YES |

## §2 · AR-specific probes

| Probe | Expected | Live value |
|---|---|---|
| `<html dir>` | "rtl" | "rtl" PASS |
| `<html lang>` | "ar" | "ar" PASS |
| `<body class>` includes `cs-lf-lf-2` | yes | yes PASS |
| Computed `--heading` resolves to | first family `Noto Naskh Arabic` (LF-2 scope · NOT `Noto Kufi Arabic`) | `"Noto Naskh Arabic", "Cormorant Garamond", Georgia, serif` PASS |
| Computed `--body` resolves to | first family `Amiri` | `Amiri, "Source Sans 3", system-ui, sans-serif` PASS |
| Nav background colour | LF-2 cream `rgb(238, 240, 243)` | `rgb(238, 240, 243)` PASS |
| Voice anchor verbatim h1 | `كلّ مشروع <em>حُجَّة</em> مبنيّة، لا خدمة مُسداة.` | exact match PASS |
| Voice anchor verbatim CTA closer | same as h1 | exact match PASS |
| Hero side-quote em-noun | derived from `حُجَّة` (verb form `تُحاجَج`) | exact match PASS |
| Leadership h2 | `Marta <em>Roveri</em>` (Latin script preserved · CS-NAV-06) | exact match PASS |
| 4 magazine card h3 em-words | هندسة · قطعة · حُجَّة · الثانويّة | 4/4 PASS |

## §3 · Frozen-sibling probe (delta from A.6 baseline)

```
Anonymous HTTP across 5 locales × 4 frozen siblings = 20 routes:
all 200.

Continua AR specifically:
  body.className     = "cs-lf-lf-5 lm-ready"   [LF-5 · NOT lf-2]
  h1.fontFamily      = '"Noto Kufi Arabic", "Crimson Pro", Georgia, serif'
  h1.innerHTML       = "استمراريّة العائلة تُقاس <em>بالأجيال</em>."
  → Cluster default Kufi preserved. NO Naskh leakage from the LF-2
    override (which is selector-scoped to body.cs-lf-lf-2).

Pragma IT specifically:
  nav.bg             = rgb(30, 41, 59)         [navy · LF-1]
  h1.innerHTML       = "Dove si prendono le decisioni <em>che contano</em>."
  → LF-1 chrome unchanged · h1 verbatim.
```

## §4 · Test suite delta

```
Before workflow C (A.6 review-lock):  545 passed, 1 failed (booking-flag)
After workflow C (this run):          545 passed, 1 failed (same booking-flag)

Δ regression:                         0
Δ new failures:                       0
```

## §5 · Verdict

**PASS.** No review-blocking, chrome-consistency, or editorial-rhythm
issues surfaced during the 5-locale walk. The Naskh heading swap
applies cleanly to LF-2 only. Frozen siblings show 0/4 regression.
Test suite holds at 545/546 (same pre-existing failure).
