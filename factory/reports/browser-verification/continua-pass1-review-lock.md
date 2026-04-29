# Continua · Pass 1.5 Review-Lock · Browser-verification index

**Date**: 2026-04-29
**Walk artefact root**: `factory/reports/browser-verification/continua-pass1-review-lock/`
**Scorecard packet**: `factory/reports/scorecard/continua-pass1-review-lock/`
**Tool**: Playwright MCP (live · staff session)

The walk for this pass is narrow by design — it verifies one thing and one thing only: **after the DB-side `tier` was synced back to `draft`, the legitimate D-055 staff-preview path still reaches the page and the anonymous tier gate still rejects.** The visual / scorecard / contrast / responsive walks from pass-1 (`continua-pass1-it.md`) are NOT re-run; pass-1's strong visual outcome is preserved unmodified, so re-walking those would only repeat work without adding signal.

---

## 1 · Server posture

- **Working dir**: `C:\tmp\sitoBadr2\mw-integration-baseline-v15`
- **Branch**: `phase-x4-continua-pass1-review-lock`
- **Dev server**: `python manage.py runserver 127.0.0.1:8092 --noreload` (background)
- **URL kept open**: `http://127.0.0.1:8092/templates/business/continua-stewardship/preview/?preview=1`
- **Auth**: `solaria_qa_staff / continuapass1lock` (existing staff user reused from Solaria passes; password reset for this verification session only)
- **DB tier of `continua-stewardship`**: `draft` (synced from `TEMPLATE_REGISTRY.json` via `python manage.py sync_template_tiers`)

`manage.py sync_template_tiers` post-condition: 22 published_live / 1 draft.

---

## 2 · Captures filed

```
factory/reports/browser-verification/continua-pass1-review-lock/
  home-1440-firstscroll.png        · Continua hero · 1440 viewport · staff + ?preview=1
  listing-staff-preview-1440.png   · /templates/business/?preview=1 · staff sees Continua + 4 live siblings
```

Two captures only — the visual evidence the lock-pass needs is "the page still renders the same hero" + "the staff listing surfaces the draft Continua card alongside live siblings". Pass-1's full 12-PNG walk is the canonical visual record and is not repeated.

---

## 3 · The Pass-1.5-specific check

> **After flipping `tier` back to `draft` in the DB, the IT home opened with `?preview=1` in a staff session must still render and propagate `?preview=1` on every internal href, while anonymous traffic must continue to 404.**

### 3.1 Staff session · 11 internal hrefs harvested from the rendered IT home

```
/templates/business/continua-stewardship/?preview=1                                        → 200
/templates/business/?preview=1                                                              → 200
/templates/business/continua-stewardship/preview/?preview=1                                 → 200
/templates/business/continua-stewardship/preview/chi-siamo/?preview=1                       → 200
/templates/business/continua-stewardship/preview/custodia/?preview=1                        → 200
/templates/business/continua-stewardship/preview/mandati/?preview=1                         → 200
/templates/business/continua-stewardship/preview/contatti/?preview=1                        → 200
/templates/business/continua-stewardship/preview/case-studies/famiglia-a-…/?preview=1       → 404 ★
/templates/business/continua-stewardship/preview/case-studies/famiglia-b-…/?preview=1       → 404 ★
/templates/business/continua-stewardship/preview/case-studies/famiglia-c-…/?preview=1       → 404 ★
/templates/business/continua-stewardship/preview/case-studies/famiglia-d-…/?preview=1       → 404 ★
```

7 / 11 → 200. The 4 ★ entries fall back to 404 due to a pre-existing hardcoded `'case-studies'` parent slug in the shared `templates/live_templates/business/corporate-suite/home.html:660`. Continua's case_study_list page slug is `mandati`, so the home-band href routes to a non-existent page. **This was not introduced by review-lock**; it predates Continua's commit and affects Fiscus + Solaria the same way. Detail in `factory/reports/scorecard/continua-pass1-review-lock/build-report.md §4`.

### 3.2 The legitimate detail-route walk via the nav

The natural review path from `home → Mandati nav link → list → detail` works end-to-end:

```
/preview/mandati/?preview=1                                                                 → 200
/preview/mandati/famiglia-a-quarta-generazione-holding-industriale/?preview=1               → 200
/preview/mandati/famiglia-b-fondazione-di-famiglia/?preview=1                               → 200
/preview/mandati/famiglia-c-trasferimento-intergenerazionale/?preview=1                     → 200
/preview/mandati/famiglia-d-single-family-office-estero/?preview=1                          → 200
```

5 / 5 → 200. Every case-study detail post is reachable from a staff session via the nav-driven flow.

### 3.3 Anonymous tier-gate probes (must 404 / must NOT list)

```
GET /templates/business/continua-stewardship/preview/         (no cookies) → 404 ✓
GET /templates/business/                                       (no cookies) → 200, body does not contain
                                                                                "continua-stewardship" ✓
```

The D-055 tier gate is intact — anonymous traffic cannot reach the preview surface and cannot see Continua in the listing.

### 3.4 Staff listing visibility

```
GET /templates/business/?preview=1                             (staff session) → 200
                                                                                  body lists 5 cards:
                                                                                  Continua + Pragma + Fiscus
                                                                                  + Solaria + Elevate
```

Continua surfaces in the listing only when staff opts in via `?preview=1`. Anonymous catalog count is 4; staff-preview catalog count is 5. The card visible at `listing-staff-preview-1440.png` shows Continua sitting next to Solaria, both surfaced under the corporate-suite cluster.

---

## 4 · What was NOT walked

- Multilingual (EN/FR/ES/AR + AR RTL parity) — out of scope per pass-1 brief; deferred to workflow C.
- Responsive at 5 viewports — pass-1 covered this; no source change here that would invalidate it.
- Contrast/accessibility — same reason; no theme or palette change.
- Reduced-motion — same.
- Editor / projects / commerce surfaces — explicit hard constraint excludes these from any change in this pass; they need no re-walk.
- Style critique / scorecard re-grading — pass-1's `scorecard.md` (4.74 / 5) stands; review-lock is operational, not visual.

---

## 5 · Verdict

**Walk PASS** at the review-lock scope.

- 7/11 home hrefs → 200 with `?preview=1` propagated.
- 4/11 home → case-detail hrefs 404 due to a pre-existing shared-template hardcoded parent slug; **the same 4 detail posts are reachable via the nav-driven path** (5/5 → 200), so no review surface is unreachable.
- Anonymous tier gate intact (404 on preview, absent from listing).
- Staff listing correctly surfaces Continua as the 1 draft card alongside 4 live siblings.

Server URL kept open at:
`http://127.0.0.1:8092/templates/business/continua-stewardship/preview/?preview=1`
(login as `solaria_qa_staff / continuapass1lock` if the session is fresh)

The reviewer can now walk Continua exactly as they would walk Solaria pre-Pass-D — through the legitimate D-055 path — with no DB/registry mismatch lurking underneath.
