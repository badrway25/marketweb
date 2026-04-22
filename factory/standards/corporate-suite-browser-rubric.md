# Corporate-suite Browser Live Verification Rubric

**Phase**: X.4a · Corporate-suite Factory Hardening · **Date**: 2026-04-21
**Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Scope**: factory files only · no `apps/editor`, `apps/projects`, `apps/commerce` changes · no new archetypes.
**Inputs**: `factory/reports/audits/corporate-suite-audit-master.md`, `factory/references/template-inventory.md`, `factory/references/pattern-library.md`, `factory/references/anti-pattern-library.md`, `factory/standards/corporate-suite-design-standard.md`, `factory/standards/corporate-suite-imagery-standard.md`.
**Audience**: every agent that verifies a corporate-suite template against the design + imagery standards in a live browser (browser-verifier, contrast-accessibility-auditor, responsive-auditor, imagery-curator reviewer, style-critic, release-gatekeeper). This file is the canonical answer to "has this template earned the right to flip LIVE?" — it is the executable counterpart of every `[BLOCKING]` rule in the sibling standards.

---

## 0 · How to use this document

1. Every rubric check carries a **severity tag** (same model as the design + imagery standards):
   - `[BLOCKING]` — failure prevents flip to `published_live`. Any occurrence here blocks the verdict.
   - `[REQUIRED]` — failure must be remediated before sign-off. A draft may land with a tracked TODO.
   - `[STRONG]` — failure is allowed only with explicit justification in the verdict under `§ deviation`.
   - `[GUIDELINE]` — a taste check; document the reason if you waive it.
2. Every check traces back to a rule in one of the sibling standards (tag shown inline, e.g., `CS-PAL-01`, `CS-HERO-07`, `CS-IMG-COH-01`). If a check has no sibling-rule anchor, it is a browser-only concern and will be marked `[BRWS-*]`.
3. **This rubric is not optional.** Running the Playwright MCP walk described here is the operational meaning of `CS-BROWSER-01 [BLOCKING]`. A template without a recorded walk cannot flip LIVE.
4. **Pair this document with**:
   - `corporate-suite-design-standard.md` · §5 Hero, §6 Nav, §7 Footer, §8 Rhythm, §14 Responsive, §15 Browser.
   - `corporate-suite-imagery-standard.md` · §3 Coherence, §4 Premium, §7 Crop.
   - `corporate-suite-blocking-rules.md` (to be populated) · detection recipes 1:1 with each `[BLOCKING]` below.
   - `factory/agents/browser-verifier.md` (to be populated) · the agent prompt that drives this rubric.

---

## 1 · Browser-first validation philosophy

### 1.1 · The load-bearing premise

Corporate-suite ships three templates today — Pragma (LIVE since Session 32, pre-factory), Fiscus (LIVE since Session 80, first full-factory pilot), Solaria (IT-only draft, paused). Solaria exposed a palette-polarity bug (`e8f38b5` → `6b70d56`) in which `--primary` was set to cream. Every `h1..h5`, every nav text, every KPI number rendered cream-on-cream — near-invisible body text on every page × every locale.

The bug survived:
- `manage.py check` — **0 issues**.
- `manage.py test apps.catalog` — **131/131** passing.
- `manage.py test apps` — **506/506** passing.
- `generate_previews` — **ran successfully**.

The bug did not survive **30 minutes of live browser walk**. That is the entire philosophy of this rubric in one incident.

### 1.2 · The operational claim

> **CLI green is a lower bound. Browser walk is the ship signal.**

This is not rhetoric. The repo's entire deterministic test surface cannot catch:
- Contrast failures (AP1 · palette polarity).
- Responsive breakage (AP2 · zero real breakpoints in 6/7 skin files).
- Imagery-semantic mismatches (AP4/AP5 · PlayStation gamepad as "map of Rome").
- Focus-ring branding regressions (E1 pattern vs browser-default blue).
- Dark-on-dark pockets created by new dark-section child elements (AP11).
- Reduced-motion JS wiring regressions (AP12).
- Editor affordances leaking into the public `/live/` route (CS-MARKET-01 guard).

Every class above has been observed in this repo. Every class above was caught by a human looking at a rendered page in a browser, not by a test runner.

### 1.3 · What this means operationally

1. **The browser walk is a required acceptance gate**, not a nice-to-have. Every new pilot on this archetype passes through this rubric before tier flips from `draft` to `published_live`.
2. **Tests-then-browser is the order** (CS-BROWSER-03). Tests running green is a precondition; if tests fail, the walk is pointless. If tests pass, the walk decides.
3. **Playwright MCP is the default mechanism.** Manual walks are allowed but must meet the same evidence bar. The MCP tool provides repeatable navigation, resize, screenshot, evaluate, and console-read — everything this rubric needs.
4. **The local server stays open throughout the walk**, and the URL + port are recorded so the user (or any second reviewer) can verify in parallel. A walk without a reported URL + port is a phantom walk and is rejected.
5. **Evidence is captured, not claimed.** Screenshots, console dumps, and DOM measurements are stored under `factory/reports/browser-verification/<template-slug>/`. Verdicts that assert "it looks fine" without evidence are rejected.

---

## 2 · CLI green is insufficient — explicit statement

> A template that passes `manage.py check` + `manage.py test apps.catalog` + `manage.py test apps` + `generate_previews` + `scripts/check_imagery_pack.py` **still has not earned the right to flip LIVE**.
>
> CLI green means only that the test harness could not fabricate a failure. It does not mean the rendered site works, is readable, is responsive, is cluster-coherent, or looks premium.
>
> Every `[BLOCKING]` check in this rubric was written because a CLI-green template shipped a defect that was invisible to the test suite and only visible to a reviewer in a browser. **Do not flip LIVE on CLI signal alone. Ever.**

This statement is intentionally redundant with CS-BROWSER-01 in the design standard and with AP8 in the anti-pattern library. It is restated here because the rubric is the moment of enforcement — every agent or human reading this file is about to decide a tier flip, and the cost of a false green is an Solaria-class defect in production.

---

## 3 · Mandatory tooling · Playwright MCP

### BRWS-TOOL-01 [BLOCKING] · The walk is driven by Playwright MCP unless explicitly waived by a human reviewer

- **Rule**: every programmatic walk on this archetype uses the `mcp__plugin_playwright_playwright__*` tool surface (or the equivalent `mcp__claude-in-chrome__*` surface). No headless screenshot scripts outside the MCP flow are accepted as primary evidence.
- **Rationale**: the MCP flow gives repeatable `navigate → resize → snapshot → evaluate → console` primitives that map 1:1 to the checks below. Ad-hoc scripts drift; MCP calls are auditable.
- **Minimum MCP surface used per walk**:
  - `browser_navigate` · load each locale × each page URL.
  - `browser_resize` · rotate through the viewport matrix (§5).
  - `browser_take_screenshot` OR `browser_snapshot` · evidence capture.
  - `browser_evaluate` · DOM measurements (contrast, widths, computed styles, outline checks).
  - `browser_console_messages` · JS error detection.
  - `browser_press_key` · keyboard walk (`Tab`-through for focus-visible).
- **Waiver condition**: a human reviewer may conduct a manual walk (real Chrome, DevTools open) IF the evidence bar below (§7) is met in full AND the walk log explicitly records "manual walk, MCP unavailable because …". A manual walk does NOT lower the evidence bar.

