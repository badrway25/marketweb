# Brand System Guidelines

## Marketplace Brand (marketweb itself)

### Visual Identity
- **Premium, not flashy.** The marketplace should feel like a curated gallery, not a discount store.
- **Trust-first design.** Every element should reinforce professionalism and quality.
- **Spacious layouts.** Generous whitespace, deliberate spacing, no visual clutter.

### Color System
Define in the design system SCSS variables:
- `$primary` — main brand color (trust, action)
- `$secondary` — supporting accent
- `$success`, `$warning`, `$danger` — semantic colors
- `$neutral-50` through `$neutral-900` — grayscale scale for text, backgrounds, borders
- `$surface-*` — background surfaces (card, elevated, sunken)

### Typography
- **Headings:** Modern, distinctive sans-serif (e.g., Inter, Plus Jakarta Sans, or similar premium Google Font)
- **Body:** Highly readable, generous line height (1.6-1.7), base size 16px
- **Scale:** Use a consistent type scale (e.g., 1.25 ratio: 16, 20, 25, 31, 39, 49px)

### Spacing System
- Base unit: 8px
- Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128px
- Use only values from the scale — no arbitrary spacing

### Component Standards

#### Cards (Template Listing)
- Subtle shadow or border, not both
- Hover state: gentle lift (translateY + shadow change)
- Image ratio: 16:9 or 4:3 for consistency
- Clear hierarchy: image → title → category badge → price → CTA

#### Buttons
- Primary: filled, rounded corners (6-8px radius)
- Secondary: outlined variant
- Generous padding (12-16px vertical, 24-32px horizontal)
- Clear hover/active states

#### Navigation
- Clean, minimal header
- Logo left, navigation center or right
- Sticky on scroll with subtle background blur
- Mobile: slide-out or full-screen overlay menu

#### Forms
- Large input fields (48-56px height)
- Floating labels or clear placeholders
- Visible focus states with brand color
- Inline validation feedback

### Responsive Breakpoints
Follow Bootstrap 5 defaults:
- sm: 576px
- md: 768px
- lg: 992px
- xl: 1200px
- xxl: 1400px

### Accessibility
- Color contrast ratio: minimum 4.5:1 for text
- Focus indicators on all interactive elements
- Semantic HTML throughout
- ARIA labels where needed

### RTL Considerations
- All spacing/layout utilities must work in RTL
- Use logical properties where possible (margin-inline-start vs margin-left)
- Test navigation, cards, forms in RTL mode
- Bootstrap RTL bundle handles most grid/utility flipping

## Implemented Design System (Session 2)

### CSS Architecture
Three CSS files loaded in this order:
1. `design-system.css` — Variables, base resets, typography, buttons, badges, utilities
2. `components.css` — Navbar, cards, hero, footer, stats, filter bar, detail components
3. `pages.css` — Homepage, listing, detail page-specific styles

### Color Palette (as implemented)
| Token                | Hex       | Usage                          |
|----------------------|-----------|--------------------------------|
| `--mw-primary`       | `#1B2A4A` | Dark navy — hero backgrounds   |
| `--mw-primary-light` | `#2C3E6B` | Gradient end                   |
| `--mw-secondary`     | `#6366F1` | Indigo — CTAs, links, accents  |
| `--mw-secondary-dark`| `#4F46E5` | Hover states                   |
| `--mw-accent`        | `#F59E0B` | Amber — highlights, overlines  |
| `--mw-neutral-50`    | `#F8FAFC` | Sunken surface backgrounds     |
| `--mw-neutral-900`   | `#0F172A` | Darkest text, footer background|

### Typography (as implemented)
| Role     | Font               | Weights Used  |
|----------|--------------------|---------------|
| Display  | Plus Jakarta Sans  | 500–800       |
| Body     | Inter              | 400–700       |

Type scale: 12, 14, 16, 18, 20, 24, 30, 36, 48, 60px (1.25 ratio)

