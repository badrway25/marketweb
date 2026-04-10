# Agent Handoff

Last updated: 2026-04-10 — after Restaurant Pilot Fix Pass (Session 10)

## Current State

**Template DNA System now has TWO validated category pilots: Medical (4 archetypes) and Restaurant (3 archetypes).** Templates inside the same category are no longer recolors of each other — each one has a unique "DNA" (archetype + hero/navbar/footer/cards/conversion/density/tone) that drives a bespoke HTML composition.

- **Medical** pilot: 4 genuinely distinct templates (clinic, family, specialist, wellness), validated on `/templates/medical/`
- **Restaurant** pilot: 3 genuinely distinct templates (fine-dining, trattoria-warm, street-modern), **Session 9 shipped weak Gusto/Sapore differentiation; Session 10 fixed it** — Gusto now fully DARK editorial, Sapore now fully BRIGHT cream scrapbook, Brace untouched

Branch: `restaurant-template-pilot` worktree (built on top of `medical-pilot-fix` → `template-dna-system`, **none merged to master yet**).

## Session 10 — Restaurant Pilot Fix Pass

Visual review of Session 9 found that **only Brace was clearly distinct**. Gusto and Sapore had two overlapping problems:

1. **Imagery overlap**: `restaurant-fine` and `restaurant-trattoria` pools shared 5 of 6 URLs (only the hero differed). Session 9's claim of "fully-distinct URL sets" was wrong — only Brace's pool was actually distinct.
2. **Same macro silhouette**: both compositions were "cream paper top + dark band bottom". At thumbnail size the dark/cream split dominated and made them read as the same skeleton.

### Fix applied
- **Imagery pools**: both `restaurant-fine` and `restaurant-trattoria` rebuilt with 6 hand-checked URLs each, **zero overlap**. Fine got 6 dark plated dish photos. Trattoria got 6 bright sunny rustic photos. Each candidate was downloaded and visually inspected via the Read tool before committing — caught one clothing-store image and replaced it.
- **`restaurant/fine-dining.html` rewritten**: pivoted from cream-paper to **fully dark charcoal page** (no cream anywhere, no contrast band, full-bleed plate close-up hero, italic Playfair throughout, course list on the same dark background separated only by hairline gold rules).
- **`restaurant/trattoria-warm.html` rewritten**: pivoted from cream-with-dark-chalkboard to **fully bright cream page** (no dark areas at all, two stacked tilted polaroid scrapbook photos with washi tape, huge Caveat handwritten headline, cream washi-tape recipe card replacing the dark chalkboard, no dark hours band).
- **Brace left untouched** — already strongly distinct (yellow brutalist).

Result: 3 cards now occupy three opposite ends of the visual spectrum — dark editorial / bright handwritten / yellow brutalist.

## Session 9 — Restaurant Pilot Phase 2f.1 (superseded by Session 10 fix for Gusto/Sapore)

Replicated the medical DNA pilot for the Restaurant category. Three brand-new HTML compositions, three distinct imagery pools, one new seed template. Visually validated — but the Session 9 imagery pool was wrong (5/6 URL overlap between fine and trattoria) and the compositions had structurally similar bottom dark bands. Both fixed in Session 10.

| Layer            | Before                                          | After                                                                       |
|------------------|-------------------------------------------------|-----------------------------------------------------------------------------|
| Restaurant templates | 2 (Gusto, Sapore)                           | 3 (added Brace — Street Food Lab)                                           |
| Restaurant archetypes | 1 (legacy fallback only)                   | 3 (fine-dining, trattoria-warm, street-modern)                              |
| Restaurant compositions | 1 (legacy `restaurant.html`)             | 4 (legacy + 3 new under `restaurant/<archetype>.html`)                      |
| Restaurant imagery pools | 1 (`restaurant`)                         | 4 (`restaurant`, `restaurant-fine`, `restaurant-trattoria`, `restaurant-street`) |
| Total templates  | 18                                              | 19                                                                          |

The DNA system is still **strictly additive** — templates without a DNA entry continue to render via the legacy per-category composition. The legacy `templates/preview_compositions/restaurant.html` is retained as a safety net for any future restaurant template not yet pulled into an archetype.

## What makes the 3 restaurant templates genuinely different (not recolors) — post Session 10

| Slug                       | Archetype       | Page macro tone   | Hero composition                                    | Navbar         | Card mood                  | Display Font           |
|----------------------------|-----------------|-------------------|-----------------------------------------------------|----------------|----------------------------|------------------------|
| gusto-fine-dining          | fine-dining     | **fully DARK** charcoal #0b0907 | full-bleed plated dish R · italic serif text L  | serif-centered (dark + gold rule) | course-index on same dark bg, gold dotted leaders | Playfair Display       |
| sapore-trattoria-pizzeria  | trattoria-warm  | **fully BRIGHT** cream #fff4da | two tilted polaroids L · handwritten Caveat R   | warm-bar (cream + phone CTA) | cream-paper recipe card with washi tape | Caveat (handwritten)   |
| brace-street-food-lab      | street-modern   | **bright YELLOW** #FFE600 | giant condensed display L · tilted burger product R | bold-pill (black floating) | brutalist black product grid w/ corner badges | Big Shoulders Display  |

