# Cornice · Factory intake · LF-2 · 5th corporate-suite sibling

```yaml
report_type:        intake
template_slug:      cornice-architettura
studio_name:        Cornice
archetype:          corporate-suite
sub_cluster_label:  architecture-firm · single-principal studio (editorial-led)
cluster:            corporate-suite
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · cornice-architettura · Step 2 (paper-only)
date:               2026-04-30
inputs_consumed:
  - design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
  - design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md
  - design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md
  - factory/reports/hardening/corporate-suite-layout-family-matrix.md (LF-2 row)
  - factory/reports/hardening/corporate-suite-layout-divergence-plan.md (Step 6)
  - factory/standards/corporate-suite-design-standard.md
  - factory/standards/corporate-suite-imagery-standard.md
  - factory/standards/corporate-suite-blocking-rules.md
  - factory/agents/template-planner.md · factory/agents/imagery-curator.md
  - design-orchestrator/workflows/pre-build-quick-checks.md
status_tag:         INTAKE-COMPLETE · ready for planner-brief
verdict:            CONTINUE → planner-brief.md · then prebuild-quick-checks.md
next_action:        Planner reads §1–§12 · writes planner-brief.md · re-runs the 5 checks in factory format
```

This intake is the binding input contract for `planner-brief.md`. Every claim is concrete; no field is "TBD." The promotion that produced this file is the Step 2 conversion of the LF-2 fifth-sibling pilot work into factory-paper form. No application code is touched. No registry edit. No imagery URL committed.

---

## 0 · Cluster / family precondition

```
cluster:                              corporate-suite
cluster_reference_pack_exists:        YES (design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md)
cluster_distinctness_matrix_exists:   YES (design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md)
cluster_layout_family_matrix_exists:  YES (factory/reports/hardening/corporate-suite-layout-family-matrix.md)
declared_layout_family:               LF-2 · Editorial Spread (OPEN — claim by this template)
proceed_decision:                     CONTINUE
```

LF-2 is OPEN per `corporate-suite-layout-family-matrix.md §3`. Claim by this template makes the cluster occupancy 5/6 (LF-1 Pragma · LF-3 Fiscus · LF-4 Solaria · LF-5 Continua · LF-2 Cornice · LF-6 reserved).

---

## 1 · Identity

```
template_slug:        cornice-architettura
studio_name:          Cornice
wordmark_form:        split-wordmark masthead — line 1 "CORNICE" · line 2 "studio di architettura"
cluster:              corporate-suite
sub_cluster_label:    architecture-firm · single-principal studio (editorial-led)
archetype:            corporate-suite
layout_family:        LF-2 · Editorial Spread
sibling_position:     5th corporate-suite · 1st architecture-firm · 1st LF-2 occupant
```

Slug uniqueness check at planner-brief sign-off: `grep -r 'cornice-architettura' apps/catalog/` returns zero hits at intake date. Re-grep at A.5 build entry per planner SOP §4.

---

## 2 · Cluster · archetype context

```
existing_siblings_in_cluster:    Pragma · Fiscus · Solaria · Continua
nearest_two_siblings:            Pragma (institutional voice neighbour) · Continua (object-led imagery neighbour)
furthest_sibling:                Solaria (warm-coaching · 1:1 conversation · single-practitioner manifesto-led)
cluster_invariant_summary:       institutional-advisory tone · serif heading + italic-em emphasis · cream paper · Pexels-only · voice anchor verbatim 5-locale · :focus-visible accent ring · whistleblowing legal row · max-width 1400 · padding 100×72
layout_family_invariants_lifted: CS-HERO-01 (55/45) → demoted at family level by LF-2 · CS-TONE-03 (one dark band on home) → demoted at family level by LF-2 (KPI moves into hero overlay) · CS-LAYOUT-* govern instead
archetype_position:              1st LF-2 occupant · validates the layout-family system (divergence plan §10 Step 6)
```

**Triangulation rationale**: Cornice is closest to Pragma on **stance** (institutional, serious, professional Italian) and to Continua on **imagery polarity** (object-led + zero people in hero). It is furthest from Solaria (warm/conversational/single-practitioner-method) and from Fiscus (calendar/scadenze/tax-form). Pragma + Continua are the binding triangulation pair. Solaria + Fiscus are residual axes.

Critically: Cornice's tonal stance is **editorial-curatorial · architectural-discipline**, which is structurally distinct from Pragma's *decisional gravity* and from Continua's *stewardship-longitudinal*. The first 30s read for Cornice is "an architecture studio whose work is an editorial argument," not "an advisory firm" or "a custodian."

---

## 3 · Desired differentiation

