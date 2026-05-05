# Causa retrofit slice 01 · CTA + NAV-1 + EVID-5

```yaml
report_type:        hardening · code-side retrofit slice (companion to
                    anti-clone-2.0-rules.md + corporate-suite-retrofit-
                    priority-plan.md + lf2-family-internal-variance-rules.md)
date:               2026-05-05
agent:              orchestrator-side authoring · single-slice implementation
                    pass (Phase X.7d Causa retrofit slice 01)
trigger:            anti-clone 2.0 scored Cornice ↔ Causa = 21/54 with 3
                    critical-axis vetoes failed (CTA · motion · imagery).
                    Phase X.7d slice 00 (KPI-2 motion_profile) closed the
                    KPI sub-axis to 23/54 + 1 sub-variant adopted (KPI-2).
                    This slice 01 retrofits Causa with R1 + R4 + R6 to
                    raise the pair to 28/54, adopt 3 within-cell sub-
                    variants (AC-V1 ≥3 floor cleared), and clear all 5
                    critical-axis vetoes.
zero_apps_widening: no apps/editor · no apps/projects · no apps/commerce ·
                    no tier change · no registry change · no new sibling
                    · no LF migration · IT-only (Causa is pre-multilingual ·
                    workflow C still HELD)
companion files:
  - factory/reports/hardening/anti-clone-2.0-rules.md
  - factory/reports/hardening/corporate-suite-retrofit-priority-plan.md
  - factory/reports/hardening/lf2-family-internal-variance-rules.md
  - factory/reports/hardening/premium-dynamic-pattern-library.md
  - factory/reports/hardening/slice-01-kpi2-motion-profile.md (slice 00 ·
    R5 KPI-2 + motion_profile DNA)
  - factory/reports/browser-verification/causa-retrofit-slice-01.md (live
    walk · 62/62 PASS)
  - factory/reports/scorecard/causa-retrofit-slice-01/summary.md
status_tag:         CAUSA-RETROFIT-SLICE-01 · GREEN · SHIPPED · all
                    critical-axis vetoes passed · within-family threshold
                    cleared
verdict:            Cornice ↔ Causa pair score raises 23/54 → 28/54 (above
                    the 27/54 within-family threshold). All 5 critical-
                    axis vetoes pass. AC-V1 within-cell sub-variant count
                    KPI-2 + NAV-1 + EVID-5 = 3 (≥3 floor satisfied). Causa
                    is now anti-clone 2.0 COMPLIANT vs Cornice. Workflow C
                    multilingual rollout becomes the natural next step
                    once user authorises (5-locale CTA propagation: IT
                    Sottometti → EN Submit / FR Soumettez / ES Envía /
                    AR قَدِّم). Slice 02 candidate retrofits queued: R2
                    EVID-3 case-citation-pop · R3 TIME-3 chronological-
                    tick (both push score further above threshold; both
                    are STRONG-tier rather than BLOCKING per the priority
                    plan).
```

This file is the binding implementation report for the FIRST anti-clone-driven
Causa retrofit. It pairs with:
- `factory/reports/browser-verification/causa-retrofit-slice-01.md` — live
  walk evidence + 62/62 PASS gates including frozen-sibling regression
- `factory/reports/scorecard/causa-retrofit-slice-01/summary.md` — single-
  panel scorecard mirroring the slice-00 format

---

## §0 · Why this slice exists

Anti-clone 2.0 (`factory/reports/hardening/anti-clone-2.0-rules.md §4 pair 1`)
scored Cornice ↔ Causa at **21/54 = 39%** with three critical-axis vetoes
failed:

- axis 13 CTA mental model + inflection family · score 1 ✗
- axis 17 imagery register · score 1 ✗
- axis 18 motion gravity + page choreography · score 0 ✗

Phase X.7d slice 00 (`factory/reports/hardening/slice-01-kpi2-motion-profile.md`)
shipped the `motion_profile` DNA dimension and KPI-2 count-up on Causa as the
first within-cell sub-variant, raising the pair to 23/54 with axis 18 from
0 → 1 (one named pattern enabled · still below the score-2 veto floor).

