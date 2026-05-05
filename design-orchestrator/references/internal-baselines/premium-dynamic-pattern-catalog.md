# Premium dynamic pattern catalog

```yaml
file_type:    internal-baseline · planner reference · table-driven catalog
status:       v1 · paper-only · paired with `premium-dynamic-pattern-library.md`
                (the comprehensive library) and `dynamic-pattern-usage-rules.md`
                (the rule book)
date:         2026-05-05
audience:     orchestrator at intake · planner at workflow A.1 · style-critic
                at A.6 · browser-verifier at workflow C/D walk
purpose:      single-page reference the planner reads at every intake to pick
                the dynamic-pattern set for the new sibling
companion:    factory/reports/hardening/premium-dynamic-pattern-library.md
                (full 9-field spec per pattern · this catalog is the index)
              design-orchestrator/references/internal-baselines/
                dynamic-pattern-usage-rules.md (when each is allowed · §
                decision triggers · gating)
              design-orchestrator/references/internal-baselines/
                template-factory-capability-gap-map.md (capability axes ·
                axis 3 motion · this catalog instantiates the missing axis)
maintenance:  monotonically extended at every new cluster ship · never
                truncated · every new pattern adds a row · every retired
                pattern keeps its row marked DEPRECATED with a date and a
                pointer to the replacement
```

---

## §1 · The six motion gravities (the register)

| Gravity | Tone read | Cluster default | Cluster fit | Cluster no-fit |
|---|---|---|---|---|
| **G1** safe premium | "alive but composed" | corporate-suite LF-1/3/4 | corporate-suite, lawyer, medical-clinic, real-estate-mass-market | agency-digital-studio, startup-saas |
| **G2** editorial | "publication, not website" | corporate-suite LF-2 | corporate-suite LF-2, agency-creative-studio, restaurant-fine, real-estate-luxury | corporate-suite LF-1/3/4, medical, e-commerce |
| **G3** institutional | "every animation is paid for by purpose" | corporate-suite Pragma · Fiscus · Causa | corporate-suite institutional, lawyer-classic-gold, family-office | portfolio, e-commerce, restaurant-street, startup-saas |
| **G4** stewardship-restrained | "this firm holds something across time" | corporate-suite LF-5 (Continua) | corporate-suite LF-5, lawyer-classic-gold (heavier register), medical-specialist, family-office | clusters with active audience verb |
| **G5** sprint-console | "this product ships" | agency-digital-studio (Aura) | agency-digital-studio, startup-saas, lawyer-modern-transparent (light-touch only) | corporate-suite, lawyer-classic-gold, medical-specialist, real-estate-luxury |
| **G6** gallery-cinematic | "this site is a slow film" | portfolio-cinematic | portfolio-cinematic, real-estate-ultra-luxury, agency-creative-studio (lighter touch), restaurant-fine, e-commerce-fashion-editorial | corporate-suite, medical, lawyer, startup-saas |

**Banned at archetype level (any cluster)**: decorative motion (no semantic
purpose), manipulative SaaS motion (designed to override visitor judgement).

---

## §2 · The 12 pattern families · index

