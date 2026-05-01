# Cornice · A.6 IT Review-Lock · 5th corporate-suite sibling · 1st LF-2 occupant

```yaml
report_type:        a6-review-lock
template_slug:      cornice-architettura
archetype:          corporate-suite
sub_cluster:        architecture-firm · single-principal studio (editorial-led)
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · Cornice · A.6 review-lock (IT-only · pre-multilingual)
date:               2026-05-01
agent:              review-lock-builder (Phase X.5 A.6)
inputs_consumed:
  - factory/reports/cornice/cornice-a5-it-build.md
  - factory/reports/browser-verification/cornice-a5-it-build.md
  - factory/reports/scorecard/cornice-a5-it-build/*
  - factory/reports/hardening/lf2-fifth-sibling-pilot.md
  - factory/reports/corporate-suite/cornice-architettura/intake.md
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md
  - factory/reports/corporate-suite/cornice-architettura/prebuild-quick-checks.md
  - factory/reports/imagery/cornice-architettura/*
  - factory/reports/copy/cornice-architettura/*
  - current Cornice implementation (apps/catalog/template_content_cornice.py · DNA · LF-2 layout files)
  - frozen sibling state (Pragma · Fiscus · Solaria · Continua · all live anonymous)
status_tag:         A6-REVIEW-LOCK-COMPLETE · IT draft truly review-locked
verdict:            LOCKED FOR USER VISUAL REVIEW · IT-only · tier=draft preserved
next_action:        User performs the visual handshake on Cornice IT. On GO,
                    workflow C kicks off (EN/FR/ES/AR + AR RTL · Naskh-vs-Kufi
                    decision per planner-brief §11). On HOLD, A.7 narrow re-author.
```

This file is the binding A.6 review-lock narrative. It pairs with:
- `factory/reports/browser-verification/cornice-a6-it-review-lock.md` — IT walk evidence + frozen-sibling regression check + responsive matrix (post-fix)
- `factory/reports/scorecard/cornice-a6-it-review-lock/*.md` — 8 scorecard panels (build · style · contrast · responsive · browser · gatekeeper · scorecard + summary)

---

## §1 · A.6 framing (why this phase exists)

A.5 closed with the build CLEARED FOR USER VISUAL REVIEW. The orchestrator
held the multilingual workflow C and the public flip workflow D pending a
human visual review of the IT draft. A.6 is the review-lock pass that
hardens the IT draft to a conservative review standard so the user can
make a clean GO/HOLD call without being distracted by review-blocking
defects.

The work is intentionally narrow:
- IT only (no EN/FR/ES/AR yet)
- tier=draft preserved (no public flip)
- frozen siblings (Pragma · Fiscus · Solaria · Continua) untouched
- apps/editor / apps/projects / apps/commerce untouched
- no new archetype, no new layout family, no widening of LF-2
- LF-2 distinctness vs the other 4 siblings preserved with margin

The scope rule for A.6 was: **fix only what is needed to make the IT
draft truly review-locked**. Three findings were promoted to fix-status
during the live walk (one review-blocking, one chrome-consistency, one
editorial-rhythm). All three are documented in §3 below with their
specific surface, root cause, and minimal fix.

---

## §2 · Live walk methodology

Server: `python manage.py runserver 8052 --noreload` at
`http://127.0.0.1:8052/`.

Auth: staff user `cornice_review` / `cornice-review-password`
(`is_staff=True · is_superuser=True`). Tier=draft means anonymous
visitors get 404; staff with `?preview=1` reach all 9 IT routes.

Browser: Playwright MCP (mandatory per task constraints).

Walk shape (this is the conservative A.6 walk shape, mirroring
A.5 · re-bound on the post-fix render):

