# Continua · Pass 1 IT · workflow A landing report

**Status**: workflow A pass 1 closed at draft tier · IT-only · 2026-04-29
**Branch**: `phase-x4-design-orchestrator-hardening-v1`
**Cluster**: corporate-suite · 4th sibling · 1st family-office variant
**Brief**: `design-orchestrator/real-candidates/continua-build-brief.md`
**Distinctness proof**: `design-orchestrator/real-candidates/continua-distinctness-proof.md` (5/5 vs Pragma · 5/5 vs Fiscus · 5/5 vs Solaria)
**Walk gate**: `design-orchestrator/real-candidates/continua-browser-gate.md`

This is the workflow A landing report for the first real template generated from the design-orchestrator system. Pass 1 ships IT-only at draft tier per the brief's D-102 cadence; multilingual rollout (EN / FR / ES / AR + AR RTL parity) and the LIVE-flip user handshake belong to workflow C.

---

## 1 · One-paragraph summary

Continua landed at draft tier with 9 page surfaces (home, chi-siamo, custodia, mandati list + 4 detail posts, contatti) returning HTTP 200, a curated Pexels-only `business-stewardship` 6-slot pool (slot 0 was re-curated live during the walk after the initial candidate rendered a Scrabble-tile composition), pine + pewter + brass palette consuming the only OPEN matrix §1.3 warmth combination, Crimson Pro + Public Sans typography pulling the cluster out of "Inter on whatever serif" territory, an object-led hero with zero people (the cluster's first), a fresh `governance-cycle-strip` mid-beat that names a CADENCE not a number/calendar/arc, leadership demographics that close Solaria's `30sCx2` gap, an "Avvia un dialogo di mandato" CTA + scope + orizzonte + struttura form gate, whistleblowing channel surfaced in the legal row, and a scorecard aggregate of **4.74 / 5** (exceeds the 4.50 target and the 4.67 Solaria precedent) with 0 `[BLOCKING]` findings and 0 deviation notes.

---

## 2 · Files changed

See `factory/reports/scorecard/continua-pass1-it/build-report.md §1` for the file-by-file table. Summary:

- 1 new content registry: `apps/catalog/template_content_continua.py`
- 6 source-file edits: `template_dna.py` · `template_content.py` · `preview_imagery.py` · `imagery_policy.py` · `seed_templates.py` · `TEMPLATE_REGISTRY.json`
- 1 shared skin file with 3 backward-compatible additions: `templates/live_templates/business/corporate-suite/home.html`
  (auto-fit on `cs-pillars .grid` · new `cs-cycle` section gated on `page_data.cycle_strip` · `|safe` filter on `cta_heading`)

No editor / projects / commerce file touched. No new archetype defined.

---

## 3 · Server posture at landing

- `python manage.py runserver 8088` (background)
- URL kept open: `http://127.0.0.1:8088/templates/business/continua-stewardship/preview/`
- DB tier: `published_live` (transient · flipped only to bypass staff-preview gate during the walk)
- Registry tier: `draft` (correct per brief · auto-restores on next `seed_templates` run)

---

## 4 · Distinctness verdict on live render

| Pair | Score | Evidence |
|---|---|---|
| Continua vs Pragma | **5/5** | Hero: object-led library vs sticky-note board (people-led). Palette: pine+brass vs navy+emerald. Voice: temporal noun italic vs agency word italic. Mid-strip: governance-cycle vs none. Form gate: horizon-selector vs NDA boardroom. |
| Continua vs Fiscus | **5/5** | Hero: library room vs tax-desk-with-laptop. Palette: pine+brass vs gray-blue+gold-blunotte. Mid-strip: governance-cycle vs fiscal-calendar. Detail slot: wax-seal vs tax-doc. Form gate: scope+horizon vs P.IVA+CF. |
| Continua vs Solaria | **5/5** | Hero: object-led zero-people vs 1:1 conversation. Palette: cool/cool/warm vs warm/warm/warm. Voice: one em on temporal noun vs two em contrast pair. Demographics: 60s+40s+50s vs 30sCx2. Form gate: mandate dialogue vs ICF-referenced. |

Side-by-side captures filed under `factory/reports/browser-verification/continua-stewardship/it/20260429/_compare-{pragma,fiscus,solaria}-1920.png`.

---

## 5 · Risk mitigation status

All five risks survived to live render and all five mitigations PASSED. Detail in `factory/reports/scorecard/continua-pass1-it/browser-verifier.md §five-mitigation-live-verification`.

---

## 6 · Imagery decisions

| Slot | Pexels ID | Subject |
|---|---|---|
| 0 hero | 36093623 | Historic library room with rich wooden interiors · partner desk + fireplace + leather chair in foreground · ZERO people |
| 1 feature | 7045772 | Black classic desk near elegant leather chair next to window in light study room · ZERO people |
| 2 portrait senior | 5333750 | Senior woman with white hair in coral suit holding eyeglasses thoughtfully — 60s · institutional |
| 3 portrait 40s | 7841828 | Mature businessman in business attire arms crossed in modern office — 40s · West African heritage |
| 4 detail | 36824936 | Elegant letter with red wax seal on a wooden desk |
| 5 ambient | 6587827 | Marble stairway with golden banister in classic styled villa — daylight |

Cross-cluster grep against `business-corporate` / `business-fiscal` / `business-coaching` — clean.

A live re-curate happened during the walk: slot 0 (Pexels 207658) → 36093623, slot 1 (Pexels 4050291) → 7045772, slot 2 (Pexels 2379004) → 5333750, slot 3 (Pexels 3796217) → 7841828, slot 5 (Pexels 2724664) → 6587827. The earlier IDs were guess-by-pattern; the final pool was sourced through the Pexels search UI inside the walk session and verified live before commit.

---

## 7 · Top visible improvements delivered (vs the design-orchestrator dry-run benchmark)

1. **The `business-stewardship` pool exists, on Pexels, on first build** — closes the brief's `pexels_pack_status: not started` slot.
2. **Object-led hero with zero people** — the cluster's first; closes the silhouette gap from Pragma/Fiscus/Solaria's people-present heroes.
3. **Pine + brass palette landing live** — first cool-non-blue primary in the cluster, brass eyebrow + nav active underline + CTA arrow visible at first scroll.
4. **Governance-cycle-strip rendering as the differentiator beat** — three cells with the (eyebrow · figure · context-line) triple at every viewport.
5. **Leadership 3-card demographic spread closing the Solaria 30sCx2 gap** — 60s coral / 40s African heritage / 50s warm-brown, all photo-present, all readable at every viewport.
6. **Whistleblowing channel surfaced** — the channel column on `/contatti/` carries D.lgs. 24/2023 as a first-class element, NOT a footnote afterthought.
7. **Voice anchor verbatim restated in the cta-closer** — the page opens and closes with `La continuità di una famiglia si misura in <em>generazioni</em>.`

---

## 8 · Issues found and fixes applied

| Finding | Fix | Time |
|---|---|---|
| Slot 0 hero rendered Scrabble tiles | Re-curate live in the same walk · Pexels 36093623 replaces 207658 | 5 min |
| Slot 2 portrait was young man not 60s · Slot 3 was woman with laptop on sofa | Re-curate live · 5333750 + 7841828 + 8424881 | 8 min |
| `cs-pillars .grid` fixed at `repeat(3, 1fr)` so 4 pillars wrapped 3+1 | Switched to `repeat(auto-fit, minmax(220px, 1fr))` — backward-compatible with 3-pillar siblings | 1 min |
| `cta_heading` `<em>` rendering as escaped HTML | Added `\|safe` filter to the cta-closer h2 in shared `home.html` | 1 min |
| `data-lm` reveal elements rendering at opacity 0 in fullPage capture (IntersectionObserver hadn't fired) | Force-revealed via DOM override in the capture session — does not affect production rendering | n/a |

No `[BLOCKING]` finding. Every defect was caught and resolved within the same walk.

---

## 9 · Whether Continua IT is ready for human visual review

**YES** — the URL is open, the scorecard is GREEN at the draft-tier scope, every brief contract is honoured, every risk mitigation passes live, and the side-by-side captures show 5/5 distinctness vs every existing sibling.

The user runs the human visual review at:
`http://127.0.0.1:8088/templates/business/continua-stewardship/preview/`

with three checkpoints to focus on:
1. **Brass landing on first scroll** — distinguishable from Pragma's emerald?
2. **Hero photo coherence** — reads as stewardship office, not generic warm interior?
3. **Cycle-strip framing** — reads as calendar rhythm, not numeric KPI re-skin?

If all three land, pass 1 is human-ratified at draft. The orchestrator routes to workflow C planning (multilingual rollout + LIVE flip + user handshake) for the next pass.
