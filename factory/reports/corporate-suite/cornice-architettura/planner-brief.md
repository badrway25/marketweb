# Cornice · Factory planner brief · LF-2 · 5th corporate-suite sibling

```yaml
report_type:        planner
template_slug:      cornice-architettura
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread
agent:              template-planner (paper-only · Step 2 promotion)
role:               primary
phase:              X.5 · cornice-architettura · Step 2
date:               2026-04-30
inputs_consumed:
  - factory/reports/corporate-suite/cornice-architettura/intake.md (binding input contract)
  - factory/standards/corporate-suite-design-standard.md
  - factory/standards/corporate-suite-imagery-standard.md (§1 sourcing · §2 6-slot pool)
  - factory/standards/corporate-suite-blocking-rules.md §3 (18 hard blockers)
  - factory/standards/corporate-suite-multi-agent-sop.md §3.1 (planner mission)
  - factory/agents/template-planner.md
  - factory/agents/imagery-curator.md (handoff contract)
  - factory/reports/hardening/corporate-suite-layout-family-matrix.md (LF-2 row authoritative)
  - factory/reports/hardening/corporate-suite-layout-divergence-plan.md (Step 6 enrolment)
  - factory/reports/hardening/corporate-suite-layout-variance-rules.md (CS-LAYOUT-* rule book)
  - design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
  - design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md
  - design-orchestrator/DISTINCTNESS_RULES.md (4-of-5-axes gate)
outputs:
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md (this file)
  - factory/reports/corporate-suite/cornice-architettura/prebuild-quick-checks.md (5-check re-run)
status_tag:         DRAFT-INTERNAL · ready for orchestrator A.2 sign-off
verdict:            n/a · upstream authoring agent
next_action:        Hand off to imagery-curator · path:
                    factory/reports/corporate-suite/cornice-architettura/planner-brief.md ·
                    status: BLOCKED until orchestrator A.2 sign-off · then handoff to A.3
                    imagery-curator with §4 pack spec as input · cross-cluster grep BEFORE
                    committing URLs · curator approval gate before A.4 copy-translation
```

This brief is concrete enough to start the build immediately. Every field is decision-locked. Where the brief leaves a tactical choice (heading-serif fallback, AR Naskh-vs-Kufi at workflow C, layout-router file placement), the choice is named and bounded — not deferred.

The brief inherits `intake.md` verbatim where the intake declared concrete values; it expands each declaration into implementation-ready spec.

---

## 1 · Required inputs (intake summary)

| Field | Value |
|---|---|
| `template_slug` | `cornice-architettura` |
| `studio_name` | Cornice |
| `wordmark_form` | split-line masthead — line 1 "CORNICE" · line 2 "studio di architettura" |
| `cluster` | `corporate-suite` |
| `sub_cluster_label` | architecture-firm · single-principal studio (editorial-led) |
| `archetype` | `corporate-suite` |
| `layout_family` | **LF-2 · Editorial Spread** (5th sibling · 1st LF-2 occupant · OPEN-claim per family-matrix §3) |
| `audience_profile` | Committenza pubblica e privata · enti culturali · committenze di restauro · uffici tecnici comunali · sviluppatori privati con sensibilità editoriale. Progetti residenziali, pubblici, di interno, paesaggistici, di restauro, concorsi. Valore commissionato per qualità editoriale + caso-studio, non per numero di mq. |
| `org_scale` | 1 founding architect + 2 collaboratori (single-principal studio · NOT multi-partner) |
| `locales` | `[it]` initial · others enter via workflow C |
| `nearest_two_siblings` | Pragma (institutional voice) · Continua (object-led imagery) |
| `furthest_sibling` | Solaria (warm-coaching · 1:1 conversation · single-practitioner manifesto) |
| `user_constraints` | see `intake.md §11` (8 must-haves · 13 must-avoids) |
| `target_tier` | `draft` · D-102 cadence |
| `pexels_pack_status` | `not started` · curator briefed by §4 of this file at A.3 entry |

---

## 2 · Forbidden similarities + collision check (planner contract)

The 47 explicit anti-collision lines from `intake.md §4` are inherited here verbatim. The collision check matrix lives in §6 of this file. Headline result: **5/5 vs Pragma · 5/5 vs Fiscus · 5/5 vs Solaria · 5/5 vs Continua** — plan sign-off authorised on `DISTINCTNESS_RULES.md §1` (≥4/5 gate).

Hard prohibitions (planner-brief-schema §2.1 · no waiver, ever) all satisfied:
- ✓ No URL appearing in another corporate-suite sibling's pool — cross-cluster grep mandatory at A.3
- ✓ Inter is NOT body sans (Source Sans 3 instead)
- ✓ `--primary-2: #2c3e6b` is NOT introduced into the skin (CS-PAL-03)
- ✓ Hero credit overlay is NOT KPI tuple / fiscal-calendar / percorso-cadenza / stewardship-horizon-strip
- ✓ `--primary` (`#1F2226`) L\* ≈ 12 — well under 40 cream-safe ceiling (CS-PAL-01)
- ✓ No lorem ipsum / placeholder copy
- ✓ Pexels-only · no Unsplash carve-out
- ✓ No geometric sans on heading
- ✓ LF-2 layout-family declaration is OPEN-claim, not collision

LF-2-specific family-level demotions of cluster invariants (per divergence plan §3 + family-matrix §1) are **declared, not silent** — see §6 row "Layout family invariants demoted":
- CS-HERO-01 (55/45 hero) → demoted at family level · LF-2 declares stacked-editorial
- CS-TONE-03 (one dark band on home) → demoted at family level · LF-2 declares zero dark bands
- CS-RHYTHM-02 (fixed home sequence A) → demoted at family level · LF-2 declares sequence B
- CS-NAV-01 (sticky-top wordmark-only) → demoted at family level · LF-2 declares split-wordmark-top
- CS-FOOT-01 (3-col footer) → demoted at family level · LF-2 declares 4-col-with-whistleblowing

---

## 3 · Design DNA · `template_dna.py` shape

```python
TemplateDNA(
    archetype="corporate-suite",
    sub_cluster="architecture-firm-single-principal",
    layout_family="LF-2",                       # NEW · CS-LAYOUT first explicit value · routes _layouts/lf2/home.html

    hero_style="stacked-editorial-cornice",     # LF-2 L1 · 8/4 split BELOW full-bleed photo · NOT 55/45
    navbar_style="split-wordmark-cornice",      # LF-2 L8 · "CORNICE" / "studio di architettura"
    footer_style="four-col-cornice",            # LF-2 L9 · brand + sitemap + contact + disclosures-with-whistleblowing

    section_order=[
        "hero",                     # LF-2 stacked-editorial · h1 + side-quoted intro · KPI in overlay
        "narrative",                # LF-2 L4 · 4-paragraph essay with pull-quotes + side-rail anchors
        "sectors-ribbon",           # sentence-ribbon · "Tipologie d'intervento"
        "leadership-single",        # LF-2 L6 · single-portrait masthead
        "cases-magazine-grid",      # LF-2 L7 · 3+1 magazine grid
        "cta-closer-cream",         # LF-2-specific · cream hairline-bordered band · NOT dark
    ],

    card_style="magazine-card-cornice",     # cream paper · graphite border · rust hover-rule
    button_style="ghost-cornice",           # outline-only on cream · filled rust ONLY in CTA closer
    density="airy-editorial",               # cluster invariant + LF-2 narrative breathing
    tone="editorial-curatorial",
    imagery_direction="architecture-editorial-built-form",
    imagery_key="business-architecture",
    conversion_pattern="project-dossier-submission",

    font_pairing=("Cormorant Garamond", "Source Sans 3"),

    palette={
        "primary":   "#1F2226",   # graphite · L* ≈ 12 (cream-safe) · NEUTRAL
        "secondary": "#C7BFB1",   # pietra-serena · drafting-paper stone · NEUTRAL
        "accent":    "#B7491F",   # terracotta-rust · WARM · the cluster's only NEUTRAL/NEUTRAL/WARM polarity
        "paper":     "#F4ECDB",   # cream paper · cluster invariant
        "ink":       "#1B1F23",   # body text on cream · NOT primary
    },

    voice_anchor="Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.",
    voice_anchor_em_word="argomento",
    voice_anchor_contrast_pair=False,
)
```

