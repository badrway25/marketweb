# Template intake checklist

The reusable intake form for every future template. Filled at workflow A.1 (single-template) or batch phase 1 (batch). The orchestrator does not approve a planner-brief request without this checklist filled.

This checklist captures the ANSWER to "what is this template, and what does it specifically refuse to be?" — BEFORE the planner spec, the imagery pack, or any code. A blank field here is an unanswered question the rest of the pass will fail to recover.

Companion files: `next-template-brief-schema.md` (the planner contract this checklist feeds) · `corporate-suite-distinctness-matrix.md` (the matrix the brief scores against) · `template-orchestrator-master.md` (the master prompt this checklist precedes) · `pre-build-quick-checks.md` (the five micro-gates from §0.5, §3, §6.5, §7, §12 below — runs in ~15 minutes total).

---

## How to use

1. Copy this file to `factory/reports/<archetype>/<template_slug>/intake.md` at the start of a new template's workflow A pass.
2. Fill every field. A blank or vague field ("modern", "premium", "professional") is a fail — the orchestrator will reject the intake and ask for specifics.
3. The completed checklist is read by the planner at A.2 and becomes part of the template's permanent record.

---

## 0.5 · Cluster reference-pack precondition (run first · pre-build-quick-checks.md §1)

Before filling anything else, confirm this template's cluster has the two reference files needed to triangulate distinctness. Without them, every downstream score is meaningless.

```
cluster:                          <copied from §1 below>
cluster_reference_pack_exists:    <YES | NO · path: design-orchestrator/references/internal-baselines/<cluster>-reference-pack.md>
cluster_distinctness_matrix_exists: <YES | NO · path: design-orchestrator/references/internal-baselines/<cluster>-distinctness-matrix.md>
proceed_decision:                 <CONTINUE | HALT-build-pack-first | USER-WAIVER>
```

**Validation:**
- [ ] Both files exist for this cluster, OR cluster is `corporate-suite` (the only cluster with a complete pack today)
- [ ] If cluster is anything else and either file is missing, the pass HALTS at intake until the pack is built (separate one-off pass · same shape as the corporate-suite reference pack and matrix)
- [ ] If a `USER-WAIVER` is recorded, paste the user's exact authorising sentence here verbatim

**If decision is HALT**: stop the intake. Do not score §3 distinctness against an empty grid. The next pass builds the cluster's reference pack first; this template's intake resumes after.

---

## 1 · Identity

```
template_slug:           <kebab-case · lowercase · alphanumeric + dash>
studio_name:             <single word preferred · brand-readable>
cluster:                 <corporate-suite | medical-specialist | restaurant | portfolio | ecommerce | real-estate | law | agency | startup-saas | medical-other>
sub_cluster_label:       <one phrase identifying the variant · e.g. "studio notarile" / "boutique law" / "fiduciary office">
archetype:               <archetype slug · matches the existing archetype taxonomy>
```

**Validation:**
- [ ] `template_slug` is unique across the catalog (grep `TEMPLATE_REGISTRY.json` first)
- [ ] `studio_name` does not echo an existing template's brand name
- [ ] `cluster` matches one of the live cluster identifiers
- [ ] `sub_cluster_label` is concrete enough to triangulate against (not "professional firm", but "studio notarile")

---

## 2 · Cluster · archetype context

```
existing_siblings_in_cluster:    <list every existing template in this cluster>
nearest_two_siblings:            <the two nearest in palette · imagery · voice — the triangulation anchors>
cluster_invariant_summary:       <one-line restatement of the cluster's invariant from DISTINCTNESS_RULES.md §3>
archetype_position:              <which sub-cluster slot this fills · e.g. "4th corporate-suite · 2nd notarile">
cluster_reference_pack_path:     <path to the cluster's reference pack · or "none yet · falls back to corporate-suite + per-sibling DNA">
distinctness_matrix_path:        <path to the cluster's distinctness matrix · or "none yet · use corporate-suite as baseline">
```

**Validation:**
- [ ] Every existing sibling is named (not "all the others" — explicit list)
- [ ] `nearest_two_siblings` is unambiguous — if you cannot name them, the cluster is too thin or this template's identity is unclear
- [ ] Cluster invariant is restated correctly (re-read the matrix to confirm)

---

## 3 · Desired differentiation

This is the load-bearing section of the entire intake. The planner will score this template against these claims at A.2; if the claims are vague, the score will collapse.