| # | Family | Patterns | Library §ref |
|---|---|---|---|
| 1 | KPI / count-up | KPI-1 tabular-static · KPI-2 count-up-on-view · KPI-3 live-counter · KPI-4 range-fill · KPI-5 comparative-tick | §2.1 |
| 2 | Timeline / progression | TIME-1 static-vertical · TIME-2 scroll-driven · TIME-3 chronological-tick · TIME-4 stewardship-rings · TIME-5 chapter-stepper | §2.2 |
| 3 | Evidence / proof reveal | EVID-1 progressive-disclosure-tap · EVID-2 attestation-chip-hover · EVID-3 case-citation-pop · EVID-4 audit-trail-arrow · EVID-5 provenance-tooltip-image | §2.3 |
| 4 | Media block | MEDIA-1 cinematic-fade · MEDIA-2 parallax-restrained · MEDIA-3 image-grid-stagger · MEDIA-4 before-after-drag-slider · MEDIA-5 gallery-strip-snap · MEDIA-6 lightbox-preserve-context | §2.4 |
| 5 | Hover / focus / microinteraction | MICRO-1 hairline-on-hover · MICRO-2 card-lift-restrained · MICRO-3 magnetic-button · MICRO-4 text-underline-grow-from-left · MICRO-5 accent-glow-focus-ring · MICRO-6 cursor-vignette | §2.5 |
| 6 | Editorial motion | EDIT-1 text-fade-staggered · EDIT-2 pull-quote-em-reveal · EDIT-3 drop-cap-stagger · EDIT-4 sticky-side-rail · EDIT-5 magazine-page-flip (BANNED) | §2.6 |
| 7 | Navigation behavior | NAV-1 sticky-condensed · NAV-2 sticky-hide-on-scroll-down · NAV-3 scroll-progress-bar · NAV-4 breadcrumb-persistent · NAV-5 locale-pill-with-flag (limited) · NAV-6 scroll-position-memory | §2.7 |
| 8 | Comparison / scenario | COMP-1 = MEDIA-4 · COMP-2 scenario-tab-switcher · COMP-3 metric-vs-benchmark-chip · COMP-4 case-vs-baseline-narrative | §2.8 |
| 9 | Quote / testimonial | QUOTE-1 editorial-pull-quote · QUOTE-2 quote-carousel-restrained · QUOTE-3 single-quote-with-portrait · QUOTE-4 quote-stack-sticky-rotate · QUOTE-5 attribution-rich-quote · QUOTE-6 peer-citation-named-industry | §2.9 |
| 10 | Case-study preview | CASE-1 magazine-grid-3+1 · CASE-2 list-row-stagger · CASE-3 = TIME-1 · CASE-4 = MEDIA-5 · CASE-5 numbered-ledger · CASE-6 filterable-grid-with-chips · CASE-7 case-card-reveal-inline | §2.10 |
| 11 | Scroll choreography | SCROLL-1 = EDIT-1 · SCROLL-2 staggered-reveal-multi-card · SCROLL-3 sticky-pin-narrative · SCROLL-4 = MEDIA-5 · SCROLL-5 = MEDIA-2 · SCROLL-6 scroll-velocity-aware-fade | §2.11 |
| 12 | Reduced-motion safe equivalents | one per pattern above (per §2.12 of library) | §2.12 |

**Total: 48 named patterns · 7 cross-listings · 1 explicit BAN.**

---

## §3 · Pattern × gravity matrix (which gravity each pattern belongs to)

