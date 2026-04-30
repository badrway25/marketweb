# Continua Pass 2 · LF-5 IT rebuild — build report

**Status**: GREEN · IT-only · `tier=draft` preserved · multilingual deferred
**Date**: 2026-04-29
**Branch**: `phase-x4b-continua-lf5-it-rebuild`
**Reads**: `factory/reports/hardening/corporate-suite-layout-{divergence-plan,variance-rules,family-matrix,family-backfill}.md` · `design-orchestrator/references/internal-baselines/{corporate-suite-layout-family-assignment.md,continua-lf5-migration-brief.md}`

---

## 1 · What this pass changed

Phase X.4b structural rebuild. Continua migrated from **LF-3 (Compliance Calendar) → LF-5 (Stewardship Object-Hero)** with the minimum architecture needed to make layout families a first-class differentiation axis without disturbing the three frozen siblings.

### Source files touched

| File | Change | Blast radius |
|---|---|---|
| `apps/catalog/models.py` | + `WebTemplate.layout_family` CharField (max 8 · indexed · default `""`) | Schema only — empty default keeps every non-corporate-suite template untouched |
| `apps/catalog/migrations/0006_webtemplate_layout_family.py` | New AddField + idempotent data migration backfilling Pragma=LF-1 · Fiscus=LF-3 · Solaria=LF-4 · Continua=LF-5 | Data only — reverse path clears the four rows |
| `apps/catalog/template_content_continua.py` | + `pillars_matrix` (4-pillar 2×2 with icons) · `cases_timeline` (timeline rows) · `whistleblowing` (sectors-band eyebrow) · `site.whistleblowing_footer` (4-col footer column) · `leadership[*].station` (environmental anchor) · `cycle_label` reframed Calendario→Ciclo di governance | Continua-only — every other template's content registry is untouched |
| `templates/live_templates/business/corporate-suite/_layouts/lf1/styles.html` (new) | Boardroom-vertical CSS extracted byte-equivalent from the pre-X.4b shared `home.html` `extra_css` block | Used by Pragma · Fiscus · Solaria |
| `templates/live_templates/business/corporate-suite/_layouts/lf1/content.html` (new) | Boardroom-vertical markup extracted byte-equivalent from the pre-X.4b shared `home.html` `content` block | Same |
| `templates/live_templates/business/corporate-suite/_layouts/lf5/styles.html` (new) | LF-5 Stewardship Object-Hero CSS — object-overlay hero, slot-2 cycle, 2×2 pillars matrix, slot-4 KPI, sectors with whistleblowing slot, pillar-photo leadership, vertical timeline, condensed-minimal-top nav scope | Continua-only |
| `templates/live_templates/business/corporate-suite/_layouts/lf5/content.html` (new) | LF-5 markup with section sequence D | Same |
| `templates/live_templates/business/corporate-suite/home.html` | Replaced with router that includes `_layouts/lf5/{styles,content}.html` when `template.layout_family == "LF-5"`, else `_layouts/lf1/{styles,content}.html` | Dispatch only |
| `templates/live_templates/business/corporate-suite/_base.html` | + `body class="cs-lf-{slug}"` modifier · `cs-nav cs-nav--lf5` modifier (height 76→64 · no phone-right) · 4th footer column branches: LF-5 renders `cs-foot-col--whistleblowing`, others render offices · LF-5 chrome CSS rules added | LF-5 only — LF-1/LF-3/LF-4 chrome is byte-equivalent |
| `apps/catalog/tests.py` | `CorporateSuiteChromeContractTests.setUpClass` and `CorporateSuiteRhythmContractTests.setUpClass` concatenate `home.html` + `_layouts/lf1/{styles,content}.html` so the existing CS-* contracts continue to bind to the LF-1 grammar | Test infra only |

### Files explicitly NOT changed

- `apps/editor/**` · `apps/projects/**` · `apps/commerce/**` (hard constraint)
- `apps/catalog/views.py` (the existing `cases_parent_slug` + `?preview=1` propagation closed in `phase_x4_corporate_suite_case_parent_fix` continues to hold unchanged)
- `apps/catalog/template_content_pragma.py` · `template_content_fiscus.py` · `template_content_solaria.py` · every other `template_content_*.py`
- `templates/live_templates/business/corporate-suite/{about,contact,services,case_study_detail,case_study_list}.html`
- `templates/live_templates/**/*` outside corporate-suite
- Locale registry · multilingual files · tier flip plumbing

### Output sequence at runtime

