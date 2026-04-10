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

## D-022: SVG Preview Images Using Brand Palettes (2026-04-09)
**Decision:** Generate structured SVG files that look like website mockups (browser chrome + page layout), colored with each template's brand palette. Stored via TemplateAsset model (asset_type='preview').
**Rationale:** SVGs scale perfectly, are lightweight, and each is visually unique because of the distinct brand palettes. The browser-chrome framing makes them look like real screenshots. They can be replaced with actual screenshots later without changing any template code — just swap the TemplateAsset file.

## D-023: Search via ORM icontains Across 4 Fields (2026-04-09)
**Decision:** Search filters using Django ORM `Q(name__icontains=q) | Q(short_description__icontains=q) | Q(description__icontains=q) | Q(brand__brand_name__icontains=q)`.
**Rationale:** Simple, works with SQLite in dev. PostgreSQL full-text search can replace this in production via a selector swap — no view or template changes needed.

## D-024: Four Sort Options, No "Popular" (2026-04-09)
**Decision:** Sort options are: recent (default), price ascending, price descending, name A-Z. "Popular" sort omitted.
**Rationale:** No view/download count model exists yet. Adding a dummy popularity sort would be misleading. Can add when commerce or analytics tracking is implemented.

## D-025: Pagination at 12 Per Page (2026-04-09)
**Decision:** `paginate_by = 12` on TemplateListView.
**Rationale:** 12 items = 4 rows of 3 cards on desktop, a comfortable scroll depth. Matches the 3-column grid layout. With 16 templates, produces 2 pages — enough to verify pagination works.

## D-029: HTML Compositions + Playwright Screenshots for Previews (2026-04-10)
**Decision:** Replace SVG-string previews with PNG screenshots of Django-rendered HTML pages, captured via headless Chromium (Playwright sync API).
**Rationale:** A premium marketplace cannot ship grey wireframes. Real homepage screenshots with photographic content communicate template value at a glance and dramatically improve conversion intent. HTML+CSS gives us the same expressive control as a real website (fonts, gradients, real photos) without re-implementing a layout engine in Python. The `TemplateAsset` API stays the same, so listing/detail templates need zero changes — only the file format moves from `.svg` to `.png`.
**Trade-off:** Heavier dependency surface (Playwright + Chromium binary), larger asset files (~4 MB vs ~5 KB), and screenshot generation requires a browser process. Acceptable because previews are generated offline and served as static media.

## D-030: Per-Category Preview Compositions, Brand-Customised at Render Time (2026-04-10)
**Decision:** One HTML composition per MVP category (8 total), parameterised by brand palette + typography. Multiple templates inside a category share the same layout and stock imagery; brand identity comes from injected colours and Google Font pairing.
**Rationale:** 8 well-crafted layouts is a much better quality bar than 16+ rushed ones. Category specificity (a restaurant looks like a restaurant, a clinic looks like a clinic) is the primary signal users need. Brand differentiation via palette + type still gives each preview its own colour signature without doubling the maintenance cost.
**Trade-off:** Two templates in the same category have identical photo content. Mitigation path: add an optional `imagery_overrides` field on `TemplateBrand` later if buyers report confusion.

## D-031: Curated Stock Imagery via Cached Unsplash URLs (2026-04-10)
**Decision:** Imagery is configured as a Python dict (`apps/catalog/preview_imagery.IMAGERY_CONFIG`) of category → list of Unsplash CDN URLs, with a `ensure_cached()` helper that downloads them once into `media/preview_imagery/<category>/<sha>.jpg` and returns local file paths.
**Rationale:** A single config file is the swap point. To move to local stock, licensed images, or AI-generated illustrations later, only the config changes — compositions and the generator stay untouched. The cache means subsequent runs are offline-friendly and idempotent. Unsplash CDN URLs are stable and free for commercial use under Unsplash's license.
**Trade-off:** First run requires network access; broken URLs degrade gracefully (the affected slot just falls back to the hero photo, padded by `_build_context`).

## D-032: Three-Phase generate_previews Pipeline (2026-04-10)
**Decision:** The command runs in three sequential phases: (A) all ORM reads + HTML rendering, (B) Playwright headless screenshots with no ORM access, (C) all ORM writes (TemplateAsset persistence).
**Rationale:** `playwright.sync_api.sync_playwright()` runs an asyncio loop on the calling thread. Inside its `with` block, Django's ORM raises `SynchronousOnlyOperation` because the loop is "running". Splitting work into three phases avoids the conflict cleanly without `sync_to_async` shims.
**Trade-off:** All templates' rendered HTML must be held in memory before screenshots start. At 16 templates × ~10 KB HTML = 160 KB, this is irrelevant.

