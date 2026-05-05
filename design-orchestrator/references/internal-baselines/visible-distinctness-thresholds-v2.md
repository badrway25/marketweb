# Visible-distinctness thresholds v2

```yaml
file_type:    internal-baseline · table-driven threshold reference
status:       v2 · paper-only · paired with anti-clone-2.0-rules.md
                (the rule book) and corporate-suite-retrofit-priority-plan.md
                (the application)
date:         2026-05-05
audience:     orchestrator at every intake · planner at workflow A.1 · style-
                critic at A.6 · browser-verifier at workflow C/D · release-
                gatekeeper at flip
purpose:      single-page reference the orchestrator and planner read at every
                intake to compute the new sibling's distinctness score against
                the existing cluster. Replaces the v1.0 4/5+4/9 scoring;
                inherits CS-LAYOUT-12 § decision near-occupant ladder; adds 6
                new axes + critical-axis vetoes + within-family variance
                rules
companion:    factory/reports/hardening/anti-clone-2.0-rules.md (the rule book
                · 18 axes · scoring · vetoes)
              factory/reports/hardening/corporate-suite-retrofit-priority-plan.md
                (Causa retrofit · LF-2 family variance rules)
              factory/reports/hardening/premium-dynamic-pattern-library.md
                (motion gravity G1-G6 · 48 patterns referenced in axes 17 + 18)
              design-orchestrator/references/internal-baselines/corporate-suite-
                {distinctness-matrix,reference-pack,layout-family-assignment,
                live-family-map}.md (v1.0 references this v2 supersedes for
                scoring · v1.0 retains for narrative)
maintenance:  monotonically extended at every new sibling ship · at every
                hardening pass · NEVER truncated · deprecations carry forward
                with date and pointer to replacement
```

---

## §1 · The 18 axes · table-driven reference

| # | Axis | What is scored | Score range | Critical? |
|---|---|---|---|---|
| 1 | Hero geometry (L1) | structural shape | 0-3 | — |
| 2 | Hero subject 1-second read | subject class | 0-3 | **CRITICAL · ≥ 2** |
| 3 | Hero color temperature | warm / cool / mixed register | 0-3 | — |
| 4 | Section sequence (L2) | atom order | 0-3 | — |
| 5 | Mid-strip differentiator (L3) | absent / slot-N / cell shape | 0-3 | — |
| 6 | Pillars / narrative treatment (L4) | numbered-grid / essay / manifesto / 4-pillar | 0-3 | — |
| 7 | KPI placement + cell shape (L5) | band / overlay + cell tuple | 0-3 | — |
| 8 | Leadership presence + composition (L6) | type + composition sub-axis | 0-3 | — |
| 9 | Cases-preview shape (L7) | list-row / magazine-grid / timeline / numbered-ledger / etc. | 0-3 | — |
| 10 | Navbar geometry + chrome (L8) | sticky-top / split-wordmark / condensed-minimal | 0-3 | — |
| 11 | Footer structure + content (L9) | 3-col / 4-col-with-whistleblowing | 0-3 | — |
| 12 | Voice anchor noun + recurrence | em-noun + recurrence count | 0-3 | **CRITICAL · ≥ 3** |
| 13 | CTA mental model + inflection family | mental model + verb-class | 0-3 | **CRITICAL · ≥ 2** |
| 14 | Audience verb register | interview / read / schedule / explore / etc. | 0-3 | — |
| 15 | Palette polarity + accent deployment | macro tone + accent surface class | 0-3 | — |
| 16 | Typographic envelope | combined feel · italic-em / display-condensed / kinetic / etc. | 0-3 | — |
| 17 | Imagery register | composed-restraint / fullbleed-EXIF / product-in-context / etc. | 0-3 | **CRITICAL · ≥ 2** |
| 18 | Motion gravity + page choreography | G1-G6 + which patterns fire | 0-3 | **CRITICAL · ≥ 2** |

