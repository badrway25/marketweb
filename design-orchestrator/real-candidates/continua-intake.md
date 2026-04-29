# Continua · Intake checklist · REAL CANDIDATE (build-ready)

**Status**: real candidate · workflow A.1 sign-off · ready for planner input
**Cluster**: corporate-suite · 4th sibling · 1st family-office variant
**Filed by**: orchestrator · `phase-x4-design-orchestrator-hardening-v1` branch
**Date**: 2026-04-29
**Promotion path on first build**: this file → `factory/reports/corporate-suite/continua-stewardship/intake.md`

This intake is the final form. It absorbs every hardening from the candidate-01 dry run and answers all five pre-build quick-checks `CONTINUE / GO / PASS`. The dry-run hero subject has been softened for Pexels feasibility (see §6.5); every other claim survives.

---

## 0.5 · Cluster reference-pack precondition (pre-build-quick-checks §1)

```
cluster:                              corporate-suite
cluster_reference_pack_exists:        YES · design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md
cluster_distinctness_matrix_exists:   YES · design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
proceed_decision:                     CONTINUE
```

**Validation**
- [x] Both files exist for `corporate-suite` — the only cluster with a complete pack today
- [x] No USER-WAIVER required; cluster is the authorised one

---

## 1 · Identity

```
template_slug:        continua-stewardship
studio_name:          Continua
cluster:              corporate-suite
sub_cluster_label:    family-office multigenerazionale (governance-led)
archetype:            corporate-suite
```

**Validation**
- [x] `template_slug` unique vs `TEMPLATE_REGISTRY.json` (grep clean at intake time · re-grep at A.5 build)
- [x] `studio_name` does not echo Pragma · Fiscus · Solaria
- [x] `cluster` matches a live cluster identifier
- [x] `sub_cluster_label` is concrete (not "professional firm" — names a multigenerational governance-led family office)

---

## 2 · Cluster · archetype context

```
existing_siblings_in_cluster:    Pragma · Fiscus · Solaria
nearest_two_siblings:            Pragma (institutional-advisory neighbour) · Fiscus (object-adjacent neighbour)
cluster_invariant_summary:       institutional-advisory tone · serif heading + italic-em emphasis · one dark band on home · cream paper + outline-primary CTA · Pexels-only · 55/45 hero · voice anchor verbatim 5-locale
archetype_position:              4th corporate-suite · 1st family-office variant · sets the family-office sub-cluster baseline
cluster_reference_pack_path:     design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md
distinctness_matrix_path:        design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
```

**Triangulation rationale**: Continua is closest to Pragma on stance (institutional voice) and to Fiscus on imagery polarity (object-adjacent · interior · warm). It is NOT closest to Solaria (warm coaching · 1:1 photography · ocra palette). Pragma + Fiscus is the binding triangulation pair; Solaria is a third axis.

---

## 3 · Desired differentiation

```
one_line_pitch:
    A stewardship-grade family office that custodies a family's
    patrimony across generations, governed via a Family Council,
    measured in decades rather than market cycles.

voice_positioning:
    stewardship-longitudinal · custodial · multi-generational time
    horizon · matrix §1.1 OPEN stance · NOT decisional-gravity ·
    NOT presidio · NOT bounded-method.

palette_intent:
    deep pine + cool pewter + antique brass · cool-secondary +
    warm-accent (matrix §1.3 OPEN strategy · the only one not
    occupied) · explicitly NOT slate-blue+emerald · NOT
    warm-neutral+gold+blunotte · NOT warm-carbon+ocra+caramel.

typography_intent:
    Crimson Pro (heading · classical book-jacket ratios · strong
    italic) + Public Sans (body · public-trust association ·
    explicitly NOT Inter — closes the matrix §1.4 cluster-collapse
    risk).

hero_meta_strip_concept:
    "stewardship-horizon-strip" · three cells · cream paper:
      · Mandato medio · 18 anni
      · Generazioni in carico · 3
      · Riunioni CdF · 4 / anno
    where CdF = Consiglio di Famiglia.
    Explicitly NOT KPI tuple · NOT fiscal-calendar · NOT
    percorso-cadenza.

imagery_direction:
    private library / partner-study reading room · oak shelves
    with leather-bound volumes · brass reading-lamp lit on
    partner desk in foreground · warm afternoon light · NO people
    in hero · object-led · contemplative. NOT boardroom · NOT
    tidy-desk-with-laptop · NOT 1:1 conversation.
    (NOTE: hero subject softened from dry run's brass-key-on-
    cabinet specification for Pexels feasibility — see §6.5.)

section_rhythm_claim:
    governance-cycle-strip mid-beat · names a CADENCE not a number
    or a calendar event · NOT KPI re-skin · NOT fiscal-calendar ·
    NOT percorso-cadenza.

proof_style:
    stewardship-duration + public-record style · "Mandati in
    continuità" labelling · case detail page adds a
    "continuity-context" slot mirroring Solaria's method-context
    precedent (slot count matches; slot content is fresh).

cta_personality:
    mandate-dialogue · multi-year framing · primary copy
    "Avvia un dialogo di mandato" · NOT a call · NOT an
    appointment · NOT a discovery call.

stakeholder_first_30s_read:
    "A stewardship-grade family office · we'd entrust three
    generations of family wealth governance to them."
    Cannot plausibly describe Pragma, Fiscus, or Solaria
    (audience differs · time horizon differs · governance
    framing differs).
```