| Pattern | G1 | G2 | G3 | G4 | G5 | G6 |
|---|---|---|---|---|---|---|
| KPI-1 tabular-static | ✓ default | ✓ | ✓ | ✓ | ✓ | ✓ |
| KPI-2 count-up-on-view | ✓ | ✓ | ✓ | — | ✓ | — |
| KPI-3 live-counter | — | — | — | — | ✓ | — |
| KPI-4 range-fill | ✓ | — | ✓ | — | ✓ | — |
| KPI-5 comparative-tick | ✓ | — | — | — | ✓ | — |
| TIME-1 static-vertical | — | — | ✓ | ✓ default | — | — |
| TIME-2 scroll-driven | — | ✓ | — | ✓ 2nd-occupant | — | — |
| TIME-3 chronological-tick | — | ✓ | — | — | — | — |
| TIME-4 stewardship-rings | — | — | — | ✓ | — | — |
| TIME-5 chapter-stepper | — | ✓ | — | — | — | ✓ |
| EVID-1 disclosure-tap | ✓ | — | ✓ | — | — | — |
| EVID-2 attestation-chip | ✓ | ✓ | ✓ | ✓ | — | — |
| EVID-3 case-citation-pop | — | — | ✓ | — | — | — |
| EVID-4 audit-trail-arrow | ✓ | — | ✓ | ✓ | — | — |
| EVID-5 provenance-tooltip | — | ✓ | — | — | — | ✓ |
| MEDIA-1 cinematic-fade | — | — | — | — | — | ✓ default |
| MEDIA-2 parallax-restrained | — | — | — | — | — | ✓ (hero only) |
| MEDIA-3 image-grid-stagger | — | ✓ | — | — | ✓ | ✓ |
| MEDIA-4 before-after-slider | ✓ | — | — | — | — | ✓ |
| MEDIA-5 gallery-snap | — | — | — | — | — | ✓ default |
| MEDIA-6 lightbox-preserve | — | — | — | — | — | ✓ default |
| MICRO-1 hairline-hover | ✓ default | ✓ default | ✓ default | ✓ default | ✓ | ✓ |
| MICRO-2 card-lift | ✓ | — | ✓ | — | ✓ | — |
| MICRO-3 magnetic-button | — | — | — | — | ✓ (hero CTA only) | — |
| MICRO-4 text-underline-grow | ✓ | ✓ default | — | — | — | — |
| MICRO-5 focus-ring | ✓ inv. | ✓ inv. | ✓ inv. | ✓ inv. | ✓ inv. | ✓ inv. |
| MICRO-6 cursor-vignette | — | — | — | — | — | ✓ (dark hero only) |
| EDIT-1 fade-stagger | ✓ default | ✓ default | ✓ | ✓ | ✓ | ✓ |
| EDIT-2 pull-quote-em | — | ✓ | — | — | — | — |
| EDIT-3 drop-cap-stagger | — | ✓ | — | — | — | — |
| EDIT-4 sticky-side-rail | — | ✓ default | — | — | — | — |
| EDIT-5 page-flip | — | BAN | — | — | — | — |
| NAV-1 sticky-condensed | ✓ | ✓ 2nd-occupant | ✓ | ✓ default | — | — |
| NAV-2 sticky-hide-on-scroll | ✓ | — | — | — | ✓ | — |
| NAV-3 progress-bar-thin | — | ✓ light-touch | — | — | ✓ | — |
| NAV-4 breadcrumb-persistent | ✓ | — | ✓ | — | — | — |
| NAV-5 locale-pill-flag | — | — | — | — | ✓ limited | ✓ limited |
| NAV-6 scroll-position-memory | ✓ consent | ✓ consent | — | — | — | — |
| COMP-2 scenario-tab | ✓ | — | — | — | ✓ | — |
| COMP-3 metric-vs-benchmark | ✓ | — | — | — | ✓ | — |
| COMP-4 case-vs-baseline | ✓ | — | ✓ | — | — | — |
| QUOTE-1 editorial-pull-quote | ✓ default | ✓ default | ✓ default | ✓ | — | — |
| QUOTE-2 carousel-restrained | ✓ | — | — | — | ✓ | — |
| QUOTE-3 single-with-portrait | ✓ | — | ✓ | ✓ | — | — |
| QUOTE-4 sticky-stack-rotate | — | ✓ 2nd-occupant | — | — | — | ✓ |
| QUOTE-5 attribution-rich | ✓ | ✓ | ✓ | ✓ | — | — |
| QUOTE-6 peer-citation | — | — | ✓ | ✓ | — | — |
| CASE-1 magazine-3+1 | — | ✓ default | — | — | — | — |
| CASE-2 list-row-stagger | ✓ default | — | ✓ | — | ✓ | — |
| CASE-5 numbered-ledger | — | ✓ | ✓ | — | — | — |
| CASE-6 filterable-grid | ✓ | — | — | — | ✓ | — |
| CASE-7 card-reveal-inline | ✓ | — | ✓ | — | — | — |
| SCROLL-2 staggered-multi-card | ✓ default | ✓ default | ✓ | ✓ | ✓ | ✓ |
| SCROLL-3 sticky-pin-narrative | — | ✓ default | — | — | — | — |
| SCROLL-6 velocity-aware-fade | ✓ inv. | ✓ inv. | ✓ inv. | ✓ inv. | ✓ inv. | ✓ inv. |

