# Candidate-01 · Orchestrator dry-run output · DRY RUN

**Status**: dry-run · simulation of what the orchestrator would produce on this candidate
**Read with**: `candidate-01-intake.md` (input) · `candidate-01-distinctness-proof.md` (proof) · `candidate-01-browser-plan.md` (verification plan)
**Purpose**: a practical blueprint that could become a real build brief without rewriting

This file simulates the planner-brief and design-DNA output the orchestrator would route through `template-orchestrator-master.md` steps A.2 → A.5 for `continua-stewardship`. Sources are concrete; no theory, no marketing prose.

---

## 1 · Design DNA · `template_dna.py` shape

```python
TemplateDNA(
    archetype="corporate-suite",
    sub_cluster="family-office-multigenerazionale",

    hero_style="split-stewardship",            # 55/45 invariant · object-led right
    navbar_style="solid-stewardship",          # sticky · primary bg · brass focus ring
    footer_style="sectors-ribbon-continuita",  # 3-col · whistleblowing required

    section_order=[
        "hero",
        "pillars-4",                # custodia · governance · successione · compliance
        "kpi-band-dark",            # the ONE dark band · CS-TONE-03
        "governance-cycle-strip",   # mid-strip · the differentiator
        "sectors-ribbon",           # "Profili familiari"
        "leadership",               # "Custodi del mandato" · photo-present
        "cases",                    # "Mandati in continuità"
        "cta-closer-dark",          # restates voice anchor
    ],

    card_style="pillar-stewardship",     # cream paper · pewter divider · brass underline on hover
    button_style="ghost-stewardship",    # outline-only on cream · filled brass only in dark
    density="airy",                      # cluster invariant · CS-RHYTHM-01
    tone="stewardship-longitudinal",
    imagery_direction="stewardship-archive-room",
    imagery_key="business-stewardship",
    conversion_pattern="mandate-dialogue",

    font_pairing=("Crimson Pro", "Public Sans"),   # both fresh · NOT Inter · NOT Merriweather/Plex/Fraunces

    palette={
        "primary":   "#0F3A30",   # deep pine · L* ≈ 21 (well under 40 cream-safe ceiling)
        "secondary": "#5A6E78",   # cool pewter (cool secondary)
        "accent":    "#B0875E",   # antique brass (warm accent · cluster signature focus ring colour)
        "paper":     "#F4ECDB",   # cream paper · cluster invariant
        "ink":       "#1F2A2C",   # text on cream · NOT primary (avoid mono on dark band)
    },

    voice_anchor="La continuità di una famiglia si misura in <em>generazioni</em>.",
    voice_anchor_em_word="generazioni",
    voice_anchor_contrast_pair=False,
)
```

**Why each line is non-negotiable**

| Field | Decision | Anti-collision rationale |
|---|---|---|
| `primary #0F3A30` | deep pine green | NOT navy (Pragma) · NOT gray-blue (Fiscus) · NOT warm-carbon (Solaria) |
| `secondary #5A6E78` | cool pewter | first cool secondary in the cluster — Pragma had cool blue (different family) · Fiscus warm gold · Solaria warm ocra |
| `accent #B0875E` | antique brass | NOT emerald (Pragma) · NOT deep-navy (Fiscus) · NOT caramel (Solaria) · brass reads "weighed metal" not "tech green" |
| `font_pairing` | Crimson Pro + Public Sans | Crimson Pro is open in matrix §1.4 · Public Sans signals public-trust (gov-designed) and is concretely NOT Inter — addresses the §1.4 overlap risk head-on |
| `voice_anchor` | one sentence + one em on `generazioni` | one em is the default per CS-TYPE-02 · contrast-pair (Solaria) explicitly avoided per matrix §1.4 |

---

## 2 · Imagery DNA · `business-stewardship` pack

Six Pexels slots, all with subject + mood + coherence note. URLs are illustrative subject specs (the real curator agent runs cross-cluster grep at A.3 before committing real URLs). Matrix §1.6 OPEN territory: object-led / library-reading-room.