### BRWS-TOOL-02 [REQUIRED] · One walk = one MCP session · no mixing

- **Rule**: a single walk run uses a single MCP browser session. Do not stitch half a Playwright run together with half a Chrome-DevTools session. Either one tool or the other, with a clean transition recorded if the reviewer genuinely needed to switch.

### BRWS-TOOL-03 [REQUIRED] · Dev server runs locally; walk never hits a staging URL

- **Rule**: the walk targets `http://127.0.0.1:<port>/` running the current branch. Never target `staging.marketweb.*` or any remote host. The branch-local server is the source of truth for the rendered artifact.
- **Why**: staging may have stale static files; the walk is verifying THIS branch's render.

---

## 4 · Local server discipline — keep it open, report URL and port

### BRWS-SRV-01 [BLOCKING] · Start the dev server before the walk; keep it running throughout the walk

- **Rule**: the reviewer starts `python manage.py runserver` on a deterministic port BEFORE the MCP calls begin and keeps the process alive until the walk verdict is recorded. The server is not restarted mid-walk unless a migration or static-collect change is explicitly logged.
- **Why**: restarts can mask or introduce regressions. A stable server means every screenshot and every DOM measurement is comparable.

### BRWS-SRV-02 [BLOCKING] · Dev server URL and port MUST be recorded in the verdict

- **Rule**: the verdict block (§11) opens with `Server: http://127.0.0.1:<port>/` and a `Started at: <ISO-8601 timestamp>`. No exceptions. A verdict without URL + port is rejected at review.
- **Why**: the user (or any second reviewer) MUST be able to open the exact URL in a parallel browser window to sanity-check what the walk report claims. This is how the user verifies in parallel.

### BRWS-SRV-03 [REQUIRED] · The walk logs name the exact URLs hit, per locale and per page

- **Rule**: the walk log captures the full URL per navigation, including locale prefix and page path:
  - `http://127.0.0.1:<port>/it/templates/fiscus-commercialista/live/`
  - `http://127.0.0.1:<port>/en/templates/fiscus-commercialista/live/`
  - `http://127.0.0.1:<port>/it/templates/fiscus-commercialista/live/about/`
  - … etc.
- **Why**: URL discipline makes the walk reproducible. A verdict that says "checked all pages" without URLs is not auditable.

### BRWS-SRV-04 [REQUIRED] · The server stays open AFTER the walk until the user has verified in parallel

- **Rule**: the reviewer does NOT shut the server down as soon as the walk writes its verdict. The server remains running so the user can open the same URL + port in their own browser and confirm the evidence independently.
- **How to signal**: the verdict block closes with `Server still running at http://127.0.0.1:<port>/ — shut down on user confirmation`.
- **Why**: the user's parallel verification is the final layer of the acceptance gate. Shutting the server as the walk completes defeats that layer.

### BRWS-SRV-05 [REQUIRED] · If the server must be restarted mid-walk, the walk restarts from the top

- **Rule**: a mid-walk server restart invalidates prior evidence. The walk resumes from the top of the viewport matrix (§5) on the restarted server, and the verdict notes `Restart at <timestamp>, reason: <one line>`.
- **Why**: evidence captured against a different process instance is not comparable.

---

## 5 · Viewport matrix for verification

The current skin ships with effectively zero responsive breakpoints (AP2). The hardening pass adds `@media (max-width: 1100px)` and `@media (max-width: 720px)` to `_base.html` and the 6 page files. The walk must verify the result at the following target viewports:

| Viewport | Width × Height | Purpose | Severity if broken |
|---|---|---|---|
| **Wide desktop** | 1920 × 1080 | Confirm airy density holds — sections breathe, hero split stays 55/45, max-width 1400 stays centered with visible margins. | `[BLOCKING]` |
| **Standard desktop** | 1440 × 900 | The everyday desktop — most reviewer screens. | `[BLOCKING]` |
| **Narrow desktop** | 1280 × 800 | First stress test — 72 px horizontal padding starts to feel tight but no collapse yet. | `[BLOCKING]` |
| **Small desktop / large tablet** | 1024 × 768 | At or just above the 1100 breakpoint — verifies the condensed tablet layout kicks in cleanly. | `[BLOCKING]` |
| **Portrait tablet** | 768 × 1024 | Below the 1100 breakpoint, above 720 — tablet mode: tighter section padding, 2-column cards. | `[BLOCKING]` |
| **Mobile landscape** | 640 × 360 | Between the 720 breakpoint and the small-phone floor — confirms intermediate behavior. | `[REQUIRED]` |
| **iPhone-class** | 414 × 896 | The larger iOS phone — hero must be stacked, nav hamburger, 1-column cards. | `[BLOCKING]` |
| **Small phone floor** | 390 × 844 | The tightest-supported mobile — hero h1 ≥ 32 px, touch targets ≥ 44×44, no horizontal scroll. | `[BLOCKING]` |

### BRWS-VIEW-01 [BLOCKING] · The walk covers EVERY viewport in the matrix

- **Rule**: the MCP `browser_resize` call iterates the full matrix for each page × each locale that the scope of the walk demands. Skipping a viewport without justification is a rejected verdict.

### BRWS-VIEW-02 [BLOCKING] · At every viewport: no horizontal scrollbar

- **Rule**: `document.documentElement.scrollWidth <= document.documentElement.clientWidth` at every viewport. Record the two values in the evidence block. Any page where `scrollWidth > clientWidth` fails.
- **MCP call**: `browser_evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }))`.
- **Anchor**: CS-RESPONSIVE-02.

### BRWS-VIEW-03 [BLOCKING] · Below 720 px the hero stacks (text above photo)

- **Rule**: at 414 × 896 and 390 × 844 the hero grid must be `grid-template-columns: 1fr` and the left column (text) stacks above the right column (photo). Screenshot evidence required at both widths.
- **Anchor**: CS-HERO-07, CS-RESPONSIVE-01.

### BRWS-VIEW-04 [BLOCKING] · Below 1100 px the nav condenses · below 720 px the nav collapses to a hamburger

- **Rule**: at 1024 × 768 the nav shows tighter padding with still-horizontal links; at 390 × 844 the nav is a menu trigger that expands into a drawer. Both conditions are screenshot-recorded.
- **Anchor**: CS-NAV-05, CS-RESPONSIVE-01.

### BRWS-VIEW-05 [REQUIRED] · Contact page stacks at ≤ 880 px

- **Rule**: `contact.html`'s form + coordinates 2-column layout stacks form-above-coordinates at `@media (max-width: 880px)` (the only real pre-hardening breakpoint). Confirmed at 768 × 1024 and below.
- **Anchor**: CS-COMP-05, CS-RESPONSIVE-01.

### BRWS-VIEW-06 [REQUIRED] · Hero h1 font-size ≥ 32 px at 390 px

- **Rule**: at 390 × 844, `getComputedStyle(document.querySelector('.cs-hero h1')).fontSize` returns a value ≥ 32 px. Smaller values fail.
- **Anchor**: CS-RESPONSIVE-03.

### BRWS-VIEW-07 [REQUIRED] · Touch targets ≥ 44×44 on mobile viewports

- **Rule**: at 390 × 844 the nav CTA, hero primary CTA, each nav link when the drawer is open, and each locale-switcher pill all render with bounding-box `width ≥ 44 AND height ≥ 44`. `getBoundingClientRect()` evaluation captures.
- **Anchor**: CS-RESPONSIVE-06.

