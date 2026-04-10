# Category Roadmap

## MVP Categories (Phase 1)

| Priority | Category    | Slug         | Description                              | Templates / Archetypes |
|----------|-------------|--------------|------------------------------------------|-----------------|
| 1        | Agency      | agency       | Digital/creative agencies                | 2 (no DNA yet)  |
| 2        | Business    | business     | General business, corporate              | 2 (no DNA yet)  |
| 3        | **Restaurant** | restaurant | Restaurants, cafés, food delivery       | **3 / 3 ✅ DNA pilot — fine-dining + trattoria-warm + street-modern** |
| 4        | **Medical** | medical      | Clinics, doctors, health practices       | **4 / 4 ✅ DNA pilot — clinic + family + specialist + wellness** |
| 5        | Lawyer      | lawyer       | Law firms, legal practices               | 2 (no DNA yet)  |
| 6        | Real Estate | real-estate  | Agencies, property listings              | 2 (no DNA yet)  |
| 7        | Portfolio   | portfolio    | Freelancers, designers, photographers    | 2 (no DNA yet)  |
| 8        | eCommerce   | ecommerce    | Online stores, product showcases         | 2 (no DNA yet)  |

### DNA migration order (Phase 2f)
1. ✅ Medical — done (Session 7 — clinic / family / specialist / wellness)
2. ✅ Restaurant — done (Session 9 — fine-dining / trattoria-warm / street-modern)
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

## Template Completeness — what makes a template "complete" (Session 11)

A template is **completeness-ready** (eligible for the live multi-page preview) when it has:
1. A DNA entry in `apps/catalog/template_dna.py`
2. A content registry entry in `apps/catalog/template_content.py`
3. A per-archetype skin folder at `templates/live_templates/<category>/<archetype>/` containing all the page kinds the content registry references

When all three are in place, the template's marketplace detail page automatically shows "Apri anteprima completa" → linking to a real, navigable, multi-page website with that template's brand chrome.

### Completeness coverage (Session 11)
| Template                      | DNA | Content | Skin folder                                    | Status |
|-------------------------------|-----|---------|------------------------------------------------|--------|
| cardio-studio-specialistico   | ✅  | ✅       | medical/specialist (8 pages)                   | **Complete** |
| gusto-fine-dining             | ✅  | ✅       | restaurant/fine-dining (7 pages)               | **Complete** |
| salute-studio-medico          | ✅  | —       | medical/clinic (skin folder not yet created)   | preview-only |
| benessere-centro-olistico     | ✅  | —       | medical/wellness                               | preview-only |
| famiglia-pediatria            | ✅  | —       | medical/family                                 | preview-only |
| sapore-trattoria-pizzeria     | ✅  | —       | restaurant/trattoria-warm                      | preview-only |
| brace-street-food-lab         | ✅  | —       | restaurant/street-modern                       | preview-only |
| (all others)                  | —   | —       | —                                              | preview-only |

### Page kinds vocabulary (so far)
The page-kind names referenced in `template_content.py` map to template files. Each archetype defines which kinds it supports.

| Page kind     | Used by archetype  | Purpose                                |
|---------------|---------------------|----------------------------------------|
| `home`        | all                 | Homepage                               |
| `about`       | specialist · fine-dining | About / philosophy                |
| `services`    | specialist          | Services list (medical visits)         |
| `team`        | specialist          | Doctors / staff                        |
| `blog_list`   | specialist · fine-dining | List of articles                  |
| `blog_detail` | specialist · fine-dining | Single article (full body)        |
| `contact`     | specialist          | Contact info + form                    |
| `appointment` | specialist          | Appointment / consultation request form |
| `menu`        | fine-dining         | Restaurant menu                        |
| `gallery`     | fine-dining         | Gallery / atmosphere                   |
| `reservations`| fine-dining         | Reservation form + concierge           |

Each NEW archetype is free to introduce new page kinds (e.g. an `agency` archetype might add `case_studies`, an `ecommerce` one might add `shop`).
