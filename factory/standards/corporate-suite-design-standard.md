# Corporate-suite Design Standard

**Phase**: X.4a · Corporate-suite Factory Hardening · **Date**: 2026-04-21
**Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Scope**: factory files only · no `apps/editor`, `apps/projects`, `apps/commerce` changes · no new archetypes.
**Inputs**: `factory/reports/audits/corporate-suite-audit-master.md`, `factory/references/template-inventory.md`, `factory/references/pattern-library.md`, `factory/references/anti-pattern-library.md`.
**Audience**: every agent that plans, builds, edits, or reviews a corporate-suite template (template-planner, template-builder, template-editor-fixer, style-critic, browser-verifier, release-gatekeeper). This file is the canonical answer to "does this look premium/elegant/modern/professional?" — decision-oriented, not taste-based.

---

## 0 · How to use this document

1. Every rule carries a **severity tag**:
   - `[BLOCKING]` — violation prevents flip to `published_live`. Merge can land a draft, but `TEMPLATE_REGISTRY.json` stays on `draft` until fixed.
   - `[REQUIRED]` — violation must be fixed before the reviewer walk signs off. Draft merge allowed only with an open TODO.
   - `[STRONG]` — violation allowed only if explicitly justified in the module docstring (`§ design deviation`).
   - `[GUIDELINE]` — taste; document the reason if you break it.
2. Every decision should trace back to a named rule in this file by tag (e.g., `CS-T-02`, `CS-HERO-04`).
3. Pair this document with:
   - `corporate-suite-blocking-rules.md` (enforcement recipes · 1:1 with `[BLOCKING]` rules here),
   - `corporate-suite-browser-rubric.md` (the Playwright walk script that verifies this document),
   - `corporate-suite-imagery-standard.md` (G1-G3 patterns · pack format).
4. **Browser live verification is central to acceptance**. Every `[BLOCKING]` and `[REQUIRED]` rule in this document was written because a green CLI is a lower bound, not a ship signal. If you cannot open the live URL in a browser and walk it, you cannot sign off on this archetype.

---

## 1 · Operational meaning of "premium / elegant / modern / professional"

The four adjectives users use to describe this archetype decompose into checkable properties. Replace the adjective with the criterion when making a decision.