**Legend**:
- `default` = the cluster's default at this gravity ships this pattern.
- `2nd-occupant` = recommended differentiator for a 2nd same-family sibling.
- `inv.` = cluster invariant — every cluster ships this regardless of gravity.
- `BAN` = explicitly banned · NEVER allowed.
- `(...)` = constrained scope (e.g., hero CTA only, dark hero only, with consent).
- `light-touch` = allowed only in subdued form.
- `limited` = allowed only in specific clusters.

---

## §4 · Cluster × pattern matrix (recommended set per cluster)

Quick-look. The planner reads the row for the new sibling's cluster.

### corporate-suite Pragma · Fiscus · Solaria (LF-1/3/4 · gravity G1+G3)
- **Default-ship**: KPI-1, EDIT-1, SCROLL-2, MICRO-1, MICRO-5, NAV-1 (cluster
  invariant), QUOTE-1, CASE-2.
- **Recommended add**: KPI-2 (count-up · 1× per home), EVID-2 (attestation-chip
  on Albo IDs), EVID-4 (audit-trail-arrow), MICRO-2 (card-lift on case-rows),
  NAV-1 (sticky-condensed extending from LF-5).
- **Allowed**: COMP-2 (scenario-tabs on pricing), QUOTE-3 (single-with-portrait),
  CASE-7 (card-reveal-inline · for case-list page).
- **Banned**: KPI-3, KPI-4, MICRO-3, MICRO-4, MICRO-6, MEDIA-2, MEDIA-6,
  EDIT-5, NAV-3, NAV-5, QUOTE-2, TIME-3, TIME-4, EDIT-2, EDIT-3, EDIT-4.

### corporate-suite Cornice · Causa (LF-2 · gravity G2)
- **Default-ship**: KPI-1, EDIT-1, EDIT-2, EDIT-3, EDIT-4, MICRO-1, MICRO-4,
  MICRO-5, SCROLL-3, CASE-1, EVID-5, QUOTE-1, NAV-1.
- **Recommended add for 2nd LF-2 occupant**: TIME-3 (chronological-tick),
  TIME-5 (chapter-stepper), QUOTE-4 (sticky-stack-rotate).
- **Allowed**: NAV-3 (light-touch progress bar in long narratives only),
  COMP-4 (case-vs-baseline-narrative), MEDIA-3 (image-grid-stagger).
- **Banned**: KPI-3, KPI-4 (range-fill reads infographic in editorial),
  KPI-5 (no comparator register), MICRO-2 (LF-2 cards stay still), MICRO-3,
  MICRO-6, MEDIA-2, MEDIA-6 (cinematic gallery breaks editorial),
  EDIT-5 (always banned), NAV-2, NAV-5, NAV-6, QUOTE-2, COMP-2 (no scenario-tab
  reading in editorial), TIME-4 (rings only in stewardship register).

### corporate-suite Continua (LF-5 · gravity G4)
- **Default-ship**: KPI-1, EDIT-1, MICRO-1, MICRO-5, SCROLL-2, NAV-1, QUOTE-1,
  TIME-1.
- **Recommended add for 2nd LF-5 occupant**: TIME-2 (scroll-driven-timeline),
  TIME-4 (stewardship-rings), QUOTE-6 (peer-citation), EVID-2.
- **Allowed**: EVID-1 (governance-disclosure), EVID-4 (audit-trail-arrow),
  COMP-3 (metric-vs-benchmark with citations).
- **Banned**: KPI-2 (count-up · stewardship register prefers stillness even
  on KPIs), KPI-3, KPI-4, KPI-5, MICRO-2 (cards stay still), MICRO-3, MICRO-4
  (text-grow reads editorial · stewardship is more restrained), MICRO-6,
  MEDIA-2, MEDIA-6, EDIT-2, EDIT-3, EDIT-5, NAV-2, NAV-3, NAV-5, QUOTE-2,
  QUOTE-4, COMP-2, CASE-6.

