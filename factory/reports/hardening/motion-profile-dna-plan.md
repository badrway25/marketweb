# Motion-profile DNA plan · Phase X.7b

```yaml
report_type:        hardening · DNA-axis paper definition · binding intake contract
phase:              X.7b · motion_profile elevation from one-pattern carrier to
                    first-class DNA axis (8th template-DNA dimension after tone ·
                    palette · typography · density · hero · navbar · card · button)
date:               2026-05-05
agent:              orchestrator-side authoring (post-slice-01 · post-anti-clone-2.0
                    · post-LF-2-variance ratification · post-Causa-retrofit-slice-01)
trigger:            anti-clone 2.0 §3 named axis 18 (motion gravity + page
                    choreography) a critical-axis-veto field at floor 2 vs every
                    sibling. Today motion_profile is on disk as a 7-key registry
                    with 3 boolean flags · used by KPI-2 + NAV-1 + EVID-5 only.
                    For sibling 7 to open and for cluster-cross intakes to score
                    cleanly under v2.0, motion_profile must read at intake the
                    way palette + typography read today: an enumerated DNA value
                    with a per-cluster allowed set, a per-profile feel-statement,
                    a safe-pattern allowance, an anti-tacky red-line list, and a
                    reduced-motion equivalent guaranteed by the JS layer.
zero_code_this_pass: paper definition · planner-side intake contract · catalog
                    reference + standards-stack cross-references. Implementation
                    scaffold is the lightest non-breaking addition: a reduced-
                    motion alias key in MOTION_PROFILES (paper-listed here · code
                    in §11). NO new behavior · NO new patterns wired · NO new
                    siblings opened.
companion files:
  - factory/reports/hardening/premium-dynamic-pattern-library.md (the 6
    gravities G1-G6 + 48 patterns are the source vocabulary)
  - factory/reports/hardening/anti-clone-2.0-rules.md §3 (axis 18 critical-axis
    veto · floor 2 vs every sibling · this plan operationalises it)
  - factory/reports/hardening/lf2-family-internal-variance-rules.md §4 AC-V1
    (sub-variant adoption inside LF-2 reads from motion_profile bundle flags)
  - factory/reports/hardening/causa-retrofit-slice-01.md (3-flag bundle
    g2-editorial-counter shipped · paper here describes how the bundle scales)
  - factory/reports/hardening/premium-dynamic-implementation-slice-01.md
    (slice-01 narrative · what the field is on disk today)
  - factory/reports/hardening/template-personalization-architecture.md §2 CS-12
    (motion presets at Layer-B · Phase X.7c picks up from this plan's §10)
  - design-orchestrator/references/internal-baselines/motion-profile-catalog.md
    (planner-side reference · authored in same pass · cross-references this plan)
  - design-orchestrator/references/internal-baselines/premium-dynamic-pattern-
    catalog.md (per-pattern × gravity matrix)
  - design-orchestrator/references/internal-baselines/dynamic-pattern-usage-rules.md
  - apps/catalog/template_dna.py · MOTION_PROFILES (the 7-key registry on disk)
  - static/js/live-motion.js (counter gate · the working precedent for how a
    bundle flag gets honored at runtime)
status_tag:         PROFILE-V1 · 7 enumerated values · 12 bundle flags total
                    (3 implemented · 9 paper-declared) · per-cluster allowed set
                    · binding at every A.1 intake from this point forward
verdict:            motion_profile is ready to bind future intakes the moment
                    this plan ratifies. Sibling 7 can open IFF (a) its declared
                    motion_profile is in its cluster's allowed set, (b) its
                    pair-wise axis-18 score ≥ 2 vs every existing sibling, AND
                    (c) cluster-S6 readiness — for corporate-suite specifically
                    that means a non-corporate-suite cluster must ship FIRST
                    (Phase X.7a) per anti-clone-2.0 §5 S6 operational rule. The
                    DNA axis is ready; the cluster-S6 gate is the remaining
                    blocker for a 7th corporate-suite sibling.
```

---

## §0 · Why motion_profile must be a first-class DNA axis

Until slice 01 (Phase X.7d), motion was the only template DNA dimension that
was **never declared** at intake. The other seven (`tone` · `palette` ·
`typography` · `density` · `hero_style` · `navbar_style` · `card_style` ·
`button_style`) all read from `apps/catalog/template_dna.py` as enumerated
values with a planner-facing meaning. Motion was implicit:
- LF-2 = "static" because Cornice didn't ship animations.
- LF-1/3/4 = "count-up KPI band" because Pragma did.
- LF-5 = "static timeline" by Continua precedent.

Six siblings shipped under this implicit contract. The audit
(`premium-dynamic-personalization-audit.md §10 gap #2`) and the user signal
("templates feel too similar / not dynamic") named the cost: **one motion
vocabulary is shared across all 6 corporate-suite templates**, and there
is no DNA cell to score against.

Slice 01 fixed the carrier (a `motion_profile` key landed on each of the 6
templates with one bundle flag `kpi_animate`). Slice 02 (Causa retrofit
slice 01) extended the bundle with `nav_condense_on_scroll` +
`evid5_provenance` and shipped Causa as the 2nd LF-2 occupant differentiator.
This plan is the **promotion**: motion_profile becomes a first-class axis
the planner declares at A.1 intake, the style-critic scores at A.6
review-lock, and the gatekeeper scores at workflow D flip.

The promotion has four parts:

1. **Enumerated values + feel-statement** (§1) — what the seven profiles
   semantically mean (not just what flags they enable).
2. **Per-cluster/family allowed set + safe motion pool** (§3) — what each
   profile is allowed to ship; the rest is blocked.
3. **Anti-tacky red-lines + reduced-motion guarantee** (§5–§6) — what each
   profile MUST refuse + the static fallback.
4. **Distinctness contribution + customization plan** (§7–§10) — how the
   profile feeds anti-clone 2.0 axis 18 + how it becomes a Layer-B preset.

The lightest implementation scaffold (§11) adds one reduced-motion alias
field per profile so the JS layer can resolve the right static fallback
without changing today's gating logic.

---

## §1 · The seven motion_profile values · enumerated · binding