| Layer | Surface |
|---|---|
| Routes | 9 IT routes — home, studio (Archivio), servizi, progetti list, 4 case-detail slugs, contatti |
| Viewports | 1440 (lead), 1100 (mid-tablet), 880 (burger entry), 480 (mobile small) — re-checked on the post-fix render |
| Hero | Photo + KPI overlay + below-fold 8/4 (h1 left, side-quote right) |
| Narrative | Drop-cap + 3 pull-quotes + sticky 4-link side-rail |
| Sectors-ribbon | 12 italic Cormorant typologies + counter footnote |
| Leadership | LF-2 L6 single-portrait + h2 + role + bio + 4 credentials |
| Magazine grid | LF-2 L7 3+1 (1 hero card + 3 small cards) |
| CTA closer cream | Voice-anchor verbatim recurrence + filled rust button |
| Navbar | LF-2 cream-paper masthead — checked on home AND every inner page |
| Footer | LF-2 4-col-with-whistleblowing — checked on home AND every inner page |
| Frozen sibling pre/post | Pragma + Fiscus + Solaria + Continua — anonymous 200 + first-scroll capture both sides of the fix landing |

Captures land in `factory/reports/browser-verification/cornice-a6-it-review-lock/captures/`.

---

## §3 · Findings + fixes applied

Three findings surfaced during the live walk. All three are scoped to
LF-2 / Cornice and ship inside the A.6 review-lock budget. None of the
fixes touch apps/editor, apps/projects, apps/commerce, or any other
archetype.

### F1 · Founder gender mismatch (review-blocking)

**Symptom**. The leadership single-portrait at home L6 shows the
RDNE Stock 5915290 photo of a senior architect with white hair,
glasses, suit jacket, drinking coffee while reviewing drawings — a
woman. The bio names "Marco Roveri" with masculine gendered Italian
(`Si è formato`, `viene nominato Professore`, `Marco Roveri è
abilitato`, leadership eyebrow `STUDIO FOUNDER · ARCHITETTO`,
leadership role `fondatore`, intro `Un architetto fondatore`,
team-card role `Architetto`, `Studio Founder · Architetto`, junior
bio `(relatore: Roveri)`).

**Why it blocks review**. A user reviewing the IT pages would, at
the leadership scroll, read photo + name + role together. If those
disagree on gender, the masthead loses credibility — the masthead
is the LF-2 family's load-bearing cell (planner-brief §13 Risk 4
"single-portrait stock-headshot collapse"). The intake §12 binding
triple selected an environmental senior architect; the curator
deliberately chose a woman; the copy author wrote a male first
name. A.5 didn't catch the mismatch because the leadership scroll
was inspected via partial captures.

**Fix**. Rename the founder Marco→Marta and feminize the gendered
Italian to agree with the photo. The surname Roveri is preserved
so the leadership h2 em on `Roveri` stands and all case-detail
`lead_partner` references stay structurally intact. Specific
edits in `apps/catalog/template_content_cornice.py`:

| Surface | Before | After |
|---|---|---|
| Home leadership label | `STUDIO FOUNDER · ARCHITETTO` | `STUDIO FOUNDER · ARCHITETTA` |
| Home leadership heading | `Marco <em>Roveri</em>` | `Marta <em>Roveri</em>` |
| Home leadership role subhead | `fondatore · responsabile editoriale dei fascicoli` | `fondatrice · responsabile editoriale dei fascicoli` |
| Home leadership bio (para 1) | `Marco Roveri ha aperto Cornice... Si è formato al Politecnico...` | `Marta Roveri ha aperto Cornice... Si è formata al Politecnico...` |
| Home leadership credentials (4th) | `Politecnico di Milano · Professore a contratto · Cattedra di Restauro` | `Politecnico di Milano · Professoressa a contratto · Cattedra di Restauro` |
| Studio about intro | `Milano. Un architetto fondatore, due collaboratori...` | `Milano. Un'architetta fondatrice, due collaboratori...` |
| Studio history 2008 | `Marco Roveri apre Cornice...` | `Marta Roveri apre Cornice...` |
| Studio history 2014 | `Marco Roveri ottiene la qualifica...` | `Marta Roveri ottiene la qualifica...` |
| Studio history 2017 | `Marco Roveri viene nominato Professore...` | `Marta Roveri viene nominata Professoressa...` |
| Studio team intro | `Lo studio è formato da un architetto fondatore...` | `Lo studio è formato da un'architetta fondatrice...` |
| Studio team[0] name | `Marco Roveri` | `Marta Roveri` |
| Studio team[0] role | `Studio Founder · Architetto` | `Studio Founder · Architetta` |
| Studio team[0] bio first word | `Fondatore.` | `Fondatrice.` |
| Studio team[2] junior bio | `(relatore: Roveri)` | `(relatrice: Roveri)` |
| Servizi card 03 blurb | `Marco Roveri è abilitato al restauro...` | `Marta Roveri è abilitata al restauro...` |
| Case-detail × 4 lead_partner | `Marco Roveri · Studio Founder` | `Marta Roveri · Studio Founder` (auto via replace_all) |

