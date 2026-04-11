# Category Roadmap

## 🛑 Session 16 audit severity (2026-04-11) — see D-049, Phase 2g2x is blocking

## MVP Categories (Phase 1)

| Priority | Category    | Slug         | Description                              | Templates / Archetypes | **Audit severity** |
|----------|-------------|--------------|------------------------------------------|-----------------|--------------------|
| 1        | Agency      | agency       | Digital/creative agencies                | 2 (no DNA) — vertex + aura share `agency.html` with 6 fake case-study literals  | **CRITICO** (identity crash) |
| 2        | Business    | business     | General business, corporate              | 2 (no DNA) — pragma + elevate share `business.html` with hardcoded `"Hanno scelto Pragma"` label + Marco Bianchi testimonial | **CRITICO** (identity crash) |
| 3        | Restaurant  | restaurant | Restaurants, cafés, food delivery       | 3 / 3 ✅ DNA pilot — fine-dining + trattoria-warm + street-modern, all visually distinct at card | **MEDIO** (latent D-047 leaks in trattoria-warm preview comp + 5 Gusto leak files in fine-dining live skin; Phase 2g.3 absorbed into Phase 2g2x.3) |
| 4        | Medical     | medical      | Clinics, doctors, health practices       | 5 / 4 ✅ DNA pilot — clinic + family + specialist ×2 + wellness (specialist hosts cardio + dermatologia-elite-roma) | **MEDIO** (cardio+derm share specialist hero imagery which is from lawyer pool 5/6 overlap; `medical-family` pool 100% overlaps with `medical` pool; latent single-tenant leak in `medical/family.html` preview comp) |
| 5        | Lawyer      | lawyer       | Law firms, legal practices               | 2 (no DNA) — lex + juris share `lawyer.html` hardcoding "Studio legale dal 1962 · Roma · Milano" | **CRITICO** (identity crash — Juris modern template renders Lex's 60-year heritage) |
| 6        | Real Estate | real-estate  | Agencies, property listings              | 2 (no DNA) — casa + villa share `real-estate.html` with "600+ immobili · €500K–€1.2M" mass-market search box | **CRITICO** (identity crash — Villa ultra-luxury renders mass-market copy) |
| 7        | Portfolio   | portfolio    | Freelancers, designers, photographers    | 2 (no DNA) — chiara + pixel share `portfolio.html` hardcoding "Sono una designer indipendente" | **CRITICO** (identity crash — Pixel photographer renders Chiara's designer identity) |
| 8        | eCommerce   | ecommerce    | Online stores, product showcases         | 2 / 2 ✅ DNA pilot — luxe (fashion-editorial) + bottega (artisan-workshop), Session 15 macro-tone split | **MEDIO** (latent — `fashion-editorial.html` has 12+ Luxe literals; `artisan-workshop.html` has 10+ Bottega literals. Will detonate on Phase 2f.2 reuse) |

**Completeness coverage (preview vs full multi-page):**
- **Full multi-page websites:** 3 of 20 templates (cardio, dermatologia-elite-roma via specialist reuse, gusto)
- **Preview-PNG-only templates:** 17 of 20. Marketplace positions as "complete multipage websites" but 85% of the catalog ships as single-page posters. See Phase 2g2x.4 for the tiering/demotion decision.

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

### Specialist copy-abstraction lift (Session 14) — Phase 2g.2 CLOSED
The 17 cardio-specific literal leaks in the specialist chrome identified by Session 13 are **all removed**. The chrome is now editorially reusable — a third specialist template (e.g. `ortopedia-studio-privato`) can ship with ONLY a seed row + DNA entry + content block. All 25 routes (Cardio 9 + Derm 9 + Gusto 7) remain 200. Zero cardio-specific literal leaks detected in rendered dermatologia HTML after the lift.

Specific fixes:
- `_base.html` — `site.license` and `site.hours_footer_rows` now drive the footer strap and day rows
- `home.html` — hero right sidebar (quote, author, pulse triple, top label), chief portrait URL, all section labels and headings, and CTA all from `page_data.*`
- `about.html` — values label/heading + CTA band heading/labels from `page_data.*`
- `services.html` — brand-name leak (`Studio Marani`) removed via `visite.cta_heading`; footnote heading + CTA labels abstracted
- `team.html` — `nth-child` portrait CSS rules deleted; per-doctor inline styles with `d.portrait`; portrait signature reads `d.portrait_city|default:medici.portrait_city`; **3-doctor cap removed**
- `blog_list.html` + `blog_detail.html` — hardcoded `'pubblicazioni'` slug replaced with `blog_parent_slug` context variable computed in `LiveTemplateView.get_context_data()`. D-044's hard constraint is lifted (**see D-048**). Lead image + footer strap + empty-body fallback all from content.
- `contact.html` — form placeholders from `contatti.form_placeholders` dict; sidebar headings from `contatti.hours_heading`/`transport_heading`
- `appointment.html` — hand-written form replaced with a generic `{% for f in page_data.form_fields %}` loop; `form_fields` reshaped to dicts with `options` for selects and `full_width` for row spans

**New formal decision:** D-047 — Chrome-Authoring Contract. Every string in a per-archetype skin must be a CSS rule, a generic archetype label, a `{{ context.var }}`, or a `{% for %}` loop item. Applied from the first authoring pass of any new skin, this eliminates the need for any follow-up lift pass.

**Next:** Phase 2g.3 — repeat the same lift on `templates/live_templates/restaurant/fine-dining/`. Add a second fine-dining template (e.g. `tartufo-truffle-house`) and run the leak-audit sweep on Gusto-specific strings. See TODO_NEXT.md Phase 2g.3.

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
