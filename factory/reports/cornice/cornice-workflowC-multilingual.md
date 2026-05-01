# Cornice · Workflow C · Multilingual rollout (EN/FR/ES/AR + AR RTL)

```yaml
report_type:        workflow-c-multilingual
template_slug:      cornice-architettura
archetype:          corporate-suite
sub_cluster:        architecture-firm · single-principal studio (editorial-led)
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · Cornice · workflow C (multilingual rollout · 5 locales)
date:               2026-05-01
agent:              workflow-c-multilingual-builder (Phase X.5)
inputs_consumed:
  - factory/reports/cornice/cornice-a5-it-build.md
  - factory/reports/cornice/cornice-a6-it-review-lock.md
  - factory/reports/browser-verification/cornice-a5-it-build.md
  - factory/reports/browser-verification/cornice-a6-it-review-lock.md
  - factory/reports/scorecard/cornice-a6-it-review-lock/*
  - factory/reports/corporate-suite/cornice-architettura/intake.md
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md
  - factory/reports/copy/cornice-architettura/copy-authoring.md
  - apps/catalog/template_content_cornice.py (locked LF-2 IT source)
  - templates/live_templates/business/corporate-suite/_layouts/lf2/* (frozen)
  - templates/live_templates/business/corporate-suite/_base.html (chrome)
  - frozen sibling state (Pragma · Fiscus · Solaria · Continua · all live anonymous)
status_tag:         WORKFLOW-C-COMPLETE · 5 locales authored · review-ready
verdict:            READY FOR USER VISUAL REVIEW · all 5 locales · tier=draft preserved
next_action:        User performs the visual handshake on the multilingual
                    Cornice walk. On GO, workflow D kicks off (public flip
                    + cascade per the standard sequence). On HOLD, narrow
                    re-author against the surface flagged.
```

This file is the binding workflow-C narrative for Cornice multilingual.
It pairs with:
- `factory/reports/browser-verification/cornice-workflowC-multilingual.md`
  — 5-locale walk evidence + frozen-sibling regression check + responsive
  matrix
- `factory/reports/scorecard/cornice-workflowC-multilingual/*.md`
  — 8 scorecard panels (build · style · contrast · responsive · browser ·
  gatekeeper · scorecard + summary)
- `factory/reports/browser-verification/cornice-workflowC-multilingual/captures/*.png`
  — 11 captures (5 home @1440 + 1 studio AR @1440 + 1 contatti FR @1440 +
  1 progetti ES @1440 + 1 case-detail EN @1440 + AR @880 + AR @480)

---

## §1 · Workflow framing (why this phase exists)

A.6 closed with the IT draft REVIEW-LOCKED. The orchestrator held
multilingual workflow C and the public flip workflow D pending a human
visual review of the IT draft. The user signalled GO on the multilingual
extension; workflow C is the pass that adds EN/FR/ES/AR on top of the
locked LF-2 Italian shape, preserves the voice anchor verbatim-in-
translation, and resolves the AR Naskh-vs-Kufi decision flagged at the
planner brief §11 as an open call deferred to workflow C pre-flight.

The work is intentionally narrow:
- 4 new locales authored (EN, FR, ES, AR), IT preserved
- LF-2 layout shape preserved exactly (no edits to lf2/styles.html
  beyond what A.6 already ratified · no edits to lf2/content.html)
- tier=draft preserved (no public flip)
- frozen siblings (Pragma · Fiscus · Solaria · Continua) untouched
- apps/editor / apps/projects / apps/commerce untouched
- no new archetype, no new layout family, no widening of LF-2

The scope rule: **add the 4 locales without weakening LF-2 or Cornice's
distinctness vs the four other corporate-suite siblings**. The voice
anchor `argomento` is the load-bearing italic across the LF-2 home; it
moves with the equivalent CURATORIAL noun in each locale, not with a
generic stand-in.

---

## §2 · Voice anchor verbatim-in-translation policy (CS-EXEC-01 / CS-BLOCK-11)

The IT voice anchor lives on exactly two surfaces of the home page:

