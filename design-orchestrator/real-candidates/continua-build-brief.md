# Continua · Build brief · REAL CANDIDATE (implementation-ready)

**Status**: build-ready · planner-brief equivalent · ready to hand to a real workflow A.2 → A.5 session
**Cluster**: corporate-suite · 4th sibling · 1st family-office variant
**Filed by**: orchestrator · `phase-x4-design-orchestrator-hardening-v1` branch
**Date**: 2026-04-29
**Companion files**: `continua-intake.md` (input contract) · `continua-distinctness-proof.md` (gate evidence) · `continua-browser-gate.md` (verification plan)
**Promotion path on first build**: this file → `factory/reports/corporate-suite/continua-stewardship/planner-brief.md`

This brief is concrete enough to start the build immediately. Every field is decision-locked. Where the brief leaves a tactical choice (e.g. heading-serif fallback if Crimson Pro is licence-cumbersome), the choice is named and bounded — not deferred.

---

## 1 · Required inputs (intake summary)

| Field | Value |
|---|---|
| `template_slug` | `continua-stewardship` |
| `studio_name` | Continua |
| `cluster` | `corporate-suite` |
| `sub_cluster_label` | family-office multigenerazionale (governance-led) |
| `audience_profile` | Famiglie imprenditoriali · holding di partecipazioni · fondazioni di famiglia · seconde generazioni in trasferimento. Patrimoni privati medio-alti con governance multigenerazionale, mandato di custodia su decadi, non gestione di portafoglio infra-annuale. |
| `org_scale` | 3 stewards · 1 sede principale (Milano) · multi-partner stewardship office (NOT solo-practitioner — Solaria's "absent leadership" precedent does not apply) |
| `locales` | `[it]` · others enter via workflow C |
| `nearest_two_siblings` | Pragma (institutional-voice neighbour) · Fiscus (object-adjacent imagery neighbour) |
| `user_constraints` | see `continua-intake.md §11` (6 must-haves · 6 must-avoids) |
| `target_tier` | `draft` · D-102 cadence |
| `pexels_pack_status` | `not started` (curator briefed by this file at A.3 entry) |

---

## 2 · Forbidden similarities + collision check (planner contract)

The 32 explicit anti-collision lines from `continua-intake.md §4` are inherited here verbatim. The collision check matrix from `next-template-brief-schema.md §2` is filled in `continua-distinctness-proof.md §1`. Headline result: **5/5 vs Pragma · 5/5 vs Fiscus · 5/5 vs Solaria** — plan sign-off authorised on `DISTINCTNESS_RULES.md §1` (4/5 gate).

Hard prohibitions (`schema §2.1` · no waiver, ever) all satisfied:
- ✓ No URL appearing in another corporate-suite sibling's pool (cross-cluster grep mandatory at A.3)
- ✓ Inter is NOT body sans
- ✓ `--primary-2: #2c3e6b` is NOT introduced into the skin
- ✓ Hero meta-strip is NOT KPI tuple / fiscal-calendar / percorso-cadenza
- ✓ `--primary` (`#0F3A30`) L\* ≈ 21 — well under 40 cream-safe ceiling (CS-PAL-01)
- ✓ No lorem ipsum / placeholder copy
- ✓ Pexels-only · no Unsplash carve-out
- ✓ No geometric sans on heading

---

## 3 · Design DNA · `template_dna.py` shape

```python
TemplateDNA(
    archetype="corporate-suite",
    sub_cluster="family-office-multigenerazionale",

    hero_style="split-stewardship",            # 55/45 invariant · object-led right
    navbar_style="solid-stewardship",          # sticky · pine bg · brass focus ring
    footer_style="sectors-ribbon-continuita",  # 3-col · whistleblowing required

    section_order=[
        "hero",                     # 55/45 · object-led · serif h1 + meta-strip
        "pillars-4",                # custodia · governance · successione · compliance
        "kpi-band-dark",            # the ONE dark band on home · CS-TONE-03
        "governance-cycle-strip",   # mid-strip · the differentiator
        "sectors-ribbon",           # "Profili familiari"
        "leadership",               # "Custodi del mandato" · photo-present
        "cases",                    # "Mandati in continuità"
        "cta-closer-dark",          # restates voice anchor · single filled-brass CTA
    ],

    card_style="pillar-stewardship",     # cream paper · pewter divider · brass underline on focus
    button_style="ghost-stewardship",    # outline-only on cream · filled brass only in dark band
    density="airy",                      # cluster invariant · CS-RHYTHM-01
    tone="stewardship-longitudinal",
    imagery_direction="stewardship-archive-room",
    imagery_key="business-stewardship",
    conversion_pattern="mandate-dialogue",

    font_pairing=("Crimson Pro", "Public Sans"),

    palette={
        "primary":   "#0F3A30",   # deep pine · L* ≈ 21 (cream-safe)
        "secondary": "#5A6E78",   # cool pewter
        "accent":    "#B0875E",   # antique brass · the load-bearing differentiator
        "paper":     "#F4ECDB",   # cream paper · cluster invariant
        "ink":       "#1F2A2C",   # body text on cream · NOT primary
    },

    voice_anchor="La continuità di una famiglia si misura in <em>generazioni</em>.",
    voice_anchor_em_word="generazioni",
    voice_anchor_contrast_pair=False,
)
```

### Why every line is non-negotiable

| Field | Decision | Anti-collision rationale |
|---|---|---|
| `primary #0F3A30` | deep pine green | NOT navy (Pragma) · NOT gray-blue (Fiscus) · NOT warm-carbon (Solaria) · L\* well under 40 cream-safe ceiling |
| `secondary #5A6E78` | cool pewter | first cool secondary not in Pragma's blue family · differs in hex by ≥ 30° hue |
| `accent #B0875E` | antique brass | NOT emerald (Pragma) · NOT deep-navy (Fiscus) · NOT caramel (Solaria) · brass reads "weighed metal" not "tech green" — the load-bearing warmth-flip the matrix §1.3 OPEN strategy requires |
| `font_pairing` | Crimson Pro + Public Sans | Crimson Pro on matrix §1.4 OPEN · Public Sans signals public-trust (gov-designed) and is concretely NOT Inter — addresses the §1.4 cluster-collapse risk head-on |
| `voice_anchor` | one sentence + one em on `generazioni` | one em is the default per CS-TYPE-02 · contrast-pair (Solaria) explicitly avoided |

### Heading-serif fallback (decision-locked at A.5 entry)

Crimson Pro is the primary choice. If at A.5 the build session encounters a licence/availability friction (Google Fonts API failure · weight-set incomplete · italic glyph coverage thin), the substitution is **Spectral** (humanist · highly readable across heading + body). Do NOT substitute Crimson Pro with PT Serif or Lora — both have been considered but have lower italic personality and would soften the temporal-noun italic emphasis. Spectral is the binding fallback.

---

## 4 · Imagery DNA · `business-stewardship` pack

The pack file lives at `docs/content-factory/imagery/packs/business-stewardship.md` after A.3. The 6 slots below are subject specifications; real Pexels URLs land at A.3 with the cross-cluster grep on file.

```yaml
imagery_pack:
  imagery_key: business-stewardship
  pool_source: Pexels                # CS-IMG-SRC-01 · no Unsplash carve-out
  pool_size: 6                       # CS-IMG-POOL-01

  slot_0_hero:
    subject:        private library / partner-study reading room · oak shelves
                    with leather-bound volumes in soft focus · brass reading-lamp
                    lit on partner desk in foreground · single book on desk in
                    sharp focus · NO people · warm afternoon light through
                    windows
    mood:           contemplative · object-led · afternoon-warm · institutional-
                    but-domestic · deep DoF on lamp + book spine
    composition:    landscape · subject right of frame so 55/45 hero text-left
                    has breathing room
    color_temp:     warm interior · pine-shadow ambient
    coherence:      object-led hero · the library IS the firm's value proposition
                    rendered as room · not a desk · not a boardroom · not a 1:1
    pexels_search:  "library reading room oak shelves brass lamp"
    feasibility:    GO (12-18 plausible candidates · §6.5 GO)
    rejection_rules_for_curator:
                    REJECT: any laptop / keyboard / monitor visible
                    REJECT: more than 1 document / paper visible on desk
                    REJECT: any human (even partial limbs)
                    REJECT: cold daylight (Pragma adjacency)
                    REJECT: tidy-task framing (Fiscus collision warning §12.2)

  slot_1_feature:
    subject:        oak partner-desk close-up · brass desk-lamp lit · single
                    open ledger with bookmark ribbon · hand-written annotations
                    visible but illegible (no readable client data) · cream
                    paper texture
    mood:           working-archive · focused-but-quiet
    use:            about.html hero band · home pillars accent
    coherence:      shows what custodial work looks like in close-up — same
                    object world as hero, framed tighter
    pexels_search:  "oak partner desk leather chair warm afternoon"
    feasibility:    GO (8-12 candidates)

  slot_2_portrait:
    subject:        senior steward · 60s · seated three-quarter profile in
                    leather wing-back chair · light sweater + collared shirt ·
                    direct gaze · neutral background · natural light
    mood:           senior · trustworthy · calm
    diversity_note: explicitly older-generation steward · NOT 30s · solves
                    Solaria 30sCx2 residual gap
    pexels_search:  "senior man professional 60s natural light"
    feasibility:    GO (15-25 candidates)

  slot_3_portrait:
    subject:        co-steward · 40s · standing posed three-quarter against
                    bookcase shadow · tailored jacket · direct gaze · visibly
                    different gender + ethnicity from slot_2
    mood:           mid-career · contemplative · institutional
    diversity_note: explicit visible variation vs slot_2 (age + gender +
                    ethnicity) · curator confirms triple at A.3
    pexels_search:  "professional woman 40s wing-back chair institutional"
    feasibility:    GO (10-15 candidates)

  slot_4_detail:
    subject:        wax-seal letterhead in close-up · brass bookmark ribbon
                    crossing the seal · cream paper texture visible · NO tax
                    documents · NO laptop · NO eyeglasses-on-paper
    mood:           archival · ceremonial · quiet
    coherence:      replaces "documents" with "stewardship object" · the only
                    paper visible is a single sealed letterhead
    pexels_search:  "wax seal letterhead bookmark ribbon"
    feasibility:    GO (6-10 candidates)

  slot_5_ambient:
    subject:        slate stairwell with brass handrail at dusk · warm interior
                    light spilling from a doorway above · architectural · NO
                    people
    mood:           building-of-substance · longevity · NOT atrium · NOT
                    bookshelf
    why_not_bookshelf: Fiscus owns bookshelf as ambient · CS-IMG-SRC-04
                    cross-cluster distinct subject
    pexels_search:  "slate stairwell brass handrail interior architecture"
    feasibility:    CAUTION (5-8 candidates) · curator authorised to take first
                    viable swap if cross-cluster grep fails on lead candidate

  imagery_distinctness:
    vs_pragma:
      - hero is object-led · Pragma's is 4-person boardroom
      - feature is desk close-up · Pragma's feature is corporate atrium
      - ambient is slate stairwell · Pragma's ambient is industrial conference
      - portraits are 60s + 40s diverse · Pragma is typographic-only (no portraits)
      - mood is mahogany-warm · Pragma is daylight-cool
      - subject density is 0 (hero) then 1 (portraits) · Pragma is 1-4 throughout

    vs_fiscus:
      - hero is reading-room · Fiscus is desk-with-documents
      - hero shows a SINGLE archival object · Fiscus shows 3+ document layers
      - ambient is stairwell · Fiscus's ambient is law-bookshelf (banned overlap)
      - portraits show 60s + 40s · Fiscus has typographic-only
      - hero color temp is mahogany-warm · Fiscus is interior-warm-but-task-focused
      - detail is wax-seal letterhead · Fiscus's detail is tax-document close-up

    vs_solaria:
      - hero is object-led + zero people · Solaria is 1:1 conversation
      - hero is mahogany-warm · Solaria is cool-bright meeting room
      - feature is desk close-up · Solaria's feature is man-writing-in-notebook
      - portraits are 60s + 40s diverse · Solaria is 30s × 2 (the residual gap)
      - ambient is stairwell · Solaria's ambient is warm-home-office-with-plants
      - detail is wax-seal letterhead · Solaria's detail is open-notebook-pen-on-desk

  cross_cluster_grep_clean:    YES (intent · curator confirms at A.3 BEFORE committing URLs)
```

---

## 5 · Typography DNA

| Surface | Specification |
|---|---|
| **h1 hero** | Crimson Pro 56px / line-height 1.08 / weight 500 / italic on `generazioni` only |
| **h2 section** | Crimson Pro 36px / line-height 1.16 / weight 500 / italic only on em-word |
| **h3 card** | Crimson Pro 24px / line-height 1.24 / weight 500 |
| **eyebrow / label** | Public Sans 12px / uppercase / letter-spacing 0.22em / weight 600 (RTL resets letter-spacing to 0 — CS-TYPE-05) |
| **body** | Public Sans 17px / line-height 1.6 / weight 400 / tracking 0 |
| **CTA label** | Public Sans 15px / weight 600 / letter-spacing 0.04em |
| **`.num` KPI** | Public Sans 48px / weight 600 / `font-variant-numeric: tabular-nums` (CS-TYPE-03) |
| **AR heading** | swap to Noto Kufi Arabic via `html[dir="rtl"]` (CS-TYPE-06) — Crimson Pro Latin wordmark preserved (CS-NAV-06 / CS-FOOT-03) |
| **AR body** | swap to Amiri |

**Why Crimson Pro vs the alternatives**: Crimson Pro's classical book-jacket ratios + strong italic carry the stewardship register without the editorial-newspaper flavor (Pragma's Merriweather), the document-pair stiffness (Fiscus's Plex Serif), or the warm humanist contemporary feel (Solaria's Fraunces). It reads "long-form, considered, generational." Italic personality is strong enough that the temporal-noun italic emphasis lands at h1 56px without colour or weight assistance.

