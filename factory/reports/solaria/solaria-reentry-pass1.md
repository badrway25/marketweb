# Solaria · Controlled re-entry · Pass 1 narrative

**Phase**: X.4 Wave 2 Pilot #2 · Solaria — Business Coaching
**Branch**: `phase-x4-solaria-controlled-reentry-pass1` (forked from the post-GO tip `075e623` of `phase-x4a-corporate-factory-hardening-followup`)
**Run-ISO**: `20260426T0907Z`
**User authorization**: explicit un-pause of paused Solaria Commit B per the binding R-SOL-8 lever; this report records the FIRST controlled pass under that authorization.
**Reviewer**: Claude (Opus 4.7)
**Hardened-archetype baseline at re-entry**: `075e623` (Step 2E P1E final Go reassessment) — corporate-suite archetype was promoted to GO under plan §10.3 with `avg 4.9 / 5 · all 9 CRITICAL ≥ 4 · 0 / 18 blocking · 0 / 18 required outstanding`.
**Solaria source state pre-pass-1**: paused two-commit Wave 2 Pilot #2 trail on `phase-x4-wave2-solaria-coaching-v1`:
- `e8f38b5` · Commit A: solaria-coaching draft (IT-only, ~935 LOC content tree, original cream-as-primary palette `#F7F3EC`)
- `6b70d56` · Commit B (palette polarity fix only): swap to dark-foreground convention `#2B2A28 / #C8621A / #8B5A2B` after live walk diagnosed cream-on-cream rendering
- The Solaria branch was NOT rebased into the hardening-followup branch during the X.4a cycle (R-SOL-2 binding throughout).

---

## 1 · Why pass 1 is "controlled" and what it deliberately is NOT

The user's authorization message specifies "controlled re-entry pass 1 — resume Solaria only under the corporate-suite GO rules." Three explicit constraints distinguish it from "continue Commit B blindly":

1. **Pass 1 is IT-only**, by binding D-102 cadence. The original Commit A was IT-only with EN/FR/ES/AR explicitly deferred to Commit B. The R-SOL-14 5-locale rubric is a closure floor for **Solaria-overall**, not for the first pass. Pass 2 will land the 4 deferred locale trees; pass 3 will close on the full rubric matrix + AP8 pipeline scorecard.
2. **Pass 1 stays at `tier=draft`**. Flipping to `published_live` cascades 6 public-count tests (`21 → 22`) and surfaces Solaria in `/templates/` listing, the homepage trust counters, and discovery facets. Those side-effects belong to a deliberate go-live decision, not the first pass. Browser walks reach the live route via the staff `?preview=1` query-string (D-055 pattern).
3. **No archetype-level skin edit**. The hardened corporate-suite skin (`templates/live_templates/business/corporate-suite/_base.html` + 6 page templates) is exercised AS-IS. Any defect would have to be archetype-grade — a contract regression that would also break Pragma + Fiscus. Zero such regressions surfaced.

---

## 2 · Reconciliation: archetype-inherited (free) vs Solaria-local (must implement)

### 2.1 · Archetype-inherited (zero pass-1 work required)

These contracts were already in force on the hardened branch and Solaria simply receives them by enrolment:

- **CS-PAL-01 build-time palette gate** (`corporate_suite.E001`) — runs on every `manage.py check`, fails CI if any enrolled corporate-suite primary fails the cream-paper polarity check. Solaria's `#2B2A28` passes (luminance 0.024, contrast vs cream 12.56 AAA).
- **CS-IMG-SRC-01 / CS-IMG-POOL-01 build-time imagery gate** (`corporate_suite.E002 / E003`) — Solaria's `business-coaching` pool ships 6 Pexels URLs in canonical `[hero, feature, portrait, portrait, detail, ambient]` shape, so both checks are silent. Solaria is **NOT** in `LEGACY_EXEMPT_KEYS`; only Pragma `business-corporate` is grandfathered (`corporate_suite.W001` warning surfaces on Pragma alone, exactly per the GO-reassessment-bound contract).
- **CS-BLOCK-17 (extended) palette safety on dark surfaces** — the four chrome surfaces (`mp-bar a.mp-bar-back · .mp-lang.is-current · .cs-nav .wm .crest · .cs-post .kpi-band .stat .num`) are already promoted from `var(--accent)` → `var(--on-dark)` at archetype level. Solaria inherits cream-on-primary (`#EEF0F3` on `#2B2A28` = 12.56 AAA) on every dark surface.
- **mp-back `:focus-visible` whitelist** — landed in P1C; carried unchanged.
- **CS-CTA-04 footer real-route wiring** — 8 / 8 Solaria footer anchors verified non-`#`.
- **AP12 reduced-motion JS contract** — `live-motion.js matchMedia` branch + `_base.html @media (prefers-reduced-motion: reduce)` block; Solaria's 5 IT pages walked clean under emulation.
- **Hamburger drawer at ≤ 880 px + `html { overflow-x: clip }` root guard** — verified at 768 + 390 mobile cells.
- **D-054 three-template-ready triangulation** — Pragma + Fiscus docstrings already triangulate against Solaria-as-placeholder (P1D refresh). Solaria's own docstring at `e8f38b5` already encodes the reciprocal vs Pragma + vs Fiscus 10-gate triangulations, so R-SOL-11 is satisfied **by construction** with zero pass-1 docstring edits.
- **Static-test set** (CorporateSuite\*Tests families) — every red-path the hardening cycle hardened (palette, imagery, footer, theme, build-time) carries unchanged.