**The macro tone column is the critical one** — this is the lesson from Session 10's fix pass. At thumbnail scale, page-level color regions dominate over hero details. Two templates with the same "cream top, dark bottom" silhouette will read as similar regardless of what's in each section. The fix is to make the WHOLE PAGE one consistent macro tone (dark / cream / yellow) so the entire silhouette is different from card to card.

Differences also span hero composition (full-bleed plate L vs polaroid scrapbook L vs tilted product cutout R), navbar shape (centered serif wordmark with gold rule vs cream warm-bar with phone CTA vs floating black pill), card stride (5-row dotted-leader course index on dark vs 5-day cream washi-tape recipe card vs 4-up brutalist product grid), button language (gold-underlined serif ghost vs rustic rounded with red+green tilted shadow vs brutalist block-bold with hard offset shadow), density (very-airy → medium → compact), and copy tone (editorial chef → familiar warm → energetic bold).

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

### Lessons from Session 10 — read these before designing any new category

1. **Imagery pool distinctness is non-negotiable.** Two pools that share even 5 of 6 URLs will produce sibling templates that look identical, regardless of how different the compositions are. When designing a new category's pools, write down the URL list and visually verify zero overlap. Hand-check every Unsplash candidate by downloading via curl and reading the file with the Read tool — HTTP 200 just means the photo exists, not that it shows what you expect (Session 10 caught a clothing store image that way).
2. **Page-level macro tone trumps hero details.** A "cream top, dark bottom" composition will always look similar to another "cream top, dark bottom" composition at thumbnail size, even if the content within each section is wildly different. Solution: make each composition's WHOLE PAGE one consistent macro tone, and pick a different macro tone for each sibling. Restaurant settled on dark / bright cream / yellow — three opposite ends of the spectrum.
3. **Dark bands at the bottom of cream layouts are a trap.** They feel safe and editorial, but they collapse two-region silhouettes into "the same shape with different details". Avoid the pattern entirely.
4. **Browser cache trap when verifying.** Playwright Chromium aggressively caches preview PNGs. After regenerating, the listing page may show the OLD images. Force-refresh by mutating `img.src` with a `?cb=<timestamp>` query string via `browser_evaluate`, OR navigate directly to `/media/.../preview.png?v=<n>` first.

### Watch out for the Session 8/9 timing trap (still unfixed)
When you add a DNA entry to a slug that *already* has a generated preview, that preview was rendered through the legacy fallback and is now stale. The `generate_previews` "skip if exists" branch will not regenerate it. Always run `python manage.py generate_previews --force --only <slug>` after creating or modifying a DNA entry for an existing template — **AND** delete the canonical-named PNG file on disk first, otherwise Django storage will append a random suffix to the new file (the DB row will still point correctly to the suffixed file, so functionally fine, but the disk gets cluttered with orphans). Session 10 also taught us to clear `media/preview_imagery/<key>/` when imagery URLs change so the new ones get downloaded fresh.

The clean recipe used in Session 9 to avoid the orphan trap:
```bash
# 1. Delete the row + canonical file + any suffixed file via a small Django shell snippet
python -c "import django, os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','marketweb.settings'); django.setup(); ..."
# 2. Then re-run WITHOUT --force so the new file lands at the canonical name (no collision)
python manage.py generate_previews --only <slug>
```

### Immediate next step (highest impact)
**Replicate the DNA pilot for the Agency category.** Same recipe — but apply Session 10 lessons rigorously:

1. Open `apps/catalog/template_dna.py` and add 3 entries: vertex-creative-agency → `bold-grid`, aura-digital-studio → `editorial-quiet`, plus 1 NEW template `case-study-led` (e.g. a strategy/branding agency that leads with case studies).
2. Add the new template to `apps/catalog/management/commands/seed_templates.py`.
3. **Decide each composition's macro page tone BEFORE writing CSS** — never two with the same silhouette. E.g.: bold-grid = full-bleed dark with bright accent; editorial-quiet = pure white minimal; case-study-led = colorful blocks with black type. Three different page-level macro tones.
4. Create `templates/preview_compositions/agency/bold-grid.html`, `agency/editorial-quiet.html`, `agency/case-study-led.html`. Use the **restaurant** (post-Session 10) and **medical** files as the structural reference — each must have a completely different hero, navbar, cards, and footer composition. **DO NOT** put a dark band on the bottom of a light layout — that's the silhouette trap from Session 10.
5. Add 3 new imagery keys (`agency-bold`, `agency-editorial`, `agency-cases`) in `preview_imagery.py`. **HAND-CHECK every Unsplash candidate via curl + Read** — Session 10 caught a clothing-store photo that way. Each pool must have ZERO URL overlap with the others. Aim for 6 photos per pool.
6. Choose multi-weight Google Fonts only (`_base.html` requests `wght@500;600;700;800` and Google Fonts CSS2 returns 400 if no requested weight exists). Big Shoulders Display, Playfair Display, Caveat, Space Grotesk, DM Sans, Manrope are all safe.
7. Use the clean delete + regenerate-without-force recipe (also clear `media/preview_imagery/<new-key>/` if you change URLs after a first generation pass).
8. Verify with Playwright at `/templates/agency/`. **Cache-bust each `<img>` via `browser_evaluate` before screenshotting** — see the browser cache trap note above. Inspect direct PNG URLs with `?v=N` query strings.

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
