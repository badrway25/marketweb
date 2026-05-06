# Motion-profile DNA · implementation pass 1

```yaml
report_type:        hardening · motion_profile DNA elevation · code-side
                    implementation slice (first non-Causa-retrofit code
                    pass since slice 02 closed)
phase:              X.7b · motion_profile DNA · implementation pass 1
                    (paper contract ratified 2026-05-05; this pass extends
                    code so the contract is REAL in CSS+JS and reachable
                    from any future intake brief)
date:               2026-05-06
agent:              orchestrator-side authoring (post-Causa-slice-02 ·
                    post-LF-2-variance ratification · post-anti-clone-2.0)
trigger:            user authorisation to ship the lightest non-breaking
                    scaffold that makes motion_profile real in code so
                    template distinctness no longer depends only on
                    layout/palette/copy but also on motion gravity, reveal
                    logic, interaction rhythm, and page choreography.
predecessor:        factory/reports/hardening/motion-profile-dna-plan.md
                    (16-section paper plan · ratified 2026-05-05)
                    factory/reports/hardening/causa-retrofit-slice-02.md
                    (3-flag → 5-flag bundle · g2-editorial-counter live)
                    factory/reports/hardening/premium-dynamic-pattern-library.md
                    (12-family · 48-pattern vocabulary · §2.4 MEDIA-1 ·
                    §2.5 MICRO-2 · this pass wires both)
companion files:
  - factory/reports/browser-verification/motion-profile-implementation-pass1.md
    (browser walk · default-motion + reduced-motion · 6 frozen siblings
    + 2 synthetic gate probes)
  - factory/reports/scorecard/motion-profile-implementation-pass1/scorecard.md
    (9 verification cells · 9/9 PASS · zero blocking)
  - design-orchestrator/references/internal-baselines/motion-profile-catalog.md
    §2 (the 12-flag table · updated to mark MICRO-2 + MEDIA-1 wired-today)
status_tag:         IMPL-PASS-1 · 5 → 7 wired bundle flags · 7 paper-flagged
                    · all 6 frozen corporate-suite siblings byte-equivalent
                    on body data-attributes + computed styles · all 546
                    Django tests still PASS · zero apps/editor / apps/projects
                    / apps/commerce edits · zero new templates opened ·
                    zero public tier flips
verdict:            motion_profile is a first-class DNA axis the planner
                    can now declare AND see take effect at first paint
                    via two new code-side gates. The g2-editorial-counter
                    profile is live in production (Causa, 5-flag bundle).
                    The g6-cinematic profile is wired in code and READY
                    for the first non-corporate-suite intake (Phase X.7a)
                    to declare it. Reduced-motion is honored on three
                    layers (JS root short-circuit + body.lm-reduced
                    class + native @media query). Frozen siblings are
                    preserved at byte-equivalence on every observable
                    surface verified.
recommendation:     next pass = (B) Causa workflow C multilingual.
                    Reasoning in §13.
```

---

## §0 · TL;DR

- **2 new bundle-flag gates wired**: `card_lift_restrained` (MICRO-2 ·
  pure-CSS) and `cinematic_fade` (MEDIA-1 · CSS+JS observer).
- **MOTION_PROFILES registry extended** from 5 boolean keys to 7. The
  `g6-cinematic` profile claims `cinematic_fade=True`; every other profile
  gets both new flags as `False` (additive · zero behavior change for any
  existing template).
- **Body data-attribute emission extended** with two new attributes
  (`data-motion-card-lift` · `data-motion-cinematic-fade`). Today no
  corporate-suite sibling emits either attribute (verified by walk).
- **`--mp-*` CSS token namespace** introduced on `:root` so each
  pattern's parameters (durations · easings · distances · saturation
  start · scale start) live as named tokens that profiles can override
  in scoped selectors.
- **Reveal sequencing**: existing `data-lm` system unchanged. The new
  cinematic-fade adds a peer pattern `[data-motion-fade-in]` that the
  observer toggles via `.lm-fade-in`.
- **Reduced-motion preserved**: belt + braces + suspenders. (1) JS init
  short-circuits before `setupCinematicFade()` runs. (2) `body.lm-reduced`
  body-class clears the hidden state via CSS. (3) `@media (prefers-reduced-
  motion: reduce)` clears it again for any client whose JS never executed.