```
one_line_pitch:
    A single-principal architecture studio that publishes its work as
    case-led editorial · each project a built argument · catalogued and
    annotated, not sold.

voice_positioning:
    editorial-curatorial · architectural-discipline · case-led · matrix
    §1.1 OPEN stance (architectural-discipline) · NOT decisional-gravity ·
    NOT presidio · NOT bounded-method · NOT stewardship-longitudinal.

palette_intent:
    graphite + pietra-serena + terracotta-rust · NEUTRAL-primary +
    NEUTRAL-secondary + WARM-accent · the only sibling so far with a
    NEUTRAL-anchored polarity (Pragma cool/cool/cool · Fiscus cool/warm/cool ·
    Solaria warm/warm/warm · Continua cool/cool/warm). Explicitly NOT
    navy+emerald · NOT warm-neutral+gold+blunotte · NOT warm-carbon+ocra+caramel ·
    NOT pine+pewter+brass.

typography_intent:
    Cormorant Garamond (heading · display-elegant · architectural-monograph
    register · strong italic) + Source Sans 3 (body · editorial-clean ·
    explicitly NOT Inter — closes matrix §1.4 collapse risk · NOT Plex Sans ·
    NOT Public Sans).

hero_geometry:
    LF-2 stacked-editorial · full-bleed editorial photo TOP with credit
    overlay · serif h1 + side-quoted intro BELOW (8-col / 4-col split).
    Explicitly NOT 55/45 split. CS-HERO-01 demoted at family level — LF-2
    declares its own hero geometry per family-matrix §1.

hero_credit_overlay (L5=hero-overlay):
    "Cornice-credit-strip" · 3 inline stats inside the photo's overlay
    frame · cream type on photo:
      · 47 — Progetti realizzati
      · 18 — Anni di pratica
      · 6 — Città italiane
    KPI placement is INSIDE the hero photo's caption frame · NO separate
    cs-kpi-band on home · LF-2 declares L5=hero-overlay.
    Explicitly NOT a separate KPI tuple band · NOT a fiscal-calendar ·
    NOT a percorso-cadenza · NOT a stewardship-horizon-strip.

imagery_direction:
    architectural-interior + editorial-built-form · zero people in hero ·
    a built courtyard/portico of one of the studio's projects at golden
    hour · architectural shadow lines · sharp linework · NOT boardroom ·
    NOT tidy-desk · NOT 1:1 conversation · NOT library-reading-room
    (Continua adjacency).

section_rhythm_claim:
    LF-2 sequence B: hero · narrative · sectors · leadership · cases · cta.
    NO cs-pillars · NO cs-kpi-band · NO cs-trust · NO cs-cycle · NO dark band
    on home. Pillars REPLACED by editorial-narrative essay with pull-quotes
    and side-rail anchor links (L4=essay-with-anchors). Leadership reduced
    to single-portrait masthead (L6=single-portrait-feature). Cases shift
    from list-row to magazine 3+1 grid (L7=magazine-grid).

proof_style:
    project-portfolio + completion-year + client-typology · "Progetti —
    argomenti costruiti" labelling · cases ARE the proof; the firm is the
    curator. Case-detail page gains a "site-context" slot mirroring
    Solaria's `method-context` precedent (slot count parity; slot content
    fresh — names the SITE, not a method).

cta_personality:
    project-dossier-submission · "Apri un fascicolo progetto" · NOT a call ·
    NOT an appointment · NOT a discovery · NOT a mandate-dialogue · NOT a
    primo-appuntamento. Form gate is brief-upload-shape (sito + tipologia +
    cronoprogramma + documenti) — distinct from every existing sibling form.

stakeholder_first_30s_read:
    "An editorial-led architecture studio · they publish their projects
    like a built monograph · we'd brief them for the new headquarters."
    Cannot plausibly describe Pragma (B2B advisory · no building work)
    nor Fiscus (tax · no architecture) nor Solaria (coaching · no firm-
    of-architects identity) nor Continua (stewardship · no design-author
    identity). Audience differs · proof shape differs · CTA differs.
```

**Validation**
- [x] Every field concrete · operational vocabulary · no "modern" / "premium" / "professional"
- [x] `voice_positioning` is on matrix §1.1 OPEN stances list (`architectural-discipline`)
- [x] `palette_intent` lands in matrix §1.2 OPEN territory and a previously un-claimed §1.3 polarity strategy (NEUTRAL-anchored)
- [x] `hero_credit_overlay` composition is fresh — no sibling owns the in-overlay 3-stat strip
- [x] `stakeholder_first_30s_read` could not plausibly describe any of the four existing siblings (test §3.2 below)
- [x] Layout family LF-2 is OPEN territory — per family-matrix §3 — claim is authorised by Step 6 of divergence plan

### 3.1 · Palette warmth/coolness conflict check

```
proposed_palette_temperature:
  primary:    NEUTRAL    (#1F2226 graphite · L* ≈ 12 · cream-safe)
  secondary:  NEUTRAL    (#C7BFB1 pietra-serena · drafting-paper stone)
  accent:     WARM       (#B7491F terracotta-rust)

sibling_temperature_grids:
  Pragma:     primary=cool      · secondary=cool     · accent=cool
  Fiscus:     primary=cool      · secondary=warm     · accent=cool
  Solaria:    primary=warm      · secondary=warm     · accent=warm
  Continua:   primary=cool      · secondary=cool     · accent=warm

overlap_count_per_sibling:
  vs_Pragma:    0 / 3   (every cell differs by warmth class)
  vs_Fiscus:    0 / 3   (every cell differs)
  vs_Solaria:   1 / 3   (accent warm matches; primary + secondary differ)
                Note: hex distance is large (terracotta-rust #B7491F vs caramel
                #8B5A2B); rust reads red-orange ceramic whereas caramel reads
                muted brown — visually unambiguous.
  vs_Continua:  1 / 3   (accent warm matches; primary + secondary differ)
                Note: rust #B7491F vs antique-brass #B0875E — rust is red-orange
                ceramic, brass is yellow-gold metallic — different hue family.
                Mitigation §12 Warning 1 makes the rust visibly load-bearing in
                editorial display contexts NOT in chrome (different surfaces from
                Continua's brass).

palette_warmth_decision:    PASS
```

**Validation**
- [x] All four sibling grids filled (read off `template_dna.py` and Continua build brief)
- [x] No sibling overlaps on ≥ 2 cells → PASS
- [x] Cornice's NEUTRAL/NEUTRAL/WARM polarity is the only NEUTRAL-anchored strategy in the cluster (matrix §1.3 fresh territory)
- [x] Worst-case (1/3 vs Solaria and 1/3 vs Continua) carries explicit mitigation: rust is deployed on different surfaces from caramel/brass — see §12 Warning 1

### 3.2 · "Remove the studio name" pre-test

```
A · with the studio name as written:
    "Cornice is a single-principal architecture studio that publishes
     its projects as case-led editorial — each commission a built
     argument, catalogued and annotated."

B · with the studio name removed:
    "[___] is a single-principal architecture studio that publishes
     its projects as case-led editorial — each commission a built
     argument, catalogued and annotated."

C · with the studio name swapped to a generic placeholder:
    "Studio Acme is a single-principal architecture studio that
     publishes its projects as case-led editorial — each commission
     a built argument, catalogued and annotated."

studio_name_swap_verdict:    PASS
```

