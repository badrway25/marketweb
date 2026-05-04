# Causa · A.6 IT review-lock · build-report

**Phase**: X.6 Step 5 · A.6 review-lock
**Template**: causa-legale (LF-2 · 6th corporate-suite sibling)
**Date**: 2026-05-03
**Verdict**: 4.2 / 5 · build is HEALTHY but imagery hold caps the score

---

## §1 · What the A.6 build pass shipped

A.6 is a review-lock pass, not a re-build. The deliverable is:

- **1 source file modified**: `apps/catalog/template_content_causa.py` —
  10 Pexels URL constants replaced with a single `_IMAGERY_HOLD_PLACEHOLDER`
  base64-encoded SVG data URL. ~30 lines of new comment block documenting
  the F1 finding and the conservative-narrow mitigation rationale. Net
  diff: ~50 lines added (comment + 1 placeholder constant + 10 reassignments)
  / ~32 lines removed (the 10 broken URL constants).

- **Zero edits to**:
  - apps/editor / apps/projects / apps/commerce
  - apps/catalog/preview_imagery.py (business-legale pool stays at curator URLs · A.5b will re-curate)
  - apps/catalog/template_dna.py · template_content.py · views.py · migrations
  - LF-1 / LF-2 / LF-3 / LF-4 / LF-5 layout files
  - corporate-suite chrome (_base.html)
  - Any other archetype's template_content_*.py
  - TEMPLATE_REGISTRY.json
  - docs/content-factory/imagery/packs/business-litigation.md (curator pack to be replaced at A.5b)

- **10 reports + 20 captures created** under `factory/reports/causa/` ·
  `factory/reports/browser-verification/causa-a6-it-review-lock/` ·
  `factory/reports/scorecard/causa-a6-it-review-lock/`.

---

## §2 · Build score by axis

| Axis | Score | Notes |
|---|---|---|
| Layout integrity (LF-2 family signal · 13 signatures) | 5/5 | All 13 LF-2 signatures intact post-fix · cs-lf-lf-2 + cs-nav--lf2 + split-wordmark + filled CTA pill + stacked-editorial hero + KPI in overlay + drop-cap narrative + 3 pull-quotes + side-rail + 12-cell sectors + single-portrait L6 + magazine grid 3+1 L7 + cream CTA closer + 4-col-with-whistleblowing footer all DOM-verified |
| Copy fidelity (voice anchor + em audit + vocabulary density) | 5/5 | Voice anchor verbatim 2/2 surfaces · 12/12 em words distinct + forensic-publication-register · 21 `evidenza` + 21 `massima` + 11 `patrocinio` + 9 `incardinata` body hits |
| Palette + typography (DOM probes) | 5/5 | --primary `#14342B` · --secondary `#F0EBE0` · --accent `#0B0A0E` · --heading `'GT Sectra', Georgia, ...` · --body `'Manrope', system-ui, ...` all DOM-verified |
| Navbar pill consistency (9 pages) | 5/5 | "APRI UN PARERE PRELIMINARE" verified live on all 9 pages including 4 case-detail · zero Cornice `Apri un fascicolo` leak |
| Imagery (10 photographic surfaces) | 0/5 | All 10 Pexels URLs verified live to render WRONG content · A.6 mitigation substitutes with placeholder · imagery axis HELD pending A.5b re-curate · this single axis caps the build aggregate |
| Frozen sibling regression (5 siblings) | 5/5 | Pragma + Cornice + Fiscus + Solaria + Continua all 200 anonymous + byte-equivalent body lengths vs A.5 · zero content edits to any sibling module |
| Test suite (546 tests) | 5/5 | 546/546 OK · 171/171 catalog OK · zero new failures |
| Draft preview path | 5/5 | Anonymous 4/4 404 · staff 9/9 200 · DB tier='draft' · counter '24+' preserved |

**Aggregate: (5+5+5+5+0+5+5+5)/8 = 35/40 = 4.38 / 5.0**.