- **Visible code differentiation**: 2 distinct premium-safe profiles
  are now live in code:
    1. `g2-editorial-counter` (Causa · evidence-led / reactive · 5 flags
       firing on home + chrome surfaces).
    2. `g6-cinematic` (cluster signature · `cinematic_fade` gate fires
       at first paint when assigned · ready for Phase X.7a intake).
- **Tests**: 546/546 PASS (baseline 546/546 → no regression).
- **Frozen siblings**: 6/6 byte-equivalent on body data-attributes +
  computed styles for every probe taken.
- **Recommended next step**: (B) Causa workflow C multilingual — the
  motion_profile axis is now binding at intake AND verifiable at gate;
  the highest-leverage next move is to ship Causa to 5 locales now that
  the LF-2 cell-pair voice + motion contract is fully cross-referenced
  in code (paper + slice-01 + slice-02 + this pass).

---

## §1 · The user signal this slice answers

The Phase X.7 audit named the cost: "templates feel too similar / not
dynamic." The audit's gap #2 was "one motion vocabulary is shared across
all 6 corporate-suite templates." Slice 01 (KPI-2 count-up gate · 1 flag)
+ slice 02 (NAV-1 sticky-condensed + EVID-5 provenance + EVID-3 case-
citation-pop + TIME-3 chronotick · 4 more flags) closed the LF-2 cell
within Causa. The Phase X.7b paper plan ratified the 8th DNA axis on
2026-05-05.

This pass is the **first non-Causa-retrofit code pass since the audit**.
It says: motion_profile is not just an enum on disk; it is a code-side
mechanism the planner can REACH. Two more flags get gates so future
clusters can immediately have premium-safe motion vocabulary the moment
their brief declares the profile.

The user's stated dimensions for this layer:
- motion gravity ✓ — `g6-cinematic` is now a code-reachable cluster
  signature via MEDIA-1.
- reveal logic ✓ — `data-motion-fade-in` joins `data-lm="reveal"` as a
  per-pattern reveal hook with profile-scoped activation.
- interaction rhythm ✓ — `data-motion-card` joins `[data-attestation-pop]`
  + `[data-evid3]` as a per-pattern interaction hook with profile-scoped
  activation.
- page choreography ✓ — slice-02 already shipped TIME-3 (chronological
  tick reveal); this pass adds editorial-fade choreography for cinematic
  templates.

---

## §2 · The smallest safe slice

Three rules governed slice scoping:

1. **Do not flip any flag on a frozen sibling.** All 6 corporate-suite
   live siblings (Pragma · Cornice · Fiscus · Solaria · Continua · Causa)
   ship the SAME flag set as before this pass. Verification in §6.
2. **Do not wire a flag without its CSS+JS gate landing in the same
   pass.** The paper plan §11 explicitly forbids extending the registry
   with un-wired flags ("creates a misleading API surface"). This pass
   wires 2 flags AND their gates · symmetric.
3. **Do not touch apps/editor / apps/projects / apps/commerce.** The
   Layer-B preset slot (`ProjectDesignTokens.motion_profile_intensity`)
   is Phase X.7c · explicitly out of scope. This pass is rendering-side
   only.

The two flags chosen — `card_lift_restrained` and `cinematic_fade` —
were selected against three criteria:

- **Cluster-coverage utility**: card-lift belongs to the safe pool of
  `g1-safe-premium` + `g3-institutional` + `g5-sprint-console` (3 of 7
  profiles), so 1 flag covers 3 future cluster intakes. cinematic-fade
  is the cluster signature for `g6-cinematic` (4 candidate clusters per
  the catalog: portfolio-cinematic Pixel · agency-creative-studio Vertex
  hero-only · ultra-luxury Villa · fashion-editorial Luxe).
- **Implementation cost**: card-lift is pure-CSS with no JS gate (the
  `:hover` / `:focus-within` selector pair is enough). cinematic-fade
  needs an IntersectionObserver but the precedent is identical to the
  existing TIME-3 observer wired in slice 02 — same one-shot semantics ·
  same threshold philosophy · same reduced-motion handling. Total LOC
  added across CSS+JS: ~120.
- **Anti-tacky safety**: both patterns have hard-encoded ceiling values
  in CSS variables (`--mp-card-lift-y: 3px` · `--mp-cinematic-dur:
  1200ms`). The system cannot render a flashier value without a code
  edit. AT-G1-2 (lift ≤3px · shadow ≤16px) and AT-G6-2 (fade ≥1200ms ·
  saturation start ≥0.85 · scale start ≤1.05) are encoded.

