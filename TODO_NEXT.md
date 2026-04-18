# TODO Next

## 🟢 Current State (2026-04-19 · after Session 70 A.14b Brace (street-modern · restaurant-continuation family · second template) Editor + Multi-locale Enrollment merge · CLOSES RESTAURANT-CONTINUATION FAMILY)

Baseline `phase-integration-baseline-v15` tip is **`7c064f8`** (A.14b merge), pushed to origin. **12 archetype slugs enrolled / 13 templates editabili end-to-end**. Twelfth enrollment closes the restaurant-continuation family: Vertex + Pragma + Gusto + specialist + classic-gold + modern-transparent + mass-market + ultra-luxury-cinematic + editorial-designer-grid + cinematic-photographer + trattoria-warm + **street-modern** are all multi-locale enrolled. **Five families editor-complete** (law · medical-specialist · real-estate · portfolio · **restaurant-continuation**). Four families still open for editor enrollment · 7 templates residue total.

- **Vertex** (`agency-creative-studio`) · 1 template · 284 editable fields (81 translatable · 203 global) · 4 mutable lists · customer image upload on 2 image fields · full A.3c→A.5 feature set · **first archetype to expose image-in-dict-row** via `studio.partners[].portrait` col (production since A.3a/A.4)
- **Pragma** (`corporate-suite`) · 1 template · ~53 scalar + 1 image + 3 readonly indexed lists · 53 translatable · no repeater mutable
- **Gusto** (`fine-dining`) · 1 template · ~108 scalar + 2 image + 3 readonly indexed lists · 97 translatable · no repeater mutable · no image per-locale
- **specialist** (archetype shared by `cardio-studio-specialistico` + `dermatologia-elite-roma` · 2 templates · A.9) · ~95 scalar + 5 image + 6 readonly indexed lists · 77 translatable fields per-template · D-064 divergent home premium sections kept registry-only · no repeater mutable · no image per-locale
- **classic-gold** (Lex · 1 template · A.10 · first dedicated-schema slot of the law family) · ~102 scalar + 1 image + 6 readonly indexed lists · 79 translatable · `.lx-*` skin AR RTL authentic
- **modern-transparent** (Juris · 1 template · A.11 · closes law family via second dedicated-schema) · ~180 scalar + **zero image fields** + 6 readonly indexed lists · 110 translatable · `.jr-*` skin AR RTL · complex shapes outside perimeter
- **mass-market** (Casa · 1 template · A.12 · first dedicated-schema slot of the real-estate family) · ~185 scalar + **zero image fields** + 15 readonly indexed lists · 134 translatable · `search_widget` flat 14-scalar · `.dm-*` skin AR RTL
- **ultra-luxury-cinematic** (Villa · 1 template · A.12b · closes real-estate family via second dedicated-schema) · ~175 scalar + 4 scalar image + 14 readonly indexed lists, 3 with image cols — 18 editable image surfaces · 128 translatable · `.vp-*` skin AR RTL
- **editorial-designer-grid** (Chiara · 1 template · A.13 · first dedicated-schema slot of the portfolio family) · ~140 scalar + 1 scalar image (`studio.founder.image` nested-dict · Vertex `home.cover.image` precedent) + 11 readonly indexed lists, **1 with image col at deep path 2 levels** (`home.featured_works.items[].image` × 4 rows — third precedent of image-in-dict-row after Vertex + Villa) — **5 total editable image surfaces** (1 scalar + 4 image cells) · 112 translatable · 212 global · `.ed-*` skin AR RTL (46 `html[dir=rtl]` rules · highest count of any enrolled archetype, Session 37 D-070 perfection pass) · complex shapes outside perimeter
- **cinematic-photographer** (Pixel · 1 template · A.13b · closes portfolio family via second dedicated-schema) · 8 sidebar groups · ~140 scalar + **1 scalar image globally** (`home.hero_image` top-level · no image-in-dict-row · no nested-dict image) + 10 readonly indexed lists (9 tuple + 1 dict `pubblicazioni.press`) · 107 translatable · 211 global · `.cp-*` skin AR RTL (38 `html[dir=rtl]` rules · Session 39 D-071 Pixel perfection pass) · complex shapes outside perimeter (posts.* incl. `posts[].cover_image` + series_detail stay registry-only — **sixth uniform detail-page enforcement** after Lex/Juris/Casa/Villa/Chiara)
- **trattoria-warm** (Sapore · 1 template · A.14 · first dedicated-schema slot of the restaurant-continuation family) · 8 sidebar groups · ~141 scalar + **7 scalar image fields** + 2 image-in-dict-row lists (home.family + storia.family · 6 portrait cells) — **13 total editable image surfaces** · 20 readonly indexed lists (15 base + 5 `menu.sections.{i}.dishes` deep-path tuple-in-dict-list parent) · 121 translatable · `.tw-*` skin AR RTL (18 rules) · complex shapes outside perimeter · **posts list empty**
- **street-modern** (Brace · 1 template · A.14b · **closes the restaurant-continuation family** via second dedicated-schema · staged progression with Sapore) · 8 sidebar groups · ~170 scalar + **3 scalar image fields** (home.hero_image · lab.hero_image · moments.featured_image) + **6 image-in-dict-row lists** (home.menu_strip_items × 6 · home.crew × 3 · home.atmo_strip × 3 · lab.crew × 4 · moments.grid × 6 + **menu.sections.{0..4}.items deep-path** × 19 cells) — **44 total editable image surfaces** (3 scalar + 41 cells · 3.4× Sapore) · **30 readonly indexed list entries** (22 parent + 5 `menu.sections.{i}.items` dict-in-dict-list deep-path + 3 `ordina.routes.{i}.lines` tuple-in-dict-list deep-path) · 148 translatable · 401 global · `.sm-*` skin AR RTL (24 rules) · **first `order` page kind enrolled** · **no form structures** (Brace ships zero · smaller out-policy than Sapore) · **posts list empty**
- **Multi-locale editor on all twelve** · 5 locales (it/en/fr/es/ar) with authentic RTL preview for Arabic · per-locale `@<locale>:<path>` storage · authored-only fallback · sidebar pill switcher · flush-before-switch · "per lingua" marker · image overrides global/plain-keyed at deep paths · **deep-path overrides (both dict-in-dict-list AND tuple-in-dict-list parent) render end-to-end on all 5 public-preview locales** (browser-walk verified on Sapore menu + Brace menu + Brace ordina · neighbor cells stay untouched)
- Orphan asset GC available via `python manage.py gc_project_assets` (default dry-run, `--apply`, `--project`, `--grace`)
- 266/266 server tests passing, smoke_full 834/834 unchanged, catalog 20/20 `published_live` unchanged
- **12 archetype slugs enrolled · 12 multi-locale enrolled · 13 templates editable end-to-end**
- **Families CLOSED (5)**: law (Lex + Juris sequential dedicated-schema · A.10+A.11) · medical-specialist (Cardio+Derm shared-schema · A.9) · real-estate (Casa+Villa staged dedicated-schema · A.12+A.12b) · portfolio (Chiara+Pixel staged dedicated-schema · A.13+A.13b) · **restaurant-continuation (Sapore+Brace staged dedicated-schema · A.14+A.14b)**
- **Staged dedicated-schema closure topology has 3 real closed precedents** (real-estate · portfolio · restaurant-continuation) · staged is the most-applied D-098 topology. Shared-schema (A.9 specialist · 1 precedent) and sequential dedicated-schema (A.10+A.11 law · 1 precedent) round out the three.
- **Render-side contract-alignment fix `f66ac24` is cross-pattern operationally confirmed**: 3 editor layers (`services._resolve_path` · `schema._resolve_path` · `rendering._apply_indexed`) aligned on list numeric indexing · covers both tuple-in-dict-list parent (Sapore menu) and dict-in-dict-list parent (Brace menu · Chiara-precedent shape) uniformly.
- **Detail-page registry-only policy enforced uniformly on 6 archetypes**: Lex `notabili` · Juris `insights` · Casa `posts` · Villa `posts` · Chiara `posts` · Pixel `posts` + `series_detail`. Sapore + Brace both ship `posts: []` (structural absence, not a perimeter decision) · count stays at 6.
- **Guard removal pattern consolidated** · 3 precedents: Villa-out (A.12b) · Pixel-out (A.13b) · Brace-out (A.14b) · each contract-tested via symmetric `test_*_was_removed_from_*_tests`.
- **Image surface patterns with multiple precedents**: single-scalar-image (Pragma · Pixel) · multiple-scalar-images (Gusto · specialist · Villa · Sapore) · nested-dict-scalar-image (Vertex · Chiara) · image-in-dict-row (Vertex · Villa · Chiara deep path 2 levels · Sapore · **Brace with both shallow and deep-path dict-in-dict-list**). Recipe scales downward and upward.
- **Families still open for editor enrollment (4 families · 7 templates total)**: **ecommerce** (Bottega + Luxe · 2 templates) · **medical-other** (Salute + Benessere + Famiglia · 3 templates) · **agency-secondary** (Aura · 1 template) · **startup-saas** (Elevate · 1 template)

No explicitly-deferred debt is pending. 13 commit-clean phases delivered back-to-back (A.6 → A.14b). A.14b was 3 commits total on branch (schema · lifecycle · merge) · no additional infra fixes required (Brace fully reused A.14 `f66ac24`).

### Next workstream — immediate candidates (no family open; 4 residual families + 1 housekeeping task)

A.14b closed a family; it does NOT prescribe the next workstream. Pick based on leverage (family closure > single-template single-category close). Ranking for A.15:

- [ ] **A.15 · eCommerce family (Bottega `artisan-workshop` + Luxe `fashion-editorial`)** — **top candidate**. Two-template family closure. `artisan-workshop` (Bottega) is the current outside-gate reference in the unsupported-archetype fixtures (rotated into that role from A.14b). Bottega + Luxe have commerce-foundation overlap (Phase 3a+3b already landed `apps/commerce/` seed for both) — **Step-0 must check whether the editor schema should avoid overlap with commerce-managed content**: the editor should edit presentational/marketing content (hero, copy bands, gallery, about/story page) · NOT commerce-admin state (product catalog, prices, inventory · those live in `apps/commerce/` models). Expected topology: shared-schema or staged dedicated-schema depending on audit · most likely staged given shape divergence hypothesized by Session 41/42 observations. ~3-4 commits.
- [ ] **A.15 alt · Medical-other family (Salute + Benessere + Famiglia)** — three single-template medical archetypes (`medical-clinic` · `wellness-serene` · `family-warm`) rolled `published_live` in Session 51 but never enrolled. **Three separate phases preferred over bundling** — the "one-phase-one-archetype" discipline is now 13 phases strong (A.6 → A.14b). Three enrollment waves would take A.15 + A.15b + A.15c.
- [ ] **A.15 alt · Aura (agency-digital-studio) individual enrollment** — low novelty, low risk, single template. Closes agency-secondary category (Vertex already enrolled as `agency-creative-studio`).
- [ ] **A.15 alt · Elevate (startup-saas-landing) individual enrollment** — low novelty, single template. Closes the startup-saas category.
- [ ] **A.15 alt · MEMORY.md maintenance mini-phase** — auto-memory index ~29-30KB sopra warning-soglia 24.4KB (grows ~1KB per enrollment phase). Index entries can be shortened without losing content. **Separate housekeeping task, NOT bundled with an enrollment**. Low-value-low-risk; queue for a "breather" session between bigger phases.
- [ ] **A.15 alt · Selective editor polish** — search Cmd-K locale-aware ranking · "solo translatable" sidebar filter · badge-per-group pre-sync at mount · palette page-slug-match boost · sticky-last-page on reopen. Defer unless customer signal surfaces.
- [ ] **A.15 alt · Media evolution / remote storage (S3/Cloudinary)** — defer. A.12b+A.13+A.13b+A.14+A.14b validated current infra scales to 44-image-surface archetypes including deep-path dict-in-dict-list and tuple-in-dict-list without pressure. No technical trigger.
- [ ] **A.15 alt · Editor operator tools** — defer. Admin-facing work belongs after another round of scale-out consolidates the editor footprint.
- [ ] **A.15 alt · Repeater-per-locale first wave** — defer. Out-of-scope family per D-098 · opens localized repeater content only if customer signal emerges.

Recommended framing: **A.15 eCommerce Step-0 planning session on Bottega + Luxe** — closes the ecommerce category which is already live end-to-end (commerce foundation v1+v2). Highest leverage among the 4 residual families.

**What NOT to open immediately (red-lamps)**:
- **Do NOT bundle ecommerce + medical-other** · discipline violation (one phase = one archetype decision · 13 phases strong)
- **Do NOT re-open restaurant family** · CLOSED post-A.14b · any "coverage expansion on Sapore/Brace" would be scope-creep, not enrollment
- **Do NOT open detail-page editing as side quest** · horizontal feature cross-archetype (affects 6 archetypes with per-item content) · single-archetype special-casing is a policy violation
- **Do NOT bundle MEMORY.md maintenance with an enrollment** · housekeeping stays separate by design
- Remote asset storage (no technical pressure · current infra dimostrato scalare)
- Repeater-per-locale family (no customer request · D-098 invariant)
- Search Cmd-K localized ranking (polish only · low signal)
- Editor operator tools (better after scale-out consolidates footprint)
- Any bundled multi-archetype phase (13 phases A.6→A.14b have all respected discipline · preserve)
- Coverage expansion on already-enrolled archetypes · bloats phase without customer pull
- Mixing Aura / Elevate / medical-other with ecommerce · each is a separate workstream

### Carried-forward observations (not blocking)

- [ ] L2 — programmatic focus on a collapsed sidebar accordion doesn't trigger iframe page-aware nav (pre-A.2.8 observation). Low impact since palette jump / click flows work.
- [ ] Badge per-group not synced at mount with persisted overrides (pre-A.2.8 observation). Customer-cosmetic, no functional gap.
- [ ] Sticky last page on reopen (currently one-shot only on row-op reloads, by design). Customer-convenience opt-in if requested.
- [ ] Palette page-slug-match boost in ranking (Vertex-specific "studio" ambiguity). Low signal so far.
- [ ] A.3d widen repeater to `manifesto.principles`, `manifesto.promise_stats`, `lavori.archive_stats` (pattern validated in A.3c). Low priority; no customer request.
- [ ] Search Cmd-K palette could become locale-aware (show the translated label when a translatable field is selected in an active locale); not urgent — current behavior is correct, just not localized.

### A.7 / A.7b / A.8 fuori-scope esplicitamente rinviati (respect when planning)

- Repeater per-locale (struttura + row content restano globali — A.10+ only on explicit customer signal)
- Image per-locale (asset uploaded once, universal — A.10+)
- Full RTL editor chrome pass (editor shell stays LTR, preview iframe RTL authentic is sufficient)
- Per-locale publish gating / approval (single atomic publish is the contract)
- Translation memory / ML helpers (out of product scope)
- "Solo translatable filter" UI toggle (optional polish, not required)
- Pragma coverage expansion — the current 53 translatable fields are the A.7b-closing set; any Pragma field gap is A.9+ scope
- Gusto coverage expansion — the current 97 translatable fields are the A.8-closing set; `prenota.form_sections` intentionally omitted (IT-only parity gap · guard `{% if %}` in skin). Any Gusto gap is A.9+ scope
- Search Cmd-K locale-aware ranking — current shape is correct, just not localized; polish only

### Scope red-lamps (to resist when planning)

- Don't enroll a new archetype in multi-locale without its own lifecycle regression test (D-098 binding).
- Don't bypass D-097 at the rendering layer — if customer requests cross-locale suggestion, surface it as explicit UI flow, not storage default.
- Don't add cron / scheduler for A.5 GC. Management command manual is the contract per D-094.
- Don't replace the `/media/` accept path in `validate_value` — A.10 must live in parallel (D-095 binding).
- Don't bundle A.8 (third archetype editor support) + selective multi-locale expansion in one phase — two independent streams, merging them loses leverage.
- Don't flip `mutable=True` on existing readonly indexed lists (Pragma pillars/kpi_strip/leadership) without a dedicated A.3-family rollout test — repeater family decisions are orthogonal to multi-locale.

---

## 🟢 Phase A.2 — Editor UX + Live Preview — ✅ CLOSED (Session 57, 2026-04-16)

Per D-088: the editor is now a premium app shell — debounced JSON autosave (400ms), wide device-aware preview canvas, 14-group accordion sidebar with icons + search + reset-to-baseline, hover-to-highlight via postMessage to `preview-bridge.js`, baseline before/after compare slider, clean notification hygiene (no Django-messages stacking). Rich customization widened ~doubled on Vertex (~39 editable fields across 14 grouped sections, was 23/4). 20/20 project tests green (4 new).

**What's binding for Phase A.3 and every later subphase (carries forward from D-088 + D-087 + D-086):**
- **Autosave is the single customer mutation path.** Any new field type in the schema MUST be consumable by the JSON autosave payload (`{content:{}, tokens:{}}`). Don't add new form-POST endpoints for per-field writes.
- **Revisions are explicit, not reflexive.** Only `Salva versione` or `Pubblica` / `Sposta in bozza` create revisions. Autosave never does. Preserve this — it's why the cronologia stays readable.
- **Highlight groups MUST declare `region`.** Every schema group needs an `icon` + `region` CSS selector so the UI can map field focus/hover to a preview overlay. Groups without a selector degrade silently.
- **Baseline preview contract.** `?baseline=1` MUST short-circuit the project overlay in `LiveTemplateView.setup`. Don't refactor into post-render diffing — the contract is "same pipeline, deterministic diff".
- **`preview-bridge.js` stays behind `{% if preview_project %}`.** The baseline iframe must not load it. Skin authors adding new archetypes must preserve the guard.
- **Editor shell is standalone.** Don't extend `base.html` from `project_editor.html`. Marketing chrome has no place inside the editor viewport.
- **Post-save aggregate reads bypass prefetch.** Any `.count()` on reverse-relations after a mutation goes through a fresh queryset to avoid stale cached results.

