# Cornice · Browser verification · A.6 IT review-lock

```yaml
report_type:        browser-verification
template_slug:      cornice-architettura
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · Cornice · A.6 review-lock IT walk
date:               2026-05-01
agent:              walk-verifier (A.6 review-lock pass)
walk_locale:        it
walk_viewports:     [1440, 1100, 880, 480]
walk_pages:         [home, studio, servizi, progetti, progetti/<slug>, contatti]
captures_dir:       factory/reports/browser-verification/cornice-a6-it-review-lock/captures/
status_tag:         IT-WALK-PASS · all 9 routes 200 · post-fix render verified · 4 frozen siblings clean
verdict:            PASS · IT draft truly review-locked
next_action:        User performs visual handshake on the live IT pages.
                    Workflow C (EN/FR/ES/AR + RTL) gated on user-handshake.
```

---

## §1 · Server URL + port left open

```
http://127.0.0.1:8052/

started:  python manage.py runserver 8052 --noreload
preview:  http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?preview=1
auth:     cornice_review / cornice-review-password (is_staff=True, is_superuser=True)
```

The server stays open at port 8052 for the user-handshake review.
Anonymous visitors do NOT see Cornice (tier=draft); staff with
`?preview=1` reach all 9 IT routes.

---

## §2 · Route status (HTTP)

| Route | Anonymous | Staff + `?preview=1` |
|---|---|---|
| `.../preview/` (home) | 404 | 200 |
| `.../preview/studio/` (about · "Archivio") | 404 | 200 |
| `.../preview/servizi/` (services) | 404 | 200 |
| `.../preview/progetti/` (cases list) | 404 | 200 |
| `.../preview/progetti/biblioteca-pietrasanta-concorso/` | 404 | 200 |
| `.../preview/progetti/via-volpe-roma-residenziale/` | 404 | 200 |
| `.../preview/progetti/palazzo-lignari-bologna-restauro/` | 404 | 200 |
| `.../preview/progetti/cornice-fronte-minore-saggio/` | 404 | 200 |
| `.../preview/contatti/` | 404 | 200 |

**Tier-gate intact**. Anonymous 404 confirms `tier=draft` is hidden
from public catalog. Staff `?preview=1` reaches every IT route. The
D-055 staff-preview semantics hold across the cluster (Pragma/
Fiscus/Solaria/Continua continue to be `tier=published_live` and
serve 200 anonymously; Cornice continues to be `tier=draft` and
serves 404 anonymously).

---

## §3 · Captures (post-fix · 1440 lead viewport + responsive sweep + frozen siblings)

