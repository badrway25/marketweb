# Continua LF-5 IT rebuild · browser-verification log

**Status**: GREEN · all browser gates PASS · 0 fixes mid-walk on the LF-5 render itself · 1 source-file fix mid-walk (multi-line comment → `{% comment %}` block)
**Date**: 2026-04-29
**Engine**: Playwright MCP (Chromium · headless)
**Server**: `python manage.py runserver 127.0.0.1:8042 --noreload`
**Session**: staff superuser `cs_review_fix` (preview gate `?preview=1`)

This log mirrors the corporate-suite browser rubric (`factory/standards/corporate-suite-browser-rubric.md`) plus the three new layout-family gates (B-LAYOUT-1/2/3) introduced in `factory/reports/hardening/corporate-suite-layout-variance-rules.md §5`.

---

## 1 · Pre-rebuild baseline captures (1920×1080)

| Sibling | Section list (live render) | Total y-extent | Body class |
|---|---|---|---|
| Pragma   | cs-hero(122,686) · cs-pillars(808,712) · cs-kpi-band(1520,254) · cs-sectors(1774,163) · cs-trust(1936,366) · cs-leadership(2302,850) · cs-cases-preview(3152,747) · cs-cta(3898,412) | 4310 | (no family class · pre-X.4b) |
| Fiscus   | cs-hero(122,751) · cs-pillars(874,691) · cs-kpi-band(1564,254) · cs-sectors(1818,163) · cs-trust(1980,366) · cs-leadership(2346,942) · cs-cases-preview(3288,798) · cs-cta(4086,492) | 4578 | same |
| Solaria  | cs-hero(122,724) · cs-pillars(846,660) · cs-kpi-band(1506,254) · cs-sectors(1759,213) · cs-trust(1972,366) · cs-leadership(2338,1305) · cs-cases-preview(3642,886) · cs-cta(4528,440) | 4968 | same |
| Continua | cs-hero(116,751) · cs-pillars(867,736) · cs-kpi-band(1604,254) · cs-cycle(1857,733) · cs-sectors(2590,213) · cs-trust(2802,366) · cs-leadership(3168,1139) · cs-cases-preview(4307,962) · cs-cta(5269,468) | 5737 | same · cycle at slot-4 (LF-3 shape) |

PNGs filed at `factory/reports/scorecard/continua-pass2-lf5/_baseline/{slug}-1920-fullpage.png` (Continua pre-rebuild as `*-pre-rebuild.png`). Section-list JSONs filed at `_baseline/section-list-{slug}.json`. Diagnostic at `_baseline/baseline-summary.md`.

---

## 2 · Continua LF-5 walk (post-rebuild)

### 2.1 · 1920 desktop reference

`continua-1920-fullpage-lf5-final.png`

Section bounding boxes:

```
cs-hero          (0, 156, 1905, 720)
cs-cycle         (253, 876, 1400, 733)
cs-pillars       (253, 1608, 1400, 933)
cs-kpi-band      (0, 2542, 1905, 254)
cs-sectors       (0, 2795, 1905, 164)
cs-leadership    (253, 2959, 1400, 1370)
cs-cases-preview (253, 4330, 1400, 1020)
cs-cta           (0, 5350, 1905, 468)
```

Body class: `cs-lf-lf-5 lm-ready`. Nav class: `cs-nav cs-nav--lf5`. Phone-right block suppressed.

### 2.2 · Responsive matrix

| Breakpoint | Capture | Notes |
|---|---|---|
| 1440 | `continua-1440-fullpage-lf5.png` | Hero/cycle/pillars 2×2/timeline preserved at 1440 |
| 1100 | `continua-1100-fullpage-lf5.png` | Frame stacks · pillars matrix collapses to 1-col · timeline rail collapses · whistleblowing column wraps |
| 720  | `continua-720-fullpage-lf5.png`  | Hero photo 4:5 above primary-bg frame · KPI 2x2 · drawer engaged · whistleblowing column reachable |
| 480  | `continua-480-fullpage-lf5.png`  | Single-column everywhere · CS-RESPONSIVE-03 hero h1 ≥32px floor holds · CS-CTA-01 touch target ≥44px |

### 2.3 · B-LAYOUT-1 wireframe overlay (BLOCKING)

Bounding-box surface-area difference vs each frozen sibling:

- vs Pragma  · ≈ 41% diff · PASS (≥30%)
- vs Fiscus  · ≈ 39% diff · PASS
- vs Solaria · ≈ 38% diff · PASS

### 2.4 · B-LAYOUT-2 DOM section-list (BLOCKING)

Continua LF-5 list: `cs-hero · cs-cycle · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta` (8 sections).

vs every frozen sibling list (`cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta`):
- 1 insertion (cs-cycle at slot-2)
- 1 deletion (cs-trust)
- 1+ reorderings (cs-pillars · cs-kpi-band · cs-leadership shift slots)

≥3 entries differ. Threshold ≥2. **PASS.**

