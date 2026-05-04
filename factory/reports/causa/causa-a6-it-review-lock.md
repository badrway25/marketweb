# Causa · A.6 IT Review-Lock · 6th corporate-suite sibling · 2nd LF-2 occupant

```yaml
report_type:        a6-review-lock
template_slug:      causa-legale
archetype:          corporate-suite
sub_cluster:        studio-legale-cassazionista · evidence-led litigation boutique
layout_family:      LF-2 · Editorial Spread (2nd occupant after Cornice)
phase:              X.6 · Causa · A.6 review-lock (IT-only · pre-multilingual)
date:               2026-05-03
agent:              review-lock-builder (Phase X.6 Step 5)
inputs_consumed:
  - factory/reports/causa/causa-a5-it-build.md
  - factory/reports/browser-verification/causa-a5-it-build.md
  - factory/reports/scorecard/causa-a5-it-build/*
  - factory/reports/causa/causa-planner-brief.md
  - factory/reports/causa/causa-imagery-pack.md
  - factory/reports/causa/causa-prebuild-quick-checks.md
  - factory/reports/causa/causa-distinctness-proof.md
  - factory/reports/imagery/causa-legale/pool-selection.md
  - factory/reports/imagery/causa-legale/reviewer-lgtm.md
  - factory/reports/copy/causa-legale/copy-authoring.md
  - factory/reports/copy/causa-legale/voice-anchor-lock.md
  - docs/content-factory/imagery/packs/business-litigation.md
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md
  - factory/reports/cornice/cornice-a6-it-review-lock.md (precedent shape)
  - current Causa implementation (apps/catalog/template_content_causa.py · DNA · LF-2 layout files)
  - frozen sibling state (Pragma · Cornice · Fiscus · Solaria · Continua · all live anonymous)
status_tag:         A6-REVIEW-LOCK-PARTIAL · copy/chrome/typography/palette LOCKED · imagery HELD
verdict:            NOT YET LOCKED FOR USER VISUAL HANDSHAKE — imagery hold pending A.5b re-curate
next_action:        Orchestrator authorizes a Phase X.6 Step 5b imagery re-curate
                    (real Pexels search + verify · replace 10 fabricated URLs with
                    actual courtroom/codex/chambers photos). On A.5b GREEN, an A.6b
                    rapid review-lock re-runs the priority surfaces (hero · founder
                    · case-cards) before workflow C is authorised. Workflow C
                    (multilingual EN/FR/ES/AR + AR Naskh) and workflow D (public
                    flip · tier=draft → published_live) remain explicitly HELD.
```

This file is the binding A.6 review-lock narrative for Causa. It pairs with:
- `factory/reports/browser-verification/causa-a6-it-review-lock.md` — IT live walk evidence + per-Pexels-URL verification + frozen-sibling regression check + responsive matrix (1440 / 880 / 375)
- `factory/reports/scorecard/causa-a6-it-review-lock/*.md` — 8 scorecard panels (build · style · contrast · responsive · browser · gatekeeper · scorecard + summary)

---

## §1 · A.6 framing (why this phase exists)

A.5 (Phase X.6 Step 4) closed with a build report claiming the IT draft was
GREEN review-ready · `tier=draft` · 9 routes 200 staff · 5 frozen siblings 0/5
regression · 546/546 tests · 12 captures. The orchestrator held workflow C
(multilingual) and workflow D (public flip) pending a human visual handshake on
the IT draft. A.6 is the review-lock pass that:

1. Walks the IT draft live in the browser at 1440 / 880 / 375.
2. Performs per-Pexels-URL verification on every photographic surface (the
   `causa-a5-it-build.md §3 Issue 3` flagged the Pexels CDN as
   "sandbox-only" — A.6's brief explicitly asks the reviewer to confirm or
   refute that classification).
3. Closes any review-blocking issues with the minimum surgical fix per the
   classification rule (Class I = chrome · Class II = family/sibling · Class
   III = template-local).
4. Re-walks post-fix and confirms zero frozen-sibling regression.

The A.6 walk uncovered **one critical Class III review-blocker (F1)** + **one
Class III copy-cleanup (F2)** + **two minor accessibility nudges deferred**.
F1 (the imagery breakage) is review-blocking and forces the verdict to
**NOT YET LOCKED FOR USER VISUAL HANDSHAKE** despite all other panels being
GREEN.

---

## §2 · Live walk methodology

```
server:                python manage.py runserver 8052 --noreload
URL prefix:            http://127.0.0.1:8052/
template root:         /templates/business/causa-legale/preview/
auth:                  staff user `causa_review_a6` · is_staff=True · is_superuser=True
                       (also re-authenticated existing `cornice_review` session for
                       cross-checks · both sessions hit ?preview=1 to clear the
                       D-055 staff-preview gate on tier=draft)
browser:               Playwright MCP · viewports 1440×900 (lead) · 880×900 (tablet)
                       · 375×800 (mobile)
HTTP smoke:            urllib opener + cookie-jar session for repeatable per-route
                       status assertions (anonymous + staff)
direct Pexels probe:   Playwright navigated each Pexels CDN URL (8 unique IDs
                       across 6 primary slots + 4 magazine extras + 4 backup
                       slot-0 candidates) AND saved the rendered photo to
                       captures/02..08 + 03/04/05/06 for evidence
test suite:            python manage.py test (full Django suite · 546 tests)
                       + python manage.py test apps.catalog (171 tests)
```

