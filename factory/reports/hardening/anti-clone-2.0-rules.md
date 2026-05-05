# Anti-clone 2.0 rules

```yaml
report_type:        hardening · paper-only · binding rule-system
date:               2026-05-05
agent:              orchestrator-side authoring (Phase X.7d hardening · post-
                    audit / pattern-library / personalization-architecture trio)
trigger:            user signal that recent templates still feel too similar ·
                    treated as load-bearing per ORCHESTRATOR.md §6.10
zero_code:          paper only · no apps/* · no template touches · no tier
                    change · no registry change
companion files:
  - factory/reports/hardening/premium-dynamic-personalization-audit.md
    (the audit · §10 named "feels samey" as load-bearing)
  - factory/reports/hardening/current-template-factory-drift-map.md
    (32 specific repeated patterns across the latest 6)
  - factory/reports/hardening/premium-dynamic-pattern-library.md
    (motion gravity G1-G6 · 48 named patterns · the source of new axes 17 + 18)
  - factory/reports/hardening/template-personalization-architecture.md
    (4-layer model · the customization side of the same problem)
  - factory/reports/hardening/corporate-suite-retrofit-priority-plan.md
    (companion · names which siblings retrofit first)
  - design-orchestrator/references/internal-baselines/visible-distinctness-thresholds-v2.md
    (companion · table-driven threshold reference for orchestrator at intake)
  - design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md
    (the v1.0 12-dim scoring · this rule book extends to 18-axis)
  - design-orchestrator/references/internal-baselines/corporate-suite-live-family-map.md
    (5-sibling state)
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md
    (LF-2 1st-occupant reference · binding for Causa retrofit)
  - factory/reports/hardening/corporate-suite-layout-{divergence-plan,variance-rules,family-matrix}.md
    (existing CS-LAYOUT-* rule book · CS-LAYOUT-12 ≥4/9 is what 2.0 raises)
  - factory/reports/causa/causa-a6-it-review-lock.md (most recent A.6 close)
status_tag:         RULES-V2 · 18-axis · 0-3 scoring · critical-axis veto · published
verdict:            The current 4/5-skin + 4/9-layout rules pass templates that
                    feel similar at first scroll. The new 18-axis scoring catches
                    the gap at ≥36/54 cross-family + ≥27/54 within-family + 5
                    critical axes that must each ≥2. Cornice ↔ Causa scores 21/54
                    today (well below threshold · 2 critical axes failed).
                    Pragma ↔ Fiscus scores 22/54 (already documented near-occupant
                    § decision). Both pairs require retrofit attention; only Causa
                    is still draft and retrofittable cleanly.
```

## §0 · Why 2.0 exists

The audit (`premium-dynamic-personalization-audit.md §3`) named six concrete
sameness signals that pass the existing distinctness gates:

1. One typographic envelope across all 6 corporate-suite templates.
2. One CTA inflection ("Apri / Fissa / Avvia + abstract noun").
3. One imagery register (composed-restraint Pexels editorial).
4. One motion contract (quiet-editorial · marquee 110s OR none · text fade-in).
5. One section-vocabulary atom set.
6. One audience-verb register (deliberative).

The existing v1.0 distinctness model scores against:
- **Layout L1–L9** at CS-LAYOUT-12 ≥4/9 different.
- **Skin axes** (voice · palette · imagery · typography · structure) at
  DISTINCTNESS_RULES ≥4/5.
- **12-dim distinctness matrix** (corporate-suite-distinctness-matrix.md
  §1.1–§1.12).

Both pass siblings that share all six sameness signals. The model is
correct as far as it goes — it scores correctly on layout/skin axes — but
it does NOT score the **visible-feel envelope** that emerges from the
combination of typography + motion + audience verb + page choreography
+ CTA inflection. That envelope is what the user senses.

Anti-clone 2.0 closes the gap by adding **6 new axes** to the existing
12, scoring each on a **0-3 scale**, applying a **total-points threshold**
PLUS **per-critical-axis veto**, and tightening the within-family rules
for second-occupants.

This rule book does NOT replace v1.0. It supersedes the v1.0 scoring
tables; the existing rule IDs (CS-LAYOUT-12 · DISTINCTNESS_RULES §1)
remain as floor checks. 2.0 is the upgrade.

---

## §1 · The 18 anti-clone 2.0 axes

Each axis is scored 0-3 between any two siblings. Higher = more distinct.
Axes 1–11 derive from the existing L1-L9 layout-family system + the
12-dim matrix. Axes 12–18 are new (hero subject 1-second read, audience
verb register, motion gravity, typographic envelope, CTA inflection
family, imagery register, page choreography).

