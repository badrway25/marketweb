# Cornice · Imagery curator pool-selection · LF-2 · 5th corporate-suite sibling

```yaml
report_type:        imagery-curator-pool-selection
template_slug:      cornice-architettura
archetype:          corporate-suite
layout_family:      LF-2 · Editorial Spread
phase:              X.5 · cornice-architettura · A.3 imagery curation (paper-only · pre-code)
agent:              imagery-curator (CS-IMG-SRC-05 · curator side · separate from reviewer)
date:               2026-04-30
inputs_consumed:
  - factory/reports/corporate-suite/cornice-architettura/intake.md (binding input · §6 imagery mood · §12 warnings 1/2/4)
  - factory/reports/corporate-suite/cornice-architettura/planner-brief.md (§4 imagery DNA · binding subject + rejection-rules per slot)
  - factory/reports/corporate-suite/cornice-architettura/prebuild-quick-checks.md (§Σ GO · §Δ 3 named risks · §Ω pre-cleared fallback authorities)
  - factory/standards/corporate-suite-imagery-standard.md
  - apps/catalog/preview_imagery.py (cross-cluster grep target: business-corporate · business-fiscal · business-coaching · business-stewardship)
  - docs/content-factory/imagery/packs/*.md (cross-pack grep target)
outputs:
  - docs/content-factory/imagery/packs/business-architecture.md (canonical pack · 24 candidates total · 6 primary + 4 magazine-grid extras + 14 backups)
  - factory/reports/imagery/cornice-architettura/pool-selection.md (this file · curator selection narrative + decision logic)
status_tag:         CURATOR-COMPLETE · LGTM-PENDING-REVIEWER
verdict:            CURATOR-PROPOSE-LGTM · 6/6 main slots filled · 4/4 magazine-grid extras filled · 0 fallbacks invoked · 1 pre-cleared widening (slot 2 demographic) · 0 escalations to orchestrator
next_action:        independent reviewer reads `reviewer-lgtm.md` first then this file then the pack file · runs the 4 review gates · signs LGTM-CONFIRMED or returns to curator
```

This file is the curator's selection narrative. It is not the canonical pack — that is `docs/content-factory/imagery/packs/business-architecture.md`. The two files are paired; the pack carries the URLs + captions + per-URL coherence; this file carries the **decision logic** (search lanes, candidate-pool counts, why each URL was selected over its peers, how each Risk in `prebuild-quick-checks.md §Δ` was actively managed, and what fallback authority was or was not invoked).

The reviewer read order at A.3 LGTM is (per `prebuild-quick-checks.md §Φ` + CS-IMG-SRC-05): `reviewer-lgtm.md` (gate-list) → this file (curator decision logic) → the pack file (URL contract) → cross-cluster grep re-run.

---

## §1 · Search lanes (by slot)

These are the lanes the curator queried at A.3 entry. Counts are post-rejection-rules-pass — i.e. plausible candidates AFTER applying the planner-brief §4 hard-rejection rules per slot. Counts are larger than `prebuild-quick-checks.md §3` orchestrator paper-level estimates because the curator queried both primary and backup search lanes.

| Slot | Primary search lane | Backup search lane | Plausible candidates after rejection-rules | Verdict |
|---|---|---|---|---|
| 0 hero | `architecture courtyard` + `italian portico` | `italian architecture stone shadow` | ≥ 12 (Bologna porticoes deeper than expected · Italian-context bonus) | **GO** |
| 1 feature | `architectural model` + `scale model architecture studio` | (combined returned ≥ pool floor) | ≥ 8 (Tima Miroshnichenko architectural-model series carries the bulk) | **GO** |
| 2 portrait | `architect portrait` + `senior architect studio` | `architect studio woman blueprint` | ≥ 7 (RDNE senior-architect-woman + Ron Lach architect-at-desk + Tima Miroshnichenko architect-with-model) | **GO** (with planner-pre-cleared widening to senior-mid-career — see §4 below) |
| 3 portrait | `young architect drafting` + `architect studio woman blueprint` (path-a) | `architecture interior stone no people` (path-b) | ≥ 10 path-a · ≥ 12 path-b — both clear; curator selected path-a per planner default | **GO (path-a)** |
| 4 detail | `architectural drawing section` | `drafting compass paper` (planner-pre-cleared fallback) | 5 plausible (Ivan S series 4458193/4458196/4458200/4458205/4458210) clearing the BIND rule + the compass-on-blueprints fallback (6615086) ready in pack | **GO** (above the §3 CAUTION threshold of 5; the load-bearing risk did NOT bite) |
| 5 ambient | `architecture studio drafting board` + `architecture studio pin-up wall` | (combined returned ≥ pool floor) | ≥ 5 (Jesus Rivera concrete-wall + cottonbro studio corkboard + interior-art-studio variants) | **GO** |
| extras × 4 | per-typology variants: `restoration architecture facade` · `modern italian residential architecture` · `architectural interior concrete stone minimal` · `architectural detail cornice column` | (each returned ≥ pool floor independently) | ≥ 30 candidates pooled across 4 typology lanes | **GO** |

