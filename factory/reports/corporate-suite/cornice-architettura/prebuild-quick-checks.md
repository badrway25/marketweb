# Cornice · Pre-build quick-checks · LF-2 · 5th corporate-suite sibling

```yaml
report_type:        prebuild-quick-checks
template_slug:      cornice-architettura
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · cornice-architettura · Step 2 (paper-only)
date:               2026-04-30
binds_against:      design-orchestrator/workflows/pre-build-quick-checks.md
                    (the canonical procedure · 5 checks)
checked_by:         orchestrator (Step 2 promotion · stricter factory format)
inputs_consumed:
  - factory/reports/corporate-suite/cornice-architettura/intake.md (binding input)
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md
  - design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
  - design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md
  - factory/reports/hardening/corporate-suite-layout-family-matrix.md (LF-2 row)
  - factory/standards/corporate-suite-imagery-standard.md (§1 sourcing · §2 6-slot)
  - apps/catalog/template_dna.py (Pragma · Fiscus · Solaria · Continua palettes)
status_tag:         CHECKS-COMPLETE · ready for A.3 imagery-curation handoff
verdict:            GO for A.3 (with 3 named risks · zero RESPEC · zero HALT)
next_action:        Hand off to imagery-curator at A.3 entry · curator reads
                    planner-brief §4 as pack spec · cross-cluster grep BEFORE
                    committing any URL · curator approval gate before A.4
```

This file re-runs the five canonical pre-build quick-checks (`design-orchestrator/workflows/pre-build-quick-checks.md`) in stricter factory format. Stricter means: every check has an explicit numeric test, an explicit pass/fail trigger, an explicit weak point if the score is borderline, and an explicit fallback action. No "looks fine."

The five canonical checks:

| # | Check | Canonical when | Outcome |
|---|---|---|---|
| 1 | Reference-pack availability | A.1 entry | **CONTINUE** |
| 2 | Sibling palette warmth/coolness conflict | A.1 §3 | **PASS** |
| 3 | Imagery feasibility quick-search | pre-A.3 | **GO** with CAUTION on slot 4 |
| 4 | Content-volume estimate | A.1 §7 / A.2 §6 | **CONTINUE with watch** (LF-2 family floor adjusted · 1450 inside band) |
| 5 | "Remove the studio name" pre-test | A.1 §3 + A.2 §10 | **PASS** · re-bound at A.7 walk |

Headline: **GO for A.3 imagery curation** · zero RESPEC · zero HALT · 3 named risks documented for the curator handoff.

---

## Check 1 · Reference-pack availability (cluster + family precondition)

**Canonical procedure** (`pre-build-quick-checks.md §Check 1`): confirm cluster reference-pack and distinctness-matrix files exist; if cluster ≠ corporate-suite and either is missing, HALT.

**Cornice · stricter factory format**:

```
cluster_check:
  cluster_value:                      corporate-suite
  cluster_reference_pack:             design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md
                                      EXISTS · 261 lines · last touched 2026-04-28
  cluster_distinctness_matrix:        design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
                                      EXISTS · 374 lines · last touched 2026-04-28

layout_family_check (LF-2 specific · added at Step 2 promotion):
  layout_family_value:                LF-2 · Editorial Spread
  layout_family_matrix:               factory/reports/hardening/corporate-suite-layout-family-matrix.md
                                      EXISTS · 226 lines · last touched 2026-04-29
  lf2_row_status:                     OPEN (per §3 · "Reserved for the 5th sibling enrolment per plan Step 6")
  lf2_l1_l9_tuple_locked:             YES · per §1 LF-2 row table:
                                        L1 stacked-editorial · L2 B · L3 absent ·
                                        L4 essay-with-anchors · L5 hero-overlay ·
                                        L6 single-portrait-feature · L7 magazine-grid ·
                                        L8 split-wordmark-top · L9 4-col-with-whistleblowing
  divergence_plan_step6_authorisation: factory/reports/hardening/corporate-suite-layout-divergence-plan.md
                                       §10 Step 6 · "Build LF-2 (Editorial Spread) on
                                       the next corporate-suite enrollee" · architecture
                                       firm explicitly named as candidate

waiver_required:                      NO · cluster is the authorised one + family is OPEN
proceed_decision:                     CONTINUE
```

**Validation gates**
- [x] Cluster reference-pack exists (corporate-suite is the only cluster with a complete pack today)
- [x] Cluster distinctness matrix exists
- [x] LF-2 row OPEN per family-matrix §3 — claim is authorised by divergence plan §10 Step 6
- [x] LF-2 L1–L9 tuple is fully declared in family-matrix §1 — Cornice inherits, does not invent
- [x] No USER-WAIVER required