| # | Axis | What is scored | v1.0 mapping |
|---|---|---|---|
| 1 | Hero geometry (L1) | structural shape: split-55-45 · stacked-editorial · object-overlay · side-rail-photo · type-only | L1 + matrix §1.5 |
| 2 | Hero subject 1-second read | what a visitor reads in the first 800ms (boardroom · empty-courtroom · library · portico · etc.) | matrix §1.6 |
| 3 | Hero color temperature | cool daylight · golden-hour · warm-mahogany · cool-clerestory · etc. | matrix §1.6 sub-axis |
| 4 | Section sequence (L2) | declared atom list per family | L2 |
| 5 | Mid-strip differentiator (L3) | absent · slot-2 · slot-4 · slot-5 · etc. | L3 + matrix §1.8 |
| 6 | Pillars / narrative treatment (L4) | numbered-grid · essay-with-anchors · manifesto-replacement · 4-pillar-matrix | L4 |
| 7 | KPI placement + cell shape (L5) | band-at-3 · band-at-4 · hero-overlay · with cell tuple distinct | L5 |
| 8 | Leadership presence + composition (L6) | typographic-grid · single-portrait-feature · pillar-photo · absent · WITH portrait composition for photo-bearing variants | L6 |
| 9 | Cases-preview shape (L7) | list-row · magazine-grid · timeline · numbered-ledger · filterable-grid · gallery-strip | L7 |
| 10 | Navbar geometry + chrome (L8) | sticky-top · split-wordmark-top · condensed-minimal-top · WITH chrome polarity | L8 |
| 11 | Footer structure + content (L9) | 3-col · 4-col-with-whistleblowing · WITH column content distinct | L9 |
| 12 | Voice-anchor noun + recurrence | em-noun + recurrence count (1 · 2 · 3 surfaces) | matrix §1.4 |
| 13 | **CTA mental model + inflection family** | mental model (private-call · scope-brief · scheduled-appointment · discovery-call · mandate-dialogue · parere-screening · etc.) AND inflection family (Italian-polite-imperative + abstract noun · transactional · invitational · concrete-action · conversational) | NEW (raised bar from §1.7) |
| 14 | **Audience verb register** | interview · read · schedule · declare · entrust · plead · explore · ship · buy · play · watch · taste · fit · visit | NEW |
| 15 | Palette polarity + accent deployment | macro tone + accent surface class (display-only · chrome-only · body-typographic-only · matte-on-matte) | matrix §1.2 + §1.3 |
| 16 | **Typographic envelope** | the COMBINED feel: serif italic-em + cream + restraint OR display-condensed + monospace OR variable-axis playful OR sans-display kinetic OR ... | NEW (raised from §1.4) |
| 17 | **Imagery register** | composed-restraint editorial OR fullbleed-EXIF cinematic OR product-in-context OR maker-in-frame OR UI-led OR illustration-led | NEW (raised from §1.6) |
| 18 | **Motion gravity + page choreography** | G1 / G2 / G3 / G4 / G5 / G6 from `premium-dynamic-pattern-library.md §1` AND which patterns fire (KPI-2? EVID-3? TIME-3? NAV-3?) | NEW |

The 6 axes named NEW are the audit's named sameness signals operationalised
into scoring.

---

## §2 · Scoring scale (0-3)

| Score | Meaning | Example |
|---|---|---|
| **0** identical | both siblings ship the exact same value | both stacked-editorial · both Cormorant Garamond · both "Apri un X" |
| **1** same sub-family | shared sub-class · differ only in surface content | both italic-em editorial typography · different fonts · same heading scale; OR same magazine-grid 3+1 with different photos |
| **2** adjacent | shared broader register · clearly separated sub-class | both deliberative verb but `read` ≠ `plead`; OR both editorial G2 motion but different patterns enabled; OR both architectural-empty hero but exterior vs interior |
| **3** distinct | structurally separate · the visitor would not confuse the templates on this axis | split-55-45 vs object-overlay; OR G2 editorial vs G5 sprint-console; OR private-call vs ship-log; OR composed-restraint Pexels vs fullbleed-EXIF dark cinematic |

The rubric is calibrated for the visitor's first-30-second read, NOT for
the planner's static-overlay test. Two templates with different content
in the same shape score 1, not 3.

---

## §3 · Threshold rules (binding)

### Total-points threshold
- **Cross-family pair** (different L1–L9 family): **≥ 36/54 distinct (66%)**
  to ship. Below this is "too related" — re-spec required.