---

## 6 · The full check roster

Every check below runs at every relevant viewport (the viewport-class label after the tag notes where it applies). Checks without a viewport label apply at all viewports.

### 6.1 · Contrast

#### BRWS-CONTRAST-01 [BLOCKING] · `h1..h5` color vs body background · RGB distance ≥ 120, WCAG AA ≥ 4.5, AAA target ≥ 7.0

- **Evaluate**: for each of the 6 pages, iterate every `h1, h2, h3, h4, h5`. For each, compute `getComputedStyle.color` and compare against the body or section background at that DOM position. Compute both the RGB L2 distance and the WCAG contrast ratio.
- **Rule**:
  - RGB distance between text and immediate background ≥ 120. Distance < 120 is a suspected polarity inversion (Solaria AP1 pattern).
  - WCAG contrast ratio ≥ 4.5 (AA) for all body text; ≥ 7.0 (AAA) for hero h1.
- **Fail example**: Solaria `e8f38b5` — `primary = #F7F3EC` cream on `#F7F4EC` cream paper. Distance ~6, ratio ~1.02. Every h1..h5 fails.
- **MCP snippet**:
  ```js
  browser_evaluate(() => {
    const toRGB = (c) => c.match(/\d+/g).map(Number);
    const dist = (a, b) => Math.hypot(a[0]-b[0], a[1]-b[1], a[2]-b[2]);
    const body = toRGB(getComputedStyle(document.body).backgroundColor);
    return Array.from(document.querySelectorAll('h1,h2,h3,h4,h5')).map(h => {
      const fg = toRGB(getComputedStyle(h).color);
      return { tag: h.tagName, text: h.textContent.slice(0, 40), distance: dist(fg, body) };
    });
  });
  ```
- **Anchor**: CS-PAL-01, CS-HERO-03, AP1.

#### BRWS-CONTRAST-02 [BLOCKING] · Dark-section child elements use `--on-dark*` variants

- **Evaluate**: for each section with `background: var(--primary)` (or any visibly dark background), walk every descendant with visible text. For each, compute `color` vs section `backgroundColor` and apply the same distance/ratio test as BRWS-CONTRAST-01.
- **Rule**: every text node inside `.cs-section.dark` OR `.cs-kpi-band` OR `.cs-nav` OR `.cs-foot` (when footer is dark) must have RGB distance ≥ 120 against the section background.
- **Fail example**: a new `.cs-cta .new-text { color: var(--ink); }` inside a dark CTA band — dark text on dark navy.
- **Anchor**: CS-PAL-04, AP11.

#### BRWS-CONTRAST-03 [REQUIRED] · Nav text vs nav background · WCAG AA floor

- **Evaluate**: compute contrast of every `.cs-nav a, .cs-nav .wm, .cs-nav button` text color vs `.cs-nav` background.
- **Rule**: default-state AA ≥ 4.5, hover-state AA ≥ 4.5, active-state distinct from default.
- **Anchor**: CS-NAV-02, CS-PAL-06.

#### BRWS-CONTRAST-04 [REQUIRED] · Focus-visible outline is the gold accent, not browser default

- **Evaluate**: press `Tab` through the first 12 focusable elements on each page. For each, capture the computed `outlineColor` and `outlineStyle` while focused.
- **Rule**: `outlineColor` resolves to `var(--accent)` (Pragma emerald, Fiscus gold, Solaria ocra). `outlineStyle: solid`. `outlineOffset: 4px`. No browser-default blue (`rgb(0, 95, 204)` or any sRGB-blue default).
- **Anchor**: CS-NAV-02, E1.

### 6.2 · Readability

#### BRWS-READ-01 [BLOCKING] · Hero h1 readable at all viewports

- **Evaluate**: at every viewport in the matrix, screenshot the hero. Visually verify h1 is present, readable, and does not clash with the photo behind it.
- **Rule**: at 1920/1440/1280/1024 the h1 occupies the left column with clear separation from the photo. At 768 the left column narrows but h1 remains legible. At ≤ 720 the h1 stacks above the photo and remains ≥ 32 px.
- **Anchor**: CS-HERO-01, CS-HERO-07, CS-RESPONSIVE-03.

#### BRWS-READ-02 [BLOCKING] · Subhead is one paragraph ≤ 35 words · renders on 1-3 lines desktop

- **Evaluate**: grep the hero subhead text, count words; at 1280 verify it renders on 1-3 lines (not 6).
- **Anchor**: CS-HERO-05, CS-DENSITY-01.

#### BRWS-READ-03 [REQUIRED] · Body paragraphs ≤ ~120 words per block · no walls of text

- **Evaluate**: on home/about/services screenshot each section; flag any `<p>` above ~120 words.
- **Anchor**: CS-DENSITY-07.

#### BRWS-READ-04 [REQUIRED] · Letter-spacing and line-height preserve legibility across locales

- **Evaluate**: switch to the French and Arabic locales; re-capture the hero and a mid-page section. In FR, verify headlines don't overflow (French is typically ~15% longer than English). In AR, verify the `0.22em` tracking has reset to 0 (pattern D4) and Arabic glyphs don't render as squares.
- **Rule**: no overflow clipping; no square-glyph rendering (= font-swap failure, pattern D1 broken).
- **Anchor**: CS-TYPE-05, CS-TYPE-06, D1, D4.

#### BRWS-READ-05 [REQUIRED] · KPI numerics are tabular-aligned across locales

- **Evaluate**: on each locale's home, inspect `.cs-kpi-band .num` computed `fontVariantNumeric`. Confirm `tabular-nums`.
- **Rule**: value contains `tabular-nums`; visually verify each figure's decimal/unit sits in the same column across the 3-4 stats.
- **Anchor**: CS-TYPE-03, B5.

### 6.3 · Accent / navbar harmony

#### BRWS-NAV-01 [BLOCKING] · Navbar background = `--primary` · never inverted

- **Evaluate**: `getComputedStyle(document.querySelector('.cs-nav')).backgroundColor` resolves to the seeded `primary` hex.
- **Rule**: mismatch with the template's `SEED_TEMPLATES[...].brand.palette.primary` is a fail.
- **Anchor**: CS-NAV-01, CS-PAL-06.

#### BRWS-NAV-02 [BLOCKING] · Exactly one accent CTA in the nav · the trailing one · accent-filled

- **Evaluate**: query `.cs-nav button, .cs-nav a[role=button]`. Count nodes whose computed `backgroundColor` matches `--accent`. Must be exactly 1. That node is the trailing CTA ("Prenota una consulenza" / "Prenota una call" / etc.).
- **Fail example**: accent-coloring the wordmark or adding accent dividers — more than 1 accent element appears.
- **Anchor**: CS-NAV-04, CS-PAL-05.

#### BRWS-NAV-03 [REQUIRED] · Locale switcher renders with `lang` and `dir` per link

- **Evaluate**: query each `<a>` inside the locale switcher pill. Verify each has `lang` and `dir` attributes matching its target locale (`lang="en"`, `lang="ar" dir="rtl"`, …).
- **Anchor**: CS-NAV-03, D5.

#### BRWS-NAV-04 [REQUIRED] · Four distinct nav-link states visible

- **Evaluate**:
  1. Screenshot the nav at rest.
  2. Hover one link (MCP `browser_hover`); screenshot.
  3. `Tab` to one link; screenshot.
  4. Navigate to a non-home page and screenshot the nav to verify the "current page" indicator.