### Why every line is non-negotiable

| Field | Decision | Anti-collision rationale |
|---|---|---|
| `layout_family="LF-2"` | first explicit LF-2 occupant | Validates the layout-family system per divergence plan §10 Step 6 · forces the build to introduce `_layouts/lf2/home.html` (or its inline equivalent) — a structural change the cluster needs |
| `primary #1F2226` | graphite | NOT navy (Pragma) · NOT gray-blue (Fiscus) · NOT warm-carbon (Solaria) · NOT deep-pine (Continua) · L\* well under 40 cream-safe ceiling · reads as architectural-ink not as a brand colour |
| `secondary #C7BFB1` | pietra-serena | drafting-paper stone · neutral-warm-light · NOT cool-blue (Pragma) · NOT warm-gold (Fiscus) · NOT warm-ocra (Solaria) · NOT cool-pewter (Continua) |
| `accent #B7491F` | terracotta-rust | NOT emerald (Pragma) · NOT deep-navy (Fiscus) · NOT caramel (Solaria) · NOT antique-brass (Continua) · rust reads "ceramic / terracotta / earthen pigment" — the architectural pigment of Italian materials · cluster's NEUTRAL/NEUTRAL/WARM is the only un-claimed polarity |
| `font_pairing` | Cormorant Garamond + Source Sans 3 | Cormorant on matrix §1.4 OPEN · display-elegant editorial register suited to LF-2 stacked spread · Source Sans 3 explicitly NOT Inter — closes the §1.4 cluster-collapse risk · NOT Plex Sans (Fiscus) · NOT Public Sans (Continua) |
| `voice_anchor` | one sentence + one em on `argomento` | one em is the default per CS-TYPE-02 · contrast-pair (Solaria) explicitly avoided · em-word names the project's KIND not its action |
| `card_style="magazine-card-cornice"` | LF-2 magazine-grid card style | L7 cases-preview shape is `magazine-grid` (LF-2 declared) · cards differ from list-row (Pragma/Fiscus/Solaria's L7) and from timeline (Continua's L7) |

### Heading-serif fallback (decision-locked at A.5 entry)

Cormorant Garamond is the primary choice for its display-elegant editorial register. If at A.5 the build session encounters a licence/availability friction (Google Fonts API failure · weight-set incomplete · italic glyph coverage thin at display sizes), the substitution is **Spectral** (humanist transitional · highly readable across heading + body). Do NOT substitute Cormorant with Lora or PT Serif — both have lower display-italic personality and would soften the editorial-curatorial register at h1 64px. Spectral is the binding fallback. GT Sectra is rejected as fallback (paid licence).

### Body-sans fallback (decision-locked at A.5 entry)

Source Sans 3 is the primary choice. Binding fallback: **Manrope** (modern humanist · matrix §1.4 OPEN). Do NOT substitute with Inter (banned) · Plex Sans (Fiscus) · Public Sans (Continua) · Work Sans (acceptable but Manrope is closer to editorial-clean register).

---

## 4 · Imagery DNA · `business-architecture` pack (input to A.3 imagery-curator)

The pack file lives at `docs/content-factory/imagery/packs/business-architecture.md` after A.3. The 6 slots below are **subject specifications**; real Pexels URLs land at A.3 with cross-cluster grep on file. Pool-key naming convention `business-<kind>` per CS-IMG-POOL-03 — `business-architecture`.

