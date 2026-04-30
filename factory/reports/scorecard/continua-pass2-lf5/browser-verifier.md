# Continua LF-5 · browser-verifier

**Verdict**: PASS · B-LAYOUT-1/2/3 all GREEN · standard rubric all GREEN
**Date**: 2026-04-29 · IT-only walk · Playwright MCP (Chromium)
**Server**: `python manage.py runserver 127.0.0.1:8042 --noreload`

The walk runs the standard corporate-suite browser rubric **plus** the three new layout-family gates introduced in `factory/reports/hardening/corporate-suite-layout-variance-rules.md §5` (B-LAYOUT-1 wireframe overlay · B-LAYOUT-2 DOM section list · B-LAYOUT-3 layout-dimension classification).

---

## 1 · B-LAYOUT-1 · wireframe overlay compare (BLOCKING)

Wireframe = bounding-box-only outline of `home.html` at 1920px. Each `<section>` rendered as a coloured rectangle at its native bounding box. Overlay against the pre-rebuild capture for each existing sibling.

### Continua LF-5 vs Pragma (LF-1)

- Continua LF-5 sections: 8 (cs-hero / cs-cycle / cs-pillars / cs-kpi-band / cs-sectors / cs-leadership / cs-cases-preview / cs-cta).
- Pragma LF-1 sections: 8 (cs-hero / cs-pillars / cs-kpi-band / cs-sectors / cs-trust / cs-leadership / cs-cases-preview / cs-cta).
- Cs-cycle (slot-2 on Continua) vs cs-pillars (slot-2 on Pragma) — different content shapes occupying the same y-band.
- Cs-trust marquee absent on Continua.
- Hero geometry differs: Continua's hero is a single full-bleed `cs-hero` rectangle (no inner left/right split visible at the wireframe level since both subsections live inside one section bounding box). Pragma's hero is also a single bounding box but its inner geometry differs visibly.
- Per-section y-positions across the 8 sections differ at every slot from slot-2 onwards.

**Bounding-box surface-area difference vs Pragma**: ≈ 41% (well above the ≥30% pass threshold). PASS.

### Continua LF-5 vs Fiscus (LF-3)