### agency-digital-studio · Aura (gravity G5)
- **Default-ship**: KPI-3 (live-counter · the cluster's signature), NAV-2
  (sticky-hide-on-scroll), NAV-3 (scroll-progress), MICRO-2 (card-lift),
  MICRO-3 (magnetic-button on hero CTA), MICRO-5, EDIT-1, SCROLL-2.
- **Recommended add**: KPI-5 (comparative-tick), COMP-3 (metric-vs-benchmark),
  MEDIA-3 (image-grid-stagger).
- **Allowed**: KPI-2 (count-up · pre-arrival to live-counter), CASE-2 list-row,
  CASE-6 (filterable-grid).
- **Banned**: KPI-4 (range-fill reads dashboard in this register), TIME-1/2/3/4,
  MEDIA-1, MEDIA-2, MEDIA-6, MICRO-4, MICRO-6, EDIT-2, EDIT-3, EDIT-4, EDIT-5,
  NAV-1 (G5 nav stays fixed for usability), QUOTE-1 (carousel preferred for G5
  testimonial register), QUOTE-3, QUOTE-4, QUOTE-6, COMP-4, CASE-1, CASE-5.

### agency-creative-studio · Vertex (gravity G2)
- **Default-ship**: as Cornice/Causa LF-2 (G2 default set).
- **Recommended add**: CASE-5 (numbered-ledger · canonical for editorial-
  agency), EVID-5 (provenance-tooltip), TIME-3.
- **Banned**: most G5 patterns (sprint clashes with editorial register).

### portfolio-cinematic · Pixel (gravity G6)
- **Default-ship**: MEDIA-1 (cinematic-fade), MEDIA-2 (parallax-hero),
  MEDIA-3, MEDIA-5 (gallery-snap), MEDIA-6 (lightbox), MICRO-1, MICRO-5,
  MICRO-6 (cursor-vignette · dark hero), SCROLL-2, EDIT-1.
- **Recommended add**: NAV-3 (subtle progress for long galleries),
  EVID-5 (provenance/EXIF).
- **Banned**: G3 institutional patterns, KPI-3, MICRO-3, NAV-2, NAV-4,
  EDIT-2, EDIT-3, EDIT-5, COMP-*, QUOTE-2/3/4/6, CASE-1/2/5/6/7.

### portfolio-editorial-designer-grid · Chiara (gravity G2)
- Inherits Vertex recommendations · CASE-5 numbered-ledger is canonical.

### real-estate-ultra-luxury (gravity G6 + G2)
- **Default-ship**: as portfolio-cinematic for hero · plus EDIT-2/3/4 for
  property-detail narrative.
- **Allowed**: MEDIA-4 (renovation-before/after with consent).

### real-estate-mass-market (gravity G1)
- **Default-ship**: as corporate-suite G1 default · plus CASE-6 (filterable-
  grid for listings) and MICRO-2 (card-lift for property cards).
- **Allowed**: NAV-5 (locale-pill-with-flag).
- **Banned**: G6 cinematic patterns.

### lawyer-classic-gold · Lex (gravity G3)
- **Default-ship**: KPI-1, EDIT-1, MICRO-1, MICRO-5, SCROLL-2, NAV-1, QUOTE-1,
  EVID-1, EVID-2, CASE-2.
- **Recommended add**: EVID-3 (case-citation-pop · forensic), EVID-4 (audit-
  trail-arrow), QUOTE-6 (peer-citation in legal press).
- **Banned**: G5 sprint, MICRO-3, MICRO-6, MEDIA-2, MEDIA-6, NAV-3, NAV-5,
  KPI-3, EDIT-5, QUOTE-2.

### lawyer-modern-transparent · Juris (gravity G1 with light G5)
- **Default-ship**: G1 default set.
- **Recommended add**: KPI-5 (comparative-tick), COMP-3 (metric-vs-benchmark),
  MICRO-2 (card-lift), NAV-2 (sticky-hide-on-scroll-down).
- **Allowed**: NAV-3 (scroll-progress · subtle).
- **Banned**: KPI-3, MICRO-3 on body content (hero CTA only).

### medical-clinic / family / specialist / wellness (gravity G1)
- **Default-ship across all 4**: G1 default set · plus EVID-2 (attestation-chip
  on credentials), QUOTE-3 (single-with-portrait).
- **Specialist-only**: COMP-1 (before-after with consent), QUOTE-6.
- **Family-only**: SCROLL-2 with gentler stagger.
- **Banned across medical**: G5 sprint, MICRO-3, MEDIA-2, KPI-3.

### restaurant-fine (gravity G2 + G6)
- **Default-ship**: G2 editorial set · MEDIA-1 (course image fade-in), TIME-5
  (chapter-stepper for course progression), CASE-1 (magazine-grid for
  signature-dishes).

### restaurant-trattoria-warm (gravity G1)
- **Default-ship**: G1 default · plus MICRO-2 (gentle card-lift on chalkboard
  daily-special), QUOTE-3.

### restaurant-street-modern (gravity G5)
- **Default-ship**: G5 sprint set · plus NAV-3 (progress) on order-flow.
- **Banned**: countdown timers, "limited time" badges, urgency overlays
  (manipulative SaaS · always banned).

### e-commerce-artisan · bottega (gravity G1 + G2)
- **Default-ship**: G2 editorial · plus MEDIA-3 (product-grid stagger),
  MEDIA-6 (lightbox), MICRO-2 (product-card lift), CASE-6 (filterable-grid).

### e-commerce-fashion-editorial · luxe (gravity G6)
- **Default-ship**: G6 cinematic · plus EVID-5 (provenance tooltip on photos).
- **Banned**: scarcity timers, "people viewing now", exit-intent (always banned).

### startup-saas-landing · elevate (gravity G5)
- **Default-ship**: G5 sprint set · KPI-3 (live-counter), NAV-2 + NAV-3,
  MICRO-3 (magnetic on hero CTA), MEDIA-3 (feature-grid stagger).
- **Banned**: countdown urgency, autoplay video bg, exit-intent.

---

## §5 · Personalization · what end-users configure

Five tiers per `premium-dynamic-pattern-library.md §4`:

| Tier | Knob | Default | End-user can change |
|---|---|---|---|
| 1 | per-template motion intensity | `standard` (cluster's gravity default) | yes — pick `minimal` · `standard` · `expressive` (latter only for G5/G6 clusters) |
| 2 | per-section enable/disable | per-pattern default | yes (toggle KPI-2 · NAV-3 · MICRO-2 · MICRO-6 · etc.) |
| 3 | pattern parameter knobs | discrete sets (200/250/300ms etc.) | yes — pick from preset list, NOT free numeric input |
| 4 | live-data backend hookup (G5) | disabled | yes — requires explicit ops config |
| 5 | global accessibility (`prefers-reduced-motion`) | OS-driven | no — automatic |

The orchestrator should NOT expose Tier 4 by default · it requires backend
configuration that breaks trust if mis-wired.

---

## §6 · Quick-look priority lists

Reproduced from library §5/§6/§7 for orchestrator at-intake reference:

### 12 highest-value patterns to introduce first (lowest implementation friction × highest impact)
1. `motion_profile` DNA dimension (the field itself).
2. KPI-2 count-up-on-view.
3. EDIT-1 + SCROLL-2 codified as `cs-anim` utilities.
4. MICRO-2 card-lift-restrained.
5. EVID-2 attestation-chip-hover.
6. NAV-1 sticky-condensed-on-scroll (extending from LF-5).
7. EDIT-4 sticky-side-rail (already on LF-2, codify).
8. CASE-6 filterable-grid-with-chips.
9. MEDIA-3 image-grid-stagger-reveal.
10. EVID-1 progressive-disclosure-tap.
11. NAV-3 scroll-progress-bar-thin.
12. MICRO-3 magnetic-button-restrained.

### 5 patterns that most increase sibling distinction
1. Timeline shape variation (TIME-2 / TIME-3 / TIME-4).
2. Case-preview shape variation (CASE-5 vs CASE-1 vs CASE-6).
3. Evidence-revelation variation (EVID-3 vs EVID-1).
4. Quote shape variation (QUOTE-4 vs QUOTE-1).
5. Navbar behavior variation (NAV-1 vs NAV-2 vs NAV-3).

### 5 patterns that signal "real product, not static theme"
1. KPI-3 live-counter (G5 only · highest single tell).
2. CASE-6 filterable-grid-with-chips.
3. EVID-1/2/3 progressive-disclosure suite.
4. NAV-3 scroll-progress-bar-thin.
5. MEDIA-5 + MEDIA-6 gallery-snap + lightbox.

---

## §7 · How the planner uses this catalog at intake

At workflow A.1 (intake) for a new sibling:

1. **Identify the cluster** of the new sibling. Look up the cluster's row
   in §4.
2. **Read the default-ship + recommended add + allowed + banned** lists for
   that cluster.
3. **For a 2nd-same-family-occupant** (e.g., 3rd LF-5 sibling), pick a
   pattern from the "2nd-occupant differentiator" line — this is the cell
   that produces sibling distinction without leaving the family.
4. **For a fresh cluster** (first hardening pass · Phase X.7a), declare the
   cluster's `motion_profile` and validate the pattern set against §3 (gravity
   matrix).
5. **For every pattern selected**, verify it is NOT on the BANNED list for
   that cluster.
6. **For every pattern selected**, copy its 9-field spec from
   `premium-dynamic-pattern-library.md` into the planner-brief content-module
   docstring (CS-EXEC-02 binding).
7. **Pass the brief to the builder** with the pattern set declared.

At workflow A.6 (review-lock), the style-critic verifies:
- declared patterns fired on the rendered home;
- reduced-motion equivalents work when `prefers-reduced-motion: reduce`
  is set;
- no banned patterns leaked from a different cluster's pattern set.

At workflow C/D (browser walk), the browser-verifier runs `BRWS-MOTION-*`
checks against each declared pattern.

---

## §8 · Maintenance protocol

- **Each new pattern is added to §2 (index) and §3 (gravity matrix) and §4
  (cluster recommendations) in the same edit pass.** Don't add a pattern
  to one section but not the others.
- **A pattern marked DEPRECATED stays in the catalog with date and pointer
  to replacement.** Never silently remove.
- **Each new cluster ship adds a row to §4.** The cluster's recommended set
  is declared at A.1 (planner intake) for that cluster's first sibling.
- **Each `BAN` entry is final unless a § decision review opens it.** The
  banned list is monotonic.
- **The catalog refreshes when a new motion gravity is needed.** New
  gravities are added at orchestrator-decision level (not mid-pass).

---

## §9 · One-paragraph summary

The factory has 6 motion gravities (G1 safe-premium · G2 editorial · G3
institutional · G4 stewardship-restrained · G5 sprint-console · G6 gallery-
cinematic), 12 dynamic-pattern families, 48 named patterns, 1 explicit BAN
(EDIT-5 magazine-page-flip), and 2 banned motion classes (decorative · 
manipulative-SaaS). Every pattern lives in exactly one gravity (or is a
cluster invariant). Every cluster has a recommended-set + allowed + banned
pattern list. Every pattern has a reduced-motion equivalent. Every end-
user-facing customization knob is enumerated with a default. The 12-pattern
implementation priority list is set; the 5 sibling-distinction patterns
and the 5 real-product patterns are named. Implementation is Phase X.7b ·
this catalog is the planner's at-intake reference for every sibling from
this point on.