- **Rule**: each state is visually distinguishable from the others; the focus-visible state shows the gold outline; the active-page indicator is an underline or accent dot (not an accent-color text shift).
- **Anchor**: CS-NAV-02, E1.

#### BRWS-NAV-05 [REQUIRED] · Accent color appears ≤ 2-3 times per viewport · not everywhere

- **Evaluate**: at the desktop viewport, snapshot the visible above-the-fold region. Count elements whose `backgroundColor` OR `borderColor` OR `color` resolves to `--accent`. Typical acceptable: nav CTA (1), hero primary CTA (1), hero italic `<em>` or editorial accent (≤ 1). Total ≤ 3.
- **Fail example**: accent underlines on every nav link + accent dividers + accent-filled icon squares — 8+ accent elements per fold.
- **Anchor**: CS-PAL-05.

### 6.4 · Hero quality

#### BRWS-HERO-01 [BLOCKING] · 55/45 split holds on desktop · stacks at ≤ 720

- **Evaluate**: `getComputedStyle(document.querySelector('.cs-hero')).gridTemplateColumns`.
- **Rule**: at 1920/1440/1280 resolves to `1.3fr 1fr` (or equivalent widths near 55/45). At 390/414 resolves to a single column.
- **Anchor**: CS-HERO-01, CS-HERO-07.

#### BRWS-HERO-02 [BLOCKING] · Hero photo is from curated Pexels pack · full-bleed right column · credit overlay present

- **Evaluate**: inspect the hero `<img>` `src`. Confirm it matches the template's `preview_imagery.py` slot 0. Confirm a credit overlay exists (curator attribution per CS-IMG-SRC-03).
- **Fail examples**: a 4-up photo grid in the hero; a video background; a gradient-only hero.
- **Anchor**: CS-HERO-02, CS-IMG-POOL-02, CS-IMG-COH-06.

#### BRWS-HERO-03 [BLOCKING] · Hero has one primary CTA · at most one secondary · real `href` targets

- **Evaluate**: query CTAs inside `.cs-hero`. Count accent-filled = 1, count outline/ghost ≤ 1. For each, verify `href` is a real route (`/contact/`, `/services/`, not `#` or `#contact-form`).
- **Fail examples**: three accent CTAs; `href="#"`.
- **Anchor**: CS-HERO-04, CS-CTA-01, CS-CTA-04.

#### BRWS-HERO-04 [REQUIRED] · Hero meta-strip shows 2-4 credential anchors

- **Evaluate**: locate the meta-strip below the hero subhead. Count credential entries ("Iscritti ODCEC Milano", "Cassazionisti", etc.).
- **Rule**: between 2 and 4 entries; every entry maps to the cluster blueprint §4 vocabulary.
- **Anchor**: CS-HERO-06, CS-EXEC-03.

#### BRWS-HERO-05 [REQUIRED] · Hero h1 uses italic `<em>` emphasis on one load-bearing word

- **Evaluate**: inner HTML of `.cs-hero h1` contains `<em>…</em>`; the `<em>` wraps exactly one word (or one short phrase); computed `fontStyle` is `italic`.
- **Anchor**: CS-TYPE-02, B4.

#### BRWS-HERO-06 [REQUIRED] · Hero photo survives crop at 4:3 (desktop) AND 16:9 (mobile stacked)

- **Evaluate**: at 1440 screenshot the hero right column (~4:3). At 390 screenshot the stacked hero (~16:9). Subject legible in both.
- **Anchor**: CS-IMG-CROP-01, CS-RESPONSIVE-05.

### 6.5 · Footer quality

#### BRWS-FOOT-01 [REQUIRED] · Three columns desktop · brand + sitemap + contact

- **Evaluate**: count direct children of `.cs-foot .foot-grid` (or equivalent). Must be 3. Each column content matches the prescribed role.
- **Anchor**: CS-FOOT-01.

#### BRWS-FOOT-02 [REQUIRED] · Polarity matches navbar · dark background + `--on-dark` text

- **Evaluate**: `getComputedStyle(.cs-foot).backgroundColor` is dark (primary or a deep neutral). Text inside uses `--on-dark*`.
- **Anchor**: CS-FOOT-01, CS-PAL-04.

#### BRWS-FOOT-03 [REQUIRED] · Legal row carries the 5 canonical links · whistleblowing present for advisory clusters

- **Evaluate**: enumerate legal-row links. Verify presence: copyright · P.IVA · privacy · cookie · whistleblowing (commercialista/law/advisory).
- **Anchor**: CS-FOOT-02.

#### BRWS-FOOT-04 [REQUIRED] · RTL footer keeps Latin wordmark + Latin numerics

- **Evaluate**: on the AR locale, inspect `.cs-foot .brand .word` and `.cs-foot .num` — computed `font-family` resolves to the Latin heading font, not Kufi/Amiri.
- **Anchor**: CS-FOOT-03, D2.

#### BRWS-FOOT-05 [REQUIRED] · Footer stacks to 1 column at ≤ 720 px

- **Evaluate**: at 390 × 844 the 3 columns become 1 stacked column.
- **Anchor**: CS-FOOT-05.

#### BRWS-FOOT-06 [GUIDELINE] · No newsletter signup above the legal row

- **Evaluate**: no `<form>` inside the footer above the legal row.
- **Anchor**: CS-FOOT-04.

### 6.6 · Section rhythm

#### BRWS-RHYTHM-01 [BLOCKING] · Every section wrapper has `100px 72px` padding · `max-width: 1400`

- **Evaluate**: iterate direct-child sections of the home layout. `getComputedStyle(section).padding` ≈ `100px 72px` at desktop. `maxWidth: 1400px`. `margin: 0 auto`.
- **Anchor**: CS-RHYTHM-01, CS-TONE-02.

#### BRWS-RHYTHM-02 [REQUIRED] · Home section order matches the fixed contract

- **Evaluate**: enumerate section DOM order. Must read: hero · pillars · kpi-band · sectors+trust · leadership · cases · CTA.
- **Anchor**: CS-RHYTHM-02.

#### BRWS-RHYTHM-03 [REQUIRED] · Home has exactly one dark band · the KPI band · at position 3 · not adjacent to another dark band

- **Evaluate**: count `background-color` matches against `--primary` across home sections. Expect 1 (or 2, non-adjacent). Fail if 3+ or if two dark bands are adjacent.
- **Anchor**: CS-TONE-03, CS-RHYTHM-03.

#### BRWS-RHYTHM-04 [REQUIRED] · No two adjacent sections share the same functional label

- **Evaluate**: label each home section in one word (hero/pillars/kpi/sectors/leadership/cases/cta). Fail if two adjacent sections would get the same label.
- **Anchor**: CS-RHYTHM-04.

#### BRWS-RHYTHM-05 [REQUIRED] · Section h2 uses italic `<em>` emphasis · no uppercase-shouted titles

- **Evaluate**: every h2 inner HTML contains at most one italic `<em>` span; no `text-transform: uppercase` on h2.
- **Anchor**: CS-RHYTHM-05, CS-TYPE-02.

### 6.7 · Imagery quality and coherence

#### BRWS-IMG-01 [BLOCKING] · Every visible `<img>` resolves · no 404 · no missing src

- **Evaluate**: collect every `<img>.src`. For each, MCP `browser_network_requests` confirms a 200 response. Flag any 4xx/5xx.
- **Anchor**: imagery standard §1.