```yaml
imagery_pack:
  imagery_key: business-stewardship
  pool_source: Pexels                # CS-IMG-SRC-01 · no Unsplash carve-out
  pool_size: 6                       # CS-IMG-POOL-01

  slot_0_hero:
    subject:        private family-office reading room with stewardship archive
                    cabinet open · brass key on cabinet face · single bound family
                    register visible spine-out · no people
    mood:           mid-afternoon mahogany-warmth · deep DoF on brass · contemplative
    composition:    landscape · subject right of frame so 55/45 hero text-left has
                    breathing room
    color_temp:     warm interior · pine-shadow ambient
    coherence:      object-led hero · stewardship cabinet IS the firm's value
                    proposition rendered as object · not a desk · not a boardroom

  slot_1_feature:
    subject:        oak partner-desk close-up · brass desk-lamp lit · open ledger
                    with bookmark ribbon · hand-written annotations visible but
                    illegible (no readable client data)
    mood:           working-archive · focused-but-quiet
    use:            about.html hero band · home second-section accent
    coherence:      shows what custodial work looks like in close-up

  slot_2_portrait:
    subject:        senior steward · 60s · seated three-quarter profile in
                    leather wing-back chair · light sweater + collared shirt ·
                    direct gaze · neutral background
    mood:           senior · trustworthy · calm
    diversity_note: explicitly older-generation steward · NOT 30s

  slot_3_portrait:
    subject:        co-steward · 40s · standing posed three-quarter against
                    bookcase shadow · tailored jacket · direct gaze ·
                    visibly different gender + ethnicity from slot_2
    mood:           mid-career · contemplative · institutional
    diversity_note: explicit visible variation vs slot_2 · solves Solaria 30sCx2

  slot_4_detail:
    subject:        wax-seal letterhead in close-up · brass bookmark ribbon
                    crossing the seal · cream paper texture visible
    mood:           archival · ceremonial · quiet
    coherence:      replaces "documents" with "stewardship object" · no tax forms

  slot_5_ambient:
    subject:        slate stairwell with brass handrail at dusk · warm interior
                    light spilling from a doorway above · architectural · no people
    mood:           building-of-substance · longevity · NOT atrium · NOT bookshelf
    why_not_bookshelf: Fiscus owns bookshelf as ambient · CS-IMG-SRC-04 cross-cluster
                       distinct subject

  imagery_distinctness:
    vs_pragma:
      - hero is object-led · Pragma's is 4-person boardroom
      - feature is desk close-up · Pragma's feature is corporate atrium
      - ambient is slate-stairwell · Pragma's ambient is industrial conference
      - portraits are 60s + 40s diverse · Pragma is typographic-only
      - mood is mahogany-warm · Pragma is daylight-cool
      - subject density is 0 then 1 · Pragma is 1-4 throughout

    vs_fiscus:
      - hero is reading-room · Fiscus is desk-with-documents
      - hero shows a SINGLE archival object · Fiscus shows 3+ document layers
      - ambient is stairwell · Fiscus's ambient is law-bookshelf (banned overlap)
      - portraits show 60s + 40s · Fiscus has typographic-only
      - hero color temp is mahogany-warm · Fiscus is interior-warm-but-task-focused
      - detail is wax-seal · Fiscus's detail is tax-document close-up

    vs_solaria:
      - hero is object-led + zero people · Solaria is 1:1 conversation
      - hero is mahogany-warm · Solaria is cool-bright meeting room
      - feature is desk close-up · Solaria's feature is man-writing-in-notebook
      - portraits are 60s + 40s diverse · Solaria is 30s × 2 (the residual risk)
      - ambient is stairwell · Solaria's ambient is warm-home-office-with-plants
      - detail is wax-seal · Solaria's detail is open-notebook-pen-on-desk

  cross_cluster_grep_clean:    YES (intent · curator confirms at A.3)
```

---

## 3 · Typography direction

