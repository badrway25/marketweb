# Cornice · A.5 IT Build · 5th corporate-suite sibling · 1st LF-2 occupant

```yaml
report_type:        a5-build
template_slug:      cornice-architettura
archetype:          corporate-suite
sub_cluster:        architecture-firm · single-principal studio (editorial-led)
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · Cornice · A.5 build (IT-only · pre-multilingual)
date:               2026-05-01
agent:              template-builder (Phase X.5 A.5 implementation)
inputs_consumed:
  - factory/reports/corporate-suite/cornice-architettura/intake.md
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md
  - factory/reports/corporate-suite/cornice-architettura/prebuild-quick-checks.md
  - factory/reports/imagery/cornice-architettura/pool-selection.md
  - factory/reports/imagery/cornice-architettura/reviewer-lgtm.md
  - factory/reports/copy/cornice-architettura/copy-authoring.md
  - factory/reports/copy/cornice-architettura/voice-anchor-proof.md
  - factory/reports/copy/cornice-architettura/content-volume-check.md
  - templates/live_templates/business/corporate-suite/_layouts/lf{1,5}/ (architecture reference)
  - apps/catalog/template_content_continua.py (LF-5 content shape reference)
status_tag:         A5-BUILD-COMPLETE · ready for human visual review
verdict:            CLEARED FOR USER-HANDSHAKE · IT-only · tier=draft
next_action:        User performs visual review on the live IT pages (6 routes ·
                    5 viewports). On approval, workflow C kicks off (EN/FR/ES/AR
                    + RTL). Tier flip to `published_live` is held until
                    workflow D, post-multilingual.
```

This file is the binding A.5 build narrative. It pairs with:
- `factory/reports/browser-verification/cornice-a5-it-build.md` — IT walk evidence + frozen-sibling regression check + responsive matrix
- `factory/reports/scorecard/cornice-a5-it-build/*.md` — 8 scorecard panels (build · style · contrast · responsive · browser · gatekeeper · summary + master scorecard)

---

## §1 · What was built

| Surface | Implementation |
|---|---|
| **DNA registry** | `apps/catalog/template_dna.py` — added `cornice-architettura` entry with `archetype=corporate-suite`, `layout_family=LF-2`, hero/navbar/footer/card/button styles, NEUTRAL/NEUTRAL/WARM palette tokens (graphite + pietra-serena + terracotta-rust), Cormorant Garamond + Source Sans 3 typography, voice anchor on `argomento` |
| **Content module** | `apps/catalog/template_content_cornice.py` — IT-only `CORNICE_CONTENT_IT` dict with 5 pages (home, studio, servizi, progetti, contatti) + 4 case-detail posts. Pages-array uses distinct labels ("Lo studio" home + "Archivio" about) so the navbar reads as 5 editorial-architectural sections without repetition. |
| **Imagery pool** | `apps/catalog/preview_imagery.py` — added `business-architecture` pool (6 Pexels URLs from A.3 curator selection · cross-cluster grep CLEAN). |
| **Imagery policy** | `apps/catalog/imagery_policy.py` — added `business-architecture` to `CORPORATE_SUITE_POOL_KEYS` so the validator runs the Pexels-only check on the new pool. |
| **Content registry** | `apps/catalog/template_content.py` — registered `cornice-architettura` mapping in `TEMPLATE_CONTENT`. EN/FR/ES/AR fall back to IT until workflow C lands them. |
| **Seed metadata** | `apps/catalog/management/commands/seed_templates.py` — added taxonomy metadata + brand seed entry for Cornice (price €89, featured=False, order=6). |
| **Migration** | `apps/catalog/migrations/0007_cornice_layout_family.py` — backfills `layout_family="LF-2"` on the Cornice WebTemplate row. |
| **Registry JSON** | `TEMPLATE_REGISTRY.json` — added Cornice row at `tier=draft` with single-locale [it] (no AR/RTL until workflow C). |
| **LF-2 layout files (NEW)** | `templates/live_templates/business/corporate-suite/_layouts/lf2/content.html` (140 lines) + `_layouts/lf2/styles.html` (~720 lines · the LF-2 visual identity). |
| **Home dispatcher** | `templates/live_templates/business/corporate-suite/home.html` — extended the LF-5 dispatch branch to also handle LF-2: `if LF-2 → lf2/content + lf2/styles`. LF-1/LF-3/LF-4 fallback unchanged. |
| **Base nav variant** | `_base.html` — extended the navbar block to support `cs-nav--lf2` modifier (split-wordmark masthead instead of single-line wordmark + crest). The trailing-CTA element is gated on layout_family so LF-2 ships a filled-rust pill instead of LF-1's phone block. |
| **Base footer variant** | `_base.html` — extended the 4-col-with-whistleblowing footer condition to also fire for LF-2 (LF-5 already had it). The whistleblowing column-level disclosure (D.lgs. 24/2023) is now shared between LF-2 and LF-5 — both families elevate it from a legal-row footnote to a column. |

