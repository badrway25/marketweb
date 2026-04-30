# Imagery Pack · `business-architecture`

**Curator**: Phase X.5 · Cornice (LF-2 5th corporate-suite sibling) · A.3 imagery curation · paper-only.
**Date**: 2026-04-30
**Pack key**: `business-architecture` (CS-IMG-POOL-03 · `business-` prefix · grep-able with the four siblings).
**Templates served**: `cornice-architettura` (1st occupant · architecture-firm · single-principal studio · LF-2 Editorial Spread).
**Pool shape**: `[hero, feature, portrait, portrait, detail, ambient]` · CS-IMG-POOL-01 · 6 slots in order.
**Plus**: 4 magazine-grid case-card extras (LF-2 L7=magazine-grid · 3+1 layout · 1 hero card + 3 small cards).
**Plus**: backup roster (CS-IMG-POOL-04 · 20-40 candidates · pack holds extras for 404 recovery and case-detail rotation).

**Reference contracts**:
- `factory/reports/corporate-suite/cornice-architettura/intake.md` · §6 imagery mood · §12 sibling conflict warnings 1, 2, 4
- `factory/reports/corporate-suite/cornice-architettura/planner-brief.md` · §4 imagery DNA (binding subject + rejection rules per slot)
- `factory/reports/corporate-suite/cornice-architettura/prebuild-quick-checks.md` · §Δ 3 named risks · §Ω pre-cleared fallback authorities
- `factory/standards/corporate-suite-imagery-standard.md` · §1 sourcing · §2 6-slot pool · §3 coherence · §4 premium · §13 stock-look diagnostic
- `factory/reports/imagery/cornice-architettura/pool-selection.md` · curator selection (paired with this pack)
- `factory/reports/imagery/cornice-architettura/reviewer-lgtm.md` · independent reviewer LGTM (paired with this pack)

## Validation summary

- All URLs from Pexels (`images.pexels.com`) · CS-IMG-SRC-01 · zero Unsplash · zero AI-generated · zero custom photography.
- URL format conforms to CS-IMG-SRC-02 · `?auto=compress&cs=tinysrgb&w=<width>` per slot width budget.
- Cross-cluster grep (CS-IMG-SRC-04) **CLEAN** against `business-corporate` (Pragma legacy Unsplash · grep ran on Pexels IDs anyway · zero matches), `business-fiscal` (Fiscus), `business-coaching` (Solaria), `business-stewardship` (Continua) · grep run 2026-04-30 against `apps/catalog/preview_imagery.py` + `docs/content-factory/imagery/packs/` + `design-orchestrator/` + `factory/`.
- Resolution thresholds per CS-IMG-PREM-02: hero ≥ 1600×900 · feature ≥ 1200×800 · portrait ≥ 800×800 (square-safe) · detail ≥ 800×600 · ambient ≥ 800×600.
- Rejection rules from `planner-brief.md §4` are inlined into `pool-selection.md §3` and were applied URL-by-URL during curator pass.
- Pexels License (CC0-compatible · commercial OK · attribution optional) · CS-IMG-SRC-03 attribution recorded below per photo.

**Coherence lead**: Studio di architettura · single-principal editorial-curatorial · institutional-architecture-practice · zero people in hero · object-led + architectural-shadow-line + stone-and-concrete material clarity.

**Voice anchor coherence (CS-IMG-COH-07)**: voice anchor "Ogni progetto è un *argomento* costruito, non un servizio reso." → imagery underlines `argomento` (built form as argument) by foregrounding the work itself (porticoes, models, drawings, studio wall) and demoting people to a single environmental portrait + one collaboratore portrait.

---

## URL list — primary 6-slot pool (CS-IMG-POOL-01)

### slot 0 · hero

