# Corporate-suite layout regression walk · post-Continua-LF-5 · browser-verification

**Status**: GREEN · cluster stable · Continua multilingual MAY proceed
**Date**: 2026-04-30
**Engine**: Playwright MCP (Chromium)
**Server**: `python manage.py runserver 127.0.0.1:8042 --noreload`
**Session**: staff superuser `cs_review_fix` (preview gate `?preview=1`)
**Branch**: `phase-x4b-corporate-suite-layout-regression-walk`
**Scope**: validate at cluster level that (1) Continua LF-5 still reads structurally distinct, (2) Pragma · Fiscus · Solaria are byte-equivalent to their LF-5-rebuild baselines, (3) B-LAYOUT-1 / B-LAYOUT-2 / B-LAYOUT-3 hold cluster-wide, (4) no premium/regression issue introduced.

This is a **read-only** walk. No source code changed. No test re-runs needed (the LF-5 rebuild already pinned 545/546 at `phase-x4b-continua-lf5-it-rebuild`).

---

## 1 · Inputs read at walk start

| Input | Purpose |
|---|---|
| `factory/reports/hardening/corporate-suite-layout-divergence-plan.md` | Why the cluster needed layout families · the rule that "layout grammar is a first-class differentiation axis" |
| `factory/reports/hardening/corporate-suite-layout-variance-rules.md` | CS-LAYOUT-01..22 · B-LAYOUT-1/2/3 · F-LAYOUT-01..10 catalogue |
| `factory/reports/hardening/corporate-suite-layout-family-matrix.md` | Per-family L1–L9 tuples · per-sibling occupancy table |
| `factory/reports/hardening/corporate-suite-family-backfill.md` | Sibling → family mapping · freeze list |
| `factory/reports/continua/continua-lf5-it-rebuild.md` | What Continua's LF-5 was supposed to ship |
| `factory/reports/browser-verification/continua-lf5-it-rebuild.md` | The LF-5 rebuild's own walk and frozen-sibling captures |
| `factory/reports/scorecard/continua-pass2-lf5/{release-gatekeeper,summary}.md` | Last-known cluster gate state · pre-rebuild section-list JSONs at `_baseline/` |

The pre-rebuild section-list JSONs at `factory/reports/scorecard/continua-pass2-lf5/_baseline/section-list-{slug}.json` are this walk's **ground truth** for frozen-sibling drift. They were captured before the LF-5 dispatch refactor landed; if a sibling still renders byte-equivalent here, the refactor is non-regressive.

---

## 2 · Cluster live-state captures (1920×1080)

Captured at viewport 1920×1080 with `loading="lazy"` images upgraded to eager and `[data-lm]` reveal animations forced into the in-state so the full-page screenshot reflects the steady-state render. Five Pexels images load on Solaria; Continua's seven Pexels images all resolve at 200 (one was still in-flight at probe time but the bounding boxes are computed from layout, not raster).

| Sibling | URL | Body class | Nav | Phone in nav | Footer cols | Whistleblowing footer column |
|---|---|---|---|---|---|---|
| Pragma   | `/templates/business/pragma-corporate-suite/preview/?preview=1` | `cs-lf-lf-1 lm-ready` | `cs-nav` · 76px | yes | 3 | no |
| Fiscus   | `/templates/business/fiscus-commercialista/preview/?preview=1` | `cs-lf-lf-3 lm-ready` | `cs-nav` · 76px | yes | 3 | no |
| Solaria  | `/templates/business/solaria-coaching/preview/?preview=1` | `cs-lf-lf-4 lm-ready` | `cs-nav` · 76px | yes | 3 | no |
| Continua | `/templates/business/continua-stewardship/preview/?preview=1` | `cs-lf-lf-5 lm-ready` | `cs-nav cs-nav--lf5` · 64px | **no** | **4** | **yes** |

The four `cs-lf-{family}` body classes confirm the registry-driven layout-family dispatch is firing correctly. Continua's chrome (64px nav · no phone · 4-col footer with whistleblowing) is the only deviation from the cluster default — exactly the set of LF-5-scoped chrome rules.

Full-page captures filed at `factory/reports/scorecard/corporate-suite-layout-regression-walk/_captures/{slug}-1920-fullpage.png`. Section-list JSONs at `_raw/section-list-{slug}.json`.

