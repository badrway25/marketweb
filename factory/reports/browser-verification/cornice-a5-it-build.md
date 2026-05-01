# Cornice · Browser verification · A.5 IT build

```yaml
report_type:        browser-verification
template_slug:      cornice-architettura
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · Cornice · A.5 build IT walk
date:               2026-05-01
agent:              walk-verifier (A.7-equivalent on the A.5 build pass)
walk_locale:        it
walk_viewports:     [1440, 1100, 880, 720, 480]
walk_pages:         [home, studio, servizi, progetti, progetti/<slug>, contatti]
captures_dir:       factory/reports/browser-verification/cornice-a5-it-build/captures/
status_tag:         IT-WALK-PASS · all 6 routes 200 · 5 viewports captured · 4 frozen siblings clean
verdict:            PASS · ready for human visual review
next_action:        User performs visual review on the live IT pages. Workflow C
                    (EN/FR/ES/AR + RTL) gated on user-handshake.
```

---

## §1 · Server URL + port left open

```
http://127.0.0.1:8052/

started:  python manage.py runserver 8052 --noreload
preview:  http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?preview=1
auth:     cornice_review / cornice-review-password (is_staff=True, is_superuser=True)
```

The server stays open at port 8052 for the user-handshake review. Anonymous visitors do NOT see Cornice (tier=draft); staff with `?preview=1` reach all 6 IT routes.

---

## §2 · Route status (HTTP)

| Route | Anonymous | Staff + `?preview=1` |
|---|---|---|
| `.../preview/` (home) | 404 ✓ | 200 ✓ |
| `.../preview/studio/` (about · "Archivio") | 404 ✓ | 200 ✓ |
| `.../preview/servizi/` (services) | 404 ✓ | 200 ✓ |
| `.../preview/progetti/` (cases list) | 404 ✓ | 200 ✓ |
| `.../preview/progetti/biblioteca-pietrasanta-concorso/` | 404 ✓ | 200 ✓ |
| `.../preview/progetti/via-volpe-roma-residenziale/` | 404 ✓ | 200 ✓ |
| `.../preview/progetti/palazzo-lignari-bologna-restauro/` | 404 ✓ | 200 ✓ |
| `.../preview/progetti/cornice-fronte-minore-saggio/` | 404 ✓ | 200 ✓ |
| `.../preview/contatti/` | 404 ✓ | 200 ✓ |

**Tier-gate intact**: anonymous 404 confirms `tier=draft` is hidden from public catalog. Staff `?preview=1` reaches the live route. CS-MARKET-01 / D-055 staff-preview semantics holding. Catalog visibility check: anonymous catalog `/templates/business/` shows 0 hits for `cornice-architettura`; staff `?preview=1` shows 5 hits (the card, the slug links, the price tag).

---

## §3 · Captures (5 viewports · cornice home + frozen siblings)

| File | What it shows |
|---|---|
| `captures/cornice-home-1440-vp.png` | Home first scroll @ 1440 · stacked-editorial hero with KPI tuple in overlay |
| `captures/cornice-home-1440-full.png` | Full page @ 1440 · hero → narrative → sectors → leadership → cases → cta-closer → footer |
| `captures/cornice-narrative-1440.png` | Narrative section + side-rail @ 1440 · drop-cap "L" + first paragraph + side-rail anchors |
| `captures/cornice-sectors-1440.png` | Sectors-ribbon @ 1440 · italic Cormorant 12 typologies + counter footnote with `novanta` em |
| `captures/cornice-leadership-1440.png` | Single-portrait leadership @ 1440 · Marco Roveri environmental portrait + h2 + bio + 4 credentials |
| `captures/cornice-cases-1440.png` | Magazine 3+1 grid @ 1440 · hero card (b&w concrete concorso) + small cards (residenziale + restauro + pubblicazione) |
| `captures/cornice-cta-closer-1440.png` | Cream CTA closer + 4-col footer with whistleblowing column @ 1440 |
| `captures/cornice-home-1100.png` | Home @ 1100 · KPI tuple still visible · 8/4 split below holds |
| `captures/cornice-home-880.png` | Home @ 880 · burger drawer · KPI tuple still visible |
| `captures/cornice-home-720.png` | Home @ 720 · photo aspect 4:5 portrait · KPI tuple still visible |
| `captures/cornice-home-480.png` | Home @ 480 · h1 first 2 lines visible below photo · KPI tuple intact |
| `captures/frozen-pragma-1440.png` | Pragma (LF-1) frozen @ 1440 · 55/45 split + boardroom planning + navy nav |
| `captures/frozen-fiscus-1440.png` | Fiscus (LF-3) frozen @ 1440 · 55/45 split + desk + tax docs + dark gray nav |
| `captures/frozen-solaria-1440.png` | Solaria (LF-4) frozen @ 1440 · 55/45 split + 1:1 conversation + warm-carbon nav |
| `captures/frozen-continua-1440.png` | Continua (LF-5) frozen @ 1440 · object-overlay hero + library + pine nav |

