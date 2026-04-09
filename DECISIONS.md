# Decisions Log

## D-001: Django App Structure — Modular Multi-App (2026-04-09)
**Decision:** Seven separate Django apps under `apps/` directory: core, accounts, catalog, editor, projects, commerce, pages.
**Rationale:** Each domain has distinct responsibilities. Avoids monolithic app. Enables parallel development (backend-core can work on catalog models while premium-ui works on templates).
**Trade-off:** More boilerplate vs. better separation of concerns and scalability.

## D-002: Custom User Model from Day One (2026-04-09)
**Decision:** Create custom User model in `accounts` app before first `migrate`.
**Rationale:** Switching to a custom User model after migrations exist is extremely painful in Django. Even if we don't need custom fields now, this is a one-way door that must be done first.

## D-003: Services/Selectors Pattern (2026-04-09)
**Decision:** Business logic in `services.py` (writes) and `selectors.py` (reads), not in views or models.
**Rationale:** Keeps views thin, makes logic testable without HTTP, prevents fat model anti-pattern.

## D-004: "WebTemplate" Naming for Marketplace Items (2026-04-09)
**Decision:** Marketplace template listings are called `WebTemplate` (model) in the `catalog` app.
**Rationale:** Avoids confusion with Django's template engine. The app is `catalog`, not `templates`.

## D-005: Bootstrap 5.x with Custom SCSS (2026-04-09)
**Decision:** Use Bootstrap 5 as the CSS framework, but heavily customized via SCSS variables and custom components.
**Rationale:** Bootstrap provides responsive grid, utilities, and accessibility out of the box. Custom SCSS prevents the "default Bootstrap" look and achieves premium aesthetics.

## D-006: Django 5.2.7 LTS (2026-04-09)
**Decision:** Use Django 5.2.7 (the version actually installed), not 6.0.4 as stated in the auto-generated settings comment.
**Rationale:** 5.2 is the current LTS release. The settings.py was generated from a template that referenced 6.0.4, but our environment has 5.2.7.

## D-007: UUIDs for Customer-Facing IDs (2026-04-09)
**Decision:** Use UUIDs for public-facing resources (projects, orders, licenses). Integer PKs internally.
**Rationale:** UUIDs prevent enumeration attacks and look professional in URLs. Integer PKs kept for internal FK performance.

## D-008: SQLite for Development, PostgreSQL for Production (2026-04-09)
**Decision:** Keep SQLite for local dev. Plan for PostgreSQL in production.
**Rationale:** SQLite is zero-config for development. PostgreSQL provides the JSON fields, full-text search, and concurrency needed in production.

## D-009: Stripe for Payments (2026-04-09)
**Decision:** Stripe as the payment processor (already installed in environment).
**Rationale:** Industry standard, excellent Python SDK, supports one-time payments and subscriptions.

## D-010: Italian as Primary Language (2026-04-09)
**Decision:** Italian is the primary language, with EN, FR, AR as secondary.
**Rationale:** Project originates in Italian market. Arabic requires RTL support.

## D-011: `mw-` CSS Class Prefix (2026-04-09)
**Decision:** All custom CSS classes use `mw-` prefix (e.g., `.mw-btn`, `.mw-template-card`, `.mw-hero`).
**Rationale:** Avoids collision with Bootstrap utility classes and third-party CSS. Makes custom styles easily identifiable.

## D-012: Plus Jakarta Sans + Inter Font Pairing (2026-04-09)
**Decision:** Plus Jakarta Sans for display/headings, Inter for body text. Both from Google Fonts.
**Rationale:** Plus Jakarta Sans has a distinctive, premium feel with excellent weight range (500-800). Inter is the gold standard for UI body text with excellent readability. Both are free and well-supported.

## D-013: CSS Custom Properties Over SCSS (2026-04-09)
**Decision:** Use native CSS custom properties (variables) instead of SCSS for the design system.
**Rationale:** Zero build step for development. Custom properties work at runtime (theming possible). Can add SCSS later if needed without breaking existing styles. SCSS can still be introduced later for nesting/imports.

## D-014: Template Cards Reference Backend Model Fields (2026-04-09)
**Decision:** Template card partials use `template.name`, `template.brand.brand_name`, `template.category.name`, `template.price`, `template.is_free`, `template.short_description`, `template.assets.first.file.url` — matching backend-core's catalog models.
**Rationale:** Ensures seamless integration when backend views pass model instances to templates. Static fallback content provided for development without backend data.

## D-015: Static Fallback Content in Listing Pages (2026-04-09)
**Decision:** Listing pages include `{% if templates %}...{% else %}...{% endif %}` blocks with hardcoded realistic content.
**Rationale:** Allows the UI to be previewed and developed independently of backend views. Fallback content uses realistic Italian text matching CONTENT_GUIDELINES.md. Will be replaced by dynamic data as backend views are connected.

## D-016: All Template Content in Italian (2026-04-09)
**Decision:** All UI text, placeholder content, and microcopy written in Italian as the primary language.
**Rationale:** Per D-010, Italian is the primary market language. i18n/{% trans %} tags will be added in Phase 4 for multilingual support.

## D-017: Category Names in Italian, Slugs in English (2026-04-09)
**Decision:** Category `name` field uses Italian display names (Ristorante, Medico, Avvocato, Immobiliare) while `slug` stays English (restaurant, medical, lawyer, real-estate).
**Rationale:** Italian names match the homepage UI and D-016. English slugs are URL-friendly and internationally readable. International categories (Agency, Business, Portfolio, eCommerce) are the same in both languages.

## D-018: Two-Segment Detail URL `/<category>/<slug>/` (2026-04-09)
**Decision:** Template detail uses `/templates/<category_slug>/<template_slug>/` instead of `/templates/<slug>/`.
**Rationale:** Prevents slug collisions across categories (e.g., two categories could each have a "starter" template). Also improves SEO with category context in the URL and enables breadcrumb navigation.

## D-019: Selectors Return QuerySets (2026-04-09)
**Decision:** Catalog selectors return Django QuerySets, not evaluated lists.
**Rationale:** Allows views to chain additional filters, annotations, or pagination on top. QuerySets are lazy — no DB hit until the template iterates.

## D-020: Icon Field Without `bi-` Prefix (2026-04-09)
**Decision:** Category `icon` stores just the icon name (e.g., "megaphone") without the `bi-` prefix. The template partial renders `<i class="bi bi-{{ category.icon }}">`.
**Rationale:** Previous seed data stored "bi-rocket-takeoff" which would render as `bi bi-bi-rocket-takeoff` (double prefix). Keeping the raw name is more portable — could switch icon libraries later.

## D-021: Static Fallbacks Removed After Catalog Integration (2026-04-09)
**Decision:** Removed all hardcoded static fallback content from listing pages. Pages now show `{% empty %}` states instead.
**Rationale:** D-015 was a temporary measure for UI development. With catalog views and seed data in place, static fallbacks are no longer needed and would mask missing data issues.