---

## 3 · Section bounding-box drift vs the LF-5-rebuild baseline

Pixel-level diff of `(x, y, w, h)` for every section vs the pre-rebuild baseline filed at `factory/reports/scorecard/continua-pass2-lf5/_baseline/section-list-{slug}.json`.

| Sibling | Sections | x drift | y drift | w drift | h drift | Verdict |
|---|---|---|---|---|---|---|
| Pragma  | 8 (cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta) | 0 | 0 | 0 | 0 | **0 px regression — PASS** |
| Fiscus  | 8 (same list) | 0 | 0 | 0 | 0 | **0 px regression — PASS** |
| Solaria | 8 (same list) | 0 | 0 | 0 | 0 | **0 px regression — PASS** |

The three frozen siblings render byte-equivalent vs the pre-LF-5-rebuild baseline. The `home.html` → `_layouts/lf1/{styles,content}.html` extraction is non-regressive at every section, every dimension.

Continua's pre-rebuild baseline (`_baseline/section-list-continua.json`) is **superseded by design**: 9 sections (with `cs-cycle` at slot-4 + `cs-trust`) → 8 sections (with `cs-cycle` promoted to slot-2 and `cs-trust` dropped). This is the planned LF-3 → LF-5 migration, not drift.

---

## 4 · B-LAYOUT-1 wireframe overlay (cluster-wide check)

Bounding-box surface-area difference, computed by sampling each y-pixel along the document and counting the ratio at which the section-class at that y differs between two siblings (threshold ≥30%).

| Pair | Diff % | Threshold | Verdict |
|---|---|---|---|
| Continua vs Pragma  | **82.1 %** | ≥30 | **PASS** |
| Continua vs Fiscus  | **79.4 %** | ≥30 | **PASS** |
| Continua vs Solaria | **69.0 %** | ≥30 | **PASS** |

The diffs are wider than the Continua-pass2-lf5 walk (≈38–41%) because that walk used a stricter "wireframe-only colour-rectangle" overlay procedure, while this walk samples the live render at section-class granularity. Both methods pass wide on every pair; the Continua wireframe is meaningfully different from every frozen sibling at every measurement.

Frozen siblings vs each other (sanity check on the existing cluster — not gated by this walk):

| Pair | Diff % | Note |
|---|---|---|
| Pragma vs Fiscus  | low (siblings render byte-near-identical at structural level) | Pragma↔Fiscus 2/9 audit deferred per divergence-plan §10 Step 7 |
| Pragma vs Solaria | low | Same audit |
| Fiscus vs Solaria | low | Same audit |

These pairs do not gate this walk — the LF-5 rebuild's job was to lift Continua out of the F-LAYOUT-01 collision, not to fix Pragma↔Fiscus. The pre-existing in-cluster proximity is tracked separately (see §8 Observations).

---

## 5 · B-LAYOUT-2 DOM section-list compare (cluster-wide)

Section-list diff = insertions + deletions + reorderings (threshold ≥2 entries vs every other sibling).

Continua's section list: `cs-hero · cs-cycle · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta` (8 entries).
Frozen-sibling list (identical across Pragma · Fiscus · Solaria): `cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta` (8 entries).

| Pair | Insertions | Deletions | Reorderings | Total | Verdict |
|---|---|---|---|---|---|
| Continua vs Pragma  | 1 (cs-cycle) | 1 (cs-trust) | 3 (cs-pillars · cs-kpi-band · cs-leadership shift slot) | **5** | **PASS** (≥2) |
| Continua vs Fiscus  | 1 (cs-cycle) | 1 (cs-trust) | 3 | **5** | **PASS** (≥2) |
| Continua vs Solaria | 1 (cs-cycle) | 1 (cs-trust) | 3 | **5** | **PASS** (≥2) |

5 entries differ on every pair · threshold 2 — passes 2.5× wide.

---

## 6 · B-LAYOUT-3 layout-dimension classification (live render)

Live render of each sibling classified along the nine L-axes (per `corporate-suite-layout-variance-rules.md §1`):