Walk shape — mirrors A.5 + adds a per-Pexels-URL probe layer (the A.5 build
disclosed "Pexels CDN sandbox-blocked at this build" but did not prove which
class of failure that was; A.6's job was to disambiguate):

| Layer | What was verified |
|---|---|
| Routes | 9 IT routes — home + studio + materie + contenzioso list + 4 case-detail + contatti |
| Anonymous draft-gate | 6 anon checks — 4 must-be-404 + 1 catalog must-not-list-Causa + 1 home-counter must-stay-24+ |
| Frozen siblings | 5 anon homes — Pragma · Cornice · Fiscus · Solaria · Continua (all 200 + same body length) |
| Hero photo | DOM probe `getComputedStyle(.cs-hero .photo).backgroundImage` + DIRECT navigate to Pexels CDN URL + screenshot |
| Founder portrait | DOM probe `.cs-leadership-single img` + DIRECT navigate + screenshot |
| Magazine cards | DOM probe `.cs-cases-magazine .card img` × 4 + DIRECT navigate to each Pexels URL + screenshot |
| Hero backups | DIRECT navigate to backup 11 · 12 · 13 · 14 (the planner-pre-cleared codex-spread fallback) + screenshot |
| Voice anchor | regex `Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa\.` count on rendered home (target=2) |
| Em-word audit | `<em>...</em>` extraction on rendered home (target ≥10 forensic-publication ems · all unique words except `evidenza` recurrence) |
| Navbar pill | `.cs-nav-cta-btn` innerText check on EVERY page including 4 case-detail (must read "APRI UN PARERE PRELIMINARE" — Cornice default `Apri un fascicolo` would be a fail) |
| Palette / typography | CSS custom property probes `--primary` / `--secondary` / `--accent` / `--heading` / `--body` |
| Responsive | 1440 + 880 + 375 fullpage screenshots on home (post-fix) |
| Captures | factory/reports/browser-verification/causa-a6-it-review-lock/captures/ — 20 JPEGs |

---

## §3 · Findings + fixes applied

### F1 · Imagery pack contains 10 fabricated Pexels URLs (CRITICAL · Class III · review-blocking)

**Symptom**. The A.5 build wired 10 photographic surfaces (6 primary slots + 4
magazine-grid extras) to Pexels URLs taken from
`docs/content-factory/imagery/packs/business-litigation.md` and
`apps/catalog/preview_imagery.py business-legale`. The A.5 build report §3
Issue 3 noted "Pexels CDN sandbox-blocked at this build" and disclosed a
mitigation: 5 captures used a `bottle-green-gradient` placeholder via
JavaScript while the DOM wiring "verified correct." A.6 was explicitly
asked by the brief to "distinguish clearly between real product issue and
tooling issue."

A.6 navigated each Pexels CDN URL directly in the browser and screenshotted
the actual rendered content. Every URL was checked against the curator's
caption and the planner-brief subject-class binding rules. The result is
**CATEGORICALLY a real product issue · NOT a sandbox-only tooling issue**.

| Slot | Pexels ID | Curator caption (verbatim from `business-litigation.md`) | Actual rendered content (A.6 direct verify) | Capture |
|---|---|---|---|---|
| 0 hero | 17109985 | "Empty courtroom interior · vertical timber wainscoting + bone-painted walls · daylight through high clerestory windows · low-luminance judicial bench in mid-ground · zero people · zero documents-on-desk · cool register" | **Group portrait of casual youths in sepia/dark setting · multiple people present · "JEAN YLLANA" sign visible behind · Chicago Bulls jersey on one subject · zero courtroom · zero timber wainscoting** | `02-hero-pexels-direct.jpeg` |
| 1 feature | 6077368 | "Open Italian law codex (codice-shaped volume) lying on a wooden chambers table · single tome · faint marginal annotations" | **Residential bay-window living-room · cream couches with burgundy throw cushion · panoramic city view through windows · zero codex · zero chambers** | `09-feature-6077368.jpeg` |
| 2 founder portrait | 8101948 | "Senior man (60s · greying hair · horn-rimmed eyeglasses · charcoal-grey three-piece suit · pen in hand) seated 3/4 toward camera at a chambers desk · open codice in mid-ground" | **Bowl of food (Mexican-style ceviche / shredded mixed dish) in a terracotta dish on a light wooden surface · zero person · zero chambers · zero codex** | `07-portrait-8101948.jpeg` |
| 7 case-card hero | 9489162 | "Italian high-court exterior detail · classical pediment with Latin inscription · cool overcast daylight · vertical column visible at left edge · zero people · architectural detail at mid-distance" | **Half-nude male model seated on white fabric backdrop · studio portrait with pop-culture chain accessory · zero courthouse · zero architectural** | `08-case-9489162.jpeg` |
| 11 hero backup #1 | 15796091 | "Empty European court chamber · light timber-and-bone interior · narrow side-aisle visible at right · pendant lights off · daylight from clerestory · zero people" | **Single palm tree silhouetted against grey-blue sky · low-angle exterior shot · zero court · zero interior** | `03-backup11-15796091.jpeg` |
| 12 hero backup #2 | 8112167 | "Wide chamber interior with tall narrow windows · deep DoF on empty wood-panelled gallery · daylight cool register · zero people" | **HTTP 404 · the URL does not resolve · the photo does not exist on Pexels** | `04-backup12-8112167.jpeg` |
| 13 hero backup #3 | 4427451 | "Empty courtroom interior with vertical timber columns · raised judicial bench in mid-ground · cool side-light · zero people · zero documents" | **Night cityscape · church/castle silhouette + medieval town wall + park bench in foreground · cool blue twilight · zero courtroom** | `05-backup13-4427451.jpeg` |
| 14 hero backup #4 (PRE-CLEARED CODEX-SPREAD FALLBACK per planner-brief §4) | 7841457 | "Codex-spread on chambers desk wide-shot · object-dominant composition · cool light · zero people · the planner-pre-cleared backup hero subject" | **Three-person consultation in warm wood-panelled office · burgundy leather chairs · mahogany desk · framed paintings on patterned wallpaper walls · zero codex-spread · multiple people · warm-mahogany dominant (Continua R-CAU-2 collision)** | `06-backup14-7841457.jpeg` |

**Why this blocks review.** A user reviewing the IT pages would, at the hero
scroll, see a sepia-toned street-portrait of casual youths instead of an
empty courtroom. At the founder scroll, they would see a bowl of food
instead of a senior Cassazionista in chambers. At the magazine-grid hero
card, they would see a half-nude male model instead of a high-court
architectural detail. **The page categorically fails the priority surfaces
1 + 2 + 4 of the A.6 brief**:

> 1. Hero must read courtroom/interior-litigation, not library/editorial
> 2. Founder portrait must read chambers/environmental, not LinkedIn headshot
> 4. (case-card visual register must read public-record-evidence, not stock)

It also fails the planner-brief §4 binding triple (zero-people +
interior-architectural + cool-timber-and-bone) on slot 0 with maximum
margin (multiple people + casual-street + sepia-warm). And it fails the
copy-authoring §17 anti-collapse contract on slot 2 (the founder is
gendered male `Lorenzo Marchetti` with masculine bio · the photo is a bowl
of food · the gender / subject-class / room-prop axes ALL collapse to a
single category-mismatch error).

**Why A.5 missed it.** The A.5 builder described its Issue 3 as "Pexels
CDN sandbox-blocked at this build" and inferred wiring-correctness from a
DOM probe (`background-image` URL contains `pexels-photo-17109985`). The DOM
probe IS correct — the URL IS wired correctly — but the A.5 builder did
NOT navigate to the URL itself in a browser and inspect the rendered photo.
The A.5 builder treated "DNS failure on a subset of CDN URLs" as the most
likely class of failure when the actual failure was "the curator pack
contains hallucinated Pexels ID assignments." A.6 closed this gap by
directly visiting each URL in the browser sandbox AND confirming that the
SAME URLs that A.5 reported as "sandbox DNS-blocked" actually return real
photo content (just NOT the content the curator captioned).

**Root cause inference**. The `business-litigation.md` curator pack reads
as if it were authored by an LLM that selected plausible-sounding Pexels
photo IDs from its pretraining distribution without ever fetching them
from Pexels. This pattern matches the A.3 imagery curator's known LLM-driven
authoring pipeline. Every Pexels ID in the pack appears curator-hallucinated:
8/8 sampled IDs (6 primary + 4 backups + 1 magazine-grid hero · with one
URL returning HTTP 404 entirely) returned content categorically different
from the captioned subject. The grep-clean result reported in pool-selection
.md §6 is technically true (the IDs don't appear in any other pack) but
that's because the IDs were never real-Pexels assignments — they were
fabricated tokens that happen to be unique by virtue of being made up.

**Class**. **Class III · template-local**. The defect lives entirely inside
Causa's content module (the photo URL constants at the top of
`apps/catalog/template_content_causa.py`) plus the static curator pack
(`docs/content-factory/imagery/packs/business-litigation.md`). It does NOT
touch chrome (Class I), does NOT touch the LF-2 family (Class II), and
does NOT affect any other sibling.

**Conservative narrow A.6 mitigation (applied · NOT a re-curate)**. The
A.6 budget does NOT cover a fresh imagery curation (that's A.3's job and
properly belongs to a Phase X.6 Step 5b workstream). The most conservative
and most honest A.6 action is to:

1. **Document the breakage with full per-URL evidence** (this section + the
   browser-verification report + the 8 Pexels-direct screenshots).
2. **Substitute the 10 photo URLs with a single inline SVG data URL
   placeholder** that renders as a bottle-green / bone / obsidian gradient
   with a small "imagery hold · A.5b re-curate pending" italic label. This:
   - Removes the inappropriate / off-brand imagery from the staff-preview
     surface (the page is no longer rendering content that would be a
     reputational issue if seen).
   - Preserves the LF-2 layout shape (hero box · portrait frame · 4
     magazine cards · ambient backdrops all keep their geometry).
   - Preserves all other reviewable layers (copy · KPI tuple · voice
     anchor · navbar pill · footer chrome · responsive · palette ·
     typography · narrative essay · sectors-ribbon · pull-quotes · drop-
     cap · CTA closer · whistleblowing footer column).
   - Uses the locked palette tokens (`#14342B` primary · `#F0EBE0`
     secondary · `#0B0A0E` accent) so the placeholder reads as a
     deliberate hold pattern, not as a broken render.
   - Is base64-encoded so Django's HTML auto-escape does not mangle the
     SVG body when the data URL appears inside CSS `background-image:
     url('...')`. (An earlier `?utf8` variant was attempted at A.6 mid-walk
     and failed because Django converted the `<svg>` markup to `&lt;svg&gt;`
     — the base64 form sidesteps the escape entirely.)
3. **Mark the IT review-lock as PARTIAL** — copy/chrome/typography/palette
   are LOCKED but imagery is HELD pending A.5b re-curate.
4. **Recommend that workflow C does NOT proceed** until A.5b re-curate is
   complete + A.6b rapid re-review confirms the priority surfaces.

**Files changed by this fix**:

- `apps/catalog/template_content_causa.py` — replaced the 10 Pexels URL
  constants (`_HERO_COURTROOM_INTERIOR` + `_FEATURE_OPEN_CODEX` +
  `_PORTRAIT_FOUNDER` + `_PORTRAIT_ASSOCIATA` + `_DETAIL_CODEX_PAGE` +
  `_AMBIENT_CODEX_SHELVES` + 4 `_CASE_*` magazine-grid extras) with a
  single `_IMAGERY_HOLD_PLACEHOLDER` base64-encoded SVG data URL constant,
  plus a ~30-line comment block at the top of the imagery-constants
  section documenting the A.6 finding · the planner-brief §4 escape-hatch
  invocation · the conservative-narrow-mitigation rationale · the things
  this fix deliberately does NOT touch.

**Files deliberately left untouched at A.6**:

- `apps/catalog/preview_imagery.py` — the `business-legale` pool stays at
  the curator URLs (these URLs only feed the marketplace preview-tile
  composition; Causa is `tier=draft` so the catalog does not surface them
  publicly; A.5b will re-curate this pool with verified URLs).
- `apps/catalog/template_dna.py` — the imagery_key indirection stays
  (`imagery_key=business-legale`).
- `apps/catalog/template_content.py` — registry stays.
- `docs/content-factory/imagery/packs/business-litigation.md` — the curator
  pack stays (A.5b will produce a replacement pack with real Pexels URLs +
  the correct cross-cluster grep verification).
- `apps/editor/`, `apps/projects/`, `apps/commerce/` — zero edits (per scope
  rules).
- LF-1 / LF-3 / LF-4 / LF-5 layout files — zero edits.
- Cornice's content module / DNA / chrome / styles — zero edits (frozen
  sibling).