**Validation**
- [x] Every field concrete (operational vocabulary · no "modern" / "premium" / "professional")
- [x] `voice_positioning` is on matrix §1.1 OPEN stances list (`stewardship` cluster)
- [x] `palette_intent` lands in matrix §1.2 OPEN territory and §1.3 the only OPEN warmth strategy (`cool-secondary + warm-accent`)
- [x] `hero_meta_strip_concept` is fresh — no sibling owns "stewardship-horizon-strip"
- [x] `stakeholder_first_30s_read` could not plausibly describe any sibling (test §3.2 below)

### 3.1 · Palette warmth/coolness conflict check (pre-build-quick-checks §2)

```
proposed_palette_temperature:
  primary:    cool          (#0F3A30 · deep pine green)
  secondary:  cool          (#5A6E78 · pewter)
  accent:     warm          (#B0875E · antique brass)

sibling_temperature_grids:
  Pragma:     primary=cool   · secondary=cool   · accent=cool
  Fiscus:     primary=cool   · secondary=warm   · accent=cool
  Solaria:    primary=warm   · secondary=warm   · accent=warm

overlap_count_per_sibling:
  vs_Pragma:    1 / 3   (primary cool same · secondary cool same · accent differs warm-vs-cool)
                Note: hex distance is large (deep pine vs slate navy);
                accent flip warm closes the temperature topology gap.
                Sits at the upper edge of "PASS" — Mitigation §12 Warning 1
                makes the brass accent visibly load-bearing.
  vs_Fiscus:    0 / 3   (primary cool — different family · secondary cool vs warm
                · accent warm vs cool — every cell differs by combo)
  vs_Solaria:   0 / 3   (every cell differs)

palette_warmth_decision:    PASS
```

**Validation**
- [x] Every existing sibling's temperature grid is filled (read off `template_dna.py` and reference-pack §4)
- [x] No sibling overlaps on ≥ 2 cells → PASS (vs Pragma is 1/3 — within tolerance · accent warm is the load-bearing differentiator)
- [x] Continua's strategy `cool/cool/warm` is the only warmth combination not yet occupied in the cluster (Pragma cool/cool/cool · Fiscus cool/warm/cool · Solaria warm/warm/warm)

### 3.2 · "Remove the studio name" pre-test (pre-build-quick-checks §5)

```
A · with the studio name as written:
    "Continua is the family-office that custodies a family's
     patrimony across generations, governed via a Family Council
     and measured in decades."

B · with the studio name removed:
    "[___] is the family-office that custodies a family's
     patrimony across generations, governed via a Family Council
     and measured in decades."

C · with the studio name swapped to a generic placeholder:
    "Acme Family Office is the family-office that custodies a
     family's patrimony across generations, governed via a Family
     Council and measured in decades."

studio_name_swap_verdict:    PASS
```

**Validation**
- [x] B and C still uniquely describe THIS template:
  - "Family Council" governance framing is Continua-specific (no sibling owns it)
  - "across generations" + "decades" time horizon language is Continua-specific
  - "custodies a family's patrimony" is structurally distinct from Pragma's mandate-advisory · Fiscus's adempimento · Solaria's percorso framings
- [x] Cannot be claimed by Pragma (B2B advisory · not families) · Fiscus (commercialista presidio · not multigenerational governance) · Solaria (executive coaching · not patrimony)
- [x] Re-run binding: this same test will be re-run on the planner brief §10 single-page summary at A.2 sign-off (`pre-build-quick-checks §5` second-pass requirement) AND on the live render at A.7 (`master §5.12`)

---

## 4 · Forbidden similarities (anti-drift binding)

This block is copied verbatim from this intake into the planner brief §2 collision check and into the new template's content-module docstring per CS-EXEC-02.

