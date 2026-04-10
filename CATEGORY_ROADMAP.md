# Category Roadmap

## MVP Categories (Phase 1)

| Priority | Category    | Slug         | Description                              | Templates / Archetypes |
|----------|-------------|--------------|------------------------------------------|-----------------|
| 1        | Agency      | agency       | Digital/creative agencies                | 2 (no DNA yet)  |
| 2        | Business    | business     | General business, corporate              | 2 (no DNA yet)  |
| 3        | **Restaurant** | restaurant | Restaurants, cafés, food delivery       | **3 / 3 ✅ DNA pilot — fine-dining + trattoria-warm + street-modern** |
| 4        | **Medical** | medical      | Clinics, doctors, health practices       | **5 / 4 ✅ DNA pilot — clinic + family + specialist ×2 + wellness (specialist archetype now hosts cardio + dermatologia-elite-roma, reuse validated)** |
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

### Completeness coverage (Session 13 — archetype reuse validation)
| Template                      | DNA | Content | Skin folder                                    | Status |
|-------------------------------|-----|---------|------------------------------------------------|--------|
| cardio-studio-specialistico   | ✅  | ✅       | medical/specialist (8 pages)                   | **Complete** |
| dermatologia-elite-roma       | ✅  | ✅       | medical/specialist (REUSED · 8 pages · 0 new HTML) | **Complete (reuse)** |
| gusto-fine-dining             | ✅  | ✅       | restaurant/fine-dining (7 pages)               | **Complete** |
| salute-studio-medico          | ✅  | —       | medical/clinic (skin folder not yet created)   | preview-only |
| benessere-centro-olistico     | ✅  | —       | medical/wellness                               | preview-only |
| famiglia-pediatria            | ✅  | —       | medical/family                                 | preview-only |
| sapore-trattoria-pizzeria     | ✅  | —       | restaurant/trattoria-warm                      | preview-only |
| brace-street-food-lab         | ✅  | —       | restaurant/street-modern                       | preview-only |
| (all others)                  | —   | —       | —                                              | preview-only |

### Archetype reuse validation result (Session 13)
Adding `dermatologia-elite-roma` under the `specialist` archetype required only:
1. One new row in `apps/catalog/management/commands/seed_templates.py`
2. One new DNA entry in `apps/catalog/template_dna.py`
3. One new content block in `apps/catalog/template_content.py`
**Zero new HTML files.** All 9 routes (marketplace detail + 7 inner preview pages + 1 post detail) return 200. The specialist chrome renders with the new brand palette, fonts, copy, doctors, press list, and services.

**Confirmed leaks in the specialist chrome** that a second template cannot override via content alone — logged under Session 13 in SESSION_LOG.md and DECISIONS.md D-046. These bake cardio-specific text directly into HTML:
- `_base.html:240` — `OMCeO Roma 12 / 4408` (footer license, appears on EVERY page)
- `home.html:199-205` — `«La cardiologia non è una catena...»` quote, `Lancet · 2024`, `Roma · Parioli`, `2010`, `Cardiologia clinica` pulse band
- `services.html:100` — `Una visita allo Studio Marani è concordata personalmente` (brand name baked in)
- `team.html:87` — `Roma · Parioli` portrait signature (every doctor card)
- `team.html:70-72` — 3 hardcoded Unsplash portrait URLs (caps the archetype at 3 doctors and re-uses cardio's photos)
- `blog_detail.html:120` — `Studio Marani · Cardiologia clinica` footer
- blog parent slug is hardcoded to `pubblicazioni` in blog_list + blog_detail URL reverses

The validation succeeded as a structural reuse proof but revealed the chrome needs a **copy-abstraction pass** before more specialist templates can ship cleanly. See TODO_NEXT.md Phase 2g.2 for the lift-copy-to-content-or-site plan.

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
