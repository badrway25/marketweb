# Causa · A.5 build · executive summary

**Verdict**: **GREEN review-ready** · IT-only · `tier=draft` · ready for human visual review.
**Aggregate**: **4.78 / 5** across 6 scorecards.
**Date**: 2026-05-03 · Phase X.6 Step 4 · workflow A.5 IT build.
**Branch**: `phase-x6-causa-a5-it-build`.

---

## What shipped

Causa is the 6th corporate-suite sibling and the 2nd LF-2 occupant after Cornice. Italian content layer + registry/DNA/imagery/seed wiring shipped at IT-only / draft tier per the D-102 cadence.

- 3 new files: `apps/catalog/template_content_causa.py` (1100 lines IT content) · `apps/catalog/migrations/0008_causa_layout_family.py` · this report set.
- 5 edited files: `template_content.py` registry · `template_dna.py` DNA · `preview_imagery.py` `business-legale` Pexels pool · `seed_templates.py` metadata + SEED_TEMPLATES · `TEMPLATE_REGISTRY.json` row.
- Zero edits to `apps/editor/`, `apps/projects/`, `apps/commerce/`, the corporate-suite chrome (`_base.html`), or the LF-2 layout files (`_layouts/lf2/`).

## What got verified live

- **9 staff-preview routes** all 200 (5 pages: home + studio + materie + contenzioso + contatti · 4 case-detail: Cass. SS.UU. 2024 + Cass. civ. III 2023 + TAR Lombardia 2022 + App. Milano trib. 2021).
- **6 anonymous draft-gate checks** all 404 — Causa is invisible to the public · public catalog count remains **24** unchanged.
- **5 frozen siblings** all 200 anonymous · zero edits to sibling content modules · zero regression.
- **18 DOM probes** confirm the bottle-green / bone / obsidian palette · GT Sectra + Manrope typography · LF-2 family signal (cs-lf-lf-2 · cs-nav--lf2 · cs-cta-cream · cs-cases-magazine · whistleblowing footer column).
- **Voice anchor `evidenza`** verbatim recurrence on hero h1 + cs-cta-closer-cream h2 (2 surfaces · per AC-15).
- **12 captures** at 1440 + 880 + 375 + Cornice control + 4 inner pages + 1 case-detail.

## Mid-build fix applied

The corporate-suite shared `_base.html:1241` defaults the navbar trailing CTA pill to `"Apri un fascicolo"` (Cornice's literal). Causa's home page_data carried the correct `primary_cta` but inner pages did not — bleeding Cornice's CTA copy onto Causa's navbar across all 4 inner pages. Fixed by adding `primary_cta: "Apri un parere preliminare"` to each of the 4 inner-page page_data dicts. Single-line addition × 4 surfaces. Zero edits to the shared `_base.html`. Verified live.

## Distinctness verdict

- **vs Pragma (LF-1)**: 5/5 axes distinct (different layout family) — boardroom navy-emerald vs courtroom bottle-green-bone.
- **vs Cornice (LF-2 first occupant · highest collision risk)**: 12/12 skin-axes distinct (voice · palette · typography · hero subject · founder · wordmark · geography · nav labels · KPI cells · CTA · whistleblowing column · vocabulary). Layout axes are family-shared by intent per AC-2.
- **vs Fiscus (LF-3)**: 6/6 axes distinct · R-CAU-3 mitigation confirmed (Cassazionista vocabulary collision avoided · credential SET reads forensic-publishing register).
- **vs Solaria (LF-4)**: 7/7 axes distinct.
- **vs Continua (LF-5 · second-highest collision risk · cool-on-cool)**: 11/11 axes distinct · R-CAU-1 hex distance ≥6 ΔE cleared · R-CAU-2 interior subject differentiation cleared at the imagery wiring level (rendered-subject re-test held for A.6 live-verification gate).

The 30-second wordmark-stripped read is unmistakably **"evidence-led Cassazionista litigation boutique"** — zero collapse against any of the 5 live siblings.

## Frozen sibling regression verdict

**0/5 regression.** All 5 live siblings (Pragma · Cornice · Fiscus · Solaria · Continua) render at 200 anonymous with same body length envelope as pre-Causa. Zero content edits to any sibling. Public catalog count holds at 24.

## Test status

```
Ran 546 tests in 166.682s · OK   (full suite)
Ran 171 tests in 2.213s · OK     (apps.catalog)
```

**546 / 546 + 171 / 171 OK.** Zero new failures · zero regressions.

## Held for A.6 + Workflow C + Workflow D

1. **R-CAU-2 hero rendered subject** re-test (Pexels CDN sandbox-blocked at this build · URL wiring verified correct).
2. **R-LF2-1 founder portrait** rendered LinkedIn-collapse audit (same sandbox issue).
3. **Naskh AR h1 swap** (LF-2-scoped) → workflow C multilingual rollout.
4. **5 locales × 5 page kinds + 5 × 4 case-detail = 45+ routes** → workflow C.
5. **Tier flip draft → published_live** with 7 explicit-literal test bumps `24 → 25` and `"24+" → "25+"` → workflow D + explicit user handshake (R-SOL-8 / CS-BLOCK-13 / D-102 cadence).

## Causa IT draft is ready for human visual review

Open the dev server URL to walk the build:

```
http://127.0.0.1:8052/templates/business/causa-legale/preview/?preview=1
```

Workflow C (multilingual) and Workflow D (public flip) remain **held** until explicit user handshake — same shape as the Solaria + Continua + Cornice flips.
