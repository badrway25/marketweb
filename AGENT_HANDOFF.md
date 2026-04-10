# Agent Handoff

Last updated: 2026-04-10 — after Template Polish Fixes (Session 12)

## Session 12 — Template Polish Fixes (2026-04-10)

Two product-quality issues closed before the next pilot:

1. **Over-narrow inner-page layouts.** The live multi-page template skins used max-width 1100/1200/1280 which felt "compressed into the middle" of 1600-1920px displays. Bumped to a two-tier standard: **1400px** for medical/specialist wide sections, **1440px** for restaurant/fine-dining wide sections. The home manifesto had an additional double-constraint bug (`outer 1100px` + `inner p max-width: 36ch; margin: 0 auto`) producing a tiny ~450px centered column — fixed by removing the inner centering and widening to `68ch` left-aligned so the drop-cap anchors the frame's left edge. Blog detail pages stay at 760px intentionally (long-form reading column).

2. **Restaurant listing preview mismatch.** Two layers:
   - **Outer layer:** `template.assets.first` in the card + detail partials is fragile — default-ordering fetch, not filtered by asset_type. Replaced with a new `WebTemplate.preview_asset` property in `apps/catalog/models.py` that explicitly filters `asset_type == preview`, is prefetch-aware (iterates `_prefetched_objects_cache` when available), and returns `None` when no preview exists. Selector uses `Prefetch('assets', queryset=...filter(asset_type='preview'))` to ship a smaller payload.
   - **Inner layer (actual cause):** The gusto + sapore PNG files on disk were stale legacy `restaurant.html` renders — both showed the same wood-interior trattoria. Session 10's claimed regeneration never actually landed in this worktree. Fixed by deleting the stale asset rows + files and re-running `generate_previews --only <slug>` (no `--force`, so the canonical filename lands clean without an orphan suffix).

**Branch:** `template-polish-fixes` worktree (built on top of `template-completeness-pilot` → ... → `template-dna-system`, **none merged to master yet**).

**All three restaurant cards now read as three distinct products at thumbnail size** — Brace (yellow brutalist), Sapore (bright cream polaroid), Gusto (dark editorial Playfair). 20 routes verified 200 via Django test client, `python manage.py check` passes.

### Lessons from Session 12