Total candidate pool surveyed at A.3 entry: **≥ 60 unique Pexels photo IDs** spanning the 6 primary slots and 4 magazine-grid extras, well above CS-IMG-POOL-04's "20-40 in pack" floor and well above the curator-selection ratio recommended in CURATION_PROTOCOL §3.

---

## §2 · Final 6-slot ordered pool

Per CS-IMG-POOL-01 the order `[hero, feature, portrait, portrait, detail, ambient]` is fixed — `preview_compositions/business/corporate-suite.html` reads slots by index. The curator's selection is:

| # | Slot role | Pexels ID | Subject (1-line semantic caption) | Photographer | Width |
|---|---|---|---|---|---|
| 0 | hero | **35715509** | Sunlit corridor of an Italian portico in Bologna, stone columns and ceiling, golden-hour warmth on cool stone, zero people, exterior architectural | Marcel Gierschick | w=1600 |
| 1 | feature | **6614835** | Architectural scale model on a designer's worktable, drawing tools and documents, raking natural light, zero people, zero monitor | Tima Miroshnichenko | w=1200 |
| 2 | portrait | **5915290** | Senior architect (woman, white hair, eyeglasses) reviewing blueprints with pen, environmental home-office workspace, working posture | RDNE Stock project | w=800 |
| 3 | portrait | **6615222** | Mid-career architect (man, afro hair) reviewing project blueprints at office desk, environmental, working posture | Tima Miroshnichenko | w=800 |
| 4 | detail | **4458196** | Close-up architectural blueprint / floor plan, intricate technical lines, single sheet, macro still life | Ivan S | w=800 |
| 5 | ambient | **36809500** | Architectural design studio wall — concrete surface, blueprints + design models pinned/placed, industrial finish, zero people | Jesus Rivera | w=800 |

URL format (CS-IMG-SRC-02): `https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=<width>` — the canonical pack file `docs/content-factory/imagery/packs/business-architecture.md` carries the full URL strings.

---

## §3 · Magazine-grid extras (LF-2 L7=magazine-grid · 3+1 layout · 4 case-card photos)

| # | Card role | Pexels ID | Subject | Project typology | Photographer | Width |
|---|---|---|---|---|---|---|
| 7 | hero card (large) | **2747599** | Minimalist concrete architecture exterior, sharp geometric lines, dramatic high-contrast b&w | concorso / culturale | Bruno Thethe | w=1200 |
| 8 | small card | **36547058** | Contemporary apartment buildings in Rome at sunset, vibrant facades against clear sky | residenziale | Léa Claisse | w=800 |
| 9 | small card | **36428417** | Sunlit elegant arches and shadows in a historic Venaria courtyard, Piedmont | restauro | Ree A | w=800 |
| 10 | small card | **13306459** | Detailed close-up of an ornate stone column and cornice carving, classical | detail / culturale | Zeynep | w=800 |

The 4 cards visibly differ from slot 0 (different season · different scale · different typology · different material palette) AND from each other (4 different Italian cities/sites · 4 different programs · 4 different scales). The studio's range — heritage · residential · cultural · detail-craft — reads at the magazine-grid scroll without further copy.

---

## §4 · Per-slot decision logic (curator narrative)

### slot 0 hero · `35715509` (Marcel Gierschick · Bologna portico)

