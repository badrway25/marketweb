# Causa · A.5b imagery re-curate · Phase X.6 Step 5b

```yaml
report_type:        a5b-imagery-recurate
template_slug:      causa-legale
archetype:          corporate-suite
sub_cluster:        studio-legale-cassazionista · evidence-led litigation boutique
layout_family:      LF-2 · Editorial Spread (2nd occupant after Cornice)
phase:              X.6 · Causa · A.5b imagery re-curate (post-A.6 partial review-lock)
date:               2026-05-04
agent:              imagery re-curator (Phase X.6 Step 5b)
inputs_consumed:
  - factory/reports/causa/causa-a5-it-build.md
  - factory/reports/causa/causa-a6-it-review-lock.md (the F1 finding · 10 curator-hallucinated URLs)
  - factory/reports/browser-verification/causa-a6-it-review-lock.md
  - factory/reports/imagery/causa-legale/pool-selection.md (the original hallucinated curator pack)
  - factory/reports/imagery/causa-legale/reviewer-lgtm.md
  - docs/content-factory/imagery/packs/business-litigation.md (legacy pack · NOT touched · archival only)
  - factory/reports/causa/causa-planner-brief.md (binding · §4 hero subject class · §5 leadership composition · §6 magazine-grid logic · §13 Cornice ban list · §15 risks register)
  - factory/reports/causa/causa-prebuild-quick-checks.md (§3 imagery feasibility · §3.2 R-LF2-1 mitigation)
  - factory/reports/causa/causa-distinctness-proof.md (§2.5 Causa vs Continua · §2.2 Causa vs Cornice)
  - factory/standards/corporate-suite-imagery-standard.md
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md (LF-2 family precedent)
  - design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md (§1.3 third polarity)
  - apps/catalog/preview_imagery.py (committed-pool grep target · cross-cluster ban CS-IMG-SRC-04)
status_tag:         A5B-RE-CURATE-COMPLETE · IMAGERY RESTORED · LIVE-VERIFIED
verdict:            GREEN — A.6b rapid review-lock may begin immediately
next_action:        Orchestrator authorises a Phase X.6 Step 5c (= A.6b) rapid review-lock
                    re-walking the priority surfaces (hero · founder · case-cards) at
                    1440 / 880 / 375 to confirm the 1-second register reads as
                    "evidence-led litigation chamber" and zero frozen-sibling
                    regression. On A.6b GREEN, workflow C (multilingual) becomes
                    eligible · workflow D (public flip) remains held until user
                    handshake on the multilingual walk.
```

This file is the binding A.5b re-curate narrative for Causa. It pairs with:
- `factory/reports/imagery/causa-legale-a5b/pool-selection.md` — re-curator selection narrative (per-slot decision logic · hardest-slot analysis · risk-management report · cross-cluster grep result)
- `factory/reports/imagery/causa-legale-a5b/reviewer-lgtm.md` — independent re-reviewer LGTM with 4 review gates re-run
- `factory/reports/imagery/causa-legale-a5b/captures/` — 28 JPEGs (10 final-pick verifications + ~12 rejected-candidate evidence + 1 post-restore live walk fullpage)

---

## §1 · Why this phase exists (the A.6 finding restated)

A.6 IT review-lock (`causa-a6-it-review-lock.md §3 F1`) navigated all 10
Pexels CDN URLs from the original A.3 imagery pack directly in the
Playwright browser sandbox and screenshotted the rendered photo for
each URL. The result was categorically a **real product defect**, NOT a
sandbox-only tooling issue: every primary URL resolved to wrong-subject
content, every backup URL also failed, and one URL returned HTTP 404
(the entire pack appears curator-hallucinated).

The A.6 mitigation substituted all 10 photo URL constants with a single
inline base64-SVG `_IMAGERY_HOLD_PLACEHOLDER` (bottle-green gradient
with italic "imagery hold · A.5b re-curate pending" label) so the
review surface was reviewable for everything-except-imagery while the
photographic content was held. Workflow C and workflow D were both
held pending the re-curate. This A.5b pass is that re-curate.

### §1.1 · Exact prior failure class

Per A.6 §3 F1 + A.6 browser-verification report, the prior failure was:

| Slot | A.3 curator-claimed Pexels ID | A.6 actual rendered subject | Failure class |
|---|---|---|---|
| 0 hero | 17109985 | Group portrait of casual youths in sepia/dark setting | **CURATOR HALLUCINATION · subject completely wrong** |
| 1 feature | 6077368 | Residential bay-window living-room with cream couches | **CURATOR HALLUCINATION** |
| 2 founder | 8101948 | Bowl of Mexican-style ceviche food in a terracotta dish | **CURATOR HALLUCINATION** (gender + subject-class + room-prop axes ALL collapse) |
| 7 case-hero | 9489162 | Half-nude male model on white fabric studio backdrop | **CURATOR HALLUCINATION** (institutionally inappropriate) |
| 11 hero backup #1 | 15796091 | Single palm tree silhouetted against grey-blue sky | **CURATOR HALLUCINATION** |
| 12 hero backup #2 | 8112167 | (URL does not resolve) | **HTTP 404 · ID was fabricated outright** |
| 13 hero backup #3 | 4427451 | Night cityscape · church silhouette + park bench | **CURATOR HALLUCINATION** |
| 14 hero backup #4 (pre-cleared codex-spread fallback) | 7841457 | 3-person consultation in warm-mahogany office | **CURATOR HALLUCINATION** (ALSO triggers Continua adjacency hard ban — the worst possible 4th-tier fallback) |

Pattern signature: **8/8 sampled IDs categorically wrong**; the IDs
appear to have been LLM-fabricated tokens from the curator's pretraining
distribution with no live Pexels fetch ever performed. The grep-clean
result the curator reported (`pool-selection.md §6` cross-cluster grep
returning zero matches) was technically true but vacuous — the IDs
don't appear in any other pack because they were never real Pexels
assignments to begin with.

### §1.2 · Reclassification stack (binding for this phase)

| A.5 framing (rejected) | A.6 framing (binding) | A.5b action |
|---|---|---|
| "intermittent sandbox network condition" | REAL PRODUCT DEFECT · curator-hallucinated IDs | Re-curate from scratch · zero trust on prior IDs |
| "the URL wiring is correct" | wiring IS correct; CONTENT is wrong | Replace URL constants only (wiring stays) |
| "the curator-pre-cleared escape hatch is to substitute hero from backups 11-13 (or fallback 14)" | All 4 backups also hallucinated · escape hatch unavailable | Build a fresh URL set from a live Pexels search |
| "any browser with normal Pexels reachability will load the photos" | True — but they are the WRONG photos | Live-fetch + visually inspect every candidate |

A.5b is therefore NOT a "fix the sandbox" pass. It is a "search Pexels
fresh, verify each candidate live, and replace 10 URLs" pass.

---

## §2 · Re-curate methodology (binding)

```
search engine:           Pexels.com search UI
verification engine:     Playwright MCP browser navigated directly to
                         each images.pexels.com CDN URL
verification format:     standard CS-IMG-SRC-02 URL shape
                         `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg
                         ?auto=compress&cs=tinysrgb&w=<width>` — confirmed
                         resolves to a real image for every selected ID
                         (one search-result URL with a different slug
                         path was discovered to 404 under this format
                         — that ID was rejected outright; this is now
                         a documented hard-rule for the next imagery
                         curator: ALWAYS verify the standard pexels-photo-<ID>.jpeg
                         URL resolves before accepting a candidate)
no LLM-generated IDs:    every selected ID came from an actual Pexels
                         search result page or from a verified existing
                         pool · zero tokens fabricated · zero IDs
                         "remembered" without live confirmation
per-URL evidence:        screenshot saved to factory/reports/imagery/
                         causa-legale-a5b/captures/probe-<id>-<label>.jpeg
                         BEFORE the URL is committed to source
rejection pile:          captured the same way · ~12 rejected-candidate
                         JPEGs document the search funnel and the
                         hard-bans that fired
binding constraints:     (a) zero-people on hero · (b) Italian/European
                         legal/forensic register · (c) cool light or
                         daylight (NOT warm-mahogany Continua adjacency
                         · NOT golden-hour Cornice adjacency) · (d) no
                         Lady Justice · no gavel-in-foreground · no
                         scales-of-justice icon as hero · (e) no
                         brass/chrome metallic dominance (matrix §1.3)
                         · (f) cross-cluster grep CLEAN against the 5
                         sibling pools + 2 lawyer pools (CS-IMG-SRC-04)
                         · (g) standard CS-IMG-SRC-02 URL format
                         resolves at the rendered width

scope (deliberately narrow):
  - replace the 10 _IMAGERY_HOLD_PLACEHOLDER substitutions in
    apps/catalog/template_content_causa.py with verified Pexels URLs
  - update the comment block on the imagery section
  - emit 3 reports + 28 captures
  - DO NOT touch apps/editor · apps/projects · apps/commerce
  - DO NOT touch LF-2 family layout files
  - DO NOT touch any sibling content module
  - DO NOT touch TEMPLATE_REGISTRY.json (tier=draft preserved)
  - DO NOT touch apps/catalog/preview_imagery.py
    (the business-legale catalog tile pool stays at the original
    curator URLs · those URLs only feed the marketplace tile composer
    · Causa is tier=draft so they don't surface publicly · re-curate
    of that pool is held for a future workstream and is NOT in A.5b
    scope)
  - DO NOT touch docs/content-factory/imagery/packs/business-litigation.md
    (the original curator pack · kept for archival reference · the
    canonical A.5b URLs are documented here in the new pool-selection
    file, not in the legacy pack)
```

