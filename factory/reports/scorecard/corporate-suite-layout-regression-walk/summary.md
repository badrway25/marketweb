# Corporate-suite layout regression walk · summary

**Status**: GREEN · cluster stable · Continua multilingual MAY proceed
**Date**: 2026-04-30
**Branch**: `phase-x4b-corporate-suite-layout-regression-walk`
**Aggregate**: 0 BLOCKING · 0 REQUIRED · 0 STRONG · 2 OBSERVATION (pre-existing)
**Ground truth**: `factory/reports/scorecard/continua-pass2-lf5/_baseline/section-list-{slug}.json`

---

## Why this pass exists

Continua migrated LF-3 → LF-5 on 2026-04-29 (Pass 2 LF-5 IT rebuild). That migration touched the corporate-suite shell — `home.html` became a router, `_layouts/lf1/{styles,content}.html` and `_layouts/lf5/{styles,content}.html` were introduced, and `_base.html` learned three layout-family-scoped chrome rules. The cluster is held still until a confirmation walk says nothing leaked into Pragma, Fiscus, or Solaria.

This walk is that confirmation. It runs no source change. It re-classifies all four siblings live, re-runs the three layout-family gates (B-LAYOUT-1 / B-LAYOUT-2 / B-LAYOUT-3) at cluster level, and pixel-diffs the frozen-sibling renders against the pre-rebuild baseline.

---

## What was walked

| Sibling | URL | Family |
|---|---|---|
| Pragma   | `http://127.0.0.1:8042/templates/business/pragma-corporate-suite/preview/?preview=1` | LF-1 |
| Fiscus   | `http://127.0.0.1:8042/templates/business/fiscus-commercialista/preview/?preview=1` | LF-3 |
| Solaria  | `http://127.0.0.1:8042/templates/business/solaria-coaching/preview/?preview=1` | LF-4 |
| Continua | `http://127.0.0.1:8042/templates/business/continua-stewardship/preview/?preview=1` | LF-5 |

All four reachable in the staff superuser session at `cs_review_fix`. Anonymous Continua returns 404 by design (tier=draft + preview gate).

---

## Frozen-sibling regression verdict

| Sibling | Sections | x drift | y drift | w drift | h drift | Body class | Verdict |
|---|---|---|---|---|---|---|---|
| Pragma  | 8 | 0 | 0 | 0 | 0 | `cs-lf-lf-1 lm-ready` | **0 px regression** |
| Fiscus  | 8 | 0 | 0 | 0 | 0 | `cs-lf-lf-3 lm-ready` | **0 px regression** |
| Solaria | 8 | 0 | 0 | 0 | 0 | `cs-lf-lf-4 lm-ready` | **0 px regression** |

Compared against the pre-LF-5-rebuild baseline at `continua-pass2-lf5/_baseline/section-list-{slug}.json`. Every section's `(x, y, w, h)` matches byte-for-byte.

Nav chrome: 76 px sticky-top with phone-right preserved on all three.
Footer: 3-col preserved on all three. No whistleblowing column on any frozen sibling.

---

## Continua LF-5 distinctness verdict (cluster gates)

### B-LAYOUT-1 wireframe overlay surface-area difference

| Pair | Diff % | Threshold | Verdict |
|---|---|---|---|
| Continua vs Pragma  | 82.1 % | ≥30 % | **PASS** |
| Continua vs Fiscus  | 79.4 % | ≥30 % | **PASS** |
| Continua vs Solaria | 69.0 % | ≥30 % | **PASS** |

### B-LAYOUT-2 DOM section-list diff

Continua list: `cs-hero · cs-cycle · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta` (8).
Frozen list (identical across Pragma/Fiscus/Solaria): `cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta` (8).

| Pair | Insertions | Deletions | Reorderings | Total | Verdict (≥2) |
|---|---|---|---|---|---|
| Continua vs Pragma  | 1 (cs-cycle) | 1 (cs-trust) | 3 | **5** | **PASS** |
| Continua vs Fiscus  | 1 | 1 | 3 | **5** | **PASS** |
| Continua vs Solaria | 1 | 1 | 3 | **5** | **PASS** |

### B-LAYOUT-3 layout-dimension classification

