# Premium dynamic pattern library

```yaml
report_type:        hardening · system-design · paper-only
date:               2026-05-05
agent:              orchestrator-side authoring (Phase X.7 hardening · post-audit)
trigger:            audit recommendation Phase X.7b — formalize motion as a first-class
                    DNA dimension and enumerate the dynamic-pattern vocabulary the factory
                    is missing
zero_code:          this pass writes paper only · no live template touched · no apps/* edited
audience:           planner · style-critic · browser-verifier · orchestrator
                    at every intake from this point forward
companion files:
  - design-orchestrator/references/internal-baselines/premium-dynamic-pattern-catalog.md
    (table-driven planner reference)
  - design-orchestrator/references/internal-baselines/dynamic-pattern-usage-rules.md
    (rule book · gating · § decision triggers)
  - factory/reports/hardening/premium-dynamic-personalization-audit.md (the diagnosis · §3 ·
    §4 · §10 gaps named here are addressed by this library)
  - factory/reports/hardening/current-template-factory-drift-map.md (concrete pattern catalog
    of what 6 corporate-suite templates already share)
  - design-orchestrator/references/internal-baselines/template-factory-capability-gap-map.md
    (capability matrix · axis 3 motion is the binding gap)
  - factory/references/pattern-library.md · factory/references/anti-pattern-library.md
    (prior pattern records · E2 · E3 · AP12 · this library extends them)
inputs_consumed:
  - factory/standards/corporate-suite-{design-standard,blocking-rules,browser-rubric,
    imagery-standard,multi-agent-sop,quality-scorecard}.md (cluster-level rule book)
  - design-orchestrator/references/internal-baselines/corporate-suite-{distinctness-matrix,
    reference-pack,layout-family-assignment,live-family-map}.md
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md
  - design-orchestrator/references/skillui-extracts/{pragma,fiscus,solaria}/127-design/*.md
    (motion guidance from skillui design extracts · §7 Animation & Motion)
  - apps/catalog/template_dna.py · TONES dict + CONVERSION_PATTERNS + LAYOUT_ARCHETYPES
verdict:            12 pattern families · 48 named pattern variants · 6 motion gravities ·
                    every pattern has 9-field spec · every cluster has a recommended
                    pattern set · every pattern has a reduced-motion equivalent · zero new
                    DNA dimensions invented mid-pass — `motion_profile` is the only new
                    dimension and it lands at Phase X.7b implementation pass
```

## §0 · Why this library exists

The audit (`premium-dynamic-personalization-audit.md`) named the gap:
- **Gap #1** "one tonal grammar across all 6 latest templates" — partially structural.
- **Gap #2** "one motion vocabulary" — directly the user's "not dynamic enough" signal.
- **Gap #3** "one CTA inflection" — overlaps the motion gap (CTA-feedback IS motion).

This library answers Gap #2 in full and unblocks the dynamic-feel half of Gap #1. It
does not invent motion abstract; it *names* what is already encoded (in `apps/catalog/
template_dna.py` HERO_STYLES + NAVBAR_STYLES + CARD_STYLES + BUTTON_STYLES) but never
formalised into rule, plus what is on disk in skillui-extracts (`expressive motion ·
spring physics · staggered reveals · 150-300ms micro-interactions · 300-500ms page
transitions · always respect prefers-reduced-motion`) but never wired.

Every pattern below is **on-paper**. Implementation work is Phase X.7b · separate brief.

The library is **monotonic**. New patterns are added; existing ones are refined; no
pattern is silently removed. A pattern marked as deprecated stays in the catalog as
a deprecated reference so future planners can read why it was deprecated.

---

## §1 · Six motion gravities (the register axis)

Every pattern in this library belongs to **exactly one** of six motion gravities. The
gravity is the contract — what the motion is doing semantically — not the duration or
the easing. Gravities can be mixed within a single template only when explicitly
declared by family.

### G1 · Safe premium motion · cluster-default
**What it does**: every animation has a documented purpose (reveal · feedback ·
narrative). Tabular numerals on KPIs. Hairline-on-hover. 600ms ease-out fade-ins
on first viewport intersection. `prefers-reduced-motion` honoured globally. No
parallax. No scroll-snap. No live-data. No autoplay.
**Tone read**: "This site is alive but composed."
**Cluster fit**: corporate-suite (LF-1 · LF-3 · LF-4 default), lawyer-classic-gold,
medical-clinic, medical-family.
**Cluster no-fit**: agency-digital-studio, startup-saas-landing, portfolio-cinematic
(too restrained for those audiences).

### G2 · Editorial motion · LF-2 default
**What it does**: magazine-spread feel. Slow narrative reveals. Drop-cap appears
first, paragraph fades around it. Pull-quote staggers. Sticky 4-link side-rail.
NO parallax (too cinematic for editorial). NO scroll-snap (too app-like).
NO live-data (too tech-y).
**Tone read**: "This is a publication, not a website."
**Cluster fit**: corporate-suite LF-2 (Cornice · Causa), agency-creative-studio,
restaurant-fine, real-estate-ultra-luxury.
**Cluster no-fit**: corporate-suite LF-1 / LF-3 / LF-4 (tonally wrong),
medical-clinic, e-commerce, startup-saas.

### G3 · Institutional motion · gravitas-end
**What it does**: motion = essential reveal only. KPIs animate ONCE per session
(count-up acceptable). Ledgers reveal as user scrolls past. NO tickers. NO
marquees beyond the documented sectors-association marquee at 110s. NO
live-data. NEVER autoplay. Hover affordances are hairline-only (NO lift, NO
tilt, NO accent-glow on body content — the gold focus ring is the only
glow-class element).
**Tone read**: "Every animation is paid for by a clear semantic purpose. Nothing
is decorative."
**Cluster fit**: corporate-suite Pragma (LF-1) · Fiscus (LF-3) · Causa (LF-2 with
forensic register adjustments), lawyer-classic-gold, family-office.
**Cluster no-fit**: portfolio, e-commerce, restaurant-street, startup-saas.

### G4 · High-trust professional motion · stewardship-restrained
**What it does**: Continua / Cassazione / family-office register. Motion =
institutional-restraint **plus exactly one editorial cue** (e.g., voice-anchor
recurrence, governance-cycle dot animation on slot-2). NO icon animation. NO
emoji. NO confetti. NO hover-lift on portrait cards. **Reduced from G3 by one
notch on every parameter.**
**Tone read**: "This firm holds something across time. Nothing is flashing."
**Cluster fit**: corporate-suite LF-5 (Continua), lawyer-classic-gold (heavier
forensic register), medical-specialist (Cassazione-grade clinical authority).
**Cluster no-fit**: any cluster whose audience verb is "explore", "ship", "buy",
"play", "watch".

### G5 · Sprint-console motion · digital-product
**What it does**: live-data feel. Ticker chips with real (or simulated) numbers
that update on a slow cadence (every 8-12s, NOT every 1s — that reads slot-
machine). Scroll-progress bar at top of viewport (1px hairline accent).
Sprint-chip showing "current sprint" status. Snap-fold scroll on hero (the
single legitimate scroll-snap gravity). Glow-pill CTAs with subtle drop-glow.
Card hover = 2px lift + 8% accent-glow.
**Tone read**: "This product ships. Things are in motion."
**Cluster fit**: agency-digital-studio (Aura), startup-saas-landing,
lawyer-modern-transparent (light-touch borrowing only).
**Cluster no-fit**: corporate-suite, lawyer-classic-gold, medical-specialist,
real-estate-ultra-luxury.

### G6 · Gallery-cinematic motion · photography & luxury
**What it does**: slow fade transitions. Scroll-snap on horizontal hero strips.
Cinematic Ken Burns drift on full-bleed photos (max 1.05x scale at 8s · NEVER
faster). Lightbox preserves scroll position. Cursor vignette in dark hero.
NO live-data. NO sprint-style chips. NO blink. NO glow-on-CTA.
**Tone read**: "This site is a slow film."
**Cluster fit**: portfolio-cinematic, real-estate-ultra-luxury, agency-creative-
studio (lighter touch · Vertex), restaurant-fine (course-indexed reveal),
e-commerce-fashion-editorial.
**Cluster no-fit**: corporate-suite, medical-clinic, lawyer-classic-gold,
startup-saas.

### Gravities deliberately NOT defined (banned)

**Decorative motion**: floating shapes, background gradient sweeps, particle
effects, cursor trails, light-flares, idle-loop video backgrounds, rotating
hero text "AI · Smart · Modern" carousels. **BAN at archetype level for the
entire factory.** No cluster, family, or sibling may invoke a decorative
gravity. The detector test: "if removed, does the page lose any information?"
If no, the motion is decorative.

**Manipulative SaaS motion**: blinking CTAs, "limited time" countdowns,
urgency badges, "X people are viewing this now" notifications, autoplay
carousels with arrows, popup modals that bounce in, exit-intent overlays,
"don't go!" stay-on-page interceptors, scarcity timers, social-proof
fly-ins. **BAN at archetype level for the entire factory.** Detector: "is
the motion designed to override visitor judgement?" If yes, it is manipulative.

These two banned classes are written into the rule book (`dynamic-pattern-usage-
rules.md §6`) as `[BLOCKING]` red lines. Every cluster's design standard inherits
them.

---

## §2 · Pattern families and named variants

Twelve families. 48 named patterns. Each pattern has:
- **name** · stable identifier · used in DNA `motion_profile.<pattern_id>`
- **gravity** · which of G1–G6
- **use case** · what the visitor reads
- **visual behavior** · what literally moves
- **interaction behavior** · what the visitor does
- **premium failure modes** · how this becomes "tacky"
- **anti-tacky rules** · the bright lines
- **personalization knobs** · what end-users configure
- **cluster fit / no-fit** · where it belongs · where it is banned
- **anti-clone notes** · how it differs from sibling patterns

---

## §2.1 · Family 1 · KPI / count-up systems

The "numerical proof" surface. Every premium template has at least one. The
question is *how the number arrives*.

### KPI-1 · `tabular-static` · CURRENT CORPORATE-SUITE DEFAULT
- **Gravity**: G1 (institutional default · safe premium).
- **Use case**: a KPI tuple in a hero meta-strip or dark band — "180+ mandates · 22
  anni · €1.4 B · 94%". The number is its own argument.
- **Visual behavior**: numbers sit there. `font-variant-numeric: tabular-nums`
  guarantees alignment. NO motion. The italic-em on the unit ("anni" · "mandates")
  is the only typographic accent.
- **Interaction behavior**: none. The number is read.
- **Premium failure modes**: numbers without tabular-nums shift across locales
  (RTL especially) · the eye reads "broken" · CS-TYPE-03 catches.
- **Anti-tacky rules**: NO drop-shadow on the number. NO bold weight. NO accent
  color on the digits (accent on unit/label is fine). NO outline.
- **Personalization knobs**: end-user can edit the figure value, the unit label,
  the order of cells; cannot change the visual treatment.
- **Cluster fit**: corporate-suite (all LFs), lawyer-classic-gold, medical-
  specialist, family-office, audit-led methodology. Default for institutional.
- **Cluster no-fit**: nowhere — this is the safe baseline. Even when a richer
  KPI variant is shipped, this is the reduced-motion fallback.
- **Anti-clone**: **the differentiator is the cell composition**, not the
  motion. Pragma's `(HQ · Equipe · Mandati)` ≠ Causa's `(28 sentenze · 14 voci ·
  31 anni)`. Same motion, different content.

### KPI-2 · `count-up-on-view`
- **Gravity**: G1 (institutional · with a single editorial cue) OR G3 (when the
  count-up is the only motion on the page).
- **Use case**: KPI band animates from 0 to target value when the band first
  enters viewport. "47 → 180+" over 800ms ease-out. Plays ONCE per session.
- **Visual behavior**: numbers tick from 0 to target with `requestAnimationFrame`
  loop. Easing: `cubic-bezier(0.16, 1, 0.3, 1)` (gentle deceleration). Duration:
  600-900ms (NEVER under 400ms — too fast reads slot-machine; NEVER over 1500ms
  — too slow reads loading).
- **Interaction behavior**: triggered by `IntersectionObserver` at 60% visibility.
  No re-trigger on scroll-back (anti-fatigue rule).
- **Premium failure modes**: count-up that runs every time the band enters viewport
  (reads slot-machine); count-up over too-large numbers like 1000000 with no
  comma formatter (reads gibberish ticking); count-up with sparkle animation on
  arrival (reads gameshow).
- **Anti-tacky rules**: ONE-TIME per session (use sessionStorage). MAX duration
  900ms. NO comma-by-comma reveal of digits. NO color flash on completion. The
  arrival is silent — the visitor sees the final number and moves on.
- **Personalization knobs**: on/off toggle (default on for G1+G3 clusters · off
  for G4 · NEVER available for G6); duration (600 · 800 · 900ms); ease curve
  (only `gentle-decel` or `linear`, no springs, no bounces).
