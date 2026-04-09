# Agent Handoff

Last updated: 2026-04-09 — after Premium-UI Phase 1 (Session 2)

## Current State

**Backend-Core (Session 2, worktree-backend-core):** Complete. 7 apps created, custom User model, catalog models (Category, WebTemplate, TemplateBrand, TemplateAsset, Tag), admin, migrations, seed data, URL routing. Exists in `worktree-backend-core` branch.

**Premium-UI (Session 2, worktree-premium-ui):** Complete. Full design system, 14 template/static files created. Base template, navbar, footer, homepage, category list, template list, template detail, card components. All Italian content, no lorem ipsum.

**Merge needed:** Both worktrees must be merged to master before integration work can begin. No file conflicts expected — backend owns `apps/`, premium-UI owns `templates/` and `static/`.

## For Backend-Core Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, DECISIONS.md, TODO_NEXT.md

### Your immediate tasks (in order):

1. **Create the `apps/` directory** with seven app packages:
   ```
   apps/core/
   apps/accounts/
   apps/catalog/
   apps/editor/
   apps/projects/
   apps/commerce/
   apps/pages/
   ```
   Each with `__init__.py`, `models.py`, `admin.py`, `apps.py`, `services.py`, `selectors.py`, `urls.py`, `tests.py`.

2. **Create custom User model** in `apps/accounts/models.py`:
   - Extend `AbstractUser`
   - Add `uuid` field (public-facing ID)
   - Set `AUTH_USER_MODEL = 'accounts.User'` in settings.py
   - This MUST happen before any `migrate`

3. **Update `marketweb/settings.py`:**
   - Add all apps to `INSTALLED_APPS`
   - Set `AUTH_USER_MODEL`
   - Configure `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL`, `MEDIA_ROOT`
   - Configure `STATICFILES_DIRS`
   - Set `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'`
   - Update `TEMPLATES` DIRS to include project-level `templates/` directory

4. **Create core base models** in `apps/core/models.py`:
   - `TimestampedModel` — abstract with `created_at`, `updated_at`
   - `SlugModel` — abstract with `slug` field + auto-generation

5. **Create catalog models** in `apps/catalog/models.py`:
   - `Category` — name, slug, description, icon, order, is_active
   - `Tag` — name, slug
   - `WebTemplate` — title, slug, category FK, description, price, status, preview_url, etc.
   - `TemplateBrand` — OneToOne to WebTemplate: brand_name, tagline, palette JSON, typography, personality
   - `TemplateAsset` — FK to WebTemplate: file, asset_type, order

6. **Register all models in admin** with `list_display`, `list_filter`, `search_fields`.

7. **Create `requirements.txt`** pinning the dependencies we need.

8. **Run `makemigrations` then `migrate`** — verify everything is clean.

9. **Create initial categories** via fixture or management command (the 8 MVP categories).

10. **Set up URL routing skeleton** — include each app's `urls.py` in the main `marketweb/urls.py`.

### Constraints
- Follow the services/selectors pattern (see ARCHITECTURE.md)
- Keep models focused — no business logic in models beyond validation
- Use `apps.` prefix for all app references (configure `AppConfig.name` accordingly)
- Do NOT create frontend templates — that's the premium-UI workstream's job
- Document any architecture decisions in DECISIONS.md
- Update TODO_NEXT.md and AGENT_HANDOFF.md when done

## For Premium-UI Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, BRAND_SYSTEM_GUIDELINES.md, CONTENT_GUIDELINES.md, DECISIONS.md, TODO_NEXT.md

### Your immediate tasks:

1. **Create the `templates/` directory structure:**
   ```
   templates/
     base.html
     includes/
       _navbar.html
       _footer.html
       _template_card.html
       _category_card.html
       _hero.html
     pages/
       home.html
     catalog/
       category_list.html
       template_list.html
       template_detail.html
   ```

2. **Create the `static/` directory structure:**
   ```
   static/
     css/
       design-system.css      (or SCSS if build pipeline added)
       components.css
       pages.css
     js/
       main.js
     images/
       brand/
   ```

3. **Build `base.html`:**
   - Bootstrap 5.3 CDN (CSS + JS bundle)
   - Google Fonts (Inter or Plus Jakarta Sans)
   - Include design-system.css
   - Blocks: title, meta, extra_css, content, extra_js
   - Include navbar and footer partials
   - `lang` and `dir` attributes ready for RTL switching

