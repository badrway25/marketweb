# Candidate-01 · Intake checklist · DRY RUN

**Status**: dry-run only · no app code touched · no real template seeded
**Purpose**: pressure-test `template-intake-checklist.md` on a hypothetical executive-advisory / family-office / governance candidate before the next real template enters the pipeline.
**Date**: 2026-04-29
**Filed by**: orchestrator (dry-run mode) · `phase-x4-design-orchestrator-dry-run` branch

---

## 1 · Identity

```
template_slug:      continua-stewardship
studio_name:        Continua
cluster:            corporate-suite
sub_cluster_label:  family-office multigenerazionale
archetype:          corporate-suite
```

**Validation**
- [x] `template_slug` unique vs `TEMPLATE_REGISTRY.json` (dry-run: simulated grep clean)
- [x] `studio_name` does not echo Pragma · Fiscus · Solaria
- [x] `cluster` matches a live cluster identifier
- [x] `sub_cluster_label` is concrete enough to triangulate (not "professional firm")

---

## 2 · Cluster · archetype context

```
existing_siblings_in_cluster:    Pragma · Fiscus · Solaria
nearest_two_siblings:            Pragma (institutional-advisory neighbour) · Fiscus (formal-document neighbour)
cluster_invariant_summary:       institutional-advisory tone · serif heading + italic-em emphasis · one dark band on home · cream paper + outline-primary CTA · Pexels-only · 55/45 hero · voice anchor verbatim 5-locale
archetype_position:              4th corporate-suite · 1st family-office variant
cluster_reference_pack_path:     design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md
distinctness_matrix_path:        design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
```

**Triangulation rationale**: Continua is closest to Pragma on stance (institutional voice) and to Fiscus on imagery polarity (object-led, document-adjacent). It is NOT closest to Solaria (warm coaching · 1:1 photography · ocra palette). Pragma + Fiscus is the correct triangulation pair.

---

## 3 · Desired differentiation

```
one_line_pitch:
    A stewardship-grade family office that custodies a family's
    patrimony across generations, not market cycles.

voice_positioning:
    stewardship-longitudinal · custodial · multi-generational time horizon
    (matrix §1.1 open stance · not gravitas / not presidio / not bounded-method)

palette_intent:
    deep pine + cool pewter + antique brass · cool primary + cool secondary
    + warm accent · the matrix §1.3 OPEN warmth strategy · explicitly NOT
    in slate-blue+emerald · NOT in warm-neutral+gold+blunotte · NOT in
    warm-carbon+ocra+caramel adjacencies

typography_intent:
    Crimson Pro (heading · classical book-jacket ratios · strong italic) +
    Public Sans (body · public-trust association · clearly NOT Inter)

hero_meta_strip_concept:
    "stewardship-horizon-strip" · three cells composed as:
      (Mandato medio · Generazioni in carico · Riunioni CdF / anno)
    where CdF = Consiglio di Famiglia (Family Council)
    explicitly NOT KPI tuple · NOT fiscal-calendar · NOT percorso-cadenza

imagery_direction:
    object-led private reading room · stewardship archive cabinet ·
    afternoon mahogany-warmth · no people in hero · brass-detail focal ·
    deep DoF · NOT boardroom · NOT tidy desk · NOT 1:1 conversation

section_rhythm_claim:
    governance-cycle-strip mid-beat · NOT fiscal-calendar · NOT
    percorso-cadenza · NOT a KPI re-skin

proof_style:
    stewardship-duration + public-record style ·
    "Mandati in continuità" labelling · case detail page adds a
    "continuity-context" slot mirroring Solaria's method-context precedent

cta_personality:
    mandate-opening · multi-year framing · NOT a call · NOT an appointment ·
    NOT a discovery call · primary copy "Avvia un dialogo di mandato"

stakeholder_first_30s_read:
    "A stewardship-grade family office · we'd entrust three generations of
    family wealth governance to them."
    Cannot plausibly describe Pragma, Fiscus, or Solaria.
```

