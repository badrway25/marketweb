# Template-personalization architecture

```yaml
report_type:        hardening · paper-only architecture
date:               2026-05-05
agent:              orchestrator-side authoring (Phase X.7c paper preparation ·
                    follows audit + dynamic-pattern library)
trigger:            audit gap #5 (no editor-side palette swap) + the user's
                    stated goal: "hundreds of customizable templates · all
                    different · modern · dynamic · professional"
zero_code:          paper only · no apps/* edits · no template touches ·
                    no tier change · no registry change
companion files:
  - factory/reports/hardening/premium-dynamic-personalization-audit.md
    (the gap diagnosis · §5 names this work)
  - factory/reports/hardening/premium-dynamic-pattern-library.md
    (motion/dynamic-pattern vocabulary · personalization knobs are
    declared per pattern there · this architecture aggregates them)
  - design-orchestrator/references/internal-baselines/
    premium-dynamic-pattern-catalog.md (planner's at-intake reference ·
    every pattern's `personalization_knobs` field maps to controls here)
  - design-orchestrator/references/internal-baselines/
    dynamic-pattern-usage-rules.md (the motion rule book · USAGE-PERSONAL-*
    rules covered here)
  - design-orchestrator/references/internal-baselines/
    template-factory-capability-gap-map.md (axis 7 customization · this
    architecture instantiates it)
  - design-orchestrator/references/internal-baselines/
    corporate-suite-{distinctness-matrix,reference-pack,layout-family-
    assignment,live-family-map}.md (cluster contract that constrains
    customization)
  - design-orchestrator/ORCHESTRATOR.md §6 (anti-drift) · §7 (user goal)
  - apps/projects/models.py · CustomerProject + ProjectContent +
    ProjectDesignTokens (CURATED_FONTS = 20-Google-font whitelist already
    shipped) + ProjectRevision + ProjectAsset (Foundation v1 already on
    disk · this architecture extends it)
audience:           orchestrator at every project-flip · planner at every
                    intake · editor-team at Phase X.7c implementation pass ·
                    style-critic at workflow A.6 · browser-verifier at
                    workflow C/D
status_tag:         ARCHITECTURE-V1 · 4-LAYER MODEL · 17 CONTROL SURFACES ·
                    paper · ready for X.7c implementation slice
verdict:            The factory already has Foundation v1 personalization
                    bones (CustomerProject · ProjectContent · ProjectDesignTokens
                    with CURATED_FONTS whitelist · ProjectRevision · ProjectAsset).
                    What is missing is (a) Layer-B preset catalogs per cluster ·
                    (b) constraint enforcement on the existing freeform tokens
                    (palette · font) · (c) Layer-C section-level toggles · (d)
                    explicit Layer-D bans. This architecture defines all four.
```

## §0 · Why this architecture exists

The audit (`premium-dynamic-personalization-audit.md §10 gap #5`) named
"no editor-side palette swap" as a top system gap. The capability-gap map
(`template-factory-capability-gap-map.md §1 axis 7`) showed customization
shipped as `LIVE` only on the copy-axis (editor program A.6 → A.17b · 19
archetypes · 375/375 + 834/834). Every other customization affordance
(palette · imagery · structure · typography · motion) is not LIVE.

This architecture is the paper that unblocks Phase X.7c implementation. It
makes one design call binding: **customization is a layered control system,
not a single switch**. The four layers are the architecture.

The original product goal restated (`ORCHESTRATOR.md §7`):

> "Hundreds of customizable templates · all clearly different from each
> other · premium · elegant · modern · professional · dynamic · browser-live
> verified · scalable without quality loss."

"Customizable" + "all clearly different" is a tension. Customization is the
mechanism by which a thousand customers can make a single template "theirs";
"all clearly different" means none of them produce the same output. The
tension is resolved by: **most customization is preset-bound; freeform
customization is forbidden where it would let a customer collapse a template
into a SaaS-grade default.**

---

## §1 · The four-layer control model (binding · architectural)

Every personalization knob in the system belongs to **exactly one** of
these four layers. The layer determines what the user sees, what they can
edit, and what the system enforces.

### Layer A · Locked brand/family constraints
**What it is**: invariants that flow from the cluster contract, the layout
family, the imagery rule book, the legal compliance posture, and the motion
gravity. These are the rules `factory/standards/corporate-suite-design-
standard.md` ships, plus per-cluster equivalents for non-corporate-suite
clusters when those land at hardening parity.

**What the user sees**: nothing. Layer A is invisible to the customer. They
do not discover a setting and find it greyed out — the setting is not in
the UI.

**What the user can edit**: nothing.

**Examples**:
- The cluster identity (corporate-suite · agency-creative-studio · etc.).
- The layout family L1–L9 tuple of the source template (LF-2 inheritor stays
  LF-2; cannot flip cells).
- The voice anchor noun (`argomento` for Cornice · `evidenza` for Causa) —
  the customer can edit copy but the voice-anchor recurrence on hero h1 +
  CTA closer h2 is system-enforced.
- The Pexels-only imagery rule (CS-IMG-SRC-01).
- The whistleblowing column (D.lgs. 24/2023) cannot be removed when the
  cluster + locale combination requires it.