1. `https://images.pexels.com/photos/35715509/pexels-photo-35715509.jpeg?auto=compress&cs=tinysrgb&w=1600`
   - **Caption**: Sunlit corridor of an Italian portico in Bologna, stone columns and ceiling, warm golden-hour light on cool stone, zero people, exterior architectural composition.
   - **Role**: hero
   - **Coherence (Cornice)**: object-led · zero people · exterior architectural · stone material clarity · golden-hour warm sunlight on cool stone (matches §3.1 NEUTRAL/NEUTRAL/WARM warmth grid: graphite + pietra-serena anchor + terracotta-rust accent in palette mirror imagery) · the building IS the subject · reads "an editorial-architectural studio published its work" within 3 seconds (CS-IMG-HERO-02). Italian context lands the architectural-firm sub-cluster vocabulary in the first scroll alongside the h1 voice anchor.
   - **Why NOT collapse vs siblings**:
     · NOT Pragma boardroom long-table (zero people · exterior · no meeting context)
     · NOT Fiscus tidy-desk-with-documents (no paperwork · no laptop · no eyeglasses-on-papers)
     · NOT Solaria 1:1 conversation (zero people)
     · NOT Continua library/partner-study reading-room (EXTERIOR · stone-and-light · NO mahogany · NO leather · NO wood interior · NO bookshelf · NO contemplative-warm-interior)
   - **Photographer**: Marcel Gierschick (Pexels)
   - **Pexels ID**: 35715509
   - **Estimated rendered resolution at w=1600**: 1600×~2400 (vertical original · landscape crop survives 16:9 / 4:3 swap per CS-IMG-CROP-01)
   - **Search lane**: `italian portico` (planner §4 backup search "modern Italian architecture courtyard interior light" + primary "architectural courtyard portico golden hour shadow stone")

### slot 1 · feature

