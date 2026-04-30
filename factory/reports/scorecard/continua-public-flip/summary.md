# summary · Continua · Public Flip · 2026-04-30

**Status**: GREEN · `tier=published_live` · catalog 23/23 live · cluster ships 4 corporate-suite siblings · LF-5 active

---

## TL;DR

Continua flipped from `tier=draft` to `tier=published_live` after the user's explicit handshake closed the last gate workflow D held open. The cascade: 1 registry edit · 1 `sync_template_tiers` run · 7 explicit-literal test bumps in `apps/catalog/tests.py` · 0 source / template / HTML edits beyond those · 0 changes to editor/projects/commerce. Anonymous live verification at `http://127.0.0.1:8052/` is GREEN: catalog lists Continua, home trust counter renders `23+`, all 5 locale preview routes return 200 to anonymous visitors, AR ships `html dir="rtl"`, the 45-route smoke (5 locales × 5 pages + 5 locales × 4 mandate posts) returns 45/45 200, and frozen siblings (Pragma / Fiscus / Solaria) stay at 200. Test suite: 545/546 PASS — identical to workflow D pre-flip baseline (the sole failure is the documented pre-existing `test_medical_and_restaurant_templates_have_booking_flag`).

---

## Files changed

```
TEMPLATE_REGISTRY.json                                                                  (Continua row · tier + status + tier_reason)
apps/catalog/tests.py                                                                    (7 literal swaps · 22→23, "22+"→"23+")
factory/reports/continua/continua-public-flip.md                                        (new)
factory/reports/browser-verification/continua-public-flip.md                            (new)
factory/reports/scorecard/continua-public-flip/build-report.md                          (new)
factory/reports/scorecard/continua-public-flip/browser-verifier.md                      (new)
factory/reports/scorecard/continua-public-flip/release-gatekeeper.md                    (new)
factory/reports/scorecard/continua-public-flip/summary.md                               (this file · new)
C:/Users/badrw/.claude/projects/C--tmp-sitoBadr2-marketweb/memory/MEMORY.md             (rollup)
C:/Users/badrw/.claude/projects/C--tmp-sitoBadr2-marketweb/memory/phase_x4_continua_public_flip.md  (new)
```

---

## Commands run

```
python manage.py sync_template_tiers
python manage.py test
python manage.py runserver 127.0.0.1:8052 --noreload   (left running)
```

---

## Server posture

- **Command**: `python manage.py runserver 127.0.0.1:8052 --noreload`
- **URL**: `http://127.0.0.1:8052/`
- **Port**: 8052 (left running for any post-flip user re-walk)

Anonymous URLs to walk:

```
http://127.0.0.1:8052/                                                              (home · 23+ counter)
http://127.0.0.1:8052/templates/business/                                           (catalog · Continua card)
http://127.0.0.1:8052/templates/business/continua-stewardship/preview/              (IT)
http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=en      (EN)
http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=fr      (FR)
http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=es      (ES)
http://127.0.0.1:8052/templates/business/continua-stewardship/preview/?lang=ar      (AR · RTL)
```

No staff session required.

---

## Anonymous public verification

| Probe | Result |
|---|---|
| `/templates/business/` slug visibility | `continua-stewardship` × 5 in HTML (was 0) |
| Home `templates_live` counter | `23+` (was `22+`) |
| 5 locale preview routes | 5 × 200 anon (were 5 × 404 anon) |
| AR `html lang/dir` | `lang="ar" dir="rtl"` |
| 45-route catalog smoke | **45 / 45 200** |
| `?preview=1` legacy flag | benign no-op · 200 |
| Frozen siblings (Pragma / Fiscus / Solaria) | 3 × 200 |

---

## Final tier state

| Plane | Pre-flip | Post-flip |
|---|---|---|
| `TEMPLATE_REGISTRY.json` Continua `tier` | `draft` | **`published_live`** |
| `TEMPLATE_REGISTRY.json` Continua `status` | `draft` | **`published`** |
| DB `WebTemplate` Continua `tier` | `draft` | **`published_live`** |
| Catalog distribution | 22 published_live · 1 draft | **23 published_live · 0 draft** |

---

## Continua is now fully `published_live`.

The workflow A → A.5 → B → C → D → public-flip pipeline is closed. The corporate-suite cluster ships 4 live siblings (Pragma + Fiscus + Solaria + Continua) at full 5-locale parity with LF-5 layout-family divergence active for Continua. No further action required for this template; the gatekeeper queue moves on.