| File | What it shows |
|---|---|
| **Pre-fix Cornice walk (recorded for diff)** | |
| `captures/01-cornice-home-1440-vp.png` | Home first scroll @ 1440 · stacked-editorial hero with KPI tuple in overlay (PRE-FIX) |
| `captures/02-cornice-home-1440-full.png` | Full home page @ 1440 (PRE-FIX · pre-magazine-grid hero card stretch) |
| `captures/03-cornice-narrative-1440.png` | Narrative section + side-rail @ 1440 |
| `captures/04-cornice-hero-h1-1440.png` | Hero h1 below photo @ 1440 |
| `captures/05-cornice-narrative-mid-1440.png` | Narrative middle (autore + regola pull-quotes) @ 1440 |
| `captures/06-cornice-sectors-1440.png` | Sectors-ribbon @ 1440 |
| `captures/07-cornice-leadership-1440.png` | Single-portrait leadership @ 1440 (PRE-FIX · Marco Roveri + woman portrait mismatch) |
| `captures/08-cornice-cases-magazine-1440.png` | Magazine 3+1 grid top @ 1440 |
| `captures/09-cornice-cases-rest-1440.png` | Magazine grid right column @ 1440 |
| `captures/10-cornice-cases-bottom-1440.png` | Magazine grid bottom @ 1440 (PRE-FIX · empty band below hero card) |
| `captures/11-cornice-cta-cream-1440.png` | CTA closer cream + footer top @ 1440 |
| `captures/12-cornice-footer-1440.png` | 4-col-with-whistleblowing footer @ 1440 |
| `captures/13-cornice-studio-1440-vp.png` | Studio (about) page @ 1440 (PRE-FIX · dark navbar inconsistency) |
| `captures/14-cornice-servizi-1440-vp.png` | Servizi page @ 1440 (PRE-FIX · dark navbar) |
| `captures/15-cornice-progetti-1440-vp.png` | Progetti list @ 1440 (PRE-FIX · dark navbar) |
| `captures/16-cornice-contatti-1440-vp.png` | Contatti page @ 1440 (PRE-FIX · dark navbar) |
| `captures/17-cornice-case-detail-1440-vp.png` | Biblioteca case detail @ 1440 (PRE-FIX) |
| `captures/r1-cornice-home-880-vp.png` | Home @ 880 (burger drawer entry point) |
| `captures/r2-cornice-home-480-vp.png` | Home @ 480 (mobile small) |
| `captures/r3-cornice-cases-1100.png` | Magazine grid stacked @ 1100 |
| **Pre-fix frozen sibling baselines (recorded before fixes)** | |
| `captures/sib-pragma-pre.png` | Pragma (LF-1) @ 1440 PRE-FIX |
| `captures/sib-fiscus-pre.png` | Fiscus (LF-3) @ 1440 PRE-FIX |
| `captures/sib-solaria-pre.png` | Solaria (LF-4) @ 1440 PRE-FIX |
| `captures/sib-continua-pre.png` | Continua (LF-5) @ 1440 PRE-FIX |
| **Post-fix Cornice walk** | |
| `captures/post-01-cornice-leadership-1440.png` | Leadership scroll @ 1440 BETWEEN-FIX (server still cached, name still Marco) |
| `captures/post-02-cornice-leadership-1440.png` | Leadership scroll @ 1440 POST-FIX after server restart (Marta + ARCHITETTA + bio fixed) |
| `captures/post-03-cornice-leadership-1440.png` | Leadership scroll @ 1440 POST-FIX with role subhead `fondatrice` corrected |
| `captures/post-04-cornice-cases-bottom-1440.png` | Magazine grid bottom @ 1440 BETWEEN-FIX (margin-top:auto attempt — solved alignment but introduced a different empty band, NOT shipped) |
| `captures/post-05-cornice-cases-mid-1440.png` | Magazine grid middle @ 1440 BETWEEN-FIX (showing the bad mid-card empty band) |
| `captures/post-06-cornice-cases-top-1440.png` | Magazine grid top @ 1440 POST-FIX (flex-grow on hero photo · dominant lead photo) |
| `captures/post-07-cornice-cases-bottom-1440.png` | Magazine grid bottom @ 1440 POST-FIX (card foots aligned · zero empty band) |
| `captures/post-08-cornice-studio-1440-vp.png` | Studio page @ 1440 POST-FIX (cream LF-2 nav with split wordmark + filled rust CTA) |
| `captures/post-09-cornice-servizi-1440-vp.png` | Servizi page @ 1440 POST-FIX (cream LF-2 nav consistent) |
| `captures/post-10-cornice-case-detail-1440-vp.png` | Case detail page @ 1440 POST-FIX (cream LF-2 nav + ARCHITETTO REFERENTE: Marta Roveri) |
| `captures/post-11-cornice-home-1440-vp.png` | Home first scroll @ 1440 POST-FIX (byte-equivalent to pre-fix: home was the only page where lf2 styles loaded · F2 invariant) |
| **Post-fix frozen sibling parity** | |
| `captures/post-sib-pragma.png` | Pragma (LF-1) @ 1440 POST-FIX (byte-equivalent to pre-fix) |
| `captures/post-sib-fiscus.png` | Fiscus (LF-3) @ 1440 POST-FIX (byte-equivalent to pre-fix) |
| `captures/post-sib-solaria.png` | Solaria (LF-4) @ 1440 POST-FIX (byte-equivalent to pre-fix) |
| `captures/post-sib-continua.png` | Continua (LF-5) @ 1440 POST-FIX (byte-equivalent to pre-fix) |

---

## §4 · Cornice live render verification (10 verification points · post-fix)