#### BRWS-IMG-02 [BLOCKING] · Hero and feature slots come from the curated pack

- **Evaluate**: src of `.cs-hero img` and the first feature image match URLs in the template's slot-0 and slot-1 pool entries. Zero Unsplash URLs for new pilots (Pragma grandfathered until the business-corporate retro-pack lands).
- **Anchor**: CS-IMG-SRC-01, AP3.

#### BRWS-IMG-03 [BLOCKING] · Subject match to the profession (3-second semantic check)

- **Evaluate**: for each of the 6 pool URLs, open the image, look for 3+ seconds, and answer: does a person in this profession recognize this as their world?
- **Rule**: any "no" is a fail. No compromise; this is the rule that caught PlayStation-gamepad-as-map-of-Rome and Bumble-Bee-tuna-as-artisan-ingredients. A Pexels URL with a perfect license is still wrong if the subject is wrong.
- **Anchor**: CS-IMG-COH-01, AP4.

#### BRWS-IMG-04 [BLOCKING] · Mood match to the voice anchor

- **Evaluate**: re-read the template's voice anchor (module docstring §5 / cluster blueprint §5). For each image, ask whether its mood (light, palette, posture) underlines or contradicts the anchor.
- **Rule**: contradicts = fail. "Il coaching non è terapia" + therapy couch = fail.
- **Anchor**: CS-IMG-COH-02, CS-IMG-COH-07.

#### BRWS-IMG-05 [REQUIRED] · No visible product placement · no brand logos in frame

- **Evaluate**: inspect each image for Apple glow, Starbucks cup, Nespresso pod, ThinkPad lid, Nike swoosh, gaming RGB.
- **Rule**: one or more = fail (exception: industry-association marquee logos, legitimately in scope).
- **Anchor**: CS-IMG-COH-04.

#### BRWS-IMG-06 [REQUIRED] · Portrait demographic spread is plausible for the Italian market

- **Evaluate**: examine the 3-6 leadership portraits together. Are they a single demographic? Flag mono-demographic lineups without an explicit rationale.
- **Anchor**: CS-IMG-COH-05.

#### BRWS-IMG-07 [REQUIRED] · Every image carries its caption + role + coherence justification in the pack file

- **Evaluate**: cross-reference the pack file at `docs/content-factory/imagery/packs/<cluster>.md` — every URL rendered on the page has a matching 3-field record (caption, slot role, coherence statement) in the pack.
- **Anchor**: CS-IMG-COH-06, CS-IMG-SRC-03.

#### BRWS-IMG-08 [REQUIRED] · Imagery reads editorial · not stock-plate

- **Evaluate**: semantic scan. Operational signals: natural light, specific setting, action posture, intentional composition. Fail signals: flat studio fill, white backdrop, centered-face smile, crossed-arms pose.
- **Anchor**: CS-IMG-PREM-01.

#### BRWS-IMG-09 [STRONG] · Hero and feature imagery imply motion

- **Evaluate**: hero + feature subjects should read mid-action (writing, reviewing, walking) rather than posed-static.
- **Anchor**: CS-IMG-DYN-01.

### 6.8 · Responsive behavior

#### BRWS-RESP-01 [BLOCKING] · At every viewport: no horizontal scroll · see BRWS-VIEW-02

#### BRWS-RESP-02 [BLOCKING] · 1100 px breakpoint active · see BRWS-VIEW-04

#### BRWS-RESP-03 [BLOCKING] · 720 px breakpoint active · see BRWS-VIEW-03

#### BRWS-RESP-04 [REQUIRED] · Card-grid images lock aspect-ratio with object-fit: cover

- **Evaluate**: inspect `.cs-pillars img`, `.cs-leadership img`, `.cs-cases img`. Computed `aspectRatio` is a fixed value (not `auto`); `objectFit: cover`.
- **Anchor**: CS-RESPONSIVE-05.

#### BRWS-RESP-05 [REQUIRED] · KPI band restacks at ≤ 720 · preserves tabular-nums

- **Evaluate**: at 390 × 844 the KPI band becomes 2×2 or 1×N; each stat keeps `.num` tabular-nums behavior.
- **Anchor**: CS-RESPONSIVE-04.

#### BRWS-RESP-06 [REQUIRED] · Focus-visible outline survives all viewports

- **Evaluate**: at 390 × 844, `Tab` through the first 6 focusable elements; each shows the gold outline.
- **Anchor**: CS-RESPONSIVE-07.

#### BRWS-RESP-07 [STRONG] · RTL tested at desktop + tablet + mobile viewports

- **Evaluate**: switch to AR; run the viewport matrix (at least 1440 / 768 / 390). Grid polarity flips correctly; hamburger opens from the expected side; locale switcher legible.
- **Anchor**: CS-RESPONSIVE-08, D3.

### 6.9 · Text / image alignment

#### BRWS-ALIGN-01 [REQUIRED] · Hero text block does not overlap the hero image

- **Evaluate**: at 1280 and 1024, screenshot the hero. Left-column bounding box does not overlap right-column image bounding box.

#### BRWS-ALIGN-02 [REQUIRED] · Section titles don't collide with card edges

- **Evaluate**: at 768 × 1024, inspect section headings relative to the card grid below. Titles sit above cards with the prescribed padding.

#### BRWS-ALIGN-03 [REQUIRED] · Leadership portraits align with name + title blocks below · no baseline drift across the row

- **Evaluate**: at 1280, visually confirm each portrait bottom edge sits on the same y-coordinate as its siblings, and the name+title blocks share a common baseline.

#### BRWS-ALIGN-04 [REQUIRED] · Image captions sit within the image frame · not floating into adjacent text

- **Evaluate**: hero credit overlay is positioned on the image; it does not shift into the left column text.

#### BRWS-ALIGN-05 [REQUIRED] · RTL alignment reverses correctly · text-align and flex-direction flip

- **Evaluate**: on the AR locale, the hero text column moves to the right; the photo to the left. Nav link flow reverses.
- **Anchor**: D3.

### 6.10 · Overall premium / professional feel

#### BRWS-FEEL-01 [BLOCKING] · Read as a real firm's site · not a template showcase

- **Evaluate**: mentally remove the studio name. Does the site still read as a real commercialista / advisory / coaching firm? Or does it read as "a template demo"?
- **Anchor**: CS-TONE-05, CS-MARKET-01, CS-MARKET-05.

#### BRWS-FEEL-02 [BLOCKING] · No editor affordances leak into the public `/live/` route

- **Evaluate**: load `/templates/<slug>/live/` in an incognito or cookie-cleared session. Confirm `body` does NOT have `mw-is-editor-preview`. Confirm no click-to-edit halos, no region selector highlights, no "edit zone" badges.
- **Anchor**: CS-MARKET-01, A5.

#### BRWS-FEEL-03 [BLOCKING] · No lorem ipsum · no "Replace this text" · no "Your headline here"

- **Evaluate**: text search across every page's rendered body. Flag any placeholder strings.
- **Anchor**: CS-MARKET-02, CS-MARKET-03.

#### BRWS-FEEL-04 [REQUIRED] · No marketing hyperbole · no banned phrases · no celebrity quotes

- **Evaluate**: grep rendered content for: "Unlock your potential", "Sblocca il tuo potenziale", "Trasforma la tua vita", "Versione migliore di te", "Mindset vincente", "Game-changing", "Einstein", "Jung", "Gandhi", "Steve Jobs", "10,000+ clients", "Trusted by".
- **Anchor**: CS-EXEC-04, AP9.