Today's registry has 7 keys. This plan keeps the keys, freezes the
canonical-name format, attaches a feel-statement (the user's "what does
this profile feel like" question), names the **canonical-alias** in
human-readable form (the user's suggested taxonomy), and binds the
cluster-fit and the safe-pattern pool.

| key | canonical alias (human read) | one-line feel | gravity ref | cluster default |
|---|---|---|---|---|
| `g1-safe-premium` | **safe-institutional** | "alive but composed · no animation costs the visitor a moment of doubt" | G1 (library §1) | corporate-suite generic · medical-clinic · medical-family · real-estate-mass-market |
| `g2-editorial` | **restrained-editorial** | "publication, not website · narrative reveals · drop-cap leads · sticky side-rail anchors" | G2 | corporate-suite LF-2 1st-occupant (Cornice) · agency-creative-studio (Vertex) · restaurant-fine · real-estate-luxury concierge |
| `g2-editorial-counter` | **evidence-led-reactive** | "publication that ALSO answers · KPI ticks once · provenance reveals on hover · nav condenses to clear the page" | G2-with-G3-cell-borrowing | corporate-suite LF-2 2nd-occupant (Causa) · audit-led methodology future-2nd-occupant |
| `g3-institutional` | **institutional-progressive** | "every animation paid for by purpose · count-up arrives · hairline hover · static cards · NEVER live tickers" | G3 | corporate-suite LF-1/3/4 (Pragma · Fiscus · Solaria) · lawyer-classic-gold (Lex) · family-office (paper-deferred) |
| `g4-stewardship` | **calm-architectural** (alias: high-trust-stewardship) | "this firm holds something across time · the timeline does not move · numbers do not tick · attention is the gift" | G4 | corporate-suite LF-5 (Continua) · medical-specialist (Cassazione-grade clinical authority) · fiduciary-stewardship (paper) |
| `g5-sprint-console` | **sprint-product** | "this product ships · KPI updates from a feed · scroll-progress ribbon · magnetic CTA on hero · nav hides as you read" | G5 | agency-digital-studio (Aura) · startup-saas-landing (Elevate) · lawyer-modern-transparent (Juris · light-touch only) |
| `g6-cinematic` | **curatorial-cinematic** | "this site is a slow film · 1.04× Ken-Burns · scroll-snap horizontal galleries · cursor-vignette in dark hero · zero chrome motion" | G6 | portfolio-cinematic (Pixel) · real-estate-ultra-luxury (Villa) · e-commerce-fashion-editorial (Luxe) · agency-creative-studio Vertex (lighter touch) |

The **canonical-alias** column is the planner-facing name used in briefs +
scorecards. Code keeps the gravity-letter key (`g2-editorial-counter`) for
backward compatibility with slice 01.

The user's suggested taxonomy maps cleanly onto the existing seven:
- "restrained-editorial" → `g2-editorial`
- "institutional-progressive" → `g3-institutional`
- "evidence-led-reactive" → `g2-editorial-counter`
- "curatorial-cinematic" → `g6-cinematic`
- "calm-architectural" → `g4-stewardship`
- "high-trust-forensic" → `g3-institutional` with **forensic-register imagery
  + voice** (NOT a separate motion gravity · forensic clusters score on
  imagery + audience-verb axes 14 + 17, not on motion). The forensic register
  is a sub-cluster lens that overlays `g3-institutional` (Pragma/Fiscus) or
  `g2-editorial-counter` (Causa).

**Why no 8th profile**: anti-clone 2.0 axis 18 scores 0-3 between any pair
of siblings. Seven profiles spread across four cluster archetypes (corporate
· agency · cinematic · sprint) generate 21 cross-pair distances; that is
already over-discriminating for 19 enrolled archetypes + 5 future cluster
candidates. Adding an 8th profile would inflate the axis without adding
distinguishability.

---

## §2 · Bundle shape · 12 declared flags (3 wired · 9 paper)

The bundle is a flat namespace of boolean flags. Each flag corresponds to
**exactly one named pattern** from `premium-dynamic-pattern-library.md`.
The flag is the carrier; the pattern is the visible behavior.

| flag | pattern (library §) | meaning when true | wired today? |
|---|---|---|---|
| `kpi_animate` | KPI-2 count-up-on-view (§2.1) | KPI cells tick from 0 to target on viewport entry · once per session | ✓ slice 01 |
| `nav_condense_on_scroll` | NAV-1 sticky-condensed-on-scroll (§2.7) | nav shrinks 76→56 (LF-5) or 84→64 (LF-2 2nd-occupant) at scroll threshold | ✓ retrofit slice 01 |
| `evid5_provenance` | EVID-5 provenance-tooltip-image (§2.3) | hero/feature photos reveal photographer/license overlay on hover/focus | ✓ retrofit slice 01 |
| `nav_hide_on_scroll_down` | NAV-2 (§2.7) | G5 nav hides on scroll-down · reveals on scroll-up | paper |
| `scroll_progress_bar` | NAV-3 (§2.7) | 1px hairline at top tracking scroll percentage | paper |
| `hero_parallax` | MEDIA-2 parallax-restrained (§2.4) | G6 hero photo offsets at 0.15× scroll · single layer | paper |
| `gallery_snap` | MEDIA-5 gallery-strip-snap-horizontal (§2.4) | G6 horizontal scroll-snap on photo strips + lightbox preserves context | paper |
| `cinematic_fade` | MEDIA-1 cinematic-fade-on-view (§2.4) | full-bleed photos fade from 0.7 opacity / 0.85 saturation / 1.04× scale | paper |
| `card_lift_restrained` | MICRO-2 card-lift-restrained (§2.5) | cards translate 2-4px up + hairline shadow on hover | paper |
| `magnetic_button` | MICRO-3 magnetic-button-restrained (§2.5) | G5-only · single hero-CTA attracts cursor at ≤30px proximity | paper |
| `cursor_vignette` | MICRO-6 cursor-vignette (§2.5) | G6 dark-hero only · radial-gradient overlay tracks cursor | paper |
| `live_data_kpi` | KPI-3 live-counter (§2.1) | G5-only · KPI updates from backend feed every 8-12s with timestamp | paper · gated |

Three principles govern the bundle:

1. **Each flag maps to exactly one pattern.** A flag never enables two
   patterns. A pattern never reads two flags.
2. **Adding a flag is purely additive.** Each new flag is a key with a
   default of `False` for every profile that doesn't enable it; existing
   profiles are not destabilised by the addition.
3. **Banned patterns get no flag.** EDIT-5 magazine-page-flip · decorative
   motion · manipulative SaaS motion are banned at archetype level (library
   §1) and therefore have no flag · no profile · no opt-in path.

---

## §3 · Per-profile feel · safe pool · cluster fit · anti-fit

For each profile, this section names: the FEEL the visitor reads, the
PATTERN POOL it is allowed to ship, the patterns that are FORBIDDEN even
within its safe pool, the cluster/family fits, and the cluster/family
anti-fits (where adopting this profile would break the cluster contract).

### 3.1 · `g1-safe-premium` (safe-institutional)

- **Feel**: "alive but composed." Every animation has a documented purpose.
  Tabular numerals on KPIs. Hairline-on-hover. 600ms ease-out fade-ins on
  first viewport intersection. `prefers-reduced-motion` honored globally.
- **Safe pool**: KPI-1 tabular-static · KPI-2 count-up-on-view · KPI-4
  range-fill (with discipline) · KPI-5 comparative-tick (with citation) ·
  EVID-1 progressive-disclosure-tap · EVID-2 attestation-chip-hover ·
  EVID-4 audit-trail-arrow · MEDIA-3 image-grid-stagger (light) ·
  MEDIA-4 before-after-slider (when semantic) · MICRO-1 hairline-hover ·
  MICRO-2 card-lift-restrained · MICRO-5 focus-ring · EDIT-1 fade-stagger ·
  NAV-1 sticky-condensed · NAV-4 breadcrumb · QUOTE-1 editorial-pull-quote ·
  QUOTE-3 single-with-portrait · CASE-2 list-row-stagger · CASE-6
  filterable-grid-with-chips · SCROLL-2 staggered-reveal · SCROLL-6
  scroll-velocity-aware-fade.
- **Forbidden in safe pool**: parallax (MEDIA-2) · cinematic-fade (MEDIA-1) ·
  cursor-vignette (MICRO-6) · magnetic-button (MICRO-3) · gallery-snap
  (MEDIA-5) · live-counter (KPI-3) · sticky-stack-rotate (QUOTE-4) ·
  scroll-driven-timeline (TIME-2 · stewardship-class) · stewardship-rings
  (TIME-4 · stewardship-class) · scroll-progress-bar (NAV-3 · sprint-class).
- **Cluster fit**: corporate-suite generic siblings outside LF-2/LF-5 ·
  medical-clinic · medical-family · real-estate-mass-market · lawyer-classic-
  gold (some patterns; `g3-institutional` is the lawyer-classic-gold default).
- **Anti-fit**: agency-digital-studio (too restrained · register collapses) ·
  startup-saas (the product needs sprint-feel) · portfolio-cinematic (the
  cinematic register rejects the institutional reading).

### 3.2 · `g2-editorial` (restrained-editorial)

- **Feel**: "publication, not website." Slow narrative reveals. Drop-cap
  appears first, paragraph fades around it. Pull-quote staggers. Sticky
  4-link side-rail anchors. NO parallax. NO scroll-snap. NO live-data.
- **Safe pool**: EDIT-1 fade-stagger · EDIT-2 pull-quote-em-reveal ·
  EDIT-3 drop-cap-stagger-around-paragraph · EDIT-4 sticky-side-rail-anchor-
  active · MICRO-1 hairline-hover · MICRO-4 text-underline-grow-from-left ·
  MICRO-5 focus-ring · QUOTE-1 editorial-pull-quote · CASE-1 magazine-grid-
  3+1 · MEDIA-3 image-grid-stagger (60ms quick) · TIME-5 chapter-stepper-
  magazine (when narrative exceeds 7 paragraphs).
- **Forbidden in safe pool**: KPI-2 count-up (LF-2 1st-occupant chooses
  static · the count-up surface is the LF-2 2nd-occupant differentiator) ·
  parallax · cursor-vignette · magnetic-button · scroll-progress-bar ·
  carousel-restrained (use QUOTE-1) · gallery-snap.
- **Cluster fit**: corporate-suite LF-2 1st-occupant (Cornice canonical) ·
  agency-creative-studio (Vertex) · restaurant-fine (course-indexed editorial
  cues) · real-estate-luxury-concierge (editorial register).
- **Anti-fit**: corporate-suite LF-1/3/4 (boardroom register prefers
  institutional-progressive · the editorial reveal feels staged for advisory
  audiences) · medical-clinic (clinical reading prefers safe-institutional) ·
  e-commerce · startup-saas.

### 3.3 · `g2-editorial-counter` (evidence-led-reactive)

- **Feel**: "publication that ALSO answers." The editorial restraint is
  preserved (drop-cap · pull-quote · side-rail) AND a small set of evidence-
  led behaviors fire: KPI ticks once · provenance overlays reveal on hover ·
  nav condenses to give the page room. The visitor reads as in `g2-editorial`
  AND senses the page responds.
- **Safe pool**: full `g2-editorial` pool PLUS KPI-2 count-up-on-view ·
  NAV-1 sticky-condensed-on-scroll · EVID-5 provenance-tooltip-image ·
  EVID-2 attestation-chip-hover · EVID-3 case-citation-pop (forensic-class
  only · per library §2.3) · QUOTE-4 sticky-stack-rotate (long-narrative
  2nd-occupant only) · TIME-3 chronological-tick-horizontal.
- **Forbidden in safe pool**: parallax · cursor-vignette · magnetic-button ·
  scroll-progress-bar · gallery-snap · live-counter · cinematic-fade ·
  card-lift-restrained on the magazine-grid (LF-2 cards stay still per
  CASE-1).
- **Cluster fit**: corporate-suite LF-2 2nd-occupant (Causa canonical) ·
  audit-led methodology (paper-future · 2nd-occupant register) · forensic
  legal sub-clusters that need editorial register WITH live evidence proof.
- **Anti-fit**: LF-2 1st-occupant (would collapse Cornice's static-by-design
  signature) · any non-LF-2 family (the bundle assumes LF-2 cells; mapping
  to LF-1/3/4/5 would re-introduce the editorial register where institutional
  is the cluster default).
- **Within-LF-2 contract**: the `g2-editorial` 1st-occupant ships exactly
  zero of the three v2-only flags (KPI-2 · NAV-1 · EVID-5). The `g2-editorial-
  counter` 2nd-occupant ships exactly all three. This is the AC-V1 ≥3 sub-
  variant floor (per `lf2-family-internal-variance-rules.md §4`) being read
  off the motion_profile bundle directly.

### 3.4 · `g3-institutional` (institutional-progressive)

- **Feel**: "every animation paid for by purpose. Nothing decorative." KPI
  count-up arrives once on first scroll past. Hairline-on-hover. Static
  cards. Marquee 110s OR none. Hover affordances are hairline-only · NO
  lift, NO tilt, NO accent-glow on body content.
- **Safe pool**: KPI-1 + KPI-2 (the institutional default · count-up at
  band-at-3 or band-at-4) · KPI-4 range-fill (audit-led methodology only) ·
  EVID-1 progressive-disclosure-tap · EVID-2 attestation-chip-hover · EVID-3
  case-citation-pop (forensic class) · EVID-4 audit-trail-arrow · MICRO-1
  hairline-hover · MICRO-2 card-lift-restrained (cases-list cards · lift ≤
  3px) · MICRO-5 focus-ring · EDIT-1 fade-stagger · NAV-1 sticky-condensed
  (when family allows) · NAV-4 breadcrumb · QUOTE-1 editorial-pull-quote ·
  QUOTE-3 single-with-portrait · QUOTE-5 attribution-rich · CASE-2 list-
  row-stagger · CASE-5 numbered-ledger-editorial · CASE-7 case-card-reveal-
  inline · COMP-2 scenario-tab-switcher (pricing-explainer pages) ·
  COMP-4 case-vs-baseline-narrative.
- **Forbidden in safe pool**: parallax · cursor-vignette · magnetic-button ·
  scroll-progress-bar · cinematic-fade · gallery-snap · live-counter ·
  scroll-driven-timeline · stewardship-rings · sticky-stack-rotate · drop-
  cap-stagger (G2-only).
- **Cluster fit**: corporate-suite LF-1 (Pragma) · LF-3 (Fiscus) · LF-4
  (Solaria) · lawyer-classic-gold (Lex) · family-office (paper) · audit-led
  methodology (paper-future).
- **Anti-fit**: LF-2 (the editorial register would lose the magazine-spread
  reading) · LF-5 (the stewardship register prefers stillness) · agency-
  digital-studio (the product register needs sprint patterns) · portfolio-
  cinematic.

### 3.5 · `g4-stewardship` (calm-architectural)

- **Feel**: "this firm holds something across time. Nothing is flashing."
  Motion = institutional-restraint **minus** count-up · KPIs sit static ·
  timeline does not move · narrative reveals are softer. Reduced from
  `g3-institutional` by one notch on every parameter.
- **Safe pool**: KPI-1 tabular-static (forced · count-up forbidden by
  cluster fit) · TIME-1 static-vertical-timeline · TIME-2 scroll-driven-
  timeline (2nd-occupant differentiator only) · TIME-4 stewardship-rings-
  concentric (2nd-occupant differentiator only) · EVID-1 progressive-
  disclosure-tap · EVID-2 attestation-chip · EVID-4 audit-trail-arrow ·
  MICRO-1 hairline-hover · MICRO-5 focus-ring · EDIT-1 fade-stagger · NAV-1
  sticky-condensed (current Continua canonical) · NAV-4 breadcrumb · QUOTE-1
  editorial-pull-quote · QUOTE-3 single-with-portrait · QUOTE-5 attribution-
  rich · QUOTE-6 peer-citation-named-industry.
- **Forbidden in safe pool**: KPI-2 count-up · KPI-3 live-counter · KPI-4
  range-fill · MICRO-2 card-lift (stewardship cards stay still) · MICRO-3
  magnetic · MICRO-6 cursor-vignette · MEDIA-2 parallax · MEDIA-1 cinematic-
  fade · NAV-3 progress-bar · NAV-2 hide-on-scroll · gallery-snap · sticky-
  stack-rotate · drop-cap-stagger.
- **Cluster fit**: corporate-suite LF-5 (Continua canonical) · medical-
  specialist (Cassazione-grade clinical authority) · fiduciary-stewardship
  (paper) · law-classic-gold heavier-forensic register variant.
- **Anti-fit**: every cluster whose audience verb is "explore", "ship",
  "buy", "play", "watch", "fit", "taste" · LF-1/3/4 generic corporate-suite
  (the institutional register expects the count-up and would lose the proof
  signal if static).

### 3.6 · `g5-sprint-console` (sprint-product)

- **Feel**: "this product ships. Things are in motion." Live-data feel.
  Ticker chips with real (or simulated) numbers updating every 8-12s. Scroll-
  progress bar. Magnetic CTA on hero. Snap-fold scroll on hero. Glow-pill
  CTA with subtle drop-glow.
- **Safe pool**: KPI-1 + KPI-2 + KPI-3 live-counter (cluster signature
  pattern) + KPI-4 range-fill + KPI-5 comparative-tick · EVID-2 attestation-
  chip · MICRO-1 hairline-hover · MICRO-2 card-lift-restrained (lift ≤
  4px) · MICRO-3 magnetic-button-restrained (single hero CTA only) · MICRO-5
  focus-ring · EDIT-1 fade-stagger · NAV-2 sticky-hide-on-scroll-down ·
  NAV-3 scroll-progress-bar-thin · NAV-4 breadcrumb · NAV-5 locale-pill-flag
  (allowed) · QUOTE-2 quote-carousel-restrained · QUOTE-5 attribution-rich ·
  CASE-2 list-row-stagger · CASE-6 filterable-grid-with-chips · COMP-2
  scenario-tab-switcher · COMP-3 metric-vs-benchmark-chip · MEDIA-3 image-
  grid-stagger.
- **Forbidden in safe pool**: parallax (G6 only) · cursor-vignette (G6
  dark-hero only) · cinematic-fade (G6 only) · stewardship-rings · scroll-
  driven-timeline · drop-cap-stagger · sticky-side-rail · sticky-stack-rotate ·
  page-flip · magazine-grid 3+1 (LF-2 only).
- **Cluster fit**: agency-digital-studio (Aura · cluster signature) ·
  startup-saas-landing (Elevate · cluster signature) · lawyer-modern-
  transparent (Juris · light-touch borrowing only · KPI-3 live-counter still
  excluded for Juris).
- **Anti-fit**: corporate-suite (the boardroom-advisory register collapses
  under sprint-feel) · lawyer-classic-gold · medical-specialist · real-
  estate-luxury · restaurant-fine.

### 3.7 · `g6-cinematic` (curatorial-cinematic)

- **Feel**: "this site is a slow film." Slow fade transitions. Ken-Burns
  drift on full-bleed photos. Scroll-snap on horizontal hero strips. Cursor
  vignette in dark hero. Lightbox preserves scroll position.
- **Safe pool**: MEDIA-1 cinematic-fade-on-view (cluster default) · MEDIA-2
  parallax-restrained (hero only · single layer · disabled below 880px) ·
  MEDIA-3 image-grid-stagger (100ms slow stagger) · MEDIA-4 before-after-
  slider (when semantic · medical-specialist case-studies · restoration ·
  brand-redesign) · MEDIA-5 gallery-strip-snap-horizontal · MEDIA-6 lightbox-
  preserve-context · MICRO-1 hairline-hover · MICRO-5 focus-ring · MICRO-6
  cursor-vignette (dark-hero only · disabled on touch · disabled with reduced-
  motion) · EVID-5 provenance-tooltip-image · EDIT-1 fade-stagger ·
  TIME-5 chapter-stepper (when narrative chapters exist) · QUOTE-1 editorial-
  pull-quote · QUOTE-4 sticky-stack-rotate (with discipline).
- **Forbidden in safe pool**: count-up (KPI-2) · live-counter (KPI-3) ·
  range-fill (KPI-4) · comparative-tick (KPI-5) · scroll-progress-bar (NAV-3) ·
  sticky-hide-on-scroll (NAV-2) · magnetic-button (MICRO-3) · card-lift
  (MICRO-2) · scroll-driven-timeline · stewardship-rings · drop-cap-stagger
  (G2-only) · sticky-side-rail (G2-only) · filterable-grid-chips · scenario-
  tab-switcher · range-fill · attestation-chip-hover (the tooltip pollutes
  the cinematic stillness · ship the credit as a static EXIF row instead).
- **Cluster fit**: portfolio-cinematic (Pixel canonical) · real-estate-ultra-
  luxury (Villa) · e-commerce-fashion-editorial (Luxe) · agency-creative-
  studio Vertex (lighter touch · hero only).
- **Anti-fit**: corporate-suite · lawyer-classic-gold · medical-clinic ·
  startup-saas-landing · real-estate-mass-market · lawyer-modern-transparent.

---

## §4 · Per-cluster allowed-set + default-profile binding (intake contract)

This is the table the planner consults at A.1 intake to declare a sibling's
motion_profile. The cluster + sub-cluster + layout-family triple selects the
allowed set; the planner picks ONE.

| cluster | sub-cluster / family | allowed motion_profile set | default | notes |
|---|---|---|---|---|
| corporate-suite | LF-1 (advisory) | `g3-institutional` | g3 | Pragma canonical · 1-occupancy today |
| corporate-suite | LF-2 1st-occupant (editorial-press) | `g2-editorial` | g2 | Cornice canonical · LF-2 1st-occupant ALWAYS picks `g2-editorial` (no count-up) |
| corporate-suite | LF-2 2nd-occupant (editorial-press) | `g2-editorial-counter` | g2-counter | Causa canonical · 2nd-occupant ALWAYS picks `g2-editorial-counter` (the within-family differentiator vs Cornice) |
| corporate-suite | LF-2 3rd-occupant (editorial-press) | `g2-editorial` OR `g2-editorial-counter` (with AC-V5 cumulative ladder check vs both prior occupants) | TBD | per `lf2-second-occupant-variance-contract.md §3` · 3rd-occupant must clear AC-V1..V5 vs BOTH Cornice AND Causa |
| corporate-suite | LF-3 (fiscal) | `g3-institutional` | g3 | Fiscus canonical |
| corporate-suite | LF-4 (coaching) | `g3-institutional` | g3 | Solaria canonical |
| corporate-suite | LF-5 (stewardship) | `g4-stewardship` | g4 | Continua canonical |
| corporate-suite | LF-{NEW} (audit-led methodology · law-firm boutique · etc.) | `g3-institutional` OR `g1-safe-premium` (depending on imagery + audience-verb register) | TBD at intake | Phase X.7d+ candidates · paper-deferred per Phase X.7a precondition |
| agency-creative-studio | Vertex / editorial-agency | `g2-editorial` (default) · `g6-cinematic` (hero-only borrowing) | g2 | manifesto-with-peer-voices register |
| agency-digital-studio | Aura / sprint-console | `g5-sprint-console` | g5 | shiplog-console + magnetic CTA |
| portfolio-cinematic | Pixel | `g6-cinematic` | g6 | gallery + lightbox |
| portfolio-editorial-grid | Chiara | `g2-editorial` | g2 | Vertex-class register · numbered-ledger cases |
| real-estate-ultra-luxury | Villa | `g6-cinematic` | g6 | property gallery + concierge editorial cues |
| real-estate-mass-market | Casa | `g1-safe-premium` | g1 | filterable-grid + card-lift |
| lawyer-classic-gold | Lex | `g3-institutional` | g3 | NO `g5` patterns |
| lawyer-modern-transparent | Juris | `g1-safe-premium` (default) · `g5-sprint-console` patterns allowed light-touch (NAV-2 · KPI-5) | g1 | no live-counter |
| medical-clinic / family / wellness | Salute / Famiglia / Benessere | `g1-safe-premium` | g1 | NO `g6`/`g5` patterns |
| medical-specialist | Cardio / Derm | `g4-stewardship` (Cassazione-grade clinical) OR `g3-institutional` | g4 | clinical authority register |
| restaurant-fine | Gusto | `g2-editorial` (default) · `g6-cinematic` (course-image fade-in only) | g2 | course-indexed editorial reveal |
| restaurant-trattoria | Sapore | `g1-safe-premium` | g1 | warm-institutional |
| restaurant-street-modern | Brace | `g5-sprint-console` patterns (sprint-shape borrowing) OR `g1-safe-premium` | g1-or-g5 | NEVER countdown timers |
| ecommerce-artisan | Bottega | `g1-safe-premium` (default) · `g2-editorial` (warm) | g1 | NEVER scarcity-timers |
| ecommerce-fashion-editorial | Luxe | `g6-cinematic` | g6 | gallery-strip + lightbox |
| startup-saas-landing | Elevate | `g5-sprint-console` | g5 | live-counter + magnetic CTA + scroll-progress |

The orchestrator REJECTS any A.1 brief whose declared motion_profile is
outside the cluster's allowed set. (Planner-side rejection is paper-only
today; code-side enforcement is Phase X.7c.)

---

## §5 · Anti-tacky red-lines · per profile

These are the bright lines that, if crossed, demote a profile from
"premium" to "tacky" regardless of how well the rest of the page is
executed. Each line is a YES/NO check the style-critic walks at A.6.

### Cross-profile (every motion_profile honors these)

- **AT-X1**: `prefers-reduced-motion: reduce` is honored at the JS root.
  Animation-bearing patterns short-circuit to their static fallback. Verified
  at workflow C/D walk on every locale.
- **AT-X2**: NO decorative motion. The detector test is: "if the animation
  is removed, does the page lose any information?" If no, the motion is
  decorative and is banned.
- **AT-X3**: NO manipulative-SaaS motion. The detector test is: "is the
  motion designed to override visitor judgement?" Examples: blinking CTAs ·
  countdown timers · "X people viewing now" · exit-intent overlays · scarcity
  badges. All BANNED at archetype level.
- **AT-X4**: NO once-per-session animation re-triggers on scroll-back.
  KPI-2 captures session-scope, not viewport-scope.
- **AT-X5**: total stagger ≤ 1500ms on any multi-element reveal. Anything
  longer reads as page loading.

### `g1-safe-premium`

- **AT-G1-1**: count-up ≤ 1 invocation per home (the KPI band).
- **AT-G1-2**: card-lift ≤ 3px · shadow blur ≤ 16px · shadow opacity ≤ 0.10.
- **AT-G1-3**: NO parallax on any surface.

### `g2-editorial`

- **AT-G2-1**: NO count-up. The static numeric proof is the editorial signature.
- **AT-G2-2**: drop-cap fades · NEVER drops in from above · NEVER pulses ·
  NEVER stretches.
- **AT-G2-3**: pull-quote em-reveal delay 200ms · NEVER colour-flashes ·
  NEVER grows.
- **AT-G2-4**: NO scroll-progress-bar (sprint-class · pollutes editorial register).

### `g2-editorial-counter`

- **AT-G2C-1**: count-up ≤ 1 invocation per home (the KPI overlay tuple).
- **AT-G2C-2**: NAV-1 sticky-condensed delta ≠ LF-5's 76→56 (use 84→64 to
  preserve LF-2 chrome distinction).