| # | Verification | Live verdict (post-fix) |
|---|---|---|
| 1 | Hero overlay quality (KPI tuple inside photo · NOT separate dark band) | PASS — KPI tuple "47 PROGETTI / 18 ANNI / 6 CITTÀ" sits inside the photo's bottom-left overlay frame at every viewport (1440, 1100, 880, 480). Credit caption "Bologna · portico restaurato · 2023 · fascicolo n. 31" reads above the KPI cluster. Cream-on-photo with rgba(15,18,22,0.78) gradient scrim — readable on golden-hour stone. |
| 2 | Magazine-grid quality (3+1 with editorial dominant hero photo) | PASS — F3 fix landed: hero card photo (b&w concrete concorso) now ~720px tall (vs ~480px pre-fix), dominating the spread. Body + meta clustered at the foot. Right column 3 small cards stack normally. Card foots align at y=7461 in DOM (measured). Reads as Casabella/Domus magazine spread. |
| 3 | Leadership single-portrait credibility (environmental NOT headshot · photo↔copy agreement) | PASS — F1 fix landed: photo (senior architect with white hair, glasses, suit jacket, drinking coffee while reviewing drawings) now reads as Marta Roveri. Eyebrow `STUDIO FOUNDER · ARCHITETTA`. Heading `Marta <em>Roveri</em>` (rust em on Roveri preserved). Role `fondatrice · responsabile editoriale dei fascicoli`. Bio para 1: `Marta Roveri ha aperto Cornice... Si è formata al Politecnico...`. 4 credentials: OAPPC + CNAPPC + MIBAC + Politecnico Professoressa a contratto. Photo and copy now agree. |
| 4 | Navbar polish (cream LF-2 chrome consistent across home + 8 inner pages) | PASS — F2 fix landed: home + studio + servizi + progetti + 4 case-detail + contatti all render the cream-paper LF-2 nav with split wordmark `CORNICE / studio di architettura` + filled-rust CTA `APRI UN FASCICOLO PROGETTO`. Hamburger lines read graphite (not on-dark). Active link underline reads rust. Chrome uniform across the family. Home byte-equivalent before/after the move. |
| 5 | Footer polish (4-col-with-whistleblowing on home + inner pages) | PASS — STUDIO + tagline + body | PAGINE links | CONTATTI (address + phone + email + hours) | SEGNALAZIONI whistleblowing column with D.lgs. 24/2023 channel + email + linked policy. Bottom row: copyright + Albo OAPPC + privacy/cookie/note legali. Footer was already correct at A.5; F2 didn't disturb it. |
| 6 | Responsive behavior (1440/1100/880/480) | PASS — 1440: 8/4 hero split + magazine 2-col + leadership 2-col. 1100: hero 8/4 holds + magazine starts stacking + leadership 2-col stacks to 1-col. 880: cream nav burger drawer activates + KPI tuple still visible + h1 still readable. 480: mobile photo aspect compressed but KPI overlay still clean + h1 floors at 32px. No horizontal scroll. No content drop. |
| 7 | Contrast/readability | PASS — Spot-checked rust on cream (drop-cap, em-words, magazine card numerals, cta-closer button, focus rings); graphite on cream (body text, h1, bio text); cream/on-dark on photo (hero overlay KPI labels). All readable at every viewport. The hero photo's bottom-left gradient (rgba(15,18,22,0.78) at 100%) provides ≥AA scrim under the credit + KPI cluster. Filled-rust button on cream provides clear CTA contrast. |
| 8 | Route usability in draft preview (legitimate staff-preview path) | PASS — All 9 IT routes 200 on staff session with `?preview=1`. Anonymous returns 404 on every Cornice route (catalog list, all 9 page slugs). Catalog list `/templates/business/` shows 0 hits for `cornice-architettura` anonymous, 5 hits with staff `?preview=1`. D-055 / CS-MARKET-01 staff-preview semantics holding. |
| 9 | Frozen sibling stability | PASS — 4/4 frozen siblings (Pragma · Fiscus · Solaria · Continua) byte-equivalent before and after the A.6 fixes. F1 is content-only inside Cornice's content module. F2 is selector-scoped to `.cs-nav--lf2` (only Cornice). F3 is in lf2/styles.html (only Cornice's home loads it). |
| 10 | Premium/editorial feel on first scroll and full page | PASS — First scroll: cream nav + golden-hour Bologna portico + KPI overlay + fascicolo credit reads as architectural-editorial publication, not corporate-advisory. H1 below photo with rust em on `argomento` builds the curatorial argument. Full page: narrative drop-cap + 3 italic Cormorant pull-quotes + sectors-ribbon + (post-fix) editorial leadership masthead with credible founder identity + (post-fix) dominant magazine spread + cream CTA closer with voice-anchor verbatim. The whole page reads consistently editorial. |

**Verdict: 10/10 verification points PASS.**

---

## §5 · LF-2-specific layout-gate verifications (post-fix · B-LAYOUT-1/2/3)