```yaml
imagery_pack:
  imagery_key: business-architecture
  pool_source: Pexels                # CS-IMG-SRC-01 · no Unsplash carve-out
  pool_size: 6                       # CS-IMG-POOL-01 · 6-slot pool · cluster contract
  pack_extras: 4                     # additional case-card photos for LF-2 magazine-grid
  pack_total_candidates: 24-32       # CS-IMG-POOL-04 · pack file holds 20-40 candidates

  slot_0_hero:
    subject:        a built courtyard / portico of one of the studio's projects
                    at golden hour · stone or concrete material clarity ·
                    sharp architectural shadow lines · landscape composition ·
                    NO people · deep DoF on foreground colonnade with mid-
                    ground court receding · h1 area is BELOW-photo (LF-2
                    stacked-editorial) so the photo carries no text overlay
                    constraint at top — credit overlay sits at bottom-left
    mood:           editorial-architectural · golden-hour · structural ·
                    cinematic-but-quiet
    composition:    landscape · subject framed for full-bleed top of stacked
                    hero · vertical structural element (column / wall edge)
                    grounded near horizontal third
    color_temp:     warm sunlight on cool stone · neutral overall
    coherence:      the building IS the firm's value proposition · the firm's
                    work is published, not its meeting rooms or its desks
    pexels_search:  "architectural courtyard portico golden hour shadow stone"
                    backup: "modern Italian architecture courtyard interior light"
    feasibility:    GO (10-15 plausible candidates · §3 quick-check GO)
    rejection_rules_for_curator:
                    REJECT: any human (even partial limbs) · any vehicle ·
                            any signage with brand text · any cosy-interior
                            with wood tones (Continua adjacency) · any tax-
                            document or paper-work in frame (Fiscus adjacency)
                    REJECT: any photo where the building is incidental and
                            people-in-foreground are the subject (Pragma
                            adjacency) — the building must be unambiguously
                            the subject
                    REJECT: cliché modernist-glass-tower from below (stock-
                            architecture cliché · imagery-standard §13 stock-look diagnostic)

  slot_1_feature:
    subject:        a scaled architectural model on a drafting table ·
                    raking light from window · trace paper · drafting pencil ·
                    architect's compass · NO people · deep DoF on model with
                    table edge in foreground
    mood:           workshop-editorial · process-as-proof · quiet-craft
    use:            about.html hero band · narrative-essay second column on home
    coherence:      shows what the editorial-curatorial work LOOKS like in
                    process — same architectural world as hero, but framed
                    at studio-craft scale rather than built-form scale
    pexels_search:  "architectural model drafting table trace paper compass"
                    backup: "scale model architecture studio raking light"
    feasibility:    GO (8-12 candidates · §3 quick-check GO)
    rejection_rules_for_curator:
                    REJECT: any laptop / monitor / digital screen visible
                            (the studio's craft is hand-drafted + printed) ·
                            any computer-rendered model on screen ·
                            any office-grade model setup (the model must
                            read as in-progress not as a museum piece)

  slot_2_portrait:
    subject:        founding architect · 50s · environmental portrait at
                    studio window · drafting tools (compass · ruler · pencil)
                    in soft-focus mid-ground · direct gaze · neutral
                    background · natural side-light · seated or standing
                    three-quarter
    mood:           senior · serious · editorially photographed · NOT a
                    LinkedIn headshot
    diversity_note: explicit visible age (50s) and visible craft context ·
                    NOT 30s × 2 (Solaria gap) · NOT 60s + 40s pair
                    (Continua's pattern) — LF-2 has only ONE portrait
                    so the SINGLE choice carries the whole leadership read
    pexels_search:  "architect 50s studio window drafting tools natural light"
                    backup: "Italian architect portrait studio environmental"
    feasibility:    GO (8-12 candidates · §3 quick-check GO)
    rejection_rules_for_curator:
                    REJECT: pure white / grey / seamless studio backdrop
                            (LinkedIn-headshot tell) · shoulders-up tight
                            crop · pure face-only framing without environmental
                            context · corporate-suit + tie (suggests advisory
                            not architecture · Pragma adjacency)
                    REJECT: any photo where the subject reads as "model on
                            a stock photoshoot" rather than "real architect
                            in their studio"
                    BIND:   subject MUST be in 50s OR clearly senior-mid-career ·
                            drafting-tools or sketches MUST be visible in the
                            mid-ground · environmental NOT studio-backdrop

  slot_3_portrait_or_project_alt:
    subject:        SECONDARY use · LF-2 has only one portrait on home · this
                    slot serves about.html team-grid OR a project-interior
                    photo for case-card use · either:
                    (a) collaboratore portrait — 30s/40s · different gender
                        and ethnicity from slot_2 · environmental at
                        drafting board · for about.html team-grid
                    OR
                    (b) project-interior at golden hour · stone-and-light ·
                        NO people · used as 4th case-card photo for
                        magazine-grid extras
    mood:           collaboratore-as-team OR project-interior-as-evidence
    diversity_note: if (a) chosen — explicit visible variation from slot_2
                    (age + gender + ethnicity); if (b) chosen — interior
                    case-photo at distinct project from slot_0
    use:            about.html team-grid OR cases magazine-grid card #4
    pexels_search_a: "young architect collaborator drafting board"
    pexels_search_b: "project interior architecture stone light no people"
    feasibility:    GO (10-15 candidates either path)
    decision_at_a3: curator picks (a) or (b) at A.3 entry based on which
                    serves the about.html team-grid better; default is (a)
                    if no other constraint binds
    rejection_rules_for_curator:
                    REJECT (a): same demographic as slot_2 (pair must read
                                visibly distinct) · headshot framing
                    REJECT (b): any people · any wood-tones-warm interior
                                (Continua adjacency)

  slot_4_detail:
    subject:        architectural section drawing close-up · india ink on
                    parchment · architectural section visible · cropped
                    tight · NO documents · NO laptop · NO eyeglasses-on-
                    paperwork · OR architect's compass on trace paper at
                    macro distance · cream paper texture visible
    mood:           archival-editorial · craft-evidence · quiet
    coherence:      replaces "documents" with "drawing" · the only paper
                    visible is a single section drawing — distinct from
                    Fiscus's tax-document detail and from Continua's wax-
                    seal letterhead
    pexels_search:  "architectural drawing section ink parchment close-up"
                    backup: "compass trace paper architectural drafting macro"
    feasibility:    CAUTION (4-8 candidates · §3 quick-check CAUTION)
    rejection_rules_for_curator:
                    REJECT: any tax document · invoice · contract paper-
                            stack · printed report (Fiscus adjacency)
                    REJECT: blueprint at angle on a desk with multiple
                            sheets and tools — too cluttered, becomes
                            workshop-task framing not detail-craft
                    BIND:   single sheet · single drawing · single tool ·
                            macro distance — the detail must read as a
                            STILL LIFE not as a desk-in-progress
    fallback_subject: brass architect's compass at macro distance on trace
                      paper · feasibility ~6-10 candidates · curator
                      authorised to take this route at A.3 entry without
                      re-spec if the section-drawing pool returns ≤4

  slot_5_ambient:
    subject:        studio-interior at low natural light · drafting boards
                    visible · pin-up wall with sketches and site-photographs ·
                    NO people · NOT bookshelf (Fiscus reservation) · NOT
                    atrium (Pragma) · NOT slate-stairwell (Continua's
                    adjacency-but-acceptable) · NOT bright-meeting-room
                    (Solaria)
    mood:           studio-as-evidence · architectural-design-room · the
                    place where editorial work happens
    why_not_bookshelf: Fiscus owns bookshelf as ambient · CS-IMG-SRC-04
                    cross-cluster distinct subject
    pexels_search:  "architecture studio drafting boards pin-up wall sketches"
                    backup: "architect office sketches walls drafting"
    feasibility:    GO (5-10 candidates)
    rejection_rules_for_curator:
                    REJECT: any laptop / monitor on a desk in foreground ·
                            any cosy-interior with wood tones (Continua
                            adjacency) · any modern open-plan office
                            (reads SaaS not editorial-architectural)
                    BIND:   pin-up wall OR drafting-table OR both must be
                            visibly part of the framing

  imagery_distinctness:
    vs_pragma:
      - hero is exterior architectural · Pragma's is 4-person boardroom
      - feature is hand-craft model · Pragma's feature is corporate atrium
      - ambient is studio-with-pin-ups · Pragma's ambient is industrial conference
      - portrait is environmental architect · Pragma is typographic-only
      - mood is editorial-golden-hour · Pragma is daylight-cool
      - subject density is 0 (hero) then 1 (single portrait) · Pragma is 1-4

    vs_fiscus:
      - hero is built-form · Fiscus is desk-with-documents
      - feature is scale-model + drafting · Fiscus is tax-document close-up
      - ambient is design-studio · Fiscus's ambient is law-bookshelf (banned overlap)
      - portrait is environmental architect · Fiscus has typographic-only
      - mood is editorial · Fiscus is institutional-fiscal-task

    vs_solaria:
      - hero is exterior architectural · Solaria is 1:1 conversation
      - hero is golden-hour-stone · Solaria is cool-bright meeting room
      - feature is craft-model · Solaria's feature is man-writing-in-notebook
      - portrait is 50s environmental · Solaria is 30s × 2 (the residual gap)
      - ambient is studio-craft · Solaria's ambient is warm-home-office-with-plants

    vs_continua:
      - hero is exterior at golden hour · Continua is interior reading-room
      - hero is stone-and-concrete material · Continua is mahogany-and-leather
      - hero is architectural-shadow-line cinematic · Continua is contemplative-warm
      - feature is hand-craft model · Continua's is desk close-up with ledger
      - ambient is design-studio with sketches · Continua's is slate-stairwell
      - portrait is single 50s environmental · Continua is 60s + 40s pair
      - detail is ink-on-parchment drawing · Continua's is wax-seal letterhead
      - mood is editorial-curatorial · Continua's is custodial-stewardship

  cross_cluster_grep_clean:    YES (intent · curator confirms at A.3 BEFORE committing URLs)
                               grep targets: business-corporate · business-fiscal ·
                                             business-coaching · business-stewardship
```

### Pool-to-page wiring (CS-IMG-POOL-02)