- **Within-family second-occupant pair** (same L1–L9 family · e.g., Cornice ↔
  Causa both LF-2): **≥ 27/54 distinct (50%)**. The lower threshold
  acknowledges that family inheritance shares many cells by design;
  but 27 still requires meaningful diversification on axes 12-18.
- **Within-family near-occupant pair** (siblings in adjacent L-tuples ·
  e.g., LF-1 Pragma vs LF-3 Fiscus = LF-1 + slot-4 cell): **≥ 30/54**.
  This is the documented Pragma ↔ Fiscus § decision class.

### Critical-axis veto (independent of total points)
- **Voice anchor noun** (axis 12) MUST be ≥ 3 vs every other sibling. No
  exceptions. The voice anchor is the cluster's typographic identity
  signal.
- **CTA mental model + inflection** (axis 13) MUST be ≥ 2 vs every other
  sibling. (Same inflection family is allowed at within-family pairs;
  same mental model is not.)
- **Hero subject 1-second read** (axis 2) MUST be ≥ 2 vs every other
  sibling.
- **Motion gravity + page choreography** (axis 18) MUST be ≥ 2 vs every
  other sibling.
- **Imagery register** (axis 17) MUST be ≥ 2 vs every other sibling
  (a 7th `composed-restraint Pexels editorial` template is the audit's
  named risk).

If ANY critical axis fails, the pair is "too related" REGARDLESS of
total. The veto exists because total points can hide a single-critical-
axis failure that visibly dominates the rendered first-30-second read.

### Total-points + veto combined gates
A pair passes anti-clone 2.0 iff:
1. Total ≥ 36 (cross-family) / 30 (near-occupant) / 27 (within-family).
2. AND every critical axis is ≥ its veto floor.

---

## §4 · Real-world scoring of the 6 corporate-suite siblings

Applying the 18-axis scoring to the most informative pairs (15 pairs total ·
3 worth the full table for evidence).

### Pair 1 · Cornice (LF-2) ↔ Causa (LF-2 · 2nd occupant)
The user's named concern. Causa is still draft so retrofittable.

| # | Axis | Cornice | Causa | Score |
|---|---|---|---|---|
| 1 | Hero geometry | stacked-editorial | stacked-editorial | **0** |
| 2 | Hero subject | Bologna golden-hour portico (exterior · zero people) | Liverpool empty courtroom (interior · zero people) | **2** |
| 3 | Hero color temp | warm golden-hour stone | cool clerestory + bone-walls | **2** |
| 4 | Section sequence | B (essay-led) | B (essay-led) | **0** |
| 5 | Mid-strip | absent (essay covers) | absent (essay covers) | **0** |
| 6 | Pillars/narrative | essay-with-anchors + 3 pull-quotes + sticky 4-link side-rail | same as Cornice | **0** |
| 7 | KPI placement + cells | hero-overlay 3-cell `(novanta fascicoli · 2008 · 38 menzioni)` | hero-overlay 3-cell `(28 sentenze · 14 voci · 31 anni)` | **1** |
| 8 | Leadership shape | single-portrait-feature · seated · feminine (Marta Roveri) | single-portrait-feature · masculine (Lorenzo Marchetti) — composition currently identical to Cornice | **1** |
| 9 | Cases-preview | magazine-grid 3+1 with architectural cases | magazine-grid 3+1 with sentence cases | **1** |
| 10 | Navbar | split-wordmark-top cream-paper + filled-rust pill | split-wordmark-top cream-paper + filled-bottle-green pill | **1** |
| 11 | Footer | 4-col-with-whistleblowing · architecture-firm channel | 4-col-with-whistleblowing · forensic-firm channel | **1** |
| 12 | Voice anchor | `argomento → argument · argumento · حُجَّة` | `evidenza → evidence · preuve · evidencia · دليل` | **3** |
| 13 | CTA mental model + inflection | "Apri un fascicolo progetto" · scope-brief · Italian-polite-imperative | "Apri un parere preliminare" · parere-screening · Italian-polite-imperative | **1** |
| 14 | Audience verb | `read` (deliberative-receptive) | `plead` (deliberative-active) | **2** |
| 15 | Palette polarity + accent deployment | graphite + pietra-serena + warm-display-rust (display-side-only) | bottle-green + bone + obsidian (matte-on-matte · zero metallic · body-typographic-only) | **3** |
| 16 | Typographic envelope | Cormorant Garamond + Source Sans 3 + cream + italic-em + 84px rust drop-cap | GT Sectra + Manrope + cream + italic-em + 84px obsidian drop-cap | **2** |
| 17 | Imagery register | composed-restraint Pexels editorial · architectural-press subject pool | composed-restraint Pexels editorial · forensic-publication subject pool | **1** |
| 18 | Motion gravity + page choreography | G2 editorial · EDIT-1/2/3/4 · sticky 4-link side-rail | G2 editorial · EDIT-1/2/3/4 · sticky 4-link side-rail (currently identical) | **0** |

