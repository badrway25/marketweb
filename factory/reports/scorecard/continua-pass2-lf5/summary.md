# Continua Pass 2 · LF-5 IT rebuild — summary

**Status**: GREEN · approved for human visual review · `tier=draft` preserved · multilingual deferred
**Date**: 2026-04-29
**Branch**: `phase-x4b-continua-lf5-it-rebuild`
**Aggregate**: 4.85 / 5 · 0 BLOCKING · 0 REQUIRED · 1 STRONG · 2 OBSERVATION

---

## What landed

Continua migrated from **LF-3 (Compliance Calendar)** to **LF-5 (Stewardship Object-Hero)** in IT only. The rebuild added the minimum architecture needed for layout families (a `WebTemplate.layout_family` field + a `_layouts/{lf1,lf5}/` dispatcher inside the corporate-suite shell), then replaced Continua's home with a full structural shape change while keeping Pragma · Fiscus · Solaria byte-equivalent.

### Files changed

- `apps/catalog/models.py` — added `WebTemplate.layout_family` (max 8 chars · indexed · default `""`).
- `apps/catalog/migrations/0006_webtemplate_layout_family.py` — schema + idempotent backfill (Pragma=LF-1 · Fiscus=LF-3 · Solaria=LF-4 · Continua=LF-5).
- `apps/catalog/template_content_continua.py` — added `pillars_matrix` (4-pillar 2×2 with icons) · `cases_timeline` (4 timeline rows) · `whistleblowing` (sectors-band eyebrow) · `whistleblowing_footer` (4-col footer column) · `leadership[*].station` (environmental anchor) · cycle eyebrow `Calendario`→`Ciclo di governance`.
- `templates/live_templates/business/corporate-suite/_layouts/lf1/styles.html` (new) — boardroom-vertical CSS extracted byte-equivalent from the pre-X.4b shared `home.html`.
- `templates/live_templates/business/corporate-suite/_layouts/lf1/content.html` (new) — boardroom-vertical markup extracted byte-equivalent.
- `templates/live_templates/business/corporate-suite/_layouts/lf5/styles.html` (new) — LF-5 Stewardship Object-Hero CSS.
- `templates/live_templates/business/corporate-suite/_layouts/lf5/content.html` (new) — LF-5 markup with section sequence D.
- `templates/live_templates/business/corporate-suite/home.html` — replaced with router that includes `_layouts/lf5/{styles,content}.html` for LF-5, `_layouts/lf1/{styles,content}.html` otherwise.
- `templates/live_templates/business/corporate-suite/_base.html` — body modifier `cs-lf-{family}`, `cs-nav cs-nav--lf5` (64px no phone), 4th footer column branches LF-5 → whistleblowing column, LF-5 chrome CSS rules added.
- `apps/catalog/tests.py` — `CorporateSuite{Chrome,Rhythm}ContractTests.setUpClass` concatenates `home.html` + `_layouts/lf1/{styles,content}.html` so existing CS-* contracts continue to bind to the LF-1 grammar.

### Reports written

- `factory/reports/continua/continua-lf5-it-rebuild.md`
- `factory/reports/browser-verification/continua-lf5-it-rebuild.md`
- `factory/reports/scorecard/continua-pass2-lf5/{build-report,style-critic,contrast-accessibility,responsive-auditor,browser-verifier,release-gatekeeper,scorecard,summary}.md`
- `factory/reports/scorecard/continua-pass2-lf5/_baseline/{4 PNGs + 4 JSONs + baseline-summary.md}`
- `factory/reports/scorecard/continua-pass2-lf5/_regression-{pragma,fiscus,solaria}/{slug}-1920-fullpage-post.png`
- `factory/reports/scorecard/continua-pass2-lf5/continua-1920|1440|1100|720|480-fullpage-lf5*.png`

---

## What visibly changed

**Hero**: 55/45 split (serif h1 LEFT + photo RIGHT) → object-overlay (full-bleed library photograph + lower-third dark plate carrying the headline + dual credit overlays at top corners). The first ~720px of the page is now a single full-bleed object-led photograph. The stewardship-horizon-strip moved from inside the LEFT cell to a cream-paper band full-bleed *below* the photo.