| Page | Imagery presence | Slot sources |
|---|---|---|
| `home.html` | hero photo (1) + single-portrait (1) + magazine-grid case cards (4) + sectors-ribbon visuals (text-ribbon, no photos) | slot 0 · slot 2 · slots 4 / 5 / extras × 4 |
| `about.html` | feature/history shot (1) + team-grid portraits (2-3) | slot 1 · slot 2 + slot 3a (collaboratore) or extras |
| `services.html` | feature or ambient shot (1) + process-strip icon set (line-stroke rust on cream) | slot 1 or slot 5 |
| `case_study_list.html` | 1 card thumbnail per case (3-6) | slots 4 / 5 + pack extras rotated |
| `case_study_detail.html` | hero-scale case photo (1) + body-embedded detail (1-2) + site-context slot (1) | slot 0 variant or pack extras · slot 4 · slot 5 OR slot 3b project-interior |
| `contact.html` | ambient studio photo (1) + optional map tile | slot 5 |

CS-IMG-POOL-02 minimum-distribution check: home shows ≥3 photographic surfaces (hero + portrait + ≥1 case-card) ✓.

---

## 5 · Typography DNA

| Surface | Specification |
|---|---|
| **h1 hero** | Cormorant Garamond 64px / line-height 1.06 / weight 500 / italic on `argomento` only |
| **h2 section** | Cormorant Garamond 40px / line-height 1.14 / weight 500 / italic only on em-word |
| **h3 card / pull-quote** | Cormorant Garamond 28px / line-height 1.22 / weight 500 |
| **drop-cap (narrative essay opener)** | Cormorant Garamond 84px / weight 500 / colour `--accent` (rust) — LF-2 editorial signature |
| **eyebrow / label** | Source Sans 3 12px / uppercase / letter-spacing 0.22em / weight 600 (RTL resets letter-spacing to 0 — CS-TYPE-05) |
| **body** | Source Sans 3 17px / line-height 1.65 / weight 400 / tracking 0 |
| **pull-quote text** | Cormorant Garamond italic 22px / line-height 1.36 / weight 400 — italic em-word in rust on cream |
| **CTA label** | Source Sans 3 15px / weight 600 / letter-spacing 0.04em |
| **`.num` KPI (in hero credit overlay only)** | Cormorant Garamond 32px / weight 500 / `font-variant-numeric: tabular-nums` (CS-TYPE-03) — display-serif on photo |
| **case-card numerals (magazine-grid)** | Cormorant Garamond 24px / weight 500 / italic / colour rust |
| **AR heading** | swap to Noto Naskh Arabic via `html[dir="rtl"]` (decision at C pre-flight) — Cormorant Latin wordmark preserved (CS-NAV-06 / CS-FOOT-03) |
| **AR body** | swap to Amiri |

