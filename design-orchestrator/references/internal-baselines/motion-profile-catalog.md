# Motion-profile catalog · planner-side reference

```yaml
file_type:    internal-baseline · planner reference · table-driven catalog
status:       v1 · paper-only · paired with the binding plan
                  `factory/reports/hardening/motion-profile-dna-plan.md`
                  and the comprehensive vocabulary
                  `factory/reports/hardening/premium-dynamic-pattern-library.md`
date:         2026-05-05
audience:     orchestrator at intake · planner at workflow A.1 · style-critic
                  at A.6 · browser-verifier at workflow C/D walk · release-
                  gatekeeper at workflow D flip
purpose:      single-page reference the planner reads at every intake to
                  declare the new sibling's motion_profile + bundle flags
                  and to score axis 18 vs every existing sibling
companion:    factory/reports/hardening/motion-profile-dna-plan.md (the
                  binding plan · 16 sections · anti-tacky red-lines ·
                  reduced-motion fallback · customization plan)
              factory/reports/hardening/premium-dynamic-pattern-library.md
                  (12 families · 48 named patterns · per-pattern 9-field
                  spec · this catalog is the index)
              factory/reports/hardening/anti-clone-2.0-rules.md §3 · §1
                  axis 18 (this catalog operationalises the critical-axis
                  veto)
              design-orchestrator/references/internal-baselines/
                  premium-dynamic-pattern-catalog.md (per-pattern × gravity
                  matrix)
              apps/catalog/template_dna.py · MOTION_PROFILES (the 7-key
                  registry on disk)
maintenance:  monotonically extended at every new cluster ship · never
                  truncated · profile rows stay; new flags are appended
                  with default False; deprecated patterns keep their flag
                  marked DEPRECATED with a date and a pointer to the
                  replacement
```

---

## §1 · The seven motion_profile values · canonical table

| key | canonical alias (planner brief) | feel (one-line) | gravity letter | bundle-flags-on (current registry) |
|---|---|---|---|---|
| `g1-safe-premium` | safe-institutional | "alive but composed" | G1 | none |
| `g2-editorial` | restrained-editorial | "publication, not website" | G2 | none |
| `g2-editorial-counter` | evidence-led-reactive | "publication that ALSO answers" | G2-with-G3-cell-borrowing | kpi_animate · nav_condense_on_scroll · evid5_provenance |
| `g3-institutional` | institutional-progressive | "every animation paid for by purpose" | G3 | kpi_animate |
| `g4-stewardship` | calm-architectural | "this firm holds something across time" | G4 | none |
| `g5-sprint-console` | sprint-product | "this product ships" | G5 | kpi_animate (paper-future: nav_hide_on_scroll · scroll_progress_bar · magnetic_button · live_data_kpi) |
| `g6-cinematic` | curatorial-cinematic | "this site is a slow film" | G6 | none (paper-future: hero_parallax · gallery_snap · cinematic_fade · cursor_vignette) |

The planner brief carries the **canonical alias**; code keeps the
**gravity-letter key**. Both names refer to the same row.

---

## §2 · The 12 declared bundle flags

| flag | pattern (library §) | wired today? | profiles that opt in (today) |
|---|---|---|---|
| `kpi_animate` | KPI-2 count-up-on-view (§2.1) | ✓ | g2-editorial-counter · g3-institutional · g5-sprint-console |
| `nav_condense_on_scroll` | NAV-1 sticky-condensed-on-scroll (§2.7) | ✓ | g2-editorial-counter · g4-stewardship (current Continua canonical) |
| `evid5_provenance` | EVID-5 provenance-tooltip-image (§2.3) | ✓ | g2-editorial-counter |
| `evid3_citation` | EVID-3 case-citation-pop (§2.3) | ✓ retrofit slice 02 | g2-editorial-counter |
| `time3_chronotick` | TIME-3 chronological-tick-horizontal (§2.6) | ✓ retrofit slice 02 | g2-editorial-counter |
| `card_lift_restrained` | MICRO-2 card-lift-restrained (§2.5) | ✓ Phase X.7b pass 1 | g1-safe-premium · g3-institutional · g5-sprint-console (paper opt-in · 0 templates flip today) |
| `cinematic_fade` | MEDIA-1 cinematic-fade (§2.4) | ✓ Phase X.7b pass 1 | g6-cinematic (cluster signature · 0 templates declared today · ready for Phase X.7a intake) |
| `nav_hide_on_scroll_down` | NAV-2 (§2.7) | paper | g5-sprint-console (declared) |
| `scroll_progress_bar` | NAV-3 (§2.7) | paper | g5-sprint-console (declared) |
| `hero_parallax` | MEDIA-2 parallax-restrained (§2.4) | paper | g6-cinematic (declared) |
| `gallery_snap` | MEDIA-5 gallery-strip-snap (§2.4) | paper | g6-cinematic (declared) |
| `magnetic_button` | MICRO-3 magnetic-button-restrained (§2.5) | paper | g5-sprint-console only |
| `cursor_vignette` | MICRO-6 cursor-vignette (§2.5) | paper | g6-cinematic (dark-hero only) |
| `live_data_kpi` | KPI-3 live-counter (§2.1) | paper · ops-gated | g5-sprint-console only · ops-config required |