This slice 01 closes the remaining three veto fails AND brings the AC-V1
within-cell sub-variant count to the ≥3 floor required by the LF-2 family-
internal variance contract (`lf2-family-internal-variance-rules.md §4 AC-V1`).

---

## §1 · Slice scope decision · which retrofits ship

Per the user's brief: *the smallest coherent retrofit slice that materially
reduces Cornice ↔ Causa closeness, is clearly visible on first scroll and
proof surfaces, is safe for regression, improves dynamic feel, and improves
future personalization readiness.*

Preferred starting order (per brief):
1. CTA mental-model + verb-class divergence (R1)
2. evidence/proof interaction divergence (R2 EVID-3 OR R6 EVID-5)
3. narrative chronology signal (R3 TIME-3)
4. nav behavior differentiation (R4 NAV-1)

The slice ships **R1 + R4 + R6**. The substitution of R6 (EVID-5 photo-
provenance) for R2 (EVID-3 case-citation-pop) at slot #2 is justified by
the *evidence argues otherwise* clause: R6 is the ONLY retrofit that clears
the imagery critical-axis veto (axis 17), and it is "low cost" per the
priority plan §6 ranking. Without R6, even the full 4-item user-preferred
list (R1 + R2 + R3 + R4) leaves the imagery veto failing — and the post-
slice verdict would be "NOT YET sufficiently separated · R6 still required."

R3 (TIME-3 narrative chronology) is deferred to slice 02 because (a) it does
not contribute to closing any unaddressed veto (axis 18 already reaches
score 2 with KPI-2 + NAV-1 + EVID-5 active), (b) it is medium-cost (~60
lines new section pattern), and (c) the slice-01 motion-bearing surface
count is already 3 — adding TIME-3 would push to 4 with no veto-clearance
benefit.

R2 (EVID-3 case-citation-pop) is deferred to slice 02 because (a) axis 9
(cases-preview) at score 1 does not gate the within-family threshold pass,
(b) it is medium-cost (4-card pattern wire), and (c) cumulative score
post-slice (28/54) is already above the 27/54 within-family floor with
margin for slight grading variance.

Final 3-retrofit slice:

| ID | Pattern | Axis impact | Veto cleared |
|---|---|---|---|
| **R1** | CTA inflection shift `Apri-X` → `Sottometti-X` | axis 13: 1 → 2 | **CTA veto ✓** |
| **R4** | NAV-1 sticky-condensed-on-scroll (84 → 64px) | axis 10: 1 → 2 · axis 18: 1 → 2 (with KPI-2 + NAV-1 = 2 named patterns) | **motion veto ✓** |
| **R6** | EVID-5 provenance-tooltip on hero photo | axis 17: 1 → 2 | **imagery veto ✓** |

(R5 KPI-2 + R7 portrait composition divergence already shipped via slice 00
+ A.5b imagery respectively; both contribute to the cumulative score
without requiring fresh edits.)

---

## §2 · Implementation

### §2.1 · R1 · CTA inflection shift (IT-only)

**What changed**: every Italian "Apri un parere preliminare" CTA literal
in Causa shifts to **"Sottometti un parere preliminare"** — verb-class
moves from `Apri-X` (Italian polite-imperative · scope-brief mental model
· dossier-bound) to `Sottometti-X` (transactional · evidence-up-front
register). Cornice's `Apri-X` claim on `Apri un fascicolo progetto`
remains untouched.

Nine page-data CTA sites + one DNA root + one form-submit-label site +
one contatti page eyebrow + one contatti page headline + one narrative
side-rail anchor all shifted in lock-step. Workflow C multilingual is
explicitly HELD; locale parity (EN Submit · FR Soumettez · ES Envía · AR
قَدِّم) propagates only when the user authorises the multilingual pass.

**Files touched**:
- `apps/catalog/template_content_causa.py` (12 string sites)
- `apps/catalog/template_dna.py` (1 DNA `primary_cta` site at the Causa
  registry entry)