**Why this URL over its peers**:
- Italian portico (Bologna) is the strongest Italian-architectural-firm context the search returned · the planner intake §3 stakeholder one-liner ("editorial-led architecture studio · publishes its work as a built monograph") needs the hero to land **architectural-firm + Italian + editorial** in 3 seconds (CS-IMG-HERO-02). Bologna's UNESCO-listed porticoes are the platonic Italian-architectural-firm subject.
- Golden-hour warmth on cool stone matches the palette intent (graphite + pietra-serena + terracotta-rust · NEUTRAL/NEUTRAL/WARM · `intake.md §3.1`). No re-grading needed.
- Zero people, sharp shadow lines, deep DoF on foreground colonnade with mid-ground court receding — matches the planner §4 slot_0 binding subject **exactly** (read aloud: "a built courtyard / portico of one of the studio's projects at golden hour · stone material clarity · sharp architectural shadow lines").
- Survives the 4:3 ↔ 16:9 crop swap (CS-IMG-CROP-01): the architectural composition is centred and the colonnade vertical anchors the frame at any tested aspect.

**Peers rejected and why**:
- 18167495 (Betül Seyrantepe · colonnade dramatic lighting) — strong runner-up · slightly more dramatic / less "Italian editorial" feel · kept as backup in pack
- 36471383 (Tahir Xəlfə · stone courtyard · Baku Azerbaijan) — geographically wrong · Italian context is stronger from the Bologna pool · backup
- Bologna competitors 17857002 / 36965004 / 29575243 — all strong; 35715509 won the **golden-hour + warm-on-cool-stone palette match** test.
- Cliché modernist-glass-tower from below (planner §4 slot_0 reject rule) — none in candidate set passed past first round
- Atrium / lobby with people in foreground (Pragma adjacency) — rejected in first round

### slot 1 feature · `6614835` (Tima Miroshnichenko · designer's worktable)

**Why this URL over its peers**:
- Real designer's worktable feel — architectural model + drawing tools and documents on the surface — distinguishes from museum-piece model studio shots (planner §4 slot_1 rejection rule "model must read as in-progress not as a museum piece").
- Tima Miroshnichenko's architectural-craft series carries a uniform colour science across slots 1, 3, 4 backup, and slot-2 backup — CS-IMG-COLOR-06 grain consistency satisfied without forcing all 6 primary URLs into one photographer's series (which would read mono-tonal).
- Zero monitor / laptop / screen visible in frame · planner §4 slot_1 reject rule "any laptop / monitor / digital screen visible (the studio's craft is hand-drafted + printed)" satisfied.

**Peers rejected and why**:
- 7883875 (wooden interior cutaway model with miniature figures) — miniature human figures within the model; planner §4 slot_1 reject "any human (even partial limbs)" was applied conservatively; rejected.
- 13727724 (Steph · model on grid surface) — clean but less editorial-narrative; kept as backup.
- 6614834 (ceramic miniature classical building model · Tima Miroshnichenko) — flat-lay studio shot, less worktable register; kept as backup.

### slot 2 portrait · `5915290` (RDNE Stock project · senior architect woman)

**Why this URL over its peers and how the planner pre-cleared widening was handled**:
- The planner-brief §4 slot_2 binding triple is **50s + drafting-tools/sketches-mid-ground + environmental-NOT-studio-backdrop**. The planner explicitly authorised at A.3 entry (`prebuild-quick-checks.md §Ω·3`) widening from 50s to senior-mid-career (60s) without orchestrator escalation if the binding triple cannot be cleared at exactly 50s.
- The curator's pass found that all leading 50s-only candidates failed at least one binding-triple axis (mostly the environmental-NOT-studio-backdrop axis — "professional 50s portraits" on Pexels skew toward seamless-grey-backdrop LinkedIn-style framing, the exact Risk 3 collapse). 5915290 (senior woman with white hair, focused on blueprints, environmental modern home-office, pen in hand, working posture) clears the binding triple at "clearly senior-mid-career" reading rather than narrowly-50s.
- Per planner: "subject MUST be in 50s OR clearly senior-mid-career". 5915290 satisfies the OR-clause cleanly.
- Demographic gap-closure vs Solaria: Solaria's portrait pair is 30s × 2 (the residual gap). Cornice slot 2 + slot 3 = senior-woman + mid-career-man. The pair closes the demographic gap from BOTH sides without invoking a 60s+40s pair (Continua's reservation).

**Peers rejected and why**:
- 9617905 (Ron Lach · architect at desk · warm lighting) — very strong but reads younger (30s-40s) which would NOT close the senior-side demographic gap and would force slot 3 into senior territory, losing the mid-career anchor; kept as backup.
- 9617379 (Ron Lach · architect with drawings) — same age read; backup.
- 6615231 (Tima Miroshnichenko · architect measuring scale model) — strong environmental but 30s-40s; backup.
- 6614828 / 6615225 (young woman architect with pink hair) — pink hair signals creative-tech register, not editorial-architectural senior-principal; pink-hair version kept ONLY as slot 3 backup, NOT slot 2.

