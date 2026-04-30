# Continua LF-5 IT rebuild · pass 2 · 2026-04-29

**Status**: GREEN · approved for human visual review · `tier=draft` preserved · multilingual deferred
**Scope**: corporate-suite layout family migration · IT only
**Pre-rebuild state**: LF-3 (Compliance Calendar) — DOM-identical to Fiscus with cycle-strip copy variant
**Post-rebuild state**: LF-5 (Stewardship Object-Hero)
**Branch**: `phase-x4b-continua-lf5-it-rebuild`
**Aggregate**: 4.85 / 5 · 0 BLOCKING · 0 REQUIRED · 1 STRONG · 2 OBSERVATION

---

## 1 · Why this pass exists

The four corporate-suite siblings (Pragma · Fiscus · Solaria · Continua) were shipping at 4–5/5 on the existing 5-axis distinctness matrix yet still reading as palette/copy variants of one master template. The diagnosis (`corporate-suite-layout-divergence-plan.md`) found that **all four siblings render the same DOM**: a single shared `home.html` with one optional cs-cycle slot. Layout grammar was never promoted to a first-class differentiation axis, so every sibling passed the matrix while the wireframes overlaid at >90% identical bounding boxes.

Continua was the most visible casualty: its only structural divergence from Fiscus was a copy difference on the slot-4 cycle cell — `(presidio · figura · orizzonte)` vs `(mese · scadenza · ambito)`. Same DOM, same hero geometry, same pillars, same cases shape, same footer. The Fiscus↔Continua layout-distinctness score was **0/9** (F-LAYOUT-01 fail state).

The hardening pass (`phase-x4b-corporate-suite-layout-divergence-plan` 2026-04-29) codified the layout-variance rules and named LF-5 (Stewardship Object-Hero) as Continua's correct family. The follow-up family-backfill pass (`phase-x4b-corporate-suite-family-backfill` 2026-04-29) wrote the migration brief at implementation level. **This pass is the rebuild itself.**

---

## 2 · What changed

The 9 layout dimensions all moved from the LF-3 baseline to the LF-5 target.

| Axis | LF-3 (today) | LF-5 (target) |
|---|---|---|
| L1 hero geometry | `split-55-45` | `object-overlay` |
| L2 section sequence | A+slot4 (cycle@4, trust@5) | D (cycle@2, no trust) |
| L3 mid-strip slot | slot-4 | slot-2 |
| L4 pillars treatment | `numbered-grid` 3-up | `2x2-with-image` 4-pillar matrix |
| L5 KPI placement | band-at-3 | band-at-4 |
| L6 leadership presence | `typographic-grid` | `pillar-photo` |
| L7 cases-preview shape | `list-row` | `timeline` |
| L8 navbar geometry | sticky-top 76px + phone | condensed-minimal-top 64px no phone |
| L9 footer structure | 3-col offices column | 4-col-with-whistleblowing |

Every move is a real DOM change: new section bounding boxes, new section ordering, new chrome dispatch. The cluster's brand contract (CS-LAYOUT-20) — typography, palette, accent budget, AAA h1, italic-em emphasis, Pexels-only imagery, locale switcher infra — is inherited verbatim from `_base.html`.

---

## 3 · How dispatch works

```
template.layout_family
  ├── ""      → corporate-suite shell defaults to LF-1 boardroom-vertical
  ├── "LF-1"  → _layouts/lf1/{styles,content}.html
  ├── "LF-3"  → _layouts/lf1/{styles,content}.html (cs-cycle slot-4 fires when cycle_strip is supplied)
  ├── "LF-4"  → _layouts/lf1/{styles,content}.html (manifesto/percorsi shape lives in content registry)
  └── "LF-5"  → _layouts/lf5/{styles,content}.html (distinct DOM scaffold)
```

The `home.html` is now a router that branches on `template.layout_family`. The LF-1 partials are byte-equivalent to the pre-X.4b shared shell, which is why Pragma · Fiscus · Solaria render unchanged.

`_base.html` chrome branches on the same field:
- Body class `cs-lf-{family}` exposed for any layout-family-scoped CSS rule.
- Nav: `cs-nav cs-nav--lf5` (64px no phone) on LF-5; cluster default otherwise.
- Footer 4th column: whistleblowing channel on LF-5; offices column otherwise.

---

## 4 · Continua page_data shape (LF-5)

The LF-5-specific keys added to `apps/catalog/template_content_continua.py`:

