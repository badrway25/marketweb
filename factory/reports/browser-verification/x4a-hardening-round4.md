# Corporate-suite X.4a Hardening · Round 4 · RTL AR Browser Verification

**Verdict**: **PASS** (0 blocking · 0 required failures on Priority 1B scope · two independent walks · no fixes applied)
**Archetype**: `corporate-suite`
**Templates walked**: `pragma-corporate-suite`, `fiscus-commercialista`
**Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at re-verification walk**: `edcdbed` (Step 2E P1A bundle · committed). The original walk ran at `44700fc` (working tree of the same P1A bundle); both share the four-element CS-BLOCK-17 (extended) palette-safety patch.
**Walk run-ISOs**:
- `20260425T0837Z` — initial walk (server `:8734` · pre-fix corpus only · no post-fix needed because pre-fix was already PASS).
- `20260425T1100Z` — **re-verification walk on the post-merge tip `edcdbed`** (server `:8735`); identical PASS verdict; 0 blocking / 0 required failures across the same 6 pages × 4 sampled viewports per template; same contract checks ran; same contrast ratios observed (16.87 / 12.81 / 12.86); the locale switch IT→AR remained a layout flip rather than a contrast change, so the Round 2 CS-BLOCK-17 (extended) patches still hold without amendment.
**Reviewer**: Claude (Opus 4.7, Playwright MCP driver)
**Walk type**: Playwright MCP (`mcp__plugin_playwright_playwright__*`).
**Evidence**:
- `factory/reports/browser-verification/x4a-step2/20260425T0837Z-rtl-ar/` — initial walk corpus
  - `screenshots/pragma/`  — 7 PNG (Pragma AR home @ 1440 + 390 + 5 interior pages @ 1440)
  - `screenshots/fiscus/`  — 7 PNG (Fiscus AR home @ 1440 + 390 + 5 interior pages @ 1440)
  - `measurements/contrast-ar.json`   — cream-on-navy chrome contrast ratios per template
  - `measurements/rtl-contract.json`  — per-cell RTL contract validation (12 cells × sampled viewports)
- `factory/reports/browser-verification/x4a-step2/20260425T1100Z-rtl-ar/` — re-verification corpus (same shape; 14 PNG total · 7 / template; 2 measurement JSONs)
- `factory/reports/hardening/step2-ci/test-run-20260425T1100Z.txt` — re-verification CI floor (171 tests · OK · 2.795 s)

**Companion execution report**: `factory/reports/hardening/step2-execution-round2.md` (P1B section appended).

**Scope note** — this is the Round 4 live walk for the Step 2 **P1B bundle only** (RTL AR walk per plan §6.3 / T-P1-2). LTR multi-locale walk V2 (T-P1-1 · P1A) was closed by Round 3 (`x4a-hardening-round3.md`); the Round 3 verdict remains in force unchanged. P0 (reduced-motion + build-time gates + footer-href + gatekeeper-CRITICAL alignment + canonical CI transcript) was closed in Round 2 (`x4a-hardening-round2.md`); the Round 2 verdict remains in force unchanged. Solaria Commit B remains paused (B1) — this round does not un-pause it.

---

## Server

- **URL (current · re-verification)**: `http://127.0.0.1:8735/`
- **Started at**: `2026-04-25T11:00Z` (fresh `python manage.py runserver 127.0.0.1:8735 --noreload` on the post-P1A-merge tip `edcdbed`).
- **Still running**: **yes** — the server remains running for parallel user verification at `http://127.0.0.1:8735/` until the user explicitly releases the walk (BRWS-SRV-04 honored).
- **Restarts during re-verification walk**: 0 (no fixes applied → no restart needed).
- **Initial-walk server**: `http://127.0.0.1:8734/` was used for run-ISO `20260425T0837Z` and stopped before this re-verification began (port freed; `:8735` is the only live process).
- **Earlier servers** — `http://127.0.0.1:8731/` (Round 1), `:8732/` (P1A pre-fix), `:8733/` (P1A post-fix), `:8734/` (initial P1B) all stopped.

## Scope