- Pragma / Fiscus / Solaria / Continua content modules — zero edits (frozen
  siblings).
- `TEMPLATE_REGISTRY.json` — zero edits (`tier=draft` preserved).
- The 4 case-detail post entries inside `template_content_causa.py` — only
  the photo URL constants were touched; all body copy / sections / KPI
  tuples / lead_partner / team / next_label fields unchanged.

**Verification post-fix**. Re-walked the home + studio + contenzioso list
+ case-detail + contatti at 1440 / 880 / 375. Captures
`13-home-1440-postfix-fullpage.jpeg` + `14-home-1440-postfix-revealed-
fullpage.jpeg` + `15-studio-1440-fullpage.jpeg` + `16-contenzioso-1440-
fullpage.jpeg` + `17-case-ssuu-1440-fullpage.jpeg` + `18-home-880-fullpage
.jpeg` + `19-home-375-fullpage.jpeg` show the placeholder renders cleanly
as a bottle-green tile with the "imagery hold · A.5b re-curate pending"
italic label centred. KPI tuple (28 / 14 / 31) stays AAA-legible above
the placeholder. The hero h1 voice anchor reads "Ogni sentenza è un'
*evidenza* incardinata, non un'opinione difesa." in GT Sectra (italic
em on `evidenza`) on bone paper. The narrative essay drop-cap renders
in obsidian-tinted serif. The 12-cell sectors-ribbon renders. The
leadership-single section renders the founder name + role + bio + 4
credentials with the placeholder portrait. The magazine grid renders 1
hero card + 3 small cards each with placeholder thumbnails. The CTA
closer cream renders the voice anchor verbatim recurrence. The 4-col
footer with whistleblowing column renders. Navbar pill on every inner
page reads "APRI UN PARERE PRELIMINARE". 9/9 routes 200 staff. 6/6 anon
checks pass. 5/5 frozen siblings 0/5 regression. PASS-FOR-IMAGERY-HOLD.

