---
report_type: build
template_slug: fiscus-commercialista
archetype: corporate-suite
agent: template-builder
role: primary
run_timestamp: 20260426T0757Z
branch: phase-x4a-corporate-factory-hardening-followup
baseline_tip: e210b6b (X.4a step2E-P1B · RTL AR re-verification)
post_fix_tip: HEAD + 1 archetype-skin edit (mp-back focus-visible whitelist)
inputs:
  - factory/reports/hardening/step2-readiness-reassessment.md
  - factory/reports/hardening/step2-execution-round2.md
  - factory/standards/corporate-suite-design-standard.md §4 (palette · CS-PAL-01..06)
  - factory/standards/corporate-suite-imagery-standard.md §2 (pool shape · CS-IMG-POOL-01)
  - factory/standards/corporate-suite-blocking-rules.md §3 (CS-BLOCK-01 · CS-BLOCK-07)
outputs:
  - factory/reports/scorecard/fiscus-pipeline-round1/build-report.md
  - factory/reports/hardening/step2-ci/test-run-20260426T0757Z.txt
status_tag: DRAFT-RETROACTIVE
---

# Build report · Fiscus — Studio Tributario · AP8 first-run

## 1 · Summary

Fiscus already shipped at `tier: published_live` in Session 80 (Phase X.4 Wave 2 Pilot #1, 2026-04-20) — the present run is the **AP8 first end-to-end pipeline application** required by plan §6.4 (T-P1-3) and is therefore retro-built against the existing baseline rather than wiring a fresh template. Builder duties are reduced to: (a) re-running the deterministic CI floor on the post-fix tip, (b) re-asserting the palette + Pexels invariants against the already-wired pools, (c) acknowledging the Pragma legacy grandfather W001 surfaces silently per design.

## 2 · Inputs consumed

- `apps/catalog/preview_imagery.py` — pool `business-fiscal` already wired (Session 80) with 6 Pexels URLs in CS-IMG-POOL-01 order.
- `apps/catalog/template_dna.py` — Fiscus DNA row already present with `palette = {primary: #1F2937, secondary: #B58F4A, accent: #1C3D5A}`.
- `apps/catalog/management/commands/seed_templates.py` — Fiscus seed entry already present at `dna_phase: x4.1` / `session_closed: 80`.
- `TEMPLATE_REGISTRY.json` — Fiscus already at `tier: published_live`.
- Five content modules already at `apps/catalog/template_content_fiscus{,_en,_fr,_es,_ar}.py` (all five present, voice anchors verified at §4 below).
- The Round 2 / Round 3 / Round 4 CS-BLOCK-17 (extended) palette-safety patches landed on `_base.html` + `case_study_detail.html` (commit `709b54c` initial set + `edcdbed` LTR multi-locale set).
- One small archetype-level skin edit applied in this round: `_base.html` adds `.mp-bar .mp-back:focus-visible` to the gold-accent ring whitelist, closing the Round 4 P2 deviation that the marketplace back-link landed on browser-default outline (BRWS-CONTRAST-04 / E1 alignment).

## 3 · Findings

### 3.1 · Blocking

None. Every CI gate green; no palette / imagery / registry override surfaces an Error.

### 3.2 · Required

None. The Pragma `business-corporate` grandfather surfaces as `corporate_suite.W001` Warning per design — this is not a `[REQUIRED]` failure, it is the gatekeeper-discipline contract documented in plan §5 / R-SOL-10 and surfaced explicitly in the gatekeeper scorecard in this round.

### 3.3 · Strong / Guideline notes

- The palette self-check uses the seeded `--paper` token `#FAF8F4` (warm cream) — slightly warmer than Pragma's `#F7F3EC` because Fiscus's commercialista voice asks for a warm-neutral cream surface. Both clear `CS-PAL-01` (`L*(primary) ≤ 40` AND `ΔL*(primary, paper) ≥ 40`) by margin.
- The `mp-back` focus-visible whitelist edit is one line in `_base.html`; it preserves the existing `outline: 2px solid var(--accent); outline-offset: 4px;` rule and adds the marketplace back-link to the same selector group. Static contract: every interactive `:focus-visible` paints the gold/accent ring, never the browser-default blue (E1).

## 4 · Measurements

### 4.1 · Palette self-check (CS-PAL-01)

```
Fiscus
  primary   #1F2937 → sRGB (31, 41, 55)   → CIELAB L* ≈ 16.8
  paper     #FAF8F4 → sRGB (250, 248, 244) → CIELAB L* ≈ 97.6
  ΔL* (primary → paper)                    ≈ 80.8   ✓ ≥ 40
  primary L*                               ≈ 16.8   ✓ ≤ 40
  verdict: CS-PAL-01 PASS

Pragma (sibling · in scope of build-time gate, not in scope of THIS scorecard)
  primary   #1E293B → CIELAB L* ≈ 17.2     ✓ ≤ 40
  paper     #F7F3EC → CIELAB L* ≈ 95.1
  ΔL* ≈ 77.9                                 ✓ ≥ 40
  verdict: CS-PAL-01 PASS
```

The build-time `corporate_suite.E001` palette safety check (`apps/catalog/checks.py`) re-asserts both rows on every `manage.py check`. Solaria's bug palette `#F7F3EC` (cream-on-cream) is rejected by the same check — the static test `CorporateSuiteThemeSafetyTests.test_primary_safety_fails_on_solaria_bug_palette` pins the red path.

### 4.2 · CI floor (post-fix tip)

```
$ python manage.py check catalog
System check identified some issues:

WARNINGS:
business-corporate: (corporate_suite.W001) corporate-suite imagery pool 'business-corporate'
  is grandfathered under LEGACY_EXEMPT_KEYS and ships 6 non-Pexels url(s) pending AP3
  retro-curation. The archetype accepts this; the gatekeeper must cite it explicitly
  (O7 precondition).

System check identified 1 issue (0 silenced).

$ python manage.py test apps.catalog -v 2
…
Ran 171 tests in 2.218s

OK
```

Full transcript: `factory/reports/hardening/step2-ci/test-run-20260426T0757Z.txt` (171/171 OK · 2.218 s).

### 4.3 · Pexels-only grep (CS-BLOCK-07 layer-2 enforcement)

```
$ grep -nE 'unsplash|shutterstock|getty|adobestock|istockphoto|pixabay|freepik' \
    apps/catalog/preview_imagery.py | grep -v "business-corporate"
(returns 0 matches for the Fiscus business-fiscal pool — Pexels-only)
```

The legacy Pragma `business-corporate` block returns 6 `images.unsplash.com` matches by design (the LEGACY_EXEMPT_KEYS grandfather). The Pexels-only assertion is scoped to non-exempt pools and Fiscus's pool is clean.

### 4.4 · Registry tier check

```
$ grep -n 'fiscus-commercialista' TEMPLATE_REGISTRY.json
127:      "slug": "fiscus-commercialista",
…
147:      "tier": "published_live",
```

Fiscus is **already at `published_live`** from Session 80 (2026-04-20). The release-gatekeeper's Commit B (draft → published_live flip) is therefore a **no-op** in this round — the slug already shipped. The gatekeeper scorecard records this explicitly (no live registry edit issued).

### 4.5 · Voice anchor verbatim across 5 locales (BRWS-FEEL-05 / O11)

```
template_content_fiscus.py:98       L'adempimento <em>corretto</em>, non la trovata.
template_content_fiscus_en.py:78    The <em>correct</em> filing, not the clever trick.
template_content_fiscus_fr.py:74    L'application <em>correcte</em> de la norme, jamais l'artifice.
template_content_fiscus_es.py:70    El cumplimiento <em>correcto</em>, no la ocurrencia.
template_content_fiscus_ar.py:78    الامتثال <em>الصحيح</em>، لا الحيلة الضريبية.
```

Five locales, five verbatim anchors, italic `<em>` on the load-bearing word per locale. O11 NOT triggered.

### 4.6 · D-054 10-gate triangulation (CS-BLOCK-12 / O12)

`apps/catalog/template_content_fiscus.py` lines 14-39 carry the full 10-gate block triangulating Fiscus against **Pragma** (every dimension named: hero image · first-2 imagery · silhouette · section order · primary CTA · block rhythm · macro tone · imagery direction · typography · voice anchor). Pragma is Fiscus's only enrolled corporate-suite sibling at the current tip (Solaria Commit B paused). O12 NOT triggered for Fiscus.

**Caveat carried into the gatekeeper scorecard** (S3 from `step2-readiness-reassessment.md`): Pragma's docstring (`template_content_pragma.py` lines 12-32) was authored in Session 32 against **Elevate** (its archetype-era sibling at the time), not against Fiscus. Pragma has an O12 staleness vs Fiscus that T-P1-4 schedules to refresh post-T-P1-3. This is **NOT a blocker on Fiscus's scorecard** — it is a known Pragma-side staleness deliberately kept until after this AP8 first-run lands so the gatekeeper exercises current-state docstrings.

## 5 · Per-dimension scores

n/a · upstream authoring agent.

## 6 · Escalations raised

- **Pragma O12 staleness vs Fiscus** — escalated to T-P1-4 (planner-driven docstring refresh on `template_content_pragma.py` + `template_content_fiscus.py`). Lands post-T-P1-3.
- **Pragma `business-corporate` legacy Unsplash grandfather** — explicit O7 acknowledgment passed forward to the gatekeeper. The Pexels retro-pack (T-P2-1) is deferrable-past-Solaria per plan §5; this build run does not address it.

## 7 · Parallel-verification handshake

n/a · build-time agent · no live server interaction.

## 8 · Next action

Hand off to **browser-verifier** · the existing multi-round browser corpus
(`factory/reports/browser-verification/x4a-step1d/20260424T2300Z/` · `x4a-step2/20260424T2346Z/reduced-motion/` · `x4a-step2/20260425T0030Z-multi-locale-ltr/` · `x4a-step2/20260425T0125Z-multi-locale-ltr-postfix/` · `x4a-step2/20260425T0837Z-rtl-ar/` · `x4a-step2/20260425T1100Z-rtl-ar/`) is reused as the AP8 evidence base; the verifier consolidates its findings into the Round 1 pipeline scorecard at `factory/reports/scorecard/fiscus-pipeline-round1/browser-verifier.md`.

— end of build report —
