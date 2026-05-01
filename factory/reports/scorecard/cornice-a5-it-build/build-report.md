# Build report · Cornice A.5 IT build

```yaml
panel:           build-report
template_slug:   cornice-architettura
phase:           X.5 · A.5 build
date:            2026-05-01
verdict:         BUILD-COMPLETE
score:           5/5
```

## Summary

Cornice A.5 IT build delivered the full LF-2 editorial-spread layout family on the corporate-suite shell. Five new files (content module, migration, LF-2 content scaffold + LF-2 styles, this report set), eight modified files (DNA, content registry, imagery pool, imagery policy, seed metadata, registry JSON, home dispatcher, base nav/footer conditionals).

## Build inventory

**Created**:
- `apps/catalog/template_content_cornice.py` — IT-only `CORNICE_CONTENT_IT` dict, 5 pages + 4 case-detail posts, ~700 lines.
- `apps/catalog/migrations/0007_cornice_layout_family.py` — backfills `layout_family="LF-2"` on the cornice WebTemplate row.
- `templates/live_templates/business/corporate-suite/_layouts/lf2/content.html` — LF-2 content scaffold (~145 lines). Stacked-editorial hero with KPI tuple inside the photo overlay, narrative essay with rust drop-cap and 3 pull-quotes, sentence-ribbon sectors, single-portrait leadership, 3+1 magazine grid, cream CTA closer.
- `templates/live_templates/business/corporate-suite/_layouts/lf2/styles.html` — LF-2 visual identity (~720 lines). 5-tier responsive matrix (1280/1100/880/720/480). Drop-cap, side-quote rust border, side-rail anchors, magazine-card primitives, cream CTA closer with hairline borders + filled-rust button.

**Modified**:
- `apps/catalog/preview_imagery.py` — added `business-architecture` pool (6 Pexels URLs · cross-cluster grep CLEAN).
- `apps/catalog/imagery_policy.py` — added `business-architecture` to `CORPORATE_SUITE_POOL_KEYS`.
- `apps/catalog/template_dna.py` — added `cornice-architettura` DNA entry.
- `apps/catalog/template_content.py` — wired `cornice-architettura` into `TEMPLATE_CONTENT` registry (5 locales fall back to IT until workflow C).
- `apps/catalog/management/commands/seed_templates.py` — added taxonomy metadata + brand seed.
- `TEMPLATE_REGISTRY.json` — added Cornice row at `tier=draft`.
- `templates/live_templates/business/corporate-suite/home.html` — extended layout-family dispatch chain to handle LF-2.
- `templates/live_templates/business/corporate-suite/_base.html` — extended nav (split-wordmark + LF-2 trailing CTA pill) and footer (LF-2 4-col-with-whistleblowing) conditionals; added `.cs-nav-cta--lf2` styles.

## Scope discipline

- **Apps/editor** — not touched.
- **Apps/projects** — not touched.
- **Apps/commerce** — not touched.
- **No new archetype** introduced.
- **Pexels-only** imagery (CS-IMG-SRC-01).
- **IT-only** content; multilingual deferred to workflow C.
- **Tier=draft** preserved; public flip held for workflow D post-multilingual.

## Build deviations from planner brief

1. `/pubblicazioni/` page deferred to a phase-2 enrolment (planner-brief §16 fallback authority). The Archivio (about) page covers the studio's editorial method + collana monografica history. Re-introducing the `/pubblicazioni/` page is a single registry addition + one new content section.
2. About page label "Studio" renamed to "Archivio" to avoid duplicate "Studio · Studio" reading in the navbar (home label is "Lo studio").

Both deviations are scope-preserving and documented in `factory/reports/cornice/cornice-a5-it-build.md §5`.

## Score: 5/5

Every required surface implemented. Every input report consumed. No scope creep. Ready for human visual review.