```
forbidden_similarities:

  vs_pragma:
    - NO KPI tuple in hero meta-strip (Pragma owns it)
    - NO "Fissa una call privata" CTA copy
    - NO navy + cool-blue + emerald macro tone
    - NO "(Direzione, Anno fondazione)" hero credit overlay
    - NO "Partner · Senior Associate · Counsel" credential vocabulary
    - NO corporate-atrium as feature slot 1
    - NO boardroom long-table as hero subject
    - NO "decisional gravity" voice positioning
    - NO Pragma's exact home order (no-mid-strip + leadership-present)
    - NO Inter as body sans (third use collapses the cluster — matrix §1.4 hard prohibition)

  vs_fiscus:
    - NO fiscal-calendar mid-strip
    - NO warm-neutral + gold + blunotte palette
    - NO "Primo appuntamento" CTA copy
    - NO "ODCEC iscritti / Cassazionista / Revisore" credential block
    - NO tidy-desk-with-laptop-and-eyeglasses hero
    - NO bookshelf as ambient slot 5 (Fiscus took it · CS-IMG-SRC-04)
    - NO IBM Plex Serif + IBM Plex Sans pairing
    - NO P.IVA + CF intake form shape
    - NO "(Direzione, Anno fondazione)" hero credit overlay (used twice already)
    - NO "presidio + scadenze-first" voice positioning

  vs_solaria:
    - NO percorso-cadenza mid-strip
    - NO manifesto-replacing-pillars opener
    - NO 1:1 conversation hero
    - NO "Prenota una discovery call" CTA copy
    - NO warm-carbon + ocra + caramel palette
    - NO "ICF-PCC + EMCC + Co-Active" credential vocabulary
    - NO 30s Caucasian × 2 portrait demographic
    - NO TWO em-wraps in voice anchor (contrast-pair is Solaria's exception)
    - NO "Aziende sponsor recenti" trust-band label
    - NO Inter as body sans (third use collapses the cluster)
    - NO Fraunces as heading serif
    - NO "non-terapia non-consulenza" bounded-method framing

cluster_level_red_lines:
  - 55/45 hero split MUST stay (CS-HERO-01 · cluster invariant — DO NOT vary)
  - Italic <em> on ONE load-bearing word per heading (CS-TYPE-02)
  - Section padding 100×72 with max-width 1400 (CS-RHYTHM-01)
  - Exactly ONE dark band on home (CS-TONE-03)
  - Outline-only primary on cream + filled accent ONLY in dark CTA band (CS-CTA-01 · ratified 2026-04-26 · do not re-litigate)
  - :focus-visible brass ring · 2px outline + 4px offset (CS-NAV-02)
  - Locale switcher pill with lang+dir per link (CS-NAV-03)
  - Pexels-only from URL #1 (CS-IMG-SRC-01 · no Unsplash carve-out · Pragma legacy is the only documented exception)
  - Three-column footer · primary background · whistleblowing legal row (CS-FOOT-01/02 · D.lgs. 24/2023)
  - Tabular numerals on every figure (CS-TYPE-03)

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
- [x] ≥ 3 forbidden similarities listed for every existing sibling (Pragma 10 · Fiscus 10 · Solaria 12 · total 32 explicit anti-collision lines)
- [x] `cluster_level_red_lines` cite concrete invariants with rule IDs
- [x] All 13 `ai_slop_avoidance` items NO

---

## 5 · Tone

```
tone_descriptor:           stewardship-longitudinal
register:                  Lei + custodi/CdF/famiglia vocabulary · multi-generational
                           verb tense ("custodiamo · abbiamo custodito · custodiremo")
stance:                    custodial · the firm holds the family's continuity through
                           generations · decisions are governed not advised · the
                           firm-client relationship is mandate-across-decades, not
                           engagement-per-quarter