**Validation**
- [x] Every field concrete (operational vocabulary, no "modern" / "premium")
- [x] `voice_positioning` is on matrix §1.1 OPEN stances list (`stewardship` + `custodial` + `longitudinal-care` cluster)
- [x] `palette_intent` is in matrix §1.2 OPEN territory ("Deep teal + champagne + cream" / "Sage + stone + dusty-ochre" family — pine/pewter/brass is in this orthogonal band)
- [x] `hero_meta_strip_concept` not in any sibling
- [x] `stakeholder_first_30s_read` could not plausibly describe any sibling

---

## 4 · Forbidden similarities (anti-drift binding)

```
forbidden_similarities:

  vs_pragma:
    - NO KPI tuple in hero meta-strip (Pragma owns it)
    - NO "Fissa una call privata" CTA copy (Pragma owns it)
    - NO navy + emerald + cream macro tone
    - NO "Direzione, Anno fondazione" hero credit overlay (used twice)
    - NO "Partner · Senior Associate · Counsel" credential vocabulary
    - NO corporate-atrium as feature slot 1
    - NO boardroom long-table as hero subject
    - NO "decisional gravity" voice positioning
    - NO Pragma's exact home order (no-mid-strip + leadership-present)

  vs_fiscus:
    - NO fiscal-calendar mid-strip
    - NO warm-neutral + gold + blunotte palette
    - NO "Primo appuntamento" CTA copy
    - NO "ODCEC iscritti / Cassazionista / Revisore" credential block
    - NO tidy-desk-with-documents-and-eyeglasses hero
    - NO bookshelf as ambient slot 5 (Fiscus took it)
    - NO IBM Plex Serif + IBM Plex Sans pairing
    - NO P.IVA + CF intake form shape
    - NO "Direzione, Anno fondazione" hero credit overlay (twice already)
    - NO "presidio + scadenze-first" voice positioning

  vs_solaria:
    - NO percorso-cadenza mid-strip
    - NO manifesto-replacing-pillars opener
    - NO 1:1 conversation hero
    - NO "Prenota una discovery call" CTA copy
    - NO warm-carbon + ocra + caramel palette
    - NO "ICF-PCC + EMCC + Co-Active" credential vocabulary
    - NO 30s Caucasian × 2 portrait demographic
    - NO TWO em-wraps in voice anchor (contrast-pair exception is Solaria's)
    - NO "Aziende sponsor recenti" trust-band label
    - NO Inter as body sans (used twice — third use collapses cluster)
    - NO Fraunces as heading serif
    - NO "non-terapia non-consulenza" bounded-method framing

cluster_level_red_lines:
  - 55/45 hero split MUST stay (CS-HERO-01 · cluster invariant — DO NOT vary)
  - Italic <em> on ONE load-bearing word per heading (CS-TYPE-02 · cluster
    typography signature; bold/uppercase emphasis collapses the cluster)
  - Section padding 100×72 with max-width 1400 (CS-RHYTHM-01)
  - Exactly ONE dark band on home (CS-TONE-03)
  - Outline-only primary on cream + filled accent ONLY in dark CTA band
    (CS-CTA-01 · ratified 2026-04-26 · do not re-litigate)
  - :focus-visible gold-equivalent ring (here: brass), 2px outline + 4px offset
  - Locale switcher pill with lang+dir per link
  - Pexels-only from URL #1 (no Unsplash; Pragma legacy is the only carve-out)

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
- [x] ≥ 3 forbidden similarities listed for each existing sibling (Pragma 9 · Fiscus 10 · Solaria 12)
- [x] `cluster_level_red_lines` cite concrete invariants with rule IDs
- [x] All 13 `ai_slop_avoidance` items NO

---

## 5 · Tone

```
tone_descriptor:           stewardship-longitudinal
register:                  Lei + custodi/CdF/famiglia vocabulary · multi-generational
                           verb tense ("custodiamo, abbiamo custodito, custodiremo")
stance:                    custodial · the firm holds the family's continuity
                           through generations, decisions are governed not advised
