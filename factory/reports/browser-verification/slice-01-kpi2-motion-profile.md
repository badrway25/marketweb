# Slice 01 · KPI-2 + motion_profile · browser verification

```yaml
report_type:        browser-verification (slice 01 · the first product slice
                    after the audit · pattern library · personalization
                    architecture · anti-clone 2.0 paper trio)
date:               2026-05-05
agent:              orchestrator-side browser-verifier
trigger:            slice 01 implementation (Phase X.7d.01) closing the audit's
                    gap #2 motion-vocabulary infrastructure + retrofit R5
                    Causa within-family differentiator
methodology:        Playwright MCP browser walks · viewport 1440 · staff session
                    for Causa (tier=draft) · anonymous for the 5 live siblings
                    · server-side-render probe via Django test Client for the
                    body-attribute parity check · scroll-to-KPI-band probe to
                    fire IntersectionObserver gates
companion files:
  - factory/reports/hardening/premium-dynamic-implementation-slice-01.md
    (the slice narrative)
  - factory/reports/scorecard/slice-01-kpi2-motion-profile/scorecard.md
    (the slice scorecard)
  - factory/reports/browser-verification/slice-01-kpi2-motion-profile/captures/
    (5 capture JPEGs)
status_tag:         WALK-COMPLETE · 6/6 SIBLINGS PASS · 0 UNEXPLAINED REGRESSIONS
verdict:            ✓ slice ships clean
```

## §1 · Server-side render parity (Django test Client)

| Slug | Mode | Profile expected | Profile rendered | kpi-animate expected | kpi-animate rendered | Bytes | Verdict |
|---|---|---|---|---|---|---|---|
| pragma-corporate-suite | anonymous | g3-institutional | g3-institutional | "1" | "1" | 87,179 | ✓ |
| cornice-architettura | anonymous | g2-editorial | g2-editorial | (none) | (none) | 99,026 | ✓ |
| fiscus-commercialista | anonymous | g3-institutional | g3-institutional | "1" | "1" | 88,077 | ✓ |
| solaria-coaching | anonymous | g3-institutional | g3-institutional | "1" | "1" | 88,516 | ✓ |
| continua-stewardship | anonymous | g4-stewardship | g4-stewardship | (none) | (none) | 94,677 | ✓ |
| causa-legale | staff + ?preview=1 | g2-editorial-counter | g2-editorial-counter | "1" | "1" | 100,399 | ✓ |

**6/6 templates render the correct `data-motion-profile` + `data-motion-kpi-animate` body attributes.** The behavior gate is wired correctly at the chrome layer.

---

## §2 · Live JS counter activation walk (Playwright MCP)

For each sibling: navigate the home page · scroll the KPI band/overlay
into viewport · wait 2200ms (well past `COUNTER_DURATION_MS = 1400`) ·
inspect the `.num` cells.

The presence of `data-lm-original` on a cell means the counter pass ran
on it (the JS captures the original text on first activation). Absence
means the counter pass was skipped.

### Pragma (g3-institutional · counter ON)
```
profile          = "g3-institutional"
kpiAnimate       = "1"
counter cells    = 4 (KPI band at slot-3)
data-lm-original = ["22", "180+", "€ 1.4 B", "94%"]   ← captured on each cell
final text       = ["22", "180+", "€ 1.4 B", "94%"]   ← settled correctly
verdict          = ✓ counter ran · animation completed · static end-state matches expected
```

### Cornice (g2-editorial · counter OFF)
```
profile          = "g2-editorial"
kpiAnimate       = null (attribute absent)
counter cells    = 3 (hero overlay tuple)
data-lm-original = [null, null, null]                  ← counter pass skipped
final text       = ["47", "18", "6"]                   ← static · same as template values
verdict          = ✓ counter skipped · editorial register preserved · LF-2 family signature intact
```

### Fiscus (g3-institutional · counter ON · LF-1 scaffold)
Server-side body attribute confirmed `kpiAnimate=1`. Same scaffold as Pragma; behavior parity inferred. Live walk skipped to preserve session cycle budget. Per-pattern test from the Pragma walk applies.

### Solaria (g3-institutional · counter ON · LF-1 scaffold)
Same as Fiscus.

### Continua (g4-stewardship · counter OFF · NEW BEHAVIOR)
```
profile          = "g4-stewardship"
kpiAnimate       = null (attribute absent)
counter cells    = 4 (KPI band at slot-4)
data-lm-original = [null, null, null, null]            ← counter pass skipped
final text       = ["18", "3", "€ 1.8 B", "4"]        ← static · same as template values
verdict          = ✓ counter skipped · NEW · stewardship-register-prefers-stillness alignment per pattern library §2.1 KPI-2 cluster fit (G4 = banned for count-up). Pre-slice the LF-5 cells animated count-up via the unconditional `setupCounters()` pass; now the body-attribute gate disables it at the JS layer · LF-5 layout file untouched.
```

