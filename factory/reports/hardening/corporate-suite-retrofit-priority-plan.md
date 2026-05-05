# Corporate-suite retrofit priority plan

```yaml
report_type:        hardening · paper-only retrofit plan (companion to
                    anti-clone-2.0-rules.md)
date:               2026-05-05
agent:              orchestrator-side authoring (Phase X.7d)
trigger:            anti-clone-2.0-rules.md identified Cornice ↔ Causa as
                    21/54 pair with 3 critical-axis veto fails AND
                    Pragma ↔ Fiscus as 22/54 with 2 critical-axis veto
                    fails; both pairs require retrofit attention;
                    corporate-suite cluster has 6 siblings now (5 live ·
                    1 draft); the 6th (Causa) is the cleanest retrofit
                    surface
zero_code:          paper only · no template touched · no apps/* edited ·
                    no tier change · no registry change
companion files:
  - factory/reports/hardening/anti-clone-2.0-rules.md (the rule book)
  - design-orchestrator/references/internal-baselines/visible-distinctness-thresholds-v2.md (the threshold reference · per-axis floors)
  - factory/reports/hardening/premium-dynamic-pattern-library.md (motion + dynamic patterns referenced by retrofits)
  - factory/reports/hardening/template-personalization-architecture.md (4-layer model · Layer C toggles unlock retrofits)
  - factory/reports/hardening/premium-dynamic-personalization-audit.md (the audit · §11 recommendations · this plan extends)
  - design-orchestrator/references/internal-baselines/corporate-suite-{distinctness-matrix,reference-pack,layout-family-assignment,live-family-map}.md
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md (LF-2 1st-occupant · binding for Causa retrofit)
  - factory/reports/causa/causa-a6-it-review-lock.md (most recent A.6 · Causa is at PARTIAL · imagery now restored at A.5b)
  - factory/reports/causa/causa-a5b-imagery-recurate.md (A.5b imagery · the most recent state)
status_tag:         RETROFIT-PLAN-V1 · published · binding for next product pass
verdict:            Causa is the only retrofittable sibling without a public-flip
                    cascade · retrofit it FIRST. Pragma + Fiscus retrofits cost
                    more than they save at v2.0 (already shipped under § decision)
                    · accept-as-grandfathered. LF-2 family variance rules need
                    formalisation BEFORE a 7th sibling ships. Causa retrofit
                    closes 4 of 6 v2.0 critical-axis vetoes immediately at low
                    cost; paper-spec'd here, code at Phase X.7d implementation
                    pass.
```

## §0 · The two too-close pairs · severity-ranked

Both pairs failed v2.0 vetoes. Both require attention. The retrofit cost
differs sharply.