| Surface | Specification |
|---|---|
| **h1 hero** | Crimson Pro 56px / line-height 1.08 / weight 500 / italic on `generazioni` only |
| **h2 section** | Crimson Pro 36px / line-height 1.16 / weight 500 / italic only on em-word |
| **h3 card** | Crimson Pro 24px / line-height 1.24 / weight 500 |
| **eyebrow / label** | Public Sans 12px / uppercase / letter-spacing 0.22em / weight 600 (RTL resets to 0 — CS-TYPE-05) |
| **body** | Public Sans 17px / line-height 1.6 / weight 400 / tracking 0 |
| **CTA label** | Public Sans 15px / weight 600 / letter-spacing 0.04em |
| **`.num` KPI** | Public Sans 48px / weight 600 / `font-variant-numeric: tabular-nums` (CS-TYPE-03 · the cluster's invisible discipline) |
| **AR heading** | swap to Noto Kufi Arabic via `html[dir="rtl"]` (CS-TYPE-06) — Crimson Pro Latin wordmark preserved (CS-NAV-06 / CS-FOOT-03) |
| **AR body** | swap to Amiri |

**Why Crimson Pro vs the alternatives**: Crimson Pro's classical book-jacket ratios + strong italic carry the stewardship register without the editorial-newspaper flavor (Pragma's Merriweather), the document-pair stiffness (Fiscus's Plex Serif), or the warm humanist contemporary feel (Solaria's Fraunces). Crimson Pro reads "long-form, considered, generational." Fallback if license proves cumbersome: PT Serif (cooler · narrower x-height) or Spectral (humanist · highly readable across heading + body).

**Why Public Sans body**: matrix §1.4 calls Inter "taken twice — third use collapses cluster." Public Sans is gov-designed (US Web Design System), reads "public trust / institutional neutrality," differs visibly from Inter (slightly wider counters, less geometric, more Helvetica-Neue-adjacent). It pairs cleanly with Crimson Pro and explicitly pulls the cluster out of "Inter on whatever serif" territory.

---

## 4 · Section sequence · home page

A practical beat sheet, not a wireframe novel.

| # | Section | Beat purpose | Concrete content |
|---|---|---|---|
| 1 | `hero` 55/45 | Position + voice anchor + first proof tuple | h1 = voice anchor (italic on `generazioni`) · subhead 1 line · primary CTA "Avvia un dialogo di mandato" · stewardship-horizon-strip below CTA · object-led hero photo right with credit overlay `(Custodi · Iscrizione albo)` |
| 2 | `pillars-4` | Tell the visitor what the firm DOES, in 4 named verbs | 4 cards: Custodia patrimoniale · Governance familiare · Successione strutturata · Compliance fiduciaria · each card = one icon (not emoji) + one h3 + 2-line body + cream paper + brass underline on focus |
| 3 | `kpi-band-dark` | The ONE dark band on home (CS-TONE-03) | 4 KPIs on `--primary` background: `18 anni — orizzonte medio mandato` · `3 generazioni — famiglie in carico` · `€ 1.8 B — patrimonio in custodia` · `4 — riunioni CdF / anno` · all `font-variant-numeric: tabular-nums` |
| 4 | `governance-cycle-strip` | The differentiator beat — the firm's RHYTHM rendered as cells | 3 cells, cream paper: Cadenza CdF · 4 riunioni / anno · Audit di continuità · annuale · Patto familiare · revisione triennale. Each cell has eyebrow-label + figure + 1-line context. NOT a KPI re-skin. |
| 5 | `sectors-ribbon` | Anonymized client-segment proof (CS-COMP-01) | label "Profili familiari" · 6-8 segments: famiglie imprenditoriali · holding di partecipazioni · fondazioni di famiglia · gruppi multi-asset · seconde generazioni in trasferimento · trustees indipendenti · ufficio di rappresentanza · single family office estero |
| 6 | `leadership` | "Custodi del mandato" · 3 stewards, photo-present | 3 cards: nome + ruolo (Senior Steward · Family Officer · Compliance Officer) + 1 credential each (real: Albo Trustees / STEP Affiliate / OAM) + portrait from slot 2/3 + slot 1 cropped square. NOT "Partner / Senior Associate / Counsel" |
| 7 | `cases` | "Mandati in continuità" · 3 anonymized · with multi-year timeline marker | each case: anonymized profile (e.g. "Famiglia A · 4ª generazione · holding industriale · scope: continuità + governance + audit triennale") + 3 stewardship-duration markers + brief outcome. Different from "Casi seguiti" / "Casi anonimizzati" framing. |
| 8 | `cta-closer-dark` | Restates the voice anchor + final CTA | Dark `--primary` band but distinct visual treatment from KPI band (centred copy · larger h2 · single filled-brass CTA). Voice anchor restated verbatim. |

