# Pattern Library · `corporate-suite` archetype

**Audit baseline**: 2026-04-21 · **Refined**: 2026-04-22
**Source**: repo evidence from Pragma (LIVE), Fiscus (LIVE post-merge), Solaria (local draft).

Each pattern lists: **evidence** (file:line), **why it works**, **how to reuse**, the **standards anchor** (the `CS-*` / `BRWS-*` rule it codifies in `factory/standards/*.md`), the **agent(s)** that consume it, and a **reusability tag** (REUSABLE-NOW · REUSABLE-AFTER-HARDENING · LOCAL-ONLY · ANTI-PATTERN).

The legacy `[G] / [A] / [I]` letter tags are kept for back-reference but the unified severity model `[BLOCKING] / [REQUIRED] / [STRONG] / [GUIDELINE]` from the standards is now the source of truth. Every pattern below maps to a tagged rule (or, in two cases, is informational with no enforcement).

---

## 0 · How to use this document

1. Patterns are evidence-anchored facts about what is already in the repo. Standards rules in `factory/standards/*.md` are derived from them.
2. **REUSABLE-NOW** = a downstream agent may consume the pattern as-is. **REUSABLE-AFTER-HARDENING** = the pattern is sound but the supporting code/skin still has a known gap (AP1 enforceability, AP2 breakpoints, AP3 retro-pack, AP7 token decoupling, AP12 motion JS) that must close before the pattern is fully realized.
3. The **Used by** column names the agents from `corporate-suite-multi-agent-sop.md` §2 that consume each pattern. When a pattern shows up as a `[BLOCKING]` standard rule, the cited agent enforces it; when it's a positive example, the cited agent uses it as a reference.
4. Pair with `factory/references/anti-pattern-library.md` (failure modes), `factory/references/template-inventory.md` (what exists today), and the standards it codifies.

---

## A · Architecture / file layout