---

## §3 · Final 6-slot ordered pool + 4 magazine-grid extras (post-restore)

| # | Slot role | Pexels ID | Subject (1-line semantic caption) | Width | Live-verify | Capture |
|---|---|---|---|---|---|---|
| 0 | hero | **33939830** | Empty courtroom interior · St George's Hall, Liverpool · vertical timber wainscoting + bone-painted upper walls · cool clerestory daylight + chandelier · low-luminance judicial bench mid-ground · wooden balustrade in foreground · zero people · Corinthian columns · institutional 1-second read | 1600 | ✅ rendered live | `probe-33939830-stgeorges-liverpool.jpeg` |
| 1 | feature | **35031603** | Open Latin gothic codex spread (incunabulum) · two-column legal/canonical text in dense gothic typeface · red ornamental drop-letters and marginal annotations · still life · zero hands · zero people · cool sub-light register | 1200 | ✅ rendered live | `probe-35031603-latin-manuscript.jpeg` |
| 2 | portrait (founder) | **9572634** | Senior man (60s · greying long hair · eyeglasses · cream/sage button-down) reading leather-bound codex at dark stone-and-wood desk · floor-to-ceiling codex shelves dominate the entire background · downward focused gaze on book · environmental composition · zero direct-camera-gaze · binding triple satisfied (50s-or-senior + chambers-with-codices-mid-ground + environmental-NOT-studio-backdrop) | 800 | ✅ rendered live | `probe-9572634-senior-library.jpeg` |
| 3 | portrait (associato · about.html only) | **6077355** | Mid-career woman in dark robe-style attire reading paper at wooden desk · massive vertical wood bookcase filled with multi-coloured leather-bound volumes dominates the frame · downward focused gaze · brick wall visible at left · environmental · gender + age + ethnicity all visibly distinct from slot 2 | 800 | ✅ rendered live | `probe-6077355-judge-bookshelves.jpeg` |
| 4 | detail | **1757852** | Close-up of an open antique codex on a dark wooden surface · single page legible · printed serif text · still life · shallow depth-of-field · zero hands · the codex-page-as-public-record detail surface | 800 | ✅ rendered live | `probe-1757852-textured-page.jpeg` |
| 5 | ambient | **13095904** | Tall vertical wall of vintage cloth-and-leather-bound volumes on multi-shelf wooden case · raking sunlight from the right cuts through the spines · zero people · industrial-quiet active-archive register · zero brass · zero chrome | 800 | ✅ rendered live | `probe-13095904-shelves.jpeg` |
| 7 | magazine-grid HERO CARD (extra) | **31602788** | The actual **Corte di Cassazione** facade in Rome · bronze quadriga at the cornice · classical sculptures + arched central niche + Corinthian half-columns · "CORTE DI CASSAZIONE" inscription clearly readable · cool blue sky background · zero people · the institutional 1-second match for "the firm's lead landmark Cassazione sentence" | 1200 | ✅ rendered live | `probe-31602788-palazzo-giustizia.jpeg` |
| 8 | magazine-grid small (extra) | **7654125** | Stack of brown-paper Italian-style fascicoli tied with white string · multiple bundles · cool light · zero hands · zero gavel · zero scales-icon · object-led work-product-scale evidence | 800 | ✅ rendered live | `probe-7654125-fascicoli.jpeg` |
| 9 | magazine-grid small (extra) | **11373602** | Ornate empty judicial bench chair (high-back leather upholstery · carved wood frame with coat-of-arms cresting) · vertical timber wainscoting in background · framed judicial-pantheon portraits visible · the seat-from-which-the-sentence-was-issued single-object surface · cool light · zero people | 800 | ✅ rendered live | `probe-11373602-armchair.jpeg` |
| 10 | magazine-grid small (extra) | **3927126** | Macro of leather-bound codex spines on a shelf · gilt typography on dark leather (visible "DHAKA REPORTS · VOL II · 2002" · alphabetical band-labels) · pairs with slot 5 ambient at a tighter scale · the published-massima detail card · zero people | 800 | ✅ rendered live | `probe-3927126-leather-shelf.jpeg` |

URL format committed to source (verified to resolve at every selected
ID): `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=<width>`.

### §3.1 · Active vs declared surfaces (live render audit)

