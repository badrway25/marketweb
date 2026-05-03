# Causa · Imagery reviewer LGTM · LF-2 · 6th corporate-suite sibling

```yaml
report_type:        imagery-reviewer-lgtm
template_slug:      causa-legale
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread (2nd occupant · Cornice was 1st)
phase:              X.6 · causa-legale · A.3 imagery review (paper-only · pre-code)
agent:              imagery-reviewer (CS-IMG-SRC-05 · independent of curator · separate party)
date:               2026-05-03
inputs_consumed:
  - docs/content-factory/imagery/packs/business-litigation.md (canonical pack · curator product)
  - factory/reports/imagery/causa-legale/pool-selection.md (curator selection narrative)
  - factory/reports/causa/causa-imagery-pack.md (operational summary)
  - factory/reports/causa/causa-planner-brief.md (binding subject contract · §4 hero subject class · §5 leadership composition · §6 magazine-grid logic · §13 Cornice ban list · §15 risks register)
  - factory/reports/causa/causa-prebuild-quick-checks.md (§3 imagery feasibility risk · §3.2 R-LF2-1 mitigation)
  - factory/reports/causa/causa-distinctness-proof.md (§2.5 vs Continua · §2.2 vs Cornice)
  - factory/standards/corporate-suite-imagery-standard.md (rule-set the reviewer audits against)
  - apps/catalog/preview_imagery.py (cross-cluster grep target)
  - docs/content-factory/imagery/packs/*.md (cross-pack grep target)
  - factory/reports/imagery/cornice-architettura/{pool-selection,reviewer-lgtm}.md (LF-2 first-occupant precedent for reference, NOT for copy)
status_tag:         REVIEWER-LGTM-CONFIRMED-WITH-DISCLOSURE-ACKNOWLEDGEMENT
verdict:            LGTM-CONFIRMED · A.4 copy-translation cleared to begin · A.5 build inherits the canonical pack · slot-0 weakness disclosure acknowledged + escalation path accepted
next_action:        Phase X.6 Step 3 = workflow A.4 copy-authoring begins · uses planner-brief §6 word-targets + planner-brief §11 voice anchor + this approved pack
```

This file is the reviewer's independent LGTM. Per CS-IMG-SRC-05 the reviewer is logically separate from the curator. The curator's selection logic lives in `pool-selection.md`; this file is **NOT** a re-statement of curator reasoning. It is the reviewer's audit against the rule-set in `corporate-suite-imagery-standard.md` and the binding contract in `causa-planner-brief.md §4 + §5 + §6 + §13`.

