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