**Anti-pattern guards baked in**:
- No two adjacent sections share function (CS-RHYTHM-04): pillars (4 verbs) → KPI (4 numbers) → governance-cycle (3 cadences) → sectors (segments) → leadership (people) → cases (mandates) — every adjacent pair is functionally distinct.
- KPI count = 4 (CS-DENSITY-04) · pillar count = 4 (CS-DENSITY-02).
- CTA-closer is ONE primary, not three (CS-PAL-05).
- No "Our Story" wall-of-text opener (CS-COMP-06): about.html opens with a `timeline` instead.

---

## 5 · Navbar · footer direction

### Navbar (`solid-stewardship`)
- Sticky · `background: var(--primary)` (deep pine) · cream link text
- Wordmark: "Continua" (single word · cluster default · Latin preserved under RTL)
- 5 links: `Lo studio · Custodia · Governance · Mandati · Contatti` (5 = cluster default · CS-NAV)
- Trailing accent CTA: `"Avvia un dialogo di mandato"` · solid brass on dark · the chrome's only filled element
- Locale switcher: pill with lang+dir per link · sits between last nav item and CTA · CS-NAV-03
- `:focus-visible` brass ring (2px outline · 4px offset) · CS-NAV-02 · the cluster's signature interactive moment
- 4 link states (default / hover / focus / active) · all distinct
- Mobile (≤880): hamburger drawer · CSS-only (per X.4a step1d hardening)

### Footer (`sectors-ribbon-continuita`)
- 3 columns on `--primary` background · cream type
- Col 1 brand: wordmark + 1-line stewardship one-liner ("Custodi del patrimonio familiare attraverso le generazioni.")
- Col 2 sitemap: 5 nav links + 3 secondary (Trasparenza · Privacy · Whistleblowing)
- Col 3 contact: address · email · phone · CdF schedule note
- Legal row at bottom: P.IVA · privacy · cookie · **whistleblowing link required** (D.lgs. 24/2023 · CS-FOOT-02)
- Footer stacks to 1 column at ≤720px (CS-FOOT-05 — fix added BEFORE first build · cluster R2 fault line addressed)
- Latin wordmark + Latin numerics preserved under RTL · CS-FOOT-03

---

## 6 · Proof style

**Rendering principle**: stewardship-duration over numeric KPI alone.