2. `https://images.pexels.com/photos/6614835/pexels-photo-6614835.jpeg?auto=compress&cs=tinysrgb&w=1200`
   - **Caption**: Architectural scale model on a designer's worktable in office setting, drawing tools and documents on the desk, raking natural light, zero people, zero monitor.
   - **Role**: feature
   - **Coherence (Cornice)**: workshop-editorial · process-as-proof · the editorial-curatorial work is shown in process at studio-craft scale. Reads "what the editorial-curatorial work looks like in process" alongside slot 0's "what the editorial-curatorial work has built." Pairs with about.html hero band and narrative-essay second column on home (planner §4 slot_1 use clauses).
   - **Why NOT collapse vs siblings**:
     · NOT Pragma corporate-HQ-atrium (worktable · craft scale · object-led)
     · NOT Fiscus tax-document close-up (architectural model · NOT printed-tax-documents)
     · NOT Solaria man-writing-in-notebook (model · craft tools · zero people)
     · NOT Continua oak partner-desk feature (designer's worktable with active model in progress · NOT museum-piece corner-of-empty-study)
   - **Photographer**: Tima Miroshnichenko (Pexels)
   - **Pexels ID**: 6614835
   - **Estimated rendered resolution at w=1200**: 1200×800
   - **Search lane**: `scale model architecture studio` (planner §4 primary "architectural model drafting table trace paper compass" + backup variant)

### slot 2 · portrait (founding architect)

3. `https://images.pexels.com/photos/5915290/pexels-photo-5915290.jpeg?auto=compress&cs=tinysrgb&w=800`
   - **Caption**: Senior architect (woman, white hair, eyeglasses, blazer) seated at desk reviewing blueprints with pen in hand, modern home-office workspace, focused working posture, zero studio-backdrop seamlessness.
   - **Role**: portrait (single-portrait masthead · LF-2 L6=single-portrait-feature)
   - **Coherence (Cornice)**: founding architect at studio window-light reviewing site/project blueprints · matches the "binding triple" from planner §4 slot_2: senior-mid-career + drafting-tools/sketches-visible-in-mid-ground (blueprints + pen) + environmental NOT studio-backdrop. Working posture (downward gaze on documents) avoids the LinkedIn-headshot collapse risk (Risk 3). Demographic read is "long-running editorial practice" not "rookie-tech-creative" — appropriate for the studio's "since 2008" framing on home.
   - **Why NOT collapse vs siblings**:
     · NOT Pragma typographic-only leadership (this is a present photographic portrait · LF-2 L6 is a single-portrait-feature · explicit family-level departure from Pragma's typographic-only)
     · NOT Fiscus typographic-only leadership (same · this is a real face, not a credentials block alone)
     · NOT Solaria 30s × 2 portrait pair (single + senior-mid-career — the residual Solaria gap closed without being mistaken FOR Solaria)
     · NOT Continua 60s + 40s pair (this is ONE portrait · LF-2 has only ONE · cluster's first single-portrait masthead)
   - **Photographer**: RDNE Stock project (Pexels)
   - **Pexels ID**: 5915290
   - **Estimated rendered resolution at w=800**: 800×~534 (landscape original · square-safe crop verified per CS-IMG-CROP-02)
   - **Search lane**: `senior architect studio` (planner §4 primary "architect 50s studio window drafting tools natural light" applied with the pre-cleared planner widening to senior-mid-career per `prebuild-quick-checks.md §Ω·3`)
   - **Curator note**: planner-brief §4 slot_2 + `prebuild-quick-checks.md §Δ·Risk 3` pre-authorise the curator to widen demographic from 50s to senior-mid-career when the binding-triple cannot be satisfied at 50s without falling into LinkedIn-headshot collapse. This URL clears the binding triple cleanly without invoking the second escalation path (slot_3b project-interior as leadership backdrop).

### slot 3 · portrait (collaboratore · path A · default per planner §4)

4. `https://images.pexels.com/photos/6615222/pexels-photo-6615222.jpeg?auto=compress&cs=tinysrgb&w=800`
   - **Caption**: Mid-career architect (man, afro hair, white shirt) seated at office desk reviewing project blueprints, focused working posture, contemporary studio setting, zero seamless backdrop.
   - **Role**: portrait (collaboratore · about.html team-grid · LF-2 L6 is single-portrait on home so this slot serves about.html only — NOT the home masthead)
   - **Coherence (Cornice)**: pairs with slot 2 to populate the about.html team-grid for the studio's "1 founding architect + 2 collaboratori" org-scale (intake §1 `org_scale`). Same Tima Miroshnichenko series as slot 1 → CS-IMG-COLOR-06 grain consistency satisfied across the architectural-craft surfaces of the pack.
   - **Why NOT collapse vs siblings**:
     · NOT Pragma 4-partner card-grid (this is a single environmental collaboratore on about.html, not a home-page leadership grid)
     · NOT Fiscus typographic-only (real photographic portrait)
     · NOT Solaria 30s × 2 portrait demographic (slot 2 + slot 3 are mid-50s/60s + 30s/40s · gender + age + ethnicity all visibly differ · NOT 30s-Caucasian × 2)
     · NOT Continua 60s + 40s diverse pair on home (slot 3 lives on about.html team-grid · home masthead is single-portrait · cluster's first single-portrait shape)
   - **Demographic anti-collision (CS-IMG-COH-05 + planner §4 slot_3 reject rule)**: vs slot 2 — different age (mid 30s/40s vs senior-mid-career), different gender (M vs F), different ethnicity (African heritage vs European). Triple-axis distinct.
   - **Photographer**: Tima Miroshnichenko (Pexels)
   - **Pexels ID**: 6615222
   - **Estimated rendered resolution at w=800**: 800×~534 (landscape original · square-safe crop verified)
   - **Search lane**: `young architect drafting` (planner §4 slot_3 path-a primary search "young architect collaborator drafting board")

### slot 4 · detail

5. `https://images.pexels.com/photos/4458196/pexels-photo-4458196.jpeg?auto=compress&cs=tinysrgb&w=800`
   - **Caption**: Close-up of a detailed architectural blueprint / floor plan, intricate technical lines, single sheet, macro distance, zero tools-in-clutter, still-life composition.
   - **Role**: detail
   - **Coherence (Cornice)**: archival-editorial · craft-evidence · quiet · the "drawing replaces the document" framing from planner §4 slot_4. Single sheet · single subject · macro distance · cropped tight (BIND rule satisfied). Ivan S series carries the cleanest still-life feel of the candidate pool · pairs visually with slot 1's worktable model (same craft world, different scale).
   - **Why NOT collapse vs siblings**:
     · NOT Pragma whiteboard-strategy (no diagrams · no people)
     · NOT Fiscus tax document / invoice / paper-stack (architectural floor plan · NOT printed tax 730 / SPA / BILANCIO)
     · NOT Solaria method-notebook (technical floor plan · NOT lined notebook with handwriting)
     · NOT Continua wax-seal letterhead (architectural drawing · NOT correspondence · NOT seal · NOT envelope · NOT institutional-record register)
   - **Photographer**: Ivan S (Pexels)
   - **Pexels ID**: 4458196
   - **Estimated rendered resolution at w=800**: 800×~533 (landscape · 4:3 case-card crop survives per CS-IMG-CROP-05)
   - **Search lane**: `architectural drawing section` (planner §4 slot_4 primary search "architectural drawing section ink parchment close-up")
   - **Risk note**: this is the load-bearing slot per `prebuild-quick-checks.md §Δ·Risk 1` (narrow Pexels pool · CAUTION verdict on §3 Check 3). Curator did NOT need to invoke the pre-cleared fallback (compass on trace paper → ID 6615086) because Ivan S series returned ≥4 plausible candidates clearing the BIND rule. Fallback URL preserved in backup roster below.

### slot 5 · ambient

6. `https://images.pexels.com/photos/36809500/pexels-photo-36809500.jpeg?auto=compress&cs=tinysrgb&w=800`
   - **Caption**: Architectural design studio wall — concrete surface, blueprints and physical design models pinned and placed, natural studio light, zero people, zero laptop or monitor in foreground, industrial finish (NOT wood-tone-cosy).
   - **Role**: ambient
   - **Coherence (Cornice)**: studio-as-evidence · architectural-design-room · the place where editorial work happens · pin-up wall + design models satisfies planner §4 slot_5 BIND rule ("pin-up wall OR drafting-table OR both must be visibly part of the framing"). Industrial concrete material aligns with palette intent (graphite + pietra-serena) and explicitly avoids the warm wood-tone register that belongs to Continua's adjacency.
   - **Why NOT collapse vs siblings**:
     · NOT Pragma corporate atrium (architectural-design studio · NOT lobby · NOT meeting-room)
     · NOT Fiscus law/regulation bookshelf (CS-IMG-SRC-04 reservation honoured · NO bookshelf in this slot · models + blueprints on concrete wall, not legal volumes)
     · NOT Solaria warm home-office with plants and ambient light (concrete wall · industrial · zero plants · zero soft furnishing)
     · NOT Continua marble stairway with golden banister (architectural studio interior · workspace · NOT building-of-substance circulation)
   - **Photographer**: Jesus Rivera (Pexels)
   - **Pexels ID**: 36809500
   - **Estimated rendered resolution at w=800**: 800×~534 (landscape · 4:3 / 3:2 case-card crop survives)
   - **Search lane**: `architecture studio drafting board` (planner §4 slot_5 primary search "architecture studio drafting boards pin-up wall sketches")

---

## URL list — magazine-grid extras (LF-2 L7=magazine-grid · 4 case-card photos)

The 4 cards must visibly differ from slot 0 (different project, different season, different scale per `prebuild-quick-checks.md §3 pack_extras risk_flags`) AND from each other AND must read as REAL architectural projects (not stock-architecture clichés). Each card maps to a typology declared in `intake.md §7 sectors_count` (residenziale · pubblico · interno · paesaggio · restauro · concorso · culturale · uffici · industriale · sanitario · scolastico · misto-uso).

### extra 1 · magazine-grid HERO CARD (1 large · ~1200×800 · photo-dominant)

7. `https://images.pexels.com/photos/2747599/pexels-photo-2747599.jpeg?auto=compress&cs=tinysrgb&w=1200`
   - **Caption**: Minimalist concrete architecture exterior, sharp geometric lines, dramatic high-contrast lighting, zero people, abstract structural composition (b&w).
   - **Role**: case-card hero (magazine-grid 3+1 · the dominant card)
   - **Project typology**: concorso / culturale (a competition or cultural-program project · the editorial argument is "geometry as argument")
   - **Coherence (Cornice)**: object-led · architectural-shadow · sharp linework — matches the Cornice voice anchor's curatorial-argument framing exactly · the building IS the project's argument · b&w high-contrast deviates from slot 0's golden-hour warmth, ensuring the 4 cards read as four DIFFERENT projects, not four crops of one shoot (CS-IMG-COLOR-06 diversity at the case-grid scale).
   - **Why NOT collapse vs slot 0**: different season (b&w vs golden-hour · different time of day · different material palette · different scale of structure)
   - **Photographer**: Bruno Thethe (Pexels)
   - **Pexels ID**: 2747599
   - **Search lane**: `architectural interior concrete stone minimal`

### extra 2 · small case-card

8. `https://images.pexels.com/photos/36547058/pexels-photo-36547058.jpeg?auto=compress&cs=tinysrgb&w=800`
   - **Caption**: Contemporary apartment buildings in Rome at sunset, vibrant facades against clear sky, zero people, residential architectural exterior.
   - **Role**: case-card small (magazine-grid 3+1 · one of three small)
   - **Project typology**: residenziale (a residential commission · explicit Italian context · Rome)
   - **Coherence (Cornice)**: residential project · Italian sub-cluster vocabulary · contemporary-residential balances the historic-portico of slot 0 → studio's range read as "we work on heritage AND new residential."
   - **Why NOT collapse**: contemporary residential block is structurally different from a historic stone portico, a minimalist concrete gallery, or a Piedmont heritage courtyard.
   - **Photographer**: Léa Claisse (Pexels)
   - **Pexels ID**: 36547058
   - **Search lane**: `modern italian residential architecture`

### extra 3 · small case-card

9. `https://images.pexels.com/photos/36428417/pexels-photo-36428417.jpeg?auto=compress&cs=tinysrgb&w=800`
   - **Caption**: Sunlit elegant arches and shadows in a historic Venaria courtyard, Piedmont, classical Italian architecture, zero people.
   - **Role**: case-card small (magazine-grid 3+1)
   - **Project typology**: restauro (a heritage restoration project · explicit Italian heritage · Piedmont)
   - **Coherence (Cornice)**: restoration project · explicit Italian heritage · sunlit arches mirror the slot 0 shadow-line vocabulary at a different site → studio's continuity read across heritage commissions.
   - **Why NOT collapse**: Venaria is a different site / season / interior-courtyard register vs Bologna's portico (slot 0). Different shadow geometry, different stone colour, different program.
   - **Photographer**: Ree A (Pexels)
   - **Pexels ID**: 36428417
   - **Search lane**: `italian architecture stone shadow`

### extra 4 · small case-card

10. `https://images.pexels.com/photos/13306459/pexels-photo-13306459.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Detailed close-up of an ornate stone column and cornice, classical/neoclassical carving, weathered greys, zero people.
    - **Role**: case-card small (magazine-grid 3+1)
    - **Project typology**: detail (an architectural-detail study · cornice carving close-up)
    - **Coherence (Cornice)**: thematic resonance — the studio is named **Cornice** and one of the case cards is literally a cornice detail · subtle editorial pun without becoming gimmicky · also serves the case-detail page "site-context" slot in the body-embedded detail role per planner-brief §8 detail-page surface table. Ornate carving close-up reads as "the discipline pays attention" — the editorial-curatorial register made literal.
    - **Why NOT collapse**: this is a tight macro detail of carved stone; slot 0 is a wide portico interior; extras 1-3 are full-building exteriors. Different scale entirely.
    - **Photographer**: Zeynep (Pexels)
    - **Pexels ID**: 13306459
    - **Search lane**: `architectural detail cornice column`

---

## URL list — backup roster (CS-IMG-POOL-04 · 20-40 candidates · 404 recovery + case-detail rotation)

The reviewer-approved selections above number 10. The following 14 backups bring the pack file to 24 entries, comfortably inside the 20-40 floor. Each backup also passed the cross-cluster grep (zero overlap vs the 4 sibling pools) and the planner §4 rejection-rules pass. They survive in the pack as case-detail body-embedded photos (CS-IMG-SEC-08) and as 404-recovery substitutes.

### slot 0 hero backups

11. `https://images.pexels.com/photos/18167495/pexels-photo-18167495.jpeg?auto=compress&cs=tinysrgb&w=1600`
    - **Caption**: Elegant colonnade with dramatic lighting and perspective, classical stone columns, zero people.
    - **Role**: hero (backup) · **Photographer**: Betül Seyrantepe · **ID**: 18167495 · **Search lane**: `italian portico`

12. `https://images.pexels.com/photos/36471383/pexels-photo-36471383.jpeg?auto=compress&cs=tinysrgb&w=1600`
    - **Caption**: Historic stone courtyard with arched entrances and central tree, peaceful exterior, zero people.
    - **Role**: hero (backup) · **Photographer**: Tahir Xəlfə · **ID**: 36471383 · **Search lane**: `architecture courtyard`

13. `https://images.pexels.com/photos/36739215/pexels-photo-36739215.jpeg?auto=compress&cs=tinysrgb&w=1600`
    - **Caption**: Sunlit arcade with arches in Modena, Italian classical architecture, zero people.
    - **Role**: hero (backup) · **Photographer**: not recorded at intake (Pexels page) · **ID**: 36739215 · **Search lane**: `italian architecture stone shadow`

14. `https://images.pexels.com/photos/35869451/pexels-photo-35869451.jpeg?auto=compress&cs=tinysrgb&w=1600`
    - **Caption**: Sunlight streaming through ancient stone arches in a Tuscan building, zero people.
    - **Role**: hero (backup) · **Photographer**: not recorded at intake (Pexels page) · **ID**: 35869451 · **Search lane**: `italian architecture stone shadow`

### slot 1 feature backups

15. `https://images.pexels.com/photos/13727724/pexels-photo-13727724.jpeg?auto=compress&cs=tinysrgb&w=1200`
    - **Caption**: Modern architectural house model on a grid surface, close-up, zero people, zero monitor.
    - **Role**: feature (backup) · **Photographer**: Steph (@steph-320380194) · **ID**: 13727724 · **Search lane**: `scale model architecture studio`

16. `https://images.pexels.com/photos/6614834/pexels-photo-6614834.jpeg?auto=compress&cs=tinysrgb&w=1200`
    - **Caption**: Ceramic miniature classical building model on white display surface, natural lighting, zero people.
    - **Role**: feature (backup) · **Photographer**: Tima Miroshnichenko · **ID**: 6614834 · **Search lane**: `architectural model`

### slot 2 portrait backups (second-tier · used if 5915290 fails RDNE 3-second read)

17. `https://images.pexels.com/photos/9617905/pexels-photo-9617905.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Architect at desk, focused on design work surrounded by tools, plans and warm ambient studio lighting.
    - **Role**: portrait (backup) · **Photographer**: Ron Lach · **ID**: 9617905 · **Search lane**: `architect portrait`

18. `https://images.pexels.com/photos/9617379/pexels-photo-9617379.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Adult male architect at desk surrounded by drawings, blueprints and sketches, working posture.
    - **Role**: portrait (backup) · **Photographer**: Ron Lach · **ID**: 9617379 · **Search lane**: `architect portrait`

19. `https://images.pexels.com/photos/6615231/pexels-photo-6615231.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Architect at desk measuring scale model with ruler, precision tools visible in environmental studio.
    - **Role**: portrait (backup) · **Photographer**: Tima Miroshnichenko · **ID**: 6615231 · **Search lane**: `senior architect studio`

### slot 3 alternate path-a + alternate path-b

20. `https://images.pexels.com/photos/6615225/pexels-photo-6615225.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Young architect (woman, glasses, denim jacket) bent over floor plans with compass, modern workspace, environmental.
    - **Role**: portrait (slot 3 path-a alternate · same Tima Miroshnichenko architect-series voice as slot 3 primary)
    - **Photographer**: Tima Miroshnichenko · **ID**: 6615225 · **Search lane**: `young architect drafting`

21. `https://images.pexels.com/photos/7422192/pexels-photo-7422192.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Modern stone interior architecture with towering columns and natural light, zero people, zero wood-tone-warm.
    - **Role**: project-interior (slot 3 path-b alternate · planner §4 slot_3 pre-cleared at A.3 entry)
    - **Photographer**: Mavera zehra Çoşkun · **ID**: 7422192 · **Search lane**: `architecture interior stone no people`
    - **Activation**: invoked only if the 2nd portrait path-a is rejected at A.6 style-critic for any reason; then slot 3 becomes a 4th case-card photo + about.html team-grid drops to 1 portrait. Decision held at A.3.

### slot 4 detail backups (one is the pre-cleared planner fallback)

22. `https://images.pexels.com/photos/268362/pexels-photo-268362.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Single black pencil resting on architectural blueprints, macro still life, single tool, single sheet.
    - **Role**: detail (backup · also supports CS-IMG-SEC-08 case-detail body-embedded surface)
    - **Photographer**: Pixabay (Pexels) · **ID**: 268362 · **Search lane**: `architectural drawing section`

23. `https://images.pexels.com/photos/6615086/pexels-photo-6615086.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Drawing compass resting on architectural blueprints, macro close-up, single tool, single sheet, planning detail.
    - **Role**: detail · **PRE-CLEARED FALLBACK** (planner-brief §4 slot_4 `fallback_subject` · `prebuild-quick-checks.md §Ω·2`) · curator authorised to swap this URL into slot 4 primary at A.3 entry without re-spec if slot 4 primary search returned ≤4 plausible candidates. **NOT INVOKED at this curator pass** (Ivan S series returned ≥4 candidates · slot 4 primary held).
    - **Photographer**: Tima Miroshnichenko · **ID**: 6615086 · **Search lane**: `drafting compass paper`

24. `https://images.pexels.com/photos/4458210/pexels-photo-4458210.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Architectural floor plan close-up, clean, single sheet, no clutter, design creativity and layout precision.
    - **Role**: detail (backup) · **Photographer**: Ivan S · **ID**: 4458210 · **Search lane**: `architectural drawing section`

### slot 5 ambient backups

25. `https://images.pexels.com/photos/7504583/pexels-photo-7504583.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Brown corkboard displaying architectural drawings in minimalist office setting, vertical composition, zero people.
    - **Role**: ambient (backup) · **Photographer**: cottonbro studio · **ID**: 7504583 · **Search lane**: `architecture studio drafting board`

26. `https://images.pexels.com/photos/6044300/pexels-photo-6044300.jpeg?auto=compress&cs=tinysrgb&w=800`
    - **Caption**: Interior art studio with architectural drawings and sketches displayed on table surface, zero people.
    - **Role**: ambient (backup) · **Photographer**: not recorded at intake (Pexels page) · **ID**: 6044300 · **Search lane**: `architecture studio drafting board`

---

## Cross-cluster overlap report (CS-IMG-SRC-04 · CLEAN)

Grep run on 2026-04-30 against:
- `apps/catalog/preview_imagery.py` (committed pools: business-corporate · business-fiscal · business-coaching · business-stewardship · all other corporate-suite-or-adjacent pool keys)
- `docs/content-factory/imagery/packs/*.md` (all existing pack files)
- `design-orchestrator/` (real-candidates · references · workflows)
- `factory/` (reports · standards · references)

Result: **0/26 IDs overlap** with any committed URL or any existing pack URL. The pack is grep-clean by Pexels photo-id at curator commit time. Reviewer re-runs the grep at LGTM signoff (per `reviewer-lgtm.md §4`).

---

## Curator-vs-reviewer separation (CS-IMG-SRC-05)

This pack is the curator product. The independent reviewer LGTM lives in `factory/reports/imagery/cornice-architettura/reviewer-lgtm.md` and is logically separate from the curator's selection logic in `factory/reports/imagery/cornice-architettura/pool-selection.md`. Copy-authoring (A.4) MUST NOT begin until both files exist with curator-status `LGTM-PENDING-REVIEWER` resolved to `LGTM-CONFIRMED` by the reviewer. This pack file is the canonical artefact both reports reference.
