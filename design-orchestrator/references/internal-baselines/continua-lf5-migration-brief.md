# Continua LF-5 migration brief

**Status**: build brief v1 · **Date**: 2026-04-29
**Target sibling**: Continua (stewardship, slug `continua`)
**Migration**: LF-3 (Compliance Calendar) → **LF-5 (Stewardship Object-Hero)**
**Scope of this pass**: IT-only rebuild · `tier=draft` preserved · multilingual deferred
**Branch this brief is written for**: a Step-3 rebuild branch off `phase-x4b-corporate-suite-family-backfill`

**Read first**:
- `factory/reports/hardening/corporate-suite-family-backfill.md`
- `design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md`
- `factory/reports/hardening/corporate-suite-layout-family-matrix.md` (LF-5 row in §1)
- `factory/reports/hardening/corporate-suite-layout-variance-rules.md` (CS-LAYOUT-* + B-LAYOUT-* + F-LAYOUT-*)

This brief is the implementation-ready hand-off. The rebuild session reads this and starts working.

---

## 1 · What this rebuild is and is not

### Is
- A structural rebuild of Continua's `home.html` render to the LF-5 family shape.
- An update to Continua's `template_content_continua.py` page_data to feed the new shape.
- A registry update so `WebTemplate` (or equivalent) carries `layout_family=LF-5` for Continua.
- A refactor of the shared `home.html` shell so it can dispatch by family without breaking Pragma · Fiscus · Solaria. Recommended split: `templates/live_templates/business/corporate-suite/_layouts/{lf1,lf3,lf4,lf5}/home.html` selected by `_base.html` (or by a `home.html` router) on the registry's `layout_family`.
- An IT-only browser walk against the standard corporate-suite rubric **plus** the three new layout gates B-LAYOUT-1 / B-LAYOUT-2 / B-LAYOUT-3.
- A regression walk on Pragma · Fiscus · Solaria for **0 px** wireframe drift.

### Is not
- A multilingual rollout. EN/FR/ES/AR + AR RTL are deferred. Continua stays IT-only at the end of this pass.
- A public-flip. `tier=draft` is preserved. No `sync_template_tiers` flip in this brief.
- A repeat of work covered by previous Continua passes. Cycle copy in IT, voice anchor, imagery pack, and meta-strip text are reused, not rewritten.
- A change to Pragma / Fiscus / Solaria visible behaviour. Their renders must come out byte-equivalent at the end of the refactor.
- An edit to any cluster invariant in CS-LAYOUT-20.

---

## 2 · Current state vs LF-5 target