| Surface | Concrete shape |
|---|---|
| KPI band (home, dark) | mix of duration + scope — `18 anni · 3 generazioni · €1.8 B · 4 riunioni CdF/anno` (NOT pure numeric like Pragma's "22 anni · 180+ mandati · €1.4 B · 94%") |
| Sectors ribbon | "Profili familiari" labelled segments (NOT "Settori" generic — names the audience as families, not industries) |
| Leadership card | name + role + ONE real albo credential (Albo Trustees / STEP / OAM) — NOT a list of 3-4 like Solaria's |
| Cases list | "Mandati in continuità" · each card carries duration marker (`4ª generazione · da 12 anni`) + scope segment + audit cadence — public-record proof shape |
| Case detail page | adds a `continuity-context` slot mirroring Solaria's `method-context` precedent — slot shows multi-year timeline + governance milestones (anonymized) |
| Trust band | NO "Aziende sponsor" (Solaria) · NO "Partner verticali" (Pragma) · instead a `Riconoscimenti istituzionali` band with real institutional badges (STEP · Albo Trustees · ANC etc.) — anonymized but verifiable |

**What this avoids**: numeric-only KPI inflation that reads as B2B-advisory chest-thump. The shape carries time, not just magnitude.

---

## 7 · CTA style

**Primary CTA copy**: `"Avvia un dialogo di mandato"`

**Polarity rules** (CS-CTA-01 · cluster ratification 2026-04-26 · do not re-litigate):
- On cream paper: outline-only · pine border · pine label · brass on `:focus-visible`
- In the dark CTA-closer band: filled brass on pine background · the polarity inversion is the cluster's signature CTA move
- Hover: 4px brass underline grows from baseline (NOT a fill swap on cream)

**Form gate** (`/contatti/`): scope-meeting shape · 3 fields:
1. Scope familiare (free text · 1-2 sentences placeholder: "Ci dica brevemente la struttura attuale e la sua preoccupazione di continuità")
2. Orizzonte temporale (select · 5y / 10y / 25y / multi-generazionale)
3. Struttura attuale (select · holding / fondazione / trust / patto di famiglia / nessuna formalizzata)

NO P.IVA + CF (Fiscus collision). NO ICF code-of-ethics referenced (Solaria's). NO NDA-ready boardroom form (Pragma's). The horizon-selector is the differentiating field.

**CTA copy banlist respected**:
- NOT "Get started free" · NOT "Sign up now" (CS-CTA-02)
- NOT "Fissa una call privata" (Pragma)
- NOT "Primo appuntamento" (Fiscus)
- NOT "Prenota una discovery call" (Solaria)
- NOT "Iscriviti gratis" / "Free trial" (banlist)

---

## 8 · What makes the output PREMIUM in visible terms

Concrete, not vibes. A reviewer should see these in the live walk.

1. **Generous restraint**: 100×72 section padding · 1400 max-width · 96-100px vertical rhythm. The whitespace IS the rhythm; compressing it is the most common silent quality loss (`reference-pack §8`).
2. **Editorial italic on a single load-bearing word per heading**: `<em>generazioni</em>` in the hero, no bold, no uppercase, no color shift. CS-TYPE-02. A reviewer scanning the page sees one italic per heading and reads it as restraint.
3. **The hero photo is object-led + carries a credit overlay**: `(Custodi del mandato · Iscrizione Albo Trustees)` — moves the photo from "stock" to "editorial" and explicitly opts out of the boardroom/desk/1:1 sibling triangle.
4. **One dark band on home (the KPI band)**: editorial punctuation. Two dark bands reads aggressive; three reads SaaS funnel. CS-TONE-03.
5. **Outline-on-cream + filled-on-dark CTA polarity**: the polarity inversion is the cluster's signature. Visible at first scroll because the hero CTA is outline and the closer CTA is filled.
6. **`:focus-visible` brass ring at 2px / 4px offset**: keyboard tab through the navbar, see the cluster's interactive signature. CS-NAV-02 / E1.
7. **Tabular numerals on every KPI**: `18` and `2 700` align cleanly across IT/EN/FR/ES/AR. Invisible until you compare locales side-by-side; once you do, the alternative looks broken.
8. **Cream paper + pine type**: cream is the cluster's "paper" tone. Body type sits on cream at 1.6 line-height. Reads as a printed quarterly, not a SaaS dashboard.
9. **No 4-up grid on hero**: single editorial photo · no card collage · no parallax · no video background. The hero is one image, full-bleed-right, deeply cropped.
10. **AR locale ships with Kufi heading + Amiri body + RTL via logical properties**: the multi-locale handles RTL parity at runtime, not via duplicate CSS. CS-RESPONSIVE-08 / CS-TYPE-06.
11. **The "remove the studio name" test passes**: if you delete "Continua" everywhere, the page still reads as a real stewardship family office — not as "any premium firm." CS-TONE-05.
12. **Mid-strip names a CADENCE, not a number**: `Cadenza CdF · 4 riunioni / anno` reads as the firm's calendar, not as a metric. The first stakeholder reads it and instantly understands the firm operates on a multi-year governance loop, not a quarterly engagement.

---

## 9 · What this dry-run output is NOT

- Not a real `template_dna.py` entry (no app-code change in this branch)
- Not a real seed file write (the build phase A.5 would do that)
- Not a curator-approved Pexels pack (real Pexels URLs only emerge at A.3 with the cross-cluster grep on file)
- Not a copy diff (A.4 produces the IT locale tree)
- Not a critique or walk verdict (A.6/A.7)
- Not a scorecard (A.9)

It IS: a complete-enough planner-brief equivalent that a real workflow A pass could pick up at A.3 with no re-spec. The intake is signed. The DNA is concrete. The differentiation is non-trivial. The premium moves are listed and defendable.

If a real candidate survived an intake to this level of specificity, the orchestrator would route to:
- A.3 imagery-curator (with this pack spec as input)
- A.4 copy-translation (with this voice anchor + em-word)
- A.5 template-builder (with this DNA + section sequence + nav/footer specs)

— in that order, gates between each step, no skipping.