**Total: 21/54 = 39%.**

**Critical-axis check**:
- Voice anchor: 3 ✓
- CTA mental model + inflection: 1 ✗ **VETO FAIL**
- Hero subject: 2 ✓
- Motion gravity + page choreography: 0 ✗ **VETO FAIL**
- Imagery register: 1 ✗ **VETO FAIL**

**Verdict**: pair is too-related under v2.0. Three critical-axis vetoes
fail. Even at the within-family threshold of 27/54, the pair scores
21/54. **Retrofit required.** The critical-axis vetoes name the priority
retrofit surfaces (CTA · motion · imagery).

### Pair 2 · Pragma (LF-1) ↔ Fiscus (LF-3)
The documented near-occupant. Already § decision · ratified.

| # | Axis | Pragma | Fiscus | Score |
|---|---|---|---|---|
| 1 | Hero geometry | split-55-45 | split-55-45 | **0** |
| 2 | Hero subject | boardroom long-table | tidy desk + tax docs | **2** |
| 3 | Hero color temp | cool daylight | warm-neutral interior | **2** |
| 4 | Section sequence | A | A+slot4 | **1** |
| 5 | Mid-strip | absent | slot-4 fiscal-calendar | **3** |
| 6 | Pillars | numbered-grid 3-up | numbered-grid 3-up | **0** |
| 7 | KPI | band-at-3 (HQ · Equipe · Mandati) | band-at-3 (different cells) | **1** |
| 8 | Leadership | typographic 3-card | typographic 4-card ODCEC | **1** |
| 9 | Cases | list-row | list-row | **0** |
| 10 | Navbar | sticky-top primary | sticky-top primary | **0** |
| 11 | Footer | 3-col | 3-col | **0** |
| 12 | Voice anchor | decisional gravity (no single noun) | adempimento corretto | **2** |
| 13 | CTA | "Fissa una call privata" · private-call | "Primo appuntamento" · scheduled-appointment | **2** |
| 14 | Audience verb | interview | schedule | **2** |
| 15 | Palette | navy + emerald + cream | warm-neutral + blu-notte + gold | **3** |
| 16 | Typography envelope | Merriweather + Inter + cream + italic-em | IBM Plex Serif + IBM Plex Sans + cream + italic-em | **1** |
| 17 | Imagery register | composed-restraint editorial · executive boardroom pool | composed-restraint editorial · fiscal-desk pool | **1** |
| 18 | Motion gravity | G3 institutional · KPI-1 · marquee 110s | G3 institutional · KPI-1 · marquee 110s | **0** |

**Total: 21/54 = 39%.** (Same as Cornice ↔ Causa coincidentally.)

**Critical-axis check**:
- Voice anchor: 2 ✓ (acceptable adjacent-register)
- CTA mental model: 2 ✓
- Hero subject: 2 ✓
- Motion gravity: 0 ✗ **VETO FAIL**
- Imagery register: 1 ✗ **VETO FAIL**

**Verdict**: Pragma ↔ Fiscus also fails 2.0 vetoes. Pre-existing § decision
(CS-LAYOUT-12 near-occupant exception) handles the layout-axis side at
v1.0 level. **2.0 raises the bar**: under 2.0 even Pragma ↔ Fiscus would
need motion + imagery diversification to pass. Since Pragma is grandfathered
and Fiscus is shipped at hardening parity, the retrofit cost-benefit is
lower than for Causa (still draft).

### Pair 3 · Pragma (LF-1) ↔ Continua (LF-5)
The maximally-distant pair · sanity check the rubric.

(Without the full table for brevity, but every axis scored.)