| Surface | Continua today (LF-3) | Continua target (LF-5) | Implementation note |
|---|---|---|---|
| **L1 Hero** | 55/45 grid · serif h1 LEFT · photo RIGHT · `min-height: 620px` · meta-strip three flex items below | Object-overlay · full-bleed object photo (no people) · h1 OVERLAID lower-third · TWO credit-block overlays (top-left + top-right) · eyebrow + sub move into the credit overlay frame · no 55/45 split | New `_layouts/lf5/home.html`. Old grid replaced with `position: relative` photo container + absolute-positioned overlay zones. Photo = full-bleed `<picture>` with `srcset` for 1920/1440/1280/1024/768/640/414/390. h1 sits in a translucent dark plate (CSS gradient or `background: rgba(10,12,16,0.45)` blur 16px) to keep AAA contrast irrespective of photo luminance |
| **L2 Sequence** | A+slot4: `cs-hero · cs-pillars · cs-kpi-band · cs-cycle · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta` | D: `cs-hero · cs-cycle · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta` | Trust marquee dropped from LF-5 (sectors band absorbs the trust function). Cycle promoted to slot-2. Pillars demoted to slot-3. KPI demoted to slot-4. Adjust the `<section>` order in `_layouts/lf5/home.html` exactly to this list |
| **L3 Mid-strip slot** | `slot-4` `cs-cycle` named "Calendario" with (presidio · figura · orizzonte) | `slot-2` `cs-cycle` named "Ciclo di governance" with same (presidio · figura · orizzonte) tuple but reframed as governance cadence, not calendar | Cell shape + tuple keys preserved · only the slot moves and the eyebrow label changes. IT copy reusable · re-target eyebrow from "Calendario" to "Ciclo di governance" (or the page_data-defined IT label) |
| **L4 Pillars** | 3-up `auto-fit minmax(220px, 1fr)` numbered serif eyebrow | 2×2 matrix · 4 pillars: **Custodia** · **Governance** · **Successione** · **Compliance** · each with a small monochrome icon-image (60–80px) above the pillar title | New `cs-pillars` template variant. Grid: `grid-template-columns: repeat(2, 1fr); gap: 64px;`. Image position: top-left of each card, monochrome (mix-blend or `filter: grayscale`). Numbered serif eyebrow stays |
| **L5 KPI band** | Dark band at slot-3 with 3–4 stats | Dark band at slot-4 (post-cycle, post-pillars) with 3–4 stats | One dark band on home (CS-TONE-03 holds). Same stat-card shape; just the slot moves |
| **L6 Leadership** | Typographic 3-card row · role + name + 2-3 credentials · no portraits | `pillar-photo`: 3-card row with **environmental portraits** (partner-at-archive-vault · partner-at-desk · partner-at-boardroom-roundtable). Card carries portrait above name + role + credentials | Imagery pack expansion required — see §4. Card grid stays `repeat(3, 1fr)`; image ratio 4:5 portrait, 320–400px wide |
| **L7 Cases-preview** | List-row · numbered rows with thumb · title · category · year · arrow | **Timeline**: vertical list with year on the left rail · mandate title centre · horizon (orizzonte temporale) right · arrow link to detail. Visual rule on the left rail (1px primary line) connects rows | New `cs-cases-preview` variant. CSS: `display: grid; grid-template-columns: 80px 1fr 200px 40px; row-gap: 32px;` plus a left-rail `::before` pseudo. Year typography = serif large numerals |
| **L8 Navbar** | Sticky-top 76px · wordmark-L + 5-link inline + phone-R | **Condensed-minimal-top**: sticky-top primary-bg, 64px (was 76px) · tighter wordmark · 5-link inline · **no phone-right** · locale-pill stays · hamburger appears at ≤880px exactly as today | Edit `_base.html` nav block to branch on `layout_family`: LF-1/LF-3/LF-4 keep 76px + phone-right; LF-5 renders 64px + no phone-right. Primary-bg polarity (CS-BLOCK-16) holds |
| **L9 Footer** | 3-col: brand + sitemap + contact | **4-col-with-whistleblowing**: brand + sitemap + contact + **whistleblowing channel column** (D.lgs. 24/2023 surfaced as a first-class element with the channel URL/email/phone) | Edit `_base.html` footer block to branch on `layout_family`. The whistleblowing column lives as a `<div class="cs-foot-col cs-foot-col--whistleblowing">` with eyebrow, channel name, channel address, and a "Tutela del segnalante" line. CS-FOOT-02 legal-row at the bottom keeps the whistleblowing link as it does today |
| **Imagery** | Object-led pack from Pass 1 | Carries through unchanged for hero + cycle context, **expansion required** for L4 (4 pillar icons) and L6 (3 environmental portraits) | See §4 for the imagery shortfall list |
| **Voice anchor (IT)** | Current IT anchor (verbatim from Continua Pass 1.5) | Unchanged text · italic-`<em>` re-anchored on the overlaid h1 · re-validate the em word lands on a region of the photo with sufficient luminance for AAA contrast | If the photo's lower-third covers an unpredictable luminance region, mandate the dark plate behind h1 (see L1 implementation note) so contrast is photo-independent |
| **Locales** | IT only | IT only | No EN/FR/ES/AR work in this pass |
| **Tier** | `draft` | `draft` | No `sync_template_tiers` flip |
| **`?preview=1` propagation** | Working (closed in `phase_x4_corporate_suite_case_parent_fix`) | Working unchanged | Re-verify after refactor — staff session 11/11 home → 200 should still hold |

---

## 3 · Concrete file-level work plan

Numbered so the rebuild session can follow without re-deriving anything.

### Step A — Pre-flight (no code yet)
1. Confirm `git status` is clean off `phase-x4b-corporate-suite-family-backfill` — Pragma/Fiscus/Solaria untouched since 2026-04-29.
2. Capture **baseline wireframe** at 1920px for Pragma, Fiscus, Solaria, Continua-LF3. These are the regression-comparison artifacts.
3. Capture **baseline section-list** (`document.querySelectorAll('section[class*="cs-"]')`) for the same four siblings.
4. File baselines under `factory/reports/scorecard/continua-pass2-lf5/_baseline/`.

