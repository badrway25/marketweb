# Dynamic-pattern usage rules

```yaml
file_type:    internal-baseline · rule book · enforcement document
status:       v1 · paper-only · binding for every workflow that touches motion
date:         2026-05-05
authority:    orchestrator-side · binding once committed (Phase X.7b
                implementation pass adopts these as `[REQUIRED]` /
                `[BLOCKING]` rules in the per-cluster design-standard files)
companion:    factory/reports/hardening/premium-dynamic-pattern-library.md
                (the comprehensive 48-pattern library)
              design-orchestrator/references/internal-baselines/
                premium-dynamic-pattern-catalog.md (the index · gravity matrix ·
                cluster recommendations)
purpose:      tell every agent in the pipeline (planner · builder · style-
                critic · browser-verifier · release-gatekeeper) when a pattern
                may be used, when it requires escalation, when it is banned,
                and what evidence proves correct adoption
audience:     planner at A.1 intake · builder at A.5 build · style-critic at
                A.6 critique · browser-verifier at workflow C/D walk · release-
                gatekeeper at flip
```

---

## §1 · Severity ladder (binding)

Every rule below carries one of these four tiers. Same ladder as the
existing CS-* rule book.

| Tier | Meaning | Where it gates |
|---|---|---|
| **[BLOCKING]** | merge-blocker · walk-fail · no waiver without § decision | A.5 build · A.6 critique · workflow D · release-gatekeeper |
| **[REQUIRED]** | walk-fail · waiver only with § decision in design-standard | A.6 · workflow D · release-gatekeeper |
| **[STRONG]** | critique-flag · re-spec preferred but not blocking | style-critic · plan re-spec |
| **[GUIDELINE]** | preference · documented for cluster cohesion | plan-time annotation only |

---

## §2 · Cluster invariant rules (every cluster · all gravities)

These hold across every cluster, every layout family, every sibling. A
proposal that violates any of them triggers a § decision review at the
design-standard level — not at the per-sibling level.

### CS-MOTION-INV-01 [BLOCKING] · `prefers-reduced-motion` is honoured globally
- Every motion pattern MUST detect `@media (prefers-reduced-motion: reduce)`
  and fall back to its reduced-motion equivalent (per library §2.12).
- The fallback delivers the same INFORMATION (the visitor can still read
  the data, navigate the timeline, see the gallery) — it does NOT need to
  deliver the same FEEL.
- **Failure mode**: a reduced-motion visitor cannot access content because
  the content is animation-gated.
- **Evidence**: browser-verifier emulates `prefers-reduced-motion: reduce`
  on every walk · BRWS-MOTION-INV-01 fires per pattern.

### CS-MOTION-INV-02 [BLOCKING] · No decorative motion
- A decorative animation has no semantic purpose. Detector test:
  "if removed, does the page lose any information?" If no, the motion is
  decorative.
- BANNED examples (non-exhaustive): floating shapes · background gradient
  sweeps · particle effects · cursor trails · light-flares · idle-loop
  video backgrounds without purpose · rotating hero text "AI · Smart ·
  Modern" carousels.
- **Failure mode**: the page reads as a marketing template.
- **Evidence**: style-critic at A.6 lists every motion path on the home and
  cites a semantic purpose for each. Any animation without a documented
  purpose triggers a fix.

### CS-MOTION-INV-03 [BLOCKING] · No manipulative-SaaS motion
- A manipulative animation is designed to override visitor judgement.
  Detector test: "is the motion pushing a conversion through urgency or
  social pressure?" If yes, banned.
- BANNED examples: blinking CTAs · "limited time" countdowns · urgency
  badges · "X people are viewing this now" notifications · autoplay
  carousels · popup modals that bounce in · exit-intent overlays · "don't
  go!" interceptors · scarcity timers · social-proof fly-ins.
- **Failure mode**: the page reads SaaS-funnel.
- **Evidence**: style-critic at A.6 verifies none of the banned patterns
  appear in source or render.

### CS-MOTION-INV-04 [BLOCKING] · The focus-visible gold ring is the same everywhere
- `:focus-visible` is the cluster's signature interactive moment. Per
  CS-NAV-02. Across all gravities the ring is `outline: 2px solid
  var(--accent); outline-offset: 4px; static`.