```
template.layout_family
  ├── ""      → corporate-suite shell defaults to LF-1 boardroom-vertical
  ├── "LF-1"  → _layouts/lf1/{styles,content}.html (Pragma)
  ├── "LF-3"  → _layouts/lf1/{styles,content}.html (Fiscus — same scaffold; cs-cycle gate at slot-4 fires when content registry supplies cycle_strip)
  ├── "LF-4"  → _layouts/lf1/{styles,content}.html (Solaria — same scaffold; manifesto/percorsi shape lives in content registry)
  └── "LF-5"  → _layouts/lf5/{styles,content}.html (Continua — distinct DOM scaffold)
```

The router preserves byte-equivalent output for LF-1/LF-3/LF-4 because they all dispatch to the same `lf1/` partials, which were extracted verbatim from the pre-X.4b shared shell.

---

## 2 · Server command + URLs left open

```
python manage.py runserver 127.0.0.1:8042 --noreload
```

Listening at **http://127.0.0.1:8042/** (PID 58128 at the close of this report). Single listener; both prior runs were killed cleanly with `taskkill /F`.

Walked URLs (staff `cs_review_fix` superuser session):

- Continua LF-5 home   · http://127.0.0.1:8042/templates/business/continua-stewardship/preview/?preview=1
- Pragma  regression   · http://127.0.0.1:8042/templates/business/pragma-corporate-suite/preview/?preview=1
- Fiscus  regression   · http://127.0.0.1:8042/templates/business/fiscus-commercialista/preview/?preview=1
- Solaria regression   · http://127.0.0.1:8042/templates/business/solaria-coaching/preview/?preview=1

Continua case-study reachability (4/4 200): `…/mandati/{famiglia-a,famiglia-b,famiglia-c,famiglia-d}*/?preview=1`.

---

## 3 · LF-5 layout moves actually implemented

All nine L-axes moved from the LF-3 baseline to the LF-5 target.

| Axis | Pre-rebuild (LF-3) | Post-rebuild (LF-5) | Implementation |
|---|---|---|---|
| L1 hero geometry | `split-55-45` (serif h1 LEFT + photo RIGHT, 1.3fr/1fr) | `object-overlay` (full-bleed photo + h1 in lower-third dark plate + dual credit overlays top-L/top-R) | `_layouts/lf5/styles.html` `.cs-hero { position: relative; min-height: 720px }` + `.frame` lower-third gradient plate |
| L2 section sequence | A+slot4 (cycle at 4, trust at 5) | D (cycle at 2, trust dropped, leadership at 6, timeline cases at 7) | `_layouts/lf5/content.html` reorders `<section>` blocks; trust marquee deliberately absent |
| L3 mid-strip slot | slot-4 (cs-cycle between KPI + sectors) | slot-2 (cs-cycle immediately after hero) | Content reordering · same `(eyebrow, figure, context)` tuple shape preserved |
| L4 pillars treatment | `numbered-grid` (3-up auto-fit) | `2x2-with-image` (4 pillars in 2×2 with monochrome icons) | New `.cs-pillars .matrix` grid + new `pillars_matrix` page_data shape with `icon_image` per cell |
| L5 KPI placement | band-at-3 | band-at-4 (post-cycle, post-pillars) | Pure section-order shift; same KPI band primitive |
| L6 leadership presence | typographic-grid | pillar-photo (3 environmental portraits + station label) | New `.pillar-photo` 4:5 figure block at top of card · `partner.station` field added |
| L7 cases-preview shape | list-row (numbered table) | timeline (year-on-rail + title + horizon column + arrow, 1px primary rule on left rail with accent-tinted dot at year intersection) | New `.cs-cases-preview .timeline` grid + new `cases_timeline` page_data entries |
| L8 navbar geometry | sticky-top 76px with phone-right | condensed-minimal-top 64px without phone-right | `_base.html` `cs-nav--lf5` class modifier · `{% if template.layout_family != "LF-5" %}` gate on the phone block |
| L9 footer structure | 3-col (brand + sitemap + contact + offices = 4 cols at the CSS layer with offices as the 4th) | 4-col-with-whistleblowing (brand + sitemap + contact + whistleblowing channel) | `_base.html` 4th-col branches on `layout_family`; `site.whistleblowing_footer` block in Continua content |

LF-5 also shifts the **sectors band** to surface a `Tutela del segnalante · Canale interno · D.lgs. 24/2023` eyebrow (`page_data.whistleblowing`), which is the family's first-class flag of the legal channel that the 4-col footer also addresses. CS-TONE-03 (one dark band per home) stays satisfied: KPI band at slot-4 is the dark beat; CTA closer at slot-8 is the closer beat the rule already permits cluster-wide.

---

## 4 · What visibly changed in first scroll and page rhythm

**First scroll (above-the-fold at 1920×1080):**

Pre-rebuild Continua showed a 55/45 split: serif headline LEFT on cream paper with a stewardship-horizon-strip below, a darkened library photo + credit RIGHT. Two visible vertical zones, paper-on-the-left + photo-on-the-right.