| Adjective user says | What it operationally means on corporate-suite |
|---|---|
| **Premium** | (a) Generous whitespace (96-100 px vertical, 72 px horizontal section padding). (b) Editorial imagery with credit overlays. (c) Tabular numerics. (d) No stock-collage feel — one hero photo, not a 4-up grid. (e) Gold/emerald/warm-earth accent used once or twice per viewport, never decoratively. |
| **Elegant** | (a) Serif heading + sans body. (b) Italic `<em>` carries emphasis in headings, not bold/uppercase. (c) Anchor line preserved verbatim in all locales. (d) One dark band per home (the KPI band) — not 3. (e) Letter-spacing is restraint-tracked: labels `0.22em`, body `0`. |
| **Modern** | (a) CSS custom properties driving the palette. (b) Logical properties + dir-aware layout (RTL works without duplicate CSS). (c) `:focus-visible` gold outline, not browser blue. (d) `prefers-reduced-motion` honored. (e) Breakpoints at 1100 and 720 — the skin adapts, not just shrinks. |
| **Professional** | (a) Verifiable credentials (ODCEC, Cassazionista, CONSOB) in leadership copy. (b) No marketing hyperbole ("sblocca il tuo potenziale"). (c) Licensure terminology consistent across locales. (d) Anonymized client proof only (no logos a commercialista can't legally show). (e) KPIs rounded to boardroom figures, never fake-precise decimals. |

If any agent output fails the right-column tests, it does not qualify as any of the left-column adjectives regardless of how it "feels."

---

## 2 · Overall visual tone

### CS-TONE-01 [BLOCKING] · Institutional-advisory, not startup-tech
- **Definition**: the visitor should feel they are reading a boutique advisory's materials, not a SaaS landing page.
- **Test**: a reader cannot mistake the page for (a) a VC-funded SaaS, (b) a coaching funnel, (c) a template-marketplace tile.
- **Evidence**: Pragma voice anchor "Dove si prendono le decisioni che contano"; Fiscus "L'adempimento corretto, non la trovata".
- **Failure modes**:
  - Emoji in body copy or headings.
  - Exclamation marks outside direct testimonial quotes.
  - "Get started free" CTA language.
  - Gradient backgrounds with multi-hue sweeps.

### CS-TONE-02 [BLOCKING] · Restraint over density
- **Definition**: negative space is a design element. Every section must breathe.
- **Test**: no section compresses its padding below `96px 72px` (desktop) to fit more content. If content doesn't fit, trim content, not padding.
- **Reference**: `_base.html` / `home.html` — every section wrapper uses `padding: 100px 72px; max-width: 1400px; margin: 0 auto`.

### CS-TONE-03 [REQUIRED] · One dark band per home, placed once
- **Definition**: the KPI band is THE dark surface on the home page. Dark sections elsewhere (CTA, case-study hero) are allowed but never two in sequence.
- **Test**: scroll home top-to-bottom; count sections with `background: var(--primary)`. Count must be ≤ 2 and they must not be adjacent.
- **Why**: three or more dark bands makes the page feel startup-aggressive; one dark band reads as editorial punctuation.

### CS-TONE-04 [STRONG] · Palette polarity follows the skin
- **Definition**: on this archetype `--primary` is the text/nav color (dark); body paper is cream. Do not invert.
- **Cross-reference**: CS-PAL-01 is the blocking numeric rule; this one states the tone implication.

### CS-TONE-05 [BLOCKING] · No template-marketplace aesthetic
- **Definition**: the page must not advertise that it is a template. It must read as a real firm's site.
- **Test**: remove the studio name — does the page still work as a real company site? If it only works as "a template showcase", it fails.
- **Concrete bans**:
  - Rainbow highlight on "Click to edit" zones visible in the live preview route (must be editor-preview-only per `body.mw-is-editor-preview { ... }` guard, `_base.html:441`).
  - Lorem ipsum anywhere.
  - Stock portrait placeholders with the grey "person silhouette" icon.
  - Text like "Your headline here" / "Insert subtitle".

---

## 3 · Typography hierarchy

Rules codify pattern B3, B4, B5.

### CS-TYPE-01 [BLOCKING] · Serif heading + sans body · humanist/transitional pairing
- **Allowed families for headings**: Merriweather (Pragma), IBM Plex Serif (Fiscus), Fraunces (Solaria), or any serif from the humanist/transitional/slab axis (e.g., PT Serif, Source Serif, Lora, Recoleta).
- **Allowed families for body**: Inter (Pragma/Solaria), IBM Plex Sans (Fiscus), or a neutral sans of the same x-height class.
- **Disallowed**: geometric sans on headings (Montserrat, Poppins, Raleway). Display-script on headings. Monospace anywhere except KPI `.num`.

### CS-TYPE-02 [REQUIRED] · Italic `<em>` is the emphasis mechanism in headings
- **Rule**: wrap the one load-bearing word per headline in `<em>…</em>`. Do not use `<strong>`, uppercase, or color shifts to emphasize in headings.
- **Evidence**: `_base.html:91` — `h1 em, h2 em, h3 em { font-style: italic; color: var(--primary); }`.
- **DON'T**: "L'ADEMPIMENTO CORRETTO, NON LA TROVATA" (shouting).
- **DO**: "L'adempimento <em>corretto</em>, non la trovata".

### CS-TYPE-03 [BLOCKING] · Tabular numerals on every KPI figure
- **Rule**: any element displaying a number in the KPI band, stat strips, or case-study metrics uses `.num` class (`font-variant-numeric: tabular-nums`). Without tabular-nums, "180+" and "94%" misalign vertically across locales.

### CS-TYPE-04 [REQUIRED] · Heading scale is restrained
| Level | Font-size floor | Font-size ceiling | Use |
|---|---:|---:|---|
| Hero h1 | 44 px | 72 px | ONE per page |
| Section h2 | 32 px | 48 px | one per section |
| Card/sub h3 | 22 px | 28 px | card titles |
| Eyebrow / label | 12 px | 14 px | tracked 0.22em, uppercase |
| Body | 16 px | 18 px | paragraphs |

- **DON'T**: 96 px neon display headline — reads startup, not advisory.
- **DO**: 56-64 px serif h1 with italic `<em>` emphasis on one word.

### CS-TYPE-05 [REQUIRED] · Letter-spacing — restraint-tracked
- Eyebrow / label classes: `letter-spacing: 0.22em` uppercase.
- Body / headings: `letter-spacing: 0` (default).
- Under `html[dir="rtl"]`: all `0.22em` tracking resets to `0` (D4 pattern). If you add a new tracked label class, add it to the reset list in `_base.html:337-369`.

### CS-TYPE-06 [BLOCKING] · Arabic locale uses Kufi heading + Amiri body
- **Rule**: `html[dir="rtl"]` swaps `--heading` to Noto Kufi Arabic and `--body` to Amiri (pattern D1). Latin wordmark and `.num` keep the Latin heading font (pattern D2).
- **DON'T**: leave Latin serif under RTL — Arabic glyphs render as squares.

---

## 4 · Color · palette · accent/navbar harmony

Rules codify pattern B1, B2 and anti-patterns AP1, AP7, AP10, AP11.

### CS-PAL-01 [BLOCKING] · `--primary` is dark foreground · L\* ≤ 40 on cream paper
- **Rule**: every new palette on this archetype MUST provide a `primary` hex that is dark enough to pass:
  - RGB max channel ≤ 80 (approx), OR
  - Computed L\* in CIELAB ≤ 40 against `#F7F4EC` cream paper, OR
  - WCAG AA contrast ≥ 7.0 vs cream body background (AAA for small text).
- **Why**: `--primary` is reused as text (`h1..h5`), nav background, KPI band background, button fill. If it is light, body text becomes invisible (AP1 · Solaria bug).
- **Enforcement**: palette validator (to be added in X.4a Step N+) rejects any tier advance to `published_live` with a light primary. Until then: mandatory live browser walk per CS-BROWSER-01.
- **Cross-reference**: blocking rule 1:1 in `corporate-suite-blocking-rules.md`.

### CS-PAL-02 [BLOCKING] · Secondary + accent are the differentiation vector (D-054)
- **Rule**: the secondary and accent colors differentiate siblings on the same skin. Across Pragma/Fiscus/Solaria the trio is (cool blue/emerald) · (cool gold/navy) · (warm ocra/caramel). A 4th template must pick an orthogonal warmth/hue axis.
- **Test**: side-by-side at 1280×800 of sibling homes — do they read as different firms? If two feel interchangeable, the secondary+accent pair is not doing its D-054 job.
- **Failure mode (AP10)**: every sibling drifts into variants of navy+gold.

### CS-PAL-03 [REQUIRED] · Three tokens only — no fourth brand color
- **Rule**: palette ships exactly `primary / secondary / accent`. Additional color variables (`--primary-2`, `--accent-tint`) must be DERIVED server-side from the three tokens, not hardcoded.
- **Current known violation (AP7)**: `_base.html:20` hardcodes `--primary-2: #2c3e6b`. This navy value hurts every non-Pragma template. Hardening task: either derive or drop.

### CS-PAL-04 [BLOCKING] · Dark-section child text uses `--on-dark` variants
- **Rule**: any text, button, or border inside a section with `background: var(--primary)` (or any dark surface) must pick its color from `--on-dark`, `--on-dark-2`, `--on-dark-3`. Do not use `--ink` on dark surfaces.
- **Failure mode (AP11)**: adding a new child element that forgets the dark context creates dark-on-dark pockets that tests miss.
- **Test**: `document.querySelectorAll('.cs-section.dark *')` in DevTools — every element with `getComputedStyle.color` should be light; flag RGB distance < 120 from the section background.

### CS-PAL-05 [REQUIRED] · Accent used as punctuation · not decoration
- **Rule**: accent color appears at most 2-3 times per viewport (not per page — per viewport). Use it for: the one primary CTA button, the `:focus-visible` outline, one editorial pull-quote border, one italic headline word's emphasis.
- **DON'T**: accent underlines on every link, accent dividers between every section, accent-filled icon squares on every card.
- **DO**: one accent CTA per section · the rest of the page is primary+neutral+photographic.

### CS-PAL-06 [BLOCKING] · Navbar background = `--primary` · navbar text = `--on-dark`
- **Rule**: the top nav is always the dark band. Matching background-to-primary-token means palette identity flows through the chrome.
- **Evidence**: `_base.html:130` — `.cs-nav { background: var(--primary); }`.
- **Failure mode**: light nav on cream body disappears visually on scroll; dark nav on dark hero also disappears. Keep the contract.

---

## 5 · Hero readability and premium feel

### CS-HERO-01 [BLOCKING] · 55/45 split · serif h1 LEFT · one full-bleed photo RIGHT
- **Rule**: hero grid is `grid-template-columns: 1.3fr 1fr` desktop. Left column: eyebrow + serif h1 (with italic `<em>`) + subhead + meta-strip + primary CTA. Right column: ONE photo from imagery pool slot 0 (`hero`), full-bleed with credit overlay.
- **Evidence**: `home.html:5-67`.
- **Reuse**: copy author fills left text block; imagery curator fills slot 0. No mid-hero overlays, no 4-up photo grid, no video backgrounds.

### CS-HERO-02 [BLOCKING] · Hero photo is editorial, not stock
- **Rule**: hero photo must (a) come from the curator's Pexels pack, (b) match the imagery direction (e.g., `executive-boardroom`, `fiscal-desk-documents`, `coaching-1to1`), (c) carry a credit overlay labeling it as editorial, (d) resolve at ≥ 1600×900.
- **Failure mode (AP5)**: "smiling businesswoman shaking hands in vague office" — fails the semantic check.
- **Cross-reference**: `corporate-suite-imagery-standard.md` G1, G3.

### CS-HERO-03 [BLOCKING] · Hero h1 contrast against paper is AAA
- **Rule**: h1 in `color: var(--primary)` on cream paper must meet WCAG AAA (≥ 7.0) for text ≥ 44 px is conservative — enforce AA (≥ 4.5) as a floor and AAA as the target. Pragma/Fiscus/Solaria-post-fix all pass AAA by construction when CS-PAL-01 is respected.
- **Test**: DevTools → inspect h1 → contrast ratio ≥ 7.0.

### CS-HERO-04 [REQUIRED] · Hero has ONE primary CTA · at most ONE secondary
- **Rule**: left column renders exactly one primary button (accent-filled) + optionally one ghost/outline secondary. Never three.
- **Failure mode**: three CTAs in the hero reads as a consumer-funnel page (template-marketplace aesthetic, AP / CS-TONE-05).

### CS-HERO-05 [REQUIRED] · Hero subhead is one paragraph, ≤ 35 words
- **Rule**: the subhead under h1 clarifies the proposition in one dense sentence. Multiple sentences push the fold below the hero image and break the editorial pacing.

### CS-HERO-06 [REQUIRED] · Hero meta-strip carries credential anchors
- **Rule**: the meta-strip below the subhead shows 2-4 credential snippets (e.g., "Iscritti ODCEC Milano · Cassazionisti · Revisori Legali"). These are the verifiable trust anchors per CS-COPY-03.
- **DON'T**: "Trusted by 10,000+ clients" — unverifiable, reads funnel.

### CS-HERO-07 [BLOCKING] · Below 720px viewport the split collapses to stacked
- **Rule**: at `@media (max-width: 720px)`, hero grid becomes `grid-template-columns: 1fr`. Text stacks above the photo. This must exist in the skin (currently MISSING — see AP2 responsive gap).
- **Ship gate**: hardening pass adds this breakpoint before CS-RESPONSIVE-03 can be satisfied.

---

## 6 · Navbar quality and states

### CS-NAV-01 [BLOCKING] · Sticky dark nav · primary background · wordmark + links + locale switcher + CTA
- **Rule**: nav is `position: sticky; top: 0; z-index: 100`, background `var(--primary)`. Composition: left wordmark · center or right link group (5-7 links) · locale switcher pill · trailing accent CTA.
- **Evidence**: `_base.html:130-210`.

### CS-NAV-02 [BLOCKING] · Hover, focus, and active-route states are distinct and visible
- **Rule**: every nav link has 4 visual states:
  1. Default — `color: var(--on-dark-2)` with subtle opacity,
  2. Hover — color upgrades to `var(--on-dark)` (full white),
  3. Focus-visible — gold accent outline (`:focus-visible` cascade, E1 pattern, `outline: 2px solid var(--accent); outline-offset: 4px`),
  4. Active / current page — underline or accent dot indicator, NOT accent-color text.
- **DON'T**: browser-default blue focus ring. Reset and style.
- **Test (browser walk)**: keyboard `Tab` through the nav — every link shows a visible gold outline.

### CS-NAV-03 [REQUIRED] · Locale switcher is a pill with current-state and lang+dir on each link
- **Rule**: locale switcher renders `<a lang="ar" dir="rtl">…</a>` etc. per locale. Active locale is indicated visually. See pattern D5.
- **Test**: open DevTools on any locale page, hover the switcher — each link's `lang` and `dir` attributes must match the target locale.

### CS-NAV-04 [REQUIRED] · Nav CTA uses accent · stands as the one button in the chrome
- **Rule**: trailing CTA is accent-filled ("Prenota una consulenza", "Prenota una call conoscitiva", …). It is the only accent element in the nav.
- **DON'T**: accent-coloring the wordmark or accent dividers between links.

### CS-NAV-05 [BLOCKING] · Below 1100px the nav condenses · below 720px becomes a hamburger
- **Rule**: breakpoints at 1100 (reduce padding, tighter links) and 720 (collapse to a menu trigger). Agency archetype is the reference (`templates/live_templates/agency/agency-creative-studio/_base.html:349,359`).
- **Ship gate**: missing in the current skin (AP2). Fix before flipping any new pilot LIVE.

### CS-NAV-06 [REQUIRED] · Wordmark stays in Latin heading font under RTL
- **Rule**: the wordmark (e.g., "Fiscus", "Pragma") keeps the Latin heading font even on AR pages (pattern D2 · `_base.html:371-387`). Arabic-glyphs for a Latin brand name misreads.

---

## 7 · Footer quality

### CS-FOOT-01 [REQUIRED] · Three-column footer · brand + sitemap + contact
- **Composition**: column 1 = wordmark + 1-line tagline + social/legal stubs; column 2 = sitemap links grouped by section; column 3 = coordinates (address, phone, email, hours).
- **Rule**: footer uses `background: var(--primary)` OR a deep neutral; text in `var(--on-dark)`/`var(--on-dark-2)`. Match the navbar polarity.

### CS-FOOT-02 [REQUIRED] · Legal row · copyright + P.IVA + privacy + cookie + whistleblowing
- **Rule**: bottom legal row carries the 5 canonical links. For commercialisti/law/advisory the whistleblowing link is REQUIRED per D.lgs. 24/2023; for other clusters it's optional.
- **DON'T**: social media icons as the only footer content.

### CS-FOOT-03 [REQUIRED] · Latin wordmark + Latin numerics in RTL footer
- **Same rule as CS-NAV-06** applied to `.cs-foot .brand .word` and `.num` per pattern D2.

### CS-FOOT-04 [GUIDELINE] · No newsletter signup above the legal row
- **Why**: advisory firms don't run newsletter funnels. If a pilot wants one, the primary CTA in the last section ("Prenota una call") carries that intent. The footer stays sober.

### CS-FOOT-05 [REQUIRED] · Footer has its own responsive collapse at 720px
- **Rule**: 3 columns → 1 column stacked at `@media (max-width: 720px)`. Missing today. Fix in the hardening pass.

---

## 8 · Section rhythm and spacing

### CS-RHYTHM-01 [BLOCKING] · Section wrapper: `padding: 100px 72px; max-width: 1400px; margin: 0 auto`
- **Rule**: every section on home, about, services, case-study-list, case-study-detail uses this padding/max-width contract. No section compresses to 40px vertical to fit more content.
- **Evidence**: `home.html` every section.

### CS-RHYTHM-02 [REQUIRED] · Home section order is fixed
- **Order**: hero · pillars · KPI band · sectors ribbon + trust band · leadership · cases · CTA.
- **Why**: institutional pacing — proposition → method → proof-in-numbers → sectors served → people → work shown → invite. Reordering to e.g., "cases first" reads as portfolio-site, not advisory.
- **Evidence**: `home.html:5-384`.

### CS-RHYTHM-03 [REQUIRED] · One dark section per home · placed as KPI band at position 3
- **Rule**: the KPI band is the dark grounding beat. No other section on home is dark unless justified in the docstring `§ design deviation`.
- **Cross-reference**: CS-TONE-03.

### CS-RHYTHM-04 [REQUIRED] · No section duplicates the function of the previous one
- **Example failure**: "Our services" section followed by "What we do" section — duplicate intent.
- **Test**: write a one-word label for each section (hero/pillars/kpi/sectors/leadership/cases/cta). If two adjacent sections get the same label, merge or cut.

### CS-RHYTHM-05 [REQUIRED] · Section titles use the italic-em restraint pattern
- **Rule**: section h2 follows the same emphasis rule as hero h1 — one italic `<em>` wrap if emphasis is needed. No uppercase section titles.

### CS-RHYTHM-06 [REQUIRED] · Vertical spacing between sections ≥ their own padding
- **Rule**: sections have their own `100px 72px` padding; there is no additional margin between them. The padding IS the rhythm. Do not add 40px margins that shrink the breath.

---

## 9 · Content density rules

### CS-DENSITY-01 [BLOCKING] · Hero subhead ≤ 35 words · h1 ≤ 12 words
- See CS-HERO-05 and CS-TYPE-04.

### CS-DENSITY-02 [REQUIRED] · Pillars section: 3 or 4 cards · not 6
- **Rule**: the pillars/services grid is 3 or 4 columns. 6 cards reads as feature-matrix, not advisory.

### CS-DENSITY-03 [REQUIRED] · Card body copy ≤ 60 words per card
- **Rule**: card titles ≤ 6 words; card body ≤ 3 short sentences. Dense legal prose belongs in case-study-detail or a dedicated services page, not in home cards.

### CS-DENSITY-04 [REQUIRED] · KPI band shows 3 or 4 stats · never more
- **Rule**: the dark band holds 3 (preferred) or 4 figures. 5+ stats ruins the boardroom feel.

### CS-DENSITY-05 [REQUIRED] · Leadership: 3-6 people · each with name + title + 2-3 credentials + portrait
- **Rule**: leadership block names real roles (Partner, Senior Associate, Counsel), not marketing titles ("Visionary Chief Happiness Architect"). Credentials follow CS-COPY-03.

### CS-DENSITY-06 [REQUIRED] · Cases: 3-6 on home · more on `case_study_list`
- **Rule**: home shows 3-6 featured cases. Listing page (`case_study_list.html`) holds the full set.

### CS-DENSITY-07 [STRONG] · No section is a wall of text
- **Test**: any `<p>` above 120 words is a red flag on home/about/services. Split, or move to case-study-detail.

---

## 10 · CTA hierarchy

### CS-CTA-01 [BLOCKING] · One primary CTA per viewport · accent-filled
- **Rule**: the primary CTA is the accent-filled button. It appears once in the hero, once in the final CTA section, and optionally inline in services. Total per home: 2-3. Per viewport as the user scrolls: always at most one primary.
- **Failure mode**: three accent buttons in the hero (see CS-HERO-04).

### CS-CTA-02 [REQUIRED] · CTA label names the action in the advisor's voice
- **Preferred**: "Prenota una consulenza", "Prenota una call conoscitiva", "Richiedi un'analisi preliminare", "Inizia il percorso di coaching".
- **Disallowed**: "Click here", "Get started free", "Sign up now", "Iscriviti gratis".

### CS-CTA-03 [REQUIRED] · Secondary CTAs are ghost/outline · never accent-filled
- **Rule**: if a section offers two actions, the primary is accent-filled and the secondary is outlined/ghost using `--primary` or a neutral.
- **Failure mode**: two accent buttons side by side — the visitor cannot tell which one is primary.

### CS-CTA-04 [REQUIRED] · CTA targets are real routes, not `#`
- **Rule**: every CTA `href` goes to a real route (`/contact/`, `/services/`, `/case-studies/`). `href="#"` or `href="#contact"` placeholders fail the browser walk.

### CS-CTA-05 [REQUIRED] · Final-section CTA is the cadence closer
- **Rule**: home ends with a dark or tinted CTA section that restates the voice anchor and offers one primary action. This is the one place the voice anchor appears as a section headline.

### § Decision · Primary CTA on paper surfaces — outline-only is intentional restraint (NOT a placeholder reading)

**Phase**: X.4a · Step 2E P1D · **Date**: 2026-04-26 · **Status**: APPROVED · **Direction**: WAIVER (no `.cs-btn-primary--solid` modifier introduced)

**Question carried forward from Step 1B → 1D → Round 1 → Round 2 → Round 3 → Round 4 → P1C**:
On cream paper surfaces (hero, mid-page CTA contexts outside the dark `.cs-cta` band), the primary CTA renders as an outline-boxed button (`.cs-btn-primary { color: var(--primary); border: 1.5px solid var(--primary); }` per `_base.html:348-355`) rather than an accent-filled solid. Style-critic memos at Step 1B flagged this as "reads placeholder, not executive button" and proposed introducing a `.cs-btn-primary--solid` modifier (or a paper-scoped override keyed to `.cs-lead` / `.cs-hero`) so the primary on cream looks like a filled boardroom button.

**Decision**: WAIVER — the outline-only primary on cream is the **intentional archetype contract** and is **not** a placeholder reading. No `.cs-btn-primary--solid` modifier is introduced. The skin contract at `_base.html:342-347` (the `/* CTA primitives · CS-CTA-01/03 · primary reads as outline-boxed boardroom button on cream paper (light-tier dominance via shape, not fill — keeps the accent budget for state and punctuation); ghost is a typographic-underline. The dark-section override in '.cs-cta .actions .cs-btn-primary' inverts the polarity so the same primitive reads correctly on either surface. */` comment) is now ratified at the standards layer.

**Why this is the right call** (each row independently load-bearing):

1. **Live-walk evidence supersedes the early style-critic memo.** The Step 1B "placeholder reading" was a single offline observation; four rounds of Playwright walks (Step 1D IT-LTR · Round 2 reduced-motion · Round 3 LTR multi-locale EN/FR/ES · Round 4 RTL AR + re-verification) and the AP8 first-run pipeline scorecard (`factory/reports/scorecard/fiscus-pipeline-round1/style-critic.md §5`) all rendered the cream-surface primary as outline-only and graded **D1 = 5 (reference-class)** with **zero** finding citing it as placeholder. A reading flagged once offline that **never recurred** under five distinct live-walk passes across two templates × five locales is a hypothesized defect, not an observed one.
2. **Accent budget binding (CS-PAL-05) constrains the answer.** CS-PAL-05 caps accent-color hits at "≤ 2-3 per viewport." On the home above-the-fold, the existing accent budget already funds: (a) one trailing nav CTA, (b) the eyebrow before-mark, (c) the hero h1 italic `<em>`, (d) the `.cs-btn-primary:after` arrow glyph (accent-coloured via `_base.html:356`), and (e) the `:focus-visible` gold ring on tab-walk. Promoting the hero primary's body fill to accent would push the above-the-fold accent count to 4-5 hits — over budget and reading "decorative wash" rather than "punctuation." This is precisely the AP10/AP11 polarity-drift class the four-round hardening just closed; a solid-fill modifier would re-introduce the same risk class.
3. **Tone alignment binding (CS-TONE-01).** CS-TONE-01 requires institutional-advisory polarity, not startup-tech. Outline-boxed buttons are the boardroom convention (Bain, BCG, McKinsey, Deloitte advisory pages all default to outline-or-letter primaries on cream stationery); accent-filled glow primaries are the SaaS funnel convention. The reading "outline = placeholder" is a SaaS-trained reflex; the reading "outline = institutional restraint" is the cluster-correct anchor.
4. **Polarity inversion already exists where it matters (`_base.html:346`).** The dark-section override `.cs-cta .actions .cs-btn-primary { color: var(--on-dark); border-color: var(--accent); }` (defined at `home.html:311-313` for the home final-CTA band, recapped in the `_base.html:346` comment) already promotes the same primitive to a high-emphasis cream-on-navy button on every dark CTA band. The visitor's funnel-completion CTA (the cadence-closer, CS-CTA-05) reads as a confident filled boardroom button; the upstream hero/mid-page CTAs read as restraint-first outline buttons. The two states answer different jobs and the existing override pattern is the reason a separate `--solid` modifier is not needed.
5. **Modifier proliferation has a cost.** Introducing `.cs-btn-primary--solid` would add a third CTA primitive (alongside `.cs-btn-primary` and `.cs-btn-ghost`); every page file would need a per-section decision rule for which primitive to use; every locale walk would need a new BRWS-* check verifying the right primitive landed in the right slot; the planner brief (CS-EXEC-02) would need a new D-054 gate ("CTA primitive choice"). The cost is non-zero and the offsetting evidence for the gain is absent.
6. **Touch-target and focus-ring contracts are unaffected.** The waiver does not change `:focus-visible` (still gold accent ring, `_base.html:370-378`), does not change touch-target floors (CTAs already meet 44 × 44 at 390 per Round 3 + Round 4 measurements), and does not change the ghost-CTA waiver under `CS-CTA-03` (separate decision, P2 scope, unchanged here).

**What this decision is NOT**:
- It is **not** a license to use outline-only buttons everywhere. The dark `.cs-cta` band override (cream-on-navy fill via `border-color: var(--accent)`) remains the cadence-closer treatment and remains required by CS-CTA-05.
- It is **not** a waiver of CS-CTA-01 (one primary CTA per viewport): outline-only does not mean optional or de-emphasized; it means restraint-as-emphasis. The button must still be the single dominant action per viewport.
- It is **not** a waiver of the AAA contrast floor: outline + body color = `--primary` on cream = 12.81 / 12.86 ratio (verified across Pragma + Fiscus four-round corpus); the contract holds.
- It is **not** retroactive — a future archetype (e.g., a startup-saas variant or a consumer-facing template) is free to choose accent-filled primaries; this decision binds **corporate-suite** specifically.

**What changes**:
- This `§ decision` block is the standards-layer ratification.
- The skin comment at `_base.html:342-347` already encodes the intent; no skin edit required.
- The `template-planner` agent's CS-EXEC-02 D-054 gate "CTA tone" continues to read CTA copy + position + bound-form composition (per `factory/agents/template-planner.md §3.2 row 10`) — primitive choice is **not** a D-054 differentiation gate.
- The `style-critic` agent should **not** flag outline-only primary on cream as a `[STRONG]` deviation in future Fiscus / Pragma / Solaria scorecards. If a reviewer reaches for this finding again, this `§ decision` block is the reference.

**Implementation footprint**: zero. No code changes, no test changes, no skin edits. The decision is a standards-layer ratification of the existing skin contract.

**Anchor**: `CS-CTA-01` (one primary per viewport) · `CS-CTA-03` (secondary = ghost) · `CS-CTA-05` (cadence closer) · `CS-TONE-01` (institutional-advisory) · `CS-PAL-05` (accent as punctuation) · `_base.html:342-358` (skin contract) · `home.html:311-315` (dark-section polarity inversion).

**Closes**: T-P1-5 from `factory/reports/hardening/step2-followup-plan.md §3.P1` and the open question carried at `factory/reports/hardening/step2-readiness-reassessment.md §S6`. Frees the archetype to advance from Conditional-Go to Go per plan §10.3 once T-P1-4 (D-054 triangulation refresh, this same Step 2E P1D) lands.

---

## 11 · Section composition rules

### CS-COMP-01 [REQUIRED] · Sectors ribbon + trust band — anonymized proof
- **Rule**: corporate-suite clusters (commercialista, law, advisory) often can't show client logos (secreto professionale). Use a text-only sectors ribbon ("Manifattura · Retail · Real Estate · Wellness") + a logo marquee of industry associations (ODCEC, Assolombarda, …), NOT client logos. See pattern C4.
- **DON'T**: fake client logos.

### CS-COMP-02 [REQUIRED] · Leadership section uses portrait photos, not avatars
- **Rule**: each leader has a real portrait pulled from slots 2-3 (`portrait`) of the imagery pool. Resolution ≥ 800×800. Grey silhouette placeholders = blocking failure.

### CS-COMP-03 [REQUIRED] · Case-study cards use `detail` / `ambient` imagery slots
- **Rule**: cases on home pull photos from imagery pool slots 4-5. The hero photo (slot 0) is NOT reused as a case thumbnail.

### CS-COMP-04 [REQUIRED] · Case-study-detail has kpi-strip · team-strip · next-case block
- **Rule**: detail page order: breadcrumb · hero title + lede · kpi-strip (reusing `.cs-kpi-band`) · narrative body · team-strip · next-case. See `case_study_detail.html:1-166`.

### CS-COMP-05 [REQUIRED] · Contact page splits form + coordinates column
- **Rule**: `/contact/` layout is 2-column — form left, coordinates right. The only file with a current responsive breakpoint (`contact.html` `@media (max-width: 880px)`). At 880px it stacks form above coordinates.

### CS-COMP-06 [REQUIRED] · About page opens with a timeline, not a "Our Story" wall of text
- **Rule**: about renders studio history as a timeline (year · moment · one line), followed by values (3-4 cards), team grid, coordinates. See `about.html:1-202`.

### CS-COMP-07 [BLOCKING] · Every section wrapper carries the `cs-` class prefix
- **Rule**: no raw Bootstrap classes on section elements. New components follow `cs-{name}` pattern (A3 · scoped archetype CSS). Mixing `cs-kpi-band` with `container-fluid row col-md-4` breaks the scoped-prefix guarantee.

---

## 12 · Executive / corporate premium feel

### CS-EXEC-01 [BLOCKING] · Voice anchor is preserved verbatim across all 5 locales
- **Rule**: the anchor line (one sentence · from cluster blueprint §5) translates but remains identifiable per locale. See F2 pattern.
- **Test**: grep the IT anchor in `template_content_{name}.py`, then grep the translated anchor in `_en.py`, `_fr.py`, `_es.py`, `_ar.py`. Each must be the voice-carrier sentence.

### CS-EXEC-02 [BLOCKING] · D-054 10-gate differentiation is present in every module docstring
- **Rule**: every `template_content_{name}.py` opens with a 10-dimension differentiation block diffed against EVERY sibling on this archetype (not just one). Pragma vs Elevate (legacy) is insufficient once Fiscus and Solaria exist. Triangulate.

### CS-EXEC-03 [BLOCKING] · Credentials in leadership are verifiable, cluster-specific
- **Rule**: leadership `credentials` field uses vocabulary from the cluster blueprint §4 terminology dictionary:
  - Commercialista: ODCEC Milano, sezione A, Revisore Legale reg. n., Cassazionista, LL.M. Bocconi.
  - Law: Albo Avvocati Milano, Cassazionista, Università Bocconi/LUISS.
  - Coaching: ICF PCC/MCC, EMCC Senior Practitioner, AICP.
  - Corporate/advisory: CONSOB Albo n., ABI, Assogestioni.
- **Failure mode (AP9)**: "Certified Life Transformation Expert" — fake certification.

### CS-EXEC-04 [REQUIRED] · No marketing hyperbole
- **Banned phrases** (cross-locale):
  - "Sblocca il tuo potenziale" / "Unlock your potential"
  - "Trasforma la tua vita in X giorni"
  - "Versione migliore di te"
  - "Mindset vincente"
  - "10,000+ clients trusted us"
  - "Game-changing", "revolutionary", "next-gen", "world-class"
- **Banned quotes**: Einstein, Jung, Gandhi, Steve Jobs.
- **Cross-reference**: AP9 · documented in Solaria module docstring lines 22-34.

### CS-EXEC-05 [REQUIRED] · KPIs are boardroom figures · rounded · no fake decimals
- **Rule**: "180+", "94%", "€ 1.4 B" — clean figures a reviewer can defend. Not "187.4 clients" or "93.7%".

### CS-EXEC-06 [REQUIRED] · First-person-plural voice ("ci", "we") anchors authority
- **Rule**: site speaks as the firm ("Noi seguiamo ~ ", "We advise ~ "). Not as a product ("Our platform helps you ~ ").

### CS-EXEC-07 [REQUIRED] · No funnel-pattern sections
- **Disallowed**: "Free diagnosis in 10 questions", "Download our free ebook", urgency countdown timers, "limited spots", lead-magnet forms before the leadership section.

---

## 13 · Rules to avoid the template-marketplace look

### CS-MARKET-01 [BLOCKING] · The live preview route must not reveal editor affordances
- **Rule**: editor-only affordances (click-to-edit halos, region selector highlights, edit-zone badges) render ONLY under `body.mw-is-editor-preview` (pattern A5 · `_base.html:441-452`). The public `/templates/<slug>/live/` route must render as a real firm's site.
- **Test**: load the live URL in an incognito browser (no editor cookies). No edit affordances must appear.

### CS-MARKET-02 [BLOCKING] · No lorem ipsum anywhere
- **Rule**: every content field uses cluster-specific copy. Even placeholder images must carry the cluster's imagery direction.

### CS-MARKET-03 [BLOCKING] · No "Replace this text" / "Your headline here" strings
- **Rule**: template-author-facing placeholders belong in the editor schema, not in the rendered content modules.

### CS-MARKET-04 [REQUIRED] · No feature-grid of "What you get" CMS bragging
- **Rule**: a corporate-suite site talks about the FIRM's services, not about the template's features. "Responsive design ✓ SEO optimized ✓ Mobile friendly ✓" belongs on the template marketplace tile, NEVER in the rendered site.

### CS-MARKET-05 [REQUIRED] · No "Made with Marketweb" badge in the rendered site
- **Rule**: the rendered template is presented as the firm's own site. Marketplace attribution lives on the marketplace, not in the footer.

### CS-MARKET-06 [REQUIRED] · No demo-data-only placeholder avatars
- **Rule**: portraits are from the curated imagery pack. The "initial-in-a-circle" avatar placeholder is editor-UI only, never in the live render.

### CS-MARKET-07 [REQUIRED] · The studio name and voice are coherent with the copy
- **Rule**: if the studio name is "Fiscus", the meta-strip, leadership, cases, and contact address all reference the Fiscus identity. No cross-pollination with Pragma or Solaria copy.

---

## 14 · Desktop / tablet / mobile expectations

Codifies AP2 gap. The current skin breaks below ~1100px because the hardening pass has not landed yet. This section specifies the TARGET state every new pilot must ship against.

### CS-RESPONSIVE-01 [BLOCKING] · Three breakpoints · 1100px · 720px · plus contact-form 880px
- **Desktop** (≥ 1101 px): full layout · 55/45 hero · 3-4 column cards · section padding 100px 72px · nav horizontal links.
- **Tablet** (721–1100 px): tighter section padding (72px 48px) · cards reflow to 2 columns where appropriate · nav links tighter but still horizontal · hero becomes 60/40 or keeps 55/45 with smaller h1.
- **Mobile** (≤ 720 px): section padding 56px 24px · hero stacks (text above photo) · cards 1-column · nav collapses to hamburger · locale switcher dropdown.
- **Contact form** (≤ 880 px): form and coordinates stack (already present — `contact.html`).

### CS-RESPONSIVE-02 [BLOCKING] · No horizontal scrollbar at any target viewport
- **Test viewports**: 1920 · 1440 · 1280 · 1024 · 768 · 414 · 390.
- **Rule**: `document.documentElement.scrollWidth <= clientWidth` at every target viewport. Playwright MCP `browser_resize` + `browser_evaluate(() => document.documentElement.scrollWidth)` verifies.

### CS-RESPONSIVE-03 [BLOCKING] · Hero h1 never crushes below 32px mobile
- **Rule**: at 390px, hero h1 font-size floor is 32px. Below that the italic `<em>` detail is lost and the headline reads weak.

### CS-RESPONSIVE-04 [REQUIRED] · Tabular numerals and KPI band remain aligned on mobile
- **Rule**: KPI band restacks as a 2×2 or 1×N grid on mobile · each stat keeps its serif figure + sans caption. `font-variant-numeric: tabular-nums` preserved.

### CS-RESPONSIVE-05 [REQUIRED] · Imagery in cards uses `object-fit: cover` with aspect-ratio lock
- **Rule**: `aspect-ratio: 4/3` or `3/2` on card images. No `height: auto` letting tall portraits expand cards asymmetrically on mobile.

### CS-RESPONSIVE-06 [REQUIRED] · Touch targets ≥ 44×44 px
- **Rule**: CTAs, nav links, and locale pills meet the Apple HIG / WCAG 2.5.5 target minimum on mobile. Buttons that are 32×20 fail.

### CS-RESPONSIVE-07 [REQUIRED] · `:focus-visible` gold outline works on keyboard AND on switch/keyboard-only mobile
- **Rule**: focus outline appears under keyboard navigation regardless of viewport. E1 pattern must survive the responsive collapse.

### CS-RESPONSIVE-08 [STRONG] · RTL layouts tested at all three viewport classes
- **Rule**: the RTL-specific grid flips (pattern D3) must survive mobile stack. At 390px RTL, nav hamburger opens to the right, locale switcher remains legible.

---

## 15 · Browser live verification — acceptance gate

### CS-BROWSER-01 [BLOCKING] · No pilot flips to `published_live` without a live browser walk
- **Rule**: 506/506 tests green is NECESSARY but NOT SUFFICIENT. The reviewer walk (Playwright MCP or manual) is the ship gate.
- **Walk scope** per pilot:
  1. All 5 locales (IT / EN / FR / ES / AR) — language switcher works, anchor line preserved, RTL polarity correct for AR.
  2. All target viewports (1920 / 1440 / 1280 / 1024 / 768 / 390) — no horizontal scroll, hero stacks correctly at ≤ 720, nav collapses.
  3. All pages on the archetype (home · about · services · case_study_list · case_study_detail · contact).
  4. DOM contrast check — run the h1-vs-body RGB distance check on every page (AP1 prevention).
  5. Dark-section child check — no dark-on-dark text pockets (AP11 prevention).
  6. Focus-visible keyboard walk — tab through each page; every interactive element shows the gold outline (E1).
  7. Imagery semantic check — each photo passes the "does a member of this profession recognize their world?" test (AP4/AP5).
- **Artifact**: screenshots saved under `factory/reports/browser-verification/{template-slug}/` per locale × viewport.
- **Cross-reference**: `corporate-suite-browser-rubric.md` is the exact walk script that implements this rule.

### CS-BROWSER-02 [BLOCKING] · Dev server URL + port must be recorded in the walk log
- **Rule**: the walk log includes `http://127.0.0.1:{port}/` and the timestamp. No phantom walks.

### CS-BROWSER-03 [REQUIRED] · Tests-then-browser is the order, but browser has the veto
- **Rule**: run `python manage.py test apps` before the walk. If tests fail, the walk is pointless. If tests pass, the walk decides.

---

## 16 · DO / DON'T summary (quick reference for agents)

### DO
- Use serif headings + sans body · italic `<em>` for emphasis.
- Keep `--primary` dark (L\* ≤ 40 on cream).
- Place ONE dark section on home (KPI band, position 3).
- Curate a Pexels pack per template BEFORE writing copy.
- Preserve the voice anchor verbatim across all 5 locales.
- Enforce `@media (max-width: 1100px)` + `@media (max-width: 720px)` on every page of the skin.
- Run the Playwright walk at 1920/1280/1024/768/390 for every locale.
- Use `.num` + tabular numerals on every KPI figure.
- Wrap one load-bearing word per headline in `<em>`.
- Cite cluster-verifiable credentials (ODCEC, Cassazionista, ICF, CONSOB).

### DON'T
- Don't set `--primary` to a light color (AP1).
- Don't ship without live browser verification (AP8).
- Don't paraphrase the voice anchor.
- Don't use geometric sans on headings (Montserrat, Poppins).
- Don't show client logos a commercialista can't legally show.
- Don't use "Unlock your potential" / "Trasforma la tua vita" / Einstein quotes (AP9).
- Don't place two accent buttons side-by-side.
- Don't add a 4th brand color (`--primary-2` is already a known issue — AP7).
- Don't reuse imagery URLs across clusters (AP6).
- Don't ship Unsplash imagery on a new pilot (AP3 · Pexels-only).
- Don't show "Replace this text" / "Your headline here" in the live render.
- Don't crush section padding below `100px 72px` on desktop.
- Don't announce "Made with Marketweb" in the footer.

---

## 17 · Blocking examples (fail ship) vs non-blocking examples (fail polish)

### Blocking examples — MUST fix before merge or LIVE flip

| Example | Why it blocks | Rule |
|---|---|---|
| Solaria `primary=#F7F3EC` cream — all h1-h5 invisible cream-on-cream | Skin convention violation (AP1) | CS-PAL-01 |
| Hero shows 6 cards in a grid instead of one full-bleed photo | Reads template-marketplace, not advisory | CS-HERO-01 |
| At 720px viewport the hero split stays horizontal, horizontal scroll appears | AP2 responsive gap | CS-RESPONSIVE-01 / CS-HERO-07 |
| `.cs-section.dark .new-class { color: var(--ink); }` — dark-on-dark pocket | AP11 / CS-PAL-04 | CS-PAL-04 |
| Hero h1 contrast 3.8:1 on cream (AA small-text fails) | Fails readability floor | CS-HERO-03 |
| Fake certification "Certified Life Transformation Expert" | AP9 / CS-EXEC-03 | CS-EXEC-03 |
| "Replace this text" string in live render | Template-marketplace leak | CS-MARKET-03 |
| Voice anchor paraphrased in `_en.py` ("Where important decisions are made" instead of a faithful render of the IT anchor) | F2 / CS-EXEC-01 | CS-EXEC-01 |
| `href="#"` on the hero primary CTA | Broken CTA | CS-CTA-04 |
| Editor click-to-edit halo appears on public `/live/` URL | A5 / CS-MARKET-01 | CS-MARKET-01 |
| Navbar focus ring is browser-default blue | E1 / CS-NAV-02 | CS-NAV-02 |
| No recorded Playwright walk before LIVE flip | AP8 / CS-BROWSER-01 | CS-BROWSER-01 |

### Non-blocking examples — SHOULD fix before sign-off but don't block merge

| Example | Why non-blocking | Rule |
|---|---|---|
| KPI band shows 5 stats instead of 3-4 | Density drift, not a broken page | CS-DENSITY-04 |
| Secondary CTA is accent-filled instead of ghost | Visual hierarchy muddied, not broken | CS-CTA-03 |
| Section padding is `88px 72px` instead of `100px 72px` | Rhythm drift | CS-RHYTHM-01 |
| Pragma imagery still on Unsplash (legacy) | Pre-factory; migration planned | CS-IMG (see imagery standard) · AP3 |
| `--primary-2` hardcoded as `#2c3e6b` | Known skin issue, needs refactor | AP7 · CS-PAL-03 |
| Home has 7 featured cases instead of 3-6 | Density drift | CS-DENSITY-06 |
| Footer legal row missing whistleblowing link (commercialista/law cluster) | Required per cluster, not per archetype | CS-FOOT-02 |
| Logo marquee duration 60s instead of 110s | Feels consumer-tech, not advisory | E3 (acceptable pattern · drift) |
| About page opens with a paragraph before the timeline | Less editorial cadence | CS-COMP-06 |
| Reduced-motion `[data-lm]` coverage unverified | AP12 · polish | CS-RESPONSIVE-07 |

---

## 18 · Rule index (fast lookup)

| Tag | One-line rule |
|---|---|
| CS-TONE-01 | Institutional-advisory tone, not startup-tech |
| CS-TONE-02 | Restraint over density — breathe |
| CS-TONE-03 | One dark band per home, placed once |
| CS-TONE-04 | Palette polarity follows the skin |
| CS-TONE-05 | No template-marketplace aesthetic |
| CS-TYPE-01 | Serif heading + sans body, humanist/transitional |
| CS-TYPE-02 | Italic `<em>` is the heading emphasis |
| CS-TYPE-03 | Tabular numerals on every KPI figure |
| CS-TYPE-04 | Restrained heading scale |
| CS-TYPE-05 | Letter-spacing 0.22em for labels, 0 for body |
| CS-TYPE-06 | Arabic Kufi+Amiri swap under RTL |
| CS-PAL-01 | `--primary` L\* ≤ 40 on cream (BLOCKING) |
| CS-PAL-02 | Secondary+accent are the D-054 differentiation vector |
| CS-PAL-03 | Three tokens only — no hardcoded fourth color |
| CS-PAL-04 | Dark-section child text uses `--on-dark` variants |
| CS-PAL-05 | Accent is punctuation, not decoration |
| CS-PAL-06 | Navbar = `--primary` bg + `--on-dark` text |
| CS-HERO-01 | 55/45 split, serif LEFT + photo RIGHT |
| CS-HERO-02 | Editorial hero photo from curated pack |
| CS-HERO-03 | Hero h1 AAA contrast on paper |
| CS-HERO-04 | One primary CTA in hero, at most one secondary |
| CS-HERO-05 | Subhead ≤ 35 words |
| CS-HERO-06 | Meta-strip carries credential anchors |
| CS-HERO-07 | Hero stacks at ≤ 720px |
| CS-NAV-01 | Sticky dark nav with 5 elements |
| CS-NAV-02 | 4 nav-link states distinct and visible |
| CS-NAV-03 | Locale switcher pill, lang+dir per link |
| CS-NAV-04 | Nav CTA is accent-filled |
| CS-NAV-05 | Nav condenses at 1100, hamburger at 720 |
| CS-NAV-06 | Latin wordmark under RTL |
| CS-FOOT-01 | 3-column footer: brand + sitemap + contact |
| CS-FOOT-02 | Legal row + whistleblowing (cluster-specific) |
| CS-FOOT-03 | Latin wordmark + .num in RTL footer |
| CS-FOOT-04 | No newsletter signup |
| CS-FOOT-05 | Footer stacks at 720px |
| CS-RHYTHM-01 | Section wrapper 100px 72px, max-width 1400 |
| CS-RHYTHM-02 | Home section order is fixed |
| CS-RHYTHM-03 | One dark section (KPI band) on home |
| CS-RHYTHM-04 | No two adjacent sections with same function |
| CS-RHYTHM-05 | Section titles use italic-em restraint |
| CS-RHYTHM-06 | Padding IS the rhythm, no extra margins |
| CS-DENSITY-01 | Hero subhead ≤ 35 words, h1 ≤ 12 words |
| CS-DENSITY-02 | Pillars: 3 or 4 cards |
| CS-DENSITY-03 | Card body ≤ 60 words |
| CS-DENSITY-04 | KPI band: 3 or 4 stats |
| CS-DENSITY-05 | Leadership: 3-6 people |
| CS-DENSITY-06 | Cases: 3-6 on home |
| CS-DENSITY-07 | No section is a wall of text |
| CS-CTA-01 | One primary CTA per viewport |
| CS-CTA-02 | CTA label in advisor's voice |
| CS-CTA-03 | Secondary CTAs are ghost/outline |
| CS-CTA-04 | CTAs target real routes, not `#` |
| CS-CTA-05 | Final-section CTA is the cadence closer |
| CS-COMP-01 | Anonymized proof (text ribbon + association marquee) |
| CS-COMP-02 | Leadership portraits, not avatars |
| CS-COMP-03 | Case cards use `detail`/`ambient` slots |
| CS-COMP-04 | Case-study-detail: kpi-strip + team-strip + next-case |
| CS-COMP-05 | Contact = form + coordinates, 880px breakpoint |
| CS-COMP-06 | About opens with timeline, not wall of text |
| CS-COMP-07 | Scoped `cs-` class prefix |
| CS-EXEC-01 | Voice anchor verbatim across 5 locales |
| CS-EXEC-02 | D-054 10-gate in module docstring, triangulated |
| CS-EXEC-03 | Credentials are verifiable and cluster-specific |
| CS-EXEC-04 | No marketing hyperbole, no celebrity quotes |
| CS-EXEC-05 | KPIs are clean boardroom figures |
| CS-EXEC-06 | First-person-plural firm voice |
| CS-EXEC-07 | No funnel-pattern sections |
| CS-MARKET-01 | Editor affordances gated by body class |
| CS-MARKET-02 | No lorem ipsum |
| CS-MARKET-03 | No "Replace this text" strings |
| CS-MARKET-04 | No "What you get" feature-grid |
| CS-MARKET-05 | No "Made with Marketweb" badge |
| CS-MARKET-06 | No placeholder avatars in live render |
| CS-MARKET-07 | Studio name coherent with all copy |
| CS-RESPONSIVE-01 | 1100 + 720 + contact 880 breakpoints |
| CS-RESPONSIVE-02 | No horizontal scroll at any viewport |
| CS-RESPONSIVE-03 | Hero h1 ≥ 32px at 390px |
| CS-RESPONSIVE-04 | KPI band restacks preserving tabular-nums |
| CS-RESPONSIVE-05 | Card images use aspect-ratio + object-fit cover |
| CS-RESPONSIVE-06 | Touch targets ≥ 44×44 |
| CS-RESPONSIVE-07 | `:focus-visible` survives all viewports |
| CS-RESPONSIVE-08 | RTL tested at all three viewport classes |
| CS-BROWSER-01 | Live browser walk is the ship gate |
| CS-BROWSER-02 | Dev server URL + port in the walk log |
| CS-BROWSER-03 | Tests-then-browser, browser has the veto |
| CS-LF2-VAR-V1 | LF-2 second occupant adopts ≥3 within-cell sub-variants vs Cornice |
| CS-LF2-VAR-V2 | LF-2 second occupant portrait composition diverges ≥2 axes vs Cornice |
| CS-LF2-VAR-V3 | LF-2 second occupant CTA verb-class differs from Cornice's `Apri-X` |
| CS-LF2-VAR-V4 | LF-2 second occupant KPI cell semantic class diverges ≥1 cell vs Cornice |
| CS-LF2-VAR-V5 | LF-2 third occupant clears AC-V1..V4 vs BOTH Cornice AND the 2nd occupant |

---

## 19 · LF-2 family-internal variance rules (CS-LF2-VAR-V1..V5)

**Status**: ratified 2026-05-05 · Phase X.7d hardening · paper-only.
**Source**: anti-clone-2.0 audit (`factory/reports/hardening/anti-clone-2.0-rules.md`) scored Cornice ↔ Causa = 21/54 with 3 critical-axis vetoes failed (CTA · motion · imagery). The correct fix is NOT family migration but LF-2 family-internal variance rules.
**Ratification authorities**:
- `factory/reports/hardening/lf2-family-internal-variance-rules.md` (the binding hardening report · all reasoning · 12 browser gates F2-VAR-1..12).
- `design-orchestrator/references/internal-baselines/lf2-second-occupant-variance-contract.md` (the orchestrator-side intake contract · LF-2 claims registry · failure-mode catalog).
- `design-orchestrator/references/internal-baselines/visible-distinctness-thresholds-v2.md §7` (the per-axis rubric · same AC-V1..V5 in table form).
- `design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md §4 AC-1..AC-16` (the negative companion · what NOT to copy verbatim — the AC-V rules are the positive companion: what MUST be diversified).

**Cluster-context (why these rules exist here, not at the cluster-invariant layer)**:
LF-2 is the only multi-occupancy layout family in the corporate-suite cluster today (Cornice 1st · Causa 2nd at `tier=draft`). The other 4 layout families (LF-1 Pragma · LF-3 Fiscus · LF-4 Solaria · LF-5 Continua) are single-occupancy and per-family AC-V rules are paper-deferred until a 2nd occupant proposes the family. CS-LF2-VAR-* binds LF-2 only; LF-{N}-VAR-* would be authored at each family's first 2nd-occupant intake.

### CS-LF2-VAR-V1 [REQUIRED] · ≥ 3 within-cell sub-variants vs Cornice
- **Rule**: a 2nd LF-2 occupant adopts ≥ 3 patterns from the LF-2 sub-variant pool that the 1st occupant (Cornice) does not ship: NAV-1 sticky-condensed-on-scroll · NAV-3 progress-bar-light-touch · EDIT-2 pull-quote-em-reveal-longer-delay · QUOTE-4 sticky-stack-rotate · EVID-2 attestation-chip-hover · EVID-3 case-citation-pop · EVID-5 provenance-tooltip · TIME-3 chronological-tick-horizontal · KPI-2 count-up animation. Cornice ships 0 of 9 (static LF-2 baseline).
- **Why**: closes axis 18 (motion + page choreography critical-axis veto · floor 2) AND raises axis 9 (cases-preview · floor 2) AND axis 7 (KPI · floor 2) AND axis 17 (imagery register critical-axis veto · floor 2 · via EVID-5 · the only LF-2-internal axis-17 lever).
- **Test at A.1 intake**: brief lists ≥ 3 chosen sub-variants. Test at A.5 build: builder wires ≥ 3 patterns. Test at A.6 review-lock: style-critic counts ≥ 3 rendered. Test at workflow C/D walk: F2-VAR-1 fires under both default-motion AND `prefers-reduced-motion: reduce`.
- **Failure mode**: 2nd occupant ships 0-2 sub-variants OR ships only static-equivalent without the live motion (motion-mode leakage).
- **Cross-reference**: `factory/reports/hardening/lf2-family-internal-variance-rules.md §4 AC-V1` · `factory/reports/hardening/premium-dynamic-pattern-library.md §2` (the 9 patterns in the pool).

### CS-LF2-VAR-V2 [REQUIRED] · Portrait composition divergence ≥ 2 axes
- **Rule**: a 2nd LF-2 occupant's leadership single-portrait composition diverges from the 1st occupant's on ≥ 2 of: subject posture · subject activity · room props · photographic register. Gender, ethnicity, age are NOT axes of distinctness for this rule.
- **Why**: closes axis 8 (leadership) toward floor 2. Both occupants inherit AC-1's L6 = `single-portrait-feature` cell verbatim; divergence happens within the cell.
- **Test at A.3 imagery curate**: pool selection brief declares the 4 axes vs Cornice (and Causa for the 3rd occupant). Test at A.6 review-lock: style-critic side-by-sides at 1280px and counts shared axes. Test at walk: F2-VAR-4 captures both portraits at 1280px and confirms ≥ 2 axes diverge.
- **Failure mode**: portrait that overlaps Cornice on ≥ 3 of 4 axes.
- **Cross-reference**: `factory/reports/hardening/lf2-family-internal-variance-rules.md §4 AC-V2` · `cornice-lf2-reference-pack.md §3 D6` (Cornice's load-bearing portrait composition).

### CS-LF2-VAR-V3 [REQUIRED] · CTA inflection family divergence
- **Rule**: a 2nd LF-2 occupant's CTA inflection family is non-`Apri-X` (Cornice's claim · `Apri un fascicolo progetto`). Open inside LF-2: `Sottometti-X` · `Richiedi-X` · `Visualizza-X` · `Esplora-X`. Forbidden inside LF-2 (claimed by other corporate-suite siblings): `Fissa-X` (Pragma) · `Primo + abstract noun` (Fiscus) · `Prenota-X` (Solaria) · `Avvia-X` (Continua).
- **Why**: closes axis 13 (CTA mental model + inflection family) critical-axis veto floor 2. Same inflection family with same mental model is forbidden under anti-clone 2.0 v2.0 — a Cornice-cognate `Apri-X` produces axis 13 = 1 today (veto fail).
- **Locale parity**: chosen verb-class propagates verbatim across 5 locales without collapsing onto Cornice's translation (`Apri / Open / Ouvrez / Abre / افتح` is forbidden in any locale).
- **Test at A.4 copy author**: voice-anchor-lock declares verb-class. Test at A.6 review-lock: style-critic loops 25 routes (5 locales × 5 page kinds) and confirms primary CTA pill is non-Apri-cognate. Test at walk: F2-VAR-2 confirms.
- **Failure mode**: any locale's primary CTA pill reads `Apri-X` cognate. Frozen-sibling regression check: Cornice still reads `Apri un fascicolo progetto` verbatim.
- **Cross-reference**: `factory/reports/hardening/lf2-family-internal-variance-rules.md §4 AC-V3` · `cornice-lf2-reference-pack.md §4 AC-8` (Cornice's CTA semantic-family claim) · CS-CTA-02 (advisor's-voice CTA copy at cluster level).

### CS-LF2-VAR-V4 [REQUIRED] · KPI cell semantic-class divergence ≥ 1 cell
- **Rule**: a 2nd LF-2 occupant's hero-overlay KPI tuple shares the 3-cell SHAPE with Cornice (per AC-1 verbatim L5 inheritance — the family's L5 = `hero-overlay`) but diverges semantic class on ≥ 1 of the 3 cells. Closed registry of cell semantic classes: count · period-anchored · publication-anchored · achievement-anchored · year-range · regulatory-anchor (regulatory-anchor is taken by Fiscus L3 mid-strip · forbidden inside LF-2 KPI).
- **Why**: closes axis 7 (KPI placement + cell shape) toward floor 2. Cornice's tuple `(novanta fascicoli · 2008 · 38 menzioni)` = (count · period · publication). A 2nd occupant tuple must NOT match all 3 classes.
- **Test at A.5 build**: builder's KPI authoring brief declares each cell's semantic class. Test at A.6 review-lock: style-critic checks tuple semantic-shape vs Cornice. Test at walk: F2-VAR-3 parses rendered tuple and classifies each cell.
- **Failure mode**: 3-cell tuple matches Cornice on all 3 semantic classes.
- **Cross-reference**: `factory/reports/hardening/lf2-family-internal-variance-rules.md §4 AC-V4` · CS-DENSITY-04 (KPI band 3-or-4 stats at cluster level).