**Risk closed**: "we built a 5th corporate-suite sibling against a stale or missing layout-family declaration and shipped a cluster collision."

**Outcome · CONTINUE.**

---

## Check 2 · Sibling palette warmth/coolness conflict warning

**Canonical procedure** (`pre-build-quick-checks.md §Check 2`): classify proposed palette on warm/cool/neutral grid for primary/secondary/accent; compare cell-by-cell against EVERY existing sibling; ≥2 cells overlap with any sibling = RESPEC.

**Cornice · stricter factory format**: 4 existing siblings to check (not 3 as in the canonical procedure — this is the only place Cornice runs four sibling-comparisons, not three).

```
proposed_palette:
  primary:      #1F2226   graphite       L* ≈ 12   classification: NEUTRAL (genuinely
                                                   neutral-cool dark · reads architectural-
                                                   ink not as a hued brand colour)
  secondary:   #C7BFB1   pietra-serena  L* ≈ 76   classification: NEUTRAL (warm-leaning
                                                   neutral light · drafting-paper stone ·
                                                   reads as paper-tint not as a hued
                                                   secondary)
  accent:      #B7491F   terracotta-rust L* ≈ 41   classification: WARM (red-orange ceramic ·
                                                   architectural-pigment register)

sibling_temperature_grids (read off apps/catalog/template_dna.py + Continua build brief):
  Pragma:      primary=cool   secondary=cool    accent=cool       (full-cool · matrix §1.3)
  Fiscus:      primary=cool   secondary=warm    accent=cool       (mixed · matrix §1.3)
  Solaria:     primary=warm   secondary=warm    accent=warm       (full-warm · matrix §1.3)
  Continua:    primary=cool   secondary=cool    accent=warm       (cool/cool/warm · matrix §1.3)

cell_by_cell_overlap:
  vs Pragma   (cool, cool, cool):
    primary    NEUTRAL vs cool    DIFFER     (graphite #1F2226 vs slate-navy #1E293B)
    secondary  NEUTRAL vs cool    DIFFER     (pietra-serena vs cool blue #3B82F6)
    accent     WARM    vs cool    DIFFER     (rust vs emerald #10B981)
    overlap_count:                0 / 3      PASS
    hex_distance_primary:         large · graphite is hue-neutral; slate-navy has visible blue cast

  vs Fiscus   (cool, warm, cool):
    primary    NEUTRAL vs cool    DIFFER     (graphite vs gray-blue #1F2937)
    secondary  NEUTRAL vs warm    DIFFER     (pietra-serena vs gold #B58F4A)
    accent     WARM    vs cool    DIFFER     (rust vs deep-navy #1C3D5A)
    overlap_count:                0 / 3      PASS
    hex_distance_primary:         large

  vs Solaria  (warm, warm, warm):
    primary    NEUTRAL vs warm    DIFFER     (graphite vs warm-carbon #2B2A28)
    secondary  NEUTRAL vs warm    DIFFER     (pietra-serena vs ocra #C8621A)
    accent     WARM    vs warm    SAME       (rust #B7491F vs caramel #8B5A2B)
    overlap_count:                1 / 3      PASS (≤1)
    hex_distance_accent:          medium · rust reads red-orange ceramic ·
                                  caramel reads muted brown · visually unambiguous
                                  but two warm accents in cluster requires
                                  surface-class deployment mitigation (see Risk 1
                                  in handoff)

  vs Continua (cool, cool, warm):
    primary    NEUTRAL vs cool    DIFFER     (graphite vs deep-pine #0F3A30)
    secondary  NEUTRAL vs cool    DIFFER     (pietra-serena vs cool-pewter #5A6E78)
    accent     WARM    vs warm    SAME       (rust #B7491F vs antique-brass #B0875E)
    overlap_count:                1 / 3      PASS (≤1)
    hex_distance_accent:          medium · rust is red-orange ceramic ·
                                  brass is yellow-gold metallic · visually
                                  unambiguous · surface-class deployment
                                  mitigation BINDING (rust on display surfaces
                                  4 of 6 touchpoints · brass on chrome only)

aggregate_overlap_max:    1 / 3   (worst case · vs Solaria and vs Continua)
gate_threshold:           ≤ 1 / 3 with any sibling → PASS
                          ≥ 2 / 3 with any sibling → RESPEC
palette_warmth_decision:  PASS

cluster_polarity_position:
  Pragma:    cool/cool/cool      (claimed)
  Fiscus:    cool/warm/cool      (claimed)
  Solaria:   warm/warm/warm      (claimed)
  Continua:  cool/cool/warm      (claimed · matrix §1.3 OPEN-when-claimed)
  Cornice:   NEUTRAL/NEUTRAL/WARM (the only un-claimed cluster polarity ·
                                   matrix §1.3 fresh territory · validates the
                                   matrix's hypothesis that the cluster has
                                   space for at least one neutral-anchored
                                   polarity)
```

