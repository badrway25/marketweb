# Personalization control-surface map

```yaml
file_type:    internal-baseline · planner reference · table-driven catalog
status:       v1 · paper-only · paired with the architecture doc and the
                safety-rules doc
date:         2026-05-05
audience:     orchestrator at every fork · planner at A.1 · editor-team
                at every X.7c slice · style-critic at A.6 · browser-verifier
                at workflow C/D walk
purpose:      single-page reference the orchestrator and editor-team read
                to know "for control X, what is its layer, what is its
                allowed range, what is its hidden constraint, what's the
                anti-collapse rule, and how do we preview-verify"
companion:    factory/reports/hardening/template-personalization-
                architecture.md (the system design · this catalog
                instantiates §2)
              design-orchestrator/references/internal-baselines/
                personalization-safety-rules.md (the rule book · this
                catalog cross-references its rule IDs)
              design-orchestrator/references/internal-baselines/
                premium-dynamic-pattern-catalog.md (motion patterns · this
                catalog references their personalization knobs)
              apps/projects/models.py (the existing Foundation v1 model
                · CURATED_FONTS = 20-Google-font list is the foundation)
maintenance:  monotonically extended at every new cluster ship · at every
                Layer B preset addition · at every Layer C toggle addition
                · never truncated
```

---

## §1 · The 4-layer model · index

| Layer | Visibility to user | Editable by user | Validation | Failure mode |
|---|---|---|---|---|
| **A** locked invariants | NOT shown · NOT a knob | impossible | static at standards | architectural |
| **B** curated presets | shown as picker (3-7 options) | pick one | preset-authoring time | preset never violates contract |
| **C** safe toggles | shown as switch / checkbox | on/off | runtime · always reversible | binary states both validated |
| **D** banned freeform | NOT shipped | impossible | rejected at architecture level | orchestrator refuses |

Target ratio per template: ~30% A · ~50% B · ~20% C · 0% D.

---

## §2 · The 17 control surfaces · table-driven map

Each row gives: control name · layer · allowed range · hidden constraint ·
likely misuse · anti-collapse rule · preview verification.