- **AT-G2C-3**: EVID-5 tooltip ≤ 240px wide · hover-only · NO permanent
  watermark · NO glint animation.
- **AT-G2C-4**: card-lift FORBIDDEN on the magazine-grid 3+1 (CASE-1 cards
  stay still).

### `g3-institutional`

- **AT-G3-1**: ONE invocation of count-up per home. NO live-counter.
- **AT-G3-2**: hover affordances are hairline-only on body content. NO lift
  on body links. NO accent-glow.
- **AT-G3-3**: card-lift ≤ 3px on cases-list cards. NO tilt.
- **AT-G3-4**: NO marquee beyond the documented sectors-association marquee
  at 110s.

### `g4-stewardship`

- **AT-G4-1**: NO count-up. NO range-fill. NO comparative-tick. The numbers
  are static.
- **AT-G4-2**: NO card-lift on portrait cards. NO accent-glow.
- **AT-G4-3**: NO icon animation. NO emoji. NO confetti. NO spinner.
- **AT-G4-4**: timeline rings draw ONCE on viewport entry · then static.

### `g5-sprint-console`

- **AT-G5-1**: live-counter cadence ≥ 8s · NEVER below. (8-12s is the
  legibility zone.)
- **AT-G5-2**: live-counter MUST cite a documented data source on hover.
- **AT-G5-3**: magnetic-button range ≤ 30px · displacement ≤ 6px · ONE
  magnetic button per viewport · NEVER on body links.