| Axis | Score |
|---|---|
| 1 hero geometry · split-55-45 vs object-overlay | 3 |
| 2 hero subject · boardroom vs library reading-room | 3 |
| 3 hero color temp · cool daylight vs warm-mahogany | 3 |
| 4 section sequence · A vs D | 3 |
| 5 mid-strip · absent vs slot-2 governance-cycle | 3 |
| 6 pillars · numbered-grid vs 4-pillar 2x2 | 3 |
| 7 KPI · band-at-3 vs band-at-4 | 2 |
| 8 leadership · typographic 3-card vs pillar-photo 3 environmental | 3 |
| 9 cases · list-row vs timeline | 3 |
| 10 navbar · sticky-top vs condensed-minimal-top | 2 |
| 11 footer · 3-col vs 4-col-with-whistleblowing | 3 |
| 12 voice anchor · decisional gravity vs `generazioni` | 3 |
| 13 CTA · "Fissa una call" vs "Avvia un dialogo di mandato" | 3 |
| 14 audience verb · interview vs entrust | 3 |
| 15 palette · navy+emerald vs pine+pewter+brass | 3 |
| 16 typography envelope · Merriweather+Inter+cream+italic-em vs Crimson Pro+Public Sans+cream+italic-em | 1 (envelope same · pair distinct) |
| 17 imagery register · boardroom 1-4ppl vs library zero-ppl interior | 3 |
| 18 motion gravity · G3 marquee vs G4 static-no-marquee | 2 |

**Total: 50/54 = 93%.**

**Verdict**: well-distinct on every axis except typographic envelope (axis
16 = 1 because both are serif italic-em editorial restraint; the FONTS
differ but the envelope is shared). This is the audit's named gap
manifesting even at the maximally-distant pair: **the cluster's
typographic envelope is shared across all 6 siblings.** All cross-cluster
pairs score 3 on this axis once a non-corporate-suite cluster ships.

---

## §5 · Classification of sameness types (operational vocabulary)

Every sameness signal between two siblings falls into one of six classes.
The classification answers "should we worry about this?"

### S1 · Acceptable family inheritance
**Definition**: shared cells that flow from L1–L9 family choice. Two LF-2
siblings sharing stacked-editorial hero · essay-with-anchors · magazine-
grid · etc. **By design.**
**Verdict**: **acceptable.** Do not retrofit.
**Examples**: Cornice ↔ Causa axes 1, 4, 5, 6 (all 0 · all family-shared).

### S2 · Premium coherence
**Definition**: shared signals that derive from the cluster contract ·
serif italic-em · cream paper · 100×72 padding · `:focus-visible` gold
ring · tabular numerals · CS-RHYTHM-01.
**Verdict**: **acceptable.** This is the cluster's signature; removing
it breaks the cluster.
**Examples**: every corporate-suite sibling sharing CS-RHYTHM-01 padding;
every cluster sibling sharing the focus-ring spec.

### S3 · Safe reuse
**Definition**: a pattern (motion · component · structure) deliberately
re-used across siblings because it has been proved correct AND its content
is sibling-distinct. The shape is shared; the content carries the identity.
**Verdict**: **acceptable.** Sectors-ribbon shape across LF-1/3/4/5 ·
CTA closer cream variant on LF-2 · the magazine-grid 3+1 in LF-2 family.
**Examples**: 4-col-with-whistleblowing footer used by both Cornice and
Continua with different content (Cornice's architectural channel vs
Continua's stewardship channel).

### S4 · Unhealthy family sameness
**Definition**: cells that COULD differentiate at within-family level but
currently don't · siblings in the same family choosing the same sub-variant
even though the sub-variants are pre-built.
**Verdict**: **retrofit required.** This is the most common failure
class. The fix is sub-variant-within-cell diversification.
**Examples**: Cornice ↔ Causa axis 18 (motion + page choreography
identical · could differ via EVID-3 + TIME-3 unlock). Cornice ↔ Causa
axis 8 (leadership composition identical seated-at-desk · could differ
via standing-at-shelf or working-at-codex).

### S5 · Clone-like resemblance
**Definition**: a critical axis fails the veto. Two siblings that read
similar at first scroll because they share voice anchor noun OR CTA
mental model OR hero subject OR motion gravity OR imagery register.
**Verdict**: **re-spec required.** Cannot be hidden by other axes
scoring high.
**Examples**: a hypothetical 7th sibling with `argomento` cognate as
voice anchor (clone of Cornice on a critical axis even if all other
axes scored 3).

### S6 · Overused premium tropes
**Definition**: signals that are the cluster's identity but that, taken
together at six instances, produce the audit's named "tonal monoculture"
signal. Each individual trope is fine; the AGGREGATION across all
siblings reads as samey.
**Verdict**: **retrofit ONLY at the cluster level**, not per pair. The
fix is a NEW cluster (Phase X.7a per audit) — a new tonal envelope.
Retrofit within corporate-suite cannot resolve S6.
**Examples**: all 6 corporate-suite use composed-restraint Pexels editorial
imagery · all 6 use serif italic-em + cream paper · all 6 use deliberative
audience verb register. These individually pass v2.0 between any one pair;
the aggregation is the user signal.

### Operational rule
- S1 + S2 + S3 = **acceptable**. Do not retrofit.
- S4 = **retrofit at sibling level**. Within-cell sub-variant diversification.
  Score raise: typically +5 to +10 points per pair.
- S5 = **re-spec or major retrofit**. Critical-axis veto fail.
- S6 = **fix at cluster level**. Cannot be addressed inside the cluster.
  Phase X.7a (ship a non-corporate-suite cluster) is the only resolution.

---

## §6 · Eight named-axis divergence thresholds

For the 8 most-visible axes, here are the v2.0 minimum-divergence floors
between any two siblings in the cluster. (Companion file
`visible-distinctness-thresholds-v2.md` carries the detailed table; this
section names the operational rules.)

### Hero divergence · ≥ 5/9 across {L1 geometry · subject · color temp}
- L1 geometry score (axis 1) · subject score (axis 2) · color temp
  score (axis 3) · combined ≥ 5/9.
- **Floor**: 0 + 2 + 2 = 4 ≥ 5 FAIL · means at least one of {2, 3} must be 3.
- **Implication for Causa**: subject 2 + color temp 2 = 4 · same family = 0 ·
  total 4 · FAIL. Causa needs to push at least one of {2, 3} to 3 (e.g.,
  shift hero color temp from cool-clerestory to fully-cool-mahogany-free
  via a different photo treatment).

### Nav divergence · ≥ 2/3 (axis 10)
- Same family allowed for L8, but a within-family second occupant must
  enable at least one nav behavior pattern Cornice doesn't (NAV-1
  sticky-condensed · NAV-3 progress-bar light-touch).
