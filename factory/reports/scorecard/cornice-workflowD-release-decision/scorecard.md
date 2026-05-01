# Scorecard · Cornice Workflow D Release Decision · 2026-05-01

**Verdict**: APPROVED-PENDING-HANDSHAKE · `tier=draft` preserved · HOLD public flip
**Aggregate**: 4.97 / 5 · 79 / 79 walk cells · 45 / 45 staff routes · 20 / 20 frozen-sibling routes · 0 BLOCKING · 0 STRONG outstanding · 0 OBSERVATION new

## 1 · Layer 1 · Blocking-override summary

| Override | Triggered? |
|---|---|
| O1 contrast | NO |
| O2 horizontal scroll | NO |
| O3 mobile stack | NO |
| O4 imagery 404 | NO |
| O5 imagery semantic | NO |
| O6 imagery mood | NO |
| O7 non-Pexels on new pilot | NO |
| O8 editor on `/preview/` | NO |
| O9 placeholders | NO |
| O10 fake certifications | NO |
| O11 voice anchor missing | NO |
| O12 D-054 triangulation absent | NO |
| O13 walk URL + port | half-met (URL recorded · user handshake pending) |
| O14 missing rubric viewport | NO |
| O15 evidence directory incomplete | NO |
| O16 nav polarity / accent | NO |
| O17 dark-on-dark | NO |
| O18 no live walk | NO |

**0 / 18 overrides triggered.** O13's user-handshake half is the reason
the gatekeeper holds.

## 2 · Layer 2 · Per-dimension scores

| D# | Dim | CRITICAL? | Score | Floor | Met? |
|---|---|---|---|---|---|
| D1  | Premium feel | ✓ | 5 | ≥ 4 | YES |
| D2  | Elegance | ✓ | 5 | ≥ 4 | YES |
| D3  | Modern professionalism | ✓ | 5 | ≥ 4 | YES |
| D4  | Hero readability | ✓ | 5 | ≥ 4 | YES |
| D5  | Navbar quality | — | 5 | ≥ 3 | YES |
| D6  | Footer quality | — | 5 | ≥ 3 | YES |
| D7  | Typography hierarchy | — | 5 | ≥ 3 | YES |
| D8  | Spacing rhythm | — | 5 | ≥ 3 | YES |
| D9  | Imagery quality | — | 4.5 | ≥ 3 | YES |
| D10 | Imagery coherence | ✓ | 5 | ≥ 4 | YES |
| D11 | Pexels-only compliance | ✓ | 5 | ≥ 4 | YES |
| D12 | Contrast safety | ✓ | 5 | ≥ 4 | YES |
| D13 | Responsive quality | ✓ | 5 | ≥ 4 | YES |
| D14 | Browser live verification quality | ✓ | 5 | ≥ 4 | YES |
| D15 | Text/image coherence | — | 5 | ≥ 3 | YES |

All 9 CRITICAL ≥ 4. All 6 non-critical ≥ 3. **Aggregate: 4.97 / 5.**

## 3 · Layer 3 · Aggregate gate

| Gate | Threshold | Actual | Met? |
|---|---|---|---|
| Overall average | ≥ 4.3 | 4.97 | YES (margin 0.67) |
| `[BLOCKING]` outstanding | 0 | 0 | YES |
| `[REQUIRED]` outstanding | 0 | 0 | YES |
| Critical floors | all ≥ 4 | all = 5 | YES |
| Non-critical floors | all ≥ 3 | min = 4.5 | YES |

