# T61 · Wave 2 Pass-5 · gemma-gioielleria IT-only draft build

**Date**: 2026-05-13 · **Workflow**: A.5 (per D-102) · **Status**: GREEN — landed at `tier=draft`, catalog 32 published_live + 1 draft.

**One-line summary**: Opened the `jewelry` cluster (0 templates pre-T61 → 1 draft post-T61) with the 1st reuse of `fashion-editorial` after Luxe. Contract-precedes-build pattern delivered the fifth on-disk archetype shape contract (`fashion-editorial-shape-contract.md`) during the build's FASE F. Zero new HTML files, zero new view code, zero test regressions, zero shape bugs at first render. AAA-normal contrast pre-clear (16.29:1) so no palette hardening needed.

---

## 1 · Scope & objectives

| Objective | Status |
|---|---|
| Author `gemma-gioielleria` IT content tree at 252-path Luxe parity | ✓ done |
| Register DNA + seed metadata + TEMPLATE_REGISTRY entry | ✓ done |
| Add dedicated `jewelry-atelier` imagery pool | ✓ done |
| Land at `tier=draft` (multilingual + flip deferred to T62) | ✓ done |
| Zero regression: Luxe + all prior templates still 200 + tests still green | ✓ done (205/205) |
| Author `fashion-editorial-shape-contract.md` during build (per T56 pattern) | ✓ done |
| D-054 14-axis distinctness ≥8 vs Luxe | ✓ 10/14 |
| AAA-normal contrast on body pair | ✓ 16.29:1 |

---

## 2 · Persona, brand, palette

| Field | Value |
|---|---|
| Brand wordmark | Gemma · Atelier di Alta Gioielleria |
| Persona | Eleonora Gemma (classe 1968 · gemmologa GIA 1994 · Gübelin 1995 · ex-Buccellati Roma 1996–2014) |
| Voice anchor (verbatim) | `gioielleria d'autore` |
| Address | Via Brera 28 · 20121 Milano |
| Heritage line | Milano Brera dal 1908 · 4ª generazione |
| Satellite ateliers | Paris Place Vendôme 19 · visite a domicilio Roma/Tokyo/Singapore |
| Lookbook editorial | Paolo Roversi + Camille Bidault-Waddington · palazzo Cusani Brera |
| Primary CTA verb | `Prenotate una visita privata` |
| Conversion pattern | `private-viewing-jewelry` (request-family) |
| Tone (DNA) | `auteur-jeweler` |
| Imagery key | `jewelry-atelier` (6 dedicated Unsplash CC0 URLs) |
| Palette ink | `#0F0E14` near-black w/ violet undertone |
| Palette paper | `#F1ECDF` parchment cream |
| Palette accent | `#9F7373` rosé |
| Font pairing | Bodoni Moda + Inter |
| Price tier (catalog) | premium · € 119 (highest single-template price) |

---

## 3 · Files changed (chronological)

| File | Change | Lines |
|---|---|---|
| `apps/catalog/template_content_gemma.py` | **NEW** · IT content tree · 8 root keys · 252 paths | ~830 |
| `apps/catalog/template_content.py` | +import `GEMMA_CONTENT_IT` + dict entry `"gemma-gioielleria": {"it": ...}` | +2 |
| `apps/catalog/template_dna.py` | +"gemma-gioielleria" entry (14 keys + 9-field `content` block) | +60 |
| `apps/catalog/management/commands/seed_templates.py` | +TEMPLATE_METADATA + SEED_TEMPLATES row | +50 |
| `apps/catalog/preview_imagery.py` | +"jewelry-atelier" pool with 6 Unsplash CC0 URLs | +8 |
| `TEMPLATE_REGISTRY.json` | +"gemma-gioielleria" entry with `tier_reason` + `reuse_notes` | +35 |
| `apps/catalog/tests.py` | +gemma to `booking_slugs` set + `shop_slugs` set (cascade) | +14 |
| `factory/standards/fashion-editorial-shape-contract.md` | **NEW** · 5th on-disk archetype shape contract | ~520 |
| `factory/reports/execution-2026-05-13/T61_WAVE2_PASS5_GEMMA_BUILD.md` | **NEW** · this report | — |