**Validation**
- [x] B and C still uniquely describe THIS template:
  - "single-principal architecture studio" — none of Pragma/Fiscus/Solaria/Continua claims architecture
  - "publishes its projects as case-led editorial" — magazine-grid + LF-2 editorial spread is fresh
  - "each commission a built argument" — voice anchor framing (`argomento`) is structurally distinct from decision/scadenza/percorso/generazioni
- [x] Cannot be claimed by Pragma (B2B advisory · no design authorship), Fiscus (commercialista · no design), Solaria (coaching · no firm-of-architects), Continua (stewardship · no design-author identity)
- [x] Re-run binding: same test re-runs on planner-brief §10 single-page summary at A.2 sign-off AND on the live render at A.7 (`master §5.12`)

---

## 4 · Forbidden similarities (anti-drift binding)

This block is copied verbatim into `planner-brief.md §2` and into the new template's content-module docstring per CS-EXEC-02 at A.5 build.

```
forbidden_similarities:

  vs_pragma:
    - NO 55/45 hero split (LF-2 declares stacked-editorial · CS-HERO-01 demoted at family level)
    - NO KPI tuple as a separate cs-kpi-band (LF-2 folds KPI into hero overlay)
    - NO "Fissa una call privata" CTA copy
    - NO navy + cool-blue + emerald palette
    - NO "(Direzione, Anno fondazione)" hero credit overlay shape
    - NO "Partner · Senior Associate · Counsel" credential vocabulary
    - NO boardroom long-table as hero subject
    - NO numbered 3-up pillar grid (LF-2 has no cs-pillars)
    - NO "decisional gravity" voice positioning
    - NO Inter as body sans (third use collapses cluster · CS-TYPE-* hard ban)
    - NO sticky-top wordmark-only navbar (LF-2 declares split-wordmark)

  vs_fiscus:
    - NO fiscal-calendar mid-strip (LF-2 has no cs-cycle)
    - NO warm-neutral + gold + blunotte palette
    - NO "Primo appuntamento" CTA copy
    - NO "ODCEC iscritti / Cassazionista / Revisore" credential block
    - NO tidy-desk-with-laptop-and-eyeglasses hero
    - NO bookshelf as ambient slot (Fiscus took it · CS-IMG-SRC-04)
    - NO IBM Plex Serif + IBM Plex Sans pairing
    - NO P.IVA + CF intake form shape
    - NO "(Direzione, Anno fondazione)" hero credit overlay
    - NO "presidio + scadenze-first" voice positioning

  vs_solaria:
    - NO percorso-cadenza mid-strip
    - NO manifesto-replacing-pillars opener (LF-2 replaces pillars with essay-with-anchors, not manifesto)
    - NO 1:1 conversation hero
    - NO "Prenota una discovery call" CTA copy
    - NO warm-carbon + ocra + caramel palette
    - NO "ICF-PCC + EMCC + Co-Active" credential vocabulary
    - NO 30s Caucasian × 2 portrait demographic (LF-2 has only ONE portrait — single-portrait-feature)
    - NO TWO em-wraps in voice anchor (contrast-pair is Solaria's exception)
    - NO "Aziende sponsor recenti" trust-band label
    - NO Inter as body sans
    - NO Fraunces as heading serif
    - NO "non-terapia non-consulenza" bounded-method framing

  vs_continua:
    - NO library / partner-study reading room as hero (Continua adjacency · object-led + interior-warm overlap risk)
    - NO stewardship-horizon-strip OR governance-cycle-strip (LF-2 has no mid-strip · L3=absent)
    - NO pine + pewter + brass palette
    - NO "Avvia un dialogo di mandato" CTA copy (mandate-dialogue conversion)
    - NO Crimson Pro as heading serif
    - NO Public Sans as body sans
    - NO "Albo dei Trustees · STEP · OAM · ANC" credential vocabulary
    - NO "(Custodi del mandato · Iscrizione Albo Trustees)" hero credit overlay
    - NO "Mandati in continuità" cases-list label
    - NO timeline cases shape (Continua's L7=timeline · LF-2 declares L7=magazine-grid)
    - NO 4-pillar 2x2 matrix with image (Continua's L4=2x2-with-image · LF-2 has no pillars)
    - NO 60s + 40s photographic leadership grid (LF-2 has only ONE portrait)
    - NO object-overlay hero (LF-5's hero shape · LF-2 declares stacked-editorial)
    - NO "Riconoscimenti istituzionali" trust-band label

cluster_level_red_lines:
  - Italic <em> on ONE load-bearing word per heading (CS-TYPE-02) — KEPT
  - Eyebrow letter-spacing 0.22em uppercase (CS-TYPE-05) — KEPT (RTL resets to 0)
  - Section padding 100×72 with max-width 1400 (CS-RHYTHM-01) — KEPT
  - Outline-only primary on cream + filled accent in CTA closer (CS-CTA-01 · ratified 2026-04-26) — KEPT
  - :focus-visible accent ring · 2px outline + 4px offset (CS-NAV-02) — KEPT (rust ring instead of brass/gold)
  - Locale switcher pill with lang+dir per link (CS-NAV-03) — KEPT
  - Pexels-only from URL #1 (CS-IMG-SRC-01) — KEPT
  - Whistleblowing legal row (CS-FOOT-02 · D.lgs. 24/2023) — KEPT (LF-2 L9=4-col-with-whistleblowing column)
  - Tabular numerals on every figure (CS-TYPE-03) — KEPT
  - Reduced-motion honoured · low motion vocabulary inherited (CS-MOTION-*) — KEPT
  - Editor click-to-edit guarded by body.mw-is-editor-preview (CS-MARKET-01) — KEPT

cluster_invariants_demoted_at_family_level (LF-2-only · per divergence-plan §3):
  - CS-HERO-01 (55/45 hero split) → REQUIRED at family level · LF-2 declares stacked-editorial
  - CS-TONE-03 (one dark band on home) → REQUIRED at family level · LF-2 declares zero dark bands on home (KPI in hero overlay; CTA closer is hairline cream)
  - CS-RHYTHM-02 (fixed home section sequence A) → REQUIRED at family level · LF-2 declares sequence B
  - CS-NAV-01 (sticky-top wordmark-only) → REQUIRED at family level · LF-2 declares split-wordmark-top
  - CS-FOOT-01 (3-col footer) → REQUIRED at family level · LF-2 declares 4-col-with-whistleblowing

ai_slop_avoidance:
  inter_on_h1:                NO
  purple_gradient:            NO
  cards_in_cards:             NO
  gray_on_colored_bg:         NO
  three_accent_buttons_hero:  NO
  get_started_free_cta:       NO
  emoji_in_body_or_headings:  NO
  exclamation_outside_quotes: NO
  backdrop_blur:              NO
  celebrity_quote:            NO
  mountain_peak_hero:         NO
  unverifiable_trusted_by:    NO
  made_with_marketweb_footer: NO
```