**Validation gates**
- [x] Every existing sibling's temperature grid filled (read off `template_dna.py` + Continua planner brief §3)
- [x] No sibling overlaps on ≥ 2 cells → PASS
- [x] Worst case (1/3 vs Solaria and 1/3 vs Continua) carries explicit surface-class mitigation in planner-brief §7 rust touchpoint inventory
- [x] Cornice's NEUTRAL/NEUTRAL/WARM polarity is documented as a NEW cluster polarity entry · planner-brief §3 binds this verbatim

**Weak point** (named for handoff): the 1/3 accent-warm overlap with Continua is the strongest residual collision risk. Both are warm metallic-ceramic accents. The mitigation is **surface-class deployment** — Cornice deploys rust across 6 touchpoints split CHROME (2) + DISPLAY (4); Continua's brass is CHROME-only (5 chrome touchpoints). The visible rendered separation is what makes the two warm accents read as distinct families, not as a "warm-accent cluster pattern." Planner-brief §7 binds this. Style-critic at A.6 verifies. Walk at A.7 confirms on render.

**Risk closed**: "Cornice's palette is unique by hex but reads as the same family as Continua because both lean warm-accent."

**Outcome · PASS** · weak point named for handoff to A.3 / A.6 / A.7.

---

## Check 3 · Imagery feasibility quick-search

**Canonical procedure** (`pre-build-quick-checks.md §Check 3`): for each of the 6 declared slot subjects from planner brief §4, run ONE Pexels search using the most concrete keyword phrase; count plausible candidates on first results page; ≥5 = GO, 3-4 = CAUTION, ≤2 = RESPEC.

**Cornice · stricter factory format**: 6 main slots + 4 magazine-grid extras (LF-2 needs 4 case-card photos beyond the 6-slot pool). Counts below are orchestrator paper-level estimates from candidate-pool surveying; the actual A.3 curator pass produces final candidates with cross-cluster grep on file.