### F2 · Founder portrait `<img>` alt text reads as bare name (Class III · accessibility · low priority)

**Symptom**. The leadership-single block renders
`<img src="..." alt="{{ page_data.leadership_heading|striptags }}">` and the
heading is `Lorenzo <em>Marchetti</em>`, so the alt resolves to literal
`Lorenzo Marchetti`. The planner-brief §5 + imagery-pack §1 binding triple
called for an alt text that conveys the chambers backdrop (the room is
half the subject); A.5 did not add a `leadership_portrait_alt` field, so
the alt fell back to the heading striptags.

**Why it surfaces only at A.6**. A.5's DOM probes verified the leadership
img URL but did not screen-reader-walk the alt text. A.6's accessibility
panel flagged it as a CS-IMG-COH-04-class concern (the alt text on
load-bearing portrait surfaces should describe the environmental
composition, not just name the founder).

**Why this is NOT promoted to fix at A.6**. The fix would require either:
(a) adding a new `leadership_portrait_alt` field to the content module
+ updating `lf2/content.html` to read it (touches the LF-2 family layout
file = Class I or II depending on framing), or (b) renaming the founder's
heading to remove the em wrap (changes display semantics). Neither
is a narrow A.6 fix — they are A.5 builder territory or A.5b re-curate
territory. The placeholder portrait at A.6 has alt="Lorenzo Marchetti"
which is functionally accessible but less descriptive than the planner-
brief §5 ideal. Held for A.5b to ship the canonical alt text alongside
the real portrait URL.

**Class**. **Class III · template-local accessibility nudge**. Deferred to
A.5b for combined imagery+alt fix.

### F3 · Hero credit-overlay tuple has no separator between text + strong (Class III · cosmetic · deferred)

**Symptom**. The hero `.credit-line` template renders
`{{ page_data.hero_image_credit_left.0 }}<strong>{{ ...credit_left.1 }}</strong>`
which produces `Aula di tribunale · interno · 2024Foro di Milano` with no
space/separator between the two clauses. Visually the strong applies a
weight change so the eye can parse it but a literal space or middot would
be more conventional.

**Why this is NOT promoted to fix at A.6**. The same bug exists on Cornice
(the lf2/content.html layout file is family-shared), so the fix would touch
the LF-2 family file = Class II. Held for cluster-level follow-up if the
orchestrator wants to consolidate.

**Class**. **Class II · LF-2 family shared file**. Out of A.6 scope.

### F4 · A.5 build report claim re-classified

The A.5 build report §3 Issue 3 classified the Pexels failures as
"NOT FIXED · sandbox-only" with a "Pexels CDN sandbox-blocked at this
build" framing and predicted that "any browser with normal Pexels
reachability will load the photos." A.6 directly verified this claim and
**refutes it**:

| A.5 claim | A.6 verification | A.6 reclassification |
|---|---|---|
| "intermittent sandbox network condition" | A.6 directly fetched 8 Pexels IDs in the browser. ALL 8 returned 200 (one with content · seven with wrong-subject content · one URL itself returning 404) — there is NO sandbox network problem. | **Reclassified: REAL PRODUCT DEFECT · curator-hallucinated Pexels IDs · imagery pack must be re-curated.** |
| "the URL wiring is correct" | URL wiring IS correct (the strings are what the build wired in). The strings themselves point to wrong/inappropriate content. | Wiring-vs-content distinction acknowledged; the defect is at the curator layer, not the wiring layer. |
| "the curator-pre-cleared escape hatch is to substitute hero from backups 11-13 (or fallback 14)" | A.6 directly fetched all 4 backups. Backups 11=palm tree · 12=404 · 13=night cityscape · 14=3-person warm consultation. None are usable. | The escape hatch is unavailable; A.5b must re-curate from scratch. |
| "in the dev-server context any browser with normal Pexels reachability will load the photos" | True — the photos load — but they are the WRONG photos. | The A.5 framing collapsed two distinct failure classes (CDN-unreachable vs wrong-content). A.6 disambiguates. |

