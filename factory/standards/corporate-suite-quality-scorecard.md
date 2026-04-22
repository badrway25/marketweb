# Corporate-suite Quality Scorecard

**Phase**: X.4a · Corporate-suite Factory Hardening · **Date**: 2026-04-22
**Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Scope**: factory files only · no `apps/editor`, `apps/projects`, `apps/commerce` changes · no new archetypes · Solaria Commit B remains paused.
**Inputs**: `factory/reports/audits/corporate-suite-audit-master.md`, `factory/standards/corporate-suite-design-standard.md`, `factory/standards/corporate-suite-imagery-standard.md`, `factory/standards/corporate-suite-browser-rubric.md`.
**Audience**: every agent that signs off on a corporate-suite template before `TEMPLATE_REGISTRY.json` flips from `draft` to `published_live` — release-gatekeeper primarily, plus the upstream agents (style-critic, contrast-accessibility-auditor, responsive-auditor, imagery-curator-reviewer, browser-verifier) whose outputs feed this scorecard.

This file is the numeric ship gate. The design standard says **what** premium means, the imagery standard says **what** imagery qualifies, the browser rubric says **how** to verify the render. This scorecard is the **decision artifact** that collapses all three into a single PASS / BORDERLINE / FAIL verdict with a defensible numeric trail.

---

## 0 · How to use this document

1. The scorecard has **15 scoring dimensions** (§3), each graded on a **0–5 scale** (§1).
2. The verdict is computed by three layers in order — **any single layer can reject**:
   - **Layer 1 · Blocking overrides** (§4) — any triggered override = automatic FAIL regardless of scores.
   - **Layer 2 · Critical-dimension floors** (§5) — specific dimensions must clear a minimum bar or the verdict cannot be PASS, even if the average is high.
   - **Layer 3 · Aggregate thresholds** (§6) — overall and per-dimension thresholds separate PASS / BORDERLINE / FAIL.
3. **Scores are evidence-backed, not vibes.** Every dimension score cites the rubric checks (BRWS-*), standard rules (CS-*), and evidence artifacts (screenshots, measurements, walk-log entries) that produced it. A score with no citation is rejected on review.
4. **Fill this scorecard after the browser walk completes**, once the rubric's `verdict.md` and evidence directory exist. This scorecard IS the ship artifact; it lives alongside the rubric verdict.
5. Pair this document with:
   - `corporate-suite-design-standard.md` · rule source for dimensions 1–8, 10.
   - `corporate-suite-imagery-standard.md` · rule source for dimensions 9–11, 15.
   - `corporate-suite-browser-rubric.md` · evidence source for every dimension; the verdict here cannot exist without a completed rubric walk.
   - `corporate-suite-blocking-rules.md` (to be populated) · enforcement recipes for the Layer 1 overrides.
6. **One scorecard per walk.** A template flipped LIVE after two walks gets two scorecards, one per walk. Never edit a completed scorecard in place — superseded scorecards stay in their `<run-timestamp>` directory as part of the audit trail.

---

## 1 · Scoring scale · 0 to 5

The scale is deliberately narrow. Six grades are enough to separate ship-ready from borderline from broken, and narrow enough that two reviewers agree. Half-scores are not allowed — round down if torn.

| Score | Label | Operational meaning |
|:-:|---|---|
| **5** | Exemplary | Reference-class. This dimension would be a positive example in `pattern-library.md`. Zero `[BLOCKING]`, zero `[REQUIRED]`, zero `[STRONG]` failures in this dimension. Rubric measurements clear the design-standard targets with margin (e.g., contrast AAA ≥ 7.0, not just AA ≥ 4.5). Feature for future pilots to copy. |
| **4** | Ship-quality | Meets the bar for `published_live`. Zero `[BLOCKING]`, zero `[REQUIRED]`, at most one `[STRONG]` failure in this dimension, and that failure has a written `§ deviation` justification. Rubric measurements clear the design-standard targets. **This is the default target for every dimension on a passing template.** |
| **3** | Ship-soft · borderline | No `[BLOCKING]` failures in this dimension, but one or more `[REQUIRED]` failures OR multiple `[STRONG]` failures. Render is acceptable but erodes archetype quality if normalized. A PASS verdict requires dimension ≥ 4, so a score of 3 cannot produce PASS — it produces BORDERLINE or FAIL depending on §5 floors and §6 aggregate logic. |
| **2** | Weak | Multiple `[REQUIRED]` failures OR a `[BLOCKING]` failure that was partially remediated but still visible (e.g., hero contrast AA-passing at 4.6 but AAA target 7.0 missed). Render is noticeably off-standard. Cannot pass. |
| **1** | Fail | At least one unremediated `[BLOCKING]` failure in this dimension, even if other aspects of the dimension are fine. Example: hero h1 contrast AA-failing at 3.8 on paper (CS-HERO-03 violated) regardless of how lovely the typography is. |
| **0** | Absent · Broken | The dimension cannot be evaluated at all — evidence missing, walk not performed, render broken to the point of occluding the test (e.g., horizontal scrollbar at every viewport so layout cannot be judged; imagery URLs all 404; editor affordances pasted across every page). Automatic blocking override (§4). |

### 1.1 · Scoring discipline

- A score of 4 or 5 requires **positive evidence**, not merely absence of failure. "I didn't see a problem" ≠ 4. The scorer must cite the specific rubric measurement (contrast ratio, scrollWidth, computed style) or rule (CS-*) that the dimension satisfies.
- A score of 3 or below requires **a named failure** with its rubric tag, incident anchor, and evidence artifact. Vague "feels a bit cluttered" scoring is rejected.
- When the rubric's §6 check produces multiple measurements that map to a single scorecard dimension, the dimension score is bounded by the **worst** measurement. No averaging measurements up.
- If a reviewer cannot distinguish between two scores for a dimension, round down. Rounding up hides risk.

---

## 2 · Relationship between rubric severities and scorecard scores

The browser rubric (§6 check roster) already tags each check with `[BLOCKING]` / `[REQUIRED]` / `[STRONG]` / `[GUIDELINE]`. The scorecard rolls those into per-dimension scores as follows:

| Rubric findings within a dimension | Produces score |
|---|:-:|
| Any `[BLOCKING]` failed (unremediated) | **1** or **0** |
| Zero `[BLOCKING]` failed, ≥ 2 `[REQUIRED]` failed | **2** |
| Zero `[BLOCKING]` failed, 1 `[REQUIRED]` failed | **3** |
| Zero `[BLOCKING]` failed, zero `[REQUIRED]` failed, ≥ 2 `[STRONG]` failed (no justification) | **3** |
| Zero `[BLOCKING]` failed, zero `[REQUIRED]` failed, ≤ 1 `[STRONG]` failed with `§ deviation` | **4** |
| Zero failures at any severity AND measurements clear the design-standard targets with margin | **5** |

**Layer 1 blocking overrides (§4) bypass this table** — if a blocking override trips, the verdict is FAIL regardless of how the scores aggregate. The table above is for computing scores within an already-non-blocked walk.

---

## 3 · The 15 scoring dimensions

Each dimension lists its rule anchors (design standard tags, imagery standard tags, rubric tags), the measurement that drives the score, and the 0–5 rubric specific to that dimension. Dimensions are numbered but not weighted equally — dimensions flagged **[CRITICAL]** in §5 have minimum floors that must be met for PASS regardless of other dimensions.

### D1 · Premium feel [CRITICAL]

