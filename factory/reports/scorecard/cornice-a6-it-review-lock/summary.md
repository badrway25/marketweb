# Cornice · A.6 IT review-lock · One-page summary

```
PHASE X.5 · CORNICE · A.6 REVIEW-LOCK SIGN-OFF
================================================

Slug:               cornice-architettura
Archetype:          corporate-suite (5th sibling)
Sub-cluster:        architecture-firm · single-principal studio
Layout family:      LF-2 · Editorial Spread (1st LF-2 occupant)
Phase:              A.6 review-lock (IT-only · pre-multilingual · pre-public-flip)
Tier:               draft (anonymous: 404 · staff_preview: 200 with ?preview=1)
Catalog:            23 published_live + 1 draft = 24 total

A.6 fixes shipped (3 findings · all resolved):
  F1 (review-blocking)     Founder gender mismatch
                           → Marco→Marta + feminize gendered Italian (16 surfaces)
  F2 (high)                LF-2 cream nav only on home, dark on inner pages
                           → Lift cs-nav--lf2 body styles into _base.html
  F3 (medium)              Magazine-grid hero card visible empty band
                           → flex-grow on hero photo + remove flex from copy

Files modified at A.6:
  apps/catalog/template_content_cornice.py                            (F1)
  templates/.../corporate-suite/_base.html                            (F2)
  templates/.../corporate-suite/_layouts/lf2/styles.html              (F2 + F3)

Untouched at A.6 (per scope rules):
  apps/editor                       zero edits
  apps/projects                     zero edits
  apps/commerce                     zero edits
  LF-1 / LF-3 / LF-4 / LF-5 layout files   zero edits
  TEMPLATE_REGISTRY.json                   zero edits (tier=draft preserved)
  DNA registry                             zero edits
  Imagery pool / imagery policy            zero edits

Voice anchor (verbatim · unchanged from A.5):
    "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."

Founder identity (post-F1):
    Eyebrow:    STUDIO FOUNDER · ARCHITETTA
    Heading:    Marta Roveri (rust em on Roveri preserved)
    Role:       fondatrice · responsabile editoriale dei fascicoli

DISTINCTNESS (5-axis · post-fix · planner-brief §15):
  vs Pragma:    5/5 distinct  (LF-1 · navy/emerald boardroom)
  vs Fiscus:    5/5 distinct  (LF-3 · gray/blu-notte commercialista)
  vs Solaria:   5/5 distinct  (LF-4 · warm-carbon coaching)
  vs Continua:  5/5 distinct  (LF-5 · pine/brass stewardship)

LAYOUT-DISTINCTNESS (9-cell L1–L9 · post-fix · CS-LAYOUT-12 ≥4/9):
  vs Pragma (LF-1):    9/9
  vs Fiscus (LF-3):    9/9
  vs Solaria (LF-4):   8/9
  vs Continua (LF-5):  8/9
  L7 magazine-grid distinctness STRENGTHENED by F3.

PANEL SCORES (6 panels):
  build-report:           4.90/5
  style-critic:           4.85/5
  contrast-accessibility: 4.70/5
  responsive-auditor:     4.70/5
  browser-verifier:       4.85/5
  release-gatekeeper:     4.80/5
  ───────────────────
  MEAN:                   4.80/5  (floor 4.50)
  A.5 mean was 4.65; A.6 lifts to 4.80.

CRITICAL DIMENSIONS (9 · intake §10):
  Mean: 4.88/5 (floor 4.0)
  A.5 was 4.83; A.6 lifts to 4.88.

BLOCKING FINDINGS:    0/3 open (all 3 resolved at A.6)

FROZEN SIBLINGS:      0/4 regressed (verified pre/post)
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
  http://127.0.0.1:8052/   (port 8052 · staff session active at hand-back)

VERDICT:                LOCKED FOR USER VISUAL HANDSHAKE

NEXT GATE:              user-handshake on IT walk
ON GO:                  workflow C (EN/FR/ES/AR + AR RTL · Naskh-vs-Kufi decision)
ON HOLD:                A.7 narrow re-author OR A.6b re-build
PUBLIC FLIP:            workflow D · post-multilingual · post-second-handshake
```

## Open questions for the user-handshake (refined from A.5)

1. Does the LF-2 stacked-editorial hero feel sufficiently distinct from Continua's library reading-room hero at 1440 + 720?
2. Does the post-fix single-portrait masthead read environmental architect (Marta Roveri at her studio drafting table) at 1440 + 768?
3. Does the post-fix 3+1 magazine spread (dominant hero photo) land editorially, NOT as a generic gallery?
4. Does the cream-paper navbar (now consistent across all 9 pages) feel right for the editorial-curatorial register?
5. Are the architectural-vocabulary density (Risk C-1) and the 3-time `argomento` motif (Risk C-3) reading as serious-editorial, NOT gatekeepy or repetitive?

## Files written at A.6

**Source code (3 files modified)**:
- `apps/catalog/template_content_cornice.py` (F1 content edits)
- `templates/live_templates/business/corporate-suite/_base.html` (F2 chrome lift)
- `templates/live_templates/business/corporate-suite/_layouts/lf2/styles.html` (F2 cleanup + F3 flex-grow)

**Reports (this scorecard set)**:
- `factory/reports/cornice/cornice-a6-it-review-lock.md`
- `factory/reports/browser-verification/cornice-a6-it-review-lock.md`
- `factory/reports/browser-verification/cornice-a6-it-review-lock/captures/*.png` (36 captures)
- `factory/reports/scorecard/cornice-a6-it-review-lock/{build-report,style-critic,contrast-accessibility,responsive-auditor,browser-verifier,release-gatekeeper,scorecard,summary}.md`

## What multilingual workflow C still has to do

A.6 doesn't pre-empt or shorten workflow C. Workflow C still has to:

1. EN/FR/ES/AR translations of the entire `CORNICE_CONTENT_IT` dict
2. Voice anchor verbatim-in-translation per locale (EN: argument/case/proposition · FR: argument · ES: argumento · AR: TBD)
3. AR RTL handling (Naskh-vs-Kufi decision per planner-brief §11)
4. TEMPLATE_REGISTRY.json locales flip from `[it]` to `[it, en, fr, es, ar]` + `rtl: true`
5. Per-locale browser walk
6. Tier remains `draft` through workflow C
7. Workflow D (public flip) gated on a second user handshake