Each flag maps to **exactly one named pattern**. A flag never enables two
patterns. A pattern never reads two flags. Adding a flag is purely
additive; default `False` for every profile that doesn't opt in.

---

## §3 · Per-cluster allowed-profile set · intake binding

The planner brief (`next-template-brief-schema.md §1`) MUST declare
`motion_profile` from the cluster's allowed set. Orchestrator rejects the
brief if the declared profile is outside the set.

| cluster | sub-cluster / family | allowed | default | within-cluster sibling claims |
|---|---|---|---|---|
| corporate-suite | LF-1 advisory | g3-institutional | g3 | Pragma claims |
| corporate-suite | LF-2 1st-occupant | g2-editorial | g2 | Cornice claims |
| corporate-suite | LF-2 2nd-occupant | g2-editorial-counter | g2-counter | Causa claims (within-family differentiator) |
| corporate-suite | LF-2 3rd-occupant | g2-editorial OR g2-editorial-counter | TBD intake | AC-V5 cumulative ladder check vs both prior occupants |
| corporate-suite | LF-3 fiscal | g3-institutional | g3 | Fiscus claims |
| corporate-suite | LF-4 coaching | g3-institutional | g3 | Solaria claims |
| corporate-suite | LF-5 stewardship | g4-stewardship | g4 | Continua claims |
| corporate-suite | LF-{NEW} 1st-occupant | g3-institutional · g1-safe-premium · g4-stewardship (per intake-declared register) | TBD intake | unclaimed |
| agency-creative-studio | Vertex / editorial-agency | g2-editorial · g6-cinematic (hero-only borrowing) | g2 | Vertex would claim g2 + cinematic-fade hero |
| agency-digital-studio | Aura / sprint-console | g5-sprint-console | g5 | Aura would claim g5 + live_data_kpi |
| portfolio-cinematic | Pixel | g6-cinematic | g6 | Pixel would claim g6 + gallery_snap + cursor_vignette |
| portfolio-editorial-grid | Chiara | g2-editorial | g2 | Chiara claims |
| real-estate-ultra-luxury | Villa | g6-cinematic | g6 | Villa claims |
| real-estate-mass-market | Casa | g1-safe-premium | g1 | Casa claims |
| lawyer-classic-gold | Lex | g3-institutional | g3 | Lex claims |
| lawyer-modern-transparent | Juris | g1-safe-premium · light-touch g5 patterns (NAV-2 · KPI-5 only · NEVER live-counter) | g1 | Juris claims |
| medical-clinic / family / wellness | Salute / Famiglia / Benessere | g1-safe-premium | g1 | claims · 3-template family closed |
| medical-specialist | Cardio / Derm | g4-stewardship · g3-institutional | g4 | Cardio + Derm claim · CASE-1 before-after with consent |
| restaurant-fine | Gusto | g2-editorial · g6-cinematic (course-image fade only) | g2 | Gusto claims |
| restaurant-trattoria | Sapore | g1-safe-premium | g1 | Sapore claims |
| restaurant-street-modern | Brace | g1-safe-premium · g5 patterns light-touch | g1-or-g5 | Brace claims · NEVER countdown timers |
| ecommerce-artisan | Bottega | g1-safe-premium · g2-editorial (warm) | g1 | Bottega claims · NEVER scarcity-timers |
| ecommerce-fashion-editorial | Luxe | g6-cinematic | g6 | Luxe claims |
| startup-saas-landing | Elevate | g5-sprint-console | g5 | Elevate claims · 1 single image surface only |

---