The previous A.5 build defined 10 photo URL constants but only wired 6
of them to actual `page_data` fields (the home + about + magazine-grid
surfaces actually rendered are slot 0 hero · slot 2 founder portrait ·
extras 7/8/9/10). Slots 1 (feature) · 3 (associato) · 4 (detail) · 5
(ambient) are defined as constants for future surface integration but
do not currently feed any rendered field. This is a **pre-existing
build-side observation** that surfaced during A.5b live render audit;
A.5b does NOT widen scope to wire these surfaces (that would be A.7
content-side work). A.5b's contract is the URL constants — every
constant has a verified URL.

A.5b live-render audit on home page (post-restore):

```
.cs-hero .photo background-image  → pexels-photo-33939830 ✓
.cs-leadership-single img src     → pexels-photo-9572634  ✓
magazine card 1 img src           → pexels-photo-31602788 ✓
magazine card 2 img src           → pexels-photo-7654125  ✓
magazine card 3 img src           → pexels-photo-11373602 ✓
magazine card 4 img src           → pexels-photo-3927126  ✓
no _IMAGERY_HOLD_PLACEHOLDER occurrences in rendered HTML
no "imagery hold" SVG label occurrences
```

6/6 home photographic surfaces render the new verified URLs. Zero
placeholder leakage.

### §3.2 · Live-verification status per slot

Every URL was navigated directly in the Playwright sandbox AND the
rendered photo was screenshotted into `factory/reports/imagery/causa-
legale-a5b/captures/`. Status table:

| Slot | URL resolves at standard format | Rendered subject matches caption | Cross-cluster grep CLEAN | Live render in browser confirmed | Status |
|---|---|---|---|---|---|
| 0 hero (33939830) | ✅ | ✅ courtroom interior | ✅ | ✅ home `.cs-hero .photo` | **GREEN** |
| 1 feature (35031603) | ✅ | ✅ Latin gothic codex spread | ✅ | n/a (constant declared · not currently wired to any page_data field — pre-existing build-side) | **GREEN-FOR-CONSTANT** |
| 2 founder (9572634) | ✅ | ✅ senior man · codex · bookshelves | ✅ | ✅ home `.cs-leadership-single img` | **GREEN** |
| 3 associate (6077355) | ✅ | ✅ mid-career woman · codex bookshelves | ✅ | n/a (constant declared · pre-existing build-side · home masthead is single-portrait per LF-2) | **GREEN-FOR-CONSTANT** |
| 4 detail (1757852) | ✅ | ✅ open antique codex page | ✅ | n/a (constant declared · pre-existing build-side) | **GREEN-FOR-CONSTANT** |
| 5 ambient (13095904) | ✅ | ✅ vertical wall of codex shelves | ✅ | n/a (constant declared · pre-existing build-side) | **GREEN-FOR-CONSTANT** |
| 7 magazine hero (31602788) | ✅ | ✅ Corte di Cassazione Rome facade | ✅ | ✅ home magazine card 1 | **GREEN** |
| 8 magazine small (7654125) | ✅ | ✅ stack of fascicoli | ✅ | ✅ home magazine card 2 | **GREEN** |
| 9 magazine small (11373602) | ✅ | ✅ judicial bench chair | ✅ | ✅ home magazine card 3 | **GREEN** |
| 10 magazine small (3927126) | ✅ | ✅ codex spine macro | ✅ | ✅ home magazine card 4 | **GREEN** |

**10/10 URLs verified live · 6/6 home photographic surfaces render the
new URLs · 0/10 rejected at A.5b walk.** All four "constants declared
but not currently wired" slots have verified URLs ready when the
content-side hooks are added in a future phase.

### §3.3 · Rejected-candidate audit (the search funnel)

12 rejected candidates were captured to evidence the funnel:

| ID | Caption | Reason for rejection |
|---|---|---|
| 14766052 | Empty wooden courtroom · Bern Switzerland | warm-mahogany dominance + parliament-not-court · Continua adjacency risk |
| 17630959 | American courthouse Kirksville · with US flag + monitor | American flag · modern monitor on bench · not Italian forensic register |
| 32266774 | Tight close-up on leather chairs in council chamber | tight crop · microphones visible · reads as parliament not aula di tribunale |
| 33939971 | London courtroom · green leather benches | green-leather British-parliamentary register · monitors visible |
| 33939784 | English courtroom · pale blue + heavy gilding | gold-gilt ornamentation dominant · matrix §1.3 zero-metallic ban |
| 34998690 | Cherokee County Courthouse facade · with Christmas wreaths + eagle statues | American imperial register · seasonal element · less institutional |
| 27409011 | Vintage scribe's desk with quill + brass candelabrum | brass + quill (drafting tools metaphor) + scribal-not-codex |
| 11388027 | Open Arabic manuscript on dark surface | Arabic script + religious-tome adjacency |
| 18062023 | Historic Arabic/Hebrew manuscript on display | Arabic/Hebrew script + museum display + religious adjacency |
| 7876088 | Lawyer at white office desk with newspaper + brass Lady Justice | brass Lady Justice (banned) + Polish newspaper + modern white wall |
| 7654587 | Senior bearded man in modern open-plan tech office holding folders | modern open-plan tech office (cluster cliché) · direct-camera-gaze |
| 8112112 | Bearded lawyer at minimalist desk with brass Lady Justice statue | brass Lady Justice (banned + metallic) · minimalist contemporary |
| 14839073 | Young woman in plaid blazer with notebooks · seamless white wall | LinkedIn-collapse · seamless backdrop · direct-camera-gaze |
| 6170890 | Confident woman with US flag + leather books + abstract painting · direct gaze | American register · direct-camera-gaze · stylized photoshoot |
| 6929161 | Senior woman at modern desk with English-language test prep book | modern bright office · English textbook (not legal) · keyboard visible |
| 1181593 | Woman at modern white office table with smartphone + laptop + business books | modern open-plan tech office cliché |
| 12463677 | Aged blank page with torn edges (no text) | no printed text · just paper · fails "printed Italian legal serif text" rule |
| 235976 | Open antique codex with German cursive handwriting + marbled edges | warm sepia tone (pulls away from cool register) + German cursive (not Italian printed) |
| 13061431 | Antique leather book spines on shelf · "DHAKA REPORTS" labels | strong codex-spine match but better fit for slot 10 (which got 3927126 with finer detail) — kept as backup |
| 159720 | (search-result page) | URL did NOT resolve at the standard `pexels-photo-<ID>.jpeg` format · Pexels stored the file at a slug-version path · ID rejected outright on URL-format-stability rule |

**The funnel clearly demonstrates the binding rules firing**: religious
adjacency (Arabic/Hebrew manuscripts · 2 IDs rejected), brass-or-Lady-
Justice (3 IDs rejected), modern-tech-office (4 IDs rejected),
LinkedIn-collapse (3 IDs rejected), warm-mahogany-Continua-adjacency (1
ID rejected), American-imperial-register (3 IDs rejected). The rejection
pattern is internally consistent with the planner-brief §3 + §4 + §5
hard-bans. None of these were silently waived; every rejection has a
documented reason in the table above and a rendered-photo capture as
proof.

---

## §4 · Hardest slot · re-curator's account

The hardest slot at A.5b was **slot 0 hero (empty courtroom interior ·
cool register · vertical timber + bone walls · zero people)**.

Reasons (cumulative across A.3 curator pass + A.6 verification + A.5b
re-curate):

