# Browser-verifier · Continua Workflow D Release Decision · 2026-04-30

## 1 · Walk posture

- Server: `python manage.py runserver 127.0.0.1:8051 --noreload`
- Tier: `draft` in DB and registry · before, during, after the walk
- Auth: existing staff user `cs_review_fix` (`is_staff=True`)
- Tooling: Playwright MCP (Chromium · 1440×900 desktop · 720×1024 mobile RTL) + Django test Client (45-route smoke)
- Read-only: zero source code, content registry, JSON registry, template, or migration touched

The walk reproduces Pass B Multilingual's outcome on a fresh server, validates the legitimate D-055 staff-preview path, and confirms the anonymous tier gate. No new findings on the product.

## 2 · Walk cells

| Cell | IT | EN | FR | ES | AR | Source |
|---|---|---|---|---|---|---|
| HTTP 200 (home) staff session | PASS | PASS | PASS | PASS | PASS | smoke 45/45 |
| h1 voice anchor on equivalent TEMPORAL noun | PASS | PASS | PASS | PASS | PASS | live walk §3.1 |
| 5 italic-em hits (h1+cycle+pillars+cases+cta) | PASS | PASS | PASS | PASS | PASS | live walk §3.1 |
| LF-5 8-section sequence intact | PASS | PASS | PASS | PASS | PASS | live walk §2 |
| Body class `cs-lf-lf-5 lm-ready` | PASS | PASS | PASS | PASS | PASS | live walk §2 |
| Locale switcher 5 pills · current flagged | PASS | PASS | PASS | PASS | PASS | live walk §2 |
| `?lang=xx` propagation across nav | PASS | PASS | PASS | PASS | PASS | smoke 45/45 (each locale's nav routes 200) |
| `?preview=1` propagation across internal links | PASS | PASS | PASS | PASS | PASS | smoke 45/45 |
| No horizontal overflow @ 1440 | PASS | PASS | PASS | PASS | PASS | live walk §2 (1425=1425) |
| No horizontal overflow @ 720 (AR) | n/a | n/a | n/a | n/a | PASS | live walk §3.4 (705=705) |
| AR `<html dir="rtl" lang="ar">` | n/a | n/a | n/a | n/a | PASS | live walk §3.1 |
| AR Noto Kufi h1 + Amiri body | n/a | n/a | n/a | n/a | PASS | live walk §3.2 |
| AR letter-spacing normal on 9 LF-5 surfaces | n/a | n/a | n/a | n/a | PASS | live walk §3.3 |
| AR Latin proper-noun preservation | n/a | n/a | n/a | n/a | PASS | live walk §3.5 + ar-1440-firstscroll.png |
| Hero h1 AAA contrast on dark plate | PASS | PASS | PASS | PASS | PASS | live walk §5 (≈11–13:1) |
| KPI band cream-on-primary AAA | PASS | PASS | PASS | PASS | PASS | live walk §5 (11.03:1) |
| CTA dark-closer AAA | PASS | PASS | PASS | PASS | PASS | live walk §5 (11.03:1) |
| Nav cream-on-primary AAA | PASS | PASS | PASS | PASS | PASS | live walk §5 (11.03:1) |

**Cell pass count: 18 cells × 5 locales (effective, AR-only cells counted once) = 70 cells. 70 / 70 PASS.** Identical to Pass B Multilingual's 70/70 result, on a fresh server.

## 3 · Anonymous tier-gate probes

```
GET /templates/business/                                       anon → 200 (catalog list)
   slug "continua-stewardship" in HTML                                        ABSENT
GET /templates/business/continua-stewardship/preview/          anon → 404
GET /templates/business/continua-stewardship/preview/?preview=1 anon → 404
```

The D-055 tier gate excludes Continua from the anonymous catalog and rejects the preview flag without a staff session. The legitimate review path is staff-session + `?preview=1`, which is exactly what was hardened in `continua-pass1-review-lock` and surfaced again here.

## 4 · 45-route smoke (staff session)

The Django test Client probe (`_smoke.py`):

```
LOCALES = ['it','en','fr','es','ar']
PAGES   = ['', 'chi-siamo/', 'custodia/', 'mandati/', 'contatti/']  (5 pages)
MANDATES = 4 detail-post slugs

5 × 5 (pages) + 5 × 4 (mandate posts) = 45 routes
Result: 45 / 45 → 200
```

Zero 404 on internal routes. Zero 500 on any locale.

## 5 · Frozen-sibling sanity

This walk does NOT re-measure Pragma · Fiscus · Solaria. The corporate-suite layout regression walk (`corporate-suite-layout-regression-walk.md §3`) filed 0 px wireframe drift on those three siblings, and no edits to LF-1/LF-3/LF-4 paths have landed since. Frozen-sibling regression evidence remains valid at the workflow-D commit.

## 6 · Console output

No console errors at first paint on IT or AR home. Pass B's static-file 404 console note is unrelated to LF-5 / multilingual / RTL and does not reproduce here.

## 7 · Stop-conditions checklist (per `corporate-suite-browser-rubric.md`)

- [x] Page returns 200 with staff `?preview=1`
- [x] Body class carries `cs-lf-{family}` + `lm-ready`
- [x] Reveal animations advance into `lm-in` (no permanently-hidden sections)
- [x] One dark band per home (KPI band slot-4 + dark CTA closer)
- [x] Whistleblowing surface where required (sectors-band eyebrow + footer column)
- [x] Pexels-only imagery, all reachable
- [x] Console errors at first paint = 0
- [x] No horizontal scrollbar at any rubric viewport
- [x] Hero AAA contrast on h1
- [x] Locale switcher functional and current flagged
- [x] `?preview=1` propagation across internal hrefs
- [x] `?lang=xx` propagation across internal hrefs
- [x] AR RTL with proper Arabic typography swap
- [x] AR letter-spacing normal on uppercase eyebrow surfaces
- [x] No editor affordance on `/preview/` route

15 / 15 cleared.

## 8 · Issues found

**0 BLOCKING · 0 STRONG · 0 OBSERVATION new on the product.**

Operational note (not a finding): the dev-environment `runserver` requires a port outside the OS-blocked range (`8061` and `8073` were rejected by Windows port permissions; `8051` was used). This is a Windows port-permission detail, not a product issue.

## 9 · Verdict

**GREEN.** The walk side of the gatekeeper handshake is complete. The Continua live render reproduces all of Pass B Multilingual's gates, the LF-5 IT rebuild's frozen-sibling discipline, and the review-lock's tier-gate behaviour. The user side of the handshake (parallel verification + explicit confirmation per SOP §5.4) is the only piece pending. Server is left running for the user-handshake walk.