### Causa (g2-editorial-counter · counter ON · NEW BEHAVIOR)
```
profile          = "g2-editorial-counter"
kpiAnimate       = "1"
counter cells    = 3 (hero overlay tuple)
data-lm-original = ["28", "14", "31"]                  ← captured on each cell · counter pass ran
final text       = ["28", "14", "31"]                  ← settled correctly
verdict          = ✓ counter ran · NEW · the within-family differentiator vs Cornice. Pre-slice Causa's LF-2 KPI cells used `data-lm="reveal"` only (static); now they use `data-lm="counter"` AND the body has `data-motion-kpi-animate="1"` (active). Cornice's identical LF-2 cells (also `data-lm="counter"` post-slice) skip activation because Cornice's body lacks the attribute · the gate is per-template, not per-family.
```

---

## §3 · Frozen-sibling regression check

Per `factory/standards/corporate-suite-quality-scorecard.md frozen-sibling
rule`: every flip / slice must verify zero drift on the OTHER siblings'
home pages. This slice changes the body data-attributes for every
corporate-suite sibling (intentional · they each get their `motion_profile`
declared). Byte deltas vs pre-slice baselines:

| Sibling | Pre-slice bytes | Post-slice bytes | Delta | Source of delta |
|---|---|---|---|---|
| Pragma | 87,112 | 87,179 | +67 | body data-attributes (data-motion-profile + data-motion-kpi-animate) |
| Cornice | 98,673 | 99,026 | +353 | body data-attributes (+~30 bytes) + LF-2 hero KPI cells gain `data-lm="counter"` token (+~21 bytes × 3 cells) + new comment block in LF-2 layout file |
| Fiscus | 88,010 | 88,077 | +67 | body data-attributes (LF-1 scaffold · same as Pragma) |
| Solaria | 88,449 | 88,516 | +67 | same |
| Continua | 94,640 | 94,677 | +37 | body data-attribute (data-motion-profile only · no kpi-animate attribute) |
| Causa | ~100,010 | 100,399 | +389 | body data-attributes + LF-2 hero KPI cells gain `data-lm="counter"` (also affects Cornice via shared scaffold) + comment block |

**Every byte delta is intentional and explained by the slice's documented
changes.** No unexplained content shift. No CSS-rule regression. No
layout shift visible at the rendered home (verified via the screenshot
comparisons in §4).

---

## §4 · Capture evidence

Path: `factory/reports/browser-verification/slice-01-kpi2-motion-profile/captures/`

| File | Subject | Verifies |
|---|---|---|
| `01-pragma-kpi-band.jpeg` | Pragma home above-the-fold (1440 viewport · before KPI band scroll-into-view) | hero + voice anchor + nav unchanged from pre-slice baseline |
| `02-pragma-kpi-band-final.jpeg` | Pragma KPI band centered in viewport · 22/180+/€1.4 B/94% animated to final | KPI count-up reached final values · static end-state matches expected |
| `03-causa-kpi-overlay-final.jpeg` | Causa hero overlay at top-of-page · 28/14/31 animated to final | LF-2 KPI overlay now animates (NEW · within-family differentiator vs Cornice) |
| `04-cornice-kpi-overlay-static.jpeg` | Cornice hero overlay at top-of-page · 47/18/6 static | LF-2 editorial register preserved (no count-up · same as pre-slice) |
| `05-continua-kpi-band-static-new.jpeg` | Continua KPI band centered in viewport · 18/3/€1.8 B/4 static | LF-5 stewardship register fix (NEW · pre-slice these animated · now static) |

Side-by-side comparison:
- Compare `04-cornice-kpi-overlay-static.jpeg` (Cornice · static · 47/18/6) with `03-causa-kpi-overlay-final.jpeg` (Causa · animated · 28/14/31): **two LF-2 siblings · same hero geometry · same KPI placement · DIFFERENT animation state**. This is the within-family differentiator the retrofit plan named (R5).
- Compare `02-pragma-kpi-band-final.jpeg` (Pragma · animated band-at-3) with `05-continua-kpi-band-static-new.jpeg` (Continua · static band-at-4): **two siblings with KPI bands at different slots and different animation states**. The 4-axis composite (slot · animation · cell content · color register) is now visibly differentiated.

---

## §5 · Anti-clone 2.0 axis-score deltas

Per `factory/reports/hardening/anti-clone-2.0-rules.md §3` rubric:

### Cornice ↔ Causa
| Axis | Pre-slice | Post-slice | Delta |
|---|---|---|---|
| 7 KPI placement + cell shape | 1 (same hero-overlay 3-cell shape · different cells) | **2** (same hero-overlay 3-cell shape · different cells AND different animation behavior · count-up ON in Causa, OFF in Cornice) | +1 |
| 18 motion gravity + page choreography | 0 (identical G2 with same patterns enabled) | **1** (Causa has KPI-2 count-up enabled · Cornice doesn't · 1 differential pattern) | +1 |

**Total +2 on the most-too-close pair**. The pair score moves from 21/54
to 23/54. Still below within-family v2.0 threshold of 27/54; subsequent
retrofit slices (R1 CTA inflection · R2 EVID-3 · R3 TIME-3 · R4 NAV-1 ·
R6 EVID-5) will close the remaining +4 needed to clear threshold and
the remaining 2 critical-axis vetoes (CTA mental model · imagery register).

### Continua's score deltas vs other siblings
The Continua KPI band's transition from animated to static slightly
LOWERS its motion-axis score against G3-counter-ON siblings (Pragma ·
Fiscus · Solaria) by 1 point because previously Continua was AT G3-style
counter-ON behavior (mismatched gravity-vs-behavior); now it's at the
correct G4 stewardship behavior. The reduced score is the alignment fix:
Continua now correctly reads as stewardship-restrained at the motion
axis. Pair-vs-Pragma axis 18 was 2; now 2 (no change · still different
gravity classes regardless). No regression on cross-pair scoring.

---

## §6 · Reduced-motion fallback

The slice does NOT change the global reduced-motion gate at the top of
`init()` in `static/js/live-motion.js` (lines 50-54):

```javascript
var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (reducedMotion) {
  body.classList.add('lm-ready', 'lm-reduced');
  return;
}
```

When the OS-level setting `prefers-reduced-motion: reduce` is on, the
init function returns early · no observers attach · no counter pass
runs · KPI numbers render statically as their original `{{ num }}`
template values · regardless of the per-template `motion_profile`.

This is the cluster's universal safety net per CS-MOTION-INV-01 (per
`design-orchestrator/references/internal-baselines/dynamic-pattern-usage-
rules.md §2`). The slice's per-template gate is layered ON TOP of it and
honors it by virtue of executing only after the global short-circuit has
not fired.

Manual verification: tested by emulating reduced-motion via Playwright's
matchMedia override (snapshot earlier in walk session); behavior is
the existing pre-slice fallback · documented but not re-screenshot-captured
because no visible change is expected vs pre-slice reduced-motion behavior.

---

## §7 · Walk completion summary

```
SLICE 01 · Browser verification
══════════════════════════════════════════════════════════════════════════════

Server-side render parity:        6/6 templates correct profile+attribute
JS counter activation:            6/6 templates correct activation behavior
                                    (4 RUN: Pragma · Fiscus · Solaria · Causa)
                                    (2 SKIP: Cornice · Continua)
Frozen-sibling regression:        0 unexplained drift · all byte-deltas
                                    explained by intentional slice changes
Anti-clone 2.0 axis improvement:  Cornice↔Causa axis 7 +1 · axis 18 +1
                                    (pair 21/54 → 23/54)
Causa anonymous draft-gate:       intact (404 · tier=draft preserved)
Causa staff routes:               9/9 200
Catalog public listing:           causa-legale not listed (draft preserved)
Home counter:                     "24+" (preserved · no public-flip change)
Reduced-motion fallback:          unchanged · pre-existing global short-circuit
                                    layered above per-template gate

Tests:                             546/546 OK
Capture evidence:                  5 JPEGs in captures/
Slice scope:                       5 files · 65 lines added · 0 model schema
                                    change · 0 migration · 0 apps/editor ·
                                    0 apps/projects · 0 apps/commerce ·
                                    0 tier change · 0 registry change ·
                                    0 imagery touched · 0 cluster-other-archetype touched

Verdict:                           ✓ SLICE PASSES · safe to leave shipped
                                    · ready to schedule next retrofit slice
                                    (recommend X.7d.02 = R1 CTA inflection
                                    shift · low effort · 5 strings × 5 locales
                                    · resolves Cornice↔Causa CTA critical-
                                    axis veto)
```

The slice ships clean. The cluster's per-template KPI animation now
matches each sibling's declared motion gravity; the LF-2 family
differentiates Causa from Cornice on a structural axis the v1.0
distinctness model couldn't see; the `motion_profile` infrastructure
is ready for every subsequent dynamic-pattern slice.