- Hero h1: `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.`
- CTA-closer h2: same line verbatim

Workflow C preserves this two-surface verbatim recurrence in every
locale. The `<em>` italic moves with the curatorial noun's equivalent:

| Locale | Voice anchor (h1 + CTA closer) | Em-noun | Curator note |
|---|---|---|---|
| IT | `Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.` | argomento | source · curatorial-thesis sense |
| EN | `Every project is a built <em>argument</em>, not a service rendered.` | argument | direct cognate · Architectural Review register |
| FR | `Chaque projet est un <em>argument</em> construit, non un service rendu.` | argument | direct cognate · L'Architecture d'Aujourd'hui register |
| ES | `Cada proyecto es un <em>argumento</em> construido, no un servicio prestado.` | argumento | direct cognate · Arquitectura Viva register |
| AR | `كلّ مشروع <em>حُجَّة</em> مبنيّة، لا خدمة مُسداة.` | حُجَّة (ḥujja) | curatorial-thesis equivalent · MENA architectural-press · NOT موضوع/topic, NOT حالة/case-study |

The hero side-quote (em on the verb form derived from `argomento`) and
all four magazine-card h3 em-words (`geometria · lotto · argomento ·
minore`) move with the same curatorial sensibility per locale (see
`scorecard/style-critic.md §1` for the 12-em audit per locale).

---

## §3 · AR Naskh-vs-Kufi decision (planner-brief §11 · resolved)

The planner brief §11 left this open: the cluster default for Arabic
heading text is **Noto Kufi Arabic**, used by every existing AR-RTL
skin (Pragma, Fiscus, Solaria, Continua). LF-2's editorial register
favours humanist Naskh forms over Kufi geometry — Kufi reads
display-monumental (Pictet/family-office register), Naskh reads
editorial-publication (Casabella/Domus/Architectural Review register).