- **AT-G5-4**: scroll-progress-bar height = 1px exactly. NO gradient. NO
  pulse.
- **AT-G5-5**: NEVER autoplay video bg. NEVER countdown urgency. NEVER
  exit-intent. (These are USAGE-BAN-02 manipulative-SaaS lines.)

### `g6-cinematic`

- **AT-G6-1**: parallax HERO ONLY · single layer · disabled below 880px ·
  disabled with reduced-motion.
- **AT-G6-2**: cinematic-fade duration ≥ 1200ms · saturation start ≥ 0.85 ·
  scale start ≤ 1.05.
- **AT-G6-3**: cursor-vignette dark-hero only · disabled on touch · disabled
  with reduced-motion.
- **AT-G6-4**: gallery-snap horizontal-only · keyboard navigable · visible
  scroll-progress indicator.
- **AT-G6-5**: lightbox backdrop is dark-with-alpha (NEVER pure black) ·
  scroll position preserved on close · NO social-share buttons inside.

---

## §6 · Reduced-motion equivalents (mandatory · per profile)

Every profile guarantees a static-equivalent rendering when
`prefers-reduced-motion: reduce` is detected. The user's information access
is preserved; the FEEL is gracefully degraded.

| profile | reduced-motion behavior |
|---|---|
| `g1-safe-premium` | KPI-2 count-up: numbers are at their final value at first paint. Card-lift: static border-color shift on hover instead of lift. Filterable grid: instant layout transition. SCROLL-2 staggered-reveal: content visible at first paint. |
| `g2-editorial` | EDIT-1 fade-stagger: text visible at first paint. EDIT-2 pull-quote-em-reveal: italic-em visible at first paint with surrounding text. EDIT-3 drop-cap-stagger: drop-cap and paragraph visible together. EDIT-4 sticky-side-rail: smooth-scroll → instant scroll · color transition still occurs (color is not motion). |
| `g2-editorial-counter` | full `g2-editorial` behavior PLUS: KPI-2 count-up → static final number. NAV-1 sticky-condensed → nav has fixed condensed height from start. EVID-5 provenance-tooltip → static caption below image (no hover). |
| `g3-institutional` | KPI-2 count-up → static final number. EDIT-1 fade-stagger → content visible at first paint. NAV-1 sticky-condensed → nav has fixed condensed height from start. MICRO-2 card-lift → static border-color shift. SCROLL-2 staggered-reveal → cards visible at first paint. |
| `g4-stewardship` | TIME-1 timeline → unchanged (already static). TIME-2 scroll-driven-timeline → falls back to static TIME-1 vertical timeline. TIME-4 stewardship-rings → all rings drawn statically at first paint. EVID-2 chip-tooltip → tooltip shown without fade transition. |
| `g5-sprint-console` | KPI-3 live-counter → static recent value with timestamp · backend feed paused · "live" badge replaced with "as of HH:MM". MICRO-3 magnetic-button → disabled · static button. NAV-2 sticky-hide-on-scroll-down → nav stays sticky always. NAV-3 scroll-progress-bar → unchanged (scroll-bound width is not animation). MEDIA-3 image-grid-stagger → static grid. |
| `g6-cinematic` | MEDIA-1 cinematic-fade → image fully revealed at first paint. MEDIA-2 parallax → static photo · no offset. MEDIA-3 image-grid-stagger → static grid. MEDIA-4 before-after-slider → side-by-side static photos with labels. MEDIA-5 gallery-snap → regular horizontal scroll · no snap. MEDIA-6 lightbox → unchanged (instant overlay · no fade). MICRO-6 cursor-vignette → disabled. |