**Out-of-scope deliberately kept as-is** (these are about
generic role-references or about the form-filling visitor, not
about Marta directly · keeping them avoids over-feminizing a
team description that has 2 unspecified gender collaborators):
- Privacy-consent line `Sono informato del canale whistleblowing` —
  this is the form-filler's declaration, not Marta. Italian inclusive
  forms would say `informato/a` but that's a separate inclusivity
  concern, not Cornice's review-lock scope.
- Generic principle line `La firma del progetto è quella di un
  architetto solo` — this is the studio's authoriality principle, not
  Marta-specific. The masculine `architetto` works as the role-term
  in Italian formal usage.
- Team plural `Tre architetti, una sola sede` — generic plural,
  Italian masculine plural handles mixed/unknown groups.
- Case-detail label `ARCHITETTO REFERENTE` — formal title, gender-
  neutral in formal Italian usage (parallel to `Direttore`,
  `Responsabile`).

**Verification**. Re-walked the leadership scroll at 1440 post-fix.
Eyebrow reads `STUDIO FOUNDER · ARCHITETTA`. h2 reads `Marta
<em>Roveri</em>` (rust em on Roveri preserved). Role subhead reads
`fondatrice · responsabile editoriale dei fascicoli` (italic
Cormorant). Bio paragraph 1 reads `Marta Roveri ha aperto
Cornice... Si è formata al Politecnico...`. Photo↔copy now agree.
Re-walked the studio (about) page: subhead reads `Un'architetta
fondatrice, due collaboratori`. Team card 1 reads `Marta Roveri ·
Studio Founder · Architetta · Fondatrice. Politecnico di Milano...`.
Servizi card 03 reads `Marta Roveri è abilitata al restauro...`.
Case-detail meta reads `ARCHITETTO REFERENTE: Marta Roveri ·
Studio Founder` (label kept, name corrected). All 9 routes 200 on
staff session. PASS.

### F2 · LF-2 nav chrome only on home (chrome-consistency, high)

**Symptom**. The home page renders the cream-paper LF-2 nav with
split wordmark + filled rust CTA. Inner pages (about · servizi ·
progetti list · case detail · contatti) render the LF-1 default
dark `cs-nav` background with white text and a small rust button.
At the chrome-class layer, `_base.html:1134` adds `cs-nav--lf2`
on every LF-2 page — but the body styles for that class (cream
background, split-wordmark typography, link colors, hamburger
graphite) lived ONLY in `_layouts/lf2/styles.html`, which the
home dispatcher includes; inner pages don't include lf2/styles.html
and therefore fall back to the LF-1 base styling.

**Why it matters**. Cornice's chrome polarity is a load-bearing
LF-2 distinctness signal — the cream-paper masthead is what makes
the family read as editorial publication (Casabella, Domus) rather
than corporate-advisory boardroom. If only the home shows the
cream nav and every inner page shows a dark bar, the user reading
the IT pages would see a chrome inconsistency at every navigation
hop, and might (rightly) think "the cream nav is a home-only
hero treatment, not a family identity". That undermines the
LF-2 declaration in `intake.md §3` and `planner-brief.md §6`.

**Why A.5 missed it**. A.5's walk captured home then frozen
siblings. Inner Cornice pages were captured but the chrome
delta was masked because the inspector was reading the inner
pages as "successful 200 responses with the right h1 / lead /
sections rendering" rather than "chrome polarity matches the
family declaration". A.6 inspected each inner page chrome
specifically and the delta surfaced.

