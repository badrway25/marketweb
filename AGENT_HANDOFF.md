# Agent Handoff

Last updated: 2026-04-19 — after **Session 74 A.16b Benessere (wellness · medical-other family · second template · MIDDLE PHASE) Editor + Multi-locale Enrollment merge** (baseline tip `e9cc419`, pushed to origin)

## Current state — read this before opening any new workstream (2026-04-19)

**Sixteen archetype slugs enrolled** — Vertex (`agency-creative-studio`) + Pragma (`corporate-suite`) + Gusto (`fine-dining`) + **specialist** (Cardio + Derm shared) + **classic-gold** (Lex) + **modern-transparent** (Juris) + **mass-market** (Casa) + **ultra-luxury-cinematic** (Villa) + **editorial-designer-grid** (Chiara) + **cinematic-photographer** (Pixel) + **trattoria-warm** (Sapore) + **street-modern** (Brace) + **artisan-workshop** (Bottega) + **fashion-editorial** (Luxe) + **clinic** (Salute) + **wellness** (Benessere) — all multi-locale enrolled. **17 templates editable end-to-end.** A.16b Benessere enters as MIDDLE phase of the medical-other 3-phase staged dedicated-schema progression (A.16 Salute opener · A.16b Benessere middle · **A.16c Famiglia closer pending**). Wellness-out guard half of the DUAL-OUT GUARD planted in A.16 Salute was removed symmetrically (5th precedent of guard removal pattern) · family-out guard PRESERVED unchanged for A.16c closer. **Six families editor-complete**: law (A.10+A.11 sequential dedicated-schema) · medical-specialist (A.9 shared-schema) · real-estate (A.12+A.12b staged dedicated-schema) · portfolio (A.13+A.13b staged dedicated-schema) · restaurant-continuation (A.14+A.14b staged dedicated-schema) · ecommerce (A.15+A.15b staged dedicated-schema). **Medical-other family STILL HALF-OPEN** (Salute + Benessere IN · Famiglia pending A.16c).

A.16b validates three critical framings:

1. **Guard removal sub-recipe extended from 1-removal (2-phase) to 2-removal (3-phase) phase**. Previous 4 guard removal precedents (Villa/Pixel/Brace/Luxe) all applied to 2-phase staged progressions where 1 opener planted 1 guard and 1 closer removed it. A.16 Salute planted 2 guards (wellness-out + family-out) in a 3-phase progression · A.16b removes wellness-out symmetrically via `test_a16b_benessere_out_guard_was_removed_from_salute_tests` while family-out guard is PRESERVED unchanged at all 3 layers · A.16c will remove family-out via 6th precedent. **First time 1 opener plants 2 guards and each closure phase removes 1** — sub-recipe generalizes from "one-opener-one-closer" (A.12→A.12b topology) to "one-opener-two-closers" (A.16→A.16b→A.16c topology). D-098 invariant preserved throughout.

2. **Scheduler-state bool flags + nested list-of-str uniformly OUT across 2 calendar lists**. Benessere ships `home.calendar` + `prenota.calendar` (both 7 rows × 6 cols) as identical shape · both calendars share `day`/`num`/`month` IN (editorial visible labels) and `has_slots`/`soldout`/`slots` OUT (scheduler-state-like). 4 bool flag cols (2 lists × 2 cols) OUT col-level per Luxe `available` + Salute `is_popular` precedent re-application. 2 nested list-of-str cols (`slots`: concrete time-slots like `['10:00','14:30']`) OUT col-level per Juris precedent. **Scheduler-state is a per-col-type policy category, not a per-archetype special case** — mechanical reuse of 3 prior precedents re-applied to the same content-tree shape twice.

3. **First-ever NOVEL SHAPE DEFERRAL outcome formalized**: `home.ambients` tuple-with-image (4 × `(image_url, title, sub)` · positional tuple with image as first element) discovered during Step 0 audit · **ZERO precedent in any existing archetype** (all prior tuple shapes across 15 enrolled archetypes carry text-only cols). Decision: whole list OUT first-wave via schema omission · mechanical-reuse principle preserved · no horizontal-feature introduction (would be first-ever image-typed cell inside a tuple col requiring runtime verification of 3 editor layers) · 4-tile image coverage loss accepted for middle-phase enrollment · explicit future expansion candidate after dedicated infra verification. **Establishes a 4th deferral category** (novel-shape-deferred) alongside mutable repeater · image per-locale · detail-page editing.

Catalog 20/20 `published_live` unchanged since D-082 / Session 53. Editor footprint: **16 archetype slugs enrolled · 16 multi-locale enrolled · 17 templates editable end-to-end**. Note: "16 enrolled" does NOT mean "every catalog archetype covered" — the DNA registry carries 3 residual slugs (`family`, `agency-digital-studio`, `startup-saas-landing`) that remain editor-unsupported (3 templates across 3 open families · 1 half-open medical-other with Famiglia pending A.16c). All acceptance gates are green:

- `python manage.py check` → 0 issues
- `python manage.py test apps` → **325/325 PASS**
- `python smoke_full.py` → 834/834 routes HTTP 200

Baseline `phase-integration-baseline-v15` tip: **`e9cc419`** (A.16b merge), pushed to `origin/phase-integration-baseline-v15`.

### What the editor does today

**Vertex (`agency-creative-studio`) — multi-locale enrolled:**
- 284 editable fields across 33 accordion groups (14 curated + 18 indexed + 1 design) — 81 translatable, 203 global
- 4 mutable lists with full add / remove / reorder / persistence / preview sync / publish / page-preservation:
  - `studio.facts` (tuple, 1–8 rows) · `studio.partners` (dict, 2–8 rows) · `contatti.channels` (tuple, 1–10 rows) · `studio.timeline_rows` (tuple, 2–10 rows)
- Customer image upload on the 2 image fields (`studio.partners[].portrait` + `home.cover.image`) persisting to `MEDIA_ROOT/project-assets/<project-uuid>/<uuid>.<ext>` — global per D-098
- Page-aware preview navigation · palette Cmd-K search · public `MWEditor.jumpField(key, kind)` API · deterministic field targeting · baseline before/after compare
- **5-locale editing** (it/en/fr/es/ar): sidebar pill strip switches both edit buffer and preview · `@<locale>:<path>` storage per translatable row · global rows universal · authored fallback on untouched locales · RTL iframe for AR · "per lingua" marker UI on translatable fields · `editor_ctx` exposes `active_locale` + `supported_locales`.

**Pragma (`corporate-suite`) — editable AND multi-locale enrolled (A.7b):**
- 7 sidebar groups · ~53 scalars + 1 image · 3 readonly indexed lists (`home.pillars`/`kpi_strip`/`leadership`) · image upload on `home.hero_image`
- 53 translatable fields (out of 92 total sidebar entries) · globals preserve the shared `_GLOBAL_TEXT_PATHS` set (logo, phone, email, address, license) + all image/select/structured-list cells
- `supported_locales=["it","en","fr","es","ar"]` · same UX surface as Vertex (sidebar pill stateful · flush-before-switch · "per lingua" marker · authored-only fallback · RTL iframe authentic for AR)
- Enrolled via A.7b Session 60 (gate flip in `_MULTILOCALE_ENABLED_ARCHETYPES` + lifecycle regression test `test_a7b_pragma_full_multilocale_lifecycle_end_to_end`)

**Gusto (`fine-dining`) — editable AND multi-locale enrolled (A.8):**
- 11 sidebar groups · ~108 scalars + 2 scalar images (`home.ingredienti.image` + `filosofia.filosofia_image`) + 3 readonly indexed lists (`home.signature_courses` tuple 5×4 · `menu.courses` tuple 8×4 · `home.produttori.items` dict 4×4 with `portrait` intentionally NOT in cols so it stays registry-readonly)
- 97 translatable fields (out of 181 total sidebar entries) · `prenota.form_sections` intentionally omitted from schema (IT-only parity gap in registry, skin already has `{% if %}` graceful guard)
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface to Vertex + Pragma. AR preview on `.fd-*` skin renders `<html dir="rtl" lang="ar">` authentic (Arabic nav labels + Arabic H1 + RTL layout)
- Enrolled via A.8 Session 61 (combined A.6 schema register + A.7b gate flip in a single phase · `test_a8_gusto_full_multilocale_lifecycle_end_to_end` + dedicated `test_a8_gusto_preview_bridge_injected_only_with_preview_project` integration test)

**specialist — editable AND multi-locale enrolled (A.9) · FIRST MULTI-TEMPLATE ARCHETYPE:**
- **Shared between 2 templates**: `cardio-studio-specialistico` + `dermatologia-elite-roma`. Both carry `archetype: "specialist"` in their DNA. A.9 Step-0 runtime audit confirmed 95% content-tree parity — 100% on 6/7 pages (studio · visite · medici · pubblicazioni · contatti · richiedi-visita · site) and 85% on home (29 shared keys · 5 Cardio-only + 5 Derm-only premium sections from D-064 Session 30).
- 11 sidebar groups · ~95 shared-core scalar fields + 5 scalar images (`home.chief.portrait` · `studio.studio_image` · `visite.service_image` · `pubblicazioni.lead_image`) + 6 readonly indexed lists (home.facts · home.signature_visits · medici.doctors · studio.history · studio.values · visite.treatments) · the `portrait` column on `medici.doctors` is intentionally NOT in the dict cols so the 3 doctor portraits stay registry-only (same pattern as Gusto produttori.items).
- **Divergent home premium sections kept registry-only**: `anchor_nav`, `insurance`, `location`, `percorso`, `tecnologie` (Cardio-only) and `before_after`, `credentials`, `editorial_feed`, `gallery_strip`, `trattamenti_tabs` (Derm-only). Lock guarded by the dedicated `test_a9_specialist_divergent_premium_sections_excluded` test that enforces exclusion via 4 independent check layers (`is_translatable` False · `validate_key_path` raises · `STRUCTURED_FIELD_SHAPES` absent · sidebar group ids free of divergent hints).
- 77 translatable fields per-template sidebar rendering (out of 171 total sidebar entries including the 6 indexed groups)
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface to Vertex + Pragma + Gusto. AR preview on `.sp-*` skin renders `<html dir="rtl" lang="ar">` authentic.
- Enrolled via A.9 Session 62 (combined A.6 schema register + A.7b gate flip in a single phase, plus **two distinct lifecycle regression tests** — `test_a9_cardio_full_multilocale_lifecycle_end_to_end` + `test_a9_derm_full_multilocale_lifecycle_end_to_end` — confirming the operational clarification to D-098: **shared-schema enrollments still require dedicated lifecycle coverage per template carried in**, there is no "free ride").

**classic-gold (Lex) — editable AND multi-locale enrolled (A.10) · FIRST DEDICATED-SCHEMA SLOT OF THE LAW FAMILY:**
- **Single template**: `lex-studio-legale`. At A.10 time Juris stayed out (guarded by `test_a10_lex_archetype_registered`). At A.11 time Juris was enrolled in its own phase with its own archetype — the Lex guard was updated to drop the Juris-absence assertions while keeping the Lex-must-stay regression guard. Lex and Juris together close the law family via two dedicated schemas (NOT shared-schema).
- 9 sidebar groups · ~102 scalar fields + 1 scalar image (`notabili.lead_image` — only image in Lex registry; lawyers + partners dicts carry no portraits) + 6 readonly indexed lists:
  - `avvocati.lawyers` dict 14×(bio/foro/name/role/specialization/year) — 14 lawyers · all 6 cols exposed · no portrait col to omit
  - `pratiche.services` dict 12×(num/title/blurb/lead/jurisdiction) — 12 practice areas · `scope` nested-list-of-str bullet points intentionally omitted from cols, stays registry-only
  - `pratiche.process` tuple 4×3, `studio.history` tuple 6×3, `studio.values` tuple 4×3, `contatti.offices` dict 2×7 (full: city/tag/address/area/phone/email/hours)
- 79 translatable fields per-template sidebar rendering (distributed across home + studio + pratiche + avvocati + notabili + contatti + site chrome)
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.lx-*` skin renders `<html dir="rtl" lang="ar">` authentic with ledger-style RTL.
- Enrolled via A.10 Session 63 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a10_lex_full_multilocale_lifecycle_end_to_end` as the single dedicated lifecycle regression test).

**modern-transparent (Juris) — editable AND multi-locale enrolled (A.11) · CLOSES LAW FAMILY VIA SECOND DEDICATED-SCHEMA ENROLLMENT · FIRST ZERO-IMAGE ARCHETYPE:**
- **Single template**: `juris-avvocato-moderno`. Distinct archetype from Lex — the two law templates ship distinct DNA + distinct skin folders (`lawyer/classic-gold/` vs `lawyer/modern-transparent/`) and only ~25% content-tree shape overlap. A.9 shared-schema recipe does NOT apply — the law family is closed through two separate enrollments, each with its own schema + skin bridge + lifecycle test. This is the first time a category closes through stacked dedicated-schema enrollments rather than one shared schema (Cardio+Derm specialist pattern).
- 10 sidebar groups · ~180 scalar fields + **ZERO image fields anywhere** (advisory-modern DNA explicitly rejects portraits / case photos / hero illustrations — locked by user-imposed guardrail test `test_a11_juris_schema_contains_zero_image_fields` that iterates the entire schema + `STRUCTURED_FIELD_SHAPES` tree asserting no `type: "image"` field exists) + 6 readonly indexed lists:
  - `approccio.founders` dict 2×(name/role/bio) — 2 managing partners · `credentials` list-of-str col intentionally omitted (stays registry-only)
  - `approccio.story` tuple 5×3 · `approccio.manifesto` tuple 4×3
  - `servizi.services` dict 7×(num/title/tier/blurb/duration/engagement/price) — 7 offers · `deliverables` nested-list-of-str bullet points col intentionally omitted (stays registry-only)
  - `settori.sectors` dict 6×(num/title/tagline/case_snippet/partner/legal_ops) — 6 sectors · THREE nested-list-of-str cols intentionally omitted: `pain_points`, `signals`, `legal_ops`-bullets (all stay registry-only; the SCALAR `partner` + SCALAR `legal_ops`-person cols ARE exposed — the scalar col name collides with the bullets-list key but addresses a different shape per row)
  - `settori.team` dict 10×(name/role/bio/office/email) — 10 people (8 lawyers + 2 legal ops)
- 110 translatable fields + 188 global fields per-template sidebar rendering (walk-verified: `per lingua` badge count = 110 exactly, zero accidentally-translatable globals, zero image widgets in the sidebar)
- **Complex shapes explicitly outside perimeter** (locked by user-imposed guardrail test `test_a11_juris_complex_shapes_excluded_from_perimeter`): `approccio.dashboard_mock` (nested dict with URL + columns + cards) + `home.trust_logos` / `insights.topics` (flat list-of-str marquee / filter pills) + the 4 nested-list-of-str cells listed above. All rejected by `validate_key_path` so scope creep into non-scalar widgets cannot happen silently even via crafted payloads.
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.jr-*` skin renders `<html dir="rtl" lang="ar">` authentic with advisory-modern pill nav and confident-blue CTA ring.
- Enrolled via A.11 Session 64 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a11_juris_full_multilocale_lifecycle_end_to_end` as the single dedicated lifecycle regression test). Confirms D-098 scales to a family-closure topology where the category closes via multiple separate archetype enrollments (not a shared schema).

**mass-market (Casa) — editable AND multi-locale enrolled (A.12) · FIRST DEDICATED-SCHEMA SLOT OF THE REAL-ESTATE FAMILY · SECOND ZERO-IMAGE ARCHETYPE:**
- **Single template**: `casa-agenzia-immobiliare`. Distinct archetype from Villa — the two real-estate templates ship distinct DNA + distinct skin folders (`real-estate/mass-market/` with `.dm-*` prefix vs `real-estate/ultra-luxury-cinematic/` with `.vp-*`) and ~0% non-home page-slug overlap (Casa: home/immobili/quartieri/agenzia/valutazione/contatti vs Villa: home/collezione/territorio/studio/esperienza/concierge — only `home` shared). Shared-schema recipe does NOT apply; real-estate closed in staged dedicated-schema progression (Casa A.12 → Villa A.12b). Third valid D-098 family-progression topology confirmed alongside shared-schema (A.9) and sequential closure (A.10+A.11).
- 10 sidebar groups · ~185 scalar fields + **ZERO image fields anywhere** (mass-market DNA is image-free — the same `test_a12_casa_schema_contains_zero_image_fields` guardrail as Juris ships unchanged, locking the DNA constraint end-to-end) + 15 readonly indexed lists:
  - **home (5 lists)**: `featured_listings` tuple 4×(title/location/price/badge) — 4 cols exposed of 8 tuple positions · `neighborhoods` tuple 6×4 · `stats` tuple 4×3 · `agents_preview` tuple 4×4 · `valuation_proof` tuple 3×2
  - **immobili (1 list)**: `map_cells` tuple 5×2
  - **quartieri (2 lists)**: `guides` tuple 8×(name/tagline/price/inventory/description/agent_note) — 6 cols of 9 (transit/green/tone stay registry-only) · `faq` tuple 4×2
  - **agenzia (2 lists)**: `agents` dict 9×(name/role/area/years/languages/speciality/phone/email/quote) — 9 cols of 10 (`whatsapp_href` stays registry-only) · `facts` tuple 4×3
  - **valutazione (3 lists)**: `how_it_works` tuple 3×3 · `proof` tuple 4×2 · `faq` tuple 4×2
  - **contatti (2 lists)**: `channels` tuple 5×3 · `offices` dict 2×(name/address/metro/hours/phone/email/lead_agent/parking/note) — 9 cols of 13 (whatsapp/whatsapp_href/map_link/map_href stay registry-only)
- **`search_widget` flattened into the `hero_home` group** as 14 scalar fields across 4 subgroups (hero copy · widget intestazione · 4 label+value campi · CTA). `popular_tags` flat list-of-str stays registry-only. This is A.12's only non-trivial design decision vs the A.11 pattern — the nested-dict shape is exposed as scalars, not as a sub-editor, keeping the perimeter consistent.
- 134 translatable fields + 313 global fields per-template sidebar rendering (walk-verified: `per lingua` badge count = 134 exactly, zero accidentally-translatable globals, zero image widgets in the sidebar).
- **Complex shapes explicitly outside perimeter** (locked by user-imposed guardrail test `test_a12_casa_complex_shapes_excluded_from_perimeter`): `home.search_widget.popular_tags` + `immobili.filters` + `immobili.sort_options` (flat list-of-str containers) · `valutazione.form_fields` + `form_sections` + `contatti.form_fields` + `form_sections` (form structure blocks) · `posts` list entries (12 per-property records, stay registry-only like Lex `notabili` / Juris `insights` posts). All rejected by `validate_key_path` so scope creep into non-scalar widgets cannot happen silently even via crafted payloads.
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.dm-*` skin renders `<html dir="rtl" lang="ar">` authentic with light/tile grid density and title `"WalkCasaBrand — الرئيسية"` confirming `site.logo_word|default:brand.brand_name` applied correctly.
- Enrolled via A.12 Session 65 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a12_casa_full_multilocale_lifecycle_end_to_end` as the single dedicated lifecycle regression test). Schema LOC delta +604 (slightly over the 600-LOC soft guardrail) recorded as a non-blocking exception — reflects Casa's structural richness (15 indexed lists vs Juris's 6). The Villa-out guards that lived here during A.12 (registration-time `assertNotIn` in `test_a12_casa_archetype_registered` + runtime `assertNotIn` inside the lifecycle test) were **removed in A.12b** together with Villa's own registrations, and the removal is itself tested by `test_a12b_villa_out_guard_was_removed_from_casa_tests` so a silent regression on the inversion cannot happen.

**ultra-luxury-cinematic (Villa) — editable AND multi-locale enrolled (A.12b) · CLOSES THE REAL-ESTATE FAMILY VIA SECOND DEDICATED-SCHEMA ENROLLMENT · SECOND ARCHETYPE TO USE IMAGE-IN-DICT-ROW:**
- **Single template**: `villa-immobili-lusso`. Distinct archetype from Casa — see Casa block above for DNA/skin-folder/page-slug divergence. Villa's skin `.vp-*` ships 34 mature `html[dir="rtl"]` rules (highest count of any enrolled archetype). 5-locale parity PERFECT (185 keys × 5 locales, zero gaps) — same quality class as Lex.
- 11 sidebar groups · ~175 scalar fields + **4 scalar image fields** (`home.cover_image`, `home.advisor_portrait`, `studio.director_portrait`, `collezione.lead_image`) + 14 readonly indexed lists, with **image cols on 3 of them**:
  - **home (3 lists)**: `signature` dict 4×(index/title/territorio/superficie/provenance/availability/**image**) · `hero_credit_cells` tuple 4×(label/value) · `numbers` tuple 4×(value/label)
  - **collezione (1 list)**: `filter_groups` dict 3×(label) — `options` nested list-of-str col EXCLUDED (complex-shape exclusion like Juris `deliverables`)
  - **territorio (2 lists)**: `territories` dict 6×(name/region/history/architects/count/since/**image**) · `stats` tuple 4×(value/label)
  - **studio (4 lists)**: `advisors` dict 4×(name/role/bio/territories/since/**portrait**/langs) · `partners` tuple 5×(name/note) · `press_items` dict 5×(magazine/issue/title/byline) · `numbers` tuple 6×(value/label)
  - **esperienza (2 lists)**: `process` dict 5×(n/title/duration/text) · `faq_items` dict 6×(q/a)
  - **concierge (2 lists)**: `phone_rows` tuple 4×(label/value) · `offices` dict 3×(city/address/hours/email/role)
- **Total editable image surface: 18** (4 scalar + 14 image cells across 3 non-mutable dict lists: home.signature × 4 rows + territorio.territories × 6 rows + studio.advisors × 4 rows). This is the **second archetype to use image-in-dict-row** after Vertex (`studio.partners[].portrait`, production since A.3a/A.4) — same widget infrastructure, smaller capability surface (non-mutable lists mean cell-edit only, no add/remove row).
- 128 translatable fields + 247 global fields per-template sidebar rendering (walk-verified: `per lingua` badge count = 128 exactly, zero accidentally-translatable globals, **18 `input[type="file"]` image upload widgets** in sidebar matching the expected editable image surface).
- **Complex shapes explicitly outside perimeter** (locked by user-imposed guardrail test `test_a12b_villa_complex_shapes_excluded_from_perimeter`): (a) nested list-of-str inside dict rows (`collezione.filter_groups[].options`, `concierge.form_fields[].options`) · (b) flat list-of-str containers (`home.territory`, `home.press_items`, `collezione.sort_options`, `site.hours_footer_rows`, `site.offices_footer_rows`, `site.office_rows`) · (c) form structure (`concierge.form_fields`) · (d) all per-post `posts` entries including the `posts[].image` col (8 blog post records stay registry-only, same policy as Lex notabili / Juris insights / Casa posts). All 19 paths rejected by `validate_key_path`.
- **Image overrides stay global/plain-keyed** even inside dict rows. Lifecycle test verifies end-to-end: `home.cover_image` + `home.signature.0.image` persist as plain keys; `@<locale>:home.cover_image` + `@<locale>:home.signature.0.image` absent. Per-locale image policy remains out-of-scope per D-098.
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.vp-*` skin renders `<html dir="rtl" lang="ar">` authentic with 34 vp-classed elements and title `"WalkVillaBrand — المنازل"` confirming `site.logo_word|default:brand.brand_name` applied correctly. Both image overrides visible universally across all 5 public-preview locales (verified in Step 3 browser walk).
- Enrolled via A.12b Session 66 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a12b_villa_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched vs A.12 Casa with 1 scalar image override + 1 image-in-dict-row override + assertIn on both image URLs across all 5 public-preview locales + Casa-stays-enrolled runtime guard). Schema LOC delta +587 · **under** the 600-LOC soft guardrail. Zero service-layer / rendering / editor-widget changes required — pure enrollment on 3-file surface (`schema.py` + `_base.html` + `tests.py`), confirming image-in-dict-row is a reusable enrollment pattern rather than a horizontal feature.

**editorial-designer-grid (Chiara) — editable AND multi-locale enrolled (A.13) · FIRST DEDICATED-SCHEMA SLOT OF THE PORTFOLIO FAMILY · THIRD PRECEDENT OF IMAGE-IN-DICT-ROW AT DEEP PATH:**
- **Single template**: `chiara-portfolio-creativo`. Distinct archetype from Pixel — the two portfolio templates ship distinct archetypes + distinct skin folders (`portfolio/editorial-designer-grid/` with `.ed-*` prefix vs `portfolio/cinematic-photographer/` with its own prefix) and ~2/5 page-slug overlap (only `home`+`contatti` shared; `studio`/`biografia` + `lavoro`/`serie` + `processo`/`pubblicazioni` diverge entirely · same divergence pattern as law/real-estate). Shared-schema impossible; closure will follow staged dedicated-schema progression like A.12+A.12b (Chiara now, Pixel in A.13b).
- 8 sidebar groups · ~140 scalar fields + **1 scalar image nested inside parent dict** (`studio.founder.image` — Vertex `home.cover.image` precedent, production since editor foundation A.1) + 11 readonly indexed lists:
  - **home (5 lists)**: `ledger_rows` tuple 6×(num/title/category/year/medium) · `capabilities` tuple 4×2 · `featured_works.items` dict 4×(year/discipline/title/blurb/**image**) — **deep path 2 levels** via `home.featured_works` parent dict · `press` dict 3×(year/honor/work/note) · `commissions` tuple 3×2
  - **studio (3 lists)**: `team` dict 6×(name/role/bio) · `principles` tuple 4×(num/title/body) · `press_full` tuple 8×(year/outlet/category/work)
  - **processo (2 lists, novel `process` kind)**: `process` tuple 5×(num/title/body/deliverable_label/deliverable_value) · `capabilities_full` dict 5×(num/title/blurb/duration) — **`scope` nested list-of-str col intentionally excluded** (complex-shape exclusion)
  - **contatti (1 list)**: `channels` tuple 3×(label/value/note)
- **Total editable image surface: 5** (1 scalar nested-dict `studio.founder.image` + 4 image cells at deep path `home.featured_works.items[0..3].image`). This is the **third precedent of image-in-dict-row** after Vertex `studio.partners[].portrait` (A.3a/A.4) and Villa's 3 A.12b image-col lists (A.12b). The deep path works because `_resolve_path` walks arbitrary-depth dotted paths through dicts — no infrastructure change required.
- 112 translatable fields + 212 global fields per-template sidebar rendering (walk-verified: `per lingua` badge count = 112 exactly, zero accidentally-translatable globals, **5 `input[type="file"]` image upload widgets** in sidebar matching the expected editable image surface).
- **Complex shapes explicitly outside perimeter** (locked by user-imposed guardrail test `test_a13_chiara_complex_shapes_excluded_from_perimeter` · 22 paths rejected by `validate_key_path`):
  - **Per-project `posts` entries** (3 project detail records with nested `sections`/`summary`/`deliverables`/`credits` bodies). Detail-page editing is OUT of A.13 scope — **coherent perimeter decision** consistent with Lex `notabili`, Juris `insights`, Casa `posts`, Villa `posts`. Five uniform enforcements of the "per-item content stays registry-only" policy now. Opening detail-page-scoped editing would be a horizontal feature affecting all 5+ archetypes with per-item content, not Chiara-special-casing. The explicit detail-page-registry-only verify in the Step 3 browser walk fetches `/preview/lavoro/<slug>/` for all 3 project records and confirms static registry content renders with global chrome override but zero per-project editability.
  - Nested list-of-str inside parent dict / dict rows: `studio.founder.credentials` (6 credentials) · `processo.capabilities_full[].scope` (capability bullets)
  - Flat list-of-str containers: `home.clients` (8 client wordmarks) · `lavoro.filters` (6 filter pills)
  - Form structure blocks: `contatti.form_fields` + `contatti.form_sections` + `contatti.upload_field`
- **Image overrides stay global/plain-keyed even at deep path 2 levels** — lifecycle test verifies `home.featured_works.items.0.image` and `studio.founder.image` persist as plain keys, with explicit `assertNot` on `@<locale>:home.featured_works.items.0.image` and `@<locale>:studio.founder.image`.
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.ed-*` skin renders `<html dir="rtl" lang="ar">` authentic with 46 mature `html[dir=rtl]` rules (highest count of any enrolled archetype · Session 37 D-070 Chiara perfection pass · Amiri + Noto Kufi Arabic fonts). Title `"WalkChiaraBrand — الاستوديو"` confirms `site.logo_word|default:brand.brand_name` applied on `.ed-*` skin. The `.ed-*` prefix collides with the editor sidebar namespace (editor shell uses `.ed-sidebar`/`.ed-field`/`.ed-lang-pill`) but the two live in DIFFERENT DOM trees (editor shell vs preview iframe) — zero functional conflict · documented in skin CSS guard block comment.
- **Pixel (`cinematic-photographer`) explicitly NOT enrolled** — guard inside `test_a13_chiara_archetype_registered` asserts `cinematic-photographer NOT in _ARCHETYPE_SCHEMAS NOR in _MULTILOCALE_ENABLED_ARCHETYPES` + all 8 previous archetypes still enrolled. Additionally, the lifecycle test runs a runtime `assertNotIn("cinematic-photographer", _MULTILOCALE_ENABLED_ARCHETYPES)` at both start AND end of test. Both guards will be removed in A.13b together with Pixel's own registrations — same pattern as A.12 Villa-out that was removed in A.12b.
- Enrolled via A.13 Session 67 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a13_chiara_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched vs A.12b Villa with **page-specific image assertions** because Chiara's scalar image lives on studio page, not home · `IMG_FEATURED0` verified on home renders, `IMG_FOUNDER` verified on studio renders across all 5 public-preview locales). Schema LOC delta +533 · **under** the 600-LOC soft guardrail (vs Casa +604 exception, Villa +587). Zero service-layer / rendering / editor-widget changes required — pure enrollment on 3-file surface. The Pixel-out guards that lived here during A.13 (registration-time `assertNotIn` in `test_a13_chiara_archetype_registered` + runtime `assertNotIn` inside the lifecycle test) were **removed in A.13b** together with Pixel's own registrations, and the removal is itself tested by `test_a13b_pixel_out_guard_was_removed_from_chiara_tests` so a silent regression on the inversion cannot happen.

**cinematic-photographer (Pixel) — editable AND multi-locale enrolled (A.13b) · CLOSES THE PORTFOLIO FAMILY VIA SECOND DEDICATED-SCHEMA ENROLLMENT · SINGLE-SCALAR-IMAGE ARCHETYPE PATTERN:**
- **Single template**: `pixel-portfolio-fotografico`. Distinct archetype from Chiara — the two portfolio templates ship distinct archetypes + distinct skin folders (`portfolio/editorial-designer-grid/` with `.ed-*` prefix vs `portfolio/cinematic-photographer/` with `.cp-*` prefix · 133 `.cp-*` hits in the skin, 38 mature `html[dir="rtl"]` rules shipped with the published_live skin since Session 39 D-071 Pixel perfection pass) and ~2/5 page-slug overlap (only `home`+`contatti` shared; `studio`/`biografia` + `lavoro`/`serie` + `processo`/`pubblicazioni` diverge entirely · same divergence pattern as law/real-estate). Shared-schema impossible; closure followed staged dedicated-schema progression like A.12+A.12b real-estate. 5-locale parity PERFECT (154 keys × 5 locales, zero gaps).
- 8 sidebar groups · ~140 scalar fields + **1 scalar image globally** (`home.hero_image` top-level · **no image-in-dict-row · no nested-dict image**) + 10 readonly indexed lists:
  - **home (3 lists)**: `hero_credit_cells` tuple 4×(label/value) · `filmstrip` tuple 4×(num/title/discipline/period) — `slug` col intentionally excluded (used only by `/serie/<slug>/` detail routing) · `publications` tuple 3×(outlet/text/period)
  - **biografia (2 lists)**: `kit` tuple 4×(num/model/body/availability_label/availability_value) · `timeline` tuple 12×(year/title/body)
  - **pubblicazioni (3 lists)**: `press` dict 8×(year/outlet/type/subject/format) — **only dict list on Pixel** · `exhibitions` tuple 6×(year/title/meta/period) · `awards` tuple 6×(year/title/subject)
  - **contatti (1 list)**: `channels` tuple 4×(label/value/note)
  - **site chrome (1 list)**: `exif_footer` tuple 4×(label/value) — IN/OUT decision finalized at Step-0 as IN
- **Total editable image surface: 1** (scalar `home.hero_image` only). This is the **single-scalar-image archetype enrollment precedent** — confirms that a new archetype enrollment does NOT need image-in-dict-row or nested-dict scalar image to be complete. The recipe scales downward (Pixel 1-image-surface) as cleanly as it scales upward (Villa 18-image-surfaces · Chiara deep-path image-in-dict-row at 2 levels). Pragma (1 scalar image) is the first precedent · Pixel is the second.
- 107 translatable fields + 211 global fields per-template sidebar rendering (walk-verified: `per lingua` badge count = 107 exactly, zero accidentally-translatable globals, **exactly 1 `input[type="file"]` image upload widget** in sidebar matching the expected editable image surface).
- **Complex shapes explicitly outside perimeter** (locked by user-imposed guardrail test `test_a13b_pixel_complex_shapes_excluded_from_perimeter` · 23 paths rejected by `validate_key_path`):
  - **Per-project `posts` entries** (3 series records with `cover_image` and body content) + **`series_detail`** page kind. Detail-page editing is OUT of A.13b scope — **coherent perimeter decision** consistent with Lex `notabili`, Juris `insights`, Casa `posts`, Villa `posts`, Chiara `posts`. **Six uniform enforcements** of the "per-item content stays registry-only" policy now. Opening detail-page-scoped editing would be a horizontal feature affecting all 6+ archetypes with per-item content, not Pixel-special-casing. Explicit rejections include `posts.0.cover_image`, `posts.1.cover_image`, `posts.2.cover_image` per user guardrail. The Step 3 browser walk fetches `/preview/serie/{porto-vecchio-trieste,case-di-pietra-puglia,ritratti-del-po}/` for all 3 series records and confirms zero walk-text leak (overridden home headline does NOT bleed into series detail · global chrome logo DOES render everywhere).
  - `serie.filters`, `biografia.statement_paragraphs`, `contatti.form_fields`, `contatti.form_sections`, `contatti.upload_field` — user-imposed absences all verified in the Step 3 browser walk (0 hits across sidebar).