### 2.2 · Solaria-local (the minimum pass-1 delta · 7 files touched)

Every change below is required for Solaria to be discoverable, renderable, and gate-passing on the hardened branch. Each is the smallest possible delta that achieves that.

| # | File | Change | Why required |
|---|---|---|---|
| 1 | `apps/catalog/template_content_solaria.py` | **NEW · 949 LOC IT content tree** | Restored from `e8f38b5` Commit A. Solaria's 5 pages × all `page_data` keys the corporate-suite skin templates expect. Already encodes reciprocal D-054 vs Pragma + vs Fiscus 10-gate triangulations in the docstring (R-SOL-11 satisfied by construction). Voice anchor verbatim. Anti-pattern guardrails listed. |
| 2 | `apps/catalog/template_content.py` | Import `SOLARIA_CONTENT_IT` + register `"solaria-coaching": {"it": SOLARIA_CONTENT_IT}` in `TEMPLATE_CONTENT` | The `LiveTemplateView` renders only templates registered here. Without this dict entry Solaria's preview routes 404 even with `?preview=1`. |
| 3 | `apps/catalog/preview_imagery.py` | Add `business-coaching` 6-URL Pexels pool (slot-shape `[hero, feature, portrait, portrait, detail, ambient]`) | The skin reads `IMAGERY_CONFIG[<imagery_key>]` to produce `page_data.hero_image`. Without this entry the hero photo would be empty. Pool is Pexels-only (build-time gate enforces). |
| 4 | `apps/catalog/template_dna.py` | Add `solaria-coaching` DNA entry on `corporate-suite` archetype with `imagery_key="business-coaching"` + `font_pairing=("Fraunces","Inter")` + `tone="professional-warm"` + `conversion_pattern="discovery-call-booking"` | The DNA registry resolves archetype + imagery + tone for the live preview. Without this entry the corporate-suite skin can't be selected for Solaria. |
| 5 | `apps/catalog/management/commands/seed_templates.py` | Add `solaria-coaching` to `TEMPLATE_METADATA` (cluster `coaching` · style `minimal-light` · price-tier `standard` · feature flags) AND to `SEED_TEMPLATES` (palette `#2B2A28 / #C8621A / #8B5A2B` — POST-FIX from `6b70d56`, NOT the cream `#F7F3EC` from `e8f38b5`) | Seeds Solaria into the DB on `manage.py seed_templates`. Palette must be the polarity-fixed dark-warm-carbon set; the cream variant would fire `corporate_suite.E001` and stop CI. |
| 6 | `apps/catalog/tests.py` | Add `solaria-coaching` to `booking_slugs` set in `test_medical_and_restaurant_templates_have_booking_flag` | Solaria has `has_booking=True` (discovery-call CTA). Without the test-set update the count would be 11 vs the actual 12 and the test would fail. |
| 7 | `TEMPLATE_REGISTRY.json` | Add `solaria-coaching` entry with `tier="draft"` + `live_pages = [home, il-coach, percorsi, casi, contatti]` + post-fix palette + extensive `tier_reason` documenting the pass-1 → pass-2 → pass-3 closure path | `sync_template_tiers` (invoked at the end of `seed_templates`) reads from this file to set `WebTemplate.tier`. Without it Solaria seeds at the model default tier (draft), but registry consistency tests would surface the mismatch. |