Post-rebuild Continua shows a single full-bleed library photograph filling the viewport. Two credit cells pin the top-left and top-right corners of the photo (no body chrome carved out for them). The serif headline `La continuità di una famiglia si misura in *generazioni*.` overlays the lower-third on a translucent dark plate, with the intro paragraph + filled-brass CTA + ghost CTA inside the overlay frame. Below the photo, a single cream-paper band carries the stewardship-horizon-strip (Mandato medio · 18 anni / Generazioni in carico · 3 / Riunioni CdF · 4 per anno) full-bleed across the viewport.

**Page rhythm (hero → CTA closer):**

| # | Pre-rebuild slot | Post-rebuild slot |
|---|---|---|
| 1 | cs-hero (split serif/photo) | cs-hero (object-overlay) |
| 2 | cs-pillars (3-up numbered) | cs-cycle (slot-2 governance · cream paper · 3 cells) |
| 3 | cs-kpi-band (dark) | cs-pillars (2×2 matrix · paper-2 · 4 cells with icons) |
| 4 | cs-cycle (slot-4 calendar tuple) | cs-kpi-band (dark · slot-4) |
| 5 | cs-sectors | cs-sectors + whistleblowing eyebrow |
| 6 | cs-trust marquee | cs-leadership (pillar-photo with environmental portraits) |
| 7 | cs-leadership (typographic) | cs-cases-preview (vertical timeline) |
| 8 | cs-cases-preview (list-row) | cs-cta (dark closer) |
| 9 | cs-cta (dark) | — |

Section count drops from 9 to 8 (cs-trust marquee absorbed by cs-sectors). The cycle promotes from mid-page to the slot-2 opening beat (governance is now the second thing the visitor reads after the hero, not the eighth). Pillars become an icon-marked custodia matrix that reads as four object-glyphs not a row of numbered prose. Cases preview reads as a vertical timeline with year-on-rail rather than a numbered table.

---

## 5 · Frozen-sibling regression verdict

**0 px wireframe drift on Pragma · Fiscus · Solaria.** Each sibling's `<section class="cs-*">` bounding box at 1920px exactly matches the pre-rebuild capture (see `_baseline/section-list-{pragma,fiscus,solaria}.json` vs `_regression-{pragma,fiscus,solaria}/`).

| Sibling | Section list (rendered) | Y-positions match baseline | DOM shape preserved |
|---|---|---|---|
| Pragma  | 8 sections · cs-hero(122) · cs-pillars(808) · cs-kpi-band(1520) · cs-sectors(1774) · cs-trust(1936) · cs-leadership(2302) · cs-cases-preview(3152) · cs-cta(3898) | ✓ all 8 match | ✓ |
| Fiscus  | 8 sections · cs-hero(122) · cs-pillars(874) · cs-kpi-band(1564) · cs-sectors(1818) · cs-trust(1980) · cs-leadership(2346) · cs-cases-preview(3288) · cs-cta(4086) | ✓ all 8 match | ✓ |
| Solaria | 8 sections · cs-hero(122) · cs-pillars(846) · cs-kpi-band(1506) · cs-sectors(1759) · cs-trust(1972) · cs-leadership(2338) · cs-cases-preview(3642) · cs-cta(4528) | ✓ all 8 match | ✓ |

Body class on each: `cs-lf-{lf-1,lf-3,lf-4} lm-ready`. `cs-nav` keeps phone-right. `cs-foot` keeps offices column. `cs-foot-col--whistleblowing` is absent on the three frozen siblings. Pragma/Fiscus/Solaria full corporate-suite contract suites pass (33/33).

The `phase_x4_corporate_suite_case_parent_fix` `cases_parent_slug` propagation continues to work — verified separately on the live Pragma/Fiscus/Solaria homes; staff session 11/11 home → 200 holds.

---

## 6 · Distinctness verdict vs Pragma · Fiscus · Solaria

After the migration, Continua's L1–L9 tuple differs from each sibling's tuple on the dimension count below:

| Pair | Differing dimensions | Layout-distinctness score |
|---|---|---|
| Pragma   ↔ Continua | L1 · L2 · L3 · L4 · L5 · L6 · L7 · L8 · L9 | **9 / 9** (was 2/9) |
| Fiscus   ↔ Continua | L1 · L2 · L3 · L4 · L5 · L6 · L7 · L9 | **8 / 9** (was 0/9 — F-LAYOUT-01 fail state cleared) |
| Solaria  ↔ Continua | L1 · L2 · L3 · L4 · L5 · L6 · L7 · L9 | **8 / 9** (was 5/9) |

