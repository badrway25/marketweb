# Corporate-suite Imagery Standard

**Phase**: X.4a · Corporate-suite Factory Hardening · **Date**: 2026-04-21
**Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Scope**: factory files only · no `apps/editor`, `apps/projects`, `apps/commerce` changes · no new archetypes.
**Inputs**: `factory/reports/audits/corporate-suite-audit-master.md`, `factory/references/template-inventory.md`, `factory/references/pattern-library.md`, `factory/references/anti-pattern-library.md`, `factory/standards/corporate-suite-design-standard.md`.
**Audience**: every agent that selects, validates, or reviews imagery on a corporate-suite template (imagery-curator, template-planner, template-builder, style-critic, browser-verifier, release-gatekeeper). This file is the canonical answer to "is this image acceptable for this template?" — rule-based, not taste-based.

---

## 0 · How to use this document

1. Every rule carries a **severity tag** (same model as the design standard):
   - `[BLOCKING]` — violation prevents flip to `published_live`. Pack cannot be signed off.
   - `[REQUIRED]` — violation must be fixed before the reviewer walk signs off. Pack can be drafted with open TODOs.
   - `[STRONG]` — violation allowed only if explicitly justified in the pack file (`§ deviation`).
   - `[GUIDELINE]` — taste; document the reason if you break it.
2. Every URL in every pack must trace back to at least the BLOCKING rules here by tag (e.g., `CS-IMG-SRC-01`, `CS-IMG-HERO-02`).
3. Pair this document with:
   - `corporate-suite-design-standard.md` (§5 Hero readability, §11 Section composition — imagery is wired through those rules),
   - `corporate-suite-blocking-rules.md` (enforcement recipes — 1:1 with `[BLOCKING]` rules here),
   - `corporate-suite-browser-rubric.md` (the Playwright walk that verifies imagery semantics on the live render),
   - `docs/content-factory/imagery/CURATION_PROTOCOL.md` (upstream curator workflow · binding · §1-7),
   - `docs/content-factory/imagery/blacklist.md` (pattern blacklist, Session 31 incidents).
4. **Pexels-only is non-negotiable for every new template.** Pragma's legacy Unsplash pack is a known gap (AP3) and is scheduled for retro-curation; it is the **only** tolerated exception until the `business-corporate` Pexels pack lands.
5. **Browser live verification has the veto.** A pack that passes curator review and CLI tests can still fail on the live render — the reviewer walk (CS-IMG-BROWSER-01) catches category mismatches and stock-cliché shots that no grep or dimension check can detect.

---

## 1 · Sourcing policy — Pexels-only

### CS-IMG-SRC-01 [BLOCKING] · Pexels is the ONLY source for every new template on this archetype

- **Rule**: every URL in every new imagery pool on this archetype MUST come from Pexels (`images.pexels.com`). No Unsplash, no Shutterstock, no Adobe Stock, no Getty, no custom photography, no AI-generated imagery, no random-web scraping.
- **Rationale**: Pexels is the project-wide primary source (Session 47 adoption · `docs/content-factory/imagery/sources.md`). CC0-compatible, curator audit trail is uniform, deduplication grep covers a single CDN, per-image attribution is traceable via photographer metadata.
- **Enforcement**: `scripts/check_imagery_pack.py` (X.3 C3) greps for non-Pexels hostnames and fails the PR. A reviewer who spots a non-Pexels URL must reject the pack.
- **Single known exception** (legacy, time-limited): `business-corporate` pool (Pragma) at `apps/catalog/preview_imagery.py:312-322` carries 6 legacy Unsplash URLs from Session 32 — pre-dates the X.3 curation protocol. Retro-curate before the next pilot lands on this archetype; do NOT drop the Unsplash URLs until the Pexels replacements are reviewer-approved per CURATION_PROTOCOL §3.5.
- **What this rule does NOT grant**:
  - "Pexels" is the domain test, not the quality test. A Pexels URL can still fail every subsequent rule in this standard (semantic, crop, palette, stock-cliché).
  - "Permissive license" is not an escape hatch — Unsplash is also permissive. License is not the reason; pipeline uniformity is.

### CS-IMG-SRC-02 [BLOCKING] · URL format is the Pexels CDN with explicit `w=` and `auto=compress,cs=tinysrgb`

- **Rule**: every URL uses the shape `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=<width>`. No Pexels preview URLs (`images.pexels.com/search/...`), no missing query string, no raw CDN URLs without compression hints.
- **Width budget** per slot role:
  - `hero` → `w=1600` (min 1600×900 rendered)
  - `feature` → `w=1200` (min 1200×800)
  - `portrait` → `w=800` (min 800×800, aspect close to square)
  - `detail` → `w=800` (min 800×600)
  - `ambient` → `w=800` (min 800×600)
- **Evidence**: `preview_imagery.py:346-358` (Fiscus reference) and `:370-383` (Solaria on-branch reference) both follow this shape.
- **Failure mode**: a hero at `w=800` looks soft on retina; a portrait at `w=1600` blows the byte budget. Use the width budget above, not a default.

### CS-IMG-SRC-03 [REQUIRED] · Per-URL photographer + pexels-id + resolution recorded in the pack file

- **Rule**: every URL entry in `imagery/packs/<cluster>.md` records the photographer name (Pexels attribution), the numeric photo id, and the final resolution actually delivered. This is the audit trail that makes deduplication and re-source possible.
- **Rationale**: CC0 does not require attribution, but audit trail does. If a URL 404s later, the photographer metadata lets the curator find the replacement.

### CS-IMG-SRC-04 [BLOCKING] · One URL = one cluster · zero cross-cluster reuse

- **Rule**: a given Pexels URL appears in AT MOST one cluster's pool. Genuinely neutral textures (paper grain, concrete wall) may repeat, but only with an explicit comment in both packs.
- **Incident reference**: Session 38 — `portfolio-photographer[0-1]` reused `restaurant-fine[0-1]` URLs under a "proven offline-safe" rationale. All 6 URLs were swapped.
- **Enforcement**: `scripts/check_imagery_pack.py` greps every pack against all other packs and fails on duplicates.
- **Cross-reference**: AP6.

### CS-IMG-SRC-05 [REQUIRED] · Pack file reviewer ≠ curator

- **Rule**: the curator produces the pack; a separate reviewer signs off (CURATION_PROTOCOL §6). The copy author begins only after LGTM. This is a process rule, not a taste rule.

---

## 2 · The 6-slot imagery pool — slot roles and minimum distribution

This section codifies pattern A4 (6-slot pool shape) and is the contract every template on this archetype ships against.

### CS-IMG-POOL-01 [BLOCKING] · Pool shape is `[hero, feature, portrait, portrait, detail, ambient]` in that exact order

- **Rule**: every imagery pool keyed under `apps/catalog/preview_imagery.py` as `business-<kind>` for a corporate-suite template MUST list exactly 6 URLs in this slot order:
  - **0 · hero** — the above-the-fold full-bleed photo on `home.html`. Sets the mood. ≥ 1600×900.
  - **1 · feature** — institutional/contextual wide shot used in secondary home sections and on `about.html`. ≥ 1200×800.
  - **2 · portrait** — first leadership portrait, square-ish, ≥ 800×800.
  - **3 · portrait** — second leadership portrait, square-ish, ≥ 800×800, different person from slot 2.
  - **4 · detail** — close-up of the work itself (documents, instruments, artefacts). ≥ 800×600.
  - **5 · ambient** — environmental/contextual shot (bookshelf, atrium, tools in situ). ≥ 800×600.
- **Evidence**: `business-corporate` (l.312), `business-fiscal` (l.346), `business-coaching` (l.370 on branch).
- **Why it blocks**: the preview composition (`templates/preview_compositions/business/corporate-suite.html`) reads slots by index; a reordered pool renders the wrong photo in the wrong frame.
- **Mutability**: new archetypes may pick a different shape, but the corporate-suite archetype is frozen at this 6-slot contract.

### CS-IMG-POOL-02 [BLOCKING] · Minimum image distribution across page sections

Every LIVE template on this archetype MUST carry AT LEAST the following imagery presence across the 7 skin files:

| Page | Imagery presence (minimum) | Slot sources |
|---|---|---|
| `home.html` | Hero photo (1) + leadership portraits (2) + case-card photos (3-6) + trust/sectors visuals (logo marquee) | slot 0 · slots 2-3 · slots 4-5 |
| `about.html` | Feature/history shot (1) + team-grid portraits (3-6) | slot 1 · slots 2-3 (repeat OK) |
| `services.html` | Feature or ambient shot (1) + optional process-strip icon set | slot 1 or slot 5 |
| `case_study_list.html` | Card thumbnail per case (3-6) | slots 4 / 5 rotated |
| `case_study_detail.html` | Hero-scale case photo (1) + body-embedded detail (1-2) + team-strip portraits (2-3) | slot 0 variant or slot 1 · slot 4 · slots 2-3 |
| `contact.html` | Ambient studio/office photo (1) + optional map tile | slot 5 |
| Preview tile composition | Slot 0 hero-dominant · slot 1 secondary · slots 2-5 micro-tile rotation | all 6 slots in composition |