**5 critical axes.** A pair fails iff ANY critical axis is below its
veto floor, regardless of total. (Voice anchor at 3 because the cluster
contract requires a sibling-distinct anchor; the others at 2 because
adjacent-register pairs are acceptable.)

---

## §2 · Per-axis scoring rubric

### Axis 1 · Hero geometry (L1)
| Score | Examples |
|---|---|
| 0 | both stacked-editorial · both split-55-45 |
| 1 | both 55/45 sub-family but with different meta-strip placement |
| 2 | one stacked-editorial vs one type-only (related register) |
| 3 | one stacked-editorial vs one object-overlay · or split-55-45 vs side-rail-photo |

### Axis 2 · Hero subject 1-second read (CRITICAL)
| Score | Examples |
|---|---|
| 0 | both boardroom long-table · both library reading-room |
| 1 | both interior-architectural-empty (e.g., courtroom + library reading-room) |
| 2 | one interior chamber vs one exterior architectural |
| 3 | one boardroom-with-people vs one product-in-context · or institutional-interior vs cinematic-exterior |

### Axis 3 · Hero color temperature
| Score | Examples |
|---|---|
| 0 | both warm-mahogany · both cool-clerestory |
| 1 | both cool-with-warm-display-accent |
| 2 | warm-stone vs cool-clerestory (one notch apart) |
| 3 | warm-mahogany vs cool-no-warm |

### Axis 4 · Section sequence (L2)
| Score | Examples |
|---|---|
| 0 | both sequence A · both sequence B |
| 1 | A vs A+slot4 (within-family near-occupant) |
| 2 | A vs B (different but related) |
| 3 | A vs D (cross-family) |

### Axis 5 · Mid-strip differentiator (L3)
| Score | Examples |
|---|---|
| 0 | both `absent` · both `slot-4` with same cell |
| 1 | both `slot-4` with different cell · OR both `absent` with different mechanism |
| 2 | `absent` vs `slot-4` |
| 3 | `slot-2 governance-cycle` vs `absent` (different mechanism + different slot) |

### Axis 6 · Pillars / narrative treatment (L4)
| Score | Examples |
|---|---|
| 0 | both essay-with-anchors · both numbered-grid 3-up |
| 1 | both numbered-grid with different cell count (3 vs 4) |
| 2 | numbered-grid vs essay-with-anchors |
| 3 | manifesto-replacement vs 4-pillar 2x2 with icons |

### Axis 7 · KPI placement + cell shape (L5)
| Score | Examples |
|---|---|
| 0 | both hero-overlay 3-cell · both band-at-3 with same cells |
| 1 | both hero-overlay with different cells (Cornice vs Causa today) · OR both band-at-3 with different cells (Pragma vs Fiscus) |
| 2 | hero-overlay vs band-at-3 · OR band-at-3 vs band-at-5 with different cells |
| 3 | hero-overlay vs band-at-closer · narrative-prose-replacement vs band |

### Axis 8 · Leadership presence + composition (L6)
| Score | Examples |
|---|---|
| 0 | both single-portrait · same composition (seated-at-desk · same gender · same room) |
| 1 | both single-portrait with different gender + different cell content (Cornice + Causa today) |
| 2 | both single-portrait with different composition (seated-at-desk vs standing-at-shelf) · OR typographic-grid-3-card vs typographic-grid-4-card |
| 3 | single-portrait vs absent · single-portrait vs pillar-photo · absent vs typographic-grid |

### Axis 9 · Cases-preview shape (L7)
| Score | Examples |
|---|---|
| 0 | both list-row · both magazine-grid 3+1 with same composition |
| 1 | both magazine-grid 3+1 with different photos and copy (Cornice vs Causa today) |
| 2 | both magazine-grid with different sub-pattern layered (e.g., Cornice static vs Causa with EVID-3 case-citation-pop) |
| 3 | list-row vs magazine-grid · timeline vs filterable-grid |

