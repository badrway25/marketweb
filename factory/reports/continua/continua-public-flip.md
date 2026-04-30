# Continua · Public Flip · Final Release

**Status**: GREEN · `tier=published_live` · Continua is now fully publicly reachable in all 5 locales · 2026-04-30
**Branch**: `phase-x4-continua-public-flip`
**Predecessor pass**: `factory/reports/continua/continua-workflowD-release-decision.md` (HOLD pending user handshake)
**User handshake**: explicit · "execute the documented Workflow D release cascade after explicit user approval" (this conversation, 2026-04-30)
**Cluster**: corporate-suite · 4th sibling · 1st family-office · LF-5 active · 4th cluster live sibling
**Catalog count**: 22 → **23** published_live · 0 draft

---

## 1 · Verdict (one paragraph)

Continua flipped from `tier=draft` to `tier=published_live` after the user provided the explicit parallel-verification handshake that workflow D §6 / R-SOL-8 / D-102 reserved as the final gate. The cascade documented to the line in workflow D §2 Q5 was applied verbatim: 1 registry edit (line 337 + tier_reason rewrite + status field flip), 1 management-command sync (`sync_template_tiers` reports `continua-stewardship: draft -> published_live` and lands the catalog at **23 published_live / 0 draft**), 7 tier-fact test-literal bumps in `apps/catalog/tests.py` (`templates_live` 22→23 · catalog `total` 22→23 (×2) · `qs.count()` 22→23 (×2) · `has_rtl` 22→23 · home-rendered string `"22+"`→`"23+"`), zero source/template/HTML edits (the home trust-counter binding is fully dynamic from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()` so the rendered band updates with no template change), and 0 changes to `apps/editor/`, `apps/projects/`, `apps/commerce/`. Full Django test run: **545/546 PASS** with the single failure being the documented pre-existing `test_medical_and_restaurant_templates_have_booking_flag` (assertion enumerates the medical/restaurant/lawyer/W2-booking cohort; Continua carries `has_booking=True` from seed but is not a member of any of those families · same failure mode as every prior Continua pass · zero new regressions). Anonymous live verification on `http://127.0.0.1:8052/`: home page renders `23+ template premium` (was `22+`), `/templates/business/` lists `continua-stewardship` as a public card (slug appears 5× in the rendered HTML — was absent), all 5 locale preview routes (IT/EN/FR/ES/AR) return 200 to anonymous visitors with no `?preview=1` flag, AR locale serves `html lang="ar" dir="rtl"` and the LF-5 letter-spacing reset still applies, the legacy `?preview=1` flag is now a benign no-op pass-through (route serves 200 either way · staff-preview semantics preserved for any link the corporate-suite chrome may still propagate), and the 45-route catalog smoke (5 locales × 5 pages + 5 locales × 4 mandate posts) returns **45/45 200** anonymously. Frozen siblings Pragma/Fiscus/Solaria spot-check 200/200/200 — no cluster regression. Continua is now **fully published_live**.

---

## 2 · Cascade applied (line-by-line)

Applied verbatim from workflow D §2 Q5 (the Solaria Pass D playbook adapted to Continua's row).

### 2.1 · Registry flip (1 file)

`TEMPLATE_REGISTRY.json` — Continua row:

```diff
-      "status": "draft",
-      "tier": "draft",
-      "tier_reason": "Phase X.4 design-orchestrator first real candidate (pass 1 IT, 2026-04-29 ...) ... Public catalog count remains unchanged at draft; staff preview reaches the live route via `?preview=1`."
+      "status": "published",
+      "tier": "published_live",
+      "tier_reason": "Phase X.4 Continua — Family-Office Stewardship · 4th corporate-suite sibling · 1st family-office variant · 23rd published_live template. ... Public flip (2026-04-30) flipped tier draft → published_live after the user completed the parallel-verification handshake and authorised the gatekeeper to apply the documented cascade: 7 tier-fact test assertions bumped 22 → 23, no template/source/HTML edits, dynamic trust counter inherits 22+ → 23+ from DB. Public catalog count moves 22 → 23; Continua card surfaces under /templates/business/ for anonymous visitors; staff-preview path (?preview=1) preserved as a no-op since the slug is now publicly reachable."
```

The `tier_reason` rewrite consolidates workflow A → workflow A.5 → workflow B → workflow C → workflow D → public flip into a single audit trail string mirroring Solaria's pass D format.

### 2.2 · Database sync (1 management command)

```
$ python manage.py sync_template_tiers
  continua-stewardship: draft -> published_live
1 tier(s) updated. Catalog distribution: 23 published_live / 0 draft.
```

Single row updated. No other slugs touched. The `business-corporate` LEGACY_EXEMPT_KEYS warning is the same `(corporate_suite.W001)` advisory every prior corporate-suite pass observed and is unchanged from the workflow D pre-flip baseline (AP3 retro-curation backlog · not a flip blocker).

### 2.3 · Trust-counter cascade (zero source edits)

The catalog's "trust counter" string in the marketing band is rendered from a live DB filter at `apps/pages/views.py:94–103`:

```python
ctx["trust_counters"] = {
    "templates_live": WebTemplate.objects.filter(
        tier=WebTemplate.Tier.PUBLISHED_LIVE
    ).count(),
    ...
}
```

…and the home template binds `{{ trust_counters.templates_live }}+` at `templates/pages/home.html:32` and `:170`. So the moment the DB sync lands `23` in that filter, the rendered string updates from `22+` to `23+` with no edit to view code, template HTML, CSS, or static assets. Verified live (§4.2).

### 2.4 · Tier-fact test bumps (1 file · 7 literal swaps)

`apps/catalog/tests.py`:

| L# | Before | After | Test |
|---|---|---|---|
| 824 | `qs.count(), 22` | `qs.count(), 23` | `test_listing_filter_by_unknown_feature_flag_is_ignored` |
| 862 | `counts["total"], 22` | `counts["total"], 23` | `test_facet_counts_shape` |
| 868 | `counts["features"].get("has_rtl"), 22` | `counts["features"].get("has_rtl"), 23` | `test_facet_counts_shape` |
| 1134 | `counters["templates_live"], 22` | `counters["templates_live"], 23` | `test_home_trust_counters_are_live_from_db` |
| 1141 | `assertIn("22+", body)` | `assertIn("23+", body)` | `test_home_trust_counters_render_in_html` |
| 1554 | `qs.count(), 22` | `qs.count(), 23` | `test_discovery_surfaces_no_regression` |
| 1556 | `counts["total"], 22` | `counts["total"], 23` | `test_discovery_surfaces_no_regression` |

Per `DECISIONS.md` "Explicit literal counts in public-count tests beat dynamic `len(...)`" rationale: these literals are intentional Wave-2-merge tripwires. The dynamic `len(SEED_TEMPLATE_METADATA)` tests at L561, L705, L711, L1470 already track the seed automatically and required no edit.

### 2.5 · Files NOT changed

To eliminate scope ambiguity:

- `apps/editor/**` — UNTOUCHED
- `apps/projects/**` — UNTOUCHED
- `apps/commerce/**` — UNTOUCHED
- `apps/catalog/template_content_continua*.py` — UNTOUCHED (5 locale modules)
- `apps/catalog/views.py · selectors.py · models.py · imagery_pool.py · theme_safety.py` — UNTOUCHED
- `templates/live_templates/business/corporate-suite/**` — UNTOUCHED (no chrome edit)
- `templates/pages/home.html` — UNTOUCHED (counter is dynamic)
- DNA registry · seed command · migrations — UNTOUCHED
- No new archetype · no new template · no new migration

---

## 3 · Test suite

```
$ python manage.py test
Ran 546 tests in 182.0s
FAILED (failures=1)
  → test_medical_and_restaurant_templates_have_booking_flag
```

Pre-existing failure documented in workflow D §3.4 + `continua-lf5-it-rebuild.md §8.4`. The assertion compares the medical/restaurant/lawyer/Wave-2-booking exact slug-set; Continua carries `has_booking=True` from its Pass-1 seed (Wave 2 design intent — family-office mandate-dialogue is booking-shaped) but is not a member of any of those families, so the set difference reads `Items in the first set but not the second: 'continua-stewardship'`. Same failure mode as every prior Continua pass (workflow A, A.5, B, C, D). Zero new regressions introduced by the flip.

Final tally: **545 / 546 PASS** · same as workflow D pre-flip baseline.

---

## 4 · Anonymous live verification (`http://127.0.0.1:8052/`)

### 4.1 · Anonymous routes — pass

```
GET /templates/business/                                                  → 200
GET /templates/business/continua-stewardship/preview/                     → 200    (was 404)
GET /templates/business/continua-stewardship/preview/?lang=en             → 200
GET /templates/business/continua-stewardship/preview/?lang=fr             → 200
GET /templates/business/continua-stewardship/preview/?lang=es             → 200
GET /templates/business/continua-stewardship/preview/?lang=ar             → 200    (RTL)
```

The 4 mandate-detail posts ship reachable per locale: 5 locales × 4 posts = 20 routes, all 200. Combined with 5 locales × 5 page kinds = 25 routes, the **45-route smoke returns 45/45 200 anonymously** (post slugs discovered live: `famiglia-a-quarta-generazione-holding-industriale`, `famiglia-b-fondazione-di-famiglia`, `famiglia-c-trasferimento-intergenerazionale`, `famiglia-d-single-family-office-estero`).

### 4.2 · Trust counter rendered live

```
$ curl -sS http://127.0.0.1:8052/ | grep -oE 'mw-home-trust-n[^>]*>[^<]+'
mw-home-trust-n">23+        ← templates_live   (was 22+)
mw-home-trust-n">15         ← categories_active
mw-home-trust-n">52         ← clusters_active
mw-home-trust-n">5          ← locales_supported
```

`23+` appears twice in the home-page HTML (hero meta strip line 32 + trust-band figure line 170). Inherited from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()` with zero template edit.

### 4.3 · Catalog band surfaces Continua

```
$ curl -sS http://127.0.0.1:8052/templates/business/ | grep -c continua-stewardship
5
```

Slug appears 5 times on the anonymous business catalog page (card image src + name + cluster chip + detail link + meta). Was 0 before the flip.

### 4.4 · AR RTL parity preserved

```
$ curl -sS '...?lang=ar' | grep -oE 'html lang="[^"]+"|dir="[^"]+"'
html lang="ar"
dir="rtl"
dir="rtl"
```

LF-5 letter-spacing reset (Pass B `_base.html` extension across 9 LF-5 eyebrow surfaces under `html[dir="rtl"]`) was not edited and remains in place.

### 4.5 · Staff-preview legacy flag remains benign

```
GET /templates/business/continua-stewardship/preview/?preview=1            → 200
GET /templates/business/continua-stewardship/preview/?lang=ar&preview=1    → 200
```

The `?preview=1` flag is now a no-op pass-through: any internal link the corporate-suite chrome may still propagate from a stale staff session continues to work. The D-055 anonymous gate is no longer triggered for this slug because `tier=published_live` short-circuits it upstream.

### 4.6 · Frozen-sibling regression spot-check

```
GET /templates/business/pragma-corporate-suite/preview/                   → 200
GET /templates/business/fiscus-commercialista/preview/                    → 200
GET /templates/business/solaria-coaching/preview/                         → 200
```

Cluster mates unaffected. No collateral.

---

## 5 · Files changed (full list)

### Source / config (3 files):

```
TEMPLATE_REGISTRY.json
  · Continua row · status draft → published · tier draft → published_live
  · tier_reason rewritten to consolidate workflow A→D + public flip audit trail

apps/catalog/tests.py
  · L824  · qs.count() literal       22 → 23
  · L862  · counts["total"] literal  22 → 23
  · L868  · has_rtl literal          22 → 23
  · L1134 · templates_live literal   22 → 23
  · L1141 · "22+" literal            "22+" → "23+"
  · L1554 · qs.count() literal       22 → 23
  · L1556 · counts["total"] literal  22 → 23
```

### Reports / scorecards (4 + 2 = 6 docs):

```
factory/reports/continua/continua-public-flip.md                                   (this file)
factory/reports/browser-verification/continua-public-flip.md                       (browser walk index)
factory/reports/scorecard/continua-public-flip/build-report.md
factory/reports/scorecard/continua-public-flip/browser-verifier.md
factory/reports/scorecard/continua-public-flip/release-gatekeeper.md
factory/reports/scorecard/continua-public-flip/summary.md
```

### Memory rollup:

```
C:/Users/badrw/.claude/projects/C--tmp-sitoBadr2-marketweb/memory/MEMORY.md
C:/Users/badrw/.claude/projects/C--tmp-sitoBadr2-marketweb/memory/phase_x4_continua_public_flip.md
```

---

## 6 · Final state

| Field | Pre-flip | Post-flip |
|---|---|---|
| Registry · `tier` | `draft` | **`published_live`** |
| Registry · `status` | `draft` | **`published`** |
| Registry · `locales` | `[it,en,fr,es,ar]` | unchanged |
| Registry · `rtl` | `true` | unchanged |
| DB · `WebTemplate.tier` (Continua) | `draft` | **`published_live`** |
| DB · catalog distribution | 22 live / 1 draft | **23 live / 0 draft** |
| Anonymous `/templates/business/` slug | absent | **present (5× in HTML)** |
| Anonymous `?lang=*` reachability | 404 anon · staff-only | **200 all 5 locales** |
| Home `templates_live` counter | `22+` | **`23+`** |
| Test suite | 545 / 546 | 545 / 546 (same pre-existing failure) |
| Pragma/Fiscus/Solaria | 200 / 200 / 200 | 200 / 200 / 200 |

**Continua is now fully `published_live`.** The corporate-suite cluster ships 4 live siblings (Pragma + Fiscus + Solaria + Continua) at full multilingual parity with LF-5 layout-family divergence active for Continua against the three frozen siblings.

---

## 7 · Server posture at landing

```
$ python manage.py runserver 127.0.0.1:8052 --noreload
```

Listening at **http://127.0.0.1:8052/**. Server left running for any user-side post-flip verification. URL/port preserved on the scorecard.

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