Two flags NOT wired this pass and their reasons:

- **`hero_parallax`** (MEDIA-2) — single-layer scroll-bound transform
  on hero only. Wiring requires `<880px` disabling logic plus a wrapper
  with `overflow:hidden` plus per-template viewport-width data plumbing.
  Cost ~3-5× of cinematic_fade. Defer to a later slice when a real
  cinematic template adopts the profile.
- **`nav_hide_on_scroll_down`** (NAV-2) — sprint-console pattern. No
  current cluster runs g5-sprint-console with chrome that would benefit
  (Aura's nav is already non-sticky · Elevate ships static). Defer to
  Phase X.7a if Aura/Elevate are picked.

---

## §3 · What changed on disk

### Source-file diff summary

| file | lines added | nature |
|---|---|---|
| `apps/catalog/template_dna.py` | +30 / -10 | MOTION_PROFILES extended with 2 keys per profile + 1 paragraph of in-place documentation explaining the implementation pass. |
| `apps/catalog/views.py` | +14 / -0 | 2 new flat context keys (`motion_card_lift` · `motion_cinematic_fade`) surfaced from the bundle config + 1 paragraph of in-place documentation. |
| `templates/live_templates/business/corporate-suite/_base.html` | +1 / -1 | Body tag emits 2 new conditional `data-motion-*` attributes (line 1220). |
| `static/css/live-motion.css` | +95 / -0 | `--mp-*` token namespace on `:root` (10 new tokens) + 4 new gate rules (card-lift idle + card-lift hover/focus + cinematic-fade hidden + cinematic-fade fired) + 2 reduced-motion short-circuit blocks (`@media` + `body.lm-reduced`). |
| `static/js/live-motion.js` | +35 / -0 | `setupCinematicFade()` IntersectionObserver wired in `init()` after `setupTime3()`. Identical one-shot semantics + threshold pattern to the slice-02 TIME-3 observer. |

Total source delta: **5 files · ~175 net lines added**.

### MOTION_PROFILES per-profile flag set (after this pass)

| profile | kpi_animate | nav_condense | evid5 | evid3 | time3 | **card_lift** | **cinematic_fade** |
|---|---|---|---|---|---|---|---|
| g1-safe-premium       | False | False | False | False | False | **False** | **False** |
| g2-editorial          | False | False | False | False | False | **False** | **False** |
| g2-editorial-counter  | True  | True  | True  | True  | True  | **False** | **False** |
| g3-institutional      | True  | False | False | False | False | **False** | **False** |
| g4-stewardship        | False | False | False | False | False | **False** | **False** |
| g5-sprint-console     | True  | False | False | False | False | **False** | **False** |
| g6-cinematic          | False | False | False | False | False | **False** | **True**  |

Bold = changed by this pass. The `g6-cinematic` row is the only profile
with the `cinematic_fade` flag opted in.

### Forbidden-pool encoding

- `card_lift_restrained` is **False on g2-editorial-counter** even though
  MICRO-2 is in g3-institutional's safe pool, because AT-G2C-4 in the
  motion-profile-dna-plan §5 forbids card-lift on the LF-2 magazine-grid
  3+1 (CASE-1 cards stay still). Causa is the only g2-editorial-counter
  occupant today; it must not flip card-lift.
- `cinematic_fade` is **False on every g1-g5 profile** because the slow
  editorial fade-in collapses the institutional / safe / sprint registers
  to a register that reads "this is a portfolio site" rather than "this
  is a corporate site." Anti-fit per motion-profile-dna-plan §3.

---

## §4 · Token structure

The new `--mp-*` tokens live on `:root` in `static/css/live-motion.css`:

```css
/* MICRO-2 card-lift-restrained · safe-pool of g1/g3/g5 */
--mp-card-lift-y:        3px;     /* AT-G1-2 ceiling */
--mp-card-lift-shadow:   0 6px 16px -8px rgba(15, 18, 22, 0.10);
--mp-card-lift-dur:      var(--lm-dur-fast);  /* 360ms */
--mp-card-lift-ease:     var(--lm-ease-smooth);

/* MEDIA-1 cinematic-fade-on-view · g6-cinematic claim */
--mp-cinematic-dur:               1200ms;  /* AT-G6-2 floor */
--mp-cinematic-opacity-start:     0.7;
--mp-cinematic-saturation-start:  0.85;     /* AT-G6-2 floor */
--mp-cinematic-scale-start:       1.04;     /* AT-G6-2 ceiling */
--mp-cinematic-ease:              cubic-bezier(0.22, 0.61, 0.36, 1);
```

Three properties of this token namespace:

1. **Anti-tacky values are encoded · not configurable.** `--mp-cinematic-
   dur` cannot be set below 1200ms without a code edit. `--mp-card-lift-y`
   cannot exceed 3px without a code edit. The system structurally cannot
   ship the flashy version of either pattern.
2. **Profile-scoped overrides are paper-allowed · code-deferred.** A
   future profile that legitimately needs a slower fade (e.g., a
   `g6-cinematic-stewardship` hybrid) can scope:
   ```css
   body[data-motion-profile="g6-cinematic-stewardship"] {
     --mp-cinematic-dur: 1600ms;
   }
   ```
   No such profile exists today.
3. **Easing reuses the existing `--lm-ease` family.** All transitions
   share the cubic-bezier(0.22, 0.61, 0.36, 1) (ease-out) and 0.33-curve
   already vetted across the slice-01/02 + reveal + marquee patterns.
   No new easing function is introduced.

---

## §5 · Reveal sequencing logic

The cinematic-fade pattern uses a different reveal hook from the existing
`data-lm` system:

- **Existing**: `data-lm="reveal"` / `data-lm="reveal-soft"` / `data-lm-
  stagger` — generic content-block reveals · 720ms · vertical translate.
  Active on every live archetype (Cornice / Causa / Continua / Pixel /
  Vertex / Aura / etc.)
- **New (cinematic-only)**: `data-motion-fade-in` — full-bleed photo
  fade · 1200ms · opacity 0.7→1 · saturate 0.85→1 · scale 1.04→1 ·
  active ONLY when `body[data-motion-cinematic-fade="1"]`.

The two systems coexist on the same page without interference. A
hypothetical g6-cinematic template can emit both:

```html
<section data-lm="reveal-soft">
  <h2>...</h2>                                   <!-- generic editorial reveal -->
  <img data-motion-fade-in src="...">            <!-- cinematic photo fade -->
</section>
```

Each hook fires when its observer fires (different thresholds: 0.15
for `data-lm`, 0.20 for `data-motion-fade-in`); both unobserve on
intersect (one-shot · no re-trigger on scroll-back · matches AT-X4
red-line).

---

## §6 · Hover / card response class

The MICRO-2 card-lift hook is `[data-motion-card]`. Production usage:

```html
<a class="case-card" data-motion-card href="...">
  <h3>Case study title</h3>
  <p>Excerpt...</p>
</a>
```

CSS rule pair:

```css
body[data-motion-card-lift="1"] [data-motion-card] {
  transition:
    transform   var(--mp-card-lift-dur) var(--mp-card-lift-ease),
    box-shadow  var(--mp-card-lift-dur) var(--mp-card-lift-ease);
}
body[data-motion-card-lift="1"] [data-motion-card]:hover,
body[data-motion-card-lift="1"] [data-motion-card]:focus-within {
  transform: translate3d(0, calc(-1 * var(--mp-card-lift-y)), 0);
  box-shadow: var(--mp-card-lift-shadow);
}
```

Why `:focus-within` and not `:focus`: the production card pattern is
typically a wrapper containing a focus-able link or button. `:focus-within`
matches the wrapper when ANY descendant focuses. Keyboard navigation
gets the same lift-with-shadow as mouse hover · accessibility parity.

The pure-CSS approach intentionally has NO JS scaffolding. There is no
observer to gate. The `:hover`/`:focus-within` pseudo-classes are the
trigger; the body data-attribute is the profile gate. Reduced-motion
short-circuits via the existing `body.lm-reduced` class plus the
explicit `@media (prefers-reduced-motion: reduce)` rule.

---

## §7 · Timeline / proof / citation interaction (already shipped)

The slice-01 + slice-02 bundle covers:
- TIME-3 chronological-tick-horizontal · slice-02 · `body[data-motion-time3="1"]`
- EVID-3 case-citation-pop · slice-02 · `body[data-motion-evid3="1"]`
- EVID-5 provenance-tooltip-image · slice-01 · `body[data-motion-evid5="1"]`
- KPI-2 count-up-on-view · slice-01 · `body[data-motion-kpi-animate="1"]`
- NAV-1 sticky-condensed-on-scroll · slice-01 · `body[data-motion-nav-condense="1"]`

This pass adds:
- MICRO-2 card-lift-restrained · `body[data-motion-card-lift="1"]`
- MEDIA-1 cinematic-fade-on-view · `body[data-motion-cinematic-fade="1"]`

Total wired bundle flags: **7**. Total paper-flagged (un-wired): **5**
(scroll_progress_bar · hero_parallax · gallery_snap · magnetic_button ·
cursor_vignette · live_data_kpi · nav_hide_on_scroll_down — minus the
already-paper-listed flags this pass had to revisit).

---

## §8 · Reduced-motion equivalents (per profile)

The plan §6 reduced-motion table is honored by this pass on three layers:

### Layer 1 · JS root short-circuit

`static/js/live-motion.js` line 50-60: when `window.matchMedia('(prefers-
reduced-motion: reduce)').matches` returns `true`, the entire animation
pass aborts before any observer is created. Body gets `lm-ready` AND
`lm-reduced` classes. The new `setupCinematicFade()` function is
positioned AFTER this short-circuit, so it never runs under reduced-
motion.

### Layer 2 · `body.lm-reduced` class-based CSS short-circuit

`static/css/live-motion.css` adds two new blocks:

```css
body.lm-reduced[data-motion-card-lift="1"] [data-motion-card] {
  transition: none !important;
}
body.lm-reduced[data-motion-card-lift="1"] [data-motion-card]:hover,
body.lm-reduced[data-motion-card-lift="1"] [data-motion-card]:focus-within {
  transform: none !important;
  box-shadow: none !important;
}
body.lm-reduced[data-motion-cinematic-fade="1"] [data-motion-fade-in] {
  opacity:   1 !important;
  filter:    none !important;
  transform: none !important;
  transition: none !important;
}
```

### Layer 3 · `@media (prefers-reduced-motion: reduce)` for JS-off clients

Same rules wrapped in the native media query so that a JS-disabled
client whose browser still honors the OS preference also gets the
static fallback. Belt + braces.

### Verification

The browser-verification report walks both gates under both default-
motion and reduced-motion. Computed styles confirm:
- Default-motion + body data-attr ON: probe element starts at opacity
  0.7 / scale 1.04 / saturate 0.85; transitions to 1/1/1 over 1200ms
  when `.lm-fade-in` is added.
- Reduced-motion + body data-attr ON: probe element starts at opacity
  1 / no transform / no filter; transition is `none`.
- Default-motion + body data-attr ON, focus simulated: card translates
  -3px after 360ms transition, shadow appears.
- Reduced-motion + body data-attr ON, focus simulated: card transform
  stays `none`, no shadow, transition is `none`.

This satisfies AT-X1 (prefers-reduced-motion honored at JS root + CSS
layer) and the reduced-motion fallback contract per profile in
motion-profile-dna-plan §6.

---

## §9 · Anti-tacky constraints

The plan §5 anti-tacky red-lines for the two new flags:

| red-line | applied | how |
|---|---|---|
| AT-G1-2: card-lift ≤ 3px | ✓ | `--mp-card-lift-y: 3px` ceiling encoded in CSS variable. Cannot be raised without a code edit. |
| AT-G1-2: shadow blur ≤ 16px | ✓ | `--mp-card-lift-shadow: 0 6px 16px -8px rgba(15, 18, 22, 0.10)`. Blur capped at 16px. |
| AT-G1-2: shadow opacity ≤ 0.10 | ✓ | Alpha channel encoded as `0.10` in the shadow value. |
| AT-G2C-4: NO card-lift on magazine-grid 3+1 | ✓ | `g2-editorial-counter` ships `card_lift_restrained: False` (Causa cannot accidentally flip the lift on its LF-2 cards). |
| AT-G6-2: cinematic-fade duration ≥ 1200ms | ✓ | `--mp-cinematic-dur: 1200ms` floor encoded. |
| AT-G6-2: saturation start ≥ 0.85 | ✓ | `--mp-cinematic-saturation-start: 0.85`. |
| AT-G6-2: scale start ≤ 1.05 | ✓ | `--mp-cinematic-scale-start: 1.04` (≤ 1.05 ceiling). |
| AT-X1: prefers-reduced-motion honored | ✓ | 3-layer guarantee (§8). |
| AT-X2: no decorative motion | ✓ | Both flags map to documented patterns from the library; both have an information-test (the photo's CONTENT becomes legible after the fade · the card's interactability becomes legible at hover). |
| AT-X3: no manipulative-SaaS motion | ✓ | Neither pattern overrides visitor judgement. |
| AT-X4: no once-per-session re-trigger | ✓ | `setupCinematicFade()` calls `io.unobserve(entry.target)` on intersect — same one-shot semantics as `setupReveals` / `setupCounters` / `setupTime3`. |
| AT-X5: total stagger ≤ 1500ms | ✓ | Single-element fade (no stagger). |

---

## §10 · Regression boundaries

The slice ships behind a **default-False on every live template** flag
contract. Before the pass:

- 6 corporate-suite siblings each emit 0–5 `data-motion-*` flag attributes.
- 0 templates use `g6-cinematic` (Pixel/Villa/Vertex/Luxe currently default
  to `g3-institutional` because they don't declare a profile).

After the pass:

- 6 corporate-suite siblings each emit the SAME 0–5 flag attributes (zero
  change).
- 0 templates use `g6-cinematic` (same as before).
- The 2 new attributes (`data-motion-card-lift` · `data-motion-cinematic-
  fade`) are emitted on ZERO body tags across the entire catalog.

Verified by browser-walk · 6/6 frozen siblings byte-equivalent on body
attribute set. Computed-style probes on Cornice (g2-editorial) confirmed
zero new style impact when the body lacks the new data-attributes.

The verification cells are in
`factory/reports/scorecard/motion-profile-implementation-pass1/scorecard.md`.

---

## §11 · How motion_profile becomes user-customizable (path forward)

Layer-B (Phase X.7c · paper-deferred) maps the 7 internal profiles to a
3-tier customer-facing intensity slider per cluster. This pass does NOT
ship Layer-B. It ships the LAYER-A bedrock that Layer-B will read:

- The `MOTION_PROFILES` registry is the bounded universe.
- The cluster's allowed-profile set (motion-profile-catalog §3) is the
  fence.
- Bundle flags map 1-to-1 with patterns; turning a bundle flag on emits
  a body data-attribute; the data-attribute gates a CSS+JS pattern.
- Reduced-motion is the absolute floor; no customer setting can override
  it.

When Phase X.7c lands, it will:
- Add `motion_profile_intensity` (`minimal|standard|expressive`) to
  `apps/projects/models.py · ProjectDesignTokens` (Layer-B preset slot).
- Add an editor-side picker that reads the cluster's allowed-set from
  the source template's DNA + this `MOTION_PROFILES` registry.
- Renderer (in `apps/editor/rendering.py`) maps the customer's picker
  choice to a flag bundle subset within the cluster's tier ladder.

The mechanism for "how customization preserves variety" is documented
in motion-profile-dna-plan §10 (per-cluster preset narrowing · sibling-
aware flag claims · Layer-A reduced-motion floor). All three mechanisms
operate on the bundle-flag layer this pass extends.

---

## §12 · Workflow-gate verification matrix

Where this pass intersects the workflow gates per motion-profile-dna-plan §13:

| gate | what this pass adds |
|---|---|
| A.0 territory-scout | scout report can now name `card_lift_restrained` / `cinematic_fade` as intake-declared bundle flags · the catalog row for the candidate's cluster lists which flags are in the safe pool. |
| A.1 intake | brief schema (`next-template-brief-schema.md §1`) already requires `motion_profile`. This pass means the brief can name BOTH new flags as opt-ins from the cluster's allowed set. |
| A.2 plan | plan-side axis-18 scoring re-uses the matrix in motion-profile-dna-plan §7 unchanged. The new flag count moves the delta on the "≥3-flag delta" rubric for any future g3-or-g5 sibling. |
| A.5 build | builder edits `apps/catalog/template_dna.py` to add the per-template DNA entry with `motion_profile = "g6-cinematic"` (or another); the registry's flag map propagates to the body data-attribute through the CS chrome (or future non-CS chrome). |
| A.6 review-lock | style-critic walks the per-profile anti-tacky checklist in motion-profile-catalog §7. This pass adds card-lift + cinematic-fade red-lines to the AT-G1 / AT-G6 rows. |
| Workflow C/D walk | browser-verifier walks default-motion + reduced-motion; this pass's reduced-motion guarantee is verified across both probe gates. |
| Workflow D flip | gatekeeper scores axis 18 vs every existing sibling per motion-profile-dna-plan §7 rubric. The new wiring does NOT change today's scores (no flag flipped on any sibling). |

---

## §13 · Recommended next step

**Choose exactly one of**:

| option | description | leverage | block |
|---|---|---|---|
| A | personalization-layer contract (Phase X.7c · Layer-B 3-tier intensity slider on `ProjectDesignTokens`) | medium · unlocks customer-side motion variety | requires apps/editor + apps/projects edits · explicit out-of-scope this slice |
| **B** | Causa workflow C multilingual (Causa 1 → 5 locales · IT preserved · EN/FR/ES/AR added) | **HIGH · cluster-level visible delivery · LF-2 cell-pair voice + motion contract is now fully verifiable in code (paper + slice-01 + slice-02 + this pass)** | none · gated only on user-handshake |
| C | sibling 7 intake (Phase X.7a non-corporate-suite cluster · audit-recommended) | high · resolves S6 cluster-tropes rule · unblocks future 7th CS sibling | requires fresh A.0 territory-scout · larger scope |

**Recommendation: B · Causa workflow C multilingual.**

Reasoning:

1. **The motion_profile axis is now fully ratified, fully wired, and
   fully verifiable.** Cornice (g2-editorial · 0 flags) ↔ Causa (g2-
   editorial-counter · 5 flags) is the canonical demonstration of the
   axis-18 sub-variant differentiation. Shipping Causa in 4 more locales
   is the highest-leverage move because every multilingual surface
   ALREADY honors the motion_profile contract; the work is voice +
   imagery + RTL · not motion.
2. **Phase X.7a (option C) needs a fresh A.0 scout pass** for the
   non-CS cluster candidate (Vertex agency-creative-studio · Aura
   agency-digital-studio · Pixel portfolio-cinematic · Villa real-estate-
   ultra-luxury · Luxe ecommerce-fashion-editorial · Elevate startup-
   saas-landing). That is a new workflow loop · larger scope than
   workflow C/D for an already-IT-locked sibling.
3. **Phase X.7c (option A) requires apps/editor + apps/projects edits**
   that this slice explicitly avoided. The Layer-B preset ladder is
   READY in paper but cannot ship without taking the customer-side
   architecture pass.

The B path closes the LF-2 cell at corporate-suite cluster level
(Causa goes from 1 → 5 locales · Cornice + Solaria + Pragma + Fiscus +
Continua have been at 5 locales since their respective public flips).
That is the cluster-coverage move · not the cluster-expansion move.

After B closes, the next implementation pass should be either A (Phase
X.7c · Layer-B preset) or C (Phase X.7a · 1st non-CS cluster) on user
handshake.

---

## §14 · One-paragraph summary

motion_profile is now a first-class DNA axis the planner declares at
A.1 intake AND can verify in code at first paint. Two new bundle-flag
gates landed: MICRO-2 `card_lift_restrained` (pure-CSS · ≤3px translate ·
≤16px shadow blur · safe-pool of g1/g3/g5) and MEDIA-1 `cinematic_fade`
(CSS+JS observer · opacity 0.7→1 + saturate 0.85→1 + scale 1.04→1 over
1200ms · g6-cinematic claim). The `g2-editorial-counter` profile (Causa
· 5 flags) is live in production as the evidence-led / reactive
demonstration; the `g6-cinematic` profile is wired in code and ready
for the first Phase X.7a non-corporate-suite intake to declare it. Both
gates honor `prefers-reduced-motion: reduce` on three layers (JS root +
body class + native media query). All 6 frozen corporate-suite siblings
emit the SAME body attributes as before this pass (0 flags newly
emitted). 546/546 Django tests still PASS. The recommended next pass
is workflow C multilingual for Causa (option B) — the LF-2 cell-pair
voice + motion contract is now fully cross-referenced in code, and
shipping Causa to 4 more locales is the highest-leverage corporate-
suite cluster-coverage move available.