| Pair | v2.0 score | Critical-axis vetoes failed | Tier state | Retrofit cost | Action |
|---|---|---|---|---|---|
| **Cornice (LF-2) ↔ Causa (LF-2 · 2nd occupant)** | 21/54 = 39% | CTA mental model + inflection · motion + page choreography · imagery register | Cornice = `published_live` · Causa = `draft` (A.6 partial · imagery just restored at A.5b) | LOW (Causa is still draft · no public-flip cascade impact · retrofits ship as part of Causa's A.6b) | **DO NOW · Phase X.7d.1** |
| **Pragma (LF-1) ↔ Fiscus (LF-3) · documented near-occupant** | 22/54 = 41% | motion + page choreography · imagery register | both `published_live` since Phase 2g3.6f / 2g3.2 | HIGH (would require re-walk of Pragma + Fiscus + frozen-sibling regression on the other 4 + Pragma's Unsplash grandfather still open) | **ACCEPT-AS-GRANDFATHERED · re-evaluate at Phase X.10+ if catalog hits 50 templates** |

The cluster has TWO too-close pairs. The plan retrofits ONE (the cheap
one) and accepts the other as carried-over technical debt with explicit
documentation.

---

## §1 · Causa retrofit · the binding plan

**Goal**: raise Causa ↔ Cornice from 21/54 to ≥27/54 (within-family
threshold) AND clear all 3 critical-axis vetoes (CTA · motion · imagery).

The current state of Causa (post-A.5b imagery restore · A.6 partial):
- Hero geometry: stacked-editorial (LF-2 family · LOCKED)
- Hero subject: Liverpool empty courtroom interior · cool clerestory (axis 2 = 2 · acceptable)
- Section sequence: B (LF-2 family · LOCKED)
- Pillars/narrative: essay-with-anchors + 3 pull-quotes + sticky 4-link side-rail (axis 6 = 0)
- KPI placement: hero-overlay 3-cell `(28 sentenze · 14 voci · 31 anni)` (axis 7 = 1)
- Leadership: single-portrait-feature · masculine senior in chambers reading codex (axis 8 = 1 currently · but the working-at-codex composition is structurally distinct from Cornice's seated-at-drafting-table — RAISE TO 2 by leveraging the A.5b imagery already in place)
- Cases: magazine-grid 3+1 with sentence cases (axis 9 = 1)
- Navbar: split-wordmark-top cream-paper + filled-bottle-green pill (axis 10 = 1)
- Footer: 4-col-with-whistleblowing forensic-firm channel (axis 11 = 1)
- Voice anchor: `evidenza` (axis 12 = 3 ✓)
- CTA: "Apri un parere preliminare" · parere-screening (axis 13 = 1 · CRITICAL VETO FAIL)
- Audience verb: `plead` (axis 14 = 2 ✓)
- Palette: bottle-green + bone + obsidian (axis 15 = 3 ✓)
- Typography envelope: GT Sectra + Manrope · cream · italic-em (axis 16 = 2)
- Imagery register: composed-restraint Pexels editorial · forensic-publication subject pool (axis 17 = 1 · CRITICAL VETO FAIL)
- Motion gravity + page choreography: G2 editorial · same patterns as Cornice (axis 18 = 0 · CRITICAL VETO FAIL)

### The 7 retrofit interventions (in priority order)

#### Retrofit R1 [BLOCKING for v2.0 pass] · CTA inflection shift
**What**: change "Apri un parere preliminare" to a non-Apri inflection.
Recommended: "**Sottometti un parere preliminare**" (transactional ·
evidence-up-front register). Alternative: "**Richiedi un parere
preliminare**" (consultation-request · concrete-action register).

**Why**: Cornice's "Apri un fascicolo progetto" claims the Apri-X
inflection. Two LF-2 siblings sharing the exact inflection family
(Italian-polite-imperative + abstract noun) makes the CTA mental-model
critical-axis veto fail at score 1.

**Score raise**: axis 13 from 1 → 2 (resolves veto · the CTA shape now
reads "submit evidence" rather than "open a folder").

**Locale parity**: must propagate across 5 locales:
- IT: `Sottometti un parere preliminare` (or `Richiedi`)
- EN: `Submit a preliminary opinion` (or `Request`)
- FR: `Soumettez un avis préliminaire` (or `Demandez`)
- ES: `Envía una opinión preliminar` (or `Solicita`)
- AR: `قَدِّم رأيًا أوّليًّا` (or `اطلب`)

**Cost**: 1 string per locale + propagation per Causa's 9 routes (per
A.6 nav pill audit). Low. Single content edit + sync.

**Gate**: A.6b critic verifies (a) the new CTA is verbatim across 5
locales, (b) the verb is non-Apri-cognate, (c) every page's nav pill
matches.

#### Retrofit R2 [BLOCKING for v2.0 pass] · Enable EVID-3 case-citation-pop on magazine cards
**What**: each of the 4 magazine-grid case cards gains an inline-expandable
section showing the actual Cassazione citation snippet ("Cass. SS.UU.
12345/2024 · La consulenza fiscale del Cassazionista..."). Click expands;
inline expansion (NOT modal). 350ms ease-out · max-height transition.

**Why**: Cornice's magazine-grid currently has 4 static cards (per
`cornice-lf2-reference-pack.md §3 D7`). Adding EVID-3 is a 2nd-occupant
within-cell differentiator per the pattern catalog (`premium-dynamic-pattern-
library.md §2.3 EVID-3 · Cluster fit: corporate-suite Causa (forensic-
publication register)`). Cornice doesn't ship EVID-3.

**Score raise**:
- axis 9 (cases) from 1 → 2 (cards now expandable; same shape, different
  pattern layered).
- axis 18 (motion + page choreography) from 0 → 1 (one new pattern enabled).

**Cost**: medium. Pattern wire on 4 cards + reduced-motion equivalent
(static expanded with "[collapse]" link).

**Gate**: A.6b verifier checks (a) inline expansion fires at click +
keyboard, (b) reduced-motion equivalent shows static-with-collapse, (c)
no modal takeover, (d) Cornice's home re-walked at 0/0 regression.

#### Retrofit R3 [BLOCKING for v2.0 pass] · Enable TIME-3 chronological-tick-horizontal in narrative essay
**What**: add a small horizontal timeline strip in the narrative essay's
upper section. 6-8 ticks marking the studio's history (1995 founding ·
2003 Cassazionista · 2008 founding · 2014 first SS.UU. landmark · 2019
ENCA enrollment · 2024 most-recent). Line draws left-to-right on viewport
entry over 1200ms ease-out; ticks animate in 80ms-staggered after the
line crosses them.

**Why**: Cornice's narrative essay has only the sticky 4-link side-rail
+ 3 pull-quotes. Adding TIME-3 is a 2nd-occupant within-narrative
differentiator per pattern catalog (`§2.2 TIME-3 · Cluster fit:
corporate-suite LF-2 second occupant`). Cornice doesn't ship TIME-3.

**Score raise**:
- axis 18 (motion + page choreography) from 1 (after R2) → 2 (resolves
  veto · ≥2 critical-axis floor satisfied).

**Cost**: medium. Single section pattern · ~60 lines of source.

**Gate**: A.6b verifier checks (a) one-time-per-session draw, (b)
reduced-motion equivalent (line + ticks fully drawn at first paint),
(c) tick tooltip behaves on hover · keyboard-accessible.

#### Retrofit R4 [STRONG for v2.0 pass] · Enable NAV-1 sticky-condensed-on-scroll
**What**: Causa's nav shrinks from 76 → 60px after 240px of scroll
(reuses Continua LF-5's already-shipped pattern · adapted for LF-2 cream-
paper). Cornice's nav stays static.

**Why**: per pattern catalog, NAV-1 is allowed for LF-2 second occupant
(within-family differentiator). Cornice ships it as static · Causa ships
it as condensed-on-scroll.

**Score raise**: axis 10 (navbar) from 1 → 2.

**Cost**: low. Pattern is already on disk for LF-5; LF-2 adaptation is
~30 lines of CSS + JS scroll-listener (already shipped by Continua).

**Gate**: A.6b verifier confirms (a) shrink fires at 240px threshold,
(b) reduced-motion equivalent has nav at fixed condensed height, (c)
Cornice's nav still static (frozen-sibling regression).

#### Retrofit R5 [STRONG for v2.0 pass] · KPI placement sub-variant
**What**: Causa's hero-overlay KPI shifts cell composition from the
3-cell tuple `(28 sentenze · 14 voci · 31 anni)` to a year-anchored
form `(dal 1995 · 14 in massimario · 28 sentenze citate)` AND
optionally enables KPI-2 count-up animation. Cornice's tuple
`(novanta fascicoli · 2008 · 38 menzioni)` is period-anchored (count + year + count).

**Why**: same shape (hero-overlay · 3-cell) · different cell semantic.
Combined with KPI-2 count-up that Cornice doesn't ship, the proof shape
diverges meaningfully.

**Score raise**:
- axis 7 (KPI) from 1 → 2.

**Cost**: low. Cell-content edit + KPI-2 pattern wire.

**Gate**: A.6b verifier confirms count-up fires once-per-session ·
reduced-motion equivalent shows static final number.

#### Retrofit R6 [STRONG for v2.0 pass] · Imagery register diversification within composed-restraint
**What**: Causa's hero image (currently 33939830 Liverpool empty courtroom)
acquires a sibling-distinct treatment via a NEW pattern: provenance-
tooltip-image (EVID-5) showing photographer + license inline on hover.
Cornice doesn't ship EVID-5 currently.

**Why**: same imagery REGISTER as Cornice (composed-restraint Pexels
editorial · per audit) but a DIFFERENT pattern layered on top. Axis 17
gets one notch up via the pattern that fires ON the imagery (not a pool
swap which would be S6 cluster-level work).

**Score raise**: axis 17 (imagery register) from 1 → 2 (resolves veto
· register is same but the pattern differentiates).

Note: this retrofit does NOT resolve the cluster-level S6 overused-trope
problem — that requires Phase X.7a (ship a non-corporate-suite cluster).
This is the maximum that can be done within the corporate-suite contract.

**Cost**: low. EVID-5 pattern wire on hero + 4 magazine cards.

**Gate**: A.6b verifier confirms tooltip fires on hover + focus, photographer
credit is correct, reduced-motion equivalent shows static caption below.

#### Retrofit R7 [GUIDELINE · for completeness] · Leadership composition divergence
**What**: ensure Causa's portrait composition reads structurally distinct
from Cornice's. Per A.5b imagery (`9572634 · senior man reading leather-
bound codex at dark stone desk against floor-to-ceiling codex shelves`),
the composition is already different from Cornice's `5915290 · senior
woman white hair reviewing blueprints with pen at home-office desk`.

**Why**: per pattern library MICRO-2 within-cell sub-variant. Already
satisfied by A.5b imagery; this retrofit just records the score raise.

**Score raise**: axis 8 (leadership) from 1 → 2.

**Cost**: zero (already shipped via A.5b).

**Gate**: A.6b verifier confirms portrait composition reads distinct.

### Cumulative score after R1-R7
| Axis | Pre-retrofit | Post-retrofit | Change |
|---|---|---|---|
| 1 hero geometry | 0 | 0 | — |
| 2 hero subject | 2 | 2 | — |
| 3 hero color temp | 2 | 2 | — |
| 4 section sequence | 0 | 0 | — |
| 5 mid-strip | 0 | 0 | — |
| 6 pillars/narrative | 0 | 0 | — |
| 7 KPI | 1 | 2 | +1 (R5) |
| 8 leadership | 1 | 2 | +1 (R7 · already shipped via A.5b) |
| 9 cases | 1 | 2 | +1 (R2) |
| 10 navbar | 1 | 2 | +1 (R4) |
| 11 footer | 1 | 1 | — |
| 12 voice anchor | 3 | 3 | — |
| 13 CTA | 1 | 2 | +1 (R1) |
| 14 audience verb | 2 | 2 | — |
| 15 palette | 3 | 3 | — |
| 16 typography envelope | 2 | 2 | — |
| 17 imagery register | 1 | 2 | +1 (R6) |
| 18 motion + choreography | 0 | 2 | +2 (R2 + R3) |

**Pre-retrofit total: 21/54 = 39%.**
**Post-retrofit total: 29/54 = 54%.**
**Threshold (within-family): 27/54.** ✓ PASSES.

**Critical-axis check post-retrofit**:
- Voice anchor: 3 ✓
- CTA: 2 ✓ (resolved by R1)
- Hero subject: 2 ✓
- Motion + choreography: 2 ✓ (resolved by R2 + R3)
- Imagery register: 2 ✓ (resolved by R6)

All 5 critical-axis vetoes pass. Causa is now ANTI-CLONE 2.0 COMPLIANT.

### Implementation order
The 7 retrofits are sequenced so each ships as a separate commit and
the A.6b walk re-verifies cumulatively:

1. **R1 CTA inflection shift** — content-only · 5 locales · single
   content commit.
2. **R5 KPI sub-variant + KPI-2 count-up** — content + pattern wire.
3. **R4 NAV-1 sticky-condensed** — chrome-level · single CSS+JS commit.
4. **R6 EVID-5 provenance-tooltip** — pattern wire · 5 surfaces (hero
   + 4 magazine cards).
5. **R2 EVID-3 case-citation-pop** — pattern wire on 4 cards.
6. **R3 TIME-3 chronological-tick** — single section pattern.
7. **R7** — already shipped via A.5b imagery · just record in A.6b.

Each commit + browser-walk pass adds to the cumulative score; A.6b at
the end re-runs the full 18-axis matrix vs Cornice and confirms 29/54
+ all 5 critical axes ≥ 2.

### Out-of-scope at this retrofit
- LF-2 family escape (would force LF-{NEW} · expensive · loses LF-2 fit benefits)
- Cornice retrofit (Cornice is `published_live` · its tier flip is intact ·
  retrofitting it would force re-walk + frozen-sibling regression of
  the other 4)
- Pexels imagery pool swap (S6 cluster-level · only resolvable by Phase
  X.7a)
- Voice-anchor noun change for Causa (axis 12 already at 3 · don't touch)

---

## §2 · Pragma ↔ Fiscus · accept-as-grandfathered

Both `published_live` since the editor program era (Phase 2g3.2 / 2g3.6f).
Both walked through workflow C/D and the public-flip cascade. Retrofitting
either requires:
- Pragma's content-module rewrite OR LF-1's nav/footer/CTA shape
  modification.
- Fiscus's content-module rewrite OR LF-3's L7 cases-shape modification
  (would force divergence away from list-row).
- Frozen-sibling regression on the other 4 corporate-suite siblings (Solaria
  · Continua · Cornice · Causa).
- Re-walk of all 5 locales × 5 routes = 25 walks per template re-shipped.
- Pragma's Unsplash grandfather (W001) is open · resolving simultaneously
  would compound risk.

**Cost-benefit at v2.0**: high. Both pairs scored 22/54 (similar to
Cornice ↔ Causa pre-retrofit), but the retrofit cost is 5-10× higher
than Causa's because of the public-flip undoing.

**Acceptance reasoning**:
- Pragma ↔ Fiscus is the documented near-occupant § decision per
  `corporate-suite-distinctness-matrix.md §4` (CS-LAYOUT-12 § decision
  · 2026-05-03).
- Under v2.0, both Pragma and Fiscus carry the same near-occupant
  exception forward — but the ladder is now formalised at 30/54 for
  near-occupant pairs vs the 36/54 cross-family threshold.
- The 22/54 pair fails the 30/54 near-occupant threshold by 8 points,
  with motion + imagery vetoes failing.
- Resolution path for the cluster: Phase X.7a (new cluster) brings new
  motion gravity + new imagery register · the user's "samey" signal
  resolves at the cluster level, not via Pragma + Fiscus retrofit.

**Acceptance documentation**:
- `factory/standards/corporate-suite-design-standard.md` adds a new §
  "Pragma ↔ Fiscus 2.0-grandfathered exception · 2026-05-05" recording
  this decision and the conditions under which it would be re-evaluated
  (catalog ≥ 50 templates · Pragma Unsplash grandfather closed · Phase
  X.10+ batch retrofit pass).

**Action**: NO retrofit. Document the carry-over. Re-evaluate at
Phase X.10+.

---

## §3 · Solaria · Continua · acceptance check

The other 3 cross-pairs that include Solaria + Continua + Cornice. Each
needs to score against v2.0 for completeness.

### Cornice (LF-2) ↔ Solaria (LF-4)
| Axis | Cornice | Solaria | Score |
|---|---|---|---|
| 1 hero geom | stacked-editorial | split-55-45 | **3** |
| 2 hero subject | golden-hour portico | 1:1 conversation | **3** |
| 3 hero color temp | warm golden-hour | minimal-light cool | **3** |
| 4 section sequence | B | C (manifesto-replaces-pillars) | **3** |
| 5 mid-strip | absent | slot-5 method-cadenza | **3** |
| 6 pillars | essay-with-anchors | manifesto-replacement | **3** |
| 7 KPI | hero-overlay | band-at-5 | **3** |
| 8 leadership | single-portrait | absent (single-coach) | **3** |
| 9 cases | magazine-grid | list-row | **3** |
| 10 navbar | split-wordmark cream | sticky-top primary | **3** |
| 11 footer | 4-col-with-whistleblowing | 3-col | **3** |
| 12 voice anchor | `argomento` (one em) | `terapia/consulenza` (two em contrast pair) | **3** |
| 13 CTA | scope-brief Apri | discovery-call Prenota | **2** |
| 14 audience verb | read | declare | **3** |
| 15 palette | graphite + rust | warm-carbon + ocra | **3** |
| 16 typography envelope | Cormorant + Source Sans 3 + cream | Fraunces + Inter + cream | **2** (envelope same · pair distinct) |
| 17 imagery register | composed-restraint exterior architectural | composed-restraint 1:1 conversation | **1** |
| 18 motion + choreography | G2 editorial | G3 institutional | **2** |

**Total: 47/54 = 87%.** Well-distinct cross-family.
**Critical axes**: voice 3 · CTA 2 · subject 3 · motion 2 · imagery 1 ✗.
**Imagery register critical-axis fail.** Same composed-restraint Pexels
editorial register. This is the cluster-level S6 problem · not a
sibling-level retrofit.

**Action**: NO sibling-level retrofit. Cluster-level resolution at
Phase X.7a.

### Solaria (LF-4) ↔ Continua (LF-5)
Quick score summary: 8/9 layout dims different (matrix v1.0). v2.0 adds
~38/54 with same-imagery-register critical-axis fail (S6).
**Action**: same as above. Cluster-level S6.

### Continua (LF-5) ↔ Causa (LF-2)
Quick score summary: 8/9 layout dims different. v2.0 ~42/54 with critical-
axis vetoes mostly clear (voice 3 · subject 3 · CTA 2 · motion 2 ·
imagery 1 ✗).
**Action**: same as above.

### Pattern emerging
Every cross-cluster pair in corporate-suite shares axis 17 (imagery
register) at score 1 because all 6 use composed-restraint Pexels
editorial. The only way to clear this veto across the entire cluster
is to ship a non-corporate-suite cluster (Phase X.7a) which brings a
different register (e.g., gallery-cinematic for portfolio · sprint-
console for digital-studio · maker-in-frame for artisan).

---

## §4 · Should Cornice and Causa both stay LF-2?

Yes. The architectural answer is unchanged: Causa belongs in LF-2 by
correct family-fit (`sixth-sibling-territory-scout.md` recommended LF-2
because portfolio-of-work-led firm fits LF-2's reference profile per
`corporate-suite-live-family-map.md §4`). Migrating Causa to LF-{NEW}
would force:
- Family declaration overhead (~13 standards docs · per
  `template-factory-capability-gap-map.md §1 axis 1`).
- Loss of LF-2 family-fit benefits (the 5-axis distinctness model the
  cluster relies on).
- Reset of the LF-2 second-occupant precedent (which Causa is establishing
  · its successful retrofit teaches the cluster how 2nd-occupants
  differentiate within a shared family).

**What needs to change is NOT Causa's family. What needs to change is
LF-2's family-internal variance rules.** Today LF-2 has only the AC-1
through AC-N rules from `cornice-lf2-reference-pack.md §4`, which are
oriented toward what a 2nd occupant must NOT copy. They lack POSITIVE
RULES: "a 2nd LF-2 occupant MUST adopt at least N of [list of within-cell
sub-variants]."

The proposal: extend LF-2 family rules with a NEW section in
`cornice-lf2-reference-pack.md` (or a fresh `lf2-family-variance-rules.md`)
adding:

### LF-2 family-internal variance rules · paper proposal

1. **AC-V1 [REQUIRED]**: a 2nd LF-2 occupant MUST adopt at least 3 of
   the following within-cell sub-variants:
   - NAV-1 sticky-condensed-on-scroll (Cornice ships static).
   - EVID-3 case-citation-pop on magazine cards (Cornice doesn't ship).
   - TIME-3 chronological-tick-horizontal in narrative (Cornice doesn't ship).
   - QUOTE-4 sticky-stack-rotate replacing static pull-quotes
     (Cornice ships QUOTE-1 only).
   - EDIT-2 pull-quote-em-reveal with longer-delay variant (Cornice
     defaults to standard).
   - KPI-2 count-up animation on hero overlay (Cornice ships KPI-1 static).
   - EVID-5 provenance-tooltip on hero photo (Cornice doesn't ship).

2. **AC-V2 [REQUIRED]**: the 2nd occupant's portrait composition (axis
   8 sub) MUST differ from the 1st occupant's on at least 2 of: subject
   posture (seated vs standing) · subject activity (reading vs writing
   vs reviewing) · room props (drafting tools vs codex vs blueprints
   vs ledgers).

3. **AC-V3 [REQUIRED]**: the 2nd occupant's CTA inflection MUST differ
   from the 1st on the verb-class axis (Apri-X · Sottometti-X · Richiedi-X
   · Avvia-X · Prenota-X · Fissa-X). Same mental-model class with same
   verb-class is forbidden.

4. **AC-V4 [REQUIRED]**: the 2nd occupant's KPI cell semantic class MUST
   differ from the 1st on at least one cell. The cell-tuple shape
   (3-cell · 4-cell) is family-shared; the SEMANTIC CLASS of each cell
   (period-anchored vs year-anchored vs publication-anchored vs achievement-
   anchored) must differ.

5. **AC-V5 [GUIDELINE]**: a 3rd LF-2 occupant MUST clear AC-V1 through
   AC-V4 vs BOTH the 1st AND 2nd occupants. The cumulative within-family
   distinctness ladder.

These rules are paper here. Phase X.7d implementation would commit them
to `corporate-suite-design-standard.md` as `[REQUIRED]` rules.

---

## §5 · Cluster-level diversification surfaces (the "diversify first"
list)

Per anti-clone 2.0 §5 S6 overused tropes · the cluster's 6 most-shared
signals across all siblings:

1. **Imagery register** (composed-restraint Pexels editorial) — 6/6.
2. **Typographic envelope** (italic-em + cream + 100×72 + tabular nums) — 6/6.
3. **Motion gravity** (G2/G3 quiet-editorial · marquee 110s OR none) — 6/6.
4. **CTA inflection family** (Italian-polite-imperative + abstract noun) — 6/6.
5. **Audience verb register** (deliberative) — 6/6.
6. **Section atom vocabulary** (`cs-hero · cs-pillars OR essay · cs-kpi
   · cs-leadership · cs-cases · cs-cta`) — 6/6.

These signals are the cluster's shared identity AND the audit's named
"samey" complaint. They cannot all be fixed inside corporate-suite. The
priority order for cluster-level resolution:

1. **Motion gravity** — closed by Phase X.7b (motion_profile DNA dimension
   + 2 alternate gravities). Lowest cost · highest impact.
2. **Imagery register** — closed by Phase X.7a (ship a new cluster with
   a non-Pexels-editorial register).
3. **CTA inflection family** — closed by Phase X.7a (new cluster brings
   new CTA mental-model class).
4. **Typographic envelope** — closed by Phase X.7a (new cluster declares
   alternate envelope · e.g., display-condensed for digital-studio).
5. **Audience verb register** — closed by Phase X.7a (new cluster's
   audience verb is non-deliberative).
6. **Section atom vocabulary** — extends naturally as new clusters bring
   new atom types (sprint-console · ship-log · gallery-strip · etc.).

Phase X.7a + Phase X.7b together resolve 4 of 6 cluster-level samey
signals. That's why the audit prioritised them. This retrofit plan
prioritises X.7d Causa retrofit because it's the cheapest sibling-level
move that visibly raises the cluster's average distinctness score
TODAY.

---

## §6 · Biggest visible gain for smallest risk · ranked

| # | Action | Visible gain | Risk |
|---|---|---|---|
| 1 | Causa CTA inflection shift (R1) | high · the CTA is the action moment; visible at every page | low · content-only · 5-locale propagation already designed |
| 2 | Causa enable EVID-3 case-citation-pop (R2) | high · 4 cards become interactive · "real product" signal | medium · pattern wire on 4 cards |
| 3 | Causa enable TIME-3 chronological-tick in narrative (R3) | high · narrative section gains a visible distinctive pattern | medium · single section pattern |
| 4 | Causa enable NAV-1 sticky-condensed (R4) | medium · chrome behavior · subtle but cumulative | low · pattern already on disk for LF-5 |
| 5 | LF-2 family variance rules formalisation (paper) | high · prevents the next LF-2 occupant from same trap | zero · paper-only |
| 6 | Pragma ↔ Fiscus retrofit | high · resolves long-standing 2/9 documented gap | high · public-flip cascade undo · 5+ template re-walks |
| 7 | Cornice retrofit | high · Cornice could adopt one new pattern to differentiate from a 3rd LF-2 occupant | high · published_live · regression cascade |
| 8 | Phase X.7a (ship a new cluster) | very high · resolves S6 across the cluster | very high · 8-session pass |
| 9 | Phase X.7b (motion_profile DNA) | very high · resolves cluster motion gap | medium · DNA + 2 profiles + per-cluster compatibility |

**Verdict**: the 4-step Causa retrofit (R1 + R2 + R3 + R4) is the highest
gain × lowest risk move available. The LF-2 family variance rules
formalisation costs nothing and prevents future occurrence.

---

## §7 · Top 5 retrofits to consider first

Ordered by gain ÷ cost.

1. **Causa CTA inflection shift (R1)** — 1 string × 5 locales = 5 changes ·
   resolves CTA critical-axis veto. Highest leverage.
2. **LF-2 family variance rules (paper)** — zero cost · prevents future
   3rd-occupant trap.
3. **Causa NAV-1 sticky-condensed (R4)** — pattern already shipped on
   disk for LF-5; ~30 lines of CSS+JS adaptation. Low risk.
4. **Causa EVID-3 case-citation-pop on magazine cards (R2)** — pattern
   wire on 4 cards; medium effort. Resolves cases-axis floor.
5. **Causa TIME-3 chronological-tick in narrative (R3)** — single section
   pattern; medium effort. Resolves motion + choreography veto fully.

The other 2 Causa retrofits (R5 KPI · R6 EVID-5 provenance · R7 leadership
already shipped) are STRONG-tier rather than BLOCKING. Ship them in
A.6b too if the implementation pass has budget; otherwise hold for a
later A.6c.

---

## §8 · Is the system ready for sibling 7?

**No · not immediately. One more hardening pass + retrofit are needed
first.**

Concretely:
1. **Causa retrofit (R1-R6) MUST land first.** Without it, sibling 7
   would inherit a cluster where 2 of 5 sibling pairs are below v2.0
   threshold AND the LF-2 family variance rules are not formalised.
   A 7th sibling at LF-{any} would be authored against an inconsistent
   reference layer.
2. **LF-2 family variance rules MUST be formalised** (paper here, code
   committed as `[REQUIRED]` rules in the standards stack). Without
   them, a 3rd LF-2 occupant (if proposed for sibling 7) would face the
   same audit gaps as Causa is now correcting — and the cluster has only
   one Causa-grade retrofit budget per sibling.
3. **Phase X.7b (motion_profile DNA) MUST be implemented** OR the 7th
   sibling MUST belong to a non-corporate-suite cluster (Phase X.7a) so
   that the motion-axis sameness is broken at the 7th sibling's intake.
4. **The 7th sibling's intake brief MUST score against the 18-axis v2.0
   model** (not v1.0 4/5 + 4/9). The orchestrator must have the new
   threshold reference live before a 7th intake opens.

If the 7th sibling is a corporate-suite candidate (LF-{NEW} or LF-6
first-occupant) AND the above 4 conditions are satisfied, the system is
ready.

If the 7th sibling is a non-corporate-suite cluster's first hardening
pass (Phase X.7a · the audit's recommendation), the system is ready
TODAY for the cluster's standards-stack authoring · the 7th individual
template within that cluster lands after the standards-stack closes.

The orchestrator's call:
- **If Phase X.7a is the next product pass** (recommended per audit):
  the system is ready today for the standards-stack authoring · cluster
  template lands after.
- **If a 7th corporate-suite sibling is the next pass**: NOT READY today.
  Causa retrofit + LF-2 variance rules + motion_profile DNA must all
  land before the 7th opens.

---

## §9 · Top 10 anti-clone 2.0 upgrades (priority ordered · cluster-level)

Repeated from `anti-clone-2.0-rules.md §8` for at-a-glance reference.

1. CTA mental-model + inflection-family critical-axis veto (axis 13).
2. Motion gravity + page-choreography axis (axis 18) and its veto.
3. Imagery register critical-axis veto (axis 17).
4. Hero color-temperature scoring as separate axis 3 (split from subject).
5. Typographic envelope as separate axis 16 (split from heading-serif +
   body-sans).
6. Audience verb register axis 14.
7. Within-family within-cell sub-variant variance rules (AC-V1..V5
   for LF-2).
8. Critical-axis veto independent of total points.
9. Tiered threshold ladder 30/27/36 for near/within/cross-family.
10. 6-class sameness operational vocabulary (S1-S6).

---

## §10 · One-paragraph summary

The corporate-suite cluster has 2 too-close sibling pairs under anti-clone
2.0: Cornice ↔ Causa (21/54 · 3 critical-axis vetoes failed) and
Pragma ↔ Fiscus (22/54 · 2 critical-axis vetoes failed). Causa is still
draft and cleanly retrofittable; 6 named retrofits (R1 CTA inflection
shift · R2 EVID-3 case-citation-pop · R3 TIME-3 chronological-tick · R4
NAV-1 sticky-condensed · R5 KPI sub-variant + KPI-2 · R6 EVID-5 provenance-
tooltip · R7 leadership composition already shipped via A.5b) raise
Causa ↔ Cornice from 21/54 to 29/54 with all 5 critical-axis vetoes
clear. Pragma ↔ Fiscus is accepted-as-grandfathered with a § decision
documented in the cluster design-standard. Causa stays LF-2 by correct
family fit; what changes is LF-2 family-internal variance rules — five
new rules (AC-V1..AC-V5) formalised here with paper-spec, ready for
implementation. Cluster-level S6 overused-trope signals (imagery register
· typographic envelope · motion gravity · CTA inflection family ·
audience verb register · section atom vocabulary) cannot be fixed inside
corporate-suite; they require Phase X.7a (new cluster) and Phase X.7b
(motion_profile DNA dimension). The system is NOT ready for sibling 7
today; readiness requires Causa retrofit + LF-2 variance rules
formalisation + Phase X.7b implementation. If Phase X.7a is the next
product pass (audit's recommendation), the cluster's standards-stack
authoring is ready today and the cluster's first individual template
lands after the stack closes. The 4-step minimum priority retrofit
(R1 + R4 + R2 + R3) is paper-spec'd here; implementation is Phase
X.7d-implementation, separate brief.
