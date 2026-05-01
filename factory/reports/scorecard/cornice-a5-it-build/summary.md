# Cornice · A.5 IT build · one-page summary

```
PHASE X.5 · CORNICE · A.5 BUILD SIGN-OFF
==========================================

Slug:               cornice-architettura
Archetype:          corporate-suite (5th sibling)
Sub-cluster:        architecture-firm · single-principal studio
Layout family:      LF-2 · Editorial Spread (1st LF-2 occupant in cluster)
Build pass:         IT-only (pre-multilingual · pre-public-flip)
Tier:               draft (anonymous: 404 · staff_preview: 200 with ?preview=1)
Catalog:            23 published_live + 1 draft = 24 total

Voice anchor (verbatim):
    "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."

Palette: graphite #1F2226 + pietra-serena #C7BFB1 + terracotta-rust #B7491F
         (NEUTRAL/NEUTRAL/WARM · only un-claimed cluster polarity)
Typography: Cormorant Garamond + Source Sans 3 (closes Inter cluster-collapse risk)

Section sequence (LF-2 sequence B):
  1. Hero (stacked-editorial · KPI tuple in photo overlay · NO dark band)
  2. Narrative essay (rust drop-cap + 3 pull-quotes + 4-link side-rail)
  3. Sectors-ribbon (italic Cormorant · 12 typologies · NO photos)
  4. Single-portrait leadership (LF-2 L6 · ONE founding architect)
  5. Cases magazine 3+1 grid (LF-2 L7 · 1 hero card + 3 small cards)
  6. CTA closer cream (LF-2-specific · hairline borders + filled rust)

Navbar: split-wordmark on cream "CORNICE / studio di architettura"
Footer: 4-col with whistleblowing column (D.lgs. 24/2023)

DISTINCTNESS (5-axis · planner-brief §15):
  vs Pragma:    5/5 distinct  (LF-1 · navy/emerald boardroom)
  vs Fiscus:    5/5 distinct  (LF-3 · gray/blu-notte commercialista)
  vs Solaria:   5/5 distinct  (LF-4 · warm-carbon coaching)
  vs Continua:  5/5 distinct  (LF-5 · pine/brass stewardship)

LAYOUT-DISTINCTNESS (9-cell L1–L9 · CS-LAYOUT-12 ≥4/9):
  vs Pragma (LF-1):    9/9
  vs Fiscus (LF-3):    9/9
  vs Solaria (LF-4):   8/9
  vs Continua (LF-5):  8/9

PANEL SCORES (6 panels):
  build-report:           5.0/5
  style-critic:           4.7/5
  contrast-accessibility: 4.6/5
  responsive-auditor:     4.6/5
  browser-verifier:       4.7/5
  release-gatekeeper:     4.6/5
  ───────────────────
  MEAN:                   4.65/5  (floor 4.50)

CRITICAL DIMENSIONS (9 · intake §10):
  Mean: 4.83/5 (floor 4.0)

BLOCKING FINDINGS:    0/18 open

FROZEN SIBLINGS:      0/4 regressed
TEST SUITE:           545/546 (1 pre-existing failure · unrelated)

ROUTES (all 200 staff-preview · 404 anonymous):
  /preview/                                              home
  /preview/studio/                                       about ("Archivio")
  /preview/servizi/                                      services
  /preview/progetti/                                     cases list
  /preview/progetti/biblioteca-pietrasanta-concorso/     case detail
  /preview/progetti/via-volpe-roma-residenziale/         case detail
  /preview/progetti/palazzo-lignari-bologna-restauro/    case detail
  /preview/progetti/cornice-fronte-minore-saggio/        case detail
  /preview/contatti/                                     contact

SERVER:
  http://127.0.0.1:8052/   (port 8052 · staff session active)

VERDICT:                READY FOR HUMAN VISUAL REVIEW

NEXT GATE:              user-handshake on IT walk
ON GO:                  workflow C (EN/FR/ES/AR + AR RTL · Naskh-vs-Kufi decision)
ON HOLD:                A.6 narrow re-author OR A.5b re-build
PUBLIC FLIP:            workflow D · post-multilingual · post-handshake
```

## Open questions for the user-handshake

1. Does the LF-2 stacked-editorial hero feel sufficiently distinct from Continua's library reading-room hero at 1280 + 720?
2. Does the single-portrait masthead read environmental, NOT LinkedIn headshot, at 1280 + 768? (Risk 4 from intake §12)
3. Does the 3+1 magazine grid land editorially, NOT as a generic gallery?
4. Does the cream-paper navbar feel right for the editorial-curatorial register, or should LF-2 ship a primary-bg variant?
5. Are the architectural-vocabulary density (Risk C-1) and the 3-time `argomento` motif (Risk C-3) reading as serious-editorial, NOT gatekeepy or repetitive?

## Files written

**Source code (5 created + 8 modified)**:
- Created: `apps/catalog/template_content_cornice.py`, `apps/catalog/migrations/0007_cornice_layout_family.py`, `templates/.../_layouts/lf2/{content,styles}.html`
- Modified: `apps/catalog/{preview_imagery,imagery_policy,template_dna,template_content}.py`, `apps/catalog/management/commands/seed_templates.py`, `TEMPLATE_REGISTRY.json`, `templates/.../home.html`, `templates/.../_base.html`

**Reports** (this scorecard set):
- `factory/reports/cornice/cornice-a5-it-build.md`
- `factory/reports/browser-verification/cornice-a5-it-build.md`
- `factory/reports/browser-verification/cornice-a5-it-build/captures/*.png` (15 captures)
- `factory/reports/scorecard/cornice-a5-it-build/{build-report,style-critic,contrast-accessibility,responsive-auditor,browser-verifier,release-gatekeeper,scorecard,summary}.md`
