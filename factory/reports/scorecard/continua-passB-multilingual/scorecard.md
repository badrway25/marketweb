# Scorecard · Continua Pass B Multilingual · 2026-04-30

## 1 · Aggregate (5-axis distinctness matrix · per locale)

| Axis | IT | EN | FR | ES | AR | Notes |
|---|---|---|---|---|---|---|
| Voice anchor identity (em on temporal noun) | 5 | 5 | 5 | 5 | 5 | em-word travels in every locale |
| LF-5 layout shape (8 cs-* sections in order) | 5 | 5 | 5 | 5 | 5 | DOM verified identical |
| Imagery (Pexels-only · `_POOL_*` shared) | 5 | 5 | 5 | 5 | 5 | substitution structurally impossible |
| Tone register (institutional / custodial / multi-generational) | 5 | 5 | 5 | 5 | 5 | per-locale reference voices honoured |
| Distinctness vs Pragma · Fiscus · Solaria | 5 | 5 | 5 | 5 | 5 | matrix preserved (DOM unchanged) |

**Per-locale aggregate: 5.0 / 5** for IT · EN · FR · ES · AR.
**Pass aggregate: 5.0 / 5** (geometric mean across 5 locales).

## 2 · Panel results

| Panel | Verdict |
|---|---|
| Build report          | GREEN |
| Style critic          | GREEN |
| Contrast / accessibility | GREEN |
| Responsive auditor    | GREEN |
| Browser verifier      | GREEN |
| Release gatekeeper    | HOLD (correct posture for Pass B · workflow D opens on user-handshake) |

6 panels, 5 GREEN + 1 HOLD-by-design = pass aggregate GREEN.

## 3 · 14-cell walk × 5 locales = 70 cells

| Cell | Pass count |
|---|---|
| Hero overlay AAA | 5/5 |
| Section sequence intact | 5/5 |
| Italic-em on load-bearing word | 5/5 |
| Hero meta-strip | 5/5 |
| Pillars matrix 4-pillar 2×2 | 5/5 |
| KPI band one-dark | 5/5 |
| Sectors + whistleblowing | 5/5 |
| Leadership 3-card with stations | 5/5 |
| Cases timeline (4 rows) | 5/5 |
| CTA dark closer + voice-anchor restate | 5/5 |
| Locale switcher (5 pills) | 5/5 |
| `?lang=xx` propagation | 5/5 |
| `?preview=1` propagation | 5/5 |
| No horizontal overflow at 1440 | 5/5 |

**70 / 70 PASS.**

## 4 · Findings

| # | Severity | Resolved | Note |
|---|---|---|---|
| F-001 | STRONG | YES | LF-5-specific eyebrow surfaces RTL letter-spacing — fix landed in `_base.html` mid-walk, AR re-walked clean |
| F-002 | OBSERVATION (dev-env) | n/a | `runserver --noreload` did not pick up template edit; restart cleared |
| F-003 | OPERATIONAL | YES | DB tier transient flip for the walk; restored to `draft` via `sync_template_tiers` |

0 BLOCKING · 1 STRONG (closed) · 0 OBSERVATION on the product.

## 5 · Pass-or-fail decision

**PASS** at draft tier · workflow D / public flip held for user-handshake gate.

## 6 · Final aggregate

```
Pass B Multilingual aggregate: 5.0 / 5
Walk cell pass rate:           70 / 70
Locales authored:              5 (IT preserved + EN/FR/ES/AR added)
Routes returning 200:          45 / 45
BLOCKING findings:             0
STRONG findings (closed):      1
Tier:                          draft (preserved)
```
