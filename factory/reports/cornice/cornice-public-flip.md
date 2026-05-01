# Cornice · Public Flip · Final Release

**Status**: GREEN · `tier=published_live` · Cornice is now fully publicly reachable in all 5 locales · 2026-05-01
**Branch**: `phase-x5-cornice-public-flip`
**Predecessor pass**: `factory/reports/cornice/cornice-workflowD-release-decision.md` (HOLD pending user handshake · APPROVED-PENDING-HANDSHAKE)
**User handshake**: explicit · "execute the documented Workflow D release cascade after explicit user approval" (this conversation, 2026-05-01)
**Cluster**: corporate-suite · 5th sibling · 1st LF-2 occupant in the cluster · 1st single-principal architecture-firm variant
**Catalog count**: 23 → **24** published_live · 0 draft

---

## 1 · Verdict (one paragraph)

Cornice flipped from `tier=draft` to `tier=published_live` after the user provided the explicit parallel-verification handshake that workflow D §6 / R-SOL-8 / SOP §5.4 / D-102 reserved as the final gate. The cascade documented to the line in workflow D `release-gatekeeper.md §6` was applied verbatim: 1 registry edit (line 387 + tier_reason rewrite), 1 management-command sync (`sync_template_tiers` reports `cornice-architettura: draft -> published_live` and lands the catalog at **24 published_live / 0 draft**), 7 tier-fact test-literal bumps in `apps/catalog/tests.py` (`templates_live` 23→24 · catalog `total` 23→24 (×2) · `qs.count()` 23→24 (×2) · `has_rtl` 23→24 · home-rendered string `"23+"`→`"24+"`), 1 related-templates test re-binding (Pragma fallback test bumped from `limit=3` to `limit=4` so both style-layer (Lex) and category-layer (Elevate) candidates remain visible alongside the corporate-suite style siblings — the test's intent is preserved), zero source/template/HTML edits (the home trust-counter binding is fully dynamic from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()` so the rendered band updates with no template change), and 0 changes to `apps/editor/`, `apps/projects/`, `apps/commerce/`. Full Django test run: **545/546 PASS** with the single failure being the documented pre-existing `test_medical_and_restaurant_templates_have_booking_flag` (Continua-related · enumerates the medical/restaurant/lawyer/W2-booking cohort and `continua-stewardship` carries `has_booking=True` from seed but is not a member of any of those families · same failure mode as every prior Continua and Cornice pass · zero new regressions). Anonymous live verification on `http://127.0.0.1:8052/`: home page renders `24+ template premium` (was `23+`), `/templates/business/` lists `cornice-architettura` as a public card (slug appears 5× in the rendered HTML — was absent · catalog now reads `6 template disponibili` vs the prior 5), all 5 locale preview routes (IT/EN/FR/ES/AR) return 200 to anonymous visitors with no `?preview=1` flag, AR locale serves `html lang="ar" dir="rtl"` and the LF-2-scoped Naskh swap (`Noto Naskh Arabic` h1 inside `body.cs-lf-lf-2`) holds verbatim, the legacy `?preview=1` flag is now a benign no-op pass-through, and a 45-route catalog smoke (5 locales × 5 pages + 5 locales × 4 case-detail) returns **45/45 200** anonymously. Frozen siblings Pragma/Fiscus/Solaria/Continua spot-check 200/200/200/200 and Continua's AR LF-5 h1 still computes to `Noto Kufi Arabic` (zero Naskh leakage across LF families). Cornice is now **fully published_live**.

---

## 2 · Cascade applied (line-by-line)

Applied verbatim from `factory/reports/scorecard/cornice-workflowD-release-decision/release-gatekeeper.md §6` (the same Continua public-flip playbook adapted to Cornice's row).

### 2.1 · Registry flip (1 file)

`TEMPLATE_REGISTRY.json` — Cornice row (`slug: cornice-architettura`):

```diff
       "status": "published",
-      "tier": "draft",
-      "tier_reason": "Phase X.5 Cornice · workflow C multilingual rollout (2026-05-01) ... Public flip held for the user-handshake on the multilingual walk (workflow D)."
+      "tier": "published_live",
+      "tier_reason": "Phase X.5 Cornice — Studio di Architettura · 5th corporate-suite sibling · 1st LF-2 occupant in the cluster · 1st single-principal architecture-firm variant · 24th published_live template. ... Public flip (2026-05-01) flipped tier draft → published_live after the user completed the parallel-verification handshake and authorised the gatekeeper to apply the documented cascade: 7 tier-fact test assertions bumped 23 → 24, no template/source/HTML edits, dynamic trust counter inherits 23+ → 24+ from DB. ..."
```

The `tier_reason` rewrite consolidates workflow A.5 → A.6 → C → D → public-flip into a single audit trail string mirroring Continua's pass D format. `status` stays `published` (was already `published` pre-flip · only `tier` flipped).

### 2.2 · Database sync (1 management command)

```
$ python manage.py sync_template_tiers
WARNINGS:
business-corporate: (corporate_suite.W001) corporate-suite imagery pool 'business-corporate' is grandfathered ...
  cornice-architettura: draft -> published_live

1 tier(s) updated. Catalog distribution: 24 published_live / 0 draft.
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

…and the home template binds `{{ trust_counters.templates_live }}+` at `templates/pages/home.html:32` and `:170`. So the moment the DB sync lands `24` in that filter, the rendered string updates from `23+` to `24+` with no edit to view code, template HTML, CSS, or static assets. Verified live (§4.2).

### 2.4 · Tier-fact test bumps (1 file · 7 literal swaps)

`apps/catalog/tests.py`:

| L# | Before | After | Test |
|---|---|---|---|
| 824 | `qs.count(), 23` | `qs.count(), 24` | `test_listing_filter_by_unknown_feature_flag_is_ignored` |
| 862 | `counts["total"], 23` | `counts["total"], 24` | `test_facet_counts_shape` |
| 868 | `counts["features"].get("has_rtl"), 23` | `counts["features"].get("has_rtl"), 24` | `test_facet_counts_shape` |
| 1134 | `counters["templates_live"], 23` | `counters["templates_live"], 24` | `test_home_trust_counters_are_live_from_db` |
| 1141 | `assertIn("23+", body)` | `assertIn("24+", body)` | `test_home_trust_counters_render_in_html` |
| 1554 | `qs.count(), 23` | `qs.count(), 24` | `test_discovery_surfaces_no_regression` |
| 1556 | `counts["total"], 23` | `counts["total"], 24` | `test_discovery_surfaces_no_regression` |

Per `DECISIONS.md` "Explicit literal counts in public-count tests beat dynamic `len(...)`" rationale: these literals are intentional Wave-2-merge tripwires. The dynamic `len(SEED_TEMPLATE_METADATA)` tests at L561, L705, L711, L1470 already track the seed automatically and required no edit. Same 7-literal cascade as the Continua public-flip precedent.

### 2.5 · Related-templates fallback re-binding (1 file · 1 test edit)

`apps/catalog/tests.py · test_pragma_falls_back_gracefully` (L1265):

| L# | Before | After | Reason |
|---|---|---|---|
| 1269 | `slugs = self._related_slugs("pragma-corporate-suite")` (default `limit=3`) | `slugs = self._related_slugs("pragma-corporate-suite", limit=4)` | With Cornice live the fallback pool for Pragma now surfaces Continua + Cornice + Lex (style layer) ahead of Elevate (category layer); at `limit=3` Elevate is bumped. The test's intent is to validate the layered fallback (cluster → style → category) reaches **both** the style layer (Lex) **and** the category layer (Elevate). Bumping the limit to 4 preserves that intent without changing the selector contract. The cluster comment was extended to record the post-flip semantics. |

The test's three assertions (`assertGreater(len(slugs), 0)`, `assertIn("lex-studio-legale")`, `assertIn("elevate-startup-landing")`) are unchanged. This is a negative-test re-binding of the kind explicitly anticipated in workflow D `release-gatekeeper.md §6.7`: "Negative tests too: any test that asserts Cornice is *absent* from the live catalog must be revised." Pragma's fallback set is a soft member of that family — Cornice's promotion changes the available fallback pool.

### 2.6 · Files NOT changed

To eliminate scope ambiguity:

- `apps/editor/**` — UNTOUCHED
- `apps/projects/**` — UNTOUCHED
- `apps/commerce/**` — UNTOUCHED
- `apps/catalog/template_content_cornice*.py` — UNTOUCHED (5 locale modules · `it/en/fr/es/ar`)
- `apps/catalog/template_content.py` — UNTOUCHED (Cornice schema entry frozen)
- `apps/catalog/views.py · selectors.py · models.py · imagery_pool.py · theme_safety.py` — UNTOUCHED
- `templates/live_templates/business/corporate-suite/**` — UNTOUCHED (no chrome edit · LF-2 layouts frozen)
- `templates/pages/home.html` — UNTOUCHED (counter is dynamic)
- `apps/pages/views.py` — UNTOUCHED (trust counter is a live DB filter)
- DNA registry · seed command · migrations — UNTOUCHED
- No new archetype · no new template · no new migration · no new image · no new locale

---

## 3 · Test suite

```
$ python manage.py test
Ran 546 tests in 184.7s
FAILED (failures=1)
  → test_medical_and_restaurant_templates_have_booking_flag
```

Pre-existing failure documented in workflow D §3.4 + Continua public-flip §3 + every Cornice pass since A.5. The assertion compares the medical/restaurant/lawyer/Wave-2-booking exact slug-set; Continua carries `has_booking=True` from its Pass-1 seed (Wave 2 design intent — family-office mandate-dialogue is booking-shaped) but is not a member of any of those families, so the set difference reads `Items in the first set but not the second: 'continua-stewardship'`. Same failure mode as every prior Continua and Cornice pass (workflow A.5 → A.6 → C → D → public flip). Zero new regressions introduced by the Cornice flip.

Final tally: **545 / 546 PASS** · same as workflow D pre-flip baseline.

Note: an intermediate run showed an additional failure on `test_pragma_falls_back_gracefully` (Cornice promotion shifted Pragma's category-fallback pool past the default `limit=3`). The test was re-bound at §2.5 above and the re-run lands at the same 545/546 result.

---

## 4 · Anonymous live verification (`http://127.0.0.1:8052/`)

### 4.1 · Anonymous routes — pass

```
GET /                                                                       → 200
GET /templates/business/                                                    → 200
GET /templates/business/cornice-architettura/preview/                       → 200    (was 404)
GET /templates/business/cornice-architettura/preview/?lang=en               → 200
GET /templates/business/cornice-architettura/preview/?lang=fr               → 200
GET /templates/business/cornice-architettura/preview/?lang=es               → 200
GET /templates/business/cornice-architettura/preview/?lang=ar               → 200    (RTL)
```

The 4 case-detail posts ship reachable per locale: 5 locales × 4 posts = 20 routes, all 200 anonymously (slugs: `biblioteca-pietrasanta-concorso`, `via-volpe-roma-residenziale`, `palazzo-lignari-bologna-restauro`, `cornice-fronte-minore-saggio`). Combined with 5 locales × 5 page kinds = 25 routes, the **45-route smoke returns 45/45 200 anonymously**.

### 4.2 · Trust counter rendered live

```
$ curl -sS http://127.0.0.1:8052/ | grep -oE 'mw-home-trust-n[^>]*>[^<]+'
mw-home-trust-n">24+        ← templates_live   (was 23+)
mw-home-trust-n">15         ← categories_active
mw-home-trust-n">52         ← clusters_active
mw-home-trust-n">5          ← locales_supported
```

`24+` rendered. Inherited from `WebTemplate.objects.filter(tier=PUBLISHED_LIVE).count()` with zero template edit.

### 4.3 · Catalog band surfaces Cornice

```
$ curl -sS http://127.0.0.1:8052/templates/business/ | grep -c cornice-architettura
5
$ curl -sS http://127.0.0.1:8052/templates/business/ | grep -oE '[0-9]+ template (disponibili|disponibile)'
6 template disponibili
```

Slug appears 5 times on the anonymous business catalog page (card image src + name + cluster chip + detail link + customize link). Was 0 before the flip. Catalog header reads `6 template disponibili` (was 5).

### 4.4 · AR RTL parity preserved

```
$ curl -sS '...?lang=ar' | grep -oE 'html lang="[^"]+"|dir="[^"]+"'
html lang="ar"
dir="rtl"
dir="rtl"
dir="rtl"
dir="rtl"
```

LF-2-scoped Naskh swap on h1 still applies and the cluster default Amiri body font is preserved. Live DOM probe at §4.6 below confirms the computed font on h1 = `Noto Naskh Arabic` and on body = `Amiri`.

### 4.5 · Staff-preview legacy flag remains benign

```
GET /templates/business/cornice-architettura/preview/?preview=1            → 200
GET /templates/business/cornice-architettura/preview/?lang=ar&preview=1    → 200
```

The `?preview=1` flag is now a no-op pass-through: any internal link the corporate-suite chrome may still propagate from a stale staff session continues to work. The D-055 anonymous gate is no longer triggered for this slug because `tier=published_live` short-circuits it upstream.

### 4.6 · Playwright DOM probes (anonymous · fresh viewport)

```
IT home  · htmlLang=it    htmlDir=ltr   bodyClass=cs-lf-lf-2 lm-ready
                         navClass=cs-nav cs-nav--lf2
                         navBg=rgb(238,240,243)              (LF-2 cream)
                         h1Text="Ogni progetto è un argomento costruito, non un servizio reso."
                         h1Em="argomento"
                         h1FontFamily=Cormorant Garamond, Georgia, ...
                         inner=1440  docWidth=1425           (zero overflow)

AR home  · htmlLang=ar    htmlDir=rtl   bodyClass=cs-lf-lf-2 lm-ready
                         navClass=cs-nav cs-nav--lf2
                         navBg=rgb(238,240,243)              (LF-2 cream · same as LTR)
                         h1Text="كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة."
                         h1Em="حُجَّة"
                         h1FontFamily="Noto Naskh Arabic", "Cormorant Garamond", ...
                         bodyFontFamily=Amiri, "Source Sans 3", system-ui
                         inner=1440  docWidth=1425           (zero overflow)
```

DOM values reproduce the workflow D walk verbatim under the new anonymous tier.

### 4.7 · Frozen-sibling regression spot-check

```
GET /templates/business/pragma-corporate-suite/preview/                   → 200
GET /templates/business/fiscus-commercialista/preview/                    → 200
GET /templates/business/solaria-coaching/preview/                         → 200
GET /templates/business/continua-stewardship/preview/                     → 200
```

Cluster mates unaffected. Continua AR LF-5 spot-probe (Playwright):

```
bodyClass=cs-lf-lf-5 lm-ready          (NOT lf-2 → Naskh override does not match)
h1FontFamily="Noto Kufi Arabic", "Crimson Pro", Georgia, serif
                                       (cluster default Kufi PRESERVED · zero Naskh leakage)
htmlDir=rtl
```

This is the load-bearing proof that Cornice's LF-2-scoped Naskh swap still does not leak into Continua's LF-5 RTL render after the flip.

---

## 5 · Files changed (full list)

### Source / config (2 files):

```
TEMPLATE_REGISTRY.json
  · Cornice row · tier draft → published_live
  · tier_reason rewritten to consolidate workflow A.5→D + public flip audit trail

apps/catalog/tests.py
  · L824  · qs.count() literal       23 → 24
  · L862  · counts["total"] literal  23 → 24
  · L868  · has_rtl literal          23 → 24
  · L1134 · templates_live literal   23 → 24
  · L1141 · "23+" literal            "23+" → "24+"
  · L1554 · qs.count() literal       23 → 24
  · L1556 · counts["total"] literal  23 → 24
  · L1265 · test_pragma_falls_back_gracefully · default limit → limit=4
                                       (preserves intent of layered fallback test
                                        post-Cornice promotion)
```

### Reports / scorecards (4 + 2 = 6 docs + 4 captures):

```
factory/reports/cornice/cornice-public-flip.md                                   (this file)
factory/reports/browser-verification/cornice-public-flip.md                      (browser walk index)
factory/reports/browser-verification/cornice-public-flip/captures/
   it-1440-anon-firstscroll.png
   ar-1440-anon-firstscroll.png
   home-1440-anon-trust-counter-24plus.png
   business-catalog-1440-anon-cornice-card.png
factory/reports/scorecard/cornice-public-flip/build-report.md
factory/reports/scorecard/cornice-public-flip/browser-verifier.md
factory/reports/scorecard/cornice-public-flip/release-gatekeeper.md
factory/reports/scorecard/cornice-public-flip/summary.md
```

### Memory rollup:

```
C:/Users/badrw/.claude/projects/C--tmp-sitoBadr2-marketweb/memory/MEMORY.md
C:/Users/badrw/.claude/projects/C--tmp-sitoBadr2-marketweb/memory/phase_x5_cornice_public_flip.md
```

---

## 6 · Final state

| Field | Pre-flip | Post-flip |
|---|---|---|
| Registry · `tier` | `draft` | **`published_live`** |
| Registry · `status` | `published` | unchanged (was already `published`) |
| Registry · `locales` | `[it,en,fr,es,ar]` | unchanged |
| Registry · `rtl` | `true` | unchanged |
| DB · `WebTemplate.tier` (Cornice) | `draft` | **`published_live`** |
| DB · catalog distribution | 23 live / 1 draft | **24 live / 0 draft** |
| Anonymous `/templates/business/` slug | absent | **present (5× in HTML)** |
| Anonymous `/templates/business/` count | "5 template disponibili" | **"6 template disponibili"** |
| Anonymous `?lang=*` reachability | 404 anon · staff-only | **200 all 5 locales** |
| Anonymous case-detail posts | 404 anon | **20/20 200 (5 locales × 4 posts)** |
| Home `templates_live` counter | `23+` | **`24+`** |
| Test suite | 545 / 546 | 545 / 546 (same pre-existing failure) |
| Pragma / Fiscus / Solaria / Continua | 200 / 200 / 200 / 200 | 200 / 200 / 200 / 200 |
| Continua AR h1 fontFamily (Naskh leak check) | `Noto Kufi Arabic` | `Noto Kufi Arabic` (zero leak) |

**Cornice is now fully `published_live`.** The corporate-suite cluster ships **5 live siblings** (Pragma LF-1 + Fiscus LF-3 + Solaria LF-4 + Continua LF-5 + Cornice LF-2) at full multilingual parity with all 5 layout-family slots populated.

---

## 7 · Server posture at landing

```
$ python manage.py runserver 127.0.0.1:8052 --noreload
```

Listening at **http://127.0.0.1:8052/**. Server left running for any user-side post-flip verification. URL/port preserved on the scorecard.

Anonymous URLs to walk:

```
http://127.0.0.1:8052/                                                              (home · 24+ counter)
http://127.0.0.1:8052/templates/business/                                           (catalog · Cornice card)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/              (IT)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=en      (EN)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=fr      (FR)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=es      (ES)
http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?lang=ar      (AR · RTL · Naskh h1 · Amiri body)
```

No staff session required.