- **`template.assets.first` is a bug magnet.** It returns "whatever's first by default `(order, asset_type)` ordering", which silently picks the wrong file the moment a template gains a second asset. Always filter by `asset_type` explicitly. The `WebTemplate.preview_asset` property encapsulates this rule once so templates never need to remember it.
- **Page-level max-widths of 1100-1280 are too narrow for 1600+ displays.** 1400-1440 is the new standard for wide content. Editorial narrow reading columns (blog articles) stay at ~720-800 because those are about line length, not frame width. **Never double-constrain** with outer `max-width` + inner `margin: 0 auto + max-width: Xch` on the same element tree — either widen the outer container and use `max-width: <NN>ch` on the text (left-aligned, drop-cap anchored to the frame's left edge), or keep the outer narrow and drop the inner centering. The double constraint creates compositions that look "floating in a void".
- **DNA-fallback timing trap is still live.** Gusto and Sapore's PNGs were stale despite Session 10's claim. Whatever the root cause (cross-branch drift, unrecorded regen, worktree sync), the fix recipe is the same every time: delete the asset row + canonical file first, then re-run `generate_previews --only <slug>` without `--force`. TODO_NEXT.md Phase 2d item 4 — "auto --force whenever the DNA file or composition path on disk is newer than the preview's TemplateAsset" — would catch this class of bug structurally. Strong candidate for the next DX polish pass.

## Current State (since Session 11, carried through 12)

**Two pilot templates now ship as full multi-page websites — not just preview screenshots.** The DNA system (Sessions 7-10) made each template's homepage visually unique. Session 11 added the missing piece: every template can now be a *navigable, complete website product*. Session 12 then polished the inner-page layout widths and hardened the preview-asset selection against the fragile `template.assets.first` fallback.

- **`cardio-studio-specialistico`** (Medical · specialist archetype): 8 navigable inner pages — Home, Lo Studio, Visite, Medici, Pubblicazioni (list + article detail), Contatti, Richiedi visita
- **`gusto-fine-dining`** (Restaurant · fine-dining archetype): 7 navigable inner pages — Casa, Filosofia, Menu (otto atti), Atmosfera, Diario (list + article detail), Prenota
- All 17 routes (8 + 7 + 2 marketplace detail) verified 200 via Django test client (Session 11), extended to 20 in Session 12
- The system is **strictly opt-in per template** — every other template in the catalog behaves exactly as before
- **New in Session 12:** `WebTemplate.preview_asset` property, selector uses `Prefetch` with filtered queryset, layout widths bumped to 1400/1440, home manifesto double-constraint fixed, stale gusto/sapore PNGs regenerated. Three restaurant cards now read as three distinct products at thumbnail size.

The marketplace template detail page now shows "Apri anteprima completa" (linking to the full live site) when content is registered, and falls back to the old "Anteprima Live" placeholder otherwise.

Branch: `template-polish-fixes` worktree (built on top of `template-completeness-pilot` → ... → `template-dna-system`, **none merged to master yet**).

## Session 11 — Template Completeness Pilot Phase

Three architectural layers introduced:

1. **Content registry** — `apps/catalog/template_content.py`. Python dict keyed by `WebTemplate.slug` holding the page list, per-page content blocks (eyebrow, headline, sections, lists), and a `posts` list for blog/news inner pages. All Italian, all realistic, no boilerplate.

2. **Per-archetype standalone skin** — `templates/live_templates/<category>/<archetype>/`. Each archetype gets its own `_base.html` that is a *complete HTML document* (NOT extending the marketplace `base.html`), loading the DNA's font pairing and brand palette. Each page kind (`home.html`, `about.html`, `services.html`, `team.html`, `blog_list.html`, `blog_detail.html`, `contact.html`, `appointment.html`, `menu.html`, `gallery.html`, `reservations.html`) extends that base and overrides `extra_css` + `content`.

3. **Single dispatcher view** — `LiveTemplateView` in `apps/catalog/views.py`. Resolves WebTemplate → DNA → content registry in `setup()` (NOT `get_template_names`, see D-044 trap), computes the template path `live_templates/<category>/<archetype>/<page-kind>.html`, returns 404 if either DNA or content is missing.

Three new URL patterns:
```
/templates/<cat>/<slug>/preview/                         → live_template_home
/templates/<cat>/<slug>/preview/<page>/                  → live_template_page
/templates/<cat>/<slug>/preview/<page>/<post_slug>/      → live_template_post
```

### What makes a template "complete" now

A template earns the "Apri anteprima completa" CTA on its detail page once it has BOTH:
1. A DNA entry in `apps/catalog/template_dna.py` (archetype + chrome decisions)
2. A content registry entry in `apps/catalog/template_content.py` (the editorial copy for every page)

Without either, it falls back to the legacy `Anteprima Live` placeholder and the new URL space returns 404. Every template that's been in the catalog before Session 11 still works exactly as it did.

### What is now reusable across all future templates
- `LiveTemplateView` and the three URL patterns
- The content-registry pattern (`template_content.py`) — adding a new template = adding ONE new top-level dict
- The per-archetype skin folder structure — any new template that picks an existing archetype gets the chrome FOR FREE, just needs content
- Brand palette → CSS variable injection
- Nav loop with `is-current` highlight
- Footer pattern with site-data block

### What still needs per-archetype work
- Each NEW archetype needs its own `_base.html` (intentionally bespoke — that's the point of DNA)
- Each NEW archetype's page kinds need their own page templates (a `menu.html` is meaningless for a medical template)

## Old: Session 10 — Restaurant Pilot Fix Pass

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
**Add a third template to validate that the inner-page abstraction holds with content alone.** Pick ONE of:

- **Option A — second `specialist` template** (e.g. `dermatologia-elite-roma`): proves the Medical specialist 8-page model travels with content alone. Recipe:
  1. Add a row to `apps/catalog/management/commands/seed_templates.py`
  2. Add a DNA entry to `apps/catalog/template_dna.py` (archetype: `specialist`)
  3. Add a content block to `apps/catalog/template_content.py` (use `CARDIO_CONTENT` as the structural reference — same keys, different copy)
  4. Run `python manage.py seed_templates` to insert the new row
  5. Hit `/templates/medical/dermatologia-elite-roma/preview/` — should render with the Cardio chrome but completely different content
  6. **Zero new HTML files needed.** If something breaks, the abstraction failed and we need to identify where.

- **Option B — second `fine-dining` template** (e.g. `tartufo-truffle-house`): proves the Restaurant fine-dining 7-page model travels with content alone. Same recipe, use `GUSTO_CONTENT` as reference.

(B) is the stronger signal — restaurant is the most visually-loaded category and the one most likely to expose hidden assumptions.

After validating, pick one of the Phase 2g.1 backlog items in TODO_NEXT.md (previous/next page nav, per-page meta tags, imagery in registry, or building inner pages for the other 4 medical / 2 restaurant archetypes).

### Phase 2f — DNA rollout to other categories (still pending)
The DNA rollout from Sessions 7-10 stopped after Restaurant. Three more categories still need archetype splits — Agency (3 archetypes), Lawyer (2), Real Estate (2). See the previous handoff note for the recipe; the constraint is now both:
1. Distinct preview compositions per archetype (Sessions 7-10 lessons)
2. Inner-page chrome under `templates/live_templates/<category>/<archetype>/` if the new templates are to ship as full sites (Session 11 architecture)

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

### Key Files for the DNA System (preview screenshots — Sessions 7-10)
- `apps/catalog/template_dna.py` — DNA registry + vocabulary (the source of truth)
- `apps/catalog/templatetags/preview_extras.py` — `at` filter for image indexing in loops
- `apps/catalog/preview_imagery.py` — `IMAGERY_CONFIG` with per-archetype keys
- `apps/catalog/management/commands/generate_previews.py` — DNA-aware pipeline
- `templates/preview_compositions/<category>/<archetype>.html` — bespoke per-template preview HTML (1600x900 fixed)
- `templates/preview_compositions/<category>.html` — legacy fallback for non-DNA templates

### Key Files for the Live Template System (multi-page websites — Session 11)
- `apps/catalog/template_content.py` — content registry (per-template page copy + helpers `has_live_template`/`get_content`/`find_page`/`find_post`)
- `apps/catalog/views.py` — `LiveTemplateView` (resolves DNA + content in `setup()`, dispatches to per-archetype/page-kind template)
- `apps/catalog/urls.py` — three URL patterns: `live_template_home`, `live_template_page`, `live_template_post`
- `templates/live_templates/<category>/<archetype>/_base.html` — standalone HTML doc for the archetype (NOT extending `base.html`)
- `templates/live_templates/<category>/<archetype>/<page-kind>.html` — per-page-kind layouts (home, about, services, team, blog_list, blog_detail, contact, appointment, menu, gallery, reservations)
- `templates/catalog/template_detail.html` — conditional CTA (`Apri anteprima completa` if content registered)

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
- **Template-completeness-pilot** owns: `apps/catalog/template_content.py`, `LiveTemplateView`, the live preview URL patterns, `templates/live_templates/<category>/<archetype>/` skin folders
- All sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md, TEMPLATE_REGISTRY.json, BRAND_SYSTEM_GUIDELINES.md, CATEGORY_ROADMAP.md at end