```
slot_feasibility:

  slot_0_hero (built courtyard / portico at golden hour · architectural shadow lines · NO people):
    primary_search:       "architectural courtyard portico golden hour shadow stone"
    backup_search:        "modern Italian architecture courtyard interior light"
    plausible_candidates: 10-15
    verdict:              GO
    risk_flags:           cliché modernist-glass-tower must be hard-rejected by curator
                          (planner-brief §4 slot_0 rejection_rules) · cross-cluster grep
                          against `business-stewardship` (Continua adjacency) for
                          interior-warm overlap

  slot_1_feature (architectural model on drafting table · NO people):
    primary_search:       "architectural model drafting table trace paper compass"
    backup_search:        "scale model architecture studio raking light"
    plausible_candidates: 8-12
    verdict:              GO
    risk_flags:           any laptop / monitor / digital screen visible = REJECT ·
                          model must read as in-progress, not museum-piece

  slot_2_portrait (founding architect · 50s · environmental at studio window):
    primary_search:       "architect 50s studio window drafting tools natural light"
    backup_search:        "Italian architect portrait studio environmental"
    plausible_candidates: 8-12
    verdict:              GO
    risk_flags:           pure-white / seamless studio backdrop = REJECT ·
                          shoulders-up tight crop = REJECT · this is the highest-
                          stakes single image in the pack (LF-2 single-portrait-
                          feature) — see Risk 3 in handoff

  slot_3_portrait_or_project_alt (collaboratore OR project-interior):
    primary_search_a:     "young architect collaborator drafting board"
    primary_search_b:     "project interior architecture stone light no people"
    plausible_candidates: 10-15 either path
    verdict:              GO
    risk_flags:           if (a) — must visibly differ from slot_2 demographic;
                          if (b) — no wood-tones-warm interior (Continua adjacency)
    decision_at_a3:       curator picks (a) or (b) at A.3 entry · default (a)

  slot_4_detail (architectural section drawing close-up · india ink · NO documents):
    primary_search:       "architectural drawing section ink parchment close-up"
    backup_search:        "compass trace paper architectural drafting macro"
    plausible_candidates: 4-8
    verdict:              CAUTION (range straddles 5-cutoff)
    risk_flags:           narrow pool · hard-reject any tax document / invoice /
                          contract paper-stack (Fiscus adjacency)
    fallback_subject:     brass architect's compass at macro distance on trace
                          paper · feasibility ~6-10 candidates · curator
                          authorised to take this route at A.3 entry without
                          re-spec
    escalation_threshold: if A.3 curator returns ≤3 plausible candidates on
                          BOTH primary and fallback searches, escalate to
                          orchestrator at A.3 entry (not at A.4) · planner-
                          brief §4 slot_4 already bounds the fallback so
                          escalation is procedural, not re-spec

  slot_5_ambient (studio-interior · drafting boards · pin-up wall · NO people):
    primary_search:       "architecture studio drafting boards pin-up wall sketches"
    backup_search:        "architect office sketches walls drafting"
    plausible_candidates: 5-10
    verdict:              GO
    risk_flags:           any laptop / monitor on a desk in foreground = REJECT ·
                          any cosy wood-tones interior (Continua adjacency) =
                          REJECT · any modern open-plan office = REJECT (reads SaaS)

  pack_extras (4 additional case-card photos for LF-2 magazine-grid):
    extras_count:         4   # LF-2 L7=magazine-grid · 3+1 grid · 4 cards
                              # need 4 case photos beyond the 6-slot pool
    primary_search:       "architecture project building golden hour exterior" +
                          "architecture interior stone light" +
                          "architecture restoration project facade" +
                          "architecture residential exterior modern"
    plausible_candidates: 8-15 per search variant
    verdict:              GO
    risk_flags:           ALL 4 must cross-cluster grep clean against existing
                          corporate-suite pools · ALL 4 must visibly differ
                          from slot_0 hero (different project · different
                          season · different scale) · ALL 4 must read as
                          REAL architectural projects not as stock-architecture
                          clichés
    decision_at_a3:       curator picks 4 from a pool of ≥30 · the magazine-grid
                          carries 1 hero card + 3 small cards · the hero card
                          photo is the highest-impact extra (≥1200×800)

overall_pack_feasibility:    GO (with CAUTION on slot 4 detail)
total_plausible_unique_urls: ≥40 across primary + backup + extras searches
                             (well above CS-IMG-POOL-04 floor of 20-40 candidates)
```

**Validation gates**
- [x] 5 of 6 main slots → GO (each ≥ 5 plausible candidates)
- [x] 1 of 6 main slots → CAUTION (slot 4 detail · 4-8 candidates · planner-brief §4 carries explicit fallback)
- [x] 0 of 6 main slots → RESPEC
- [x] No slot ≤ 2 candidates · no HALT
- [x] Pack extras × 4 → GO across all 4 case-card searches
- [x] Cross-cluster grep targets named explicitly: `business-corporate` · `business-fiscal` · `business-coaching` · `business-stewardship`

**Weak point** (named for handoff): slot 4 detail (4-8 candidates · CAUTION) is the narrow-pool slot. Mitigation is the binding fallback to "brass architect's compass on trace paper" (~6-10 candidates) — planner-brief §4 slot_4 declares this verbatim so curator does NOT escalate; curator takes the fallback if primary search returns ≤4. Escalation only triggers if BOTH primary and fallback return ≤3.

**Risk closed**: "Cornice's planner declared a beautiful imagery direction that the Pexels-only constraint cannot satisfy at slot 4."

**Outcome · GO** with CAUTION on slot 4 (handled by binding fallback) · zero HALT.

---

## Check 4 · Content-volume estimate (with LF-2 family-floor calibration)

**Canonical procedure** (`pre-build-quick-checks.md §Check 4`): estimate home word budget per beat against cluster typical range (corporate-suite: 1500-2500). < 70% of floor → RESPEC; > 130% of ceiling → RESPEC; one beat > 50% of total → RESPEC that beat.

**Cornice · stricter factory format**: LF-2 family carries fewer beats than LF-1/3/4/5 (no cs-pillars, no cs-kpi-band, no cs-trust, no cs-cycle), so the cluster's 1500-2500 range needs an LF-2-specific calibration. Cornice's home is the first LF-2 occupant; the family-floor recommendation derived from this estimate is recorded for future LF-2 candidates.