### Step B — Registry surface
1. Add `layout_family` to `WebTemplate` (or chosen registry path — `template_dna.py` field is the alternative). Recommended: both, with `WebTemplate.layout_family` as authoritative and `template_dna.py` reflecting it for cluster-pack lookups.
2. Migration: `0xxx_add_layout_family.py` — add nullable `CharField(max_length=8)` with a one-time data migration setting `LF-1` for Pragma, `LF-3` for Fiscus, `LF-4` for Solaria, `LF-5` for Continua. Idempotent.
3. Run the migration in dev. Confirm the four rows have the expected values.

### Step C — Layout dispatch refactor
1. Create `templates/live_templates/business/corporate-suite/_layouts/lf1/home.html` byte-equivalent to today's `home.html`.
2. Create `_layouts/lf3/home.html` (LF-1 with `cs-cycle` inserted at slot-4 — same DOM Fiscus already renders).
3. Create `_layouts/lf4/home.html` (the manifesto-first sequence Solaria already renders).
4. Edit the shared `home.html` to act as a router: `{% include "live_templates/business/corporate-suite/_layouts/" ~ template.layout_family|lower ~ "/home.html" %}` — or equivalent under the project's template-include conventions.
5. Run Pragma · Fiscus · Solaria locally. **Visual diff = 0 px.** If any pixel drifts, halt and triage before touching LF-5.

### Step D — `_base.html` family-aware chrome
1. Branch the nav block on `layout_family`:
   - `LF-1` / `LF-3` / `LF-4` → 76px sticky-top with phone-right (existing).
   - `LF-5` → 64px sticky-top, no phone-right, otherwise identical (locale pill, hamburger ≤880px, focus rings).
2. Branch the footer block on `layout_family`:
   - `LF-1` / `LF-3` / `LF-4` → 3-col (existing).
   - `LF-5` → 4-col with whistleblowing column.
3. Re-walk Pragma/Fiscus/Solaria. **Wireframe diff = 0 px.**

### Step E — LF-5 layout
1. Author `_layouts/lf5/home.html` with the section sequence D from §2.
2. Implement the object-overlay hero — full-bleed `<picture>`, two credit overlays, h1 in a dark plate at lower-third.
3. Implement `cs-cycle` at slot-2 — same `(eyebrow, figure, context)` tuple shape, eyebrow re-labeled.
4. Implement the 4-pillar 2×2 matrix at slot-3 with monochrome icon images.
5. Implement the dark KPI band at slot-4.
6. Implement the sectors band at slot-5 — surface whistleblowing eyebrow within the band content.
7. Implement `cs-leadership` at slot-6 with `pillar-photo` (3 environmental portraits).
8. Implement the timeline cases at slot-7 (year + mandate + horizon + arrow).
9. Implement the dark CTA closer at slot-8.
10. Wire RTL fallbacks even though IT is the only locale walked — the family must be RTL-ready for the deferred multilingual pass.

### Step F — Continua page_data
1. Update `apps/catalog/template_content_continua.py`:
   - Add `layout_family = 'LF-5'` to the dna/registry block as a documentation hint (authoritative value lives in `WebTemplate`).
   - Restructure `home.hero` to provide: `image`, `image_alt`, `credit_top_left` (eyebrow + figure + context), `credit_top_right`, `eyebrow`, `h1` (with `<em>` markup), `subhead`, `cta_primary`, `cta_secondary`.
   - Restructure `home.pillars` to a 4-pillar list with `icon_image`, `eyebrow`, `title`, `body`.
   - Move `home.cycle` to top-level `home.governance_cycle` (or rename `home.cycle` semantically — keep the tuple shape).
   - Restructure `home.cases` to provide `year`, `title`, `horizon`, `href` per row (the timeline columns).
   - Restructure `home.leadership` to provide `portrait_image`, `name`, `role`, `credentials` per card.
   - Add `home.whistleblowing` block: `channel_name`, `channel_url` or `channel_email`, `policy_link`, `note`.
2. Confirm IT copy is reused verbatim from Pass 1.5 for cycle, voice anchor, pillar titles, case mandates. New surfaces (4th pillar, whistleblowing, timeline horizons) are the only new IT copy required.

### Step G — Imagery
See §4 for the shortfall list.