**Lines of code change (excluding the new 949-LOC content file)**: ~120 LOC additions across 6 files. No deletions. No edits to `apps/editor`, `apps/projects`, `apps/commerce`, `apps/catalog/models.py`, `apps/catalog/views.py`, `apps/catalog/urls.py`, `apps/catalog/migrations`, or any skin-folder template (B3 + B7 + B-no-new-archetype constraints honored).

---

## 3 · R-SOL rule reconciliation

| Rule | Pass-1 status |
|---|---|
| **R-SOL-1** No Solaria-scope planner activity during P1 (binding **before** GO) | n/a · GO already issued, this is the post-GO un-pause work |
| **R-SOL-2** No Solaria branch rebasing | Honored — no rebase from `phase-x4-wave2-solaria-coaching-v1` into the hardening branch. The Solaria content tree was **re-introduced via fresh additions on the controlled-reentry branch**, not via merge/cherry-pick. |
| **R-SOL-3** No Solaria content-file edits during P1 | n/a · post-GO. Pass 1 explicitly authors the IT content tree. |
| **R-SOL-4** No Solaria palette / imagery / schema edits during P1 | n/a · post-GO. Pass 1 authors them with build-time gates as the safety rail. |
| **R-SOL-5** Constraint B3 (no `apps/editor`/`apps/projects`/`apps/commerce` edits) | **Honored · 0 LOC touched in those packages.** |
| **R-SOL-6** Constraint B4 (no new archetypes) | **Honored · Solaria enrolls on the existing `corporate-suite` archetype.** |
| **R-SOL-7** Distinct dev-server port for parallel walks | **Honored · `:8731`** (Pragma + Fiscus prior corpora used `:8730`). |
| **R-SOL-8** User un-pause = separate explicit instruction | **Issued in this session's user message. Acknowledged.** |
| **R-SOL-9** Solaria enters the SAME 10-agent AP8 pipeline that passed on Fiscus | Pass 1 exercises the `template-builder` + `browser-verifier` legs end-to-end. The full 10-agent fan-out (style-critic / contrast-accessibility / responsive / release-gatekeeper / etc.) is captured in the `factory/reports/scorecard/solaria-pass1/` packet. |
| **R-SOL-10** First Solaria scorecard cites `O7` Pragma legacy grandfather | **Cited in `release-gatekeeper.md §3.1` and `scorecard.md §6 · E1`.** |
| **R-SOL-11** Solaria refreshes own D-054 triangulation | **Already encoded in `template_content_solaria.py` docstring at `e8f38b5`** (10-gate vs Fiscus + 10-gate vs Pragma). Pragma + Fiscus side already triangulates against Solaria-as-placeholder per P1D refresh. **Three-template-ready by construction.** |
| **R-SOL-12** Solaria palette passes `corporate_suite.E001` | **PASS · `#2B2A28` luminance 0.024 · contrast vs cream 12.56 AAA.** Build transcript at `factory/reports/browser-verification/solaria-pass1/20260426T0907Z/check-clean.log` (only `W001` Pragma grandfather warning; zero errors). |
| **R-SOL-13** Solaria imagery is Pexels-only (NOT grandfathered) | **PASS · 6 / 6 Pexels URLs in canonical pool shape.** Built-time `corporate_suite.E002 / E003` silent. |
| **R-SOL-14** Full rubric matrix (5 locales × 6 pages × 4 viewports = 120+ PNGs in single ISO) | **DEFERRED to pass 2 + pass 3** by binding D-102 cadence. Pass-1 ships 7 cells (5 IT pages × 1 desktop + 1 mobile + 1 tablet sample). § deviation 1 in `browser-verifier.md` documents the cap. |
| **R-SOL-15** Failures loop via template-editor-fixer → re-walk | n/a · zero failures in pass 1 required a fix loop. The motion-capture mechanism switch (default-motion → reduced-motion emulation) is a capture-mechanism choice already documented as `§ deviation 3` in the GO reassessment, not a defect. |

---

## 4 · Tests + builds before / after