- **Failure mode**: a sibling overrides the ring (pulse · color shift ·
  drop-shadow). Triggers a § decision because it breaks accessibility
  parity across the cluster.

### CS-MOTION-INV-05 [REQUIRED] · One-time animation per session
- Patterns triggered by viewport intersection (KPI-2 · TIME-2/3 · MEDIA-1 ·
  EDIT-1 et al.) MUST animate ONCE per session. `sessionStorage` is the
  recommended mechanism.
- **Failure mode**: scroll-back retriggers the animation · reads slot-machine.
- **Evidence**: browser-verifier scrolls past the section, scrolls back, and
  confirms the animation does NOT replay.

### CS-MOTION-INV-06 [REQUIRED] · No scroll-jacking
- Scroll-driven patterns may track position (sticky · pin · progress) but
  may NEVER hijack scroll velocity to enforce a per-step pause.
- **Failure mode**: visitor scrolls and the page resists · reads
  presentation-mode.
- **Evidence**: browser-verifier at workflow C walks with normal scroll
  velocity and confirms no resistance.

### CS-MOTION-INV-07 [BLOCKING] · No autoplay carousels
- Carousels (QUOTE-2 · MEDIA-5) MUST require explicit visitor action
  (click · keyboard · swipe). NEVER auto-advance on a timer.
- **Failure mode**: content moves while the visitor is reading · reads
  marketing-banner.
- **Evidence**: style-critic verifies no `setInterval` advances a carousel.

### CS-MOTION-INV-08 [REQUIRED] · Every animation has a documented duration ceiling
- No animation exceeds:
  - micro-interaction: 300ms
  - viewport-reveal entry: 900ms
  - cross-fade transition: 350ms
  - scroll-driven sticky transition: 250ms
  - timeline draw: 1800ms
  - cinematic Ken Burns: 8000ms (longest legitimate animation in the system)
  - gallery snap: 400ms (deceleration)
- **Failure mode**: animations chain into each other and the page reads
  loading.
- **Evidence**: style-critic audits durations declared in CSS / JS against
  these ceilings.

### CS-MOTION-INV-09 [BLOCKING] · No magazine-page-flip
- EDIT-5 is permanently banned. 3D-flip carousels · page-curl-on-scroll ·
  2-page-spread that pages over with simulated paper sound · all banned.
- **Failure mode**: reads gimmick. The cluster's editorial register is
  defeated by the page-flip metaphor.

### CS-MOTION-INV-10 [REQUIRED] · Animation has a `motion_profile` source declaration
- Every animation in source code MUST declare which `motion_profile` (G1–G6)
  it belongs to via comment or class name.
- **Failure mode**: an animation enters source without gravity declaration ·
  drift to wrong gravity at next refactor.
- **Evidence**: style-critic at A.6 grep-confirms every animation file/section
  carries a `/* @motion_profile: G2 */` annotation or `cs-anim--g2-*` class.

---

## §3 · Per-pattern allow/deny rules (binding)

Each row gives `[REQUIRED]` constraints + the § decision triggers.

### Family 1 · KPI / count-up

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| KPI-1 tabular-static | every cluster | — | — (cluster default) |
| KPI-2 count-up-on-view | G1, G2, G3, G5 | G4, G6 | invoking outside G1/G2/G3/G5 · invoking 2× per home |
| KPI-3 live-counter | G5 only | G1, G2, G3, G4, G6 | proposed for non-G5 cluster · cadence < 8s · without timestamp · without source attribution |
| KPI-4 range-fill | G1 (audit-led only), G3 (audit-led), G5 | G2, G4, G6 | proposed for editorial · proposed with gradient · proposed with comma-by-comma reveal |
| KPI-5 comparative-tick | G1, G5 | G2, G3, G4, G6 | proposed without benchmark source · proposed with color coding (green/red) |