- The `:focus-visible` gold ring (CS-NAV-02).
- The 100×72 padding · max-width 1400px (CS-RHYTHM-01).
- The Latin wordmark + Latin numerics under RTL (CS-NAV-06 + CS-FOOT-03).

**Why locked**: removing any of these breaks the cluster contract or violates
accessibility/legal. The orchestrator does not surface a knob the system
must enforce against.

### Layer B · Curated preset choices
**What it is**: pre-validated alternative configurations. The user picks ONE
from a small enumerated set (typically 3-7 options per control). Each
preset has been verified against the cluster contract by the orchestrator
at preset-authoring time.

**What the user sees**: a picker (radio · select · dropdown · 3-card chooser).

**What the user can edit**: the choice between presets. They cannot author a
new preset; they cannot edit a preset's internals.

**Examples**:
- Palette: pick from "Pragma Blue · Cornice Graphite-Rust · Continua Pine ·
  Causa Bottle-Green · custom-corporate-presets" (5 presets per cluster ·
  each pre-validated for CS-PAL-01 L\* ≤ 40 on cream).
- Heading + body typography pair: pick from 3-5 cluster-validated pairs.
- Hero-photography pool: pick from 2-3 sub-cluster Pexels pools (e.g.,
  "boardroom advisory" · "corporate atrium" · "executive portrait stack").
- Density: pick from `compact · medium · airy · very-airy` (existing DNA
  `DENSITY_PROFILES`).
- Motion intensity: pick from `minimal · standard · expressive`.
- Section variant: pick from "3-card pillars · 4-card pillars" (when both
  variants are pre-built).

**Why preset**: the validation cost has been paid once by the orchestrator;
the customer cannot accidentally produce an out-of-spec configuration. This
is the safe-by-construction class.

### Layer C · Safe user toggles
**What it is**: boolean on/off switches for optional sections, optional
patterns, or optional behaviors. The toggle changes RENDER · it does not
change DATA · it does not change CONTRACT.

**What the user sees**: a switch / checkbox.

**What the user can edit**: on or off.

**Examples**:
- Show/hide the case-study section on home (default: on; off only if
  cluster permits).
- Enable/disable count-up animation on the KPI band (KPI-2 · default per
  motion-gravity).
- Show/hide newsletter subscribe (default: off · cluster-conditional).
- Enable/disable scroll-progress-bar (NAV-3 · default off in G3 · default
  on in G5).
- Show/hide secondary CTA in hero.
- Show/hide the AR locale toggle in nav (default: on if AR locale shipped).

**Why toggle**: each toggle is independent, reversible, and bounded. The
visitor sees A or NOT A — both states are validated at preset-authoring time.

### Layer D · Dangerous/freeform controls that should NOT exist
**What it is**: customization affordances that, if shipped, would allow
the customer to break the cluster contract, the accessibility floor, or
the brand discipline. These are explicitly NOT shipped and listed here as
a permanent ban-list so future passes do not silently introduce them.

**What the user sees**: nothing (Layer D controls are never built).

**Examples**:
- A free hex color picker without contrast validation (would let a customer
  pick `#FFD700` primary against `#FFFFFF` paper · CS-PAL-01 violation
  invisible to them).
