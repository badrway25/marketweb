# Causa · A.6 review-lock · executive summary

**Verdict**: **PARTIAL — copy/chrome/typography/palette LOCKED · imagery HELD**
**Gatekeeper**: HOLD · NOT YET LOCKED FOR USER VISUAL HANDSHAKE
**Aggregate (numeric panels)**: 4.51 / 5
**Date**: 2026-05-04 · Phase X.6 Step 5 · workflow A.6 IT review-lock
**Branch**: `phase-x6-causa-a6-it-review-lock`

---

## What the A.6 walk found

A.6 is the human-handshake-prep review-lock pass. The IT draft entered A.6
as A.5-claimed-GREEN. The walk surfaced **one critical Class III review-
blocker** that A.5's process did not catch:

**F1 · 10 of the curator-pack's Pexels URLs are fabricated — they resolve to
inappropriate / off-brand content.** A.6 directly navigated each URL in the
browser sandbox + screenshotted the rendered photo + compared against the
curator's caption. 8 / 8 sampled URLs returned content categorically
different from what the curator pack claimed:

- Hero (slot 0): rendered as group portrait of casual youths in sepia
  setting — curator captioned as "empty courtroom interior · zero people"
- Founder portrait (slot 2): rendered as a bowl of food in a terracotta
  dish — curator captioned as "senior man 60s in chambers with codex"
- Magazine card hero (extra 7): rendered as half-nude male studio model —
  curator captioned as "Italian high-court exterior detail"
- Feature (slot 1): rendered as residential bay-window living-room — curator
  captioned as "open Italian law codex on chambers desk"
- Hero backups 11-14 (the 4 documented escape-hatch fallbacks): all 4
  unusable — palm tree · 404 · night cityscape · 3-person warm-mahogany
  consultation

A.5's report classified this as "sandbox CDN issue" and predicted that "any
browser with normal Pexels reachability will load the photos." A.6
**refutes** this classification. The URLs DO load — they just load the
WRONG content. The defect is at the curator layer (Pexels IDs are
curator-hallucinated assignments), not at the CDN layer.

## What was fixed at A.6

**Conservative narrow mitigation** (A.6 is a review-lock, not a re-curate):

- Replaced the 10 photo URL constants in
  `apps/catalog/template_content_causa.py` with a single
  `_IMAGERY_HOLD_PLACEHOLDER` base64-encoded SVG data URL that renders as a
  bottle-green / bone / obsidian gradient with an italic "imagery hold ·
  A.5b re-curate pending" label.
- Added a ~30-line comment block at the imagery section documenting the
  finding and the mitigation rationale.

**Zero edits to**: apps/editor · apps/projects · apps/commerce ·
preview_imagery.py · template_dna.py · views.py · migrations · LF-* layout
files · corporate-suite chrome · other archetype content modules ·
TEMPLATE_REGISTRY.json · the curator pack itself.

## What got verified live

- **9/9 staff-preview routes 200** (5 pages + 4 case-detail).
- **4/4 anonymous draft-gate 404** + catalog absent + counter "24+" preserved.
- **5/5 frozen siblings 200 anon · byte-equivalent to A.5** (Pragma + Cornice
  + Fiscus + Solaria + Continua all 0/5 regression). Cornice control capture
  confirms Bologna golden-hour portico + Cormorant + rust intact.
- **24/24 DOM probes** confirm bottle-green palette + GT Sectra+Manrope
  typography + LF-2 family signal (cs-lf-lf-2 · cs-nav--lf2 · cs-cta-cream ·
  cs-cases-magazine · whistleblowing footer column).
- **Voice anchor `evidenza`** verbatim recurrence on hero h1 + cs-cta-closer-
  cream h2 (2 surfaces · per AC-15) preserved through imagery hold.
- **12 ems on home** all distinct forensic-publication words including the
  triple-resonance trilogy `incardinare/incardina/incardinata`.
- **Navbar pill** "APRI UN PARERE PRELIMINARE" verified live on all 9 pages
  including 4 case-detail (zero Cornice `Apri un fascicolo` leak).
- **Per-Pexels-URL direct probe** disambiguated A.5's misclassification ·
  reclassified Issue 3 from "sandbox-only · NOT FIXED" to "REAL PRODUCT
  DEFECT · curator pack must be re-curated at A.5b".
- **20 captures** including 8 pre-fix Pexels-direct evidence + 7 post-fix
  rendering verification + 3 responsive (1440/880/375) + 1 Cornice control +
  1 case-detail.

## Distinctness verdict

- vs Pragma (LF-1): **5/5**
- vs Cornice (LF-2 first occupant): **12/13** (only the hero subject axis on hold)
- vs Fiscus (LF-3): **6/6**
- vs Solaria (LF-4): **7/7**
- vs Continua (LF-5 · cool-on-cool): **10/11** (R-CAU-1 + R-CAU-2 cleared at copy + palette layers · photographic layer held)

Aggregate: **NO COLLAPSE**. The placeholder pattern introduces zero new
collision risks — it's hex-distinct from Continua's pine, palette-distinct
from Cornice's graphite/rust, layout-distinct from Pragma/Fiscus/Solaria.

## Frozen sibling regression verdict

**0 / 5 regression.** All 5 live siblings byte-equivalent vs A.5. Public
catalog count holds at 24 published_live. Trust counter "24+" unchanged.

## Test status

```
$ python manage.py test
Ran 546 tests in 170.425s · OK

$ python manage.py test apps.catalog
Ran 171 tests in 3.156s · OK
```

**546 / 546 + 171 / 171 OK.** Zero new failures.

## Held + recommended next action

**Workflow C (multilingual) HELD.** Cannot proceed until A.5b imagery
re-curate completes. Translating placeholder content would lock the
imagery-hold pattern across 5 locales.

**Workflow D (public flip) HELD.** Currently locked behind workflow C.

**Recommended next action**: orchestrator authorises **Phase X.6 Step 5b**
imagery re-curate workstream:

1. Re-curator does fresh Pexels search for the 6 primary slots + 4
   magazine-grid extras with **mandatory live-URL verification** at curator
   commit time (no LLM-fabricated IDs).
2. Re-curator updates `business-litigation.md` + `preview_imagery.py` +
   `template_content_causa.py` with verified URLs (revert the A.6
   placeholder mitigation).
3. **A.6b rapid review-lock** re-walks the priority surfaces (hero ·
   founder · case-cards) live to confirm the empty-courtroom + chambers-
   Cassazionista + high-court-architectural register reads as intended.
4. On A.6b GREEN: orchestrator re-issues user-handshake invitation.

## Causa IT draft is NOT YET ready for visual handshake

Open the dev server URL to walk the build:

```
http://127.0.0.1:8052/templates/business/causa-legale/preview/?preview=1
```

The page is reviewable for everything-except-imagery. Photographic surfaces
render as a deliberate hold pattern. The visual handshake itself requires
real photos — A.5b is the prerequisite.
