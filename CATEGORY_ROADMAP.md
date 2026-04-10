# Category Roadmap

## MVP Categories (Phase 1)

| Priority | Category    | Slug         | Description                              | Templates / Archetypes |
|----------|-------------|--------------|------------------------------------------|-----------------|
| 1        | Agency      | agency       | Digital/creative agencies                | 2 (no DNA yet)  |
| 2        | Business    | business     | General business, corporate              | 2 (no DNA yet)  |
| 3        | Restaurant  | restaurant   | Restaurants, cafés, food delivery        | 2 (no DNA yet)  |
| 4        | **Medical** | medical      | Clinics, doctors, health practices       | **4 / 4 ✅ DNA pilot — clinic + family + specialist + wellness** |
| 5        | Lawyer      | lawyer       | Law firms, legal practices               | 2 (no DNA yet)  |
| 6        | Real Estate | real-estate  | Agencies, property listings              | 2 (no DNA yet)  |
| 7        | Portfolio   | portfolio    | Freelancers, designers, photographers    | 2 (no DNA yet)  |
| 8        | eCommerce   | ecommerce    | Online stores, product showcases         | 2 (no DNA yet)  |

### DNA migration order (Phase 2f)
1. ✅ Medical — done (Session 7)
2. Restaurant — fine-dining / trattoria-warm / street-modern (3 archetypes)
3. Agency — bold-grid / editorial-quiet / case-study-led (3 archetypes)
4. Lawyer — classic-gold / modern-transparent (2 archetypes — Lex and Juris already have very different tones)
5. Real Estate — mass-market / ultra-luxury-cinematic (2 archetypes)
6. Business, Portfolio, eCommerce — last, after the differentiation pattern is fully proven

### Per-archetype expectations
A category is considered "DNA-complete" when:
- Every published template in the category has a registered DNA entry
- Each archetype has its own composition file under `templates/preview_compositions/<category>/<archetype>.html`
- Each archetype has its own `imagery_key` (or at minimum, a different photo subset within a shared pool)
- A side-by-side listing-page screenshot shows visibly distinct previews — no two should read as the same skeleton

## Post-MVP Categories (Phase 3+)

- SaaS / Startup
- Education / School
- Fitness / Gym
- Beauty / Salon
- Event / Wedding
- Church / Nonprofit
- Construction / Architecture
- Travel / Hotel
- Blog / Magazine
- Photography Studio

## Template Count Target
- MVP: 12-20 templates across 8 categories
- V1.0: 40+ templates across 12+ categories

## Per-Template Requirements
Each template must have:
- Unique brand name
- Unique color palette (primary, secondary, accent, neutral tones)
- Unique logo concept description
- Distinct visual personality (minimal, bold, elegant, playful, etc.)
- Category-appropriate realistic content (no lorem ipsum)
- Mobile-first responsive design
- At least 3 pages: Home, About/Services, Contact