The A.5 report's misclassification is the proximate reason this defect
survived to the user-handshake gate. A.6's contribution is to (a) catch
it before the user sees it, (b) apply the conservative-narrow mitigation
to remove the inappropriate content from the live render, and (c) escalate
to the orchestrator with a recommended A.5b re-curate workstream.

---

## §4 · Frozen sibling regression verdict (post-fix)

| Sibling | Layout family | Anonymous home | A.5 body length | A.6 body length | Verdict |
|---|---|---|---|---|---|
| Pragma | LF-1 | 200 | 87,112 bytes | 87,112 bytes | **NO REGRESSION** (byte-equivalent) |
| Cornice | LF-2 | 200 | 98,673 bytes | 98,673 bytes | **NO REGRESSION** (byte-equivalent · Bologna golden-hour portico hero intact · Cormorant Garamond + rust accent intact · Marta Roveri founder intact) |
| Fiscus | LF-3 | 200 | 88,010 bytes | 88,010 bytes | **NO REGRESSION** (byte-equivalent) |
| Solaria | LF-4 | 200 | 88,449 bytes | 88,449 bytes | **NO REGRESSION** (byte-equivalent) |
| Continua | LF-5 | 200 | 94,640 bytes | 94,640 bytes | **NO REGRESSION** (byte-equivalent · library reading-room mahogany · pine + brass intact · 3-pillar governance intact) |

**Verdict: 5/5 frozen siblings unchanged.** F1's mitigation is selector-
scoped to Causa's content module (the `_IMAGERY_HOLD_PLACEHOLDER` constant
only feeds Causa's own page_data dict; no other template module is touched).
The home dispatcher chain in `home.html` is unchanged. Cornice's hero photo
loads from `business-architecture` pool (Pexels 35715509 · empty Bologna
portico · verified live in capture `20-cornice-1440-control.jpeg` · golden-
hour stone-warm exterior intact). Causa's bottle-green palette is NOT
bleeding into Cornice's graphite + pietra-serena + rust palette.

**Anonymous HTTP check (frozen sibling tier-gate intact)**:

```
pragma-corporate-suite : 200 (87,112 bytes)
cornice-architettura  : 200 (98,673 bytes)
fiscus-commercialista : 200 (88,010 bytes)
solaria-coaching      : 200 (88,449 bytes)
continua-stewardship  : 200 (94,640 bytes)
```

Trust counter on home `/` reads `24+` (Causa is draft, NOT counted in
public listings). Catalog header `templates/business/` lists 6 corporate-
suite siblings — Pragma + Cornice + Fiscus + Solaria + Continua + Pragma's
existing extra — Causa is correctly absent from the public listing.

---

## §5 · Causa distinctness verdict (post-fix · 5-axis triangulation)

The distinctness contract is per `causa-distinctness-proof.md §2` and
`copy-authoring.md §17`. A.5 reported 5/5 vs Pragma · 12/12 vs Cornice ·
6/6 vs Fiscus · 7/7 vs Solaria · 11/11 vs Continua. A.6's question is:
**does the imagery hold change any of these axes?**

The honest answer is YES on the imagery axis specifically (the photographic
distinctness claim from A.5 is now unverifiable because the photos are
hold-state placeholders), but the layout / typography / copy / palette /
voice axes are UNCHANGED and continue to discriminate Causa from every
sibling.

### vs Cornice (LF-2 first occupant · highest collision risk · load-bearing axis)

