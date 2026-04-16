# Category Roadmap

## ✅ MVP CHIUSO (Session 53, 2026-04-15) — 20/20 published_live, 8 categorie chiuse · ✅ Phase 3 unblock gate MET
## 🆕 Strategia di espansione (Session 54, 2026-04-15) — vedi `CATALOG_EXPANSION_STRATEGY.md` + `PROFESSION_PRESET_TAXONOMY.md` + D-083/D-084/D-085

### Catalogo target medio termine (Phase A-F): 14 categorie · 28-30 archetypi · 75-90 preset professionali
La roadmap si sposta da "altri template autoriali" a "**editor-first + preset-driven expansion**". Phase A (Editor Foundation v1) è la priorità assoluta. Phase B (Trades + Local-food retail) apre il primo set di nuove categorie con 6 nuovi archetypi + 24-30 nuovi preset.

### Categorie top-level proposte (medio termine: 14)
1. ✅ **Medical & Care** — esistente, 5/5 live, archetypi: clinic · specialist · wellness · family · (opz pharmacy)
2. ✅ **Restaurant & Food** — esistente, 3/3 live, archetypi: fine-dining · trattoria-warm · street-modern · (opz bistro-modern)
3. ✅ **Business** — esistente, 2/2 live, archetypi: corporate-suite · startup-saas-landing
4. ✅ **Agency** — esistente, 2/2 live, archetypi: agency-creative-studio · agency-digital-studio
5. ✅ **Lawyer** — esistente, 2/2 live, archetypi: classic-gold · modern-transparent
6. ✅ **Real Estate** — esistente, 2/2 live, archetypi: mass-market · ultra-luxury-cinematic
7. ✅ **Portfolio** — esistente, 2/2 live, archetypi: editorial-designer-grid · cinematic-photographer
8. ✅ **eCommerce** — esistente, 2/2 live, archetypi: artisan-workshop · fashion-editorial
9. 🆕 **Hotel & Hospitality** (`hospitality`) — 4 archetypi nuovi: boutique-hotel · b&b-warm · agriturismo-rurale · resort-luxury
10. 🆕 **Local Food Retail** (`food-retail`) — 3 archetypi nuovi: bakery-warm · deli-counter · artisan-food-shop
11. 🆕 **Automotive Services** (`automotive`) — 3 archetypi nuovi: garage-trust · bodyshop-clean · dealership-showroom
12. 🆕 **Home Services & Trades** (`trades`) — 3 archetypi nuovi: single-trade-pro · multi-trade-team · emergency-pro
13. 🆕 **Personal Services & Beauty** (`beauty`) — 3 archetypi nuovi: salon-fashion · barber-classic · aesthetic-spa
14. 🆕 **Wellness & Fitness** (`wellness-fit`) — 3 archetypi nuovi: gym-strength · yoga-studio-soft · boutique-fitness-bold
15. 🆕 **Professional Services** (`professional`) — 3 archetypi nuovi: consultant-advisory · accountant-trust · notary-institutional
16. 🆕 **Education & Training** (`education`) — 3 archetypi nuovi: language-school-bright · vocational-academy-pro · private-tutor-warm
17. 🆕 **Events & Wedding** (`events`) — 2-3 archetypi nuovi: wedding-romantic · event-planner-corporate · (opz catering-events-warm)

(Le ultime 9 categorie aprono progressivamente in Phase B-F; vedi `CATALOG_EXPANSION_STRATEGY.md` §9 per la sequenza.)

### Sequenza rollout post-MVP (Phase A-G)
| Phase | Contenuto | Archetypi nuovi | Preset nuovi | Categorie nuove | Mesi |
|-------|-----------|-----------------|--------------|------------------|------|
| **A** — Editor Foundation v1 | Apre `apps/editor/` su 20 template attuali | 0 | 0 | 0 | 2-3 |
| **B** — Trades + Food retail | Prima ondata mestieri italiani locali | 6 | 24-30 | 2 | 2 |
| **C** — Beauty + Wellness-fit | Servizi alla persona | 6 | 16-20 | 2 | 2 |
| **D** — Hospitality + Automotive | Servizi turistici e auto | 7 | 16-20 | 2 | 2 |
| **E** — Professional + Education | Knowledge economy + formazione | 6 | 16-20 | 2 | 2 |
| **F** — Events + MVP extension | Eventi + preset estensione 8 cat MVP | 3 | 25-37 | 1 | 2 |
| **G** — Tier monetization + commerce extensions | Tier free/pro/business + Stripe Connect + multi-storefront | 0 | 0 | 0 | 2-3 |

**Decisione binding (D-085):** nessun nuovo template `published_live`, nessun nuovo archetypo, nessuna nuova categoria viene aperta finché Phase A non è chiusa.

---