- `home.pillars_matrix` — 4-pillar list with `num`, `title`, `body`, `icon_image` (monochrome Pexels frame, ≤200px). Preserves the legacy 3-tuple `pillars` field for any non-LF-5 surface that might consume it.
- `home.cases_timeline` — 4 timeline rows with `slug`, `year`, `eyebrow`, `title`, `horizon_label`, `horizon`. Slugs match the existing `posts` table so timeline rows reach `case_study_detail` exactly like the legacy list-row iteration did.
- `home.whistleblowing` — sectors-band eyebrow with `eyebrow` + `channel_name`.
- `site.whistleblowing_footer` — 4-col footer column with `heading`, `eyebrow`, `note`, `email`, `policy_label`, `policy_href`.
- `home.leadership[*].station` — environmental anchor label per partner (Sala dell'archivio · Tavolo del Consiglio · Studio del compliance).
- `home.cycle_label` reframed `Ritmo di governance` → `Ciclo di governance` to mark slot-2 promotion as a governance opening, not a mid-page cadence aside.
- `home.headline` and `home.cta_heading` italic-em on `<em>generazioni</em>` (preserved from Pass 1.5).
- `home.pillars_heading` italic-em added on `<em>un solo</em>`.
- `home.cases_heading` italic-em added on `<em>una sola cadenza</em>`.
- `home.cycle_heading` italic-em added on `<em>cadenza</em>`.

IT copy is reused verbatim from Pass 1.5 wherever shape allowed; only the four new surfaces (4th pillar body, sectors whistleblowing eyebrow, timeline horizons, whistleblowing footer body) are new IT copy. No translation churn.

---

## 5 · Frozen-sibling verdict

**0 px wireframe drift on Pragma · Fiscus · Solaria.**

| Sibling | Section bounding boxes (post) | Match to baseline? |
|---|---|---|
| Pragma | cs-hero(122,686) · cs-pillars(808,712) · cs-kpi-band(1520,254) · cs-sectors(1774,163) · cs-trust(1936,366) · cs-leadership(2302,850) · cs-cases-preview(3152,747) · cs-cta(3898,412) | ✓ exact match |
| Fiscus | cs-hero(122,751) · cs-pillars(874,691) · cs-kpi-band(1564,254) · cs-sectors(1818,163) · cs-trust(1980,366) · cs-leadership(2346,942) · cs-cases-preview(3288,798) · cs-cta(4086,492) | ✓ exact match |
| Solaria | cs-hero(122,724) · cs-pillars(846,660) · cs-kpi-band(1506,254) · cs-sectors(1759,213) · cs-trust(1972,366) · cs-leadership(2338,1305) · cs-cases-preview(3642,886) · cs-cta(4528,440) | ✓ exact match |

Body class and chrome match too: `cs-lf-{lf-1,lf-3,lf-4} lm-ready` · phone-right preserved · 3-col offices footer preserved.

---

## 6 · Continua LF-5 distinctness verdict

| Pair | Differing layout dimensions | Score |
|---|---|---|
| Pragma↔Continua  | L1, L2, L3, L4, L5, L6, L7, L8, L9 | **9/9** (was 2/9) |
| Fiscus↔Continua  | L1, L2, L3, L4, L5, L6, L7, L9 | **8/9** (was 0/9) |
| Solaria↔Continua | L1, L2, L3, L4, L5, L6, L7, L9 | **8/9** (was 5/9) |

CS-LAYOUT-12 (≥4/9) — passes wide on every pair.
CS-LAYOUT-13 (≥1 of L1/L2/L7) — all three differ vs every pair.
B-LAYOUT-1 wireframe-overlay surface-area diff ≥38% on every pair.
B-LAYOUT-2 section-list diff ≥3 entries on every pair.
B-LAYOUT-3 classification = LF-5 declaration on all 9 axes.

---

## 7 · Browser walk (Playwright MCP, Chromium)

| Cell | Result |
|---|---|
| Hero AAA contrast (h1 cream-on-dark plate) | PASS |
| Section padding tokenized | PASS (LF-5 uses `--space-section-y/--space-section-x` per CS-RHYTHM-01) |
| One dark band per home | PASS (KPI slot-4 + dark CTA closer) |
| Italic-em emphasis | PASS (5 hits) |
| Accent budget per viewport | PASS |
| Pexels-only imagery, zero URL overlap | PASS |
| Sticky nav + drawer at ≤880 | PASS (drawer engages; LF-5's condensed-minimal-top stacks correctly) |
| Locale switcher | n/a (Continua locales = `[it]`; suppressed) |
| 4-col footer with whistleblowing | PASS |
| `?preview=1` propagation | PASS (11/11 home → 200) |
| Cases reachability | PASS (4/4 timeline rows → 200) |
| Editor isolation | PASS |
| Reduced motion | PASS |
| 1920/1440/1100/720/480 responsive | PASS at every breakpoint |
| Whistleblowing column reachable on every breakpoint | PASS |
| Tab traversal + focus rings | PASS (brass `:focus-visible` on every interactive) |

---

## 8 · Issues encountered + fixes applied

1. **Multi-line `{# … #}` Django comments rendered as plain text** — caused a 52px y-shift on Pragma. Fixed by switching every multi-line `{# … #}` to `{% comment %}…{% endcomment %}`.
2. **Stale `runserver` PIDs on port 8042** — half the requests landed on a pre-edit interpreter without the new field. Fixed by `taskkill /F` on both PIDs.
3. **Existing CS contract tests scanning the now-router `home.html`** — 6 tests failed because the hero/leadership/cases markup moved to `_layouts/lf1/`. Fixed by updating `setUpClass` to concatenate `home.html` + `_layouts/lf1/{styles,content}.html`.
4. Pre-existing `test_medical_and_restaurant_templates_have_booking_flag` — out of scope.

---

## 9 · Server left open

```
python manage.py runserver 127.0.0.1:8042 --noreload
```

Listening at **http://127.0.0.1:8042/**. Walked URLs in a `cs_review_fix` superuser session.

---

## 10 · What was held back

- Tier flip (`tier=draft` preserved).
- Multilingual rollout (5 locales × ~7 cells deferred to a future workflow C pass).
- Public-flip handshake (cluster gate R-SOL-8).
- Pragma↔Fiscus 2/9 audit (deferred per divergence-plan §10 Step 7).
- 5th-sibling LF-2 build (deferred per §10 Step 6).
- Hero `<picture>` + srcset (deferred to imagery hardening pass).

---

## 11 · Next action

> The user reviews the LF-5 walk artifacts under `factory/reports/scorecard/continua-pass2-lf5/` and the live render at `http://127.0.0.1:8042/templates/business/continua-stewardship/preview/?preview=1`. On approval, this branch merges to `main`, the layout-family-matrix §2 row is annotated `Continua → LF-5 active 2026-04-29`, and the next workstream — **Continua multilingual port (workflow C)** — is opened against the locked LF-5 IT shape.