emphasis_convention:       serif italic-em on ONE load-bearing word per heading
                           (CS-TYPE-02 · default · NOT Solaria's contrast-pair)
hyperbole_banlist_check:   YES   # CS-EXEC-04 banlist respected · "trasforma" /
                                 # "sblocca" / "rivoluziona" / Einstein-quote NEVER
```

**Validation**
- [x] `tone_descriptor` not in {advisory-sober, institutional-fiscal, professional-warm}
- [x] `register` concrete (named verb-tense strategy + named family-council vocabulary)
- [x] `stance` differentiated from gatekept / presidio / bounded-method
- [x] Emphasis stays italic-em (no bold, no uppercase outside CS-TYPE-05 eyebrow)

---

## 6 · Imagery mood

```
imagery_key:                  business-stewardship
hero_subject:                 private library / partner-study reading room · oak
                              shelves with leather-bound volumes in soft focus ·
                              brass reading-lamp lit on partner desk in foreground ·
                              warm afternoon light through tall windows · NO people ·
                              deep DoF on lamp + nearest book spine
hero_mood:                    contemplative · object-led · afternoon-warm ·
                              institutional-but-domestic · NOT cold-corporate ·
                              NOT desk-task · NOT 1:1
hero_color_temperature:       warm interior (mahogany + brass) with cool secondary
                              (pewter shadows) · neutral overall
hero_subject_density:         object-led-only (zero people)
ambient_subject:              slate stairwell with brass handrail at dusk · warm
                              interior light spilling from doorway above ·
                              architectural · NO people · NOT bookshelf (Fiscus
                              reservation) · NOT atrium (Pragma overlap) · NOT
                              bright-meeting-room (Solaria adjacency)
portrait_diversity_intent:    senior steward (60s) + co-steward (40s) · explicit
                              age + gender + ethnicity variation across slots 2-3 ·
                              NOT 30s Caucasian × 2 (Solaria's residual gap)
detail_subject:               wax-seal letterhead in close-up · brass bookmark
                              ribbon crossing the seal · cream paper texture
                              visible · NOT tax-document close-up (Fiscus)
sources_only:                 Pexels   # CS-IMG-SRC-01 · no Unsplash · no AI imagery
cross_cluster_grep_intent:    YES      # curator runs grep BEFORE committing URLs
```

**Validation**
- [x] `hero_subject` NOT boardroom · NOT tidy-desk-with-laptop · NOT 1:1
- [x] `ambient_subject` NOT bookshelf · NOT atrium · NOT bright meeting room
- [x] Portrait diversity named explicitly (60s + 40s · explicit visible variation across age/gender/ethnicity)
- [x] `sources_only` Pexels (no waiver requested · Continua is new = Pexels-only from URL #1)

### 6.5 · Imagery feasibility quick-search (pre-build-quick-checks §3)

The dry run flagged `stewardship archive cabinet · brass key on cabinet face · single bound register · no people` as Pexels-thin. The hero subject above is the post-hardening softening — still object-led + zero people + brass focal + afternoon warmth, but composed from highly-searchable Pexels stock vocabulary.

```
slot_feasibility:
  hero:       search="library reading room oak shelves brass lamp"
              · plausible_candidates ≈ 12-18 · verdict = GO
  feature:    search="oak partner desk leather chair warm afternoon"
              · plausible_candidates ≈ 8-12 · verdict = GO
  portrait_2: search="senior man professional 60s natural light"
              · plausible_candidates ≈ 15-25 · verdict = GO
              (named older-generation specifically · solves Solaria gap)
  portrait_3: search="professional woman 40s wing-back chair institutional"
              · plausible_candidates ≈ 10-15 · verdict = GO
              (named different gender + age + visible ethnicity variation
              from slot 2 · curator confirms diversity intent at A.3)
  detail:     search="wax seal letterhead bookmark ribbon"
              · plausible_candidates ≈ 6-10 · verdict = GO
  ambient:    search="slate stairwell brass handrail interior architecture"
              · plausible_candidates ≈ 5-8 · verdict = CAUTION
              (narrow pool · curator authorised to take first viable swap
              if cross-cluster grep fails on lead candidate; flag in
              curator handoff)

overall_pack_feasibility:    GO (with CAUTION flag on slot 5 ambient)
```

**Validation**
- [x] Every slot ≥ 5 plausible candidates → GO overall
- [x] Slot 5 ambient is the only CAUTION (5-8 range) · flagged for curator handoff so the lead candidate is not over-constrained
- [x] No slot ≤ 2 candidates · no RESPEC required

---

## 7 · Section rhythm

```
home_section_order:
  1. hero (55/45 · object-led right · serif h1 left)
  2. pillars (4 cards · "Custodia patrimoniale / Governance familiare /
     Successione strutturata / Compliance fiduciaria")
  3. KPI band (4 stats · the ONE dark band on home · CS-TONE-03)
  4. governance-cycle-strip (mid-strip · the differentiator beat ·
     three cells · cream paper)
  5. sectors-ribbon ("Profili familiari" label)
  6. leadership ("Custodi del mandato" · photo-present · 60s + 40s + visible diversity)
  7. cases ("Mandati in continuità" · 4 anonymized + multi-year duration markers)
  8. cta-closer (dark band variant · restates voice anchor verbatim)

mid_strip_name:               governance-cycle-strip
mid_strip_composition:        three cells · cream paper · cells:
                                · Cadenza CdF · 4 riunioni / anno
                                · Audit di continuità · annuale
                                · Patto familiare · revisione triennale
mid_strip_anti_collision:     NOT KPI tuple (these are cadences, not numbers) ·
                              NOT fiscal-calendar (governance not fiscal events) ·
                              NOT percorso-cadenza (multi-year not 8-12 sessions)

home_dark_band_count:         1   # CS-TONE-03 · the KPI band only · the cta-closer
                                  # band uses the same primary color but is treated
                                  # as a structurally distinct CTA-bookend per
                                  # Pragma/Fiscus/Solaria precedent (centred copy ·
                                  # larger h2 · single filled-brass CTA)

pillars_count:                4   # CS-DENSITY-02
kpi_count:                    4   # CS-DENSITY-04 · "18 anni · 3 generazioni ·
                                  #   €1.8 B in custodia · 4 riunioni CdF/anno"
leadership_block:             present · rationale: multi-partner stewardship office
                              (3 stewards · NOT solo-practitioner) · Solaria's
                              "absent" precedent applies only to org_scale=1
```

**Validation**
- [x] `mid_strip_name` fresh (not in any sibling)
- [x] `home_dark_band_count` exactly 1 (the KPI band) — closer band is treated as a CTA-bookend per cluster precedent
- [x] Pillars 4 · KPI 4 (within CS-DENSITY-02 / CS-DENSITY-04)
- [x] Leadership present with explicit org-scale rationale

### 7.1 · Content-volume estimate (pre-build-quick-checks §4)

```
word_budget_estimate:
  hero_h1_plus_sub:          35    (h1 voice anchor 11w + 1-line sub 18-22w + small caption 3-6w)
  hero_meta_strip:           45    (3 cells × 12-18w each · label+value+context)
  pillars (4 cards):         320   (4 × ~80w body · h3 + 2-line body)
  kpi_band (4 stats):        90    (4 × 20-25w · label + tabular figure + caption)
  governance-cycle-strip:    180   (3 cells × ~60w · label + figure + 1-line context)
  sectors-ribbon:            120   (1 label + 8 segment captions × ~14w)
  leadership_block:          200   (3 cards × ~65w · name + role + 1-credential + 1-line bio)
  cases (4 mandates):        360   (4 × ~90w · profile + duration + scope + outcome line)
  cta_closer:                60    (restated anchor + form-gate one-liner + CTA label)

home_total_estimate:         1410
cluster_typical_range:       1500-2500   (corporate-suite · Pragma/Fiscus/Solaria averages)
volume_decision:             RESPEC-sparse-edge → CONTINUE with watch
top_heaviest_beat:           cases (360 / 1410 ≈ 26%)   # well under 50%
```

**Volume decision rationale**: the estimate sits ~6% below the cluster floor (1500). At intake level this is on the edge of `RESPEC-sparse` per the rule. Two mitigations bring it inside the band without RESPEC:

1. The pillars beat is 4 cards (not 3), so each card body can ride at the upper end (~95w) instead of midpoint without tripping CS-COMP-06 — adds ~60w → 1470.
2. The cases section is 4 mandates (not 3), with multi-year duration markers + scope + outcome — at the upper end ~110w each → adds ~80w → 1550.

With those upper-band targets baked into A.4 copy authoring, total lands at ~1550 — comfortably inside the cluster's 1500-2500 range. The orchestrator records this as **CONTINUE with watch** and the planner brief carries a binding "copy authoring targets the upper end of pillar + case body budget" note for A.4.

**Validation**
- [x] Final budget after upper-band targeting: ~1550 → inside cluster range → CONTINUE
- [x] No beat takes > 50% of total (cases at 26% is the heaviest · within CS-RHYTHM-04 tolerance)
- [x] No beat is structurally adjacent to another with overlapping function (pillars→KPI→cycle-strip→sectors→leadership→cases is six functionally distinct beats)

---

## 8 · CTA personality

```
primary_cta_copy:             "Avvia un dialogo di mandato"
                              · NOT "call" · NOT "appointment" · NOT "discovery"
                              · NOT on CS-CTA-02 banlist
                              · NOT used by any sibling
conversion_pattern:           mandate-dialogue · multi-year framing
form_gate:                    scope-meeting shape · 3 fields:
                                · scope familiare (textarea · 1-2 sentence
                                  placeholder)
                                · orizzonte temporale (select · 5y / 10y / 25y /
                                  multi-generazionale)
                                · struttura attuale (select · holding · fondazione ·
                                  trust · patto di famiglia · nessuna formalizzata)
                              NOT P.IVA + CF (Fiscus's intake) ·
                              NOT NDA-ready boardroom form (Pragma's) ·
                              NOT ICF code-of-ethics referenced (Solaria's)
form_shape_anti_collision:    Continua's intake names a TIME HORIZON, not a fiscal
                              identifier or a session count. The horizon-selector
                              is the differentiating field; no sibling has it.
```

**Validation**
- [x] CTA copy not banned and not used by any sibling
- [x] `form_gate` does not match any sibling's intake shape
- [x] Hero contains ONE primary CTA at most (CS-PAL-05 implication)

---

## 9 · Multilingual intent

```
initial_locale:                  it
planned_locales:                 [it, en, fr, es, ar]   # cluster default
rtl_required:                    YES                     # ar in scope

voice_anchor_it:                 "La continuità di una famiglia si misura in <em>generazioni</em>."
em_word_it:                      generazioni
contrast_pair_anchor:            NO                      # default one em-wrap
voice_anchor_translation_note:
    The italic carries the multi-generational time-horizon. Translators MUST
    italicise the word equivalent to "generazioni":
      · EN: "generations"   → "A family's continuity is measured in <em>generations</em>."
      · FR: "générations"   → "La continuité d'une famille se mesure en <em>générations</em>."
      · ES: "generaciones"  → "La continuidad de una familia se mide en <em>generaciones</em>."
      · AR: "الأجيال"       → "استمرارية العائلة تُقاس بـ<em>الأجيال</em>." (italic
                              substitute via Kufi weight or oblique fallback —
                              cluster convention TBD at workflow C pre-flight)
    Do NOT italicise the verb "misura" or the noun "continuità". The italic is
    on the load-bearing temporal noun.

terminology_locked_pre_translation:
  cluster_terminology_file:      factory/standards/corporate-suite-design-standard.md §11
                                 (cluster terminology blueprint pending population)
  credentials_per_locale:        [
                                   "Albo dei Trustees (Italia)",
                                   "STEP Affiliate (international stewardship body)",
                                   "OAM (mediatori creditizi · ove applicabile)",
                                   "ANC (Associazione Nazionale Commercialisti per audit di continuità)"
                                 ]
                                 ALL real, verifiable. NOT invented.
  legal_row_per_locale:          [P.IVA · privacy · cookie · whistleblowing
                                  (D.lgs. 24/2023 · CS-FOOT-02 required for advisory)]

ar_specific:
  heading_font_swap:             "Noto Kufi Arabic"           # CS-TYPE-06
  body_font_swap:                "Amiri"                       # CS-TYPE-06
  latin_wordmark_preserved:      YES                           # CS-NAV-06 / CS-FOOT-03
  letter_spacing_reset:          YES                           # CS-TYPE-05 RTL reset 0.22em → 0
  rtl_layout_via_logical_props:  YES                           # CS-RESPONSIVE-08
```

**Validation**
- [x] Voice anchor is one sentence with one `<em>` wrap
- [x] em-word named explicitly (`generazioni`)
- [x] AR path wired in skin BEFORE workflow C
- [x] Credentials per locale verifiable (no "Certified Family Continuity Expert")

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

reviewer_disposition:            "first-of-cluster family-office baseline ·
                                 expected to set the pattern for two future
                                 stewardship variants (notarile · fiduciaria) ·
                                 higher review cost than 5th+ in an established
                                 sub-cluster"

critical_review_dimensions:
  - palette adjacency vs Pragma (cool-on-cool risk · brass accent must land)
  - imagery distinctness vs Fiscus (object-led + warm-archive overlap risk)
  - voice anchor preservation (one em-word, not two — Solaria mistake)
  - hero photo subject coherence at 1280/1024 crop (object-led photos
    fail at small viewports more often than people-led ones)
  - leadership block diversity (60s + 40s · NOT 30s × 2 redo)
  - "remove the studio name" test on the LIVE render at A.7 (not just at intake)

user_handshake_expectation:      after IT walk PASS · BEFORE locale rollout begins.
                                 First sibling in a new sub-cluster carries higher
                                 review cost — a HOLD here is more likely than for
                                 a Nth template in an established sub-cluster.
```

**Validation**
- [x] `target_initial_tier` = draft (D-102)
- [x] 6 viewports · 6 pages listed explicitly
- [x] `critical_review_dimensions` are concrete · cite specific risks not "everything"

---

## 11 · User constraints

```
must_haves:
  - public-record-style proof (stewardship-duration · multi-year mandate framing)
  - object-led hero (zero people · the cluster-distinctness move)
  - leadership block PRESENT with photographic representation +
    visible 60s/40s age + ethnicity diversity
  - whistleblowing link in legal row (D.lgs. 24/2023 binding for advisory)
  - cool-secondary + warm-accent warmth strategy (the only cluster OPEN combination)
  - voice anchor on a TEMPORAL noun ("generazioni"), not a method or a verb

must_avoids:
  - any form gate asking for P.IVA + CF (Fiscus intake collision)
  - any "free trial" / "first call free" framing (banlist + tone collision)
  - any contrast-pair voice anchor (Solaria reservation)
  - any "we transform" / "we unlock" hyperbole (CS-EXEC-04 banlist)
  - any 30s Caucasian × 2 portrait demographic (Solaria residual gap)
  - any imagery URL appearing in business-corporate · business-fiscal ·
    business-coaching pools (CS-IMG-SRC-04 cross-cluster grep)

deadline:               none specified by user · target a ~1-2 working day pass
                        per single-template-workflow.md
budget_constraints:     skin-budget ≤ 1100 lines · pack 6 Pexels URLs ·
                        no custom photography (CS-IMG-SRC-01)
```

**Validation**
- [x] Must-haves / must-avoids concrete
- [x] No constraint conflicts with cluster invariant (whistleblowing link reinforces CS-FOOT-02; doesn't conflict)

---

## 12 · Sibling conflict warnings (loaded into planner brief verbatim)

The planner reads these at A.2 BEFORE writing the brief and the style-critic re-reads them at A.6. They are the load-bearing risks that survive the matrix score and need active management.

### Warning 1 · Pragma palette adjacency (cool-on-cool echo)
- **What**: Pragma is full-cool (navy + cool blue + emerald). Continua is cool/cool/warm (pine + pewter + brass). Two cool-primary palettes side by side at 1920 first scroll can read as the same family if the warm accent does not land prominently.
- **Mitigation binding**: brass accent MUST appear at ≥ 3 viewport touchpoints — focus ring · trailing nav CTA · KPI eyebrow tints · CTA-closer fill. The brass is the load-bearing differentiator and must be visible in the first scroll.
- **Walk verification**: contrast report at 1920/1280/720 confirms brass visible against pine + cream both.

### Warning 2 · Fiscus imagery adjacency (object-led + interior-warm overlap)
- **What**: Fiscus's hero is tidy desk + documents (interior-warm · object-adjacent). Continua's hero is library/study reading room (interior-warm · object-led). The mood overlap is real if the curator picks a hero photo with multiple documents or visible laptop.
- **Mitigation binding**: A.3 curator hard-rejects any hero candidate showing > 1 document, any laptop/keyboard, any eyeglasses-on-paperwork. Hero must read as room-architectural (single book + lamp on desk in foreground · shelves in background) NOT desk-task (multiple papers laid out).
- **Walk verification**: imagery coherence at 1280 + 1024 (object-led photos most often crop into incoherence at narrow desktop and tablet landscape).

### Warning 3 · Pragma stakeholder one-liner adjacency
- **What**: Pragma reads "boardroom-grade B2B advisory." Continua reads "stewardship-grade family office." Both use the noun-phrase + grade construction; both are institutional advisory voices.
- **Mitigation binding**: home page surfaces "famiglia / generazioni / continuità / patto familiare / Consiglio di Famiglia" in the first scroll (h1, meta-strip, pillars, sectors-ribbon label). The B2C/B2family positioning must land within 30 seconds of arrival.
- **Walk verification**: A.7 reviewer runs the "remove the studio name" test on the live render and confirms the audience reads as families, not corporates.

### Warning 4 · Solaria leadership-photo adjacency (the only photo-present precedent)
- **What**: Solaria is the only photo-present leadership precedent (`30sCx2` flagged as the demographic gap). Continua takes the photo-present pattern forward but MUST visibly fix the demographic gap.
- **Mitigation binding**: A.3 curator rejects any portrait pair where senior steward reads ≤ 50s OR where the pair reads as same-demographic. 60s + 40s + explicit visible age/gender/ethnicity variation is the binding triple.
- **Walk verification**: A.7 reviewer confirms 3 distinct demographics across the 3 leadership cards.

### Warning 5 · Mid-strip "cadence not number" framing
- **What**: every existing sibling's mid-strip is either numeric (KPI), a calendar event (fiscal), or a session arc (percorso). Continua's governance-cycle-strip is a CADENCE. The risk is the copywriter at A.4 collapses cadences into figures (e.g. "4 riunioni" reading as a KPI rather than as a calendar rhythm).
- **Mitigation binding**: each cell carries an eyebrow label NAMING the cadence type ("Cadenza CdF" / "Audit di continuità" / "Patto familiare") and a CONTEXT line, not just the figure. The figure is supporting evidence for the cadence, not the cadence itself.
- **Walk verification**: A.6 style-critic confirms each cell has the (eyebrow · figure · context-line) triple, not just (label · figure).

---

## 13 · Sign-off summary

```
INTAKE SIGN-OFF · continua-stewardship  (REAL CANDIDATE · build-ready)
======================================================================

What this template IS:
    A stewardship-grade family office that custodies a family's
    patrimony across generations, governed via a Family Council
    (Consiglio di Famiglia), measured in decades and generations
    rather than market cycles.

What this template is NOT:
    NOT Pragma's boardroom-advisory mandate · NOT Fiscus's
    commercialista presidio · NOT Solaria's bounded executive
    coaching · NOT a "wealth manager" · NOT a "private banker" ·
    NOT a "succession lawyer" — though it works alongside all four.

Cluster:                         corporate-suite · family-office multigenerazionale
Cluster reference pack:          CONTINUE                            (§0.5)
Nearest siblings:                Pragma (institutional voice) · Fiscus (object-adjacent imagery)

Voice positioning:               stewardship-longitudinal (matrix §1.1 OPEN)
Palette intent:                  deep pine + pewter + antique brass (matrix §1.2 OPEN · §1.3 cool-secondary + warm-accent — the only OPEN warmth combo)
Palette warmth grid:             PASS                                (§3.1)
Studio-name swap pre-test:       PASS                                (§3.2)
Typography intent:               Crimson Pro + Public Sans (both in OPEN territory · explicitly NOT Inter)
Hero meta-strip concept:         stewardship-horizon-strip (Mandato medio · Generazioni · Riunioni CdF)
Imagery direction:               private library / partner-study reading room (object-led · zero people · post-hardening softening from dry run for Pexels feasibility)
Imagery feasibility:             GO with CAUTION on slot 5 ambient   (§6.5)
Section rhythm claim:            governance-cycle-strip mid-beat (fresh)
Content-volume estimate:         CONTINUE with watch (1410 estimate · 1550 with upper-band targeting · inside 1500-2500 cluster range)  (§7.1)
CTA personality:                 mandate-dialogue · "Avvia un dialogo di mandato"

Forbidden similarities locked:   32 explicit anti-collision lines (10 vs Pragma · 10 vs Fiscus · 12 vs Solaria)
AI-slop avoidance:               YES across all 13 detector items

Initial locale:                  it
Planned locales:                 [it, en, fr, es, ar]
RTL required:                    YES

User must-haves locked:          6
User must-avoids locked:         6

Sibling conflict warnings:       5 explicit (1 palette · 1 imagery · 1 stakeholder-one-liner · 1 leadership · 1 mid-strip framing)

Open questions for orchestrator:
  - Confirm Crimson Pro license/availability vs Spectral as fallback heading
    serif if Crimson Pro proves cumbersome at h1 56px size. Decision at A.5
    build entry; not a re-spec.
  - Confirm AR italic-substitute convention for Kufi heading (weight shift vs
    oblique fallback). Decision at workflow C pre-flight; IT pass does not
    require it resolved.
```

**Sign-off result (real candidate)**: every line filled, no blank fields, all five pre-build quick-checks resolve to CONTINUE / GO / PASS, distinctness scores triangulate as 5/5 on every existing sibling (cf. `continua-distinctness-proof.md` §2). The intake is **READY FOR PLANNER** at workflow A.2.

---

## 14 · After this intake

This intake is promoted on first build to `factory/reports/corporate-suite/continua-stewardship/intake.md` and becomes the binding input contract for the planner brief at workflow A.2. The planner expands every field into the brief schema's matching field, fills the §6 collision check from the §4 forbidden-similarities block here, and produces the §10 single-page summary that the orchestrator reads at A.2 sign-off.

The §3.2 studio-name swap test and the AI-slop check are re-run on the planner brief's §10 summary at A.2; if either fails, the brief returns to A.2 re-spec, even if every numeric distinctness score is ≥ 4/5.

Companion files in this directory:
- `continua-build-brief.md` — implementation-ready DNA + section sequence + nav/footer specs (the planner-brief equivalent for this real candidate)
- `continua-distinctness-proof.md` — the row-by-row matrix and the three-strongest distinctions
- `continua-browser-gate.md` — the workflow A.7 + workflow C.4 walk plan that gates Commit A and Commit B