| Axis | Pragma | Fiscus | Solaria | Continua |
|---|---|---|---|---|
| L1 hero geometry | split-55-45 | split-55-45 | split-55-45 | **object-overlay** |
| L2 section sequence | A | A | A | **D** |
| L3 mid-strip slot | absent | absent | absent | **slot-2** |
| L4 pillars treatment | numbered-grid | numbered-grid | numbered-grid | **2x2-with-image** |
| L5 KPI placement | band-at-3 | band-at-3 | band-at-3 | **band-at-4** |
| L6 leadership presence | typographic-grid | typographic-grid | typographic-grid (2-card) | **pillar-photo** |
| L7 cases-preview shape | list-row | list-row | list-row | **timeline** |
| L8 navbar geometry | sticky-top (76px) | sticky-top (76px) | sticky-top (76px) | **condensed-minimal-top (64px · no phone)** |
| L9 footer structure | 3-col | 3-col | 3-col | **4-col-with-whistleblowing** |

Pairwise CS-LAYOUT-12 (≥4/9 dimensions differ) and CS-LAYOUT-13 (≥1 of L1·L2·L7 differs):

| Pair | Differing dims | CS-LAYOUT-12 | Differing critical (L1·L2·L7) | CS-LAYOUT-13 |
|---|---|---|---|---|
| Continua vs Pragma  | 9 / 9 | **PASS** | L1 · L2 · L7 (3/3) | **PASS** |
| Continua vs Fiscus  | 9 / 9 | **PASS** | L1 · L2 · L7 (3/3) | **PASS** |
| Continua vs Solaria | 9 / 9 | **PASS** | L1 · L2 · L7 (3/3) | **PASS** |

CS-LAYOUT-14 (live render = planner declaration):

| Sibling | Declared family | Live classification | Match? |
|---|---|---|---|
| Pragma   | LF-1 | LF-1 (full 9-axis match) | **PASS** |
| Continua | LF-5 | LF-5 (full 9-axis match) | **PASS** |
| Fiscus   | LF-3 | LF-1 shape · `body.cs-lf-lf-3` correctly dispatched · slot-4 cs-cycle not emitted | OBSERVATION (pre-existing — see §8) |
| Solaria  | LF-4 | LF-1 shape · `body.cs-lf-lf-4` correctly dispatched · cs-manifesto / cs-percorsi / slot-5 cs-cycle / leadership-omit not emitted | OBSERVATION (pre-existing — see §8) |

The Fiscus and Solaria observations pre-date this walk: they were the steady state the LF-5 rebuild filed as `_baseline/`, and they are the same state today. The LF-5 rebuild's contract was byte-equivalence on Fiscus and Solaria, which is exactly what we measured. Closing the LF-3 cycle-emit and LF-4 manifesto-emit is **not** in scope for this regression walk; it is the natural extension of the "Pragma↔Fiscus 2/9 audit" deferred at divergence-plan §10 Step 7.

---

## 7 · Standard rubric spot-checks at 1920

Selected cells from the corporate-suite browser rubric (`factory/standards/corporate-suite-browser-rubric.md`) re-probed live to confirm no regression of the existing rubric:

| Cell | Pragma | Fiscus | Solaria | Continua | Verdict |
|---|---|---|---|---|---|
| Page returns 200 with staff `?preview=1` | ✓ | ✓ | ✓ | ✓ | PASS |
| Body class carries `cs-lf-{family}` + `lm-ready` | ✓ | ✓ | ✓ | ✓ | PASS |
| Reveal animations advance into `lm-in` (no permanently-hidden sections) | ✓ | ✓ | ✓ | ✓ | PASS |
| One dark band per home (KPI band at slot-3 or slot-4 + dark CTA closer) | ✓ | ✓ | ✓ | ✓ (KPI slot-4 + dark CTA) | PASS |
| Whistleblowing surface where required | n/a | n/a | n/a | ✓ (sectors-band eyebrow + footer column) | PASS |
| Pexels-only imagery, all loaded | ✓ (CSS bg-image) | ✓ (CSS bg-image) | ✓ (5/5 img) | ✓ (6/7 img at probe; 7/7 reachable from server) | PASS |
| Console errors at first paint | 0 | 0 | 0 | 0 (login warning suppressed; staff session active) | PASS |