**Why this is NOT the LinkedIn-headshot collapse (Risk 3 mitigation in action)**:
- Backdrop is environmental modern home-office workspace — NOT pure white / grey / seamless studio backdrop (planner §4 slot_2 reject rule)
- Subject is captured mid-action with pen in hand reviewing blueprints — NOT shoulders-up tight crop, NOT face-only framing (planner §4 slot_2 reject rule)
- Eyeglasses, blazer, focused posture — institutional-architectural register, NOT fashion / lifestyle / consumer-tech
- Working posture (downward gaze on documents) — NOT direct-camera-gaze stock-pose

### slot 3 portrait · `6615222` (Tima Miroshnichenko · architect with afro hair)

**Why path-a was selected over path-b**:
- Planner §4 slot_3 default is path-a (collaboratore portrait) "if no other constraint binds." The about.html team-grid is the load-bearing about-page surface for the studio's "1 founding architect + 2 collaboratori" org-scale (intake §1), and a real photographic team-grid is stronger evidence of the studio than a project-interior tile.
- Path-b (project-interior · 7422192 Mavera zehra Çoşkun) is preserved as alternate in the pack and is invoked only if A.6 style-critic rejects path-a for any reason.

**Why this URL over its peers (within path-a)**:
- Demographic anti-collision vs slot 2: slot 2 is European-heritage senior-woman; slot 3 must be visibly different on age + gender + ethnicity (planner §4 slot_3 path-a "must visibly differ from slot_2 demographic"). 6615222 is mid-career man with afro hair — three-axis distinct.
- Pairs visually with slot 1 (Tima Miroshnichenko series) — CS-IMG-COLOR-06 colour-grain consistency across the studio-craft surfaces.
- Working posture, environmental contemporary studio — NOT seamless backdrop · NOT shoulders-up crop.

**Peers rejected and why**:
- 6614828 / 6615225 (young Asian woman with pink hair) — same gender as slot 2 (both female); insufficient axis-of-distinction at the gender axis; kept only as backup behind 6615222.
- 9617369 (Ron Lach · young Caucasian architect) — same broad ethnicity-read as slot 2 (European); insufficient ethnicity contrast.
- 6282079 (top-down crop · Yaroslav Shuraev) — top-down crop is not a usable square-safe portrait per CS-IMG-CROP-02.

### slot 4 detail · `4458196` (Ivan S · architectural blueprint close-up) · LOAD-BEARING RISK 1

**Why this URL over its peers and how Risk 1 was handled**:
- Risk 1 (`prebuild-quick-checks.md §Δ`) is the narrow Pexels pool for the section-drawing close-up subject. The escalation-trigger threshold is "≤ 3 plausible candidates on BOTH primary AND fallback searches"; the binding-fallback (compass on trace paper · 6615086) is pre-cleared in planner §4 slot_4 `fallback_subject` so curator does not escalate.
- The curator's primary search (`architectural drawing section`) returned 5+ plausible candidates clearing the BIND rule (single sheet · single subject · macro distance · still life): the Ivan S series (4458193/4458196/4458200/4458205/4458210) plus 268362 (Pixabay · single pencil on blueprints).
- Result: **the load-bearing risk did NOT bite at curator pass.** 4458196 is the cleanest single-sheet macro of the Ivan S series with the most "section-drawing-feel" (intricate technical lines).
- The pre-cleared fallback (6615086 · Tima Miroshnichenko · compass on blueprints) is **NOT INVOKED** at curator pass; preserved in pack as backup #23. The fallback authority remains live for re-curate at A.6 if the style-critic rejects 4458196 for any reason.

**Peers rejected and why**:
- 17115287 (Czapp Árpád · sketch with hands) — hands visible · planner §4 slot_4 BIND "still life NOT desk-in-progress" violated; rejected.
- 9617373 (sketches on wall) — wall-mounted sketches are an ambient-slot subject, not a detail-slot still life; kept as slot 5 candidate (rejected there too because not as strong as 36809500).

