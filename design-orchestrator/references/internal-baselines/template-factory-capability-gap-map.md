# Template factory · capability-gap map

```yaml
report_type:        internal-baseline · capability-gap diagnosis
date:               2026-05-04
status_tag:         BASELINE-V1 · live · monotonically extended at each new cluster ship
purpose:            structured map of what the factory CAN produce today vs what 50/100/200
                    truly different premium templates would require · written so the
                    orchestrator can read it at every intake and at every hardening pass to
                    triangulate "what is the next cluster missing" against a fixed reference
companion files:
  - factory/reports/hardening/premium-dynamic-personalization-audit.md (the diagnosis)
  - factory/reports/hardening/current-template-factory-drift-map.md (concrete pattern catalog)
  - design-orchestrator/references/internal-baselines/corporate-suite-{distinctness-matrix,reference-pack,layout-family-assignment,live-family-map}.md
  - design-orchestrator/ORCHESTRATOR.md §6 (anti-drift) · §7 (user goal restatement)
  - apps/catalog/template_dna.py (DNA vocabulary registry · the encoded but un-shipped capacity)
audience:           orchestrator (Badr) at every intake · planner-agent at workflow A.1 · style-critic when challenging cluster-contract appeals
```

This file is the orchestrator's reference for "what the factory does NOT yet
do at hardening parity." It is paired with `corporate-suite-live-family-map.md`
(which catalogs what IS shipped at hardening parity) and with `apps/catalog/
template_dna.py` (which encodes what the factory has the *vocabulary* to ship
at some level of fidelity, regardless of hardening parity).

The three states of any factory capability:

```
ENCODED       — the DNA registry knows it · the templates folder may contain a draft
LIVE          — at least one template ships under it on disk (catalog and live render)
HARDENED      — at least one template ships under it AND has cleared the full hardening
                pipeline (cluster standards stack · planner-brief · A.5/6 · workflow C/D ·
                public flip · cluster reference pack)
```

A capability is **gap** if it is `LIVE` (or `ENCODED`) but not `HARDENED`. The
factory's effective ceiling is the set of `HARDENED` capabilities. Today that
set is one cluster: corporate-suite. Everything else is at-best `LIVE` (the
editor program closed there) but unhardened against the corporate-suite-grade
standards stack.

---

## §1 · Capability axes

The factory's output space decomposes along **8 axes**. Each axis has a value
inventory (what is enumerated) and a `HARDENED` subset (what has shipped under
the closed pipeline). The gap is the difference.

### Axis 1 · Layout family (L1–L9 tuple)

**Value inventory** (`corporate-suite-layout-variance-rules.md §1`):
- Hero geometry (L1): `split-55-45 · stacked-editorial · object-overlay · side-rail-photo · type-only`.
- Section sequence (L2): family-declared.
- Mid-strip slot (L3): `absent · slot-2 · slot-4 · slot-5 · slot-6 · slot-2+slot-4`.
- Pillars treatment (L4): `numbered-grid · vertical-stagger · 2x2-with-image · essay-with-anchors · side-quote-with-cards · manifesto-replacement · 4-pillar-matrix · absent`.
- KPI placement (L5): `hero-overlay · band-at-3 · band-at-4 · band-at-5 · band-at-closer · narrative-prose-replacement`.
- Leadership presence (L6): `absent · typographic-grid · photo-grid · single-portrait-feature · pillar-photo`.
- Cases-preview shape (L7): `list-row · magazine-grid · timeline · collage-3+1 · single-feature + sub-list · gallery-strip`.
- Navbar geometry (L8): `sticky-top · side-rail · drawer-only · split-wordmark-top · condensed-minimal-top`.
- Footer structure (L9): `3-col · 4-col-with-whistleblowing · 2-col-stacked · full-bleed-crest · condensed-single-row`.

**Combinatorial space**: 5 × N × 6 × 8 × 6 × 5 × 6 × 5 × 5 ≈ multiple thousands
of layout-family tuples in principle. Constrained by family-coherence rules
the realistic space is closer to 30-50 distinct families.

