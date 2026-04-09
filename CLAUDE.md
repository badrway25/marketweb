# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**marketweb** is an ultra-premium Django-based multilingual marketplace for website templates and customizable websites. Users browse templates by category/profession, preview them, customize content online, save changes, and buy/download the result or use a hosted subscription.

## Tech Stack

- **Backend**: Django 5.2.7 LTS, Python 3.13.5
- **API**: Django REST Framework + drf-spectacular
- **Frontend**: Bootstrap 5.x (custom SCSS) with Django templates
- **Forms**: django-crispy-forms + crispy-bootstrap5
- **Payments**: Stripe
- **Async**: Celery + django-celery-beat
- **Database**: SQLite (dev), PostgreSQL (production)
- **Languages**: Italian (primary), English, French, Arabic (RTL)
- **Linting**: ruff, black

## Common Commands

```bash
# Run development server
python manage.py runserver

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test
python manage.py test apps.<app_name>
python manage.py test apps.<app_name>.tests.TestClass.test_method

# Linting and formatting
ruff check .
black .

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Install dependencies
pip install -r requirements.txt
```

## Architecture

### Django Apps (under `apps/`)

| App         | Responsibility                                              |
|-------------|-------------------------------------------------------------|
| `core`      | Abstract base models, shared utilities, mixins, site config |
| `accounts`  | Custom User model, profiles, authentication                 |
| `catalog`   | Categories, WebTemplate listings, tags, assets, brands      |
| `editor`    | Customization engine, editable regions, live preview         |
| `projects`  | Customer saved projects, revisions, exports                 |
| `commerce`  | Cart, orders, pricing, licenses, Stripe payments            |
| `pages`     | Homepage and marketing/static pages                         |

All apps use `apps.<name>` import paths. App configs set `name = 'apps.<name>'`.

### Services/Selectors Pattern

- **`services.py`** — write operations, business logic, orchestration
- **`selectors.py`** — read operations, complex queries, filtering
- **Views** are thin HTTP handlers that delegate to services/selectors
- Cross-app communication goes through services, not direct model imports

### Key Models

- `accounts.User` — custom user model (AUTH_USER_MODEL), has public UUID
- `catalog.Category` — marketplace categories
- `catalog.WebTemplate` — the main product listing
- `catalog.TemplateBrand` — unique brand identity per template (OneToOne)
- `catalog.TemplateAsset` — files attached to a template
- `editor.EditableRegion` — customizable zones within templates
- `projects.CustomerProject` — user's customization of a template
- `commerce.Order` / `commerce.License` — purchase and licensing

### URL Structure

```
/                           → Homepage
/templates/                 → Browse templates
/templates/<category>/      → Category listing
/templates/<slug>/          → Template detail
/editor/<project_id>/       → Customization editor
/projects/                  → User's projects
/account/                   → User dashboard
/cart/ and /checkout/       → Commerce flow
/api/v1/                    → DRF API
/admin/                     → Django admin
```

### Frontend

- Django template inheritance: `base.html` → page templates
- Design system in `static/css/` with CSS custom properties
- RTL support via Bootstrap RTL bundle + logical CSS properties
- Reusable partials in `templates/includes/`

## Multi-Agent Workflow

Three specialized agent roles in `prompts/claude/`:
- **00_orchestrator_bootstrap.md** — architecture, roadmap, coordination
- **10_backend_core.md** — Django backend implementation
- **20_premium_ui.md** — premium design system and templates

### Session Coordination Files

Update these at the end of each session:
- `SESSION_LOG.md` — what was done
- `DECISIONS.md` — architectural decisions with rationale
- `TODO_NEXT.md` — prioritized next tasks per workstream
- `ARCHITECTURE.md` — full system architecture reference
- `AGENT_HANDOFF.md` — instructions for next session
- `CONTENT_GUIDELINES.md` — writing rules per category
- `BRAND_SYSTEM_GUIDELINES.md` — visual design system spec
- `CATEGORY_ROADMAP.md` — MVP and future categories
- `TEMPLATE_REGISTRY.json` — template brand registry

## Critical Rules

1. **Custom User model** (`accounts.User`) must exist before first `migrate`
2. **No lorem ipsum** — all content must be realistic and business-specific
3. Each template needs a unique brand identity (name, palette, logo, personality)
4. Backend-core and premium-UI must not overwrite each other's files
5. UUIDs for customer-facing IDs, integer PKs internally