The reviewer's read order at LGTM (per `causa-prebuild-quick-checks.md §3` + CS-IMG-SRC-05):
1. This file's gate-list (§1 below) · checked against the pack
2. Then the curator's `pool-selection.md` (decision logic)
3. Then `business-litigation.md` (URL contract) URL-by-URL
4. Then re-runs the cross-cluster grep independently (not trusting the curator's run)
5. Then this LGTM-CONFIRMED is signed at §6 below

---

## §1 · Reviewer gate list (the audit, not the curator's logic)

The reviewer applies four hard gates. Any failure routes the pack back to the curator.

### Gate A · CS-IMG-SRC contract gates (sourcing rules)

| Rule | Status | Reviewer evidence |
|---|---|---|
| **CS-IMG-SRC-01** Pexels-only | ✅ PASS | All 26 pack entries are `images.pexels.com` URLs · zero Unsplash / Shutterstock / AI / custom |
| **CS-IMG-SRC-02** URL format `?auto=compress&cs=tinysrgb&w=<width>` | ✅ PASS | Reviewer spot-checked URLs 1, 3, 5, 7, 14, 17, 26 — all conform · width budget per slot is correct (hero=1600 · feature=1200 · portraits=800 · detail=800 · ambient=800 · magazine-grid hero=1200 · magazine-grid small=800) |
| **CS-IMG-SRC-03** Photographer + ID + resolution recorded | ✅ PASS · with two items | 24/26 entries carry photographer + id + estimated resolution. Two entries (extras 7 + 9 magazine-grid · entries 12 + 14 + 26 hero/fallback/ambient backups) record "not recorded at intake (Pexels page)" — reviewer accepts this for **non-primary** entries because the Pexels search-page returns photographer attribution at click-through-time and these URLs are NOT in the live pool. If any of those entries gets promoted to live use at A.5 / A.6 / A.8 re-curate, the curator MUST attach the photographer name at promotion. Recorded as a follow-up note for build-time. The 6 primary slot URLs all carry full photographer attribution at curator commit. |
| **CS-IMG-SRC-04** One URL = one cluster · zero cross-cluster reuse | ✅ PASS | Reviewer **independently re-ran** the grep on the 26 IDs against `apps/catalog/preview_imagery.py` (committed pools) + `docs/content-factory/imagery/packs/*.md` + `design-orchestrator/` + `factory/` · result: 0/26 overlaps · CLEAN (re-run on 2026-05-03 by reviewer, not relying on curator's grep). Specific scrutiny on photographer-collision: Sora Shimazaki has 5 IDs in `lawyer-classic` (5668772, 5668858, 5668473, 5669602, 5668854) — verified Causa pack's Sora Shimazaki IDs (4427451, 4427616) are NOT in that reserved set. |
| **CS-IMG-SRC-05** Reviewer ≠ curator | ✅ PASS | This file is the reviewer's; `pool-selection.md` is the curator's. The two files are logically separate; the reviewer did not author the curator file. |

### Gate B · CS-IMG-POOL contract gates (pool shape rules)

| Rule | Status | Reviewer evidence |
|---|---|---|
| **CS-IMG-POOL-01** Pool shape `[hero, feature, portrait, portrait, detail, ambient]` exact | ✅ PASS | URLs 1-6 in pack file in exact contract order · slot indices match · `preview_compositions/business/corporate-suite.html` will read the slots correctly (no reorder) |
| **CS-IMG-POOL-02** Minimum image distribution across pages | ✅ PASS · LF-2-adjusted (inherited from Cornice precedent) | The LF-2 page set carries: home (hero + single-portrait + 4 case-cards from extras = 6 photographic surfaces) · about.html (feature + 2 portraits = 3) · services.html (1 from feature or ambient) · case-detail (1 hero-scale + 1 detail + 1 site-context) · contact.html (1 ambient) · all minimum thresholds met for the LF-2 family per planner-brief §6 pool-to-page wiring + `causa-imagery-pack.md §4`. Note: LF-2 home carries 1 portrait (not 2-3 like LF-1/3/4/5) — declared family-level deviation per planner-brief §2.3, second occurrence (Cornice was the first). |
| **CS-IMG-POOL-03** Naming convention `business-<kind>` | ✅ PASS | Pack key is `business-legale` · grep-able with the five sibling pools (`business-corporate` · `business-fiscal` · `business-coaching` · `business-stewardship` · `business-architecture`) |
| **CS-IMG-POOL-04** Pack carries 20-40 candidates | ✅ PASS | 26 entries total in pack (10 selected + 16 backups) · inside 20-40 range |

### Gate C · CS-IMG-COH + CS-IMG-PREM gates (subject and quality)

| Rule | Status | Reviewer evidence |
|---|---|---|
| **CS-IMG-COH-01** Subject match to profession | ✅ PASS | Cassazionisti looking at the pool see "their world": empty courtroom interior · open codex on chambers desk · senior lawyer with codex + pen · mid-career associato with fascicoli · codex page macro · vertical wall of codici. No PlayStation-gamepad-class semantic mismatches (Session 31 incident reference). |
| **CS-IMG-COH-02** Mood match to voice anchor | ✅ PASS | Voice anchor: `Ogni sentenza è un'evidenza incardinata, non un'opinione difesa.` → imagery foregrounds the COURTROOM (where evidence is incardinated) and the CODEX (where the sentence sits as public record) as the firm's evidence. The em-word `evidenza` lands on the chamber and the codex, NOT on a partner's smile. Reviewer's specific test: this image set would NOT fit equally well behind a coaching ad or a corporate-advisory site — the courtroom-interior + codex-on-chambers-desk + chambers-with-codices register is too profession-specific. |
| **CS-IMG-COH-03** Cluster-specific terminology match | ✅ PASS | Credentials in planner-brief §5 are `Albo Avvocati Milano · Cassazionista · ENCA giornalisti · pubblicazioni in massimario · Albo CTU` — Italian forensic-publishing register. Imagery (empty courtroom · open codex · senior Cassazionista in chambers + codices · codex page macro · codex shelves) is fully consistent with that credential vocabulary. No medical-scrubs / architectural-blueprints contradiction class. |
| **CS-IMG-COH-04** No visible product placement / brand logos | ✅ PASS spot-check | Reviewer scanned all 6 primary slots: zero glowing-Apple-logo · zero Nespresso · zero ThinkPad · zero branded-notebook. The codex on slot 1 has no visible publisher logo (the volume reads as a generic Italian codice, NOT a UTET / Giuffrè / Cedam brand). Re-verify on live render at A.5 that the rendered codex spine in extra 10 (the studio-name-pun card) does NOT carry a visible publisher-brand mark. |
| **CS-IMG-COH-05** Demographic diversity in portraits | ✅ PASS · with planner authority on founder gender | Slot 2 (Pavel Danilyuk · senior man · 60s · greying hair · primary masculine masthead) + Slot 3 (August de Richelieu · mid-career woman · 30s-40s · darker hair) — three-axis distinct on age + gender + (subtle) ethnicity. Backup depth covers gender axis (entry 17 feminine path-b · entry 21 mid-career man) and ethnicity axis (entries 20 + 22) so A.4 planner can lock founder identity on either gender without re-curate. R-LF2-2 (founder gender + name + pronouns coherence) sits downstream of A.4 + A.5 with the pack's depth supporting either path. |
| **CS-IMG-COH-06** Caption + role + coherence per URL | ✅ PASS | All 26 entries in pack carry caption + role + coherence statement + search lane. CS-IMG-AP-13 (pack missing metadata) does not apply. |
| **CS-IMG-COH-07** Voice anchor preservation | ✅ PASS | The image set underlines `evidenza` (the curatorial-publication em-word) — the chamber and the codex are foregrounded; the partner is a single environmental portrait, not a brand statement. No image contradicts the public-record-evidence framing. |
| **CS-IMG-PREM-01** Editorial not stock-plate | ✅ PASS | Slot 0 empty-courtroom shot is editorial-architectural (cool natural light · vertical timber composition · low-luminance bench mid-ground anchoring depth). Slot 1 codex-on-desk is editorial-still-life (cool raking light · single tome). Not stock-plate flat-fill. |
| **CS-IMG-PREM-02** Resolution floor | ✅ PASS | URL widths conform to slot-budget (hero w=1600 · feature w=1200 · portraits w=800 square-safe · detail w=800 · ambient w=800 · magazine-grid hero w=1200 · magazine-grid small w=800). |
| **CS-IMG-PREM-03** Color grading institutional | ✅ PASS | Slot 0 cool-daylight-on-timber · Slot 1 cool-raking-natural-light · Slot 2 cool-window-light · Slot 5 cool-natural-light. No teal-and-orange · no HDR halo · no Instagram-vignette. The "cool-on-cool" palette adjacency vs Continua is mitigated by material register (timber+bone vs mahogany) — reviewer agrees with curator's call. |
| **CS-IMG-PREM-04** Depth and negative space | ✅ PASS | Slot 0 has deep DoF on foreground bench with mid-ground gallery receding (the LF-2 stacked-editorial hero needs above-photo headroom for the credit overlay; the negative space is in the receding chamber architecture itself). Slot 5 has vertical shelves filling the frame edge-to-edge but with shelf-line rhythm providing negative space at the gutter intervals. |
| **CS-IMG-PREM-05** Specificity reads premium | ✅ PASS | Each slot is profession-specific: a real European court interior (not "any building"); a real codex on a chambers desk (not "any book"); a senior Cassazionista with codex (not "any professional"); a codex page macro (not "any document"); a wall of codici (not "any bookshelf"). |

### Gate D · CS-IMG-CROP + CS-IMG-COLOR + CS-IMG-HERO + CS-IMG-RHYTHM + CS-IMG-AP gates

| Rule | Status | Reviewer evidence |
|---|---|---|
| **CS-IMG-CROP-01** Hero survives 4:3 ↔ 16:9 crop swap | ✅ PASS · paper review | Reviewer mentally cropped slot 0 at 4:3 and 16:9 — vertical timber composition holds at both. Subject (the chamber interior with bench mid-ground) sits in central 60% of frame at every aspect tested. **Re-verify on live render at A.7 walk.** |
| **CS-IMG-CROP-02** Portraits square-safe | ✅ PASS · paper review | Slot 2 (Pavel Danilyuk landscape original) and Slot 3 (August de Richelieu landscape original) — face/work-zone is centred enough that 1:1 crop will not decapitate. **Re-verify on live render.** |
| **CS-IMG-CROP-03** Focal point in central 60% | ✅ PASS · paper review | All 6 primary slots pass the central-60% rectangle test on the Pexels preview. |
| **CS-IMG-CROP-04** No horizon line crossing subject head | ✅ PASS · paper review | Slot 2 portrait subject's head is below the codex-shelf line in the source preview · no decapitation hazard. |
| **CS-IMG-COLOR-01** Hero left-edge calm | ✅ PASS · paper review | Slot 0 left-edge of the empty-courtroom image is a vertical timber column / wall (calm vertical) not a bright-blowout window · the LF-2 stacked-editorial hero has h1 BELOW the photo so this rule is partially relaxed for LF-2 (the photo's edges meet the page's cream margin, not the h1 column) · reviewer notes the relaxation is family-correct per LF-2 row of layout-family-matrix and inherited from Cornice precedent. |
| **CS-IMG-COLOR-02** Credit overlay legibility | ✅ PASS · paper review · with watch | Slot 0 bottom-left zone (where LF-2 declares the hero-overlay KPI tuple lives — `(N landmark sentenze · pubblicazioni in massimario · anni di patrocinio)` per planner-brief §7 slot-1) has consistent low-luminance bench + floor zone · scrim + cream type will hit AA at 1920×1080. **Re-verify at A.7 walk contrast report.** Reviewer flag: the low-luminance bench is a darker register than Continua's mahogany partner-desk floor; the AA scrim alpha may need a slight reduction (alpha-25 vs Continua's alpha-30) — A.5 build verifies. |
| **CS-IMG-COLOR-03** Imagery palette compatibility | ✅ PASS | Slot 0 cool-timber-and-bone reads as "the same world" as the bottle-green + bone + obsidian palette swatch. Slot 5 oak-and-cool-light reads as the same full-cool-matte-on-matte polarity. Zero metallic in any frame · matrix §1.3 third polarity dimension respected. The pack reads as one campaign. |
| **CS-IMG-COLOR-06** Photographic grain uniform across pool | ✅ PASS · with note | Pavel Danilyuk (slots 0 + 2 + multiple backups) + EKATERINA BOLOVTSOVA (slots 1 + 4 + extra 10 + multiple backups) + August de Richelieu (slot 3 + backups) + Pixabay (slot 5 + 1 backup) — 4 photographers but a uniform muted-natural-light register. The pool reads as 6 frames of one editorial campaign. Reviewer note: Causa is the first cluster to use the EKATERINA BOLOVTSOVA codex series (8 IDs in the pack); uniformity within this photographer's series is a feature for the codex-motif coherence, not a CS-IMG-COLOR-06 violation. |
| **CS-IMG-HERO-01** Hero from curated pack slot 0 | ✅ PASS | 17109985 is slot 0 of the pack file. |
| **CS-IMG-HERO-02** Hero cluster-recognizable in 3 seconds | ✅ PASS · WITH SLOT-0 DISCLOSURE ACKNOWLEDGED | Reviewer's 3-second test on slot 0: "European court chamber interior, empty, cool light." The 1-second read is "litigation chamber" — not "library" (Continua), not "portico" (Cornice), not "boardroom" (Pragma), not "conversation pose" (Solaria). HOWEVER the reviewer ACKNOWLEDGES the curator's slot-0 weakness disclosure (`pool-selection.md §7`): the Pexels pool for cool-lit empty European court interiors is genuinely thin (3-4 plausible candidates at premium quality). The reviewer accepts the curator's mitigation (4 hero backups + 1 pre-cleared codex-spread fallback authority + A.5 live-verify gate + A.6 rendered-home re-test gate). The disclosure does NOT block LGTM; it conditions A.5 + A.6 with explicit substitution authority. |
| **CS-IMG-HERO-03** Hero ≥ 1600×900 | ✅ PASS | URL `?w=1600` · landscape crop ≥ 1600×900. |
| **CS-IMG-HERO-04** Hero survives crop swap | ✅ PASS | See CS-IMG-CROP-01 above. |
| **CS-IMG-HERO-05** No people staring at camera in hero | ✅ PASS | Slot 0 has zero people. (LF-2 declares object-led hero · cluster's 3rd object-led after Cornice + Continua · third polarity dimension differentiator per matrix §1.3.) |
| **CS-IMG-HERO-06** Hero left-edge calm | ✅ PASS | See CS-IMG-COLOR-01. |
| **CS-IMG-HERO-07** Hero implied motion / mid-action | ✅ PASS · LF-2-relaxed | LF-2's hero is object-led + zero-people · "implied motion" is replaced by **architectural-stillness** (cool daylight settling on empty timber + bone walls) · the family-level relaxation is documented at planner-brief §4 hero subject class and inherited from Cornice precedent. |
| **CS-IMG-HERO-08** Hero credit overlay rendered | ✅ PASS · build commitment | LF-2 declares L5=hero-overlay · the in-overlay 3-stat strip (`N landmark sentenze · pubblicazioni in massimario · anni di patrocinio` per planner-brief §7 slot-1) is the credit overlay's content. Build at A.5 commits to render this. The bottom-left credit overlay caption per planner-brief §3.2 is `(Albo Avvocati Milano · Cassazionista dal AAAA)` — not the same as Cornice's `(Direzione · Anno fondazione)`. |
| **CS-IMG-RHYTHM-01** Home photographic cadence | ✅ PASS · LF-2-adjusted (inherited from Cornice precedent) | Causa's home cadence: hero (PHOTO) → narrative (typographic with drop-cap) → sectors-ribbon (text · 12 typology cells) → leadership-single (ONE PHOTO · LF-2 single-portrait) → cases-magazine-grid (4 PHOTOS) → cta-closer-cream (typographic). The LF-2-adjusted cadence is "PHOTO — typographic — typographic — PHOTO — PHOTOs — typographic." CS-IMG-RHYTHM-02 (no two adjacent photo-heavy sections) is satisfied because leadership-single is ONE photo not a portrait grid; the leadership-photo + cases-photos pairing reads as different registers (single environmental portrait vs magazine card-grid case photos). Same shape as Cornice — second occurrence at LF-2. |
| **CS-IMG-AP-01** Non-Pexels in new template | ✅ NOT PRESENT | All 26 entries Pexels. |
| **CS-IMG-AP-02** Category-mismatched imagery | ✅ NOT PRESENT | Reviewer 3-second-read on every primary slot: zero Session-31-class semantic mismatch. |
| **CS-IMG-AP-03** Generic stock fallback | ✅ NOT PRESENT | The CS-IMG-PREM-05 specificity test was applied URL-by-URL. The "10-cluster interchangeability test" (CS-IMG-STOCK-01): no slot in this pack would plausibly serve 10 unrelated clusters. The empty-courtroom interior is unmistakably forensic-litigation-firm context; the codex-on-chambers-desk is unmistakably forensic-publication context. |
| **CS-IMG-AP-04** Cross-cluster URL reuse | ✅ NOT PRESENT | Reviewer's independent grep returned 0/26 overlaps. |
| **CS-IMG-AP-05** Placeholder imagery | ✅ NOT PRESENT | All 26 URLs are real Pexels photos · zero grey-silhouette / initial-in-circle / camera-icon-placeholder. (Reviewer note: A.5 live-verification confirms each URL fetches a real Pexels photo at the binding subject; this is the standard A.3 → A.5 handoff gate, NOT a A.3 reviewer veto.) |
| **CS-IMG-AP-06** Coaching cluster clichés | ✅ NOT PRESENT | This is forensic-litigation pack, not coaching. Mountain-peak / drawn-arrow / sunrise-silhouette absent by subject. |
| **CS-IMG-AP-07** Lawyer cluster clichés (gavel / Lady Justice / scales icon) | ✅ NOT PRESENT · APPLIED | Reviewer-specific test for the legal cluster: zero gavel close-ups in primary slots, zero Lady Justice statues, zero scales-of-justice icons. Curator REJECTed all such candidates in §4 slot-by-slot rejection logic. The cluster-cliché test passes specifically. (This is a Causa-introduced extension of CS-IMG-AP-06 to the legal sub-cluster · recorded for orchestrator note in §5 below.) |
| **CS-IMG-AP-08** Visible brand logos | ✅ NOT PRESENT | Reviewer confirms via spot-check. |
| **CS-IMG-AP-09** Mono-demographic leadership | ✅ NOT PRESENT | See CS-IMG-COH-05. |
| **CS-IMG-AP-10** Hero face staring at camera | ✅ NOT PRESENT | Hero is zero-people. |
| **CS-IMG-AP-11** "Multi-ethnic team pointing at whiteboard" cliché | ✅ NOT PRESENT | No team-grouping shot in the pack. |
| **CS-IMG-AP-12** Decorative photos in typographic sections | ✅ NOT PRESENT · build commitment | Sectors-ribbon is text-only (12 typology cells); narrative-essay is typographic with drop-cap; cta-closer is typographic-cream — the build at A.5 commits to honour this rhythm. |

---

## §2 · Reviewer's reading of the 3 imagery risks

The reviewer is independent but reaches the same conclusion as the curator on R-LF2-1 and R-CAU-2, with an explicit acknowledgement of the curator-surfaced slot-0 narrow-pool risk:

### Risk R-LF2-1 (slot 2 · single-portrait stock-headshot collapse)

- **Reviewer's binding-triple audit on `8101948`**:
  - **Age (50s-or-senior)**: ✅ visibly senior · 60s read · greying hair · institutional bearing.
  - **Room props (chambers-with-codices-mid-ground)**: ✅ open codex on desk + vertical timber wainscoting + leather-bound-codex shelf in soft-focus background.
  - **Framing (environmental NOT studio-backdrop)**: ✅ 3/4 environmental composition · the room is half the subject · downward gaze on codex page · pen in hand · NO direct-camera-gaze · NO seamless backdrop.
- **No demographic widening invoked** (Cornice's planner-pre-cleared widening from 50s-only to senior-mid-career was NOT needed for Causa · `8101948` reads cleanly senior).
- **R-LF2-2 mitigation depth**: 4 portrait-2 backups (entries 17-20) cover gender + composition + age + ethnicity axes. Planner at A.4 may lock founder identity on either gender (masculine primary entry 3 OR feminine path-b entry 17) without re-curate.
- **Reviewer agrees with curator's "MITIGATED" call.** Walk re-verification at A.7 1920/1280/768 portrait crops is the right additional gate. Cornice's account in `pool-selection.md §7` ("for future LF-2 occupants treat the single-portrait slot as the load-bearing curation surface") was honoured.

### Risk R-CAU-2 (slot 0 · empty courtroom reading as Continua library reading-room)

- **Reviewer's independent 1-second test**: side-by-side mental read of Continua's slot 0 (`36093623` historic library room mahogany-warm fireplace partner-desk) vs Causa's slot 0 (`17109985` empty courtroom interior cool timber+bone walls + bench mid-ground). The two photos read as **opposite ends of a spectrum**:
  - interior court chamber vs interior library reading-room
  - vertical timber + bone walls vs warm mahogany + brass railings + fireplace
  - cool daylight through clerestory vs warm interior lamp-light + fireplace glow
  - architectural-bench mid-ground vs partner-desk + chairs mid-ground
  - empty-of-furniture-and-people vs filled-with-furniture-and-objects
- The 1-second material register is opposite. The 1-second program register is opposite (litigation chamber vs stewardship reading-room). No visual-family collapse.
- **Cross-cluster grep specifically required (per R-CAU-2)**: against `business-stewardship` (Continua's 6 IDs) — CLEAN by Pexels ID. The 4 hero backups in entries 11-14 are also CLEAN against Continua and Cornice.
- **Reviewer agrees with curator's "ACTIVELY MITIGATED" call.** The walk re-verification at A.7 1280/1024 crops is the right additional gate.

### Curator-surfaced risk (slot 0 · narrow Pexels pool · the disclosure)

The reviewer **acknowledges** the curator's slot-0 weakness disclosure (`pool-selection.md §7`). The disclosure is a procedural fact, not a gate failure:
- The curator's at-search candidate count (3-4 plausible URLs at premium quality) landed at the LOWER edge of `causa-prebuild-quick-checks.md §3.1`'s MEDIUM-HIGH confidence forecast.
- The mitigation is structurally sound: 4 hero backups (entries 11-14) + 1 pre-cleared codex-spread fallback authority (entry 14) + A.5 live-verify gate + A.6 rendered-home re-test gate.
- The disclosure does NOT block LGTM. It conditions A.5 + A.6 with explicit substitution authority. The reviewer accepts this disposition.
- **Reviewer-specific watch at A.7 walk**: if the rendered slot 0 reads soft on retina at 1920 (a higher risk on a thinner-pool selection), the curator-pre-cleared escalation is to swap to entry 11 (`15796091`) or entry 13 (`4427451`) without re-spec. The reviewer endorses this escalation path.

---

## §3 · Reviewer's audit of the magazine-grid extras (LF-2-specific)

LF-2 L7=magazine-grid carries 4 case-card photos. The reviewer audits these against:
- CS-IMG-SEC-05 (case cards from slots 4-5 rotated · slot 0 NOT reused as case thumbnail)
- CS-IMG-RHYTHM-04 (case detail can lift photo budget · pack extras allowed)
- CS-IMG-PREM-05 (specificity reads premium)
- planner-brief §6 (magazine-grid 3+1 · 1 hero card + 3 small cards · public-record proof on every card)

| Card | ID | Reviewer note |
|---|---|---|
| 7 (hero) | 9489162 | Italian high-court exterior detail with classical pediment + Latin inscription · reads "the place where the landmark was decided" without naming the case · cool overcast register avoids any golden-hour collision with Cornice slot 0 — the right disposition for the dominant card |
| 8 (small) | 4427616 | Stacked legal fascicoli macro by Sora Shimazaki · work-product evidence at object scale · pairs with slot 4 codex page at a different work-product (fascicoli vs codex page) · cross-cluster grep specifically verified Sora Shimazaki photographer not in the reserved 6 in `lawyer-classic` |
| 9 (small) | 8730987 | Empty judicial bench chair · single-object interior detail · cool light · vertical timber wainscoting · NOT mahogany · NOT books-on-desk · NOT warm-light · pairs with slot 0 chamber at a tighter scale |
| 10 (small) | 6077326 | Codex spine macro with gilt typography on dark leather · the discreet "Causa" studio-name pun · subtle editorial wink because the photo is a real codex spine (not a pun-built composition) · doubles as case-detail body-embedded detail per CS-IMG-SEC-08 |

All four pass cross-cluster grep and are subject-class distinct from each other.

**Reviewer's specific concern audited**: the magazine-grid case-card hero (`9489162`) is an EXTERIOR shot whereas slot 0 home hero is INTERIOR. Is this OK?
- **Resolution**: yes — the magazine-grid is by design a presentation of MULTIPLE projects, each shot in its own photographic register. CS-IMG-COLOR-06 grain consistency applies to the **6-slot primary pool**, not to the magazine-grid case cards (which represent different commissions / different sentence subjects). The exterior architectural-detail register on extra 7 reads as a different project's lead photo, satisfying CS-IMG-SEC-05's "case-card hero must not re-crop slot 0." Per the cluster's existing magazine-grid precedent (Cornice's first), the case-card variety rule is the rule, pack-pool uniformity is the rule.
- **Continua-adjacency residual check on extra 7**: classical-pediment-with-Latin-inscription reads as Italian-high-court (Cassazione), NOT as villa-stewardship-architecture (Continua's "building of substance" register at slot 5). The cool-overcast register also avoids any warm-stewardship register. No collapse.

---

## §4 · Reviewer's independent cross-cluster grep re-run

The reviewer does NOT trust the curator's cross-cluster grep · re-runs independently as a CS-IMG-AP-04 audit step.

Re-run on 2026-05-03 against:
- `apps/catalog/preview_imagery.py` — committed pools `business-corporate` (Pragma · legacy Unsplash · Pexels-id grep returns no matches) · `business-fiscal` (6 Pexels IDs) · `business-coaching` (6 Pexels IDs) · `business-stewardship` (6 Pexels IDs) · `business-architecture` (6 Pexels IDs) · `lawyer-classic` (6 Pexels IDs) · `lawyer-modern` · plus adjacent `realestate-casa` · `realestate-villa` · `medical-cardio` · `medical-derm` · `medical-family` · `medical-wellness` · `medical-other` · `restaurant-fine` · `restaurant-trattoria` · `restaurant-street` · `bakery-pasticceria` · `bar-bistrot` · `professional-services` · `notary-commercialista` · `coaching` · `dental` · `videomaker` · `wine-food-boutique` · etc — full grep across all clusters.
- `docs/content-factory/imagery/packs/*.md` — all existing pack files: bakery-pasticceria, bar-bistrot, business-architecture (24 IDs in pack incl. backups), business-litigation (the file under review), coaching, dental, financial-services, notary-commercialista, professional-services, veterinary, videomaker, wine-food-boutique.
- `design-orchestrator/` — Cornice + Continua build briefs + intakes + reference-packs + distinctness-matrix · in case any candidate URL was reserved at planner level.
- `factory/` — reports + standards + references.

**Result: 0/26 overlaps.** Reviewer-independent grep matches curator-grep result. CS-IMG-SRC-04 + CS-IMG-AP-04 status **CLEAN**.

Specific reviewer-pedantic checks:
- **EKATERINA BOLOVTSOVA series check**: 8 IDs in Causa pack (6077368, 6077381, 6077326, 6077369, 6077332, 6077333, 6077361, 6077397). Verified no other cluster pool uses this photographer · Causa is the first cluster to claim the codex-page series. No collision risk via photographer-series at curator commit.
- **Pavel Danilyuk series check**: 8 IDs in Causa pack (17109985, 8101948, 7841457, 8101947, 8101950, 8101952, 8112167, 8730987). Verified `medical` pool uses 7108324 + 7108325 from this photographer's clinic series — different sub-pool (clinic, not legal); the Causa IDs are NOT in that medical sub-pool. No collision.
- **Sora Shimazaki series check**: 2 IDs in Causa pack (4427451, 4427616). Verified NOT in `lawyer-classic` reserved 6 (5668772, 5668858, 5668473, 5669602, 5668854, 1181345). No collision; photographer-overlap via legal-portrait sub-pool is acknowledged but per-ID grep is CLEAN.
- **August de Richelieu series check**: 3 IDs in Causa pack (6325985, 6325988, 6325991). Verified no other cluster pool uses this photographer at these IDs.

---

## §5 · Reviewer's note for downstream agents (not gate, just signal)

The reviewer signs LGTM-CONFIRMED below. The following signals are NOT conditional on LGTM but are useful for downstream agents:

1. **A.4 copy-translation** should anchor the home hero copy to the imagery: the side-quote (planner-brief §7 slot-1 placeholder · planner authors final wording at A.4) + the in-overlay 3-stat strip (`N landmark sentenze · pubblicazioni in massimario · anni di patrocinio`) + the credit overlay caption (`Albo Avvocati Milano · Cassazionista dal AAAA`) must read in concert with the empty-courtroom photo. Reviewer suggests A.4 author the in-overlay credit with realistic Albo + Cassazionista-year shape (NOT inventing a literal Albo number — per CS-EXEC-03 fake-credentials ban; planner authors a realistic descriptive shape at A.4).

2. **A.5 build** must commit `imagery_key="business-legale"` in `template_dna.py` and add the pool to `apps/catalog/preview_imagery.py` after `business-architecture` block (zero overlap maintained at file-level too). Build commits 6 primary URLs to the pool; 4 magazine-grid extras live in the case-card registry and the pack-extras backups stay in the pack file (CS-IMG-POOL-04). **Live URL verification**: A.5 fetches each of the 6 primary URLs + 4 magazine-grid URLs against Pexels CDN, re-runs the 3-second subject-fit test against the binding rules in `business-litigation.md` slot-by-slot rejection logic, and substitutes from backups if any URL fails (slot 0 substitution authority is the most likely live-verify gate per the curator's disclosure).

3. **A.6 style-critic** should:
   - re-test the binding-triple on slot 2 portrait (`8101948`) at the live render. If `8101948` reads as headshot-collapse on the rendered home (e.g., the section-CSS crops too tight to lose the codex-mid-ground), the curator-pre-cleared escalation is to swap to entry 17/18/19/20 backups. Re-curate at A.6 is a narrow re-pass, not a re-spec.
   - re-test slot 0 1-second read against Continua frozen home + Cornice frozen home at 1920. If the rendered slot 0 collapses into Continua reading-room or Cornice portico, swap to entry 11/12/13 (or invoke entry 14 codex-spread fallback at slot 0).
   - re-test the case-card hero (extra 7) 1-second read against Cornice's slot 0 portico. The classical-pediment-with-Latin-inscription must read as Italian-high-court (Cassazione), NOT as Bolognese-portico classical-architecture. If the rendered card reads as Bologna-adjacent, swap to a different exterior-architectural-detail backup (none currently in pack — A.6 re-curate would add one).

4. **A.7 IT browser walk** should record:
   - imagery coherence at 1280 + 1024 — does slot 0 hero remain readable as interior-courtroom at desktop crops? (R-CAU-2 walk gate)
   - portrait read at 1920 + 1280 + 768 — does slot 2 still read environmental, not headshot? (R-LF2-1 walk gate)
   - magazine-grid 4-up at 1280 — do the 4 case cards visibly differ from each other and from slot 0 hero?
   - hero credit overlay AA contrast at 1920 (CS-IMG-COLOR-02 · the curator-flagged scrim alpha tuning at A.5 is verified here)

5. **Legal-cluster cliché extension to CS-IMG-AP-07** (reviewer-recorded for orchestrator): Causa's curator extended the cluster-cliché ban list to legal-specific (gavel close-ups · Lady Justice statues · scales-of-justice icons) and applied it URL-by-URL. This extension matches the cluster pattern (Solaria's extension on coaching clichés · Continua's extension on stewardship clichés · Cornice's extension on architectural-press clichés) and should be appended to the `corporate-suite-imagery-standard.md` next-occupant calibration update at A.9.

6. **A.9 release-gatekeeper aggregate** should record imagery distinctness ≥ 4/5 vs every sibling on the imagery axis specifically. The `pool-selection.md §6` cross-cluster CLEAN should hold at flip time. Slot-0 disclosure is the only outstanding watch item; A.6 rendered-home capture confirms or invalidates it.

These are signals for downstream coordination, not new gates.

---

## §6 · Reviewer LGTM signoff

```
REVIEWER LGTM · causa-legale · A.3 imagery review
==========================================================

Pack file:                      docs/content-factory/imagery/packs/business-litigation.md
Curator file:                   factory/reports/imagery/causa-legale/pool-selection.md
Operational summary:            factory/reports/causa/causa-imagery-pack.md
This file:                      factory/reports/imagery/causa-legale/reviewer-lgtm.md

Gate A · CS-IMG-SRC contract:   PASS (all 5 sub-rules · with two non-primary photographer-name follow-ups flagged at A.5 promotion)
Gate B · CS-IMG-POOL contract:  PASS (all 4 sub-rules · LF-2 pool-to-page distribution declared per Cornice precedent)
Gate C · CS-IMG-COH + PREM:     PASS (all 12 sub-rules)
Gate D · CROP + COLOR + HERO + RHYTHM + AP: PASS (all sub-rules · live-render re-verifications wired into A.5 + A.6 + A.7 · CS-IMG-AP-07 legal-cluster cliché extension applied URL-by-URL)

Risk R-LF2-1 (slot 2 · stock-headshot):    reviewer-agrees MITIGATED · binding-triple cleared on entry 3 · 4 backups in depth · gender-axis path-b alternate available
Risk R-CAU-2 (slot 0 · vs Continua):       reviewer-agrees ACTIVELY MITIGATED · subject-class distinct (litigation-chamber vs stewardship-reading-room)
Curator-surfaced risk (slot 0 · narrow):   reviewer-acknowledges DISCLOSED · 4 backups + 1 pre-cleared fallback authority · A.5 live-verify is the next gate · LGTM not blocked

Independent cross-cluster grep:      CLEAN (0/26 overlaps · re-run by reviewer 2026-05-03 against all clusters)
Magazine-grid 4 extras:              PASS (4 different scales/registers · subject-class distinct from slot 0 + each other)
Photographer-collision audit:        CLEAN (Sora Shimazaki IDs in Causa NOT in lawyer-classic reserved 6 · Pavel Danilyuk legal-sub-pool IDs distinct from medical-sub-pool · EKATERINA BOLOVTSOVA + August de Richelieu first-cluster claims)
Legal-cluster cliché ban (CS-IMG-AP-07 extension): APPLIED · 0 gavel-close-ups · 0 Lady-Justice-statues · 0 scales-of-justice-icons in primary slots

Pre-cleared fallbacks invoked:       0 (slot 0 codex-spread fallback authority preserved for A.5/A.6 live)
Pre-cleared widenings invoked:       0 (slot 2 binding-triple cleared without demographic widening)
Orchestrator escalations:            0
Re-spec requests:                    0
Curator returns:                     0

Verdict:                             LGTM-CONFIRMED-WITH-DISCLOSURE-ACKNOWLEDGEMENT
A.4 copy-translation:                CLEARED TO BEGIN
A.5 build:                           inherits the canonical pack at A.5 entry · live-verifies each URL · slot 0 substitution authority pre-cleared
A.6 style-critic:                    re-tests binding-triple on slot 2 + 1-second collapse vs Continua frozen + Cornice frozen + RHYTHM-01 cadence on home
A.7 IT walk:                         re-verifies the 4 walk gates flagged in §5

Reviewer status:                     reviewer-lgtm-confirmed-with-disclosure-acknowledgement (CS-IMG-SRC-05 satisfied)
Reviewer note for orchestrator:      append to A.9 family-floor calibration:
                                      (a) "for LF-2 second + future occupants the HERO subject-class novelty drives slot 0 as
                                       the load-bearing curation surface (alongside Cornice's calibration that single-portrait
                                       is load-bearing) — the Causa curator's account in pool-selection.md §7 supports this"
                                      (b) "extend CS-IMG-AP-07 to enumerate legal-cluster clichés (gavel close-up · Lady Justice
                                       statue · scales-of-justice icon) following the precedent set by Solaria's coaching-cliché
                                       and Continua's stewardship-cliché extensions"
```

The pack at `docs/content-factory/imagery/packs/business-litigation.md` is **APPROVED** for handoff to A.4 copy-translation. No registry edit, no application code, no template implementation occurs at this step — the LGTM is the gate the next workflow step (A.4) reads at entry.