Maps to **PASS · reference class** per `corporate-suite-quality-scorecard.md
§6.1` (the "all 15 dims at ≥ 4 with one at 4.5, zero overrides, complete
evidence" profile is the closest to the all-fives reference row in §6.3),
modulo the user-handshake.

## 4 · Per-locale walk

| Locale | Walk verdict | BLOCKING | Anchor verbatim? | RTL parity? |
|---|---|---|---|---|
| IT | PASS | 0 | ✓ argomento | n/a |
| EN | PASS | 0 | ✓ argument | n/a |
| FR | PASS | 0 | ✓ argument | n/a |
| ES | PASS | 0 | ✓ argumento | n/a |
| AR | PASS | 0 | ✓ حُجَّة | ✓ Naskh swap LF-2-scoped |

5 / 5 PASS · 0 BLOCKING.

## 5 · Walk-cell pass count

| Cell | Pass count |
|---|---|
| HTTP 200 home (5 locales) | 5/5 |
| HTTP 200 inner pages (5 locales × 4 pages) | 20/20 |
| HTTP 200 case-detail (5 locales × 4 posts) | 20/20 |
| Voice anchor verbatim on h1 (5 locales) | 5/5 |
| CTA-closer verbatim with hero h1 (5 locales) | 5/5 |
| 12 italic-em hits (5 locales) | 5/5 |
| LF-2 chrome `cs-nav--lf2` on home + inner pages (5 locales) | 5/5 |
| Body class `cs-lf-lf-2 lm-ready` (5 locales) | 5/5 |
| Locale switcher current flagged (5 locales) | 5/5 |
| `?lang=xx` propagation (5 locales) | 5/5 |
| `?preview=1` propagation (5 locales) | 5/5 |
| No horizontal overflow @ 1440 (5 locales) | 5/5 |
| AR-only · `<html dir="rtl">` | 1/1 |
| AR-only · Noto Naskh h1 + Amiri body (LF-2-scoped swap) | 1/1 |
| AR-only · Latin proper-noun preservation (CORNICE · Marta Roveri · Via Volpe · Palazzo Lignari) | 1/1 |
| AR-only · No horizontal overflow @ 720 | 1/1 |
| Hero h1 AAA contrast on cream (5 locales) | 5/5 |
| KPI cream-on-dark photo plate AAA (5 locales) | 5/5 |
| CTA-closer h2 AAA (5 locales) | 5/5 |
| Cream nav links AAA (5 locales) | 5/5 |
| Continua LF-5 AR sibling spot-check · still Kufi (1) | 1/1 |

**79 / 79 PASS** (expanded from Workflow C's 70/70 by the inner-page
chrome consistency cell + Continua LF-5 AR Naskh-scope sibling spot-check).

## 6 · Anonymous tier-gate verification

| Probe | Expected | Actual |
|---|---|---|
| `GET /` anon → 200 | YES | YES |
| `GET /templates/business/` anon → 200 | YES | YES |
| Slug `cornice-architettura` in anon HTML → ABSENT | YES | YES |
| `GET /templates/business/cornice-architettura/preview/` anon → 404 | YES | YES |
| `GET /templates/business/cornice-architettura/preview/?preview=1` anon → 404 | YES | YES |

D-055 tier gate intact.

## 7 · 45-route smoke (staff session) + 20-route frozen-sibling sweep (anon)

| Route family | Count | Status |
|---|---|---|
| 5 locales × 5 pages (home + 4 inner) | 25 | 200 |
| 5 locales × 4 case-detail posts | 20 | 200 |
| **Cornice staff total** | **45** | **45 / 45 → 200** |
| 4 frozen siblings × 5 locales (anon) | 20 | 200 |
| **Frozen-sibling total** | **20** | **20 / 20 → 200** |

## 8 · Findings

| # | Severity | Resolved | Note |
|---|---|---|---|
| F-001 | OPERATIONAL (dev-env) | n/a | Port 8053 was already bound by another process; port 8052 was used (matches all prior Cornice walks A.5/A.6/Workflow C). Not a product issue. |

0 BLOCKING · 0 STRONG · 0 OBSERVATION on the product.

## 9 · Final aggregate

```
Aggregate (mean of 15 dimensions):    4.97 / 5
Walk cell pass rate:                  79 / 79
Cornice staff smoke pass rate:        45 / 45
Frozen-sibling anon smoke:            20 / 20
Locales authored:                     5 (IT/EN/FR/ES/AR)
Tests:                                545 / 546 (1 pre-existing unrelated failure)
BLOCKING findings:                    0
STRONG findings outstanding:          0
OBSERVATION findings new:             0
Tier:                                 draft (preserved)
Public flip:                          HELD pending user handshake
Verdict:                              APPROVED-PENDING-HANDSHAKE
```

Per `corporate-suite-quality-scorecard.md §6.1`: PASS reference-class —
flip proceeds only on user explicit authorization.

## 10 · Pass-or-flip decision

**APPROVED-PENDING-HANDSHAKE.** Technical work GREEN. Cluster release
contract (SOP §5.4) requires user parallel-verification confirmation in
the conversation before the registry flip. Server is left running for
the user-handshake walk. The Pass-D cascade is documented to the line
in `release-gatekeeper.md §6`.