- **Locale walked**: AR (`?lang=ar`) — closes the rubric's RTL bar that LTR rounds left empty.
- **Pages walked** (12 cells = 2 templates × 6 pages):
  - **Pragma**: `home` · `chi-siamo` · `competenze` · `case-studies` · `case-studies/manifatturiero-bresciano-piano-industriale` · `contatti`.
  - **Fiscus**: `home` · `lo-studio` · `competenze` · `casi-seguiti` · `casi-seguiti/pmi-manifattura-bilancio-revisione` · `contatti`.
- **Viewports walked**:
  - **1440 × 900** — primary walk for all 12 cells with full-page screenshots + DOM measurements.
  - **390 × 844** — mobile floor sampled on home for both templates (2 cells); confirms hero stack + drawer collapse + h1 ≥ 32 px floor + mp-lang touch-target ≥ 44 × 44 + no overflow.
  - **1024 × 768** — sampled on Pragma AR home for breakpoint stability spot-check (BRWS-VIEW-04).
  - **768 × 1024** — sampled on Pragma AR home for the 880-px drawer engagement floor.
- **Screenshots captured (this round)**: 14 PNG (7 / template). The §7 floor of 120 / template at the full 5-locale × 6-page × 4-viewport matrix is met **cumulatively** across Rounds 1D + 2 + 3 + 4 (this round adds the AR slice; the floor closes here).

## Reduced-motion handling

The walk uses an explicit `force-reveal` evaluator (`document.querySelectorAll('[data-lm]').forEach(el => { el.style.opacity='1'; el.style.transform='none'; })`) before each `fullPage` screenshot. This is the same Round 2 / Round 3 capture-mechanism convention; the **JS reduced-motion contract** (BRWS-FEEL-08) was verified live in Round 2's reduced-motion walk (`x4a-step2/20260424T2346Z/reduced-motion/verdict.md`) on 150 `[data-lm]` elements across 12 pages. The locale switch from IT/EN/FR/ES to AR does not touch motion JS or the CSS `@media (prefers-reduced-motion: reduce)` block — nothing in this round could regress the AP12 contract.

## Summary counts

```
[BLOCKING]   total:  9   failed:  0
[REQUIRED]   total:  6   failed:  0
[STRONG]     total:  3   failed:  0
[GUIDELINE]  total:  2   failed:  0
```

The pre-fix AR walk surfaced **0 blocking** and **0 required** failures across all 12 (template, page) cells × 4 sampled viewports. No archetype-level skin edits were applied in this round.

## Per-cell measurements (1440 baseline)

| Template | Locale | Page | scrollW vs clientW | overflow | h1 (truncated) | h1 fontSize | placeholder text | footer legal |
|---|---|---|---:|:---:|---|---:|:---:|---:|
| Pragma | ar | home | 1425 ≤ 1425 | no | حيث تُتَّخَذ القرارات التي تصنع الفرق. | 64 px | no | 3/3 real |
| Pragma | ar | about | 1425 ≤ 1425 | no | بوتيك مستقل، اثنان وعشرون عاماً … | n/a | no | 3/3 real |
| Pragma | ar | services | 1425 ≤ 1425 | no | ست كفاءات، توقيع واحد. | n/a | no | 3/3 real |
| Pragma | ar | cases | 1425 ≤ 1425 | no | ثلاثة تكليفات، ثلاثة اتجاهات. | n/a | no | 3/3 real |
| Pragma | ar | case-detail | 1425 ≤ 1425 | no | مجموعة تصنيع في بريشيا · خطة صناعية 2025-28 | n/a | no | 3/3 real |
| Pragma | ar | contact | 1425 ≤ 1425 | no | ثلاثون دقيقة، أجندة محدودة، دون أي التزام. | n/a | no | 3/3 real |
| Fiscus | ar | home | 1425 ≤ 1425 | no | الامتثال الصحيح، لا الحيلة الضريبية. | 64 px | no | 3/3 real |
| Fiscus | ar | about | 1425 ≤ 1425 | no | مكتب استشارات ضريبية مستقل، اثنان وعشرون عاماً … | n/a | no | 3/3 real |
| Fiscus | ar | services | 1425 ≤ 1425 | no | ستة مجالات اختصاص، توقيع واحد. | n/a | no | 3/3 real |
| Fiscus | ar | cases | 1425 ≤ 1425 | no | ثلاث حالات، ثلاثة مجالات اختصاص. | n/a | no | 3/3 real |
| Fiscus | ar | case-detail | 1425 ≤ 1425 | no | شركة تصنيع صغيرة ومتوسطة في لومبارديا · إطار مراجعة قانونية | n/a | no | 3/3 real |
| Fiscus | ar | contact | 1425 ≤ 1425 | no | خمس وأربعون دقيقة، بأجندة مفتوحة، دون أي التزام. | n/a | no | 3/3 real |