**Subject-class anti-collision vs Fiscus tax-document** (Risk 1 cross-cluster grep specifically):
- Fiscus's slot 4 is `7821914` (tax documents with calculator). 4458196 is an architectural blueprint with technical line-work. Subject reads "design drawing" not "tax document" within 1 second. Cross-cluster grep on URL is CLEAN; subject-class read at curator's 3-second test is also CLEAN.

### slot 5 ambient · `36809500` (Jesus Rivera · studio wall with concrete + blueprints + models)

**Why this URL over its peers**:
- The most differentiating ambient candidate: **concrete wall + pin-up blueprints + architectural models** is the studio-as-evidence subject the planner §4 slot_5 BIND rule asks for ("pin-up wall OR drafting-table OR both must be visibly part of the framing"). This URL satisfies BOTH.
- Industrial finish (concrete) explicitly avoids the warm wood-tone register that belongs to Continua's adjacency (Risk 2 mitigation in pack); planner §4 slot_5 reject rule "any cosy-interior with wood tones (Continua adjacency)" enforced.
- Zero laptop / monitor in foreground · planner §4 slot_5 reject rule satisfied.
- Material palette pairs with Cornice's NEUTRAL primary + NEUTRAL secondary (graphite + pietra-serena) — the imagery does not fight the template tokens (CS-IMG-COLOR-03).

**Peers rejected and why**:
- 7504583 (cottonbro studio · corkboard with architectural drawings) — strong but tighter framing on a single corkboard; less full-studio register; kept as backup.
- 6044300 (interior art studio · drawings on table) — table not wall; less the "studio-room-as-witness" register; kept as backup.
- Open-plan generic offices — rejected at first round (reads SaaS · planner §4 slot_5 reject rule).

### magazine-grid extras (4 case-card photos)

**Why these 4 were selected and ordered**:
- The 4 extras are 4 different project typologies (concorso/culturale · residenziale · restauro · detail/culturale) populating 4 different cells of the planner-brief §6 sectors-ribbon. The studio's range — heritage AND new residential AND cultural-competition AND detail-craft — reads at the magazine-grid scroll without further copy.
- Hero card (large · 2747599 · b&w concrete) is the visual outlier vs slot 0 (golden-hour warm) — the case-card hero must look like a DIFFERENT project's lead photo, not a re-crop of the home hero (CS-IMG-SEC-05 forbids slot 0 reuse as case thumbnail). Bruno Thethe's b&w concrete delivers maximum visual contrast vs the home hero's golden-hour Bologna portico while still reading "architecture studio's work."
- 13306459 (Zeynep · cornice carving close-up) is the **studio-name pun** (Cornice, the studio · cornice, the architectural element). Subtle editorial wink; not gimmicky because the photo is real architectural-craft documentation. Doubles as case-detail body-embedded detail per CS-IMG-SEC-08.
- All 4 extras visibly differ from slot 0 hero (different season · different scale · different typology · different country / city). Cross-cluster grep on Pexels IDs CLEAN.

---

## §5 · Risk-management report (the 3 risks from `prebuild-quick-checks.md §Δ`)

### Risk 1 · Slot 4 detail · narrow Pexels pool — **DID NOT BITE**

- **Anticipated severity**: load-bearing (the most likely risk to bite at curator pass).
- **What happened at A.3**: primary search returned 5 plausible candidates (Ivan S series + Pixabay single-pencil), clearing the BIND rule (single sheet · single tool · macro distance · still life). The pre-cleared fallback (6615086 · compass on blueprints) was NOT invoked — preserved in backup roster as live re-curate authority for A.6.
- **Escalation trigger**: ≤3 candidates on BOTH primary AND fallback. Not met.
- **Curator status on Risk 1**: **CLEARED at A.3 entry · zero escalations · fallback authority live for A.6.**

### Risk 2 · Slot 0 hero · object-led + zero-people overlap with Continua — **ACTIVELY MITIGATED**

- **Anticipated severity**: the cluster's first two object-led heroes (Continua reading-room interior + Cornice exterior portico) could read as "the cluster pattern." The curator's hard-rejection rules from planner §4 slot_0 (REJECT cosy-interior with wood tones · REJECT building incidental + people-in-foreground subject · REJECT cliché modernist-glass-tower) were applied URL-by-URL.
- **What happened at A.3**: 35715509 is **exterior** + **stone-and-light** + **golden-hour-warm-on-cool-stone** + **architectural-shadow-line** — the visual register is structurally different from Continua's library/partner-study mahogany-warm reading-room interior:
  - exterior vs interior
  - stone vs mahogany
  - golden-hour vs daylight-contemplative
  - architectural-shadow vs furniture-and-fireplace
  - vertical colonnade composition vs horizontal partner-desk-and-fireplace composition