- **What it measures**: does the rendered site read as ultra-premium / editorial / advisory, rather than stock-plate / template-showcase / SaaS-funnel?
- **Design anchors**: CS-TONE-01, CS-TONE-02, CS-TONE-05, CS-MARKET-01..07, CS-PAL-05 (accent as punctuation), CS-EXEC-04 (no hyperbole), CS-EXEC-07 (no funnel sections).
- **Rubric anchors**: BRWS-FEEL-01, BRWS-FEEL-02, BRWS-FEEL-03, BRWS-FEEL-04, BRWS-NAV-05 (accent density), BRWS-IMG-08 (editorial, not stock-plate).
- **Primary measurement**: "remove the studio name" test — does the page still read as a real firm? Combined with accent-density count per fold (≤ 3) and absence of banned phrases/editor affordances/placeholders.
- **Score rubric**:
  - **5**: reads as a real boutique advisory; editorial imagery; accent used ≤ 2 per fold; zero banned phrases; zero editor affordances; reference-class "premium" rendering.
  - **4**: reads as a real firm; accent used ≤ 3 per fold; no banned phrases; at most one `[STRONG]` drift (e.g., marquee duration off) with justification.
  - **3**: reads as a real firm but with density drift or one `[REQUIRED]` failure (e.g., home has 7 cases instead of 3–6).
  - **2**: reads ambiguously — could be a template showcase or a real firm; accent over-used; stock-plate hero photo.
  - **1**: reads as a template showcase; editor affordances visible OR banned phrases present OR placeholder strings visible.
  - **0**: walk did not evaluate this dimension.

### D2 · Elegance [CRITICAL]

- **What it measures**: restraint. Does the typography, spacing, and emphasis read as restrained/editorial, not shouted/decorative?
- **Design anchors**: CS-TONE-02 (restraint over density), CS-TYPE-02 (italic `<em>` emphasis, not bold/uppercase/color), CS-TYPE-05 (letter-spacing discipline), CS-RHYTHM-05 (section titles), CS-PAL-05 (accent as punctuation), CS-DENSITY-07 (no walls of text).
- **Rubric anchors**: BRWS-HERO-05 (italic `<em>` on one word), BRWS-RHYTHM-05 (h2 italic `<em>` · no uppercase), BRWS-READ-03 (no paragraph walls), BRWS-NAV-05 (accent ≤ 3 per fold).
- **Primary measurement**: emphasis mechanism audit (every headline uses italic `<em>` at most on one load-bearing word); no uppercase-shouted section titles; `<p>` ≤ ~120 words; letter-spacing 0 on body, 0.22em reserved for labels.
- **Score rubric**:
  - **5**: every headline respects italic-em restraint; zero uppercase titles; every section breathes (`100px 72px` padding intact at desktop); accent-as-punctuation with margin.
  - **4**: italic `<em>` restraint on headlines; no shouted titles; padding intact; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — a single paragraph-wall OR a single uppercase-tracked title OR padding compressed one section.
  - **2**: multiple `[REQUIRED]` drifts — headline emphasis via bold or uppercase; multiple paragraph-walls.
  - **1**: `[BLOCKING]` elegance failure — e.g., section padding crushed below `100px 72px` across home (CS-RHYTHM-01), OR every h2 rendered uppercase.
  - **0**: walk did not evaluate this dimension.

### D3 · Modern professionalism [CRITICAL]

- **What it measures**: the site reads as a contemporary institutional firm — CSS custom properties driving the palette, logical RTL, accessible focus states, reduced-motion honored, voice and credentials verifiable — not a 2015 corporate-clip-art page.
- **Design anchors**: CS-EXEC-01..07 (voice anchor, D-054 triangulation, credentials, first-person-plural, no funnel), CS-TYPE-01 (humanist/transitional serif + sans), D1–D5 (RTL patterns), E1–E2 (accessibility), CS-PAL-03 (three tokens, no hardcoded fourth).
- **Rubric anchors**: BRWS-FEEL-04 (no hyperbole), BRWS-FEEL-05 (voice anchor verbatim), BRWS-FEEL-06 (verifiable credentials), BRWS-FEEL-08 (reduced-motion), BRWS-CONTRAST-04 (focus-visible gold), BRWS-READ-04 (locale tracking behavior).
- **Primary measurement**: voice-anchor verbatim across 5 locales; cluster-specific credentials; first-person-plural firm voice; `:focus-visible` gold outline; `prefers-reduced-motion` honored; D-054 triangulated in module docstring.
- **Score rubric**:
  - **5**: voice anchor preserved verbatim across 5 locales; all credentials cluster-verifiable (ODCEC/Cassazionista/ICF PCC/CONSOB); `:focus-visible` gold outline on every interactive element; reduced-motion fully honored; D-054 10-gate triangulated; zero hardcoded fourth color.
  - **4**: voice anchor faithful; credentials verifiable; focus + reduced-motion working; D-054 present; one `[STRONG]` drift (e.g., `--primary-2` hardcoded · AP7).
  - **3**: one `[REQUIRED]` drift — e.g., one credential ambiguous (not fake, just generic) OR reduced-motion JS path unverified (AP12).
  - **2**: multiple `[REQUIRED]` drifts — voice drifting in one locale; credentials generic; focus ring partly browser-default.
  - **1**: `[BLOCKING]` failure — fake certification ("Certified Life Transformation Expert"), OR voice anchor paraphrased in one locale, OR D-054 10-gate absent from docstring.
  - **0**: walk did not evaluate this dimension.

### D4 · Hero readability [CRITICAL]

- **What it measures**: does the hero h1 read cleanly and confidently against its background at every viewport? Does the hero pass WCAG AA floor with AAA target?
- **Design anchors**: CS-HERO-01 (55/45 split), CS-HERO-03 (AAA target), CS-HERO-05 (subhead ≤ 35 words), CS-HERO-07 (stacks at ≤ 720), CS-RESPONSIVE-03 (h1 ≥ 32px mobile), CS-PAL-01 (dark primary foreground).
- **Rubric anchors**: BRWS-CONTRAST-01 (h1..h5 RGB distance ≥ 120 · AA ≥ 4.5 · AAA target ≥ 7.0), BRWS-READ-01 (h1 readable at every viewport), BRWS-READ-02 (subhead 1–3 lines), BRWS-HERO-01 (split holds), BRWS-VIEW-03 (stacks at ≤ 720), BRWS-VIEW-06 (h1 ≥ 32px at 390).
- **Primary measurement**: hero h1 WCAG contrast ratio vs paper (target AAA ≥ 7.0, floor AA ≥ 4.5), RGB distance ≥ 120, computed font-size at every viewport in the matrix.
- **Score rubric**:
  - **5**: h1 AAA contrast ≥ 7.0 on every locale; 55/45 split holds on desktop, stacks cleanly ≤ 720; h1 ≥ 44px desktop, ≥ 32px mobile; subhead 1–2 lines desktop; zero overlap with hero photo at any viewport.
  - **4**: h1 AA ≥ 4.5 (AAA target not fully met but approaching); split holds; stacks cleanly; h1 meets size floors.
  - **3**: one `[REQUIRED]` drift — h1 at 31px at 390 (just under 32) OR subhead 4 lines at 1280.
  - **2**: multiple `[REQUIRED]` drifts — h1 both slightly low-contrast AND slightly undersized.
  - **1**: `[BLOCKING]` failure — h1 contrast < 4.5 (AA fails), OR hero does not stack at ≤ 720 (CS-HERO-07 · AP2), OR h1 RGB distance < 120 (AP1 class — Solaria pattern).
  - **0**: walk did not evaluate this dimension OR hero unreadable at every viewport.

### D5 · Navbar quality

