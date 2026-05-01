# Build-report · Cornice Public Flip · 2026-05-01

**Branch**: `phase-x5-cornice-public-flip`
**Status**: applied · `tier=draft → published_live` · catalog 23 → **24 live / 0 draft**
**Author**: release-gatekeeper (Phase X.5 · public-flip cascade)
**Predecessor pass**: workflow D `release-gatekeeper.md` (HOLD · APPROVED-PENDING-HANDSHAKE)
**Trigger**: explicit user authorization in this conversation (2026-05-01)

---

## 1 · What changed

| Layer | File | Change |
|---|---|---|
| Registry | `TEMPLATE_REGISTRY.json` (Cornice row · L341–L389) | `tier: draft → published_live` · `tier_reason` rewritten to consolidate workflow A.5 → A.6 → C → D → public flip audit trail |
| DB | runtime (no migration) | `python manage.py sync_template_tiers` → `cornice-architettura: draft -> published_live` · 1 row updated |
| Tests · tier-fact | `apps/catalog/tests.py` | 7 explicit-literal swaps `23 → 24` and `"23+" → "24+"` (L824, L862, L868, L1134, L1141, L1554, L1556) |
| Tests · related-templates | `apps/catalog/tests.py` (L1265–L1273) | `test_pragma_falls_back_gracefully` · default `limit=3` → explicit `limit=4` (Cornice promotion shifted Pragma's category-fallback pool past the 3-slot ceiling; intent of layered-fallback test preserved) |

Total: **2 source/config files** (1 JSON + 1 test module) and **0 template/view/migration edits**.

## 2 · What did NOT change

- `apps/editor/**` — UNTOUCHED
- `apps/projects/**` — UNTOUCHED
- `apps/commerce/**` — UNTOUCHED
- `apps/catalog/template_content_cornice*.py` (5 locale modules · IT/EN/FR/ES/AR) — UNTOUCHED
- `apps/catalog/template_content.py` (Cornice schema entry) — UNTOUCHED
- `apps/catalog/views.py · selectors.py · models.py · imagery_pool.py · theme_safety.py` — UNTOUCHED
- `apps/catalog/management/commands/seed_templates.py` — UNTOUCHED (Cornice seed entry frozen)
- `templates/live_templates/business/corporate-suite/**` — UNTOUCHED (LF-2 layouts frozen)
- `templates/pages/home.html` — UNTOUCHED (counter is dynamic from DB)
- `apps/pages/views.py` — UNTOUCHED
- DNA registry · migrations — UNTOUCHED
- No new archetype · no new template · no new image · no new locale · no new migration

## 3 · Why no template/view edit was needed for the trust counter

`apps/pages/views.py:94–103` already binds `templates_live` from a live DB
filter on `tier=PUBLISHED_LIVE`. `templates/pages/home.html:32` and `:170`
consume it as `{{ trust_counters.templates_live }}+`. So the moment
`sync_template_tiers` lifted Cornice's row, `23+` became `24+` automatically.
The workflow D playbook anticipated this with "Check before editing — the
registry-derived path may already be authoritative". Confirmed live (browser
verifier §3.3 + §4.2).

## 4 · Why the related-templates test needed 1 line changed

Pragma's related-templates fallback walks cluster → style → category. Pragma's
cluster `corporate` is a singleton; the style layer `classic-serif` includes
Lex (and now also the corporate-suite siblings Continua + Cornice that share
the same style); the category layer `business` adds Elevate. With Cornice
draft, the style layer returned 2 siblings (Continua + Lex) and the category
layer fit Elevate at slot 3. With Cornice live, the style layer returns 3
siblings (Continua + Cornice + Lex) and Elevate is bumped at the default
`limit=3`. The test asserts both Lex AND Elevate must surface — bumping the
limit to 4 preserves that intent without changing the selector contract or
the rendered UI (the UI surface that consumes this selector defaults to 3
slots and is unchanged). One-line test edit + comment-line documenting the
post-flip semantics.

## 5 · Cascade execution log

```
$ python manage.py sync_template_tiers
WARNINGS:
business-corporate: (corporate_suite.W001) corporate-suite imagery pool 'business-corporate' is grandfathered ...
  cornice-architettura: draft -> published_live

1 tier(s) updated. Catalog distribution: 24 published_live / 0 draft.

$ python manage.py test
Ran 546 tests in 184.7s
FAILED (failures=1)
  → test_medical_and_restaurant_templates_have_booking_flag    [pre-existing · Continua-related · documented]

$ curl -sS http://127.0.0.1:8052/templates/business/cornice-architettura/preview/
HTTP/1.1 200 OK                                                  (was 404 anon)

$ curl -sS http://127.0.0.1:8052/ | grep -oE 'mw-home-trust-n[^>]*>[^<]+'
mw-home-trust-n">24+                                              (was "23+")

$ curl -sS http://127.0.0.1:8052/templates/business/ | grep -c cornice-architettura
5                                                                 (was 0)

$ curl -sS http://127.0.0.1:8052/templates/business/ | grep -oE '[0-9]+ template (disponibili|disponibile)'
6 template disponibili                                            (was 5)
```

## 6 · DB tier distribution (post-flip)

```
$ python manage.py shell -c "from apps.catalog.models import WebTemplate; print('LIVE:', WebTemplate.objects.filter(tier='published_live').count(), 'DRAFT:', WebTemplate.objects.filter(tier='draft').count())"
LIVE: 24 DRAFT: 0
```

24 live · 0 draft. Cornice is now the cluster's 5th live sibling.

## 7 · Server posture

```
$ python manage.py runserver 127.0.0.1:8052 --noreload
```

Listening at `http://127.0.0.1:8052/`. Background process kept up across the flip; no restart required. Left running for user-side post-flip verification.

## 8 · Verdict

**APPLIED · GREEN.** All cascade steps from workflow D `release-gatekeeper.md §6` were performed verbatim with the addition of one related-templates test re-binding (covered above). Tests at the post-flip baseline (545/546 — same pre-existing failure as workflow D and Continua public-flip). Anonymous reachability live-confirmed. No new regressions introduced.