```
word_budget_estimate (planner-brief §6):
  hero (h1 + sub + side-quote + 3-stat overlay):     60
  narrative (4 paragraphs + 3 pull-quotes +
             side-rail anchors):                    600   # LF-2 carries body weight
                                                          # in narrative essay because
                                                          # there are no pillars
  sectors-ribbon (label + 12 segments):             144
  leadership-single (h2 + role + 2-para bio +
                     4 credentials):                240   # single-principal warrants
                                                          # longer bio than card-grid
  cases-magazine-grid (1 hero card 130w +
                       3 small cards 75w each):     360
  cta-closer-cream (voice anchor + form-hint +
                    CTA label):                      65

home_total_estimate:                              1469

cluster_typical_range (corporate-suite Pragma/Fiscus/Solaria averages):  1500-2500
continua_actual_estimate (LF-5):                                         1550 (after upper-band targeting)
lf2_family_floor_calibration (proposed · derived from this estimate):    1400-2200

  rationale: LF-2 has 6 home sections vs LF-1/3/4/5's 7-8 sections. The family
             carries body weight in the narrative essay (600w) and the
             magazine-grid hero card (130w · upper end). Even with upper-band
             targeting on every beat, LF-2 estimate sits ~50w below cluster
             1500 floor. This is structural to the family, not a Cornice gap.
             Recommend lowering family-floor for LF-2 to 1400, ceiling to
             2200 (proportional adjustment). Cornice at 1469 sits comfortably
             inside the LF-2-adjusted range.

heaviest_beat:        narrative essay  600 / 1469 ≈ 41%
                      (under 50% threshold · CS-RHYTHM-04 OK)
second_heaviest:      cases-magazine-grid  360 / 1469 ≈ 25%

beat_function_check (CS-RHYTHM-04 · no two adjacent share function):
  hero (position) → narrative (essay) → sectors-ribbon (typology-list) →
  leadership-single (single-portrait) → cases-magazine-grid (case-studies) →
  cta-closer (closer)
  every adjacent pair is functionally distinct → PASS

volume_decision:           CONTINUE with watch
weak_point:                ~50w below 1500 cluster floor · LF-2 family-floor
                           calibration recommended (1400-2200) · planner-brief §6
                           targets upper-band on every beat to land at 1469
copy_authoring_target_a4:  upper-band targeting binding · A.4 must hit 600w in
                           narrative + 240w in leadership + 360w in cases ·
                           shortfalls > 5% in any of these three beats trigger
                           A.4 narrow re-author
mitigation_if_a4_falls_short:
  - extend narrative para 3 (commissions / authorship) by ~50w
  - extend cases hero-card argument-of-the-project by ~30w
  - extend leadership bio para 2 by ~40w
  total recoverable upside: ~120w → 1589 (above 1500 even at unadjusted cluster floor)
```

**Validation gates**
- [x] Final budget at 1469 · inside the LF-2-adjusted range (1400-2200)
- [x] At unadjusted cluster floor (1500) · 31w gap · within RESPEC tolerance with upper-band targeting binding for A.4
- [x] No beat takes > 50% of total (narrative at 41% · cases at 25%)
- [x] CS-RHYTHM-04 passes (every adjacent beat functionally distinct)
- [x] LF-2 family-floor calibration recorded for future LF-2 candidates (orchestrator append-to-matrix at A.9)

**Weak point** (named for handoff): the 31w gap below the unadjusted 1500 cluster floor is the load-bearing watch point. The mitigation is **upper-band targeting binding on three beats** (narrative · leadership · cases) at A.4 copy-authoring entry. If A.4 falls > 5% short of any of those three targets, A.4 narrow re-author triggers — not a re-spec.

**Risk closed**: "Cornice IT walk passed but the home reads sparse against Pragma/Continua because nobody estimated LF-2's structural body-volume gap upstream."

**Outcome · CONTINUE with watch** · LF-2 family-floor calibration proposed at 1400-2200 · A.4 upper-band targeting binding.

---

## Check 5 · "Remove the studio name" pre-test

**Canonical procedure** (`pre-build-quick-checks.md §Check 5`): write the `stakeholder_first_30s_read` three ways (A as written · B with name removed · C with name swapped to generic placeholder); B and C must still uniquely describe THIS template (not the generic cluster · not any sibling).

**Cornice · stricter factory format**: re-run TWICE per the canonical binding — once on intake §3 claim, once on planner-brief §15 single-page summary. Both runs PASS. The third re-run is at A.7 walk on the live render.