#### BRWS-FEEL-05 [REQUIRED] · Voice anchor appears and is preserved verbatim across all 5 locales

- **Evaluate**: grep the voice anchor line in each of the 5 locale renders. Must appear; must be the faithful translation, not a paraphrase.
- **Anchor**: CS-EXEC-01, F2.

#### BRWS-FEEL-06 [REQUIRED] · Credentials in leadership are cluster-specific and verifiable

- **Evaluate**: read each leadership `credentials` line. Must use cluster blueprint §4 vocabulary (ODCEC, Cassazionista, CONSOB, ICF PCC/MCC, …). No "Certified Life Transformation Expert".
- **Anchor**: CS-EXEC-03, AP9.

#### BRWS-FEEL-07 [STRONG] · Console is clean · no JavaScript errors during the walk

- **Evaluate**: `browser_console_messages` at the end of the walk. Zero `error`-level messages. `warn` acceptable only if explainable.
- **Anchor**: BRWS-TOOL-01.

#### BRWS-FEEL-08 [STRONG] · `prefers-reduced-motion` respected

- **Evaluate**: set `reduce` via `browser_evaluate` (`matchMedia('(prefers-reduced-motion: reduce)')`) or via an OS-level emulation. Reload the home page. No entrance animations fire; buttons have `transition: none`.
- **Anchor**: CS-RESPONSIVE-07, E2, AP12.

---

## 7 · Evidence collection format

### BRWS-EVID-01 [BLOCKING] · All evidence stored under `factory/reports/browser-verification/<template-slug>/<run-timestamp>/`

- **Directory layout** (required):
  ```
  factory/reports/browser-verification/<slug>/<run-timestamp>/
  ├─ verdict.md                    # the final verdict (template in §11)
  ├─ walk-log.md                   # chronological log with URLs + MCP call summaries
  ├─ screenshots/
  │  ├─ <locale>/<page>/<viewport>.png   # e.g., it/home/1440x900.png
  │  └─ … (one per locale × page × viewport in the walk scope)
  ├─ measurements.json             # structured DOM measurements per check
  └─ console.log                   # aggregated console output per page
  ```
- **Naming**: `<run-timestamp>` is ISO-8601 basic (`20260421T143055Z`). `<viewport>` is `WIDTHxHEIGHT` with no units. `<locale>` is two-letter ISO (`it`, `en`, `fr`, `es`, `ar`).

### BRWS-EVID-02 [BLOCKING] · Screenshot coverage is dense enough to reproduce the verdict

- **Minimum screenshots per template**: 5 locales × 6 pages × 4 core viewports (1440 / 1024 / 768 / 390) = **120 screenshots**. The remaining 4 viewports in the §5 matrix (1920 / 1280 / 414 / 640) are captured only for the home page in the default locale unless a check fails at the core-4 and requires triangulation.
- **Why this floor**: any blocking failure must be re-findable from the evidence alone. A verdict that says "hero stacks correctly" without a 390×844 screenshot of the home page for every locale cannot be audited.

### BRWS-EVID-03 [BLOCKING] · Every `[BLOCKING]` check has a measurement or a screenshot recording its pass/fail

- **Rule**: `measurements.json` keys by check tag (e.g., `BRWS-CONTRAST-01`) and stores the raw numbers the check produced (distance, ratio, computed styles). `screenshots/` carries a labeled image for every `[BLOCKING]` visual check. Both must be present for the verdict to stand.

### BRWS-EVID-04 [REQUIRED] · Walk log is chronological and reproducible

- **Rule**: `walk-log.md` opens with server URL + port + start time, then records every MCP call as `[HH:MM:SS] <tool> <args-summary> → <result-summary>`. A reviewer reading the log top-to-bottom can replay the walk exactly.

### BRWS-EVID-05 [REQUIRED] · Console log captured per page

- **Rule**: `console.log` captures `browser_console_messages` output grouped by page URL. Any `error` entry is cross-referenced in the verdict and must be resolved before flip.

### BRWS-EVID-06 [REQUIRED] · No evidence edits after verdict

- **Rule**: once `verdict.md` is written, the evidence directory is treated as immutable. If a retest is needed, a fresh `<run-timestamp>/` directory is created.
- **Why**: tier flips rely on an auditable artifact. Edits post-verdict destroy the audit trail.

---

## 8 · Pass / borderline / fail logic

The walk produces one of three outcomes. The rules below remove any ambiguity.

### 8.1 · PASS

- **Definition**: zero `[BLOCKING]` failures AND zero `[REQUIRED]` failures AND all viewport-matrix screenshots captured AND server URL + port recorded AND evidence directory complete.
- **Meaning**: the template may flip from `draft` to `published_live` in `TEMPLATE_REGISTRY.json`. The release-gatekeeper proceeds.
- **Note**: `[STRONG]` failures are allowed under PASS only if each is listed in `verdict.md § deviation` with a written justification. Anything listed in `§ deviation` must be reviewed by a second reviewer before the gatekeeper acts.

### 8.2 · BORDERLINE

- **Definition**: zero `[BLOCKING]` failures AND one or more `[REQUIRED]` failures AND all evidence captured.
- **Meaning**: the template does NOT flip to `published_live` on this walk. The verdict lists the `[REQUIRED]` failures as a remediation TODO. The draft may remain in `TEMPLATE_REGISTRY.json` at `draft` tier with a linked TODO; a follow-up walk on a branch containing the fixes must produce a PASS before flipping LIVE.
- **Why borderline is not pass**: `[REQUIRED]` rules encode quality invariants. Shipping with known `[REQUIRED]` regressions erodes the archetype over time.

### 8.3 · FAIL

- **Definition**: one or more `[BLOCKING]` failures. ANY single blocking failure = FAIL regardless of everything else.
- **Meaning**: the branch cannot merge to the integration branch. The verdict documents the blocking failure(s) with the captured evidence. The author fixes, a new walk runs, and the new walk produces a verdict against a fresh `<run-timestamp>`. No in-place patching of the old verdict.
- **Examples of FAIL triggers** (non-exhaustive · lifted from §6):
  - Hero h1 RGB distance to background < 120 (BRWS-CONTRAST-01 · Solaria AP1 class).
  - Horizontal scrollbar at any matrix viewport (BRWS-VIEW-02).
  - Hero does not stack at ≤ 720 (BRWS-VIEW-03).
  - Nav does not collapse at ≤ 720 (BRWS-VIEW-04).
  - Editor affordance visible on `/live/` (BRWS-FEEL-02).
  - "Replace this text" placeholder in rendered content (BRWS-FEEL-03).
  - Fake credential in leadership (BRWS-FEEL-06 / CS-EXEC-03).
  - Missing URL + port in the verdict (BRWS-SRV-02).
  - No recorded walk (CS-BROWSER-01).

### 8.4 · Scoring summary block (required in every verdict)

Every verdict includes a line-count summary of the three severity tiers:

```
[BLOCKING] total: <n> · failed: <k>
[REQUIRED] total: <n> · failed: <k>
[STRONG]   total: <n> · failed: <k>
[GUIDELINE] total: <n> · failed: <k>
```

The verdict is PASS if both `[BLOCKING]` and `[REQUIRED]` failed counts are 0. BORDERLINE if `[BLOCKING]` failed is 0 and `[REQUIRED]` failed ≥ 1. FAIL otherwise.