- **Cross-cluster grep specifically required (per Risk 2)**: against `business-stewardship` (Continua reading-room URLs · the candidate 36093623 + 7045772) — CLEAN by Pexels ID. The 5 hero backups in the pack are also CLEAN against Continua.
- **Curator status on Risk 2**: **CLEARED at A.3 entry · the imagery distinctness vs Continua at hero is by SUBJECT-CLASS (exterior-architectural-shadow vs interior-warm-reading-room), not just by URL.**
- **Walk re-verification at A.7**: imagery coherence at 1280 + 1024 (planner §13 walk plan) — the curator-marked "exterior architectural · stone material · golden-hour warmth" must hold under crop, not just at full-bleed.

### Risk 3 · Slot 2 portrait · LF-2 single-portrait stock-headshot collapse — **MITIGATED VIA PLANNER-PRE-CLEARED WIDENING**

- **Anticipated severity**: LF-2 L6=single-portrait-feature concentrates the cluster's leadership-presence into ONE image — higher-stakes than typical because no second portrait balances.
- **What happened at A.3**: curator found that exact-50s candidates clustered in seamless-backdrop / shoulders-up-crop / direct-gaze-stock-pose territory — the Risk 3 collapse class. Per `prebuild-quick-checks.md §Ω·3` curator was pre-authorised to widen to senior-mid-career (60s) without orchestrator escalation. 5915290 (senior woman + blueprints + environmental + working posture + eyeglasses + blazer) clears the binding triple at "clearly senior-mid-career" reading.
- **No 60s + 40s pair created** (Continua's reservation): slot 3 is mid-career-man (path-a), keeping the Cornice pair distinctly NOT a Continua-pattern duplicate.
- **Curator status on Risk 3**: **MITIGATED · planner-pre-cleared widening invoked once · zero orchestrator escalations · binding-triple cleared · LinkedIn-headshot collapse avoided.**
- **Walk re-verification at A.7**: portrait reads ENVIRONMENTAL not HEADSHOT at 1920 / 1280 / 768 (planner §10 walk plan) — the curator's "RDNE blueprints + pen + home-office workspace" must hold under crop, not just at portrait-card render.

### Bonus · Warning 5 (LF-2 zero-dark-band on home) — **NOT IMAGERY · OUT OF CURATOR SCOPE**

Documented at intake §12 Warning 5 (zero dark band on home is an LF-2 family-level demotion of CS-TONE-03). Curator notes for handoff: imagery does not contribute to dark-band rendering since LF-2 declares L5=hero-overlay (KPI lives in the photo's overlay, not on a separate dark band). No curator action required; flag is for style-critic at A.6 and walker at A.7.

---

## §6 · Cross-cluster grep result (CS-IMG-SRC-04 · CS-IMG-AP-04)

Grep run on 2026-04-30 against:
- `apps/catalog/preview_imagery.py` (committed pools)
- `docs/content-factory/imagery/packs/*.md`
- `design-orchestrator/`
- `factory/`

For each of the 26 candidate Pexels IDs (10 selected + 14 backups + 1 path-b alternate + 1 fallback) the grep returned **CLEAN · 0 matches**. The pack is grep-clean by Pexels photo-id at curator commit time.

Grep targets that were specifically scrutinised:
- vs `business-corporate` (Pragma): legacy Unsplash; Pexels-id grep returned no matches by definition; manual subject-class read confirms zero overlap (Pragma boardroom + atrium + executive portraits + manufacturing facility · Cornice exterior portico + worktable model + senior architect + collaboratore + drawing detail + studio wall — no shared subject class)
- vs `business-fiscal` (Fiscus): 6 Pexels IDs (8927688 · 36175676 · 7845284 · 30614308 · 7821914 · 159832) — none in Cornice pack
- vs `business-coaching` (Solaria): 6 Pexels IDs (7979456 · 5756579 · 9064347 · 12934369 · 34601 · 31236101) — none in Cornice pack
- vs `business-stewardship` (Continua): 6 Pexels IDs (36093623 · 7045772 · 5333750 · 7841828 · 36824936 · 6587827) — none in Cornice pack

---

## §7 · Hardest slot · curator's account

The hardest slot was **slot 2 portrait** (the founding architect masthead). Reasons:

- LF-2 L6=single-portrait-feature concentrates the entire cluster's leadership presence into **one image**. There is no second portrait to balance a marginal first portrait. Risk 3 (`prebuild-quick-checks.md §Δ`) named this "the highest-stakes single image in the pack."
- Pexels' "professional 50s portrait" search returns are heavily biased toward seamless-grey-backdrop LinkedIn-style framing — exactly the failure mode the planner §4 slot_2 reject rules forbid. The "stock LinkedIn collapse" risk is not theoretical; it is the dominant Pexels return for the search.
- The binding triple (50s + drafting-tools-mid-ground + environmental-NOT-studio-backdrop) intersects three independent axes; finding all three in one frame is rare on Pexels.
- The curator was pre-authorised by `prebuild-quick-checks.md §Ω·3` to widen demographic from 50s to senior-mid-career without escalation. Widening did not weaken the read — RDNE Stock project's senior-architect-with-blueprints series delivered a stronger frame than the narrower-50s candidate set.

By contrast slot 4 detail (the load-bearing CAUTION risk) returned 5 plausible candidates clearing the BIND rule — the anticipated "load-bearing" risk did NOT actually bite, while the "lower-anticipated" Risk 3 was the one that needed the planner-pre-cleared escalation lane.

This shifts the family-floor calibration recommendation forward (`prebuild-quick-checks.md §Ω·1`): future LF-2 occupants should treat **the single-portrait slot as the load-bearing curation surface**, not the detail. Recorded for orchestrator at A.9 append-to-matrix.

---

## §8 · Sign-off (curator side · CS-IMG-SRC-05)

```
CURATOR SIGN-OFF · cornice-architettura · A.3 imagery curation
=================================================================

Pool key:                       business-architecture
Pool shape (CS-IMG-POOL-01):    [hero, feature, portrait, portrait, detail, ambient]
Primary 6-slot URLs:            6/6 filled
Magazine-grid extras:           4/4 filled (LF-2 L7=magazine-grid · 3+1 layout)
Backup roster (CS-IMG-POOL-04): 14 backups · pack file holds 24 entries total · inside 20-40 floor

Cross-cluster grep result:      CLEAN · 0/26 IDs overlap with committed pools or existing packs
Cross-cluster grep run date:    2026-04-30
Cross-cluster grep targets:     business-corporate · business-fiscal · business-coaching · business-stewardship · all factory/* + design-orchestrator/* + docs/content-factory/imagery/packs/*

Pre-cleared fallbacks invoked:  0 (slot 4 fallback compass-on-blueprints NOT invoked)
Pre-cleared widenings invoked:  1 (slot 2 demographic widened from 50s to senior-mid-career per Ω·3)
Orchestrator escalations:       0
Re-spec requests:                0

Risk 1 (slot 4 narrow pool):    DID NOT BITE · primary search ≥5 candidates cleared
Risk 2 (slot 0 vs Continua):    ACTIVELY MITIGATED · subject-class distinct (exterior vs interior)
Risk 3 (slot 2 stock-headshot): MITIGATED · planner-pre-cleared widening invoked once

Hardest slot:                   slot 2 portrait (single-portrait stakes + Pexels stock-headshot bias)
Easiest slot:                   slot 1 feature (Tima Miroshnichenko architectural-craft series)

Status:                          CURATOR-COMPLETE · LGTM-PENDING-REVIEWER
Verdict:                         CURATOR-PROPOSE-LGTM
Next agent:                      independent reviewer (CS-IMG-SRC-05 · separate party)
                                 reads `factory/reports/imagery/cornice-architettura/reviewer-lgtm.md`
                                 first, then this file, then the pack file
                                 runs the 4 review gates · signs LGTM-CONFIRMED or returns

Walk re-verifications wired:    A.6 style-critic · A.7 IT browser walk
                                 (Risk 2 imagery-coherence at 1280/1024
                                  Risk 3 portrait-environmental-not-headshot at 1920/1280/768
                                  CS-IMG-RHYTHM-01 photographic cadence on home
                                  CS-IMG-COH-07 voice anchor + imagery alignment)
```

The curator does NOT sign the pack as LGTM. CS-IMG-SRC-05 requires that approval be the reviewer's act, not the curator's. This file is the curator's proposal; the reviewer accepts, returns, or returns-with-changes.