**Total skin lines for LF-2** (CSS + HTML): ~860 lines, in two new files only. **Zero edits** to LF-1/LF-3/LF-4/LF-5 layout files. The only non-LF-2 file edits are the home dispatcher + base nav/footer conditional branches — strictly additive.

**Apps/editor, apps/projects, apps/commerce** — not touched. **No new archetype** introduced. **Pexels-only**.

---

## §2 · LF-2 layout implementation (the load-bearing structural change)

The LF-2 family validates the layout-family system by being the first sibling whose home shell **differs structurally** from the LF-1 default. The 9-cell L1–L9 classification:

| Slot | LF-2 declared | Implementation in `_layouts/lf2/content.html` + `_layouts/lf2/styles.html` |
|---|---|---|
| L1 hero | stacked-editorial | `.cs-hero` is a single section: `.photo` is full-bleed top with credit-overlay positioned absolute inside the photo (KPI tuple + caption), and `.below` is a paper-coloured 8/4 grid with h1+actions LEFT and side-quote RIGHT. NOT a 55/45 split. |
| L2 sequence | B | `[hero, narrative, sectors-ribbon, leadership-single, cases-magazine, cta-closer-cream]` — different ordering than LF-1's sequence A and LF-5's sequence D. |
| L3 mid-strip | absent | No `cs-cycle` / `cs-kpi-band` / `cs-trust` mid-strip. The narrative essay covers the cadence-cell role. |
| L4 essay-with-anchors | present | `.cs-narrative` is a 2-col grid with rust drop-cap (Cormorant 84px) on para 1, three pull-quotes interspersed (each with its own italic em-word), and a sticky 4-link side-rail. Replaces `.cs-pillars`. |
| L5 hero-overlay | present | KPI tuple lives **inside** the photo's bottom-left overlay frame · NOT on a separate dark band. CS-TONE-03 demoted at family level. |
| L6 single-portrait-feature | present | `.cs-leadership-single` is a 2-col grid with ONE large environmental portrait LEFT + h2 + role + 2-paragraph bio + 4-credential list RIGHT. NOT a 3-card grid (Continua's L6) · NOT typographic-only (Pragma/Fiscus's L6). |
| L7 magazine-grid | present | `.cs-cases-magazine` is a 2-col CSS grid with the hero card spanning rows 1-3 on the left and 3 small cards stacked on the right. Each card carries photo + eyebrow + h3 + body + pill. NOT list-row · NOT timeline. |
| L8 split-wordmark-top | present | Navbar reads `cs-nav--lf2` modifier · cream background (NOT primary-bg dark band) · split-line masthead "CORNICE / studio di architettura" · trailing filled-rust CTA. |
| L9 4-col-with-whistleblowing | present | Footer reads the LF-2 + LF-5 shared 4-col-with-whistleblowing primitive. The 4th column is `cs-foot-col--whistleblowing` carrying the canale interno (D.lgs. 24/2023). |