### 2.5 · B-LAYOUT-3 layout classification (REQUIRED)

Live render classified along all 9 L-axes:

```
L1 hero geometry  · object-overlay
L2 section seq    · D
L3 mid-strip slot · slot-2
L4 pillars        · 2x2-with-image
L5 KPI placement  · band-at-4
L6 leadership     · pillar-photo
L7 cases shape    · timeline
L8 navbar         · condensed-minimal-top
L9 footer         · 4-col-with-whistleblowing
```

Matches LF-5 declaration on all 9 axes (CS-LAYOUT-14 holds).
CS-LAYOUT-12 ≥4/9 — passes wide.
CS-LAYOUT-13 (L1+L2+L7) — all three differ vs every sibling.

### 2.6 · Standard rubric

| Cell | Result | Probe |
|---|---|---|
| Hero AAA contrast | PASS | h1 cream `#eef0f3` on translucent dark plate — 8.6:1 worst-case |
| Section rhythm tokens | PASS | LF-5 styles use `var(--space-section-y/x)` per CS-RHYTHM-01 |
| Italic-em emphasis | PASS | 5 hits (generazioni · cadenza · un solo · una sola cadenza · generazioni) |
| One dark band per home | PASS | KPI slot-4 + CTA closer (closer permitted) |
| Pexels-only · 0 URL overlap | PASS | Hero + 4 icons + 3 portraits all Pexels |
| Drawer at ≤880 | PASS | CS-NAV-05 drawer engages; LF-5 condensed-minimal stacks correctly |
| Cases reachability | PASS | 4/4 timeline → 200 |
| Internal home links | PASS | 11/11 → 200 with `?preview=1` propagated |
| Editor isolation | PASS | `body.mw-is-editor-preview` not set on `/preview/` |
| Reduced motion | PASS | `prefers-reduced-motion: reduce` zeros transitions |
| Tab order + focus | PASS | brass `:focus-visible` on every interactive |
| Whistleblowing reach | PASS | sectors-band eyebrow + footer column + legal-row link · all breakpoints |

---

## 3 · Frozen-sibling regression walk

| Sibling | Section bounding boxes | Body class | Nav phone | Footer whistle col | Verdict |
|---|---|---|---|---|---|
| Pragma  | exact match to baseline (8 sections, 8/8 y-positions identical) | cs-lf-lf-1 lm-ready | true | false | **0 px regression · PASS** |
| Fiscus  | exact match (8 sections, 8/8 y-positions identical) | cs-lf-lf-3 lm-ready | true | false | **0 px regression · PASS** |
| Solaria | exact match (8 sections, 8/8 y-positions identical) | cs-lf-lf-4 lm-ready | true | false | **0 px regression · PASS** |

Captures: `_regression-{pragma,fiscus,solaria}/{slug}-1920-fullpage-post.png`.

---

## 4 · Issue + fix mid-walk

**Issue**: After the rebuild's first run, Pragma's `cs-hero` had shifted from y=122 (baseline) to y=174 (post). Fiscus and Solaria showed similar shifts.

**Diagnosis**: Multi-line `{# … #}` Django comment in `_layouts/lf1/content.html` was being rendered as a plain text node (Django's `{# … #}` is single-line only). Same defect in `_layouts/lf1/styles.html`, `_layouts/lf5/{styles,content}.html`, and the new `home.html` router.

**Fix**: Replaced every multi-line `{# … #}` with `{% comment %}…{% endcomment %}`. After server restart (with stale PID cleanup), the regression walk returned 0 px drift on all three frozen siblings.

**Time cost**: ~5 min (diagnose + fix + restart + re-walk).

---

## 5 · Console + network

- Console: 0 errors at first paint (login page warning ignored — login is the entry).
- Network: no 404s on home or any page; Pexels image URLs all resolve at 200.
- Mixed-content: clean (HTTPS Pexels URLs · HTTP localhost server).

---

## 6 · URL/port left open

- Server: `http://127.0.0.1:8042/`
- Continua LF-5 IT walk URL: `http://127.0.0.1:8042/templates/business/continua-stewardship/preview/?preview=1`
- Pragma  regression: `http://127.0.0.1:8042/templates/business/pragma-corporate-suite/preview/?preview=1`
- Fiscus  regression: `http://127.0.0.1:8042/templates/business/fiscus-commercialista/preview/?preview=1`
- Solaria regression: `http://127.0.0.1:8042/templates/business/solaria-coaching/preview/?preview=1`

Single listener on PID 58128 at the close of the walk.

---

## 7 · Aggregate browser verdict

**GREEN · approve at LF-5 for human visual review.** All 3 layout-family gates plus the standard corporate-suite rubric pass. Frozen-sibling regression is 0 px on each of Pragma · Fiscus · Solaria. No blocking issues; one STRONG observation (photo lower-third luminance plate must hold on future hero swaps) and two GUIDELINE observations (pillar-icon photographer cohesion · environmental-portrait literal-room match).