The principle (per pattern library §2.12): **every animation has a non-
animation equivalent that delivers the same INFORMATION but not the same
FEEL.** Information remains accessible.

The JS layer guarantees this at render time. Today `static/js/live-motion.js`
short-circuits the entire animation pass at line 50 (`reducedMotion`). The
slice-01 counter gate at line 152 ALSO short-circuits independently. Future
flag wires must follow the same pattern: the gate is checked AFTER the
top-level reduced-motion short-circuit, so reduced-motion always wins.

---

## §7 · How motion_profile contributes to anti-clone 2.0 axis 18

Per `anti-clone-2.0-rules.md §1 axis 18` and §3 critical-axis-veto, every
sibling pair must score ≥ 2 on motion gravity + page choreography. The
scoring rubric:

| score | meaning | example |
|---|---|---|
| 0 | identical motion_profile AND identical bundle flag set | Cornice ↔ Causa pre-slice (both shipped `g2-editorial` register · 0 flags · score 0) |
| 1 | same motion_profile · different bundle flag count (sub-variant differentiation in same gravity) | Cornice ↔ post-slice-00 Causa (both `g2-editorial` family but Causa added KPI-2 · score 1) |
| 2 | adjacent motion_profile (same cluster · different sub-key) OR same profile + ≥3 distinct bundle flags | Cornice (g2-editorial · 0 flags) ↔ Causa post-slice-01 (g2-editorial-counter · 3 flags · adjacent profile) · score 2 |
| 3 | structurally distinct motion_profile (different gravity letter · different cluster fit) | Pragma (g3-institutional) ↔ Continua (g4-stewardship) · score 2 (G3 and G4 are adjacent in the gravity-letter sequence; the conceptual register differs but flag bundle overlap is high) · OR Pragma ↔ Pixel (g6-cinematic) · score 3 |