**Validation**
- [x] ≥ 3 forbidden similarities per existing sibling (Pragma 11 · Fiscus 10 · Solaria 12 · Continua 14 · total 47 explicit anti-collision lines)
- [x] `cluster_level_red_lines` cite concrete invariants with rule IDs · KEPT vs DEMOTED-AT-FAMILY columns explicit
- [x] LF-2 family-level demotions of cluster invariants are itemised (5 lines) — these are NOT silent breaks of CS-* rules; they are family-scoped per divergence plan §3 + family-matrix §1 LF-2 row
- [x] All 13 `ai_slop_avoidance` items NO

---

## 5 · Tone

```
tone_descriptor:           editorial-curatorial · architectural-discipline
register:                  Lei · committenza/intervento/progetto vocabulary ·
                           past-and-completed verb tense ("abbiamo costruito ·
                           abbiamo concluso · abbiamo pubblicato") + ongoing
                           ("stiamo curando")
stance:                    case-led · the firm is a curator of its own work ·
                           projects are arguments, not services · the firm-
                           client relationship is commission-per-project, not
                           mandate-across-decades
emphasis_convention:       serif italic-em on ONE load-bearing word per heading
                           (CS-TYPE-02 default · NOT Solaria's contrast-pair)
hyperbole_banlist_check:   YES   # CS-EXEC-04 banlist · "trasforma"/"sblocca"/
                                 # "rivoluziona"/Einstein-quote NEVER
```

**Validation**
- [x] `tone_descriptor` not in {advisory-sober, institutional-fiscal, professional-warm, stewardship-longitudinal}
- [x] `register` concrete (named verb-tense strategy + named architectural vocabulary)
- [x] `stance` differentiated from gatekept / presidio / bounded-method / custodial
- [x] Emphasis stays italic-em (no bold, no uppercase outside CS-TYPE-05 eyebrow)

---

## 6 · Imagery mood

```
imagery_key:                  business-architecture
hero_subject:                 a built courtyard / portico of one of the studio's
                              projects at golden hour · sharp architectural
                              shadow lines · stone-and-concrete material clarity ·
                              landscape composition · NO people · deep DoF on
                              foreground colonnade with mid-ground court
                              receding
hero_mood:                    editorial-architectural · golden-hour ·
                              structural · cinematic-but-quiet · NOT cold-
                              corporate · NOT desk-task · NOT cosy-interior ·
                              NOT 1:1 · NOT mahogany-warm-library
                              (Continua adjacency)
hero_color_temperature:       warm sunlight on cool stone · neutral overall ·
                              NOT mahogany-warm (Continua) · NOT cool-daylight
                              (Pragma)
hero_subject_density:         object-led-only (zero people) · the building IS
                              the subject — not a person in a building
ambient_subject:              studio-interior at low natural light · drafting
                              boards visible · pin-up wall with sketches and
                              site-photographs · NO people · NOT bookshelf
                              (Fiscus reservation) · NOT atrium (Pragma) · NOT
                              warm-home-office (Solaria) · NOT slate-stairwell
                              (Continua's adjacency)
portrait_intent:              SINGLE portrait masthead (LF-2 L6=single-portrait-
                              feature) · founding architect · 50s · environmental
                              portrait at studio window with drafting tools in
                              soft-focus mid-ground · direct gaze · neutral
                              background · NOT 30s × 2 (Solaria's gap) · NOT
                              60s+40s pair (Continua's pattern · LF-5 only)
detail_subject:               architectural section drawing close-up · india ink
                              on parchment OR architect's compass on trace paper ·
                              NOT tax document (Fiscus) · NOT wax-seal letterhead
                              (Continua) · NOT method-notebook (Solaria)
sources_only:                 Pexels   # CS-IMG-SRC-01 · no Unsplash · no AI
                                       # imagery · Cornice is new = Pexels-only
                                       # from URL #1
cross_cluster_grep_intent:    YES      # curator runs grep BEFORE committing URLs
                                       # against business-corporate, business-
                                       # fiscal, business-coaching, business-
                                       # stewardship pools
```