### Step H — Walk
1. Run `python manage.py runserver` and load `/templates/continua/?preview=1` in a staff session.
2. Capture `_layout-1920-wireframe.png` (B-LAYOUT-1) and pair-compare against Pragma/Fiscus/Solaria baselines.
3. Capture the section-list (B-LAYOUT-2).
4. Classify L1–L9 (B-LAYOUT-3) and confirm match to LF-5 declaration.
5. Run the standard corporate-suite browser rubric (style-critic · contrast · responsive 1920/1440/1280/1100/880/720/480 · hreflang · focus-rings · reduced-motion · cases preview links 200).
6. File `factory/reports/scorecard/continua-pass2-lf5/{build-report,style-critic,browser-verifier,responsive-auditor,contrast-accessibility,scorecard,summary}.md`.

### Step I — Regression walk on Pragma · Fiscus · Solaria
1. Re-run the standard corporate-suite browser rubric on the three frozen siblings.
2. Confirm 0 px wireframe drift vs the Step A baselines.
3. Confirm all CS-* rules still pass.
4. File regression evidence under `factory/reports/scorecard/continua-pass2-lf5/_regression-{pragma,fiscus,solaria}/`.

### Step J — Hold
1. Tier stays `draft`. No public flip.
2. No multilingual.
3. Update `MEMORY.md` index with the LF-5 GREEN checkpoint.

---

## 4 · Imagery shortfall

Continua's existing imagery pack is object-led from Pass 1 and covers the hero photo + cycle context surfaces. **New surfaces in LF-5** that need imagery:

| Surface | Quantity | Subject | Treatment |
|---|---|---|---|
| Hero photo | 1 (likely already present) | Object-led — seal · codex · ledger · deed · vault interior · archive shelf · notary stamp | Full-bleed editorial · ≥2400px wide · ratio 16:9 or 21:9 · luminance pre-graded so the lower-third can host AAA-contrast h1 (or use the dark plate fallback) |
| Pillar icons | 4 | Custodia · Governance · Successione · Compliance — abstract or object glyphs · monochrome | 200–400px wide · transparent or cream background · `filter: grayscale(1) brightness(...)` to flatten variance |
| Leadership portraits | 3 | Partner-at-archive-vault · partner-at-desk-with-codex · partner-at-boardroom-roundtable | Editorial · ratio 4:5 · environmental (the room is half the subject) · Pexels-only · zero URL overlap with any existing corporate-suite sibling per CS-IMG-SRC-04 |

The pre-build session must confirm Pexels has the leadership portraits available. If not, the orchestrator decides between (a) deferring LF-5 leadership to typographic-grid as a temporary downgrade — which would break L6 declaration and force a re-classification — or (b) running an imagery scout pass before the rebuild starts. Recommended: (b). Imagery decisions are cheap pre-build, expensive mid-build.

---

## 5 · Visual regressions to avoid during the migration

Listed as antipatterns to guard against at build and walk time.

1. **Pragma/Fiscus/Solaria pixel drift.** Any wireframe difference between the pre-rebuild and post-rebuild capture for the three frozen siblings is a regression. Treat **0 px** as the contract.
2. **Empty-section debt re-introduced.** If Continua's leadership data does not match the `pillar-photo` shape, the renderer MUST NOT silently fall back to an empty card grid. The build must fail loudly until imagery is delivered.
3. **Two dark bands on home.** LF-5 places the band at slot-4. The cycle band at slot-2, the sectors band at slot-5, and the CTA closer at slot-8 must NOT also be dark. CS-TONE-03 is one band per home.
4. **Whistleblowing column vanishing on mobile.** ≤720px footer collapse must keep the whistleblowing channel surfaced — collapsing to a sub-link of "contact" is a CS-FOOT-02 fail.
5. **h1 contrast failure on the photo overlay.** If the photo's lower-third luminance varies, h1 AAA contrast (CS-HERO-03) is no longer guaranteed. The dark plate behind h1 must be present, OR the photo must be pre-graded.
6. **Italic-em landing on the wrong word.** The voice anchor's italic word must land on a region with sufficient contrast and must remain the same word that bound at IT-build time (CS-EXEC-01 / R7). Changing the em word silently is a multilingual blocker for the deferred pass.
7. **`?preview=1` propagation breaking.** The 11/11 home → 200 + 4/4 case-study posts staff-reachability that closed in `phase_x4_continua_pass1_5_review_lock` must still hold after refactor.
8. **Pillar count slipping.** LF-5 declares 4 pillars in 2×2 — not 3, not 5. Pillar-count drift = layout-family drift = B-LAYOUT-3 fail.
9. **Cycle reverting to slot-4.** If the layout dispatcher silently routes to LF-3 because of a registry miss, Continua renders Fiscus's shape with Continua's copy — exactly the problem the migration is fixing.
10. **Trust marquee resurrected.** LF-5's section sequence D drops the trust marquee. Builders may be tempted to keep it "for completeness" — that is exactly an A+slot4 leak into D.