### Component Inventory
| Component          | File              | Key Classes                    |
|--------------------|-------------------|--------------------------------|
| Navbar             | `_navbar.html`    | `.mw-navbar`, `.scrolled`      |
| Footer             | `_footer.html`    | `.mw-footer`, `.mw-footer-*`  |
| Template Card      | `_template_card`  | `.mw-template-card`            |
| Category Card      | `_category_card`  | `.mw-category-card`            |
| Hero               | `_hero.html`      | `.mw-hero`, `.mw-hero-*`      |
| Buttons            | design-system.css | `.mw-btn`, `.mw-btn-primary`   |
| Badges             | design-system.css | `.mw-badge`, `.mw-badge-free`  |
| Stats              | components.css    | `.mw-stat`, `.mw-stat-value`   |
| Filter Bar         | components.css    | `.mw-filter-bar`               |
| Detail Panel       | components.css    | `.mw-detail-panel`             |
| Testimonials       | pages.css         | `.mw-testimonial`              |
| Steps              | pages.css         | `.mw-steps`, `.mw-step`        |

## Template DNA System (Session 7 — 2026-04-10)

### Why DNA exists
A premium marketplace cannot ship two templates in the same category that look like recolors of each other. Each listing needs to be a credible, distinct *product*. Brand differentiation via palette + typography is necessary but not sufficient — buyers also need to perceive a **different layout, different conversion pattern, and different tone of voice** at a glance.

The DNA system encodes those differences as structured per-template metadata that drives bespoke HTML compositions during preview generation.

### DNA dimensions
Every template registered in `apps/catalog/template_dna.py` defines:

| Field                | What it controls                                                          |
|----------------------|---------------------------------------------------------------------------|
| `archetype`          | Which HTML composition file to render. Determines the entire skeleton.    |
| `hero_style`         | Hero composition: split-booking, centered-soft, editorial-serif, full-bleed-manifesto |
| `navbar_style`       | Navbar: solid-phone, pill-floating, minimal-serif, soft-pastel            |
| `footer_style`       | Footer: corporate-4col, compact-2col, centered-minimal, spa-social        |
| `section_order`      | Ordered list of sections to render                                        |
| `card_style`         | icon-grid, portrait-stack, editorial-large, pricelist                     |
| `button_style`       | rounded-solid, pill-soft, ghost-underline, square-bold                    |
| `density`            | compact, medium, airy, very-airy                                          |
| `tone`               | institutional, warm-family, prestigious, serene                           |
| `imagery_direction`  | High-level photo brief (used in copywriting/sourcing)                     |
| `imagery_key`        | Lookup into `IMAGERY_CONFIG` — distinct photo pool per archetype          |
| `conversion_pattern` | booking-widget, phone-and-chat, private-request, calendar-spot            |
| `font_pairing`       | Tuple of (heading, body) Google Fonts — overrides brand.typography        |
| `content`            | Per-template copy block: eyebrow, headline, CTAs, cards, doctors, ...     |

### Pilot category: Medical (4 archetypes)
| Archetype  | Use case                              | Hero               | Navbar         | Cards            | Conversion       | Tone           |
|------------|---------------------------------------|--------------------|----------------|------------------|------------------|----------------|
| clinic     | Multi-specialty institutional clinic  | split-booking      | solid-phone    | icon-grid 4-up   | booking-widget   | institutional  |
| family     | Pediatric / family practice           | centered-soft      | soft-pastel    | portrait-stack   | phone-and-chat   | warm-family    |
| specialist | High-end private specialist           | editorial-serif    | minimal-serif  | editorial-large  | private-request  | prestigious    |
| wellness   | Holistic / spa / osteopathy           | full-bleed-manifesto | pill-floating | pricelist        | calendar-spot    | serene         |

### How to design a new archetype
1. **Identify the buyer.** Who is shopping for this and what do they want to see in the first scroll?
2. **Pick distinct dimensions.** No two archetypes in the same category should share more than ~3 of the dimensions above.
3. **Sketch the section order.** This is the structural fingerprint — make it different.
4. **Choose imagery direction.** A photo brief, even if it ends up reusing existing pool URLs at first.
5. **Write the DNA entry** in `apps/catalog/template_dna.py`.
6. **Build the composition** at `templates/preview_compositions/<category>/<archetype>.html`. It must fit the 1600×900 viewport (the generator screenshots that exact box).
7. **Add the imagery key** in `preview_imagery.py` if you want a distinct pool.
8. **Run** `python manage.py generate_previews --force --only <slug>` and inspect the PNG.

### What NOT to call differentiation
- Same skeleton, different palette → ✗ this is what DNA exists to prevent
- Same skeleton, different fonts → ✗ same problem
- Same skeleton, different photos → ✗ same problem
- Same hero shape, different navbar colour → ✗ still feels like one product
- Different section order, different hero composition, different cards, different conversion CTA, different density → ✓ this is a distinct product