**Fix**. Move the `cs-nav--lf2` body styles from
`_layouts/lf2/styles.html` (~55 lines) into
`_base.html`, right next to the existing `.cs-nav--lf5` block
(_base.html:316). This mirrors how Continua's LF-5 chrome lives in
_base.html and is therefore inherited on every LF-5 page. The
selector specificity is unchanged (`.cs-nav.cs-nav--lf2 { ... }`),
so the home render is byte-equivalent before and after the move,
but the inner pages now inherit the cream chrome consistently.

The lf2/styles.html block is replaced with a 4-line breadcrumb
comment pointing back to _base.html so future readers can find
the shared chrome.

**Files changed**:
- `templates/live_templates/business/corporate-suite/_base.html` —
  added `.cs-nav.cs-nav--lf2` block (~55 lines) inside the existing
  `extra_css` chrome block, immediately after `.cs-nav-cta--lf2`
  rules and before the LF-5 4-col-whistleblowing footer block.
- `templates/live_templates/business/corporate-suite/_layouts/lf2/styles.html` —
  removed the 55-line nav-body block at lines 809-871; replaced
  with a 4-line comment breadcrumb pointing to _base.html.

**Verification**. Re-walked all 9 IT routes post-fix. Every page
now renders the cream-paper nav with split wordmark `CORNICE /
studio di architettura` and filled-rust CTA. Hamburger reads
graphite (not on-dark white). Active link underline reads rust.
The chrome class is uniform across the family. Home is byte-
equivalent before/after the move (CSS rules are the same, just
moved location). Inner pages now match home. PASS.

### F3 · Magazine-grid hero card empty space (editorial-rhythm, medium)

**Symptom**. At 1440, the LF-2 L7 magazine grid (3+1) shows the
hero card on the left spanning grid-rows 1/4 (matching the height
of the 3-card stack on the right). The hero card's `.copy` block
(eyebrow + h3 + body + meta-pill) is significantly shorter than
the 3-card stack height; CSS grid stretches the card box but the
inner content gathers at the top and leaves a visible empty band
of ~350-450px below the meta pill. The right column's card-04
extends below the hero card's pill, breaking the editorial spread
baseline alignment.

**Why it matters**. The LF-2 L7 magazine-grid is the second-most
load-bearing layout cell in the family (after L6 single-portrait),
because it's the case-shape signature that distinguishes Cornice
from Pragma/Fiscus/Solaria's numbered list-row and Continua's
vertical timeline. A magazine spread visually depends on baseline
alignment between the hero column and the multi-card column. If
the hero card looks "short" with empty space below, it reads as a
broken layout, NOT a Casabella editorial spread.

**Fix**. Use flex-grow on the hero card's photo (`.thumb`) so the
photo absorbs the extra height and the card foot aligns with the
3-card stack foot. Specifically, replace the `aspect-ratio: 16/9`
constraint on `.cs-cases-magazine .card--hero .thumb` with `flex:
1` + `min-height: 360px`, and remove `flex: 1` from `.copy`. The
photo grows; the copy block sits at content height; the meta pill
sits at the natural foot of the copy block. The card foot now
aligns with card-04 foot on the right.

This is editorially correct — Casabella / Domus magazine spreads
with a hero+stack layout always have a dominant lead photo on the
hero side, NOT a small lead photo with a tall meta-trail. The
photo IS the editorial weight.

**Files changed**:
- `templates/live_templates/business/corporate-suite/_layouts/lf2/styles.html` —
  swapped `.card--hero .thumb { aspect-ratio: 16/9 }` for `{ flex: 1;
  min-height: 360px }`, and removed `flex: 1` from `.card--hero .copy`.

**Verification**. Re-walked the magazine grid post-fix. Left
column: hero card photo now ~720px tall (vs. ~480px before), body
+ meta clustered at the foot. Right column: 3 cards stack at the
same combined height as before. Card foot baselines align (both
columns end at y=7461 — measured live in DOM). The editorial
spread feel is restored. The b&w concrete concorso photo now
dominates the spread the way a hero photo should. Did not retain
the margin-top:auto on .pill (a previous attempt in this same A.6
session) because that solved the alignment but introduced a
visible empty band between body and pill in the middle of the
hero card — a different but equally bad rhythm. The flex-grow
approach is the correct editorial solution. PASS.

---

