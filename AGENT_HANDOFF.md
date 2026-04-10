# Agent Handoff

Last updated: 2026-04-10 — after Real Preview Assets Phase 2 (Session 6)

## Current State

**Real preview assets phase 2 complete.** Each of the 16 templates now has a PNG preview that looks like a real homepage screenshot — actual photographic content (restaurant interiors, doctors, lady justice, modern houses, fashion editorial, etc.) composed into a category-appropriate layout and screenshot via headless Chromium.

Branch: `real-preview-assets` worktree (not yet merged to master).

## What changed in this session

| Layer            | Before                                  | After                                                      |
|------------------|-----------------------------------------|------------------------------------------------------------|
| Asset format     | Inline SVG wireframe                    | 1600×900 PNG screenshot of real HTML                      |
| Photo content    | None (colored rectangles)               | Real Unsplash photos cached locally                        |
| Layout source    | String-formatted SVG in Python          | Django HTML templates per category (8 layouts)             |
| Brand fidelity   | Palette only                            | Palette + Google Font pair + accent contrast              |
| Generator        | Pure Python                             | Three-phase: ORM → Playwright/Chromium → ORM              |

The `TemplateAsset` API and the existing `template.assets.first.file.url` template usage are unchanged — listing/detail templates needed zero edits.

## What's Working

| Page                          | URL                                        | Status (port 8096) |
|-------------------------------|--------------------------------------------|--------------------|
| Homepage featured grid        | `/`                                        | 6 cards × real-imagery PNGs |
| Template listing (all)        | `/templates/`                              | 16 templates × real PNGs, paginated |
| Template listing (filtered)   | `/templates/<category_slug>/`              | Same as above, category-filtered |
| Template detail               | `/templates/<category_slug>/<slug>/`       | Gallery + related templates show real PNGs |
| Category listing              | `/templates/categories/`                   | Working (no preview imagery on this page) |

## How the new pipeline works

```
apps/catalog/preview_imagery.py
  ├── IMAGERY_CONFIG: {category_slug: [hero_url, feature_url, *card_urls]}
  ├── ensure_cached(category_slug) → list[Path]   # download once, cache forever
  └── _cache_path() / _download() helpers

templates/preview_compositions/
  ├── _base.html          # shared chrome, brand vars, fonts, 1600×900 viewport
  ├── restaurant.html     # hero photo + menu cards with food
  ├── medical.html        # split hero + booking card + service cards
  ├── lawyer.html         # diagonal hero + practice areas + testimonial
  ├── agency.html         # dark theme + case studies + marquee
  ├── business.html       # corporate hero + stats bar + services
  ├── real-estate.html    # hero photo + search bar + property cards
  ├── portfolio.html      # editorial hero + project tiles
  └── ecommerce.html      # promo bar + hero + product grid

apps/catalog/management/commands/generate_previews.py
  Phase A — ORM: select templates, render HTML strings, gather imagery cache
  Phase B — Playwright: open Chromium, screenshot each HTML temp file
  Phase C — ORM: persist TemplateAsset rows pointing at the new PNGs
```

Run with `python manage.py generate_previews [--force] [--only <slug>]`.

## Database State (unchanged from Phase 2a, only file format flipped)

- 8 categories
- 16 templates (status=published, 6 featured)
- 16 brands
- 16 preview assets — **all PNG now**, no SVG remnants in DB
- 47 cached source photos in `media/preview_imagery/<category>/`

## For Next Session

**Read first:** CLAUDE.md, ARCHITECTURE.md, TODO_NEXT.md, this file

### Immediate polish opportunities (Phase 2d)
1. **Per-template imagery overrides** — Both ecommerce templates currently share the same fashion shots. Add an optional `imagery_overrides` JSONField on `TemplateBrand` and merge it into the context in `_build_context()`. This is the highest-impact next step for visual differentiation.
2. **PNG optimisation** — Each preview is ~4 MB at 2× DPI. Pipe screenshots through Pillow with `optimize=True` (or convert to JPEG quality 88) to bring listing-page weight under 5 MB total instead of ~50 MB.
3. **Hero text legibility on dark serif palettes** — Cormorant Garamond at 70px+ on dark navy reads thin (lawyer + villa). Either bump font weight to 800 in those compositions or swap the heading font when palette luminance is below a threshold.
4. **Add `media/preview_imagery/` to .gitignore** — It's a local cache and shouldn't be committed.

### Phase 3 (Interactivity & Accounts) — unchanged from prior handoff
1. Tag seeding and filtering
2. User authentication views
3. Commerce flow
4. Editor + projects integration
5. Live demo iframe per template

### Key Files for Preview System
- `apps/catalog/preview_imagery.py` — imagery config + cache
- `apps/catalog/management/commands/generate_previews.py` — pipeline command
- `templates/preview_compositions/_base.html` — shared brand vars, fonts, chrome
- `templates/preview_compositions/<category>.html` — per-category layout
- `media/preview_imagery/` — local imagery cache (gitignore candidate)
- `media/template_assets/<YYYY>/<MM>/*.png` — generated previews (committed via Django FileField)

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
- Both sessions update: SESSION_LOG.md, DECISIONS.md, TODO_NEXT.md, AGENT_HANDOFF.md at end