### Family 2 · Timeline / progression

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| TIME-1 static-vertical-timeline | G3, G4 (default) | — | — |
| TIME-2 scroll-driven-timeline | G2, G4 (2nd-occupant) | G1 (Pragma/Fiscus), G3 institutional, G5, G6 | proposed for 1st cluster occupant when family signature requires static · proposed with scroll-jacking |
| TIME-3 chronological-tick-horizontal | G2 | G3, G4, G5 | proposed in a cluster that already ships TIME-1 (one timeline shape per cluster) |
| TIME-4 stewardship-rings-concentric | G4 only | other gravities | proposed in non-stewardship register · ring count > 4 |
| TIME-5 chapter-stepper-magazine | G2, G6 | G3, G5 | proposed in non-narrative register · TOC takes over screen |

### Family 3 · Evidence / proof reveal

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| EVID-1 progressive-disclosure-tap | G1, G3 | G6 | proposed in cinematic register · expansion bounces |
| EVID-2 attestation-chip-hover | G1, G2, G3, G4 | G5, G6 | tooltip with drop-shadow · click opens an internal modal |
| EVID-3 case-citation-pop | G3 forensic only | non-forensic clusters | proposed for any non-forensic register |
| EVID-4 audit-trail-arrow | G1, G3, G4 | G6 | arrow grows on hover · arrow with `target="_blank"` |
| EVID-5 provenance-tooltip-image | G2, G6 | G1/G3/G4/G5 | overlay watermark visible permanently · without hover gate |

### Family 4 · Media block

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| MEDIA-1 cinematic-fade-on-view | G6 | G1, G2, G3, G4 | duration < 1200ms · saturation start < 0.85 · scale start > 1.05 |
| MEDIA-2 parallax-restrained-hero | G6 only · hero only | every non-G6, every non-hero context | parallax outside hero · multi-layer · enabled on mobile |
| MEDIA-3 image-grid-stagger-reveal | G2, G5, G6 | G1 (institutional · except for case-list), G3 (Causa), G4 | total stagger > 1500ms · scale animation · flip animation |
| MEDIA-4 before-after-drag-slider | G1 (with discipline), G6 | corporate-suite, lawyer, e-commerce, restaurant | auto-animation on arrival · pulsing handle · initial position outside 30-70% |
| MEDIA-5 gallery-strip-snap-horizontal | G6 only | G1, G2, G3, G4, G5 | vertical snap · without keyboard navigation · without visible scroll-progress |
| MEDIA-6 lightbox-preserve-context | G6 only (paired with MEDIA-5) | non-G6 | pure-black backdrop · scroll position lost on close · social-share buttons |

