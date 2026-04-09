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