### Axis 10 · Navbar geometry + chrome (L8)
| Score | Examples |
|---|---|
| 0 | both split-wordmark-top cream-paper · both sticky-top primary |
| 1 | both split-wordmark-top with different accent fill (Cornice rust vs Causa bottle-green) |
| 2 | both split-wordmark-top with one shipping NAV-1 sticky-condensed vs static (Cornice + Causa post-retrofit) |
| 3 | split-wordmark-top cream vs sticky-top primary · condensed-minimal vs side-rail |

### Axis 11 · Footer structure + content (L9)
| Score | Examples |
|---|---|
| 0 | both 3-col with same column content · both 4-col-with-whistleblowing with same channel |
| 1 | both 4-col-with-whistleblowing with different sub-cluster channel content (Cornice arch + Continua stewardship + Causa forensic) |
| 2 | both 4-col but with different column ordering · OR 3-col vs 4-col |
| 3 | 4-col-with-whistleblowing vs 3-col vs condensed-single-row |

### Axis 12 · Voice anchor noun + recurrence (CRITICAL · ≥ 3)
| Score | Examples |
|---|---|
| 0 | both `argomento` cognate · both `generazioni` cognate (banned by CS-EXEC-01 cluster contract) |
| 1 | one curatorial-thesis-cognate vs one (banned at v1.0) |
| 2 | one curatorial-thesis vs one stewardship-temporal (banned at v1.0) |
| 3 | distinct voice-anchor noun classes (`argomento` vs `evidenza` vs `generazioni` vs `terapia/consulenza`) |

### Axis 13 · CTA mental model + inflection family (CRITICAL · ≥ 2)
| Score | Examples |
|---|---|
| 0 | identical inflection AND identical mental model |
| 1 | same inflection family (Apri-X) different mental model (fascicolo-bound vs parere-screening) — Cornice + Causa today |
| 2 | different inflection family (Apri-X vs Sottometti-X · Apri-X vs Prenota-X) · OR same family but distinct mental model with different gate |
| 3 | different mental model + different inflection family + different gate (e.g., private-call NDA vs ship-log-feed) |

### Axis 14 · Audience verb register
| Score | Examples |
|---|---|
| 0 | both `interview` · both `read` |
| 1 | both deliberative (read · plead · interview · schedule — same broader mode) |
| 2 | adjacent (interview vs schedule · read vs plead) |
| 3 | different mode entirely (deliberative vs energetic · `interview` vs `ship` or `taste` or `play`) |

### Axis 15 · Palette polarity + accent deployment
| Score | Examples |
|---|---|
| 0 | identical palette tokens AND identical surface deployment |
| 1 | both warm-display-accent (Cornice rust + Continua brass display class shared but distinct surface) |
| 2 | one full-cool vs one cool-with-warm-display-accent |
| 3 | full-cool (Pragma navy + emerald) vs cool-with-warm-chrome-metallic (Continua pine + brass) vs matte-on-matte-zero-metallic (Causa bottle-green + obsidian) |

### Axis 16 · Typographic envelope
| Score | Examples |
|---|---|
| 0 | identical envelope AND identical fonts |
| 1 | identical envelope (italic-em + cream + restraint) different fonts (Cornice Cormorant + Source Sans 3 vs Causa GT Sectra + Manrope) |
| 2 | adjacent envelope (italic-em editorial vs italic-em with kinetic-display-accent) |
| 3 | different envelope (italic-em editorial vs sprint-console kinetic vs cinematic-EXIF dark) |

### Axis 17 · Imagery register (CRITICAL · ≥ 2)
| Score | Examples |
|---|---|
| 0 | identical register AND identical pool |
| 1 | identical register (composed-restraint Pexels editorial) different sub-cluster pool (Cornice exterior architectural vs Causa interior chamber) |
| 2 | adjacent register (composed-restraint editorial vs composed-restraint maker-in-frame) · OR same register with one shipping a unique pattern (e.g., EVID-5 provenance-tooltip differentiator) |
| 3 | different register (composed-restraint editorial vs fullbleed-EXIF cinematic vs product-in-context vs UI-led) |