**Layout-distinctness matrix** (CS-LAYOUT-12 ≥4/9 gate):

| Pair | Distinct cells | Same cells | Gate |
|---|---:|---|---|
| Cornice (LF-2) vs Pragma (LF-1) | 9/9 | none | PASS |
| Cornice (LF-2) vs Fiscus (LF-3) | 9/9 | none | PASS |
| Cornice (LF-2) vs Solaria (LF-4) | 8/9 | L3=absent (both) | PASS |
| Cornice (LF-2) vs Continua (LF-5) | 7/9 | L9=4-col-with-whistleblowing (both, distinct content) · L3=absent (Cornice) vs governance-cycle-strip (Continua) — actually different here so 8/9 | PASS |

Every pair clears the ≥4/9 threshold by a wide margin. The 4-col footer shared between LF-2 and LF-5 is intentional (the cluster's compliance posture is the same) but the column-content is sub-cluster-specific (Continua = stewardship · Cornice = architectural commissioning).

---

## §3 · Distinctness verdict (5-axis triangulation)

The intake §3.2 studio-name swap test, the §17 sibling-collision audit, and the planner-brief §6 distinctness scoring re-bind on the live IT render at A.7 walk. Verdict per axis:

| Axis | vs Pragma | vs Fiscus | vs Solaria | vs Continua | Verdict |
|---|---|---|---|---|---|
| Voice (`argomento` curatorial-architectural) | distinct (decisional gravity) | distinct (presidio scadenze) | distinct (bounded coaching method) | distinct (stewardship temporal `generazioni`) | PASS |
| Palette (graphite + pietra-serena + rust) | distinct (navy/blue/emerald) | distinct (warm-neutral/gold/blu-notte) | distinct (warm-carbon/ocra/caramel) | distinct (pine/pewter/brass · only 1/3 cell warmth-grid overlap on accent · resolved by surface-class deployment) | PASS |
| Hero geometry (stacked-editorial 8/4) | distinct (55/45 split) | distinct (55/45 split) | distinct (55/45 split) | distinct (object-overlay) | PASS |
| Hero subject (Bologna golden-hour portico · zero people · exterior architectural) | distinct (boardroom planning · 1 person) | distinct (desk + tax documents · zero people but task-class) | distinct (1:1 conversation · 2 people) | distinct (library reading-room interior · zero people but interior-warm-mahogany) | PASS |
| Cases shape (3+1 magazine-grid) | distinct (numbered list-row) | distinct (numbered list-row) | distinct (numbered list-row) | distinct (vertical timeline) | PASS |

**5/5 vs every existing sibling** → matches the planner-brief §6 prediction. Distinctness gate `DISTINCTNESS_RULES.md §1 ≥4/5` cleared with margin.

---

## §4 · Voice + content fidelity

**Voice anchor verbatim** at exactly two places on the home page (copy-authoring §12):
- Hero h1: `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` ✓
- CTA-closer h2: `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` ✓

**Em-word audit** (CS-TYPE-02 single em per heading) — verified on the live render:
- Hero h1 em on `argomento` ✓
- Hero side-quote em on `argomenta` (verb form) ✓
- Pull-quote 1 em on `prima` ✓
- Pull-quote 2 em on `autore` ✓
- Pull-quote 3 em on `regola` ✓
- Sectors counter footnote em on `novanta` ✓
- Leadership h2 em on `Roveri` ✓
- Magazine card 1 h3 em on `geometria` ✓
- Magazine card 2 h3 em on `lotto` ✓
- Magazine card 3 h3 em on `argomento` (motif resonance) ✓
- Magazine card 4 h3 em on `minore` ✓
- CTA-closer h2 em on `argomento` (verbatim) ✓

**12 italic em occurrences on home · all on distinct headings/quotes.** CS-TYPE-02 PASS 12/12. The `argomento`/`argomenta` recurrence on 3 surfaces (hero h1 + hero side-quote + card 3) builds the curatorial motif without overpowering — Risk C-3 mitigation in action.

**Architectural vocabulary in first 30s** (Risk C-1 mitigation):
- Hero first scroll surfaces: `argomento · progetto · servizio · architettura · editoriale · committenze · novanta · fascicoli · 2008 · MILANO · STUDIO DI ARCHITETTURA` — 11+ Tier 1/2 hits in the first viewport at 1440 (counts the eyebrow + h1 + subhead + side-quote + KPI labels).
- Narrative drop-cap paragraph 1 surfaces: `architettura · argomenta · studio · architettura · editoriale · progetto · argomento · sito · committenza · vincolo · opere · cantiere · contesto · programma` — 14 hits in the first paragraph.

**Cluster-banlist audit** (CS-EXEC-04 hyperbole · sibling-anchor CTAs):
- ✗ "trasforma · sblocca · rivoluziona · disrupt" — ABSENT
- ✗ "Fissa una call privata" (Pragma) — ABSENT
- ✗ "Primo appuntamento" (Fiscus) — ABSENT
- ✗ "Prenota una discovery call" (Solaria) — ABSENT (and explicitly negated in CTA closer's closing line)
- ✗ "Avvia un dialogo di mandato" (Continua) — ABSENT
- ✓ Used: "Apri un fascicolo progetto" — fresh · architectural-vocabulary · no collision

---

## §5 · Build deviations from planner brief

Two minor adjustments at A.5 build entry (per planner-brief §16 deferred decisions):

**Deviation 1 · `/pubblicazioni/` page** (planner-brief §4 deferred · §16 fallback authority).
**Decision**: deferred to a phase-2 enrolment. The 5th nav link "Pubblicazioni" was held; the navbar ships 5 links anyway: `Lo studio · Archivio · Servizi · Progetti · Contatti`. The Archivio (about) page covers the studio's editorial method + collana-monografica history. The dedicated `/pubblicazioni/` page would duplicate ~60% of that content in the IT pass; we'd rather author a real publications page after the user-handshake on the IT review. Decision recorded in the page registry; a later edit can add the page slug.

**Deviation 2 · home-page label vs about-page label**.
**Decision**: home label "Lo studio" (manifesto editoriale · overview), about label "Archivio" (history + cv + collana monografica). The pattern follows Continua's home/about pair where the two labels are different words rather than the same word twice. The planner brief §4 had the navbar starting with "Studio" but the codebase iterates over the `pages` array — the home label appears too — and "Studio · Studio" would have read as a duplication.

Both deviations are scope-preserving (no new archetype, no public-tier change, no commerce/editor/projects edits). They are documented here for the workflow C / D agents.

---

## §6 · Risks identified at A.5 build · status

The planner-brief §13 + intake §12 enumerated 5 mitigations + 4 sibling-warning risks. Live-render status:

| Risk | Mitigation | Live status |
|---|---|---|
| Continua palette adjacency (warm-accent on accent cell) | Rust deployed on display-typographic surfaces (drop-cap + pull-quote em + magazine card numerals + cta-closer button + focus ring) — different surface class from Continua's brass which is chrome-only | RESOLVED at first scroll · rust touchpoints visible at 6 distinct surfaces; chrome-vs-display surface separation visible |
| Continua imagery adjacency (object-led + zero people) | Cornice hero is exterior + golden-hour-stone + architectural-shadow + landscape (Bologna portico); Continua hero is interior + mahogany-warm + library-fireplace + horizontal partner-desk | RESOLVED at first scroll · subject-class read at 1 second is "Italian portico architecture" vs Continua's "library reading-room" |
| Pragma stakeholder one-liner adjacency (institutional + serious Italian) | Architectural sub-cluster vocabulary (`progetto · committenza · cantiere · fascicolo · vincolo · MIBAC · OAPPC · concorso · cornice · portico`) lands at first-scroll | RESOLVED at first scroll · the eyebrow "STUDIO DI ARCHITETTURA · MILANO · DAL 2008" + the h1 word `argomento` + the subhead `novanta fascicoli` make the audience read as architecture commissioning, not B2B advisory |
| LF-2 single-portrait stock-headshot collapse (LinkedIn-headshot risk) | Curator-bound to environmental composition + binding triple (50s-or-senior + drafting-tools-mid-ground + environmental-NOT-studio-backdrop). The selected slot 2 photo (RDNE Stock 5915290) is senior-mid-career architect with eyeglasses + papers + working posture in environmental home-office | RESOLVED at portrait scroll · the senior architect reads as "real architect at her studio" not "stock LinkedIn headshot"; the bio + 4 credentials below the portrait reinforce the editorial portrait read |
| LF-2 zero-dark-band on home (cluster-invariant deviation) | LF-2 declares L5=hero-overlay (KPI in photo's overlay) + cta-closer-cream (hairline-bordered cream band, NOT dark). Family-level demotion of CS-TONE-03 declared in `intake.md §4` and `planner-brief.md §6` | RESOLVED on live render · home shows ZERO dark sections · KPI lives in hero photo overlay · cta-closer is cream with filled-rust button + hairline borders |

All 5 mitigations cleared on live render at the 1440 walk. Re-binding at workflow C across 5 locales + AR RTL, and at workflow D pre-flip.

---

## §7 · Files changed

**Created** (5 files):
1. `apps/catalog/template_content_cornice.py` (~700 lines · IT-only CORNICE_CONTENT_IT dict)
2. `apps/catalog/migrations/0007_cornice_layout_family.py` (~50 lines · backfill migration)
3. `templates/live_templates/business/corporate-suite/_layouts/lf2/content.html` (~145 lines · LF-2 content scaffold)
4. `templates/live_templates/business/corporate-suite/_layouts/lf2/styles.html` (~720 lines · LF-2 visual identity)
5. `factory/reports/cornice/cornice-a5-it-build.md` (this file)

**Modified** (8 files):
1. `apps/catalog/preview_imagery.py` — added `business-architecture` pool (6 Pexels URLs)
2. `apps/catalog/imagery_policy.py` — added `business-architecture` to `CORPORATE_SUITE_POOL_KEYS`
3. `apps/catalog/template_dna.py` — added `cornice-architettura` DNA entry
4. `apps/catalog/template_content.py` — wired `cornice-architettura` into `TEMPLATE_CONTENT` registry (5 locales falling back to IT)
5. `apps/catalog/management/commands/seed_templates.py` — added taxonomy metadata + brand seed
6. `TEMPLATE_REGISTRY.json` — added Cornice row at `tier=draft`
7. `templates/live_templates/business/corporate-suite/home.html` — extended layout-family dispatch to handle LF-2
8. `templates/live_templates/business/corporate-suite/_base.html` — extended nav (split-wordmark + LF-2 trailing CTA) and footer (LF-2 4-col-with-whistleblowing) conditionals; added `.cs-nav-cta--lf2` button styles

**Created** (browser-verification + scorecard reports — see §8 for the file list):
- `factory/reports/browser-verification/cornice-a5-it-build.md`
- `factory/reports/browser-verification/cornice-a5-it-build/captures/*.png` (10 screenshots)
- `factory/reports/scorecard/cornice-a5-it-build/*.md` (8 scorecard panels)

**Total surface**: 5 created + 8 modified source files = **13 files**. Within planner-brief §11 budget guidance ("skin-budget ≤ 1300 lines" — actual LF-2 lines ~865).

---

## §8 · Reports written

This A.5 build session produced the following report set:

| Path | Contents |
|---|---|
| `factory/reports/cornice/cornice-a5-it-build.md` | This file · build narrative + distinctness verdict |
| `factory/reports/browser-verification/cornice-a5-it-build.md` | Browser walk evidence · 5 viewports · all 6 IT routes · 4 frozen siblings parity check |
| `factory/reports/browser-verification/cornice-a5-it-build/captures/*.png` | 10 screenshots · cornice (5 viewports + 4 sections) + 4 frozen siblings |
| `factory/reports/scorecard/cornice-a5-it-build/build-report.md` | Implementation summary · what shipped · what didn't |
| `factory/reports/scorecard/cornice-a5-it-build/style-critic.md` | Style-critic panel · LF-2 layout verification · CS rule audit |
| `factory/reports/scorecard/cornice-a5-it-build/contrast-accessibility.md` | Contrast + accessibility report |
| `factory/reports/scorecard/cornice-a5-it-build/responsive-auditor.md` | Responsive matrix verification 1440/1100/880/720/480 |
| `factory/reports/scorecard/cornice-a5-it-build/browser-verifier.md` | Live walk verifier panel |
| `factory/reports/scorecard/cornice-a5-it-build/release-gatekeeper.md` | Release-gate aggregator panel · IT pass-or-hold |
| `factory/reports/scorecard/cornice-a5-it-build/scorecard.md` | Master scorecard · 6 panels averaged |
| `factory/reports/scorecard/cornice-a5-it-build/summary.md` | One-page summary for orchestrator sign-off |

---

## §9 · Server / route status (handed back to orchestrator)

```
server:                 python manage.py runserver 8052 --noreload
URL prefix:             http://127.0.0.1:8052/
template root URL:      /templates/business/cornice-architettura/preview/
6 IT routes (all 200):
  - /preview/                                                       (home)
  - /preview/studio/                                                (about · "Archivio")
  - /preview/servizi/                                               (services)
  - /preview/progetti/                                              (cases list)
  - /preview/progetti/biblioteca-pietrasanta-concorso/              (case detail · concorso)
  - /preview/progetti/via-volpe-roma-residenziale/                  (case detail · residenziale)
  - /preview/progetti/palazzo-lignari-bologna-restauro/             (case detail · restauro)
  - /preview/progetti/cornice-fronte-minore-saggio/                 (case detail · pubblicazione)
  - /preview/contatti/                                              (contact + form)
tier:                   draft (anonymous: 404 · staff_preview: 200 with ?preview=1)
catalog count:          23 published_live + 1 draft
session reqs:           staff user authenticated (cornice-review@cornice-architettura.it · is_staff=True · is_superuser=True)
                        + ?preview=1 query string

frozen siblings (all 200 anonymous):
  - /templates/business/pragma-corporate-suite/preview/      LF-1
  - /templates/business/fiscus-commercialista/preview/       LF-3
  - /templates/business/solaria-coaching/preview/            LF-4
  - /templates/business/continua-stewardship/preview/        LF-5

test suite:             546 tests · 545 pass · 1 pre-existing failure (booking-flag · Continua-related · UNRELATED to Cornice)
```

---

## §10 · Next-step expectations

The A.5 build is **CLEARED FOR USER VISUAL REVIEW** on the IT pass. The user-handshake gate is BEFORE workflow C (multilingual). Per `intake.md §10` and `planner-brief.md §13`, this is the first LF-2 occupant — the review cost is higher than 5th+ in an established sub-cluster, and a HOLD-here is more likely than a typical N-th template.

Open questions for the user at the handshake:
- Does the LF-2 stacked-editorial hero read distinct from Continua's library hero at 1280 + 720?
- Does the single-portrait masthead read environmental, NOT LinkedIn headshot, at 1280 + 768?
- Does the 3+1 magazine grid read editorially, NOT as a generic gallery?
- Does the 4-col-with-whistleblowing footer read appropriate for a single-principal architecture studio (not over-formal)?
- Does the cream-paper navbar feel right vs. the cluster's other dark-bar navs (or should LF-2 ship a primary-bg variant)?

Workflow C kicks off ONLY on user GO. Tier flip to `published_live` is held until workflow D, post-multilingual.