| Axis | Cornice | Causa (post A.6 fix) | Verdict |
|---|---|---|---|
| Voice anchor noun | `argomento` · curatorial-thesis | `evidenza` · public-record-evidence (verbatim recurrence on hero h1 + cta-closer h2 verified live · 2/2) | **DISTINCT** |
| Em-word recurrence count | 12 ems on home | 12 ems on home (`evidenza` · `incardina` · `giurisdizione` · `massima` · `sostenuta` · `2008` · `Marchetti` · `incardinata` · `giurisprudenza` · `principio` · `controversia` · `evidenza`) — verified live | **DISTINCT** (zero `argomento · argomenta · geometria · lotto · minore` overlap) |
| Heading serif | Cormorant Garamond | GT Sectra (DOM probe verified) | **DISTINCT** |
| Body sans | Source Sans 3 | Manrope (DOM probe verified) | **DISTINCT** |
| Palette | graphite + pietra-serena + rust (warm-display-on-cool) | bottle-green `#14342B` + bone `#F0EBE0` + obsidian `#0B0A0E` (full cool · matte-on-matte · zero metallic) — DOM-verified `--primary` / `--secondary` / `--accent` | **DISTINCT** (matrix §1.3 third polarity dimension) |
| Hero subject | Bologna golden-hour portico exterior (verified live in capture 20) | imagery hold (placeholder · A.5b will replace with empty courtroom interior per planner-brief §4 binding triple) | **PENDING A.5b** (claim cannot be re-verified at A.6 because the photographic surface is held; the COPY axis around the hero (eyebrow + h1 + KPI tuple + side-quote + alt text) reads forensic-publication and does NOT collapse into Cornice's architectural-press register) |
| Founder identity | Marta Roveri · feminine · architect | Lorenzo Marchetti · masculine · Cassazionista (8 surfaces in agreement · bio + role + h2 + label + intro + history + values + servizi card all read masculine + Cassazionista) | **DISTINCT** (R-LF2-2 mitigation per Cornice precedent · gender + name + pronouns + role + bio + intro + team-card role + studio-founder-eyebrow ALL agree) |
| Wordmark + descriptor | `CORNICE / studio di architettura` | `CAUSA / studio legale` (DOM probe verified) | **DISTINCT** |
| Geographic anchor | Bologna (case slug + portico subject) | Milano (sede via Borgonuovo · Foro di Milano · zero Bologna references) | **DISTINCT** |
| Nav labels | `Lo studio · Archivio · Servizi · Progetti · Contatti` | `Studio · Materie · Pubblicazioni · Contenzioso · Contatti` (5-link inline · zero shared tokens) | **DISTINCT** |
| KPI cells | `(novanta fascicoli · 2008 · 38 menzioni)` | `(28 sentenze · 14 voci · 31 anni)` — verified live | **DISTINCT** |
| CTA pill copy | "APRI UN FASCICOLO PROGETTO" filled rust | "APRI UN PARERE PRELIMINARE" filled bottle-green (verified live on home + 4 inner pages + 4 case-detail · Cornice default `Apri un fascicolo` would be a fail · A.5 closed this with primary_cta on every page_data dict) | **DISTINCT** (no fascicolo / dossier mental model) |
| Whistleblowing column content | architecture-firm | forensic-firm-specific (D.lgs. 24/2023 · responsabile = associato senior · Codice Deontologico Forense art. 622 c.p. on contatti consent) | **DISTINCT** |
| Vocabulary density | architectural-press | forensic-publication (`evidenza` 21 hits · `massima` 21 hits · `patrocinio` 11 hits · `incardinata` 9 hits · `Cassazionista` 7+ hits · zero `argomento · monografia · saggio · concorso · restauro · MIBAC · OAPPC · DAStU`) | **DISTINCT** |

**12/13 distinctness axes vs Cornice clear at A.6.** The hero subject axis
is the only one where the photographic claim cannot be re-verified at A.6
(the photograph is on hold). All copy / chrome / typography / palette /
geography / vocabulary axes continue to read forensic-publication and do
NOT collapse into Cornice's architectural-press register. The voice anchor
recurrence (the load-bearing distinctness signal per CS-EXEC-01 + AC-15)
verifies live as 2/2 verbatim surfaces with em on `evidenza`.

### vs Pragma (LF-1) · vs Fiscus (LF-3) · vs Solaria (LF-4) · vs Continua (LF-5)

These distinctness axes were measured at A.5 and depend primarily on copy /
palette / typography / layout-family — none of which changed at A.6. The
imagery hold does NOT increase the collision risk against any of these
siblings (Pragma has photographic boardroom · Fiscus has tidy desk + tax
docs · Solaria has 1:1 conversation · Continua has library reading-room ·
none of these are bottle-green-gradient-with-italic-label so the imagery
hold is unmistakably distinct from all four).

| Sibling | A.5 verdict | A.6 verdict |
|---|---|---|
| Pragma (LF-1) | 5/5 distinct | **5/5 distinct** (layout family + palette + typography + copy axes unchanged) |
| Fiscus (LF-3) | 6/6 distinct | **6/6 distinct** |
| Solaria (LF-4) | 7/7 distinct | **7/7 distinct** |
| Continua (LF-5 · cool-on-cool) | 11/11 distinct | **11/11 distinct** (R-CAU-1 hex distance + R-CAU-2 interior subject differentiation cleared at copy + palette levels; the imagery axis is on hold but the placeholder bottle-green is hex-distinct from Continua's pine and the placeholder text "imagery hold" makes it unambiguously NOT a Continua library reading-room) |

**Aggregate distinctness verdict: NO COLLAPSE.** Causa reads as "evidence-
led Cassazionista litigation boutique with imagery hold pending re-curate"
which is unmistakably distinct from all 5 live siblings. The hold pattern
does NOT introduce any new collision risk.

---

## §6 · Voice + content fidelity (post-fix)

**Voice anchor verbatim recurrence** at exactly two surfaces on home:

- Hero h1: `Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.` ✓ (DOM-verified)
- CTA-closer h2: `Ogni sentenza è un'<em>evidenza</em> incardinata, non un'opinione difesa.` ✓ (DOM-verified)

**Em-word audit on home (CS-TYPE-02 single em per heading)** — 12 ems
verified live post-fix:

| Surface | Em-word | Polarity |
|---|---|---|
| Hero h1 | `evidenza` | obsidian italic GT Sectra |
| Hero side-quote | `incardina` | obsidian italic |
| Pull-quote 1 | `giurisdizione` | obsidian italic |
| Pull-quote 2 | `massima` | obsidian italic |
| Pull-quote 3 | `sostenuta` | obsidian italic |
| Sectors counter footnote | `2008` | obsidian italic |
| Leadership h2 | `Marchetti` | obsidian italic |
| Magazine card 1 (hero) h3 | `incardinata` | obsidian italic (forensic resonance with hero h1 anchor) |
| Magazine card 2 (small) h3 | `giurisprudenza` | obsidian italic |
| Magazine card 3 (small) h3 | `principio` | obsidian italic |
| Magazine card 4 (small) h3 | `controversia` | obsidian italic |
| CTA closer h2 | `evidenza` | obsidian italic (verbatim recurrence) |

**12 em occurrences on home · all on distinct headings/quotes · `evidenza`
recurs 2× verbatim per AC-15.** CS-TYPE-02 PASS 12/12. The triple-resonance
on `incardinare`/`incardina`/`incardinata` (hero h1 + side-quote + magazine
card 1) creates the forensic-publication motif Voice Anchor Lock §3.4
specified — preserved through F1's photographic hold (the em pattern is
copy-only, unaffected by imagery).

**Forensic vocabulary density audit** (rendered home body):

| Vocabulary | Hits |
|---|---|
| `evidenza` | 21 |
| `incardinata` | 9 |
| `massima` | 21 |
| `massimario` | 10 |
| `patrocinio` | 11 |
| `giurisdizione` | 7 |
| `sentenze` | 7 |
| `parere preliminare` | 5 |
| `Cassazionista` | 7+ |

**≥40 forensic-publication hits + ≥6 credential hits achieved.** Forensic
register unmistakably dense from first scroll fold despite the imagery
hold — the page reads as litigation boutique through copy alone.

---

## §7 · Navbar pill audit (per page · post-fix)

The corporate-suite shared `_base.html:1241` defaults the trailing CTA pill
to `{{ page_data.primary_cta|default:"Apri un fascicolo" }}` (Cornice's
literal). A.5 closed the inner-page leak by adding `primary_cta` to all 4
inner page_data dicts. A.6 re-walked every page including the 4 case-detail
routes (which inherit `page_data` from the parent `contenzioso` page entry
per `views.py:440 ctx["page_data"] = content.get(self.page_entry["slug"], {})`).

| Page | Navbar pill (verified live) |
|---|---|
| home (`/preview/`) | APRI UN PARERE PRELIMINARE ✓ |
| studio (`/preview/studio/`) | APRI UN PARERE PRELIMINARE ✓ |
| materie (`/preview/materie/`) | APRI UN PARERE PRELIMINARE ✓ |
| contenzioso list (`/preview/contenzioso/`) | APRI UN PARERE PRELIMINARE ✓ |
| contatti (`/preview/contatti/`) | APRI UN PARERE PRELIMINARE ✓ |
| case-detail SS.UU. 2024 | APRI UN PARERE PRELIMINARE ✓ |
| case-detail Cass. III 2023 | APRI UN PARERE PRELIMINARE ✓ |
| case-detail TAR 2022 | APRI UN PARERE PRELIMINARE ✓ |
| case-detail App. Milano 2021 | APRI UN PARERE PRELIMINARE ✓ |

**9/9 pages render the Causa-specific CTA pill.** Zero Cornice-collision
surfaces. The Cornice CTA literal `Apri un fascicolo` does NOT appear
anywhere in the Causa render. Priority surface 4 (Inner-page CTA pill must
remain Causa-specific on every page) PASS.

---

## §8 · Draft preview path legitimacy (priority surface 5)

| Check | Expected | Got | Verdict |
|---|---|---|---|
| Anonymous home | 404 | 404 | ✅ |
| Anonymous case-detail | 404 | 404 | ✅ |
| Anonymous catalog listing (Causa MUST NOT appear) | 200 + Causa absent | 200 + `causa-legale` not in body | ✅ |
| Staff session + `?preview=1` home | 200 | 200 (104,466 bytes · larger than A.5's 100,006 because the placeholder data URL appears 10 times in the rendered HTML) | ✅ |
| Staff session + `?preview=1` 4 inner + 4 case-detail | 200 each | 200 each (sizes 61,299 — 70,709 bytes) | ✅ |
| Homepage trust counter `templates_live` | "24+" (unchanged) | "24+" preserved | ✅ |
| DB tier on `causa-legale` row | draft | draft (verified `WebTemplate.objects.filter(slug='causa-legale').first().tier == 'draft'`) | ✅ |
| DB layout_family on `causa-legale` row | LF-2 | LF-2 (verified) | ✅ |
| Cornice tier (frozen) | published_live | published_live | ✅ |

**Draft preview path is legitimate and intact.** Priority surface 5 PASS.

---

## §9 · Test suite status (post-fix)

```
$ python manage.py test
Ran 546 tests in 170.425s
OK

$ python manage.py test apps.catalog
Ran 171 tests in 3.156s
OK
```

**546 / 546 + 171 / 171 OK.** Zero new failures. Zero regressions on existing
tests.

The A.6 fix touches only content-string constants in `template_content_causa.py`
— no model fields, no DB schema, no view logic, no URL routing, no migration.
The placeholder data URL is opaque to every test (the tests assert on slug /
tier / layout_family / facet count / search keywords / route status — none of
which depend on photo URL content).

---

## §10 · What workflow C still has to do (no change vs A.5 spec)

The IT draft is review-locked for COPY/CHROME/TYPOGRAPHY/PALETTE but
imagery is HELD. Workflow C (multilingual) cannot proceed until A.5b
imagery re-curate completes. Once A.5b GREEN + A.6b rapid review pass
GREEN, workflow C delivers (unchanged from A.5):

1. **EN translation** of `CAUSA_CONTENT_IT` — 5 pages + 4 case-detail
   posts. Voice anchor verbatim-in-translation: `evidenza → evidence`
   (per voice-anchor-lock §6.2).
2. **FR translation** — voice anchor `evidenza → preuve`.
3. **ES translation** — voice anchor `evidenza → evidencia`.
4. **AR translation** — voice anchor `evidenza → دليل` + RTL handling
   + LF-2-scoped Naskh AR h1 swap (`html[dir="rtl"] body.cs-lf-lf-2`
   selector inherited from Cornice Pass C).
5. **TEMPLATE_REGISTRY.json** — flip Causa row's `locales` from `[it]`
   to `[it, en, fr, es, ar]` and `rtl: true`.
6. **Tier flip held until workflow D** — workflow C lands at tier=draft.
   Workflow D flips to `published_live` after a second user handshake on
   the multilingual walk.

**Workflow C is HELD pending A.5b imagery re-curate.** The orchestrator
should authorise A.5b first.

---

## §11 · Files changed at A.6

**Modified** (1 source file):

1. `apps/catalog/template_content_causa.py` — F1 mitigation. Replaced 10
   Pexels URL constants with a single `_IMAGERY_HOLD_PLACEHOLDER`
   base64-encoded SVG data URL. Added a ~30-line comment block at the
   imagery section documenting the A.6 finding and the conservative-narrow
   mitigation rationale.

**Created** (10 reports + 20 captures):

- `factory/reports/causa/causa-a6-it-review-lock.md` (this file)
- `factory/reports/browser-verification/causa-a6-it-review-lock.md`
- `factory/reports/browser-verification/causa-a6-it-review-lock/captures/*.jpeg` (20 captures: pre-fix evidence + post-fix verification + 4 backup-Pexels-direct + 1 Cornice control)
- `factory/reports/scorecard/causa-a6-it-review-lock/build-report.md`
- `factory/reports/scorecard/causa-a6-it-review-lock/style-critic.md`
- `factory/reports/scorecard/causa-a6-it-review-lock/contrast-accessibility.md`
- `factory/reports/scorecard/causa-a6-it-review-lock/responsive-auditor.md`
- `factory/reports/scorecard/causa-a6-it-review-lock/browser-verifier.md`
- `factory/reports/scorecard/causa-a6-it-review-lock/release-gatekeeper.md`
- `factory/reports/scorecard/causa-a6-it-review-lock/scorecard.md`
- `factory/reports/scorecard/causa-a6-it-review-lock/summary.md`

**Untouched at A.6** (per scope rules):

- apps/editor — zero edits
- apps/projects — zero edits
- apps/commerce — zero edits
- apps/catalog/preview_imagery.py — zero edits (business-legale pool stays at curator URLs · A.5b will re-curate)
- apps/catalog/template_dna.py — zero edits
- apps/catalog/template_content.py — zero edits
- apps/catalog/views.py — zero edits
- apps/catalog/migrations/* — zero edits
- All other archetype templates (template_content_pragma.py · _cornice.py · _fiscus.py · _solaria.py · _continua.py · _vertex.py · _gusto.py · _aura.py · _elevate.py · etc.) — zero edits
- LF-1 / LF-3 / LF-4 / LF-5 layout files — zero edits
- LF-2 layout files (`_layouts/lf2/content.html` + `_layouts/lf2/styles.html`) — zero edits
- corporate-suite chrome (`_base.html`) — zero edits
- TEMPLATE_REGISTRY.json — zero edits (`tier=draft` preserved)
- docs/content-factory/imagery/packs/business-litigation.md — zero edits (curator pack to be replaced at A.5b)

---

## §12 · Server / route status (handed back to orchestrator · post-fix)

```
server:                 python manage.py runserver 8052 --noreload
URL prefix:             http://127.0.0.1:8052/
template root URL:      /templates/business/causa-legale/preview/
9 IT routes (all 200 staff_preview · 404 anonymous):
  - /preview/                                                                   (home)
  - /preview/studio/                                                            (about · "Pubblicazioni")
  - /preview/materie/                                                           (services · 12 materie)
  - /preview/contenzioso/                                                       (cases list)
  - /preview/contatti/                                                          (contact + 7-field intake)
  - /preview/contenzioso/cass-ssuu-responsabilita-consulente-fiscale-2024/      (case-detail · SS.UU.)
  - /preview/contenzioso/cass-civ-iii-anatocismo-bancario-2023/                 (case-detail · Cass. civ. III)
  - /preview/contenzioso/tar-lombardia-agcom-proporzionalita-2022/              (case-detail · TAR Lombardia)
  - /preview/contenzioso/appello-milano-art-36bis-dpr-600-1973-2021/            (case-detail · App. Milano trib.)

tier:                   draft (anonymous: 404 · staff_preview: 200 with ?preview=1)
catalog count:          24 published_live + 1 draft = 25 total
session reqs:           staff user authenticated (causa_review_a6 · is_staff=True · is_superuser=True)
                        + ?preview=1 query string

frozen siblings (all 200 anonymous · byte-equivalent to A.5):
  - /templates/business/pragma-corporate-suite/preview/      LF-1   87,112 bytes
  - /templates/business/cornice-architettura/preview/        LF-2   98,673 bytes
  - /templates/business/fiscus-commercialista/preview/       LF-3   88,010 bytes
  - /templates/business/solaria-coaching/preview/            LF-4   88,449 bytes
  - /templates/business/continua-stewardship/preview/        LF-5   94,640 bytes

test suite:             546 / 546 OK · 171 / 171 catalog OK
```

Server is left running on port 8052 for orchestrator inspection.

---

## §13 · Lock verdict

The A.6 review-lock is **PARTIAL · IMAGERY HELD**.

- Copy / chrome / typography / palette / responsive / voice anchor / em-word
  audit / navbar pill / draft preview path / frozen sibling regression /
  test suite — ALL LOCKED.
- Photographic surfaces (hero · feature · 2 portraits · detail · ambient ·
  4 magazine cards) — HELD pending A.5b imagery re-curate.

**Causa IT is NOT YET LOCKED FOR USER VISUAL HANDSHAKE.** The placeholder
imagery makes the page reviewable for everything-except-imagery, but the
visual handshake itself requires real photos for the user to confirm the
litigation-boutique register reads as intended at the photographic axis.

**Workflow C (multilingual) and Workflow D (public flip) remain HELD.**
The orchestrator should authorise a Phase X.6 Step 5b imagery re-curate
workstream:

1. Re-curator does fresh Pexels search for the 6 primary slots + 4 magazine-
   grid extras with **mandatory live-URL verification** (no LLM-fabricated
   IDs · every URL navigated and screenshotted before commit).
2. Re-curator updates `business-litigation.md` and `apps/catalog/preview_
   imagery.py business-legale` with verified URLs.
3. Re-curator updates `apps/catalog/template_content_causa.py` to replace
   the `_IMAGERY_HOLD_PLACEHOLDER` with the new verified URLs.
4. A.6b rapid review re-walks the priority surfaces (hero · founder ·
   case-cards) live to confirm the empty-courtroom + chambers-Cassazionista
   + high-court-architectural register.
5. On A.6b GREEN, the orchestrator re-issues the user-handshake invitation
   with the now-fully-locked IT draft.

If user signals **HOLD** instead of authorising A.5b: A.7 narrow re-author
on copy axis (NOT imagery) per the Cornice precedent.