### Axis 18 · Motion gravity + page choreography (CRITICAL · ≥ 2)
| Score | Examples |
|---|---|
| 0 | identical gravity AND identical patterns enabled (Cornice + Causa today: G2 editorial · same EDIT-1/2/3/4 set) |
| 1 | identical gravity with different sub-patterns (e.g., Cornice G2 with QUOTE-1 only vs Causa G2 with QUOTE-1 + KPI-2) |
| 2 | identical gravity with materially different page-choreography pattern set (Cornice G2 with EDIT-1/2/3/4 · Causa G2 with EDIT-1/2/3/4 + EVID-3 + TIME-3 — Causa post-retrofit) |
| 3 | different gravity (G2 editorial vs G5 sprint-console · G3 institutional vs G6 cinematic) |

---

## §3 · Threshold ladder · binding

The pair-distinctness threshold depends on family relationship:

| Pair relationship | Total threshold | Critical-axis veto applies? |
|---|---|---|
| **Cross-family** (different L1-L9 family) | **≥ 36/54 (66%)** | yes · all 5 vetoes |
| **Near-occupant** (same family but L cell differs · e.g., LF-1 + LF-3 = LF-1 with slot-4 added) | **≥ 30/54 (56%)** | yes · all 5 vetoes |
| **Within-family second-occupant** (same L1-L9 tuple verbatim · e.g., 2nd LF-2 occupant) | **≥ 27/54 (50%)** | yes · all 5 vetoes |

Below threshold = "too related" = retrofit OR re-spec required.

Critical-axis veto is applied independently of total. A pair scoring
high on aggregate that fails ANY critical axis is "too related."

---

## §4 · Six-class sameness diagnostic vocabulary