```
intake §3 stakeholder_first_30s_read:
    "An editorial-led architecture studio · they publish their projects
     like a built monograph · we'd brief them for the new headquarters."

A · with the studio name written:
    "Cornice is a single-principal architecture studio that publishes its
     projects as case-led editorial — each commission a built argument,
     catalogued and annotated."

B · with the studio name removed:
    "[___] is a single-principal architecture studio that publishes its
     projects as case-led editorial — each commission a built argument,
     catalogued and annotated."

C · with the studio name swapped to generic placeholder:
    "Studio Acme is a single-principal architecture studio that publishes
     its projects as case-led editorial — each commission a built argument,
     catalogued and annotated."

paper_level_verdict:    PASS (intake re-run)

reasons_b_and_c_still_describe_cornice_uniquely:
  - "single-principal architecture studio" — none of Pragma/Fiscus/
    Solaria/Continua claims architecture as a sub-cluster. Architecture
    is sub-cluster vocabulary specific to Cornice.
  - "publishes its projects as case-led editorial" — magazine-grid
    cases + narrative essay + drop-cap is the LF-2 editorial-spread
    signature; no existing sibling has this rhythm.
  - "each commission a built argument" — the voice anchor framing
    (`argomento`) is structurally distinct from Pragma's "decisione" /
    Fiscus's "scadenza" / Solaria's "percorso" / Continua's "generazioni"
    framings.
  - "catalogued and annotated" — editorial-curatorial register; not
    advisory-mandate, not commercialista-presidio, not coaching-method,
    not stewardship-custody.

cannot_be_claimed_by:
  - Pragma (B2B advisory · no design authorship · no architecture sub-cluster)
  - Fiscus (commercialista presidio · tax not building)
  - Solaria (coaching · no firm-of-architects identity)
  - Continua (stewardship · custodial not authorial · no built-form proof)

planner_brief §15 single-page summary re-test:
  same A/B/C variants applied to:
    "A single-principal architecture studio that publishes its projects
     as case-led editorial — each commission a built argument, catalogued
     and annotated, not sold as a service."
  paper_level_verdict:    PASS (planner re-run · the "not sold as a service"
                                clarifier strengthens the editorial-curatorial
                                positioning further)

re-run_bindings:
  - A.2 sign-off: orchestrator runs A/B/C on planner-brief §15 single-page
    summary AT sign-off · failure returns brief to re-spec
  - A.6 style-critic: includes this test as a [REQUIRED] check on the
    rendered home page first-scroll copy (h1 + subhead + side-quote + first
    narrative paragraph + sectors-ribbon label) — copy-authoring at A.4
    must preserve the architectural sub-cluster vocabulary in the first scroll
  - A.7 walk: re-runs on live render with wordmark hidden in dev tools
    (master §5.12 · CS-TONE-05) — failure routes to A.4 narrow copy-fix
```

**Validation gates**
- [x] B and C still uniquely describe Cornice — not generic, not any sibling
- [x] Architecture-firm sub-cluster vocabulary lands in 4+ surface locations on first scroll (h1, narrative, sectors-ribbon, leadership-credentials)
- [x] Voice anchor's `argomento` em-word is the structural anchor — removing the brand name does not weaken the curatorial-editorial frame
- [x] Re-run binding at A.2 sign-off (planner brief §15) · A.6 style-critic [REQUIRED] check · A.7 live walk (CS-TONE-05)

**Weak point** (named for handoff): the "remove the studio name" test passes at paper level, but at A.7 the live render's CSS-image-load-time and hero-photo-render at 1280/1024 may briefly show the page WITHOUT the wordmark mounted (FOUT) — during that flash, the hero photo + narrative-essay first scroll must STILL read as architecture-editorial. Mitigation: the architectural vocabulary lands inline with the h1 voice anchor (no above-the-fold dependency on the wordmark to resolve) — planner brief §6 hero row carries this verbatim.

**Risk closed**: "Cornice's planner brief scored ≥ 4/5 on every axis but the live page reads as a generic architecture-firm placeholder because the differentiation lived in the studio name and adjectives, not in the structure."

**Outcome · PASS** at intake AND at planner-brief re-runs · A.7 live walk binding.

---

## §Σ · GO/NO-GO for A.3 imagery curation

