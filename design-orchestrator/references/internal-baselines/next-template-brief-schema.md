# Next-template brief schema

**Status**: operational v1 · **Date**: 2026-04-28
**Purpose**: the form every new corporate-suite sibling planner brief MUST fill out before code starts. Designed so two siblings cannot silently collapse into the same template.
**How to use**: copy this file as `factory/reports/<archetype>/<template-slug>/planner-brief.md` at workflow step A.2 and fill every field. A blank field = an unanswered question = no plan sign-off.
**Companion files**: `corporate-suite-reference-pack.md` · `corporate-suite-distinctness-matrix.md` · `factory/standards/corporate-suite-design-standard.md`.

---

## 0 · Hand-fill rules

- Every field below is **required** unless explicitly marked `optional`.
- Every "MUST NOT" check requires either a YES (compliant) or an explicit waiver with rationale tied to a rule ID.
- Vague answers ("modern", "premium", "professional") are rejected. Answers must be concrete (e.g., "Cormorant Garamond at 56px hero, Source Sans at 17px body").
- The schema is the contract. The orchestrator's plan-gate (workflow A.2) refuses any brief with blank or vague fields.

---

## 1 · Required inputs (intake)

These come from the user's roadmap entry or from workflow A.1 intake.

| Field | Format | Example |
|---|---|---|
| `template_slug` | kebab-case, lowercase | `notario-stewardship` |
| `studio_name` | Italian-readable, single word preferred | "Praesto" |
| `cluster` | one of `corporate-suite` | `corporate-suite` |
| `sub_cluster_label` | one phrase identifying the variant | "studio notarile" / "boutique law" / "fiduciary office" |
| `audience_profile` | who the firm serves · 1-2 sentences | "famiglie imprenditoriali con patrimoni privati medio-alti, atti notarili e successioni" |
| `org_scale` | partner/sole/multi-office count | "1 notaio + 2 praticanti · 1 sede Milano" |
| `locales` | always start IT-only per D-102 | `[it]` (others added in workflow C) |
| `nearest_two_siblings` | the two closest in palette/imagery/voice | "Fiscus (formal-document neighbor) · Pragma (institutional-advisory neighbor)" |
| `user_constraints` | explicit user must-have / must-avoid | "must include public-record proof · must not have any leadership-photo above the fold" |
| `target_tier` | `draft` (D-102 default) | `draft` |
| `pexels_pack_status` | `not started` / `curator briefed` / `pack drafted` / `pack reviewer-approved` | `curator briefed` |
| `motion_profile` | one of the 7 enumerated values (`g1-safe-premium` · `g2-editorial` · `g2-editorial-counter` · `g3-institutional` · `g4-stewardship` · `g5-sprint-console` · `g6-cinematic`) · MUST be in the cluster's allowed-set per `motion-profile-catalog.md §3` · per CS-MOTION-DNA-01 | `g3-institutional` (Pragma-class) · `g2-editorial-counter` (LF-2 2nd-occupant) |

---

## 2 · Forbidden similarities (anti-drift binding)

The planner copies these checks verbatim from `corporate-suite-distinctness-matrix.md` §1 and answers each YES (still distinct) / NO (collides → re-spec required).

For each existing sibling (Pragma · Fiscus · Solaria · plus any new sibling already merged), the planner answers:

```
COLLISION CHECK · vs Pragma
  Tone:                            [YES / NO]   Why:
  Palette polarity:                [YES / NO]   Why:
  Secondary/accent warmth:         [YES / NO]   Why:
  Typography (heading serif):      [YES / NO]   Why:
  Typography (body sans):          [YES / NO]   Why:
  Hero meta-strip composition:     [YES / NO]   Why:
  Hero photography subject:        [YES / NO]   Why:
  CTA copy:                        [YES / NO]   Why:
  Section order (mid-strip):       [YES / NO]   Why:
  Leadership feel:                 [YES / NO]   Why:
  Proof / case style:              [YES / NO]   Why:
  Stakeholder one-liner:           [YES / NO]   Why:
  AXES DIFFERENT (DISTINCTNESS §1, of voice/palette/imagery/typography/structure): __ / 5
  PASS GATE (≥ 4/5): YES / NO
```

Repeat the block for `vs Fiscus` and `vs Solaria`. A NO on any axes-different score blocks plan sign-off.