### CS-LF2-VAR-V5 [REQUIRED] · Cumulative two-pair ladder for the 3rd LF-2 occupant
- **Rule**: a 3rd LF-2 occupant clears CS-LF2-VAR-V1..V4 vs **both** Cornice AND the 2nd occupant (Causa post-retrofit). Two-pair scoring at A.1 intake; both pairs must clear 27/54 within-family threshold AND all 5 critical-axis vetoes ≥ floor.
- **Sub-variant adoption** (V1 cumulative form): ≥ 3 sub-variants AND ≥ 1 of those is unused by both Cornice (ships 0) AND Causa (post-retrofit ships NAV-1 + KPI-2 + EVID-3 + TIME-3 + EVID-5 = 5). The open set for the 3rd occupant: NAV-3 · EDIT-2 · QUOTE-4 · EVID-2.
- **Promoted from `[GUIDELINE]` → `[REQUIRED]`**: the priority plan paper-proposed AC-V5 as a guideline; ratification raises it to required because soft-guideline scoring lets the 3rd occupant pass selectively against one sibling while collapsing visibly against the other.
- **Pre-condition**: the 3rd-occupant intake CANNOT open until the 2nd occupant (Causa) ships at hardening parity. PENDING-row Causa columns (per `lf2-second-occupant-variance-contract.md §3.2`) produce an unstable scoring matrix.
- **Test at A.1 intake**: brief carries two pair matrices (vs Cornice · vs Causa). Test at workflow C/D walk: F2-VAR-6 + F2-VAR-7 fire (matrix vs Cornice + matrix vs Causa) AND F2-VAR-8 voice-anchor cognate ladder safety AND F2-VAR-9 audience-verb register check.
- **Failure mode**: 3rd occupant passes one pair but not the other · OR one critical-axis veto fails on either pair.
- **Cross-reference**: `factory/reports/hardening/lf2-family-internal-variance-rules.md §4 AC-V5` · `corporate-suite-retrofit-priority-plan.md §1 AC-V5` (the promotion path).