- **Cluster fit**: corporate-suite (all LFs · single explicit invocation per
  home · always at the cluster's existing KPI placement), agency-digital-studio
  (extends to live-update post-arrival per KPI-3), startup-saas-landing.
- **Cluster no-fit**: G4 stewardship (Continua), G6 cinematic (portfolio · luxury),
  family-office (the longitudinal register prefers stillness).
- **Anti-clone**: Pragma's count-up animates the 4 cells of the dark KPI band at
  slot-3. Cornice would NOT use count-up because LF-2 promotes KPI to hero overlay
  and the editorial register prefers tabular-static. Causa SHOULD adopt count-up
  on its KPI overlay if and only if the orchestrator authorises the editorial
  cue per A.6b.

### KPI-3 · `live-counter`
- **Gravity**: G5 (sprint-console only). Banned in G1/G2/G3/G4/G6.
- **Use case**: a KPI cell shows a number that updates on a slow cadence. "1,247
  active mandates · updated 14m ago". Real backend feed OR simulated cadence with
  a documented seed.
- **Visual behavior**: number ticks by ±1 with a 200ms ease-out micro-transition
  every 8-12 seconds (NEVER less than 8s · NEVER more than 30s · the in-between
  is the legibility zone). A timestamp updates with the number ("12s ago · 28s
  ago · 1m ago").
- **Interaction behavior**: visitor reads, optionally clicks the timestamp to
  refresh.
- **Premium failure modes**: ticks every second (reads stock-ticker); shows
  artificially large numbers without provenance (reads vanity); doesn't actually
  pull live data and is just a JS counter (reads dishonest).
- **Anti-tacky rules**: cadence ≥ 8s. Timestamp must be present. Number must
  have a documented data source visible on hover ("Source: internal mandate
  registry · cached 14m"). NO red/green up/down indicators (reads stock-app).
  NO sparklines on a single live-counter cell.
- **Personalization knobs**: data source URL (defaults to `/api/v1/live-kpi/`),
  cadence (8 / 12 / 30s), display number format (raw · k-suffix · M-suffix), show
  timestamp (default on). Can be disabled entirely; defaults to disabled in
  most clusters and enabled only in G5 sprint-console.
- **Cluster fit**: agency-digital-studio (sprint chip · live deploys), startup-
  saas-landing (live MAU · uptime · build status). Allowed only with consent
  for any data backed by user analytics.
- **Cluster no-fit**: every G1/G2/G3/G4/G6 cluster. Specifically **never in
  corporate-suite** — the boardroom-advisory register is defeated by live tickers.
- **Anti-clone**: Aura digital-studio's `shiplog-console` is the single live-
  counter shape that ships at hardening parity (when it ships). A 2nd
  digital-studio sibling cannot ship a 2nd live-counter as their "differentiator
  move" — they pick a different family.

### KPI-4 · `range-fill`
- **Gravity**: G1 with optional G3 reduction (reduce duration or fill speed).
- **Use case**: KPI is a hairline horizontal bar that fills from 0 to its end-state
  width. "94% client retention · ████████████░ ".
- **Visual behavior**: 1px hairline track + accent-color fill that transitions
  from `width: 0` to target via `transform: scaleX(1)` over 800-1200ms ease-out.
  The numeric value can either count-up alongside (combining KPI-2 + KPI-4) OR
  appear at the end of the fill (anti-tacky rule: pick one, never both
  simultaneously).
- **Interaction behavior**: triggered by IntersectionObserver. ONE-time per
  session.
- **Premium failure modes**: bar fills with a glow trail (reads videogame); bar
  fills past 100% (reads broken); multiple bars race each other on same row
  (reads competition); bar has gradient fill (reads infographic).
- **Anti-tacky rules**: SINGLE accent-color fill. NO gradient. NO percent
  marker that sweeps along. Track is a hairline (1px) NOT a track-with-shadow.
  Fill duration matches count-up if both fire on same band (else pick the
  longer one — bar leads).
- **Personalization knobs**: on/off (default on for fiscal/audit/methodology
  contexts; default off for editorial/cinematic); fill duration (600 · 900 ·
  1200ms); show numeric label after fill (default yes).
- **Cluster fit**: lawyer-modern-transparent (case-success rate),
  audit-led methodology (audit-coverage rate · NOT YET shipped at hardening),
  fiscal-clinic (compliance rate). All G1.
- **Cluster no-fit**: G2 editorial (Cornice/Causa: bars feel infographic-tacky
  in a publication register); G6 cinematic (no horizontal-fill mechanics in a
  cinematic register).
- **Anti-clone**: range-fill is the only KPI variant that introduces a *visual*
  for the number. A new sibling can pick range-fill if their CTA mental model
  is "audit-coverage" or "completion-rate" — semantic justification required.

### KPI-5 · `comparative-tick`
- **Gravity**: G1 (with discipline) OR G5 (with permission).
- **Use case**: KPI shows a value AND its delta vs benchmark. "180+ mandates ·
  ↑ 12 vs 2024".
- **Visual behavior**: the delta arrow + small number animate in *after* the
  main value, with a 200ms delay. Static after arrival.
- **Interaction behavior**: hovering the delta reveals the benchmark source
  on a hairline tooltip ("Industry avg: 168 · ICCRI 2025 report").
- **Premium failure modes**: green/red color coding without a documented
  benchmark (reads investor-deck); delta number that shifts as you watch
  (reads stock-app); arrow that rotates (reads spinner).
- **Anti-tacky rules**: benchmark source MUST be cited on hover. NO color
  coding (the arrow direction is enough · ↑ for up · ↓ for down). NO
  background fill on the delta cell. Static after arrival.
- **Personalization knobs**: show/hide delta (default off if no benchmark
  source); benchmark source URL or text; delta number format.
- **Cluster fit**: lawyer-modern-transparent (vs prior year), agency-digital-
  studio (vs sprint baseline), startup-saas (vs cohort).
- **Cluster no-fit**: G2 editorial (no benchmark register), G3 institutional
  (Pragma's "180+ mandates" doesn't need a comparator — comparators read
  marketing).
- **Anti-clone**: each sibling that picks comparative-tick claims a benchmark
  source no other sibling cites.

---

## §2.2 · Family 2 · Timeline / progression systems

Time as proof. Stewardship · longitudinal practice · case-bundle history.

### TIME-1 · `static-vertical-timeline` · CURRENT LF-5 SHIPPED
- **Gravity**: G4 (stewardship-restrained · current Continua shape).
- **Use case**: vertical column with 3-7 timeline entries (year + mandate + horizon).
  Renders as a static list of entries with hairline dividers.
- **Visual behavior**: no motion. The visual hierarchy carries the meaning
  (year column · entry column · horizon column).
- **Interaction behavior**: read-only.
- **Premium failure modes**: too-many entries (>7) read as resume; sparse year-
  values with big gaps read as half-built; no horizon column reads as pure
  history.
- **Anti-tacky rules**: 3-7 entries. Each entry MUST carry the (year · what ·
  horizon) triple. NO illustration of "branches" between entries. NO
  parenthetical clients.
- **Personalization knobs**: end-user edits entries; can toggle horizon column
  visibility; cannot change the linear vertical shape.
- **Cluster fit**: corporate-suite LF-5 (Continua canonical), family-office,
  audit-led methodology, conservation-studio (vincolo-timeline).
- **Cluster no-fit**: agency, e-commerce, restaurant.
- **Anti-clone**: Continua claims `(year · mandate · horizon)`. A 2nd LF-5
  occupant must pick a different triple — `(year · vincolo · Soprintendenza)`,
  `(year · audit · finding)`, `(year · case · ruling)`.

### TIME-2 · `scroll-driven-timeline`
- **Gravity**: G2 (editorial) OR G4 (stewardship-restrained).
- **Use case**: a sticky timeline header (left rail) where each entry's body
  appears in the main column as the visitor scrolls past. Subtle progress dot
  on the rail tracks position.
- **Visual behavior**: rail has a vertical 1px hairline + 4-8 dots. The active
  dot is filled with accent. As the visitor scrolls, the active dot
  transitions (200ms) to the next entry's dot. Body content fades in
  (600ms · 80ms stagger between siblings) as it enters viewport.
- **Interaction behavior**: clicking a rail dot scrolls to that entry's body
  (smooth scroll · `behavior: 'smooth'`). Keyboard arrow keys move between dots.
- **Premium failure modes**: scroll-jacking (the page scroll is hijacked to
  enforce a per-step pause — banned at archetype level); dots that bounce on
  arrival (G3+ ban); rail that overlaps body content on narrow viewports.
- **Anti-tacky rules**: NO scroll-jacking. NO bounces. The rail collapses below
  880px to a horizontal stripe at the top of each entry. Smooth scroll is
  optional and disabled if `prefers-reduced-motion` is on. The active dot is
  filled with accent — NEVER glowing or pulsing.
- **Personalization knobs**: number of entries; dot count must match; show/hide
  rail body labels; smooth-scroll behavior on/off (default on if reduced-motion
  off).
- **Cluster fit**: corporate-suite LF-5 (extension of Continua's static
  timeline), audit-led methodology, agency-creative-studio (selected-work
  chronology), real-estate concierge (property-history-chronology).
- **Cluster no-fit**: G3 institutional (Pragma · Fiscus): too active for boardroom
  register; G6 cinematic at hero (timeline pollutes cinematic stillness).
- **Anti-clone**: scroll-driven-timeline is positioned as a 2nd-occupant move
  for LF-5. The 1st occupant (Continua) ships static. A 2nd LF-5 occupant
  inherits the L7=timeline cell shape and differentiates inside the cell with
  scroll-driven motion.

### TIME-3 · `chronological-tick-horizontal`
- **Gravity**: G2 (editorial) — magazine-spread reading.
- **Use case**: horizontal timeline strip on a single section. Each entry is
  a tick on the line, with a small year label below and a heading above.
  Reveals as the strip enters viewport.
- **Visual behavior**: the line itself draws from left to right (1px accent)
  on first viewport entry, over 1200ms ease-out. Tick marks appear in sequence
  (80ms stagger) AS the line crosses them. Heading + year fade in after the
  tick is in place (200ms delay).
- **Interaction behavior**: hovering a tick brings up a hairline tooltip
  with the entry detail. Clicking opens a modal lightbox-style detail.
- **Premium failure modes**: line that draws too fast (reads cartoon); ticks
  that pop in with bounce (G3+ ban); modal that takes over screen (use
  inline reveal instead).
- **Anti-tacky rules**: line draws over 1200ms minimum. ONE-time on first
  view. Reduced-motion: line is fully drawn statically at first paint.
- **Personalization knobs**: tick count (4-8); year format (`2024` vs `2024.06`
  vs `Q1 2024`); show/hide tooltip on hover; modal vs inline detail.
- **Cluster fit**: corporate-suite LF-2 (a 2nd-occupant move), agency-creative-
  studio (selected-work index by year), restaurant-fine (course-indexed
  chronology).
- **Cluster no-fit**: G3 (Pragma · Fiscus · Causa institutional reading),
  G5 sprint-console.
- **Anti-clone**: horizontal tick is the editorial-magazine alternative to LF-5's
  vertical timeline. The shapes are DIFFERENT axes — one cluster cannot ship
  both.

### TIME-4 · `stewardship-rings-concentric`
- **Gravity**: G4 (stewardship-restrained · Continua-class).
- **Use case**: 3-4 concentric rings representing time horizons. Each ring is a
  custodial mandate (annual · multi-annual · generational). Reveals on scroll.
  Specifically for family-office / stewardship / fiduciary / longitudinal-care.
- **Visual behavior**: rings draw outward (innermost first) on viewport entry,
  300ms each, 100ms stagger. After all rings are drawn, the labels fade in
  (200ms each).
- **Interaction behavior**: hover a ring to highlight its label and dim the
  others (200ms transition · 0.4 opacity for non-active rings).
- **Premium failure modes**: rings that pulse continuously (reads
  meditation-app); rings that rotate (reads logo-loader); too-many rings
  (>4 reads pie-chart).
- **Anti-tacky rules**: 3-4 rings maximum. NO continuous pulse. NO rotation.
  NO gradient on rings. Reduced-motion: all rings are drawn statically at
  first paint.
- **Personalization knobs**: ring count (3 · 4); ring labels; ring colors
  (must be derived from palette tokens, no fourth color); accent intensity.
- **Cluster fit**: corporate-suite LF-5 (Continua-shaped · could be a 2nd-
  occupant move), family-office, fiduciary-stewardship.
- **Cluster no-fit**: anywhere not stewardship.
- **Anti-clone**: rings are the cluster's only "geometric proof shape" allowed.
  No other family may invoke them (the LF-2 editorial reading rejects geometric
  visuals).

### TIME-5 · `chapter-stepper-magazine`
- **Gravity**: G2 (editorial) · G6 (cinematic with discipline).
- **Use case**: long-form narrative with numbered chapters. As visitor scrolls
  past each chapter, a sticky chapter indicator updates ("Chapter 3 of 7").
  Magazine-spread feel.
- **Visual behavior**: sticky indicator at top of viewport (or bottom). Chapter
  number increments with a 200ms cross-fade transition (not a tick · a fade).
- **Interaction behavior**: clicking the indicator opens a TOC overlay with
  chapter titles. Esc closes.
- **Premium failure modes**: indicator that pulses to draw attention (G3+ ban);
  TOC that takes over screen (use a side-rail or top-overlay, not full-screen);
  chapter numbers in a spinner that flips (reads dashboard).
- **Anti-tacky rules**: cross-fade only. NO flip. TOC is dismissible with
  click-outside AND Esc. NO progress percentage in the indicator (the chapter
  count is enough).
- **Personalization knobs**: chapter count (3-12); chapter titles; TOC
  position (top vs side); show/hide chapter cross-fade.
- **Cluster fit**: corporate-suite LF-2 (Cornice · Causa · narrative essay
  extension), agency-creative-studio (manifesto chapters), restaurant-fine
  (course-indexed reading).
- **Cluster no-fit**: G3 institutional, G5 sprint, G6 photography (the
  cinematic read prefers no chapter chrome).
- **Anti-clone**: Cornice's narrative essay currently has 3 pull-quotes + sticky
  4-link side-rail. Chapter-stepper is the natural extension when the narrative
  exceeds ~7 paragraphs. The 2nd LF-2 occupant can pick chapter-stepper if their
  narrative is longer; Cornice retains the simpler side-rail.

---

## §2.3 · Family 3 · Evidence/proof reveal systems

Surfacing the receipts. Critical for high-trust professional clusters.

### EVID-1 · `progressive-disclosure-tap`
- **Gravity**: G1 (institutional default) · G3 (gravity-end).
- **Use case**: a claim is shown with a "expand for citation" affordance. Tapping
  the claim reveals the full evidence inline.
- **Visual behavior**: claim shows with a small "+ citation" hairline link.
  Tap → the citation slides down (250ms ease-out · max 200px tall) below the
  claim · "+" rotates to "−" (180° · 200ms). Tap again → citation slides up.
- **Interaction behavior**: keyboard accessible (`role="button"` · `aria-expanded`).
  Multiple disclosures can be open at once on one page.
- **Premium failure modes**: disclosure that bounces open (G3+ ban); citation
  rendered in a popup tooltip (read tone-deaf); "+" that rotates to "X" (reads
  modal-close, not toggle).
- **Anti-tacky rules**: slide animation MAX 250ms. NO bounce. NO opacity flicker.
  Citation text renders in the same typography as body. NO red/yellow highlight
  on the claim itself.
- **Personalization knobs**: claim text; citation text; default-state (collapsed
  vs expanded); icon character ("+" / "▾" / "▸" / "→").
- **Cluster fit**: corporate-suite (Pragma · Cornice · Causa · Fiscus all benefit
  · evidence-led legal especially), lawyer-classic-gold, audit-led methodology,
  family-office (governance-citation).
- **Cluster no-fit**: e-commerce (no claims to cite), agency-digital-studio (the
  shiplog itself is the evidence), restaurant.
- **Anti-clone**: each sibling claims a different KIND of citation —
  Pragma cites internal mandates, Causa cites Cassazione sentences, Fiscus cites
  ODCEC iscrizione. Same pattern, different evidence class.

### EVID-2 · `attestation-chip-hover`
- **Gravity**: G1 / G3.
- **Use case**: a credential or albo number is shown as a small chip. Hover or
  focus reveals the full citation in a hairline tooltip.
- **Visual behavior**: chip has a hairline border. On hover, a small tooltip
  fades in (200ms · 8px above the chip) with the full citation. Tooltip has
  a 4px arrow pointing back to the chip.
- **Interaction behavior**: hover or focus shows tooltip; click opens an
  external link (e.g., Albo Avvocati registry).
- **Premium failure modes**: tooltip with a drop-shadow (reads marketing);
  tooltip that doesn't dismiss on blur (annoying); chip with a glow (reads
  notification badge).
- **Anti-tacky rules**: tooltip is 1 line, 2 max. NO drop-shadow. NO glow on
  chip. Tooltip MUST dismiss on `mouseleave` AND blur. Reduced-motion: tooltip
  is shown without fade transition.
- **Personalization knobs**: chip text; tooltip text; link URL; tooltip
  direction (above · below · left · right); chip variant (hairline · filled ·
  ghost).
- **Cluster fit**: every cluster with verifiable credentials — corporate-suite
  (all LFs), lawyer-classic-gold, lawyer-modern-transparent, medical-clinic,
  medical-specialist, real-estate (broker license).
- **Cluster no-fit**: e-commerce, restaurant, portfolio (these have NO
  formal credentials to cite typically).
- **Anti-clone**: chip text format is sibling-distinct (Pragma's
  `(Direzione, Anno fondazione)` ≠ Causa's `(Albo, Numero iscrizione)`).

### EVID-3 · `case-citation-pop`
- **Gravity**: G3 institutional · forensic.
- **Use case**: a case-card on the cases-preview shows a sentence number ("Cass.
  SS.UU. 12345/2024"). Click reveals the actual citation snippet inline.
- **Visual behavior**: card expands inline (NOT a modal · NOT a route change)
  · 350ms ease-out · max-height transition. Inside the expanded area, the
  citation text fades in (200ms delay). Click again or click-outside collapses.
- **Interaction behavior**: keyboard `Enter` / `Space` toggles. Esc collapses.
  Multiple cards can be expanded.
- **Premium failure modes**: card that opens a modal taking over screen (the
  inline expansion is the editorial register); card that flies in from
  off-screen (reads slot-machine); citation rendered in monospace (reads
  developer-doc unless it actually IS a code citation).
- **Anti-tacky rules**: inline expansion only. Citation typography matches body.
  Click-outside collapses. Reduced-motion: card is statically expanded with
  a "collapse" link, no transition.
- **Personalization knobs**: max expanded height; default state; show/hide
  external link to full sentence; citation source label.
- **Cluster fit**: corporate-suite Causa (forensic-publication register),
  lawyer-classic-gold (forensic case-law citation), audit-led methodology
  (audit-finding citation).
- **Cluster no-fit**: every non-forensic cluster.
- **Anti-clone**: Causa is the canonical first occupant. A 2nd forensic-cluster
  sibling cannot ship the same shape; they pick `EVID-1` progressive-disclosure
  inline-expansion instead.

### EVID-4 · `audit-trail-arrow`
- **Gravity**: G1 / G3 / G4.
- **Use case**: each KPI or claim has a small subtle arrow icon next to it. The
  arrow links to the audit reference (a method-page · a publications page · a
  citation list).
- **Visual behavior**: arrow is a 12px serif chevron in accent color. On hover,
  it shifts 2px right (200ms ease-out). NO pulse. NO grow.
- **Interaction behavior**: click navigates to the audit reference page.
- **Premium failure modes**: arrow that bounces (G3+ ban); arrow that grows on
  hover (reads tooltip-tease); arrow with a `target="_blank"` icon (read SaaS
  shopping-cart).
- **Anti-tacky rules**: 2px shift maximum on hover. NO bounce. NO grow. NO icon
  change. The reference page is on the SAME domain (no external popup unless
  it's a regulatory body like Cassazione).
- **Personalization knobs**: target href; arrow style (serif chevron · sans
  arrow · ghost); enable/disable.
- **Cluster fit**: any cluster with audit references — corporate-suite (all
  LFs), lawyer (both), audit-led methodology, family-office.
- **Cluster no-fit**: e-commerce, restaurant, portfolio.
- **Anti-clone**: target page is sibling-specific. Multiple siblings can use
  the arrow shape; the destination differs.

### EVID-5 · `provenance-tooltip-image`
- **Gravity**: G1 / G2 (editorial).
- **Use case**: hovering a hero or feature photo reveals a hairline overlay
  with photographer + license + date.
- **Visual behavior**: overlay slides in from the bottom-right corner of the
  photo (200ms · ease-out). Overlay is a hairline-bordered cream paper card
  with 12px serif text inside.
- **Interaction behavior**: hover only · keyboard `focus` on the photo (with a
  visible focus ring) shows the same overlay.
- **Premium failure modes**: overlay that takes over the photo (reads watermark);
  overlay that animates with a "glint" (reads marketplace); overlay that
  appears immediately on viewport-load (the photo is the photo).
- **Anti-tacky rules**: overlay is small (≤ 240px wide). Hover only. The
  visitor must opt-in by hover. NO permanent watermark.
- **Personalization knobs**: photographer credit; license; date; overlay
  position (bottom-right · bottom-left · top-right); enable/disable per slot.
- **Cluster fit**: corporate-suite LF-2 / LF-5 (editorial register · Cornice ·
  Continua already use editorial photography), agency-creative-studio
  (colophon-press), portfolio-cinematic (the EXIF row is the canonical
  expression of this).
- **Cluster no-fit**: every cluster that uses stock without credit.
- **Anti-clone**: each sibling cites a different photographer. The overlay
  shape can be reused; the credit content cannot.

---

## §2.4 · Family 4 · Media block systems

How photos / video / illustration carry weight on the page.

### MEDIA-1 · `cinematic-fade-on-view`
- **Gravity**: G6 (cinematic).
- **Use case**: a full-bleed photo enters viewport with a slow fade from
  initial-state (slightly desaturated · slightly scaled) to full-state (full
  saturation · 1.0 scale).
- **Visual behavior**: photo starts at `opacity: 0.7 · saturate(0.85) · scale(1.04)`
  and transitions over 1200-1800ms ease-out to `opacity: 1 · saturate(1) ·
  scale(1)`.
- **Interaction behavior**: triggered on viewport entry. ONE-time per session.
- **Premium failure modes**: fade in over <600ms (reads consumer-app);
  saturation that overshoots (reads filter); scale that overshoots above 1.05
  (reads zoom).
- **Anti-tacky rules**: duration ≥ 1200ms. Saturation start ≥ 0.85. Scale
  start ≤ 1.05. Reduced-motion: photo is fully revealed at first paint.
- **Personalization knobs**: duration (1200 · 1500 · 1800ms); saturation
  start (0.85 · 0.9); scale start (1.0 — opt out · 1.02 · 1.04).
- **Cluster fit**: portfolio-cinematic, real-estate-ultra-luxury, agency-
  creative-studio (Vertex hero), restaurant-fine (course-image arrival),
  e-commerce-fashion-editorial.
- **Cluster no-fit**: corporate-suite (all LFs · the editorial register
  prefers a static hero), lawyer-classic-gold, medical-clinic.
- **Anti-clone**: each cluster's hero subject is different (per drift-map §1)
  · the fade behavior can be shared because the subject content makes them
  distinct.

### MEDIA-2 · `parallax-restrained-hero`
- **Gravity**: G6 (cinematic) · NEVER G1/G2/G3/G4.
- **Use case**: hero photo has a 0.85x parallax offset on scroll — the photo
  scrolls slower than the page, giving a depth cue.
- **Visual behavior**: photo `transform: translateY(scrollY * -0.15)` clamped
  to the hero section's height. NEVER full-page parallax (only hero section).
  Layer count: 1 (the photo). NEVER 6-layer parallax.
- **Interaction behavior**: parallax is tied to scroll position. ONLY active
  in the hero section.
- **Premium failure modes**: parallax outside the hero (reads marketing-template);
  multi-layer parallax (reads gimmicky); parallax that exposes the bottom
  edge of the photo (reads broken layout); parallax-on-mobile (reads janky).
- **Anti-tacky rules**: hero only. Single layer. Disabled below 880px viewport.
  Disabled when reduced-motion is on.
- **Personalization knobs**: offset multiplier (0.10 · 0.15 · 0.20); hero
  enable/disable; mobile fallback (always disabled).
- **Cluster fit**: portfolio-cinematic (Pixel), real-estate-ultra-luxury,
  agency-creative-studio (only for hero · NEVER body sections).
- **Cluster no-fit**: every non-G6 cluster. Specifically banned in corporate-
  suite (the editorial register rejects parallax · Cornice walked clean
  without it · Continua walked clean without it · ratified at A.6).
- **Anti-clone**: only G6 clusters use this; sibling distinction comes from
  hero subject, not parallax behavior.

### MEDIA-3 · `image-grid-stagger-reveal`
- **Gravity**: G2 (editorial) / G6 (cinematic).
- **Use case**: a grid of N (3-12) images. As the grid enters viewport, images
  fade in with stagger (60-100ms between siblings).
- **Visual behavior**: each image starts at `opacity: 0 · translateY(8px)` and
  transitions to `opacity: 1 · translateY(0)` over 500ms ease-out. Stagger
  between siblings: 60-100ms (G2 = 60ms · G6 = 100ms).
- **Interaction behavior**: triggered by grid container's IntersectionObserver
  at 30% visibility. Stagger order: row-major reading order.
- **Premium failure modes**: stagger that takes >2 seconds to complete (reads
  loading); images that flip in (reads photo-album); images that scale up
  (reads zoom-in).
- **Anti-tacky rules**: stagger total ≤ 1500ms. NO scale. NO flip. NO
  blur-to-sharp. Reduced-motion: images are statically revealed.
- **Personalization knobs**: stagger duration (60 · 80 · 100ms); per-image
  duration (400 · 500 · 600ms); enable/disable; reverse order toggle.
- **Cluster fit**: agency-creative-studio (selected-work grid), portfolio
  (both archetypes), e-commerce (product grid · with reduced velocity for
  trust register), restaurant (course-grid).
- **Cluster no-fit**: corporate-suite (the magazine-grid 3+1 in LF-2 is a
  fixed-shape composition · stagger pollutes the editorial reveal), lawyer.
- **Anti-clone**: image content is sibling-distinct. The stagger duration is
  family-distinct (G2 = quick · G6 = slow).

### MEDIA-4 · `before-after-drag-slider`
- **Gravity**: G1 (with discipline · institutional) / G6 (cinematic).
- **Use case**: two photos shown overlapping, with a vertical drag handle at
  the midpoint. Visitor drags the handle to compare. Restoration · health ·
  coaching · before/after.
- **Visual behavior**: handle is a 1px hairline + 24px circle thumb. Drag
  gesture moves the clip-path of the foreground photo to reveal more or less
  of the background. Initial state: handle at 50%. NO auto-animation on
  arrival.
- **Interaction behavior**: mouse drag · touch drag · keyboard arrow keys
  (left/right move handle by 5%).
- **Premium failure modes**: handle that pulses to "discover me" (G3+ ban);
  initial state at 0% or 100% (reads broken); auto-animation that demos the
  drag (reads gimmick).
- **Anti-tacky rules**: NO auto-animation. NO pulsing handle. The visitor
  must initiate. Initial state at 50%. Photos must be SAME aspect ratio.
- **Personalization knobs**: initial handle position (default 50% · NEVER
  outside 30-70%); orientation (vertical · horizontal); show/hide labels
  ("Prima · Dopo" / "Before · After"); enable touch.
- **Cluster fit**: medical-specialist (case studies · with explicit consent
  watermark), conservation-studio (vincolo before/after · DNA-named not
  shipped), real-estate (renovation listings), agency-creative-studio
  (rebrand case-study).
- **Cluster no-fit**: corporate-suite (no before/after register), lawyer,
  e-commerce, restaurant.
- **Anti-clone**: each cluster's case-content is different (clinical case ·
  restoration vincolo · brand redesign · property-renovation). The slider
  shape is reusable.

### MEDIA-5 · `gallery-strip-snap-horizontal`
- **Gravity**: G6 (cinematic) · single legitimate scroll-snap gravity.
- **Use case**: horizontal strip of images. Visitor scrolls horizontally
  (swipe / arrow keys / drag scrollbar) and the strip snaps to each image.
- **Visual behavior**: `scroll-snap-type: x mandatory` on the container.
  Each image is a snap target. A subtle scroll-progress indicator below the
  strip shows position (1px hairline + accent dot).
- **Interaction behavior**: swipe / drag / arrow keys. Tab focuses next image.
  Click an image opens MEDIA-6 lightbox.
- **Premium failure modes**: snap that overshoots (reads janky); snap on
  vertical (banned · scroll-snap is horizontal-only in this library); snap
  that hides scrollbar without keyboard navigation (accessibility fail).
- **Anti-tacky rules**: horizontal-only. Keyboard navigable. Visible
  scroll-progress indicator. Reduced-motion: snap is disabled · strip is
  scrollable normally.
- **Personalization knobs**: image set; image count (3-12); show/hide
  scroll-progress; enable/disable lightbox link.
- **Cluster fit**: portfolio (both), real-estate-ultra-luxury (property
  gallery), restaurant-fine (course-image strip).
- **Cluster no-fit**: corporate-suite (no horizontal-snap reading register),
  lawyer.
- **Anti-clone**: image content carries the distinction. Snap behavior is
  reusable.

### MEDIA-6 · `lightbox-preserve-context`
- **Gravity**: G6 (cinematic) — paired with MEDIA-5.
- **Use case**: clicking a gallery image opens a fullscreen lightbox. Esc
  closes. Background page scroll position is preserved.
- **Visual behavior**: lightbox overlay is a dark semi-transparent backdrop
  (rgba(0,0,0,0.92)) · the photo is centered · max 90% viewport height.
  Lightbox fades in (200ms ease-out) · fades out (150ms ease-in).
- **Interaction behavior**: click photo or `Enter` opens. Esc · click backdrop
  · click close-button (top-right · 32px hairline) closes. Arrow keys
  navigate between gallery images while open.
- **Premium failure modes**: backdrop that's pure black 100% (reads
  presentation-mode); lightbox that pushes scroll position to top on close
  (frustrating); lightbox that includes social-share buttons (reads marketing).
- **Anti-tacky rules**: backdrop is dark-with-alpha (NEVER pure black). Scroll
  position preserved on close. NO social-share. NO download button. NO
  fullscreen-toggle (the lightbox IS the fullscreen).
- **Personalization knobs**: enable/disable; backdrop opacity (0.85 · 0.92 ·
  0.96); show/hide close button (Esc always works); arrow-key navigation
  enable/disable.
- **Cluster fit**: pairs with MEDIA-5. Same fit / no-fit.
- **Anti-clone**: lightbox shape is reused; image content is sibling-distinct.

---

## §2.5 · Family 5 · Hover / focus / microinteraction systems

The vocabulary of "this responds to me." Critical for "real product" feel.

### MICRO-1 · `hairline-accent-on-hover` · CURRENT CORPORATE-SUITE DEFAULT
- **Gravity**: G1 / G2 / G3 / G4.
- **Use case**: link or button hover · a 1px hairline appears or thickens
  underneath.
- **Visual behavior**: `text-decoration: underline; text-decoration-color:
  transparent; transition: text-decoration-color 200ms;` — on hover, color
  shifts to accent. OR `border-bottom: 1px solid transparent` → accent.
- **Interaction behavior**: hover or focus.
- **Premium failure modes**: underline that animates (slides in from left)
  reads SaaS at G3 register; underline thickness change (1px → 2px) reads
  coloring-book-app.
- **Anti-tacky rules**: color transition only. NO thickness change. NO slide.
  Focus state shows the same hairline + the gold focus ring.
- **Personalization knobs**: accent color (must be palette token); transition
  duration (150 · 200 · 250ms); hairline thickness (always 1px).
- **Cluster fit**: every cluster.
- **Anti-clone**: this is the cluster-default. Sibling distinction is in
  accent color, not in mechanism.

### MICRO-2 · `card-lift-restrained`
- **Gravity**: G1 / G3 / G5.
- **Use case**: a card hover state · the card translates 2-4px up · subtle
  shadow grows (or hairline accent appears).
- **Visual behavior**: `transition: transform 250ms, box-shadow 250ms`. On
  hover: `transform: translateY(-2px) · box-shadow: 0 4px 12px rgba(0,0,0,0.08)`.
- **Interaction behavior**: hover only. Focus state has the gold ring.
- **Premium failure modes**: lift > 4px (reads bouncy); shadow > 16px blur
  (reads SaaS); rotation/tilt on lift (reads game-card).
- **Anti-tacky rules**: lift ≤ 4px. Shadow blur ≤ 16px. Shadow opacity ≤
  0.10. NO rotation. NO color change on the card.
- **Personalization knobs**: lift distance (2 · 3 · 4px); shadow strength
  (subtle · medium · NEVER strong); enable/disable.
- **Cluster fit**: corporate-suite (cases-list cards, leadership cards),
  agency-digital-studio, real-estate (listings).
- **Cluster no-fit**: corporate-suite Cornice (LF-2 editorial · cards in the
  3+1 magazine grid stay still · the editorial register prefers them
  composed-rest), portfolio-cinematic (gallery images don't lift).
- **Anti-clone**: card content carries the distinction. Lift parameters are
  family-specific (Pragma's 2px ≠ Aura's 4px-with-glow).

### MICRO-3 · `magnetic-button-restrained`
- **Gravity**: G5 (sprint-console only).
- **Use case**: a CTA button very subtly attracts the cursor when within 30px
  of its center.
- **Visual behavior**: button center is the attractor. Within 30px, the button
  translates toward the cursor by 0.15 × cursor-distance. NEVER more than
  6px total displacement.
- **Interaction behavior**: cursor proximity.
- **Premium failure modes**: magnet range > 50px (feels desperate); displacement
  > 8px (feels rubber-band); applied to multiple buttons on one page (every
  CTA pulls the cursor — reads carnival).
- **Anti-tacky rules**: range ≤ 30px. Displacement ≤ 6px. Limit ONE magnetic
  button per viewport. NEVER on body links · ONLY on the primary CTA in a
  dark band.
- **Personalization knobs**: range (20 · 30px); displacement multiplier (0.10 ·
  0.15 · 0.20); enable/disable.
- **Cluster fit**: agency-digital-studio (single hero CTA), startup-saas-
  landing (single hero CTA).
- **Cluster no-fit**: every other cluster. Specifically banned in
  corporate-suite (the institutional register rejects magnetic interactions).
- **Anti-clone**: only G5 clusters can use this. Within G5, sibling distinction
  is in CTA copy, not in magnetism.

### MICRO-4 · `text-underline-grow-from-left`
- **Gravity**: G1 / G2.
- **Use case**: a link's underline appears to grow from left to right on hover.
  Subtle editorial cue.
- **Visual behavior**: link has `position: relative; ::after { content: '';
  position: absolute; bottom: -2px; left: 0; width: 0; height: 1px;
  background: var(--accent); transition: width 250ms ease-out; }`. On hover,
  `width: 100%`.
- **Interaction behavior**: hover or focus.
- **Premium failure modes**: underline that grows from center (reads
  modern-template); underline that flashes after growing (reads mistake);
  duration < 150ms (reads instant · loses the editorial cue).
- **Anti-tacky rules**: grow from left only. Duration 200-300ms. NO flash. NO
  return-on-blur (collapse on `mouseleave` · not auto-collapse on a timer).
- **Personalization knobs**: duration (200 · 250 · 300ms); grow-from (left · 
  center is BANNED · right is BANNED — left only); accent color.
- **Cluster fit**: corporate-suite Cornice (LF-2 · editorial register · already
  shipped on the sticky 4-link side-rail), agency-creative-studio, restaurant-
  fine.
- **Cluster no-fit**: G3 institutional (Pragma · Fiscus · Causa) — the boardroom
  register prefers static underlines; G5 sprint-console (use the magnetic
  button instead).
- **Anti-clone**: same shape across all G2 clusters · sibling distinction is
  via accent color (Cornice's rust ≠ another LF-2 occupant's bottle-green).

### MICRO-5 · `accent-glow-focus-ring` · CLUSTER INVARIANT
- **Gravity**: cluster-shared.
- **Use case**: keyboard `:focus-visible` shows a gold/accent ring around the
  focused element. WCAG accessibility requirement.
- **Visual behavior**: `outline: 2px solid var(--accent); outline-offset:
  4px;`. Static (no pulse).
- **Interaction behavior**: keyboard focus only (NOT mouse-click focus, per
  `:focus-visible`).
- **Premium failure modes**: ring that pulses (G3+ ban); ring that disappears
  too quickly; ring color that doesn't meet AA contrast.
- **Anti-tacky rules**: 2px outline · 4px offset · accent-color · static. NO
  pulse, NO glow blur, NO inset shadow.
- **Personalization knobs**: outline thickness (always 2px); offset (4 · 6px);
  accent color (palette token).
- **Cluster fit**: every cluster. Cluster invariant per CS-NAV-02.
- **Anti-clone**: the gold ring is shared. The ACCENT TOKEN is sibling-distinct.

### MICRO-6 · `cursor-vignette`
- **Gravity**: G6 (cinematic) only.
- **Use case**: in a dark hero section, a subtle vignette/spotlight follows the
  cursor.
- **Visual behavior**: `radial-gradient` overlay positioned at cursor coordinates.
  Update on `mousemove` (throttled to 60fps).
- **Interaction behavior**: cursor position drives the spotlight.
- **Premium failure modes**: vignette outside the hero (banned · only hero);
  vignette that's too bright (reads flashlight); vignette on touch devices
  (reads broken — touch has no cursor); applied to a light-colored section
  (reads pollution).
- **Anti-tacky rules**: dark hero only. Subtle (max 20% darken at center · 0%
  at periphery). Disabled on touch devices. Disabled with reduced-motion.
- **Personalization knobs**: spotlight intensity (subtle · medium · NEVER
  strong); enable/disable.
- **Cluster fit**: portfolio-cinematic (Pixel hero), agency-digital-studio
  (Aura's dark hero · light touch).
- **Cluster no-fit**: every cluster with a cream-paper hero (which is most
  of corporate-suite). Specifically banned in LF-2 (cream paper) and LF-1/3/4
  default heroes.
- **Anti-clone**: only G6 clusters · within G6, vignette intensity is family-
  specific (cinematic-photographer = subtle · digital-studio = medium).

---

## §2.6 · Family 6 · Editorial motion systems

The patterns specifically for the LF-2 editorial register (and its peers).

### EDIT-1 · `text-fade-in-on-view-staggered` · CURRENT CORPORATE-SUITE DEFAULT
- **Gravity**: G1 / G2 (the safe default).
- **Use case**: section text reveals on viewport entry · siblings stagger by 80ms.
- **Visual behavior**: `opacity: 0; transform: translateY(12px);` initial state →
  `opacity: 1; translateY(0);` over 600ms ease-out. Siblings stagger 80ms.
- **Interaction behavior**: triggered by IntersectionObserver at 30% visibility.
  ONE-time per session.
- **Premium failure modes**: stagger that takes too long (>1500ms total reads
  loading); content that re-fades on scroll-back (annoying).
- **Anti-tacky rules**: total stagger ≤ 1500ms. ONE-time. Reduced-motion:
  content visible at first paint.
- **Personalization knobs**: stagger duration (60 · 80 · 100ms); per-element
  duration (400 · 600 · 800ms); translate distance (8 · 12 · 16px); enable/disable.
- **Cluster fit**: every cluster (this is the safe default).
- **Anti-clone**: same shape everywhere. Distinction comes from content.

### EDIT-2 · `pull-quote-em-reveal`
- **Gravity**: G2 (editorial).
- **Use case**: pull-quote in a narrative essay · the italic-em word reveals
  with a 200ms delay after the surrounding text fades in.
- **Visual behavior**: surrounding text fades in (per EDIT-1) · the italic-em
  span has its own `opacity: 0; transform: scaleY(0.95);` initial → `opacity:
  1; scaleY(1);` over 300ms after a 200ms delay.
- **Interaction behavior**: IntersectionObserver triggered.
- **Premium failure modes**: em that flashes (G3+ ban); em that grows (reads
  zoom-in); em with delay > 500ms (reads broken sequence).
- **Anti-tacky rules**: delay 200ms · scale start ≥ 0.95 · NO color change ·
  NO flash. Reduced-motion: em visible at first paint with surrounding.
- **Personalization knobs**: delay (150 · 200 · 250ms); scale start (0.95 · 0.98 ·
  1.0 — opt out); enable/disable.
- **Cluster fit**: corporate-suite LF-2 (Cornice · Causa · the 3 pull-quotes
  in the narrative essay).
- **Cluster no-fit**: G3 institutional, G5/G6, agency-digital-studio.
- **Anti-clone**: pull-quote em-WORD differs per sibling (Cornice's `argomento`
  · Causa's `evidenza` · per `corporate-suite-distinctness-matrix.md §1.4`).

### EDIT-3 · `drop-cap-stagger-around-paragraph`
- **Gravity**: G2 (editorial).
- **Use case**: narrative essay paragraph 1 has a drop-cap. Drop-cap appears
  first; paragraph fades in around it with a 300ms delay.
- **Visual behavior**: drop-cap fades in over 600ms ease-out. After 300ms,
  paragraph fades in (per EDIT-1).
- **Interaction behavior**: IntersectionObserver.
- **Premium failure modes**: drop-cap that drops in (animates from above · reads
  cartoon); drop-cap that pulses (G3+ ban); drop-cap with stretch animation
  (reads gimmick).
- **Anti-tacky rules**: fade only. NO drop-from-above. NO pulse. NO stretch.
  Drop-cap font and color match the cluster's drop-cap convention (Cornice's
  rust 84px Cormorant).
- **Personalization knobs**: drop-cap delay before paragraph (200 · 300 · 400ms);
  drop-cap fade duration (400 · 600 · 800ms); enable/disable.
- **Cluster fit**: corporate-suite LF-2 (Cornice's narrative · Causa's narrative).
- **Cluster no-fit**: same as EDIT-2.
- **Anti-clone**: the drop-cap glyph (which letter it lands on) is sibling-
  distinct based on the paragraph's first word.

### EDIT-4 · `sticky-side-rail-anchor-active`
- **Gravity**: G2 (editorial).
- **Use case**: narrative essay has a sticky side-rail with 4 anchor links
  (Lo studio · Archivio · Servizi · Progetti). As the visitor scrolls, the
  link corresponding to the current section becomes active (accent color).
- **Visual behavior**: side-rail is `position: sticky; top: 100px;`. Active
  link transitions color (250ms ease-out) when its section's heading crosses
  the rail's top.
- **Interaction behavior**: clicking a link smooth-scrolls to the section.
  Keyboard navigable.
- **Premium failure modes**: rail that pulses on active change (G3+ ban);
  smooth-scroll with overshoot/bounce (reads springy); active-state with
  background fill (reads dashboard).
- **Anti-tacky rules**: color transition only on active. Smooth-scroll
  duration 600ms · ease-out. NO bounce. Active-state is COLOR ONLY · no fill.
  Reduced-motion: smooth-scroll → instant scroll.
- **Personalization knobs**: link count (3-6); link labels; sticky offset
  (80 · 100 · 120px); active color; smooth-scroll on/off.
- **Cluster fit**: corporate-suite LF-2 (canonical · Cornice/Causa narrative).
- **Cluster no-fit**: every non-LF-2 family. The pattern is LF-2's claim.
- **Anti-clone**: link labels are sibling-specific (Cornice's `Lo studio ·
  Archivio · Servizi · Progetti` ≠ Causa's `Studio · Materie · Pubblicazioni
  · Contenzioso`).

### EDIT-5 · `magazine-page-flip` · BANNED
- **Gravity**: would be G2 if it weren't banned.
- **Why banned**: reads gimmick. Magazine-page-flip is the single editorial
  motion the cluster forbids · it is included here to document the prohibition
  so future planners cannot re-introduce it. Examples that violate: 3D-flip
  carousels, page-curl-on-scroll, 2-page-spread that "pages over" with a
  simulated paper sound. **All BLOCKED at archetype level.**

---

## §2.7 · Family 7 · Navigation behavior systems

How the chrome moves (or doesn't).

### NAV-1 · `sticky-condensed-on-scroll` · CURRENT LF-5 SHIPPED
- **Gravity**: G1 / G3 / G4.
- **Use case**: nav shrinks from 76 to 56px after 240px of scroll.
- **Visual behavior**: nav `height: 76px → 56px` over 200ms ease-out at scroll
  threshold. Wordmark and link sizes adjust proportionally.
- **Interaction behavior**: scroll position only.
- **Premium failure modes**: shrink that bounces (G3+ ban); shrink that hides
  some links (reads broken); shrink that moves across viewport mid-shrink.
- **Anti-tacky rules**: shrink only · no bounce · no link-hiding · no
  position-change. Reduced-motion: nav has fixed condensed height from start.
- **Personalization knobs**: scroll threshold (120 · 240 · 320px); shrink ratio
  (76/56 · 80/60 · 64/48); enable/disable.
- **Cluster fit**: corporate-suite LF-5 (Continua canonical), corporate-suite
  LF-2 second occupant (with smaller shrink delta), real-estate-luxury.
- **Cluster no-fit**: G5 sprint-console (the nav stays fixed for usability),
  G6 cinematic (the cinematic register prefers no chrome motion).
- **Anti-clone**: shrink ratio is family-specific. LF-5's 76→56 is taken; an LF-2
  second occupant with shrink uses 80→60.

### NAV-2 · `sticky-hide-on-scroll-down`
- **Gravity**: G1 / G5.
- **Use case**: nav hides on scroll-down (visitor is reading) and reveals on
  scroll-up (visitor wants to navigate).
- **Visual behavior**: nav `transform: translateY(0 → -100%)` over 250ms ease-
  out on downward scroll past 240px · `translateY(-100% → 0)` over 200ms
  ease-out on upward scroll.
- **Interaction behavior**: scroll direction only.
- **Premium failure modes**: hide that's too aggressive (hides on every micro-
  scroll-down · annoying); hide that disappears the locale switcher (lost
  affordance).
- **Anti-tacky rules**: minimum scroll-distance threshold of 120px before
  re-toggling (anti-jitter). NO hide on initial scroll-down before threshold
  is met. Reduced-motion: nav stays sticky always.
- **Personalization knobs**: scroll threshold; hide on/off; reveal on/off.
- **Cluster fit**: agency-digital-studio (Aura), startup-saas, lawyer-modern-
  transparent.
- **Cluster no-fit**: G2/G3/G4 (the institutional register prefers persistent
  nav presence), G6 cinematic (the cinematic register prefers no chrome
  motion).
- **Anti-clone**: same shape across G5 cluster · sibling distinction comes
  from nav content (links · CTA copy · wordmark).

### NAV-3 · `scroll-progress-bar-thin`
- **Gravity**: G5 sprint-console primary; G2 editorial in light-touch form.
- **Use case**: 1px progress bar at top of viewport showing scroll percentage.
- **Visual behavior**: 1px bar in accent color · `width: 0% → 100%` driven by
  scroll position. Static · no animation other than width.
- **Interaction behavior**: read-only.
- **Premium failure modes**: bar > 1px (reads loading-bar); gradient on bar
  (reads SaaS); bar that pulses (reads error).
- **Anti-tacky rules**: 1px height. Single accent color. NO pulse. NO gradient.
- **Personalization knobs**: enable/disable; bar position (top · bottom);
  accent color (palette token).
- **Cluster fit**: agency-digital-studio, startup-saas, corporate-suite LF-2
  long-narrative second occupant (light-touch · subtle progress cue).
- **Cluster no-fit**: G3 institutional, G4 stewardship, G6 cinematic.
- **Anti-clone**: 1px is the ceiling · siblings cannot differentiate via thickness.
  Distinction is via accent color and on/off.

### NAV-4 · `breadcrumb-persistent-deep`
- **Gravity**: G1 / G3.
- **Use case**: deep pages (case-detail · service-detail) have an inline
  breadcrumb in the nav showing the path.
- **Visual behavior**: static breadcrumb shown below the wordmark · separator
  is a simple `›` glyph.
- **Interaction behavior**: each segment is a link to its parent page.
- **Premium failure modes**: breadcrumb on home (redundant); breadcrumb with
  emoji separators (reads consumer); breadcrumb that scrolls horizontally
  on overflow (truncate instead).
- **Anti-tacky rules**: home only when justified · home is hidden on home page.
  Truncate middle segments at 1100px viewport · NO horizontal scroll.
- **Personalization knobs**: separator glyph (`›` · `/` · `→`); show/hide on
  specific page kinds.
- **Cluster fit**: corporate-suite (case-detail · service-detail · about
  multi-page), real-estate (listing-detail), e-commerce (product-detail).
- **Cluster no-fit**: G2 editorial home (no deep navigation in a magazine-
  spread reading), G6 cinematic.
- **Anti-clone**: breadcrumb structure is page-shape-driven, not sibling-driven.
  Same pattern across all clusters that need it.

### NAV-5 · `locale-pill-static-with-flag` · BANNED FOR INSTITUTIONAL
- **Gravity**: G5 / G6.
- **Use case**: locale switcher shows flag emoji alongside the language code.
- **Visual behavior**: pill with flag-emoji + language code.
- **Why partially banned**: emoji in chrome reads consumer-brand. The
  corporate-suite cluster + lawyer-classic-gold REJECT this pattern.
- **Cluster fit**: real-estate-mass-market, e-commerce-fashion-editorial (with
  serif · disciplined version), startup-saas-landing.
- **Cluster no-fit**: corporate-suite (all LFs), lawyer-classic-gold, medical-
  specialist (the institutional register rejects emoji-in-chrome).
- **Anti-clone**: this pattern is SECONDARY · the cluster default is
  pill-with-language-code-only.

### NAV-6 · `scroll-position-memory`
- **Gravity**: G1 / G2 (with explicit consent).
- **Use case**: returning visitor lands at the last-seen scroll position on a
  given page.
- **Visual behavior**: on page-load, scroll position is restored without
  animation (instant).
- **Interaction behavior**: requires consent (cookie/localStorage). Visitor
  can opt out.
- **Premium failure modes**: scroll-restore that fights with browser's native
  scroll-restoration (reads broken); restore that conflicts with anchor links;
  restore on first visit (reads creepy).
- **Anti-tacky rules**: explicit consent gate. First-visit always lands at top.
  Anchor links override restore. Reduced-motion has no effect (it's instant).
- **Personalization knobs**: consent state (opt-in default); per-page enable/disable.
- **Cluster fit**: corporate-suite long-narrative, real-estate-luxury (property-
  detail).
- **Cluster no-fit**: every cluster that doesn't justify it (most clusters).
- **Anti-clone**: presence of restore is the differentiator; behavior is identical.

---

## §2.8 · Family 8 · Comparison / before-after / scenario modules

Showing two states side by side. Critical for service offerings.

### COMP-1 · `before-after-drag-slider` (= MEDIA-4)
See §2.4 MEDIA-4. Cross-listed because the visual mechanism is media-class but
the semantic class is comparison.

### COMP-2 · `scenario-tab-switcher`
- **Gravity**: G1 / G5.
- **Use case**: 2-3 tabs that show different scenarios. "Standard fee · With
  retainer · Multi-year mandate". Switching tabs cross-fades content.
- **Visual behavior**: tabs have hairline divider · active tab has accent
  underline · cross-fade between scenarios over 250ms ease-out.
- **Interaction behavior**: click tab · keyboard arrow keys.
- **Premium failure modes**: scenarios named "Without us · With us" (reads
  snake-oil — see anti-tacky rules); cross-fade with slide (reads carousel);
  active tab with background fill (reads SaaS app).
- **Anti-tacky rules**: NEVER use "without us" framing. Tab labels must be
  factual scenarios, not comparison narratives. Cross-fade only · NO slide.
  Active state is hairline underline only · NO fill.
- **Personalization knobs**: scenario labels; scenario content; default-active
  tab.
- **Cluster fit**: corporate-suite (pricing-explainers · service-tiers),
  lawyer (engagement scenarios), agency-digital-studio (sprint-tier comparison).
- **Cluster no-fit**: G2 editorial, G6 cinematic.
- **Anti-clone**: scenario labels and content carry the distinction.

### COMP-3 · `metric-vs-benchmark-chip`
- **Gravity**: G1 / G5.
- **Use case**: KPI cell shows your metric vs industry benchmark. "Our: 94% ·
  Industry: 78%".
- **Visual behavior**: static · two values with a hairline rule between · NO
  bars · NO arrows.
- **Interaction behavior**: hover the benchmark to see source citation.
- **Premium failure modes**: bar comparison (reads infographic); arrow up/down
  (reads dashboard); benchmark that's a fictional number (reads dishonest).
- **Anti-tacky rules**: benchmark MUST be a citable source. NO bar. NO arrow.
  NO color coding (green vs red).
- **Personalization knobs**: benchmark value; benchmark source; show/hide.
- **Cluster fit**: lawyer-modern, audit-led methodology, agency-digital-studio.
- **Cluster no-fit**: G2/G3 editorial, G6 cinematic, G4 stewardship.
- **Anti-clone**: benchmark source is sibling-distinct.

### COMP-4 · `case-vs-baseline-narrative`
- **Gravity**: G1 / G3.
- **Use case**: case-study detail page · "before · after" with narrative
  context. NOT a slider · a written narrative.
- **Visual behavior**: 2-column layout · before-state | after-state · static
  · text-led.
- **Interaction behavior**: read-only.
- **Premium failure modes**: as a slider (use COMP-1 for visual cases · COMP-4
  for text-led cases); using stock photography for "before" (reads cliché).
- **Anti-tacky rules**: text-led only. Photos optional · if used, must be
  client-consented.
- **Personalization knobs**: column ratio (50/50 · 60/40); show photos
  on/off; section labels.
- **Cluster fit**: corporate-suite case-detail (Pragma · Cornice · Causa),
  lawyer case-detail.
- **Cluster no-fit**: e-commerce, restaurant.
- **Anti-clone**: case content is sibling-distinct.

---

## §2.9 · Family 9 · Quote / testimonial / authority modules

Voices not your own.

### QUOTE-1 · `editorial-pull-quote-static` · CURRENT CORPORATE-SUITE DEFAULT
- **Gravity**: G1 / G2 / G3.
- **Use case**: italic serif large quote in a narrative essay or as a hero
  side-quote.
- **Visual behavior**: static · 32-44px italic serif · accent-color em on a
  load-bearing word · attribution below in smaller sans.
- **Interaction behavior**: read-only.
- **Premium failure modes**: quote in a card with shadow (reads testimonial-
  block · breaks editorial register); quote with quotation-mark sweep on
  arrival (reads animation-fest); quote without attribution (reads
  ghost-written).
- **Anti-tacky rules**: italic serif. NO card chrome. NO quotation-mark
  sweep. Attribution required (name + role + organization).
- **Personalization knobs**: quote text; em-word position; attribution; size
  (32 · 38 · 44px).
- **Cluster fit**: every cluster.
- **Anti-clone**: each sibling's quote is a different speaker.

### QUOTE-2 · `quote-carousel-restrained`
- **Gravity**: G1 / G5.
- **Use case**: 3 quotes max · navigation dots · NO autoplay.
- **Visual behavior**: 3 quote-cards · only one visible at a time · cross-fade
  300ms on dot-click. Dots below in hairline.
- **Interaction behavior**: dot click · keyboard arrows · swipe gesture (mobile).
  NO autoplay.
- **Premium failure modes**: autoplay (reads marketing-template); cards with
  drop-shadow (reads SaaS); arrows on left/right of card (reads carousel).
- **Anti-tacky rules**: NO autoplay (the visitor controls). NO arrows · dots
  only. ≤ 3 quotes.
- **Personalization knobs**: quote count (1 · 2 · 3); cross-fade duration; dot
  position.
- **Cluster fit**: corporate-suite (testimonial section optional), agency,
  lawyer-modern.
- **Cluster no-fit**: G2 editorial (use QUOTE-1 instead), G6 cinematic.
- **Anti-clone**: each carousel features 3 different speakers per sibling.

### QUOTE-3 · `single-quote-with-portrait`
- **Gravity**: G1 / G3.
- **Use case**: ONE quote with a small environmental portrait of the speaker.
- **Visual behavior**: static · portrait left (square 96px) · quote right
  (italic serif).
- **Interaction behavior**: read-only.
- **Premium failure modes**: portrait that's a stock-LinkedIn headshot (reads
  fake testimonial); quote that's too long (reads ghost-written); quote
  followed by "verified" badge (reads e-commerce review).
- **Anti-tacky rules**: portrait must be environmental (the room is half the
  subject) · per CS-IMG-COH-08. Quote ≤ 60 words. NO badges.
- **Personalization knobs**: quote text; speaker name + role; portrait image.
- **Cluster fit**: corporate-suite, lawyer, family-office.
- **Cluster no-fit**: G6 cinematic (cinematic register prefers no testimonials),
  e-commerce.
- **Anti-clone**: speaker is sibling-distinct.

### QUOTE-4 · `quote-stack-sticky-rotate`
- **Gravity**: G2 (editorial) · G6 with discipline.
- **Use case**: 3 quotes stacked vertically. Sticky pin holds the topmost in
  view as the visitor scrolls past · the next quote rotates into focus.
- **Visual behavior**: container is `position: sticky` for the duration of 3
  scroll-heights. Active quote has full opacity · others are 0.4. Cross-fade
  on scroll-progression.
- **Interaction behavior**: scroll only.
- **Premium failure modes**: scroll-jacking to enforce one-quote-per-stop
  (banned); quotes that flip (banned); 4+ quotes (loses sticky discipline).
- **Anti-tacky rules**: 3 quotes max. NO scroll-jacking. NO flip. Reduced-
  motion: all 3 quotes are fully visible · no sticky behavior.
- **Personalization knobs**: quote count (always 3); per-quote opacity for
  inactive (0.3 · 0.4 · 0.5); enable/disable.
- **Cluster fit**: corporate-suite LF-2 second occupant (extension of narrative),
  agency-creative-studio (manifesto with peer voices).
- **Cluster no-fit**: G3 institutional, G5 sprint, G6 cinematic at hero.
- **Anti-clone**: each sibling's 3 quotes feature different speakers.

### QUOTE-5 · `attribution-rich-quote`
- **Gravity**: G1 / G3.
- **Use case**: quote with full attribution: name + role + organization +
  optional LinkedIn-link icon.
- **Visual behavior**: static · attribution in 14px sans below quote.
- **Interaction behavior**: hover/focus on attribution → small chip with
  organization linkage.
- **Premium failure modes**: clickable LinkedIn icon that opens a modal (reads
  CRM); attribution with too many micro-credentials (reads stuffed).
- **Anti-tacky rules**: ≤ 3 attribution lines. LinkedIn icon optional · subtle.
  NO emoji. NO "verified" badges.
- **Personalization knobs**: attribution lines (1 · 2 · 3); LinkedIn link
  on/off; organization linkage on/off.
- **Cluster fit**: corporate-suite, lawyer, family-office, real-estate.
- **Cluster no-fit**: e-commerce (per-product reviews use a different pattern),
  restaurant.
- **Anti-clone**: attribution content is sibling-distinct.

### QUOTE-6 · `peer-citation-named-industry`
- **Gravity**: G3 / G4.
- **Use case**: a named industry peer cites the firm in a publication, with link.
  "MF Magazine · 14/03/2024 · 'Causa · the litigation studio rewriting Italian
  Cassazione doctrine on consultancy liability.'"
- **Visual behavior**: small hairline-bordered cell with publication mark, date,
  excerpt, and "→ leggi" link.
- **Interaction behavior**: link opens external publication.
- **Premium failure modes**: peer-citation with logo of the publication (reads
  vanity); excerpt that's too long (reads marketing).
- **Anti-tacky rules**: text-only. Excerpt ≤ 30 words. External link is
  required (it's the proof).
- **Personalization knobs**: publication name; date; excerpt; link URL.
- **Cluster fit**: corporate-suite Cornice · Causa (curatorial · forensic),
  lawyer-classic-gold, family-office.
- **Cluster no-fit**: G5/G6.
- **Anti-clone**: each sibling's cited publication is different.

---

## §2.10 · Family 10 · Case-study preview systems

How the cases-list feels.

### CASE-1 · `magazine-grid-3-1` · CURRENT LF-2 SHIPPED
- **Gravity**: G2 (editorial).
- **Use case**: 1 hero card spans rows 1-3 · 3 small cards stacked right.
- **Visual behavior**: static grid · subtle hairline-on-hover (MICRO-1).
- **Interaction behavior**: hover changes hairline · click navigates to detail.
- **Premium failure modes**: cards that lift on hover (G2 register prefers
  static · use MICRO-1 instead); 4 equal cards (loses asymmetry).
- **Anti-tacky rules**: static. Asymmetry preserved. 1 hero + 3 small.
- **Personalization knobs**: hero card content; small card count (always 3);
  hover affordance (hairline · subtle-shift).
- **Cluster fit**: corporate-suite LF-2 (Cornice canonical · Causa).
- **Cluster no-fit**: every other family.
- **Anti-clone**: hero card is sibling's lead landmark.

### CASE-2 · `list-row-stagger`
- **Gravity**: G1 / G3.
- **Use case**: vertical list of cases · each row has photo + title + meta.
- **Visual behavior**: rows fade in with EDIT-1 staggered reveal.
- **Interaction behavior**: hover-row → MICRO-2 lift.
- **Premium failure modes**: rows that shift sideways on hover (reads
  marketplace); rows with infinite-scroll loading (reads CRM list).
- **Anti-tacky rules**: pagination · no infinite scroll · no sideways shift.
- **Personalization knobs**: row count per page; lift-on-hover on/off.
- **Cluster fit**: corporate-suite LF-1/LF-3/LF-4 (current shipped),
  agency-digital-studio.
- **Cluster no-fit**: G2 editorial, G6 cinematic.
- **Anti-clone**: row content is sibling-distinct.

### CASE-3 · `timeline-strip-vertical` · CURRENT LF-5 SHIPPED
- **Gravity**: G4 (stewardship).
- See TIME-1.

### CASE-4 · `gallery-strip-horizontal-snap` (= MEDIA-5)
- See §2.4. Cross-listed.

### CASE-5 · `numbered-ledger-editorial`
- **Gravity**: G2 (editorial).
- **Use case**: numbered case-study ledger like agency-creative-studio's
  `editorial-index-dossier` — index · name · sector · year · arrow.
- **Visual behavior**: static rows. Hover: row gets a hairline divider color
  shift.
- **Interaction behavior**: click navigates to detail.
- **Premium failure modes**: numbered ledger with crossed-out items (reads
  resume); ledger with too many columns (reads spreadsheet).
- **Anti-tacky rules**: ≤ 5 columns. Static rows.
- **Personalization knobs**: column count; sort order.
- **Cluster fit**: agency-creative-studio, audit-led methodology, lawyer-classic-gold.
- **Cluster no-fit**: G6 cinematic.
- **Anti-clone**: ledger structure is sibling-specific (number format ·
  column choice).

### CASE-6 · `filterable-grid-with-chips`
- **Gravity**: G1 / G5.
- **Use case**: case grid with sector chips at top · click a chip → grid
  reflows to show only matching cases.
- **Visual behavior**: chips with hairline border · active chip is filled
  with accent. Grid cells reflow with 300ms ease-out (FLIP technique · NOT
  fade).
- **Interaction behavior**: click chip · keyboard arrow keys.
- **Premium failure modes**: reflow that takes >500ms (reads slow); chips
  that overflow vertically (use horizontal scroll on chip rail or truncate);
  empty state without copy ("No cases match" silently).
- **Anti-tacky rules**: FLIP layout transition for the grid (preserve
  card identity · don't fade-recreate). Empty-state message present.
  Reduced-motion: layout changes instantly · no transition.
- **Personalization knobs**: chip set (sector list); default-active chip;
  reflow duration.
- **Cluster fit**: corporate-suite (case-list page · NOT home), agency-digital-
  studio, audit-led methodology.
- **Cluster no-fit**: G6 cinematic, restaurant.
- **Anti-clone**: chip set is sibling-distinct.

### CASE-7 · `case-card-reveal-inline`
- **Gravity**: G1 / G2.
- **Use case**: small previews expand to full card on click. Catalog with
  many entries · home shows compact teasers.
- **Visual behavior**: card height transitions from compact (120px) to
  expanded (480px) over 350ms ease-out.
- **Interaction behavior**: click toggle · keyboard accessible.
- **Premium failure modes**: expand-with-content-shift (other cards jump);
  expand-into-modal (use COMP-1 inline-expansion convention).
- **Anti-tacky rules**: inline expansion only. Other cards animate to their
  new positions (FLIP). Reduced-motion: instant expand · instant collapse.
- **Personalization knobs**: compact height; expanded height; transition
  duration.
- **Cluster fit**: lawyer-classic-gold (long sentence-list), audit-led
  methodology (long audit-list).
- **Cluster no-fit**: G2 LF-2 magazine grid (the 3+1 is a fixed shape · use
  CASE-1 instead).
- **Anti-clone**: card content is sibling-distinct.

---

## §2.11 · Family 11 · Scroll choreography patterns

How the page reveals as the visitor descends.

### SCROLL-1 · `quiet-fade-on-view` (= EDIT-1) · CURRENT DEFAULT
See §2.6.

### SCROLL-2 · `staggered-reveal-multi-card`
- **Gravity**: G1 / G2.
- **Use case**: multi-card sections (pillars · KPI band · leadership grid · cases).
- **Visual behavior**: cards stagger 80ms each as section enters viewport.
- **Interaction behavior**: scroll only.
- **Premium failure modes**: stagger that visibly takes long (>2s); stagger
  on scroll-back (annoying).
- **Anti-tacky rules**: ONE-time. Total stagger ≤ 1500ms. Reduced-motion:
  cards visible at first paint.
- **Personalization knobs**: per-element duration; stagger gap.
- **Cluster fit**: every cluster's multi-card sections.
- **Anti-clone**: card content is sibling-distinct.

### SCROLL-3 · `sticky-pin-with-progress-narrative`
- **Gravity**: G2 (editorial).
- **Use case**: long narrative · left column is sticky (heading + side-rail) ·
  right column scrolls (paragraphs · pull-quotes · images).
- **Visual behavior**: left column `position: sticky; top: 100px;`. Right
  column scrolls normally. As right scrolls past sections, left's side-rail
  active link transitions (per EDIT-4).
- **Interaction behavior**: scroll only.
- **Premium failure modes**: pin that breaks responsive layout below 880px;
  pin that's full-viewport-height (reads landing-page section-pin).
- **Anti-tacky rules**: pin scope is the narrative section · NOT full page.
  Below 880px the pin disengages and the side-rail collapses to a horizontal
  band.
- **Personalization knobs**: pin offset; side-rail link count.
- **Cluster fit**: corporate-suite LF-2 (Cornice/Causa narrative).
- **Cluster no-fit**: every non-LF-2 family.
- **Anti-clone**: side-rail labels and section count are sibling-distinct.

### SCROLL-4 · `horizontal-snap-scroll` (= MEDIA-5)
See §2.4.

### SCROLL-5 · `parallax-restrained-hero` (= MEDIA-2)
See §2.4.

### SCROLL-6 · `scroll-velocity-aware-fade`
- **Gravity**: G1 (cluster-shared meta-pattern).
- **Use case**: if visitor is scrolling fast (>1500px/s), fade-in animations
  are shortened or skipped to prevent motion-sickness.
- **Visual behavior**: standard SCROLL-1 fade-in · OR if velocity > threshold,
  duration shrinks to 200ms · OR if velocity > 2× threshold, animation is
  skipped (content visible immediately).
- **Interaction behavior**: scroll velocity sensed.
- **Premium failure modes**: velocity sensor that's too aggressive (skips
  legitimate animations on normal scrolling).
- **Anti-tacky rules**: thresholds well-tuned (1500px/s · 3000px/s defaults).
  Disabled with reduced-motion.
- **Personalization knobs**: velocity thresholds; enable/disable.
- **Cluster fit**: every cluster — this is a meta-pattern that COVERS for
  scroll-fade-in (SCROLL-1 + SCROLL-2 inherit it).
- **Anti-clone**: same shape across all clusters · safety net for animation
  fatigue.

---

## §2.12 · Family 12 · Low-motion variants and reduced-motion-safe equivalents

For each pattern above, when `prefers-reduced-motion: reduce`, an equivalent.

| Pattern | Reduced-motion equivalent |
|---|---|
| KPI-2 `count-up-on-view` | static final number with same tabular-nums |
| KPI-3 `live-counter` | static recent value with timestamp |
| KPI-4 `range-fill` | static fill at end-state width |
| KPI-5 `comparative-tick` | static delta + arrow + benchmark |
| TIME-2 `scroll-driven-timeline` | static vertical timeline (TIME-1) |
| TIME-3 `chronological-tick-horizontal` | static horizontal line with all ticks |
| TIME-4 `stewardship-rings-concentric` | static rings drawn at first paint |
| TIME-5 `chapter-stepper-magazine` | static chapter indicator at last position |
| EVID-1 `progressive-disclosure-tap` | always-expanded inline · "[collapse]" link |
| EVID-2 `attestation-chip-hover` | tooltip shown without fade transition |
| EVID-3 `case-citation-pop` | always-expanded · "[collapse]" link |
| EVID-5 `provenance-tooltip-image` | static caption below image (no hover) |
| MEDIA-1 `cinematic-fade-on-view` | image fully revealed at first paint |
| MEDIA-2 `parallax-restrained-hero` | static photo · no offset |
| MEDIA-3 `image-grid-stagger-reveal` | static grid |
| MEDIA-4 `before-after-drag-slider` | side-by-side static photos with labels |
| MEDIA-5 `gallery-strip-snap-horizontal` | regular horizontal scroll · no snap |
| MEDIA-6 `lightbox-preserve-context` | unchanged (instant overlay · no fade) |
| MICRO-1 `hairline-accent-on-hover` | unchanged (color transition is fine even at reduced-motion · OPTIONAL: static accent on hover with no transition) |
| MICRO-2 `card-lift-restrained` | static border-color shift instead of lift |
| MICRO-3 `magnetic-button-restrained` | disabled · static button |
| MICRO-4 `text-underline-grow-from-left` | static accent underline appears on hover (no grow) |
| MICRO-5 `accent-glow-focus-ring` | unchanged |
| MICRO-6 `cursor-vignette` | disabled |
| EDIT-1 `text-fade-in-on-view-staggered` | content visible at first paint |
| EDIT-2 `pull-quote-em-reveal` | unchanged from EDIT-1 |
| EDIT-3 `drop-cap-stagger-around-paragraph` | drop-cap and paragraph visible together |
| EDIT-4 `sticky-side-rail-anchor-active` | smooth-scroll → instant scroll · color transition unchanged |
| NAV-1 `sticky-condensed-on-scroll` | nav has fixed condensed height from start |
| NAV-2 `sticky-hide-on-scroll-down` | nav stays sticky always |
| NAV-3 `scroll-progress-bar-thin` | unchanged · scroll-bound width is not animation |
| QUOTE-2 `quote-carousel-restrained` | all 3 quotes shown stacked |
| QUOTE-4 `quote-stack-sticky-rotate` | all 3 fully visible · no sticky |
| CASE-6 `filterable-grid-with-chips` | layout changes instantly · no transition |
| CASE-7 `case-card-reveal-inline` | instant expand · instant collapse |
| SCROLL-3 `sticky-pin-with-progress-narrative` | pin disengaged · normal flow |
| SCROLL-6 `scroll-velocity-aware-fade` | unchanged · velocity adapter is the safety net |

The general principle: **every animation has a non-animation equivalent that
delivers the same INFORMATION but not the same FEEL.** The information remains
accessible.

---

## §3 · Cluster fit · the matrix

For each cluster + each motion gravity + which patterns are recommended /
allowed / banned. This is the orchestrator's quick-look at intake.

### Corporate-suite (LF-1 / LF-3 / LF-4 — Pragma · Fiscus · Solaria)

- **Default gravity**: G1 (institutional default).
- **Recommended patterns to introduce in next pass**:
  - KPI-2 (count-up-on-view) · ONE invocation per home at the existing
    KPI band.
  - EVID-2 (attestation-chip-hover) on credentials.
  - EVID-4 (audit-trail-arrow) on KPI cells.
  - MICRO-1 (hairline-accent-on-hover · current default) — unchanged.
  - SCROLL-2 (staggered-reveal-multi-card) — current default · unchanged.
- **Allowed but not recommended**: COMP-2 (scenario-tab-switcher) on
  service-pricing pages.
- **Banned**: KPI-3 (live-counter), MICRO-3 (magnetic-button), MEDIA-2
  (parallax), MEDIA-6 (cursor-vignette), QUOTE-2 (carousel · use QUOTE-1),
  EDIT-5 (page-flip · always banned).

### Corporate-suite LF-2 (Cornice · Causa · editorial)

- **Default gravity**: G2 (editorial).
- **Recommended**:
  - EDIT-1 + EDIT-2 + EDIT-3 (current LF-2 default).
  - EDIT-4 (sticky-side-rail-anchor-active · current).
  - EVID-2 + EVID-5 (provenance-tooltip on hero photo).
  - CASE-1 (magazine-grid-3+1 · current).
- **Allowed**: TIME-3 (chronological-tick-horizontal · 2nd-occupant
  differentiator), TIME-5 (chapter-stepper · for long narratives), QUOTE-4
  (sticky-stack-rotate · 2nd-occupant differentiator).
- **Banned**: KPI-3 live-counter, MEDIA-2 parallax, MEDIA-6 cursor-vignette,
  MICRO-3 magnetic-button, NAV-3 progress-bar, QUOTE-2 carousel.

### Corporate-suite LF-5 (Continua · stewardship)

- **Default gravity**: G4 (stewardship-restrained).
- **Recommended**:
  - TIME-1 (static-vertical-timeline · current).
  - EVID-1 (progressive-disclosure on governance-cycle).
  - EVID-2 (attestation-chip on credentials).
  - MICRO-1 (hairline-accent-on-hover · current).
- **Allowed for 2nd-occupant**: TIME-2 (scroll-driven-timeline), TIME-4
  (stewardship-rings-concentric), QUOTE-6 (peer-citation).
- **Banned**: KPI-3 live-counter, MICRO-2 card-lift (stewardship
  prefers static cards), MICRO-3 magnetic, MEDIA-2 parallax, NAV-3 progress.

### Agency-digital-studio (Aura · sprint-console)

- **Default gravity**: G5 (sprint-console).
- **Recommended**:
  - KPI-3 (live-counter · the cluster's signature).
  - NAV-2 (sticky-hide-on-scroll-down).
  - NAV-3 (scroll-progress-bar-thin).
  - MICRO-3 (magnetic-button on hero CTA).
  - MICRO-2 (card-lift-restrained on capability-grid).
- **Allowed**: COMP-3 (metric-vs-benchmark), KPI-5 (comparative-tick).
- **Banned**: G2 editorial patterns inappropriate for product-velocity register.

### Agency-creative-studio (Vertex · editorial-agency)

- **Default gravity**: G2 (editorial).
- **Recommended**:
  - EDIT-1 + EDIT-2 + EDIT-3 (editorial reveal).
  - QUOTE-1 (editorial-pull-quote · current).
  - CASE-5 (numbered-ledger-editorial).
  - EVID-5 (provenance-tooltip · colophon-press).
- **Allowed**: TIME-3 (chronological-tick), QUOTE-4 (sticky-stack), MICRO-4
  (text-underline-grow).
- **Banned**: G5 sprint-console patterns, KPI-3 live-counter, MEDIA-2 parallax.

### Portfolio-cinematic (Pixel)

- **Default gravity**: G6 (cinematic).
- **Recommended**:
  - MEDIA-1 (cinematic-fade-on-view).
  - MEDIA-2 (parallax-restrained-hero).
  - MEDIA-5 (gallery-strip-snap-horizontal).
  - MEDIA-6 (lightbox-preserve-context).
  - MICRO-6 (cursor-vignette).
- **Banned**: every G1/G3/G5 pattern that imposes chrome on a cinematic register.

### Portfolio-editorial-designer-grid (Chiara)

- **Default gravity**: G2 (editorial).
- Inherits Vertex's recommendations. CASE-5 (numbered-ledger) is the canonical case.

### Real-estate-ultra-luxury

- **Default gravity**: G6 (cinematic) + G2 (concierge editorial cues).
- **Recommended**:
  - MEDIA-1 (cinematic-fade) on property hero.
  - MEDIA-5 + MEDIA-6 (gallery + lightbox) for property-detail.
  - MICRO-4 (text-underline-grow) on link/CTAs.
- **Banned**: G5 sprint patterns, MICRO-3 magnetic.

### Real-estate-mass-market

- **Default gravity**: G1 (institutional default).
- **Recommended**:
  - CASE-6 (filterable-grid-with-chips) for listings.
  - MICRO-2 (card-lift-restrained).
- **Allowed**: NAV-5 (locale-pill-with-flag).
- **Banned**: G6 cinematic patterns (mass-market is daylight-pragmatic).

### Lawyer-classic-gold (Lex)

- **Default gravity**: G3 (institutional · gravity-end).
- **Recommended**:
  - QUOTE-1 (editorial-pull-quote).
  - EVID-1 (progressive-disclosure on case-law).
  - EVID-2 (attestation-chip on Albo).
  - MICRO-1 (hairline-accent · gold).
- **Banned**: G5 sprint, MICRO-3 magnetic, NAV-3 progress, MEDIA-2 parallax,
  MEDIA-6 cursor-vignette, EDIT-5 page-flip.

### Lawyer-modern-transparent (Juris)

- **Default gravity**: G1 with light G5 borrowing.
- **Recommended**:
  - KPI-5 (comparative-tick).
  - COMP-3 (metric-vs-benchmark).
  - MICRO-2 (card-lift-restrained).
  - NAV-2 (sticky-hide-on-scroll-down).
- **Banned**: KPI-3 live-counter (overshoots into product register),
  MICRO-3 magnetic on body content (only on hero CTA).

### Medical (clinic · family · specialist · wellness)

- **Default gravity**: G1 (institutional).
- **Recommended (across all 4 sub-archetypes)**:
  - EVID-2 (attestation-chip on credentials).
  - QUOTE-3 (single-quote-with-portrait).
  - MICRO-1 + MICRO-2 (hairline + restrained-lift).
- **Specialist-only**: COMP-1 (before-after-slider with consent), QUOTE-6
  (peer-citation).
- **Family-only**: SCROLL-2 (staggered-reveal · gentle).
- **Banned across medical**: G5 sprint, MICRO-3 magnetic, MEDIA-2 parallax,
  KPI-3 live-counter.

### Restaurant (fine · trattoria · street)

- **Default gravity per archetype**:
  - fine = G2 + G6 (course-indexed editorial · cinematic plate reveal).
  - trattoria = G1 (warm institutional · static).
  - street = G5 (sprint-shape).
- **Fine recommended**: MEDIA-1 (course image fade-in), TIME-5 (chapter-stepper
  for course progression).
- **Street allowed**: NAV-3 (progress-bar), MICRO-2 (card-lift on order-grid).
- **Street banned**: countdown timers (manipulative SaaS · always banned).

### E-commerce (artisan · fashion-editorial)

- **Default gravity per archetype**:
  - artisan = G1 + G2 (editorial-warm).
  - fashion-editorial = G6 (cinematic).
- **Recommended**: MEDIA-3 (image-grid-stagger), MEDIA-6 (lightbox), MICRO-2
  (card-lift), CASE-6 (filterable-grid).
- **Banned across e-commerce**: scarcity-timers, "people viewing now",
  exit-intent (the manipulative SaaS class · always banned).

### Startup-saas-landing (Elevate)

- **Default gravity**: G5 (sprint-console).
- **Recommended**: KPI-3 (live-counter), NAV-2 + NAV-3, MICRO-3 (magnetic on
  hero CTA), MEDIA-3 (image-grid-stagger on feature-grid).
- **Banned**: countdown urgency, autoplay video bg (decorative · banned),
  exit-intent.

---

## §4 · Personalization knobs (end-user side)

Cross-cutting summary of what end-users (template customers) can configure.

### Tier 1 · per-template motion intensity (cluster-default · single switch)
- Values: `minimal` · `standard` · `expressive`.
- `minimal` = G3-equivalent regardless of cluster's default gravity.
- `standard` = cluster's declared default gravity.
- `expressive` = cluster's declared maximum gravity (only for G5/G6 clusters
  that have an "expressive" tier).
- **Default**: `standard`.
- **Auto-override**: if `prefers-reduced-motion: reduce` is detected at OS level,
  every animation falls back to its reduced-motion equivalent (per §2.12).

### Tier 2 · per-section enable/disable
For specific patterns: KPI-2 count-up · NAV-3 progress-bar · MICRO-2 card-lift ·
MICRO-6 cursor-vignette. Each can be turned off without breaking the page.

### Tier 3 · pattern parameter knobs
For specific patterns: count-up duration · stagger gap · range-fill speed.
End-user picks from a discrete set (200/250/300ms) NOT a free numeric input
(prevents janky values).

### Tier 4 · live-data backend hookup (G5 only)
KPI-3 live-counter requires a backend feed. End-user can plug in a URL
or use a pre-validated catalog of feed types (sprint-status · uptime · MAU ·
active-mandate count).

### Tier 5 · global accessibility
- `prefers-reduced-motion` honored automatically.
- `prefers-color-scheme: dark` (future tier 6 work · dark-mode variants per
  cluster — NOT in scope this pass).
- Locale auto-switch with consent.

The orchestrator should NOT expose Tier 4 knobs as default because mis-wired
backends break trust; require explicit ops-level configuration.

---

## §5 · The 12 most valuable patterns to introduce first

Ordered. Implementation priority list for Phase X.7b.

1. **Motion gravity DNA dimension** — `motion_profile: g1 | g2 | g3 | g4 | g5 | g6`
   added to `apps/catalog/template_dna.py · TEMPLATE_DNA[<slug>]`. Single
   field. Drives all subsequent enable/disable.
2. **KPI-2 `count-up-on-view`** — single-pattern win. Can be added to every
   existing corporate-suite KPI band with one IntersectionObserver wire.
   Immediately makes 5 templates feel less static.
3. **EDIT-1 + SCROLL-2 codified** — the existing default fade-in and stagger
   patterns get formalized into a `cs-anim` utility class with documented
   thresholds. Today they exist via `[data-lm]` but are under-documented.
4. **MICRO-2 `card-lift-restrained`** — single hover affordance. Adds "this
   responds to me" without changing the cluster register. Recommended for
   LF-1 / LF-3 / LF-4 / G5.
5. **EVID-2 `attestation-chip-hover`** — first-class affordance for credentials.
   Every corporate-suite sibling has Albo IDs; this gives them interactive
   verification without leaving the page.
6. **NAV-1 `sticky-condensed-on-scroll`** — already shipped on LF-5 (Continua).
   Extending to LF-1/LF-3/LF-4 makes the chrome feel modern without changing
   the editorial register.
7. **EDIT-4 `sticky-side-rail-anchor-active`** — already shipped on LF-2
   (Cornice/Causa narrative). Codify and document.
8. **CASE-6 `filterable-grid-with-chips`** — opens a dynamic affordance to the
   case-list page (NOT home). Adds interaction without compromising the
   home's editorial register.
9. **MEDIA-3 `image-grid-stagger-reveal`** — generic enough to use across
   cluster (case-list · service-list · product-grid future). Single-implementation
   reusability.
10. **EVID-1 `progressive-disclosure-tap`** — opens the door for evidence-led
    expansion (Causa · audit-led · medical-specialist). Single-implementation
    pattern with high semantic value.
11. **NAV-3 `scroll-progress-bar-thin`** — minimal cost · maximal "real product"
    signal. Allowed in LF-2 long-narrative second-occupant + every G5 cluster.
12. **MICRO-3 `magnetic-button-restrained`** — for the eventual G5 sprint-console
    cluster (Phase X.7a's likely candidate · agency-digital-studio). Single
    hero CTA affordance. Defines the cluster's "feels alive" signature without
    imposing on any other cluster.

These 12 are ordered by **lowest implementation friction × highest user-signal
impact**. The first 5 are zero-risk additions to the existing corporate-suite
contract. The next 7 are clean per-cluster opt-ins.

---

## §6 · The 5 patterns that most increase perceived distinction between siblings

Ordered. These five do the heaviest lifting against the audit's "samey" signal.

1. **TIME-2 / TIME-3 / TIME-4 timeline shape variation** — picking
   scroll-driven (G2/G4) vs horizontal-tick (G2) vs concentric-rings (G4)
   gives three structurally different time-progression shapes. Two siblings
   in the same family can both ship a timeline and read as different.
2. **CASE-5 numbered-ledger vs CASE-1 magazine-grid vs CASE-6 filterable-grid**
   — three case-preview shapes that have NEVER been mixed in the same cluster.
   A 2nd LF-2 occupant that picks `numbered-ledger` over `magazine-grid` reads
   different from Cornice without leaving LF-2.
3. **EVID-3 case-citation-pop vs EVID-1 progressive-disclosure-tap** —
   different evidence-revelation behaviors that read different at the
   interaction layer. Causa using EVID-3 (Cassazione case-pop) while Cornice
   uses EVID-1 (architectural-thesis disclosure) is two LF-2 siblings reading
   structurally different.
4. **QUOTE-4 sticky-stack-rotate vs QUOTE-1 editorial-pull-quote-static** —
   inserting QUOTE-4 in a 2nd LF-2 occupant's narrative gives a 3rd reveal
   shape distinct from Cornice's static pull-quotes.
5. **NAV-1 vs NAV-2 vs NAV-3 navbar behavior** — sticky-condensed (LF-5
   default) vs sticky-hide-on-scroll-down (G5) vs scroll-progress (G5/G2-light)
   produce three structurally different chrome experiences. A 2nd corporate-
   suite cluster sibling that adopts NAV-2 lightly reads structurally
   different from the existing 6 — without leaving the cluster register.

These five are *within-cluster* distinction unlocks. They do NOT require a
new cluster · they make the existing cluster's siblings tonally separable.

---

## §7 · The 5 patterns that most increase "this is a real product, not a
static theme"

Ordered. These five are the strongest "real product" tells.

1. **KPI-3 `live-counter`** (G5 only) — the single strongest tell. A KPI
   that updates with a backend feed reads as "this is alive · backed by real
   data". Restricted to G5 clusters but very high-impact there.
2. **CASE-6 `filterable-grid-with-chips`** — interactive grid that responds
   to the visitor reads as "this is an app, not a brochure". Adds genuine
   interactivity without compromising premium register.
3. **EVID-1 + EVID-2 + EVID-3 progressive-disclosure suite** — content that
   reveals on demand reads as "this is information-dense and considerate".
   Static brochures don't have on-demand depth; products do.
4. **NAV-3 `scroll-progress-bar-thin`** — single 1px hairline at top of
   viewport. Reads as "this site is paying attention to where I am". Very
   common in modern product surfaces; conspicuously absent in the corporate-
   suite cluster.
5. **MEDIA-5 + MEDIA-6 `gallery-strip-snap` + `lightbox-preserve-context`**
   — interactive gallery with keyboard navigation reads as "this is a real
   product designed for people who want to look at images, not just a
   page that happens to have images". Restricted to G6 cinematic clusters
   but high-impact there.

The list is shorter than the previous lists by design — these five are the
strongest single signals. Adding any one of them measurably shifts the
"feels alive" perception. Adding two or three (in the right cluster combination)
crosses the threshold from "static premium theme" to "premium product".

---

## §8 · Implementation note (out of scope this pass)

Phase X.7b implementation pass should:

1. Add `motion_profile` field to `apps/catalog/template_dna.py · TEMPLATE_DNA`.
   Default value per existing slug: derive from cluster (G3 for Pragma/Fiscus/
   Causa · G2 for Cornice/Causa-narrative · G4 for Continua · etc.).
2. Create `templates/_partials/animations/` partials per pattern, scoped by
   `motion_profile`.
3. Extend `static/js/live-motion.js` to honor `motion_profile` per template.
4. Add a `cs-anim-*` utility class set documented in
   `factory/standards/corporate-suite-design-standard.md §13` (new section).
5. Add browser-rubric checks for each pattern: `BRWS-MOTION-01..N` — does
   the pattern fire? Does it respect reduced-motion? Does it ONE-time?
6. Update `corporate-suite-distinctness-matrix.md §1.11` (motion row) to
   reflect the new gravity options instead of "motion is a cluster invariant".
7. Update `corporate-suite-quality-scorecard.md` to score motion fitness
   per cluster default vs declared.

These steps are out of scope for this paper-only pass. They are listed so
the next pass has a launch plan.

---

## §9 · One-paragraph summary

The factory has shipped six corporate-suite siblings under one motion vocabulary
(`quiet-editorial` · text fade-in + staggered reveals + marquee 110s OR none),
which the user correctly senses as "not dynamic enough." The DNA registry
already encodes hero / nav / footer / card / button / tone variety but does
not encode motion — there is no `motion_profile` field on `TEMPLATE_DNA`. This
library defines six motion gravities (G1 safe-premium · G2 editorial · G3
institutional · G4 stewardship-restrained · G5 sprint-console · G6 gallery-
cinematic), names 48 specific patterns across 12 families, gives each pattern
9 fields including reduced-motion equivalent + cluster fit + anti-clone notes,
maps every cluster to a recommended pattern set, and bans two motion classes
outright (decorative · manipulative-SaaS). Twelve patterns are recommended
for first-pass implementation (top 5 are zero-risk corporate-suite additions).
Five patterns specifically increase sibling distinction within a cluster (timeline-
shape variation · case-shape variation · evidence-revelation variation ·
quote-shape variation · navbar-behavior variation). Five patterns specifically
signal "real product not static theme" (live-counter · filterable-grid ·
progressive-disclosure · scroll-progress · gallery-lightbox). Implementation
is Phase X.7b · separate brief · paper here is sufficient to launch.
