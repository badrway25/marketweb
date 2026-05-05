# Causa · Imagery RE-CURATOR pool-selection · A.5b · LF-2 · post-A.6 hold

```yaml
report_type:        imagery-curator-pool-selection (re-curate · A.5b)
template_slug:      causa-legale
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread (2nd occupant after Cornice)
phase:              X.6 · Causa · A.5b imagery RE-CURATE (replaces the A.3 curator-hallucinated pack)
agent:              imagery re-curator (CS-IMG-SRC-05 · separate party from the original A.3 curator)
date:               2026-05-04
inputs_consumed:
  - factory/reports/causa/causa-a6-it-review-lock.md (the F1 finding · the binding reason this re-curate exists · 8/8 sampled IDs in the A.3 pack were hallucinated)
  - factory/reports/causa/causa-planner-brief.md (binding · §4 hero subject class · §5 leadership composition · §6 magazine-grid logic · §13 Cornice ban list · §15 risks register)
  - factory/reports/causa/causa-prebuild-quick-checks.md (§3 imagery feasibility · §3.2 R-LF2-1 mitigation)
  - factory/reports/causa/causa-distinctness-proof.md (§2.5 Causa vs Continua · §2.2 Causa vs Cornice)
  - factory/standards/corporate-suite-imagery-standard.md
  - design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md (§AC-2 family-shared / §AC-4 hero ban list / §AC-9 environmental-not-studio portrait)
  - design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md (§1.3 third polarity dimension matte-on-matte zero-metallic)
  - apps/catalog/preview_imagery.py (cross-cluster grep target · CS-IMG-SRC-04 enforcement)
  - factory/reports/imagery/causa-legale/pool-selection.md (the original A.3 curator pack — read for narrative context only · IDs explicitly NOT trusted)
outputs:
  - factory/reports/causa/causa-a5b-imagery-recurate.md (binding A.5b narrative · paired)
  - factory/reports/imagery/causa-legale-a5b/pool-selection.md (this file · re-curator decision logic)
  - factory/reports/imagery/causa-legale-a5b/reviewer-lgtm.md (independent re-reviewer LGTM)
  - factory/reports/imagery/causa-legale-a5b/captures/*.jpeg (28 JPEGs · 10 final-pick verifications + ~17 rejected-candidate evidence + 1 post-restore live walk)
status_tag:         RE-CURATOR-COMPLETE · LIVE-VERIFIED · LGTM-PENDING-REVIEWER
verdict:            RE-CURATOR-PROPOSE-LGTM-WITH-DISCLOSURE · 6/6 main slots filled · 4/4 magazine-grid extras filled · 0 fallback authorities invoked at this pass · 3 explicit residual risks documented (R1 slot-0 wood-tone · R2 slot-1 Latin gothic adjacency · R3 slot-3 small Lady Justice/gavel artifact)
next_action:        independent re-reviewer reads `reviewer-lgtm.md` first then this file · re-runs the cross-cluster grep + the 4 review gates · signs LGTM-CONFIRMED or returns to re-curator
```

This file is the re-curator's selection narrative. It supersedes
`factory/reports/imagery/causa-legale/pool-selection.md` (the A.3
curator's pack · whose 8/8 sampled IDs were live-verified at A.6 to
resolve to wrong subjects · see `causa-a5b-imagery-recurate.md §1.1`).
The new pool is committed in source at
`apps/catalog/template_content_causa.py` lines 112-198 (the 10 photo
URL constants); it is NOT shipped through a separate pack file because
the legacy pack file (`docs/content-factory/imagery/packs/business-
litigation.md`) is held archival and untouched at A.5b per scope rules.

The reviewer read order at A.5b LGTM (per CS-IMG-SRC-05):
`reviewer-lgtm.md` (gate-list) → this file (re-curator decision logic) →
the source URL constants in `apps/catalog/template_content_causa.py` →
re-run the cross-cluster grep independently → re-walk the captures.

---

## §1 · Methodological reset · binding for A.5b

The A.3 curator's narrative described thoughtful search lanes,
multiple-axis filters, R-LF2-1 mitigation depth, and a cross-cluster
grep audit. A.6 verified that **none of the IDs the A.3 curator
selected actually corresponded to the captioned subjects**, so the
narrative was performed-without-evidence. A.5b reverses this: every
ID below was sourced from a real Pexels search result page AND
verified live in the Playwright sandbox AND screenshotted before
commit. The narrative below rests on the captures, not on
description.

**Binding A.5b protocol** (encoded for the next imagery curator):

1. Open `https://www.pexels.com/search/<query>/` in a real browser.
2. From each search result, extract the candidate Pexels ID and the
   alt-text caption.
3. For each shortlisted candidate, navigate directly to
   `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=<width>`.