- **What it measures**: does the nav hold the dark polarity, show 4 distinct link states, collapse correctly on mobile, and carry exactly one accent element (the trailing CTA)?
- **Design anchors**: CS-NAV-01..06, CS-PAL-06 (nav bg = primary), CS-RESPONSIVE-01 (1100 + 720 breakpoints).
- **Rubric anchors**: BRWS-NAV-01 (bg = primary), BRWS-NAV-02 (one accent CTA), BRWS-NAV-03 (lang+dir per switcher link), BRWS-NAV-04 (4 distinct states), BRWS-VIEW-04 (1100 condense, 720 hamburger), BRWS-CONTRAST-03 (nav text AA), BRWS-CONTRAST-04 (focus-visible gold).
- **Primary measurement**: `getComputedStyle(.cs-nav).backgroundColor` matches seeded primary; count of accent elements = 1; keyboard tab-through shows gold outline on every link; nav condenses at ≤ 1100 and collapses to hamburger at ≤ 720.
- **Score rubric**:
  - **5**: bg matches primary exactly; exactly 1 accent CTA (trailing); 4 visually distinct states with gold `:focus-visible`; condenses cleanly at ≤ 1100; hamburger at ≤ 720 with accessible drawer; locale switcher carries lang+dir per link; wordmark stays Latin under RTL.
  - **4**: bg, CTA count, responsive collapse, focus ring all correct; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — active-page indicator uses accent-color text instead of underline/dot, OR locale switcher missing dir on one link.
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — nav bg ≠ primary (polarity broken · AP1 class), OR > 1 accent element in nav, OR nav does not collapse at ≤ 720 (AP2 class), OR focus ring is browser-default blue (E1 regression).
  - **0**: walk did not evaluate this dimension.

### D6 · Footer quality

- **What it measures**: 3-column composition on desktop, polarity matches navbar, legal row present with cluster-appropriate whistleblowing, Latin wordmark and numerics under RTL, stacks at ≤ 720.
- **Design anchors**: CS-FOOT-01..05, CS-PAL-04 (dark-section child text), D2 (Latin wordmark under RTL).
- **Rubric anchors**: BRWS-FOOT-01..06.
- **Primary measurement**: 3 columns desktop; dark bg + `--on-dark*` text; legal row carries canonical 5 links with whistleblowing when required; stacks to 1 column at ≤ 720.
- **Score rubric**:
  - **5**: 3 columns clean; polarity matches navbar; all 5 legal links present with whistleblowing (advisory clusters); RTL wordmark + numerics Latin; stacks cleanly at ≤ 720; no newsletter signup.
  - **4**: composition correct; polarity correct; legal row complete; stacks correctly; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — whistleblowing missing on commercialista/law cluster, OR legal row missing one canonical link, OR footer does not stack at 720 (pending hardening; acceptable pre-hardening but flagged).
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — footer polarity inverted creating dark-on-dark pocket (CS-PAL-04 · AP11), OR no footer rendered.
  - **0**: walk did not evaluate this dimension.

### D7 · Typography hierarchy

- **What it measures**: serif heading + sans body pairing; italic `<em>` as emphasis mechanism; restrained heading scale; tabular numerals on KPIs; Arabic Kufi+Amiri under RTL.
- **Design anchors**: CS-TYPE-01..06.
- **Rubric anchors**: BRWS-HERO-05 (italic `<em>` on hero h1), BRWS-RHYTHM-05 (h2 italic `<em>`, no uppercase), BRWS-READ-04 (locale tracking), BRWS-READ-05 (tabular-nums), BRWS-FOOT-04 (Latin wordmark+numerics RTL).
- **Primary measurement**: heading font family (humanist/transitional serif), body font family (neutral sans), italic `<em>` on headings, `font-variant-numeric: tabular-nums` on `.num`, Kufi+Amiri swap under `html[dir="rtl"]`, heading sizes within `CS-TYPE-04` floors/ceilings.
- **Score rubric**:
  - **5**: humanist/transitional serif on all headings; neutral sans body; italic `<em>` on every headline load-bearing word; tabular-nums on every `.num`; Kufi+Amiri under RTL; Latin wordmark and numerics survive RTL; heading sizes within the restrained scale with margin.
  - **4**: pairings correct; italic `<em>` correct; tabular-nums correct; RTL font swap correct; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — one headline missing italic `<em>` OR one KPI figure without `.num` OR heading scale slightly out of range (e.g., h1 at 76px, ceiling 72).
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — geometric sans on headings (Montserrat/Poppins/Raleway · CS-TYPE-01), OR missing tabular-nums on KPI band (CS-TYPE-03), OR Arabic glyphs rendering as squares (D1 broken · CS-TYPE-06).
  - **0**: walk did not evaluate this dimension.

### D8 · Spacing rhythm

- **What it measures**: section wrapper discipline (`100px 72px` · `max-width: 1400`), home section order fixed, one dark band (KPI) at position 3, no adjacent sections with duplicate function, padding IS the rhythm (no additional margins).
- **Design anchors**: CS-RHYTHM-01..06, CS-TONE-02 (restraint over density), CS-TONE-03 (one dark band per home).
- **Rubric anchors**: BRWS-RHYTHM-01..05.
- **Primary measurement**: computed `padding: 100px 72px`, `max-width: 1400px`, `margin: 0 auto` on every home section; DOM order matches hero · pillars · kpi · sectors · leadership · cases · cta; count of `background: var(--primary)` sections ≤ 2 non-adjacent.
- **Score rubric**:
  - **5**: every section clears `100px 72px` + `max-width: 1400`; home order matches the fixed contract; exactly one dark band (KPI) at position 3; no adjacent sections share functional labels; padding IS the rhythm with zero extra margins.
  - **4**: section wrapper discipline correct; home order correct; ≤ 2 non-adjacent dark bands; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — section padding at `88px 72px` on one section, OR two sections with similar functional labels adjacent.
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — section padding crushed below `100px 72px` on multiple sections (CS-RHYTHM-01), OR home section order wrong (e.g., cases before leadership · CS-RHYTHM-02), OR 3+ dark bands on home (CS-TONE-03).
  - **0**: walk did not evaluate this dimension.

### D9 · Imagery quality

- **What it measures**: editorial (not stock-plate), resolution floors met, color grading institutional, depth/negative space, every URL resolves (no 404s).
- **Imagery anchors**: CS-IMG-PREM-01..04, CS-IMG-POOL-01 (6-slot shape), CS-IMG-SRC-02 (URL format + width budget).
- **Rubric anchors**: BRWS-IMG-01 (no 404s), BRWS-IMG-08 (editorial, not stock-plate), BRWS-HERO-02 (hero from pack + credit overlay), BRWS-HERO-06 (crop survives 4:3 desktop + 16:9 mobile), BRWS-RESP-04 (aspect-ratio lock + object-fit cover).
- **Primary measurement**: 6/6 pool URLs return 200; hero ≥ 1600×900, feature ≥ 1200×800, portraits ≥ 800×800 square; editorial lighting/setting/posture signals present; institutional color grading; aspect-ratio locked on card grids.
- **Score rubric**:
  - **5**: every URL resolves; every slot clears its resolution floor with margin; every image reads editorial (natural light, specific setting, action posture); institutional grading throughout; aspect-ratios locked; hero photo survives desktop + mobile crop cleanly.
  - **4**: all URLs resolve; resolution floors met; at least 5/6 read editorial; institutional grading; one `[STRONG]` drift at most (e.g., one ambient shot slightly punchy).
  - **3**: one `[REQUIRED]` drift — one slot below the resolution floor OR one slot reads stock-plate.
  - **2**: multiple `[REQUIRED]` drifts — two stock-plate shots, OR two resolution shortfalls.
  - **1**: `[BLOCKING]` failure — any URL 404s (CS-IMG-SRC-01 / BRWS-IMG-01), OR hero uses 4-up grid / video background instead of single editorial photo (CS-HERO-01), OR hero resolution below 1600×900 (CS-IMG-PREM-02).
  - **0**: walk did not evaluate this dimension OR no imagery rendered.

### D10 · Imagery coherence [CRITICAL]