**Decision**: ship Cornice AR with **Noto Naskh Arabic** for headings,
**Amiri** for body (cluster default body font preserved). The Latin
wordmark `CORNICE` on the masthead and the founder's Latin name `Marta
Roveri` are preserved (CS-NAV-06 / CS-FOOT-03 binding). Latin numerals
are preserved on KPI tuples and dossier numbers (planner-brief §11).

**Implementation** (single chrome edit, scoped to LF-2):
- `templates/live_templates/business/corporate-suite/_base.html` line 12 —
  add `Noto+Naskh+Arabic:wght@400;500;600;700` to the existing AR
  Google-Fonts <link> alongside Amiri + Noto Kufi Arabic
- `_base.html` line ~767 — add a `html[dir="rtl"] body.cs-lf-lf-2 {
  --heading: 'Noto Naskh Arabic', '{{ theme.heading_font }}', Georgia,
  serif; }` override

The selector specificity guarantees: every other RTL skin (Continua
LF-5, Solaria LF-4, etc.) keeps its Kufi heading. Continua AR walk
post-fix shows `Noto Kufi Arabic` on the heading (verified live);
Cornice AR walk shows `Noto Naskh Arabic` on the heading (verified
live).

---

## §4 · Files changed at workflow C

**Created** (4 new locale modules):

1. `apps/catalog/template_content_cornice_en.py` — 1,083 lines · full
   English locale tree mirroring CORNICE_CONTENT_IT shape exactly
2. `apps/catalog/template_content_cornice_fr.py` — 1,107 lines · full
   French locale tree mirroring the IT shape
3. `apps/catalog/template_content_cornice_es.py` — 1,082 lines · full
   Spanish locale tree mirroring the IT shape
4. `apps/catalog/template_content_cornice_ar.py` — 1,088 lines · full
   Arabic locale tree mirroring the IT shape · formal MSA / الفصحى
   · Italian normative refs preserved (D.lgs., MIBAC, OAPPC, CNAPPC,
   PRG, Soprintendenza, DAStU, Reg. UE)

Each module imports the Pexels URL constants from
`template_content_cornice.py` (single source of truth · matches the
Solaria / Continua Pass B precedent).

**Modified** (3 files, all minimal):

1. `apps/catalog/template_content.py` — replaced the 5-line
   "EN/FR/ES/AR fall back to IT" stub with real imports + locale-tree
   wiring. Net change: 4 new imports, 4 dict entries flipped from
   `CORNICE_CONTENT_IT` to per-locale modules.
2. `templates/live_templates/business/corporate-suite/_base.html` —
   - line 12: added `&family=Noto+Naskh+Arabic:wght@400;500;600;700`
     to the `is_rtl`-gated Google Fonts <link>.
   - line ~768: added a 6-line scoped override
     `html[dir="rtl"] body.cs-lf-lf-2 { --heading: 'Noto Naskh
     Arabic', ... }` immediately after the cluster-default AR token
     block. Selector-scoped to LF-2 only.
3. `TEMPLATE_REGISTRY.json` — Cornice row:
   - `locales`: `[it]` → `[it, en, fr, es, ar]`
   - `rtl`: `false` → `true`
   - `tier_reason`: rewritten to record the multilingual rollout +
     Naskh decision (tier=draft preserved · public flip held).

**Untouched** (per scope rules):
- apps/editor — zero edits
- apps/projects — zero edits
- apps/commerce — zero edits
- All other archetype templates — zero edits
- LF-1, LF-3, LF-4, LF-5 layout files — zero edits
- LF-2 layout files (`lf2/styles.html`, `lf2/content.html`) — zero edits
- DNA registry (apps/catalog/template_dna.py) — zero edits
- Imagery pool (apps/catalog/preview_imagery.py) — zero edits
- Imagery policy (apps/catalog/imagery_policy.py) — zero edits

---

## §5 · Live walk methodology (Playwright MCP · mandatory)

Server: `python manage.py runserver 8052 --noreload` at
`http://127.0.0.1:8052/`.

Auth: staff user `cornice_review` / `cornice-review-password`
(`is_staff=True · is_superuser=True`). Tier=draft means anonymous
visitors get 404; staff with `?preview=1` reach all 9 routes; locale
toggling via `?lang=xx`.

Browser: Playwright MCP, Chromium engine.

Walk shape:

| Layer | What was checked |
|---|---|
| 5 locale homes @ 1440 | h1 voice anchor verbatim · em-noun preservation · side-quote em · leadership h2 · 4 magazine card titles · CTA closer recurrence · nav links · cream-paper masthead computed bg |
| AR home @ 1440 specifically | `dir=rtl` set · `--heading` resolves to `Noto Naskh Arabic` (LF-2 scope · NOT Kufi) · `--body` resolves to `Amiri` · cream-paper masthead `cs-nav--lf2` class · Latin wordmark + Latin Marta Roveri preserved · 12 italic em-surfaces |
| AR studio (about) @ 1440 | history list · values list · team cards · coordinates strip · 4-col footer with whistleblowing column · all RTL · Latin Italian normative refs preserved · D.lgs. 24/2023 in footer column |
| FR contatti @ 1440 | form labels · form sections · select options · consent text · footer · whistleblowing column |
| ES progetti @ 1440 | list-page intro · cases lead · trailing CTA |
| EN case-detail @ 1440 | breadcrumb · meta strip (Programme / Dossier year / Site status / Lead architect) · KPI tuple · 3 sections · lead-partner · team strip · next-dossier link |
| AR home @ 880 | hamburger entry · stacked magazine grid · RTL flow preserved |
| AR home @ 480 | mobile single-column · KPI strip wraps · cream chrome stays cream · em-bold preserves emphasis |
| Frozen siblings × 5 locales × anon | 4 siblings × 5 locales = 20 routes · anonymous HTTP — all 200 |
| Continua AR specifically | h1 font family computed `Noto Kufi Arabic` (LF-5 unaffected by Naskh override) · h1 still verbatim `استمراريّة العائلة تُقاس بالأجيال.` |
| Pragma IT specifically | navy nav `rgb(30,41,59)` unchanged · h1 verbatim `Dove si prendono le decisioni che contano.` |

Captures saved under
`factory/reports/browser-verification/cornice-workflowC-multilingual/captures/`
(11 PNGs).

---

## §6 · Findings during the walk

Zero findings. The IT review-lock did the heavy lifting — the LF-2
shape, chrome, and content were already validated at A.6, so workflow
C had to deliver translation-only work without disturbing layout. No
review-blocking, chrome-consistency or editorial-rhythm issues
surfaced during the 5-locale walk.

Specific surfaces inspected for translation regressions:
- Voice anchor verbatim recurrence: 5/5 locales correct (h1 + CTA
  closer carry the SAME phrase byte-equivalent).
- Em-word audit on home: 12 italic em surfaces per locale; all in
  place, all on distinct headings/quotes/counters (CS-TYPE-02 PASS
  12/12 × 5 locales = 60/60).
- LF-2 chrome class `cs-nav--lf2` active on every locale's home AND
  inner pages (A.6 F2 lift verified once, holds across locales).
- Cream-paper nav background `rgb(238,240,243)` computed live on
  every locale's home AND inner pages.
- Founder name `Marta Roveri` preserved in Latin script in every
  locale's leadership h2, every team card, every case-detail
  lead_partner.
- Italian normative refs (D.lgs. 24/2023 · D.lgs. 42/2004 · D.M.
  154/2017 · OAPPC · CNAPPC · MIBAC · Soprintendenza · PRG · DAStU
  · Reg. UE 679/2016) preserved verbatim in every locale's footer
  whistleblowing column AND inline body where they occur.
- Italian addresses preserved (Via Pasquale Paoli 9 · 20143
  Milano/Milán/Milan · phone +39 02 6610 4708 · email
  fascicolo@cornice-architettura.it).
- AR Naskh swap active ONLY on body.cs-lf-lf-2 — Continua AR (LF-5)
  computed font still `Noto Kufi Arabic` (no font regression on the
  cluster default).
- AR `<em>` rendered as bold (chrome CS-TYPE-05 reset:
  `html[dir="rtl"] em { font-style: normal; font-weight: 700 }`) —
  Arabic italics are typographically hostile, bold conveys the same
  emphasis. The voice anchor's em-noun `حُجَّة` reads as bold-Naskh
  in the live render, which is the editorially correct choice.

---

## §7 · Frozen sibling regression verdict

| Sibling | Layout family | Anonymous /it | Anonymous /en | /fr | /es | /ar | Verdict |
|---|---|---|---|---|---|---|---|
| Pragma | LF-1 | 200 | 200 | 200 | 200 | 200 | NO REGRESSION (navy nav preserved · h1 verbatim) |
| Fiscus | LF-3 | 200 | 200 | 200 | 200 | 200 | NO REGRESSION |
| Solaria | LF-4 | 200 | 200 | 200 | 200 | 200 | NO REGRESSION |
| Continua | LF-5 | 200 | 200 | 200 | 200 | 200 | NO REGRESSION (LF-5 chrome preserved · Kufi heading preserved) |

**Verdict: 4/4 frozen siblings unchanged.** The Naskh override is
selector-scoped to `body.cs-lf-lf-2` (Cornice only). The Google-Fonts
<link> addition imports a new weight/family but only when `is_rtl` is
true; LTR locales of every skin are byte-equivalent before/after.
Pragma/Fiscus/Solaria/Continua AR pages still render Noto Kufi
Arabic.

---

## §8 · Cornice distinctness verdict (post-multilingual · 5-axis triangulation × 5 locales)

Distinctness is preserved across all 5 locales — translation does not
collapse any of the 5 distinctness axes:

| Axis | vs Pragma | vs Fiscus | vs Solaria | vs Continua | All-locale verdict |
|---|---|---|---|---|---|
| Voice (curatorial-architectural) | distinct (decisional gravity) | distinct (presidio scadenze) | distinct (bounded coaching method) | distinct (stewardship temporal `generazioni`/`generations`/`générations`/`generaciones`/`الأجيال`) | PASS · all 5 locales |
| Palette (graphite + pietra-serena + rust) | distinct (navy/blue/emerald) | distinct (warm-neutral/gold/blu-notte) | distinct (warm-carbon/ocra/caramel) | distinct (pine/pewter/brass) | PASS · palette is locale-neutral |
| Hero geometry (stacked-editorial 8/4 + KPI in photo overlay) | distinct (55/45 split) | distinct (55/45 split) | distinct (55/45 split) | distinct (object-overlay) | PASS · layout is locale-neutral |
| Hero subject (Bologna golden-hour portico · zero people · exterior architectural) | distinct | distinct | distinct | distinct | PASS · imagery is locale-neutral |
| Cases shape (3+1 magazine-grid · dominant hero photo) | distinct (numbered list-row) | distinct (numbered list-row) | distinct (numbered list-row) | distinct (vertical timeline) | PASS · shape is locale-neutral |

**5/5 axes × 5 locales** = 25/25. The translation work strengthens
the editorial-curatorial axis specifically — `حُجَّة` carries the
Arabic architectural-press register exactly the way `argomento`
carries the Italian one, so Cornice's voice reads architecturally
distinct from Continua's family-office stewardship register in every
locale, not only Italian.

---

## §9 · Test suite + system check

```
python manage.py check                    System check identified 1 issue
                                          (corporate_suite.W001 grandfathered
                                          warning · pre-existing · unrelated)

python manage.py test apps.catalog        Ran 171 tests in 2.408s
                                          FAILED (failures=1)
                                          [pre-existing booking-flag failure
                                           on Continua test · unrelated to
                                           Cornice · documented in v15
                                           baseline]

python manage.py test                     Ran 546 tests in 169.747s
                                          FAILED (failures=1)
                                          [same pre-existing failure]
```

545/546 — same outcome as the A.6 review-lock. No new test breakage
introduced by workflow C.

---

## §10 · Server / route status (handed back to orchestrator)

```
server:                 python manage.py runserver 8052 --noreload
URL prefix:             http://127.0.0.1:8052/
template root URL:      /templates/business/cornice-architettura/preview/
9 routes × 5 locales = 45 staff-preview routes (all 200 with ?preview=1):
  IT  /preview/ (and /studio/ /servizi/ /progetti/ /contatti/ + 4 case-detail slugs)
  EN  ?lang=en  on every route above
  FR  ?lang=fr  on every route above
  ES  ?lang=es  on every route above
  AR  ?lang=ar  on every route above (dir=rtl)
tier:                   draft (anonymous: 404 · staff_preview: 200 with ?preview=1)
catalog count:          23 published_live + 1 draft = 24 total

frozen siblings (all 200 anonymous · IT + EN/FR/ES/AR · 20 routes total):
  - /templates/business/pragma-corporate-suite/preview/         LF-1
  - /templates/business/fiscus-commercialista/preview/          LF-3
  - /templates/business/solaria-coaching/preview/               LF-4
  - /templates/business/continua-stewardship/preview/           LF-5

test suite:             546 tests · 545 pass · 1 pre-existing failure
                        (test_medical_and_restaurant_templates_have_booking_flag
                         · Continua-related · UNRELATED to Cornice ·
                         documented in v15 baseline as pre-existing)
```

Server stays open at port 8052 for the user-handshake review.

---

## §11 · Workflow C verdict

Workflow C is **CLOSED**. Cornice ships in 5 locales (it/en/fr/es/ar)
on top of the locked LF-2 IT shape. Voice anchor preserved verbatim-
in-translation across all 5 locales (`argomento → argument / argument
/ argumento / حُجَّة`). LF-2 layout shape preserved exactly. Real
Arabic RTL with the LF-2-specific Naskh heading swap (planner-brief
§11 decision realised). Frozen siblings show 0/4 regression. Cornice
distinctness across all 5 locales 5/5 vs every other corporate-suite
sibling. Tier=draft preserved (no public flip). Test suite 545/546
(same pre-existing failure).

If user signals **GO**: workflow D kicks off (public flip via
`sync_template_tiers` + the standard test-bumps cascade).

If user signals **HOLD on a specific locale**: narrow re-author of
that locale module; LF-2 chrome and IT remain untouched.