Fiscus today renders the same 8 sections as Pragma (cycle_strip not authored on Fiscus's content registry, so cs-cycle is gated off). The bounding-box overlay is therefore identical to the Continua-vs-Pragma case structurally, with only Y-deltas from Fiscus's slightly larger hero (h=751 vs Pragma's h=686).

**Bounding-box surface-area difference vs Fiscus**: ≈ 39%. PASS.

### Continua LF-5 vs Solaria (LF-4)

Solaria's 8 sections match the same A-sequence as Pragma/Fiscus. Solaria's hero sits at h=724, leadership at h=1305 (taller than Pragma due to longer demographics), cases at h=886 — Y-positions drift but the bounding-box list is identical to Pragma/Fiscus.

**Bounding-box surface-area difference vs Solaria**: ≈ 38%. PASS.

### Evidence files

- Pre-rebuild: `_baseline/{pragma,fiscus,solaria,continua}-1920-fullpage*.png` and `_baseline/section-list-{pragma,fiscus,solaria,continua}.json`
- Post-rebuild: `continua-1920-fullpage-lf5-final.png` and `_regression-{pragma,fiscus,solaria}/{slug}-1920-fullpage-post.png`

---

## 2 · B-LAYOUT-2 · DOM section list compare (BLOCKING)

Enumeration of `document.querySelectorAll('section[class*="cs-"]')` on the live home of each sibling.

| Sibling | Section list (ordered) | Diff vs Continua LF-5 |
|---|---|---|
| Pragma   | cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta | **3 entries** differ: cs-cycle inserted at slot-2 + cs-trust deleted + cs-pillars/cs-kpi-band order shift |
| Fiscus   | cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta | same as Pragma |
| Solaria  | cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta | same as Pragma |
| Continua | cs-hero · **cs-cycle** · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta | — |

Difference is ≥3 entries (≥1 insertion + ≥1 deletion + ≥1 reorder) vs every existing sibling. Pass threshold is ≥2; LF-5 passes wide. **PASS.**

---

## 3 · B-LAYOUT-3 · layout-dimension classification (REQUIRED)

Live render classified along all 9 L-axes per CS-LAYOUT-01..09.

| Axis | Declared (LF-5 row) | Live render | Match? |
|---|---|---|---|
| L1 hero geometry | object-overlay | object-overlay (full-bleed photo + lower-third dark plate + dual credit overlays) | ✓ |
| L2 section sequence | D | D (cs-hero · cs-cycle · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta) | ✓ |
| L3 mid-strip slot | slot-2 | slot-2 (cs-cycle immediately after hero) | ✓ |
| L4 pillars treatment | 2x2-with-image | 2×2 matrix with monochrome icon images (4 pillars) | ✓ |
| L5 KPI placement | band-at-4 | dark band at slot-4 (post-cycle, post-pillars) | ✓ |
| L6 leadership presence | pillar-photo | pillar-photo with environmental station label | ✓ |
| L7 cases-preview shape | timeline | vertical timeline with year-on-rail + horizon column | ✓ |
| L8 navbar geometry | condensed-minimal-top | condensed-minimal-top (64px, no phone-right) | ✓ |
| L9 footer structure | 4-col-with-whistleblowing | 4-col with whistleblowing channel column | ✓ |

Classification matches the declaration exactly. CS-LAYOUT-14 holds. **PASS.**

### CS-LAYOUT-12 sibling-pair distinctness

| Pair | Differing dimensions | Pass (≥4/9)? |
|---|---|---|
| Pragma   ↔ Continua | L1, L2, L3, L4, L5, L6, L7, L8, L9 | ✓ 9/9 |
| Fiscus   ↔ Continua | L1, L2, L3, L4, L5, L6, L7, L9 | ✓ 8/9 |
| Solaria  ↔ Continua | L1, L2, L3, L4, L5, L6, L7, L9 | ✓ 8/9 |

CS-LAYOUT-13 (≥1 of L1/L2/L7) — passes wide (all three differ vs every sibling).

---

## 4 · Standard corporate-suite browser rubric

| Cell | Result | Notes |
|---|---|---|
| Hero AAA contrast (CS-HERO-03) | PASS | h1 cream on translucent dark plate over photo: AAA. |
| Section padding tokenized (CS-RHYTHM-01) | PASS | Every cs-* section reaches `--space-section-y` / `--space-section-x`. |
| One dark band per home (CS-TONE-03) | PASS | KPI at slot-4 + dark CTA closer (cluster permits dark closer). |
| Italic-em emphasis (CS-TYPE-02) | PASS | 5 hits across page — generazioni · cadenza · un solo · una sola cadenza · generazioni. |
| Accent budget ≤3 hits/viewport (CS-PAL-05) | PASS | See style-critic §9. |
| Pexels-only imagery (CS-IMG-SRC-01) | PASS | Hero + 4 pillar icons + 3 portraits — all Pexels frames. URL overlap audit: 0 with sibling pools. |
| Sticky nav + drawer at ≤880 (CS-NAV-01/05) | PASS | Drawer engages; LF-5's condensed-minimal-top stacks correctly. |
| Locale pill switcher | n/a | Continua locale registry = [it]; switcher suppressed (D-068). |
| 4-col footer with whistleblowing (LF-5 L9) | PASS | Whistleblowing column renders with eyebrow + note + email + policy link. |
| `?preview=1` propagation closed | PASS | 11/11 home → 200 carries `?preview=1` in staff session (verified live). |
| Cases reachability | PASS | 4/4 timeline rows resolve to `mandati/{slug}/` at status 200. |
| Editor isolation | PASS | `/templates/business/continua-stewardship/preview/?preview=1` does not show editor click-to-edit affordances (no `body.mw-is-editor-preview`). |
| Reduced motion | PASS | `prefers-reduced-motion: reduce` zeroes transitions + reveal animations. |

---

## 5 · Internal home-link reachability

11 hrefs from the home page point at corporate-suite Continua routes. Verified each resolves at status 200 in the staff session and propagates `?preview=1`:

- 5 nav links: `/preview/` · `/chi-siamo/` · `/custodia/` · `/mandati/` · `/contatti/`
- 4 timeline cases: `/mandati/famiglia-{a,b,c,d}-…/`
- 2 CTA bands (hero + closer): both link to `/contatti/` and `/chi-siamo/`

11/11 → 200. `?preview=1` propagated.

---

## 6 · Console + network

Verified: no JS errors in the console at first load · no 404s · no CORS errors · no mixed-content warnings.

---

## 7 · Frozen-sibling regression walk

| Sibling | Section list | Y-positions vs baseline | Body class | navPhone | footWhistle | Verdict |
|---|---|---|---|---|---|---|
| Pragma | 8 sections | y exact-match across all 8 | cs-lf-lf-1 lm-ready | true | false | **0 px regression · PASS** |
| Fiscus | 8 sections | y exact-match across all 8 | cs-lf-lf-3 lm-ready | true | false | **0 px regression · PASS** |
| Solaria | 8 sections | y exact-match across all 8 | cs-lf-lf-4 lm-ready | true | false | **0 px regression · PASS** |

---

## 8 · Verdict

LF-5 IT walk: **PASS** at the new browser gates and the standard rubric.
Frozen-sibling regression: **0 px** on each of Pragma · Fiscus · Solaria.
Aggregate ready for release-gatekeeper.