### CS-1 · Hero variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Hero geometry | A | locked at template's L1 (per CS-LAYOUT-01) | family identity | n/a (not exposed) | family contract enforced | n/a |
| Hero photo (slot 0) | C with validation | upload OR pick from sub-cluster pool | ≥1600 wide · 16:9 native preferred · CS-IMG-SRC-01 (Pexels-only when picking from pool) | upload of low-res selfie | smart-crop + quality warning · refuse upload if <1200 wide | preview pane re-renders hero · contrast check on h1 over photo |
| Hero meta-strip composition | B | per-cluster preset list (e.g., for corporate-suite Pragma: `(HQ · Equipe · Mandati)` · `(Sede · Albo · Anno)` · `(Foro · Iscrizione · Anno)`) | each preset pre-validated against L5 KPI placement | n/a (preset only) | sibling-aware: Cornice's hero-overlay tuple removed from picker for non-LF-2 siblings | preview KPI cells with chosen tuple |
| Hero CTA copy | B | per-cluster preset list (e.g., for Pragma: "Fissa una call privata" · "Apri un confronto strategico" · ...) | each preset cleared CS-CTA-02 (advisor's voice) + cluster's voice register | n/a | banned: "Buy now", "Limited offer" — Layer D | hero h1 + CTA juxtaposition checked for visual balance |
| Hero secondary CTA | C | on/off | when on, must point to a real route (CS-CTA-04) | linking to `#` placeholder | route-presence check at save | preview shows secondary CTA in hero |

### CS-2 · Section ordering variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Section sequence | A | locked at template's L2 (CS-LAYOUT-02) | family identity | reorder banned (D) | section-list immutable per family | renderer enforces via layout-family dispatcher |
| Optional sections per page | C | on/off per section (cluster-conditional) | minimum 4 sections on home (Layer A architectural floor) | hiding cases AND leadership AND KPI = page collapse | floor enforced at save | empty-state guards in renderer |
| Section reorderer | D | NOT SHIPPED | n/a | drag CTA to slot-1 | banned at architecture | n/a |

### CS-3 · Case-study display variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Case-preview shape | A · within family | locked at L7 per CS-LAYOUT-07 | family signature | n/a | family contract enforces | n/a |
| Sub-variant (when family allows) | B | per-cluster preset (e.g., G1 cluster on case-list page can pick CASE-2 list-row OR CASE-6 filterable-grid) | each variant pre-built and validated | n/a | family contract enforces | preview case-list page with chosen variant |
| Case count on home | C with bounds | 3-6 (CS-DENSITY-06) | enforced at save | 7+ (out of range) | save rejected with explanation | preview re-renders with chosen count |
| Per-case visibility | C | show/hide per case | n/a | hiding all cases = page collapse | minimum 1 case if section is on | preview re-renders without hidden |

### CS-4 · Leadership variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Leadership presence | A · at family | locked at template's L6 | family signature | n/a | family contract | n/a |
| Card count (where family allows) | B | 3 OR 4 cards (CS-DENSITY-05) | only on LF-1/3 typographic-grid · LF-2 fixed at 1 portrait · LF-4 fixed at absent · LF-5 fixed at 3-pillar | n/a | family contract enforces | preview re-renders with chosen count |
| Photo vs typographic-only | B | only when both pre-built | within-cluster sub-variant | switching mid-fork could orphan portraits | warn before switch · preserve uploaded portraits in revision | preview re-renders |
| Per-leader visibility | C | show/hide individual leader | minimum 3 visible if section is on (CS-DENSITY-05 floor) | hiding to collapse to 2-card | floor enforced | preview |

### CS-5 · CTA personality variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| CTA mental model | A | locked at cluster (per `corporate-suite-distinctness-matrix.md §1.7`) | cluster identity | n/a | cluster contract | n/a |
| CTA label text (primary) | B | 3-5 cluster-curated copies | each preset pre-validated CS-CTA-02 + cluster voice | n/a | sibling-aware · Cornice's label removed from picker for any non-LF-2 sibling | preview hero + CTA closer |
| CTA label text (secondary · optional) | B | 3-5 secondary copies | secondary is GHOST style (CS-CTA-03) | n/a | sibling-aware | preview |
| CTA button visual class | A | per-cluster polarity rule (filled-on-dark · outline-on-cream OR LF-2 filled-on-cream) | CS-CTA-01 ratified | customer changing button style | banned at architecture | n/a |

### CS-6 · Proof / KPI variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| KPI placement | A | locked at L5 (CS-LAYOUT-05) | family signature | n/a | family contract | n/a |
| KPI cell tuple | B | per-cluster preset (3-4 tuples per cluster) | tabular-nums (CS-TYPE-03) · count of 3 or 4 (CS-DENSITY-04) | 5+ cells | enforced | preview |
| KPI cell figure values | C with validation | end-user-editable text per cell | tabular-nums-compatible · no fake-decimals | "180+ %" malformed · ASCII-only fallback for old fonts | regex validation · italic-em on unit | preview with tabular alignment |
| KPI count-up animation (KPI-2) | C | on/off (per gravity default) | one-time-per-session | re-trigger on scroll | sessionStorage discipline | preview ensures one-time · scroll-back doesn't replay |
| KPI live-counter (KPI-3) | A · ops-config | NOT customer-toggleable · ops only | G5 cluster only · backend feed required | wiring fake feed | banned at customer layer | n/a |
| KPI range-fill (KPI-4) | C · cluster-conditional | on/off | only on G1/G3/G5 audit-led clusters | enabling on editorial cluster (G2) | gravity-allow-list enforces | preview |
| KPI comparative-tick (KPI-5) | C · cluster-conditional | on/off · benchmark URL required | benchmark source citation must be present | enabling without benchmark | enforced | preview shows benchmark + arrow |

### CS-7 · Nav variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Nav geometry | A | locked at L8 | family identity | n/a | family contract | n/a |
| Nav background polarity | A | locked at CS-PAL-06 + CS-NAV-01 (`--primary` background OR family-cream variant) | architectural | customer trying to change background to white | banned | n/a |
| Phone-right (where family allows) | C | on/off | depends on family (LF-1/3/4 default on · LF-2 default off · LF-5 default off) | enabling on LF-2 | family contract enforces availability | preview |
| Locale-pill style | B | pill · dropdown · static | each variant pre-built per cluster | choosing flag-emoji on institutional cluster (NAV-5 · banned for institutional) | gravity-allow-list enforces | preview |
| Sticky-condensed-on-scroll (NAV-1) | C | on/off · per gravity default | only G1/G2/G3/G4 | n/a | gravity-allow-list | preview |
| Sticky-hide-on-scroll-down (NAV-2) | C | on/off · default off in G3 · on in G5 | only G1/G5 | enabling on institutional | gravity-allow-list | preview |
| Scroll-progress-bar (NAV-3) | C | on/off · default off in G3 · on in G5 | thickness always 1px | thickness > 1px | enforced | preview |
| Breadcrumb on deep pages | C | on/off | deep pages only · home banned | on home | enforced | preview |

### CS-8 · Footer variants

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Footer column count | A | locked at L9 per CS-LAYOUT-09 | family contract | n/a | family contract | n/a |
| Whistleblowing column | A · cluster-conditional | locked when D.lgs. 24/2023 applies | legal compliance | removing | banned | rendered + verified by checker |
| Column ordering | B | per-cluster preset (brand-first · sitemap-first · contact-first) | each preset pre-validated | n/a | sibling-aware | preview |
| Newsletter signup | C | on/off · default off (CS-FOOT-04) | when on, must be above legal row | leak below legal row | enforced | preview shows signup placement |
| Office-hours-row | C | on/off | n/a | n/a | n/a | preview |
| Social-row | C | on/off · default off | n/a | adding too many platforms | enforced cap (3-5 platforms) | preview |
| Legal-row content | A | system-managed | always present · matches locale | customer trying to remove copyright | banned | renderer always emits |

### CS-9 · Color intensity / mood presets

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Palette preset | B | 5-7 cluster-validated palettes | CS-PAL-01 (L\* ≤ 40 on cream) · CS-PAL-05 (≤3 accent hits) · cluster polarity strategy | n/a (preset only) | sibling-aware: each live sibling's palette removed from picker for new forks of OTHER siblings | preview pane re-renders hero + 3 sections |
| Free hex picker | D | NOT SHIPPED | n/a | navy-on-navy · CS-PAL-01 violation invisible | banned at architecture | n/a |
| Per-token override (within preset) | B sub-control | only the secondary token can be customer-shifted ±15% in HSL | preserves CS-PAL-01 | shifting too far | clamped at architecture | preview |
| Custom palette upload (`from existing brand book`) | NOT IN MVP · D for now | future feature | requires constraint engine | n/a | banned at MVP | n/a |

### CS-10 · Imagery mood presets

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Imagery preset pool | B | sub-cluster pools per template (per `apps/catalog/preview_imagery.py` keyed pools) | CS-IMG-SRC-01 + binding triple per slot | n/a | pool-keyed at template-fork | preview re-renders |
| Customer image upload (slot 0 hero) | C with validation | per-slot upload via ProjectAsset | ≥1600 wide · 16:9 native · sub-cluster register fit | uploading inappropriate subject | smart-crop + slot-aware quality warning | preview · re-render hero |
| Customer image upload (other slots) | C with validation | per-slot upload | slot-specific specs (square portrait · 4:3 detail · 4:3 ambient) | wrong aspect ratio | smart-crop + warning | preview |
| Free Pexels URL paste | D | NOT SHIPPED | n/a | n/a | banned · use upload OR pool only | n/a |
| Free CDN URL paste | D | NOT SHIPPED | n/a | bypassing CS-IMG-SRC-01 | banned | n/a |
| AI image generation | D | NOT SHIPPED | n/a | n/a | banned | n/a |

### CS-11 · Typography presets

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Heading + body font pair | B | 3-5 cluster-validated pairs (subset of global CURATED_FONTS) | CS-TYPE-01 (serif heading + sans body) · cluster's font-pair allow-list per `corporate-suite-distinctness-matrix.md §1.4` | n/a | sibling-aware · Cornice's pair removed from picker for non-LF-2 corporate-suite | preview re-renders type |
| Free font name input | D | NOT SHIPPED | n/a | "Comic Sans" · banned fonts | banned · CURATED_FONTS only | n/a |
| Custom OTF/WOFF upload | D | NOT SHIPPED | n/a | licensing risk · perf risk | banned | n/a |
| Variable-axis font sliders | D | NOT SHIPPED | n/a | unbounded weights | banned | n/a |
| Heading scale | A | locked at CS-TYPE-04 | architectural | n/a | banned | n/a |
| Letter-spacing | A | locked at CS-TYPE-05 | architectural | n/a | banned | n/a |

### CS-12 · Motion presets

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| `motion_profile` master | B | cluster-allowed gravity set (per `dynamic-pattern-usage-rules.md §5`) | family + cluster contract | choosing G5 sprint-console for G3 institutional | gravity-allow-list enforces | preview re-runs |
| Motion intensity (`minimal · standard · expressive`) | B | enum | depends on cluster default · `expressive` only available for G5/G6 | choosing `expressive` on G3 | not exposed for G3 clusters | preview |
| Per-pattern enable/disable | C | on/off per pattern with `personalization_knobs` | reduced-motion always wins | can't override `prefers-reduced-motion` | fallback enforced | preview |
| Motion-curve editor | D | NOT SHIPPED | n/a | 50ms slot-machine timings | banned | n/a |
| Motion duration free input | D | NOT SHIPPED | n/a | duration < 200ms or > 2000ms | banned · enum only | n/a |

### CS-13 · Density presets

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Density preset | B | `compact · medium · airy · very-airy` (existing DENSITY_PROFILES) | template default ±1 notch · CS-RHYTHM-01 | jumping ±2 notches (e.g., compact → very-airy) | clamped to ±1 | preview |
| Free padding-pixel input | D | NOT SHIPPED | n/a | breaking 100×72 cluster invariant | banned | n/a |
| Free max-width input | D | NOT SHIPPED | n/a | breaking 1400px cap | banned | n/a |
| Free vertical-rhythm slider | D | NOT SHIPPED | n/a | breaking CS-RHYTHM-06 | banned | n/a |

### CS-14 · Trust / authority modules

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| D.lgs. 24/2023 whistleblowing | A · cluster-conditional | locked when applicable | legal compliance | removing | banned | renderer enforces |
| Voice-anchor recurrence | A | locked · system-enforced (h1 + CTA closer h2) | CS-EXEC-01 | customer editing h1 to remove anchor | preview detects missing anchor · save blocked | regex check at save |
| Sectors ribbon | C | on/off (cluster-aware) | when on, label is editable per CS-COMP-01 (text-only) | adding client logos | banned at architecture | preview · text-only check |
| Trust marquee (logos) | C | on/off · cluster-conditional | only association marks (ODCEC · OAPPC · ICF · etc.) · NEVER client logos | adding fake logos | banned at architecture · brand audit | preview |
| Peer-citation module (QUOTE-6) | C | on/off · cluster-conditional | requires real publication name + date + excerpt | fake citations | save validation · external link required | preview |
| Award-ribbon | C | on/off · cluster-conditional | requires real award credentials | fake awards | banned · CS-EXEC-03 | preview |

### CS-15 · Optional modules on/off

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| KPI band | C · cluster-conditional | on/off (default on · LF-2 has overlay-only) | minimum-section floor | turning off | enforced | preview |
| Trust marquee | C · cluster-conditional | on/off (default per family) | n/a | n/a | enforced | preview |
| Newsletter signup | C | on/off (default off) | placement above legal row | enabling without backend | save validation | preview |
| Live ship-log | C · G5 only | on/off | requires backend feed (ops config) | enabling without feed | banned without ops | preview |
| Cookie banner | A | system-managed | always on if locale requires | n/a | system enforces | n/a |
| AR locale switcher in nav | C | on/off · only when AR locale shipped | n/a | hiding when AR is required | preserved per locale list | preview |

### CS-16 · Page-level optional sections

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Case-study list page | C | on/off · default on for clusters that ship cases · auto-hides nav link if off | when off, hide from nav AND search · preserve cases data | turning off but linking from home (broken link) | save check | preview |
| Pricing page | C · cluster-conditional | on/off · default off; on if cluster ships AND customer has copy | requires copy author at fork | empty pricing page | empty-state guard | preview |
| About page | A | always on · cannot be removed | architectural · about-required-per-cluster | trying to remove | banned | n/a |
| Contact page | A | always on · cannot be removed | architectural | trying to remove | banned | n/a |
| Blog/insights page | C | on/off · default off · on if customer enables AND has content | requires posts · empty-state guard | empty page | save check | preview |
| Custom page | D · NOT IN MVP | NOT SHIPPED | adding pages is planner-side | bypass distinctness checks | banned for customer | n/a |

### CS-17 · Locale / RTL safe constraints

| Control | Layer | Allowed range | Hidden constraint | Likely misuse | Anti-collapse | Preview verify |
|---|---|---|---|---|---|---|
| Locale set | A | locked at template's `locales` row | shipped at workflow C | adding new locale | banned · pipeline-only | n/a |
| Per-locale enable/disable | C | on/off per locale (within shipped set) | revisions preserve disabled translations | disabling all locales | minimum 1 locale enforced | preview |
| Voice-anchor verbatim per locale | A | system-enforced · CS-EXEC-01 | em-noun preserved in translation per cluster's distinctness-matrix §1.4 row | customer editing translation | save block if anchor missing | regex check |
| Latin wordmark in AR locale | A | locked · CS-NAV-06 | architectural | translating wordmark | banned | renderer | n/a |
| Latin numerics in AR KPI | A | locked · CS-FOOT-03 | architectural | swapping numerals | banned | renderer | n/a |
| Naskh AR h1 (LF-2 only) | A | locked · `body.cs-lf-lf-2` selector-scope | family-scoped · CS-TYPE-06 | porting to LF-1/3/4/5 | banned | computed-style check |
| Customer-supplied translation | D | NOT SHIPPED | n/a | breaks anchor verbatim guarantee | banned · pipeline-only | n/a |

---

## §3 · Layer assignment summary by surface

| Surface | Layer A locked | Layer B presets | Layer C toggles | Layer D banned |
|---|---|---|---|---|
| CS-1 hero | hero geometry · CTA visual class | meta-strip composition · CTA copy · photo pool | secondary CTA on/off · phone in hero · photo upload | free CTA copy · arbitrary aspect ratio |
| CS-2 sections | section sequence | n/a | optional section on/off | section reorder · custom page |
| CS-3 cases | case-preview shape | sub-variant · case count | per-case visibility | n/a |
| CS-4 leadership | leadership presence | card count · photo vs typographic | per-leader visibility | reordering family-locked cells |
| CS-5 CTA | mental model · button visual class | label preset (primary + secondary) | secondary CTA on/off | free CTA · "Buy now" |
| CS-6 KPI | KPI placement (L5) | cell tuple preset | count-up · range-fill · comparative on/off | live-counter customer-edit · arbitrary cells |
| CS-7 nav | geometry · polarity | locale-pill style | NAV-1 · NAV-2 · NAV-3 · NAV-4 toggles | nav-color · custom nav |
| CS-8 footer | column count · whistleblowing · legal row | column ordering | newsletter · office-hours · social | removing legal row |
| CS-9 palette | n/a | palette preset · per-token shift ±15% | n/a | free hex · custom upload |
| CS-10 imagery | n/a (sourcing rule is Layer A) | preset pool | upload per slot | free URL · AI gen |
| CS-11 typography | heading scale · letter-spacing | font pair preset | n/a | free font · OTF upload · variable-axis |
| CS-12 motion | reduced-motion · banned classes | `motion_profile` · intensity | per-pattern toggles | curve editor · duration free input |
| CS-13 density | n/a | density preset (±1) | n/a | free padding · max-width · rhythm |
| CS-14 trust | whistleblowing · voice-anchor · sectors-ribbon (when on) | n/a | trust-marquee · peer-citation · award on/off | client logos · fake credentials |
| CS-15 optional modules | cookie banner · about · contact | n/a | KPI band · trust marquee · newsletter · ship-log · AR switcher | live-counter customer-wired |
| CS-16 pages | about · contact | n/a | cases · pricing · blog | custom page |
| CS-17 locales | locale set · voice-anchor · Latin wordmark · Naskh selector | n/a | per-locale enable/disable | customer translation · new locale |

---

## §4 · Per-cluster default Layer A/B/C ratio

The actual ratio per cluster shipped today + projected for new clusters.

| Cluster | Layer A surfaces | Layer B surfaces | Layer C surfaces | Note |
|---|---|---|---|---|
| corporate-suite (LF-1/3/4) | hero geometry · section sequence · KPI placement · L8 nav · L9 footer · whistleblowing · voice anchor · CTA visual class · density invariants | palette · font pair · imagery pool · density · KPI cell tuple · CTA copy · footer column ordering | KPI count-up · card-lift · NAV-1 · NAV-2 · NAV-3 · cases on/off · trust marquee on/off · newsletter on/off · per-locale on/off | 30% A · 50% B · 20% C target hits |
| corporate-suite (LF-2 · Cornice/Causa) | + L4 essay-with-anchors · L7 magazine-grid · LF-2 cream nav · LF-2 4-col footer | + chapter-stepper variants · pull-quote-em variants · provenance-tooltip on/off | NAV-3 light-touch | LF-2 has slightly tighter A (more locked cells) |
| corporate-suite LF-5 (Continua) | + L1 object-overlay · L3 governance-cycle · L7 timeline | + ring-count · timeline shape (TIME-1 vs TIME-2) | + governance-cycle disclosure on/off | stewardship-restrained tightens C |
| agency-digital-studio (G5 · projected) | live-counter ops-config locked · ship-log feed locked | sprint-console motion gravity · capability grid count · KPI live OR static | NAV-3 · NAV-2 · MICRO-3 magnetic on hero CTA · ship-log on/off | G5 has more C toggles |
| portfolio-cinematic (G6 · projected) | hero MEDIA-1/2 locked · gallery snap locked | gallery image set · cinematic-fade duration · cursor-vignette intensity | MICRO-6 cursor-vignette on/off · per-image lightbox on/off | G6 has fewer C toggles than G5 |

Each cluster's exact ratio is computed at hardening-pass time (when the
cluster's standards stack lands).

---

## §5 · Anti-collapse mechanisms · per-control summary

Three mechanisms (per architecture §3) interlocking per-control:

| Control surface | Mechanism 1 (per-cluster narrowing) | Mechanism 2 (sibling-aware) | Mechanism 3 (Layer A invariant) |
|---|---|---|---|
| CS-9 palette | each cluster has its own preset library (no cross-cluster reuse) | a shipped sibling's palette is REMOVED from the picker for new forks of OTHER siblings in the same family | CS-PAL-01 + CS-PAL-05 + cluster polarity strategy |
| CS-11 typography | each cluster narrows the global CURATED_FONTS to ~5 per cluster | a shipped sibling's font pair is REMOVED from the picker | CS-TYPE-01 + heading scale + letter-spacing |
| CS-10 imagery | each sub-cluster has its own pool | a sibling's photo URLs are REMOVED via cross-cluster grep CS-IMG-SRC-04 | binding triple per slot |
| CS-5 CTA copy | each cluster has its own copy register | a sibling's exact copy is REMOVED from the picker | CS-CTA-02 advisor's voice |
| CS-12 motion | each cluster has its own gravity allow-list | a sibling's chosen `motion_profile` is REMOVED from the picker if it would collapse | reduced-motion · banned classes |
| CS-3 / CS-7 / CS-8 layout | family-locked at L1-L9 | n/a (family-locked) | family contract |

The three mechanisms ensure: (a) the customer always has variety within
their cluster · (b) two customers forking the SAME template can produce
different projects · (c) two TEMPLATES produced by the orchestrator
cannot accidentally ship with the same identity.

---

## §6 · Preview-verification requirements (per surface)

Every Layer-B/C change must preview-verify before save. The preview-verifier
runs the matching subset of the orchestrator's A.6 critique:

| Surface | Preview verification rule |
|---|---|
| CS-1 hero | h1 contrast over photo · CTA contrast against background · photo aspect-ratio fit |
| CS-2 sections | minimum 4 sections on home · banned-state empty pages |
| CS-3 cases | minimum 1 case visible if section on |
| CS-4 leadership | card count within 3-6 · all visible leaders have a portrait OR all are typographic |
| CS-5 CTA | label text passes CS-CTA-02 · route is real · button polarity preserved |
| CS-6 KPI | tabular-nums · count is 3-4 · cells render |
| CS-7 nav | 5-7 links · primary-bg polarity preserved · phone-right placement valid |
| CS-8 footer | column count matches L9 · legal row present · whistleblowing column when applicable |
| CS-9 palette | CS-PAL-01 L\* contrast · CS-PAL-05 ≤3 accent hits · `--primary-2` not invoked |
| CS-10 imagery | image resolved · resolution ≥ slot floor · aspect fit OK · CS-IMG-SRC-01 (Pexels-only) |
| CS-11 typography | font pair allowed for cluster · heading scale unchanged · letter-spacing unchanged |
| CS-12 motion | `motion_profile` in cluster's allow-list · reduced-motion equivalent ships · banned patterns absent |
| CS-13 density | within ±1 notch of template default · CS-RHYTHM-01 preserved |
| CS-14 trust | sectors-ribbon text-only · trust marquee = associations only · voice-anchor present |
| CS-15 optional | minimum-section floor · whistleblowing not removed · cookie banner present |
| CS-16 pages | about + contact present · pricing has copy if enabled · blog has posts if enabled |
| CS-17 locales | minimum 1 locale enabled · Latin wordmark in AR · Naskh selector intact in LF-2 AR |

If any check fails: save is BLOCKED, customer sees the reason, no broken
state ships.

---

## §7 · How the editor uses this map at every save

For each customer-side change:

1. Identify the control surface the change affects (CS-1 to CS-17).
2. Identify the layer (A / B / C). If Layer D, refuse silently (the UI
   should not have offered the control in the first place).
3. Apply preview verification per §6 row.
4. If verify passes:
   - Save the override to `ProjectDesignTokens` or `ProjectContent` or
     `ProjectAsset`.
   - Create a `ProjectRevision` snapshot with reason `manual`.
   - Update the live preview pane.
5. If verify fails:
   - Block save.
   - Show the customer the reason ("Contrast on the new palette is too
     low for body text. Adjust or pick another preset.").
   - Preserve their input state for retry.

The editor never silently degrades. Every change is auditable in
`ProjectRevision`.

---

## §8 · Maintenance protocol

- Each new cluster ships at hardening parity and adds a row to §4 (per-cluster
  Layer A/B/C ratio).
- Each new Layer-B preset added to a cluster must be cross-checked against
  every shipped sibling in that cluster (Mechanism 2).
- Each new Layer-C toggle added to a cluster must include preview-verification
  rule(s) in §6.
- Each new Layer-D ban (proposed by future passes) must be filed as a § decision
  in `personalization-safety-rules.md §3`.
- Cells in §2 are extended monotonically. Deprecated controls stay marked
  DEPRECATED with date + replacement pointer.

---

## §9 · One-paragraph summary

17 control surfaces map across the 4-layer model: hero (A locked geometry +
B presets) · section ordering (A locked sequence + C toggles) · case-study
display (A family-locked + B sub-variants) · leadership (A presence + B
cards · C visibility) · CTA (A mental model + B copy preset) · KPI (A
placement + B cells + C animations) · nav (A geometry + B locale-pill +
C behaviors) · footer (A column count + B ordering + C optionals) · palette
(B preset · D free hex banned) · imagery (B pool + C upload · D free URL
banned) · typography (B font pair · D free font banned) · motion (B
profile + C per-pattern · D curve editor banned) · density (B preset · D
free input banned) · trust (A locked + C optionals) · optional modules
(C toggles · A architectural floor) · page-level (C cases/pricing/blog
· A about/contact required) · locales (A locked set + C per-locale on/off
· D customer translation banned). Each surface has a preview-verification
rule that fires at every save. Three anti-collapse mechanisms interlock:
per-cluster narrowing · sibling-aware preset subtraction · Layer A
invariants. The orchestrator and editor read this map at every fork; the
customer never confronts Layer A or D directly.
