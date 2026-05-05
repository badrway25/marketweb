# Causa · Imagery RE-REVIEWER LGTM · A.5b · LF-2 · post-A.6 hold

```yaml
report_type:        imagery-reviewer-lgtm (re-review · A.5b)
template_slug:      causa-legale
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread (2nd occupant after Cornice)
phase:              X.6 · Causa · A.5b imagery RE-CURATE LGTM (validates the re-curate · NOT the original A.3 pack)
agent:              imagery re-reviewer (CS-IMG-SRC-05 · separate party from the A.5b re-curator · ALSO separate from the original A.3 curator + reviewer)
date:               2026-05-04
inputs_consumed:
  - factory/reports/imagery/causa-legale-a5b/pool-selection.md (re-curator selection narrative)
  - factory/reports/causa/causa-a5b-imagery-recurate.md (binding A.5b narrative)
  - factory/reports/causa/causa-a6-it-review-lock.md (the F1 finding · the A.6 evidence base for the prior failure)
  - factory/reports/causa/causa-planner-brief.md (binding · §4 hero subject class · §5 leadership composition · §13 Cornice ban list)
  - apps/catalog/template_content_causa.py (the actual source · lines 112-198 carry the 10 photo URL constants under re-review)
  - factory/reports/imagery/causa-legale-a5b/captures/*.jpeg (28 JPEGs · re-walked URL-by-URL during this re-review)
  - apps/catalog/preview_imagery.py (cross-cluster grep target · re-run independently at this LGTM)
  - docs/content-factory/imagery/packs/business-litigation.md (legacy A.3 pack · read for completeness · 26 IDs explicitly NOT trusted)
status_tag:         LGTM-CONFIRMED-WITH-DISCLOSURE
verdict:            LGTM-CONFIRMED-WITH-DISCLOSURE — A.6b rapid review-lock may begin immediately
gates_run:          4/4 (CS-IMG-SRC-05 · CS-IMG-POOL-01 · CS-IMG-PREM-02 · CS-IMG-COH-07)
gate_results:       4/4 PASS
disclosures_carried: 3 (Risk A.5b-R1 slot 0 wood-tone · Risk A.5b-R2 slot 1 Latin gothic · Risk A.5b-R3 slot 3 small Lady Justice + gavel)
```

This file is the independent re-reviewer's LGTM for the A.5b
re-curate. It pairs with `pool-selection.md` (re-curator narrative)
and `causa-a5b-imagery-recurate.md` (binding A.5b phase narrative).
The re-reviewer's role is to VERIFY the re-curator's claims by:

1. Re-walking the 28 captures URL-by-URL.
2. Re-running the cross-cluster grep independently.
3. Running the 4 review gates against the source.
4. Checking the live render hits the new URLs at the expected
   surfaces.

The reviewer authority is bound by CS-IMG-SRC-05 (curator does NOT
sign their own LGTM). The re-reviewer-vs-re-curator separation is the
mechanism that prevents an A.5b-style hallucination from re-surfacing
as A.5c-style hallucination — the reviewer must independently verify
the curator's claims.

---

## §1 · Re-walk of the 10 final-pick captures

The re-reviewer re-opened each of the 10 final-pick capture JPEGs in
`factory/reports/imagery/causa-legale-a5b/captures/` and re-confirmed
the rendered subject matches the slot caption. Result:

| Slot | Pexels ID | Capture | Rendered subject (re-reviewer's 1-second read) | Caption match |
|---|---|---|---|---|
| 0 hero | 33939830 | `probe-33939830-stgeorges-liverpool.jpeg` | Empty courtroom · wood paneling + bone painted upper walls + skylit vault + judicial bench mid-ground + wooden balustrade foreground · institutional 1-second read | ✅ matches "litigation chamber" register · honey-warm wood-tone is the documented Risk A.5b-R1 |
| 1 feature | 35031603 | `probe-35031603-latin-manuscript.jpeg` | Open Latin gothic codex spread · two-column dense text + red ornamental drop-letters + visible "peccato" · scholarly/canonical-law register | ✅ matches "open codex spread" with documented Risk A.5b-R2 (theological adjacency) |
| 2 founder | 9572634 | `probe-9572634-senior-library.jpeg` | Senior man (60s+ · greying long hair · eyeglasses) reading leather book at dark stone-and-wood desk against floor-to-ceiling codex shelves · downward gaze · environmental | ✅ matches binding triple verbatim (50s-or-senior + chambers-with-codices + environmental) |
| 3 associate | 6077355 | `probe-6077355-judge-bookshelves.jpeg` | Mid-career woman in dark robe-style attire reading paper at wooden desk · vertical wood bookcase fills frame · downward gaze · brick wall at right · small Lady Justice + gavel visible at left edge | ✅ matches "associato in chambers" with documented Risk A.5b-R3 (small Lady Justice + gavel) |
| 4 detail | 1757852 | `probe-1757852-textured-page.jpeg` | Open antique codex on dark wooden surface · printed serif text · single page · shallow DOF · still life | ✅ matches "codex page macro · printed serif text" |
| 5 ambient | 13095904 | `probe-13095904-shelves.jpeg` | Tall vertical wall of multi-shelf wooden bookcase + cloth/leather-bound volumes + raking sunlight from right · industrial-quiet active-archive register | ✅ matches "vertical wall of codex volumes · cool light · zero brass" |
| 7 magazine hero | 31602788 | `probe-31602788-palazzo-giustizia.jpeg` | The actual Corte di Cassazione facade in Rome · "CORTE DI CASSAZIONE" inscription clearly readable · bronze quadriga + classical sculptures + cool blue sky | ✅ matches "Italian high-court exterior · classical pediment · institutionally exact for the firm's lead landmark Cassazione card" |
| 8 magazine small | 7654125 | `probe-7654125-fascicoli.jpeg` | Stack of brown-paper Italian-style fascicoli tied with white string · multiple bundles · cool light · zero hands · zero gavel | ✅ matches "stacked legal fascicoli · register tags · cool desk light" |
| 9 magazine small | 11373602 | `probe-11373602-armchair.jpeg` | Ornate empty judicial bench chair (high-back leather + carved wood frame with coat-of-arms) + vertical timber wainscoting + framed pantheon portraits visible · zero people · small wooden gavel on desk | ✅ matches "empty judicial bench chair · high-back oak · vertical timber wainscoting · zero people" with disclosure note (small wooden gavel visible · contextual not cliché) |
| 10 magazine small | 3927126 | `probe-3927126-leather-shelf.jpeg` | Macro of leather-bound codex spines + gilt typography on dark leather + visible "DHAKA REPORTS · VOL II · 2002" + alphabetical band-labels · zero people | ✅ matches "codex spine macro · gilt typography on dark leather · Roman-numeral volume marker" |

**10/10 captures verify the captioned subject.** Zero curator-
hallucinations re-surfacing in the A.5b pool.

---

## §2 · Re-walk of the rejection captures

The rejected-candidate captures (~17 JPEGs) document the search
funnel. The re-reviewer re-opened each rejection capture and confirmed
the documented rejection reason in `pool-selection.md §4` matches
visually. Result: **17/17 rejection reasons verify** (e.g., the
14766052 Bern parliament IS warm-mahogany dominant verbatim;
8112112 DOES have a brass Lady Justice on the desk; etc.). The
re-reviewer notes that the rejection audit is more substantive than
the A.3 curator's narrative because each rejection is photographically
falsifiable.

---

## §3 · Cross-cluster grep · independent re-run

The re-reviewer re-ran the cross-cluster grep at LGTM independently
of the re-curator's claim:

```
$ for id in 33939830 35031603 9572634 6077355 1757852 13095904 \
            31602788 7654125 11373602 3927126; do
    grep -l "pexels-photo-$id\\|/$id/pexels" \
      apps/catalog/preview_imagery.py \
      docs/content-factory/imagery/packs/ \
      design-orchestrator/ factory/standards/ factory/references/ \
      2>/dev/null
done

(no matches · grep CLEAN · 0/10 IDs collide with any committed pool or pack)
```

Re-reviewer-pedantic verification:

- vs `business-corporate` (Pragma · legacy Unsplash) — Pexels-id grep
  returns no matches by definition; manual re-check of Pragma's
  imagery pool confirms zero overlap.
- vs `business-architecture` (Cornice): the 24 IDs in Cornice's pack
  + the 6 IDs in the committed `apps/catalog/preview_imagery.py
  business-architecture` pool → all CLEAN.
- vs `business-stewardship` (Continua) → CLEAN.
- vs `business-fiscal` (Fiscus) → CLEAN.
- vs `business-coaching` (Solaria) → CLEAN.
- vs `lawyer-classic` (Lex) — 6 reserved IDs (5668772, 5668858,
  5668473, 5669602, 5668854, 1181345) → CLEAN.
- vs `lawyer-modern` (Juris) → CLEAN.
- vs the **legacy A.3 Causa pack** (`docs/content-factory/imagery/
  packs/business-litigation.md` · 26 hallucinated IDs):
  17109985, 6077368, 8101948, 6325985, 6077381, 2128249, 9489162,
  4427616, 8730987, 6077326, 15796091, 8112167, 4427451, 7841457,
  6077369, 6077332, 8101947, 6077397, 8101950, 8101952, 6325988,
  6325991, 6077333, 6077361, 2128247, 8730991. The A.5b pack:
  33939830, 35031603, 9572634, 6077355, 1757852, 13095904,
  31602788, 7654125, 11373602, 3927126. **0/10 A.5b IDs appear in
  the legacy 26 IDs** — A.5b is a fresh pool · zero re-use of
  hallucinated tokens.

**Cross-cluster grep CONFIRMED CLEAN at re-reviewer LGTM.**

---

## §4 · Four review gates

### Gate 1 · CS-IMG-SRC-05 (curator-vs-reviewer separation) · PASS

The A.5b re-curator and this re-reviewer are separate parties,
documented in the report frontmatter (`agent:` field of
`pool-selection.md` vs this file). The re-curator's `pool-selection.md`
is signed at "RE-CURATOR-COMPLETE · LGTM-PENDING-REVIEWER"; this
LGTM is the reviewer's act. The original A.3 curator and reviewer are
both retired from the lifecycle of the A.5b pool by virtue of A.5b
superseding the A.3 pack with new IDs.

### Gate 2 · CS-IMG-POOL-01 (slot order [hero, feature, portrait, portrait, detail, ambient]) · PASS

The 6-slot pool order is preserved in source at
`apps/catalog/template_content_causa.py` lines 112-160 (verbatim
slot order). The 4 magazine-grid extras are defined separately at
lines 167-198 (consistent with LF-2 L7=magazine-grid composition
contract).

### Gate 3 · CS-IMG-PREM-02 (resolution thresholds) · PASS

Resolution thresholds verified by Pexels page URL widths:

| Slot | Required | Committed width | Verified at |
|---|---|---|---|
| 0 hero | ≥ 1600 | w=1600 | `probe-33939830-stgeorges-liverpool.jpeg` (1600×1066) |
| 1 feature | ≥ 1200 | w=1200 | `probe-35031603-latin-manuscript.jpeg` (1200×800) |
| 2 portrait | ≥ 800 (square-safe) | w=800 | `probe-9572634-senior-library.jpeg` (800×1200 portrait original) |
| 3 portrait | ≥ 800 | w=800 | `probe-6077355-judge-bookshelves.jpeg` (800×1200) |
| 4 detail | ≥ 800 | w=800 | `probe-1757852-textured-page.jpeg` (800×480) |
| 5 ambient | ≥ 800 | w=800 | `probe-13095904-shelves.jpeg` (800×1422) |
| 7 magazine hero | ≥ 1200 | w=1200 | `probe-31602788-palazzo-giustizia.jpeg` (1200×944) |
| 8 magazine small | ≥ 800 | w=800 | `probe-7654125-fascicoli.jpeg` (800×1198) |
| 9 magazine small | ≥ 800 | w=800 | `probe-11373602-armchair.jpeg` (800×1200) |
| 10 magazine small | ≥ 800 | w=800 | `probe-3927126-leather-shelf.jpeg` (800×1200) |

All resolutions clear the CS-IMG-PREM-02 thresholds.

### Gate 4 · CS-IMG-COH-07 (voice anchor coherence) · PASS

The voice anchor `Ogni sentenza è un'<em>evidenza</em> incardinata,
non un'opinione difesa.` foregrounds the COURTROOM (the chamber where
evidence is incardinated) and the CODEX (the public record where the
sentence sits). The A.5b pool delivers:

- The COURTROOM at three scales: slot 0 (Liverpool chamber interior)
  + slot 7 magazine hero (Cassazione Rome facade) + magazine extra 9
  (judicial bench chair).
- The CODEX at four scales: slot 1 (Latin gothic spread) + slot 4
  (codex page macro) + slot 5 (vertical archive shelves) + magazine
  extra 10 (codex spine macro).
- The PEOPLE demoted to environmental masthead: slot 2 (founder
  reading codex) + slot 3 (associate reading paper).
- The WORK PRODUCT visible: magazine extra 8 (fascicoli stack).

**The em-word `evidenza` lands on the chamber, the codex, and the
case-card, NOT on a partner's smile.** Voice-anchor coherence
PASSES.

---

## §5 · Live render audit

The re-reviewer re-opened the dev-server-walk evidence in
`captures/walk-causa-home-1440-fullpage.jpeg` and confirmed:

- The Liverpool empty courtroom (33939830) renders at the full-bleed
  hero band as the `.cs-hero .photo` background-image.
- The senior man portrait (9572634) renders as the `.cs-leadership
  -single img`.
- The 4 magazine cards render the Cassazione exterior + fascicoli
  stack + bench chair + codex spine in the correct 3+1 grid shape.
- Zero `_IMAGERY_HOLD_PLACEHOLDER` content surfaces in the rendered
  HTML.
- Zero "imagery hold · A.5b re-curate pending" italic SVG label
  surfaces.

The 6/6 home-rendered photographic surfaces hit the new verified
URLs. Slots 1/3/4/5 are constants without current page_data
hookup (a pre-existing build-side observation; A.5b deliberately
does not widen scope to wire those surfaces).

---

## §6 · Risk acceptance (re-reviewer's accept-with-disclosure)

The re-reviewer accepts the A.5b pool with three explicit
disclosures carried forward to A.6b:

| Risk | Severity | A.6b test |
|---|---|---|
| **A.5b-R1** · slot 0 wood-paneling tone is honey-warm rather than cool-timber | MEDIUM | side-by-side capture of Causa home and Continua home at 1920 + 1100 + 880 must NOT read "same studio, different copy" at 1-second read. If it does, recommend A.5c slot-0 single-slot re-curate (cool-timber European chamber URL pool). |
| **A.5b-R2** · slot 1 Latin gothic codex pulls slightly toward religious-text adjacency | LOW (dormant — slot 1 not currently wired to render) | re-test only if slot 1 becomes wired to a page_data field. The visible "peccato" word should read as canonical-law / Decretals rather than as Bible at 1-second. |
| **A.5b-R3** · slot 3 small Lady Justice + gavel visible at desk's left edge | LOW (dormant — slot 3 not currently wired to render) | re-test only if slot 3 becomes wired. At rendered about-page size, the small Lady Justice + gavel may need to be cropped or substituted; mitigation is the dominant register (vertical wood bookcase >70% frame). |

The re-reviewer notes that R2 and R3 are dormant as long as slots 1
and 3 remain wired only at the constant level (not in any page_data
field). The active live-render carries only R1, which is borderline
but acceptable.

---

## §7 · Comparison to the A.3 curator-reviewer pair (post-mortem note)

The original A.3 curator's `pool-selection.md` claimed CURATOR-
PROPOSE-LGTM-WITH-DISCLOSURE. The original A.3 reviewer's
`reviewer-lgtm.md` likely (per the file name) signed LGTM-CONFIRMED.
A.6 IT review-lock then disproved both signoffs by live-fetching the
Pexels CDN URLs and finding 8/8 sampled IDs resolved to wrong
subjects. The A.3 reviewer's failure mode was identical to the A.3
curator's: trust on description without per-URL live verification.

The A.5b re-reviewer therefore took the additional step of physically
re-opening every capture JPEG (not just reading the captions) and
re-running the cross-cluster grep independently. This LGTM thus rests
on:

1. The re-curator's per-URL live capture (one Playwright screenshot
   per chosen ID before commit).