| Gate | Verdict |
|---|---|
| B-LAYOUT-1 (wireframe overlay) — bounding-box variance ≥30% per pair | PASS — no 55/45 hero on Cornice · zero KPI-band on Cornice · no list-row cases · no timeline · no pillar grid · no cycle mid-strip. 9-cell L1–L9 differs in 7+ slots vs each frozen sibling. F3 STRENGTHENS L7 magazine-grid distinctness — dominant hero photo reads less like list-row or timeline. |
| B-LAYOUT-2 (DOM section list compare) — ≥2 entries differ | PASS — Cornice has zero overlap with LF-1's `[hero, pillars, kpi, sectors, trust, leadership, cases, cta]` — 6 vs 8 sections, only `cta-closer` semantically maps. Differs by 6+ entries vs LF-1/LF-3/LF-4. vs LF-5 differs by 5+ entries. |
| B-LAYOUT-3 (L1–L9 classification) — match planner-declared LF-2 row | PASS — verified at section level: L1=stacked-editorial · L2=B · L3=absent · L4=essay-with-anchors · L5=hero-overlay · L6=single-portrait-feature · L7=magazine-grid · L8=split-wordmark-top · L9=4-col-with-whistleblowing. Every slot matches. |

**Layout-distinctness scores** (planner-brief §15 ≥4/9 gate · post-fix):

- vs Pragma (LF-1):    9/9 distinct
- vs Fiscus (LF-3):    9/9 distinct
- vs Solaria (LF-4):   8/9 distinct (only L3=absent same)
- vs Continua (LF-5):  8/9 distinct (only L9=4-col-with-whistleblowing shape · column content differs)

GATE: PASS by wide margin.

---

## §6 · Issues found + fixes applied during the A.6 walk

| # | Issue | Severity | Cause | Fix |
|---|---|---|---|---|
| F1 | Founder photo↔copy gender mismatch (woman in photo, "Marco Roveri" + masculine Italian in copy) | review-blocking | Curator deliberately chose senior-woman portrait in A.3 imagery pack; copy author wrote male first name in A.4 copy authoring; A.5 walk didn't catch the mismatch via partial captures | Renamed Marco→Marta and feminized gendered Italian (16 surfaces in `apps/catalog/template_content_cornice.py`). Surname Roveri preserved (em-word + lead_partner refs unchanged). Voice anchor untouched. |
| F2 | LF-2 cream-paper nav only renders on home; inner pages fall back to LF-1 dark-bar default | high (chrome consistency) | The cs-nav--lf2 body styles lived in `_layouts/lf2/styles.html` which is included only by the home dispatcher; inner pages add the `cs-nav--lf2` class but don't load the matching styles | Moved the ~55-line cs-nav--lf2 body styles from lf2/styles.html into _base.html (shared chrome block, immediately after cs-nav-cta--lf2). Mirrors how cs-nav--lf5 already lives in _base.html. lf2/styles.html replaced the moved block with a 4-line breadcrumb comment. |
| F3 | Magazine-grid hero card has visible empty band below the meta pill (~350-450px at 1440) | medium (editorial rhythm) | Hero card spans grid-rows 1/4 to match the 3-card stack; CSS grid stretches the box but inner `.copy` content gathers at top with `flex: 1`; photo aspect-ratio is fixed so it can't absorb extra space | Replaced `.card--hero .thumb { aspect-ratio: 16/9 }` with `{ flex: 1; min-height: 360px }` so the photo grows to absorb extra height; removed `flex: 1` from `.copy` so copy block sits at content height. Card foots now align at y=7461 (DOM-verified). |

A previous between-fix attempt on F3 used `margin-top: auto` on
the .pill — that solved card-foot alignment but introduced a
visible empty band BETWEEN body text and pill in the middle of
the hero card (different rhythm break, not shipped). The
flex-grow approach is the editorial solution.

All three fixes are narrow and scoped to LF-2 / Cornice. **Zero
edits** to LF-1/LF-3/LF-4/LF-5 layout files. **Zero edits** to
apps/editor, apps/projects, apps/commerce.

---

## §7 · Frozen-sibling regression verdict (post-fix)