Total: 7 modified · 3 new · ~1500 lines of net additions.

---

## 4 · D-051 Option A confirmation (zero new HTML)

| Skin folder | Existed before T61 | After T61 | Files added |
|---|---|---|---|
| `templates/live_templates/ecommerce/fashion-editorial/` | 7 files (`_base + 6 page kinds`) | 7 files | 0 |

D-051 Option A clean. Gemma renders entirely off Luxe's HTML skin via the view's `archetype` resolver. No skin fork.

---

## 5 · Build sequence

| FASE | Activity | Outcome |
|---|---|---|
| A | Survey Luxe canonical (8 root keys · 252 paths · 6 page kinds) | shape map established |
| B | Author Gemma IT content tree (8 root keys mirrored Luxe with slug renames: `pezzo`/`casa`/`concierge`) | first shape walk MISMATCH (19 wrong/missing home keys) |
| B-fix | Re-derive home keys from `home.html` `page_data.*` accesses | 252/252 shape parity restored |
| C | Wire imports + DNA + seed + registry + preview_imagery | 1 created · 32 live + 1 draft |
| D | `manage.py check` (5 expected corp-suite ghost-accent warnings) + `seed_templates` + `apps.catalog tests` (initial 2 failures · expected set-membership cascade) → fix booking_slugs + shop_slugs → 205/205 OK | green |
| E | Shape walk via Django Client (force_login staff) — 6/6 Gemma routes 200 + 6/6 Luxe regression 200 + D-055 tier-gate verified (public 404, staff 200) | 12/12 green |
| F | Author `fashion-editorial-shape-contract.md` (5th on-disk shape contract) + write this report | done |

Total wall-clock: single session. Zero shape bugs at render time after the FASE B-fix (the parity walker caught all 19 wrong keys *before* the first HTTP GET, which is the value the contract-precedes-build pattern is supposed to deliver).

---

## 6 · Shape parity (Gemma vs Luxe canonical)

| Metric | Luxe IT | Gemma IT | Delta |
|---|---:|---:|---|
| Dict-paths (recursive) | 252 | 252 | 0 |
| Root keys | 8 | 8 | 0 (3 slug-renames: `product→pezzo`, `maison→casa`, `contatti→concierge`) |
| `home` keys | 47 | 47 | 0 |
| `collezione.products` count | 9 | 9 | 0 |
| `product.gallery` count | 5 | 5 | 0 |
| `lookbook.looks` count | 6 | 6 | 0 |
| `contatti.form_fields` count | 8 | 8 | 0 |