**HARDENED**: 5 (LF-1, LF-2, LF-3, LF-4, LF-5 · all in corporate-suite).

**LIVE non-hardened**: 0 explicitly · the agency / medical / restaurant /
portfolio / real-estate / e-commerce / lawyer / startup-saas archetypes all
ship under the older editor program but **none has been declared in L1–L9
tuple form**, none has a `<cluster>-layout-variance-rules.md` style rule book.

**ENCODED only**: LF-6 (Rail-Side Chrome · provisional tuple), LF-{NEW} (open).

**Gap**: every non-corporate-suite cluster on disk has a layout but no
declared L1–L9 tuple and no per-cluster variance rules. The hardening
infrastructure is corporate-suite-shaped only. Closing this gap is a
per-cluster authoring cost (~13 docs per cluster · `<cluster>-design-standard.md`
+ `<cluster>-layout-variance-rules.md` + `<cluster>-distinctness-matrix.md` etc.).

### Axis 2 · Tonal grammar (heading + body + voice + chrome polarity)

**Value inventory** (per DNA `TONES` dict + observed clusters):
- `institutional` · `warm-family` · `prestigious` · `serene` · `editorial-chef` ·
  `familiar-warm` · `energetic-bold` · `advisory-sober` · `growth-tech` ·
  `editorial-designer` · `cinematic-authorial` · `editorial-agency` · `digital-sprint`
  · `forensic-notarile` · `advisory-modern` · `market-approachable` ·
  `editorial-concierge`.

**HARDENED**: ~6 sub-flavors of one tonal envelope (corporate-suite cluster) ·
{advisory-sober · editorial-curatorial · institutional-fiscal · professional-warm
· stewardship-longitudinal · evidence-litigation}. All six share the
"Italian-premium-editorial · serif italic-em · cream paper · Pexels editorial
photography · Lei register · ≤3 accent hits · 100×72 padding" envelope.

**LIVE non-hardened**: editorial-chef (fine-dining), familiar-warm (trattoria-
warm), energetic-bold (street-modern), growth-tech (startup-saas-landing),
editorial-designer (editorial-designer-grid), cinematic-authorial (cinematic-
photographer), editorial-agency (vertex creative-agency), digital-sprint (aura
digital-studio), forensic-notarile (lex classic-gold), advisory-modern (juris
modern-transparent), market-approachable (mass-market real-estate), editorial-
concierge (ultra-luxury-cinematic real-estate).

**Gap**: 12+ tonal grammars exist on disk but only 1 envelope has been hardened.
**The "templates feel similar" signal is exactly this gap.** When the factory
ships under hardening, it ships under one tonal envelope; the 12+ alternates
are unhardened.

### Axis 3 · Motion vocabulary

**Value inventory** (this is the most under-developed axis):
- `quiet-editorial` (corporate-suite default · text fade-in + staggered reveals
  + marquee 110s OR none · zero parallax · zero scroll-snap · zero video).
- (no other vocabulary named or shipped today)

**HARDENED**: 1 (`quiet-editorial`).

**LIVE non-hardened**: technically the older editor-program archetypes ship
their own motion code, but it is NOT declared as a vocabulary. agency-digital-
studio has shiplog-console (counter ticker · live-feeling · NOT formalized as
a motion profile). cinematic-photographer has filmstrip-series (horizontal
strip animation · NOT formalized).

**ENCODED only**: nothing — the DNA does not have a `motion_profile` field
yet. This axis is implicit in archetype identity.

**Gap**: the most acute. The factory has effectively one motion vocabulary
across all `HARDENED` output. Adding motion-vocabulary as a first-class DNA
dimension is the single fastest unlock for "feels dynamic" (per audit §4).

**Recommended motion vocabulary set** (3-tier · enumerated · for the next
hardening pass to formalize):
- `quiet-editorial` (current default · do not change).
- `sprint-console` (digital-studio · live-data · ticker-style · sprint-chip
  · scroll-progress).