- **Image override stays global/plain-keyed** — lifecycle test verifies `home.hero_image` persists as a plain key across all 5 locales (5 explicit `assertNotIn("@<locale>:home.hero_image")` assertions covering `@it/en/fr/es/ar`).
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.cp-*` skin renders `<html dir="rtl" lang="ar">` authentic with 38 `html[dir=rtl]` rules. Title `"A13b Pixel Walk Brand — الفهرس"` confirms `site.logo_word|default:brand.brand_name` applied on `.cp-*` skin.
- Enrolled via A.13b Session 68 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a13b_pixel_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched vs A.13 Chiara with 5 explicit `assertNotIn("@<locale>:home.hero_image")` + ninefold regression guard + posts-stay-out end-of-test re-check). Schema LOC delta +510 — comfortably under the 600-LOC soft guardrail (vs Chiara +533, Villa +587, Casa +604 exception). Zero service-layer / rendering / editor-widget changes required — pure enrollment on 3-file surface (`schema.py` + `_base.html` + `tests.py`). **Mechanical reuse of A.13 recipe** confirmed — no schema refactor, no new widget, no new test helper. The Chiara-out guard removal / Pixel-in inversion was done in controlled fashion and contract-tested (`test_a13b_pixel_out_guard_was_removed_from_chiara_tests` mirrors the A.12b `test_a12b_villa_out_guard_was_removed_from_casa_tests` pattern).

**trattoria-warm (Sapore) — editable AND multi-locale enrolled (A.14) · OPENS THE RESTAURANT-CONTINUATION FAMILY · DEEP-PATH TUPLE-IN-DICT-LIST PARENT SHAPE PRECEDENT:**
- **Single template**: `sapore-trattoria-pizzeria`. Distinct archetype from Brace — the two restaurant-continuation templates ship distinct archetypes + distinct skin folders (`restaurant/trattoria-warm/` with `.tw-*` prefix (60 hits) vs `restaurant/street-modern/` with `.sm-*` prefix (87 hits)) and 50% page-slug overlap (home/menu/contatti shared; storia/forno/eventi Sapore vs lab/moments/ordina Brace). Fundamentally different menu shape (Sapore nested tuple vs Brace nested dict-with-image-col) and image surface ratio 1:3.5 — **shared-schema (A.9 recipe) is impossible**. Closure will follow staged dedicated-schema progression like A.12+A.12b real-estate and A.13+A.13b portfolio (Sapore now, Brace in A.14b). 5-locale parity PERFECT (224 keys × 5 locales, zero gaps). 18 mature `html[dir="rtl"]` rules in `_base.html` since Session 48 D-078 Sapore rollout.
- 8 sidebar groups · ~141 scalar fields + **7 top-level scalar image fields** (home.hero_image · home.forno_image · home.tavolata_image · storia.photo_image · forno.forno_story_image · forno.dough_image · eventi.birthday_image) + **2 image-in-dict-row lists** (home.family[].portrait × 3 + storia.family[].portrait × 3) — **13 total editable image surfaces** · 20 readonly indexed lists:
  - **home (5 lists)**: `family` dict 3×(name/role/blurb/**portrait**) · `reviews` dict 3×(quote/author) · `facts` tuple 3×(label/value) · `chalkboard_days` tuple 5×(day/dish/side/note) · `hours_rows` tuple 3×(days/hours/note)
  - **menu (6 lists)**: `sections` dict 5×(label/heading) parent + **5 deep-path tuple lists `menu.sections.{0..4}.dishes`** (section sizes 7/7/6/5/5 dishes · cols name/desc/price) — novel tuple-in-dict-list parent shape, first precedent
  - **storia (3 lists)**: `timeline` dict 3×(year/title/desc) · `family` dict 3×(name/role/blurb/**portrait**) · `values` dict 4×(title/desc)
  - **forno (3 lists)**: `pizza_signatures` dict 4×(n/name/desc/price) · `pasta_signatures` dict 4×(n/name/desc/price) · `producers` dict 5×(name/place/ingredient)
  - **eventi (1 list)**: `experiences` dict 3×(n/title/persons/menu/wine/desc)
  - **contatti (2 lists)**: `transport` dict 4×(mode/line/note) · `hours_table` tuple 4×(days/hours/note)
- 121 translatable fields + 296 global fields per-template sidebar rendering (walk-verified · browser walk Step 3 showed `per lingua` badge count = 121 · 13 `input[type="file"]` image upload widgets matching expected surface).
- **Menu rows are INSIDE perimeter via deep-path tuple-in-dict-list parent shape** — novel shape first precedented in A.14. Each section's tuple 7/7/6/5/5 × 3-col (name/desc/price) is registered as a separate STRUCTURED_FIELD_SHAPES entry at deep path `menu.sections.{i}.dishes`. Without menu in perimeter the enrollment would have been fake-editable (user-imposed Step 0 guardrail: "perimetro vero, non finto"). Browser walk verified `menu.sections.0.dishes.0.name` override renders universally across all 5 public-preview locales (IT/EN/FR/ES/AR) on the menu page.
- **Complex shapes explicitly outside perimeter** (locked by `test_a14_sapore_complex_shapes_excluded_from_perimeter`):
  - `contatti.form_sections` + `contatti.form_fields` (form structure blocks · consistent policy)
  - `contatti.occasion_options` (7 options for form select · flat list-of-str)
  - `storia.story` (4 bio paragraphs · flat list-of-str · same category as Pixel `biografia.statement_paragraphs`)
  - `site.hours_footer_rows` (2 hours rows · flat list-of-str)
  - `pages` (top-level navigation index · always out)
  - `posts` + `posts.0.*` paths — **Sapore ships `posts: []` in the registry** (structural absence, not a perimeter decision). First enrollment since A.10 without posts list. The cross-archetype uniform detail-page enforcement count stays at 6 (Lex+Juris+Casa+Villa+Chiara+Pixel).
- **Image + deep-path-menu overrides stay global/plain-keyed** — lifecycle test verifies `home.hero_image` and `menu.sections.0.dishes.0.name` persist as plain keys across all 5 locales (5× `assertNotIn` per path).
- **Three editor layers now aligned on list numeric indexing** — Sapore's novel shape required finally completing the contract-alignment across `services._resolve_path` (always supported), `schema._resolve_path` (Step 1 · 8-line extension), `rendering._apply_indexed` (Step 2 · contract-alignment bugfix, commit `f66ac24`). The render-side fix is **NOT scope-creep**: it closes a historical runtime incoherence that only surfaced with Sapore's novel shape (save layer persisted overrides correctly · render layer silently dropped them on list-parent-walks). Committed isolated from the test commit (2-commit split: `f66ac24` for the fix + `7a8e1c3` for the test) so bug fix provenance is clean.
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.tw-*` skin renders `<html dir="rtl" lang="ar">` authentic. Title `"A14 Sapore Walk Brand — الرئيسية"` confirms `site.logo_word|default:brand.brand_name` applied.
- Enrolled via A.14 Session 69 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a14_sapore_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched vs A.13b Pixel with 5× `assertNotIn("@<locale>:menu.sections.0.dishes.0.name")` + menu page spot-check for dish override universality). Schema LOC delta +663 — **slightly over** the 600-LOC soft guardrail, recorded as a non-blocking exception because the overshoot reflects the 5 additional menu-deep-path shape entries (structurally necessary). 12 contract tests + 1 lifecycle test + `rendering.py` contract-alignment fix. **Four-commit phase** (not three): `ef74b4e` schema · `f66ac24` render fix · `7a8e1c3` lifecycle test · `8fae2df` merge — the 2-commit split between bug fix and test keeps history honest about the production-code touch. The Brace-out guards that lived here during A.14 (registration-time + runtime · 2 locations) were **removed in A.14b** together with Brace's own registrations · contract-tested by `test_a14b_brace_out_guard_was_removed_from_sapore_tests`.