### A1 [G · REUSABLE-NOW] Per-template content files named `template_content_{name}[_{locale}].py`
- **Evidence**: `apps/catalog/template_content_pragma.py`, `..._fiscus.py`, `..._fiscus_en.py` (5-file locale tree).
- **Why it works**: keeps the IT author and each locale author in a dedicated file; shape-parity is verifiable by diff.
- **Reuse**: each new template = 5 files (1 IT + 4 locales). Default locale `_it` exports `CONTENT_IT`; each locale exports `CONTENT_<LOCALE>` with identical shape.
- **Standards anchor**: `CS-EXEC-01` (voice anchor verbatim across 5 locales) · `CS-BLOCK-11` / `O11` enforces it on the rendered DOM.
- **Used by**: `copy-translation-agent` (writes the 5 files) · `release-gatekeeper` (cites the file count in the scorecard's locale-walked field).

### A2 [G · REUSABLE-NOW] DNA record keyed by template slug in `apps/catalog/template_dna.py`
- **Evidence**: `template_dna.py:972` (`pragma-corporate-suite`), `template_dna.py:1318` (`fiscus-commercialista`).
- **Why it works**: single dict per template enumerates archetype, hero style, navbar style, footer style, section order, card style, button style, density, tone, imagery direction, imagery pool key, conversion pattern, font pairing — everything non-content reviewers need for D-054 differentiation.
- **Reuse**: copy the Fiscus block, change `imagery_key`, `conversion_pattern`, `tone`, `imagery_direction`, and the inlined `content` sample used by the tile preview.
- **Standards anchor**: `CS-EXEC-02` (D-054 10-gate triangulation against every sibling) · `CS-BLOCK-12` / `O12` enforces.
- **Used by**: `template-builder` (writes the new DNA row · SOP §3.4) · `template-planner` (reads sibling DNA rows for `d-054-triangulation.md` · SOP §3.1).

### A3 [G · REUSABLE-NOW] Scoped `cs-` CSS class prefix keeps the archetype isolated
- **Evidence**: `templates/live_templates/business/corporate-suite/_base.html` — every component class starts with `cs-` (`cs-nav`, `cs-hero`, `cs-lead`, `cs-pillars`, …).
- **Why it works**: zero bleed between archetype skins; search-replacing a `cs-` class refactors one archetype only.
- **Reuse**: when forking this skin for a new archetype, rename the prefix globally (`cs-` → `ae-`, etc.) before content authoring.
- **Standards anchor**: `CS-COMP-07` (scoped `cs-` class prefix · `[BLOCKING]`).
- **Used by**: `style-critic` (BRWS-RHYTHM-* spot-checks rely on `.cs-section`, `.cs-kpi-band`, `.cs-nav` selectors) · `contrast-accessibility-auditor` (BRWS-CONTRAST-02 sweeps `.cs-section.dark`, `.cs-kpi-band`, `.cs-nav`, `.cs-foot`).

### A4 [G · REUSABLE-NOW] Preview imagery pool per template, 6-slot shape `[hero, feature, portrait, portrait, detail, ambient]`
- **Evidence**: `apps/catalog/preview_imagery.py` — `business-corporate` (l.312), `business-fiscal` (l.346), `business-coaching` (l.370 on branch).
- **Why it works**: uniform slot shape means one preview composition can swap pools without re-layout. Prevents "hero-style shot in position 5" mismatches.
- **Reuse**: curator produces a 6-URL pack matching the slot convention; copy author wires it via the pool key.
- **Standards anchor**: `CS-IMG-POOL-01` (`[BLOCKING]`) · `CS-IMG-POOL-02` (page-by-page distribution) · `CS-IMG-POOL-03` (pool key prefix `business-`).
- **Used by**: `imagery-curator` (writes 6 slots in CS-IMG-POOL-01 order · SOP §3.2) · `template-builder` (writes the pool block to `preview_imagery.py` · SOP §3.4) · `browser-verifier` (BRWS-IMG-02 confirms the live render uses slot 0 as the hero).

### A5 [G · REUSABLE-NOW] Editor preview mode guards in the skin
- **Evidence**: `_base.html:441-452` — `body.mw-is-editor-preview { ... }` hides marketplace bar and adds overflow guards for long user-edited titles.
- **Why it works**: the same skin renders both in the public `/templates/.../live/` route and the in-editor iframe; no duplicated HTML.
- **Reuse**: new archetypes inherit this by mimicking the exact body-class guard.
- **Standards anchor**: `CS-MARKET-01` (editor affordances gated by body class · `[BLOCKING]`) · `CS-BLOCK-08` / `O8` enforces.
- **Used by**: `browser-verifier` (BRWS-FEEL-02 loads the public `/live/` URL in an incognito session and confirms `body` does NOT carry `mw-is-editor-preview` and zero edit halos render).

### A6 [A · REUSABLE-NOW] Tier gated by `TEMPLATE_REGISTRY.json` · applied via `sync_template_tiers`
- **Evidence**: Fiscus commit `65c6dd6` flipped `draft` → `published_live` via the JSON + sync.
- **Why acceptable**: decouples content authoring (Commit A) from go-live flip (Commit B). Mirrors the D-102 2-commit cadence.
- **Reuse**: Commit A sets tier `draft`; Commit B flips to `published_live` only after the reviewer walk passes.
- **Standards anchor**: now formalized in `corporate-suite-multi-agent-sop.md` §1.3 and `corporate-suite-blocking-rules.md` §2.2 (severity model two-axis decision · merge vs LIVE-flip).
- **Used by**: `template-builder` (sets `draft` at Commit A · SOP §3.4) · `release-gatekeeper` (flips to `published_live` at Commit B, **only after user parallel-verification handshake** · SOP §3.10 / §5.4).

---

## B · Design tokens · palette · typography

### B1 [G · REUSABLE-NOW] Three-token brand palette → skin CSS custom properties
- **Evidence**: `_base.html:19-21` — `--primary: {{ theme.primary }}; --secondary: {{ theme.secondary }}; --accent: {{ theme.accent }};`
- **Why it works**: every template swaps identity via 3 hex values. Rest of the skin derives fills, rules, and text color from these.
- **Reuse**: every new template on this skin must provide exactly these 3 tokens in `SEED_TEMPLATES[...]["brand"]["palette"]`.
- **Standards anchor**: `CS-PAL-03` (three tokens only — no hardcoded fourth color · `[REQUIRED]`).
- **Caveat**: AP7 — `_base.html:20` hardcodes `--primary-2: #2c3e6b` violating CS-PAL-03 in spirit. Tracked as `[STRONG]` archetype debt.
- **Used by**: `template-planner` (palette spec in `brief.md` · SOP §3.1) · `template-builder` (writes the seed row · SOP §3.4).

### B2 [G · REUSABLE-NOW · LOAD-BEARING] **Dark foreground convention** — `--primary` IS the text color
- **Evidence**: `_base.html:87` — `h1..h5 { color: var(--primary); }`. Pragma `#1E293B`, Fiscus `#1F2937`, Solaria post-fix `#2B2A28`. All three dark.
- **Why it works**: matching nav background (`.cs-nav { background: var(--primary) }`, `_base.html:130`) automatically contrasts against the cream paper body. The pattern is load-bearing.
- **Reuse**: every new palette on this archetype MUST choose a dark hex (L\* ≤ 40 on cream) for `primary`. The accent may be warm/cool; the secondary is a bridge.
- **Standards anchor**: `CS-PAL-01` (`primary` L\* ≤ 40 on cream · `[BLOCKING]`) · `CS-PAL-06` (navbar bg = `--primary` · `[BLOCKING]`) · `CS-HERO-03` (hero h1 AAA target · `[BLOCKING]`) · `CS-BLOCK-01` / `O1` enforces.
- **Validation**: cross-reference palette primary with the repo convention before seeding. See AP1 for what happens otherwise. **Today's enforcement** = Builder L\* self-check (refuses to advance past `draft` when L\* > 40 · SOP §3.4) + browser walk hard-veto (`contrast-accessibility-auditor` SOP §3.6). A pre-commit palette validator is a **REUSABLE-AFTER-HARDENING** complement (still pending).
- **Used by**: `template-planner` (palette spec includes the L\* number · SOP §3.1) · `template-builder` (computes and reports L\* in `build-report.md` · SOP §3.4) · `contrast-accessibility-auditor` (hard-veto authority for O1 · SOP §3.6) · `browser-verifier` (BRWS-CONTRAST-01 measures every h1..h5 distance + ratio).

### B3 [G · REUSABLE-NOW] Serif heading + sans body · humanist/transitional pairing
- **Evidence**: Pragma = Merriweather + Inter, Fiscus = IBM Plex Serif + IBM Plex Sans, Solaria = Fraunces + Inter.
- **Why it works**: institutional weight on headlines + neutral sans body matches the advisory/boardroom voice the archetype is built for.
- **Reuse**: new templates on this skin pick a serif-sans pair from the humanist/transitional/slab families. Geometric sans on headings breaks the identity.
- **Standards anchor**: `CS-TYPE-01` (serif heading + sans body · humanist/transitional pairing · `[BLOCKING]`) · `CS-BLOCK-VI-01` enforces.
- **Used by**: `template-planner` (typography stack in `brief.md`) · `style-critic` (BRWS-RHYTHM-05 / D7 dimension) · `browser-verifier` (computed `font-family` snippet rejects Montserrat/Poppins/Raleway/Gotham/Futura/Century Gothic on headings).

### B4 [G · REUSABLE-NOW] Italic `<em>` in serif headings = boardroom emphasis
- **Evidence**: `_base.html:91` — `h1 em, h2 em, h3 em { font-style: italic; ... color: var(--primary); }`.
- **Why it works**: italic serif inside a sober serif headline gives "emphasis by restraint" — classic editorial.
- **Reuse**: voice authors wrap the one load-bearing word per headline in `<em>…</em>` (e.g., "L'adempimento <em>corretto</em>, non la trovata").
- **Standards anchor**: `CS-TYPE-02` (italic `<em>` is the heading emphasis · `[REQUIRED]`) · `CS-RHYTHM-05` (section titles use the italic-em restraint pattern).
- **Used by**: `copy-translation-agent` (wraps the one load-bearing word per headline in 5 locale files) · `style-critic` (D2 elegance dimension · BRWS-HERO-05 / BRWS-RHYTHM-05).

### B5 [G · REUSABLE-NOW] Tabular numerals for KPI strip
- **Evidence**: `_base.html:93-98` — `font-variant-numeric: tabular-nums;` on `.cs-kpi-band .stat .num`.
- **Why it works**: keeps "180+", "94%", "€ 1.4 B" vertically aligned across locales.
- **Reuse**: any KPI-ish figure on this skin inherits via `.num` class.
- **Standards anchor**: `CS-TYPE-03` (tabular numerals on every KPI figure · `[BLOCKING]`) · `CS-BLOCK-VI-02` enforces.
- **Used by**: `style-critic` (D7 typography hierarchy) · `browser-verifier` (BRWS-READ-05 confirms `.cs-kpi-band .num` computed `fontVariantNumeric` contains `tabular-nums`).

---

## C · Layout · composition

### C1 [G · REUSABLE-NOW] 55/45 hero split — serif drama LEFT + photo-led RIGHT
- **Evidence**: `home.html:5-67` — `grid-template-columns: 1.3fr 1fr`; left=eyebrow+h1+sub+meta-strip, right=full-bleed hero image with credit overlay.
- **Why it works**: serif headline carries identity above the fold while a single premium photo carries mood. No stock-collage feel.
- **Reuse**: one hero photo drawn from pool slot 0 (hero). Credit overlay labels it so the image reads as editorial, not stock.
- **Standards anchor**: `CS-HERO-01` (`[BLOCKING]`) · `CS-HERO-02` (editorial hero photo from curated pack · `[BLOCKING]`) · `CS-IMG-HERO-01..08` · `CS-IMG-HERO-08` (credit overlay labels image as editorial · `[REQUIRED]`).
- **Reusability caveat**: the 55/45 split is **REUSABLE-AFTER-HARDENING** for mobile — `CS-HERO-07` requires the split to collapse to a single column at ≤ 720 px, but the skin currently lacks that breakpoint (AP2). New pilots inherit the desktop split now and the mobile collapse once the responsive pass lands.
- **Used by**: `imagery-curator` (slot 0 selection + credit overlay feasibility · CS-IMG-HERO-01) · `style-critic` (D1 premium feel) · `browser-verifier` (BRWS-HERO-01..06).

### C2 [G · REUSABLE-NOW] Airy density · max-width 1400 · padding 72px horizontal · 96–100px vertical
- **Evidence**: `_base.html:171, 225`; home.html sections all `padding: 100px 72px; max-width: 1400px; margin: 0 auto;`.
- **Why it works**: institutional-advisory tone demands negative space. Every section breathes.
- **Reuse**: every section wrapper on this skin inherits these values. Non-negotiable for the editorial cadence.
- **Standards anchor**: `CS-RHYTHM-01` (section wrapper `100px 72px` · max-width 1400 · `[BLOCKING]`) · `CS-TONE-02` (restraint over density · `[BLOCKING]`) · `CS-BLOCK-VI-04` enforces.
- **Reusability caveat**: **REUSABLE-AFTER-HARDENING** for tablet/mobile. `CS-RESPONSIVE-01` requires `72px 48px` at 1100 and `56px 24px` at 720; the skin currently has none of these.
- **Used by**: `style-critic` (D8 spacing rhythm) · `responsive-auditor` (BRWS-RHYTHM-01 measurement at every viewport).

### C3 [G · REUSABLE-NOW] Dark navy KPI band on institutional cream body
- **Evidence**: `home.html:91-122` — `.cs-kpi-band { background: var(--primary); color: var(--on-dark); }` with rule-separated stat cells.
- **Why it works**: the one dark band on the page grounds the advisory voice.
- **Reuse**: place once per home, re-used on case_study_detail as `.cs-post .kpi-band`.
- **Standards anchor**: `CS-TONE-03` (one dark band per home · `[REQUIRED]`) · `CS-RHYTHM-03` (KPI band at position 3) · `CS-PAL-04` (dark-section child text uses `--on-dark*` variants · `[BLOCKING]`) · `CS-BLOCK-17` / `O17` enforces.
- **Used by**: `style-critic` (D8 spacing rhythm · BRWS-RHYTHM-03) · `contrast-accessibility-auditor` (BRWS-CONTRAST-02 sweeps every text descendant · D12).

### C4 [G · REUSABLE-NOW] Sectors ribbon + trust band — anonymized client proof
- **Evidence**: `home.html:125-157` (`.cs-sectors`, `.cs-trust`).
- **Why it works**: commercialisti can't show client logos (secreto professionale). This pattern gives a trust surface without violating it.
- **Reuse**: text-only ribbon + logo marquee — no real logos needed.
- **Standards anchor**: `CS-COMP-01` (anonymized proof · text ribbon + association marquee · `[REQUIRED]`) · `CS-IMG-SEC-04` (sectors ribbon text-led · trust marquee = industry-association marks only).
- **Used by**: `copy-translation-agent` (composes the sector chip text per cluster) · `imagery-curator` (selects industry-association marks, not client logos · CS-IMG-COH-04).

---

## D · Internationalization · RTL

### D1 [G · REUSABLE-NOW] Font-family swap on `html[dir="rtl"]`
- **Evidence**: `_base.html:309-312` — Noto Kufi Arabic (heading) + Amiri (body) mapped to `--heading` and `--body`.
- **Why it works**: Latin fonts render Arabic as square glyphs; swap via CSS var keeps the rest of the skin untouched.
- **Reuse**: every archetype that supports AR inherits this block verbatim.
- **Standards anchor**: `CS-TYPE-06` (Arabic Kufi+Amiri swap under RTL · `[BLOCKING]`) · `CS-BLOCK-VI-03` (Arabic glyphs render as squares = font-swap failure).
- **Used by**: `browser-verifier` (BRWS-READ-04 confirms AR locale headings are not square glyphs).

### D2 [G · REUSABLE-NOW] Latin wordmark + Latin numerics preserved in RTL
- **Evidence**: `_base.html:371-387` — `.cs-nav .wm`, `.cs-foot .brand .word`, and every `.num` class forced back to the Latin heading font under `dir="rtl"` with `unicode-bidi: isolate`.
- **Why it works**: brand name readability + KPI legibility do not degrade under Arabic body text.
- **Reuse**: any new chrome element that mixes Latin numerics into AR inherits via the same rule list.
- **Standards anchor**: `CS-NAV-06` (Latin wordmark under RTL · `[REQUIRED]`) · `CS-FOOT-03` (Latin wordmark + .num in RTL footer).
- **Used by**: `browser-verifier` (BRWS-FOOT-04 confirms AR footer wordmark + .num computed `font-family` resolves Latin).

### D3 [G · REUSABLE-NOW] RTL page-level grid flips guarded by `{% if is_rtl %}`
- **Evidence**: `_base.html:388-432` — whole page-level section grid flips only emitted for the AR render.
- **Why it works**: LTR visitors don't pay the CSS byte cost; AR visitors get the correct grid polarity.
- **Reuse**: flip rules live inside one `{% if is_rtl %}…{% endif %}` block; add new flips there.
- **Standards anchor**: `CS-RESPONSIVE-08` (RTL layouts tested at all three viewport classes · `[STRONG]`).
- **Used by**: `responsive-auditor` (BRWS-RESP-07 tests RTL at desktop + tablet + mobile) · `browser-verifier` (BRWS-ALIGN-05 confirms text-align and flex-direction flip).

### D4 [G · REUSABLE-NOW] Letter-spacing flatten on chrome labels for Arabic
- **Evidence**: `_base.html:337-369` — every class that uses Latin tracking (`letter-spacing: 0.22em`, etc.) is reset to `0` under `dir="rtl"`.
- **Why it works**: Arabic uppercase tracking destroys legibility.
- **Reuse**: when adding new uppercase-tracked labels, add them to the reset list.
- **Standards anchor**: `CS-TYPE-05` (letter-spacing — restraint-tracked · `[REQUIRED]`).
- **Used by**: `browser-verifier` (BRWS-READ-04 confirms 0.22em tracking resets to 0 under RTL).

### D5 [G · REUSABLE-NOW] Locale switcher pill with current-state + `lang` + `dir` on each link
- **Evidence**: `_base.html:461-480` — locale switcher renders `<a lang="ar" dir="rtl">` per entry.
- **Why it works**: search engines + assistive tech get correct per-link language metadata.
- **Standards anchor**: `CS-NAV-03` (locale switcher pill · lang+dir per link · `[REQUIRED]`).
- **Used by**: `browser-verifier` (BRWS-NAV-03 confirms `<a>` inside the locale switcher carries `lang` + `dir`).

---

## E · Accessibility · motion

### E1 [G · REUSABLE-NOW] Focus-visible outline in gold accent · NOT browser default
- **Evidence**: `_base.html:212-220` — `outline: 2px solid var(--accent); outline-offset: 4px;` on every interactive element (buttons, nav links, language pills, case rows).
- **Why it works**: keyboard visibility without the blue halo that clashes with institutional palette.
- **Reuse**: new interactive elements on this skin opt in via the same `:focus-visible` cascade.
- **Standards anchor**: `CS-NAV-02` (4 nav-link states distinct and visible · `[BLOCKING]`) · `CS-RESPONSIVE-07` (focus-visible survives all viewports · `[REQUIRED]`) · `CS-BLOCK-N-04` enforces (browser-default blue = block).
- **Used by**: `contrast-accessibility-auditor` (Tab-walk first 12 focusables per page · BRWS-CONTRAST-04) · `responsive-auditor` (BRWS-RESP-06 confirms focus outline survives 390 px).

### E2 [G · REUSABLE-AFTER-HARDENING] `prefers-reduced-motion: reduce` disables button animation
- **Evidence**: `_base.html:299-301` — button `transition: none` under reduced motion.
- **Why it works**: WCAG 2.3.3 compliance. Motion-sensitive visitors aren't punished.
- **Reuse**: any new motion on this skin must be disabled under the same media query.
- **Standards anchor**: `CS-RESPONSIVE-07` · `BRWS-FEEL-08` (`[STRONG]`).
- **Caveat**: AP12 — `[data-lm]` reveal animations driven by `static/js/live-motion.js` are unverified. Pattern is **REUSABLE-AFTER-HARDENING** until the JS path is confirmed to honor the same media query.
- **Used by**: `browser-verifier` (BRWS-FEEL-08 emulates reduced-motion + reloads home + confirms no entrance animations fire).

### E3 [A · REUSABLE-NOW] Logo marquee with sober institutional drift (110s duration)
- **Evidence**: `_base.html:74-78` — `--lm-marquee-duration: 110s`, slower than shared default.
- **Why acceptable**: institutional voice benefits from a very slow drift. Fast marquees read as consumer-tech.
- **Standards anchor**: noted as `[STRONG]` drift in design-standard §17 non-blocking examples (a marquee duration of 60s instead of 110s "feels consumer-tech, not advisory").
- **Used by**: `style-critic` (informational only; logged as `§ deviation` if a sibling pilot diverges with justification).

---

## F · Content · voice

### F1 [G · REUSABLE-NOW] D-054 10-gate differentiation documented in module docstring
- **Evidence**: Pragma docstring (lines 12-32), Fiscus docstring (lines 14-40), Solaria docstring (on branch).
- **Why it works**: reviewers can read a single file header and verify that this template differs from every sibling on the same archetype across 10 dimensions.
- **Reuse**: every new template's `template_content_{name}.py` must open with this 10-gate block.
- **Standards anchor**: `CS-EXEC-02` (`[BLOCKING]`) · `CS-BLOCK-12` / `O12` enforces.
- **Reusability caveat**: the **template** is REUSABLE-NOW, but Pragma's docstring triangulates against Elevate (different archetype) and Fiscus's docstring triangulates against Pragma only. With three siblings now extant, both should be refreshed on next touch — see **systemic issue #6** in `template-inventory.md` §7. New pilots author against ALL three siblings via `template-planner`'s `d-054-triangulation.md`.
- **Used by**: `template-planner` (writes `factory/reports/plans/<slug>/d-054-triangulation.md`) · `copy-translation-agent` (mirrors the table into the IT module docstring) · `release-gatekeeper` (Layer 1 override O12 fails the scorecard if absent).

### F2 [G · REUSABLE-NOW] Voice anchor line preserved verbatim across all 5 locales
- **Evidence**: Pragma "Dove si prendono le decisioni che contano" → translated but identifiable in each locale file. Fiscus "L'adempimento corretto, non la trovata" → idem.
- **Why it works**: the anchor is the brand's mission statement; keeping it intact preserves identity across languages.
- **Reuse**: blueprint §5 of each cluster provides the anchor; copy authors MUST NOT paraphrase it.
- **Standards anchor**: `CS-EXEC-01` (`[BLOCKING]`) · `CS-BLOCK-11` / `O11` enforces.
- **Used by**: `template-planner` (records the anchor verbatim in `brief.md` §1) · `copy-translation-agent` (preserves verbatim across 5 locale files) · `browser-verifier` (BRWS-FEEL-05 greps each rendered locale page) · `release-gatekeeper` (O11).

### F3 [G · REUSABLE-NOW] Anti-pattern guardrails copied from blueprint into the module docstring
- **Evidence**: Solaria docstring lines 22-34 — explicit list of banned phrases ("Sblocca il potenziale", "Trasforma la vita", "Einstein quotes", …) lifted from `cluster_blueprints/coaching.md` §13.
- **Why it works**: the author and reviewer share the list of failure modes in the file itself, not behind a URL.
- **Reuse**: every new template's docstring repeats its cluster's §13 anti-patterns inline.
- **Standards anchor**: `CS-EXEC-04` (no marketing hyperbole · `[REQUIRED]`) · `CS-BLOCK-P-05` enforces (banned phrase grep on rendered content).
- **Used by**: `copy-translation-agent` (mirrors the anti-pattern list into the IT module docstring) · `style-critic` (BRWS-FEEL-04 banned-phrase grep across 5 locales).

### F4 [G · REUSABLE-NOW] Licensure/credential vocabulary anchors trust
- **Evidence**: Fiscus = ODCEC Milano, sezione A, Revisore Legale reg. n., LL.M. Bocconi, Cassazionista. Pragma = CONSOB Albo n.
- **Why it works**: boardroom readers look for verifiable licensure. Invented or vague credentials break trust instantly.
- **Reuse**: blueprint §4 terminology dictionary for each cluster; copy author picks 2-3 verifiable anchors per `leadership` entry.
- **Standards anchor**: `CS-EXEC-03` (credentials are verifiable and cluster-specific · `[BLOCKING]`) · `CS-HERO-06` (meta-strip carries credential anchors · `[REQUIRED]`) · `CS-BLOCK-10` / `O10` enforces (fake certifications block).
- **Used by**: `copy-translation-agent` (cites cluster blueprint §4 vocabulary) · `style-critic` (BRWS-FEEL-06 reads each leadership credentials line and rejects fakes) · `imagery-curator` (CS-IMG-COH-03 cross-checks portrait set against credentials).

---

## G · Imagery · curation protocol (X.3 C3 · binding)

### G1 [G · REUSABLE-NOW for new pilots / REUSABLE-AFTER-HARDENING for Pragma] Pexels-only for new templates · per-cluster curator pack
- **Evidence**: `docs/content-factory/imagery/CURATION_PROTOCOL.md` §2 — Pexels primary. `packs/financial-services.md` (Fiscus), `packs/coaching.md` (Solaria).
- **Why it works**: CC0-compatible license, curator audit trail, photo-ID dedup across all clusters.
- **Reuse**: every new pilot starts with an imagery pack reviewed and approved BEFORE copy authoring begins. No pack = no author.
- **Standards anchor**: `CS-IMG-SRC-01` (Pexels-only for new templates · `[BLOCKING]`) · `CS-IMG-SRC-05` (curator ≠ reviewer · `[REQUIRED]`) · `CS-BLOCK-07` / `O7` enforces.
- **Reusability caveat**: Pragma's `business-corporate` pool is **ANTI-PATTERN** AP3 (legacy Unsplash). Single grandfathered exception in the standards (`CS-IMG-SRC-01` legacy paragraph). Closes when the `business-corporate` Pexels retro-pack lands — see `template-inventory.md` §7 issue #3.
- **Used by**: `imagery-curator` (writes the pack and the pool selection · SOP §3.2) · `imagery-curator` (reviewer pass with `role: reviewer` · CS-IMG-SRC-05) · `release-gatekeeper` (Layer 1 override O7).

### G2 [G · REUSABLE-NOW] One URL = one cluster · zero cross-cluster reuse
- **Evidence**: `preview_imagery.py` comments lines 337-345, 361-368 — "zero URL overlap with business-fiscal or business-corporate".
- **Why it works**: Session 38 caught a portfolio-photographer pool reusing restaurant-fine URLs. Fix was swapping all 6 URLs.
- **Reuse**: curator greps each candidate URL across `imagery/packs/*.md` before adding. `scripts/check_imagery_pack.py` automates.
- **Standards anchor**: `CS-IMG-SRC-04` (`[BLOCKING]`) · `CS-BLOCK-I-02` enforces.
- **Used by**: `imagery-curator` (runs the dedup grep and reports the result in `curator-report.md` · SOP §3.2) · CI script `scripts/check_imagery_pack.py`.

### G3 [G · REUSABLE-NOW] Resolution floor: hero ≥ 1600×900, portraits ≥ 800×800
- **Evidence**: `imagery/blacklist.md` §4 and `imagery/CURATION_PROTOCOL.md` §3.2.
- **Reuse**: curator verifies Content-Type and dimensions during discovery, not after the fact.
- **Standards anchor**: `CS-IMG-PREM-02` (resolution floor per slot · `[BLOCKING]`) · `CS-IMG-SRC-02` (URL format with `auto=compress&cs=tinysrgb&w=<budget>` · `[BLOCKING]`) · `CS-BLOCK-IQ-01` enforces.
- **Used by**: `imagery-curator` (records resolution per URL in the pack · CS-IMG-SRC-03) · `browser-verifier` (BRWS-IMG-01 + BRWS-RESP-04 + measurement of `img.naturalWidth × img.naturalHeight`).

---

## H · Testing discipline · what the repo CAN catch (and what it can't)

### H1 [G · REUSABLE-NOW] 5-locale lifecycle test + shape-parity test on every template
- **Evidence**: Fiscus commit `65c6dd6` test delta — facet-count shape, RTL count, tier-filter count all updated alongside the flip.
- **Why it works**: catches registry drift (wrong locale count, wrong tier, missing RTL).
- **Reuse**: every new template flip comes with the 5-6 small test deltas (listing/facet/rtl/tier counts + session_closed).
- **Standards anchor**: this is the CI floor that every agent in the SOP treats as a precondition (SOP §3.4 / §3.8 / §3.9). It is necessary but never sufficient (see H2 below).
- **Used by**: `template-builder` (CI floor part of `build-report.md` · SOP §3.4) · `browser-verifier` (refuses to walk if CI floor is red · SOP §3.8 mandatory preconditions).

### H2 [I · INFORMATIONAL · REUSABLE-NOW as evidence for the central premise] `manage.py test` CANNOT catch contrast, responsive, or imagery-semantic issues
- **Evidence**: Solaria commit `6b70d56` body — "Tests before/after: 506/506. **Live browser verification pending**."
- **Implication**: CLI green is a lower bound, not a ship signal. See AP1 / AP8 for the Solaria palette-polarity bug that passed tests but failed browser.
- **Pattern**: the reviewer walk is the only gate that catches these three failure modes.
- **Standards anchor**: this informational pattern IS the central premise codified in `corporate-suite-design-standard.md` §15 (CS-BROWSER-01..03), `corporate-suite-blocking-rules.md` §1.3 + §20, `corporate-suite-browser-rubric.md` §2, `corporate-suite-quality-scorecard.md` §1.1, and `corporate-suite-multi-agent-sop.md` §1.1.
- **Used by**: every agent in the pipeline. It is the reason `browser-verifier` exists, the reason the rubric is `[BLOCKING]` end-to-end, and the reason CS-BLOCK-18 / O18 fires automatic FAIL on a test-only ship.

---

## Appendix · Pattern → standards-rule cross-reference (fast lookup)

This appendix is the round-trip from a repo pattern to the rule that codifies it. Useful for an agent that wants to know "if I see pattern X in the diff, which rule am I enforcing?"

| Pattern | Standards rule(s) | Enforced by agent |
|---|---|---|
| A1 5-locale tree | CS-EXEC-01 / CS-BLOCK-11 / O11 | copy-translation-agent · browser-verifier |
| A2 DNA per slug | CS-EXEC-02 / CS-BLOCK-12 / O12 | template-planner · template-builder · release-gatekeeper |
| A3 `cs-` prefix | CS-COMP-07 | style-critic · contrast-accessibility-auditor |
| A4 6-slot pool | CS-IMG-POOL-01..03 | imagery-curator · template-builder · browser-verifier |
| A5 editor preview guard | CS-MARKET-01 / CS-BLOCK-08 / O8 | browser-verifier |
| A6 tier discipline | SOP §1.3, §3.10 / scorecard §6.2 | template-builder · release-gatekeeper |
| B1 3-token palette | CS-PAL-03 | template-planner · template-builder |
| B2 dark `--primary` | CS-PAL-01 / CS-PAL-06 / CS-PAL-04 / CS-HERO-03 / CS-BLOCK-01 / O1 | template-builder (L\* self-check) · contrast-accessibility-auditor (hard veto) · browser-verifier |
| B3 serif+sans pairing | CS-TYPE-01 / CS-BLOCK-VI-01 | style-critic · browser-verifier |
| B4 italic `<em>` | CS-TYPE-02 / CS-RHYTHM-05 | copy-translation-agent · style-critic |
| B5 tabular nums | CS-TYPE-03 / CS-BLOCK-VI-02 | style-critic · browser-verifier |
| C1 55/45 hero split | CS-HERO-01..02 / CS-IMG-HERO-01..08 | imagery-curator · style-critic · browser-verifier |
| C2 100×72 padding | CS-RHYTHM-01 / CS-TONE-02 / CS-BLOCK-VI-04 | style-critic · responsive-auditor |
| C3 dark KPI band | CS-TONE-03 / CS-RHYTHM-03 / CS-PAL-04 / CS-BLOCK-17 / O17 | style-critic · contrast-accessibility-auditor |
| C4 sectors+trust | CS-COMP-01 / CS-IMG-SEC-04 | copy-translation-agent · imagery-curator |
| D1 RTL font swap | CS-TYPE-06 / CS-BLOCK-VI-03 | browser-verifier |
| D2 Latin wordmark | CS-NAV-06 / CS-FOOT-03 | browser-verifier |
| D3 RTL grid flips | CS-RESPONSIVE-08 | responsive-auditor · browser-verifier |
| D4 letter-spacing flatten | CS-TYPE-05 | browser-verifier |
| D5 locale switcher attrs | CS-NAV-03 | browser-verifier |
| E1 gold focus ring | CS-NAV-02 / CS-RESPONSIVE-07 / CS-BLOCK-N-04 | contrast-accessibility-auditor · responsive-auditor |
| E2 reduced-motion | CS-RESPONSIVE-07 / BRWS-FEEL-08 | browser-verifier (REUSABLE-AFTER-HARDENING per AP12) |
| E3 marquee 110s | design-standard §17 non-blocking | style-critic (informational) |
| F1 D-054 docstring | CS-EXEC-02 / CS-BLOCK-12 / O12 | template-planner · copy-translation-agent · release-gatekeeper |
| F2 voice anchor verbatim | CS-EXEC-01 / CS-BLOCK-11 / O11 | template-planner · copy-translation-agent · browser-verifier · release-gatekeeper |
| F3 anti-pattern docstring | CS-EXEC-04 / CS-BLOCK-P-05 | copy-translation-agent · style-critic |
| F4 verifiable credentials | CS-EXEC-03 / CS-HERO-06 / CS-BLOCK-10 / O10 | copy-translation-agent · style-critic · imagery-curator |
| G1 Pexels-only | CS-IMG-SRC-01 / CS-IMG-SRC-05 / CS-BLOCK-07 / O7 | imagery-curator (primary + reviewer) · release-gatekeeper |
| G2 one URL = one cluster | CS-IMG-SRC-04 / CS-BLOCK-I-02 | imagery-curator · CI script |
| G3 resolution floor | CS-IMG-PREM-02 / CS-IMG-SRC-02 / CS-BLOCK-IQ-01 | imagery-curator · browser-verifier |
| H1 CI floor | SOP §3.4 / §3.8 preconditions | template-builder · browser-verifier |
| H2 tests ≠ ship | CS-BROWSER-01..03 / CS-BLOCK-18 / O18 / AP8 | every agent in the pipeline |