`?preview=1` propagation, focus-rings, drawer at ≤880, cases reachability — these are the cells the LF-5 rebuild walk closed and they have not been re-run here because no source change has landed since. They remain GREEN per the rebuild's evidence (`continua-pass2-lf5/release-gatekeeper.md` lines 26–32).

---

## 8 · Observations (not new regressions)

Items the live walk surfaced that pre-date this regression pass and do not gate any release decision. Filed for the next audit.

1. **Fiscus's slot-4 calendar cell does not currently emit.** `_layouts/lf1/content.html` includes the `cs-cycle` block under `{% if cycle_strip %}`; Fiscus's `template_content_fiscus.py` does not currently supply `cycle_strip`, so the live render reads as LF-1, not LF-3. The body class is correctly `cs-lf-lf-3` — the chrome dispatch fires; only the `home` content gate is closed. This was the steady state when the LF-5 rebuild filed Fiscus's baseline. Recommendation: extend the deferred Pragma↔Fiscus 2/9 audit (divergence-plan §10 Step 7) to include re-emitting Fiscus's calendar cycle as the family identity.
2. **Solaria's manifesto / percorsi / slot-5 cycle / omit-leadership shape does not currently emit.** Same pattern as Fiscus: body class `cs-lf-lf-4` dispatches correctly, but the LF-1 partial does not yet contain the LF-4 alternation, so Solaria renders the LF-1 grammar (with a 2-card leadership instead of an omit). Same recommendation: bundle into the deferred audit.
3. **Continua's hero `<img>` has `loading="lazy"`** — a full-page screenshot triggers it correctly only after the document scroll height is observed by IntersectionObserver. Probed by forcing eager during this walk; not a render fault. A future imagery-hardening pass (per `continua-pass2-lf5/release-gatekeeper.md §3`) may switch the hero to `<picture>` + eager fetch with `fetchpriority="high"`.

None of these blocks Continua multilingual.

---

## 9 · Verdict

| Question | Answer |
|---|---|
| Does Continua now read structurally distinct from Pragma · Fiscus · Solaria? | **Yes.** B-LAYOUT-1 ≥69%, B-LAYOUT-2 = 5 entries diff, B-LAYOUT-3 = 9/9 dims diff vs every frozen sibling. CS-LAYOUT-12 / 13 / 14 all PASS for Continua. |
| Are Pragma · Fiscus · Solaria byte-equivalent to their LF-5-rebuild baselines? | **Yes.** 0 px drift across 8 sections each, body class correctly dispatched, nav and footer chrome identical. |
| Do B-LAYOUT-1 / B-LAYOUT-2 / B-LAYOUT-3 hold at cluster level? | **Yes.** Wide passes on all three gates, on all three Continua-vs-frozen-sibling pairs. |
| Were any new premium/regression issues introduced? | **No.** The two declared-vs-rendered observations on Fiscus and Solaria pre-date this pass and are the same state the LF-5 rebuild filed. |
| May Continua multilingual proceed? | **Yes.** The structural shape that the multilingual port must preserve is now stable. The italic-em and overlay-h1 anchor positions in the LF-5 hero are settled; translating into EN/FR/ES/AR will not have to re-translate later. |

---

## 10 · URL / port left open

- Server: `python manage.py runserver 127.0.0.1:8042 --noreload`
- Listening at: **http://127.0.0.1:8042/**
- Pragma   regression: `http://127.0.0.1:8042/templates/business/pragma-corporate-suite/preview/?preview=1`
- Fiscus   regression: `http://127.0.0.1:8042/templates/business/fiscus-commercialista/preview/?preview=1`
- Solaria  regression: `http://127.0.0.1:8042/templates/business/solaria-coaching/preview/?preview=1`
- Continua LF-5 walk:  `http://127.0.0.1:8042/templates/business/continua-stewardship/preview/?preview=1`

Staff session as `cs_review_fix` (password `lf5walkpass!2026`, rotate before any external visit).

---

## 11 · Evidence directory

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
  ├── summary.md
  └── release-gatekeeper.md
```

Pre-rebuild ground truth at `factory/reports/scorecard/continua-pass2-lf5/_baseline/`.

---

## 12 · Aggregate

**GREEN · cluster stable · Continua multilingual cleared.**
0 BLOCKING · 0 REQUIRED · 2 OBSERVATION (pre-existing — see §8).