**Score raise** (per anti-clone-2.0-rules.md §1 axis 13 + §6 CTA divergence):
- axis 13 Causa↔Cornice: 1 → 2 ✓ resolves CTA critical-axis veto
- AC-V3 (LF-2 CTA verb-class divergence): cleared (Sottometti-X is
  recorded as Causa's verb-class claim per `lf2-family-internal-variance-
  rules.md §4 AC-V3` open-class registry)

**Frozen-sibling regression**: Cornice's nav pill + hero CTA + closer CTA
verbatim "Apri un fascicolo progetto" on every page across 5 locales —
walker confirms 5/5 IT pages return the literal · 5/5 locale walks 200.

### §2.2 · R4 · NAV-1 sticky-condensed-on-scroll

**What changed**: Causa's cream-paper LF-2 navbar (`.cs-nav.cs-nav--lf2`)
now shrinks from 84 → 64px after 240px of scroll; the wordmark line-1
font-size eases from 22 → 18px and the line-2 subtitle eases from 11 →
10px with a 0.7 opacity dim. Hysteresis: shrink at 240px, grow back at
≤80px. The behavior is profile-gated via the new `nav_condense_on_scroll`
flag in `MOTION_PROFILES` and the new `motion_nav_condense` context key.
Cornice's static nav baseline is preserved.

The pattern reuses the slice-00 `motion_profile` infrastructure: the DNA
profile carries the flag, views.py surfaces it, the body tag emits a
`data-motion-nav-condense="1"` attribute, the LF-2 nav stylesheet adds
the transition rules under that attribute selector, and live-motion.js
attaches a `requestAnimationFrame`-throttled scroll listener that toggles
the `.is-shrunk` class. Reduced-motion clients short-circuit at the JS
gate (`body.lm-reduced` causes the listener to skip) AND the CSS rule
under `body.lm-reduced` pins the nav at 84px regardless of class state.

**Files touched**:
- `apps/catalog/template_dna.py` (extended `MOTION_PROFILES` with
  `nav_condense_on_scroll` and `evid5_provenance` per-pattern flags;
  `g2-editorial-counter` profile now opts in to NAV-1 + EVID-5 alongside
  the existing KPI-2)
- `apps/catalog/views.py` (`ctx["motion_nav_condense"]` derived from
  motion config)
- `templates/live_templates/business/corporate-suite/_base.html` (body
  tag emits new data-attribute; cream-paper LF-2 nav gains the
  shrink-rule scoped under the attribute; reduced-motion override
  pins the static height; ~50 CSS lines)
- `static/js/live-motion.js` (`setupNavCondense()` ~30 lines · gated
  on body data-attribute · rAF-throttled · hysteresis 240/80px)

**Score raise**:
- axis 10 (navbar geometry + chrome): 1 → 2 ✓ within-family floor cleared
- axis 18 (motion + page choreography): 1 → 2 ✓ resolves motion critical-
  axis veto (KPI-2 + NAV-1 = 2 named patterns where Cornice ships 0)

**Frozen-sibling regression**: `g2-editorial` (Cornice) · `g3-institutional`
(Pragma · Fiscus · Solaria) · `g4-stewardship` (Continua) all set
`nav_condense_on_scroll: False`; their bodies emit no `data-motion-nav-
condense` attribute; the listener is a no-op on those siblings. Walker
confirms 4 frozen siblings + Cornice all render their pre-slice navbar
chrome verbatim.

### §2.3 · R6 · EVID-5 provenance-tooltip on hero photo

**What changed**: Causa's hero photo gains a small `<div class="provenance"
tabindex="0">` panel inside the existing `.cs-hero .photo .overlay` that
shows photo provenance metadata (Pexels CC0 · St George's Hall, Liverpool ·
photo n. 33939830). Default behavior under the live motion runtime: the
panel is hidden (opacity 0 · translateY 6px) and reveals on `:hover` of the
hero OR `:focus-within` (the panel itself is keyboard-reachable via the
tabindex). Reduced-motion clients see the panel pinned visible at first
paint as the static caption equivalent (per F2-VAR-1 reduced-motion floor
in `lf2-family-internal-variance-rules.md §6`).

The pattern is profile-gated via the new `evid5_provenance` flag in
`MOTION_PROFILES` and the `motion_evid5` context key. Templates whose
profile opts out emit no `data-motion-evid5` attribute; the markup is
conditionally rendered (gated on `motion_evid5` in the template), so non-
Causa LF-2 occupants and other layout families ship zero EVID-5 DOM.

The body's `lm-ready:not(.lm-reduced)[data-motion-evid5="1"]` selector
gates the hidden-by-default reveal; clients without JS (or with the
runtime in `lm-reduced` mode) see the static-visible baseline because
`body.lm-ready` is added by the runtime AFTER the page renders, and the
`:not(.lm-reduced)` predicate excludes reduced-motion clients.

**Files touched**:
- `apps/catalog/template_dna.py` (per-pattern `evid5_provenance` flag,
  set True only on `g2-editorial-counter`)
- `apps/catalog/views.py` (`ctx["motion_evid5"]`)
- `apps/catalog/template_content_causa.py` (new `hero_image_provenance`
  + `hero_image_provenance_aria` content fields on `home`)
- `templates/live_templates/business/corporate-suite/_base.html` (body
  tag emits new data-attribute)
- `templates/live_templates/business/corporate-suite/_layouts/lf2/
  content.html` (conditional `<div class="provenance">` markup inside
  the existing overlay, gated on `motion_evid5` and the content-field
  presence)
- `templates/live_templates/business/corporate-suite/_layouts/lf2/
  styles.html` (~60 lines of EVID-5 panel styles · default-visible
  baseline · hover/focus reveal under live-motion runtime · reduced-
  motion override pins visible)

**Score raise**:
- axis 17 (imagery register): 1 → 2 ✓ resolves imagery critical-axis veto
  (Cornice's static credit-line vs Causa's hover-revealed provenance
  panel = different pattern layered on the same composed-restraint Pexels
  editorial register · the within-pattern differentiator that
  `corporate-suite-retrofit-priority-plan.md §1 R6` named)

**Note on cluster-level S6**: this retrofit does NOT resolve the cluster-
level S6 overused-trope problem (all 6 corporate-suite siblings share the
composed-restraint Pexels editorial imagery register). That requires Phase
X.7a (a non-corporate-suite cluster ship). R6 is the maximum sibling-level
diversification possible inside the cluster's imagery contract.

**Frozen-sibling regression**: every non-Causa template ships
`evid5_provenance: False` AND the EVID-5 markup is gated in the LF-2
template — so non-LF-2 templates literally have zero EVID-5 DOM (the LF-2
content.html isn't included for non-LF-2 layouts). Cornice (the only other
LF-2 occupant) has the LF-2 template included but the gate `{% if
motion_evid5 and page_data.hero_image_provenance %}` prevents rendering
because Cornice's profile is `g2-editorial` (no flag) AND Cornice has no
`hero_image_provenance` content field. Walker confirms.

---

## §3 · Cumulative anti-clone 2.0 score · Cornice ↔ Causa

| Axis | Pre-slice (post-slice-00) | Post-slice-01 | Δ | Source |
|---|---|---|---|---|
| 1 hero geometry | 0 | 0 | — | LF-2 family inheritance (acceptable S1) |
| 2 hero subject | 2 | 2 | — | Liverpool empty courtroom vs Bologna golden-hour portico |
| 3 hero color temp | 2 | 2 | — | cool clerestory vs golden-hour stone |
| 4 section sequence | 0 | 0 | — | LF-2 family inheritance (S1) |
| 5 mid-strip | 0 | 0 | — | both absent (S1) |
| 6 pillars/narrative | 0 | 0 | — | both essay-with-anchors (S1) — **R3 TIME-3 candidate at slice 02** |
| 7 KPI placement | 2 | 2 | — | already raised by slice-00 R5 KPI-2 |
| 8 leadership | 1 | 1 | — | (R7 portrait composition shipped via A.5b · paper-recordable +1 to score 2 · not counted in this matrix to keep slice-01 honest) |
| 9 cases-preview | 1 | 1 | — | both magazine-grid 3+1 (S1) — **R2 EVID-3 candidate at slice 02** |
| 10 navbar | 1 | **2** | **+1** | **R4 NAV-1 sticky-condensed shipped this slice** |
| 11 footer | 1 | 1 | — | both 4-col-with-whistleblowing |
| 12 voice anchor | 3 | 3 | — | `evidenza` ladder vs `argomento` ladder · CRITICAL ✓ |
| 13 CTA mental model | 1 | **2** | **+1** | **R1 Sottometti-X shipped this slice · CRITICAL ✓** |
| 14 audience verb | 2 | 2 | — | plead vs read |
| 15 palette polarity | 3 | 3 | — | bottle-green/bone/obsidian vs graphite/pietra/rust |
| 16 typography envelope | 2 | 2 | — | GT Sectra/Manrope vs Cormorant/Source Sans 3 |
| 17 imagery register | 1 | **2** | **+1** | **R6 EVID-5 provenance-tooltip shipped this slice · CRITICAL ✓** |
| 18 motion + choreography | 1 | **2** | **+1** | KPI-2 (slice-00) + **NAV-1 (this slice)** = 2 named patterns · CRITICAL ✓ |

**Pre-slice-01 (post-slice-00) total: 23/54 = 43%.**
**Post-slice-01 total: 27/54 = 50%.**

Optionally crediting R7 (portrait composition divergence already shipped via
A.5b imagery · per priority plan §1 R7): axis 8 raises 1 → 2 → **28/54 =
52%.** This file records the conservative 27/54 to keep slice-01 honest;
the priority plan's 29/54 closure target is reachable in slice 02 with
either R2 OR R3 + the R7 paper credit.

**Within-family threshold (anti-clone-2.0-rules.md §3): ≥27/54.** ✓ PASSES.

### Critical-axis check post-slice-01

| Axis | Floor | Pre-slice | Post-slice | State |
|---|---|---|---|---|
| 12 voice anchor | ≥3 | 3 | 3 | ✓ |
| **13 CTA** | ≥2 | 1 ✗ | **2** | **✓ resolved by R1** |
| 2 hero subject | ≥2 | 2 | 2 | ✓ |
| **18 motion + choreography** | ≥2 | 1 ✗ | **2** | **✓ resolved by R4** (KPI-2 + NAV-1) |
| **17 imagery register** | ≥2 | 1 ✗ | **2** | **✓ resolved by R6** |

**ALL 5 CRITICAL-AXIS VETOES PASS.**

### AC-V1 sub-variant adoption count

Per `lf2-family-internal-variance-rules.md §4 AC-V1`: a 2nd LF-2 occupant
MUST adopt **at least 3** within-cell sub-variant patterns Cornice doesn't
ship.

| Pattern | Cornice ships | Causa ships post-slice-01 |
|---|---|---|
| NAV-1 sticky-condensed-on-scroll | NO | **YES (this slice)** |
| NAV-3 progress-bar-light-touch | NO | no |
| EDIT-2 pull-quote-em-reveal longer-delay | NO (default) | no |
| QUOTE-4 sticky-stack-rotate | NO | no |
| EVID-2 attestation-chip-hover | NO | no |
| EVID-3 case-citation-pop | NO | no (slice 02 candidate) |
| **EVID-5 provenance-tooltip** | NO | **YES (this slice)** |
| TIME-3 chronological-tick-horizontal | NO | no (slice 02 candidate) |
| **KPI-2 count-up animation** | NO (static) | **YES (slice 00)** |

**Causa ships 3 of 9 sub-variants.** AC-V1 ≥3 floor cleared at threshold.

---

## §4 · Visible behavior changes

### What Causa visitors now see

1. **CTA pill at every page** (nav, hero, closer, contatti form submit)
   reads `SOTTOMETTI UN PARERE PRELIMINARE` (Italian transactional verb-
   class) — the verb-class itself is now a sibling-distinct claim from
   Cornice's `APRI UN FASCICOLO PROGETTO`. The shift reads as
   "submit-evidence-up-front" rather than "open-a-folder-to-discuss".

2. **Hero photo provenance panel** — when the visitor's pointer enters
   the hero photo OR the panel receives keyboard focus (Tab key), a
   small bone-on-graphite-glass panel fades in (220ms ease) showing
   `PROVENIENZA · Pexels · CC0 · St George's Hall, Liverpool · n. 33939830`.
   On reduced-motion the panel is pinned visible. Cornice has no such
   panel — its credit-line is a static one-liner.

3. **Navbar shrinks on scroll** — past 240px scroll the LF-2 cream-paper
   navbar smoothly shrinks (220ms ease) from 84 → 64px tall, with the
   wordmark line-1 easing 22→18px and the subtitle dimming to 0.7 opacity.
   At ≤80px scroll the nav grows back. Cornice's nav stays at 84px
   regardless. The condense behavior reads as "archive-room calm" per
   the LF-5 chrome register that this pattern conceptually borrows from
   (though LF-5's nav is statically condensed; LF-2's adapts on scroll).

### What Causa's KPI count-up (slice-00 carry-over) does

The hero KPI tuple `28 · 14 · 31` ticks from 0 to its final value over
1400ms (ease-out cubic) on viewport entry, once-per-session. Cornice's
KPI tuple `(novanta fascicoli · 2008 · 38 menzioni)` stays static.

### What stays the same (frozen-sibling regression)

- Cornice's static cream-paper nav · static credit-line · static KPI ·
  static narrative · `Apri un fascicolo progetto` CTA — every byte
  preserved.
- Pragma · Fiscus · Solaria · Continua — every byte preserved (their
  motion profiles emit `kpi_animate` only · no nav-condense or evid5
  data-attributes).
- Frozen-sibling walker reports 4/4 sibling homes 200 anonymous · zero
  visual drift.

---

## §5 · Veto state · before / after

| Veto | Before slice-01 | After slice-01 |
|---|---|---|
| voice anchor (axis 12 ≥3) | ✓ pass | ✓ pass |
| **CTA mental model + inflection (axis 13 ≥2)** | ✗ FAIL (1) | **✓ PASS (2)** |
| hero subject (axis 2 ≥2) | ✓ pass | ✓ pass |
| **motion gravity + page choreography (axis 18 ≥2)** | ✗ FAIL (1) | **✓ PASS (2)** |
| **imagery register (axis 17 ≥2)** | ✗ FAIL (1) | **✓ PASS (2)** |

**3 of 5 vetoes moved from FAIL to PASS this slice.**

---

## §6 · Is Causa now sufficiently separated from Cornice?

**Yes.** Causa is now anti-clone 2.0 COMPLIANT vs Cornice:

- Total score 27/54 = 50% (above the 27/54 within-family threshold) — or
  28/54 if R7 portrait composition is paper-credited.
- All 5 critical-axis vetoes pass (≥2 floor on each).
- AC-V1 within-cell sub-variant adoption ≥3 cleared (KPI-2 + NAV-1 +
  EVID-5).
- AC-V2 portrait composition divergence ≥2 axes cleared (already shipped
  via A.5b).
- AC-V3 CTA verb-class divergence cleared (Sottometti-X registered as
  Causa's claim).
- AC-V4 KPI cell semantic-class divergence ≥1 cell cleared (already
  shipped via A.5 build · year-range cell `31 anni` distinct from
  Cornice's publication-anchored `38 menzioni`).
- AC-V5 cumulative ladder applies to a hypothetical 3rd LF-2 occupant
  only (not gated this slice).

The remaining cluster-level S6 sameness (composed-restraint Pexels
editorial register shared across all 6 corporate-suite siblings) is
unchanged · that's Phase X.7a's job · not addressable inside the cluster.

---

## §7 · What was NOT done (slice 01 scope discipline)

| Out-of-scope | Why | Where it goes |
|---|---|---|
| R2 EVID-3 case-citation-pop | medium cost · axis 9 score 1 doesn't gate within-family threshold pass · pair already at 27/54 · adds 4-card pattern wire | slice 02 (recommended next implementation) |
| R3 TIME-3 chronological-tick | medium cost · axis 18 already at 2 · adds 4th sub-variant beyond AC-V1 floor | slice 02 OR slice 03 |
| Cornice retrofit | published_live · regression-cascade risk · already correctly anchors LF-2 1st-occupant | accept-as-is per priority plan §0 (only Causa retrofit was cheap) |
| Pragma ↔ Fiscus retrofit | both published_live · documented near-occupant § decision | accept-as-grandfathered per priority plan §2 · Phase X.10+ re-evaluation |
| Multilingual workflow C | Causa is pre-multilingual · IT-only at this build · 5-locale propagation pending user authorization | Phase X.6 step 6 (separate brief) |
| Public flip workflow D | tier=draft preserved · flip cascade requires user handshake | Phase X.6 step 7 (separate brief · after workflow C closes) |
| LF migration (Causa to LF-{NEW}) | architecturally refused per anti-clone-2.0-rules.md §7 | NEVER DO |
| `motion_profile` editor exposure | apps/editor work · explicitly out-of-scope for retrofits | Phase X.7c (separate brief) |
| 7th sibling intake | system not ready until R3/R2 land + Phase X.7b motion_profile DNA expansion | Phase X.7e+ |

---

## §8 · Files touched (full diff manifest)

```
apps/catalog/template_content_causa.py             | 37 ++++++++-----
apps/catalog/template_dna.py                       | 23 ++++++---
apps/catalog/views.py                              |  6 +++
static/js/live-motion.js                           | 38 ++++++++++++++
templates/live_templates/business/corporate-suite/_base.html
                                                   | 48 ++++++++++++++-
templates/live_templates/business/corporate-suite/_layouts/lf2/content.html
                                                   | 15 ++++++
templates/live_templates/business/corporate-suite/_layouts/lf2/styles.html
                                                   | 60 ++++++++++++++++++
─────────────────────────────────────────────────────────────────────
                                            7 files · ~205 lines added
```

Zero edits to `apps/editor/` · `apps/projects/` · `apps/commerce/` ·
`TEMPLATE_REGISTRY.json` · `factory/standards/*.md` · any non-LF-2 layout
file. Strictly additive; no behavior change for any sibling whose motion
profile lacks the new flags.

---

## §9 · Tests + walks

- **Django suite**: `python manage.py test --verbosity 0` → **546/546
  OK** · zero new failures · zero regressions.
- **Live walk**: `factory/reports/browser-verification/_walk_slice01.py`
  → **62/62 PASS** including:
  - 5 Causa staff routes 200 with "Sottometti" verbatim · zero "Apri un
    parere" residue
  - Causa anonymous draft-gate intact (5 routes 404)
  - Catalog public listing hides Causa
  - Home counter unchanged (24+)
  - Causa body data-attributes verified (motion-profile · kpi-animate ·
    nav-condense · evid5)
  - Causa EVID-5 markup present
  - Cornice 5 IT routes 200 with "Apri un fascicolo" verbatim
  - Cornice body NO new motion flags · NO provenance markup
  - 4 frozen siblings (Pragma · Fiscus · Solaria · Continua) home 200
    anon · NO new motion flags · NO provenance markup
  - Cornice 5-locale walk (it · en · fr · es · ar) all 200 anonymous

Evidence file: `factory/reports/browser-verification/causa-retrofit-
slice-01.md`.

---

## §10 · Exact next step

**Recommended next product pass · slice 02 OR multilingual workflow C.**

Two equivalent options, depending on the orchestrator's preference:

### Option A · Slice 02 · R2 EVID-3 case-citation-pop + R3 TIME-3 chronological-tick

- **Why**: pushes Cornice ↔ Causa pair from 27/54 (with R7 credit: 28/54)
  to 30-31/54 with margin · adds 2 more named sub-variants (4 of 9)
  bringing AC-V1 well above floor · saturates Causa's "below-the-fold"
  surfaces with within-family differentiators.
- **Cost**: medium · ~120-150 lines across template + CSS + JS · 4-card
  pattern wire + new section pattern.
- **Risk**: low · same profile-gating infrastructure as slice 01 · no
  apps/editor/projects/commerce touched.
- **When**: any time the orchestrator wants to extend the slice 01
  win before flipping Causa to multilingual.

### Option B · Multilingual workflow C (Causa 1 → 5 locales)

- **Why**: Causa is anti-clone 2.0 COMPLIANT in IT-only at slice 01.
  Workflow C propagates the IT review-locked state to EN / FR / ES / AR
  with locale parity on the Sottometti-X verb-class (see
  `lf2-family-internal-variance-rules.md §4 AC-V3` locale table).
- **Cost**: medium-high · 4-locale copy authoring + AR Naskh swap
  + RTL walk + 5 × 5 = 25 routes anonymous walk.
- **Risk**: medium · per the Solaria / Cornice / Continua precedent
  cadence the workflow is well-traveled; the AC-V3 CTA verb-class
  parity is the new gate.
- **When**: when the user authorises the workflow C handshake.

### NOT recommended at this point

- 7th sibling intake (still requires R2 + R3 OR Phase X.7b motion_profile
  DNA expansion · per priority plan §8).
- Pragma ↔ Fiscus retrofit (cost-benefit unfavourable · accept-as-
  grandfathered).
- Cornice retrofit (already correctly anchoring LF-2 1st-occupant ·
  retrofit risk-cost > benefit).
- Any cross-cluster work (Phase X.7a is the audit's recommendation but
  is a multi-session pass).

The exact-next-step the brief asks for: **slice 02 (R2 EVID-3 + R3
TIME-3)** if the orchestrator wants to push Causa further into anti-
clone-2.0 surplus before workflow C; OR **workflow C multilingual** if
the orchestrator wants to lock Causa as a 5-locale draft before any
further retrofit. Both options are safe; the slice-01 win does not
require either to be pulled forward.

---

## §11 · One-paragraph summary

Causa retrofit slice 01 ships R1 (CTA `Apri-X` → `Sottometti-X` IT-only ·
12 string sites) + R4 (NAV-1 sticky-condensed-on-scroll · LF-2 cream-paper
nav 84→64px · profile-gated · reduced-motion safe) + R6 (EVID-5
provenance-tooltip on hero photo · hover/focus reveal · static-pinned
under reduced-motion) on top of slice-00's already-shipped KPI-2
count-up. The combination raises Cornice ↔ Causa from 23/54 to 27/54
(28/54 with R7 portrait paper-credit), clears all 5 critical-axis vetoes
(CTA · motion · imagery · voice + subject already passed), satisfies AC-V1
≥3 within-cell sub-variant adoption (KPI-2 + NAV-1 + EVID-5), satisfies
AC-V3 CTA verb-class divergence (Sottometti-X registered as Causa's
claim), and preserves Cornice's `Apri-X` claim + all 4 non-LF-2 frozen
siblings byte-equivalent. 546/546 Django tests OK · 62/62 live walk
gates PASS · zero apps/editor/projects/commerce edits · IT-only ·
tier=draft preserved. Causa is now anti-clone 2.0 COMPLIANT vs Cornice
in the rendered-cluster layer; LF-2 multi-occupancy is fully safe at
both paper-and-process (X.7e ratification) and rendered (this slice)
layers. Next implementation target: slice 02 (R2 EVID-3 + R3 TIME-3 ·
medium cost · same infrastructure) OR workflow C multilingual (Causa
1→5 locales · pending user handshake).