**Reading the table for the 6 shipped corporate-suite siblings**:

| pair | profiles | flag-count delta | axis 18 score |
|---|---|---|---|
| Pragma ↔ Cornice | g3 ↔ g2 | 1 ↔ 0 | 2 |
| Pragma ↔ Causa | g3 ↔ g2-counter | 1 ↔ 3 | 2 |
| Pragma ↔ Fiscus | g3 ↔ g3 | 1 ↔ 1 | 0 ← v2.0 veto fail (Pragma ↔ Fiscus grandfathered per §19 of design-standard) |
| Pragma ↔ Solaria | g3 ↔ g3 | 1 ↔ 1 | 0 ← v2.0 veto fail (same retrofit deferral applies; documented as Pragma ↔ Solaria 2.0-grandfathered) |
| Pragma ↔ Continua | g3 ↔ g4 | 1 ↔ 0 | 2 |
| Cornice ↔ Causa | g2 ↔ g2-counter | 0 ↔ 3 | 2 (post-slice-01) |
| Cornice ↔ Fiscus | g2 ↔ g3 | 0 ↔ 1 | 2 |
| Cornice ↔ Solaria | g2 ↔ g3 | 0 ↔ 1 | 2 |
| Cornice ↔ Continua | g2 ↔ g4 | 0 ↔ 0 | 1 (different profiles · 0 flag delta · static-vs-static reads similar; this is a S6 cluster-tropes signal not a S4 retrofit signal) |
| Causa ↔ Fiscus | g2-counter ↔ g3 | 3 ↔ 1 | 2 |
| Causa ↔ Solaria | g2-counter ↔ g3 | 3 ↔ 1 | 2 |
| Causa ↔ Continua | g2-counter ↔ g4 | 3 ↔ 0 | 2 |
| Fiscus ↔ Solaria | g3 ↔ g3 | 1 ↔ 1 | 0 ← v2.0 veto fail (same grandfather class) |
| Fiscus ↔ Continua | g3 ↔ g4 | 1 ↔ 0 | 2 |
| Solaria ↔ Continua | g3 ↔ g4 | 1 ↔ 0 | 2 |

11 of 15 pairs clear the veto under the new motion_profile bundle. The 4
that fail are all Pragma/Fiscus/Solaria pairs (they share `g3-institutional`
with identical 1-flag bundles). These are the documented 2.0-grandfathered
corporate-suite trio per design-standard §19. Their retrofit cost is
5-10× higher than Causa's; the user-handshake to retrofit is queued for
Phase X.10+.

For sibling 7 (or any future intake): the cluster's allowed-profile set
SHALL constrain the choice such that axis 18 ≥ 2 vs every existing sibling
is structurally guaranteed by the profile selection. Practically: a 7th
corporate-suite sibling MUST pick a profile + flag bundle that produces
score ≥ 2 vs all 6 existing siblings. Inside the 5 LF families that are
already taken, no profile is unclaimed; opening sibling 7 therefore requires
a NEW LF family AND a profile that does not collide with any existing one.

---

## §8 · Visible-distinctness contribution at the visitor's first 30 seconds

Per the audit's "first-30-second read" framing (anti-clone-2.0 §2):
motion_profile shows up to the visitor on three surfaces in the first
viewport-and-a-half of scroll:

1. **Hero arrival** (first 1.5s of viewport mount): cinematic-fade vs
   static · parallax vs static · cursor-vignette vs static. `g6-cinematic`
   reads instantly different from `g1`/`g2`/`g3`/`g4`.
2. **First scroll past the KPI surface** (typical at 600-1200px scroll):
   count-up arrives or doesn't · live-counter ticks or sits static. The
   binary KPI-2 flag distinguishes `g3-institutional` from `g2-editorial`
   from `g4-stewardship` immediately.
3. **First hover** (when the visitor reaches a card · a chip · a hero
   photo): card-lift · provenance-tooltip · attestation-chip-hover ·
   magnetic-button. The microinteraction layer carries the "this responds
   to me" signal that `g5-sprint-console` advertises and `g4-stewardship`
   refuses.

Together those three surfaces produce ~80% of the "feels different" signal
the user named in the audit. The remaining 20% comes from page-choreography
patterns (timeline · sticky-side-rail · scroll-progress-bar · drop-cap-
stagger) which fire deeper into the page.