```
one_line_pitch:                  <one sentence the orchestrator can write at intake — "what this template IS">
voice_positioning:               <a stance, not a synonym for the cluster's existing stances · see corporate-suite-distinctness-matrix.md §1.1 "Open stances">
palette_intent:                  <a hue family + warm/cool strategy + adjacency NOT to take · concrete e.g. "deep forest green + brass + cream · cool-secondary + warm-accent">
typography_intent:               <heading serif + body sans candidates · cite open territory from the cluster reference pack §5>
hero_meta_strip_concept:         <a fresh proof-shape composition · NOT KPI tuple / fiscal-calendar / percorso-cadenza / any sibling's existing shape>
imagery_direction:               <subject + mood + density · concrete e.g. "object-led codex spread on desk · no people · warm afternoon light">
section_rhythm_claim:            <which mid-strip beat this template owns · e.g. "jurisdiction-strip" / "licensure-timeline" / "audit-cadence">
proof_style:                     <numeric KPI · public-record · stewardship-duration · audit-trail · etc. — concrete>
cta_personality:                 <conversion shape · e.g. "scope-meeting" / "public-hearing-booking" / "custodial-onboard">
stakeholder_first_30s_read:      <one sentence describing how a first-time visitor reads the page in 30 seconds · MUST not echo any existing sibling's first-30s read>
```

**Validation:**
- [ ] Every field is concrete (no "modern", "premium", "professional", "elegant" without specific operational vocabulary)
- [ ] `voice_positioning` is on the cluster's open-stances list, not on the taken-stances list
- [ ] `palette_intent` is in the cluster's open palette territory
- [ ] `hero_meta_strip_concept` is NOT one of the existing siblings' compositions
- [ ] `stakeholder_first_30s_read` could not plausibly describe any existing sibling

### 3.1 · Palette warmth/coolness conflict check (pre-build-quick-checks.md §2)

Hex-distinct palettes can still read as siblings if the warm/cool topology matches. Fill this 2×3 grid for the proposed palette and for each existing sibling, then check overlap.

```
proposed_palette_temperature:
  primary:    <warm | cool | neutral>
  secondary:  <warm | cool | neutral>
  accent:     <warm | cool | neutral>

sibling_temperature_grids:
  <sibling_1>:  primary=<...> · secondary=<...> · accent=<...>
  <sibling_2>:  primary=<...> · secondary=<...> · accent=<...>
  # repeat for every existing sibling

overlap_count_per_sibling:
  vs_<sibling_1>:   <0 | 1 | 2 | 3>
  vs_<sibling_2>:   <0 | 1 | 2 | 3>

palette_warmth_decision:    <PASS · CAUTION · RESPEC>
```

**Validation:**
- [ ] Every existing sibling's temperature grid is filled (read it from the sibling's `template_dna.py` and the cluster reference pack §4)
- [ ] If `overlap_count_per_sibling` is 2 or 3 against ANY sibling → **RESPEC** (flip secondary or accent temperature) before continuing
- [ ] 0 or 1 overlap against every sibling → continue

### 3.2 · "Remove the studio name" pre-test (pre-build-quick-checks.md §5)

Write the proposed `stakeholder_first_30s_read` three times. If versions B and C still uniquely describe THIS template, the differentiation lives in the structure, not the brand-name lift.

```
A · with the studio name as written:
    "<sentence>"

B · with the studio name removed:
    "[___] <sentence>"

C · with the studio name swapped to a generic placeholder:
    "Acme <cluster_label> <sentence>"

studio_name_swap_verdict:    <PASS · RESPEC>
```

**Validation:**
- [ ] B and C still uniquely describe this template (cannot be claimed by Pragma · Fiscus · Solaria · or any sibling) → PASS
- [ ] B or C reads as a generic cluster description any sibling could claim → **RESPEC** (the voice anchor, palette, hero meta-strip, or section rhythm has to do more lifting)
- [ ] This same test is re-run on the planner brief §10 single-page summary at A.2 sign-off

---

## 4 · Forbidden similarities (anti-drift binding)

For each existing sibling in this cluster, name the explicit similarities this template will NOT produce. This list is appended to the planner brief and copied verbatim into the template's content-module docstring (CS-EXEC-02 equivalent).