- A free font input box with arbitrary Google Font names (would bypass the
  CURATED_FONTS list · introduces fonts that haven't been licensed/validated).
- A drag-and-drop section reorderer (would let a customer move CTA to the
  top · breaks cluster section-rhythm CS-RHYTHM-02).
- Custom CSS injection (would bypass every cluster contract).
- Arbitrary motion-curve picker (would let a customer pick a 50ms slot-machine
  count-up).
- A "remove all D.lgs. 24/2023 references" toggle (legal compliance violation
  for forensic clusters).
- A "delete language locale" button (breaks multilingual contract).
- A "swap layout family" picker (Pragma → Cornice without going through the
  intake pipeline · breaks CS-LAYOUT-11).
- A "make all caps" typography toggle (breaks CS-TYPE-01/02 · uppercase
  headings are banned).
- A "stronger animation" master switch beyond `expressive` (breaks G3/G4
  cluster register).
- An "exit-intent popup" toggle (USAGE-BAN-02 manipulative-SaaS).

**Why banned**: the customer's local optimization (more freedom) is in tension
with the marketplace's global optimization (every template stays premium).
Layer D controls hand the local optimization to the customer at a cost the
customer cannot see. The orchestrator refuses.

### The ratio principle (architectural)
A healthy personalization architecture has approximately:
- 30% Layer A (the cluster contract bites)
- 50% Layer B (the curated presets cover most personality choices)
- 20% Layer C (the toggles cover optional sections + features)
- 0% Layer D (banned by definition)

A system that drifts toward 5% Layer A + 10% Layer B + 30% Layer C + 55%
Layer D (free everything) is the SaaS template-marketplace pattern. It
produces the convergence the user named in the audit.

A system that drifts toward 80% Layer A + 5% Layer B + 0% Layer C + 0%
Layer D is the architecture-firm-bespoke pattern. It produces beautiful
templates that no customer feels ownership of.

The 30/50/20/0 ratio is the target.

---

## §2 · The 17 control surfaces

Each surface is a class of customization. Per surface: the control name,
user-facing meaning, layer assignment, allowed range, hidden constraints,
likely misuse, anti-collapse rules, preview verification. The detailed
catalog lives in `personalization-control-surface-map.md`; this section
gives the architectural view.

### CS-1 · Hero variants
- **Layer**: A (locked at family) for hero geometry · B for sub-variant
  picker.
- **Locked at family**: hero geometry (split-55-45 · stacked-editorial ·
  object-overlay · etc. — declared by L1 of the layout-family tuple).
- **B preset**: hero photography pool selector (3 pre-validated sub-cluster
  pools per cluster); meta-strip composition picker (2 pre-validated cell
  shapes when family allows alternate KPI placement); hero-CTA copy preset.
- **Anti-collapse**: a sibling cannot escape its family by hero-swap — the
  L1 cell is system-enforced.

### CS-2 · Section ordering variants
- **Layer**: A (locked at family) for the L2 section sequence.
- **Locked at family**: the section list and order (per CS-LAYOUT-02).
- **C toggle**: optional sections on/off where the family permits (e.g.,
  case-study section can be hidden on home only when cluster's audience
  doesn't need it; leadership block follows L6 family rules).
- **Anti-collapse**: section reordering is Layer D · banned. The customer
  cannot move CTA to slot-1.

### CS-3 · Case-study display variants
- **Layer**: B preset (within family).
- **Allowed range**: pick from family-allowed shapes — LF-2 ships only
  `magazine-grid-3+1` (CASE-1); LF-1/3/4 ship `list-row-stagger` (CASE-2);
  G1 cluster on case-list page can pick `filterable-grid-with-chips`
  (CASE-6).
- **Anti-collapse**: the family contract narrows the legal set per
  CS-LAYOUT-07.

### CS-4 · Leadership variants
- **Layer**: A (locked) at family-level for L6 presence; B for sub-variant.
- **Locked at family**: leadership presence is the family's choice
  (LF-4 = absent · LF-2 = single-portrait · LF-5 = pillar-photo · LF-1/3
  = typographic-grid).
- **B preset within family**: card count where the family allows (3-card
  vs 4-card on LF-1/3); typographic-only vs photo-grid where both are
  pre-built.
- **C toggle**: per-leader visibility (hide a single leader from the grid).
- **Anti-collapse**: the customer cannot promote LF-2 to a 3-card grid
  (would flip an L cell · breaks family invariant).

### CS-5 · CTA personality variants
- **Layer**: A (locked) for CTA mental model; B for label preset.
- **Locked at cluster**: the CTA's mental-model class (private-call · open-
  dossier · book-appointment · book-discovery-call · open-mandate · open-
  parere · etc.) — see `corporate-suite-distinctness-matrix.md §1.7`.
- **B preset**: CTA label text — pick from 3-5 sibling-curated copies
  (e.g., for a Causa-shaped sibling: "Apri un parere preliminare · Chiedi
  un parere · Richiedi una consulenza"). Each preset is pre-validated for
  CS-CTA-02 + the cluster's voice register.
- **C toggle**: secondary CTA on/off; phone-right on/off (where family
  allows).
- **Anti-collapse**: the customer cannot author a free CTA copy (Layer D)
  because the brand-quality bar would silently degrade ("Buy now" · "Limited
  time"). The 3-5 preset library defines the cluster's CTA register.

### CS-6 · Proof / KPI variants
- **Layer**: B preset for cell composition; C toggle for animation.
- **B preset**: KPI cell-composition picker (3-4 pre-validated tuples per
  sub-cluster · e.g., "Years · Mandates · Capital · Retention" vs "Sentenze
  · Pubblicazioni · Anni · Cassazione" vs "Albo · Iscrizione · Studi · Cause").
- **C toggle**: enable count-up-on-view (KPI-2) · enable comparative-tick
  (KPI-5) · enable range-fill (KPI-4) — per the cluster's `motion_profile`
  allowance.
- **Anti-collapse**: KPI-3 live-counter is gated by ops config (not user-
  toggleable) per `dynamic-pattern-usage-rules.md USAGE-PERSONAL-04`.

### CS-7 · Nav variants
- **Layer**: A (locked at family) for nav geometry; C toggle for behavior.
- **Locked**: navbar geometry (sticky-top · split-wordmark-top · condensed-
  minimal-top) — declared by L8.
- **C toggle**: NAV-2 sticky-hide-on-scroll-down on/off (where motion gravity
  allows); NAV-3 scroll-progress-bar on/off; NAV-4 breadcrumb on/off
  (page-shape-driven).
- **B preset**: nav CTA label (3-5 cluster presets); locale switcher style
  (pill · dropdown · static — within cluster permission).
- **Anti-collapse**: nav background polarity (CS-PAL-06 · CS-NAV-01) is
  locked. NO custom-color nav.

### CS-8 · Footer variants
- **Layer**: A (locked at family) for column count; B for column ordering.
- **Locked at family**: 3-col vs 4-col-with-whistleblowing per CS-LAYOUT-09.
- **B preset within family**: column ordering (brand-first · sitemap-first ·
  contact-first); footer-legal-row layout.
- **C toggle**: newsletter signup on/off (default off · CS-FOOT-04 prefers
  off); social-row on/off; office-hours-row on/off.
- **Anti-collapse**: D.lgs. 24/2023 whistleblowing column cannot be removed
  in clusters/locales where required (Layer A enforcement).

### CS-9 · Color intensity / mood presets
- **Layer**: B preset · core control surface for "make this template ours."
- **B preset**: cluster-validated palettes (5-7 per cluster · each
  pre-validated for CS-PAL-01 L\* ≤ 40 + CS-PAL-05 ≤3 accent hits +
  cluster's polarity-strategy rule per `corporate-suite-distinctness-matrix.md
  §1.3`). Examples for corporate-suite:
  - "Slate-Navy + Emerald" (Pragma family).
  - "Graphite + Pietra-Serena + Rust" (Cornice family).
  - "Warm-Neutral + Blu-Notte + Gold" (Fiscus family).
  - "Warm-Carbon + Ocra + Caramel" (Solaria family).
  - "Pine + Pewter + Brass" (Continua family).
  - "Bottle-Green + Bone + Obsidian" (Causa family).
  - "Custom-A · Custom-B · Custom-C" (3 generic-corporate-grade alternates).
- **D banned**: free hex color picker without contrast validation. Free
  RGB/HSL input. Drag-the-saturation-slider.
- **Anti-collapse**: the preset list is curated; new presets require an
  orchestrator-side authoring pass (so a careless customer can't accidentally
  produce a navy-on-navy template).

### CS-10 · Imagery mood presets
- **Layer**: B preset for pool selection; C upload with validation.
- **B preset**: pick from sub-cluster pools (per
  `apps/catalog/preview_imagery.py` keyed pools — `business-corporate ·
  business-architecture · business-fiscal · business-coaching · business-
  stewardship · business-legale · ...`). Each pool is 6+ Pexels URLs
  pre-curated against the binding triple.
- **C with validation**: customer can upload images via `ProjectAsset`
  (already exists from A.4) with smart-crop, EXIF orientation auto-rotate,
  resolution validation (≥1600 wide for hero), and slot-aware quality
  warnings.
- **D banned**: free Unsplash URL paste, free CDN paste, AI-generated
  image generation (would bypass CS-IMG-SRC-01).
- **Anti-collapse**: the customer's upload replaces a slot's URL but the
  cropping is family-aware (e.g., hero is always 16:9; portrait is square-
  safe). NO arbitrary aspect ratio.

### CS-11 · Typography presets
- **Layer**: B preset · the existing CURATED_FONTS list is the foundation
  but must be cluster-narrowed.
- **B preset**: heading + body pair · pick from 3-5 cluster-validated
  pairs per cluster. The current global CURATED_FONTS = 20 fonts whitelist
  is a SUPERSET; each cluster narrows to 3-5 ALLOWED PAIRS so a corporate-
  suite template cannot produce "Inter heading + Inter body" (banned per
  CS-TYPE-01 + the Inter-double-claim risk per
  `corporate-suite-distinctness-matrix.md §1.4`).
- **D banned**: free font name input. Custom OTF/WOFF upload. Variable-
  axis sliders.
- **Anti-collapse**: each cluster's font-pair preset list is sibling-aware
  — Cornice's pair (Cormorant + Source Sans 3) is removed from the picker
  for any non-LF-2 corporate-suite sibling so two siblings can't accidentally
  reach the same identity.

### CS-12 · Motion presets
- **Layer**: B preset for `motion_profile`; C toggle for per-pattern
  enable/disable.
- **B preset**: pick a `motion_profile` from the cluster's allowed gravity
  set (per `premium-dynamic-pattern-catalog.md §5`). Most clusters have
  a single default; LF-5 corporate-suite second-occupants may pick G2 or
  G4; G5 sprint-console clusters may pick `minimal · standard · expressive`.
- **C toggle**: per-pattern enable/disable for the patterns whose
  `personalization_knobs` field allows it (KPI-2 · NAV-3 · MICRO-2 · etc.).
- **A locked**: `prefers-reduced-motion` always honored regardless of
  user choice (USAGE-PERSONAL-01 binding).
- **Anti-collapse**: the customer cannot pick G5 sprint-console for a
  corporate-suite Pragma sibling — the cluster's allowed gravity set
  excludes it.

### CS-13 · Density presets
- **Layer**: B preset.
- **B preset**: `compact · medium · airy · very-airy` from existing DNA
  `DENSITY_PROFILES`. Cluster-default per the source template's archetype.
  The customer can shift one notch in either direction (e.g., Pragma's
  default `medium` can become `airy` or `compact` — but NOT `very-airy`
  which would break the institutional register).
- **D banned**: free padding-pixel input. Free max-width input. Free
  vertical-rhythm slider.
- **Anti-collapse**: density shift is bounded ±1 notch. The cluster
  contract (CS-RHYTHM-01) is preserved.

### CS-14 · Trust / authority modules
- **Layer**: A (locked) for required modules; C toggle for optional ones.
- **Locked**: D.lgs. 24/2023 whistleblowing (where applicable per cluster);
  voice-anchor h1 + CTA closer recurrence; sectors-ribbon (12-cell
  typology).
- **C toggle**: peer-citation module (QUOTE-6 · default off unless cluster
  ships it); award-ribbon module (default off · cluster-aware); trust-
  marquee on/off (cluster-conditional).
- **Anti-collapse**: removing the sectors-ribbon collapses the cluster's
  audience-positioning per `corporate-suite-reference-pack.md §6`.

### CS-15 · Optional modules on/off
- **Layer**: C toggle.
- **C toggles** (per cluster's pre-built variants):
  - KPI band (default on; LF-2 has it as overlay on hero).
  - Trust marquee (default on for LF-1/3/4; default off for LF-2/5).
  - Newsletter signup (default off · CS-FOOT-04 prefers off).
  - Live ship-log (default off; G5 sprint-console only).
  - Cookie banner (system-managed · always on if locale requires).
- **Anti-collapse**: removing too many sections leaves a half-built page.
  Implement a "minimum 4 sections on home" enforcement at the renderer
  (Layer A architecturally · enforced via empty-state guards).

### CS-16 · Page-level optional sections
- **Layer**: C toggle per page.
- **C toggles**:
  - Case-study list page (default on for clusters that ship cases · off
    if customer chooses, hides the link in nav).
  - Pricing page (default off; on if cluster ships and customer has
    pricing copy authored).
  - About page (default on · always · banned-from-removal).
  - Contact page (default on · always · banned-from-removal).
  - Blog/insights page (default off; on if customer enables and has
    content).
- **Anti-collapse**: about + contact are non-removable. Cases hide-only-
  if-empty (defensive).

### CS-17 · Locale / RTL safe constraints
- **Layer**: A (locked) for the locale list of the source template; C
  for per-locale enable/disable; A for RTL-specific rules.
- **Locked at template**: the locale set the template ships (typically
  IT/EN/FR/ES/AR for corporate-suite — declared by template's
  `locales` row in TEMPLATE_REGISTRY).
- **C toggle per-locale**: customer can disable a locale they don't need
  (e.g., disable AR if their audience is only IT/EN/FR/ES). System
  preserves the locale's translations in revisions; disabling hides from
  nav and search but doesn't delete.
- **A locked under RTL**: Latin wordmark in AR locale (CS-NAV-06); Latin
  numerics on KPI surfaces under RTL (CS-FOOT-03); voice-anchor verbatim-
  in-translation (CS-EXEC-01); Naskh AR h1 swap on LF-2 (`body.cs-lf-lf-2`
  selector-scope cannot be moved).
- **D banned**: customer-supplied translations (would bypass the voice-
  anchor binding · loses verbatim recurrence guarantee). Adding a new
  locale not on the template's shipped list (would bypass the planner's
  multilingual workflow C).
- **Anti-collapse**: removing a locale doesn't remove the translation
  data; reversal is one toggle. Adding a locale outside the shipped set
  is forbidden.

---

## §3 · How customization keeps templates DIFFERENT (anti-collapse architecture)

The audit's load-bearing concern: customization is the path by which all
templates converge to the same default. The architecture's answer is in
three mechanisms.

### Mechanism 1 · Per-cluster preset narrowing
Every Layer-B preset list is **cluster-narrowed**, not global. The 20-font
CURATED_FONTS whitelist on `ProjectDesignTokens` is a foundation; the
architecture extends it so corporate-suite renders see ~5 of those 20,
agency-creative-studio sees ~5 different ones, agency-digital-studio
sees ~5 different ones, and the union covers the 20 without overlap.

The same pattern applies to:
- palette presets (5-7 per cluster · zero cross-cluster reuse).
- imagery pools (one per sub-cluster).
- CTA copy presets (cluster-specific copy register).

This means **a Pragma customer's choices and a Cornice customer's choices
draw from different libraries**. Even if both pick "the most institutional
preset," they pick from different lists.

### Mechanism 2 · Sibling-aware preset narrowing
Within a cluster, the preset library NARROWS as siblings ship. When Cornice
shipped under graphite + pietra-serena + rust, that exact palette becomes
unavailable to a future LF-2 second-occupant. The customer-facing palette
picker for a 2nd LF-2 sibling shows the cluster's palettes MINUS Cornice's
claimed one.

This produces **distinctness via subtraction**: the longer the catalog runs,
the more constrained each new template's customer choices become. The
customer always has variety; that variety is sibling-aware.

Implementation note: this requires the preset registry to reference live
sibling state (`TEMPLATE_REGISTRY.json`), which the orchestrator already
does at intake. The customer-facing picker is computed at project-fork time.

### Mechanism 3 · Layer A invariants per cluster
The cluster contract is the bright line. Every cluster's Layer A list
includes:
- The cluster's voice-anchor recurrence pattern.
- The cluster's polarity-strategy ban list (e.g., "no warm-mahogany hero
  for Continua").
- The cluster's prohibited fonts (e.g., Inter is double-claimed in
  corporate-suite — for a hypothetical 7th sibling, Inter is locked OUT
  of the typography preset list).
- The cluster's prohibited motion gravities (per
  `dynamic-pattern-usage-rules.md §5`).

Layer A is the system's hard "no". The customer never confronts it
because it doesn't appear as a knob.

### The non-collapse property (architectural claim)
**Claim**: with Mechanisms 1 + 2 + 3 in place, two customers who fork the
SAME template produce visually distinct projects iff one of the following
is true:
- They pick different palettes (Layer B independent choice).
- They pick different fonts (Layer B independent choice).
- They pick different imagery (Layer C upload OR Layer B pool variant).
- They author different copy (existing editor · solved at A.6 → A.17b).
- They toggle different optional sections.

If both customers pick all defaults across all layers, they produce the
SAME project — and that's correct: the default IS the template's identity.
What they've cloned is the source template's identity, not each other's
projects.

The collapse-risk is addressed at template-authoring time (Mechanism 2 ·
sibling-aware narrowing): two TEMPLATES cannot ship with the same
default-set even if their orchestrator-authoring agents tried.

---

## §4 · Interaction with layout families

The L1–L9 layout-family system (per `corporate-suite-layout-variance-rules.md`)
gives the customization architecture its skeleton.

| Layout dim (L#) | Customization layer | Customer can edit |
|---|---|---|
| L1 hero geometry | Layer A | NO — locked at template's family |
| L2 section sequence | Layer A · main order | NO ordering · YES Layer C optional toggles per section |
| L3 mid-strip slot | Layer A | NO — family signature |
| L4 pillars treatment | Layer A · sub-variant Layer B if pre-built | choice between 3-card vs 4-card if family allows |
| L5 KPI placement | Layer A | NO |
| L6 leadership presence | Layer A · sub-variant Layer B | choice between typographic vs photo-grid if both pre-built |
| L7 cases-preview shape | Layer A · LF-2 ships fixed shape · Layer B for non-LF-2 |  choice between list-row · gallery-strip · numbered-ledger if cluster supports |
| L8 navbar geometry | Layer A | NO geometry · Layer C for behavior toggles |
| L9 footer structure | Layer A | column count · Layer B for column ordering |

**Architectural rule**: L1–L9 cells are Layer A. Sub-variant-within-cell can
be Layer B if the orchestrator pre-built multiple validated sub-variants.
The customer cannot author a new sub-variant.

This means the layout-family system is the **skeleton** (Layer A) and the
customization architecture is the **clothing** (Layers B + C). The skeleton
determines identity; the clothing determines personality. A customer
cannot reshape the skeleton.

---

## §5 · Interaction with motion / dynamic patterns

Motion is the most user-visible "feels alive" axis, also the most prone
to mis-personalization.

### Single-knob master · `motion_profile` (Layer B)
The customer picks a `motion_profile` from the cluster's allowed gravity
set. For most clusters this is a single value (the cluster's default).
For G5 sprint-console clusters and LF-5 corporate-suite, the user picks
between `minimal · standard · expressive`.

Behind the single knob, the system maps to:
- A bundle of patterns enabled (per cluster's gravity-recommended set in
  `premium-dynamic-pattern-catalog.md §4`).
- A set of duration presets (each pattern's `duration_ms` enum value).
- A set of stagger gaps (each pattern's `stagger_ms` enum value).

The customer does NOT see the bundle. They see the master.

### Per-pattern fine-tune (Layer C)
For patterns whose `personalization_knobs` field marks them as user-
toggleable (per `premium-dynamic-pattern-library.md §2.x`), the customer
sees a per-pattern toggle. Examples:
- KPI-2 count-up: on/off (default per gravity).
- NAV-3 scroll-progress: on/off (default off in G3, on in G5).
- MICRO-2 card-lift: on/off (default per gravity).
- MICRO-6 cursor-vignette: on/off (default off · only available in G6).

### Reduced-motion override (Layer A)
`prefers-reduced-motion: reduce` always wins over the user's choice. The
customer cannot disable this (USAGE-PERSONAL-01 binding).

### What the customer cannot do (Layer D)
- Pick an arbitrary motion-curve (Bezier coordinates · banned).
- Set duration to 50ms or 5000ms (only enum values from the duration
  whitelist).
- Disable `prefers-reduced-motion` honoring (Layer A · can never be
  bypassed).
- Wire a custom backend feed for KPI-3 live-counter (ops config only).
- Select G5 sprint-console motion for a G2 editorial cluster (cluster's
  gravity-allow-list excludes it).

This means motion personalization is a **single-knob master + per-pattern
toggles + automatic accessibility safety net**. The customer experiences
a quality range from minimal to expressive without ever touching a curve
editor or a duration slider.

---

## §6 · Anti-collapse rules (architectural)

These rules enforce that the customer cannot drift the template out of
the cluster contract. They appear as `[BLOCKING]` rules in
`personalization-safety-rules.md`; this section covers the architectural
intent.

### Rule 1 · Preview-verify before save
Every customer-side change MUST live-preview before save. The preview
runs the same validations as the orchestrator's A.6 critique:
- CS-PAL-01 contrast (`get_palette_safety()` per palette token).
- CS-RHYTHM-01 padding/max-width preserved.
- CS-NAV-* navbar polarity preserved.
- CS-EXEC-01 voice-anchor presence preserved.
- USAGE-BAN-01 / USAGE-BAN-02 motion ban (no decorative · no manipulative).

If any check fails, the save is blocked AND the customer sees the reason.
The customer cannot save a broken state.

### Rule 2 · Contract diff visible to customer
When a Layer B/C choice approaches a contract limit (e.g., palette
contrast at the L\* = 40 boundary · or a font choice that triggers a
sibling-collision warning), the editor surfaces the warning text:
- "This palette has been used by Cornice (the cluster's LF-2 occupant).
  Pick a different option to keep your project distinct."
- "This contrast is below the recommended floor for body text. Consider
  adjusting."

The customer can still proceed within Layer B (the orchestrator pre-
validated everything in the Layer B pickers), but they're told when their
choice is on a known-hot edge.

### Rule 3 · Revision snapshot per change
Every customer-side change creates a revision row in `ProjectRevision`
(already shipped from A.1b). The customer can revert any change. The
system never "loses" a state.

### Rule 4 · Source-template snapshot at fork
Per `apps/projects/models.py CustomerProject.source_archetype` (existing).
A project remembers WHICH archetype it forked from. If the source
template is later updated by the orchestrator (palette refresh · new
locale · new motion gravity), the customer's project does NOT auto-
update. The customer chooses when to "rebase" their project against the
new template.

### Rule 5 · Cluster contract as schema constraint
The Layer B preset library is stored as **schema** alongside DNA
(`apps/catalog/template_dna.py`), not in `apps/projects` (which is
project-state). This means cluster-contract enforcement is at orchestrator-
authoring time; customer choices are bound at runtime.

### Rule 6 · Layer D bans are codified (not just style preference)
Each Layer D ban appears as a `[BLOCKING]` line in
`personalization-safety-rules.md §3`. The orchestrator does not silently
add a Layer D feature; new freeform controls require an explicit § decision
at the standards level.

### Rule 7 · Three-cluster minimum before adding Layer-B preset
A new Layer B preset (e.g., a 6th palette for corporate-suite) requires the
orchestrator to verify it does not collide with any existing live sibling
in the cluster. The "sibling-aware narrowing" mechanism is enforced by the
authoring-time check.

---

## §7 · Implementation slice (recommended first pass · Phase X.7c)

The architecture above maps to multiple implementation passes. The
recommended FIRST slice focuses on the audit's named gap #5: editor-side
palette swap.

### Slice 1 · Palette Layer-B preset picker (Phase X.7c.1)
**Scope**:
- Extend `ProjectDesignTokens` model with a `palette_preset_key` field
  (FK or string-key) referencing a cluster-keyed preset registry.
- Author 5-7 palette presets per shipped cluster (corporate-suite first
  · ~6 presets covering Pragma · Cornice · Fiscus · Solaria · Continua
  · Causa · Custom-corporate-A · Custom-corporate-B).
- Each preset carries the 3 tokens + the cluster validation passes.
- Editor UI: a 3-card preset chooser ("Pragma Blue · Cornice Graphite-Rust
  · ...").
- Live preview: the preview pane re-renders with the chosen preset.
- Constraint enforcement: CS-PAL-01 contrast check on every preset (catches
  any preset-authoring mistake at orchestrator-side).

**Out of scope for slice 1**:
- Free hex picker (Layer D · banned).
- Per-cluster preset narrowing for siblings (slice 2 work).
- Palette → font interaction (slice 3).
- Preset import/export (slice 4).

### Slice 2 · Sibling-aware narrowing (Phase X.7c.2)
**Scope**: when the customer is forking a 2nd LF-2 corporate-suite sibling,
the palette picker excludes Cornice's claimed palette. This requires the
preset registry to read live sibling state.

**Effort**: ~3-5 days.

### Slice 3 · Typography preset picker (Phase X.7c.3)
**Scope**: extend ProjectDesignTokens with `font_pair_preset_key`.
Author 3-5 font pairs per cluster. Same shape as slice 1.

**Effort**: ~3 days · the model + UI work mirrors slice 1.

### Slice 4 · Imagery upload + smart-crop (Phase X.7c.4)
**Scope**: extend `ProjectAsset` (existing from A.4) with smart-crop
metadata. Add slot-aware quality validation (warn if upload is <1600
wide on hero slot).

**Effort**: ~5-7 days · imagery is the most complex slice because of
the smart-crop work.

### Slice 5 · Layer-C section toggles (Phase X.7c.5)
**Scope**: add per-section enable/disable toggles to project content.
First targets: case-study, KPI band, trust marquee, newsletter signup.

**Effort**: ~3-5 days.

### Slice 6 · Motion preset picker (Phase X.7c.6 · DEPENDS ON Phase X.7b)
**Scope**: editor exposes the `motion_profile` field added by Phase X.7b
implementation. Customer picks `minimal · standard · expressive`.

**Effort**: ~3 days · the heavy lifting is Phase X.7b's `motion_profile`
DNA dimension; this slice is just the editor wiring.

### Sequencing recommendation
```
Phase X.7c.1 → palette preset picker (highest customer value)
Phase X.7c.3 → typography preset picker (low-effort companion)
Phase X.7b   → motion_profile DNA + alternate gravities (per audit
                §11 · runs in parallel with editor work)
Phase X.7c.4 → imagery upload + smart-crop
Phase X.7c.5 → section toggles
Phase X.7c.6 → motion preset picker (after 7b)
Phase X.7c.2 → sibling-aware narrowing (after 7a ships a 2nd cluster)
```

The first three slices (palette · typography · motion) collectively close
the audit's gap #5 ("no editor-side palette swap" → now palette + typography
+ motion are all editor-personalizable). They are independently shippable.

---

## §8 · The 20 highest-value personalization controls (priority order)

Ordered by customer-felt impact × implementation friction. The list maps
each control to its layer and slice.

| # | Control | Layer | Slice |
|---|---|---|---|
| 1 | Palette preset (5-7 per cluster) | B | X.7c.1 |
| 2 | Heading + body font pair (3-5 per cluster) | B | X.7c.3 |
| 3 | Imagery upload + smart-crop on hero | C with validation | X.7c.4 |
| 4 | Imagery preset pool (sub-cluster) | B | X.7c.4 |
| 5 | Motion intensity (`minimal · standard · expressive`) | B | X.7c.6 |
| 6 | KPI cell composition | B | X.7c.5 |
| 7 | KPI count-up animation (KPI-2) on/off | C | X.7c.5 |
| 8 | Card-lift hover animation (MICRO-2) on/off | C | X.7c.5 |
| 9 | Hero CTA copy preset | B | X.7c.5 |
| 10 | Density (`compact · medium · airy · very-airy`) | B | X.7c.3 |
| 11 | Case-study section on home on/off | C | X.7c.5 |
| 12 | Trust marquee on/off | C | X.7c.5 |
| 13 | Newsletter signup on/off (default off) | C | X.7c.5 |
| 14 | Phone-right in nav on/off (where family allows) | C | X.7c.5 |
| 15 | Locale enable/disable per locale (where shipped) | C | X.7c.5 |
| 16 | Photo provenance tooltip (EVID-5) on/off | C | X.7c.6 |
| 17 | Scroll-progress bar (NAV-3) on/off | C | X.7c.6 |
| 18 | Per-leader visibility (hide single team member) | C | X.7c.5 |
| 19 | Footer column ordering | B | X.7c.5 |
| 20 | Pricing page on/off (where cluster ships) | C | X.7c.5 |

The first 5 are the lever-class controls — they alone shift "this template
is mine" from "this template is the orchestrator's".

---

## §9 · The 10 controls that most increase visible user freedom

Ordered. These are what a customer sees and feels personal control over.

1. Palette preset picker (visible immediately on first preview).
2. Heading + body font pair picker.
3. Imagery upload to the hero slot.
4. Motion intensity master.
5. Density preset.
6. KPI cell composition.
7. CTA copy preset.
8. Hero photography preset pool.
9. Footer column ordering.
10. Section toggles (cases on/off · trust marquee on/off · newsletter on/off).

These ten produce roughly 80% of the felt "I customized my template" signal.
The other ten controls in the top-20 are useful but less viscerally felt.

---

## §10 · The 10 controls that most risk damaging quality

Ordered by harm potential. Each appears in Layer D for a reason.

1. **Free hex color picker** — would allow #FFD700 primary on cream paper
   (CS-PAL-01 violation invisible to customer).
2. **Free font name input** — would let "Comic Sans" + free Google fonts
   bypass CURATED_FONTS list and break CS-TYPE-01.
3. **Drag-and-drop section reorderer** — would move CTA to top, break
   CS-RHYTHM-02, collapse the cluster's section-rhythm contract.
4. **Custom CSS injection** — would bypass every cluster contract
   simultaneously.
5. **Free motion-curve editor** — would allow 50ms slot-machine count-ups
   or 5000ms loading-screen reveals.
6. **Free imagery URL paste (non-Pexels)** — would bypass CS-IMG-SRC-01
   and the cluster's editorial photography register.
7. **Cluster/family change after fork** — would migrate a Pragma project to
   Cornice without going through the planner pipeline (CS-LAYOUT-11
   violation).
8. **Voice-anchor h1 free edit (without recurrence preserved)** — would
   break CS-EXEC-01 binding.
9. **D.lgs. 24/2023 whistleblowing column removal** (where applicable) —
   legal compliance violation.
10. **Locale outside the shipped set** — would bypass workflow-C
    multilingual rollout.

These ten are the architectural ban list. They define the boundary between
"customizable" and "broken." Any future pass that proposes lifting any of
them requires a § decision at the standards level.

---

## §11 · One-paragraph summary

The factory already ships Foundation v1 personalization bones (`CustomerProject ·
ProjectContent · ProjectDesignTokens` with 20-Google-font CURATED_FONTS · 
`ProjectRevision · ProjectAsset` from A.1b → A.4). What's missing is (a) Layer-B
preset catalogs per cluster · (b) constraint enforcement on the existing
freeform palette/font fields · (c) Layer-C section + pattern toggles · (d)
explicit Layer-D bans codified as standards. This architecture defines a
4-layer control model: Layer A locked brand/family invariants (cluster contract
+ L1-L9 layout cells + voice anchor + accessibility) · Layer B curated preset
choices (palette · font · imagery pool · motion gravity · density · CTA copy)
· Layer C safe boolean toggles (per-section + per-pattern enable/disable) ·
Layer D banned freeform controls (free hex · free font · section reorder ·
custom CSS · arbitrary motion curves). 17 control surfaces are mapped across
the 4 layers. Anti-collapse is preserved by per-cluster preset narrowing,
sibling-aware preset subtraction (each new live sibling removes its claimed
identity from the future-customer picker), and contract enforcement at
preview time. Phase X.7c implementation runs in 6 slices ordered by
customer-felt impact: palette preset (X.7c.1) · typography preset (X.7c.3)
· imagery upload + smart-crop (X.7c.4) · section toggles (X.7c.5) · motion
preset (X.7c.6) · sibling-aware narrowing (X.7c.2 · after a 2nd cluster
ships at X.7a). The 30/50/20/0 layer ratio is the architectural target;
drift toward Layer D is the failure mode the orchestrator refuses.
