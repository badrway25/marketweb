# Agent Handoff

Last updated: 2026-04-10 — after Restaurant Pilot Phase 2f.1 (Session 9)

## Current State

**Template DNA System now has TWO validated category pilots: Medical (4 archetypes) and Restaurant (3 archetypes).** Templates inside the same category are no longer recolors of each other — each one has a unique "DNA" (archetype + hero/navbar/footer/cards/conversion/density/tone) that drives a bespoke HTML composition.

- **Medical** pilot: 4 genuinely distinct templates (clinic, family, specialist, wellness), validated on `/templates/medical/`
- **Restaurant** pilot: 3 genuinely distinct templates (fine-dining, trattoria-warm, street-modern), validated on `/templates/restaurant/`

Branch: `restaurant-template-pilot` worktree (built on top of `medical-pilot-fix` → `template-dna-system`, **none merged to master yet**).

## Session 9 — Restaurant Pilot Phase 2f.1

Replicated the medical DNA pilot for the Restaurant category. Three brand-new HTML compositions, three distinct imagery pools, one new seed template, full visual verification.

| Layer            | Before                                          | After                                                                       |
|------------------|-------------------------------------------------|-----------------------------------------------------------------------------|
| Restaurant templates | 2 (Gusto, Sapore)                           | 3 (added Brace — Street Food Lab)                                           |
| Restaurant archetypes | 1 (legacy fallback only)                   | 3 (fine-dining, trattoria-warm, street-modern)                              |
| Restaurant compositions | 1 (legacy `restaurant.html`)             | 4 (legacy + 3 new under `restaurant/<archetype>.html`)                      |
| Restaurant imagery pools | 1 (`restaurant`)                         | 4 (`restaurant`, `restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) |
| Total templates  | 18                                              | 19                                                                          |

The DNA system is still **strictly additive** — templates without a DNA entry continue to render via the legacy per-category composition. The legacy `templates/preview_compositions/restaurant.html` is retained as a safety net for any future restaurant template not yet pulled into an archetype.

## What makes the 3 restaurant templates genuinely different (not recolors)

| Slug                       | Archetype       | Hero                  | Navbar         | Cards            | Conversion              | Tone           | Display Font           |
|----------------------------|-----------------|-----------------------|----------------|------------------|-------------------------|----------------|------------------------|
| gusto-fine-dining          | fine-dining     | editorial-plate       | serif-centered | course-index     | concierge-reservation   | editorial-chef | Playfair Display       |
| sapore-trattoria-pizzeria  | trattoria-warm  | warm-photo-frame      | warm-bar       | chalkboard-day   | phone-and-whatsapp      | familiar-warm  | Caveat (handwritten)   |
| brace-street-food-lab      | street-modern   | product-cutout        | bold-pill      | product-grid     | order-now-delivery      | energetic-bold | Big Shoulders Display  |

Differences span page background colour family, navbar shape and position, hero composition (editorial split-plate vs polaroid + handwritten manifesto vs giant condensed display + tilted product cutout), card stride (5-row Roman-numeral course list vs 5-day chalkboard daily specials vs 4-up product grid with corner badges), button language (gold-underline serif ghost vs rustic rounded with shadow + tilt vs brutalist block-bold with hard offset shadow), density (very-airy → medium → compact), and copy tone (editorial chef → familiar warm → energetic bold).

## What's Working

| Page                          | URL                                        | Status (port 8101) |
|-------------------------------|--------------------------------------------|--------------------|
| Homepage featured grid        | `/`                                        | Salute (clinic), Pragma, Vertex, Lex, Chiara, Gusto in featured grid |
| Template listing (all)        | `/templates/`                              | 19 templates × paginated |
| Template listing (medical)    | `/templates/medical/`                      | 4 medical templates × 4 visibly different archetypes (regression OK) |
| Template listing (restaurant) | `/templates/restaurant/`                   | 3 restaurant templates × 3 visibly different archetypes |
| Template detail (each restaurant) | `/templates/restaurant/<slug>/`        | Gallery shows the new archetype PNG |
| Template detail (each medical)| `/templates/medical/<slug>/`               | Gallery shows the new archetype PNG |

## How the DNA system works

```
apps/catalog/template_dna.py
  ├── Vocabulary dicts: LAYOUT_ARCHETYPES, HERO_STYLES, NAVBAR_STYLES,
  │                     FOOTER_STYLES, CARD_STYLES, BUTTON_STYLES,
  │                     DENSITY_PROFILES, TONES, CONVERSION_PATTERNS,
  │                     IMAGERY_DIRECTIONS
  ├── TEMPLATE_DNA: dict[slug, dna]  # the registry (7 entries: 4 medical + 3 restaurant)
  └── get_dna(slug), has_dna(slug)

apps/catalog/templatetags/preview_extras.py
  └── `at` filter — `{{ imagery|at:forloop.counter }}` for safe loop indexing

apps/catalog/preview_imagery.py
  └── Per-archetype keys:
      • medical-family / medical-specialist / medical-wellness  (recycle existing URLs, offline-safe)
      • restaurant-fine / restaurant-trattoria / restaurant-street  (fully-distinct URL sets)

apps/catalog/management/commands/generate_previews.py
  ├── _resolve_composition(template, dna)
  │     → with DNA: preview_compositions/<category>/<archetype>.html
  │     → without:  preview_compositions/<category>.html
  ├── Pre-warms imagery by *imagery_key*, not just category slug
  └── DNA's `font_pairing` overrides brand.typography parsing

templates/preview_compositions/medical/
  ├── clinic.html      — institutional, split-hero with booking widget, 4-up icons
  ├── family.html      — pastel pill nav, organic-shape portrait, intro trio + hours strip
  ├── specialist.html  — minimal serif nav, editorial headline, drop cap, 01/02 fields, press band
  └── wellness.html    — full-bleed hero, glass pill nav, dotted-leader pricelist, therapists strip

templates/preview_compositions/restaurant/
  ├── fine-dining.html    — centered serif wordmark, editorial split-plate, course index, concierge tile, press strip
  ├── trattoria-warm.html — cream warm-bar nav, polaroid photo card, Caveat handwritten manifesto, chalkboard daily specials, family + hours band
  └── street-modern.html  — black floating pill nav, giant condensed display + tilted product cutout + price badge, 4-up product grid, delivery strip
```

Run with `python manage.py generate_previews [--force] [--only <slug>]`.

## Database State

- 8 categories (unchanged)
- **19** templates (was 18; +1 restaurant: brace-street-food-lab)
- 19 brands
- 19 preview assets — 4 medical + 3 restaurant now use the new per-archetype compositions
- ~70 cached source photos across 11 pools (3 new restaurant pools added in Session 9)

## For Next Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, TODO_NEXT.md, this file, then `apps/catalog/template_dna.py` (the source of truth for differentiation), then peek at `templates/preview_compositions/restaurant/` and `medical/` for the structural reference compositions.

### Watch out for the Session 8/9 timing trap (still unfixed)
When you add a DNA entry to a slug that *already* has a generated preview, that preview was rendered through the legacy fallback and is now stale. The `generate_previews` "skip if exists" branch will not regenerate it. Always run `python manage.py generate_previews --force --only <slug>` after creating or modifying a DNA entry for an existing template — **AND** delete the canonical-named PNG file on disk first, otherwise Django storage will append a random suffix to the new file (the DB row will still point correctly to the suffixed file, so functionally fine, but the disk gets cluttered with orphans).

The clean recipe used in Session 9 to avoid the orphan trap:
```bash
# 1. Delete the row + canonical file + any suffixed file via a small Django shell snippet
python -c "import django, os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','marketweb.settings'); django.setup(); ..."
# 2. Then re-run WITHOUT --force so the new file lands at the canonical name (no collision)
python manage.py generate_previews --only <slug>
```

### Immediate next step (highest impact)
**Replicate the DNA pilot for the Agency category.** Same recipe:

1. Open `apps/catalog/template_dna.py` and add 3 entries: vertex-creative-agency → `bold-grid`, aura-digital-studio → `editorial-quiet`, plus 1 NEW template `case-study-led` (e.g. a strategy/branding agency that leads with case studies).
2. Add the new template to `apps/catalog/management/commands/seed_templates.py`.
3. Create `templates/preview_compositions/agency/bold-grid.html`, `agency/editorial-quiet.html`, `agency/case-study-led.html`. Use the **restaurant** and **medical** files as the structural reference — each must have a completely different hero, navbar, cards, and footer composition.
4. Add 3 new imagery keys (`agency-bold`, `agency-editorial`, `agency-cases`) in `preview_imagery.py`. The restaurant pilot taught us that fully-distinct URL sets produce noticeably better differentiation than recycling — copy that approach.
5. Choose multi-weight Google Fonts only (`_base.html` requests `wght@500;600;700;800` and Google Fonts CSS2 returns 400 if no requested weight exists). Big Shoulders Display, Playfair Display, Caveat, Space Grotesk, DM Sans, Manrope are all safe.
6. Use the clean delete + regenerate-without-force recipe above for any existing slug that gains DNA.
7. Verify with Playwright at `/templates/agency/`.

### Phase 2d polish (still pending from previous sessions)
1. Optimize PNG file sizes (~4 MB → ~500 KB via Pillow `optimize=True` or oxipng)
2. Cormorant Garamond on dark backgrounds reads thin (Lex, Villa, Cardio specialist) — consider bumping weight or swapping serif at low luminance
3. Add `media/preview_imagery/` to .gitignore
4. **DNA-fallback timing trap safety net** — see TODO_NEXT.md for options (a/b/c)
5. **`--force` orphan cleanup** — auto-delete the canonical file before saving so Django storage doesn't suffix
6. **Imagery URL validation** — Session 9 hit one HTTP 404 from Unsplash; a `--validate-imagery` flag would catch these before a full regeneration run

### Phase 3 (Interactivity & Accounts) — unchanged
1. Tag seeding and filtering
2. User authentication views
3. Commerce flow
4. Editor + projects integration
5. Live demo iframe per template

### Key Files for the DNA System
- `apps/catalog/template_dna.py` — DNA registry + vocabulary (the source of truth)
- `apps/catalog/templatetags/preview_extras.py` — `at` filter for image indexing in loops
- `apps/catalog/preview_imagery.py` — `IMAGERY_CONFIG` with per-archetype keys
- `apps/catalog/management/commands/generate_previews.py` — DNA-aware pipeline
- `templates/preview_compositions/<category>/<archetype>.html` — bespoke per-template HTML
- `templates/preview_compositions/<category>.html` — legacy fallback for non-DNA templates

### Constraints (unchanged)
- Do not redesign architecture or model structure
- Preserve premium UI — listing/detail/card templates should not be modified for preview changes
- Follow services/selectors pattern for new business logic
- Italian content (D-016)
- Update coordination files at end of session

## Coordination Rules

- Backend-core owns: models, migrations, admin, services, selectors, management commands
- Premium-UI owns: templates/, static/, design system, frontend components
- **Real-preview-assets** owns: `apps/catalog/preview_imagery.py`, `apps/catalog/management/commands/generate_previews.py`, `templates/preview_compositions/`
- **Template-DNA-system** owns: `apps/catalog/template_dna.py`, `apps/catalog/templatetags/preview_extras.py`, `templates/preview_compositions/<category>/<archetype>.html` files
- **DNA-pilot sessions** (medical, restaurant, ...) own per-category vocabulary additions in `template_dna.py`, the per-category composition folder, and the matching imagery pool keys
- All sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md, TEMPLATE_REGISTRY.json, BRAND_SYSTEM_GUIDELINES.md, CATEGORY_ROADMAP.md at end