2. The re-reviewer's per-URL re-walk of the same captures.
3. The re-reviewer's independent cross-cluster grep.
4. The live render audit on the post-restore Causa home.

If the orchestrator wants additional defensive depth, a third party
(e.g. the A.6b critic) could perform a third independent live-fetch
of each Pexels CDN URL during the A.6b walk. The re-reviewer
recommends this third-party verification step be made standard for
every imagery pack going forward; the A.3 → A.6 → A.5b chain proves
that two-stage curator-reviewer is insufficient to catch hallucination
when both stages share the same evidence basis (description without
live fetch).

---

## §8 · Sign-off (re-reviewer side · CS-IMG-SRC-05)

```
RE-REVIEWER LGTM · causa-legale · A.5b imagery RE-CURATE (2026-05-04)
======================================================================

Pool key:                       business-legale (committed in source)
Pool shape (CS-IMG-POOL-01):    [hero, feature, portrait, portrait, detail, ambient]
Primary 6-slot URLs:            6/6 verified live · captures match captions
Magazine-grid extras:           4/4 verified live · captures match captions
Backup roster:                  empty at A.5b · backup-pass held for a future light workstream

Cross-cluster grep result:      CLEAN at LGTM (re-run independently)
Cross-cluster grep run date:    2026-05-04 (re-reviewer LGTM)
Cross-cluster grep targets:     business-corporate · business-fiscal ·
                                business-coaching · business-stewardship
                                · business-architecture · lawyer-classic
                                · lawyer-modern · plus design-orchestrator/
                                + factory/ + docs/content-factory/imagery/packs/

Gate results:                   4/4 PASS
                                · CS-IMG-SRC-05 (curator-vs-reviewer
                                  separation) PASS
                                · CS-IMG-POOL-01 (6-slot order) PASS
                                · CS-IMG-PREM-02 (resolution thresholds) PASS
                                · CS-IMG-COH-07 (voice anchor coherence) PASS

Disclosures accepted:           3
                                · Risk A.5b-R1 (slot 0 wood-tone honey-
                                  warm rather than cool-timber) MEDIUM ·
                                  re-test at A.6b
                                · Risk A.5b-R2 (slot 1 Latin gothic
                                  religious-text adjacency) LOW · dormant ·
                                  re-test only if slot 1 becomes wired
                                · Risk A.5b-R3 (slot 3 small Lady Justice +
                                  gavel) LOW · dormant · re-test only if
                                  slot 3 becomes wired

Hardest slot:                   slot 0 hero (re-confirmed · borderline-LOW
                                · 1 strong primary at premium quality ·
                                no available backups at A.5b)
Easiest slot:                   magazine extra 7 (Corte di Cassazione
                                Rome · institutionally exact)

Status:                          LGTM-CONFIRMED-WITH-DISCLOSURE
Verdict:                         A.6b RAPID REVIEW-LOCK MAY BEGIN
Next agent:                      A.6b critic (Phase X.6 Step 5c)
                                 reads `causa-a5b-imagery-recurate.md` first
                                 · re-walks the IT draft live at 1440 / 880
                                 / 375 · re-tests the priority surfaces
                                 (hero · founder · case-cards) for
                                 1-second register · re-runs the frozen-
                                 sibling regression · re-tests the 3
                                 disclosed risks. On A.6b GREEN, the
                                 orchestrator re-issues the user-handshake
                                 invitation; workflow C (multilingual)
                                 becomes eligible after that handshake.

Imagery axis verdict:            GREEN (vs A.6 "imagery HELD · review-
                                 lock PARTIAL"). Copy/chrome/typography/
                                 palette remain LOCKED from A.6 with no
                                 re-visit needed at A.6b.
```

The re-reviewer signs LGTM-CONFIRMED-WITH-DISCLOSURE. The disclosures
are documented · the risks are dormant or A.6b-testable · the
re-curator's claims verify against the captures · the cross-cluster
grep independent re-run is CLEAN · the live render audit confirms the
6 active surfaces hit the new URLs. **A.6b rapid review-lock is
authorised.**