---

## 6 · Browser checks that prove the migration

The walk artifact list. All must pass before the migration is filed GREEN.

### New layout gates (BLOCKING)
| Gate | What it asserts | Evidence file |
|---|---|---|
| **B-LAYOUT-1** | Continua wireframe ≥30% bounding-box-area different from each of Pragma · Fiscus · Solaria | `_compare-pragma-1920-wireframe.png` · `_compare-fiscus-1920-wireframe.png` · `_compare-solaria-1920-wireframe.png` |
| **B-LAYOUT-2** | Continua section-class list differs by ≥2 entries from each existing sibling | `walk-log.md §section-list` |
| **B-LAYOUT-3** | Continua's L1–L9 classification matches LF-5 declaration · ≥4 of 9 dimensions differ vs every sibling · no L1–L9 collision | `walk-log.md §layout-classification` + appended row in `corporate-suite-layout-family-matrix.md §2` |

### Standard corporate-suite rubric (existing, all REQUIRED)
- Style-critic side-by-side at 1920px (skin pair, in addition to the wireframe pair).
- Contrast: h1 AAA on cream / dark-plate · KPI band descendant ≥ AA + ΔL ≥120 · CTA primary AAA on its background · whistleblowing column legible.
- Responsive: 1920 · 1440 · 1280 · 1100 · 880 · 720 · 480 · all sections render correctly · hamburger drawer at ≤880px · footer stack at ≤720px keeps whistleblowing surfaced.
- Locale: IT renders correctly (EN/FR/ES/AR not yet activated · the locale pill should not expose them yet — registry locale list = [it]).
- Focus: Tab traversal hits hero CTA → nav links → cycle cells → pillars → KPI → sectors → leadership cards → cases timeline rows → CTA closer → footer. Gold ring on every interactive.
- Reduced-motion: `prefers-reduced-motion: reduce` zeroes out marquee + reveal animations.
- Cases preview reachability: 4/4 case-study detail pages 200 in staff session via timeline rows.
- Editor isolation: `/live/templates/continua/?preview=1` does not show editor click-to-edit affordances unless `body.mw-is-editor-preview` is set.

### Regression walk on frozen siblings (all BLOCKING)
- Pragma 1920px wireframe = pre-rebuild capture (0 px diff).
- Fiscus 1920px wireframe = pre-rebuild capture (0 px diff) · slot-4 cycle still renders.
- Solaria 1920px wireframe = pre-rebuild capture (0 px diff) · manifesto + percorsi + omitted leadership preserved.
- All three: full corporate-suite rubric still passes · test suite still 375/375 · existing scorecards' aggregate unchanged.

### Aggregate
- Continua scorecard ≥ 4.50 · 0 BLOCKING · ≤3 STRONG.
- 0 fixes mid-walk.

---

## 7 · What must not be touched before the LF-5 rebuild lands

Hard prohibitions for this pass and any incidental edit while the rebuild is in flight.

- **Pragma source files** — `home.html`, `_base.html`, `template_content_pragma.py`. Frozen.
- **Fiscus source files** — same. Frozen, including the slot-4 cycle cell.
- **Solaria source files** — same. Public-flip held; tier stays `draft`; locale list unchanged.
- **Solaria `?preview=1` propagation** — closed in `phase_x4_corporate_suite_case_parent_fix`; do not touch.
- **The shared `home.html`** — only edited as part of Step C (refactor into `_layouts/{lf1..lf5}/`). No other edits. If the rebuild needs an unrelated tweak in the shared shell, defer it.
- **`templates/live_templates/business/corporate-suite/{about,contact,services,case_study_detail,case_study_list}.html`** — out of scope for this pass. The rebuild touches `home.html` and `_base.html` only.
- **`apps/catalog/views.py`** — no view changes. The `cases_parent_slug` resolver landed in `phase_x4_corporate_suite_case_parent_fix` and stays.
- **Test fixtures + tests** — adjustments are allowed only where the LF-5 page_data shape requires new keys. No drive-by test cleanup.
- **Multilingual pipeline** — no edits to translation files, registry locale lists, or the locale switcher beyond what LF-5's chrome dispatch requires (chrome dispatch is structural, not locale-related).
- **Tier flip plumbing** — no `sync_template_tiers` invocation. `tier=draft` preserved.
- **5th-sibling LF-2 work** — out of scope. Do not start LF-2 in this pass even if LF-5 finishes early. LF-2 is a separate enrollment with its own brief.
- **Pragma↔Fiscus 2/9 audit** — out of scope. Documented in the divergence plan §10 Step 7.