(`scrollW = 1425` at viewport `1440` reflects the 15-px Playwright scrollbar reservation; the inequality `scrollW ≤ clientW + 1` is what BRWS-VIEW-02 actually requires, so 1425 ≤ 1425 = pass.)

## Per-cell mobile floor (390 × 844)

| Template | Page | scrollW vs clientW | overflow | h1 fontSize | navLinks display | navBurger display | mp-lang pill size |
|---|---|---:|:---:|---:|---|---|---|
| Pragma | home | 375 ≤ 375 | no | 32 px | none | flex | 44 × 44 |
| Fiscus | home | 375 ≤ 375 | no | 32 px (h1 height 70.4 px = 2 lines) | none | flex | 44 × 44 |

## Per-cell sampled mid-viewports (Pragma AR home)

| Viewport | scrollW vs clientW | overflow | navLinks display | navBurger display | hero gridTemplateColumns |
|---|---:|:---:|---|---|---|
| 1024 × 768 | 1009 ≤ 1009 | no | flex | none | 504.5 px 504.5 px |
| 768 × 1024 | 753 ≤ 753 | no | none | flex | 376.5 px 376.5 px |

## Per-element AR contrast battery (1440 home · cream-on-navy chrome)

| Element | Pragma AR ratio | Fiscus AR ratio | WCAG bar |
|---|---:|---:|---|
| `.mp-bar .mp-back` | 16.87 | 16.87 | AAA (≥ 7.0) ✓ |
| `.mp-lang a.mp-lang-pill.is-current` | 16.87 | 16.87 | AAA (≥ 7.0) ✓ |
| `.cs-nav .wm .crest` | 12.81 | 12.86 | AAA (≥ 7.0) ✓ |
| `.cs-nav .wm` (wordmark span) | 12.81 | 12.86 | AAA (≥ 7.0) ✓ |
| `.cs-nav .links a` | 12.81 | 12.86 | AAA (≥ 7.0) ✓ |
| `.cs-hero h1` | 12.81 | 12.86 | AAA (≥ 7.0) ✓ |
| `.cs-kpi-band .stat .num` | 12.81 | 12.86 | AAA (≥ 7.0) ✓ |
| `.cs-foot .brand .word` | 12.81 | 12.86 | AAA (≥ 7.0) ✓ |

The 16.87 / 12.81 / 12.86 ratios are identical to the post-fix LTR Round 3 figures because the locale switch is a layout flip, not a contrast change. The four CS-BLOCK-17 (extended) patches landed in P1A close the AP11 risk on every dark surface they cover, irrespective of the rendering locale.

## Rubric checks that ran

### BRWS-CONTRAST-01 (BLOCKING · h1 vs body bg ≥ AA 4.5 / AAA 7.0) — **PASS**

Pragma AR home hero h1 = `rgb(30, 41, 59)` navy on `rgb(238, 240, 243)` cream paper-2 → ratio **12.81** (AAA ✓). Fiscus AR home → **12.86**. Identical to LTR figures (locale switch does not change foreground or background hex).

### BRWS-CONTRAST-02 (BLOCKING · dark-section descendants ≥ distance 120 / AA 4.5) — **PASS**

Every walked dark-surface descendant ≥ 12.81 ratio across both templates. The CS-BLOCK-17 (extended) palette-safety patches that closed Round 2's four AP11 hits on Fiscus's blu-notte palette carry to AR identically.

### BRWS-CONTRAST-03 (REQUIRED · nav text vs nav bg) — **PASS**

`.cs-nav .links a` and `.cs-nav .wm` resolve to ratio 12.81 (Pragma) / 12.86 (Fiscus) on their respective navy backgrounds. Hover-state ratios (not measured this round) are equal-or-greater per the LTR walk verdicts that remain in force.

