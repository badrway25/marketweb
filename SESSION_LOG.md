# Session Log

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