- `gallery-cinematic` (photography / luxury · scroll-snap · slow fade
  transitions · panoramic horizontal strips).
- (optional 4th) `studio-craft` (agency / artisan · slight tilt-on-hover ·
  hand-drawn flourish · ink-bleed reveal).
- (optional 5th) `concierge-restrained` (luxury concierge · subtler than
  quiet-editorial · zero marquee · single hairline reveal).

### Axis 4 · CTA mental model

**Value inventory** (`CONVERSION_PATTERNS` dict + observed inflections):
- private-call · NDA-ready · partner-gatekept (Pragma)
- scope-brief · fascicolo-bound (Cornice)
- appointment-request · P.IVA + CF (Fiscus)
- discovery-call · 20-30 min · ICF (Solaria)
- mandate-dialogue · custody-onboard (Continua)
- parere-screening · evidence-and-jurisdiction (Causa)
- dossier-request (Vertex)
- session-brief (Aura)
- private-viewing-request (luxury real-estate)
- visit-request (mass-market real-estate)
- demo-request (startup-saas)
- order-now (e-commerce + restaurant-street)
- reservation (restaurant-fine + restaurant-trattoria)
- consultation-booking (medical specialist)
- forensic-consultation (lex classic-gold)
- strategy-call (juris modern-transparent)

