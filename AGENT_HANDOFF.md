# Agent Handoff

Last updated: 2026-04-09 — after Catalog Integration Phase 1 (Session 4)

## Current State

**Merged and running.** Backend-core and premium-UI branches merged to master. Catalog integration complete — all marketplace pages are now database-backed with real querysets.

**Session 4 completed:** Catalog views, selectors, URLs, and seed data. Homepage, listing, detail, and category pages all wired to real Category and WebTemplate models. 16 templates with brand identities seeded across all 8 MVP categories.

**UI status:** All premium UI preserved. Homepage renders: hero, stats, 8 dynamic category cards (with real counts), 6 featured template cards (from DB), how-it-works, testimonials, CTA. Listing page shows all 16 templates with dynamic category filter dropdown. Detail page has working breadcrumbs, tabs, sidebar, and related templates section.

## What's Working

| Page                          | URL                                        | Status  |
|-------------------------------|-------------------------------------------|---------|
| Homepage                      | `/`                                        | Dynamic |
| Template listing (all)        | `/templates/`                              | Dynamic |
| Template listing (filtered)   | `/templates/<category_slug>/`              | Dynamic |
| Template detail               | `/templates/<category_slug>/<slug>/`       | Dynamic |
| Category listing              | `/templates/categories/`                   | Dynamic |
| Admin                         | `/admin/`                                  | Working |

## Database State

- **8 categories** — Agency, Business, Ristorante, Medico, Avvocato, Immobiliare, Portfolio, eCommerce
- **16 templates** — 2 per category, all status=published, 6 marked featured
- **16 brands** — One TemplateBrand per template with palette, typography, personality
- **0 assets** — No images yet (placeholder icons shown)
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

### Immediate tasks (Phase 2):

1. **Add template preview images** — Either create placeholder screenshots or use CSS-generated previews. TemplateAsset model is ready, `_template_card.html` already handles `template.assets.first`.

2. **Search and sort functionality** — The filter bar in `template_list.html` has a search input and sort dropdown but they're not wired to backend queries. Add query params handling in `TemplateListView` and corresponding selectors.

3. **Pagination** — `TemplateListView` should paginate. The template already has pagination HTML (using `templates.has_other_pages`). Add `paginate_by = 12` to the view.

4. **Tag seeding and filtering** — Tag model exists. Seed relevant tags per template, add tag filter to listing page.

5. **User authentication** — `accounts` app exists with custom User model. Build register, login, dashboard views and templates.

6. **Commerce flow** — Cart, checkout, order confirmation templates and views.

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