emphasis_convention:       serif italic-em on ONE load-bearing word per heading
                           per CS-TYPE-02 · default (NOT Solaria's contrast-pair)
hyperbole_banlist_check:   YES   # CS-EXEC-04 banlist respected
```

**Validation**
- [x] `tone_descriptor` not in {advisory-sober, institutional-fiscal, professional-warm}
- [x] `register` concrete (Lei + CdF/custode vocabulary, named verb-tense strategy)
- [x] `stance` differentiated from gatekept / presidio / bounded-method
- [x] Emphasis stays italic-em (no bold, no uppercase outside CS-TYPE-05 eyebrow)

---

## 6 · Imagery mood

```
imagery_key:                  business-stewardship
hero_subject:                 private family-office reading room with stewardship
                              archive cabinet open, brass key visible on cabinet
                              face, mid-afternoon mahogany-warmth, no people,
                              deep DoF on cabinet brass detail
hero_mood:                    archive-warm afternoon · object-led · contemplative ·
                              NOT cold-corporate · NOT desk-task
hero_color_temperature:       warm interior with cool secondary (mahogany + pewter
                              shadows), neutral overall
hero_subject_density:         object-led-only (zero people)
ambient_subject:              slate stairwell with brass handrail at dusk · NO
                              bookshelf (Fiscus reservation) · NO atrium
                              (Pragma overlap) · NO bright-meeting-room
                              (Solaria adjacency)
portrait_diversity_intent:    senior steward (60s) + co-steward (40s) · explicit
                              age + gender + ethnicity variation across slots 2-3 ·
                              NOT 30s Caucasian × 2 (Solaria already)
detail_subject:               brass key in keyhole on stewardship cabinet OR
                              wax-seal letterhead with bookmark ribbon · NOT
                              tax-document close-up (Fiscus)
sources_only:                 Pexels   # CS-IMG-SRC-01 · no Unsplash · no AI imagery
cross_cluster_grep_intent:    YES      # curator runs grep BEFORE committing URLs
```

**Validation**
- [x] `hero_subject` NOT boardroom · NOT tidy-desk-documents · NOT 1:1
- [x] `ambient_subject` NOT bookshelf
- [x] Portrait diversity named explicitly (60s + 40s, not 30s × 2)
- [x] `sources_only` Pexels (no waiver requested)

---

## 7 · Section rhythm

```
home_section_order:
  1. hero (55/45 · object-led right, serif h1 left)
  2. pillars (4 cards · "Custodia patrimoniale / Governance familiare /
     Successione strutturata / Compliance fiduciaria")
  3. KPI band (4 stats · the ONE dark band on home, CS-TONE-03)
  4. governance-cycle-strip (mid-strip · the differentiator beat)
  5. sectors-ribbon ("Profili familiari" label)
  6. leadership ("Custodi del mandato" · photo-present · 60s + 40s)
  7. cases ("Mandati in continuità" · 4 anonymized + multi-year)
  8. cta-closer (dark band variant · restates voice anchor)

mid_strip_name:               governance-cycle-strip
mid_strip_composition:        three cells:
                                · Cadenza CdF · 4 riunioni / anno
                                · Audit di continuità · annuale
                                · Patto familiare · revisione triennale
mid_strip_anti_collision:     NOT KPI tuple (these are cadences, not numbers) ·
                              NOT fiscal-calendar (governance not fiscal events) ·
                              NOT percorso-cadenza (multi-year not 8-12 sessions)

home_dark_band_count:         1   # CS-TONE-03 · the KPI band
pillars_count:                4   # CS-DENSITY-02
kpi_count:                    4   # CS-DENSITY-04 · "18 anni · 3 generazioni ·
                                  #   €1.8 B in custodia · 4 riunioni CdF/anno"
leadership_block:             present · rationale: multi-partner stewardship office,
                              NOT solo-practitioner (Solaria precedent only applies
                              to org_scale=1)
```

**Validation**
- [x] `mid_strip_name` fresh (not in any sibling)
- [x] `home_dark_band_count` exactly 1
- [x] Pillars 4 · KPI 4 (within CS-DENSITY-02 / CS-DENSITY-04)
- [x] Leadership present with explicit org-scale rationale

---

## 8 · CTA personality

```
primary_cta_copy:             "Avvia un dialogo di mandato"
                              · NOT a call · NOT an appointment · NOT a discovery
                              · NOT on CS-CTA-02 banlist
conversion_pattern:           mandate-dialogue · multi-year framing
form_gate:                    scope-meeting shape:
                                · scope familiare (free text · 1-2 sentences)
                                · orizzonte temporale (select · 5y / 10y / 25y / multi-gen)
                                · struttura attuale (select · holding / fondazione /
                                  trust / patto di famiglia / nessuna formalizzata)
                              NOT P.IVA + CF (Fiscus's intake) ·
                              NOT NDA-ready boardroom form (Pragma's) ·
                              NOT ICF code-of-ethics referenced (Solaria's)
form_shape_anti_collision:    Continua's intake names a TIME HORIZON, not a fiscal
                              identifier or a session count. The shape is fresh.
```

**Validation**
- [x] CTA copy not banned and not used by any sibling
- [x] `form_gate` does not match any sibling's intake shape
- [x] Hero contains ONE primary CTA at most (CS-PAL-05 implication)

---

## 9 · Multilingual intent

```
initial_locale:                  it
planned_locales:                  [it, en, fr, es, ar]   # cluster default
rtl_required:                    YES                     # ar is in scope

voice_anchor_it:                 "La continuità di una famiglia si misura in <em>generazioni</em>."
em_word_it:                      generazioni
contrast_pair_anchor:            NO                      # default one em-wrap
voice_anchor_translation_note:
    The italic carries the multi-generational time-horizon. Translators MUST
    italicise the word equivalent to "generazioni":
      · EN: "generations"        ("A family's continuity is measured in <em>generations</em>.")
      · FR: "générations"
      · ES: "generaciones"
      · AR: "أجيال"            (post-RTL · check Kufi italic substitute or weight shift)
    Do NOT italicise the verb "misura" or the noun "continuità". The italic is
    on the load-bearing temporal noun.

terminology_locked_pre_translation:
  cluster_terminology_file:      factory/cluster_blueprints/corporate-suite.md (when populated)
                                 OR factory/standards/corporate-suite-design-standard.md §11
  credentials_per_locale:        [
                                   "Albo dei Trustees (Italia)",
                                   "Iscrizione OAM (mediatori creditizi · ove applicabile)",
                                   "STEP Affiliate (international stewardship body)",
                                   "ICAEW / OIC reference for continuity audit",
                                 ]
                                 ALL real, verifiable. NOT invented.
  legal_row_per_locale:          [P.IVA · privacy · cookie · whistleblowing
                                  (D.lgs. 24/2023 · CS-FOOT-02 required for advisory)]

ar_specific:
  heading_font_swap:             "Noto Kufi Arabic"           # CS-TYPE-06
  body_font_swap:                "Amiri"                       # CS-TYPE-06
  latin_wordmark_preserved:      YES                           # CS-NAV-06 / CS-FOOT-03
  letter_spacing_reset:          YES                           # CS-TYPE-05 RTL reset
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
target_scorecard_grade:          ≥ 4.50/5        # 4.67 is precedent
target_blocking_findings:        0/N             # zero open [BLOCKING] before flip

walk_locales:                    [it]            # workflow A initial
walk_viewports:                  [1920, 1440, 1280, 1024, 768, 390]   # CS-RESPONSIVE-02
walk_pages:                      [home, about, services, case_study_list,
                                  case_study_detail, contact]   # CS-BROWSER-01

reviewer_disposition:            "first-of-cluster family-office baseline ·
                                 expected to set the pattern for two future
                                 stewardship variants (notarile · fiduciaria)"

critical_review_dimensions:
  - palette adjacency vs Pragma (cool-on-cool risk)
  - imagery distinctness vs Fiscus (object-led + warm-archive overlap risk)
  - voice anchor preservation (one em-word, not two — Solaria mistake)
  - hero photo subject coherence at 1280/1024 crop (object-led photos
    fail at small viewports more often than people-led ones)
  - leadership block diversity (60s + 40s · NOT 30s × 2 redo)

user_handshake_expectation:      after IT walk PASS, before any locale rollout.
                                 The first sibling in a new sub-cluster carries
                                 higher review cost — a HOLD here is more likely
                                 than for a Nth template in an established sub-cluster.
```

**Validation**
- [x] `target_initial_tier` = draft (D-102)
- [x] 6 viewports · 6 pages listed explicitly
- [x] `critical_review_dimensions` are concrete, not "everything"

---

## 11 · User constraints

```
must_haves:
  - public-record style proof (stewardship-duration · multi-year mandate)
  - object-led hero (zero people · cluster-distinctness move)
  - leadership block PRESENT with photographic representation +
    visible 60s/40s age diversity
  - whistleblowing link in legal row (D.lgs. 24/2023 binding for advisory)

must_avoids:
  - any form gate asking for P.IVA + CF (Fiscus intake collision)
  - any "free trial" / "first call free" framing (banlist + tone collision)
  - any contrast-pair voice anchor (Solaria reservation)
  - any "we transform" / "we unlock" hyperbole (CS-EXEC-04 banlist)

deadline:               none (dry run)
budget_constraints:     skin-budget ~1100 lines · pack 6 Pexels URLs ·
                        no custom photography (CS-IMG-SRC-01)
```

**Validation**
- [x] Must-haves / must-avoids concrete
- [x] No constraint conflicts with cluster invariant (whistleblowing link is
      already CS-FOOT-02 required for advisory; reinforces, doesn't conflict)

---

## 12 · Sign-off summary

```
INTAKE SIGN-OFF · continua-stewardship  (DRY RUN)
=================================================

What this template IS:
    A stewardship-grade family office that custodies a family's
    patrimony across generations, governed via a Family Council
    (Consiglio di Famiglia · CdF), measured in decades and
    generations rather than market cycles.

What this template is NOT:
    NOT Pragma's boardroom-advisory mandate · NOT Fiscus's
    commercialista presidio · NOT Solaria's bounded executive
    coaching. Not a "wealth manager", not a "private banker",
    not a "succession lawyer" — though it works alongside all
    three.

Cluster:                         corporate-suite · family-office multigenerazionale
Nearest siblings:                Pragma (institutional voice neighbour) · Fiscus (object-led adjacency neighbour)

Voice positioning:               stewardship-longitudinal (matrix §1.1 OPEN)
Palette intent:                  deep pine + cool pewter + antique brass (matrix §1.3 OPEN: cool secondary + warm accent)
Typography intent:               Crimson Pro + Public Sans (both in OPEN territory)
Hero meta-strip concept:         stewardship-horizon-strip (Mandato medio · Generazioni · CdF)
Imagery direction:               object-led private reading room (no people · NOT boardroom · NOT desk · NOT 1:1)
Section rhythm claim:            governance-cycle-strip mid-beat (fresh)
CTA personality:                 mandate-dialogue · "Avvia un dialogo di mandato"

Forbidden similarities locked:   31 explicit anti-collision lines (9 vs Pragma · 10 vs Fiscus · 12 vs Solaria)
AI-slop avoidance:               YES across all 13 detector items

Initial locale:                  it
Planned locales:                 [it, en, fr, es, ar]
RTL required:                    YES

User must-haves locked:          4
User must-avoids locked:         4

Open questions for orchestrator:
  - Confirm `Crimson Pro` license/availability vs `PT Serif` / `Spectral` as
    fallback heading serif if Crimson Pro proves cumbersome at h1 size.
    (Not a re-spec; a font-availability check at A.2 to A.5 boundary.)
  - Confirm whistleblowing-link copy convention for stewardship sub-cluster
    (cluster terminology file is partial today).
```

**Sign-off result (dry run)**: every line filled, no blank fields, no
forbidden-similarity blocks empty, distinctness scores triangulate as 5/5
on every existing sibling (cf. `candidate-01-distinctness-proof.md` §2).
The intake is **READY FOR PLANNER** had this been a real candidate.

---

## 13 · After this dry run

This intake is NOT promoted to `factory/reports/<archetype>/continua-stewardship/intake.md`. It stays in `design-orchestrator/dry-runs/` as a system test artefact. The intake's purpose is solely to verify that the checklist produces a concrete, distinct, premium-coded answer when run end-to-end — the assessment of that result lives in this dry-run's closing summary.