---

## 8 · Why Continua multilingual still waits

The deferred locales (EN, FR, ES, AR + AR RTL) wait until **after** this rebuild lands GREEN at LF-5 in IT. Three reasons, ordered from most concrete to most strategic.

1. **The translatable surfaces themselves change shape.** LF-5 alters where every IT string sits — the hero h1 moves into a photo overlay, the eyebrow + sub move into credit blocks, the cycle moves to slot-2, the cases become a timeline with a horizon column, the footer gains a whistleblowing column. Translating those surfaces at LF-3 means re-translating them at LF-5 — pure waste. Translation should happen against the final shape, once.
2. **Italic-em positioning is layout-sensitive and resets per locale.** CS-EXEC-01 / R7 requires the `<em>` to land on a specific word in each locale's voice anchor. The IT em-anchor is photo-coordinate-dependent in LF-5 (it lands on the photo overlay's lower-third, which has variable luminance). EN/FR/ES/AR translators receive a per-locale brief telling them which translated word carries the italic — and that brief is invalid until the LF-5 hero is final. Issuing the brief now would require re-issuing it after LF-5 lands, which means the FR/ES/AR translation work runs twice.
3. **Walk arithmetic.** Solaria Pass B precedent: 5 locales × 7 cells = ~35 walk cells per multilingual pass. Walking Continua at LF-3 (~35 walks) and again at LF-5 (~35 walks) costs ~70 walks. Building LF-5 first, walking once IT-only (~7 walks), then porting once to 4 locales (~35 walks) costs ~42 walks total. The savings are 28 walks, plus the avoided re-translation cost.

The user-handshake gate from R-SOL-8 also applies — public-flip waits for explicit authorization. Multilingual rollout for Continua is its own future workstream (workflow C), opened only after this rebuild ships and the user authorizes the next pass. **Sequence is structural-rebuild → IT-only walk → user OK → multilingual port → public-flip.** No shortcut.

A second-order reason: the family-matrix occupancy stabilises only after LF-5 lands. If the rebuild surfaces a problem with the family declaration (e.g., the `pillar-photo` leadership data shortfall escalates and L6 changes), the family's L1–L9 tuple may shift — and the multilingual brief is built on top of that tuple. Locking the tuple before translating is the only sequencing that doesn't waste downstream work.

---

## 9 · Acceptance summary

The rebuild is filed GREEN when, all in one pass:

- Pragma · Fiscus · Solaria render byte-equivalent to the Step A baselines (0 px wireframe drift, full rubric passes).
- Continua renders LF-5 in IT and passes B-LAYOUT-1 (≥30% wireframe-area difference vs each sibling), B-LAYOUT-2 (section-list ≥2-entry difference vs each sibling), B-LAYOUT-3 (live classification = LF-5 · ≥4/9 dimensions differ vs each sibling · no L1–L9 collision).
- Continua passes the standard corporate-suite browser rubric at IT.
- `factory/reports/scorecard/continua-pass2-lf5/` contains build-report · style-critic · browser-verifier · responsive-auditor · contrast-accessibility · scorecard · summary, plus the wireframe pair captures and the regression evidence on the three frozen siblings.
- Test suite stays at the project-wide green baseline (375/375 at this report's time, allowing for additions if the registry migration drives new tests).
- `MEMORY.md` is updated with a checkpoint pointing at this brief and the new scorecard directory.
- Continua tier stays `draft`. Continua locales stay `[it]`. The user-authorization gate for multilingual is held.

That is the entire scope. Anything beyond it (LF-2 build, multilingual port, public flip, Pragma↔Fiscus 2/9 audit) belongs to a later pass.