```
forbidden_similarities:
  vs_<sibling_1>:
    - <similarity to refuse>
    - <similarity to refuse>
    - <similarity to refuse>
  vs_<sibling_2>:
    - <similarity to refuse>
    - <similarity to refuse>
    - <similarity to refuse>
  # repeat for every existing sibling

cluster_level_red_lines:
  - <invariant the cluster maintains — what this template MUST NOT erode>
  - <invariant the cluster maintains — what this template MUST NOT erode>

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

**Validation:**
- [ ] At least 3 forbidden similarities listed per existing sibling
- [ ] `cluster_level_red_lines` cites concrete invariants (not "it should feel premium")
- [ ] Every `ai_slop_avoidance` item is explicitly `NO`

---

## 5 · Tone

```
tone_descriptor:           <2-3 word descriptor · e.g. "stewardship-grave" / "evidence-precise" / "longitudinal-care">
register:                  <Italian register · "Lei + partner vocab" / "noi declarative" / etc.>
stance:                    <the firm-client relationship framing · how the firm positions itself>
emphasis_convention:       <how the page emphasises · serif italic-em on load-bearing word per CS-TYPE-02 cluster contract>
hyperbole_banlist_check:   YES   # confirms CS-EXEC-04 banlist will be respected
```

**Validation:**
- [ ] `tone_descriptor` is not used by any existing sibling
- [ ] `register` is concrete (not "professional")
- [ ] `stance` is differentiated from existing sibling stances
- [ ] Emphasis stays within cluster contract (italic-em, not bold or uppercase)

---

## 6 · Imagery mood

```
imagery_key:                  <kebab-case · matches docs/content-factory/imagery/packs/<key>.md>
hero_subject:                 <concrete subject · e.g. "notary chamber with codex spread on oak desk, no people">
hero_mood:                    <concrete mood · e.g. "warm afternoon light, deep DoF, object-led, no smiles">
hero_color_temperature:       <warm | cool | neutral · with adjective>
hero_subject_density:         <0 people | 1-2 people | 1-4 people | object-led-only>
ambient_subject:              <slot 5 ambient · NOT bookshelf if Fiscus already took it · e.g. "atrium with morning light" / "conservation-laboratory bench">
portrait_diversity_intent:    <visible variation in age / gender / ethnicity · explicit "different from Solaria's 30s Caucasian × 2">
detail_subject:               <slot 4 detail · what we do close-up · e.g. "wax seal on parchment" / "audit-trail spreadsheet detail">
sources_only:                 Pexels   # CS-IMG-SRC-01 binding · no Unsplash · no AI imagery · no custom photography
cross_cluster_grep_intent:    YES      # curator runs the grep before committing any URL
```

**Validation:**
- [ ] `hero_subject` is NOT one of the existing siblings' hero subjects
- [ ] `ambient_subject` is NOT bookshelf if Fiscus exists
- [ ] `portrait_diversity_intent` is named explicitly
- [ ] `sources_only` is `Pexels` (the only documented exception is Pragma legacy; no second exception without user-signed waiver)

### 6.5 · Imagery feasibility quick-search (pre-build-quick-checks.md §3)

Before A.3 commits any URL, the orchestrator runs ONE Pexels search per declared slot subject and counts plausible candidates. Five minutes of search beats a half-day of pack rework. Performed AFTER planner brief sign-off (A.2) but BEFORE the curator commits at A.3 — record the result here at intake so the brief inherits the feasibility envelope.

```
slot_feasibility:
  hero:       search="<concrete keyword phrase>" · plausible_candidates=<count> · verdict=<GO · CAUTION · RESPEC>
  feature:    search="<...>" · plausible_candidates=<count> · verdict=<...>
  portrait:   search="<...>" · plausible_candidates=<count> · verdict=<...>
  ambient:    search="<...>" · plausible_candidates=<count> · verdict=<...>
  detail:     search="<...>" · plausible_candidates=<count> · verdict=<...>
  closer:     search="<...>" · plausible_candidates=<count> · verdict=<...>

overall_pack_feasibility:    <GO · CAUTION · RESPEC>
```

**Validation:**
- [ ] Every slot has ≥ 5 plausible candidates → GO
- [ ] Any slot has 3-4 candidates → CAUTION (continue, but flag the slot as "narrow pool")
- [ ] Any slot has ≤ 2 candidates → **RESPEC the imagery direction** at A.2 before A.3 begins · do NOT enter A.3 with an infeasible slot

---

## 7 · Section rhythm

```
home_section_order:           <list of beats · e.g. "hero · pillars · KPI · jurisdiction-strip · sectors · cases · CTA">
mid_strip_name:               <unique invented label · NOT KPI / fiscal-calendar / percorso-cadenza>
mid_strip_composition:        <the three cells that compose it>
mid_strip_anti_collision:     <one sentence: "different from <each sibling's mid-strip> because <reason>">

