# Causa · A.5 build · release-gatekeeper scorecard

**Status**: GREEN at A.5 build · NOT release-ready (Workflow C + D held)
**Date**: 2026-05-03
**Aggregate**: 4.7 / 5
**Decision**: **HELD at tier=draft** for explicit user handshake per R-SOL-8 / CS-BLOCK-13 / D-102 cadence

---

## §1 · D-102 cadence checkpoint

| Phase | Required | Status |
|---|---|---|
| A.5 build · IT only · tier=draft | Ship Italian content + registry/DNA/imagery/seed wiring · NO public flip | ✅ Delivered |
| A.6 review-lock | IT review walks LF-2 12 walk gates + frozen-sibling regression | (NEXT · gated on this report's sign-off) |
| Workflow C multilingual | Add EN/FR/ES/AR with verbatim-in-translation voice anchor + LF-2-scoped Naskh AR h1 | (HELD · separate pass) |
| Workflow D public flip | Tier draft → published_live · 7 explicit-literal test bumps `24` → `25` and `"24+"` → `"25+"` in `apps/catalog/tests.py` | (HELD · explicit user handshake required per R-SOL-8 / CS-BLOCK-13) |

**A.5 GREEN · A.6 ready · C/D held as planned.** ✅

---

## §2 · Hard-constraint compliance

| Constraint | Verdict | Evidence |
|---|---|---|
| do not touch apps/editor | ✅ | zero edits |
| do not touch apps/projects | ✅ | zero edits |
| do not touch apps/commerce | ✅ | zero edits |
| do not create a new archetype | ✅ | reuses corporate-suite + LF-2 dispatch |
| do not widen beyond IT | ✅ | TEMPLATE_CONTENT entry has only `it` key |
| keep tier as draft | ✅ | TEMPLATE_REGISTRY.json `tier=draft` · sync_template_tiers shows 24/1 |
| preserve LF-2 family logic | ✅ | 13/13 LF-2 family signatures intact (cs-nav--lf2 · stacked-editorial · KPI overlay · drop-cap · sectors-ribbon · single-portrait · 3+1 magazine · cream CTA closer · 4-col whistleblowing footer · cs-lf-lf-2 body class · LF-2-scoped Naskh swap inherited · 5-link nav · zero dark bands on home) |
| do not collapse into Cornice | ✅ | 12/12 skin-axis differences verified (voice · palette · typography · hero subject · founder · wordmark · geography · nav labels · KPI cells · CTA · whistleblowing column · vocabulary set) |
| do not regress the 5 live siblings | ✅ | 5/5 frozen siblings 200 anonymous · zero edits to sibling content modules |
| browser-live verification central | ✅ | 9 staff-preview routes 200 + 6 anonymous-draft-gate checks 404 + 18/18 DOM probes + 12 captures |
| be conservative | ✅ | one mid-build collision fix (4-line addition) · zero refactors · zero unrequested cleanup |

**12/12 hard constraints satisfied.** ✅

---

## §3 · Test status

```
$ python manage.py test
Ran 546 tests in 166.682s
OK

$ python manage.py test apps.catalog
Ran 171 tests in 2.213s
OK
```

**546/546 + 171/171 OK.** ✅

---

## §4 · Required reports inventory

| Report | Path | Status |
|---|---|---|
| Build report | `factory/reports/causa/causa-a5-it-build.md` | ✅ |
| Browser verification | `factory/reports/browser-verification/causa-a5-it-build.md` | ✅ |
| Build report scorecard | `factory/reports/scorecard/causa-a5-it-build/build-report.md` | ✅ |
| Style critic scorecard | `factory/reports/scorecard/causa-a5-it-build/style-critic.md` | ✅ |
| Contrast accessibility scorecard | `factory/reports/scorecard/causa-a5-it-build/contrast-accessibility.md` | ✅ |
| Responsive auditor scorecard | `factory/reports/scorecard/causa-a5-it-build/responsive-auditor.md` | ✅ |
| Browser verifier scorecard | `factory/reports/scorecard/causa-a5-it-build/browser-verifier.md` | ✅ |
| Release gatekeeper scorecard | `factory/reports/scorecard/causa-a5-it-build/release-gatekeeper.md` | ✅ (this file) |
| Aggregated scorecard | `factory/reports/scorecard/causa-a5-it-build/scorecard.md` | ✅ |
| Summary | `factory/reports/scorecard/causa-a5-it-build/summary.md` | ✅ |

**10/10 reports authored.** ✅

---

## §5 · Frozen sibling regression check

Each of the 5 live siblings walked anonymously after the Causa build:

| Sibling | LF | Anonymous home | Body length | Regression? |
|---|---|---|---|---|
| Pragma | LF-1 | 200 | 87 KB | NO |
| Cornice | LF-2 | 200 | 99 KB | NO (zero Cornice content edited) |
| Fiscus | LF-3 | 200 | 88 KB | NO |
| Solaria | LF-4 | 200 | 88 KB | NO |
| Continua | LF-5 | 200 | 95 KB | NO |

**0/5 regression.** ✅ Public catalog count remains 24 published_live.

---

## §6 · Held verification gates (for A.6 + Workflow C + D)

| Gate | Held until | Reason |
|---|---|---|
| Hero photo rendered subject 3-second binding-triple | A.6 review-lock live-verification | Pexels CDN fetch sandbox-blocked; URL wiring is correct |
| Founder portrait rendered LinkedIn-collapse audit | A.6 review-lock live-verification | same Pexels CDN sandbox issue |
| Naskh AR h1 swap (LF-2-scoped) | Workflow C multilingual rollout | IT-only at A.5 per D-102 |
| 5-locales × 5 page kinds + 5 × 4 case-detail = 45+ routes 200 | Workflow C multilingual rollout | IT-only at A.5 per D-102 |
| Tier flip draft → published_live + 7 explicit-literal test bumps | Workflow D + explicit user handshake | per R-SOL-8 / CS-BLOCK-13 / D-102 cadence |

---

## §7 · 5 critical dimensions roll-up

| Scorecard | Aggregate | Verdict |
|---|---|---|
| Build report | 5 / 5 | GREEN |
| Style critic | 4.85 / 5 | GREEN |
| Contrast accessibility | 4.7 / 5 | GREEN |
| Responsive auditor | 4.7 / 5 | GREEN |
| Browser verifier | 4.8 / 5 | GREEN |

**5-scorecard average: 4.81 / 5.** Marked 4.7 conservative on the gatekeeper because two image-fetch dimensions are held for A.6 live-verification.

---

## §8 · Verdict

**4.7 / 5 · GREEN at A.5 · NOT release-ready (held by design).**

Causa IT draft is **ready for A.6 review-lock** OR for human visual review at the dev server URL. Workflow C (multilingual) and Workflow D (public flip) remain held for explicit user handshake per the D-102 cadence the cluster has used for Solaria + Continua + Cornice flips.

**Public catalog count stays at 24** until the user explicitly authorises the gatekeeper-cascade documented in the planner-brief §11 and the Cornice public-flip precedent (`phase_x5_cornice_public_flip.md`):
- 1 registry edit (`tier: draft` → `tier: published_live`)
- `python manage.py sync_template_tiers`
- 7 explicit-literal test bumps in `apps/catalog/tests.py` (`24` → `25` and `"24+"` → `"25+"`)
- Re-test 546/546 OK
- Frozen-sibling 5/5 200 anonymous re-walk

That cascade is **NOT** authorised at this build. A.5 is **ready · held**.