- **Test**: walk the live render top-to-bottom across the 6 pages; count photographic surfaces. If a page has zero photos, it must be deliberate (services sometimes is — flag in docstring); otherwise it fails.
- **Cross-reference**: CS-COMP-01 (sectors ribbon), CS-COMP-02 (leadership portraits), CS-COMP-03 (case cards) in the design standard.

### CS-IMG-POOL-03 [REQUIRED] · Pool key naming convention is `business-<kind>`

- **Rule**: corporate-suite pools use the `business-` prefix (`business-corporate`, `business-fiscal`, `business-coaching`). New pilots on this archetype extend the same namespace.
- **Why**: grep-ability. A maintainer looking for "every corporate-suite pool" runs one grep.

### CS-IMG-POOL-04 [REQUIRED] · The pack file carries more candidates than the pool uses

- **Rule**: the pack file (`imagery/packs/<cluster>.md`) holds 20-40 curated URLs (CURATION_PROTOCOL §6). The pool (`preview_imagery.py`) selects 6 of those. The extras survive in the pack as backup if a URL 404s or if a case-detail page needs an alternate.

---

## 3 · Image-to-copy coherence rules

Imagery must match what the copy is actually saying — cluster, profession, and voice anchor. Tests cannot catch this; the curator + reviewer + browser walk can.

### CS-IMG-COH-01 [BLOCKING] · Subject match to the profession

- **Rule**: every photo depicts a subject a member of this profession would recognize as "their world." A commercialista looking at `business-fiscal` sees desks with paperwork, professionals in focus, document close-ups — NOT generic boardroom handshakes. A corporate advisor looking at `business-corporate` sees boardroom long-tables, corporate HQ atriums, executive portraits — NOT startup open-plan laptop rows.
- **Test** (binding per CURATION_PROTOCOL §3.3): "open each URL, look at the image for ≥ 3 seconds, ask: does a person in this profession recognize this as their world?" If not, discard.
- **Incident reference** (Session 31 · AP4): PlayStation gamepad shipped as "map of Rome"; tuna can as "artisan ingredients". Each was a URL the author trusted without opening. Zero passed the 3-second read.

### CS-IMG-COH-02 [BLOCKING] · Mood match to the voice anchor

- **Rule**: the image's visual mood (lighting, palette, posture) aligns with the template's voice anchor (blueprint §5 · pattern F2).
  - `business-corporate` (Pragma) · "Dove si prendono le decisioni che contano" → boardroom gravitas · dark daylight · serious posture.
  - `business-fiscal` (Fiscus) · "L'adempimento corretto, non la trovata" → warm-neutral institutional · focused professionals · no smile-at-camera stock.
  - `business-coaching` (Solaria) · "Il coaching non è terapia e non è consulenza" → warm-earth 1-to-1 setting · studio/dialogue posture · no mountain peaks, no arrow-on-whiteboard (AP9).
- **Test**: if the image would fit equally well behind a coaching funnel ad and an advisory firm's homepage, the mood isn't specific enough — discard.

### CS-IMG-COH-03 [BLOCKING] · Cluster-specific terminology match

- **Rule**: if the copy names a credential or specialty (ODCEC, Revisore Legale, ICF PCC, Cassazionista), the accompanying imagery cannot contradict it. A "medical scrubs" portrait next to "Cassazionista" copy fails instantly.
- **Test**: grep the leadership `credentials` field; for each credential, ask "does the portrait set suggest this world?" If the credentials point to legal/tax/advisory but the portraits show lab coats or coaching hoodies, fail.

### CS-IMG-COH-04 [REQUIRED] · No visible product placement or logos

- **Rule**: zero visible brand logos (no Apple laptops with glowing logo visible, no Nespresso machine in view, no Starbucks cup on the desk, no ThinkPad lid). Neutral unbranded equipment is preferred.
- **Rationale**: product placement is an unintended endorsement + license risk + breaks the "real firm's site" illusion (CS-MARKET-05 pattern).
- **Exception**: industry-association logos in the marquee (ODCEC, Assolombarda, CONSOB) — these are legitimate trust signals, not product placements.

### CS-IMG-COH-05 [REQUIRED] · Portraits show age, gender, ethnicity diversity where plausible for Italian market

- **Rule**: leadership and team portraits are NOT a mono-demographic lineup unless the cluster has an explicit rationale (very rare). Default: mixed age, mixed gender, plausible-for-Italy ethnicity mix.
- **Rationale**: a 3-person leadership block rendering as three 55-year-old white men in navy suits reads as stock-plate-cliché and dates the site.
- **Cross-reference**: CURATION_PROTOCOL §4.

### CS-IMG-COH-06 [REQUIRED] · Caption + role + coherence statement required for every URL

- **Rule**: for every URL in the pack, the curator records:
  1. A **1-sentence semantic caption** describing what's actually in the image (descriptive, not aspirational): *"Professional woman, glasses, at wooden desk reviewing printed financial statements, warm window light."*
  2. The **slot role** (`hero`, `feature`, `portrait`, `detail`, `ambient`).
  3. A **coherence justification** (1 sentence) mapping to cluster positioning.
- **Rationale**: a URL that cannot support all three is ambiguous and will fail in rendering. This is the single strongest guardrail against Session 31-class errors.

### CS-IMG-COH-07 [REQUIRED] · Voice anchor is preserved verbatim; imagery underlines it, never contradicts it

- **Rule**: imagery supports the voice anchor; it never argues against it. Coaching anchor "Il coaching non è terapia" + imagery of a therapy couch = instant disqualification.
- **Cross-reference**: CS-EXEC-01 (design standard · voice anchor verbatim across locales).

---

## 4 · What qualifies as premium imagery

Corporate-suite is an ultra-premium archetype. Premium is checkable — it is not "I know it when I see it."

### CS-IMG-PREM-01 [BLOCKING] · Editorial, not stock-plate

- **Rule**: premium photography reads as **editorial** — it looks like it was shot for a magazine feature, not for a stock library. Operational signals:
  - Natural or considered light (window daylight, practical fixtures), NOT flat even-fill studio stock light.
  - Specific setting (a real boardroom, a real office, a real desk with real papers), NOT generic white backdrop.
  - Composition has intent (leading lines, rule-of-thirds, depth), NOT center-framed centered subject.
  - Subjects in natural posture (mid-action, looking at work), NOT facing camera and smiling.
- **Acceptable example**: *Fiscus slot 0* — `pexels-photo-8927688` — tidy workspace, laptop, documents, eyeglasses, warm window light, subject's hands visible, no face-to-camera shot.
- **Unacceptable example**: *"Smiling businesswoman shaking hands in vague office, studio light, white teeth, stock pose"* — this is the Session 31 cliché.

### CS-IMG-PREM-02 [BLOCKING] · Resolution floor

- **Rule**:
  - Hero (slot 0): ≥ 1600 × 900 native resolution (the Pexels `w=1600` delivery is the floor).
  - Feature (slot 1): ≥ 1200 × 800.
  - Portraits (slots 2-3): ≥ 800 × 800 and aspect close to square (±10%).
  - Detail (slot 4): ≥ 800 × 600.
  - Ambient (slot 5): ≥ 800 × 600.
- **Rationale**: below these floors the hero reads soft on retina and the portrait reads pixelated on card grids.
- **Cross-reference**: pattern G3, CURATION_PROTOCOL §3.2, `imagery/blacklist.md` §4.

### CS-IMG-PREM-03 [REQUIRED] · Color grading reads as institutional, not consumer

- **Rule**: preferred grading is muted-neutral-warm (institutional) or low-saturation-cool (corporate-advisory). AVOID:
  - Punchy HDR with blown highlights.
  - Teal-and-orange cinematic grading.
  - Heavy Instagram-style vignettes and film-emulation presets.
- **Test**: if the image would fit a wedding-photographer's Instagram feed, it is NOT premium for this archetype.

### CS-IMG-PREM-04 [REQUIRED] · Depth and negative space

- **Rule**: premium editorial shots leave negative space the copy composition can breathe into. Shots that fill every pixel with subject matter clash with the skin's 100×72 section padding (CS-TONE-02 / CS-RHYTHM-01).
- **Acceptable**: a long boardroom table receding into soft-focus distance, empty headroom above the subject.
- **Unacceptable**: 14 people all in frame, zero negative space, every pixel busy.

### CS-IMG-PREM-05 [REQUIRED] · Specificity reads premium; genericity reads stock