### Family 5 · Hover / focus / microinteraction

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| MICRO-1 hairline-accent-on-hover | every cluster | — | thickness change on hover · slide animation |
| MICRO-2 card-lift-restrained | G1, G3, G5 | G2 (LF-2 cards stay still), G4 (stewardship cards stay still), G6 (gallery images don't lift) | lift > 4px · shadow blur > 16px · rotation/tilt |
| MICRO-3 magnetic-button-restrained | G5 only · hero CTA only | every other cluster, every non-hero CTA | range > 30px · displacement > 6px · multiple per viewport · on body links |
| MICRO-4 text-underline-grow-from-left | G1, G2 | G3 (institutional prefers static), G5 (use magnetic instead) | grow from center · grow from right · duration < 150ms · auto-collapse on timer |
| MICRO-5 accent-glow-focus-ring | every cluster (invariant) | — | outline ≠ 2px · pulse · glow blur · inset |
| MICRO-6 cursor-vignette | G6 only · dark hero only | every other cluster, every other context | enabled on touch · enabled on light backgrounds · vignette intensity > 20% darken |

### Family 6 · Editorial motion

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| EDIT-1 text-fade-in-on-view-staggered | every cluster (default) | — | total stagger > 1500ms · re-fade on scroll-back |
| EDIT-2 pull-quote-em-reveal | G2 | G3, G5, G6 | em scale start < 0.95 · color change · flash |
| EDIT-3 drop-cap-stagger-around-paragraph | G2 | G3, G5, G6 | drop-cap drops in from above · pulse · stretch |
| EDIT-4 sticky-side-rail-anchor-active | G2 (default for narrative) | non-LF-2 families | side-rail with background fill · smooth-scroll with overshoot |
| EDIT-5 magazine-page-flip | NOWHERE | EVERYWHERE (BANNED) | proposed at all (always § decision · always denied) |

### Family 7 · Navigation behavior

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| NAV-1 sticky-condensed-on-scroll | G1, G2 (2nd-occupant), G3, G4 (default) | G5 (G5 nav stays fixed), G6 | shrink with bounce · shrink that hides links |
| NAV-2 sticky-hide-on-scroll-down | G1, G5 | G2, G3, G4, G6 | hide threshold < 120px (jitter) · hide of locale switcher |
| NAV-3 scroll-progress-bar-thin | G2 (light-touch · long narrative only), G5 | G3, G4, G6 | thickness > 1px · gradient · pulse |
| NAV-4 breadcrumb-persistent-deep | G1, G3 | G2 (no deep-nav reading), G6 | breadcrumb on home · emoji separators · horizontal scroll |
| NAV-5 locale-pill-with-flag | G5, G6 (with discipline) | corporate-suite, lawyer-classic-gold, medical-specialist (institutional register rejects emoji-in-chrome) | invoking in institutional register |
| NAV-6 scroll-position-memory | G1, G2 (consent-gated) | non-consent contexts, G3/G4/G5/G6 by default | enabled without consent · first-visit override |

### Family 8 · Comparison / scenario

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| COMP-1 (= MEDIA-4) | (see MEDIA-4) | (see MEDIA-4) | — |
| COMP-2 scenario-tab-switcher | G1, G5 | G2, G6 | tab labels using "without us" framing · cross-fade with slide · active tab with background fill |
| COMP-3 metric-vs-benchmark-chip | G1, G5 | G2/G3/G4 (no benchmark register) | benchmark without source · color coding · arrow rotation |
| COMP-4 case-vs-baseline-narrative | G1, G3 | e-commerce, restaurant | photos without consent · stock photos for "before" |

### Family 9 · Quote / testimonial / authority

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| QUOTE-1 editorial-pull-quote-static | every cluster (default) | — | quotation-mark sweep on arrival · card chrome · without attribution |
| QUOTE-2 quote-carousel-restrained | G1, G5 | G2, G6 | autoplay · arrows · > 3 quotes |
| QUOTE-3 single-quote-with-portrait | G1, G3, G4 | G6, e-commerce | LinkedIn-style stock headshot · "verified" badge · quote > 60 words |
| QUOTE-4 quote-stack-sticky-rotate | G2 (2nd-occupant), G6 | G3, G5 | scroll-jacking · flip · > 3 quotes |
| QUOTE-5 attribution-rich-quote | G1, G2, G3, G4 | G5, G6 | > 3 attribution lines · emoji · "verified" badges |
| QUOTE-6 peer-citation-named-industry | G3, G4 | G5, G6 | excerpt > 30 words · without external link |

### Family 10 · Case-study preview

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| CASE-1 magazine-grid-3+1 | G2 (LF-2 default) | every non-LF-2 family | invoking outside LF-2 · 4 equal cards |
| CASE-2 list-row-stagger | G1, G3, G5 (default) | G2, G6 | sideways shift on hover · infinite scroll |
| CASE-3 (= TIME-1) | (see TIME-1) | (see TIME-1) | — |
| CASE-4 (= MEDIA-5) | (see MEDIA-5) | (see MEDIA-5) | — |
| CASE-5 numbered-ledger-editorial | G2, G3 | G6 | ledger with crossed-out items · > 5 columns |
| CASE-6 filterable-grid-with-chips | G1 (case-list page only · NOT home), G5 | G6 | reflow > 500ms · empty state without copy |
| CASE-7 case-card-reveal-inline | G1, G2 (NOT in 3+1 magazine) | G6 | content-shift jumps · expand-into-modal |

### Family 11 · Scroll choreography

| Pattern | Allowed in | Banned in | § Decision triggers |
|---|---|---|---|
| SCROLL-1 (= EDIT-1) | every cluster | — | (see EDIT-1) |
| SCROLL-2 staggered-reveal-multi-card | every cluster (default) | — | total stagger > 1500ms · re-trigger on scroll-back |
| SCROLL-3 sticky-pin-with-progress-narrative | G2 only | G1, G3, G4, G5, G6 | pin scope full-page · pin breaks below 880px |
| SCROLL-4 (= MEDIA-5) | (see MEDIA-5) | (see MEDIA-5) | — |
| SCROLL-5 (= MEDIA-2) | (see MEDIA-2) | (see MEDIA-2) | — |
| SCROLL-6 scroll-velocity-aware-fade | every cluster (meta-pattern) | — | thresholds outside 1500-3000px/s defaults |

---

## §4 · Personalization · what end-users may configure (binding)

Per `premium-dynamic-pattern-catalog.md §5` + library §4. Binding rules:

### USAGE-PERSONAL-01 [REQUIRED] · `prefers-reduced-motion` is automatic
- The OS-level setting overrides every motion intensity choice.
- The orchestrator does NOT expose an end-user toggle that re-enables motion
  when reduced-motion is set.

### USAGE-PERSONAL-02 [REQUIRED] · Motion intensity is a discrete enum
- Values: `minimal · standard · expressive`.
- `expressive` is only available for clusters with G5 or G6 default gravity.
- Default per template is `standard`.

### USAGE-PERSONAL-03 [REQUIRED] · Per-pattern parameter knobs are discrete
- Duration / stagger / shrink-ratio / etc. are picked from a documented enum,
  NOT free numeric input.
- Example: KPI-2 duration = `600ms · 800ms · 900ms`.
- **Failure mode**: free numeric input lets an end-user pick 50ms (slot-
  machine) or 5000ms (broken). The pre-validated enum prevents both.

### USAGE-PERSONAL-04 [REQUIRED] · Live-data backend hookup requires ops config
- KPI-3 `live-counter` requires a backend feed URL.
- Default: feature DISABLED.
- Enabling requires the orchestrator to configure the URL at the apps/catalog
  layer · NOT exposed to the end-user editor for security reasons.
- **Failure mode**: end-user wires a feed they don't own · breaks trust ·
  exposes implementation details · CORS errors break the page.

### USAGE-PERSONAL-05 [GUIDELINE] · End-user can save N motion presets per project
- A "premium · animated · expressive" preset stack tied to a `motion_profile`
  in DNA.
- Saved on `projects.CustomerProject` (out of scope this pass · enters editor
  scope at Phase X.7c+).

---

## §5 · The 6 motion gravities · binding cluster default mapping

The orchestrator does NOT redefine these per pass.

| Cluster | Default gravity | Cluster sub-gravity (when LF-specific) |
|---|---|---|
| corporate-suite | G3 | LF-2 → G2; LF-5 → G4 |
| agency-creative-studio | G2 | — |
| agency-digital-studio | G5 | — |
| portfolio-cinematic | G6 | — |
| portfolio-editorial-designer-grid | G2 | — |
| real-estate-mass-market | G1 | — |
| real-estate-ultra-luxury | G6 | (with G2 narrative cues for property-detail) |
| lawyer-classic-gold | G3 | — |
| lawyer-modern-transparent | G1 | (with light G5 borrowing) |
| medical-clinic | G1 | — |
| medical-family | G1 | — |
| medical-specialist | G3 / G4 | — |
| medical-wellness | G1 | — |
| restaurant-fine | G2 + G6 | — |
| restaurant-trattoria-warm | G1 | — |
| restaurant-street-modern | G5 | — |
| e-commerce-artisan | G1 + G2 | — |
| e-commerce-fashion-editorial | G6 | — |
| startup-saas-landing | G5 | — |

A new cluster's default gravity is declared at the cluster's first hardening
pass (Phase X.7a-style) AND ratified by adding a row here.

---

## §6 · Banned motion classes (cluster-wide · permanent)

These two classes are banned at archetype level for every cluster. They
override every cluster-level allow.

### USAGE-BAN-01 · Decorative motion · BANNED
- Definition: animation with no semantic purpose.
- Detector: "if removed, does the page lose any information?" If no, banned.
- Examples (non-exhaustive · the list extends but never shrinks):
  - floating shapes
  - background gradient sweeps
  - particle effects
  - cursor trails
  - light-flares
  - idle-loop video bg without purpose
  - rotating hero text "AI · Smart · Modern" carousels
  - confetti animation
  - hover-glow that pulses continuously
  - typewriter effect on hero h1 (the visitor reads the text immediately)
- **Severity**: [BLOCKING].
- **Where caught**: A.6 style-critic enumerates every motion path and cites
  the semantic purpose · any uncited path triggers a re-spec.

### USAGE-BAN-02 · Manipulative-SaaS motion · BANNED
- Definition: animation designed to override visitor judgement.
- Detector: "is the motion pushing a conversion through urgency or social
  pressure?" If yes, banned.
- Examples (non-exhaustive):
  - blinking CTAs
  - "limited time" countdowns
  - urgency badges
  - "X people are viewing this now"
  - autoplay carousels with arrows
  - popup modals that bounce in
  - exit-intent overlays
  - "don't go!" interceptors
  - scarcity timers
  - social-proof fly-ins
  - "you have unlocked an offer" notifications
  - falling-stars / shower of icons on action
  - sticky banner that grows on inactivity
- **Severity**: [BLOCKING].
- **Where caught**: A.6 style-critic + browser-verifier fire BRWS-MOTION-INV-03
  test which scrolls the page and verifies no banned pattern appears.

---

## §7 · Gating mechanism (workflow-by-workflow)

Where each rule fires in the pipeline.

### A.1 intake (planner)
- The planner declares the new sibling's `motion_profile` (G1–G6).
- The planner picks a pattern set from the catalog's cluster-row.
- The brief copies the 9-field spec for each picked pattern into the
  content-module docstring (per CS-EXEC-02 binding).
- **Gates fired**: USAGE-BAN-01, USAGE-BAN-02 (planner cannot pick a
  banned pattern) + per-pattern allow/deny rules (planner verifies cluster
  fit) + CS-MOTION-INV-10 (every animation path declares its gravity).

### A.5 build (template-builder)
- Builder wires the patterns declared in the brief.
- Each animation path carries an inline comment naming its `motion_profile`.
- Each animation has a documented duration ≤ ceiling (CS-MOTION-INV-08).
- Reduced-motion equivalent shipped per pattern (CS-MOTION-INV-01).
- **Gates fired**: CS-MOTION-INV-01, INV-04, INV-05, INV-06, INV-07, INV-08,
  INV-10.

### A.6 critique (style-critic)
- Style-critic enumerates every motion path on the rendered home + 4 key
  inner pages (about · services · cases · contact).
- For each path: cites the semantic purpose · cites the gravity declaration ·
  cites the duration · cites the reduced-motion equivalent.
- An uncited path triggers a re-spec.
- A path violating any per-pattern rule from §3 triggers a re-spec.
- A path matching USAGE-BAN-01 or USAGE-BAN-02 triggers an immediate halt.
- **Gates fired**: every rule in §2 + §3 fires here.

### Workflow C/D walk (browser-verifier)
- Browser-verifier emulates `prefers-reduced-motion: reduce` AT EVERY
  WALK · not just one walk. Verifies fallbacks fire.
- Browser-verifier scrolls past every animated section, scrolls back, and
  confirms ONE-time animation discipline (CS-MOTION-INV-05).
- Browser-verifier scrolls at high velocity and confirms no scroll-jacking
  (CS-MOTION-INV-06).
- Browser-verifier opens a carousel-pattern (if present) and confirms no
  autoplay (CS-MOTION-INV-07).
- New `BRWS-MOTION-*` rubric checks per pattern shipped on disk · added at
  Phase X.7b implementation pass.

### Release-gatekeeper (D)
- The aggregated motion-fitness score is part of the scorecard.
- A site cannot flip `tier=draft → published_live` if any [BLOCKING]
  motion rule is unresolved.

---

## §8 · § Decision triggers (escalation paths)

A § decision is required when the orchestrator wants to deviate from a
[BLOCKING] / [REQUIRED] rule. § decisions are filed in:
- `factory/standards/<cluster>-design-standard.md` (per cluster).
- `corporate-suite-distinctness-matrix.md §4` style (named near-occupant exception).

A § decision MUST include:
1. Which rule is being deviated from.
2. The cluster + sibling that deviates.
3. The semantic justification.
4. Whether the deviation is per-sibling or per-family.
5. The evidence the deviation does NOT propagate.

The orchestrator does NOT silently waive a [BLOCKING] rule. Always § decision.

Common § decision triggers:
- Invoking KPI-3 live-counter outside G5 (e.g., on a corporate-suite sibling).
  Rationale required: the cluster's institutional register is being explicitly
  re-defined, AND the live-counter has a documented backend, AND the cadence is
  ≥ 8s, AND the timestamp is present.
- Invoking MEDIA-2 parallax outside G6. Default-deny. Almost always rejected.
- Invoking EDIT-5 magazine-page-flip. Always rejected.
- Adding a new motion gravity (G7, G8, ...). Triggers a § decision at
  design-orchestrator level (not per-cluster).

---

## §9 · How a planner files a brief that uses these rules

Pseudo-template for the planner's at-A.1 brief, motion section:

```yaml
# planner brief excerpt — Motion section
new_sibling: <slug>
cluster: <cluster-name>
default_gravity: <G1..G6>  # from catalog §5

motion_profile_declared: <G1..G6>  # the actual chosen profile

pattern_set:
  - id: KPI-2
    parameters:
      duration_ms: 800
      curve: gentle-decel
    placement: home · KPI band · slot-3
    reduced_motion_equivalent: KPI-1 tabular-static
    semantic_purpose: "the count-up communicates institutional weight on viewport entry"
    cluster_fit_check: "G3 cluster · KPI-2 allowed per §3 family 1"

  - id: EVID-2
    parameters:
      tooltip_direction: above
    placement: leadership · 4-credential list
    reduced_motion_equivalent: tooltip without fade
    semantic_purpose: "credentials are verifiable on hover"
    cluster_fit_check: "G3 cluster · EVID-2 allowed"

  # ... (one entry per pattern)

excluded_patterns:
  # patterns deliberately NOT picked from the catalog's "allowed" list,
  # with reason
  - id: CASE-7
    reason: "card-reveal-inline conflicts with the 3+1 magazine-grid · LF-2 ships
              CASE-1 instead"

motion_distinctness_vs_existing_siblings:
  # how this sibling's pattern set differs from the 5 live siblings
  vs_pragma: ["+ KPI-2 (count-up)", "+ EVID-2 (chip)"]
  vs_cornice: ["+ EVID-3 (case-pop)", "+ TIME-3 (chronological)"]
  # ...
```

The brief is read at A.5 by the builder · at A.6 by the critic · at workflow C/D
by the verifier. Each step verifies its respective gates.

---

## §10 · Maintenance protocol

- Every new pattern adds a row to §3.
- Every pattern that becomes deprecated stays in §3 marked DEPRECATED with date
  + replacement pointer.
- Every cluster that ships under hardening adds a row to §5.
- Every § decision filed against a rule adds a footnote linking the decision.
- Every cluster invariant added (CS-MOTION-INV-11+) extends §2.
- BANs in §6 are monotonic — items extend, never shrink.

---

## §11 · One-paragraph summary

This rule book makes motion enforceable. 10 cluster invariants (CS-MOTION-INV-01
through 10) cover reduced-motion fallback · decorative ban · manipulative-SaaS
ban · focus-ring uniformity · one-time discipline · no-scroll-jacking · no
autoplay · duration ceilings · no page-flip · gravity declaration in source.
Per-pattern allow/deny tables in §3 cover all 48 patterns across 12 families
with explicit cluster fit and § decision triggers. End-user personalization
is constrained to discrete enums (no free numeric input), live-data backend
requires ops config, reduced-motion is automatic. Two motion classes are
permanently banned at archetype level: decorative (no semantic purpose) and
manipulative-SaaS (designed to override judgement). Each workflow stage (A.1
intake · A.5 build · A.6 critique · workflow C/D walk · release-gatekeeper)
fires its respective gates with browser-verifier rubrics added at Phase X.7b
implementation pass. § decisions are required for every deviation; silent
waivers are forbidden. The book is monotonic — patterns extend, BANs extend,
cluster invariants extend.