**Why Public Sans body**: matrix §1.4 calls Inter "taken twice — third use collapses the cluster." Public Sans is gov-designed (US Web Design System), reads "public trust / institutional neutrality," differs visibly from Inter (slightly wider counters, less geometric, more Helvetica-Neue-adjacent). Pairs cleanly with Crimson Pro and explicitly pulls the cluster out of "Inter on whatever serif" territory.

---

## 6 · Section sequence · home page

A practical beat sheet, not a wireframe novel. Word counts target the upper-band targeting from `continua-intake.md §7.1` (~1550 total).

| # | Section | Beat purpose | Concrete content (IT) | Word target |
|---|---|---|---|---|
| 1 | `hero` 55/45 | Position + voice anchor + first proof tuple | h1: voice anchor (italic on `generazioni`) · subhead 1 line: "Custodi del patrimonio familiare attraverso le generazioni." · primary CTA "Avvia un dialogo di mandato" (outline-on-cream) · stewardship-horizon-strip below CTA · object-led hero photo right with credit overlay `(Custodi del mandato · Iscrizione Albo Trustees)` | 35 |
| 2 | `pillars-4` | What the firm DOES, in 4 named verbs | 4 cards: **Custodia patrimoniale** (asset stewardship across generations) · **Governance familiare** (Family Council facilitation, charters, voting structures) · **Successione strutturata** (multi-generational transfer planning) · **Compliance fiduciaria** (trustee oversight, regulatory continuity) · each card = one icon (line-stroke, brass) + one h3 + ~95w body + cream paper + brass underline on focus | 380 (4×95) |
| 3 | `kpi-band-dark` | The ONE dark band on home (CS-TONE-03) | 4 KPIs on `--primary` background: `18 anni — orizzonte medio mandato` · `3 generazioni — famiglie in carico` · `€ 1.8 B — patrimonio in custodia` · `4 — riunioni CdF / anno` · all `font-variant-numeric: tabular-nums` · brass eyebrow tints on labels (Mitigation §12 Warning 1) | 90 |
| 4 | `governance-cycle-strip` | The differentiator beat — the firm's RHYTHM rendered as cells | 3 cells, cream paper. Each cell = (eyebrow label · figure · context-line) triple, NOT (label · figure) — Mitigation §12 Warning 5: <br>· **Cadenza CdF** · 4 riunioni / anno · "calendario di governance condiviso con la famiglia" <br>· **Audit di continuità** · annuale · "verifica indipendente sulla coerenza pluriennale del mandato" <br>· **Patto familiare** · revisione triennale · "aggiornamento delle regole interne, con o senza generazione entrante" | 180 |
| 5 | `sectors-ribbon` | Anonymized client-segment proof (CS-COMP-01) | label "Profili familiari" · 8 segments: famiglie imprenditoriali · holding di partecipazioni · fondazioni di famiglia · gruppi multi-asset · seconde generazioni in trasferimento · trustees indipendenti · ufficio di rappresentanza · single family office estero | 120 |
| 6 | `leadership` | "Custodi del mandato" · 3 stewards, photo-present | 3 cards: nome + ruolo (**Senior Steward** · **Family Officer** · **Compliance Officer**) + 1 credential each (real: Albo Trustees / STEP Affiliate / OAM) + portrait from slot 2/3 + 1-line bio. NOT "Partner / Senior Associate / Counsel". 60s + 40s + visible diversity (Mitigation §12 Warning 4). | 200 |
| 7 | `cases` | "Mandati in continuità" · 4 anonymized · multi-year | each case = anonymized profile + 3 stewardship-duration markers + scope segment + 1-line outcome. Example: "Famiglia A · 4ª generazione · holding industriale · scope: continuità + governance + audit triennale · 12 anni di mandato in continuità · revisione patto familiare 2023" · upper-band ~110w each | 440 (4×110) |
| 8 | `cta-closer-dark` | Restates voice anchor + final CTA | Dark `--primary` band but distinct visual register from KPI band (centred copy · larger h2 · single filled-brass CTA "Avvia un dialogo di mandato"). Voice anchor restated verbatim. | 65 |

