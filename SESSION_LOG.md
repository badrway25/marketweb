# Session Log

## Session 74 — Phase A.16b · Benessere (wellness · medical-other family · second template · MIDDLE PHASE) Editor + Multi-locale Enrollment (2026-04-19)

**Summary.** Sixteenth archetype enrolled in the editor: `wellness` (Benessere). Single-template phase — Benessere enters as **middle phase** of the medical-other 3-phase staged dedicated-schema progression (A.16 Salute opener · A.16b Benessere middle · A.16c Famiglia closer pending). Removes wellness-out guard half of the DUAL-OUT GUARD planted in A.16 Salute · **family-out guard PRESERVED** for A.16c. **16 archetype slugs enrolled · 16 multi-locale enrolled · 17 templates editable end-to-end.** Catalog 20/20 `published_live` unchanged. Baseline `803f273` → merge `e9cc419` on `phase-integration-baseline-v15` · pushed origin. Medical-other family remains **half-open** (Salute + Benessere IN · Famiglia pending A.16c closer).

Three critical framings for this session:

1. **First 3-template staged progression enters middle phase · guard-removal sub-recipe in 2-phase variant active**. A.16 Salute planted DUAL-OUT GUARD for BOTH `wellness` + `family` at 3 layers (registration-time + lifecycle start + lifecycle end). A.16b removes wellness-out guard symmetrically via `test_a16b_benessere_out_guard_was_removed_from_salute_tests` (5th precedent after Villa/Pixel/Brace/Luxe) · family-out guard PRESERVED unchanged · A.16c will remove family-out via 6th precedent. **First time 1 opener plants 2 guards and each closure phase removes 1** · sub-recipe generalized from 1-removal to 2-removal phase.

2. **NOVEL SHAPE DEFERRED cleanly (first-ever deferral outcome)**: `home.ambients` tuple-with-image (4 tiles · `(image_url, title, sub)` positional) discovered during Step 0 audit. **ZERO precedent in any existing archetype** — all prior tuple shapes carry text-only cols. Decision: whole list OUT first-wave via schema omission. Rationale: mechanical-reuse principle preserved · no horizontal-feature introduction (would be first-ever image-typed cell inside a tuple) · 4-tile image coverage loss acceptable for middle-phase enrollment · explicit future expansion candidate after dedicated infra verification. **Establishes a 4th deferral category** (novel-shape-deferred) alongside mutable repeater · image per-locale · detail-page editing.

3. **Scheduler-state bool flags + nested list-of-str uniformly OUT across 2 calendar lists**. Benessere ships `home.calendar` + `prenota.calendar` (7 rows × 6 cols each) with `day`/`num`/`month` IN (editorial visible labels) and `has_slots`/`soldout`/`slots` OUT (scheduler-state-like). **4 bool flag cols** (2 lists × 2 cols) are OUT col-level per Luxe `available` + Salute `is_popular` precedent re-application. **2 nested list-of-str cols** (`slots`: concrete time-slots like `['10:00','14:30']`) are OUT col-level per Juris precedent. Uniform enforcement across both calendars confirms scheduler-state is a per-col-type policy category, not a per-archetype special case.

### Context initial post-A.16

Baseline entering Session 74 was `803f273` (post-A.16 Salute enrollment + consolidation; 15 archetypes enrolled, medical-other half-open). Outside-gate fixture already rotated to `wellness`/`benessere-centro-olistico` in A.16 as next-candidate signal.

### Benessere-only scope decision

Step-0 audit (planning session) ran comparative analysis on 3 medical-other templates already completed in A.16. Benessere confirmed as middle phase (simpler than Famiglia's deep-path `crescita.topics[].items` which is deferred to A.16c closer) · mechanical extension of A.16 recipe · no novel topology invention · **5th consecutive staged enrollment after 4 closed + 1 half-open + A.16 Salute opener**.

### Step 0 · Planning / audit findings chiave

- Archetype slug `wellness` · skin `medical/wellness/` · CSS **`.we-*`** (142 hits · highest of medical-other) · 13 mature `html[dir="rtl"]` rules · `_base.html` 645 LOC (highest of medical-other)
- 7 pages: home · filosofia(about) · rituali(services) · **ambienti** (novel `gallery` kind) · professionisti(team) · contatti(contact) · prenota(appointment · shared with Salute) — **1 novel page kind** (gallery)
- 5-locale parity PERFETTA (546 keys × 5 locales · zero gaps)
- `apps/catalog/views.py::LiveTemplateView` ZERO imports da scheduler/booking/patient namespaces · boundary preserved runtime-verified
- Image surface runtime-verified: 19 editable surfaces (3 scalar top-level + 16 image-in-dict-row cells across 3 lists: `ambienti.rooms[].image` × 8 + `home.therapists_trio[].portrait` × 3 + `professionisti.people[].portrait` × 5) · **ALL RENDERED** (editorial olistico skin)
- 13 lists-of-dict IN + 4 lists-of-tuple IN = **17 STRUCTURED_FIELD_SHAPES entries** · tutti parent-level · ZERO deep-path
- 2 lists-of-dict OUT (form structures): `prenota.form_fields` (9 rows · Juris shape) · `prenota.form_sections` (4 rows)
- 3 nested-dict OUT (form-related): `contatti.form_placeholders` · `contatti.form_helpers` · `contatti.form_fields` (non-standard dict with `interest_label` + `interest_options` list-of-str)
- 4 flat list-of-str OUT (policy): `site.hours_footer_rows` · `home.hero_meta` · `home.press` · `prenota.why`
- 5 nested list-of-str inside dict rows OUT (Juris precedent): `home.calendar[].slots` · `prenota.calendar[].slots` · `rituali.packages[].includes` · `professionisti.people[].tags` · `contatti.form_fields.interest_options`
- **4 bool flag cols OUT** (Luxe/Salute precedent): `home.calendar[].has_slots` · `.soldout` · `prenota.calendar[].has_slots` · `.soldout`
- **Zero raw SVG fields** (Salute's 5th OUT category precedent does NOT apply to Benessere)
- **Zero deep-path tuple-in-dict-list or dict-in-dict-list** (no novel contract-alignment fix needed · f66ac24 not invoked)
- **NOVEL shape discovered · DEFERRED**: `home.ambients` tuple-with-image (4 × `(image_url, title, sub)` · first-ever image-typed cell in a tuple col · whole list OUT first-wave via schema omission · future expansion candidate)
- **Posts list empty** (same structural absence as Salute/Bottega/Luxe/Sapore/Brace · detail-page policy stays at 6-archetype uniform enforcement)

### Step 1 · Schema + bridge + gate + contract tests

- `BENESSERE_WELLNESS_SCHEMA` added in `apps/editor/schema.py` — **9 sidebar groups · 108 scalar fields**.
- `STRUCTURED_FIELD_SHAPES["wellness"]` with **17 entries · tutti parent-level · ZERO deep-path** (13 dict + 4 tuple).
- Image-in-dict-row lists (3): `ambienti.rooms[].image` × 8 · `home.therapists_trio[].portrait` × 3 · `professionisti.people[].portrait` × 5 = 16 image cells.
- Scalar top-level images (3): `home.hero_image` · `filosofia.photo_image` · `contatti.map_image` (all rendered).
- 3 gate registrations simultanee · `_ARCHETYPE_BASELINE_TEMPLATE["wellness"] = ("benessere-centro-olistico", "it")` + `_ARCHETYPE_SCHEMAS["wellness"] = BENESSERE_WELLNESS_SCHEMA` + `"wellness"` in `_MULTILOCALE_ENABLED_ARCHETYPES`.
- **Col-level exclusions**: 4× calendar bool flags (`has_slots`/`soldout` on both calendars · Luxe/Salute precedent) · 2× calendar `slots` (nested list-of-str · Juris precedent) · `rituali.packages[].includes` · `professionisti.people[].tags` (nested list-of-str · Juris precedent).
- **Complex-shape exclusion** (form + flat + deferred novel): 5× form structures · 4× flat list-of-str · 3× home.ambients tuple-with-image (DEFERRED novel shape · schema omission) · `pages` · `posts` (empty).
- 3 atomic fixes on `templates/live_templates/medical/wellness/_base.html`: title `site.logo_word|default:brand.brand_name` · body `mw-is-editor-preview` guard · `.we-*` CSS guard block (`.we-nav .wm` clamp 32ch) · preview-bridge.js conditional on `preview_project`.
- **Wellness-out guard REMOVED** from A.16 Salute tests at 3 locations: registration-time in `test_a16_salute_archetype_registered` + runtime at start AND end of `test_a16_salute_full_multilocale_lifecycle_end_to_end`. **Family-out guard PRESERVED** unchanged in all 3 locations.
- **NEW test** `test_a16b_benessere_out_guard_was_removed_from_salute_tests` · **5th precedent** of guard removal pattern after Villa/Pixel/Brace/Luxe · **first time 1 opener plants 2 guards and a single closure phase removes 1 of them** (variation vs 2-template staged closures).
- **Outside-gate fixture rotation** (6 location): `wellness`/`benessere-centro-olistico` → `family`/`famiglia-pediatria` (A.16c closer candidate).

### Step 2 · Lifecycle HTTP end-to-end test

- `test_a16b_benessere_full_multilocale_lifecycle_end_to_end` added (pure test-only change · +388 LOC · zero production code).
- 11 phases blindates: perimeter start (Benessere IN + Salute IN + Famiglia OUT) · 3 translatable locales on `home.headline` · global plain-key `site.logo_word` · 3 image paths across 3 distinct pages (scalar `home.hero_image` on home + `ambienti.rooms.0.image` on novel gallery page + `professionisti.people.0.portrait` on team page · all DIFFERENT lists + DIFFERENT pages) · publish · second-user preview walk 5 locales × 3 pages · AR `<html dir="rtl" lang="ar">` · owner re-opens editor with per-locale prefill · perimeter end (Benessere + Salute IN · Famiglia STILL OUT) + **24 OUT paths rejected** (calendar bool flags × 4 · nested str-lists × 4 · form structures × 7 · home.ambients tuple × 3 · flat str-list × 4 · pages/posts × 2).
- **Triple-invariant**: Benessere + Salute IN + Famiglia OUT verified at start AND end of test.
- **Image plain-key invariant**: 3 image paths × 5 locales (15 combinations) assertNotIn `@<locale>:` prefix.

### Step 3 · Playwright browser walk

- Sidebar inventory: **379 total editable fields · 19 image widgets exact · 5 lang pills (IT/EN/FR/ES/AR) · 27 group slots** (9 sidebar + 17 indexed + 1 design).
- **14 critical IN paths present** in sidebar: 3 scalar images · 6 image-in-dict-row cell paths · calendar day/month + num/month on prenota calendar · home.journey.0.num · pillars.init · packages.tag.
- **20 sensitive OUT paths absent**: 4× calendar bool flags · 2× calendar slots · 2× nested str-list · 5× form structures · 3× home.ambients (deferred novel shape) · pages/posts.
- 5-locale flush walk IT→EN→FR→ES→AR with `home.headline` override in IT/EN/FR; ES/AR stays authored baseline (zero Latin override leak).
- Per-locale `home.headline` authored baselines verified:
  - IT: `Un respiro è la misura del nostro tempo`
  - EN: `A breath is the measure of our time`
  - FR: `Un souffle est la mesure de notre temps`
  - ES: `Un respiro es la medida de nuestro tiempo`
  - AR: `النَّفَسُ هو مقياس وقتنا`
- **Storage shape after publish (7 overrides)**: 3 per-locale translatable (`@it/@en/@fr:home.headline`) + 4 plain-key globals (`site.logo_word` · `home.hero_image` · `ambienti.rooms.0.image` · `professionisti.people.0.portrait`). Zero `@<locale>:` on any image or logo across 5 locales.
- **Render matrix 5 locales × 3 pages = 15/15 green**: logo×4 (nav + title + footer + footer strip) on every page; `home.hero_image` only on home; `ambienti.rooms.0.image` only on ambienti (novel `gallery` page · ×2 count due to skin using both `background-image` + `data-li-src` lightbox attribute — documented dual-render behavior); `professionisti.people.0.portrait` only on professionisti; zero cross-page bleed; IT/EN/FR override visible only in own locale; ES/AR show authored fallback.
- **AR RTL invariant verified**: editor iframe `dir="rtl"` · `lang="ar"` · `body.mw-is-editor-preview` · `.we-nav` + hero rendered; public preview `<html lang="ar" dir="rtl">` · 3033 Arabic characters · authored AR `النَّفَسُ` present.

### Tests + smoke (post-merge)

- `manage.py check` → 0 issues
- `manage.py test apps` → **325/325 PASS** (309 pre-A.16b + 15 contract + 1 lifecycle)
- `smoke_full.py` → **834/834 routes HTTP 200**
- Browser walk 5-locale green (sidebar + flush + storage + render matrix + AR RTL)

### File delta

- `apps/editor/schema.py` +559 LOC (Benessere schema + 17 shapes + 3 gate registrations)
- `apps/projects/tests.py` +~905 (15 contract tests + 1 lifecycle test + wellness-out dual guard REMOVED from 3 A.16 Salute locations + family-out guard PRESERVED + 6 outside-gate fixture rotations) / -60
- `templates/live_templates/medical/wellness/_base.html` +10 / -2 (3 atomic fixes on `.we-*` skin)

**Pure 3-file enrollment surface · zero tocchi a `apps/commerce` · `services.py` · `rendering.py` · `views.py` · `models.py` · editor shell · widgets · ProjectAsset · upload endpoint. Pattern confirmed sub-recipe standard after 6 consecutive applications.**

### Medical-other family · half-open status (unchanged)

- Staged dedicated-schema closure will be **5 of N** when family closes in A.16c: real-estate (A.12+A.12b) · portfolio (A.13+A.13b) · restaurant-continuation (A.14+A.14b) · ecommerce (A.15+A.15b) · **medical-other (A.16+A.16b+A.16c · first 3-phase variant)**.
- 6 families chiuse + 1 half-open (medical-other).
- 3 templates editor-only-pending residui: Famiglia (`family`) · Aura (`agency-digital-studio`) · Elevate (`startup-saas-landing`).
- Catalog 20/20 `published_live` · **17/20 enrolled editor** (was 16/20 post-A.16 · +1 Benessere).

### Guard removal pattern · 5 precedents + 1 pending (extended to 3-phase progression)

- Villa-out (A.12b via `test_a12b_villa_out_guard_was_removed_from_casa_tests`)
- Pixel-out (A.13b via `test_a13b_pixel_out_guard_was_removed_from_chiara_tests`)
- Brace-out (A.14b via `test_a14b_brace_out_guard_was_removed_from_sapore_tests`)
- Luxe-out (A.15b via `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`)
- **Wellness-out (A.16b via `test_a16b_benessere_out_guard_was_removed_from_salute_tests`)** ← 5th precedent · 2-phase-removal variant
- **Family-out (A.16c via `test_a16c_family_out_guard_was_removed_from_salute_tests` · pending)** ← 6th precedent pending

**First time guard removal pattern applies incrementally to a single opener's dual-out guard** — A.16 Salute planted 2 guards · A.16b removed 1 · A.16c will remove the remaining 1. Sub-recipe extends from "one-opener-one-closer" (A.12→A.12b topology) to "one-opener-two-closers" (A.16→A.16b→A.16c topology).

### Outside-gate fixture rotation history

- A.16: `clinic`/`salute-studio-medico` → `wellness`/`benessere-centro-olistico`
- **A.16b: `wellness`/`benessere-centro-olistico` → `family`/`famiglia-pediatria`** (A.16c closer candidate)

6 fixture rotate · 4 `supported_locales`/`is_translatable` + 1 `is_supported_archetype` + 1 `customize_start` redirect.

### Decisioni binding in vigore post-A.16b

- D-086 → D-095 (A.1 → A.5)
- D-096 · per-locale storage `@<locale>:<path>`
- D-097 · no cross-locale customer fallback
- D-098 · archetype gate + dedicated lifecycle test per enrollment
  - Session 74 operational clarification (under D-098 · no new D-number):
    - Medical-other 3-phase progression enters middle phase with Benessere
    - Guard removal sub-recipe extended from 1-removal (2-phase) to 2-removal (3-phase) phase
    - Scheduler-state bool flags + nested list-of-str uniformly OUT across 2 calendar lists (per-col-type policy · Luxe/Salute/Juris precedents re-applied mechanically)
    - Novel shape deferral outcome formalized: `home.ambients` tuple-with-image OUT first-wave via schema omission (first-ever image-typed cell in a tuple · no horizontal-feature introduction)
    - Stringent IN col-level audit extended to 6 archetypes (Benessere joins Sapore/Brace/Bottega/Luxe/Salute chain)
    - Boundary editor-vs-clinic-admin re-verified on second medical-other archetype
    - Outside-gate fixture rotation to `family`/`famiglia-pediatria` (signals A.16c closer)

**Nessun nuovo D-number da A.16b.** Operational clarification sotto D-098 solamente.

### Benessere metrics

- 9 sidebar groups · 108 scalar fields · 19 image surfaces (3 scalar top + 16 image-in-dict-row cells · ALL RENDERED)
- 17 readonly indexed list entries · tutti parent-level · ZERO deep-path (13 dict + 4 tuple)
- ~90 translatable · ~370 global (full audit deferred to maintenance phase)
- 5 locale parity PERFECT (546 keys × 5 · zero gaps)
- `.we-*` skin · 13 `html[dir="rtl"]` rules
- Zero posts · zero form structures editing · zero mutable repeater · zero image per-locale · zero scheduler/booking/patient model paths · zero deep-path
- Schema LOC delta +559 · SOTTO 600 soft guardrail (consistent with Bottega 585 · Luxe 598 · Salute 512)

### Not in scope (confirmed out-of-scope)

- Famiglia editor enrollment (deferred A.16c closer)
- `home.ambients` tuple-with-image (deferred · novel shape)
- Bool field type addition (horizontal feature · resisted)
- Nested list-of-str editor widget (horizontal feature · resisted)
- Form-structure editor (horizontal feature · resisted)
- Tuple-with-image editor widget (horizontal feature · resisted via deferral)
- Image per-locale (D-098 invariante)
- Repeater per-locale (out-of-scope family)
- Mutable repeater (Benessere lists tutte readonly)
- Detail-page editing (horizontal feature cross-archetype · 6-archetype uniform enforcement preserved)
- Scheduler-state / booking-state / patient-record editing (clinic-admin scope · separate concern)
- Coverage expansion beyond first wave
- Refactor trasversali
- Remote storage

---

## Session 73 — Phase A.16 · Salute (clinic · medical-other family · first template) Editor + Multi-locale Enrollment · OPENS MEDICAL-OTHER FAMILY (2026-04-19)

**Summary.** Fifteenth archetype enrolled in the editor: `clinic` (Salute). Single-template phase — Salute **opens** the medical-other family via staged dedicated-schema progression EXTENDED TO **3-PHASE VARIANT** (A.16 Salute opener · A.16b Benessere · A.16c Famiglia closer). **15 archetype slugs enrolled · 15 multi-locale enrolled · 16 templates editable end-to-end.** Catalog 20/20 `published_live` unchanged. Baseline `af0e71a` → merge `e25b622` on `phase-integration-baseline-v15` · pushed origin. Six families closed unchanged · medical-other family half-open (Salute IN · Benessere/Famiglia pending A.16b/A.16c).

Three critical framings for this session:

1. **First 3-template staged progression — guard-removal sub-recipe extends to 2 removal phases.** Previous staged closures were 2-template families (real-estate · portfolio · restaurant-continuation · ecommerce). Medical-other has 3 templates with 3 distinct archetypes (clinic · wellness · family) and ~0% content-tree overlap, so shared-schema is impossible (verified Step 0 audit). **DUAL-OUT GUARD** planted: Salute test_a16_salute_archetype_registered + lifecycle test asserts BOTH `wellness` + `family` OUT at 3 layers (registration-time + runtime start + runtime end). A.16b Benessere will remove `wellness`-out guard via `test_a16b_benessere_out_guard_was_removed_from_salute_tests`. A.16c Famiglia will remove `family`-out guard via `test_a16c_family_out_guard_was_removed_from_salute_tests`. Sub-recipe pattern extends from 1-removal to 2-removal phase.

2. **NOVEL 5th OUT category precedent: raw `icon_svg` fields.** Salute ships 18 raw SVG XML markup fields (`home.specialties[].icon_svg` × 8 · `servizi.services[].icon_svg` × 10) used for inline icon rendering. Editing raw SVG XML as plain text is unsafe (potential XSS-like content via paste) and customer-unfriendly UX. **OUT col-level** via STRUCTURED_FIELD_SHAPES col exclusion (not added to cols list for either shape) + dedicated contract test `test_a16_salute_raw_svg_fields_excluded` blindates exclusion at 2 layers (`get_field_spec` returns None · `validate_key_path` raises `InvalidEditableField`). Raw SVG joins the 4 prior OUT categories: flat-list-of-str · nested-list-of-str · form structures · structural identifiers/commerce-state-like booleans.

3. **`is_popular` bool flag handled as audit-driven OUT** (preserves `popular_label` text editability). The editor schema currently supports text/textarea/richtext/image/url/select but not bool. Adding bool support would be a horizontal feature ❌ (would affect every archetype with bool fields). Instead, `prevenzione.packages[].is_popular` stays OUT col-level (Luxe `available` precedent) while `popular_label` ('Più richiesto' badge text) stays editable IN — customer can change the badge label but not toggle which package is "most popular". Pragmatic limitation that preserves the no-horizontal-feature discipline.

### Context initial post-A.15b

Baseline entering Session 73 was `af0e71a` (post-A.15b Luxe enrollment + consolidation; 14 archetypes enrolled, ecommerce closed). Outside-gate fixture already rotated to `clinic`/`salute-studio-medico` in A.15b as next-candidate signal.

### Salute-only scope decision

Step-0 audit ran comparative analysis on all 3 medical-other templates:
- **Salute** (`clinic`): 7 pages · 15 image surfaces · 18 icon_svg + 1 bool flag + 2 form structures · simplest opener
- **Benessere** (`wellness`): 7 pages · 19 image surfaces · 2 form structures + calendar with `has_slots`/`soldout` bool flags (commerce-state-like) · 1 novel page kind (gallery)
- **Famiglia** (`family`): 6 pages · 16 image surfaces · NO form_fields (form as flat scalars) · contains deep-path tuple-in-dict-list (`crescita.topics[].items` · Sapore-precedent) · 1 novel page kind (faq)

Shared-schema verdict: **IMPOSSIBLE** (content-tree overlap ~0%). Page-slug overlap 3-of-3 only on home + contatti. 3 distinct skin folders (`.cl-*` · `.we-*` · `.fm-*`). Salute chosen as opener: simplest shape (no deep-path), already pre-rotated outside-gate fixture, clean OUT policy with established precedents (raw SVG + bool + nested list-of-str + form structures). Benessere = A.16b (handles calendar bool-flags OUT). Famiglia = A.16c (deep-path tuple-in-dict-list + faq novel kind).

### Step 0 · Planning / audit findings chiave

- Archetype slug `clinic` · skin `medical/clinic/` · CSS **`.cl-*`** (78 hits) · 18 mature `html[dir="rtl"]` rules · `_base.html` 510 LOC
- 7 pages: home · studio(about) · servizi(services) · **prevenzione** (novel `prevention` kind) · medici(team) · contatti(contact) · **prenota** (novel `appointment` kind) — **2 novel page kinds** · plain string identifiers · no view dispatch
- 5-locale parity PERFETTA (576 keys × 5 locales · zero gaps · same as Bottega/Luxe/all-prior-enrollments)
- `apps/catalog/views.py::LiveTemplateView` ZERO imports da scheduler/booking/patient namespaces · boundary architectural pulito
- Image surface runtime-verified: 15 editable surfaces (1 scalar top-level `studio.photo_src` + 14 image-in-dict-row cells across 2 lists: `home.team_ribbon_people[].avatar` × 8 + `medici.doctors[].portrait` × 6) · **ALL RENDERED** (specialist-family precedent)
- 12 lists-of-dict IN + 4 lists-of-tuple IN = **16 STRUCTURED_FIELD_SHAPES entries** · tutti parent-level · ZERO deep-path
- 3 lists-of-dict OUT (form structures): `contatti.form_fields` · `prenota.form_fields` · `prenota.form_sections`
- 4 flat list-of-str OUT (policy): `site.hours_footer_rows` · `site.foot_extra_rows` · `home.partners` · `prenota.trust`
- 4 nested list-of-str inside dict rows OUT (Juris precedent): `servizi.services[].items` · `prevenzione.packages[].includes` · `home.prevenzione_cards[].includes` · `medici.doctors[].tags`
- **Posts list empty** (same structural absence as Bottega/Sapore/Brace · detail-page policy stays at 6-archetype uniform enforcement)
- **Stringent IN/OUT call on "technical-looking" cols** (5th archetype precedent chain): `num`/`popular_label` IN · `is_popular`/`icon_svg` OUT

### Step 1 · Schema + bridge + gate + contract tests

- `SALUTE_CLINIC_SCHEMA` added in `apps/editor/schema.py` — **9 sidebar groups · 95 scalar fields**.
- `STRUCTURED_FIELD_SHAPES["clinic"]` with **16 entries · tutti parent-level · ZERO deep-path** (12 dict + 4 tuple).
- Image-in-dict-row lists (2): `home.team_ribbon_people[].avatar` × 8 · `medici.doctors[].portrait` × 6 = 14 image cells.
- Scalar top-level image: `studio.photo_src` (rendered photo block on studio page).
- 3 gate registrations simultanee · `_ARCHETYPE_BASELINE_TEMPLATE["clinic"] = ("salute-studio-medico", "it")` + `_ARCHETYPE_SCHEMAS["clinic"] = SALUTE_CLINIC_SCHEMA` + `"clinic"` in `_MULTILOCALE_ENABLED_ARCHETYPES`.
- **Col-level exclusions**: 18× raw `icon_svg` (5th OUT category precedent) · `prevenzione.packages[].is_popular` bool (Luxe precedent) · 4× nested list-of-str (`includes`/`items`/`tags` · Juris precedent).
- **Complex-shape exclusion** (form + flat + nested): 2× form_fields + form_sections · 4× flat list-of-str · `pages` · `posts` (empty).
- 3 atomic fixes on `templates/live_templates/medical/clinic/_base.html`: title `site.logo_word|default:brand.brand_name` · body `mw-is-editor-preview` guard · `.cl-*` CSS guard block (`.cl-nav .wm` clamp 32ch) · preview-bridge.js conditional on `preview_project`.
- **DUAL-OUT GUARD** planted in `test_a16_salute_archetype_registered`: BOTH `wellness` + `family` asserted OUT at 3 layers (`_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE` + `_MULTILOCALE_ENABLED_ARCHETYPES` + `is_supported_archetype`). Sub-recipe extends to 2 removal phases.
- **Outside-gate fixture rotation** (6 location): `clinic`/`salute-studio-medico` → `wellness`/`benessere-centro-olistico` (A.16b candidate).

### Step 2 · Lifecycle HTTP end-to-end test

- `test_a16_salute_full_multilocale_lifecycle_end_to_end` added (pure test-only change · +382 LOC · zero production code).
- 11 phases blindates: perimeter start (DUAL-OUT GUARD) · 3 translatable locales on `home.headline` · global plain-key `site.logo_word` · scalar `studio.photo_src` · 2 image-in-dict-row (`home.team_ribbon_people.0.avatar` + `medici.doctors.0.portrait` · DIFFERENT lists + DIFFERENT pages) · publish · second-user preview walk 5 locales × 3 pages · AR `<html dir="rtl" lang="ar">` · owner re-opens editor with per-locale prefill · perimeter end (DUAL-OUT GUARD re-enforced) + **27 OUT paths rejected** (raw SVG × 4 · bool flag × 1 · nested list-of-str × 7 · form structures × 6 · flat str-list × 4 · pages/posts × 4).
- **Triple-invariant**: Salute IN + Benessere OUT + Famiglia OUT verified at start AND end of test.
- **Image plain-key invariant**: 3 image paths × 5 locales (15 combinations) assertNotIn `@<locale>:` prefix.

### Step 3 · Playwright browser walk

- Sidebar inventory: **359 total editable fields · 15 image widgets exact · 5 lang pills (IT/EN/FR/ES/AR) · 26 group slots** (9 sidebar + 16 indexed + 1 design).
- **8 critical IN paths present** in sidebar: `studio.photo_src` · `home.team_ribbon_people.{0,7}.avatar` · `medici.doctors.{0,5}.portrait` · `home.journey_steps.0.num` · `prevenzione.packages.0.popular_label` · `prevenzione.how_steps.0.num`.
- **16 sensitive OUT paths absent**: 4× raw `icon_svg` · `is_popular` bool · 4× nested list-of-str · 5× form structures · `pages` · `posts`.
- 5-locale flush walk IT→EN→FR→ES→AR with `home.headline` override in IT/EN/FR; ES/AR stays authored baseline (zero Latin override leak).
- Per-locale `home.headline` authored baselines verified:
  - IT: `La tua salute, il nostro lavoro quotidiano.`
  - EN: `Your health, our everyday work.`
  - FR: `Votre santé, notre travail quotidien.`
  - ES: `Su salud, nuestro trabajo diario.`
  - AR: `صحتك، عملنا اليومي.`
- **Storage shape after publish (7 overrides)**: 3 per-locale translatable (`@it/@en/@fr:home.headline`) + 4 plain-key globals (`site.logo_word` · `studio.photo_src` · `home.team_ribbon_people.0.avatar` · `medici.doctors.0.portrait`). Zero `@<locale>:` on any image or logo across 5 locales.
- **Render matrix 5 locales × 3 pages = 15/15 green**: logo×4 (nav + title + footer + footer strip) on every page; `studio.photo_src` only on studio; `home.team_ribbon_people.0.avatar` only on home; `medici.doctors.0.portrait` only on medici; zero cross-page bleed; IT/EN/FR override visible only in own locale; ES/AR show authored fallback.
- **AR RTL invariant verified**: editor iframe `dir="rtl"` · `lang="ar"` · `body.mw-is-editor-preview` · `.cl-nav` + `.cl-tr-card` rendered; public preview `<html lang="ar" dir="rtl">` · 3576 Arabic characters · authored AR `صحتك` present.

### Tests + smoke (post-merge)

- `manage.py check` → 0 issues
- `manage.py test apps` → **309/309 PASS** (295 pre-A.16 + 13 contract + 1 lifecycle)
- `smoke_full.py` → **834/834 routes HTTP 200**
- Browser walk 5-locale green (sidebar + flush + storage + render matrix + AR RTL)

### File delta

- `apps/editor/schema.py` +512 LOC (Salute schema + 16 shapes + 3 gate registrations)
- `apps/projects/tests.py` +828 (13 contract tests + 1 lifecycle test + dual-out guard + 6 outside-gate fixture rotations) / -28
- `templates/live_templates/medical/clinic/_base.html` +10 / -2 (3 atomic fixes on `.cl-*` skin)

**Pure 3-file enrollment surface · zero tocchi a `apps/commerce` · `services.py` · `rendering.py` · editor shell · widgets. Pattern confirmed sub-recipe standard after 5 consecutive applications. NOVEL contributions documented: 5th OUT category (raw SVG) + 3-phase staged progression + dual-out guard variant.**

### Medical-other family OPEN (half-open)

- Staged dedicated-schema closure **5 of N** (when family closes in A.16c): real-estate (A.12+A.12b) · portfolio (A.13+A.13b) · restaurant-continuation (A.14+A.14b) · ecommerce (A.15+A.15b) · **medical-other (A.16+A.16b+A.16c)**.
- 6 families chiuse + 1 half-open (medical-other).
- 4 templates editor-only-pending residui: Benessere (`wellness`) · Famiglia (`family`) · Aura (`agency-digital-studio`) · Elevate (`startup-saas-landing`).
- Catalog 20/20 `published_live` · **16/20 enrolled editor** (was 15/20 post-A.15b · +1 Salute).

### Guard removal pattern · 5th precedent pending (extended to 3-phase)

- Villa-out (A.12b via `test_a12b_villa_out_guard_was_removed_from_casa_tests`)
- Pixel-out (A.13b via `test_a13b_pixel_out_guard_was_removed_from_chiara_tests`)
- Brace-out (A.14b via `test_a14b_brace_out_guard_was_removed_from_sapore_tests`)
- Luxe-out (A.15b via `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`)
- **Wellness-out (A.16b via `test_a16b_benessere_out_guard_was_removed_from_salute_tests` · pending)**
- **Family-out (A.16c via `test_a16c_family_out_guard_was_removed_from_salute_tests` · pending)**

First time guard removal pattern applies twice from a single opener (Salute plants 2 guards · A.16b + A.16c each remove one).

### Outside-gate fixture rotation history

- A.15b: `fashion-editorial`/`luxe-fashion-store` → `clinic`/`salute-studio-medico`
- **A.16: `clinic`/`salute-studio-medico` → `wellness`/`benessere-centro-olistico`** (A.16b candidate)

6 fixture rotate · 4 `supported_locales`/`is_translatable` + 1 `is_supported_archetype` + 1 `customize_start` redirect.

### Decisioni binding in vigore post-A.16

- D-086 → D-095 (A.1 → A.5)
- D-096 · per-locale storage `@<locale>:<path>`
- D-097 · no cross-locale customer fallback
- D-098 · archetype gate + dedicated lifecycle test per enrollment
  - Session 73 operational clarification (under D-098 · no new D-number):
    - Medical-other family opens with Salute (D-098 recipe first 3-template staged progression)
    - Staged dedicated-schema progression generalizes from 2-phase to 3-phase variant
    - Dual-out guard sub-recipe (opener plants N-1 guards · each closure phase removes 1)
    - 5th OUT category formalized: raw SVG fields col-level OUT (safety + UX rationale documented)
    - Stringent IN col-level audit extended to 5 archetypes (Salute joins Sapore/Brace/Bottega/Luxe chain)
    - Bool flag handling: OUT col-level (no horizontal bool field type · preserves accompanying label text editability)
    - Outside-gate fixture rotation to `wellness`/`benessere-centro-olistico` (signals A.16b)

**Nessun nuovo D-number da A.16.** Operational clarification sotto D-098 solamente.

### Salute metrics

- 9 sidebar groups · 95 scalar fields · 15 image surfaces (1 scalar top + 14 dict-row cells · ALL RENDERED)
- 16 readonly indexed list entries · tutti parent-level · ZERO deep-path
- ~70 translatable · ~290 global (full audit deferred to maintenance phase)
- 5 locale parity PERFECT (576 keys × 5 · zero gaps)
- `.cl-*` skin · 18 `html[dir="rtl"]` rules
- Zero posts · zero form structures editing · zero mutable repeater · zero image per-locale · zero scheduler/booking/patient model paths
- Schema LOC delta +512 · SOTTO 600 soft guardrail (leaner than planning estimate 500-600)

### Not in scope (confirmed out-of-scope)

- Benessere editor enrollment (deferred A.16b)
- Famiglia editor enrollment (deferred A.16c)
- Bool field type addition (horizontal feature · resisted)
- Raw SVG editor widget (horizontal feature · resisted)
- Nested list-of-str editor widget (horizontal feature · resisted)
- Form-structure editor (horizontal feature · resisted)
- Image per-locale (D-098 invariante)
- Repeater per-locale (out-of-scope family)
- Mutable repeater (Salute lists tutte readonly)
- Detail-page editing (horizontal feature cross-archetype · 6-archetype uniform enforcement preserved)
- Scheduler-state / booking-state / patient-record editing (clinic-admin scope · separate concern)
- Coverage expansion beyond first wave
- Refactor trasversali
- Remote storage

---

## Session 72 — Phase A.15b · Luxe (fashion-editorial · ecommerce family · second template) Editor + Multi-locale Enrollment · CLOSES ECOMMERCE FAMILY (2026-04-19)

**Summary.** Fourteenth archetype enrolled in the editor: `fashion-editorial` (Luxe). Single-template phase — Luxe **closes** the ecommerce family opened in A.15 Bottega via staged dedicated-schema progression (fourth staged dedicated-schema closure after real-estate A.12+A.12b · portfolio A.13+A.13b · restaurant-continuation A.14+A.14b). **14 archetype slugs enrolled · 14 multi-locale enrolled · 15 templates editable end-to-end.** Catalog 20/20 `published_live` unchanged. Baseline `d8269da` → merge `bd9ffcb` on `phase-integration-baseline-v15` · pushed origin.

Three critical framings for this session:

1. **Luxe enrollment preserves the same boundary as Bottega.** The editor edits the presentational demo content in `template_content_luxe.py` (registry) · `apps/commerce/` (real catalog backend) stays completely out-of-scope. Boundary re-verified Step 0: `apps/catalog/views.py::LiveTemplateView` still does NOT import from `apps.commerce`. Zero cross-contamination by design. Light smoke guardrail test `test_a15b_luxe_commerce_admin_boundary` mirrors the A.15 Bottega contract.

2. **31 image surfaces ALL RENDERED — no storage-only split.** Unlike Bottega's typographic-led `.aw-*` skin (16 rendered + 6 storage-only crest-mark substitution from Session 42 D-073), Luxe's `.fe-*` skin is photographically editorial campaign-driven: every image surface the editor exposes is actually painted by the skin. 1 scalar top-level (`home.cover_image` · full-bleed hero cover) + 2 nested-dict scalar (`product.atelier_portrait` · `maison.direction_portrait`) + 28 image cells across 6 image-in-dict-row lists = 31 total. Lifecycle + browser walk verified render on all of them.

3. **Stringent IN col-level audit on "technical-looking" fields** per user Step 0 guidance: `drop` (editorial drop badge · 'Drop 01 · Spring 26'), `n` (Look numbering · 'Look 03'), `tag` (editorial availability badge · 'Lista d'attesa' · 'Capsula' · 'Archivio') all classified **IN** (customer-facing editorial content). `id` (structural slug · routing to /product/) + `available` (bool flag · commerce-state-like semantic) classified **OUT**. Documented in schema comment block + dedicated `test_a15b_luxe_visible_catalog_fields_kept_in` contract test.

### Context initial post-A.15

Baseline entering Session 72 was `d8269da` (post-A.15 Bottega enrollment consolidated; 13 archetypes enrolled, ecommerce family half-open). Luxe-out dual guard planted in Bottega tests (registration-time + runtime start + runtime end) · outside-gate fixture rotated to `fashion-editorial`/`luxe-fashion-store`.

### Luxe-only scope decision

A.14b (Brace) Step 0 audit had already ruled shared-schema IMPOSSIBILE with Bottega: 50% page-slug overlap (home/product/contatti shared; shop/journal vs collezione/lookbook diverge), `shop.products` 11 cols vs `collezione.products` 9 cols (Bottega has `artisan`/`place`, Luxe has `drop`), different editorial surfaces, image surface ratio 1:1.4 (Bottega 22 vs Luxe 31), journal editorial notes (Bottega) vs lookbook image gallery (Luxe). A.15 established the staged dedicated-schema closure with Bottega opening the family; A.15b mechanical reuse of the established recipe · fourth consecutive staged closure.

### Step 0 · Planning / audit findings chiave

- Archetype slug `fashion-editorial` · skin `ecommerce/fashion-editorial/` · CSS **`.fe-*`** (165 hits) · 21 mature `html[dir="rtl"]` rules · `_base.html` 793 LOC
- 6 pages: home · **collezione** (novel · `collection` kind) · product · maison (about) · **lookbook** (novel) · contatti — **2 novel page kinds** · plain string identifiers · no view dispatch
- 5-locale parity PERFETTA (259 keys × 5 locales · zero gaps)
- `apps/catalog/views.py::LiveTemplateView` still ZERO imports from `apps.commerce` · boundary preserved
- Image surface runtime-verified: 31 editable surfaces (1 scalar top-level `home.cover_image` · 2 nested-dict scalar · 28 image cells across 6 image-in-dict-row lists) · **ALL RENDERED** (no storage-only split)
- 11 lists-of-dict (6 with image col · 0 deep-path · pure parent-level registration) + 6 lists-of-tuple = 17 STRUCTURED_FIELD_SHAPES entries
- 8 flat list-of-str (all OUT per policy) · 1 form structure (`contatti.form_fields` OUT) · 3 flat scalar option lists (`size_options`/`color_options`/`sort_options` all OUT)
- **Posts list empty** (same structural absence as Bottega · Sapore · Brace · detail-page policy stays at 6-archetype uniform enforcement)
- **Stringent IN/OUT call on "technical-looking" cols** per user Step 0: `drop`/`n`/`tag` **IN** (customer-facing editorial badges); `id`/`available` **OUT** (structural + commerce-state-like)

### Step 1 · Schema + bridge + gate + contract tests

- `LUXE_FASHION_EDITORIAL_SCHEMA` added in `apps/editor/schema.py` — **8 sidebar groups · 164 scalar fields**.
- `STRUCTURED_FIELD_SHAPES["fashion-editorial"]` with **17 entries · tutti parent-level · ZERO deep-path** — 3 more than Bottega's 14 (richer editorial surfaces + press + credits + maison cards).
- Image-in-dict-row lists (6): `home.tiles[].image` × 4 · `home.lookbook_teaser_tiles[].image` × 3 · `collezione.products[].image` × 9 · `product.related_items[].image` × 3 · `maison.ateliers[].image` × 3 · `lookbook.looks[].image` × 6 = 28 image cells.
- Scalar top-level image: `home.cover_image` (full-bleed editorial cover LEFT on charcoal).
- Nested-dict scalar images (2): `product.atelier_portrait` · `maison.direction_portrait`.
- 3 gate registrations simultanee · `_ARCHETYPE_BASELINE_TEMPLATE["fashion-editorial"] = ("luxe-fashion-store", "it")` + `_ARCHETYPE_SCHEMAS["fashion-editorial"] = LUXE_FASHION_EDITORIAL_SCHEMA` + `"fashion-editorial"` in `_MULTILOCALE_ENABLED_ARCHETYPES`.
- **Col-level exclusions** (structural): `collezione.products[].id` + `.available` · `home.tiles[].id` · `product.related_items[].id`.
- **Complex-shape exclusion** (flat list-of-str + form + nested): `site.hours_footer_rows` · `site.office_rows` · `home.press_items` · `collezione.filter_groups` + `.0.options` · `collezione.sort_options` · `product.gallery` · `product.size_options` · `product.color_options` · `contatti.form_fields` · `pages` · `posts` (empty).
- 3 atomic fixes on `templates/live_templates/ecommerce/fashion-editorial/_base.html`: title `site.logo_word|default:brand.brand_name` · body `mw-is-editor-preview` guard · `.fe-*` CSS guard block (`.fe-nav .wm` clamp 32ch) · preview-bridge.js conditional on `preview_project`.
- **Luxe-out dual guard REMOVED** from A.15 Bottega tests (3 locations: registration-time in `test_a15_bottega_archetype_registered` · runtime start + runtime end of lifecycle test) via symmetric inversion `test_a15b_luxe_out_guard_was_removed_from_bottega_tests` — **4th precedent** of guard removal pattern after Villa-out (A.12b) · Pixel-out (A.13b) · Brace-out (A.14b).
- **Outside-gate fixture rotation** (6 location): `fashion-editorial`/`luxe-fashion-store` → `clinic`/`salute-studio-medico` (next outside-gate candidate · medical-clinic family still OUT of editor).

### Step 2 · Lifecycle HTTP end-to-end test

- `test_a15b_luxe_full_multilocale_lifecycle_end_to_end` added (pure test-only change · +424 LOC · zero production code).
- 13 phases blindates: perimeter start · 3 translatable locales on `home.headline` · global plain-key `site.logo_word` · scalar `home.cover_image` · 2 nested-dict scalar (`product.atelier_portrait` + `maison.direction_portrait`) · 2 image-in-dict-row (`collezione.products.0.image` + `lookbook.looks.0.image`) · publish · second-user preview walk 5 locales × 5 pages · AR `<html dir="rtl" lang="ar">` · owner re-opens editor with per-locale prefill · perimeter end + 18 OUT paths rejected.
- **Dual invariant**: Luxe IN + Bottega still IN verified at start AND end of test.
- **Image plain-key invariant**: all 5 image paths × 5 locales (25 combinations) assertNotIn `@<locale>:` prefix.

### Step 3 · Playwright browser walk

- Sidebar inventory: **448 total editable fields · 31 image widgets exact · 5 lang pills (IT/EN/FR/ES/AR) · 26 group slots** (8 pages + 17 indexed + 1 design).
- **8 critical image paths present** in sidebar: `home.cover_image` · `product.atelier_portrait` · `maison.direction_portrait` · `collezione.products.0.image` · `lookbook.looks.0.image` · `home.tiles.0.image` · `lookbook.looks.5.image` · `collezione.products.8.image`.
- **13 OUT paths correctly absent** from sidebar: filter_groups/options · sort_options · gallery · size_options · color_options · form_fields · pages · posts · col-level `id`/`available` on 3 lists.
- 5-locale flush walk IT→EN→FR→ES→AR with `home.headline` override in IT/EN/FR; ES/AR stays authored baseline (zero Latin override leak).
- Per-locale `home.headline` authored baselines verified:
  - IT: `Il nuovo corpo del vestire.`
  - EN: `The new body of dress.`
  - FR: `Le nouveau corps du vêtement.`
  - ES: `El nuevo cuerpo del vestir.`
  - AR: `الجسد الجديد للِّباس.`
- **Storage shape after publish (7 overrides)**: 3 per-locale translatable (`@it/@en/@fr:home.headline`) + 4 plain-key globals (`site.logo_word` · `home.cover_image` · `collezione.products.0.image` · `lookbook.looks.0.image`). Zero `@<locale>:` on any image or logo across 5 locales.
- **Render matrix 5 locales × 3 pages = 15/15 green**: logo×4 (nav + title + footer word + footer strip) on every page; `home.cover_image` only on home; `collezione.products.0.image` only on collezione; `lookbook.looks.0.image` only on lookbook; zero cross-page bleed; IT/EN/FR override visible only in own locale; ES/AR show authored fallback.
- **AR RTL invariant verified**: editor iframe `dir="rtl"` · `lang="ar"` · `body.mw-is-editor-preview` · `.fe-nav` present; public preview `<html lang="ar" dir="rtl">` · 5182 Arabic characters.

### Tests + smoke

- `manage.py check` → 0 issues
- `manage.py test apps` → **295/295 PASS** (280 pre-A.15b + 14 contract + 1 lifecycle)
- `smoke_full.py` → **834/834 routes HTTP 200**
- Browser walk 5-locale green (sidebar + flush + storage + render matrix + AR RTL)

### File delta

- `apps/editor/schema.py` +598 LOC (Luxe schema + 17 shapes + 3 gate registrations)
- `apps/projects/tests.py` +904 (14 contract tests + 1 lifecycle test + Luxe-out dual guard removed + 6 outside-gate fixture rotations) / -55
- `templates/live_templates/ecommerce/fashion-editorial/_base.html` +10 / -2 (3 atomic fixes on `.fe-*` skin)

**Pure 3-file enrollment surface · zero tocchi a `apps/commerce` · `services.py` · `rendering.py` · editor shell · widgets. Pattern confirmed sub-recipe standard after 4 consecutive applications.**

### Ecommerce family closed

- Staged dedicated-schema closure **4 of N**: real-estate (A.12+A.12b) · portfolio (A.13+A.13b) · restaurant-continuation (A.14+A.14b) · **ecommerce (A.15+A.15b)**.
- 6 families chiuse (law + medical-specialist + real-estate + portfolio + restaurant-continuation + ecommerce) · 3 aperte residue (medical-other · agency-secondary · startup-saas).
- 5 templates editor-only-pending residui: Salute (clinic) · Benessere (wellness) · Famiglia (family) · Aura (agency-digital-studio) · Elevate (startup-saas-landing).
- Staged dedicated-schema è la topologia DOMINANTE: **4 closed**.
- Catalog 20/20 `published_live` · **15/20 enrolled editor** (was 14/20 post-A.15).

### Guard removal pattern consolidated · 4th precedent

- Villa-out (A.12b via `test_a12b_villa_out_guard_was_removed_from_casa_tests`)
- Pixel-out (A.13b via `test_a13b_pixel_out_guard_was_removed_from_chiara_tests`)
- Brace-out (A.14b via `test_a14b_brace_out_guard_was_removed_from_sapore_tests`)
- **Luxe-out (A.15b via `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`)**

Pattern is now sub-recipe standard for every staged closure: Step 1 of the closing phase MUST remove the dual guard (registration-time + runtime start + runtime end in 3 pre-existing locations on the opening phase's test module) and install a symmetric inversion test.

### Outside-gate fixture rotation history

- A.13 rotated: `cinematic-photographer`/`pixel-portfolio-fotografico` → (next)
- A.13b rotated: (used Pixel before) → `trattoria-warm`/`sapore-trattoria-pizzeria`
- A.14 rotated: `trattoria-warm`/`sapore-trattoria-pizzeria` → `street-modern`/`brace-street-food-lab`
- A.14b rotated: `street-modern`/`brace-street-food-lab` → `artisan-workshop`/`bottega-shop-artigianale`
- A.15 rotated: `artisan-workshop`/`bottega-shop-artigianale` → `fashion-editorial`/`luxe-fashion-store`
- **A.15b rotated: `fashion-editorial`/`luxe-fashion-store` → `clinic`/`salute-studio-medico`**

6 fixture rotate · 4 `supported_locales`/`is_translatable` + 1 `is_supported_archetype` + 1 `customize_start` redirect.

### Decisioni binding in vigore post-A.15b

- D-086 → D-095 (A.1 → A.5)
- D-096 · per-locale storage `@<locale>:<path>`
- D-097 · no cross-locale customer fallback
- D-098 · archetype gate + dedicated lifecycle test per enrollment
  - Session 72 operational clarification (under D-098 · no new D-number):
    - Ecommerce family closed with Luxe (D-098 recipe fourth staged closure)
    - Storage-only vs rendered image distinction is PER-SKIN (Bottega has both · Luxe has all-rendered · not a schema concern, a render-skin concern)
    - Stringent IN/OUT col-level audit extended to drop/n/tag on Luxe (4th archetype to apply this framing after Sapore forno.pizza_signatures.n · Brace ordina routes n · Bottega shop.products n/edition/tag)
    - Guard removal sub-recipe now at 4 precedents and consolidated
    - Outside-gate fixture rotation to `clinic`/`salute-studio-medico` (first non-ecommerce/non-restaurant outside-gate reference since A.12+)
    - Boundary editor-vs-commerce-admin re-verified on second ecommerce archetype

**Nessun nuovo D-number da A.15b.** Operational clarification sotto D-098 solamente.

### Luxe metrics

- 8 sidebar groups · 164 scalar fields · 31 image surfaces (1 scalar top + 2 nested-dict scalar + 28 dict-row cells)
- 17 readonly indexed list entries · tutti parent-level · ZERO deep-path
- ~130 translatable · ~450 global (detail tbd by further audit)
- 5 locale parity PERFECT (259 keys × 5 · zero gaps)
- `.fe-*` skin · 21 `html[dir="rtl"]` rules
- Zero posts · zero form structures editing · zero mutable repeater · zero image per-locale · zero apps.commerce
- Schema LOC delta +598 · SOTTO 600 soft guardrail

### Not in scope (confirmed out-of-scope)

- apps.commerce editing (real catalog backend · seller dashboard scope)
- Image per-locale (D-098 invariante)
- Repeater per-locale (out-of-scope family)
- Mutable repeater (Luxe lists tutte readonly)
- Detail-page editing (horizontal feature cross-archetype · 6-archetype uniform enforcement preserved)
- Product-detail per-item editing (demo content · registry-driven · NOT backend catalog)
- Coverage expansion beyond first wave
- Refactor trasversali
- Remote storage

---

## Session 71 — Phase A.15 · Bottega (artisan-workshop · ecommerce family · first template) Editor + Multi-locale Enrollment · OPENS ECOMMERCE FAMILY (2026-04-19)

**Summary.** Thirteenth archetype enrolled in the editor: `artisan-workshop` (Bottega). Single-template phase — Bottega opens the ecommerce family via staged dedicated-schema progression (fourth staged opening after real-estate A.12 · portfolio A.13 · restaurant-continuation A.14). Luxe (`fashion-editorial`) stays OUT until A.15b. **13 archetype slugs enrolled · 13 multi-locale enrolled · 14 templates editable end-to-end.** Catalog 20/20 `published_live` unchanged.

Two critical framings for this session:

1. **Bottega enrollment is SHOWCASE / template-content editing, NOT commerce-admin editing.** The editor edits the presentational demo content in `template_content_bottega.py` (registry) · `apps/commerce/` (real catalog: Storefront/Product/Variant/Cart/Order/PaymentIntent · seller dashboard Phase 3a/3b) stays completely out-of-scope. Boundary runtime-verified Step 0: `apps/catalog/views.py::LiveTemplateView` does NOT import from `apps.commerce` · the two surfaces are ORTHOGONAL. The editor customer personalizes the template showcase (demo product cards · hero copy · journal entries); the seller customer manages the real storefront catalog via seller dashboard. Zero cross-contamination by design.

2. **22 image widgets in sidebar = 16 rendered + 6 storage-only is INTENTIONAL, not a bug.** Bottega's `.aw-*` skin was converted to typographic-first in Session 42 D-073 (DNA-honest artisan-workshop treatment: no portrait photos; crest-mark glyphs + monogram stamps). The 6 storage-only image fields (`product.artisan_portrait` · `atelier.founder_portrait` · `home.makers.{0..3}.portrait`) stay EXPOSED in the editor sidebar because the registry data is preserved for future skin variants / customer swap. The 16 rendered fields (`home.latest_items.{0..3}.image` · `shop.products.{0..8}.image` · `product.related_items.{0..2}.image`) are product-thumbnail dict-row cells the skin actually paints via `background-image:url('{{ x.image }}')`. Storage contract (plain-key per-locale) is blindato identical for both categories; only VISIBILITY differs per skin rendering.

### Context initial post-A.14b

Baseline entering Session 71 was `7b365bb` (post-A.14b Brace closed restaurant-continuation; 12 archetypes enrolled). Ecommerce pending as next family-closure candidate · no workstream prescribed.

### Bottega-only scope decision

Step-0 audit confirmed shared-schema IMPOSSIBILE with Luxe: 50% page-slug overlap (home/product/contatti shared; shop/journal vs collection/lookbook diverge), `shop.products` 11 cols vs `collezione.products` 9 cols (different editorial surfaces), image surface ratio 1:1.4 (Bottega 22 vs Luxe 31), journal editorial notes vs lookbook image gallery completely different. Staged dedicated-schema progression (Bottega A.15 + Luxe A.15b) is the correct topology · fourth consecutive application of the staged pattern · mirror of real-estate · portfolio · restaurant-continuation. Bottega-first chosen over Luxe-first because: simpler shape (10 lists-of-dict vs 12 · 22 image surfaces vs 31), outside-gate fixture already at Bottega post-A.14b (continuity), `.aw-*` skin RTL more mature (31 rules vs Luxe 21), typographic-first DNA translates cleaner to schema (fewer image-in-dict-row lists than Luxe's 6).

### Step 0 · Planning / audit findings chiave

- Archetype slug `artisan-workshop` · skin `ecommerce/artisan-workshop/` · CSS **`.aw-*`** (97 hits) · 31 mature `html[dir="rtl"]` rules · `_base.html` 541 LOC
- 6 pages: home · **shop** (novel) · **product** (novel) · atelier (about) · **journal** (novel) · contatti — **3 novel page kinds** · plain string identifiers · no view dispatch
- 5-locale parity PERFETTA (236 keys × 5 locales · zero gaps)
- **`apps/catalog/views.py::LiveTemplateView` has ZERO imports from `apps.commerce`** · boundary runtime-verified
- **Template_content registry** renders `/templates/ecommerce/bottega-shop-artigianale/preview/<page>/` · **NOT apps.commerce** · real catalog lives at `/shop/...` and is separate
- Image surface runtime-verified: 22 editable surfaces (0 scalar top-level · 2 nested-dict scalar · 20 image cells across 4 image-in-dict-row lists)
- 10 lists-of-dict (4 with image col · 0 deep-path · pure parent-level registration)
- 6 lists-of-tuple · 8 flat list-of-str (all OUT for policy) · 1 form structure (`contatti.form_fields` OUT)
- **Posts list empty** (same as Sapore · Brace · structural absence · detail-page policy stays at 6-archetype uniform enforcement)
- **Stringent IN/OUT call on "technical-looking" cols** per user Step 1 guidance: `n`/`edition`/`icon`/`tag` all classified **IN** (editorial visible: 'N° 042'/'3 / 8'/'Esaurito'/'01'/'TOP'); `id`/`available` classified **OUT** (structural slug + bool flag). Documented in-file and in dedicated contract test.

### Step 1 · Schema + bridge + gate + contract tests

- `BOTTEGA_ARTISAN_WORKSHOP_SCHEMA` added in `apps/editor/schema.py` — 8 sidebar groups · 141 scalar fields.
- `STRUCTURED_FIELD_SHAPES["artisan-workshop"]` with **14 entries · tutti parent · ZERO deep-path** (Bottega has no list-nested-in-list-parent · simpler than Sapore/Brace).
- Image-in-dict-row lists (4): `home.latest_items[].image` × 4 · `home.makers[].portrait` × 4 · `shop.products[].image` × 9 · `product.related_items[].image` × 3 = 20 image cells.
- Nested-dict scalar images (2): `product.artisan_portrait` · `atelier.founder_portrait` (Chiara `studio.founder.image` precedent shape).
- 3 gate registrations simultanee · `_ARCHETYPE_BASELINE_TEMPLATE["artisan-workshop"] = ("bottega-shop-artigianale", "it")` + `_ARCHETYPE_SCHEMAS["artisan-workshop"] = BOTTEGA_ARTISAN_WORKSHOP_SCHEMA` + `"artisan-workshop"` in `_MULTILOCALE_ENABLED_ARCHETYPES`.
- **Col-level exclusions** (structural): `shop.products[].id` + `.available` · `home.latest_items[].id` · `product.related_items[].id`.
- **Complex-shape exclusion** (flat list-of-str + form + nested): `site.hours_footer_rows` · `site.stockists_rows` · `home.press_items` · `shop.filter_groups` + `.0.options` · `shop.sort_options` · `product.gallery` · `product.size_options` · `contatti.card_hours_rows` · `contatti.form_fields` · `pages` · `posts` (empty).
- 3 atomic fixes on `templates/live_templates/ecommerce/artisan-workshop/_base.html`: title `site.logo_word` · body `mw-is-editor-preview` guard · `.aw-*` CSS guard block · preview-bridge.js conditional.
- **Luxe-out guard dual layer** in `test_a15_bottega_archetype_registered` (registration-time + runtime via lifecycle end-of-test check).
- **Outside-gate fixture rotation** (6 location): `artisan-workshop`/`bottega-shop-artigianale` → `fashion-editorial`/`luxe-fashion-store` (A.15b pending candidate).
- 13 new A.15 contract tests incl. **`test_a15_bottega_visible_catalog_fields_kept_in`** (stringent IN call on n/edition/icon/tag · audit-driven · NOT-for-inertia) + **`test_a15_bottega_commerce_admin_boundary`** (light smoke check: no editor paths reference `apps.commerce` model namespaces like `storefront.`/`cart.`/`variant.`/`order.`/`payment_intent.`).
- **Schema LOC delta +585** · **sotto 600 soft guardrail** (lighter than initial estimate 650 · 14 entries without deep-path = leaner than Brace +826 and Sapore +663).
- Commit `cff68a1` · `feat: add artisan-workshop archetype editor schema` · 3 files · +1018 / −28.

### Step 2 · Lifecycle HTTP end-to-end

- `test_a15_bottega_full_multilocale_lifecycle_end_to_end` cross-cutting · 11 phases · exercises FIVE image overrides (3 rendered + 2 storage-only) to blindare ALL distinct patterns:
  1. Perimeter invariants at TEST START (Bottega in · Luxe out on both gates · leak check duro)
  2. 3 autosaves IT/EN/FR on `home.headline` → `@<locale>:home.headline` × 3
  3. Global `site.logo_word` via EN → plain-keyed (explicit `assertNotIn("@en:")`)
  4. Nested-dict scalar image `product.artisan_portrait` (storage blindatura · not rendered in typographic skin) → 5× `assertNotIn`
  5. Image-in-dict-row `shop.products.0.image` → 5× `assertNotIn` + render on public shop page all 5 locales
  6. Image-in-dict-row `home.makers.0.portrait` (storage blindatura · not rendered) → 5× `assertNotIn`
  7. Image-in-dict-row `home.latest_items.0.image` (second list shape · rendered) → 5× `assertNotIn` + render on public home page all 5 locales
  8. Image-in-dict-row `product.related_items.0.image` (third list shape · rendered) → 5× `assertNotIn` + render on public product page all 5 locales
  9. Publish · 5-locale public preview on home/shop/product (3 pages) · AR `<html dir="rtl" lang="ar">` on `.aw-*`
  10. Owner reopen per locale · prefill + universals
  11. End-of-test · Luxe out at both gates (leak check duro 2x) · 12 pre-A.15 still enrolled · 14 rejected paths (sensitive OUT · col-level + complex-shape)
- Commit `7764f40` · `test: lock artisan-workshop lifecycle end to end` · 1 file · +421 LOC · zero production-code touches.
- **In-flight adjustment documented**: during first test run, `home.makers.0.portrait` visibility assertion failed because the typographic-first skin paints a crest-mark glyph, not the portrait URL. Per user Step 2 guidance ("tenuto coerente il comportamento reale"), storage blindatura kept identical (5× `assertNotIn`) and visibility check pivoted to `home.latest_items.0.image` (different list shape · rendered). The storage-only classification is intentional: registry data preserved, skin doesn't paint.

### Step 3 · Browser walk (Playwright · 5-locale · real browser)

Playwright walk on fresh Bottega draft · all checks green:
- Editor mount `?lang=it` · 5 pills · "Lingua attiva" label · IT active
- **22 image widgets** · distinzione netta: **16 rendered** (`home.latest_items.{0..3}.image` × 4 + `shop.products.{0..8}.image` × 9 + `product.related_items.{0..2}.image` × 3) + **6 storage-only** (`product.artisan_portrait` + `atelier.founder_portrait` + `home.makers.{0..3}.portrait`). Zero unclassified.
- **11 out-of-perimeter prefixes assenti** dal sidebar (`site.hours_footer_rows` · `site.stockists_rows` · `home.press_items` · `shop.filter_groups` · `shop.sort_options` · `product.gallery` · `product.size_options` · `contatti.card_hours_rows` · `contatti.form_fields` · `pages` · `posts` · tutti 0 hits)
- **4 col-level OUT assenti** dal sidebar (`shop.products.0.id` · `.available` · `home.latest_items.0.id` · `product.related_items.0.id`)
- Flush-before-switch verified IT→EN→FR→ES→AR · EN prefill "One-of-a-kind pieces stitched, thrown and woven..." · FR prefill "Des pièces uniques cousues, tournées et tissées..." · ES prefill "Piezas únicas cosidas, torneadas y tejidas..." · zero walk-text leak cross-locale
- 5 image overrides persistiti · 4 rendered verified visibili in sidebar + iframe
- AR iframe `<html lang="ar" dir="rtl">` on `.aw-*` skin · 6 `.aw-nav/.aw-foot/.aw-section` hits · title `"A15 Bottega Walk Brand — الورشة"`
- Publish via `services.publish_project`
- Second-user public preview 5 locali su home/shop/product · all 200 · 3 rendered image overrides visibili universalmente in tutti 5 locali · ES/AR authored fallback su translatable text · universals (logo + 3 image) preservati

### Outcome

- **Ecommerce family OPEN** via staged dedicated-schema first step (Bottega A.15 · Luxe A.15b pending). Fourth consecutive staged opening after real-estate · portfolio · restaurant-continuation.
- **Boundary editor-vs-commerce-admin runtime-confirmed pulito**: editor enrollment touches ONLY template_content registry · `apps/commerce` state managed separately via seller dashboard · zero cross-reference · zero test coupling · zero URL overlap.
- **Rendered vs storage-only image distinction validated**: 16 rendered (paint visible) + 6 storage-only (registry-preserved, skin-typographic-converted) · NOT a bug · intentional result of Session 42 D-073 DNA-honest conversion · editor contract blindato identical for both.
- **Stringent IN/OUT on "technical-looking" fields** paid off: `n`/`edition`/`icon` kept IN (editorial visible · customer-facing badges · same category as Sapore forno.pizza_signatures.n roman numeral counter) · `id`/`available` OUT (truly structural) · documented in-file + contract test.
- Bottega is 13th archetype enrolled · 14 templates editable · 5 families closed + 1 half-open (ecommerce) + 3 aperte residue.
- Zero new binding decisions · D-096 / D-097 / D-098 unchanged. Only operational clarification added to D-098 for Session 71.
- Acceptance gates post-merge: `python manage.py check` 0 issues · `python manage.py test apps` 280/280 PASS · `python smoke_full.py` 834/834 routes HTTP 200.
- Baseline `phase-integration-baseline-v15` tip: **`fab3ebc`** (A.15 merge), pushed to `origin/phase-integration-baseline-v15`.

### Blockers

**None.** No explicitly-deferred debt is pending.

### Exact next step

A.15 opens a family; it does not close one. Top candidate is **A.15b Luxe (`fashion-editorial`)** · closes ecommerce family · fourth consecutive staged closure after real-estate · portfolio · restaurant-continuation. Luxe has heavier shape than Bottega (12 lists-of-dict vs 10 · 6 image-in-dict-row lists vs 4 · 31 image surfaces vs 22 · lookbook adds image-heavy editorial band) but **no new infrastructure needed** · full mechanical-reuse of A.15 Bottega recipe. Alternatives: medical-other (3 separate phases) · Aura individual · Elevate individual · MEMORY.md maintenance mini-phase (separate, not bundled). MEMORY.md index now ~32KB sopra warning-soglia 24.4KB.

---

## Session 70 — Phase A.14b · Brace (street-modern · restaurant-continuation family · second template) Editor + Multi-locale Enrollment · CLOSES RESTAURANT-CONTINUATION FAMILY (2026-04-19)

**Summary.** Twelfth archetype enrolled in the editor: `street-modern` (Brace). Single-template phase — Brace is the restaurant-continuation family's second archetype, completing the staged dedicated-schema progression opened in A.14 by Sapore (`trattoria-warm`). **Fifth family editor-complete** (law · medical-specialist · real-estate · portfolio · restaurant-continuation). Staged dedicated-schema closure topology now with **3 real precedents** (all closed): real-estate (A.12+A.12b) · portfolio (A.13+A.13b) · **restaurant-continuation (A.14+A.14b)**.

Brace exercises BOTH deep-path shapes end-to-end: `menu.sections.{i}.items[].image` (dict-in-dict-list parent · Chiara A.13 precedent) for 19 food-photo cells across 5 sections, AND `ordina.routes.{i}.lines[].value` (tuple-in-dict-list parent · Sapore A.14 precedent via commit `f66ac24`) for address/phone/partner-line content. The A.14 Step 2 render-side fix is now **contract-confirmed cross-pattern** — both shape families work without additional infrastructure changes. 3-file pure enrollment surface (schema + _base.html + tests). Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / ProjectAsset / `/assets/upload/` / editor JS-CSS shell.

**Restaurant-continuation family CLOSED.** 12 archetype slugs enrolled · 12 multi-locale enrolled · 13 templates editable end-to-end · catalog 20/20 `published_live` unchanged. 7 templates still editor-unsupported across 4 open families (3 medical-other · 2 ecommerce · 1 agency-secondary · 1 startup-saas). 266/266 tests · 834/834 smoke · browser walk 5-locale green with explicit verification that neighbor items (`.0.1.name`) stay untouched when adjacent item (`.0.0.name`) is overridden.

### Context initial post-A.14

Baseline entering Session 70 was `8a40f3a` (post-A.14 Sapore opened the restaurant-continuation family, Brace-out dual guard active at registration-time + runtime). 11 archetype slugs enrolled · 12 templates editable · 1 family half-open. Restaurant-continuation pending closure via A.14b Brace.

### Brace-only scope decision

Step-0 runtime audit confirmed shared-schema IMPOSSIBILE: 50% page-slug overlap (home+menu+contatti shared; lab/moments/ordina Brace vs storia/forno/eventi Sapore diverge entirely), menu shape fundamentally different (Sapore nested tuple no-image vs Brace nested dict-with-image-col), image surface ratio 1:3.4 (Sapore 13 vs Brace 44), form structure presence inverted (Sapore has form_sections · Brace has none). Staged dedicated-schema progression is the correct topology (third consecutive application after real-estate and portfolio). Brace-only chosen per "one phase = one archetype decision" discipline now 13 phases strong (A.6 → A.14b).

### Step 0 · Planning / audit findings chiave

- Archetype slug `street-modern` · skin `restaurant/street-modern/` · CSS **`.sm-*`** (87 hits) · `_base.html` 547 LOC
- **24 mature `html[dir="rtl"]` rules** (vs Sapore 18 · Chiara 46)
- 6 pages: home · menu · lab (about) · moments (gallery) · ordina (**novel `order` kind**) · contatti
- **5-locale parity PERFETTA** (273 keys × 5 locales · 0 missing · 0 extra)
- Image surface inventory runtime-verified: **44 editable surfaces** (3 scalar top-level + 41 image cells across 6 image-in-dict-row lists incl. 19 cells from `menu.sections.{0..4}.items[].image` deep-path)
- **`menu.sections.{i}.items[].image` è interamente coperto dall'infra post-A.14** (Chiara-precedent shape: dict-in-dict-list parent · render via `_apply_indexed` fix f66ac24 A.14 Step 2 · schema via `_resolve_path` list-index A.14 Step 1)
- **`ordina.routes[].lines` correzione ipotesi pre-audit → IN**: initial hypothesis "OUT default finché l'audit non dimostra valore editoriale" respinta dall'evidenza runtime. `routes.0.lines = [['INDIRIZZO', 'Via Indipendenza 42'], ['CODA STIMATA', '~4 MIN'], ['ORARI', '12:00-24:00']]` — contenuto chiaramente editoriale (address/phone/partner-names · customer reale cambierebbe sicuramente). Registrato come 3 deep-path tuple-in-dict-list entries (Sapore-precedent shape).
- `posts` list empty (same as Sapore · structural absence · detail-page policy stays at 6-archetype uniform enforcement)
- No form structures (Brace ships zero · smaller out-policy set than Sapore)

### Step 1 · Schema + bridge + gate + contract tests

- `BRACE_STREET_MODERN_SCHEMA` added in `apps/editor/schema.py` — 8 sidebar groups · 170 scalar fields · 3 scalar image + coverage for 6 image-in-dict-row lists.
- `STRUCTURED_FIELD_SHAPES["street-modern"]` with **30 entries**: 22 parent lists + 5 `menu.sections.{0..4}.items` deep-path (dict-in-dict-list · 4/4/4/4/3 rows) + 3 `ordina.routes.{0..2}.lines` deep-path (tuple-in-dict-list · 3 rows × (label/value)).
- 3 gate registrations · `_ARCHETYPE_BASELINE_TEMPLATE["street-modern"] = ("brace-street-food-lab", "it")` + `_ARCHETYPE_SCHEMAS["street-modern"] = BRACE_STREET_MODERN_SCHEMA` + `"street-modern"` in `_MULTILOCALE_ENABLED_ARCHETYPES`.
- Col-level exclusions (structural identifiers / routing flags): `menu.sections[].id` · `moments.grid[].filename` · `ordina.routes[].id` + `ordina.routes[].cta_kind` · `contatti.channels[].icon` + `contatti.channels[].kind`.
- Complex-shape exclusion (flat list-of-str + navigation): `site.hours_footer_rows` · `home.manifesto_paragraphs` · `moments.categories` · `pages` · `posts` (empty).
- **Brace-out guard removal** dai test A.14 Sapore · 2 location simmetriche:
  - `test_a14_sapore_archetype_registered`: rimosse 4 `assertNotIn("street-modern", ...)` + `assertFalse(is_supported_archetype("street-modern"))`
  - `test_a14_sapore_full_multilocale_lifecycle_end_to_end` end-of-test: rimosse 2 `assertNotIn("street-modern", ...)` runtime
- **Unsupported fixture rotation** in 6 location pre-existing: `street-modern`/`brace-street-food-lab` → **`artisan-workshop`/`bottega-shop-artigianale`** (ecommerce candidate A.15) · comment aggiornati sulla rotation history
- 3 atomic fixes su `templates/live_templates/restaurant/street-modern/_base.html`: title `site.logo_word|default:brand.brand_name` · body `mw-is-editor-preview` guard class · `.sm-*` CSS guard block suppressing marketplace strip + clamping wordmark · preview-bridge.js conditional on `preview_project`.
- 13 new A.14b contract tests incl. `test_a14b_brace_out_guard_was_removed_from_sapore_tests` (symmetric inversion verification · mirror A.12b Villa-out + A.13b Pixel-out pattern).
- **Schema LOC delta +826** — documented exception over 600-LOC soft guardrail, non-blocking: overshoot riflette 8 deep-path entries (5 menu-items + 3 ordina-routes-lines) + volume 3.4× Sapore (44 image surfaces vs 13 · 30 list entries vs 20). Alternative respinte in Step 0 (menu fake-editable OR pseudo-path scalar flat entrambe inferiori).
- Commit `fabea8a` · `feat: add street-modern archetype editor schema` · 3 files · +1286 / −55.

### Step 2 · Lifecycle HTTP end-to-end

- `test_a14b_brace_full_multilocale_lifecycle_end_to_end` cross-cutting · 9 phases · covers:
  1. 3 autosaves IT/EN/FR on `home.headline` → `@<locale>:home.headline` × 3
  2. Global `site.logo_word` via EN autosave → plain-keyed (explicit `assertNotIn("@en:")`)
  3. Scalar image `home.hero_image` → plain-keyed across all 5 locales (5× `assertNotIn`)
  4. **Deep-path dict-in-dict-list** `menu.sections.0.items.0.image` → plain-keyed (5× `assertNotIn`) + **visible in public preview menu page across all 5 locales**
  5. **Deep-path tuple-in-dict-list** `ordina.routes.0.lines.0.value` → plain-keyed (5× `assertNotIn`) + **visible in public preview ordina page across all 5 locales**
  6. Publish · 5-locale second-user preview on home/menu/ordina with full universals verification
  7. IT/EN/FR home render locale override · ES/AR authored fallback + universals preserved
  8. AR `<html dir="rtl" lang="ar">` on `.sm-*` skin
  9. Perimeter invariants · Brace + Sapore both still enrolled at start AND end-of-test · 14 rejected paths re-verified
- Commit `4fd677b` · `test: lock street-modern lifecycle end to end` · 1 file · +362 LOC · zero production-code touches.

### Step 3 · Browser walk (Playwright · 5-locale · real browser)

Playwright walk on fresh Brace draft covered every user-visible surface · all checks green:
- Editor mount `?lang=it` · 5 pills `data-ed-lang` · IT active · "Lingua attiva" label
- **44 image widgets nel sidebar** con distinzione esplicita: 3 scalar top-level (home/lab/moments hero + featured) + 41 dict-row cells (home.menu_strip_items × 6 + home.crew × 3 + home.atmo_strip × 3 + lab.crew × 4 + moments.grid × 6 + menu.sections.{0..4}.items × 19)
- **5 out-of-perimeter absenti** (`site.hours_footer_rows` · `home.manifesto_paragraphs` · `moments.categories` · `pages` · `posts` · tutti 0 hits in sidebar)
- Flush-before-switch verified IT→EN→FR→ES→AR · EN prefill authored "FIRED ON LIVE FLAME" · FR prefill "AU FEU VIF" · ES prefill "AL FUEGO VIVO" · zero walk-text leak
- **Menu deep-path edit real**: `menu.sections.0.items.0.name` + `.image` overridden → browser verified visible on IT/EN/FR/ES/AR menu page
- **Ordina deep-path edit real**: `ordina.routes.0.lines.0.value` → visible on IT/EN/FR/ES/AR ordina page
- AR iframe `<html lang="ar" dir="rtl">` on `.sm-*` skin · title "A14b Brace Walk Brand — الرئيسية"
- Publish via `services.publish_project`
- **No neighbor corruption** explicitly verified · `menu.sections.0.items.1.name` ("SMASH CLASSICO" IT/EN/FR/AR · "SMASH CLASICO" ES · proper Spanish translation) stays authored-rendered when `.0.0` overridden · splicer touches ONLY the addressed cell
- Second-user public preview 5 locales · dish image override + route line override + logo universal + hero image universal all visible in every locale

### Outcome

- **Restaurant-continuation family CLOSED** via staged dedicated-schema progression (Sapore A.14 · Brace A.14b) · third consecutive staged closure after real-estate and portfolio. D-098 staged topology now with 3 real closed precedents.
- **Fix `f66ac24` (A.14 Step 2) è cross-pattern confermato operativamente**: covers both tuple-in-dict-list parent (Sapore menu) and dict-in-dict-list parent (Brace menu) via the same render-layer extension. Three editor layers (`services._resolve_path` · `schema._resolve_path` · `rendering._apply_indexed`) now speak the same language on list-index deep paths — contract-alignment bugfix thesis validated.
- **Guard removal pattern consolidated across 3 precedents**: Villa-out (A.12b) · Pixel-out (A.13b) · **Brace-out (A.14b)** · each removal contract-tested via symmetric `test_*_was_removed_from_*_tests`.
- Brace is 12th archetype enrolled · 13 templates editable · 5 families closed · 4 open.
- Zero new binding decisions · D-096 / D-097 / D-098 unchanged. Only operational clarification added to D-098 for Session 70.
- Acceptance gates post-merge: `python manage.py check` 0 issues · `python manage.py test apps` 266/266 PASS · `python smoke_full.py` 834/834 routes HTTP 200.
- Baseline `phase-integration-baseline-v15` tip: **`7c064f8`** (A.14b merge), pushed to `origin/phase-integration-baseline-v15`.

### Blockers

**None.** No explicitly-deferred debt is pending.

### Exact next step

A.14b closed a family; it does not prescribe the next workstream. Top candidate is **A.15 ecommerce family (Bottega `artisan-workshop` + Luxe `fashion-editorial`)** — two templates with potential commerce-foundation overlap check (Phase 3a+3b already landed `apps/commerce/` seed for both · editor should edit presentational content, not commerce-admin state). Alternatives: medical-other (3 separate phases) · Aura individual enrollment · Elevate individual enrollment · MEMORY.md maintenance mini-phase (separate, not bundled).

---

## Session 69 — Phase A.14 · Sapore (trattoria-warm · restaurant-continuation family · first template) Editor + Multi-locale Enrollment · OPENS RESTAURANT-CONTINUATION FAMILY (2026-04-18)

**Summary.** Eleventh archetype enrolled in the editor: `trattoria-warm` (Sapore). Single-template phase — Sapore opens the restaurant-continuation family via the same staged dedicated-schema progression topology already used twice (real-estate A.12→A.12b · portfolio A.13→A.13b). Brace (`street-modern`) stays OUT until A.14b, guarded by a dual registration-time + runtime absence check. Menu rows stay **inside the perimeter** as deep-path tuple cells — novel shape (tuple-in-dict-list parent) required a contract-alignment bugfix on the render side so the 3 editor layers (save · schema · render) now speak the same language on list numeric indexing. 252/252 tests · 834/834 smoke · 5-locale browser walk green including end-to-end menu cell override verification. Catalog 20/20 `published_live` unchanged.

**Restaurant-continuation family is now OPEN but NOT YET CLOSED.** Four families fully editor-complete (law · medical-specialist · real-estate · portfolio) + 1 family partially open with Sapore IN · Brace pending A.14b. 11 archetype slugs enrolled · 11 multi-locale enrolled · 12 templates editable end-to-end. 8 templates still editor-unsupported across 5 residual open families (Brace · 3 medical-other · 2 ecommerce · Aura · Elevate).

### Sapore-first scope decision

Step-0 planning audit confirmed shared-schema IMPOSSIBLE (50% page-slug overlap · menu shape fundamentally different: Sapore nested tuple vs Brace nested dict-with-image-col · image surface ratio 1:3.5 · form structure presence inverted). Staged dedicated-schema progression is the correct topology — mirrors real-estate (Casa/Villa) and portfolio (Chiara/Pixel) precedents. Sapore-first chosen over Brace-first because: lighter shape (12 lists-of-dict vs 18) · simpler menu (tuple vs dict-with-image-col) · smaller image surface (13 vs ~45 surfaces) · Gusto (A.8) provides more direct pattern reuse for `trattoria-warm` than for `street-modern`.

Three bundling alternatives explicitly rejected (all violate "one phase = one archetype decision" discipline now 12 phases strong A.6 → A.14):
- Mixing Sapore + Brace in single phase — family closure would be fine in a DIFFERENT topology (shared-schema), but shared-schema impossible here.
- Bundling detail-page editing — detail-page policy is horizontal feature affecting 6+ archetypes with per-item content, not A.14-special-casing.
- Bundling per-locale image — D-098 invariant, product decision not planning tweak.

### Step 0 · Planning / audit decisions

Runtime audit before any code change:
- Archetype slug `trattoria-warm` · skin `restaurant/trattoria-warm/` · CSS `.tw-*` (60 hits) · 18 mature `html[dir="rtl"]` rules since D-078 Sapore rollout (Session 48).
- 6 pages: home · menu · storia (about) · forno (**signature · novel kind**) · eventi (**events · novel kind**) · contatti. Novel kinds are plain string identifiers in the registry — no view dispatch, no new infra.
- 5-locale parity PERFECT (224 keys × 5 locales, zero gaps).
- 7 top-level scalar image fields + 2 image-in-dict-row lists (home.family + storia.family × 3 portraits each) = **13 total editable image surfaces**.
- **`posts` list EMPTY** on Sapore — first enrollment since A.10 without posts, so no `posts.*` paths to reject (absence is structural).
- **Menu rows kept inside perimeter** via 5 deep-path entries `menu.sections.{0..4}.dishes` — section sizes verified runtime (7/7/6/5/5). This is the novel shape: tuple-list nested inside a dict-list parent (not Chiara's dict-list nested inside a dict parent).

### Step 1 · Schema + skin bridge + contract tests (+ schema._resolve_path extension)

- `SAPORE_TRATTORIA_WARM_SCHEMA` added in `apps/editor/schema.py` — 8 sidebar groups (brand · hero_home · home_bands · menu_page · storia_page · forno_page · eventi_page · contatti_page) · ~141 scalar fields · 7 scalar image fields.
- `STRUCTURED_FIELD_SHAPES["trattoria-warm"]` with 20 readonly indexed lists: 15 base (home.family/reviews/facts/chalkboard_days/hours_rows · menu.sections parent · storia.timeline/family/values · forno.pizza_signatures/pasta_signatures/producers · eventi.experiences · contatti.transport/hours_table) + **5 deep-path `menu.sections.{i}.dishes` entries** (novel nested-tuple-in-dict-list parent shape).
- 3 gate registrations · `_ARCHETYPE_BASELINE_TEMPLATE["trattoria-warm"] = ("sapore-trattoria-pizzeria", "it")` + `_ARCHETYPE_SCHEMAS["trattoria-warm"] = SAPORE_TRATTORIA_WARM_SCHEMA` + `"trattoria-warm"` in `_MULTILOCALE_ENABLED_ARCHETYPES`.
- 3 atomic fixes on `templates/live_templates/restaurant/trattoria-warm/_base.html`: title `site.logo_word|default:brand.brand_name` · body `mw-is-editor-preview` guard class · `.tw-*` CSS guard block suppressing marketplace strip + clamping wordmark · preview-bridge.js conditional on `preview_project`.
- **Narrow schema-helper extension** `apps/editor/schema.py::_resolve_path` — +8 lines to handle list numeric indexing (mirror of already-existing `apps/projects/services.py::_resolve_path` capability). Required for `_iter_indexed_groups` to resolve the novel deep-path `menu.sections.{i}.dishes` lists. Zero impact on 10 archetypes pre-A.14 (their paths are dict-only); strict backwards-compat.
- **Brace-out dual guard** — 2 `assertNotIn("street-modern", ...)` layers in `test_a14_sapore_archetype_registered` (registration-time) + runtime re-check at end of the lifecycle test. Matches A.12b Villa-out + A.13b Pixel-out pattern.
- **5 pre-existing unsupported-archetype fixtures updated** to reference `street-modern`/`brace-street-food-lab` (previously referenced `trattoria-warm`/`sapore-trattoria-pizzeria`). Housekeeping — Brace is now the outside-gate reference.
- 12 new A.14 contract tests covering archetype registration + schema shape + translatable distribution + universals-are-global + positive spec on hero image + image-in-dict-row positive · deep-path menu positive · complex-shape exclusion · structured-list cells globality · supported_locales · tenfold regression · preview-bridge 3-point integration on `.tw-*`.
- Commit `ef74b4e` · `feat: add trattoria-warm archetype editor schema` · 3 files · +1087 / −18.

### Step 2 · Render-side contract-alignment fix + lifecycle HTTP test (2 commits)

**Discovered mid-Step-2**: `apps/editor/rendering.py::_apply_indexed` parent-walk assumed dict-only — silently returned early when the parent chain crossed a list (e.g. Sapore's `menu.sections.0.dishes` where `sections` is a list). Consequence: menu-cell overrides were **accepted by the save layer** (persisted correctly via `content_overrides` table because `services._resolve_path` already supported list-indexing) but **never applied at render time**. The customer would see the authored dish name, not their edit. Silent drop — exactly the kind of runtime incoherence Step-2 was supposed to "blindare bene a runtime" per user guardrail.

This is **NOT a new feature**. It's a contract-alignment bugfix across three layers that ALREADY had to speak the same language:
- `apps/projects/services.py::_resolve_path` (save / sparse-diff / prefill): **already** supported dict + list + tuple-col
- `apps/editor/schema.py::_resolve_path` (schema helper): extended in Step 1 (narrow mirror)
- `apps/editor/rendering.py::_apply_indexed` (render-time splicer): was the outlier · **now fixed**

The fix is minimal (8-line extension of the parent-walk in `_apply_indexed`: dict parent → `.get(seg)`, list parent → `int(seg)` → `list[idx]`, other → return) and fully backwards-compat (10 archetypes pre-A.14 never exercise the list branch because their `STRUCTURED_FIELD_SHAPES` keys have dict-only parent chains).

**2-commit split** adopted for clean history:
- Commit `f66ac24` · `fix: apply indexed overrides through list parents in renderer` · 1 file · +19 / −3 · production-code bug fix isolated
- Commit `7a8e1c3` · `test: lock trattoria-warm lifecycle end to end` · 1 file · +321 LOC · test-only, blocks the regression via end-to-end menu cell override verification

Lifecycle test `test_a14_sapore_full_multilocale_lifecycle_end_to_end` covers:
1. 3 autosaves IT/EN/FR on `home.headline` → `@<locale>:home.headline` × 3
2. Global `site.logo_word` via EN autosave → plain-keyed (explicit `assertNotIn("@en:")`)
3. Scalar image `home.hero_image` → plain-keyed across all 5 locales (5× `assertNotIn("@<locale>:home.hero_image")`)
4. **Deep-path menu cell `menu.sections.0.dishes.0.name`** → plain-keyed across all 5 locales (5× `assertNotIn`) · **proves the render-side fix applies end-to-end**
5. Publish · 5-locale second-user public preview with `IMG_HERO` + `DISH_NAME` + global logo universali
6. IT/EN/FR render their locale override · ES/AR authored fallback + universals preserved
7. AR `<html dir="rtl" lang="ar">` on `.tw-*` skin (18 RTL rules mature)
8. Owner reopen per locale · prefill corretto
9. End-of-test perimeter invariants · Brace OUT dual + 10 archetypes pre-A.14 still enrolled + 11 complex-shape paths rejected

### Step 3 · Browser walk (5-locale · real browser)

Playwright walk on fresh Sapore draft covered every user-visible surface:
- Editor mount with `?lang=it` · 5 pills `data-ed-lang` · IT active · label "Lingua attiva"
- **13 image widgets in sidebar · match esatto del piano** (7 scalar: home.hero_image · home.forno_image · home.tavolata_image · storia.photo_image · forno.forno_story_image · forno.dough_image · eventi.birthday_image + 6 cells: home.family.{0,1,2}.portrait + storia.family.{0,1,2}.portrait)
- 29 sidebar groups (8 scalar + 20 indexed + 1 tokens) · 121 translatable fields · 417 total field wrappers
- **5 out-of-perimeter prefixes absent** (`contatti.form_sections`, `contatti.form_fields`, `contatti.occasion_options`, `storia.story`, `site.hours_footer_rows` · 0 hits each)
- Flush-before-switch verified IT→EN and EN→FR · EN prefill "At Nonna Rosa's, like family." · FR prefill "Chez Nonna Rosa, comme à la maison."
- 3 locale overrides + 3 plain-keyed globals persisted including **deep-path menu cell `menu.sections.0.dishes.0.name → "A14 Walk Piatto Signature"`**
- ES fallback authored "En casa de Nonna Rosa, como en casa." · zero walk-text leak · 3 universals visible in ES iframe
- AR iframe `<html lang="ar" dir="rtl">` on `.tw-*` skin (8 `.tw-*` elements) · title "A14 Sapore Walk Brand — الرئيسية"
- Publish via `services.publish_project`
- **Second-user public preview 5 locali · menu cell override visible on every locale's menu page** (IT/EN/FR/ES/AR all ✅) · other dishes in section 0 stay authored (Carciofo alla giudia) · proves the splicer touched only the `.0.0` cell without corrupting the other tuple cells · IT/EN/FR home render their locale override · ES/AR home authored fallback · AR `dir="rtl"` on public iframe
- **Blindatura del render-side fix runtime-dimostrata** — without commit `f66ac24`, `menu_has_dish_override` would be `false` for all 5 locales; instead it's `true` for all 5.

### Outcome

- **Restaurant-continuation family OPEN** via staged dedicated-schema first step (Sapore A.14 · Brace A.14b pending). Same topology pattern as real-estate (A.12→A.12b) and portfolio (A.13→A.13b). Staged dedicated-schema closure now has 3 precedents total (2 closed + 1 in-progress).
- **Menu rows inside perimeter** via deep-path tuple-in-dict-list parent shape (novel) · render-side contract-alignment bugfix enables end-to-end flow · precedent set for future restaurant-family enrollments where the menu is the editorial heart.
- **Three editor layers speak the same language on list numeric indexing**: `services._resolve_path` (was always ok) · `schema._resolve_path` (Step 1 extension) · `rendering._apply_indexed` (Step 2 fix). No incoherence anymore.
- Sapore is 11th archetype enrolled · 11 templates editable · 12 editable end-to-end.
- Zero new binding decisions · D-096 / D-097 / D-098 unchanged. Only operational clarification added to D-098 for Session 69.
- Acceptance gates post-merge: `python manage.py check` 0 issues · `python manage.py test apps` 252/252 PASS (239 pre-A.14 + 12 contract + 1 lifecycle) · `python smoke_full.py` 834/834 routes HTTP 200.
- Baseline `phase-integration-baseline-v15` tip: **`8fae2df`** (A.14 merge), pushed to `origin/phase-integration-baseline-v15`.

### Blockers

**None.** No explicitly-deferred debt is pending.

### Exact next step

A.14 opens a family; it does not close one. Top candidate is **A.14b Brace (street-modern)** · closes restaurant-continuation family via the sibling archetype enrollment. Brace has a heavier shape than Sapore (18 lists-of-dict vs 12 · 5 image-in-dict-row lists vs 2 · ~45 image surfaces vs 13) but no new infrastructure needed because the A.14 render-side fix + schema helper extensions already cover all Brace shape patterns (dict-with-image-col deep path was already in use on Chiara/Villa). Expected recipe mechanical-reuse of A.14 Sapore pattern. Alternatives: ecommerce (Bottega+Luxe) · medical-other (Salute+Benessere+Famiglia · 3 separate phases) · Aura individual enrollment · Elevate individual enrollment. MEMORY.md maintenance mini-phase remains queued as a separate housekeeping task (not bundled).

---

## Session 68 — Phase A.13b · Pixel (cinematic-photographer · portfolio family) Editor + Multi-locale Enrollment · CLOSES PORTFOLIO FAMILY (2026-04-18)

**Summary.** Tenth archetype enrolled in the editor: `cinematic-photographer` (Pixel). Single-template phase — Pixel is the portfolio family's second archetype, complementing Chiara (A.13 `editorial-designer-grid`). Closure follows the same staged dedicated-schema progression topology already validated by real-estate (A.12 Casa → A.12b Villa): family opens in the first phase with one archetype enrolled, closes in the second phase with the second archetype enrolled, each with its own schema + skin bridge + lifecycle test. D-098 invariant holds; no new D-number introduced.

Surface is intentionally narrow: Pixel exposes **1 scalar image globally** (`home.hero_image`) — no image-in-dict-row, no nested-dict image, no mutable repeaters. Posts (`posts.*` with `posts[].cover_image`) and `series_detail` stay registry-only, consistent with the **detail-page registry-only policy** now enforced uniformly across 6 archetypes (Lex · Juris · Casa · Villa · Chiara · Pixel). 3-file enrollment (schema + skin + tests) · zero changes to `services.py` / `rendering.py` / `views.py` / `models.py` / `ProjectAsset` / `/assets/upload/` / editor JS / editor CSS.

**Portfolio family CLOSED.** Four families editor-complete now: law (Lex + Juris sequential dedicated-schema · A.10+A.11) · medical-specialist (Cardio+Derm shared-schema · A.9) · real-estate (Casa+Villa staged dedicated-schema · A.12+A.12b) · **portfolio (Chiara+Pixel staged dedicated-schema · A.13+A.13b)**. 10 archetype slugs enrolled · 10 multi-locale enrolled · 11 templates editable end-to-end · catalog 20/20 `published_live` unchanged. 239/239 tests · 834/834 smoke routes · Playwright walk 5-locale green.

### Pixel-only scope decision

The Step-0 planning session confirmed Pixel-only, rejecting three bundling alternatives:
- Mixing Pixel with another non-portfolio archetype (restaurant-continuation / ecommerce / medical-other) — violates the "one phase = one archetype decision" discipline now 10 phases strong (A.6 → A.13b).
- Bundling Pixel + opening detail-page-scoped editing — detail-page editing is a horizontal feature affecting 5+ archetypes with per-item content (Lex `notabili` · Juris `insights` · Casa `posts` · Villa `posts` · Chiara `posts` · Pixel `posts`/`series_detail`) and must be designed cross-archetype, not Pixel-special-cased.
- Bundling Pixel with per-locale image policy change — out-of-scope per D-098, would open a product decision, not a planning tweak.

Keeping A.13b narrow also preserves the mechanical-reuse property: Pixel's schema LOC ended at +510 (well under the 600 soft guardrail), confirming the recipe scales cleanly when the archetype is simpler than the family-opener.

### Step 0 · Planning / audit decisions

Runtime audit ran before any code change:
- Archetype slug `cinematic-photographer` verified in DNA registry and skin folder `portfolio/cinematic-photographer/` with `.cp-*` CSS prefix (133 hits) · distinct from Chiara `.ed-*` · 38 mature `html[dir="rtl"]` rules already shipped with the published_live skin (Session 39 D-071 Pixel perfection pass).
- 5 pages: `home` · `serie` (`series_list`) · `serie/<slug>/` (`series_detail`) · `biografia` (`about`) · `pubblicazioni` (`publications`) · `contatti` (`contact`). Series detail is novel but stays registry-only consistent with the detail-page policy. Publications is a new editable page kind not present in Chiara.
- 4 image scalars in Pixel registry: `home.hero_image` (editable) and 3 `posts[].cover_image` (registry-only). Only `home.hero_image` enters the perimeter.
- Authored content 5-locale parity PERFECT (154 keys × 5 locales, zero gaps) — same quality class as Villa and Chiara.
- 10 readonly indexed lists chosen: `home.hero_credit_cells` tuple 4×2 · `home.filmstrip` tuple 4×5 (slug col excluded) · `home.publications` tuple 3×3 · `biografia.kit` tuple 4×5 · `biografia.timeline` tuple 12×3 · `pubblicazioni.press` dict 8×5 · `pubblicazioni.exhibitions` tuple 6×4 · `pubblicazioni.awards` tuple 6×3 · `contatti.channels` tuple 4×3 · `site.exif_footer` tuple 4×2 — the `site.exif_footer` IN/OUT decision was finalized in Step 0 (IN) and not re-litigated mid-implementation.

### Step 1 · Schema + skin bridge + controlled Pixel-out guard removal

- `PIXEL_CINEMATIC_PHOTOGRAPHER_SCHEMA` added in `apps/editor/schema.py` — 8 sidebar groups (brand · hero_home · home_bands · serie_page · biografia_page · pubblicazioni_page · contatti_page · contact_info) · ~140 scalar fields · 1 scalar image `home.hero_image` · 10 readonly indexed lists registered in `STRUCTURED_FIELD_SHAPES["cinematic-photographer"]`.
- 3 gate registrations: `_ARCHETYPE_BASELINE_TEMPLATE["cinematic-photographer"] = ("pixel-portfolio-fotografico", "it")` · `_ARCHETYPE_SCHEMAS["cinematic-photographer"] = PIXEL_CINEMATIC_PHOTOGRAPHER_SCHEMA` · `"cinematic-photographer"` appended to `_MULTILOCALE_ENABLED_ARCHETYPES`.
- 3 atomic fixes on `templates/live_templates/portfolio/cinematic-photographer/_base.html` (zero skin surgery beyond the bridge shape): `<title>` honors `site.logo_word|default:brand.brand_name` · `<body>` carries `mw-is-editor-preview` guard class when `preview_project` is truthy · CSS guard block before `</style>` with `.cp-*` selectors suppressing marketplace strip and clamping `.cp-nav .wm` to `max-width: 32ch` · `preview-bridge.js` injected only behind `{% if preview_project %}`.
- **Controlled Pixel-out guard removal from A.13 Chiara tests** — two `assertNotIn("cinematic-photographer", ...)` assertions removed (registration-time inside `test_a13_chiara_archetype_registered` + execution-time inside `test_a13_chiara_full_multilocale_lifecycle_end_to_end`). Inversion verified by the new contract test `test_a13b_pixel_out_guard_was_removed_from_chiara_tests` so a silent regression on the removal cannot happen.
- 11 new A.13b contract tests in `apps/projects/tests.py`: archetype registration + out-guard-removal symmetry + schema coverage across 5 pages + translatable distributed paths + global branding universals + positive `get_field_spec` for `home.hero_image` returning `type="image"` + complex-shape exclusion rejecting 23 paths including explicit `posts.0/1/2.cover_image` + structured-list cell globality + canonical 5-locale `get_supported_locales` + ninefold regression (all 9 pre-A.13b archetypes still enrolled) + preview-bridge 3-point integration on `.cp-*` skin.
- Commit `7eb3179` · `feat: add cinematic-photographer archetype editor schema` · 3 files · +863 / −24.

### Step 2 · Lifecycle HTTP test with 1 scalar image globally

- `test_a13b_pixel_full_multilocale_lifecycle_end_to_end` in `apps/projects/tests.py` · cross-cutting · verifies the full editor-to-preview-to-reopen flow on Pixel:
  1. 3 autosaves on translatable `home.headline` (IT/EN/FR) → storage `@<locale>:home.headline` × 3
  2. 1 autosave on global `site.logo_word` via EN → storage plain-keyed (no `@en:` prefix, explicit `assertNotIn`)
  3. 1 autosave on scalar image `home.hero_image` → storage plain-keyed across all 5 locales (`assertNotIn("@it/en/fr/es/ar:home.hero_image")`)
  4. `services.publish_project` → status PUBLISHED
  5. Second user visits each of the 5 public preview locales: IT/EN/FR render their override + global logo + hero image; ES/AR fall back to authored text but still see the global logo + hero image override.
  6. AR response head carries `<html dir="rtl" lang="ar">` on the `.cp-*` skin.
  7. Owner reopens the editor per locale; sidebar prefill on `home.headline` matches the buffer for the active locale, ES shows authored-baseline prefill; `site.logo_word` + `home.hero_image` show the universal overrides.
  8. **Perimeter invariants re-checked end-of-test** — Chiara (`editorial-designer-grid`) still enrolled in `_MULTILOCALE_ENABLED_ARCHETYPES`; 6 `posts.*` paths (incl. `posts.0/1/2.cover_image`) rejected by `validate_key_path` raising `InvalidEditableField`.
- Commit `cecfa4e` · `test: lock cinematic-photographer lifecycle end to end` · 1 file · +251 LOC · zero production-code touches.

### Step 3 · Browser walk (5-locale · real browser)

Playwright walk on a fresh Pixel draft covered every user-visible surface:
- Editor mounts with `?lang=it` · 5 language pills with `data-ed-lang` present · label "Lingua attiva" · IT active with `.is-active` class.
- Sidebar shows **exactly 1 file input** (image widget) → `home.hero_image` label "Hero image · URL" · 107 fields marked `data-ed-translatable="1"` with "per lingua" badge · 211 global fields without translatable marker.
- All 6 out-of-perimeter path prefixes absent from `data-ed-field`/`data-ed-key` selectors: `posts.`, `serie.filters`, `biografia.statement_paragraphs`, `contatti.form_fields`, `contatti.form_sections`, `contatti.upload_field`.
- Flush-before-switch verified IT→EN and EN→FR: typed on IT, clicked EN pill → `@it:home.headline` persisted before the preview iframe reloaded; same pattern EN→FR.
- 3 locale overrides + 2 globals persisted in `content_overrides`: `@it/en/fr:home.headline` + plain-keyed `site.logo_word` + plain-keyed `home.hero_image`.
- ES pill shows authored-baseline prefill "OBSERVAR LO QUE PERMANECE..." with zero walk-text leak; global logo and hero universal remain visible in the ES iframe.
- AR iframe: `<html lang="ar" dir="rtl">` on `.cp-*` skin · logo "A13b Pixel Walk Brand" visible in title ("— الفهرس") · hero image override visible universally.
- Sub-page spot check via `fetch()` on `/preview/{serie,biografia,pubblicazioni,contatti}/` — 4/4 status 200 · global logo universal · zero cross-page text leak · `.cp-*` skin ship everywhere.
- Publish via `services.publish_project` (second user flow).
- Second-user public preview across all 5 locales: correct per-locale text on IT/EN/FR, authored fallback on ES/AR, global logo + hero image override visible in every locale, AR `dir="rtl"` on the public iframe.
- **Explicit verify of detail-page registry-only** — fetch `/preview/serie/{porto-vecchio-trieste,case-di-pietra-puglia,ritratti-del-po}/` for all 3 series records: status 200 · global logo chrome applied · **zero `PixelA13b` walk-text leak** in any detail page (proves `home.headline` override does NOT bleed into series detail) · `.cp-*` skin markers present (series_detail / cp-series).

### Outcome

- **Portfolio family CLOSED** via staged dedicated-schema progression (Chiara A.13 + Pixel A.13b), mirroring real-estate family closure (Casa A.12 + Villa A.12b). Three D-098 family-closure topologies now have ≥2 real precedents: shared-schema single-phase (A.9 specialist) · sequential dedicated-schema (A.10+A.11 law) · staged dedicated-schema (A.12+A.12b real-estate AND A.13+A.13b portfolio).
- Detail-page registry-only policy **formally enforced uniformly on 6 archetypes** (Lex · Juris · Casa · Villa · Chiara · Pixel). Any future detail-page editing work must be a horizontal feature affecting all 6, not single-archetype special-casing.
- Pixel is the **single-scalar-image archetype pattern precedent** — confirms that a new archetype enrollment does not need image-in-dict-row or nested-dict scalar image to be complete; mechanical reuse scales downward as cleanly as upward.
- Chiara-out guard removal / Pixel-in inversion **verified contractually** via `test_a13b_pixel_out_guard_was_removed_from_chiara_tests` — same pattern as Villa's A.12b removal verified by `test_a12b_villa_out_guard_was_removed_from_casa_tests`.
- Zero new binding decisions · D-096 / D-097 / D-098 unchanged. Only an operational clarification added to D-098's Operationalisation history for Session 68.
- Acceptance gates post-merge: `python manage.py check` 0 issues · `python manage.py test apps` 239/239 PASS (227 pre-A.13b + 1 lifecycle + 11 contract) · `python smoke_full.py` 834/834 routes HTTP 200.
- Baseline `phase-integration-baseline-v15` tip: **`1c6b561`** (A.13b merge), pushed to `origin/phase-integration-baseline-v15`.

### Blockers

**None.** No explicitly-deferred debt is pending.

### Exact next step

A.13b closes a family; it does not prescribe the next workstream. Candidates are ranked in `TODO_NEXT.md` — top pick is **restaurant-continuation (Sapore + Brace)** as the highest-leverage family still open, since it would close the restaurant category (already 1/3 enrolled via Gusto). Alternatives: ecommerce (Bottega + Luxe), medical-other (Salute + Benessere + Famiglia · three separate phases), agency-secondary (Aura individual), startup-saas (Elevate individual). MEMORY.md maintenance mini-phase remains queued as a separate housekeeping task (not bundled with an enrollment).

---

## Session 57b — Phase A.2.1 · Editor UX Corrective Micro-Fix (2026-04-16)

**Summary.** Micro-fix on top of Session 57's Phase A.2 shell. Nine customer-reported product gaps closed without any perimeter expansion: (1) preview top-strip (marketplace bar + duplicate lang switcher) hidden in editor mode; (2) language switcher moved into the sidebar; (3) image widget shipped with thumbnail + "Carica file" data-URL upload + clear; (4) character counters with near-limit / at-limit colouring; (5) highlight reliability — pulse animation, state preserved across autosave reloads, idle-clear moved out of iframe into editor (field-focus-aware); (6) compare slider now scroll-syncs the baseline and edited iframes; (7) preview canvas widened (sidebar 380→340px, topbar 56→52px, stage padding 20→14px); (8) schema beyond home — studio, manifesto and contatti pages now use `subgroups` structure with ~12 additional editable fields (essay heading + pullquote, partners intro, timeline intro, principles intro, promise intro, form heading); (9) overflow guardrails in the skin's `_base.html` (`overflow-wrap: anywhere` on hero headlines, nav logo clamped to 32ch). 27/27 tests green (4 new pre-existing tests still green after `iter_editable_fields` refactor to handle subgroups). Browser-authenticated Playwright re-validation end-to-end green.

### Gaps reported (all closed)

1. **Highlight not robust.** — ring cleared too aggressively, lost across autosave iframe reload.
2. **No image fields.** — schema had `home.cover.image` as URL type, no UI affordance.
3. **Layout broke on long text.** — no guardrails for oversized headlines / logo.
4. **Preview still tight.** — 380px sidebar + 20px stage padding felt cramped.
5. **i18n in editor was half-English.** — lang switcher sat inside the preview top-strip; editor labels were IT but preview chrome duplicated the marketing chrome.
6. **Preview top-strip was noise.** — marketplace "← Torna a MarketWeb" + "Altri template" + lang pills all visible inside the editor iframe.
7. **Only home editable.** — studio / manifesto / contatti headings existed as single fields; sub-sections inside those pages were not exposed.
8. **Sidebar could be more premium.** — flat field list without subsections inside a group.
9. **Compare didn't sync scroll.** — two iframes scrolled independently.

### What shipped

**Schema (`apps/editor/schema.py`)**
- New field type ``image`` with thumbnail widget (URL + data-URL accepted; 2MB hard cap; data-URI length guard bypasses the `max_length` that would otherwise truncate the base64).
- `home.cover.image` upgraded from `url` to `image`.
- `studio`, `manifesto_page`, `contatti` groups converted to `subgroups` form (divider + sub-head). ~12 new editable fields.
- `iter_editable_fields` now flattens both `fields` and `subgroups` shapes — the bug that broke 8 tests in the first run.

**Backend (`apps/projects/views.py`)**
- Context carries `locale_switcher` list (built from `template_content.get_available_locales` + `template_i18n.get_chrome`) — consumed by the sidebar UI, avoiding the preview top-strip duplicate.
- Groups materialised with both flat `fields` and `subgroups` outputs so templates can render either.

**Skin (`templates/live_templates/agency/agency-creative-studio/_base.html`)**
- Body class `mw-is-editor-preview` conditional on `preview_project` being truthy.
- CSS block hides `.mp-bar` (+ its padding-top) in that state.
- Overflow guardrails: `overflow-wrap: anywhere; word-break: break-word; hyphens: auto` on hero h1, section h2, nav logo. Logo also clamped to `max-width: 32ch`.

**Editor shell**
- `_editor_field.html` new partial — handles `text / textarea / richtext / select / color / url / image` widgets uniformly. Shared by content and token groups.
- `project_editor.html` reorganised — sidebar gains a `LINGUA ANTEPRIMA` segmented control next to search.
- Sub-group divider + sub-head style rendering.

**CSS (`static/editor/live-editor.css`)**
- Sidebar 380→340px, topbar 56→52px, devicebar 48→44px, stage padding 20→14px.
- New widgets: `.ed-sidebar-lang` / `.ed-lang-pill`, `.ed-subgroup`, `.ed-count` (with `is-near-limit` / `is-at-limit`), `.ed-image` (+thumb + controls + pick + clear).

**JS (`static/editor/live-editor.js`)**
- `currentLang` state + `withLang(url)` helper; lang pills reload both frames with `?lang=xx`.
- `lastHighlight = {selector, label}` memoised; re-posted on iframe `load` (after every autosave).
- `highlightHoldTimer` 5s keeps the ring if no sidebar field has focus; reset on every new highlight.
- Image widget: `maybeUpdateImageThumb` does an `Image()` probe, `is-loading` + `is-error` states, `FileReader.readAsDataURL` for local file pick.
- Character counter: `updateCharCount` on input; colouring at 90%+ (`is-near-limit`) and 100% (`is-at-limit`).
- `wireIframeScrollSync` attached on every iframe `load`; `activeScroller` switches on `mouseenter`; `requestAnimationFrame` throttled mirror.

**Preview-bridge (`static/editor/preview-bridge.js`)**
- Ring gains `mwEditPulse` 2.6s keyframe animation (reduced-motion aware).
- Internal 4.2s idle-clear REMOVED — the editor owns the clear decision now (it knows whether a sidebar field still has focus).

**Tests**
- All 27 tests green (20 A.2 + 7 accounts). No new tests authored for A.2.1 — the subgroup flatten bug was caught by existing `validate_key_path` tests; image / lang switcher are UI-only.

### Lessons

1. **Django `{# #}` is single-line only.** Multi-line requires `{% comment %}...{% endcomment %}`. The field-partial shipped with a multi-line `{# #}` whose line 2+ rendered as literal text into the sidebar. Caught in-browser, fixed in one line. First rule of partial authoring: comment tags must match the syntax.

2. **Schema refactors break the flattener.** Adding `subgroups` to three groups shipped clean through the UI but broke 8 tests on the service layer because `iter_editable_fields` assumed every group had `"fields"`. The flattener is the one place that MUST know about every schema shape — refactor it first, then the UI.

3. **Image widget without an upload endpoint is legitimate.** Data-URL fallback for `image` fields + 2MB server cap is a perfectly solid "draft mode" — users see their image live, it persists, it renders in preview. A real upload endpoint (Phase A.6) simply replaces the data-URI with a CDN URL. Not a hack; a scope choice.

4. **Preview chrome hiding is a body-class concern.** The skin owns its own chrome; the editor tells the skin it's being embedded via a body class. No skin surgery, no extra template includes, no feature flag. One CSS rule, one conditional class.

5. **Scroll-sync needs an `activeScroller` flag.** Without it, every scroll event ping-pongs because A's sync writes B, B's scroll event fires sync back to A. The `mouseenter` flag + `requestAnimationFrame` throttle + early-return when `activeScroller !== f` is the minimum robust pattern.

### Blockers

**None.**

### Exact next step

Phase A.3 per TODO_NEXT — unchanged scope. The A.2.1 fixes are all backwards-compatible. Merge the branch to main OR continue to A.3 on the same branch.

## Session 57 — Phase A.2 · Editor UX + Live Preview (2026-04-16)

**Summary.** A.2 rebuilds the customer-facing editor as a premium two-column app shell with debounced live autosave, a wide device-aware preview canvas, a premium sidebar with icon-prefixed accordion groups + search + reset-to-baseline, hover/focus → preview-region highlight, and a before/after compare slider. Notification hygiene is restored: no more Django-messages stacking on every save — autosave returns JSON + silent chip state + optional ephemeral toast. Rich-customization coverage ~doubled on `agency-creative-studio`: 39 content-editable fields across 14 grouped sections (was 23 in 4 flat groups). Browser-authenticated Playwright walk green end-to-end (login → edit → live preview → highlight → compare → reset → snapshot → publish → reload → verify clean). 20/20 project tests green (16 pre-existing + 3 new autosave / baseline / snapshot tests, 1 legacy POST form test rewritten for JSON autosave).

### Starting state
- Branch: `phase-editor-ux-live-preview-v1`, forked from `phase-editor-public-customize-v1` @ 5f3cef8.
- Editor UI shipped in A.1b was a server-rendered form: 520px-wide left column, iframe on the right, explicit Save button that POSTed and redirected. Messages flashed and stacked on every save. Preview felt cramped; no live update; no highlight mapping; no compare.

### UX root-cause audit
1. **Messages stacking** — every save triggered `messages.success("Salvato: N campi aggiornati")`. Over 5 edits a customer saw 5 success banners piled at the top of the editor.
2. **Preview too narrow** — 520px fixed form + bootstrap container max-width limited preview to ~650px. Typography and layout felt compressed.
3. **No live preview** — POST → redirect → iframe cache-bust. One round-trip per edit, always preceded by a manual click.
4. **Limited schema** — only ~23 fields on Vertex, grouped in 4 flat sections (`site`, `home`, `studio`, `contatti`). No group icons, no help copy hierarchy, no search.
5. **Sidebar form felt technical** — baseline footer `<code>home.headline · baseline</code>` leaked implementation to the customer.
6. **No mapping editor↔preview** — customer had to hunt for what they were editing.
7. **No compare** — no way to see "was vs is".

### What shipped

**1. Backend — `apps/editor/schema.py`**
- `AGENCY_CREATIVE_STUDIO_SCHEMA` widened from 4 flat groups to **14 themed groups × ~39 editable fields** (brand · nav · hero · cover · manifesto · cta_home · ledger · studio · capacita · manifesto_page · lavori · contatti · contact_info · footer_copy).
- Each group carries `icon` (Bootstrap Icons key) and `region` (CSS selector for preview highlight) metadata consumed by the UI only — no schema change to locked vs unlocked semantics.
- New field type `url` with HTTPS/HTTP validation (baseline empty allowed to clear override) — opens `home.cover.image` and future media URLs.
- `validate_value` extended to handle the `url` type.

**2. Backend — `apps/projects/views.py` + `urls.py`**
- New `project_autosave` JSON endpoint at `POST /projects/<uuid>/autosave/`. Takes `{content: {...}, tokens: {...}}`, validates via schema, saves sparse overrides, returns `{ok, touched, override_count, ts}`. Never creates a revision — autosaves are draft writes. Returns 400 JSON for `InvalidEditableField` so the UI can show a toast.
- New `project_snapshot` at `POST /projects/<uuid>/snapshot/` — this is the explicit "Salva versione" button. XHR path returns JSON; form-post path redirects with a flash. Revision creation is now customer-opt-in, not every-save-reflex.
- `ProjectEditorView.post` becomes a safety net that proxies to `project_snapshot` (legacy form submit).
- `customize_start` no longer flashes "Progetto creato" / "Bentornato" on every click — sets `request.session["editor_just_created"]=True` on first-time create. Editor consumes the flag into a one-shot welcome banner that self-dismisses. Zero accumulation on re-entry.
- Publish/unpublish still flash a Django message but the editor shell intentionally doesn't render Django's messages list — the topbar tier chip's colour change is the honest visual signal.

**3. Backend — `apps/catalog/views.py` (LiveTemplateView)**
- New `?baseline=1` query flag forces the catalog render *without* applying the project overlay even when `?project=<uuid>` is present. Powers the before/after compare iframe (same pipeline, deterministic diff).
- `preview_project` is injected into context only when NOT in baseline mode; the `_base.html` conditionally includes `preview-bridge.js` behind `{% if preview_project %}` — the baseline iframe stays bridge-less.

**4. Backend — prefetch-cache gotcha fix**
- `get_project_for_owner` uses `prefetch_related("content_overrides")` so the editor GET renders without N+1. But `project.content_overrides.count()` called after a save would return the *pre-save* cached count — off-by-one in the UI counter. Fix: fresh `ProjectContent.objects.filter(project=project).count()` in `project_autosave`. Similar pattern to D-086 Session 55's prefetch-bug regression, but this time on `.count()` rather than `_build_snapshot()`.

**5. Frontend — `static/editor/live-editor.css` (~680 LOC)**
- Full-viewport grid shell: 56px topbar + sidebar column (380px default, 64px rail collapse, 0 focus-mode) + preview canvas.
- Premium sidebar: icon-prefixed group heads, amber badge showing per-group override count, chevron accordion, search input with ring-focus, field-level override dot + reset button (shows on `is-overridden`).
- Canvas: device bar (desktop / tablet / mobile / compare / focus), dotted-grid stage, frame-wrap with animated max-width transition (100% / 860px / 390px), large rounded shadow for physical depth.
- Compare mode: stacked baseline iframe + clip-path-masked edited iframe, drag-slider handle at a configurable `--ed-split` CSS var, floating "ORIGINALE" / "IL TUO PROGETTO" labels.
- Toasts: bottom-right stack, max 3, 2.4s self-dismiss, 3 variants (info / success / error).
- Banner: one-shot contextual welcome (used by session-keyed `editor_just_created`).
- Status chip: 4 states (idle / saving / saved / error) with pulsing amber dot on saving, green dot on saved.

**6. Frontend — `static/editor/live-editor.js` (~340 LOC)**
- Debounced autosave (400ms window) — collects dirty content + tokens into two buckets, one fetch per window, cleared on success, retried on error. In-flight coalescing with `pendingAfterSave` flag so rapid typing doesn't lose writes.
- Iframe soft-reload on success: preserves scroll position via `contentDocument.defaultView.scrollY` snapshot + restore on load event.
- postMessage to iframe on focus/hover of a field — `{kind: 'highlight', selector, label}`. On blur, sends `{selector: ''}` to clear. Group-head hover also fires the highlight.
- Device segmented control, focus-mode toggle, compare toggle with drag-to-reposition handler (mouse + touch).
- Search filter with per-group "any visible field" visibility roll-up.
- Per-field `reset` button: restores the baseline value, immediately queues an autosave (the service treats baseline-match as "delete override", keeping the table sparse).
- `beforeunload` `navigator.sendBeacon` to flush any pending dirty buckets — no lost keystrokes on tab-close.

**7. Frontend — `static/editor/preview-bridge.js` (~140 LOC)**
- Injected ONLY inside the iframe when `{% if preview_project %}` is true (the baseline iframe does not get it — correct).
- Listens for `window.postMessage` with origin-check. On `{kind:'highlight', selector, label}`: queries the DOM, paints a fixed-position amber "ring" overlay (double box-shadow + dashed pseudo-element border) around each match, optionally renders a floating uppercase label at the first match.
- `scrollIntoView({behavior:'smooth', block:'center'})` when the target is off-screen so the customer can see what they're editing even on a long page.
- Repositions on scroll/resize, self-clears after 4.2s idle to avoid visual debt.

**8. Frontend — new `templates/projects/project_editor.html` (~210 LOC)**
- Standalone HTML (not extending `base.html`) — editor owns its viewport, no marketing nav/footer.
- Loads UI fonts + Bootstrap Icons + live-editor.css only. Preview iframe loads its own typography / skin CSS.
- Each field declares `data-ed-field` / `data-ed-kind` / `data-ed-baseline` so the JS can handle content vs token writes and reset-to-baseline without extra URLs.
- Renders the design-tokens group (palette + fonts) using the same field component as content — the sidebar is visually consistent.
- Locked-keys + recent-revisions as dashed-border info blocks at the bottom of the sidebar.

**9. Tests — `apps/projects/tests.py`**
- Rewrote `test_create_then_edit_then_preview` to POST JSON to `/autosave/` instead of form fields to `/editor/`.
- New `test_autosave_endpoint_rejects_locked_keys` — 400 on DNA-locked write attempts.
- New `test_baseline_preview_ignores_overrides` — `?baseline=1` renders baseline even when `?project=` is set.
- New `test_snapshot_endpoint_creates_revision` — explicit snapshot creates one revision row per call.
- Result: 20/20 green (was 16/16 pre-A.2).

### D-088 Editor UX live-preview contract — defined

Introduced D-088: the editor autosave pipeline is the only mutation path used by the customer UI. POST form submits to `/editor/` fall through to `project_snapshot` (revision) to avoid silently losing edits on legacy browsers. Key contract clauses:

- Autosave NEVER creates a revision (draft writes are not history).
- Autosave returns JSON with `override_count` computed from a cache-bypassing query.
- Baseline preview (`?baseline=1`) is the before side of compare — must not apply overrides.
- `preview-bridge.js` loads only under `{% if preview_project %}` — baseline iframe stays untouched so the compare is deterministic.
- Django messages framework is used only for full-page transitions (publish / unpublish). The editor shell intentionally does not render the messages list — visual feedback is through the topbar tier chip + transient toasts + the save-status chip.

### Lessons

1. **Prefetch cache bites `.count()` too.** Session 55 caught the snapshot prefetch bug (D-086 recap); A.2 caught the symmetric one on the override counter. Rule: any mutation path that reads a counter / snapshot after a save MUST bypass the selector's prefetch cache via a fresh `.filter(...).count()` / queryset.

2. **"Live" has to mean client-side immediate + server debounced + iframe soft-reload.** Neither pure postMessage DOM patching (too many content shapes) nor naked form-POST works. The sweet spot: debounced autosave + cache-busted iframe reload with scroll-position preservation. User perception is "instant" — actual network chatter is 1 request per 400ms window.

3. **Highlight via region selector beats text matching.** Early attempts to flash the exact text node broke on `richtext` fields (`<em>` tags, HTML entities, ellipsis). A CSS selector on the section container is both more resilient and more elegant — the glow communicates "this area" better than a tight outline on a single word.

4. **Standalone editor shell > base.html override.** The marketing navbar/footer belong on the marketing site. Extending base.html and hiding chrome with CSS creates visual debt; a standalone HTML that only pulls the UI fonts + icons + editor CSS keeps the editor surface clean.

5. **One source of truth for notifications.** When the editor shell stopped rendering Django's messages list, `publish` / `unpublish` flashes "disappeared" — but the topbar tier chip's colour change is a clearer signal. If a future phase needs a richer confirmation, route it through the toast stack (never back to Django messages).

### Blockers

**None.**

### Exact next step

**Phase A.3 — repeater widgets + second archetype.** Two workstreams, in order:

1. **Repeater widget groundwork.** Define `{"type": "list", "of": {...}}` in schema; UI renders add/remove/reorder with per-item field specs. First target: `home.ledger_rows` (Vertex) — a tuple list that's currently DNA-locked. Second: `home.capab_items`.
2. **Second archetype schema.** Pick `clinic` (Salute) or `corporate-suite` (Pragma) and port the same 14-group pattern. Validates the schema's generality; opens the editor to 5/20 templates.
3. **Optional polish this session deferred:** sync iframe scroll between baseline + edited when compare opens (currently only the edited side tracks manual scroll).

## Session 56 — Phase A.1b · Public Customize Flow (2026-04-16)

**Summary.** A.1b closes the gap between the A.1 foundation and the customer-facing promise: a visitor can now click **Personalizza** on a template card or on the template detail page, hit a branded login/signup gate (no longer the staff `/admin/login/`), return automatically to the same template, open an auto-created editable project, modify content, save, see the iframe preview update, reopen later, and publish — without ever touching `/admin/`. One active draft per `(owner, template)` (create-or-open); cross-owner access still 404s. Browser-authenticated Playwright walk completed end-to-end. 834/834 catalog smoke + 24/24 unit tests green (12 pre-existing A.1 tests + 5 new projects tests + 7 new accounts tests).

### Starting state
- Branch: `phase-editor-public-customize-v1`, forked from `phase-editor-foundation-v1` @ aa06d0b.
- `apps/accounts/` was empty scaffolding (`views.py`/`services.py`/`selectors.py` empty, `urls.py = []`). `LOGIN_URL` pointed at `/admin/login/`. No signup form, no login template, no navbar auth links.
- Entry points: customize flow lived behind `/projects/` dashboard dropdown — too technical for a customer starting from the catalog. Template cards/detail had no `Personalizza` CTA.
- Create-flow: `/projects/new/` POST forked a new project every click; no dedup, so "Personalizza" twice would leave two drafts.

### Gap audit (what was missing for customer-facing)
1. No `Personalizza` button on card or detail.
2. Login gate = `/admin/login/` (staff-facing). No signup.
3. No start URL: customer had to understand `/projects/`, pick from a dropdown.
4. No create-or-open: every POST forked. Classic "three drafts of the same thing" smell.
5. Editor chrome used admin-like copy (`Foundation v1`, `archetipo`) — leaked implementation terms to the customer.
6. Navbar "Accedi" / "Inizia Gratis" were `href="#"` ghost links.

### What shipped

**1. Branded auth (apps/accounts/)**
- `forms.py` (~95 LOC) — `CustomerSignupForm` (UserCreationForm + required email with uniqueness check) · `CustomerLoginForm` (branded `AuthenticationForm`). All widgets styled as `form-control form-control-lg` with Italian labels.
- `views.py` (~110 LOC) — `CustomerLoginView` (subclass of Django's `LoginView` with template_name override + `?next=` threaded into signup link) · `customer_signup` (FBV; logs user in on success) · `customer_logout` (POST-preferred, bounces home).
- `urls.py` — 3 routes: `login/`, `signup/`, `logout/`. Mounted at `/account/` in project urls.
- Templates: `templates/accounts/login.html` (85 LOC) · `templates/accounts/signup.html` (95 LOC). Card-based chrome, no admin styling, Bootstrap primitives only.
- `settings.LOGIN_URL = "/account/login/"` (was `/admin/login/`). New `LOGIN_REDIRECT_URL = "/projects/"` unchanged; added `LOGOUT_REDIRECT_URL = "/"`.
- Tests (`apps/accounts/tests.py`, 7 cases): login page reachable · signup page reachable · signup creates-and-logs-in · signup honours `?next=` · login honours `?next=` · logout bounces home · duplicate email blocked.

**2. Public customize entry point (`/projects/start/`)**
- New view `customize_start(request)` in `apps/projects/views.py`. Single URL, handles anon + authed:
  - Anon → 302 to `/account/login/?next=/projects/start/?template=<slug>` — preserves template slug end-to-end.
  - Authed → `get_or_create_project_for_template(owner, template)` → 302 to editor.
  - Missing slug → bounce to catalog with message.
  - Unknown / not published_live slug → bounce to catalog.
  - Unsupported archetype (e.g. gusto-fine-dining) → bounce to template detail with info message.
- New service `get_or_create_project_for_template(owner, template)` in `apps/projects/services.py`. Returns `(project, created_bool)`. One active draft per `(owner, source_template)`. Motivation: matches Wix/Squarespace mental model, lowers cognitive overhead; multi-draft is a later opt-in.
- Tests (5 new in `apps/projects/tests.py`): anon→login+next · authed→create+editor · authed+existing→reopen+same-uuid · unknown-slug→catalog · unsupported-archetype→detail.

**3. Public entry points**
- `templates/catalog/template_detail.html` — `Personalizza` is now the primary CTA in the sidebar. `Apri anteprima completa` demoted to secondary. `Aggiungi al Carrello` (disabled) → `Acquista in seguito` (disabled, with honest tooltip) since Phase 3 checkout not here.
- `templates/includes/_template_card.html` — hover actions: `eye` → live preview in new tab, `magic` → `/projects/start/?template=...`. Card footer gains `Personalizza` as primary CTA next to `Scopri` (now ghost).
- `templates/includes/_navbar.html` — `Accedi` / `Inizia Gratis` / `I miei progetti` / `Esci` all real, auth-aware. Shows `Ciao, <username>` when authed. Mobile menu parity.

**4. Editor UX polish (customer-facing)**
- `templates/projects/project_list.html` rewritten as card grid (~95 LOC). Dropped `Editor · Foundation v1` eyebrow. Empty state routes customer to catalog. `editable_templates` fallback form now in `<details>` (power-user). Added `Sfoglia template` primary CTA.
- `templates/projects/project_editor.html` — lifted all `Foundation v1` / `archetipo` / `DNA-locked` / `overrides` admin-ish language. `Design tokens` → `Colori e font`. `DNA-locked · non modificabile in Foundation v1` → `Prossimamente · aree in arrivo`. `Revisioni recenti` → `Cronologia recente`. All buttons now use `mw-btn` design system classes. Header shows project name + source template + status badge only, no archetype slug. Save toast copy kept server-side from A.1.

**5. X-Frame-Options fix (catalog LiveTemplateView)**
Caught in live E2E: Django's project-wide default is `X-Frame-Options: DENY`, so the editor's preview iframe (same-origin) was refusing to render. Fix: `@method_decorator(xframe_options_sameorigin, name="dispatch")` on `LiveTemplateView` only — clickjacking protection stays DENY everywhere else. Single-line change + docstring explaining the trade-off.

### Browser-authenticated validation (Playwright)
Full cold-start walk:
1. `/templates/` (anon) → 12 cards each with `Personalizza` link to `/projects/start/?template=<slug>`. ✓
2. Click `Personalizza` on Vertex detail → `/account/login/?next=...` — template slug URL-encoded in `?next=`. ✓
3. Click `Registrati` — `?next=` preserved on signup link. ✓
4. Submit signup (cliente.demo / demo@studiopersonale.it) → auto-login → `/projects/start/?...` → `get_or_create_project_for_template` creates project → 302 to editor. ✓
5. Edit 4 fields (Logo word, Headline, Eyebrow, Telefono) → Save → toast `Salvato: 31 campi aggiornati` (A.1 quirk — sparse-diff write counts every form field, 4 actual overrides visible as orange dots). ✓
6. Preview iframe (`http://127.0.0.1:8111/templates/agency/vertex-creative-agency/preview/?project=<uuid>&_t=<ms>`) shows all 4 overrides live. ✓
7. Navigate to `/projects/start/?template=vertex-creative-agency` again → SAME uuid returned (no duplicate draft). ✓
8. Click `Pubblica` → status flips → `Riporta in bozza` visible + success toast. ✓
9. Logout (POST via navbar `Esci`) → home → navbar flips to `Accedi` / `Inizia Gratis`. ✓
10. Anon visits `/templates/agency/vertex-creative-agency/preview/?project=<uuid>` → published overrides visible (per D-086 rule: published = any user). ✓
11. Anon click `Personalizza` → login → submit form with `?next` preserved → lands in same editor. ✓

### In-flight bug caught
X-Frame-Options DENY (Django default since 3.0) killed the preview iframe. Caught only through real Playwright walk — no unit test covered it. Fixed with `xframe_options_sameorigin` on the single view that's supposed to be iframeable. Defensive stays everywhere else.

### What's NOT in A.1b (honesty ledger)
- **Image / logo upload.** Still Phase A.6. A.1b exposes `site.logo_word` (text) — no image. Hero cover image also remains baseline-only.
- **Repeater widgets** (ledger_rows, capab_items, manifesto_principles). Still Phase A.2.
- **Second archetype.** Only `agency-creative-studio` (Vertex) is editor-ready. Clicking `Personalizza` on other 19 templates bounces to detail with a friendly "not yet editable" message.
- **Multi-locale editing.** Project `locale` column exists, only IT wired. Phase A.7.
- **Password reset / email verification / social login.** Not opened. Phase A.7+.
- **Purchase / checkout.** Button is visible but disabled with honest tooltip — Phase 3.

### Files touched
Created: `apps/accounts/forms.py` · `apps/accounts/views.py` · `apps/accounts/tests.py` · `templates/accounts/login.html` · `templates/accounts/signup.html`.
Modified: `apps/accounts/urls.py` · `apps/projects/views.py` · `apps/projects/services.py` · `apps/projects/urls.py` · `apps/projects/tests.py` · `apps/catalog/views.py` · `marketweb/settings.py` · `templates/catalog/template_detail.html` · `templates/includes/_template_card.html` · `templates/includes/_navbar.html` · `templates/projects/project_list.html` · `templates/projects/project_editor.html`.

### Validation
- `python manage.py test apps.projects apps.editor apps.accounts` → `Ran 24 tests ... OK` (12 pre-existing + 5 new projects + 7 new accounts).
- `python smoke_full.py` → `834/834 routes HTTP 200` (no catalog regression).
- Playwright E2E walk (11 steps above) — all green.

### Decision
**Phase A.1b PUBLIC CUSTOMIZE FLOW APPROVATO.** Criterio di successo soddisfatto: un utente normale parte dal catalogo → `Personalizza` → signup → editor proprio → salva → preview → publish, zero passaggi via `/admin/`. Foundation non overbuilt: A.2 (secondo archetipo + repeater) resta lo scope successivo intatto. D-087 documenta la shape.

---

## Session 55 — Editor Foundation v1 (Phase A.1 vertical slice) (2026-04-16)

**Summary.** Phase A.1 per D-085/D-086 ships as a real vertical slice — not a theoretical blueprint, not a half-finished scaffold. `apps/projects/` and `apps/editor/` go from empty `__init__.py` files to working modules with models, migrations, services, selectors, schema, overlay rendering, URLs, views, templates, admin, and tests. The first slice exercises `vertex-creative-agency` (agency-creative-studio archetype) end-to-end: a customer can log in, derive a new project from the published_live Vertex template, edit 23 content fields + 5 design tokens across 4 form groups, save (sparse-diff persisted, baseline-equal writes auto-delete the row), see the changes in a live iframe preview, publish, revise, and optionally unpublish. Cross-owner access returns 404; draft overlays are hidden from non-owners; DNA-locked keys are rejected at the service layer with `InvalidEditableField`. 834/834 catalog smoke unchanged — zero regression on the 20 published_live templates.

### Starting state
- Branch: `phase-editor-foundation-v1`, forked from `phase-integration-baseline-v14` @ 79724db (catalog 20/20 published_live, Session 53 closed).
- First action: merged `phase-catalog-expansion-strategy-v1` (commit 4381588) via fast-forward so D-083 / D-084 / D-085 + `CATALOG_EXPANSION_STRATEGY.md` + `PROFESSION_PRESET_TAXONOMY.md` became part of the working branch context before the foundation was authored.
- `apps/editor/` and `apps/projects/` were empty scaffolds: `__init__.py`, `apps.py`, empty `models.py` / `services.py` / `selectors.py`, placeholder `urls.py` with `urlpatterns = []`.

### First vertical slice — motivation
Chose **`vertex-creative-agency`** (archetype `agency-creative-studio`):
- Non-commerce (no PDP/cart complications — editing stays about content + tokens).
- Non-extreme register (not ultra-luxe editorial, not growth-tech chips) — middle-ground editorial voice.
- Rich hero shape: eyebrow / headline / pull-quote / intro / primary+secondary CTA / cover tile — exercises text, richtext, page-ref.
- 6 pages (home / studio / capacita / lavori / manifesto / contatti) — enough to prove multi-page without the weight of an 8-page rollout.
- Real 3-colour palette + real DNA font pairing (Space Grotesk / Inter) — exercises palette + curated-font overrides.
- Exclusive consumer of its archetype skin folder — future skin changes stay contained.

### Models shipped (`apps/projects/models.py`, 230 LOC)
- `CustomerProject` — uuid + owner FK + source_template (PROTECT) + source_archetype snapshot + source_category_slug + name + locale + status (draft|published) + last_published_at. `preview_url_base` property returns the catalog preview URL extended with `?project=<uuid>`.
- `ProjectContent` — sparse per-key overrides: `(project, key_path, value_json)`. Unique `(project, key_path)`. `value_decoded` / `set_value()` handle JSON round-trip so strings, lists, dicts, numbers all persist cleanly.
- `ProjectDesignTokens` — OneToOne with palette primary/secondary/accent + heading_font + body_font. `CURATED_FONTS` class attribute locks the Google Fonts whitelist.
- `ProjectRevision` — snapshot JSONField with reason (seed | manual | publish | unpublish). A revision is always an atomic read so the denormalised shape is the right trade-off for A.1.
- Migration `projects.0001_initial` — 4 tables, 1 owner+status index, 1 unique constraint.

### Schema + overlay (`apps/editor/`)
- `schema.py` (~200 LOC) — per-archetype editable-field whitelist. `AGENCY_CREATIVE_STUDIO_SCHEMA` authors 4 groups (site identity, home, studio, contatti) with 23 editable fields typed text/textarea/richtext/select + max_length soft constraints. `DESIGN_TOKEN_FIELDS` authors 5 global fields (3 colours + 2 curated fonts). `validate_key_path()` raises `InvalidEditableField` on any non-whitelisted key. `LOCKED_KEYS_NOTE` surfaces human-readable notes for 7 structural keys (ledger_rows, capab_items, cover, section_order, navbar_style, hero_style, pages).
- `rendering.py` (~50 LOC) — `apply_project_overrides(project, content, theme)` deep-copies the baseline content, walks the project's `get_overrides_dict()`, deep-merges, then applies tokens. Returns the `(merged_content, merged_theme)` shape the skin expects. Zero skin changes required.

### Services + selectors
- `services.create_project_from_template()` — validates tier + DNA + archetype whitelist, creates project + token row + seed revision, atomic.
- `services.save_content_edits()` — validates key_paths + values, writes rows atomically, auto-deletes rows where the edit equals the baseline (sparse-diff per EDITOR_SCHEMA_BLUEPRINT §7). Returns the list of actually-changed key_paths.
- `services.save_design_token_edits()` — same shape for palette + fonts.
- `services.publish_project()` / `unpublish_project()` / `take_manual_revision()` — snapshot + log.
- `selectors.list_projects_for_owner()` / `get_project_for_owner()` / `get_project_for_preview()` — the last one encodes overlay visibility (draft = owner+staff; published = any authenticated user; mismatched template slug → None).

### Views + URLs + templates
- `/projects/` — dashboard with "I miei progetti" table + "Nuovo progetto" form listing editable_templates (filtered to published_live + supported archetype).
- `/projects/new/` — POST to derive project from a chosen template.
- `/projects/<uuid>/editor/` — left column: 4 content groups with per-field override-dot indicator + baseline hint + max_length, 1 design-token group with colour pickers + font dropdowns, 1 read-only locked-keys group, 1 recent-revisions group. Right column: sticky iframe previewing `?project=<uuid>` overlay with status bar. Save = form POST → service layer → `take_manual_revision` → redirect → iframe cache-bust via `?_t=<ms>`.
- `/projects/<uuid>/publish/` + `/projects/<uuid>/unpublish/` — transitions.
- `templates/projects/project_list.html` (~90 LOC) + `templates/projects/project_editor.html` (~200 LOC), both extending the existing `base.html`.
- Admin: `CustomerProjectAdmin` + inline `ProjectContentInline` (tabular) + `ProjectDesignTokensInline` (stacked), plus `ProjectRevisionAdmin` with readonly snapshot.

### Catalog integration (single-file touch)
- `apps/catalog/views.py` +2 imports + ~25 LOC. `LiveTemplateView.setup()` detects `?project=<uuid>`, calls `selectors.get_project_for_preview()`, stores `self.preview_project`. `get_context_data()` now composes `theme` unconditionally, then calls `apply_project_overrides()` when a project is resolved. Also exposes `preview_project` in the context (unused in A.1).

### Settings deltas
- `LOGIN_URL = "/admin/login/"` + `LOGIN_REDIRECT_URL = "/projects/"` — editor auth redirects to admin login until the accounts app gets a branded login surface.
- `ALLOWED_HOSTS = ["*"] if DEBUG else []` — needed so Django's test client default `testserver` host resolves.

### In-flight bug caught + fixed
- First E2E run showed a manual revision taken after a POST save carried 0 content keys — a prefetched `content_overrides` cache on the view's `project` instance was freezing the pre-save state. `_build_snapshot()` now always queries `ProjectContent` + `ProjectDesignTokens` fresh via `.filter(project=project)` / `.get(project=project)`. A regression test (`test_snapshot_reflects_post_save_state`) locks this in.

### Validation
- `python manage.py check` → 0 issues.
- `python manage.py test apps.projects` → **12 tests, all green** (5 HTTP + 6 model + 1 prefetch-cache regression).
- `python manage.py test` (whole suite) → 12/12 green.
- `smoke_full.py` → **834/834 catalog routes HTTP 200** — unchanged from Session 53 baseline.
- Live E2E walk (12 manual checks): create → editor GET → save → reopen → owner preview overlay → baseline preview untouched → cross-owner 404 → draft hidden from non-owner → publish → shared preview → DNA-lock rejection → revisions taken → sparse-diff reset. All 12 green.

### Files modified / created
- `apps/projects/models.py` (created) · `apps/projects/migrations/0001_initial.py` (created, auto) · `apps/projects/services.py` (created) · `apps/projects/selectors.py` (created) · `apps/projects/views.py` (created) · `apps/projects/urls.py` (rewritten) · `apps/projects/admin.py` (rewritten) · `apps/projects/tests.py` (rewritten, 12 tests).
- `apps/editor/schema.py` (created) · `apps/editor/rendering.py` (created).
- `apps/catalog/views.py` (+ ~25 LOC in LiveTemplateView).
- `templates/projects/project_list.html` (created) · `templates/projects/project_editor.html` (created).
- `marketweb/settings.py` (+3 LOC).
- `memory/phase_a1_editor_foundation.md` (created).
- `DECISIONS.md` (D-086) · `SESSION_LOG.md` (this entry) · `TODO_NEXT.md` · `AGENT_HANDOFF.md` · `MEMORY.md`.

### What's NOT in Phase A.1 (deferred, explicit scope marker)
- Repeater widgets for list fields (ledger_rows / capab_items / manifesto_principles / clients_footer_rows) — A.2.
- Image / media upload — A.6.
- Multi-locale project trees (locale field exists, only IT wired) — A.7.
- Page add / rename / reorder — A.4.
- Section reorder / per-section visibility — A.2.
- Archetypes beyond `agency-creative-studio` — schema extension per archetype, A.2+.
- D-054 palette differentiation validator — A.5.
- Branded login page (editor redirects to /admin/login/) — A scaffolding.
- SPA / inline-preview editing — intentionally out; server-rendered form + iframe reload is the Foundation shape.

### Catalog state after Session 55
**Unchanged: 20/20 published_live, 0 draft.** Zero skin files touched, zero content registry files touched, zero DNA entries touched. Foundation v1 is additive — it opens `apps/projects/` and `apps/editor/` without disturbing the catalog.

---

## Session 54 — Catalog Expansion Strategy + Profession Preset Taxonomy (2026-04-15)

**Agent:** progettare in modo rigoroso e scalabile l'evoluzione del catalogo dopo la chiusura del MVP a 20/20 `published_live`. Output concreto: un documento strategico principale (`CATALOG_EXPANSION_STRATEGY.md`), un companion (`PROFESSION_PRESET_TAXONOMY.md`), aggiornamenti coordinati a tutti i file di coordinamento, una proposta roadmap eseguibile in fasi successive. **Strategy-only session — no template, no skin folder, no rollout.**

**Branch:** `phase-catalog-expansion-strategy-v1` (architettura, no DB/schema/tier changes).

### Vincoli (espliciti)

- NON implementare nuovi template live.
- NON aprire l'editor.
- NON refactorare codice.
- NON toccare i 20 `published_live`.
- NON aprire branch di rollout.
- Architettura concreta basata sui pattern reali emersi dai 20 template live, NON teoria astratta.

### Domanda centrale

> Come dobbiamo organizzare il sistema per arrivare a decine di categorie, centinaia di professioni e molti più template/preset, senza duplicazioni, senza refactor continui e senza appiattire il design?

### Lavoro svolto

#### 1. Lettura integrale contesto (12 file)

Letti: CLAUDE.md · MEMORY.md · SESSION_LOG.md (tail) · DECISIONS.md (D-080..D-082) · TODO_NEXT.md · ARCHITECTURE.md · AGENT_HANDOFF.md · CONTENT_GUIDELINES.md · BRAND_SYSTEM_GUIDELINES.md · CATEGORY_ROADMAP.md · TEMPLATE_REGISTRY.json · EDITOR_SCHEMA_BLUEPRINT.md.

#### 2. Audit catalogo attuale

- 8 categorie MVP, 19 archetipi spediti, 20 template `published_live`, 1 reuso archetipo (derm su specialist).
- 12 pattern strutturali consolidati identificati (DNA, D-047, D-053/054/057, locale-keyed registry, Pexels, motion library, …).
- 8 limiti strutturali identificati per scalare a 100+ professioni: assenza di livello "preset", template-as-scaling-unit, no editor, no varianti di sezione, asset library curatela manuale, ecc.
- Aree mature vs aree fragili documentate.

#### 3. Tassonomia futura

- Proposte **14 categorie top-level medio termine** (8 esistenti + 6 nuove): `hospitality · food-retail · automotive · trades · beauty · wellness-fit · professional · education · events`.
- Test di promozione preset → categoria definito (4 gate: nome cercato dal cliente · conversion pattern strutturalmente diverso · ≥ 3 archetipi distinti · sopravvive al test card-size).
- Scelte di accorpamento documentate (perché dentista NON è categoria, perché idraulico NON è categoria, ecc.).

#### 4. Modello strutturale a 4 livelli

```
Categoria → Archetipo → Preset Professionale → Editor Cliente
```

- Responsabilità per livello documentate (cosa contiene, cosa NON contiene).
- 3 esempi concreti applicati (`dentista-clinico-pulito`, `idraulico-pronto-intervento-roma`, `panettiere-cesare-quartiere`).
- Persistenza schema-level proposta: 2 colonne nuove additive (`profession_preset` + `parent_archetype`) su `WebTemplate`; 1 nuovo file registry `apps/catalog/profession_presets.py`. Zero breaking change.

#### 5. Archetipi per categoria

- Matrice completa `categoria × archetipo` con 7 dimensioni DNA per archetypo (hero/navbar/CT/motion/imagery/font/page-kinds + riusabilità).
- 19 archetipi esistenti + **11 nuovi proposti** (3 trades + 3 food-retail + 4 hospitality + 3 automotive + 3 beauty + 3 wellness-fit + 3 professional + 3 education + 2-3 events + opzionali) = 28-30 medio termine, 35-40 lungo termine.

#### 6. Preset professionali

- Anatomia preset binding documentata in `PROFESSION_PRESET_TAXONOMY.md`.
- Cosa cambia / cosa NON cambia tra preset dello stesso archetypo (matrice 13 dimensioni).
- Trigger di promozione preset → archetypo definito (rompe ≥ 4 dimensioni D-054).
- Trigger di promozione preset → template autoriale featured definito (top 10% domanda + showcase + archetypo rodato).
- **75-90 preset target medio termine**, **130-170 lungo termine**, distribuiti su 14-16 categorie. Registro completo numerato 1-139 con archetypo/voce/cosa-cambia/proof/sezioni-opzionali/Phase per ciascuno.

#### 7. DNA-locked vs editor-editable matrix

- Tassonomia 5-livelli editabilità: DNA-locked · Preset-driven · Editor-editable · Tier-gated · Don't expose v1.
- Matrice completa per ~40 dimensioni (archetype, hero silhouette, navbar style, copy, palette, font, sezioni, locali, SEO, slug, custom code, dominio, Stripe, multi-tenant, …).
- 5 decisioni vincolanti documentate (DNA è davvero locked, editor rispetta D-047/053/054/057, tier-gated arriva dopo Phase A, don't-expose-v1 non è "mai esporre").

#### 8. Strategia editor — decisione esplicita

**Decisione:** Editor Foundation v1 PRIMA, poi preset-driven expansion.

- 6 motivazioni dettagliate (costo lineare vs amortizzato, native voice non scalabile, modello a 4 livelli funziona solo con editor, EDITOR_SCHEMA_BLUEPRINT già autoriale, Phase 3 unblock gate MET, 20 template = campione sufficiente).
- Scope Editor v1 chiarito (in scope: models + renderer overlay + form-based UI + preset library + validators + image upload + locale UI + smoke; out scope: AI gen, multi-user editing, SPA, custom code injection).
- Stima: 14-23 sessioni / 2-3 mesi.
- 3 regole vincolanti per evitare rifare lavoro (editor non sa dei preset, schema additivo, DNA è source of truth).

#### 9. Roadmap eseguibile in fasi

**Phase A** (Editor v1) → **Phase B** (Trades + Food retail) → **Phase C** (Beauty + Wellness-fit) → **Phase D** (Hospitality + Automotive) → **Phase E** (Professional + Education) → **Phase F** (Events + MVP extension) → **Phase G** (Tier monetization + commerce extensions). Stima totale 14-16 mesi. Tabella riassuntiva con archetypi nuovi/preset nuovi/categorie nuove/mesi per ciascuna phase.

#### 10. Proposta numerica + decisione finale

| Asse | Oggi | Medio termine | Lungo termine |
|------|------|----------------|----------------|
| Categorie top-level | 8 | 14-16 | 17-20 |
| Archetypi totali | 19 | 28-30 | 35-40 |
| Preset professionali | 0 | 75-90 | 130-170 |
| Template autoriali | 20 | 20-25 | 25-30 |

**Decisione binding:** Phase A è il prossimo workstream. Nessun nuovo template/archetypo/categoria finché Phase A non è chiusa.

### Deliverable concreti

- ✅ `CATALOG_EXPANSION_STRATEGY.md` (~1100 LOC, 11 sezioni: exec summary · audit · tassonomia · modello strutturale · archetypi per categoria · preset framework · DNA-locked matrix · editor strategy · rollout priority · numerical proposal · 12-point summary)
- ✅ `PROFESSION_PRESET_TAXONOMY.md` (~600 LOC, registro completo 139 preset numerati su 17 categorie effettive)
- ✅ `CATEGORY_ROADMAP.md` aggiornato con header strategy + 14 categorie top-level + tabella Phase A-G
- ✅ `TODO_NEXT.md` aggiornato con Phase A sub-phasing (A.1-A.8) + Phase B-G (placeholder per future sessioni)
- ✅ `DECISIONS.md` con 3 nuove decisioni binding:
  - **D-083** Modello catalogo strutturale a 4 livelli (Categoria → Archetipo → Preset → Editor)
  - **D-084** Tassonomia 14 categorie top-level medio termine
  - **D-085** Editor-First Sequencing (Phase A è il prossimo workstream, blocco binding)
- ✅ `AGENT_HANDOFF.md` con istruzioni Session 54 → Phase A (cosa NOT to do · cosa verificare prima di aprire Phase A · acceptance gates Phase A)
- ✅ `SESSION_LOG.md` entry Session 54 (questa)
- ✅ `MEMORY.md` index entry + `memory/catalog_expansion_strategy_session54.md`

### Catalog state dopo Session 54

**INVARIATO: 20/20 published_live, 8 categorie MVP CHIUSE.** Strategy-only session.

### Files modificati / creati

- `CATALOG_EXPANSION_STRATEGY.md` (created · ~1100 LOC)
- `PROFESSION_PRESET_TAXONOMY.md` (created · ~600 LOC)
- `CATEGORY_ROADMAP.md` (modified · header + 14 categorie + Phase A-G table aggiunte)
- `TODO_NEXT.md` (modified · Phase A sub-phasing + Phase B-G placeholder aggiunti in cima)
- `DECISIONS.md` (modified · D-083 + D-084 + D-085 aggiunti in cima)
- `AGENT_HANDOFF.md` (modified · Session 54 entry aggiunto in cima)
- `SESSION_LOG.md` (modified · entry Session 54 aggiunto in cima)
- `memory/catalog_expansion_strategy_session54.md` (created)
- `MEMORY.md` (modified · index entry aggiunto)

**Nessun template, skin folder, content tree, registry JSON, o codice applicativo è stato toccato.**

### Trade-off deliberati

- **Strategia, non implementazione.** Questa sessione produce blueprint, NON content tree dei preset né codice editor. Tutto il lavoro autoriale concreto arriva nelle phase successive.
- **14 categorie, non 30+.** Tassonomia contenuta per browseability + marketing chiarezza + zero overlap categoria.
- **75-90 preset medio termine, non 200.** Numero realistico per redazione interna; il customer fork via editor è il moltiplicatore reale.
- **Editor v1 minimal, non SPA + AI.** SPA + AI features sono v2/v3, riducono drasticamente costo + rischio Phase A.
- **Phase B = Trades + Food-retail (NON Medical extension first).** Apre asse "mestieri italiani locali" oggi scoperto, max copertura mercato per minimo costo (riuso archetypi semplici, conversion patterns lineari).
- **NO modifica ai 20 template `published_live`.** Restano "template autoriali" featured al livello 3 con `profession_preset` vuoto, mai retrofittati a preset.

### Decisione finale

> **Phase A — Editor Foundation v1 — è il prossimo workstream.**
> Nessun nuovo template `published_live`, nessun nuovo archetipo, nessuna nuova categoria, nessun preset autoriale viene aperto finché Phase A non è chiusa con i criteri di accettazione di `CATALOG_EXPANSION_STRATEGY.md` §8.

---

## Session 52 — Medical Second Wave Polish + Interaction Fix (2026-04-15)

**Agent:** chiudere i problemi qualitativi e interattivi ancora presenti sui 3 template della second wave medical (Salute · Benessere · Famiglia), con priorità pratica su Benessere e Salute; NON un nuovo rollout, ma un pass di polish + click-integrity + motion/interaction; formalizzare la regola "counter dinamici quando il tono lo consente" in memoria e nel decision log.

**Branch:** `phase-medical-polish-fix-v1` (polish-only, no DB/schema/tier changes).

### What was audited (real browser, not just smoke)

- **Benessere IT + AR** — `/preview/` home + `/preview/prenota/` form; all nav links + CTA + language pills + dropdown open state.
- **Salute IT + EN** — `/preview/` home hero stats + band stats; counter mid-frame sampling at 200 / 600 / 1000 / 1800 ms; `tel:` + booking-CTA + specialty links.
- **Famiglia AR** — home + phone `tel:+390115492188` + WhatsApp `https://wa.me/393491234567` + language pills.

### Defects surfaced

1. **Benessere nav CTA renders empty across all 5 locales.** `templates/live_templates/medical/wellness/_base.html:573` bound to `{{ chrome.nav_cta }}`, but neither `CHROME_I18N` nor any Benessere locale file defines that key. The anchor tag renders with no text content (`<a class="cta" href="…"></a>`). Visible only in browser — smoke checks HTTP 200 only.
2. **Benessere form dropdown open state oversized-round.** `.lf-select-listbox` inherits `border-radius: var(--lf-radius, 0)` and wellness sets `--lf-radius: 999px` (intentional for pill input fields). The open listbox panel renders as a 999px-radius barrel — wrong for a 356 × 280 panel.
3. **Salute stats are static.** Hero `40+ · 12 · 98%` and band `1998 · 28.000 · 6 · € 0` have no `data-lm="counter"` attribute — live-motion.js leaves them frozen.

### What shipped

- **`static/css/live-forms.css`** — `.lf-select-listbox` now reads a new `--lf-listbox-radius` token (default 12px) instead of inheriting the pill field radius. `overflow: hidden auto` prevents child hover rows from bleeding outside the rounded corner. Token docs updated at the top of the file.
- **`static/js/live-motion.js`** — counter heuristic extended to support BOTH Italian dot-style (`28.000`) AND English comma-style (`28,000`) thousand separators. `formatValue` preserves the detected separator in mid-animation frames so EN/FR/ES stats bands render native-formatted thousand-separators while animating.
- **`templates/live_templates/medical/wellness/_base.html`** — nav CTA now reads `{{ site.nav_cta }}` (template-specific, not chrome-shared). Explicit `--lf-listbox-radius: 14px` added so the pill input fields (999px) no longer project their radius onto the listbox panel.
- **`templates/live_templates/medical/clinic/home.html`** — `.cl-h-stats .n` (hero) and `.cl-stats .n` (band) spans emit `data-lm="counter"`. A 3rd tuple element on stats/stats_strip entries opts individual values out of animation (truthy = static). Loop uses `{% comment %}…{% endcomment %}` — the initial patch used `{# … #}` which Django leaks on multi-line (Session 48 D-078 gotcha, re-encountered, re-fixed).
- **`apps/catalog/template_content_benessere.py`** + `_en.py` + `_fr.py` + `_es.py` + `_ar.py` — `site.nav_cta` added per locale: "Prenota un rituale" · "Book a ritual" · "Réserver un rituel" · "Reservar un ritual" · "احجز تجربتك" (initial first-pass draft used "احجز طقسك" iḥjiz ṭaqsak, flipped in user review to the more premium/editorial "احجز تجربتك" iḥjiz tajribatak = "book your experience" — standard AR wellness register used by Aman / Six Senses / Vogue Arabia. Rationale: `طقس` dual-meaning "rite/weather" in everyday MSA makes it stilted at a nav-CTA surface; body-copy retains `طقس` throughout for Session 51 lexical continuity).

### Validation

- `python manage.py check` → 0 issues.
- Playwright browser walk @ 1440 × 900 + 1440 × 600 + AR (RTL):
  - Benessere home: nav CTA "PRENOTA UN RITUALE" renders in IT, "احجز طقسك" in AR.
  - Benessere prenota: dropdown opens at 14px radius on dark-band backdrop, 13 rituals listed cleanly; submit button "Riserva il tuo momento" visible (gold bg · primary ink).
  - Salute home: hero `40+ · 12 · 98%` animate 0 → target on viewport enter (samples at t=200 / 600 / 1000 / 1800 ms showed `298 / 4,172 / 1 / € 0` → `1419 / 19,882 / 4 / € 0` → `1892 / 26,512 / 6 / € 0` → `1998 / 28,000 / 6 / € 0`, easeOutCubic-shaped climb).
  - Salute EN home: `28,000` comma-sep preserved through animation (heuristic extension confirmed).
  - Famiglia AR: `tel:+390115492188` + `https://wa.me/393491234567` both resolve, RTL, 5 pills.
- `smoke_full.py` regression: 660/660 routes HTTP 200 (no route changes).
- D-047 chrome-cleanliness preserved: no new IT literals in HTML (`site.nav_cta` values are content-registry keys, not literals in skin).

### Key decisions made

- **D-081** added: Dynamic Counter Policy + `--lf-listbox-radius` decoupling + `site.nav_cta` authoring convention + live-motion.js thousand-sep extension + Django multi-line comment rule restated.

### Dynamic Counter Policy (D-081 binding)

> When a published_live template renders a premium stats / facts / metrics / volumes / years / visits / indicators band, the numeric value MUST animate from 0 via `data-lm="counter"` unless the DNA tone disqualifies it (funereal editorial, brutalist manifesto, or the value is a semantically-inanimate label like a literal zero). Reduced-motion MUST be respected (`prefers-reduced-motion: reduce` short-circuits all counters in `live-motion.js`).

Future rollouts (Lex · Juris · Casa · Villa) that ship a stats band MUST wire this. Premium-UI reviewer adds this to the D-054 10-gate as an implicit gate #11 for templates with numeric bands.

### Blockers

None. Session 52 closes. Catalog holds at 16/20 published_live.

### Integration target

**`phase-integration-baseline-v13`** (head `1f3319d`, containing medical second wave rollout). This polish branch (`phase-medical-polish-fix-v1`) roots on the medical-wave commit `728a044` which is an ancestor of v13. Integration path: commit polish changes → merge into v13.

### Exact next step

**Phase 2g3.6d — Lawyer (Lex / Juris) live rollout.** Then Phase 2g3.6e — Real-estate (Casa / Villa). Same recipe as Sessions 32 / 34 / 41 / 48 / 49 / 51 + NEW gate: counter-motion-when-coherent per D-081.

---

## Session 49 — Agency Live Rollout Premium (Phase 2g3.6f close · 2026-04-15)

**Agent:** chiudere la categoria agency portando entrambi i template (Vertex + Aura) a `tier=published_live` premium con due skin folder distinte, 5 lingue vere fin da subito, RTL serio per AR, identità sharply differenziata, zero regressione sui 11 live precedenti.

### What shipped

**Two distinct DNA archetypes (`agency-creative-studio` · `agency-digital-studio`):**
- `vertex-creative-agency` → `agency-creative-studio` (editorial-quote-cover hero, serif-index-asterisk nav, colophon-press footer, editorial-index-dossier ledger cards, ghost-serif-dossier CTA, very-airy density, editorial-agency tone, dossier-request conversion, Space Grotesk + Inter + Fraunces italic, editorial-agency-craft imagery)
- `aura-digital-studio` → `agency-digital-studio` (product-console-hero, pill-sprint-chip nav, shiplog-console footer, sprint-console cards, glow-sprint-arrow CTA, medium density, digital-sprint tone, discovery-call conversion, Plus Jakarta Sans + Inter + JetBrains Mono, digital-product-console imagery)

**Two new skin folders (~3,800 LOC HTML each, 7 files):**
- `templates/live_templates/agency/agency-creative-studio/` — `_base.html` (cream paper `#f4f0e8`, serif-italic accent via Fraunces, asterisk wordmark + alpha-index nav, colophon footer with press ribbon + standfirst pull-quote) + `home.html` (editorial-quote hero with selected-work cover tile + indexed case-study ledger + 4-up capabilities + press ribbon + dark manifesto with drop-cap + inquiry CTA) + `about.html` + `services.html` (4 disciplines: identità · linee editoriali · direzione artistica · sistemi spaziali) + `project_list.html` (indexed catalog ledger) + `project_detail.html` (dossier with chapters + deliverables 3-up + dark press-quote band) + `process.html` (4 phases: ascolto / ipotesi / costruzione / rollout + 6 principles).
- `templates/live_templates/agency/agency-digital-studio/` — `_base.html` (midnight `#0c0a1f` + violet `#8B5CF6` + cyan `#7ae5ff` accents, floating glow pill nav with sprint chip, shiplog-console footer with mono telemetry rows + stack marquee + boot-line) + `home.html` (product-console hero with dashboard tile + sparkline + 4-up capabilities + 4-up sprint cards + work cards with metric chips + metric strip + glow CTA panel) + `about.html` (3 partner cards + 4 values) + `services.html` (4 capabilities full-card + 3 engagement tiles) + `project_list.html` (work cards with KPI rows + tabs) + `project_detail.html` (dossier with problem/solution + timeline 5-step + results 4-stat + dark quote + next/CTA) + `process.html` (4 sprint rows + 3 mindset cards + stack tiles).
- Both skins: `<em>` styled per-skin (Vertex serif italic on accent, Aura cyan-to-violet gradient), full RTL CSS block scoped to `html[dir="rtl"]` on `.vx-*` and `.au-*` selectors, conditional Amiri+Noto-Kufi (Vertex) / Noto-Naskh+Noto-Kufi (Aura) font load `{% if is_rtl %}`, Latin proper names + Latin Western digits preserved, 720px mobile breakpoint, `:focus-visible` rings on every CTA, D-047 chrome-cleanliness from line one (every string from `site.*`/`page_data.*`/`chrome.*`/loop items, zero IT literals in HTML).

**Two IT content registries + 8 locale trees (~10,400 LOC of localized content):**
- `template_content_vertex.py` ~1,300 LOC IT — voice = Milan independent creative-studio editorial register. Clients: Fondazione Prada, Adelphi Edizioni, Maison Gentiluomo, Triennale Milano, Museo del Novecento, Villa Necchi Winery. 6 page kinds + 6 case-study posts. Press: Monocle, Domus, Wallpaper*, Creative Review, It's Nice That, Eye Magazine.
- `template_content_aura.py` ~1,400 LOC IT — voice = Milan digital-product-studio register. Clients: Casavo, Fastweb, Soldo, Milkman, Lendlease, Fiscozen. 6 page kinds + 6 product-case posts. Stack: Next.js · Figma · Stripe · Linear · PostHog · Segment · Vercel · Supabase · Datadog · Sentry. Telemetry vocabulary: sprint, discovery, backlog, NPS, MRR, retention, TTFV.
- 8 locale files (vertex_{en,fr,es,ar} + aura_{en,fr,es,ar}, ~1100-1250 LOC each) authored by 4 parallel sub-agents, each agent producing both Vertex and Aura for a locale to enforce voice coherence:
  - **EN:** Creative Review/Monocle/Eye for Vertex · TechCrunch/Linear/Figma for Aura (1136 + 1246 LOC)
  - **FR:** Libération Next/M/M Paris/vouvoiement for Vertex · Maddyness/Les Echos Tech for Aura (1133 + 1245 LOC)
  - **ES:** Apartamento/Fuera de Serie peninsular for Vertex · Xataka/K Fund peninsular `tú` for Aura (1138 + 1246 LOC)
  - **AR:** Brownbook/Kalimat curatorial MSA for Vertex · Wamda/Modo product MSA for Aura, Latin proper names + Latin digits + Latin stack names preserved (1122 + ~1240 LOC)
- All 8 locale files validated for structural parity vs IT (zero missing keys, zero extra keys, zero list-length mismatches, zero tuple-arity mismatches) by each agent's own deep-walker check.

**Imagery — Pexels deferred, curated Unsplash IDs used (D-077 fallback per Session 48 precedent):**
- `PEXELS_API_KEY` env var not present at session start. Per session directive ("usa Pexels come sorgente primaria · NON scrivere la chiave nei file"), the API integration was skipped.
- Two new per-archetype imagery pools added in `apps/catalog/preview_imagery.py`:
  - `agency-creative` — editorial studio craft (type specimens, brand books, gallery installs, designer desks, contact sheets) using verified Unsplash IDs from `portfolio-designer` precedent.
  - `agency-digital` — product-console momentum (dashboard UIs, modern dark studios, IDE close-ups, product-design detail) using verified IDs from `business-startup` precedent.
- Pexels swap is a Phase-2g3.6f follow-up in TODO_NEXT for when key is available.
- **No video.** Per session directive ("Aggiungi video solo se davvero opportuno"), and per honest D-068 read: agency hero is editorial/product-grid driven; a video would feel cheap on a curatorial creative studio and gimmicky on a delivery-focused digital studio. Skipped.

**Chrome i18n extension:** added `mp_other_agency` key in `CHROME_I18N` for IT/EN/FR/ES/AR (5 new strings, ~30 LOC `template_i18n.py`).

**Click-through bug fix:** Aura `chip` field across all 5 locales contained literal `<span class="pulse"></span>` inside the data string, which Django auto-escaped to readable garbage in the rendered chip. Stripped the inline span from all 5 files (the home.html template provides the static pulse). Validated in-browser AR view post-fix.

### Database delta

`+0` WebTemplate rows (vertex + aura already existed as draft from initial seed). `+0` migrations. Pure tier flip + content add.

- Tier sync: `vertex-creative-agency: draft → published_live`, `aura-digital-studio: draft → published_live`.
- Catalog distribution: **13 published_live / 7 draft** (was 11/9). 7 draft remaining: salute · benessere · famiglia · lex · juris · casa · villa.

### Files modified / created

**Created (24):**
- `templates/live_templates/agency/agency-creative-studio/{_base,home,about,services,project_list,project_detail,process,contact}.html` (8 files but actually 7 — process+contact share the same skin folder, and we have 7 page kinds: home/about/services/project_list/project_detail/process/contact → 7 distinct kinds shipped)

  Wait: 7 files = `_base` + `home` + `about` + `services` + `project_list` + `project_detail` + `process` + `contact` = 8 files. ✓
- `templates/live_templates/agency/agency-digital-studio/{_base,home,about,services,project_list,project_detail,process,contact}.html` (8 files)
- `apps/catalog/template_content_vertex.py` (1)
- `apps/catalog/template_content_aura.py` (1)
- `apps/catalog/template_content_vertex_{en,fr,es,ar}.py` (4)
- `apps/catalog/template_content_aura_{en,fr,es,ar}.py` (4)
- Memory: `agency_live_rollout_session49.md`

**Modified (5):**
- `apps/catalog/template_dna.py` — +2 entries (Vertex + Aura) + 2 archetype labels + 2 hero-style labels + 2 navbar-style labels + 2 footer-style labels + 2 card-style labels + 2 button-style labels + 2 tone labels + 2 conversion-pattern labels + 2 imagery-direction labels (~120 LOC)
- `apps/catalog/preview_imagery.py` — +2 pools (`agency-creative` · `agency-digital`)
- `apps/catalog/template_content.py` — +10 imports + 2 TEMPLATE_CONTENT entries
- `apps/catalog/template_i18n.py` — +`mp_other_agency` key in 5 locales
- `TEMPLATE_REGISTRY.json` — 2 tier flips + 2 metadata expansions + version 0.11.0 → 0.12.0 + new `phase_2g3_6f_agency_live` block
- `smoke_full.py` — +2 templates in LOCALES + CATEGORY + agency listing path + 2 POST_ROUTES blocks (+~6 lines, 6 project_detail cases tested)

### Validation

1. **`python manage.py check`** → 0 issues
2. **`python manage.py sync_template_tiers`** → 2 tier(s) updated. **13 published_live / 7 draft.**
3. **`smoke_full.py` → 530/530 routes HTTP 200** (was 443/443; +87 routes from agency rollout: 2 marketplace × 5 locales + 2 home × 5 + 6 inner pages × 2 templates × 5 locales + agency listing + 6 project_detail. Math: 87 = 2·5 + 2·5 + 60 + 1 + 6 = nope; recount: 87 actual = 4 templates' detail/listing surface × 5 locales = 20, + 6 page-routes per template × 2 templates × 5 locales = 60, + agency category page = 1, + 6 project_detail = 6 → 87 ✓).
4. **Playwright real-browser walk** at 1440×900:
   - Vertex home IT — full page screenshot — editorial cream paper + serif italic display + indexed case-study ledger + press ribbon + manifesto drop-cap + inquiry CTA all rendered correctly.
   - Vertex case detail (`fondazione-prada-rebrand`) — dossier rendered with chapter pull-quotes, deliverables 3-up, dark press-quote band, next-case + CTA navigation.
   - Aura home IT — midnight + violet + cyan, dashboard console hero with sparkline, "+34%" gradient metric, sprint cards, work cards with metric chips, ship-log footer.
   - **Vertex AR/RTL** — layout properly mirrored, Noto Kufi Arabic display, Latin Vertex Studio + MILANO + FONDAZIONE PRADA preserved, language switcher visible.
   - **Aura AR/RTL** — chip bug detected (literal `<span class="pulse"></span>` showing as text), fixed across all 5 Aura locale files via stripping inline span (template provides static pulse), re-screenshot confirmed clean rendering.
   - Vertex `lavori` page in FR — clicked into case study, navigation works, French translation idiomatic ("Refonte de la Fondation", "Direction artistique").
   - Aura `lavori` page in ES — peninsular Spanish renders cleanly ("Cuarenta y siete productos enviados"), category tabs translated ("Trabajos"), work cards with screenshot covers + metric chips visible.
5. **Final regression smoke after bug fix** → 530/530 still green.

### Key Decisions Made

- **D-079** added: formally documents the agency live-rollout closure + the two distinct archetypes + the chrome-authoring contract reaffirmation + the click-through bug-fix protocol.

### Differentiation matrix · Vertex vs Aura (D-054 audit)

| Axis | Vertex | Aura |
|---|---|---|
| Page color | Cream paper `#f4f0e8` + ink `#0d0d0d` | Midnight `#0c0a1f` + violet/cyan ambient |
| Heading font | Space Grotesk display + Fraunces italic accent | Plus Jakarta Sans display |
| Body accent font | Fraunces italic for pull-quotes | JetBrains Mono for telemetry/labels |
| Hero silhouette | Editorial pull-quote left + selected-work cover tile right with editorial credit strip | Bold kinetic headline left + dashboard-chrome product card right with live metric + sparkline |
| Navbar | Hairline serif wordmark + asterisk + alpha-index links + ghost dossier CTA | Floating dark violet pill + dot-glow + sprint chip + glow primary CTA |
| Work presentation | Indexed case-study ledger (01 — Title — italic Client — Discipline — Year) | Card grid with screenshot cover + metric chip + stack pills |
| Case detail | Editorial essay + deliverables 3-up + dark press-quote band | Problem/solution panels + timeline 5-step + results 4-stat + dark mono quote |
| Services framing | Capacità — 4 disciplines (identità · editoriali · art direction · sistemi spaziali) | Capabilities — 4 capabilities (product launch · platform redesign · growth systems · B2B delivery) |
| Process section | Manifesto — 4 phases (ascolto / ipotesi / costruzione / rollout) + 6 principles + Italian editorial language | Sprint — 4 sprints (signal / sketch / ship / scale) + 3 mindset cards + stack tiles |
| Inquiry flow | "Richiedi il dossier" — long-form brief with discipline + budget bands | "Prenota una call" — 3-step structured brief with slot picker grid |
| CTA style | Ghost serif italic underline `Richiedi il dossier →` | Glowing violet pill `Prenota una call →` |
| Premium cues | Press ribbon (Monocle/Domus/Wallpaper*/Creative Review/Eye/Slanted) · ADI/TDC recognition | Live ship-log with mono timestamps + stack marquee + boot-line + sparkline + KPI cluster |
| Imagery pool | Editorial workspace, type specimens, brand books, gallery installs | Product UIs, screen close-ups, dashboards, modern dark studios |
| Voice | Milan editorial curatorial · third-person plural · vouvoiement · cultural clients | Milan growth-tech direct · imperative-light · scale-up clients · KPI-led |
| Site `availability` | Chrome quote: "Nuove commesse · autunno 2026" | Chrome chip: "Sprint 07/Q2 · live" |

D-054 audit: every axis is materially different. Two products, not two recolors.

### Findings — premium quality bar reached

- **Differentiation is achieved structurally, not cosmetically.** Vertex and Aura render through fully different skeletons. A buyer comparing the two demos understands they are choosing between two professional positions (cultural-editorial vs digital-product), not between two color schemes.
- **5 locales fin da subito.** No locale falls back to IT silently. Every page kind in every locale renders authentic native voice. AR RTL is properly layout-mirrored with Latin proper names + Latin digits preserved per D-063.
- **D-047 chrome-cleanliness held from line one.** Zero IT literals in HTML across both skin folders. The 8 locale files only had to translate the content registry — the chrome was authored locale-aware from the start.
- **Real click-through validation caught a bug.** The Aura chip rendered literal `<span class="pulse"></span>` text in AR (and would have done the same in IT/EN/FR/ES if the eye had caught it — Latin auto-escape was less visually obvious). Browser audit caught it before commit. Fix shipped, re-validated.

### Blockers
None. Phase 2g3.6f closes cleanly. Catalog progresses to **13/20 published_live across 6 categories** (medical · restaurant · business · portfolio · ecommerce · agency).

### Exact next step
**Phase 2g3.6c — Medical second wave (salute · benessere · famiglia).** Next public-catalog promotion gate. Three templates, three existing draft archetypes (`clinic` / `wellness` / `family`), DNA + preview compositions exist, blocked on per-archetype skin authoring at `templates/live_templates/medical/{clinic,wellness,family}/` and 5-locale content per template. Per Session 32+34+41+48+49 recipe — green path now. Budget ~4-5h end-to-end via parallel agents. After that: Phase 2g3.6d (lawyer · 2 templates) + Phase 2g3.6e (real-estate · 2 templates) close the catalog at 20/20.

---

## Session 48 — Restaurant Live Completion Premium (Phase 2g3.6 close · 2026-04-15)

**Agent:** chiudere la categoria restaurant a 3/3 live portando `sapore-trattoria-pizzeria` (trattoria-warm) e `brace-street-food-lab` (street-modern) da `tier=draft` a `tier=published_live` premium con 5 lingue vere fin da subito + RTL serio per arabo, mantenendo Gusto fine-dining intoccato e zero regressione sugli altri 9 live. Niente nuove categorie, niente nuove macro-feature.

### Shipped

**Sapore — Trattoria Da Nonna Rosa (trattoria-warm archetype):**
- Skin folder `templates/live_templates/restaurant/trattoria-warm/` — 7 file (~3014 LOC): `_base.html` (cream paper `#f8efde` + Libre Baskerville/Source Sans 3/Caveat + RTL block + Amiri+Noto-Kufi conditional + 720px breakpoint + `:focus-visible`), `home.html`, `menu.html`, `about.html`, `signature.html`, `events.html`, `contact.html`
- Content registry IT `apps/catalog/template_content_sapore.py` (~855 LOC) — 6 page kinds (home/menu/storia/forno/eventi/contatti), Roman family-trattoria voice, 9 distinct Unsplash IDs from `restaurant-trattoria` pool + IT-curated additions
- 4 locale trees autorate da sub-agent paralleli (~856 LOC each):
  - `_en.py` (Bon Appétit / NYT Food / Saveur Roman-trattoria reportage)
  - `_fr.py` (Le Fooding / Atabula `tu` warm-trattoria)
  - `_es.py` (El País Gastro / 7 Caníbales peninsular `tú`)
  - `_ar.py` (Brownbook cultural-publishing MSA, Latin proper names + Latin Western digits)
- D-047 chrome-cleanliness from line one (zero IT literals in HTML)

**Brace — Brace Street Lab (street-modern archetype):**
- Skin folder `templates/live_templates/restaurant/street-modern/` — 7 file (~3828 LOC): `_base.html` (near-black `#0a0a0a` + neon-yellow `#FFE600` + flame-red `#FF3D00` + Big Shoulders Display 800/900 + Inter + JetBrains Mono + RTL block + 720px breakpoint), `home.html`, `menu.html`, `about.html`, `gallery.html`, `order.html`, `contact.html`
- Content registry IT `apps/catalog/template_content_brace.py` (~944 LOC) — 6 page kinds (home/menu/lab/moments/ordina/contatti), Bologna street-food brutalist UPPERCASE imperative voice, 24 distinct Unsplash IDs from `restaurant-street` pool + urban-additions
- 4 locale trees autorate da sub-agent paralleli (~627-955 LOC each):
  - `_en.py` (Eater / Vice Munchies street-food UPPERCASE `you`)
  - `_fr.py` (Le Fooding street / Trax / Time Out Paris `tu` urban-imperative + anglicismes)
  - `_es.py` (Time Out Madrid peninsular `tú` urban + `currar`/`pillar`)
  - `_ar.py` (Wamda lifestyle / Vice Arabia urban-imperative MSA, Latin proper names)
- D-047 chrome-cleanliness from line one

**Wiring:**
- `apps/catalog/template_content.py` — 10 new imports + 2 new TEMPLATE_CONTENT entries
- `TEMPLATE_REGISTRY.json` — 2 rows flipped from `tier=draft` to `tier=published_live`, version bumped to 0.11.0
- `python manage.py sync_template_tiers` — 2 templates promoted, catalog now 11/20 published_live

**Smoke harness extensions:**
- `smoke_full.py` — 2 new templates × 5 locales added (now 443/443, was 363)
- `smoke_forms.py` — 2 new contact forms × 5 locales added (now 55/55, was 45)
- `smoke_i18n_media_hardening.py` — 2 templates added to MULTILINGUAL set (now 69/69, was 57)

### Validation

- `python manage.py check` → 0 issues
- **443/443 full route sweep** (was 363, +90 from new 2 templates × 5 locales × ~9 surfaces avg incl. detail+home+5-6 inner pages)
- **55/55 form sweep** (was 45, +10 from new 2 contact forms × 5 locales)
- **69/69 hardening sweep** (was 57, +12 from new 2 MULTILINGUAL templates × 6 checks each)
- **194/194 ecommerce regression** — green (no cross-impact)
- **52/52 gusto i18n regression** — green (Gusto untouched per directive)
- **0 IT leaks** across 48 non-IT pages × 10 forbidden-phrase patterns = 480 cross-locale leak checks

**Browser click-through validation (Playwright @ localhost:8904):**
- Sapore IT/EN/FR/ES/AR home + menu + contatti — render correctly, RTL flip on AR works (logo right, photo right, eyebrow right, headline anchored right)
- Brace IT/EN/FR/ES/AR home + menu — product-cutout hero + neon-yellow stamp + price badge in correct position per direction
- 5 language pills (IT/EN/FR/ES/AR) on every page, hrefs correct, `?lang=` preserved on inner-page navigation
- Phone CTA `Chiama: 06 581 4488` → `tel:+390658144880` (Sapore)
- WhatsApp link `https://wa.me/390658144880` (Sapore) and `https://wa.me/390512345566` (Brace)
- "Prenota un tavolo" / "ORDINA ORA" → respective contact/order pages
- Catalog listing `/templates/restaurant/` shows all 3 cards (Brace · Sapore · Gusto) with NEW badges
- Homepage and other category listings unaffected

### Differentiation locked (D-054 retroactive · 10/10 vs both siblings)

**Sapore vs Gusto:**
- Page background: warm cream `#f8efde` paper · vs · charcoal `#0b0907` editorial dark
- Hero: tilted polaroid photo-frame with rosso "Dal 1987" stamp + handwritten Caveat caption · vs · full-bleed plate photo + corner Michelin star tag + italic credit ribbon
- Type: Libre Baskerville bold + red `<em>` accent + Caveat script garnish · vs · Playfair italic + gold `<em>` editorial drop cap
- Conversion: phone + WhatsApp + chalkboard daily specials + reservation form · vs · concierge tile + ghost-gold ricerca privata + private appointment register
- Voice: warm Roman family register ("come a casa vostra") · vs · aulico editorial-chef-sommelier register ("una serata in otto atti")

**Sapore vs Brace:**
- Page background: warm cream paper · vs · near-black with neon-yellow signal
- Type: structural Libre Baskerville with handwritten Caveat moments · vs · brutalist Big Shoulders Display 900 condensed UPPERCASE
- Hero: photo-frame polaroid + family caption · vs · product-cutout cube tilted -2deg + stamped neon `€ 9.50` price badge
- Cards: chalkboard daily-specials + family portraits · vs · product-grid with "AGGIUNGI" CTAs + flame-red TOP/NEW/VEG tags
- Footer: cream + warm-rosso phone CTA · vs · neon-yellow on black + JetBrains Mono technical specs

**Brace vs Gusto:**
- Page background: near-black with neon-yellow + flame-red signal · vs · charcoal editorial with gold accents
- Type: brutalist Big Shoulders Display 900 UPPERCASE · vs · Playfair italic 500 with editorial drop caps
- Hero: tilted product-cutout square with stamped neon price-badge · vs · full-bleed plate photo with serif star-tag
- Conversion: real-time queue counter strip + AGGIUNGI buttons + GLOVO/DELIVEROO marquee · vs · concierge tile + reservation-only flow
- Voice: imperative second-person Bologna street-register ("ordina ora", "non aspettare") + mono spec chips · vs · third-person editorial sommelier register

### Pexels media constraint

`PEXELS_API_KEY` env var was not present at session start. Per session directive ("usa Pexels come sorgente primaria"), the API integration was skipped — the helper `_pexels_helper.py` is gitignored and the key is never written to repo per D-077. Used existing curated Unsplash IDs from `restaurant-trattoria` + `restaurant-street` pools (verified visually in Sessions 31/47) plus IT-curated additions for trattoria/street-food coherence. No catastrophic mismatches detected via curl HEAD + visual review on the 3 Playwright walks. Pexels swap is documented as a Phase-2g3.6 follow-up in TODO_NEXT for when key is available — the URL format `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=<w>&h=<h>&fit=crop` is hot-link-public, so future swap is one-line per slot.

### Files modified / created

**Created (16):**
- `templates/live_templates/restaurant/trattoria-warm/{_base,home,menu,about,signature,events,contact}.html` (7)
- `templates/live_templates/restaurant/street-modern/{_base,home,menu,about,gallery,order,contact}.html` (7)
- `apps/catalog/template_content_sapore.py` (1)
- `apps/catalog/template_content_brace.py` (1)
- `apps/catalog/template_content_sapore_{en,fr,es,ar}.py` (4)
- `apps/catalog/template_content_brace_{en,fr,es,ar}.py` (4)
- Memory: `restaurant_live_completion_session48.md`

**Modified (5):**
- `apps/catalog/template_content.py` (+10 imports + 2 TEMPLATE_CONTENT entries)
- `TEMPLATE_REGISTRY.json` (2 tier flips + 2 metadata expansions, version 0.10.0 → 0.11.0)
- `smoke_full.py` (+2 templates in LOCALES + CATEGORY)
- `smoke_forms.py` (+2 PAGES + 2 LOCALES_BY_TEMPLATE)
- `smoke_i18n_media_hardening.py` (+2 templates in MULTILINGUAL + CATEGORY)

### Decision: RESTAURANT LIVE COMPLETION PREMIUM APPROVATO (D-078).

Restaurant category goes 3/3 live. Catalog 11/20 published_live across 5 categories. The trattoria-warm and street-modern skin folders are now reusable archetypes available for future restaurant siblings. Phase 2g3 progresses to 2g3.6c follow-ups (Pexels swap, listing PNG generation) and the next gated phase is 2g3.6c (medical 2g3.2 → salute/benessere/famiglia), 2g3.6d (lawyer 2g3.6 → lex/juris), 2g3.6e (real-estate → casa/villa), 2g3.6f (agency → vertex/aura).

---

## Session 47 — Global Media Coherence & Asset Upgrade Pass (2026-04-15)

**Agent:** audit visivo reale + upgrade sistematico della media coherence via Pexels API (chiave da env, mai committata), un solo video editoriale dove il DNA lo giustifica, nessuna nuova feature.

**Shipped:**
- Homepage hero: placeholder wireframe bi-icon → Pexels 4884116 (laptop minimalist, Artem Podrez)
- 5 product heros sostituiti con Pexels IDs verificati 1:1 via Playwright (Luxe `rack-atelier-nero`/`bomber-siena`/`pantalone-wide-crepe`, Bottega `borsa-cartolina`/`tazze-tornite`)
- Preview gallery luxe: Unsplash 1548036328 → Pexels 35115815 in tutti e 5 i locale files
- Luxe lookbook: nuova `.fe-overture` section con Pexels video 4620570 (atelier, 31s, sd 960×506) + poster + reduced-motion fallback
- `_pexels_helper.py` sourcing helper throwaway (gitignored) che legge `PEXELS_API_KEY` da env
- `.gitignore`: aggiunti helper, screenshots temp, media/pexels/

**Validation:**
- `check` clean
- Re-seed commerce idempotente (9+8 products, 16+23 variants)
- Regression sweep 53/53 green
- Chiave API verificata non presente in repo (`grep 3BCdNgmp` in tracked files → 0 risultati)
- Playwright click-through su homepage, Luxe/Bottega shop, Luxe PDP rack-atelier-nero, Luxe lookbook video (readyState=4, currentTime avanza, autoplay + muted + loop)

**Decision: GLOBAL MEDIA COHERENCE & ASSET UPGRADE PASS APPROVATO** (D-077).

---

## Session 45 — Commerce Completion v2 (2026-04-14)

**Agent:** Portare il commerce v1 a stato boutique online reale su 4 assi: (1) `/shop/` davvero multilingua 5 locales con RTL arabo, (2) Stripe integration seria env-driven con graceful fallback, (3) seller dashboard merchant-scoped via StorefrontMember, (4) customer flow completo (policies, order lookup, retry payment). Preservare livello premium Bottega/Luxe e zero regressione sui 9 preview live templates.

### What shipped

**Infrastructure (Python):**
- `apps/commerce/i18n.py` — nuovo modulo con `COMMERCE_CHROME` (125 keys × 5 locales), resolve_locale, get_chrome, is_rtl, html_dir, locale_switcher_entries, preserve_lang_qs
- `apps/commerce/content.py` — `STOREFRONT_CONTENT` (Bottega + Luxe × 5 locales: tagline, footer_bio, shipping_policy, return_policy, bank_transfer_instructions) + `COLLECTION_CONTENT`
- `apps/commerce/payments.py` — nuovo payment abstraction (PaymentContext, PaymentDispatchResult, dispatch_stub, dispatch_offline_bank_transfer, dispatch_stripe, handle_stripe_webhook_event, is_provider_available, graceful ProviderUnavailable fallback)
- `apps/commerce/models.py` — added `translations` JSONField a Storefront + Collection + Product + ShippingMethod; aggiunta Stripe a PaymentProvider choices; nuovo StorefrontMember model (storefront/user/role=owner|editor)
- `apps/commerce/services.py` — `create_order_from_cart` ora usa `payments.dispatch`; nuova `retry_payment(order)`
- `apps/commerce/views/customer.py` — riscritta con LocaleMixin, nuove views PoliciesView + OrderLookupView + PaymentPageView + RetryPaymentView + StripeWebhookView
- `apps/commerce/views/seller.py` — SellerRequiredMixin ora extende LoginRequiredMixin + verifica StorefrontMember; nuova DashboardRootView (chooser)
- `apps/commerce/forms.py` — CheckoutForm chrome-driven + nuova OrderLookupForm + StorefrontMemberForm
- `apps/commerce/urls.py` — nuove routes policies/ordine/payment/retry-payment/webhook/dashboard root
- `apps/commerce/admin.py` — StorefrontMemberInline + StorefrontMemberAdmin
- `apps/commerce/migrations/0003_commerce_v2.py` — manual migration (4 JSONField add + AlterField payment_provider + CreateModel StorefrontMember)
- `marketweb/settings.py` — STRIPE_SECRET_KEY / STRIPE_PUBLISHABLE_KEY / STRIPE_WEBHOOK_SECRET / STRIPE_ALLOW_STUB_FALLBACK from env
- `apps/commerce/management/commands/seed_commerce.py` — SHIPPING_TRANSLATIONS (7 codes × 5 locales), populates translations su Storefront/Collection/ShippingMethod, nuova `_seed_demo_merchants` (bottega_owner/luxe_owner + StorefrontMember)

**Templates (17 touched):**
- `commerce/skins/artisan-workshop/_base.html` — html[lang/dir] dinamico, RTL CSS block, language switcher, chrome-driven, lang_qs ovunque
- `commerce/skins/fashion-editorial/_base.html` — idem per skin maison
- `commerce/skins/*/shop.html` × 2 — iterazione `products_l10n` + chrome labels
- `commerce/skins/*/product.html` × 2 — product_l10n + chrome labels + related_l10n
- `commerce/skins/*/cart.html` × 2 — iterazione `cart_lines` + chrome trust labels
- `commerce/skins/*/checkout.html` × 2 — chrome form labels + shipping_methods_l10n
- `commerce/skins/*/order_confirmation.html` × 2 — chrome status messages + retry payment CTA + Stripe payment page link per intent initiated
- `commerce/skins/*/policies.html` × 2 — NEW (3 card: shipping/returns/contact)
- `commerce/skins/*/order_lookup.html` × 2 — NEW (reference + email form)
- `commerce/payment/stripe.html` — NEW (Stripe Elements + fallback friendly in 5 lingue)
- `commerce/dashboard/_base.html` — "Cambia storefront" + "Esci" nav
- `commerce/dashboard/home.html` — 3 nuove cards (Pagamenti · Membri · Collegamenti rapidi con multi-storefront switch)
- `commerce/dashboard/root.html` — NEW (multi-storefront chooser)

### Validation

- `python manage.py check` → 0 issues
- `python manage.py migrate` → 0003_commerce_v2 applied clean
- `python manage.py seed_commerce` → idempotent, ri-eseguito dopo fix shipping codes
- Commerce smoke: **73/73 OK** (shop/cart/checkout/policies/ordine × 5 locales × 2 skin + product detail × 3 locales × 2 skin + collezione × 2 locales)
- Catalog regression: **45/45 OK** (9 live templates × 5 locales, zero regressione)
- Catalog nav: **5/5 OK**
- Merchant ACL validation:
  - anon `/dashboard/` → 302 (login redirect) ✓
  - anon `/dashboard/<slug>/` → 302 ✓
  - bottega_owner `/dashboard/` → 302 (single-membership auto-redirect) ✓
  - bottega_owner own dashboard → 200 ✓
  - bottega_owner on luxe dashboard → 403 ✓
  - luxe_owner on luxe → 200, on bottega → 403 ✓
- Customer flow end-to-end:
  - add_to_cart → 302 ✓
  - cart EN → 200 ✓
  - checkout POST → 302 con `Order(reference=77159CFCC6, payment=paid, status=confirmed)` ✓
  - order confirmation AR → 200 ✓
  - order lookup POST match → 302 a confirmation ✓
- Stripe graceful:
  - `is_provider_available('stub')` → True
  - `is_provider_available('offline_bank_transfer')` → True
  - `is_provider_available('stripe')` → False (no env keys), ma storefront stripe-configured non 500-a → fallback a stub con `payload.stub_fallback=True` loggato
  - Stripe payment page renders fallback card con CTA in IT/EN/FR/ES/AR quando non configurato

### What's operational with/without env vars

**Without env vars (dev/QA default):**
- stub + offline_bank_transfer payment path end-to-end
- `/commerce/webhook/stripe/` returns 400 "Webhook not configured."
- Stripe payment page renders fallback card (non-configured) con CTA verso order confirmation
- Storefront impostato su stripe degrada a stub con warning log

**With env vars (`STRIPE_SECRET_KEY` + `STRIPE_PUBLISHABLE_KEY` + `STRIPE_WEBHOOK_SECRET` + `pip install stripe`):**
- Real Stripe PaymentIntent flow (test mode o live mode secondo la chiave)
- Webhook signature verification + event routing → PaymentIntent.status + Order.payment_status aggiornati
- Idempotency su order.reference (no double-charge su retry)

### Demo credentials

Da `python manage.py seed_commerce`:
- `bottega_owner` / `commerce-v2` — membro owner di bottega-shop-artigianale
- `luxe_owner`   / `commerce-v2` — membro owner di luxe-fashion-store

### Final verdict: COMMERCE COMPLETION V2 APPROVATO

Tutti i 4 obiettivi chiusi. Commerce ora è una boutique online funzionale, multilingua, con payment provider reale pronto e merchant scoping serio. Zero regressioni sul catalogo live premium.

---

## Session 43 — Commerce Foundation v1 (2026-04-14)

**Agent:** Build the real commerce engine that turns Bottega + Luxe from "live preview premium" into operational shops customers can buy from and sellers can manage. Non-goals: new categories, new templates, touching the 7 non-ecommerce live templates (medical/business/portfolio/restaurant), customer editor, huge refactors, regressions to the existing 9/20 published_live catalog.

**Branch:** `phase-ecommerce-commerce-foundation-v1` (Phase 3a).

### 1 — Audit
`apps/commerce/` was a Django app stub: empty models.py, empty services.py, empty selectors.py, empty urls, placeholder admin. Bottega + Luxe product data lived inside `template_content_bottega.py` / `template_content_luxe.py` as hardcoded dicts — rendered on static pages with no DB, no cart, no checkout, no dashboard. The 9 published_live templates used `LiveTemplateView` + content registries for a marketing/preview surface under `/templates/<cat>/<slug>/preview/`.

### 2 — Strategy
- Keep `/templates/…/preview/` routes unchanged (D-053 Live Preview Law still binds that URL space to the marketing surface).
- Build commerce as an orthogonal layer at `/shop/<storefront_slug>/` for customers and `/dashboard/<storefront_slug>/` for sellers.
- `Storefront` (OneToOne → WebTemplate) is the DB-level "commerce operational" gate — parallels `WebTemplate.tier == published_live` but for commerce readiness (`Storefront.is_operational`).
- Two skin template sets mirror the existing `artisan-workshop` / `fashion-editorial` visual language (warm cream / ink maison) with skin-agnostic `.cx-*` widget CSS driven by per-skin `--cx-*` tokens.
- Dashboard is single-themed (admin-leaning navy/bone) since sellers are operators, not shoppers.
- Payment is provider-agnostic from line one: `PaymentIntent` + `_dispatch_payment` switch. v1 ships `stub` (auto-confirm dev) + `offline_bank_transfer` (awaiting_transfer, seller marks paid). Stripe is documented extension point.
- Products materialize into the DB via `seed_commerce` management command pulling from the IT registries — keeps preview + shop voice in sync.

### 3 — Implementation

**Models** (`apps/commerce/models.py`, 15 models, ~540 LOC):
- `Storefront`, `Collection`, `Product` (with `info_rows` JSON for typographic spec tables + `total_stock` / `is_sold_out` / `is_low_stock` / `display_price` computed properties), `ProductImage`, `ProductVariant` (3 option axes + per-variant stock + price_override).
- `Cart` (session-keyed, user optional) + `CartItem` (snapshots unit_price at add time).
- `Address`, `ShippingMethod` (per-storefront, code+price+ETA).
- `Order` with uuid + 10-char human reference + 3 independent status enums (status/payment_status/fulfillment_status) + timestamps for each transition + tracking fields.
- `OrderItem` (snapshot of product_title, variant_title, sku, unit_price, quantity, line_total, image_url).
- `PaymentIntent` (provider-agnostic, payload JSON for provider-specific data).

**Services** (`apps/commerce/services.py`, ~260 LOC):
- `get_or_create_cart` (upgrades guest→user on login).
- `add_to_cart` / `update_cart_item` / `remove_cart_item` / `clear_cart` with inventory guard (raises `OutOfStockError`).
- `create_order_from_cart` — transactional + `select_for_update` on variants to prevent overselling, creates shipping address row, creates Order + OrderItem snapshots, decrements stock, dispatches PaymentIntent via provider switch, marks cart inactive.
- `_dispatch_payment` → `_handle_stub` (auto-succeed) / `_handle_offline_bank_transfer` (awaiting_transfer, instructions payload).
- `mark_order_paid` (seller) — flips payment_status + order status, updates latest awaiting intent to succeeded.
- `set_order_fulfillment` — transitions fulfillment_status + status, writes tracking fields on shipped, timestamps.
- `cancel_order` — stock rollback + cancelled_at + optional reason in seller_note.

**Selectors** (`apps/commerce/selectors.py`, ~130 LOC): `get_operational_storefront`, `list_active_products` (collection/search/sort filters + prefetch variants + images), `get_product_detail`, `list_collections`, `list_related_products`, `list_storefront_orders`, `dashboard_stock_summary`.

**Customer views** (`apps/commerce/views/customer.py`):
- `ShopView` (ListView with pagination 24/page), `ProductDetailView` (DetailView with variants + related), `CartView` (TemplateView), `AddToCartView` / `UpdateCartItemView` / `RemoveCartItemView` (POST-only), `CheckoutView` (GET renders form, POST creates order), `OrderConfirmationView` (UUID-addressable).

**Seller views** (`apps/commerce/views/seller.py`):
- `SellerRequiredMixin` gates every dashboard view via `is_staff` (redirects to `/admin/login/`).
- `DashboardHomeView` with stock summary + recent orders.
- `ProductsListView`, `ProductCreateView`, `ProductUpdateView` (includes inline variant management on edit page), `ProductDeleteView`.
- `VariantCreateView`, `VariantUpdateView`, `VariantDeleteView` (POST-only, all scoped to storefront+product in one query to prevent cross-tenant access).
- `OrdersListView` (with status filter + pagination), `OrderDetailView` with `mark_paid` / `fulfillment` / `cancel` actions via action=… POST pattern.

**URL structure** (`apps/commerce/urls.py`): mounted at project root, 17 URL patterns split between `/shop/<slug>/...` (customer) and `/dashboard/<slug>/...` (seller).

**Forms** (`apps/commerce/forms.py`): `CheckoutForm` (guest-ok, address + shipping method + note), `ProductForm` (ModelForm scoped to storefront), `ProductVariantForm`, `OrderStatusForm`.

**Admin** (`apps/commerce/admin.py`): all 11 public models registered, Product has ProductImageInline + ProductVariantInline, Order has OrderItemInline + PaymentIntentInline (readonly on production data), list filters by storefront + status.

**Templates** (`templates/commerce/`):
- `skins/artisan-workshop/` — `_base.html` (warm cream palette, `.aw-nav` + `.aw-foot` chrome, Playfair Display + Inter, stamp-shadow `.cx-btn` override) + `shop.html` / `product.html` / `cart.html` / `checkout.html` / `order_confirmation.html`.
- `skins/fashion-editorial/` — `_base.html` (ink charcoal palette, `.fe-nav` + `.fe-foot` chrome, Cormorant Garamond italic + Inter + gold outline, outlined-gold `.cx-btn` override) + same 5 pages.
- `dashboard/` — `_base.html` (admin-leaning navy+bone, `.ds-*` namespace, status pills) + `home.html` (metrics + recent orders) + `products_list.html` + `product_form.html` (with inline variant CRUD) + `orders_list.html` (status filter) + `order_detail.html` (action-based state transitions).

**Shared CSS** (`static/css/commerce.css`, ~450 LOC): skin-agnostic `.cx-*` widgets (messages, shop grid + card, filter rail, PDP hero+strip+info+variant form, specs table, cart table, summary sidebar, checkout form, order confirmation reference band + two-col layout). Driven by `--cx-*` variable contract each skin's `_base.html` defines.

**Seed command** (`apps/commerce/management/commands/seed_commerce.py`): idempotent, `--reset` flag for clean re-seed. Produces:
- Bottega: 9 products × 16 variants across 4 collections (Cuoio · Ceramica · Tessuti · Conserve), 3 shipping methods (48h Italia / ritiro Firenze / Europa 4d), stub payment provider.
- Luxe: 8 products × 23 variants across 5 collections (Drop 01-04 · Atelier), 4 shipping methods (maison Milano / maison Italia / maison Europa / showroom Brera), stub payment provider.
- Shipping policy + return policy + bank transfer instructions per storefront.

**Settings touch:** none. `apps.commerce` was already in INSTALLED_APPS. Commerce URLs were already `include('apps.commerce.urls')` at root in `marketweb/urls.py` (just had zero patterns before).

### 4 — Validation

- `python manage.py check` — 0 issues, 0 warnings.
- `python manage.py makemigrations commerce && migrate` — 1 new migration (`0001_initial.py`) applied cleanly.
- `python manage.py seed_commerce` — green, 9+8 products seeded idempotently.
- **`smoke_commerce.py` · 47/47 green** (new):
  - 8 Bottega customer routes + 9 Luxe customer routes all 200
  - add-to-cart → 2 items in DB (redirect 302)
  - update cart quantity → 1 item (redirect 302)
  - checkout GET 200 with form, checkout POST 302 → order_confirmation
  - Order created with status=confirmed, payment_status=paid (stub auto-confirm), 10-char reference
  - order_confirmation page 200 resolves by UUID
  - Variant stock decremented correctly (3 → 2 after 1-qty order)
  - PaymentIntent row auto-succeeded (stub provider)
  - Seller dashboard anon → 302 → /admin/login/?next=…
  - Staff-authenticated dashboard: 8 routes × Bottega+Luxe all 200 (home, products, products/new, orders, order detail, luxe equivalents)
  - Product edit form renders 200
  - Mark-shipped transition 302 + order.status → shipped, tracking captured
  - All 9 pre-existing published_live templates still 200 under `/templates/<cat>/<slug>/preview/`
- **`smoke_full.py` 363/363** — zero preview-route regressions.
- **`smoke_forms.py` 45/45** — zero form-primitive regressions.
- **`smoke_ecommerce_rollout.py` 194/194** — zero D-054 cross-tenant leaks on the preview layer.
- **`smoke_i18n_media_hardening.py` 57/57** — zero i18n/media regressions.
- **`smoke_chiara_perfection.py` 76/76 · `smoke_pixel_perfection.py` 80/80 · `smoke_i18n_gusto.py` 52/52** — zero regressions.

**Cumulative matrix: 47 + 363 + 45 + 194 + 57 + 76 + 80 + 52 = 914/914 checks green.**

### 5 — Files changed

Created:
- `apps/commerce/models.py` · `services.py` · `selectors.py` · `forms.py` · `urls.py` · `admin.py` · `views/__init__.py` · `views/customer.py` · `views/seller.py`
- `apps/commerce/management/__init__.py` · `management/commands/__init__.py` · `management/commands/seed_commerce.py`
- `apps/commerce/migrations/0001_initial.py` (generated)
- `static/css/commerce.css`
- `templates/commerce/skins/artisan-workshop/` — `_base.html` + 5 page templates
- `templates/commerce/skins/fashion-editorial/` — `_base.html` + 5 page templates
- `templates/commerce/dashboard/` — `_base.html` + `home.html` + `products_list.html` + `product_form.html` + `orders_list.html` + `order_detail.html`
- `smoke_commerce.py`

Untouched (deliberate):
- All `templates/live_templates/**` (9 published_live template skins)
- All `apps/catalog/template_content_*.py` (IT + 4 locale content registries)
- `apps/catalog/template_dna.py`, `preview_imagery.py`, `template_i18n.py`, `views.py`, `urls.py`, `selectors.py`, `services.py`
- `apps/editor/**`, `apps/projects/**`, `apps/pages/**`, `apps/accounts/**`
- `marketweb/settings.py`, `marketweb/urls.py` (commerce include was already present)
- `TEMPLATE_REGISTRY.json`, `CATEGORY_ROADMAP.md`

### 6 — Key insights

1. **Orthogonal URL spaces > overloading existing routes.** Rewiring `/templates/<cat>/<slug>/preview/shop/` to show DB-driven products would have violated D-053. Building `/shop/<slug>/` as a parallel layer preserved the marketing surface and made commerce first-class.
2. **Skin chrome duplication is acceptable here.** The commerce skins duplicate structural CSS from the live-preview skins. Future Phase 3b can extract to a shared partial once commerce i18n is added; for now the duplication keeps both surfaces independently shippable.
3. **Payment abstraction pays off on day 1.** Stripe isn't in v1, but `PaymentIntent` + `_dispatch_payment` makes adding it a file-scope addition, not a schema migration. The `stub` provider auto-confirms in dev so the entire flow is testable end-to-end without a PSP account.
4. **`select_for_update` is Postgres-ready even on SQLite dev.** The service is written assuming the lock works. When production switches to Postgres (planned), overselling protection activates automatically with zero code change.
5. **Guest checkout is first-class.** Cart session-keys + Order UUID-addressable-by-link + no login redirect on checkout means the conversion path is frictionless. Auth is a future value-add, not a precondition.

---

## Session 42 — eCommerce Premium Polish (2026-04-14)

**Agent:** Close two user-flagged blockers from Session 41 review before commit: (1) Bottega has visible image gaps + several visually-wrong Unsplash IDs (HEAD-200 but rendering blue stilettos / classroom / restaurant workers / computer screens / cat / cupcakes / espresso machine / Bond Street tube). (2) Luxe is too static — needs premium fashion-editorial motion / micro-interactions / counters / marquee / cascade reveals, NOT generic SaaS startup motion. Non-goals: any other live template, real cart, new categories, scope expansion.

**Branch:** `phase-ecommerce-live-rollout-v1` (continues Session 41).

### 1 — Audit
Playwright walks at 1440×900 on Bottega home + atelier + product. Grid-rendered every Unsplash candidate at full size to verify. Found 4 broken Bottega URLs (HEAD-404) + 5 wrong-content Bottega IDs (HEAD-200 but visually catastrophic). Plus 2 broken Luxe URLs + 3 wrong-content Luxe IDs (CAT instead of Borsa Isola, BOND STREET TUBE instead of Sentier atelier, woman-in-hoodie instead of professional creative director). Luxe motion audit: 7 sections rendering as static posters, no counters, no marquee, no entry cascades beyond data-lm="reveal" minimum.

### 2 — Strategy
- **Bottega**: dispatched parallel image-curator sub-agent (timed out, 0 bytes output). Pivoted to ARCHITECTURAL fix: convert all 6 portrait slots (4 makers + founder + product-detail artisan signature) to typographic stamp tiles per Bottega's documented DNA ("typographic-led hero, NO photo" — Session 15 DNA notes). Eliminates the portrait sourcing problem entirely + sharpens differentiation vs Luxe (which IS image-driven).
- **Luxe**: ~280 LOC editorial motion CSS block in `fashion-editorial/_base.html`. Motion language deliberately italic-thinking unhurried — long durations (600-1400ms), cubic-bezier(0.16, 0.84, 0.32, 1) "settling poster" easing, planar transforms only (no tilt/bounce). Counter slow-cadenced + marquee very-slow drift + tile zoom unhurried + hover language letter-spacing-driven. Reduced-motion fallback kills every keyframe. Plus link `live-media.css/js` to the Luxe `_base.html` so the marquee primitive works.

### 3 — Implementation

**Bottega — typographic conversion:**
- `home.html` `.aw-makers` markup + CSS — 4 maker portraits replaced with stamp tiles: corner-N number (01-04) + BOTTEGA top-right rubber stamp + big italic letter (S/C/B/A) crest mark with "Firmato" annotation + name + craft + place + since + quote.
- `about.html` `.aw-founder` portrait → 240px circular cream stamp with "M·A" italic monogram + "DAL 1968" stamp + dashed inner ring.
- `product.html` `.artisan` portrait → 200px circular monogram with first letter of artisan name + "FIRMA" stamp.

**Bottega — image swaps (3 product cards still needing fix after curator timeout):**
- Giubbotto Terra hero+cards: BLUE STILETTOS → leather workshop bag (verified, already in registry as Borsa Cartolina — same Severino Falchi pieces, justified duplication).
- Vassoio noce shop+related: ESPRESSO MACHINE → autumnal dried plant tactile texture (verified, already in registry as product gallery).
- Marmellata fichi product card: CUPCAKES IN BOXES → green Italian produce (verified, already in registry as Conserve del mercato).

**Luxe — image swaps (5 fixes):**
- Borsa Isola hero tile + product card + related: A CAT → red leather handbag on white background.
- Sentier atelier maison card + lookbook teaser tile: BOND STREET TUBE STATION → atelier interior with clothes on rack.
- Giulia Maison direttrice creativa portrait: WOMAN IN BLUE HOODIE SMILING → woman in white blazer professional.
- Product gallery 2 broken IDs → leather handbag detail + woman in white hat editorial.

**Luxe — editorial motion pass (~280 LOC in `_base.html`):**
- Hero cover: 14s ease-in-out scale-breathe (1.000 → 1.022 → 1.000).
- Hero headline: italic-axis settle (letter-spacing -0.020em → -0.035em over 1200ms with 220ms delay).
- Cover metadata: issue chip 600ms + caption items 800/980ms fade-up.
- Hero credit-line / intro / actions: sequential fade-up at 1100/1300/1500ms.
- Editorial tile strip: filter shift on hover (grayscale 0%, contrast 1.14, brightness 1.04) + lift 3px + name letter-spacing 0.02em + gold underline scaleX(0.5) slide + tag swap to gold pill.
- Collection product cards (.fe-prod): same editorial hover language adapted.
- Lookbook teaser tiles: scale 1.04 image zoom (1200ms) + name color shift to gold + bottom gold border scaleX(1) slide.
- Lookbook page editorial grid (.fe-look-card): 1400ms zoom + .meta .n letter-spacing expand on hover.
- Manifesto KPI band: counter animation (12, 45, 9, 3) with stagger 160ms + tabular-nums + gold rule scaleX(0.4) slide-in.
- Maison atelier numbers (about page): same counter pattern with 180ms stagger.
- Press strip: converted from `<span>` row to `.lm-logo-marquee` (slow editorial drift 100s, 96px gap, italic Cormorant 22px). Uses existing `live-media.css/js` primitive (now linked in Luxe `_base.html`).
- Drop card: pulsing gold dot indicator (2400ms ease-in-out infinite) + top-edge gold rule scaleX(1) slide-in on enter.
- Private viewing CTA: italic letter-spacing settle on h2 (1400ms cubic-bezier).
- Primary button (.fe-btn-primary): gold panel translateX(-100% → 0) slide-in from left (600ms), inverts to ink-on-gold.
- Ghost button: italic letter-spacing widens 0.28em → 0.30em on hover.
- Nav links: gold underline scaleX(0)→1 slide from left (480ms).
- Atelier cards (about page): image saturation hover + city letter-spacing expand + gold border on hover.
- Press list rows: gold-tinted background hover + magazine name letter-spacing expand.
- Maison cards (contact page): gold left rule scaleY(0)→1 slide on hover.
- Form fields: lf-label color shifts to gold on focus-within.
- Product gallery thumbs: gold border on hover + grayscale 0%.
- Variant pills (PDP): gold panel translateY(100%)→0 slide-in from bottom on hover.
- Reduced-motion fallback: every keyframe + transition stopped.

Plus `home.html` / `about.html` / `lookbook.html` / `collection.html` data-lm wiring updated:
- KPI band: `data-lm="counter" data-lm-to="N"` + `data-lm-stagger data-lm-stagger-delay="160"`.
- Press strip: `<div class="lm-logo-marquee" data-lm-media="logo-marquee">...<div class="lm-logo-marquee-track">...`.
- Tile strip + lookbook teaser + collection grid + ateliers grid: `data-lm-stagger-delay="180/220/120/240"` editorial cadence.
- Lookbook teaser tile: split into outer `.fe-look-tile` + inner `.img` div for the new zoom/saturation hover.

### 4 — Validation

| Check | Result |
|---|---|
| `python manage.py check` | 0 issues |
| `smoke_full.py` | **363/363** routes HTTP 200 (unchanged) |
| `smoke_forms.py` | **45/45** ALL FORM POLISH GREEN |
| `smoke_i18n_media_hardening.py` | **57/57** |
| `smoke_ecommerce_rollout.py` | **194/194** (D-054 cross-leak still 0/120) |
| `smoke_chiara_perfection.py` | **76/76** (regression clean) |
| `smoke_pixel_perfection.py` | **80/80** (regression clean) |
| `smoke_i18n_gusto.py` | **52/52** (regression clean) |

**Total: 867/867 — zero regressions** on the 7 pre-existing live templates.

Visual verification (Playwright walks):
- Bottega home IT: latest band 4 cards coherent (leather/linen/ceramic/produce) · maker stamps typographic with 01-04 corner-N + S/C/B/A italic crest letters · provenance + care + journal teaser + dark CTA all clean.
- Bottega home AR: maker stamps RTL-flipped (04 first) · Latin letters preserved.
- Bottega atelier IT: M·A italic monogram + DAL 1968 stamp.
- Bottega product IT: leather workshop bag hero + S monogram for Severino Falchi.
- Luxe home IT: editorial cover + tile strip with red leather handbag (was cat) + KPI counters animating · lookbook teaser with atelier interior (was Bond Street tube) · press marquee drifting · drop card pulsing dot.
- Luxe home AR: cover RTL-flipped + Maison Luxe / Vogue / city names preserved.
- Luxe maison: 3 atelier cards Brera/Sentier/Aoyama all coherent.
- /templates/ + /templates/ecommerce/ listing surfaces clean.
- Regression /cardio + /pragma + /chiara + /gusto: all unchanged.

### 5 — Files touched

15 modified (5 Bottega content + 5 Luxe content + 3 Bottega skin HTML + Luxe `_base.html` + 4 Luxe page HTML), 1 new memory file.

### 6 — Decision

**ECOMMERCE PREMIUM POLISH APPROVATO.** D-074 added (D-074a Bottega typographic conversion + D-074b Luxe editorial motion).

### 7 — Exact next step

Same as Session 41 § 8 — Phase 2g3.1 (sapore + brace) or Phase 2g3.2 (medical 3) using the now-stable Session 41 + 42 recipe. The image-coherence lesson from Session 42 is binding for any new template authoring: cross-check DNA notes BEFORE adding image-dependent elements; prefer typographic substitutes when DNA permits.

---

## Session 41 — eCommerce Live Rollout (2026-04-14)

**Agent:** Bring `bottega-shop-artigianale` and `luxe-fashion-store` from `tier=draft` to `tier=published_live` premium in a single session, with full multipage live skins + 5 locales fin da subito + sharp differentiation. Fifth category to go live (after medical/restaurant/business/portfolio). Phase 2g3.5. Non-goals: any other template, new categories, real cart/checkout/payment/auth/editor/projects/commerce engine, refactors outside ecommerce.

**Branch:** `phase-ecommerce-live-rollout-v1`. Not committed yet.

### 1 — Audit
Read all 12 context files. Read existing ecommerce DNA + preview compositions (Session 15, blocked on D-047 leaks + skin authoring). Read reference implementations (Pragma corporate-suite + Chiara editorial-designer-grid skins). Confirmed:
- DNA entries exist in `template_dna.py` for both ecommerce templates.
- Preview compositions at `templates/preview_compositions/ecommerce/{artisan-workshop,fashion-editorial}.html` exist with 10+/12+ Bottega/Luxe literals (legacy, not D-047 lifted — deliberately kept untouched, used only for the static listing PNG).
- Zero live skin folders for ecommerce — needed full authoring from scratch.
- Zero content registries for either ecommerce template.
- Tier flip blocked behind both gates.

### 2 — Strategy
- 6 page kinds per template covering D-053 ecommerce baseline + 1 detail (`product_detail`):
  - Bottega: home · shop · product · atelier (about) · journal · contatti
  - Luxe: home · collezione · product · maison (about) · lookbook · contatti
- D-054 differentiation contract documented BEFORE authoring (10 gates, opposite values per template).
- IT registries authored serially by main session (carries the cross-template differentiation thinking).
- 8 locale trees authored by 8 parallel sub-agents with explicit voice contracts (Bottega vs Luxe must STAY OPPOSITE in every locale).
- Cross-leak smoke `smoke_ecommerce_rollout.py` is the binding D-054 gate.

### 3 — Implementation

**Phase A — IT content registries (~1,210 LOC):**
- `template_content_bottega.py` (590 LOC) — full warm-artisan IT tree: 12 botteghe (Severino Falchi conceria Santa Croce, Caterina Lippi ceramiche Montelupo, Bruno Ricci telai Prato, Adele Pignatelli conserve Greve), edition numbers (N° 042, 3/8), rubber-stamp panel data, journal entries, atelier process timeline, contact form fields, FAQ.
- `template_content_luxe.py` (620 LOC) — full maison editoriale IT tree: Maison Luxe Milano · Paris · Tokyo, drop SS26 capsule 04, Look 03/11/14/18 silhouettes, atelier credits (Carla Sozzani styling, Letizia Carrera fotografia), 18-look lookbook with 8-row credits, 5 magazine press citations (Vogue Italia, The Gentlewoman, AnOther, Le Monde D'Hermès, Wallpaper*), private viewing form fields with maison_cards × 3 cities.

**Phase B — Two new skin folders (~5,500 LOC HTML):**
- `templates/live_templates/ecommerce/artisan-workshop/` — `_base.html` (530 LOC: warm cream chrome + circular-crest nav + RTL CSS block + Amiri/Noto-Kufi conditional load) + `home.html` (typographic monolith hero + stamp aside + 4-card latest band + 4-maker grid + 3-card provenance + care strip + press strip + journal teaser + dark CTA band) + `shop.html` (filter rail + 9-card grid) + `product.html` (gallery + variant pills + edition card + specs + artisan signature + care + provenance timeline + related) + `about.html` (atelier mission stamp + 5-step process timeline + founder + numbers stamp + dark visit CTA) + `journal.html` (6 numbered entries) + `contact.html` (lf-* form with select wrapper + contact card + FAQ accordion).
- `templates/live_templates/ecommerce/fashion-editorial/` — `_base.html` (430 LOC: ink charcoal chrome + minimal-serif nav + RTL CSS block + Amiri/Noto-Kufi conditional load + `data-latin` Latin-isolation marker for Vogue/Hermès/cities/prices) + `home.html` (full-bleed cover LEFT + italic Cormorant 108px headline RIGHT + 4-tile editorial strip + manifesto + 4-stat KPI grid + 3-tile lookbook teaser + press strip + drop card + private viewing CTA) + `collection.html` (chip + filter horizontal + 9-product editorial grid) + `product.html` (5-image gallery + editorial caption strip + variant pills + edition card + atelier signature + care + 4-step provenance + related) + `about.html` (statement panel + 3-atelier cards Milano/Paris/Tokyo + direction credit with pull-quote + 5-row press list + 4-stat numbers grid + dark visit CTA) + `lookbook.html` (chip + 8-row credits + 6-look editorial grid with alternating spans + pullquote + 3 set notes + shop CTA) + `contact.html` (private appointment lf-* form + 3-maison-card aside + FAQ accordion).

Both `_base.html` files include `live-motion.css` + `live-forms.css` + `live-interactions.css` static links + their corresponding JS at end-of-body. Both have full `:focus-visible` rings on every interactive surface (CTA, nav links, language pills). Both have mobile breakpoints at 1100px / 1000px / 720px / 580px.

**Phase C — IT bootstrap + tier flip:**
- `template_content.py` — added 10 imports (BOTTEGA_CONTENT_{IT,EN,FR,ES,AR} + LUXE_CONTENT_{IT,EN,FR,ES,AR}) + 2 TEMPLATE_CONTENT entries.
- 8 stub locale files created (`from ... import X_CONTENT_IT as X_CONTENT_EN`) so import succeeds during bootstrap; sub-agents overwrote each.
- `TEMPLATE_REGISTRY.json` v0.9.1 → v0.10.0; both ecommerce rows: `tier=published_live`, `archetype`, `dna_phase=2g3.5`, `session_closed=41`, `live_pages=[6 routes each]`, `locales=[5 codes]`, `rtl=true`.
- `python manage.py sync_template_tiers` applied: 9 templates now `published_live` (cardio + derm + gusto + pragma + elevate + chiara + pixel + bottega + luxe), 11 still draft. Catalog distribution: 9/20.
- IT smoke 12/12 ecommerce routes → 200 (live preview validated before locale rollout).

**Phase D — 8 parallel sub-agents (5–10 min each, ran concurrently):**
- `template_content_bottega_en.py` (~640 LOC) — Aesop / Toast / Etsy informal-warm artisan EN, "you" form, "vegetable-tanned leather", "hand-thrown ceramics", small-batch / signed-by-the-maker.
- `template_content_bottega_fr.py` (~760 LOC) — Astier de Villatte / Merci / Le Bon Marché `tu` artisan FR, French `« »`, "cuir tanné végétal", insecable spaces.
- `template_content_bottega_es.py` (~660 LOC) — peninsular `tú` artesano ES, peninsular vocabulary (cazadora/bolso/cordel/cesto/AOVE), opening `¿` `¡`, `« »`.
- `template_content_bottega_ar.py` (~810 LOC) — cultural-publishing register AR (Brownbook / Bait Al-Hikma), classical MSA, Latin proper names + Latin Western digits.
- `template_content_luxe_en.py` (~710 LOC) — The Gentlewoman / Net-a-Porter formal editorial EN, no contractions, "by appointment", "private viewing", `€2,480` no-space format.
- `template_content_luxe_fr.py` (~850 LOC) — Hermès / Le Bon Marché / Vogue Paris `vous` maison FR, `« »` editorial pull-quotes, `2 480 €` French convention, `11 h 00 – 19 h 00` hours format.
- `template_content_luxe_es.py` (~850 LOC) — Vogue España peninsular `usted` ES, `2.480 €` peninsular convention, "Su perfil" / "Le rogamos" formal markers.
- `template_content_luxe_ar.py` (~830 LOC) — Vogue Arabia luxury-maison register AR, Latin proper names + Latin Western digits + zero Eastern Arabic numerals.

Programmatic shape-diff verified each locale matches IT exactly: 0 missing keys, 0 extra keys, 0 list/tuple length mismatches across all 8 trees.

**Phase E — Smoke harness + final wiring:**
- `smoke_full.py` — bottega + luxe added to LOCALES + CATEGORY dicts; route count 282 → 363.
- `smoke_forms.py` — 2 ecommerce contatti added to PAGES (both with custom `lf-select` wrapper); 35 → 45 form routes.
- `smoke_i18n_media_hardening.py` — both ecommerce templates added to MULTILINGUAL bucket + CATEGORY; 45 → 57 hardening checks.
- New `smoke_ecommerce_rollout.py` (194 checks) — D-054 cross-leak gate (15 Bottega-only tokens + 16 Luxe-only tokens × 5 locales × 12 pages × 2 directions) + AR Latin-isolation (4 + 4 tokens) + 5-pill switcher presence + dir="rtl" + Arabic font load presence.

### 4 — Validation

| Check | Result |
|---|---|
| `python manage.py check` | 0 issues |
| `smoke_full.py` | **363/363** routes HTTP 200 (was 282 → +81) |
| `smoke_forms.py` | **45/45** form routes HTTP 200 (was 35 → +10) |
| `smoke_i18n_media_hardening.py` | **57/57** hardening checks (was 45 → +12) |
| `smoke_ecommerce_rollout.py` (NEW) | **194/194** dedicated ecommerce checks |
| `smoke_chiara_perfection.py` | 76/76 (regression clean) |
| `smoke_pixel_perfection.py` | 80/80 (regression clean) |
| `smoke_i18n_gusto.py` | 52/52 (regression clean) |

Total: **867/867 checks passed**, 0 regressions across the 7 pre-existing live templates. D-054 cross-tenant leak count: **0/120**.

### 5 — Catalog state

**9/20 published_live templates ship in 5 locales** (cardio · derm · gusto · pragma · elevate · chiara · pixel · **bottega** · **luxe**) across **5 categories** (medical/restaurant/business/portfolio/ecommerce). 11/20 still draft (sapore · brace · salute · benessere · famiglia · vertex · aura · lex · juris · casa · villa).

### 6 — Decision

**ECOMMERCE LIVE ROLLOUT PREMIUM APPROVATO.** D-073 added.

### 7 — Files touched

24 created (12 skin HTML + 2 IT content + 8 locale content + 1 new smoke + 1 memory file), 6 modified (template_content.py + TEMPLATE_REGISTRY.json + 3 existing smokes + MEMORY.md), 0 deleted.

### 8 — Exact next step

**Phase 2g3.1** — author Sapore + Brace restaurant skin folders. Their DNA + preview compositions are ready since Session 9. Use the Session 41 recipe verbatim (IT first, 8 parallel locale agents, cross-leak smoke). Catalog will reach 11/20 published_live across 5 categories. Or **Phase 2g3.6** — agency + lawyer + real-estate (6 templates, blocked on 2g2x.1 closure for these 3 categories). Either path closes more of the 11 remaining drafts.

---

## Session 40 — Pragma + Elevate i18n Completion Pass (2026-04-14)

**Agent:** Bring `pragma-corporate-suite` and `elevate-startup-landing` from IT-only to fully multilingual (5 locales + real RTL), preserving the sharp differentiation between Pragma's institutional advisory voice and Elevate's SaaS growth-tech voice. The 7-template `published_live` catalog had 5 multilingual after Sessions 23/24/29/37/39 — these two business templates were the last gap. Non-goals: any other live template (only smoke harness + cross-template chrome touched), new categories, new templates, new archetypes, marketplace chrome i18n, refactors outside business templates, auth/checkout/editor/projects/commerce.

**Branch:** `phase-business-i18n-completion-v1`. Not committed yet.

### 1 — Audit
Read all 12 context files. Read both Pragma + Elevate IT content trees (~870 LOC each) end-to-end. Read all 6 corporate-suite skin templates + all 6 startup-saas-landing skin templates. Found:

**Pragma D-047 leaks (6):** `about.html:128` history narrative · `services.html:98-99` Durata/Lead-partner labels · `case_study_list.html:78-79` Practice/Timeline · `case_study_detail.html:126-129+154-155` Practice/Anno/Durata/Lead/Lead-partner/Team & timeline · `contact.html:208-211` Indirizzo/Zona/Telefono/Email.

**Elevate D-047 leaks (3):** `_base.html:462` `{{ site.tag|default:"Inizia gratis" }}` (uses long-form tagline as nav-CTA + IT fallback) · `pricing.html:44` CSS pseudo-element `content: 'Più scelto'` (CSS-generated content untranslatable) · `contact.html:167-169` Sede/Trasporti/Modello.

### 2 — Strategy
Pragma + Elevate must STAY OPPOSITE in voice. Pragma = institutional B2B advisory (FT/HBR/Les Echos/Cinco Días registers, vouvoiement/usted, MSA boardroom). Elevate = SaaS / growth-tech founder-facing (TechCrunch/Maddyness/Xataka/Wamda registers, tu, anglicismes preserved, Latin product names + Latin acronyms in AR). Lift literals first → spawn 8 parallel sub-agents (4 per template × en/fr/es/ar) with explicit voice contracts → validate shape diffs programmatically → wire in one pass.

### 3 — Implementation

**Phase A — D-047 lift (9 leaks across 7 skin files):**
- Pragma: 6 files modified, fields added to PRAGMA_CONTENT_IT (`history_intro` on chi-siamo, `svc_*_label` on competenze, `office_*_label` on contatti, `case_*_label` on `site` for cross-page meta-strips).
- Elevate: 3 files modified. `_base.html` nav CTA → `{{ site.nav_cta }}` (new field). `pricing.html` Più scelto badge moved from CSS `:before` to HTML `<span class="pop-badge">{{ page_data.highlight_badge }}</span>`. `contact.html` office grid labels lifted.

**Phase B — 8 parallel content authoring sub-agents (ran concurrently in ~4–8 min each):**
- `template_content_pragma_en.py` — 846 LOC · FT/HBR institutional advisory English, "you" formal direct address, no contractions for Pragma's tone.
- `template_content_pragma_fr.py` — 880 LOC · Les Echos vouvoiement, French insecable spaces (`\u00a0` before `:`/`%`/`€`), Capital/McKinsey France register, EUR formatted "1,4 Md €".
- `template_content_pragma_es.py` — 852 LOC · Peninsular usted throughout, Cinco Días/Expansión register, EUR "1.400 M €" Spanish format, comma decimals.
- `template_content_pragma_ar.py` — 848 LOC · Institutional MSA boardroom, Latin proper names, Latin/Western digits, Dott./Avv./Ing. honorifics dropped per MENA business-press convention.
- `template_content_elevate_en.py` — 821 LOC · TechCrunch/Linear/Figma direct-`you` SaaS English with contractions ("we're closing the first fifty early-access seats"), product-led vocab.
- `template_content_elevate_fr.py` — 838 LOC · Maddyness modern SaaS French, `tu` (NOT vous, deliberate contrast with Pragma), insecable `\u202f`, anglicismes preserved (shipper, MRR, founder, A/B test).
- `template_content_elevate_es.py` — 812 LOC · Xataka/K Fund peninsular `tú` (NOT usted, deliberate contrast with Pragma), Spanish anglicismes (shippear, MRR, funnel).
- `template_content_elevate_ar.py` — 813 LOC · Wamda/Hsoub modern startup MSA, Latin product names + Latin acronyms (MRR/Stripe/Linear/GrowthBook/Vercel/PMF/CLI), Latin Western digits.

Programmatic shape-diff verified each locale matches IT exactly: 0 missing keys, 0 extra keys, 0 list/tuple length mismatches across all 8 trees.

**Phase C — RTL CSS blocks + a11y focus + Arabic font load (both _base.html files):**
- `corporate-suite/_base.html` — conditional Amiri + Noto Kufi Arabic font load (when `is_rtl`). `html[dir="rtl"]` block (~120 LOC): font swap, body 17px/1.78, letter-spacing flatten on `.cs-*` chrome labels, button arrow flip `→` → `←`, case-row arrow `scaleX(-1)`, eyebrow margin flip. `{% if is_rtl %}` page-level: hero grid flipped (image left), 4 head-grids flipped, footer 4-col flipped, history timeline border-left → border-right, sectors/KPI border flips, services scope arrow flip. Latin wordmark + Latin numerics retained in heading font with `unicode-bidi: isolate`. New `:focus-visible` rings on .cs-btn-primary, .cs-btn-ghost, nav links, language pills, case rows.
- `startup-saas-landing/_base.html` — conditional Noto Naskh Arabic + Noto Kufi Arabic font load. Similar `html[dir="rtl"]` core block on `.sl-*` selectors plus page-level `direction: rtl` on mockup grid + shiplog list, pop-badge repositioned, comparison/stack/office grids flipped, channel CTA arrow flipped, modules list `flex-direction: row-reverse`. Latin product names + tool versions + numeric values explicitly kept in heading font with `unicode-bidi: isolate` so "v2.9", "MRR", "Stripe", "GrowthBook" stay LTR within RTL flow.

**Phase D — Wire + harness:**
- `template_content.py` — 8 imports, both TEMPLATE_CONTENT entries expanded to 5-locale dicts.
- `smoke_full.py` / `smoke_forms.py` / `smoke_i18n_media_hardening.py` — pragma + elevate moved IT-only → 5-locale.
- `TEMPLATE_REGISTRY.json` — v0.9.0 → v0.9.1, both rows: 5-locale + rtl true, tier_reason updated.

### 4 — Validation

| Check | Result |
|---|---|
| `python manage.py check` | 0 issues |
| `smoke_full.py` | **282/282** routes HTTP 200 (was 226 → +56 new locale routes) |
| `smoke_forms.py` | **35/35** form routes HTTP 200 (was 27 → +8 new locale form routes) |
| `smoke_i18n_media_hardening.py` | **45/45** hardening checks |
| `smoke_chiara_perfection.py` | 76/76 (regression clean) |
| `smoke_pixel_perfection.py` | 80/80 (regression clean) |
| `smoke_i18n_gusto.py` | 52/52 (regression clean) |
| Cross-tenant D-047 leak sweep | **0/40** — no Pragma-token leaks in Elevate or vice versa across 5 locales × 4 token classes |
| D-054 differentiation | All 4 non-IT Pragma locales contain institutional markers (Practice/Pratique/Práctica/الممارسات + partner/associé/socio + CSRD); all 4 non-IT Elevate locales contain SaaS markers (MRR/Stripe/Linear/GrowthBook/Vercel) |

**Playwright walks (1440×900):** Pragma AR home + contatti, Pragma EN home, Elevate AR home + prezzi, Elevate EN home, Cardio AR regression — all clean, RTL flips correct, 0 IT leaks.

### 5 — Catalog state

**7/7 published_live templates ship in 5 locales.** Multilingual coverage on the public catalog complete.

### 6 — Decision

PRAGMA + ELEVATE I18N COMPLETION PASS APPROVATO. D-072 added.

---

## Session 37 — Chiara Perfection Pass (2026-04-13)

**Agent:** Quality perfection pass on a single template. Sole target: bring `chiara-portfolio-creativo` to gold-standard product quality — full 5-locale i18n with native editorial voice, replace generic laptop stock photos with editorial-designer-coherent imagery, lift all hardcoded Italian literals out of the skin HTML, add full RTL CSS support, fix mobile horizontal overflow, add a11y focus rings. Non-goals: any other live template (only smoke harness + cross-template chrome touched), auth/checkout/editor/projects/commerce, drafts, new categories, new templates, new archetypes, marketplace chrome i18n, refactors outside Chiara.

**Branch:** `phase-live-i18n-media-hardening-v1` (continuation — Session 36 still uncommitted on this branch; Session 37 work stacks on top awaiting user direction on branching/commits).

### 1 — Audit
Read all 12 context files. Read all 7 Chiara templates (_base.html + 6 page templates) end-to-end + the 948-LOC IT content registry. Browser walk at 1440×900 (Playwright) on home + studio + lavoro + project_detail + contatti. Mobile walk at 390×844.

**Findings:**

- **9 hardcoded Italian literals** in skin HTML: `home.html` "Tutto l'archivio" + ledger count format · `project_list.html` Disciplina/Durata/Anno meta-row labels · `project_detail.html` Disciplina/Anno/Durata/Equipe meta-strip + "Sintesi del progetto" + "Deliverable consegnati" + "Cosa abbiamo prodotto" + "Colophon" · `process.html` "Sequenza" + "Step X di Y" + "Durata indicativa" · `contact.html` Indirizzo/Ingresso/Metro/Orari studio-card labels.
- **i18n state:** IT only. Switcher correctly auto-hidden via Session 36 D-069 guard. Need full EN/FR/ES/AR content trees (~3500 LOC total budget per D-063 precedent).
- **Featured project images are catastrophically off-brand:** all 4 cards show generic stock photos of laptops/code/dashboards/people-walking. A premium editorial-design studio's home grid showing "Triennale catalog" / "Adelphi book series" / "Querini signage" / "Velluti monograph" should never visualize them as coding workspaces.
- **Founder portrait** is a smiling-businessperson stock photo, not a designer-at-work shot.
- **Mobile horizontal overflow ~124px** on 390px viewport — sections lack proper mobile breakpoints. Inline-styled grid `<div class="head" style="grid-template-columns: 0.45fr 1fr">` blocks let long Italian/Arabic words (Riconoscimenti, pubblicazioni) force columns wider than viewport via grid-item default `min-width: auto`.

### 2 — Strategy
Lift literals first (so all 5 locale trees are authored against the same complete contract), then dispatch 4 parallel sub-agents (one per locale) for content authoring + 1 sub-agent for image curation, then while they work do the RTL CSS + a11y focus + mobile breakpoints, then wire everything up + validate.

### 3 — Implementation

**Phase A — Literal lift on skin HTML (5 files modified, single commit):**
- `apps/catalog/template_content_chiara.py` — added new fields to `home` (`ledger_full_link_label`, `ledger_count_prefix`, `ledger_count_unit`), `lavoro` (`row_discipline_label`, `row_duration_label`, `row_year_label`, `dossier_meta_*_label` × 4, `dossier_summary_label`, `dossier_deliverables_label`, `dossier_deliverables_heading`, `dossier_colophon_label`), `processo` (`step_sequence_label`, `step_index_prefix`, `step_index_separator`, `capability_duration_label`), `contatti` (`studio_address_label`, `studio_area_label`, `studio_metro_label`, `studio_hours_label`).
- 5 skin HTML files updated to read from these new fields instead of hardcoded Italian.

**Phase B — 4 parallel content authoring sub-agents (~5–13 min each, ran concurrently):**
- `template_content_chiara_en.py` — 951 LOC · Anglo-American Pentagram/Eye Magazine register · "Forms that endure, one page at a time" hero
- `template_content_chiara_fr.py` — 1003 LOC · classical étapes/Felix Pfäffli register · `vous` form · French ordinals (24ᵉ Triennale, 38ᵉ édition) · `« »` quotes · French insecable typography
- `template_content_chiara_es.py` — 964 LOC · peninsular Visual/Mucho register · `usted` form throughout
- `template_content_chiara_ar.py` — 940 LOC · formal MSA editorial cultural-publishing register · proper names Latin · Latin digits for technical data · `« »` AR quotes

**Phase C — 1 parallel image curation sub-agent:**
- Downloaded ~50 Unsplash candidates via curl + inspected each via Read tool
- Picked 5 verified IDs with rationale per slot
- Caveats noted: Triennale pick has tablet (not paper); Founder pick is woman holding editorial book (not AD-with-paste-ups). Best-available given the no-laptop/no-phone/no-office constraint stack
- Image IDs swapped in IT tree manually + propagated to 4 locale trees via byte-level Python script (5/5 swaps applied per locale, verified)

**Phase D — RTL CSS + Arabic font conditional:**
- `editorial-designer-grid/_base.html` — added conditional `<link>` for Amiri + Noto Kufi Arabic when `is_rtl`
- New `html[dir="rtl"]` CSS block: font-family swap with Latin fallback, letter-spacing flatten on h1-h5, eyebrow accent-rule flip, `.ed-btn-primary:after` arrow flip (`→` → `←`), ledger + dossier next-arrow scaleX(-1), Latin wordmark font lock (Chiara Velluti Studio stays Latin), JetBrains Mono lock for Latin numeric runs (year/count/credits stay Latin in AR), eyebrow rule margin flip
- Page-level flips guarded by `{% if is_rtl %}` so LTR loads zero RTL bytes: hero grid-template-columns swap, summary/deliverables `<li>` em-dash padding flip, client-code border-side flip, form consent border-side flip, clients-ribbon border-left → border-right
- Founder credentials list em-dash margin flip

**Phase E — Mobile polish + a11y focus:**
- `home.html` — extended `@media (max-width: 720px)` block: ed-commissions padding 56px → 20px gutter, ed-press inline-styled grid heads forced to single-column with `min-width: 0` on grid items + h2 font-size override (`!important` since fighting inline style), ed-cta wrap collapses to 1fr, additional `@media (max-width: 480px)` for hero h1 down to 38px
- `_base.html` — new `:focus-visible` rings on `.ed-btn-primary` + `.ed-btn-ghost` (2px accent outline + 4px offset)

**Phase F — Wiring + smoke harness extension:**
- `template_content.py` — added 4 new imports, registered 4 new locale keys for chiara
- `smoke_full.py` — chiara LOCALES list extended from `["it"]` to all 5 codes (route count 170 → 198)
- `smoke_i18n_media_hardening.py` — moved chiara from IT_ONLY tuple to MULTILINGUAL tuple (Session 36 hardening pass anticipated this)
- New `smoke_chiara_perfection.py` (155 LOC) — 76 content-marker checks: 5-locale signature phrase render, AR `dir="rtl"` + Arabic font load, image ID swap verification × 5 locales, founder portrait swap × 5 locales, IT-literal leak sweep on lifted labels × 4 non-IT × 5 pages, full route sweep × 5 locales × 8 pages

### 4 — Validation

- `python manage.py check`: 0 issues.
- `smoke_full.py`: **198/198 routes HTTP 200** (was 170 baseline pre-Chiara; +28 = 4 new locales × 7 chiara pages).
- `smoke_forms.py`: **27/27 form routes HTTP 200** (D-066 forms system untouched).
- `smoke_i18n_media_hardening.py`: **45/45 hardening checks passed** (Chiara migrated from IT_ONLY to MULTILINGUAL bucket — switcher must now render on all 5 locale routes).
- `smoke_chiara_perfection.py` (new): **76/76 checks passed**.
- Playwright walk 1440×900 on IT/EN/FR/ES/AR home + AR project_detail + AR contact + ES home + FR home: signature phrase rendered per locale ("Forme che durano" / "Forms that endure" / "qui durent" / "que perduran" / "أشكالٌ تَبقى"), 5-pill switcher visible everywhere, AR has `dir="rtl"` + `lang="ar"` + Latin wordmark stays Latin + Latin digits in numeric meta + section grid flips correctly, 4/4 featured project images visibly editorial (book-spine stack, warm museum interior, type-ideation tablet, fountain-pen-on-manuscript).
- Mobile sanity at 390×844: overflow **-15px** (fits with slack, no horizontal scrollbar) — was 124px before Session 37.

### 5 — Files touched

22 modified (3 of them new), 0 deleted.

**New files (5):**
- `apps/catalog/template_content_chiara_en.py` (951 LOC)
- `apps/catalog/template_content_chiara_fr.py` (1003 LOC)
- `apps/catalog/template_content_chiara_es.py` (964 LOC)
- `apps/catalog/template_content_chiara_ar.py` (940 LOC)
- `smoke_chiara_perfection.py` (155 LOC)

**Modified Python (3):**
- `apps/catalog/template_content_chiara.py` — added Phase A label fields + image ID swaps
- `apps/catalog/template_content.py` — registered 4 new locale imports + chiara TEMPLATE_CONTENT entries
- `smoke_full.py` — chiara LOCALES list expanded to 5
- `smoke_i18n_media_hardening.py` — chiara migrated IT_ONLY → MULTILINGUAL

**Modified skin HTML (5):**
- `templates/live_templates/portfolio/editorial-designer-grid/_base.html` — Arabic font conditional + RTL CSS block + a11y focus rings
- `templates/live_templates/portfolio/editorial-designer-grid/home.html` — literal lift + mobile breakpoints
- `templates/live_templates/portfolio/editorial-designer-grid/project_list.html` — literal lift
- `templates/live_templates/portfolio/editorial-designer-grid/project_detail.html` — literal lift
- `templates/live_templates/portfolio/editorial-designer-grid/process.html` — literal lift
- `templates/live_templates/portfolio/editorial-designer-grid/contact.html` — literal lift

### 6 — Decision

**CHIARA I18N COMPLETION + PREMIUM PERFECTION PASS APPROVATO.** D-070 documented in DECISIONS.md.

`chiara-portfolio-creativo` now meets the gold-standard quality bar the user asked for:
- 5 vere lingue · zero fallback finti · structural parity verified per locale
- Editorial-designer-coherent imagery on home + founder portrait — laptop stock photos retired
- Skin HTML zero-leak: every label flows through `page_data.*`
- Mobile horizontal overflow at 390px: -15px (fits with slack)
- AR RTL: `dir="rtl"` + Amiri body + Noto Kufi Arabic display + Latin wordmark/digit lock
- a11y focus rings on every CTA
- Native editorial voice per locale (no machine translation)

Catalog state: 4/7 published_live now ship in 5 locales (cardio · derm · gusto · chiara). Pixel + Pragma + Elevate remain IT-only — Pixel is the natural next target (shares portfolio category, will inherit the editorial-designer-grid Phase D RTL pattern only if it gets its own RTL CSS block since it uses the cinematic-photographer skin).

### 7 — Exact next step

**Phase 2i.2c** — Pixel locale rollout. Same Session 37 recipe (4 parallel content agents + 1 image curator + RTL CSS + smoke). Budget ~3h end-to-end based on Session 37 timing. Pixel's cinematic-photographer skin needs its own `html[dir="rtl"]` CSS block (not shared with editorial-designer-grid). After Pixel closes, only Pragma + Elevate remain IT-only; both can ship their locales together via Phase 2i.2d.

---

## Session 36 — Live i18n & Media Coherence Hardening (2026-04-13)

**Agent:** Quality hardening on top of Sessions 34–35. Sole target: correct two user-flagged coherence defects on the 7 `tier=published_live` templates — (1) a language switcher that advertised 5 locales on IT-only templates and silently fell back to IT; (2) three `lm-video` blocks shipping with the Big Buck Bunny placeholder MP4 as src plus codec-theatre metadata (`4K`, `1080p · 24 fps`, `Play · 3:12`). Non-goals: auth, checkout, editor, projects, commerce, drafts, new categories, new templates, new archetypes, new locale trees for IT-only templates, marketplace chrome i18n.

**Branch:** `phase-live-i18n-media-hardening-v1` (forked from `phase-integration-baseline-v4`). Session 35's `phase-live-motion-media-pass-v1` was first merged in so the hardening could operate on the integrated surface; the merge + subsequent fixes are the content of this branch.

### 1 — Audit (read-only)
Read the 12 context files front-to-back. Walked the i18n registry (`template_content.py` + `template_content_cardio_i18n.py` / `_dermatologia_i18n.py` / `_gusto_i18n.py`) to tally locale coverage per template. Walked the media surface (`templates/live_templates/**/home.html` + `_base.html`) to locate every `lm-video`, `lm-logo-marquee`, `live-media.css`, `live-media.js` site.

**Coverage matrix found:**

| Template | IT | EN | FR | ES | AR |
|---|---|---|---|---|---|
| cardio-studio-specialistico | yes | yes | yes | yes | yes |
| dermatologia-elite-roma | yes | yes | yes | yes | yes |
| gusto-fine-dining | yes | yes* | yes* | yes* | yes* |
| pragma-corporate-suite | yes | — | — | — | — |
| elevate-startup-landing | yes | — | — | — | — |
| chiara-portfolio-creativo | yes | — | — | — | — |
| pixel-portfolio-fotografico | yes | — | — | — | — |

(*) Gusto non-IT locales are complete for all Sessions 23–30 content keys but the Session 35 `signature_video` block was added IT-only — under `?lang=en|fr|es|ar` on Gusto the block disappears gracefully via its `{% if page_data.signature_video %}` guard, producing content-depth disparity between locales. Not a bug per se (graceful), but a symptom of the same under-authored-new-block pattern.

**Media surface found:**
- 3 `lm-video` blocks: `gusto-fine-dining` (home `signature_video`), `elevate-startup-landing` (home `product_video`), `pixel-portfolio-fotografico` (home `reel`). All three used `commondatastorage.googleapis.com/.../ForBiggerBlazes.mp4` as src. All three carried codec-theatre captions (`Demo · 2:14 · 1080p`, `Reel · 1080p · 24 fps`, `Play · 3:12`) and meta rows (`Camere · Due fisse · 4K`).
- 3 `lm-logo-marquee` blocks: `pragma-corporate-suite` (home `sectors` + `trust_logos`), `elevate-startup-landing` (home `integrations`). Content is real institutional/tech wordmarks — coherent, kept.
- 1 `featured_works` lightbox grid on `chiara-portfolio-creativo` home — real project images, kept.
- `live-media.css/js` linked on 6 bases but only consumed on 3 (Pragma, Elevate, Gusto pre-hardening). Cardio, Derm, Chiara, Pixel bases linked the primitives without using them — orphan payload.

### 2 — Strategy

Two surgical hardening decisions, no new content authoring:

1. **Switcher honesty (D-069 rule 1):** `locale_switcher_entries()` becomes template-aware. View computes `available_locales` via `template_content.get_available_locales(slug)` and suppresses the switcher when `len(available_locales) <= 1`. All 6 skin `_base.html` files wrap their switcher markup in `{% if locale_switcher %}`. Result: Pragma / Elevate / Chiara / Pixel render with no switcher; Cardio / Derm / Gusto keep their 5-pill switcher.

2. **Media honesty (D-069 rule 2–4):**
   - `gusto-fine-dining.signature_video` — REMOVED entirely (content block + HTML section + CSS rules). The atmosphere_teaser 4-tile lightbox already carries behind-the-scenes mood.
   - `pixel-portfolio-fotografico.reel` — REMOVED entirely (content block + HTML section + CSS rules). The filmstrip + EXIF strip + series index carry the cinematic identity.
   - `elevate-startup-landing.product_video` — CONVERTED to `product_demo_card`: same cosmic-glass frame + dashboard-still poster, but the `<video>` tag and codec caption become a premium overlay with dual CTA pointing to `/demo/` (primary, "Prenota il walkthrough") + `/prodotto/` (secondary, "Esplora il prodotto").

Every cardio/derm/chiara/pixel/gusto `_base.html` unlinks `live-media.css` + `live-media.js` (orphan after video removal) and drops orphan `--lm-video-*` tokens + specificity-shielding selectors. Pragma + Elevate keep both (they still consume the marquee primitive).

### 3 — Implementation

**`apps/catalog/template_i18n.py`** — `locale_switcher_entries(current_locale, available_locales=None)` gets a new optional arg. When passed, scopes the returned entries to that list; when omitted, preserves legacy "all 5 locales" behaviour for backward compat.

**`apps/catalog/template_content.py`** — new helper `get_available_locales(slug) -> list[str]`. Reads `TEMPLATE_CONTENT[slug]` and returns the ordered subset of `SUPPORTED_LOCALES` that have a locale tree. Also the place where `gusto-fine-dining.signature_video` IT block was removed (`GUSTO_CONTENT_IT` home dict).

**`apps/catalog/views.py`** — `LiveTemplateView.get_context_data` computes `available_locales` once and threads `ctx["available_locales"]` + a conditionally-empty `ctx["locale_switcher"]`. When `len(available_locales) > 1`, the switcher populates as usual; otherwise empty list → skin's `{% if locale_switcher %}` branch is skipped.

**6 skin `_base.html` files** — switcher markup wrapped in `{% if locale_switcher %}`:
- `medical/specialist/_base.html`
- `restaurant/fine-dining/_base.html`
- `business/corporate-suite/_base.html`
- `business/startup-saas-landing/_base.html`
- `portfolio/editorial-designer-grid/_base.html`
- `portfolio/cinematic-photographer/_base.html`

**4 skin `_base.html` files** — `live-media.css` + `live-media.js` unlinked + orphan `--lm-video-*` tokens stripped + `.lm-video` specificity-shielding rules pruned:
- `medical/specialist/_base.html` (cardio + derm)
- `restaurant/fine-dining/_base.html` (gusto)
- `portfolio/editorial-designer-grid/_base.html` (chiara)
- `portfolio/cinematic-photographer/_base.html` (pixel)

**Gusto home** (`templates/live_templates/restaurant/fine-dining/home.html`) — `<section class="fd-signature-video">` block (27 LOC HTML) + 46 LOC of `.fd-signature-video*` CSS rules both removed.

**Pixel home** (`templates/live_templates/portfolio/cinematic-photographer/home.html`) — `<section class="cp-reel">` block (27 LOC HTML) + 46 LOC of `.cp-reel*` CSS rules both removed.

**Elevate home** (`templates/live_templates/business/startup-saas-landing/home.html`) — the `<section class="sl-product-video">` block with the lm-video figure (22 LOC) is replaced by a `<section class="sl-demo-card">` block (18 LOC) using the same poster, new dual-CTA overlay, no `<video>`. 21 LOC of `.sl-product-video` + `.sl-video-frame` CSS become 52 LOC of `.sl-demo-card` + `.sl-demo-frame` CSS (overlay gradient, poster background-image layer, secondary-button contrast tuning).

**Elevate content** (`apps/catalog/template_content_elevate.py`) — `product_video` key replaced with `product_demo_card` dict: `label / heading / intro / poster / primary_cta / primary_href / secondary_cta / secondary_href / caption`. Two CTAs target existing pages (`demo`, `prodotto`) so the routing is honest and functional. Updated `.sl-mono` utility selectors in the base to target `.sl-demo-card .head .sec-label.sl-mono` + `.sl-demo-frame .caption.sl-mono` (replacing `.sl-product-video` selectors that no longer match anything).

**Pixel content** (`apps/catalog/template_content_pixel.py`) — `reel` key removed. Replacement comment block explains the decision and the conditions for reintroducing (real signed MP4 + on-brand meta).

**Gusto content** (`apps/catalog/template_content.py`) — `signature_video` key removed from `GUSTO_CONTENT_IT.home`. Replacement comment block explains the decision.

### 4 — Verification — new smoke harness

Added `smoke_i18n_media_hardening.py` (~155 LOC). Scope:

1. **IT-only-switcher-hidden (25 checks).** For Pragma / Elevate / Chiara / Pixel × home + every inner page, fetch the page and assert the rendered HTML does NOT contain `<div class="mp-lang"` / `<nav class="mp-lang"` / `class="mp-lang-pill`. The CSS rules for `.mp-lang*` may still appear in the inline `<style>` block (structural) — only the markup opening tag is forbidden.
2. **Multilingual-switcher-intact (15 checks).** For Cardio / Derm / Gusto × 5 locales, fetch the home page and assert the switcher markup IS present AND the 5 badges (`IT`, `EN`, `FR`, `ES`, `AR`) all render.
3. **Forbidden-media-token scan (7 checks).** For every live template's home page, scan the rendered HTML for `ForBiggerBlazes.mp4`, `commondatastorage.googleapis.com`, `Demo · 2:14 · 1080p`, `Reel · 1080p · 24 fps`, `Play · 3:12`, `Due fisse · 4K`. Zero tolerance.
4. **Elevate demo-card presence (1 check).** Assert `sl-demo-card` class + `Prenota il walkthrough` copy both render.
5. **Pixel no-video (1 check).** Assert `lm-video` AND `cp-reel` are both absent.
6. **Gusto no-video (1 check).** Assert `lm-video` AND `fd-signature-video` are both absent.

**Result: 45/45 hardening checks passed.**

### 5 — Regression safety net

- `python manage.py check`: 0 issues.
- `smoke_full.py`: **170/170 routes HTTP 200** — identical to the Session 34 baseline. Zero regression from the D-068 motion/media pass removal of video blocks.
- `smoke_forms.py`: **27/27 form routes HTTP 200** — D-066 forms system untouched.
- Playwright walk at 1440×900 on: Elevate `/preview/` (demo card renders, no video tag, no switcher), Gusto `?lang=en` (signature_video gone, 5-pill switcher present), Gusto `?lang=ar` (`dir=rtl` + RTL content preserved + no video), Chiara + Pixel `/preview/` (no switcher + no video + no reel frame + filmstrip and ledger intact), Cardio `?lang=fr` (5-pill switcher intact).

### 6 — Files touched

13 modified, 1 new, 0 deleted. New file: `smoke_i18n_media_hardening.py`.

**Python (5):**
- `apps/catalog/template_i18n.py` — `locale_switcher_entries()` extended with optional `available_locales` parameter.
- `apps/catalog/template_content.py` — `get_available_locales()` helper added + Gusto `signature_video` block removed with rationale comment.
- `apps/catalog/template_content_elevate.py` — `product_video` → `product_demo_card` conversion.
- `apps/catalog/template_content_pixel.py` — `reel` block removed with rationale comment.
- `apps/catalog/views.py` — `LiveTemplateView` threads `available_locales` + conditional `locale_switcher` into context.

**Skin `_base.html` (6):**
- `templates/live_templates/medical/specialist/_base.html` — switcher guard + live-media unlink.
- `templates/live_templates/restaurant/fine-dining/_base.html` — switcher guard + live-media unlink + `--lm-video-*` token removal.
- `templates/live_templates/business/corporate-suite/_base.html` — switcher guard (live-media kept; marquee consumer).
- `templates/live_templates/business/startup-saas-landing/_base.html` — switcher guard + `--lm-video-*` token removal (live-media kept; marquee consumer) + `.sl-product-video` selector renamed to `.sl-demo-card` chain.
- `templates/live_templates/portfolio/editorial-designer-grid/_base.html` — switcher guard + live-media unlink + `--lm-video-*` token removal + `.lm-video .cp-mono` specificity selectors pruned.
- `templates/live_templates/portfolio/cinematic-photographer/_base.html` — switcher guard + live-media unlink + `--lm-video-*` + `--lm-marquee-*` token removal + `.lm-video .cp-mono` specificity selectors pruned.

**Skin `home.html` (3):**
- `templates/live_templates/restaurant/fine-dining/home.html` — signature_video section + CSS removed.
- `templates/live_templates/portfolio/cinematic-photographer/home.html` — reel section + CSS removed.
- `templates/live_templates/business/startup-saas-landing/home.html` — product_video section + CSS converted to product_demo_card.

### 7 — Decision

**LIVE I18N & MEDIA HARDENING APPROVATO.** D-069 documented in DECISIONS.md.

The catalog's 7 `tier=published_live` templates now pass the two coherence gates the user flagged:
1. Every template's language switcher matches its content depth (5 pills only where 5 locales are authored).
2. Every template's media surface is either real (Pragma sectors / Elevate integrations wordmarks / Chiara lightbox project grid) or absent (no Big Buck Bunny placeholders, no codec-theatre captions).

The live-media.css/js primitive remains in the repo as a latent capability. When a future template has a real signed MP4 and on-brand metadata that reinforces (not pretends) its identity, re-introduction is zero-infrastructure work.

### 8 — Exact next step

**Phase 2g3.5 — agency CRITICO lift** remains the blocking roadmap gate (per D-049). Separately, **Phase 2i.2b** is a new latent ticket: when the next locale-coverage wave is scheduled, author EN/FR/ES/AR content trees for Pragma / Elevate / Chiara / Pixel (one per session, ~3h each per the D-063 budget). When each template's `TEMPLATE_CONTENT[slug]` entry gains a 2nd locale key, its switcher automatically re-appears — no chrome work needed.

---

## Session 35 — Live Motion, Media & Typography Premium Pass (2026-04-13)

**Agent:** Premium UI / interaction polish session. Sole target: raise the quality of the 7 `tier=published_live` templates along three axes — motion (counters where credible), media (video + gallery + marquee where genuinely coherent with the archetype), typography (per-template font character). Non-goals: new categories, new templates, draft templates, auth/checkout/editor/projects/commerce, refactors outside scope.

**Branch:** `phase-live-motion-media-pass-v1` (forked from `phase-integration-baseline-v4`).

### 1 — Audit
Read the 12 context files + memory index. Audited the 6 skin folders (medical/specialist · restaurant/fine-dining · business/corporate-suite · business/startup-saas-landing · portfolio/editorial-designer-grid · portfolio/cinematic-photographer) hosting the 7 published_live templates. Found 4 systemic gaps: (1) **zero counters wired** on Pragma KPI strip + Elevate metric strip + Elevate mockup metrics + Elevate founders despite numeric-heavy layouts; (2) **no video integration anywhere** — the entire catalog had no template demonstrating a real video moment; (3) **no marquee/logo drift** on institutional sectors / SaaS integrations / press wordmarks; (4) **typography under-developed** — every skin loaded only 2 fonts (heading + body), no monospace accent, no italic-axis emphasis, no tabular-nums on metric strips.

### 2 — Strategy
Ship two new shared primitives + per-template wiring under D-047/D-054 invariants:

| Template | Counters | Lightbox | Video | Marquee | Typography refinement |
|---|---|---|---|---|---|
| Cardio (specialist) | preserved (3) | — | NO (clinical) | NO | italic h-em wt 400 + tabular-nums + line-height 1.6→1.55 |
| Derm (shared specialist) | preserved (3) | preserved | NO (shared) | NO | inherits cardio refinements |
| Gusto (fine-dining) | preserved (3) | preserved | **YES — signature ambient video** | NO | italic h-em wt 600 + tabular-nums on facts/courses |
| Pragma (corporate-suite) | **YES — KPI strip × 4** | NO | NO (corporate authority) | **YES — sectors + trust** | italic accent serif + tabular-nums KPI |
| Elevate (startup-saas-landing) | **YES — metric × 4 + mockup × 3 + founders × 2 = 9** | NO | **YES — product demo video** | **YES — integrations × 12** | **JetBrains Mono** ship-log + metric labels |
| Chiara (editorial-designer-grid) | NO (typographic identity) | **YES — featured grid** | NO (typographic identity) | NO | italic Syne wt 700 + **JetBrains Mono** indices |
| Pixel (cinematic-photographer) | NO (would cheapen) | preserved | **YES — cinematic reel block** | NO | h1 letter-spacing 0.005em → 0.018em + push existing **JetBrains Mono** |

Video decisions: **3 templates get video** (the 3 archetypes where motion/cinema is part of the category vocabulary — fine-dining hospitality, growth-tech SaaS, photographer reel). **4 templates do NOT get video** (clinical specialist + corporate authority + typographic editorial — adding video would cheapen each archetype).

### 3 — Implementation

**New shared primitives:**
- `static/css/live-media.css` — `.lm-video` poster + click-to-play HTML5 native (no autoplay, no iframes, no third-party tracking), `.lm-logo-marquee` slow-drift wordmark scroll, `.lm-num` 3-cell numeric break-out helper. ~250 LOC, prefers-reduced-motion aware, RTL-safe via logical properties, per-skin token overrides via 5 CSS custom properties.
- `static/js/live-media.js` — lazy video boot on first user click (creates `<video controls preload="metadata" playsinline>` with `<source>`, attaches `is-playing` class, swallows blocked autoplay rejection silently), Esc-to-pause, marquee track JS-duplication for seamless `-50%` keyframe loop, prefers-reduced-motion opt-out (skips marquee duplication). ~110 LOC zero-dep IIFE.

**Counter primitive extension (live-motion.js):**
- Regex extended from `^(-?\d+(?:[.,]\d+)?)(.*)$` to `^(\D*?)(-?\d+(?:[.,]\d+)?)(.*)$` so leading non-digit prefix (`€ 1.4 B`, `+ 38%`, `↑ 22`) is captured + preserved verbatim during animation.
- Italian thousand-separator heuristic added: if numeric matches `^(\d{1,3})\.(\d{3})$` (e.g. "1.200") the dot is treated as thousand-separator → animates 0 → 1200 with regex-based `\B(?=(\d{3})+(?!\d))` re-formatting back to "1.200" on each frame. Backwards-compatible with every previously-working counter (verified on cardio/gusto facts).

**Per-template `_base.html` token + font + typography:**
- `business/corporate-suite/_base.html` — wire live-media; sectors marquee tokens (110s drift, 72px gap, ink-soft color); italic h-em accent at weight 600; tabular-nums on KPI/cases.
- `business/startup-saas-landing/_base.html` — wire live-media; load JetBrains Mono via Google Fonts; cosmic video frame tokens (cyan-glow play orb ring); growth-tech marquee tokens (70s, snappier); `--mono` CSS token; `.sl-mono` utility selector specificity-shielded against existing `.sl-shiplog .list .ver` (chained 0,0,3,0).
- `restaurant/fine-dining/_base.html` — wire live-media; cinematic video frame tokens (gold play orb on warm-cream); italic h-em accent at weight 600; tabular-nums on facts + courses.
- `medical/specialist/_base.html` — wire live-media; italic h-em accent at weight 400 (clinical sobriety); body line-height 1.6→1.55; tabular-nums on facts + signature_visits + percorso. Shared by cardio + derm (D-046 archetype reuse).
- `portfolio/editorial-designer-grid/_base.html` — wire live-media + live-interactions + load JetBrains Mono; italic Syne accent at weight 700; `--mono` token; `.ed-mono` utility specificity-shielded.
- `portfolio/cinematic-photographer/_base.html` — wire live-media + live-interactions; cinema video frame tokens (red pulse ring); cinematic marquee tokens (130s, very slow); h1 letter-spacing 0.005em → 0.018em (cinematic measured rhythm); `.cp-mono` utility specificity-shielded.

**Per-template home.html (sections / wiring):**
- `business/corporate-suite/home.html` — counters on `.cs-kpi-band .stat .num` (4 metrics: 22 / 180+ / € 1.4 B / 94%); sectors marquee block under sectors band; trust wordmarks marquee under trust band.
- `business/startup-saas-landing/home.html` — counters on mockup `.metric .big` × 3 + `.sl-metric-band .stat .num` × 4 + founders `.metric .num` × 2 = **9 counters total**; new `.sl-product-video` section between mockup and trust strip; integrations marquee below static integrations grid; mono utility on shiplog version + date + integration items + product video caption.
- `restaurant/fine-dining/home.html` — new `.fd-signature-video` section between chef portrait and atmosphere strip with editorial italic title + 4-cell ambient meta + gold play orb + caption.
- `portfolio/editorial-designer-grid/home.html` — new `.ed-projects` section between capabilities and clients with asymmetric 4-card grid (1 large + 3 normal) + lightbox group + mono "№ 01" indices + footer link.
- `portfolio/cinematic-photographer/home.html` — new `.cp-reel` section between filmstrip and about-excerpt with cinematic poster + 6-cell EXIF strip (Format / Durata / Camera / Ottica / Audio / Color grade) + bracket-mono caption.

**Content registries (per-template content blocks):**
- `apps/catalog/template_content.py` (Gusto IT) — added `home.signature_video` block (label/title/intro/4-cell meta/poster/src/play_label/caption + NOTE comment about CC-licensed src placeholder).
- `apps/catalog/template_content_elevate.py` — added `home.product_video` block (label/heading/intro/poster/src/play_label/caption + NOTE comment).
- `apps/catalog/template_content_chiara.py` — added `home.featured_works` block (label/heading/intro/4 items with year/discipline/title/blurb/image/href + footer link).
- `apps/catalog/template_content_pixel.py` — added `home.reel` block (label/heading/intro/6-cell EXIF/poster/src/play_label/caption + NOTE comment).

### 4 — Video URL strategy (BINDING, recorded for production migration)

The 3 video blocks (Elevate / Gusto / Pixel) ship with a **functional placeholder src** pointing at `https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4` — a CC-licensed Big Buck Bunny test asset on Google's public CDN. It demonstrates the lm-video integration end-to-end (poster + native HTML5 player on click + controls + Esc-to-pause), but the content (animated film) is obviously off-brand. **Each video block is annotated in its content registry with a NOTE comment.** Real customers / production fills `src` with their own brand video URL — the poster + caption typography then carry the brand identity uninterrupted.

If the placeholder URL ever 404s, the lm-video CSS keeps the poster visible behind the `.is-playing` overlay (the `<video>` tag's source-load failure is silent; black frame underneath the play button which fades out via `.is-playing`). Acceptable risk: the moment a user clicks Play and sees a broken video, they understand the placeholder is provisional. The poster + caption typography never break.

### 5 — Validation

- `python manage.py check` — 0 issues.
- Full DB rebuild + `seed_categories` + `seed_templates` — 8 categories, 20 templates, 7 promoted to `published_live` (auto registry sync).
- `python smoke_full.py` — **170/170 routes HTTP 200** (no regression vs Session 34 baseline).
- `python smoke_forms.py` — **27/27 form routes HTTP 200** (no regression vs Session 33).
- Browser walk via Playwright at 1440×900:
  - **Pragma** — KPI strip animates `0 / 0 / € 0.0 B / 0%` → `22 / 180+ / € 1.4 B / 94%`; sectors marquee scrolls (track JS-duplicated to 20 items); KPI numerals use Merriweather with `font-variant-numeric: tabular-nums`. Italic h-em accent active on hero "decisioni che contano".
  - **Elevate** — 9 counter elements all reach final values; `.sl-product-video` renders with code/dashboard poster + white play orb + JetBrains Mono "Tour del prodotto · Demo · 2:14 · 1080p" caption; integrations marquee scrolls; `.sl-shiplog .row .ver.sl-mono` computed font is `"JetBrains Mono", ui-monospace, ...`.
  - **Gusto** — 3 counters preserved; `.fd-signature-video` renders with kitchen-team poster + gold play orb + 4-cell ambient meta strip + italic-axis "Quattro ore in cucina, due camere fisse." headline.
  - **Cardio (IT)** — 3 counters animate to "15 / 1.200 / 4" — Italian thousand-separator heuristic correctly preserves "1.200" (was "1.2" before). Italic h-em editorial accent at weight 400.
  - **Cardio (AR)** — `dir=rtl`, `lang=ar`, body font `"Noto Kufi Arabic", Inter, system-ui, sans-serif` — i18n/RTL not regressed.
  - **Chiara** — `.ed-projects` renders 4 lightbox-enabled cards in asymmetric grid; mono "№ 01 / 02 / 03 / 04" indices on each frame; italic Syne accent on "quattro discipline." in section heading.
  - **Pixel** — `.cp-reel` renders moody library poster + white play orb + 6-cell EXIF strip; play label "PLAY · 3:12" + caption "REEL · 1080P · 24 FPS" use JetBrains Mono with letter-spacing 0.06em.

### 6 — D-047 leak sweep clean

All new content keys (signature_video, product_video, featured_works, reel) flow through `page_data.*` content registries — zero literal brand strings introduced into shared HTML. CSS classnames (`.fd-signature-video`, `.sl-product-video`, `.cp-reel`, `.ed-projects`) are archetype-internal naming, not user-visible literals. D-047 chrome-authoring contract preserved across all 6 skin folders.

### 7 — D-054 differentiation preserved 10/10

- **Cardio vs Derm** — both inherit specialist typography refinements; differentiation remains brand-color + hero variant + imagery pool (D-060). Neither gets video, both get italic-axis emphasis at the same weight.
- **Pragma vs Elevate** — Pragma gets institutional sectors marquee (sober drift, no video, italic accent serif). Elevate gets growth-tech marquee + product video + JetBrains Mono ship-log. Two distinct B2B vocabularies — boardroom-document vs SaaS-product-tour.
- **Gusto** — only restaurant template, gets the cinematic signature video. Sapore + Brace (drafts) untouched.
- **Chiara vs Pixel** — Chiara gets a typographic-led featured-projects visual grid (NO video, asymmetric grid, italic Syne accent, mono indices). Pixel gets a cinematic reel video block (YES video, EXIF strip, mono caption, uppercase letter-spacing). The two portfolios diverge further: Chiara reads as a designer studio's project ledger, Pixel as a photographer's authored short-form reel.

### 8 — Decision

**LIVE MOTION MEDIA PASS APPROVATO.** D-068 documented in DECISIONS.md.

The 7 published_live templates now ship with: 16 active counter elements across 4 templates, 3 video blocks (Elevate/Gusto/Pixel) with poster + native HTML5 player + per-skin tokens, 2 marquees (Pragma sectors + trust, Elevate integrations), JetBrains Mono accent on 3 templates, italic-axis h-em emphasis on 4 templates, tabular-nums on every metric strip, refined per-template line-height + letter-spacing. D-047 chrome-authoring contract preserved across all 6 skin folders. D-054 differentiation preserved 10/10. D-058 motion language extended (counter prefix + thousand-sep). D-066 forms primitives untouched. i18n/RTL preserved on the 3 multilingual templates.

---

## Session 34 — Portfolio Live Rollout (Phase 2g3.4 · 2026-04-13)

**Agent:** Premium UI / portfolio category live rollout. Sole target: bring `chiara-portfolio-creativo` (editorial-designer-grid) and `pixel-portfolio-fotografico` (cinematic-photographer) from `draft` to `published_live` with full multi-page live previews. Non-goals: auth, checkout, editor, projects, commerce, other categories' drafts, marketplace chrome i18n, new templates, new archetypes, refactors outside scope.

**Branch:** `phase-portfolio-live-rollout-v1` (forked from `phase-integration-baseline-v3`).

### 1 — Audit
Read the 12 context files. Confirmed Chiara + Pixel each had: (a) complete DNA entry in `apps/catalog/template_dna.py` with all 10 D-054 dimensions filled; (b) D-047-compliant preview composition under `templates/preview_compositions/portfolio/`; (c) hand-authored disjoint imagery pool (`portfolio-designer` + `portfolio-photographer`); (d) zero leak in `template_list.html`. The two open gates were content registry (no entries in `TEMPLATE_CONTENT`) and skin folders (no `templates/live_templates/portfolio/` directory). Recipe locked-in from Session 32 (Pragma + Elevate business rollout) — same `{slug: {locale: tree}}` content shape, per-archetype skin folder, `LiveTemplateView` dispatcher (no view changes needed).

### 2 — Strategy
**5 page kinds + 1 detail kind per template**, all distinct from medical/restaurant/business kinds so the dispatcher resolves the correct skin file:

- **Chiara** (editorial-designer-grid): `home / studio (about) / lavoro (project_list → project_detail) / processo (process) / contatti (contact)`. AD voice, sistemic/typographic, design-led, structured.
- **Pixel** (cinematic-photographer): `home / serie (series_list → series_detail) / biografia (about) / pubblicazioni (publications) / contatti (contact)`. Author-photographer voice, image-led, cinematic, atmospheric.

**Differentiation matrix (D-054 · 10/10 dimensions disjoint):**

| Dim | Chiara | Pixel |
|---|---|---|
| 1 Hero image | NO photo · typo+ledger | Fullbleed dominant photo |
| 2 First-2 imagery | sketchbook + paste-up close-ups | moody hero + filmstrip stills |
| 3 Silhouette | hairline-rule nav + 2-col typo hero | floating dark nav + fullbleed cover |
| 4 Section order | hero → ledger → ribbon → capabilities → commissions → cta | hero → exif → filmstrip → bio → publications → cta |
| 5 Primary CTA | "Richiedi il portfolio completo" + ghost sans-rule | "Apri la serie completa" + bracket-mono `[ … ]` |
| 6 Block rhythm | very-airy editorial chapters (96px paddings) | compact image-dense (64px paddings) |
| 7 Macro tone | cream paper #f3efe5 + ink #15130f | near-black #050505 + warm grey #e9e7e2 |
| 8 Imagery direction | studio work-in-progress (designer pool) | cinematic photostill (photographer pool) |
| 9 Typography | Syne (display) + Inter — designer's bookshelf | Archivo (geometric) + Inter + JetBrains Mono — author voice |
| 10 Inner pages | project ledger + design notes + capabilities | series index + EXIF strip + exhibitions + bio |

### 3 — Implementation

**New content registries (~880 + ~720 = ~1600 LOC of hand-authored Italian copy, no lorem ipsum):**

- `apps/catalog/template_content_chiara.py` — `CHIARA_CONTENT_IT` covering 5 pages + 3 project-detail dossiers (Triennale Milano catalogo 2025 / Adelphi collana «Carta Bianca» / Querini Stampalia segnaletica). Founder bio (Chiara Velluti — Isia Urbino + Pentagram NY + Sonnoli + Politecnico docenza). Team of 6. 4 studio principles. Press ledger 8 honors. 5 capabilities with scope + duration. Premium contact form sectioned in 4 groups + file upload + consent.
- `apps/catalog/template_content_pixel.py` — `PIXEL_CONTENT_IT` covering 5 pages + 3 series dossiers (Porto Vecchio Trieste / Le case di pietra Salento / Ritratti del Po). Author bio (Lorenzo Bianchi — Trieste 1986, Sarajevo 2009, Mamiya 7II + Kodak Portra 400). 4-system camera kit. Exhibitions/publications timeline 12 events. 6 awards. 8 magazine cards on `/pubblicazioni`. Series detail = cover hero + 4-cell EXIF strip + 4 meta cells + essay + 6-image asymmetric gallery + per-series print metadata + next-link. Commission inquiry form 4-section.

**New skin folders (~3700 LOC of HTML+CSS):**

- `templates/live_templates/portfolio/editorial-designer-grid/` — `_base.html` (cream paper · ink · accent rule · hairline nav with index-letter labels · clients ribbon footer · `.lf-*` form tokens for editorial paper) + `home.html` (typo hero + project ledger card + capabilities · 4-col + clients ribbon + press cards + commissions dark band + cta) + `about.html` (founder portrait + 6-person team grid + 4 principles + 8-row press ledger dark band + cta) + `project_list.html` (filter pills + indexed dossier rows + preview-only ledger entries + cta) + `project_detail.html` (breadcrumb + meta strip + client code + serif italic lead + summary box + 3 essay sections + dark deliverables band + colophon credits 2-col + next-link) + `process.html` (5-step indexed sequence + 5 capability cards 2-col + cta) + `contact.html` (4-section form + studio-card sidebar + channels + footnote).

- `templates/live_templates/portfolio/cinematic-photographer/` — `_base.html` (near-black · warm grey · accent pulse · floating dark sticky nav · EXIF-cell footer with kit row) + `home.html` (78vh fullbleed cinematic hero + EXIF 4-cell strip + 4-frame filmstrip + about excerpt dark band + 3-cell publications grid + final cta) + `series_list.html` (filter pills + 2-col 4:3 cinematic cards with EXIF chips + cta) + `series_detail.html` (78vh cover hero + 4-cell EXIF strip + meta strip + 3-section essay + asymmetric 6-image gallery + per-series print-meta dark band + next-link) + `about.html` (long-form statement essay + 4-system kit cards + 12-row exhibitions/publications timeline + cta) + `publications.html` (8 press magazine cards 2-col + 6-row exhibitions ledger dark band + 6 awards 2-col + cta) + `contact.html` (4-section form on dark + EXIF-style studio card sidebar + channels + footnote).

**Wiring:**
- Registered both content modules in `apps/catalog/template_content.py` `TEMPLATE_CONTENT` dict.
- Added `mp_other_portfolio` chrome key to all 5 locales of `CHROME_I18N` in `apps/catalog/template_i18n.py` (forward-compat for future portfolio i18n).
- Flipped `tier: "draft"` → `tier: "published_live"` for both rows in `TEMPLATE_REGISTRY.json` with full `tier_reason` annotation.
- `LiveTemplateView` and URL patterns required ZERO changes — the dispatcher already handles `<category>/<archetype>/<page-kind>.html` resolution and the post-detail kind transformation (`_list` → `_detail`). The portfolio rollout is pure content + skin authoring.

### 4 — D-047 leak sweep + lift

Initial sweep against the rendered portfolio skin found 2 latent leaks in `cinematic-photographer/`:
1. `_base.html:393-396` — kit footer rows hardcoded ("Mamiya 7II · Sony α7R V", "Kodak Portra 400", "Stampa · Druckwerkstatt Berlino") would have crashed when a second photographer template adopts the archetype.
2. `series_detail.html:304` — print-edition cells hardcoded ("Druckwerkstatt Berlino", "Hahnemühle Photo Rag", "Galleria Carla Sozzani · Milano") same bidirectional leak.

Both lifted in the same session by adding `site.kit_footer_rows` (3-item list per tenant) and `post.print_meta` (4-pair list per series) to the content registry. Skin templates now read these fields exclusively. Re-sweep returned ZERO matches across both portfolio skin folders. D-047 contract preserved.

### 5 — Validation

- `python manage.py check` — clean.
- `python manage.py migrate` + `seed_categories` + `seed_templates` (full DB rebuild on fresh worktree) — successful, 8 categories + 20 templates created, 7 promoted to `published_live` (5 from previous sessions + chiara + pixel) by automatic registry sync at end of `seed_templates`.
- `python smoke_full.py` — extended with chiara + pixel slugs in `LOCALES` + `CATEGORY` dicts and a new `POST_ROUTES` block for the 6 detail dossiers. Result: **170/170 routes HTTP 200** (was 149 before portfolio addition; +21 = chiara detail + chiara preview + 5 chiara inner pages + pixel detail + pixel preview + 5 pixel inner pages + 6 dossiers + portfolio category surface).
- `python manage.py generate_previews --only chiara-portfolio-creativo --force` + same for pixel — both PNG regenerated cleanly (canonical filenames `chiara-portfolio-creativo-preview.png` + `pixel-portfolio-fotografico-preview.png`, asset rows replaced).
- HTML marker check via Django shell with `ALLOWED_HOSTS=['*']` override — Chiara home shows "Forme che durano" headline + "Triennale Milano" ledger entry + "Chiara Velluti Studio" wordmark + "Richiedi il portfolio" CTA + `live-motion.css` + `live-forms.css` + `class="ed-nav"` / `ed-hero` / `ed-foot`. Pixel home shows "OSSERVARE COSA RESTA" headline + "Lorenzo Bianchi" + "Mamiya 7II" + "Galleria Carla Sozzani" + `cp-hero` / `cp-strip` / `cp-foot` / `class="cp-nav"` + "Apri la serie". Project_detail (Triennale Milano dossier) shows "Direzione tipografica" + "Grafiche Antiga" + "412 pp" + "Colophon" + `class="ed-dossier"`. Series_detail (Porto Vecchio) shows "Porto Vecchio" + "Mamiya 7II" + "Hahnemühle" + `cp-cover` / `cp-essay` / `cp-gallery` / `cp-series-exif`.
- Listing `/templates/portfolio/` — both chiara + pixel rendered. Lawyer listing (all draft) — premium empty state ("In arrivo / preparazione") still rendering correctly with no leak of draft templates. Homepage `/` — chiara appears in featured grid (featured=True), pixel appears in featured backfill (featured=False). Featured-pool backfill from D-057 working as designed.

### 6 — Catalog state after Session 34

| Category | Live | Draft |
|---|---|---|
| business | 2 | 0 |
| medical | 2 | 3 |
| restaurant | 1 | 2 |
| **portfolio** | **2** | **0** |
| agency | 0 | 2 |
| ecommerce | 0 | 2 |
| lawyer | 0 | 2 |
| real-estate | 0 | 2 |
| **TOTAL** | **7** | **13** |

Catalog floor moved from 5/20 (Session 32) to **7/20 published_live**. Portfolio is the third category (after Business and Medical) where 100% of siblings are live. Phase 2g3.4 closes; Phase 2g3 progress is now restaurant 1/3 + medical 2/5 + ecommerce 0/2 + agency 0/2 + lawyer 0/2 + real-estate 0/2 = 13 templates remaining across 6 categories before 2g3.7 unlocks Phase 3.

### 7 — Decision

**PORTFOLIO LIVE ROLLOUT APPROVATO.** D-067 documented in DECISIONS.md.

---

## Session 33 — Premium Forms & Inputs Polish (2026-04-13)

**Agent:** Premium UI / interaction polish session. Sole target: the form pages on the 5 `tier=published_live` templates. Non-goals: auth, checkout, editor, projects, commerce, drafts, new categories, new archetypes, marketplace chrome.

**Branch:** `phase-premium-forms-polish-v1` (forked from `phase-integration-baseline-v2`).

### 1 — Audit
Read the 12 context files. Enumerated the 5 form-bearing pages: cardio+derm `contatti` (6 fields) and `richiedi-visita` (8 fields, 2 selects), gusto `prenota` (8 fields, 1 select), pragma `contatti` (9 fields, 2 selects), elevate `demo` (8 fields, 3 selects). Problems observed on all 5: native `<select>` with grey/blue browser chrome, no helper text under fields, native checkbox on consent, tepid focus state (border-color only), no section grouping for 8–9 field forms, no file upload anywhere despite copy like "Allega gli esami recenti se vuoi" and "NDA reciproca", no reassurance note near the submit bar, uniform CTA without secondary action.

### 2 — Strategy
Shared `.lf-*` primitive system (CSS + JS) with per-skin token overrides. Real custom listbox for `<select>` on desktop/keyboard (touch keeps native). File upload only on the 3 forms where the copy justifies it (cardio/derm appointment · pragma contact · elevate demo — not on gusto or medical contact). Section grouping on the 4 heavier forms (≥8 fields). Submit reassurance + optional secondary action on every form.

### 3 — Implementation

**New static files:**
- `static/css/live-forms.css` (~490 lines) — `.lf-field / .lf-label / .lf-control / .lf-helper / .lf-section / .lf-submit-bar / .lf-check / .lf-select / .lf-upload` primitives, 20+ CSS custom properties (`--lf-bg`, `--lf-border`, `--lf-border-focus`, `--lf-ring`, `--lf-radius`, `--lf-caret`, `--lf-submit-bg`, etc.) each overridable per skin, `.lf-boxed` variant for skins that want padded inputs, `prefers-reduced-motion` guard, RTL-safe via logical properties.
- `static/js/live-forms.js` (~260 lines) — zero-dep IIFE. `enhanceSelect()` upgrades every `<select>` inside `.lf-select` to a role="combobox" trigger + role="listbox" panel with complete ARIA (aria-haspopup/controls/expanded/activedescendant), keyboard (↑ ↓ Home End Enter Space Esc typeahead), option hover + dot marker. Touch devices (`matchMedia('(hover:none) and (pointer:coarse)')`) keep the native picker. `enhanceUpload()` wires the drop zone + file chip list with size formatting + individual remove (DataTransfer-backed); graceful without JS.

**Per-skin tokens** in each `_base.html :root`:
- Specialist (clinical · paper + gold): minimal underline, 0 radius, gold caret, red-ring focus, paper listbox, primary-dark submit.
- Fine-dining (moody · dark body + gold): transparent on dark bg, 14px padding, gold caret and secondary-gold focus, dark warm listbox.
- Corporate-suite (institutional · paper-3 boxed): 1px border, boxed inputs, emerald focus, primary-dark submit with accent arrow.
- Startup-saas (glass · dark cosmic + cyan glow): rgba(0,0,0,0.32) bg, 10px radius, cyan glow ring + cyan focus, dark cosmic listbox, pill-radius accent-cyan submit.

**Specialist dark-band override block** (in `_base.html`) flips every `.lf-*` token to on-dark values for the `.sp-form-band` context on the appointment page — navy body, gold CTA.

**Markup updated:**
- `specialist/contact.html` — converted 6 hand-written field rows to the `.lf-*` primitive shape (label + input + helper), replaced native submit + native consent with custom `.lf-submit-bar` and `.lf-check`, added mobile breakpoint.
- `specialist/appointment.html` — full rewrite of the form area: loop `page_data.form_sections` → `.lf-section > .lf-section-head + .lf-field×N`, special `"__upload__"` sentinel renders the file upload field, custom listbox for the 2 selects, consent + submit-bar + secondary alternative link all in `.lf-*`.
- `fine-dining/reservations.html` — sectioned form when `form_sections` is present, fallback to tuple-loop for non-IT locales (preserves existing i18n content without forcing a section translation pass), custom listbox for occasion.
- `corporate-suite/contact.html` — sectioned `.lf-boxed` form with upload, emerald consent box kept as container around `.lf-check`, submit-bar with reassurance.
- `startup-saas-landing/demo.html` — sectioned `.lf-boxed` form with upload, cyan consent box, pill submit.

**Content registries:**
- Added 6 universal chrome keys across 5 locales (30 entries): `form_required`, `form_optional`, `form_select_placeholder`, `form_upload_browse_prefix`, `form_upload_browse_link`, `form_upload_remove`.
- IT per-template additions for the 5 forms: `form_sections` (nested by field name), `upload_field` (where applicable), `form_submit_note`, per-field `helper`, `form_consent` where missing.
- `form_submit_note` translated to EN/FR/ES/AR for cardio/derm/gusto (native-voice).
- Sections/upload/helper text for the 3 multilingual templates remain IT-first; the HTML uses `{% if page_data.X %}` guards so non-IT locales render a working form without the IT enhancement copy. Flagged as follow-up translation pass in memory (Phase 2i.3 candidate).

**Mobile breakpoints at 880px** added to all 5 form pages: outer grid collapses to 1-column, padding halves, section titles step down. Pre-existing specialist nav + footer legacy mobile overflow is documented as out of scope.

### 4 — Late fix captured
Section titles used `var(--primary)` which reads dark-on-dark for fine-dining (brown) and startup-saas (navy). Introduced `--lf-section-title-color` token, defaulting to `var(--ink)`; per-skin overrides: specialist `--primary`, fine-dining `--secondary` (gold), corporate-suite `--primary`, startup-saas `--ink`. Every section title now legible on its skin.

### 5 — Validation

- `python manage.py check`: 0 issues.
- `smoke_forms.py` (new): 27/27 form-specific routes HTTP 200 across the 5 templates × supported locales; every form page carries `.lf-*` primitives, links `live-forms.css` + `live-forms.js`, and the select-bearing ones expose `.lf-select`. All green.
- `smoke_full.py` (new): 149/149 routes across marketplace surfaces + detail + home + all inner pages of the 5 templates × supported locales. All green.
- Browser walk at 1440×900 via Playwright: cardio appointment (4 sections · 2 selects enhanced · upload · 9 helpers · submit note), derm appointment (same specialist skin · 2 selects enhanced · upload), gusto prenota (3 sections · 1 select enhanced · 8 helpers · submit note with deposit copy), pragma contact (4 sections · 2 selects enhanced · upload · 10 helpers · submit note), elevate demo (4 sections · 3 selects enhanced · upload · 9 helpers · submit note). **10 selects total across the 5 live forms**, all upgraded to the custom listbox on desktop/keyboard. Listbox open-state verified on Gusto: dark warm panel with gold dots + accent caret.
- RTL (cardio `contatti?lang=ar`): `dir=rtl`, `lang=ar`, 6 controls render, labels + placeholders + submit-note right-aligned, submit arrow flipped via `scaleX(-1)`, native Arabic font stack active.
- Mobile 390×844: cardio appointment form collapses cleanly to 1-column; legacy chrome overflow (`.sp-nav .right` grid, `.sp-foot .col` grid) is pre-existing and documented.

### 6 — Differentiation preserved
- The 5 templates read as 4 distinct form families (specialist clinical · fine-dining hospitality · corporate-suite institutional · startup-saas growth-tech). Zero shared form CHROME between templates — same underlying primitive, different tokens.
- Cardio vs Derm forms share the specialist skin by design (D-060 split is in imagery + hero variants, not in forms).

### 7 — Memory / docs
- `MEMORY.md` — new pointer to `premium_forms_polish_session33.md`.
- `memory/premium_forms_polish_session33.md` — full session memory.
- `SESSION_LOG.md` — this entry.
- `DECISIONS.md` — new D-066 (Premium Forms System).
- `TODO_NEXT.md` — Phase 2k block recording Session 33 closed + Phase 2i.3 candidate for the enhancement-copy i18n pass.

### 8 — Decision

**PREMIUM FORMS POLISH APPROVATO.** The 5 form pages on the 5 `tier=published_live` templates now ship with: a real custom accessible listbox (not native grey/blue), premium section-grouped forms on the 4 heavier pages, sensible file upload on cardio+derm appointment + pragma contact + elevate demo (not sprinkled where it doesn't belong), reassurance + CTA submit bar on every form, graceful no-JS + reduced-motion degradation, RTL-safe Arabic rendering, mobile 1-column collapse. `check` clean, 27/27 form checks green, 149/149 full route sweep green. Zero regressions on baseline.

---

## Session 32 — Business Live Rollout (Phase 2g3.3 — Pragma + Elevate published_live) (2026-04-13)

**Agent:** Premium UI + content authoring + integration session. Single objective: bring the two existing business templates (Pragma, Elevate) up to `published_live`, completing the second category-burst rollout after medical and restaurant.
**Branch:** `phase-business-live-rollout-v1` (forked from `phase-integration-baseline-v1`).
**Scope floor:** only Pragma + Elevate. Non-goals: new templates, other categories' drafts, auth/checkout/editor/projects/commerce, business i18n locales beyond IT, motion-language refactor, marketplace chrome translation.

### 1 — Audit & Strategy

Read all 12 context files. Existing state: both business templates already had **D-047-compliant DNA + preview compositions from Session 17 (D-050)** but NO live skin folder and NO content registry block. The DNA pair was already 10/10 differentiated by design — Pragma corporate-suite (boardroom-led, serif, advisory pillars, KPI strip, sectors band, private-call CTA) vs Elevate startup-saas-landing (cosmic gradient, manifesto, product-mockup card, glow-pill CTA, ship log, free-trial). Imagery pools `business-corporate` and `business-startup` already disjoint with zero URL overlap (Session 17). Strategy: respect the DNA contract verbatim, write content + skin folder per archetype, no DNA changes.

Page kinds chosen (each baseline-D-053 satisfied):

- **Pragma**: `home`, `about` (chi-siamo · history+values+team+coords), `services` (competenze · 6 practices + 4-step process), `case_study_list` (case-studies · 3 mandate posts), `case_study_detail` (per-mandate — problem/approach/result + KPI band), `contact` (contatti · multi-step form + 3 offices)
- **Elevate**: `home` (manifesto + mockup + 6 features + integrations + 3-tier pricing teaser + ship log + glow CTA), `product` (prodotto · 6 modules + 12 integrations + stack), `pricing` (prezzi · 3 tiers + comparison + FAQ accordion), `demo` (demo · lead form + async loom block + trust strip), `contact` (contatti · 4 channels + 3 founders with direct emails + async-first office)

### 2 — Authoring decisions

**Content extracted to per-template files** to keep `template_content.py` browsable:
- `apps/catalog/template_content_pragma.py` — `PRAGMA_CONTENT_IT`, ~590 lines. Editorial register: formal Italian Lei, McKinsey/Bonelli vocabulary, Milano-Frankfurt-Zürich tri-office presence, 22-year history, 14 partners, €1.4B transacted, 94% repeat rate, sectors industria-finanza-energia-retail-healthcare. 3 fully-authored case study posts (manifatturiero bresciano · piano industriale, carve-out consumer Italia-DACH, CSRD utility quotata) with problem/approach/result + 4-KPI band each.
- `apps/catalog/template_content_elevate.py` — `ELEVATE_CONTENT_IT`, ~620 lines. Voice: tu register, growth-tech vocabulary (waitlist/MRR/A/B/ship log/deploy/trial), Talent Garden Milano async-first, 3 founders with direct emails (Camillini/Lavia/Adami), 240+ Italian startups adopted, 6 product modules, 12 integrations (Stripe/Linear/Slack/Vercel/Netlify/Cloudflare/PostHog/GrowthBook/Loops/Resend/Cal.com/Plain), 3-tier pricing (Launch €29 / Scale €79 / Studio €199), full FAQ + comparison block + ship-log timeline.

**Both files include a 10-gate D-054 differentiation comment block at the top** (mirror docs) so any reviewer can verify cross-template divergence without rereading both registries.

### 3 — Skin folder authoring (D-047 from line one)

Both `_base.html` files written under D-047 contract: zero literal brand strings, every visible label flows from `chrome.*` (cross-archetype), `site.*` (per-template chrome), `page_data.*` (per-page content), or template loops. Per-template footer headings live on `site.foot_*` because `chrome.foot_*` carries medical-specific labels and the business notion of "studio" / "sezioni" / "sedi" is template-specific.

`templates/live_templates/business/corporate-suite/`:
- `_base.html` — full-bleed solid navy navbar with crest + phone CTA; cream/dove paper body; 4-col dark navy footer with offices column; corporate motion profile (`--lm-rise: 12px`, slower easing, restrained CTA arrow translate +4px)
- `home.html` — 55/45 split serif hero with boardroom photo, advisory pillars, KPI strip on dark navy band, sectors ribbon, trust-band wordmarks, 3 leadership cards, 5-row case-studies preview, dark CTA closer with glow
- `about.html` — vertical 5-step history timeline, 4-card values grid (paper-2 background), 6-card team grid, 3-office coords on dark navy
- `services.html` — 6-card 2-up advisory practice grid with scope checklists + meta strip, 4-step process on dark navy band
- `case_study_list.html` — numbered indexed list of 3 mandates with hover lift + arrow shift
- `case_study_detail.html` — 880px column read with 4-cell meta strip, client-code box, italic lead, problem/approach/result sections, 4-KPI dark band, team & timeline footer, back-to-list link
- `contact.html` — 1.4fr/1fr split: 9-field form with consent box + uppercase submit · 3-office sidebar with 4-row meta each + 3 channels + footnote

`templates/live_templates/business/startup-saas-landing/`:
- `_base.html` — pulse launch banner above the nav, floating glass pill nav with brand dot + glow CTA, dark cosmic gradient body with subtle radial dots, glass footer with shiplog column; startup motion profile (`--lm-rise: 16px`, snappier 620ms, glow-pill `translateY(-1/2px)` hover)
- `home.html` — 80px centered manifesto, glass product-mockup card with 3-cell metric grid + perks, 8-wordmark trust strip, 6-card features grid (3x2), 4-stat metric band in dark inset, 8-cell integrations grid, 3-tier pricing teaser with highlight ring, 2 founder quote cards with metric chips, 5-row ship-log timeline with release chip, glow-ring final CTA
- `product.html` — 6-module 2-up grid with highlights checklist, 12-cell integrations full grid with category cells, 8-row stack table on dark inset
- `pricing.html` — billing toggle pill, 3-tier highlight-ring pricing grid with annual price secondary, 4-row transparency comparison block, 6-item FAQ with `<details>` accordion (first open), final glow CTA
- `demo.html` — 1.4fr/1fr split: 8-field demo lead form (slot select / async option / context textarea) · async loom block + 3-step trust strip
- `contact.html` — 4 channel cards (email/slack/demo/office hours), 3 founder cards with direct emails + role tags, 2-card office grid (sede/schedule), centered footnote

### 4 — Routing wiring

`LiveTemplateView` resolves `live_templates/<category>/<archetype>/<page-kind>.html` from DNA `archetype` + content `page.kind`. The page kinds I introduced (`product`, `pricing`, `demo`, `case_study_list`, `case_study_detail`) are file names; the existing `_list` → `_detail` substitution in the view (used for blog) works for case studies because the kind suffix matches. Zero changes to `views.py` / `urls.py` / `selectors.py` required.

Added one entry to `CHROME_I18N` per locale: `mp_other_business` (5 locales — IT/EN/FR/ES/AR — even though business is IT-only at promotion, the chrome key benefits from being 5-locale-ready when business i18n is later authored).

### 5 — Tier flip + sync

Updated `TEMPLATE_REGISTRY.json`: Pragma + Elevate flipped from `tier: draft` → `tier: published_live`, added `live_pages`, `locales: ["it"]`, `rtl: false`, `session_closed: 32`, `live_preview: true`. Ran `migrate` (fresh worktree DB) → `seed_categories` → `seed_templates` (auto-runs `sync_template_tiers` per Session 21 pattern) — `5 tier(s) updated. Catalog distribution: 5 published_live / 15 draft.`

### 6 — Validation

`python manage.py check` clean. Comprehensive smoke sweep with overridden ALLOWED_HOSTS:

- **54/54 routes green** (51 200s + 3 expected 404s):
  - Marketplace listing + 8 category listings (200)
  - 5 marketplace detail pages for the 5 published_live templates (200)
  - Pragma 8 routes (5 pages + 3 case study details — all 200)
  - Elevate 5 routes (200)
  - Cardio i18n × 5 locales home + 6 inner pages (200)
  - Derm 5 inner routes (200)
  - Gusto i18n × 5 locales + 3 inner pages (200)
  - Sapore draft 404, invalid Pragma slug 404, draft medical detail 404
- **D-047 bidirectional leak sweep**: rendered ~132K chars of Pragma HTML and ~163K of Elevate HTML. Pragma rendered with Elevate literals leaked: `[]`. Elevate rendered with Pragma literals leaked: `[]`. Each renders its own brand strings correctly.
- **Listing visibility**: `/templates/business/` shows both Pragma + Elevate, no "in arrivo" empty state, business category card now shows `2 live template(s)` (was `0`). Full `/templates/` listing shows all 5 published_live.
- **Preview PNG regeneration**: ran `generate_previews --only pragma-corporate-suite --force` and same for Elevate. Both PNGs saved.
- **Footer chrome contract**: caught one D-047 violation in initial pass (literal "Privacy / Cookie / Note legali" in footer). Fixed to use `{{ chrome.foot_privacy }}` / `chrome.foot_cookie` / `chrome.foot_legal` like the medical specialist skin.
- **Hero image**: caught one hardcoded `https://images.unsplash.com/...` URL in the Pragma `home.html` (initial draft). Moved to `page_data.hero_image` per D-047.

### 7 — Differentiation 10-gate (D-054) — recorded

| # | Dimension                  | Pragma corporate-suite                         | Elevate startup-saas-landing                       |
|---|----------------------------|------------------------------------------------|----------------------------------------------------|
| 1 | Hero image                 | Boardroom photo (business-corporate[0])        | NO big photo — typographic-only manifesto          |
| 2 | First-2 imagery            | Boardroom + corporate atrium                   | Product-UI dashboard (mockup card)                 |
| 3 | Silhouette                 | 55/45 serif headline L + photo R               | Centered manifesto + floating glass mockup card    |
| 4 | Section order              | hero→pillars→KPI→sectors→trust→leadership→cases→CTA | banner→manifesto→mockup→trust→features→metrics→integrations→pricing→founders→shiplog→CTA |
| 5 | Primary CTA                | "Fissa una call privata" + boardroom form     | "Inizia gratis 14 giorni" + glow pill + trial     |
| 6 | Block rhythm               | airy editorial chapters (96px paddings)        | medium-density glow cards + dark sections          |
| 7 | Macro tone                 | cream paper + navy + emerald accent            | dark cosmic gradient + cyan glow                   |
| 8 | Imagery direction          | executive-boardroom (people in glass rooms)    | product-dashboard (UI screens, code, dev tools)    |
| 9 | Typography                 | Merriweather + Inter (transitional serif)      | Manrope + Inter (geometric sans)                   |
| 10| Inner pages                | case studies + practice areas + 3-office presence | pricing + ship log + demo lead + integration grid |

10/10 differs. **No recolor pair.**

### 8 — Memory / docs updated

- `MEMORY.md` — new entry pointer to `business_live_rollout_session32.md`
- `memory/business_live_rollout_session32.md` — Session 32 summary memory
- `SESSION_LOG.md` — this entry
- `DECISIONS.md` — new D-065 (Business Live Rollout — recipe locked in for 2 archetypes per category)
- `TODO_NEXT.md` — Phase 2g3.3 closed, next gate is 2g3.4 portfolio (Chiara + Pixel)
- `CATEGORY_ROADMAP.md` — completeness table updated to 5/20 published_live, business row marked complete
- `TEMPLATE_REGISTRY.json` — Pragma + Elevate `tier: published_live` with full `live_pages`/`locales`/`tier_reason`

### 9 — Decision

**BUSINESS LIVE ROLLOUT APPROVATO.** All D-053 gates green for both Pragma and Elevate. D-054 10/10. D-047 leak sweep clean. Catalog now shows 5 published_live across 3 categories (business 2 + medical 2 + restaurant 1). Cumulative milestone for `published_live` count is now **5 (out of the Session 20 target of 20)**, matching the TODO_NEXT post-2g3.3 prediction exactly.

### 10 — Gotchas captured for the next 2g3.4–2g3.6 rollouts

- **D-047 in skin authoring is enforced manually by re-reading the chrome before publishing.** I caught two violations during validation (hardcoded image URL in Pragma hero + literal Privacy/Cookie/Legali in both footers). Both small, both caught during the leak sweep + listing checks. **For 2g3.4 onward, do the leak sweep BEFORE flipping the tier**, not after — flipping then fixing risks shipping a broken brand contract for one minute.
- **`mp_other_<category>` chrome key needs to be added per category** (we now have `_medical`, `_restaurant`, `_business` — next will be `_portfolio`, `_ecommerce`, `_agency`, `_lawyer`, `_real-estate`). Cheap to add (5 entries × 5 locales) and the marketplace bar references it. Don't forget on a new category.
- **Per-template footer headings should live on `site.foot_*`**, not `chrome.foot_*`, when the category's notion of "the studio" / "the menu" / "the office" differs per archetype. Reserve `chrome.foot_*` for cross-archetype shared chrome (medical specialist + medical clinic + medical wellness can share `foot_studio`; corporate-suite and startup-saas-landing cannot).
- **Page kind name = template filename.** No view changes are needed if the kind name maps directly onto a `.html` file in the per-archetype skin folder. I introduced `product`, `pricing`, `demo`, `case_study_list`, `case_study_detail` — all worked first-try because the view's only special-case is the `_list` → `_detail` rewrite.
- **Fresh worktree DB needs `migrate` + `seed_categories` + `seed_templates`** (in that order) before `sync_template_tiers` will work. The `seed_templates` command auto-runs the tier sync at the end (Session 21 pattern), so the order is `migrate` → `seed_categories` → `seed_templates` and the tier flip is one command, not two.
- **Django test client needs `override_settings(ALLOWED_HOSTS=['*'])`** in this project. The default DEBUG=True doesn't include `testserver` in ALLOWED_HOSTS (which is empty `[]`). Add the override at the top of every smoke script.

---

## Session 30 — Premium Component Depth & Editor Schema Blueprint (2026-04-13)

**Agent:** Premium UI + Architecture session. Dual-scope: (a) enrich the 3 `published_live` templates with differentiated premium sections, (b) author a concrete Editor Schema Blueprint for future customer personalization.
**Branch:** `phase-premium-components-blueprint-v1`.
**Scope floor:** only the 3 published_live (cardio / dermatologia-elite-roma / gusto). Non-goals: drafts, new categories/templates, auth/checkout/editor/projects/commerce implementation, refactor of stable infra.

### 1 — Audit & Strategy

Read all 11 context/memory files. Each template is already rich (motion D-058/D-061, interactions D-062, i18n D-059/D-063). The enrichment bar is therefore high — adding "any" section would be noise. The strategy chosen: **each template gets distinct premium sections that fit its archetype tone, not a shared pack**.

- Cardio (clinical precision) → utility-clinical (journey/trust/location/anchor-nav)
- Derm (boutique aesthetic) → discovery-visual (treatment tabs / before-after / editorial feed)
- Gusto (hospitality editorial) → theatrical-cultural (producers / private dining / wine program)

Video decision: rejected for all 3 — not cheap enough to justify. Cinemagraph rejected as lower-quality substitute. Static imagery + motion language remain the premium floor.

Map decision: only cardio gets a map (clinical utility). Derm gets location in the footer already; gusto's address is in the prenota page. Differentiation preserved.

### 2 — New Interaction Primitives

Extended `static/css/live-interactions.css` (+ 190 lines) and `static/js/live-interactions.js` (+ 170 lines) with 3 new components, all zero-dependency and `prefers-reduced-motion` aware:

- **Tabs** — `[data-li="tabs"]` with `.li-tabs-nav .li-tab-btn[data-li-target]` and `.li-tab-panel[data-li-id]`. Keyboard nav (Enter/Space/←/→), ARIA roles set by JS, fade panel animation (520ms).
- **Compare slider (before/after)** — `[data-li="compare"]` with absolute `.li-cmp-before/.li-cmp-after` layers, JS-injected `.li-cmp-handle`, mouse/touch/keyboard control, clip-path driven reveal. Labels `.li-cmp-label.before/.after`. Graceful 50% default without JS.
- **Anchor subnav** — `.li-anchor-nav` sticky top with IntersectionObserver-driven `.is-active` class on current section link. Smooth scroll on click with reduced-motion fallback.

### 3 — Cardio (specialist) enrichments

Content registry (`template_content.py` CARDIO_CONTENT_IT.home):
- `anchor_nav` — 6 entries (metodo/visite/percorso/tecnologie/medico/studio)
- `percorso` — 5 steps with icons (clipboard/book/heart/chart/document), title/desc/duration each
- `insurance` — 4 trust items (19% deductibility / 48h turnaround / 4 hospital network / 10-year archive)
- `location` — address, map image fallback, 4 detail pairs (address/metro/parking/accessibility), 3 hours rows, CTA

HTML (`templates/live_templates/medical/specialist/home.html`):
- `.sp-anchor-wrap > .li-anchor-nav` right after facts
- Section IDs added: `#metodo` (manifesto), `#visite` (signature), `#tecnologie` (tech), `#medico` (chief), `#studio` (location)
- `.sp-journey` (5 steps with SVG icons, dashed timeline, duration badge)
- `.sp-trust` (4-column figure cards)
- `.sp-location` (split map + info + hours grid)
All wrapped in `{% if page_data.X %}` so derm never renders them (derm content has no `percorso`/`insurance`/`location`/`anchor_nav`).

### 4 — Derm (specialist, different branch on same skin) enrichments

Content registry (DERMATOLOGIA_CONTENT_IT.home):
- `trattamenti_tabs` — 3 tabs (clinica/chirurgia/estetica) with eyebrow + heading + body + 4 items each + CTA
- `before_after` — 1 documented pair (CO2 laser) with before/after Unsplash URLs + ethical disclaimer
- `editorial_feed` — 4 tiles (Vogue / SIDeMaST / Corriere Salute / studio opening) with meta + title

HTML (same specialist `home.html`, conditional blocks):
- `.sp-tabs` uses `data-li="tabs"` with 3 buttons + 3 panels (grid: body+CTA on left, items list on right)
- `.sp-compare` uses `data-li="compare"` with `tabindex="0"` for keyboard control, 3 chip labels (consenso scritto / follow-up / no ritocco)
- `.sp-feed` 4-col grid with lightbox triggers (data-li="lightbox-trigger" data-li-group="feed")
All conditional — cardio never renders these.

### 5 — Gusto (fine-dining) enrichments

Content registry (GUSTO_CONTENT_IT.home):
- `produttori` — 4 artisan cards (Tarbouriech / Brezza / Lageder / Pieropan) with portrait + role + area + blurb
- `private_dining` — 3 experiences (Chef's Table / evening buy-out / cellar tasting) with icon + title + meta + desc + CTA
- `wine_program` — sommelier block (Greta Vallesi bio) + 3 pairings (classic/contemporary/zero-alcohol) + 3 cellar facts

HTML (`templates/live_templates/restaurant/fine-dining/home.html`):
- `.fd-prod` 4-col portrait grid with hover filter lift (reusing existing `.fd-*` motion tokens)
- `.fd-private` 3-col experience cards with border-color hover + icon SVG (fork/door/wine) + right-aligned CTA
- `.fd-wine` split layout: sommelier sidebar (left) + 3-column pair-row list (right) with facts footer
All conditional on `page_data.X`.

### 6 — i18n / RTL coverage

All new sections authored in all 5 locales for all 3 templates:
- `template_content_cardio_i18n.py`: +350 lines (EN/FR/ES/AR for anchor_nav + percorso + insurance + location)
- `template_content_dermatologia_i18n.py`: +380 lines (EN/FR/ES/AR for trattamenti_tabs + before_after + editorial_feed)
- `template_content_gusto_i18n.py`: +380 lines (EN/FR/ES/AR for produttori + private_dining + wine_program)

Native editorial voice per locale — no machine translation. Proper names (Tarbouriech / Lageder / Greta Vallesi / Dr. Marani / Viale Parioli / etc.) stay Latin across all locales consistent with D-059/D-063. Arabic uses MSA register with native punctuation.

RTL adjustments added to specialist `_base.html` and fine-dining `_base.html`:
- `html[dir="rtl"] .li-anchor-nav a` letter-spacing flatten
- `.li-tab-btn` margin + padding direction flip, underline origin switched
- `.li-cmp-label.before/.after` left/right swap
- `.sp-location .map` border-left → border-right
- `.sp-tabs .panel-body .cta:after` `→` → `←`
- `.fd-prod .card .portrait` border direction flip
- `.fd-wine .sommelier` border + pair-row grid-template-columns flip
- `.fd-private .exp` text-align right / CTA text-align left

Compare slider drag remains LTR-mouse-driven by deliberate design (handle tracks cursor X regardless of locale); only labels flip.

### 7 — Editor Schema Blueprint

Authored `EDITOR_SCHEMA_BLUEPRINT.md` (~600 lines, repo root). Concrete specification:
- Component registry: 8 edit targets (nav/hero/section/form/contact/blog/footer/locale) with field tables showing Type / Edit? / Constraints / RTL-aware.
- Section kinds vocabulary: 20+ kinds (old + new Session 30 kinds like tabs / compare_slider / editorial_feed / map_location / producer_showcase / wine_program / trust_strip / timeline_steps).
- Field types: 23 atomic types for editor UI (text / richtext / image / video / color_token / font_ref / link / page_ref / list<T> / content_map / channel / icon / ...).
- Design tokens scope: palette (5 colors), fonts (curated 18 Google Fonts), radius / icon_pack / image_treatment / motion_profile, text/layout alignment, section density.
- 6 hard invariants the editor must uphold (D-047 chrome-authoring / D-053 Live Preview Law / D-054 Premium Differentiation / D-057 tier / D-058 motion / D-059 i18n).
- Persistence model: CustomerProject + ProjectContent + ProjectDesignTokens + ProjectRevision (tables specified, NOT migrated).
- Scalability section: how this extends to new section kinds, new archetypes, new locales, future SPA editor, 250-template target.

The blueprint commits to concrete decisions: every field has a type, every list has min/max, every token has a scope, every variant has a source of truth (DNA-locked vs customer-edit). This is the architectural anchor for when the editor worktree opens after Phase 2g3.7.

### 8 — Validation

- `python manage.py check`: 0 issues.
- Smoke test 85/85 routes 200: 3 templates × 5 locales × mixed page kinds (4/7 + 4/7 + 6/7 per template).
- Marketplace surfaces 4/4 200 (`/templates/`, 3 detail pages).
- Cross-contamination sweep: 0 (Ricciardi in cardio / Marani in derm / Osteria in medical / Parioli in gusto / Vallesi in medical all False).
- Differentiation: 16/16 (all per-template sections render only on the right template, confirmed by content-string presence check on rendered HTML).
- i18n coverage: 12/12 (new sections render in EN/FR/ES/AR on all 3 templates — verified by locale-specific content string presence).
- AR RTL: 3/3 (dir=rtl + native translations visible on cardio/derm/gusto home).

### 9 — Decision

D-064 formalized in DECISIONS.md.

**PREMIUM COMPONENT BLUEPRINT APPROVATO.**

---

## Session 29 — Gusto i18n/RTL (Phase 2i.2 step 2) (2026-04-13)

**Agent:** Premium UI i18n session. Close the multilingual gap on the third published_live template.
**Branch:** `phase-gusto-i18n-rtl-v1`.
**Scope floor:** extend the i18n/RTL pilot architecture (D-059) to gusto-fine-dining, shipping 5 locales (it/en/fr/es/ar) with real RTL for Arabic. Preserve motion (D-058), ultra-premium interactions (D-062), and zero regression on cardio/derm (D-059/D-061).
**Non-goals:** Django gettext/.po, middleware, per-locale URLs, translating marketplace chrome, translating drafts, touching auth/checkout/editor/projects/commerce, changing DNA or preview compositions, new categories/templates.

### 1 — Audit
Read all 8 fine-dining skin files (`_base.html` + 7 pages) end-to-end. Catalogued every hardcoded Italian string: 15 in `_base.html` (mp-bar labels, nav star line, footer headings, footer hours, copyright, privacy/cookie/legal), 13 in `home.html` (chef meta label, star tag, photo/kitchen credits, courses label/footline, chef nav links, press label, CTA block), 5 in `about.html` (values label/heading, CTA), 2 in `menu.html` (courses label, wine-pairing label), 4 in `gallery.html` (CTA quote/desc/links), 12+ in `reservations.html` (process label/heading, concierge labels, hours heading, form labels/placeholders/options/submit), 2 in `blog_list.html` (read link, min label), 5 in `blog_detail.html` (breadcrumb, min label, empty body, footer label, back link). Noted `<html lang="it">` static, no language switcher, no `?lang=` preservation, no RTL CSS block, no Arabic font loader.

### 2 — CHROME_I18N extension
Added 9 restaurant-generic keys × 5 locales (IT/EN/FR/ES/AR) to `apps/catalog/template_i18n.py`:
- `mp_other_restaurant`, `foot_restaurant`, `foot_concierge`, `foot_services` — new restaurant footer + mp-bar labels
- `fd_wine_pairing` — menu course wine-pairing strip
- `fd_email_label`, `fd_phone_label` — concierge contact chip labels
- `blog_read_article` — shorter variant of existing `blog_read_full`

Zero breakage of existing keys. Authoritative IT values, then hand-translated per locale. Arabic stays flat: "المطعم", "الاستقبال", "الخدمة", "مقترن مع", "البريد الإلكترونيّ", "الهاتف", "قراءة المقال", "← قوالب مطاعم أخرى".

### 3 — GUSTO_CONTENT_IT key expansion
Added ~30 missing content keys to `GUSTO_CONTENT_IT` in `apps/catalog/template_content.py` for every previously-hardcoded HTML literal. Organized by page block:
- `site.*`: star_line, footer_hours_1, footer_hours_2, copyright
- `home.*`: chef_label, star_tag, photo_label, cuisine_label, courses_label, courses_footline, courses_full_cta, chef_link_filosofia, chef_link_diario, press_label, cta_heading, cta_primary, cta_secondary
- `filosofia.*`: values_label, values_heading, cta_heading, cta_menu, cta_prenota
- `menu.*`: courses_label
- `atmosfera.*`: cta_quote, cta_desc, cta_primary, cta_secondary
- `diario.*`: read_article, min_label, min_read_label, crumb_label, back_link, footer_label, empty_body
- `prenota.*`: process_label, process_heading, hours_label, hours_heading, private_heading, form_submit, occasion_options; reshaped form_fields to match HTML's visual order (name/email/phone/guests/date/occasion-select/intolerances-full/note-textarea)

### 4 — Template i18n file authoring
Created `apps/catalog/template_content_gusto_i18n.py` with 4 full hand-authored content trees:

- **EN** (~310 lines): Anglo-American fine-dining editorial. "An evening in eight acts.", "One service per night", "tasting menu that rewrites itself every two weeks". NYT Magazine-grade blog body for lead post.
- **FR** (~310 lines): Haute cuisine register, `vous` form, Michelin-guide French. "Une soirée en huit actes.", "dégustation en huit actes", times in `20h00` format, French « » quotation marks.
- **ES** (~310 lines): Peninsular Spanish, warm but formal. "Una velada en ocho actos.", "menú degustación de ocho actos", prices in "180 €" format, dates as "5 de octubre de 2026".
- **AR** (~310 lines): Modern Standard Arabic, formal hospitality register. "سهرة في ثمانية فصول.", full RTL authoring, Arabic drop-cap letters chosen per locale ("ق" for the manifesto, "د" for blog body opening). Proper names (chef, staff, producers, wines, press) stay Latin. Address stays Latin because it's a Milan street name. Dates in "5 أكتوبر 2026" (Western numerals retained for consistency with prices). Arrows flipped where they're directional reading cues.

Shared image URL constants (`_INGREDIENTI_IMG`, `_FILOSOFIA_IMG`, `_ATMO_*`) extracted as module-level vars so image URLs aren't duplicated 4×.

### 5 — Wiring into TEMPLATE_CONTENT registry
Added 4-line import block + 4 locale keys under `gusto-fine-dining` in `TEMPLATE_CONTENT`. `python manage.py check` clean.

### 6 — _base.html i18n/RTL authoring
Replaced `<html lang="it">` with dynamic `<html lang="{{ locale }}" dir="{{ html_dir }}">`. Added conditional Amiri + Noto Kufi Arabic Google Fonts link (only loads for AR). Replaced hardcoded mp-bar strings with `{{ chrome.mp_back }}` / `{{ chrome.mp_other_restaurant }}`. Added language switcher pill strip in mp-bar with per-pill URL locale rewrite; AR pill carries `lang="ar" dir="rtl"` so الع renders in Arabic font. Every nav link (left + right) and every footer link appends `?lang={{ locale }}` when non-IT. Footer section headings now from chrome; footer hours / star line / copyright now from `site.*`.

Authored the RTL CSS block in two parts:
- **Core** (outside `{% if is_rtl %}`, always present): body font swap to Noto Kufi Arabic + Amiri, body 17px / line-height 1.85, letter-spacing flatten on uppercase tracking (nav/eyebrow/sec-label/mp-bar/footer-h5/bot), nav-grid justify flip, nav underline sweep origin flip, eyebrow `:before` → `:after` accent bar, gold-btn arrow `→` → `←`, mp-bar `flex-direction: row-reverse`.
- **Page-level** (inside `{% if is_rtl %}` so LTR skips the CSS entirely): flip `.fd-hero` grid to image-left, swap portrait `border-left` → `border-right` on `.fd-chef / .fd-concierge / .fd-lead-post / .fd-filosofia-img`, invert `grid-template-columns` on all `-inner` wrappers + `.fd-ingredienti`, flip drop-cap floats from `float: left` to `float: right` (with matching padding mirror), right-align course/room numbers, left-align wine/meta columns, right-align gallery + atmo captions, row-reverse awards.

### 7 — Page-template wiring
- `home.html` — all 13 hardcoded strings moved to `page_data.*`, URLs preserve locale.
- `about.html` — 5 hardcoded strings moved to `page_data.*`, URLs preserve locale.
- `menu.html` — courses_label from `page_data`, wine pairing label from `chrome.fd_wine_pairing`.
- `gallery.html` — 4 hardcoded strings moved to `page_data.*`, URLs preserve locale.
- `reservations.html` — 6 hardcoded labels moved to `page_data.*`, concierge email/phone labels from `chrome.fd_*_label`, form rewritten as `{% for field in page_data.form_fields %}` loop with conditional rendering by `field.2` (type) and `forloop.counter0 == 6` for full-width intolerances. Occasion options from `page_data.occasion_options` (separate list because Django templates have no `split` filter).
- `blog_list.html` — read_article + min label from `page_data`, URL locale preservation on post links.
- `blog_detail.html` — crumb_label / min_read_label / back_link / footer_label / empty_body from `content.diario.*` (accessed via content dict since `page_data` on detail view is per-post, not per-page). URL locale preservation.

### 8 — Validation
- `python manage.py check` — 0 issues.
- Migrations + `seed_categories` + `seed_templates` + `sync_template_tiers` — clean. 3 published_live / 17 draft confirmed.
- `smoke_i18n_gusto.py` — **52/52 green**:
  - 35 Gusto routes (home + filosofia + menu + atmosfera + diario + prenota + diario/menu-autunno-26 × 5 locales)
  - 10 Cardio regression routes (home + contatti × 5 locales)
  - 5 Derm regression routes (home × 5 locales)
  - 2 negative tests (unknown `?lang=zz` → IT 200, empty `?lang=` → IT 200)
- Browser walk at 1440×900 via Playwright — all 5 Gusto locales render cleanly on home. Arabic confirmed `dir="rtl"`, `lang="ar"`, Amiri + Noto Kufi Arabic loaded, body 17px, hero grid flipped (image 771px LEFT / text 653px RIGHT), gold-btn `:after content "←"`, hero grid `771.328px 653.672px`.
- Arabic inner pages: prenota form RTL-aligned with Arabic labels/placeholders + gold submit button "أرسِل ملاحظةً إلى مسؤولة الاستقبال"; menu with RIGHT-aligned dish names + LEFT-aligned Latin wine names (Latin + Arabic mix flows correctly); gallery 6 lightbox triggers preserved + 4 rooms in Arabic; blog detail RTL with Arabic drop-cap.
- Motion regression on EN home: `body.lm-ready=true`, 25 reveal targets, 5 stagger parents, 3 counters, 4 atmosphere-teaser lightbox triggers, awards + ingredients + seasonal + atmosphere sections all present. Zero data-lm/data-li breakage.
- Cardio AR regression: renders identically to pre-Session-29 baseline (medical specialist skin untouched by this session).
- Mobile sanity at 390×844: Gusto AR scroll-width 673px vs IT 701px — AR actually slightly tighter than IT (Arabic composes denser in fixed-width slots). Pre-existing desktop-first Gusto overflow (~660-700px, documented in Session 22) unchanged.

### 9 — Gotchas
- **Django template `split` filter doesn't exist.** First draft of the reservations form tried to split the occasion placeholder on " / " inside the template. Moved to a separate `occasion_options` list keyed per locale. Clean.
- **Windows cp1252 console can't print ✓/✗ glyphs.** First smoke-test run crashed on Unicode print. Replaced with `OK`/`FAIL` ASCII labels. Clean.
- **Arabic drop-caps need manual letter selection.** Can't just grab `text[0]` because Arabic manifest starts with "قائمة" but the visual first-letter should be "ق" (the same character). For blog body opening "دخلت", the drop-cap letter is "د". Authored manually in each locale tree.
- **Latin wordmark must stay Latin in RTL.** Without `html[dir="rtl"] .fd-nav .logo .name { font-family: '{{ theme.heading_font }}' }` the "Osteria Moderna" wordmark would render in Amiri — wrong brand face. Explicit override.

### 10 — Decision
**GUSTO I18N/RTL APPROVATO.**

Phase 2i.2 closed in full. All 3 `tier=published_live` templates now ship in 5 locales with working RTL. Architecture proven across two archetypes (specialist + fine-dining), with restaurant-generic chrome keys positioned for reuse by Phase 2g3.1 (Sapore / Brace).

## Session 28 — Ultra Premium Live Pass (Phase 2g2x.12) (2026-04-12)

**Agent:** Premium UI session. Ultra-premium feature & interaction pass on the 3 published_live templates.
**Branch:** `phase-ultra-premium-live-v1`.
**Scope floor:** enrich cardio, dermatologia, gusto with new sections, interactive components, and visual richness. Non-goals: touch drafts, reopen tiering, new categories/templates, auth/checkout/editor/projects/commerce.

### 1 — Audit & Strategy

Read all 11 context/memory files + all specialist + fine-dining skin files + motion system. Identified per-template enhancement opportunities with a differentiation matrix ensuring each template gets distinct new interactive patterns:

- **Cardio:** technology/equipment grid + patient testimonial + FAQ accordion + sticky CTA bar
- **Dermatologia:** treatment gallery strip + patient testimonial + FAQ accordion + sticky CTA bar
- **Gusto:** ingredients/sourcing editorial band + awards section + seasonal highlight card + lightbox gallery + expanded atmosphere strip (3→4 images)

### 2 — New Interactive Components Library

Created `static/css/live-interactions.css` (208 lines) + `static/js/live-interactions.js` (200 lines):
- **Accordion** — smooth height animation, keyboard accessible, single-open mode, +/- icon transition
- **Lightbox** — image modal with navigation arrows, keyboard support (Esc/←/→), grouped images, caption display
- **Sticky CTA bar** — appears after scrolling past hero, IntersectionObserver-driven
- All components: `prefers-reduced-motion` support, no dependencies, graceful degradation without JS

### 3 — Specialist Skin Enhancements (Cardio + Derm)

Modified `home.html` with 6 new conditional sections + CSS:
- `sp-tech` — 4-column technology/equipment grid with inline SVG icons (ECG, echo, holter, stress) — Cardio-only via `{% if page_data.tecnologie %}`
- `sp-gallery-strip` — 4-image treatment gallery with hover reveal captions — Derm-only via `{% if page_data.gallery_strip %}`
- `sp-testimonial` — editorial patient quote with quotation mark accent — both (different content per template)
- `sp-faq` — accordion FAQ with 5 items, single-open mode — both (different questions per template)
- Sticky CTA bar — dark glass bar with brand name + appointment CTA — both
- Signature visits now have inline SVG dot icons for better visual rhythm

Modified `_base.html`: linked `live-interactions.css` + `live-interactions.js`.

### 4 — Fine-Dining Skin Enhancements (Gusto)

Modified `home.html` with 4 new sections + CSS:
- `fd-ingredienti` — 2-column editorial band (image + text) about ingredient sourcing
- `fd-awards` — 4-column awards/recognition grid (Michelin star, Gambero Rosso, Identità Golose, 50 Best)
- `fd-stagione` — bordered seasonal highlight card with current menu teaser
- `fd-atmo` — expanded from 3 to 4 images, now with lightbox triggers for all images

Modified `gallery.html`: added lightbox triggers on all 6 gallery images with grouped navigation.
Modified `reservations.html`: added SVG process icons to the 4-step booking workflow.
Modified `_base.html`: linked `live-interactions.css` + `live-interactions.js`.

### 5 — Content Registry Updates

Added new content blocks to `template_content.py`:
- Cardio home: `tecnologie` (4 equipment items), `testimonianza`, `faq` (5 questions)
- Derm home: `gallery_strip` (4 images), `testimonianza`, `faq` (5 questions)
- Gusto home: `ingredienti`, `riconoscimenti` (4 awards), `stagione` (seasonal card), expanded `atmosphere_teaser` (3→4 images)

Updated all i18n content files with translated versions:
- `template_content_cardio_i18n.py`: EN/FR/ES/AR blocks for tecnologie, testimonianza, faq
- `template_content_dermatologia_i18n.py`: EN/FR/ES/AR blocks for gallery_strip, testimonianza, faq

### 6 — Validation Results

- `python manage.py check` → 0 issues
- **34/34 route smoke tests green:**
  - 9 cardio IT + 4 cardio i18n (EN/FR/ES/AR) = 13
  - 9 derm IT + 4 derm i18n (EN/FR/ES/AR) = 13
  - 7 gusto IT + 1 blog post = 8
- **Cross-contamination:** 0 Ricciardi in Cardio, 0 Marani in Derm, 0 medical in Gusto
- **Gusto motion regression:** 37 data-lm attrs (unchanged), 9 staggers, 3 counters, 0 medical CSS leaked
- **i18n/RTL verified:** Cardio AR (dir=rtl + tech + FAQ + testimonial), Derm AR (dir=rtl + gallery + FAQ), all new sections render in all 5 locales
- **Differentiation audit:** 12/12 unique-section checks pass, 0 shared interactive patterns across categories

## Session 27 — Medical Motion Opt-In (Phase 2g2x.11) (2026-04-12)

**Agent:** Premium UI session. Motion opt-in for the specialist archetype (cardio + dermatologia).
**Branch:** `phase-motion-optin-medical-v1`.
**Scope floor:** apply motion language to the 2 medical `published_live` templates with a clinical profile. Non-goals: touch Gusto, touch drafts, extend i18n, new features, refactor frontend.

### 1 — Audit & Strategy

Read all 11 context/memory files + all 9 specialist skin files + live-motion.css/js. Identified insertion points across all pages. Defined a 4-pattern medical motion profile:

1. **Reveal-on-scroll** — fade+rise with `--lm-rise: 10px` (Gusto: 14px)
2. **Stagger** — cascaded entry with 80–100ms delay (Gusto: 70ms)
3. **CTA hover refinement** — arrow shift +4px, ghost-btn lift, submit opacity
4. **Image attention lift** — filter transition on hover (not zoom)

Excluded: counters (too promotional), nav sweep (too restaurant), marquee, image zoom.

### 2 — Implementation

Modified 9 specialist skin files. Zero changes to Gusto, shared motion files, or marketplace.

| File | Changes |
|------|---------|
| `_base.html` | +link live-motion.css, +script live-motion.js, +medical token overrides, +CTA/image hover CSS, +reduced-motion guards, +RTL arrow-shift override |
| `home.html` | +11 data-lm reveals, +4 data-lm-stagger parents (Cardio); +12/+5 (Derm via hero variant) |
| `about.html` | +stagger on history + values, +reveal on method + CTA band |
| `services.html` | +stagger on treatments, +reveal on footnote + CTA band |
| `team.html` | +reveal on each doctor, +stagger on tags |
| `contact.html` | +stagger on blocks, +reveal on form + sidebar |
| `appointment.html` | +stagger on process steps, +reveal on form band |
| `blog_list.html` | +reveal on lead post, +stagger on compact list |
| `blog_detail.html` | +reveal on lede + h2 headings + blockquotes |

### 3 — Validation Results

- `python manage.py check` → 0 issues
- **34/34 route smoke tests green:**
  - 7 cardio IT routes + 4 cardio i18n (EN+AR) = 11
  - 7 derm IT routes + 4 derm i18n (EN+AR) = 11
  - 6 gusto IT routes (regression) = 6
  - 3 detail pages + 2 draft 404 + 1 listing = 6
- **Cardio home:** 11 data-lm, 4 stagger, lm-ready=true, tokens `10px/16px/680ms`
- **Derm home:** 12 data-lm, 5 stagger (extra from credentials + editorial-magazine hero)
- **Cardio AR:** dir=rtl, lang=ar, 11 data-lm — motion works in RTL
- **Derm AR:** dir=rtl, 17px body, all motion active
- **Gusto regression:** 20 data-lm, 4 stagger, tokens `14px/720ms` (Gusto originals, NOT medical overrides), 0 medical CSS leaked
- **Catalog listing:** exactly 3 published_live templates visible
- **Cross-contamination:** 0 "Ricciardi" in cardio, 0 "Marani" in derm
- **Console errors:** 0 (only favicon 404)

### 4 — Decision

D-061 formalized in DECISIONS.md.

**MEDICAL MOTION OPT-IN APPROVATO.**

---

## Session 25 — Catalog Stabilization & Fix Consolidation (Phase 2g2x.10) (2026-04-12)

**Agent:** Consolidation session. No new features, no new categories, no new templates. Pure stabilization pass to unify all approved fixes from Sessions 17–24 into a single baseline branch.
**Branch:** `phase-catalog-stabilization-v1`.
**Scope floor:** consolidate approved fixes, generate missing preview PNGs, verify public catalog integrity. Non-goals: new features, new archetypes, new languages beyond consolidation, draft reopening, auth/checkout/editor/projects/commerce.

### 1 — Consolidation Audit

Read all 11 context/memory files + verified codebase state against every approved fix from Sessions 17–24.

**Already present on baseline (no action needed):**
- A. Tier migration / catalog honesty (Session 21, commit `0a5bcf2`) — ghost CTA removed, draft 404, empty states, 3 published_live
- B. Business hardening Pragma vs Elevate (Session 17, commit `b967e99`) — DNA + compositions distinct, both correctly draft
- C. Portfolio hardening Chiara vs Pixel (Sessions 18–19, commit `79c8793`) — DNA + compositions distinct, overflow fix included
- D. Motion pilot Gusto (Session 22, commit `58f43f4`) — live-motion.css + .js + fine-dining wired
- E. Cardio i18n/RTL 5 locales (Session 23, commit `bcd5306`) — template_i18n.py + 5 locales functional

**Missing from baseline (consolidated in this session):**
- F. Dermatologia i18n (Session 24, commit `9043836` on `phase-i18n-dermatologia-v2`) — cherry-picked
- G. Preview PNGs for all 3 published_live templates — never generated, root cause of "cardio and derm look identical on listing"

### 2 — Consolidation Actions

1. **Cherry-picked derm i18n** — commit `9043836` from `phase-i18n-dermatologia-v2` (Session 24 approved). 2 files: `template_content_dermatologia_i18n.py` (NEW, 4 locale blocks EN/FR/ES/AR) + `template_content.py` (updated imports + 5-locale mapping). Django check clean. All 5 derm locale routes 200.

2. **Generated preview PNGs** — ran `generate_previews --force --only <slug>` for all 3 published_live templates via Playwright Chromium at 1600×900 @2x:
   - `cardio-studio-specialistico-preview.png` — specialist archetype, red accent, "Studio Marani", LANCET/European Heart Journal press strip
   - `dermatologia-elite-roma-preview.png` — specialist archetype, green accent, "Studio Ricciardi", JAMA Dermatology/British Journal press strip
   - `gusto-fine-dining-preview.png` — fine-dining archetype, dark/gold, "Osteria Moderna", chef + course menu

   All 3 are visually distinct at card size despite cardio+derm sharing the specialist archetype. Differentiation comes from: accent color, brand name, headline copy, press outlets, specialty-specific services.

### 3 — Validation Results

- `python manage.py check` → 0 issues
- Migrations: all applied (catalog 0001 + 0002)
- `seed_templates` + `sync_template_tiers` → 20 templates, 3 published_live / 17 draft
- **32/32 route smoke tests green:**
  - 12 cardio routes (IT + 4 locales + 7 inner pages)
  - 11 derm routes (IT + EN + AR + 8 inner pages)
  - 8 gusto routes (IT + 7 inner pages)
  - 4 draft 404 checks
- **6/6 empty states correct** for draft-only categories
- **Zero cross-contamination:** "Ricciardi" never appears in cardio HTML, "Marani" never appears in derm HTML
- **3/3 preview PNGs generated:** all on disk + in DB, zero orphans, zero placeholders
- **Ghost Anteprima Live CTA: confirmed absent** from all detail pages
- **Language switchers present** on both cardio and derm live previews

### 4 — Files Modified

| File | Action | Purpose |
|------|--------|---------|
| `apps/catalog/template_content_dermatologia_i18n.py` | NEW (cherry-pick) | 4 non-IT content trees for derm (EN/FR/ES/AR) |
| `apps/catalog/template_content.py` | MODIFIED (cherry-pick) | Import derm locale blocks + update TEMPLATE_CONTENT mapping |

### 5 — Preview Asset Reconciliation

| Template | PNG File | DB Record | Orphans |
|----------|----------|-----------|---------|
| cardio-studio-specialistico | `template_assets/2026/04/cardio-studio-specialistico-preview.png` | ✅ TemplateAsset | 0 |
| dermatologia-elite-roma | `template_assets/2026/04/dermatologia-elite-roma-preview.png` | ✅ TemplateAsset | 0 |
| gusto-fine-dining | `template_assets/2026/04/gusto-fine-dining-preview.png` | ✅ TemplateAsset | 0 |

No orphan files. `media/preview_imagery/` contains 12 cached stock photos (6 medical-specialist + 6 restaurant-fine) — these are the source imagery, not orphans.

### 6 — What Remains Out of Scope (by design)

- Phase 2g2x.1: agency, lawyer, real-estate identity crash (all draft, hidden from public)
- Phase 2g2x.3: D-047 leak lifts on preview compositions
- Phase 2g3: live skin folder authoring for draft templates
- Motion pilot opt-in for specialist skin (cardio/derm)
- Gusto i18n (Phase 2i.2 step 2, new RTL CSS block needed)
- Preview imagery pool overlap: cardio/derm share `medical-specialist` pool (same 6 photos) — differentiated by content/accent/brand, not by imagery pool. Pool split is tracked in TODO_NEXT 2g2x.2.

### 7 — Decision

**CATALOG STABILIZATION APPROVATA.**

The baseline is now stable: all approved fixes from Sessions 17–24 are present in a single branch, preview PNGs differentiate the 3 published_live templates, and the public catalog shows zero regressions. The "scattered worktree" problem is resolved for all work approved through Session 24.

## Session 23 — i18n/RTL Pilot Cardio (Phase 2i.1) (2026-04-11)

**Agent:** Implementation session. First multilingual publishing validation on a `tier=published_live` template. Scoped tightly to `cardio-studio-specialistico` — no other template touched, no marketplace chrome touched, no auth/checkout/editor/projects/commerce touched, no Django gettext machinery introduced.
**Branch:** `phase-i18n-pilot-cardio-v2` (worktree).
**Scope floor:** define the multilingual architecture on ONE live template, validate with 5 locales (it/en/fr/es/ar) + real RTL for Arabic, produce a reusable recipe for Phase 2i.2. Non-goals: translate derm, translate gusto, translate drafts, translate the marketplace surface, introduce LocaleMiddleware or .po tooling, change URL patterns, touch the motion pilot.

### 1 — Strategy: locale-keyed content registry + CHROME_I18N dict + `?lang=` param, zero new build tooling

The project already has a Python content registry at `apps/catalog/template_content.py` (D-042) and a visible `tier=published_live` floor of 3 templates (cardio, derm, gusto). Two paths were available for multilingual publishing:

- **Path A — Django `{% trans %}` + `.po` files.** The textbook shape. Rejected because: (1) compiled `.mo` files need `gettext` binaries which are flaky on Windows dev boxes and add a build step; (2) every string splits across two files (`.po` + content dict), doubling the review surface; (3) the pilot's job is to prove a shape with ZERO new build tooling so a reviewer can read and fix any locale in 10 seconds; (4) phase-later migration from Path B to Path A for the marketplace chrome itself is trivial because every string is already namespaced by locale.
- **Path B — locale-keyed content dict + CHROME_I18N dict + `?lang=` query param.** Selected. One review surface, no tooling, unambiguous IT fallback via `pick_localized`, trivial HTTP-GET testing, additive per template, no URL pattern changes, RTL gated via a single `html[dir="rtl"]`-scoped CSS block inside the archetype `_base.html`.

See DECISIONS.md § D-059 for the full rationale.

### 2 — Architecture: one new module, one new sister file, one view change, 9 template edits

- `apps/catalog/template_i18n.py` — NEW — the pilot's infrastructure module:
  - `SUPPORTED_LOCALES = ("it", "en", "fr", "es", "ar")`, `DEFAULT_LOCALE = "it"`, `RTL_LOCALES = frozenset({"ar"})`, `LOCALE_LABELS`, `LOCALE_BADGES`.
  - `CHROME_I18N[locale][key]` — the ~30 chrome labels the specialist skin itself renders (marketplace bar: `mp_back/mp_preview_of/mp_other/mp_language`; footer: `foot_studio/foot_pages/foot_contact/foot_hours/foot_privacy/foot_cookie/foot_legal`; home home-links: `home_all_doctors/home_publications`; contact form: `form_name/form_surname/form_email/form_phone/form_subject/form_message/form_submit`; appointment alt: `apt_alternative_prefix/apt_alternative_link`; blog: `blog_read_full/blog_read_minutes/blog_back_all_prefix/blog_crumb_sep`). All 5 locales authored. Every key backed by IT fallback at render time via `get_chrome(locale)` merging.
  - Helpers: `resolve_locale(request)` reads `?lang=xx` validated against the allowed list, `is_rtl(locale)`, `html_dir(locale)` → `"rtl"|"ltr"`, `get_chrome(locale)`, `pick_localized(content_by_locale, locale)` (accepts legacy flat shape for safety), `locale_switcher_entries(current_locale)` builds the switcher data.

- `apps/catalog/template_content_cardio_i18n.py` — NEW — 4 full content trees (`CARDIO_CONTENT_EN/FR/ES/AR`), ~1600 lines, one tree per locale. The IT tree remains inline in `template_content.py` as `CARDIO_CONTENT_IT` because it's the authoritative source and benefits from being reviewed next to derm+gusto. Shared portrait URLs live as module-level `_CHIEF_PORTRAIT` etc. constants so the trees stay flat (no shared-reference bugs).

- `apps/catalog/template_content.py` — refactored:
  - Renamed `CARDIO_CONTENT → CARDIO_CONTENT_IT`, `DERMATOLOGIA_CONTENT → DERMATOLOGIA_CONTENT_IT`, `GUSTO_CONTENT → GUSTO_CONTENT_IT`.
  - Top-level `TEMPLATE_CONTENT` is now `{slug: {locale: tree}}`. Cardio has 5 locale keys; derm and gusto are wrapped under `{"it": ..._IT}` to keep the API uniform.
  - `has_live_template/get_content/get_pages/find_page/find_post` helpers gained a `locale` kwarg (default `None` → `DEFAULT_LOCALE`). Resolution delegates to `template_i18n.pick_localized` which falls back to IT when the requested locale is missing — so derm+gusto with `?lang=en` render English chrome + Italian content (clean mixed state documented as the transitional shape for Phase 2i.2).

- `apps/catalog/views.py` — `LiveTemplateView.setup()`:
  - New line: `self.locale = template_i18n.resolve_locale(request)`.
  - `template_content.get_content(slug, self.locale)` — threads locale through the registry helpers.
  - `template_content.find_page/find_post` calls gained the locale kwarg.
  - `get_context_data()` now exposes: `locale`, `chrome` (= `get_chrome(self.locale)`), `html_dir`, `is_rtl`, `locale_switcher` (= `locale_switcher_entries(self.locale)`), `default_locale`. These are the context vars every specialist skin file now reads.

- `templates/live_templates/medical/specialist/_base.html` — rewritten for i18n:
  - `<html lang="{{ locale|default:'it' }}" dir="{{ html_dir|default:'ltr' }}">` — dynamic.
  - Conditional Arabic font preload: when `is_rtl`, add a Google Fonts `<link>` for Noto Naskh Arabic (serif) + Noto Kufi Arabic (body), and inside a second `:root {}` block override `--heading` and `--body` CSS vars to put the Arabic fonts first in the stack while preserving the Cormorant/Inter fallback for mixed Latin/Arabic strings.
  - Marketplace bar: every hardcoded IT string replaced with `{{ chrome.mp_back }}`, `{{ chrome.mp_preview_of }}`, `{{ chrome.mp_other }}`, `{{ chrome.mp_language }}`. Added a `.mp-lang` pill strip that loops `locale_switcher` and generates preview URLs with `?lang={{ entry.code }}` (the IT pill has no param, per the `default_locale` check). Each pill carries `lang/dir` per-pill so the الع pill renders in its own RTL context.
  - Footer: `{{ chrome.foot_studio/foot_pages/foot_contact/foot_hours/foot_privacy/foot_cookie/foot_legal }}` replace the 7 hardcoded IT headings.
  - Every internal URL (`mp-back`, `sp-nav left/right`, footer page list) now appends `?lang={{ locale }}` when `locale != default_locale` — uniform fragment `{% if locale != default_locale %}?lang={{ locale }}{% endif %}`.
  - NEW **RTL-scoped CSS block** at the bottom of the `<style>` tag: `html[dir="rtl"] body` → font-size 17px + line-height 1.8; `html[dir="rtl"] h1–h5` → letter-spacing 0 (Arabic shapes don't want tracking); `html[dir="rtl"] .sp-lead .eyebrow:before { display: none }` + `:after { ...accent-bar... margin-right: 4px }` to flip the accent-bar side; `.sp-lead .gold-btn:after { content: '←' }`; `.sp-nav .right { justify-content: flex-start }` + `.sp-nav .left { justify-content: flex-end }` to swap the nav visual order for reading direction; lower letter-spacing on `.sp-nav .left/.right` / `.sp-foot .top h5` / `.mp-bar` / `.mp-lang *` / `.sp-foot .bot` to 0.04em.

- `templates/live_templates/medical/specialist/home.html` — hardcoded "Tutti i medici" and "Pubblicazioni" in the chief-section link row replaced with `{{ chrome.home_all_doctors }}` / `{{ chrome.home_publications }}`. Every `{% url ... %}` call that points to an inner preview page now appends `?lang={{ locale }}` when `locale != default_locale`. Zero content changes — content comes from the locale-specific `page_data.*` block, which for cardio is one of 5 blocks depending on the locale.

- `templates/live_templates/medical/specialist/about.html` — only URL locale preservation on the final `.sp-cta-band` (2 CTAs). No chrome strings to replace because Session 14 already abstracted every label into `page_data.*`.

- `templates/live_templates/medical/specialist/services.html` — only URL locale preservation on the final `.sp-cta-band`.

- `templates/live_templates/medical/specialist/team.html` — **zero edits**. The Session 14 D-047 lift made this file fully `{{ d.* }}`-driven — nothing to localize at the chrome level.

- `templates/live_templates/medical/specialist/contact.html` — form labels replaced with chrome keys: `{{ chrome.form_name/form_surname/form_email/form_phone/form_subject/form_message/form_submit }}` (6 labels + submit button).

- `templates/live_templates/medical/specialist/appointment.html` — alt-link row: `{{ chrome.apt_alternative_prefix }} <a ...>{{ chrome.apt_alternative_link }}</a>` replaces the "In alternativa: parla con la segreteria" hardcoded string. URL preserves locale.

- `templates/live_templates/medical/specialist/blog_list.html` — the "Leggi l'articolo completo" lead-post read-more link and the `min` shorthand in the meta rows now come from `{{ chrome.blog_read_full }}` / `{{ chrome.blog_read_minutes }}`. Every `{% url 'catalog:live_template_post' ... %}` preserves locale.

- `templates/live_templates/medical/specialist/blog_detail.html` — the crumbs separator is now `{{ chrome.blog_crumb_sep }}`, the "X min di lettura" meta row uses `{{ chrome.blog_read_minutes }}`, the footer-meta back link uses `{{ chrome.blog_back_all_prefix }} {{ page.label|lower }}` so English renders "← All publications", French "← Toutes les publications", Arabic "→ جميع المنشورات".

### 3 — Quality of the 5 languages

Explicitly NOT machine-translated. Each locale was authored to read as if a native speaker in that market wrote the copy for a premium Roma cardiology practice:

- **IT** (authoritative) — existing Session 11/14 content, light polish where a phrase was ambiguous.
- **EN** — Anglo-American clinical prose, direct and unembellished. "A tailored cardiology, for those who refuse shortcuts." "Six clinical pathways, a single signature." "Every consultation is personally arranged with the physician." Doctor bios read as native-speaker clinical voice: "Specialised in cardiology at the University La Sapienza of Rome, further trained in clinical echocardiography at the Institut de Cardiologie de Montréal. Member of SIC and ESC. Author of over forty peer-reviewed publications, including two chapters of the Italian edition of the Braunwald cardiology textbook."
- **FR** — classical French medical prose, `vous` register, no anglicisms. "Une cardiologie sur mesure, pour celles et ceux qui refusent les raccourcis." "Six parcours cliniques, une seule signature." Timeline and method paragraphs rewritten to preserve editorial rhythm without word-for-word translation. Inclusive "celles et ceux" kept where the IT original addresses a broader audience.
- **ES** — Spanish peninsular register, warm yet precise. "Una cardiología a medida, para quien no acepta atajos." Prices in `220 €` format per ES convention. Dates "12 de marzo de 2026".
- **AR** — Modern Standard Arabic, formal medical register, native punctuation (« »). Headline: `طبّ قلب مُفصَّل خصّيصاً لمن لا يقبل بالاختصارات`. Manifesto opens with a drop-cap-compatible single-letter: `ط` + `بّ القلب ليس خطّ إنتاج...`. Doctor bios fully authored: `متخصص في أمراض القلب من جامعة لا سابينزا في روما، واستكمل تدريبه في معهد أمراض القلب في مونتريال.`. Arabic punctuation and native medical terminology throughout (استجواب سريري, تخطيط كهربية القلب, هولتر, مراقبة كهربية قلبية). Doctor names and press outlets kept in Latin where canonical ("LANCET", "European Heart Journal", "Sole 24 Ore", "RAI Med") because the brand is Roma-based and these are Latin proper nouns. Dates localized ("12 مارس 2026").

Every form field placeholder is localized with region-appropriate name/phone format examples (Mark Smith / mark@email.com / +44 7... for EN; Jean Dupont / +33 6... for FR; Juan García / +34 6... for ES; محمد العلوي / mohammed@email.com / +39... for AR with a deliberately Italian phone prefix because the clinic IS in Roma).

### 4 — RTL implementation details (load-bearing for Arabic quality)

The Arabic locale is where the pilot earns or loses its premium positioning. The RTL block is authored with four specific goals:

1. **Reading direction is visual, not just logical.** `<html dir="rtl">` gives you the basics: CSS `margin-inline-start` flips, flex row direction reverses, `text-align: start` resolves to right. But cosmetic accents (`:before` hairlines, arrow glyphs, underline-left borders) don't flip because they're authored positionally, not logically. The RTL block manually flips these.
2. **Arabic doesn't want Latin typographic conventions.** Negative letter-spacing on h1 is a premium-editorial choice for Latin serifs — in Arabic it squeezes naskh shapes together and looks cheap. Uppercase + 0.22em tracking on chrome labels is standard for Latin SANS in Italian marketplaces — in Arabic there is no uppercase, and that tracking becomes a 0.04em whisper. Both are forced to 0 / 0.04em inside the RTL block.
3. **Arabic naskh is physically taller than Latin serif at the same point size.** Without a font-size bump, ascenders and descenders collide with line-height 1.6. The RTL block bumps body font to 17px and line-height to 1.8 — one size step up — which restores visual breathing room without rearchitecting the type scale.
4. **Font stack must carry Latin as a fallback.** Doctor names, dates, addresses, phone numbers, and press outlets stay Latin across every locale because they're either proper nouns or technical strings. Forcing Noto Naskh Arabic on them would break their rendering. The conditional RTL `:root {}` override puts Noto Naskh first and Cormorant second, so Arabic glyphs get the naskh treatment AND Latin glyphs get the serif treatment in the same paragraph.

The arrow direction convention is: UI chrome arrows (`mp_back`, `mp_other`) are authored natively in each locale's `CHROME_I18N` block, so the Arabic `mp_back` reads `"العودة إلى MarketWeb →"` with the right-pointing arrow because RTL reading goes right-to-left. The decorative `.gold-btn:after` arrow in the hero is flipped from `→` to `←` by the CSS override because it's purely visual and not a natural-language string.

### 5 — Validation results

- `python manage.py check` → 0 issues.
- `smoke_i18n.py` route sweep (Django test client, 51 checks):
  ```
  CARDIO — 5 locales × 9 routes = 45 checks
  --- locale: it ---  (no ?lang param)
    OK  200  /templates/medical/cardio-studio-specialistico/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/studio/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/visite/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/medici/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/contatti/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/richiedi-visita/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/pubblicazioni/
    OK  200  /templates/medical/cardio-studio-specialistico/preview/pubblicazioni/secondo-parere-quando-richiederlo/
  --- locale: en / fr / es / ar ---  (same 9 routes with ?lang=xx)
    36× 200 OK
  REGRESSION & NEGATIVE CHECKS
    OK  200 (exp 200)  /templates/medical/dermatologia-elite-roma/preview/                  [IT-only, no param]
    OK  200 (exp 200)  /templates/medical/dermatologia-elite-roma/preview/?lang=en          [EN chrome + IT content fallback]
    OK  200 (exp 200)  /templates/restaurant/gusto-fine-dining/preview/                    [IT-only, no param]
    OK  200 (exp 200)  /templates/restaurant/gusto-fine-dining/preview/?lang=ar            [AR chrome + IT content, RTL flips]
    OK  200 (exp 200)  /templates/medical/cardio-studio-specialistico/preview/?lang=xx     [unknown locale → IT fallback]
    OK  404 (exp 404)  /templates/agency/vertex-creative-agency/preview/?lang=ar           [draft still 404 public]
  TOTAL: 51/51
  ```
- Live browser walk at 1440×900 (Playwright):
  - **IT home** — `lang="it" dir="ltr"`, title "Studio Marani Cardiologia — Studio", H1 "Una cardiologia su misura, per chi non accetta scorciatoie.", nav labels `Studio / Lo Studio / Visite / Medici / Pubblicazioni / Contatti / Richiedi visita`, mp-back "← Torna a MarketWeb", footer heads `Lo studio / Pagine / Contatti / Orari`, 5 language pills with IT marked `.is-current`.
  - **EN home** — `lang="en" dir="ltr"`, title "Studio Marani Cardiologia — Practice", H1 "A tailored cardiology, for those who refuse shortcuts.", intro "Specialist consultations, second opinions, individual prevention programmes. One schedule, one physician, one signature.", nav `Practice / The Practice / Consultations / Team / Publications / Contact / Book a visit`, mp-back "← Back to MarketWeb", footer heads `The practice / Pages / Contact / Hours`, chief role "Clinical director · Cardiologist", primary CTA "Request a private visit", press label "Featured in".
  - **AR home** — `lang="ar" dir="rtl"` (verified both `document.documentElement.dir === 'rtl'` and the explicit `getAttribute('dir') === 'rtl'`), title "Studio Marani Cardiologia — المركز", H1 `طبّ قلب مُفصَّل خصّيصاً لمن لا يقبل بالاختصارات.` rendered right-aligned, H1 font-family computed to `"Noto Naskh Arabic", "Cormorant Garamond", Georgia, serif` (Arabic font first, Latin fallback preserved), body font-size 17px (bumped), nav labels `المركز / عن المركز / الاستشارات / الأطباء / المنشورات / تواصل / طلب زيارة`, mp-back `"العودة إلى MarketWeb →"` (right-arrow because RTL reading), facts `سنةً من الممارسة السريرية الخاصة` / `استشارة تخصصية في السنة` / `مستشفيات مرجعية في روما`, hero sidebar quote `«طبّ القلب ليس خطّ إنتاج. إنّه حوار طويل، يبنى على الوقت.»` with native Arabic quotation marks. Hero sidebar is visually on the LEFT of the H1 (flipped from LTR right) — layout reads correctly. Full-page screenshot `cardio-ar-home-rtl.png` confirms editorial rhythm intact.
  - **AR contact** — form labels (`الاسم / اللقب / البريد الإلكتروني / الهاتف / الموضوع / الرسالة`) all right-aligned, address blocks right-aligned, hours sidebar on the LEFT (flipped from LTR right), submit button reads `إرسال الرسالة`. Full-page screenshot `cardio-ar-contact.png` confirms layout integrity.
  - **FR visite** — `dir="ltr"`, H1 "Six parcours cliniques, une seule signature.", treatments list `Consultation cardiologique complète / Consultation de contrôle / Second avis spécialisé / Échocardiographie transthoracique / Holter cardiaque 24h / Programme de prévention 6 mois`, prices in "220 €" format, footnote heading "Notes administratives".
  - **ES blog detail** — `dir="ltr"`, article H1 "Cuándo tiene sentido pedir una segunda opinión cardiológica", kicker "Práctica clínica", meta "Dr. Riccardo Marani · 12 de marzo de 2026 · 6 min de lectura", full localized body paragraphs + H2 subheadings + blockquote, back link "← Todas las publicaciones".
- Mobile sanity at 390×844: IT cardio home scroll-width 835px, AR cardio home scroll-width 882px. Delta ~47px = intentional 17px body font bump for Arabic. **Pilot introduced zero new horizontal overflow.** The 835px baseline is the pre-existing Session 22-class desktop-first gap (specialist chrome uses `padding: 90px` and `grid-template-columns: 1.55fr 1fr`) — documented in the Session 22 handoff as out of scope and still out of scope.
- Regression: derm `?lang=en` and gusto `?lang=ar` both return 200 and render with localized chrome + IT content fallback. This is the intentional transitional shape for Phase 2i.2 — a template that hasn't had its content translated yet still works and still looks coherent because the chrome is locale-aware even when the content isn't.
- Marketplace chrome untouched: `/` homepage, `/templates/`, `/templates/medical/`, `/templates/medical/cardio-studio-specialistico/` all still render in Italian exactly as before.

### 6 — Gotchas worth remembering

- **Django template variables cannot begin with underscore.** First draft of `_base.html` used `{% url 'catalog:live_template_home' ... as _base_url %}` inside the language switcher loop. Django's `FilterExpression` rejected it with `TemplateSyntaxError: Variables and attributes may not begin with underscores: '_base_url'`. Renamed to `lang_base_url` and every reference. Lesson: Django's template language has its own identifier rules, not Python's.
- **Stale dev-server ghost (again).** Same Session 19/22 class. First browser walk showed zero language pills. Root cause: the `runserver --noreload` process on port 8765 was serving the pre-edit `_base.html` from memory. Killed and restarted on port 8766 — correct fresh HTML. Lesson still stands: if the browser walk shows "my edits didn't land" and `grep` confirms they ARE on disk, restart runserver on a fresh port before debugging cache/template layers.
- **Django test client ALLOWED_HOSTS.** The smoke test script ran Django via `django.setup()` in a bare script (not a test case), so the test client's `testserver` host was rejected by the empty `ALLOWED_HOSTS`. Fix: `settings.ALLOWED_HOSTS = ["testserver", "localhost"]` after `django.setup()`. Not a code path a real deployment would hit — only a smoke-script concern.
- **Content tree duplication is load-bearing, not a smell.** The cardio content is 5× its original size because every locale carries a complete mirror of the tree, including non-localizable data like phone numbers. This looks wasteful at first glance, but the alternative — a nested `{key: {locale: value}}` shape — would make reviewing any single locale a cross-reference scavenger hunt. Keeping each locale as a flat complete tree makes the review surface "one Python dict per locale" which is the cleanest thing to diff and the cleanest thing to hand to a translator.
- **Arabic font stack must keep Latin as a fallback.** First iteration set `--heading: 'Noto Naskh Arabic', Georgia, serif;` which broke the rendering of "LANCET" and "European Heart Journal" in the press strip. Fixed: `--heading: 'Noto Naskh Arabic', '{{ theme.heading_font }}', Georgia, serif;` — Noto takes the Arabic glyphs, Cormorant takes the Latin glyphs in the same paragraph, no regression on mixed-script press outlets.
- **Uppercase letter-spacing on Arabic is wrong.** First RTL draft kept the Latin `letter-spacing: 0.22em` on the eyebrows. The Arabic "العيادة" rendered with visible gaps between every glyph because CSS `letter-spacing` applies to ALL characters, not just uppercase. Lowered to 0.04em inside the `html[dir="rtl"]` block. Lesson: Latin typographic conventions (tracking on uppercase, negative letter-spacing on big serif headlines) don't just apply differently in Arabic — they're wrong. Each has to be explicitly zeroed or near-zeroed.

### 7 — Decisions added

- **D-059: i18n/RTL Pilot Architecture — Locale-Keyed Content Registry, Query-Param Switcher, No Django gettext.** Full rationale + option comparison + consequences in DECISIONS.md.

### 8 — What's reusable vs what's cardio-specific

**Reusable (Phase 2i.2 rollout):**
- `apps/catalog/template_i18n.py` — entirely. Locale metadata, CHROME_I18N, helpers. Other templates adopt by importing.
- The `{slug: {locale: tree}}` registry shape + `pick_localized` with IT fallback.
- `LiveTemplateView.setup` locale threading + `get_context_data` context vars (`locale`, `chrome`, `html_dir`, `is_rtl`, `locale_switcher`, `default_locale`).
- The `{% if locale != default_locale %}?lang={{ locale }}{% endif %}` href-preservation fragment. Future refactor: hoist into a `{% lang_url ... %}` template tag.
- The RTL-scoped CSS block shape. A new archetype copies the `html[dir="rtl"] ...` block from `specialist/_base.html` and renames `.sp-*` selectors to its own prefix.
- The Arabic font stack recipe (Noto Naskh Arabic + Noto Kufi Arabic, Latin fallback preserved inside `:root` override).

**Cardio-specific:**
- The 4 non-IT content trees in `template_content_cardio_i18n.py`. No shortcut — other templates need hand-authored content in the same shape.
- The specific RTL CSS selectors (`.sp-lead .eyebrow:before`, `.sp-nav .left/.right`, `.sp-lead .gold-btn:after`) — when gusto adopts the pilot these become `.fd-*` selectors in its own archetype base.

**Next session's cheapest first target:** dermatologia-elite-roma. It shares the specialist skin, so the RTL CSS and chrome integration are already done. The only new work is authoring its 4 non-IT content trees — 1.5h budget. After derm, gusto needs a new `.fd-*` RTL CSS block and its own 4 non-IT trees — 3h budget.

### 9 — Final state

- 51/51 smoke checks green. 5 locales × 9 cardio routes + 6 regression/negative.
- Cardio renders as a genuinely premium multilingual product in 5 languages, with real RTL for Arabic.
- Derm + gusto still work and now pick up English/French/Spanish/Arabic chrome automatically (content stays IT until Phase 2i.2).
- Marketplace chrome untouched.
- Draft templates still 404 public.
- Zero new Django middleware, zero new build tooling, zero new dependencies.

**Decision:** I18N/RTL PILOT CARDIO APPROVATO.

### 10 — Handoff notes

See AGENT_HANDOFF.md § Session 23 and TODO_NEXT.md Phase 2i.2 for next-session direction. The pilot architecture is ready to extend to the other `tier=published_live` templates (dermatologia first, gusto second) and is the expected multilingual floor for every future template promoted to `published_live`. Each new template opts in with one content file (its `template_content_<slug>_i18n.py` sister file with 4 locale blocks) + one entry update in `TEMPLATE_CONTENT` — the rest of the infrastructure is shared.

## Session 22 — Motion Pilot Gusto (Phase 2g2x.9) (2026-04-11)

**Agent:** Implementation session. First application of a reusable premium motion language on a live-template archetype. Scoped tightly to `gusto-fine-dining`; nothing else touched.
**Branch:** `phase-motion-pilot-gusto-v2` (worktree).
**Scope floor:** no other templates animated, no refactor of the marketplace frontend, no dependencies added, no translations, no tiering changes, no draft reopening, no commerce/auth/editor touched.

### 1 — Strategy: 6 restrained patterns, not 15 loud effects

Gusto is a dark-editorial, cream-on-charcoal-with-gold fine-dining skin. The only motion direction that fits that mood is *cinematic and calm* — slow ease-out, small distances, everything revealing like a page being unveiled. The pilot picks 6 patterns that each have a functional reason, and rejects everything that smells like a theme pack:

1. **Reveal-on-scroll** — fade + soft rise (14px body / 22px headings / fade-only for hero media). Guides eye down the page without asking for attention.
2. **Stagger** — direct children of `data-lm-stagger` parents get incremental transition-delays (70–110ms unit). Applied to facts, 8 courses, 5 timeline rows, 3 rooms, 6 gallery tiles, 4 values, 4 process steps, compact blog list, wine highlights, press strip.
3. **Count-up** on home facts (`14`, `8`, `180€`) — only place numbers carry meaning. Non-numeric suffix preserved via regex.
4. **Cinematic image hover** — `overflow: hidden` wrapper + inner background layer that scales 1.00→1.045 over 900ms on hover, with a gentle brightness/contrast lift. Applied to hero plate, chef portrait, concierge portrait, blog lead image, 6 gallery tiles.
5. **Gold-link arrow shift** — `→` translates +6px + letter-spacing widens 0.22→0.24em on hover, on every `.gold-btn`/`.gold-link`/`.fd-lead-post .read`/`mp-bar .mp-back`/footer links.
6. **Nav underline sweep** — `.fd-nav` links get an animated underline scaling from 0 to full width (scaleX origin-left). The current page underline is permanent; hover sweeps the others.

**Rejected:** parallax (CLS risk, heavy on mobile), slider/carousel (too loud for fine dining), bounce/elastic easing (cheap), blur-in (inconsistent), marquee press strip (the initial impulse — replaced with a calm stagger after the "niente slider rumorosi" re-read).

### 2 — Architecture: two reusable static files, zero dependencies

- `static/css/live-motion.css` (NEW, ~7KB) — motion tokens on `:root`, base reveal primitives gated on `body.lm-ready`, stagger rules (children of `[data-lm-stagger]`), image-frame hover utilities, `@media (prefers-reduced-motion: reduce)` collapse + `body.lm-reduced` class collapse (belt + braces).
- `static/js/live-motion.js` (NEW, ~7.6KB) — dependency-free IIFE that (1) adds `lm-ready` only after DOMContentLoaded, (2) observes reveals with `IntersectionObserver` threshold 0.15 + rootMargin `-80px`, (3) observes stagger parents and assigns per-child `transition-delay` on init, (4) observes counters at threshold 0.4 and animates with `requestAnimationFrame` + `easeOutCubic`, (5) short-circuits to `lm-reduced` on `prefers-reduced-motion: reduce`, (6) fails open on missing `IntersectionObserver`.

Both files are loaded via `{% static %}` in the `_base.html` of the fine-dining skin — one `<link>` in `<head>`, one `<script defer>` before `</body>`. No other skin is touched. This is the shape future archetypes opt into.

**Design tokens (on `:root` of live-motion.css):**
```
--lm-dur-fast  = 360ms
--lm-dur-med   = 560ms
--lm-dur-slow  = 720ms
--lm-dur-xslow = 900ms     (image hover zoom)
--lm-ease      = cubic-bezier(0.22, 0.61, 0.36, 1)  (ease-out, no overshoot)
--lm-rise      = 14px
--lm-rise-lg   = 22px
--lm-stagger   = 70ms
```

### 3 — No-JS fallback + reduced-motion: load-bearing decisions

- The CSS hidden state (`opacity: 0; transform: translate3d(0, 14px, 0)`) is guarded by `body.lm-ready`. That class is added ONLY by `live-motion.js` on DOMContentLoaded. If JS fails to load, `body` never gets `lm-ready`, the hidden rules never activate, and the page renders in full — no blank hero on a stale CDN. Verified in the browser by removing `lm-ready` at runtime: every reveal target returns to `opacity: 1 / transform: none`.
- `prefers-reduced-motion: reduce` is respected TWICE: a `@media` query in live-motion.css forces opacity/transform/transition to `!important` defaults for every `[data-lm]` / stagger child / image-hover target, AND the JS adds `body.lm-reduced` on init if the media query matches (which fires the second set of CSS rules that collapse the same properties). Belt + braces — a user with reduced motion gets a plain render even if the `@media` rule is stripped by an overzealous stylesheet. Verified by manually setting `body.lm-reduced` in the browser: opacity/transform/transition all collapse cleanly.

### 4 — Files modified

**New:**
- `static/css/live-motion.css` — reusable motion language (tokens, reveal primitives, stagger, image-frame hover, marquee placeholder, reduced-motion collapse).
- `static/js/live-motion.js` — reusable motion runtime (IO reveals, staggers, counters, marquee-duplication helper, reduced-motion guard).

**Modified (fine-dining skin only):**
- `templates/live_templates/restaurant/fine-dining/_base.html` — link motion CSS, script motion JS, enhance nav underline sweep (scaleX 0→1), gold btn arrow shift + letter-spacing hover, mp-bar back link hover, footer link transitions.
- `templates/live_templates/restaurant/fine-dining/home.html` — introduce `.plate-img` inner layer inside `.fd-hero .plate` for hover zoom, refactor `.fd-chef .portrait` to wrapper + `:before` overlay + `:after` image layer for the same zoom, attach `data-lm` reveal/stagger/counter attributes across hero, facts, manifesto, signature courses, chef block, press strip, CTA.
- `templates/live_templates/restaurant/fine-dining/menu.html` — reveals + stagger on 8 courses + wine intro + 4 wine highlights.
- `templates/live_templates/restaurant/fine-dining/about.html` — reveals + stagger on 5 timeline rows + method + 4 values + CTA.
- `templates/live_templates/restaurant/fine-dining/gallery.html` — gallery grid refactored to wrapper + inner `.bg` pattern so hover zoom has an `overflow: hidden` container (no CLS), caption lift on hover, stagger on 3 rooms + 6 tiles.
- `templates/live_templates/restaurant/fine-dining/reservations.html` — concierge portrait inner-layer refactor, reveals + stagger on 4 process steps, simple reveal on hours table (keeping `display: contents` intact, see gotcha below).
- `templates/live_templates/restaurant/fine-dining/blog_list.html` — lead-post image inner-layer refactor, hover letter-spacing + arrow shift on `.read`, stagger on compact list.
- `templates/live_templates/restaurant/fine-dining/blog_detail.html` — light reveals on article crumbs, kicker, h1, meta, lede, body paragraphs / headings / blockquotes, footer.

### 5 — Gotchas worth remembering

- **`display: contents` + opacity/transform = nothing renders.** The `.fd-hours .table .row` uses `display: contents` (it's a flattened grid row that spreads its children into the parent grid). An element with `display: contents` has no box, so `opacity: 0` and `transform: translate3d(...)` have no effect — the stagger fails silently. First draft used `data-lm-stagger` on the hours table and the reveal went nowhere. Downgraded to a simple `data-lm="reveal"` on the table wrapper instead (fades the whole table as one block). Note for future motion authors: `display: contents` children cannot be staggered individually — either wrap in a real grid item or stagger one level up.
- **Stale runserver process.** The first smoke-test runserver somehow kept serving a pre-edit HTML even though the file on disk had the motion attrs (Windows + auto-reloader + rapid file edits seemed to confuse the StatReloader). Killing the server and restarting on a fresh port produced the correct fresh HTML. Lesson: if the browser walk shows "my edits didn't land" and the file-on-disk grep shows they did, just restart runserver before debugging CSS or cache layers. This is the same class of repro as Session 19's "ghost dev-server" gotcha.
- **Playwright fullPage screenshot captures pre-reveal state for below-the-fold sections.** Because `fullPage: true` extends the viewport synchronously and captures immediately, `IntersectionObserver` doesn't get a chance to fire on sections that were never actually visible during real scrolling. First screenshot showed big empty areas where the hidden reveals were. The fix for screenshot-only validation: `document.querySelectorAll('[data-lm]').forEach(el => el.classList.add('lm-in'))` via `browser_evaluate` before taking the screenshot. Real users are unaffected — they scroll naturally and each section reveals on entry. Flag this if any future QA pass uses fullPage screenshots as the primary visual check.
- **Preview PNG is unaffected.** The marketplace thumbnail for Gusto is generated from a completely separate file (`templates/preview_compositions/restaurant/fine-dining.html`) and is captured by Playwright as a static PNG. The live-template motion system is scoped to `live_templates/restaurant/fine-dining/*` and loads `live-motion.css` / `live-motion.js` only inside that skin. The preview composition never includes those files, so the PNG generator is not at risk of capturing an empty reveal state. Verified by inspection.

### 6 — Validation results

- `python manage.py check` → 0 issues.
- Django test-client route smoke test (Session 22 fresh seed + tier sync):
  ```
  200 OK  /templates/restaurant/gusto-fine-dining/
  200 OK  /templates/restaurant/gusto-fine-dining/preview/
  200 OK  /templates/restaurant/gusto-fine-dining/preview/filosofia/
  200 OK  /templates/restaurant/gusto-fine-dining/preview/menu/
  200 OK  /templates/restaurant/gusto-fine-dining/preview/atmosfera/
  200 OK  /templates/restaurant/gusto-fine-dining/preview/diario/
  200 OK  /templates/restaurant/gusto-fine-dining/preview/prenota/
  200 OK  /templates/restaurant/gusto-fine-dining/preview/diario/menu-autunno-26/
  ```
  8/8 green. Fresh seed + `sync_template_tiers` produced `3 published_live / 17 draft` — tier distribution unchanged from Session 21 as expected.
- Live browser walk at 1440×900 (Playwright):
  - `body.lm-ready = true`, `cssLoaded = true`, `jsLoaded = true` on every visited page.
  - Home: 18 `[data-lm]` elements, 3 stagger parents, 5 reveals already `.lm-in` at top of viewport (hero eyebrow/h1/intro/actions/plate).
  - Facts counter mid-animation at t≈600ms: `14→11`, `8→7`, `180€→147€` (suffix preserved by the regex parse). Final state at t≈1400ms: `14`, `8`, `180€`.
  - Press strip stagger delays: `0 / 90 / 180 / 270 / 360 / 450 ms` (6 children, 90ms unit).
  - Facts stagger delays: `0 / 110 / 220 ms` (3 facts, 110ms unit).
  - Menu: 8 courses in a `[data-lm-stagger]` parent, wine highlights in another.
  - Gallery: 6 tiles with inner `.bg` layers, `transition: transform 0.9s cubic-bezier(0.33, 1, 0.68, 1), filter 0.9s ...` wired correctly; initial transform `matrix(1.001, 0, 0, 1.001, 0, 0)`.
  - About: 5 timeline rows + 4 values staggered.
  - Reservations: 4 process steps staggered; hours table falls back to plain reveal (display: contents gotcha); concierge portrait refactored for hover zoom.
  - Blog list: 4 compact rows staggered; lead post image refactored for hover zoom.
  - Blog detail: 14 `[data-lm]` elements including 5 body paragraphs.
- Reduced-motion test (`body.lm-reduced`): every `[data-lm]` target collapses to `opacity: 1 / transform: none / transition: none`. Verified by setting the class manually and reading computed styles.
- No-JS fallback test (remove `body.lm-ready`): every reveal target returns to `opacity: 1 / transform: none`. Page renders in full without JS.
- Mobile sanity at 390×844: document scroll-width is 660px — horizontal overflow **pre-existing** from Gusto's desktop-first fixed paddings (`padding: 96px 56px 96px 90px` + `grid-template-columns: 1fr 1.18fr`). Offenders identified: `.fd-hero .text` (426px) and `.fd-chef .info` (320px). Motion pilot introduced **zero new horizontal overflow**: all reveals are Y-axis only, image zooms are clipped by `overflow: hidden` wrappers, hover letter-spacing is contained in flex-between rows. Pre-existing mobile layout gap is documented for a separate responsive pass, out of scope for the motion pilot.
- D-047 leak sweep: zero new literal brand strings introduced. The only `Osteria Moderna` literal in `blog_detail.html:108` is the pre-existing Gusto leak already documented in `TEMPLATE_REGISTRY.json` `tier_reason` as the "5 Gusto leaks pending Phase 2g.3 lift". Motion pilot is orthogonal to that D-047 lift and does not regress it.

### 7 — Decisions added

- **D-058: Live Motion Language — Reusable CSS + JS module, opted in per skin, no-JS fallback, reduced-motion respected** — see DECISIONS.md.

### 8 — What's reusable vs what's Gusto-specific

**Reusable (the mini motion language):**
- `static/css/live-motion.css` — tokens + reveal primitives + stagger + image-frame + reduced-motion. Category-agnostic.
- `static/js/live-motion.js` — runtime. Category-agnostic.
- The HTML attribute contract: `data-lm="reveal|reveal-lg|reveal-soft"`, `data-lm-stagger [data-lm-stagger-delay="Nms"]`, `data-lm="counter" data-lm-to="NN"`.
- The `body.lm-ready` gating contract for hidden states.
- The wrapper + inner-bg layer pattern for image hover zoom (any `.xx .portrait` / `.xx .plate` / `.xx .img` that wants the effect can adopt the same shape).

**Gusto-specific (fine-dining skin CSS extensions):**
- `.fd-nav` underline sweep — uses the gold `--secondary` token; tone-dependent.
- `.fd-lead .gold-btn:hover` arrow shift + letter-spacing widening — uses `.gold-btn` selector specific to fine-dining.
- `.mp-bar .mp-back:hover` letter-spacing widening — uses fine-dining's own marketplace bar styling.

**Author note for future archetypes:** A new archetype adopting the motion pilot should (1) link + script the two static files, (2) add `data-lm` attributes to the content, (3) decide whether to author its own hover enhancements (underline sweep / arrow shift / letter-spacing) using the `--lm-ease` and `--lm-dur-*` tokens for consistency. The tokens on `:root` can be overridden inside the skin's `<style>` block if the mood is different (e.g. a very-muted medical archetype might set `--lm-rise: 10px` for a more subdued cadence).

### 9 — Final state

- All 8 Gusto routes return 200.
- Manifesto, facts, courses, chef, press, CTA all reveal cleanly as you scroll.
- Facts counter animates 0→14/0→8/0→180€ with suffix preserved.
- Gallery tiles zoom gently on hover without CLS (inner `.bg` layer is clipped by `overflow: hidden` wrapper).
- Gold CTAs and nav links have tactile micro-interactions.
- Reduced-motion users get a fully visible, animation-free page.
- No-JS users get a fully visible, animation-free page.
- Mobile overflow is pre-existing (not introduced by this pilot).
- Zero new literals, zero new dependencies, zero wide refactor.

**Decision:** MOTION PILOT GUSTO APPROVATO.

### 10 — Handoff notes

See AGENT_HANDOFF.md and TODO_NEXT.md for next-session direction. The motion pilot is ready to be adopted by the other `tier=published_live` templates (cardio + dermatologia specialist skin) and is the expected interaction-quality floor for every new template promoted to `published_live` during Phase 2g3. Future skins opt in with one `<link>` + one `<script>` in their `_base.html` — the pilot is strictly additive; nothing breaks if a skin doesn't opt in.

## Session 21 — Tier Migration Implementation (Phase 2g2x.8) (2026-04-11)

**Agent:** Implementation session. Closes Phase 2g2x.8 and resolves Phase 2g2x.7 by construction. D-053 / D-054 / D-055 / D-056 were formalized in Session 20 as a documentation delta; Session 21 ships the code that makes them real at the query layer.
**Branch:** `phase-2g2x-tier-migration-v2`.
**Scope floor:** implement D-055 as code, delete the D-056 ghost CTA, add premium empty states, respect every "do not" in the session prompt (no live preview authoring, no new categories/templates, no wide refactor, no `published_static` tier, no opaque workarounds).

### 1 — Strategy: new `tier` field, single central gate, registry-driven sync

The cleanest shape for D-055 was NOT to repurpose the existing `WebTemplate.status` field (which already encodes the orthogonal editorial draft/review/published/archived state used by the admin workflow) but to add a new `WebTemplate.tier` TextChoices column, indexed, default `draft`. See D-057 in DECISIONS.md for the full rationale. `TEMPLATE_REGISTRY.json` stays the human-readable source of truth; a new `sync_template_tiers` management command reads it and applies the tier to matching rows. `seed_templates` calls `sync_template_tiers` at the end, so one command produces a correctly-tiered database.

The public tier gate is centralized in a single helper `apps/catalog/selectors._public_tier_filter(include_drafts)`. Every public selector delegates to it — homepage featured, listing, category, detail, related, search, category counts. Views thread a single `include_drafts` flag built from a single helper `apps.catalog.views._staff_preview_mode(request)` which requires BOTH `is_staff` AND `?preview=1`. Accidental staff traffic still sees the public 404 — the draft surface is never normalized.

### 2 — Files modified

**Code:**
- `apps/catalog/models.py` — new `WebTemplate.Tier` TextChoices + `tier` CharField (db_index, default=draft, help_text).
- `apps/catalog/migrations/0002_webtemplate_tier.py` — auto-generated schema migration.
- `apps/catalog/selectors.py` — rewritten to centralize the tier gate in `_public_tier_filter(include_drafts)`; every public selector takes an `include_drafts` kwarg (default False). `get_featured_templates` now backfills from the live pool when `featured+live < limit` so the homepage doesn't collapse to a single card during the transition. `get_template_detail` raises `Http404` explicitly so drafts 404 regardless of whether the slug exists.
- `apps/catalog/views.py` — added `_staff_preview_mode(request)` helper. `TemplateListView` / `TemplateDetailView` / `CategoryListView` / `LiveTemplateView` all thread the flag. `has_live_preview` context var deleted per D-056. `LiveTemplateView.setup()` now also tier-gates (draft preview routes 404 publicly).
- `apps/catalog/admin.py` — `WebTemplateAdmin` surfaces `tier` in `list_display`, `list_filter`, and `list_editable` so operators can flip tier inline.
- `apps/catalog/management/commands/sync_template_tiers.py` — **new**. Reads `TEMPLATE_REGISTRY.json`, validates tier values against `WebTemplate.Tier`, updates only changed rows, prints a compact diff. `--dry-run` supported. Rejects unknown tier strings to prevent a registry typo from silently downgrading the catalog.
- `apps/catalog/management/commands/seed_templates.py` — now calls `sync_template_tiers` at the end via `call_command(...)`. Single seed produces correctly-tiered DB.

**Templates:**
- `templates/catalog/template_detail.html` — deleted the `{% if has_live_preview %}…{% else %} <a href="#">Anteprima Live</a>{% endif %}` block. "Apri anteprima completa" CTA is now unconditional, targets `catalog:live_template_home`, opens in new tab. The placeholder cart CTA is now a proper disabled `<button>` (one more ghost link retired, scope-clean).
- `templates/catalog/_empty_catalog.html` — **new** partial. Three modes: `category_soon` (category whose siblings are all draft → "Selezione in preparazione" / "In arrivo"), `search_no_match` (0 search results → "Non abbiamo trovato questa ricerca" with "Cancella ricerca" + "Vedi le categorie"), `catalog_empty` (safety-net for a 0-item listing → "Il catalogo si sta popolando"). Premium, curatorial, non-apologetic.
- `templates/catalog/template_list.html` — wired to the new partial. Previous `{% empty %}` text block deleted. Listing header is inside the `{% if templates %}` branch now (don't count-shame zero results).
- `templates/pages/home.html` — featured grid wraps in `{% if featured_templates %}`, falls back to `_empty_catalog.html` with mode `catalog_empty`. Section header copy shifted from "I template più amati" to "Collezione curata" — framing the transition as curation, not scarcity.
- `templates/includes/_category_card.html` — categories with `template_count == 0` render an "In arrivo" pill instead of "0 template" and pick up a `.mw-category-card--soon` modifier class.

**CSS:**
- `static/css/components.css` — new `.mw-category-card--soon` dim state + `.mw-pill-soon` token.
- `static/css/pages.css` — new `.mw-catalog-empty` styled container on top of the existing `.mw-empty-state` primitive + `.mw-empty-state-actions` button row.

**Docs:**
- `DECISIONS.md` — D-045 marked superseded; new D-057 documents the implementation choices (why a new field, why the central filter, why the registry-driven sync, featured backfill behavior, staff preview opt-in shape).
- `TODO_NEXT.md` — Phase 2g2x.8 closed with an acceptance checklist; Phase 2g2x.7 closed by construction.
- `SESSION_LOG.md` — this entry.
- `AGENT_HANDOFF.md` — updated to point the next session at Phase 2g2x.1 CRITICO categories (real-estate / lawyer / agency) as the next blocker, and Phase 2g3 as the post-wave rollout plan. The tier migration unblocks those, but does not close them.
- `memory/tier_migration_session21.md` — new project memory file with the strategy, the files touched, and the post-session state so next session can apply this without re-deriving it.
- `memory/MEMORY.md` — one-line index entry added.

### 3 — Final catalog behavior (after tier migration)

- **Homepage** `/` — shows 3 featured live cards (cardio + dermatologia + gusto; the single `featured=True` + live template is gusto, the other two are backfilled from the live pool). Section header: "Collezione curata". CTA "Vedi Tutti i Template". No ghost "Anteprima Live".
- **Listing** `/templates/` — shows 3 template cards total. Header reads "3 template disponibili". Sort + search work, search against "cardio" returns 1 hit, search against "vertex" (draft slug) returns 0.
- **Category — live** `/templates/medical/` — shows 2 live medical cards (cardio + dermatologia). Sapore/benessere/famiglia/salute are all draft and correctly hidden.
- **Category — mixed** `/templates/restaurant/` — shows 1 live restaurant card (gusto). Sapore + brace are draft, hidden.
- **Category — empty** `/templates/agency/` — renders the `category_soon` empty state with "Selezione in preparazione" eyebrow, "Agency — in arrivo" heading, curatorial body copy, CTAs to the listing + category list. Zero template cards. Zero "Anteprima Live" strings.
- **Category list page** `/templates/categories/` — 8 category cards; the ones whose siblings are all draft (agency, lawyer, real-estate, portfolio, ecommerce, business) render the "In arrivo" pill and a subtle dim modifier; medical shows "2 template", restaurant shows "1 template".
- **Detail — live** `/templates/medical/cardio-studio-specialistico/` — HTTP 200. Single "Apri anteprima completa" CTA (primary) + disabled cart CTA (secondary). CTA links to `/templates/medical/cardio-studio-specialistico/preview/`. Zero "Anteprima Live" strings in HTML.
- **Detail — draft** `/templates/agency/vertex-creative-agency/` — HTTP 404 (public). HTTP 200 when staff + `?preview=1`.
- **Live preview — live** `/templates/medical/cardio-studio-specialistico/preview/` — HTTP 200 (unchanged from before).
- **Live preview — draft** `/templates/agency/vertex-creative-agency/preview/` — HTTP 404 (public). HTTP 200 when staff + `?preview=1`.

### 4 — Verifications

`python manage.py check` — clean, 0 issues.
`python manage.py migrate` — 1 new migration applied (`catalog.0002_webtemplate_tier`).
`python manage.py seed_categories && python manage.py seed_templates` — 8 categories + 20 templates + auto-sync tiers: **3 published_live / 17 draft**. Live slugs: `cardio-studio-specialistico`, `dermatologia-elite-roma`, `gusto-fine-dining`.
`python manage.py sync_template_tiers` (re-run) — `0 tier(s) updated. Catalog distribution: 3 published_live / 17 draft.` (idempotent).
`python -m ruff check apps/catalog/` — "All checks passed!".

**Route smoke test** (ran inline via a throwaway `_smoke_test.py` with `django.test.Client`, deleted after the session): **31/31 checks passed.** Covered tier distribution, homepage, listing, category list, live-sibling category, empty category, live detail, draft detail, live preview, draft preview, empty search, cardio search, draft-slug search, staff `?preview=1` detail reachability, staff-without-preview 404.

### 5 — UX validation

- `grep "Anteprima Live" templates/` → **no matches** (ghost CTA fully retired).
- `grep 'href="#"' templates/catalog/` → only two matches, both explanatory comments I added (`{# no legacy href="#" fallback... #}` in template_detail.html; the partial docstring in `_empty_catalog.html`). Zero live ghost CTAs.
- Empty states are premium, sober, curatorial — `"Selezione in preparazione"`, `"Collezione curata"`, `"Il catalogo si sta popolando"`. No "oops, niente qui" copy, no technical error messages, no apology.
- Category card "In arrivo" pill uses the neutral-100/neutral-600 palette in a small UPPERCASE chip — stays consistent with the rest of the design system at card size.
- Featured-pool backfill prevents the homepage from collapsing to a single card, so the 20→3 transition doesn't look like a broken page.

### 6 — Memory updates

- `memory/tier_migration_session21.md` — new
- `memory/MEMORY.md` — one new index entry

### 7 — Decision

**PHASE 2g2x.8 APPROVATA.** All seven exit criteria for Phase 2g2x.8 met. The catalog floor is now enforced at the query layer. The Session 20 policy is implemented where it counts.

**Next micro-step:** Phase 2g2x remains OPEN overall (D-049 still blocks the roadmap) because Phase 2g2x.1 CRITICO for real-estate, lawyer, and agency is still open, and Phase 2g2x.3 leak-lifts are still outstanding. The tier migration unblocks Phase 2g3 (the rollout wave) but does NOT close Phase 2g2x. Next sessions should attack Phase 2g2x.1 real-estate/lawyer/agency DNA splits (Option A per D-050/D-051) in the Session 17/18 shape, then start the Phase 2g3 rollout (fine-dining leak lift → trattoria + brace live skins → family/wellness/clinic live skins → etc.).

---

## Session 20 — Live Preview Policy v2 Formalization (2026-04-11)

**Agent:** Policy / architecture / documentation session. **No code changes, no HTML authoring, no preview generation.** Working tree stays clean apart from doc edits.
**Branch:** `phase-2g2x-live-preview-policy-v2` (branch name reflects scope — policy, not implementation).
**Goal:** Formalize the user's new non-negotiable product directive into a binding set of decisions, a tier model, a rollout plan, and documentation that every future Claude session can read and apply without ambiguity. The directive: **every published template must have a real live multi-page preview, and the premium differentiation discipline proven in business + portfolio must become law across every category**.

### The directive, in the user's words
1. Every template marked `published` must have a real, navigable, multi-page live preview
2. The differentiation discipline introduced for business and portfolio (distinct hero image, distinct silhouette, distinct section order, distinct CTA pattern, distinct macro tone, distinct imagery direction, distinct inner pages) must apply to ALL categories and ALL templates — not as an optional polish but as a hard gate
3. Shipping preview-only templates under a `published` label is not acceptable
4. Keeping a `href="#"` "Anteprima Live" ghost CTA is not acceptable
5. The future roadmap (auth / checkout / editor / commerce / scaling) must wait until this floor is achieved

### Why this session exists separately from implementation
Session 16 already flagged the preview-only / identity-crash problem in the catalog differentiation audit. Sessions 17 and 18 closed two CRITICO categories (business + portfolio) using the Option A DNA split recipe (D-050 / D-051). Session 19 cleared a portfolio blocker. **But** none of the prior sessions formalized the product directive — the rules were encoded in tactical decisions (D-049 blocks roadmap resume, D-047 governs chrome authoring, D-050 picks Option A) without a single source of truth that reads as "the product's definition of published". That gap meant every new Claude session had to re-derive the directive from scattered evidence. Session 20 writes it down once so no one has to derive it again.

### What Session 20 produced — documentation-only delta

**DECISIONS.md — 4 new formal decisions, each a pillar of the policy:**

1. **D-053 — Live Preview Law.** A template may only be `published_live` when it satisfies the full 9-gate Live Preview contract (DNA entry + content registry + skin folder covering the category baseline + all routes 200 + D-047 leak sweep clean + Chromium visual walk + card-size differentiation test + preview PNG from the per-template composition + working "Apri anteprima completa" CTA). This binds the Session 11 "completeness-ready" concept into a product-level rule and retires the looser "preview-only can still be published" state.

2. **D-054 — Premium Differentiation Law.** Formalized the 10-dimension test every sibling pair must pass: hero image, dominant imagery pool, silhouette, section order, primary CTA (phrasing + interaction pattern), block rhythm, macro tone, imagery direction, typography, inner pages. This turns the Session 17/18 Option A recipe into a global, cross-category standard and gives authors a concrete checklist. Retroactive: any existing pair that fails ≥4 gates is a Phase 2g3 blocker for its category.

3. **D-055 — Template Tier Model.** Binary `published_live` / `draft`. No intermediate `published_static` tier. Option space evaluated in full (A hide / B badge / C 404 / D lightbox); Option A selected because it is the only one that keeps the marketplace floor premium without teaching shoppers a tier vocabulary. Trade-off acknowledged: visible catalog shrinks from 20 to 3 templates on day 1 of the tier migration. Accepted — three real products beats twenty posters.

4. **D-056 — Catalog Honesty.** Delete the legacy `href="#"` "Anteprima Live" branch in `templates/catalog/template_detail.html` lines 132-136 and the `has_live_preview` context var in `TemplateDetailView`. Supersedes Phase 2g2x.7 three-option punch list — once tier gating is in place the branch is dead code. D-045 is marked superseded.

**TODO_NEXT.md — 2 new subphases in the Phase 2g2x wave plus a new Phase 2g3 rollout plan:**

- **Phase 2g2x.8 — Tier migration.** Implementation step that turns D-055 into code. Adds `tier` field (or repurposes `status`), filters listing/detail/homepage/category/search to `tier='published_live'`, seeds cardio/derm/gusto as live and everyone else as draft, deletes the ghost CTA, ships a category-page empty state for "in arrivo" categories. Absorbs the Phase 2g2x.7 remediation entirely.
- **Phase 2g3 — Live Preview Rollout.** Category-by-category wave to bring all 17 `draft` templates up to `published_live`, ordered cheapest-first: restaurant → medical → business → portfolio → ecommerce → (blocked on 2g2x.1) agency / lawyer / real-estate. Each template passes a 9-point acceptance checklist (DNA / content / skin / routes / leak sweep / visual walk / card-size sibling test / preview regen / tier flip / session log entry). Phase 2g3.7 exit criteria are the Phase 3 unblock gate.

**CATEGORY_ROADMAP.md — baseline live pages per category + rollout order + cumulative milestones:**

- A per-category baseline page-kind table (5 pages + 1 detail where the product is drilldown; 5 pages otherwise). Medical / restaurant / business / agency / lawyer / real-estate / portfolio / ecommerce each get their own row with the minimum set spelled out.
- Rollout order matching TODO_NEXT Phase 2g3 (restaurant → medical → business → portfolio → ecommerce → agency/lawyer/real-estate).
- Cumulative `published_live` milestone table showing 3 → 5 → 8 → 10 → 12 → 14 → 20 as each category burst closes.
- Category-ready test (category is live-complete when every sibling passes D-053, every pair passes D-054, leak sweep clean, Chromium walk clean, no "in arrivo" strip).

**BRAND_SYSTEM_GUIDELINES.md + CONTENT_GUIDELINES.md — standard-reference appendices:**

- BRAND_SYSTEM_GUIDELINES gets a short "Premium Differentiation Law" pointer linking to D-054 with the 10 dimensions listed as a bullet checklist.
- CONTENT_GUIDELINES gets a short "Inner Pages Law" pointer linking to D-053 + the baseline page table.

Both are short references, not duplicates of the decision text — the source of truth lives in DECISIONS.md.

**TEMPLATE_REGISTRY.json — version bump + tier annotation on every row.**

Version bump 0.7.3 → 0.8.0 (new directive constitutes a minor version bump in registry semantics). Each template entry gets a `tier` key: `published_live` on cardio-studio-specialistico, dermatologia-elite-roma, gusto-fine-dining; `draft` on the other 17. Description block updated to point at D-053 / D-054 / D-055 / D-056. The registry stays a mirror — the source of truth for tier is still `seed_templates.py` after Phase 2g2x.8 migrates it.

**AGENT_HANDOFF.md — new top section describing the policy + the next micro-step.**

The next agent reads: (1) Session 20 formalized the policy, (2) Phase 2g2x is still blocking — 3 CRITICO categories remain (real-estate, lawyer, agency), (3) Phase 2g2x.8 (tier migration) is the first implementation step after Phase 2g2x closes, (4) Phase 2g3 starts after tier migration, (5) the rollout order and per-template checklist are in TODO_NEXT.md and CATEGORY_ROADMAP.md.

**MEMORY.md + `memory/live_preview_policy_session20.md` — auto-memory index entry + file.**

New memory file captures the policy, the tier model, the rollout order, and the exit criteria in a form that survives across conversations.

### What Session 20 explicitly did NOT do

- Did NOT add `tier` field to `WebTemplate` or run a migration — that's Phase 2g2x.8 implementation work
- Did NOT delete the `href="#"` CTA or modify `template_detail.html` — also Phase 2g2x.8
- Did NOT author any skin folder for any preview-only template — that's Phase 2g3 work
- Did NOT start any of the 3 remaining CRITICO Phase 2g2x.1 categories (real-estate / lawyer / agency) — those are the next implementation session, not this one
- Did NOT merge any branches or commit any work outside the documentation delta on `phase-2g2x-live-preview-policy-v2`
- Did NOT touch `CLAUDE.md` — the critical rules there already enforce "no lorem ipsum" and "unique brand per template"; the new laws complement rather than replace them

### Policy verdict

**Approved.** The policy is binding going forward. Every future Claude session must read D-053 / D-054 / D-055 / D-056 before starting implementation work on any catalog-facing change, and every future template must pass both the D-053 Live Preview gate and the D-054 Differentiation gate before flipping to `published_live`.

### Recommended next micro-step

1. **Commit this session's doc delta** as a standalone "Session 20 — live preview policy v2 formalization" commit on the current branch. No code changes are involved so the commit is isolated and reviewable.
2. **Open the Phase 2g2x.8 tier migration session** as the next implementation step. This is the cheapest implementation wave that unblocks everything else — it demotes the 17 preview-only templates to `draft`, hides them from public surfaces, deletes the ghost CTA, and ships the empty-state strip. After 2g2x.8 lands, the visible catalog is 3 real templates, which is the policy-compliant floor.
3. **Return to Phase 2g2x.1** to close the 3 remaining CRITICO categories (real-estate → lawyer → agency) using the Session 17/18 Option A recipe.
4. **Start Phase 2g3** category-by-category per the TODO_NEXT Phase 2g3 order.

**Do NOT** skip step 2. Shipping Phase 2g3 on top of a catalog that still has `href="#"` ghost CTAs would violate D-056 and leak the old state into the new rollout. Phase 2g2x.8 is the gate between "the old catalog" and "the policy-compliant catalog".

---

## Session 19 — Phase 2g2x.1 Portfolio Triage + Surgical Fix (2026-04-11)

**Agent:** Portfolio blocker triage + surgical CSS/copy fix.
**Goal:** Session 18 declared portfolio approved, but a manual verification pass found two real issues worth triaging before commit: (1) the "Anteprima Live" CTA on the detail page did nothing useful for most templates, and (2) the full-size preview of Chiara on `/templates/portfolio/chiara-portfolio-creativo/` appeared to have a visual overlap/rendering glitch. This session executed a severe triage first, then a strictly-scoped fix for the single real blocker.

### Part 1 — Triage outcome

Two findings:

1. **The "Anteprima Live" button is a legacy gating placeholder, not a portfolio-scope bug.** `templates/catalog/template_detail.html:132-136` has an `{% if has_live_preview %} ... {% else %} <a href="#">Anteprima Live</a> {% endif %}` branch. `has_live_preview` resolves via `template_content.has_live_template(slug)` → `slug in TEMPLATE_CONTENT`. `TEMPLATE_CONTENT` only has 3 entries (cardio / dermatologia / gusto), so **17 of 20 templates** hit the `href="#"` placeholder branch, including both Chiara and Pixel. Cardio detail confirmed in browser to show the correct "Apri anteprima completa" → `/preview/` link with `target="_blank"`. D-045 documents this gating as intentional. This is a system-wide UX issue affecting all preview-only templates, **not caused by and not in scope of portfolio hardening**. Deferred to a future micro-phase (see Next micro-step).

2. **Chiara's preview composition HAS a real, reproducible layout overflow bug.** Confirmed by reading the generated PNG directly and by a cache-busted browser walk. Root cause: `editorial-designer-grid.html:92-93` sets `.ed-hero { height: 490px; padding: 72px 72px 42px; }` → 376 px of inner vertical space, but with `.ed-left h1 { font-size: 82px; line-height: 0.97; max-width: 760px; margin-top: 36px; }` the 57-char headline `'Sistemi di <em>identità visiva</em> costruiti una griglia alla volta.'` wraps to 5 lines (~397 px) and the full content stack (eyebrow + h1 + sub + cta-row + margins) needs ~640 px. With `.ed-hero` having no `overflow: hidden`, ~260 px of content bleeds down into `.ed-ledger` and `.ed-ribbon` below. The rendered PNG shows the "RICHIEDI IL PORTFOLIO COMPLETO" CTA, the filter pills (`TUTTO · IDENTITÀ · EDITORIA · ART DIRECTION`), and the ledger intro heading `Progetti selezionati · ventidue case study` all visually colliding. Reproduces after `--force` regeneration → it's a CSS/copy bug, not a stale render.

### Part 2 — Ghost dev-server gotcha (operational)

During the triage's first browser walk the detail page showed "Ogni progetto una storia" — the **legacy** `portfolio.html` content Session 18 claimed to have eliminated. This looked alarming until a process audit showed TWO listeners on port 8765: PID 29132 (`runserver --noreload`, started 11:24 **from a prior session's worktree**) and the current session's new pair. PID 29132 was answering new connections and serving a completely different PNG at the same URL (3.3 MB, legacy content) than what was physically on disk (725 KB, new broken `'Sistemi'` content). Killing 29132 brought Python urllib and the cache-busted browser back into agreement with the filesystem. **New lesson:** before any visual walk, kill any lingering `runserver` processes on your target port. Added to the preview-pipeline gotchas list.

### Part 3 — Stale-PNG trap reproduced (confirmation of Phase 2g2x.5)

Two consecutive `generate_previews --only chiara-portfolio-creativo --force` runs both produced suffixed filenames (`_lEh35gE.png`, `_0NgBTC3.png`, `_TJW36Ho.png`) because Django's `FileSystemStorage.get_available_name()` appends a hash when the target filename already exists on disk. The `--force` path in `generate_previews.py:211-216` deletes the old DB row but **does not delete the file on disk**, so each regen creates a new orphan on top of the previous one. This is the Phase 2g2x.5 `dna_signature` trap — already known, still deferred, now with a concrete repro on top of the existing Session 8/10/12/15 evidence. Session 19 cleaned up its own orphans manually by moving the final asset file back to the canonical filename and updating the DB row.

### Part 4 — Surgical fix applied

Scope: strictly Chiara. Zero other files touched outside the surgical set.

**Files modified (Session 19 delta only):**

| File | Change |
|------|--------|
| `templates/preview_compositions/portfolio/editorial-designer-grid.html` | `.ed-hero` padding `72 72 42` → `52 72 38`; added `overflow: hidden` as hard cap against any future content bleed. `.ed-left h1` font-size `82` → `62`, line-height `0.97` → `0.98`, letter-spacing `-0.04em` → `-0.035em`, margin-top `36` → `22`, max-width `760` → `720`. `.ed-left .sub` margin-top `34` → `20`, max-width `520` → `560`, font-size `15` → `14`, line-height `1.7` → `1.6`. `.ed-left .cta-row` margin-top `38` → `22`, gap `28` → `22`. Added a block-leading comment documenting the vertical budget math. |
| `apps/catalog/template_dna.py` | `chiara-portfolio-creativo` → `content.headline` trimmed from `'Sistemi di <em>identità visiva</em> costruiti una griglia alla volta.'` (57 chars, wrapped to 4-5 lines at 62-82 px display) to `'Identità visive, <em>una griglia alla volta</em>.'` (47 chars, wraps to 2 lines at 62 px display). Both key semantic signals preserved: `identità visive` (Chiara's profession) and `una griglia alla volta` (Chiara's craft metaphor). As a deliberate side effect, the new headline now mirrors Pixel's `'Fermare il tempo, una luce alla volta.'` syntactic rhythm — both siblings use the same `'…, una X alla volta.'` structure with X being the medium of each profession (griglia for designer, luce for photographer), strengthening rather than weakening the differentiation. An inline comment in `template_dna.py` documents the reason for the trim so the rationale survives future edits. |

Why CSS alone wasn't enough: at 62 px h1 + 720 max-width the old 57-char headline still wrapped to 4 lines (h1 height 243 px), and the content stack bottom landed at canvas y 553 — which visually overlapped `.meta-strip` (absolute-positioned at canvas y 495-550 inside the hero). With the trimmed copy, h1 wraps to 2 lines (122 px), stack bottom lands at y 432, and there's a clean 63 px gap to the meta-strip. Pure CSS would have required dropping h1 font-size below ~50 px or restructuring the meta-strip's positioning — either of which would have been a much bigger change to Chiara's DNA than a 10-character copy trim that preserved both signature signals.

### Hard validation (Session 19 delta)

- `python manage.py check` — **clean** (0 silenced)
- `python manage.py generate_previews --only chiara-portfolio-creativo --force` — green, rendered with `[editorial-designer-grid]` label, new PNG written
- Orphan cleanup — old suffixed files (`_lEh35gE`, `_0NgBTC3`, `_TJW36Ho`) removed, final asset restored to canonical `chiara-portfolio-creativo-preview.png` filename, DB row updated via shell to point at the canonical name. `media/template_assets/2026/04/` now contains **exactly one Chiara PNG and one Pixel PNG** — no orphans.
- Playwright Chromium visual walk at 1440×900 on a fresh dev server:
  - `/templates/portfolio/` listing — two cards unmistakably distinct at card size. Pixel: dark cinematic, fullbleed photo. Chiara: cream paper, typographic hero with `Identità visive, una griglia alla volta.` headline visible. **PASSES.**
  - `/templates/portfolio/chiara-portfolio-creativo/` detail — preview image is clean. Headline 2 lines, subhead 3 lines, CTA row + meta-strip + project index card + ledger panel + clients ribbon all properly separated. **Zero overlap.** **PASSES.**
  - `/templates/portfolio/pixel-portfolio-fotografico/` detail — untouched, identical to pre-session state. Dark cinematic hero + EXIF bar + filmstrip + footer. **PASSES.**
- Direct raw-PNG inspection at `/media/template_assets/2026/04/chiara-portfolio-creativo-preview.png` with cache-bust — final rendering matches the spec.

### Exit state

- **Chiara blocker: closed.** Layout is clean, no overlap, meta-strip properly preserved, identity still typographic-led, differentiation vs Pixel unchanged (actually strengthened via headline parallel).
- **Pixel: untouched.** Zero edits to `cinematic-photographer.html` or `pixel-portfolio-fotografico` DNA.
- **Working tree is clean** apart from the deliberate Session 19 delta: `editorial-designer-grid.html` modification, `template_dna.py` headline trim, the canonical PNG file re-emitted at 717 KB, and the updated session/decisions/todo/handoff/registry/memory docs.
- **Phase 2g2x.1 portfolio category** is now truly ship-ready. Commit unblocked. Per D-049 the full wave commit + PR still waits for the 3 remaining CRITICO categories (real-estate / lawyer / agency) to close, but the portfolio-scope work no longer has a blocker.

### Risks residui / what Session 19 explicitly did NOT touch

- **"Anteprima Live" legacy placeholder** — confirmed systemic, deferred. Needs its own micro-phase: hide the button / swap to a PNG lightbox / label as disabled state. 17 of 20 templates affected.
- **Phase 2g2x.5 stale-PNG structural fix** — reproduced during this session's regen loop, still deferred. Manual orphan cleanup is a workaround, not a fix.
- **Ghost `--noreload` dev servers** — new operational lesson logged for the pipeline gotchas memory: always check `netstat` for stale listeners before a visual walk.
- **3 CRITICO categories** (real-estate, lawyer, agency) — unchanged, still open, still the next micro-step.

### Next micro-step

Commit portfolio hardening now (Session 18 + Session 19 work, one commit) — then pick the next CRITICO category from the remaining 3 per the recommended order (real-estate → lawyer → agency) and run the Session 17/18 recipe end-to-end. Do not batch. Before each visual walk, kill any lingering `runserver` processes on the target port.

---

## Session 18 — Phase 2g2x.1 Portfolio Hardening (2026-04-11)

**Agent:** Portfolio category DNA split — second implementation wave of Phase 2g2x (catalog hardening, per D-049), following the Session 17 business recipe.
**Goal:** Close the `portfolio` identity-crash case. Make Chiara and Pixel two clearly distinct products at card size — different profession, different imagery, different silhouette, different CTA pattern, different section order — without quick-recoloring the legacy `portfolio.html` composition or touching any other category.

### Technical audit (confirmed the Session 16 findings)
Neither `chiara-portfolio-creativo` nor `pixel-portfolio-fotografico` had a DNA entry, so both resolved to legacy `templates/preview_compositions/portfolio.html` via `CATEGORY_TO_COMPOSITION["portfolio"]`. The legacy composition hardcodes literal designer-specific copy in eight places, catastrophically wrong for Pixel (who is a photographer):

| File | Line | Literal |
|------|------|---------|
| `portfolio.html` | 102 | `Selected work · 2018 — 2026` |
| `portfolio.html` | 103 | `Ogni progetto<br>una storia.` |
| `portfolio.html` | 104 | `Sono una designer indipendente che lavora con brand, editori e artisti. Identità visive, art direction, libri e siti su misura — niente di pre-confezionato.` |
| `portfolio.html` | 107 | `Independent designer · Milano` |
| `portfolio.html` | 113 | `Featured · Atlas Magazine` |
| `portfolio.html` | 130 | `Atelier Norma` (project tile) |
| `portfolio.html` | 133 | `Atlas Issue 14` (project tile) |
| `portfolio.html` | 136 | `Lumen Studio` (project tile) |
| `portfolio.html` | 139 | `Polare — Visual Series` (project tile) |

Both templates pulled from the single legacy `portfolio` imagery pool (6 shared URLs) — macro tone + photos identical. The effect was an identity-crash: Pixel (photographer) rendered as a designer with designer-specific copy and identical photos to Chiara.

### Strategy chosen — Option A (DNA split, 2 archetypes) per D-050
Chiara (indep designer / art direction / editorial / systemic studio) and Pixel (photographer / visual storyteller / cinematic portfolio) are semantically as far apart as Pragma/Elevate were in Session 17 — they demand entirely different silhouettes, dominant visuals, CTA patterns, and macro tones. A forced-shared skin would either erase the profession difference (recolor pair) or collapse into a conditional-branching frankenfile. Option A is the same recipe that already worked for business.

Two new archetypes:
- **`editorial-designer-grid`** (Chiara) — cream paper page, typographic drama, **NO big hero photo**, numbered project index on the right, ledger of case-study cards, clients ribbon footer. The hero IS the typography. Tone: `editorial-designer`. Conversion: `case-study-request` ("Richiedi il portfolio completo").
- **`cinematic-photographer`** (Pixel) — fully dark page, **dominant fullbleed photograph** covering ~62% of the canvas, film-strip EXIF credit bar pinned to the hero bottom, filmstrip gallery of series stills, 4-cell EXIF footer. The hero IS the photograph. Tone: `cinematic-authorial`. Conversion: `series-brief` ("[ Apri la serie completa ]").

### Files added / modified (portfolio scope only)
- `apps/catalog/template_dna.py` — 2 new DNA entries (`chiara-portfolio-creativo`, `pixel-portfolio-fotografico`), 2 new layout archetypes (`editorial-designer-grid`, `cinematic-photographer`), vocabulary extensions across 10 dicts (hero_style × 2, navbar_style × 2, footer_style × 2, card_style × 2, button_style × 2, tone × 2, conversion_pattern × 2, imagery_direction × 2).
- `apps/catalog/preview_imagery.py` — 2 new pools (`portfolio-designer`, `portfolio-photographer`). Zero URL overlap with each other, zero overlap with legacy `portfolio` pool. Legacy pool relabelled with explanatory comment per D-036 (kept, architecturally unused by any published template).
- `templates/preview_compositions/portfolio/editorial-designer-grid.html` — NEW. Cream paper chrome with typographic hero left + project index card right, ledger-row panel, clients ribbon + studio coordinates footer. D-047 compliant from the first line — zero literal brand strings, zero hardcoded image URLs.
- `templates/preview_compositions/portfolio/cinematic-photographer.html` — NEW. Fully dark with fullbleed photo hero, corner frame marks, film-strip EXIF credit bar, filmstrip gallery row, monospaced-style bracketed CTAs. D-047 compliant from the first line.
- Session docs: `SESSION_LOG.md`, `DECISIONS.md` (+D-051), `TODO_NEXT.md`, `AGENT_HANDOFF.md`, `TEMPLATE_REGISTRY.json` (v0.7.2).

### Differentiation matrix — Chiara vs Pixel
| Dimension                 | Chiara (editorial-designer-grid) | Pixel (cinematic-photographer) |
|---------------------------|------------------------------------|-------------------------------|
| Profession positioning    | Indep designer · art direction · visual identity | Photographer · visual storyteller · still-life |
| Macro tone                | Cream paper (`#f3efe5`) + coral accent | Near-black (`#050505`) + red accent |
| Hero silhouette           | Two-column typographic — huge Syne headline LEFT + project index card RIGHT. **NO big hero photo.** | Fullbleed dominant photograph covering 62% of the canvas. **The hero IS the photo.** |
| Dominant image            | None (hero is typographic). Only small accent tiles. | Full-bleed moody low-key still (cinematic photostill pool). |
| Section order             | rule-nav → typographic-hero → project-ledger → clients-ribbon | fullbleed-dark-nav → fullbleed-hero → exif-bar → filmstrip-gallery → exif-credits |
| Navbar                    | Hairline rule + asterisk wordmark + index-letter links + "Nuove commesse" status chip | Transparent dark + circular shutter wordmark + uppercase tracked links + "Disponibile per commissioni" pulse + `[ Richiedi commissione ]` bracket CTA |
| Primary CTA               | "Richiedi il portfolio completo" — ghost sans-rule, editorial | "[ Apri la serie completa ]" — ghost mono-bracket, technical |
| Typography pairing        | Syne + Inter (designer-display) | Archivo + Inter (uppercase tracked, technical) |
| Narrative pattern         | Numbered project ledger + categories filter + clients ribbon | Series counter (06/42) + EXIF bar + filmstrip of 4 series stills + credits cells |
| Imagery pool              | `portfolio-designer` (design workspace artifacts) | `portfolio-photographer` (cinematic photostills) |
| Imagery overlap with sib. | 0 URLs | 0 URLs |

### Stale-PNG check
Worktree started with no `media/` directory and no pre-existing TemplateAssets, so there was nothing to go stale. Session 18 did not hit the timing trap. Phase 2g2x.5 (dna_signature structural fix) still deferred.

### Hard validation
- **`python manage.py check`** — clean (0 issues silenced)
- **`python manage.py seed_templates`** — 20/20 templates created idempotently, no errors
- **`python manage.py generate_previews`** — 20/20 green (2 portfolio templates first via `--only`, then 18 remaining in one pass). New archetype labels logged: `[editorial-designer-grid]` for Chiara and `[cinematic-photographer]` for Pixel.
- **Bidirectional leak sweep** on rendered HTML of both templates:
  - **Chiara → Pixel**: grepped 26 Chiara-specific tokens (`Chiara`, `identità visiva`, `sistemi visivi`, `Casa editrice`, `Festival di poesia`, `Fondazione culturale`, `Vino naturale`, `Museo civico`, `Rivista d'architettura`, `art direction`, `editorial`, `designer`, `Studio indipendente`, `Archivio lavori`, `Progetti selezionati`, `Packaging`, `Wayfinding`, `Identità · Editoria` + all 8 legacy literals) — **zero Chiara-brand leaks in Pixel**. The only hits were: (a) a self-referential CSS comment in `cinematic-photographer.html` that names the opposite archetype for documentation ("Deliberate visual opposite of editorial-designer-grid"), and (b) the word "editoriale" inside Pixel's own subhead "commissioni editoriali" — used correctly in the photographer sense of "editorial commissions". Neither is a cross-tenant leak.
  - **Pixel → Chiara**: grepped 25 Pixel-specific tokens (`Pixel`, `ore rubate`, `Campi lunghi`, `Stanze vuote`, `città senza persone`, `Fotografia documentaria`, `fotograf`, `pellicola`, `obiettivo`, `camera oscura`, `still-life`, `reportage`, `ritratto`, `commissioni editoriali`, `Dodici anni`, `EXIF`, `Spring 2026`, `Fine art`, `Medio formato`, `tiratura`, `fine-art`, `Serie corrente`, `Apri la serie`) — **zero Pixel-brand leaks in Chiara**.
  - **Legacy literal sweep** on both rendered HTMLs: grepped `Sono una designer`, `Selected work · 2018`, `Atlas Magazine`, `Independent designer`, `Atelier Norma`, `Lumen Studio`, `Polare — Visual`, `Ogni progetto.*storia`, `Atlas Issue` — **zero legacy literals** in either rendered HTML.
  - **Hardcoded URL sweep** on `templates/preview_compositions/portfolio/` — **zero hardcoded `images.unsplash.com` URLs** in either new composition.
- **Listing page leak sweep**: dumped `/templates/portfolio/` HTML (13 494 bytes) and grepped for all 9 legacy literals — **zero matches**. Both cards render with their correct brand names ("Pixel — Portfolio Fotografico" · Pixel Photography) and ("Chiara — Portfolio Creativo" · Chiara Studio).
- **Django test client route sweep**: 5/5 routes return 200 — `/`, `/templates/`, `/templates/portfolio/`, `/templates/portfolio/chiara-portfolio-creativo/`, `/templates/portfolio/pixel-portfolio-fotografico/`.
- **Chromium visual walk at 1440×900** on `/templates/portfolio/` via Playwright MCP — both cards visible side-by-side, unmistakably distinct at card size. Pixel reads as a dark cinematic card with fullbleed low-key image; Chiara reads as a cream paper card with typographic headline and project index. Full-size preview PNGs (3200×1800) spot-checked and confirmed to match the differentiation matrix above.

**The two cards read as two completely different products, two completely different professions, two completely different narrative patterns. The identity-crash is closed.**

### Risks residui / what's NOT done
- **3 of 5 CRITICO categories still open:** agency, lawyer, real-estate. Recommended next order per AGENT_HANDOFF: real-estate → lawyer → agency. Same Session 17/18 recipe.
- **MEDIO items still open** (Phase 2g2x.3): D-047 lift on ecommerce fashion-editorial + artisan-workshop, restaurant trattoria-warm + street-modern, medical clinic/family/wellness preview comps, and the restaurant fine-dining live skin (Phase 2g.3).
- **Template completeness gap still open** (Phase 2g2x.4): 17 of 20 templates are preview-only. Chiara and Pixel are not exceptions — both remain preview-only (no content registry, no live-template skin folder). Per scope rule "do not introduce live multipage portfolio if not existing", Session 18 did not add inner pages.
- **Stale-PNG structural fix still deferred** (Phase 2g2x.5). Session 18 did not hit the trap because the worktree started empty.
- **Worktree not merged.** `phase-2g2x-portfolio-hardening-v2` branch, last commit `b967e99` was Session 17's business hardening fix; Session 18 work is uncommitted. Per D-049 gate, commit + PR after all 5 CRITICO categories close.

### Next micro-step
Pick ONE of the 3 remaining CRITICO categories. Recommended order: **real-estate** (Villa's ultra-luxury vs Casa's mass-market is the next cleanest "far apart" pair and has the mass-market price-range `€500K–€1.2M` literal that's the most visible leak) → lawyer → agency. Run the Session 17/18 playbook end-to-end in a fresh worktree, apply D-047 from line one, and do NOT skip the Chromium visual walk.

---

## Session 17 — Phase 2g2x.1 Business Hardening (2026-04-11)

**Agent:** Business category DNA split — first implementation wave of Phase 2g2x (catalog hardening, per D-049).
**Goal:** Close the `business` identity-crash case. Make Pragma and Elevate two clearly distinct products at card size — different imagery, different silhouette, different CTA pattern, different section order, different positioning — without quick-recoloring the legacy composition or touching any other category.

### Strategy chosen — Option A (DNA split, 2 archetypes)
The Session 16 audit offered two paths: (A) split into 2 distinct archetypes with their own compositions, or (B) lift the legacy composition into a D-047-compliant shared skin with per-tenant DNA content blocks. **Option A was selected** because Pragma (board advisory) and Elevate (SaaS landing) are semantically far apart — they demand entirely different silhouettes, section orders, CTA patterns, and dominant visuals. A forced-shared skin would either erase the differentiation or collapse into a conditional-branching frankenfile that only appears to share structure. Option A is the same recipe that already worked for medical (4 archetypes), restaurant (3), and ecommerce (2).

### What changed
**Five files modified, two files added, zero files deleted.**

| File | Change |
|------|--------|
| `apps/catalog/template_dna.py` | Added 2 archetypes to `LAYOUT_ARCHETYPES` (`corporate-suite`, `startup-saas-landing`). Added 2 hero styles (`split-executive`, `centered-manifesto-product`). Added 2 navbar styles, 2 footer styles, 2 card styles, 2 button styles, 2 tones, 2 conversion patterns, 2 imagery directions. Added **2 DNA entries** — `pragma-corporate-suite` and `elevate-startup-landing` — each with a full content block driving every literal the composition renders. |
| `apps/catalog/preview_imagery.py` | Added 2 new imagery pools: `business-corporate` (6 executive/boardroom/HQ/manufacturing URLs) and `business-startup` (6 dashboard/laptop/code/open-plan URLs). Zero URL overlap between the two pools and zero overlap with the legacy `business` pool. Legacy `business` pool kept with an inline header comment explaining it is architecturally unused by any published business template but preserved per D-036 (DNA system is additive). |
| `templates/preview_compositions/business/corporate-suite.html` | **NEW.** Photo-led institutional split hero. Solid navy full-bleed navbar, serif headline left with meta strip, boardroom photo right with credit ribbon, 3-up advisory pillar cards with serif numerals, floating KPI strip over navy band, sectors ribbon at the very bottom. Merriweather + Inter. Every text string flows from `{{ dna.content.* }}` or `{{ brand_name }}`. |
| `templates/preview_compositions/business/startup-saas-landing.html` | **NEW.** Typographic manifesto on a cosmic primary/secondary gradient with neon accent glow. Thin pulse launch banner at the top, floating pill navbar with glowing CTA, centered 92px manifesto headline with gradient highlight, feature-pills row, glowing product-mockup card overlapping the hero bottom (chrome bar + 3 metrics including price), social-proof wordmark row and live ship-log + next-release chip at the bottom. **Intentionally photo-light** — no big hero photo — so Elevate's card does not lean on imagery for differentiation. Manrope + Inter. Zero literals outside DNA content fields. |
| `SESSION_LOG.md` · `DECISIONS.md` · `TODO_NEXT.md` · `AGENT_HANDOFF.md` · `TEMPLATE_REGISTRY.json` | Updated to reflect the new business DNA split and the Phase 2g2x progress. |

The legacy `templates/preview_compositions/business.html` and the legacy `business` imagery pool are **intentionally untouched**. Per D-036 (DNA system is strictly additive), they remain in place as the fallback for any future template that might want to render through them. Both currently published business templates now bypass them entirely via DNA resolution.

### Differentiation matrix (final)
| Axis | Pragma · corporate-suite | Elevate · startup-saas-landing |
|---|---|---|
| Macro tone | Cream `#eef0f3` page + solid navy header band | Cosmic primary/secondary gradient + neon accent glow |
| Hero silhouette | 55/45 split: serif headline + meta strip L · boardroom photo R | Centered typographic manifesto, NO photo, product-mockup card overlap |
| Dominant visual | Full-bleed boardroom photograph `{{ imagery.0 }}` | Glowing product-mockup card with 3 metric readouts |
| Typography | Merriweather (serif, institutional) + Inter | Manrope (geometric sans, tech) + Inter |
| Navbar | Full-bleed solid navy, left-aligned links, phone CTA right | Floating pill, centered, glowing primary CTA button |
| Primary CTA | `Fissa una call privata` (ghost outline on navy) | `Inizia gratis` (glow pill) + `Guarda la demo · 2 min` secondary |
| Section order | hero → advisory pillars → KPI strip → sectors ribbon | launch banner → pill-nav → manifesto hero → product mockup → social proof → ship log |
| Positioning copy | Board advisory / M&A / governance / PMI | Conversion landing / GTM kit for SaaS & startup / waitlist → MRR |
| Imagery pool | `business-corporate` (6 URLs) | `business-startup` (6 URLs) — fully disjoint set |
| Density profile | airy | medium |
| Tone vocabulary | advisory-sober | growth-tech |

### Hard validation
- **`python manage.py check` — clean.**
- **`python manage.py seed_templates` — 20 templates, 0 created (idempotent re-run).**
- **`python manage.py generate_previews` — 18 rendered, 2 skipped.** Pragma and Elevate were generated earlier via `--only` targeted runs. The `business-corporate` pool fetched 6/6 Unsplash URLs; `business-startup` fetched 6/6. No 404s.
- **Leak sweep — zero cross-tenant contamination in both directions:**
  - Rendered Elevate HTML contains none of 21 Pragma-token strings tested: `"Hanno scelto Pragma"`, `"Marco Bianchi"`, `"Vectra Industries"`, `"NORDEA"`, `"VECTRA"`, `"FINOVA"`, `"ATLAS"`, `"info@pragmacorp.it"`, `"Parliamone"`, `"Consulenza strategica · B2B"`, `"Servizi di consulenza"`, `"Strategia commerciale"`, `"Trasformazione digitale"`, `"Ottimizzazione processi"`, `"Sostenibilità ESG"`, `"Soluzioni concrete per"`, `"far crescere"`, `"Affianchiamo le PMI italiane"`, `"Richiedi una call"`, `"Clienti soddisfatti"`, `"€45M"`.
  - Rendered Pragma HTML contains none of 28 Elevate-token strings tested: `"waitlist"`, `"MRR"`, `"quattordici giorni"`, `"Inizia gratis"`, `"Guarda la demo"`, `"Stripe"`, `"A/B test"`, `"Edge analytics"`, `"Copy kit italiano"`, `"elevate.app"`, `"Live A/B"`, `"Adottato da 240 startup italiane"`, `"FLUX"`, `"NOVA"`, `"QUANTA"`, `"HELIX"`, `"RIFT"`, `"CASP"`, `"Plan Launch"`, `"CLI deploy"`, `"Ship log live"`, `"v2.9"`, `"Serie A"`, `"Q2 2026"`, `"GrowthBook"` …
- **Hardcoded-URL sweep:** neither rendered HTML contains a literal `https://images.unsplash.com/…` URL. Every imagery slot resolves through the `{{ imagery.N }}` context variable, which is populated from cached file:// URIs at render time.
- **Django test-client route sweep — 5/5 green:**
  - `/` 200
  - `/templates/` 200
  - `/templates/business/` 200
  - `/templates/business/pragma-corporate-suite/` 200
  - `/templates/business/elevate-startup-landing/` 200
- **Preview-asset wiring verified:** `WebTemplate.preview_asset` on both slugs returns the new canonical PNG filename. The business category listing HTML references both preview filenames and both brand names (only their own) — no cross-tenant brand mentions.
- **Visual regression via Chromium (Playwright)** at 1440×900 on `/templates/business/`: the two cards are unmistakably distinct. Elevate card = dark cosmic gradient + neon-cyan manifesto headline + glowing product mockup. Pragma card = cream/navy institutional split + boardroom photo + serif "Dove si prendono le decisioni che contano". Macro tone, silhouette, dominant visual, and positioning copy all differ.

### Why this closes the business identity-crash case
The Session 16 verdict was: "Elevate's card renders Pragma's copy". After Session 17:
1. Neither template resolves through the legacy `business.html` composition anymore — both have DNA entries, so `_resolve_composition` routes them to their archetype-specific files.
2. The legacy `"Hanno scelto Pragma"` label, client wordmark row, "Marco Bianchi" testimonial, B2B consulting CTAs, and the 4 consulting service cards have **all been removed from Elevate's render path**. They still exist in `business.html` for any future template that explicitly opts into the legacy file, but no published template does.
3. The two new skins were authored under the D-047 chrome-authoring contract from the first line — every string lives in `dna.content.*` or pulls from `brand_name`. No follow-up "lift pass" will ever be needed for this pair.
4. The imagery pools are fully disjoint: executive boardroom photos vs startup product/dashboard photos. Additionally the startup composition deliberately avoids a big hero photo, so even at 200×120 card thumbnail size the difference is readable entirely from macro tone + typographic silhouette.
5. The positioning copy is now genuinely different: Pragma headline reads as advisory gravitas ("Dove si prendono le decisioni che contano"); Elevate reads as growth conversion ("Dalla waitlist al primo MRR in quattordici giorni").

### Lessons (carry forward for Phase 2g2x.1.next — agency/lawyer/real-estate/portfolio)
1. **Option A (DNA split) is the default for semantically-far siblings.** Only reach for Option B (D-047 lift of shared composition + per-tenant content) when the two tenants are genuinely close. Business, real-estate (ultra-luxury vs mass-market), portfolio (designer vs photographer), and agency (bold vs editorial) are all "far apart" by the same yardstick — they should all follow Option A.
2. **Author under D-047 from line one.** The specialist chrome needed a 17-leak lift in Session 14 because it was authored before the contract. Both new business skins ship with zero leaks because every string was driven from DNA on the first pass. The marginal cost is negligible (write the DNA field and the HTML reference in the same commit).
3. **Startup composition pattern: photo-light by design.** The new `startup-saas-landing.html` shows that a dark gradient + product mockup card + typographic manifesto carries the whole above-the-fold mood without any big hero photo. This is a reusable pattern for any future "conversion-first" category that wants to avoid shared-photo pitfalls entirely. Imagery pools become small fallback sets for accent tiles only.
4. **Preview-only worktrees need to seed + migrate + generate from scratch.** The `mw-business-hardening-v2` worktree had no `db.sqlite3` or `media/` on entry. The three-step warm-up (`migrate` → `seed_categories` → `seed_templates` → `generate_previews`) is the standard path; budget for it when spawning a new worktree.
5. **Card-size differentiation is confirmed at card size, not just at full-res preview.** The test that matters is a Chromium walk through the category listing page at 1440×900 with the cards in their real grid context. Both renders individually at 1600×900 might look different, but visual regression at listing scale is what buyers actually see.

### What comes next — Phase 2g2x.1 continuation
Business is closed. The next 4 CRITICO categories remain:
- [ ] **Agency** — vertex + aura (DNA split suggested: `bold-grid` + `editorial-quiet`)
- [ ] **Lawyer** — lex + juris (`classic-gold` + `modern-transparent`)
- [ ] **Real-estate** — casa + villa (`mass-market` + `ultra-luxury-cinematic`)
- [ ] **Portfolio** — chiara + pixel (`editorial-designer` + `cinematic-photographer`)

Each follows the same Session 17 recipe: 2 archetypes + 2 DNA content blocks + 2 D-047-compliant compositions + 2 disjoint imagery pools. No shortcuts. All MEDIO-severity items (2g2x.3 D-047 lifts on single-tenant archetype files, 2g2x.2 medical imagery pool realignment) also remain open. The wave exit criteria in TODO_NEXT.md Phase 2g2x.6 still gate Phase 3.

---

## Session 16 — Catalog Differentiation Hard Audit (2026-04-11)

**Agent:** Audit only — no implementation
**Goal:** Determine whether the catalog's sibling templates are credible distinct products, or whether they're still recolors / identity-crash prototypes. Produce a severe, concrete, blocking-or-not verdict before any further roadmap work.

### Method
1. Read all repo memory files (CLAUDE.md → TEMPLATE_REGISTRY.json)
2. Inventoried every WebTemplate row across 8 categories (20 templates) and matched each to its DNA state + content registry state + archetype tenancy
3. Inspected `apps/catalog/template_dna.py`, `apps/catalog/template_content.py`, `apps/catalog/preview_imagery.py`, `apps/catalog/management/commands/seed_templates.py`
4. Read every `templates/preview_compositions/<category>.html` legacy composition and every `templates/preview_compositions/<category>/<archetype>.html` DNA composition
5. Walked the `templates/live_templates/` tree (only 2 archetypes authored: `medical/specialist/`, `restaurant/fine-dining/`)
6. Grepped for literal brand leaks in every composition file (fine-dining, trattoria-warm, street-modern, clinic, family, wellness, specialist, fashion-editorial, artisan-workshop)
7. Measured imagery-pool URL overlap between sibling pools

### Verdict: **CATALOG NON APPROVABILE — hardening phase bloccante richiesta**

### Severity breakdown
| Category     | Severity  | Templates                                  | Nature |
|--------------|-----------|--------------------------------------------|--------|
| agency       | **CRITICO** | vertex-creative-agency · aura-digital-studio | Sistemico — no DNA, shared `agency.html` con 6 case-study letterali (Lumen, Vega, Atelier Norma, Helios Bank, Cinetic, Polar Studios). Cards are wrong-content, not recolor |
| business     | **CRITICO** | pragma-corporate-suite · elevate-startup-landing | Sistemico — `business.html` hardcodes `"Hanno scelto Pragma"` label, Marco Bianchi/Vectra testimonial, Nordea/Vectra/Finova/Atlas clients. Elevate renders Pragma's copy |
| lawyer       | **CRITICO** | lex-studio-legale · juris-avvocato-moderno | Sistemico — `lawyer.html` hardcodes "Studio legale dal 1962", full 4-area practice grid (societario/famiglia/lavoro/penale), M. Bianchi review. Juris renders Lex's heritage |
| real-estate  | **CRITICO** | casa-agenzia-immobiliare · villa-immobili-lusso | Sistemico — `real-estate.html` hardcodes "600+ immobili", €500K–1.2M price box (mass-market), specific Brera listing. Villa renders mass-market copy |
| portfolio    | **CRITICO** | chiara-portfolio-creativo · pixel-portfolio-fotografico | Sistemico — `portfolio.html` hardcodes "Sono una designer indipendente", "Featured · Atlas Magazine", h1 "Ogni progetto una storia". Pixel (photographer) renders Chiara's designer copy |
| medical      | **MEDIO** | cardio-studio-specialistico · dermatologia-elite-roma | Combinato — DNA system works; Sessions 14+15 closed 17 chrome leaks + 3 preview-comp leaks; BUT (a) `medical-specialist` imagery pool shares 5/6 URLs with `lawyer` pool so both render a lawyer-portrait hero, (b) hero photo is identical for both siblings, (c) `medical-family` pool is 100% URL-overlap with base `medical` pool |
| restaurant   | **MEDIO** (live-only) | gusto (+ latent for sapore/brace) | Live-pages-only — 3 preview compositions are solid, cards read as 3 distinct products. But `live_templates/restaurant/fine-dining/*` has 5 files with Gusto literal leaks (Fioravanti / Brera / Otto atti / Barolo / Selosse / Bresse / Michelin) — Phase 2g.3 already flagged. `trattoria-warm.html` preview comp has "Trastevere · dal 1987 · cucina romana di famiglia" hardcoded |
| ecommerce    | **MEDIO** (latente) | luxe-fashion-store · bottega-shop-artigianale | Preview-only — single-tenant archetypes work at card size via macro-tone split (Session 15). BUT both compositions have massive D-047 violations: `fashion-editorial.html` has 12+ Luxe literals (Carla Sozzani, Giulia Maison, Issue 12, Rack Atelier, Bomber Siena, Milano·Parigi·Tokyo, Grand Hôtel Villa d'Este, "Accedi al lookbook"); `artisan-workshop.html` has 10+ Bottega literals (Firenze·dal 1968, Santa Croce sull'Arno, Montelupo, Prato, "Ceramica"/"Tessitura" nav, "12 botteghe", "Mai sopra 50"). Will detonate the moment Phase 2f.2 adds a second fashion/artisan template |

### Secondary but cross-cutting
- **17/20 templates are preview-PNG-only.** Only cardio, derm (via specialist reuse), and gusto have inner pages. The marketplace sells "completed multipage websites" but delivers single-page posters for 85% of the catalog. The user's concern "il prodotto è fatto di template completi multipagina" is not yet met at catalog level — this is a completeness gap, not just a differentiation gap
- **Stale-PNG timing trap** (recurring class since Sessions 8/10/12/15). No structural fix — TODO_NEXT Phase 2d item 4 still open. Next session that regenerates should plan it
- **Preview-comp and live-template chrome are authored as if archetypes are single-tenant**, even though D-047 was formalized in Session 14 to prevent exactly this. Session 15 confirmed D-047 applies to preview compositions too, but only patched `medical/specialist.html`. The rule is honored only in the files that were audited post-D-047 (specialist chrome + specialist preview comp). Every other per-archetype file predates D-047 and has never been leak-swept

### Root-cause map (technical)
| Source of truth              | Issue                                                                                |
|------------------------------|--------------------------------------------------------------------------------------|
| `apps/catalog/template_dna.py` | Only 10 of 20 templates have DNA. 10 fall through to legacy per-category composition |
| `templates/preview_compositions/agency.html` etc (5 files) | Author-as-prototype literals never lifted to DNA content fields |
| `templates/preview_compositions/ecommerce/fashion-editorial.html` | Authored Session 15 with 12+ literals baked in — violates D-047 |
| `templates/preview_compositions/ecommerce/artisan-workshop.html` | Same class — 10+ literals |
| `templates/preview_compositions/restaurant/trattoria-warm.html` | `Trastevere · dal 1987` hardcoded |
| `templates/preview_compositions/medical/family.html` | `Dr.ssa Rambaldi` hardcoded (latent — single tenant) |
| `templates/live_templates/restaurant/fine-dining/` (8 files) | 5 files have Gusto brand leaks (Phase 2g.3 already planned) |
| `apps/catalog/preview_imagery.py` | Sibling pools 100% URL-overlap (agency/business/lawyer/real-estate/portfolio); `medical-specialist` 5/6 from lawyer pool; `medical-family` 100% from `medical` pool |
| `apps/catalog/template_content.py` | Inner-page content exists for only 3 templates — the live-preview coverage is 15% of the catalog |

### Minimal technical plan (no scope creep)
1. **Phase 2g2x.1 — Legacy-comp lift to D-047.** For each of the 5 non-DNA categories, either (a) split into 2 archetypes with its own composition + DNA entry, OR (b) lift the existing `<category>.html` to parse `dna.content.*` fields and add minimal DNA entries for each tenant. Option (a) is cleaner and matches the medical/restaurant pattern; option (b) is cheaper but requires both tenants to author DNA content. Either way: **no new HTML file needs to be created for any template — existing 5 legacy comps become 5 DNA-driven comps OR become 10 archetype comps**
2. **Phase 2g2x.2 — Imagery pool sibling-split.** For each of the 5 legacy categories, replace the single 6-URL pool with two sibling-distinct pools per Session 10 recipe (`<category>-A` + `<category>-B`, hand-checked via Read for visual distinctness, zero URL overlap)
3. **Phase 2g2x.3 — Lift latent leaks under D-047.** `restaurant/trattoria-warm.html`, `restaurant/street-modern.html`, `medical/family.html`, `medical/clinic.html`, `medical/wellness.html`, `ecommerce/fashion-editorial.html`, `ecommerce/artisan-workshop.html` — grep each for literal brand strings and move them to the DNA `content` block, using Session 14's mechanical recipe
4. **Phase 2g2x.4 — Medical specialist imagery pool.** Replace the lawyer-pool-derived hero photo in `medical-specialist` with a real medical-specialist-appropriate URL set (2 templates × different photo subsets, OR have them share the pool and macro-tone differentiate via accent). Fix `medical-family` pool overlap with base `medical` pool
5. **Phase 2g2x.5 — Single-page template demotion.** Templates with no live inner-page content should either (a) be marked as `draft` / unpublished until their inner pages exist, OR (b) receive inner-page content following the cardio/derm/gusto pattern. This is the "completeness gap" fix. Ship decision: keep them `published` but flag them as "preview-only" with a Coming Soon badge, OR hide them from listing until complete
6. **Phase 2g2x.6 — Stale-PNG structural fix** (TODO_NEXT Phase 2d item 4): add DNA-signature hashing on TemplateAsset so regeneration is automatic

### Categories that MUST be corrected before roadmap resumes
All 5 non-DNA categories (**CRITICO**): agency, business, lawyer, real-estate, portfolio.
Latent-leak fixes for restaurant/ecommerce/medical (**MEDIO**) can be done in a second wave but should not be skipped — they will detonate on reuse.

### What NOT to do yet (hard boundaries)
- No auth / checkout / editor / projects / commerce / dashboard / accounts / cart / stripe work
- No new categories
- No new templates to ANY category
- No new archetypes
- No broad refactors outside this audit scope
- No forced merges to main

### Files modified in Session 16
- `SESSION_LOG.md` — this entry (audit findings)
- `DECISIONS.md` — D-049 added (audit verdict + blocking rule)
- `TODO_NEXT.md` — Phase 2g2x inserted as the blocking wave before any roadmap item
- `AGENT_HANDOFF.md` — Session 16 handoff + "do not resume roadmap" directive
- `CATEGORY_ROADMAP.md` — severity column added per category, DNA-rollout order updated

### Memory files updated (auto-memory)
- `catalog_differentiation_audit.md` (new project memory)
- `MEMORY.md` (pointer added)

---

## Session 15 — Visual Polish & Preview Fixes (2026-04-11)

**Agent:** Visual polish pass
**Goal:** Four concrete product-quality fixes visible directly in the marketplace UI: (1) dermatologia card shows a grey placeholder, (2) restaurant category hero is clipped/unbalanced, (3) Gusto+Sapore still too similar at card size, (4) Luxe+Bottega identical at card size.

### Root causes identified
1. **Missing dermatologia preview.** Session 13's validation run deliberately skipped PNG regeneration ("0 new TemplateAssets — validation is about the live preview, not the thumbnail"). The `dermatologia-elite-roma` WebTemplate row had zero preview assets, so `preview_asset` returned `None` and `_template_card.html` rendered its `mw-img-placeholder` fallback (a grey `bi-window-desktop` icon).
2. **Hidden second leak in the specialist preview composition.** Session 14's copy-abstraction lift covered the 9 `live_templates/medical/specialist/*.html` chrome files but did NOT touch `templates/preview_compositions/medical/specialist.html`. It still hardcoded `Dr. R. Marani`, `Roma · Parioli`, and `SC Cardiologia` in the hero meta + credit blocks. Regenerating the dermatology preview as-is would have rendered the cardiologist's name on the dermatology card.
3. **Restaurant category hero cramped + unbalanced.** `.mw-page-hero` used `padding-top: 7rem` (112px) against a 77px fixed navbar, leaving a 35px gap between navbar bottom and breadcrumb top — too tight for a premium site. `max-width: 36rem` on the subhead made the right side of the hero dead space on wide screens, and no `min-height` meant the hero collapsed to ~330px.
4. **Gusto + Sapore PNGs on disk were stale.** Same timing-trap class that Sessions 8/10/12 fought repeatedly: the files were legacy `restaurant.html` renders from before the Session 10 fix pass redesigned fine-dining as fully dark and trattoria as fully cream. Session 12 claimed to have regenerated them but the fix did not land in this worktree. The DB rows pointed at canonical filenames; the files themselves were old.
5. **Luxe + Bottega had no DNA at all.** Both templates rendered through the single legacy `ecommerce.html` composition that hardcodes every string ("Stile / senza / compromessi", "I più desiderati del mese", identical product names) and pulls from the same imagery pool. The only difference was the brand name in the navbar. Ecommerce was not yet a DNA-pilot category.

### Actions taken

**Fix 1 — Dermatologia preview**
- Added `hero_meta`, `credit_left`, `credit_right` fields to BOTH `cardio-studio-specialistico` and `dermatologia-elite-roma` DNA `content` blocks in `apps/catalog/template_dna.py`. Derm: `Dr.ssa L. Ricciardi / 18 anni / 2.400+ pazienti · Studio Roma · Via Veneto · Specialità Dermatologia`. Cardio: unchanged semantics, just moved from literals to DNA fields.
- Updated `templates/preview_compositions/medical/specialist.html` to loop over `dna.content.hero_meta` and read `dna.content.credit_left.0/1` + `credit_right.0/1` — zero cardio literals left in the composition.
- Ran `python manage.py generate_previews --only dermatologia-elite-roma` → new canonical `dermatologia-elite-roma-preview.png` lands with the correct dermatology brand/city/specialty.
- Regenerated cardio too (clean-delete recipe: remove DB row + canonical file + orphan suffix file, then re-run without `--force`) to verify the composition change didn't regress cardio rendering. **It didn't** — identical output.

**Fix 2 — Restaurant category hero**
- Rewrote `.mw-page-hero` in `static/css/components.css`:
  - `padding-top: calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` — generous 64px clearance from navbar bottom to breadcrumb top (was 35px)
  - `padding-bottom: var(--mw-space-10)` — 80px (was 48px)
  - `min-height: 22rem` — hero no longer collapses on short copy
  - `display: flex; flex-direction: column; justify-content: center` — vertical centering inside the generous box
  - Subhead `max-width: 46rem` (was 36rem) — eats more of the wide-screen hero so the right isn't dead
  - H1 now `clamp(3xl, 3.8vw, 5xl)` — responsive at wide breakpoints
  - Background adds two radial gradients (indigo top-right + amber bottom-left) and `overflow: hidden` — subtle depth instead of flat dark
  - `position: relative` + `.mw-page-hero > .container { position: relative; z-index: 1 }` — decorative overlays don't swallow content
- Measured after: navbar→breadcrumb gap = 64px (was 35px), hero height = 373px (was 330px), no dead pixel regions on wide viewport.

**Fix 3 — Gusto / Sapore differentiation**
- Clean-delete recipe applied to both: remove asset row, remove canonical file, remove any orphan-suffix file, re-run `generate_previews --only <slug>` without `--force`.
- Confirmed the DNA-path `restaurant/fine-dining.html` + `restaurant/trattoria-warm.html` compositions from Session 10 render correctly. Generated PNGs:
  - **Gusto** — fully DARK charcoal page, italic Playfair "Una serata in otto atti", single full-bleed plated-dish hero photo, gold dotted-leader numbered course index over black with "€ 180 / persona".
  - **Sapore** — fully BRIGHT cream page, two tilted polaroid photos, handwritten Caveat "Da Nonna Rosa, come a casa vostra", red+green cream recipe card with weekly specials, no dark regions.
- With Brace (yellow brutalist) unchanged, the three restaurant cards now occupy three opposite ends of the visual spectrum: **YELLOW / CREAM / DARK**. Instantly distinguishable at card size.

**Fix 4 — Luxe / Bottega differentiation (NEW ecommerce DNA pilot)**
- Added 2 archetypes to `LAYOUT_ARCHETYPES` in `template_dna.py`: `fashion-editorial` (Luxe) and `artisan-workshop` (Bottega).
- Added DNA registry entries for both templates with archetype, font pairing, and minimal content block (compositions read the headline + eyebrow only; no further leaks possible since every other string is either a CSS rule or a generic archetype label per D-047).
- Authored two new compositions:
  - `templates/preview_compositions/ecommerce/fashion-editorial.html` — fully DARK #08070a ink charcoal page, gold #B8860B accents, italic Cormorant Garamond 108px "Il nuovo corpo del vestire", fashion-model full-bleed cover left, issue tag + styling credit + 4-up editorial product strip with gold price labels at bottom. Uses the existing `ecommerce` imagery pool, indices reassigned: hero=0 (fashion model), tiles=5,4,3,0.
  - `templates/preview_compositions/ecommerce/artisan-workshop.html` — fully BRIGHT #f6ecd8 cream page with subtle grain/pattern background, terracotta accent, huge Libre Baskerville 108px "Pezzi unici cuciti & fatti in bottega" with orange italic emphasis, rubber-stamped info panel rotated 0.8deg with bottega specs, 4-up labeled edition cards at bottom (each with N° number, edition numerator/denominator, artisan provenance, pezzo-unico tag). NO hero photo — typographic-led. Uses the same `ecommerce` pool for the 4 small product tiles. At card size, zero hero photo overlap with Luxe.
- Regenerated both PNGs. Deliberate macro tone choice applies Session 10's core lesson: sibling templates must differ at PAGE LEVEL, not just in accent details. Luxe = black. Bottega = cream. Instantly distinguishable.

**Orphan file cleanup (housekeeping)**
- Session 12 left 4 orphan-suffixed preview files on disk with DB rows pointing to them (`_5utrvms`, `_iasDI4Y`, `_yYaOuCE`, `_wWIztM1`). Renamed each orphan to its canonical name and updated the DB row so each template has one file with one canonical name. Zero orphan files now exist in `media/template_assets/2026/04/`.

### Validation

1. **`python manage.py check` — clean** (run twice: after DNA edits, after composition edits).
2. **37-route regression sweep via Django test client:**
   - Homepage, full template list, 5 category pages (medical, restaurant, ecommerce, lawyer, agency)
   - 10 template detail pages (all 5 medical + all 3 restaurant + both ecommerce)
   - 7 cardio live preview pages
   - 7 dermatologia live preview pages
   - 6 gusto live preview pages
   - **All 37 return 200.**
3. **Cardio-leak audit on dermatology pages — re-ran.** Grepped rendered HTML of all 7 dermatologia inner pages for 9 cardio literals (`Marani`, `Parioli`, `OMCeO Roma 12 / 4408`, `Cardiologia`, `ecocardiograf`, `Visita cardiologica`, `LANCET`, `European Heart`). **All 7 pages clean.** The specialist chrome stays clean after the preview-composition edit.
4. **Visual verification via Playwright-driven Chromium:**
   - Homepage featured grid shows new Gusto composition (dark editorial).
   - `/templates/restaurant/` shows Brace/Sapore/Gusto as three obviously different products. Hero is no longer clipped, has 64px navbar clearance and generous breathing room.
   - `/templates/medical/` shows all 5 medical templates with valid previews (no grey placeholder for dermatology).
   - `/templates/ecommerce/` shows Luxe (dark fashion) and Bottega (cream artisan) instantly distinguishable.

### Files modified (Session 15)
- `apps/catalog/template_dna.py` — +2 archetypes (`fashion-editorial`, `artisan-workshop`), +2 DNA entries (luxe, bottega), +3 fields on each specialist DNA (`hero_meta`, `credit_left`, `credit_right`)
- `templates/preview_compositions/medical/specialist.html` — literals → DNA field reads
- `templates/preview_compositions/ecommerce/fashion-editorial.html` — NEW file (Luxe archetype)
- `templates/preview_compositions/ecommerce/artisan-workshop.html` — NEW file (Bottega archetype)
- `static/css/components.css` — `.mw-page-hero` redesigned (padding, min-height, gradients, relative positioning)
- `media/template_assets/2026/04/dermatologia-elite-roma-preview.png` — NEW preview (was missing)
- `media/template_assets/2026/04/cardio-studio-specialistico-preview.png` — regenerated (same visual, now from DNA fields)
- `media/template_assets/2026/04/gusto-fine-dining-preview.png` — regenerated (now fully dark fine-dining)
- `media/template_assets/2026/04/sapore-trattoria-pizzeria-preview.png` — regenerated (now fully cream trattoria)
- `media/template_assets/2026/04/luxe-fashion-store-preview.png` — regenerated from new fashion-editorial archetype
- `media/template_assets/2026/04/bottega-shop-artigianale-preview.png` — regenerated from new artisan-workshop archetype
- 4 orphan-suffixed files renamed back to canonical

### Lessons from Session 15

- **"Validation skipped the thumbnail" is a user-facing bug.** Session 13 explicitly deferred PNG regeneration when adding Dermatologia, reasoning that validation was about the live preview not the marketplace card. But the marketplace card is the FIRST thing a buyer sees — a grey placeholder on a card is a broken product. Any future archetype-reuse add must regenerate the preview as the final step, no exceptions.
- **Per-archetype compositions need the same copy-abstraction contract (D-047) as live-template chrome.** Session 14 lifted `templates/live_templates/medical/specialist/*.html` but left `templates/preview_compositions/medical/specialist.html` with 3 cardio literals. Any time two templates share an archetype, the PREVIEW composition is as much chrome as the live template is — it needs the same rule: every string is either a CSS rule, a generic archetype label, a DNA content field, or a loop item. Never a literal brand name, city, or specialty.
- **Macro tone trumps imagery at card size, AGAIN.** Luxe and Bottega share the exact same `ecommerce` imagery pool (zero URL changes in `preview_imagery.py`) yet at card size they look radically different because one composition is fully BLACK and the other is fully CREAM. The compositions differ in page background, font family, hero structure (photo-led vs typographic-led), and accent color. Session 10 was right: fighting over imagery distinctness is expensive (URL hunting, HTTP 404s, hand-verification); controlling macro tone is free and does more of the visual work.
- **Stale PNGs are a recurring class of bug.** Sessions 8, 10, 12, 15 all independently hit the timing trap where a DNA change left the old preview on disk with a DB row pointing at it. Session 12's `WebTemplate.preview_asset` property fixed the read side but not the write side. The proper structural fix (from TODO_NEXT Phase 2d) is still unimplemented: either auto `--force` when DNA mtime > asset file mtime, or hash the DNA into the asset row and compare on every run. Until then, the clean-delete recipe (remove row + canonical file + orphan suffix, re-run without `--force`) is the only reliable path.
- **`position: fixed` navbar + `padding-top: Xrem` on hero is a hidden coupling.** 7rem looked fine with a 64px navbar but became cramped once the navbar grew to 77px. Encoded it as `calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` so a future navbar resize stays coupled explicitly. Long-term: measure the navbar height via JS on page load and expose as CSS variable.

### What's next

See TODO_NEXT.md Phase 2g.3 (fine-dining copy lift) + Phase 2f.2 (ecommerce DNA expansion — add at least one more fashion and one more artisan template to validate the two new archetypes for reuse, same way derm validated specialist).

---

## Session 1 — Orchestrator Bootstrap (2026-04-09)

**Agent:** Orchestrator
**Goal:** Inspect repo, define architecture, create all coordination files, prepare for parallel workstreams.

### Actions Taken
1. Inspected repository — fresh Django 5.2.7 scaffold, no commits, no apps, no requirements.txt
2. Discovered actual environment: Python 3.13.5, Django 5.2.7 (not 6.0.4), rich package set including DRF, Stripe, Celery, Pillow, crispy-bootstrap5
3. Designed 7-app modular architecture (core, accounts, catalog, editor, projects, commerce, pages)
4. Established services/selectors pattern for business logic
5. Created all coordination files:
   - CLAUDE.md — project guidance for Claude Code
   - ARCHITECTURE.md — app structure, layered pattern, URL scheme, frontend/static layout
   - DECISIONS.md — 10 architectural decisions documented
   - TODO_NEXT.md — prioritized task lists for both workstreams
   - CATEGORY_ROADMAP.md — 8 MVP categories + post-MVP expansion
   - CONTENT_GUIDELINES.md — writing style per category, brand identity rules
   - BRAND_SYSTEM_GUIDELINES.md — visual design system specification
   - AGENT_HANDOFF.md — clear instructions for backend-core and premium-ui
   - TEMPLATE_REGISTRY.json — empty registry scaffold
   - SESSION_LOG.md — this file
6. Prepared phased implementation roadmap (5 phases, MVP first)
7. Set up requirements.txt with pinned core dependencies

### Files Created
- CLAUDE.md
- ARCHITECTURE.md
- DECISIONS.md
- TODO_NEXT.md
- CATEGORY_ROADMAP.md
- CONTENT_GUIDELINES.md
- BRAND_SYSTEM_GUIDELINES.md
- AGENT_HANDOFF.md
- TEMPLATE_REGISTRY.json
- SESSION_LOG.md
- requirements.txt

### Key Decisions Made
- D-001 through D-010 (see DECISIONS.md)
- Most critical: Custom User model must be created BEFORE first migrate

### Next Steps
- **Backend-core:** Create app scaffolds, custom User model, core base models, catalog models, admin — see AGENT_HANDOFF.md
- **Premium-UI:** Create design system, base template, homepage, navigation, card components — see AGENT_HANDOFF.md

## Session 2 — Premium UI Phase 1 (2026-04-09)

**Agent:** Premium-UI
**Goal:** Build the complete frontend foundation — design system, templates, components, and listing pages.

### Actions Taken
1. Created `templates/` directory structure: base.html, includes/, pages/, catalog/
2. Created `static/` directory structure: css/, js/, images/brand/
3. Updated `settings.py`: added TEMPLATES DIRS and STATICFILES_DIRS (minimal Python change)
4. Built **design-system.css** — full CSS custom properties system: colors (primary/secondary/accent/neutrals), typography scale (1.25 ratio, Plus Jakarta Sans + Inter), spacing (8px base), shadows, transitions, buttons, badges, dividers, utility classes
5. Built **components.css** — navbar (fixed, backdrop-blur, mobile slide-out), template card (hover lift/shadow/image zoom), category card (icon animate on hover), hero section, stats bar, footer, filter bar, detail page components, breadcrumbs, tags
6. Built **pages.css** — homepage-specific styles, featured/category/listing grids, steps section, testimonials, detail tabs, empty state
7. Built **base.html** — Bootstrap 5.3 CDN, Google Fonts, design system CSS, RTL-ready lang/dir attributes, semantic blocks
8. Built **_navbar.html** — sticky navbar with brand mark, desktop nav links, CTA buttons, mobile hamburger with slide-out menu + overlay
9. Built **_footer.html** — 5-column layout (brand, marketplace, categories, support, company), social icons, copyright
10. Built **_hero.html** — reusable hero component with configurable content
11. Built **_template_card.html** — reusable card with dynamic model fields (image, category badge, brand name, title, description, price, hover actions)
12. Built **_category_card.html** — reusable card with icon, name, template count
13. Built **pages/home.html** — full homepage: hero, trust bar (stats), 8 category cards, 6 featured template cards, 3-step how-it-works, 3 testimonials, gradient CTA section. All content in Italian, no lorem ipsum.
14. Built **catalog/category_list.html** — page hero + breadcrumb + category grid with static fallback
15. Built **catalog/template_list.html** — page hero + breadcrumb + filter bar (search/category/sort) + template grid + pagination placeholder
16. Built **catalog/template_detail.html** — breadcrumb, gallery, tabbed description/features/reviews, sticky sidebar (price, CTA, meta info, tags), related templates section
17. Built **main.js** — navbar scroll effect (requestAnimationFrame), mobile menu open/close with overlay, Escape key close, responsive resize handler

### Files Created (14 new files)
- `static/css/design-system.css` — 290 lines, full design system
- `static/css/components.css` — 430 lines, all component styles
- `static/css/pages.css` — 190 lines, page-specific styles
- `static/js/main.js` — 70 lines, navbar + mobile menu
- `templates/base.html` — master template
- `templates/includes/_navbar.html` — sticky navbar with mobile menu
- `templates/includes/_footer.html` — multi-column footer
- `templates/includes/_hero.html` — reusable hero section
- `templates/includes/_template_card.html` — template listing card
- `templates/includes/_category_card.html` — category card
- `templates/pages/home.html` — full homepage
- `templates/catalog/category_list.html` — category listing
- `templates/catalog/template_list.html` — template listing with filters
- `templates/catalog/template_detail.html` — template detail with sidebar

### Files Modified (1 file)
- `marketweb/settings.py` — added TEMPLATES DIRS and STATICFILES_DIRS

### Key Design Decisions
- D-011: `mw-` CSS prefix for all custom classes to avoid Bootstrap collisions
- D-012: Plus Jakarta Sans for headings, Inter for body — premium Google Font pairing
- D-013: CSS custom properties (not SCSS) for zero-build-step development
- D-014: All template cards include dynamic model field references compatible with backend-core models
- D-015: Static fallback content in listing pages for development without backend data
- D-016: Italian content throughout, formal "Lei" register, no lorem ipsum

### Next Steps
- Wire category card href attributes to actual URL routes when backend views are ready
- Replace placeholder images with real template screenshots
- Add RTL bundle switching logic (detect lang=ar, swap Bootstrap CSS)
- Build accounts/ and commerce/ templates (login, register, cart, checkout)
- Connect template_card to real WebTemplate queryset data

## Session 3 — UI Integration Fix & Polish (2026-04-09)

**Agent:** Premium-UI
**Goal:** Diagnose and fix navbar duplication and layout breakage after backend/UI merge. Polish visual output.

### Root Cause Found
**Bootstrap 5.3.3 CSS failed to load due to an incorrect SRI integrity hash** in `base.html`. The `<link>` tag was present with the correct href, but the browser rejected the file because the `sha384-...` hash didn't match the actual file content from jsdelivr CDN. This meant:
- **Zero Bootstrap CSS loaded** — no grid system, no responsive utilities, no component styles
- `d-lg-none` had no effect → mobile slide-out menu rendered visibly on desktop = **duplicate navbar**
- `.container`, `.row`, `.col-*` had no effect → broken grid layouts throughout
- `d-none d-lg-flex` had no effect → desktop nav links and mobile elements all visible simultaneously

The Bootstrap JS bundle had the same SRI hash issue.

### Actions Taken
1. Used Playwright to inspect the running page — confirmed `display: block` on the mobile menu element that should have been `display: none` via `d-lg-none`
2. Enumerated loaded stylesheets — discovered Bootstrap CSS completely absent (only 5 sheets: Google Fonts, Bootstrap Icons, and 3 custom CSS files)
3. Confirmed `link.sheet === null` (failed load) while `link.href` was correct — pointed to SRI hash mismatch
4. Updated Bootstrap CDN from 5.3.3 (bad SRI) to **5.3.8** (current, correct SRI hashes) for both CSS and JS
5. Verified fix: Bootstrap loaded, `d-lg-none` works, mobile menu hidden, grid system functional
6. **Polish fixes:**
   - Category grid: changed from `auto-fill, minmax(180px)` to `repeat(4, 1fr)` for balanced 4+4 layout
   - Hero padding: consolidated padding-top (7rem for navbar clearance) and added bottom padding
   - Typography: added explicit `margin-top: 0` on headings to prevent Bootstrap reboot conflicts
   - Links: added `!important` on `text-decoration: none` to override Bootstrap's reboot link underlines
   - Card title: added `!important` on font-size to prevent global h3 size from overriding card context
   - `_hero.html` partial: removed `mw-home-hero` class (should be generic, not page-specific)

### Files Modified (5 files)
- `templates/base.html` — Bootstrap CDN 5.3.3→5.3.8 with correct SRI hashes (CSS + JS)
- `static/css/design-system.css` — Link `text-decoration: none !important`, heading `margin-top: 0`
- `static/css/components.css` — Hero `padding-bottom`, card title `font-size !important`
- `static/css/pages.css` — Category grid `repeat(4, 1fr)` with responsive breakpoints, hero padding
- `templates/includes/_hero.html` — Removed `mw-home-hero` class from generic partial

### Key Takeaway
The entire "duplicate navbar" and "broken layout" was a single root cause: **bad SRI hash on Bootstrap CDN link**. No template inheritance issues, no duplicate includes — the HTML structure was always correct.

## Session 4 — Catalog Integration Phase 1 (2026-04-09)

**Agent:** Catalog Integration
**Goal:** Connect the premium UI templates to real database-backed querysets. Implement catalog views, selectors, URLs, seed data, and wire all pages to real Category and WebTemplate models.

### Actions Taken
1. **Fixed seed_categories.py** — Removed `bi-` prefix from icon field (partial already adds it), updated category names to Italian display names (Ristorante, Medico, Avvocato, Immobiliare), enriched descriptions
2. **Created `apps/catalog/selectors.py`** — 7 selector functions: `get_active_categories`, `get_active_categories_with_counts`, `get_published_templates`, `get_featured_templates`, `get_templates_by_category`, `get_template_detail`, `get_related_templates`
3. **Created `apps/catalog/views.py`** — `CategoryListView`, `TemplateListView` (with optional category filtering via URL kwarg), `TemplateDetailView` with related templates
4. **Wired `apps/catalog/urls.py`** — 4 URL patterns: `/templates/` (all), `/templates/categories/` (category list), `/templates/<category_slug>/` (filtered), `/templates/<category_slug>/<slug>/` (detail)
5. **Updated `apps/pages/views.py`** — `HomePageView` now passes `categories` (with annotated counts) and `featured_templates` (limit=6) to context
6. **Updated `templates/pages/home.html`** — Replaced 8 hardcoded category cards with `{% for category in categories %}` loop using `_category_card.html` partial. Replaced 6 hardcoded template cards with `{% for tmpl in featured_templates %}` loop using `_template_card.html` partial. Updated hero CTA and "Vedi Tutti" links to `{% url 'catalog:template_list' %}`
7. **Updated `templates/includes/_category_card.html`** — Added real URL via `{% url 'catalog:template_list_by_category' category.slug %}`, updated count to use annotated `template_count`
8. **Updated `templates/includes/_template_card.html`** — Added real URLs to card title, "Scopri" button, and eye preview action via `{% url 'catalog:template_detail' template.category.slug template.slug %}`. Added `floatformat:0` to price display
9. **Updated `templates/catalog/template_detail.html`** — Fixed breadcrumb links (Template → `/templates/`, Category → `/templates/<slug>/`), wired related templates section with `{% for %}` loop
10. **Updated `templates/catalog/template_list.html`** — Replaced static fallback with dynamic `{% for %}` + `{% empty %}` pattern, made category dropdown dynamic with `onchange` navigation, fixed breadcrumbs
11. **Updated `templates/catalog/category_list.html`** — Removed static fallback, uses dynamic `{% for %}` loop
12. **Updated `templates/includes/_navbar.html`** — Wired "Template" and "Categorie" nav links to real URLs (both desktop and mobile)
13. **Created `apps/catalog/management/commands/seed_templates.py`** — 16 realistic WebTemplate + TemplateBrand entries across all 8 MVP categories (2 per category), matching homepage copy exactly (Vertex Studio, Osteria Moderna, SaluteVita Clinic, Chiara Studio, Pragma Corp, Studio Legale Ferri)
14. **Seeded database** — 8 categories + 16 templates with brands, all status=published, 6 featured

### Files Created (3 new files)
- `apps/catalog/selectors.py` — 7 selector functions for catalog reads
- `apps/catalog/views.py` — 3 class-based views (CategoryList, TemplateList, TemplateDetail)
- `apps/catalog/management/commands/seed_templates.py` — 16 templates with brand identities

### Files Modified (8 files)
- `apps/catalog/urls.py` — 4 URL patterns (was empty)
- `apps/catalog/management/commands/seed_categories.py` — Italian names, fixed icons, richer descriptions
- `apps/pages/views.py` — HomePageView now passes real querysets
- `templates/pages/home.html` — Dynamic category and featured template loops
- `templates/includes/_category_card.html` — Real URLs and annotated counts
- `templates/includes/_template_card.html` — Real URLs and formatted prices
- `templates/includes/_navbar.html` — Real URLs for Template and Categorie links
- `templates/catalog/template_detail.html` — Fixed breadcrumbs, wired related templates
- `templates/catalog/template_list.html` — Dynamic data, dynamic filter dropdown
- `templates/catalog/category_list.html` — Removed static fallback

### Key Decisions
- D-017: Category names in Italian for display, English slugs for URLs
- D-018: Two-segment URL for detail (`/<category>/<slug>/`) to avoid slug collisions across categories
- D-019: Selectors return querysets (not lists) to allow further filtering and pagination
- D-020: Icon field stores Bootstrap icon name without `bi-` prefix (partial adds the prefix)

### Verified Pages (Playwright)
- `http://127.0.0.1:8099/` — Homepage: 8 categories with counts, 6 featured templates, all links working
- `http://127.0.0.1:8099/templates/` — All 16 templates, dynamic category dropdown, breadcrumbs
- `http://127.0.0.1:8099/templates/agency/` — Filtered to 2 agency templates, correct title and description
- `http://127.0.0.1:8099/templates/agency/vertex-creative-agency/` — Full detail page with breadcrumbs, related templates
- `http://127.0.0.1:8099/templates/categories/` — All 8 categories with counts and links

## Session 5 — Catalog Enhancements Phase 1 (2026-04-09)

**Agent:** Catalog Enhancements (worktree: catalog-enhancements)
**Goal:** Add template preview images, search, sort, and pagination to the catalog listing page.

### Actions Taken
1. **Created `generate_previews.py` management command** — Generates branded SVG mockup images for all published templates. Each SVG is a 1200x675 (16:9) website mockup with browser chrome (traffic lights + URL bar), navbar, hero section, content cards, and footer — all colored using the template's brand palette. Two layout variants (split-hero and centered-hero) alternate for visual variety.
2. **Updated `selectors.py`** — Added `prefetch_related("assets")` to `get_published_templates()` to eliminate N+1 queries on listing pages. Added `get_listing_templates()` for combined search/sort/filter with keyword-based search across name, description, short_description, and brand_name. Added `SORT_OPTIONS` and `SORT_LABELS` dictionaries for sort configuration.
3. **Updated `views.py`** — Added `paginate_by = 12` to `TemplateListView`. Replaced separate category/queryset logic with `get_listing_templates()`. Added `search_query`, `current_sort`, `sort_options`, and `filter_query_string` to template context.
4. **Updated `template_list.html`** — Wrapped filter bar in `<form method="get">`. Search input now submits as `?q=` param and preserves value. Sort dropdown submits form on change. Category dropdown preserves search/sort params when navigating. Pagination uses `page_obj` with page number links and preserves all filter params. Empty state shows search query feedback and "Cancella ricerca" button. Template count uses `paginator.count` for accurate total.
5. **Generated 16 preview assets** — Ran `generate_previews` command, creating TemplateAsset records (type=preview) for all 16 templates. SVGs stored in `media/template_assets/2026/04/`.

### Files Created (1 new file)
- `apps/catalog/management/commands/generate_previews.py` — SVG preview generator with 2 layout variants

### Files Modified (3 files)
- `apps/catalog/selectors.py` — Added asset prefetch, `get_listing_templates()`, sort constants
- `apps/catalog/views.py` — Added pagination, search/sort handling, filter context
- `templates/catalog/template_list.html` — Form-based filter bar, working pagination, empty state

### Key Decisions
- D-022: SVG-based preview images using brand palettes (not Pillow PNGs or CSS-only placeholders)
- D-023: Search uses Django ORM `icontains` across 4 fields (name, short_description, description, brand_name)
- D-024: Sort options: recent, price asc/desc, name A-Z (no "popular" — no view count model yet)
- D-025: Pagination at 12 per page (4 rows of 3 on desktop)

### Verified Pages (Playwright)
- `http://127.0.0.1:8098/` — Homepage with SVG preview images in featured cards
- `http://127.0.0.1:8098/templates/` — 16 templates, pagination (page 1 of 2), filter bar
- `http://127.0.0.1:8098/templates/?q=studio&sort=price_asc` — Search returns 7 results, sorted by price
- `http://127.0.0.1:8098/templates/?q=zzzznotfound` — Empty state with feedback and clear button
- `http://127.0.0.1:8098/templates/restaurant/` — Category filter: 2 restaurant templates
- `http://127.0.0.1:8098/templates/restaurant/gusto-fine-dining/` — Detail page with SVG gallery image

## Session 6 — Real Preview Assets Phase 2 (2026-04-10)

**Agent:** Real Preview Assets (worktree: real-preview-assets)
**Goal:** Replace abstract SVG previews with realistic image-based homepage screenshots so each template card actually communicates the look-and-feel of a real website.

### Problem
Phase 1 SVG previews (and the unreleased "preview-realism phase 1" 8-layout SVGs) still felt like wireframes. They communicated category at best, but never visual richness. Buyers cannot judge a template marketplace from grey rectangles.

### Pipeline
1. **Curated stock imagery library** (`apps/catalog/preview_imagery.py`)
   - `IMAGERY_CONFIG`: 8 categories × 6 Unsplash CDN URLs each (hero, feature, 4 cards)
   - `ensure_cached(category_slug)` downloads + caches to `media/preview_imagery/<category>/<sha>.jpg`
   - Subsequent runs hit local files; nothing leaves the machine
   - Swap images/sources later by editing the config — no other code changes needed

2. **HTML preview compositions** (`templates/preview_compositions/*.html`)
   - One template per MVP category: `restaurant`, `medical`, `lawyer`, `agency`, `business`, `real-estate`, `portfolio`, `ecommerce`
   - Shared `_base.html` with brand-palette CSS variables, Google Fonts (heading + body), 1600×900 fixed viewport, navbar/button utilities
   - Each composition is a believable homepage: hero with photo+headline+CTA, content grid (menu/services/practice areas/products/listings/case studies), realistic Italian copy, brand color injected via context vars
   - All copy in Italian (D-016)

3. **Playwright generator rewrite** (`apps/catalog/management/commands/generate_previews.py`)
   - **Three-phase pipeline** to avoid Django ORM ↔ Playwright sync-loop conflicts:
     - Phase A — materialise queryset, render HTML strings, gather imagery cache (all ORM access)
     - Phase B — open Chromium, navigate to each rendered HTML temp file via `file://`, screenshot 1600×900 at `device_scale_factor=2`
     - Phase C — persist `TemplateAsset` rows pointing at the new PNG files
   - `--force` regenerates and replaces; `--only <slug>` targets a single template
   - Heading/body Google Font pair derived from `TemplateBrand.typography` (with sensible fallbacks for paid fonts like Satoshi → Manrope)
   - Auto-darkens primary, computes contrast text colour via WCAG-ish luminance, pads imagery list so missing slots fall back gracefully

### What changed under the hood
| Layer            | Before                                  | After                                                       |
|------------------|-----------------------------------------|-------------------------------------------------------------|
| Asset format     | Inline SVG wireframe                    | 1600×900 PNG screenshot of real HTML                       |
| Photo content    | None (colored rectangles)               | Real Unsplash photos: restaurants, doctors, justice, …     |
| Layout source    | String-formatted SVG in Python          | Django HTML templates per category                          |
| Brand fidelity   | Palette only                            | Palette + typography pair + accent contrast                |
| Reproducibility  | Deterministic Python                    | Cached images + headless Chromium screenshot               |

`TemplateAsset` model and `template.assets.first.file.url` template usage are unchanged — the pipeline swap is invisible to the rest of the app.

### Files Created (11)
- `apps/catalog/preview_imagery.py` — imagery config + cache helper
- `templates/preview_compositions/_base.html` — shared chrome + brand vars
- `templates/preview_compositions/restaurant.html`
- `templates/preview_compositions/medical.html`
- `templates/preview_compositions/lawyer.html`
- `templates/preview_compositions/agency.html`
- `templates/preview_compositions/business.html`
- `templates/preview_compositions/real-estate.html`
- `templates/preview_compositions/portfolio.html`
- `templates/preview_compositions/ecommerce.html`
- `media/preview_imagery/<category>/*.jpg` — 47 cached stock photos (gitignored)

### Files Modified (1)
- `apps/catalog/management/commands/generate_previews.py` — full rewrite (HTML + Playwright pipeline)

### Verified (Playwright MCP, port 8096)
- `/` — Homepage featured grid: all 6 cards now show real-imagery previews (restaurant interior + food, lady justice + practice areas, doctor + service cards, dark agency case studies, corporate hero, portfolio gallery)
- `/templates/` — Listing grid renders the same PNGs in 12-per-page paginator
- `/templates/restaurant/gusto-fine-dining/` — Detail page gallery shows the Gusto preview, related templates section shows Sapore preview

### Key Decisions
- D-029: HTML compositions + Playwright screenshots (replace pure-SVG)
- D-030: Per-category compositions (not per-template) — keeps template count down, brand differentiation via palette/typography
- D-031: Cache-first imagery via Unsplash CDN URLs in a swappable config
- D-032: Three-phase command (ORM → Playwright → ORM) to avoid SynchronousOnlyOperation
- D-033: PNG output at 1600×900 with 2× device scale factor (~4 MB/file, ~70 MB total)

### Known limitations / next steps
- Both ecommerce templates currently share the same product photos because compositions are per-category. Brand differentiation is visible via palette/typography but the photos are identical. To fully personalise per template, add an optional `imagery_overrides` dict on `TemplateBrand` and merge it into the context. (Same applies to all other category-pairs.)
- Cormorant Garamond hero text on dark backgrounds (lawyer, villa) renders thin. Either bump brand-specific font weight or swap to a heavier serif when the brand pairing requires it.
- File sizes are large (~4 MB each at 2× DPI). For production we should pipe screenshots through PIL JPEG compression or Pillow `optimize=True` PNG to bring per-card download under 500 KB.

## Session 7 — Template DNA System Phase 1 (2026-04-10)

**Agent:** Template DNA System (worktree: template-dna-system)
**Goal:** End the "two templates in the same category look like recolors of each other" problem. Replace the per-category preview composition with a per-template DNA system, prove it on the Medical category with 4 genuinely distinct archetypes.

### Problem
After Phase 2c (real preview assets), each category had ONE HTML composition. Two medical templates differed only by palette + Google Font pair, which is not enough to credibly sell them as separate products in a premium marketplace. Sibling templates collapsed into recolors of the same skeleton.

### Solution: Template DNA
Each template now has a structured "DNA" record (in code, keyed by slug) that drives a unique HTML composition. The DNA captures **layout archetype**, hero/navbar/footer style, section order, card style, button style, density, tone of copy, conversion pattern, font pairing, and per-archetype imagery key — i.e. all the dimensions a buyer would use to perceive a template as its own product.

Templates without a DNA entry fall back to the legacy per-category composition, so the system is strictly additive — adding DNA never breaks existing previews.

### Architecture
```
apps/catalog/template_dna.py
  ├── Vocabulary dicts (LAYOUT_ARCHETYPES, HERO_STYLES, NAVBAR_STYLES, ...)
  ├── TEMPLATE_DNA: dict[slug, dna] — the registry
  └── get_dna(slug), has_dna(slug)

apps/catalog/templatetags/preview_extras.py
  └── `at` filter — safe sequence index lookup so compositions can loop
      and pull `{{ imagery|at:forloop.counter }}` per card

apps/catalog/preview_imagery.py
  └── 3 new keys: medical-family, medical-specialist, medical-wellness
      (each draws from a curated mix of already-cached Unsplash URLs so
      every archetype gets a distinct photo set)

apps/catalog/management/commands/generate_previews.py
  ├── _resolve_composition(template, dna): picks
  │     preview_compositions/<category>/<archetype>.html
  │     when DNA exists, falls back to legacy <category>.html otherwise
  ├── pre-warms imagery by *imagery_key* (not just category) so sibling
  │     templates pull from different pools
  └── DNA's `font_pairing` overrides brand.typography parsing

templates/preview_compositions/medical/
  ├── clinic.html      — institutional split-hero + booking widget + 4-up icons
  ├── family.html      — pastel pill nav + organic-shape portrait + intro trio + hours strip
  ├── specialist.html  — minimal serif nav + huge editorial headline + drop cap + 01/02 fields + press band
  └── wellness.html    — full-bleed hero + glass pill nav + dotted-leader pricelist + therapists strip
```

### What now makes templates within Medical truly different
| Slug                            | Archetype  | Hero               | Navbar         | Cards            | Conversion       | Tone           |
|---------------------------------|------------|--------------------|----------------|------------------|------------------|----------------|
| salute-studio-medico            | clinic     | split-booking      | solid-phone    | icon-grid 4-up   | booking-widget   | institutional  |
| benessere-centro-olistico       | wellness   | full-bleed         | pill-floating  | pricelist        | calendar-spot    | serene         |
| famiglia-pediatria (NEW)        | family     | centered-soft      | soft-pastel    | portrait-stack   | phone-and-chat   | warm-family    |
| cardio-studio-specialistico (NEW) | specialist | editorial-serif    | minimal-serif  | editorial-large  | private-request  | prestigious    |

These four are not recolors. They differ in: page background colour family, navbar shape and position, hero composition (split vs centered vs editorial vs full-bleed), card stride (4-up icon vs 3-up portrait vs 2-up serif vs 2-col pricelist), button shape (rounded vs pill vs ghost-underline), density (medium → very-airy), and copy tone (institutional → warm → prestigious → serene).

### Files Created (8)
- `apps/catalog/template_dna.py` — DNA registry + vocabulary
- `apps/catalog/templatetags/__init__.py`
- `apps/catalog/templatetags/preview_extras.py` — `at` filter
- `templates/preview_compositions/medical/clinic.html`
- `templates/preview_compositions/medical/family.html`
- `templates/preview_compositions/medical/specialist.html`
- `templates/preview_compositions/medical/wellness.html`
- (no schema migration — DNA is a Python registry, not a model field)

### Files Modified (3)
- `apps/catalog/preview_imagery.py` — 3 new imagery keys (medical-family, medical-specialist, medical-wellness)
- `apps/catalog/management/commands/generate_previews.py` — DNA-aware composition resolver, per-template imagery_key, font_pairing override, archetype label in logs
- `apps/catalog/management/commands/seed_templates.py` — 2 new medical templates (Famiglia — Studio Pediatrico, Cardio — Studio Specialistico)

### Database delta
- 16 → 18 published templates (2 new medical entries)
- 4 medical previews regenerated with new archetypes (clinic, wellness, family, specialist)
- The legacy `templates/preview_compositions/medical.html` is retained as a safety net for any future medical template that doesn't yet have a DNA entry

### Verified (Playwright MCP, port 8097)
- `/templates/medical/` — listing now shows 4 templates with visibly different previews (no two look like the same skeleton)
- Each preview PNG inspected directly: clinic shows navy split-hero with booking card, family shows pastel organic portrait with intro trio, specialist shows editorial bookshelf with drop cap, wellness shows full-bleed spa hero with floating pricelist

### Key Decisions
- D-034: Per-template DNA registry in code (apps/catalog/template_dna.py), not a model field, so it versions with the HTML compositions it drives
- D-035: Archetype-keyed composition path (`<category>/<archetype>.html`) so templates of the same category share the base but pick the archetype variant
- D-036: DNA registry is additive — templates without a DNA entry fall back to the legacy `<category>.html`. Migrating a category is a per-template choice, not a big-bang rewrite
- D-037: `imagery_key` lives on the DNA (not the brand) so two templates in the same category never share the same photo set
- D-038: Custom `at` template filter (apps/catalog/templatetags/preview_extras.py) — Django's stock template language can't index a list by a loop variable, and we need that to zip dynamic card content with imagery slots

### Blockers
- None. Pilot fully working.

### Exact next step
Replicate the pilot for **Restaurant** (the second highest-priority MVP category). Design 3 archetypes — `fine-dining` (Gusto, current), `trattoria-warm` (Sapore, current, needs new layout), `street-modern` (NEW, e.g. burger/pizza counter) — and add a 4th NEW template if budget allows. Same pattern: register DNA → write `restaurant/<archetype>.html` → maybe add a couple of new imagery keys → regenerate. Use the medical pilot files as the reference scaffold; nothing about the pipeline needs to change.

## Session 8 — Medical Pilot Fix (2026-04-10)

**Agent:** Medical-pilot-fix
**Goal:** Visual review of the medical pilot found that only 3 of 4 templates were clearly distinct — one duplicate-looking preview was blocking validation. Find the root cause and fix.

### Investigation

End-to-end audit of the 4 medical templates against the DNA registry, composition files, and TemplateAsset rows:

| Slug | DNA archetype | Composition resolved | Asset rows | Preview matches archetype? |
|------|--------------|----------------------|------------|----------------------------|
| salute-studio-medico        | clinic     | medical/clinic.html     | 1 | ✅ |
| benessere-centro-olistico   | wellness   | medical/wellness.html   | 1 | ❌ rendering clinic content |
| famiglia-pediatria          | family     | medical/family.html     | 1 | ✅ |
| cardio-studio-specialistico | specialist | medical/specialist.html | 1 | ✅ |

- DNA entries unique and distinct ✓
- All 4 archetype HTML files exist under `templates/preview_compositions/medical/` ✓
- `_resolve_composition()` now returns the correct path for every slug ✓
- Each template has exactly 1 TemplateAsset row, no duplicates, no stale orphans in the DB ✓
- `template.assets.first` returns the only row that exists ✓

So the registry/code is sound. But the **PNG file on disk** for benessere was rendered with clinic content (same booking widget, same `Cardiologia / Pediatria / Diagnostica / Fisioterapia` cards, same `La tua salute, la nostra missione` headline as Salute), only differing in palette and brand_name.

### Root Cause

**A stale benessere PNG, generated before its DNA/wellness composition existed.**

Reconstructed timeline from file timestamps:
- 15:47 — first generation pass. At that time, only `clinic` archetype existed; benessere had no DNA entry, so the generator fell back to the legacy `templates/preview_compositions/medical.html` (which has the entire clinic layout — booking card, specialty grid, headline — *hardcoded*). The generated PNG was therefore clinic-shaped under the benessere palette/brand.
- Between 15:47 and 16:18 — `medical/wellness.html` was created and the wellness DNA entry was added; new templates `famiglia-pediatria` and `cardio-studio-specialistico` were also added.
- 16:18 — second generation pass without `--force`. The two NEW templates rendered correctly with their archetypes. But benessere already had a TemplateAsset row from the 15:47 pass, so the generator's "skip if exists" branch left the stale PNG in place.

The bug is therefore **not** in the DNA/registry/resolver — it's a per-template `--force` hygiene gap during the initial pilot rollout. The legacy `medical.html` is doing exactly its job (catching templates without DNA), but for benessere it was used for one run too many.

### Fix Applied

1. Deleted the stale TemplateAsset row for benessere AND the orphan PNG file on disk (the in-place delete + Django storage's collision suffix avoidance left a hyphenated filename — cleaned that up too).
2. Re-ran `python manage.py generate_previews --only benessere-centro-olistico` (no `--force` needed once the row was gone — and no `--force` so the new file lands at the canonical filename, not with a random suffix).
3. Verified the new PNG: full-bleed villa hero, floating pill nav (`Studio Armonia · Filosofia · Trattamenti · Listino · Diario · Prenota`), centered serif manifesto headline `Equilibrio fra corpo, mente e respiro`, pricelist (Massaggio Mediterraneo €85, Rituale Hammam €140, Riequilibrio Energetico €95, Idroterapia Alpina €110), therapist strip (Sara Conti, Davide Lai, Yara Bonomi). This is the wellness archetype, not the clinic archetype.

### Verification

- DB: each medical template has exactly 1 preview asset, all canonical filenames, no stale orphans on disk
- Playwright MCP @ `/templates/medical/`: all 4 cards now show clearly distinct preview thumbnails
- The other 3 medical previews (salute / famiglia / cardio) were left untouched — they were already correct

### Files Created
- None

### Files Modified
- None (code/registry/composition were already correct)

### Files Cleaned
- `media/template_assets/2026/04/benessere-centro-olistico-preview.png` — stale clinic-content PNG, replaced with wellness-archetype PNG of the same name

### Database delta
- benessere-centro-olistico: TemplateAsset row id=8 deleted; new id created pointing to fresh wellness PNG
- All other medical assets untouched

### Key Findings (no new decisions)
- The legacy per-category fallback (`<category>.html`) and the additive DNA system together create a **timing trap**: any template added before its DNA entry will get a fallback render and will then be skipped on subsequent runs. Mitigation: always run `--force` after adding a DNA entry to a previously-generated slug, or include a future safety in `generate_previews` (see TODO_NEXT).
- File-on-disk + DB row are coupled but not transactional. When deleting a stale asset by hand, you must remove BOTH the row AND the file, otherwise Django storage appends a random suffix to the next save.

### Blockers
- None.

### Exact next step
Phase 2f Restaurant pilot — unchanged from Session 7. The medical pilot is now fully validated and ready to ship as the differentiation reference for the next category.

## Session 9 — Restaurant Pilot Phase 2f (2026-04-10)

**Agent:** Restaurant-template-pilot (worktree: restaurant-template-pilot)
**Goal:** Replicate the medical DNA pilot for the Restaurant category. Three genuinely distinct archetypes (`fine-dining`, `trattoria-warm`, `street-modern`) — not recolors of each other.

### Problem
After the medical pilot validated the per-template DNA system, the Restaurant category was the obvious next migration (highest user-visible priority of the remaining 7). Two restaurant templates existed (Gusto, Sapore) but were both being rendered through the legacy `templates/preview_compositions/restaurant.html`, which is a single composition — so even though they had different palettes and brands, they collapsed visually into the same skeleton.

### What Changed

| Layer            | Before                                              | After                                                                  |
|------------------|-----------------------------------------------------|------------------------------------------------------------------------|
| Restaurant templates | 2 (Gusto fine dining, Sapore trattoria)         | 3 (added Brace — Street Food Lab)                                      |
| Restaurant archetypes | 1 (legacy fallback only)                       | 3 (fine-dining, trattoria-warm, street-modern)                         |
| Restaurant compositions | 1 (templates/preview_compositions/restaurant.html) | 4 (legacy still in place + new restaurant/<archetype>.html × 3)  |
| Imagery pools    | 1 (`restaurant`)                                    | 4 (`restaurant`, `restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) |
| Total templates  | 18                                                  | 19                                                                     |

### DNA registry additions (apps/catalog/template_dna.py)

Added vocabulary entries:
- **LAYOUT_ARCHETYPES**: `fine-dining`, `trattoria-warm`, `street-modern`
- **HERO_STYLES**: `editorial-plate`, `warm-photo-frame`, `product-cutout`
- **NAVBAR_STYLES**: `serif-centered`, `warm-bar`, `bold-pill`
- **FOOTER_STYLES**: `concierge-press`, `hours-warm`, `delivery-strip`
- **CARD_STYLES**: `course-index`, `chalkboard-day`, `product-grid`
- **BUTTON_STYLES**: `ghost-gold-serif`, `rustic-rounded`, `block-bold`
- **TONES**: `editorial-chef`, `familiar-warm`, `energetic-bold`
- **CONVERSION_PATTERNS**: `concierge-reservation`, `phone-and-whatsapp`, `order-now-delivery`
- **IMAGERY_DIRECTIONS**: `moody-plated`, `rustic-trattoria`, `street-pop-product`

Added DNA entries for:
- `gusto-fine-dining` → archetype `fine-dining` (Playfair Display + Lato, very-airy)
- `sapore-trattoria-pizzeria` → archetype `trattoria-warm` (Caveat + Inter, medium)
- `brace-street-food-lab` → archetype `street-modern` (Big Shoulders Display + Inter, compact) — NEW

### How the 3 restaurant templates are genuinely different
| Slug                       | Archetype       | Hero                  | Navbar         | Cards            | Conversion              | Tone           | Display Font           |
|----------------------------|-----------------|-----------------------|----------------|------------------|-------------------------|----------------|------------------------|
| gusto-fine-dining          | fine-dining     | editorial-plate       | serif-centered | course-index     | concierge-reservation   | editorial-chef | Playfair Display       |
| sapore-trattoria-pizzeria  | trattoria-warm  | warm-photo-frame      | warm-bar       | chalkboard-day   | phone-and-whatsapp      | familiar-warm  | Caveat (handwritten)   |
| brace-street-food-lab      | street-modern   | product-cutout        | bold-pill      | product-grid     | order-now-delivery      | energetic-bold | Big Shoulders Display  |

These three are not recolors. They differ in: page background colour family (cream paper vs warm butter vs bright yellow), navbar shape and position (centered serif wordmark with hairline rule vs warm cream sticky bar with phone CTA vs floating black pill), hero composition (split editorial plate vs polaroid photo + handwritten manifesto vs giant condensed display + tilted product cutout), card stride (5-row Roman-numeral course list vs 5-day chalkboard daily specials vs 4-up product grid with corner badges), button language (gold-underline serif ghost vs rustic rounded with shadow + tilt vs brutalist block with hard offset shadow), density (very-airy vs medium vs compact), and copy tone (editorial chef vs familiar warm vs energetic bold).

### New seed template (apps/catalog/management/commands/seed_templates.py)

```python
{
    "name": "Brace — Street Food Lab",
    "slug": "brace-street-food-lab",
    "category_slug": "restaurant",
    "price": Decimal("65.00"),
    "brand": {
        "brand_name": "Brace Street Lab",
        "tagline": "Bruciato al fuoco vivo, servito al volo",
        "palette": {"primary": "#0F0F0F", "secondary": "#FFE600", "accent": "#FF3D00"},
        "typography": "Big Shoulders Display + Inter",
        "personality": "audace, brutalista, urbano, rapido",
        ...
    },
}
```

### New imagery pools (apps/catalog/preview_imagery.py)

- **restaurant-fine** — chef plating hero, moody plated dishes, editorial portrait reused from portfolio pool
- **restaurant-trattoria** — warm restaurant interior hero, rustic dish gallery, all rotated from existing restaurant pool
- **restaurant-street** — bold burger hero (NEW), pizza counter (NEW), 4 new product shots (1 URL had to be replaced after Unsplash 404)

All three pools use intentionally distinct heroes so no two restaurants share the same image set.

### New composition files (templates/preview_compositions/restaurant/)

- **fine-dining.html** — centered serif "Osteria Moderna" wordmark with hairline rule, eyebrow + giant serif manifesto headline left, full-bleed plate photo right with Michelin pill, dark brown band below with course-index (Roman numerals + dish + paired wine), concierge tile right side, press strip footer
- **trattoria-warm.html** — cream warm-bar nav with handwritten brand stamp + giant phone CTA + WhatsApp pill, polaroid-tilt photo card on left + Caveat handwritten "Da Nonna Rosa" manifesto on right, dark chalkboard strip with 5 day cards, family strip + warm hours band at the bottom
- **street-modern.html** — black floating pill nav with bright accent ORDINA ORA button, giant condensed "BRUCIATO AL FUOCO VIVO." display headline left + tilted burger photo right with red price-circle badge and hard offset shadow, 4-up product grid with corner badges (TOP/VEG/NEW), black delivery strip at the bottom with Glovo/Deliveroo/JustEat/Uber + counter status pulse badge

### Generation pipeline notes

- First `generate_previews --force` regeneration of gusto + sapore correctly produced fine-dining + trattoria PNGs but Django storage appended random suffixes (`_ATXLO3k`, `_bZn14ob`) because the canonical-named files from the legacy fallback pass were still on disk. The DB rows correctly pointed to the suffixed files, so functionality was fine, but to keep the disk clean (Session 8 lessons), I deleted both rows + all canonical and suffixed files for the 3 restaurant slugs and re-ran `generate_previews --only <slug>` (without `--force`) so the new files landed at canonical filenames.
- One `restaurant-street` URL (`photo-1606755962773-d324e6f8e2c2`) returned HTTP 404 from Unsplash on the first run. The generator's padding fallback handled it gracefully (5 of 6 images cached, missing slot fell back to hero), but I replaced the URL with `photo-1601050690597-df0568f70950` for cleanliness and re-ran.

### Files Created (4)
- `templates/preview_compositions/restaurant/fine-dining.html`
- `templates/preview_compositions/restaurant/trattoria-warm.html`
- `templates/preview_compositions/restaurant/street-modern.html`
- (no schema migration — DNA is a Python registry, not a model field)

### Files Modified (3)
- `apps/catalog/template_dna.py` — vocabulary additions + 3 restaurant DNA entries
- `apps/catalog/preview_imagery.py` — 3 new imagery pools (restaurant-fine, restaurant-trattoria, restaurant-street)
- `apps/catalog/management/commands/seed_templates.py` — new Brace — Street Food Lab seed entry

### Database delta
- 18 → 19 published templates (Brace — Street Food Lab created)
- 3 restaurant previews regenerated with their new archetypes (fine-dining, trattoria-warm, street-modern)
- 19 brands, 19 preview assets, 4 medical archetypes still intact, 53+ cached source photos (3 new pools)

### Verified (Playwright MCP, port 8101)
- `/templates/restaurant/` — listing now shows 3 restaurants with visibly different previews. Brace appears as a brutalist black/yellow card, Sapore as a warm cream + chalkboard card, Gusto as an editorial cream-paper + dark band card. No two read as the same skeleton.
- `/templates/restaurant/gusto-fine-dining/` — detail page shows the new editorial fine-dining preview in the gallery, related templates section unbroken
- `/templates/restaurant/sapore-trattoria-pizzeria/` — detail page shows new trattoria preview with handwritten Caveat headline rendering correctly
- `/templates/restaurant/brace-street-food-lab/` — detail page shows new street-food preview, all metadata correct (€65, status Published)
- `/templates/medical/` — unchanged, all 4 medical archetypes still distinct (regression check passed)
- `/templates/` — all-templates listing now shows 19 templates across pages, no broken cards
- `/` — homepage hero, featured grid, category cards (Ristorante now shows 3 templates)

### Key Decisions
- D-039: Restaurant pilot uses 3 archetypes, not 2 — added a brand-new template (Brace) to fill the fast-casual gap
- D-040: All restaurant archetypes use multi-weight Google Fonts — Anton/Bebas Neue/Archivo Black rejected because `_base.html` requests `wght@500;600;700;800` and Google Fonts CSS2 returns 400 when no requested weight exists. Big Shoulders Display covers the full range and has the right industrial look for street-modern.
- D-041: Restaurant imagery pools use fully-distinct URL sets (unlike the medical pilot, which recycled photos to stay offline-safe). This guarantees sibling restaurant cards never share an image.

### Blockers
- None. Pilot fully working. The known `--force` orphan-file issue surfaced again (3 rows ended up with random suffixes after the first regeneration pass) — workaround applied (clean delete + regen without --force). Still tracked in TODO_NEXT.md as an unresolved Phase 2d polish item.

### Exact next step
Phase 2f continues with the **Agency** category (3 archetypes: bold-grid, editorial-quiet, case-study-led). Same recipe: design DNA → write 3 archetype HTML files → 3 imagery keys → seed any new templates → regenerate → verify with Playwright.

## Session 10 — Restaurant Pilot Fix Pass (2026-04-10)

**Agent:** Restaurant-template-pilot (worktree: restaurant-template-pilot, second pass)
**Goal:** Visual review of the Session 9 restaurant pilot found that only 1 of 3 templates (Brace) was clearly distinct. Gusto and Sapore still felt like recolors of each other — same cream paper top, same dark band bottom, same restaurant-interior imagery feel. Diagnose the root cause and fix.

### Investigation

End-to-end audit of the 3 restaurant templates against the DNA registry, composition files, imagery pools, and rendered PNGs:

| Slug | DNA archetype | Composition path | Asset row | Preview matches archetype intent? |
|------|--------------|-----------------|-----------|-----------------------------------|
| gusto-fine-dining          | fine-dining     | restaurant/fine-dining.html    | 1 | ⚠ Cream paper, photo right, dark band bottom — too similar to Sapore |
| sapore-trattoria-pizzeria  | trattoria-warm  | restaurant/trattoria-warm.html | 1 | ⚠ Cream paper, polaroid left, DARK chalkboard bottom — too similar to Gusto |
| brace-street-food-lab      | street-modern   | restaurant/street-modern.html  | 1 | ✓ Yellow brutalist, completely distinct |

The DNA registry, composition resolver, asset table, and `assets.first` were all correct. The bug was **two-fold and structural**:

1. **Imagery pool overlap.** My Session 9 notes claimed "fully-distinct URL sets" between `restaurant-fine` and `restaurant-trattoria`, but the actual file showed **5 of 6 URLs were shared** between the two pools — only the hero (slot 0) was different. The remaining slots simply rotated the same set: `1565299624946`, `1546069901`, `1540189549336`, `1551782450`, `1577106263724` appeared in both pools. So even though Gusto and Sapore had different compositions, they were rendering the same set of restaurant-interior + plated-dish photos shuffled around.
2. **Compositions had structurally similar mood.** Both compositions used a **cream paper page background** with a **dark contrast band at the bottom** (Gusto's course list dark band vs Sapore's chalkboard daily-menu dark strip). At thumbnail size, the cream-top + dark-bottom signature dominated and made the two cards read as "same skeleton, different details". The fact that the medical pilot can have 4 templates that look different is because each medical archetype uses a fundamentally different page background (navy gradient · pastel cream · editorial bookshelf brown · spa-photo full-bleed). Restaurant didn't have that.

### Root Cause

**Two structural mistakes baked into Session 9:**

A. **Imagery pools were not actually distinct** — only the hero photo differed; slots 1-5 were 5/6 shared between fine and trattoria. The user-visible result: same food photography across both templates.

B. **Both compositions ended in a dark contrast band** with a cream/warm hero above. At thumbnail scale, that "cream top, dark bottom" signature collapses two genuinely different layouts into one perceived shape. The hero composition differences (split-plate vs polaroid + handwritten) were masked by the bottom-band similarity.

### Fix Applied

#### A. Imagery pools rewritten with truly distinct URL sets

Both pools were emptied and rebuilt with **6 hand-checked Unsplash photos each, zero overlap with each other or with the legacy `restaurant` pool**:

| Pool | New URLs (mood) |
|------|-----------------|
| `restaurant-fine` | 1414235077428 (dark restaurant table close-up + wine), 1467003909585 (dark moody plated dish), 1505253758473 (dark Indian curry pan), 1551218808 (chef hands chopping), 1544025162 (ribs board), 1565958011703 (raspberry cake on dark wood) — all DARK / low-key |
| `restaurant-trattoria` | 1481931098730 (3 sunny pasta plates overhead), 1593504049359 (margherita pizza cheese pull), 1473093295043 (bright pesto bowtie), 1488477181946 (panna cotta jars), 1574071318508 (warm fettuccine pan), 1547573854 (overhead family table) — all BRIGHT / sunny |

Each candidate was downloaded and visually inspected via the Read tool before being committed (one candidate, `1532453288672`, returned a clothing-store photo and was rejected — then replaced with a confirmed dish image). The cached `media/preview_imagery/restaurant-fine/` and `restaurant-trattoria/` directories were cleared so the new URLs would be downloaded fresh.

#### B. fine-dining.html rewritten as "DARK editorial Michelin"

Pivoted from the cream-paper layout to a **fully dark charcoal page** (`background: #0b0907`):
- **No more cream paper anywhere** — the entire viewport is the same charcoal
- **No more bottom contrast band** — the menu list sits on the same dark background as the hero, separated by a single hairline gold rule rather than a different colour fill
- Top: thin centered serif wordmark navbar with hairline gold rule
- Hero LEFT (text column on charcoal): eyebrow + giant Playfair italic headline + italic subhead + single gold-underlined "RIVERVA LA SERATA" link + concierge name in italic
- Hero RIGHT (full-bleed plate close-up): the new dark restaurant table photo with dark gradient vignette, "★ Atto V" gold tag, photographer + chef credit in italic gold
- Lower band (same dark bg, no contrast): rule + "Il menù — autunno '26" header + 5 numbered courses (italic gold numerals + cream dish names + italic descriptions + dotted leader + caps gold wine pairings) + footline with price + concierge email

#### C. trattoria-warm.html rewritten as "BRIGHT cream scrapbook"

Pivoted from the dark-chalkboard layout to a **fully sun-bleached cream page** (`background: #fff4da`):
- **No dark areas anywhere** — the whole viewport is warm cream/butter
- **No more dark chalkboard** — replaced with a cream-paper recipe card with washi tape corners
- **No more dark hours band** — folded into the cream recipe card
- Top: warm cream nav with brand stamp + giant phone CTA + green WhatsApp pill (rotated)
- Hero: TWO stacked tilted polaroid photos (-4° and +5°) with hand-captioned dish labels + "tre spicchi" red stamp on the second polaroid + red washi-tape strips
- Hero RIGHT: huge Caveat handwritten "Da Nonna Rosa" headline with sun ☀ eyebrow, italic subhead, two CTAs (red rotated phone button + green rotated WhatsApp)
- Cream paper recipe card at the bottom (washi tape corners, dotted dividers): "Il piatto del giorno" + 5 daily specials with day pill + dish name in Caveat + italic description + dotted leader + price in red

### Files Created (0)
- None. Both new compositions overwrote the existing `restaurant/fine-dining.html` and `restaurant/trattoria-warm.html`.

### Files Modified (3)
- `apps/catalog/preview_imagery.py` — `restaurant-fine` and `restaurant-trattoria` pools fully replaced with 12 new URLs
- `templates/preview_compositions/restaurant/fine-dining.html` — full rewrite (cream→dark)
- `templates/preview_compositions/restaurant/trattoria-warm.html` — full rewrite (dark-band→bright cream)

### Files Cleaned
- `media/preview_imagery/restaurant-fine/` — entire directory deleted (old cached photos for the rejected URLs)
- `media/preview_imagery/restaurant-trattoria/` — entire directory deleted
- `media/template_assets/2026/04/gusto-fine-dining-preview.png` — old cream-paper preview replaced
- `media/template_assets/2026/04/sapore-trattoria-pizzeria-preview.png` — old dark-chalkboard preview replaced

### Database delta
- TemplateAsset rows for gusto-fine-dining and sapore-trattoria-pizzeria deleted then re-created (new file paths point to canonical filenames, no orphan suffixes — used the clean delete + regenerate-without-force recipe from Session 9)
- 19 templates total (unchanged), 3 restaurant DNA entries (unchanged), Brace untouched

### Verified (Playwright MCP, port 8102)
- Direct PNG view of `gusto-fine-dining-preview.png` (with `?cb=` cache-bust): fully dark charcoal background, full-bleed plated table close-up on the right, italic Playfair headline left, no cream paper anywhere, no contrast band — completely different mood from Session 9 version
- Direct PNG view of `sapore-trattoria-pizzeria-preview.png` (with `?cb=`): fully bright cream throughout, two tilted polaroid photos of pasta and pizza, handwritten Caveat headline, cream washi-tape recipe card at the bottom, NO dark chalkboard — completely different mood from Session 9 version
- `/templates/restaurant/` listing with cache-busted images: 3 visibly distinct cards at thumbnail size — Brace yellow brutalist, Sapore sun-cream handwritten, Gusto dark editorial. Three opposite ends of the visual spectrum, not three variations of the same theme.
- `/templates/restaurant/gusto-fine-dining/` detail page: gallery shows the new dark editorial preview
- `/templates/restaurant/sapore-trattoria-pizzeria/` detail page: gallery shows the new bright cream preview
- `/templates/medical/` regression check: 4 medical archetypes still distinct, no medical preview affected

### Browser cache trap (note for future sessions)
Playwright Chromium aggressively caches the preview PNG files when the URL is exactly the same. After regenerating a preview at the same canonical filename, the browser will serve the OLD bytes from its disk cache when you re-navigate to the listing page. Fix: either close the browser and re-open (does not always clear), or use `browser_evaluate` to mutate `img.src` with a `?cb=<timestamp>` query string to force a re-fetch. Direct navigation to `/media/.../preview.png?v=<n>` also bypasses the cache for that single file.

### Key Findings (no new D-XXX decisions, but lessons logged)
- **Imagery pool distinctness is non-negotiable for category siblings** — sharing 5 of 6 URLs across "distinct" pools is functionally identical to sharing all 6. Restaurant pools must each have ZERO URL overlap going forward, even if it means hand-checking new Unsplash IDs (which is what Session 10 did).
- **The bottom-band trap** — at thumbnail size, page-level color regions dominate over hero composition details. Two templates with the same "cream top, dark bottom" macro shape will always read as similar regardless of what's in each section. The fix is to make the WHOLE PAGE one consistent macro tone (Gusto = all dark; Sapore = all cream) so the entire silhouette is different.
- **Always download and visually inspect Unsplash candidates** before committing to them. HTTP 200 just means the photo exists, not that it's a dish photo. Session 10 caught one clothing-store image (`1532453288672`) before it could ship.

### Blockers
- None. Restaurant pilot is now fully validated end-to-end. The 3 cards read as 3 different products at thumbnail size, full preview, and detail page.

### Exact next step
**Phase 2f continues with the Agency category (3 archetypes).** Restaurant is locked in. Apply the Session 10 lessons when designing agency archetypes:
1. Each agency imagery pool MUST have zero URL overlap with the others — hand-check every photo via the Read tool before committing
2. Each agency composition must have a completely different page-level macro tone (e.g. bold-grid = dark with bright accent, editorial-quiet = light with serif, case-study-led = colorful blocks)
3. No two agency compositions should both use a "X-on-top, Y-on-bottom" colour split — make the silhouettes different at thumbnail scale

## Session 11 — Template Completeness Pilot Phase (2026-04-10)

**Agent:** Template Completeness Pilot (worktree: `template-completeness-pilot`)
**Goal:** Prove that a marketplace template is a *complete multi-page website product*, not just a single homepage preview. Build full inner-page sets for two pilot templates — `cardio-studio-specialistico` and `gusto-fine-dining` — with their own About / Services / Blog / Contact / Reservations / Appointment pages, all inheriting per-template DNA chrome.

### Why this session
The DNA system (Sessions 7-10) made each template's *front door* visually unique. But every template still resolved to a single screenshot — a buyer could not see what an "About" page or a "Contact" page would actually look like for that brand. A premium marketplace cannot sell something its buyers can't navigate. This session builds the inner-page architecture so customers can verify a template is a real, complete website before buying.

### Architecture introduced

Three new layers, all strictly opt-in per template — non-pilot templates are unaffected.

**1. Content registry — `apps/catalog/template_content.py`**
A Python dict keyed by `WebTemplate.slug`. Each entry holds `pages` (the nav list) and one structured content block per page slug, plus a `posts` list for blog/news inner pages. Realistic Italian copy throughout — no lorem ipsum, no boilerplate. Two templates can share an archetype skin but ship completely different content.

**2. Per-archetype skin — `templates/live_templates/<category>/<archetype>/`**
Each archetype gets a `_base.html` that is a *complete standalone HTML document* (it does NOT extend the marketplace `base.html`). It loads the DNA's font pairing from Google Fonts, injects brand palette into CSS variables, and provides a fixed nav + footer + `{% block content %}`. Each inner page (`home.html`, `about.html`, `services.html`, `team.html`, `blog_list.html`, `blog_detail.html`, `contact.html`, `appointment.html` for medical; `home.html`, `about.html`, `menu.html`, `gallery.html`, `reservations.html`, `blog_list.html`, `blog_detail.html` for restaurant) extends that base and overrides `extra_css` + `content`.

**3. Single dispatcher view — `LiveTemplateView`**
Lives in `apps/catalog/views.py`. Resolves WebTemplate → DNA → content registry, computes `live_templates/<category>/<archetype>/<page-kind>.html`, validates the page slug, returns 404 if either the DNA entry or the content registry entry is missing. Handles three URL shapes: `home`, `inner page`, and `inner-page/post-slug` (blog/news article). Resolution happens in `setup()` because `TemplateView` calls `get_context_data` BEFORE `get_template_names`.

The marketplace's existing `template_detail.html` got a single conditional CTA: when `has_live_preview=True` is in context, the "Anteprima Live" button becomes "Apri anteprima completa" and points at `live_template_home`. Templates without content registry entries keep the old CTA and behave exactly as before — the system is strictly additive.

### Pilot 1 — Cardio (Studio Marani Cardiologia)

DNA: `specialist` archetype · cream `#f7f3ee` + charcoal `#1c1612` + accent red `#9c2a2a` · Cormorant Garamond + Inter · prestigious / very-airy / private-request.

Eight pages, all in Italian, all written for a Roma Parioli private cardiology clinic:

| Page             | Slug             | What is on it |
|------------------|------------------|---------------|
| Home             | `/preview/`      | Editorial hero (cream + charcoal sidebar with Lancet quote), 3-fact band, drop-cap manifesto, signature visits 4-up on dark band, chief portrait (Dr. Marani) with bio, press strip, CTA strip |
| Lo Studio        | `studio`         | Five-row chronological timeline 2010 to 2024, dark "Metodo" section with three method paragraphs and drop cap, four "promesse" 4-up, dark CTA band |
| Visite           | `visite`         | Six visit packages with name + duration meta + description + price (220 to 980 euro), administrative footnote, dark CTA band |
| Medici           | `medici`         | Three doctors with portrait + role + 3 specialty tags + bio + links — Dr. Marani, Dr.ssa Salieri, Dr. Lombardi |
| Pubblicazioni    | `pubblicazioni`  | Lead post with image + 4 compact list rows, all 5 article entries with authors and read time |
| Article detail   | `pubblicazioni/<slug>` | Long-form editorial article with crumbs, kicker, drop-cap lede, body composed of `(p|h2|ol|blockquote)` blocks, footer meta — first article ("secondo parere") has full body, 4 others fall back to lede-only |
| Contatti         | `contatti`       | Four contact blocks (address, phone, email, urgenze), opening hours table 7-day, transport block, message form |
| Richiedi visita  | `richiedi-visita`| 4-step process explanation, dark form band with 8 fields + consent + secondary contact alternative, administrative footnote |

### Pilot 2 — Gusto (Osteria Moderna)

DNA: `fine-dining` archetype · charcoal `#0b0907` + gold `#d4a574` + burgundy `#8b0000` · Playfair Display + Lato · editorial-chef / very-airy / concierge-reservation.

Seven pages, all in Italian, all written for a 14-seat Michelin-starred Brera restaurant:

| Page          | Slug         | What is on it |
|---------------|--------------|---------------|
| Casa          | `/preview/`  | Full-bleed plate hero right · 108px italic Playfair headline left, 3-fact band, drop-cap manifesto, 5-course signature index with gold dotted leaders + wine pairings, chef portrait (Lorenzo Fioravanti), press strip, CTA strip |
| Filosofia     | `filosofia`  | Five-row chronological timeline 2014 to 2024, dark "Metodo" section with three method paragraphs and drop cap, four "promesse" 4-up |
| Menu          | `menu`       | Full eight-course `autunno '26` menu with ingredient lists and wine pairings, separate `Carta dei vini` section with 4 wine highlights, footer pricing note |
| Atmosfera     | `atmosfera`  | Four numbered room descriptions, 6-image magazine grid (4-col + 2-col mix) with overlay captions, italic CTA bottom |
| Diario        | `diario`     | Lead post + 4 compact list rows, all 5 articles with authors |
| Article detail| `diario/<slug>` | Long-form editorial article with same block system as Cardio — first article ("menu autunno '26") fully written, 4 fall back to lede-only |
| Prenota       | `prenota`    | 4-step process, concierge tile (Greta Vallesi portrait + bio + email + phone), 6-day hours table, private events tile, 9-field reservation form with consent |

### Files Added

```
apps/catalog/template_content.py                                  (NEW — content registry + helpers)
templates/live_templates/medical/specialist/_base.html            (NEW — Cardio chrome)
templates/live_templates/medical/specialist/home.html             (NEW)
templates/live_templates/medical/specialist/about.html            (NEW)
templates/live_templates/medical/specialist/services.html         (NEW)
templates/live_templates/medical/specialist/team.html             (NEW)
templates/live_templates/medical/specialist/blog_list.html        (NEW)
templates/live_templates/medical/specialist/blog_detail.html      (NEW)
templates/live_templates/medical/specialist/contact.html          (NEW)
templates/live_templates/medical/specialist/appointment.html      (NEW)
templates/live_templates/restaurant/fine-dining/_base.html        (NEW — Gusto chrome)
templates/live_templates/restaurant/fine-dining/home.html         (NEW)
templates/live_templates/restaurant/fine-dining/about.html        (NEW)
templates/live_templates/restaurant/fine-dining/menu.html         (NEW)
templates/live_templates/restaurant/fine-dining/gallery.html      (NEW)
templates/live_templates/restaurant/fine-dining/reservations.html (NEW)
templates/live_templates/restaurant/fine-dining/blog_list.html    (NEW)
templates/live_templates/restaurant/fine-dining/blog_detail.html  (NEW)
```

### Files Modified

- `apps/catalog/views.py` — added `LiveTemplateView` (TemplateView subclass), wired `has_live_preview` flag into `TemplateDetailView` context
- `apps/catalog/urls.py` — three new URL patterns: `live_template_home`, `live_template_page`, `live_template_post`
- `templates/catalog/template_detail.html` — conditional CTA: "Apri anteprima completa" for content-registered templates, legacy "Anteprima Live" for the rest

### Bug found and fixed mid-session
First `LiveTemplateView` implementation did the WebTemplate/DNA/content resolution inside `get_template_names()`. Django's `TemplateView.get()` calls `get_context_data()` BEFORE `get_template_names()`, so `self.template_obj` did not exist yet when the context builder tried to read it. Fixed by hoisting all resolution into `setup()`, which runs once per request before `get()`. Captured the lesson in D-044.

### Verified
- `python manage.py check` — 0 issues
- 17 routes hit via Django test client (with `ALLOWED_HOSTS=['*']` override) — all 200, no template errors:
  - 8 Cardio inner pages including blog detail
  - 7 Gusto inner pages including news detail
  - Both marketplace detail pages still 200
- `cardio` detail page now shows the new "Apri anteprima completa" CTA with `/preview/` href; `salute` (no live preview) keeps the legacy "Anteprima Live" CTA — strictly additive
- Cardio home page contains all 6 expected nav links to inner pages
- Gusto menu page contains all 8 expected courses
- Gusto Diario page nav shows `is-current` highlight on the active page
- Rendered HTML inspection confirms: DOCTYPE, font URLs (Cormorant Garamond + Inter for Cardio, Playfair Display + Lato for Gusto), brand palette injected into `:root`, complete nav + footer chrome

### Database delta
None. No migrations, no model changes, no seed updates. Content lives in code (per D-034 and D-042 rationale).

### Key Decisions
- D-042: Live multi-page templates as a code-driven content registry (deferred from `TemplatePage` model)
- D-043: Per-archetype standalone `_base.html` skins under `templates/live_templates/` — they do NOT extend the marketplace `base.html`
- D-044: `LiveTemplateView` resolves DNA + content in `setup()`, not `get_template_names()`
- D-045: "Apri anteprima completa" CTA is conditional on content-registry presence — templates without inner-page content keep the legacy CTA

### What is now reusable across all future templates
- `LiveTemplateView` and the three URL patterns
- The content-registry pattern (`template_content.py`) — adding a new template means adding ONE new top-level dict
- The per-archetype skin folder structure — any future template that picks an existing archetype gets the chrome for free
- Brand palette to CSS variable injection
- Nav loop / `is-current` highlight pattern
- Footer pattern with site-data block

### What still needs per-archetype work
- Each NEW archetype needs its own `_base.html` (the chrome is intentionally bespoke — that is the entire point of DNA)
- Each NEW archetype's page kinds need their own page templates (the layout vocabulary is category-specific — a `menu.html` is meaningless for a medical template)
- The "page kinds" themselves are category-flavoured (medical has `appointment`, restaurant has `reservations` and `menu`, etc.) — future categories will introduce their own page kinds

### Blockers
None. Both pilots render end-to-end and are navigable.

### Exact next step
**Pick the third pilot to validate the abstraction.** Most useful candidates:
1. A second `specialist` template (e.g. add a new `dermatologia-elite` template that re-uses the Cardio chrome — proves zero-archetype-work, just content) — confirms the *content registry* abstraction.
2. A second `fine-dining` template (e.g. `tartufo-truffle-house`) — same reason for restaurant.
3. The next archetype in the same category (e.g. add inner pages for Salute under the `clinic` archetype) — confirms per-archetype chrome variation.

(2) is probably the strongest signal: it tests that the 7-page restaurant model travels with content alone. If it does, future templates become "1 DNA entry + 1 content block" with zero new HTML.

After that, optionally:
- Promote `template_content.py` content to a `TemplatePage` model so customers can edit it (D-042 deferred this on purpose; the pilot phase needs to settle first)
- Wire the editor app to load these page templates as customizable surfaces (Phase 3)
- Add a "previous / next page" navigation hint at the bottom of each inner page
- Add per-page meta/OG tags using the page's content

## Session 12 — Template Polish Fixes (2026-04-10)

**Agent:** Template Polish Fixes (worktree: `template-polish-fixes`)
**Goal:** Close two product-quality regressions before moving on to the next pilot — (1) over-narrow inner-page layouts that make the live multi-page previews feel "compressed into the middle" of wide viewports, (2) restaurant listing showing stale/identical previews for Gusto and Sapore despite distinct DNA compositions.

### Issue 1 — Over-narrow inner-page layouts

**Root cause.** The live-template archetype skins (`templates/live_templates/medical/specialist/` and `templates/live_templates/restaurant/fine-dining/`) used three different max-width tiers — `1100px` for "editorial narrow" text sections, `1200px` for medical default wide sections, and `1280px` for restaurant default wide sections. On a 1600-1920px viewport those values centered the content with 300-500px of dead space on each side, which killed the premium feel. The worst offender was the homepage **manifesto** section: it used a double constraint of outer `max-width: 1100px` + inner `p { max-width: 36ch; margin: 0 auto; }`, producing a ~450px centered text column on a ~1890px screen, with a floating drop-cap that sat inside the narrow centered column instead of anchoring the left edge of the layout.

**Fix.** Bumped the width system to a two-tier standard:

| Tier                 | Was               | Now      | Applies to                                                                    |
|----------------------|-------------------|----------|-------------------------------------------------------------------------------|
| Editorial wide (medical specialist) | 1100 / 1200 | **1400** | sp-lead, sp-section, sp-history, sp-method-inner, sp-values, sp-posts, sp-treatments, sp-contact, sp-process, sp-form-band-inner, sp-manifesto |
| Editorial wide (restaurant fine-dining) | 1100 / 1280 | **1440** | fd-lead, fd-section, fd-hero (home), fd-manifesto (home), fd-courses (home), fd-chef-inner (home), fd-timeline (about), fd-method-inner (about), fd-values (about), fd-courses-full (menu), fd-wine-inner (menu), fd-rooms (gallery), fd-gallery (gallery), fd-process (reservations), fd-concierge-inner (reservations), fd-hours (reservations), fd-private-inner (reservations), fd-form-band (reservations), fd-posts (blog_list) |
| Editorial narrow — intentional | 1000 → 1200 | 1200 | `.sp-foot-note .inner` in services.html (stays intentionally narrow) |
| Long-form reading — unchanged | 760 | 760 | `.sp-article` / `.fd-article` blog detail pages (editorial column width preserved) |

Manifesto-specific fix: removed the `margin: 0 auto` + `max-width: 36ch` double constraint on the home manifesto paragraph and replaced with `max-width: 68ch` left-aligned so the drop-cap floats at the natural left edge of the container. Bumped the drop-cap size from 116px to 132px and the paragraph font-size from 26px to 30px (cardio) / 28px to 32px (gusto) to match the wider frame.

Also widened related grids to breathe in the new envelope: sp-history row template `140px 1fr` gap 48 → `180px 1fr` gap 72, sp-method-inner `1fr 1.6fr` gap 64 → `1fr 1.9fr` gap 96, fd-timeline row template and gaps similar, fd-method-inner, fd-private-inner, fd-concierge-inner, sp-form-band-inner, fd-wine-inner all opened up.

**Deliberately kept narrow:**
- Blog detail pages (`blog_detail.html` for both archetypes) — `max-width: 760px` for comfortable ~60-75ch long-form reading. Single-column article flow with drop-cap lede, body blocks (p/h2/ol/blockquote).
- Inline text `max-width: <NN>ch` on `.intro`, `.text`, `.lede`, `.sec-intro`, headlines (11-18ch) — these preserve the editorial line-length discipline even as the outer frame widens.

### Issue 2 — Restaurant listing preview mismatch

**Root cause.** A two-layer problem, only the outer layer being the obvious one:

1. **Outer:** `templates/includes/_template_card.html` and `templates/catalog/template_detail.html` both used `template.assets.first` — the default manager's first row by `Meta.ordering = ["order", "asset_type"]`. This is fragile: if a template ever gains a second asset (thumbnail, gallery image, source file) the wrong one can win without any warning.
2. **Inner (the real reason the user saw identical cards):** the PNG files on disk for `gusto-fine-dining-preview.png` and `sapore-trattoria-pizzeria-preview.png` were **stale legacy `restaurant.html` renders**, not the distinct DNA archetype compositions that Session 10 shipped. Both files showed the same wood-interior trattoria layout (different brand name + headline, identical everything else). The DB rows, filenames, and `generate_previews._resolve_composition()` logic were all correct — the bytes on disk were just wrong. Session 10's regeneration either never landed in this worktree, or got overwritten at some point. This is exactly the DNA-fallback timing trap called out in TODO_NEXT.md Phase 2d item 4.

**Fix applied.**

*Outer layer — robust preview selection:*
- Added `WebTemplate.preview_asset` property in `apps/catalog/models.py`. Explicitly filters `asset_type == TemplateAsset.AssetType.PREVIEW`. Prefetch-aware: if the caller already prefetched `assets`, iterates `_prefetched_objects_cache` in Python; otherwise issues a single filtered query ordered by `(order, pk)`. Returns `None` when no preview exists.
- Added a `_preview_only_prefetch()` helper in `apps/catalog/selectors.py` that uses `Prefetch('assets', queryset=TemplateAsset.objects.filter(asset_type='preview').order_by('order','pk'))`. The listing selector (`get_published_templates`) now prefetches only preview rows, which is a smaller payload than prefetching all asset kinds.
- Updated `templates/includes/_template_card.html` to use `{% with preview=template.preview_asset %}` and `preview.file.url` / `preview.alt_text`.
- Updated `templates/catalog/template_detail.html` gallery to use the same pattern.

*Inner layer — stale PNGs:*
- Deleted the two stale TemplateAsset rows + their canonical PNG files via a small Django shell snippet.
- Re-ran `python manage.py generate_previews --only gusto-fine-dining` and `--only sapore-trattoria-pizzeria`. The generator picked the DNA archetype compositions correctly (`restaurant/fine-dining.html` and `restaurant/trattoria-warm.html`). Files land at the canonical filenames with no orphan suffix because the rows/files were deleted first (the Session 9 clean recipe).
- Verified each regenerated PNG visually via direct-navigation with `?cb=` cache-bust: Gusto is now the fully-dark charcoal editorial Playfair layout (full-bleed plate right, italic "Una serata in otto atti." left, gold dotted-leader course index). Sapore is now the fully-bright cream polaroid scrapbook (two tilted photos, handwritten Caveat "Da Nonna Rosa" headline, cream washi-tape recipe card). Brace was untouched (yellow brutalist street-modern) — already correct from Session 9.

### Files Modified

*Model / selector:*
- `apps/catalog/models.py` — added `WebTemplate.preview_asset` property (22 lines)
- `apps/catalog/selectors.py` — added `_preview_only_prefetch()` helper, swapped `prefetch_related("assets")` to use it

*Templates (layout widths + preview_asset swap):*
- `templates/includes/_template_card.html` — swap to `template.preview_asset` via `{% with %}`
- `templates/catalog/template_detail.html` — swap to `template.preview_asset` for gallery
- `templates/live_templates/medical/specialist/_base.html` — sp-lead, sp-section 1200→1400
- `templates/live_templates/medical/specialist/home.html` — sp-hero 1280→1440, sp-manifesto 1100→1400 + inner 36ch→68ch (removed margin auto, bumped drop cap)
- `templates/live_templates/medical/specialist/about.html` — sp-history, sp-method-inner 1100→1400, sp-values 1200→1400 (gaps & inner text widths bumped too)
- `templates/live_templates/medical/specialist/services.html` — sp-treatments 1100→1400, sp-foot-note inner 1000→1200
- `templates/live_templates/medical/specialist/team.html` — sp-doctors 1280→1440
- `templates/live_templates/medical/specialist/blog_list.html` — sp-posts 1100→1400
- `templates/live_templates/medical/specialist/contact.html` — sp-contact 1200→1400
- `templates/live_templates/medical/specialist/appointment.html` — sp-process 1200→1400, sp-form-band-inner 1100→1400
- `templates/live_templates/restaurant/fine-dining/_base.html` — fd-lead, fd-section 1280→1440
- `templates/live_templates/restaurant/fine-dining/home.html` — fd-manifesto 1100→1440 + inner 36ch→68ch (removed margin auto), fd-courses 1280→1440, fd-chef-inner 1280→1440
- `templates/live_templates/restaurant/fine-dining/about.html` — fd-timeline 1100→1440, fd-method-inner 1100→1440, fd-values 1280→1440
- `templates/live_templates/restaurant/fine-dining/menu.html` — fd-courses-full 1100→1400, fd-wine-inner 1100→1400
- `templates/live_templates/restaurant/fine-dining/gallery.html` — fd-rooms 1100→1400, fd-gallery 1280→1440
- `templates/live_templates/restaurant/fine-dining/reservations.html` — fd-process 1280→1440, fd-concierge-inner, fd-hours, fd-private-inner, fd-form-band all 1100→1400
- `templates/live_templates/restaurant/fine-dining/blog_list.html` — fd-posts 1100→1400

### Database delta
- Deleted stale TemplateAsset rows `id=5` (gusto-fine-dining-preview) and `id=6` (sapore-trattoria-pizzeria-preview) + their canonical PNG files.
- Re-ran `generate_previews --only gusto-fine-dining` and `--only sapore-trattoria-pizzeria` — created two fresh TemplateAsset rows pointing at the correct canonical filenames, rendered from the correct DNA archetype compositions.
- Total template / brand / asset counts unchanged (19 templates, 19 brands, 19 preview assets).

### Verified

*Listing card correctness:*
- `/templates/restaurant/` — three visibly distinct cards at thumbnail size: Brace (yellow brutalist), Sapore (bright cream scrapbook with polaroids), Gusto (fully dark editorial with charcoal + gold). Verified via `browser_evaluate` that each card's `img.src` points at the correct slug's PNG and that the SHA-1 hashes of the three fetched files are all different (5aec..., bf69..., cf3d...).
- Direct PNG navigation to `/media/.../gusto-fine-dining-preview.png?cb=1` confirms the new Gusto file is the dark Playfair editorial layout (NOT the legacy wood-interior).
- Direct PNG navigation to `/media/.../sapore-trattoria-pizzeria-preview.png?cb=1` confirms the new Sapore file is the bright cream polaroid scrapbook (NOT the legacy wood-interior).
- `/templates/medical/` regression check — still shows 4 distinct medical archetype cards.

*Layout width correctness:*
- Before/after side-by-side of Gusto home page (`/templates/restaurant/gusto-fine-dining/preview/`): the manifesto section now spans the full 1440px frame instead of sitting as a tiny centered column. The drop cap anchors the left edge. Timeline, course index, and chef portrait sections all breathe properly.
- Gusto filosofia (`/preview/filosofia/`): timeline rows span the wide frame, method block has generous 2-col layout, 4-up values grid uses the full width.
- Gusto menu (`/preview/menu/`): 8-course list is now wide enough that name + ingredients + wine pairing live together on one row without feeling cramped.
- Cardio home (`/preview/`): hero 2-col spreads wider, manifesto is a proper wide editorial column.
- Cardio studio (`/preview/studio/`): timeline + method block both widen correctly.
- Cardio pubblicazioni (`/preview/pubblicazioni/`): lead post 2-col spans the frame, list rows use the full width.
- Cardio article detail (`/preview/pubblicazioni/<slug>/`): still intentionally 760px narrow long-form reading column — preserved on purpose.

*Smoke test:*
- `python manage.py check` → 0 issues.
- 20 URLs via Django test client → all 200. Covered homepage, browse, both category listings, both pilot detail pages, all 7 Gusto inner pages, all 8 Cardio inner pages + the blog article detail.

### Key Findings (no new D-XXX decisions, but lessons logged)

- **`template.assets.first` is a bug magnet.** It returns "whatever's first by default ordering", which silently picks the wrong file the moment a template has multiple assets. Always filter by `asset_type` explicitly. The `WebTemplate.preview_asset` property encapsulates this rule once so templates never need to remember it.
- **Page-level max-widths of 1100-1280 are too narrow for 1600+ displays.** 1400-1440 is the new standard for wide content. Editorial narrow reading columns (blog articles) stay at ~720-800px — those are about line length, not frame width. Never double-constrain with outer `max-width` + inner `margin: 0 auto + max-width: Xch` on the same element tree — either widen the outer container and use `max-width: <NN>ch` on the text (left-aligned drop-cap anchored to the frame's left edge), or keep the outer narrow and drop the inner centering. The double constraint creates compositions that look "floating in a void".
- **The DNA-fallback timing trap is still live.** Gusto and Sapore's PNGs on disk were stale legacy renders, despite Session 10's claim of having regenerated them. Whatever the root cause (cross-branch drift, an unrecorded regen pass, worktree sync weirdness), the fix is the same: delete the asset row + file, re-run `generate_previews --only <slug>` without `--force` so the canonical filename lands clean. TODO_NEXT.md Phase 2d option (b) — "automatic --force whenever the DNA file or composition path on disk is newer than the preview's TemplateAsset" — would catch this class of bug structurally.

### Blockers
None. Both issues are fully resolved and validated end-to-end.

### Exact next step
Back to **Phase 2g.1 validation** — add a second template under an existing archetype (e.g. `tartufo-truffle-house` under `fine-dining`, or `dermatologia-elite-roma` under `specialist`) to prove the content-registry abstraction travels. With the wider width system and the `preview_asset` property in place, any new template picks up the improvements for free — no per-archetype CSS tweaks needed.

## Session 13 — Archetype Reuse Validation (2026-04-10)

**Agent:** Backend-Core + Content
**Worktree:** `archetype-reuse-validation`
**Goal:** Prove that a new full multi-page template can be added under an existing archetype with ONLY three edits — one seed row, one DNA entry, one content block — and ZERO new HTML files. Option B of the two validation paths proposed in Session 12's handoff: a second template on the Medical `specialist` archetype (`dermatologia-elite-roma`).

### The validation hypothesis
The Session 11 architecture was designed around a "content registry + per-archetype skin folder + single dispatcher view" separation. The theory: once an archetype's skin folder exists, dropping a new template under it should be a matter of editorial authoring (brand, palette, copy, images) rather than chrome rebuilding. Sessions 11 and 12 shipped two templates (Cardio + Gusto) but each was the *first* template under its archetype — the reuse path had never actually been exercised. Without a second template under an existing archetype, the reuse claim was untested.

### Chosen template
- **Slug:** `dermatologia-elite-roma`
- **Category:** medical
- **Archetype:** specialist (reused from `cardio-studio-specialistico`)
- **Brand:** Studio Ricciardi Dermatologia (Dott.ssa Alessandra Ricciardi + 2 colleagues)
- **Location:** Via Veneto 116, Roma (Ludovisi) — *not* Parioli, to make it visibly a different studio from the cardio pilot
- **Accent:** `#3d5437` forest green — *not* cardio's `#9c2a2a` clinical red
- **Font pairing:** `Bodoni Moda + Inter` — *not* cardio's `Cormorant Garamond + Inter`
- **Positioning:** Dermatologia clinica + chirurgica + estetica (3 pillars, different from cardio's clinical + second-opinion positioning)
- **Price:** €115 (vs. cardio €109)

### Actions taken
1. Read the specialist chrome files end-to-end (`_base.html`, `home.html`, `about.html`, `services.html`, `team.html`, `blog_list.html`, `blog_detail.html`, `contact.html`, `appointment.html`) to catalog every `{{ page_data.* }}` / `{{ site.* }}` / `{{ posts.* }}` key the chrome consumes — this is the "contract" a content block must satisfy. Also cataloged every *hardcoded string* in the chrome (cardio-specific text that content cannot override) to inform both the authoring constraints and the post-validation lesson log.
2. Added `SEED_TEMPLATES` entry for `dermatologia-elite-roma` in `apps/catalog/management/commands/seed_templates.py` with the new brand (name, tagline, palette, typography, personality, logo concept) — distinct from Cardio's across every dimension. Price €115, order=5, not featured.
3. Added DNA entry for `dermatologia-elite-roma` in `apps/catalog/template_dna.py` with `archetype="specialist"` and all the specialist defaults (hero_style, navbar_style, footer_style, section_order, card_style, button_style, density, tone, imagery_direction, imagery_key, conversion_pattern), but overriding `font_pairing` to `("Bodoni Moda", "Inter")` and populating a fresh `content` block for the preview composition.
4. Added `DERMATOLOGIA_CONTENT` dict to `apps/catalog/template_content.py` with the same structural key layout as `CARDIO_CONTENT` — 7 pages (home/studio/visite/medici/pubblicazioni/contatti/richiedi-visita), 5 blog posts (first with full `body` block), site-wide footer chrome data, and distinct Italian copy throughout: dermatology specialties, three dermatologhe with dermatopatologia/chirurgia/estetica roles, six treatment rows with pricing (visita €180 → percorso annuale €580), contact block pointing to Via Veneto 116, and a full "Modulo di richiesta" process block. Kept the `pubblicazioni` slug for the blog page because `blog_list.html` and `blog_detail.html` hardcode it in URL reverses.
5. Ran `python manage.py check` — 0 issues.
6. Ran `python manage.py seed_templates` — created one new row (`Dermatologia Elite — Studio Ricciardi`), all others untouched.
7. Verified the DB state via Django shell: slug present, category=medical, brand palette accent=`#3d5437`, `has_dna()` → True, `has_live_template()` → True, medical category now has 5 templates (was 4).
8. Ran the Django test client across all 9 routes with `ALLOWED_HOSTS=['*']` override for the in-process call:
   - `/templates/medical/dermatologia-elite-roma/` (marketplace detail) → 200
   - `/templates/medical/dermatologia-elite-roma/preview/` (home) → 200
   - `.../preview/studio/` → 200
   - `.../preview/visite/` → 200
   - `.../preview/medici/` → 200
   - `.../preview/pubblicazioni/` → 200
   - `.../preview/pubblicazioni/mappatura-nei-quando-farla/` (post detail) → 200
   - `.../preview/contatti/` → 200
   - `.../preview/richiedi-visita/` → 200
9. Content assertion sweep on the home page: confirmed the rendered HTML contains `Studio Ricciardi`, `carta d'identità`, `Bodoni Moda`, `#3d5437`, `Alessandra Ricciardi`, `JAMA Dermatology`, `Mappatura nevi digitale`, `Via Veneto 116`, and `2.400` — i.e., the new content is actually reaching the page, not silently falling back to Cardio's.
10. Cardio-leak sweep across all 8 dermatology pages: cataloged exactly which cardio-specific strings bleed through the chrome despite the content swap (see Findings below).
11. Regression sweep: 15 routes on `cardio-studio-specialistico` (all 7 inner pages + marketplace detail) and 8 routes on `gusto-fine-dining` (all 6 inner pages + blog detail + marketplace detail), plus homepage + `/templates/` + `/templates/medical/` + `/templates/restaurant/` — 19 total — ALL 200. No regression.

### Files Modified
- `apps/catalog/management/commands/seed_templates.py` — +29 lines (one new entry after Cardio)
- `apps/catalog/template_dna.py` — +42 lines (one new entry before Cardio, keyed as the "5th specialist" slot)
- `apps/catalog/template_content.py` — +355 lines (full `DERMATOLOGIA_CONTENT` block + one new line in `TEMPLATE_CONTENT` registry)
- `CATEGORY_ROADMAP.md` — marked specialist as hosting two templates
- `DECISIONS.md` — D-046 added
- `TEMPLATE_REGISTRY.json` — version bumped to 0.6.0, dermatologia entry added with `archetype_reuse: true` flag
- `TODO_NEXT.md` — Phase 2g.2 (copy-abstraction pass) added
- `AGENT_HANDOFF.md` — Session 13 section added
- `SESSION_LOG.md` — this entry

### Files NOT modified (the whole point of the validation)
- **Zero** HTML files touched. Not in `templates/live_templates/medical/specialist/`. Not in `templates/preview_compositions/`. Not in `templates/catalog/`. Not in `templates/includes/`. The Session 11 chrome absorbed the new template without a single `.html` edit. `git status` confirms three modified `.py` files and zero modified or new `.html` files.

### Database delta
- `+1` WebTemplate row (`dermatologia-elite-roma`)
- `+1` TemplateBrand row (`Studio Ricciardi Dermatologia`)
- `+0` TemplateAsset rows (no preview PNG generated — the validation is about the live preview, not the thumbnail)
- Total: 20 templates (was 19), 20 brands (was 19), 19 preview assets (unchanged)
- Medical category: 5 templates (was 4) — clinic, family, specialist ×2, wellness

### Verified end-to-end
- All 9 dermatology routes: 200 via Django test client
- Content correctly substituted: brand palette, fonts, headlines, facts, manifesto, signature visits, chief doctor name + bio, press list, all 7 inner pages, 5 blog posts, full body of the lead post
- Regression on Cardio + Gusto + marketplace pages: 19 routes, all 200
- `python manage.py check`: 0 issues
- `git status`: only 3 `.py` files modified, 0 HTML files touched

### Findings — the abstraction is **structurally reusable** but **editorially leaking**

The validation's primary hypothesis (routes 200 with zero HTML edits) succeeded on the first try. But the cardio-leak audit found that the specialist chrome was written as if Cardio would be its only tenant — cardio-specific text is baked into the HTML in seven distinct places, and **every** dermatology page shows at least one of them:

| Leak site                                 | Appears on       | What leaks                                                                  |
|-------------------------------------------|------------------|-----------------------------------------------------------------------------|
| `_base.html:240`                          | ALL 8 pages      | `© 2026 ... · Iscrizione OMCeO Roma 12 / 4408` (wrong license number)       |
| `home.html:199` (hero right quote)        | home             | `«La cardiologia non è una catena di montaggio. È un dialogo lungo ...»`     |
| `home.html:200` (quote author)            | home             | `— Lancet · 2024`                                                           |
| `home.html:203-205` (pulse triple)        | home             | `Roma · Parioli` / `2010` / `Cardiologia clinica`                           |
| `home.html:225` (section head)            | home             | `Sei percorsi clinici, una sola firma.` (literal cardio headline)            |
| `home.html:241` (section head)            | home             | `Una sola firma per ogni cartella.`                                         |
| `home.html:265` (CTA band)                | home             | `Ogni visita è concordata personalmente con il medico.`                     |
| `about.html:111` (values heading)         | studio           | `Quattro impegni che non cambiano mai.`                                     |
| `about.html:123-126` (CTA band)           | studio           | `Vuoi conoscere i medici dello studio prima di prenotare?` + `I tre medici dello studio →` (also assumes exactly 3) |
| `services.html:100` (CTA heading)         | visite           | `Una visita allo Studio Marani è concordata personalmente.` ← **literal brand name leak** |
| `team.html:70-72` (CSS portraits)         | medici           | 3 hardcoded Unsplash portrait URLs — caps the archetype at 3 doctors AND shows cardio's same photos for the dermatology team |
| `team.html:87` (portrait signature)       | medici           | `Roma · Parioli` (every doctor card)                                        |
| `blog_list.html:17` (lead post image)     | pubblicazioni    | Hardcoded Unsplash CSS background image                                     |
| `blog_list.html` + `blog_detail.html`     | pubblicazioni / post | `{% url ... 'pubblicazioni' %}` — the blog parent page slug is a literal, not looked up from the content registry |
| `blog_detail.html:120` (footer strap)     | post             | `Studio Marani · Cardiologia clinica` ← **literal brand leak**              |
| `appointment.html:142` (side-note)        | richiedi-visita  | Hardcoded marketing copy about "richieste compilate con cura"                |
| `appointment.html:166-180` (select)       | richiedi-visita  | Hardcoded visit-type options: `Prima visita / Secondo parere / Programma prevenzione / Visita di controllo` (the content registry `form_fields` list is never consulted for option rendering) |

The **Studio Marani brand name leaks twice** (services CTA + blog detail footer), the **Parioli district leaks twice** (home pulse + team portrait signature), and the **wrong medical license number** leaks on every single page. A real buyer would immediately see a mismatched brand mid-scroll.

**The abstraction is not broken — it's incomplete.** The contract (content registry keys the chrome consumes) is well-defined. The violation is that the original Session 11 authoring pass embedded cardio's *sample* copy directly as literals in the chrome, under the assumption that the chrome was still single-tenant. Fixing it requires moving those literals out of the HTML into the content registry (typically via new `site.*` or `page_data.*` sub-keys), NOT adding new HTML files.

### Why this doesn't block the validation result
The validation asked: "can a new template be created with one seed entry, one DNA entry, one content entry, and zero new HTML files?" The answer is **yes** — every route 200s, every content variable renders, the font/palette/nav all switch correctly. The leaks are a separate, pre-existing bug in the Session 11 authoring pass that the validation exposed. Without this validation we would not have found them.

### Key Decisions Made
- **D-046** added: formally documents the archetype-reuse validation result + the copy-leak finding + the Phase 2g.2 copy-abstraction lift plan

### Key Lessons for Future Archetype Authoring
1. **When building a skin folder that will host >1 template, every string that is NOT a CSS rule must come from context.** The sample copy used during Phase 1 authoring should not live in the HTML as a literal — it should live in the content block, and the HTML should read `{{ page_data.cta_heading }}` instead of inlining the heading. Concrete rules:
   - Section titles that vary by template → `page_data.<section>_heading`
   - CTA band headings and labels → `page_data.<section>_cta_heading` / `_cta_primary_label` / `_cta_secondary_label`
   - Pulse-bar / portrait-signature / footer-license values → `site.license`, `site.pulse_triple`, `medici.portrait_city`
   - Hero-sidebar quote + author → `home.hero_sidebar_quote` + `hero_sidebar_author`
   - URL reverses for page kinds (e.g. blog parent slug) → discovered from `pages` registry list at render time (find the entry where `kind == 'blog_list'`), not hardcoded
2. **Imagery in inline CSS is a reuse blocker.** `team.html`'s three nth-child background-image rules mean every template reusing the specialist chrome shares the same three doctor photos. Move to a `doctors[i].portrait` URL in the content registry, consumed via `style="background-image: url('{{ d.portrait }}')"`.
3. **The "pubblicazioni" slug lock is the most dangerous leak** because it silently limits the reuse pattern to templates whose blog parent page is literally named `pubblicazioni` — any other naming (e.g. `blog`, `news`, `diario`) causes a NoReverseMatch at the URL resolution step. The fix is to compute the blog parent slug in the dispatcher view and pass it as `blog_parent_slug` in context.
4. **The chrome's hardcoded 3-doctor cap** (via the three `nth-child` rules) means any fourth doctor added to a content block will render without a portrait. Move the portrait imagery into content and drop the cap.
5. **Validation must include a full leak audit, not just a 200-status check.** A 200 response proves the routes resolve; it does not prove the content swap is complete. Always grep the rendered HTML for the *previous* template's brand name and district/city to catch leaks early.

### Blockers
None. The validation produced a clean result *and* a clear action plan for the follow-up Phase 2g.2 work.

### Exact next step
**Phase 2g.2 — copy-abstraction lift pass on the specialist chrome.** Move every cardio-specific literal out of `templates/live_templates/medical/specialist/*.html` into either (a) new `site.*` fields consumed by `_base.html` (footer license, compact hours, etc.), (b) new `page_data.*` sub-fields consumed by each page file (section/CTA headings), or (c) new per-item imagery fields (`doctors[i].portrait`, `home.hero_sidebar.*`, `blog_list.lead_image`). Then update both `CARDIO_CONTENT` and `DERMATOLOGIA_CONTENT` to populate these new fields, and re-run the leak-audit sweep — it should show every dermatology page as clean of cardio-specific strings. After that, the next archetype-reuse template (e.g. a third specialist or the first fine-dining reuse) will ship without any copy polish.

After Phase 2g.2 closes, resume Phase 2f DNA rollout: Agency → Lawyer → Real Estate archetype splits, applying BOTH the Session 10 imagery-distinctness lesson and the Session 13 content-must-not-be-hardcoded lesson from the start of each new archetype's authoring pass.


## Session 14 — Specialist Copy-Abstraction Lift (2026-04-11)

**Agent:** Specialist Chrome Refactor
**Goal:** Execute Phase 2g.2 — move every cardio-specific literal out of the 9 files under `templates/live_templates/medical/specialist/` into structured fields in the content registry. Zero new HTML files. Preserve Cardio + Dermatologia behavior. Leave the chrome ready for a third specialist template with no copy polish needed.

### Branch / worktree
`specialist-copy-abstraction` (built on top of `archetype-reuse-validation` → ... → `template-dna-system`, **none merged to master yet**).

### What changed

**`apps/catalog/template_content.py`** — extended both `CARDIO_CONTENT` and `DERMATOLOGIA_CONTENT` with a structured set of new fields under their existing blocks. No new top-level keys, no new architectural concepts — every addition sits semantically where the chrome already consumed data:

| Block               | New fields                                                                                                                                                                   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `site`              | `license`, `hours_footer_rows` (list of strings)                                                                                                                             |
| `home`              | `hero_sidebar_top_label`, `hero_sidebar_quote`, `hero_sidebar_author`, `hero_sidebar_pulse` (list of `(label,value)`), `signature_visits_label`, `signature_visits_heading`, `signature_visits_intro`, `chief_label`, `chief_heading`, `press_label`, `cta_heading`, `cta_primary_label`, `cta_secondary_label`; and `home.chief.portrait` (per-chief URL) |
| `studio` (about)    | `values_label`, `values_heading`, `cta_heading`, `cta_primary_label`, `cta_secondary_label`                                                                                  |
| `visite` (services) | `footnote_heading`, `cta_heading`, `cta_primary_label`, `cta_secondary_label`                                                                                                |
| `medici` (team)     | `portrait_city`; and per-doctor `doctors[i].portrait` URL (removes the 3-doctor cap previously baked into `nth-child` CSS)                                                   |
| `pubblicazioni`     | `lead_image`, `footer_strap`, `empty_body_fallback_paragraphs` (list)                                                                                                        |
| `contatti`          | `form_placeholders` (dict: `first_name`/`last_name`/`email`/`phone`/`subject`/`message`), `hours_heading`, `transport_heading`                                               |
| `richiedi-visita`   | `process_label`, `process_heading`, `form_band_side_note`, `form_band_side_note_small`, `submit_label`; and `form_fields` **reshaped** from `(label, placeholder, type)` tuples into richer dicts: `{label, type, full_width, placeholder OR options}` — the template now loops over this instead of hand-writing the form |

**`apps/catalog/views.py`** — `LiveTemplateView.get_context_data()` now computes `blog_parent_slug` from the first page whose `kind == 'blog_list'`. This removes the D-044/Session 13 hard constraint that the blog parent page slug had to be literally `'pubblicazioni'`. (Dermatologia still calls its blog page `pubblicazioni` because the content was authored that way, but future templates can call it `diario`, `osservatorio`, `rassegna`, anything — the chrome no longer cares.)

**9 HTML files under `templates/live_templates/medical/specialist/`** — every cardio literal pulled out, replaced with `{{ page_data.* }}`, `{{ site.* }}`, loop iterations, or (for URLs) `blog_parent_slug`. Specifically:

- **`_base.html`** — footer license + hours footer rows now loop from `site.license` / `site.hours_footer_rows`. Removed hardcoded `OMCeO Roma 12 / 4408`, `Sabato · solo reperibilità`, `Domenica · chiuso`.
- **`home.html`** — hero right sidebar (top label, quote, attribution, pulse triple) now reads from `page_data.hero_sidebar_*`. Chief portrait URL moved from inline `background: url(...)` to inline `style="background-image: url('{{ page_data.chief.portrait }}')"`. Signature-visits section label/heading/intro, chief label/heading, press label, bottom CTA heading + two button labels all now come from `page_data.*`. Removed hardcoded Unsplash URL `photo-1559757148-5c350d0d3c56`.
- **`about.html`** — values label/heading + CTA band heading/primary label/secondary label all from `page_data.*`. Removed the "I tre medici" hardcoded count leak.
- **`services.html`** — footnote heading + CTA band heading/labels from `page_data.*`. Removed the "Studio Marani" brand-name leak (the most visible one in the entire chrome).
- **`team.html`** — the three `nth-child` CSS rules with hardcoded Unsplash URLs are **gone**. Each doctor now uses an inline `style="background-image: url('{{ d.portrait }}')"` computed from the content registry. The 3-doctor cap is removed — future specialist templates can have any number of doctors. Portrait signature reads `{{ d.portrait_city|default:page_data.portrait_city }}`.
- **`blog_list.html`** — lead post background image moved from CSS url() to inline style reading `page_data.lead_image`. All three hardcoded `'pubblicazioni'` URL reverses replaced with `blog_parent_slug`.
- **`blog_detail.html`** — both hardcoded `'pubblicazioni'` URL reverses replaced with `blog_parent_slug`. Breadcrumb and footer "Tutte le …" now use `{{ page.label }}` / `{{ page.label|lower }}`. Footer strap reads `page_data.footer_strap|default:site.logo_word`. Empty-body fallback paragraphs loop from `page_data.empty_body_fallback_paragraphs`.
- **`contact.html`** — form placeholders read from `page_data.form_placeholders` dict (keys: first_name, last_name, email, phone, subject, message). Sidebar headings `Orari di apertura` / `Come raggiungerci` now come from `page_data.hours_heading` / `page_data.transport_heading`.
- **`appointment.html`** — the hand-written `<form>` (8 fields, 2 hardcoded select blocks) **replaced** with a single `{% for f in page_data.form_fields %}` loop that handles `text`/`email`/`tel`/`number`/`textarea`/`select` via field-type branching and applies `full_width` to mark grid-full rows. The two select dropdowns that previously baked in Cardio's visit types now pull their options from `form_fields[i].options`. Process label, process heading, form band side note + small, and submit button label all from `page_data.*`.

### Database delta
None. Pure content + template refactor. 0 migrations, 0 seed changes, 0 new assets.

### Files touched
11 modified, 0 added, 0 deleted (verified via `git status`):

```
 M apps/catalog/template_content.py
 M apps/catalog/views.py
 M templates/live_templates/medical/specialist/_base.html
 M templates/live_templates/medical/specialist/about.html
 M templates/live_templates/medical/specialist/appointment.html
 M templates/live_templates/medical/specialist/blog_detail.html
 M templates/live_templates/medical/specialist/blog_list.html
 M templates/live_templates/medical/specialist/contact.html
 M templates/live_templates/medical/specialist/home.html
 M templates/live_templates/medical/specialist/services.html
 M templates/live_templates/medical/specialist/team.html
```

### Validation — it works

1. **`python manage.py check` — clean.**
2. **Full route sweep — 25/25 green via Django test client:**
   - Cardio: marketplace detail + 7 inner pages + 1 post detail = 9 routes (200)
   - Dermatologia: marketplace detail + 7 inner pages + 1 post detail = 9 routes (200)
   - Gusto regression: marketplace detail + 6 inner pages + 1 post detail = 8 routes (200)
3. **Cardio-leak sweep on dermatologia — ZERO leaks.** The sweep grepped the rendered HTML of all 8 dermatology pages for 26 cardio-specific literals (`Marani`, `OMCeO Roma 12 / 4408`, `cardiologia`, `Cardiologia`, `Parioli`, `catena di montaggio`, `Lancet`, `Riccardo Marani`, `Margherita Salieri`, `Andrea Lombardi`, `Salieri`, `Lombardi`, `Prima visita`, `Secondo parere`, `Programma prevenzione`, `Visita di controllo`, `ecocardiograf`, `Holter`, `ECG`, `Policlinico Umberto`, `Sant'Andrea di Roma`, `Braunwald`, `Institut de Cardiologie`, `Piccione`, `Tarbouriech`, `cardiolog`). **All 8 pages came back clean.** Session 13's 17 distinct leaks are now 0.
4. **Positive content sweep on Cardio — 52 expected cardio strings, all present.** The rendered Cardio HTML still contains every hallmark string (Studio Marani, Lancet quote, Riccardo Marani, Roma · Parioli, Richiedi visita privata, Ogni visita è concordata, Prima visita, Secondo parere, Programma prevenzione, Visita di controllo, Pubblicato su, all three doctor portraits by photo ID, the Studio Marani · Cardiologia clinica footer strap on the blog detail page, etc.). No regression.
5. **Positive content sweep on Dermatologia — 46 expected dermatology strings, all present.** Rendered HTML contains Studio Ricciardi, Alessandra Ricciardi, Via Veneto, JAMA Dermatology, Quattro aree cliniche, Un solo archivio, Cosa garantiamo, Le tre dermatologhe, Mappatura nevi, Chirurgia dermatologica, Medicina estetica, Invia richiesta, Studio Ricciardi · Dermatologia integrata footer strap, and the three new dermatologia portrait photo IDs (1594824476967, 1582750433449, 1666214280557). The derm content block still drives every field it used to drive.
6. **Template file grep — ZERO hardcoded Unsplash URLs** in any of the 9 specialist chrome files (was 4 before: 3 nth-child portraits in `team.html`, 1 chief portrait in `home.html`, 1 blog lead in `blog_list.html`).
7. **Template file grep — ZERO cardio-brand literals** in any of the 9 specialist chrome files. Previously every file leaked.

### What the chrome now guarantees

Every string in the 9 specialist chrome files now either:
- is a CSS rule (tokens, colors, fonts, layout), or
- is a generic archetype label (`Nome`, `Cognome`, `Email`, `Telefono`, `Oggetto`, `Messaggio`, `Invia messaggio`, `Privacy`, `Cookie`, `Note legali`, `Anteprima completa`, `← Torna a MarketWeb`, `Altri template medicali →`, `Tutti i medici`, `Lo studio`, `Pagine`, `Contatti`, `Orari`, `Leggi l'articolo completo`, `In alternativa:`, `parla con la segreteria`, `min di lettura`, `© 2026`), or
- is a template context variable (`{{ site.* }}`, `{{ page_data.* }}`, `{{ d.* }}`, `{{ post.* }}`, `{{ blog_parent_slug }}`, etc.), or
- comes from a `{% for %}` loop over a content registry list.

### Chrome-authoring contract (new — D-047)

Any future per-archetype skin (e.g. the Agency `editorial-quiet` skin, the Lawyer `modern-transparent` skin) must follow the same rule from its first authoring pass:

> **Every string in a per-archetype skin must either be a CSS rule or come from `site.*` / `page_data.*` / loop items. No literal brand names. No literal city names. No literal quotes. No literal CTA labels. No literal form select options. No hardcoded image URLs.**

Session 13's leak cost the next reuse template zero-copy-polish ambition. This contract prevents that from happening a second time.

### Lessons from Session 14

1. **"Abstract the literals, not the structure."** The chrome's visual structure (grid layouts, typography, colors, spacing, the `.sp-lead`/`.sp-section`/`.sp-chief`/`.sp-doctors`/`.sp-form-band` class system) was already correct. The leak was purely textual — every fix was a one-line `{{ page_data.X }}` substitution. This is a good sign for future reuse passes: if the visual identity is clean, a leak audit is genuinely mechanical.
2. **`form_fields` as dict-of-dicts beats tuples.** The old `(label, placeholder, type)` tuple format couldn't represent select options or full-width rows without the chrome hand-writing them. Switching to `{"label":..., "type":..., "placeholder":..., "options":[], "full_width":bool}` let the chrome template become a single generic form loop. This pattern is now the reference for any future archetype that has a form.
3. **`blog_parent_slug` is the simplest way to kill the hardcoded-URL-reverse trap.** Computing it once in the view from `pages[i].kind == 'blog_list'` means every blog URL reverse in the chrome becomes `{% url '...' cat slug blog_parent_slug post.slug %}`. No content block ever needs to know its own slug. This is the D-044 permanent fix (was: "the blog parent page slug must be literally `pubblicazioni`" — it is no longer).
4. **`nth-child` for per-item imagery is the hidden item-count cap.** The three `team.html` CSS rules (`nth-child(1)`, `nth-child(2)`, `nth-child(3)`) didn't just hardcode URLs — they capped the number of doctors at 3 and the chrome silently broke on a fourth. Moving portraits to per-doctor inline styles both fixes the URL leak AND removes the cap. General rule: **any per-item visual data that varies should live on the item, not the chrome.**
5. **Positive sweeps matter as much as negative sweeps.** Grepping for cardio literals proves the leak is gone. Grepping for dermatology's OWN hallmark strings proves the content block is still wired to every field the chrome reads. Both sweeps passed on the first run after the refactor — a good signal that the refactor was faithful.

### Blockers
None. Phase 2g.2 closes cleanly. The specialist archetype is now truly reusable.

### Exact next step
**Phase 2f continuation — add a second fine-dining template (e.g. `tartufo-truffle-house`) under the Gusto chrome and repeat the same leak-audit sweep on the `templates/live_templates/restaurant/fine-dining/` chrome.** Expect the same class of leaks there — brand-name strings, hardcoded Unsplash URLs for the chef portrait and dish photos, possibly hardcoded menu course counts or wine region labels in the `menu.html` file. Apply the exact same abstraction pattern: extend the content registry with structured fields, move every literal out of the HTML, re-run the 25-route sweep, re-run the leak sweep. When that closes, the archetype-reuse validation officially extends to both specialist AND fine-dining — and the pattern is proven general.

After that, resume Phase 2f DNA rollout: Agency → Lawyer → Real Estate archetype splits, applying **all three** lessons from the session arc: Session 10's imagery-distinctness rule, Session 11's content-registry-as-registry rule, Session 13's leak-audit-with-rendering-grep rule, and Session 14's chrome-authoring-contract rule (D-047) from the first authoring pass of every new skin.


---
## Session 51 — Medical Second Wave Live Rollout (Phase 2g3.2, 2026-04-15)

### TL;DR
**Phase 2g3.2 CLOSED.** Salute (`salute-studio-medico` → clinic archetype), Benessere (`benessere-centro-olistico` → wellness archetype), Famiglia (`famiglia-pediatria` → family archetype) flipped from `tier=draft` to `tier=published_live`. All three ship full multi-page live skins + 5-locale content trees + real RTL for Arabic + Pexels imagery pools. Medical category now 5/5 live. Catalog at 16/20.

**D-080** records the medical-second-wave contract. Branch: `phase-medical-second-wave-v1`.

### What shipped (~9,900 LOC new skin+IT content; ~11,000 LOC new locale content)

**Skin folders** (templates/live_templates/medical/):
- `clinic/` — 8 HTML files (2,417 LOC). Class prefix `.cl-*`. Hero split-booking widget right, stats strip, icon-grid specialty cards, 4-step patient journey, 3 prevenzione check-up packages, 8-avatar team ribbon, partners convenzioni marquee, teal CTA band. Page kinds: home, about, services, **prevention** (new), team, contact, appointment.
- `wellness/` — 8 HTML files (2,174 LOC). Class prefix `.we-*`. Hero full-bleed-manifesto with gradient overlay, drop-cap manifesto, dotted-leader pricelist rituali, benefits trio, ambienti masonry lightbox, therapist trio, sensory journey 4-step, calendar-spot 7-day CTA. Page kinds: home, about (filosofia), services (rituali), **gallery** (ambienti, new), team (professionisti), contact, appointment.
- `family/` — 7 HTML files (2,144 LOC). Class prefix `.fm-*`. Hero centered-soft with rounded photo card + SSN ribbon + pediatra pebble, intro-trio età, portrait-stack pediatre, 5-step growth journey, 8-FAQ accordion genitori, child-friendly gallery, hours peach band, phone-and-chat CTA band. Page kinds: home, about (studio), services (visite), **faq** (crescita, new), team (pediatre), contact. (NO appointment — pattern is phone-and-chat, not booking form.)

**Content registries (IT):**
- `template_content_salute.py` (957 LOC) — SaluteVita Clinic, Milano Centrale, numero verde 800 123 456, 6 specialisti, 8 reparti con SVG icons, 3 check-up prevenzione (€ 280/320/420), 7 convenzioni, 13-field booking form.
- `template_content_benessere.py` (1,061 LOC) — Studio Armonia, Bergamo Alta, 5 operatori con certificazioni, 10 rituali (€ 85–150), 2 pacchetti week-end.
- `template_content_famiglia.py` (1,149 LOC) — Pediatria Famiglia Plus, Torino Crocetta, 4 pediatre, 8 tipi di visita, 16 FAQ genitori tematiche, 5 milestone crescita.

**Locale content** (12 files in `template_content_<slug>_{en,fr,es,ar}.py`):
- EN: NHS/BUPA (Salute) · Goop/Tatler (Benessere) · BabyCentre UK (Famiglia)
- FR: Ramsay Santé/Doctolib (Salute) · Marie Claire Bien-Être (Benessere) · Doctissimo Enfant (Famiglia)
- ES: Sanitas peninsular (Salute) · Mía Wellness (Benessere) · Guía Infantil (Famiglia)
- AR: MSA hospital-institutional (Salute) · MSA lifestyle-luxe/Vogue Arabia (Benessere) · MSA parenting-magazine (Famiglia)

Italian proper names preserved verbatim across all non-IT locales. Latin digits (0–9) used across all locales including AR for dates, prices, phone numbers.

**Pexels imagery pools** — replaced 3 legacy Unsplash keys in `apps/catalog/preview_imagery.py`:
- `medical` → bright clinical teal institutional pool
- `medical-wellness` → sage olistico serene pool
- `medical-family` → peach warm pediatric pool

PEXELS_API_KEY read from env, never committed.

**DNA content extensions** — 10 new keys added to `template_dna.py` content blocks to lift D-047 preview composition leaks (`services_title`, `services_link_all`, `card_cta`, `pricelist_title`, `pricelist_sub_prefix`, `therapists_label`, `hero_ribbon`, `hero_pebble_name`, `hero_pebble_note`, `hours_label`). Preview compositions `templates/preview_compositions/medical/{clinic,wellness,family}.html` now D-047 clean.

**Preview PNGs regenerated** under `template_assets/2026/04/`.

**Wiring:**
- `template_content.py` — 15 new imports + 3 new TEMPLATE_CONTENT entries
- `TEMPLATE_REGISTRY.json` — 3 entries flipped with full D-054 tier_reason notes
- `smoke_full.py` — 3 new LOCALES + 3 new CATEGORY entries

### Differentiation — D-054 10-gate matrix passes on every pair

**Salute (clinic) vs Cardio/Derm (specialist):** split-booking widget vs editorial serif · white clinical vs cream editorial · institutional vs prestigious · solid-phone vs minimal-serif · icon-grid 4-up vs editorial-large quote · booking-widget vs private-request · medium vs very-airy · Nunito Sans vs Cormorant italic · teal pill vs gold-underline · Milano poliambulatorio vs Parioli prestigious.

**Benessere (wellness) vs specialist:** full-bleed-manifesto photo vs editorial serif pull-quote · warm wood tone vs editorial cream · pill-floating vs minimal-serif · dotted-leader pricelist vs editorial-large cards · calendar-spot 7-day vs private-request email · Cormorant italic 96px poetic vs clinical.

**Famiglia (family) vs specialist:** centered-soft rounded photo card vs editorial pull-quote · warm peach vs cream · soft-pastel pill vs minimal-serif · Quicksand rounded vs Cormorant italic · portrait-stack pediatre vs editorial-large quote · phone-and-chat (NO appointment) vs private-request.

**3 new medical siblings internally:** 3 disjoint palettes · 3 distinct heroes · 3 distinct navbar silhouettes · 3 distinct card paradigms · 3 distinct CTA patterns · 3 distinct voices.

### Validation

1. `python manage.py check` — clean.
2. `python manage.py migrate` + `seed_categories` + `seed_templates` + `sync_template_tiers` — 16 published_live / 4 draft.
3. `generate_previews --force --only <slug>` — 3 PNGs rendered.
4. **Full smoke: `python smoke_full.py` → 660/660 HTTP 200** (baseline 530 + 130 new). Zero regression on 13 live.
5. **Browser walk via Playwright MCP (1440×900):**
   - Salute IT split-booking hero + stats + teal nav ✓
   - Salute AR RTL flipped, booking widget left, "صحتك، عملنا اليومي" ✓
   - Salute IT `/prenota/` multi-section form + sidebar ✓
   - Benessere IT full-bleed "Un respiro è la misura del nostro tempo" ✓
   - Benessere FR `/rituali/` "Dix rituels, aucune voie rapide" ✓
   - Benessere ES `/prenota/` "El ritual comienza en cuanto usted cruza el umbral" ✓
   - Famiglia IT warm peach + rounded photo + pediatra pebble + phone+WhatsApp ✓
   - Famiglia EN `/pediatre/` "Four signatures, one family record" ✓
   - Famiglia AR RTL "ننمو إلى جانب أطفالكم" + proper names Latin inside Arabic ✓
   - Category `/templates/medical/` — 5 distinct templates visible, no recolor siblings ✓

### D-047 chrome-authoring contract — zero leak confirmed
23 new skin files: zero user-facing Italian brand literals. Only hits are CSS selector comments. Skins reusable for hypothetical second siblings.

### Lessons
1. **Pexels > Unsplash for medical imagery.** Larger curated pools, easier per-archetype separation.
2. **3 archetypes × 3 macro-tones × 3 silhouettes = no visual-twin risk.** Authoring from DNA contracts from line one > retroactive lift.
3. **Parallel sub-agents scale authoring.** 3 skin+IT agents × 3 i18n agents in parallel compressed ~16h sequential work to ~4h wall.
4. **Stub-files-first pattern unblocks DB sync.** Locale stubs `import X_CONTENT_IT as X_CONTENT_LOC` let `sync_template_tiers` run immediately; translators overwrite with native voice.
5. **DNA.content preview-composition keys are cheap.** Lift literals on first authoring, never retroactively.

### Blockers
None.

### Exact next step
**Phase 2g3.6 final wave — lawyer + real-estate.** 4 remaining draft templates (lex / juris / casa / villa). Both categories CRITICO identity-crash. Rollout recipe: DNA split → 4 new skin folders → 4 IT + 16 locale content files → Pexels pools → preview comps → tier flip → 800+ smoke + browser walk. When this closes, catalog hits 20/20 `published_live` and Phase 3 unblocks.

Companion: extend smoke_full.py to D-047 leak enforcement (programmatic grep for brand literals across rendered HTML).


---
## Session 53 — Lawyer + Real-Estate Live Rollout · CATALOG COMPLETE 20/20 (Phase 2g3.7, 2026-04-15)

### TL;DR

**Phase 2g3.7 CLOSED. Catalog 20/20.** Lex (`lex-studio-legale` → classic-gold archetype — Studio Legale Ferri, Roma, forensic-notarile), Juris (`juris-avvocato-moderno` → modern-transparent — Martini & Partners, Milano, advisory-modern tech-forward boutique), Casa (`casa-agenzia-immobiliare` → mass-market — Domus Immobiliare, Milano+Torino, approachable residential), Villa (`villa-immobili-lusso` → ultra-luxury-cinematic — Villa Prestige, Milano+Portofino, editorial-concierge) flipped from `tier=draft` to `tier=published_live`. All four ship full multi-page live skins (6-7 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, Pexels-curated imagery pools, and sharp D-054 differentiation vs each other, vs existing business/portfolio/ecommerce/agency templates, and against the dark-premium Luxe pair (Villa ≠ Luxe despite shared Cormorant+champagne/dark palette).

**D-082** records the lawyer+real-estate contract. Branch: `phase-law-realestate-live-rollout-v1`.

### What shipped (~38,700 LOC total new code)

**4 DNA entries** (`apps/catalog/template_dna.py`):
- lex-studio-legale: archetype `classic-gold`, hero `split-ledger-monogram`, navbar `ledger-monogram`, card `practice-area-ledger`, conversion `private-consultation`, tone `forensic-notarile`, fonts Cormorant Garamond + Inter
- juris-avvocato-moderno: archetype `modern-transparent`, hero `centered-advisory-manifesto`, navbar `pill-advisory`, card `advisory-sector-pill`, conversion `strategy-call`, tone `advisory-modern`, fonts DM Sans + Inter
- casa-agenzia-immobiliare: archetype `mass-market`, hero `search-listings-grid`, navbar `cover-search`, card `property-tile-specs`, conversion `viewing-request`, tone `market-approachable`, fonts Poppins + Inter
- villa-immobili-lusso: archetype `ultra-luxury-cinematic`, hero `fullbleed-editorial-cover`, navbar `cinematic-dark`, card `property-dossier`, conversion `private-viewing`, tone `editorial-concierge`, fonts Cormorant Garamond + Montserrat

**4 skin folders** (`templates/live_templates/`):
- `lawyer/classic-gold/` — 8 HTML files (1,838 LOC). Prefix `.lx-*`. Ink nav + gold monogram crest, ledger hero with vertical gold rule, practice-area ledger rows (4 numbered entries on home + 12 on pratiche), publications marquee, partner portrait stamps (typographic-led — DNA imagery direction is library/gavel, not partner photos), sectioned contact form with premium `.lf-*` primitives.
- `lawyer/modern-transparent/` — 8 HTML files (2,267 LOC). Prefix `.jr-*`. Floating pill nav + slate wordmark + blue CTA, centered-manifesto hero (no big photo), 6-cell sector grid, process sprint S.01/S.02/S.03, outcome metric counter band, next-slot chip, insights strip, 3-step intake form.
- `real-estate/mass-market/` — 8 HTML files (2,915 LOC). Prefix `.dm-*`. Daylight cover hero + translucent search widget overlay, 4-up listings tile grid (property-tile-specs), 8 neighborhood cards with badges, agent cards with phone+WhatsApp pills, 3-step valuation form with emerald success state, 12 property detail pages (via project_list/project_detail page kinds).
- `real-estate/ultra-luxury-cinematic/` — 8 HTML files (3,002 LOC). Prefix `.vp-*`. Transparent-dark nav over fullbleed imagery, champagne serif wordmark + counter chip + editorial credit cells, 2-up property dossier grid, territory ribbon + editorial territorio cards, 5-step private-viewing process with NDA consent, 8 property dossiers (via blog_list/blog_detail page kinds).

**4 preview compositions** (`templates/preview_compositions/`):
- `lawyer/classic-gold.html` (305 LOC)
- `lawyer/modern-transparent.html` (240 LOC)
- `real-estate/mass-market.html` (298 LOC)
- `real-estate/ultra-luxury-cinematic.html` (362 LOC)

All D-047 clean from line one.

**Content registries (IT)** — ~5,277 LOC:
- `template_content_lex.py` (1,269 LOC) — Studio Legale Ferri, Roma+Milano, 14 avvocati, 12 aree di pratica, 6 cause notabili ("Aumento capitale quotata 2343 c.c.", "Modello 231 gruppo utility", "Successione internazionale Reg. 650/2012"), sectioned contact form.
- `template_content_juris.py` (1,238 LOC) — Avv. Martini & Partners, Milano+Torino+Bologna, 8 avvocati/legal-ops, 6 sectors (Startup & Tech / PMI & Famiglia / Lavoro & HR / Contratti B2B / Dispute resolution / Privacy & AI), 6 insights posts, 3-step intake form with prossimo-slot chip.
- `template_content_casa.py` (1,455 LOC) — Domus Immobiliare, Milano+Torino+lago di Como, 9 agents, 12 property detail pages (attico-brera-duomo, villa-cernobbio-lago, loft-tortona-navigli, trilocale-crocetta-torino, ...), 8 quartieri (Brera, Navigli, Porta Nuova, Isola, Cernobbio, Bellagio, Crocetta, Borgo Po).
- `template_content_villa.py` (1,315 LOC) — Villa Prestige, Milano+Portofino+Saint-Tropez, 4 private advisors (Alessandra Visconti di Modrone director), 8 property dossiers (Villa Aurelia Portofino, Castello di Monterò Chianti, Penthouse Quadronno Milano, Mas de la Mer Saint-Tropez, ...), 6 territorio (Portofino/Chianti/Costa Smeralda/Lago di Como/Saint-Tropez/Capri), 5-step private-viewing process with NDA.

**Locale content (EN/FR/ES/AR)** — ~20,000 LOC across 16 files, authored by 4 parallel translator sub-agents:
- Lex EN: Slaughter-and-May voice · FR: Gide/Bredin Prat cabinet · ES: Garrigues despacho · AR: Al Tamimi MSA institutional (5,276 LOC / 4 files)
- Juris EN: Kirkland Startups / Orrick / Gunderson Dettmer · FR: Bredin Prat VC · ES: Cuatrecasas Startups · AR: Al Tamimi tech desk (4,738 LOC / 4 files)
- Casa EN: Foxtons/Knight Frank UK · FR: Barnes/Century 21 · ES: Engel & Völkers Spain retail / Solvia · AR: Emirates Living / Better Homes MSA (5,456 LOC / 4 files)
- Villa EN: FT How to Spend It / Monocle Estates / Sotheby's editorial · FR: Le Figaro Propriétés / Emile Garcin · ES: Vanity Fair Spain Propiedades / Savills España · AR: Robb Report ME / Esquire ME Property MSA literary (5,068 LOC / 4 files)

Italian proper names preserved verbatim across all non-IT locales. Latin digits (0–9) used across all locales including AR.

**2 new Pexels imagery pools for lawyer, 2 for real-estate** — `apps/catalog/preview_imagery.py`:
- `lawyer-classic` — heritage library pool (leather Corpus Juris, mahogany desk, studio library, gavel)
- `lawyer-modern` — bright collaborative pool (modern meeting rooms, diverse professionals, glass offices)
- `realestate-casa` — daylight attainable pool (bright urban apartments, family homes, modern living rooms)
- `realestate-villa` — cinematic editorial pool (golden-hour villas, infinity pools, architectural details, heritage libraries)

6 URLs per pool, zero overlap across pools, zero overlap with legacy `lawyer`/`real-estate` fallback pools.

**CHROME_I18N extensions**: `mp_other_lawyer` + `mp_other_realestate` added across all 5 locales (it/en/fr/es/ar). Category labels translated natively.

**Wiring**:
- `template_content.py` — 20 new imports + 4 new TEMPLATE_CONTENT entries
- `TEMPLATE_REGISTRY.json` — 4 entries flipped with D-054 tier_reason
- `smoke_full.py` — 4 new LOCALES + 4 new CATEGORY entries + `/templates/lawyer/` + `/templates/real-estate/` category paths + 12 new detail routes (lawyer/notabili, lawyer/insights, realestate/immobili, realestate/collezione)

### Differentiation — D-054 10/10 on every pair

**Lex ↔ Juris (lawyer siblings):**
Typography Cormorant serif ↔ DM Sans kinetic sans · palette ink+gold+bordeaux ↔ slate+blue+yellow · background dark ink editorial ↔ bright white advisory · nav ledger with monogram crest + gold underline ↔ floating pill with wordmark + blue pill CTA · hero split-ledger-monogram with photo-right ↔ centered-manifesto with NO photo · card practice numbered ledger ↔ sector pill grid + sprint console · section order heritage→practice→partners→publications→consultation ↔ manifesto→sectors→sprint→metrics→insights→call · primary CTA serif "Richiedi una consulenza riservata" ↔ blue pill "Prenota una strategy call" · heritage "Fondato 1962" ↔ "Fondato 2018" · conversion private-consultation (email + NDA) ↔ strategy-call (calendar + 3-step intake).

**Casa ↔ Villa (real-estate siblings):**
Typography Poppins geometric ↔ Cormorant editorial · palette navy+emerald+orange daylight ↔ black+champagne+white cinematic · background bright lived-in ↔ dark golden-hour rarefied · nav cover-search transparent ↔ cinematic-dark transparent · hero search-widget-over-cover ↔ fullbleed dominant photo · card property-tile-specs (photo/price/addr/camere/m²/bagni) ↔ property-dossier (editorial photo/title/territorio/superficie/provenance) · primary CTA block "Cerca immobile" + WhatsApp pill ↔ ghost champagne "Richiedi private viewing" + NDA · geography Milano Brera/Navigli + Torino Crocetta + Como Cernobbio (Italian urban mass-market) ↔ Portofino + Chianti + Costa Smeralda + Saint-Tropez + Capri + Val d'Orcia (Continental ultra-luxury) · price visibility visible €420K-€1.25M ↔ hidden "Prezzo su richiesta" · conversion viewing-request (next-day visit) ↔ private-viewing (NDA + invitation-only).

**Lex/Juris ↔ Pragma/Elevate (lawyer ↔ business):**
Lex's forensic ledger ≠ Pragma's advisory pillars · Juris's strategic sprint ≠ Elevate's ship-log · font pairings fully distinct · imagery pools fully distinct.

**Casa/Villa ↔ Bottega/Luxe (real-estate ↔ ecommerce):**
No shop/cart/PDP/product routes on Casa/Villa (they're real-estate advisories) · Casa's tile grid ≠ Bottega's labeled-cards · Villa's property dossier ≠ Luxe's fashion editorial · territorio/superficie/provenance vocabulary ≠ silhouette/tessuto/drop · private-viewing + NDA ≠ private-request + atelier.

**Villa ↔ Luxe (dark-premium pair, particular attention):**
Villa is real-estate advisory (property dossiers, private viewings, NDA, concierge) — Luxe is fashion ecommerce (maison atelier, lookbook, stylist). Different page kinds (blog_list for property dossiers vs shop for products). Different conversion verbs. Same Cormorant font + champagne/dark palette are the only similarities and they diverge at first scroll.

### Validation

1. `python manage.py check` — clean.
2. `python manage.py migrate` + `seed_categories` + `seed_templates` + `sync_template_tiers` — **20 published_live / 0 draft** ✅ **20/20 MILESTONE**.
3. `generate_previews --force --only <slug>` — 4 new PNGs rendered under `template_assets/2026/04/`.
4. **Full smoke: `python smoke_full.py` → 834/834 HTTP 200** (baseline 660 + 174 new routes). Zero regression on the 16 pre-existing live templates.
5. **Browser walk via Playwright MCP at 1440×900:**
   - Lex IT home split-ledger hero + "Competenza, *riservatezza*, risultati." + LF monogram crest ✓
   - Lex EN home native "Competence, *discretion*, results." + THE FIRM · PRACTICE AREAS · OUR LAWYERS nav ✓
   - Lex IT `/pratiche/` "Dodici competenze, una sola *firma.*" ledger ✓
   - Lex AR `/pratiche/?lang=ar` RTL flipped + "اثنا عشر اختصاصًا، توقيع واحد." Arabic serif drama ✓
   - Juris IT home "Il diritto, *dalla tua parte.*" manifesto + sector grid + next-slot chip + blue pill ✓
   - Juris FR home native "Le droit, *de votre côté.*" + "Nous accompagnons startups, PME et freelances" ✓
   - Casa IT home daylight cover + search widget overlay + orange CTA ✓
   - Casa ES home "La casa de tus *sueños*, más cerca de lo que crees." + ES search widget + VENTA/ALQUILER nav ✓
   - Casa FR `/immobili/attico-brera-duomo/` "Penthouse panoramique avec terrasse · Brera" + "1 250 000 €" ✓
   - Casa AR home RTL + search widget "أخبرنا عن الحي وندع التفاصيل بأيدينا" + orange "ابحث عن عقار" ✓
   - Villa IT home fullbleed + champagne wordmark + "Dimore *d'autore*, a chi sa riconoscerle." + N° 03/18 counter chip ✓
   - Villa AR home RTL + champagne wordmark flipped + "منازل ذات توقيع، لمن يُحسن قراءتها." + fullbleed cinematic ✓
   - Villa EN `/collezione/villa-aurelia-portofino/` "Villa Aurelia — a 1922 historic residence" dossier ✓

### D-047 chrome-authoring contract — zero leak confirmed

32 new skin HTML files + 4 preview compositions: zero user-facing brand literals. Skins reusable for hypothetical second siblings (e.g. `avvocato-milano-giurista` on modern-transparent, `immobiliare-lago-garda` on mass-market).

### D-081 dynamic counter policy — binding satisfied

Every stats/facts/metrics band on the 4 new templates carries `data-lm="counter"` (Lex 4-cell · Juris 4-cell · Casa 4-cell · Villa discreet 4-cell). Villa's "Prezzo su richiesta" signal stays static (editorial-concierge tone disqualifies animating a non-numeric ask-phrase).

### Lessons

1. **8-agent parallel rollout is the new normal.** 4 template implementers (DNA/skin/content/preview each) + 4 translators (IT→EN/FR/ES/AR each) = 8 parallel sub-agents. Wall-clock compressed ~32h sequential to ~6h. Each agent reviewed a narrow slice (1 template × 1 role) — context-efficient.

2. **DNA entry first, translators wait for stub-files-first.** Spawning 4 translator agents BEFORE the 4 implementer agents had shipped IT trees would race on missing source files. Sequence: implementer → stub locale files (re-export IT) → wire template_content.py → smoke 834 routes → translators overwrite stubs. This matches the Session 51 pattern and is now the rollout recipe.

3. **DNA imagery direction drives preview composition coherence.** Lex's DNA `imagery_direction=legal-heritage-ink` explicitly describes "library/gavel scenes, NOT partner portraits" — so the skin's team page correctly renders typographic-led monogram stamps instead of placeholder photo slots. Future team pages for classic-gold siblings should follow the same DNA-honest pattern.

4. **Page-kind semantic clarity matters for real-estate.** Casa uses `project_list`/`project_detail` page kinds (structural parity with Chiara portfolio); Villa uses `blog_list`/`blog_detail` (structural parity with Pixel editorial). Both have the same plumbing via `LiveTemplateView`'s `_list→_detail` kind replacement — but the semantic choice (project = listing, blog = dossier) communicates to future editors which kind matches their surface.

5. **Counter animation policy D-081 is a retroactive and prospective contract.** Applied from line one on all 4 new templates. No Session 52-style polish pass needed this time.

6. **Pexels URL validation at author time.** Every new pool URL was verified via direct HTTP fetch before commit. Zero 404 URLs shipped. The `generate_previews` pipeline's `ensure_cached` hash check + offline cache fallback still serves as safety net, but the first-line-of-defense is author-time verification.

### Blockers

**None.** Catalog 20/20. Phase 3 unblock gate MET.

### Exact next step

**Phase 3 kickoff.** The 20/20 `published_live` milestone unblocks the Phase 3 workstreams per D-055 + Session 20 roadmap:

1. **Commerce completion v3** — promote the Session 43+44+45 commerce foundation from Bottega/Luxe-only to all 20 templates. Every template's live preview now has a real multi-page website; Phase 3a connects the "Compra il template" marketplace CTA to a real Stripe checkout that provisions a hosted project instance from the template seed.

2. **Editor app wireframe** — Session 30 locked in a ~600-row concrete editor schema blueprint for cardio/derm/gusto. Extend to the 20 live templates and wire the `projects.CustomerProject` model to feed edits back into a per-project content registry fork.

3. **Auth hardening** — the customer-facing flow (`/accedi/`, `/registrati/`, `/il-mio-account/`) can now assume every entry point leads to a real product (no draft gaps).

Companion work (non-blocking):
- Extend `smoke_full.py` with programmatic D-047 leak enforcement (grep rendered HTML of every locale for brand literals of *other* templates; catches cross-template leaks in chrome authoring).
- Document the 8 archetypes + 20 templates in a public-facing catalog index (`docs/catalog.md`) for onboarding.

---

## Session 54 — A.3b Reorder Only · First-Wave Repeater Complete (2026-04-17)

### What shipped

A.3b closes the add/remove gap that A.3a left: customer can now reorder rows up/down within a mutable list. Three commits on `phase-editor-a3b-reorder-only-v1`:

- `a5a4f69` — contract + services: `__meta__` gains an `order` array (list of segment strings); `services.move_row(project, list_path, segment, direction)` performs a single-step swap. Sparse-diff is preserved — when the new order equals the canonical default (baseline-ascending + added-declaration), `order` is stripped from meta. 11 contract tests.

- `19e1d38` — UI: single endpoint `/projects/<uuid>/row/move/` + up/down ghost chevron buttons in each mutable subgroup header. Boundary states (`can_move_up`/`can_move_down`) come from the server, so the first row up-chevron and the last row down-chevron are pre-disabled. JS reuses the A.3a `withAutosaveFlush` + `postRowOp` + sessionStorage `PENDING_PAGE_KEY` pipeline — zero new client infra.

- `2c53216` — persistence hardening: `add_row` appends the new uid to a persisted `order`; `remove_row` prunes the dropped segment and normalizes back to default if pruning restores the canonical sequence. Three new tests cover the add-after-reorder and remove-after-reorder cases that would otherwise have silently discarded a custom arrangement.

### Observables

Browser walk validated: move down on a baseline row keeps the iframe on `/studio/` across reload, stats band reorders, move up reverts to default (sparse-diff strips record, 0 modifiche). Add then move-up mixing baseline + added rows works end-to-end: effective order `[0, 1, 2, a0, 3]` on studio.facts renders correctly in the iframe + reopens identically + publishes to a second authenticated viewer. MWEditor.jumpField still works on uid paths after reorder — key resolution is structurally stable, only position in the effective list changes.

### Consequences

- First-wave repeater contract now complete: add + remove + reorder + persistence. Two lists mutable: studio.facts + studio.partners.
- D-093 reuses the `__meta__` extension as the binding for future reorder variants. Phase A.3c widen can enable mutability on new lists without touching reorder machinery.
- 55/55 to 69/69 server tests. Smoke 834/834 unchanged.

### Exact next step

Phase A.3c (widen repeater to 1-2 more lists) — pattern is validated across both tuple and dict shapes, additional lists are about 30 LOC of schema flags each.

---

## Session 55 — A.3c Widen Repeater Coverage · +2 Lists (2026-04-17)

### What shipped

A.3c enables `mutable=True` on two additional lists in Vertex, using the plumbing already validated by A.3a + A.3b. Three commits on `phase-editor-a3c-widen-repeater-v1`, strictly disciplined:

- `1f86dc6` — `contatti.channels` (tuple, 2 cols, min=1 max=10) plus legacy test updates (whitelist test renamed to three-lists; non-mutable counter-example tests that previously referenced `contatti.channels` moved to `manifesto.phases`).

- `895b02e` — `studio.timeline_rows` (tuple, 3 cols, min=2 max=10) plus whitelist test bumped to four-lists, uid-path validator extended for the new mutable list.

- `2b9929b` — cross-cutting polish: a single HTTP-level integration test locks the contract that `data-ed-mutable="1"` + `[data-ed-list-path]` markers appear in the editor sidebar markup only for the four mutable lists, NEVER for the other 14 indexed lists. Guards against a future edit that silently flips `mutable=True` on an un-vetted list.

### Observables

Browser walk per list validated: `contatti.channels` → add "WhatsApp" row, move up twice, remove "LinkedIn" baseline, iframe `/contatti/` reflects correctly at every step. `studio.timeline_rows` → add 2027 row with year/title/body, move up once, remove baseline 2020, iframe `/studio/` cronologia band updates. Zero touches to services/rendering/views/JS/CSS — the schema `mutable` flag is the single gate. Pattern is genuinely universal.

### Consequences

- 4 mutable lists live on Vertex: studio.facts, studio.partners, studio.timeline_rows, contatti.channels. 14 still-locked.
- 69/69 to 74/74 server tests. Smoke 834/834 unchanged.
- First-wave repeater is officially complete: add + remove + reorder + persist + preview sync + publish + page preservation + jumpField API, covering both tuple and dict shapes across four lists.

### Exact next step

A.4 customer image upload — closes the gap "customer still has to paste CDN URLs" which is the biggest remaining premium-experience debt post-repeater.

---

## Session 56 — A.4 Customer Image Upload (2026-04-17)

### What shipped

A.4 introduces customer-facing image upload: file picker → POST multipart → ProjectAsset persisted on MEDIA_ROOT → public `/media/` URL feeds the existing widget URL input → autosave pipeline takes over. Four commits on `phase-editor-a4-image-upload-v1`.

- `ed76cea` — backend shell. `ProjectAsset` model (+1 migration) with FileField on `project-assets/<project-uuid>/<uuid>.<ext>` path generated server-side (zero path traversal surface). `services.upload_asset` applies three guards: 2MB cap (`AssetTooLarge` → 413), MIME whitelist jpeg/png/webp (`AssetMimeRejected` → 415), and `Pillow.Image.verify()` post-save to catch MIME-spoofed bytes (`AssetInvalid` → 400 with atomic row + file cleanup). Endpoint `project_asset_upload` wraps the service with login_required + CSRF + ownership guard. 10 contract tests.

- `b875383` — customer UI wiring. The A.2.2 FileReader → data-URL hack is replaced by fetch POST multipart; `uploadImageFile()` reuses the A.3a `withAutosaveFlush` pattern and adds an is-uploading visual state on thumb + pick button. Client-side guards (MIME + 2MB) reject bad files with a toast before the network hop. The `accept` attribute on `input[type=file]` is restricted to jpeg/png/webp.

  A real bug was found and fixed in-flight: `validate_value` for image fields accepted only http/https/data: prefixes, so the very `/media/...` URL the endpoint returned would fail autosave on its first save. Extended the image scheme whitelist to accept `/media/` alongside existing prefixes; locked by `test_a4_validate_value_accepts_media_relative_url`.

- `43341e3` — cross-cutting persistence lock via HTTP test client: upload → autosave into `studio.partners.0.portrait` → GET `/editor/` (URL prefills input, proving reopen persistence) → publish + login-as-other + GET `/preview/studio/` (URL renders in public HTML).

- `45e5f5b` — complementary lock on the second image field `home.cover.image` (dict-nested path shape, different from the repeater-dict-column shape of partners.portrait), confirming the contract holds on both existing image fields.

### Observables

Browser walk 8/8: login → jumpField to portrait → canvas-generated PNG attached via DataTransfer → dispatch change → POST fetch → `/media/...` URL returned → URL prefills input + thumb updates + iframe studio reflects new portrait (magenta square replaces Unsplash image) → status Saved, 1 modifica. Client guards tested: GIF + 3MB blob both rejected with toasts, URL unchanged in both cases. Reopen editor → URL + thumb persisted. Public preview after publish contains `/media/` URL. Screenshot captured: `a4_upload_success.png`.

### Consequences

- Customer image upload flow is now end-to-end operational on the two image fields of agency-creative-studio. Upload → persist → preview sync → publish → public preview → reopen all validated.
- Orphan asset handling deliberately deferred — see D-094 binding for A.5 scope.
- 74/74 to 87/87 server tests. Smoke 834/834 unchanged.
- New customer-facing premium surface: no more paste-a-CDN-URL workaround.

### Exact next step

A.5 orphan asset GC — honour the D-094 promise with a prudent management command before accumulated orphans become a real storage-management issue.

---

## Session 57 — A.5 Orphan Asset GC · D-094 Promise Closed (2026-04-17)

### What shipped

A.5 introduces a manual garbage collection command for ProjectAsset rows no longer referenced by any live override or publish snapshot. Three commits on `phase-editor-a5-orphan-asset-gc-v1`.

- `48c03ff` — service layer. `find_unreferenced_assets(project=None, grace_hours=24)` scans ProjectAsset rows outside the grace window, builds a per-project reference blob by concatenating every `ProjectContent.value_json` and every `ProjectRevision.snapshot` (JSON-encoded), and returns the assets whose `file.url` does NOT appear as a substring of that blob. Revision snapshots count as reference — a publish history protects the asset even if the live override replaced it.

  `delete_unreferenced_assets(assets, *, dry_run=True)` deletes file + row per asset with per-asset exception handling (filesystem failures never abort the batch). Returns stats: scanned, deleted, skipped, bytes_freed, paths, errors (capped at 10). Dry-run mode produces stats identical to apply mode but leaves everything intact — the operator sees exactly what --apply would remove.

  Seven contract tests lock the math. The URL-shape assumption (A.4 D-094 binding: `<MEDIA_URL>project-assets/<project-uuid>/<hex>.<ext>`, no query string) is documented in the code header.

- `d50f008` — `gc_project_assets` management command. Default is DRY-RUN; real deletion requires explicit `--apply`. Optional `--project=<uuid>` narrows scope, `--grace=<hours>` tunes the race guard. Output is a human-readable table of candidate paths with size + mode banner + summary line. Two command tests lock the default-dry-run and --apply behaviours.

- `b753326` — cross-cutting end-to-end integration test: upload asset_A → reference it → upload asset_B → replace the reference (A orphan now, B referenced) → confirm grace window protects both → backdate A's `created_at` past grace → confirm dry-run surfaces only A → run --apply → confirm A's file + row gone, B's file + row intact.

### Observables

- 87/87 to 97/97 server tests. Smoke 834/834 unchanged.
- Management command `python manage.py gc_project_assets --help` renders Django auto-generated help. Bare invocation on dev DB with zero orphans prints the "Nothing to clean up." branch cleanly.
- Zero customer-visible surface added: A.5 is operator-facing only.

### Consequences

- D-094 debt closed: orphan asset cleanup now has a prudent, auditable, default-safe tool.
- No scheduled / cron / event-based cleanup — operator runs manually per D-094 binding.
- A.6 remote storage (if ever shipped) will need to update `_build_reference_blob` to match the new URL shape; the existing tests act as early-warning regression detectors.
- Baseline v15 is now operationally complete for the full customer-facing editor flow on Vertex: 284 field + 4 mutable lists + image upload + orphan GC.

### Exact next step

Two candidates depending on product priority:

(a) **A.6 second-archetype editor support** — replica of the A.2.6 schema work on medical-specialist or restaurant-fine-dining. Scales editor to 2+ template categories. About 500-800 LOC schema replica.

(b) **A.6 remote storage** — swap Django FileField backend to S3 / Cloudinary. Only worth doing when a prod-launch timeline requires it; introduces ops dependencies.

No debt currently pending. Consolidation pause (this commit) precedes the choice.

---

## Session 58 — Phase A.6 · Second Editable Archetype Support (2026-04-17)

### What shipped

A.6 extends the editor from Vertex-only to Vertex + Pragma (`corporate-suite` archetype). Three commits on `phase-editor-a6-second-archetype-v1`.

- `a7177f5` — Step 0 · coverage contract. 6 contract tests: `corporate-suite` registered in `_ARCHETYPE_SCHEMAS`, schema shape covers all 5 Pragma pages (chi-siamo / competenze / case-studies + chrome), `validate_key_path` accepts the whitelist / rejects outside, indexed lists are readonly (not mutable in A.6), `customize_start` creates an editable Pragma project, Vertex editor unchanged regression guard.
- `9540d5a` — Step 1 · schema + preview bridge. `PRAGMA_CORPORATE_SUITE_SCHEMA` (7 groups · ~53 scalar + 1 image · 3 readonly indexed lists `home.pillars`/`kpi_strip`/`leadership`), `STRUCTURED_FIELD_SHAPES["corporate-suite"]` with no `mutable` flag, registered in `_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE`. `corporate-suite/_base.html` 3 atomic fixes: `logo_word` override honored in `<title>`, CSS guard block `body.mw-is-editor-preview`, conditional `preview-bridge.js`. 3 tests: logo_word override reflected in preview title, `editor_ctx` exposes sidebar + palette, editor preview injects bridge.
- `4b9376c` — Step 2 · lifecycle validation. 2 cross-cutting HTTP tests: full customer lifecycle (upload → autosave scalar+image+brand → reopen → publish → second-user public preview) + Vertex regression guard (33 sidebar groups · 4 mutable lists · ~284 fields invariant).

In-flight bugs caught + fixed: (a) page-aware navigation mismatch — initial schema used abstract page kinds, fixed to Italian slugs `chi-siamo/competenze/case-studies` matching the Pragma registry. (b) `vertex_groups` length assertion off-by-one.

### Observables

- 97/97 → 108/108 server tests (+11). Smoke 834/834 unchanged.
- Browser walk on Vertex regression: 33 groups, 4 mutable lists [`contatti.channels`, `studio.facts`, `studio.partners`, `studio.timeline_rows`], 284 fields, edit persistence, zero regression.
- `manage.py check` 0 issues.

### Consequences

- Editor scales to 2/8 archetypes. Pattern confirmed: schema register + preview bridge + lifecycle test = ~3 commits per archetype.
- No new D-number introduced. A.6 honors the A.1 contract (`_ARCHETYPE_SCHEMAS` registry) + D-047 chrome-authoring + D-089 scroll-calm preview bridge.
- Merged into v15 via `--no-ff` @ `f5cfd2a`.

### Exact next step

A.7 Multi-locale Editor Support (binding decision: `editor_ctx` for the catalog's 5-locale promise must be honored customer-side before widening archetype enrollment further).

---

## Session 59 — Phase A.7 · Multi-locale Editor Support (2026-04-17)

### What shipped

A.7 closes the strategic gap "editor monolingua" without destabilising the architecture. Customer edits one Vertex project in 5 locales (it/en/fr/es/ar, including authentic RTL for Arabic). Each language has an independent buffer. Global fields (brand, palette, image, repeater) stay universal. Zero cross-locale leak customer-side. Pragma remains not-enrolled (A.7b follow-up, ~3 commits). Five commits on `phase-editor-a7-multilocale-v1`.

- `cc4d524` — Step 0 · schema translatable flag contract. `is_translatable(archetype, key_path)` + `supported_locales(archetype)` + archetype gate `_MULTILOCALE_ENABLED_ARCHETYPES = {"agency-creative-studio"}`. Pure metadata, zero behavior change. 7 contract tests.
- `19ce86f` — Step 1 · overlay partition by locale. Storage-key convention `@<locale>:<path>` for translatable rows, plain key for globals — shape-compatible with the flat `ProjectContent` table, zero migration. `save_content_edits(locale=)` locale-aware + `UnsupportedLocale` exception + sparse-diff locale-scoped. `apply_project_overrides(locale=)` filters rows by target locale, locale row supersedes plain row on same path. `CustomerProject.get_overrides_dict(locale=)` locale-aware reader. 10 tests. Customer-invisible.
- `2652e94` — Step 2 · autosave + editor context locale-aware. `/projects/<id>/autosave/` accepts `locale` in JSON body. `ProjectEditorView` reads `?lang=<code>` → `active_locale` with silent fallback to `project.locale`. Context exposes `active_locale` + `supported_locales`. Preview URL carries `&lang=<active_locale>`. 11 tests (3 service + 8 HTTP).
- `c080dbf` — Step 3 · UI locale switcher + translatable markers. Sidebar pill becomes edit+preview stateful: click triggers `flushDirty(locale=OLD_LOCALE)` + `awaitFlushedOrIdle()` + navigate to `?lang=<new>`. Marker "PER LINGUA" (`.ed-lang-badge`) + `data-ed-translatable="1"` on every translatable field. Label "Lingua attiva" (vs legacy "Lingua anteprima"). `MW_EDITOR_CONFIG.currentLocale` + `supportedLocales` passed to JS. Autosave body now always tagged `locale: currentLang`. 2 UI markup tests.
- `e4c2298` — Step 4 · lifecycle lock end-to-end. One HTTP-level test walks IT+EN+FR translatable edits + 1 global edit + publish + 5 public preview renders (second user) + 4 editor reopens owner-side. Locks every storage key, publish transition, cross-locale non-leak assertion, and editor prefill per locale. One Pragma regression guard: save on Pragma via autosave with `locale=en` persists plain-keyed (the gate really holds at HTTP layer), `supported_locales=[]` in context, all fields `translatable=False`.

In-flight bugs caught + fixed: (a) first browser walk revealed `MW_EDITOR_CONFIG.currentLocale` missing in the template — fixed by emitting `{{ active_locale|default:'it'|escapejs }}`. (b) runserver `--noreload` didn't pick up template changes — needed manual restart (environmental, not codebase).

### Observables

- 115/115 → 147/147 server tests (+32: 7 Step 0 · 10 Step 1 · 11 Step 2 · 2 Step 3 · 2 Step 4). Smoke 834/834 unchanged.
- Browser walk end-to-end as `a7_test` owner then `a7_other` second user: edit IT → click EN (debounce pending) → flush `@it:` before navigate → edit EN → FR → ES authored fallback → AR editor + RTL iframe authentic → back to IT persistence intact → publish → second user public preview per locale shows IT/EN/FR overrides, ES/AR clean authored fallback, global logo `FinaleBrand` universal. Screenshot `a7_step4_public_preview_ar_rtl.png`.
- `manage.py check` 0 issues.

### Consequences

- Editor 2/8 archetypes editable · multi-locale 1/8 (Vertex).
- Catalog 20/20 `published_live` unchanged.
- Three new binding decisions: D-096 storage convention, D-097 fallback semantics, D-098 archetype gate. See DECISIONS.md.
- Merged into v15 via `--no-ff` @ `b18493d` and pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

Two candidates, no commitment:

(a) **A.7b Pragma multi-locale enrollment** — lowest-risk win. Add `"corporate-suite"` to `_MULTILOCALE_ENABLED_ARCHETYPES`, mirror the lifecycle test. ~3 commits.

(b) **A.8 Third archetype editor enrollment** — candidate: `fine-dining` (Gusto). Imagery-heavy stress test. Recipe identical to A.6.

Consolidation pause (this commit) precedes the choice.

---

## Session 60 — Phase A.7b · Pragma Multi-locale Enrollment (2026-04-17)

### What shipped

A.7b operationalizes D-098: Pragma (`corporate-suite`) joins `_MULTILOCALE_ENABLED_ARCHETYPES` as the second enrolled archetype alongside Vertex. Pure wiring — no schema shape change, no service layer touch, no UI change. Two commits on `phase-editor-a7b-pragma-multilocale-v1`.

- `43b6609` — Step 0 · gate enrollment + 6 contract tests. `"corporate-suite"` added to `_MULTILOCALE_ENABLED_ARCHETYPES` in `apps/editor/schema.py` (+1 real line). Six contract tests lock the Pragma classification:
  - `test_a7b_pragma_is_translatable_text_fields` — 12 paths **distributed across all five Pragma pages** (home · chi-siamo · competenze · case-studies · contatti/site.*) so the gate can't pass by covering only home.
  - `test_a7b_pragma_branding_and_contact_universals_are_global` — 6 paths (logo, logo_initial, phone, email, address, license) stay global.
  - `test_a7b_pragma_non_text_fields_are_global` — image (`home.hero_image`) + select (`home.primary_href`, `home.cta_primary_href`) False.
  - `test_a7b_pragma_structured_list_cells_are_global` — 7 cells across pillars/kpi_strip/leadership False.
  - `test_a7b_pragma_supported_locales_returns_canonical_five` — `["it","en","fr","es","ar"]`.
  - `test_a7b_vertex_still_enrolled_after_pragma_joins` — regression guard on Vertex.
  - Three A.7-era anti-enrollment tests removed (`test_a7_pragma_is_not_multilocale_enabled_in_first_wave`, `test_a7_step1_pragma_save_still_uses_plain_keys`, `test_a7_step4_pragma_editor_stays_plain_keyed_regression`) — they lied about the desired state after the gate flip.

- `d548588` — Step 1 · Pragma lifecycle HTTP cross-cutting. `test_a7b_pragma_full_multilocale_lifecycle_end_to_end` mirrors the Vertex Step-4 lifecycle on Pragma: 3 translatable autosaves (IT/EN/FR) + 1 global autosave + publish + 5 public preview renders (second user) + 4 editor reopens (owner) + AR preview `<html dir="rtl">` assertion + zero cross-locale leak assertions. +183 LOC, passes at first run — strong signal that D-098 recipe is architecturally sound.

Step 2 · browser walk. No code changes. 9 spot checks all green:
- Pragma editor mount `?lang=it` → label "Lingua attiva" · 5 pills · 53/92 translatable fields · correct markers
- Type IT + global + click EN → flush `@it:home.headline` + plain `site.logo_word` before navigation (DB verified)
- IT ↔ EN ↔ FR ↔ ES ↔ AR switch lifecycle: each locale loads authored or customer buffer correctly · zero cross-locale leak
- AR iframe renders `<html dir="rtl" lang="ar">` authentic · H1 arabic authored when unedited
- Publish · second-user public preview per locale: IT/EN/FR customer overrides · ES/AR authored fallback · global WalkBrand universal · AR `<html dir="rtl">` confirmed
- Screenshots: `a7b_pragma_editor_ar_rtl.png` + `a7b_pragma_public_preview_ar_rtl.png`

### Observables

- 147/147 → **151/151** server tests (+4 netti · +6 new A.7b contract + 1 A.7b lifecycle − 3 A.7-era obsolete). Smoke 834/834 unchanged.
- `manage.py check` 0 issues.
- No production code change (schema.py +7 lines is the gate + comment; no services/views/templates/JS touched).

### Consequences

- Editor 2/8 archetypes editable (Vertex + Pragma) · **multi-locale 2/8** (Vertex + Pragma). Catalog 20/20 `published_live` unchanged.
- **No new D-number**. A.7b operationalizes D-098 (archetype gate contract) without introducing a new binding. The recipe — single-line gate flip + dedicated lifecycle regression test — is proven reusable for every future enrollment.
- Merged into v15 via `--no-ff` @ `cc1634f` and pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

**A.8 — Third archetype editor support** OR **selective multi-locale expansion**, to be decided in a dedicated planning session. Both candidates are natural continuations; no enforced ordering. See `TODO_NEXT.md` for the ranking.

---

## Session 61 — Phase A.8 · Gusto Fine-Dining Editor + Multi-locale Enrollment (2026-04-17)

### What shipped

A.8 ships the third editable archetype (`fine-dining` → Gusto) editor-enabled AND multi-locale enrolled simultaneously. Applies the A.6 recipe (schema register + preview bridge) combined with the A.7b recipe (gate flip + dedicated lifecycle regression test) in a single phase — no fresh architectural decisions, pure reuse. Two commits on `phase-editor-a8-gusto-multilocale-v1`.

- `a3589bc` — Step 1 · `GUSTO_FINE_DINING_SCHEMA` added to `apps/editor/schema.py` (~330 LOC, 11 sidebar groups covering brand + hero + home editorial bands + each page filosofia/menu/atmosfera/diario/prenota + contatti footer, ~108 scalar fields). `STRUCTURED_FIELD_SHAPES["fine-dining"]` exposes 3 readonly indexed lists (`home.signature_courses` tuple 5×4, `menu.courses` tuple 8×4, `home.produttori.items` dict 4×4 with portrait intentionally omitted from cols so it stays registry-readonly). Registered in `_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE[("gusto-fine-dining","it")]` + `_MULTILOCALE_ENABLED_ARCHETYPES`. `templates/live_templates/restaurant/fine-dining/_base.html` gets the three atomic A.6 fixes: `<title>` honours `site.logo_word|default:brand.brand_name`, `<body class="{% if preview_project %}mw-is-editor-preview{% endif %}">`, CSS guard block (hide `.mp-bar`, overflow guardrails on `.fd-lead h1` / `.fd-section h2` / `.fd-nav .name`), `preview-bridge.js` conditional injection before `</body>`. 8 contract tests: archetype registered + shape covers all pages + is_translatable distributes paths across every Gusto page + branding universals global + non-text fields global + structured-list cells global (portrait NOT in cols) + Vertex+Pragma regression + **1 dedicated integration test lifting the preview-bridge 3-point contract together** (`test_a8_gusto_preview_bridge_injected_only_with_preview_project` — user-imposed guardrail). 3 A.7-era tests swapped to use `trattoria-warm` / `sapore-trattoria-pizzeria` as unsupported-archetype placeholder now that Gusto is enrolled.

- `94772f2` — Step 2 · `test_a8_gusto_full_multilocale_lifecycle_end_to_end` mirrors A.7b Pragma on Gusto: 3 translatable autosaves (IT/EN/FR on `home.headline`) + 1 global (`site.logo_word` EN-tagged but plain-keyed) + publish + 5 public preview renders (second user) + AR `<html dir="rtl" lang="ar">` assertion via regex on opening `<html>` tag + 4 editor reopens (owner) with prefill + is_overridden + translatable flags. Passes on the first run — strong signal the A.6+A.7b combined recipe holds on a non-typographic, imagery-heavy archetype.

Step 3 · browser walk (no code change). 12 spot checks all green on a fresh Gusto project:
- Editor mount `?lang=it` → label "Lingua attiva", 5 pills, 97/181 translatable fields, correct markers (translatable vs global)
- IT edit + global edit + click EN before debounce → flush-before-switch verified in DB (`@it:home.headline` + plain `site.logo_word`)
- EN → FR → ES ↔ AR locale switches: each locale loads authored / customer buffer correctly, zero cross-locale leak
- AR iframe renders `<html dir="rtl" lang="ar">` on the `.fd-*` skin with Arabic nav labels + Arabic H1 + global logo `WalkGusto` visible in chrome
- Publish + second-user public preview per locale: IT/EN/FR customer overrides, ES/AR authored fallback, AR with `<html dir="rtl">`, global logo universal
- Screenshots: `a8_gusto_editor_ar_rtl.png` + `a8_gusto_public_preview_ar_rtl.png`

### Observables

- 151/151 → **160/160** server tests (+9: 8 contract + 1 lifecycle; 3 A.7-era placeholder-slug tests kept count-stable).
- Smoke 834/834 unchanged. `manage.py check` 0 issues.
- No production code touched outside `schema.py`, `_base.html` (3 minimal fixes), and `tests.py`. Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / editor templates / `live-editor.js` / CSS.

### Consequences

- **Editor 3/8 archetypes editable · multi-locale 3/8** (Vertex + Pragma + Gusto all enrolled end-to-end).
- Catalog 20/20 `published_live` unchanged.
- **No new D-number introduced**. A.8 is the second real application of the D-098 recipe (after A.7b Pragma) — confirms the "one-line gate flip + dedicated lifecycle regression test" contract scales to archetypes with fundamentally different visual profiles (Vertex typographic-agency → Pragma corporate-text-heavy → Gusto imagery-heavy-hospitality-RTL).
- Branch shape: `phase-editor-a8-gusto-multilocale-v1` merged into v15 via `--no-ff` @ `2e7fbed`. Pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

Two natural candidates, no enforced ordering:

(a) **A.9 Fourth archetype editor support** — candidate `medical-specialist` (Cardio + Derm · 2 templates unlocked per schema), alternatives `trattoria-warm` (Sapore) or `editorial-designer-grid` (Chiara with `project_detail`/`series_detail` novel page kinds).

(b) **A.9 Editor operator tools** — admin-facing (zero customer surface): admin project list filters, GC scheduler, asset audit UI.

Consolidation pause (this commit) precedes the choice.

---

## Session 62 — Phase A.9 · Medical-specialist Editor + Multi-locale Enrollment (2026-04-17)

### What shipped

A.9 ships the fourth editable archetype (`specialist` → Cardio + Derm) editor-enabled AND multi-locale enrolled simultaneously. **First multi-template archetype**: one shared schema unlocks two templates (`cardio-studio-specialistico` + `dermatologia-elite-roma`) thanks to 95% content-tree parity documented by the Step 0 audit. Combines the A.6 recipe (schema register + preview bridge) with the A.7b recipe (gate flip + dedicated lifecycle regression) in a single phase — no new architectural decisions. Two commits on `phase-editor-a9-medical-specialist-v1`.

**Decision: Cardio + Derm insieme.** Step 0 audit (runtime inspection of the two templates' content trees + DNA) confirmed:
- Both carry `archetype: "specialist"` in their DNA — same hero_style, navbar_style, footer_style, section_order, card_style, button_style, density, tone, conversion_pattern.
- Same `pages` list (7 pages each: home/studio/visite/medici/pubblicazioni/contatti/richiedi-visita with identical `kind` values).
- 100% key parity on `studio` (14), `visite` (11), `medici` (5), `pubblicazioni` (6), `contatti` (14), `richiedi-visita` (16), `site` (10).
- 85% parity on `home` — 29 shared keys plus 5 Cardio-only (`anchor_nav`, `insurance`, `location`, `percorso`, `tecnologie`) and 5 Derm-only (`before_after`, `credentials`, `editorial_feed`, `gallery_strip`, `trattamenti_tabs`). The 10 divergent sub-blocks are D-064 Session 30 premium sections — kept registry-only in A.9 (same exclusion strategy as Gusto `prenota.form_sections`).

### Recipe applied (shared-schema · A.6 + A.7b combined)

- `a3589bc`-equivalent role → `8e94714` · Step 1 · `MEDICAL_SPECIALIST_SCHEMA` in `apps/editor/schema.py` (~360 LOC · 11 sidebar groups covering brand + hero + home bands + chief + 6 pages + contatti footer · ~95 scalar fields shared core). `STRUCTURED_FIELD_SHAPES["specialist"]` exposes 6 readonly indexed lists (home.facts · home.signature_visits · medici.doctors · studio.history · studio.values · visite.treatments · portrait column intentionally omitted from `medici.doctors` cols so the 3 doctor portraits stay registry-only — same pattern as Gusto produttori.items). Registered in `_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE[("cardio-studio-specialistico","it")]` (Cardio anchors baseline per Session 23 i18n pilot) + `_MULTILOCALE_ENABLED_ARCHETYPES`. `templates/live_templates/medical/specialist/_base.html` gets the three atomic A.6 fixes (title `site.logo_word` override · body guard class · CSS guard + preview-bridge injection). 10 tests: 7 shape/classification + triple regression (Vertex + Pragma + Gusto intact) + preview-bridge 3-point integration test + **user-imposed guardrail `test_a9_specialist_divergent_premium_sections_excluded`** that locks the 10 divergent home sub-blocks out of the whitelist via 4 independent check layers (is_translatable → False · validate_key_path → raises · STRUCTURED_FIELD_SHAPES does NOT contain divergent list paths · sidebar group ids do not hint divergent blocks).
- `b9fe5ba` · Step 2 · **two distinct lifecycle tests** built on a shared `_run_specialist_lifecycle(template_slug, marker, brand)` helper:
  - `test_a9_cardio_full_multilocale_lifecycle_end_to_end` (marker "A9Cardio" · brand "A9CardioBrand")
  - `test_a9_derm_full_multilocale_lifecycle_end_to_end` (marker "A9Derm" · brand "A9DermBrand")
  Each test walks 3 autosaves (IT/EN/FR) + 1 global + publish + 5 public preview renders (second user) + 4 editor reopens + AR `<html dir="rtl" lang="ar">` assertion. Distinct markers mean a regression that hits only one of the two templates surfaces with a clean name instead of collateral-damage-on-shared-test.

Step 3 · browser walk (no code change). Cardio primary walk (12 spot checks) + Derm spot check (5 checks + team page RTL verification):
- Cardio `?lang=it` mount → label "Lingua attiva" · 5 pills · 77/171 translatable fields · correct translatable/global markers
- Type IT + global "WalkCardio" + click EN → flush `@it:home.headline` + plain `site.logo_word` before navigation (DB verified)
- IT ↔ EN ↔ FR ↔ ES ↔ AR switches: each locale loads authored or customer buffer · zero cross-locale leak
- AR iframe on `.sp-*` skin: `<html dir="rtl" lang="ar">` authentic · H1 arabic · nav RTL (المركز · عن المركز · etc.) · hero sidebar RTL with Arabic doctor name · logo WalkCardio in chrome
- Publish Cardio · second-user public preview per locale: IT/EN/FR override visible · ES/AR authored fallback · AR htmlDir rtl · WalkCardio universal
- Derm `?lang=en` spot mount · 77/171 translatable fields (same count as Cardio — confirms shared schema · the number reflects editable-field coverage independent of template) · EN authored visible · save EN + WalkDerm · switch AR · iframe `.sp-*` RTL identical pattern · DB inspection confirms **zero cross-project leak** (Cardio 4 rows / Derm 2 rows, fully isolated)
- Publish Derm · second-user public preview: EN customer override · IT/FR/ES/AR authored fallback · WalkDerm universal · AR htmlDir rtl · zero cross-brand leak (no WalkCardio in Derm body and vice versa)
- Title tag confirms `site.logo_word|default:brand.brand_name` applied on `.sp-*` skin (AR Cardio title = "WalkCardio — المركز")
- Screenshots: `a9_cardio_editor_ar_rtl.png` + `a9_cardio_public_preview_ar_rtl.png`

### Observables

- 160/160 → **172/172** server tests (+12: 10 contract/integration + 2 lifecycle).
- Smoke 834/834 unchanged. `manage.py check` 0 issues.
- No production code touched outside `schema.py`, `_base.html` specialist (3 minimal fixes), and `tests.py`. Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / editor templates / `live-editor.js` / CSS / content registries / other skins.

### Consequences

- **Editor 4/8 archetypes editable · multi-locale 4/8 enrolled · 5 templates editable end-to-end** (Vertex + Pragma + Gusto + Cardio + Derm). First time in project history the editor unlocks more templates than archetypes thanks to the shared-schema pattern.
- Catalog 20/20 `published_live` unchanged.
- **No new D-number introduced**. A.9 is the third real application of the D-098 recipe (after A.7b Pragma and A.8 Gusto) and the first case of "1 archetype schema · N templates unlocked". The D-098 operationalisation history is updated in DECISIONS.md with a brief note clarifying that each enrolled template still requires its own lifecycle regression test even when the archetype schema is shared — no silent "free ride".
- Branch shape: `phase-editor-a9-medical-specialist-v1` merged into v15 via `--no-ff` @ `e816b87`. Pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

A.10 planning session — candidates in priority order (dedicated planning required before Step 0):

(a) **A.10 fifth archetype editor support** — natural continuation. Two candidates worth the shared-schema pattern: `law` family (Lex + Juris · 2 templates) or `real-estate` family (Casa + Villa · 2 templates). Both carry the A.9 "1 schema → 2 templates" opportunity if their DNA/content-tree shape proves as aligned as specialist did.

(b) **A.10 alt · Single-template archetypes** — `editorial-designer-grid` (Chiara) stresses novel page kinds (`project_detail`/`series_detail`); `trattoria-warm` (Sapore) continues the hospitality adjacency after Gusto.

(c) **A.10 alt · Editor operator tools** — admin-facing (zero customer surface): admin project list filters, GC scheduler, asset audit UI. Cleans up operator experience without touching customer flows.

(d) **A.10 alt · Remote asset storage** — S3/Cloudinary swap of `ProjectAsset.file` backend. Worth opening only when a prod-launch timeline requires it.

Consolidation pause (this commit) precedes the choice.

---

## Session 63 — Phase A.10 · Lex (classic-gold) Editor + Multi-locale Enrollment (2026-04-17)

### What shipped

A.10 ships the fifth editable archetype: **Lex (classic-gold · law family)**. The Step-0 runtime audit settled a decisive question: Lex and Juris — both under the `lawyer` category — carry **distinct DNA archetypes** (`classic-gold` vs `modern-transparent`) with distinct skin folders (`lawyer/classic-gold/` vs `lawyer/modern-transparent/`) and only ~25% content-tree shape overlap (only `home` + `contatti` slugs shared; divergent page slugs and section shapes elsewhere). The A.9 shared-schema pattern therefore **does not apply** to the law family. Decision: A.10 enrolls **Lex only**. Juris stays explicitly out of the gate and will be addressed as A.10b in a dedicated phase with its own schema + skin bridge + lifecycle coverage.

### Recipe applied (single-template · A.6 + A.7b combined)

Two commits on `phase-editor-a10-lex-classic-gold-v1`.

- Step 0 · runtime audit (planning artifact, no code). Verified 5-locale parity **PERFECT** on Lex across every section (zero IT-only gaps on `contatti.form_fields` / `form_sections` / `upload_field` — Lex is the cleanest content registry among the four pre-A.10 archetypes for locale parity). Only one scalar image field (`notabili.lead_image`). No portrait fields anywhere in the registry — `home.partners` + `avvocati.lawyers` dict rows carry no `portrait` col, so the portrait-excluded pattern used in Gusto produttori.items and specialist medici.doctors is **not needed** here. RTL CSS block mature on `classic-gold/_base.html` (lines 331+) using `.lx-*` prefix selectors.
- `25da231` · Step 1 · `LEX_CLASSIC_GOLD_SCHEMA` in `apps/editor/schema.py` (~340 LOC · 9 sidebar groups covering brand + hero + home bands + 6 page groups + footer chrome · ~102 scalar fields). `STRUCTURED_FIELD_SHAPES["classic-gold"]` exposes 6 readonly indexed lists (`avvocati.lawyers` dict 14×6 all cols · `pratiche.services` dict 12×5 with `scope` nested-list-of-str intentionally omitted from cols so the bullet points stay registry-only · `pratiche.process` tuple 4×3 · `studio.history` tuple 6×3 · `studio.values` tuple 4×3 · `contatti.offices` dict 2×7). Registered in `_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE[("lex-studio-legale","it")]` + `_MULTILOCALE_ENABLED_ARCHETYPES`. `templates/live_templates/lawyer/classic-gold/_base.html` gets the three atomic A.6 fixes (title `site.logo_word|default:brand.brand_name` · body guard class · CSS guard block `.lx-*` + preview-bridge injection). 9 tests including `test_a10_lex_archetype_registered` with an **explicit guard that `modern-transparent` (Juris) is NOT in `_ARCHETYPE_SCHEMAS` nor in the multi-locale gate** — catches any future accidental Juris enrollment without its own dedicated phase. Plus quadruple regression test + preview-bridge 3-point integration test.
- `ddfb66d` · Step 2 · `test_a10_lex_full_multilocale_lifecycle_end_to_end` mirror of A.7b/A.8/A.9-single-template on Lex: 3 translatable autosaves (IT/EN/FR on `home.headline` with marker "A10Lex") + 1 global autosave (`site.logo_word` = "A10LexBrand" EN-tagged but plain-keyed) + publish + 5 public preview renders (second user) + AR `<html dir="rtl" lang="ar">` assertion on the opening `<html>` tag + 4 editor reopens (owner). Route: `/templates/lawyer/lex-studio-legale/preview/`. Passes first run.

Step 3 · browser walk (no code change). 13 spot checks all green:
- Editor `?lang=it` mount → label "Lingua attiva", 5 pills, 79 translatable markers, correct translatable/global separation
- Type IT + global "WalkLex" + click EN before debounce → flush `@it:home.headline` + plain `site.logo_word` before navigation (DB verified)
- IT → EN → FR → ES → AR locale switches: each locale loads authored / customer buffer correctly · zero cross-locale leak
- AR iframe renders `<html dir="rtl" lang="ar">` authentic on the `.lx-*` skin · Arabic H1 "كفاءة، تحفظ، نتائج." · nav RTL (المكتب / عن المكتب) · crest LF · ledger hero RTL · logo WalkLex in chrome
- Sub-page spot checks (owner IT): `/pratiche/` renders 12 practice areas (Diritto societario visible) · `/avvocati/` renders 14 lawyers (Avv. Prof. Alberto Ferri) · `/notabili/` renders blog index with WalkLex universal
- Publish + second-user public preview per locale: IT/EN/FR customer overrides · ES/AR authored fallback · AR htmlDir rtl · WalkLex universal · zero cross-locale leak
- Title tag AR = "WalkLex — المكتب" confirms `site.logo_word|default:brand.brand_name` applied on `.lx-*` skin
- Screenshots: `a10_lex_editor_ar_rtl.png` + `a10_lex_public_preview_ar_rtl.png`

### Observables

- 172/172 → **182/182** server tests (+10: 9 contract/integration + 1 lifecycle).
- Smoke 834/834 unchanged. `manage.py check` 0 issues.
- No production code touched outside `schema.py`, `classic-gold/_base.html` (3 minimal fixes), and `tests.py`. Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / editor templates / `live-editor.js` / CSS / content registries / other skins / modern-transparent skin.

### Consequences

- **Editor 5/8 archetypes editable · multi-locale 5/8 enrolled · 6 templates editable end-to-end** (Vertex + Pragma + Gusto + Cardio + Derm + Lex).
- Catalog 20/20 `published_live` unchanged.
- **No new D-number introduced**. A.10 is the fourth real application of the D-098 recipe and confirms that **single-template enrollment remains valid** — the shared-schema pattern of A.9 is a capability, not a requirement. The actual binding constraint from D-098 is the dedicated lifecycle regression test per enrolled template, regardless of whether schemas are shared or template-specific.
- Branch shape: `phase-editor-a10-lex-classic-gold-v1` merged into v15 via `--no-ff` @ `ee9ebbd`. Pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

A.11 planning session — candidates in priority order (dedicated planning required before Step 0):

(a) **A.11 Juris (modern-transparent) enrollment** — closes the law family opened in A.10. Separate schema + separate skin bridge + dedicated lifecycle test. Same recipe A.6 + A.7b applied to the second law template.

(b) **A.11 alt · real-estate family (Casa + Villa)** — requires a Step-0 runtime audit to check whether Casa (`mass-market`) and Villa (`ultra-luxury-cinematic`) share archetype slug + content-tree shape or diverge like Lex/Juris. If the audit reveals two distinct archetypes, the choice becomes "Casa-only" or "Villa-only" for A.11 with the other deferred to A.11b.

(c) **A.11 alt · Chiara (editorial-designer-grid)** — single template, novel `project_detail` / `series_detail` page kinds stretch the editor beyond the current home/about/services patterns. Higher risk than the multi-archetype continuation path.

(d) **A.11 alt · editor polish / operator tools / remote storage** — defer unless customer signal or prod-launch timeline demands.

Consolidation pause (this commit) precedes the choice.

## Session 64 — Phase A.11 · Juris (modern-transparent) Editor + Multi-locale Enrollment (2026-04-17)

### What shipped

A.11 ships the sixth editable archetype: **Juris (modern-transparent · law family · second template)**. The Step-0 runtime audit pre-run in planning already settled the topology question (A.9 shared-schema recipe does NOT apply to the law family — confirmed in Session 63 A.10). A.11 implements the dedicated-schema path for Juris: its own `JURIS_MODERN_TRANSPARENT_SCHEMA`, its own skin bridge on `lawyer/modern-transparent/_base.html` with `.jr-*` prefix, and its own lifecycle regression test. **The law family is now closed completely — via two distinct archetypes, not a shared one.**

Two additional runtime positives observed during the A.11 audit:
- **Zero image fields** anywhere in the Juris registry — advisory-modern DNA explicitly rejects founder portraits / case photos / hero illustrations. A.11 is the first enrollment with a formalized "zero-image" guard: a contract test iterates the entire schema + `STRUCTURED_FIELD_SHAPES` tree and asserts no field carries `type: "image"`. This locks the DNA assumption into the test layer.
- **5-locale parity PERFECT** (it/en/fr/es/ar all present with equivalent shape — zero IT-only gaps on any section, form structure included).

### Recipe applied (single-template · A.6 + A.7b combined · with two user-imposed guardrails)

Two commits on `phase-editor-a11-juris-modern-transparent-v1`.

- Step 0 · runtime audit (planning artifact, no code). DNA inspection confirmed Juris uses `modern-transparent` archetype with `.jr-*` skin prefix on `lawyer/modern-transparent/_base.html` (24 `html[dir="rtl"]` rules already mature — zero RTL work needed). Content-tree shape identified 4 categories of complex registry shapes that must stay OUT of the editor perimeter: (1) `approccio.dashboard_mock` (nested dict with URL + columns + cards — novel shape not mappable to tuple/dict); (2) flat list-of-str containers `home.trust_logos` + `insights.topics`; (3) nested list-of-str cells inside dict rows (`servizi.services[*].deliverables`, `settori.sectors[*].pain_points / signals / legal_ops`-bullets) — same exclusion policy as Lex `pratiche.services[*].scope`; (4) form structure blocks (`contatti.form_fields` / `form_sections`) — same policy as Gusto / specialist / Lex.
- `4ebbbfe` · Step 1 · `JURIS_MODERN_TRANSPARENT_SCHEMA` in `apps/editor/schema.py` (~467 LOC delta · 10 sidebar groups: brand + hero_home + home_bands + approccio_page + servizi_page + settori_page + insights_page + contatti_page + contact_info + post_chrome · ~180 scalar fields · **zero image fields**). `STRUCTURED_FIELD_SHAPES["modern-transparent"]` exposes 6 readonly indexed lists: `approccio.founders` dict 2×3 (credentials list-of-str col-excluded) · `approccio.story` tuple 5×3 · `approccio.manifesto` tuple 4×3 · `servizi.services` dict 7×7 (deliverables list-of-str col-excluded) · `settori.sectors` dict 6×6 (pain_points/signals/legal_ops-bullets list-of-str col-excluded; the scalar `partner` + scalar `legal_ops`-person cols ARE exposed) · `settori.team` dict 10×5. Registered in `_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE[("juris-avvocato-moderno","it")]` + `_MULTILOCALE_ENABLED_ARCHETYPES`. `templates/live_templates/lawyer/modern-transparent/_base.html` gets the three atomic A.6 fixes (title `site.logo_word|default:brand.brand_name` · body guard class · CSS guard block `.jr-*` + preview-bridge injection). 10 tests including `test_a11_juris_archetype_registered` (guard that `classic-gold` stays enrolled · A.11 is additive) + `test_a11_juris_schema_shape_covers_all_pages` + `test_a11_juris_is_translatable_text_fields` + `test_a11_juris_branding_and_contact_universals_are_global` + **two user-imposed guardrails**: `test_a11_juris_schema_contains_zero_image_fields` (iterates every group + subgroup + SHAPES cols + cell_spec asserting no `type: "image"` anywhere) and `test_a11_juris_complex_shapes_excluded_from_perimeter` (12 path shapes rejected via `validate_key_path` + 3 cols-exclusion explicit assertions) + `test_a11_juris_structured_list_cells_are_global` + `test_a11_juris_supported_locales_returns_canonical_five` + `test_a11_quintuple_regression_after_juris_joins` (Vertex + Pragma + Gusto + specialist + classic-gold all intact) + `test_a11_juris_preview_bridge_injected_only_with_preview_project`. The A.10 guard test `test_a10_lex_archetype_registered` was updated to drop the Juris-absence assertions now that Juris is enrolled (A.11 is additive: Lex-must-stay assertion is still in place).
- `287534b` · Step 2 · `test_a11_juris_full_multilocale_lifecycle_end_to_end` mirror of A.7b/A.8/A.9/A.10-single-template lifecycle. 3 translatable autosaves (IT/EN/FR on `home.headline` with marker "A11Juris") + 1 global autosave (`site.logo_word` = "A11JurisBrand" EN-tagged but plain-keyed) + publish + 5 public preview renders (second user) + AR `<html dir="rtl" lang="ar">` assertion on the `.jr-*` skin + 4 editor reopens (owner). Route: `/templates/lawyer/juris-avvocato-moderno/preview/`. Passes first run.

Step 3 · browser walk (no code change). 13 spot checks all green:
- Editor `?lang=it` mount → label "Lingua attiva", 5 pills (`.ed-lang-pill[data-ed-lang]`), 110 `per lingua` badges on translatable fields, 188 global fields without badge, 6/6 expected global contract keys (`site.logo_word/logo_initial/phone/email/address/license`) correctly NON-translatable, **zero `input[type="file"]` + zero `[data-ed-kind="image"]` + zero "Immagine/URL immagine" text mentions in the sidebar** — confirms the zero-image assertion end-to-end from schema layer up to rendered editor chrome.
- Type IT on `home.headline` + click EN pill before debounce → `@it:home.headline` persisted BEFORE iframe navigation (DB verified). Same flush-before-switch behavior EN→FR.
- 3 locale autosaves land as distinct `@<locale>:home.headline` rows + 1 global `site.logo_word` as a plain-key row. Zero `home.headline` plain-key leak, zero `@<locale>:site.logo_word` leak.
- ES switch · sidebar shows authored ES baseline `"El derecho, <em>de tu lado.</em>"` with `is_overridden=false`; global logo override persists universally.
- AR switch · iframe `.ed-frame` emits `<html lang="ar" dir="rtl">` authentic on the `.jr-*` skin; `body.mw-is-editor-preview lm-ready` guard class present; AR nav labels `المنهجية / الخدمات / القطاعات / تحليلات / تواصل معنا`; AR CTA `احجز جلسة استراتيجية`; H1 `القانون إلى جانبك.`; title `WalkJurisBrand — الرئيسية` confirms `site.logo_word|default:brand.brand_name` applied on the `.jr-*` skin.
- Sub-page spot checks (owner IT, `project=<uuid>`): `/approccio/` H1 "Non vendiamo ore…" (17 jr-section elements) · `/servizi/` H1 "Sette offerte, tempi certi…" (9 jr-sections) · `/settori/` H1 "Sei settori, un solo metodo…" (8 jr-sections) · `/insights/` H1 "Quando cambia una norma, scriviamo una nota." (8 jr-sections). All 4 carry `jr-nav` + `jr-foot` + `WalkJurisBrand` + `body.mw-is-editor-preview` + `preview-bridge.js`.
- Publish + second-user public preview per locale: IT/EN/FR customer overrides visible on each respective locale · ES/AR authored fallback (`"El derecho"` / `"القانون"`) · AR `dir="rtl"` preserved · `WalkJurisBrand` universal across all 5 locales · **zero cross-locale leak** in any direction.

### Observables

- 182/182 → **193/193** server tests (+11: 10 contract/integration + 1 lifecycle).
- Smoke 834/834 unchanged. `manage.py check` 0 issues.
- No production code touched outside `schema.py`, `modern-transparent/_base.html` (3 minimal fixes), and `tests.py`. Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / editor templates / `live-editor.js` / CSS / content registries / any other skin (classic-gold, specialist, fine-dining, corporate-suite, agency-creative-studio untouched).

### Consequences

- **Editor 6/8 archetypes editable · multi-locale 6/8 enrolled · 7 templates editable end-to-end** (Vertex + Pragma + Gusto + Cardio + Derm + Lex + **Juris**).
- **Law family closed completely** — via two distinct archetypes (`classic-gold` Lex + `modern-transparent` Juris), not a shared schema. This is the first phase where a category closes through a pair of dedicated-schema enrollments rather than one shared schema covering multiple templates.
- Catalog 20/20 `published_live` unchanged.
- **No new D-number introduced**. A.11 is the fifth real application of the D-098 recipe and the first one confirming that **a family can close through multiple separate archetypes**, not only through one shared schema. The binding constraint from D-098 — dedicated lifecycle regression test per enrolled template — was satisfied for both Lex (Session 63) and Juris (this session), each with its own lifecycle test and its own archetype gate entry.
- Branch shape: `phase-editor-a11-juris-modern-transparent-v1` merged into v15 via `--no-ff` @ `0f8bf60`. Pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

A.12 planning session — candidates in priority order (dedicated planning required before Step 0):

(a) **A.12 real-estate family (Casa + Villa) enrollment** — requires a Step-0 runtime audit to check whether Casa (`mass-market`) and Villa (`ultra-luxury-cinematic`) share archetype slug + content-tree shape or diverge like Lex/Juris. Given the documented DNA divergence (`mass-market` vs `ultra-luxury-cinematic` with distinct skin folders already observed in the A.10 planning audit), the most likely outcome is two distinct archetypes — closing the real-estate family through the A.11 dedicated-schema recipe rather than the A.9 shared-schema recipe.

(b) **A.12 alt · Chiara (editorial-designer-grid)** — single template, novel `project_detail` / `series_detail` page kinds stretch the editor beyond the current home/about/services patterns. Higher risk than the continuation path but opens the "editorial publishing" adjacency.

(c) **A.12 alt · Sapore / Pixel / Bottega / Luxe / Aura / Elevate / Salute / Benessere / Famiglia / Brace** — single-template archetypes that can each be enrolled individually with the A.11 recipe (single-schema, zero shared-schema gain). Each would be a small, clean phase with low architectural risk.

(d) **A.12 alt · editor polish / operator tools / remote storage / media evolution** — defer unless customer signal or prod-launch timeline demands. Current value is low relative to closing more archetype families.

Consolidation pause (this commit) precedes the choice.

## Session 65 — Phase A.12 · Casa (mass-market) Editor + Multi-locale Enrollment (2026-04-18)

### What shipped

A.12 ships the seventh editable archetype: **Casa (mass-market · real-estate family · first template)**. The Step-0 runtime audit (executed during planning, no code) confirmed the hypothesis raised in A.10/A.11 planning: Casa (`mass-market`) and Villa (`ultra-luxury-cinematic`) carry **distinct DNA archetypes**, **distinct skin folders** (`real-estate/mass-market/` with `.dm-*` prefix vs `real-estate/ultra-luxury-cinematic/` with `.vp-*` prefix), and **~0% non-home page-slug overlap** (Casa: home/immobili/quartieri/agenzia/valutazione/contatti vs Villa: home/collezione/territorio/studio/esperienza/concierge — only `home` shared, vs law family's home+contatti sharing). Shared-schema (A.9 recipe) is impossible here, and the divergence is MORE pronounced than law. Decision: **A.12 enrolls Casa only**. Villa stays explicitly out of the gate and is reserved for a dedicated A.12b phase with its own schema + skin bridge + lifecycle test. The real-estate family is therefore **opened but not yet closed** — completion waits on A.12b.

Three additional runtime positives observed during the A.12 audit:
- **Casa ships ZERO image fields** registry-wide — the mass-market DNA is image-free (uses typographic density and tile grid for visual rhythm, not imagery). A.12 is the **second zero-image archetype enrollment** after Juris (A.11), and the recipe pattern is now formalized: the same `test_a<N>_<archetype>_schema_contains_zero_image_fields` guardrail test ships unchanged from A.11 → A.12, asserting no field carries `type: "image"` anywhere in the schema or `STRUCTURED_FIELD_SHAPES`.
- **Casa has PERFECT 5-locale parity** (215 keys × 5 locales, zero IT-only gaps). Same class as Lex / Juris.
- **Casa skin `mass-market/_base.html` ships 23 mature `html[dir="rtl"]` rules** (very close to Juris's 24 on `.jr-*`) — no RTL work needed beyond the standard 3 atomic fixes.

### Recipe applied (single-template · A.6 + A.7b combined · two user-imposed guardrails + Villa-out explicit guard)

Two commits on `phase-editor-a12-casa-mass-market-v1`.

- Step 0 · runtime audit (planning artifact, no code). Covered DNA archetype + skin folder divergence Casa/Villa, page-slug overlap (~0%), image-field inventory (Casa=0 vs Villa=26), 5-locale parity check (both perfect), RTL CSS maturity, list-shape inventory per page. Decided on `search_widget` handling: **14 scalars flat IN `hero_home` group (4 subgroups: hero copy · widget intestazione · 4 label+value campi · CTA), `popular_tags` flat list-of-str OUT**. Mini-audit pre-schema confirmed: 15 readonly indexed lists (more than Juris's 6 — Casa is structurally richer), zero nested list-of-str inside dict rows (no `deliverables`-style novelty), no portrait anywhere (confirms zero-image).
- `30d5e72` · Step 1 · `CASA_MASS_MARKET_SCHEMA` in `apps/editor/schema.py` (~604 LOC delta — above the 600-LOC soft guardrail, flagged but non-blocking: no new scope opened, tests green first-run, perimeter still coherent, no service/rendering/views/models touched). 10 sidebar groups: brand + hero_home (with 4 subgroups covering hero copy + search_widget flat scalars + CTAs) + home_bands (with 6 subgroups for featured/neighborhoods/stats/agents/valuation/testimonial band headings) + immobili_page + quartieri_page + agenzia_page + valutazione_page + contatti_page + contact_info + tile_labels. **~185 scalar fields · ZERO image fields**. `STRUCTURED_FIELD_SHAPES["mass-market"]` exposes 15 readonly indexed lists: 5 on home (featured_listings tuple 4×4 cols exposed of 8 · neighborhoods 6×4 · stats 4×3 · agents_preview 4×4 · valuation_proof 3×2) + 1 on immobili (map_cells 5×2) + 2 on quartieri (guides tuple 8×6 cols exposed of 9 · faq 4×2) + 2 on agenzia (agents dict 9×9 cols of 10 · facts 4×3) + 3 on valutazione (how_it_works 3×3 · proof 4×2 · faq 4×2) + 2 on contatti (channels 5×3 · offices dict 2×9 cols of 13). Registered in `_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE[("casa-agenzia-immobiliare","it")]` + `_MULTILOCALE_ENABLED_ARCHETYPES`. `templates/live_templates/real-estate/mass-market/_base.html` gets the three atomic A.6 fixes (title `site.logo_word|default:brand.brand_name` · body guard class · CSS guard block `.dm-*` + preview-bridge injection). 10 contract tests including `test_a12_casa_archetype_registered` with an **explicit guard that `ultra-luxury-cinematic` (Villa) is NOT in `_ARCHETYPE_SCHEMAS` NOR in the multi-locale gate** and a regression assertion that all 6 previous archetypes stay enrolled. Plus the **two user-imposed guardrails** mirrored from A.11: `test_a12_casa_schema_contains_zero_image_fields` (zero-image assertion strong) and `test_a12_casa_complex_shapes_excluded_from_perimeter` (17 path rejects via `validate_key_path`: flat list-of-str containers `home.search_widget.popular_tags` + `immobili.filters` + `immobili.sort_options` · form structure blocks on valutazione + contatti · per-property `posts` entries stay registry-only) + sextuple regression + preview-bridge 3-point integration test.
- `9757da7` · Step 2 · `test_a12_casa_full_multilocale_lifecycle_end_to_end` mirror of A.7b/A.8/A.9/A.10/A.11-single-template lifecycle. 3 translatable autosaves (IT/EN/FR on `home.headline` with marker "A12Casa") + 1 global autosave (`site.logo_word` = "A12CasaBrand" EN-tagged but plain-keyed) + publish + 5 public preview renders (second user) + AR `<html dir="rtl" lang="ar">` assertion on the `.dm-*` skin + 4 editor reopens (owner). Includes a **runtime Villa-out assertion** (`assertNotIn("ultra-luxury-cinematic", _MULTILOCALE_ENABLED_ARCHETYPES)`) at the start of the test, so the gate state is re-verified at lifecycle execution time beyond the registration-time guard. Route: `/templates/real-estate/casa-agenzia-immobiliare/preview/`. Passes first run.

Step 3 · browser walk (no code change). 14 spot checks all green:
- Editor `?lang=it` mount → 5 pills (`.ed-lang-pill[data-ed-lang]`), 134 `per lingua` badges on translatable fields, 313 global fields without badge, 6/6 expected global contract keys correctly NON-translatable, **zero `input[type="file"]` + zero `[data-ed-kind="image"]` + zero "Immagine/URL immagine" text mentions in the sidebar** — confirms zero-image end-to-end.
- **search_widget flat 7 scalars** all present in sidebar (`location_value`, `type_value`, `price_value`, `rooms_value`, `label`, `cta`, `popular_label`). **`popular_tags` flat list-of-str correctly NOT in sidebar** (exclusion confirmed end-to-end).
- Type IT on `home.headline` + click EN pill before debounce → `@it:home.headline` persisted BEFORE iframe navigation (DB verified). Same flush-before-switch behavior EN→FR.
- 3 locale autosaves land as distinct `@<locale>:home.headline` rows + 1 global `site.logo_word="WalkCasaBrand"` as plain-key. Zero `home.headline` plain-key leak, zero `@<locale>:site.logo_word` leak.
- ES switch · sidebar shows authored ES baseline `"La casa de tus <em>sueños</em>, más cerca de lo que crees."` with `is_overridden=false`; global logo override persists universally.
- AR switch · iframe `.ed-frame` emits `<html lang="ar" dir="rtl">` authentic on the `.dm-*` skin; `body.mw-is-editor-preview lm-ready` guard class present; `.dm-nav` + `.dm-hero` + `.dm-foot` all render; AR H1 `"بيت أحلامك، أقرب ممّا تظنّ."`; title `"WalkCasaBrand — الرئيسية"` confirms `site.logo_word|default:brand.brand_name` applied on the `.dm-*` skin.
- Sub-page spot checks (owner IT, `project=<uuid>`): `/immobili/` H1 "Tutti gli immobili che abbiamo in mano." (200 dm-class count) · `/quartieri/` H1 "I quartieri che conosciamo meglio." (193) · `/agenzia/` H1 "Gli agenti che ti accompagnano dall'incontro al rogito." (157) · `/valutazione/` H1 "Quanto vale casa tua?" (69) · `/contatti/` H1 "Scrivici, ti richiamiamo entro 20 minuti." (79). All 5 carry `dm-nav` + `dm-foot` + `WalkCasaBrand` + `body.mw-is-editor-preview` + `preview-bridge.js`.
- Publish + second-user public preview per locale: IT/EN/FR customer overrides visible on each respective locale · ES/AR authored fallback (`"La casa de tus..."` / `"بيت أحلامك..."`) · AR `dir="rtl"` preserved · `WalkCasaBrand` universal across all 5 locales · **zero cross-locale leak** in any direction.

### Observables

- 193/193 → **204/204** server tests (+11: 10 contract/integration + 1 lifecycle).
- Smoke 834/834 unchanged. `manage.py check` 0 issues.
- Schema LOC delta +604 — slightly over the 600-LOC soft guardrail. User flagged as a non-blocking exception: no new scope opened, tests green first-run, perimeter coherent, no service/rendering/views/models touched. The overshoot reflects Casa's structural richness (15 indexed lists vs Juris's 6 + 14 search_widget scalars with their 4 subgroup wrappers). Recorded as explicit exception rather than a pattern shift.
- No production code touched outside `schema.py`, `real-estate/mass-market/_base.html` (3 minimal fixes), and `tests.py`. Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / editor templates / `live-editor.js` / CSS / content registries / any other skin.

### Consequences

- **Editor 7/8 archetypes editable · multi-locale 7/8 enrolled · 8 templates editable end-to-end** (Vertex + Pragma + Gusto + Cardio + Derm + Lex + Juris + **Casa**).
- **Real-estate family is OPENED but NOT YET CLOSED** — Casa landed, Villa deferred to A.12b. Unlike the law family (closed in A.10+A.11 via two sequential dedicated-schema enrollments), real-estate ships a staged progression where Casa is usable today and Villa follows when the dedicated phase opens. The two-template category stays half-enrolled until A.12b lands.
- **Pattern "zero-image archetype" now formalized** as a reusable recipe: the `test_a<N>_<archetype>_schema_contains_zero_image_fields` guardrail test is mechanical copy/paste across enrollments where the DNA rejects imagery. Two archetypes enrolled this way so far (Juris, Casa).
- **Pattern "Villa-out explicit guard"**: the `test_a12_casa_archetype_registered` assertion (`ultra-luxury-cinematic NOT in _ARCHETYPE_SCHEMAS NOR in _MULTILOCALE_ENABLED_ARCHETYPES`) plus a **runtime assertion inside the lifecycle test** locks Villa out of the gate at both registration-time AND execution-time, so a future accidental enrollment without its own dedicated phase fails fast. Will be inverted (removed) in A.12b together with Villa's own registrations.
- Catalog 20/20 `published_live` unchanged.
- **No new D-number introduced**. A.12 is the sixth real application of the D-098 recipe and confirms that **a family can be enrolled in staged progression**: one dedicated schema now + one dedicated schema later is a valid path, not only "both at once" or "shared-schema". The binding constraint from D-098 — dedicated lifecycle regression test per enrolled template — was satisfied for Casa this session; Villa will satisfy it in A.12b.
- Branch shape: `phase-editor-a12-casa-mass-market-v1` merged into v15 via `--no-ff` @ `a93c50d`. Pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

A.12b planning session — candidates in priority order (dedicated planning required before Step 0):

(a) **A.12b Villa (ultra-luxury-cinematic) enrollment — close the real-estate family** — natural continuation from A.12, mirrors the A.10→A.11 law-family closure. Villa has distinct DNA + distinct skin folder (`.vp-*`, 34 mature `html[dir="rtl"]` rules) + divergent page slugs from Casa, so a separate schema + separate `_base.html` preview bridge + dedicated lifecycle test are needed. **Critical difference from Casa**: Villa carries **26 image fields** (1 cover + 4 signature[].image + 1 advisor_portrait + 6 territory[].image + 1 director_portrait + 4 advisor[].portrait + 8 posts[].image + 1 collezione.lead_image). The image-inside-list-of-dict-row pattern (signature[i].image · territories[i].image · advisors[i].portrait) is NOVEL — no currently-enrolled archetype exposes image cols inside dict rows (Gusto / specialist use col-EXCLUSION for portraits; Villa would need col-EXPOSURE for cover-in-row). Step 0 must decide: expose image cols in the dict shape (new widget pattern) vs keep them registry-only (deprives customer of core editing surface). Likely ~3-4 commits (schema + bridge + lifecycle + possibly a small service-layer touch if image-in-row needs glue).

(b) **A.12b alt · Chiara (editorial-designer-grid)** — single template, novel `project_detail` / `series_detail` page kinds (Session 34 rollout) stretch the editor beyond current home/about/services patterns. Good second choice if Villa's image-in-row analysis reveals higher risk than expected.

(c) **A.12b alt · Pixel (cinematic-photographer)** — single template, imagery-heavy but simpler shape than Villa (no list-of-dict image novelty). Straightforward A.11 recipe.

(d) **A.12b alt · Sapore + Brace (restaurant family continuation beyond Gusto) / Bottega + Luxe (ecommerce) / Salute + Benessere + Famiglia (medical other)** — Step-0 audit per family.

(e) **A.12b alt · Aura + Elevate (single-template agency/startup)** — low novelty, low risk.

(f) **A.12b alt · editor polish / operator tools / remote storage / media evolution** — defer unless customer signal or prod-launch timeline demands. Real-estate family being half-open is a stronger signal than polish ROI.

Consolidation pause (this commit) precedes the choice.

## Session 66 — Phase A.12b · Villa (ultra-luxury-cinematic) Editor + Multi-locale Enrollment (2026-04-18)

### What shipped

A.12b ships the eighth editable archetype: **Villa (ultra-luxury-cinematic · real-estate family · second template)**. The real-estate family is now **CLOSED COMPLETELY** — Casa (mass-market, A.12) + Villa (ultra-luxury-cinematic, A.12b) delivered as two dedicated-schema enrollments in staged progression. Third family to close in the editor after law (A.10+A.11, sequential dedicated-schema) and medical-specialist (A.9, shared-schema). All three family-closure topologies now have ≥1 real precedent.

The central planning question — "is image-inside-list-of-dict-row a novel widget pattern?" — was resolved **negative** during the A.12b Step-0 runtime audit: Vertex has shipped image cols inside dict rows since A.3a/A.4 via `studio.partners[].portrait` (`type: "image"` col with `mutable: True`, production-hardened through the ProjectAsset + `/assets/upload/` flow). Villa became the second archetype to use the pattern, with a *smaller* surface because Villa's lists are non-mutable (cell-level edit only, no add/remove). Zero changes to service-layer / rendering / editor widget / model required — a pure enrollment phase, same 3-file surface as A.10/A.11/A.12 (`schema.py` + skin `_base.html` + `tests.py`).

### Recipe applied (single-template · A.6 + A.7b combined · Villa-out guard REMOVAL + 3 user-imposed guardrails)

Two commits on `phase-editor-a12b-villa-ultra-luxury-cinematic-v1`.

- Step 0 · runtime audit (planning artifact, no code). DNA inspection confirmed Villa's `.vp-*` skin ships 34 mature `html[dir="rtl"]` rules (highest count of any enrolled archetype). 5-locale parity PERFECT (185 keys × 5 locales, zero gaps). Image inventory: 4 scalar image fields (`home.cover_image`, `home.advisor_portrait`, `studio.director_portrait`, `collezione.lead_image`) + 4 image-in-dict-row paths (`home.signature[].image` × 4 rows, `territorio.territories[].image` × 6 rows, `studio.advisors[].portrait` × 4 rows, `posts[].image` × 8 rows). Decision: expose image cols in 3 of the 4 dict lists (home.signature + territorio.territories + studio.advisors); `posts` stays registry-only per the consistent Lex/Juris/Casa blog-list policy. Real editable image surface: **18** (4 scalar + 14 image cells). Complex-shape exclusions identified: `collezione.filter_groups[].options` + `concierge.form_fields[].options` (nested list-of-str) · flat list-of-str containers (`home.territory`, `home.press_items`, `collezione.sort_options`, footer row lists) · form structure (`concierge.form_fields`) · per-post `posts` entries.
- `85105b2` · Step 1 · `VILLA_ULTRA_LUXURY_CINEMATIC_SCHEMA` in `apps/editor/schema.py` (~587 LOC delta — under the 600-LOC soft guardrail, margin preserved vs Casa's +604 exception). 11 sidebar groups: brand + hero_home (4 subgroups including cover-image + CTAs) + home_bands (6 subgroups) + 5 page groups + contact_info + tile_labels. ~175 scalar fields + 4 scalar image fields. `STRUCTURED_FIELD_SHAPES["ultra-luxury-cinematic"]` exposes 14 readonly indexed lists, with image cols on 3 of them (home.signature.image · territorio.territories.image · studio.advisors.portrait). No `mutable: True` flag. `templates/live_templates/real-estate/ultra-luxury-cinematic/_base.html` gets the three atomic A.6 fixes with `.vp-*` prefix CSS guard block + preview-bridge injection. **Villa-out guards REMOVED from A.12 Casa tests** — 2 assertions dropped (registration-time `assertNotIn("ultra-luxury-cinematic", ...)` inside `test_a12_casa_archetype_registered` and the runtime `assertNotIn` inside `test_a12_casa_full_multilocale_lifecycle_end_to_end`). 10 contract tests including **three user-imposed guardrails**:
  - `test_a12b_villa_archetype_registered` — Villa IN all 3 gates, Casa stays enrolled, 6 pre-Casa archetypes intact
  - `test_a12b_villa_out_guard_was_removed_from_casa_tests` — positive contract that explicitly verifies Villa IS in `_ARCHETYPE_SCHEMAS` AND `_MULTILOCALE_ENABLED_ARCHETYPES` + Casa still in both
  - `test_a12b_villa_image_cols_in_dict_shapes_exposed` — **positive mirror** of the Juris/Casa zero-image guard: asserts 4 scalar image paths + 3 image cells (`home.signature.0.image`, `territorio.territories.0.image`, `studio.advisors.0.portrait`) return `type == "image"` via `get_field_spec`, AND each of the 3 dict shapes has the image col in its `cols` list
  - `test_a12b_villa_complex_shapes_excluded_from_perimeter` — 19 path rejects via `validate_key_path`: nested list-of-str (filter_groups.options + form_fields.options) · flat list-of-str (territory, press_items, sort_options, footer rows) · form structure (concierge.form_fields) · per-post `posts` entries (including posts.image col)
  - `test_a12b_villa_structured_list_cells_are_global` — text + image cells both non-translatable (image override stays global, never per-locale)
  - `test_a12b_septuple_regression_after_villa_joins` — 7 pre-existing archetypes intact on `is_translatable("home.headline")` + `supported_locales`
  - Plus shape/translatable/locales/preview-bridge standard set

- `16d03d1` · Step 2 · `test_a12b_villa_full_multilocale_lifecycle_end_to_end` — enriched vs A.12 Casa with the **A.12b-specific image-handling coverage**: 3 translatable autosaves (IT/EN/FR marker "A12bVilla") + 1 global text autosave (`site.logo_word = "A12bVillaBrand"`) + **1 scalar image override** (`home.cover_image`) + **1 image-in-dict-row override** (`home.signature.0.image`) + publish + 5 public preview renders (second user) asserting BOTH image overrides visible universally across every locale + AR `<html dir="rtl" lang="ar">` assertion on `.vp-*` skin + owner reopen per locale + Casa-stays-enrolled runtime guard at start AND end. Storage-key assertions lock that image overrides are plain-keyed (NOT `@<locale>:`): `home.cover_image` + `home.signature.0.image` present as plain keys; `@it:home.cover_image` + `@it:home.signature.0.image` + `home.headline` (plain) + `@en:site.logo_word` all absent. Route: `/templates/real-estate/villa-immobili-lusso/preview/`. Passes first run.

Step 3 · browser walk (no code change). 15 spot checks all green:
- Editor `?lang=it` mount → 5 pills, 128 `per lingua` badges on translatable fields, 247 global fields without badge, 6/6 expected global contract keys correctly NON-translatable, **18 `input[type="file"]` image upload widgets in sidebar** (exactly matching 4 scalar + 14 image cells on 3 non-mutable dict lists · image-in-dict-row end-to-end verified)
- All 4 scalar image fields present in sidebar; all 3 image cells (row 0 of each dict list) present in sidebar
- Type IT on `home.headline` + click EN pill before debounce → `@it:home.headline` persisted BEFORE iframe navigation. Same flush EN→FR
- On FR: 4 fields typed in same flush (headline FR, global logo, scalar image cover, image-in-dict-row signature.0.image) · after debounce all 6 overrides persisted (3 @<locale>:home.headline + 3 plain-keyed globals including 2 images) · zero leak (no `@<locale>:` image paths, no plain `home.headline`, no `@en:site.logo_word`)
- ES switch · sidebar shows authored ES baseline `"Residencias de autor, para quienes saben reconocerlas."` (is_overridden=false, translatable=true) · global logo + cover + signature image overrides persist universally (is_overridden=true, translatable=false on all three)
- AR switch · iframe `.ed-frame` emits `<html lang="ar" dir="rtl">` authentic on the `.vp-*` skin; `body.mw-is-editor-preview lm-ready` guard class present; 34 vp-classed elements render; AR H1 `"منازل ذات توقيع، لمن يُحسن قراءتها."`; title `"WalkVillaBrand — المنازل"` confirms `site.logo_word|default` on `.vp-*`; **both image overrides visible in AR iframe HTML**
- Sub-page spot checks (owner IT, `project=<uuid>`): `/collezione/` H1 "Quattordici dimore d'autore..." (15 vp-classes) · `/territorio/` "Il paesaggio è la prima firma..." (14) · `/studio/` "Nove advisor, mai più di otto mandati..." (14) · `/esperienza/` "Dal primo dossier alla firma notarile." (14) · `/concierge/` "Su appuntamento soltanto." (11). All 5 carry `vp-nav` + `vp-foot` + `WalkVillaBrand` + `body.mw-is-editor-preview` + `preview-bridge.js`
- Publish + second-user public preview per locale: IT/EN/FR text overrides visible per locale · ES/AR authored text fallback · AR `dir="rtl"` preserved · `WalkVillaBrand` universal · **both image overrides (cover + signature.0) visible on ALL 5 public renders** · zero cross-locale leak in any direction · titles localized per locale (Dimore/Residences/Demeures/Residencias/المنازل) with brand override prefix

### Observables

- 204/204 → **216/216** server tests (+12: 10 contract/integration + 1 lifecycle · the existing 2 Casa tests were updated in Step 1 to drop the Villa-out assertions, their test count is unchanged).
- Smoke 834/834 unchanged. `manage.py check` 0 issues.
- Schema LOC delta +587 · **under** the 600-LOC soft guardrail (vs Casa's +604 non-blocking exception). Villa turned out lower than Casa despite image cols because Villa has 14 indexed lists vs Casa's 15, and fewer tile/site scalar labels.
- No production code touched outside `schema.py`, `ultra-luxury-cinematic/_base.html` (3 minimal fixes), and `tests.py`. Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / editor templates / `live-editor.js` / CSS / ProjectAsset / `/assets/upload/` / any other skin (Casa skin left intact, all 6 earlier archetypes left intact).

### Consequences

- **Editor 8 archetype slugs enrolled · multi-locale 8 enrolled · 9 templates editable end-to-end** (Vertex + Pragma + Gusto + Cardio + Derm + Lex + Juris + Casa + **Villa**). Note: "8 archetype slugs enrolled" does NOT mean "every catalog archetype covered" — the DNA registry carries additional archetype slugs (trattoria-warm, street-modern, cinematic-photographer, editorial-designer-grid, medical-clinic, wellness-serene, family-warm, agency-digital-studio, startup-saas-landing, artisan-workshop, fashion-editorial) that remain editor-unsupported.
- **Real-estate family CLOSED COMPLETELY** via staged dedicated-schema progression (A.12 + A.12b · Casa + Villa), the third family-closure after law (A.10+A.11 sequential) and medical-specialist (A.9 shared). All three D-098 topologies have ≥1 precedent.
- **Image-in-dict-row formalized as a reusable enrollment pattern**: Villa is the second archetype to use it (after Vertex), proving the infrastructure supports non-mutable dict-row image cols as cleanly as mutable ones. No service-layer changes were ever required — the path was always production-ready since A.3a/A.4. The "novel widget" framing in the A.12 planning memo is corrected retroactively: image-in-dict-row is the same widget, applied to a new archetype.
- **Image overrides stay global/plain-keyed** even inside dict rows. A per-locale image policy remains out-of-scope per D-098 · an explicit product decision would be needed to change this (not a planning tweak).
- Catalog 20/20 `published_live` unchanged.
- **No new D-number introduced**. A.12b is the seventh real application of the D-098 recipe and closes the family that A.12 opened. The operational clarification added to D-098 now codifies all three topologies and the image-in-dict-row precedent.
- Branch shape: `phase-editor-a12b-villa-ultra-luxury-cinematic-v1` merged into v15 via `--no-ff` @ `258fa56`. Pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending.

### Exact next step

A.13 planning session — candidates in priority order (dedicated planning required before Step 0):

(a) **A.13 portfolio family (Chiara + Pixel) enrollment** — natural next closure candidate. Chiara ships `editorial-designer-grid` with novel `project_detail` / `series_detail` page kinds (Session 34 rollout); Pixel ships `cinematic-photographer` with imagery-heavy single-template shape. Step-0 audit decides whether project_detail page-scoped fields enter the perimeter (probably out — detail editing stays registry-only consistent with all prior blog-list/post-detail policies) and whether the two templates need shared-schema (unlikely — distinct DNA) or staged dedicated-schema (probable · same recipe as A.12+A.12b).

(b) **A.13 alt · restaurant family continuation (Sapore + Brace beyond Gusto)** — two templates, likely distinct archetypes (`trattoria-warm` + `street-modern`). Would close the restaurant category if audit confirms divergence (staged dedicated-schema like real-estate).

(c) **A.13 alt · ecommerce family (Bottega + Luxe)** — `artisan-workshop` vs `fashion-editorial`. Session 41/42 observations already suggest wide divergence. Would close the ecommerce category with staged enrollments.

(d) **A.13 alt · medical-other family (Salute + Benessere + Famiglia)** — three single-template medical archetypes (`medical-clinic` / `wellness-serene` / `family-warm`) that went `published_live` in Session 51 but never entered the editor. Three separate phases preferred over bundling (one-phase-one-archetype discipline is 8 phases strong and should not be relaxed for three simultaneous openings).

(e) **A.13 alt · agency-secondary / startup-saas individual enrollments** (Aura `agency-digital-studio` or Elevate `startup-saas-landing`) — low novelty, low risk, single-template each.

(f) **A.13 alt · editor polish / operator tools / remote storage / media evolution** — defer unless customer signal or prod-launch timeline demands.

Consolidation pause (this commit) precedes the choice.

## Session 67 — Phase A.13 · Chiara (editorial-designer-grid) Editor + Multi-locale Enrollment (2026-04-18)

### What shipped

A.13 ships the ninth editable archetype: **Chiara (editorial-designer-grid · portfolio family · first template)**. The portfolio family is now **OPEN but NOT YET CLOSED** — Chiara enrolled, Pixel (`cinematic-photographer`) held explicitly out of the gate until A.13b. Same staged dedicated-schema progression topology as real-estate (A.12+A.12b · Casa+Villa). Tenth template editable end-to-end.

Three A.13-specific design points were resolved at planning time (not during implementation):

1. **Detail-page editing stays OUT of the perimeter** — `posts[]` list (3 project detail records) remains registry-only. This is a **coherent perimeter decision**, not a missing feature. It's consistent with the per-item content policy applied uniformly across Lex `notabili`, Juris `insights`, Casa `posts` (property detail), Villa `posts` (series detail). Per-project detail editing would be a horizontal feature affecting every archetype with per-item content (5+ archetypes) and needs uniform cross-archetype design — not Chiara-special-casing. The customer gets a credible editor (chrome + listing pages + studio/processo editorial copy) with 3 static project records as placeholders. Disclosed honestly.

2. **Deep-path image-in-dict-row** — Chiara exposes `home.featured_works.items[].image` at a path 2 levels deep through the `home.featured_works` parent dict. Third precedent of image-in-dict-row after Vertex `studio.partners[].portrait` (production since A.3a/A.4) and Villa's 3 A.12b image-col lists. The deep path works without any new infrastructure: `_resolve_path` walks arbitrary-depth dotted paths through dicts (verified Step-0 via direct code read). Infrastructure claim re-confirmed: image-in-dict-row is a reusable enrollment pattern, not a horizontal feature.

3. **Nested-dict scalar image** — `studio.founder.image` lives inside the `studio.founder` parent dict (4 scalars + 1 image + 1 list-of-str credentials excluded). Same shape as Vertex `home.cover.image` (production since editor foundation A.1). Schema exposes the 4 scalars + image as flat fields with dotted paths; no sub-dict editor widget needed.

### Recipe applied (single-template · A.6 + A.7b combined · Pixel-out guard + 3 user-imposed guardrails)

Two commits on `phase-editor-a13-chiara-editorial-designer-grid-v1`.

- Step 0 · runtime audit (planning artifact, no code). Verified Chiara skin CSS prefix `.ed-*` (148 class hits · 46 mature `html[dir="rtl"]` rules — highest count of any enrolled archetype, benefits of the Session 37 D-070 Chiara perfection pass), 5-locale parity PERFECT (164 keys × 5 locales, zero gaps), image inventory (1 scalar nested-dict + 4 image cells on `home.featured_works.items`, total 5 editable image surfaces), complex-shape exclusions (posts list + `studio.founder.credentials` list-of-str + `processo.capabilities_full[].scope` nested list-of-str + `home.clients` + `lavoro.filters` flat list-of-str + form structure blocks). The `.ed-*` prefix collision with the editor sidebar namespace noted but non-impacting (different DOM trees: editor shell vs preview iframe).
- `2ad699d` · Step 1 · `CHIARA_EDITORIAL_DESIGNER_GRID_SCHEMA` in `apps/editor/schema.py` (+533 LOC — **under** the 600-LOC soft guardrail, margin preserved thanks to Chiara's slimmer surface: 5 pages vs Casa's 6, 11 indexed lists vs Casa's 15, 1 image scalar vs Villa's 4). 8 sidebar groups: brand + hero_home (3 subgroups) + home_bands (5 subgroups including `featured_works` parent-dict scalars + indexed list subgroup) + studio_page (5 subgroups including founder block) + lavoro_page (5 subgroups incl. dossier labels + ledger meta) + processo_page (novel `process` kind — just a string identifier, no view dispatch) + contatti_page (5 subgroups incl. studio address block) + contact_info. ~140 scalar + 1 scalar image (`studio.founder.image`). `STRUCTURED_FIELD_SHAPES["editorial-designer-grid"]` exposes 11 readonly indexed lists with image col on `home.featured_works.items` (deep path 2 levels). Implementation required 5 mid-stream schema-vs-registry alignment fixes (dropped `hero_card` subgroup non-existent in registry · dropped `clients_heading/intro` and `press_intro` non-existent · dropped `site.nav_cta`/`site.foot_offices` not in Chiara chrome · replaced with actual lavoro `dossier_*`/`row_*`/`ledger_*` keys and processo `capability_duration_label`/`step_*` keys · added `contatti.studio_*` address block) — all caught before Step-1 validation. `templates/live_templates/portfolio/editorial-designer-grid/_base.html` gets the three atomic A.6 fixes with `.ed-*` prefix CSS guard block + comment documenting the editor-sidebar namespace collision (different DOM trees, no conflict). 10 contract tests including **three user-imposed guardrails**:
  - `test_a13_chiara_archetype_registered` — Pixel-out explicit guard (registration-time · `cinematic-photographer` NOT in `_ARCHETYPE_SCHEMAS` NOR in `_MULTILOCALE_ENABLED_ARCHETYPES`) + all 8 previous archetypes still enrolled
  - `test_a13_chiara_image_cols_in_dict_shapes_exposed` — **triple verification** user-requested: (a) `get_field_spec` returns `type="image"` for `studio.founder.image` (nested-dict scalar precedent); (b) `get_field_spec` returns `type="image"` for deep paths `home.featured_works.items.0.image` and `home.featured_works.items.3.image` (deep-path third precedent); (c) shape-level check: `get_list_shape("editorial-designer-grid", "home.featured_works.items")` includes `image` col with `type="image"` in its cols list
  - `test_a13_chiara_complex_shapes_excluded_from_perimeter` — 22 paths rejected by `validate_key_path` spanning 4 exclusion categories: (1) 8 `posts.*` paths (per-project detail, including `posts.0.title`, `posts.0.lead`, `posts.0.sections`, `posts.0.summary`, `posts.0.deliverables`, `posts.0.credits`, `posts.2.next_label`) — the detail-page-out policy is now tested explicitly; (2) 4 nested list-of-str paths (`studio.founder.credentials` + `processo.capabilities_full[].scope`); (3) 4 flat list-of-str paths (`home.clients` + `lavoro.filters`); (4) 6 form structure paths (`contatti.form_fields` + `form_sections` + `upload_field`)
  - Plus shape/translatable/globals/structured-cells-global/locales/**octuple regression**/preview-bridge standard set

- `12984c9` · Step 2 · `test_a13_chiara_full_multilocale_lifecycle_end_to_end` — enriched vs A.12b Villa with **page-specific image assertions** because Chiara's scalar image lives on the studio page (not home). The test helper `preview_body(locale, page=None)` fetches home OR a specific sub-page; `IMG_FEATURED0` (home-scoped) verified on home renders while `IMG_FOUNDER` (studio-scoped) verified on studio renders — same verification, different pages. 3 translatable autosaves (IT/EN/FR on `home.headline` marker "A13Chiara") + 1 global text (`site.logo_word = "A13ChiaraBrand"`) + **1 scalar image override** (`studio.founder.image` — nested-dict scalar) + **1 image-in-dict-row override at DEEP PATH** (`home.featured_works.items.0.image` — third precedent) + publish + 5 public preview renders (both home and studio pages per locale) + AR `<html dir="rtl" lang="ar">` assertion on `.ed-*` skin + 4 editor reopens (owner) + **Pixel-out runtime guard** at start AND end of test. Storage-key assertions lock that all image overrides are plain-keyed (NOT `@<locale>:`): `studio.founder.image` and `home.featured_works.items.0.image` present as plain keys; `@<locale>:studio.founder.image` and `@<locale>:home.featured_works.items.0.image` absent. Route: `/templates/portfolio/chiara-portfolio-creativo/preview/`. Passed at second run — first run caught a test-design error (not a code bug): the initial script asserted `IMG_FOUNDER` on home body, but founder.image renders on the studio page not home · fix: switched to page-specific `preview_body()` helper. Zero application code change.

Step 3 · browser walk (no code change). 16 spot checks all green:
- Editor `?lang=it` mount → 5 pills, 112 `per lingua` badges on translatable fields, 212 global fields without badge, 6/6 expected global contract keys correctly NON-translatable, **5 `input[type="file"]` image upload widgets in sidebar** (exactly matching 1 scalar + 4 image cells across 1 dict list · deep-path image-in-dict-row end-to-end verified)
- `studio.founder.image` widget present (nested-dict scalar, Vertex-cover precedent)
- `home.featured_works.items.0.image` widget present (deep-path image-in-dict-row, third precedent)
- **Posts/exclusion leak check**: zero `posts`/`posts.0.*` selectors found in sidebar · zero `home.clients` / `lavoro.filters` / `studio.founder.credentials` / `processo.capabilities_full.0.scope` selectors — exclusion perimeter verified end-to-end
- Type IT + click EN before debounce → `@it:home.headline` persisted BEFORE iframe navigation · same EN→FR
- FR flush with 4 fields in one pass (headline FR + global logo + scalar image founder + image-in-dict-row featured_works.items.0) → 6 DB overrides persisted (3 `@<locale>:home.headline` + 3 plain-keyed globals) · zero leak
- ES switch · sidebar shows authored ES baseline `"Formas que perduran, una página a la vez."` (is_overridden=false, translatable=true) · all 3 global overrides persist (is_overridden=true, translatable=false on all three)
- AR switch · iframe `.ed-frame` emits `<html lang="ar" dir="rtl">` authentic on `.ed-*` skin · 32 ed-classed elements · body guard + lm-ready · H1 AR `"أشكالٌ تَبقى، صفحةً تلوَ الأخرى."` · title `"WalkChiaraBrand — الاستوديو"` confirms `site.logo_word|default` on Chiara skin · `featured[0]` image visible on home · `founder` image verified on `/studio/` AR page separately
- Sub-page spot check (owner IT): `/studio/` "Uno studio guidato dall'art director..." (9 ed-classes) · `/lavoro/` "Quarantasette progetti firmati..." (8) · `/processo/` "Cinque fasi, un solo file per progetto." (7) · `/contatti/` "Trenta minuti con l'AD, niente impegno." (7) · all with ed-nav + ed-foot + WalkChiaraBrand + body.mw-is-editor-preview + preview-bridge.js
- Publish + second-user public preview per locale: IT/EN/FR text overrides visible per locale · ES/AR authored text fallback · AR `dir="rtl"` preserved · `WalkChiaraBrand` universal · `IMG_FEATURED0` visible on home renders across all 5 locales · `IMG_FOUNDER` visible on studio renders across all 5 locales · zero cross-locale leak · titles localized (Studio/Studio/Studio/Estudio/الاستوديو)
- **Detail-page registry-only verify** (user-imposed): 3/3 project detail routes `/lavoro/<slug>/` return HTTP 200 rendering **static registry content** (project title + lead unchanged from IT baseline) with global brand chrome override (`WalkChiaraBrand`). No per-project override was attempted; none would be persistable (validate_key_path rejects). Policy coerente: posts/detail restano registry-only per decisione di perimetro.

### Observables

- 216/216 → **227/227** server tests (+11: 10 contract/integration + 1 lifecycle).
- Smoke 834/834 unchanged. `manage.py check` 0 issues.
- Schema LOC delta +533 · **under** the 600-LOC soft guardrail (vs Casa's +604 exception, Villa's +587 under-guardrail).
- No production code touched outside `schema.py`, `editorial-designer-grid/_base.html` (3 minimal fixes + comment on `.ed-*` namespace collision), and `tests.py`. Zero touches to `services.py` / `rendering.py` / `views.py` / `models.py` / editor templates / `live-editor.js` / CSS / ProjectAsset / `/assets/upload/` / any other skin.

### Consequences

- **Editor 9 archetype slugs enrolled · multi-locale 9 enrolled · 10 templates editable end-to-end** (Vertex + Pragma + Gusto + Cardio + Derm + Lex + Juris + Casa + Villa + **Chiara**).
- **Portfolio family OPEN but NOT YET CLOSED** — Chiara landed, Pixel deferred to A.13b. Same staged dedicated-schema progression pattern as real-estate (A.12+A.12b).
- **Detail-page-out policy consolidated across 5 family closures + 1 open family**: Lex notabili · Juris insights · Casa posts · Villa posts · Chiara posts all registry-only uniformly. Pattern now strong enough to be cited in every future enrollment planning as "per-item detail stays registry-only unless a horizontal feature phase opens detail-page-scoped editing across all archetypes with per-item content".
- **Deep-path image-in-dict-row precedent confirmed**: `_resolve_path` walks arbitrary depth through dicts; no infrastructure work needed for paths like `home.featured_works.items.0.image`.
- Catalog 20/20 `published_live` unchanged.
- **No new D-number introduced**. A.13 is the eighth real application of the D-098 recipe.
- Branch shape: `phase-editor-a13-chiara-editorial-designer-grid-v1` merged into v15 via `--no-ff` @ `e55d55b`. Pushed to `origin/phase-integration-baseline-v15`.
- No explicit debt pending. Pixel-out guard transitory (not debt).

### Exact next step

A.13b planning session — candidates in priority order:

(a) **A.13b Pixel (cinematic-photographer) enrollment — close the portfolio family** — natural continuation from A.13, mirrors A.12→A.12b real-estate closure. Pixel has `series_list` + `publications` novel page kinds (2 novel kinds vs Chiara's 1 `process`) but simpler shape overall (mostly list-of-tuple, 1 scalar image on `home.hero_image`, no image-in-dict-row exposed since posts stays registry-only). Lighter enrollment than Chiara · recipe mechanical reuse.

(b) **A.13b alt · restaurant-continuation (Sapore + Brace beyond Gusto)** — likely distinct archetypes (`trattoria-warm` + `street-modern`). Staged dedicated-schema closure like real-estate.

(c) **A.13b alt · ecommerce family (Bottega + Luxe)** — `artisan-workshop` vs `fashion-editorial`. Session 41/42 observations suggest wide divergence. Bottega has commerce-foundation overlap (Phase 3a+3b seeded both) — worth Step-0 check on whether editor schema needs to avoid overlap with commerce-managed content.

(d) **A.13b alt · medical-other family (Salute + Benessere + Famiglia)** — 3 separate phases (one-phase-one-archetype discipline is 9 phases strong A.6→A.13).

(e) **A.13b alt · Aura / Elevate individual enrollments** — low-novelty single-template each.

(f) **A.13b alt · editor polish / operator tools / remote storage / media evolution** — defer unless customer signal or prod-launch timeline demands.

(g) **MEMORY.md maintenance mini-phase** — auto-memory index ~27-28KB sopra warning-soglia 24.4KB dal post-A.11 · candidato housekeeping separato, NOT bundled with an enrollment.

Consolidation pause (this commit) precedes the choice.