## 🛑 Session 16 audit severity (2026-04-11) — see D-049, Phase 2g2x is blocking [STORICO — chiuso da Session 53]

## MVP Categories (Phase 1)

| Priority | Category    | Slug         | Description                              | Templates / Archetypes | **Audit severity** |
|----------|-------------|--------------|------------------------------------------|-----------------|--------------------|
| 1        | Agency      | agency       | Digital/creative agencies                | 2 / 2 ✅ all live (Session 49) — agency-creative-studio (Vertex editorial) + agency-digital-studio (Aura midnight-violet product), all 5-locale + RTL, sharp D-054 differentiation | **CHIUSA** (Phase 2g3.6f closed Session 49 — Vertex + Aura flipped to published_live, agency 2/2 live) |
| 2        | Business    | business     | General business, corporate              | 2 (no DNA) — pragma + elevate share `business.html` with hardcoded `"Hanno scelto Pragma"` label + Marco Bianchi testimonial | **CRITICO** (identity crash) |
| 3        | Restaurant  | restaurant | Restaurants, cafés, food delivery       | 3 / 3 ✅ all live (Session 48) — fine-dining + trattoria-warm + street-modern, all 5-locale + RTL, sharp D-054 differentiation | **CHIUSA** (Phase 2g3.6 closed Session 48 — Sapore + Brace flipped to published_live, restaurant 3/3 live) |
| 4        | Medical     | medical      | Clinics, doctors, health practices       | 5 / 5 ✅ all live (Session 51) — cardio + dermatologia (specialist) + salute (clinic) + benessere (wellness) + famiglia (family), all 5-locale + RTL, 3 disjoint Pexels pools, D-054 10/10 on 9 sibling pairs | **CHIUSA** (Phase 2g3.2 closed Session 51 — Salute/Benessere/Famiglia flipped to published_live, medical 5/5 live) |
| 5        | Lawyer      | lawyer       | Law firms, legal practices               | 2 / 2 ✅ all live (Session 53) — classic-gold (Lex, ink+gold forensic ledger) + modern-transparent (Juris, slate+blue advisory sprint), all 5-locale + RTL, sharp D-054 differentiation | **CHIUSA** (Phase 2g3.7 closed Session 53 — Lex + Juris flipped to published_live, lawyer 2/2 live) |
| 6        | Real Estate | real-estate  | Agencies, property listings              | 2 / 2 ✅ all live (Session 53) — mass-market (Casa, Poppins daylight search-grid) + ultra-luxury-cinematic (Villa, Cormorant fullbleed editorial concierge), all 5-locale + RTL, sharp D-054 differentiation | **CHIUSA** (Phase 2g3.7 closed Session 53 — Casa + Villa flipped to published_live, real-estate 2/2 live) |
| 7        | Portfolio   | portfolio    | Freelancers, designers, photographers    | 2 (no DNA) — chiara + pixel share `portfolio.html` hardcoding "Sono una designer indipendente" | **CRITICO** (identity crash — Pixel photographer renders Chiara's designer identity) |
| 8        | eCommerce   | ecommerce    | Online stores, product showcases         | 2 / 2 ✅ DNA pilot — luxe (fashion-editorial) + bottega (artisan-workshop), Session 15 macro-tone split | **MEDIO** (latent — `fashion-editorial.html` has 12+ Luxe literals; `artisan-workshop.html` has 10+ Bottega literals. Will detonate on Phase 2f.2 reuse) |

**Completeness coverage (preview vs full multi-page) — updated Session 53:**
- **Full multi-page websites:** **20 of 20 templates** ✅ CATALOG COMPLETE — cardio, dermatologia (specialist reuse), gusto-fine-dining, pragma-corporate-suite, elevate-startup-landing, chiara-portfolio-creativo, pixel-portfolio-fotografico, bottega-shop-artigianale, luxe-fashion-store, sapore-trattoria-pizzeria, brace-street-food-lab, vertex-creative-agency, aura-digital-studio, salute-studio-medico, benessere-centro-olistico, famiglia-pediatria, **lex-studio-legale, juris-avvocato-moderno, casa-agenzia-immobiliare, villa-immobili-lusso** — all 20/20 multilingual (5 locales + RTL).
- **Preview-PNG-only templates:** 0 of 20 — no draft slugs remaining. Phase 3 unblock gate met.

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

## Baseline live pages per category (Session 20 — D-053)

Per D-053 Live Preview Law, a template may only be `published_live` when its skin folder covers the full category baseline below. These are the **minimum** page kinds — an archetype is free to add more, but not to ship with fewer. Every page kind in the baseline must be backed by real content in `template_content.py` (no stub pages).

| Category       | Baseline page kinds (minimum set)                                                                                          | Detail page kind? | Total pages (min) |
|----------------|----------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|
| Medical        | `home`, `about` (studio), `services` (visite/reparti/percorsi), `team` (medici), `contact` + one of `appointment` / `blog_list`+`blog_detail` | blog_detail where blog exists | 5 pages + 1 detail |
| Restaurant     | `home`, `about` (filosofia/storia), `menu`, `gallery` (atmosfera), `contact` or `reservations`                              | —                 | 5 pages            |
| Business       | `home`, `about`, `services` (advisory pillars / product tour), `case_studies` or `pricing`, `contact`                       | case_study_detail for corporate-suite; pricing static for startup-saas-landing | 5 pages + 1 detail (corporate side) |
| Agency         | `home`, `about` (studio), `services`, `case_studies` (work list), `contact`                                                 | case_study_detail (at least one)    | 5 pages + 1 detail |
| Lawyer         | `home`, `about` (studio), `practice_areas`, `team` (avvocati), `contact`                                                    | —                 | 5 pages            |
| Real Estate    | `home`, `listings`, `about` (agenzia), `contact` + one of `neighborhoods` / `sell_with_us`                                  | property_detail (at least one)      | 5 pages + 1 detail |
| Portfolio      | `home`, `about` (studio/biografia), `work` (projects/series index), `contact` + one of `blog_list`+`blog_detail` / `process`| project_detail or series_detail (at least one) | 5 pages + 1 detail |
| eCommerce      | `home`, `shop` (catalogo/collezione), `about` (bottega/atelier), `contact` or `appointment`                                 | product_detail (at least one)       | 5 pages + 1 detail |

**Minimum shape:** 5 navigable pages + (for categories where the product IS drilldown) at least one fully-authored detail page. Landing-page-only templates do NOT qualify as `published_live`.

**Navigation rule:** the baseline pages must be reachable from the top-level nav of the live skin `_base.html`. A page that exists in the content registry but isn't linked from the nav counts as hidden and breaks the navigation test.

## Rollout order — Phase 2g3 (Session 20)

Templates flip from `draft` to `published_live` category-by-category, cheapest-first. The order below minimizes new HTML work by reusing DNA + preview compositions that already exist:

1. **Restaurant** (2 templates: Sapore, Brace) — DNA + preview compositions exist, 2 new skin folders. Smallest lift.
2. **Medical** (3 templates: Salute, Benessere, Famiglia) — DNA + preview compositions exist, 3 new skin folders.
3. **Business** (2 templates: Pragma, Elevate) — DNA + preview compositions exist (Session 17), 2 new skin folders.
4. **Portfolio** (2 templates: Chiara, Pixel) — DNA + preview compositions exist (Session 18 + 19 triage), 2 new skin folders.
5. **Ecommerce** (2 templates: Bottega, Luxe) — DNA + preview compositions exist (Session 15), 2 new skin folders. **Blocked by Phase 2g2x.3 leak lifts** (12+ Luxe + 10+ Bottega latent literals in preview comps).
6. **Agency / Lawyer / Real-estate** (6 templates) — **blocked by Phase 2g2x.1 closure.** After 2g2x.1 ships 2 archetypes per category, 2g3.6 authors 6 new skin folders. Sub-order: real-estate → lawyer → agency (per AGENT_HANDOFF Session 19 guidance — cleanest pair first, heaviest leak surface last).

**Cumulative `published_live` count milestone:**
- Session 32 (Phase 2g3.3 — business): 5
- Session 34 (Phase 2g3.4 — portfolio): 7
- Session 41 (Phase 2g3.5 — ecommerce): 9
- Session 48 (Phase 2g3.6 — restaurant sapore + brace): 11
- Session 49 (Phase 2g3.6f — agency vertex + aura): 13
- Session 51 (Phase 2g3.2 — medical salute + benessere + famiglia): 16
- Session 53 (Phase 2g3.7 — lawyer lex+juris + real-estate casa+villa): **20** ← today, 20/20 multilingual ✅ CATALOG COMPLETE

**Phase 3 unblock gate:** Phase 2g3.7 fully green (all 20 templates `published_live`). ✅ MET — Session 53 flipped the final 4 draft slugs. Phase 3 (auth / checkout / editor / projects / commerce) is now unblocked.

## Category-ready test (Session 20)

A category is considered **`published_live`-complete** when:
1. Every sibling template in the category is tier `published_live`
2. The D-054 10-gate Premium Differentiation Law passes on every sibling pair (bidirectional)
3. The D-047 bidirectional leak sweep returns zero cross-tenant literals across the live skin folder(s)
4. A Chromium walk at 1440×900 confirms the category listing reads as N distinct products (not recolor siblings), and clicking each card leads to a complete, navigable website
5. The category listing page is no longer showing the "in arrivo" empty strip (per D-055 it's empty until N≥1; per this test it's green when N = category's seeded count)

Only categories that pass this test contribute to the Phase 3 unblock gate.