home_dark_band_count:         1   # CS-TONE-03 cluster invariant — exactly one dark band on home (the KPI band)
pillars_count:                <3 or 4 · CS-DENSITY-02>
kpi_count:                    <3 or 4 · CS-DENSITY-04>
leadership_block:             <present | absent · with rationale tied to org_scale>
```

**Validation:**
- [ ] `mid_strip_name` is fresh (not in any sibling's section rhythm)
- [ ] `home_dark_band_count` is exactly 1
- [ ] `pillars_count` and `kpi_count` are within their bands
- [ ] If `leadership_block` is `absent`, the rationale references the org scale (Solaria precedent: solo-practitioner)

### 7.1 · Content-volume estimate (pre-build-quick-checks.md §4)

Estimate the home-page rendered word budget per beat. Locks the working envelope before A.4 copy authoring inherits it. Reference budget for corporate-suite (Pragma · Fiscus · Solaria averages); other clusters extrapolate from sibling renders ±20% for verticality.

```
word_budget_estimate:
  hero_h1_plus_sub:        <25-45>
  hero_meta_strip:         <30-60>
  pillars:                 <240-400>     # 60-100 words per pillar body × 3 or 4
  kpi_band:                <60-120>
  mid_strip:               <120-240>
  sectors_or_vertical:     <80-160>
  leadership_block:        <0 if absent · 120-240 if present>
  cases_or_proof:          <240-400>
  cta_closer:              <40-80>

home_total_estimate:       <sum>
cluster_typical_range:     <e.g. corporate-suite: 1500-2500>
volume_decision:           <CONTINUE · RESPEC-sparse · RESPEC-wall · RESPEC-skewed>
top_heaviest_beat:         <beat name · % of total>
```

**Validation:**
- [ ] `home_total_estimate` falls inside the cluster's typical range → CONTINUE
- [ ] `home_total_estimate` < 70% of cluster floor → **RESPEC-sparse** (the page will read editorial-thin · rhythm flattens)
- [ ] `home_total_estimate` > 130% of cluster ceiling → **RESPEC-wall** (CS-COMP-06 wall-of-text trip)
- [ ] One beat takes > 50% of total → **RESPEC-skewed** (CS-RHYTHM-04 risk · two adjacent sections of similar function)

---

## 8 · CTA personality

```
primary_cta_copy:                <verbatim CTA text · NOT "Fissa una call privata" / "Primo appuntamento" / "Prenota una discovery call" / "Get started free" / "Sign up now">
conversion_pattern:              <e.g. "scope-meeting" / "public-hearing-booking" / "custodial-onboard" / "mandate-brief-upload">
form_gate:                       <what the form asks for · e.g. "P.IVA + scope" / "atto-type + parties" / "case-jurisdiction">
form_shape_anti_collision:       <if any sibling shares a form pattern, name it and explain why this is not a collision>
```

**Validation:**
- [ ] `primary_cta_copy` is not on the banned list (CS-CTA-02) and is not used by any sibling
- [ ] `form_gate` does not exactly match any sibling's intake shape
- [ ] CTA is not three-buttons-in-hero (CS-PAL-05 implication)

---

## 9 · Multilingual intent

```
initial_locale:                  it
planned_locales:                 [it, en, fr, es, ar]   # cluster default · adjust if cluster differs
rtl_required:                    YES                     # YES if ar is in planned_locales
voice_anchor_it:                 "<verbatim sentence with one or two <em> wraps>"
em_word_it:                      <the load-bearing word that carries the italic>
contrast_pair_anchor:            <YES | NO · YES only if anchor is built on a contrast pair, Solaria precedent>
voice_anchor_translation_note:   <note for translators on which word to italicize post-translation>

terminology_locked_pre_translation:
  cluster_terminology_file:      <path to the cluster's terminology guide>
  credentials_per_locale:        [list — must be verifiable, not invented]
  legal_row_per_locale:          [P.IVA · privacy · cookie · whistleblowing? per cluster]

ar_specific:
  heading_font_swap:             "Noto Kufi Arabic"           # CS-TYPE-06
  body_font_swap:                "Amiri"                       # CS-TYPE-06
  latin_wordmark_preserved:      YES                           # CS-NAV-06 / CS-FOOT-03
  letter_spacing_reset:          YES                           # CS-TYPE-05 RTL reset 0.22em → 0
  rtl_layout_via_logical_props:  YES                           # CS-RESPONSIVE-08
```

**Validation:**
- [ ] `voice_anchor_it` is a single sentence with one (or two if contrast-pair) `<em>` wrap
- [ ] `em_word_it` is named explicitly so translators can identify the equivalent
- [ ] AR-specific path is wired in the skin BEFORE workflow C begins
- [ ] Credentials per locale are real, not invented translations

---

## 10 · Review expectations

```
target_initial_tier:             draft           # D-102 cadence · always start at draft
target_eventual_tier:            published_live  # the goal · arrived at via release-decision-orchestrator after the multilingual rollout
target_scorecard_grade:          ≥ 4.50/5        # 4.67/5 is precedent
target_blocking_findings:        0/N             # zero open [BLOCKING] before any flip