- **Rule**: the more specific the subject (an actual document on the desk, actual instruments in view, a specific architectural detail), the more premium. Generic stand-in subjects read as stock fallback.
- **Test**: "if I changed the surrounding copy from commercialista to dentist to coach, would this image still work?" If yes → too generic → reject.

---

## 5 · What qualifies as dynamic imagery

Dynamic ≠ animated. On this archetype dynamic means the image carries motion, posture, or action that keeps the page from reading as a static diorama.

### CS-IMG-DYN-01 [REQUIRED] · Motion implied in hero and feature slots

- **Rule**: slot 0 (hero) and slot 1 (feature) should carry IMPLIED motion — people in mid-action (writing, reviewing, walking through space), light shifting across a surface, a door opening, hands mid-gesture. Static centered headshots do not belong in slots 0-1.
- **Acceptable**: subject leaning over a document with a pen in hand; light streaming through a corridor.
- **Unacceptable**: a person standing arms-crossed in a lobby looking straight at the camera (hero slot).

### CS-IMG-DYN-02 [STRONG] · Portrait slots may be static, but posture is working-posture

- **Rule**: slots 2-3 (portraits) are allowed to be static headshots since they carry the leadership identity, BUT the posture is working-posture: mid-consultation, mid-review, natural expression — NOT the plate-of-stock "smile at camera with crossed arms."
- **Test**: ask "is this person clearly in the middle of their work, or clearly posed for a stock photo?"

### CS-IMG-DYN-03 [STRONG] · Detail and ambient slots carry environmental motion cues

- **Rule**: slots 4-5 (detail / ambient) imply the space is lived-in and working — open folders, marked-up papers, half-drunk coffee (unbranded), afternoon light moving across a floor — NOT a sterile-staged product shot.
- **Rationale**: a lived-in ambient makes the firm feel real. A sterile staged shot feels like a catalog page.

### CS-IMG-DYN-04 [GUIDELINE] · Animation/parallax/video backgrounds are forbidden in the hero

- **Rule**: the hero frame is a still editorial photograph. No video backgrounds, no canvas-animated particles, no parallax scroll that tilts the hero photo.
- **Rationale**: advisory/institutional voice does not tolerate consumer-motion. Motion here reads as SaaS landing page (CS-TONE-01 violation).

---

## 6 · What qualifies as professional / corporate imagery

Professional/corporate on this archetype has specific visual markers. This section converts the adjective into selection criteria.

### CS-IMG-PRO-01 [BLOCKING] · Dress code and posture read as the profession

- **Rule**: business-corporate / business-fiscal / business-advisory imagery shows tailored workwear (suits, formal shirts, blazers, conservative dresses), neat grooming, and upright working posture. Coaching is an exception — `business-coaching` reads warm-earth casual-professional (knitwear, linen), but never gym clothes, never sportswear.
- **Counterexample**: a "fiscal" portrait of someone in a hoodie at a coworking hot-desk fails. That's a `business-startup` subject.

### CS-IMG-PRO-02 [BLOCKING] · Setting is institutional, not coworking or café

- **Rule**: backgrounds show real offices, conference rooms, atriums, law-library shelves, formal meeting spaces. Coworking-lofts with exposed brick, cafés, and coffee-shop-as-office all fail. They belong to `business-startup`, which is a sibling archetype, not corporate-suite.
- **Test**: a reader cannot mistake the setting for a WeWork, a Starbucks, or a home office.

### CS-IMG-PRO-03 [REQUIRED] · Working artifacts are cluster-specific

- **Rule**: the detail and ambient slots show artifacts that name the work:
  - Fiscal: printed tax documents, calculators, folders labelled with `SPA`, `BILANCIO`, `730`, magnifying glass on a line item.
  - Corporate/advisory: whiteboard with strategy diagrams (hand-drawn, not stock vector), printed financial statements, leather portfolios.
  - Law: bound volumes of codici (Codice Civile, Codice Penale), gavel-free desks (gavels are US-TV cliché — AVOID in Italian law context), fountain pens, dossiers.
  - Coaching: notebooks mid-writing, two mugs on a low table, framed ICF/EMCC diploma on a wall.
- **Rationale**: specificity is professionalism; genericity is stock.

### CS-IMG-PRO-04 [REQUIRED] · No consumer-tech or gaming artifacts

- **Rule**: no gaming controllers, no RGB-lit keyboards, no streaming/podcast microphones on a boom arm, no tablets with Netflix UI visible. All of these read consumer-tech / gamer / influencer — not advisory.
- **Cross-reference**: Session 31 PlayStation gamepad incident (AP4, CURATION_PROTOCOL §Why).

### CS-IMG-PRO-05 [STRONG] · No over-diverse "multi-ethnic team pointing at a whiteboard" tropes

- **Rule**: CS-IMG-COH-05 calls for representation, but NOT at the cost of stock-cliché. The "15-people multi-ethnic team pointing at a whiteboard" is a named Session-31 anti-pattern. Real diversity without the cliché means individual portraits or small-group shots, each reading as actual working moments.

---

## 7 · Crop suitability and focal-point rules

Hero and card images render at fixed aspect ratios set by the skin. Choosing a URL whose subject sits in a crop-hostile spot breaks the render even when the image is otherwise perfect.

### CS-IMG-CROP-01 [BLOCKING] · Hero aspect ratio tolerates 16:9 → 4:3 across viewports

- **Rule**: `home.html:5-67` hero photo occupies the right column of the 55/45 split. On desktop (≥ 1101 px) it renders at roughly 4:3. At ≤ 720 px (CS-HERO-07 stacked layout) it renders at roughly 16:9. The chosen hero URL must survive BOTH crops with the subject intact.
- **Test**: mentally crop the image at 4:3 (desktop) AND at 16:9 (mobile stacked) — the subject must remain legible and centered-enough in both. Edge-of-frame subjects fail.
- **Rationale**: CS-RESPONSIVE-05 forces `object-fit: cover` with `aspect-ratio` lock. `object-fit: cover` crops; it doesn't letterbox.

### CS-IMG-CROP-02 [BLOCKING] · Portrait slots use square-safe framing

- **Rule**: slot 2-3 portraits render at `aspect-ratio: 1/1` on the card grid. The subject must be centered enough that a 1:1 square crop of the image does not decapitate, truncate to profile-only, or cut the subject in half.
- **Rationale**: CS-DENSITY-05 (3-6 leadership portraits in grid) + CS-RESPONSIVE-05 (aspect-ratio-locked cards) = every portrait gets square-cropped at render time.

### CS-IMG-CROP-03 [BLOCKING] · Focal point is the subject's face or action-zone · NOT a corner

- **Rule**: the primary subject sits in the central 60% of the frame. No action-in-the-corner compositions that will be cropped out at mobile.
- **Test**: draw a central 60% rectangle on the image; the face (portrait) or action-zone (hero/feature) must fall inside.

### CS-IMG-CROP-04 [REQUIRED] · No hard horizon lines crossing the subject's head

- **Rule**: a strong horizontal line (desk edge, window frame, horizon) must not bisect the subject's head. This is a basic photography rule — ignored, it creates "horizon-slicing-head" renders that read amateur.

### CS-IMG-CROP-05 [REQUIRED] · Card-grid shots tolerate 4:3 and 3:2 with object-fit: cover

- **Rule**: case-study card thumbnails render at `aspect-ratio: 4/3` or `3/2` (CS-RESPONSIVE-05). Chosen thumbnail URLs must survive both crops. Tall portrait-orientation shots in a 3:2 card get top-cropped to near-empty sky.

### CS-IMG-CROP-06 [REQUIRED] · Preview-tile composition is hero-led · slot 0 dominates

- **Rule**: `templates/preview_compositions/business/corporate-suite.html` (313 lines) renders slot 0 as the dominant tile with slots 1-5 as smaller adjacent frames. Slot 0's crop must work as a big editorial dominant AND as a small thumbnail.

---

## 8 · Color compatibility with palette and text overlays

Imagery and palette must coexist. A photo that fights the palette makes the page look wrong even if every other rule passes.

### CS-IMG-COLOR-01 [BLOCKING] · Hero image does not compete with `--primary` text left of it

- **Rule**: the hero split renders serif h1 (in `--primary`, dark) on cream paper LEFT, and the hero photo RIGHT. The photo's left edge (the boundary between the text column and the photo) must be calm — no bright white blowouts, no busy high-contrast edge that visually fights the h1.
- **Test**: sample the leftmost 10% of the hero photo; if it's visually louder than the h1 text, the reader's eye lands on the photo edge instead of the headline. Reject.

### CS-IMG-COLOR-02 [BLOCKING] · Credit overlay and caption chips stay legible on the photo