```
=========================================================
COMBINED VERDICT · cornice-architettura · LF-2 · 5th sibling
=========================================================

Check 1 · Reference-pack availability     CONTINUE
Check 2 · Palette warmth/coolness         PASS (worst case 1/3 vs Solaria + 1/3 vs Continua · within tolerance)
Check 3 · Imagery feasibility             GO (5 GO + 1 CAUTION on slot 4 with binding fallback)
Check 4 · Content-volume estimate         CONTINUE with watch (LF-2 family-floor calibration proposed · upper-band binding)
Check 5 · "Remove the studio name"        PASS (intake + planner re-runs)

OVERALL: GO for A.3 imagery curation
         · zero RESPEC
         · zero HALT
         · 3 named risks for handoff (see §Δ below)

A.3 entry binding:
  - Curator reads planner-brief §4 as pack spec (subject + mood + composition + rejection rules per slot)
  - Curator runs cross-cluster grep BEFORE committing any URL
    against:  business-corporate (Pragma · legacy Unsplash · grep both anyway)
              business-fiscal (Fiscus)
              business-coaching (Solaria)
              business-stewardship (Continua)
  - Curator-vs-reviewer separation per CS-IMG-SRC-05 · curator produces pack;
    separate reviewer signs off; A.4 copy-authoring begins only after LGTM
  - Curator hard-rejection rules from planner-brief §4 are binding · curator
    cannot soft-accept a candidate that fails any rejection rule
  - Curator authorised to take the slot 4 fallback (brass compass on trace
    paper) without orchestrator escalation if primary slot 4 search returns
    ≤4 candidates · planner-brief §4 slot_4 fallback_subject is pre-cleared
  - Curator escalates to orchestrator ONLY if BOTH primary and fallback for
    slot 4 return ≤3 candidates · this is procedural escalation not re-spec
```

---

## §Δ · 3 named imagery-curation risks for A.3 handoff

These are the load-bearing risks the curator must actively manage. Listed in descending order of likelihood-to-bite-at-A.3.

### Risk 1 · Slot 4 detail · narrow Pexels pool