### BRWS-CONTRAST-04 (REQUIRED · focus-visible accent ring · `Tab` walk) — **PASS**

`Tab → Tab → Tab` from the `<body>` lands on the EN locale-switcher pill on Pragma AR home; computed `outline: 2px solid rgb(16, 185, 129)` (Pragma emerald `--accent`) with `outline-offset: 4px`. Matches BRWS-CONTRAST-04 / E1 verbatim. `mp-back` (first Tab) returns browser-default `outline: auto rgb(16, 16, 16) 1px` because the `_base.html:370-375` whitelist does not include `.mp-bar .mp-back`; this is a pre-existing P2 deviation observable equally in LTR and is **not** an AR-specific regression. Tracked as a style-critic-pass item for T-P1-3.

### BRWS-VIEW-01 / VIEW-02 (BLOCKING · viewport coverage / no horizontal scroll) — **PASS**

`document.documentElement.scrollWidth ≤ document.documentElement.clientWidth + 1` on every (template, page, viewport) cell walked. Step 1D root-guard (`html { overflow-x: clip; body { overflow-x: clip; }`) is active in RTL; no edge-case overflow surfaced.

### BRWS-VIEW-03 (BLOCKING · hero stacks ≤ 720) — **PASS**

At 390 × 844 the hero grid resolves to a single column (`grid-template-columns: 375px`) on both Pragma + Fiscus AR home; mobile screenshots confirm hero text stacks above the photo. The is_rtl branch (`_base.html:700`) flips the desktop ratio to `1fr 1.3fr` (text-narrower, photo-wider on the right because the column flow reverses), but at ≤ 720 the responsive cascade collapses to a single column regardless of `dir`.

### BRWS-VIEW-04 (BLOCKING · drawer collapses ≤ 720; in our skin ≤ 880) — **PASS**

Drawer engaged at 768 (`navLinksDisplay: none`, `navBurgerDisplay: flex`) and 390 across both templates' AR home. At 1024 the drawer is **not** engaged (`navLinksDisplay: flex`, `navBurgerDisplay: none`) — matches the 880 breakpoint contract.

### BRWS-VIEW-06 (REQUIRED · hero h1 ≥ 32 px @ 390) — **PASS**

`heroH1FontSize: "32px"` on Pragma AR home and Fiscus AR home at 390 × 844. The Arabic h1 wraps to 2 lines with line-height 1.18 (per `html[dir="rtl"] h1 { letter-spacing: 0; line-height: 1.18; }`) — Fiscus AR home h1 measured 70.375 px tall.

### BRWS-VIEW-07 (REQUIRED · touch targets ≥ 44 × 44 @ 390) — **PASS**

`.mp-lang a.mp-lang-pill` rendered at 44 × 44 px on AR mobile (per the `@media (max-width: 720px)` rule at `_base.html:944-948`). The `.cs-nav-burger` is 44 × 44 by static rule. Hero `.cs-btn-primary` (visible in mobile screenshots) reads as a touch-friendly button at the 32-px hero scale.

### BRWS-NAV-01 (BLOCKING · nav bg = `--primary`) — **PASS**

Pragma AR navBg = `rgb(30, 41, 59)` (matches Pragma `SEED_TEMPLATES[...].brand.palette.primary` `#1E293B`). Fiscus AR navBg = `rgb(31, 41, 55)` (matches Fiscus `--primary` `#1F2937`). No polarity inversion.

### BRWS-NAV-02 (BLOCKING · ≤ 1 accent CTA in nav) — **PASS**

The trailing nav CTA cell is unchanged from LTR; the AR locale rotation does not introduce additional accent hits in the nav. Visual confirmation in Pragma + Fiscus AR home screenshots.

### BRWS-NAV-03 (REQUIRED · locale-switcher pills carry `lang` + `dir`) — **PASS**

The `_base.html` template renders `<a class="mp-lang-pill" lang="{{ entry.code }}" dir="{% if entry.code == 'ar' %}rtl{% else %}ltr{% endif %}">…</a>`. AR pill renders `lang="ar" dir="rtl"`; LTR pills render `lang="<code>" dir="ltr"`. Static-test floor remains green.

### BRWS-RHYTHM-01..05 — **PASS**