### 2.1 · Hard prohibitions (no waiver, ever)

- Any URL appearing in another corporate-suite sibling's pool (CS-IMG-SRC-04).
- Inter as body sans for the 4th sibling (Pragma + Solaria already use it · 3-of-4 collapses Inter into the cluster default).
- `--primary-2: #2c3e6b` hardcoded in skin (AP7 · CS-PAL-03).
- Hero meta-strip identical to Pragma's KPI tuple, Fiscus's fiscal-calendar, or Solaria's percorso-cadenza.
- `--primary` palette hex with L\* > 40 on cream paper (CS-PAL-01).
- Lorem ipsum / "Replace this text" / "Your headline here" anywhere (CS-MARKET-02 / CS-MARKET-03).
- Unsplash URLs (Pexels-only · CS-IMG-SRC-01).
- Geometric sans on headings — Montserrat, Poppins, Raleway (CS-TYPE-01).

### 2.2 · Soft prohibitions (waiver allowed with rationale + rule ID)

- Reusing a heading serif another sibling uses (Merriweather / IBM Plex Serif / Fraunces). Waiver allowed only if a different italic-em strategy + different scale ceiling + different heading personality is explicitly justified.
- Skipping the leadership block. Allowed only on solo-practitioner (Solaria precedent).
- Adding a 6th-pillar card to make the pillars feel "richer". Always reject — CS-DENSITY-02 caps at 4.

---

## 3 · Design DNA fields

These populate the new template's `template_dna.py` entry. Fill in every line.

```
template_dna_fields:
  archetype:           "corporate-suite"
  hero_style:          "split-<descriptor>"      # e.g., split-stewardship, split-evidence, split-jurisdiction
  navbar_style:        "<solid|minimal>-<descriptor>"   # e.g., solid-notarile, minimal-archivio
  footer_style:        "sectors-ribbon" | "<custom>"
  section_order:       [list of section beats]   # see §6 for valid options
  card_style:          "pillar-<descriptor>"
  button_style:        "ghost-<descriptor>"      # e.g., ghost-institutional, ghost-stewardship
  density:             "airy"                    # cluster invariant
  tone:                "<descriptor>"            # e.g., stewardship-grave, evidence-precise
  imagery_direction:   "<noun-noun>"             # e.g., notary-chamber, legal-codex
  imagery_key:         "business-<sub>"          # e.g., business-notarile, business-legale
  conversion_pattern:  "<descriptor>"            # e.g., scope-meeting, public-hearing-booking
  font_pairing:        ("<heading-serif>", "<body-sans>")
  palette:
    primary:    "#XXXXXX"                        # L* ≤ 40 on cream (CS-PAL-01)
    secondary:  "#XXXXXX"
    accent:     "#XXXXXX"
  voice_anchor:        "<verbatim sentence with <em>...</em> wrap on the load-bearing word>"
```

### Validation checklist for the DNA fields:
- [ ] `palette.primary` passes `is_primary_safe_on_cream()` (CS-PAL-01).
- [ ] `palette` triple is orthogonal to all three existing siblings (matrix §1.2 · §1.3).
- [ ] `font_pairing` heading-serif is NOT Merriweather, IBM Plex Serif, or Fraunces.
- [ ] `font_pairing` body-sans is NOT Inter (already at 2/3 · enforce variation).
- [ ] `voice_anchor` is a single sentence, contains exactly ONE `<em>` wrap (or two if anchor is a contrast pair · Solaria precedent).
- [ ] `voice_anchor` survives translation to EN/FR/ES/AR with the load-bearing word italicizable.
- [ ] `imagery_direction` is unique to this template (not `executive-boardroom`, `fiscal-desk-documents`, or `coaching-conversation`).
- [ ] `conversion_pattern` is unique (not `private-call`, `appointment-request`, or `discovery-call-booking`).

---

## 4 · Imagery DNA fields

The pack must be authored in `docs/content-factory/imagery/packs/<imagery_key>.md` BEFORE copy starts (workflow A.3 precedes A.4).