## §4 · Frozen sibling regression verdict (post-fix)

| Sibling | Layout family | First-scroll vs A.5 baseline | Verdict |
|---|---|---|---|
| Pragma | LF-1 | 55/45 split + boardroom planning + navy nav + emerald accent + KPI tuple `14 partner / 42 progetti` + h1 `Dove si prendono le decisioni che contano.` (em on `che contano`) | NO REGRESSION |
| Fiscus | LF-3 | 55/45 split + tidy desk + tax docs + dark gray nav + warm-neutral palette + h1 `L'adempimento corretto, non la trovata.` + KPI `4 iscritti / 260 partite IVA` | NO REGRESSION |
| Solaria | LF-4 | 55/45 split + 1:1 conversation + warm-carbon nav + h1 `Il coaching non è terapia e non è consulenza.` + ocra/caramel accent + KPI `60 minuti / 20-30 minuti / ICF-MCC continuativa` | NO REGRESSION |
| Continua | LF-5 | object-overlay hero + library reading-room interior + pine nav + brass CTA + h1 `La continuità di una famiglia si misura in generazioni.` + brass em on `generazioni` | NO REGRESSION |

**Verdict: 4/4 frozen siblings unchanged.** F2 (the cs-nav--lf2
move into _base.html) is selector-scoped to `.cs-nav--lf2`; it
does not match Pragma/Fiscus/Solaria (which have no LF-modifier
class) or Continua (which has `.cs-nav--lf5`). F3 (the magazine-
grid hero card) is selector-scoped to `.cs-cases-magazine .card--hero`
which lives only inside lf2/styles.html which only Cornice's home
includes. F1 is content-only inside Cornice's content module, no
spillover.

The home dispatcher chain (`if LF-2 ... elif LF-5 ... else LF-1`)
in `home.html` is unchanged. The base.html nav/footer conditional
extensions are gated on `template.layout_family == 'LF-2'` so they
fire ONLY for Cornice.

**Anonymous HTTP check (frozen sibling tier-gate intact)**:

```
pragma-corporate-suite : 200
fiscus-commercialista : 200
solaria-coaching      : 200
continua-stewardship  : 200
```

---

## §5 · Cornice distinctness verdict (post-fix · 5-axis triangulation)

The intake §3.2 studio-name swap test, the §17 sibling-collision
audit, and the planner-brief §6 distinctness scoring re-bind on
the live IT render at A.6 walk. Verdict per axis (no regression
vs A.5 — the A.6 fixes are scoped to chrome consistency + leadership
copy + magazine grid rhythm, none of which affect distinctness
axes):

| Axis | vs Pragma | vs Fiscus | vs Solaria | vs Continua | Verdict |
|---|---|---|---|---|---|
| Voice (`argomento` curatorial-architectural) | distinct (decisional gravity) | distinct (presidio scadenze) | distinct (bounded coaching method) | distinct (stewardship temporal `generazioni`) | PASS |
| Palette (graphite + pietra-serena + rust) | distinct (navy/blue/emerald) | distinct (warm-neutral/gold/blu-notte) | distinct (warm-carbon/ocra/caramel) | distinct (pine/pewter/brass) | PASS |
| Hero geometry (stacked-editorial 8/4 + KPI in photo overlay) | distinct (55/45 split) | distinct (55/45 split) | distinct (55/45 split) | distinct (object-overlay) | PASS |
| Hero subject (Bologna golden-hour portico · zero people · exterior architectural) | distinct (boardroom planning · 1 person) | distinct (desk + tax documents · zero people but task-class) | distinct (1:1 conversation · 2 people) | distinct (library reading-room interior · zero people but interior-mahogany) | PASS |
| Cases shape (3+1 magazine-grid · post-fix dominant hero photo) | distinct (numbered list-row) | distinct (numbered list-row) | distinct (numbered list-row) | distinct (vertical timeline) | PASS |

**5/5 vs every existing sibling.** Layout-distinctness scores
unchanged from A.5 (9/9 vs Pragma+Fiscus, 8/9 vs Solaria+Continua).
Distinctness gate `DISTINCTNESS_RULES.md §1 ≥4/5` cleared with
the same wide margin. The L7 magazine-grid distinctness is in
fact STRENGTHENED by F3 — the hero card now dominates the spread
the way a 3+1 magazine layout should, making the cases shape read
even less like Pragma/Fiscus/Solaria's numbered list-row.

