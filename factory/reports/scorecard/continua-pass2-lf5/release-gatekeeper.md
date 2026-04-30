# Continua Pass 2 · LF-5 IT rebuild — release-gatekeeper

**Verdict**: GREEN · approved for human visual review at LF-5 · `tier=draft` preserved · public-flip held
**Date**: 2026-04-29
**Branch**: `phase-x4b-continua-lf5-it-rebuild`
**Aggregate**: 4.78 / 5

---

## 1 · Gates

| Gate | Result | Notes |
|---|---|---|
| Cluster freeze pre-rebuild | ✓ | Pragma · Fiscus · Solaria source files clean off `phase-x4b-corporate-suite-family-backfill` tip; only the two empty placeholder reports were untracked at session start |
| Pre-rebuild baseline captured | ✓ | `_baseline/{slug}-1920-fullpage*.png` + `section-list-{slug}.json` for all 4 siblings |
| Registry surface added | ✓ | `WebTemplate.layout_family` field + migration `0006_webtemplate_layout_family.py`. Backfill: Pragma=LF-1 · Fiscus=LF-3 · Solaria=LF-4 · Continua=LF-5 |
| Layout dispatch refactored | ✓ | `home.html` is now a router; `_layouts/lf1/{styles,content}.html` for Pragma/Fiscus/Solaria; `_layouts/lf5/{styles,content}.html` for Continua |
| Chrome branched | ✓ | `cs-nav--lf5` modifier (64px no phone) + 4th footer column branches to whistleblowing on LF-5 only |
| Continua page_data updated for LF-5 | ✓ | `pillars_matrix` (2×2 with icons) · `cases_timeline` (4 rows) · `whistleblowing` (sectors-band eyebrow) · `whistleblowing_footer` (4-col footer column) · leadership `station` field · cycle `Calendario`→`Ciclo di governance` |
| Imagery surfaces | ✓ | Hero (Pass 1 · object-led library photo) + 4 pillar icons (Pexels object glyphs) + 3 environmental portraits (Pass 1 · re-curated). All Pexels-only. Zero URL overlap with sibling pools |
| B-LAYOUT-1 wireframe overlay | ✓ | ≥38% bounding-box surface-area difference vs each frozen sibling (threshold ≥30%) |
| B-LAYOUT-2 DOM section list compare | ✓ | ≥3-entry difference vs each frozen sibling (threshold ≥2) |
| B-LAYOUT-3 layout classification | ✓ | Live render = LF-5 declaration on all 9 axes. CS-LAYOUT-12 ≥4/9 holds wide on every pair. CS-LAYOUT-13 L1+L2+L7 differ vs every pair |
| Standard corporate-suite browser rubric | ✓ | Style-critic, contrast, responsive 1920/1440/1100/720/480, hreflang, focus rings, reduced-motion, cases reachability, editor isolation — all GREEN |
| Frozen-sibling regression walk | ✓ | 0 px wireframe drift on Pragma · Fiscus · Solaria. Body classes correct. Nav phone preserved. Footer column 4 still offices |
| Cases-link reachability | ✓ | 4/4 timeline rows → `mandati/{slug}/` at status 200 |
| Internal home-link propagation | ✓ | 11/11 hrefs from home → 200 with `?preview=1` propagated in staff session |
| Test suite | ✓ | 545/546 pass. 33/33 corporate-suite contracts pass. The 1 failure (`FreshSeedChainBackfill.test_medical_and_restaurant_templates_have_booking_flag`) is pre-existing on the pre-X.4b tip |
| Tier preserved | ✓ | `continua-stewardship` stays at `tier=draft`. No `sync_template_tiers` invocation |
| Locale registry preserved | ✓ | Continua locales = `[it]`. Multilingual switcher suppressed |
| Whistleblowing column reachable on mobile | ✓ | `_layouts/lf5/styles.html` + `_base.html` ≤880/720 stack preserves the column with email + policy link |
| `?preview=1` propagation | ✓ | Closed in `phase_x4_corporate_suite_case_parent_fix`; LF-5 inherits unchanged. Staff 11/11 home → 200 verified |

---

## 2 · Layout-family-matrix update (CS-LAYOUT-22 evidence)

After this pass, `corporate-suite-layout-family-matrix.md §2` should read:

```
| Continua (stewardship) | LF-3 | … | 2026-04-29 | superseded — migration to LF-5 landed 2026-04-29 |
| Continua (stewardship) | LF-5 | object-overlay | D | slot-2 | 2x2-with-image | band-at-4 | pillar-photo | timeline | condensed-minimal-top | 4-col-with-whistleblowing | 2026-04-29 | active |
```

Open territory remains LF-2 (5th sibling) + LF-6 (reserved 6th–7th).

---

## 3 · Risks acknowledged

- **Pragma↔Fiscus 2/9 layout-distinctness** — out of scope for this pass per `corporate-suite-layout-divergence-plan.md §10 Step 7`. Tracked for a later audit.
- **Pillar-icon photographer cohesion** — 4 Pexels frames from 4 different photographers, flattened by grayscale filter. Acceptable; future imagery scout pass may swap to a tighter source.
- **Environmental portrait literal-room match** — current portraits are studio editorial; the `station` text builds the room-anchor rhetorically. Acceptable for IT-only pass.
- **Photo lower-third luminance variance** — the dark-plate gradient is the active legibility fallback. Future hero swaps must preserve the plate or pre-grade the photo. Documented in `_layouts/lf5/styles.html` `.cs-hero .frame { background: linear-gradient … }`.
- **Picture/srcset not introduced** — the LF-5 hero loads as a CSS `background-image` URL. A future imagery hardening pass should add `<picture>` + `srcset` + WebP/AVIF for reduced-data accessibility. Not blocking.

---

## 4 · Acceptance summary (from `continua-lf5-migration-brief.md §9`)

| Criterion | Met |
|---|---|
| Pragma · Fiscus · Solaria render byte-equivalent at 0 px wireframe drift | ✓ |
| Continua passes B-LAYOUT-1 (≥30% surface diff vs each sibling) | ✓ |
| Continua passes B-LAYOUT-2 (section-list diff ≥2 vs each sibling) | ✓ |
| Continua passes B-LAYOUT-3 (live = declaration · ≥4/9 dim diff · no L1–L9 collision) | ✓ |
| Continua passes standard corporate-suite browser rubric at IT | ✓ |
| Scorecard directory `factory/reports/scorecard/continua-pass2-lf5/` populated with build-report · style-critic · browser-verifier · responsive-auditor · contrast-accessibility · scorecard · summary + wireframe pair captures + regression evidence | ✓ |
| Test suite green at the project-wide baseline | ✓ (545/546; the 1 failure is pre-existing) |
| `MEMORY.md` checkpoint pending | ⚠ to be added in the SUMMARY |
| Continua tier stays `draft`, locales stay `[it]`, multilingual gate held | ✓ |

---

## 5 · Aggregate scoring

| Dimension | Score (out of 5) | Reason |
|---|---|---|
| Layout-family compliance | 5.0 | LF-5 declaration matched on all 9 axes |
| Hero geometry novelty | 5.0 | First object-overlay hero in cluster |
| Section-rhythm distinctness vs siblings | 5.0 | 8/9 to 9/9 dimension diff vs every frozen sibling |
| Italic-em + accent budget | 5.0 | Cluster invariants held |
| Contrast + accessibility | 4.8 | AAA on h1 + KPI; one accent-on-cream eyebrow at AA Large per cluster pattern |
| Responsive matrix | 4.8 | All 5 breakpoints render; whistleblowing column reachable on every breakpoint |
| Frozen-sibling regression | 5.0 | 0 px on all three |
| Imagery cohesion | 4.5 | Pillar icons from 4 photographers (grayscale-flattened); portraits literal-room is rhetorical |
| Tooling + tests | 4.7 | 545/546 pass; the 1 failure pre-existing |
| **Aggregate** | **4.78 / 5** | |

≥ 4.50 threshold satisfied. 0 BLOCKING. ≤3 STRONG (1 STRONG · 3 GUIDELINE/observation).

---

## 6 · Decision

**APPROVE LF-5 IT pass for human visual review.**

Continue to hold:

- Tier flip (`tier=draft` preserved).
- Multilingual rollout (5 locales × ~7 cells deferred to a future workflow C pass).
- Public-flip handshake gate per R-SOL-8 (applies cluster-wide).
- Pragma↔Fiscus 2/9 audit (deferred per divergence-plan §10 Step 7).