4. **Implement the design system CSS:**
   - CSS custom properties for colors, spacing, typography
   - Follow BRAND_SYSTEM_GUIDELINES.md specifications
   - Premium card component styles
   - Button variants
   - Section spacing utilities

5. **Build premium navbar** (`_navbar.html`):
   - Logo placeholder, navigation links, CTA button
   - Sticky with backdrop-blur on scroll
   - Mobile responsive (hamburger → slide-out)

6. **Build premium footer** (`_footer.html`):
   - Multi-column layout, links, social icons, copyright

7. **Build homepage** (`pages/home.html`):
   - Hero section with headline, subheadline, CTA
   - Featured categories grid
   - Featured templates grid (using template_card partial)
   - Trust/stats section
   - Final CTA section

8. **Build template card component** (`_template_card.html`):
   - Image, category badge, title, brand name, price, hover effect
   - Follow BRAND_SYSTEM_GUIDELINES.md card standards

9. **Build category listing page skeleton**

10. **Build template detail page skeleton**

### Constraints
- Do NOT modify models, migrations, or backend Python code
- Use Django template tags and blocks properly
- Make all components RTL-aware from the start (logical properties, dir-aware spacing)
- The backend may not have views ready yet — you can use static/hardcoded content in templates for now
- Create a simple view in `apps/pages/views.py` for the homepage if needed, but keep it minimal
- Document design decisions in BRAND_SYSTEM_GUIDELINES.md
- Update TODO_NEXT.md and AGENT_HANDOFF.md when done

### Status: COMPLETE
All 10 tasks finished. See SESSION_LOG.md Session 2 for details.

## For Integration Session (Phase 1.5)

**Read first:** CLAUDE.md, ARCHITECTURE.md, TODO_NEXT.md, BRAND_SYSTEM_GUIDELINES.md

### Your immediate tasks:

1. **Merge both worktrees to master:**
   - `worktree-backend-core` — has all apps/, models, migrations, admin, settings updates
   - `worktree-premium-ui` — has all templates/, static/, design system, settings changes
   - Resolve any settings.py conflict (backend-core version is more complete, just ensure TEMPLATES DIRS and STATICFILES_DIRS are present)

2. **Create catalog views:**
   - `CategoryListView` — pass `categories` queryset to `catalog/category_list.html`
   - `TemplateListView` — pass `templates` queryset to `catalog/template_list.html`, support category filtering
   - `TemplateDetailView` — pass `template` with `select_related('brand', 'category')` to `catalog/template_detail.html`

3. **Update catalog URLs:**
   - `/templates/` → TemplateListView
   - `/templates/<category_slug>/` → TemplateListView (filtered)
   - `/templates/<slug>/` → TemplateDetailView

4. **Wire homepage to real data:**
   - Update `HomePageView` to pass `categories` (active, ordered) and `featured_templates` (featured=True) to context
   - Update `home.html` to use `{% for %}` loops over real querysets instead of hardcoded cards

5. **Add seed template data:**
   - Create at least 2-3 WebTemplate instances with TemplateBrand data for each MVP category
   - Match the brand names used in the static homepage content (Vertex Studio, Osteria Moderna, SaluteVita Clinic, Chiara Studio, Pragma Corp, Studio Legale Ferri)

### Key files and their expected context variables:

| Template                        | Expected Context                                             |
|---------------------------------|--------------------------------------------------------------|
| `pages/home.html`               | `categories`, `featured_templates`                            |
| `catalog/category_list.html`    | `categories` (with `.templates.count`)                        |
| `catalog/template_list.html`    | `templates`, `category` (optional, for filtered view)         |
| `catalog/template_detail.html`  | `template` (with `.brand`, `.category`, `.assets`, `.tags`)   |

### Template card model field mapping:

| Card Element          | Model Field                          |
|-----------------------|--------------------------------------|
| Image                 | `template.assets.first.file.url`     |
| Category badge        | `template.category.name`             |
| Brand name            | `template.brand.brand_name`          |
| Title                 | `template.name`                      |
| Description           | `template.short_description`         |
| Price                 | `template.price`, `template.is_free` |

## Coordination Rules

- Both sessions MUST read ARCHITECTURE.md before starting
- Backend-core owns: models, migrations, admin, services, selectors, management commands
- Premium-UI owns: templates/, static/, design system, frontend components
- Neither session should overwrite the other's files
- Both sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md at end
- If a session needs something from the other, document it in TODO_NEXT.md as a dependency