- **What it measures**: subject-to-profession match (3-second semantic check), mood-to-voice-anchor match, cluster-specific terminology match, no visible product placement, plausible demographic spread, caption + role + coherence justification recorded per URL.
- **Imagery anchors**: CS-IMG-COH-01..07, CS-IMG-SRC-04 (one URL = one cluster).
- **Rubric anchors**: BRWS-IMG-03 (subject match · 3-second check), BRWS-IMG-04 (mood-to-voice-anchor), BRWS-IMG-05 (no product placement), BRWS-IMG-06 (demographic spread), BRWS-IMG-07 (pack record: caption + role + coherence).
- **Primary measurement**: 3-second semantic read per URL (member-of-this-profession recognition); voice-anchor mood read per URL; credentials-to-imagery cross-check; zero visible brand logos; demographic spread plausible; every URL has 3-field pack record.
- **Score rubric**:
  - **5**: every URL passes the 3-second semantic check cleanly; every URL's mood underlines the voice anchor; zero product placement; demographic spread plausible for the Italian market; pack records complete and descriptive; zero cross-cluster URL reuse.
  - **4**: all URLs pass 3-second check; mood correct; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — one portrait demographic slightly mono OR one pack record missing coherence statement.
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — any URL fails the 3-second subject check (AP4 · Session 31 class: PlayStation gamepad as "map of Rome"), OR imagery mood contradicts voice anchor (AP5 · coaching anchor "not therapy" + therapy couch imagery), OR cross-cluster URL reuse (AP6).
  - **0**: walk did not evaluate this dimension OR no imagery rendered.

### D11 · Pexels-only compliance [CRITICAL]

- **What it measures**: every URL on a new template comes from Pexels; legacy Unsplash tolerated only for Pragma until retro-pack lands; URL format correct; per-URL photographer+id+resolution recorded.
- **Imagery anchors**: CS-IMG-SRC-01..05.
- **Rubric anchors**: BRWS-IMG-02 (hero/feature from curated pack · Pexels for new pilots).
- **Primary measurement**: `grep -E 'unsplash|shutterstock|getty|adobestock'` across `preview_imagery.py` for the template's pool returns zero (new pilots); pack file carries photographer + id + resolution for every URL; `scripts/check_imagery_pack.py` passes.
- **Score rubric**:
  - **5**: every URL from Pexels; every URL in the pack file carries photographer + id + resolution; zero cross-cluster URL reuse; width budget per slot respected (hero `w=1600`, feature `w=1200`, portrait `w=800`, etc.); pack reviewer ≠ curator recorded.
  - **4**: every URL from Pexels; pack records present; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — one pack record missing photographer metadata OR one width budget off.
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — any non-Pexels URL on a NEW pilot (CS-IMG-SRC-01 / AP3). **Pragma's legacy Unsplash pack is the single tolerated exception and is flagged at 3, not 1, until the business-corporate retro-pack lands.**
  - **0**: walk did not evaluate this dimension.

### D12 · Contrast safety [CRITICAL]

- **What it measures**: `--primary` is dark on cream (L* ≤ 40 · RGB distance ≥ 120 · AA ≥ 4.5 floor · AAA ≥ 7.0 target for hero h1); dark-section child text uses `--on-dark*` variants; nav + footer polarity held.
- **Design anchors**: CS-PAL-01 (primary L* ≤ 40), CS-PAL-04 (dark-section child text), CS-HERO-03 (hero AAA target), CS-NAV-01, CS-FOOT-01.
- **Rubric anchors**: BRWS-CONTRAST-01 (h1..h5 distance + contrast), BRWS-CONTRAST-02 (dark-section child), BRWS-CONTRAST-03 (nav text AA), BRWS-NAV-01 (nav bg = primary).
- **Primary measurement**: `getComputedStyle(h).color` vs `getComputedStyle(body).backgroundColor` → RGB distance ≥ 120 AND WCAG ratio ≥ 4.5 (AAA target ≥ 7.0 for hero h1); same check for every text descendant of `.cs-section.dark`, `.cs-kpi-band`, `.cs-nav`, `.cs-foot`.
- **Score rubric**:
  - **5**: hero h1 AAA ≥ 7.0 on every locale; every h1..h5 distance ≥ 120; dark-section child text all `--on-dark*`; nav AA ≥ 4.5 on every state; zero contrast complaints from DevTools accessibility audit.
  - **4**: every h1..h5 AA ≥ 4.5 and distance ≥ 120; dark-section text correct; nav AA; hero h1 approaching AAA target.
  - **3**: one `[REQUIRED]` drift — hero h1 at AA 4.7 (AA-pass, AAA-miss) on one locale.
  - **2**: multiple `[REQUIRED]` drifts — hero AA-pass but nav hover state below AA.
  - **1**: `[BLOCKING]` failure — **any h1..h5 distance < 120 (AP1 class · Solaria `e8f38b5` pattern — cream-on-cream headlines)**, OR hero h1 AA < 4.5 on any locale, OR dark-section child text renders dark-on-dark (AP11 · CS-PAL-04).
  - **0**: walk did not evaluate this dimension.

### D13 · Responsive quality [CRITICAL]

- **What it measures**: breakpoints at 1100 + 720 active on every page; no horizontal scroll at any matrix viewport; hero stacks ≤ 720; nav collapses ≤ 720; contact form stacks ≤ 880; hero h1 ≥ 32px at 390; touch targets ≥ 44×44 on mobile.
- **Design anchors**: CS-RESPONSIVE-01..08, CS-HERO-07, CS-NAV-05, CS-FOOT-05.
- **Rubric anchors**: BRWS-VIEW-01..07, BRWS-RESP-01..07.
- **Primary measurement**: full §5 viewport matrix walked (1920 / 1440 / 1280 / 1024 / 768 / 640 / 414 / 390); `scrollWidth ≤ clientWidth` at every viewport; hero `grid-template-columns: 1fr` at ≤ 720; nav drawer at ≤ 720; contact stacks at ≤ 880; h1 `font-size ≥ 32px` at 390; every CTA + nav link `width ≥ 44 AND height ≥ 44` at 390.
- **Score rubric**:
  - **5**: full matrix walked across every locale × every page; zero horizontal scroll; hero stacks cleanly at ≤ 720; nav hamburger with accessible drawer at ≤ 720; contact stacks at ≤ 880; h1 ≥ 32px (typically ≥ 36) at 390; touch targets ≥ 44×44; RTL tested at desktop + tablet + mobile.
  - **4**: matrix walked; responsive behavior correct; one `[STRONG]` drift (e.g., RTL walked at desktop + mobile but tablet skipped).
  - **3**: one `[REQUIRED]` drift — KPI band does not restack cleanly at 390 OR one touch target at 42×42.
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — horizontal scrollbar at any matrix viewport (AP2 class · CS-RESPONSIVE-02), OR hero does not stack at ≤ 720 (CS-HERO-07), OR nav does not collapse at ≤ 720 (CS-NAV-05), OR h1 < 32px at 390 (CS-RESPONSIVE-03).
  - **0**: matrix not walked — automatic blocking override (§4).

### D14 · Browser live verification quality [CRITICAL]

- **What it measures**: the walk itself — was it real, complete, captured with dense evidence, and reproducible by a second reviewer opening the server URL?
- **Design anchors**: CS-BROWSER-01..03.
- **Rubric anchors**: BRWS-TOOL-01..03, BRWS-SRV-01..05, BRWS-VIEW-01, BRWS-EVID-01..06.
- **Primary measurement**: Playwright MCP (or fully-justified manual) walk performed; server URL + port recorded; 5 locales × 6 pages × 4 core viewports = 120 screenshots minimum captured; `measurements.json` keyed by `[BLOCKING]` tag; `walk-log.md` chronological with every MCP call; server still running at verdict time for user parallel verification; zero in-place edits to the evidence directory post-verdict.
- **Score rubric**:
  - **5**: Playwright MCP walk; URL + port recorded; full matrix × 5 locales × 6 pages = 200+ screenshots; every `[BLOCKING]` check measured; console.log clean; server still running; verdict template filled completely; reference-class evidence trail.
  - **4**: walk recorded; evidence directory complete per §7 floor (120+ screenshots); every `[BLOCKING]` measured; verdict template complete; server still running.
  - **3**: one `[REQUIRED]` drift — evidence slightly below the 120-screenshot floor on a non-core viewport OR console.log capture partial.
  - **2**: multiple `[REQUIRED]` drifts — screenshot floor missed AND measurements.json partial.
  - **1**: `[BLOCKING]` failure — server URL + port missing from verdict (BRWS-SRV-02), OR no screenshots captured, OR walk reports "it looked fine" without measurement evidence.
  - **0**: no walk performed — automatic blocking override (§4). A template without a recorded walk cannot be scored.