The imagery axis (0/5) is the single drag on the score. Every other axis
clears at the maximum (5/5). The build is structurally HEALTHY — the
defect is concentrated in one classification (Class III · template-local
imagery) and is mitigated to a state where the user can visually review
everything-except-imagery.

---

## §3 · Build-side observations (non-blocking)

- **Comment-block quality**. The new ~30-line comment block at the imagery
  section of `template_content_causa.py` documents the A.6 finding inline
  (rather than deferring all explanation to the report). This pattern
  matches the Cornice precedent's F2 cleanup comment. Future readers
  inspecting the file will understand why the placeholder is there without
  having to cross-reference the report.

- **Base64 vs ?utf8 SVG**. An earlier A.6 mid-walk attempt used
  `data:image/svg+xml;utf8,<svg ...>` but Django's HTML auto-escape
  converted `<` → `&lt;` and `'` → `&#x27;` inside the CSS `background-image:
  url('...')` declaration in `lf2/styles.html`, mangling the SVG. The
  base64 form (`data:image/svg+xml;base64,...`) sidesteps the escape
  entirely because the body contains zero `<`/`>`/`'`/`"` characters.
  This is the canonical pattern for inline SVG data URLs inside Django
  templates and should be the standard approach if any future A.5b uses
  inline SVG.

- **Migration footprint**. Zero new migrations. The A.6 fix is content-only
  and does not touch any model field. The pre-existing
  `0008_causa_layout_family.py` migration (A.5) continues to backfill
  `WebTemplate.layout_family='LF-2'` for `causa-legale` correctly.

---

## §4 · What the user sees post-A.6 fix

1. Hero band: bottle-green gradient placeholder with "imagery hold · A.5b
   re-curate pending" italic label centred at ~y=455. KPI tuple `28 / 14 /
   31` with labels `Sentenze citate / Voci in massimario / Anni di
   patrocinio` legible in bottom-left credit-overlay frame.
2. Below-fold 8/4 split: voice anchor h1 in GT Sectra (italic em on
   `evidenza` in obsidian) · sub line · 2 buttons (filled bottle-green
   primary + ghost secondary) on the left · italic side-quote with em on
   `incardina` on the right.
3. Narrative essay: drop-cap `L` in obsidian-tinted GT Sectra 84px on
   bone · 4 paragraphs · 3 italic pull-quotes interspersed (em on
   `giurisdizione` · `massima` · `sostenuta`) · sticky 4-link side-rail.
4. 12-cell sectors-ribbon: italic Manrope 14px uppercase · middot-
   separated · counter footnote with em on `2008`.
5. Leadership-single section: bottle-green placeholder portrait (4:5 aspect)
   with figcaption "Lo studio · chambers di via Borgonuovo · 2024" · h2
   "Lorenzo *Marchetti*" · italic role · 2-paragraph bio · 4 credentials
   list · secondary CTA "Studio · biografia estesa".
6. Magazine grid 3+1: 1 large hero card (bottle-green placeholder · "01"
   eyebrow · italic em on `incardinata` · meta pill `Cassazione SS.UU. ·
   grado di legittimità · 2024 · ricorrente`) + 3 small cards stacked.
7. CTA closer cream: hairline bordered cream band · centred h2 voice anchor
   verbatim recurrence · filled bottle-green pill "Apri un parere
   preliminare" · closing line + sub line.
8. 4-col footer with whistleblowing column: brand + pages + contatti +
   segnalazioni (D.lgs. 24/2023).

The page reads as a coherent IT-only Causa draft with imagery on hold.
Copy / chrome / typography / palette / voice anchor / KPI tuple all
review-lockable.

---

## §5 · Build verdict

**Build is HEALTHY · imagery HELD.** The conservative-narrow mitigation
preserves all reviewable surfaces and removes the inappropriate Pexels
content from the live render. The A.5b re-curate workstream is the
prerequisite for promoting Causa to LOCKED-FOR-USER-HANDSHAKE.

Score: **4.38 / 5**.