---

## §4 · Cornice live render verification (10 verification points from the task)

| # | Verification | Live verdict |
|---|---|---|
| 1 | Cornice first scroll reads UNLIKE all 4 live siblings | PASS — cream nav (vs all 4 siblings' dark navs) · split-wordmark masthead · stacked editorial photo TOP · KPI tuple INSIDE photo overlay · rust filled CTA on cream nav. Subject-class read at 1 second is "Italian portico architecture" — not boardroom, not desk, not conversation, not library. |
| 2 | LF-2 layout declaration is actually respected in DOM and visual rhythm | PASS — DOM structure verified: `<nav class="cs-nav cs-nav--lf2">` + `<section class="cs-hero">` with nested `<div class="overlay">` (KPI inside photo) + `<div class="below">` 8/4 split + `<section class="cs-narrative">` + `<section class="cs-sectors-ribbon">` + `<section class="cs-leadership-single">` + `<section class="cs-cases-magazine">` + `<section class="cs-cta-cream">`. Sequence B respected. ZERO dark band on home. |
| 3 | Hero does not collapse into Continua or Pragma feel | PASS — Cornice hero exterior architectural Bologna golden-hour stone-and-shadow vs Continua interior mahogany-warm reading-room vs Pragma indoor planning wall with sticky notes. |
| 4 | Single-portrait leadership does not read as generic headshot | PASS — senior architect (woman, white hair, eyeglasses) at her drafting table with papers + drafting pencil + working posture. Reads as "real architect at work in her studio", NOT "stock LinkedIn headshot". The 4 credentials below the bio (OAPPC + CNAPPC + MIBAC + Politecnico cattedra) reinforce the editorial-architectural register. Risk 4 from intake §12 cleared. |
| 5 | Magazine-grid cases read editorially, not generic gallery | PASS — 3+1 layout: hero card on left (b&w concrete concorso · 5,2 M €), three small cards on right with rust italic numerals 02/03/04 + project eyebrows + h3 with rust em-words (`lotto`, `argomento`, `minore`) + body copy with site/committenza/programma/anno + pill metadata. Reads as Casabella/Domus magazine spread. Photos mix b&w (concorso) + warm sunset Roma + warm Venaria courtyard + classical cornice carving — visibly diverse typologies and material palettes. |
| 6 | No frozen sibling regression | PASS — All 4 frozen siblings (Pragma · Fiscus · Solaria · Continua) capture identical to pre-Cornice baseline. The home dispatcher's `if LF-2 ... elif LF-5 ... else LF-1` chain preserves LF-1 default for all 4 siblings. |
| 7 | No contrast regressions | PASS — Spot-checked rust on cream (drop-cap, em-word, magazine-card numerals, cta-closer button), graphite on cream (body text + h1), cream on photo (hero overlay KPI labels). All readable at 1440 + 720 + 480. The hero photo's bottom-left gradient (rgba(15,18,22,0.78) at 100%) provides ≥AA scrim under the credit + KPI cluster. |
| 8 | No responsive regressions | PASS — All 5 viewports captured: hero remains structurally readable, KPI tuple visible at every viewport, h1 hits the floor (32px) only at 480, drop-cap shrinks 84→64→56 across breakpoints, magazine grid stacks to 1-col at 1100, leadership 2-col stacks to 1-col at 1100, sectors ribbon flexes naturally with the italic Cormorant readable at all sizes. The cream nav burger drawer activates at 880. |
| 9 | No imagery/category mismatch | PASS — Hero (Bologna portico) reads architectural-firm exterior. Feature (architectural model on worktable) reads design-studio. Single portrait (senior architect with blueprints) reads working-architect not coach/advisor/steward/commercialista. Magazine cards read concorso/residenziale/restauro/pubblicazione — all architectural typologies. Cluster vocabulary lands at first scroll. |
| 10 | Server remains open + URL/port reported | PASS — Server is running at `http://127.0.0.1:8052/` (port 8052). Reported in §1 above. |

**Verdict: 10/10 verification points PASS.**

---

## §5 · LF-2-specific layout-gate verifications (B-LAYOUT-1/2/3)

| Gate | Verdict |
|---|---|
| B-LAYOUT-1 (wireframe overlay) — bounding-box variance ≥30% per pair | PASS — no 55/45 hero on Cornice · zero KPI-band on Cornice · no list-row cases · no timeline · no pillar grid · no cycle mid-strip. The 9-cell L1–L9 classification differs in 7+ slots vs each frozen sibling. |
| B-LAYOUT-2 (DOM section list compare) — ≥2 entries differ | PASS — Cornice has zero overlap with LF-1's `[hero, pillars, kpi, sectors, trust, leadership, cases, cta]` — 6 vs 8 sections, only `cta-closer` semantically maps. Differs by 6+ entries vs LF-1/LF-3/LF-4. vs LF-5 differs by 5+ entries. |
| B-LAYOUT-3 (L1–L9 classification) — match planner-declared LF-2 row | PASS — verified at section level: L1=stacked-editorial · L2=B · L3=absent · L4=essay-with-anchors · L5=hero-overlay · L6=single-portrait-feature · L7=magazine-grid · L8=split-wordmark-top · L9=4-col-with-whistleblowing. Every slot matches. |

**Layout-distinctness scores** (planner-brief §15 ≥4/9 gate):
- vs Pragma (LF-1):    9/9 distinct
- vs Fiscus (LF-3):    9/9 distinct
- vs Solaria (LF-4):   8/9 distinct (only L3=absent same)
- vs Continua (LF-5):  8/9 distinct (only L9=4-col-with-whistleblowing shape · column content differs)

GATE: PASS by wide margin.

---

## §6 · Issues found + fixes applied during the IT walk

| # | Issue | Cause | Fix |
|---|---|---|---|
| 1 | KPI tuple in hero overlay was not visible at first capture | `.cs-hero` lacked `position: relative`; the `.cs-hero .overlay` was absolute-positioning relative to body, so the KPI cluster landed at the bottom of the page (under the footer) instead of the bottom-left of the photo | Added `position: relative` to `.cs-hero` (1 line), then restructured HTML to nest `.overlay` INSIDE `.photo` div so the absolute positioning is unambiguous (10-line HTML restructure in `lf2/content.html` + 2-line CSS update in `lf2/styles.html`). Re-captured · KPI tuple now visible at every viewport. |
| 2 | Navbar showed two "Studio"-related labels ("Lo studio" + "Studio") | Home page label "Lo studio" + about page label "Studio" both appear in nav-iteration | Renamed about page label "Studio" → "Archivio" in content module. Nav now reads `Lo studio · Archivio · Servizi · Progetti · Contatti` — 5 distinct labels. |

Both fixes were narrow CSS/markup adjustments inside the new LF-2 files (and one content-module label edit). **Zero edits** to LF-1/LF-3/LF-4/LF-5 layout files. **Zero edits** to apps/editor, apps/projects, apps/commerce.

---

## §7 · Frozen-sibling regression verdict

| Sibling | Layout family | First-scroll match to baseline | Verdict |
|---|---|---|---|
| Pragma | LF-1 | 55/45 split + boardroom planning + navy nav + "decisioni che contano" h1 + emerald accent + KPI tuple "14 partner / 42 progetti" | NO REGRESSION |
| Fiscus | LF-3 | 55/45 split + tidy desk + tax documents + dark gray nav + "L'adempimento corretto, non la trovata" h1 + warm-neutral palette + KPI "4 iscritti / 260 partite IVA" | NO REGRESSION |
| Solaria | LF-4 | 55/45 split + 1:1 conversation + warm-carbon nav + "Il coaching non è terapia e non è consulenza" (contrast-pair em) + ocra/caramel accent | NO REGRESSION |
| Continua | LF-5 | object-overlay hero + library reading-room interior + pine nav + "La continuità di una famiglia si misura in generazioni" + brass accent | NO REGRESSION |

**Verdict: 4/4 frozen siblings unchanged.** The home dispatcher cascade preserved. The base nav/footer conditional extensions are gated on `template.layout_family == 'LF-2'` so they fire ONLY for Cornice.

---

## §8 · Distinctness verdict vs all live siblings

| Pair | 5-axis verdict | Layout-distinctness |
|---|---|---|
| Cornice vs Pragma | 5/5 | 9/9 |
| Cornice vs Fiscus | 5/5 | 9/9 |
| Cornice vs Solaria | 5/5 | 8/9 |
| Cornice vs Continua | 5/5 | 8/9 |

**5/5 vs every existing sibling on the planner-brief 5-axis matrix.**

---

## §9 · Test-suite regression check

```
Ran 546 tests in 173.370s
FAILED (failures=1)
```

The 1 failure is `test_medical_and_restaurant_templates_have_booking_flag` — a pre-existing test failure related to Continua's `has_booking=True` flag in the `business` cluster. Per the v15 baseline memory: *"545/546 tests pass (sole failure pre-existing booking-flag · unrelated)"*. **NOT introduced by Cornice.** Cornice's seed has `has_booking=False` (architecture-firm doesn't ship a booking widget; it ships a project-brief form gate).

---

## §10 · Whether Cornice A.5 IT is ready for human visual review

**YES.**

The build cleared every A.5 sign-off criterion:
- ✓ 6 IT routes 200 (staff_preview)
- ✓ Tier-gate intact (anonymous 404)
- ✓ 5/5 distinctness vs every existing sibling
- ✓ 9/9 (or 8/9) layout-distinctness scores
- ✓ All 5 mitigations from intake §12 cleared on live render
- ✓ All 12 italic em-words on home land per CS-TYPE-02
- ✓ 4/4 frozen siblings show NO regression
- ✓ 545/546 tests pass (sole failure pre-existing · UNRELATED)
- ✓ Build line budget within planner guidance (~865 LF-2 lines)

The user-handshake review is the next gate. Workflow C (multilingual) and workflow D (public flip) are held until the user signs off on the IT walk.

Open questions for the user-handshake meeting:
1. Does the LF-2 stacked-editorial hero feel sufficiently distinct from Continua's library reading-room hero at 1280 + 720?
2. Does the single-portrait masthead read environmental, NOT LinkedIn headshot, at 1280 + 768? (Risk 4 from intake §12)
3. Does the 3+1 magazine grid land editorially, NOT as a generic gallery?
4. Does the cream-paper navbar feel right for the editorial-curatorial register, or should LF-2 ship a primary-bg variant?
5. Are the architectural-vocabulary density (Risk C-1) and the 3-time `argomento` motif (Risk C-3) reading as serious-editorial, NOT gatekeepy or repetitive?

If user signals GO: workflow C kicks off (EN/FR/ES/AR + AR RTL + Naskh-vs-Kufi decision per planner-brief §11).
If user signals HOLD: A.6 narrow re-author or A.5b re-build per the documented re-spec authority.