(Cross-reference with `anti-clone-2.0-rules.md §5`. Same definitions ·
this section is the orchestrator's at-intake quick reference.)

| Class | Definition | Verdict | Example |
|---|---|---|---|
| **S1** Acceptable family inheritance | shared L1-L9 cells flowing from family choice | acceptable | Cornice + Causa axis 1 (stacked-editorial · LF-2 family) |
| **S2** Premium coherence | shared cluster-contract signals | acceptable | every corporate-suite sibling sharing CS-RHYTHM-01 padding |
| **S3** Safe reuse | shape shared · content sibling-distinct | acceptable | 4-col-with-whistleblowing footer used by Cornice + Continua |
| **S4** Unhealthy family sameness | within-family cells that COULD differentiate but don't | retrofit at sibling level | Cornice + Causa axis 18 (motion + page choreography identical · could differ via EVID-3 + TIME-3) |
| **S5** Clone-like resemblance | critical-axis veto fail | re-spec or major retrofit | Cornice + Causa axis 13 (CTA inflection family identical · veto fails) |
| **S6** Overused premium tropes | cluster-wide sameness signal across all siblings | resolve at cluster level (Phase X.7a new cluster) | all 6 corporate-suite using composed-restraint Pexels editorial |

---

## §5 · Eight named-axis divergence floors (per-cluster · binding)

These are the per-axis floors a sibling MUST clear vs every other
sibling in the cluster. Cross-references `anti-clone-2.0-rules.md §6`.

### Hero divergence
- L1 + subject + color temp axes (1+2+3) **combined ≥ 5/9** between any pair.
- Floor failure example: Cornice + Causa = 0+2+2 = 4 · FAIL · either subject
  (axis 2) or color temp (axis 3) must rise to 3.

### Nav divergence
- Axis 10 ≥ 2 between any pair.
- Floor failure example: Cornice + Causa axis 10 = 1 (split-wordmark-top
  cream-paper · different accent fill only) · FAIL · second-occupant
  must enable a within-cell sub-variant (NAV-1 sticky-condensed).

### Proof system divergence
- Axis 7 ≥ 2 between any pair.
- Floor failure example: Cornice + Causa axis 7 = 1 (hero-overlay 3-cell
  shared shape · different cells) · FAIL · KPI-2 count-up + cell-semantic-
  class shift required.

### Case-preview divergence
- Axis 9 ≥ 2 between any pair.
- Floor failure example: Cornice + Causa axis 9 = 1 (magazine-grid 3+1
  shared · different cards) · FAIL · pattern layered on top required
  (EVID-3 for Causa).

### Leadership divergence
- Axis 8 ≥ 2 between any pair.
- Floor failure example: hypothetical 3rd LF-2 occupant with seated-at-
  desk identical to Cornice OR Causa · FAIL · composition variation
  required.

### Motion divergence (CRITICAL)
- Axis 18 ≥ 2 between any pair.
- Floor failure example: every corporate-suite pair currently scores
  axis 18 ∈ {0, 1} · CLUSTER-WIDE FAIL · S6 cluster-level resolution
  required (Phase X.7b).

### CTA divergence (CRITICAL)
- Axis 13 ≥ 2 between any pair.
- Floor failure example: Cornice + Causa axis 13 = 1 · FAIL · inflection-
  family shift required (Apri-X → Sottometti-X).

### Page-choreography divergence (CRITICAL · sub-axis of 18)
- Per axis 18.

---

## §6 · Per-cluster baseline (snapshot at 2026-05-05)

Quick lookup of every cluster's current 18-axis state and what's
locked vs differentiable.

### Corporate-suite (LF-1 · Pragma · LF-2 · Cornice + Causa · LF-3 · Fiscus · LF-4 · Solaria · LF-5 · Continua)

| Axis | All-sibling shared signal | Within-cluster distinguishable | Cluster-level resolution path |
|---|---|---|---|
| 1 hero geometry | NO (5 distinct geoms in 6 siblings) | yes | within-family second-occupant (rare) |
| 2 hero subject | NO | yes (sibling-specific subject) | per-sibling |
| 3 hero color temp | NO | yes | per-sibling |
| 4-11 layout cells | varies per L · most distinct | yes per family | family choice |
| 12 voice anchor | NO (6 distinct nouns) | yes | per-sibling |
| 13 **CTA inflection family** | YES — all "Apri/Fissa/Avvia + abstract noun" | within-family pair fails veto today | Phase X.7a (new cluster brings new inflection class) |
| 14 audience verb | YES — all deliberative | per-sibling differentiation possible (interview vs read vs schedule vs declare vs entrust vs plead) | Phase X.7a (new cluster brings active-verb class) |
| 15 palette | NO (6 distinct palettes) | yes | per-sibling |
| 16 **typographic envelope** | YES — all italic-em + cream + restraint | NOT differentiable inside cluster | Phase X.7a (new cluster declares alternate envelope) |
| 17 **imagery register** | YES — all composed-restraint Pexels editorial | NOT differentiable inside cluster | Phase X.7a (new cluster brings non-editorial register) |
| 18 **motion + choreography** | YES — all G2/G3 quiet-editorial | NOT differentiable inside cluster · except via per-pattern enable/disable (e.g., EVID-3, TIME-3) | Phase X.7b (motion_profile DNA dimension + 2 alternate gravities) |

**Summary**: 4 cluster-wide sameness signals (axes 13 · 14 · 16 · 17 ·
18) cannot be resolved inside corporate-suite. Phase X.7a + Phase X.7b
together resolve them.

### Other clusters · projected baseline (when first hardening pass lands)
- **agency-creative-studio** (Vertex · projected G2 + editorial-agency
  envelope): brings axis-16 envelope alternative (kinetic-italic-pull-
  quote · serif-index-asterisk).
- **agency-digital-studio** (Aura · projected G5 + sprint-console envelope):
  brings axis-13 CTA inflection class (`[ AVVIA SESSIONE ]` · sprint-chip)
  AND axis-14 audience verb class (`ship` · `track` · `deploy`) AND
  axis-17 imagery register (UI-led · dashboard mock · live-data) AND
  axis-18 motion gravity (G5 · live-counter · scroll-progress · magnetic-
  button).
- **portfolio-cinematic** (Pixel · projected G6 + cinematic envelope):
  brings axis-17 register (fullbleed-EXIF dark cinematic) AND axis-18
  motion gravity (G6 · cinematic-fade · parallax-restrained · gallery-
  snap · cursor-vignette) AND axis-14 audience verb class (`watch` ·
  `view`).
- **real-estate-ultra-luxury**: brings axis-17 register (fullbleed-
  editorial-cover champagne) AND axis-13 CTA class (`Visualizza dossier`
  · `Richiesta privata`).

A new cluster ship resolves 4-5 of corporate-suite's S6 axes simultaneously.

---

## §7 · Within-family variance rules · LF-2 (Cornice + Causa)

LF-2 family-internal variance rules · paper proposal · binding once
ratified by orchestrator-side commit (Phase X.7d).

### AC-V1 [REQUIRED] · Within-cell sub-variant adoption
A 2nd LF-2 occupant MUST adopt at least 3 of the following within-cell
sub-variants vs Cornice (the 1st occupant):
- NAV-1 sticky-condensed-on-scroll (Cornice ships static).
- EVID-3 case-citation-pop on magazine cards.
- TIME-3 chronological-tick-horizontal in narrative.
- QUOTE-4 sticky-stack-rotate replacing static pull-quotes.
- EDIT-2 pull-quote-em-reveal with longer-delay variant.
- KPI-2 count-up animation on hero overlay.
- EVID-5 provenance-tooltip on hero photo.

### AC-V2 [REQUIRED] · Portrait composition divergence
A 2nd LF-2 occupant's leadership portrait composition MUST differ from
the 1st on at least 2 of:
- subject posture (seated vs standing vs working-at-desk).
- subject activity (reading vs writing vs reviewing vs holding tools).
- room props (drafting tools vs codex vs blueprints vs ledgers vs
  bookshelves).

### AC-V3 [REQUIRED] · CTA verb-class divergence
A 2nd LF-2 occupant's CTA inflection MUST differ from the 1st on the
verb-class axis. The verb classes:
- Apri-X (open · taken by Cornice with `Apri un fascicolo progetto`).
- Sottometti-X (submit · open for 2nd LF-2).
- Richiedi-X (request · open).
- Prenota-X (book · taken by Solaria · forbidden for LF-2).
- Avvia-X (initiate · taken by Continua · forbidden for LF-2).
- Fissa-X (fix · taken by Pragma · forbidden for LF-2).

### AC-V4 [REQUIRED] · KPI cell semantic-class divergence
A 2nd LF-2 occupant's KPI cell tuple MUST differ from the 1st on at
least one cell semantic class:
- period-anchored cell (e.g., `2008` · `dal 1995`).
- count-cell (e.g., `90 fascicoli` · `28 sentenze`).
- publication-anchored cell (e.g., `38 menzioni` · `14 in massimario`).
- achievement-anchored cell (e.g., `prima donna OAPPC Milano`).
- year-range cell (e.g., `31 anni`).

### AC-V5 [GUIDELINE] · 3rd-occupant cumulative ladder
A 3rd LF-2 occupant MUST clear AC-V1..AC-V4 vs BOTH the 1st AND 2nd
occupants. The cumulative within-family distinctness ladder.

These rules apply to LF-2 specifically (Cornice + Causa). Per-family
variance rules for other layout families (LF-1 + LF-3 + LF-4 + LF-5)
are authored at each cluster's hardening pass.

---

## §8 · How a planner uses this catalog at intake

At workflow A.1 (new sibling intake):

1. **Identify the new sibling's family** (LF-1 · LF-2 second occupant ·
   LF-6 · LF-{NEW} · or new cluster).