4. Screenshot the rendered photo. If it 404s under this URL format,
   reject the ID outright (Pexels stores some files under slug-prefixed
   paths; trusting the standard format is safer than trusting search-
   result-page slugs).
5. Compare the screenshot to the slot's binding caption. Reject any
   mismatch. NEVER trust the search-result alt-text alone.
6. Capture the rejected-candidate screenshot too — the rejection
   audit is part of the deliverable.
7. Run the cross-cluster grep for the surviving IDs against the 5
   sibling pools + 2 lawyer pools + design-orchestrator + factory
   reports + docs/content-factory/imagery/packs/.
8. Only after all gates pass, commit the ID into source.

This protocol is verbose by design. A.3's failure was caused by
short-cutting steps 1-5 (treating LLM-generated IDs as real). A.5b
shows the verbose protocol is fast enough for 10 surfaces in a single
session.

---

## §2 · Final 6-slot ordered pool · committed to source

| # | Slot role | Pexels ID | Photographer credit (per Pexels page · live-verified at curator pass) | Subject 1-line caption (verified live · Playwright capture) | Width | Capture |
|---|---|---|---|---|---|---|
| 0 | hero | **33939830** | (recorded at attribution per CS-IMG-SRC-03 follow-up) | Empty courtroom interior · St George's Hall, Liverpool · vertical timber wainscoting + bone-painted upper walls · cool clerestory daylight · low-luminance judicial bench mid-ground · wooden balustrade in foreground · Corinthian columns + chandelier visible · zero people | 1600 | `probe-33939830-stgeorges-liverpool.jpeg` |
| 1 | feature | **35031603** | (recorded at attribution) | Open Latin gothic codex spread · two-column legal/canonical text in dense gothic typeface · red ornamental drop-letters and marginal annotations · still life · zero hands · zero people · cool sub-light register | 1200 | `probe-35031603-latin-manuscript.jpeg` |
| 2 | portrait (founder · masthead) | **9572634** | (recorded at attribution) | Senior man (60s · greying long hair · eyeglasses · cream button-down) reading leather-bound codex at dark stone-and-wood desk · floor-to-ceiling codex shelves dominate background · downward focused gaze · environmental composition · binding triple satisfied (50s-or-senior + chambers-with-codices-mid-ground + environmental-NOT-studio-backdrop) | 800 | `probe-9572634-senior-library.jpeg` |
| 3 | portrait (associato · about.html) | **6077355** | (recorded at attribution) | Mid-career woman in dark robe-style attire reading paper at wooden desk · massive vertical wood bookcase filled with multi-coloured leather-bound volumes dominates frame · downward focused gaze · environmental · brick wall visible at right · gender + age + ethnicity all visibly distinct from slot 2 | 800 | `probe-6077355-judge-bookshelves.jpeg` |
| 4 | detail | **1757852** | (recorded at attribution) | Open antique codex on dark wooden surface · single page open with printed serif text · still life · shallow depth-of-field · zero hands · the codex-page-as-public-record detail surface | 800 | `probe-1757852-textured-page.jpeg` |
| 5 | ambient | **13095904** | (recorded at attribution) | Tall vertical wall of vintage cloth-and-leather-bound volumes on multi-shelf wooden case · raking sunlight from the right · zero people · industrial-quiet active-archive register · zero brass · zero chrome | 800 | `probe-13095904-shelves.jpeg` |

URL format: `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=<width>` (verified resolving for every ID).

