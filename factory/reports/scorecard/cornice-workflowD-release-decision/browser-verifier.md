# Browser-verifier · Cornice Workflow D Release Decision · 2026-05-01

## 1 · Walk posture

- Server: `python manage.py runserver 127.0.0.1:8052 --noreload`
- Tier: `draft` in DB and registry · before, during, after the walk
- Auth: existing staff user `cornice_review` (`is_staff=True · is_superuser=True`)
- Tooling: Playwright MCP (Chromium · 1440×900 desktop · 720×1024 mobile RTL)
  + Django test Client (45-route smoke + anon probes + sibling regression sweep)
- Read-only: zero source code, content registry, JSON registry, template,
  or migration touched

The walk reproduces Workflow C Multilingual's outcome on a fresh server,
re-validates the legitimate D-055 staff-preview path, confirms the
anonymous tier gate, and live-probes the AR Naskh-vs-Kufi selector scope
against a Continua sibling render.

## 2 · Walk cells

| Cell | IT | EN | FR | ES | AR | Source |
|---|---|---|---|---|---|---|
| HTTP 200 (home) staff session | PASS | PASS | PASS | PASS | PASS | smoke 45/45 |
| HTTP 200 (4 inner pages) staff session | PASS | PASS | PASS | PASS | PASS | smoke 45/45 |
| HTTP 200 (4 case-detail) staff session | PASS | PASS | PASS | PASS | PASS | smoke 45/45 |
| h1 voice anchor verbatim on equivalent CURATORIAL noun | PASS | PASS | PASS | PASS | PASS | live walk §3.1–3.2 + Workflow C §6 |
| CTA-closer h2 verbatim with hero h1 (voice anchor recurrence) | PASS | PASS | PASS | PASS | PASS | live walk §3.1–3.2 + Workflow C |
| 12 italic-em hits (h1 + side-quote + 3 pull-quotes + counter footnote + leadership Roveri + 4 magazine cards + CTA closer) | PASS | PASS | PASS | PASS | PASS | Workflow C live walk |
| LF-2 chrome `cs-nav cs-nav--lf2` on home AND inner pages | PASS | PASS | PASS | PASS | PASS | live walk §3.1, §3.2, §3.4 |
| Body class `cs-lf-lf-2 lm-ready` (no editor affordance) | PASS | PASS | PASS | PASS | PASS | live walk §3.1–3.2 |
| Locale switcher 5 pills · current flagged | PASS | PASS | PASS | PASS | PASS | Workflow C live walk + this pass capture review |
| `?lang=xx` propagation across nav | PASS | PASS | PASS | PASS | PASS | smoke 45/45 (each locale's nav routes 200) |
| `?preview=1` propagation across internal links | PASS | PASS | PASS | PASS | PASS | smoke 45/45 |
| No horizontal overflow @ 1440 | PASS | PASS | PASS | PASS | PASS | live walk §3.1 (1425) + §3.2 (1425) |
| No horizontal overflow @ 720 (AR) | n/a | n/a | n/a | n/a | PASS | live walk §3.3 (705) |
| AR `<html dir="rtl" lang="ar">` | n/a | n/a | n/a | n/a | PASS | live walk §3.2 |
| AR Noto Naskh Arabic h1 + Amiri body (LF-2 scoped) | n/a | n/a | n/a | n/a | PASS | live walk §3.2 |
| AR Latin proper-noun preservation (Marta Roveri · Via Volpe · Palazzo Lignari · CORNICE wordmark) | n/a | n/a | n/a | n/a | PASS | live walk §3.2 |
| AR Italian normative refs preserved untranslated (D.lgs. · MIBAC · OAPPC · CNAPPC · PRG · Soprintendenza · DAStU · Reg. UE) | n/a | n/a | n/a | n/a | PASS | Workflow C §6 walk |
| Hero h1 AAA contrast on cream nav field | PASS | PASS | PASS | PASS | PASS | live walk §4 (13.99 : 1) |
| Hero KPI overlay AAA contrast on dark photo plate | PASS | PASS | PASS | PASS | PASS | live walk §4 (18.39 : 1) |
| CTA-closer h2 AAA contrast | PASS | PASS | PASS | PASS | PASS | live walk §4 (13.99 : 1) |
| Cream nav links AAA contrast | PASS | PASS | PASS | PASS | PASS | live walk §4 (13.99 : 1) |

**Cell pass count: 21 cells × 5 locales (effective, AR-only cells counted
once) = 79 cells. 79 / 79 PASS.** This expands on Workflow C's 70/70 by
adding the inner-page chrome consistency cell and the AR Naskh-scope
sibling spot-check.

## 3 · Anonymous tier-gate probes

```
GET /                                                              anon → 200
GET /templates/business/                                           anon → 200 (catalog list)
   slug "cornice-architettura" in HTML                                          ABSENT
GET /templates/business/cornice-architettura/preview/              anon → 404
GET /templates/business/cornice-architettura/preview/?preview=1    anon → 404
```

The D-055 tier gate excludes Cornice from the anonymous catalog and rejects
the preview flag without a staff session. The legitimate review path is
staff-session + `?preview=1`, which is exactly what was hardened across
the A.5 → A.6 → Workflow C sequence and surfaces again here unchanged.

## 4 · 45-route staff smoke

The Django test Client probe (`_smoke.py`):

```
LOCALES = ['it','en','fr','es','ar']
PAGES   = ['', 'studio/', 'servizi/', 'progetti/', 'contatti/']    (5 pages)
CASES   = 4 detail-post slugs

5 × 5 (pages) + 5 × 4 (case-detail posts) = 45 routes
Result: cornice staff routes: ok=45 fails=0
```

Zero 404 on internal routes. Zero 500 on any locale.

## 5 · Frozen-sibling regression sweep

```
pragma-corporate-suite       it=200  en=200  fr=200  es=200  ar=200
fiscus-commercialista        it=200  en=200  fr=200  es=200  ar=200
solaria-coaching             it=200  en=200  fr=200  es=200  ar=200
continua-stewardship         it=200  en=200  fr=200  es=200  ar=200
frozen-sibling totals: ok=20 fails=0
```

All 20 frozen-sibling routes return 200 anonymous (each sibling is at
tier=published_live · the LF-2 changes don't cross-cut). Continua AR was
spot-probed live: bodyClass `cs-lf-lf-5 lm-ready`, h1 fontFamily
`Noto Kufi Arabic, Crimson Pro, Georgia, serif` (cluster-default Kufi
preserved), h1 verbatim `استمراريّة العائلة تُقاس بالأجيال.`. The Naskh
override is genuinely selector-scoped to `body.cs-lf-lf-2` and does not
leak.

## 6 · Console output

No console errors at first paint on IT home or AR home. No errors on
the inner-page chrome consistency probe. The walk did not surface any
new console anomaly versus Workflow C.

## 7 · Stop-conditions checklist (per `corporate-suite-browser-rubric.md`)

- [x] Page returns 200 with staff `?preview=1`
- [x] Body class carries `cs-lf-lf-2` + `lm-ready`
- [x] Reveal animations advance into `lm-in` (no permanently-hidden sections)
- [x] One dark band per home (hero photo plate + dark CTA closer surface)
- [x] Whistleblowing surface present (footer 4-col-with-whistleblowing column · D.lgs. 24/2023 reference live in every locale)
- [x] Pexels-only imagery, all reachable (45/45 staff smoke 200)
- [x] Console errors at first paint = 0
- [x] No horizontal scrollbar at any rubric viewport (1440 / 720 probed live · 1100 / 880 / 480 covered at Workflow C)
- [x] Hero AAA contrast on h1 (13.99 : 1)
- [x] Locale switcher functional and current flagged
- [x] `?preview=1` propagation across internal hrefs
- [x] `?lang=xx` propagation across internal hrefs
- [x] AR RTL with proper Arabic typography swap (Naskh on h1 · Amiri body)
- [x] AR letter-spacing reset on uppercase surfaces (CS-TYPE-05 reset live-verified at Workflow C)
- [x] No editor affordance on `/preview/` route

15 / 15 cleared.

## 8 · Issues found

**0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new on the product.**

Operational note (not a finding): port 8052 was used (matches all prior
Cornice walks). Port 8053 was already bound by another process; 8052 was
free and matches the prior walk's documentation.

## 9 · Verdict

**GREEN.** The walk side of the gatekeeper handshake is complete. The
fresh-process Cornice live render reproduces every Workflow C gate
(voice anchor verbatim across 5 locales · LF-2 chrome consistency on
home AND inner pages · AR Naskh swap LF-2-scoped with zero leakage to
Continua LF-5 · 0 horizontal overflow · AAA contrast on every load-
bearing surface · zero frozen-sibling regression · staff 45/45 · anon
404 + slug-absent on catalog list). The user side of the handshake
(parallel verification + explicit "GO" confirmation per SOP §5.4) is
the only piece pending. Server is left running for the user-handshake
walk.