Section padding `100px 72px` desktop (eased to 84/48 at ≤ 1280, 72/40 at ≤ 1100, 64/28 at ≤ 880, 52/22 at ≤ 720, 18-x at ≤ 480) holds in AR. Home section order is preserved: hero · pillars · kpi · sectors+trust · leadership · cases · CTA. Single dark KPI band per home; no two adjacent dark bands.

### BRWS-FOOT-01..05 — **PASS**

Three columns at desktop (1.4 / 1 / 1 / 1 with the 4th col wrap-bottom), polarity matches navbar (cream-on-navy), legal-row 3 anchors all real routes (36 / 36 anchors across 12 cells), Latin wordmark + Latin numerics preserved (D2 / CS-FOOT-04), 1-column at ≤ 720 with `text-align: left` on `.bot`.

### BRWS-FEEL-01..06 — **PASS**

- **FEEL-01** Pragma + Fiscus AR cells read as authentic Arabic-localized advisory + commercialista renderings — the typography (Noto Kufi Arabic display, Amiri body) gives the Arabic version a distinct editorial weight that matches the cluster voice. No template-showcase tells.
- **FEEL-02** No `mw-is-editor-preview` body class; no editor halos on `/live/`.
- **FEEL-03** `body.innerText.toLowerCase()` substring scan on every walked cell returns 0 hits for "lorem ipsum" / "replace this text" / "your headline here".
- **FEEL-04** No celebrity quotes / no banned phrases.
- **FEEL-05** Voice anchor rendered as the home h1 verbatim per template:
  - Pragma AR: `"حيث تُتَّخَذ القرارات التي تصنع الفرق."` ✓
  - Fiscus AR: `"الامتثال الصحيح، لا الحيلة الضريبية."` ✓
- **FEEL-06** Credentials cluster-specific (ODCEC, Cassazionista, Partita IVA preserved Latin; Arabic credential phrasing matches advisory voice).

### BRWS-FEEL-07 (STRONG · console clean) — **PASS**

0 errors / 0 warnings on subsequent navigations after the first-load favicon 404. The favicon 404 was not repeated on any walked page after the initial load and is waivable per the Round 2 convention.

### BRWS-FEEL-08 (STRONG · prefers-reduced-motion) — **PASS** (carried from Round 2)

The Round 2 reduced-motion walk verdict at 1440 × 900 × IT remains in force. The Round 4 walk did not touch motion JS or the CSS `@media (prefers-reduced-motion: reduce)` block; nothing in the AR locale switch could regress the AP12 contract.

### CS-CTA-04 (REQUIRED · footer legal real-route) — **PASS**

36 / 36 footer legal anchors across the 12 (template, page) cells point at `/templates/business/<slug>/preview/contatti/?lang=ar`. Zero `href="#"` placeholders survive. The Round 1 wiring + the per-locale querystring carry to AR unchanged.

### CS-PAL-04 / AP11 (BLOCKING · dark-section AP11 inversions) — **PASS**

Every walked AR dark-surface text element ≥ 12.81 ratio. The Round 2 four-element CS-BLOCK-17 (extended) patch closes the AP11 risk on `mp-bar .mp-back` / `mp-lang.is-current` / `cs-nav .wm .crest` / `cs-post .kpi-band .stat .num` for every corporate-suite locale. Round 4 verifies the contract on AR — the patch holds without amendment.

### RTL-SPECIFIC CONTRACT CHECKS (corporate-suite-blocking-rules / D-class)

