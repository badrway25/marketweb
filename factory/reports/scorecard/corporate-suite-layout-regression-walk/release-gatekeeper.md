# Corporate-suite layout regression walk · release-gatekeeper

**Verdict**: GREEN · cluster stable · Continua multilingual cleared
**Date**: 2026-04-30
**Branch**: `phase-x4b-corporate-suite-layout-regression-walk`
**Aggregate**: 0 BLOCKING · 0 REQUIRED · 0 STRONG · 2 OBSERVATION (pre-existing)
**Tier preserved**: Continua = `draft` · Pragma/Fiscus/Solaria = `published_live`

---

## 1 · Gates

| Gate | Result | Notes |
|---|---|---|
| Cluster freeze since 2026-04-29 | ✓ | Branch tip `26d8537`. No source change in this pass. Only one untracked file at start: this report's directory. |
| Server up + 4 previews reachable | ✓ | `127.0.0.1:8042` · staff session `cs_review_fix` · 4/4 previews 200 (Continua via `?preview=1`) |
| Frozen-sibling Pragma · 0 px drift vs LF-5-baseline | ✓ | 8 sections · 0 dx/dy/dw/dh on every section · `cs-lf-lf-1 lm-ready` body class · 76px nav with phone · 3-col footer |
| Frozen-sibling Fiscus · 0 px drift vs LF-5-baseline | ✓ | 8 sections · 0 dx/dy/dw/dh · `cs-lf-lf-3 lm-ready` body class · 76px nav with phone · 3-col footer |
| Frozen-sibling Solaria · 0 px drift vs LF-5-baseline | ✓ | 8 sections · 0 dx/dy/dw/dh · `cs-lf-lf-4 lm-ready` body class · 76px nav with phone · 3-col footer |
| Continua live render = LF-5 declaration | ✓ | 9/9 axes match (object-overlay · D · slot-2 · 2x2-with-image · band-at-4 · pillar-photo · timeline · condensed-minimal-top · 4-col-with-whistleblowing) · `cs-lf-lf-5 lm-ready` body class · `cs-nav cs-nav--lf5` (64px no phone) · 4-col footer with whistleblowing |
| B-LAYOUT-1 wireframe overlay | ✓ | 82.1% / 79.4% / 69.0% surface-area diff vs Pragma / Fiscus / Solaria (threshold ≥30%) |
| B-LAYOUT-2 DOM section-list compare | ✓ | 5-entry diff (1 ins + 1 del + 3 reorderings) vs each peer (threshold ≥2) |
| B-LAYOUT-3 layout-dim classification | ✓ | Continua 9/9 dim diff vs every peer · CS-LAYOUT-12 (≥4) and CS-LAYOUT-13 (≥1 of L1·L2·L7 · all 3 differ) PASS wide |
| CS-LAYOUT-14 live = declared | ✓ for Pragma · Continua | OBSERVATION on Fiscus + Solaria — pre-existing, see §3 |
| Standard rubric spot-checks (200 status, body class, lm-in advancement, dark-band economy, whistleblowing, Pexels-only) | ✓ | All cluster invariants hold; no new STRONG flag |
| Console errors at first paint | ✓ | 0 errors on each sibling. Login warning suppressed in staff session. |
| `?preview=1` propagation closed at `phase_x4_corporate_suite_case_parent_fix` | ✓ | Inherited unchanged. Verified by reachability. |
| Pexels imagery reachable from server | ✓ | `curl -m5 https://images.pexels.com/...` returns 200 in <1s. Two image-load timing observations covered in §3. |
| Test suite | n/a | No source change made — the LF-5 rebuild's 545/546 (1 pre-existing pre-X.4b failure) is still the project-wide baseline |

---

## 2 · Cluster gate-by-gate scoring