walk_locales:                    [it]            # workflow A initial · others come at workflow C
walk_viewports:                  [1920, 1440, 1280, 1024, 768, 390]   # CS-RESPONSIVE-02 · adjust per cluster
walk_pages:                      [home, about, services, case_study_list, case_study_detail, contact]   # CS-BROWSER-01

reviewer_disposition:            <expected · "draft for internal review" / "premium reference candidate" / "first-of-cluster baseline">
critical_review_dimensions:      <which dimensions the reviewer will scrutinise hardest · e.g. "imagery distinctness vs Solaria · palette adjacency vs Fiscus">

user_handshake_expectation:      <when the user expects to be asked for parallel-walk sign-off · e.g. "after IT walk PASS" / "after multilingual rollout">
```

**Validation:**
- [ ] `target_initial_tier` is `draft` (D-102 cadence is non-negotiable)
- [ ] `walk_viewports` and `walk_pages` are listed explicitly
- [ ] `critical_review_dimensions` cite concrete dimensions, not "everything"

---

## 11 · User constraints

```
must_haves:           <explicit user must-have items · e.g. "must include public-record proof" / "must surface ICF-PCC credential">
must_avoids:          <explicit user must-avoid items · e.g. "no leadership-photo above the fold" / "no NDA-anonymized framing">
deadline:             <if any · YYYY-MM-DD · or "none">
budget_constraints:   <skin-budget / imagery-budget / scope cap · or "none">
```

**Validation:**
- [ ] Every must-have / must-avoid is concrete (not "should be premium")
- [ ] Constraints that conflict with the cluster invariant are surfaced (the cluster wins; user constraints that violate invariants need a re-scope conversation, not a silent waiver)

---

## 12 · Sign-off summary

The orchestrator reads this single block at sign-off. If it cannot be filled coherently, the intake is incomplete.

```
INTAKE SIGN-OFF · <template_slug>
=================================

What this template IS:           <one sentence>
What this template is NOT:       <one sentence — references siblings explicitly>

Cluster:                         <cluster · sub_cluster_label>
Cluster reference pack:          <CONTINUE · HALT · USER-WAIVER>     (§0.5)
Nearest siblings:                <two named siblings>

Voice positioning:               <stance · not in taken list>
Palette intent:                  <family + warm/cool · in open territory>
Palette warmth grid:             <PASS · CAUTION · RESPEC>           (§3.1)
Studio-name swap pre-test:       <PASS · RESPEC>                      (§3.2)
Typography intent:               <heading serif + body sans · in open territory>
Hero meta-strip concept:         <fresh composition>
Imagery direction:               <hero subject · not in taken list>
Imagery feasibility:             <GO · CAUTION · RESPEC>              (§6.5)
Section rhythm claim:            <mid-strip name · fresh>
Content-volume estimate:         <CONTINUE · RESPEC-sparse · RESPEC-wall · RESPEC-skewed>  (§7.1)
CTA personality:                 <conversion pattern + copy · not in taken list>

Forbidden similarities locked:    <count of explicit anti-collision lines>
AI-slop avoidance:                YES across all 13 detector items

Initial locale:                   it
Planned locales:                  <list>
RTL required:                     <YES | NO>

User must-haves locked:           <count>
User must-avoids locked:          <count>

Open questions for orchestrator:
  - <question or "none">
```

The orchestrator REJECTS sign-off if any of the five pre-build quick-checks (§0.5 · §3.1 · §3.2 · §6.5 · §7.1) ends in HALT or RESPEC. The check has to be cleared (or, for §0.5, explicitly user-waived) before the planner brief can begin.

The orchestrator signs off ONLY if every line is filled, no forbidden-similarity blocks are empty, and `Open questions` is either empty or contains questions that genuinely require user input rather than agent improvisation.

---

## 13 · After sign-off

The signed checklist is the input to the planner brief at workflow A.2. The planner reads this checklist verbatim, expands each field into the planner brief schema's matching field, and produces the triangulation matrix on top.

If the planner cannot expand a field because it is too vague, the planner returns the brief to intake — they are NOT to invent answers. The intake's specificity is the planner's input contract.

The signed checklist becomes part of the template's permanent record at `factory/reports/<archetype>/<template_slug>/intake.md` and is referenced by every subsequent workflow B and C pass on this template.
