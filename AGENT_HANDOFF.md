# Agent Handoff

Last updated: 2026-04-09 — after Catalog Enhancements Phase 1 (Session 5)

## Current State

**Catalog enhancements complete.** Preview images, search, sort, and pagination all implemented and verified. Branch: `catalog-enhancements` worktree (not yet merged to master).

**Session 5 completed:** SVG preview images for all 16 templates, search across name/description/brand, sort by recent/price/name, pagination at 12/page, asset prefetching, empty state UX.

**UI status:** All premium UI preserved — no CSS or component structure changes. Filter bar now functional with form-based search and sort. Pagination shows page numbers with Previous/Next navigation.

## What's Working

| Page                          | URL                                        | Status  |
|-------------------------------|-------------------------------------------|---------|
| Homepage                      | `/`                                        | Dynamic, with preview images |
| Template listing (all)        | `/templates/`                              | Search, sort, paginated |
| Template listing (filtered)   | `/templates/<category_slug>/`              | Search, sort, paginated |
| Template listing (search)     | `/templates/?q=studio&sort=price_asc`      | Working |
| Template detail               | `/templates/<category_slug>/<slug>/`       | Gallery shows SVG preview |
| Category listing              | `/templates/categories/`                   | Dynamic |
| Admin                         | `/admin/`                                  | Working |

## Database State

- **8 categories** — Agency, Business, Ristorante, Medico, Avvocato, Immobiliare, Portfolio, eCommerce
- **16 templates** — 2 per category, all status=published, 6 marked featured
- **16 brands** — One TemplateBrand per template with palette, typography, personality
- **16 assets** — One TemplateAsset (type=preview) per template, SVG mockups in media/template_assets/
- **0 tags** — Tag model exists but no tags seeded yet

## Key Architecture (Catalog)

```
Views (catalog/views.py)          ← Thin CBVs, delegate to selectors
  ↓
Selectors (catalog/selectors.py)  ← QuerySet-based read functions
  ↓
Models (catalog/models.py)        ← Category, WebTemplate, TemplateBrand, TemplateAsset, Tag
```

### URL Patterns (`catalog/urls.py`)
```
/templates/                           → TemplateListView (all published)
/templates/categories/                → CategoryListView
/templates/<category_slug>/           → TemplateListView (filtered by category)
/templates/<category_slug>/<slug>/    → TemplateDetailView
```

### Context Variables Per Template
| Template                        | Context                                                      |
|---------------------------------|--------------------------------------------------------------|
| `pages/home.html`               | `categories` (with template_count), `featured_templates`     |
| `catalog/category_list.html`    | `categories` (with template_count)                           |
| `catalog/template_list.html`    | `templates`, `category` (if filtered), `categories` (for dropdown) |
| `catalog/template_detail.html`  | `template` (with brand, category, tags, assets), `related_templates` |

## For Next Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, TODO_NEXT.md

### Immediate tasks (Phase 2b):

1. **Tag seeding and filtering** — Tag model exists. Seed relevant tags per template, add tag filter chips to listing page. Tags display already works on detail page sidebar.

2. **User authentication** — `accounts` app exists with custom User model. Build register, login, dashboard views and templates.

3. **Commerce flow** — Cart, checkout, order confirmation templates and views.

4. **Replace SVG previews with real screenshots** — When actual template HTML pages exist, generate real screenshots with Playwright and replace the SVG placeholders via `generate_previews --force`.

5. **PostgreSQL full-text search** — When deploying to production, replace `icontains` search in `get_listing_templates()` with PostgreSQL `SearchVector`/`SearchQuery` for better relevance ranking.

### Key Files for This Work Area
- `apps/catalog/selectors.py` — All read logic (search, sort, filter)
- `apps/catalog/views.py` — TemplateListView with pagination
- `templates/catalog/template_list.html` — Filter bar, grid, pagination
- `apps/catalog/management/commands/generate_previews.py` — SVG preview generator

### Constraints
- Do not redesign the existing architecture or model structure
- Preserve the premium UI — do not change CSS classes or component structure
- Follow the services/selectors pattern for new business logic
- All content in Italian per D-016
- Update coordination files at end of session

## Coordination Rules

- Backend-core owns: models, migrations, admin, services, selectors, management commands
- Premium-UI owns: templates/, static/, design system, frontend components
- Catalog integration owns: views, URLs, wiring templates to querysets
- Neither session should overwrite the other's files
- Both sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md at end
