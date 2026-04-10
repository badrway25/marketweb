# Agent Handoff

Last updated: 2026-04-10 — after Medical Pilot Fix (Session 8)

## Current State

**Template DNA System Phase 1 complete + medical pilot fix shipped.** Templates inside the same category are no longer recolors of each other — each one has a unique "DNA" (archetype + hero/navbar/footer/cards/conversion/density/tone) that drives a bespoke HTML composition. The Medical category is the working pilot with **4 genuinely distinct templates (clinic, family, specialist, wellness), all visually validated end-to-end on `/templates/medical/`**.

Branch: `medical-pilot-fix` worktree (built on top of `template-dna-system`, neither merged to master yet).

## Session 8 fix — what was wrong and what changed

The visual review caught that `benessere-centro-olistico` (wellness archetype) was rendering with a clinic-shaped preview (same booking widget, same `Cardiologia/Pediatria/Diagnostica/Fisioterapia` cards, same headline `La tua salute, la nostra missione` as Salute), only differing in palette. After end-to-end inspection, the registry, composition resolver, asset table, and `assets.first` were all correct — the bug was a **stale PNG file** generated *before* the DNA/wellness composition existed (when the generator legitimately fell back to the legacy `templates/preview_compositions/medical.html`, which has clinic content hardcoded). On the next `generate_previews` run, the fallback skip prevented the regeneration. Fix: deleted the stale TemplateAsset row + orphan PNG, re-ran `generate_previews --only benessere-centro-olistico`, verified the new wellness PNG and the listing.

**No code or template changes** — the fix was data-only. See SESSION_LOG.md Session 8 for the full timeline. New polish entries added to TODO_NEXT.md to prevent the timing trap from recurring (DNA-aware staleness detection + clean `--force` file removal).

## What changed in this session

| Layer            | Before                                              | After                                                                  |
|------------------|-----------------------------------------------------|------------------------------------------------------------------------|
| Differentiation  | Per-category composition (palette/font only)        | Per-template DNA → per-template archetype HTML                         |
| Composition path | `preview_compositions/<category>.html`              | `preview_compositions/<category>/<archetype>.html` (DNA) or fallback   |
| Imagery          | One photo pool per category                         | Per-template `imagery_key` → distinct pool per archetype               |
| Medical templates| 2                                                   | 4 (added Famiglia — Studio Pediatrico, Cardio — Studio Specialistico)  |
| Medical archetypes | 1 (institutional clinic only)                     | 4 (clinic, family, specialist, wellness)                               |

The DNA system is **strictly additive** — templates without a DNA entry continue to render via the legacy per-category composition. No category is forced to migrate at once.

## What's Working

| Page                          | URL                                        | Status (port 8097) |
|-------------------------------|--------------------------------------------|--------------------|
| Homepage featured grid        | `/`                                        | Salute (clinic archetype) appears in featured grid |
| Template listing (all)        | `/templates/`                              | 18 templates × paginated |
| Template listing (medical)    | `/templates/medical/`                      | 4 medical templates × 4 visibly different archetypes |
| Template detail (each medical)| `/templates/medical/<slug>/`               | Gallery shows the new archetype PNG |

## How the DNA system works

```
apps/catalog/template_dna.py
  ├── Vocabulary dicts: LAYOUT_ARCHETYPES, HERO_STYLES, NAVBAR_STYLES,
  │                     FOOTER_STYLES, CARD_STYLES, BUTTON_STYLES,
  │                     DENSITY_PROFILES, TONES, CONVERSION_PATTERNS,
  │                     IMAGERY_DIRECTIONS
  ├── TEMPLATE_DNA: dict[slug, dna]  # the registry
  └── get_dna(slug), has_dna(slug)

apps/catalog/templatetags/preview_extras.py
  └── `at` filter — `{{ imagery|at:forloop.counter }}` for safe loop indexing

apps/catalog/preview_imagery.py
  └── New keys: medical-family, medical-specialist, medical-wellness
      (each draws from a curated mix of already-cached Unsplash URLs)

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
```

Run with `python manage.py generate_previews [--force] [--only <slug>]`.

## Database State

- 8 categories (unchanged)
- **18** templates (was 16; +2 medical: famiglia-pediatria, cardio-studio-specialistico)
- 18 brands
- 18 preview assets — 4 medical now use the new per-archetype compositions
- 47 + 18 cached source photos (3 new pools: medical-family, medical-specialist, medical-wellness)

## For Next Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, TODO_NEXT.md, this file, then `apps/catalog/template_dna.py` (the new source of truth for differentiation)

### Watch out for the Session 8 timing trap
When you add a DNA entry to a slug that *already* has a generated preview, that preview was rendered through the legacy fallback and is now stale. The `generate_previews` "skip if exists" branch will not regenerate it. Always run `python manage.py generate_previews --force --only <slug>` after creating or modifying a DNA entry for an existing template. The polish list in TODO_NEXT.md tracks the proper safety net (DNA staleness detection in the generator).

### Immediate next step (highest impact)
**Replicate the DNA pilot for the Restaurant category.** Same recipe:

1. Open `apps/catalog/template_dna.py` and add 3 entries: gusto-fine-dining → `fine-dining`, sapore-trattoria-pizzeria → `trattoria-warm`, plus 1 NEW template `street-modern` (e.g. burger/pizza counter brand).
2. Add the new template to `apps/catalog/management/commands/seed_templates.py`.
3. Create `templates/preview_compositions/restaurant/fine-dining.html`, `restaurant/trattoria-warm.html`, `restaurant/street-modern.html`. Use the medical files as the structural reference — each must have a **completely different** hero, navbar, cards, and footer composition (not just different palettes).
4. Add 2 new imagery keys in `preview_imagery.py` if you want each restaurant archetype to pull from a distinct food photo pool.
5. `python manage.py seed_templates && python manage.py generate_previews --force --only <slug>` for each.
6. Verify with Playwright at `/templates/restaurant/`.

### Phase 2d polish (still pending from previous session)
1. Optimize PNG file sizes (~4 MB → ~500 KB via Pillow `optimize=True` or oxipng)
2. Cormorant Garamond on dark backgrounds reads thin (Lex, Villa, Cardio specialist) — consider bumping weight or swapping serif at low luminance
3. Add `media/preview_imagery/` to .gitignore

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
- All sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md, TEMPLATE_REGISTRY.json at end