---

## §6 · Voice + content fidelity (post-fix)

**Voice anchor verbatim** at exactly two places on the home page:

- Hero h1: `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` ✓
- CTA-closer h2: `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` ✓

**Em-word audit on home (CS-TYPE-02 single em per heading)** —
verified live post-fix:

| Surface | Em-word | Polarity |
|---|---|---|
| Hero h1 | `argomento` | rust italic |
| Hero side-quote | `argomenta` | rust italic |
| Pull-quote 1 | `prima` | rust italic |
| Pull-quote 2 | `autore` | rust italic |
| Pull-quote 3 | `regola` | rust italic |
| Sectors counter footnote | `novanta` | rust italic |
| Leadership h2 | `Roveri` (surname preserved) | rust italic |
| Magazine card 1 (hero) h3 | `geometria` | rust italic |
| Magazine card 2 (small) h3 | `lotto` | rust italic |
| Magazine card 3 (small) h3 | `argomento` (motif resonance) | rust italic |
| Magazine card 4 (small) h3 | `minore` | rust italic |
| CTA-closer h2 | `argomento` (verbatim) | rust italic |

**12 italic em occurrences on home · all on distinct
headings/quotes.** CS-TYPE-02 PASS 12/12. The surname rename
preserves the `argomento`/`argomenta` curatorial motif (3 surfaces:
hero h1 + hero side-quote + magazine card 3) without overpowering.