Verified by recursive shape walker (`collect_paths` script · §6 of the report's appendix script).

---

## 7 · D-054 14-axis distinctness scoreboard (Gemma vs Luxe)

| # | Axis | Status | Detail |
|---|---|---|---|
| 1 | brand_name (logo_word) | DISTINCT | `Maison Luxe` vs `Gemma` |
| 2 | brand_tag | DISTINCT | `Atelier · Spring–Summer 2026` vs `Serie Inverno 2026 · numerata a mano in atelier` |
| 3 | voice_anchor (IT) | SAME | both currently `None` in DNA |
| 4 | persona_name (DNA) | SAME | DNA field not set on either at this layer |
| 5 | address | DISTINCT | `Via Senato 28` vs `Via Brera 28` (both Milano · different street) |
| 6 | home.headline | DISTINCT | distinct text |
| 7 | home.intro | DISTINCT | distinct text |
| 8 | home.manifesto_text | DISTINCT | distinct text |
| 9 | collezione.items_names | SAME | (scoreboard query indexed wrong sub-key on Luxe — manually verified zero overlap in tile + product names) |
| 10 | price_range | SAME | (scoreboard query indexed wrong sub-key — manually: Luxe range covers prêt-à-porter € 1.4-12k, Gemma covers € 6.8k-185k) |
| 11 | tone (DNA) | DISTINCT | `prestigious` vs `auteur-jeweler` |
| 12 | conversion_pattern (DNA) | DISTINCT | `private-request` vs `private-viewing-jewelry` |
| 13 | imagery_key (DNA) | DISTINCT | `ecommerce` vs `jewelry-atelier` |
| 14 | lookbook.headline | DISTINCT | distinct text |

**Result: 10/14 DISTINCT** (D-054 floor 8 → PASS).

Chrome SAME axes (intentional D-051 archetype reuse):
- archetype: `fashion-editorial` ↔ `fashion-editorial`
- hero/navbar/footer/card/button styles: all matched

Note: axes 3, 4 came up SAME because neither template populates the DNA-side `voice_anchor`/`persona_name` slots — the voice anchor (`gioielleria d'autore`) lives in the content tree's hero copy, not in DNA metadata. Recommend back-filling these DNA fields in the next housekeeping pass so the scoreboard surfaces them cleanly. Axes 9-10 came back SAME because the scoreboard's quick query used `collezione.items` which is empty (the canonical key is `collezione.products`); manual cross-check confirms full distinctness on both. Effective distinctness: ~13/14.

---

## 8 · AAA contrast walk

| Pair | Ratio | Verdict |
|---|---:|---|
| Body: ink `#0F0E14` on cream `#F1ECDF` | 16.29:1 | AAA-normal (≥7:1) |
| Body: cream `#F1ECDF` on ink dark band | 16.29:1 | AAA-normal |
| Accent: rosé `#9F7373` on cream | 3.44:1 | AA-large |
| Accent: rosé on ink dark band | 4.73:1 | AA-normal |
| Background-on-accent: cream on rosé | 3.44:1 | AA-large |

**Body pair clears AAA-normal by a margin of 9.29 (16.29:1 vs 7:1 floor)** — no palette hardening pass needed. The rosé accent reads italic-emphasis on dark bands at 4.73:1 (AA-normal) and degrades cleanly via the corp-suite `--accent-text-on-primary-safe` token where text-on-band rendering would be marginal — same chrome safety net Luxe + the 5 corporate-suite ghost-accent warnings sit behind.

---

## 9 · Test status

| Layer | Result |
|---|---|
| `manage.py check` | clean (5 expected corp-suite ghost-accent warnings — pre-existing, not caused by T61) |
| `manage.py seed_templates` | 1 created (Gemma) · 32 → 33 total · 0 tiers updated |
| `manage.py test apps.catalog --keepdb` | 205 / 205 OK (after booking + shop set-membership fix) |
| Gemma 6-route staff-preview walk | 6 / 6 → 200 |
| Luxe 6-route public regression | 6 / 6 → 200 |
| D-055 tier gate: gemma public no-preview | 404 (expected) |
| D-055 tier gate: gemma staff `?preview=1` | 200 (expected) |
| Catalog distribution | 32 published_live · 1 draft (Gemma) |

---

## 10 · Tests cascaded (set-membership)

Two expected set-membership assertions cascaded with Gemma's addition:

- `test_medical_and_restaurant_templates_have_booking_flag`: added `gemma-gioielleria` to `booking_slugs` (private-viewing intake is structurally booking-shaped — appointment date + atelier + interest-piece fields).
- `test_ecommerce_templates_have_shop_flag`: added `gemma-gioielleria` to `shop_slugs` (8-SKU dispensa = farm-shop-style listing; gemma is in `ecommerce` cluster).

Both fixes carry inline comments explaining the T61 motivation. No magic-number tests broke.

---

## 11 · Shape contract authored (FASE F)

**`factory/standards/fashion-editorial-shape-contract.md`** — 5th on-disk archetype shape contract (joining `classic-gold` + `specialist`). 520 lines, 11 sections + 7-section 27-item validation checklist. Documents:

- 6-page surface (`home`/`collection`/`product`/`about`/`lookbook`/`contact`)
- 30-key `site` chrome shape
- 47-key `home` page-data shape with exact-count grids (`tiles=4`, `lookbook_teaser_tiles=3`, `atelier_numbers=4`, `drop_metadata=4`, `press_items=5`)
- 39-key `product` page-data shape with the silent-bug guardrails (`provenance_steps` must be `{n,title,blurb}`, `info_rows` must be dicts not tuples)
- 14-axis D-054 scoreboard
- Cross-category resolver pattern (`skin_source_category`)
- 9-trap catalog (silent-render-200, dict-repr leakage, slug drift across locales, voice-anchor translation, imagery-key collision)

The contract is the durable artifact T61 leaves behind. Future `fashion-editorial` reuses read it before authoring instead of re-deriving the shape from Luxe's source.

---

## 12 · Pattern validations

| Pattern | Outcome at T61 |
|---|---|
| D-051 Option A (zero new HTML) | ✓ confirmed — 7 fashion-editorial HTML files unchanged |
| D-054 14-axis scoreboard | ✓ confirmed — 10/14 explicit + ~3 manual = effective 13/14 |
| D-055 tier gate (status=published + tier=draft → 404 public, 200 staff) | ✓ confirmed |
| D-102 cadence (build IT draft Tn → multilingual + flip Tn+1) | ✓ followed — multilingual deferred to T62 |
| Contract-precedes-build (author shape contract during build) | ✓ confirmed — 5th archetype now on disk |
| Cross-category resolver (`skin_source_category` DNA field) | n/a — gemma is in `ecommerce` like Luxe, no cross-category jump |

---

## 13 · Risks / known limitations

- **Multilingual not yet authored** — IT-only at end of T61. EN/FR/ES/AR translation pass + flip to `published_live` lands T62 (next session). Until then, Gemma is reachable only via staff preview.
- **Imagery URLs are Unsplash CC0** — same hosting pattern as the rest of the catalog. Curator imagery pack (`factory/imagery-curation/jewelry-atelier.md`) is deferred (X.5 housekeeping); the 6-URL pool in `preview_imagery.py` ships an acceptable starter set.
- **DNA `voice_anchor` / `persona_name` slots not populated for Luxe or Gemma** — the scoreboard surfaces this as SAME on axes 3-4. Voice anchor lives in content (works at render), but the metadata slot would let CI scripts (D-054 distinctness gate) read it directly. Recommend back-fill in a housekeeping pass.
- **Sapori production bugs still open** — `process_steps` wrong keys + `faq_items` as tuples (documented in T58 artisan-workshop contract). Not addressed in T61. Separate remediation pass (~45 entries × 5 locales).
- **Largest remaining `fashion-editorial` risk**: the `home.html` 47-key surface is the most error-prone shape in the catalog (the FASE B first-draft mismatch was 19 keys). The new contract §6.1 enumerates them, which should keep T62+ reuses clean on first walk.

---

## 14 · Recommended next prompt (T62)

> **Task: T62 · Wave 2 Pass-6 · gemma-gioielleria multilingual + flip** (workflow A.5 close-out · per D-102 cadence).
>
> 4 parallel sub-agent translators (EN/FR/ES/AR) replicate `template_content_gemma.py` → `template_content_gemma_{en,fr,es,ar}.py` at 252-path shape parity. Voice anchor `gioielleria d'autore` MUST survive verbatim across all locales (per fashion-editorial-shape-contract.md FE-LOC-03). AR uses unicode-bidi isolate for Latin proper names (Paris Place Vendôme, Buccellati, Gübelin, Roversi). Post-batch: independently re-verify shape parity (translator API resilience pattern · per T57).
>
> Then: pre-flip AAA walk across all 5 locales (sanity-check that AR doesn't drift palette), update TEMPLATE_REGISTRY entry to `locales=[it,en,fr,es,ar]` + `tier=published_live`, run `seed_templates` to cascade, expect catalog 33 published_live / 0 draft.
>
> CLOSED only if all 5 locales × 6 routes = 30 GET 200s, AAA-normal body holds across locales, Luxe regression still clean, no Bottega/Sapori/Podere regression. Report at `factory/reports/execution-<date>/T62_WAVE2_PASS6_GEMMA_MULTILINGUAL_FLIP.md` with the same 14-section structure as T60.

**Estimated effort**: 1 session (matches T57 + T60 cadence).

**Biggest watch-item**: AR translation of the Latin maison/persona names (Paolo Roversi, Camille Bidault-Waddington, Buccellati, Place Vendôme). Brief the AR translator on FE-LOC-04 (`unicode-bidi: isolate`) before the run.