- **Rule**: the hero carries a credit overlay (pattern C1 · "editorial not stock" marker). The overlay renders at `color: var(--on-dark)` on a semi-opaque dark scrim. The underlying photo region (usually bottom-left) must not fight the overlay — sample the overlay zone for luminance; if it's blown-out white, the scrim won't rescue legibility.
- **Test**: load the live render at 1920×1080; inspect overlay contrast ratio vs scrim + photo; must hit WCAG AA 4.5:1 minimum on the overlay text.

### CS-IMG-COLOR-03 [REQUIRED] · Imagery palette does not clash with template palette

- **Rule**: template palettes on this archetype are constrained (CS-PAL-01 dark `--primary`, warm/cool secondary+accent pair). The imagery should read as compatible:
  - `business-corporate` (Pragma navy/blue/emerald) → imagery grades cool-neutral.
  - `business-fiscal` (Fiscus charcoal/gold/navy) → imagery grades warm-neutral with ochre or natural-wood tones.
  - `business-coaching` (Solaria warm-carbon/ocra/caramel) → imagery grades warm-earth, sunlight, natural materials.
- **Failure mode**: a bright-teal-and-magenta shot in a warm-carbon-and-ocra template — reads as mismatched.
- **Test**: place the hero photo next to the template palette swatch in the pack file. Do they read as the same world?

### CS-IMG-COLOR-04 [REQUIRED] · No bright brand-hostile hues dominating a slot

- **Rule**: a single slot image must not be dominated by a hue the template palette fights (e.g., a bright red sports-car image in a template whose accent is emerald green). The imagery carries its own quiet palette that can cohabit with the template tokens.
- **Exception**: a deliberate, single, small accent hit in an otherwise muted photo is fine and often premium (e.g., a flash of amber in an otherwise gray boardroom shot).

### CS-IMG-COLOR-05 [REQUIRED] · Dark-section photo overlays must not plunge below AA

- **Rule**: when a photo appears in a section with `background: var(--primary)` (dark) and overlaid light text (CS-PAL-04), the photo is usually dimmed with a scrim. The final rendered text must hit WCAG AA 4.5:1 against the scrim-photo composite, not just against the scrim alone.

### CS-IMG-COLOR-06 [STRONG] · Photographic grain and noise level is uniform across the pool

- **Rule**: the 6 URLs in a pool read as shot by a consistent visual sensibility — similar grain, similar grading, similar exposure profile. Six URLs each from a wildly different color science make the pool feel like a clip-art bag.
- **Test**: line up thumbnails of all 6 URLs in the pack file. Do they feel like six frames of one campaign, or like six random stock buys?

---

## 9 · Hero image rules

The hero photo is the single most important image on the template. Extra-strict rules apply.

### CS-IMG-HERO-01 [BLOCKING] · Hero photo comes from the curated Pexels pack · slot 0

- **Rule**: the hero photo MUST be `preview_imagery.py` slot 0 of the template's pool AND present in the approved pack file. No drop-ins, no "I found a better one at authoring time."
- **Rationale**: the pack is reviewer-approved; a drop-in photo bypasses the review gate.

### CS-IMG-HERO-02 [BLOCKING] · Hero is editorial, specific, cluster-recognizable within 3 seconds

- **Rule**: a reader landing on the page gives the hero 3 seconds. In that window the image must answer "what does this firm do?" A generic office lobby fails. A boardroom long-table with printed agendas passes for a corporate-advisory template.
- **Cross-reference**: CS-HERO-02 in the design standard.

### CS-IMG-HERO-03 [BLOCKING] · Hero resolution ≥ 1600×900 rendered

- **Rule**: the URL delivers at least 1600×900 with the Pexels `w=1600` parameter. Soft/pixelated hero on retina fails.

### CS-IMG-HERO-04 [BLOCKING] · Hero survives the 4:3 ↔ 16:9 crop swap

- **Rule**: see CS-IMG-CROP-01. Test both crops before the pack is approved.

### CS-IMG-HERO-05 [BLOCKING] · No people looking at the camera in the hero

- **Rule**: hero subjects are seen mid-action OR seen in profile / three-quarter. A face staring dead at the camera reads as corporate-headshot stock and collapses the editorial feel.
- **Exception**: a deliberate direct-gaze portrait for a coaching cluster is allowed if the blueprint §8 explicitly calls for it; the deviation is noted in the pack file.

### CS-IMG-HERO-06 [REQUIRED] · Hero left-edge is calm (pairs with CS-IMG-COLOR-01)

- **Rule**: the edge where the photo meets the text column is not visually loud. Busy left edges pull the eye off the h1.

### CS-IMG-HERO-07 [REQUIRED] · Hero carries implied motion or mid-action posture

- **Rule**: see CS-IMG-DYN-01. The hero is where the archetype's "firm is at work right now" tone has to read loudest.

### CS-IMG-HERO-08 [REQUIRED] · Hero carries credit overlay · labels image as editorial

- **Rule**: the skin renders a credit overlay on the hero (`home.html:5-67` · pattern C1). The overlay text names the photographer or the editorial context. Missing credit overlay = the image reads as uncredited stock.

---

## 10 · Section image rules

Beyond the hero, each section has specific imagery expectations.

### CS-IMG-SEC-01 [REQUIRED] · Pillars section is icon-led, NOT photo-led

- **Rule**: the pillars/services grid on `home.html` is typographic + icon, NOT photographic. Do not place 3-4 small photos in pillar cards — that reads as link-card-grid, not advisory.
- **Cross-reference**: CS-DENSITY-02.

### CS-IMG-SEC-02 [BLOCKING] · KPI band has zero photography

- **Rule**: the dark KPI band (`home.html:91-122`) carries tabular numerics on a dark surface. No photo backgrounds, no watermark photography, no blurred hero repeats. This is a typographic section.
- **Rationale**: mixing photo and dark-surface numerics fights the institutional cadence.

### CS-IMG-SEC-03 [BLOCKING] · Leadership section uses real portraits from slots 2-3

- **Rule**: leadership block uses actual Pexels portraits (square-safe, ≥ 800×800). NO avatar placeholders, NO initial-in-a-circle, NO grey silhouettes. If a real portrait for a role is missing, the role is cut, not filled with a placeholder.
- **Cross-reference**: CS-COMP-02, CS-MARKET-06.

### CS-IMG-SEC-04 [REQUIRED] · Sectors ribbon is text-led · trust marquee uses industry-association marks only

- **Rule**: the sectors ribbon is text ("Manifattura · Retail · Real Estate · Wellness"). The adjacent trust marquee uses industry-association logos (ODCEC, Assolombarda, CONSOB) — never fake client logos.
- **Cross-reference**: CS-COMP-01.

### CS-IMG-SEC-05 [REQUIRED] · Case cards use slots 4-5 · hero slot is NOT reused as a case thumbnail

- **Rule**: home case-card grid pulls from slots 4 (detail) and 5 (ambient), rotated. Slot 0 (hero) is not reused as a case thumbnail — that duplication reads as "we had 1 photo and split it."
- **Cross-reference**: CS-COMP-03.

### CS-IMG-SEC-06 [REQUIRED] · About timeline uses feature-slot photo OR goes photo-less

- **Rule**: about page opens with a timeline (CS-COMP-06). It may feature a slot-1 feature photo as a wide above-timeline image, OR be entirely typographic. What it must NOT do: sprinkle small decorative photos between timeline rows.

### CS-IMG-SEC-07 [REQUIRED] · Services page uses at most one feature-slot photo

- **Rule**: services page is card-grid + process-strip. One feature-slot photo at section break max. Services is a typographic information page, not a photo gallery.

### CS-IMG-SEC-08 [REQUIRED] · Case-study detail pages lift the photo budget

- **Rule**: case-study detail (`case_study_detail.html`) is the one page where photo budget can exceed the pool's 6 URLs — it pulls from the pack's extended roster (CS-IMG-POOL-04) for the hero + embedded detail + team-strip. Every extended URL still passes all rules in this document.

### CS-IMG-SEC-09 [REQUIRED] · Contact page uses one ambient photo max

- **Rule**: contact page (`contact.html`) carries form + coordinates. Imagery presence: AT MOST one ambient studio/office photo (slot 5) in the coordinates column. Optional map tile beside it. No hero photo, no portrait wall.

### CS-IMG-SEC-10 [REQUIRED] · Dark-section child imagery uses scrim if text overlays are present

- **Rule**: if a photo appears inside `.cs-section.dark` with overlaid text (rare · see CS-RHYTHM-03 · one dark band per home), the photo is darkened/scrimmed so the light text meets AA. No un-scrimmed photos behind body copy on dark sections.

---

## 11 · Image rhythm across sections

Rhythm is the cadence of photo vs typography down the home page. Wrong rhythm reads as a gallery, not an advisory firm.

### CS-IMG-RHYTHM-01 [BLOCKING] · Home photographic cadence: hero — (typographic) — (typographic-dark) — (typographic-trust) — portrait-grid — case-photo-grid — (typographic CTA)