| Pair | Differing dims (of 9) | CS-LAYOUT-12 (≥4) | Differing in {L1·L2·L7} | CS-LAYOUT-13 (≥1) |
|---|---|---|---|---|
| Continua vs Pragma  | 9 / 9 | **PASS** | 3 / 3 | **PASS** |
| Continua vs Fiscus  | 9 / 9 | **PASS** | 3 / 3 | **PASS** |
| Continua vs Solaria | 9 / 9 | **PASS** | 3 / 3 | **PASS** |

CS-LAYOUT-14 (live = declaration) for Continua: PASS on all 9 axes (object-overlay · D · slot-2 · 2x2-with-image · band-at-4 · pillar-photo · timeline · condensed-minimal-top · 4-col-with-whistleblowing).

---

## Cluster-wide verdict

| Question | Answer |
|---|---|
| Continua reads structurally distinct from frozen siblings? | **Yes** — 9/9 layout dimensions differ vs each peer; B-LAYOUT-1 ≥69%; B-LAYOUT-2 = 5 entries diff |
| Frozen siblings byte-equivalent to LF-5-rebuild baseline? | **Yes** — 0 px drift on every section, every dimension, every sibling |
| B-LAYOUT-1 / B-LAYOUT-2 / B-LAYOUT-3 hold at cluster level? | **Yes** — wide pass on every gate × every pair |
| New premium/regression issues introduced? | **No** — two declared-vs-rendered observations on Fiscus and Solaria pre-date this pass |
| May Continua multilingual begin? | **Yes** — the LF-5 IT shape is stable; translating now will not have to be redone |

---

## Observations (pre-existing — not gated by this walk)

1. **Fiscus does not currently emit its slot-4 cs-cycle calendar cell.** Live section list is the LF-1 sequence; only the body class signals LF-3. The `_layouts/lf1/content.html` partial gates `cs-cycle` on `{% if cycle_strip %}` and Fiscus's `template_content_fiscus.py` does not currently supply that key. This was the state when the LF-5 rebuild filed Fiscus's baseline; it is not new in this walk. Tracked for the divergence-plan §10 Step 7 audit (originally framed as "Pragma↔Fiscus 2/9").
2. **Solaria does not currently emit its LF-4 cs-manifesto / cs-percorsi / slot-5 cs-cycle / omit-leadership shape.** Same pattern: body class `cs-lf-lf-4` dispatches correctly, but the LF-1 partial does not yet contain the LF-4 alternation, so the live render is the LF-1 grammar. Same baseline state as 2026-04-29; same audit recommendation.

Both observations are evidence that the LF-3 and LF-4 alternations of the LF-1 partial were never built — only LF-1 and LF-5 partials exist today. The LF-5 rebuild hand-off was explicit that it "shipped the minimum architecture" (`continua-pass2-lf5/summary.md` line 12), and that minimum did not include filling in LF-3 and LF-4 emit rules. The next pass that wants to close this can do so under the deferred audit.

---

## What was held back / out of scope

- Tier flip on Continua (`tier=draft` preserved).
- Multilingual rollout (this walk only certifies that it MAY proceed).
- Public-flip handshake (R-SOL-8 cluster gate held).
- Pragma↔Fiscus 2/9 audit.
- LF-3 cycle-emit and LF-4 manifesto-emit closure (extensions to the deferred audit).
- Test re-run (the LF-5 rebuild's 545/546 is still the project-wide baseline · this walk made no source change).

---

## URL / port left open

```
python manage.py runserver 127.0.0.1:8042 --noreload
```

Listening at `http://127.0.0.1:8042/`.

Staff session as `cs_review_fix` (password `lf5walkpass!2026`, rotate before any external visit).

---

## Evidence directory

```
factory/reports/scorecard/corporate-suite-layout-regression-walk/
  ├── _captures/
  │     ├── pragma-1920-fullpage.png
  │     ├── fiscus-1920-fullpage.png
  │     ├── solaria-1920-fullpage.png
  │     └── continua-1920-fullpage.png
  ├── _raw/
  │     ├── section-list-pragma.json
  │     ├── section-list-fiscus.json
  │     ├── section-list-solaria.json
  │     └── section-list-continua.json
  ├── summary.md             (this file)
  └── release-gatekeeper.md  (verdict)
```

Plus the long-form verification log at `factory/reports/browser-verification/corporate-suite-layout-regression-walk.md`.

---

## Decision

**APPROVE — cluster is stable. Open Continua multilingual workflow C.**