## §4 · Sibling-claim registry (corporate-suite live state · 2026-05-05)

The 6 corporate-suite siblings on disk + their declared motion_profile +
their bundle flag set. New corporate-suite siblings consult this table at
intake to confirm non-collision.

| sibling | template_slug | layout_family | motion_profile | bundle flags ON | sub-cluster |
|---|---|---|---|---|---|
| Pragma | pragma-corporate-suite | LF-1 | g3-institutional | kpi_animate | studio-direzionale-mandato |
| Cornice | cornice-architettura | LF-2 1st | g2-editorial | (none) | studio-architettura |
| Fiscus | fiscus-commercialista | LF-3 | g3-institutional | kpi_animate | studio-commercialista |
| Solaria | solaria-coaching | LF-4 | g3-institutional | kpi_animate | studio-coaching-percorso |
| Continua | continua-stewardship | LF-5 | g4-stewardship | nav_condense_on_scroll | studio-stewardship-fiduciario |
| Causa | causa-legale | LF-2 2nd | g2-editorial-counter | kpi_animate · nav_condense_on_scroll · evid5_provenance | studio-legale-cassazionista |

LF-1 / LF-3 / LF-4 / LF-5 are 1-occupancy. LF-2 is 2-occupancy. A 7th
corporate-suite sibling MUST land on a NEW layout family AND pick a
profile that scores ≥ 2 on axis 18 vs every row above. The existing 5
LF families' default profiles are taken; sibling 7 is structurally
constrained to either:
- A new LF family + `g3-institutional` (only safe if sibling 7 also
  diversifies imagery + audience-verb register vs Pragma/Fiscus/Solaria
  trio's grandfathered axis-18 collisions), OR
- A new LF family + a profile not yet claimed at corporate-suite cluster
  level (today: `g1-safe-premium` is the only unclaimed option within
  cluster).

Per `motion-profile-dna-plan.md §15`: a 7th corporate-suite sibling
cannot open today regardless of motion_profile choice; the S6 cluster-
tropes rule binds the ordering (Phase X.7a non-cs cluster ships first).

---

## §5 · Anti-clone 2.0 axis 18 scoring rubric · table-form

Score the pair on motion_profile + bundle flag count delta:

| profiles compared | flag-count delta | axis 18 score |
|---|---|---|
| identical profile + identical flag bundle | 0 | 0 |
| identical profile + 1-flag delta | 1 | 1 |
| identical profile + ≥3-flag delta | ≥3 | 2 |
| adjacent profile (g2 ↔ g2-counter · g3 ↔ g4) + any | any | 2 |
| structurally distinct profile (different gravity-letter family · e.g., g3 ↔ g6 · g2 ↔ g5) | any | 3 |

**Critical-axis veto floor**: 2 vs every other sibling.

The 4 documented Pragma/Fiscus/Solaria pairs (all `g3-institutional` with
identical 1-flag bundles) score 0; they are 2.0-grandfathered per
design-standard §19. NO new sibling may join the grandfather class.

---

## §6 · Per-profile safe pool + forbidden pool · planner quick-look

For each profile, what the planner is allowed to wire AND what is forbidden
even within the cluster's allowed set. (See `motion-profile-dna-plan.md §3`
for full prose; this is the lookup form.)

### `g1-safe-premium`

```
SAFE:        KPI-1 KPI-2 KPI-4 KPI-5 EVID-1 EVID-2 EVID-4 MEDIA-3-light MEDIA-4
             MICRO-1 MICRO-2 MICRO-5 EDIT-1 NAV-1 NAV-4 QUOTE-1 QUOTE-3 CASE-2
             CASE-6 SCROLL-2 SCROLL-6
FORBIDDEN:   parallax cinematic-fade cursor-vignette magnetic-button gallery-snap
             live-counter sticky-stack-rotate scroll-driven-timeline stewardship-
             rings scroll-progress-bar drop-cap-stagger sticky-side-rail
             page-flip
```

### `g2-editorial`

```
SAFE:        EDIT-1 EDIT-2 EDIT-3 EDIT-4 MICRO-1 MICRO-4 MICRO-5 QUOTE-1 CASE-1
             MEDIA-3-quick TIME-5
FORBIDDEN:   KPI-2 (LF-2 1st-occupant signature is static) parallax cursor-
             vignette magnetic-button scroll-progress-bar quote-carousel
             gallery-snap live-counter card-lift sticky-hide-on-scroll
             page-flip
```