**HARDENED**: 6 (the corporate-suite inflections · all "<Italian polite
imperative> + <abstract noun phrase>").

**LIVE non-hardened**: 10+ alternates on disk via the editor program archetypes.

**Gap**: per drift-map §4A, the `HARDENED` set is one inflection family. The
unhardened inflections include the entire range of energetic / transactional /
concrete-action mental models the user signal is missing.

### Axis 5 · Imagery register

**Value inventory** (`IMAGERY_DIRECTIONS` dict + per-cluster pools):
- composed-restraint Pexels editorial (corporate-suite)
- maker-in-frame portraiture (artisan-workshop)
- product-in-context fashion (fashion-editorial)
- fullbleed-EXIF dark photography (cinematic-photographer)
- editorial-quote + selected-work cover (vertex creative-agency)
- product-console + dashboard mock (aura digital-studio)
- map / search-overlay (mass-market real-estate)
- fullbleed-editorial-cover champagne (ultra-luxury-cinematic real-estate)
- ledger-monogram + partner portraits (lex classic-gold)
- advisory bright-page (juris modern-transparent)
- editorial-plate course-indexed (fine-dining)
- chalkboard-day handwritten (trattoria-warm)
- product-cutout tilted (street-modern)
- portrait-led pastel (medical family)
- editorial magazine serif drama (medical specialist)
- spa pricelist (medical wellness)
- split-booking widget (medical clinic)

**HARDENED**: 1 register (composed-restraint Pexels editorial · 5 sub-flavors).

**LIVE non-hardened**: 16+ alternates on disk.

**ENCODED only**: 10+ "open territory" imagery directions named in the
distinctness matrix (notary-chamber · audit-room · trust-deposit-vault · etc.)
that the corporate-suite cluster could enumerate but has not yet exercised.

**Gap**: imagery is the second most acute axis after motion. Pool exhaustion
(per Causa A.5b §4) makes the gap binding rather than aspirational.

### Axis 6 · Content shape (proof tactic + audience verb + register)

**Value inventory** (synthesized from drift-map):
- Numerical proof + deliberative audience verb + Lei register (5/6 corporate-suite).
- Curatorial-publication proof + read verb + Lei (Cornice).
- Public-record proof + plead verb + Lei (Causa).
- Live-data proof + ship verb + product-led register (DNA-named, un-hardened).
- Restoration-bundle proof + restore verb + tradesman register (DNA-encoded
  via artisan-workshop, un-hardened).
- Press-citation proof + read verb + curatorial register (DNA-encoded via
  vertex / cinematic-photographer, un-hardened).
- Reservation proof + visit verb + warm-host register (DNA-encoded via
  restaurant-fine, un-hardened).
- Search-shopping proof + browse verb + market-approachable register (DNA-encoded
  via mass-market real-estate, un-hardened).

**HARDENED**: 3 proof tactics (numerical · curatorial-publication · public-
record) · 1 audience-verb register (deliberative).

**Gap**: the cluster has never shipped a sibling whose content is shaped
around active-verb registers (ship · explore · buy · play · taste · fit · visit).

### Axis 7 · Customer-side customization (editor surface)

**Value inventory** (per audit §5):
- Copy customization (HARDENED via editor program A.6 → A.17b · 19 archetypes
  · 375/375 + 834/834 tests).
- Imagery upload via ProjectAsset (LIVE · A.4 phase · NOT smart-cropped, NOT
  Pexels-integrated, NOT slot-quality-validated).
- Palette swap (NOT LIVE · NOT ENCODED · highest-priority gap).
- Section pick-list per archetype (NOT LIVE · NOT ENCODED).
- Typography pair-set picker (NOT LIVE · NOT ENCODED).
- Motion profile picker (BLOCKED on Axis 3 · NOT LIVE).

**HARDENED**: copy customization only.

**Gap**: every customization affordance beyond copy is missing. This is the
single largest "user-customizable" deficit. Resolution requires editor-side
work (out of scope for the audit's pass · in scope for Phase X.7c).

### Axis 8 · Pipeline shape (build · review · flip)

**Value inventory**:
- Per-sibling sequential walk (corporate-suite default · `intake → A.5 → A.6 →
  C → D → flip`).
- Multi-cluster batch walk (NOT LIVE).
- Parallel-locale build (NOT LIVE · workflow C extends 1 → 5 sequentially).
- Brand-system instantiation from DNA (NOT LIVE · would let a customer "spin
  up a Cornice with custom palette + custom slug" without orchestrator-side
  re-authoring).
- Auto-cohort matrix re-fill (NOT LIVE · the matrix is hand-extended at flip).
- Auto-frozen-sibling regression (LIVE only as DOM probe; the byte-equivalent
  guarantee is asserted manually per flip).

**HARDENED**: per-sibling sequential walk.

**Gap**: the pipeline is N×1 (each sibling one walk). Scaling beyond ~12
templates per cluster requires at least:
- Brand-system-instantiation-from-DNA (the customer becomes a sibling-spawner
  through the editor).
- Per-locale parallel build (workflow C runs 5 locales in parallel from a
  single A.6-locked IT base).
- Multi-cluster cohort flip (one user-handshake covers a batch).

This is Phase X.10+ work · not in immediate scope but the binding for 100+
template scale.

---

## §2 · Capability matrix · cluster × axis × state

The cells answer: what is each cluster's state on each axis?

| Axis ↓ / Cluster → | corporate-suite | agency | medical | restaurant | portfolio | real-estate | ecommerce | lawyer | startup-saas |
|---|---|---|---|---|---|---|---|---|---|
| 1 · Layout family (L1–L9) | **HARDENED** ×5 | LIVE (no L tuple) | LIVE (no L tuple) | LIVE (no L tuple) | LIVE (no L tuple) | LIVE (no L tuple) | LIVE (no L tuple) | LIVE (no L tuple) | LIVE (no L tuple) |
| 2 · Tonal grammar | **HARDENED** ×6 sub-flavors of 1 envelope | LIVE ×2 (editorial-agency · digital-sprint) | LIVE ×3 (institutional · warm-family · prestigious) | LIVE ×3 (editorial-chef · familiar-warm · energetic-bold) | LIVE ×2 (editorial-designer · cinematic-authorial) | LIVE ×2 (market-approachable · editorial-concierge) | LIVE ×2 (artisan · fashion-editorial) | LIVE ×2 (forensic-notarile · advisory-modern) | LIVE ×1 (growth-tech) |
| 3 · Motion vocabulary | **HARDENED** ×1 (quiet-editorial) | LIVE only · not formalized as profile (digital-studio has live-feeling shiplog-console) | LIVE only · not formalized | LIVE only · not formalized | LIVE only · not formalized (cinematic has filmstrip) | LIVE only · not formalized | LIVE only · not formalized | LIVE only · not formalized | LIVE only · not formalized (saas has glow + countdown) |
| 4 · CTA mental model | **HARDENED** ×6 inflections (all in "<imperative> + <abstract noun>" family) | LIVE ×2 (dossier-request · session-brief) | LIVE ×3 (consultation · spa-booking · split-booking) | LIVE ×3 (reservation · order-now · order-now) | LIVE ×2 (dossier · ghost-mono-bracket) | LIVE ×2 (private-viewing · visit-request) | LIVE ×2 (add-to-cart · order-now) | LIVE ×2 (forensic-consultation · strategy-call) | LIVE ×1 (demo-request) |
| 5 · Imagery register | **HARDENED** ×1 register (composed-restraint Pexels editorial · 5 sub-flavors) | LIVE ×2 (editorial-quote-cover · product-console) | LIVE ×4 | LIVE ×3 | LIVE ×2 | LIVE ×2 | LIVE ×2 | LIVE ×2 | LIVE ×1 |
| 6 · Content shape | **HARDENED** ×3 proof tactics + 1 verb register (deliberative) | LIVE — verb-active not formalized | LIVE — verb varies by sub-archetype | LIVE — verb-active (taste · book · order) | LIVE — verb-receptive (read · view) | LIVE — verb-active (visit · search · request) | LIVE — verb-active (buy · add · choose) | LIVE — verb-deliberative | LIVE — verb-active (try · ship · launch) |
| 7 · Customization (editor) | LIVE: copy via editor A.17b. NOT LIVE: palette · imagery-smart-fit · section pick · typography pair · motion profile. | (same · cluster-agnostic) | (same) | (same) | (same) | (same) | (same) | (same) | (same) |
| 8 · Pipeline shape | **HARDENED**: per-sibling sequential walk (recipe). NOT LIVE: cluster-batch · parallel-locale · brand-instantiation-from-DNA. | (same · cluster-agnostic) | (same) | (same) | (same) | (same) | (same) | (same) | (same) |

The matrix is brutally honest: **only column 1 (corporate-suite) has any
HARDENED cell on any of the 8 axes that is cluster-specific.** Columns 2–9 are
all LIVE or LIVE-only-not-formalized.

This is the single most important fact in the gap map: the factory's hardened
output ceiling is one cluster wide.

---

## §3 · Gap-closure cost estimates (for orchestrator planning)

For each axis, the order-of-magnitude cost to add one new HARDENED instance.

| Axis | Cost per added HARDENED instance | Bottleneck step | Typical pass length |
|---|---|---|---|
| 1 · Layout family | ~13 reference docs + 1 hardening pass + 1 sibling build | per-cluster standards-stack authoring (~5 days) | ~10 days first time, ~6 days subsequent (when standards-stack-template lands at Phase X.7d) |
| 2 · Tonal grammar | bundles with axis 1 (a new cluster brings a new tonal grammar by definition) | (subsumed) | (subsumed) |
| 3 · Motion vocabulary | ~1 DNA dimension + ~3 vocabulary profiles + per-LF compatibility verification | profile-vs-LF compatibility matrix authoring | ~3 days (single-pass) |
| 4 · CTA mental model | bundles with axis 1 (a new cluster brings new CTAs) | (subsumed) | (subsumed) |
| 5 · Imagery register | ~1 new pool key + ~6 URL curate + ~1 register-rule-set | curator scout + cross-cluster grep update | ~2 days per pool |
| 6 · Content shape | bundles with axis 1 + 4 (proof tactic + audience verb co-vary with cluster) | (subsumed) | (subsumed) |
| 7 · Customization (editor) | 1 product feature per affordance (palette · imagery · section · type · motion) | editor-side work (apps/editor) — out of scope this pass | ~5-10 days per affordance |
| 8 · Pipeline shape | major refactor work (batch · parallel-locale · brand-instantiation) | architectural work | ~2-4 weeks (Phase X.10+) |

The implication: **adding one hardened cluster simultaneously closes axes 1,
2, 4, 5, 6** (all subsumed by the new cluster's standards stack). It is the
highest-leverage single move. It does NOT close axis 3 (motion) or axis 7
(customization) or axis 8 (pipeline) — those are independent.

The recommended Phase X.7 sequence (per audit):
- X.7a · ship 1 new hardened cluster → closes 1, 2, 4, 5, 6 by 1 instance.
- X.7b · land motion_profile DNA + 2 new profiles → closes axis 3.
- X.7c · editor palette swap → closes axis 7 (palette only).

That is 3 sub-passes producing measurable progress on 7 of 8 axes. **This is
the right shape for the next 6-8 weeks.**

---

## §4 · The blocker model (what prevents hundreds of templates)

Synthesizing the audit + drift map + this map:

### Blocker A · Hardened envelope is one cluster wide
Every recent template is from the corporate-suite cluster. The cluster contract
forbids every dynamic-feel, energetic, transactional, conversion-focused, or
visually-active mechanism that would break sameness. **As long as new templates
ship inside this contract, they will feel like the existing six.**

Resolution: ship a non-corporate-suite cluster. Phase X.7a.

### Blocker B · Motion is uniform by undeclared default
There is no `motion_profile` DNA dimension. Every template inherits an unnamed
"quiet-editorial-restraint-marquee-or-none" default. **Even if the cluster
contract were broken, every template would still feel quiet.**

Resolution: name motion as a DNA dimension. Phase X.7b.

### Blocker C · Customization is single-axis
Customers can change copy. They cannot change palette, imagery (smart-fit),
section composition, typography, or motion. **A premium template that cannot
be made the customer's own reads as a brochure, not a product.**

Resolution: editor-side palette swap first, then progressive customization
expansion. Phase X.7c+.

### Blocker D · Imagery pool exhaustion is real
The Pexels-editorial-composed-restraint register is 5-6 siblings deep into
its tail. The 7th will scrape the bottom (Causa A.5b proved it).

Resolution: a new cluster brings a new register · each new cluster's pool is
fresh. Phase X.7a closes this naturally.

### Blocker E · Standards-stack authoring is not a template
13 reference docs per cluster is a per-cluster authoring cost. **At 4-5
clusters this is 50-65 docs of dedicated standards work that produces no
template directly.**

Resolution: after the second new cluster ships, abstract the standards stack
into a copy-fill template. Phase X.7d.

### Blocker F · Pipeline is sequential per sibling
Each sibling is its own walk. Multilingual is sequential. **At 50 templates
this is 50 walks · ~300 working days minimum.**

Resolution: batch / parallel pipeline mechanisms. Phase X.10+.

The five non-pipeline blockers (A, B, C, D, E) are the immediately addressable
set. Closing all five is the work that lifts the factory from "1 cluster
hardened" to "3-4 clusters hardened with documented and replicable process."
That is the bridge to a 50-template catalog.

---

## §5 · How to read this map at intake

The orchestrator at every new intake answers, in order:

1. **Which cluster is this sibling joining?**
   - If `corporate-suite`: read `corporate-suite-live-family-map.md` and
     `corporate-suite-distinctness-matrix.md`. The sibling MUST inherit the
     cluster contract (axes 2, 3, 4, 6 frozen by the contract). It MUST claim
     a different cell on axes 1 (layout family), 5 (imagery register sub-
     flavor), and the cluster-internal differentiators.
   - If a new cluster (NOT yet shipped under hardening): you are filing Phase
     X.7a · open a `<cluster>-design-standard.md` · author the 13-doc stack
     · this is a hardening pass, not just a sibling pass.
   - If a cluster that already shipped under hardening but has < 5 siblings:
     read that cluster's family map + matrix + reference pack. Same pattern
     as corporate-suite.

2. **On which un-hardened axis is this sibling differentiating?**
   - If the answer is "none — it's a fresh corporate-suite enrollment":
     the audit-named gates are unaddressed · the orchestrator should NOT
     authorise the build until X.7a closes (per audit recommendation).
   - If the answer is "axis 1 + 2 + 4 + 6 simultaneously by cluster choice":
     this is X.7a · the right move · proceed.
   - If the answer is "axis 3 (motion) only": this is X.7b · DNA dimension
     work · independent of cluster.
   - If the answer is "axis 7 (customization) only": this is X.7c · enters
     editor scope · separate brief.

3. **What is the expected cost?**
   Read §3 above and apply the order-of-magnitude estimate. If the proposed
   pass is more than 50% over the estimate, the brief is mis-sized; re-spec.

4. **What does the catalog NOT yet have at hardening parity?**
   Read §2 matrix. Find a column with no `HARDENED` cell. That cluster is
   the next candidate for Phase X.7a.

The map is monotonic: once a cell flips from `LIVE` to `HARDENED`, it does
not flip back. New cells are added when new axes are introduced (e.g., when
motion gets formalized, axis 3's value inventory expands). New columns are
added when new clusters land.

---

## §6 · Maintenance protocol

- **Each new HARDENED instance updates §2.** Single cell flip from `LIVE` to
  `HARDENED` per cluster × axis pair.
- **Each new DNA dimension expands an axis.** Axis 3 (motion) currently has
  one entry; Phase X.7b adds at least two more.
- **Each new editor-side capability flips a row in axis 7.** Phase X.7c flips
  palette from `NOT LIVE` to `LIVE`.
- **§4 blockers stay until explicitly resolved.** The orchestrator does not
  remove a blocker because they "feel less acute"; only because a documented
  pass has closed the resolution.
- **§3 cost estimates are revisited at each pass close.** If a pass came in
  significantly over or under, update the row.

This file is the orchestrator's reference for "is the factory ready to scale."
Today the answer is "ready for one more cluster · then ready for editor-side
customization · then ready for the second cluster after that." It is *not*
ready for hundreds of templates today, and it is honest about why.

---

## §7 · One-paragraph summary

The factory currently produces hardened output along **one cluster (corporate-
suite)**, **one tonal envelope (Italian-premium-editorial)**, **one motion
vocabulary (quiet-editorial)**, **one CTA inflection family (Italian-polite-
imperative + abstract-noun)**, **one imagery register (Pexels-editorial-
composed-restraint)**, **one audience-verb register (deliberative)**, **one
customization affordance (copy)**, and **one pipeline shape (per-sibling
sequential walk)**. The DNA registry encodes 22 archetypes · 19 hero styles ·
21 navbars · 18 footers · 18 cards · 18 buttons · 18 tones · 18 conversion
patterns; the catalog has 19 templates from the editor program shipped under
the older standards floor and 5 corporate-suite siblings shipped under the
new hardening pipeline (with Causa as a 6th in draft). The gap between
**encoded capacity** and **hardened delivery** is wide: 12+ tonal grammars
exist on disk that have never walked the hardening pipeline · ≥10 imagery
registers · ≥10 CTA mental models · ≥6 motion-vocabulary candidates. Closing
the gap is **not** a per-template authoring cost — it is a per-cluster
authoring cost, and a per-axis declaration cost, and a one-time editor-side
customization cost. Phase X.7a closes 5 of 8 axes by shipping one new
cluster. Phase X.7b closes axis 3 by formalizing motion. Phase X.7c closes
the highest-priority cell of axis 7 (palette swap). After that triple the
factory has 3 clusters hardened, 3 motion vocabularies, and 1 customer-
visible customization affordance — the right shape for the next 12-24
templates. Beyond that, batch / parallel pipeline (Phase X.10+) is the
ceiling-lifter for hundreds.