2. **Identify the family relationship** with every existing sibling in
   the cluster (cross-family · near-occupant · within-family-second-
   occupant).
3. **Apply the appropriate threshold** per §3 (36 · 30 · 27).
4. **Score the new sibling's draft DNA** on all 18 axes vs each existing
   sibling using §2 rubric.
5. **Verify all 5 critical-axis vetoes** clear.
6. **Verify the 8 named-axis floors** clear (§5).
7. **For within-family pairs**, verify §7 family variance rules clear.
8. **Append the scored matrix to the planner brief** (extends
   `corporate-suite-distinctness-matrix.md`).

If any check fails, re-spec required at A.2 plan stage.

---

## §9 · Per-workflow-stage gate firing

| Workflow stage | What is verified |
|---|---|
| A.1 intake | full 18-axis scoring vs every existing sibling · all critical-axis vetoes · threshold ladder · within-family variance rules |
| A.5 build | builder verifies declared scores match implementation (e.g., declared "axis 18 = 2 via EVID-3 + TIME-3" actually ships those patterns) |
| A.6 critique | style-critic re-runs the 18-axis matrix on rendered home + 4 inner pages · confirms post-build score matches A.1 declared |
| Workflow C/D walk | browser-verifier emulates `prefers-reduced-motion` · re-walks distinctness check at each locale · BRWS-DISTINCT-* rubric checks |
| Release-gatekeeper at flip | aggregated 18-axis score is part of scorecard · flip blocked if any critical-axis veto unresolved |