### `g2-editorial-counter`

```
SAFE:        full g2-editorial pool PLUS KPI-2 NAV-1 EVID-2 EVID-3 EVID-5
             QUOTE-4 TIME-3
FORBIDDEN:   parallax cursor-vignette magnetic-button scroll-progress-bar
             gallery-snap live-counter cinematic-fade card-lift-on-magazine-grid
             page-flip
```

### `g3-institutional`

```
SAFE:        KPI-1 KPI-2 KPI-4-audit-only EVID-1 EVID-2 EVID-3-forensic EVID-4
             MICRO-1 MICRO-2 MICRO-5 EDIT-1 NAV-1 NAV-4 QUOTE-1 QUOTE-3 QUOTE-5
             CASE-2 CASE-5 CASE-7 COMP-2-pricing COMP-4
FORBIDDEN:   parallax cursor-vignette magnetic-button scroll-progress-bar
             cinematic-fade gallery-snap live-counter scroll-driven-timeline
             stewardship-rings sticky-stack-rotate drop-cap-stagger sticky-
             side-rail
```

### `g4-stewardship`

```
SAFE:        KPI-1 (forced static) TIME-1 TIME-2-2nd-occupant TIME-4-2nd-occupant
             EVID-1 EVID-2 EVID-4 MICRO-1 MICRO-5 EDIT-1 NAV-1 NAV-4 QUOTE-1
             QUOTE-3 QUOTE-5 QUOTE-6
FORBIDDEN:   KPI-2 KPI-3 KPI-4 MICRO-2 MICRO-3 MICRO-6 MEDIA-2 MEDIA-1 NAV-3
             NAV-2 gallery-snap sticky-stack-rotate drop-cap-stagger scroll-
             progress-bar
```

### `g5-sprint-console`

```
SAFE:        KPI-1 KPI-2 KPI-3 KPI-4 KPI-5 EVID-2 MICRO-1 MICRO-2 MICRO-3
             MICRO-5 EDIT-1 NAV-2 NAV-3 NAV-4 NAV-5 QUOTE-2 QUOTE-5 CASE-2
             CASE-6 COMP-2 COMP-3 MEDIA-3
FORBIDDEN:   parallax cursor-vignette cinematic-fade stewardship-rings scroll-
             driven-timeline drop-cap-stagger sticky-side-rail sticky-stack-
             rotate page-flip magazine-grid-3+1 (LF-2 only)
             countdown-urgency exit-intent autoplay-video-bg (manipulative-
             SaaS · always banned)
```

### `g6-cinematic`

```
SAFE:        MEDIA-1 MEDIA-2-hero-only MEDIA-3-slow MEDIA-4-when-semantic
             MEDIA-5 MEDIA-6 MICRO-1 MICRO-5 MICRO-6 EVID-5 EDIT-1 TIME-5
             QUOTE-1 QUOTE-4-with-discipline
FORBIDDEN:   KPI-2 KPI-3 KPI-4 KPI-5 NAV-3 NAV-2 magnetic-button card-lift
             scroll-driven-timeline stewardship-rings drop-cap-stagger sticky-
             side-rail filterable-grid-chips scenario-tab-switcher attestation-
             chip-hover countdown-urgency
```

---

## §7 · Anti-tacky red-lines · single-page checklist (per profile · for style-critic)

The style-critic walks this checklist at A.6 review-lock. Each line is a
binary YES (compliant) / NO (re-spec required).