- **Implication for Causa**: enable NAV-1 sticky-condensed (Causa's nav
  shrinks 76→60px on scroll while Cornice stays static). Score raise:
  axis 10 from 1 → 2.

### Proof system divergence · ≥ 2/3 (axis 7)
- KPI cell composition + KPI animation pattern · within-family pairs at
  least 2.
- **Implication for Causa**: Cornice ships static KPI overlay tuple
  `(novanta fascicoli · 2008 · 38 menzioni)`. Causa ships with KPI-2
  count-up enabled OR EVID-2 attestation-chip-hover on the KPI cells (a
  pattern Cornice doesn't ship · per pattern catalog). Score raise:
  axis 7 from 1 → 2.

### Case-preview divergence · ≥ 2/3 (axis 9)
- Within-family second occupants share the cases SHAPE (LF-2 magazine-grid
  is locked) · but must layer a distinct PATTERN on top.
- **Implication for Causa**: layer EVID-3 case-citation-pop on the magazine-
  grid (each card has expandable Cassazione citation). Cornice doesn't
  ship EVID-3 (architectural cases don't have published-record citations
  in the same forensic register). Score raise: axis 9 from 1 → 2.

### Leadership divergence · ≥ 2/3 (axis 8)
- Within-family second occupants share the L6 cell (single-portrait for
  LF-2). The portrait's COMPOSITION must differ — seated-at-desk · standing-
  at-shelf · working-at-codex · arms-crossed. AT LEAST ONE composition
  axis must differ.
- **Implication for Causa**: portrait should be a different composition
  from Cornice's seated-at-drafting-table. Working-at-codex-with-pen is
  the recommended composition (currently the Causa A.5b imagery shows
  a senior man reading a leather-bound codex at a stone desk — the
  composition differs sufficiently). Score raise: axis 8 from 1 → 2.

### Motion divergence · ≥ 2/3 (axis 18) · CRITICAL-AXIS VETO
- Within-family pairs MUST differ on motion + page choreography. Same
  motion gravity is acceptable but the PATTERNS enabled must differ.
- **Implication for Causa**: enable EVID-3 + TIME-3 (chronological-tick-
  horizontal in the narrative essay) + KPI-2 count-up on the KPI overlay
  · Cornice ships with none of these enabled. Score raise: axis 18 from
  0 → 2.

### CTA divergence · ≥ 2/3 (axis 13) · CRITICAL-AXIS VETO
- Within-family pairs MUST differ on CTA mental model AND/OR inflection
  family. Same mental model is allowed in v1.0 but FORBIDDEN in v2.0
  for any cross-pair.
- **Implication for Causa**: shift "Apri un parere preliminare" to a
  non-Apri inflection. Recommended replacement: "**Sottometti un parere
  preliminare**" (transactional · evidence-up-front register) OR
  "**Richiedi un parere preliminare**" (consultation-request · concrete-
  action register). Score raise: axis 13 from 1 → 2.

### Page-choreography divergence · ≥ 2/3 (axis 18 sub) · CRITICAL-AXIS VETO
- Same as motion divergence. The combined axis 18 must reach 2.

The above 8 named thresholds are formalised in
`visible-distinctness-thresholds-v2.md` with per-cluster sub-tables.

---

## §7 · The "do now / do later / never do" matrix

Per the audit + drift-map + this rule book, what changes are worth doing,
when, and what should never be done.

### DO NOW (Phase X.7d retrofit · paper-only at this pass · code in next pass)

| Action | Surface | Why | Cost |
|---|---|---|---|
| Causa CTA inflection shift (Apri → Sottometti / Richiedi) | axis 13 | resolves critical-axis veto fail vs Cornice | low (copy-only · 1 string per locale) |
| Causa enable EVID-3 case-citation-pop on magazine cards | axis 18 + axis 9 | resolves critical-axis veto fail · adds forensic differentiator | medium (pattern wire · 4 cards) |
| Causa enable TIME-3 chronological-tick-horizontal in narrative | axis 18 | adds page-choreography differentiation | medium (single section pattern) |
| Causa NAV-1 sticky-condensed | axis 10 | within-family nav differentiation | low (existing pattern · LF-5 already ships) |
| Codify LF-2 second-occupant within-cell variance rules | structural | prevents future LF-2 3rd-occupant from same trap | low (rule-book extension) |
| Authoring `motion_profile` DNA dimension paper-spec | infrastructure | unblocks Phase X.7b implementation | already done in pattern library |

### DO LATER (Phase X.7c · editor work · separate brief)

| Action | Surface | Why |
|---|---|---|
| Customer palette swap with constraint | axis 15 | named gap #5 in audit · highest customer value |
| Customer typography pair swap | axis 16 | second highest customer value |
| Imagery upload + smart-crop | axis 17 | unlocks customer differentiation without orchestrator |
| Section toggle preset library | structural | allows customer to reduce overlap with cluster siblings |
| Motion intensity preset (`minimal · standard · expressive`) | axis 18 | exposes audit gap #2 closure |

### DO LATER · CLUSTER-LEVEL (Phase X.7a · ship one new cluster)

| Action | Surface | Why |
|---|---|---|
| Ship 1 non-corporate-suite cluster at hardening parity | axes 14, 16, 17, 18 simultaneously | only resolution to S6 overused tropes |
| Author the new cluster's design-standard stack | structural | per-cluster standards-stack prerequisite |

### NEVER DO (banned · Layer D · architecturally refused)

| Action | Why |
|---|---|
| Migrate Causa from LF-2 to LF-{NEW} mid-cluster | breaks AC-1 LF-2 second-occupant inheritance contract · forces orchestrator-side family redeclaration · expensive · loses LF-2 family-fit benefits |
| Demote CS-TONE-03 across non-LF-2 families | LF-2's zero-dark-band demotion is family-scoped · porting it to LF-1/3/4/5 collapses cluster editorial-punctuation discipline |
| Lift the Pexels-only contract for "more imagery variety" | CS-IMG-SRC-01 invariant · drops cluster's image-quality floor |
| Add free hex / free font / free CSS controls to editor | Layer D bans per personalization-safety-rules.md §3 |
| Ship a 7th corporate-suite sibling without retrofitting Causa first | repeats audit gap #1 at 7 templates instead of 6 |
| Add a 7th sibling to corporate-suite without first shipping a non-cs cluster | extends S6 overused-tropes problem |
| Score against v1.0 (4/5 + 4/9) only after this rule book ships | leaves the named cluster collapse signals uncaught |

---

## §8 · The 10 most valuable anti-clone 2.0 upgrades (priority ordered)

1. **CTA mental-model + inflection-family critical-axis veto** (axis 13).
   The single highest-impact upgrade. Forces every new sibling to ship a
   non-clone CTA — which in v1.0 was the cluster's most-monomorphic axis.
2. **Motion gravity + page-choreography axis** (axis 18) AND its
   critical-axis veto. Operationalises the audit's named gap #2.
3. **Imagery register critical-axis veto** (axis 17). Prevents the 7th
   sibling from shipping a 7th composed-restraint Pexels editorial pool.
4. **Hero color-temperature scoring** (axis 3) as a separate cell from
   subject (axis 2). The current matrix conflates them.
5. **Typographic envelope axis** (axis 16) as separate from heading-serif
   + body-sans. Catches the audit's "all 6 share italic-em + cream"
   sameness even when the FONTS differ.
6. **Audience verb register axis** (axis 14). Operationalises the audit's
   "deliberative-only" sameness signal.
7. **Within-family within-cell sub-variant variance rules** (formalised
   here · expanded in `visible-distinctness-thresholds-v2.md`). Closes
   the LF-2 second-occupant gap revealed by Cornice ↔ Causa.
8. **Critical-axis veto independent of total** (binding · §3). Even a
   pair scoring high on aggregate can fail if it shares one critical
   axis — the visible failure mode.
9. **30/27/36 within-/near-/cross-family threshold ladder** (binding ·
   §3). Acknowledges family inheritance is acceptable up to a point.
10. **6-class sameness operational vocabulary** (S1-S6 · §5). Lets the
    orchestrator name the kind of sameness rather than treating "same"
    as binary.

---

## §9 · The 5 highest-risk areas for clone-drift (by descending risk)

1. **CTA inflection family** — every sibling can default to "Apri / Fissa /
   Avvia + abstract noun" inside the corporate-suite contract. The
   inflection is the cluster's CTA register. Without v2.0 enforcement,
   the 7th sibling will produce a 7th "Apri un X." (Highest risk.)
2. **Motion gravity** — without the `motion_profile` dimension, every
   sibling defaults to G2/G3 quiet-editorial. The 7th sibling without
   motion vocabulary unlock will be a 7th identical motion contract.
3. **Imagery register** — Pexels pool exhaustion (Causa A.5b §4 confirmed
   the courtroom-pool is genuinely thin). The 7th composed-restraint
   editorial pool will scrape the bottom.
4. **Audience verb register** — every sibling currently has a deliberative
   verb. Without v2.0 axis 14 scoring, a 7th deliberative-verb sibling
   passes v1.0 trivially but reads identical at the audience-positioning
   axis.
5. **Typographic envelope** — italic-em + cream + serif heading + sans
   body. All 6 share. v2.0 axis 16 catches it; v1.0 fragments it across
   axes that pass individually.

---

## §10 · Maintenance protocol

- Each new sibling at intake (workflow A.1) MUST be scored against v2.0
  on all 18 axes vs every existing sibling. The matrix is appended to
  the planner brief.
- Each new pair scored below threshold MUST be filed for retrofit OR
  the brief MUST be re-spec'd before A.5 build.
- Critical-axis vetoes are non-waivable without a § decision filed at
  the cluster's design-standard level.
- The within-/near-/cross-family threshold ladder applies; only the
  family relationship determines the threshold.
- The 18-axis catalog is monotonically extended at each new cluster
  ship (e.g., when a non-corporate-suite cluster lands, axis 14 + 16 +
  17 gain new value-classes).
- Sameness-type classification (S1-S6) is the orchestrator's diagnostic
  vocabulary; new classes can be added but never removed.

---

## §11 · One-paragraph summary

V1.0 distinctness scored against L1-L9 layout (≥4/9) + 5 skin axes
(≥4/5) + a 12-dim matrix. Both Cornice ↔ Causa AND Pragma ↔ Fiscus
passed v1.0 even though the user senses both pairs as too-related.
V2.0 expands to 18 axes (adds hero color temp · CTA inflection family ·
audience verb register · typographic envelope · imagery register ·
motion gravity + page choreography), scores each 0-3, applies a 36/30/27
threshold ladder for cross/near/within-family pairs, AND requires every
critical axis (voice anchor · CTA mental model · hero subject · motion
gravity · imagery register) to score ≥ 2 vs every other sibling regardless
of total. Cornice ↔ Causa scores 21/54 = 39% with three critical-axis
vetoes failed (CTA inflection · motion · imagery register) — retrofit
required and feasible because Causa is still draft. Pragma ↔ Fiscus
scores 22/54 with two critical-axis vetoes failed — already documented
near-occupant § decision; retrofit cost-benefit is lower at hardening
parity. Pragma ↔ Continua scores 50/54 — well-distinct sanity confirmation.
Six sameness classes (S1 family inheritance · S2 cluster contract · S3
safe reuse · S4 unhealthy family sameness · S5 clone-like critical-axis
fail · S6 overused tropes) provide diagnostic vocabulary. The "do now /
do later / never do" matrix prioritises Causa CTA inflection + EVID-3
+ TIME-3 + NAV-1 retrofits as immediate (paper-spec'd here, code at
Phase X.7d). Phase X.7a (ship a non-corporate-suite cluster) is the
ONLY resolution to S6 overused tropes; v2.0 retrofits resolve S4 and
S5 but cannot resolve S6 inside corporate-suite. The system is NOT
ready for sibling 7 today; it becomes ready after Causa retrofit lands
+ LF-2 family-internal variance rules formalised. See
`corporate-suite-retrofit-priority-plan.md` for the implementation
slice and `visible-distinctness-thresholds-v2.md` for the per-axis
threshold tables.