## D-033: 1600×900 PNG at 2× Device Scale (2026-04-10)
**Decision:** Previews render at viewport 1600×900 with `device_scale_factor=2`, output PNG. Resulting files are ~3200×1800 pixels and ~4 MB each.
**Rationale:** 16:9 matches the 4:3-to-16:9 ratio expected by the existing template card. 2× DPI keeps text crisp on retina displays. PNG preserves the sharp UI lines (buttons, dividers) without JPEG halos.
**Trade-off:** ~70 MB total media for 16 templates. Acceptable for development; for production we should add an optional `--optimize` step that runs `oxipng`/`pngquant` or pipes through Pillow with `optimize=True`/JPEG conversion.

## D-034: Per-Template DNA Registry in Code, Not in the Database (2026-04-10)
**Decision:** Each template's design DNA (archetype, hero/navbar/footer style, density, tone, conversion pattern, font pairing, content blocks) lives as a Python dict in `apps/catalog/template_dna.py`, keyed by `WebTemplate.slug` — not as a JSONField on `TemplateBrand`.
**Rationale:** The DNA drives HTML composition files. It must be reviewed in PRs alongside the layouts it controls, version-locked to its compositions, and editable without a migration. Promoting it to the database is an option later when the vocabulary stabilises and marketing wants admin-side editing — but doing so now would couple "design intent" to "data state", which is harder to reason about.
**Trade-off:** Marketing cannot edit DNA without a developer. Acceptable for a pre-launch marketplace where every template still has bespoke design work anyway.

## D-035: Archetype-Keyed Composition Path (2026-04-10)
**Decision:** Composition files for DNA-driven templates live at `templates/preview_compositions/<category>/<archetype>.html` (e.g. `medical/clinic.html`, `medical/family.html`, `medical/wellness.html`, `medical/specialist.html`). The legacy single-file path `<category>.html` remains as a fallback.
**Rationale:** Grouping by category-then-archetype makes the file tree describe the differentiation: a glance at `templates/preview_compositions/medical/` tells you exactly which archetypes are in production for that category. The fallback path keeps the system additive.
**Trade-off:** Two files per template (DNA entry + composition file). Worth it: that's exactly the level at which a "premium template" stops being a recolor and becomes a real product.

## D-036: DNA System Is Strictly Additive (2026-04-10)
**Decision:** Adding a DNA entry never breaks an existing preview. Templates without DNA continue to render via the legacy per-category composition. Migrating a category to per-template archetypes is a slug-by-slug choice.
**Rationale:** A big-bang rewrite of all 8 categories at once would block delivery for weeks and risk regressing quality on the templates that already work. Per-template migration lets us pilot Medical, prove the model, then move to the next category with zero risk to the others.
**Trade-off:** Mixed state during the migration window — some categories use DNA, others don't. The catalog UI doesn't care; the only place that knows is `generate_previews._resolve_composition`.

## D-037: `imagery_key` Lives on the DNA, Not on the Brand (2026-04-10)
**Decision:** Each DNA entry can specify `imagery_key`, which is the lookup into `IMAGERY_CONFIG`. Without it, the generator falls back to `category.slug`.
**Rationale:** Two templates in the same category should not share the same photo set, otherwise they collapse visually even if their layouts differ. Keying imagery on DNA (not on `TemplateBrand`) keeps the imagery decision adjacent to the layout decision — they are part of the same design choice.
**Trade-off:** New imagery keys mean new entries in `IMAGERY_CONFIG`. Acceptable; the file is already the swap point per D-031.

## D-038: Custom `at` Template Filter for Image Indexing (2026-04-10)
**Decision:** `apps/catalog/templatetags/preview_extras.py` registers an `at` filter that takes a sequence and an integer (or string-of-integer, for `forloop.counter`) and returns the element, falling back to `seq[0]` on overflow.
**Rationale:** Django's stock template language cannot index a list by a loop variable — `{{ imagery|slice:i:i+1 }}` doesn't accept variables. The DNA-driven compositions need to zip a content list (e.g. specialties, doctors) with the imagery list, which requires per-iteration index lookup. A four-line custom filter is the minimal correct solution.
**Trade-off:** A new templatetag library. Tiny surface, zero risk.