CS-LAYOUT-12 (≥4/9 dimensions differ) — passes wide on every pair. CS-LAYOUT-13 (≥1 of L1/L2/L7 differs) — passes on every pair (L1 + L2 + L7 all differ). B-LAYOUT-1 wireframe overlay shows ≥30% bounding-box surface-area change vs each frozen sibling. B-LAYOUT-2 section-list comparison shows ≥2-entry difference (cs-trust dropped + cs-cycle inserted at slot-2 + cs-pillars/cs-kpi-band/cs-leadership reordered) vs each frozen sibling. B-LAYOUT-3 classification reads LF-5 cleanly.

---

## 7 · Issues found and fixes applied

### Issue 1 · Multi-line `{# … #}` template comments rendered as text (REGRESSION on Pragma/Fiscus/Solaria)

When the regression walk ran on Pragma, `cs-hero` was at y=174 instead of the baseline y=122 — a 52px gap had appeared between the nav and the hero. The section bounding boxes themselves were unchanged width-wise, only the y-anchor had shifted.

**Root cause**: Django's `{# … #}` comment syntax is **single-line only**; multi-line `{# … #}` is treated as plain text. The new `_layouts/lf1/content.html` opened with a 5-line `{# LF-1 / LF-3 / LF-4 home content … #}` comment, which Django was rendering verbatim as a 4-line text node before the first `<section>`. The same defect was present in `_layouts/lf1/styles.html`, `_layouts/lf5/styles.html`, `_layouts/lf5/content.html`, and the new `home.html` router header.

**Fix**: Replaced every multi-line `{# … #}` with `{% comment %}…{% endcomment %}`. After server restart, Pragma's `cs-hero` returned to y=122 — exact baseline — and the Fiscus/Solaria walks confirmed exact baseline match too. Documented as a precaution in the build report so the next layout author does not repeat it.

### Issue 2 · Two stale `runserver` processes on the same port

After editing `models.py` and re-running `runserver`, two listeners showed up on port 8042 (PIDs 36764 and 12532) — the original `pkill -f runserver 127.0.0.1:8042` did not match because of how the bash tool launches background commands. Half the requests landed on the pre-edit interpreter, which had no `layout_family` field on `WebTemplate`, so the dispatch failed silently and Continua rendered LF-1.

**Fix**: Killed both PIDs with `taskkill /PID … /F`, then started a single fresh process (PID 58128). The dispatch then returned the expected LF-5 render.

### Issue 3 · Existing CS contract tests scanned the now-empty `home.html` router

Six contract tests in `apps.catalog.tests.CorporateSuite{Chrome,Rhythm}ContractTests` failed because they read `home.html` and grep for `.cs-hero .left h1`, `.cs-leadership .card .portrait`, `<section class="cs-hero">`, `{% if partner.portrait %}`, etc. After the refactor those strings live in `_layouts/lf1/{styles,content}.html`, not in the router file.

**Fix**: Updated each class's `setUpClass` to concatenate `home.html` + `_layouts/lf1/styles.html` + `_layouts/lf1/content.html` into the same `cls.home_html` string the tests already query. The contracts continue to enforce the LF-1 grammar Pragma/Fiscus/Solaria still inhabit; LF-5 is contracted by the browser walk (B-LAYOUT-1/2/3) instead.

### Pre-existing failure (not addressed)

`apps.catalog.tests.FreshSeedChainBackfillTests.test_medical_and_restaurant_templates_have_booking_flag` — fails on the booking-flag fixture set (asserts a specific set of slugs has `has_booking=True`). The failure does not touch any file I edited; reproduces on the pre-X.4b tip after stash. Logged as out of scope for this rebuild.

---

## 8 · Test summary

- 545 / 546 tests pass (the only failure is the unrelated booking-flag fixture documented above).
- 33 / 33 corporate-suite contract tests pass (`CorporateSuite{ChromeContract,RhythmContract,ThemeSafety,ImageryPolicy}Tests`).
- 4 / 4 Continua case-study detail pages reachable at status 200 from the LF-5 timeline.
- 5-cell home navbar links resolve to the 5 page slugs (`Lo studio · Chi siamo · Custodia · Mandati · Contatti`).
- 8/8 LF-5 sections render with `data-lm` reveal hooks in place.
- AAA on hero h1 (cream `#eef0f3` on translucent dark plate over photo). KPI band: cream on `#0F3A30` pine — distance ≈ 217, AAA. CTA closer: cream on pine — same.

---

## 9 · Readiness for human visual review

**YES.** Continua LF-5 IT renders cleanly at 1920 / 1440 / 1100 / 720 / 480. All 9 L-axes match the LF-5 declaration (CS-LAYOUT-14). Whistleblowing channel surfaces in the cream sectors band AND the 4-col footer column. The three frozen siblings render byte-equivalently to the pre-rebuild baseline (B-LAYOUT-1 0px verdict on all three).

Tier remains `draft`. Locale registry is `[it]` only. Public flip held pending user authorization. Multilingual rollout deferred to a future workflow C pass.