```
CROSS-PROFILE (every profile honors)
  AT-X1  prefers-reduced-motion honored at JS root             [YES / NO]
  AT-X2  no decorative motion (information-test)               [YES / NO]
  AT-X3  no manipulative-SaaS motion (judgement-override test) [YES / NO]
  AT-X4  no once-per-session re-trigger on scroll-back         [YES / NO]
  AT-X5  total stagger ≤ 1500ms                                [YES / NO]

g1-safe-premium
  AT-G1-1  count-up ≤ 1 invocation per home                    [YES / NO]
  AT-G1-2  card-lift ≤ 3px · shadow blur ≤ 16px                [YES / NO]
  AT-G1-3  no parallax                                          [YES / NO]

g2-editorial
  AT-G2-1  no count-up                                          [YES / NO]
  AT-G2-2  drop-cap fades only · no drop-from-above             [YES / NO]
  AT-G2-3  pull-quote em-reveal delay 200ms · no flash          [YES / NO]
  AT-G2-4  no scroll-progress-bar                               [YES / NO]

g2-editorial-counter
  AT-G2C-1  count-up ≤ 1 invocation                             [YES / NO]
  AT-G2C-2  NAV-1 delta ≠ LF-5's 76→56 (use 84→64)              [YES / NO]
  AT-G2C-3  EVID-5 tooltip ≤ 240px · hover-only · no glint      [YES / NO]
  AT-G2C-4  no card-lift on magazine-grid 3+1                   [YES / NO]

g3-institutional
  AT-G3-1  one count-up per home · no live-counter              [YES / NO]
  AT-G3-2  hover affordances hairline-only on body content      [YES / NO]
  AT-G3-3  card-lift ≤ 3px · no tilt                            [YES / NO]
  AT-G3-4  no marquee beyond documented 110s sectors-marquee    [YES / NO]

g4-stewardship
  AT-G4-1  no count-up · no range-fill · no comparative-tick    [YES / NO]
  AT-G4-2  no card-lift on portrait cards · no accent-glow      [YES / NO]
  AT-G4-3  no icon animation · no emoji · no spinner            [YES / NO]
  AT-G4-4  timeline rings draw once then static                 [YES / NO]

g5-sprint-console
  AT-G5-1  live-counter cadence ≥ 8s                            [YES / NO]
  AT-G5-2  live-counter cites data source on hover              [YES / NO]
  AT-G5-3  magnetic range ≤ 30px · displacement ≤ 6px           [YES / NO]
  AT-G5-4  scroll-progress 1px exactly · no gradient · no pulse [YES / NO]
  AT-G5-5  no autoplay-video-bg · no countdown · no exit-intent [YES / NO]

g6-cinematic
  AT-G6-1  parallax HERO ONLY · single layer · disabled <880px  [YES / NO]
  AT-G6-2  cinematic-fade ≥ 1200ms · saturation start ≥ 0.85    [YES / NO]
  AT-G6-3  cursor-vignette dark-hero only · disabled on touch   [YES / NO]
  AT-G6-4  gallery-snap horizontal-only · keyboard navigable    [YES / NO]
  AT-G6-5  lightbox dark-with-alpha · scroll preserved          [YES / NO]
```

---

## §8 · Reduced-motion fallback · per profile (verifier checklist)

The browser-verifier walks every locale × viewport with both default-motion
AND `prefers-reduced-motion: reduce`. Below is the static-equivalent the
verifier expects under reduce.

| profile | reduced-motion expected behavior |
|---|---|
| g1-safe-premium | KPI numbers final-value at first paint · cards static border-color shift on hover · grid layout instant transition · staggered-reveal content visible at first paint |
| g2-editorial | text visible at first paint · italic-em visible with surrounding · drop-cap visible with paragraph · sticky-side-rail color transition unchanged · smooth-scroll → instant scroll |
| g2-editorial-counter | full g2-editorial behavior PLUS: count-up → static final number · NAV-1 → fixed condensed height from start · EVID-5 → static caption below image |
| g3-institutional | count-up → static final number · staggered-reveal content visible at first paint · NAV-1 → fixed condensed height · card-lift → static border-color shift |
| g4-stewardship | timeline static (already) · scroll-driven-timeline → static TIME-1 fallback · stewardship-rings drawn statically at first paint · attestation-chip tooltip without fade |
| g5-sprint-console | live-counter → static recent value with timestamp · magnetic-button disabled · NAV-2 nav stays sticky · NAV-3 unchanged (scroll-bound width is not animation) · MEDIA-3 grid static |
| g6-cinematic | cinematic-fade → image fully revealed at first paint · parallax → no offset · MEDIA-3 grid static · before-after-slider → side-by-side static · gallery-snap → regular horizontal scroll · lightbox unchanged · cursor-vignette disabled |

---

## §9 · Workflow gate verification · single-table summary

| gate | verifier | check | output |
|---|---|---|---|
| A.0 territory-scout | scout | likely motion_profile per cluster + family | scout report |
| A.1 intake | planner | brief declares motion_profile from cluster's allowed set + axis 18 matrix vs every existing sibling | brief field filled · matrix ≥ 2 cells per pair |
| A.2 plan | planner + style-critic | plan re-checks declared profile + bundle vs allowed + scores axis 18 | plan-gate decision · re-spec on veto fail |
| A.5 build | builder | DNA entry committed with motion_profile key + body data-attributes emitted | source-file diff |
| A.6 review-lock | style-critic | walks anti-tacky red-lines per profile (§7 above) | review-lock report cites profile + flag count + checklist YES count |
| Workflow C/D walk | browser-verifier | 5 locales × 5 viewports × default-motion AND reduced-motion both walks | walk-log per profile · screenshot pairs |
| Workflow D flip | release-gatekeeper | scores axis 18 vs every existing sibling · all 5 v2.0 critical-axis vetoes ≥ floor 2 | scorecard panel motion-profile-summary |