| Gate | Score (out of 5) | Reason |
|---|---|---|
| Frozen-sibling regression | 5.0 | 0 px drift across all 24 sections (3 siblings × 8 sections) |
| Continua structural distinctness | 5.0 | 9/9 dim diff vs every peer; wireframe surface diff 69–82% |
| Cluster gate compliance (B-LAYOUT-1/2/3) | 5.0 | All three gates PASS wide on every Continua-vs-peer pair |
| Live-vs-declaration (CS-LAYOUT-14) | 4.5 | Pragma + Continua match; Fiscus + Solaria carry pre-existing observation that does not block this walk |
| Chrome dispatch correctness (body class · nav · footer) | 5.0 | Every sibling carries the right `cs-lf-{family}` body class; LF-5 chrome modifiers fire only on Continua |
| Tier preservation | 5.0 | No tier change introduced; Continua stays `draft` |
| Evidence completeness | 5.0 | Section-list JSONs + full-page captures + this walk + summary + verification log all filed |
| **Aggregate** | **4.93 / 5** | |

≥ 4.50 threshold satisfied. 0 BLOCKING. 0 STRONG. 2 OBSERVATION (pre-existing).

---

## 3 · Observations (pre-existing — not gated by this walk)

These are documented for the next audit. Each predates this regression walk and was the steady state when the LF-5 rebuild filed its baseline.

1. **Fiscus's slot-4 cs-cycle (calendar cadence) does not emit live.** `_layouts/lf1/content.html:{cs-cycle gate}` renders only when `cycle_strip` is supplied; Fiscus's `template_content_fiscus.py` does not supply it. Live render = LF-1 sequence. Body class is correctly `cs-lf-lf-3`. **Recommendation**: bundle the LF-3 emit fix into the deferred Pragma↔Fiscus 2/9 audit (`corporate-suite-layout-divergence-plan.md §10 Step 7`).
2. **Solaria's LF-4 alternation (cs-manifesto · cs-percorsi · slot-5 cs-cycle · omit-leadership) does not emit live.** Same pattern: body class `cs-lf-lf-4` dispatches correctly, but the LF-1 partial does not contain the LF-4 alternation, so Solaria renders the LF-1 grammar with a 2-card leadership instead of an omit. **Recommendation**: same deferred audit.
3. **Hero `<img>` carries `loading="lazy"`** in some siblings, which means a fullPage screenshot has to upgrade to eager + force `[data-lm]` reveal before the steady-state render is captured. Probed and worked around in this walk; not a render fault. Future imagery hardening pass may switch to `<picture>` + `fetchpriority="high"` + `srcset`.

None of the three blocks Continua multilingual or any release decision.

---

## 4 · Acceptance criteria

| Criterion | Met |
|---|---|
| Continua structurally distinct from Pragma · Fiscus · Solaria | ✓ |
| Pragma · Fiscus · Solaria render byte-equivalent to LF-5-rebuild baseline | ✓ |
| B-LAYOUT-1 / B-LAYOUT-2 / B-LAYOUT-3 PASS at cluster level | ✓ |
| No new STRONG / REQUIRED / BLOCKING issues | ✓ |
| Server URL/port left open and documented | ✓ |
| Evidence directory populated | ✓ |
| Tier states preserved | ✓ |
| Multilingual gate addressed (PROCEED authorized) | ✓ |

---

## 5 · Decision

**APPROVE — open Continua multilingual workflow C.**

Continue to hold (unchanged from `continua-pass2-lf5/release-gatekeeper.md §6`):

- Tier flip on Continua (`draft` preserved).
- Public-flip handshake (R-SOL-8 cluster gate).
- Pragma↔Fiscus 2/9 audit, with extension to cover the Fiscus LF-3 cycle-emit and Solaria LF-4 manifesto-emit gaps.
- 5th-sibling LF-2 build.
- Hero `<picture>` + `srcset` imagery hardening pass.

---

## 6 · Next action

> Open the **Continua multilingual port (workflow C)** session. Read `factory/reports/continua/continua-lf5-it-rebuild.md §11` for the IT-anchor + italic-em map, port to EN/FR/ES/AR + AR RTL per the Solaria Pass B precedent, and walk 5 locales × 7 cells against the standard corporate-suite browser rubric. Tier stays `draft` until public-flip authorization. The LF-5 IT shape is locked; the multilingual port operates against that shape and does not need to re-run B-LAYOUT-1/2/3 — those gates are structural and the structure is settled.