---

## §10 · Maintenance protocol

- New sibling at intake adds a new column to the cluster's distinctness-
  matrix and a new row of 18 scores per existing sibling.
- New cluster at first hardening pass adds a new row to §6 (per-cluster
  baseline) and a new section in §7 (within-family variance rules per
  family).
- New axis added (axis 19+) requires a § decision at orchestrator-side.
  The 18-axis matrix is monotonic; new axes extend, never replace.
- Threshold ladder (36/30/27) revisited at each catalog-size milestone
  (10 · 25 · 50 templates). The ladder may tighten as the catalog
  grows.
- Critical-axis vetoes (5 axes · §1) are immutable. Adding a 6th critical
  axis requires § decision.

---

## §11 · One-paragraph summary

Anti-clone 2.0 ships an 18-axis distinctness scoring model with 5
critical-axis vetoes (voice anchor ≥ 3 · CTA mental model + inflection
≥ 2 · hero subject ≥ 2 · imagery register ≥ 2 · motion gravity + page
choreography ≥ 2). Threshold ladder 36/30/27 per cross / near-occupant
/ within-family pair. 8 named-axis floors (hero · nav · proof · case-
preview · leadership · motion · CTA · page choreography) · each with
its own minimum. Six-class sameness vocabulary (S1 family inheritance
· S2 cluster contract · S3 safe reuse · S4 unhealthy family sameness ·
S5 critical-axis fail · S6 overused tropes) · S1+S2+S3 acceptable · S4
+ S5 retrofit at sibling level · S6 cluster-level Phase X.7a + X.7b
resolution. LF-2 family variance rules (AC-V1..V5) formalised here for
2nd-occupant within-cell diversification. Each new sibling scored at
A.1 intake against every existing sibling using §2 rubric; any veto
fail blocks A.5 build. Pragma + Fiscus accepted-as-grandfathered
under 2.0 with carry-over § decision · Cornice + Causa retrofit at
Phase X.7d · the system is NOT ready for sibling 7 today; readiness
follows Causa retrofit + LF-2 variance rules + Phase X.7b
implementation.