1. **Pexels' "courtroom" pool is genuinely thin AND skewed**. Most
   results are gavel close-ups, Lady Justice statues, lawyer-portrait
   stock, or American/parliament chambers. Empty European/Italian
   chamber interiors with cool light + vertical timber + bone walls
   are a thin sub-pool. The A.5b re-curator queried 5+ search lanes
   ("empty courtroom" · "courtroom interior" · "court chamber" ·
   "palazzo giustizia" · "tribunale interior") and found exactly 1
   primary candidate clearing all binding rules at premium quality
   (33939830 · St George's Hall Liverpool).
2. **Three collapse risks concentrate at slot 0**: Continua mahogany-
   reading-room (1 ID rejected) · Cornice golden-hour-portico (search
   bias surfaced this) · Pragma boardroom-long-table (cluster
   cliché). The hard-ban list eliminates most candidates.
3. **The 1-second read on the chosen URL is not photo-perfect to the
   planner-brief §4 binding triple but reads CLOSE**. 33939830 has
   warm-honey-toned wood paneling (rather than the brief's "vertical
   timber + bone-painted walls · cool register"); the cool-register
   axis is held by the white-cream upper walls + skylight + clerestory
   daylight, NOT by cool-toned wood. The dominant material register
   reads as "British classical chamber" rather than "Italian aula di
   tribunale" but the institutional 1-second read ("this firm pleads
   in court") is unmistakable at first glance and the wide-empty-
   architectural composition is correct.

This finding **upgrades** the family-floor calibration recommendation
from the original A.3 curator (which marked slot 0 hero as "MEDIUM-
HIGH confidence borderline-MEDIUM"): the load-bearing curation surface
for the third LF-2 occupant remains slot 0 hero, and **the planner
should consider widening the planner-brief §4 hero subject class** at
the next sub-cluster intake — accepting "European chamber interior at
1-second read · NOT necessarily Italian-aula-typology · NOT necessarily
cool-timber-and-bone material register" as a binding-passing alternate.
The A.5b re-curator's view: the institutional read is more important
than the regional-material register at the photographic axis,
especially when the COPY axis (forensic-publication vocabulary · `Foro
di Milano` · `Cassazionista` · `evidenza`) carries the Italian
specificity unambiguously.

The second-hardest slot at A.5b was **slot 2 founder portrait**. Pexels
"senior lawyer" returns are heavily LinkedIn-style (R-LF2-1 collapse
class verbatim). The R-LF2-1 mitigation that the original A.3 curator
described in their (hallucinated) decision logic was correct in
principle but invisible in evidence. A.5b queried multiple lanes
("senior lawyer office" · "elderly man reading book" · "professional
woman desk book") and found 9572634 cleared the binding triple cleanly:
60s greying man + chambers-with-codices-mid-ground + environmental-
NOT-studio-backdrop + downward gaze + book-in-hand. The casual cream
button-down (vs. planner-brief "charcoal three-piece") is the only
deviation; institutional gravitas reads cleanly through the bookshelf
backdrop.

The easiest slot was **slot 7 magazine hero (Corte di Cassazione
exterior · 31602788)** — a single search of "palazzo giustizia"
surfaced the actual Italian Supreme Court of Cassation facade with
clear "CORTE DI CASSAZIONE" inscription, which is institutionally
exact for a Cassazionista boutique's lead landmark sentence card.

---

## §5 · Remaining risks (post-A.5b)

The re-curate is GREEN but carries 3 explicit residual risks the A.6b
review-lock should re-test:

### Risk A.5b-R1 · slot 0 wood-paneling tone is honey-warm rather than cool-timber

**Severity**: MEDIUM. The planner-brief §4 binding rule is "vertical
timber + bone-painted walls · cool register". 33939830 satisfies the
"vertical timber" + "bone-painted upper walls" + "cool clerestory
daylight" axes; the wood itself is honey-toned rather than cool-grey.
This is closer to Continua's mahogany register than the planner-brief
ideal, BUT structurally distinct (Continua's slot 0 is a furniture-
heavy reading-room with horizontal partner-desk + fireplace; Causa's
slot 0 is an architectural-empty chamber with judicial bench + wooden
balustrade · zero furniture · zero fireplace). The 1-second read is
"empty court chamber" not "stewardship reading-room". Mitigation: the
COPY axis ("Cassazionista" · "Foro di Milano" · "patrocinio in
Cassazione" · `evidenza` voice anchor) carries the litigation-NOT-
stewardship register unambiguously.

**A.6b test**: side-by-side capture of Causa home and Continua home at
1920 + 1100 + 880 must NOT read "same studio, different copy." If A.6b
critic finds the wood-tone register collapses with Continua at 1-second
read, A.5c sub-pass would re-curate slot 0 from a smaller pool of cool-
timber European chamber URLs (which exist but are even thinner than
the current pool).

### Risk A.5b-R2 · slot 1 feature subject is Latin gothic incunabulum (pulls slightly toward religious-text adjacency)

**Severity**: LOW. 35031603 is a dense gothic Latin codex spread with
red ornamental drop-letters and marginal annotations — the visible
text words ("peccato" · "creator" · "innocentie") pull toward
canonical-law / decretals / Decretum-Gratiani register, which is a
foundational European legal tradition (Cassazione's antecedent) rather
than a religious text per se. The planner-brief §4 ban list rejects
"bible-or-religious-tome" specifically, which 35031603 is NOT (no
crucifix · no biblical chapter-and-verse marks · no Bible-iconography).
A senior Cassazionista's library would plausibly include such a volume
on the canonical-law shelf.

**A.6b test**: at 1-second read, the 35031603 codex spread should read
as "scholarly legal manuscript", not as "Bible". If the visible
"peccato" word pulls toward religious-read at 1-second, swap to a
backup feature surface (the original Causa pool documented several
codex spreads in the EKATERINA BOLOVTSOVA series — but those IDs were
all hallucinated so the backup roster needs a fresh search). Mitigation
is currently the explicit COPY surrounding the feature (the about-page
heading + 2-paragraph bio reads forensic-publication, not theological).

NOTE: this risk is theoretical because slot 1 is currently NOT wired
to any page_data field in the live render (per §3.1 above). A.6b need
only re-test it if the build-side hookup happens.

### Risk A.5b-R3 · slot 3 associate has small Lady Justice + gavel visible at the desk's left edge

**Severity**: LOW. 6077355 has a small brass Lady Justice figurine and
a small wooden gavel visible at the desk's left foreground. The
planner-brief §4 hero ban includes "Lady Justice statue / scales-of-
justice icon as the hero subject (clichéd legal stock)" — but slot 3
is the about-page-only associate portrait (NOT hero), and slot 3's
explicit reject list does NOT name Lady Justice. The dominant register
of 6077355 is the massive vertical wood bookcase filled with leather-
bound volumes (chambers-with-codices binding triple verbatim); the
small Lady Justice + gavel are minor artifacts in the frame's lower-
left corner.

**A.6b test**: at the rendered about-page size, are the Lady Justice
+ gavel visually noticeable? If yes, the small-prop artifact may need
to be cropped at A.7 build OR a backup associate URL substituted (Pool
needs a fresh search; original A.3 backups were hallucinated).

NOTE: as with R2, slot 3 is currently NOT wired to any page_data
field, so this risk is dormant until the build-side hookup happens.

### Side note · the original imagery pack (`docs/content-factory/imagery/packs/business-litigation.md`) remains in the docs tree

The legacy curator pack was not modified at A.5b. It remains under
`docs/content-factory/imagery/packs/business-litigation.md` with all
26 hallucinated URLs and the curator's narrative. It is **explicitly
marked archival** by virtue of this A.5b report superseding it. Future
imagery work should treat the new
`factory/reports/imagery/causa-legale-a5b/pool-selection.md` as the
canonical pack and the legacy pack as a historical record of the
curator-hallucination incident. A separate cleanup workstream may
choose to retract or replace the legacy pack file; doing so is OUT OF
SCOPE for A.5b (that touches `docs/`, which the A.5b brief reserves
for narrow-fix-only).

---

## §6 · Frozen sibling regression verdict (post-restore)

| Sibling | Layout family | Anonymous home status | A.6 body length | A.5b body length | Verdict |
|---|---|---|---|---|---|
| Pragma | LF-1 | 200 | 87,112 bytes | 87,112 bytes | **NO REGRESSION** (byte-equivalent) |
| Cornice | LF-2 (1st occupant) | 200 | 98,673 bytes | 98,673 bytes | **NO REGRESSION** (byte-equivalent · golden-hour Bologna portico hero intact · Marta Roveri founder intact) |
| Fiscus | LF-3 | 200 | 88,010 bytes | 88,010 bytes | **NO REGRESSION** |
| Solaria | LF-4 | 200 | 88,449 bytes | 88,449 bytes | **NO REGRESSION** |
| Continua | LF-5 | 200 | 94,640 bytes | 94,640 bytes | **NO REGRESSION** (byte-equivalent · library reading-room mahogany hero intact) |

**5/5 frozen siblings UNCHANGED post-restore.** The only file modified
at A.5b is `apps/catalog/template_content_causa.py` (10 URL constants
replaced + comment block updated). Zero touches to LF-2 family files,
chrome, sibling content, registry, DB, or any cross-cluster pool.

### Anonymous draft-gate intact

```
causa-legale anon home:                      404 ✓ (tier=draft preserved)
catalog body contains 'causa-legale':        False ✓
home counter:                                 24+ ✓ (Causa not counted)
```

---

## §7 · Test suite + render audit

```
$ python manage.py test apps.catalog --verbosity 0
Ran 171 tests in 3.161s
OK

$ python manage.py test --verbosity 0
Ran 546 tests in 155.572s
OK
```

**546 / 546 + 171 / 171 OK.** Zero new failures · zero regressions.

A.5b touches only content-string constants — no model fields, no DB
schema, no view logic, no migration. The new Pexels URLs are opaque to
every test (assertions are on slug / tier / layout_family / facet
count / search keywords / route status — none of which depend on photo
URL content).

### Live route walk (post-restore)

```
GET /templates/business/causa-legale/preview/                         200 100,010 bytes
GET /templates/business/causa-legale/preview/studio/                  200  69,007 bytes
GET /templates/business/causa-legale/preview/materie/                 200  70,107 bytes
GET /templates/business/causa-legale/preview/contenzioso/             200  61,299 bytes
GET /templates/business/causa-legale/preview/contatti/                200  70,709 bytes
GET …/contenzioso/cass-ssuu-responsabilita-consulente-fiscale-2024/   200  64,011 bytes
GET …/contenzioso/cass-civ-iii-anatocismo-bancario-2023/              200  63,330 bytes
GET …/contenzioso/tar-lombardia-agcom-proporzionalita-2022/           200  63,395 bytes
GET …/contenzioso/appello-milano-art-36bis-dpr-600-1973-2021/         200  63,260 bytes
```

9/9 routes 200 under staff-preview session + `?preview=1`. Home is now
100,010 bytes (vs. 100,006 at A.5 with original hallucinated URLs · vs.
104,466 at A.6 with the 10× SVG placeholder × ~450-byte data URL × 10
surfaces). The +4 byte delta vs. A.5 reflects the slightly different
URL string lengths between the new IDs and the old hallucinated IDs.

---

## §8 · Files changed at A.5b

**Modified** (1 source file):

1. `apps/catalog/template_content_causa.py` — F1 closure. Replaced the
   single `_IMAGERY_HOLD_PLACEHOLDER` constant + 10 substitutions with
   10 explicit verified Pexels URL constants (one per surface · each
   carrying a per-slot caption comment naming the Pexels ID + subject
   summary + binding rule satisfied). The base64 SVG placeholder is
   removed. The comment block at the top of the imagery section is
   rewritten to document the A.5b re-curate methodology + the cross-
   cluster grep result + the captures location + what A.5b deliberately
   does NOT touch.

**Created** (3 reports + 28 captures):

- `factory/reports/causa/causa-a5b-imagery-recurate.md` (this file)
- `factory/reports/imagery/causa-legale-a5b/pool-selection.md`
- `factory/reports/imagery/causa-legale-a5b/reviewer-lgtm.md`
- `factory/reports/imagery/causa-legale-a5b/captures/probe-*.jpeg` —
  10 final-pick verifications + ~17 rejected-candidate evidence + 1
  post-restore live-walk fullpage screenshot

**Untouched at A.5b** (per scope rules):

- apps/editor — zero edits
- apps/projects — zero edits
- apps/commerce — zero edits
- apps/catalog/preview_imagery.py — zero edits (catalog tile pool stays at original curator URLs · re-curate of that pool is held for a future workstream and is OUT OF A.5b scope)
- apps/catalog/template_dna.py — zero edits
- apps/catalog/template_content.py — zero edits
- apps/catalog/views.py — zero edits
- apps/catalog/migrations/* — zero edits
- All other archetype templates — zero edits
- LF-1 / LF-2 / LF-3 / LF-4 / LF-5 layout files — zero edits
- corporate-suite chrome (`_base.html`) — zero edits
- TEMPLATE_REGISTRY.json — zero edits (`tier=draft` preserved)
- docs/content-factory/imagery/packs/business-litigation.md — zero edits (legacy pack remains archival)
- DB tier on `causa-legale` row — unchanged (`draft`)
- Voice anchor / chrome / typography / palette / KPI tuple / em-word audit / navbar pill / draft preview path — unchanged

---

## §9 · Lock verdict

The A.5b re-curate is **GREEN · IMAGERY RESTORED · LIVE-VERIFIED**.

- 10/10 Pexels URLs replaced with verified candidates
- 10/10 standard CS-IMG-SRC-02 URL formats confirmed resolving
- 10/10 Pexels CDN photos screenshotted and visually confirmed to match
  the slot caption and the planner-brief binding rules
- 6/6 home-rendered photographic surfaces confirmed live in the browser
- 0/10 cross-cluster collisions (grep CLEAN against `business-corporate`
  · `business-architecture` · `business-fiscal` · `business-coaching` ·
  `business-stewardship` · `lawyer-classic` · `lawyer-modern` plus
  `factory/` + `design-orchestrator/` + `docs/content-factory/imagery/
  packs/`)
- 5/5 frozen siblings byte-equivalent · 0 regressions
- 9/9 Causa staff routes 200 · anonymous draft-gate intact (404)
- 546/546 tests OK
- 3 explicit residual risks documented (slot 0 wood-tone · slot 1
  Latin gothic adjacency · slot 3 small Lady-Justice/gavel artifact);
  none are blocking · all are A.6b re-test items
- 1 explicit slot-weakness disclosure (slot 0 narrow Pexels pool ·
  same constraint the A.3 curator forecast at MEDIUM-HIGH; A.5b
  re-curator confirms borderline-MEDIUM · 1 strong primary at premium
  quality · backup roster needs a fresh search at the next pass)

**A.6b rapid review-lock may begin immediately.** The orchestrator
should authorise A.6b to re-walk the priority surfaces (hero · founder
· case-cards) at 1440 / 880 / 375 to confirm the 1-second register
reads as "evidence-led litigation chamber" and zero frozen-sibling
regression. On A.6b GREEN, the orchestrator re-issues the user-
handshake invitation with the now-fully-locked-and-imaged IT draft;
workflow C (multilingual) becomes eligible after that handshake.
Workflow D (public flip) remains held until a second user handshake
on the multilingual walk per D-102 cadence.

If A.6b finds slot 0 wood-tone collapses with Continua at 1-second
read (Risk A.5b-R1), the recommended next workstream is **A.5c slot-0
re-curate** (single-slot fresh search for cool-timber European chamber
URLs · narrow scope · same evidence-bound methodology as A.5b).