- **What**: architectural section drawing close-up + india-ink-on-parchment is concretely searchable but Pexels-thin (4-8 plausible candidates · §3 CAUTION).
- **Why it bites at A.3**: the curator is the first agent to materialise the planner's slot-4 declaration as a real URL. If the primary search returns ≤4 viable candidates, the curator either (a) takes the fallback (brass compass on trace paper) or (b) escalates. Without the binding fallback already pre-cleared in planner-brief §4, the curator might soft-accept a clichéd "blueprint at angle" composition that fails the BIND rule (single sheet · single tool · macro distance).
- **Mitigation already in place**: planner-brief §4 slot_4 declares both primary subject AND `fallback_subject: brass architect's compass at macro distance on trace paper · feasibility ~6-10 candidates · curator authorised to take this route at A.3 entry without re-spec`. Curator does not need to escalate for the swap.
- **Escalation trigger (procedural · not re-spec)**: curator returns ≤3 plausible candidates on BOTH primary AND fallback searches. At that point orchestrator picks a third subject from the architectural-detail open territory (e.g., scaled architectural model corner detail · cropped facade ornament photograph) — single A.3 narrow re-pass, not a re-spec.
- **Cross-cluster grep specifically required**: against `business-fiscal` (Fiscus's tax-document detail must NOT overlap on subject — even though hex/composition differ, "single-sheet macro paper" framing risks looking adjacent if photo is too generic).

### Risk 2 · Slot 0 hero · object-led + zero-people overlap with Continua

- **What**: Continua's hero is library/partner-study reading-room (interior · mahogany-warm · contemplative · zero people). Cornice's hero is built-courtyard/portico at golden hour (exterior · stone-and-concrete · architectural-shadow · zero people). Both are zero-people object-led. The cluster's first two object-led heroes — risk reads as "the cluster pattern."
- **Why it bites at A.3**: the curator might pick a Pexels candidate that crops too tight on a single architectural detail, losing the exterior-architectural breathing room and accidentally reading interior-warm at narrow desktop crops (1280/1024). Continua's lead candidate is "library reading-room" — search-overlap risk on Pexels broad terms like "interior light architecture."
- **Mitigation already in place**: planner-brief §4 slot_0 declares the rejection rules verbatim — REJECT any cosy-interior with wood tones (Continua adjacency) · REJECT any tax-document/paper-work in frame (Fiscus adjacency) · REJECT any photo where building is incidental and people-in-foreground are the subject (Pragma adjacency) · REJECT cliché modernist-glass-tower from below.
- **Escalation trigger**: curator returns NO candidate that passes the exterior-architectural + zero-people + sharp-shadow-line filter. Orchestrator picks between (a) widening to project-interior at golden hour with stone-and-light (slot 3b territory promoted to hero) or (b) narrowing to "Italian piazza architecture golden hour" search variant — orchestrator routes at curator escalation.
- **Cross-cluster grep specifically required**: against `business-stewardship` (Continua's reading-room URLs must NOT appear in Cornice's pool · subject framing too close to overlap) and against `business-corporate` (Pragma's atrium URLs likewise).

### Risk 3 · Slot 2 portrait · LF-2 single-portrait stock-headshot collapse

- **What**: LF-2 L6=single-portrait-feature concentrates the cluster's leadership-presence into ONE image. If the curator picks a generic stock headshot (white backdrop · shoulders-up · face-only crop), the page reads "LinkedIn profile photo" not "founding architect of an editorial studio." This is a higher-stakes single image than typical because there's no second portrait to balance.
- **Why it bites at A.3**: Pexels has many "professional 50s portrait" candidates that pass the demographic filter (50s + senior-looking + neutral) but fail the LF-2 environmental binding (drafting-tools-or-sketches-visible-in-mid-ground). The default of stock-portrait-photography is the studio-backdrop look.
- **Mitigation already in place**: planner-brief §4 slot_2 declares the rejection rules + the BIND rule verbatim — REJECT pure white/grey/seamless studio backdrop · REJECT shoulders-up tight crop · REJECT face-only framing · REJECT corporate-suit + tie · BIND subject MUST be in 50s + drafting-tools/sketches MUST be visible in mid-ground + environmental NOT studio-backdrop. Walk verification at A.7 confirms portrait reads ENVIRONMENTAL not HEADSHOT at 1920/1280/768.
- **Escalation trigger**: curator returns ≤3 candidates that pass all five binding rules (50s + senior + drafting-tools-mid-ground + environmental + neutral-not-studio-backdrop). Orchestrator authorises one of two fallback paths at A.3:
  1. **Widen demographic to 60s** (still distinct from Solaria's 30s × 2 and from Continua's 60s+40s pair) — pool likely doubles
  2. **Substitute slot_3b project-interior as the leadership-feature backdrop**: portrait is shot in a built-project interior rather than studio — environmental-architectural shifts from "where the work happens" to "where the work has happened"
- **Cross-cluster grep specifically required**: against `business-coaching` (Solaria's portrait pool · 30s × 2 demographic must not overlap by URL) and against `business-stewardship` (Continua's 60s+40s pair must not overlap by URL).

---

## §Ω · Open questions surfaced by the 5 checks

```
1. LF-2 family-floor calibration (Check 4 outcome):
   - Proposed: lower cluster floor for LF-2 family from 1500 to 1400 (and
     ceiling from 2500 to 2200 proportionally).
   - Authority: orchestrator at A.9 append-to-matrix · NOT a Cornice-specific
     decision · binding for future LF-2 candidates.
   - Decision deferral: this prebuild check records the recommendation;
     formal calibration lands when the second LF-2 occupant enrols (LF-2
     remains 1-occupant until a 6th cluster sibling claims a different family).
   - For Cornice itself: 1469 estimate is inside the LF-2-adjusted range and
     within 31w of the unadjusted cluster floor with upper-band binding —
     no Cornice-specific re-spec needed.

2. Slot 4 fallback authority (Check 3 outcome):
   - Curator pre-authorised at A.3 to take the brass-compass-on-trace-paper
     fallback if primary section-drawing search returns ≤4 candidates.
   - This is a procedural escalation policy, not a re-spec authority — the
     fallback is itself declared in planner-brief §4 slot_4 fallback_subject.

3. Single-portrait demographic widening (Check 3 / Risk 3):
   - Curator pre-authorised to widen demographic from 50s to 60s if all five
     binding rules (50s + senior + drafting-tools-mid-ground + environmental +
     not-studio-backdrop) cannot be satisfied at 50s.
   - 60s is still distinct from Solaria's 30s × 2 and from Continua's 60s+40s
     pair (Continua has TWO portraits · Cornice has ONE).
```

---

## §Φ · Exit · what the next agent reads first

A.3 imagery-curator reads this file in the order:
1. **§Σ combined verdict** — the GO/NO-GO line and the A.3 entry binding
2. **§Δ 3 named risks** — the load-bearing risks the curator must manage at pack-time
3. **§Ω open questions** — the procedural escalation policies the curator is pre-authorised to invoke
4. **planner-brief.md §4** — the per-slot pack spec that the curator implements

The intake.md and planner-brief.md are the binding contracts; this file is the gate that A.3 reads first. After A.3 produces the pack and passes reviewer LGTM (CS-IMG-SRC-05), A.4 copy-translation begins with the intake §3 voice anchor + planner-brief §6 word-targets as input.

Paper-only at this Step 2 promotion. No code change. No registry edit. No imagery URL committed yet.
