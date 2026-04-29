# Continua · Pass 1.5 Review-Lock · Browser-verifier

**Date**: 2026-04-29
**Reference**: `factory/agents/browser-verifier.md`
**Scope**: review-lock only — verify the legitimate D-055 staff-preview path still works after the DB tier was synced from `published_live` back to `draft`. Does NOT re-walk pass-1's visual scorecard.
**Tool**: Playwright MCP (live · staff session) + `fetch` from the rendered home

---

## 1 · Pre-walk state

```bash
$ python manage.py sync_template_tiers
  continua-stewardship: published_live -> draft
  1 tier(s) updated. Catalog distribution: 22 published_live / 1 draft.

$ python manage.py shell -c "from apps.catalog.models import WebTemplate; \
  print(WebTemplate.objects.get(slug='continua-stewardship').tier)"
draft

$ python manage.py runserver 127.0.0.1:8092 --noreload &
```

Auth: `solaria_qa_staff / continuapass1lock` (existing staff user reused from Solaria passes; password reset for this verification session only). Login completed at `/account/login/?next=/templates/business/continua-stewardship/preview/?preview=1` and the form redirect landed directly on the preview at HTTP 200.

---

## 2 · Anonymous tier-gate probes (must reject)

| Probe | Status | Verdict |
|---|---|---|
| `GET /templates/business/continua-stewardship/preview/` (no cookies) | **404** | PASS — D-055 tier gate intact |
| `GET /templates/business/` (no cookies) — body contains `continua-stewardship`? | **NO** | PASS — anonymous catalog does not surface draft |

Pass-1's "DB-flipped-to-live" state would have made both of these green-light Continua to anonymous traffic. The lock-pass closes that exposure.

---

## 3 · Staff-session in-page hrefs harvested from the rendered home

11 unique internal hrefs found on the IT home, all carrying `?preview=1`:

```
/templates/business/continua-stewardship/?preview=1
/templates/business/?preview=1
/templates/business/continua-stewardship/preview/?preview=1
/templates/business/continua-stewardship/preview/chi-siamo/?preview=1
/templates/business/continua-stewardship/preview/custodia/?preview=1
/templates/business/continua-stewardship/preview/mandati/?preview=1
/templates/business/continua-stewardship/preview/contatti/?preview=1
/templates/business/continua-stewardship/preview/case-studies/famiglia-a-quarta-generazione-holding-industriale/?preview=1   ★
/templates/business/continua-stewardship/preview/case-studies/famiglia-b-fondazione-di-famiglia/?preview=1                   ★
/templates/business/continua-stewardship/preview/case-studies/famiglia-c-trasferimento-intergenerazionale/?preview=1         ★
/templates/business/continua-stewardship/preview/case-studies/famiglia-d-single-family-office-estero/?preview=1              ★
```

`?preview=1` propagation: **11/11 ✓** (zero drops). The corporate-suite chrome added in Solaria Pass C threads the flag correctly through every internal href; Continua reuses that chrome unchanged.

Status of each `fetch()` against the staff session:

| URL | Status | Notes |
|---|---|---|
| `…/continua-stewardship/?preview=1` | 200 | mp-back to detail page |
| `/templates/business/?preview=1` | 200 | mp-back to category listing |
| `…/preview/?preview=1` | 200 | home (current) |
| `…/preview/chi-siamo/?preview=1` | 200 | nav |
| `…/preview/custodia/?preview=1` | 200 | nav |
| `…/preview/mandati/?preview=1` | 200 | nav |
| `…/preview/contatti/?preview=1` | 200 | nav |
| `…/preview/case-studies/famiglia-a-…/?preview=1` ★ | **404** | home preview-band row |
| `…/preview/case-studies/famiglia-b-…/?preview=1` ★ | **404** | home preview-band row |
| `…/preview/case-studies/famiglia-c-…/?preview=1` ★ | **404** | home preview-band row |
| `…/preview/case-studies/famiglia-d-…/?preview=1` ★ | **404** | home preview-band row |

7 / 11 → 200. The 4 ★ entries are a pre-existing pass-1 carryover (hardcoded `'case-studies'` parent slug in shared `home.html:660`); root cause + recommended fix in `build-report.md §4`.

---

## 4 · Detail-route reachability via the legitimate nav path

The 4 case-study posts above are still reachable in the same staff session through the nav-driven walk: home → "Mandati" nav (200) → mandati list (200) → each row (4/4 → 200).

```
/templates/business/continua-stewardship/preview/mandati/?preview=1                                                            → 200
/templates/business/continua-stewardship/preview/mandati/famiglia-a-quarta-generazione-holding-industriale/?preview=1          → 200
/templates/business/continua-stewardship/preview/mandati/famiglia-b-fondazione-di-famiglia/?preview=1                          → 200
/templates/business/continua-stewardship/preview/mandati/famiglia-c-trasferimento-intergenerazionale/?preview=1                → 200
/templates/business/continua-stewardship/preview/mandati/famiglia-d-single-family-office-estero/?preview=1                     → 200
```

5 / 5 → 200. Every review-relevant surface is reachable.

---

## 5 · Staff listing visibility

`GET /templates/business/?preview=1` (staff session) → 200 · 5 cards: Continua + Pragma + Fiscus + Solaria + Elevate.

The card grid screenshot at `factory/reports/browser-verification/continua-pass1-review-lock/listing-staff-preview-1440.png` shows the Continua "BUSINESS · PREMIUM" card on the left, Solaria on the right, both surfaced under the corporate-suite cluster. The page's "5 template disponibili" string verifies the staff-preview augmentation (anonymous count is 4).

---

## 6 · Visual carry-forward from pass-1

`home-1440-firstscroll.png` captures the Continua hero in the staff session at 1440 viewport. The image shows:

- Brass eyebrow underline + "FAMILY OFFICE · MILANO · STEWARDSHIP MULTIGENERAZIONALE"
- H1 with `<em>generazioni</em>` italic in Crimson Pro
- Library-room object-led hero photo (Pexels 36093623) on the right
- Pine primary in nav + brass secondary touchpoints (CTA, KPI label borders, sede ribbon)
- "Avvia un dialogo di mandato" CTA + "Lo studio di custodia" secondary

This matches pass-1's `home-1440-fixed-em.png` reference verbatim — the visual outcome is preserved unmodified by the lock-pass.

---

## 7 · Stop-conditions checklist (review-lock subset)

| # | Condition | Status |
|---|---|---|
| 1 | Anonymous probe of `/preview/` returns 404 | PASS |
| 2 | Anonymous catalog does NOT list Continua | PASS |
| 3 | Staff `/preview/?preview=1` returns 200 | PASS |
| 4 | Staff catalog WITH `?preview=1` lists Continua | PASS |
| 5 | All in-page internal hrefs propagate `?preview=1` | PASS (11/11) |
| 6 | The 4 case-detail posts are reachable in the same session | PASS (via nav-driven path · 5/5) |
| 7 | Pass-1 visual outcome preserved | PASS (hero capture matches) |
| 8 | DB and registry agree on `tier: draft` | PASS |
| 9 | `sync_template_tiers` is idempotent on this row | PASS (re-run prints 0 updates) |
| 10 | No editor / projects / commerce surface affected | PASS (zero source change) |

10 / 10 cleared.

---

## 8 · Verdict

**Walk PASS** at the review-lock scope. Continua is reachable through the legitimate D-055 staff-preview path with the DB and registry honest about the draft tier, and anonymous traffic is correctly rejected. The 4 home-preview-band hrefs that 404 are documented as a pre-existing finding outside this pass's minimum-fix scope; the underlying review surfaces are all reachable via the nav.
