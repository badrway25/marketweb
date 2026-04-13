# TODO Next

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

### 2g3.4 — Portfolio category completion (2 templates: Chiara, Pixel)
Both templates already have D-047-compliant preview compositions from Session 18 (editorial-designer-grid + cinematic-photographer) and the Session 19 triage fix for Chiara is already applied. Medium lift — two new skin folders.

- [ ] Create `templates/live_templates/portfolio/editorial-designer-grid/` skin folder — typographic designer chrome. Pages: home, studio (about), lavoro (project grid), lavoro/<project>, contatti, riflessioni (blog list) + riflessioni/<post>
- [ ] Create `templates/live_templates/portfolio/cinematic-photographer/` skin folder — cinematic photographer chrome. Pages: home, serie (series index), serie/<series>, biografia, contatti
- [ ] Content registry blocks for `chiara-portfolio-creativo` and `pixel-portfolio-fotografico`
- [ ] Run 2g3.0 checklist on both; flip both to `published_live`

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