**Total**: ~1510 words rendered + chrome overhead → ~1550 with footer/nav copy. Inside cluster's 1500-2500 range.

### Anti-pattern guards baked in

- **CS-RHYTHM-04** (no two adjacent sections share function): pillars (4 verbs) → KPI (4 numbers) → governance-cycle (3 cadences) → sectors (audience) → leadership (people) → cases (mandates) — every adjacent pair is functionally distinct. Style-critic at A.6 verifies.
- **CS-DENSITY-02 / CS-DENSITY-04**: KPI count = 4, pillar count = 4 (within bands, no waiver).
- **CS-PAL-05**: cta-closer is ONE primary, not three. Hero CTA + nav CTA + closer CTA = 3 across the home, never 3 in a single viewport.
- **CS-COMP-06** (no wall-of-text opener): about.html opens with `timeline`, not "Our Story" essay.
- **CS-TONE-03** (one dark band on home): only the KPI band; cta-closer is the structural bookend per cluster precedent (centred, larger h2, single filled CTA — distinct register from the KPI band).

---

## 7 · Navbar · footer direction

### Navbar (`solid-stewardship`)

- Sticky · `background: var(--primary)` (deep pine `#0F3A30`) · cream link text
- Wordmark: **"Continua"** (single word · cluster default · Latin preserved under RTL · CS-NAV-06)
- 5 links: `Lo studio · Custodia · Governance · Mandati · Contatti` (5 = cluster default)
- Trailing accent CTA: `"Avvia un dialogo di mandato"` · solid brass `#B0875E` on dark · the chrome's only filled element (CS-NAV-04 · brass touchpoint #1)
- Locale switcher: pill with `lang` + `dir` per link · sits between last nav item and CTA · CS-NAV-03
- `:focus-visible` brass ring (2px outline · 4px offset) · CS-NAV-02 · the cluster's signature interactive moment (brass touchpoint #2)
- 4 link states (default / hover / focus / active) · all distinct
- Mobile (≤880px): hamburger drawer · CSS-only · per X.4a step1d hardening (the corporate-suite skin already carries this; Continua inherits)