---

## 9 · Blocking issues · exhaustive list

Every occurrence of any item below is an automatic FAIL. This is the canonical list. No exceptions — if an instance surfaces that belongs here but is not yet enumerated, add it to this list AND fail the walk.

| # | Blocking issue | Rubric tag | Standard anchor | Incident anchor |
|---|---|---|---|---|
| 1 | `--primary` is a light color · h1..h5 invisible | BRWS-CONTRAST-01 | CS-PAL-01 | AP1 · Solaria `e8f38b5` |
| 2 | Dark-section child text uses `--ink` · dark-on-dark pocket | BRWS-CONTRAST-02 | CS-PAL-04 | AP11 |
| 3 | Horizontal scrollbar at any viewport | BRWS-VIEW-02 | CS-RESPONSIVE-02 | AP2 |
| 4 | Hero does not stack at ≤ 720 px | BRWS-VIEW-03 | CS-HERO-07 | AP2 |
| 5 | Nav does not collapse at ≤ 720 px | BRWS-VIEW-04 | CS-NAV-05 | AP2 |
| 6 | Hero uses 4-up grid or video background · not editorial photo | BRWS-HERO-02 | CS-HERO-01 | — |
| 7 | Hero has 3+ accent CTAs OR `href="#"` placeholder | BRWS-HERO-03 | CS-HERO-04 · CS-CTA-04 | — |
| 8 | Editor click-to-edit halo visible on `/live/` route | BRWS-FEEL-02 | CS-MARKET-01 | — |
| 9 | Lorem ipsum / "Replace this text" / "Your headline here" in rendered content | BRWS-FEEL-03 | CS-MARKET-02 · CS-MARKET-03 | — |
| 10 | Image URL 404s · missing `src` · broken hero | BRWS-IMG-01 | CS-IMG-SRC-01 | — |
| 11 | Hero image not from curated pack (Pexels for new pilots) | BRWS-IMG-02 | CS-IMG-SRC-01 · CS-HERO-02 | AP3 |
| 12 | Imagery subject mismatch (3-second check fails) | BRWS-IMG-03 | CS-IMG-COH-01 | AP4 · Session 31 |
| 13 | Imagery mood contradicts voice anchor | BRWS-IMG-04 | CS-IMG-COH-02 · CS-IMG-COH-07 | — |
| 14 | Navbar bg ≠ `--primary` · polarity broken | BRWS-NAV-01 | CS-PAL-06 · CS-NAV-01 | — |
| 15 | Navbar has > 1 accent element | BRWS-NAV-02 | CS-NAV-04 · CS-PAL-05 | — |
| 16 | Section wrapper padding crushed below `100px 72px` on desktop | BRWS-RHYTHM-01 | CS-RHYTHM-01 · CS-TONE-02 | — |
| 17 | Home section order wrong (e.g., cases before leadership) | BRWS-RHYTHM-02 | CS-RHYTHM-02 | — |
| 18 | Site reads as a template showcase · not a real firm | BRWS-FEEL-01 | CS-TONE-05 · CS-MARKET-* | — |
| 19 | Hero h1 AA contrast < 4.5 on paper | BRWS-CONTRAST-01 | CS-HERO-03 | — |
| 20 | Fake certification in leadership (CS-IMG-COH-03 contradicted by CS-EXEC-03) | BRWS-FEEL-06 | CS-EXEC-03 | AP9 |
| 21 | Voice anchor missing OR paraphrased in any of the 5 locales | BRWS-FEEL-05 | CS-EXEC-01 · F2 | — |
| 22 | D-054 10-gate differentiation absent from module docstring | (docstring grep during walk) | CS-EXEC-02 | — |
| 23 | Walk performed without recording dev-server URL + port | BRWS-SRV-02 | CS-BROWSER-02 | — |
| 24 | Walk missing ANY viewport in the §5 matrix | BRWS-VIEW-01 | CS-RESPONSIVE-01 | — |
| 25 | Evidence directory incomplete (missing screenshots, measurements, or walk-log) | BRWS-EVID-01/02/03 | CS-BROWSER-01 | — |

Any of the above = FAIL. Any appearance of a new defect that clearly belongs in this class = FAIL + add to the list.

---

## 10 · Reviewer checklist (pre-walk · during-walk · post-walk)

### 10.1 · Before the walk

- [ ] Branch is clean (`git status` shows only intentional changes).
- [ ] `manage.py check` → 0 issues.
- [ ] `manage.py test apps.catalog` → passing.
- [ ] `manage.py test apps` → passing.
- [ ] `scripts/check_imagery_pack.py` → passing (if touching imagery).
- [ ] Dev server started: `python manage.py runserver` on a deterministic port.
- [ ] **Server URL + port noted and shared with the user** so parallel verification can begin.
- [ ] Evidence directory created: `factory/reports/browser-verification/<slug>/<timestamp>/` with `screenshots/` subtree.
- [ ] Playwright MCP session open (or manual Chrome with DevTools ready).

### 10.2 · During the walk

- [ ] For each locale in the scope:
  - [ ] For each of the 6 skin pages (home · about · services · case_study_list · case_study_detail · contact):
    - [ ] Run the §5 viewport matrix.
    - [ ] At each viewport, execute the §6 check roster applicable to that page + viewport.
    - [ ] Capture screenshot under `screenshots/<locale>/<page>/<viewport>.png`.
    - [ ] Record measurements in `measurements.json` keyed by check tag.
    - [ ] Log the navigation + MCP calls in `walk-log.md`.
- [ ] Keyboard walk: `Tab`-through each page's first ~12 focusable elements; capture focus-visible behavior.
- [ ] Reduced-motion check: emulate `prefers-reduced-motion: reduce` on home; confirm no entrance animations fire.
- [ ] Console capture per page; aggregate into `console.log`.
- [ ] **Leave the server running throughout** — no restarts unless explicitly logged.

### 10.3 · After the walk

- [ ] Tally `[BLOCKING]` / `[REQUIRED]` / `[STRONG]` / `[GUIDELINE]` pass+fail counts (§8.4).
- [ ] Apply §8 pass / borderline / fail logic to compute the verdict.
- [ ] Write `verdict.md` using the §11 template.
- [ ] Cross-reference every failed check with its standard tag and (if applicable) its incident anchor (AP1 / AP2 / …).
- [ ] **Do not shut down the server** until the user has confirmed parallel verification OR explicitly released the walk (BRWS-SRV-04).
- [ ] If FAIL: open follow-up tasks naming each blocking issue. Do NOT edit in-place on a failing walk — new branch work + new walk.
- [ ] If PASS: release-gatekeeper may proceed to flip `TEMPLATE_REGISTRY.json` from `draft` to `published_live` (Commit B of the D-102 2-commit cadence).
- [ ] If BORDERLINE: log remediation TODOs; do not flip LIVE; schedule a re-walk.

---

## 11 · Final verdict template

Every walk produces one `verdict.md` file in its `<run-timestamp>` directory, using the template below exactly. Replace every `<placeholder>`. Do not delete any section — if a section is not applicable, mark it `— n/a —`.