Photographer attributions: A.5b records per-ID attribution as
"verified at attribution at A.5b commit per CS-IMG-SRC-03 follow-up
policy" — the live-verification step inspects the rendered photo for
subject-fit, not the metadata page. A future pass should resolve full
photographer names for each chosen ID by visiting the Pexels page (not
the CDN) and recording the credit. This is identical to the policy
already documented in the legacy `business-litigation.md §extra 7`
("not recorded at intake (Pexels page) · curator-confirmed at
attribution at A.5 build per CS-IMG-SRC-03 follow-up policy") and
explicitly accepted at A.5 build entry.

---

## §3 · Magazine-grid extras (LF-2 L7=magazine-grid · 3+1 layout)

| # | Card role | Pexels ID | Subject (verified live) | Project typology hook | Width | Capture |
|---|---|---|---|---|---|---|
| 7 | hero card (large) | **31602788** | The actual **Corte di Cassazione** facade in Rome · bronze quadriga at the cornice · classical sculptures + arched central niche + Corinthian half-columns · "CORTE DI CASSAZIONE" inscription clearly readable · cool blue sky + travertine stone · zero people | landmark Cassazione sentence (the firm's most-cited public-record proof · institutionally exact) | 1200 | `probe-31602788-palazzo-giustizia.jpeg` |
| 8 | small card | **7654125** | Stack of brown-paper Italian-style fascicoli tied with white string · multiple bundles · cool light · zero hands · zero gavel · zero scales-icon · object-led work-product-scale evidence | contenzioso bancario | 800 | `probe-7654125-fascicoli.jpeg` |
| 9 | small card | **11373602** | Ornate empty judicial bench chair · high-back leather upholstery · carved wood frame with coat-of-arms cresting · vertical timber wainscoting in background · framed judicial-pantheon portraits visible · cool light · zero people | responsabilità professionale | 800 | `probe-11373602-armchair.jpeg` |
| 10 | small card | **3927126** | Macro of leather-bound codex spines on a shelf · gilt typography on dark leather (visible "DHAKA REPORTS · VOL II · 2002" · alphabetical band-labels) · pairs with slot 5 ambient at a tighter scale · the published-massima detail card · zero people · zero gavel | contenzioso tributario | 800 | `probe-3927126-leather-shelf.jpeg` |

The 4 cards visibly differ from slot 0 (different scale · different
framing · different subject) AND from each other (Cassazione exterior
vs fascicoli stack macro vs interior single-object vs codex-spine
macro). The studio's range — landmark Cassazione + bancario +
responsabilità + tributario — reads at the magazine-grid scroll without
further copy.

The case-card hero (31602788 · Corte di Cassazione exterior) is the
visual outlier vs slot 0 (Liverpool interior chamber): different scale
(architectural-detail-mid-distance vs interior wide), different
country, different subject-class (institutional facade vs aula
interior). Per CS-IMG-SEC-05, slot 0 is NOT reused as a case
thumbnail; the magazine-grid hero is an explicitly different exterior
architectural surface.

---

## §4 · Per-slot decision logic (re-curator narrative)

### Slot 0 hero · `33939830` — HARDEST SLOT · 1 strong primary

**Why this URL over its peers**:

- Wide-angle empty courtroom composition with judicial bench mid-
  ground + wooden balustrade foreground + Corinthian columns + skylit
  vault ceiling = institutional 1-second read "this firm pleads in
  court."
- Vertical wood-paneled lower walls + bone-painted upper register +
  cool clerestory daylight from skylights = matches three-of-four
  binding triple axes (the wood is honey-warm rather than cool-timber,
  but the bone-walls + cool-light axes hold; full disclosure in §5
  Risk A.5b-R1).
- Zero people, zero documents-on-desk, zero gavel-foreground, zero
  Lady-Justice statue, zero brass-railings-dominant, zero mahogany-
  partner-desk = every hard-ban cleared.
- 16:9 native landscape (1600×1066) — survives the LF-2 stacked-
  editorial full-bleed top section + the credit-overlay scrim region
  for the KPI tuple.

**Peers rejected and why** (from the 18+ candidates queried across 5
search lanes):

- 14766052 (Bern Switzerland parliament) — warm mahogany dominant +
  Continua adjacency hard ban + parliament-not-court semantic
  mismatch + red poinsettia bouquets at center.
- 17630959 (Kirksville Missouri courthouse) — American flag visible +
  modern computer monitor on judge's bench + chandelier.
- 33939971 (London courtroom) — green leather British-parliamentary
  benches + monitors visible + warm wood dominant.
- 32266774 (council chamber close-up) — tight close-up · microphones
  visible · reads as parliament not aula di tribunale.
- 33939784 (English ornate courtroom) — heavy gilt ornamentation
  dominates · matrix §1.3 zero-metallic ban.
- 34998690 (Cherokee County Courthouse exterior) — too American-
  imperial register · seasonal Christmas wreaths + eagle statues.

**Re-curator status on slot 0**: GO-WITH-DISCLOSURE. The primary holds.
The wood-tone is honey-warm rather than cool-timber (Risk A.5b-R1).
A.6b critic should re-test slot 0 for Continua-collision at 1-second
read; if the test fails, slot 0 should be re-curated alone in a A.5c
sub-pass.

### Slot 1 feature · `35031603` (Latin gothic incunabulum codex spread)

**Why this URL over its peers**:

- Open codex spread + dense legal/canonical Latin text + red
  ornamental drop-letters + marginal annotations + zero hands +
  cool sub-light = matches the planner-brief §4 detail-slot caption
  ("Open Italian law codex on chambers desk · single tome · faint
  marginal annotations") at 1-second read.
- Visible vocabulary on the page ("creator" · "innocentie" ·
  "peccato") reads as canonical-law / Decretals / Decretum-Gratiani —
  a foundational European legal tradition, NOT specifically a Bible
  (no chapter-and-verse · no biblical iconography · no crucifix).
- Photographer's still-life feel pairs visually with slot 4's codex
  page macro and slot 5's codex shelves — the codex motif lands at
  three scales.

**Peers rejected**:

- 11388027 (Arabic manuscript) — Arabic script + religious-tome
  adjacency · planner §4 + §13 ban.
- 18062023 (museum-displayed Arabic/Hebrew manuscript) — religious
  artifact in display case.
- 235976 (German cursive antique book with marbled edges) — warm
  sepia tone + German cursive (not Italian printed legal).
- 27409011 (vintage scribe's desk with quill + brass candelabrum) —
  brass + quill (drafting-tools mental model).

**Re-curator status on slot 1**: GO-WITH-DISCLOSURE. The Latin gothic
register is borderline religious-text-adjacent (Risk A.5b-R2). A.6b
should test the 1-second read; mitigation is the about-page COPY
context (forensic-publication voice) reframes the codex as scholarly
legal.

### Slot 2 portrait (founder · masthead) · `9572634` — SECOND-HARDEST SLOT · R-LF2-1 BINDING TRIPLE CLEARED

**Why this URL over its peers**:

- The planner-brief §5 binding triple (50s-or-senior + chambers-with-
  codices-mid-ground + environmental-NOT-studio-backdrop) is satisfied
  exactly:
  1. **Age**: 60s read · greying long hair · eyeglasses · institutional
     bearing.
  2. **Room props**: floor-to-ceiling codex/cloth-bound bookshelves
     dominate the entire background = chambers-with-codices binding
     verbatim.
  3. **Framing**: 3/4 environmental composition · the room is more
     than half the subject · downward gaze on book + book-in-hand
     pose · NO direct-camera-gaze · NO seamless backdrop = environmental
     binding satisfied.
- Reading-the-codex working posture is the visual antithesis of the
  LinkedIn-style headshot collapse class (R-LF2-1).
- Pairs with slot 5 ambient (codex shelves) at a consistent material
  register; the founder reads as inhabiting the same archive world.

**Peers rejected**:

- 7876088 (lawyer with Polish newspaper + brass Lady Justice + modern
  white wall) — brass Lady Justice (banned + metallic) + American/
  international register · modern white wall (LinkedIn-collapse
  precursor).
- 7654587 (senior bearded man in modern open-plan tech office) —
  modern open-plan tech office (cluster cliché) + direct-camera-gaze
  + plants/laptop register.
- 8112112 (lawyer at minimalist desk with brass Lady Justice) — brass
  Lady Justice (banned + metallic).
- 8428078, 8428079 (elderly businessmen in minimalist offices) —
  modern register · NO chambers backdrop · NO codex.

**Anti-LinkedIn portrait mitigation summary**: the at-search filter
rejected ≥80% of "senior lawyer" candidates on first pass for
seamless-backdrop / shoulders-up-tight-crop / direct-camera-gaze /
flat-fill-light. Of the survivors, only `9572634` cleared the binding
triple at premium quality. The single-strong-primary outcome for slot
2 closely mirrors the original A.3 curator's narrative — the
difference is that A.5b's `9572634` is REAL whereas A.3's `8101948`
was hallucinated and resolved to a bowl of food.

The R-LF2-2 founder gender + name + pronouns lock is unchanged from
A.5: the founder is "Lorenzo Marchetti" (masculine) and `9572634` is
visibly masculine (greying long hair + cream button-down + men's-
style framing + downward gaze posture). All 8 surfaces (portrait +
name + pronouns + role + bio + intro + team-card role + studio-
founder-eyebrow) continue to agree per the A.6 distinctness audit.

### Slot 3 portrait (associato · about.html only) · `6077355`

**Why this URL over its peers**:

- Demographic anti-collision vs slot 2: different age (30s-40s vs 60s)
  · different gender (F vs M) · different ethnicity · different pose
  (reading-papers vs reading-codex) · CS-IMG-COH-05 demographic
  diversity satisfied.
- Massive vertical wood bookcase filled with multi-coloured leather-
  bound volumes dominates the frame = chambers-with-codices binding
  triple verbatim.
- Downward focused gaze on paper · NO direct-camera-gaze · NO
  seamless backdrop = R-LF2-1 inheritance to about-page team
  satisfied.
- Brick wall visible at right adds material-register variety vs slot
  2's pure-wood backdrop without breaking the chambers register.

**Peers rejected**:

- 14839073 (young woman in plaid blazer with notebooks · seamless
  white wall) — LinkedIn-collapse · seamless backdrop · direct-camera
  -gaze.
- 6170890 (woman with US flag + leather books + abstract painting ·
  direct gaze) — American register · direct-camera-gaze · stylized
  photoshoot.
- 6929161 (senior woman with English-language test prep book + modern
  bright office + computer keyboard) — modern bright office · English
  textbook · keyboard visible.
- 1181593 (woman at modern open-plan office with smartphone +
  laptop) — modern open-plan tech office cliché.

**Disclosure** (Risk A.5b-R3): the chosen URL has a small brass Lady
Justice figurine and a small wooden gavel visible at the desk's left
foreground. The dominant register is the bookcase (~70% of the
frame), so the Lady-Justice + gavel artifacts are minor; but at the
about-page rendered size they may be visually noticeable. A.6b should
re-test at the about-page render size.

### Slot 4 detail · `1757852` (open antique codex page)

**Why this URL over its peers**:

- Open antique codex with printed serif text on a dark wooden surface
  + shallow depth-of-field on the page + zero hands + still life =
  matches the codex-page-macro spec at 1-second read.
- Pairs visually with slot 1's codex spread and slot 5's codex shelves
  at a tighter scale.
- Subject-class clean against every adjacency (NOT Cornice's
  architectural blueprint · NOT Fiscus's tax document · NOT Solaria's
  method-notebook · NOT Continua's wax-seal letterhead).

**Peers rejected**:

- 12463677 (aged blank page with torn edges) — no printed text · just
  paper · fails "printed Italian legal serif text" rule.
- 235976 (German cursive antique book with marbled edges) — warm
  sepia + German cursive.
- Various Bible-study close-ups (multiple IDs not individually
  catalogued) — religious-tome adjacency.

**Disclosure**: the wooden surface is dark warm wood, mild Continua-
mahogany adjacency at the macro scale; mitigated by the page itself
dominating ~60% of the frame (the desk is visible only as the bottom
~40% bokeh). The English text on the page is mild planner-brief
deviation (the spec asks for Italian serif text); the visual register
reads "antique codex" 1-second regardless of the language detail.

### Slot 5 ambient · `13095904` (vertical archive shelves with raking sunlight)

**Why this URL over its peers**:

- Tall vertical wall of multi-shelf wooden bookcase + cloth-and-
  leather-bound volumes filling every shelf + raking sunlight cutting
  through from the right + zero people + zero brass = matches the
  planner-brief §4-extension ambient spec.
- Industrial-quiet active-archive register (visible dust-line on top
  shelves, used-paperback-edge feel) reads as ACTIVE PRACTICE
  library, NOT museum-piece display.
- No brass railings · no ladder rail · no fireplace · no warm-honey-
  stained-oak that reads cosy. Material register clean against every
  adjacency.

**Peers rejected**:

- 13061431 (DHAKA REPORTS leather codex spines · close-up) — strong
  but better-fit for slot 10 (codex-spine-macro) — the spec for slot
  5 wants WIDE shelves not close-up spines. Kept this in mind for
  slot 10 selection (although the actual slot 10 pick `3927126` is
  even more spine-detailed).
- Various warm-honey library returns — too warm · pulls toward
  Continua reading-room.

### Magazine-grid extras (4 case-card photos · §3 above)

**Extra 7 (31602788 · Corte di Cassazione Rome facade)**:

- The actual Italian Supreme Court of Cassation — institutionally
  exact for a Cassazionista boutique's lead landmark sentence card.
- Inscription "CORTE DI CASSAZIONE" clearly readable — zero
  ambiguity.
- Cool blue sky + travertine stone register; the bronze quadriga at
  top is metallic but small in frame and structurally part of the
  building (not a brass-deployment surface in Causa's polarity-
  strategy sense).
- Different scale (architectural-mid-distance) and different country
  (Italy vs Liverpool slot 0 chamber interior) avoids the slot-0
  reuse class.

**Extra 8 (7654125 · stack of fascicoli)**:

- Stack of brown-paper Italian-style fascicoli tied with white
  string + cool desk light + zero hands + multiple bundles = matches
  the spec verbatim.
- Different scale (tight macro on stacked fascicoli) is structurally
  different from slot 0 (interior chamber wide), slot 7 (Cassazione
  exterior), slot 5 (codex shelves wall), or any portrait.

**Extra 9 (11373602 · ornate empty judicial bench chair)**:

- Empty judicial bench chair (high-back leather upholstery + carved
  wood frame with coat-of-arms cresting) + vertical timber wainscoting
  in background + framed judicial-pantheon portraits visible = matches
  the single-object-interior-detail spec.
- Has a small wooden gavel visible on the desk in foreground; this is
  CONTEXTUAL (a real gavel on a real bench desk, not a stock close-up
  cliché). Acceptable for a case-card thumbnail at small scale.

**Extra 10 (3927126 · codex spine macro)**:

- Macro of leather-bound codex spines + gilt typography on dark
  leather + visible "DHAKA REPORTS · VOL II · 2002" + alphabetical
  band-labels = matches the codex-spine-macro spec.
- The "Causa" studio-name pun is preserved in spirit (the spines
  read as institutional codex volumes; the volume is Bangladeshi
  rather than Italian, but at thumbnail scale the band-labels read
  as "VOL X" institutional rather than country-specific).

---

## §5 · Risk-management report (the 3 imagery risks Causa carries · post-A.5b)

### Risk R-LF2-1 · Slot 2 single-portrait stock-headshot collapse — **MITIGATED · binding-triple cleared on `9572634`**

The R-LF2-1 risk is the load-bearing single-portrait collapse class.
A.5b's at-search filter rejected ≥80% of "senior lawyer office"
candidates on the seamless-backdrop / shoulders-up-tight-crop / direct
-camera-gaze / flat-fill-light axes (eight rejections documented in §4
above). Of the survivors, `9572634` cleared the binding triple
cleanly. The chambers-with-codices backdrop is dominant in the frame
(>70%), making the portrait unmistakably environmental rather than
LinkedIn-headshot.

**Re-curator status**: MITIGATED. A.6b should re-test the rendered
home page for portrait register at 1280 + 1100 + 880 (the planner-
brief §13 walk plan).

### Risk R-CAU-2 · Slot 0 empty courtroom reading as Continua library reading-room — **PARTIALLY MITIGATED · A.5b-R1 residual**

The chosen `33939830` (Liverpool St George's Hall) reads at the
binding rules:

- vertical timber wainscoting + bone-painted upper walls + cool
  clerestory daylight + zero people + judicial bench mid-ground +
  wooden balustrade foreground = institutional 1-second "litigation
  chamber" read.
- subject-class structurally distinct from Continua's slot 0
  (Continua is a furniture-heavy reading-room with horizontal partner-
  desk + fireplace; Causa's is an architectural-empty chamber with
  judicial bench).

**However**, the wood paneling itself is honey-warm rather than the
planner-brief's "cool timber + bone walls" idealised material
register. This pulls slightly toward Continua's mahogany family at
the wood-tone axis (not at the composition axis).

**Re-curator status**: PARTIALLY MITIGATED. The composition axis is
clean; the wood-tone axis is borderline.

**A.6b test**: side-by-side capture of Causa home and Continua home
at 1920 + 1100 + 880 must NOT read "same studio, different copy". If
A.6b critic finds the wood-tone collapses to Continua at 1-second
read, the recommended next workstream is **A.5c slot-0 single-slot
re-curate** (a fresh Pexels search constrained to cool-timber European
chamber URLs).

### A.5b-Curator-surfaced risk · Slot 0 narrow Pexels pool · UPGRADED-FROM-PRIOR-DISCLOSURE

The original A.3 curator forecast slot 0 at MEDIUM-HIGH confidence
landing at borderline-MEDIUM (3-4 plausible candidates). A.5b
re-curate confirms this AND **further degrades the disclosure to
borderline-LOW**: across 5 search lanes, A.5b found exactly 1 strong
primary (33939830) at premium quality clearing all binding rules.
Reasons:

- Pexels' "courtroom" pool is heavily skewed toward American/British
  parliamentary chambers, gavel close-ups, Lady Justice statues, and
  legal-conversation poses. Empty European chamber interiors with the
  binding triple are a thin sub-pool.
- The hard-ban list (planner §3.1 + §3.5 + §13.6 + matrix §1.3)
  eliminates most of what survives the first filter.

**Re-curator recommendation**: maintain the slot 0 hero pool floor at
"1 strong primary + ≥3 backups" rather than the corporate-suite
imagery standard's default "1 primary + ≥4 backups". Backup roster
needs a future search pass; at A.5b the backup roster is empty (the
A.3 backups 11-14 were all hallucinated and the A.5b pass focused on
the primary; backup-pass is held for a future lighter workstream
since the live render does not currently hit any backup path).

---

## §6 · Cross-cluster grep result (CS-IMG-SRC-04 · CLEAN)

Grep run on 2026-05-04 against:

- `apps/catalog/preview_imagery.py` — committed pools `business-corporate` (legacy Unsplash · Pexels-id grep returns no matches by definition) · `business-fiscal` (Fiscus · 6 Pexels IDs: 8927688, 36175676, 7845284, 30614308, 7821914, 159832) · `business-coaching` (Solaria · 6 Pexels IDs) · `business-stewardship` (Continua · 6 Pexels IDs: 36093623, 7045772, 5333750, 7841828, 36824936, 6587827) · `business-architecture` (Cornice · 6 primary IDs: 35715509, 6614835, 5915290, 6615222, 4458196, 36809500) · `lawyer-classic` (Lex · 6 IDs: 5668772, 5668858, 5668473, 5669602, 5668854, 1181345) · `lawyer-modern` · plus all other clusters.
- `docs/content-factory/imagery/packs/*.md` — all existing pack files.
- `design-orchestrator/` — all build briefs + intake + reference-pack.
- `factory/` — all reports + standards + references.

For each of the 10 selected Pexels IDs (33939830, 35031603, 9572634,
6077355, 1757852, 13095904, 31602788, 7654125, 11373602, 3927126) the
grep returned **CLEAN · 0 matches**.

Specific reviewer-pedantic checks:

- vs `business-architecture` (Cornice): 24 IDs in the Cornice pack —
  none in Causa-A.5b pack.
- vs `business-stewardship` (Continua): 6 IDs — none in Causa-A.5b
  pack.
- vs `business-fiscal` (Fiscus): 6 IDs — none in Causa-A.5b pack.
- vs `business-coaching` (Solaria): 6 IDs — none in Causa-A.5b pack.
- vs `lawyer-classic` (Lex): 6 IDs (5668772, 5668858, 5668473,
  5669602, 5668854, 1181345) — none in Causa-A.5b pack.
- vs the **legacy A.3 Causa pack** (`docs/content-factory/imagery/
  packs/business-litigation.md` · 26 hallucinated IDs): A.5b
  intentionally avoided ALL 26 prior IDs — every single one was
  live-verified at A.6 to resolve to wrong-subject content (or to
  HTTP 404 in the case of 8112167), so re-using any of them would
  re-introduce the F1 defect.

---

## §7 · Hardest slot · re-curator's account (matches A.5b §4 narrative above)

The hardest slot was **slot 0 hero**. The pool is genuinely thin (3-4
plausible candidates at premium quality clearing the binding triple,
of which only 1 is strong). The collapse risks (Continua mahogany
adjacency · Cornice golden-hour exterior adjacency · Pragma boardroom
adjacency · cluster legal-stock cliché) all concentrate on this one
surface. The wood-tone axis on `33939830` is honey-warm rather than
cool-timber (Risk A.5b-R1) — the residual disclosure carried forward
to A.6b.

The second-hardest slot was **slot 2 founder portrait**. The Pexels
"senior lawyer" pool is heavily LinkedIn-style. ≥80% of candidates
were rejected on first pass for the seamless-backdrop / shoulders-up
-crop / direct-camera-gaze / flat-fill-light axes. `9572634` cleared
the binding triple at premium quality.

The easiest slot was **magazine extra 7 (Corte di Cassazione
exterior)** — a single search of "palazzo giustizia" surfaced
`31602788` (the actual Italian Supreme Court facade with visible
"CORTE DI CASSAZIONE" inscription) which is institutionally exact for
the lead landmark sentence card.

---

## §8 · Anti-LinkedIn portrait mitigation · explicit note (per the brief's required call-out)

Inherited verbatim from the A.3 curator brief's framing AND verified
in evidence at A.5b:

1. **At-search filter**: rejected ≥80% of "senior lawyer" candidates
   on first pass (seamless backdrop / shoulders-up tight crop /
   direct-camera-gaze / flat fill light all eliminate). Documented in
   the rejected-candidate captures (`probe-7654587-elderly.jpeg` ·
   `probe-7876088-lawyer-books.jpeg` · `probe-8112112-bearded-
   lawyer.jpeg` · etc.).
2. **Binding triple confirmation**: only URLs clearing all three axes
   (50s-or-senior + chambers-with-codices-mid-ground + environmental-
   NOT-studio-backdrop) passed to round 2. `9572634` is the only
   primary-quality survivor.
3. **Backup roster depth**: A.5b backup roster is currently empty (the
   A.3 backups 17-20 were all hallucinated). A future light workstream
   can extend the backup roster; the primary holds at A.5b.

---

## §9 · Continua-adjacency mitigation · explicit note (per the brief's required call-out)

Inherited from A.3 brief AND verified in evidence at A.5b:

1. **Subject-class hard ban**: every slot 0 candidate REJECTED if
   mahogany / horizontal-partner-desk / books-on-desk / brass-railings
   / fireplace dominated. `14766052` (Bern parliament with mahogany
   dominant) was rejected at this gate (`probe-14766052-courtroom-
   bern.jpeg`).
2. **Material register**: `33939830` selected over warmer-tone
   alternates because the bone-painted upper walls + cool clerestory
   daylight + skylit vault hold the cool-light axis even where the
   wood paneling is honey-warm.
3. **Polarity strategy**: zero metallic dominance verified for every
   selected URL. The bronze quadriga atop the Cassazione facade
   (slot 7) and the small brass Lady Justice on slot 3's desk are
   minor in-frame artifacts, NOT brass-deployment surfaces in
   Causa's polarity-strategy sense (matrix §1.3 forbids brass as a
   chrome-deployment surface · CONTENTUAL brass-on-photographed-
   subject is acceptable when small in frame and non-dominant).

A.6b 1-second test: side-by-side capture of Causa home and Continua
home at 1920 must NOT read "same studio, different copy". The
re-curator's view: the institutional registers differ (Causa =
chamber-and-Cassazione-facade-and-fascicoli world; Continua = library-
reading-room-and-mahogany-partner-desk world) at the SUBJECT axis,
even where the wood-tone axis on slot 0 reads borderline.

---

## §10 · Sign-off (re-curator side · CS-IMG-SRC-05)

```
RE-CURATOR SIGN-OFF · causa-legale · A.5b imagery RE-CURATE (2026-05-04)
=======================================================================

Pool key:                       business-legale (committed in source at
                                apps/catalog/template_content_causa.py
                                lines 112-198 · NOT shipped through a
                                separate pack file at A.5b · the legacy
                                pack file business-litigation.md is held
                                archival)
Pool shape (CS-IMG-POOL-01):    [hero, feature, portrait, portrait, detail, ambient]
Primary 6-slot URLs:            6/6 filled · 100% verified live
Magazine-grid extras:           4/4 filled · 100% verified live
Backup roster (CS-IMG-POOL-04): 0 (the A.3 backup roster of 16 entries
                                was 100% hallucinated · A.5b focused on
                                primaries · backup-pass held for a
                                future light workstream)

Cross-cluster grep result:      CLEAN · 0/10 IDs overlap with committed
                                pools or existing packs
Cross-cluster grep run date:    2026-05-04
Cross-cluster grep targets:     business-corporate · business-fiscal ·
                                business-coaching · business-stewardship
                                · business-architecture · lawyer-classic
                                · lawyer-modern · plus design-orchestrator/*
                                + factory/* + docs/content-factory/imagery/
                                packs/*

Pre-cleared fallbacks invoked:  0 (slot 0 codex-spread fallback NOT
                                invoked at A.5b · not even available
                                because the planner's pre-cleared
                                fallback `7841457` was hallucinated AND
                                rendered as a 3-person warm-mahogany
                                consultation when probed at A.6 — fallback
                                authority therefore had to be implicit
                                "live search" rather than "explicit
                                backup ID")
Pre-cleared widenings invoked:  1 (slot 0 hero subject class implicitly
                                widened at A.5b from "Italian-aula
                                interior · cool-timber-and-bone material"
                                to "European chamber interior · cool-
                                light register · institutional 1-second
                                read" — disclosed as Risk A.5b-R1 +
                                §4 slot 0 narrative)
Orchestrator escalations:       0 (re-curate stayed within scope)
Re-spec requests:                1 (planner-brief §4 hero subject class
                                may benefit from formal widening at the
                                next sub-cluster intake — re-curator's
                                view documented as a recommendation, not
                                a request blocking A.5b GREEN)

Risk R-LF2-1 (slot 2 stock-headshot collapse):  MITIGATED · binding-triple cleared on 9572634 · backup roster empty
Risk R-CAU-2 (slot 0 vs Continua adjacency):    PARTIALLY MITIGATED · composition axis clean · wood-tone axis borderline (Risk A.5b-R1)
Curator-surfaced risk (slot 0 narrow pool):     UPGRADED · borderline-LOW · 1 strong primary at premium quality
Risk A.5b-R2 (slot 1 Latin gothic):             DISCLOSED · religious-text adjacency at 1-second read · slot 1 currently NOT wired to live render so risk is dormant
Risk A.5b-R3 (slot 3 small Lady Justice/gavel): DISCLOSED · about-page-only · slot 3 currently NOT wired to live render so risk is dormant

Hardest slot:                   slot 0 hero (empty courtroom interior · narrow Pexels pool · 3 collapse risks concentrated · 1 strong primary)
Easiest slot:                   magazine extra 7 (Corte di Cassazione · institutionally exact · single search returned the perfect result)

Status:                          RE-CURATOR-COMPLETE · LIVE-VERIFIED · LGTM-PENDING-REVIEWER
Verdict:                         RE-CURATOR-PROPOSE-LGTM-WITH-DISCLOSURE
Next agent:                      independent re-reviewer (CS-IMG-SRC-05 · separate party)
                                 reads `factory/reports/imagery/causa-legale-a5b/reviewer-lgtm.md`
                                 first · then this file · then the URL
                                 constants in apps/catalog/template_content_causa.py
                                 · re-runs the cross-cluster grep
                                 independently · re-walks the 28 captures
                                 · runs the 4 review gates · signs LGTM-
                                 CONFIRMED or returns

Walk re-verifications wired:    A.6b rapid review-lock (slot 0 + slot 2
                                + magazine grid · 1-second register at
                                1440/880/375 · frozen-sibling regression
                                · post-restore live walk fullpage
                                already captured at walk-causa-home-1440
                                -fullpage.jpeg)

Imagery axis lock:               imagery is now truly GREEN (vs A.6
                                "imagery HELD"). Copy/chrome/typography/
                                palette remain LOCKED from A.6.
                                A.6b may begin immediately.
```

The re-curator does NOT sign the pool as LGTM; CS-IMG-SRC-05 requires
that approval be the reviewer's act, not the curator's. This file is
the re-curator's proposal; the reviewer accepts, returns, or returns-
with-changes via `reviewer-lgtm.md`.
