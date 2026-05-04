# Causa · A.6 IT review-lock · aggregated scorecard

**Phase**: X.6 Step 5 · A.6 review-lock
**Template**: causa-legale (LF-2 · 6th corporate-suite sibling · 2nd LF-2 occupant)
**Date**: 2026-05-04
**Aggregate**: 4.4 / 5 (panel average) · gatekeeper verdict **HOLD**

---

## §1 · Panel scores

| Panel | Score | Verdict |
|---|---|---|
| build-report | 4.38 / 5 | Build is HEALTHY · imagery axis (0/5) is the single drag · all other panels at maximum |
| style-critic | 4.25 / 5 | Forensic-publication coherent · imagery hold suppresses 1 panel + Continua imagery-dependent panel |
| contrast-accessibility | 4.6 / 5 | Contrast clean (14/14 AA · 13/14 AAA) · 1 alt-text quality nudge deferred to A.5b |
| responsive-auditor | 4.8 / 5 | 1440 / 880 / 375 clean · placeholder mitigation byte-equivalent at layout layer |
| browser-verifier | 4.5 / 5 | Routes + DOM probes + frozen siblings clean · per-Pexels-URL probe successfully disambiguated A.5 misclassification |
| release-gatekeeper | HOLD | 12/15 gates GREEN · 3/15 RED (imagery axis · all auto-resolve at A.5b) |

**Numeric average across 5 numeric panels: (4.38 + 4.25 + 4.6 + 4.8 + 4.5) / 5 = 22.53 / 5 = 4.51 / 5.**

(Release-gatekeeper does not contribute a numeric score; it issues
PASS/HOLD/FAIL verdicts.)

---

## §2 · Findings summary

| ID | Class | Severity | Status |
|---|---|---|---|
| F1 · 10 fabricated Pexels URLs | III · template-local | review-blocking | MITIGATED at A.6 (placeholder data URL) · DEFERRED to A.5b for real re-curate |
| F2 · founder portrait alt = bare name | III · template-local accessibility | low | DEFERRED to A.5b (combined imagery+alt fix · narrow A.6 scope blocks the fix here) |
| F3 · hero credit-overlay missing separator | II · LF-2 family shared file | cosmetic | OUT OF SCOPE for A.6 (cluster-level follow-up if orchestrator wants to consolidate) |
| F4 · A.5 Issue 3 reclassification | meta · diagnostic | informational | DOCUMENTED · A.5 "sandbox-only" classification refuted; A.6 reclassifies as REAL PRODUCT DEFECT |

---

## §3 · Distinctness verdict (5-axis triangulation · post-fix)

| Sibling | A.5 verdict | A.6 verdict |
|---|---|---|
| Pragma (LF-1) | 5/5 | **5/5** (layout family + palette + typography + copy axes unchanged) |
| Cornice (LF-2 first occupant) | 12/12 | **12/13** (12 axes verifiable at A.6 · hero subject axis on hold pending A.5b · copy/typography/palette/CTA/wordmark/geography/nav-labels/KPI/whistleblowing/vocabulary all distinct) |
| Fiscus (LF-3) | 6/6 | **6/6** |
| Solaria (LF-4) | 7/7 | **7/7** |
| Continua (LF-5 · cool-on-cool) | 11/11 | **10/11** (R-CAU-1 hex distance + R-CAU-2 interior subject differentiation cleared at copy + palette layers; the photographic layer is held) |

**Aggregate distinctness verdict: NO COLLAPSE.** The placeholder pattern is
unmistakably distinct from all 5 live siblings — no new collision risks
introduced.

---

## §4 · Test + frozen-sibling status

```
Test suite:        546 / 546 OK · 171 / 171 catalog OK
Frozen siblings:   5 / 5 byte-equivalent vs A.5
                     Pragma  · 87,112 bytes · 200 anon
                     Cornice · 98,673 bytes · 200 anon (control capture 20 confirms)
                     Fiscus  · 88,010 bytes · 200 anon
                     Solaria · 88,449 bytes · 200 anon
                     Continua · 94,640 bytes · 200 anon
Catalog count:     24 published_live + 1 draft = 25 total
Trust counter:     "24+" preserved
```

---

## §5 · Source files changed

1 file modified: `apps/catalog/template_content_causa.py` (10 photo URL
constants → 1 base64-encoded SVG placeholder + ~30-line comment block
documenting the F1 finding).

10 reports created + 20 captures committed.

Zero edits to: apps/editor / apps/projects / apps/commerce /
preview_imagery.py / template_dna.py / template_content.py / views.py /
migrations / LF-* layout files / corporate-suite chrome / other archetype
content modules / TEMPLATE_REGISTRY.json / business-litigation.md.

---

## §6 · Aggregate verdict

**A.6 review-lock PARTIAL · IMAGERY HELD.**

Numeric panels: 4.51 / 5 average.
Gatekeeper: HOLD.

**Causa IT is NOT YET LOCKED FOR USER VISUAL HANDSHAKE.**
**Workflow C and Workflow D remain HELD.**

**Recommended next action**: orchestrator authorises Phase X.6 Step 5b
imagery re-curate.