- **D1** (Arabic font-swap → no square glyphs) — Noto Kufi Arabic loaded via Google Fonts swap (`_base.html:11-13` `is_rtl` block); rendered glyphs in screenshots show no `.notdef` squares. ✓
- **D2** (Latin numerics + Latin wordmark in RTL) — `.cs-kpi-band .stat .num` font-family resolves to `<theme.heading_font>, Georgia, serif` (Pragma Merriweather / Fiscus IBM Plex Serif) with `unicode-bidi: isolate`. `.cs-nav .wm`, `.cs-foot .brand .word` keep the heading font (Latin). Visual screenshots confirm "M 4 €" / "M 180 €" / "+39 02" / "20121 Milano" / "ODCEC" all render Latin, embedded inside the RTL block. ✓
- **D3** (Logical-property flips on chrome + hero credit + KPI rows + case rows) — the `is_rtl` branch (`_base.html:698-742`) flips: `cs-hero` grid-cols (1.3fr 1fr → 1fr 1.3fr); `cs-pillars/cases-preview/cases-list .head` flips (1fr 0.45fr); `cs-cta .wrap` flips (0.6fr 1fr); `cs-foot .top` flips (1fr 1fr 1fr 1.4fr); `cs-history .timeline .body-cell` border flips left → right; `cs-form .cs-consent-box` border flips; `cs-sectors .label` border flips; `cs-kpi-band .heading` + `.stat` border flips. All visible in the AR screenshots. ✓
- **D4** (eyebrow accent flips + button arrow flips) — `.cs-lead .eyebrow:before` margin flips (`margin-left: 4px; margin-right: 0;`); `.cs-btn-primary:after { content: '←'; }`; `.cs-cases-preview / -list / .next-case .arrow { transform: scaleX(-1); }`. Visible in the case-detail and cases-list screenshots. ✓
- **D5** (locale-switcher per-link `lang` + `dir`) — covered under BRWS-NAV-03 above. ✓

## Issues found in Round 4

### Inside Priority 1B scope · resolved or n/a

**No blocking issues found.** No archetype-level skin edits applied in this round; the Round 2 CS-BLOCK-17 (extended) palette-safety patches close the AP11 risk-class on every dark surface the AR locale touches by construction.

### Side-observations carried into a future round

- **R5 grandfather** — `LEGACY_EXEMPT_KEYS = {business-corporate}` still holds. `corporate_suite.W001` warning surfaces silently across the walk. Per plan §5 + R-SOL-10 this stays load-bearing; no Round 4 action.
- **mp-back focus-visible** — first Tab focuses `.mp-bar .mp-back` which uses browser-default outline (not the gold accent ring). This is identical in LTR and AR; the rule's whitelist is locale-independent. Style-critic pass under T-P1-3 should decide whether to extend the whitelist or document the deviation.
- **Hero h1 italic em color is `--primary` (navy) not `--accent`** — by current CSS contract (`_base.html:169`); identical in AR and LTR. Style-critic pass under T-P1-3 should decide whether to add an accent override or document the navy-em decision explicitly.

### Outside P1B scope · pre-existing, tracked

- **B1** Solaria Commit B remains paused (binding user instruction). Unchanged.
- **B2** `LEGACY_EXEMPT_KEYS = {business-corporate}` (Pragma legacy Unsplash). Unchanged.
- **B7** `templates/preview_compositions/business/corporate-suite.html` untouched.
- **T-P1-3 AP8 end-to-end Fiscus pipeline run** scheduled for Round 5.
- **T-P1-4 D-054 triangulation refresh** scheduled to land after T-P1-3.
- **T-P1-5 primary-CTA paper-surface solid-variant decision** scheduled before Go.

## Deviations (§ deviation)

1. **`[data-lm]` motion elements force-revealed before screenshots.** Same Round 2 / Round 3 capture-mechanism convention. Aligned with `corporate-suite-multi-agent-sop.md §5` "evidence captured, not claimed". The reduced-motion JS contract was verified separately in Round 2.
2. **8-viewport sweep limited to 1440 + 390 floor + 1024 + 768 for the AR corpus.** Per plan §6.5 the rubric §7 minimum is 5 locales × 6 pages × 4 core viewports = 120 / template; AR contributes the 5th locale and closes the cluster-cumulative floor across Rounds 1D + 2 + 3 + 4. 1920 / 1280 / 640 / 414 not walked in this round — they were verified in Step 1D's 8-viewport IT-LTR sweep, which is layout-only and locale-independent at the breakpoint level.
3. **Voice-anchor pre-check substring guesses missed Fiscus AR phrasing.** The walker's `body.innerText.includes(<guess>)` boolean returned `false` for Fiscus AR home because the precise translation differs from the substring set the walker pre-coded. Visual + h1-grep confirmed the anchor renders verbatim. Tracked as a `browser-verifier` agent prompt-update item for T-P1-3.

All deviations are explicit plan-aligned scoping or capture-mechanism choices, not unacknowledged gaps.

## Imagery walk summary

No imagery-walk results new to Round 4. The Round 1 / Round 2 / Round 3 imagery-pool findings stand unchanged:

| Pool key | Template | URLs 200 / 6 | Host policy | Build-time gate |
|---|---|---|---|---|
| `business-corporate` | Pragma | 6/6 | 6 non-Pexels (LEGACY_EXEMPT) | `corporate_suite.W001` (visible Warning, non-blocking per design) |
| `business-fiscal` | Fiscus | 6/6 | Pexels-only | silent (no finding) |

## Responsive walk summary

- 1100 px breakpoint active (BRWS-VIEW-04) — verified in Step 1D + spot-checked in Round 4 at 1024 (Pragma AR home).
- 880 px breakpoint active (drawer engagement) — verified at 768 (Pragma AR home).
- 720 px breakpoint active (BRWS-VIEW-03) — verified at 390 × 844 across both AR home cells.
- Contact-form 880 px breakpoint — not re-walked in this round (Step 1D bar holds; no edits to `contact.html`); contact-page DOM measurements at 1440 confirm RTL form-input direction is `rtl`.
- Horizontal scroll at any walked viewport — **0** cases.
- Hero h1 at 390 px — **32 px** floor met on both AR home cells.
- Touch targets at 390 px — `.cs-nav-burger` rendered at 44 × 44; `.mp-lang a.mp-lang-pill` rendered at 44 × 44; `.cs-nav .links` collapsed; ghost-CTA carries the standing CS-CTA-03 deviation (P2 decision · T-P2-3).

## Console summary

- **JS errors**: **0** across the walked pages (favicon 404 surfaces on first navigation only; waived per Round 2 convention).
- **Warnings**: **0**.

## Verdict

**PASS** on Priority 1B (RTL AR walk) scope. The walk closes T-P1-2 from plan §3.P1 with **zero archetype-level skin edits** — the Round 2 CS-BLOCK-17 (extended) palette-safety patches were sufficient by construction to make AR a green walk.

Round 4 promotes the archetype state from "Conditional-Go-plus-LTR-PASS" to **"Conditional-Go-plus-LTR-PASS-plus-RTL-PASS"**. The cluster-cumulative rubric §7 floor of 120 screenshots / template is now met across Rounds 1D + 2 + 3 + 4. A full **Go** verdict per plan §10.3 still requires:

- T-P1-3 AP8 first end-to-end Fiscus pipeline run with full SOP §6 report set + release-gatekeeper scorecard
- T-P1-4 D-054 docstring triangulation refresh
- T-P1-5 primary-CTA paper-surface solid-variant decision

T-P1-3 is the next-in-sequence item. Round 4 does not un-pause Solaria Commit B (B1 unchanged); even the eventual Go verdict only marks the archetype as ready to accept Solaria re-entry, gated still on explicit user un-pause instruction (R-SOL-8).

## Parallel-verification handshake

The dev server remains at **http://127.0.0.1:8734/** and stays running until the user confirms parallel verification or explicitly releases the walk. Recommended parallel checks:

- Open `http://127.0.0.1:8735/templates/business/pragma-corporate-suite/preview/?lang=ar` and confirm the hero text renders on the right (RTL flip), the photo on the left, with the voice anchor `"حيث تُتَّخَذ القرارات التي تصنع الفرق."` as the h1.
- Open `http://127.0.0.1:8735/templates/business/fiscus-commercialista/preview/casi-seguiti/pmi-manifattura-bilancio-revisione/?lang=ar` and inspect the bottom KPI strip — `0 / 2 / 3 سنوات / 10 أسابيع` should read clean cream on dark navy (the Round 2 fix carries to AR unchanged).
- Switch via the marketplace pills between AR ↔ EN ↔ FR ↔ ES ↔ IT and confirm the layout flips polarity correctly each time (no horizontal-scroll on the transition; nav drawer behavior preserved).
- At 390 × 844 in the same browser (DevTools device-mode) confirm the hero stacks, the drawer engages, the locale pills are 44 × 44.
- Run `python manage.py test apps.catalog -v 2` locally; transcript should report `Ran 171 tests · OK · ~2-6 s` matching `factory/reports/hardening/step2-ci/test-run-20260425T1100Z.txt`.

— end of Round 4 verdict (re-verified 20260425T1100Z @ tip edcdbed) —