---

## §10 · Cross-references · canonical (every reader follows these)

- `factory/reports/hardening/motion-profile-dna-plan.md` — the 16-section
  binding plan · §1 enumerated values · §3 per-profile feel + safe pool ·
  §4 per-cluster allowed-set · §5 anti-tacky red-lines · §6 reduced-motion
  fallback · §7 axis 18 scoring · §9 customization plan · §15 sibling 7
  decision · §16 strongest conclusion.
- `factory/reports/hardening/premium-dynamic-pattern-library.md` — the
  comprehensive 12-family · 48-pattern vocabulary · per-pattern 9-field
  spec.
- `factory/reports/hardening/anti-clone-2.0-rules.md` — axis 18 critical-
  axis-veto · floor 2 vs every sibling · 6-class sameness vocabulary.
- `factory/reports/hardening/lf2-family-internal-variance-rules.md` —
  AC-V1 ≥3 sub-variant floor reads off the motion_profile bundle directly
  for LF-2.
- `factory/reports/hardening/causa-retrofit-slice-01.md` — the 3-flag
  bundle precedent · `g2-editorial-counter` shipped · 28/54 pair score
  achieved.
- `factory/reports/hardening/premium-dynamic-implementation-slice-01.md`
  — slice 01 narrative · what is on disk today.
- `factory/reports/hardening/template-personalization-architecture.md §2
  CS-12` — Layer-B motion preset · 3-tier intensity slider for Phase X.7c.
- `apps/catalog/template_dna.py` line 200 · `MOTION_PROFILES` registry on
  disk.
- `static/js/live-motion.js` — reduced-motion short-circuit at line 50 ·
  counter gate at line 152 · the working precedent for how a bundle flag
  gets honored at runtime.
- `factory/standards/corporate-suite-design-standard.md §21` (paper-pending
  this pass) — motion_profile DNA cell + cluster's allowed set bound to
  CS-LF2-VAR-V1 contract.
- `design-orchestrator/references/internal-baselines/next-template-brief-
  schema.md §1` (paper-pending this pass) — `motion_profile` row added to
  required-inputs intake table.
- `design-orchestrator/references/internal-baselines/corporate-suite-
  distinctness-matrix.md §1.11` (paper-pending this pass) — motion row
  rewritten as DNA cell + axis 18 scoring.

---

## §11 · One-paragraph summary

motion_profile is the 8th first-class template DNA dimension. Seven
enumerated values map the audit's six gravities (G1-G6) plus a within-LF-2
2nd-occupant differentiator (`g2-editorial-counter`). Twelve bundle flags
declare per-pattern enable/disable; three are wired today (kpi_animate ·
nav_condense_on_scroll · evid5_provenance) and nine are paper-flagged for
future implementation slices. Each cluster has a per-family allowed-profile
set; the planner declares one profile at A.1 intake from that set and the
orchestrator rejects any brief outside it. Every profile has a feel-statement
(one-line semantic anchor), a safe-pattern pool, a forbidden pool, anti-tacky
red-lines, and a reduced-motion fallback that the JS layer guarantees. The
6-pair anti-clone-2.0 axis-18 scoring rubric is operational; 11 of 15
corporate-suite pairs clear the v2.0 critical-axis veto under the new bundle,
and the 4 Pragma/Fiscus/Solaria failures are documented as 2.0-grandfathered.
Customer customization (Phase X.7c · Layer-B) maps the 7 internal profiles
to a 3-tier intensity slider per cluster, preserving variety through three
mechanisms: per-cluster preset narrowing, sibling-aware flag claims, and a
Layer-A reduced-motion floor that no customer setting can override. The
DNA axis is ready to bind future intakes today; sibling 7 of the factory
opens via Phase X.7a (a non-corporate-suite cluster) per the audit's S6
operational rule, regardless of how well a 7th corporate-suite sibling
would score on motion_profile alone.