**Section sequence**: A+slot4 → D. The cs-cycle (governance cadence) now opens slot-2 instead of mid-page slot-4. The trust marquee was dropped. Pillars become a 2×2 custodia matrix (Custodia · Governance · Successione · Compliance) with monochrome icon glyphs instead of the 3-up numbered grid. KPI band shifts to slot-4. Sectors band gains a far-right whistleblowing eyebrow (D.lgs. 24/2023 channel · `Tutela del segnalante`). Leadership becomes a pillar-photo row with environmental station labels (Sala dell'archivio · Tavolo del Consiglio · Studio del compliance). Cases become a vertical timeline (year on rail + title + horizon column).

**Chrome**: Navbar shrinks from 76px to 64px and drops the phone-right cluster. Footer 4th column changes from `Sedi` to a whistleblowing channel column with eyebrow + body + email + policy link.

---

## Frozen-sibling verdict

| Sibling | Section list y-positions vs baseline | Body class | Phone-right | Whistleblowing column | Verdict |
|---|---|---|---|---|---|
| Pragma | exact match (8 sections) | cs-lf-lf-1 | preserved | absent | **0 px regression** |
| Fiscus | exact match (8 sections) | cs-lf-lf-3 | preserved | absent | **0 px regression** |
| Solaria | exact match (8 sections) | cs-lf-lf-4 | preserved | absent | **0 px regression** |

---

## Distinctness verdict (post-migration)

| Pair | Differing layout dimensions | Layout-distinctness score |
|---|---|---|
| Pragma↔Continua | L1·L2·L3·L4·L5·L6·L7·L8·L9 | **9 / 9** (was 2/9 — CS-LAYOUT-12 fail state cleared) |
| Fiscus↔Continua | L1·L2·L3·L4·L5·L6·L7·L9 | **8 / 9** (was 0/9 — F-LAYOUT-01 fail state cleared) |
| Solaria↔Continua | L1·L2·L3·L4·L5·L6·L7·L9 | **8 / 9** (was 5/9) |

---

## Issues encountered + fixes applied

1. **Multi-line `{# … #}` template comments rendered as text** — caused a 52px y-shift on the regression walk. Fixed by switching every multi-line `{# … #}` to `{% comment %}…{% endcomment %}`.
2. **Stale `runserver` listener on port 8042** — caused half the requests to land on a pre-edit Python process where `WebTemplate.layout_family` did not yet exist. Fixed by `taskkill /F` on both PIDs and a fresh single-process restart.
3. **CS contract tests scanning empty `home.html` router** — fixed by concatenating `_layouts/lf1/{styles,content}.html` into the test's `cls.home_html` string, so existing CS-NAV / CS-FOOT / CS-HERO / CS-TYPE / CS-RHYTHM / CS-IMG contracts continue to bind to the LF-1 grammar Pragma/Fiscus/Solaria still ship.
4. **Pre-existing `test_medical_and_restaurant_templates_have_booking_flag`** — fails on the pre-X.4b tip too; unrelated to this rebuild and out of scope.

---

## What was held back

- **Tier flip**: `tier=draft` preserved. No `sync_template_tiers` invocation.
- **Multilingual rollout**: Continua locales stay `[it]`. The 4-locale port + AR RTL is deferred to a future workflow C pass.
- **Public flip**: held pending user authorization (R-SOL-8 cluster gate).
- **Pragma↔Fiscus 2/9 audit**: deferred per `corporate-suite-layout-divergence-plan.md §10 Step 7`.
- **5th-sibling LF-2 build**: deferred per the same plan §10 Step 6.
- **Hero `<picture>` + srcset hardening**: not blocking for this pass; a future imagery hardening pass should add WebP/AVIF + multiple widths.

---

## Server left open

```
python manage.py runserver 127.0.0.1:8042 --noreload
```

Listening at **http://127.0.0.1:8042/**. Continua LF-5 IT walk URL:

> http://127.0.0.1:8042/templates/business/continua-stewardship/preview/?preview=1

Staff session as `cs_review_fix` superuser (password set to `lf5walkpass!2026` for this walk; rotate before any external visit).

---

## MEMORY.md checkpoint to add

```
- [Phase X.4b Continua LF-5 IT Rebuild · GREEN (2026-04-29)](phase_x4b_continua_lf5_it_rebuild.md) — Continua migrated LF-3 → LF-5 (Stewardship Object-Hero) in IT only · WebTemplate.layout_family field + dispatch refactor · _layouts/{lf1,lf5}/ split · object-overlay hero + slot-2 cycle + 2×2 pillars matrix + slot-4 KPI + whistleblowing eyebrow + pillar-photo leadership + timeline cases + 4-col footer with whistleblowing · 0 px regression on Pragma · Fiscus · Solaria · B-LAYOUT-1/2/3 PASS · 8-9/9 layout-dimension diff vs each frozen sibling · 545/546 tests · tier=draft preserved · multilingual deferred.
```
