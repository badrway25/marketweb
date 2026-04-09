# Architecture

## Django App Structure

```
marketweb/                  # Project config (settings, urls, wsgi/asgi)
apps/
  core/                     # Shared utilities, base models, mixins, site settings
  accounts/                 # Custom User model, profiles, authentication
  catalog/                  # Categories, tags, web template listings
  editor/                   # Customization engine, live preview, content editing
  projects/                 # Customer saved projects, revisions, exports
  commerce/                 # Cart, orders, pricing, licenses, Stripe payments
  pages/                    # Marketing/static pages (homepage, about, pricing)
```

### App Responsibilities

#### `core`
- Abstract base models: `TimestampedModel` (created_at, updated_at), `SlugModel`, `OrderableModel`
- Shared mixins and utilities
- Site-wide settings (singleton model or django-constance)
- Custom storage backends (media, template assets)
- Management commands shared across apps

#### `accounts`
- Custom User model extending AbstractUser (MUST be created before first migration)
- User profiles with role support (buyer, seller/admin)
- Authentication views (registration, login, password reset)
- OAuth foundations (future: Google, GitHub login)

#### `catalog`
- `Category` — marketplace categories (Agency, Business, Restaurant, etc.)
- `WebTemplate` — the main product: a website template listing
- `TemplateAsset` — images, thumbnails, preview files linked to a template
- `Tag` — flexible tagging for search/filter
- `TemplateBrand` — unique brand identity per template (name, palette, logo concept)
- Services: template listing, search, filtering
- Selectors: featured templates, by category, by tag, popular

#### `editor`
- `EditableRegion` — defines customizable zones within a template
- `RegionType` — text, image, color, font, etc.
- Template preview rendering (iframe-based or server-rendered)
- Content editing API endpoints (DRF)
- Live preview update mechanism

#### `projects`
- `CustomerProject` — a user's customization of a template
- `ProjectRevision` — version history of edits
- `ProjectContent` — stored content per editable region
- Export service (generate downloadable package)
- Services: save, load, revert, clone

#### `commerce`
- `PricePlan` — pricing tiers (free, one-time, subscription)
- `Order` — purchase record
- `OrderItem` — line items
- `License` — license keys and entitlements
- Stripe integration service (checkout sessions, webhooks)
- Subscription management

#### `pages`
- Homepage content and layout
- Static marketing pages
- SEO metadata per page
- Uses Django template inheritance with the design system

## Layered Architecture Pattern

```
Views / API Views          ← HTTP layer, thin, delegates to services
  ↓
Services (services.py)     ← Write operations, business logic, orchestration
Selectors (selectors.py)   ← Read operations, complex queries, filtering
  ↓
Models                     ← Data layer, validation, constraints
```

**Rules:**
- Views never contain business logic — they call services/selectors
- Services handle write operations (create, update, delete, state transitions)
- Selectors handle read operations (queries, filtering, aggregation)
- Models define data structure, field-level validation, and relationships
- Cross-app communication goes through services, never direct model imports between apps (except ForeignKey declarations)

## URL Structure

```
/                           → Homepage (pages app)
/templates/                 → Browse all templates (catalog)
/templates/<category>/      → Category filtered listing (catalog)
/templates/<slug>/          → Template detail + preview (catalog)
/editor/<project_id>/       → Customization editor (editor)
/projects/                  → User's saved projects (projects)
/cart/                      → Shopping cart (commerce)
/checkout/                  → Checkout flow (commerce)
/account/                   → User dashboard (accounts)
/admin/                     → Django admin
/api/v1/                    → DRF API root
```

## Frontend Architecture

- **Django templates** with template inheritance: `base.html` → `page.html` → specific pages
- **Bootstrap 5.x** customized via SCSS for premium look (not default Bootstrap appearance)
- **Design system** defined in `static/css/design-system/` with variables, typography, spacing, components
- **HTMX** (optional) for dynamic interactions without full SPA complexity
- **RTL support** via Bootstrap RTL bundle + custom RTL overrides for Arabic

## Static Files Layout

```
static/
  css/
    design-system/          # Variables, typography, spacing, colors
    components/             # Cards, buttons, forms, navigation
    pages/                  # Page-specific styles
  js/
    editor/                 # Customization editor scripts
    components/             # Shared JS components
  images/
    brand/                  # Site logo, favicon, OG images
templates/
  base.html                 # Master template
  includes/                 # Reusable partials (nav, footer, cards)
  pages/                    # Marketing pages
  catalog/                  # Listing and detail pages
  editor/                   # Editor interface
  accounts/                 # Auth and dashboard pages
  commerce/                 # Cart and checkout pages
```

## Database

- **Development:** SQLite
- **Production:** PostgreSQL (planned)
- Custom User model from day one (avoids painful migration later)
- UUIDs for customer-facing IDs (projects, orders, licenses)
- Integer PKs internally for performance

## Multilingual Strategy

- **UI strings:** Django's built-in i18n (`{% trans %}`, `.po` files)
- **Model content:** `django-modeltranslation` or manual translated fields (decision deferred to Phase 4)
- **Template marketplace content:** JSON-based translated content per template brand
- **RTL:** Bootstrap RTL + `dir="rtl"` attribute switching + custom CSS overrides
- Languages: IT (primary), EN, FR, AR

## API Layer

- Django REST Framework for editor save/load, project management, and future mobile
- `drf-spectacular` for OpenAPI schema generation
- Token or session-based auth
- Versioned under `/api/v1/`
