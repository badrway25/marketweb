# Premium-dynamic implementation slice 01 · `motion_profile` DNA + KPI-2 count-up

```yaml
report_type:        hardening · implementation slice (the first product-side
                    pass after the audit · pattern library · personalization
                    architecture · anti-clone 2.0 paper trio)
phase:              X.7d slice 01
date:               2026-05-05
agent:              orchestrator-side authoring + implementation
trigger:            audit gap #2 (one motion vocabulary) · pattern library §5
                    priority #1 (motion_profile DNA dimension) + #2 (KPI-2
                    count-up-on-view) · retrofit plan R5 (Causa within-family
                    differentiator vs Cornice on KPI placement axis 7)
slice_scope:        ONE · motion_profile DNA dimension carrying the per-pattern
                    `kpi_animate` flag + KPI-2 count-up-on-view as the first
                    pattern wired through it · 5-file change · zero apps/editor
                    · zero apps/projects · zero apps/commerce · zero new sibling
                    · zero tier change · zero registry change
status_tag:         IMPLEMENTED · LIVE-VERIFIED · 546/546 OK · ZERO REGRESSION
                    on Pragma · Cornice · Fiscus · Solaria (their per-template
                    kpi_animate flag preserves prior behavior) · DELIBERATE
                    BEHAVIOR CHANGE on Continua (KPI band stops animating ·
                    G4 stewardship register fix) · DELIBERATE BEHAVIOR CHANGE
                    on Causa (KPI overlay starts animating · within-family
                    differentiator vs Cornice)
verdict:            shipped · paper recommendations from the four prior passes
                    are now product-side reality on the cluster · the
                    `motion_profile` field becomes the carrier for every
                    subsequent slice (NAV-1 sticky-condensed · EVID-3 case-
                    citation-pop · TIME-3 chronological-tick · MICRO-2 card-
                    lift · etc.) per the priority list
```

## §0 · Why this slice was chosen

Per the audit (`premium-dynamic-personalization-audit.md §10 gap #2`), the
single most acute capability gap was "one motion vocabulary across 6
templates · uniform contract · directly the user's 'not dynamic enough'
signal." Per the pattern library (`premium-dynamic-pattern-library.md §5`),
the priority-ordered first pass was:

1. **`motion_profile` DNA dimension (the field itself)**.
2. **KPI-2 count-up-on-view** (the first pattern that reads from it).
3. EDIT-1 + SCROLL-2 codified as utilities.
4. MICRO-2 card-lift-restrained.
5. EVID-2 attestation-chip-hover.
6. NAV-1 sticky-condensed (extending from LF-5).
7. EDIT-4 sticky-side-rail (codify).
8. CASE-6 filterable-grid-with-chips.
9. MEDIA-3 image-grid-stagger-reveal.
10. EVID-1 progressive-disclosure-tap.
11. NAV-3 scroll-progress-bar-thin.
12. MICRO-3 magnetic-button-restrained.

The audit's case for slice ordering: the first 5 are zero-risk additions
to the existing corporate-suite contract. KPI-2 is THE foundational pattern
because it's the simplest motion behavior, and `motion_profile` is the
DNA carrier that makes every subsequent pattern composable.

The slice satisfies all five mandated constraints:

| Constraint | How this slice satisfies |
|---|---|
| **High visible impact** | KPI cells are the most-read numeric proof on every corporate-suite home; animating (or stopping the animation on) them changes the first-30-second perception |
| **Low regression risk** | one new pattern · IntersectionObserver-based · reduced-motion fallback is the static final number (which is what every non-animating sibling ships today) · 5-file change · 546/546 tests OK |
| **Reusable across future templates** | `motion_profile` is now a first-class DNA dimension with 7 enumerated values (G1-safe-premium · G2-editorial · G2-editorial-counter · G3-institutional · G4-stewardship · G5-sprint-console · G6-cinematic) · every future cluster declares one |
| **Improves both distinction AND personalization readiness** | DISTINCTION: Causa picks up `g2-editorial-counter` (KPI count-up ON · within-family differentiator vs Cornice's static `g2-editorial`) · raises Cornice ↔ Causa anti-clone 2.0 axis-7 from 1 → 2 and contributes to axis-18 from 0 → 1 · PERSONALIZATION: the field is what Phase X.7c editor slice will expose as Layer-B preset (`minimal · standard · expressive`) |
| **Verifiable live** | browser-walked all 6 siblings · counter behavior matches declared `motion_profile` per each · server-side renders confirm `data-motion-profile` + `data-motion-kpi-animate` attributes · screenshots captured · 546/546 tests pass |

The retrofit plan (`corporate-suite-retrofit-priority-plan.md`) named 7
Causa retrofits (R1 CTA inflection · R2 EVID-3 · R3 TIME-3 · R4 NAV-1 ·
R5 KPI sub-variant + KPI-2 count-up · R6 EVID-5 · R7 leadership composition).
**This slice ships R5 in full** and lays the DNA infrastructure that R2-R4
+ R6 will build on in subsequent slices.

---

## §1 · What was implemented

### File 1 of 5 · `apps/catalog/template_dna.py`
- New `MOTION_PROFILES: dict[str, dict[str, Any]]` registry at the top of
  the per-template DNA file. Keyed by gravity name, valued as a per-pattern
  flag bundle. Today the bundle has one flag (`kpi_animate`); Phase X.7d
  follow-up slices will extend with `nav_condense_on_scroll` ·
  `hero_parallax` · `gallery_snap` · `magnetic_button` · etc. (one flag
  per pattern as patterns ship).
- Per-template `motion_profile` field added to all 6 corporate-suite
  siblings:
  - `pragma-corporate-suite` → `g3-institutional` (kpi_animate=True · current behavior preserved)
  - `cornice-architettura` → `g2-editorial` (kpi_animate=False · current behavior preserved)
  - `fiscus-commercialista` → `g3-institutional` (kpi_animate=True · current behavior preserved)
  - `solaria-coaching` → `g3-institutional` (kpi_animate=True · current behavior preserved)
  - `continua-stewardship` → `g4-stewardship` (kpi_animate=False · **BEHAVIOR CHANGE** · pre-slice the LF-5 KPI band animated count-up; the stewardship register prefers stillness per pattern library §2.1 KPI-2 cluster fit · alignment fix)
  - `causa-legale` → `g2-editorial-counter` (kpi_animate=True · **BEHAVIOR CHANGE** · pre-slice the LF-2 KPI overlay was static via `data-lm="reveal"`; now animates · within-family differentiator vs Cornice per retrofit R5)

The `motion_profile` field is **strictly additive**: archetypes outside
corporate-suite (agency · medical · restaurant · portfolio · real-estate ·
e-commerce · lawyer · startup-saas) have no `motion_profile` set, the
view defaults to `None`, the body data-attributes are not emitted, and
the JS counter pass behavior on those archetypes is **unchanged from
pre-slice state**.

### File 2 of 5 · `apps/catalog/views.py`
- New import: `from apps.catalog.template_dna import MOTION_PROFILES, get_dna`
- Inside `LiveTemplateView.get_context_data()`, derive `motion_profile`
  + `motion_kpi_animate` from the DNA's declared profile (or `None` if
  the DNA doesn't declare one). 8-line addition.
- Added to context: `motion_profile`, `motion_kpi_animate`. The base
  template uses these to emit body data-attributes.

### File 3 of 5 · `templates/live_templates/business/corporate-suite/_base.html`
- Body tag (line 1174) extended with two new conditional attributes:
  - `data-motion-profile="{profile}"` (when `motion_profile` is set)
  - `data-motion-kpi-animate="1"` (when `motion_kpi_animate` is True)
- The body **class** string is unchanged. (Used data-attributes instead
  of class additions to preserve the body-class shape that
  `apps/projects/tests.py:8917` asserts on for Pragma editor preview.
  The data-attribute approach is also cleaner for non-styling toggles.)

### File 4 of 5 · `templates/live_templates/business/corporate-suite/_layouts/lf2/content.html`
- LF-2 hero KPI cells now carry `data-lm="counter"` on the `.num` span
  (previously they used `data-lm="reveal"` only). The structural attribute
  is now present; activation is gated by the body's `data-motion-kpi-animate`
  attribute. This means:
  - **Cornice** (`motion_profile = g2-editorial` · no body attribute) → JS skips the counter pass · KPI numbers render statically · **identical behavior to pre-slice**.
  - **Causa** (`motion_profile = g2-editorial-counter` · body attribute set) → JS activates the counter pass · KPI numbers animate count-up once-per-session on viewport entry · **new behavior · the within-family differentiator vs Cornice**.

### File 5 of 5 · `static/js/live-motion.js`
- `setupCounters()` gated by `document.body.getAttribute('data-motion-kpi-animate') !== '1'` early return. Templates without the attribute skip the counter pass and their KPI numbers render statically · the existing pre-slice fallback at the top of `init()` still short-circuits the entire pass when `prefers-reduced-motion: reduce` is set.

---

## §2 · What visibly improved

| Sibling | Pre-slice KPI behavior | Post-slice KPI behavior | Change |
|---|---|---|---|
| **Pragma** (LF-1 · g3-institutional) | count-up animates band-at-3 on viewport entry | identical · count-up still animates | no visible change · `motion_profile` field formalises what was implicit |
| **Cornice** (LF-2 · g2-editorial) | static hero overlay 47 · 18 · 6 | identical · static | no visible change · LF-2 family KPI cells gained the structural `data-lm="counter"` token but body-attribute gate keeps activation off · editorial register preserved |
| **Fiscus** (LF-3 · g3-institutional · LF-1 scaffold) | count-up animates band-at-3 | identical · count-up still animates | no visible change |
| **Solaria** (LF-4 · g3-institutional · LF-1 scaffold) | count-up animates band-at-4/5 | identical · count-up still animates | no visible change |
| **Continua** (LF-5 · g4-stewardship) | count-up animated band-at-4 (LF-5 cells used `data-lm="counter"`) | static band-at-4 (counter pass skipped via body attribute) | **BEHAVIOR CHANGE** · stewardship-register-prefers-stillness alignment per pattern library §2.1 KPI-2 cluster-fit (G4 = banned for count-up) · the longitudinal mandate-trajectory feel is reinforced by static numbers |
| **Causa** (LF-2 · g2-editorial-counter) | static hero overlay 28 · 14 · 31 (LF-2 cells used `data-lm="reveal"`) | count-up animates hero overlay (LF-2 cells now use `data-lm="counter"` AND body attribute set) | **BEHAVIOR CHANGE** · Causa within-family differentiator vs Cornice · raises Cornice ↔ Causa anti-clone 2.0 axis 7 from 1 → 2 (sub-variant within KPI placement shape · same hero-overlay shape but different animation) · contributes to axis 18 from 0 → 1 (one additional pattern enabled in Causa that's not in Cornice) |

**Net visible change at the cluster scale**: 4 of 6 siblings unchanged · 1
sibling (Continua) becomes more restrained (stewardship register fix) · 1
sibling (Causa) becomes more dynamic (within-family differentiator). The
cluster's average "feels alive" signal moves up because Causa joins
Pragma/Fiscus/Solaria as dynamic-KPI templates, and Cornice/Continua
deliberately ship the editorial/stewardship stillness their registers
demand.

The user signal "feels too similar / not dynamic enough" is partially
addressed at the within-family pair (Cornice ↔ Causa now visibly differ
on the KPI surface). Cluster-level S6 sameness (audit §10 gaps 2-4)
still requires Phase X.7a (new cluster) for full resolution; this slice
opens the per-pattern infrastructure that future slices use.

---

## §3 · What became more dynamic

- **Causa hero overlay** · 28 · 14 · 31 now ticks from 0 to its target
  values once-per-session on viewport entry (1400ms ease-out cubic ·
  per `static/js/live-motion.js COUNTER_DURATION_MS`). Reduced-motion
  fallback: static numbers from first paint.
- **Cluster motion vocabulary**: extended from one implicit unnamed
  default to seven explicitly enumerated profiles (G1-G6 + G2-editorial-
  counter sub-variant). Future slices populate the bundle.

What is NOT more dynamic in this slice (deferred to future slices):
- Cornice's narrative essay (no TIME-3 yet).
- Causa's case-cards (no EVID-3 yet).
- Any sibling's nav (no NAV-1 sticky-condensed beyond Continua's existing
  shipped behavior).
- Any sibling's hover affordances (no MICRO-2 card-lift yet).
- Any sibling's scroll-progress (no NAV-3 yet).

These are next-slice work · the `motion_profile` field carries them.

---

## §4 · What became more customizable

- **`motion_profile` is now a first-class DNA dimension**. Phase X.7c
  editor slice will read this field and expose a Layer-B preset picker
  (per `template-personalization-architecture.md §5 motion presets`).
  The customer picks `minimal · standard · expressive` from the cluster's
  allowed gravity set.
- **Per-pattern flags** (`kpi_animate` today; `nav_condense_on_scroll` ·
  `hero_parallax` · etc. in subsequent slices) form the data shape that
  end-user toggles will manipulate at Phase X.7c.5 (section toggle preset
  library).
- **Strictly additive**: no breaking change to existing project-state
  (`apps/projects/models.py · ProjectDesignTokens` is untouched). When
  Phase X.7c.6 adds a customer-side `motion_profile_override` field,
  it'll layer cleanly on top of the DNA default.

---

## §5 · Files changed (5 files · all in scope · no apps/editor · projects · commerce touched)

| File | Change | Lines added |
|---|---|---|
| `apps/catalog/template_dna.py` | `MOTION_PROFILES` registry + per-sibling `motion_profile` field × 6 | ~35 |
| `apps/catalog/views.py` | derive context keys from MOTION_PROFILES lookup | ~10 |
| `templates/live_templates/business/corporate-suite/_base.html` | body data-attributes | 1 line edit (extended attribute string) |
| `templates/live_templates/business/corporate-suite/_layouts/lf2/content.html` | KPI cell `.num` carries `data-lm="counter"` + comment | ~8 |
| `static/js/live-motion.js` | gate counter pass on body attribute + comment | ~10 |

Total: ~65 lines added (mostly comments + the registry); 5 files; 0 model
schema change; 0 migration; 0 imagery touched; 0 cluster-other-archetype
touched.

**What was NOT touched** (per slice scope rules):
- `apps/editor/*` — zero edits.
- `apps/projects/*` — zero edits (fix to brittle test deferred · used data-
  attribute approach instead to avoid editing the test).
- `apps/commerce/*` — zero edits.
- Any non-corporate-suite archetype — zero edits.
- `TEMPLATE_REGISTRY.json` — zero edits.
- DB schema · migrations — zero touch.
- Imagery pools — zero touch.
- Voice anchors · CTA copy · footer columns · whistleblowing — zero touch.
- Cornice's content module · LF-1/LF-3/LF-4/LF-5 layout files — zero touch.
- Solaria · Pragma · Fiscus content modules — zero touch.

---

## §6 · Tests + browser verification

```
$ python manage.py test --verbosity 0
Ran 546 tests in 176.539s
OK
```

**546/546 tests pass.** The pre-existing booking-flag test failure documented
across all prior corporate-suite passes is now also passing (Continua's
booking-shape was the source · unchanged here · the test passing today
is a separate phenomenon possibly from a recent test-cohort-update;
flagged for follow-up but not blocking this slice).

**Browser walk** at 1440×900 viewport · staff session for Causa · anonymous
for the 5 live siblings · all probes via Playwright MCP:

| Sibling | profile rendered | data-motion-kpi-animate | counter pass | original captured | final value | verdict |
|---|---|---|---|---|---|---|
| Pragma | g3-institutional | 1 | RUN | yes | 22 / 180+ / €1.4 B / 94% | ✅ as expected |
| Cornice | g2-editorial | (none) | SKIP | no | 47 / 18 / 6 (static) | ✅ as expected |
| Fiscus | g3-institutional | 1 | RUN | yes (per server probe) | per fiscal-calendar tuple | ✅ as expected |
| Solaria | g3-institutional | 1 | RUN | yes (per server probe) | per percorso tuple | ✅ as expected |
| Continua | g4-stewardship | (none) | SKIP | no (NEW · was capturing pre-slice) | 18 / 3 / €1.8 B / 4 (static) | ✅ as expected · NEW |
| Causa (staff) | g2-editorial-counter | 1 | RUN | yes (NEW · was static pre-slice) | 28 / 14 / 31 | ✅ as expected · NEW |

**Anonymous frozen-sibling regression**:
- pragma-corporate-suite: 200 · 87,179 bytes (was 87,112 · +67 from data-attrs)
- cornice-architettura: 200 · 99,026 bytes (was 98,673 · +353 from data-attrs + LF-2 KPI cell `data-lm="counter"` token + comment)
- fiscus-commercialista: 200 · 88,077 bytes (was 88,010 · +67)
- solaria-coaching: 200 · 88,516 bytes (was 88,449 · +67)
- continua-stewardship: 200 · 94,677 bytes (was 94,640 · +37 · only data-motion-profile attribute · no kpi-animate attribute)

All deltas explained by intentional changes. **Zero unexplained drift.**

**Causa anonymous draft-gate**: 404 · CONFIRMED preserved.
**Causa staff routes**: 9/9 200.
**Catalog · home counter**: causa-legale not listed publicly · 24+ home counter unchanged.

Capture evidence: `factory/reports/browser-verification/slice-01-kpi2-motion-profile/captures/`
- 01-pragma-kpi-band.jpeg · 02-pragma-kpi-band-final.jpeg
- 03-causa-kpi-overlay-final.jpeg
- 04-cornice-kpi-overlay-static.jpeg
- 05-continua-kpi-band-static-new.jpeg

---

## §7 · What remains untouched for later slices

The retrofit plan named 7 Causa retrofits (R1-R7). This slice ships R5
(KPI sub-variant + KPI-2 count-up) and lays the `motion_profile` infrastructure
that subsequent slices use. Remaining:

| Slice | Retrofit | Pattern | Effort |
|---|---|---|---|
| X.7d.02 | R1 | CTA inflection shift "Apri un parere preliminare" → "Sottometti un parere preliminare" (5 locales × 1 string) | low |
| X.7d.03 | R4 | NAV-1 sticky-condensed-on-scroll for Causa (extend from LF-5) | low |
| X.7d.04 | R6 | EVID-5 provenance-tooltip-image on hero | low |
| X.7d.05 | R2 | EVID-3 case-citation-pop on Causa magazine cards (4 cards) | medium |
| X.7d.06 | R3 | TIME-3 chronological-tick-horizontal in Causa narrative | medium |
| X.7d.07 | LF-2 family variance rules formalisation (paper) | rule-book extension AC-V1..V5 | low |

Plus the cluster-level S6 work (audit gap #1 · the audit's recommended
NEXT product pass after these slices):

| Phase | Action |
|---|---|
| X.7a | ship one non-corporate-suite cluster at hardening parity (audit §11) |
| X.7b extension | extend `motion_profile` bundle with NAV-1 / EVID-3 / TIME-3 / MICRO-2 / etc. flags |
| X.7c | editor-side palette/font/motion preset picker (Layer B) |

Each named slice is paper-spec'd in the audit + pattern library + retrofit
plan. **Implementation order is not strictly forced**; the orchestrator picks
based on the user-handshake at each cycle.

---

## §8 · Phase X.7d slice 01 conclusion

The first product-side pass after four paper hardening passes is in. The
audit's gap #2 (one motion vocabulary) is now infrastructure-resolved —
the cluster has a per-template `motion_profile` field, six values
enumerated, one pattern (KPI-2 count-up) reading from it, and the editor
side ready to expose it as a Layer-B preset in Phase X.7c. The retrofit
plan's R5 is shipped; R1-R4, R6, AC-V1..V5 are queued. Two visible-feel
changes ship: Continua KPI band stops animating (stewardship register fix)
and Causa KPI overlay starts animating (within-family differentiator vs
Cornice). The cluster's anti-clone 2.0 axis 7 + axis 18 score raises +2
on the Cornice ↔ Causa pair · 21/54 → 23/54 (still below within-family
threshold of 27/54 but moving in the right direction · subsequent slices
close the rest of the gap).

The system is more distinct, more dynamic on the right templates, more
restrained on the right templates, more customizable in the DNA layer,
and ready for the next 5 retrofit slices to ship under the same playbook.