- **Rule**: follow the fixed section order (CS-RHYTHM-02) and let photos appear in the sections the contract places them in:
  - **Hero** — ONE big editorial photo (slot 0). [PHOTO]
  - **Pillars** — icon-typographic. [NO PHOTO]
  - **KPI band** — dark typographic. [NO PHOTO]
  - **Sectors ribbon + trust marquee** — text + industry-association marks. [LOGO MARKS, NOT PHOTOS]
  - **Leadership** — portrait grid. [PORTRAITS: slots 2-3 rotated]
  - **Cases** — case-card grid. [SLOTS 4-5 rotated]
  - **CTA** — typographic with optional single ambient photo. [0-1 PHOTO]
- **Why it blocks**: rhythm-violations (e.g., photo-heavy pillars, decorative photos in the KPI band) visibly degrade the advisory voice. This is the single clearest diagnostic for "does this archetype feel institutional?"

### CS-IMG-RHYTHM-02 [REQUIRED] · No two adjacent photo-heavy sections

- **Rule**: the archetype's rhythm alternates photographic and typographic beats. Leadership (photos) is followed by Cases (photos) — this is allowed because portraits vs case-detail visuals read as different registers. But two consecutive hero-scale full-bleed photos are forbidden.

### CS-IMG-RHYTHM-03 [REQUIRED] · Photo density decreases as you approach the CTA

- **Rule**: home starts with a big hero (photographic peak), goes through typographic breath (pillars, KPI, sectors), re-enters photographic zones (leadership, cases), and closes on a near-photo-less CTA. The CTA section must feel like a pause, not a peak.

### CS-IMG-RHYTHM-04 [STRONG] · Cross-page rhythm: detail-page hero is allowed · list-page cards dense · contact near-empty

- **Rule**: zoom out across the 6 page set. `home` and `case_study_detail` carry photographic weight. `case_study_list` carries card-density photographic weight. `about` / `services` / `contact` are light on imagery. This asymmetry is intentional — photographic energy is not uniform.

### CS-IMG-RHYTHM-05 [REQUIRED] · Preview-tile composition reads as a single image, not a collage

- **Rule**: the marketplace preview tile composes slot 0 as dominant + slots 1-5 as supporting frames. The composed tile must read as a unified editorial sheet, not as a 6-up photo collage. If the tile reads as a collage, the pool's visual consistency (CS-IMG-COLOR-06) is failing.

---

## 12 · Anti-patterns to reject

Consolidates named anti-patterns (AP3 → AP6 and blacklist) into explicit rejection rules.

### CS-IMG-AP-01 [BLOCKING] · Non-Pexels URLs on new templates

- **Failure**: an Unsplash, Shutterstock, Getty, or raw-web URL in a NEW template's pool.
- **Detection**: grep the pool for non-`images.pexels.com` hostnames.
- **Fix**: replace with a Pexels equivalent from the reviewer-approved pack.
- **Reference**: AP3, CS-IMG-SRC-01.

### CS-IMG-AP-02 [BLOCKING] · Category-mismatched imagery

- **Failure modes** (Session 31 · repo-documented):
  - PlayStation gamepad as "map of Rome" on a real-estate template.
  - Bumble Bee tuna can as "artisan ingredients" on a bottega.
  - Hairstylists' portraits as "before/after dermatology" on a medical template.
  - Diamond ring as "oysterman's portrait" on a Luxe editorial tile.
- **Detection**: URL-by-URL 3-second semantic read during curator review (CS-IMG-COH-01). Browser walk catches residuals.
- **Fix**: discard + re-source from cluster-matched search.
- **Reference**: AP4, CURATION_PROTOCOL §3.3.

### CS-IMG-AP-03 [BLOCKING] · Generic stock fallback

- **Failure modes** (from `imagery/blacklist.md` §2):
  - "Generic laptop on clean white desk."
  - "Smiling businesswoman shaking hands in vague office."
  - "Chef holding a plate, looking at camera, perfectly lit."
  - "Multi-ethnic team pointing at a whiteboard."
  - "Two men in suits reviewing a tablet, staged handshake lighting."
  - "Young professional on phone, bright window behind, forced smile."
- **Detection**: CS-IMG-PREM-05 test — "if I changed the surrounding copy from commercialista to dentist to coach, would this image still work?"
- **Fix**: re-source with specific subject (actual documents, actual instruments, actual room).
- **Reference**: AP5.

### CS-IMG-AP-04 [BLOCKING] · Cross-cluster URL reuse

- **Failure**: the same Pexels URL appearing in two different cluster pools.
- **Detection**: `scripts/check_imagery_pack.py` greps all packs.
- **Fix**: swap one of the two URLs.
- **Reference**: AP6, CS-IMG-SRC-04.

### CS-IMG-AP-05 [BLOCKING] · Placeholder imagery in live render

- **Failure modes**:
  - Grey silhouette "person icon" avatar.
  - Initial-in-a-circle avatar.
  - Picture-of-a-camera icon "upload photo" placeholder.
  - Any editor-UI-only affordance leaking into the public render.
- **Detection**: load live URL in incognito, walk the 6 pages.
- **Fix**: either ship a real portrait or cut the slot.
- **Reference**: CS-MARKET-06, CS-IMG-SEC-03.

### CS-IMG-AP-06 [BLOCKING] · Coaching-cluster imagery clichés

- **Failure modes** (from `cluster_blueprints/coaching.md` §13):
  - Mountain-peak photography.
  - Drawn arrows on whiteboards.
  - "Sunrise over water, silhouette of person raising arms" stock shots.
  - Roadmap / goal-chart illustrations.
  - Fake-diploma close-ups.
- **Detection**: curator reads the §13 list before discovery; reviewer verifies pack absence.
- **Fix**: re-source with warm-earth studio/dialogue imagery (CS-IMG-COH-02).
- **Reference**: AP9.

### CS-IMG-AP-07 [REQUIRED] · Excessive HDR / teal-and-orange cinematic grading

- **Failure**: candle-lit scenes regraded to teal shadows / orange highlights; HDR clip with haloed outlines.
- **Detection**: visual review during curator phase.
- **Fix**: choose a naturally-lit frame instead.
- **Reference**: CS-IMG-PREM-03.

### CS-IMG-AP-08 [REQUIRED] · Visible brand logos in imagery

- **Failure**: glowing Apple logos, Nespresso cup, branded notebook.
- **Detection**: URL-by-URL semantic read.
- **Fix**: re-source unbranded equivalent.
- **Reference**: CS-IMG-COH-04.

### CS-IMG-AP-09 [REQUIRED] · Mono-demographic leadership lineup

- **Failure**: three white-male-55 portraits as the full leadership set with no rationale.
- **Detection**: pack review, section-rendering review.
- **Fix**: diversify portrait sourcing.
- **Reference**: CS-IMG-COH-05.

### CS-IMG-AP-10 [REQUIRED] · Hero face staring at camera

- **Failure**: hero slot 0 is a direct-gaze corporate headshot.
- **Detection**: visual review.
- **Fix**: re-source mid-action or profile/three-quarter framing.
- **Reference**: CS-IMG-HERO-05.

### CS-IMG-AP-11 [REQUIRED] · 15-people "pointing at whiteboard" stock tropes

- **Failure**: the named Session-31 "multi-ethnic team pointing at whiteboard" cliché.
- **Detection**: CS-IMG-PRO-05 test.
- **Fix**: substitute individual portraits or small-group working shots.

### CS-IMG-AP-12 [REQUIRED] · Decorative photos inside typographic sections

- **Failure**: a 4-up photo grid behind the pillars; photographic wallpaper on the KPI band; ambient photo under the CTA copy.
- **Detection**: CS-IMG-RHYTHM-01 walk.
- **Fix**: remove the decorative photos; keep the section typographic.

### CS-IMG-AP-13 [REQUIRED] · Pack missing captions, roles, or coherence statements

- **Failure**: pack file exists but URLs lack the 3-line metadata (caption / role / coherence).
- **Detection**: pack file scan at reviewer sign-off.
- **Fix**: curator fills the missing lines. Without them, the URL is unverifiable and must be dropped.
- **Reference**: CS-IMG-COH-06, CURATION_PROTOCOL §3.3.

---

## 13 · Avoiding the generic stock look

Stock-look is the #1 silent failure mode on this archetype. The imagery may pass every other rule and still feel cheap if it reads as stock-plate. This section is the diagnostic checklist.

### CS-IMG-STOCK-01 [BLOCKING] · The 10-cluster interchangeability test

- **Rule**: an image that could plausibly serve 10+ unrelated clusters without changing meaning is a generic stock fallback. Reject.
- **Examples that fail the test**: handshake over a conference table; smiling woman at laptop; person with coffee in one hand and phone in the other; multi-ethnic team looking at a whiteboard.
- **Examples that pass the test**: ODCEC-stamped folder on a desk next to a magnifying glass; Cassazionista's open Codice Civile next to a fountain pen; coach's notebook on a low wooden table with two mugs.
- **Reference**: `imagery/blacklist.md` §2.

