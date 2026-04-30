# Cornice · Build brief · REAL CANDIDATE (implementation-ready)

**Status**: build-ready · planner-brief equivalent · ready to hand to a real workflow A.2 → A.5 session
**Cluster**: corporate-suite · 5th sibling · 1st institutional-architecture variant · LF-2 (Editorial Spread)
**Filed by**: orchestrator · `phase-x5-lf2-fifth-sibling-pilot` branch
**Date**: 2026-04-30
**Companion files**: `cornice-distinctness-proof.md` (matrix proof) · `factory/reports/hardening/lf2-fifth-sibling-pilot.md` (Phase X.5 master · risks · build order · browser gates)
**Promotion path on first build**: this file → `factory/reports/corporate-suite/cornice-architettura/planner-brief.md`

This brief is concrete enough to start the build immediately. Every field is decision-locked. Where the brief leaves a tactical choice (Cormorant Garamond fallback, travertine vs cream contrast handling, slot_2 portrait fallback search lane), the choice is named and bounded — not deferred.

---

## 1 · Required inputs (intake summary)

| Field | Value |
|---|---|
| `template_slug` | `cornice-architettura` |
| `studio_name` | Cornice |
| `cluster` | `corporate-suite` |
| `sub_cluster_label` | institutional-architecture-practice (architettura per committenze istituzionali) |
| `layout_family` | **LF-2** (Editorial Spread · cluster's first activation) |
| `audience_profile` | Institutional clients commissioning completed built work — public-tendered civic-cultural commissions (museums, libraries, courthouses), corporate headquarters (insurance / finance / industrial), masterplans for public-private partnerships, heritage-protected refurbishments. NOT residential, NOT interior-design boutique, NOT speculative concept studios. |
| `org_scale` | 1 founding architect (28+ year practice) + 5–7 associate architects + design + admin staff. Single-portrait leadership (LF-2 L6). |
| `locales` | `[it]` · others enter via Phase X.5b (workflow C) |
| `nearest_two_siblings` | Pragma (institutional-voice neighbour · risk: stakeholder one-liner adjacency) · Continua (whistleblowing-footer neighbour · risk: footer column-count overlap) |
| `user_constraints` | see §11 (6 must-haves · 6 must-avoids) |
| `target_tier` | `draft` · D-102 cadence |
| `pexels_pack_status` | `not started` (curator briefed by §4 below at A.3 entry) |

---

## 2 · Forbidden similarities + collision check (planner contract)

The full anti-clone block is the master pilot file `factory/reports/hardening/lf2-fifth-sibling-pilot.md §4` (84 explicit anti-collision lines: 18 vs Pragma · 14 vs Fiscus · 14 vs Solaria · 22 vs Continua · 16 cluster red lines + AI-slop avoidance). The collision check matrix is filled in `cornice-distinctness-proof.md §1`. Headline result: **5/5 vs Pragma · 5/5 vs Fiscus · 5/5 vs Solaria · 5/5 vs Continua** on the 4-of-5 skin gate; **8/9 vs Pragma · 9/9 vs Fiscus · 9/9 vs Solaria · 8/9 vs Continua** on the 9-of-9 layout gate. Plan sign-off authorised on `DISTINCTNESS_RULES.md §1` (4/5 gate) AND on `corporate-suite-layout-variance-rules.md §2` CS-LAYOUT-12 (4/9 gate) AND on CS-LAYOUT-13 (full 3-axis L1+L2+L7 divergence vs every live sibling).

Hard prohibitions (`next-template-brief-schema.md §2.1` · no waiver, ever) all satisfied:
- ✓ No URL appearing in `business-corporate` / `business-fiscal` / `business-coaching` / `business-stewardship` (cross-cluster grep mandatory at A.3)
- ✓ Inter is NOT body sans (Cornice ships Work Sans · third-Inter ban respected)
- ✓ `--primary-2: #2c3e6b` is NOT introduced into the skin
- ✓ Hero meta-strip is NOT KPI tuple / fiscal-calendar / percorso-cadenza / stewardship-horizon-strip / governance-cycle (Cornice has NO mid-strip — LF-2 L3=absent — and KPI lives **inside** the hero credit overlay as 3 inline stats)
- ✓ `--primary` `#23262A` L\* ≈ 14 — well under 40 cream-safe ceiling (CS-PAL-01)
- ✓ No lorem ipsum / placeholder copy
- ✓ Pexels-only · no Unsplash carve-out
- ✓ No geometric sans on heading
- ✓ No render-as-photo imagery (architecture-firm AI-slop tell · §4 curator rejection rule)

---

## 3 · Design DNA · `template_dna.py` shape

```python
TemplateDNA(
    archetype="corporate-suite",
    sub_cluster="institutional-architecture-practice",
    layout_family="lf2",                          # CS-LAYOUT-22 REQUIRED · cluster's 1st LF-2

    hero_style="stacked-editorial-monograph",     # LF-2 L1 · full-bleed photo TOP · 8/4 col h1+intro BELOW
    navbar_style="split-wordmark-masthead",       # LF-2 L8 · sticky-top with 2-line wordmark
    footer_style="four-col-with-whistleblowing",  # LF-2 L9 · 4-col incl. whistleblowing column

    section_order=[                               # LF-2 L2 sequence "B" · NO mid-strip · NO trust marquee · NO KPI band
        "hero",                       # stacked-editorial · 3 KPI stats inline in credit overlay
        "narrative",                  # essay-with-anchors · 4-paragraph editorial + side-rail anchor links
        "sectors",                    # "Committenze realizzate" — institutional-commission types
        "leadership",                 # single-portrait-feature · founding architect masthead
        "cases",                      # magazine-grid · 1 hero card + 3 small cards
        "cta-closer-dark",            # the ONE dark band on home (CS-TONE-03 fallback per CS-LAYOUT-05)
    ],

    card_style="monograph-card",                  # cream paper · travertine hairline rule · burgundy underline on focus
    button_style="ghost-monograph",               # outline-only on cream · filled burgundy only in dark closer band
    density="airy",                               # cluster invariant · CS-RHYTHM-01
    tone="editorial-curatorial-architectural",
    imagery_direction="institutional-architecture-monograph",
    imagery_key="business-architecture",
    conversion_pattern="commission-brief",

    font_pairing=("Cormorant Garamond", "Work Sans"),

    palette={
        "primary":   "#23262A",   # graphite ink · L* ≈ 14 (cream-safe)
        "secondary": "#D9CFB8",   # travertine · warm-neutral stone · used only on hairlines/dividers/8-col body backing
        "accent":    "#6E2A2D",   # archive burgundy · the load-bearing differentiator
        "paper":     "#F4ECDB",   # cream paper · cluster invariant
        "ink":       "#1F2426",   # body text on cream · NOT primary
    },

    voice_anchor="Ogni opera istituzionale risponde al suo <em>luogo</em>.",
    voice_anchor_em_word="luogo",
    voice_anchor_contrast_pair=False,
)
```

### Why every line is non-negotiable

| Field | Decision | Anti-collision rationale |
|---|---|---|
| `layout_family="lf2"` | Editorial Spread | LF-2 was the only OPEN family-with-declared-tuple at intake; LF-6 stays reserved; LF-{NEW} is heavier than re-using a declared open slot |
| `primary #23262A` | graphite ink | NOT navy (Pragma `#1E293B`) · NOT gray-blue (Fiscus `#1F2937`) · NOT warm-carbon (Solaria `#2B2A28`) · NOT pine (Continua `#0F3A30`) — graphite is the first cool-non-blue-non-green-non-carbon primary; reads "ink on monograph cover" |
| `secondary #D9CFB8` | travertine | NOT cool-blue (Pragma) · NOT warm-gold (Fiscus) · NOT warm-ocra (Solaria) · NOT cool-pewter (Continua) — travertine reads "limestone façade / Roman civic," a non-blue, non-gold, non-pewter neutral. Used **only on hairlines/dividers/body container backing**, never as a section background that would compete with cream paper (see §12 risk 6) |
| `accent #6E2A2D` | archive burgundy | NOT emerald (Pragma) · NOT deep-navy (Fiscus) · NOT caramel (Solaria) · NOT brass (Continua) — archive-burgundy reads "Veneto leather binding / Renaissance archive cover" — a saturated warm distinct from Solaria's caramel (more orange) and Fiscus's gold (more yellow). Polarity strategy = cool/warm/warm — the only OPEN combination after Continua's cool/cool/warm |
| `font_pairing` | Cormorant Garamond + Work Sans | Cormorant Garamond on matrix §1.4 OPEN list · highest editorial-monograph register of the open serifs · strong italic personality at h1 56px. Work Sans on matrix §1.4 open body sans list — humanist, not Inter, not Plex Sans, not Public Sans (Continua's). Closes the §1.4 cluster-collapse risk a third time |
| `voice_anchor` | one sentence + one em on `luogo` (spatial noun) | Pragma's italic = decisional/agency word; Fiscus's = imperative; Solaria's = contrast-pair nouns (exception); Continua's = temporal noun (`generazioni`). Cornice's italic on a SPATIAL noun `luogo` carries the firm's defining axis (place / site / context), not its method or its product |
| `section_order` | LF-2 sequence B · 6 sections | NOT Pragma's 8 (no mid-strip + no extra) · NOT Fiscus's 9 (no fiscal-calendar) · NOT Solaria's 7 (no manifesto + no method-cadenza) · NOT Continua's 8 (no governance-cycle) · NO mid-strip, NO trust marquee, NO pillars-as-numbered-grid, NO KPI band — the editorial spread's narrative essay-with-anchors does the work that pillars+KPI+trust do in LF-1/3 |

### Heading-serif fallback (decision-locked at A.5 entry)

Cormorant Garamond is the primary choice. If at A.5 the build session encounters a licence/availability friction (Google Fonts API failure · weight-set incomplete · italic glyph coverage thin), the substitution is **Cormorant Infant** (same family, different optical size · italics preserved). Do NOT substitute Cormorant Garamond with Crimson Pro (Continua), Spectral (Continua's fallback), Lora, PT Serif, or Cormorant Upright. Both Crimson Pro and Spectral are now claimed by Continua's lifecycle; using either silently echoes Continua. Lora and PT Serif have lower italic personality and would soften the spatial-noun italic emphasis.

### Body-sans fallback

Work Sans is the primary choice. If at A.5 build encounters friction, the binding substitute is **Source Sans Pro** (matrix §1.4 OPEN). Do NOT fall back to Inter (taken by Pragma + Solaria · third use BLOCKING), IBM Plex Sans (Fiscus), or Public Sans (Continua).

---

## 4 · Imagery DNA · `business-architecture` pack

The pack file lives at `docs/content-factory/imagery/packs/business-architecture.md` after A.3. The 6 slots below are subject specifications; real Pexels URLs land at A.3 with the cross-cluster grep on file (`business-corporate` / `business-fiscal` / `business-coaching` / `business-stewardship`).

```yaml
imagery_pack:
  imagery_key: business-architecture
  pool_source: Pexels                # CS-IMG-SRC-01 · no Unsplash carve-out
  pool_size: 6                       # CS-IMG-POOL-01

  slot_0_hero_editorial:
    subject:        completed institutional building exterior at dusk · plaza-
                    level approach · limestone or concrete-and-glass civic
                    architecture · interior glow visible through ground-floor
                    glazing · evening sky transition (deep-blue to warm-low-
                    horizon-light) · NO people in foreground · pedestrian-scale
                    figures at distance ARE acceptable (≤ 5% of frame) · no
                    visible signage / branding / vehicles
    mood:           monograph-grade · civic-monumental · evening-blue-warmth ·
                    architectural-publication aesthetic · the building IS the
                    proposition rendered as a single defining image
    composition:    landscape · centred or asymmetric-balanced · subject fills
                    middle-and-upper-half · sky takes upper third · plaza/
                    foreground takes lower fifth · the hero overlay
                    (project-credit + 3 inline stats) sits in the lower third
                    over a darker zone of the photo
    color_temp:     evening-cool with warm-interior-glow · neutral overall ·
                    the photo sits between Pragma's daylight-cool and Solaria's
                    warm-meeting-room without overlapping either
    coherence:      stacked-editorial hero · the building IS the studio's
                    proposition rendered as a publishable monograph spread ·
                    not a desk · not a boardroom · not a library · not a 1:1
    pexels_search:  "modern institutional architecture exterior dusk plaza
                    limestone glass civic"
    feasibility:    GO (18-25 plausible candidates · §3.4 GO)
    rejection_rules_for_curator:
                    REJECT: any human in foreground (≤ 5% of frame at distance OK)
                    REJECT: any vehicle visible in plaza
                    REJECT: render-imagery (apply 3-gate: weathered material ·
                            plausible reflections · age-consistent finish)
                    REJECT: residential / single-family-house framing
                    REJECT: tight crop on a single architectural element
                            (column, doorway) — must read as "whole building"
                    REJECT: any URL in business-corporate (Pragma legacy
                            Unsplash + later Pexels)
                    REJECT: any URL in business-stewardship (Continua's
                            recently-claimed pool)

  slot_1_narrative_atrium:
    subject:        institutional atrium interior · monumental staircase
                    ascending toward a roof skylight · travertine or limestone
                    columns flanking · soft natural light from above · ZERO
                    people · NO chairs / tables / desks / screens · single
                    architectural-element framing · reads as "civic monument"
                    not "office lobby"
    mood:           monumental · contemplative · architectural-publication
    use:            cs-narrative band on home (background photo for the essay
                    side-rail OR a half-bleed inset between narrative
                    paragraphs)
    coherence:      shows the studio's interior register — civic-monumental
                    not corporate-occupied · shows that institutional
                    architecture is read AT human scale once the staircase is
                    walked, not from an office desk
    pexels_search:  "atrium staircase travertine columns interior architecture
                    monumental skylight"
    feasibility:    GO (12-18 candidates)
    rejection_rules_for_curator:
                    REJECT: any people walking (Pragma atrium-feature collision · §6 risk 1)
                    REJECT: chairs / tables / reception desks / digital signage
                    REJECT: any URL in business-corporate (Pragma's atrium pool)
                    REJECT: glass curtain-wall as primary subject (too SaaS-HQ)

  slot_2_portrait_founding_architect:
    subject:        founding architect · 60s+ · environmental portrait · seated
                    or standing at drafting table with physical model and
                    plan-drawings visible · OR on-site at a completed cantiere
                    with hard-hat in foreground (architect mid-distance, the
                    site visible behind) · single subject · visible signs of
                    long-term practice (gray hair, weathered hands, presence)
                    · NOT studio-headshot · NOT desk-with-laptop · NOT meeting-
                    room
    mood:           veteran · attentive · monograph-protagonist · the architect
                    in the act of architecture (not in the act of meeting)
    diversity_note: 60s+ explicitly · gender + ethnicity selected to NOT
                    overlap Solaria's slot_2 (Solaria's senior-ish female-or-
                    male slot) · curator confirms differentiation at A.3.
                    Recommended target: 60s+ male with weathered hands at a
                    drafting table with model + plans, OR 60s+ at site with
                    hard-hat — either is acceptable; the cluster's existing
                    photo-present leads (Solaria's coach + Continua's stewards)
                    do not occupy this exact composition
    pexels_search:  "senior architect atelier studio drafting environmental
                    portrait model plans"
    feasibility:    CAUTION (8-14 candidates) · §3.4 CAUTION · curator
                    authorised to escalate to fallback A search lanes if the
                    lead lane returns < 5 viable post-grep candidates
    fallback_search_lanes_pre_authorized:
                    A: "senior architect drafting table glasses environmental"
                    B: "principal architect site visit hard hat construction"
                    C: "architect office model wood desk environmental"
    rejection_rules_for_curator:
                    REJECT: studio-headshot (white backdrop, professional-
                            portrait lighting) — must be environmental
                    REJECT: visible laptop / monitor / computer
                    REJECT: subject ≤ 50s (must read as 28+ year practice)
                    REJECT: visible overlap with Solaria slot_2 portrait (run
                            cross-cluster image comparison via thumbnail check)
                    REJECT: subject in suit-and-tie corporate dress (must read
                            as creative-professional · open shirt / atelier-
                            apron / hard-hat are all acceptable)

  slot_3_case_hero:
    subject:        completed civic-cultural building exterior · daylight ·
                    full or three-quarter view · institutional-grade scale
                    (museum, library, courthouse, university building, civic
                    center, cultural foundation) · this becomes the magazine-
                    grid hero card on home cs-cases-preview
    mood:           public-record · architectural-monograph · daylight ·
                    institutional-confidence
    use:            cs-cases-preview hero card (the "1" of the 1+3 magazine
                    grid)
    pexels_search:  "civic library museum exterior modern architecture daylight
                    institutional"
    feasibility:    GO (14-22 candidates)
    rejection_rules_for_curator:
                    REJECT: render-imagery (apply 3-gate)
                    REJECT: small-residential framing
                    REJECT: visible URL/branding/signage at billboard scale
                    REJECT: same building as slot_0 hero (must be a different
                            project — the studio has "12 opere realizzate, 3 città")

  slot_4_case_smalls:                # 3 small cards in the magazine-grid
    subject:        three different completed institutional projects · each
                    distinct in program (one corporate-HQ-tier · one civic-
                    cultural · one masterplan-PPP-or-campus) · each shot in
                    daylight · each readable at 320px width
    mood:           public-record · varied-program · monograph-grade
    use:            cs-cases-preview small cards (the "3" of 1+3)
    pexels_search:  3 lanes ·
                    A: "corporate headquarters facade modern architecture daylight"
                    B: "campus building university courtyard architecture"
                    C: "civic plaza building modern architecture daylight"
    feasibility:    GO (18-30 candidates across 3 lanes · pick 1 from each)
    rejection_rules_for_curator:
                    REJECT: render-imagery (apply 3-gate per candidate)
                    REJECT: residential framing
                    REJECT: any duplicate or near-duplicate across the 3 small
                            cards (the magazine-grid's value is variety)
                    REJECT: any building that visually resembles slot_0 or
                            slot_3 (the 4 case images must read as 4 distinct
                            projects)

  slot_5_ambient_urban:
    subject:        Italian city skyline at golden hour · civic plaza · cathedral
                    or rooftop horizon line · dignified urban context · NOT
                    famous tourist landmarks (Coliseum, Duomo Milano, etc — too
                    iconic) · NOT atrium duplicate (slot_1 covers interior) ·
                    NOT a single-building exterior (slots 0/3/4 cover that)
    mood:           civic-context · golden-hour · longitudinal · the city as
                    the studio's enduring client
    use:            about/services ambient · contact page hero
    why_not_atrium: slot_1 owns atrium; about-page ambient must vary the macro
                    mood from the home narrative band
    pexels_search:  "italian city skyline civic plaza golden hour rooftop"
    feasibility:    GO (10-16 candidates)

  imagery_distinctness:
    vs_pragma:
      - hero is full-bleed institutional building at dusk · Pragma's is
        4-person boardroom-meeting daylight
      - feature/narrative band is monumental atrium · Pragma's feature is
        corporate atrium with people-walking
      - portraits are SINGLE founding-architect environmental · Pragma is
        typographic-only (no portraits)
      - mood is evening-blue-warmth · Pragma is daylight-cool
      - subject density is 0 (hero) → 1 (single portrait) → 0 (cases) ·
        Pragma is 1-4 throughout
      - pool source = business-architecture · Pragma was business-corporate

    vs_fiscus:
      - hero is institutional-building exterior · Fiscus is desk-with-documents
      - hero color temp is evening-blue-warmth · Fiscus is interior-warm-task
      - ambient is urban-skyline · Fiscus's ambient is bookshelf (banned)
      - portraits are single 60s+ · Fiscus is typographic-only
      - subject is BUILDING throughout · Fiscus is DESK throughout
      - cases are magazine-grid with project images · Fiscus is list-row
        (text-only at home)

    vs_solaria:
      - hero is no-people building · Solaria is 1:1 conversation
      - hero is evening-blue · Solaria is bright-cool meeting room
      - portraits are 60s+ environmental · Solaria is 30s × 2 studio-light
      - ambient is urban-skyline · Solaria's ambient is warm-home-office-with-plants
      - hero subject density is 0-people · Solaria's is 2-people
      - cases are 4 buildings · Solaria's are 4 anonymized 1:1 mandates

    vs_continua:
      - hero is institutional-building EXTERIOR · Continua is library-reading-
        room INTERIOR
      - hero subject is building-as-civic-monument · Continua is room-as-
        archive
      - portraits are SINGLE 60s+ environmental masthead · Continua is 3-card
        pillar-photo (60s + 40s + 50s)
      - ambient is urban-skyline · Continua's is slate-stairwell
      - cases are 4 buildings (magazine-grid) · Continua's are 4 family
        mandates (timeline)
      - palette in photos is graphite-evening + travertine-stone + burgundy-
        archive · Continua is pine-shadow + brass-warm + cream-mahogany
      - subject vocabulary is opera/luogo/cantiere/archivio · Continua's is
        custodia/famiglia/generazioni/CdF

  cross_cluster_grep_clean:    YES (intent · curator confirms at A.3 BEFORE committing URLs)
```

---

## 5 · Typography DNA

| Surface | Specification |
|---|---|
| **h1 hero** | Cormorant Garamond 60px / line-height 1.05 / weight 500 / italic on `luogo` only |
| **h2 section** | Cormorant Garamond 38px / line-height 1.14 / weight 500 / italic only on em-word |
| **h3 card / case caption** | Cormorant Garamond 24px / line-height 1.22 / weight 500 |
| **eyebrow / label** | Work Sans 12px / uppercase / letter-spacing 0.22em / weight 600 (RTL resets letter-spacing to 0 — CS-TYPE-05) |
| **body** | Work Sans 17px / line-height 1.6 / weight 400 / tracking 0 |
| **CTA label** | Work Sans 15px / weight 600 / letter-spacing 0.04em |
| **`.num` KPI (hero overlay inline stats)** | Work Sans 28px / weight 600 / `font-variant-numeric: tabular-nums` (CS-TYPE-03) — smaller than LF-1's 48px because LF-2 KPI is overlay-inline, not band-large |
| **AR heading** (Phase X.5b) | swap to Noto Kufi Arabic via `html[dir="rtl"]` (CS-TYPE-06) — Cormorant Garamond Latin wordmark preserved (CS-NAV-06 / CS-FOOT-03) |
| **AR body** (Phase X.5b) | swap to Amiri |

**Why Cormorant Garamond vs the alternatives**: Cormorant Garamond's high-contrast editorial ratios + strong italic carry the monograph register that LF-2 demands. Pragma's Merriweather reads "newspaper-editorial" (less monumental); Fiscus's Plex Serif reads "document-pair" (less elegant); Solaria's Fraunces reads "warm-humanist book-jacket" (too contemporary); Continua's Crimson Pro reads "long-form considered" (right register but already taken). Cormorant Garamond reads "monograph / Phaidon / 2G publication / Lars Müller spread" — the editorial-architectural register that the family demands. Italic personality is exceptionally strong; the spatial-noun italic emphasis (`luogo`) lands at h1 60px without colour or weight assistance.

**Why Work Sans body**: matrix §1.4 lists Work Sans on the open body-sans list; it's humanist-neutral with slightly tighter counters than Inter and noticeably wider apertures than Plex Sans. Reads "publication body / monograph caption" without falling into either Inter's geometric register or Public Sans's gov-trust register (Continua's). Pairs cleanly with Cormorant Garamond and explicitly closes the §1.4 cluster-collapse risk a third time (Pragma=Inter, Solaria=Inter, would-be third Inter sibling = collapse).

---

## 6 · Section sequence · home page (LF-2 sequence B · 6 sections)

A practical beat sheet, not a wireframe novel. Word counts target the upper-band range from §3.4 below (~1600 total).

| # | Section | Beat purpose | Concrete content (IT) | Word target |
|---|---|---|---|---|
| 1 | `cs-hero` stacked-editorial | Position + voice anchor + first proof tuple, all in one publishable spread | Full-bleed hero photo TOP (slot_0 institutional-building dusk). Below the photo, an 8-col + 4-col layout: LEFT 8 cols = h1 voice anchor (italic on `luogo`) + 1-line side-quoted intro "Studio di architettura per committenze istituzionali. 28 anni di pratica, 12 opere realizzate, 3 città." + primary CTA "Avvia una committenza" (outline-on-cream). RIGHT 4 cols = side-quoted manifesto pull "Misuriamo il lavoro in opere consegnate, non in progetti annunciati." Hero credit overlay on the photo's lower-third: `(Sede istituzionale committenza pubblica · Verona 2023)` + 3 inline stats `12 opere realizzate · 3 città · 28 anni di pratica` (LF-2 L5 hero-overlay KPI placement) | 110 |
| 2 | `cs-narrative` essay-with-anchors (replaces pillars) | What the studio thinks · its 4 architectural commitments · in editorial prose, not in cards | 4-paragraph editorial essay (8-col body + 4-col side-rail with anchor links). Each paragraph anchors to a topic the side-rail mirrors: <br>· **Permanenza** (~120w) — committed to civic durability over fashion <br>· **Luogo** (~120w) — every site is read before it is built; voice anchor restated as italics on `luogo` <br>· **Committenza** (~120w) — the public/institutional client as architectural partner <br>· **Archivio** (~120w) — every commission enters a public archive when delivered <br>Side-rail: 4 anchor links (one per topic) + 1 quotation pull ("L'architettura istituzionale dura quanto le città che la accolgono.") | 480 + 80 anchor copy = **560** |
| 3 | `cs-sectors` ribbon | Anonymized commission-program proof — public-record style, NOT marketing breadth | label "Committenze realizzate" (NOT "Settori" generic — names the audience as institutional clients). 6 segments: civico-culturali · sedi corporate · masterplan pubblico-privati · campus universitari · restauri istituzionali · attrezzature pubbliche. Each segment = one-line caption (~14w). | 110 |
| 4 | `cs-leadership` single-portrait-feature | The founding architect as monograph protagonist · LF-2 L6 | LEFT 5-col: large environmental portrait (slot_2 founding-architect) at masthead scale, 3:4 aspect. RIGHT 7-col: h2 "[Architect name] · Architetto fondatore" + 2-paragraph bio (~180w · career arc · key institutional commissions · public service appointments) + credentials line (real, verifiable: Ordine degli Architetti, P.P.C. di [città] · Iscrizione [year] · CTU per [Tribunale or Provveditorato] · Docenza [università]) | 260 |
| 5 | `cs-cases-preview` magazine-grid | 4 completed projects · LF-2 L7 · 1 hero card + 3 small cards | Magazine-grid 1+3 layout. **Hero card** (slot_3 image · spans 7 cols at 1920): h3 project name + caption: "Sede istituzionale · Verona · 2023 · committenza pubblica" + ~70w narrative + "Vedi opera" link. **3 small cards** (slot_4 images · 3 × ~5 cols stacked at 1920): each = h3 project name + 1-line caption (anno · committenza · città) + ~50w narrative. Cards read as monograph-spread tiles with image-over-caption rather than caption-only-row | 360 (1 × 70 + 3 × 50 + chrome) |
| 6 | `cs-cta` dark closer | Restates voice anchor + final CTA · the ONE dark band on home (CS-TONE-03) | Dark `--primary` band (graphite). Centred copy · larger h2 (44px) · single filled-burgundy CTA "Avvia una committenza." Voice anchor restated verbatim: "Ogni opera istituzionale risponde al suo *luogo*." Sub-line (1 line): "Apri un brief con lo studio. Una conversazione, non un preventivo." | 60 |

**Total**: ~1460 rendered + chrome overhead → ~1550 with footer/nav copy. With upper-band targeting per §3.4 below the build lands at ~1600 — comfortably inside the cluster's 1500-2500 range.

### Why no `cs-pillars` band

LF-2 explicitly replaces pillars with the narrative essay-with-anchors at L4. The 4 essay topics ARE the pillars; they're rendered as anchored prose paragraphs rather than as 3-or-4-up cards. CS-DENSITY-02 (cluster invariant: 3-4 pillars) is satisfied because the essay names 4 anchor topics; the visual treatment is family-scoped per CS-LAYOUT-04.

### Why no separate KPI dark band

LF-2's L5 = hero-overlay; the 3 KPI stats live inline inside the hero credit overlay. CS-TONE-03 (one dark band on home) is satisfied by `cs-cta` dark closer. CS-LAYOUT-05 fallback rule: "if family elects hero-overlay, dark band moves to the closer."

### Why no `cs-trust` marquee

LF-2 sequence B does not include a trust marquee. Cornice's trust signals are folded into:
- Hero credit overlay (3 inline stats + commission-credit line)
- Narrative essay (mentions key institutional commissions in prose)
- Sectors ribbon (commission types)
- Leadership credentials (Ordine + CTU + Docenza)

This is the LF-2 grammar — proof through the work, not through marquee badges.

### Anti-pattern guards baked in

- **CS-RHYTHM-04** (no two adjacent sections share function): hero (proposition) → narrative (essay) → sectors (segment listing) → leadership (architect) → cases (built work) → cta (closer) — every adjacent pair is functionally distinct. Style-critic at A.6 verifies.
- **CS-DENSITY-04** (3-4 KPI stats): 3 in hero overlay (within band).
- **CS-DENSITY-06** (3-6 cases on home): 4 (1 hero + 3 small).
- **CS-PAL-05** (≤3 accent hits per viewport): hero CTA + nav CTA + closer CTA = 3 across the home, never 3 in a single viewport. Hero CTA is outline (counts as half-hit at first scroll).
- **CS-COMP-06** (no wall-of-text opener): home opens with hero → narrative essay (not a wall-of-text "Our Story" — narrative is anchored prose with side-rail navigation, structurally distinct).
- **CS-TONE-03** (one dark band on home): only the cta-closer band; hero overlay is not a dark band per CS-LAYOUT-05 hero-overlay convention.

---

## 7 · Navbar · footer direction

### Navbar (`split-wordmark-masthead` · LF-2 L8)

- Sticky · `background: var(--primary)` (graphite `#23262A`) · cream link text
- **Wordmark**: split-line two-row layout (publication-masthead grammar)
  - Row 1: **"Cornice"** (Cormorant Garamond · 22px · cream)
  - Row 2: **"Architettura"** (Work Sans · 11px · 0.22em letter-spacing · cream-dimmed)
  - This is the L8 differentiator — the only sibling that uses split-wordmark; Pragma/Fiscus/Solaria are single-line wordmarks, Continua is condensed-minimal
- 5 links: `Lo studio · Lavoro · Archivio · Studio · Contatti` (5 = cluster default)
- Trailing accent CTA: `"Avvia una committenza"` · solid burgundy `#6E2A2D` on graphite · the chrome's only filled element (CS-NAV-04 · burgundy touchpoint #1)
- Locale switcher: pill with `lang` + `dir` per link · sits between last nav item and CTA · CS-NAV-03 (active for Phase X.5b)
- `:focus-visible` burgundy ring (2px outline · 4px offset) · CS-NAV-02 · the cluster's signature interactive moment (burgundy touchpoint #2)
- 4 link states (default / hover / focus / active) · all distinct
- Mobile (≤880px): hamburger drawer · CSS-only · per X.4a step1d hardening (the corporate-suite skin already carries this; Cornice inherits via `_base.html`)

### Footer (`four-col-with-whistleblowing` · LF-2 L9)

- 4 columns on `--primary` background · cream type (different from Pragma/Fiscus/Solaria's 3-col; same column count as Continua but distinct content shape)
- **Col 1 brand**: split wordmark + 1-line studio one-liner · "Studio di architettura per committenze istituzionali."
- **Col 2 sitemap**: 5 nav links + 3 secondary (Trasparenza · Privacy · Cookies)
- **Col 3 contact + offices**: address (sede principale) · email (`studio@cornice.it`) · phone · 2 satellite offices/cantieri (Verona · Padova) — distinguishes from Continua's column 3 which carries CdF schedule
- **Col 4 whistleblowing + tendering**: D.lgs. 24/2023 channel link (first-class, not footnote) + tendering registry link (PA art. 30) + albo iscrizione (Ordine degli Architetti) — this column is the LF-2-distinct content
- Legal row at bottom: P.IVA · privacy · cookie · whistleblowing link (CS-FOOT-02)
- Footer collapses to 1 column at ≤720px (CS-FOOT-05)
- Latin wordmark + Latin numerics preserved under RTL · CS-FOOT-03 (Phase X.5b)

### Burgundy touchpoint inventory (Risk 4 mitigation)

The archive-burgundy accent must appear at ≥ 3 viewport touchpoints to land as the cool/warm/warm palette's load-bearing differentiator. The build commits to 5:
1. Trailing nav CTA (solid burgundy on graphite)
2. `:focus-visible` ring on every interactive element (2px burgundy outline)
3. Pillar-narrative anchor-link underline on `:hover` / `:focus-within`
4. Magazine-grid case-card "Vedi opera" link underline
5. cta-closer single filled-burgundy button

Style-critic at A.6 confirms the 5 touchpoints render at 1920 first scroll. Walk at A.7 confirms at 1280 + 720 the burgundy is still visibly distinct from graphite background and travertine hairlines.

---

## 8 · Proof architecture

**Rendering principle**: completed-built-work as public-record proof. Time-axis carries the proof, but the artefact (the building, in a city, with a year) is the unit of truth.

| Surface | Concrete shape |
|---|---|
| Hero credit overlay (3 inline stats) | `12 opere realizzate · 3 città · 28 anni di pratica` (NOT pure numeric like Pragma's "22 anni · 180+ mandati" — the unit is OPERE not MANDATI; the noun carries the discipline) |
| Hero credit overlay project line | `Sede istituzionale committenza pubblica · Verona · 2023` — names a real (anonymized-into-real-archetype) commission as the cover image's identity. Different from Pragma `(Direzione · Anno fondazione)`, Fiscus same, Solaria `(Direzione · Cert.)`, Continua `(Custodi · Iscrizione Albo Trustees)` |
| Sectors ribbon | "Committenze realizzate" labelled segments — names the audience as commission-types not industries; 6 segments cover civic / corporate / masterplan / campus / restoration / public-equipment |
| Leadership single-portrait | architect's name + role + 1 verifiable albo credential (Ordine Architetti P.P.C.) + CTU/docenza credential — NOT a list of 3-4 cards like Continua's |
| Cases magazine-grid (home) | "Lavoro" labelled section; 4 cards each carry: project name + commission type + city + year + role + ~50-70w narrative + image. Public-record proof shape. Different from Pragma's "Casi seguiti" (NDA-anonymized), Fiscus's "Casi seguiti" (anonymized), Solaria's "Casi anonimizzati" (method-context), Continua's "Mandati in continuità" (timeline) |
| Case detail page | adds an `archive-context` slot mirroring Solaria's `method-context` and Continua's `continuity-context` precedents — slot shows project archive metadata: Committente · Importo dell'opera · Periodo realizzativo · Stato (consegnata · in cantiere · in archivio storico) · Bibliografia (publications, monograph references). Detail-page order: hero-strip + narrative + `archive-context` + `prossima-opera`. |
| Trust band — none | LF-2 sequence B does not include a trust marquee; trust is carried by the leadership credentials + sectors ribbon + cases archive metadata |

**What this avoids**: numeric-KPI inflation (cluster's first 4 siblings all use it), NDA-anonymization opacity (no client identified anywhere), "Aziende sponsor recenti" (Solaria's banlist), and "Mandati in continuità" (Continua's). Cornice's proof is editorial-curatorial-public-record: the work is identifiable, the year is named, the city is named, the commission type is named.

---

## 9 · Hero architecture

LF-2 stacked-editorial hero (L1) is the cluster's first non-55/45 hero. Below the hero photo (full-bleed at the top of the page), the home renders an 8/4 column layout:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│        ┌──────────────────────────────────────────────────┐     │
│        │  HERO PHOTO (slot_0 · institutional building     │     │
│        │  exterior at dusk · full-bleed)                  │     │
│        │                                                  │     │
│        │             ┌────────────────────────┐           │     │
│        │             │ CREDIT OVERLAY (lower-3rd)        │     │
│        │             │ "Sede istituzionale ·  │           │     │
│        │             │ committenza pubblica · │           │     │
│        │             │ Verona · 2023"         │           │     │
│        │             │                        │           │     │
│        │             │ ─────────────────────  │           │     │
│        │             │ 12 opere · 3 città ·   │           │     │
│        │             │ 28 anni di pratica     │           │     │
│        │             └────────────────────────┘           │     │
│        └──────────────────────────────────────────────────┘     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────┐  ┌─────────────┐      │
│  │ h1 (Cormorant Garamond 60px)        │  │ side-quote  │      │
│  │ "Ogni opera istituzionale risponde  │  │ pull        │      │
│  │  al suo *luogo*."                    │  │ "Misuriamo  │      │
│  │                                     │  │  il lavoro  │      │
│  │ 1-line subhead (Work Sans 18px)     │  │  in opere   │      │
│  │ "Studio di architettura per         │  │  consegnate"│      │
│  │  committenze istituzionali. ..."    │  │             │      │
│  │                                     │  │ – Studio    │      │
│  │ [ Avvia una committenza → ]         │  │             │      │
│  │   (outline-burgundy on cream)       │  │             │      │
│  └─────────────────────────────────────┘  └─────────────┘      │
│       (8 cols)                              (4 cols)            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Hero specifics

- **Photo aspect ratio**: 16:7 at 1920 (landscape · cinematic) · 4:3 at ≤768 · 3:2 at ≤390 (responsive crop via `object-position: 50% 35%` to preserve the upper third of the building)
- **Credit overlay**: positioned lower-third of photo · cream paper backing at 92% opacity · 24px padding · burgundy hairline rule between project-credit line and inline KPI stats · the only place where stats render at home (no separate band)
- **Text below photo**: 100×72 padding + 1400 max-width per CS-RHYTHM-01 · 8/4 col grid via CSS Grid · responsive collapse to single-column at ≤880
- **h1 italic**: only on `luogo` (one em-wrap · CS-TYPE-02 default · NOT contrast pair like Solaria)
- **Side-quote pull**: Cormorant Garamond italic · 22px · 4-col right rail · attribution "– Studio" or "– Cornice" (single line)
- **Hero CTA**: outline-burgundy on cream · "Avvia una committenza" (CS-CTA-01 polarity) · NEVER filled at hero (filled only in the dark closer · cluster's signature CTA polarity inversion)

### Hero accessibility

- AAA contrast on h1 (Cormorant Garamond 60px on cream `#F4ECDB` with graphite ink `#1F2426` reads ≥ 13.5:1)
- AAA contrast on credit overlay (graphite text on 92% cream backing)
- `:focus-visible` 2px burgundy ring on the hero CTA (CS-NAV-02)
- Photo `<img>` carries descriptive `alt` text naming the building's program (e.g., "Sede istituzionale, Verona, completata nel 2023, vista al crepuscolo dalla piazza pubblica")

---

## 10 · Leadership architecture

LF-2 L6 = single-portrait-feature. Cornice ships ONE portrait, masthead-sized, with a 2-paragraph bio.

```
leadership_block:
  presence:                  SINGLE-PORTRAIT-FEATURE (LF-2 L6 · cluster's 1st)
  card_count:                1 (NOT 3 like Continua · NOT 2 like Solaria · NOT 0 like Pragma/Fiscus typographic)
  layout:                    5-col portrait + 7-col bio (1920) · stacked at ≤880

  founding_architect:
    name:                    [TBD at A.4 — placeholder "Margherita Salviati"]
    role_label:              "Architetto fondatore"
    portrait:                slot_2 (60s+ environmental · atelier OR site)
    bio:                     2 paragraphs (~180w total)
                             para 1: career arc + formative training + sede
                                      principale (Verona / Padova)
                             para 2: 3 named completed institutional
                                      commissions (no NDA · these are public
                                      record by definition) + 1 public-service
                                      appointment OR 1 docenza
    credentials:             real, verifiable, public-record:
                              · Ordine degli Architetti P.P.C. di Verona ·
                                Iscrizione 1996
                              · CTU presso il Provveditorato Interregionale
                                alle OO.PP. del Triveneto
                              · Docenza · Università IUAV di Venezia ·
                                A.A. 2018-2022
                              (NOT "Partner / Senior Associate / Counsel" ·
                               NOT "ODCEC iscritti" · NOT "ICF-PCC" · NOT
                               "Albo Trustees")
    visible_demographic:     60s+ · weathered hands · long-practice signal ·
                             demographic distance from Solaria slot_2 +
                             Continua slot_2 confirmed at A.3
```

**Why single-portrait**: the founding architect's career *is* the studio's portfolio. Multi-card grids (Continua's 3-card pillar-photo · Solaria's 1+1 · Pragma/Fiscus's typographic-grid) flatten the principal–associate hierarchy that institutional architecture firms organise around. The single-portrait masthead is the canonical Phaidon-monograph composition; using it lands the LF-2 voice gravity at second-scroll.

**Mitigation binding** (Risk 3 · §6 master): the portrait is **environmental** (architect in atelier with model + drawings, OR architect on-site with hard-hat). Demographic distance from Solaria's slot_2 (30s Caucasian) is mandatory; target 60s+ with visible signs of long-term-practice. Curator hard-rejects studio-headshot, suit-and-tie corporate dress, visible laptop, subject ≤ 50s.

**The associates / staff** are NOT shown on home. They appear on `/lo-studio/` (about page) as a small typographic list at the bottom of the architect's bio, not as a card grid. This keeps the home page focused on the founder-as-monograph-protagonist.

---

## 11 · CTA logic

### Primary CTA copy

`"Avvia una committenza"` — institutional-civic register. Reads "open a commission" in the way an architect would speak to a public-tendering official, not "book a call" in the way a SaaS would.

### Polarity rules (CS-CTA-01 · cluster ratification 2026-04-26 · do not re-litigate)

- On cream paper: outline-only · burgundy border · burgundy label · burgundy on `:focus-visible`
- In the dark CTA-closer band: filled burgundy on graphite · the polarity inversion is the cluster's signature CTA move
- Hover on cream: 4px burgundy underline grows from baseline (NOT a fill swap on cream)
- Hover on dark: burgundy deepens 8% via `filter: brightness(0.92)` (NOT a colour change)

### Form gate (`/contatti/`)

Commission-brief shape · 4 fields:

1. **Programma** (textarea · placeholder: "Descriva il programma e il committente. Es.: 'Sede direzionale per gruppo industriale · 4.500 mq · committente privato'.")
2. **Giurisdizione/sede** (text · placeholder: "Provincia, regione o nazione del sito")
3. **Orizzonte realizzativo** (select · `Studio di fattibilità · Concorso/concept · Definitivo-esecutivo · Direzione lavori in corso · Monitoraggio post-consegna`)
4. **Tipo committente** (select · `Pubblico (PA / Ente locale / RUP) · Corporate · Pubblico-privato (PPP) · Fondazione / Ente non-profit`)

NOT P.IVA + CF (Fiscus collision). NOT NDA-ready boardroom form (Pragma collision). NOT ICF code-of-ethics referenced (Solaria collision). NOT scope+orizzonte+struttura familiare (Continua collision). The **programma + tipo-committente** fields are the differentiating fields — Cornice's intake names a BUILDING PROGRAM and a CLIENT TYPE; no sibling has either.

### Hero CTA repetition

- Hero: outline-burgundy on cream (1 hit, half-weight)
- Nav trailing: filled-burgundy on graphite (1 hit)
- cs-cta closer: filled-burgundy on graphite (1 hit)

3 across the home, never 3 in a single viewport. Below CS-PAL-05 ceiling.

### CTA copy banlist respected

- NOT "Get started free" · NOT "Sign up now" · NOT "Iscriviti gratis" (CS-CTA-02)
- NOT "Fissa una call privata" (Pragma)
- NOT "Primo appuntamento" (Fiscus)
- NOT "Prenota una discovery call" (Solaria)
- NOT "Avvia un dialogo di mandato" (Continua)

---

## 12 · Anti-clone constraints (binding for build agent)

The build agent at A.5 reads this list before writing the first line of the skin. The full anti-clone catalogue is in `factory/reports/hardening/lf2-fifth-sibling-pilot.md §4`. Highlights below; consult the master file for the complete list.

### Highlights

- ✗ split-55-45 hero (Pragma/Fiscus/Solaria) · ✗ object-overlay hero (Continua)
- ✗ section sequence A (Pragma) · ✗ A+slot4 (Fiscus) · ✗ C (Solaria) · ✗ D (Continua)
- ✗ any mid-strip section (LF-2 has none)
- ✗ pillars-as-numbered-grid (LF-1/3) · ✗ manifesto-replacement (LF-4) · ✗ 2x2-with-image (LF-5)
- ✗ band-at-3 / band-at-4 / band-at-5 dark KPI band (Cornice's KPI is hero-overlay)
- ✗ typographic-grid leadership (LF-1/3) · ✗ absent leadership (LF-4) · ✗ pillar-photo (LF-5) · ✗ 1+1 photo pair (Solaria style)
- ✗ list-row cases (LF-1/3/4) · ✗ timeline cases (LF-5)
- ✗ sticky-top single-line wordmark (LF-1/3/4) · ✗ condensed-minimal-top (LF-5)
- ✗ 3-col footer (LF-1/3/4)
- ✗ Inter as body sans · ✗ IBM Plex Sans · ✗ Public Sans (taken)
- ✗ Merriweather · ✗ Plex Serif · ✗ Fraunces · ✗ Crimson Pro · ✗ Spectral (taken)
- ✗ navy / gray-blue / warm-carbon / pine as primary · ✗ gold / blunotte / ocra / pewter as secondary · ✗ emerald / caramel / brass as accent
- ✗ render-as-photo imagery (architecture-AI-slop tell)
- ✗ "Casi seguiti" / "Casi anonimizzati" / "Mandati in continuità" cases label
- ✗ italic on temporal noun (Continua) / contrast pair (Solaria) / agency word (Pragma) / imperative (Fiscus) — Cornice italic falls on a SPATIAL noun (`luogo`)

---

## 13 · Browser-live expectations (precis · full plan in `factory/reports/hardening/lf2-fifth-sibling-pilot.md §7`)

The IT walk at A.7 produces:

- 6 pages × 6 viewports = **36 captures** at `factory/reports/browser-verification/cornice-architettura/it/<YYYY-MM-DD>/`
- Plus 1 reduced-motion capture
- Plus 1 contrast report at all 6 viewports
- Plus 1 responsive report at all 6 viewports
- Plus 4 wireframe-overlay pairs at 1920 (vs each of LF-1/3/4/5 live siblings)
- Plus a style-critic report against `corporate-suite-design-standard.md`

**The walk verdict at A.7 must read PASS** (or BORDERLINE → A.8 narrow fix → re-walk) before Commit A draft-landing.

**The 5 risks from §6 master must be verified live**:
1. slot_1 atrium reads "civic monument" not "office lobby" at 1280 + 1024
2. Render-vs-photo gate passes on every architecture image at 1920 + 1280 + 720
3. Founding-architect portrait reads "veteran architect" not "stock professional" at 1920 + 1280 + 768
4. First-30s read = "firm that BUILDS" not "firm that ADVISES" via "remove the studio name" live test
5. slot_2 portrait coherence preserved post-A.3-curation

**The 8 layout-family gates must pass**: CS-LAYOUT-10/11/12/13/14 + B-LAYOUT-1/2/3.

Phase X.5b (5 locales × 36 + AR RTL parity) gates the LIVE flip via `release-decision-orchestrator.md`. IT-only Commit A is the workflow A endpoint for Phase X.5.

---

## 14 · Release-gate expectations

The release-gatekeeper at A.9 reads these. Tier flip from `draft` to `published_live` is a SEPARATE pass (Phase X.5b) and binds on:

- Scorecard ≥ 4.50/5 (4.67/5 is precedent)
- 0 open `[BLOCKING]` findings
- IT walk PASS · 4 locale walks PASS (EN/FR/ES/AR via Phase X.5b workflow C) · AR RTL parity walk PASS
- User-handshake binary SHIP recorded
- Live DOM still matches this brief at flip time
- Pexels-only re-confirmed on live render across all 5 locales
- Distinctness re-confirmed ≥ 4/5 vs every sibling at flip time
- Layout-family classification re-confirmed = LF-2 at flip time
- All walk verdicts ≤ 30 days fresh

---

## 15 · The single-page summary the orchestrator reads at sign-off

```
PLAN SIGN-OFF SUMMARY · cornice-architettura
============================================

What this template is:
    An institutional architecture studio that delivers completed civic
    and corporate built work across northern-Italian cities. Its founding
    architect leads a small atelier on long-horizon commissions. The
    studio measures itself in opere realizzate (built works), not in
    renderings, awards, or speculative entries. Cases are public —
    completed buildings stand in cities under their own name — so the
    proof shape is editorial-curatorial: project, year, commission type,
    city, role.

What this template is NOT:
    NOT Pragma's boardroom advisory (B2B advice, no built artefact).
    NOT Fiscus's commercialista presidio (annual fiscal cycles).
    NOT Solaria's bounded executive coaching (1:1 sessions).
    NOT Continua's family-office stewardship (multi-gen custody).

Voice anchor (IT · verbatim · with <em>):
    "Ogni opera istituzionale risponde al suo <em>luogo</em>."
    (italic on SPATIAL noun · cluster's first)

Layout family: LF-2 (Editorial Spread)
  L1=stacked-editorial · L2=B · L3=absent · L4=essay-with-anchors ·
  L5=hero-overlay · L6=single-portrait-feature · L7=magazine-grid ·
  L8=split-wordmark-top · L9=4-col-with-whistleblowing
  Sub-tuple (L1, L2, L7) = (stacked-editorial, B, magazine-grid) —
  full 3-axis divergence vs every live sibling

Palette: primary #23262A · secondary #D9CFB8 · accent #6E2A2D
Macro tone: graphite + travertine + archive burgundy ·
            cool/warm/warm polarity (the only OPEN combo after Continua)

Typography: Cormorant Garamond + Work Sans

Hero: stacked-editorial · institutional-building dusk exterior with
      project-credit overlay (3 inline KPI stats: 12 opere · 3 città ·
      28 anni); h1+side-quoted intro in 8/4 col below

CTA: "Avvia una committenza" · commission-brief form with
     programma + giurisdizione + orizzonte + tipo-committente
     (programma + tipo-committente are the differentiating fields)

Section moves that distinguish this from siblings:
  1. Stacked-editorial hero with project-credit + 3 inline KPI stats
     (cluster's 1st non-55/45-and-non-object-overlay hero geometry)
  2. Editorial essay-with-anchors replaces pillars (LF-2's 4-paragraph
     essay carries the proposition where LF-1/3 use numbered cards)
  3. Single-portrait-feature leadership · founding-architect masthead
     (cluster's 1st single-portrait composition)
  4. Magazine-grid 1+3 cases with project images (cluster's 1st
     image-bearing case-preview at home)
  5. Graphite + travertine + archive-burgundy · cool/warm/warm
     polarity (only OPEN combo after Continua)

Distinctness scores:
  Skin (4-of-5 axes):    vs Pragma 5/5 · vs Fiscus 5/5 · vs Solaria 5/5 · vs Continua 5/5
  Layout (4-of-9 dims):  vs Pragma 8/9 · vs Fiscus 9/9 · vs Solaria 9/9 · vs Continua 8/9
  (L1, L2, L7) sub-tuple: full 3-axis divergence vs every live sibling
  GATE:                  PASS (CS-LAYOUT-12 + CS-LAYOUT-13 + DISTINCTNESS_RULES §1)

Imagery pack: business-architecture · curator-approved at A.3 · 6 URLs Pexels-only

Initial locale: it (others at Phase X.5b · workflow C)
Initial tier: draft

Browser walk plan: 6 viewports × 1 locale (it) × 6 pages = 36 captures
  + 1 reduced-motion + 4 wireframe-overlay pairs + contrast/responsive reports
Walk artefact dir: factory/reports/browser-verification/cornice-architettura/it/<YYYY-MM-DD>/

Scorecard expected grade: ≥ 4.50/5

Open questions for orchestrator:
  - Cormorant Garamond vs Cormorant Infant fallback decision at A.5 build entry
  - Travertine secondary vs cream paper contrast handling at A.5 build entry
    (travertine confined to hairlines/dividers/8-col body backing)
  - slot_2 portrait fallback search lane decision at A.3 curator entry
    (3 lanes pre-authorised: drafting-table-glasses · site-hard-hat · office-model-desk)
  - AR RTL editorial register at workflow C pre-flight (Phase X.5b · not blocking IT pass)
```

The studio-name swap test re-runs on this summary at A.2 sign-off per `pre-build-quick-checks §5`. If the swap collapses any line above into a generic, the brief returns for re-spec.

---

## 16 · What this brief is and is not

**This brief IS**:
- A complete, decision-locked planner-brief equivalent for the Phase X.5 LF-2 pilot.
- Ready to hand to a workflow A.3 (curator) → A.4 (copy) → A.5 (build) chain with no re-spec.
- The contract the style-critic re-reads at A.6 and the walk-verifier re-reads at A.7.
- The cluster's first LF-2 (Editorial Spread) build specification.

**This brief is NOT**:
- A real `template_dna.py` entry (the build at A.5 writes that).
- A real seed file (A.5 writes that).
- A curator-approved Pexels pack (A.3 produces that, with cross-cluster grep on file).
- A copy diff (A.4 produces that with the voice anchor verbatim).
- A critique or walk verdict (A.6 / A.7).
- A multilingual rollout (Phase X.5b · deferred to workflow C after IT-walk PASS).

If a real workflow A pass picks this up tomorrow, it routes to:
1. **A.3 imagery-curator** — with §4 pack spec as input · runs cross-cluster grep BEFORE committing URLs · render-vs-photo 3-gate per candidate · slot_2 CAUTION escalation pre-authorised · curator approval gate before A.4
2. **A.4 copy-translation** — with §6 word-targets and §3 voice anchor + em-word as input · IT only · D-102 cadence
3. **A.5 template-builder** — with §3 DNA + §6 section sequence + §7 nav/footer + §9 hero architecture + §10 leadership architecture as input · CLI green + IT live URL openable · introduces `_layouts/lf2/` per-family override path
4. **A.6 critique** — three reports against the design standard, the contrast rules, and the responsive matrix · plus the 4 wireframe-overlay pairs vs LF-1/3/4/5
5. **A.7 walk** — 6 pages × 6 viewports + the 8 layout-family gates · verdict per `factory/reports/hardening/lf2-fifth-sibling-pilot.md §7`
6. **A.9 aggregate** — scorecard, user-handshake, Commit A request

Gates between every step. No skipping.