**street-modern (Brace) — editable AND multi-locale enrolled (A.14b) · CLOSES THE RESTAURANT-CONTINUATION FAMILY VIA SECOND DEDICATED-SCHEMA ENROLLMENT · FIRST `order` PAGE KIND + DEEP-PATH DICT-IN-DICT-LIST PARENT PRECEDENT VIA LIST-INDEX WALK:**
- **Single template**: `brace-street-food-lab`. Distinct archetype from Sapore — the two restaurant-continuation templates ship distinct archetypes + distinct skin folders (`restaurant/trattoria-warm/` with `.tw-*` vs `restaurant/street-modern/` with `.sm-*` · 87 `.sm-*` hits · 24 mature `html[dir="rtl"]` rules) and 50% page-slug overlap (home+menu+contatti shared; lab/moments/ordina Brace vs storia/forno/eventi Sapore diverge entirely). Fundamentally different menu shape (Brace nested dict-with-image-col vs Sapore nested tuple no-image) + image surface ratio 3.4× (44 surfaces vs 13) + form structure presence inverted (Brace ships ZERO form) — **shared-schema impossible**. Closure followed staged dedicated-schema progression (Sapore → Brace) · third consecutive staged closure after real-estate and portfolio. 5-locale parity PERFECT (273 keys × 5 locales · zero gaps).
- 8 sidebar groups · ~170 scalar fields + **3 top-level scalar image fields** (home.hero_image · lab.hero_image · moments.featured_image) + **6 image-in-dict-row lists** (41 image cells total · 5 shallow + 1 deep-path):
  - **home (5 lists)**: `stats` tuple 4×(value/label) · `menu_strip_items` dict 6×(name/desc/price/tag/**image**) — image col · `delivery_partners` tuple 4×(name/eta/min) · `crew` dict 3×(name/role/quote/**portrait**) — image col · `atmo_strip` dict 3×(cap/**image**) — image col
  - **menu (7 lists)**: `sections` parent dict 5×(label/title/desc) — id col excluded, items nested separately + **`sections.{0..4}.items` dict 4/4/4/4/3×(name/desc/price/tag/**image**) — 5 deep-path dict-in-dict-list entries with image col (19 image cells · **Chiara-precedent shape with list-index parent walk · first precedent for this variant**)** · `producers` dict 3×(name/city/role)
  - **lab (5 lists)**: `manifesto_paragraphs` dict 4×(title/text) · `process` dict 3×(num/title/desc) · `crew` dict 4×(name/role/quote/**portrait**) — image col · `values` dict 4×(title/tag/desc) · `kitchen_specs` tuple 6×(value/label)
  - **moments (1 list)**: `grid` dict 6×(cap/tag/**image**) — image col · **`filename` col excluded** (structural ID)
  - **ordina (4 lists)**: `routes` parent dict 3×(title/subtitle/desc/cta_label/cta_href) — id+cta_kind cols excluded, lines nested separately + **`routes.{0..2}.lines` tuple 3×(label/value) — 3 deep-path tuple-in-dict-list entries (Sapore-precedent shape)** · `partners` dict 4×(name/eta/min/zone) · `hours_rows` tuple 7×(day/hours) · `faq` dict 4×(q/a)
  - **contatti (5 lists)**: `channels` dict 3×(label/value/note/href) — icon+kind cols excluded · `hours_rows` tuple 3×(days/hours) · `transport_rows` tuple 4×(mode/note) · `jobs` dict 3×(role/type/city) · `social` dict 2×(platform/handle/href)
- **Total editable image surface: 44** (3 scalar + 41 cells across 6 image-in-dict-row lists) · browser-walk verified exactly 44 `input[type="file"]` widgets in sidebar with distinct scalar/dict-row breakdown (3 scalar top-level + 41 dict-row cells).
- **Total readonly indexed list entries: 30** (22 parent + 5 `menu.sections.{i}.items` deep-path + 3 `ordina.routes.{i}.lines` deep-path) — highest count of any enrolled archetype.
- 148 translatable fields + 401 global fields per-template sidebar rendering.
- **Complex shapes explicitly outside perimeter** (locked by user-imposed guardrail test `test_a14b_brace_complex_shapes_excluded_from_perimeter` · 21 rejected paths):
  - Flat list-of-str containers: `site.hours_footer_rows` · `home.manifesto_paragraphs` · `moments.categories`
  - Col-level exclusions (structural identifiers / routing flags): `menu.sections[].id` · `moments.grid[].filename` · `ordina.routes[].id` + `cta_kind` · `contatti.channels[].icon` + `kind`
  - Navigation + empty posts: `pages` · `posts` (empty · same as Sapore · detail-page policy enforcement count stays at 6)
  - **No form structures** — Brace ships ZERO `contatti.form_sections`/`form_fields` list structures (smaller out-policy set than Sapore) · only scalar form labels (`contatti.form_field_name`/`_email`/`_phone`/`_message` etc.)
- **`ordina.routes[].lines` IN — correction di ipotesi Step 0 audit**: initial hypothesis was "OUT default unless audit proves editorial value"; audit demonstrated strong editorial value (address/phone/delivery-partner names/opening hours — customer would absolutely change them). Registered as 3 deep-path tuple-in-dict-list entries (Sapore `menu.sections.{i}.dishes` precedent shape · same infra via `f66ac24`).
- **`menu.sections[].items[].tag` IN**: Step 0 audit showed tag values ('TOP', 'NEW', 'VEG') are editorial badges visible on the customer-facing menu (not structural). All 5 cols IN per section items.
- **Image + deep-path overrides stay global/plain-keyed** — lifecycle test verifies `home.hero_image` + `menu.sections.0.items.0.image` + `ordina.routes.0.lines.0.value` persist as plain keys across all 5 locales (15× `assertNotIn` total covering all 3 paths × 5 locales).
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. **AR preview on `.sm-*` skin renders `<html dir="rtl" lang="ar">` authentic** with 24 RTL rules in `_base.html`. Title `"A14b Brace Walk Brand — الرئيسية"` confirms `site.logo_word|default:brand.brand_name` applied.
- **Brace-out guard removal was done in controlled fashion and contract-tested**: `test_a14b_brace_out_guard_was_removed_from_sapore_tests` asserts Brace IS in all three gate sets + Sapore still enrolled, mirroring the A.12b Villa-out-removal + A.13b Pixel-out-removal pattern. The 2 Brace-absence dual-layer assertions removed from the A.14 Sapore tests (registration-time + runtime end-of-lifecycle) are verified as correctly inverted rather than forgotten. **Guard removal pattern now has 3 precedents** (Villa · Pixel · Brace).
- Additionally, the **6 pre-existing "unsupported archetype" test fixtures were rotated** from `street-modern`/`brace-street-food-lab` to `artisan-workshop`/`bottega-shop-artigianale` (next likely enrollment candidate · ecommerce family) · keeps fixture set aligned with current outside-gate reality.
- Enrolled via A.14b Session 70 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a14b_brace_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched vs A.14 Sapore with BOTH deep-path shape overrides exercised: dict-in-dict-list `menu.sections.0.items.0.image` AND tuple-in-dict-list `ordina.routes.0.lines.0.value` · 15× `assertNotIn("@<locale>:...")` per path × 5 locales · menu + ordina page spot-checks for universal override rendering on all 5 public-preview locales · no-neighbor-corruption explicit browser-walk verification). **Pure 3-file enrollment surface**: schema.py +826 LOC (documented exception over 600-LOC guardrail · overshoot reflects 8 deep-path entries + 3.4× Sapore volume · alternative menu-fake-editable / pseudo-path-scalars rejected Step 0) · street-modern/_base.html 3 atomic fix · tests.py 13 contract + 1 lifecycle test + Brace-out guard removal + OUT fixture rotation. **Three-commit phase** on branch (not four, because Brace fully reused A.14 `f66ac24` with zero additional infra fixes): `fabea8a` schema · `4fd677b` lifecycle test · `7c064f8` merge — the A.14 render-fix is now cross-pattern-confirmed operationally across both tuple-in-dict-list and dict-in-dict-list parent shapes.

**artisan-workshop (Bottega) — editable AND multi-locale enrolled (A.15) · FIRST DEDICATED-SCHEMA SLOT OF THE ECOMMERCE FAMILY · SHOWCASE/TEMPLATE-CONTENT EDITING · RENDERED VS STORAGE-ONLY IMAGE DISTINCTION INTRODUCED:**
- **Single template**: `bottega-shop-artigianale`. Distinct archetype from Luxe — the two ecommerce templates ship distinct archetypes + distinct skin folders (`ecommerce/artisan-workshop/` with `.aw-*` prefix (97 hits · 31 mature `html[dir="rtl"]` rules) vs `ecommerce/fashion-editorial/` with `.fe-*` prefix). 50% page-slug overlap (home/product/contatti shared; shop/journal Bottega vs collection/lookbook Luxe), `shop.products` 11 cols vs `collezione.products` 9 cols (different editorial surfaces), image surface ratio 1:1.4. Shared-schema impossible. Luxe pending A.15b closure.
- **BOUNDARY EDITOR-VS-COMMERCE-ADMIN (runtime-verified Step 0)**: the editor edits ONLY template_content registry (presentational demo showcase). `apps/commerce/` (Storefront · Product · Variant · Cart · Order · PaymentIntent · seller dashboard Phase 3a/3b) is ORTHOGONAL and out-of-scope. `apps/catalog/views.py::LiveTemplateView` does NOT import from `apps.commerce` · the two surfaces render independently at `/templates/ecommerce/<slug>/preview/` (registry · editor) vs `/shop/<storefront>/` (commerce · seller dashboard). A light guardrail test `test_a15_bottega_commerce_admin_boundary` smoke-checks that the editor schema doesn't reference `apps.commerce` model namespaces (`storefront.` · `cart.` · `variant.` · `order.` · `payment_intent.` · etc.). This boundary is why A.15 stays a pure 3-file enrollment with ZERO touches to `apps/commerce/`.
- 8 sidebar groups · ~141 scalar fields + **0 scalar top-level image** (artisan-workshop is typographic-led DNA per Session 42 D-073 · no hero photo) + **2 nested-dict scalar images** (`product.artisan_portrait` · `atelier.founder_portrait` · Chiara `studio.founder.image` precedent shape · **STORAGE-ONLY**: skin renders monogram stamps instead of photos) + **4 image-in-dict-row lists**:
  - **home (2 lists)**: `latest_items` dict 4×(n/name/meta/place/price/edition/tag/**image**) — image col RENDERED · `makers` dict 4×(name/craft/place/since/quote/**portrait**) — portrait col STORAGE-ONLY (skin paints crest-mark glyph)
  - **shop (1 list)**: `products` dict 9×(n/name/artisan/place/meta/price/edition/tag/**image**) — image col RENDERED · **demo catalog listing** · first ecommerce-specific shape
  - **product (1 list)**: `related_items` dict 3×(n/name/meta/price/**image**) — image col RENDERED
- **Total editable image surface: 22** (0 scalar top + 2 nested-dict scalar STORAGE-ONLY + 20 image cells · 16 RENDERED + 6 STORAGE-ONLY).
- **RENDERED VS STORAGE-ONLY IMAGE DISTINCTION (INTENTIONAL · NOT A BUG)**: browser-walk Step 3 verified **22 sidebar image widgets = 16 rendered + 6 storage-only**. The 6 storage-only fields (`product.artisan_portrait` · `atelier.founder_portrait` · `home.makers.{0..3}.portrait`) are exposed because the registry data is preserved for potential future skin variants / customer swap (Session 42 D-073 typographic-first conversion). The 16 rendered fields (all `*.image` cols in dict-rows) are painted by `.aw-*` skin via `background-image:url('{{ x.image }}')`. Storage contract (plain-key per-locale) blindato identical on both categories — only VISIBILITY differs per skin rendering. Lifecycle test exercises 5 image overrides (3 rendered + 2 storage-only) with identical 5× `assertNotIn("@<locale>:...")` contract. This distinction is documented in test docstrings and is the explicit handling of a pre-existing DNA-honest skin choice.
- 125 translatable fields + 417 global fields per-template sidebar rendering (walk-verified: 125 `per lingua` badges · 22 `input[type="file"]` image widgets exactly · 3 shop-listing shapes · 16 rendered + 6 storage-only classified).
- 14 readonly indexed list entries in STRUCTURED_FIELD_SHAPES · **tutti parent-level · ZERO deep-path** (Bottega has no list-nested-in-list-parent · simpler than Sapore's 20 entries with 5 menu-deep-path and Brace's 30 entries with 8 total deep-path).
- 3 novel page kinds enrolled: `shop` (catalog listing demo) · `product` (single-product demo record) · `journal` (editorial notes / diary entries). All plain string identifiers · no view dispatch.
- **Stringent IN/OUT call on "technical-looking" fields** per user Step 1 guidance (audit-driven, not inertia):
  - **IN** (editorial visible · customer-facing badges): `shop.products[].n` ('N° 042') · `.edition` ('3 / 8' · 'Esaurito') · `.tag` ('Fatto a mano' · Brace-precedent) · `home.latest_items[].n`/`.edition`/`.tag` · `home.provenance_items[].icon` ('01'/'02'/'03') · `atelier.process_steps[].n` · `journal.entries[].n` · `product.related_items[].n`
  - **OUT col-level** (truly structural): `shop.products[].id` (slug routing) · `.available` (bool flag · commerce-state-like semantic) · `home.latest_items[].id` · `product.related_items[].id`
  - Dedicated contract test `test_a15_bottega_visible_catalog_fields_kept_in` blindates the IN call · `test_a15_bottega_complex_shapes_excluded_from_perimeter` blindates the OUT call + flat list-of-str exclusions.
- **Complex shapes explicitly outside perimeter** (21 rejected paths): `site.hours_footer_rows` · `site.stockists_rows` · `home.press_items` · `shop.filter_groups` + `.0.options` (nested list-of-str) · `shop.sort_options` · `product.gallery` (flat list-of-str of image URLs) · `product.size_options` · `contatti.card_hours_rows` · `contatti.form_fields` (form structure) · `pages` · `posts` (empty · same as Sapore/Brace · detail-page policy stays at 6-archetype enforcement count).
- **Image + nested-dict scalar overrides stay global/plain-keyed** — lifecycle test verifies 5 image paths (2 nested-dict scalar + 3 image-in-dict-row) persist as plain keys across all 5 locales (25× `assertNotIn` total covering all 5 paths × 5 locales).
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.aw-*` skin renders `<html dir="rtl" lang="ar">` authentic with 31 RTL rules. Title `"A15 Bottega Walk Brand — الورشة"` confirms `site.logo_word|default:brand.brand_name` applied.
- **Luxe (`fashion-editorial`) explicitly NOT enrolled** — Luxe-out guard inside `test_a15_bottega_archetype_registered` asserts `fashion-editorial NOT in _ARCHETYPE_SCHEMAS NOR in _MULTILOCALE_ENABLED_ARCHETYPES` + all 12 pre-A.15 archetypes still enrolled. The lifecycle test additionally runs a runtime `assertNotIn("fashion-editorial", ...)` at start AND end of test (leak check duro 2x). Both guards will be removed in A.15b together with Luxe's own registrations — **fourth precedente del guard removal pattern dopo Villa/Pixel/Brace** · contract-tested via `test_a15b_luxe_out_guard_was_removed_from_bottega_tests`.
- **6 pre-existing "unsupported archetype" test fixtures were rotated** from `artisan-workshop`/`bottega-shop-artigianale` to `fashion-editorial`/`luxe-fashion-store` (A.15b pending candidate) · keeps fixture set aligned with current outside-gate reality. Rotation is now a standard sub-recipe for staged dedicated-schema closure workflows.
- Enrolled via A.15 Session 71 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a15_bottega_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched with 5 image path overrides covering 3 rendered + 2 storage-only patterns · 25× `assertNotIn("@<locale>:...")` total · 3-page render verification on home + shop + product across all 5 public-preview locales). **Pure 3-file enrollment surface**: schema.py +585 LOC (**sotto** 600-LOC soft guardrail · leaner than initial 650 planning estimate · 14 entries senza deep-path = simpler than Sapore's 20 entries and Brace's 30) · artisan-workshop/_base.html 3 atomic fix · tests.py 13 contract + 1 lifecycle test + Luxe-out guard + OUT fixture rotation. **Three-commit phase** on branch: `cff68a1` schema · `7764f40` lifecycle test · `fab3ebc` merge — zero additional infra fixes required · full mechanical reuse of nested-dict-scalar + shallow image-in-dict-row patterns. **Zero touches to `apps/commerce/`** runtime-verified via the light commerce-boundary test · boundary is architectural (LiveTemplateView doesn't import apps.commerce).

**fashion-editorial (Luxe) — editable AND multi-locale enrolled (A.15b) · SECOND DEDICATED-SCHEMA SLOT OF THE ECOMMERCE FAMILY · CLOSES THE ECOMMERCE FAMILY · ALL IMAGE SURFACES RENDERED (no storage-only split):**
- **Single template**: `luxe-fashion-store`. Distinct archetype from Bottega · `.fe-*` skin prefix (165 hits · 21 mature `html[dir="rtl"]` rules · `_base.html` 803 LOC after atomic fixes). Fourth consecutive staged dedicated-schema closure after real-estate (A.12+A.12b) · portfolio (A.13+A.13b) · restaurant-continuation (A.14+A.14b).
- **BOUNDARY EDITOR-VS-COMMERCE-ADMIN preserved on second ecommerce archetype**: same architectural boundary validated Step-0 in A.15 Bottega · `apps/catalog/views.py::LiveTemplateView` still does NOT import from `apps.commerce` · editor edits `template_content_luxe.py` (registry: collezione catalog listings demo · single product demo · lookbook editorial · maison about · hero/copy bands) · real catalog state stays in `apps/commerce/` managed via seller dashboard. Light guardrail test `test_a15b_luxe_commerce_admin_boundary` mirrors the A.15 Bottega contract. Zero touches to `apps/commerce/`.
- 8 sidebar groups · ~164 scalar fields + **1 scalar top-level image** (`home.cover_image` · full-bleed editorial cover LEFT on charcoal · full-RENDERED) + **2 nested-dict scalar images** (`product.atelier_portrait` · `maison.direction_portrait` · both RENDERED as portrait blocks on their pages) + **6 image-in-dict-row lists**:
  - **home (2 lists)**: `tiles` dict 4×(tag/name/price/**image**) — 4 RENDERED edition tiles · `lookbook_teaser_tiles` dict 3×(title/credit/**image**) — 3 RENDERED teaser images
  - **collezione (1 list)**: `products` dict 9×(n/name/meta/drop/price/tag/**image**) — 9 RENDERED demo catalog entries · novel `collection` page kind
  - **product (1 list)**: `related_items` dict 3×(n/name/meta/price/**image**) — 3 RENDERED related capi
  - **maison (1 list)**: `ateliers` dict 3×(city/place/role/since/head/team/**image**) — 3 RENDERED atelier portraits
  - **lookbook (1 list)**: `looks` dict 6×(n/title/outfit/credit/**image**) — 6 RENDERED editorial looks · novel `lookbook` page kind
- **Total editable image surface: 31** (1 scalar top + 2 nested-dict scalar + 28 image cells · **ALL 31 RENDERED**).
- **RENDERED VS STORAGE-ONLY IMAGE DISTINCTION IS PER-SKIN · NOT PER-SCHEMA**: unlike Bottega's 16-rendered + 6-storage-only typographic split, Luxe is photographically editorial campaign-driven DNA · every image surface the editor exposes is painted by the skin. Schema exposes image fields identically in both cases (same `type: "image"` · same STRUCTURED_FIELD_SHAPES col · same plain-key per-locale storage); only skin rendering differs. Lifecycle + browser walk verified render on all 31 Luxe image surfaces across 5 locales × relevant pages.
- ~130 translatable fields + ~450 global fields per-template sidebar rendering (walk-verified: 448 total editable fields · 31 image widgets exactly · 26 group slots = 8 sidebar + 17 indexed + 1 design · 5 lang pills).
- 17 readonly indexed list entries in STRUCTURED_FIELD_SHAPES · **tutti parent-level · ZERO deep-path** · richer than Bottega's 14 (2 extra maison entries + 2 extra lookbook entries · no deep-path like Sapore/Brace).
- 2 novel page kinds enrolled: `collection` (collezione catalog listing) · `lookbook` (editorial image grid · 6-look pullquote + credits + notes-from-set).
- **Stringent IN/OUT call on "technical-looking" fields** per user Step 0 guidance (audit-driven, non-inertial · 4th archetype to apply this framing after Sapore/Brace/Bottega):
  - **IN** (editorial visible · customer-facing badges): `collezione.products[].drop` ('Drop 01 · Spring 26' · editorial drop badge) · `.n` ('Look 03' · Look numbering) · `.tag` ('Lista d'attesa' · 'Capsula' · 'Archivio' · editorial availability badge) · `home.tiles[].tag` · `product.related_items[].n` · `lookbook.looks[].n`
  - **OUT col-level** (truly structural): `collezione.products[].id` (slug routing) · `.available` (bool flag · commerce-state-like semantic) · `home.tiles[].id` · `product.related_items[].id`
  - Dedicated contract test `test_a15b_luxe_visible_catalog_fields_kept_in` blindates the IN call · `test_a15b_luxe_complex_shapes_excluded_from_perimeter` blindates the OUT call + flat list-of-str exclusions.
- **Complex shapes explicitly outside perimeter** (18 rejected paths): `site.hours_footer_rows` · `site.office_rows` · `home.press_items` · `collezione.filter_groups` + `.0.options` (nested list-of-str) · `collezione.sort_options` · `product.gallery` (flat list-of-str of image URLs) · `product.size_options` · `product.color_options` · `contatti.form_fields` (form structure) · `pages` · `posts` (empty · same as Bottega/Sapore/Brace · 7-archetype detail-page enforcement count unchanged — detail-page policy registered per-archetype-count stays at 6 because Luxe has no posts to lock).
- **Image + nested-dict scalar overrides stay global/plain-keyed** — lifecycle test verifies 5 image paths (1 scalar top `home.cover_image` + 2 nested-dict scalar + 2 image-in-dict-row) persist as plain keys across all 5 locales (25× `assertNotIn` total covering all 5 paths × 5 locales).
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.fe-*` skin renders `<html lang="ar" dir="rtl">` authentic with 21 RTL rules · 5182 Arabic characters in body. Authored AR headline `الجسد الجديد للِّباس.` verified rendering on home page after browser walk.
- **Luxe-out dual guard removed from A.15 Bottega tests** (3 locations: registration-time in `test_a15_bottega_archetype_registered` · runtime start + runtime end of lifecycle test) via symmetric inversion `test_a15b_luxe_out_guard_was_removed_from_bottega_tests` · **fourth precedente** del guard removal pattern dopo Villa/Pixel/Brace · sub-recipe standard per ogni staged dedicated-schema closure phase.
- **6 pre-existing "unsupported archetype" test fixtures were rotated** from `fashion-editorial`/`luxe-fashion-store` to `clinic`/`salute-studio-medico` (medical-clinic family · next likely enrollment wave · A.16 candidate). First rotation to a non-restaurant / non-ecommerce outside-gate target since A.12+.
- Enrolled via A.15b Session 72 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a15b_luxe_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched with 5 image path overrides covering scalar top + 2 nested-dict scalar + 2 image-in-dict-row patterns · 25× `assertNotIn("@<locale>:...")` total · 5-page render verification on home + collezione + product + maison + lookbook across all 5 public-preview locales). **Pure 3-file enrollment surface**: schema.py +598 LOC (**sotto** 600-LOC soft guardrail · leaner than initial 680-720 planning estimate · 17 entries senza deep-path) · fashion-editorial/_base.html 3 atomic fix · tests.py 14 contract + 1 lifecycle test + Luxe-out dual guard REMOVED + OUT fixture rotation to clinic/Salute. **Three-commit phase** on branch: `d946b3d` schema · `246b0e5` lifecycle test · `bd9ffcb` merge — zero additional infra fixes required · full mechanical reuse of scalar-top + nested-dict-scalar + shallow image-in-dict-row patterns. **Zero touches to `apps/commerce/`** confirmed · boundary architectural re-verified.

**clinic (Salute) — editable AND multi-locale enrolled (A.16) · FIRST DEDICATED-SCHEMA SLOT OF THE MEDICAL-OTHER FAMILY · FIRST 3-TEMPLATE STAGED PROGRESSION · NOVEL 5th OUT CATEGORY (RAW SVG):**
- **Single template**: `salute-studio-medico`. First of 3 medical-other archetypes (Benessere `wellness` + Famiglia `family` pending A.16b + A.16c respectively). Distinct skin folder (`medical/clinic/` with `.cl-*` prefix · 78 hits · 18 mature `html[dir="rtl"]` rules · `_base.html` 520 LOC after atomic fixes). Page-slug overlap with siblings only on home + contatti (3-of-3) · content-tree key overlap ~0% across all 3 medical-other → shared-schema impossible (verified Step 0 audit · same constraint as ecommerce Bottega+Luxe).
- **BOUNDARY EDITOR-VS-CLINIC-ADMIN (runtime-verified Step 0)**: the editor edits ONLY `template_content_salute.py` registry (presentational demo content). `apps/catalog/views.py::LiveTemplateView` does NOT import from any scheduler/booking/patient namespace. No real `apps/clinic_admin/` exists yet, but the boundary contract is established for future Phase 4+ work (similar shape to A.15/A.15b commerce-admin boundary — second category-class boundary established). Light guardrail test `test_a16_salute_clinic_admin_boundary` smoke-checks that the editor schema doesn't accidentally reference `appointment.` · `booking.` · `patient.` · `scheduler.` · `calendar_slot.` · `medical_record.` · `prescription.` namespaces. Boundary architectural · zero cross-contamination by design.
- 9 sidebar groups · ~95 scalar fields + **1 scalar top-level image** (`studio.photo_src` · about page photo · RENDERED) + **2 image-in-dict-row lists**:
  - **home (1 list)**: `team_ribbon_people` dict 8×(name/specialty/**avatar**) — 8 RENDERED specialist portraits in team ribbon
  - **medici (1 list)**: `doctors` dict 6×(name/role/credentials/**portrait**) — 6 RENDERED full-page doctor portraits
- **Total editable image surface: 15** (1 scalar top + 14 image-in-dict-row cells · ALL RENDERED · specialist-family precedent skin · no storage-only split unlike Bottega).
- ~70 translatable fields + ~290 global fields per-template sidebar rendering (walk-verified: 359 total editable fields · 15 image widgets exactly · 26 group slots = 9 sidebar + 16 indexed + 1 design · 5 lang pills).
- 16 readonly indexed list entries in STRUCTURED_FIELD_SHAPES · **tutti parent-level · ZERO deep-path** (12 dict + 4 tuple). Mid-complexity between Bottega 14 and Brace 30.
- **2 novel page kinds** enrolled: `prevention` (prevenzione page · check-up packages) + `appointment` (prenota page · booking form · same kind-name as Benessere prenota for future shared-skin compatibility).
- **NOVEL 5th OUT CATEGORY PRECEDENT · raw `icon_svg` fields**: 18 raw SVG XML markup fields (`home.specialties[].icon_svg` × 8 + `servizi.services[].icon_svg` × 10) used for inline icon rendering. **OUT col-level** via STRUCTURED_FIELD_SHAPES col exclusion. Rationale: editing raw SVG XML as plain text is unsafe (XSS-like content via paste · Pillow.verify only covers image binaries · sanitization would be horizontal feature) and customer-unfriendly UX (no SVG-editor widget · adding one is a horizontal feature). Dedicated contract test `test_a16_salute_raw_svg_fields_excluded` blindates exclusion at 2 layers (`get_field_spec` returns None · `validate_key_path` raises `InvalidEditableField`).
- **Stringent IN/OUT call on "technical-looking" fields** per user Step 0 guidance (audit-driven · 5th archetype precedent chain after Sapore/Brace/Bottega/Luxe):
  - **IN** (editorial visible · customer-facing): `home.journey_steps[].num` ('01'/'02'/'03'/'04' visible step numbering) · `prevenzione.how_steps[].num` · `prenota.help_steps[].num` · `prevenzione.packages[].popular_label` ('Più richiesto' customer-facing badge text)
  - **OUT col-level** (truly structural · technical · safety): `prevenzione.packages[].is_popular` (bool flag · no horizontal field type · preserves popular_label text editability · Luxe `available` precedent) · 18× `icon_svg` (raw SVG XML · 5th OUT category)
  - Dedicated contract tests `test_a16_salute_visible_catalog_fields_kept_in` blindates IN call · `test_a16_salute_complex_shapes_excluded_from_perimeter` + `test_a16_salute_raw_svg_fields_excluded` blindano OUT calls.
- **Complex shapes explicitly outside perimeter** (~25 rejected paths): 4× flat list-of-str (`site.hours_footer_rows` · `site.foot_extra_rows` · `home.partners` · `prenota.trust`) + 4× nested list-of-str inside dict rows (`servizi.services[].items` · `prevenzione.packages[].includes` · `home.prevenzione_cards[].includes` · `medici.doctors[].tags` · Juris precedent) + 3× form structures (`contatti.form_fields` · `prenota.form_fields` · `prenota.form_sections` · Juris/Gusto/Bottega/Luxe precedent) + bool `is_popular` + 4× `icon_svg` + `pages` + `posts` (empty · same structural absence as Bottega/Luxe/Sapore/Brace · detail-page policy stays at 6-archetype uniform enforcement count).
- **Image overrides stay global/plain-keyed** — lifecycle test verifies 3 image paths (1 scalar top + 2 image-in-dict-row) persist as plain keys across all 5 locales (15× `assertNotIn` total covering all 3 paths × 5 locales).
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.cl-*` skin renders `<html dir="rtl" lang="ar">` authentic with 18 RTL rules · 3576 Arabic characters in body. Authored AR headline `صحتك، عملنا اليومي.` verified rendering on home page after browser walk.
- **Benessere (`wellness`) + Famiglia (`family`) explicitly NOT enrolled** — **DUAL-OUT GUARD** inside `test_a16_salute_archetype_registered` asserts BOTH `wellness` + `family` NOT in `_ARCHETYPE_SCHEMAS` NOR in `_MULTILOCALE_ENABLED_ARCHETYPES` + all 14 pre-A.16 archetypes still enrolled. Lifecycle test additionally runs runtime `assertNotIn` for both at start AND end of test (leak check duro 2 archetypes × 2 layers = 4 assertions per phase × 2 phases = 8 total). Wellness-out guard removed in A.16b via `test_a16b_benessere_out_guard_was_removed_from_salute_tests` — **5th precedent** del guard removal pattern. Family-out guard removed in A.16c via `test_a16c_family_out_guard_was_removed_from_salute_tests` — **6th precedent**. **First time guard removal pattern applies twice from a single opener** (sub-recipe extends from 1-removal to 2-removal phase).
- **6 pre-existing "unsupported archetype" test fixtures were rotated** from `clinic`/`salute-studio-medico` to `wellness`/`benessere-centro-olistico` (A.16b pending candidate) · keeps fixture set aligned with current outside-gate reality.
- Enrolled via A.16 Session 73 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a16_salute_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched with 3 image path overrides covering scalar top + 2 image-in-dict-row patterns on different pages · 15× `assertNotIn("@<locale>:...")` total · 3-page render verification on home + studio + medici across all 5 public-preview locales · **post-A.16b**: wellness-out guard removed, family-out guard still active at start AND end of test). **Pure 3-file enrollment surface**: schema.py +512 LOC (**sotto** 600-LOC soft guardrail · leaner than initial 500-600 planning estimate · 16 entries senza deep-path) · clinic/_base.html 3 atomic fix · tests.py 13 contract + 1 lifecycle test + DUAL-OUT GUARD planted + OUT fixture rotation to wellness/Benessere. **Three-commit phase** on branch: `10e73c7` schema · `59be682` lifecycle test · `e25b622` merge — zero additional infra fixes required · full mechanical reuse of scalar-top + shallow image-in-dict-row patterns. **Zero touches to `apps/commerce/`** confirmed · boundary architectural re-verified.

**wellness (Benessere) — editable AND multi-locale enrolled (A.16b) · MIDDLE PHASE OF MEDICAL-OTHER 3-PHASE STAGED PROGRESSION · GUARD REMOVAL PATTERN 5th PRECEDENT · FIRST NOVEL SHAPE DEFERRAL (`home.ambients`):**
- **Single template**: `benessere-centro-olistico`. Middle phase between A.16 Salute opener and A.16c Famiglia closer (pending). Distinct skin folder (`medical/wellness/` with `.we-*` prefix · 142 hits — highest of medical-other · 13 mature `html[dir="rtl"]` rules · `_base.html` 655 LOC after atomic fixes). Content-tree overlap ~0% with Salute and Famiglia (beyond chrome) · shared-schema IMPOSSIBILE confirmed Step 0 audit.
- **BOUNDARY EDITOR-VS-CLINIC-ADMIN preserved on second medical-other archetype**: same architectural boundary validated Step-0 in A.16 Salute · `apps/catalog/views.py::LiveTemplateView` still does NOT import from scheduler/booking/patient namespaces · editor edits `template_content_benessere.py` (registry: ritual treatments · therapist portraits · room gallery · packages · calendar labels · hero/copy bands · philosophy pillars). Light guardrail test `test_a16b_benessere_clinic_admin_boundary` mirrors A.16 contract. Same 7-prefix smoke check (`appointment.` · `booking.` · `patient.` · `scheduler.` · `calendar_slot.` · `medical_record.` · `prescription.`). Second medical-other archetype confirms boundary holds uniformly.
- 9 sidebar groups · ~108 scalar fields + **3 scalar top-level images** (`home.hero_image` + `filosofia.photo_image` + `contatti.map_image` · all rendered) + **3 image-in-dict-row lists**:
  - **home**: `therapists_trio` dict 3×(name/role/bio/**portrait**) — 3 RENDERED operator portraits
  - **ambienti (novel `gallery` kind)**: `rooms` dict 8×(span/tag/title/sub/**image**) — 8 RENDERED room images (largest image list · skin uses both `background-image` + `data-li-src` lightbox attribute · dual-render pattern documented)
  - **professionisti**: `people` dict 5×(name/role/bio/quote/**portrait**) — 5 RENDERED full-page professional portraits
- **Total editable image surface: 19** (3 scalar top + 16 image-in-dict-row cells · ALL RENDERED · editorial olistico skin · no storage-only split).
- ~90 translatable fields + ~370 global fields per-template sidebar rendering (walk-verified: 379 total editable fields · 19 image widgets exactly · 27 group slots = 9 sidebar + 17 indexed + 1 design · 5 lang pills).
- 17 readonly indexed list entries in STRUCTURED_FIELD_SHAPES · **tutti parent-level · ZERO deep-path** (13 dict + 4 tuple · mid-complexity between Bottega 14 and Brace 30).
- **1 novel page kind** enrolled: `gallery` (ambienti page · plain string identifier · no dispatch) + shared `appointment` kind with Salute.
- **Scheduler-state bool flags OUT col-level** (4 paths · Luxe `available` + Salute `is_popular` precedent re-application): `home.calendar[].has_slots` + `.soldout` + `prenota.calendar[].has_slots` + `.soldout`. Bool field type not added (horizontal feature resisted).
- **Calendar `slots` nested list-of-str OUT col-level** (2 paths · Juris precedent): `home.calendar[].slots` + `prenota.calendar[].slots` (concrete time-slot arrays like `['10:00','14:30','17:00']` or `['silenzio']`).
- **Calendar `day`/`num`/`month` IN col-level** (6 paths · 6th archetype precedent): visible editorial calendar labels ('Lun'/'14'/'Apr' text · customer-editable editorial content vs scheduler state).
- **Stringent IN/OUT call on "technical-looking" fields** per user Step 0 guidance (audit-driven · 6th archetype precedent chain after Sapore/Brace/Bottega/Luxe/Salute):
  - **IN** (editorial visible · customer-facing): calendar `day`/`num`/`month` × 2 lists · `home.journey[].num` ('01'/'02'/'03'/'04' visible step numbering) · `filosofia.pillars[].init` ('A'/'B'/'C' editorial typographic device) · `rituali.packages[].tag` ('Giornata singola' · 'Tre giorni' editorial category badges)
  - **OUT col-level** (scheduler-state/structural/technical): `has_slots`/`soldout` bool × 4 · `slots` nested str-list × 2 · `includes`/`tags`/`interest_options` nested str-list × 3
- **Complex shapes explicitly outside perimeter** (~24 rejected paths): 4× flat list-of-str (`site.hours_footer_rows` · `home.hero_meta` · `home.press` · `prenota.why`) + 3× nested list-of-str inside dict rows (`rituali.packages[].includes` · `professionisti.people[].tags` · `contatti.form_fields.interest_options` · Juris precedent) + 5× form structures (`contatti.form_placeholders` · `contatti.form_helpers` · `contatti.form_fields` · `prenota.form_fields` · `prenota.form_sections` · Juris/Gusto/Bottega/Luxe/Salute precedent) + 4× bool flag + 2× slots + 3× home.ambients (DEFERRED) + `pages` + `posts` (empty · same structural absence as Salute/Bottega/Luxe/Sapore/Brace · detail-page policy stays at 6-archetype uniform enforcement count).
- **NOVEL SHAPE DEFERRED** (first-ever deferral outcome · 4th deferral category): `home.ambients` tuple-with-image (4 × `(image_url, title, sub)` positional tuple with image as first element). **ZERO precedent in any existing archetype** — all prior tuple shapes across 15 enrolled archetypes carry text-only cols. Whole list OUT first-wave via schema omission · `validate_key_path("wellness", "home.ambients")` raises `InvalidEditableField` · mechanical-reuse principle preserved · no horizontal-feature introduction. Future expansion candidate after dedicated infra verification (`services._resolve_path` + `schema._iter_indexed_groups` + `rendering._apply_indexed` + widget-level render test for image-type in tuple col).
- **Image overrides stay global/plain-keyed** — lifecycle test verifies 3 image paths (1 scalar top + 2 image-in-dict-row) persist as plain keys across all 5 locales (15× `assertNotIn` total covering all 3 paths × 5 locales).
- `supported_locales=["it","en","fr","es","ar"]` · identical UX surface. AR preview on `.we-*` skin renders `<html dir="rtl" lang="ar">` authentic with 13 RTL rules · 3033 Arabic characters in body. Authored AR headline `النَّفَسُ هو مقياس وقتنا` verified rendering on home page after browser walk.
- **Famiglia (`family`) explicitly NOT enrolled** — **FAMILY-OUT GUARD preserved unchanged** inside `test_a16_salute_archetype_registered` asserts `family NOT in _ARCHETYPE_SCHEMAS NOR in _MULTILOCALE_ENABLED_ARCHETYPES` + lifecycle test runtime `assertNotIn` at start AND end of test. Wellness-out guard was REMOVED in A.16b via `test_a16b_benessere_out_guard_was_removed_from_salute_tests` (5th precedent · symmetric inversion). Family-out guard will be removed in A.16c via `test_a16c_family_out_guard_was_removed_from_salute_tests` (6th precedent · closes medical-other family).
- **6 pre-existing "unsupported archetype" test fixtures were rotated** from `wellness`/`benessere-centro-olistico` to `family`/`famiglia-pediatria` (A.16c closer candidate) · keeps fixture set aligned with current outside-gate reality.
- Enrolled via A.16b Session 74 (combined A.6 schema register + A.7b gate flip in a single phase, with `test_a16b_benessere_full_multilocale_lifecycle_end_to_end` as the dedicated lifecycle regression test — enriched with 3 image path overrides across 3 DISTINCT pages: scalar `home.hero_image` on home + `ambienti.rooms.0.image` on novel gallery page + `professionisti.people.0.portrait` on team page · 15× `assertNotIn("@<locale>:...")` total · 3-page render verification on all 5 public-preview locales · TRIPLE invariant Benessere + Salute IN + Famiglia OUT at start AND end). **Pure 3-file enrollment surface**: schema.py +559 LOC (**sotto** 600-LOC soft guardrail · consistent with Bottega 585 · Luxe 598 · Salute 512) · wellness/_base.html 3 atomic fix · tests.py 15 contract + 1 lifecycle test + wellness-out guard REMOVED from 3 A.16 Salute locations + family-out guard PRESERVED + OUT fixture rotation to family/Famiglia. **Three-commit phase** on branch: `f1747b7` schema · `4574efb` lifecycle test · `e9cc419` merge — zero additional infra fixes required · full mechanical reuse of scalar-top + shallow image-in-dict-row patterns. **Zero touches to `apps/commerce/`** confirmed · boundary architectural re-verified.

### What is operator-only

- `python manage.py gc_project_assets` (default dry-run, `--apply`, `--project=<uuid>`, `--grace=<hours>`) — removes ProjectAsset rows + files no longer referenced by any live override or publish snapshot. Not scheduled. Not auto-triggered. Manual only per D-094.

### Recipe for adding multi-locale to a new archetype (A.7 playbook)

1. Add the archetype slug to `_MULTILOCALE_ENABLED_ARCHETYPES` in `apps/editor/schema.py`. No migration needed — the `@<locale>:<path>` storage convention is self-describing.
2. Write a regression test mirroring `test_a7_step4_vertex_full_multilocale_lifecycle_end_to_end` (HTTP-level: IT/EN/FR autosave → publish → 5-locale public preview → owner reopen per locale → zero cross-locale leak).
3. Browser walk validating IT ↔ EN ↔ FR ↔ AR RTL preview + flush-before-switch.
4. Merge via `--no-ff`. Catalog → N/8 archetypes multi-locale.
5. Total: ~3 commits (schema flip + lifecycle test + walk-validated merge).

### Recipe for adding a new editor archetype (A.6 playbook)

See A.6 commits `a7177f5` · `9540d5a` · `4b9376c`. 5 contract tests + schema registration (`_ARCHETYPE_SCHEMAS` + `_ARCHETYPE_BASELINE_TEMPLATE` + `STRUCTURED_FIELD_SHAPES`) + `_base.html` preview bridge + 2 lifecycle tests. Merge into v15 via `--no-ff`.

### Binding decisions added through Phase A.7

- **D-096** — Per-locale override storage convention: translatable rows use `@<locale>:<path>` prefix, globals keep plain path. Zero schema migration, zero new table.
- **D-097** — No cross-locale customer fallback: locale L rendering with no `@L:<path>` row falls back to authored registry value for locale L, NEVER to another locale's customer override.
- **D-098** — Archetype gate for multi-locale editor: `_MULTILOCALE_ENABLED_ARCHETYPES` in `apps/editor/schema.py` is the single source of truth. A.7 first wave enrolls only `agency-creative-studio` (Vertex). Each enrollment requires its own lifecycle regression test.

All prior D-086 through D-095 (A.1 → A.5 bindings) and pre-editor decisions (D-054 premium law, D-055 tier model, D-047 chrome authoring, etc.) remain in force. See DECISIONS.md for full catalogue.

### Phase A.16c+ — candidates (medical-other STILL HALF-OPEN · Famiglia chiude family A.16c)

Pick one when the next workstream opens. A.16b enters medical-other as middle phase · still half-open · 1 sibling pending. Residue is 3 editor-only-pending templates across 3 families (1 family half-open):
- **medical-other half-open** (1 template · `family` Famiglia · pending A.16c closer)
- **agency-secondary** (1 template · `agency-digital-studio` Aura)
- **startup-saas** (1 template · `startup-saas-landing` Elevate)

Recommended framing: **A.16c Famiglia (`family`) Step-0 planning session** — closes the family-out guard (6th precedent of guard removal pattern) and the entire medical-other family · brings catalog to 17 archetype slugs / 18 templates editable / 7 families closed. Half-open family is stronger ROI than opening a new front. Step-0 audit needed for: **deep-path tuple-in-dict-list `crescita.topics[].items`** (Sapore-precedent shape · 4 × list-of-tuple `(question, answer)` · mechanical reuse of `f66ac24` contract-alignment fix · Brace precedent for dict-in-dict-list handles list parent walk) · novel `faq` page kind (plain string identifier · no dispatch) · NO form_fields list-of-dict (form exposed as flat scalars · simpler OUT policy than Benessere) · 16 image surfaces (3 scalar + 13 image-in-dict-row across 3 lists) · `home.gallery[].src` + `.cap` shape (image col `src` + scalar caption). Expected schema LOC ~600-700 (higher than Benessere due to deep-path shape entries · possible exception over 600-LOC soft guardrail acceptable · Sapore precedent was +663 LOC for similar shape). Outside-gate fixture already rotated to `family`/`famiglia-pediatria` in A.16b as next candidate signal.

Alternatives: Aura individual enrollment (closes agency-secondary · pulls focus away from medical-other half-open · only justifiable if customer signal surfaces) · Elevate individual enrollment (same trade-off as Aura) · MEMORY.md maintenance mini-phase remains queued as a separate housekeeping task (auto-memory index ~34-35KB sopra warning-soglia 24.4KB · grows ~1KB per enrollment phase · 17 phases A.6→A.16b accumulated) · `home.ambients` tuple-with-image widening mini-phase (deferred novel shape from A.16b · low value · customer-signal-gated).

See `TODO_NEXT.md` for full candidate list + red-lamps + "do NOT open" list.

### Things that are not debt but look like it

- Per-group badges don't pre-sync at mount with persisted overrides; they start at 0 and catch up on the next autosave. Customer-cosmetic only.
- Reopen editor always starts the iframe on `home`, not on the page the customer last viewed. `PENDING_PAGE_KEY` sessionStorage hint is one-shot for row-op reloads only, by design.
- Orphan assets accumulate until an operator runs `gc_project_assets --apply`. This is D-094 behaviour, not neglect.
- Plain-keyed overrides on translatable paths (legacy pre-A.7 shape) still apply cross-locale until superseded by a `@L:` row. This is backward-compat, not a fallback — current production has no such rows because A.7 writes always go through the prefixed key.
- Editor chrome (sidebar, accordion, input widgets) is LTR-only even when editing AR. The preview iframe renders RTL authentic; the editor shell is an operator tool where browser bidi handles AR input natively. D-098 scope exclusion, not a gap.

---

## Session 57 — Phase A.2 Editor UX + Live Preview: Read This Before Touching The Editor, Autosave, `?baseline=1`, or the Preview-Bridge Injection (2026-04-16)

**What changed in Session 57.** The A.1b editor (server-form POST with 520px narrow sidebar) is rebuilt as a premium standalone app shell. Debounced JSON autosave (400ms) on `POST /projects/<uuid>/autosave/`. Explicit-only revisions via `POST /projects/<uuid>/snapshot/`. `?baseline=1` on `LiveTemplateView` short-circuits the project overlay for the before/after compare slider. `preview-bridge.js` (injected behind `{% if preview_project %}`) listens for `window.postMessage` and paints an amber region ring on hover/focus of any sidebar field. Schema widened on Vertex: 4 flat groups → 14 themed groups with `icon` + `region` metadata, ~39 editable fields (was 23). 20/20 project tests + full Playwright walk green.

### What's binding (D-088)

1. **Autosave is the customer-UI mutation path.** Any new field type must be serialisable into the JSON autosave payload `{content:{}, tokens:{}}`. No per-field form POSTs. The legacy `POST /editor/` form path was rewired to proxy to `project_snapshot` — a safety net, not an active path.
2. **Revisions are explicit-only.** Autosave NEVER creates a revision. Only `Salva versione` (button → `project_snapshot`) and `Pubblica` / `Sposta in bozza` create revisions. Don't regress this — it's why cronologia stays useful.
3. **Baseline preview is `?baseline=1`.** Don't refactor into post-render diffing. `LiveTemplateView.setup` reads the flag and sets `preview_project = None`; the same skin renders the baseline deterministically.
4. **`preview-bridge.js` is conditional.** Currently injected in `templates/live_templates/agency/agency-creative-studio/_base.html` behind `{% if preview_project %}`. When opening the editor to a second archetype (Phase A.3), add the same conditional include to that archetype's `_base.html`. The baseline iframe must stay bridge-less for the compare to stay deterministic.
5. **Schema groups MUST declare `icon` + `region`.** Bootstrap Icons class for `icon`; CSS selector (scoped to the archetype's skin) for `region`. Groups without these still render but without sidebar icons / without highlight. Don't ship a second archetype's schema without them.
6. **Editor shell is standalone.** `templates/projects/project_editor.html` is NOT extending `base.html`. It loads its own fonts (Inter + JetBrains Mono + Bootstrap Icons), `live-editor.css`, `live-editor.js`. No marketing navbar/footer. No Bootstrap CSS bundle.
7. **Editor does NOT render Django messages.** Autosave flow is silent JSON (chip + optional toast). `customize_start` uses `request.session["editor_just_created"]` for a one-shot welcome banner. Publish / unpublish flashes exist in the session but are discarded silently on the redirect — the topbar tier chip's colour change is the visible signal. Adding a `{% for m in messages %}` block to the editor shell reopens the stacking bug the customer reported.
8. **Prefetch-cache bypass.** Any `.count()` on `project.content_overrides` called AFTER a mutation must go through a fresh queryset (`ProjectContent.objects.filter(project=project).count()`), because the selector's `prefetch_related` caches pre-save state. Parallel to D-086 Session 55's `_build_snapshot` bug.

### Phase A.3 immediate next step

- Schema field type `"list"` + UI repeater widget (add / remove / reorder / per-item validation). Target: `home.ledger_rows` + `home.capab_items` on Vertex.
- Add `apps.editor.schema` entries for a second archetype — `clinic` (Salute) or `corporate-suite` (Pragma). MUST declare `icon` + `region` per group. Remove those slugs' equivalents from `LOCKED_KEYS_NOTE` if they become editable. Opens editor to 5/20 templates.
- Remember to add `{% if preview_project %}<script>...preview-bridge.js</script>{% endif %}` to the new archetype's `_base.html`.
- Regression: verify `customize_start` still bounces the other 18 non-editable templates cleanly after A.3 lands.
- Deferred polish from A.2: sync baseline iframe scroll to edited iframe on compare-open · replace archetype-specific `region` selectors with a shared `data-mw-region="hero"` attribute pattern · add toast-on-publish / toast-on-unpublish in the editor shell.

---

## Session 56 — Phase A.1b Public Customize Flow: Read This Before Touching Auth, `/projects/start/`, Navbar, or Detail-Page CTAs (2026-04-16)

**What changed in Session 56.** Customer-facing flow is now real. A user goes: `/templates/` → click `Personalizza` on a card or detail page → `/account/login/` or `/account/signup/` if anon → after auth, `/projects/start/?template=<slug>` does get-or-create and drops them in the editor. Second click reopens the same draft. Logout/login preserves `?next=`. Preview iframe renders (X-Frame-Options SAMEORIGIN applied to `LiveTemplateView` only). 24/24 tests + 834/834 catalog smoke green. Editor schema UNCHANGED — zero field/archetype growth.

### What's binding (D-087)

1. **Single start URL.** `customize_start` at `/projects/start/?template=<slug>` is the only public customize entry. Every new CTA that wants to launch the editor links here. **Do NOT** add `/customize/`, `/editor/start/`, or variant URLs — the decorators, the analytics hooks, and the login-next chain will only follow one path.
2. **Anon bounces to `/account/login/` (NOT `/admin/login/`).** `LOGIN_URL` in settings is the single source of truth; don't hard-code login URLs anywhere else.
3. **`?next=` round-trip.** Both `customer_signup` and `CustomerLoginView` thread the originating URL through the switch-between-them link. Preserve this on any future auth-surface change — a customer clicking `Personalizza` must come back to the same template after signup, even if they switch to login mid-way.
4. **One draft per `(owner, template)`.** `get_or_create_project_for_template` returns the most recent existing project for the pair before creating. Keep this constraint until a dashboard UX exists that can disambiguate multiple drafts.
5. **Unsupported archetypes bounce honestly.** When a template's archetype is not in `_ARCHETYPE_SCHEMAS`, `customize_start` redirects to the template detail page with an info message. Never "fake" an editor for an unsupported archetype.
6. **X-Frame-Options per view.** Keep `SAMEORIGIN` opt-in only on `LiveTemplateView`. Do not set `X_FRAME_OPTIONS = "SAMEORIGIN"` project-wide — clickjacking protection stays `DENY` for every other surface.
7. **Don't conflate the `/projects/new/` POST with `customize_start`.** `project_create` (POST form on `/projects/` dashboard) still exists for power-user flow that wants a custom name. It's wrapped in a `<details>` on the list page. Keep both paths; they have different UX signals.

### Phase A.2 immediate next step

Add a second archetype to `apps.editor.schema` (recommend `clinic` for Salute) + build `list` field type for repeaters. **Integration checkpoint:** after adding the archetype, visit `/templates/medico/salute-studio-medico/` and click `Personalizza` — the bounce-to-detail branch of `customize_start` must continue to fire for every non-editable archetype. A naïve `is_supported_archetype()` addition can accidentally "open" archetypes without their schema being complete. Re-run the Phase A.1b browser walk (step 3 especially) against the new surface.

### Files to know

- `apps/accounts/forms.py · views.py · urls.py · tests.py` — customer auth. Templates at `templates/accounts/{login,signup}.html`.
- `apps/projects/views.py :: customize_start` — the single public entry.
- `apps/projects/services.py :: get_or_create_project_for_template` — one-draft-per-template.
- `apps/catalog/views.py :: LiveTemplateView` — the `@xframe_options_sameorigin` decorator on `dispatch`.
- `marketweb/settings.py :: LOGIN_URL` — `/account/login/` (not `/admin/login/`).
- `templates/includes/_navbar.html · _template_card.html` + `templates/catalog/template_detail.html` — the 3 surfaces that wire `Personalizza`.

---

## Session 55 — Editor Foundation v1: Read This Before Touching `apps/projects/`, `apps/editor/`, `LiveTemplateView`, or Any Editor Surface (2026-04-16)

**What changed in Session 55.** `apps/projects/` + `apps/editor/` went from empty scaffolds to working modules. The editor ships a real vertical slice for ONE archetype (`agency-creative-studio`, slug `vertex-creative-agency`): customer logs in, derives a project, edits 23 content fields + 5 design tokens, saves with sparse-diff semantics, sees a live iframe overlay preview, publishes, and revises. 12/12 unit tests + 834/834 catalog smoke green. No skin files, no content registries, no DNA entries touched.

### What's binding (D-086)

1. **Overlay pipeline, not parallel routes.** Project preview is the existing `/templates/<cat>/<slug>/preview/<page>/` URL extended with `?project=<uuid>`. `LiveTemplateView.setup()` detects it + calls `selectors.get_project_for_preview()` + stores `self.preview_project`. `get_context_data()` calls `apply_project_overrides()` which deep-merges content + tokens onto the baseline. **Do NOT** introduce a second `/projects/<uuid>/preview/<page>/` route to "clean up" URLs — that would require touching every skin's hardcoded `{% url 'catalog:live_template_*' %}` tags. The overlay is the contract.

2. **Sparse-diff storage, not snapshot.** `ProjectContent` rows are per-key. A POST whose value equals the baseline auto-deletes the override row. This lets upstream registry polish flow through to the customer for free. **Do NOT** regress to a single JSONField full-state snapshot on `CustomerProject` — that breaks the blueprint's read-path model (EDITOR_SCHEMA_BLUEPRINT §7).

3. **Archetype whitelist is explicit.** `apps.editor.schema._ARCHETYPE_SCHEMAS` maps archetype → editable-fields list. Only archetypes with an entry can seed a project (`services.create_project_from_template()` raises `UnsupportedTemplate` otherwise). Foundation v1 has ONE entry — `agency-creative-studio`. Opening a second archetype in Phase A.2 = author its schema entry first, don't "let it through and see what breaks".

4. **DNA-lock at service layer, not UI.** `validate_key_path()` raises `InvalidEditableField` on any non-whitelisted key. UI already hides locked fields, but a crafted POST with `content__home.capab_items=hack` is rejected by the service. Preserve both layers — removing either weakens the contract.

5. **Snapshot queries fresh.** `_build_snapshot()` in `apps.projects.services` uses `ProjectContent.objects.filter(project=project)` + `ProjectDesignTokens.objects.get(project=project)` — NOT `project.content_overrides.all()`. The view's prefetched cache freezes the pre-save state. A regression test (`test_snapshot_reflects_post_save_state`) catches a relapse.

6. **Publish visibility contract.** `selectors.get_project_for_preview()`: draft = owner OR staff only; published = any authenticated user; template slug mismatch → None. Share tokens / unlisted-public projects are deferred to Phase B — **do NOT** silently open drafts to anonymous users.

7. **LOGIN_URL is `/admin/login/`.** A branded login page is Phase A scaffolding. Editor routes redirect anonymous users to admin login. **Do NOT** mark project routes public — they require authentication.

8. **Iframe preview reload via `?_t=<ms>` cache-bust.** After a save the redirect re-renders the editor, and the GET-side script in `project_editor.html` appends `_t=<Date.now()>` to the iframe src. This is a simple non-JS-state cache busting pattern. **Do NOT** replace with a polling loop or WebSocket for Foundation v1 — SPA is Phase A.8+.

### Do NOT do in a follow-up session without revisiting D-086

- **Do NOT author new archetypes (`apps.editor.schema`) without an explicit scope entry in TODO_NEXT.** Phase A.2 plans one archetype addition (recommend `clinic` or `corporate-suite`). Two in one session is scope creep.
- **Do NOT** modify any existing skin file (`templates/live_templates/<cat>/<arch>/*.html`) for Foundation v1. Foundation v1 is proven additive — the moment a skin changes, regression surface explodes.
- **Do NOT** touch `apps/catalog/template_content*.py` files. The registry is baseline; overrides are project-side.
- **Do NOT** collapse `ProjectContent` into a JSONField on `CustomerProject` "for simplicity". Per-row storage is the foundation for future revision diffing + the Phase A.3 multi-locale column.
- **Do NOT** remove the `LOCKED_KEYS_NOTE` read-only panel from the editor UI. It's the human-facing half of the DNA-lock contract — hiding both the controls AND the explanation removes the teaching surface.
- **Do NOT** persist `?project=<uuid>` into nav links inside any skin `_base.html`. Clicking a nav link inside the iframe exits project mode by design; this is acceptable Foundation v1 behavior. Phase A.2 addresses in-template navigation persistence via a custom template tag.
- **Do NOT** translate `CURATED_FONTS` into a dynamic query from `template_dna.py`. The whitelist is intentional — arbitrary Google Fonts break D-040 font-miss regression.
- **Do NOT** relax `InvalidEditableField` on unknown keys. Silently ignoring unknown key_paths is the same as relaxing the DNA-lock.

### Phase A.2 acceptance gates (for the next session)

1. One additional archetype shipped in `apps.editor.schema` with 15+ editable fields across 3+ groups.
2. Repeater widget groundwork: `"list"` field type in the schema + UI + services layer. Exercise on at least one list field (Vertex `home.ledger_rows` or Salute `home.services`).
3. `python manage.py test` stays at 12+ green (new tests land for the new archetype + the list widget).
4. `smoke_full.py` stays at 834/834.
5. A second slug (e.g. `salute-studio-medico` or `pragma-corporate-suite`) renders a personalised overlay at `/templates/<cat>/<slug>/preview/?project=<uuid>` with at least 10 distinct field overrides applied.

### What to verify BEFORE any Phase A.2 slice opens

- `python manage.py check` → 0 issues
- `python manage.py test apps.projects` → 12+ green
- `python smoke_full.py` → 834/834
- Browser walk: `/projects/` dashboard loads with the existing Vertex entry, the editor page renders all 4 content groups + 5 token fields + DNA-lock note + recent revisions, the iframe preview overlays edits, publish/unpublish transitions work.

---

Last updated: 2026-04-15 — after **Session 54 Catalog Expansion Strategy + Profession Preset Taxonomy**

## Session 54 — Strategy Session: Read This Before Proposing Any New Template, Archetype, Category, or Preset (2026-04-15)

**What changed in Session 54.** No code, no template, no skin folder. **Strategy-only session.** Three deliverables landed:
1. `CATALOG_EXPANSION_STRATEGY.md` — 11-section blueprint covering audit, taxonomy, 4-level model, archetype matrix, preset framework, DNA-locked vs editable matrix, editor strategy, rollout roadmap, numerical proposal, final decision.
2. `PROFESSION_PRESET_TAXONOMY.md` — concrete registry of ~75-90 profession presets across 14-16 categories, mapped to archetypes (19 existing + 11 new).
3. Coordinated updates to `CATEGORY_ROADMAP.md`, `TODO_NEXT.md`, `DECISIONS.md` (D-083 / D-084 / D-085), `AGENT_HANDOFF.md`, `SESSION_LOG.md`, `MEMORY.md`.

**Catalog state UNCHANGED after Session 54: 20/20 published_live.** Strategy session does not flip tiers or modify templates.

### What's binding (D-083 + D-084 + D-085)

1. **D-085 — Editor-First Sequencing is the next workstream.** Phase A (Editor Foundation v1) is the next phase. **NO new template, archetype, category, or preset gets opened until Phase A is closed.** This is hard, not advisory. Proposals to "just add one more template" must be refused.

2. **D-084 — 14 categorie top-level medio termine.** Le 8 MVP esistenti restano invariate (`medical · restaurant · business · agency · lawyer · real-estate · portfolio · ecommerce`); 6 nuove si aggiungono in Phase B-F (`hospitality · food-retail · automotive · trades · beauty · wellness-fit · professional · education · events` — totale 9 nuove se si conta `events` aperta in Phase F, sono 17 se si conta tutte le opzionali; il numero 14 è il **medio termine binding**, le restanti 3 sono opzionali).

3. **D-083 — Modello a 4 livelli (Categoria → Archetipo → Preset → Editor)** è la struttura vincolante. Non si aprono "categorie per ogni mestiere". Non si fanno "template completamente nuovi per ogni mestiere". Si fanno **preset professionali sopra archetipi riusati**.

4. **I 20 template `published_live` esistenti restano "template autoriali" (livello 3 con `profession_preset` vuoto)** — invariati, mai retrofittati a preset. Polish/security/a11y/mobile-audit ammessi; rewrite NO.

5. **Editor v1 NON deve sapere dei preset.** Editor v1 modifica `CustomerProject`. Il `CustomerProject` viene creato da un seed (template autoriale o, in Phase B+, preset). L'editor non sa se il seed era preset o template — lavora sul project. Quando i preset cresceranno, basta aggiungerne nel registry; l'editor non cambia.

6. **Phase A sub-phasing è in `TODO_NEXT.md`.** A.1 (models) → A.2 (renderer overlay) → A.3 (UI form-based) → A.4 (preset library) → A.5 (validators) → A.6 (image upload) → A.7 (locale UI) → A.8 (smoke). Stima ~14-23 sessioni / 2-3 mesi.

7. **Phase B (Trades + Local Food Retail)** è la prima ondata post-MVP. Sequenza fissa: B → C → D → E → F → G. NO salti, NO sostituzioni di phase.

### Do NOT do in a follow-up session

- **Do NOT propose a new template or archetype** until Phase A.8 is verde. Anche se "sembrerebbe veloce", anche se "ci sarebbe domanda". Il blocco è binding.
- **Do NOT touch the 20 published_live templates** salvo per polish/security/a11y/mobile-audit. NO rewrite. NO retrofit a preset.
- **Do NOT open new categories** before Phase A. La categoria `trades` esisterà solo quando Phase A è chiusa e Phase B inizia.
- **Do NOT translate the profession-preset taxonomy** (PROFESSION_PRESET_TAXONOMY.md) into actual content tree files yet. Quel documento è blueprint, non implementazione. I content tree dei preset si scrivono solo in Phase B-F.
- **Do NOT machine-translate any preset content seed** quando arriverà il momento. Native voice per locale rimane non-negotiable per i preset autoriali.
- **Do NOT skip the `EDITOR_SCHEMA_BLUEPRINT.md` contract.** Phase A implementa quel contratto. Se vuoi cambiare lo schema, prima aggiorna D-064 + EDITOR_SCHEMA_BLUEPRINT.md, poi implementi.
- **Do NOT collassare livelli** (es. "facciamo categoria=preset" o "facciamo template=preset"). Il modello a 4 livelli è binding per scaling sostenibile.

### What to verify BEFORE opening Phase A

- `EDITOR_SCHEMA_BLUEPRINT.md` letto integralmente (~478 LOC).
- `CATALOG_EXPANSION_STRATEGY.md` §4 (modello strutturale) + §7 (DNA-locked vs editable) + §8 (editor strategy) letti.
- `PROFESSION_PRESET_TAXONOMY.md` §1 (anatomia preset) letto — anche se Phase A non implementa preset, il design dell'editor deve essere compatibile.
- Verificare che `apps/editor/` esista come directory ma non abbia codice (vedi `ARCHITECTURE.md` §`editor`).
- Decidere persistenza: SQLite per dev, PostgreSQL per produzione (già scelto). Le migrations Phase A.1 sono additivi.
- Stripe + commerce v2 sono già operativi (D-076, Session 45). Editor v1 NON tocca commerce. Customer project Stripe domain mapping arriva in Phase G (D-085 sequenza).

### When Phase A closes (acceptance gates)

Editor v1 in produzione + tutti i 20 `published_live` clonabili + un test interno completo (clone → edit → publish) verde + smoke harness + zero regression. Solo allora si apre Phase B.

---

Last updated: 2026-04-15 — after **Session 53 Lawyer + Real-Estate Live Rollout · CATALOG COMPLETE 20/20**

## Session 53 — CATALOG COMPLETE 20/20 · Read This Before Touching Any Lawyer / Real-Estate Skin, Lex/Juris/Casa/Villa Content, or the 4 New Pexels Pools (2026-04-15)

**What changed in Session 53.** Phase 2g3.7 closed. Catalog now **20/20 published_live**. Lex (`lex-studio-legale`, classic-gold archetype — Studio Legale Ferri, Roma, forensic-notarile), Juris (`juris-avvocato-moderno`, modern-transparent — Avv. Martini & Partners, Milano, advisory-modern tech boutique), Casa (`casa-agenzia-immobiliare`, mass-market — Domus Immobiliare, Milano+Torino, market-approachable), Villa (`villa-immobili-lusso`, ultra-luxury-cinematic — Villa Prestige, Milano+Portofino, editorial-concierge) have been authored from line one with full multipage live skins (6-8 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, Pexels-curated imagery pools, and sharp D-054 differentiation. **Phase 3 unblock gate MET.**

### What's binding (D-082)

1. **4 new reusable archetypes.** `classic-gold` (forensic-notarile ink+gold studio legale institutional) · `modern-transparent` (advisory-modern slate+blue tech-forward boutique) · `mass-market` (market-approachable navy+emerald+orange residential daylight) · `ultra-luxury-cinematic` (editorial-concierge black+champagne private-advisory). Any future lawyer or real-estate sibling can ship with ONLY a seed row + DNA entry + content block + 5 locale trees. **Zero new HTML per archetype.**

2. **D-054 10-gate matrix passes on every sibling pair, bidirectional.**
   - Lex ↔ Juris: fonts (Cormorant serif ↔ DM Sans sans), palette (ink+gold+bordeaux ↔ slate+blue+yellow), hero silhouette (split-ledger ↔ centered-manifesto), conversion (private-consultation ↔ strategy-call), heritage (1962 ↔ 2018).
   - Casa ↔ Villa: fonts (Poppins ↔ Cormorant), palette (daylight navy+emerald+orange ↔ black+champagne+white), hero (search-widget ↔ fullbleed editorial cover), cards (tile-specs ↔ dossier), geography (Italian urban ↔ Continental), price visibility (visible ↔ hidden), conversion (viewing-request ↔ private-viewing + NDA).
   - Lex/Juris ↔ Pragma/Elevate: no overlap in font pairings, imagery pools, or conversion vocabulary.
   - Casa/Villa ↔ Bottega/Luxe: different page kinds (no shop/cart/PDP), different card vocabularies, different conversion verbs.
   - Villa ↔ Luxe: despite shared Cormorant+dark-champagne DNA, Villa is real-estate advisory (property dossiers, NDA, concierge) while Luxe is fashion ecommerce (atelier, lookbook, stylist).

3. **D-047 chrome-cleanliness from line one.** All 32 new HTML skin files (`lawyer/classic-gold/` 8 + `lawyer/modern-transparent/` 8 + `real-estate/mass-market/` 8 + `real-estate/ultra-luxury-cinematic/` 8) + 4 preview compositions carry zero brand literals — every visible string flows from `{{ page_data.* }}` / `{{ site.* }}` / `{{ chrome.* }}` / `{{ dna.content.* }}` / `{% for %}` loops.

4. **`html[dir="rtl"]` CSS block + conditional Noto Naskh/Kufi/Amiri Arabic font load on all 4 bases.** Latin proper names (Studio Legale Ferri, Avv. Prof. Alberto Ferri, Avv. Giorgia Martini, Domus Immobiliare, Villa Prestige, Alessandra Visconti di Modrone, Via Piemonte 39, Via Solferino 40, all 14 lawyer names, 9 agent names, 4 private advisor names, street addresses, property names Villa Aurelia/Castello di Monterò/Penthouse Quadronno/Mas de la Mer, territory labels Portofino/Chianti/Costa Smeralda/Saint-Tropez/Capri/Val d'Orcia, publication names) preserved verbatim across all non-IT locales. Arabic numerals stay Latin (unicode-bidi: isolate per skin RTL block).

5. **Native voice per locale.** Lex EN reads as Slaughter-and-May, FR as Gide/Bredin Prat cabinet, ES as Garrigues despacho, AR as Al Tamimi MENA MSA institutional. Juris EN as Kirkland Startups/Orrick/Gunderson Dettmer, FR as Bredin Prat VC, ES as Cuatrecasas Startups, AR as Al Tamimi tech desk. Casa EN as Foxtons/Knight Frank, FR as Barnes/Century 21, ES as Engel & Völkers Spain retail, AR as Emirates Living/Better Homes. Villa EN as FT How to Spend It/Monocle Estates/Sotheby's, FR as Le Figaro Propriétés/Emile Garcin, ES as Vanity Fair Spain/Savills España, AR as Robb Report ME/Esquire ME editorial literary. Structural parity verified — same key paths at every level across all 5 locales.

6. **Page slugs stay Italian (URL-canonical).** Lex: home/studio/pratiche/avvocati/notabili/contatti. Juris: home/approccio/servizi/settori/insights/contatti. Casa: home/immobili/quartieri/agenzia/valutazione/contatti. Villa: home/collezione/territorio/studio/esperienza/concierge. Only `label` fields change per locale.

7. **Pexels primary imagery, 4 disjoint pools.** `lawyer-classic` (heritage ink), `lawyer-modern` (bright collaborative), `realestate-casa` (daylight attainable), `realestate-villa` (golden-hour rarefied). 6 URLs per pool, zero overlap across pools.

8. **D-081 dynamic counter policy — Lex/Juris/Casa/Villa all compliant.** Stats bands carry `data-lm="counter"` on every numeric span; "Prezzo su richiesta" on Villa stays static per editorial-tone exception.

9. **Page-kind choices (reference for future real-estate siblings):** Casa uses `project_list`/`project_detail` for immobili listings + details. Villa uses `blog_list`/`blog_detail` for collezione dossiers + property detail. Both use the same LiveTemplateView `_list→_detail` plumbing. The choice between the two is semantic, not structural.

10. **CHROME_I18N extensions.** `mp_other_lawyer` + `mp_other_realestate` added across all 5 locales. Future category additions should follow the same pattern.

### Do NOT do in a follow-up session without revisiting D-082 + CLAUDE.md

- **Do NOT add a 5th lawyer or 3rd real-estate template without checking archetype fit.** If it's "like Lex but Napoli", reuse `classic-gold/` skin. If "like Casa but Roma", reuse `mass-market/` skin. If "like Villa but Costa Smeralda", reuse `ultra-luxury-cinematic/` skin. NEVER duplicate a skin folder; extend the content registry.
- **Do NOT machine-translate legal terminology or real-estate vocabulary.** Use the native register per locale (codici italian references must keep the Italian anchor with native gloss: `Art. 2343 c.c.` → EN `Section 2343 of the Italian Civil Code` → FR `Art. 2343 du Code civil italien` → ES `Art. 2343 del Código Civil italiano` → AR `المادة 2343 من القانون المدني الإيطالي`).
- **Do NOT translate Italian proper names (people/places/institutions/property names/publications).** They stay Italian across EN/FR/ES/AR. For AR they appear in Latin script inside Arabic text (unicode-bidi: isolate).
- **Do NOT collapse the 4 Pexels pools back into two `lawyer` and `real-estate` pools.** The per-archetype separation is D-054 enforcement infrastructure.
- **Do NOT add prices to Villa listings.** The "Prezzo su richiesta" convention is a Villa-specific brand signal per editorial-concierge tone.
- **Do NOT add a cart/shop surface to Casa or Villa.** They are real-estate advisories, not ecommerce.
- **Do NOT retroactively animate Villa's "Prezzo su richiesta" label as a counter.** D-081 tone-exception applies.

### What to verify BEFORE the next major rollout

When Phase 3 authors begin wiring commerce/editor/projects to the 20 live templates:
- Every marketplace detail page (`/templates/<cat>/<slug>/`) returns HTTP 200 in all 5 locales
- Every live preview home (`/templates/<cat>/<slug>/preview/`) returns 200 in all 5 locales
- Every inner page (about/services/team/contact/etc per template) returns 200 in all 5 locales
- `smoke_full.py` reports **834/834 HTTP 200** (baseline verified 2026-04-15)

---

Last updated: 2026-04-15 — after **Session 52 Medical Second Wave Polish + Interaction Fix**

## Session 52 — Medical Polish: Read This Before Touching `live-forms.css`, `live-motion.js`, or Any Stats Band (2026-04-15)

**What changed in Session 52.** Polish-only session — no tier churn, no locale rework, no new skins. Closed three interaction defects left behind by Session 51's rollout: empty Benessere nav CTA, barrel-radius open listbox panel, static Salute stats.

### What's binding (D-081)

1. **`--lf-listbox-radius` exists and is the RIGHT knob to tune open-dropdown corners.** `.lf-select-listbox` in `static/css/live-forms.css` reads `var(--lf-listbox-radius, 12px)` — NOT `var(--lf-radius)`. Skins with pill fields (`--lf-radius: 999px`) MUST set `--lf-listbox-radius` explicitly to avoid a 999px-radius panel (wellness = 14px). Skins that want listbox-matches-field can set `--lf-listbox-radius: var(--lf-radius)`. Default 12px is safe.

2. **Dynamic Counter Policy binds for every stats band going forward.** When a published_live template renders a stats / facts / metrics / volumes / years / visits / indicators band, the numeric span MUST carry `data-lm="counter"` (unless the DNA tone disqualifies it — funereal editorial, brutalist manifesto, literal zeros). Reduced-motion is already respected by live-motion.js. Future rollouts (Lex · Juris · Casa · Villa) are gated on this. Premium-UI reviewer treats this as an implicit gate #11 on the D-054 matrix for templates with numeric bands.

3. **`live-motion.js` now handles both Italian AND English thousand separators.** `28.000` (IT dot-sep) → target 28000; `28,000` (EN comma-sep) → target 28000. The separator character is preserved through mid-animation frames. The regex is deliberately strict (`\d{1,3}(,\d{3})+` — multi-group required) so `1,4` (French decimal) stays a decimal.

4. **Per-stat animation opt-out = 3rd tuple element truthy.** Content registries can author `("1998", "Anno di fondazione", True)` — the truthy 3rd element tells the skin "render static, don't animate". Default = animate (2-tuple, or 3-tuple with falsy 3rd). This is the escape hatch when a value reads as a label rather than a quantity. Clinic uses this pattern in `home.html`; future skins with stats bands can copy.

5. **Multi-line Django comments inside skin HTML MUST use `{% comment %}…{% endcomment %}`.** The `{# … #}` form leaks to render output when it spans multiple lines (Django tokenizer quirk; same gotcha as Session 48 D-078 key-insight #1). This is now a hard rule for all future skin edits.

6. **Nav-CTA copy lives in `site.*`, not `chrome.*`.** Chrome is archetype-shared (marketplace bar, footer headings, form primitives); nav-CTA wording is template-specific (reservation vs phone vs chat). Wellness `_base.html` binds `{{ site.nav_cta }}`; every Benessere locale defines it. Do not add `nav_cta` to `CHROME_I18N` — wrong layer.

### Do NOT do in a follow-up session

- Do NOT revert `--lf-listbox-radius` back to inheriting `--lf-radius`. The decoupling is intentional. If a future skin wants matched radii, override explicitly.
- Do NOT author new stats bands without `data-lm="counter"`. If the DNA tone argues for static (e.g. editorial funereal voice), document the exception in the section comment.
- Do NOT add `chrome.nav_cta` to `CHROME_I18N`. Per-template voice lives in `site.nav_cta`.
- Do NOT use `{# … #}` on multiple lines inside skin HTML. Always `{% comment %}…{% endcomment %}` for annotation.
- Do NOT translate `site.nav_cta` with machine translation. The native register per locale matters — Benessere AR uses "احجز طقسك" (book your ritual), not a literal "reserve" verb.

---

Last updated: 2026-04-15 — after **Session 51 Medical Second Wave Live Rollout**

## Session 51 — Medical Second Wave Live Rollout: Read This Before Touching Any Medical Skin, Salute/Benessere/Famiglia Content, or the `medical`/`medical-wellness`/`medical-family` Pexels Pools (2026-04-15)

**What changed in Session 51.** The medical category is now **5/5 published_live**. Salute (`salute-studio-medico`, clinic archetype — SaluteVita Clinic, Milano Centrale institutional poliambulatorio), Benessere (`benessere-centro-olistico`, wellness archetype — Studio Armonia, Bergamo Alta olistico), and Famiglia (`famiglia-pediatria`, family archetype — Pediatria Famiglia Plus, Torino Crocetta pediatric) have been authored from line one with full multipage live skins (6-7 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, Pexels-curated imagery pools, and sharp D-054 differentiation enforced both vs each other AND vs Cardio/Derm specialist.

### What's binding (D-080)

1. **Salute + Benessere + Famiglia + Cardio + Derm must STAY DISTINCT across every locale.** 90 D-054 gate checks (9 pairs × 10 gates) pass. Voice contracts:
   - **Salute** (clinic institutional poliambulatorio): "La tua salute, il nostro lavoro quotidiano" register · split-booking widget hero · solid-phone nav · icon-grid 4-up SVG cards · medium density · 7-page (home/studio/servizi/prevenzione/medici/contatti/prenota). NHS/BUPA (EN), Ramsay Santé/Doctolib `vous` (FR), Sanitas peninsular `usted` (ES), MSA hospital-institutional (AR).
   - **Benessere** (wellness serene olistico): "Un respiro è la misura del nostro tempo" register · full-bleed-manifesto hero + gradient · pill-floating nav · dotted-leader pricelist rituali · calendar-spot CTA · Cormorant Garamond italic 96px · airy density · 7-page (home/filosofia/rituali/ambienti/professionisti/contatti/prenota). Goop/Tatler (EN), Marie Claire Bien-Être/Cinq Mondes (FR), Mía Wellness/Six Senses (ES), Vogue Arabia Living/Kinfolk (AR).
   - **Famiglia** (family warm pediatric): "Cresciamo insieme ai vostri bambini" register · centered-soft rounded photo card hero + SSN ribbon + pediatra pebble · soft-pastel rounded-pill nav · portrait-stack pediatre · phone-and-chat CTA (NO booking form) · Quicksand rounded friendly · airy density · 6-page (home/studio/visite/crescita/pediatre/contatti). BabyCentre UK/NCT (EN), Doctissimo Enfant/Magicmaman `vous` (FR), Guía Infantil `usted` (ES), MSA parenting-magazine (AR).
   - **Cardio + Derm** (specialist prestigious editorial): untouched in Session 51 — DO NOT modify.

2. **Three new skin folders are reusable archetype templates.** Future medical siblings:
   - Clinic generalist → reuse `templates/live_templates/medical/clinic/`. Drop content registry + DNA entry pointing archetype to `clinic`, swap palette tokens.
   - Wellness holistic → reuse `templates/live_templates/medical/wellness/`. Same pattern.
   - Family pediatric → reuse `templates/live_templates/medical/family/`. Same pattern.
   - Specialist consultive → reuse `templates/live_templates/medical/specialist/` (Cardio + Derm precedent since Session 14).
   - A hypothetical 6th medical sibling (`poliambulatorio-napoli`, `terme-ischia`, `pediatria-milano`) can ship with ONLY a seed row + DNA entry + content block + locale trees. **Zero new HTML needed** per archetype.

3. **D-047 chrome-cleanliness from line one.** All 23 new HTML files carry zero IT literals — every visible string flows from `page_data.*` / `site.*` / `chrome.*` / `{% for %}`. Future skin edits MUST keep this. Also: 10 preview-composition literals lifted into DNA `content` dict keys (`services_title`, `services_link_all`, `card_cta`, `pricelist_title`, `pricelist_sub_prefix`, `therapists_label`, `hero_ribbon`, `hero_pebble_name`, `hero_pebble_note`, `hours_label`) — preview compositions for medical are now clean too.

4. **`html[dir="rtl"]` CSS block + conditional Noto Naskh/Kufi Arabic font load on all 3 bases.** Each skin's `_base.html` carries a RTL token override block + Arabic font stack import conditional on `{% if is_rtl %}`. Latin proper names (SaluteVita Clinic, Studio Armonia, Pediatria Famiglia Plus, Elisa Conti, Sara Conti, Rambaldi, Via Galvani, Via Arena, Corso Galileo Ferraris, Sant'Anna, Regina Margherita, Gaslini, Palazzo Bonomi Suardi, etc.), prices (€ 85, € 320, € 920), phone numbers (+39 035 412 998, 011 549 21 88, 800 123 456), hours, all Latin Western digits stay Latin — `unicode-bidi: isolate` handled by RTL CSS rules.

5. **Native voice per locale, never machine translation.** Salute EN reads as native NHS; Benessere FR as native Marie Claire Bien-Être; Famiglia ES as native Guía Infantil. Structural parity: same key paths at every level across all 5 locales (verified via `diff`-style walk).

6. **Italian proper names (people/places/institutions) preserved verbatim across all locales.** Brand names, doctor names, neighbourhoods, insurance schemes (Inail, Unisalute, Generali Welion, RBM Salute, Previmedical, Caspie, MioDottore), Italian institutions (Gaslini, Sant'Anna, Regina Margherita, San Raffaele, Einaudi Ragazzi, OMCeO) — stay Italian across EN/FR/ES/AR. For AR, they appear in Latin script inside Arabic text (not transliterated).

7. **Page slugs stay Italian (URL-canonical).** Salute: home, studio, servizi, prevenzione, medici, contatti, prenota. Benessere: home, filosofia, rituali, ambienti, professionisti, contatti, prenota. Famiglia: home, studio, visite, crescita, pediatre, contatti. Only `label` fields change per locale.

8. **Pexels primary imagery with 3 disjoint pools** — `medical` (bright clinical teal), `medical-wellness` (sage serene), `medical-family` (peach warm pediatric). URLs are hot-linkable Pexels CDN with explicit `fit=crop` sizing. No video in this wave (medical register favors still photography + micro-motion over reel-style video).

9. **Stub-files-first pattern for locale wiring.** Before spawning translator sub-agents, create 12 locale stub files that `import X_CONTENT_IT as X_CONTENT_LOC`. This lets `sync_template_tiers` + smoke run immediately. Translator agents then overwrite stubs with native voice. Same pattern is recommended for future rollouts.

### Do NOT do in a follow-up session without revisiting D-080 + CLAUDE.md + this handoff

- **Do NOT add a 6th medical template without checking which archetype it belongs to.** If it's "just like Salute but for Napoli", reuse `clinic/` skin. If it's "just like Famiglia but for Milano", reuse `family/` skin. NEVER duplicate a skin folder; extend the content registry.
- **Do NOT machine-translate medical terminology.** Use the native register per locale (e.g., IT "bilancio di salute" → EN "well-child check-up" → FR "bilan de santé" → ES "revisión pediátrica" → AR "فحص طبي دوري"). Machine translation will break the D-080 voice contract.
- **Do NOT add blog_list/blog_detail to the 3 new medical templates** unless there's explicit business evidence. The current baselines per CATEGORY_ROADMAP D-053 cover them without blog.
- **Do NOT collapse the 3 Pexels pools back into one `medical` pool.** The per-archetype separation is D-054 enforcement infrastructure.
- **Do NOT touch specialist skin.** Cardio + Derm are untouched in Session 51; any regression there would be a D-060 violation.

---

Last updated: 2026-04-15 — after **Session 48 Restaurant Live Completion Premium**

## Session 48 — Restaurant Live Completion Premium: Read This Before Touching Any Restaurant, Sapore/Brace, or Trattoria-Warm/Street-Modern Skin Work (2026-04-15)

**What changed in Session 48.** The restaurant category is now **3/3 published_live**. Sapore (`sapore-trattoria-pizzeria`, trattoria-warm archetype) and Brace (`brace-street-food-lab`, street-modern archetype) have been authored from line one with full multipage live skins (6 page routes each), 5 locales (it/en/fr/es/ar) with real RTL for Arabic, and sharp D-054 differentiation enforced both vs each other and vs Gusto fine-dining.

### What's binding (D-078)

1. **Sapore + Brace + Gusto must STAY DISTINCT in voice across every locale.** D-054 differentiation is enforced by 0 IT-leak smoke (480 cross-locale checks). Voice contracts:
   - **Sapore** (warm Roman family-trattoria): "Da Nonna Rosa, come a casa vostra" register · phone+WhatsApp + reservation form · chalkboard daily-specials · family band · forno-a-legna · tavolata · Cesanese del Lazio · mattarello · tirata. Bon Appétit/NYT-Food (EN), Le Fooding `tu` (FR), El País Gastro `tú` peninsular (ES), Brownbook MSA (AR).
   - **Brace** (Bologna street-food brutalist): "Bruciato al fuoco vivo, servito al volo" UPPERCASE register · order-now (al banco/takeaway/delivery) · GLOVO/DELIVEROO/JUST EAT/UBER EATS · counter status mono chips · late-night DJ moments · smashburger · scottona · Big Shoulders Display 900. Eater (EN), Le Fooding street `tu` + anglicismes (FR), Time Out Madrid `tú` peninsular + `currar` (ES), Wamda urban-imperative MSA (AR).
   - **Gusto** (editorial fine-dining concierge): "Una serata in otto atti" register · concierge tile · sommelier · Michelin · 14 coperti · Playfair italic · Cormorant. Untouched in Session 48 — DO NOT modify.

2. **Both new skin folders are now reusable archetype templates.** Future restaurant siblings:
   - Warm-family register → reuse `templates/live_templates/restaurant/trattoria-warm/`. Drop in a new content registry, point the WebTemplate.archetype at `trattoria-warm`, swap palette tokens per the `--primary/--secondary/--accent` contract.
   - Fast-casual urban brand → reuse `templates/live_templates/restaurant/street-modern/`. Same pattern.
   - Only when a third sibling is semantically as far from BOTH existing siblings as Sapore is from Brace should a new archetype be split (D-050/D-051 default applies retroactively to restaurant).

3. **D-047 chrome-cleanliness from line one.** All 14 new HTML files (7 per skin) carry zero IT literals — every visible string flows from `page_data.*` / `site.*` / `chrome.*`. Future skin edits MUST keep this.

4. **`html[dir="rtl"]` CSS block + conditional Amiri/Noto-Kufi font load on both bases.** Sapore uses Amiri body + Noto Kufi Arabic display (warm classical for the family-trattoria voice). Brace uses Amiri + Noto Kufi (urban-brutalist register). Latin proper names (Trattoria Da Nonna Rosa, Rosa Trezzi, Marco Trezzi, Giulia Trezzi, Trastevere, Roma, Via dei Salumi, Lazio, Amatrice / Brace Street Lab, Bologna, Via Indipendenza, Tortellini), prices (€ 9.50, € 12.00), phone numbers, hours (12:00 – 24:00), Latin Western digits all stay Latin via `unicode-bidi: isolate` (Sapore) or RTL CSS rules (Brace).

5. **Native voice per locale, never machine translation.** Sapore EN reads as native NYT Food; Brace EN reads as native Eater. Sapore FR uses `tu` warm-trattoria; Brace FR uses `tu` urban-imperative — DIFFERENT registers despite both being tutoyer. Same delineation for ES/AR.

6. **Italian dish/proper names preserved across all locales.** Cacio e pepe, Carbonara, Bucatini all'amatriciana, Coda alla vaccinara, Tonnarelli, Margherita Verace, Cesanese del Lazio, Saltimbocca alla romana / Margherita, Diavola, Mortadella di Bologna, Pizza Rossa, San Marzano DOP, scottona piemontese, Tiramisù — all stay Italian across EN/FR/ES/AR.

7. **Page slugs stay Italian (URL-canonical).** Sapore: home, menu, storia, forno, eventi, contatti. Brace: home, menu, lab, moments, ordina, contatti. Only `label` fields change per locale. Slugs are IT — never translate.

### Reusable recipe (now proven 8 times)

Cardio · Derm · Gusto · Chiara · Pixel · Pragma+Elevate · Bottega+Luxe · **Sapore+Brace**:

1. Audit DNA + skin folder + content registry state for both templates
2. Author IT skin folder via parallel sub-agent (1 per template) — explicit DNA contract, palette tokens, font stack, chrome-key list (D-047), RTL block, 720px breakpoint, `:focus-visible`
3. Author IT content registry per template (~500-900 LOC each)
4. Stub locale modules (re-export IT) so imports stay green during bootstrap
5. Wire into TEMPLATE_CONTENT
6. Flip `tier` in TEMPLATE_REGISTRY.json + `python manage.py sync_template_tiers`
7. IT-only smoke (12/12 routes for 2 templates × 6 pages)
8. Dispatch 8 parallel locale sub-agents (4 locales × 2 templates) with explicit voice contracts + differentiation guards + dish-name preservation rules + structural-parity validation step
9. When agents return: parse-validate, key-parity check vs IT, live-route check at `?lang=xx`, IT-leak sweep
10. Update `smoke_full.py` + `smoke_forms.py` + `smoke_i18n_media_hardening.py` to include new templates
11. Browser click-through validation across all 5 locales
12. Update memory + DECISIONS + SESSION_LOG + TODO_NEXT + AGENT_HANDOFF + CATEGORY_ROADMAP + TEMPLATE_REGISTRY in single follow-up commit

### Do NOT do

- Do NOT collapse Sapore + Brace voices into one shared register — they must stay sharply distinct across every locale.
- Do NOT add chalkboard/family-band/Caveat-script Sapore-only patterns to Brace, or order-now/AGGIUNGI/counter-status/neon-yellow Brace-only patterns to Sapore. The cross-leak smoke enforces this.
- Do NOT touch Gusto fine-dining — it's the third leg of the restaurant category and was untouched per directive. 52/52 gusto i18n regression is the binding gate.
- Do NOT use machine translation for any locale block. The quality floor is native Bon Appétit/Le Fooding/El País Gastro/Brownbook (Sapore) and native Eater/Trax/Time Out Madrid/Wamda (Brace) editorial voice per template per locale.
- Do NOT translate Italian page slugs. Sapore stays `home/menu/storia/forno/eventi/contatti`. Brace stays `home/menu/lab/moments/ordina/contatti`. Only labels change per locale.
- Do NOT introduce a real cart/checkout/payment flow on either template. Conversion patterns are deliberate demos: phone-and-whatsapp + reservation form (Sapore) and order-now hub with simulated counter status + delivery partners marquee (Brace). A real commerce engine for restaurants is a Phase 4+ topic, out of scope.
- Do NOT touch the 9 already-multilingual templates (cardio/derm/gusto/chiara/pixel/pragma/elevate/bottega/luxe) when working on Sapore+Brace. Regression smokes (363/363 was, 363/363 still) are the binding gate. The hardening smoke (69/69 OK) verifies 11/11 multilingual coverage.
- Do NOT add Big Shoulders Display or JetBrains Mono to Sapore. Sapore is Libre Baskerville + Source Sans 3 + Caveat (script accent only).
- Do NOT add Libre Baskerville or Caveat to Brace. Brace is Big Shoulders Display + Inter + JetBrains Mono.
- Do NOT use multi-line `{# … #}` Django comments in any new skin file. Use `{% comment %}…{% endcomment %}`. The `{# foo\n   bar #}` form leaks inner text to render output (caught at first Brace/Sapore render in Session 48; both fixed).

### Gotchas (Session 48)

- **Multi-line `{# … #}` Django comments leak.** Caught at first Brace/Sapore render — debug "Big Shoulders Display [display condensed (UPPERCASE)..." string visible at top of every page; fixed by switching to `{% comment %}` block. Future skin authoring MUST use `{% comment %}` for multi-line docs.
- **Apostrophe-in-single-quoted-Python-string IT content.** First Brace IT registry had `'TRE GESTI. <em>NIENT'ALTRO.</em>'` — the apostrophe terminated the string mid-value. Convention: default to **double-quoted Python strings** when content can contain apostrophes. Sub-agent prompts now mention this explicitly.
- **`runserver --noreload` does NOT pick up template OR Python changes between requests on Windows.** Even with `DEBUG=True`. Each template/Python edit needs a server bounce on a fresh port (8901 → 8902 → 8903 → 8904 in this session). Same gotcha as Session 19, 23, 42.
- **Playwright `fullPage: true` screenshots can capture mid-fade or pre-fade state.** When `live-motion.js` IntersectionObserver hasn't fired on a section yet, that section appears blank in the thumbnail but renders correctly when scrolled into view. Workaround: `page.evaluate(() => { document.querySelectorAll('[data-lm]').forEach(el => el.style.opacity = '1'); })` before screenshot.
- **PEXELS_API_KEY env var was NOT present at session start.** Used existing curated Unsplash IDs from `restaurant-trattoria` + `restaurant-street` pools (Sessions 31/47 verified). Pexels CDN swap is a Phase-2g3.6c follow-up — the URL format `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=<w>&h=<h>&fit=crop` is hot-link-public so future swap is one-line per slot when key is provided.
- **`Caveat` font in DNA registry is NOT the structural face.** Sapore DNA declares `font_pairing = ("Caveat", "Inter")` but the actual structural typography is **Libre Baskerville + Source Sans 3** (with Caveat as a 1-2-spot script garnish on chalkboard daily-specials, "Buon appetito!" stamp, footer wordmark). The skin's `_base.html` hardcodes the Google Fonts link to load all 3 families — DO NOT rely on `theme.heading_font` for primary type on Sapore; the DNA's Caveat declaration is the script-accent contract.

---

## Session 45 — Commerce Completion v2: Read This Before Touching Any /shop/, /dashboard/, Payment, i18n, or Merchant Work (2026-04-14)

**What changed in Session 45.** `apps/commerce` è passato da foundation v1 (IT-only, dev-payment, is_staff global) a v2 operativa. Le 4 modifiche load-bearing:

### 1. Multilingua /shop/ — 5 locales via chrome dict + translations JSONField
- `apps/commerce/i18n.py` è la nuova fonte di verità per le stringhe chrome commerce. `COMMERCE_CHROME` ha ~125 keys × 5 locales. Re-esporta `SUPPORTED_LOCALES`/`DEFAULT_LOCALE`/`RTL_LOCALES` da `apps/catalog/template_i18n.py` (non riallinearle indipendentemente).
- `apps/commerce/content.py` porta il per-storefront brand copy (tagline, footer_bio, shipping_policy, return_policy, bank_transfer_instructions) × 5 locales. Il seeder lo popola su `Storefront.translations`.
- `Storefront`, `Collection`, `Product`, `ShippingMethod` hanno tutti `translations` JSONField con shape `{locale: {field: value}}` + helper `.localized(locale)`.
- `LocaleMixin` (in views/customer.py) è l'unico punto in cui si risolve `?lang=` — chiamare `self.get_locale_context(storefront)` per ottenere il context bundle.
- **Regola:** ogni internal `commerce:*` URL DEVE avere `{{ lang_qs }}` appeso: `{% url 'commerce:cart' storefront.slug %}{{ lang_qs }}`. Se saltate questo, la locale si perde al primo click.
- **Regola:** NON leggere `product.title` direttamente nei template — usate `product_l10n.title` o `products_l10n` iteration. Il fallback IT è già gestito da `localized()`.

### 2. Payment — Stripe real-path via env vars, graceful fallback altrimenti
- `apps/commerce/payments.py` è il dispatcher. `dispatch(PaymentContext(order))` sostituisce il vecchio inline `_dispatch_payment` rimosso da `services.py`.
- Stripe è lazy-imported: senza `stripe` package o senza `STRIPE_SECRET_KEY` → `ProviderUnavailable` raise → `dispatch` falla a stub con `payload.stub_fallback=True` + warning log.
- Idempotency: `idempotency_key=f"order-{order.reference}"` — retry del medesimo ordine ritorna il medesimo PaymentIntent, no double-charge.
- Webhook: `/commerce/webhook/stripe/` (csrf_exempt). Verifica signature con `STRIPE_WEBHOOK_SECRET`. Gestisce `payment_intent.succeeded`/`payment_failed`/`canceled`.
- Env vars: `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_ALLOW_STUB_FALLBACK` (default `"1"`).
- **Regola:** NON chiamare `_handle_stub` o `_handle_stripe` direttamente — sempre `payments.dispatch()`.

### 3. Merchant scoping — StorefrontMember table
- Nuovo modello `StorefrontMember(storefront, user, role=owner|editor)` unique_together.
- `SellerRequiredMixin` ora extende `LoginRequiredMixin` e in `dispatch()` verifica `_user_can_access(user, storefront)` (membership OR superuser). Anonymous → login redirect. Staff senza membership → 403 `PermissionDenied`.
- Nuova view `DashboardRootView` a `/dashboard/` — chooser page o auto-redirect se single-membership.
- **Regola:** NON usare `user.is_staff` come gate per visibility di uno storefront. Ogni query dashboard deve scope-filter per `storefront=self.storefront` (il mixin pre-carica il storefront autorizzato).
- Demo users creati dal seeder: `bottega_owner` / `commerce-v2`, `luxe_owner` / `commerce-v2`.

### 4. Customer flow — policies + lookup + retry + Stripe Elements page
- `PoliciesView` a `/shop/<slug>/politiche/` — renderizza shipping/returns/contact policy localized.
- `OrderLookupView` a `/shop/<slug>/ordine/` — guest self-service: reference + email → 302 a confirmation se match, altrimenti re-render con messaggio.
- `RetryPaymentView` POST-only a `/shop/<slug>/order/<uuid>/retry-payment/` — richiama `services.retry_payment()` che re-dispatcha via `payments.dispatch`. Per Stripe → 302 a payment_page; altrimenti → 302 a confirmation.
- `PaymentPageView` a `/shop/<slug>/order/<uuid>/payment/` — renderizza `templates/commerce/payment/stripe.html` (Stripe Elements + fallback friendly).

### Seeder workflow
- `python manage.py seed_commerce` è idempotente e ri-esegue popolamento translations + merchant users.
- Se aggiungi un nuovo shipping method code, aggiorna `SHIPPING_TRANSLATIONS` nello stesso file — senza entry, ship_method renderizza solo in IT.

### Validation matrix da rieseguire dopo modifiche
- `python manage.py check` → 0 issues
- Commerce smoke (73/73): shop/cart/checkout/policies/ordine × 5 locales × 2 skin + product × 3 locales × 2 skin + collection × 2
- Live preview regression (45/45): 9 templates × 5 locales, must stay green
- ACL matrix (7/7): anon/bottega_owner/luxe_owner × 3 dashboard paths
- Customer flow: add_to_cart→302, checkout POST→302, order confirmation AR→200, order lookup POST match→302

### Non fare
- Non modificare `/templates/<cat>/<slug>/preview/*` routes o live_templates templates — zona marketing intoccabile, protetta da 45/45 regression.
- Non aggiungere hardcoded `?lang=` in un template — usa `{{ lang_qs }}`.
- Non chiamare il vecchio `_dispatch_payment` — è stato rimosso.
- Non gate dashboard su `is_staff` — usa StorefrontMember.
- Non committare chiavi Stripe reali in `settings.py` — solo env vars.

---

## Session 43 — Commerce Foundation v1: Read This Before Touching Any Commerce, Cart, Checkout, Order, or Seller Dashboard Work (2026-04-14)

**Session 43 closed Phase 3a** — `apps/commerce` is no longer empty stub. It now ships a full operational engine for shops (Product/Variant/Cart/Order/PaymentIntent) with two skin template sets serving Bottega + Luxe at `/shop/<storefront>/…`, a seller dashboard at `/dashboard/<storefront>/…`, and a provider-agnostic payment abstraction (stub + offline_bank_transfer in v1, Stripe documented extension point).

### What's binding (D-075)

1. **`/shop/<slug>/...` and `/dashboard/<slug>/...` are the operational surfaces. `/templates/<cat>/<slug>/preview/...` stays the marketing surface.** D-053 Live Preview Law still binds the preview URL space. NEVER fold commerce operations into the preview routes — they must remain untouched. When a user visits a Bottega live preview they see the Session 41+42 showcase; when they visit `/shop/bottega-shop-artigianale/` they see the real operational shop. The two surfaces are peers, not versions.

2. **`Storefront.is_operational` is the commerce-side shippability gate** — parallels `WebTemplate.tier == published_live`. Both Bottega + Luxe are operational in v1. Future ecommerce templates must flip BOTH `tier=published_live` (preview visible) AND create a `Storefront` row with `is_operational=True` (shop visible).

3. **Inventory is decremented on order creation, not at payment time.** The `create_order_from_cart` service uses `select_for_update` to lock variants inside a transaction. For the `stub` dev provider payment auto-succeeds so there's no race window; for real providers (Stripe later, offline_bank_transfer today) the order sits at `payment_status=UNPAID` while stock is already held. A compensating "release held stock on payment failure" service is a Phase 3b add.

4. **Guest checkout is first-class.** Cart is session-keyed (`request.session.session_key`). User FK is optional on both Cart and Order. Checkout form does not require login. Order confirmation page is addressable by UUID (shared link). Do NOT introduce login gates on any `/shop/` route.

5. **Seller dashboard gate is `is_staff` today.** `SellerRequiredMixin` redirects anon/non-staff to `/admin/login/?next=…`. A `Seller` model scoping users to specific storefronts is a documented Phase 3b split.

6. **Payment providers are registered in the `Storefront.PaymentProvider` enum.** v1 enum has `stub` + `offline_bank_transfer`. Adding Stripe means: (a) add `STRIPE = "stripe"` to the enum, (b) add `_handle_stripe(order)` to `services._dispatch_payment`, (c) create a webhook view that resolves PaymentIntent by `provider_reference` and transitions status, (d) add a `STRIPE_SECRET_KEY` setting. No model migration needed.

7. **Skin template duplication is DELIBERATE in v1.** `templates/commerce/skins/<skin>/_base.html` files duplicate structural CSS from `templates/live_templates/ecommerce/<archetype>/_base.html`. The two surfaces have different nav targets (commerce chrome links to `/shop/`, preview chrome links to `/templates/`), different CTA registers (operational vs marketing), and different locale coverage (commerce is IT-only v1, preview has 5 locales). Consolidate when commerce gets i18n in Phase 3b.

### Reusable recipe (for adding a new operational storefront)

When a 3rd ecommerce template ever ships a real shop:
1. Flip `tier=published_live` via the existing sync_template_tiers pipeline (Session 41 recipe).
2. Decide which skin to reuse: `artisan-workshop` for warm-artisan macros (Aesop/Toscana/soulful), `fashion-editorial` for maison-editorial macros (Hermès/Vogue/gold-on-ink). If the sibling is semantically as far from both as Bottega is from Luxe, only then split a new skin under `Storefront.Skin`.
3. Extend `seed_commerce.py` with a new `_seed_storefront(...)` call passing `template_slug`, the collections list, products list, shipping methods.
4. `python manage.py seed_commerce` — idempotent, safe to run repeatedly.
5. If a new skin: add its directory under `templates/commerce/skins/<new-skin>/` with the 5 page templates. Set `--cx-*` tokens in `_base.html`. The `commerce.css` widget CSS follows automatically.
6. Run `smoke_commerce.py` — it dispatches routes dynamically from Storefront.objects.all() (extend smoke_commerce if adding a 3rd storefront to verify the new routes).

### Do NOT do

- Do NOT fold real commerce operations into `/templates/…/preview/…` URLs. Those URLs are bound by D-053 to the marketing/showcase surface.
- Do NOT add login requirements to `/shop/` customer routes. Guest checkout is first-class.
- Do NOT bypass the `SellerRequiredMixin` on dashboard views — it's the auth gate.
- Do NOT decrement stock in templates or views. Stock mutations live in `apps/commerce/services.py`. Views call services.
- Do NOT remove the `select_for_update` lock from `create_order_from_cart` — it's silent no-op on SQLite dev but activates on production Postgres.
- Do NOT add Stripe directly to `views/customer.py`. Add it to the `_dispatch_payment` switch in `services.py` to keep the provider abstraction intact.
- Do NOT touch `templates/live_templates/**` when working on commerce — those are the preview/showcase templates and must stay frozen. Session 41 D-073 + Session 42 D-074 set the bar; commerce parallels, doesn't replace.
- Do NOT translate commerce UI strings into other locales yet. Commerce i18n is Phase 3b. The commerce pages are IT-only in v1; the preview pages keep their 5 locales.
- Do NOT add a 3rd shipping method "shortcut" like `italy-express` without going through `seed_commerce` or admin — shipping methods are per-storefront scoped and must be created via Storefront.shipping_methods.

### Gotchas (Session 43)

- **Windows `manage.py shell -c` console encoding (cp1252) breaks Unicode print output.** Use plain ASCII in smoke script output, or set `PYTHONIOENCODING=utf-8`. Smokes that use `·`, `→`, `←`, box-drawing chars will crash with `UnicodeEncodeError` on a fresh Windows shell.
- **Django Test Client rejects `testserver` hostname when `ALLOWED_HOSTS = []`.** Pass `Client(HTTP_HOST="localhost")` explicitly. `DEBUG=True` defaults to `['localhost', '127.0.0.1', '[::1]']` — not testserver.
- **`session.session_key` is None until the session is saved.** Calling `request.session.save()` forces it to materialize. The commerce helper `_ensure_session` handles this; don't inline the access in views.
- **`select_for_update` on SQLite is a no-op, the lock fires on Postgres only.** Dev works, production gains the lock automatically. If you test concurrent checkout flows on SQLite, they won't deadlock — they just race like any other SQLite writes.
- **Cart.item_count() is a `Sum` aggregate, not `.count()`.** Calling `.count()` returns the number of CartItem rows (distinct variants), not the total quantity. Use `item_count()` for the nav pill number.
- **Category.subtitle may be empty** on seeded collections. Templates that render `{{ current_collection.subtitle }}` should use `|default:current_collection.title` as fallback. Already applied in the shop.html templates.
- **UpdateCartItemView accepts quantity=0 to mean "remove"** per the service contract. Don't assume the POST body has qty > 0 — the front-end qty input has min="0" because setting to 0 is an intentional remove gesture.

---



## Session 42 — eCommerce Premium Polish: Read This Before Touching Any eCommerce Image, Motion, or DNA Drift Work (2026-04-14)

**Session 42 closed two blockers** the user flagged on Session 41 review: (1) Bottega had visible image gaps + 9 visually-wrong Unsplash IDs (HEAD-200 but rendering blue stilettos / classroom / cat / cupcakes / Bond Street tube / etc.); (2) Luxe was rendering as a polished but motionless poster, lacking the editorial premium presence its maison register requires.

### What's binding (D-074)

1. **Bottega is now archetype-honest typographic-led.** All 6 portrait slots (4 makers in home + founder in atelier + artisan signature in product detail) converted to typographic stamp tiles. NO portrait images on Bottega anywhere. Future ecommerce siblings that fit the warm-artisan macro tone reuse this typographic-stamp pattern (`.aw-maker` with corner-N + BOTTEGA stamp + italic letter crest + name/craft/place/since/quote · `.aw-founder .monogram` circular cream stamp · `.aw-pdp .artisan .monogram` smaller circular). DO NOT re-add portrait images to Bottega — the artisan-workshop DNA was always typographic-led (Session 15 DNA notes); Session 41 drifted, Session 42 returned to the DNA.

2. **Luxe ships ~280 LOC of editorial motion** that reads as italic-thinking unhurried. Hero scale-breathe (14s ease-in-out), italic-axis settle on h1 (1200ms cubic-bezier), counter on KPI bands (slow stagger 160-180ms with tabular-nums), press logo marquee (100s drift), drop card pulsing gold dot, primary button gold panel slide-in, nav links + ghost button + tile + atelier card + maison card + variant pill all get letter-spacing or color hover language. Cubic-bezier(0.16, 0.84, 0.32, 1) is the Luxe motion ease — DO NOT use startup-saas-landing's 200ms snappy timings or glow shadows on Luxe. The reduced-motion fallback is mandatory and already wired.

3. **Image-coherence rule binding for all future authoring:** HEAD-200 ≠ visually correct on Unsplash. The `curl + Read tool` per candidate verification (Session 37 Chiara recipe) is the reliable check. When 6+ slots need verification of specific photographic content (older Italian artisans, fashion editorial models, etc.), prefer ARCHITECTURAL elimination of the photo requirement (typographic substitute, gradient placeholder) over endless candidate hunting. The Session 41 → 42 lesson: respect documented DNA notes BEFORE adding image-dependent elements.

4. **The press strip pattern (`.lm-logo-marquee` from `live-media.css/js`) is now linked in Luxe `_base.html`** — also linked in Pragma + Elevate + Cardio + Derm + Gusto / Chiara / Pixel where used. Future templates that need a logo marquee just need `<link>` + `<script>` + the `<div class="lm-logo-marquee">...<div class="lm-logo-marquee-track">...` markup. The `live-motion.js` duplicates the track automatically for seamless looping.

### Reusable recipe (Session 41 + 42)

When a `published_live` ecommerce template ships from now on:
1. Cross-check DNA notes in `template_dna.py` BEFORE adding ANY image-dependent element. If DNA says "typographic-led", honor it.
2. Author the IT skin + content first under D-047 (every string from `page_data.*` / `site.*` / `chrome.*`).
3. For maker / founder / artisan signature blocks: default to typographic stamp tiles (Bottega pattern) unless the DNA explicitly calls for image portraits AND a verified photo source exists. Fashion-editorial templates (Luxe pattern) default to image portraits with `data-latin` markers preserving Latin proper names + isolated unicode-bidi for AR.
4. Wire IT, flip tier, run sync_template_tiers, validate IT-only with smoke_full.
5. Dispatch 8 parallel sub-agents for locale trees (one per locale × 2 templates) with explicit voice contracts.
6. For motion: choose ONE motion register per archetype and stay in it. Artisan-warm = slow warm 12px rise + 560ms cubic-bezier + paper-shadow stamp lift (no zoom/parallax). Maison-editorial = slow editorial 14-22px rise + 1100-1400ms cubic-bezier + tabular-num counters + scaleX gold underline slides (no glow/bounce). SaaS = snappy 200ms + glow shadows (Elevate pattern, NOT for ecommerce).
7. Validate the full 8-suite matrix + run the dedicated cross-leak smoke for the category.

### Do NOT do

- Do NOT add portrait images to Bottega ever again. The artisan-workshop DNA is typographic-led. Maker stamps + monogram circles are the only acceptable identity markers.
- Do NOT use startup-saas-landing motion timings on Luxe (200ms snappy bounce). Luxe motion is 600-1400ms cubic-bezier(0.16, 0.84, 0.32, 1) — italic-thinking unhurried.
- Do NOT trust HEAD-200 Unsplash IDs blindly. Always visual-verify (Read tool can render JPGs).
- Do NOT introduce real cart/checkout/payment on either template. Conversion patterns stay phone-and-whatsapp (Bottega) and private-request (Luxe).
- Do NOT change `live-media.css/js` linking on Luxe — it now needs the marquee primitive. Pragma + Elevate + Luxe link it; the other 6 `published_live` don't.
- Do NOT touch the 7 pre-existing live templates (cardio/derm/gusto/chiara/pixel/pragma/elevate). 867/867 regression matrix is the gate.

### Gotchas (Session 42)

- **Image-curator sub-agent timed out at 0 bytes output.** The dispatch worked, the agent never wrote. The pivot to architectural typographic conversion was the right call. For future visual-curation needs of >5 slots, dispatch the curator sub-agent BUT also have a typographic fallback ready in case it stalls.
- **Django dev server `--noreload` does NOT auto-pick up file changes.** Bounce on a fresh port after every Python/template edit (8801 → 8802 → 8803 → 8804 → 8805 in this session). Session 19's ghost-server gotcha returns periodically — always restart on a different port to be safe.
- **Same Unsplash ID can render different content at different sizes.** `photo-1543163521-1bf539c55dd2` rendered as a knit pullover at 600×600 thumb but blue floral stilettos at 900×900 product hero. The CDN serves a smart crop based on the dimensions request, and the crop can yield completely different visual content. Always verify at FULL size, not thumbnail size.
- **Marquee CSS `flex: 1; min-width: 0` is required** when `.lm-logo-marquee` lives inside a flex container with other siblings (the press strip's "lbl" label). Without it, the marquee track collapses or overflows. Already applied via `.fe-press .lm-logo-marquee { flex: 1; min-width: 0 }`.
- **Counter values get truncated mid-animation in screenshots.** "44" appearing instead of "45" on a viewport screenshot doesn't mean the counter is broken — it means the screenshot was taken at frame 0.95 of the 1400ms animation. Wait 2s then re-screenshot for the final value, or accept that mid-animation values are visible in a Playwright walk.

---

## Session 41 — eCommerce Live Rollout: Read This Before Touching Any eCommerce or Sibling-Pair Live-Rollout Work (2026-04-14)

**Session 41 closed Phase 2g3.5** — `bottega-shop-artigianale` and `luxe-fashion-store` are flipped to `tier=published_live` with full multipage skins + 5 locales (it/en/fr/es/ar) + real RTL on day one. Catalog floor is now **9/20 published_live across 5 categories** (medical/restaurant/business/portfolio/ecommerce), 9/9 multilingual.

### Catalog state

- 9/20 published_live: cardio · derm · gusto · pragma · elevate · chiara · pixel · **bottega** · **luxe**.
- 11/20 draft: sapore · brace (restaurant Phase 2g3.1) · salute · benessere · famiglia (medical Phase 2g3.2) · vertex · aura (agency Phase 2g3.6) · lex · juris (lawyer Phase 2g3.6) · casa · villa (real-estate Phase 2g3.6).
- Phase 3 (auth/checkout/editor/projects/commerce) remains gated on Phase 2g3.6 closing per D-049/D-053.

### What's binding (D-073)

1. **Bottega + Luxe must STAY OPPOSITE in voice across every locale.** D-054 differentiation is enforced by the new `smoke_ecommerce_rollout.py` cross-leak gate (15 Bottega-only tokens + 16 Luxe-only tokens × 5 locales × 12 pages × 2 directions = 120 leak checks, must always be 0/120). A regression PR that introduces a Bottega vocabulary token on a Luxe page (or vice versa) must be rejected. Voice contracts: Bottega = warm artisan Toscana (Aesop EN, Astier FR `tu`, peninsular `tú` ES, Brownbook AR cultural-publishing); Luxe = maison editoriale (Gentlewoman EN formal, Hermès FR `vous`, Vogue España `usted`, Vogue Arabia luxury-maison AR).
2. **Both ecommerce skin folders are now reusable archetypes.** A future ecommerce sibling that fits the warm-artisan macro tone reuses `templates/live_templates/ecommerce/artisan-workshop/`. A future ecommerce sibling that fits the maison-editorial macro tone reuses `templates/live_templates/ecommerce/fashion-editorial/`. Only when a third sibling is semantically as far from BOTH existing ones as Bottega is from Luxe should a new archetype be split (D-050/D-051 default).
3. **D-047 chrome-cleanliness applied from line one.** Both `_base.html` files + all 12 page templates carry zero IT literals — every label flows from `page_data.*` / `site.*` / `chrome.*`. Future skin edits MUST keep this.
4. **`html[dir="rtl"]` CSS block + conditional Amiri/Noto-Kufi font load on both bases.** Bottega uses Amiri body + Noto Kufi Arabic display (warm classical for the artisan voice). Luxe uses Amiri body + Noto Kufi Arabic display (classical for the maison voice). Latin proper names (La Bottega di Martino, Maison Luxe, Vogue Italia, The Gentlewoman, Hermès, Bottega Veneta, Lesage, Goyard, IMG Models, Grand Hôtel Villa d'Este, Setificio Tessitura Como, Maglificio Lanifer Biella, Conceria della Madonna, Atelier Sentier, Severino Falchi, Caterina Lippi, Bruno Ricci, Adele Pignatelli, Giulia Maison, Carla Sozzani, Letizia Carrera, Jean-Luc Berthier, Yumi Tanaka), prices (€ 420, € 95, € 2.480, € 1.290, € 860), edition numbers (N° 042, 3/8, Look 03, Drop 02, SS26), phone numbers (+39 055 234 11 90, +39 02 7600 1492, +33 1 4296 4720, +81 3 6450 5018), Italian city names (Firenze, Toscana, Santa Croce sull'Arno, Montelupo Fiorentino, Prato, Greve in Chianti, Milano, Brera, Sentier, Aoyama) all stay Latin via `unicode-bidi: isolate` (Bottega) or `[data-latin]` markup attribute (Luxe).
5. **Native voice per locale, never machine translation.** Bottega EN reads as native Aesop. Luxe EN reads as native The Gentlewoman. Bottega FR uses `tu` + `« »`. Luxe FR uses `vous` + `« »` + insecable spaces. Bottega ES uses `tú` + peninsular vocabulary. Luxe ES uses `usted` + peninsular maison vocabulary. Bottega AR uses cultural-publishing register. Luxe AR uses luxury-maison register. Future content edits MUST follow these per-locale per-template voice contracts.
6. **WhatsApp link is a Bottega-only conversion pattern.** Bottega's nav CTA + final CTA + contact card all expose WhatsApp via `{{ site.whatsapp_link }}`. Luxe NEVER carries WhatsApp — its conversion is private viewing by appointment. The cross-leak smoke enforces this: "WhatsApp" appearing on a Luxe page = D-054 violation.
7. **Page slugs stay Italian (URL-canonical).** Bottega: home, shop, product, atelier, journal, contatti. Luxe: home, collezione, product, maison, lookbook, contatti. Only `label` fields change per locale (e.g., "Catálogo" vs "Catalogue" vs "Shop" vs "الكتالوج"). Slugs are IT — never translate.

### Reusable recipe (now proven 6 times: Cardio · Derm · Gusto · Chiara · Pixel · Pragma + Elevate · **Bottega + Luxe**)

The Session 23/29/37/39/40/41 recipe is now stable enough to be a checklist:
1. Author both IT content registries first (D-047 from line one — never paste literals, every string flows from `page_data.*` / `site.*` / `chrome.*`).
2. Author both skin folders next.
3. Wire IT into `template_content.py` + flip tier in `TEMPLATE_REGISTRY.json` + `python manage.py sync_template_tiers`. Validate IT-only with `smoke_full.py`.
4. Dispatch 8 parallel sub-agents (one per locale × 2 templates) with explicit voice contracts that articulate the differentiation gate as a "must NOT contain X" + "must contain Y" pair.
5. While agents work: extend `smoke_full.py` + `smoke_forms.py` + `smoke_i18n_media_hardening.py` + author a new `smoke_<category>_rollout.py` that codifies the D-054 cross-leak gate.
6. When agents return: run the full validation matrix (manage.py check + 4 smokes + 3 regression smokes).
7. Update memory + DECISIONS + SESSION_LOG + TODO_NEXT + AGENT_HANDOFF + CATEGORY_ROADMAP + TEMPLATE_REGISTRY in a single follow-up commit.

When opening any future ecommerce session, read `ecommerce_live_rollout_session41.md` in memory before starting.

### Do NOT do

- Do NOT collapse Bottega + Luxe voices into one shared register — they must stay sharply distinct across every locale.
- Do NOT use machine translation for any locale block. The quality floor is native Aesop / Gentlewoman / Astier / Hermès / Vogue España / Vogue Arabia editorial voice per template per locale.
- Do NOT introduce a real cart/checkout/payment/auth flow on either ecommerce template. The conversion patterns are deliberate demos: phone-and-whatsapp (Bottega) and private-request (Luxe). A real commerce engine is Phase 3 work, gated on Phase 2g3.6 closing.
- Do NOT translate Italian page slugs (`shop`, `product`, `atelier`, `journal`, `contatti`, `collezione`, `maison`, `lookbook`) to non-IT equivalents — URLs stay canonical Italian, only labels change per locale.
- Do NOT add WhatsApp anywhere on Luxe — it's the Bottega-only conversion marker.
- Do NOT add Drop/Lookbook/Private Viewing vocabulary anywhere on Bottega — they're Luxe-only maison markers.
- Do NOT touch the 7 already-multilingual templates (cardio/derm/gusto/chiara/pixel/pragma/elevate) when working on ecommerce. Regression smokes (76/76 chiara · 80/80 pixel · 52/52 gusto · 363/363 full sweep) are the binding gate.

### Gotchas (Session 41)

- **Add `product` to `pages` array even if it's a detail page.** First validation pass failed because the registries had `product` as a content block but not in the `pages` list — the LiveTemplateView's `find_page` lookup 404'd. The simplest fix is to add it as a navigable page (`{"slug": "product", "label": "Pezzo|Look", "kind": "product"}`). For a "real" product detail with multiple drilldown variants, the post mechanism (`/preview/<page>/<post_slug>/`) would be the right path, but requires a content registry with a `posts` list.
- **`smoke_forms.py` `lf-select` marker is exact-match `class="lf-select"`.** A `<select class="lf-select lf-input">` element does NOT match. The reference pattern (Pragma/Elevate use it) is `<div class="lf-select" data-lf-label="…"><select class="lf-input">…</select></div>` — wrap the native select in a `lf-select` div, put `lf-input` on the select.
- **8 stub locale files needed during bootstrap.** When the import-block at the bottom of `template_content.py` references `BOTTEGA_CONTENT_EN` etc. but the sub-agents haven't authored them yet, Python ImportError aborts the whole catalog. Workaround: create stub files first that re-export `..._CONTENT_IT as ..._CONTENT_EN` so the import succeeds; sub-agents overwrite each stub with their full locale tree. The validation chain stays green throughout.
- **The legacy preview composition files (`templates/preview_compositions/ecommerce/{artisan-workshop,fashion-editorial}.html`) still carry their original 10+/12+ Bottega/Luxe literals.** They are deliberately untouched in this session. They are used only for the static listing PNG via the Playwright pipeline. Lifting them is a separate, cosmetic-only Phase 2g2x.3 leftover that doesn't affect the live preview tier — and is now particularly low-priority because the live preview is the primary surface, the static listing PNG is decorative.
- **`Maglificio Lanifer` was first listed in BOTTEGA_ONLY_TOKENS in the smoke** (typo from the cross-leak audit) — it's actually a Luxe-only fabric house (Lanifer Biella). The smoke includes a sanity-fix `tuple(t for t in BOTTEGA_ONLY_TOKENS if t != "Maglignifico Lanifer")` to strip it. Future tokens authored for cross-leak must be verified against both content trees before being added to the gate.
- **`data-latin` HTML attribute is a Luxe-only convention** for marking Latin proper names that need `unicode-bidi: isolate` in RTL CSS. Bottega's RTL CSS uses selector-based isolation instead (`html[dir="rtl"] .aw-nav .wm` etc.). Both work — the choice is per-archetype style, not a contract. Future templates can pick either pattern but must not mix them on the same skin.

---

## Session 40 — Pragma + Elevate i18n: Read This Before Touching Any Multilingual or Business Template Work (2026-04-14)

**Session 40 closed Phase 2g3.3b** — the 7-template `published_live` catalog now ships **7/7 multilingual** with real RTL for Arabic. `pragma-corporate-suite` and `elevate-startup-landing` were the last 2 IT-only live templates. Both keep their sharply distinct voices: Pragma institutional B2B advisory · Elevate SaaS growth-tech.

### Catalog state

- 7/7 published_live ship in 5 locales: cardio · dermatologia · gusto · chiara · pixel · **pragma** · **elevate**.
- Multilingual coverage on the public catalog is closed. Phase 3 (auth/checkout/editor/projects/commerce) remains gated on Phase 2g3.7 (all 20 templates published_live) per D-049 + D-053. 7/20 published_live, 13/20 still draft.

### What's binding (D-072)

1. **Pragma + Elevate must STAY OPPOSITE in voice across every locale.** D-054 differentiation is enforced by sub-agent voice contracts. Pragma uses formal institutional registers (FT/HBR EN, vouvoiement FR, peninsular usted ES, MSA boardroom AR with dropped honorifics). Elevate uses SaaS founder-facing registers (TechCrunch/Linear EN with contractions, modern SaaS FR with `tu`, peninsular `tú` ES with anglicismes, modern startup MSA AR with Latin product names + Latin acronyms). Future content edits MUST preserve this. A regression PR that homogenizes the two templates into one voice should be rejected.
2. **9 D-047 leaks lifted** are now `page_data.*` / `site.*` fields. Future skin edits MUST keep this — no IT labels in HTML, ever. Particular gotcha: `pricing.html` `Più scelto` was a CSS pseudo-element `content: 'Più scelto';` (CSS-generated content can't be localized via Django templates) — it was moved to HTML `<span class="pop-badge">{{ page_data.highlight_badge }}</span>` rendered conditionally. Don't revert to CSS pseudo-element badges for any locale-bound text.
3. **Both business archetypes have full `html[dir="rtl"]` CSS blocks** with conditional Arabic font load + page-level grid flips inside `{% if is_rtl %}` + Latin wordmark / Latin product name / Latin numeric isolation via `unicode-bidi: isolate`. Skin edits that add new components MUST add their RTL-flip rules in the same commit (otherwise AR ships visually broken).
4. **Native voice per locale, never machine translation.** Pragma EN reads as native FT/HBR. Elevate EN reads as native TechCrunch/Linear. Pragma FR uses vouvoiement + insecable spaces. Elevate FR uses `tu` + insecable spaces + anglicismes. Pragma ES uses peninsular `usted`. Elevate ES uses peninsular `tú`. Pragma AR uses MSA boardroom with dropped honorifics. Elevate AR uses modern startup MSA with Latin product names. Future content edits MUST follow these per-locale voice contracts.
5. **Latin proper names + Latin product names + Latin acronyms preserved across all locales.** Pragma: partner Italian names (Federico Seregni, Caterina Foschini, Marco Lavezzi, Sabina Erlanger, Lorenzo Pellizzari, Giulia Antinori), Italian institutions (Bocconi, Insead, Cattolica, Politecnico, Bonelli Erede, McKinsey), CONSOB acronym, technical acronyms (CSRD, ESG, M&A, EBITDA). Elevate: founder Italian names, all SaaS product names (Stripe, Linear, Slack, Vercel, PostHog, GrowthBook, Loops, Cal.com, Plain, Resend, Cloudflare, Netlify, Next.js, React, Postgres, Prisma, Neon, Clerk, JetBrains Mono), version strings (v2.5–v3.0), all SaaS acronyms (MRR, ARR, A/B, PMF, KPI, CLI). Latin Western digits (1, 2, 3, …) used for prices/percentages/years in AR per MENA business-press convention.

### Reusable recipe (now proven 5 times: Cardio · Derm · Gusto · Chiara · Pixel · **Pragma + Elevate**)

The Session 23/29/37/39 recipe scales to a 2-template, 8-tree fan-out without modification. The only addition: an upfront D-047 leak sweep on BOTH skin folders before authoring (otherwise the new locale trees inherit IT-hardcoded labels). For business templates specifically, also lift any CSS pseudo-element content (`::before content: "…"`) to HTML rendered from a content field — CSS-generated content cannot be localized through Django templates.

When opening any future i18n session that touches business templates, read `business_i18n_completion_session40.md` in memory before starting.

### Do NOT do

- Do NOT collapse Pragma + Elevate voices into one shared register — they must stay sharply distinct across every locale.
- Do NOT use machine translation for any locale block. The quality floor is native FT/HBR/Les Echos/Cinco Días/Wamda/Maddyness editorial voice per template per locale.
- Do NOT add CSS pseudo-element `content: '…';` for any locale-bound visible text. Lift to HTML rendered from `page_data.*` / `site.*` / `chrome.*`.
- Do NOT touch the 5 already-multilingual templates (cardio/derm/gusto/chiara/pixel) when working on business templates. Regression smokes (76/76 chiara · 80/80 pixel · 52/52 gusto · 282/282 full sweep) are the binding gate.
- Do NOT translate Italian page slugs (`prodotto`, `prezzi`, `demo`, `contatti`, `chi-siamo`, `competenze`, `case-studies`) to non-IT equivalents — URLs stay canonical Italian, only labels change.

---

## Session 37 — Chiara Perfection: Read This Before Touching Any Locale Rollout (2026-04-13)

**Session 37 brought `chiara-portfolio-creativo` to gold-standard product quality** — full 5-locale i18n (it/en/fr/es/ar) + editorial-designer-coherent imagery (laptop stock photos retired) + skin-HTML literal lift × 9 sites + mobile horizontal overflow fix (124px → -15px) + `html[dir="rtl"]` CSS block + a11y focus rings. Single template only — no other live template touched except smoke harness + cross-template chrome.

### Catalog state

- 4/7 published_live ship in 5 locales: **cardio · derm · gusto · chiara**.
- 3/7 IT-only: **pragma · elevate · pixel** (next targets for Phase 2i.2c-d).

### What's binding (D-070)

1. **Every chiara live route renders in 5 locales** with structural parity (same `pages` slugs/kinds, same key shapes, locale-specific labels + content). Verified via `smoke_chiara_perfection.py`.
2. **Skin HTML zero-leak.** The 9 hardcoded Italian literals previously in `editorial-designer-grid/*.html` are now `page_data.*` fields. Future skin edits MUST keep this — no labels in HTML, ever. Smoke checks this on lift sites.
3. **Editorial-designer imagery only.** No laptop / coding / businessperson / generic-office stock photos in any chiara surface. The 5 new IDs (`photo-1611532736597-de2d4265fba3` Triennale, `photo-1497633762265-9d179a990aa6` Adelphi, `photo-1564399579883-451a5d44ec08` Querini, `photo-1455390582262-044cdead277a` Velluti, `photo-1544717305-2782549b5136` Founder) are the references. Old laptop IDs are scrubbed.
4. **Native voice per locale**, never machine translation. FR uses `vous` + `« »` + insecable spaces + French ordinals (24ᵉ). ES uses `usted` form throughout. AR keeps proper names in Latin script + Latin digits for technical data + uses `، ؛ ؟` and `« »`.
5. **Mobile horizontal overflow at 390px viewport: ≤ 0px.** Inline-styled `<div class="head" style="display:grid; grid-template-columns: 0.45fr 1fr">` patterns require `!important` overrides at `@media (max-width: 720px)` to collapse — the Session 37 home.html fix is the precedent.
6. **a11y focus rings on every CTA.** `.ed-btn-primary` + `.ed-btn-ghost` have `:focus-visible` 2px accent outline + 4px offset. Future buttons must follow.

### Reusable recipe (now proven 4 times: Cardio · Derm · Gusto · Chiara)

1. **Lift literals** out of skin HTML into `page_data.*` content fields BEFORE authoring locale trees. Otherwise the 4 non-IT trees miss labels.
2. **Spawn 4 parallel sub-agents**, one per locale (EN/FR/ES/AR). Give each: full IT source path, exhaustive voice guidelines (proper names verbatim, taxonomy translations, typography conventions, idiomatic register), output spec (Python module mirroring IT shape exactly).
3. **Spawn 1 image curation sub-agent** (if imagery is off-brand). Method: download via curl + inspect via Read tool per candidate, reject laptops/phones/lifestyle, output verified IDs with rationale per slot.
4. **In parallel** to the agents: do the RTL CSS block + Arabic font conditional + mobile breakpoint fixes + a11y focus rings on the skin's `_base.html`. These are 100% skin-side, don't need content trees ready.
5. When agents return: verify structural parity via deep keyset diff (must be 0 missing / 0 extra per locale). Wire imports into `template_content.py` `TEMPLATE_CONTENT` dict. Apply image swaps to all 4 locale trees via batch script. Extend `smoke_full.py` LOCALES list. Migrate template from `IT_ONLY` to `MULTILINGUAL` in `smoke_i18n_media_hardening.py`. Add a per-template content-marker smoke (signature phrase per locale + RTL marker + image swap verify + IT-leak sweep).
6. Run full validation matrix: `check`, `smoke_full`, `smoke_forms`, `smoke_i18n_media_hardening`, `smoke_<template>_perfection`. All must be green. Playwright walk on 1440×900 × 5 locales + 390×844 mobile.

### Do NOT do

- Do NOT use machine translation for any locale block. The quality floor is native editorial voice. A PR that ships auto-translated content should be rejected.
- Do NOT add new content blocks to chiara IT tree without mirroring in all 4 non-IT trees at the same commit (D-069 silent-disparity rule — adding to IT only creates content-depth disparity that the `{% if page_data.X %}` guard hides).
- Do NOT use laptop/coding/businessperson stock photos anywhere in chiara. Editorial designer identity is print/type/paper/ink/signage/manuscript matter only.
- Do NOT remove the `html[dir="rtl"]` CSS block from `editorial-designer-grid/_base.html` even if no AR content exists later — it's load-bearing for any RTL locale future-state.
- Do NOT translate page slugs. Only `label` fields change per locale. URLs stay Italian (`/lavoro/`, `/processo/`, `/contatti/`).
- Do NOT transliterate proper names in AR. Chiara stays "Chiara", not "كيارا". Triennale stays Latin.
- Do NOT introduce Django gettext / .po / middleware. D-059 still binding.
- Do NOT open auth / checkout / editor / projects / commerce / dashboard / new categories / new templates.

### Gotchas (Session 37)

- **Django template tag literals inside CSS comments are still parsed.** A CSS comment like `/* guarded by {% if is_rtl %} below */` will be interpreted as an actual `{% if %}` tag (with no matching `{% endif %}` in scope) and crash `TemplateSyntaxError`. Workaround: use plain text in CSS comments, never reproduce literal tag syntax. Caught + fixed during Session 37.
- **Inline `style=` attributes have specificity 1,0,0,0** — beats normal class selectors. To override an inline style at a media query, use `[style]` attribute selector + `!important`. Session 37 mobile fix uses `.ed-press .head h2[style] { font-size: 28px !important; max-width: 100% !important; }`.
- **CSS Grid items default to `min-width: auto`** (= min-content). For text, min-content is the longest single word. Italian "pubblicazioni" or Arabic display words can force a grid column wider than the viewport. Fix: explicit `min-width: 0` on grid children at mobile breakpoints. Session 37 added this for `.ed-press .head[style] > *`.
- **Browser cache + dev server combo is a pitfall.** After major template changes, kill + restart dev server on a fresh port (e.g. 8767 vs 8765). The Session 37 mobile fix appeared not to apply until the server was bounced — same class as Session 19's ghost-server gotcha and Session 23's stale `runserver --noreload` trap.
- **Smoke patterns must avoid Romance-language word collisions.** Italian "Disciplina" / "Colophon" / "Metro" are valid Spanish/English/French words too — checking for them as "IT leak" produces false positives on EN/FR/ES pages. Session 37 smoke restricts the leak pattern to IT-specific phrasings ("Sintesi del progetto", "Deliverable consegnati", "Sequenza", "Indirizzo", "Ingresso", "Orari", "Equipe" without French acute accent, etc.).
- **Latin proper names + Latin digits + Arabic body text** is the editorial AR voice — don't transliterate. The CSS `font-family` stack keeps Latin runs in JetBrains Mono / Latin fallback so they stay legible against Amiri body. The cardio/derm/gusto AR pages all do this; chiara now joins.
- **Sub-agent prompts must mention the actual IT key shape.** Session 37 prompt initially mentioned `ledger_count_format` / `step_index_format` (placeholder format-strings) but the IT source actually uses pair-form keys (`_prefix` + `_unit`). All 4 sub-agents independently caught this via deep-comparison and corrected to mirror the true IT shape — flagged as a lesson for future locale rollouts: always read the IT source first, not the prompt's key list.

---

## Session 36 — i18n & Media Coherence: Read This Before Adding New Blocks or Promoting IT-Only Templates (2026-04-13)

**Session 36 is a hardening pass on Session 35's motion/media work (D-068).** The 7 `tier=published_live` templates now satisfy two coherence gates the user flagged:

1. **Language switcher honesty.** The 4 IT-only templates (Pragma, Elevate, Chiara, Pixel) no longer show a 5-pill switcher that silently fell back to Italian. `locale_switcher_entries(current_locale, available_locales)` is now template-aware, and `LiveTemplateView` computes `available_locales` via `template_content.get_available_locales(slug)`. When `len <= 1`, the switcher context value is an empty list and every skin's markup is guarded by `{% if locale_switcher %}`. The 3 multilingual templates (Cardio, Derm, Gusto) keep their 5-pill strip as before.

2. **Media honesty.** The 3 `lm-video` blocks introduced in Session 35 all shipped with the same Big Buck Bunny placeholder MP4 and codec-theatre metadata. They are now resolved per-archetype:
   - **Gusto signature_video** — REMOVED (content block + HTML + CSS). The atmosphere_teaser lightbox already carries BTS mood.
   - **Pixel reel** — REMOVED. The filmstrip + EXIF strip + series index already carry the cinematic identity.
   - **Elevate product_video** — CONVERTED to `product_demo_card`: same cosmic-glass frame + dashboard poster, now with a dual CTA overlay pointing to `/demo/` + `/prodotto/`. No `<video>` tag, no codec metadata.
   - **Pragma + Elevate marquees** — kept (real institutional B2B wordmarks + real SaaS integration names).

Orphan `live-media.css/js` links + `--lm-video-*` tokens pruned from bases that no longer consume them (Cardio, Derm, Gusto, Chiara, Pixel). Pragma + Elevate still link the primitive because they render marquees.

### Current stable state

- 7/20 templates `tier=published_live` (unchanged from Session 34).
- All 7 pass D-069 coherence gates.
- 170/170 full route sweep + 27/27 form sweep + 45/45 new hardening smoke (`smoke_i18n_media_hardening.py`) all green.
- `live-media.css/js` remains in the repo as a latent capability — re-introduce when a real signed MP4 and on-brand metadata exist.

### What to do next (priority order)

1. **Phase 2g3.5 — agency CRITICO lift.** Same D-047 + D-054 recipe as Sessions 17 / 18 / 32 / 34. Blocking roadmap gate per D-049.
2. **Phase 2i.2b — IT-only template locale rollout.** Author EN/FR/ES/AR content trees for Pragma / Elevate / Chiara / Pixel (one per session, ~3h each per D-063 budget). When `TEMPLATE_CONTENT[slug]` gains a second locale key, the switcher reappears automatically — the `{% if locale_switcher %}` guards installed in Session 36 already handle the re-activation.
3. **Phase 2g2x.1 remainder** — lift lawyer + real-estate CRITICO. Same DNA-split recipe (Sessions 17–19 precedent).
4. **Editor app** — do NOT start until Phase 2g3.7 closes. D-049 roadmap freeze still in effect. When it starts, `EDITOR_SCHEMA_BLUEPRINT.md` is the contract.

### Do NOT do

- Do NOT re-introduce a placeholder MP4 as an `lm-video` src. Either the source is a real brand asset or the block is not in the template. D-069 is binding.
- Do NOT ship a 5-pill language switcher on a template whose `TEMPLATE_CONTENT[slug]` has only one locale key. D-069 is binding.
- Do NOT add codec-theatre metadata (`4K`, `1080p`, `24 fps`, `Play · 3:12`) to any block where it does not genuinely reinforce the template's identity.
- Do NOT add a new content block on the IT tree without either (a) mirroring it in the 4 non-IT locale trees at the same commit or (b) documenting that the block is IT-only-intentional in a comment adjacent to the key. Silent content-depth disparity between locales is the Session 35 antipattern that produced the Session 36 cleanup.
- Do NOT revert the `live-media.css/js` unlinking on cardio/derm/chiara/pixel/gusto bases unless you are re-adding a real `lm-video` block at the same commit. Orphan primitive links are payload dead-weight.
- Do NOT open auth / checkout / editor / projects / commerce / dashboard / new categories / new templates.

### Gotchas (Session 36)

- **CSS rules for `.mp-lang*` appear in the inline `<style>` block on every page** — this is structural, not rendered chrome. Smoke tests for "switcher absent" must look for `<div class="mp-lang"` / `<nav class="mp-lang"` opening tags, not the class name alone. `smoke_i18n_media_hardening.py` does this correctly.
- **The `--lm-video-*` CSS custom properties were spread across many `:root` blocks.** Removing them requires touching every skin `_base.html` that linked live-media.css speculatively (cardio/derm/gusto/chiara/pixel). Pragma + Elevate keep their `--lm-marquee-*` tokens because they still render marquees.
- **Elevate's `.sl-product-video .head .sec-label.sl-mono` specificity-shielded selector** must be renamed to `.sl-demo-card .head .sec-label.sl-mono` after the video→demo_card conversion, otherwise the mono utility silently stops working on that element. Check any rule that chains on deprecated class names whenever a section is renamed.
- **The `--lm-video-*` specificity rule `.lm-video .lm-video-play-label.cp-mono` in the cinematic-photographer base** was orphaned after the reel removal. Pruning it was part of the cleanup. Same class of orphan risk for any future skin that declares `.lm-video` specificity-shielding rules: if the block is later removed, the rule becomes dead.
- **Elevate's existing `.sl-btn` has a `::after { content: '→' }` globally.** Adding a custom `<span class="arr">→</span>` inside a button duplicates the arrow. The demo card uses the standard `.sl-btn` primary + `.sl-btn.secondary` classes and lets the global arrow handle the glyph. When extending a button class, check for `::after` content before adding custom glyphs.

---

## Session 30 — Premium Component Blueprint: Read This Before Adding Sections or Opening the Editor (2026-04-13)

**Session 30 enriched the 3 `tier=published_live` templates with DISTINCT premium sections per archetype AND authored a concrete Editor Schema Blueprint** (~600 lines, `EDITOR_SCHEMA_BLUEPRINT.md` in repo root). The blueprint is binding for the future customer-personalization editor app.

### What was added (distinct per template by design)

| Template | New sections | New interactions |
|----------|-------------|-----------------|
| Cardio | anchor subnav + "Percorso paziente" 5-step timeline + "Garanzie & trasparenza" trust strip + location block with static map | anchor-nav (IO active state + smooth scroll) |
| Derm | Treatment tabs (3 domains: clinica/chirurgia/estetica) + Before/After compare slider with ethical disclaimer + Editorial press feed 4-tile | Tabs (keyboard nav), Compare slider (mouse/touch/keyboard) |
| Gusto | Producer showcase (4 artisans) + Private dining card (Chef's Table / evening buy-out / cellar tasting) + Wine program (sommelier + pairings + cellar facts) | — (reuses existing lightbox) |

All sections conditional on `page_data.X` so the shared specialist skin never renders the wrong set on the wrong template.

### New interaction primitives (live-interactions.css/js)

- `[data-li="tabs"]` — keyboard-accessible tab bar with fade panel transitions.
- `[data-li="compare"]` — before/after slider, mouse+touch+keyboard, clip-path driven.
- `.li-anchor-nav` — sticky subnav with IntersectionObserver active state.

All zero-dep, `prefers-reduced-motion` aware, graceful without JS.

### i18n coverage

All new sections authored in all 5 locales (it/en/fr/es/ar) for all 3 templates. Native editorial voice per locale — no machine translation. Proper names stay Latin across AR.

### Current stable state

- 3 published_live with FULL premium depth (~650+ lines per home, dense with motion + interactions + per-archetype sections).
- 85/85 routes 200 across all locales + pages.
- Cross-contamination zero. Differentiation strong.
- 17 drafts unchanged.

### Editor Schema Blueprint (EDITOR_SCHEMA_BLUEPRINT.md)

Concrete (not theoretical). Covers:
- Component registry: 8 edit targets (nav/hero/section/form/contact/blog/footer/locale).
- 20+ section kinds with items shapes.
- 23 atomic field types for editor UI.
- Design tokens scope (palette/fonts/radius/motion_profile/density/alignment).
- 6 hard invariants (D-047, D-053, D-054, D-057, D-058, D-059).
- Persistence model (CustomerProject + ProjectContent + ProjectDesignTokens) — specified, not migrated.

When Phase 2g3.7 closes and the editor worktree opens, this document is the implementation TODO. Read it end-to-end before touching `apps/editor/`.

### Do NOT do

- Do NOT add premium sections to drafts. Phase 2g3 authoring follows a different flow (full skin folder, then enrichment).
- Do NOT replicate the same section set across the 3 templates — that would collapse the D-054 differentiation earned in Sessions 26/28/30.
- Do NOT start implementing the editor until Phase 2g3.7 is green. D-049 roadmap freeze is still in effect.
- Do NOT add arbitrary Google Fonts to templates. The blueprint curates 18. Anything else regresses D-040.
- Do NOT modify `live-motion.css` tokens per-template — use motion_profile from the blueprint.
- Do NOT machine-translate any locale block. Native editorial voice remains non-negotiable.
- Do NOT add `href="#"` placeholders. Every CTA must resolve.
- Do NOT wire a compare slider inside an RTL-first section without confirming label flip works. The drag itself is LTR-mouse-driven by design.

### What to do next (priority order)

1. **Phase 2g3.1** — author Sapore + Brace restaurant skin folders. They inherit restaurant-generic CHROME_I18N keys from Session 29 for free. When their homes are ready, they can optionally opt into a subset of new primitives (e.g., anchor-nav for long trattoria menus; tabs for Brace delivery vs dine-in).
2. **Phase 2g2x.1 remainder** — lift agency / lawyer / real-estate CRITICO. Same Option A recipe (Sessions 17–19 precedent, now with even more authored sections to reference).
3. **Phase 2i.3 deferred** — marketplace chrome i18n lives when Phase 3 unblocks.
4. **Editor app** — do NOT start until 2g3.7 green. When it starts, `EDITOR_SCHEMA_BLUEPRINT.md` is the contract.

### Gotchas (Session 30)

- Clip-path animation on the compare slider is JS-driven (inline `clipPath` overrides CSS). To flip direction per-locale, change the JS, not the CSS.
- The `.sp-compare .cmp-box` container MUST have `tabindex="0"` for keyboard accessibility. Missing it breaks ←/→ control.
- The anchor-nav IntersectionObserver rootMargin is `-100px 0px -50% 0px` — tuned so a section "becomes active" when it's ~halfway up the viewport, not as soon as a pixel touches top.
- Windows cp1252 console cannot print Arabic in stdout. Smoke scripts need `sys.stdout.reconfigure(encoding='utf-8')` or ASCII-only output. Same gotcha as Session 29.
- New section CSS blocks (e.g., `.sp-tabs`, `.sp-compare`) live in the SHARED specialist `home.html` style block. Cardio renders the CSS but not the HTML (content-conditional). This is intentional: the CSS cost is negligible (~40KB unminified), and splitting into two home.html files would break the D-046 archetype-reuse recipe.

---

## Session 29 — Gusto i18n/RTL: Read This Before Touching Multilingual Publishing (2026-04-13)

**Session 29 closed Phase 2i.2 in full.** All 3 `tier=published_live` templates (cardio, dermatologia-elite-roma, gusto-fine-dining) now ship in 5 locales (it/en/fr/es/ar) with real RTL for Arabic. The pilot architecture (D-059) is validated across two archetypes — specialist (medical) and fine-dining (restaurant).

### What was added
- `apps/catalog/template_content_gusto_i18n.py` — 4 hand-authored content trees (EN/FR/ES/AR) for gusto, ~1250 lines, restaurant-hospitality native voice per locale.
- 9 new CHROME_I18N keys × 5 locales: `mp_other_restaurant`, `foot_restaurant`, `foot_concierge`, `foot_services`, `fd_wine_pairing`, `fd_email_label`, `fd_phone_label`, `blog_read_article`. These are restaurant-category-generic → reusable by draft Sapore + Brace in Phase 2g3.1.
- Gusto-specific content keys on `GUSTO_CONTENT_IT` for every previously-hardcoded HTML literal (~30 new keys across home/filosofia/menu/atmosfera/diario/prenota).
- `html[dir="rtl"]` CSS block inside `fine-dining/_base.html` — core RTL tokens always applied, page-level `.fd-*` flips inside `{% if is_rtl %}` so LTR pays zero CSS cost.
- Conditional Amiri + Noto Kufi Arabic Google Fonts (only loads for AR).
- Language switcher pill strip in mp-bar, `?lang=` URL preservation on every nav/footer/CTA link.
- Reservations form rewritten as a `{% for field in page_data.form_fields %}` loop with conditional rendering by type + index.

### Current stable state
- **3 published_live templates:** cardio + derm (medical specialist archetype, i18n in 5 locales since Session 23/24) + gusto (fine-dining archetype, i18n in 5 locales since Session 29).
- **All 3 have motion active** (D-058 + D-061) and ultra-premium sections (D-062).
- **17 draft templates:** hidden from public, IT-only.
- **52/52 routes green** in Session 29 smoke test (35 gusto + 10 cardio regression + 5 derm regression + 2 negative).

### The reusable recipe (now proven twice)
1. Create `template_content_<slug>_i18n.py` with 4 locale trees (EN/FR/ES/AR). Premium editorial voice per locale. No machine translation.
2. Wire into TEMPLATE_CONTENT registry (4 lines: import + 4 locale keys).
3. Extend CHROME_I18N with archetype-generic keys if needed (restaurant-generic keys from Session 29 are already done for any future restaurant archetype).
4. Add all hardcoded HTML labels to the `*_IT` content block as new keys, then mirror in the 4 locale trees.
5. Wire HTML templates: `{{ chrome.* }}` for cross-archetype chrome, `{{ page_data.* }}` for brand-specific labels, `{{ site.* }}` for site-wide chrome (wordmark, copyright, footer hours).
6. Add `?lang=` preservation to every URL: `{% url '...' %}{% if locale != default_locale %}?lang={{ locale }}{% endif %}`.
7. Author `html[dir="rtl"] ...` CSS block inside the archetype's `_base.html` with (a) core typography tweaks (Amiri + Noto Kufi Arabic, 17px body / 1.85 line-height, letter-spacing flatten, arrow/bar flips), plus (b) page-level section flips inside `{% if is_rtl %}` for grid flipping + border-side swap + drop-cap float + column alignments.

Budget per template: ~3h (same as Session 29 estimate).

### What to do next (in priority order)
1. **Phase 2g3** — live skin folder authoring for draft templates, cheapest-first per CATEGORY_ROADMAP.md. Restaurant first (Sapore + Brace) — they'll inherit the 7 restaurant-generic CHROME_I18N keys for free, and the i18n/RTL pattern is proven.
2. **Phase 2g2x.1 remainder** — lift the 3 CRITICO categories (agency, lawyer, real-estate) with DNA splits. Pattern proven in Sessions 17–19.
3. **Phase 2i.3 (deferred to Phase 4)** — marketplace chrome i18n. Keep `CHROME_I18N` as the natural migration target if/when the marketplace surface moves to Django `{% trans %}`.

### Do NOT do
- Do NOT re-author the i18n architecture — the pilot closed in full. D-059 + D-063 are binding.
- Do NOT introduce Django gettext/.po/middleware. Same as Session 23/24/29.
- Do NOT translate draft templates. Only `tier=published_live` is in 2i scope.
- Do NOT translate marketplace chrome (homepage, listing, detail, category, search) — deferred to Phase 4.
- Do NOT modify cardio or derm i18n content without a documented reason. They're load-bearing regression baselines.
- Do NOT touch Gusto motion tokens (`--lm-rise: 14px`, image zoom, nav sweep) — they're intentionally different from the medical clinical profile.
- Do NOT add counter animations to medical templates (D-061 exclusion).
- Do NOT machine-translate any new locale block. Native editorial voice is the non-negotiable quality floor.
- Do NOT strip Latin from the Arabic font stack — mixed Latin/Arabic strings (chef names, producer names, wine names, press outlets, phone, email, address) must stay legible.
- Do NOT apply negative `letter-spacing` or 0.22em uppercase tracking on Arabic headings/chrome labels — the `html[dir="rtl"]` core block explicitly zeroes these.
- Do NOT open auth/checkout/editor/projects/commerce (Phase 3 gated by Phase 2g3.7).
- Do NOT add new categories or templates before the 20 existing are all `published_live`.

### Gotchas (Session 29)
- **Django template `split` filter doesn't exist.** Don't try to split a slash-separated string inside the template — expose the options as a separate list field in the content registry (`occasion_options`).
- **Windows cp1252 console can't print Unicode ✓/✗.** Use ASCII `OK`/`FAIL` labels in smoke-test scripts.
- **Arabic drop-caps need manual letter selection.** Can't grab `text[0]` in a template — choose the drop-cap letter at authoring time per locale (e.g. "ق" for the manifesto, "د" for the blog body).
- **Latin wordmark must stay Latin in RTL.** The restaurant brand name "Osteria Moderna" should render in Playfair, not Amiri — explicit `html[dir="rtl"] .fd-nav .logo .name` override pins the font.

---

## Session 27 — Medical Motion Opt-In: Read This Before Touching Specialist Motion (2026-04-12)

**Session 27 applied the live motion language (D-058) to the specialist archetype with a clinical motion profile (D-061).** Both `cardio-studio-specialistico` and `dermatologia-elite-roma` now have scroll reveals, staggered entry, CTA hover refinement, and image attention lift — all more restrained than Gusto's restaurant motion.

### What was added
- `live-motion.css` + `live-motion.js` linked in specialist `_base.html`
- Medical motion profile tokens: `--lm-rise: 10px`, `--lm-rise-lg: 16px`, `--lm-dur-slow: 680ms`
- 4 pattern categories across all 8 page templates: reveal-on-scroll, stagger, CTA hover, image filter lift
- RTL-aware arrow shift on gold-btn hover
- `prefers-reduced-motion` guards on all hover enhancements

### Current stable state
- **3 published_live templates:** cardio + derm (with motion + i18n 5 locales), gusto (with motion, IT-only)
- **All 3 have motion active** — the interaction-quality floor from D-058 is fully met
- **17 draft templates:** hidden from public
- **34/34 routes green**, zero regressions, zero cross-contamination

### Motion differentiation (important for future work)
- **Gusto** — `--lm-rise: 14px`, image zoom (scale 1.045x), nav underline sweep, cinematic feel
- **Medical** — `--lm-rise: 10px`, image filter lift (no zoom), no nav sweep, clinical precision
- These profiles must remain distinct per D-054 premium differentiation law
- Future archetypes should define their own token profile

### What to do next (in priority order)
1. **Phase 2g2x.1** — lift the 3 remaining CRITICO categories (agency, lawyer, real-estate) with DNA splits. The pattern is proven (Sessions 17–19).
2. **Phase 2i.2 step 2** — gusto i18n (new `.fd-*` RTL CSS block + 4 content trees). ~3h budget.
3. **Phase 2g3** — live skin folder authoring for draft templates, cheapest-first order per TODO_NEXT. Each new `published_live` template must adopt the motion language as gate 10 of D-053.

### Do NOT do
- Do NOT modify Gusto's motion tokens or attributes — they are intentionally different from medical
- Do NOT add counter animations to medical templates (excluded by D-061 as too promotional)
- Do NOT re-scatter fixes into new worktrees without consolidating back
- Do NOT open auth/checkout/editor/projects/commerce (Phase 3 gated by Phase 2g3.7)
- Do NOT add new categories or templates
- Do NOT reopen drafts or change tiering policy
- Preview PNGs should be regenerated with `--force` whenever a preview composition changes

---

Previous (still relevant):

## Session 23 — i18n/RTL Pilot Cardio: Read This If You're Touching Localization (2026-04-11)

**Session 23 shipped the first multilingual publishing architecture on a `tier=published_live` template.** Cardio-studio-specialistico now renders in 5 locales (it/en/fr/es/ar) with real RTL for Arabic. This is the reusable recipe for Phase 2i.2 rollout to dermatologia and gusto. Short read, load-bearing:

- **D-059 — i18n/RTL Pilot Architecture.** Locale-keyed content registry (`TEMPLATE_CONTENT[slug][locale] → content tree`) + `CHROME_I18N[locale][key]` dict for the ~30 chrome labels the skin itself renders + `?lang=xx` query-param resolved in `LiveTemplateView.setup()` + RTL-scoped CSS block inside each archetype `_base.html`. **No Django `{% trans %}` / `.po` / `gettext` tooling** was introduced — the pilot's job was to prove the shape with ZERO new build tooling. Phase-later migration to `{% trans %}` for the marketplace chrome itself is trivial because every string is already locale-namespaced.
- **Where it shipped:** `apps/catalog/template_i18n.py` (new) + `apps/catalog/template_content_cardio_i18n.py` (new, 4 non-IT content trees) + `apps/catalog/template_content.py` (top-level shape changed to `{slug: {locale: tree}}`, derm/gusto wrapped under `{"it": ..._IT}`) + `apps/catalog/views.py` (`LiveTemplateView` threads locale) + all 9 specialist skin files (`_base.html` + home/about/services/team/contact/appointment/blog_list/blog_detail; `team.html` needed zero edits).
- **Validation:** 51/51 smoke test green (45 cardio routes × 5 locales + 6 regression/negative). Playwright walk at 1440×900 on IT/EN/AR/FR/ES home + AR contact + FR services + ES blog detail confirmed layout integrity. Mobile sanity at 390×844 confirmed zero new horizontal overflow.
- **Rejected:** Django `{% trans %}` (build-step tooling, splits strings across files), `django-modeltranslation` (wrong shape for structured content), per-locale URL maps (out of pilot scope), machine translation (violates premium positioning).

### What's next for the i18n pilot (Phase 2i.2, in order)

**Step 1 — Dermatologia (cheapest, same skin):**
- [ ] Create `apps/catalog/template_content_dermatologia_i18n.py` with 4 hand-authored content trees (EN/FR/ES/AR). Use the Session 23 voice guidelines: EN Anglo-American clinical, FR classical French + `vous`, ES peninsular, AR formal MSA + native punctuation (« »).
- [ ] Update `TEMPLATE_CONTENT["dermatologia-elite-roma"]` in `template_content.py` to import all 5 locale keys.
- [ ] Run the route sweep + Playwright walk.
- [ ] Budget: ~1.5h — no new HTML, no new CSS, the specialist skin's RTL block is already in place.

**Step 2 — Gusto (adds a new RTL CSS block for the fine-dining archetype):**
- [ ] Create `apps/catalog/template_content_gusto_i18n.py` with 4 hand-authored content trees for the 7 gusto pages. **Note the tone differs** — gusto is dark-editorial Michelin fine dining, not medical clinical. EN is "one service per night" not "a tailored consultation". AR needs Arabic restaurant vocabulary, not medical vocabulary.
- [ ] Author a new `html[dir="rtl"] ...` CSS block inside `templates/live_templates/restaurant/fine-dining/_base.html`. Copy the shape from the specialist `_base.html` RTL block and rename the selectors (`.sp-*` → `.fd-*`). Flip `.fd-nav`, `.fd-hero`, `.fd-chef .portrait`, `.fd-courses`, `.fd-form-band`, etc.
- [ ] Gusto's `_base.html` has its own set of ad-hoc literal labels (different from specialist). Either extend `CHROME_I18N` with the additional keys or factor a per-archetype extension pattern. Decision deferred to the next session.
- [ ] Budget: ~3h — new content trees + new RTL CSS + chrome wiring.

### Do NOT do (i18n pilot scope)

- Do NOT introduce Django `{% trans %}` / `.po` / `gettext` tooling. D-059 is explicit about this.
- Do NOT translate draft templates. Only `tier=published_live` templates are in Phase 2i scope.
- Do NOT translate the marketplace chrome (homepage, listing, detail, category). That's a Phase 4 decision.
- Do NOT use machine translation on any locale block. The pilot's quality floor is native editorial voice. A PR that ships auto-translated content should be rejected.
- Do NOT change URL patterns to add per-locale prefixes (`/en/preview/...`). The pilot uses `?lang=xx` query param and the URL pattern file is untouched. Prefix routing is a Phase 4 decision tied to the marketplace chrome migration.
- Do NOT translate page slugs. Only labels change per locale. `studio`, `visite`, `medici`, `pubblicazioni`, `contatti`, `richiedi-visita` stay Italian across every locale — avoids per-locale URL maps and works for Arabic (ASCII URLs).
- Do NOT remove the IT fallback in `pick_localized`. The transitional shape where derm+gusto get English CHROME but Italian CONTENT is load-bearing during Phase 2i.2 rollout — templates without a locale block must still render.
- Do NOT strip Latin from the Arabic font stack. The font-family override for `--heading` and `--body` keeps `{{ theme.heading_font }}` as a fallback so mixed Latin/Arabic strings (doctor names, press outlets, dates, phone numbers, addresses) stay legible.
- Do NOT apply negative `letter-spacing` or 0.22em uppercase tracking on Arabic h1-h5 or chrome labels. Arabic glyphs don't want Latin typographic conventions — the `html[dir="rtl"]` block zeroes them explicitly.

### Gotcha: Django template variable identifiers cannot begin with `_`

First draft of `_base.html` used `{% url ... as _base_url %}` inside the language switcher loop. Django's `FilterExpression` rejected it with `TemplateSyntaxError: Variables and attributes may not begin with underscores: '_base_url'`. Renamed to `lang_base_url`. If you see this error in any future work, the fix is always "rename the variable to remove the leading underscore".

### Gotcha: stale runserver (same class as Session 19 + 22)

First browser walk showed zero language pills because the `runserver --noreload` process on port 8765 was still serving the pre-edit HTML from memory. Killed + restarted on port 8766 — correct fresh HTML. Lesson unchanged from prior sessions: if the browser walk shows "my edits aren't landing" but the file-on-disk confirms they ARE, restart runserver on a fresh port before blaming anything else.

---

Previous (still relevant):
Last updated before Session 23: 2026-04-11 — after **Session 22 Motion Pilot Gusto (Phase 2g2x.9)**

## 🎬 Session 22 — Motion Pilot Gusto: Read This If You're Animating Anything (2026-04-11)

**Session 22 added a small, reusable, dependency-free premium motion system to the first tier=published_live template.** This is the interaction-quality floor for every future `published_live` template. Short read, but load-bearing:

- **D-058 — Live Motion Language.** Two static files — `static/css/live-motion.css` + `static/js/live-motion.js` — exposing a 3-attribute contract (`data-lm="reveal|reveal-lg|reveal-soft|counter"`, `data-lm-stagger`, `data-lm-to`) plus a wrapper+inner-bg image-hover pattern. Strictly opt-in per skin: one `<link>` in `<head>` + one `<script defer>` before `</body>`. No-JS fallback via `body.lm-ready` gate. Reduced-motion via `@media` + `body.lm-reduced` double guard.
- **Where it shipped:** `templates/live_templates/restaurant/fine-dining/_base.html` links the two files, and all 7 inner pages (home / menu / about / gallery / reservations / blog_list / blog_detail) tag their reveal targets.
- **Patterns used:** scroll-reveal (fade + rise), staggered children (70–110ms unit), count-up on home facts (suffix preserved), image-zoom on hover (900ms slow scale via inner `.bg` layer inside an `overflow: hidden` wrapper), CTA arrow shift + letter-spacing widening, nav underline sweep.
- **Rejected:** parallax, sliders, bounce easing, blur-in, loud marquees. See SESSION_LOG Session 22 § 1.

### What's next for the motion pilot (not blocking Phase 2g3, but cheap)

**Opt-in pass for the other two `published_live` templates:**
- [ ] Cardio (`templates/live_templates/medical/specialist/_base.html`) — link motion CSS + JS, tag reveals on the specialist skin pages. Should be a short session because the chrome is already D-047 clean. Dermatologia-elite-roma shares the same skin so it benefits for free.
- [ ] BRAND_SYSTEM_GUIDELINES.md gets a new "Motion Language" pointer section citing D-058.

**Phase 2g3 impact:**
- Every template flipped from `draft` → `published_live` MUST adopt the motion pilot as part of its D-053 acceptance checklist. The checklist in TODO_NEXT.md § 2g3.0 grew a new row: "Motion pilot adopted — reveal + stagger on home page at minimum, counters where numeric facts exist, image-hover where image frames exist." This is the interaction-quality floor; minimum opt-in is cheap (link + script + a handful of attributes).

### Do NOT do (motion pilot scope)

- Do NOT add the motion pilot to the marketplace surface (`base.html`, listing pages, detail page). The system is scoped to standalone live-template skins. The marketplace has its own interaction language.
- Do NOT apply motion to the preview composition files under `templates/preview_compositions/`. Those files are captured as static PNGs by Playwright and the reveal hidden-state would produce blank screenshots.
- Do NOT add heavyweight animation libraries (GSAP, AOS, Framer Motion, LocomotiveScroll). The whole point of the pilot is zero dependencies. If a specific archetype needs something the pilot doesn't offer, extend the pilot — don't bypass it.
- Do NOT break the no-JS fallback. The `body.lm-ready` gate is load-bearing: without it a JS-disabled user sees a blank page.
- Do NOT skip `prefers-reduced-motion`. Both the `@media` rule AND the `body.lm-reduced` class must continue to collapse motion cleanly.
- Do NOT apply `data-lm-stagger` to a parent whose direct children use `display: contents` — opacity/transform don't work on box-less elements. Fall back to plain `data-lm="reveal"` on the wrapper. See SESSION_LOG Session 22 § 5 "gotchas".
- Do NOT bulk-apply `data-lm="reveal"` to every element. The pilot is a judgment-call tool, not a batch-apply one. The Gusto adoption picked ~18 reveal targets on the home page out of ~50+ eligible elements — the unchosen ones stay instant so the cadence has contrast.

### Gotcha: stale runserver

Session 22 hit a Windows + StatReloader edge case where the initial runserver process kept serving pre-edit HTML after rapid template file changes, even though the files on disk had the updates. Killing the process and restarting on a fresh port produced the correct fresh HTML. Same class of repro as Session 19's ghost dev-server. If you ever think "my edits aren't landing" but `grep` of the files confirms they ARE on disk, just restart runserver before blaming template cache or ALLOWED_HOSTS.

---

## 🛑 Session 20 — Policy Binding: Read This Before Anything Else (2026-04-11)

**Session 20 was documentation-only — no code, no HTML, no previews, no commits of anything except doc deltas.** But it re-defined the product's floor with four formal decisions you MUST read before touching any catalog-facing work:

- **D-053 — Live Preview Law.** A template is `published_live` only when it has DNA + content registry + skin folder + all routes 200 + D-047 leak sweep clean + visual walk + card-size sibling test + preview PNG + working CTA. No exceptions.
- **D-054 — Premium Differentiation Law.** Every sibling pair must differ on 10 dimensions (hero image / dominant imagery / silhouette / section order / CTA phrasing+pattern / block rhythm / macro tone / imagery direction / typography / inner pages). Applies globally, retroactively, across every category and every template.
- **D-055 — Template Tier Model.** Two tiers only: `published_live` (public) / `draft` (hidden). No intermediate `published_static`. Today only 3 of 20 templates satisfy `published_live` — the other 17 must be demoted to `draft` in Phase 2g2x.8.
- **D-056 — Catalog Honesty.** The legacy `href="#"` "Anteprima Live" CTA gets deleted as part of Phase 2g2x.8. D-045 is superseded. Phase 2g2x.7's three-option punch list is absorbed by tier gating.

Read `DECISIONS.md` D-053 → D-056 in full before you start. They are the source of truth. This file is the summary.

### What's next — in order, no skipping

**Step A — Finish Phase 2g2x.1 on 3 CRITICO categories** (still the blocking roadmap gate per D-049):
- `real-estate.html` identity crash (Casa mass-market vs Villa ultra-luxury) — recommended first, cleanest pair
- `lawyer.html` identity crash (Lex 1962 heritage vs Juris modern/accessible) — second
- `agency.html` identity crash (Vertex bold vs Aura minimal — 6 shared fake case studies) — third, heaviest leak surface
- Use the Session 17 + Session 18 Option A recipe. Author under D-047 from line one. Bidirectional leak sweep + route sweep + Chromium visual walk per category.

**Step B — Phase 2g2x.8 tier migration** (cheapest implementation wave that makes the policy bind):
- Add `tier` field to `WebTemplate` (or repurpose `status`)
- Seed cardio / dermatologia-elite-roma / gusto-fine-dining as `published_live`, everyone else as `draft`
- Filter listing / detail / homepage / category / search to `tier='published_live'`
- Delete the `href="#"` branch in `templates/catalog/template_detail.html` lines 132-136 and the `has_live_preview` context var
- Ship a category-page empty state ("in arrivo") for categories that temporarily show zero live templates
- Add staff `?preview=1` escape hatch for in-progress work
- Exit criteria in `TODO_NEXT.md` Phase 2g2x.8

After Step B lands, the visible catalog is 3 real, complete, navigable products. That is the policy-compliant floor.

**Step C — Phase 2g3 live-preview rollout** (the long wave that brings the 17 drafts up to `published_live`):
- Order: restaurant → medical → business → portfolio → ecommerce → agency/lawyer/real-estate (last three blocked until Step A closes)
- Per-template acceptance checklist in `TODO_NEXT.md` Phase 2g3.0 — run it end-to-end on every single template
- Baseline live page-kind set per category in `CATEGORY_ROADMAP.md` — every skin must cover the baseline minimum
- Phase 2g3.7 exit criteria = Phase 3 unblock gate. Auth / checkout / editor / projects / commerce do NOT start before this gate.

### Do NOT do

- Do NOT open auth / checkout / editor / projects / commerce / dashboard — these are gated on Phase 2g3.7 per D-049 + D-053
- Do NOT add new categories or new templates before the 20 existing ones are all `published_live`
- Do NOT ship a template with "home page only + inner pages coming later" — D-053 says the inner pages are part of the gate
- Do NOT introduce a `published_static` tier or any variant — D-055 rejected Options B/C/D explicitly
- Do NOT preserve the `href="#"` CTA in any form — D-056 deletes it
- Do NOT treat the Premium Differentiation Law as optional polish — D-054 is a hard gate
- Do NOT skip the category-page empty state when a category becomes temporarily empty — leaving a ghost grid is worse than showing "in arrivo"

### Doc delta from Session 20

Touched in this session:
- `DECISIONS.md` — added D-053, D-054, D-055, D-056 (marked D-045 as superseded in the D-056 consequences)
- `TODO_NEXT.md` — added Phase 2g2x.8 (tier migration) + Phase 2g3 (live preview rollout, 2g3.0–2g3.7)
- `CATEGORY_ROADMAP.md` — added baseline live pages per category + rollout order + cumulative milestones + category-ready test
- `BRAND_SYSTEM_GUIDELINES.md` — added Premium Differentiation Law pointer (appendix)
- `CONTENT_GUIDELINES.md` — added Inner Pages Law pointer (appendix)
- `TEMPLATE_REGISTRY.json` — v0.7.3 → v0.8.0, `tier` field on every row
- `SESSION_LOG.md` — Session 20 entry prepended
- `AGENT_HANDOFF.md` — this section
- `memory/live_preview_policy_session20.md` + `memory/MEMORY.md` index — new auto-memory entry

Not touched: any code, any HTML, any CSS, any preview PNG, any migration, any view, any seed, any CLAUDE.md.

---

## ✅ Session 19 — Portfolio Blocker Cleared (2026-04-11)

**Session 18 declared portfolio approved, but a manual verification pass found a real layout-overflow bug in Chiara's detail preview.** A strictly-scoped Session 19 triage confirmed the bug was reproducible, surgically fixed it with the minimum possible footprint, and cleared the commit blocker.

### The fix (D-052)
- `templates/preview_compositions/portfolio/editorial-designer-grid.html`: `.ed-hero` padding tightened (72 72 42 → 52 72 38), `overflow: hidden` added as safety net; `.ed-left h1` dropped from 82 px to 62 px with matching line-height / letter-spacing / margin-top / max-width adjustments; `.ed-left .sub` + `.ed-left .cta-row` margins tightened.
- `apps/catalog/template_dna.py`: `chiara-portfolio-creativo.content.headline` trimmed from 57 chars to 47 chars. New headline: `'Identità visive, <em>una griglia alla volta</em>.'`. Both key signals preserved (`identità visive` = profession, `una griglia alla volta` = craft metaphor). The trim also creates a deliberate syntactic parallel with Pixel's `'Fermare il tempo, una luce alla volta.'` — both siblings now use the `'…, una X alla volta.'` structure with X being the medium of each profession.

### Validation that held (Session 19 delta)
- `python manage.py check` — clean
- `python manage.py generate_previews --only chiara-portfolio-creativo --force` — green
- Orphan cleanup — all three `_<hash>.png` intermediate files removed, final asset restored to canonical `chiara-portfolio-creativo-preview.png` via shell (media/ now has exactly one PNG per template)
- Playwright visual walk at 1440×900 on a fresh dev server: portfolio listing, Chiara detail, Pixel detail all clean, zero overlap. Differentiation vs Pixel strengthened (not weakened) via the headline parallel.

### Three operational gotchas surfaced during Session 19

1. **Stale dev-server ghost.** The first browser walk showed legacy "Ogni progetto una storia" content in the Chiara detail page. Root cause: a **stale `runserver --noreload` process (PID 29132)** was still listening on port 8765 from a prior session's worktree and serving a completely different PNG at the same URL as what was physically on disk. **Before any visual walk, kill lingering `runserver` processes on your target port** — or just use a fresh port. Python `urllib.request.urlopen()` + a cache-busting `?v=N` query string is the fastest way to confirm the dev server is serving the same bytes as disk.
2. **`generate_previews --force` creates orphan files.** Django's `FileSystemStorage.get_available_name()` appends a `_<hash>.png` suffix when the target filename exists, and `generate_previews.py:211-216` deletes the DB row but not the old file. Each `--force` run stacks a new orphan on top of the previous one. This is the Phase 2g2x.5 structural trap with one more concrete repro. For now, manually clean up post-regen and rename back to the canonical filename + update DB via shell. Permanent fix still deferred.
3. **"Anteprima Live" CTA is a legacy `href="#"` placeholder** for 17 of 20 templates (every template that isn't cardio / dermatologia / gusto). This is NOT a portfolio-scope bug — it's D-045's intentional gating meeting a legacy placeholder label. Do not fix in any per-category hardening session. Tracked as TODO_NEXT.md Phase **2g2x.7** with three remediation options.

## ⛔ ROADMAP STILL PAUSED — 3 of 5 CRITICO categories remain

**Per D-049 (Session 16), the roadmap is paused until Phase 2g2x closes.** Session 17 closed **business** (D-050). Session 18 closed **portfolio** (D-051) + Session 19 cleared its blocker (D-052). The remaining 3 identity-crash CRITICO categories are still open:
- `real-estate.html` hardcodes "600+ immobili · €500K–€1.2M mass-market" → Villa (ultra-luxury) shows mass-market language
- `lawyer.html` hardcodes "Studio legale dal 1962" → Juris (modern) shows Lex's 60-year heritage
- `agency.html` hardcodes 6 fake case-study names → both Vertex and Aura show the same clients

## ✅ Session 18 — Portfolio Closed (2026-04-11)

**Portfolio is no longer an identity-crash pair.** Chiara and Pixel are now split into two distinct DNA archetypes:
- `chiara-portfolio-creativo` → `editorial-designer-grid` archetype (cream paper `#f3efe5`, Syne + Inter, typographic hero with NO big photo, project index card with numbered ledger, 3-card case-study panel, clients ribbon + studio coordinates split footer, "Richiedi il portfolio completo" ghost sans-rule CTA, `portfolio-designer` imagery pool)
- `pixel-portfolio-fotografico` → `cinematic-photographer` archetype (near-black `#050505`, Archivo + Inter uppercase tracked, fullbleed dominant photo hero with corner frame marks and series-counter chip, monospaced EXIF credit bar pinned to hero bottom, 4-frame filmstrip gallery of series stills, 4-cell EXIF footer, `[ Apri la serie completa ]` ghost-bracket CTA, `portfolio-photographer` imagery pool)

Both skins were authored under the D-047 chrome-authoring contract from the first line — zero literal brand strings, zero hardcoded image URLs. The bidirectional leak sweep (52 tokens tested) returned zero cross-tenant contamination in both directions. The listing HTML leak sweep for all 9 legacy literals returned zero matches. Django test client returned 200 on all 5 portfolio routes. Visual regression at 1440×900 on `/templates/portfolio/` via Playwright MCP confirms the two cards read as two completely different products AND two completely different professions at card size — Chiara is unambiguously a designer studio (typographic grid, project ledger, clients ribbon with "CASA EDITRICE · FESTIVAL POESIA · FONDAZIONE · VINO D'AUTORE · MUSEO CIVICO · RIVISTA D'ARCHITETTURA") and Pixel is unambiguously a photographer ("FERMARE IL TEMPO, UNA LUCE ALLA VOLTA", EXIF bar with "Pellicola Medio formato 120 · Ottica Fisso 80mm · f/2.8 · Stampa Fine art · tiratura 12", filmstrip with 4 named series: "Le ore rubate / Campi lunghi / Stanze vuote / La città senza persone").

**Key insight reaffirmed for the next 3 categories:** The editorial-designer-grid archetype is **deliberately typographic (no big hero photo)**, so the Chiara card's readability does NOT depend on any single image URL. The hero IS the typography. This is the right pattern whenever the sibling's "visual opposite" has a weak image pool or you want to de-risk against image-download failures. The cinematic-photographer archetype is the opposite — the hero IS the photograph. Choose which side of this dichotomy each sibling lands on *before* authoring the composition.

**The Session 18 recipe (plus Session 17) is now a proven template for the remaining 3 CRITICO categories.** See SESSION_LOG.md Session 18 for the full Chiara-vs-Pixel differentiation matrix, bidirectional leak-sweep method, and the 52-token list for the sweep. See D-051 for the architectural decision rationale.

## ✅ Session 17 — Business Closed (2026-04-11)

**Business is no longer an identity-crash pair.** Pragma and Elevate are now split into two distinct DNA archetypes:
- `pragma-corporate-suite` → `corporate-suite` archetype (institutional navy + boardroom photo, Merriweather serif, advisory pillar cards + KPI strip, "Fissa una call privata" ghost CTA, `business-corporate` imagery pool)
- `elevate-startup-landing` → `startup-saas-landing` archetype (cosmic gradient, Manrope sans, typographic manifesto with NO big photo, glowing product-mockup card, "Inizia gratis" glow pill + "Guarda la demo" secondary, `business-startup` imagery pool)

Both skins were authored under the D-047 chrome-authoring contract from the first line — zero literal brand strings, zero hardcoded image URLs. The bidirectional leak sweep returned zero cross-tenant contamination in both directions. Django test client returned 200 on all 5 business routes. Visual regression at 1440×900 on `/templates/business/` confirms the two cards read as two completely different products at card size.

**The Session 17 recipe is the template for the remaining 4 CRITICO categories.** See SESSION_LOG.md Session 17 for the full differentiation matrix, leak-sweep method, and lessons-for-next-category list. See D-050 for the architectural decision rationale (Option A DNA split vs Option B lifted shared composition — Option A won and should stay the default).

**Additionally**, 4 single-tenant DNA archetype files have 10+ latent D-047 literal leaks each that will detonate on reuse:
- `ecommerce/fashion-editorial.html` — 12+ Luxe literals
- `ecommerce/artisan-workshop.html` — 10+ Bottega literals
- `restaurant/trattoria-warm.html` — "Trastevere · dal 1987"
- `restaurant/fine-dining/*.html` live skin — 5 files leak Gusto (Phase 2g.3 already planned)

**And**, 17 of 20 templates are single-page previews only. The marketplace positions as "complete multipage websites" but delivers landing-page posters for 85% of the catalog.

### What the next agent does first

1. Read `SESSION_LOG.md` Sessions 17 and 18 for the hardening recipe (portfolio is the most recent proven template; business is the first). Session 18 adds the "typographic-led vs image-led" dichotomy insight for choosing which sibling gets which side.
2. Read `DECISIONS.md` D-049 (blocking rule), D-050 (Option A DNA split default), and D-051 (portfolio validation of the default).
3. Read `TODO_NEXT.md` Phase 2g2x for the exact punch list (2g2x.1 through 2g2x.6). Business AND portfolio (2g2x.1) are marked `[x]`; the next 3 are open.
4. Pick **ONE** of the remaining 3 CRITICO categories and run the Session 17/18 recipe end-to-end:
   - **Recommended order:** real-estate (next cleanest "far apart" pair — Casa's mass-market vs Villa's ultra-luxury) → lawyer → agency (largest leak surface with 6 case-study wordmarks). This front-loads the cleanest wins while the recipe is fresh and back-loads the heaviest lift.
   - For each: add 2 archetype entries to `template_dna.py` (vocabulary + 2 DNA content blocks), add 2 imagery pools to `preview_imagery.py` (hand-verify URLs download), author 2 D-047-compliant compositions under `templates/preview_compositions/<category>/`, generate previews via `--only <slug>` (one at a time), run a bidirectional leak sweep, run a Django test-client 5-route sanity check, run a Chromium visual walk at 1440×900.
5. Do NOT start any feature work outside this wave. Not auth, not checkout, not editor, not new templates, not new categories. Do NOT touch any category other than the one you're currently closing in this session.
6. Each category close should end with: (a) bidirectional leak sweep clean, (b) `check` + `seed_templates` + `generate_previews` all green, (c) 5/5 routes return 200, (d) Chromium visual walk confirms differentiation at card size, (e) `SESSION_LOG.md` / `DECISIONS.md` / `TODO_NEXT.md` / `AGENT_HANDOFF.md` / `TEMPLATE_REGISTRY.json` / the auto-memory index all updated.

### Gotcha: Django test client + ALLOWED_HOSTS
Session 18 hit a small trap on the route sweep: `DEBUG=True` with `ALLOWED_HOSTS=[]` does NOT auto-allow `testserver` (only `localhost`/`127.0.0.1`/`::1`), and the Django test client uses `testserver` as the default Host header. If you run a test-client sweep via `manage.py shell`, monkey-patch it in-session:

```python
from django.conf import settings
settings.ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1']
```

Don't edit `settings.py` for this — it's a local-only concern and the monkey-patch is scoped to the shell session. For the Chromium visual walk, the runserver's real Host header is what matters, so `ALLOWED_HOSTS=[]` with `DEBUG=True` is fine at `127.0.0.1:<port>`.

### Minimum bar for "this wave is done" (exit criteria)

See TODO_NEXT.md Phase 2g2x.6. Summary: every sibling pair in every category must look like two different products at card size, no per-archetype file has any literal brand string, and every published template has either inner pages or is demoted to draft.

---

## Session 16 — Catalog Differentiation Hard Audit (2026-04-11)

**Question asked:** Are the catalog's sibling templates credible distinct products, or are they still recolors / identity-crash prototypes? Produce a severe, blocking-or-not verdict before the roadmap continues.

**Answer:** **Catalog not approvable.** See above. Verdict: hardening phase 2g2x is blocking. Read the new Phase 2g2x in TODO_NEXT.md and D-049 in DECISIONS.md. The audit found problems in 7 of 8 categories; only the `restaurant/street-modern` composition is fully clean. 5 categories are CRITICO severity (full identity crash), 3 categories are MEDIO severity (latent D-047 violations and cross-pool imagery leaks).

---

## Session 15 (archived) — Visual Polish & Preview Fixes (2026-04-11)

## Session 15 — Visual Polish & Preview Fixes (2026-04-11)

**Question asked:** A visual review of the current marketplace UI found four concrete product-quality problems visible directly on cards and category pages. Fix them without expanding scope: (1) Dermatologia card shows a grey placeholder, (2) restaurant category hero is clipped/unbalanced, (3) Gusto+Sapore still too similar at card size, (4) Luxe+Bottega essentially identical at card size.

**Answer:** **All four fixed, verified visually and via 37-route regression.**

### Root causes
1. **Dermatologia had zero preview TemplateAssets.** Session 13 explicitly skipped preview regeneration when validating archetype reuse ("validation is about the live preview, not the thumbnail"). The marketplace card rendered its `mw-img-placeholder` fallback — a grey `bi-window-desktop` icon.
2. **Hidden second leak in `templates/preview_compositions/medical/specialist.html`.** Session 14 covered the `live_templates/medical/specialist/*.html` chrome but missed the preview composition. It still hardcoded `Dr. R. Marani`, `Roma · Parioli`, `SC Cardiologia` in the hero meta + credit blocks. Regenerating derm's preview naively would have shown the cardiologist's name on the dermatology card.
3. **Restaurant category hero too cramped.** `.mw-page-hero` used `padding-top: 7rem` against a 77px fixed navbar — only a 35px gap navbar→breadcrumb. `max-width: 36rem` on the subhead left the right side dead on wide screens. No `min-height` → hero collapsed to ~330px.
4. **Gusto + Sapore PNGs on disk were stale** — legacy `restaurant.html` renders from before Session 10's fix pass. Session 12 claimed to have regenerated them but the fix did not land in this worktree.
5. **Luxe + Bottega had no DNA at all.** Both rendered through the single legacy `ecommerce.html` composition that hardcodes every string and pulls from the same pool. The only difference was the brand name in the navbar.

### Fixes applied
1. **Dermatologia preview.** Moved `Dr. R. Marani / Roma · Parioli / SC Cardiologia` out of `specialist.html` literals into new DNA fields `hero_meta`, `credit_left`, `credit_right` on both Cardio and Dermatologia content blocks. The composition now does `{% for label, value in dna.content.hero_meta %}` and reads `dna.content.credit_left.0/1`. Ran `generate_previews --only dermatologia-elite-roma` — the card now shows "Dr.ssa L. Ricciardi · 18 anni · 2.400+ pazienti · Studio Roma · Via Veneto · Specialità Dermatologia" with the forest-green accent + Bodoni Moda pairing. Regenerated Cardio too to verify the composition change is a no-op for it (confirmed).
2. **Restaurant hero.** Rewrote `.mw-page-hero` in `static/css/components.css`: `padding-top: calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` (64px clearance), `padding-bottom: var(--mw-space-10)` (80px), `min-height: 22rem`, vertical-centered flex, subhead `max-width: 46rem`, clamped responsive h1, dual radial gradient background (indigo top-right + amber bottom-left), `overflow: hidden`, `position: relative` + container z-index. Measured after: 64px navbar→breadcrumb gap, 373px hero height.
3. **Gusto / Sapore.** Clean-delete recipe (remove asset row + canonical file + any orphan suffix, re-run `generate_previews --only <slug>` without `--force`). The Session 10 DNA compositions for `restaurant/fine-dining.html` and `restaurant/trattoria-warm.html` render correctly — they just needed a fresh pass. Gusto = fully DARK charcoal + italic Playfair + full-bleed plate + gold course index. Sapore = fully CREAM + handwritten Caveat + polaroid scrapbook + recipe card. With Brace (yellow brutalist) unchanged, the 3 restaurant cards now occupy three opposite ends of the visual spectrum.
4. **Luxe / Bottega (new ecommerce DNA pilot).** Added 2 archetypes to `LAYOUT_ARCHETYPES`: `fashion-editorial`, `artisan-workshop`. DNA entries for both (using existing `ecommerce` imagery pool — Session 10's lesson: controlling macro tone is cheaper than URL hunting). Authored two new compositions under `templates/preview_compositions/ecommerce/`:
   - **fashion-editorial.html** (Luxe) — fully DARK #08070a, gold #B8860B accents, italic Cormorant Garamond 108px "Il nuovo corpo del vestire", fashion-model full-bleed cover L, editorial product strip with gold price labels at bottom.
   - **artisan-workshop.html** (Bottega) — fully CREAM #f6ecd8 with subtle grain, terracotta accent, huge Libre Baskerville 108px "Pezzi unici cuciti & fatti in bottega", rubber-stamped info panel rotated 0.8deg, 4-up N°-labeled edition cards. NO hero photo — typographic-led.
   
   Both compositions use the SAME imagery pool. The visual differentiation comes from macro tone (BLACK vs CREAM), font family (italic serif vs rustic serif), layout structure (photo-led vs typographic-led), and accent color. At thumbnail size, they read as two completely different products.

5. **Orphan file cleanup.** Session 12 left 4 orphan-suffixed files with DB rows pointing to them. Renamed each orphan to its canonical name and updated the DB. Zero orphan files now exist.

### Hard validation
- **`python manage.py check` — clean.**
- **37-route regression sweep via Django test client:** homepage + 5 category pages + 10 detail pages + 7 cardio inner + 7 derm inner + 6 gusto inner + 1 gusto post. **All 37 return 200.**
- **Cardio-leak audit** re-run on all 7 dermatology pages after the preview-composition change: **zero leaks.** Session 14's abstraction still holds.
- **Visual verification via Chromium (Playwright):** homepage featured grid shows new Gusto, `/templates/restaurant/` shows 3 distinct cards + balanced hero, `/templates/medical/` shows 5 medical cards all with valid previews (derm no longer a placeholder), `/templates/ecommerce/` shows Luxe (dark fashion) and Bottega (cream artisan) as instantly distinguishable products.

### What to do next

**Highest leverage: Phase 2f.2 — Ecommerce DNA expansion.** Two ecommerce archetypes now exist (`fashion-editorial`, `artisan-workshop`) but each hosts exactly one template. Validate reuse the same way the `specialist` archetype was validated in Session 13: add a second template under each archetype with ONLY a seed row + DNA entry, zero new HTML files. Then run a leak audit on the rendered preview to find any literal `Maison Luxe`, `Firenze`, `Santa Croce`, `Giulia Maison`, `Milano · Parigi · Tokyo`, etc. that snuck into the composition authoring pass. Lift them into DNA content fields per the D-047 chrome-authoring contract. The reward is that the two new ecommerce archetypes become fully reusable and the next ecommerce template ships without any copy polish.

**Second priority: Phase 2g.3 — Fine-Dining copy-abstraction lift** on `templates/live_templates/restaurant/fine-dining/` (documented in TODO_NEXT.md). This was already the highest-priority item before Session 15 and is still pending.

### Lessons from Session 15 (read these before the next pilot)

1. **"Validation skipped the thumbnail" is a user-facing bug.** Session 13's reasoning was that archetype reuse is about the live preview, not the marketplace card. But the marketplace card is the FIRST thing a buyer sees. Any future archetype-reuse validation must end with `generate_previews --only <slug>` and a visual check of the card in the listing. Skipping the thumbnail is not "smaller scope" — it leaves a broken product visible to users.

2. **D-047 applies to preview compositions too, not just live-template chrome.** Session 14 lifted `templates/live_templates/medical/specialist/*.html` and celebrated zero leaks. But `templates/preview_compositions/medical/specialist.html` still had 3 cardio literals that would have surfaced on any non-cardio template sharing that archetype. The rule generalizes: **every string in any per-archetype file (live-template chrome OR preview composition) must be a CSS rule, a generic archetype label, a DNA content field, or a loop item.** Apply it to both kinds of files every time.

3. **Macro tone trumps imagery, confirmed at a third pilot.** Luxe and Bottega share the exact same imagery pool yet read as two completely different products at card size because one composition is fully BLACK and the other is fully CREAM. Session 10 established this for Restaurant; Session 15 confirmed it for Ecommerce. **Before hunting for new Unsplash URLs on the next DNA pilot, first decide whether the compositions can carry the difference on macro tone alone.** If they can, it's free. URL hunting is expensive (HTTP 404s, hand-verification, Session 9 mistakes).

4. **Stale-PNG timing trap is still unfixed structurally.** Sessions 8, 10, 12, 15 all hit it independently. The clean-delete recipe works but is operator-dependent. The proper fix from TODO_NEXT Phase 2d — either auto `--force` when DNA mtime > asset mtime, or hash the DNA into a `dna_signature` field on TemplateAsset and compare on every run — is the next DX polish priority. Until then, any DNA edit on an existing slug requires the clean-delete recipe.

5. **`position: fixed` navbar + `padding-top: Xrem` on hero is a hidden coupling.** The previous 7rem worked with a 64px navbar but became cramped once the navbar grew to 77px. Encoded it as `calc(var(--mw-navbar-height, 77px) + var(--mw-space-10))` so the coupling is explicit. Long-term: measure the navbar height via JS on page load and expose as a CSS custom property so the hero always clears it.

---

## Session 14 — Specialist Copy-Abstraction Lift (2026-04-11)

**Question asked:** Can the specialist chrome HTML files be made truly reusable — so a third specialist template (after Cardio and Dermatologia) ships with zero copy polish — by moving every hardcoded cardio literal out of HTML into the content registry, WITHOUT adding any new HTML files?

**Answer:** **Yes.** Phase 2g.2 is closed. All 17 leak points identified in Session 13's audit are resolved via purely mechanical moves. The specialist archetype is now editorially reusable.

### What changed
Eleven files modified, zero added, zero deleted:
- `apps/catalog/template_content.py` — CARDIO_CONTENT + DERMATOLOGIA_CONTENT gained ~30 new fields each, grouped semantically under existing blocks (`site.license`, `site.hours_footer_rows`, `home.hero_sidebar_*`, `home.chief.portrait`, `home.signature_visits_*`, `home.chief_label`/`heading`, `home.press_label`, `home.cta_*`, `studio.values_*`, `studio.cta_*`, `visite.footnote_heading`, `visite.cta_*`, `medici.portrait_city`, per-doctor `doctors[i].portrait`, `pubblicazioni.lead_image`, `pubblicazioni.footer_strap`, `pubblicazioni.empty_body_fallback_paragraphs`, `contatti.form_placeholders`, `contatti.hours_heading`, `contatti.transport_heading`, `richiedi-visita.process_label`/`heading`, `richiedi-visita.form_band_side_note`/`_small`, `richiedi-visita.submit_label`). The `richiedi-visita.form_fields` list was **reshaped** from `(label, placeholder, type)` tuples into richer dicts `{label, type, full_width, placeholder OR options}` so the appointment form's two selects can loop their options from data instead of being hand-written.
- `apps/catalog/views.py` — `LiveTemplateView.get_context_data()` now computes `blog_parent_slug` from the content registry's `pages` list (first entry where `kind == 'blog_list'`). Template blog URL reverses consume this variable instead of hardcoding `'pubblicazioni'`. **D-044's hardcoded-blog-slug constraint is lifted** — see D-048.
- Nine HTML files under `templates/live_templates/medical/specialist/` — every cardio literal swapped for `{{ page_data.* }}`, `{{ site.* }}`, loop iteration, or `blog_parent_slug`. The `team.html` `nth-child` portrait CSS rules are gone, replaced with per-doctor inline styles (which also removes the 3-doctor cap). The `appointment.html` hand-written form is gone, replaced with a single generic field loop.

### Hard validation
1. **`python manage.py check` — clean.**
2. **Route sweep — 25/25 green** via Django test client:
   - Cardio: 9 routes (marketplace detail + 7 inner preview pages + 1 post detail)
   - Dermatologia: 9 routes (same structure)
   - Gusto regression: 7 routes (marketplace detail + 6 inner pages + 1 post detail)
3. **Cardio-leak sweep on dermatologia — ZERO leaks.** Rendered HTML of all 8 dermatologia pages was grepped for 26 cardio literals (`Marani`, `OMCeO Roma 12 / 4408`, `cardiologia`, `Cardiologia`, `Parioli`, `catena di montaggio`, `Lancet`, `Riccardo Marani`, `Salieri`, `Lombardi`, `Prima visita`, `Secondo parere`, `Programma prevenzione`, `Visita di controllo`, `ecocardiograf`, `Holter`, `ECG`, `Policlinico Umberto`, `Braunwald`, `Institut de Cardiologie`, etc.). **All 8 pages came back clean.**
4. **Positive content sweep — Cardio 52/52, Dermatologia 46/46** expected strings all present. The content blocks still drive every field the chrome reads.
5. **Template file grep — zero hardcoded Unsplash URLs, zero cardio-brand literals** in any of the 9 specialist chrome files.

### The chrome-authoring contract (D-047)

Every string in a per-archetype skin must satisfy exactly one of four criteria:
1. **CSS rule** (color, font, layout — the visual identity)
2. **Generic archetype label** — applies identically to every template that could use this archetype (`Nome`, `Email`, `Privacy`, `Invia messaggio`, `Leggi l'articolo completo`, `© 2026`, etc.)
3. **Template context variable** (`{{ site.* }}`, `{{ page_data.* }}`, `{{ d.* }}`, `{{ post.* }}`, `{{ blog_parent_slug }}`)
4. **Loop iteration** over a content registry list

**Never:** literal brand name, literal city name, literal quote, literal CTA heading, literal form select option, hardcoded image URL.

This contract is now a chrome-authoring precondition for Phase 2f (Agency, Lawyer, Real Estate archetype splits) and Phase 2g.3 (fine-dining copy-abstraction lift). Applied from the first authoring pass of any new skin, it eliminates the need for a follow-up lift pass entirely.

### What to do next
**Phase 2g.3 — repeat this exact lift on `templates/live_templates/restaurant/fine-dining/`.** The fine-dining chrome was authored during Session 11 in the same style as the specialist chrome and almost certainly has the same class of leaks (Lorenzo Fioravanti brand-name references, Brera district in the chef portrait, hardcoded Michelin press list labels, hardcoded `'diario'` URL reverses in blog files, hardcoded Unsplash URLs for chef/plate/room photos). The recipe is documented in TODO_NEXT.md Phase 2g.3:
1. Add a second fine-dining template (suggested: `tartufo-truffle-house` — Piedmont truffle restaurant, autumn menu, different chef/brand) with ONLY a seed row + DNA entry + content block.
2. Run the leak sweep against it: grep rendered HTML for `Fioravanti`, `Osteria Moderna`, `Brera`, `Tarbouriech`, `Vallesi`, `Otto atti`, `Barolo Cannubi`, etc.
3. For each leak, add a structured field in the appropriate block and update both Gusto and the new template's content.
4. Replace any hardcoded `'diario'` URL reverses with `blog_parent_slug` (already computed in the view).
5. Replace any hardcoded image URLs with inline `style="background-image: url('{{ ... }}')"` reading from per-item fields.
6. Re-run a full regression sweep (Cardio 9 + Derm 9 + Gusto 7 + new template 7 = 32 routes).

After Phase 2g.3 closes, both archetypes in use are proven reusable and the pattern is general. Then resume Phase 2f DNA rollout (Agency, Lawyer, Real Estate) applying D-047 from the first authoring pass of every new skin.

## Session 13 — Archetype Reuse Validation (2026-04-10)

**Question asked:** Can a new full multi-page template be added under an existing archetype (the Medical `specialist` archetype, previously single-tenant by Cardio) with ONLY three edits — one seed row, one DNA entry, one content block — and **zero** new HTML files? This was the Option A validation path proposed at the end of Session 12.

**Answer:** **Yes, structurally.** `dermatologia-elite-roma` (Studio Ricciardi Dermatologia · Via Veneto 116 · forest green accent `#3d5437` · Bodoni Moda + Inter · three dermatologhe · six treatments · five publications) now ships as a full navigable 7-inner-page website on the same specialist chrome as Cardio. All 9 routes (marketplace detail + home + 6 inner pages + 1 post detail) return 200 via Django test client. `git status` confirms three modified `.py` files (`seed_templates.py`, `template_dna.py`, `template_content.py`) and zero modified or new HTML files. 19-URL regression sweep on Cardio + Gusto + catalog pages all 200. **The Session 11 architecture works as intended for content-driven reuse.**

**BUT editorially the chrome leaks.** The same audit that confirmed the 200 statuses also found that cardio-specific copy is baked into the HTML in 17 distinct sites across 7 files, appearing on every single dermatology page. The most visible leaks: (1) `OMCeO Roma 12 / 4408` on every page's footer (wrong license number for the derm studio), (2) `«La cardiologia non è una catena di montaggio...»` quote in the home hero's right column, (3) `Roma · Parioli` in the home pulse band and in every doctor's portrait signature, (4) `Studio Marani` brand name in the services CTA heading and the blog detail footer, (5) three hardcoded Unsplash portrait URLs in `team.html`'s nth-child CSS rules (Dermatologia's team shows Cardio's doctors' photos, and the 3-doctor cap is baked into the layout). See SESSION_LOG.md Session 13 for the full 17-row leak table.

**Why this is not a blocker for the validation verdict but IS a blocker for the next reuse template:** The architecture separates "chrome + data" correctly; the implementation simply baked sample copy into the chrome during the Session 11 authoring pass. Fixing it is a mechanical lift — move the literals out of `.html` files into new `site.*` / `page_data.*` / per-item fields in the content registry. No new HTML files, no new architecture. **See TODO_NEXT.md Phase 2g.2 for the exhaustive lift plan.**

### What changed in Session 13
**New template: `dermatologia-elite-roma`** — 2nd template on the `specialist` archetype
- `seed_templates.py` — new row, order=5, price €115, brand "Studio Ricciardi Dermatologia" with palette `{primary:#1c1612, secondary:#f7f3ee, accent:#3d5437}` and typography `Bodoni Moda + Inter`
- `template_dna.py` — new DNA entry keyed `dermatologia-elite-roma`, archetype `specialist`, all the specialist defaults, font_pairing overridden to `("Bodoni Moda", "Inter")`, fresh `content` block for the preview composition
- `template_content.py` — new `DERMATOLOGIA_CONTENT` dict with all 7 pages, 5 posts (first with full body), site chrome data, dermatology-specific copy throughout. Page slugs kept as `home / studio / visite / medici / pubblicazioni / contatti / richiedi-visita` to match the hardcoded `pubblicazioni` URL reverse in the blog files
- `TEMPLATE_REGISTRY.json` — version 0.6.0, dermatologia entry added with `archetype_reuse: true` flag
- `CATEGORY_ROADMAP.md` — specialist archetype now hosts 2 templates; reuse validation result logged
- `DECISIONS.md` — D-046 added (formal record of the validation result + the copy-leak finding + the Phase 2g.2 plan)

### Database delta
- `+1` WebTemplate row, `+1` TemplateBrand row, 0 new TemplateAssets (no PNG regenerated — validation is about the live preview, not the thumbnail)
- Medical category is now 5 templates (clinic, family, specialist ×2, wellness)
- Total marketplace: 20 templates / 20 brands / 19 preview assets

### The hard constraints discovered (critical for any future reuse)
1. **The blog parent page slug must be literally `pubblicazioni`.** `blog_list.html:95,98,109` and `blog_detail.html:85,121` hardcode `{% url 'catalog:live_template_page' ... 'pubblicazioni' %}` in URL reverses. Any other naming causes `NoReverseMatch`. Dermatologia's blog page is therefore called Pubblicazioni, not "Blog" or "Diario". **Phase 2g.2 fix:** compute `blog_parent_slug` in `LiveTemplateView.get_context_data()` from the content registry's `pages` list.
2. **The chrome caps the team at 3 doctors.** `team.html:70-72` uses `nth-child(1/2/3) .portrait { background-image: ... }`. A fourth doctor would render without a portrait. **Phase 2g.2 fix:** move to per-doctor `doctors[i].portrait` URLs.
3. **The chief doctor portrait image is shared** — `home.html:127` hardcodes a single Unsplash URL in inline CSS. Dermatologia's chief shows the same photo as Cardio's chief. **Phase 2g.2 fix:** move to `home.chief.portrait`.
4. **The blog-list lead post image is shared** — `blog_list.html:17` hardcodes another Unsplash URL. **Phase 2g.2 fix:** move to `pubblicazioni.lead_image` or `posts[0].hero_image`.
5. **The appointment page `<select>` options are hardcoded** — `appointment.html:166-180` bakes in the cardio visit types (Prima visita / Secondo parere / Programma prevenzione / Visita di controllo) instead of reading from `richiedi-visita.form_fields` which already exists in both content blocks. **Phase 2g.2 fix:** template loop over `form_fields`.
6. **Seven distinct section headings / CTA labels are literal cardio copy.** See the TODO_NEXT.md Phase 2g.2 checklist for the complete per-file enumeration.

## Session 12 — Template Polish Fixes (2026-04-10)

Two product-quality issues closed before the next pilot:

1. **Over-narrow inner-page layouts.** The live multi-page template skins used max-width 1100/1200/1280 which felt "compressed into the middle" of 1600-1920px displays. Bumped to a two-tier standard: **1400px** for medical/specialist wide sections, **1440px** for restaurant/fine-dining wide sections. The home manifesto had an additional double-constraint bug (`outer 1100px` + `inner p max-width: 36ch; margin: 0 auto`) producing a tiny ~450px centered column — fixed by removing the inner centering and widening to `68ch` left-aligned so the drop-cap anchors the frame's left edge. Blog detail pages stay at 760px intentionally (long-form reading column).

2. **Restaurant listing preview mismatch.** Two layers:
   - **Outer layer:** `template.assets.first` in the card + detail partials is fragile — default-ordering fetch, not filtered by asset_type. Replaced with a new `WebTemplate.preview_asset` property in `apps/catalog/models.py` that explicitly filters `asset_type == preview`, is prefetch-aware (iterates `_prefetched_objects_cache` when available), and returns `None` when no preview exists. Selector uses `Prefetch('assets', queryset=...filter(asset_type='preview'))` to ship a smaller payload.
   - **Inner layer (actual cause):** The gusto + sapore PNG files on disk were stale legacy `restaurant.html` renders — both showed the same wood-interior trattoria. Session 10's claimed regeneration never actually landed in this worktree. Fixed by deleting the stale asset rows + files and re-running `generate_previews --only <slug>` (no `--force`, so the canonical filename lands clean without an orphan suffix).

**Branch:** `template-polish-fixes` worktree (built on top of `template-completeness-pilot` → ... → `template-dna-system`, **none merged to master yet**).

**All three restaurant cards now read as three distinct products at thumbnail size** — Brace (yellow brutalist), Sapore (bright cream polaroid), Gusto (dark editorial Playfair). 20 routes verified 200 via Django test client, `python manage.py check` passes.

### Lessons from Session 12

- **`template.assets.first` is a bug magnet.** It returns "whatever's first by default `(order, asset_type)` ordering", which silently picks the wrong file the moment a template gains a second asset. Always filter by `asset_type` explicitly. The `WebTemplate.preview_asset` property encapsulates this rule once so templates never need to remember it.
- **Page-level max-widths of 1100-1280 are too narrow for 1600+ displays.** 1400-1440 is the new standard for wide content. Editorial narrow reading columns (blog articles) stay at ~720-800 because those are about line length, not frame width. **Never double-constrain** with outer `max-width` + inner `margin: 0 auto + max-width: Xch` on the same element tree — either widen the outer container and use `max-width: <NN>ch` on the text (left-aligned, drop-cap anchored to the frame's left edge), or keep the outer narrow and drop the inner centering. The double constraint creates compositions that look "floating in a void".
- **DNA-fallback timing trap is still live.** Gusto and Sapore's PNGs were stale despite Session 10's claim. Whatever the root cause (cross-branch drift, unrecorded regen, worktree sync), the fix recipe is the same every time: delete the asset row + canonical file first, then re-run `generate_previews --only <slug>` without `--force`. TODO_NEXT.md Phase 2d item 4 — "auto --force whenever the DNA file or composition path on disk is newer than the preview's TemplateAsset" — would catch this class of bug structurally. Strong candidate for the next DX polish pass.

## Current State (since Session 11, carried through 12)

**Two pilot templates now ship as full multi-page websites — not just preview screenshots.** The DNA system (Sessions 7-10) made each template's homepage visually unique. Session 11 added the missing piece: every template can now be a *navigable, complete website product*. Session 12 then polished the inner-page layout widths and hardened the preview-asset selection against the fragile `template.assets.first` fallback.

- **`cardio-studio-specialistico`** (Medical · specialist archetype): 8 navigable inner pages — Home, Lo Studio, Visite, Medici, Pubblicazioni (list + article detail), Contatti, Richiedi visita
- **`gusto-fine-dining`** (Restaurant · fine-dining archetype): 7 navigable inner pages — Casa, Filosofia, Menu (otto atti), Atmosfera, Diario (list + article detail), Prenota
- All 17 routes (8 + 7 + 2 marketplace detail) verified 200 via Django test client (Session 11), extended to 20 in Session 12
- The system is **strictly opt-in per template** — every other template in the catalog behaves exactly as before
- **New in Session 12:** `WebTemplate.preview_asset` property, selector uses `Prefetch` with filtered queryset, layout widths bumped to 1400/1440, home manifesto double-constraint fixed, stale gusto/sapore PNGs regenerated. Three restaurant cards now read as three distinct products at thumbnail size.

The marketplace template detail page now shows "Apri anteprima completa" (linking to the full live site) when content is registered, and falls back to the old "Anteprima Live" placeholder otherwise.

Branch: `template-polish-fixes` worktree (built on top of `template-completeness-pilot` → ... → `template-dna-system`, **none merged to master yet**).

## Session 11 — Template Completeness Pilot Phase

Three architectural layers introduced:

1. **Content registry** — `apps/catalog/template_content.py`. Python dict keyed by `WebTemplate.slug` holding the page list, per-page content blocks (eyebrow, headline, sections, lists), and a `posts` list for blog/news inner pages. All Italian, all realistic, no boilerplate.

2. **Per-archetype standalone skin** — `templates/live_templates/<category>/<archetype>/`. Each archetype gets its own `_base.html` that is a *complete HTML document* (NOT extending the marketplace `base.html`), loading the DNA's font pairing and brand palette. Each page kind (`home.html`, `about.html`, `services.html`, `team.html`, `blog_list.html`, `blog_detail.html`, `contact.html`, `appointment.html`, `menu.html`, `gallery.html`, `reservations.html`) extends that base and overrides `extra_css` + `content`.

3. **Single dispatcher view** — `LiveTemplateView` in `apps/catalog/views.py`. Resolves WebTemplate → DNA → content registry in `setup()` (NOT `get_template_names`, see D-044 trap), computes the template path `live_templates/<category>/<archetype>/<page-kind>.html`, returns 404 if either DNA or content is missing.

Three new URL patterns:
```
/templates/<cat>/<slug>/preview/                         → live_template_home
/templates/<cat>/<slug>/preview/<page>/                  → live_template_page
/templates/<cat>/<slug>/preview/<page>/<post_slug>/      → live_template_post
```

### What makes a template "complete" now

A template earns the "Apri anteprima completa" CTA on its detail page once it has BOTH:
1. A DNA entry in `apps/catalog/template_dna.py` (archetype + chrome decisions)
2. A content registry entry in `apps/catalog/template_content.py` (the editorial copy for every page)

Without either, it falls back to the legacy `Anteprima Live` placeholder and the new URL space returns 404. Every template that's been in the catalog before Session 11 still works exactly as it did.

### What is now reusable across all future templates
- `LiveTemplateView` and the three URL patterns
- The content-registry pattern (`template_content.py`) — adding a new template = adding ONE new top-level dict
- The per-archetype skin folder structure — any new template that picks an existing archetype gets the chrome FOR FREE, just needs content
- Brand palette → CSS variable injection
- Nav loop with `is-current` highlight
- Footer pattern with site-data block

### What still needs per-archetype work
- Each NEW archetype needs its own `_base.html` (intentionally bespoke — that's the point of DNA)
- Each NEW archetype's page kinds need their own page templates (a `menu.html` is meaningless for a medical template)

## Old: Session 10 — Restaurant Pilot Fix Pass

Visual review of Session 9 found that **only Brace was clearly distinct**. Gusto and Sapore had two overlapping problems:

1. **Imagery overlap**: `restaurant-fine` and `restaurant-trattoria` pools shared 5 of 6 URLs (only the hero differed). Session 9's claim of "fully-distinct URL sets" was wrong — only Brace's pool was actually distinct.
2. **Same macro silhouette**: both compositions were "cream paper top + dark band bottom". At thumbnail size the dark/cream split dominated and made them read as the same skeleton.

### Fix applied
- **Imagery pools**: both `restaurant-fine` and `restaurant-trattoria` rebuilt with 6 hand-checked URLs each, **zero overlap**. Fine got 6 dark plated dish photos. Trattoria got 6 bright sunny rustic photos. Each candidate was downloaded and visually inspected via the Read tool before committing — caught one clothing-store image and replaced it.
- **`restaurant/fine-dining.html` rewritten**: pivoted from cream-paper to **fully dark charcoal page** (no cream anywhere, no contrast band, full-bleed plate close-up hero, italic Playfair throughout, course list on the same dark background separated only by hairline gold rules).
- **`restaurant/trattoria-warm.html` rewritten**: pivoted from cream-with-dark-chalkboard to **fully bright cream page** (no dark areas at all, two stacked tilted polaroid scrapbook photos with washi tape, huge Caveat handwritten headline, cream washi-tape recipe card replacing the dark chalkboard, no dark hours band).
- **Brace left untouched** — already strongly distinct (yellow brutalist).

Result: 3 cards now occupy three opposite ends of the visual spectrum — dark editorial / bright handwritten / yellow brutalist.

## Session 9 — Restaurant Pilot Phase 2f.1 (superseded by Session 10 fix for Gusto/Sapore)

Replicated the medical DNA pilot for the Restaurant category. Three brand-new HTML compositions, three distinct imagery pools, one new seed template. Visually validated — but the Session 9 imagery pool was wrong (5/6 URL overlap between fine and trattoria) and the compositions had structurally similar bottom dark bands. Both fixed in Session 10.

| Layer            | Before                                          | After                                                                       |
|------------------|-------------------------------------------------|-----------------------------------------------------------------------------|
| Restaurant templates | 2 (Gusto, Sapore)                           | 3 (added Brace — Street Food Lab)                                           |
| Restaurant archetypes | 1 (legacy fallback only)                   | 3 (fine-dining, trattoria-warm, street-modern)                              |
| Restaurant compositions | 1 (legacy `restaurant.html`)             | 4 (legacy + 3 new under `restaurant/<archetype>.html`)                      |
| Restaurant imagery pools | 1 (`restaurant`)                         | 4 (`restaurant`, `restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) |
| Total templates  | 18                                              | 19                                                                          |

The DNA system is still **strictly additive** — templates without a DNA entry continue to render via the legacy per-category composition. The legacy `templates/preview_compositions/restaurant.html` is retained as a safety net for any future restaurant template not yet pulled into an archetype.

## What makes the 3 restaurant templates genuinely different (not recolors) — post Session 10

| Slug                       | Archetype       | Page macro tone   | Hero composition                                    | Navbar         | Card mood                  | Display Font           |
|----------------------------|-----------------|-------------------|-----------------------------------------------------|----------------|----------------------------|------------------------|
| gusto-fine-dining          | fine-dining     | **fully DARK** charcoal #0b0907 | full-bleed plated dish R · italic serif text L  | serif-centered (dark + gold rule) | course-index on same dark bg, gold dotted leaders | Playfair Display       |
| sapore-trattoria-pizzeria  | trattoria-warm  | **fully BRIGHT** cream #fff4da | two tilted polaroids L · handwritten Caveat R   | warm-bar (cream + phone CTA) | cream-paper recipe card with washi tape | Caveat (handwritten)   |
| brace-street-food-lab      | street-modern   | **bright YELLOW** #FFE600 | giant condensed display L · tilted burger product R | bold-pill (black floating) | brutalist black product grid w/ corner badges | Big Shoulders Display  |

**The macro tone column is the critical one** — this is the lesson from Session 10's fix pass. At thumbnail scale, page-level color regions dominate over hero details. Two templates with the same "cream top, dark bottom" silhouette will read as similar regardless of what's in each section. The fix is to make the WHOLE PAGE one consistent macro tone (dark / cream / yellow) so the entire silhouette is different from card to card.

Differences also span hero composition (full-bleed plate L vs polaroid scrapbook L vs tilted product cutout R), navbar shape (centered serif wordmark with gold rule vs cream warm-bar with phone CTA vs floating black pill), card stride (5-row dotted-leader course index on dark vs 5-day cream washi-tape recipe card vs 4-up brutalist product grid), button language (gold-underlined serif ghost vs rustic rounded with red+green tilted shadow vs brutalist block-bold with hard offset shadow), density (very-airy → medium → compact), and copy tone (editorial chef → familiar warm → energetic bold).

## What's Working

| Page                          | URL                                        | Status (port 8101) |
|-------------------------------|--------------------------------------------|--------------------|
| Homepage featured grid        | `/`                                        | Salute (clinic), Pragma, Vertex, Lex, Chiara, Gusto in featured grid |
| Template listing (all)        | `/templates/`                              | 19 templates × paginated |
| Template listing (medical)    | `/templates/medical/`                      | 4 medical templates × 4 visibly different archetypes (regression OK) |
| Template listing (restaurant) | `/templates/restaurant/`                   | 3 restaurant templates × 3 visibly different archetypes |
| Template detail (each restaurant) | `/templates/restaurant/<slug>/`        | Gallery shows the new archetype PNG |
| Template detail (each medical)| `/templates/medical/<slug>/`               | Gallery shows the new archetype PNG |

## How the DNA system works

```
apps/catalog/template_dna.py
  ├── Vocabulary dicts: LAYOUT_ARCHETYPES, HERO_STYLES, NAVBAR_STYLES,
  │                     FOOTER_STYLES, CARD_STYLES, BUTTON_STYLES,
  │                     DENSITY_PROFILES, TONES, CONVERSION_PATTERNS,
  │                     IMAGERY_DIRECTIONS
  ├── TEMPLATE_DNA: dict[slug, dna]  # the registry (7 entries: 4 medical + 3 restaurant)
  └── get_dna(slug), has_dna(slug)

apps/catalog/templatetags/preview_extras.py
  └── `at` filter — `{{ imagery|at:forloop.counter }}` for safe loop indexing

apps/catalog/preview_imagery.py
  └── Per-archetype keys:
      • medical-family / medical-specialist / medical-wellness  (recycle existing URLs, offline-safe)
      • restaurant-fine / restaurant-trattoria / restaurant-street  (fully-distinct URL sets)

apps/catalog/management/commands/generate_previews.py
  ├── _resolve_composition(template, dna)
  │     → with DNA: preview_compositions/<category>/<archetype>.html
  │     → without:  preview_compositions/<category>.html
  ├── Pre-warms imagery by *imagery_key*, not just category slug
  └── DNA's `font_pairing` overrides brand.typography parsing

templates/preview_compositions/medical/
  ├── clinic.html      — institutional, split-hero with booking widget, 4-up icons
  ├── family.html      — pastel pill nav, organic-shape portrait, intro trio + hours strip
  ├── specialist.html  — minimal serif nav, editorial headline, drop cap, 01/02 fields, press band
  └── wellness.html    — full-bleed hero, glass pill nav, dotted-leader pricelist, therapists strip

templates/preview_compositions/restaurant/
  ├── fine-dining.html    — centered serif wordmark, editorial split-plate, course index, concierge tile, press strip
  ├── trattoria-warm.html — cream warm-bar nav, polaroid photo card, Caveat handwritten manifesto, chalkboard daily specials, family + hours band
  └── street-modern.html  — black floating pill nav, giant condensed display + tilted product cutout + price badge, 4-up product grid, delivery strip
```

Run with `python manage.py generate_previews [--force] [--only <slug>]`.

## Database State

- 8 categories (unchanged)
- **19** templates (was 18; +1 restaurant: brace-street-food-lab)
- 19 brands
- 19 preview assets — 4 medical + 3 restaurant now use the new per-archetype compositions
- ~70 cached source photos across 11 pools (3 new restaurant pools added in Session 9)

## For Next Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, TODO_NEXT.md, this file, then `apps/catalog/template_dna.py` + `apps/catalog/template_content.py` (the two registries the reuse validation depended on), then `apps/catalog/views.py` → `LiveTemplateView` (the dispatcher view), then open any file under `templates/live_templates/medical/specialist/` to see the chrome that now hosts two templates (Cardio + Dermatologia).

**The highest-impact next task is Phase 2g.2 — the copy-abstraction lift** on the specialist chrome, documented exhaustively in TODO_NEXT.md. It's a mechanical move-literals-out-of-HTML-into-content-registry pass — no new HTML files, no new architecture, just pulling hardcoded cardio strings out of 7 files and wiring them to new `site.*` / `page_data.*` / per-item fields. When done, re-running the Session 13 leak audit on the dermatologia pages should show zero cardio-specific strings, and the next archetype-reuse template (e.g. a third specialist, or the first fine-dining reuse) will ship without any copy polish.

### Lessons from Session 10 — read these before designing any new category

1. **Imagery pool distinctness is non-negotiable.** Two pools that share even 5 of 6 URLs will produce sibling templates that look identical, regardless of how different the compositions are. When designing a new category's pools, write down the URL list and visually verify zero overlap. Hand-check every Unsplash candidate by downloading via curl and reading the file with the Read tool — HTTP 200 just means the photo exists, not that it shows what you expect (Session 10 caught a clothing store image that way).
2. **Page-level macro tone trumps hero details.** A "cream top, dark bottom" composition will always look similar to another "cream top, dark bottom" composition at thumbnail size, even if the content within each section is wildly different. Solution: make each composition's WHOLE PAGE one consistent macro tone, and pick a different macro tone for each sibling. Restaurant settled on dark / bright cream / yellow — three opposite ends of the spectrum.
3. **Dark bands at the bottom of cream layouts are a trap.** They feel safe and editorial, but they collapse two-region silhouettes into "the same shape with different details". Avoid the pattern entirely.
4. **Browser cache trap when verifying.** Playwright Chromium aggressively caches preview PNGs. After regenerating, the listing page may show the OLD images. Force-refresh by mutating `img.src` with a `?cb=<timestamp>` query string via `browser_evaluate`, OR navigate directly to `/media/.../preview.png?v=<n>` first.

### Watch out for the Session 8/9 timing trap (still unfixed)
When you add a DNA entry to a slug that *already* has a generated preview, that preview was rendered through the legacy fallback and is now stale. The `generate_previews` "skip if exists" branch will not regenerate it. Always run `python manage.py generate_previews --force --only <slug>` after creating or modifying a DNA entry for an existing template — **AND** delete the canonical-named PNG file on disk first, otherwise Django storage will append a random suffix to the new file (the DB row will still point correctly to the suffixed file, so functionally fine, but the disk gets cluttered with orphans). Session 10 also taught us to clear `media/preview_imagery/<key>/` when imagery URLs change so the new ones get downloaded fresh.

The clean recipe used in Session 9 to avoid the orphan trap:
```bash
# 1. Delete the row + canonical file + any suffixed file via a small Django shell snippet
python -c "import django, os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','marketweb.settings'); django.setup(); ..."
# 2. Then re-run WITHOUT --force so the new file lands at the canonical name (no collision)
python manage.py generate_previews --only <slug>
```

### Immediate next step (highest impact) — Phase 2g.2
**~~Add a third template~~ The archetype-reuse validation was completed in Session 13 with `dermatologia-elite-roma` under the `specialist` archetype. Structurally it worked (zero new HTML files, all 9 routes 200). But the audit uncovered 17 distinct copy leaks in the chrome that must be fixed before the next reuse template ships. See TODO_NEXT.md Phase 2g.2 for the full lift plan.**

After Phase 2g.2 closes, run the same validation on the restaurant side — add a second `fine-dining` template (e.g. `tartufo-truffle-house`) under the Gusto chrome and repeat the leak audit. The fine-dining chrome likely has the same class of literals baked in; a second lift pass will be needed there too.

Then resume Phase 2f DNA rollout: Agency → Lawyer → Real Estate archetype splits. When authoring each new archetype's skin, apply the Session 13 lesson from the start: **every string in a per-archetype skin must either be a CSS rule or come from `site.*` / `page_data.*` / loop items** — no literal brand-like text, no literal city names, no literal CTA labels.

### Phase 2f — DNA rollout to other categories (still pending)
The DNA rollout from Sessions 7-10 stopped after Restaurant. Three more categories still need archetype splits — Agency (3 archetypes), Lawyer (2), Real Estate (2). See the previous handoff note for the recipe; the constraint is now both:
1. Distinct preview compositions per archetype (Sessions 7-10 lessons)
2. Inner-page chrome under `templates/live_templates/<category>/<archetype>/` if the new templates are to ship as full sites (Session 11 architecture)

### Phase 2d polish (still pending from previous sessions)
1. Optimize PNG file sizes (~4 MB → ~500 KB via Pillow `optimize=True` or oxipng)
2. Cormorant Garamond on dark backgrounds reads thin (Lex, Villa, Cardio specialist) — consider bumping weight or swapping serif at low luminance
3. Add `media/preview_imagery/` to .gitignore
4. **DNA-fallback timing trap safety net** — see TODO_NEXT.md for options (a/b/c)
5. **`--force` orphan cleanup** — auto-delete the canonical file before saving so Django storage doesn't suffix
6. **Imagery URL validation** — Session 9 hit one HTTP 404 from Unsplash; a `--validate-imagery` flag would catch these before a full regeneration run

### Phase 3 (Interactivity & Accounts) — unchanged
1. Tag seeding and filtering
2. User authentication views
3. Commerce flow
4. Editor + projects integration
5. Live demo iframe per template

### Key Files for the DNA System (preview screenshots — Sessions 7-10)
- `apps/catalog/template_dna.py` — DNA registry + vocabulary (the source of truth)
- `apps/catalog/templatetags/preview_extras.py` — `at` filter for image indexing in loops
- `apps/catalog/preview_imagery.py` — `IMAGERY_CONFIG` with per-archetype keys
- `apps/catalog/management/commands/generate_previews.py` — DNA-aware pipeline
- `templates/preview_compositions/<category>/<archetype>.html` — bespoke per-template preview HTML (1600x900 fixed)
- `templates/preview_compositions/<category>.html` — legacy fallback for non-DNA templates

### Key Files for the Live Template System (multi-page websites — Session 11)
- `apps/catalog/template_content.py` — content registry (per-template page copy + helpers `has_live_template`/`get_content`/`find_page`/`find_post`)
- `apps/catalog/views.py` — `LiveTemplateView` (resolves DNA + content in `setup()`, dispatches to per-archetype/page-kind template)
- `apps/catalog/urls.py` — three URL patterns: `live_template_home`, `live_template_page`, `live_template_post`
- `templates/live_templates/<category>/<archetype>/_base.html` — standalone HTML doc for the archetype (NOT extending `base.html`)
- `templates/live_templates/<category>/<archetype>/<page-kind>.html` — per-page-kind layouts (home, about, services, team, blog_list, blog_detail, contact, appointment, menu, gallery, reservations)
- `templates/catalog/template_detail.html` — conditional CTA (`Apri anteprima completa` if content registered)

### Constraints (unchanged)
- Do not redesign architecture or model structure
- Preserve premium UI — listing/detail/card templates should not be modified for preview changes
- Follow services/selectors pattern for new business logic
- Italian content (D-016)
- Update coordination files at end of session

## Coordination Rules

- Backend-core owns: models, migrations, admin, services, selectors, management commands
- Premium-UI owns: templates/, static/, design system, frontend components
- **Real-preview-assets** owns: `apps/catalog/preview_imagery.py`, `apps/catalog/management/commands/generate_previews.py`, `templates/preview_compositions/`
- **Template-DNA-system** owns: `apps/catalog/template_dna.py`, `apps/catalog/templatetags/preview_extras.py`, `templates/preview_compositions/<category>/<archetype>.html` files
- **DNA-pilot sessions** (medical, restaurant, ...) own per-category vocabulary additions in `template_dna.py`, the per-category composition folder, and the matching imagery pool keys
- **Template-completeness-pilot** owns: `apps/catalog/template_content.py`, `LiveTemplateView`, the live preview URL patterns, `templates/live_templates/<category>/<archetype>/` skin folders
- All sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md, TEMPLATE_REGISTRY.json, BRAND_SYSTEM_GUIDELINES.md, CATEGORY_ROADMAP.md at end