| Sibling | Layout family | First-scroll match to baseline | Verdict |
|---|---|---|---|
| Pragma | LF-1 | 55/45 split + boardroom planning + navy nav + emerald accent + KPI tuple "14 partner / 42 progetti" + h1 "Dove si prendono le decisioni che contano." | NO REGRESSION |
| Fiscus | LF-3 | 55/45 split + tidy desk + tax docs + dark gray nav + warm-neutral palette + h1 "L'adempimento corretto, non la trovata." + KPI "4 iscritti / 260 partite IVA" | NO REGRESSION |
| Solaria | LF-4 | 55/45 split + 1:1 conversation + warm-carbon nav + h1 "Il coaching non è terapia e non è consulenza." + ocra/caramel accent | NO REGRESSION |
| Continua | LF-5 | object-overlay hero + library reading-room interior + pine nav + brass accent + h1 "La continuità di una famiglia si misura in generazioni." | NO REGRESSION |

**Verdict: 4/4 frozen siblings unchanged.** F2 (cs-nav--lf2 lift)
is selector-scoped — does not match `.cs-nav` (Pragma/Fiscus/
Solaria) or `.cs-nav--lf5` (Continua). F3 (magazine grid hero
card) lives in lf2/styles.html which only Cornice's home loads.
F1 is content-only inside Cornice's content module. The home
dispatcher cascade preserved. The base.html nav/footer
conditional extensions are gated on `template.layout_family ==
'LF-2'` so they fire ONLY for Cornice.

---

## §8 · Distinctness verdict vs all live siblings (post-fix)

| Pair | 5-axis verdict | Layout-distinctness |
|---|---|---|
| Cornice vs Pragma | 5/5 | 9/9 |
| Cornice vs Fiscus | 5/5 | 9/9 |
| Cornice vs Solaria | 5/5 | 8/9 |
| Cornice vs Continua | 5/5 | 8/9 |

**5/5 vs every existing sibling.** Layout-distinctness scores
unchanged from A.5. The L7 magazine-grid distinctness is in fact
STRENGTHENED by F3 — the dominant hero photo makes the cases
shape read even less like Pragma/Fiscus/Solaria's numbered list-
row.

---

## §9 · Test-suite regression check

```
Ran 546 tests in 176.056s
FAILED (failures=1)
```

The 1 failure is `test_medical_and_restaurant_templates_have_booking_flag`
— pre-existing, related to Continua's `has_booking=True` flag in
the `business` cluster, documented in v15 baseline as
*"545/546 tests pass (sole failure pre-existing booking-flag ·
unrelated)"*. **NOT introduced by A.6.** Same failure count and
same failure name as pre-fix.

---

## §10 · Whether Cornice A.6 IT is locked for human visual review

**YES.**

The A.6 review-lock cleared every sign-off criterion:

- 9 IT routes 200 (staff_preview)
- Tier-gate intact (anonymous 404)
- Founder photo↔copy gender alignment (F1 fixed)
- Cream LF-2 nav consistent across home + 8 inner pages (F2 fixed)
- Magazine-grid editorial spread with dominant hero photo (F3 fixed)
- 5/5 distinctness vs every existing sibling
- 9/9 (or 8/9) layout-distinctness scores
- All 5 mitigations from intake §12 cleared on live render
- All 12 italic em-words on home land per CS-TYPE-02
- 4/4 frozen siblings show NO regression
- 545/546 tests pass (sole failure pre-existing · UNRELATED)
- A.6 fix budget within scope rules (3 source files modified · zero edits to apps/editor, apps/projects, apps/commerce, other archetypes)

Open questions for the user-handshake meeting (refined from A.5):

1. Does the LF-2 stacked-editorial hero feel sufficiently distinct from Continua's library reading-room hero at 1440 + 720?
2. Does the post-fix single-portrait masthead read environmental architect (Marta Roveri at her studio drafting table) at 1440 + 768?
3. Does the post-fix 3+1 magazine spread (dominant hero photo) land editorially, NOT as a generic gallery?
4. Does the cream-paper navbar (now consistent across all 9 pages) feel right for the editorial-curatorial register?
5. Are the architectural-vocabulary density (Risk C-1) and the 3-time `argomento` motif (Risk C-3) reading as serious-editorial, NOT gatekeepy or repetitive?

If user signals **GO**: workflow C kicks off (EN/FR/ES/AR + AR
RTL + Naskh-vs-Kufi decision per planner-brief §11). Tier flip to
`published_live` is held until workflow D, post-multilingual.

If user signals **HOLD**: A.7 narrow re-author or A.6b re-build
per the documented re-spec authority.