### Footer (`sectors-ribbon-continuita`)

- 3 columns on `--primary` background · cream type
- **Col 1 brand**: wordmark + 1-line stewardship one-liner · "Custodi del patrimonio familiare attraverso le generazioni."
- **Col 2 sitemap**: 5 nav links + 3 secondary (Trasparenza · Privacy · Whistleblowing)
- **Col 3 contact**: address (Milano) · email (`mandato@continua.it`) · phone · CdF schedule note ("Riunioni CdF · trimestrali")
- Legal row at bottom: P.IVA · privacy · cookie · **whistleblowing link required** (D.lgs. 24/2023 · CS-FOOT-02)
- Footer stacks to 1 column at ≤720px (CS-FOOT-05 — cluster R2 fault line · MUST be added BEFORE first build, not deferred)
- Latin wordmark + Latin numerics preserved under RTL · CS-FOOT-03

### Brass touchpoint inventory (Mitigation §12 Warning 1)

The brass accent must appear at ≥ 3 viewport touchpoints to land as the cool-on-cool palette differentiator. The build commits to 5:
1. Trailing nav CTA (solid brass on pine)
2. `:focus-visible` ring on every interactive element (2px brass outline)
3. KPI band eyebrow tints on the 4 stat labels
4. Pillar card brass underline on `:focus-within` / `:hover`
5. cta-closer single filled-brass button