```
imagery_pack_fields:
  imagery_key:                "business-<sub>"
  pool_source:                "Pexels"          # CS-IMG-SRC-01 — no other source allowed
  pool_size:                  6                 # CS-IMG-POOL-01 cluster contract
  slot_0_hero:
    pexels_url:               "https://images.pexels.com/photos/.../...jpeg?auto=compress&cs=tinysrgb&w=1600"
    pexels_id:                <int>
    photographer:             "<name>"
    subject:                  "<one-line>"      # e.g., "notary chamber with codex spread on oak desk, no people"
    mood:                     "<one-line>"      # e.g., "warm afternoon light, deep DoF, object-led"
    coherence_note:           "<why this matches the cluster's stewardship tone>"
    license:                  "Pexels CC0"
  slot_1_feature:    {...}
  slot_2_portrait:   {...}    # ≥ 800×800 · square-ish · no gray-silhouette placeholder
  slot_3_portrait:   {...}    # different person from slot_2
  slot_4_detail:     {...}    # close-up of the work itself (codex, seal, ledger, etc.)
  slot_5_ambient:    {...}    # environmental shot — not bookshelf (Fiscus took it)

  imagery_distinctness:
    vs_pragma:    [list of 6 reasons: "slot 0 differs in: subject (object-led not boardroom) · mood (afternoon not boardroom-cool) · subject density (0 people not 4)"]
    vs_fiscus:    [list of 6 reasons]
    vs_solaria:   [list of 6 reasons]
  cross_cluster_grep_clean:    YES / NO   # no URL appears in another cluster's pool
```