**Phase A.3 — immediate next step (repeater widgets + second archetype):**
- [ ] Schema field type `"list"` with `of: {...}` per-item spec. UI: add / remove / reorder rows, per-item validation, min/max per blueprint §6.
- [ ] First repeaters on Vertex: `home.ledger_rows` + `home.capab_items` (currently in `LOCKED_KEYS_NOTE` — promote them out once widget ships).
- [ ] Add `apps.editor.schema` for a second archetype — recommend `clinic` (Salute) or `corporate-suite` (Pragma). MUST reuse the `icon` + `region` metadata pattern from A.2.
- [ ] Re-verify `customize_start` bounces fire for remaining non-editable templates once the second archetype lands.
- [ ] **Polish deferred from A.2:** sync baseline iframe scroll to edited iframe when compare opens. Currently the baseline loads at page top regardless of where the edited iframe is scrolled.
- [ ] **Polish deferred from A.2:** use `webtemplate-slug-specific` CSS selectors for `region` (e.g. the current `.vx-hero` works for Vertex but won't map across archetypes — Phase A.3 should either re-select per archetype or introduce a `data-mw-region="hero"` attribute baked into each skin).
- [ ] **Polish deferred from A.2:** publish / unpublish success toast in the editor shell (currently only the tier chip changes colour — honest but subtle).

**Phase A.4+ (unchanged) — locale activation / page registry / publish-time validators / image upload / full multi-locale / smoke integration.**

**Nothing else.** Per D-085, no new templates / archetypes / categories / preset author work lands until A.8 is green.

---

## 🟢 Phase A.1b — Public Customize Flow — ✅ CLOSED (Session 56, 2026-04-16)

Per D-087: `apps/accounts/` ships branded login/signup/logout + `/projects/start/?template=<slug>` single-entry flow + `get_or_create_project_for_template` (one draft per `(owner, template)`) + X-Frame-Options SAMEORIGIN on `LiveTemplateView`. Zero schema growth — editor field set unchanged. 24/24 unit tests + 834/834 catalog smoke + 11-step authenticated Playwright walk all green.

**What's binding for Phase A.2 and every later subphase (carries forward from D-087 + D-086):**
- **`/projects/start/` is the single public entry.** Do not add a parallel customize-create URL. Views that need to launch an editor flow link to `/projects/start/?template=<slug>`.
- **Unsupported archetypes bounce honestly.** When a template's DNA archetype is not yet in `_ARCHETYPE_SCHEMAS`, `customize_start` redirects to the template detail page with an info message. Never land a customer on a blank editor. When you add a new archetype to the editor, remove no code — the bounce is driven by `is_supported_archetype()`.
- **One draft per `(owner, source_template)`.** Multi-draft is a later opt-in — do not relax the uniqueness until a richer dashboard UX is in place to disambiguate variants.
- **`/admin/login/` is staff-only.** Customer surfaces stay at `/account/`. `LOGIN_URL` must not regress.
- **`?next=` stays preserved across login↔signup switching.** The login page's signup link carries `?next=`; likewise signup carries login. Don't break the round-trip.
- **X-Frame-Options opt-in per view.** Keep project-wide default as Django's `DENY`. Only `LiveTemplateView` opts into `SAMEORIGIN` for the editor iframe.

**Phase A.2 — immediate next step (Editor extension to 1 more archetype + repeater widgets):**
- [ ] Add `apps.editor.schema` entries for a second archetype — recommend `clinic` (Salute) because medical has the richest stats/cards/services shape and exercises `section_order` visibility toggles. Alternative: `corporate-suite` (Pragma) for a growth-market seed.
- [ ] Build repeater widget groundwork: `apps.editor.schema` field type `"list"` with add/remove/reorder + per-item field spec. Exercise on `home.ledger_rows` (Vertex) + `home.services` (Salute).
- [ ] Section visibility toggles: a `home.sections_hidden` set on the project that filters `page_data.section_order` at render time.
- [ ] Section reorder: per-project `section_order_override` list with baseline diff.
- [ ] **When you add the second archetype, re-verify `customize_start` bounces still fire for the remaining 18 non-editable templates** — guard against a missing-archetype regression masking as "works for me on Vertex".

**Phase A.3+ (unchanged) — locale activation / page registry / publish-time validators / image upload / full multi-locale / smoke integration.**

**Nothing else.** Per D-085, no new templates / archetypes / categories / preset author work lands until A.8 is green.

---

## 🟢 Phase A.1 — Editor Foundation v1 (vertical slice on Vertex) — ✅ CLOSED (Session 55, 2026-04-16)

Per D-085 (editor-first) + D-086 (A.1 slice shape): `apps/projects/` + `apps/editor/` shipped as real, working modules. First slice exercises `vertex-creative-agency` (archetype `agency-creative-studio`) end-to-end — create project → 23 editable content fields + 5 design tokens → sparse-diff save → iframe preview overlay → publish/draft → revision snapshots. 834/834 catalog smoke unchanged. 12/12 unit tests green. See SESSION_LOG Session 55 + DECISIONS D-086.

**What's binding for Phase A.2 and every later subphase:**
- **Overlay pipeline is the contract.** `?project=<uuid>` on the catalog preview URL + `apply_project_overrides()` is how every archetype ships into the editor. Do NOT add a parallel `/projects/<uuid>/preview/<page>/` route — one surface, one pipeline.
- **Sparse-diff is the storage contract.** An override row equal to baseline is deleted, not stored. Upstream registry polish flows through to customer projects for free. Don't regress to full-snapshot storage.
- **Archetype whitelist is explicit, not permissive.** `apps.editor.schema._ARCHETYPE_SCHEMAS` gates which templates can seed a project. Adding a template = author the schema entry first, not "let's see if it renders".
- **DNA-lock at service layer, not UI-only.** UI hides the lock; `validate_key_path()` prevents a crafted POST from bypassing it. Preserve both layers.
- **Snapshot queries fresh.** `_build_snapshot()` must NOT consume the view's prefetched `content_overrides` cache — the cache freezes pre-save state. The regression test is there to catch a relapse.

**Phase A.2 — immediate next step (Editor extension to 1 more archetype + repeater widgets):**
- [ ] Add `apps.editor.schema` entries for a second archetype — recommend `clinic` (Salute) because medical has the richest stats/cards/services shape and exercises `section_order` visibility toggles. Alternative: `corporate-suite` (Pragma) for a growth-market seed.
- [ ] Build repeater widget groundwork: `apps.editor.schema` field type `"list"` with add/remove/reorder + per-item field spec. Exercise on `home.ledger_rows` (Vertex) + `home.services` (Salute).
- [ ] Section visibility toggles: a `home.sections_hidden` set on the project that filters `page_data.section_order` at render time.
- [ ] Section reorder: per-project `section_order_override` list with baseline diff.

**Phase A.3 — Locale activation (mirrors Phase A.7 plan):**
- [ ] Project `locale` → multi-locale tree. Each `ProjectContent` row gains a `locale` column (or move to a `(project, locale, key_path)` unique index). Editor gains a locale switcher pill matching the catalog preview `?lang=` shape.

**Phase A.4 — Page registry:**
- [ ] Add/rename/hide pages (respecting D-053 baseline-required pages per category). Editor shows "questa è una pagina baseline, non puoi eliminarla" block instead of a delete button.

**Phase A.5 — Validators (D-053 / D-054 / D-057 at publish time):**
- [ ] Publish-gate validator: required baseline pages present + required field paths non-empty + palette-vs-sibling D-054 distance ≥ threshold. Block publish with actionable error list when failing.

**Phase A.6 — Image upload + library:**
- [ ] `ProjectAsset` model (image upload to `media/projects/<uuid>/`) + `image` / `gallery` field types in schema. Starts with hero `cover.image` on Vertex.

**Phase A.7 — Locale per-locale tree (full):**
- [ ] Full CHROME_I18N / language-switcher awareness in project UI. Per-locale fallback policy (hide vs. fall-back-to-default).

**Phase A.8 — End-to-end QA + smoke integration:**
- [ ] Extend `smoke_full.py` with `?project=<uuid>` sampling on the supported archetypes. Ensure every published project renders 200 at the overlay URL for every page slug.

**Nothing else.** Per D-085, no new templates / archetypes / categories / preset author work lands until A.8 is green.

---

## 🆕 Session 54 — Catalog Expansion Strategy + Profession Preset Taxonomy — ✅ CLOSED (Session 54, 2026-04-15)

Per D-083 (modello a 4 livelli), D-084 (tassonomia 14 categorie), D-085 (editor-first sequencing), questa è una sessione **strategica/architetturale**: non implementa template, non apre rollout, non tocca i 20 `published_live`. Tre deliverable concreti: (a) `CATALOG_EXPANSION_STRATEGY.md` — strategia 11-section completa (audit + tassonomia + modello + archetipi + preset + DNA-locked vs editable + editor strategy + rollout priority + numerical proposal + decisione finale); (b) `PROFESSION_PRESET_TAXONOMY.md` — registro concreto di ~75-90 preset target su 14 categorie e 28-30 archetypi (19 esistenti + 11 nuovi); (c) aggiornamenti coordinati a CATEGORY_ROADMAP/TODO_NEXT/DECISIONS/AGENT_HANDOFF/SESSION_LOG/MEMORY.

**Catalogo state invariato dopo Session 54: 20/20 published_live.** Strategy-only session.

### 🚨 Decisione vincolante (D-085 — Editor-First Sequencing)

> **Phase A — Editor Foundation v1 — è il prossimo workstream.**
> Nessun nuovo template `published_live`, nessun nuovo archetipo, nessuna nuova categoria viene aperta finché Phase A non è chiusa.

Le sessioni 55+ devono concentrarsi su **`apps/editor/`**. Le proposte di "fai un altro template / un'altra categoria / un altro preset" vanno respinte fino a chiusura Phase A.

---

## 🔴 Phase A — Editor Foundation v1 (PROSSIMO WORKSTREAM, da aprire)

**Goal:** aprire `apps/editor/` su tutti i 20 template attuali. Un cliente può clonare un template, modificare copy/foto/team/listino/contatti/palette/font, attivare locali, pubblicare in `draft` o `published_live`.

**Source of truth:** `EDITOR_SCHEMA_BLUEPRINT.md` (D-064, esistente, ~478 LOC). `CATALOG_EXPANSION_STRATEGY.md` §8 per i criteri di accettazione.

**Sub-phasing:**
- [ ] **A.1** — `CustomerProject` + `ProjectContent` + `ProjectDesignTokens` models + migrations + admin CRUD. Source: `EDITOR_SCHEMA_BLUEPRINT.md` §7.
- [ ] **A.2** — `LiveTemplateView` overlay: legge da `CustomerProject` quando passato un `project_uuid`, fallback a registry statico altrimenti. Sparse-diff merge.
- [ ] **A.3** — Editor UI v1 form-based (server-rendered, Bootstrap 5 + crispy-forms). Widgets per i `kind` minimi: nav · hero · section (manifesto/facts/services/team/pricelist/timeline_steps/trust_strip/gallery_strip/map_location) · form · contact · blog · footer · locale.
- [ ] **A.4** — Preset library page: lista template autoriali con "Clona come progetto" CTA. Stesso pattern lavora con i preset professionali quando arriveranno in Phase B+.
- [ ] **A.5** — Validators: D-053 baseline page enforcement · D-054 sibling-distance check · D-057 completeness check (`tier=published_live` solo se 100% required field non vuoti).
- [ ] **A.6** — Image upload + library picker (no AI gen v1).
- [ ] **A.7** — Locale activation UI + per-locale tree editor + fallback policy.
- [ ] **A.8** — End-to-end QA + smoke harness + `smoke_editor.py` (clone preset → edit → publish flow).

**Stima totale:** ~14-23 sessioni / 2-3 mesi.

**Acceptance criteria (binding D-085):**
- Editor v1 in produzione, usato da almeno 1 customer-project reale di test interno.
- I 20 template originari restano invariati (zero rewrite).
- `manage.py check` clean, full smoke verde, nessuna regressione su preview live.
- D-047/D-053/D-054/D-057 enforced via validation, non solo via review umana.

---

## ⏸️ Phase B — Trades + Local Food Retail (DOPO Phase A)

**Goal:** prima ondata di nuove categorie post-MVP. Apre `trades` e `food-retail` con 6 nuovi archetypi e 24-30 nuovi preset professionali.

**Pre-condizione:** Phase A chiusa, editor v1 in produzione.

**Sub-phasing:**
- [ ] **B.1** — Categoria `trades` + 3 archetypi: `single-trade-pro`, `multi-trade-team`, `emergency-pro`. Skin folder + DNA + preview composition + imagery pool curato per ciascuno.
- [ ] **B.2** — Preset trades (15-20): idraulico · elettricista · muratore · falegname · fabbro · imbianchino · piastrellista · serramentista · giardiniere · impresa edile · impresa pulizie · ditta multiservizi + 6 emergency-pro (idraulico h24 · elettrico h24 · spurgo · disinfestazione · fabbro h24 · soccorso stradale).
- [ ] **B.3** — Categoria `food-retail` + 3 archetypi: `bakery-warm`, `deli-counter`, `artisan-food-shop`. Skin folder + DNA + preview composition + imagery pool curato per ciascuno.
- [ ] **B.4** — Preset food-retail (12-15): panettiere · pasticcere · gelateria · cioccolateria · biscottificio · salumeria · macelleria · pescheria · formaggi · gastronomia · drogheria bio · enoteca · torrefazione · oleificio · birrificio.
- [ ] **B.5** — Smoke + Playwright walk + 5-locale verification.

**Stima totale:** ~2 mesi (parallel-agent recipe ormai stabile).

---

## ⏸️ Phase C — Beauty + Wellness-Fit (DOPO Phase B)

**Goal:** servizi alla persona. 6 nuovi archetypi + 16-20 preset.

- [ ] Categorie: `beauty` (3 archetypi) + `wellness-fit` (3 archetypi).
- [ ] Preset target: parrucchiere · barbiere · centro estetico · solarium · nail bar · centro massaggi · tatuatore + palestra · CrossFit · powerlifting · yoga · pilates · meditazione · spinning · TRX-HIIT.

---

## ⏸️ Phase D — Hospitality + Automotive (DOPO Phase C)

**Goal:** turismo + servizi auto. 7 nuovi archetypi + 16-20 preset.

- [ ] Categorie: `hospitality` (4 archetypi) + `automotive` (3 archetypi).
- [ ] Preset target: hotel boutique · b&b · agriturismo · masseria · resort · rifugio · ostello design + meccanico · elettrauto · gommista · revisioni · carrozziere · detailing · concessionario auto/moto.

---

## ⏸️ Phase E — Professional + Education (DOPO Phase D)

**Goal:** knowledge economy + formazione. 6 nuovi archetypi + 16-20 preset.

- [ ] Categorie: `professional` (3 archetypi) + `education` (3 archetypi).
- [ ] Preset target: commercialista · consulente lavoro · notaio · architetto · geometra · consulente strategy · consulente HR + scuola lingue · master · scuola cucina · musica · danza · doposcuola · ripetizioni · autoscuola.

---

## ⏸️ Phase F — Events + MVP Preset Extension (DOPO Phase E)

**Goal:** eventi + estensione preset delle 8 categorie MVP. 2-3 nuovi archetypi + 25-37 preset.

- [ ] Categoria `events` (2-3 archetypi) + preset wedding/corporate/catering.
- [ ] Estensione preset MVP: medical (dentista, fisioterapista, psicologo, farmacia, veterinario) + restaurant (pizzeria, sushi, pokè, gastropub, vegan, cocktail bar) + ecommerce (home-décor, outdoor, jewelry, specialty-foods) + business (fintech, industrial-B2B, consulting boutique) + agency (branding, web-only, advertising) + portfolio (illustrator, 3D-motion) + lawyer (civile, penale, famiglia, lavoro, tributarista) + real-estate (locazioni, commerciale).

---

## ⏸️ Phase G — Tier Monetization + Commerce Extensions (DOPO Phase F)

**Goal:** monetizzazione tier (free/pro/business) + commerce v3.

- [ ] Tier free / pro / business con feature gating.
- [ ] Domain mapping per published_live customer projects.
- [ ] Multi-storefront, multi-user editing.
- [ ] Stripe Connect multi-account.
- [ ] Coupons, refunds, tax engine, carrier integration.
- [ ] Marketplace fee + commissioni.

---

## 🟢 Phase 2g3.7 — Lawyer + Real-Estate Live Rollout · CATALOG COMPLETE 20/20 — ✅ CLOSED (Session 53, 2026-04-15)

Per D-082, `lex-studio-legale` (classic-gold archetype — Studio Legale Ferri, Roma, forensic-notarile), `juris-avvocato-moderno` (modern-transparent — Avv. Martini & Partners, Milano, advisory-modern tech boutique), `casa-agenzia-immobiliare` (mass-market — Domus Immobiliare, Milano+Torino, market-approachable residential), `villa-immobili-lusso` (ultra-luxury-cinematic — Villa Prestige, Milano+Portofino, editorial-concierge) flipped from `tier=draft` to `tier=published_live` premium with 4 fully distinct multipage live skins (8 files per archetype × 4 = 32 skin files, ~10,022 LOC HTML), 5 locales fin da subito (it/en/fr/es/ar) with real RTL for Arabic, and sharp D-054 differentiation across every sibling axis + vs business/portfolio/ecommerce/agency + vs Luxe (Villa ≠ Luxe despite shared Cormorant+dark-champagne).

Three concrete deliverables: (a) 4 skin folders (`lawyer/{classic-gold,modern-transparent}/` + `real-estate/{mass-market,ultra-luxury-cinematic}/`) with full RTL CSS + 880px mobile breakpoint + `:focus-visible` rings; (b) 4 IT content registries (~5,277 LOC) + 16 locale trees (~20,538 LOC) authored by 8 parallel sub-agents (4 implementers + 4 translators) — Lex (Slaughter-and-May EN · Gide/Bredin Prat cabinet FR · Garrigues despacho ES · Al Tamimi MENA MSA AR), Juris (Kirkland Startups EN · Bredin Prat VC FR · Cuatrecasas Startups ES · Al Tamimi tech desk AR), Casa (Foxtons/Knight Frank UK EN · Barnes/Century 21 FR · Engel & Völkers Spain retail ES · Emirates Living/Better Homes MSA AR), Villa (FT How to Spend It/Monocle/Sotheby's editorial EN · Le Figaro Propriétés/Emile Garcin FR · Vanity Fair Spain/Savills España ES · Robb Report ME/Esquire ME Property MSA literary AR); (c) D-047 chrome-cleanliness from line one (zero brand literals across 32 HTML files + 4 preview compositions); (d) D-081 counter-policy satisfied on all 4 stats bands from line one.

Validation: `check` clean, **834/834 full sweep** (was 660, +174 net), Playwright real-browser walk at 1440×900 across Lex IT/EN/AR + Juris IT/FR + Casa IT/ES/FR/AR (home + /immobili/ detail) + Villa IT/AR/EN (home + /collezione/ dossier detail). Zero regression on 16 pre-existing templates. **Catalog 20/20 published_live — 8 MVP categories all CHIUSA. Phase 3 unblock gate MET.** See SESSION_LOG Session 53 + DECISIONS D-082 + AGENT_HANDOFF Session 53 binding list.

**Catalog state after Session 53: 20/20 published_live, 20/20 multilingual.** **Zero draft slugs.**
- Live: cardio · derm · gusto · pragma · elevate · chiara · pixel · bottega · luxe · sapore · brace · vertex · aura · salute · benessere · famiglia · **lex · juris · casa · villa**
- Draft: none

**Follow-ups (non blocking, for polish or future sessions):**
- [ ] Villa hero Pexels URL on `realestate-villa[0]` (photo 2351649) renders a rural Tuscan heritage estate at golden-hour — coherent with Chianti/Val d'Orcia positioning but could be swapped for a more classical luxury-villa-with-infinity-pool if a client previewer prefers instant-recognizable premium. LOW priority, current image reads as Castello di Monterò territory.
- [ ] Programmatic D-047 leak enforcement in `smoke_full.py` (grep rendered HTML of each locale for brand literals of *other* templates; catches cross-template chrome leaks at commit time).
- [ ] Mobile audit on Lex/Juris/Casa/Villa at 390×844 viewport — all 4 skins ship with 880px breakpoint, but a dedicated iPhone-size pass would confirm type-scale + nav collapse.
- [ ] Publish-facing catalog index doc (`docs/catalog.md`) summarizing the 20 templates + 14 archetypes for onboarding.
- [ ] Consider ambient video heroes for Villa editorial and Casa daylight in a future polish wave — cost/benefit not yet clear, reserve for post-Phase-3.

---

## 🟢 Phase 2g3.2a — Medical Second Wave Polish + Interaction Fix — ✅ CLOSED (Session 52, 2026-04-15)

Per D-081, three post-rollout defects closed on Salute · Benessere · Famiglia with minimal-surface fixes: (a) `--lf-listbox-radius` token decouples open-dropdown radius from field-radius (default 12px; wellness overrides to 14px); (b) wellness nav CTA reads `{{ site.nav_cta }}` instead of undefined `{{ chrome.nav_cta }}`; all 5 Benessere locale registries now carry `site.nav_cta` with locale-native voice; (c) Salute hero + band stat spans wired to `data-lm="counter"` (animates 0 → target with easeOutCubic); (d) `live-motion.js` thousand-sep heuristic extended to support EN/FR/ES comma-style `28,000` alongside IT dot-style `28.000`; (e) Dynamic Counter Policy binds retroactively + prospectively for every future stats band. 660/660 routes HTTP 200 post-fix. See SESSION_LOG Session 52 + DECISIONS D-081.

**Catalog state unchanged from Session 51: 16/20 published_live.** Polish-only session.

**Follow-ups (non blocking):**
- [ ] Audit Salute band at 390×844 mobile — 4-column grid collapse verified, but the counter band specifically may need tighter padding.
- [ ] Consider Benessere hero meta (4 short facts: "Bergamo Alta · Dal 2011 · Cinque operatori certificati · Silenzio la domenica") as a counter-opt for the year fragment "Dal 2011" if a subtle animation fits the spa register — LOW priority, wellness tone prefers calm.
- [ ] Future real-estate + lawyer rollouts: ensure every stats band ships with `data-lm="counter"` from line one per D-081. Add a regression grep to smoke (`grep -c "data-lm=\"counter\"" templates/live_templates/**/home.html` ≥ 1 per stats-band template).

---

## 🟢 Phase 2g3.2 — Medical Second Wave Live Rollout Premium — ✅ CLOSED (Session 51, 2026-04-15)

Per D-080, `salute-studio-medico` (clinic archetype), `benessere-centro-olistico` (wellness archetype), `famiglia-pediatria` (family archetype) flipped from `tier=draft` to `tier=published_live` with 3 fully distinct multipage live skins (7/7/6 page kinds), 5 locales fin da subito (it/en/fr/es/ar) with real RTL for Arabic via Noto Naskh/Kufi conditional font load, and sharp D-054 differentiation enforced on 9 sibling pairs (Salute vs Cardio/Derm/Benessere/Famiglia · Benessere vs Cardio/Derm/Famiglia · Famiglia vs Cardio/Derm). D-047 chrome-authoring contract applied from line one (zero IT literals across 23 skin HTML files + 10 preview-composition literals lifted into DNA `content` dict keys).

Deliverables: (a) 3 skin folders ~6,735 LOC HTML at `templates/live_templates/medical/{clinic,wellness,family}/` with full RTL CSS + mobile breakpoints + `:focus-visible`; (b) 3 IT content registries (~3,167 LOC) + 12 locale trees (~11,000 LOC) by 6 parallel sub-agents (3 IT + 3 i18n-waves) — Salute NHS/BUPA+Ramsay+Sanitas+MSA-institutional vs Benessere Goop+Marie Claire+Mía+Vogue Arabia vs Famiglia BabyCentre+Doctissimo+Guía Infantil+MSA-parenting; (c) 3 curated Pexels imagery pools replacing legacy Unsplash (medical · medical-wellness · medical-family); (d) 3 preview PNGs regenerated; (e) **stub-files-first pattern** introduced (12 locale stubs `import X_IT as X_LOC` unblock DB sync + translation chicken-and-egg).

Validation: `check` clean, **660/660 full sweep** (was 530, +130 net), Playwright real-browser walk on all 3 templates home/inner/booking/appointment + IT/EN/FR/ES/AR + RTL flipped + language pills + category listing `/templates/medical/` showing 5 distinct products. **Medical category 5/5 published_live. Catalog now 16/20 across 6 categories.** See SESSION_LOG Session 51 + DECISIONS D-080.

**Catalog state after Session 51: 16/20 published_live, 16/16 multilingual.** 4/20 still draft.
- Live: cardio · derm · gusto · pragma · elevate · chiara · pixel · bottega · luxe · sapore · brace · vertex · aura · **salute · benessere · famiglia**
- Draft: lex · juris (lawyer) · casa · villa (real-estate)

**Follow-ups (non blocking):**
- [ ] **Phase 2g3.6d — Lawyer (lex / juris).** Identity-crash siblings per Session 16 audit, need DNA split (classic-gold + modern-transparent).
- [ ] **Phase 2g3.6e — Real-estate (casa / villa).** Same identity-crash, need DNA split (mass-market + ultra-luxury-cinematic).
- [ ] Extend `smoke_full.py` with D-047 leak enforcement (programmatic grep for brand literals across rendered HTML) — would have caught 10 medical preview-composition leaks in Session 51 before browser walk.
- [ ] Mobile audit on Salute/Benessere/Famiglia at 390×844.
- [ ] Consider `blog_list`+`blog_detail` as opt-in for Salute/Benessere/Famiglia in a follow-up pass.

---

## 🟢 Phase 2g3.6f — Agency Live Rollout Premium — ✅ CLOSED (Session 49, 2026-04-15)

Per D-079, `vertex-creative-agency` (`agency-creative-studio`) and `aura-digital-studio` (`agency-digital-studio`) flipped from `tier=draft` to `tier=published_live` premium with two fully distinct multipage live skins (8 file kinds each: Vertex = home/about/services/project_list/project_detail/process/contact + dossier post · Aura idem with sprint replacing process and brief replacing contact), 5 locales fin da subito (it/en/fr/es/ar) with real RTL for Arabic via Amiri+Noto-Kufi (Vertex) / Noto-Naskh+Noto-Kufi (Aura) conditional font load, and sharp D-054 differentiation enforced across every axis (page color cream-paper vs midnight-violet · typography Space Grotesk + Fraunces italic vs Plus Jakarta + JetBrains Mono · hero editorial pull-quote + cover tile vs product-console + sparkline · navbar serif-asterisk vs glow-pill + sprint chip · work indexed-ledger vs metric-card-grid · services 4 disciplines vs 4 capabilities · process manifesto + 6 principles vs sprint + 3 mindset · inquiry long-form dossier brief vs 3-step slot picker · CTA ghost serif italic vs glow violet pill · imagery editorial-craft vs product-console · voice Milan editorial curatorial vs Milan growth-tech direct). Three concrete deliverables: (a) 2 new skin folders (~7,800 LOC HTML) at `templates/live_templates/agency/{agency-creative-studio,agency-digital-studio}/` with full RTL CSS + 720px mobile breakpoint + `:focus-visible` rings; (b) 2 IT content registries (~2,700 LOC) + 8 locale trees (~9,800 LOC) authored by 4 parallel sub-agents (one per locale, both templates) — Vertex Milan curatorial editorial voice (Creative Review/Monocle EN, Libération/M-M Paris vouvoiement FR, Apartamento peninsular ES, Brownbook/Kalimat curatorial MSA AR) vs Aura Milan growth-tech direct (TechCrunch/Linear EN, Maddyness FR, Xataka peninsular tú ES, Wamda product MSA AR); (c) D-047 chrome-cleanliness from line one (zero IT literals across 16 HTML files). One in-flight bug caught + fixed during Playwright AR audit (Aura `chip` field carried literal `<span class="pulse"></span>` — stripped from all 5 Aura locale files). Validation: `check` clean, **530/530 full sweep** (was 443, +87 net), Playwright real-browser walk on Vertex+Aura home/case-detail/lavori/AR/EN/FR/ES — coherent and premium. **Agency category 2/2 published_live. Catalog now 13/20 across 6 categories.** See SESSION_LOG Session 49.

**Catalog state after Session 49: 13/20 published_live, 13/13 multilingual.** 7/20 still draft.
- Live: cardio · derm · gusto · pragma · elevate · chiara · pixel · bottega · luxe · sapore · brace · **vertex** · **aura**
- Draft: salute · benessere · famiglia (medical Phase 2g3.6c) · lex · juris (lawyer Phase 2g3.6d) · casa · villa (real-estate Phase 2g3.6e)

**Follow-ups (non blocking):**
- [ ] **Pexels media swap on Vertex + Aura.** When `PEXELS_API_KEY` is provided in env, replace ~5 hero/section image URLs per template with Pexels-curated equivalents per D-077 protocol. Current Unsplash URLs are visually verified semantically correct (sourced from `portfolio-designer` + `business-startup` proven pools). Format hot-link-public, no API key needed at render time.
- [ ] **Generate static listing PNG previews** for Vertex + Aura via `python manage.py generate_previews --force --slug vertex-creative-agency --slug aura-digital-studio`.
- [ ] **Lift legacy preview composition** at `templates/preview_compositions/agency.html` may carry IT literals from Session 16 — cosmetic for static listing PNG only.
- [ ] **Inline-styled grid mobile audit on Vertex + Aura** at 390×844.
- [ ] **Phase 2g3.6c — Medical second wave (salute / benessere / famiglia).** Next public-catalog promotion gate.
- [ ] **Phase 2g3.6d — Lawyer (lex / juris).** Identity-crash siblings, need DNA split.
- [ ] **Phase 2g3.6e — Real-estate (casa / villa).** Same identity-crash, need DNA split.

---

## 🟢 Phase 2g3.6 — Restaurant Live Completion Premium — ✅ CLOSED (Session 48, 2026-04-15)

Per D-078, `sapore-trattoria-pizzeria` (trattoria-warm) and `brace-street-food-lab` (street-modern) flipped from `tier=draft` to `tier=published_live` premium with full multipage live skins (6 page routes each: Sapore = home/menu/storia/forno/eventi/contatti · Brace = home/menu/lab/moments/ordina/contatti), 5 locales fin da subito (it/en/fr/es/ar) with real RTL for Arabic via Amiri+Noto-Kufi conditional font load, and sharp D-054 differentiation enforced both vs each other and vs Gusto fine-dining. Three concrete deliverables: (a) 2 new skin folders (~6,842 LOC HTML) at `templates/live_templates/restaurant/{trattoria-warm,street-modern}/` with full RTL CSS + 720px mobile breakpoint + `:focus-visible` rings; (b) 2 IT content registries (~1,799 LOC) + 8 locale trees (~6,500 LOC) authored by 8 parallel sub-agents — Sapore warm Roman family voice (Bon Appétit EN, Le Fooding `tu` FR, El País Gastro `tú` ES, Brownbook cultural-publishing AR) vs Brace Bologna street-food brutalist (Eater EN, Le Fooding street `tu` FR, Time Out Madrid `tú` ES, Wamda urban-imperative AR); (c) D-047 chrome-cleanliness from line one (zero IT literals across 14 HTML files, verified 0 leaks across 480 cross-locale checks). Validation: `check` clean, **443/443 full sweep** (was 363), **55/55 form sweep** (was 45), **69/69 hardening sweep** (was 57), 194/194 ecommerce regression, 52/52 gusto i18n regression, 0 IT leaks. **Restaurant category 3/3 published_live. Catalog now 11/20 across 5 categories.** See SESSION_LOG Session 48.

**Catalog state after Session 48: 11/20 published_live, 11/11 multilingual.** 9/20 still draft.
- Live: cardio · derm · gusto · pragma · elevate · chiara · pixel · bottega · luxe · **sapore** · **brace**
- Draft: salute · benessere · famiglia (medical Phase 2g3.2c) · vertex · aura (agency Phase 2g3.6f) · lex · juris (lawyer Phase 2g3.6d) · casa · villa (real-estate Phase 2g3.6e)

**Follow-ups (non blocking):**
- [ ] **Pexels media swap on Sapore + Brace.** When `PEXELS_API_KEY` is provided in env, replace ~5 hero/section image URLs per template with Pexels-curated equivalents per D-077 protocol. Current Unsplash URLs are visually verified semantically correct but Pexels CDN gives more stable crop output. Format: `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=<w>&h=<h>&fit=crop` — hot-link-public, no API key needed at render time. Budget ~30min per template via the Session 47 helper pattern.
- [ ] **Generate static listing PNG previews** for Sapore + Brace via `python manage.py generate_previews --force --slug sapore-trattoria-pizzeria --slug brace-street-food-lab`. Today the listing card shows the gray placeholder. Same Phase-2g2x.3 leftover from Session 47 — non-blocking because the live preview at `/templates/restaurant/<slug>/preview/` is the primary surface.
- [ ] **Lift legacy preview compositions** at `templates/preview_compositions/restaurant/{trattoria-warm,street-modern}.html` may carry IT literals from Session 16 — cosmetic for the static listing PNG only, low priority.
- [ ] **Inline-styled grid mobile audit on Sapore + Brace** at 390×844. The skin folders use explicit `min-width: 0` on grid children at 720px breakpoint per Session 37 lesson, but a deep audit per the smoke `smoke_chiara_perfection.py` extension would lock down the +5pt mobile coherence. ~30min budget.
- [ ] **Phase 2g3.6c — Medical second wave (salute / benessere / famiglia).** Next public-catalog promotion gate. DNA + preview compositions exist, blocked on per-archetype skin authoring at `templates/live_templates/medical/{clinic,wellness,family}/`. Per Session 32+34+41+48 recipe — a green path now. Budget ~3-4h end-to-end via parallel agents.
- [ ] **Phase 2g3.6d — Lawyer (lex / juris).** Identity-crash siblings per Session 16 audit (no DNA, both render Lex's 60-year heritage). Need full DNA split (classic-gold + modern-transparent) + skin authoring + content + 5 locales.
- [ ] **Phase 2g3.6e — Real-estate (casa / villa).** Same identity-crash blocker. Need DNA split (mass-market + ultra-luxury-cinematic) + skin + content + 5 locales.
- [ ] **Phase 2g3.6f — Agency (vertex / aura).** Same identity-crash blocker. Need DNA split (bold-grid + editorial-quiet) + skin + content + 5 locales.

---

## 🟢 Session 47 — Global Media Coherence & Asset Upgrade Pass — ✅ CLOSED (2026-04-15)
Per D-077: Pexels adottato come CDN stock primario (Unsplash legacy preservato), chiave API da env, 5 product hero swaps + homepage hero + 1 video editoriale Luxe lookbook. 53/53 regression green.

**Follow-ups (non blocking):**
- [ ] Generate `/templates/` listing PNG thumbnails — `python manage.py generate_previews --force` richiede Playwright in build-time; oggi il listing card rende placeholder grigio.
- [ ] Consider 1 Pexels image per homepage testimonial (replacing letter avatars MR/GB/LV) — low-priority, editorial pattern valido così.
- [ ] Valutare 1 immagine per step "Come funziona" se il flusso si sente ancora wireframe.
- [ ] Migrate residual Unsplash product images over time (no urgency — current URLs verified coherent).

---

## 🟢 Phase 3b — Commerce Completion v2 — ✅ CLOSED (Session 45, 2026-04-14)
Per D-076, commerce è passato da foundation v1 ("poster operativo single-seller, IT-only, dev-payment") a v2 reale su 4 assi: (1) storefront `/shop/<slug>/` multilingua 5 locales (it/en/fr/es/ar) con RTL arabo reale via `COMMERCE_CHROME` + `STOREFRONT_CONTENT` + `COLLECTION_CONTENT` + LocaleMixin + translations JSONField; (2) payment provider abstraction vera con Stripe integration env-driven + idempotency_key + webhook signature verification + graceful fallback a stub se `STRIPE_SECRET_KEY` manca (`apps/commerce/payments.py`); (3) merchant-scoped dashboard via nuovo `StorefrontMember(storefront, user, role=owner|editor)` modello — `SellerRequiredMixin` ora verifica membership invece di `is_staff` global; (4) customer flow chiuso con `PoliciesView` + `OrderLookupView` (guest self-service reference+email) + `RetryPaymentView` (retry su PaymentIntent failed) + `PaymentPageView` (Stripe Elements). Validation: `check` clean, migration 0003 applied, 73/73 commerce smoke + 45/45 live preview regression + 7/7 ACL matrix green. Credenziali demo: `bottega_owner` / `commerce-v2`, `luxe_owner` / `commerce-v2`. Senza env vars: stub + offline funzionano end-to-end; con env vars + `pip install stripe`: Stripe real-mode operativo. See SESSION_LOG Session 45.

**Catalog state after Session 45: 9/20 published_live (unchanged), 2/9 of those now fully multilingual operational storefronts (Bottega + Luxe). Preview live surface untouched — zero regression.**

**Follow-ups (Phase 3c candidates, none blocking):**
- [ ] **Customer account pages.** Login-gated order history at `/shop/<slug>/account/` per autenticati. Oggi l'order lookup resta guest-first (reference + email); l'account surface è additivo.
- [ ] **Email sending.** `django-anymail` + provider (Postmark/Resend/SendGrid) + order confirmation email + bank transfer instructions email + shipment tracking email. Templates per locale.
- [ ] **Stripe Connect per multi-account.** Oggi single-account (una `STRIPE_SECRET_KEY` serve tutto). Multi-merchant con payout automatico richiede Connect + `account_id` per storefront.
- [ ] **Refunds flow UI.** `PaymentIntent.Status.REFUNDED` esiste; dashboard CTA "Rimborsa" → provider-specific refund dispatch (Stripe Refund API).
- [ ] **Dashboard i18n.** Commerce dashboard resta IT-only. Low priority — è uno strumento interno, non customer-facing.
- [ ] **Coupons / promotions.** Schema-compatible. Order ha `tax_total` + `shipping_total` separati; aggiungere `discount_total` + `Coupon` model additivo.
- [ ] **Tax engine reale.** `Order.tax_total` esiste ma è 0. Per VAT reale serve logic giurisdizionale (origin vs destination VAT).
- [ ] **Carrier integration.** `tracking_number` è free text; carrier-specific tracking URL generation via `shipping_method.carrier_code`.
- [ ] **Reviews + wishlists.** Additivi, nessun blocco.
- [ ] **Per-product localization UI.** Oggi `product.translations` si popola via seeder o admin JSON. Un future add è un tab "Traduzioni" nel ProductUpdateView per locale.
- [ ] **Commerce chrome consolidation.** Il `/templates/.../preview/` chrome e `/shop/…/` chrome restano volutamente duplicati (diversi CTA register, diverso scope). Una volta stabilizzato, estraibile in `templates/commerce/skins/<skin>/_chrome.html` condiviso.
- [ ] **Product image CDN.** Oggi Unsplash hot-link + hero_image_url sono campi URL — va bene per demo. Per produzione: `ImageField` + storage S3/Cloudinary + responsive sizes.

---

## 🟢 Phase 3a — Commerce Foundation v1 — ✅ CLOSED (Session 43, 2026-04-14)
Per D-075, `apps/commerce` is now a real engine. Bottega + Luxe have DB-backed catalogs (9+8 products, 16+23 variants, 4+5 collections, 3+4 shipping methods) rendered through two skin template sets at `/shop/<storefront>/…` with a shared `.cx-*` widget CSS surface. Customer flow is operational end-to-end: browse → product detail with variant picker → add to cart (session-keyed, guest-ok) → update qty / remove → checkout (name + email + shipping address + shipping method + note) → order creation (transactional, `select_for_update` stock lock, atomic) → confirmation page (UUID-addressable, echoes address + totals + payment instructions). Seller dashboard lives at `/dashboard/<storefront>/…` gated by `is_staff`: products/variants CRUD, orders list with status filter, order detail with mark-paid + fulfillment state transition + cancel (stock rollback) + tracking capture. Payment is provider-agnostic via `PaymentIntent` + `_dispatch_payment` — v1 ships `stub` (auto-confirm dev) and `offline_bank_transfer` (awaiting_transfer, seller marks paid); Stripe is documented extension point, not implemented. Validation: `check` clean, 47/47 new `smoke_commerce.py`, 363/363 + 45/45 + 194/194 + 57/57 + 76/76 + 80/80 + 52/52 all existing smokes **unchanged — zero regression**. Total 914/914. See SESSION_LOG Session 43.

**Catalog state after Session 43: 9/20 published_live (unchanged), 2/9 of those now ALSO operational storefronts (Bottega + Luxe). The `/templates/…/preview/` marketing surface is untouched.**

**Follow-ups (Phase 3b candidates, none blocking):**
- [ ] **Real Stripe integration.** Add `_handle_stripe` to `services.py`, a `/shop/<slug>/stripe/webhook/` endpoint, and switch `Storefront.PaymentProvider.STRIPE` to implemented. The PaymentIntent abstraction already has the right shape; this is a ~200 LOC file-scope addition.
- [ ] **i18n for /shop/ pages.** The Bottega + Luxe live preview pages already ship 5 locales. Commerce templates are IT-only in v1. Wire `resolve_locale` + locale-keyed content (storefront + shipping method + collection titles translatable) + locale switcher in commerce chrome. Keep page slugs IT for URL canonicity per D-073.
- [ ] **Customer account pages.** Login-gated order history at `/shop/<slug>/account/` listing past orders by user. Requires wiring the existing `accounts` app into the commerce flow. Guest checkout stays primary path.
- [ ] **Per-storefront seller scoping.** Today any `is_staff` user reaches any `/dashboard/<slug>/`. Add a `Seller` model linking users to specific storefronts and gate `SellerRequiredMixin` on membership. Multi-vendor stays out of scope; this is about role-scoping for the marketplace admin.
- [ ] **Dashboard i18n for sellers.** Low priority; the dashboard is a tool, not a customer surface.
- [ ] **Carrier integrations.** Today tracking number is free text. A future hook would be `shipping_method.carrier_code` + carrier-specific tracking URL generation.
- [ ] **Commerce chrome consolidation.** The `/templates/.../preview/` and `/shop/…/` chromes are deliberately duplicated at schema-v1 (different nav targets, different CTA registers, i18n switcher only on preview). Once commerce gets i18n, consolidate the shared partial into `templates/commerce/skins/<skin>/_chrome.html`.
- [ ] **Refunds flow.** `PaymentIntent.Status.REFUNDED` exists but no UI wiring. When an order is cancelled after payment, the seller dashboard would show a "process refund" action → provider-specific refund dispatch.
- [ ] **Coupons / promotions.** Schema-compatible future addition. Order has `tax_total` + `shipping_total` already separated; adding `discount_total` + a `Coupon` model is additive.
- [ ] **Reviews + wishlists.** Additive.
- [ ] **Tax engine.** `Order.tax_total` exists but always 0 in v1. Real VAT calculation requires jurisdictional logic; start with a per-storefront fixed-rate VAT on configurable.

---

## 🟢 Phase 2g3.5 — eCommerce Live Rollout — ✅ CLOSED (Session 41, 2026-04-14)
Per D-073, `bottega-shop-artigianale` and `luxe-fashion-store` are flipped from `tier=draft` to `tier=published_live` premium with full multipage live skins (6 page routes each: home + shop|collection + product + about + journal|lookbook + contact), 5 locales fin da subito (it/en/fr/es/ar) with real RTL for Arabic, sharp D-054 differentiation enforced. Three concrete deliverables: (a) two new skin folders (~5,500 LOC HTML) at `templates/live_templates/ecommerce/{artisan-workshop,fashion-editorial}/` with full RTL CSS + Amiri/Noto-Kufi conditional load + `:focus-visible` rings + mobile breakpoints; (b) two IT content registries (~1,210 LOC) + 8 locale trees authored by 8 parallel sub-agents (~6,400 LOC total) — Bottega artisan-warm Toscana voice (Aesop EN, Astier FR `tu`, peninsular `tú` ES, Brownbook AR cultural-publishing) vs Luxe maison editoriale voice (Gentlewoman EN formal, Hermès FR `vous`, Vogue España `usted`, Vogue Arabia luxury-maison AR); (c) new `smoke_ecommerce_rollout.py` (194 checks) codifying the D-054 cross-leak gate (15 Bottega-only + 16 Luxe-only tokens × 5 locales × 12 pages × 2 directions = 0/120 cross-tenant leaks). Validation: `check` clean, 363/363 full route sweep (was 282, +81 from 2 templates × 5 locales × ~7 pages avg), 45/45 form sweep (was 35, +10 from 2 ecommerce contatti × 5 locales), 57/57 hardening sweep (was 45, +12 from 2 new multilingual templates), 194/194 ecommerce rollout sweep, 76/76 chiara + 80/80 pixel + 52/52 gusto regressions clean. **Total 867/867 checks passed.** See SESSION_LOG Session 41.

**Catalog state after Session 41: 9/20 published_live ship in 5 locales** across 5 categories (medical/restaurant/business/portfolio/ecommerce). 11/20 still draft.

**Follow-ups (not blocking):**
- [ ] **Lift the legacy ecommerce preview compositions** (`templates/preview_compositions/ecommerce/{artisan-workshop,fashion-editorial}.html` carry 10+/12+ Bottega/Luxe literals from Session 15). Cosmetic-only — used for the static listing PNG. Low priority because the live preview is the primary surface; do this when adding a 3rd ecommerce sibling.
- [ ] **Regenerate ecommerce listing PNGs** via `python manage.py generate_previews --force --slug bottega-shop-artigianale --slug luxe-fashion-store` once a real device is available to test the static thumbnails. The legacy compositions still render correctly with the existing `imagery_key="ecommerce"` pool — the regeneration is to make sure the listing card matches the live preview tone.
- [ ] **Inline-styled grid mobile audit** on the ecommerce skins — ad-hoc inline `style="display:grid; grid-template-columns: 1.4fr 1fr"` patterns may have the same min-width: auto trap that bit Chiara in Session 37. Audit at 390×844 with the smoke `smoke_ecommerce_rollout.py` extension. ~30min.
- [ ] **Phase 2g3.5b candidate** — if a 3rd ecommerce template ever lands (e.g. specialty-foods, vintage-archive), reuse one of the two existing skin folders. Only split a new archetype if the new sibling is semantically as far from BOTH existing siblings as Bottega is from Luxe (D-050/D-051 default).

---

## 🟢 Phase 2g3.3b — Pragma + Elevate i18n Completion Pass — ✅ CLOSED (Session 40, 2026-04-14)
Per D-072, `pragma-corporate-suite` and `elevate-startup-landing` are brought from IT-only to fully multilingual (5 locales + real RTL for Arabic) in a single session. Both keep their sharply distinct voices (Pragma institutional B2B advisory · Elevate SaaS growth-tech). Three concrete deliverables: (a) 8 new content trees authored by 8 parallel sub-agents (Pragma EN/FR/ES/AR ~846/880/852/848 LOC + Elevate EN/FR/ES/AR ~821/838/812/813 LOC), 0 key diffs per locale; (b) 9 D-047 leaks lifted from skin HTML (6 Pragma + 3 Elevate including the `Più scelto` CSS-pseudo-element badge converted to HTML); (c) RTL CSS blocks added to both business archetype `_base.html` files (Amiri+Noto-Kufi for Pragma serif identity, Noto-Naskh+Noto-Kufi for Elevate geometric SaaS identity), `:focus-visible` rings, page-level grid flips guarded by `{% if is_rtl %}`. Validation: `check` clean, 282/282 full route sweep (was 226, +56 new locale routes), 35/35 form sweep (was 27, +8 new locale form routes), 45/45 hardening sweep (pragma + elevate moved IT_ONLY → MULTILINGUAL), 0/40 cross-tenant leak sweep, D-054 differentiation preserved across all locales. Regression: chiara/pixel/gusto smokes 76/80/52 all clean. See SESSION_LOG Session 40.

**Catalog state after Session 40: 7/7 published_live ship in 5 locales. Multilingual coverage on the public catalog is closed.**

**Follow-ups (not blocking):**
- [ ] **Inline-styled grid mobile audit on Pragma + Elevate** — same `<div class="head" style="display:grid; grid-template-columns: 0.45fr 1fr">` pattern that Session 37 fixed on Chiara likely affects Pragma's `.cs-pillars/.cs-cases-* .head` and Elevate's `.sl-comparison/.sl-stack` grids. Not a blocking issue (no smoke failure), but a polish pass for a mobile-coherent feel. Budget ~30min audit + ~30min fix.
- [ ] **Translate Pragma + Elevate `form_submit_note` consent paragraph already done by sub-agents** — verify the GDPR / RGPD / LOPDGDD references render correctly across locales. (Quick spot-check; sub-agents reported caveat that Pragma `form_consent` was rephrased for natural English flow.)
- [ ] **Phase 2g3.5 — eCommerce live rollout (Luxe + Bottega).** Next public-catalog promotion gate. DNA + preview compositions already authored in Session 15. Need: per-template content registries (extract to dedicated files per Session 32 pattern), per-archetype skin folders under `templates/live_templates/ecommerce/<archetype>/`, premium imagery audit (Session 31 image-coherence rules apply). Per Session 32 recipe — this is a green path now.

---

## 🟢 Phase 2N — Chiara Perfection Pass — ✅ CLOSED (Session 37, 2026-04-13)
Per D-070, `chiara-portfolio-creativo` is brought to gold-standard product quality on a single template. Three concrete deliverables: (a) full 5-locale rollout (it/en/fr/es/ar) with 4 new hand-authored content trees (~3850 LOC total) authored by parallel sub-agents in native editorial-design voice per locale, structural parity verified (0 missing/extra keys per locale); (b) 5 editorial-designer-coherent images replace the generic laptop/coding stock photos that were the user's flagged complaint — book-spine stack for Adelphi, warm museum interior for Querini, type-ideation tablet for Triennale, fountain-pen-on-manuscript for Velluti monograph, woman-with-editorial-book for founder portrait; (c) skin HTML literal lift × 9 sites + mobile breakpoint fix (overflow 124px → -15px) + new `html[dir="rtl"]` CSS block with Amiri + Noto Kufi Arabic font load + a11y `:focus-visible` rings on all CTAs. Validation: `check` clean, 198/198 full route sweep (was 170, +28 chiara × 4 new locales), 27/27 form sweep, 45/45 hardening sweep (chiara migrated IT_ONLY → MULTILINGUAL), 76/76 new chiara perfection sweep. See SESSION_LOG Session 37.

**Catalog state after Session 37:** 4/7 published_live ship in 5 locales (cardio · derm · gusto · chiara); 3/7 remain IT-only (pragma · elevate · pixel).

**Follow-ups (not blocking):**
- [ ] **Phase 2i.2c — Pixel locale rollout.** Same Session 37 recipe (4 parallel content agents + 1 image curator + RTL CSS + smoke). Pixel's cinematic-photographer skin needs its own `html[dir="rtl"]` CSS block (not shared with editorial-designer-grid since the skins are independent). Budget ~3h end-to-end based on Session 37 timing.
- [ ] **Phase 2i.2d — Pragma + Elevate locale rollout.** Two business templates can ship together since they share business-archetype CHROME_I18N keys. Each gets its own RTL CSS block (corporate-suite + startup-saas-landing skins are independent).
- [ ] **Inline-styled grid mobile audit on Pragma + Elevate** — the same `<div class="head" style="display:grid; grid-template-columns: 0.45fr 1fr">` pattern likely affects them too. The Session 37 mobile fix (`!important` overrides on `head[style]` selectors) is portable. ~30min audit + fix.
- [ ] **Replace the Triennale tablet image + the founder portrait** with stronger picks if a tenant-grade Velluti shoot becomes available. The Session 37 curator flagged both as "best available given constraints" but not gold. Future image-coherence pass.
- [ ] **Ledger card mobile clip** — at 390×844 the wordmark "Chiara Velluti Studio" gets visually clipped behind the status pill in the nav at extreme small viewports. Cosmetic chrome stacking issue, not horizontal overflow. Candidate fix: stack nav vertically below the status at 480px breakpoint.

## 🟢 Phase 2M — Live i18n & Media Coherence Hardening — ✅ CLOSED (Session 36, 2026-04-13)
Per D-069, the motion/media pass from Session 35 (D-068) is hardened on two coherence gates: (a) the language switcher on the 4 IT-only templates (Pragma / Elevate / Chiara / Pixel) is suppressed via a template-aware `locale_switcher_entries()` + `get_available_locales()` so the 5-pill chrome no longer lies about non-existent translations; (b) the 3 `lm-video` blocks shipped with a Big Buck Bunny placeholder MP4 + codec-theatre meta (`4K`, `1080p · 24 fps`, `Play · 3:12`) are fixed per-archetype — Gusto signature_video REMOVED, Pixel reel REMOVED, Elevate product_video CONVERTED to an honest demo-invitation card with dual CTA to `/demo/` + `/prodotto/`. Orphan `live-media.css`/`js` links + `--lm-video-*` tokens pruned from every base that no longer consumes them (Cardio/Derm/Gusto/Chiara/Pixel). Pragma + Elevate marquees kept (real institutional/SaaS wordmarks). Validation: `check` clean, 170/170 full route sweep, 27/27 form sweep, 45/45 hardening checks (new `smoke_i18n_media_hardening.py`). See SESSION_LOG Session 36.

**Follow-ups (not blocking):**
- [ ] **Phase 2i.2b — IT-only template locale rollout.** When the content authoring schedule has room, commission EN/FR/ES/AR content trees for Pragma / Elevate / Chiara / Pixel, one per session, per D-063 budget (~3h each). When `TEMPLATE_CONTENT[slug]` gains a 2nd locale key, the switcher re-appears automatically — no chrome work needed (the `{% if locale_switcher %}` guards are already installed from Session 36).
- [ ] **Phase 2i.4 candidate — Gusto content-depth disparity closure.** The `signature_video` block was IT-only; its removal closes the disparity. But the next time a new block is added to Gusto (e.g. producers showcase expansion, wine program deep-dive) it MUST be authored in all 5 locales at the same commit, not IT-only with locale guards. Document as a soft rule in BRAND_SYSTEM_GUIDELINES when it gets the next pass.
- [ ] **Live-video primitive return.** `live-media.css` + `live-media.js` remain in the repo as a latent capability. When a tenant has a real signed MP4 (Gusto kitchen footage, Pixel Carso reel) AND on-brand metadata (no codec cues), the block can return — re-add the content key, re-include the HTML section, re-link the primitive in the skin base. Zero infrastructure work.

## 🟢 Phase 2L — Live Motion / Media / Typography Pass — ✅ CLOSED (Session 35, 2026-04-13)
Per D-068, the 7 `tier=published_live` templates now ship with: 2 new shared primitives (`static/css/live-media.css` + `static/js/live-media.js`) for video block + logo marquee; counter prefix + Italian thousand-separator extension in `live-motion.js`; per-skin tokens for video/marquee/mono accent in every `_base.html`; new sections — `.cs-kpi-band` counters + Pragma sectors+trust marquee, Elevate 9 counters + product video + integrations marquee + JetBrains Mono ship-log, Gusto signature ambient video, Chiara featured-projects lightbox grid + mono indices, Pixel cinematic reel + 6-cell EXIF, Cardio/Derm typography refined (italic-axis + tabular-nums + line-height). Validation: `check` clean, 170/170 full route sweep, 27/27 form sweep. See SESSION_LOG Session 35.

**Follow-ups (not blocking):**
- [ ] Replace the 3 placeholder video src URLs (Big Buck Bunny on Google's public bucket) with real brand video URLs when production tenants come online. Each block annotated with a `NOTE` comment in its content registry.
- [ ] Phase 2i.4 candidate — translate the new content keys (`product_video`, `signature_video`, `featured_works`, `reel`) for EN/FR/ES/AR on the 3 multilingual templates (cardio/derm/gusto) that ship with i18n. Templates render gracefully without these keys (the `{% if %}` guards skip the section) so this is a polish pass, not a bug fix. Pixel + Chiara + Pragma + Elevate are IT-only at promotion (Phase 2g3.3/2g3.4 closure).
- [ ] Extend `EDITOR_SCHEMA_BLUEPRINT.md` with: (a) `font_mono` per-skin design token (currently 3 skins use it — formalize as an editor-surfaced choice), (b) `lm-video` block primitive shape (poster + src + caption + play_label + optional 4-6 cell EXIF/meta strip), (c) `lm-logo-marquee` content shape (list of strings), (d) per-template counter contract (every metric span gets `data-lm="counter"` with optional `data-lm-to` override).
- [ ] D-061 medical motion exclusion clarification — the original D-061 doc said "no counters" for clinical motion. Cardio's facts strip already had counters from earlier sessions; this Session 35 preserved them. The clarification: "no counters" applies to spectacular-feel CountUp animations on splash hero strips, not to small clinical credibility numerics on a facts strip. Documented in D-068. A future doc-pass could amend D-061 directly to remove the ambiguity.

## 🟢 Phase 2k — Premium Forms Polish — ✅ CLOSED (Session 33, 2026-04-13)
Per D-066, the 5 `tier=published_live` templates now ship with a reusable `.lf-*` forms primitives layer (`static/css/live-forms.css` + `static/js/live-forms.js`), per-skin token overrides across 4 archetypes (specialist / fine-dining / corporate-suite / startup-saas-landing), accessible custom listbox, file upload UI where page copy justifies it, sectioned form markup, reassurance submit bar, mobile 1-column collapse at 880px. Validation: `check` clean, 27/27 form checks, 149/149 full route sweep. See SESSION_LOG Session 33.

**Follow-ups (not blocking):**
- [ ] Phase 2i.3 enhancement-copy translation pass — cardio/derm/gusto `form_sections` + `upload_field` + per-field `helper` into EN/FR/ES/AR (native voice). `form_submit_note` already translated. Templates render gracefully without these keys so this is a polish pass, not a bug fix.
- [ ] Specialist legacy mobile chrome collapse — `.sp-nav .right` 3-col grid + `.sp-foot` 4-col grid overflow at 390×844. Pre-existing, not introduced by Session 33, candidate for a separate mobile pass.
- [ ] Extend `EDITOR_SCHEMA_BLUEPRINT.md` with the new form primitives (`.lf-select`, `.lf-upload`, section grouping, submit-bar) and their per-field metadata shape. The content registry now carries `form_sections`, `upload_field`, per-field `helper`, `form_consent`, `form_submit_note` — these are the editable shapes the future editor will surface.

## 🌐 Phase 2i — i18n/RTL Pilot + Rollout

### 2i.1 — i18n/RTL Pilot Cardio (it/en/fr/es/ar) — ✅ CLOSED (Session 23, 2026-04-11)
Per D-059, cardio-studio-specialistico now ships as the first genuinely multilingual `tier=published_live` template with real RTL for Arabic. Zero Django gettext machinery introduced. The pilot architecture is the reusable recipe for Phase 2i.2 rollout to the other `tier=published_live` templates.

- [x] Created `apps/catalog/template_i18n.py` — `SUPPORTED_LOCALES`, `DEFAULT_LOCALE`, `RTL_LOCALES`, `LOCALE_LABELS`, `LOCALE_BADGES`, `CHROME_I18N` (5 locales × ~30 keys), helpers `resolve_locale/is_rtl/html_dir/get_chrome/pick_localized/locale_switcher_entries`.
- [x] Created `apps/catalog/template_content_cardio_i18n.py` — 4 full hand-authored content trees (CARDIO_CONTENT_EN/FR/ES/AR), premium native-voice quality per locale, no machine translation.
- [x] Refactored `apps/catalog/template_content.py` — top-level `TEMPLATE_CONTENT` is now `{slug: {locale: tree}}`. Cardio has 5 locales; derm and gusto wrapped under `{"it": ..._IT}`. Helpers made locale-aware with IT fallback via `template_i18n.pick_localized`.
- [x] Updated `LiveTemplateView` — reads `?lang=xx`, threads locale through content helpers, exposes `locale/chrome/html_dir/is_rtl/locale_switcher/default_locale` context vars.
- [x] Rewrote `templates/live_templates/medical/specialist/_base.html` — dynamic `<html lang dir>`, conditional Noto Naskh Arabic + Noto Kufi Arabic font loading, marketplace-bar language switcher pill strip, chrome strings wired, every nav/footer URL preserves `?lang` when non-IT, RTL-scoped CSS block (`html[dir="rtl"] ...` — font-size bump, letter-spacing flatten, eyebrow accent-bar flip, gold-btn arrow flip, nav grid justify-content swap).
- [x] Chrome strings + URL locale preservation on all specialist pages: `home.html` (+ `home_all_doctors`/`home_publications` link labels), `about.html`, `services.html`, `contact.html` (6 form labels + submit), `appointment.html` (alt link), `blog_list.html` (read-full + min), `blog_detail.html` (crumbs sep, min, back link). `team.html` needed zero edits (already clean from Session 14 lift).
- [x] Validation: `python manage.py check` clean. 51/51 smoke test green (9 cardio routes × 5 locales = 45, plus 6 regression/negative checks for derm-EN fallback, gusto-AR fallback, unknown locale fallback, and draft 404).
- [x] Live browser walk at 1440×900 Playwright: IT/EN/FR/ES/AR home rendered, AR contact page verified, FR services rendered, ES blog detail rendered. AR confirmed `dir=rtl`, Noto Naskh loaded, body 17px, layout flips visually correct.
- [x] Mobile sanity at 390×844: pilot introduces zero new horizontal overflow (IT 835px, AR 882px — delta is the intentional 17px body bump).
- [x] D-059 formalized in DECISIONS.md.
- [x] memory/i18n_pilot_cardio_session23.md + MEMORY.md index entry.

**Decision:** I18N/RTL PILOT CARDIO APPROVATO.

### 2i.2 — Extend pilot to the other `published_live` templates (open)
Per D-059, the other two `tier=published_live` templates pick up multilingual publishing by opting into the pilot architecture. Order (cheapest first):

- [x] **Dermatologia-elite-roma** — ✅ **CLOSED (Session 24, cherry-picked into baseline in Session 25)**. 4 hand-authored content trees (EN/FR/ES/AR) in `template_content_dermatologia_i18n.py`. Zero new HTML or CSS. 5/5 derm locale routes 200. Same specialist skin RTL CSS already in place from cardio pilot.
- [x] **Gusto-fine-dining** — ✅ **CLOSED (Session 29, 2026-04-13)**. 4 hand-authored content trees (EN/FR/ES/AR) in `template_content_gusto_i18n.py`, restaurant-hospitality native voice per locale. New `html[dir="rtl"] ...` CSS block authored in `fine-dining/_base.html` with core + page-level split (page-level inside `{% if is_rtl %}` so LTR skips CSS entirely). CHROME_I18N extended with 9 restaurant-generic keys (mp_other_restaurant, foot_restaurant, foot_concierge, foot_services, fd_wine_pairing, fd_email_label, fd_phone_label, blog_read_article — reusable by future restaurant archetypes). 52/52 routes green (35 gusto + 10 cardio regression + 5 derm regression + 2 negative). Motion + interactions preserved. D-063 formalized.

**Exit criteria for Phase 2i.2 — all met (Session 29 closure):**
- [x] Every `tier=published_live` template has a `{locale: tree}` content block for all 5 locales (it/en/fr/es/ar) — cardio + derm + gusto all done.
- [x] Every archetype `_base.html` has a working `html[dir="rtl"]` CSS block verified by a 1440×900 browser walk on `?lang=ar` — specialist (cardio/derm) done Session 23, fine-dining (gusto) done Session 29.
- [x] Route sweep: 5 locales × all routes per template all 200 — 52/52 green in Session 29 smoke test.
- [x] No new horizontal overflow compared to the IT baseline on any template at 390×844 — Gusto AR 673px vs IT 701px, AR actually tighter.
- [x] `CHROME_I18N` is the single source of truth for all chrome strings across archetypes — restaurant-generic extensions sit alongside medical keys in one flat dict per locale.
- [x] Session log + memory entry per template — Sessions 23 / 24 / 29 all documented.

**Phase 2i.2 CLOSED.** All 3 `tier=published_live` templates ship multilingual with RTL.

### 2i.3 — Marketplace chrome i18n (deferred, Phase 4)
The marketplace surface (homepage, listing, detail, category, search) remains Italian-only through Phase 2i. When Phase 4 lifts this, the migration is:
- [ ] Audit every `templates/catalog/*.html` + `templates/pages/*.html` + `templates/includes/*.html` for hardcoded IT strings.
- [ ] Decide between (a) extending `CHROME_I18N` with a `marketplace` namespace and reading it via a context processor, or (b) finally moving to Django `{% trans %}` + `.po` files for the marketplace-only surface. Either is compatible with the Phase 2i pilot because every live-template string is already locale-namespaced.
- [ ] Decide on URL scheme — query param `?lang=` (current pilot shape) vs prefix `/<lang>/` (future). Prefix would let marketing link directly to a localized homepage.
- [ ] Out of scope until Phase 2g3 is closed and the roadmap re-unblocks.

---

### 2g2x.13 — Premium Component Depth & Editor Schema Blueprint — ✅ CLOSED (Session 30, 2026-04-13)
Per D-064, the 3 `tier=published_live` templates receive differentiated premium sections (cardio: journey/trust/location · derm: tabs/compare/feed · gusto: producers/private/wine) and a concrete Editor Schema Blueprint (`EDITOR_SCHEMA_BLUEPRINT.md`) is authored for the future customer editor. New interaction primitives (tabs, compare slider, anchor-nav) extend `live-interactions.css/js`. All 5 locales on all 3 templates for the new sections, native voice. 85/85 routes green, zero cross-contamination, 16/16 differentiation checks. D-064. See SESSION_LOG Session 30.

**Phase 3 prerequisite restated:** the Editor Schema Blueprint is binding for when the editor worktree opens. Do NOT start editor implementation until Phase 2g3.7 closes (D-049 roadmap freeze still in effect).

### 2g2x.12 — Ultra Premium Live Pass — ✅ CLOSED (Session 28, 2026-04-12)
Per D-062, the 3 `tier=published_live` templates receive a comprehensive ultra-premium enrichment pass with new interactive components (accordion/lightbox/sticky CTA), premium content sections, and visual richness differentiated per template. `static/css/live-interactions.css` + `static/js/live-interactions.js` introduced. See SESSION_LOG Session 28.

### 2g2x.11 — Medical Motion Opt-In — ✅ CLOSED (Session 27, 2026-04-12)
Specialist archetype (`cardio-studio-specialistico` + `dermatologia-elite-roma`) adopts the live motion language with a clinical profile. 4 patterns: reveal-on-scroll (10px rise), stagger (80–100ms), CTA hover refinement, image attention lift (filter, not zoom). 9 files modified, zero Gusto changes. 34/34 routes green. D-061. See SESSION_LOG Session 27.

### 2g2x.10 — Catalog Stabilization & Fix Consolidation — ✅ CLOSED (Session 25, 2026-04-12)
All approved fixes from Sessions 17–24 consolidated into branch `phase-catalog-stabilization-v1`. Cherry-picked derm i18n (Session 24). Generated preview PNGs for all 3 published_live templates. 32/32 routes green, zero regressions, zero cross-contamination. The "scattered worktree" problem is resolved. See SESSION_LOG Session 25.

---

## 🛑 BLOCKING — Phase 2g2x (Catalog Hardening Wave, Session 16 audit)

**The roadmap is paused.** Per D-049, no feature work (auth / checkout / editor / projects / commerce / dashboard / new categories / new templates / new archetypes) starts until this wave closes. See SESSION_LOG.md Session 16 for the audit + MEMORY.md → catalog_differentiation_audit.md for the condensed verdict.

### 2g2x.1 — Lift the 5 non-DNA categories (CRITICO) — identity crash fix
Each of these 5 legacy compositions hardcodes literal brand strings from ONE tenant, making the second sibling render the wrong brand's copy on its card. Choose per category: (a) split into 2 archetypes with distinct compositions (medical/restaurant pattern), OR (b) lift the existing legacy composition to read from a new DNA content block and add DNA entries for both tenants (cheaper). Option (a) is preferred for categories where the two tenants are semantically far apart; option (b) is acceptable when they're close.

- [ ] **Agency** — `templates/preview_compositions/agency.html` + pools `agency` (used by vertex + aura). 2 archetypes suggested: `bold-grid` (Vertex) + `editorial-quiet` (Aura). Leaks to lift: "Independent design & tech studio · Milano", "Lumen — Renewable energy", "Vega Mobile App", "Atelier Norma", "Helios Bank", "Cinetic", "Polar Studios", "34 case studies · 2018 — 2026", "200+ progetti"
- [x] **Business** — ✅ **CLOSED in Session 17 (2026-04-11)**. Option A (DNA split) selected per D-050. Two archetypes ship: `corporate-suite` (Pragma) + `startup-saas-landing` (Elevate). Two new D-047-compliant compositions under `templates/preview_compositions/business/`. Two disjoint imagery pools (`business-corporate`, `business-startup`). Zero cross-tenant leaks confirmed by bidirectional leak sweep. Legacy `business.html` + legacy `business` pool preserved per D-036 but architecturally unused. Pragma and Elevate now read as two clearly distinct products at card size.
- [ ] **Lawyer** — `templates/preview_compositions/lawyer.html` + pool `lawyer` (used by lex + juris). 2 archetypes suggested: `classic-gold` (Lex) + `modern-transparent` (Juris) — already outlined in CATEGORY_ROADMAP.md. Leaks: "Studio legale dal 1962 · Roma · Milano", "+39 06 4567 2300" phone, "60 anni di esperienza", M. Bianchi CEO review, 4 practice-area cards (Diritto societario/famiglia/lavoro/penale) as literal copy
- [ ] **Real-estate** — `templates/preview_compositions/real-estate.html` + pool `real-estate` (used by casa + villa). 2 archetypes suggested: `mass-market` (Casa) + `ultra-luxury-cinematic` (Villa) — already outlined. Leaks: "Oltre 600 immobili selezionati · Lombardia & Piemonte", price box "€500K — €1.2M" (mass-market, wrong for Villa), "+39 02 8765 4321", specific Milano Brera listing
- [x] **Portfolio** — ✅ **CLOSED in Session 18 (2026-04-11)** + **hardened in Session 19 triage fix (2026-04-11)**. Option A (DNA split) selected per D-051. Two archetypes ship: `editorial-designer-grid` (Chiara) + `cinematic-photographer` (Pixel). Two new D-047-compliant compositions under `templates/preview_compositions/portfolio/`. Two disjoint imagery pools (`portfolio-designer`, `portfolio-photographer`). Zero cross-tenant leaks confirmed by bidirectional leak sweep (52 tokens). Zero legacy literals in listing HTML. Legacy `portfolio.html` + legacy `portfolio` pool preserved per D-036 but architecturally unused. Chiara now reads unambiguously as a designer studio (typographic hero, project ledger, clients ribbon) and Pixel now reads unambiguously as a photographer (fullbleed cinematic hero, EXIF credit bar, filmstrip gallery). **Session 19** closed a real hero-overflow bug in Chiara (h1 82→62 px + margin trim + `overflow: hidden` safety net + headline copy trimmed from 57→47 chars per D-052) after triage confirmed the pre-commit verdict was NON COMMITTARE ANCORA. Post-fix browser walk at 1440×900: listing, Chiara detail and Pixel detail all clean, zero overlap, differentiation actually strengthened via the `'…, una X alla volta.'` syntactic parallel between the two siblings' headlines.

### 2g2x.2 — Sibling imagery pool split (CRITICO)
For each of the 5 non-DNA categories, break the single 6-URL pool into two sibling-distinct pools per the Session 10 recipe (hand-check each URL via Read; zero URL overlap between siblings; page-level macro tone should differ where possible). If 2g2x.1 chose option (a) [separate archetypes], this is almost free; if option (b) [shared composition, DNA fields], this is the only way to get visual differentiation.

- [ ] `agency-bold` vs `agency-editorial` — or equivalent per the 2g2x.1 split
- [x] `business-corporate` vs `business-startup` — ✅ **CLOSED in Session 17**. Both pools hand-authored, zero URL overlap, zero overlap with legacy `business` pool.
- [ ] `lawyer-classic` vs `lawyer-modern`
- [ ] `real-estate-mass` vs `real-estate-luxury`
- [x] `portfolio-designer` vs `portfolio-photographer` — ✅ **CLOSED in Session 18**. Both pools hand-authored, zero URL overlap with each other, zero overlap with legacy `portfolio` pool.
- [ ] **Bonus:** fix the `medical-specialist` pool — currently shares 5/6 URLs with `lawyer` pool so Cardio/Derm hero is a lawyer portrait. Replace with genuine specialist-medical photos (white-coat specialists in clinical settings)
- [ ] **Bonus:** `medical-family` pool is 100% URL-overlap with base `medical` pool (just reordered). Replace with genuine pediatric/family-practice photos

### 2g2x.3 — D-047 lift on latent single-tenant archetype files (MEDIO)
These files were authored before D-047 was formalized (or in Session 15 which predated the D-047-applies-to-preview-comps insight) and will detonate on archetype reuse. Fix now, not when reuse is attempted.

- [ ] `templates/preview_compositions/ecommerce/fashion-editorial.html` — 12+ Luxe literals: "Milano · Parigi · Tokyo", "Issue 12 · Primavera '26", "Styling · Carla Sozzani", "Cover · La Muse en Velours", "Un'unica collezione, tessuta tra Como e Prato, fotografata al Grand Hôtel Villa d'Este", "Drop mensili — solo per chi è in lista d'attesa", "Accedi al lookbook", "Direzione creativa · Giulia Maison", "Rack Atelier / Bomber Siena / Pelletteria / Sessione Vogue" product strip, "€ 2.480 / € 1.290 / € 860 / € 1.940" prices, "Nuovo / Capsula / Atelier / Archivio" tags, "Donna/Uomo/Accessori/Archivio/Atelier" nav links
- [ ] `templates/preview_compositions/ecommerce/artisan-workshop.html` — 10+ Bottega literals: "Firenze · dal 1968 · fatto a mano", "Pelletteria / Ceramica / Tessitura / Su misura" nav links, "Cesto · 2 pezzi", "Cuoio conciato al vegetale a Santa Croce sull'Arno, ceramiche tornite a Montelupo, stoffe tessute a Prato", "Visita la bottega", "WhatsApp: 055 234 11 90", "La nostra regola: tre mani, un oggetto", "12 botteghe / 100% italiani / Mai sopra 50 / In 48 ore", "Scritto a mano, impacchettato in bottega", "Le ultime arrivate in bottega"
- [ ] `templates/preview_compositions/restaurant/trattoria-warm.html` — "Trastevere · dal 1987 · cucina romana di famiglia" hardcoded
- [ ] `templates/preview_compositions/restaurant/street-modern.html` — spot-audit for Brace-specific literals (not fully swept in the audit)
- [ ] `templates/preview_compositions/medical/clinic.html` — spot-audit for salute-studio-medico literals
- [ ] `templates/preview_compositions/medical/family.html` — "Dr.ssa Rambaldi" hardcoded + any other leaks
- [ ] `templates/preview_compositions/medical/wellness.html` — spot-audit for Benessere literals
- [ ] `templates/live_templates/restaurant/fine-dining/*.html` (8 files, 5 leak Gusto strings) — **this is the already-planned Phase 2g.3** — Fioravanti / Brera / Otto atti / Barolo / Selosse / Bresse / Michelin. Recipe = Session 14 lift. **DO THIS BEFORE any second fine-dining template ships.**

### 2g2x.4 — Template completeness decision (CRITICO for product positioning)
17 of 20 templates are preview-PNG-only. Only cardio, derm, gusto have inner pages. Decide:
- [ ] **Option A:** Mark preview-only templates as `draft` in the DB and filter them out of listing until their content registry + skin folder are authored. Commit: "a premium marketplace ships complete products only"
- [ ] **Option B:** Keep them `published` but add a "Anteprima statica" badge on the card + disable the "Apri anteprima completa" CTA. Commit: "we sell product tiers — single-page and multipage"
- [ ] Whichever option is chosen: document as D-050 in DECISIONS.md and update TEMPLATE_REGISTRY.json with the per-template tier

### 2g2x.5 — Stale-PNG structural fix (MEDIO, recurrent DX bug)
Sessions 8, 10, 12, 15, **19** all independently hit the DNA-mtime-vs-PNG-mtime timing trap. Session 19 added a fresh concrete repro: two `generate_previews --only <slug> --force` runs produced three orphan `_<hash>.png` files because `FileSystemStorage.get_available_name()` suffixes the filename when the target exists, and the `--force` path in `generate_previews.py:211-216` deletes the DB row but not the file. Pick one and ship:
- [ ] **Option A (cheapest):** `generate_previews` reads DNA dict + composition path + imagery pool → hashes them → stores as `dna_signature` on TemplateAsset → skips regen when hash matches, force-regens on mismatch. Auto `--force`, no operator recipe needed
- [ ] **Option B (middleweight):** `generate_previews --audit` prints any template whose preview file mtime is older than DNA file mtime or composition file mtime. Run in CI; fail the build on mismatch
- [ ] **Option C (proper fix):** introduce a `TemplateAsset.source_fingerprint` column + migration; compute from DNA + composition + imagery pool SHA; treat stale rows as invalid and auto-regen

### 2g2x.7 — Detail-page "Anteprima Live" legacy placeholder
**✅ RESOLVED by D-056 + 2g2x.8 (Session 21, 2026-04-11).** The legacy `{% else %} <a href="#">Anteprima Live</a>` branch in `template_detail.html` and the `has_live_preview` context variable in `TemplateDetailView` have been deleted. The three-option punch list is no longer needed — tier gating per D-055 makes the branch architecturally unreachable (no draft template ever reaches the detail page publicly), so the "hide entirely" option was applied by construction. The "Apri anteprima completa" CTA is now unconditional on every detail page, because every detail page now hosts a `published_live` template.

### 2g2x.8 — Tier migration: demote preview-only templates to `draft` — ✅ CLOSED (Session 21, 2026-04-11)
Per D-055, introduced the two-tier model (`published_live` / `draft`) and hid every template that does not satisfy the full D-053 Live Preview Law gate. This is the one-way door that turns the marketplace floor premium from day one.

- [x] Added `tier` field to `WebTemplate` (`WebTemplate.Tier` TextChoices — `published_live` / `draft`, default `draft`, db_index=True). Migration `catalog/0002_webtemplate_tier.py`.
- [x] Added new management command `sync_template_tiers` that reads `TEMPLATE_REGISTRY.json` (source of truth) and applies tier to matching rows. Wired into `seed_templates` so a single seed run produces correct tiers.
- [x] Centralized the tier gate in `apps/catalog/selectors.py` via `_public_tier_filter(include_drafts)`. All public selectors (`get_published_templates`, `get_featured_templates`, `get_template_detail`, `get_related_templates`, `get_listing_templates`, `get_templates_by_category`, `get_active_categories_with_counts`) now accept a single `include_drafts` kwarg and delegate to the gate.
- [x] `TemplateListView` / `TemplateDetailView` / `CategoryListView` / `LiveTemplateView` thread the gate through `_staff_preview_mode(request)`. Staff authenticated via `is_staff` + `?preview=1` can reach draft surfaces; all other traffic is filtered.
- [x] Deleted the `{% else %} <a href="#">Anteprima Live</a>` branch in `templates/catalog/template_detail.html` + the `has_live_preview` context variable in `TemplateDetailView` per D-056. The "Apri anteprima completa" CTA is now unconditional. The placeholder cart CTA is now a disabled `<button>` (one more ghost link retired).
- [x] Added premium empty-state partial `templates/catalog/_empty_catalog.html` with three modes (`category_soon`, `search_no_match`, `catalog_empty`). Wired into `template_list.html` and `pages/home.html`. Category cards with 0 live siblings now render an "In arrivo" pill (`_category_card.html` + new tokens in `components.css`).
- [x] `TEMPLATE_REGISTRY.json` already carries the `tier` annotation on every row (shipped in Session 20 as v0.8.0) — no data change needed, just wired to the DB.
- [x] Marked D-045 as superseded by D-055 + D-056 in `DECISIONS.md`.
- [x] Featured pool backfill: `get_featured_templates` now prefers `featured=True` templates but backfills from the live pool when the featured+live intersection is thin (prevents the homepage from collapsing to 1 card during the transition).

**Exit criteria for 2g2x.8 — all met (31/31 smoke checks passed):**
- [x] `/` homepage shows 3 featured templates, all `published_live`, all with working "Apri anteprima completa" CTA
- [x] `/templates/` listing shows 3 templates total (cardio / dermatologia-elite-roma / gusto-fine-dining)
- [x] `/templates/<category>/` for categories whose only siblings are `draft` shows the `category_soon` empty state ("Selezione in preparazione" / "in arrivo") — not an empty grid
- [x] `python manage.py check` clean
- [x] No `href="#"` ghost live preview CTA remains in `templates/catalog/` (verified by grep)
- [x] Staff preview via `?preview=1` works end-to-end for draft templates (verified by smoke test)
- [x] Draft template detail URLs return 404 publicly; draft `/preview/` routes return 404 publicly

### 2g2x.9 — Motion Pilot Gusto (interaction-quality floor) — ✅ CLOSED (Session 22, 2026-04-11)
Per D-058, introduced a reusable live-template motion language on `gusto-fine-dining` as the interaction-quality floor for every `tier=published_live` template. Two dependency-free static files + an HTML attribute contract. Strictly opt-in per skin (one `<link>` + one `<script>` in the archetype's `_base.html`).

- [x] Created `static/css/live-motion.css` — reusable motion tokens + primitives (`--lm-dur-*`, `--lm-ease`, `--lm-rise*`, reveal / reveal-lg / reveal-soft / stagger / image-frame / reduced-motion collapse + `body.lm-reduced` short-circuit).
- [x] Created `static/js/live-motion.js` — reusable dependency-free runtime (IntersectionObserver reveals, per-child stagger delay assignment, counter animation with suffix preservation, marquee duplication helper, reduced-motion detection).
- [x] Wired into `templates/live_templates/restaurant/fine-dining/_base.html` via `{% static %}` link + script + nav underline sweep + gold CTA arrow shift + letter-spacing hover + mp-bar hover + footer link transitions.
- [x] Applied motion attributes across all 7 fine-dining pages (home / menu / about / gallery / reservations / blog_list / blog_detail) — 18 reveal targets on home, 3 stagger parents, 3 counters, 6 image-zoom frames, 8 menu course stagger, 5 timeline rows stagger, 4 values stagger, 6 gallery tile stagger, 4 process-step stagger, compact blog list stagger.
- [x] Refactored `.fd-hero .plate`, `.fd-chef .portrait`, `.fd-concierge .portrait`, `.fd-lead-post .img`, and `.fd-gallery .img` to the wrapper + inner-bg layer pattern so hover zoom has an `overflow: hidden` container (no CLS).
- [x] No-JS fallback: hidden CSS state gated on `body.lm-ready`; without the class (JS off), every `[data-lm]` element renders at `opacity: 1 / transform: none`. Verified in browser.
- [x] Reduced-motion fallback: `@media (prefers-reduced-motion: reduce)` + `body.lm-reduced` double guard. Verified in browser via manual `body.lm-reduced` assignment.
- [x] Validation: 8/8 Gusto routes 200, live browser walk at 1440×900 confirms reveals / staggers / counter / hovers all wired, mobile sanity at 390×844 confirms motion pilot introduces zero new horizontal overflow (existing 660px overflow is pre-existing Gusto desktop-first layout, out of scope).
- [x] D-047 leak sweep clean — zero new literals introduced (existing Gusto literal in `blog_detail.html:108` is a Phase 2g.3 leak already tracked).
- [x] D-058 formalized in DECISIONS.md.
- [x] SESSION_LOG Session 22 entry.

**Follow-up opt-ins (low priority, not blocking Phase 2g3):**
- [ ] Cardio live skin (`templates/live_templates/medical/specialist/*`) adopts the motion pilot — same two-file opt-in + attribute tagging pass. Should be a short session because chrome is already D-047 clean.
- [ ] Dermatologia (same specialist skin folder) benefits for free via the cardio pass — no separate work needed.
- [ ] BRAND_SYSTEM_GUIDELINES.md gets a new "Motion Language" pointer section citing D-058.

### 2g2x.6 — Exit criteria for the hardening wave
The wave closes when ALL of the following are green:
- [ ] All 5 non-DNA categories have either 2 archetypes each OR a D-047-compliant shared composition with per-tenant DNA content blocks
- [ ] No two siblings in the same category share more than 2 imagery URLs (zero would be better but Session 10 shows 2 non-hero URLs can overlap if the heroes are fully distinct)
- [ ] A leak sweep on every per-archetype file (preview comps + live skins) returns zero literal brand strings
- [ ] Every published template either has inner-page content OR is demoted to `draft` / flagged as preview-only
- [ ] `python manage.py generate_previews --force` on a clean cache produces canonical PNGs that visually differentiate every sibling at card size
- [ ] A fresh Chromium walk through every category listing page confirms "no two siblings read as the same product" at 200×120 card size
- [ ] Tier migration 2g2x.8 is complete, listing/detail/homepage all filter `tier='published_live'`, and the `href="#"` ghost CTA is deleted per D-056

---

## 🔴 Phase 2g3 — Live Preview Rollout (policy session, D-053 / D-054 / D-055)

**Per D-053, every template published to the public catalog must be a real navigable multi-page website.** Today only 3 of 20 templates (cardio / dermatologia-elite-roma / gusto-fine-dining) meet that bar. Phase 2g3 is the wave that brings every remaining template up to `published_live`, one category burst at a time, using the Session 11/14 architecture (content registry + per-archetype skin folder + single dispatcher view + D-047 chrome-authoring contract).

**Gate to enter Phase 2g3:** Phase 2g2x (all subphases, including 2g2x.8 tier migration) is closed. Phase 2g3 does not start otherwise.

### 2g3.0 — Per-template acceptance checklist (applies to every item below)
A template is eligible to flip from `draft` to `published_live` only when ALL of the following are green. Authors must run this checklist on every single template before flipping the flag — no batch lifts, no "we'll polish the inner pages after launch" exceptions.

- [ ] **DNA entry** complete in `apps/catalog/template_dna.py` with all 10 D-054 dimensions explicitly declared (hero image direction, dominant imagery pool, silhouette, section order, primary CTA phrase + pattern, block rhythm / density, macro tone, imagery direction, font pairing, inner-page notes)
- [ ] **Content registry block** complete in `apps/catalog/template_content.py` covering every page kind in the category baseline (see 2g3 baseline table below)
- [ ] **Skin folder** exists at `templates/live_templates/<category>/<archetype>/` — reuse if another sibling already built it, otherwise author under D-047 from line one
- [ ] **Route sweep** all green — Django test-client returns 200 on marketplace detail + `live_template_home` + every `live_template_page` + at least one `live_template_post` where blog exists
- [ ] **Leak sweep bidirectional** — grep the rendered HTML of this template against every other template using the same archetype; zero cross-tenant brand names, city names, quotes, proper names, image URLs
- [ ] **Visual walk** at 1440×900 via Chromium: home + every inner page. Brand chrome (palette / fonts / imagery direction / macro tone) consistent across pages. No page looks like a different template
- [ ] **Differentiation sibling test** — on the category's listing page at 200×120 card size, this template reads as a visually distinct product from every other `published_live` sibling. If it fails, either the DNA has under-specified ≥4 of the D-054 dimensions or the skin needs a differentiation polish pass
- [ ] **Preview PNG regenerated** via `python manage.py generate_previews --only <slug>` (orphan cleanup per Phase 2g2x.5 if triggered) and the canonical filename is `<slug>-preview.png`
- [ ] **Tier flipped** in `seed_templates.py` and re-seeded (`python manage.py seed_templates`), or the tier update applied via a data migration if the seed command has already run
- [ ] **Motion pilot adopted** — per D-058, the skin's `_base.html` links `static/css/live-motion.css` + scripts `static/js/live-motion.js`, and the home page at minimum has reveal + stagger + (where applicable) counter + image-hover patterns applied. Hover micro-interactions on CTAs / nav / image frames are encouraged but graduated: the minimum is reveal + stagger on the home page, and counters where numeric facts exist
- [ ] **Session log entry** documents the flip + validation results + any authoring insights for the next template in the wave

### 2g3.1 — Restaurant category completion (2 templates remaining: Sapore, Brace)
The `trattoria-warm` and `street-modern` archetypes already exist at the preview composition level (and have D-047 latent leaks pending lift per Phase 2g2x.3). Phase 2g3.1 authors the corresponding live skin folders and content blocks. Smallest lift because the DNA + preview composition already exist.

- [ ] Phase 2g2x.3 leak lifts on `templates/preview_compositions/restaurant/trattoria-warm.html` and `street-modern.html` land first (blocker)
- [ ] Phase 2g.3 leak lift on `templates/live_templates/restaurant/fine-dining/*.html` lands first (blocker — affects gusto, not sapore, but the contract must be enforced before adding a second template)
- [ ] Create `templates/live_templates/restaurant/trattoria-warm/` skin folder with `_base.html` + `home.html` + `filosofia.html` (about) + `menu.html` + `galleria.html` + `prenota.html` (contact + reservations merged)
- [ ] Create `templates/live_templates/restaurant/street-modern/` skin folder with `_base.html` + `home.html` + `menu.html` + `ordina.html` (delivery-first) + `dove-siamo.html` (locations) + `contatti.html`
- [ ] Content registry blocks for `sapore-trattoria-pizzeria` (fictional trattoria brand) and `brace-street-food-lab`
- [ ] Run 2g3.0 checklist on both; flip both to `published_live`

### 2g3.2 — Medical category completion (3 templates remaining: Salute, Benessere, Famiglia)
The `clinic`, `wellness`, and `family` archetypes exist at the preview composition level and need new live skin folders. Medium lift — three new skins, but the `specialist` skin (cardio + derm) has already proven the D-047 authoring recipe.

- [ ] Phase 2g2x.3 leak lifts on `templates/preview_compositions/medical/clinic.html`, `family.html`, `wellness.html` land first (blockers)
- [ ] Create `templates/live_templates/medical/clinic/` skin folder — institutional multi-specialty chrome. Pages: home, studio (about), reparti (departments), medici (team), prenota-visita (booking widget), contatti, pubblicazioni + pubblicazioni/<post>
- [ ] Create `templates/live_templates/medical/wellness/` skin folder — holistic/spa chrome. Pages: home, filosofia, percorsi (services), team, prenota (calendar spot), contatti, diario + diario/<post>
- [ ] Create `templates/live_templates/medical/family/` skin folder — pediatric/family chrome. Pages: home, studio, visite (services), equipe (team), orari-e-contatti (contact + hours), lettere-ai-genitori (blog list) + lettere-ai-genitori/<post>
- [ ] Content registry blocks for `salute-studio-medico`, `benessere-centro-olistico`, `famiglia-pediatria`
- [ ] Run 2g3.0 checklist on all three; flip each to `published_live`

### 2g3.3 — Business category completion (2 templates: Pragma, Elevate) — **CLOSED in Session 32**
Both templates already had D-047-compliant preview compositions from Session 17 (corporate-suite + startup-saas-landing). Session 32 authored both live skin folders + content registry blocks from scratch under D-047 in a single session.

- [x] Created `templates/live_templates/business/corporate-suite/` skin folder — institutional advisory chrome. Pages: home, chi-siamo (about + team + history + values + 3 offices coords), competenze (6 advisory practices + 4-step process), case-studies (list + 3 case-study posts on `case_study_detail`), contatti (9-field private call form + 3 office sidebar)
- [x] Created `templates/live_templates/business/startup-saas-landing/` skin folder — conversion-first SaaS chrome. Pages: home, prodotto (6 modules + 12 integrations + 8-row stack), prezzi (3-tier pricing + 4-row comparison + 6-item FAQ accordion), demo (8-field demo lead form + async loom block + trust strip), contatti (4 channels + 3 founder cards with direct emails + async-first office)
- [x] Content registry blocks for `pragma-corporate-suite` (`apps/catalog/template_content_pragma.py`, ~590 lines) and `elevate-startup-landing` (`apps/catalog/template_content_elevate.py`, ~620 lines)
- [x] Added `mp_other_business` chrome key to `CHROME_I18N` in all 5 locales (forward-compat for future business i18n)
- [x] Ran 2g3.0 checklist on both; flipped both to `published_live`. Validation: 54/54 routes green, D-047 leak sweep clean (0 cross-tenant literals), D-054 10/10 differentiated, preview PNGs regenerated, business category card now shows `2 live template(s)`. **D-065 documents the closure.**

### 2g3.4 — Portfolio category completion (2 templates: Chiara, Pixel) — **CLOSED in Session 34**
Both templates had D-047-compliant preview compositions from Session 18 (editorial-designer-grid + cinematic-photographer) and the Session 19 triage fix for Chiara was already applied. Session 34 authored both live skin folders + content registry blocks from scratch under D-047 in a single session.

- [x] Created `templates/live_templates/portfolio/editorial-designer-grid/` skin folder — typographic designer chrome. Pages: home, studio (about), lavoro (project_list + project_detail under `/lavoro/<slug>/`), processo (process), contatti (contact)
- [x] Created `templates/live_templates/portfolio/cinematic-photographer/` skin folder — cinematic photographer chrome. Pages: home, serie (series_list + series_detail under `/serie/<slug>/`), biografia (about), pubblicazioni (publications), contatti (contact)
- [x] Content registry blocks for `chiara-portfolio-creativo` (`apps/catalog/template_content_chiara.py`, ~880 LOC) and `pixel-portfolio-fotografico` (`apps/catalog/template_content_pixel.py`, ~720 LOC)
- [x] Added `mp_other_portfolio` chrome key to `CHROME_I18N` in all 5 locales (forward-compat for future portfolio i18n)
- [x] Ran 2g3.0 checklist on both; flipped both to `published_live`. Validation: 170/170 routes green (was 149 before, +21 new portfolio routes), D-047 leak sweep clean (2 latent leaks lifted in same session — `kit_footer_rows` + `print_meta`), D-054 10/10 differentiated, preview PNGs regenerated, portfolio category card now shows 2 live template(s). **D-067 documents the closure.**

### 2g3.5 — Ecommerce category completion (2 templates: Bottega, Luxe)
Both have D-047-compliant preview compositions from Session 15 (artisan-workshop + fashion-editorial) but Phase 2g2x.3 already flagged both preview comps for latent literal leaks (12+ Luxe literals in fashion-editorial.html, 10+ Bottega literals in artisan-workshop.html). **Phase 2g2x.3 lifts are a hard blocker** for 2g3.5.

- [ ] Phase 2g2x.3 leak lifts on `templates/preview_compositions/ecommerce/fashion-editorial.html` and `artisan-workshop.html` land first (hard blocker)
- [ ] Create `templates/live_templates/ecommerce/artisan-workshop/` skin folder. Pages: home, bottega (about + story), catalogo (product list), catalogo/<prodotto>, su-misura (custom orders form), contatti
- [ ] Create `templates/live_templates/ecommerce/fashion-editorial/` skin folder. Pages: home, lookbook (editorial gallery), collezione (product list), collezione/<prodotto>, atelier (about), appuntamento (private viewing form)
- [ ] Content registry blocks for `bottega-shop-artigianale` and `luxe-fashion-store`
- [ ] Run 2g3.0 checklist on both; flip both to `published_live`

### 2g3.6 — Agency / Lawyer / Real-estate — requires Phase 2g2x.1 closure first
These three categories are still CRITICO identity-crash cases in Phase 2g2x.1 and do NOT have DNA archetypes yet. Phase 2g3.6 cannot start until 2g2x.1 is fully closed for all three. Recommended order (lift the cleanest first per AGENT_HANDOFF Session 19 guidance): real-estate → lawyer → agency.

- [ ] Real-estate: Phase 2g2x.1 ships 2 archetypes (`mass-market` for Casa + `ultra-luxury-cinematic` for Villa). Then 2g3.6 authors both skin folders: pages = home, ricerca (search/listings), proprieta/<slug> (property detail), chi-siamo (about), contatti. Villa's detail page gets an "appuntamento privato" concierge CTA instead of a public request form.
- [ ] Lawyer: Phase 2g2x.1 ships 2 archetypes (`classic-gold` for Lex + `modern-transparent` for Juris). Then 2g3.6 authors both skin folders: pages = home, studio (about), aree (practice areas), avvocati (team), contatti. Lex gets editorial-serif chrome with case-heritage pages. Juris gets modern-clean chrome with transparency/pricing pages.
- [ ] Agency: Phase 2g2x.1 ships 2 archetypes (`bold-grid` for Vertex + `editorial-quiet` for Aura). Then 2g3.6 authors both skin folders: pages = home, studio (about), servizi, lavori (case studies list), lavori/<case-study>, contatti. Each category's 2g3.0 checklist applies.

### 2g3.7 — Exit criteria for Phase 2g3
Phase 2g3 closes — and the roadmap unblocks for Phase 3 (auth / checkout / editor / projects / commerce) — when ALL of the following are green:
- [ ] All 20 templates are tier `published_live`
- [ ] Every template's 2g3.0 checklist was run and documented (session log entry per template OR per category burst)
- [ ] `python manage.py check` clean, `python manage.py test` (if used) green
- [ ] A fresh Chromium walk through every category listing + every detail + at least the home + one inner page per template returns zero visual regressions
- [ ] A cross-category leak sweep on the full set of per-archetype skin folders returns zero cross-tenant literal brand strings
- [ ] The homepage featured grid shows at least 8 distinct templates from at least 4 categories (minimum "credible marketplace" floor)
- [ ] No `href="#"` CTA exists anywhere in the catalog
- [ ] `TEMPLATE_REGISTRY.json`, `CATEGORY_ROADMAP.md`, `MEMORY.md`, `SESSION_LOG.md`, and `AGENT_HANDOFF.md` all reflect the final state

**Exit gate for Phase 3 (unblock auth / checkout / editor / ...):** Phase 2g3.7 fully green. No exceptions, no partial unblocking. Either the marketplace's 20 templates are all real products or the product features built on top inherit the credibility gap.

---

## Immediate — Phase 1 Foundation

### Backend-Core Session
1. [x] Create `apps/` directory and all seven app packages with `__init__.py`
2. [x] Create custom User model in `accounts` (extend AbstractUser) — BEFORE any migrate
3. [x] Update `settings.py`: add all apps to INSTALLED_APPS, set AUTH_USER_MODEL, configure static/media
4. [x] Create `core` base models: TimestampedModel, SlugModel
5. [x] Create `catalog` models: Category, WebTemplate, TemplateAsset, TemplateBrand, Tag
6. [x] Register all models in Django admin with useful list displays and filters
7. [x] Create `requirements.txt` pinning key dependencies
8. [x] Run `makemigrations` and `migrate` — verify clean migration
9. [x] Create initial data fixtures or management command for MVP categories
10. [x] Set up basic URL routing skeleton across all apps

### Premium-UI Session
1. [x] Create `templates/base.html` master template with Bootstrap 5 CDN/local
2. [x] Design and implement the CSS design system (colors, typography, spacing variables)
3. [x] Create premium navigation component (header + mobile menu)
4. [x] Create premium footer component
5. [x] Build homepage skeleton with hero section, featured categories, featured templates
6. [x] Build category listing page template
7. [x] Build template detail page template
8. [x] Build premium card component for template listings
9. [x] Set up `static/` directory structure
10. [x] Ensure RTL-ready class structure from the start

## Completed — Phase 1.5 (Integration & Polish)
- [x] Merge backend-core and premium-ui branches to master
- [x] Fix Bootstrap CSS/JS loading (SRI hash mismatch — updated to 5.3.8)
- [x] Fix navbar duplication (caused by Bootstrap CSS not loading)
- [x] Category grid 4+4 balanced layout
- [x] Typography/spacing polish for Bootstrap reboot compatibility
- [x] Wire homepage category cards to actual Category queryset from backend views
- [x] Wire featured templates section to WebTemplate.objects.filter(featured=True)
- [x] Create catalog views: CategoryListView, TemplateListView, TemplateDetailView
- [x] Connect template_card partial to real WebTemplate model data
- [x] Add category card href to actual category URL ({% url 'catalog:template_list_by_category' category.slug %})
- [x] Create seed_templates management command (16 templates, 16 brands, all 8 categories)
- [x] Wire navbar Template/Categorie links to real URLs
- [x] Dynamic category dropdown in template listing filter bar
- [x] Fix breadcrumbs in detail and listing pages
- [x] Wire related templates section in detail page

## Completed — Phase 2a (Catalog Enhancements)
- [x] Generate SVG preview images for all 16 templates (branded mockups via generate_previews command)
- [x] Add search functionality (query param `?q=` + icontains across name/description/brand)
- [x] Add sort functionality (recent, price asc/desc, name A-Z)
- [x] Pagination for template listing (paginate_by=12, full page nav with param preservation)
- [x] Asset prefetching to eliminate N+1 queries on listing pages
- [x] Empty state with search feedback and clear button

## Completed — Phase 2c (Real Preview Assets, 2026-04-10)
- [x] Curated stock imagery library with cache-first downloader (8 categories × 6 photos)
- [x] HTML preview compositions per category (8 Django templates with brand-palette injection)
- [x] Playwright + Chromium screenshot pipeline (1600×900 @ 2× DPI → PNG)
- [x] Three-phase generate_previews command (avoids ORM/asyncio conflict)
- [x] All 16 templates re-rendered with real-imagery PNGs
- [x] Live verification: homepage featured grid, listing page, detail page

## Completed — Phase 2e (Template DNA System Phase 1, 2026-04-10)
- [x] Per-template DNA registry in `apps/catalog/template_dna.py`
- [x] DNA vocabulary documented (archetype, hero/navbar/footer style, density, tone, conversion, ...)
- [x] `at` templatetag filter for safe imagery indexing in loops
- [x] `_resolve_composition()` in generate_previews — DNA-aware, falls back to legacy per-category
- [x] Per-archetype `imagery_key` so sibling templates pull from different photo pools
- [x] Pilot category Medical: 4 archetypes (clinic / family / specialist / wellness)
- [x] 4 distinct medical compositions under `templates/preview_compositions/medical/`
- [x] 2 new medical seed templates (Famiglia — Studio Pediatrico, Cardio — Studio Specialistico)
- [x] All 4 medical previews regenerated and visually verified

## Completed — Phase 2e.1 (Medical Pilot Fix, 2026-04-10, Session 8)
- [x] Audited all 4 medical templates end-to-end (DNA → composition path → asset row → file on disk)
- [x] Confirmed registry is correct and no duplicate/stale TemplateAsset rows in DB
- [x] Identified stale `benessere-centro-olistico-preview.png` (rendered against legacy `medical.html` before its DNA/wellness composition existed)
- [x] Cleaned the stale asset row + orphan file, regenerated benessere with the wellness archetype, verified canonical filename
- [x] Visually verified all 4 medical cards in `/templates/medical/` are now clearly distinct

## Completed — Phase 2f.1 (Restaurant Pilot, 2026-04-10, Session 9)
- [x] Vocabulary additions in `apps/catalog/template_dna.py` (3 archetypes, 3 hero/navbar/footer/card/button styles, 3 tones, 3 conversion patterns, 3 imagery directions)
- [x] DNA entries for `gusto-fine-dining`, `sapore-trattoria-pizzeria`, `brace-street-food-lab` (NEW)
- [x] New seed template `Brace — Street Food Lab` in `seed_templates.py` (palette black/yellow/red, Big Shoulders Display + Inter)
- [x] 3 new imagery pools (`restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) in `preview_imagery.py` — Session 9 claimed "fully distinct" but Session 10 found 5/6 URL overlap between fine and trattoria
- [x] 3 archetype compositions: `restaurant/fine-dining.html`, `restaurant/trattoria-warm.html`, `restaurant/street-modern.html`
- [x] All 3 restaurant previews regenerated, canonical filenames clean (no orphan suffixes), visually verified at 1600×900
- [x] Visually verified `/templates/restaurant/` listing — Session 10 found Gusto and Sapore were too similar; fixed in Session 10
- [x] Verified detail pages for all 3 restaurants
- [x] Regression check on `/templates/medical/` — 4 medical archetypes still intact

## Completed — Phase 2g.0.1 (Template Polish Fixes, 2026-04-10, Session 12)
- [x] Audited `template.assets.first` usage in card + detail templates — identified as fragile (default-ordered fetch, not filtered by asset_type)
- [x] Added `WebTemplate.preview_asset` property — prefetch-aware, explicitly filters `asset_type=preview`
- [x] Added `_preview_only_prefetch()` in selectors to limit prefetch to preview rows only
- [x] Swapped `_template_card.html` + `template_detail.html` gallery to use `template.preview_asset`
- [x] Found stale gusto + sapore PNG files on disk (legacy `restaurant.html` render, not DNA archetype composition)
- [x] Deleted stale TemplateAsset rows + files, re-ran `generate_previews --only <slug>` for both
- [x] Verified regenerated PNGs: Gusto now fully-dark editorial Playfair, Sapore now fully-bright cream polaroid scrapbook
- [x] Audited live-template archetype skins for over-narrow max-widths
- [x] Widened medical/specialist wide sections 1100/1200→1400 (sp-lead, sp-section, sp-history, sp-method-inner, sp-values, sp-posts, sp-treatments, sp-contact, sp-process, sp-form-band-inner, sp-manifesto, sp-hero)
- [x] Widened restaurant/fine-dining wide sections 1100/1280→1440 (fd-lead, fd-section, fd-manifesto, fd-courses, fd-chef-inner, fd-timeline, fd-method-inner, fd-values, fd-courses-full, fd-wine-inner, fd-rooms, fd-gallery, fd-process, fd-concierge-inner, fd-hours, fd-private-inner, fd-form-band, fd-posts)
- [x] Fixed the home manifesto double-constraint (`max-width: 36ch; margin: 0 auto` on inner p) — widened to 68ch left-aligned so the drop-cap anchors the frame's left edge
- [x] Preserved intentional narrow editorial reading column: blog_detail pages stay at 760px
- [x] 20 routes verified 200 via Django test client, `python manage.py check` passes

## Completed — Phase 2g (Template Completeness Pilot, 2026-04-10, Session 11)
- [x] Designed scalable inner-page architecture: content registry + per-archetype skin folder + single dispatcher view
- [x] `apps/catalog/template_content.py` — content registry pattern with helpers (`has_live_template`, `get_content`, `get_pages`, `find_page`, `find_post`)
- [x] `LiveTemplateView` in `apps/catalog/views.py` — resolves WebTemplate → DNA → content in `setup()`, dispatches to per-archetype/page-kind template
- [x] Three new URL patterns: `live_template_home`, `live_template_page`, `live_template_post`
- [x] `templates/live_templates/medical/specialist/` skin: standalone `_base.html` + 8 page templates (home, about, services, team, blog_list, blog_detail, contact, appointment)
- [x] `templates/live_templates/restaurant/fine-dining/` skin: standalone `_base.html` + 7 page templates (home, about, menu, gallery, reservations, blog_list, blog_detail)
- [x] **Cardio pilot complete** — 8 inner pages, all in Italian, prestigious editorial chrome, realistic Roma Parioli cardiology copy
- [x] **Gusto pilot complete** — 7 inner pages, all in Italian, dark editorial fine-dining chrome, realistic Brera Michelin restaurant copy
- [x] Marketplace detail page conditional CTA: "Apri anteprima completa" when content is registered, legacy CTA otherwise (strictly additive)
- [x] 17 routes verified via Django test client (2 marketplace detail + 15 inner preview pages, all 200)
- [x] Bug fix: hoisted DNA/content resolution from `get_template_names` to `setup` (TemplateView builds context before names)

## Completed — Phase 2f.1.1 (Restaurant Pilot Fix Pass, 2026-04-10, Session 10)
- [x] Audited all 3 restaurant templates end-to-end (DNA → composition path → asset row → file on disk → imagery pool URLs)
- [x] Identified root cause: (a) `restaurant-fine` and `restaurant-trattoria` pools shared 5 of 6 URLs (only hero differed); (b) both compositions used cream top + dark bottom band, creating identical thumbnails despite different layouts
- [x] Replaced `restaurant-fine` pool with 6 hand-checked DARK plated dish URLs (zero overlap with trattoria, zero overlap with legacy `restaurant`)
- [x] Replaced `restaurant-trattoria` pool with 6 hand-checked BRIGHT sunny rustic URLs (zero overlap with fine, zero overlap with legacy `restaurant`)
- [x] Each candidate URL downloaded and visually inspected via Read tool — caught one clothing-store image and replaced
- [x] Rewrote `restaurant/fine-dining.html` as fully DARK charcoal page (no cream paper, no contrast band, full-bleed plate hero, italic Playfair throughout)
- [x] Rewrote `restaurant/trattoria-warm.html` as fully BRIGHT cream page (no dark chalkboard, no dark hours band, two polaroid scrapbook + cream washi-tape recipe card)
- [x] Cleaned restaurant-fine and restaurant-trattoria imagery caches; clean delete + regenerate-without-force for both slugs
- [x] Visually verified at canonical PNG URLs (with `?cb=` cache-bust): Gusto fully dark editorial, Sapore fully bright cream scrapbook, Brace yellow brutalist — three opposite ends of the visual spectrum
- [x] Verified `/templates/restaurant/` listing thumbnails after JS cache-bust (browser was serving cached old PNGs)
- [x] Verified `/templates/restaurant/gusto-fine-dining/` and `/templates/restaurant/sapore-trattoria-pizzeria/` detail pages
- [x] Regression check on `/templates/medical/` — unaffected

## Completed — Phase 2g.1 (Archetype Reuse Validation, 2026-04-10, Session 13)
- [x] **Added `dermatologia-elite-roma` under the `specialist` archetype** (Option A from Session 12 handoff). One row in `seed_templates.py`, one DNA entry in `template_dna.py`, one content block in `template_content.py`. **Zero new HTML files.**
- [x] All 9 routes return 200 via Django test client (marketplace detail + 7 inner preview pages + 1 post detail)
- [x] Regression check on Cardio (8 routes) + Gusto (7 routes) + catalog pages (4 routes): 19 total, all 200
- [x] Content assertion sweep on the home page confirms the new brand/palette/font/doctors/press list all render correctly
- [x] Cardio-leak audit across all 8 pages cataloged every hardcoded cardio-specific string in the specialist chrome — see SESSION_LOG.md Session 13 "Findings" table and DECISIONS.md D-046

**Validation result:** structurally the abstraction is reusable (zero new HTML files, all routes 200). Editorially the chrome leaks cardio-specific copy in 17 distinct sites across 7 files, appearing on every dermatology page. The follow-up work is Phase 2g.2 below.

## Completed — Phase 2g.2 (Copy-Abstraction Lift on Specialist Chrome, 2026-04-11, Session 14)
Moved every cardio-specific literal out of `templates/live_templates/medical/specialist/*.html` into the content registry. Mechanical lift — zero new HTML files, zero new archetypes, zero architectural changes.

### Site-wide chrome fixes (_base.html)
- [x] Moved `OMCeO Roma 12 / 4408` out of `_base.html` into `site.license`
- [x] Moved `Sabato · solo reperibilità` / `Domenica · chiuso` into `site.hours_footer_rows`

### Home page fixes (home.html)
- [x] Moved the hero-right quote into `home.hero_sidebar_quote`
- [x] Moved the quote attribution into `home.hero_sidebar_author`
- [x] Moved the pulse triple into `home.hero_sidebar_pulse` (list of `(label, value)` tuples)
- [x] Moved the `Direzione clinica` pulse-top label into `home.hero_sidebar_top_label`
- [x] Moved the chief portrait URL out of inline CSS into `home.chief.portrait`
- [x] Moved the signature-visits section heading into `home.signature_visits_heading`
- [x] Moved the section intro fragment into `home.signature_visits_intro` (plain text, no inline link)
- [x] Moved the chief section heading into `home.chief_heading`
- [x] Moved the final CTA heading into `home.cta_heading`
- [x] Moved the CTA primary label into `home.cta_primary_label`
- [x] Moved the CTA secondary label into `home.cta_secondary_label`
- [x] Bonus: added `home.signature_visits_label`, `home.chief_label`, `home.press_label` for full section-label coverage

### About / Studio page fixes (about.html)
- [x] Moved the values section label into `studio.values_label`
- [x] Moved the values section heading into `studio.values_heading`
- [x] Moved the CTA band heading into `studio.cta_heading`
- [x] Moved the CTA primary label into `studio.cta_primary_label`
- [x] Moved the CTA secondary label into `studio.cta_secondary_label`

### Services page fixes (services.html)
- [x] Moved the `Note amministrative` heading into `visite.footnote_heading`
- [x] Moved the CTA heading `Una visita allo Studio Marani è concordata personalmente.` into `visite.cta_heading` — **this was the most visible brand-name leak in the entire chrome**
- [x] Moved the CTA primary label into `visite.cta_primary_label`
- [x] Moved the CTA secondary label into `visite.cta_secondary_label`

### Team page fixes (team.html)
- [x] Moved each doctor's portrait URL out of `nth-child` CSS rules into per-doctor `doctors[i].portrait`. Replaced the three `nth-child` rules with a single per-iteration inline `style="background-image: url('{{ d.portrait }}')"`. **3-doctor cap removed.**
- [x] Moved `Roma · Parioli` out of the portrait signature into `medici.portrait_city` (with per-doctor override via `d.portrait_city|default:`)

### Blog list / detail page fixes
- [x] Moved the lead-post hero image URL out of inline CSS into `pubblicazioni.lead_image`
- [x] Replaced the hardcoded `'pubblicazioni'` slug in URL reverses with a context variable `blog_parent_slug` computed in `LiveTemplateView.get_context_data()` from the page entry where `kind == 'blog_list'`. **D-044's hardcoded-slug constraint is lifted** (see D-048).
- [x] Moved `Studio Marani · Cardiologia clinica` into `pubblicazioni.footer_strap` (with `|default:site.logo_word` fallback)
- [x] Moved the empty-body fallback copy into `pubblicazioni.empty_body_fallback_paragraphs` (list)
- [x] Bonus: breadcrumb + "Tutte le …" footer link now use `{{ page.label }}` / `{{ page.label|lower }}` — no hardcoded "Pubblicazioni"

### Contact page fixes (contact.html)
- [x] Moved form placeholders into `contatti.form_placeholders` (dict: first_name, last_name, email, phone, subject, message)
- [x] Moved `Orari di apertura` / `Come raggiungerci` sidebar headings into `contatti.hours_heading` / `contatti.transport_heading`

### Appointment page fixes (appointment.html)
- [x] Moved the process section label into `richiedi-visita.process_label`
- [x] Moved the process section heading into `richiedi-visita.process_heading`
- [x] Moved the form-band side-note into `richiedi-visita.form_band_side_note` + `form_band_side_note_small`
- [x] **Replaced the entire hand-written `<form>`** — the 8-field, 2-select, 2-full-width `<form>` block is now a single `{% for f in page_data.form_fields %}` loop. `form_fields` was reshaped from `(label, placeholder, type)` tuples into richer dicts: `{label, type, full_width, placeholder OR options}`. The select options are pulled from `f.options` instead of being hand-written.
- [x] Moved the submit button label into `richiedi-visita.submit_label`

### Validation after Phase 2g.2 (Session 14)
- [x] **Leak audit:** Grepped rendered HTML of all 8 dermatologia pages for 26 cardio-specific literals. **Zero leaks.** Session 13's 17 distinct leaks are all gone.
- [x] **Positive sweep on Cardio:** 52 expected hallmark strings still rendered across all 8 pages. No regression.
- [x] **Positive sweep on Dermatologia:** 46 expected dermatology strings all rendered — the new content fields successfully drive every place the chrome reads them.
- [x] **Route sweep:** 25/25 routes green via Django test client (Cardio 9 + Derm 9 + Gusto 7 regression).
- [x] **`python manage.py check`:** clean.
- [x] **Template file grep:** zero hardcoded Unsplash URLs and zero cardio-brand literals remaining in the 9 specialist chrome files.
- [x] **Chrome-authoring contract** formally recorded as **D-047** in DECISIONS.md.
- [x] **`blog_parent_slug` lifecycle** formally recorded as **D-048** in DECISIONS.md.

## Completed — Phase 2g.2.1 (Preview Composition Copy Lift & Ecommerce DNA Pilot, 2026-04-11, Session 15)
- [x] Added `hero_meta`, `credit_left`, `credit_right` fields to Cardio + Dermatologia DNA content blocks
- [x] Lifted cardio literals (`Dr. R. Marani`, `Roma · Parioli`, `SC Cardiologia`) out of `templates/preview_compositions/medical/specialist.html` into DNA field reads — zero literals left
- [x] Regenerated dermatology preview (previously missing — Session 13 explicitly skipped it) — card now shows dermatology brand/palette/specialty, not a grey placeholder
- [x] Regenerated cardio preview to verify the composition change is a no-op for Cardio (it is)
- [x] Redesigned `.mw-page-hero` in `static/css/components.css`: `calc(navbar-height + space-10)` padding-top, 64px navbar clearance, `min-height: 22rem`, vertical-centered flex, dual radial gradient background, wider subhead max-width, clamped responsive h1
- [x] Clean-deleted and regenerated stale gusto + sapore PNGs (Session 12's claimed regen didn't land in this worktree) — Gusto now fully DARK editorial, Sapore now fully CREAM polaroid
- [x] Designed 2 new ecommerce archetypes: `fashion-editorial` (Luxe) and `artisan-workshop` (Bottega)
- [x] Authored `templates/preview_compositions/ecommerce/fashion-editorial.html` — fully DARK charcoal, italic Cormorant Garamond, full-bleed fashion cover, gold editorial tile strip
- [x] Authored `templates/preview_compositions/ecommerce/artisan-workshop.html` — fully CREAM warm, typographic-led (no hero photo), Libre Baskerville + orange italic, stamped info panel, N°-labeled edition cards
- [x] DNA entries for both ecommerce templates (using existing `ecommerce` imagery pool — differentiation comes from macro tone + composition, not imagery)
- [x] Renamed 4 orphan-suffixed files from Session 12 back to canonical names, updated DB rows
- [x] 37-route regression sweep: all 200 (homepage + 5 category pages + 10 detail pages + 7 cardio inner + 7 derm inner + 6 gusto inner + 1 gusto post)
- [x] Re-ran cardio-leak audit on all 7 dermatology pages: zero leaks (Session 14's abstraction still holds after the Session 15 preview-composition lift)
- [x] `python manage.py check` clean

## Next — Phase 2f.2 (Ecommerce DNA Expansion)
Two archetypes now ship in ecommerce (`fashion-editorial`, `artisan-workshop`). Validate reuse the same way the specialist archetype was validated (Session 13):
- [ ] Add a second `fashion-editorial` template (suggested: `velvet-monobrand-milano` — Milan monobrand, different palette, different brand name). Just a seed row + DNA entry. Zero new HTML files. Verify card reads as a different product than Luxe at thumbnail size.
- [ ] Add a second `artisan-workshop` template (suggested: `sartoria-di-quartiere` — Neapolitan tailor, different trade focus). Same recipe — seed + DNA, no HTML. Verify card reads distinctly from Bottega.
- [ ] Run a Session 13-style leak audit on the second templates: grep rendered ecommerce preview PNGs (via looking at the composition output) for `Maison Luxe`, `La Bottega di Martino`, `Firenze`, `Giulia Maison`, `Santa Croce`, `Montelupo`, etc. — anything that leaked from the first template into the composition needs to go into the DNA content block or be made a generic archetype label per D-047.
- [ ] If leaks are found, lift them in one pass exactly like Phase 2g.2 did for specialist.

## Next — Phase 2g.3 (Fine-Dining Copy-Abstraction Lift)
Apply the same Phase 2g.2 recipe to `templates/live_templates/restaurant/fine-dining/` before the next fine-dining template ships.

- [ ] Add a second fine-dining template — suggested: `tartufo-truffle-house` (Piedmont truffle restaurant, autumn season, different chef/brand) — with ONLY a seed row, DNA entry, content block. Zero new HTML files.
- [ ] Run the Session 13-style leak audit: grep the rendered HTML of all 7 fine-dining inner pages for `Fioravanti`, `Osteria Moderna`, `Brera`, `Tarbouriech`, `Vallesi`, `Barolo Cannubi`, `Otto atti`, etc.
- [ ] For each leak found, add a new field under the appropriate block (`site`, `home.*`, `filosofia.*`, `menu.*`, `atmosfera.*`, `diario.*`, `prenota.*`) in both `GUSTO_CONTENT` and the new template's content block
- [ ] Replace the hardcoded `'diario'` URL reverses in `restaurant/fine-dining/blog_list.html` and `blog_detail.html` with `blog_parent_slug` (same fix as Session 14)
- [ ] Replace any hardcoded image URLs with inline `style="background-image: url('{{ ... }}')"` reading from per-item fields
- [ ] Re-run the leak sweep against the new template — should show ZERO Gusto-specific strings
- [ ] Re-run a 17-route regression sweep against Cardio + Gusto + Dermatologia + new template
- [ ] Update DECISIONS.md if any new pattern emerges (e.g. per-menu-course field structure, wine-region labels, etc.)

## Next — Phase 2g.1 (Template Completeness Validation) — [follow-up items still pending]
- [ ] Add a "previous / next page" navigation hint at the bottom of each inner page (cycle through `pages` list)
- [ ] Add per-page meta/OG tags using the page's content block (currently the `_base.html` only emits a static tagline meta-description)
- [ ] Promote `template_content.py` content to a `TemplatePage` model + migration + seed-from-registry command (D-042 deferred this — pilot phase needs to settle first)
- [ ] Wire the editor app to load a live preview page as a customizable surface (Phase 3)
- [ ] Imagery in inline styles (e.g. doctor portraits in `team.html`, plate hero in `home.html`) currently hardcodes Unsplash CDN URLs. Move to a `page_imagery` block in the content registry so each template can pick its own.
- [ ] Build inner pages for the second restaurant DNA archetypes (`trattoria-warm`, `street-modern`) once we know how the abstraction holds for fine-dining
- [ ] Build inner pages for the other 3 medical archetypes (`clinic`, `family`, `wellness`)

## Next — Phase 2f (DNA Rollout to Other Categories)
- [x] ~~**Restaurant pilot**~~ — done in Session 9, fixed in Session 10 (3 templates: fine-dining + trattoria-warm + street-modern, all visibly distinct)
- [ ] **Agency pilot** — design 3 archetypes (`bold-grid`, `editorial-quiet`, `case-study-led`). **Apply Session 10 lessons:** (a) imagery pools must have ZERO URL overlap, hand-check every candidate via Read; (b) each composition must have a different page-level macro tone — never two with the same "X-on-top, Y-on-bottom" silhouette
- [ ] **Lawyer pilot** — design 2 archetypes (`classic-gold`, `modern-transparent`) — already half-way there since Lex and Juris have very different tones
- [ ] **Real-estate pilot** — design 2 archetypes (`mass-market`, `ultra-luxury-cinematic`)
- [ ] Once 4+ categories use DNA, decide whether to delete legacy per-category compositions or keep them as scaffolding for "starter" templates
- [ ] Promote `imagery_key` URLs from "reuse existing" to dedicated photo pools per archetype (medical-family/specialist/wellness still recycle from medical+lawyer+real-estate to stay offline-safe — find proper Unsplash IDs once. Restaurant pools already done in Session 9)
- [ ] Add an admin DNA inspector page (read-only) so non-developers can see which archetype each template uses
- [ ] Validate Unsplash URLs at config-load time (Session 9 hit one HTTP 404 — `photo-1606755962773-d324e6f8e2c2` — that the generator silently fell back from). Quick `--validate-imagery` flag would catch these before a full regeneration run.

## Next — Phase 2d (Preview Polish, still pending)
- [ ] Optimize preview PNGs (Pillow `optimize=True` or oxipng/pngquant) — current ~4 MB/file is heavy
- [ ] Lawyer & villa hero text legibility — bump font weight or pick a heavier serif when palette is dark + Cormorant Garamond
- [ ] Headless font fallback audit — confirm every brand `typography` value resolves to a real Google Font weight that loads in time
- [ ] Add `--no-cache-images` flag to force re-downloads when imagery config changes
- [ ] Add to .gitignore: `media/preview_imagery/` (already user-local cache)
- [ ] **DNA-fallback timing trap safety net** (from Session 8 fix): when a slug newly gains a DNA entry, its old fallback-rendered preview becomes stale silently. Options to consider:
      (a) `generate_previews --audit` flag that prints any template whose preview was rendered before the current DNA file's mtime, or
      (b) automatic `--force` whenever the DNA file or composition path on disk is newer than the preview's TemplateAsset, or
      (c) a `dna_signature` field on TemplateAsset (hash of DNA dict) so the generator knows when to regenerate.
- [ ] **TemplateAsset cleanup on `--force`**: the generator deletes the row but not the file, so Django's storage appends a random suffix on next save. Either delete the file in the same step or use `storage.delete(asset.file.name)` before `existing.delete()`.

## Next — Phase 3 (Interactivity & Accounts)
- [ ] Tags seeding and tag filtering on listing page
- [ ] Template preview system (iframe or server-rendered live demo)
- [ ] Editor app models and basic UI
- [ ] Projects app: save/load customer customizations
- [ ] DRF API endpoints for editor save/load
- [ ] User authentication views (register, login, dashboard) + account templates
- [ ] Commerce templates: cart, checkout, order confirmation
- [ ] RTL bundle switching logic for Arabic (detect lang=ar, swap Bootstrap CSS)
- [ ] Add {% trans %} tags throughout for i18n readiness
- [ ] Wire Prezzi and Chi Siamo navbar links to real pages
- [ ] PostgreSQL full-text search upgrade (replace icontains when in production)