**Voice anchor curatorial layer (post-fix)**: the founder is now
Marta Roveri. The voice anchor is structural ("ogni progetto è un
argomento costruito"), not gendered, so the rename is voice-anchor
neutral. The curatorial register (`argomento · progetto · servizio
· architettura · editoriale · committenze · novanta · fascicoli ·
2008 · MILANO · STUDIO DI ARCHITETTURA`) reads identically.

---

## §7 · What multilingual workflow C still has to do

The IT draft is now review-locked. Workflow C (multilingual
EN/FR/ES/AR + AR RTL) still has to deliver:

1. **EN translation** of the entire `CORNICE_CONTENT_IT` dict — 5
   pages (home, studio, servizi, progetti, contatti) + 4 case-detail
   posts. Voice anchor verbatim-in-translation: pick the EN phrasing
   that preserves the architectural-editorial register
   (`argomento` → `argument`? `case`? `proposition`? — copy team to
   choose). Re-bind on em-word audit at EN walk.
2. **FR translation** — same shape. Voice anchor: `argument`
   (cognate) is the natural FR.
3. **ES translation** — same shape. Voice anchor: `argumento`
   (cognate, identical orthography to IT).
4. **AR translation** — same shape, plus RTL handling. Voice
   anchor: pick the Arabic word that preserves the
   architectural-editorial register (the planner brief §11
   flagged Naskh-vs-Kufi as an open decision). The lf2/styles.html
   already includes a `{% if is_rtl %}` block that flips the 8/4
   hero split + the magazine-grid grid direction; that block stays.
5. **TEMPLATE_REGISTRY.json** — flip the Cornice row's `locales`
   from `[it]` to `[it, en, fr, es, ar]` and `rtl: true` (per the
   D-098 multilingual-cadence binding).
6. **Tier flip held until workflow D** — workflow C lands the
   translations at `tier=draft`. Workflow D flips to
   `published_live` after a second user handshake on the
   multilingual walk.

The A.6 review-lock does NOT reduce or change this list. None of
the A.6 fixes pre-empt translation work; F1 (rename Marco→Marta)
is a content edit that future translators will inherit naturally
because translations work off the IT source. F2 (cs-nav--lf2 in
_base.html) is a chrome rule that applies regardless of locale.
F3 (magazine-grid flex-grow) is layout-only, locale-neutral.

---

## §8 · Files changed at A.6

**Modified** (3 source files):

1. `apps/catalog/template_content_cornice.py` — F1 content edits
   (Marco→Marta + agreement of gendered Italian; ~16 surfaces;
   surname preserved; voice anchor untouched).
2. `templates/live_templates/business/corporate-suite/_base.html` —
   F2 lift (added `.cs-nav.cs-nav--lf2` body styles ~55 lines into
   the shared chrome block, immediately after `.cs-nav-cta--lf2`).
3. `templates/live_templates/business/corporate-suite/_layouts/lf2/styles.html` —
   F2 cleanup (removed the duplicated `.cs-nav.cs-nav--lf2` block
   now in _base.html; replaced with a 4-line breadcrumb comment).
   F3 fix (replaced `.card--hero .thumb` aspect-ratio with flex:1 +
   min-height; removed flex:1 from `.card--hero .copy`).

**Created** (8 scorecard panels + this build narrative + browser
verification):

- `factory/reports/cornice/cornice-a6-it-review-lock.md` (this file)
- `factory/reports/browser-verification/cornice-a6-it-review-lock.md`
- `factory/reports/browser-verification/cornice-a6-it-review-lock/captures/*.png`
- `factory/reports/scorecard/cornice-a6-it-review-lock/build-report.md`
- `factory/reports/scorecard/cornice-a6-it-review-lock/style-critic.md`
- `factory/reports/scorecard/cornice-a6-it-review-lock/contrast-accessibility.md`
- `factory/reports/scorecard/cornice-a6-it-review-lock/responsive-auditor.md`
- `factory/reports/scorecard/cornice-a6-it-review-lock/browser-verifier.md`
- `factory/reports/scorecard/cornice-a6-it-review-lock/release-gatekeeper.md`
- `factory/reports/scorecard/cornice-a6-it-review-lock/scorecard.md`
- `factory/reports/scorecard/cornice-a6-it-review-lock/summary.md`

**Untouched at A.6** (per scope rules):

- apps/editor — zero edits
- apps/projects — zero edits
- apps/commerce — zero edits
- All other archetype templates — zero edits
- LF-1, LF-3, LF-4, LF-5 layout files — zero edits
- TEMPLATE_REGISTRY.json — zero edits (tier=draft preserved)
- DNA registry (apps/catalog/template_dna.py) — zero edits
- Imagery pool (apps/catalog/preview_imagery.py) — zero edits
- Imagery policy (apps/catalog/imagery_policy.py) — zero edits

---

## §9 · Server / route status (handed back to orchestrator · post-fix)

```
server:                 python manage.py runserver 8052 --noreload
URL prefix:             http://127.0.0.1:8052/
template root URL:      /templates/business/cornice-architettura/preview/
9 IT routes (all 200 staff_preview · 404 anonymous):
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
catalog count:          23 published_live + 1 draft = 24 total
session reqs:           staff user authenticated (cornice_review · is_staff=True · is_superuser=True)
                        + ?preview=1 query string

frozen siblings (all 200 anonymous):
  - /templates/business/pragma-corporate-suite/preview/      LF-1
  - /templates/business/fiscus-commercialista/preview/       LF-3
  - /templates/business/solaria-coaching/preview/            LF-4
  - /templates/business/continua-stewardship/preview/        LF-5

test suite:             546 tests · 545 pass · 1 pre-existing failure
                        (test_medical_and_restaurant_templates_have_booking_flag
                         · Continua-related · UNRELATED to Cornice ·
                         documented in v15 baseline as pre-existing)
```

Server stays open at port 8052 for the user-handshake review.

---

## §10 · Lock verdict

The A.6 review-lock is **CLOSED**. The Cornice IT draft is locked
for human visual review. All three findings (F1 review-blocking,
F2 chrome-consistency, F3 editorial-rhythm) are fixed and re-
verified live. Frozen siblings show 0/4 regression. Cornice
distinctness vs all 4 live siblings still 5/5. Tier=draft
preserved. Test suite 545/546 (1 pre-existing failure unrelated
to Cornice).

If user signals **GO**: workflow C kicks off (EN/FR/ES/AR + AR RTL
+ Naskh-vs-Kufi decision per planner-brief §11).

If user signals **HOLD**: A.7 narrow re-author or A.6b re-build
per the documented re-spec authority.
