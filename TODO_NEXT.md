# TODO Next

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
- [x] 3 new imagery pools (`restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) in `preview_imagery.py` with fully-distinct URL sets
- [x] 3 archetype compositions: `restaurant/fine-dining.html`, `restaurant/trattoria-warm.html`, `restaurant/street-modern.html`
- [x] All 3 restaurant previews regenerated, canonical filenames clean (no orphan suffixes), visually verified at 1600×900
- [x] Visually verified `/templates/restaurant/` listing — 3 visibly distinct cards
- [x] Verified detail pages for all 3 restaurants
- [x] Regression check on `/templates/medical/` — 4 medical archetypes still intact

## Next — Phase 2f (DNA Rollout to Other Categories)
- [x] ~~**Restaurant pilot**~~ — done (Session 9 — fine-dining + trattoria-warm + street-modern, 3 templates)
- [ ] **Agency pilot** — design 3 archetypes (`bold-grid`, `editorial-quiet`, `case-study-led`)
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
