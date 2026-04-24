# Walk V1 · Reduced-motion audit (P0 · T-P0-4)

**Phase**: X.4a Step 2 Round 1
**Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Run-ISO**: `20260424T2346Z`
**Driver**: Claude (Opus 4.7, Playwright MCP)
**Emulation**: `page.emulateMedia({ reducedMotion: 'reduce' })` applied at the Playwright context — confirmed live via `window.matchMedia('(prefers-reduced-motion: reduce)').matches === true` on every page.

**Verdict**: **PASS** · 0 blocking · 0 required failures · `BRWS-FEEL-08` green on both templates.

---

## Server

- **URL**: `http://127.0.0.1:8731/`
- **Start time**: 2026-04-24T23:45Z (approx · invoked as background task `bsvroh9h4`).
- **Still running**: **yes** — the server remains up for parallel verification.

## Scope

- **Templates**: Pragma (`pragma-corporate-suite`), Fiscus (`fiscus-commercialista`).
- **Pages** (12 total): home, about (`chi-siamo` / `lo-studio`), services (`competenze`), case-study list (`case-studies` / `casi-seguiti`), case-study detail (`manifatturiero-bresciano-piano-industriale` / `pmi-manifattura-bilancio-revisione`), contatti.
- **Viewport**: 1440 × 900 only (per plan §6.1 — the contract under test is JS-side motion, not CSS layout).
- **Reduced-motion media**: `prefers-reduced-motion: reduce` active on every page.

## Results per page

| Template | Page | `[data-lm]` count | Stuck opacity-0 | Footer legal hrefs | Verdict |
|---|---|---|---|---|---|
| Pragma | home                          | 26 | 0 | 3 real routes | PASS |
| Pragma | chi-siamo                     | 24 | 0 | 3 real routes | PASS |
| Pragma | competenze                    | 13 | 0 | 3 real routes | PASS |
| Pragma | case-studies                  |  5 | 0 | 3 real routes | PASS |
| Pragma | case-studies/manifatturiero-… |  7 | 0 | 3 real routes | PASS |
| Pragma | contatti                      |  0 | 0 | 3 real routes | PASS |
| Fiscus | home                          | 26 | 0 | 3 real routes | PASS |
| Fiscus | lo-studio                     | 24 | 0 | 3 real routes | PASS |
| Fiscus | competenze                    | 13 | 0 | 3 real routes | PASS |
| Fiscus | casi-seguiti                  |  5 | 0 | 3 real routes | PASS |
| Fiscus | casi-seguiti/pmi-manifattura… |  7 | 0 | 3 real routes | PASS |
| Fiscus | contatti                      |  0 | 0 | 3 real routes | PASS |
| **Totals** | **12 pages** | **150** | **0** | **36/36** | **PASS** |

## Rubric checks

- **`BRWS-FEEL-08` (strong · prefers-reduced-motion respected)** — PASS on 12/12 pages. Every `[data-lm]` element renders with its final opacity applied at page-ready; no stuck `opacity: 0` / `transform: translateY(24px)` panels. Confirmed via `document.querySelectorAll('[data-lm]')` + `getComputedStyle(el).opacity >= 0.99` on every page.
- **`BRWS-FEEL-07` (strong · console clean)** — PASS. 0 errors across the 12-page walk (the lone error seen during Pragma home is the standard `favicon.ico` 404 that the rubric explicitly waives). No JS exceptions from `live-motion.js` under reduced-motion.
- **`CS-CTA-04` (footer legal hrefs real-route)** — PASS. Side-observation: the Step 2 P0-5 footer fix is live — every footer on every page ships 3 anchors resolving via `{% url 'catalog:live_template_page' … 'contatti' %}`. Zero `href="#"` placeholders.

## Evidence

- 12 full-page screenshots under `factory/reports/browser-verification/x4a-step2/20260424T2346Z/reduced-motion/screenshots/`.
- This `verdict.md`.

## Borderline observations (out of Priority 1 scope · tracked)

- Fiscus case-study detail KPI band (`.cs-kpi-band`) dark-on-dark contrast at the bottom of `pmi-manifattura-bilancio-revisione` reads as borderline on visual inspection; digits + captions sit low-contrast on the navy band. This is an existing Layer-2 candidate for a later style-critic walk (D12 contrast), not a reduced-motion regression. **Not a P0-4 failure** — the opacity/transform contract holds.
- No other visual anomalies were surfaced by the reduced-motion emulation.

## Deviations

None. The plan §6.1 scope was `12 pages × 1 viewport = 12 cells`; the walk executed 12/12.

— end of V1 verdict —