### Validation checklist:
- [ ] All 6 URLs are `images.pexels.com/photos/...` — no other domain.
- [ ] `w=` query param matches slot budget (`hero=1600`, `feature=1200`, others `=800`).
- [ ] No URL appears in `business-corporate`, `business-fiscal`, or `business-coaching` (CS-IMG-SRC-04 grep).
- [ ] Hero photo subject is NOT boardroom long-table, tidy desk + documents, or 1:1 conversation.
- [ ] Portrait pair shows visible diversity (age / gender / ethnicity) — no Solaria-style 30s Caucasian × 2.
- [ ] Ambient slot is NOT a bookshelf (Fiscus's slot 5).
- [ ] Pack is reviewer-approved per CURATION_PROTOCOL §6 BEFORE copy step starts.

---

## 5 · Section rhythm DNA fields

```
section_rhythm:
  home_page_order:
    1: "hero"                     # CS-HERO-01 · cluster invariant · 55/45 split
    2: "<pillars | manifesto>"    # one of two openers; pillars 3-4 cards CS-DENSITY-02
    3: "<percorsi | competenze>"  # optional, only if `manifesto` chosen at 2
    4: "kpi-band"                 # CS-RHYTHM-03 · the ONE dark band on home
    5: "<mid-strip-name>"         # the differentiator beat — NEW invention required
    6: "sectors-ribbon"           # cluster pattern · label is differentiator (e.g., "Profili dei coachee")
    7: "<leadership | omitted>"   # present iff org_scale > 1 partner; omitted otherwise (Solaria precedent)
    8: "cases"                    # 3-6 anonymized · CS-DENSITY-06
    9: "cta-closer"               # dark or tinted · restates voice anchor · CS-CTA-05

  mid_strip_name:                 "<unique invented label>"
  mid_strip_composition:          "<the three cells that compose it>"
  mid_strip_anti_collision:       "different from KPI tuple (Pragma) · fiscal-calendar (Fiscus) · percorso-cadenza (Solaria) because: <reason>"

  about_page_opener:              "timeline" | "<custom>"  # never "wall of text" — CS-COMP-06
  contact_page_layout:            "form-left + coordinates-right · stacks at 880px"  # CS-COMP-05 cluster contract
  case_detail_order:              [list]    # default: kpi-strip + narrative + team-strip + next-case · adding a slot is the differentiator (Solaria added method-context)
```

### Validation checklist:
- [ ] Home has exactly ONE dark band (the KPI band at position 4 · CS-TONE-03).
- [ ] No two adjacent sections share function (CS-RHYTHM-04).
- [ ] Mid-strip composition is NOT identical to any sibling's mid-strip.
- [ ] Pillars/percorsi count is 3 or 4 (CS-DENSITY-02).
- [ ] KPI count is 3 or 4 (CS-DENSITY-04).
- [ ] If `leadership` is omitted, the planner brief includes a one-line rationale citing the org scale.

---

## 6 · Distinctness proof fields

These are the explicit "why this is not a fourth flavor" answers. The planner writes them; the orchestrator reads them at sign-off.

```
distinctness_proof:
  one_line_summary:                "<single sentence the orchestrator can write at intake>"
  what_this_is_NOT_mistakable_for: "<list of 3-5 things this sibling CAN'T be confused with>"

  axes_different_score:
    vs_pragma:    "X/5"   # must be ≥ 4
    vs_fiscus:    "X/5"   # must be ≥ 4
    vs_solaria:   "X/5"   # must be ≥ 4

  the_three_strongest_distinctions:
    1: "<dimension + how this template differs>"
    2: "<dimension + how this template differs>"
    3: "<dimension + how this template differs>"

  the_two_residual_overlap_risks:
    1: "<dimension + which sibling + why this is not a collision>"
    2: "<dimension + which sibling + why this is not a collision>"

  remove_studio_name_test:        "<does the page still work as a real firm's site? what evidence?>"
  AI_slop_red_flags_clear:        YES / NO   # see reference-pack §9
```

### Validation checklist:
- [ ] `one_line_summary` is not a paraphrase of an existing sibling's summary.
- [ ] All three `axes_different` scores are ≥ 4/5.
- [ ] Both residual risks have a stated reason for not being collisions.
- [ ] `AI_slop_red_flags_clear` is YES (no Inter h1, no purple gradients, no cards-in-cards, etc.).

---

## 7 · Multilingual intent fields

IT ships first per D-102. Locales beyond IT enter via workflow C. The brief captures intent so the locale rollout doesn't surprise the translator.

```
multilingual_intent:
  initial_locale:                 "it"          # always
  planned_locales:                [it, en, fr, es, ar]   # cluster default
  rtl_required:                   YES           # cluster default · ar requires it
  voice_anchor_strategy:
    it_anchor:                    "<verbatim IT sentence with <em>>"
    em_word:                      "<the load-bearing word that carries italic>"
    translation_note:             "<note for translators on which word to italicize post-translation>"
    contrast_pair_anchor:         YES / NO      # if YES, two em-wraps allowed (Solaria precedent)

  terminology_locked_pre_translation:
    cluster_terminology_file:     "factory/cluster_blueprints/<cluster>.md §<n> terminology"
    credentials_per_locale:       [list — must be verifiable]
    legal_row_per_locale:         [P.IVA · privacy · cookie · whistleblowing? per cluster]

  ar_specific_requirements:
    heading_font_swap:            "Noto Kufi Arabic"      # CS-TYPE-06
    body_font_swap:               "Amiri"                 # CS-TYPE-06
    latin_wordmark_preserved:     YES                     # CS-NAV-06 / CS-FOOT-03
    letter_spacing_reset:         YES                     # CS-TYPE-05 RTL reset 0.22em → 0
    rtl_layout_via_logical_props: YES                     # CS-RESPONSIVE-08
```

### Validation checklist:
- [ ] IT anchor is a single sentence with a clear load-bearing word.
- [ ] Italian translator brief identifies the em-word so EN/FR/ES/AR translations preserve emphasis on the equivalent word.
- [ ] AR locale has `dir="rtl"` planning + Kufi/Amiri swap planning + Latin wordmark preservation.
- [ ] Cluster terminology file is referenced for credentials/legal-row vocabulary.

---

## 8 · Browser verification fields

The planner brief commits to the verification matrix BEFORE the build starts. The browser-verifier reads these at workflow A.7.

```
browser_verification_intent:
  rubric_file:                    "factory/standards/corporate-suite-browser-rubric.md"
  walk_locales:                   [it]                                  # workflow A initial · others come at C
  walk_viewports:                 [1920, 1440, 1280, 1024, 768, 390]    # CS-RESPONSIVE-02
  walk_pages:                     [home, about, services, case_study_list, case_study_detail, contact]   # CS-BROWSER-01

  per_page_checks:
    no_horizontal_scroll:         YES at every viewport
    hero_h1_contrast_AAA:         YES on cream                          # CS-HERO-03
    one_dark_band_on_home:        YES (KPI band only)                   # CS-TONE-03
    accent_count_per_viewport:    "≤ 3"                                 # CS-PAL-05
    focus_visible_keyboard_walk:  YES (every interactive element shows gold ring)   # CS-NAV-02
    locale_switcher_functional:   YES (lang+dir per link)               # CS-NAV-03
    cta_targets_real_routes:      YES (no `href="#"`)                   # CS-CTA-04
    editor_affordances_hidden:    YES (no halos in /live/)              # CS-MARKET-01

  artefacts:
    screenshot_dir:               "factory/reports/browser-verification/<template-slug>/"
    walk_log_file:                "factory/reports/browser-verification/<template-slug>/walk-log-<date>.md"
    dev_server_url_recorded:      YES (per CS-BROWSER-02)
```

### Validation checklist:
- [ ] All 6 viewports listed.
- [ ] All 6 page kinds listed.
- [ ] Walk artefacts directory pre-allocated.
- [ ] Reduced-motion run scheduled (separate pass, often combined with locale walks).

---

## 9 · Release-gate expectations

The release-gatekeeper reads these at workflow A.9.

```
release_gate_expectations:
  scorecard_file:                 "factory/reports/scorecard/<template-slug>/scorecard.md"
  scorecard_template:             "factory/standards/corporate-suite-quality-scorecard.md"

  blocking_rules_to_pass:         [list of every CS-* [BLOCKING] rule from corporate-suite-design-standard.md]
  required_rules_to_pass:         [list of CS-* [REQUIRED] rules]
  strong_deviations_documented:   [list of any [STRONG] rules with `§ design deviation` justification in module docstring]

  initial_tier:                   "draft"                # D-102 cadence
  tier_flip_to_live_requires:     [
    "5/5 locale walks PASS",
    "0/N blocking findings",
    "user handshake on screencast",
    "release-gatekeeper countersign on scorecard"
  ]

  user_handshake_artefact:        "factory/reports/<template-slug>/user-handshake-<date>.md"
  evidence_retention_path:        "factory/reports/<template-slug>/"

  scorecard_deliverable:
    overall_grade:                "X.YY/5"          # ≥ 4.50 to flip · ≥ 4.67 is precedent
    blocking_findings:            "0/N"             # 0 to flip
    walk_verdicts:                "Y/Y locales PASS"
```

### Validation checklist:
- [ ] Scorecard file pre-allocated at planner step.
- [ ] All [BLOCKING] rule IDs from `corporate-suite-design-standard.md` are in the must-pass list.
- [ ] Initial tier is `draft` (per D-102).
- [ ] Tier-flip preconditions are explicit and measurable.
- [ ] User-handshake artefact path pre-allocated.

---

## 10 · The single-page summary the orchestrator reads at sign-off

Every planner brief ends with this 1-page summary. If it cannot be filled in coherently, the brief is incomplete.

```
PLAN SIGN-OFF SUMMARY · <template-slug>
=========================================

What this template is: <one sentence>

What this template is NOT: <one sentence — references siblings explicitly>

Voice anchor (IT, verbatim, with <em>): "<sentence>"

Palette: primary <hex> · secondary <hex> · accent <hex>
Macro tone: <descriptor>

Typography: <heading-serif> + <body-sans>

Hero: 55/45 split + photo subject "<line>" + meta-strip "<line>"
CTA: "<copy>" → <conversion pattern>

Section moves that distinguish this from siblings:
  1. <move>
  2. <move>
  3. <move>

Distinctness scores:
  vs Pragma:  X/5
  vs Fiscus:  X/5
  vs Solaria: X/5
  GATE:       PASS / FAIL

Imagery pack: <imagery_key> · curator-approved YES/NO · 6 URLs Pexels-only YES/NO

Initial locale: it (others at workflow C)
Initial tier: draft

Browser walk plan: 6 viewports × 1 locale (it) × 6 pages
Walk artefact dir: <path>

Scorecard expected grade: ≥ 4.50/5

Open questions for orchestrator:
  - <question or "none">
```

The orchestrator signs off ONLY if every line is filled, all distinctness scores are ≥ 4/5, and no hard prohibitions are flagged.

---

## 11 · Schema maintenance

- This schema is versioned alongside the cluster's design standard.
- A cluster-level rule change (e.g., a new `[BLOCKING]` rule in `corporate-suite-design-standard.md`) propagates here in the next planner brief.
- The schema fields are minimum required, not maximum allowed. A sibling can document additional invariants in its docstring without changing the schema.