|  | Before (tip 075e623) | After (tip TBD on this branch) |
|---|---|---|
| `manage.py check` | 0 errors · 1 warning (W001 Pragma grandfather) | 0 errors · 1 warning (same W001 only) |
| `manage.py test apps.catalog` | 171 / 171 OK · ~3.0 s | **171 / 171 OK · 2.438 s** |
| `manage.py test apps` (full suite) | 546 / 546 OK · ~189 s | not re-run in pass 1 (catalog suite covers Solaria's surface) |
| Catalog distribution | 21 published_live / 0 draft | **21 published_live / 1 draft** (Solaria) |
| Public-count cascade tests (5 of them) | 21 each | 21 each (unchanged · Solaria stays draft) |

---

## 5 · What pass 1 ships and what it does NOT ship

### Ships
- Solaria enrolled in DB at `tier=draft` with the polarity-fixed dark-warm palette
- Full IT content tree (5 pages · ~935 LOC) renderable via staff `?preview=1`
- Pexels-only `business-coaching` imagery pool registered and resolving
- DNA + seed metadata + registry entry with extensive `tier_reason` documenting pass-1 → pass-2 → pass-3 path
- Build-time gate transcripts (CI-clean palette + CI-clean imagery + 171 / 171 tests)
- Live browser-walk evidence (7 cells across 3 viewports, IT only) with reduced-motion emulation
- AP8 scorecard packet at `factory/reports/scorecard/solaria-pass1/` (8 deliverables per R-SOL-9)
- This narrative report + a browser-verification report

### Does NOT ship
- 4 additional locale trees (EN / FR / ES / AR) — pass 2
- Tier flip to `published_live` — pass 3
- Preview PNG regeneration from `business-coaching` pool — pass 2 / 3 chore
- `smoke_full.py` expansion (+ Solaria LOCALES + CATEGORY + POST_ROUTES) — pass 3
- 6 public-count test cascade (21 → 22) — pass 3 (gated on `published_live` flip)
- Multi-locale BRWS-FEEL-05 voice anchor verification — pass 2 + pass 3
- AR-RTL walk — pass 2 + pass 3
- 8-viewport sweep at every locale — pass 3
- Reciprocal D-054 docstring triangulation refresh against the **post-hardening** Pragma + Fiscus columns — already three-template-ready by construction (the `e8f38b5` docstring stands), but pass 3 may add a pointer to the post-GO baseline as housekeeping.

---

## 6 · Files changed in pass 1

```
M  TEMPLATE_REGISTRY.json                                   ( + ~25 lines, Solaria entry · tier=draft · post-fix palette)
M  apps/catalog/management/commands/seed_templates.py       ( + ~75 lines, TEMPLATE_METADATA + SEED_TEMPLATES rows)
M  apps/catalog/preview_imagery.py                          ( + ~20 lines, business-coaching 6-URL Pexels pool)
M  apps/catalog/template_content.py                         ( + ~10 lines, SOLARIA_CONTENT_IT import + dict entry)
M  apps/catalog/template_dna.py                             ( + ~65 lines, solaria-coaching DNA on corporate-suite)
M  apps/catalog/tests.py                                    ( + 2 lines, solaria-coaching in booking_slugs)
A  apps/catalog/template_content_solaria.py                 (NEW · 949 lines · IT content tree from e8f38b5 Commit A)
A  factory/reports/browser-verification/solaria-pass1/20260426T0907Z/  (browser walk evidence: 7 PNGs · check-clean.log · test-run.txt)
A  factory/reports/browser-verification/solaria-pass1.md    (this session's browser-verifier report)
A  factory/reports/scorecard/solaria-pass1/                 (8 AP8 scorecard deliverables)
A  factory/reports/solaria/solaria-reentry-pass1.md         (this narrative)
```

Every code change is reviewable. Every change has a stated reason in §2.2 above. No off-scope refactors. No `apps/editor` / `apps/projects` / `apps/commerce` touches. No new archetype.

---

## 7 · Pass-1 verdict

**PASS · ready for review.**

The hardened corporate-suite archetype absorbs Solaria as the third enrolled template without an archetype-level skin edit, without a build-time gate failure, without a test regression, without a console error, and without a Solaria-specific browser defect. The CS-BLOCK-17 (extended) chrome contracts that protect Pragma + Fiscus protect Solaria automatically. The R-SOL-12 / R-SOL-13 build-time gates accept Solaria's palette + imagery on the first attempt. The R-SOL-11 docstring triangulation is three-template-ready by construction.

Pass-1 closes the **first** of the planned three-pass Solaria re-entry path. The next two passes are user-authorized increments, not automated continuations.