Style-critic at A.6 confirms the 5 touchpoints render at 1920 first scroll. Walk at A.7 confirms at 1280 + 720 the brass is still visibly distinct from pine background.

---

## 8 · Proof style

**Rendering principle**: stewardship-duration over numeric KPI alone. Time-axis carries the proof.

| Surface | Concrete shape |
|---|---|
| KPI band (home, dark) | mix of duration + scope · `18 anni · 3 generazioni · €1.8 B · 4 riunioni CdF/anno` (NOT pure numeric like Pragma's "22 anni · 180+ mandati · €1.4 B · 94%") |
| Sectors ribbon | "Profili familiari" labelled segments (NOT "Settori" generic — names the audience as families, not industries) |
| Leadership card | name + role + ONE real albo credential (Albo Trustees / STEP / OAM) — NOT a list of 3-4 like Solaria's |
| Cases list | "Mandati in continuità" · each card carries duration marker (`4ª generazione · da 12 anni`) + scope segment + audit cadence — public-record proof shape |
| Case detail page | adds a `continuity-context` slot mirroring Solaria's `method-context` precedent — slot shows multi-year timeline + 3+ governance milestones (anonymized). Detail-page order: kpi-strip + narrative + `continuity-context` + `next-mandate`. |
| Trust band | `Riconoscimenti istituzionali` (NOT Solaria's "Aziende sponsor recenti") · real institutional badges (STEP · Albo Trustees · ANC · OAM) — anonymized but verifiable |

**What this avoids**: numeric-only KPI inflation that reads as B2B-advisory chest-thump. The shape carries time, not just magnitude.

---

## 9 · CTA personality

**Primary CTA copy**: `"Avvia un dialogo di mandato"`

### Polarity rules (CS-CTA-01 · cluster ratification 2026-04-26 · do not re-litigate)

- On cream paper: outline-only · pine border · pine label · brass on `:focus-visible`
- In the dark CTA-closer band: filled brass on pine background · the polarity inversion is the cluster's signature CTA move
- Hover on cream: 4px brass underline grows from baseline (NOT a fill swap on cream)
- Hover on dark: brass deepens 8% via `filter: brightness(0.92)` (NOT a colour change)

### Form gate (`/contatti/`)

Scope-meeting shape · 3 fields:
1. **Scope familiare** (textarea · placeholder: "Ci dica brevemente la struttura attuale e la sua preoccupazione di continuità.")
2. **Orizzonte temporale** (select · 5y / 10y / 25y / multi-generazionale)
3. **Struttura attuale** (select · holding / fondazione / trust / patto di famiglia / nessuna formalizzata)

NO P.IVA + CF (Fiscus collision). NO ICF code-of-ethics referenced (Solaria's). NO NDA-ready boardroom form (Pragma's). The horizon-selector is the differentiating field.

### CTA copy banlist respected

- NOT "Get started free" · NOT "Sign up now" · NOT "Iscriviti gratis" (CS-CTA-02)
- NOT "Fissa una call privata" (Pragma)
- NOT "Primo appuntamento" (Fiscus)
- NOT "Prenota una discovery call" (Solaria)

---

## 10 · Leadership feel

```
leadership_block:
  presence:                  PHOTO-PRESENT (carries Solaria precedent forward)
  card_count:                3
  card_composition:          portrait + h3(name) + role-label + 1-credential + 1-line bio

  steward_1:
    name:                    [TBD at A.4 — placeholder "Eleonora Marchesi"]
    role_label:              "Senior Steward"
    credential:              "Albo dei Trustees · Iscrizione 2007"
    visible_demographic:     60s · woman · Mediterranean
    portrait_slot:           slot_2 (60s steward · seated wing-back)

  steward_2:
    name:                    [TBD at A.4 — placeholder "Tomas Okafor"]
    role_label:              "Family Officer"
    credential:              "STEP Affiliate · 2014"
    visible_demographic:     40s · man · West African heritage
    portrait_slot:           slot_3 (40s co-steward · standing)

  steward_3:
    name:                    [TBD at A.4 — placeholder "Ginevra Conti"]
    role_label:              "Compliance Officer"
    credential:              "OAM · Iscrizione mediatori creditizi"
    visible_demographic:     50s · woman · Northern Italian
    portrait_slot:           cropped slot_1 feature (desk close-up reframed as
                             environmental portrait fragment — confirm at A.3
                             curator review, OR add a 6th slot if needed)
```

**Mitigation binding** (§12 Warning 4): the 3 stewards span 40s · 50s · 60s + 2 women · 1 man + 3 visible ethnicities. Curator at A.3 hard-rejects any combination that flattens to one demographic axis.

**Why photo-present**: Solaria established the photo-present precedent in this cluster (`30sCx2` flagged as the demographic gap). Continua takes the precedent forward AND fixes the gap. Typographic-only would re-collapse the cluster into "no faces by default" — a step backward for the family-office sub-cluster where personal stewardship is the value proposition.

---

## 11 · Multilingual intent

```
multilingual_intent:
  initial_locale:                 it
  planned_locales:                [it, en, fr, es, ar]
  rtl_required:                   YES

  voice_anchor_strategy:
    it_anchor:    "La continuità di una famiglia si misura in <em>generazioni</em>."
    em_word:      generazioni
    translation_note: "Italic carries multi-generational time-horizon. Translators
                      MUST italicise the equivalent of generazioni:
                        EN: generations · FR: générations · ES: generaciones ·
                        AR: الأجيال (italic-substitute via Kufi weight or oblique)
                      Do NOT italicise misura / continuità."
    contrast_pair_anchor:    NO

  terminology_locked_pre_translation:
    cluster_terminology_file:     factory/standards/corporate-suite-design-standard.md §11
    credentials_per_locale:       ["Albo dei Trustees", "STEP Affiliate", "OAM",
                                   "ANC (Audit di continuità)"]
    legal_row_per_locale:         [P.IVA, privacy, cookie, whistleblowing]

  ar_specific_requirements:
    heading_font_swap:            "Noto Kufi Arabic"
    body_font_swap:               "Amiri"
    latin_wordmark_preserved:     YES
    letter_spacing_reset:         YES
    rtl_layout_via_logical_props: YES

  per_locale_form_options:
    orizzonte_temporale_select:
      IT:   ["5 anni", "10 anni", "25 anni", "multi-generazionale"]
      EN:   ["5 years", "10 years", "25 years", "multi-generational"]
      FR:   ["5 ans", "10 ans", "25 ans", "multi-générationnel"]
      ES:   ["5 años", "10 años", "25 años", "multi-generacional"]
      AR:   ["٥ سنوات", "١٠ سنوات", "٢٥ سنة", "متعدد الأجيال"]
            # AR digit convention: confirm Western vs Eastern Arabic numerals
            # at workflow C pre-flight per cluster terminology
```

The IT pass at workflow A does NOT depend on AR resolution. AR convention questions land at workflow C pre-flight; IT walk passes regardless.

---

## 12 · Anti-clone constraints (binding for build agent)

The build agent at A.5 reads this list before writing the first line of the skin. Each line is enforced by either a rule ID, a style-critic check at A.6, or a walk check at A.7.

### Tone / voice anchor
- ✗ Pragma's "decisional gravity" framing
- ✗ Fiscus's "presidio + scadenze-first" framing
- ✗ Solaria's "non-terapia non-consulenza" bounded-method framing
- ✗ Two em-wraps in any heading

### Palette
- ✗ Slate-blue + emerald family
- ✗ Warm-neutral + gold + blu-notte family
- ✗ Warm-carbon + ocra + caramel family
- ✗ Bright pure red/orange/yellow at full saturation

### Typography
- ✗ Inter as body sans (third use collapses cluster — hard prohibition)
- ✗ IBM Plex Sans body
- ✗ Merriweather, IBM Plex Serif, Fraunces as heading
- ✗ Montserrat, Poppins, Raleway on headings (CS-TYPE-01)

### Hero composition
- ✗ Pragma's KPI tuple as meta-strip
- ✗ Fiscus's fiscal-calendar-strip
- ✗ Solaria's percorso-cadenza-strip
- ✗ `(Direzione, Anno fondazione)` as the hero credit overlay (used twice)
- ✗ Any hero photo with > 1 document, any laptop/keyboard, any visible human

### Imagery
- ✗ Boardroom long-table hero
- ✗ Tidy desk + documents hero
- ✗ 1:1 conversation hero
- ✗ Bookshelf as ambient slot
- ✗ Two 30s Caucasian portraits as slots 2-3
- ✗ Any URL appearing in `business-corporate`, `business-fiscal`, `business-coaching`

### CTA
- ✗ "Fissa una call privata" / "Primo appuntamento" / "Prenota una discovery call"
- ✗ "Get started free" / "Sign up now" / "Iscriviti gratis"
- ✗ A form gate asking for both P.IVA + CF

### Section rhythm
- ✗ Pragma's exact section order (no mid-strip + leadership present)
- ✗ Fiscus's `fiscal-calendar` mid-strip
- ✗ Solaria's `manifesto` opener replacing pillars
- ✗ Solaria's `method-cadenza` mid-strip
- ✗ Wall-of-text "Our Story" opener

### Leadership / proof
- ✗ Pragma / Fiscus / Solaria credential vocabularies verbatim
- ✗ Any fake credential (CS-EXEC-03)
- ✗ "Casi seguiti" / "Casi anonimizzati" / "Case studies" without fresh framing
- ✗ Solaria's "Aziende sponsor recenti" trust-band label

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

## 13 · Browser-live expectations (precis · full plan in `continua-browser-gate.md`)

The IT walk at A.7 produces:
- 6 pages × 6 viewports = **36 captures** at `factory/reports/browser-verification/continua-stewardship/it/<YYYY-MM-DD>/`
- Plus 1 reduced-motion capture
- Plus a contrast report at all 6 viewports
- Plus a responsive report at all 6 viewports
- Plus a style-critic report against `corporate-suite-design-standard.md`

**The walk verdict at A.7 must read PASS** (or BORDERLINE → A.8 narrow fix → re-walk) before Commit A draft-landing.

**The 5 mitigations from §12 of the intake must be verified live**:
1. Brass accent visible at ≥ 3 touchpoints at 1920 first scroll · also visible at 1280 and 720 contrast walks
2. Hero photo passes object-led + zero-document filter at 1280 + 1024 crops
3. "Remove the studio name" test passes on the live render (CS-TONE-05 · master §5.12)
4. Leadership 3-card row shows 3 distinct demographics at 1920, 1280, 768
5. Mid-strip cells render (eyebrow · figure · context-line) triple, not (label · figure)

Workflow C (5 locales · 144 + 6 captures) gates the LIVE flip via `release-decision-orchestrator.md`. IT-only Commit A is the workflow A endpoint.

---

## 14 · Release-gate expectations

The release-gatekeeper at A.9 reads these. Tier flip from `draft` to `published_live` is a SEPARATE pass and binds on:

- Scorecard ≥ 4.50/5 (4.67/5 is precedent)
- 0 open `[BLOCKING]` findings
- IT walk PASS · 4 locale walks PASS (EN/FR/ES/AR via workflow C) · AR RTL parity walk PASS
- User-handshake binary SHIP recorded
- Live DOM still matches this brief at flip time
- Pexels-only re-confirmed on live render across all 5 locales
- Distinctness re-confirmed ≥ 4/5 vs every sibling at flip time
- All walk verdicts ≤ 30 days fresh

---

## 15 · The single-page summary the orchestrator reads at sign-off

```
PLAN SIGN-OFF SUMMARY · continua-stewardship
=============================================

What this template is:
    A stewardship-grade family office that custodies a family's
    patrimony across generations, governed via a Family Council,
    measured in decades and generations rather than market cycles.

What this template is NOT:
    NOT Pragma's boardroom-advisory mandate (B2B not B2family).
    NOT Fiscus's commercialista presidio (multi-decade not annual).
    NOT Solaria's bounded executive coaching (institutional not personal).

Voice anchor (IT · verbatim · with <em>):
    "La continuità di una famiglia si misura in <em>generazioni</em>."

Palette: primary #0F3A30 · secondary #5A6E78 · accent #B0875E
Macro tone: deep pine + cool pewter + antique brass · cool-secondary + warm-accent

Typography: Crimson Pro + Public Sans

Hero: 55/45 split + photo subject "private library / partner-study reading
      room with brass lamp lit on partner desk · NO people"
    + meta-strip "stewardship-horizon-strip · Mandato medio · Generazioni · Riunioni CdF"

CTA: "Avvia un dialogo di mandato" → mandate-dialogue (multi-year framing)

Section moves that distinguish this from siblings:
  1. Object-led hero with zero people (the cluster's first; closes
     the silhouette gap from Pragma/Fiscus/Solaria's people-present heroes)
  2. Pine + brass palette with cool-secondary + warm-accent strategy
     (the only matrix §1.3 OPEN warmth combo)
  3. Mid-strip names a CADENCE not a number/calendar/arc
     (governance-cycle · 4 riunioni/anno + audit annuale + patto triennale)

Distinctness scores:
  vs Pragma:  5/5
  vs Fiscus:  5/5
  vs Solaria: 5/5
  GATE:       PASS

Imagery pack: business-stewardship · curator-approved at A.3 · 6 URLs Pexels-only

Initial locale: it (others at workflow C)
Initial tier: draft

Browser walk plan: 6 viewports × 1 locale (it) × 6 pages = 36 captures + 1 reduced-motion
Walk artefact dir: factory/reports/browser-verification/continua-stewardship/it/<YYYY-MM-DD>/

Scorecard expected grade: ≥ 4.50/5

Open questions for orchestrator:
  - Crimson Pro vs Spectral fallback decision at A.5 build entry (not a re-spec)
  - AR italic-substitute convention at workflow C pre-flight (not blocking IT pass)
```

The §3.2 studio-name swap test re-runs on this summary at A.2 sign-off per `pre-build-quick-checks §5`. If the swap collapses any line above into a generic, the brief returns for re-spec.

---

## 16 · What this brief is and is not

**This brief IS**:
- A complete, decision-locked planner-brief equivalent.
- Ready to hand to a workflow A.3 (curator) → A.4 (copy) → A.5 (build) chain with no re-spec.
- The contract the style-critic re-reads at A.6 and the walk-verifier re-reads at A.7.

**This brief is NOT**:
- A real `template_dna.py` entry (the build at A.5 writes that).
- A real seed file (A.5 writes that).
- A curator-approved Pexels pack (A.3 produces that, with cross-cluster grep on file).
- A copy diff (A.4 produces that with the voice anchor verbatim).
- A critique or walk verdict (A.6 / A.7).

If a real workflow A pass picks this up tomorrow, it routes to:
1. **A.3 imagery-curator** — with this §4 pack spec as input · runs cross-cluster grep BEFORE committing URLs · curator approval gate before A.4
2. **A.4 copy-translation** — with this §6 word-targets and §11 voice anchor + em-word as input · IT only · D-102 cadence
3. **A.5 template-builder** — with this §3 DNA + §6 section sequence + §7 nav/footer specs as input · CLI green + IT live URL openable
4. **A.6 critique** — three reports against the design standard, the contrast rules, and the responsive matrix
5. **A.7 walk** — 6 pages × 6 viewports, verdict per `continua-browser-gate.md`
6. **A.9 aggregate** — scorecard, user-handshake, Commit A request

Gates between every step. No skipping.