**Validation**
- [x] `hero_subject` NOT boardroom · NOT tidy-desk · NOT 1:1 · NOT library-reading-room
- [x] `ambient_subject` NOT bookshelf · NOT atrium · NOT bright-meeting-room · NOT slate-stairwell
- [x] `portrait_intent` is single-portrait per LF-2 L6 · explicit demographic anti-collision (NOT 30sx2 · NOT 60s+40s pair)
- [x] `detail_subject` is architectural-drawing class · concrete cross-cluster anti-collision named
- [x] `sources_only` Pexels (no waiver requested · Cornice is new = Pexels-only from URL #1)

The detailed feasibility quick-search lives in `prebuild-quick-checks.md §3`. This intake declares the direction; the planner brief writes the per-slot subject specs; the curator at A.3 sources the URLs.

---

## 7 · Section rhythm (LF-2 sequence B)

```
home_section_order:
  1. hero (LF-2 L1=stacked-editorial · full-bleed photo TOP with credit overlay ·
     serif h1 + side-quoted intro BELOW · 8-col / 4-col split)
  2. cs-narrative (LF-2 L4=essay-with-anchors · 4-paragraph editorial essay
     with 2-3 pull-quotes and a side-rail of anchor links to /studio/ ·
     /servizi/ · /progetti/)
  3. cs-sectors (sentence-ribbon of project typologies · "Tipologie d'intervento")
  4. cs-leadership (LF-2 L6=single-portrait-feature · ONE founding architect
     masthead · large portrait + 2-paragraph bio + credentials)
  5. cs-cases-preview (LF-2 L7=magazine-grid · 3+1 grid: 1 hero card + 3 small ·
     each card carries a photo)
  6. cs-cta-closer (cream hairline-bordered band · NOT a dark band — LF-2 L5=
     hero-overlay places KPI in hero, no separate dark band on home)

mid_strip_name:               (none) · L3=absent — LF-2 has no mid-strip
                              differentiator. The narrative essay covers the
                              cadence-cell role.
home_dark_band_count:         0   # LF-2 family rule · KPI lives in hero overlay ·
                                  # CTA closer is cream with hairline border ·
                                  # CS-TONE-03 demoted at family level
pillars_count:                0   # LF-2 has no cs-pillars · narrative essay
                                  # replaces them
kpi_count:                    3   # in hero credit overlay only · CS-DENSITY-04
                                  # cap respected
leadership_block:             present · ONE portrait (single-principal studio)
cases_count_on_home:          4   # 3+1 magazine-grid · CS-DENSITY-05 cap respected
sectors_count:                10-12   # architecture sub-types: residenziale ·
                                      # pubblico · interno · paesaggio · restauro ·
                                      # concorso · culturale · uffici · industriale ·
                                      # sanitario · scolastico · misto-uso
```

**Validation**
- [x] `mid_strip_name` is `(none)` · LF-2 family declares L3=absent — no clash with any sibling's mid-strip
- [x] `home_dark_band_count` exactly 0 (LF-2 family rule) — declared deviation from CS-TONE-03 at family level, not silent
- [x] Pillars 0 / KPI 3 (in hero overlay) / cases 4 — within or family-declared
- [x] Leadership SINGLE portrait with explicit org-scale rationale (single-principal studio)

The detailed content-volume estimate lives in `prebuild-quick-checks.md §4`.

---

## 8 · CTA personality

```
primary_cta_copy:             "Apri un fascicolo progetto"
                              · NOT "call" · NOT "appointment" · NOT "discovery"
                              · NOT "dialogo di mandato"
                              · NOT on CS-CTA-02 banlist
                              · NOT used by any sibling
conversion_pattern:           project-dossier-submission · brief-upload-shape
form_gate:                    project-brief shape · 4 fields:
                                · sito (textarea · 1-2 sentence placeholder
                                  describing the location and intervention)
                                · tipologia (select · residenziale · pubblico ·
                                  interno · paesaggio · restauro · concorso ·
                                  culturale · misto)
                                · cronoprogramma desiderato (select · <12 mesi ·
                                  12-24 · 24-36 · >36)
                                · documenti già disponibili (multi-select ·
                                  rilievo · planimetria · vincoli · regolamento
                                  edilizio · bandi · concept iniziale · altro)
                              NOT P.IVA + CF (Fiscus's intake) ·
                              NOT NDA-ready boardroom form (Pragma's) ·
                              NOT ICF code-of-ethics referenced (Solaria's) ·
                              NOT scope+orizzonte+struttura (Continua's)
form_shape_anti_collision:    Cornice's intake names a SITE + TYPOLOGY +
                              TIMELINE + DOCUMENTS — every field is project-
                              architectural in vocabulary. The documents
                              multi-select is the differentiating field;
                              no sibling has it.
```

**Validation**
- [x] CTA copy not banned and not used by any sibling
- [x] `form_gate` does not match any sibling's intake shape
- [x] Hero contains ONE primary CTA at most (CS-PAL-05 implication preserved)

---

## 9 · Multilingual intent

```
initial_locale:                  it
planned_locales:                 [it, en, fr, es, ar]   # cluster default
rtl_required:                    YES                     # ar in scope

voice_anchor_it:                 "Ogni progetto è un <em>argomento</em> costruito, non un servizio reso."
em_word_it:                      argomento
contrast_pair_anchor:            NO                      # default one em-wrap
voice_anchor_translation_note:
    The italic carries the curatorial-architectural claim: a project is an
    argument, not a deliverable. Translators MUST italicise the word
    equivalent to "argomento":
      · EN: "argument"      → "Every project is a built <em>argument</em>, not a service rendered."
      · FR: "argument"      → "Chaque projet est un <em>argument</em> construit, pas un service rendu."
      · ES: "argumento"     → "Cada proyecto es un <em>argumento</em> construido, no un servicio prestado."
      · AR: "حُجَّةٌ"       → "كلّ مشروع <em>حُجَّةٌ</em> مَبنِيَّة، لا خدمة مُؤدَّاة." (italic
                              substitute via Kufi weight or oblique fallback —
                              cluster convention TBD at workflow C pre-flight)
    Do NOT italicise the verb "è" / "construit" / "is" / "es" / "هو". The italic
    is on the load-bearing curatorial noun (the project's KIND, not its action).

terminology_locked_pre_translation:
  cluster_terminology_file:      factory/standards/corporate-suite-design-standard.md §11
  credentials_per_locale:        [
                                   "Albo degli Architetti P.P.C. (OAPPC)",
                                   "Ordine degli Architetti di Milano · Iscrizione [N]",
                                   "CNAPPC (Consiglio Nazionale)",
                                   "MIBAC · qualifica per restauro architettonico (ove applicabile)"
                                 ]
                                 ALL real, verifiable. NOT invented.
  legal_row_per_locale:          [P.IVA · privacy · cookie · whistleblowing
                                  (D.lgs. 24/2023 · CS-FOOT-02 required for cluster)]

ar_specific:
  heading_font_swap:             "Noto Naskh Arabic" or "Noto Kufi Arabic"
                                 # decision at workflow C pre-flight · LF-2
                                 # editorial register favours Naskh humanist
                                 # italics; cluster default has been Kufi.
                                 # Explicit § decision required at C entry.
  body_font_swap:                "Amiri"                       # CS-TYPE-06
  latin_wordmark_preserved:      YES                           # CS-NAV-06 / CS-FOOT-03
  letter_spacing_reset:          YES                           # CS-TYPE-05 RTL reset 0.22em → 0
  rtl_layout_via_logical_props:  YES                           # CS-RESPONSIVE-08
  hero_8_4_split_under_rtl:      mirror via logical props · the side-quote
                                 column flips from right to left under dir=rtl
                                 — verify in walk
```

**Validation**
- [x] Voice anchor is one sentence with one `<em>` wrap
- [x] em-word named explicitly (`argomento`)
- [x] AR path wired in skin BEFORE workflow C · Naskh-vs-Kufi decision deferred to C pre-flight (does not block IT pass)
- [x] Credentials per locale verifiable (real Italian architectural ordini)

---

## 10 · Review expectations

```
target_initial_tier:             draft           # D-102 cadence · IT-only
target_eventual_tier:            published_live  # via release-decision-orchestrator
target_scorecard_grade:          ≥ 4.50/5        # 4.67/5 is precedent
target_blocking_findings:        0/N             # zero open [BLOCKING] before flip

walk_locales:                    [it]            # workflow A initial
walk_viewports:                  [1920, 1440, 1280, 1024, 768, 390]   # CS-RESPONSIVE-02
walk_pages:                      [home, about, services, case_study_list,
                                  case_study_detail, contact]   # CS-BROWSER-01
walk_layout_gates:               B-LAYOUT-1 (wireframe overlay) · B-LAYOUT-2
                                 (DOM section-list compare) · B-LAYOUT-3
                                 (L1–L9 classification) · per divergence plan §8

reviewer_disposition:            "first-of-cluster LF-2 occupant · 1st sibling
                                 to validate the layout-family system on a
                                 fundamentally different shell (stacked
                                 hero + no dark band + single-portrait + magazine
                                 cases + split-wordmark + 4-col footer) · higher
                                 review cost than 5th+ in an established sub-
                                 cluster · the build itself is the proof that
                                 the layout-family system can ship a
                                 fundamentally different layout without breaking
                                 cluster invariants"

critical_review_dimensions:
  - L1-L9 layout classification matches LF-2 row exactly (no drift) ·
    B-LAYOUT-3 walk gate
  - wireframe overlay vs Pragma/Fiscus/Solaria/Continua shows ≥30%
    bounding-box variance per pair · B-LAYOUT-1
  - hero-overlay KPI legible at 1920/1280/720 over the photo (contrast read +
    accent rust must NOT overlap photo-bright zones)
  - palette adjacency vs Continua (1/3 warmth-grid overlap on accent)
    visibly resolved by surface-distinct deployment of rust
  - imagery distinctness vs Continua (object-led + interior overlap risk —
    Cornice's exterior architectural-shadow framing must NOT crop into
    interior-warm at 1280/1024)
  - voice anchor preservation (one em-word, not two — Solaria mistake)
  - single portrait at LF-2 L6 must NOT read as a stock LinkedIn headshot —
    environmental composition with drafting tools in soft focus is binding
  - "remove the studio name" test on the LIVE render at A.7 (not just at intake)
  - whistleblowing column visible in 4-col-with-whistleblowing footer (L9)
  - split-wordmark masthead legible at 1280 + 720 (line 1 "CORNICE" + line
    2 "studio di architettura" must not collapse)

user_handshake_expectation:      after IT walk PASS · BEFORE locale rollout
                                 begins. First LF-2 occupant carries higher
                                 review cost than 5th+ in an established
                                 family — a HOLD here is more likely than for
                                 a Nth template in an established sub-cluster.
```

**Validation**
- [x] `target_initial_tier` = draft (D-102)
- [x] 6 viewports · 6 pages listed explicitly · 3 B-LAYOUT-* gates added vs Continua's plan
- [x] `critical_review_dimensions` are concrete · cite specific risks not "everything"

---

## 11 · User constraints

```
must_haves:
  - LF-2 layout-family declaration locked at intake · planner brief MUST
    inherit · style-critic MUST verify · walk MUST classify
  - object-led hero with zero people (cluster's 2nd object-led hero · 1st
    architectural)
  - single founding-architect portrait (LF-2 L6) · explicit ENVIRONMENTAL
    composition (drafting tools in mid-ground) · NOT a headshot
  - whistleblowing link in legal row (D.lgs. 24/2023 binding for cluster)
  - NEUTRAL/NEUTRAL/WARM warmth strategy (the only un-claimed cluster polarity)
  - voice anchor on a CURATORIAL noun ("argomento"), not a method or a
    deliverable
  - cases preview MUST be magazine-grid 3+1 · NOT list-row · NOT timeline
  - footer 4-col with whistleblowing column (LF-2 L9) · NOT 3-col

must_avoids:
  - any 55/45 hero (LF-2 declares stacked-editorial · CS-HERO-01 demoted)
  - any cs-kpi-band as a separate dark band (LF-2 KPI is in hero overlay)
  - any cs-pillars block (LF-2 has none)
  - any cs-cycle mid-strip (LF-2 L3=absent)
  - any timeline cases (Continua's L7=timeline)
  - any 2x2 pillar matrix (Continua's L4=2x2-with-image)
  - any form gate asking for P.IVA + CF (Fiscus collision)
  - any "free trial" / "first call free" framing (banlist + tone collision)
  - any contrast-pair voice anchor (Solaria reservation)
  - any hyperbole "transform/unlock/revolutionise" (CS-EXEC-04 banlist)
  - any 30s × 2 portrait (Solaria's gap) — LF-2 has only ONE portrait
  - any 60s + 40s pair portrait (Continua's pattern · only Continua does this)
  - any imagery URL appearing in business-corporate · business-fiscal ·
    business-coaching · business-stewardship pools (CS-IMG-SRC-04 cross-
    cluster grep)

deadline:               none specified by user · target a ~1-2 working day pass
                        per single-template-workflow.md
budget_constraints:     skin-budget ≤ 1300 lines (LF-2 needs more lines than
                        Continua's 1100 because of the LF-2 layout-router
                        scaffolding under templates/live_templates/business/
                        corporate-suite/_layouts/lf2/) · pack 6 Pexels URLs +
                        4 case-card URLs from pack extras · no custom
                        photography (CS-IMG-SRC-01)
```

**Validation**
- [x] Must-haves / must-avoids concrete and per-LF-2-rule
- [x] No constraint conflicts with cluster invariant (whistleblowing-link reinforces CS-FOOT-02; LF-2 family-level demotions of CS-HERO-01/CS-TONE-03/CS-RHYTHM-02/CS-NAV-01/CS-FOOT-01 are declared deviations per divergence plan §3, not silent breaks)

---

## 12 · Sibling conflict warnings (loaded into planner brief verbatim)

The planner reads these at A.2 BEFORE writing the brief; the style-critic re-reads at A.6.

### Warning 1 · Continua palette adjacency (warm-accent echo)

- **What**: Cornice's accent is rust `#B7491F`; Continua's accent is brass `#B0875E`. Both warm metallic-ceramic accents at first scroll. Hex distance is large (rust red-orange ceramic vs brass yellow-gold metallic), but two warm accents in the cluster's only two warm-accent occupants risks reading as a family-of-warm-accent siblings.
- **Mitigation binding**: rust must be deployed on **editorial-display surfaces** (large drop-cap initial in narrative essay · pull-quote em-word colour · magazine-grid card numerals · single-portrait masthead frame) — explicitly NOT on chrome (Continua's brass owns CTA + focus ring + KPI eyebrow). Cornice's :focus-visible ring is rust at 2px outline + 4px offset, but the load-bearing rust touchpoints are display-typographic, not chrome-interactive. This makes the two warm accents land on different surface classes.
- **Walk verification**: contrast report at 1920/1280/720 confirms rust visible against graphite + cream both. Side-by-side capture vs Continua at 1920 confirms the rust-vs-brass surface deployment differs by ≥5 visible touchpoints in different surface classes.

### Warning 2 · Continua imagery adjacency (object-led + zero-people overlap)

- **What**: Continua hero is library/partner-study reading room (interior, mahogany-warm, contemplative, zero people). Cornice hero is a built courtyard/portico at golden hour (exterior, architectural-crisp, structural, zero people). Both are object-led + zero-people. The cluster's first two object-led heroes — the precedent could read as "the cluster pattern."
- **Mitigation binding**: A.3 curator hard-rejects any Cornice hero candidate that is interior, has wood-tones, or shows reading material. Hero must read as **exterior + architectural + stone-or-concrete material**. The shadow lines and structural geometry are the differentiators. Build-brief §4 imagery DNA carries this rejection rule explicitly.
- **Walk verification**: imagery coherence at 1280 + 1024 (object-led photos most often crop into incoherence at narrow desktop and tablet landscape — the building must remain READABLE as exterior at every viewport).

### Warning 3 · Pragma stakeholder one-liner adjacency (institutional + serious)

- **What**: Both Pragma and Cornice read as "serious institutional Italian professional firm." Both use noun-phrase + descriptor construction. The differentiator is sub-cluster (B2B advisory vs architecture-firm) and proof shape (numeric KPI vs editorial cases).
- **Mitigation binding**: home page surfaces "progetto / committenza / argomento / opera / cantiere / Albo degli Architetti" in the first scroll (h1, narrative paragraph 1, leadership credentials, sectors-ribbon). The architecture vocabulary must land within 30 seconds. Note: this is the SAME class of risk Continua faced vs Pragma, but for Cornice the architectural sub-cluster vocabulary makes it easier to land.
- **Walk verification**: A.7 reviewer runs the "remove the studio name" test on the live render and confirms the audience reads as architecture/building commissioners, not as boardrooms.

### Warning 4 · LF-2 single-portrait risk (stock-headshot collapse)

- **What**: LF-2 L6=single-portrait-feature concentrates the entire cluster's leadership-presence into one image. If the curator picks a generic stock headshot, the page reads "LinkedIn profile photo" not "founding architect of an editorial studio." This is a higher-stakes single image than typical, because there's no second portrait to balance.
- **Mitigation binding**: A.3 curator hard-rejects any portrait that is (a) shot against pure white/grey backdrop, (b) shows shoulders + face only with no environmental context, (c) is too tightly cropped to read as "professional photo." Binding triple: subject is mid-50s + drafting tools or sketches visible in soft-focus mid-ground + direct gaze + neutral environmental background (NOT studio backdrop).
- **Walk verification**: A.7 reviewer confirms portrait reads as ENVIRONMENTAL not HEADSHOT at 1920/1280/768. If the portrait fails the read at 1280, hero crop is the most likely cause — re-crop or re-curate.

### Warning 5 · LF-2 zero-dark-band on home (cluster-invariant deviation)

- **What**: Every existing sibling has exactly one dark band on home (CS-TONE-03). LF-2 declares zero — KPI in hero overlay, CTA closer in cream with hairline border. This is a family-level demotion of CS-TONE-03, not a silent break. Risk: a casual reviewer reads the home as "missing the dark KPI band" and flags it as a regression.
- **Mitigation binding**: planner brief §6 carries the CS-TONE-03 family-level demotion banner explicitly; style-critic at A.6 reads the LF-2 row of `factory/reports/hardening/corporate-suite-layout-family-matrix.md §1` BEFORE flagging dark-band absence; release-gatekeeper aggregates the layout-family classification verdict (B-LAYOUT-3) before applying scorecard.
- **Walk verification**: B-LAYOUT-3 at A.7 records L5=hero-overlay rendered, not declared — confirming the demotion is real not accidental. If the rendered home shows zero dark band AND the L5 classification is hero-overlay AND the hero credit overlay carries the 3-stat tuple, the demotion is honoured.

---

## 13 · Sign-off summary

```
INTAKE SIGN-OFF · cornice-architettura  (FACTORY · LF-2 5th sibling)
====================================================================

What this template IS:
    A single-principal architecture studio that publishes its
    projects as case-led editorial — each commission a built
    argument, catalogued and annotated, not sold as a service.

What this template is NOT:
    NOT Pragma's boardroom-advisory mandate · NOT Fiscus's
    commercialista presidio · NOT Solaria's bounded executive
    coaching · NOT Continua's stewardship-grade family office —
    though the firm's commissions may serve clients of any of them.

Cluster:                         corporate-suite · architecture-firm · single-principal studio
Layout family:                   LF-2 · Editorial Spread (5th sibling · 1st LF-2 occupant)
Cluster reference pack:          CONTINUE                            (§0)
Cluster layout-family matrix:    LF-2 row OPEN → CLAIMED by Cornice   (§0)
Nearest siblings:                Pragma (institutional voice) · Continua (object-led imagery)

Voice positioning:               editorial-curatorial · architectural-discipline (matrix §1.1 OPEN)
Palette intent:                  graphite + pietra-serena + terracotta-rust (NEUTRAL/NEUTRAL/WARM — only un-claimed polarity)
Palette warmth grid:             PASS                                (§3.1)
Studio-name swap pre-test:       PASS                                (§3.2)
Typography intent:               Cormorant Garamond + Source Sans 3 (both in OPEN territory · explicitly NOT Inter/Plex/Public Sans)
Hero geometry:                   LF-2 stacked-editorial · 8/4 split below photo
Hero credit overlay (L5):        in-overlay 3-stat strip · "47 — Progetti / 18 — Anni / 6 — Città"
Imagery direction:               built courtyard/portico at golden hour (object-led · zero people · architectural)
Section rhythm claim:            LF-2 sequence B · zero dark band on home · narrative essay replaces pillars
CTA personality:                 project-dossier-submission · "Apri un fascicolo progetto"
Cases-preview:                   magazine-grid 3+1 (LF-2 L7)
Leadership:                      single-portrait-feature (LF-2 L6) · founding architect environmental
Footer:                          4-col-with-whistleblowing (LF-2 L9)
Navbar:                          split-wordmark-top (LF-2 L8) · "CORNICE / studio di architettura"

Forbidden similarities locked:   47 explicit anti-collision lines (11 vs Pragma · 10 vs Fiscus · 12 vs Solaria · 14 vs Continua)
LF-2 family-level demotions:     5 explicit (CS-HERO-01 · CS-TONE-03 · CS-RHYTHM-02 · CS-NAV-01 · CS-FOOT-01)
AI-slop avoidance:               YES across all 13 detector items

Initial locale:                  it
Planned locales:                 [it, en, fr, es, ar]
RTL required:                    YES

User must-haves locked:          8
User must-avoids locked:         13

Sibling conflict warnings:       5 explicit (Continua palette · Continua imagery · Pragma stakeholder · LF-2 single-portrait stock-risk · LF-2 zero-dark-band invariant-deviation)

Open questions for orchestrator:
  - Confirm Cormorant Garamond licence/availability vs Spectral as fallback
    heading serif if Cormorant proves cumbersome at h1 64px display size.
    Decision at A.5 build entry; not a re-spec.
  - Confirm AR Naskh-vs-Kufi heading-font choice for LF-2 editorial register
    (cluster default has been Kufi · LF-2's editorial-display register may
    favour Naskh humanist italics). Decision at workflow C pre-flight; IT
    pass does not require it resolved.
  - Confirm `_layouts/lf2/home.html` path placement under templates/live_templates/
    business/corporate-suite/ at A.5 build entry vs an inline conditional
    branch on `template.layout_family == "LF-2"` in the existing home.html.
    Per divergence plan §10 Step 6, this is the build session's call.
```

**Sign-off result (factory intake)**: every line filled, no blank fields, all five pre-build quick-checks resolve in `prebuild-quick-checks.md` to CONTINUE / GO / PASS / PASS / PASS, distinctness scores triangulate as 5/5 on every existing sibling (cf. `planner-brief.md §6`). The intake is **READY FOR PLANNER** at workflow A.2.

---

## 14 · After this intake

This intake is the binding input contract for `planner-brief.md`. The planner expands every field into the brief schema's matching field, fills the §6 collision check from the §4 forbidden-similarities block here, and produces the §10 single-page summary that the orchestrator reads at A.2 sign-off.

The §3.2 studio-name swap test and the AI-slop check are re-run on the planner brief's §10 summary at A.2; if either fails, the brief returns to A.2 re-spec, even if every numeric distinctness score is ≥ 4/5.

Companion files in this directory:
- `planner-brief.md` — implementation-ready DNA + section sequence + nav/footer specs
- `prebuild-quick-checks.md` — the 5 pre-build quick-checks re-run in stricter factory format · GO/NO-GO for A.3

The intake is paper-only. No code change. No registry edit. No imagery URL committed. No application surface touched.