### Pragma ↔ Fiscus 2.0-grandfathered exception · 2026-05-05

Per `corporate-suite-retrofit-priority-plan.md §2`: Pragma ↔ Fiscus scored 22/54 under anti-clone 2.0 with 2 critical-axis vetoes failed (motion + imagery). Both `published_live` since the editor program era. Retrofit cost 5–10× higher than Causa's because of public-flip cascade undoing. The pair is accepted-as-grandfathered under the existing CS-LAYOUT-12 in-family near-occupant § decision (filed 2026-05-03 · 2/9 layout-axis exception) extended at 2.0 ratification:

- The 2.0-grandfather applies ONLY to Pragma ↔ Fiscus.
- It applies ONLY at the 2.0-veto layer (axis 18 motion · axis 17 imagery).
- It does NOT apply to other corporate-suite pairs.
- Re-evaluation triggers: catalog ≥ 50 templates · OR Pragma's Unsplash grandfather (W001) closure · OR Phase X.10+ batch retrofit pass.

**Action**: NO retrofit. Document the carry-over.

### How CS-LF2-VAR-* applies at each workflow gate

| Gate | Rule(s) verified | Evidence written |
|---|---|---|
| A.0 territory-scout | LF-2 second-occupant prerequisites (P1-P7 per intake contract §2) | territory scout report includes LF-2 occupancy snapshot |
| A.1 intake | CS-LF2-VAR-V1..V5 declared in brief · 18-axis matrix vs each existing LF-2 occupant | planner brief carries matrix |
| A.2 plan | CS-LF2-VAR-V1..V5 + critical-axis veto check | plan re-spec on any veto fail |
| A.3 imagery curate | CS-LF2-VAR-V2 portrait composition declaration | pool selection brief 4-axis declaration |
| A.4 copy author | CS-LF2-VAR-V3 verb-class declaration · CS-LF2-VAR-V4 KPI tuple semantic shape declaration | voice-anchor-lock + KPI authoring brief |
| A.5 build | CS-LF2-VAR-V1 sub-variants wired · CS-LF2-VAR-V4 KPI authored | builder declares chosen sub-variants in module docstring |
| A.6 review-lock | all 5 rules verified rendered · 18-axis matrix vs Cornice (and Causa for 3rd) | review-lock report carries scored matrix |
| Workflow C/D walk | F2-VAR-1..12 browser gates · 5 locales · 5 viewports · frozen siblings | walk-log.md per gate |
| Release-gatekeeper at flip | aggregated 18-axis score in scorecard · all 5 critical-axis vetoes ≥ floor | scorecard panel |