### CS-IMG-STOCK-02 [REQUIRED] · Specificity test

- **Rule**: you should be able to describe the image in one sentence that NAMES a specific subject/object visible in the frame. "Professional at desk" is too vague — rejects. "Glasses-wearing professional reviewing a printed SPA balance sheet" is specific — passes.

### CS-IMG-STOCK-03 [REQUIRED] · No forced-smile faces in professional imagery

- **Rule**: faces in professional/corporate slots show natural engagement — focused, mid-conversation, or in profile. Forced smiles plate the image as stock.
- **Exception**: coaching portrait slot 2 may carry a warm natural smile if the subject is mid-conversation, NOT teeth-baring headshot grin.

### CS-IMG-STOCK-04 [REQUIRED] · Lighting test — window vs studio

- **Rule**: prefer natural-window light or considered-practical-light. Studio-flat even-fill lighting is the lighting of stock. Images with visible window light, ambient practicals, or single-key-side-light read as editorial.

### CS-IMG-STOCK-05 [REQUIRED] · Provenance test

- **Rule**: the curator writes the photographer's name in the pack (CS-IMG-SRC-03). If the photographer has a body of work that reads as a real editorial photographer (named shoots, a style), the chance of stock-plate decreases. If the photographer's Pexels profile is 2000+ uploads of interchangeable corporate-lifestyle shots, be suspicious — they are a volume stock producer. Prefer named editorial photographers.

### CS-IMG-STOCK-06 [GUIDELINE] · Pool-level coherence test

- **Rule**: stand back from the pack file thumbnails of all 6 pool URLs — do they feel like one cohesive editorial set, or like six random stock buys from different shoots? Coherent pools read premium; mixed pools read stock even when each individual URL is fine.

---

## 14 · When imagery is blocking vs non-blocking

This section resolves the tension between "ship the pilot" and "polish the pilot." Not every imagery rule is a ship-gate; some are sign-off polish.

### CS-IMG-BLOCK-01 [BLOCKING] categories (any one failure prevents `published_live`)

1. **Source is not Pexels** on a new template (CS-IMG-SRC-01). Only exception: Pragma legacy Unsplash (AP3 · retro-curation tracked).
2. **Category mismatch** — subject not recognizable as the profession (CS-IMG-COH-01, CS-IMG-AP-02).
3. **Generic stock fallback** — fails the 10-cluster interchangeability test (CS-IMG-STOCK-01, CS-IMG-AP-03).
4. **Cross-cluster URL reuse** (CS-IMG-SRC-04, CS-IMG-AP-04).
5. **Placeholder imagery in live render** — grey silhouette, initial avatar, upload-icon (CS-IMG-AP-05).
6. **Hero photo below 1600×900** or missing crop safety (CS-IMG-HERO-03, CS-IMG-HERO-04).
7. **Palette polarity violation via imagery** — photo forces dark-on-dark or light-on-light against the skin (CS-IMG-COLOR-02, CS-IMG-SEC-10). Note: this ties back to CS-PAL-01 / CS-PAL-04 in the design standard.
8. **KPI band carries photography** (CS-IMG-SEC-02) — breaks institutional cadence.
9. **Pool shape violated** — fewer or more than 6 URLs, or wrong slot order (CS-IMG-POOL-01).
10. **Pool shipped without a reviewer-approved pack file** (CS-IMG-SRC-05, CURATION_PROTOCOL §6).
11. **Browser walk reveals a category mismatch or stock cliché** that the pack review missed (CS-IMG-BROWSER-01).
12. **Leadership section renders avatar placeholders** instead of real portraits (CS-IMG-SEC-03).

### CS-IMG-BLOCK-02 [REQUIRED] categories (must fix before reviewer walk sign-off · but merge can land with an open TODO)