### D15 · Text/image coherence

- **What it measures**: does the copy match what the imagery shows? Does a credential named in the copy appear in the imagery world? Do hero text and hero image pull in the same direction?
- **Design anchors**: CS-EXEC-01 (voice anchor verbatim), CS-EXEC-03 (verifiable credentials), CS-MARKET-07 (studio name coherent with all copy).
- **Imagery anchors**: CS-IMG-COH-01 (subject match profession), CS-IMG-COH-02 (mood match voice anchor), CS-IMG-COH-03 (cluster terminology match), CS-IMG-COH-07 (imagery underlines anchor, never contradicts).
- **Rubric anchors**: BRWS-IMG-03 + BRWS-IMG-04 + BRWS-FEEL-05 + BRWS-FEEL-06 + BRWS-ALIGN-01 (hero text/image don't overlap).
- **Primary measurement**: voice anchor line verbatim per locale; credentials list cross-checked against portrait set; hero text block doesn't overlap hero photo; image captions stay inside the image frame; section-by-section copy matches the imagery semantic for that slot.
- **Score rubric**:
  - **5**: voice anchor verbatim on 5/5 locales; credentials-to-imagery cross-check passes cleanly (legal copy → legal-world portraits, coaching copy → studio/dialogue portraits); every image caption stays within its frame; hero text/image align cleanly at every desktop viewport; RTL alignment reverses correctly (D3).
  - **4**: anchor correct; credentials-imagery match correct; alignment correct; one `[STRONG]` drift at most.
  - **3**: one `[REQUIRED]` drift — one portrait in the leadership set doesn't quite fit the cluster terminology, OR one image caption overflows into the adjacent text.
  - **2**: multiple `[REQUIRED]` drifts.
  - **1**: `[BLOCKING]` failure — imagery mood contradicts voice anchor (e.g., "Il coaching non è terapia" + therapy couch), OR credentials name a world the imagery clearly does not show (legal copy + lab coats), OR voice anchor paraphrased/missing in any locale.
  - **0**: walk did not evaluate this dimension.

---

## 4 · Layer 1 · Blocking overrides (automatic FAIL)

Any of the following trips an **automatic FAIL** regardless of how the 15 dimensions score. These are not soft penalties — they short-circuit the whole scorecard. The verdict cannot be PASS or BORDERLINE if any override fires. Every override maps 1:1 to a `[BLOCKING]` rule in the sibling standards.

| # | Blocking override | Anchor | Why it's an override, not a score penalty |
|:-:|---|---|---|
| **O1** | Any `h1..h5` has RGB distance < 120 OR WCAG contrast < 4.5 against its background (paper or dark section) on any page × any locale. | BRWS-CONTRAST-01 · CS-PAL-01 · CS-HERO-03 · AP1 | Solaria `e8f38b5` pattern — every headline invisible. 506/506 tests missed it. One cream-on-cream render = shipped-broken. |
| **O2** | Horizontal scrollbar at any viewport in the §5 rubric matrix. | BRWS-VIEW-02 · CS-RESPONSIVE-02 · AP2 | Archetype responsive gap. One viewport with scrollWidth > clientWidth = unusable layout on that class of device. |
| **O3** | Hero does not stack OR nav does not collapse at ≤ 720 px. | BRWS-VIEW-03 · BRWS-VIEW-04 · CS-HERO-07 · CS-NAV-05 · AP2 | Mobile is broken — touch users can't navigate or read the hero. |
| **O4** | Any imagery URL 404s on the live render. | BRWS-IMG-01 · CS-IMG-SRC-01 | Broken media = broken site; visible gap in the hero/feature/leadership/case rails. |
| **O5** | Imagery subject fails the 3-second semantic check on any slot (e.g., PlayStation gamepad in a commercialista hero, Bumble Bee tuna as artisan ingredient). | BRWS-IMG-03 · CS-IMG-COH-01 · AP4 · Session 31 | The single class of defect that survives curator review and tests; only live walk catches it. |
| **O6** | Imagery mood contradicts the voice anchor (e.g., "Il coaching non è terapia" + therapy couch). | BRWS-IMG-04 · CS-IMG-COH-02 · CS-IMG-COH-07 | Mood-to-anchor contradiction destroys the archetype's premium read. |
| **O7** | Any non-Pexels URL on a NEW pilot (Pragma legacy Unsplash pool is the single tolerated exception until retro-pack lands). | BRWS-IMG-02 · CS-IMG-SRC-01 · AP3 | Factory-pipeline uniformity (Session 47 adoption). Zero exceptions except the documented Pragma grandfather. |
| **O8** | Editor click-to-edit affordance visible on the public `/live/` route (cookie-cleared). | BRWS-FEEL-02 · CS-MARKET-01 · A5 | Breaks the "real firm's site" illusion — site reads as a template demo. |
| **O9** | Lorem ipsum / "Replace this text" / "Your headline here" in rendered content. | BRWS-FEEL-03 · CS-MARKET-02 · CS-MARKET-03 | Template-marketplace leak; cannot ship. |
| **O10** | Fake certification in leadership (e.g., "Certified Life Transformation Expert"). | BRWS-FEEL-06 · CS-EXEC-03 · AP9 | Legal/professional misrepresentation; blocks on ethics before it blocks on design. |
| **O11** | Voice anchor missing or paraphrased in ANY of the 5 locales. | BRWS-FEEL-05 · CS-EXEC-01 · F2 | The archetype's identity anchor; cannot drift. |
| **O12** | D-054 10-gate differentiation absent from the module docstring, OR not triangulated against EVERY sibling on the archetype. | CS-EXEC-02 | Palette/voice/credential drift across siblings compounds across releases if not triangulated. |
| **O13** | Walk performed without recording dev-server URL + port in the verdict. | BRWS-SRV-02 · CS-BROWSER-02 | Phantom walks are rejected — user parallel verification depends on URL + port. |
| **O14** | Walk missing ANY viewport from the §5 rubric matrix. | BRWS-VIEW-01 · CS-RESPONSIVE-01 | Coverage gaps hide regressions; matrix is the floor, not a ceiling. |
| **O15** | Evidence directory incomplete (screenshots below floor, measurements.json missing, walk-log.md absent). | BRWS-EVID-01..03 · CS-BROWSER-01 | The scorecard is an audit artifact; without evidence it cannot be signed. |
| **O16** | Nav background ≠ `--primary` (polarity broken), OR > 1 accent element in nav. | BRWS-NAV-01 · BRWS-NAV-02 · CS-PAL-06 · CS-NAV-04 | Navbar is the first thing a visitor reads; polarity breakage signals the whole palette is off. |
| **O17** | Dark-section child text rendering dark-on-dark (distance < 120 or WCAG < 4.5 inside `.cs-section.dark` / `.cs-kpi-band` / dark `.cs-foot`). | BRWS-CONTRAST-02 · CS-PAL-04 · AP11 | Scoped AP1 class; a new child element forgetting the dark context creates an invisible-text pocket. |
| **O18** | No live browser walk performed at all (test-only ship). | CS-BROWSER-01 · AP8 | **Tests pass ≠ ship-ready.** The whole archetype's acceptance gate depends on the walk. No walk = no flip. |

**How overrides affect the scorecard**:

- If any override trips, write `Verdict: FAIL · Blocking override: O<n>` at the top of the scorecard and STOP. Do not proceed to fill per-dimension scores (beyond what the walk already measured). The remediation cycle restarts from the walk, not from the scorecard.
- Dimension scores may still be recorded for diagnostic value (the scorecard IS the record of what failed), but the verdict is final at override time.
- More than one override at once = record all of them. The verdict is still FAIL; the blocking-override list becomes the fix punch-list for the next walk.

---

## 5 · Layer 2 · Critical-dimension floors

Layer 1 catches the hard-blocking defects; Layer 2 catches the "high average score but one load-bearing dimension weak" failure mode. A template where 14 dimensions score 5 and one critical dimension scores 3 is **not** a pass — it ships with a soft spot in a load-bearing area. The floors below make that explicit.

**Critical dimensions** (9 of 15 · marked **[CRITICAL]** in §3):

| Dimension | Critical because |
|---|---|
| **D1 · Premium feel** | The archetype's reason to exist. A corporate-suite template that doesn't read premium has no shipping purpose. |
| **D2 · Elegance** | Restraint is the differentiator vs every other archetype in the catalog. |
| **D3 · Modern professionalism** | Voice, credentials, D-054 triangulation, RTL, accessibility — the institutional-contemporary claim hinges here. |
| **D4 · Hero readability** | First fold; first impression; contrast-critical. |
| **D10 · Imagery coherence** | The single defect class that survives CLI tests (AP4/AP5); only the browser walk catches it. |
| **D11 · Pexels-only compliance** | Factory-pipeline uniformity (Session 47); no drift tolerated. |
| **D12 · Contrast safety** | AP1 class — headlines invisible; the most load-bearing skin invariant. |
| **D13 · Responsive quality** | AP2 class — one of the two structural archetype gaps identified in the master audit. |
| **D14 · Browser live verification quality** | The ship gate itself. A weak walk poisons every other dimension's score. |

Floor rules:

- **Every CRITICAL dimension must score ≥ 4** for the verdict to be PASS.
- A single CRITICAL dimension at 3 forces the verdict to **BORDERLINE** (assuming Layer 1 did not trigger FAIL). Multiple CRITICAL dimensions at 3 force **FAIL**.
- Any CRITICAL dimension at **≤ 2** forces **FAIL** even with zero blocking overrides — a weak critical dimension is evidence the walk missed something or the template isn't ready. Remediate before re-walking.
- Non-critical dimensions (6 of 15 · D5 · D6 · D7 · D8 · D9 · D15) must score ≥ 3; any of them at ≤ 2 forces BORDERLINE at minimum, and at ≤ 1 forces FAIL.

**Why this model**: a simple average would let a template pass with hero contrast at 3 (AA-just-passing, AAA-miss) and navbar + footer + typography all at 5. That profile has a load-bearing weak point. Layer 2 makes the critical-dimension floors explicit so the reviewer can't round them away.

---

## 6 · Layer 3 · Aggregate thresholds

Once Layer 1 did not trigger FAIL and the Layer 2 critical floors are evaluated, the aggregate scores decide the final verdict.

### 6.1 · Thresholds

| Verdict | Condition |
|---|---|
| **PASS** | All 9 CRITICAL dimensions ≥ 4 AND all 6 non-critical dimensions ≥ 3 AND overall average ≥ 4.3 AND zero blocking overrides AND zero `[REQUIRED]` failures outstanding. |
| **BORDERLINE** | Zero blocking overrides AND zero CRITICAL dimensions < 4 broken to the point of FAIL (i.e., one CRITICAL at exactly 3 is borderline-allowed) AND overall average ≥ 3.8 AND no non-critical dimension ≤ 2 AND any remaining `[REQUIRED]` failures are enumerated. |
| **FAIL** | Any blocking override fires, OR any CRITICAL dimension ≤ 2, OR two or more CRITICAL dimensions at 3, OR any non-critical dimension ≤ 1, OR overall average < 3.8, OR the evidence directory is incomplete. |

**Overall average** is computed as the **arithmetic mean of the 15 dimension scores**, rounded to one decimal. CRITICAL dimensions are not weighted more heavily in the average — their extra weight comes from the §5 floors, not from the average computation. (Double-weighting would hide failures: a 5+5+5+3+5+5+5 could look fine averaged, but the 3 on a critical dimension still matters and §5 catches it.)

### 6.2 · Minimum score profile required for LIVE approval

A template is considered live-approved — i.e., release-gatekeeper may flip `TEMPLATE_REGISTRY.json` from `draft` to `published_live` (Commit B of the D-102 2-commit cadence) — if and only if:

1. **Layer 1**: zero blocking overrides fired (§4 · all 18 items clear).
2. **Layer 2 critical floors**: all 9 CRITICAL dimensions (D1, D2, D3, D4, D10, D11, D12, D13, D14) score ≥ 4.
3. **Layer 3 aggregate**: all 6 non-critical dimensions (D5, D6, D7, D8, D9, D15) score ≥ 3 AND overall average ≥ 4.3.
4. **Evidence**: the browser-rubric verdict is PASS with a full §7 evidence directory (120+ screenshots, measurements.json, walk-log.md, console.log).
5. **Server handshake**: the dev server is still running for user parallel verification, URL + port recorded.
6. **Zero `[REQUIRED]` failures outstanding**: the rubric's summary-counts block shows `[REQUIRED] failed: 0`.
7. **Deviations documented**: any `[STRONG]` failures are listed in the verdict's `§ deviation` block with written justification.

A template missing ANY of 1–7 is **not** live-approved. BORDERLINE is not an acceptance — it is a remediation note. FAIL is not a near-miss — it is a rebuild-the-walk instruction.

### 6.3 · Common score profiles and their verdicts

| Example profile | Verdict | Reason |
|---|---|---|
| All 15 dims at 5, zero overrides, complete evidence | **PASS** · reference class | Ideal — propose as pattern-library example. |
| CRITICAL: 5·5·4·4·4·5·4·4·5 (avg 4.4); non-critical: 4·4·4·4·4·4 (avg 4.0); overall 4.3 | **PASS** | Meets all floors and thresholds with modest margin. |
| CRITICAL: 5·5·5·3·5·5·5·5·5 (one at 3 = hero readability); non-critical all 5; overall 4.8 | **BORDERLINE** | Average is excellent, but hero readability (a CRITICAL) at 3 forces borderline. High average cannot rescue a soft critical. |
| CRITICAL: 5·5·5·5·5·5·5·3·5 (responsive at 3); non-critical all 5; overall 4.8 | **BORDERLINE** | Same shape — one critical at 3. |
| CRITICAL: 5·5·5·5·5·5·5·3·3 (responsive + browser walk both at 3); rest 5 | **FAIL** | Two CRITICAL dimensions at 3 = FAIL per §6.1. |
| CRITICAL all 4, non-critical all 3; overall 3.6 | **FAIL** | Overall average < 3.8 = FAIL. |
| CRITICAL all 5 except contrast-safety at 1; rest 5 | **FAIL · Override O1** | Blocking override trips — contrast failure short-circuits regardless of scores. |
| CRITICAL all 5; non-critical navbar at 2 | **BORDERLINE** at best; more likely **FAIL** | Non-critical ≤ 2 = at minimum BORDERLINE, likely FAIL if another dimension also drifts. |
| 14 dims at 5, imagery coherence at 1 (PlayStation gamepad in hero) | **FAIL · Override O5** | Imagery subject fails 3-second check — automatic FAIL. |
| Scorecard filled but walk never ran | **FAIL · Override O18** | No browser walk = automatic FAIL. |

---

## 7 · Sample completed scorecard format

Every completed scorecard lives at `factory/reports/quality-scorecards/<template-slug>/<run-timestamp>-scorecard.md`. The run-timestamp matches the browser-rubric evidence directory (BRWS-EVID-01) so the scorecard and the walk it scores are paired.

```markdown
# Corporate-suite Quality Scorecard · <template-slug>

**Verdict**: <PASS | BORDERLINE | FAIL>
**Template**: <slug> · <human name> · corporate-suite
**Branch**: <branch-name>
**Baseline tip**: <commit-hash> (<commit-subject-line>)
**Walk run**: <ISO-8601 basic timestamp · matches evidence dir>
**Scored by**: <agent or human name>
**Related rubric verdict**: `factory/reports/browser-verification/<slug>/<run-timestamp>/verdict.md`

## Layer 1 · Blocking overrides

- [ ] O1  Contrast — h1..h5 distance ≥ 120 & AA ≥ 4.5 on every page × locale
- [ ] O2  No horizontal scroll at any §5 matrix viewport
- [ ] O3  Hero stacks + nav collapses at ≤ 720 px
- [ ] O4  All imagery URLs resolve (zero 404s)
- [ ] O5  Imagery passes 3-second subject check on every slot
- [ ] O6  Imagery mood underlines voice anchor (no contradiction)
- [ ] O7  Every URL is Pexels (Pragma legacy exception acknowledged if applicable)
- [ ] O8  No editor affordances on `/live/` route
- [ ] O9  No lorem ipsum / "Replace this text" / "Your headline here"
- [ ] O10 No fake certifications in leadership
- [ ] O11 Voice anchor verbatim across 5/5 locales
- [ ] O12 D-054 10-gate triangulated in module docstring
- [ ] O13 Dev-server URL + port recorded
- [ ] O14 Full §5 viewport matrix walked
- [ ] O15 Evidence directory complete (screenshots ≥ 120, measurements.json, walk-log.md)
- [ ] O16 Navbar bg = `--primary` AND ≤ 1 accent element in nav
- [ ] O17 Dark-section child text AA ≥ 4.5 with RGB distance ≥ 120
- [ ] O18 Live browser walk performed

**Blocking overrides triggered**: <none | list O<n> with one-line observed evidence>

## Layer 2 · Critical-dimension floors

| # | Dimension | Score | Critical? | Floor met (≥ 4)? |
|:-:|---|:-:|:-:|:-:|
| D1 | Premium feel | <0-5> | ✓ | <yes/no> |
| D2 | Elegance | <0-5> | ✓ | <yes/no> |
| D3 | Modern professionalism | <0-5> | ✓ | <yes/no> |
| D4 | Hero readability | <0-5> | ✓ | <yes/no> |
| D10 | Imagery coherence | <0-5> | ✓ | <yes/no> |
| D11 | Pexels-only compliance | <0-5> | ✓ | <yes/no> |
| D12 | Contrast safety | <0-5> | ✓ | <yes/no> |
| D13 | Responsive quality | <0-5> | ✓ | <yes/no> |
| D14 | Browser live verification quality | <0-5> | ✓ | <yes/no> |

**Critical floors**: <all met · N met · M below floor>

## Layer 3 · All 15 dimensions

| # | Dimension | Score | Evidence (rubric tag · measurement · screenshot) | Notes |
|:-:|---|:-:|---|---|
| D1 | Premium feel | <0-5> | BRWS-FEEL-01 · <evidence> | <one-line> |
| D2 | Elegance | <0-5> | BRWS-HERO-05 · BRWS-RHYTHM-05 · <evidence> | <one-line> |
| D3 | Modern professionalism | <0-5> | BRWS-FEEL-05 · BRWS-FEEL-06 · <evidence> | <one-line> |
| D4 | Hero readability | <0-5> | BRWS-CONTRAST-01 · BRWS-READ-01 · <evidence> | <one-line> |
| D5 | Navbar quality | <0-5> | BRWS-NAV-01..04 · <evidence> | <one-line> |
| D6 | Footer quality | <0-5> | BRWS-FOOT-01..05 · <evidence> | <one-line> |
| D7 | Typography hierarchy | <0-5> | BRWS-HERO-05 · BRWS-READ-04 · BRWS-READ-05 · <evidence> | <one-line> |
| D8 | Spacing rhythm | <0-5> | BRWS-RHYTHM-01..05 · <evidence> | <one-line> |
| D9 | Imagery quality | <0-5> | BRWS-IMG-01 · BRWS-IMG-08 · <evidence> | <one-line> |
| D10 | Imagery coherence | <0-5> | BRWS-IMG-03 · BRWS-IMG-04 · <evidence> | <one-line> |
| D11 | Pexels-only compliance | <0-5> | BRWS-IMG-02 · <evidence> | <one-line> |
| D12 | Contrast safety | <0-5> | BRWS-CONTRAST-01..04 · <evidence> | <one-line> |
| D13 | Responsive quality | <0-5> | BRWS-VIEW-01..07 · BRWS-RESP-01..07 · <evidence> | <one-line> |
| D14 | Browser live verification quality | <0-5> | BRWS-EVID-01..06 · BRWS-SRV-01..05 · <evidence> | <one-line> |
| D15 | Text/image coherence | <0-5> | BRWS-IMG-04 · BRWS-FEEL-05 · BRWS-ALIGN-01 · <evidence> | <one-line> |

**Overall average**: <n.n> (arithmetic mean · unweighted · rounded to one decimal)

## Aggregate gate

- CRITICAL dims all ≥ 4? <yes | no · list failing>
- Non-critical dims all ≥ 3? <yes | no · list failing>
- Overall average ≥ 4.3? <yes | no · actual>
- `[REQUIRED]` failures outstanding (per rubric verdict)? <0 | list>
- `[STRONG]` deviations documented in rubric `§ deviation`? <yes | n/a>

## Verdict computation

- Layer 1 (blocking overrides): <clear | FAIL · O<n>>
- Layer 2 (critical floors): <clear | BORDERLINE/FAIL per §5>
- Layer 3 (aggregate): <PASS | BORDERLINE | FAIL per §6.1>
- **Final verdict**: <PASS | BORDERLINE | FAIL>

## Evidence pointers

- Rubric verdict: `factory/reports/browser-verification/<slug>/<run-timestamp>/verdict.md`
- Screenshot tree: `.../screenshots/` · <count> PNGs
- Measurements: `.../measurements.json`
- Walk log: `.../walk-log.md`
- Console: `.../console.log`
- Dev server: `http://127.0.0.1:<port>/` · <still running | closed at <timestamp>>

## Remediation (if BORDERLINE or FAIL)

<for each failing item, one bullet:>
- **<Override ID or Dimension ID>** · <one-line observed issue> → **fix**: <one-line action> · **retest**: new walk required before re-scoring.

<if PASS>
- None. Release-gatekeeper may proceed with Commit B (flip <slug> → `published_live`).

## Deviations (PASS only · waived [STRONG] findings)

<one bullet per waived [STRONG] failure, with written justification>

## Parallel-verification handshake

Dev server remains at `http://127.0.0.1:<port>/` for user parallel verification.
This scorecard is **<draft · final>** and will be **<revisable · immutable>** after user confirmation.

— end of scorecard —
```

---

## 8 · Agent workflow integration

This scorecard is built for agent-based workflows. Each agent contributes the dimensions that are in its remit; the release-gatekeeper aggregates and writes the final scorecard.

### 8.1 · Which agent scores which dimension

| Agent | Primary dimensions | Secondary inputs |
|---|---|---|
| **style-critic** | D1 · D2 · D7 · D8 | Reads design standard §1–12; spot-checks rendered DOM. |
| **contrast-accessibility-auditor** | D4 · D12 | Implements BRWS-CONTRAST-01..04 and CS-PAL-01 / CS-PAL-04 / CS-HERO-03 checks. |
| **responsive-auditor** | D13 | Drives the §5 viewport matrix; implements BRWS-VIEW-01..07 and BRWS-RESP-01..07. |
| **imagery-curator-reviewer** | D9 · D10 · D11 · D15 | Implements BRWS-IMG-01..09 + CS-IMG-COH-01..07 + CS-IMG-SRC-01..05. |
| **browser-verifier** | D5 · D6 · D14 | Runs the Playwright MCP walk; captures evidence; produces the rubric verdict that this scorecard pairs with. |
| **voice-and-credentials-auditor** (or style-critic extension) | D3 · D15 | Verifies voice anchor verbatim across locales, credentials cluster-specific, D-054 triangulation. |
| **release-gatekeeper** | (aggregation · no direct scoring) | Reads every agent's sub-scorecard, computes Layer 1 / 2 / 3 verdict, writes the final scorecard, gates the tier flip. |

### 8.2 · Agent handoff protocol

1. **browser-verifier runs first** — its rubric verdict is the single source of evidence for every downstream score. Without a completed rubric walk, no other agent can score.
2. Specialist agents (contrast, responsive, imagery, style, voice) read the rubric evidence directory and produce per-dimension sub-scorecards. Each sub-scorecard cites specific rubric tags and evidence artifacts.
3. **release-gatekeeper aggregates** — reads all sub-scorecards, applies Layer 1 overrides, enforces Layer 2 critical floors, computes Layer 3 aggregate, writes the final scorecard to `factory/reports/quality-scorecards/<slug>/<run-timestamp>-scorecard.md`, and acts on the verdict.
4. **User parallel verification is mandatory** — before the release-gatekeeper flips `TEMPLATE_REGISTRY.json`, the user opens the server URL in their own browser and confirms. The scorecard's "Parallel-verification handshake" block records this.
5. **Fail handling**: on FAIL, the release-gatekeeper does NOT patch the scorecard. It opens follow-up tasks named by override ID or dimension ID, a new branch pass produces a new walk + new scorecard at a fresh `<run-timestamp>`. Superseded scorecards stay in their directory for audit.

### 8.3 · Why this splits the work well

- **Single responsibility per agent** — contrast auditor doesn't need to understand voice anchor discipline; imagery curator doesn't need to understand responsive breakpoints.
- **Evidence flows one direction** — browser-verifier writes evidence; every other agent reads it. Zero back-editing.
- **Aggregation is deterministic** — given the per-agent sub-scorecards, the final verdict is a mechanical computation of §4 / §5 / §6. The release-gatekeeper adds no judgment it isn't justified in citing.
- **Parallel-verification is the final human gate** — the user sees the same URL + port the walk used, confirms in their own browser, and releases the gate.

---

## 9 · What this scorecard does NOT do

- **Does not replace the rubric verdict.** The rubric verdict (`corporate-suite-browser-rubric.md` §11) is the per-check evidence ledger; this scorecard is the dimensional roll-up. Both live side-by-side in the evidence directory.
- **Does not replace the design / imagery / blocking standards.** Those define the rules. This scorecard numerically summarizes how well a template meets them.
- **Does not weight CRITICAL dimensions in the average.** Extra weight comes from the Layer 2 floors (hard thresholds) instead of from the average (soft signal). Weighting the average hides failures; floors expose them.
- **Does not allow in-place editing.** Once written, a scorecard is immutable — a re-walk produces a new scorecard at a fresh timestamp.
- **Does not grant PASS on "average looks fine".** Blocking overrides + critical floors + aggregate thresholds must ALL clear. Any one layer can reject.
- **Does not touch code outside `factory/*`.** This file is advisory + ship-gate artifact only. Palette validators, responsive breakpoint code, reduced-motion JS — all are sibling hardening tasks.
- **Does not unpause Solaria Commit B.** Per binding user instruction, Solaria's EN/FR/ES/AR authoring remains paused until the hardening pass closes. When it resumes, Solaria will be the first template to pass through this scorecard end-to-end.

---

## 10 · Summary

### 10.1 · Scoring model in one paragraph

A template is scored across **15 dimensions** on a **0–5 scale**, with three distinct gates deciding the verdict in order: **(1) Blocking overrides** (§4) — 18 named defect patterns, any one of which short-circuits to FAIL regardless of scores; **(2) Critical-dimension floors** (§5) — 9 of 15 dimensions (premium feel, elegance, modern professionalism, hero readability, imagery coherence, Pexels compliance, contrast safety, responsive quality, browser walk quality) must individually score ≥ 4 for PASS, preventing "high average hides a weak critical"; **(3) Aggregate thresholds** (§6) — non-critical dimensions ≥ 3 AND overall average ≥ 4.3 AND zero outstanding `[REQUIRED]` rubric failures. PASS requires all three gates to clear. BORDERLINE is allowed when one critical is at 3 or when average dips toward 3.8 — BORDERLINE means "do not flip LIVE yet; remediate and re-walk." FAIL means "rebuild the walk."

### 10.2 · Critical override logic in one paragraph

The 18 blocking overrides (O1–O18) encode the defect patterns that MUST never ship, whether or not the scores say otherwise. They include every AP1-class contrast failure (cream-on-cream headlines — Solaria `e8f38b5`), every AP2-class responsive failure (horizontal scrollbar, hero that won't stack, nav that won't collapse), every AP4/AP5-class imagery-semantic failure (PlayStation gamepad, Bumble Bee tuna), every AP3-class Pexels-compliance failure, every AP9-class fake-credential failure, every CS-MARKET-class template-showcase leak, and every process failure (missing URL+port, missing walk, missing viewport matrix, missing evidence). Any single override trip = automatic FAIL. Overrides short-circuit: the release-gatekeeper writes `Verdict: FAIL · Blocking override: O<n>` at the top of the scorecard and opens remediation tasks. The next walk starts from a fresh timestamp — no in-place fixes, no patched scorecards, no averaging away the defect.

### 10.3 · Minimum score profile required for LIVE approval

A corporate-suite template may move from `draft` → `published_live` if and only if the following profile holds:

1. **Zero blocking overrides** (all 18 clear).
2. **All 9 CRITICAL dimensions ≥ 4**: D1 (Premium feel), D2 (Elegance), D3 (Modern professionalism), D4 (Hero readability), D10 (Imagery coherence), D11 (Pexels-only compliance), D12 (Contrast safety), D13 (Responsive quality), D14 (Browser live verification quality).
3. **All 6 non-critical dimensions ≥ 3**: D5 (Navbar), D6 (Footer), D7 (Typography), D8 (Spacing rhythm), D9 (Imagery quality), D15 (Text/image coherence).
4. **Overall average ≥ 4.3** (arithmetic mean of the 15 dimensions, unweighted, rounded to one decimal).
5. **Zero `[REQUIRED]` failures outstanding** in the paired browser-rubric verdict.
6. **Complete evidence directory** under `factory/reports/browser-verification/<slug>/<run-timestamp>/`: verdict.md + walk-log.md + 120+ screenshots (5 locales × 6 pages × 4 core viewports) + measurements.json + console.log.
7. **Dev server still running** at the recorded URL + port, so the user can parallel-verify in their own browser before the gatekeeper flips `TEMPLATE_REGISTRY.json`.
8. **`[STRONG]` deviations, if any, documented** in the `§ deviation` block with written justification.

Anything less than this full profile is not live-approved. Borderline is remediation. Fail is a rebuild. The scorecard is the single artifact that collapses the design standard, imagery standard, and browser rubric into one defensible PASS / BORDERLINE / FAIL — and the one artifact the release-gatekeeper is required to produce before flipping any corporate-suite template LIVE.