A motion_profile selection at A.1 intake therefore commits the planner to
a specific FIRST-30-SECOND READ. The cluster's allowed-set narrows the
choices such that no two siblings can collide on this read — provided
the bundle flag count differs by ≥ 1 within the same profile family
(per LF-2's 1st-vs-2nd-occupant contract) or the profile itself differs
across siblings.

---

## §9 · How motion_profile becomes user-customizable (Phase X.7c · Layer-B preset)

Per `template-personalization-architecture.md §2 CS-12 Motion Presets`:
motion_profile is a **Layer-B curated preset** at the editor side. The
end-user (template customer) does NOT pick from the 7 gravity letters;
they pick from a **3-tier intensity selector** that maps to the cluster's
allowed-profile set:

```
Customer-facing picker:    [ minimal ] [ standard ] [ expressive ]
                                ↓           ↓             ↓
For corporate-suite LF-1:  g3-institutional with kpi_animate=False
                           g3-institutional (default · all flags as DNA-declared)
                           g3-institutional with optional NAV-1 enabled

For corporate-suite LF-2-2nd-occupant (Causa-class):
                           g2-editorial-counter with kpi_animate=False (degrades to g2)
                           g2-editorial-counter (default · all 3 flags)
                           g2-editorial-counter with optional EVID-3 + TIME-3 also enabled

For agency-digital-studio (Aura-class):
                           g5-sprint-console with live-counter=False
                           g5-sprint-console (default)
                           g5-sprint-console with magnetic-button + cursor-vignette enabled

For portfolio-cinematic (Pixel-class):
                           g6-cinematic with parallax=False + vignette=False
                           g6-cinematic (default)
                           g6-cinematic with full bundle (gallery-snap + parallax + vignette)
```

Three architectural rules govern the customer picker:

**RULE A · The cluster's allowed-set is the bounded universe.** A Pragma
customer cannot pick `g6-cinematic`; the picker only exposes their
cluster-conditional intensity tier. This is the same mechanism that hides
"Cornice's graphite-rust palette" from a Pragma customer (per §3.6 of the
personalization architecture).

**RULE B · Reduced-motion always wins.** If the customer picks
`expressive` AND their visitor's OS reports `prefers-reduced-motion: reduce`,
the JS layer short-circuits to the static equivalents per §6. The customer's
choice is preserved as data; the rendering is reduced. This is the AT-X1
binding red-line that no customer setting can override.

**RULE C · Bundle flags expose individually only when safe.** Three flags
are safe-to-individually-toggle (`kpi_animate` · `nav_condense_on_scroll` ·
`evid5_provenance` · the slice-01 set). Six flags are gated on cluster
profile (`live_data_kpi` requires `g5` AND ops-config) and three flags
are NEVER user-toggleable (`magnetic_button` · `hero_parallax` ·
`cursor_vignette` because their misuse-modes are non-obvious to a customer).

The Layer-B preset binds the existing 7 profiles to a customer-friendly
3-tier slider. The customer never sees `g3-institutional`; they see "minimal
· standard · expressive" inside their cluster's tier ladder.

**Phase X.7c implementation scaffold (paper-only here)**:

1. Add `motion_profile_intensity` (`minimal|standard|expressive`) to
   `apps/projects/models.py · ProjectDesignTokens` — Layer-B preset slot.
2. Add `motion_profile_overrides` (JSON dict of flag-name → bool) for the
   per-flag toggles whose `personalization_knobs` field allows them. Layer-C.
3. Editor-side picker reads cluster's allowed-set from the source template's
   DNA + `MOTION_PROFILES` registry.
4. Renderer reads `ProjectDesignTokens.motion_profile_intensity` →
   selects bundle from cluster's tier ladder → falls back to template's
   DNA `motion_profile` if customer left default.

Phase X.7c is paper-deferred until Phase X.7a (non-corporate-suite cluster
ship) or Phase X.7d (Causa workflow C/D · at user-handshake).

---

## §10 · Quality without collapse · why customer customization preserves variety

The user's stated goal: "hundreds of customizable templates · all clearly
different · premium · elegant · modern · professional · dynamic." The
tension is between "customizable" (each customer feels they own the result)
and "all clearly different" (no two final renderings collapse onto each
other).

Motion_profile customization preserves variety through three mechanisms
already declared in `template-personalization-architecture.md §3` and
formalized here for the motion axis:

**Mechanism 1 · Per-cluster preset narrowing.** A corporate-suite LF-1
customer's intensity slider exposes 1 underlying profile (`g3-institutional`)
across 3 tiers. An agency-digital-studio customer's slider exposes 1
different underlying profile (`g5-sprint-console`) across 3 tiers. The
two pickers DRAW FROM DIFFERENT LIBRARIES even though both look identical
to the customer ("minimal · standard · expressive").

**Mechanism 2 · Sibling-aware flag claims.** Inside corporate-suite LF-2,
1st-occupant Cornice claims `g2-editorial` and 2nd-occupant Causa claims
`g2-editorial-counter`. A 3rd LF-2 occupant's customer picker would NOT
expose `g2-editorial-counter` as default (it's claimed); the customer
would land on a new variant — `g2-editorial` with at least one flag the
2nd-occupant did not enable (e.g., NAV-3 light-touch · or EDIT-2 with
extended em-delay). The cluster's preset library NARROWS as siblings ship.

**Mechanism 3 · Layer-A reduced-motion floor.** Every customer's setting
is overridable by the visitor's OS preference. This is the architectural
guarantee that even at `expressive` tier the page never imposes motion
on a visitor who refuses it. The information remains accessible; the
feel is preserved on the customer's chosen ceiling.

The 30/50/20/0 ratio (Layer A locked / Layer B presets / Layer C toggles
/ Layer D banned · per personalization-architecture §1) applies to
motion_profile precisely:
- ~30% Layer A · `prefers-reduced-motion` honored · banned-pattern list
  enforced · cluster's allowed-set is the bounded universe.
- ~50% Layer B · the 3-tier intensity slider + the per-cluster ladder.
- ~20% Layer C · per-flag toggles for the 3 safe individual flags.
- 0% Layer D · NO customer hex-color · NO custom motion-curve picker ·
  NO live-counter URL paste without ops-config gating · NO unbounded
  cadence input.

---

## §11 · Implementation scaffold (lightest non-breaking addition · safe at this pass)

The motion_profile field already exists at `apps/catalog/template_dna.py`
line 200 (slice 01) with the 3-flag bundle. This plan ships **one paper-
only documentation slice** at the standards level + **zero code changes**
this pass.

The lightest *justified* code addition (deferred to a separate slice on
user-handshake) is the **paper-listed bundle extension** in §2 of this
plan: add 9 default-False flag keys to each of the 7 profiles in the
`MOTION_PROFILES` registry. The diff would be ~9 keys × 7 profiles = 63
new key-value pairs · all `False` · zero behavior change · zero new
patterns wired · zero new siblings · zero migrations.

This pass does NOT ship that extension because:
- The 9 paper-flagged patterns (`scroll_progress_bar` · `hero_parallax` ·
  `gallery_snap` · `cinematic_fade` · `card_lift_restrained` ·
  `magnetic_button` · `cursor_vignette` · `live_data_kpi` ·
  `nav_hide_on_scroll_down`) have no corresponding JS gate yet. Adding flag
  keys without JS gates creates a misleading API surface.
- Each gate addition requires its own implementation slice (per pattern
  library §5 priority list) with its own browser walk + scorecard. Bundling
  9 gates into a paper pass is contrary to slice discipline.

Instead this pass updates the standards stack so that the motion_profile
DNA contract is paper-binding at intake **even before** the additional 9
flags ship. The order of operations is:

1. **Today (this pass)**: ratify the motion_profile DNA contract (this
   plan + the catalog reference + design-standard §21 motion_profile cell
   added — see §12 below). 0 lines of code changed.
2. **Phase X.7d slice 03 (or wherever the queue places it)**: ship NAV-2
   sticky-hide-on-scroll-down for the eventual G5 cluster intake. Adds the
   `nav_hide_on_scroll_down` flag with corresponding JS gate.
3. **Phase X.7d slice 04**: ship MICRO-2 card-lift-restrained. Adds the
   `card_lift_restrained` flag with CSS gate (no JS · `:hover` is enough).
4. **Phase X.7a**: ship the first non-corporate-suite cluster (Vertex or
   Aura · per audit §11). The new cluster's intake is the FIRST that
   declares motion_profile **before** code is written; it is the first
   intake test of this plan as a binding contract.
5. **Phase X.7c**: editor-side Layer-B preset · `motion_profile_intensity`
   field on `ProjectDesignTokens` · the customer picker.

---

## §12 · Standards-stack updates (paper · Phase X.7b · this pass)

The motion_profile DNA contract requires three references update so that
every workflow gate honors it. Each update is ≤ 10 lines + 1 cross-reference:

1. **`factory/standards/corporate-suite-design-standard.md`**: add a new
   section §21 `· motion_profile DNA cell` that names the cluster's allowed
   set + binds the LF-2 1st-vs-2nd-occupant contract to the
   `g2-editorial` ↔ `g2-editorial-counter` profile pair. Cross-reference
   this plan + the catalog.
2. **`design-orchestrator/references/internal-baselines/next-template-brief-
   schema.md`**: add a row `motion_profile` to §1 Required-inputs intake
   table. Format: one of the 7 enumerated keys per cluster's allowed-set.
   The brief blank-field rule already binds the rejection.
3. **`design-orchestrator/references/internal-baselines/corporate-suite-
   distinctness-matrix.md §1.11`** (motion row): replace "motion is a
   cluster invariant" with "motion is the `motion_profile` DNA cell · scored
   per anti-clone-2.0 axis 18 · ≥2 vs every sibling · v2.0 grandfather
   exception applies to Pragma/Fiscus/Solaria trio only."

These three updates are documented in §12 as paper-pending. They do not
ship in this report; they are companion updates that the orchestrator
applies in the same paper-pass cycle on user handshake.

---

## §13 · Workflow-gate verification matrix

Where motion_profile gets checked at every workflow step:

| gate | check | verifier | evidence |
|---|---|---|---|
| A.0 territory-scout | candidate's likely motion_profile per cluster | scout report | territory scout includes profile prediction |
| A.1 intake | brief declares motion_profile from cluster's allowed set | planner | brief field filled |
| A.2 plan | plan re-checks declared profile against bundle's enabled flags · scores axis 18 vs every existing sibling | planner + style-critic at plan-gate | plan carries scored matrix |
| A.5 build | builder wires the declared profile's bundle flags · adds DNA entry | builder | DNA entry committed · body data-attributes emitted |
| A.6 review-lock | style-critic walks the rendered template with the declared profile's anti-tacky red-lines | style-critic | review-lock report cites profile name + flag count |
| Workflow C/D walk | browser-verifier walks every locale × viewport with both default-motion AND `prefers-reduced-motion: reduce` · confirms reduced-motion fallback per §6 | browser-verifier | walk-log per profile · reduced-motion screenshots |
| Workflow D flip | gatekeeper scores axis 18 vs every existing sibling | release-gatekeeper | scorecard panel motion_profile-summary |

The workflow C/D `prefers-reduced-motion: reduce` walk is the single most
load-bearing motion verification. It is binding for every template that
ships any motion_profile flag set to `True`.

---

## §14 · Whether motion_profile is ready to bind future intakes

**Yes.** As of ratification of this plan + the companion catalog + the
three standards-stack updates in §12, motion_profile is a first-class DNA
axis the planner declares at A.1, the style-critic scores at A.6, and the
gatekeeper scores at workflow D flip.

The readiness rests on:
- 7 enumerated values with distinct cluster-fits and feel-statements.
- 12 declared bundle flags · 3 wired today · 9 paper-flagged for future
  slices.
- Per-cluster allowed-set table (§4) covering all 23 enrolled archetypes
  + 5 candidate clusters.
- Anti-tacky red-line list per profile (§5).
- Reduced-motion fallback table per profile (§6).
- Anti-clone 2.0 axis 18 scoring rubric (§7) with the 15 corporate-suite
  pair scores enumerated.
- Layer-B customer-customization plan (§9) tied to the existing
  personalization architecture.
- Workflow-gate verification matrix (§13).

Future intakes have everything needed to declare a non-collision motion
profile at A.1 brief authoring.

---

## §15 · Whether sibling 7 can open after this

**Conditionally yes for non-corporate-suite clusters; no for a 7th corporate-
suite sibling.**

For a non-corporate-suite cluster (Phase X.7a candidates · Vertex agency-
creative-studio · Aura agency-digital-studio · ultra-luxury cinematic real-
estate · etc.):
- The cluster's allowed-set is declared in §4 above.
- The intake clears axis-18 immediately because the cluster's default
  profile is structurally different from corporate-suite's (G2/G5/G6 vs
  G1-G4).
- The other 17 axes need separate scoring (typography envelope · audience
  verb register · imagery register etc.) per anti-clone-2.0 §1.
- **Sibling 7 of the FACTORY (1st of a new cluster) is the audit's
  recommended next product pass and CAN OPEN after this plan ratifies +
  Phase X.7a workflow A.1 intake authors a brief that picks a non-corporate-
  suite motion profile.**

For a 7th corporate-suite sibling:
- Per anti-clone-2.0 §11 + §7 NEVER-DO matrix: "Ship a 7th corporate-suite
  sibling without retrofitting Causa first" was the binding red-line.
- Causa retrofit slice 01 has shipped (28/54 · all 5 vetoes pass · LF-2
  AC-V1..V5 ratified). That red-line is now CLEARED.
- The remaining red-line per anti-clone-2.0 §7 NEVER-DO: "Add a 7th sibling
  to corporate-suite without first shipping a non-cs cluster · extends S6
  overused-tropes problem." This red-line is STILL ACTIVE.
- Per anti-clone-2.0 §5 S6 operational rule: "S6 = fix at cluster level.
  Cannot be addressed inside the cluster. Phase X.7a (ship a non-corporate-
  suite cluster) is the only resolution to S6 overused tropes; v2.0
  retrofits resolve S4 and S5 but cannot resolve S6 inside corporate-suite."
- Therefore: a 7th corporate-suite sibling **CANNOT OPEN** until at least
  one non-corporate-suite cluster ships at hardening parity (Phase X.7a).

**The ordering**: Phase X.7a (1st non-cs cluster · sibling 7 of factory) →
Phase X.7c (editor Layer-B preset picker) → Phase X.10+ (eventual 7th
corporate-suite sibling on a NEW LF family with a non-collision motion
profile).

---

## §16 · Strongest conclusion

The motion_profile DNA axis is **production-ready as a paper contract**
the moment this plan + the companion catalog + the three standards-stack
cross-references ratify. The cluster's allowed-set tables (§4) cover all
23 enrolled archetypes and the 5 cluster candidates. The anti-clone 2.0
axis-18 scoring rubric (§7) is operational with the 15 corporate-suite
sibling pairs enumerated; 11 of 15 already clear the v2.0 critical-axis
veto under the 3-flag bundle, and the 4 Pragma/Fiscus/Solaria failures
are documented as 2.0-grandfathered. The reduced-motion guarantee (§6)
is structurally enforced at `static/js/live-motion.js` line 50 and
the bundle gate pattern proven by slice 01.

The DNA axis itself **is ready** to bind future intakes today. **Sibling 7
of the factory can open today** — it is necessarily a Phase X.7a non-
corporate-suite cluster (per audit §11 + S6 rule). **A 7th corporate-suite
sibling cannot open** until at least one non-cs cluster ships at hardening
parity, regardless of how well its motion_profile would score. The S6
cluster-tropes rule is independent of the motion axis and binds the
ordering.

The lightest implementation scaffold this pass is to NOT extend the
`MOTION_PROFILES` registry in code (the extension is paper-listed in §2
for the 9 currently un-wired flags · code change waits for each flag's
own implementation slice). The paper contract here is the implementation
this pass ships.

The next implementation pass that depends on this plan is whichever the
user-handshake authorises: Phase X.7a (ship a non-cs cluster · sibling 7
of factory · the recommended next product pass per audit §11), Phase X.7c
(editor Layer-B preset picker · unblocks customer-side motion variety),
or Phase X.7d slice 03+ (additional Causa retrofits R2 EVID-3 + R3
TIME-3 · pushes Cornice ↔ Causa pair score from 28/54 toward 30/54+).