- Captions/roles/coherence statements incomplete in the pack (CS-IMG-COH-06).
- Portrait set is mono-demographic without explicit rationale (CS-IMG-COH-05).
- Hero subject staring at camera (CS-IMG-HERO-05).
- Visible brand logos or product placement (CS-IMG-COH-04, CS-IMG-AP-08).
- Photo grain/color consistency fails across the 6-URL pool (CS-IMG-COLOR-06, CS-IMG-STOCK-06).
- Section imagery density drift (CS-IMG-RHYTHM-01 violations that don't land on typographic sections).
- Card-grid crops degrade below portrait integrity (CS-IMG-CROP-02, CS-IMG-CROP-05).
- Case-card reuses the hero photo (CS-IMG-SEC-05).

### CS-IMG-BLOCK-03 [STRONG / GUIDELINE] categories (polish; document the deviation)

- Photographic grain coherence across the pool is imperfect but defensible (CS-IMG-COLOR-06).
- Logo marquee drift (E3 · 110s vs shared default · not imagery-specific but related).
- Decorative ambient photo on contact page beyond one (CS-IMG-SEC-09).

### CS-IMG-BLOCK-04 · Decision recipe for reviewer

On reviewer sign-off, walk the pack + the live render and answer:

1. **Is every URL on Pexels?** (BLOCKING; Pragma-legacy exception tracked separately.)
2. **Does every URL pass the 3-second semantic read?** (BLOCKING.)
3. **Does the pool + the live render avoid all [BLOCKING] categories above?** (If not, the pack fails — no flip to LIVE.)
4. **Are [REQUIRED] items closed or tracked with open TODOs?** (If not, draft sign-off only.)
5. **Is the rhythm across sections correct (CS-IMG-RHYTHM-01)?** (If not, flag for rework.)

If all four clear, the pack is approved and the template may flip to `published_live`.

---

## 15 · Browser live verification — imagery acceptance gate

### CS-IMG-BROWSER-01 [BLOCKING] · No pilot flips to `published_live` without an imagery-focused live browser walk

- **Rule**: CLI green + pack approved is NECESSARY but NOT SUFFICIENT. The imagery-focused reviewer walk is the ship gate for imagery.
- **Walk scope** per pilot (nested inside the full CS-BROWSER-01 walk):
  1. Load the live URL across all 5 locales (IT / EN / FR / ES / AR).
  2. Load at 1920 / 1440 / 1280 / 1024 / 768 / 390 viewports.
  3. For each page, confirm:
     - Every photographic surface listed in CS-IMG-POOL-02 is rendered (no broken images, no placeholder icons).
     - Hero photo passes the 3-second cluster-recognizability test (CS-IMG-HERO-02).
     - Hero left-edge is calm next to h1 (CS-IMG-COLOR-01).
     - Credit overlay is legible at AA contrast (CS-IMG-COLOR-02).
     - Portrait slots render as real portraits, not placeholders (CS-IMG-SEC-03).
     - Case-card grid does not reuse the hero (CS-IMG-SEC-05).
     - KPI band has no photography (CS-IMG-SEC-02).
     - Pillars/services cards are icon-typographic, not photo-led (CS-IMG-SEC-01).
     - 10-cluster interchangeability test on all 6 pool slots (CS-IMG-STOCK-01).
     - Dark-section photo overlays hit AA text contrast (CS-IMG-COLOR-05).
  4. Viewport crop survival: hero crop at 4:3 (desktop) AND 16:9 (mobile stacked) (CS-IMG-CROP-01).
- **Artifact**: screenshots saved under `factory/reports/browser-verification/{template-slug}/imagery/` per locale × viewport.
- **Cross-reference**: `corporate-suite-browser-rubric.md` is the exact walk script.

### CS-IMG-BROWSER-02 [BLOCKING] · Dev server URL + port recorded in the walk log

- **Rule**: same as CS-BROWSER-02 — no phantom walks. The walk log includes `http://127.0.0.1:{port}/` and the timestamp.

### CS-IMG-BROWSER-03 [REQUIRED] · Imagery-walk failures block the imagery sign-off even if the full walk is otherwise clean

- **Rule**: an imagery-specific failure is a LIVE-flip blocker even if responsive, contrast, and copy walks are clean.

---

## 16 · DO / DON'T summary (quick reference for agents)

### DO

- Source every URL from Pexels (`images.pexels.com`).
- Record photographer + pexels-id + resolution in the pack file.
- Review every URL with the 3-second semantic read.
- Produce the pack (`imagery/packs/<cluster>.md`) BEFORE copy authoring starts.
- Maintain the 6-slot pool shape `[hero, feature, portrait, portrait, detail, ambient]` in that order.
- Match imagery palette to the template palette (cool/neutral/warm pairing).
- Keep hero image calm on the left edge next to h1.
- Use working-posture portraits (mid-consultation, mid-review) with natural engagement.
- Ship working-artifact details (SPA folder, codici, notebooks) that name the profession.
- Run the Playwright imagery walk at 1920 / 1280 / 768 / 390 across all 5 locales.
- Vary people portraits (age / gender / ethnicity) where plausible for Italian market.
- Use credit overlays on hero photos to anchor editorial feel.
- Keep case cards pulled from slots 4-5, rotated — never reuse slot 0.
- Dim/scrim photos under light text in dark sections until AA is met.

### DON'T

- Don't use Unsplash, Shutterstock, Getty, Adobe Stock, AI-generated, or raw-web URLs on new templates (CS-IMG-SRC-01, CS-IMG-AP-01).
- Don't ship a pool without a reviewer-approved pack file (CS-IMG-SRC-05, CS-IMG-AP-13).
- Don't reuse the same URL across two clusters (CS-IMG-SRC-04, CS-IMG-AP-04).
- Don't pick a hero image that stares at the camera (CS-IMG-HERO-05, CS-IMG-AP-10).
- Don't pick a hero image that fails the 4:3 ↔ 16:9 crop swap (CS-IMG-CROP-01, CS-IMG-HERO-04).
- Don't place photography on the KPI band (CS-IMG-SEC-02).
- Don't place 3-4 small photos inside pillar cards (CS-IMG-SEC-01, CS-IMG-AP-12).
- Don't use avatar/silhouette/initial-circle placeholders in the live render (CS-IMG-AP-05, CS-IMG-SEC-03).
- Don't ship category-mismatched imagery (CS-IMG-COH-01, CS-IMG-AP-02).
- Don't ship generic-stock-fallback imagery (CS-IMG-STOCK-01, CS-IMG-AP-03).
- Don't ship coaching clichés on `business-coaching` (CS-IMG-AP-06).
- Don't show visible brand logos in imagery (CS-IMG-COH-04, CS-IMG-AP-08).
- Don't ship mono-demographic leadership portraits without rationale (CS-IMG-COH-05, CS-IMG-AP-09).
- Don't use HDR / teal-and-orange cinematic grading (CS-IMG-PREM-03, CS-IMG-AP-07).
- Don't use animated/parallax/video hero backgrounds (CS-IMG-DYN-04).
- Don't flip to `published_live` without a dedicated imagery browser walk (CS-IMG-BROWSER-01).

---

## 17 · Examples — acceptable vs unacceptable

### Acceptable image characteristics

| Slot | Example (from repo-confirmed Fiscus pack) | Why it works |
|---|---|---|
| hero | `pexels-photo-8927688` — tidy workspace, laptop, documents, eyeglasses, warm window light, hands visible, no face-to-camera | Editorial, specific subject (professional at work), natural light, negative space, cluster-recognizable within 3 seconds |
| feature | `pexels-photo-36175676` — contemporary office interior, sleek desk | Institutional setting, calm palette, depth, compatible with Fiscus warm-neutral grade |
| portrait | `pexels-photo-7845284` — professional man, eyeglasses, office | Working posture, natural engagement, square-safe framing |
| portrait | `pexels-photo-30614308` — professional woman, modern office setting | Diversity (gender), cluster-appropriate dress code, specific setting |
| detail | `pexels-photo-7821914` — tax documents with calculator on wooden table | Cluster-specific artifacts (fiscal documents), warm-wood grade matches Fiscus palette |
| ambient | `pexels-photo-159832` — law/regulation bookshelf | Institutional reassurance, cluster-adjacent, premium texture |

### Unacceptable image characteristics (Session 31 + blacklist incidents)

| Failure | Why it fails | Category |
|---|---|---|
| PlayStation gamepad labelled "map of Rome" | Category mismatch — not a map, not real estate | CS-IMG-AP-02 |
| Bumble Bee tuna can labelled "artisan ingredients" | Category mismatch — consumer product, not artisan | CS-IMG-AP-02 |
| "Smiling businesswoman shaking hands in vague office" | 10-cluster interchangeability fail | CS-IMG-AP-03 |
| "Multi-ethnic team pointing at a whiteboard" | Named stock trope, zero specificity | CS-IMG-AP-03 / CS-IMG-AP-11 |
| Mountain peak at sunrise (on a coaching template) | Coaching cliché (AP9) | CS-IMG-AP-06 |
| Hairstylists' portraits as "before/after dermatology" | Category mismatch | CS-IMG-AP-02 |
| Diamond ring as "oysterman's portrait" | Category mismatch | CS-IMG-AP-02 |
| URL from `restaurant-fine` reused in `portfolio-photographer` | Cross-cluster reuse (AP6) | CS-IMG-AP-04 |
| Hero face directly at camera, teeth-bared smile | Stock-plate headshot | CS-IMG-AP-10 |
| 15 people pointing at whiteboard in a leadership slot | Stock trope, zero specificity | CS-IMG-AP-11 |
| Glowing Apple logo on laptop in a detail slot | Visible brand logo | CS-IMG-AP-08 |
| Candle-lit restaurant shot regraded to teal-and-orange cinematic | Over-grading, not editorial | CS-IMG-AP-07 |
| Grey silhouette person icon in leadership grid on live render | Placeholder leak | CS-IMG-AP-05 |
| 4-up photo grid behind pillars section | Decorative photo on typographic section | CS-IMG-AP-12 |
| Hero image at 800×450 (Pexels `w=800`) | Below resolution floor | CS-IMG-HERO-03 |

---

## 18 · Rule index (fast lookup)

| Tag | One-line rule |
|---|---|
| CS-IMG-SRC-01 | Pexels-only for new templates (only Pragma legacy Unsplash exception) |
| CS-IMG-SRC-02 | Pexels URL format with `auto=compress&cs=tinysrgb&w=<budget>` |
| CS-IMG-SRC-03 | Pack records photographer + pexels-id + resolution |
| CS-IMG-SRC-04 | One URL = one cluster, zero cross-cluster reuse |
| CS-IMG-SRC-05 | Curator ≠ reviewer on the pack |
| CS-IMG-POOL-01 | Pool shape `[hero, feature, portrait, portrait, detail, ambient]` |
| CS-IMG-POOL-02 | Minimum image distribution across the 7 skin files |
| CS-IMG-POOL-03 | Pool key prefix is `business-` |
| CS-IMG-POOL-04 | Pack carries 20-40 candidates; pool selects 6 |
| CS-IMG-COH-01 | Subject matches the profession (3-second read) |
| CS-IMG-COH-02 | Mood matches the voice anchor |
| CS-IMG-COH-03 | Cluster-specific terminology matches imagery |
| CS-IMG-COH-04 | No visible brand logos / product placement |
| CS-IMG-COH-05 | Diverse portrait representation where plausible |
| CS-IMG-COH-06 | Per-URL caption + role + coherence statement |
| CS-IMG-COH-07 | Imagery underlines the voice anchor, never contradicts |
| CS-IMG-PREM-01 | Editorial, not stock-plate |
| CS-IMG-PREM-02 | Resolution floors (hero 1600×900, portrait 800×800, etc.) |
| CS-IMG-PREM-03 | Institutional grading, not HDR/teal-orange |
| CS-IMG-PREM-04 | Depth and negative space |
| CS-IMG-PREM-05 | Specificity reads premium |
| CS-IMG-DYN-01 | Hero/feature imply motion or mid-action |
| CS-IMG-DYN-02 | Portraits in working posture, not stock-pose |
| CS-IMG-DYN-03 | Detail/ambient carry environmental motion cues |
| CS-IMG-DYN-04 | No video/parallax/animated hero backgrounds |
| CS-IMG-PRO-01 | Dress code / posture reads as the profession |
| CS-IMG-PRO-02 | Institutional settings, not coworking/café |
| CS-IMG-PRO-03 | Cluster-specific working artifacts |
| CS-IMG-PRO-04 | No consumer-tech / gaming artifacts |
| CS-IMG-PRO-05 | No "multi-ethnic-team-pointing-at-whiteboard" cliché |
| CS-IMG-CROP-01 | Hero survives 4:3 ↔ 16:9 crop swap |
| CS-IMG-CROP-02 | Portraits square-safe framing |
| CS-IMG-CROP-03 | Focal point in central 60% |
| CS-IMG-CROP-04 | No horizon-bisecting-head |
| CS-IMG-CROP-05 | Card-grid survives 4:3 and 3:2 crop |
| CS-IMG-CROP-06 | Preview tile is hero-led |
| CS-IMG-COLOR-01 | Hero left-edge calm next to h1 |
| CS-IMG-COLOR-02 | Credit overlay AA-legible on photo |
| CS-IMG-COLOR-03 | Imagery palette compatible with template palette |
| CS-IMG-COLOR-04 | No brand-hostile dominant hues |
| CS-IMG-COLOR-05 | Dark-section photo overlays meet AA text contrast |
| CS-IMG-COLOR-06 | Pool-level photographic consistency |
| CS-IMG-HERO-01 | Hero from curated pack slot 0 |
| CS-IMG-HERO-02 | Hero editorial, cluster-recognizable in 3 seconds |
| CS-IMG-HERO-03 | Hero ≥ 1600×900 rendered |
| CS-IMG-HERO-04 | Hero survives crop swap |
| CS-IMG-HERO-05 | No face-staring-at-camera hero |
| CS-IMG-HERO-06 | Hero left-edge calm |
| CS-IMG-HERO-07 | Hero carries implied motion |
| CS-IMG-HERO-08 | Credit overlay present on hero |
| CS-IMG-SEC-01 | Pillars icon-led, not photo-led |
| CS-IMG-SEC-02 | KPI band is typographic, zero photography |
| CS-IMG-SEC-03 | Leadership uses real portraits, no placeholders |
| CS-IMG-SEC-04 | Sectors ribbon + association marquee |
| CS-IMG-SEC-05 | Case cards use slots 4-5, not hero |
| CS-IMG-SEC-06 | About: feature photo OR photo-less timeline |
| CS-IMG-SEC-07 | Services: ≤ 1 feature photo |
| CS-IMG-SEC-08 | Case-study-detail lifts the photo budget |
| CS-IMG-SEC-09 | Contact: ≤ 1 ambient photo |
| CS-IMG-SEC-10 | Dark-section photos scrimmed for AA |
| CS-IMG-RHYTHM-01 | Fixed photographic cadence on home |
| CS-IMG-RHYTHM-02 | No two adjacent photo-heavy sections |
| CS-IMG-RHYTHM-03 | Photo density decreases toward CTA |
| CS-IMG-RHYTHM-04 | Cross-page rhythm: detail + list are dense, rest are light |
| CS-IMG-RHYTHM-05 | Preview tile reads as one editorial sheet, not collage |
| CS-IMG-AP-01 | Reject non-Pexels on new templates |
| CS-IMG-AP-02 | Reject category-mismatched imagery |
| CS-IMG-AP-03 | Reject generic stock fallback |
| CS-IMG-AP-04 | Reject cross-cluster URL reuse |
| CS-IMG-AP-05 | Reject placeholder imagery in live render |
| CS-IMG-AP-06 | Reject coaching clichés |
| CS-IMG-AP-07 | Reject HDR / teal-orange grading |
| CS-IMG-AP-08 | Reject visible brand logos |
| CS-IMG-AP-09 | Reject mono-demographic portrait set |
| CS-IMG-AP-10 | Reject face-staring-camera hero |
| CS-IMG-AP-11 | Reject team-pointing-at-whiteboard tropes |
| CS-IMG-AP-12 | Reject decorative photos on typographic sections |
| CS-IMG-AP-13 | Reject packs missing captions/roles/coherence |
| CS-IMG-STOCK-01 | 10-cluster interchangeability test |
| CS-IMG-STOCK-02 | Specificity test |
| CS-IMG-STOCK-03 | No forced-smile faces in professional imagery |
| CS-IMG-STOCK-04 | Natural/considered light over flat studio light |
| CS-IMG-STOCK-05 | Prefer named editorial photographers |
| CS-IMG-STOCK-06 | Pool reads as one editorial set |
| CS-IMG-BLOCK-01 | 12 blocking categories (ship-gate) |
| CS-IMG-BLOCK-02 | Required categories (sign-off gate) |
| CS-IMG-BLOCK-03 | Strong/guideline polish items |
| CS-IMG-BLOCK-04 | 5-step reviewer decision recipe |
| CS-IMG-BROWSER-01 | Imagery-focused browser walk is the ship gate |
| CS-IMG-BROWSER-02 | Dev server URL + port recorded |
| CS-IMG-BROWSER-03 | Imagery-walk failure blocks sign-off |

---

## 19 · Summary

### Imagery selection model (five steps · in order)

1. **Read the upstream blueprint + blacklist** — `cluster_blueprints/<cluster>.md` (§3 positioning, §5 voice anchor, §8 imagery direction, §13 anti-patterns) plus `imagery/blacklist.md`. The blueprint's §13 anti-pattern list is load-bearing — copy it into the pack file header.
2. **Search Pexels with cluster-specific queries** — never generic "business meeting" queries. Collect 60-100 candidates into a scratchpad.
3. **URL-by-URL semantic review** — for each candidate, write a 1-sentence semantic caption (descriptive, not aspirational), the slot role, and a coherence justification. Any URL that cannot carry all three is discarded. This is the 3-second read that caught Session 31 incidents.
4. **Cross-check against all existing packs** — `scripts/check_imagery_pack.py` greps for duplicate URLs. One URL = one cluster.
5. **Reviewer LGTM** — a second reviewer (not the curator) validates the pack against §6 of CURATION_PROTOCOL + the CS-IMG-BLOCK-04 recipe. Only then does the copy author begin.

The pool (`preview_imagery.py` slots 0-5) is a 6-URL subset of the 20-40 pack candidates, slotted in the fixed `[hero, feature, portrait, portrait, detail, ambient]` order. The extras remain in the pack for case-study-detail pages and for future URL replacement when a candidate 404s.

### Main failure patterns to avoid

1. **Category mismatch** — URLs trusted without a 3-second semantic read. Session 31 incidents (PlayStation gamepad, tuna can, diamond ring, hairstylists-as-dermatology) all shipped because the author was not the curator. Rule: URL-by-URL semantic captions, reviewer ≠ curator (CS-IMG-COH-01, CS-IMG-AP-02).
2. **Generic stock fallback** — "smiling businesswoman shaking hands in vague office" and "multi-ethnic team pointing at a whiteboard" fail the 10-cluster interchangeability test. Rule: specificity in subject, artifacts, and setting (CS-IMG-STOCK-01, CS-IMG-AP-03).
3. **Non-Pexels sourcing on new templates** — Unsplash/Shutterstock/Getty/AI-gen all forbidden on new templates. Pragma legacy Unsplash is the only tracked exception, scheduled for retro-curation (CS-IMG-SRC-01, CS-IMG-AP-01, AP3).
4. **Cross-cluster URL reuse** — Session 38 caught `portfolio-photographer` reusing `restaurant-fine` URLs. Rule: one URL = one cluster, grep check at merge time (CS-IMG-SRC-04, CS-IMG-AP-04).
5. **Pool-shape violations** — wrong count, wrong slot order, wrong aspect ratio for the slot. Breaks the preview composition and the section-rendering contract (CS-IMG-POOL-01).
6. **Placeholder leaks** — avatar silhouettes, initial circles, upload-icon placeholders on the live render. Editor-UI affordances must stay behind `body.mw-is-editor-preview` (CS-IMG-AP-05, CS-MARKET-01).
7. **Rhythm drift** — decorative photos on typographic sections (pillars, KPI, CTA) collapse the institutional cadence into a gallery (CS-IMG-RHYTHM-01, CS-IMG-AP-12).
8. **Palette fights** — imagery that clashes with the template palette or forces dark-on-dark / light-on-light. Cross-wires with CS-PAL-01 / CS-PAL-04 / AP1 (CS-IMG-COLOR-03, CS-IMG-COLOR-05).
9. **Stock-plate heroes** — face-staring-camera hero shots, teeth-bared smiles, flat studio light. Collapse the editorial register on the most important frame (CS-IMG-HERO-05, CS-IMG-AP-10).
10. **Pack metadata missing** — URL lists without captions/roles/coherence fail audit and break re-sourcing (CS-IMG-COH-06, CS-IMG-AP-13).

### Most important blocking conditions

A pilot on this archetype cannot flip to `published_live` if ANY of the following is true:

1. **The pool contains a non-Pexels URL** on a new template (only Pragma legacy is tolerated, tracked).
2. **Any URL fails the 3-second semantic read** (category mismatch).
3. **Any URL fails the 10-cluster interchangeability test** (generic stock fallback).
4. **A URL appears in two clusters**.
5. **The pool does not follow the 6-slot shape `[hero, feature, portrait, portrait, detail, ambient]`**.
6. **The hero photo is below 1600×900, has a direct-camera gaze, or fails the 4:3 ↔ 16:9 crop swap**.
7. **The KPI band carries photography** or the pillars section is photo-led.
8. **Leadership renders with placeholder avatars** instead of real portraits.
9. **A dark-section text-over-photo composite fails WCAG AA**.
10. **The pack file is not reviewer-approved** per CURATION_PROTOCOL §6.
11. **The imagery-focused browser walk at 1920 / 1280 / 768 / 390 × 5 locales surfaces any of the above**.

Until the skin hardening pass closes AP2 (responsive coverage) and the `business-corporate` Pexels retro-pack closes AP3, this imagery standard is the authoritative reference for every agent sourcing, validating, or reviewing imagery on a corporate-suite template, and the `[BLOCKING]` rules here define the floor for merge and LIVE flip.