**Why Cormorant Garamond vs the alternatives**: Cormorant Garamond's display-elegant proportions + classical italic + strong weight contrast carry the editorial-curatorial register without the newspaper-flavor (Pragma's Merriweather), the document-pair stiffness (Fiscus's Plex Serif), the warm humanist contemporary feel (Solaria's Fraunces), or the long-form book-jacket gravity (Continua's Crimson Pro). It reads "architectural monograph display." Italic personality is strong enough that the curatorial-noun italic emphasis lands at h1 64px and at drop-cap 84px without colour or weight assistance.

**Why Source Sans 3 body**: matrix §1.4 calls Inter "taken twice — third use collapses the cluster." Source Sans 3 is editorial-clean, slightly-humanist, neither geometric nor neo-grotesque, pairs cleanly with Cormorant and explicitly closes the §1.4 collapse risk. It is NOT Inter, NOT Plex Sans, NOT Public Sans (Continua already took Public Sans).

**Drop-cap rationale**: LF-2's L4 narrative essay calls for editorial display devices. The drop-cap on the first paragraph of the narrative essay is the family's typographic signature — present in LF-2, absent in LF-1/3/4/5. This is one of the visible LF-2 differentiators per §6 below.

---

## 6 · Section sequence · home page (LF-2 sequence B)

A practical beat sheet, not a wireframe novel. Word counts target the upper-band targeting from `prebuild-quick-checks.md §4` (~1450 total · LF-2 narrative carries the body weight).

| # | Section | Beat purpose | Concrete content (IT) | Word target |
|---|---|---|---|---|
| 1 | `hero` LF-2 stacked-editorial | Position + voice anchor + first proof tuple | photo TOP (full-bleed) · credit overlay bottom-left of photo with 3 inline stats `47 — Progetti realizzati / 18 — Anni di pratica / 6 — Città italiane` (KPI in overlay, L5=hero-overlay) · BELOW photo: 8/4 split · LEFT 8-col h1 voice anchor (italic on `argomento`) + 1-line subhead "Studio di architettura editoriale · Milano · committenze pubbliche e private dal 2008." · primary CTA "Apri un fascicolo progetto" (outline-on-cream) · RIGHT 4-col side-quote "L'architettura buona si argomenta — non si dimostra, non si vende, non si decora." | 60 |
| 2 | `narrative` LF-2 essay-with-anchors | Editorial position-statement · the firm's argument about its own work | 4-paragraph essay · drop-cap on para 1 (rust Cormorant 84px) · 2-3 pull-quotes interspersed · side-rail of anchor-links to /studio/, /servizi/, /progetti/, /contatti/. Para 1 ~120w (the firm's editorial position) · Para 2 ~130w (process: rilievo → contesto → argomento → cantiere) · Para 3 ~130w (commissions and the studio's view of authorship) · Para 4 ~110w (continuity into the case-studies preview below) · 3 pull-quotes × ~20w | 600 |
| 3 | `sectors-ribbon` | Project-typology ribbon (no photos, sentence-shape) | label "Tipologie d'intervento" · 10-12 segments separated by middot: residenziale · pubblico · interno · paesaggio · restauro · concorso · culturale · uffici · industriale · sanitario · scolastico · misto-uso | 144 |
| 4 | `leadership-single` LF-2 single-portrait-feature | The founding architect masthead | LARGE portrait (slot_2 · 50s environmental) · h2 name + role-eyebrow ("Studio Founder · Architetto") · 2-paragraph bio (~110w each) · credentials list: Albo Architetti P.P.C. (OAPPC) · Ordine Architetti Milano · CNAPPC · MIBAC restauro qualifica · NOT a 3-4 card grid · NOT typographic-only · the SINGLE portrait carries the whole leadership read | 240 |
| 5 | `cases-magazine-grid` LF-2 L7 | "Progetti — argomenti costruiti" · 3+1 magazine grid | 1 hero card (large, photo-dominant, ~130w copy: project-name · year · committenza · tipologia · 3-line argument-of-the-project) + 3 small cards (~75w each: project-name · year · 1-line argument). Each card carries a photo (slot_4 / slot_5 / slot_3b / pack extras). NOT list-row · NOT timeline. | 360 |
| 6 | `cta-closer-cream` | Restates voice anchor + final CTA | CREAM band (NOT dark — LF-2 family rule) · hairline graphite border top + bottom · centred copy · larger Cormorant h2 restating voice anchor verbatim · single filled-rust CTA "Apri un fascicolo progetto" · single-line form-gate hint ("Brief in italiano · risposta entro 5 giorni lavorativi") | 65 |

**Total**: ~1469 words rendered + chrome overhead → ~1450 final estimate. Inside the LF-2-adjusted floor (see prebuild-quick-checks.md §4 for the LF-2 family-floor calibration).

### Anti-pattern guards baked in

- **CS-RHYTHM-04** (no two adjacent sections share function): hero (position) → narrative (essay) → sectors-ribbon (typology-list) → leadership-single (single-portrait) → cases-magazine-grid (case studies) → cta-closer (closer) — every adjacent pair is functionally distinct. Style-critic at A.6 verifies.
- **CS-DENSITY-02 / CS-DENSITY-04**: pillars 0 (LF-2 has none), KPI 3 (in hero overlay only), cases 4 (within bands).
- **CS-PAL-05**: hero CTA + nav CTA + closer CTA = 3 across the home, never 3 in a single viewport (≤3 accent hits per viewport invariant preserved).
- **CS-COMP-06** (no wall-of-text opener): home opens with the LF-2 stacked-editorial hero, not with a "Our Story" essay; about.html opens with a feature-shot-and-narrative-band, not with text-only.
- **CS-TONE-03** (one dark band on home): demoted at family level — LF-2 declares zero dark bands. KPI lives in hero overlay; CTA closer is cream-with-hairline-border. The demotion is recorded in §2 above and re-stated in `intake.md §4 cluster_invariants_demoted_at_family_level`.

---

## 7 · Navbar · footer direction

### Navbar (`split-wordmark-cornice` · LF-2 L8=split-wordmark-top)

- Sticky · `background: var(--paper)` (cream — LF-2 deviation from CS-NAV-01 sticky-top-primary-bg) · graphite link text · DECISION-LOCKED at A.5 entry. RATIONALE: LF-2 declares split-wordmark-top + the family's chrome reads as editorial-publication-masthead, not boardroom-dark-bar. The cluster's sticky-top-primary-bg invariant (CS-NAV-01) is demoted at family level per divergence plan §3.
- **Wordmark**: split-line · line 1 "**CORNICE**" (Cormorant Garamond 22px weight 600 graphite uppercase letter-spacing 0.18em) · line 2 "studio di architettura" (Source Sans 3 11px weight 400 graphite lowercase letter-spacing 0.04em) — like a publication masthead
- 5 links: `Studio · Servizi · Progetti · Pubblicazioni · Contatti` (5 = cluster default · "Pubblicazioni" is the family-specific link variant — Cornice writes about its own work)
- Trailing accent CTA: `"Apri un fascicolo progetto"` · solid rust `#B7491F` on cream · the chrome's only filled element (rust touchpoint #1)
- Locale switcher: pill with `lang` + `dir` per link · sits between last nav item and CTA · CS-NAV-03
- `:focus-visible` rust ring (2px outline · 4px offset) · CS-NAV-02 · the cluster's signature interactive moment (rust touchpoint #2)
- 4 link states (default / hover / focus / active) · all distinct · hover = 1px rust underline · active = rust label
- Mobile (≤880px): hamburger drawer · CSS-only · cluster pattern (corporate-suite skin already carries this)

### Footer (`four-col-cornice` · LF-2 L9=4-col-with-whistleblowing)

- 4 columns on `--primary` background (graphite · LF-2 keeps primary-bg footer per divergence plan §3 · only L9 column count changes from 3 to 4) · cream type
- **Col 1 brand**: split-wordmark + 1-line studio one-liner · "Architettura editoriale · committenze pubbliche e private · Milano dal 2008."
- **Col 2 sitemap**: 5 nav links + 3 secondary (Studio · Pubblicazioni · Privacy · Cookie · Whistleblowing)
- **Col 3 contact**: studio address (Milano · via [TBD]) · email (`fascicolo@cornice-architettura.it`) · phone · studio-hours note ("Studio aperto su appuntamento · martedì–venerdì 10–18")
- **Col 4 disclosures-with-whistleblowing**: P.IVA · Albo OAPPC iscrizione N° [TBD] · CNAPPC · MIBAC qualifica restauro · whistleblowing channel link prominent (D.lgs. 24/2023 · CS-FOOT-02 · the LF-2 family elevates whistleblowing to a column-level surface, NOT a footnote)
- Footer stacks to 1 column at ≤720px (CS-FOOT-05 · cluster R2 fault line · MUST be added BEFORE first build, not deferred)
- Latin wordmark + Latin numerics preserved under RTL · CS-FOOT-03

### Rust touchpoint inventory (Mitigation §10 Warning 1)

The rust accent must appear at ≥ 5 viewport touchpoints to land as the cluster's only NEUTRAL-anchored polarity differentiator. The build commits to 6, deployed across CHROME and DISPLAY surface classes — explicitly distinct from Continua's brass which lives only in chrome:

CHROME surfaces (2):
1. Trailing nav CTA (solid rust on cream)
2. `:focus-visible` ring on every interactive element (2px rust outline)

DISPLAY surfaces (4 · LF-2-specific · this is what differentiates from Continua's brass deployment):
3. Drop-cap on narrative essay paragraph 1 (Cormorant 84px rust)
4. Pull-quote em-word colour in narrative-essay pull-quotes (rust on cream)
5. Magazine-grid case-card numerals (rust italic Cormorant)
6. cta-closer-cream filled-rust button (the closer band's only colored element)

Style-critic at A.6 confirms the 6 touchpoints render at 1920 first scroll AND that the chrome-vs-display surface separation is visible. Walk at A.7 confirms at 1280 + 720 the rust is still visibly distinct from cream + graphite both, AND that the rust deployment differs in surface class from Continua's brass (which is chrome-only).

---

## 8 · Proof style

**Rendering principle**: editorial case-publication over numeric KPI alone. The studio publishes its work; cases ARE the proof.

| Surface | Concrete shape |
|---|---|
| Hero credit overlay (KPI in overlay · L5=hero-overlay) | 3 inline stats: `47 — Progetti realizzati / 18 — Anni di pratica / 6 — Città italiane` (cream type on photo · NOT a separate dark band · NOT pure numeric brag like Pragma's "22 anni · 180+ mandati · €1.4 B") |
| Sectors ribbon | "Tipologie d'intervento" labelled segments (NOT "Settori" generic — names the WORK as typology, not the audience as industry) |
| Leadership card | name + role-eyebrow + 2-paragraph bio + 4 real albo credentials (OAPPC / Ordine Milano / CNAPPC / MIBAC) — single-portrait-feature (LF-2 L6) |
| Cases magazine-grid | "Progetti — argomenti costruiti" · 3+1 grid · each card carries photo + project-name + year + committenza + tipologia + 1-line argument-of-the-project — public-record proof shape (real architecture commissions are publishable, anonymisation not required) |
| Case detail page | adds a `site-context` slot mirroring Solaria's `method-context` precedent — slot shows site address (or anonymised regional) + intervention scope + year span + brief (≥150w) editorial argument-of-the-project. Detail-page order: hero-photo + narrative-argument + `site-context` + drawings-strip + next-project. |
| Trust band | NOT used (LF-2 has no cs-trust marquee · sectors-ribbon covers the role) |

**What this avoids**: numeric-only KPI inflation that reads as B2B-advisory chest-thump. The proof shape carries authorship and editorial argument, not magnitude. The 47/18/6 hero-overlay numbers are footnotes to the work, not the headline.

---

## 9 · CTA personality

**Primary CTA copy**: `"Apri un fascicolo progetto"`

### Polarity rules (CS-CTA-01 · cluster ratification 2026-04-26 · do not re-litigate)

- On cream paper: outline-only · graphite border · graphite label · rust on `:focus-visible`
- In the cream-hairline CTA-closer band: filled rust on cream background · the polarity is INVERTED from the cluster's filled-on-dark precedent because LF-2 has NO dark band — but the closer band's hairline graphite border + filled-rust button retains the "this is the one moment to push" signature. This is the LF-2-specific polarity inversion (recorded for the style-critic).
- Hover on cream: 4px rust underline grows from baseline (NOT a fill swap on cream)
- Hover on filled-rust closer button: rust deepens 8% via `filter: brightness(0.92)` (NOT a colour change)

### Form gate (`/contatti/`)

Project-brief shape · 4 fields:
1. **Sito** (textarea · placeholder: "Ci dica brevemente la localizzazione, la tipologia e l'intervento immaginato.")
2. **Tipologia** (select · residenziale / pubblico / interno / paesaggio / restauro / concorso / culturale / misto)
3. **Cronoprogramma desiderato** (select · <12 mesi / 12-24 / 24-36 / >36)
4. **Documenti già disponibili** (multi-select · rilievo / planimetria / vincoli / regolamento edilizio / bandi / concept iniziale / altro)

NO P.IVA + CF (Fiscus collision). NO ICF code-of-ethics referenced (Solaria's). NO NDA-ready boardroom form (Pragma's). NO scope+orizzonte+struttura (Continua's). The documents-multi-select is the differentiating field.

### CTA copy banlist respected

- NOT "Get started free" · NOT "Sign up now" · NOT "Iscriviti gratis" (CS-CTA-02)
- NOT "Fissa una call privata" (Pragma)
- NOT "Primo appuntamento" (Fiscus)
- NOT "Prenota una discovery call" (Solaria)
- NOT "Avvia un dialogo di mandato" (Continua)

---

## 10 · Leadership feel

```
leadership_block:
  presence:                  PHOTO-PRESENT (LF-2 L6=single-portrait-feature)
  card_count:                1   # SINGLE portrait masthead · NOT a card grid
  composition:               LARGE environmental portrait (slot_2) + h2(name) +
                             role-eyebrow + 2-paragraph bio + 4-credential list

  founding_architect:
    name_placeholder:        [TBD at A.4 — placeholder "Arch. Marco Roveri"]
    role_eyebrow:            "Studio Founder · Architetto"
    credentials:             "Albo OAPPC · Iscritto Ordine Architetti Milano N° [TBD]
                              · CNAPPC · MIBAC qualifica restauro architettonico"
    visible_demographic:     50s · neutral · environmental at studio window
    portrait_slot:           slot_2 (50s environmental · drafting tools mid-ground)
    bio_target_words:        220   # 2 paragraphs × ~110w · architectural authorship
                                   # warrants longer principal bio than typical
                                   # advisory-firm partner card
```

**Mitigation binding** (intake §12 Warning 4): the SINGLE portrait must read environmental, not headshot. Curator at A.3 hard-rejects any portrait that fails the binding triple: 50s + drafting-tools-or-sketches-visible + neutral environmental background (NOT studio-backdrop).

**Why single-portrait-feature**: LF-2 declares L6=single-portrait-feature. The cluster's first single-portrait shape. Solaria's photo-present precedent established that faces work for this cluster; LF-2 takes that forward but with ONE face that carries the whole authorship — appropriate for a single-principal architecture studio where the founder's editorial voice IS the proposition. Multi-partner card grid would dilute the single-author argument.

**Demographic anti-collision**: Cornice's portrait must NOT read as 30s × 2 (Solaria's residual gap) NOR as 60s + 40s pair (Continua's pattern). LF-2 has only ONE portrait, so the demographic anti-collision is entirely about how the SINGLE chosen subject reads. 50s + craft-context is the binding choice.

---

## 11 · Multilingual intent

```
multilingual_intent:
  initial_locale:                 it
  planned_locales:                [it, en, fr, es, ar]
  rtl_required:                   YES

  voice_anchor_strategy:
    it_anchor:    "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."
    em_word:      argomento
    translation_note: "Italic carries the curatorial-architectural noun (a project's
                      KIND, not its action). Translators MUST italicise the equivalent
                      of argomento:
                        EN: argument · FR: argument · ES: argumento ·
                        AR: حُجَّة (italic-substitute via Naskh-italic OR Kufi
                            weight-shift — decision at C pre-flight)
                      Do NOT italicise è / construit / built / construido / es."
    contrast_pair_anchor:    NO

  side_quote_strategy:
    it_side_quote: "L'architettura buona si argomenta — non si dimostra, non si vende, non si decora."
    translation_note: "Side-quote is NOT verbatim across locales · it carries the
                       voice-anchor's argument frame · per-locale rewrite is
                       authorised at A.4 copy-translation entry · the constraint
                       is that the rewrite must contain the locale's translation
                       of 'si argomenta' as the active verb."

  drop_cap_strategy:
    drop_cap_letter:         first letter of narrative essay paragraph 1 · per-locale
                             (e.g. IT 'L' of 'L'architettura...' · EN 'G' of 'Good
                             architecture...' · per-translator binding to keep the
                             paragraph's first letter visually grounding)
    drop_cap_size:           Cormorant 84px weight 500 colour rust (drops 3 lines)
    drop_cap_under_rtl:      mirror via logical props · drop-cap floats to inline-end
                             of paragraph in RTL

  terminology_locked_pre_translation:
    cluster_terminology_file:     factory/standards/corporate-suite-design-standard.md §11
    credentials_per_locale:       ["Albo Architetti P.P.C. (OAPPC)",
                                   "Ordine Architetti Milano",
                                   "CNAPPC",
                                   "MIBAC qualifica restauro"]
    legal_row_per_locale:         [P.IVA, privacy, cookie, whistleblowing]

  ar_specific_requirements:
    heading_font_swap:            "Noto Naskh Arabic" (LF-2-specific decision at C
                                  pre-flight · cluster default is Kufi · LF-2's
                                  editorial register favours Naskh humanist italics
                                  for the curatorial display) — § decision required
                                  at C entry; IT pass does not require it resolved
    body_font_swap:               "Amiri"
    latin_wordmark_preserved:     YES
    letter_spacing_reset:         YES
    rtl_layout_via_logical_props: YES
    hero_8_4_split_under_rtl:     mirror via logical props · side-quote column flips
                                  from inline-end to inline-start under dir=rtl —
                                  verify at C walk

  per_locale_form_options:
    tipologia_select:
      IT:   ["residenziale", "pubblico", "interno", "paesaggio", "restauro", "concorso", "culturale", "misto"]
      EN:   ["residential", "public", "interior", "landscape", "restoration", "competition", "cultural", "mixed-use"]
      FR:   ["résidentiel", "public", "intérieur", "paysage", "restauration", "concours", "culturel", "mixte"]
      ES:   ["residencial", "público", "interior", "paisaje", "restauración", "concurso", "cultural", "mixto"]
      AR:   ["سكني", "عام", "داخلي", "مشهد طبيعي", "ترميم", "مسابقة", "ثقافي", "متعدد الاستخدامات"]
            # AR digit convention for tipologia is text only · no numerals issue
```

The IT pass at workflow A does NOT depend on AR Naskh-vs-Kufi resolution. AR-font decision lands at workflow C pre-flight; IT walk passes regardless.

---

## 12 · Anti-clone constraints (binding for build agent)

The build agent at A.5 reads this list before writing the first line of the skin. Each line is enforced by either a rule ID, a style-critic check at A.6, or a walk check at A.7.

### Tone / voice anchor
- ✗ Pragma's "decisional gravity" framing
- ✗ Fiscus's "presidio + scadenze-first" framing
- ✗ Solaria's "non-terapia non-consulenza" bounded-method framing
- ✗ Continua's "stewardship-longitudinal · custodial multi-gen" framing
- ✗ Two em-wraps in any heading

### Palette
- ✗ Slate-blue + emerald family (Pragma)
- ✗ Warm-neutral + gold + blu-notte family (Fiscus)
- ✗ Warm-carbon + ocra + caramel family (Solaria)
- ✗ Pine + pewter + brass family (Continua)
- ✗ Bright pure red/orange/yellow at full saturation
- ✗ `--primary-2: #2c3e6b` hardcoded (CS-PAL-03)

### Typography
- ✗ Inter as body sans (third use collapses cluster — hard prohibition)
- ✗ IBM Plex Sans body
- ✗ Public Sans body (Continua)
- ✗ Merriweather, IBM Plex Serif, Fraunces, Crimson Pro as heading
- ✗ Montserrat, Poppins, Raleway on headings (CS-TYPE-01)

### Hero composition
- ✗ 55/45 split hero (LF-2 declares stacked-editorial · CS-HERO-01 demoted)
- ✗ Object-overlay hero (LF-5 / Continua)
- ✗ Pragma's KPI tuple as a SEPARATE meta-strip
- ✗ Fiscus's fiscal-calendar-strip
- ✗ Solaria's percorso-cadenza-strip
- ✗ Continua's stewardship-horizon-strip
- ✗ `(Direzione, Anno fondazione)` as the hero credit overlay (used twice)
- ✗ Any hero photo with > 0 documents, > 0 laptops, > 0 humans

### Imagery
- ✗ Boardroom long-table hero (Pragma)
- ✗ Tidy desk + documents hero (Fiscus)
- ✗ 1:1 conversation hero (Solaria)
- ✗ Library / partner-study reading-room hero (Continua adjacency)
- ✗ Bookshelf as ambient (Fiscus)
- ✗ Slate-stairwell as ambient (Continua adjacency)
- ✗ 30s × 2 portrait demographic (Solaria gap)
- ✗ 60s + 40s pair portrait (Continua's pattern · LF-5-only)
- ✗ Any URL appearing in `business-corporate`, `business-fiscal`, `business-coaching`, `business-stewardship` (cross-cluster grep · CS-IMG-SRC-04)
- ✗ Any pure-white-backdrop LinkedIn-headshot for the single portrait

### CTA
- ✗ "Fissa una call privata" / "Primo appuntamento" / "Prenota una discovery call" / "Avvia un dialogo di mandato"
- ✗ "Get started free" / "Sign up now" / "Iscriviti gratis"
- ✗ A form gate asking for both P.IVA + CF (Fiscus's intake)

### Section rhythm
- ✗ Pragma's exact section order (no mid-strip + leadership present + KPI band-at-3)
- ✗ Fiscus's `fiscal-calendar` mid-strip
- ✗ Solaria's `manifesto` opener replacing pillars (LF-2 replaces pillars with essay-with-anchors, not manifesto)
- ✗ Continua's slot-2 governance-cycle promotion
- ✗ Any cs-pillars block (LF-2 has none — declared)
- ✗ Any separate cs-kpi-band (LF-2 KPI is in hero overlay)
- ✗ Any cs-cycle mid-strip (LF-2 L3=absent)
- ✗ Any list-row cases (LF-2 L7=magazine-grid)
- ✗ Any timeline cases (Continua's L7)
- ✗ A wall-of-text "Our Story" opener (CS-COMP-06)

### Leadership / proof
- ✗ Pragma / Fiscus / Solaria / Continua credential vocabularies verbatim
- ✗ Any fake credential (CS-EXEC-03)
- ✗ "Casi seguiti" / "Casi anonimizzati" / "Case studies" without fresh framing
- ✗ Solaria's "Aziende sponsor recenti" trust-band label
- ✗ Continua's "Riconoscimenti istituzionali" trust-band label
- ✗ Multi-card leadership grid (LF-2 declares single-portrait-feature)

### AI-slop tells (CS reference-pack §9)
- ✗ Inter on h1
- ✗ Purple gradient
- ✗ Cards-in-cards
- ✗ Gray on colored bg
- ✗ Three accent buttons in hero
- ✗ Emoji in body or headings
- ✗ Backdrop blur
- ✗ Celebrity quotes
- ✗ Mountain-peak hero
- ✗ "Trusted by 10,000+" claims
- ✗ "Made with Marketweb" footer

---

## 13 · Browser-live expectations (precis · full plan to be filed at A.5 entry)

The IT walk at A.7 produces:
- 6 pages × 6 viewports = **36 captures** at `factory/reports/browser-verification/cornice-architettura/it/<YYYY-MM-DD>/`
- Plus 1 reduced-motion capture
- Plus a contrast report at all 6 viewports
- Plus a responsive report at all 6 viewports
- Plus a style-critic report against `corporate-suite-design-standard.md` (with LF-2 family-level demotions explicitly handled)
- Plus 3 LF-2-specific layout-gate captures: B-LAYOUT-1 wireframe overlay vs Pragma/Fiscus/Solaria/Continua · B-LAYOUT-2 DOM section-list compare · B-LAYOUT-3 L1–L9 classification

**The walk verdict at A.7 must read PASS** (or BORDERLINE → A.8 narrow fix → re-walk) before Commit A draft-landing.

**The 5 mitigations from intake §12 must be verified live**:
1. Rust accent visible at ≥ 6 touchpoints across CHROME (2) + DISPLAY (4) surface classes at 1920 first scroll · also visible at 1280 and 720 contrast walks · surface deployment differs from Continua's brass-only-in-chrome
2. Hero photo passes object-led + zero-people + exterior-architectural filter at 1280 + 1024 crops · does NOT crop into interior-warm
3. "Remove the studio name" test passes on the live render (CS-TONE-05 · master §5.12)
4. Single portrait reads ENVIRONMENTAL not HEADSHOT at 1920 / 1280 / 768
5. Zero dark band on home is RENDERED zero (KPI in overlay verified · CTA closer cream verified) — B-LAYOUT-3 records L5=hero-overlay

**LF-2-specific layout-gate verifications** (B-LAYOUT-1/2/3 per divergence plan §8):
- B-LAYOUT-1 wireframe overlay shows ≥30% bounding-box variance vs each of Pragma/Fiscus/Solaria/Continua
- B-LAYOUT-2 section-list compare: Cornice's `[hero, narrative, sectors-ribbon, leadership-single, cases-magazine-grid, cta-closer-cream]` differs from every existing sibling's section list by ≥2 entries
- B-LAYOUT-3 classification matches the planner-declared LF-2 row (L1=stacked-editorial · L2=B · L3=absent · L4=essay-with-anchors · L5=hero-overlay · L6=single-portrait-feature · L7=magazine-grid · L8=split-wordmark-top · L9=4-col-with-whistleblowing)

Workflow C (5 locales · ~35 walk cells) gates the LIVE flip via `release-decision-orchestrator.md`. IT-only Commit A is the workflow A endpoint.

---

## 14 · Release-gate expectations

The release-gatekeeper at A.9 reads these. Tier flip from `draft` to `published_live` is a SEPARATE pass and binds on:

- Scorecard ≥ 4.50/5 (4.67/5 is precedent)
- 0 open `[BLOCKING]` findings
- IT walk PASS · 4 locale walks PASS (EN/FR/ES/AR via workflow C) · AR RTL parity walk PASS
- B-LAYOUT-1/2/3 PASS at IT walk (this is the new gate the LF-2 enrolment validates)
- User-handshake binary SHIP recorded
- Live DOM still matches this brief at flip time
- Pexels-only re-confirmed on live render across all 5 locales
- Distinctness re-confirmed ≥ 4/5 vs every sibling at flip time
- All walk verdicts ≤ 30 days fresh

---

## 15 · The single-page summary the orchestrator reads at sign-off

```
PLAN SIGN-OFF SUMMARY · cornice-architettura
=============================================

What this template is:
    A single-principal architecture studio that publishes its
    projects as case-led editorial — each commission a built
    argument, catalogued and annotated, not sold as a service.

What this template is NOT:
    NOT Pragma's boardroom-advisory mandate (B2B not architecture).
    NOT Fiscus's commercialista presidio (tax not building).
    NOT Solaria's bounded executive coaching (personal not firm-of-architects).
    NOT Continua's stewardship-grade family office (custodial not authorial).

Layout family:                   LF-2 · Editorial Spread (1st LF-2 occupant · 5th cluster sibling)

Voice anchor (IT · verbatim · with <em>):
    "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."

Palette: primary #1F2226 (graphite) · secondary #C7BFB1 (pietra-serena) · accent #B7491F (terracotta-rust)
Macro tone: graphite + pietra-serena + terracotta-rust · NEUTRAL/NEUTRAL/WARM (the only un-claimed cluster polarity)

Typography: Cormorant Garamond + Source Sans 3

Hero (LF-2 stacked-editorial · NOT 55/45):
    full-bleed photo TOP (built courtyard / portico at golden hour · zero people)
    + credit overlay with 3 inline stats (47 — Progetti / 18 — Anni / 6 — Città)
    + 8/4 split BELOW (h1 LEFT + side-quote RIGHT)

CTA: "Apri un fascicolo progetto" → project-dossier-submission (brief-upload framing)

Section moves that distinguish this from siblings:
  1. LF-2 stacked-editorial hero (cluster's first non-55/45 hero) — closes
     the silhouette gap the family-matrix recorded
  2. Zero dark band on home (LF-2 declares L5=hero-overlay; KPI lives in
     the photo's overlay, no separate cs-kpi-band) — declared family-level
     demotion of CS-TONE-03
  3. Narrative essay with drop-cap + pull-quotes + side-rail anchors
     replaces pillars (LF-2 L4=essay-with-anchors) — editorial-display
     signature
  4. Single-portrait masthead (LF-2 L6=single-portrait-feature) — cluster's
     first single-portrait shape
  5. Magazine-grid 3+1 cases (LF-2 L7=magazine-grid) — cluster's first
     magazine-grid · differs from list-row (Pragma/Fiscus/Solaria) and
     from timeline (Continua)
  6. Split-wordmark masthead navbar (LF-2 L8=split-wordmark-top) on cream
     background (LF-2 family demotes CS-NAV-01 sticky-top-primary-bg)
  7. 4-col footer with whistleblowing column (LF-2 L9=4-col-with-whistleblowing)
     — cluster's second 4-col footer (Continua's was the first; the column
     content differs — Cornice's 4th col is disclosures-with-whistleblowing)

Distinctness scores (5-axis matrix):
  vs Pragma:   5/5
  vs Fiscus:   5/5
  vs Solaria:  5/5
  vs Continua: 5/5
  GATE:        PASS

Layout-distinctness scores (9-dim L1–L9 tuple · CS-LAYOUT-12 ≥4/9 gate):
  vs Pragma (LF-1):    9/9 different
  vs Fiscus (LF-3):    9/9 different
  vs Solaria (LF-4):   8/9 different (only L3 same · both `absent`)
  vs Continua (LF-5):  8/9 different (only L9 same · both `4-col-with-whistleblowing`,
                       though column-content differs — disclosures-vs-offices)
  GATE:                PASS (well above CS-LAYOUT-12 ≥4/9 threshold on every pair)

Imagery pack: business-architecture · curator-approved at A.3 · 6 URLs Pexels-only
              + 4 case-card URLs from pack extras (LF-2 magazine-grid needs 4 case photos)

Initial locale: it (others at workflow C)
Initial tier: draft

Browser walk plan: 6 viewports × 1 locale (it) × 6 pages = 36 captures
                   + 1 reduced-motion + 3 LF-2-specific layout gates (B-LAYOUT-1/2/3)
Walk artefact dir: factory/reports/browser-verification/cornice-architettura/it/<YYYY-MM-DD>/

Scorecard expected grade: ≥ 4.50/5

Open questions for orchestrator:
  - Cormorant Garamond vs Spectral fallback decision at A.5 build entry (not a re-spec)
  - AR Naskh-vs-Kufi heading-font choice for LF-2 editorial register at C pre-flight (not blocking IT pass)
  - `_layouts/lf2/home.html` path placement vs inline conditional at A.5 build entry
```

The intake §3.2 studio-name swap test re-runs on this summary at A.2 sign-off per `prebuild-quick-checks.md §5`. If the swap collapses any line above into a generic, the brief returns for re-spec.

---

## 16 · What this brief is and is not

**This brief IS**:
- A complete, decision-locked planner-brief.
- Ready to hand to a workflow A.3 (curator) → A.4 (copy) → A.5 (build) chain with no re-spec.
- The contract the style-critic re-reads at A.6 and the walk-verifier re-reads at A.7.
- The first explicit LF-2 occupant brief, validating the layout-family system per divergence plan Step 6.

**This brief is NOT**:
- A real `template_dna.py` entry (the build at A.5 writes that).
- A real seed file (A.5 writes that).
- A curator-approved Pexels pack (A.3 produces that, with cross-cluster grep on file).
- A copy diff (A.4 produces that with the voice anchor verbatim).
- A critique or walk verdict (A.6 / A.7).
- A registry edit (registry stays untouched until Commit A).

If a real workflow A pass picks this up tomorrow, it routes to:
1. **A.3 imagery-curator** — with this §4 pack spec as input · runs cross-cluster grep BEFORE committing URLs against business-corporate / business-fiscal / business-coaching / business-stewardship pools · curator approval gate before A.4
2. **A.4 copy-translation** — with this §6 word-targets and §11 voice anchor + em-word as input · IT only · D-102 cadence
3. **A.5 template-builder** — with this §3 DNA + §6 section sequence + §7 nav/footer specs as input · introduces or extends the layout-family routing scaffold · CLI green + IT live URL openable
4. **A.6 critique** — three reports against the design standard, the contrast rules, the responsive matrix, and the LF-2 family row of `corporate-suite-layout-family-matrix.md §1`
5. **A.7 walk** — 6 pages × 6 viewports + B-LAYOUT-1/2/3, verdict per the LF-2-specific layout-gate plan
6. **A.9 aggregate** — scorecard, user-handshake, Commit A request

Gates between every step. No skipping. Paper-only at this Step 2 promotion — no code change yet.