### Failure-mode summary

A failure of any CS-LF2-VAR-* rule blocks tier flip. The failure-mode catalog (10 named modes F-LF2-V1..V10) lives in `lf2-second-occupant-variance-contract.md §7`. The most common at intake are:
- F-LF2-V1 (V1 below 3 sub-variants): re-spec at A.0.
- F-LF2-V4 (V3 verb-class is `Apri-X` or any taken class): copy-author re-spec.
- F-LF2-V6 (18-axis matrix below 27/54 vs Cornice): re-route — likely candidate is LF-{NEW}.
- F-LF2-V7 (critical-axis veto fail at intake): re-spec on the failing axis.

---

## 20 · `motion_profile` DNA cell (CS-MOTION-DNA-01..04)

**Status**: ratified 2026-05-05 · Phase X.7b hardening · paper-only · no apps/* edits this pass.
**Source**: anti-clone-2.0 audit (`factory/reports/hardening/anti-clone-2.0-rules.md §1 axis 18 + §3 critical-axis veto`) named motion gravity + page choreography a critical-axis-veto field at floor 2 vs every sibling. The slice-01 implementation (`factory/reports/hardening/premium-dynamic-implementation-slice-01.md`) put the field on disk; the Phase X.7b plan (`factory/reports/hardening/motion-profile-dna-plan.md`) elevates it to a first-class DNA axis the planner declares at A.1 intake.
**Ratification authorities**:
- `factory/reports/hardening/motion-profile-dna-plan.md` (the binding 16-section plan · §1 enumerated values · §3 per-profile feel + safe pool · §4 per-cluster allowed-set · §5 anti-tacky red-lines · §6 reduced-motion fallback · §7 axis-18 scoring · §15 sibling-7 decision)
- `design-orchestrator/references/internal-baselines/motion-profile-catalog.md` (planner-side table-driven reference · §3 cluster allowed-set · §4 sibling claim registry · §7 anti-tacky checklist for style-critic A.6 walk · §8 reduced-motion fallback for browser-verifier C/D walk)
- `factory/reports/hardening/premium-dynamic-pattern-library.md` (the 12-family · 48-pattern source vocabulary · 6 motion gravities G1-G6)

### CS-MOTION-DNA-01 [REQUIRED] · `motion_profile` is declared at A.1 intake from the cluster's allowed set
- **Rule**: every new sibling brief carries `motion_profile` ∈ {`g1-safe-premium` · `g2-editorial` · `g2-editorial-counter` · `g3-institutional` · `g4-stewardship` · `g5-sprint-console` · `g6-cinematic`}. The cluster + layout-family triple selects the allowed subset per `motion-profile-catalog.md §3`.
- **Why**: implicit motion was the only DNA dimension never declared at intake (the audit's gap #2). Naming the profile makes axis 18 scorable at A.2 plan-gate, A.6 review-lock, and workflow D flip.
- **Test at A.1**: brief field filled with one of the 7 enumerated keys. Test at A.2: planner scores axis 18 vs every existing sibling (≥ 2 floor). Test at A.6: style-critic walks the per-profile anti-tacky checklist (catalog §7).
- **Failure mode**: brief blank · brief outside cluster's allowed set · profile collides with an existing sibling claim (e.g., a 3rd LF-2 occupant declaring `g2-editorial-counter` would collide with Causa's claim and trigger AC-V5 cumulative-ladder re-spec).
- **Cross-reference**: `motion-profile-dna-plan.md §4` (per-cluster allowed-set table) · `motion-profile-catalog.md §3` (planner-side lookup).

### CS-MOTION-DNA-02 [REQUIRED] · LF-2 1st-occupant claims `g2-editorial`; 2nd-occupant claims `g2-editorial-counter`
- **Rule**: LF-2 1st-occupant ALWAYS picks `g2-editorial` (zero motion-bundle flags · the static editorial signature · Cornice canonical). LF-2 2nd-occupant ALWAYS picks `g2-editorial-counter` (`kpi_animate` + `nav_condense_on_scroll` + `evid5_provenance` · the within-family differentiator · Causa canonical post-retrofit-slice-01). LF-2 3rd-occupant clears AC-V5 cumulative ladder vs both prior occupants per CS-LF2-VAR-V5.
- **Why**: this is the same AC-V1 ≥3 sub-variant floor (per `lf2-family-internal-variance-rules.md §4`) read directly off the motion_profile bundle. The two profiles are adjacent under axis-18 scoring, producing pair-score 2 (clears the within-family critical-axis-veto floor).
- **Test at A.5 build**: DNA entry's `motion_profile` value matches the occupancy slot · `MOTION_PROFILES` bundle flags propagate via body data-attributes per slice-01 contract.
- **Failure mode**: 1st-occupant ships any motion-bundle flag set to True · 2nd-occupant ships fewer than 3 flags · either occupant picks a non-LF-2 profile.
- **Cross-reference**: §19 CS-LF2-VAR-V1..V5 (the 5 LF-2 variance rules · this DNA cell carries V1's sub-variant counting at the bundle layer) · `motion-profile-dna-plan.md §3.2-§3.3` (per-profile feel + safe pool for both LF-2 profiles).

### CS-MOTION-DNA-03 [BLOCKING] · `prefers-reduced-motion: reduce` is honored at the JS root for every profile
- **Rule**: every motion-bundle flag's runtime gate sits AFTER the top-level `prefers-reduced-motion` short-circuit at `static/js/live-motion.js` line 50. Reduced-motion always wins. The static fallback per profile is enumerated in `motion-profile-dna-plan.md §6` (and `motion-profile-catalog.md §8` for the verifier).
- **Why**: WCAG accessibility floor + the `[BLOCKING]` red-line at AT-X1 (cross-profile · binding for every profile). The user's information access is preserved; the FEEL is gracefully degraded.
- **Test at workflow C/D walk**: browser-verifier walks every locale × viewport with `prefers-reduced-motion: reduce` enabled · captures static-equivalent screenshots · cross-references catalog §8 expected-behavior table.
- **Failure mode**: any motion-bundle flag drives behavior under reduced-motion · any animation re-triggers on scroll-back inside a session (AT-X4 binding).
- **Cross-reference**: `motion-profile-dna-plan.md §6` (per-profile static fallback) · `static/js/live-motion.js:50` (the runtime guarantee).

### CS-MOTION-DNA-04 [REQUIRED] · 2.0-grandfather class for shared `g3-institutional` corporate-suite trio
- **Rule**: Pragma · Fiscus · Solaria all declare `g3-institutional` with identical 1-flag bundle (`kpi_animate` only). The 3 cross-pairs (Pragma↔Fiscus · Pragma↔Solaria · Fiscus↔Solaria) score axis-18 = 0 each (identical profile + identical flag count). Per anti-clone-2.0 §3 critical-axis-veto floor 2, this is a v2.0 fail. The retrofit cost is 5-10× higher than Causa's (all three are `published_live` since pre-A.6 era). The trio is **2.0-grandfathered** under the existing CS-LAYOUT-12 in-family near-occupant § decision (filed 2026-05-03 · 2/9 layout-axis exception) extended at 2.0 ratification.
- **Why**: the audit's S6 cluster-tropes operational rule (anti-clone-2.0 §5) names "fix at cluster level · ship a non-corporate-suite cluster" as the only resolution to shared-trope sameness. Per-pair retrofit inside the cluster is uneconomic for already-shipped templates.
- **Scope of grandfather**: applies ONLY to the Pragma/Fiscus/Solaria trio. Does NOT extend to a 7th corporate-suite sibling. NO new sibling may join the grandfather class. Re-evaluation triggers: catalog ≥ 50 templates · OR Phase X.10+ batch retrofit pass · OR a new non-cs cluster ship that demonstrates the imagery + audience-verb diversification budget.
- **Cross-reference**: §19 Pragma ↔ Fiscus 2.0-grandfathered exception (sibling subclass of this rule) · `motion-profile-dna-plan.md §7` (axis-18 scoring rubric · 15 corporate-suite pair scores enumerated · 11 of 15 clear · 4 trio pairs flagged).

### How CS-MOTION-DNA-* applies at each workflow gate

| Gate | Rule(s) verified | Evidence written |
|---|---|---|
| A.0 territory-scout | likely motion_profile per cluster + family · cluster's S6-readiness check | scout report includes profile prediction + S6 status |
| A.1 intake | CS-MOTION-DNA-01 declared from cluster's allowed set + axis-18 matrix vs every existing sibling | brief field filled · matrix ≥ 2 cells per pair |
| A.2 plan | CS-MOTION-DNA-01 + critical-axis veto check | plan re-spec on any veto fail |
| A.5 build | CS-MOTION-DNA-02 LF-2 occupancy contract honored · DNA entry committed | source-file diff |
| A.6 review-lock | per-profile anti-tacky checklist (catalog §7 · all YES) | review-lock report cites profile + flag count + checklist YES count |
| Workflow C/D walk | CS-MOTION-DNA-03 reduced-motion walk · per-profile static-equivalent verified per catalog §8 | walk-log per profile · default-motion + reduced-motion screenshot pairs |
| Release-gatekeeper at flip | aggregated axis-18 score in scorecard · all 5 v2.0 critical-axis vetoes ≥ floor 2 | scorecard panel motion-profile-summary |

### Failure-mode summary

A failure of any CS-MOTION-DNA-* rule blocks tier flip. The most common at intake are:
- **F-MOTION-1**: brief outside cluster's allowed-profile set → re-route at A.1 (likely candidate is a different cluster · or the brief is mis-classified).
- **F-MOTION-2**: 2nd LF-2 occupant declares `g2-editorial` instead of `g2-editorial-counter` → AC-V1 sub-variant floor breach · re-spec at A.0/A.1.
- **F-MOTION-3**: profile collides with an existing sibling-claim (registry per `motion-profile-catalog.md §4`) → re-spec or re-route at A.1.
- **F-MOTION-4**: reduced-motion walk produces non-static fallback for any animation-bearing flag → bug · block flip until JS gate is fixed.
- **F-MOTION-5**: axis-18 score < 2 vs any sibling that is NOT in the 2.0-grandfather class → re-spec the failing axis (or pick a different profile from the cluster's allowed set).

---

## 21 · Summary

### Core design principles (seven · in priority order)

1. **Dark-foreground polarity is non-negotiable.** `--primary` is a dark text color on cream paper. Any pilot that inverts this breaks every headline on every page. This is the single most load-bearing invariant on the archetype (CS-PAL-01, CS-PAL-06, CS-PAL-04).
2. **Restraint is the aesthetic.** Editorial whitespace (100×72 section padding, 1400 max-width), serif+italic-em emphasis, accent used ≤ 2-3 times per viewport. Density kills the advisory feel (CS-TONE-02, CS-RHYTHM-01, CS-PAL-05).
3. **One dark band per home, fixed section order.** The KPI band at position 3 is the grounding beat; everything else is cream paper. Home reads hero → pillars → KPI → sectors → leadership → cases → CTA (CS-TONE-03, CS-RHYTHM-02).
4. **Typography is institutional, not display.** Humanist/transitional serif heading + neutral sans body + tabular numerics + italic-em emphasis. Geometric sans on headings is blocked (CS-TYPE-01, CS-TYPE-02, CS-TYPE-03).
5. **Voice is the firm's own voice.** First-person-plural, verifiable credentials, cluster-specific terminology, zero marketing hyperbole, voice anchor preserved verbatim across 5 locales (CS-EXEC-01 through CS-EXEC-07).
6. **The site is a firm's site, not a template.** Editor affordances hidden behind body-class guard, no placeholder strings, curated editorial imagery matched semantically to the profession (CS-MARKET-01 through CS-MARKET-07).
7. **Browser live verification has the veto.** CLI-green is a lower bound. Every blocking rule in this document was written because a passing test suite has already missed a palette-polarity bug that made every headline invisible in production-bound code (CS-BROWSER-01).

### Biggest systemic risks addressed

- **AP1 · Palette polarity inversion** (CS-PAL-01, CS-PAL-04, CS-HERO-03, CS-BROWSER-01). Solaria caught this in a 30-minute live walk that 506/506 tests missed. The design standard elevates the dark-foreground convention from a code comment to a blocking rule with an L\* threshold and a browser verification gate.
- **AP2 · Zero responsive coverage** (CS-RESPONSIVE-01 through CS-RESPONSIVE-08, CS-HERO-07, CS-NAV-05, CS-FOOT-05). The entire §14 exists because the skin ships with 1 real breakpoint across 7 files. Every rule in that section is the target state the hardening pass must achieve before the next pilot ships LIVE.
- **AP3 / AP4 / AP5 / AP6 · Imagery pitfalls** (CS-HERO-02, CS-COMP-02, CS-COMP-03 · detail in the imagery standard). Cluster-mismatched photos and generic stock fallbacks are invisible to tests but central to the premium feel.
- **AP8 · Tests pass ≠ ship-ready** (CS-BROWSER-01 through CS-BROWSER-03). The ship gate is tests + browser, not tests alone. This is encoded as a blocking rule at the design-standard level, not just a cultural preference.
- **AP9 · Coaching-cluster and cluster-generic clichés** (CS-EXEC-04, CS-EXEC-07). Marketing hyperbole and funnel-pattern sections are named explicitly and banned at the rule level.
- **AP10 · Palette differentiation drift** (CS-PAL-02, CS-EXEC-02). D-054 is codified as "secondary+accent is the D-054 vector" with an explicit triangulation rule — siblings diff against every other sibling, not just one.
- **AP11 · Dark-section child text** (CS-PAL-04). Scoped variant of AP1; the blocking rule now covers it.

### What is still missing for full factory-grade readiness

This document codifies the DESIGN standard. Full factory-grade readiness requires the siblings (currently empty):

1. **`corporate-suite-blocking-rules.md`** — the enforcement recipes matching each `[BLOCKING]` tag here with a detection command and a prevention command.
2. **`corporate-suite-browser-rubric.md`** — the Playwright MCP walk script implementing CS-BROWSER-01: navigate × resize × snapshot × contrast-check × focus-walk across 3 templates × 5 locales × 7 viewports, plus the output report format.
3. **`corporate-suite-imagery-standard.md`** — the imagery-pack format, curator protocol binding, per-cluster semantic examples, and the `business-corporate` retro-pack plan for Pragma (AP3).
4. **`corporate-suite-multi-agent-sop.md`** — the orchestration between template-planner, template-builder, style-critic, contrast-accessibility-auditor, responsive-auditor, imagery-curator, browser-verifier, release-gatekeeper for a single pilot end-to-end.
5. **`corporate-suite-quality-scorecard.md`** — the numeric scorecard the release-gatekeeper fills in (rule-by-rule pass/fail), becoming the shipping artifact attached to every tier flip.
6. **Agent prompts** — all 10 files under `factory/agents/` are empty today. Highest priority: `browser-verifier` (implements CS-BROWSER-01), `contrast-accessibility-auditor` (implements CS-PAL-01, CS-PAL-04, CS-HERO-03), `responsive-auditor` (implements §14), `style-critic` (implements §1-12 spot-checks on PR diffs), `release-gatekeeper` (fills the scorecard).
7. **Code/skin changes** (out of scope for Step 0 and this document; tracked for a later step):
   - Add `@media (max-width: 1100px)` + `@media (max-width: 720px)` to `_base.html` and the 6 page files (smallest fix for AP2 · fixes Pragma + Fiscus + Solaria at once).
   - Drop or derive `--primary-2` (AP7 cleanup).
   - Audit and extend `prefers-reduced-motion` coverage to `[data-lm]` paths (AP12).
   - Retro-curate `business-corporate` Pexels pack for Pragma (AP3 cleanup).
   - Optional: palette validator (pre-commit check against CS-PAL-01) — the automated counterpart of the browser walk.
8. **Solaria Commit B** — explicitly paused per user instruction; un-pause only after (1)–(7) above are sufficient to guarantee the next pilot inherits a sturdier skin than Solaria did.

Until those gaps close, this design standard is the authoritative reference for every agent planning, building, editing, or reviewing a corporate-suite template, and the `[BLOCKING]` rules here define the floor for merge and LIVE flip.