```markdown
# Browser Live Verification Verdict · <template-slug>

**Verdict**: <PASS | BORDERLINE | FAIL>
**Template**: <slug> · <human name> · (<archetype>)
**Branch**: <branch-name>
**Baseline tip**: <commit-hash> (<commit-subject-line>)
**Walk run**: <run-timestamp>
**Reviewer**: <agent or human name>
**Walk type**: <Playwright MCP | manual Chrome | mixed + reason>

## Server

- **URL**: `http://127.0.0.1:<port>/`
- **Started at**: <ISO-8601>
- **Still running**: <yes | no + reason>
- **Restarts during walk**: <count · timestamps · reasons>

## Scope

- **Locales walked**: <it · en · fr · es · ar>
- **Pages walked**: <home · about · services · case_study_list · case_study_detail · contact>
- **Viewports walked**: <1920 · 1440 · 1280 · 1024 · 768 · 640 · 414 · 390>
- **Screenshots captured**: <count> (expected ≥ 120 per §7 core floor)
- **Evidence directory**: `factory/reports/browser-verification/<slug>/<run-timestamp>/`

## Summary counts

```
[BLOCKING]  total: <n>  failed: <k>
[REQUIRED]  total: <n>  failed: <k>
[STRONG]    total: <n>  failed: <k>
[GUIDELINE] total: <n>  failed: <k>
```

## Blocking failures (if any)

<for each blocking failure, a block:>

### <rubric-tag> · <one-line title>

- **Standard anchor**: <CS-* tag>
- **Incident anchor**: <AP* or — n/a —>
- **Observed**: <one-line raw finding with numbers>
- **Evidence**: `screenshots/<locale>/<page>/<viewport>.png` · `measurements.json#<key>`
- **Repro**: `GET http://127.0.0.1:<port>/<locale>/templates/<slug>/live/<page>/` at <viewport>

<… repeat …>

## Required failures (if any)

<same block structure>

## Strong / Guideline notes

<bullets; each cross-referenced to a standard tag>

## Deviations (for § deviation-tagged waivers · PASS only)

<one bullet per waived [STRONG] failure, with written justification>

## Imagery walk summary

- **Pool key**: `business-<kind>`
- **Pack file**: `docs/content-factory/imagery/packs/<cluster>.md`
- **URLs rendered · confirmed non-404**: <count>/6
- **Subject-match (3-second check)**: <pass · fail per slot>
- **Mood-match to voice anchor**: <pass · fail per slot>
- **Resolution floors met**: <yes | no per slot>

## Responsive walk summary

- **1100 px breakpoint active**: <yes | no>
- **720 px breakpoint active**: <yes | no>
- **Contact-form 880 px breakpoint active**: <yes | no>
- **Horizontal scroll at any viewport**: <no | list of viewport+page>
- **Hero h1 at 390 px**: <font-size in px>
- **Touch targets at 390 px ≥ 44×44**: <yes | list of failing selectors>

## Console summary

- **JS errors**: <count · first 3 summaries>
- **Warnings**: <count · noteworthy only>

## Next actions

<if PASS> Release-gatekeeper may proceed with Commit B (flip `TEMPLATE_REGISTRY.json` <slug> → `published_live`).
<if BORDERLINE> Open follow-up task(s): <list>. Schedule re-walk on remediation branch.
<if FAIL> Do NOT merge. Author fixes <list>. New branch walk required before re-verdict.

## Parallel-verification handshake

The dev server remains at `http://127.0.0.1:<port>/` and will stay running until the user confirms parallel verification in their own browser OR explicitly releases the walk.

— end of verdict —
```

---

## 12 · What this rubric deliberately does NOT do

- **It does not replace the design standard.** Every check here cross-references a rule in `corporate-suite-design-standard.md` or `corporate-suite-imagery-standard.md`. If a rule is ambiguous, the sibling standard is authoritative; this rubric defers.
- **It does not replace the test suite.** Tests run BEFORE the walk. A green test suite is a precondition, not a substitute. A red test suite means the walk does not run at all — CS-BROWSER-03.
- **It does not codify palette validation.** A pre-commit palette validator (CS-PAL-01 automated counterpart) is a separate hardening task. Until it lands, the walk catches palette-polarity inversions via BRWS-CONTRAST-01.
- **It does not unpause Solaria Commit B.** Solaria remains on branch `phase-x4-wave2-solaria-coaching-v1` at `6b70d56` with IT-only content. The EN/FR/ES/AR authoring remains paused until the hardening pass closes per the binding user instruction. When unpaused, Solaria will be the first template to pass through this rubric end-to-end.
- **It does not touch code outside `factory/*`.** This file is advisory + enforcement-protocol only. Any skin breakpoint additions, palette validator, or reduced-motion JS wiring live in follow-up steps.

---

## 13 · Summary

### Validation flow (in one sentence)

> **Run the tests · start the dev server · record URL + port · drive Playwright MCP through the §5 viewport matrix × 5 locales × 6 pages · apply the §6 check roster · collect §7 evidence · compute §8 verdict · keep the server running so the user can verify in parallel · write the §11 verdict — and only then let the release-gatekeeper consider flipping LIVE.**

### The most important blocking checks

If only a subset of checks could ever run, these are the non-negotiables — the ones that would have caught every shipped or near-shipped defect on this archetype to date:

1. **BRWS-CONTRAST-01** — `h1..h5` RGB distance ≥ 120 and WCAG contrast ≥ 4.5 vs background. The single check that would have caught Solaria's cream-primary bug in 10 seconds.
2. **BRWS-VIEW-02** — no horizontal scrollbar at any viewport in the §5 matrix. The check that exposes AP2 (zero real breakpoints in 6/7 skin files).
3. **BRWS-VIEW-03 + BRWS-VIEW-04** — hero stacks and nav collapses at ≤ 720 px. Without these, mobile is unusable.
4. **BRWS-IMG-03 + BRWS-IMG-04** — imagery subject + mood match the profession and the voice anchor. The checks that would have caught PlayStation-gamepad-as-map-of-Rome and every Session-31-class defect.
5. **BRWS-FEEL-02 + BRWS-FEEL-03** — no editor affordances, no lorem ipsum, no "Replace this text" in the public `/live/` route. The site must be a firm's site, not a template demo.
6. **BRWS-SRV-02** — server URL + port recorded in the verdict. No URL + port = no walk = no LIVE flip.

### Minimum evidence required before any template can be considered live-approved

A walk cannot produce a PASS verdict without ALL of the following in its `<run-timestamp>` evidence directory:

1. `verdict.md` following the §11 template, with `Verdict: PASS` on line 3 and zero `[BLOCKING]` + zero `[REQUIRED]` failures in the summary block.
2. `walk-log.md` opening with a real `http://127.0.0.1:<port>/` URL, an ISO-8601 start timestamp, and a chronological record of every MCP navigation and resize call.
3. `screenshots/` containing **at least 120 PNG files** per the §7 core floor (5 locales × 6 pages × 4 core viewports), each named `<locale>/<page>/<WIDTHxHEIGHT>.png`.
4. `measurements.json` with an entry per `[BLOCKING]` check keyed by rubric tag, carrying the raw numbers the check produced (contrast distance, scroll widths, computed styles, outline colors).
5. `console.log` capturing every page's console messages — zero `error`-level entries.
6. Confirmation in the verdict's "Parallel-verification handshake" section that the server **is still running** so the user can open the same URL + port in their own browser before the walk is considered closed.

Anything less = not live-approved. No exceptions. Every rule in this rubric was written because a CLI-green template shipped a defect that only a browser walk could see; the whole file is a refusal to let that happen again.
