# Agent Handoff

Last updated: 2026-04-09 — after Backend-Core Session 2

## Current State

Phase 1 backend foundation is **complete**. All 7 app scaffolds are created, the custom User model is in place, catalog models are defined, admin is registered, migrations are applied, 8 MVP categories are seeded, and URL routing is wired up. Django system check passes with 0 issues.

The project is ready for:
- **Premium-UI** to build templates and design system (Phase 1 UI)
- **Backend-Core** Phase 2 work (editor, projects, commerce models + API)

## What Backend-Core Has Done (Session 2)

### App Structure
```
apps/
  __init__.py
  core/           ← TimestampedModel, SlugModel (abstract bases)
  accounts/       ← Custom User model (AbstractUser + UUID)
  catalog/        ← Category, Tag, WebTemplate, TemplateBrand, TemplateAsset
  editor/         ← Scaffold only (Phase 2)
  projects/       ← Scaffold only (Phase 2)
  commerce/       ← Scaffold only (Phase 2)
  pages/          ← HomePageView
```

### Models Available
| Model | App | Key Fields |
|-------|-----|------------|
| `User` | accounts | AbstractUser + `uuid` (UUIDField, unique) |
| `Category` | catalog | name, slug, description, icon, order, is_active |
| `Tag` | catalog | name, slug |
| `WebTemplate` | catalog | name, slug, category (FK), description, price, status, featured |
| `TemplateBrand` | catalog | template (O2O), brand_name, tagline, palette (JSON), typography, personality |
| `TemplateAsset` | catalog | template (FK), file, asset_type, alt_text, order |

### URL Namespaces
| Prefix | App | Namespace |
|--------|-----|-----------|
| `/` | pages | `pages` |
| `/templates/` | catalog | `catalog` |
| `/account/` | accounts | `accounts` |
| `/editor/` | editor | `editor` |
| `/projects/` | projects | `projects` |
| `/cart/`, `/checkout/` | commerce | `commerce` |
| `/api/v1/` | core | `core` |
| `/admin/` | Django admin | — |

### Settings Configured
- `AUTH_USER_MODEL = "accounts.User"`
- `LANGUAGE_CODE = "it"`, `TIME_ZONE = "Europe/Rome"`
- `TEMPLATES DIRS = [BASE_DIR / "templates"]`
- `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS`, `MEDIA_URL`, `MEDIA_ROOT`
- DRF, drf-spectacular, django-filters, crispy-forms all configured
- `DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"`

### Migrations Applied
- `accounts.0001_initial` — User model
- `catalog.0001_initial` — All catalog models
- All Django contrib migrations

### Seed Data
- 8 MVP categories loaded via `python manage.py seed_categories`

## For Premium-UI Session (Next)

**Read first:** CLAUDE.md, ARCHITECTURE.md, BRAND_SYSTEM_GUIDELINES.md, CONTENT_GUIDELINES.md

### What you can now rely on:
- `templates/` and `static/` directories exist at project root
- `base.html` should go in `templates/base.html` — TEMPLATES DIRS is configured
- URL namespace `pages:home` resolves to `/` — template expected: `pages/home.html`
- Category model fields: `name`, `slug`, `description`, `icon`, `order`, `is_active`
- WebTemplate fields: `name`, `slug`, `category`, `description`, `short_description`, `price`, `is_free`, `featured`, `status`
- TemplateBrand fields: `brand_name`, `tagline`, `palette` (JSON), `typography`, `personality`
- Bootstrap Icons are used for category icons (e.g., `bi-rocket-takeoff`)

### Your immediate tasks:
1. Create `templates/base.html` — Bootstrap 5.3 CDN, Inter font, design system CSS, blocks
2. Create `static/css/design-system.css` — CSS custom properties, premium styles
3. Build `_navbar.html`, `_footer.html` partials
4. Build `pages/home.html` — hero, featured categories, featured templates, CTA
5. Build `_template_card.html`, `_category_card.html` partials
6. Build `catalog/template_list.html`, `catalog/template_detail.html` skeletons
7. All components RTL-ready from the start

### Constraints:
- Do NOT modify any Python files (models, views, settings, migrations)
- Use hardcoded/static content in templates for now (views will pass context later)
- Follow BRAND_SYSTEM_GUIDELINES.md for all visual decisions

## For Backend-Core Session (Phase 2)

### Next tasks:
1. Editor models: `EditableRegion`, `RegionType`
2. Projects models: `CustomerProject` (UUID), `ProjectRevision`, `ProjectContent`
3. Commerce models: `PricePlan`, `Order`, `OrderItem`, `License`
4. DRF serializers and viewsets for catalog
5. Catalog selectors: `get_featured_templates()`, `get_templates_by_category()`, `get_published_templates()`
6. Auth views: registration, login, password reset
7. Homepage view context: pass featured categories and templates to template

## Coordination Rules
- Backend-core owns: models, migrations, admin, services, selectors, management commands, views, API
- Premium-UI owns: templates/, static/, design system, frontend components
- Neither session should overwrite the other's files
- Both sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md at end
