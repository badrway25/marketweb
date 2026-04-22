# Corporate-suite Blocking Rules

**Phase**: X.4a · Corporate-suite Factory Hardening · **Date**: 2026-04-22
**Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Scope**: factory files only · no `apps/editor`, `apps/projects`, `apps/commerce` changes · no new archetypes · Solaria Commit B remains paused per user instruction.
**Inputs**: `factory/reports/audits/corporate-suite-audit-master.md`, `factory/standards/corporate-suite-design-standard.md`, `factory/standards/corporate-suite-imagery-standard.md`, `factory/standards/corporate-suite-browser-rubric.md`, `factory/standards/corporate-suite-quality-scorecard.md`, `factory/references/anti-pattern-library.md`.
**Audience**: every agent and human who decides whether a corporate-suite template may merge, may flip to `published_live`, or must loop back for rework — release-gatekeeper primarily, plus style-critic, contrast-accessibility-auditor, responsive-auditor, imagery-curator-reviewer, browser-verifier, and any reviewer signing off a PR against this archetype.

This file is the **enforcement layer**. The design standard says *what* premium looks like; the imagery standard says *what* imagery qualifies; the browser rubric says *how* to verify the render; the scorecard says *how* to score the result. **This document says what is not allowed to ship, how to detect it, how to escalate it, and how to decide between "block the merge" and "ship with a follow-up TODO."**

---

## 0 · How to use this document

1. **Every rule in this file that carries `[BLOCKING]` has a 1:1 counterpart in the design standard, imagery standard, browser rubric, or quality scorecard.** This document does not invent new blockers — it operationalizes the ones that already exist, with explicit detection commands, prevention recipes, and escalation paths.
2. Each blocking rule is tagged `CS-BLOCK-<nn>`. When another document references a blocker by this tag, the reader lands here for the enforcement recipe.
3. **Severity tags are shared across the standards family** (§2). The four levels (BLOCKING, REQUIRED, STRONG, GUIDELINE) are defined identically in every document in this suite; this file is the authoritative source for what each level *does to the merge and LIVE-flip decision*.
4. **The central premise**: 506/506 tests green is a NECESSARY, NOT a SUFFICIENT, ship signal. Every rule here was written because a CLI-green template already shipped (or almost shipped) a defect that a browser walk caught. Blocking is what prevents that class of false positive. Read §3 twice.
5. Pair this document with:
   - `corporate-suite-design-standard.md` (§2-§14 · rule source for every `CS-BLOCK-*`).
   - `corporate-suite-imagery-standard.md` (§1-§13 · rule source for every imagery blocker).
   - `corporate-suite-browser-rubric.md` (§6, §9 · detection recipes in Playwright MCP form).
   - `corporate-suite-quality-scorecard.md` (§4 · the 18 overrides that short-circuit the scorecard).
   - `factory/references/anti-pattern-library.md` (AP1-AP12 · the incident anchors).

---

## 1 · What is a blocking issue

### 1.1 · Operational definition

A **blocking issue** is a defect that:

1. **Changes what ships to the user**, not merely what a reviewer prefers. A cream-on-cream headline is invisible to the visitor; a 96 px section padding instead of the canonical 100 px is not.
2. **Cannot be detected by the deterministic CI surface** (`manage.py check`, `manage.py test apps`, `manage.py test apps.catalog`, `scripts/check_imagery_pack.py`, `generate_previews`) with sufficient reliability. The repo has 506+ apps tests and none of them caught AP1 (Solaria palette inversion), AP2 (zero real breakpoints), or AP4/AP5 (PlayStation gamepad as "map of Rome"). A defect that slips the CI surface AND ships to a user is exactly the false-positive class this document exists to prevent.
3. **Breaks one of the archetype's load-bearing invariants** — dark-foreground polarity, responsive coverage, editorial imagery semantics, voice-anchor preservation, the "real firm's site, not a template demo" promise. Each of these is codified in the design/imagery/rubric family; blocking rules are the enforcement hand on those invariants.
4. **Has a documented repo incident OR a plausible near-miss** behind it. This document does not speculate. Every blocker cites AP1-AP12 or a specific `CS-*` / `BRWS-*` rule authored from a real audit finding.

If a defect fails criteria 1 AND 2 AND 3, it is blocking. If it only fails criterion 4 (rule deemed important but with no evidence yet), it goes in as `[REQUIRED]` until an incident upgrades it.

### 1.2 · What is NOT a blocking issue

- **Taste differences**: "I would have picked a different accent color." A choice inside the sanctioned palette token is not a blocker.
- **Micro drift**: `96 px 72 px` section padding instead of `100 px 72 px`. The rhythm is disturbed but the page is not broken. Follow-up.
- **Density in the acceptable band**: 5 KPI stats instead of 3-4. Drift, not breakage.
- **Pre-factory legacy state**: Pragma's Unsplash pack (AP3) is tracked for retro-curation, is not blocked from staying LIVE as-is, but *does* block any new pilot that tries to introduce non-Pexels URLs.
- **Known skin issues already tracked as hardening work**: `--primary-2: #2c3e6b` hardcode (AP7) — a `[STRONG]` drift with a hardening TODO, not a ship gate.

These distinctions matter because calling everything blocking devalues the word. Blocking is the nuclear option. Use it only when the defect changes the visitor's experience in a way tests cannot catch.

### 1.3 · The CLI false-positive prevention premise

> **A template that passes `manage.py check` + `manage.py test apps` + `manage.py test apps.catalog` + `generate_previews` + `scripts/check_imagery_pack.py` has not yet earned the right to flip LIVE.**

This is restated from the browser rubric §2 because this document is the moment of enforcement. Every blocking rule below was written because:

- The deterministic test surface cannot render the page.
- The deterministic test surface cannot inspect computed style.
- The deterministic test surface cannot resize the viewport.
- The deterministic test surface cannot open an image URL and ask "does a commercialista recognize this as their world?"
- The deterministic test surface cannot distinguish "L'adempimento corretto" from "Unlock your potential."

**Every enforcement recipe in §4-§17 below pairs a detection command or a rubric check with a prevention command. A reviewer who only runs the CI surface and claims PASS is waived into the same class of false positive that Solaria caught in 30 minutes of browser walk.**

---

## 2 · Severity model

### 2.1 · Four severity levels

The four tags are used identically across the design standard, imagery standard, browser rubric, quality scorecard, and this document. This section is the authoritative statement of what each level does to the ship decision.

| Tag | Meaning | Merge decision | LIVE-flip decision | Follow-up |
|---|---|---|---|---|
| **`[BLOCKING]`** | Violation prevents the template from reaching production in any form that would be visible to a user as broken. | **Blocks merge** if the defect is on the current PR. A draft merge is allowed ONLY if the defect is already latent on main and this PR does not make it worse; otherwise the PR goes back. | **Blocks flip** unconditionally. `TEMPLATE_REGISTRY.json` stays at `draft`. | Remediation is the next PR; no "ship and fix later." |
| **`[REQUIRED]`** | Violation must be fixed before the reviewer walk signs off. | Draft merge allowed with a linked TODO. Merge against main requires the TODO to be either resolved in-PR or explicitly tracked as a follow-up issue. | **Blocks flip** to LIVE. Remains at `draft`. The follow-up PR must close the TODO. | Allowed as a tracked task in the same sprint. |
| **`[STRONG]`** | Violation allowed ONLY with a written `§ deviation` justification referenced in the module docstring or the walk verdict. | Allowed to merge with deviation note. | Allowed to flip LIVE only if the deviation is reviewed by a second reviewer. | Tracked as archetype debt; may roll into the next hardening pass. |
| **`[GUIDELINE]`** | Taste; document the reason if you break it. | No merge impact. | No LIVE-flip impact. | Optional polish. |

### 2.2 · Why the two-axis decision (merge vs LIVE-flip)

The D-102 two-commit cadence separates "land the code on the integration branch" (Commit A) from "flip the registry to `published_live`" (Commit B). This document respects that separation.

- **Commit A (draft-landing)** — allowed when `[BLOCKING]` rules on the current diff are clean. A `[REQUIRED]` gap can land with an open TODO, because the registry stays at `draft` and nothing user-facing is promoted.
- **Commit B (LIVE flip)** — allowed only when the full rubric walk PASSes and the scorecard clears Layer 1 / 2 / 3 (scorecard §4-§6). Any `[BLOCKING]` or `[REQUIRED]` remaining blocks Commit B.

A defect that is blocking for LIVE but not for draft-landing goes on Commit B's list. A defect that is blocking even for draft-landing (e.g., a hero that 404s globally; a PR that introduces non-Pexels URLs) goes back before any merge.

### 2.3 · Escalation path (summary · detail in §18)

If a reviewer is unsure whether a defect is BLOCKING or REQUIRED, default to the stricter tag and escalate to the release-gatekeeper or the user. The cost of a false negative (ship a Solaria-class defect) is strictly higher than the cost of a false positive (one extra walk). When in doubt, BLOCK.

---

## 3 · The 18 hard blockers (1:1 with scorecard overrides)

These are the explicit, enumerated, non-negotiable blockers. Any single occurrence of any item below = **FAIL** the walk, **BLOCK** the LIVE flip, and (for items marked ✱) **BLOCK the merge** before draft-landing. Every item below maps 1:1 to a scorecard Layer-1 override (`O1`-`O18` · `corporate-suite-quality-scorecard.md` §4).

| Tag | Blocker | Merge block? | LIVE block? | Scorecard override | Standard anchor | Incident anchor |
|---|---|:-:|:-:|:-:|---|---|
| **CS-BLOCK-01** | `h1..h5` RGB distance < 120 OR WCAG contrast < 4.5 vs background on any page × any locale. | ✱ | ✱ | O1 | CS-PAL-01 · CS-HERO-03 · BRWS-CONTRAST-01 | AP1 · Solaria `e8f38b5` |
| **CS-BLOCK-02** | Horizontal scrollbar at any §5 rubric viewport (1920 / 1440 / 1280 / 1024 / 768 / 640 / 414 / 390). | ✱ | ✱ | O2 | CS-RESPONSIVE-02 · BRWS-VIEW-02 | AP2 |
| **CS-BLOCK-03** | Hero does not stack OR nav does not collapse at ≤ 720 px. | ✱ | ✱ | O3 | CS-HERO-07 · CS-NAV-05 · BRWS-VIEW-03/04 | AP2 |
| **CS-BLOCK-04** | Any imagery URL 404s on the live render. | ✱ | ✱ | O4 | CS-IMG-SRC-01 · BRWS-IMG-01 | — |
| **CS-BLOCK-05** | Imagery fails 3-second subject check on any slot (PlayStation gamepad as "map of Rome" class). |  | ✱ | O5 | CS-IMG-COH-01 · BRWS-IMG-03 | AP4 · Session 31 |
| **CS-BLOCK-06** | Imagery mood contradicts voice anchor (e.g., coaching anchor "not therapy" + therapy couch). |  | ✱ | O6 | CS-IMG-COH-02 · CS-IMG-COH-07 · BRWS-IMG-04 | AP5 |
| **CS-BLOCK-07** | Any non-Pexels URL on a NEW pilot (Pragma legacy Unsplash is the single tolerated exception). | ✱ | ✱ | O7 | CS-IMG-SRC-01 · BRWS-IMG-02 | AP3 |
| **CS-BLOCK-08** | Editor click-to-edit affordance visible on the public `/live/` route (cookie-cleared session). | ✱ | ✱ | O8 | CS-MARKET-01 · BRWS-FEEL-02 | — |
| **CS-BLOCK-09** | Lorem ipsum / "Replace this text" / "Your headline here" in rendered content. | ✱ | ✱ | O9 | CS-MARKET-02 · CS-MARKET-03 · BRWS-FEEL-03 | — |
| **CS-BLOCK-10** | Fake certification in leadership (e.g., "Certified Life Transformation Expert"). | ✱ | ✱ | O10 | CS-EXEC-03 · BRWS-FEEL-06 | AP9 |
| **CS-BLOCK-11** | Voice anchor missing or paraphrased in ANY of the 5 locales. |  | ✱ | O11 | CS-EXEC-01 · F2 · BRWS-FEEL-05 | — |
| **CS-BLOCK-12** | D-054 10-gate differentiation absent from module docstring OR not triangulated against EVERY sibling on the archetype. | ✱ | ✱ | O12 | CS-EXEC-02 | — |
| **CS-BLOCK-13** | Walk performed without recording dev-server URL + port in the verdict. |  | ✱ | O13 | CS-BROWSER-02 · BRWS-SRV-02 | — |
| **CS-BLOCK-14** | Walk missing ANY viewport from the §5 rubric matrix. |  | ✱ | O14 | CS-RESPONSIVE-01 · BRWS-VIEW-01 | — |
| **CS-BLOCK-15** | Evidence directory incomplete (screenshots below floor, missing `measurements.json`, missing `walk-log.md`). |  | ✱ | O15 | CS-BROWSER-01 · BRWS-EVID-01..03 | — |
| **CS-BLOCK-16** | Nav background ≠ `--primary` (polarity broken) OR more than one accent element in nav. | ✱ | ✱ | O16 | CS-PAL-06 · CS-NAV-01 · CS-NAV-04 · BRWS-NAV-01/02 | — |
| **CS-BLOCK-17** | Dark-section child text renders dark-on-dark (distance < 120 OR WCAG < 4.5 inside `.cs-section.dark` / `.cs-kpi-band` / dark `.cs-foot`). | ✱ | ✱ | O17 | CS-PAL-04 · BRWS-CONTRAST-02 | AP11 |
| **CS-BLOCK-18** | No live browser walk performed at all (test-only ship). |  | ✱ | O18 | CS-BROWSER-01 · AP8 | AP8 |

**Notes on the ✱ column**:

- **✱ merge-block**: defect introduces or aggravates the blocker *on the current diff*. E.g., CS-BLOCK-01 is a merge-block when the PR adds a new template whose palette inverts polarity. It is NOT a merge-block for pre-existing latent cases (Pragma's Unsplash pack predates the factory and is grandfathered under CS-BLOCK-07).
- **✱ LIVE-block**: the defect, in any form, blocks `TEMPLATE_REGISTRY.json` from flipping the template to `published_live`.
- Items without ✱ in the merge column are still LIVE-blocks; they are less restrictive at draft-landing because the fix is (e.g.) re-run the walk and record the URL, not re-author the template.

§4-§17 below are the category-by-category enforcement recipes for each family of blocker above. §18-§21 cover escalation, merge-vs-follow-up decision logic, the CLI false-positive defense, and the summary.

---

## 4 · Readability failure blockers

Readability = the visitor can read the page. If they cannot, nothing else the archetype does matters.

### CS-BLOCK-R-01 [BLOCKING] · `h1..h5` invisibility on paper (AP1 Solaria class)

- **Definition**: any `h1`, `h2`, `h3`, `h4`, or `h5` on any page of any locale renders with RGB distance < 120 against its immediate background OR WCAG contrast < 4.5:1. Hero h1 has a tighter floor — AA 4.5:1 is the absolute floor; AAA 7.0:1 is the target.
- **Why it blocks**: Solaria (`e8f38b5`) shipped cream `--primary` on cream `--paper`. Every headline on every page rendered distance ~6, ratio ~1.02. 506/506 tests passed. A visitor could not read the page. Fixed in `6b70d56`.
- **Detection** (browser walk · primary):
  ```js
  // Run via mcp__plugin_playwright_playwright__browser_evaluate
  (() => {
    const toRGB = (c) => c.match(/\d+/g).map(Number);
    const dist = (a, b) => Math.hypot(a[0]-b[0], a[1]-b[1], a[2]-b[2]);
    const body = toRGB(getComputedStyle(document.body).backgroundColor);
    return Array.from(document.querySelectorAll('h1,h2,h3,h4,h5'))
      .map(h => ({
        tag: h.tagName,
        text: h.textContent.slice(0, 40),
        color: getComputedStyle(h).color,
        distance: dist(toRGB(getComputedStyle(h).color), body),
      }))
      .filter(r => r.distance < 120);
  })()
  ```
  Any row in the returned array = fail.
- **Detection** (static · secondary):
  ```bash
  # Inspect the seeded palette primary against cream paper
  python manage.py shell -c "from apps.catalog.models import TemplateBrand; \
    b = TemplateBrand.objects.get(template__slug='<slug>'); \
    print(b.palette.primary)"
  ```
  If the hex's perceived lightness (L\* in CIELAB against `#F7F4EC`) > 40, flag.
- **Prevention**: `seed_templates.py` must carry the 8-line "primary is dark" comment block (`6b70d56`). Any new palette goes through an L\* check before advancing to tier > `draft`. A palette validator (X.4a Step N+) rejects a `published_live` flip when `primary` L\* > 40.
- **Merge decision**: **block the PR** if this defect is introduced by the diff. If the PR is pure docs/refactor and the defect is latent on main, still block the LIVE flip but allow the merge.
- **LIVE-flip decision**: **block unconditionally**. A LIVE template with this defect is broken for every visitor.
- **Escalation**: release-gatekeeper consults the user; walk verdict FAIL; new branch required with palette fix; re-walk mandatory.
- **Anchors**: CS-BLOCK-01 · CS-PAL-01 · CS-HERO-03 · BRWS-CONTRAST-01 · AP1.

### CS-BLOCK-R-02 [BLOCKING] · Hero h1 unreadable at any responsive viewport

- **Definition**: at the `390 × 844` viewport `.cs-hero h1` computed `font-size` < 32 px, OR h1 overlaps the hero photo at any desktop viewport, OR h1 truncates/clips at any viewport in the rubric matrix.
- **Why it blocks**: mobile users get a crushed headline; desktop users get overlapping image + text. Either makes the first fold unreadable.
- **Detection** (browser walk):
  ```js
  browser_resize({ width: 390, height: 844 });
  browser_evaluate(() => getComputedStyle(document.querySelector('.cs-hero h1')).fontSize);
  // Must return a value ≥ 32px
  ```
  Overlap check: `browser_take_screenshot` at 1280 × 800, visually verify left text column does not bleed into right image column.
- **Prevention**: `_base.html` carries the `@media (max-width: 720px)` block where hero h1 is re-scaled to a 32-48 px floor. The hardening pass adds this breakpoint; until it does, EVERY new pilot is at risk (AP2 class).
- **Merge decision**: block merge if the PR lands new template content that demonstrably fails at 390 px. Allow merge if the PR is unrelated infrastructure and the defect is latent.
- **LIVE-flip decision**: block unconditionally.
- **Anchors**: CS-HERO-07 · CS-RESPONSIVE-03 · BRWS-VIEW-06 · BRWS-READ-01.

### CS-BLOCK-R-03 [BLOCKING] · Rendered body copy contains placeholder strings

- **Definition**: any public-facing page renders `lorem ipsum`, "Replace this text", "Your headline here", "Insert subtitle", "Click to edit", or any synonym.
- **Why it blocks**: a visitor sees author-facing scaffolding. The "real firm's site" promise (CS-TONE-05 / CS-MARKET-02/03) collapses.
- **Detection**:
  ```bash
  # On the live render
  curl -s http://127.0.0.1:<port>/it/templates/<slug>/live/ \
    | grep -iE 'lorem|replace this|your headline|insert subtitle|click to edit'
  ```
  Also: browser walk search across home/about/services/case-list/case-detail/contact in every locale.
- **Prevention**: cluster-blueprint-driven content authoring; author-facing strings live in `apps/editor/schema.py` (editor UI), NEVER in `template_content_<name>.py` (rendered content).
- **Merge decision**: block the PR.
- **LIVE-flip decision**: block unconditionally.
- **Anchors**: CS-BLOCK-09 · CS-MARKET-02 · CS-MARKET-03 · BRWS-FEEL-03.

---

## 5 · Unsafe contrast blockers

Readability is macro — "can the visitor read?" Contrast is micro — "is each text node in compliance?" This section enumerates the specific contrast-safety blockers beyond the headline-wide check in §4.

### CS-BLOCK-C-01 [BLOCKING] · Dark-on-dark pockets (AP11)

- **Definition**: any text, button, or bordered element inside `.cs-section.dark`, `.cs-kpi-band`, dark `.cs-foot`, or `.cs-nav` has RGB distance < 120 OR WCAG contrast < 4.5 against its surface.
- **Why it blocks**: scoped AP1 class. A new child element inside a dark section picks `--ink` by default instead of `--on-dark`; tests miss it; a reviewer scrolling past in cream mode misses it; a visitor on the dark band cannot see the text.
- **Detection** (browser walk):
  ```js
  browser_evaluate(() => {
    const toRGB = (c) => c.match(/\d+/g).map(Number);
    const dist = (a, b) => Math.hypot(a[0]-b[0], a[1]-b[1], a[2]-b[2]);
    const results = [];
    document.querySelectorAll('.cs-section.dark, .cs-kpi-band, .cs-nav, .cs-foot').forEach(section => {
      const sectionBg = toRGB(getComputedStyle(section).backgroundColor);
      section.querySelectorAll('*').forEach(el => {
        if (!el.textContent.trim()) return;
        const fg = toRGB(getComputedStyle(el).color);
        const d = dist(fg, sectionBg);
        if (d < 120) results.push({ sel: el.tagName, text: el.textContent.slice(0, 30), distance: d });
      });
    });
    return results;
  })
  ```
- **Prevention**: every new dark-section child CSS rule inherits from `.cs-section.dark *` which sets `color: var(--on-dark)` by default. Authors override explicitly only with `--on-dark-2` or `--on-dark-3`, never with `--ink`.
- **Merge decision**: block merge if the PR adds the offending dark-section rule.
- **LIVE-flip decision**: block unconditionally.
- **Anchors**: CS-BLOCK-17 · CS-PAL-04 · BRWS-CONTRAST-02 · AP11.

### CS-BLOCK-C-02 [BLOCKING] · Navbar text below WCAG AA

- **Definition**: any `.cs-nav` text node has WCAG contrast < 4.5 against the nav background in default state. Hover and active states also must clear AA.
- **Why it blocks**: nav is the first thing every visitor reads on every page. A nav below AA = archetype-wide defect.
- **Detection**:
  ```js
  browser_evaluate(() => {
    // pseudocode — compute luminance + WCAG contrast for every .cs-nav a, .cs-nav .wm, .cs-nav button
    const nav = document.querySelector('.cs-nav');
    const bg = getComputedStyle(nav).backgroundColor;
    return Array.from(nav.querySelectorAll('a, .wm, button'))
      .map(el => ({ text: el.textContent.slice(0, 30), color: getComputedStyle(el).color, bg }));
  })
  ```
  Feed the color pairs into a WCAG contrast calculator; flag any < 4.5.
- **Prevention**: CS-PAL-06 (nav bg = `--primary`) + CS-NAV-02 (default `--on-dark-2`, hover `--on-dark`) together produce AA. Keep the contract.
- **Merge decision**: block if the PR muddies nav colors.
- **LIVE-flip decision**: block unconditionally.
- **Anchors**: CS-NAV-02 · CS-PAL-06 · BRWS-CONTRAST-03.

### CS-BLOCK-C-03 [BLOCKING] · Hero h1 fails AAA target AND AA floor

- **Definition**: hero h1 vs cream paper WCAG ratio < 4.5 (AA floor). A < 7.0 AAA miss is `[REQUIRED]`, not blocking; < 4.5 AA fail is blocking.
- **Why it blocks**: if the hero headline is below AA, the first fold is unreadable for low-vision visitors — a WCAG 2.1 AA violation.
- **Detection**: see CS-BLOCK-R-01 detection snippet; filter to `h.tagName === 'H1'` and check ratio explicitly.
- **Prevention**: palette `primary` passes L\* ≤ 40 on cream (CS-PAL-01) → AA automatic. AAA is achieved when L\* ≤ ~25 (Pragma charcoal-blue, Fiscus graphite, Solaria-post-fix dark carbon all do).
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-HERO-03 · CS-BLOCK-01 · BRWS-CONTRAST-01.

---

## 6 · Navbar / accent visibility blockers

The nav is the template's voice at its most concentrated — palette, typography, restraint, and dark polarity compressed into 80 px of height. If any of those break, the archetype reads wrong before the visitor scrolls.

### CS-BLOCK-N-01 [BLOCKING] · Nav polarity inverted (nav bg ≠ `--primary`)

- **Definition**: `getComputedStyle('.cs-nav').backgroundColor` does not resolve to the seeded palette's `primary` hex.
- **Why it blocks**: a cream nav on cream body vanishes on scroll. A dark nav on a dark hero also vanishes. The skin contract is "nav = `--primary`, body = cream." Break it and the visual system breaks.
- **Detection** (browser walk):
  ```js
  browser_evaluate(() => getComputedStyle(document.querySelector('.cs-nav')).backgroundColor)
  // Compare against the seeded primary (look up in SEED_TEMPLATES)
  ```
- **Prevention**: `_base.html:130` has `.cs-nav { background: var(--primary); }` hardcoded. Overriding this in a template-specific CSS block requires a `§ deviation` note in the design-standard `[STRONG]` sense; attempting it without one is a block.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-16 · CS-PAL-06 · CS-NAV-01 · BRWS-NAV-01.

### CS-BLOCK-N-02 [BLOCKING] · More than one accent element in the navbar

- **Definition**: count of `.cs-nav` child elements whose computed `backgroundColor`, `borderColor`, or `color` resolves to `--accent` is > 1.
- **Why it blocks**: the nav accent is the archetype's punctuation — ONE trailing CTA. Multiple accent hits (accent-colored wordmark + accent dividers + accent CTA) read consumer-tech / SaaS, not advisory.
- **Detection**:
  ```js
  browser_evaluate(() => {
    const accent = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim();
    const nav = document.querySelector('.cs-nav');
    return Array.from(nav.querySelectorAll('*')).filter(el => {
      const s = getComputedStyle(el);
      return [s.backgroundColor, s.borderColor, s.color].some(c => c.includes(accent));
    }).length;
  })
  // Must return exactly 1
  ```
- **Prevention**: CS-NAV-04 (nav CTA is the only accent) + CS-PAL-05 (accent as punctuation, ≤ 2-3 per viewport) enforced by visual review. The hardening pass should add a CSS rule that limits `.cs-nav` accent descendants to the CTA selector.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-16 · CS-NAV-04 · CS-PAL-05 · BRWS-NAV-02 · BRWS-NAV-05.

### CS-BLOCK-N-03 [BLOCKING] · Nav does not condense at 1100 px OR collapse to hamburger at 720 px

- **Definition**: at 1024 × 768 nav links do not tighten; at 390 × 844 nav does not collapse to a menu trigger.
- **Why it blocks**: mobile users cannot navigate; tablet users see an oversized nav that eats the first fold.
- **Detection** (browser walk): `browser_resize` through the rubric matrix; `browser_snapshot` at each; visually confirm nav state per viewport. Also check `browser_evaluate(() => getComputedStyle(document.querySelector('.cs-nav .cs-nav__links')).display)` changes correctly across breakpoints.
- **Prevention**: `_base.html` `@media (max-width: 1100px)` + `@media (max-width: 720px)` blocks. The archetype hardening pass adds these (currently AP2 gap).
- **Merge decision**: block merge if the PR promotes a template to LIVE without the breakpoints; allow merge of infrastructure changes that don't touch the nav.
- **LIVE-flip decision**: block unconditionally.
- **Anchors**: CS-BLOCK-03 · CS-NAV-05 · BRWS-VIEW-04.

### CS-BLOCK-N-04 [BLOCKING] · Focus-visible ring is browser-default blue, not the gold accent

- **Definition**: keyboard `Tab` through nav links produces `outline-color: rgb(0, 95, 204)` (Chrome default blue) or equivalent browser-default, instead of `var(--accent)`.
- **Why it blocks**: the E1 pattern (gold `:focus-visible` outline) is the archetype's accessibility signature. Browser-default blue reads like an unstyled site.
- **Detection** (browser walk): `browser_press_key({ key: 'Tab' })`; `browser_evaluate(() => document.activeElement.matches(':focus-visible') && getComputedStyle(document.activeElement).outlineColor)`.
- **Prevention**: `_base.html` carries the `:focus-visible { outline: 2px solid var(--accent); outline-offset: 4px; }` cascade. Removing it is a `[BLOCKING]` regression.
- **Merge decision**: block if the diff removes or overrides the rule.
- **LIVE-flip decision**: block.
- **Anchors**: CS-NAV-02 · E1 · BRWS-CONTRAST-04.

---

## 7 · Hero readability / premium feel blockers

The hero is the first fold. Every archetype-scale rule converges here.

### CS-BLOCK-H-01 [BLOCKING] · Hero shows a 4-up grid / video background / gradient-only hero

- **Definition**: `.cs-hero` right column is NOT a single full-bleed Pexels photo. The skin contract (`home.html:5-67`) is ONE photo, full-bleed, slot 0 of the pool.
- **Why it blocks**: a photo grid reads as template-marketplace; a video background reads as SaaS; a gradient-only hero reads as unfinished.
- **Detection** (browser walk): `browser_evaluate(() => document.querySelectorAll('.cs-hero img, .cs-hero video').length)` — must be 1 (one img), 0 videos. Visual confirmation of full-bleed right column.
- **Prevention**: `home.html` hardcodes the hero composition. Authors customize via `template_content_<name>.py` slot 0 URL, not via template markup.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-HERO-01 · CS-HERO-02 · BRWS-HERO-02.

### CS-BLOCK-H-02 [BLOCKING] · Hero has 3+ CTAs or `href="#"` placeholder

- **Definition**: count of accent-filled buttons inside `.cs-hero` > 1, OR count of ghost/outline secondary > 1, OR any CTA's `href` is `"#"` / `"#contact"` / `""`.
- **Why it blocks**: three CTAs reads as funnel; broken `href` breaks the visitor's first action.
- **Detection**:
  ```js
  browser_evaluate(() => {
    const ctas = Array.from(document.querySelectorAll('.cs-hero a, .cs-hero button'));
    return ctas.map(c => ({ text: c.textContent.trim(), href: c.getAttribute('href') }));
  })
  ```
  Inspect counts and hrefs.
- **Prevention**: cluster blueprint §7 prescribes ONE primary CTA per section; the hero carries one accent + at most one ghost.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-HERO-04 · CS-CTA-01 · CS-CTA-04 · BRWS-HERO-03.

### CS-BLOCK-H-03 [BLOCKING] · Hero face stares directly at camera (editorial failure)

- **Definition**: slot 0 hero photo shows a subject's face directly at the camera with a full-face smile. Three-quarter and profile views are fine; mid-action is ideal.
- **Why it blocks**: direct-gaze + smile = corporate-headshot stock = collapses the editorial premium read.
- **Detection**: visual review during pack curation (CURATION_PROTOCOL §3.3) + browser walk (BRWS-IMG-08). Single pass per slot.
- **Prevention**: curator applies CS-IMG-HERO-05 during selection. Any direct-gaze hero requires `§ deviation` in the pack file.
- **Merge decision**: block if the PR introduces the offending URL.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-HERO-05 · CS-IMG-PREM-01 · BRWS-IMG-08.

### CS-BLOCK-H-04 [BLOCKING] · Hero subject does not survive 4:3 desktop ↔ 16:9 mobile crop

- **Definition**: at 1440 × 900 desktop (4:3 right-column render) the hero subject is on-frame; at 390 × 844 mobile stacked (16:9) the same URL crops out the subject.
- **Why it blocks**: `object-fit: cover` with aspect-ratio lock (CS-RESPONSIVE-05) means the crop is automatic; a URL whose subject sits at the edge of the frame gets truncated on one of the two renders.
- **Detection**: `browser_resize` at 1440 and 390; `browser_take_screenshot` of the hero at both; visually verify subject presence.
- **Prevention**: curator applies CS-IMG-CROP-01 during selection. Mentally crop the URL at 4:3 and 16:9 before approval.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-CROP-01 · CS-RESPONSIVE-05 · BRWS-HERO-06.

### CS-BLOCK-H-05 [BLOCKING] · Hero meta-strip absent OR carries marketing hyperbole

- **Definition**: hero lacks the 2-4 credential-anchor meta-strip, OR the meta-strip contains banned phrases ("Trusted by 10,000+", "Unlock your potential", "Game-changing").
- **Why it blocks**: the meta-strip is where professional credibility anchors (ODCEC, Cassazionista, CONSOB, ICF PCC). Without it, the hero reads funnel; with hyperbole, the hero reads consumer-marketing.
- **Detection**: grep the rendered hero DOM for banned phrases (BRWS-FEEL-04 regex list); count meta-strip entries (BRWS-HERO-04).
- **Prevention**: cluster blueprint §4 terminology dictionary; `template_content_<name>.py` docstring enumerates banned phrases.
- **Merge decision**: block if the PR introduces or allows hyperbole.
- **LIVE-flip decision**: block.
- **Anchors**: CS-HERO-06 · CS-EXEC-04 · BRWS-HERO-04 · BRWS-FEEL-04 · AP9.

---

## 8 · Premium feel blockers (the "real firm, not a template demo" test)

The archetype claim is ultra-premium / editorial / advisory. If the rendered page could plausibly be mistaken for a template showcase, a SaaS landing page, or a coaching funnel, the claim fails.

### CS-BLOCK-P-01 [BLOCKING] · Editor affordances leak into public `/live/` route

- **Definition**: on `http://127.0.0.1:<port>/<locale>/templates/<slug>/live/` in a cookie-cleared incognito session, any click-to-edit halo, region-selector highlight, or "edit zone" badge is visible.
- **Why it blocks**: the "real firm's site" promise collapses. The visitor sees authoring UI.
- **Detection**:
  ```js
  browser_evaluate(() => ({
    hasEditorClass: document.body.classList.contains('mw-is-editor-preview'),
    editHalos: document.querySelectorAll('[data-mw-edit-region], .mw-edit-halo, .mw-region-selector').length,
  }))
  ```
  Both must be false / zero on `/live/`.
- **Prevention**: `_base.html:441-452` gates editor affordances behind `body.mw-is-editor-preview`. The public live route does not add the class; the editor preview route does.
- **Merge decision**: block if the PR removes the gate or inverts the guard.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-08 · CS-MARKET-01 · A5 · BRWS-FEEL-02.

### CS-BLOCK-P-02 [BLOCKING] · Fake certification in leadership (AP9)

- **Definition**: leadership `credentials` contains phrases like "Certified Life Transformation Expert", "Licensed Abundance Coach", "Accredited Wellness Visionary" — credentials that do not map to a real professional register.
- **Why it blocks**: ethics before design. Fake credentials expose the firm (and the marketplace) to legal risk.
- **Detection**: grep leadership entries per locale; cross-reference against cluster blueprint §4 terminology dictionary. Any entry not in {ODCEC, Cassazionista, Revisore Legale, Albo Avvocati, CONSOB, ABI, ICF PCC, ICF MCC, EMCC Senior Practitioner, AICP, …} = flag for review.
- **Prevention**: CS-EXEC-03 binding; cluster blueprint §4 is the vocabulary source.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-10 · CS-EXEC-03 · AP9 · BRWS-FEEL-06.

### CS-BLOCK-P-03 [BLOCKING] · Site reads as a template showcase, not a real firm

- **Definition**: mentally remove the studio name. If the page reads as "a template demo" rather than as an actual commercialista / advisory / law / coaching firm, the premium claim fails.
- **Why it blocks**: the archetype's entire purpose is to ship premium firm-sites. A template-showcase read defeats the purpose.
- **Detection** (subjective but disciplined · see CS-TONE-05):
  - Does the copy name a specific firm identity with real coordinates, credentials, sectors?
  - Does the imagery show a specific cluster world, not a generic office?
  - Does the voice anchor carry a stance a real firm would take?
  - Are there banned funnel patterns ("Free diagnosis in 10 questions", urgency countdowns, lead magnets before leadership)?
- **Prevention**: cluster blueprint → voice anchor → 10-gate differentiation (D-054) → curated imagery pack → first-person-plural voice. The full pipeline is the prevention.
- **Merge decision**: block if the template fails the "remove studio name" test.
- **LIVE-flip decision**: block.
- **Escalation**: subjective judgment calls go to the release-gatekeeper; if ambiguous, a second reviewer is required. The user has final say.
- **Anchors**: CS-TONE-05 · CS-MARKET-01..07 · CS-EXEC-07 · BRWS-FEEL-01.

### CS-BLOCK-P-04 [BLOCKING] · Accent color used decoratively (>3 per viewport)

- **Definition**: at desktop (1280 × 800) the above-the-fold region contains > 3 elements whose `backgroundColor` / `borderColor` / `color` resolves to `--accent`.
- **Why it blocks**: the archetype's elegance comes from accent-as-punctuation (CS-PAL-05). Accent everywhere = startup-tech aesthetic.
- **Detection**: browser walk counts accent hits in the fold. CS-BLOCK-N-02 covers the nav-specific case; this rule covers the rest of the fold.
- **Prevention**: one accent CTA per section, one italic `<em>` accent per headline, one pull-quote border. No accent underlines on every link; no accent dividers between sections.
- **Merge decision**: block if the PR adds accent decoration.
- **LIVE-flip decision**: block.
- **Anchors**: CS-PAL-05 · BRWS-NAV-05.

### CS-BLOCK-P-05 [BLOCKING] · Banned marketing hyperbole phrases in rendered content

- **Definition**: rendered body on any page × any locale contains "Unlock your potential", "Sblocca il tuo potenziale", "Trasforma la tua vita in X giorni", "Versione migliore di te", "Mindset vincente", "Game-changing", "Revolutionary", "Next-gen", "World-class", "10,000+ clients", "Trusted by X", or any Einstein/Jung/Gandhi/Steve Jobs quote.
- **Why it blocks**: the corporate-suite voice is institutional-advisory. These phrases break the voice instantly.
- **Detection**: grep live render per locale for the banned-phrase regex (BRWS-FEEL-04).
- **Prevention**: `template_content_<name>.py` docstring enumerates banned phrases (F3 pattern). Authors check against the list before writing.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-EXEC-04 · BRWS-FEEL-04 · AP9.

---

## 9 · Non-Pexels imagery blockers

Factory-pipeline uniformity (Session 47 adoption) depends on a single sourcing convention. A mixed pool defeats dedup, defeats the curator audit trail, and leaves a visible inconsistency in quality.

### CS-BLOCK-I-01 [BLOCKING] · Non-Pexels URL on a new pilot

- **Definition**: any URL in a NEW template's pool under `apps/catalog/preview_imagery.py` whose hostname is not `images.pexels.com`.
- **Why it blocks**: factory-pipeline uniformity. The `scripts/check_imagery_pack.py` grep depends on a single CDN domain; reviewer workflow assumes single-source licensing.
- **Detection**:
  ```bash
  grep -nE 'unsplash|shutterstock|getty|adobestock|gettyimages' apps/catalog/preview_imagery.py
  ```
  Any hit on a non-Pragma pool = block.
- **Prevention**: curator protocol §1 (Pexels-only binding); pack file review rejects non-Pexels URLs before they reach `preview_imagery.py`.
- **Merge decision**: **block the PR** (this is the primary merge-block in the imagery family).
- **LIVE-flip decision**: block.
- **Legacy exception**: `business-corporate` (Pragma) at `preview_imagery.py:312-322` carries 6 legacy Unsplash URLs from Session 32, pre-dates the X.3 curation protocol. These are grandfathered until the `business-corporate` Pexels retro-pack lands (AP3). The exception does NOT extend to any new pilot.
- **Anchors**: CS-BLOCK-07 · CS-IMG-SRC-01 · CS-IMG-AP-01 · BRWS-IMG-02 · AP3.

### CS-BLOCK-I-02 [BLOCKING] · Cross-cluster URL reuse (AP6)

- **Definition**: the same Pexels URL appears in ≥ 2 cluster pools under `preview_imagery.py`. Genuinely neutral textures (paper grain, concrete wall) may repeat with an explicit comment in both packs; nothing else.
- **Why it blocks**: it defeats D-054 differentiation. Two templates sharing hero photography read as the same studio — a full-frame differentiation failure.
- **Detection**:
  ```bash
  python scripts/check_imagery_pack.py
  # Exit code non-zero on duplicate URLs
  ```
- **Prevention**: curator dedupe pass before pack approval.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-SRC-04 · CS-IMG-AP-04 · AP6.

### CS-BLOCK-I-03 [BLOCKING] · Image URL 404s on live render

- **Definition**: any `<img>.src` on any rendered page returns HTTP 4xx or 5xx.
- **Why it blocks**: broken hero / broken portrait / broken case-card = visibly broken firm site.
- **Detection**:
  ```js
  // Playwright MCP: browser_network_requests() filtered to image/* with status 4xx/5xx
  ```
- **Prevention**: curator verifies every URL resolves at authoring; CI can add a scheduled check for pool URL liveness (not yet implemented).
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-04 · CS-IMG-SRC-01 · BRWS-IMG-01.

### CS-BLOCK-I-04 [BLOCKING] · URL format missing required Pexels query string

- **Definition**: a Pexels URL in a pool lacks `?auto=compress&cs=tinysrgb&w=<width>` OR uses a non-CDN Pexels preview URL (`images.pexels.com/search/...`).
- **Why it blocks**: byte budget and delivery resolution become unpredictable. A hero at default Pexels delivery (sometimes 3000+ px) bloats the page; a non-CDN preview URL may rate-limit or expire.
- **Detection**:
  ```bash
  grep -oE 'images\.pexels\.com/[^"]+' apps/catalog/preview_imagery.py | \
    grep -vE 'auto=compress&cs=tinysrgb&w=(800|1200|1600)'
  ```
- **Prevention**: curator uses the width-budget table (CS-IMG-SRC-02): hero `w=1600`, feature `w=1200`, portrait `w=800`, detail `w=800`, ambient `w=800`.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-SRC-02.

---

## 10 · Imagery mismatch with content blockers

Subject, mood, and terminology must match the copy. This is the class of defect that tests cannot detect and that Session 31 documented vividly.

### CS-BLOCK-IM-01 [BLOCKING] · Subject-to-profession mismatch (3-second test fails · AP4)

- **Definition**: opening any pool URL for ≥ 3 seconds and asking "does a member of this profession recognize this as their world?" yields a "no."
- **Why it blocks**: this is the Session 31 class — PlayStation gamepad as "map of Rome", Bumble Bee tuna as "artisan ingredients", hairstylists as "dermatology before/after", diamond ring as "oysterman's portrait". Each passed tests. None passed the 3-second read.
- **Detection** (mandatory, curator + reviewer + browser walk, three layers):
  1. Curator 3-second read per URL at authoring (CURATION_PROTOCOL §3.3).
  2. Pack reviewer 3-second read per URL at review.
  3. Browser walk reviewer 3-second read per URL on the live render (BRWS-IMG-03).
- **Prevention**: the three-layer read. No automation. The defect class survives automation by definition.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Escalation**: if ambiguous, a second reviewer's 3-second read tiebreaks. If still ambiguous, reject — reject cost is ~15 minutes to re-source; ship cost is a live defect.
- **Anchors**: CS-BLOCK-05 · CS-IMG-COH-01 · BRWS-IMG-03 · AP4 · Session 31.

### CS-BLOCK-IM-02 [BLOCKING] · Mood contradicts voice anchor

- **Definition**: image's mood (light, palette, posture) argues against the template's voice anchor. Examples:
  - Coaching anchor "Il coaching non è terapia" + therapy-couch imagery.
  - Advisory anchor "Dove si prendono le decisioni che contano" + co-working loft imagery.
  - Commercialista anchor "L'adempimento corretto" + startup-hackathon imagery.
- **Why it blocks**: mood-to-anchor contradiction destroys the archetype's premium read more completely than any other single defect.
- **Detection**: reviewer reads the anchor; re-reads imagery; asks whether the image underlines the anchor. A "fights the anchor" answer = block.
- **Prevention**: curator reads the voice anchor before sourcing; pack file records a coherence statement per URL (CS-IMG-COH-06).
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-06 · CS-IMG-COH-02 · CS-IMG-COH-07 · BRWS-IMG-04 · AP5.

### CS-BLOCK-IM-03 [BLOCKING] · Cluster-terminology contradiction

- **Definition**: leadership `credentials` name a world (Cassazionista, Revisore Legale, ICF PCC) that the portrait set clearly does not show (lab coats with legal credentials, gym wear with CONSOB credentials).
- **Why it blocks**: the copy-imagery contradiction is visible on first scan. The visitor reads "Cassazionista" and sees a hoodie — credibility evaporates.
- **Detection**: grep credentials per leader; compare against portrait imagery; ask "does the portrait set suggest this world?"
- **Prevention**: curator sources portraits against the cluster blueprint §4 credential list. Portrait pack is authored alongside leadership copy, not separately.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-COH-03 · CS-EXEC-03.

### CS-BLOCK-IM-04 [BLOCKING] · Setting is coworking / café / home office on a corporate-suite template

- **Definition**: imagery shows a WeWork-type coworking loft with exposed brick, a café as office, a coffee-shop-as-office, or a domestic setting on a template positioned for commercialista / law / corporate-advisory.
- **Why it blocks**: those settings belong to a `business-startup` archetype (which is a sibling, not corporate-suite). Using them here reads as the wrong archetype.
- **Detection**: visual review + setting check. Institutional advisory settings only.
- **Prevention**: curator applies CS-IMG-PRO-02 (institutional settings) during selection.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-PRO-02.

---

## 11 · Imagery not premium enough blockers

Stock-plate imagery passes license checks, resolution checks, and even coherence checks, and still fails the archetype. This category catches the residual "technically valid but reads as stock" defects.

### CS-BLOCK-IQ-01 [BLOCKING] · Resolution below slot floor

- **Definition**: any pool image delivered at below-slot minimum:
  - Hero < 1600×900
  - Feature < 1200×800
  - Portrait < 800×800 OR not square-aspect (±10%)
  - Detail / ambient < 800×600
- **Why it blocks**: soft hero on retina; pixelated portraits in card grids; blurry ambient. Premium archetype cannot ship soft imagery.
- **Detection**:
  ```bash
  # Extract w= parameter from each pool URL; verify against slot budget
  grep -oE 'images\.pexels\.com/photos/[0-9]+/[^"]+' apps/catalog/preview_imagery.py
  ```
  Plus browser walk natural size check: `img.naturalWidth × img.naturalHeight` in devtools.
- **Prevention**: curator follows CS-IMG-SRC-02 width-budget table.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-PREM-02 · CS-IMG-SRC-02.

### CS-BLOCK-IQ-02 [BLOCKING] · Generic stock fallback (AP5 / blacklist §2)

- **Definition**: any pool URL matches a blacklisted stock cliché:
  - "Generic laptop on clean white desk."
  - "Smiling businesswoman shaking hands in vague office."
  - "Chef holding a plate, looking at camera, perfectly lit."
  - "Multi-ethnic team pointing at a whiteboard."
  - "Two men in suits reviewing a tablet, staged handshake lighting."
  - "Young professional on phone, bright window behind, forced smile."
- **Why it blocks**: stock-plate reads instantly. A pool with even one stock-plate URL drags the whole pool's perceived quality.
- **Detection**: CS-IMG-PREM-05 10-cluster interchangeability test — "if I changed the surrounding copy from commercialista to dentist to coach, would this image still work?" YES = stock-plate = block.
- **Prevention**: curator applies the interchangeability test during sourcing. Pack reviewer re-applies before approval.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-PREM-05 · CS-IMG-AP-03 · AP5 · `docs/content-factory/imagery/blacklist.md` §2.

### CS-BLOCK-IQ-03 [BLOCKING] · KPI band or pillars section decorated with photos

- **Definition**: KPI band (`home.html:91-122`) has any `<img>` behind or among the numerics, OR pillars/services grid shows 3-4 small photos in cards.
- **Why it blocks**: rhythm violation. KPI band is typographic; pillars are typographic-with-icons. Photos here pull the page back toward link-card-grid = template-showcase read.
- **Detection**: `browser_evaluate(() => document.querySelectorAll('.cs-kpi-band img, .cs-pillars img').length)` — must be 0.
- **Prevention**: CS-IMG-SEC-01 / CS-IMG-SEC-02 enforced by design review.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-SEC-01 · CS-IMG-SEC-02 · CS-IMG-RHYTHM-01 · CS-IMG-AP-12.

### CS-BLOCK-IQ-04 [BLOCKING] · Placeholder avatars in live render

- **Definition**: leadership block shows grey silhouette "person icons", initial-in-a-circle avatars, or editor-UI "upload photo" placeholders on the public render.
- **Why it blocks**: placeholder leaks collapse the "real firm" promise.
- **Detection**: browser walk leadership section; any non-photo avatar in leadership = block.
- **Prevention**: CS-IMG-SEC-03 (real portraits from slots 2-3, ≥ 800×800); if a real portrait for a role is missing, the role is CUT, not filled with a placeholder.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-AP-05 · CS-COMP-02 · CS-MARKET-06.

### CS-BLOCK-IQ-05 [BLOCKING] · Hero left-edge visually competes with h1

- **Definition**: the hero photo's leftmost 10% is louder (brighter / busier / higher contrast) than the h1 text column to the left of it. The eye lands on the photo edge rather than the headline.
- **Why it blocks**: the hero-split composition depends on the eye landing on the h1 first. A busy left edge kills the composition.
- **Detection**: visual review at 1920 × 1080 and 1440 × 900; sample the leftmost 10% of the hero photo by eye.
- **Prevention**: curator selects hero URLs with calm left edges (CS-IMG-HERO-06).
- **Merge decision**: block if introduced on the diff.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-COLOR-01 · CS-IMG-HERO-06.

---

## 12 · Responsive breakage blockers

The archetype currently ships with one real `@media` breakpoint across 7 files (`contact.html` at 880 px). AP2 is THE structural gap. These rules govern the target state after the hardening pass lands the 1100 px + 720 px breakpoints.

### CS-BLOCK-V-01 [BLOCKING] · Horizontal scrollbar at any rubric matrix viewport

- **Definition**: `document.documentElement.scrollWidth > document.documentElement.clientWidth` at any of the §5 viewports (1920, 1440, 1280, 1024, 768, 640, 414, 390).
- **Why it blocks**: a horizontal scrollbar = layout has overflowed. On that class of device the page is unusable.
- **Detection** (browser walk, per viewport):
  ```js
  browser_evaluate(() => ({
    sw: document.documentElement.scrollWidth,
    cw: document.documentElement.clientWidth,
    overflows: document.documentElement.scrollWidth > document.documentElement.clientWidth,
  }))
  ```
- **Prevention**: `@media (max-width: 1100px)` reduces section padding to `72px 48px`; `@media (max-width: 720px)` reduces to `56px 24px` and collapses grid columns. Hero stacks; nav becomes hamburger; footer stacks.
- **Merge decision**: block if the PR introduces overflow.
- **LIVE-flip decision**: block unconditionally.
- **Anchors**: CS-BLOCK-02 · CS-RESPONSIVE-02 · BRWS-VIEW-02 · AP2.

### CS-BLOCK-V-02 [BLOCKING] · Hero does not stack at ≤ 720 px

- **Definition**: at 390 × 844 OR 414 × 896, `getComputedStyle('.cs-hero').gridTemplateColumns` is not a single column (`1fr`). Text remains side-by-side with photo → text column crushes to < 150 px; headline is unreadable.
- **Why it blocks**: mobile first fold is illegible.
- **Detection**: see CS-BLOCK-R-02.
- **Prevention**: `home.html` / `_base.html` `@media (max-width: 720px) { .cs-hero { grid-template-columns: 1fr; } }` rule.
- **Merge decision**: block for new pilots; block for any PR that removes an existing responsive rule.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-03 · CS-HERO-07 · BRWS-VIEW-03.

### CS-BLOCK-V-03 [BLOCKING] · Nav does not collapse to hamburger at ≤ 720 px

- **Definition**: at 390 × 844, nav links still render horizontally and overflow the viewport.
- **Why it blocks**: mobile users cannot navigate.
- **Detection**: see CS-BLOCK-N-03.
- **Prevention**: `_base.html` `@media (max-width: 720px) { .cs-nav__links { display: none; } .cs-nav__trigger { display: block; } }` + drawer script.
- **Merge decision**: block for new pilots.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-03 · CS-NAV-05 · BRWS-VIEW-04.

### CS-BLOCK-V-04 [BLOCKING] · Hero h1 < 32 px at 390 px viewport

- **Definition**: at 390 × 844, computed `font-size` of `.cs-hero h1` < 32 px.
- **Why it blocks**: sub-32 px hero h1 on mobile reads weak; italic `<em>` detail is lost; the archetype's restraint-plus-presence claim fails.
- **Detection**:
  ```js
  browser_resize({ width: 390, height: 844 });
  browser_evaluate(() => parseFloat(getComputedStyle(document.querySelector('.cs-hero h1')).fontSize));
  ```
- **Prevention**: `@media (max-width: 720px) { .cs-hero h1 { font-size: clamp(32px, 8vw, 48px); } }` or equivalent.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-RESPONSIVE-03 · BRWS-VIEW-06.

### CS-BLOCK-V-05 [BLOCKING] · Touch target < 44×44 px on mobile

- **Definition**: at 390 × 844, any nav CTA, hero CTA, nav link (when drawer open), or locale-switcher pill renders with bounding box `width < 44 OR height < 44`.
- **Why it blocks**: WCAG 2.5.5 / Apple HIG minimum violated → unreliable tap target.
- **Detection**:
  ```js
  browser_evaluate(() => Array.from(document.querySelectorAll('.cs-nav a, .cs-nav button, .cs-hero a, .cs-hero button, .cs-nav__locales a'))
    .map(el => {
      const r = el.getBoundingClientRect();
      return { sel: el.tagName + (el.className ? '.' + el.className : ''), w: r.width, h: r.height };
    })
    .filter(r => r.w < 44 || r.h < 44))
  ```
  Any row = fail.
- **Prevention**: mobile CSS ensures min-height / padding on all tap targets.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-RESPONSIVE-06 · BRWS-VIEW-07.

### CS-BLOCK-V-06 [BLOCKING] · Walk skipped a viewport from the rubric matrix

- **Definition**: the walk did not execute at one or more of the rubric §5 viewports (1920 / 1440 / 1280 / 1024 / 768 / 640 / 414 / 390).
- **Why it blocks**: coverage gaps hide regressions. The matrix is the floor; the walk must hit every entry.
- **Detection**: `walk-log.md` line-by-line; verify every matrix viewport appears.
- **Prevention**: browser-verifier agent iterates the full matrix per locale × per page.
- **Merge decision**: typically not a merge-block (walk happens post-merge), but BORDERLINE/FAIL scorecard blocks LIVE flip.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-14 · CS-RESPONSIVE-01 · BRWS-VIEW-01.

---

## 13 · Browser live verification failure blockers

The walk itself must be real. Phantom walks and "looks fine" signoffs are the last-mile false-positive class this document exists to prevent.

### CS-BLOCK-W-01 [BLOCKING] · No walk performed (test-only ship)

- **Definition**: the release-gatekeeper is asked to flip `TEMPLATE_REGISTRY.json` from `draft` to `published_live` without a completed rubric walk in `factory/reports/browser-verification/<slug>/<run-timestamp>/`.
- **Why it blocks**: tests pass ≠ ship-ready. AP8 is documented, named, and binding. The Solaria cream-on-cream defect survived 506/506 tests and died in 30 minutes of walk. A template without a walk has not been seen by a human (or by a Playwright MCP session).
- **Detection**: `ls factory/reports/browser-verification/<slug>/` — if empty, block. If the latest run does not contain `verdict.md` with VERDICT: PASS, block.
- **Prevention**: release-gatekeeper's workflow (scorecard §8) places the browser-verifier walk BEFORE the tier flip. There is no code path from `draft` to `published_live` that skips the walk.
- **Merge decision**: not applicable at draft-merge; strictly a LIVE-flip block.
- **LIVE-flip decision**: block unconditionally.
- **Anchors**: CS-BLOCK-18 · CS-BROWSER-01 · AP8.

### CS-BLOCK-W-02 [BLOCKING] · Walk verdict missing URL + port

- **Definition**: `verdict.md` does not open with `Server: http://127.0.0.1:<port>/` and `Started at: <ISO-8601>`.
- **Why it blocks**: the user must be able to open the exact URL in a parallel browser to verify. A missing URL means the walk is unverifiable by a second reviewer.
- **Detection**: `grep -E '^\*\*URL\*\*:' factory/reports/browser-verification/<slug>/<run>/verdict.md`.
- **Prevention**: the verdict template (browser rubric §11) starts with the server block; the template is fillable but not removable.
- **Merge decision**: not applicable.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-13 · CS-BROWSER-02 · BRWS-SRV-02.

### CS-BLOCK-W-03 [BLOCKING] · Evidence directory incomplete

- **Definition**: `factory/reports/browser-verification/<slug>/<run>/` missing one or more of:
  - 120+ PNG screenshots (5 locales × 6 pages × 4 core viewports minimum).
  - `measurements.json` keyed by `[BLOCKING]` tag with the raw numbers from the rubric §6 checks.
  - `walk-log.md` with chronological MCP calls and page URLs.
  - `console.log` aggregated per page.
- **Why it blocks**: a walk without evidence is not reproducible. The scorecard verdict depends on the evidence; without it the verdict cannot stand.
- **Detection**:
  ```bash
  find factory/reports/browser-verification/<slug>/<run>/screenshots -name '*.png' | wc -l
  test -f factory/reports/browser-verification/<slug>/<run>/measurements.json
  test -f factory/reports/browser-verification/<slug>/<run>/walk-log.md
  ```
- **Prevention**: browser-verifier agent writes the evidence as it walks. BRWS-EVID-01..06 are binding.
- **Merge decision**: not applicable.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-15 · BRWS-EVID-01/02/03.

### CS-BLOCK-W-04 [BLOCKING] · Walk verdict asserts PASS without measurement evidence

- **Definition**: `verdict.md` reports PASS but `measurements.json` is empty / partial, or screenshots are below the §7 floor, or the rubric §9 blocking-issue checklist is not filled in.
- **Why it blocks**: "it looked fine" signoffs are exactly the failure mode this document prevents. A PASS verdict must be backed by measurements keyed to `[BLOCKING]` tags.
- **Detection**: open `verdict.md`; confirm every `[BLOCKING]` rubric check has a measurement row in `measurements.json`; confirm screenshots exist at every matrix viewport for every locale × page in scope.
- **Prevention**: browser-verifier agent template enforces measurement capture per check.
- **Merge decision**: not applicable.
- **LIVE-flip decision**: block; re-walk required.
- **Anchors**: BRWS-EVID-03 · BRWS-TOOL-01.

### CS-BLOCK-W-05 [BLOCKING] · Dev server shut down before user parallel-verification

- **Definition**: the reviewer shut down `python manage.py runserver` immediately on writing the verdict, before the user had opportunity to open the same URL in their own browser and verify.
- **Why it blocks**: the user's parallel verification is the final layer of the acceptance gate. Killing the server mid-handshake defeats the layer.
- **Detection**: `verdict.md` close-block missing `Server still running at http://127.0.0.1:<port>/ — shut down on user confirmation`.
- **Prevention**: BRWS-SRV-04 binding.
- **Merge decision**: not applicable.
- **LIVE-flip decision**: block; re-walk with server kept open.
- **Anchors**: BRWS-SRV-04.

---

## 14 · Footer quality blockers

The footer is where many templates get sloppy — the reviewer has scrolled through the fun parts and the bar drops. These rules keep the floor.

### CS-BLOCK-F-01 [BLOCKING] · Footer polarity broken (dark-on-dark text pocket in footer)

- **Definition**: `.cs-foot` has `background: var(--primary)` (or a deep neutral) AND any text descendant has RGB distance < 120 against the footer background.
- **Why it blocks**: scoped AP11. A footer with invisible text is a functional failure for legal links (privacy, P.IVA, whistleblowing) that MUST be readable.
- **Detection**: same as CS-BLOCK-C-01 scoped to `.cs-foot`.
- **Prevention**: CS-PAL-04 binding; `--on-dark*` variants cascade automatically if the footer CSS is not overridden.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-17 · CS-FOOT-01 · CS-PAL-04 · AP11.

### CS-BLOCK-F-02 [BLOCKING] · Footer absent on any page

- **Definition**: one or more of the 6 skin pages renders without a `.cs-foot` element.
- **Why it blocks**: every page needs legal coordinates, P.IVA, whistleblowing (advisory clusters). A missing footer is a compliance gap on commercialista / law templates.
- **Detection**: `browser_evaluate(() => document.querySelector('.cs-foot') ? 'present' : 'missing')` per page × locale.
- **Prevention**: `_base.html` includes `{% block footer %}` with the default `.cs-foot` partial. Page templates that override the block must re-include the footer.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-FOOT-01.

### CS-BLOCK-F-03 [BLOCKING] · Legal row missing privacy OR cookie OR P.IVA links

- **Definition**: the footer legal row is missing one or more of: copyright line, P.IVA, privacy link, cookie link. (Whistleblowing is `[REQUIRED]`, not `[BLOCKING]`, for non-advisory clusters.)
- **Why it blocks**: GDPR compliance. Missing privacy / cookie links on an EU-targeted site is a legal violation, not just a polish gap.
- **Detection**:
  ```js
  browser_evaluate(() => {
    const legal = document.querySelector('.cs-foot .legal');
    return {
      hasCopyright: /©|\bcopyright\b/i.test(legal?.textContent || ''),
      hasPiva: /p\.\s*iva/i.test(legal?.textContent || ''),
      hasPrivacy: !!legal?.querySelector('a[href*="privacy"]'),
      hasCookie: !!legal?.querySelector('a[href*="cookie"]'),
    };
  })
  ```
  Any `false` = block.
- **Prevention**: `_base.html` footer partial has the 4 canonical links hardcoded; author adds whistleblowing for advisory clusters.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-FOOT-02.

---

## 15 · Strong visual inconsistency blockers

Inconsistency reads as the archetype breaking. This category covers palette drift, typography swap failures, and composition drift that collectively tip the site into "doesn't feel finished."

### CS-BLOCK-VI-01 [BLOCKING] · Geometric sans on headings (Montserrat, Poppins, Raleway)

- **Definition**: `.cs-hero h1`, `.cs-section h2`, or any heading's computed `font-family` is a geometric-sans (Montserrat, Poppins, Raleway, Gotham, Futura, Century Gothic) instead of a humanist/transitional serif (Merriweather, IBM Plex Serif, Fraunces, PT Serif, Source Serif, Lora).
- **Why it blocks**: the archetype's editorial voice depends on serif headings. Geometric sans reads startup-tech; it breaks the archetype's adjective stack ("premium / elegant / modern / professional").
- **Detection**:
  ```js
  browser_evaluate(() => {
    const banned = /Montserrat|Poppins|Raleway|Gotham|Futura|Century Gothic/i;
    return Array.from(document.querySelectorAll('h1, h2, h3'))
      .map(h => getComputedStyle(h).fontFamily)
      .filter(f => banned.test(f));
  })
  // Any result = block
  ```
- **Prevention**: CS-TYPE-01 binding; brand palette `heading_font` field restricted to the sanctioned list in `seed_templates.py`.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-TYPE-01 · BRWS-RHYTHM-05.

### CS-BLOCK-VI-02 [BLOCKING] · KPI band missing tabular numerals

- **Definition**: `.cs-kpi-band .num` computed `fontVariantNumeric` does not contain `tabular-nums`.
- **Why it blocks**: without tabular-nums, "180+" and "94%" misalign vertically across locales → boardroom figures look ragged → advisory claim erodes.
- **Detection**:
  ```js
  browser_evaluate(() => Array.from(document.querySelectorAll('.cs-kpi-band .num'))
    .map(n => getComputedStyle(n).fontVariantNumeric)
    .filter(v => !v.includes('tabular-nums')))
  // Any result = block
  ```
- **Prevention**: `_base.html` `.num { font-variant-numeric: tabular-nums; }` rule; template CSS does not override.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-TYPE-03 · BRWS-READ-05.

### CS-BLOCK-VI-03 [BLOCKING] · Arabic glyphs render as squares under RTL (font-swap failure)

- **Definition**: on `/ar/templates/<slug>/live/`, headings render as `□□□` square glyphs — the Latin heading font is not swapped to Noto Kufi Arabic + Amiri under `html[dir="rtl"]`.
- **Why it blocks**: the entire AR locale is unreadable.
- **Detection**: browser walk on AR locale home; screenshot; visually verify Arabic glyphs render correctly (not as squares).
- **Prevention**: `_base.html:371-387` carries the D1 font-swap block. Regressions against it = block.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-TYPE-06 · D1 · BRWS-READ-04.

### CS-BLOCK-VI-04 [BLOCKING] · Section padding crushed below `100px 72px` on multiple desktop sections

- **Definition**: ≥ 2 home sections on desktop (≥ 1100 px) have computed `padding` below `100px 72px` (e.g., `40px 24px` to cram in more content).
- **Why it blocks**: restraint over density (CS-TONE-02) is the archetype's core elegance. Crushed padding destroys it.
- **Detection**:
  ```js
  browser_resize({ width: 1440, height: 900 });
  browser_evaluate(() => Array.from(document.querySelectorAll('main > section, main > div.cs-section'))
    .map(s => ({ cls: s.className, padding: getComputedStyle(s).padding }))
    .filter(r => {
      const m = r.padding.match(/(\d+)px (\d+)px/);
      return m && (parseInt(m[1]) < 100 || parseInt(m[2]) < 72);
    }))
  ```
- **Prevention**: CS-RHYTHM-01 binding; every `.cs-section` inherits the base padding.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-RHYTHM-01 · CS-TONE-02 · BRWS-RHYTHM-01.

### CS-BLOCK-VI-05 [BLOCKING] · Home section order wrong (3+ dark bands, or cases before leadership)

- **Definition**: home section DOM order does not match hero · pillars · kpi-band · sectors · leadership · cases · cta, OR home has ≥ 3 sections with `background: var(--primary)` (regardless of order).
- **Why it blocks**: institutional pacing (proposition → method → proof → sectors → people → work → invite) breaks if reordered; 3+ dark bands read startup-aggressive.
- **Detection**: `browser_evaluate(() => Array.from(document.querySelectorAll('main > section, main > .cs-section')).map(s => s.className))` + count of dark-section matches.
- **Prevention**: `home.html` hardcodes the section order; template-specific `home.html` overrides are allowed only if they preserve the order.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-RHYTHM-02 · CS-TONE-03 · BRWS-RHYTHM-02/03.

### CS-BLOCK-VI-06 [BLOCKING] · D-054 10-gate differentiation missing or single-sibling-only

- **Definition**: `template_content_<name>.py` docstring opens without a 10-dimension differentiation block, OR the block only diffs against ONE sibling (e.g., Pragma only) when 2+ siblings exist on the archetype.
- **Why it blocks**: palette / voice / credential drift across siblings compounds. Pragma + Fiscus + Solaria means every NEW pilot must diff against all three. The 10-gate is the only mechanism that forces the triangulation.
- **Detection**:
  ```bash
  grep -n "10-gate" apps/catalog/template_content_<name>.py | head
  ```
  Absent = block. Present but referencing only one sibling = block.
- **Prevention**: D-054 docstring template in cluster blueprint §5; review rejects PRs where the 10-gate is thin or missing.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-12 · CS-EXEC-02.

---

## 16 · Text/image incoherence blockers

The copy and the imagery must pull in the same direction. When they don't, the site reads as assembled-from-parts.

### CS-BLOCK-TI-01 [BLOCKING] · Voice anchor missing OR paraphrased in any locale

- **Definition**: the template's voice anchor (cluster blueprint §5 · e.g., "Dove si prendono le decisioni che contano") is absent from any of the 5 locale content files, OR a locale paraphrases ("Where important decisions happen") instead of preserving the anchor verbatim-in-translation.
- **Why it blocks**: the anchor IS the template's identity. A paraphrase dilutes the identity; a missing anchor erases it.
- **Detection**:
  ```bash
  # For each locale
  for loc in it en fr es ar; do
    grep -c "<voice anchor phrase translated>" apps/catalog/template_content_<name>_<loc>.py || echo "MISSING: $loc"
  done
  ```
  Plus browser walk grep per locale on the live render.
- **Prevention**: F2 pattern binding; cluster blueprint §5 provides the anchor + 5 locale translations.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-11 · CS-EXEC-01 · F2 · BRWS-FEEL-05.

### CS-BLOCK-TI-02 [BLOCKING] · Credentials point to a world the portraits clearly do not show

- **Definition**: leadership copy lists credentials (Cassazionista, ICF PCC, CONSOB) but portrait imagery shows a clearly different world (lab coats, gym wear, retail floor).
- **Why it blocks**: credibility collapses on first scan. The visitor reads "Cassazionista" and sees a hoodie.
- **Detection**: cross-reference leadership `credentials` against the portrait pack's coherence statements (CS-IMG-COH-06).
- **Prevention**: curator authors portraits alongside leadership copy, not in isolation.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-BLOCK-IM-03 · CS-IMG-COH-03 · CS-EXEC-03.

### CS-BLOCK-TI-03 [BLOCKING] · Hero text and hero image fight each other (semantic mismatch)

- **Definition**: hero h1 subject (copy) and hero photo subject (imagery) point to different worlds. Example: h1 "Advisory strategica per famiglie imprenditoriali" + hero photo of a co-working loft with standing desks.
- **Why it blocks**: the first fold's text/image contract is broken; the visitor parses two different firms.
- **Detection**: visual review; re-read hero h1; re-read pack file slot-0 caption + coherence statement; confirm they describe the same world.
- **Prevention**: pack file coherence statement per URL (CS-IMG-COH-06) + voice-anchor-aware curator protocol.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-IMG-COH-02 · CS-IMG-COH-07.

### CS-BLOCK-TI-04 [BLOCKING] · Studio name and site copy drift apart

- **Definition**: the meta-strip, leadership, cases, coordinates, and footer reference different studio identities. Example: home meta-strip says "Fiscus Commercialisti Milano"; leadership bios reference "Pragma Advisory"; footer coordinates show "Solaria Coaching".
- **Why it blocks**: obvious copy-paste error across templates; site looks unfinished.
- **Detection**: browser walk grep for studio name across pages; mismatches = block.
- **Prevention**: `template_content_<name>.py` single source of truth for studio name; locale files inherit.
- **Merge decision**: block.
- **LIVE-flip decision**: block.
- **Anchors**: CS-MARKET-07.

---

## 17 · Required-tier issues (block LIVE flip, allow draft merge with TODO)

Not everything is blocking. This section enumerates `[REQUIRED]` defects — quality regressions that block the LIVE flip and must be remediated before sign-off, but that can land on `draft` with a tracked TODO.

### CS-REQ-01 [REQUIRED] · Hero subhead > 35 words OR > 3 lines at 1280 px

- Anchors: CS-HERO-05 · CS-DENSITY-01 · BRWS-READ-02.
- **Merge behavior**: allow draft merge with TODO.
- **LIVE-flip behavior**: block until fixed.

### CS-REQ-02 [REQUIRED] · KPI band shows > 4 stats (≥ 5)

- Anchors: CS-DENSITY-04.

### CS-REQ-03 [REQUIRED] · Pillars section shows 5+ cards OR uses photo cards instead of icon cards

- Anchors: CS-DENSITY-02 · CS-IMG-SEC-01.

### CS-REQ-04 [REQUIRED] · Whistleblowing link missing on advisory cluster footer (commercialista / law)

- Anchors: CS-FOOT-02 (D.lgs. 24/2023 whistleblowing).

### CS-REQ-05 [REQUIRED] · Secondary CTA is accent-filled instead of ghost/outline

- Anchors: CS-CTA-03.

### CS-REQ-06 [REQUIRED] · Reduced-motion JS path unverified (`[data-lm]` coverage)

- Anchors: AP12 · CS-RESPONSIVE-07 · BRWS-FEEL-08.

### CS-REQ-07 [REQUIRED] · Pack file missing caption / role / coherence statement on one or more URLs

- Anchors: CS-IMG-COH-06 · CS-IMG-AP-13.

### CS-REQ-08 [REQUIRED] · Hero h1 AA-pass but AAA-miss on ≥ 1 locale (contrast 4.5-6.9)

- Anchors: CS-HERO-03.

### CS-REQ-09 [REQUIRED] · Banned phrase grep returns 1 hit in FR / ES / AR (translator drift)

- Anchors: CS-EXEC-04 · BRWS-FEEL-04.

### CS-REQ-10 [REQUIRED] · Portrait demographic spread mono (3 same-demographic without rationale)

- Anchors: CS-IMG-COH-05.

All of the above block LIVE-flip but not draft-merge. Remediation is tracked as a follow-up task with a fixed owner. A template can accrue multiple `[REQUIRED]` TODOs on `draft` but a LIVE flip requires all closed.

---

## 18 · Escalation path

### 18.1 · When to escalate

Escalate any of the following:

1. **A defect's severity is ambiguous** — reviewer is unsure whether it is `[BLOCKING]` or `[REQUIRED]`. Default to the stricter tag, then escalate to the release-gatekeeper.
2. **A blocker is claimed to be inapplicable** — e.g., an author requests a waiver for a non-Pexels URL citing "I couldn't find an equivalent on Pexels in 15 minutes." Waivers for `[BLOCKING]` rules go to the user; they are NOT the release-gatekeeper's call.
3. **A detection method is disputed** — e.g., "the 3-second semantic check on this URL is subjective." In that case a second reviewer runs the check independently; if both say fail, it's fail. If they disagree, the release-gatekeeper tiebreaks; if still ambiguous, reject (the cost asymmetry favors rejection).
4. **A blocker is latent on main** — e.g., Pragma's Unsplash pack predates the Pexels-only rule. Latent cases are grandfathered by design, not by waiver. If a new case emerges that is not already documented as grandfathered, escalate — do not silently add it to the exception list.
5. **A walk produced borderline-ambiguous evidence** — e.g., scrollbar appears at 640 × 360 for a fraction of a pixel due to scrollbar-width rendering. Escalate with the measurement; the release-gatekeeper decides whether it is a real overflow or a rendering artifact.

### 18.2 · Escalation chain

```
Reviewer  →  Release-gatekeeper  →  User
           ↑                    ↑
           second reviewer      (final call on waivers for [BLOCKING] rules)
           for tie-breaks
```

- **Reviewer**: runs detection, identifies the defect, proposes a severity tag, tries to fix if simple.
- **Second reviewer** (peer): invoked for 3-second imagery checks, "reads as a template" subjective calls, and any tiebreak the first reviewer flags.
- **Release-gatekeeper**: aggregates rubric + scorecard; applies Layer 1 / 2 / 3 logic; writes the final scorecard; initiates remediation or proceeds to flip. Has discretion on `[STRONG]` deviations with a written `§ deviation` justification.
- **User**: final call on any waiver for a `[BLOCKING]` rule; final call on what to do when a blocker is latent on main and affects an unrelated PR.

### 18.3 · What escalation never does

- Escalation never downgrades a `[BLOCKING]` rule without user approval. A release-gatekeeper cannot waive a blocker unilaterally.
- Escalation never skips the re-walk after a FAIL. A fixed defect requires a fresh `<run-timestamp>` walk, not an in-place patch of the failing verdict.
- Escalation never replaces the user parallel-verification handshake. The user opens the server URL in their own browser before the final LIVE flip.

---

## 19 · Merge-block vs follow-up decision matrix

### 19.1 · The decision tree

```
Is the defect [BLOCKING]?
├─ YES
│   Is the defect INTRODUCED by this PR (not latent on main)?
│   ├─ YES → BLOCK MERGE · fix in this PR or split it out
│   └─ NO  → allow draft merge · BLOCK LIVE flip · fix in a follow-up PR
└─ NO (so [REQUIRED] / [STRONG] / [GUIDELINE])
    Is it [REQUIRED]?
    ├─ YES → allow draft merge with tracked TODO · BLOCK LIVE flip · fix before flip
    └─ NO  → allow merge · allow LIVE flip with § deviation note (STRONG)
             or no special handling (GUIDELINE)
```

### 19.2 · Concrete examples mapped through the matrix

| Defect | Tag | Introduced by PR? | Merge decision | LIVE decision |
|---|---|:-:|---|---|
| New template palette inverts polarity (Solaria `e8f38b5` class) | BLOCKING | ✓ | **Block merge** — fix palette first | Block flip |
| Pragma's legacy Unsplash pack | BLOCKING (CS-BLOCK-I-01) in principle, **grandfathered** | ✗ latent | Allow merge of unrelated PRs | Pragma stays LIVE as-is; any NEW pilot's non-Pexels URL blocks flip |
| PR adds a new template with `--primary-2: #2c3e6b` hardcode | STRONG (AP7) | ✓ | Allow merge with `§ deviation` note + hardening task | Allow flip |
| Walk finds horizontal scroll at 390 × 844 on home | BLOCKING | ✓ (if PR changed skin); ✗ (if skin hardening not yet done) | If introduced: block merge. If latent (AP2 pre-hardening): allow draft-merge of unrelated PR, block LIVE flip | Block flip unconditionally |
| Hero subhead 42 words on new template | REQUIRED | ✓ | Allow draft merge with TODO | Block flip |
| Footer missing whistleblowing link on commercialista | REQUIRED | ✓ | Allow draft merge with TODO | Block flip |
| Home has 6 KPI stats instead of 3-4 | REQUIRED | ✓ | Allow draft merge with TODO | Block flip |
| No walk performed | BLOCKING (CS-BLOCK-18) | n/a | n/a | Block flip; run the walk |
| Walk verdict missing URL + port | BLOCKING (CS-BLOCK-13) | n/a | n/a | Block flip; re-run with URL recorded |
| Imagery 3-second test fails on hero | BLOCKING | ✓ | Block merge · re-source URL | Block flip |
| Pillars section padding is `88 px 72 px` instead of `100 px 72 px` | REQUIRED | ✓ | Allow draft merge with TODO | Block flip |
| Nav section has accent underline on every link | BLOCKING (CS-BLOCK-N-02) | ✓ | Block merge | Block flip |
| Logo marquee duration 60 s instead of 110 s | STRONG | ✓ | Allow merge with `§ deviation` | Allow flip |
| About page paragraph above timeline 180 words | STRONG | ✓ | Allow merge, flag in polish follow-up | Allow flip |

### 19.3 · The "split it out" escape hatch

When a PR conflates unrelated work and a `[BLOCKING]` defect is introduced in only one part:

- **Default**: block the merge. Require the PR to split — one PR with the defect-free work (mergeable immediately), another PR with the blocker (mergeable when fixed).
- **Exception**: the blocker is genuinely inseparable from the rest (rare). In that case, fix-in-place in the current PR.

This avoids the pattern of "just merge it, we'll fix the hero in a follow-up" that accumulates blockers on main.

---

## 20 · Why these rules must be strong — the CLI false-positive defense

The scorecard and the rubric both say "CLI green is a lower bound." This document codifies WHY and turns it into enforcement. Two concrete examples:

### 20.1 · Solaria `e8f38b5` (AP1 · the load-bearing incident)

Before the commit:
- `manage.py check` → 0 issues.
- `manage.py test apps.catalog` → 131/131 pass.
- `manage.py test apps` → 506/506 pass.
- `generate_previews` → ran successfully.
- `scripts/check_imagery_pack.py` → passed.

After 30 minutes of browser walk: every `h1..h5` on every page rendered cream-on-cream — near-invisible. The commit was fixed at `6b70d56` with an 8-line documenting comment + 2-hex palette change.

**Lesson**: CLI tools rendered zero pixels. They cannot catch the defect. Only the browser walk did. **CS-BLOCK-01 / CS-BLOCK-R-01 is the codified defense.**

### 20.2 · Session 31 imagery incidents (AP4 · the subject-mismatch class)

Template pools shipped with:
- PlayStation gamepad labeled "map of Rome" on a real-estate template.
- Bumble Bee tuna can labeled "artisan ingredients" on a bottega template.
- Hairstylists' portraits labeled "before/after dermatology" on a medical template.
- Diamond ring labeled "oysterman's portrait" on a Luxe editorial template.

Each URL had a valid CC0 license. Each passed `scripts/check_imagery_pack.py` (hostname + dedup only). Each passed the test suite (no image rendering in tests). **Every one failed the 3-second semantic read.**

**Lesson**: license compliance + dedup + resolution ≠ subject correctness. Only a human (or a reviewer driving Playwright MCP with a 3-second pause) can catch it. **CS-BLOCK-05 / CS-BLOCK-IM-01 is the codified defense.**

### 20.3 · Why this document must be strong

The two classes above are not edge cases. They are the dominant failure mode for this archetype. Every blocking rule here either:

- Directly defends against an already-observed incident, OR
- Generalizes from an incident to a class of plausible near-misses.

**A weak blocking-rules document degrades back to CLI-only shipping.** The whole point of X.4a factory hardening is to make the bar visible and enforceable, so that the next template — whether Solaria Commit B (currently paused), a new Wave 3 pilot, or the Pragma retro-pack — lands on a sturdier skin than the Solaria draft did.

Three operational habits prevent the CLI false-positive class:

1. **Run the rubric walk, always.** No tier flip without a recorded walk.
2. **Inspect the live render with the server URL shared with the user.** The user opens it in parallel and can veto.
3. **When in doubt, BLOCK.** The asymmetric cost (15 minutes to fix vs a shipped broken headline) makes rejection cheap and shipping broken expensive.

---

## 21 · Summary

### 21.1 · Severity model (one-paragraph recap)

Four levels: `[BLOCKING]` (prevents merge when introduced by the diff; prevents LIVE flip unconditionally), `[REQUIRED]` (allows draft-merge with tracked TODO; prevents LIVE flip), `[STRONG]` (allowed with written `§ deviation` justification), `[GUIDELINE]` (taste). The two-axis decision — merge vs LIVE flip — maps to the D-102 two-commit cadence: `[BLOCKING]` can block both axes; `[REQUIRED]` blocks only the LIVE-flip axis; `[STRONG]` blocks neither if deviation is written; `[GUIDELINE]` blocks neither.

### 21.2 · The 18 hard blockers (ship-gate summary)

Codified in §3 as `CS-BLOCK-01..18`, 1:1 with the scorecard's 18 Layer-1 overrides. Each is a FAIL on its own regardless of other scores. The list, grouped by family:

- **Contrast (AP1 / AP11 class)**: CS-BLOCK-01 (h1..h5 distance / WCAG on paper), CS-BLOCK-17 (dark-section child text distance / WCAG).
- **Responsive (AP2 class)**: CS-BLOCK-02 (horizontal scrollbar), CS-BLOCK-03 (hero + nav collapse at ≤ 720), CS-BLOCK-14 (matrix coverage).
- **Imagery**: CS-BLOCK-04 (404s), CS-BLOCK-05 (3-second subject check, AP4), CS-BLOCK-06 (mood vs voice anchor, AP5), CS-BLOCK-07 (non-Pexels on new pilots, AP3).
- **Premium feel**: CS-BLOCK-08 (editor affordances leak), CS-BLOCK-09 (placeholder strings), CS-BLOCK-10 (fake certifications, AP9).
- **Voice / differentiation**: CS-BLOCK-11 (voice anchor paraphrased / missing), CS-BLOCK-12 (D-054 10-gate triangulation absent).
- **Walk discipline**: CS-BLOCK-13 (URL + port missing), CS-BLOCK-15 (evidence directory incomplete), CS-BLOCK-18 (no walk at all).
- **Navbar polarity / accent**: CS-BLOCK-16 (nav bg ≠ `--primary` OR > 1 accent element).

Plus the category-expanded blockers in §4-§17: readability (R-01/02/03), contrast (C-01/02/03), navbar (N-01..04), hero (H-01..05), premium feel (P-01..05), imagery sourcing (I-01..04), imagery coherence (IM-01..04), imagery quality (IQ-01..05), viewport (V-01..06), walk (W-01..05), footer (F-01..03), visual inconsistency (VI-01..06), text/image coherence (TI-01..04).

### 21.3 · How these rules affect release decisions

- **Commit A (draft-landing)**: a PR clears Commit A when every defect introduced *by this diff* is clear of `[BLOCKING]`. Pre-existing latent blockers on main do not block unrelated PRs, but they also do not silently reset the clock — they stay tracked in the archetype hardening backlog.
- **Commit B (LIVE flip)**: a template clears Commit B only when the full rubric walk PASSes AND the scorecard's Layer 1 (zero overrides), Layer 2 (critical floors ≥ 4), Layer 3 (aggregate ≥ 4.3) all pass, AND zero `[REQUIRED]` TODOs are outstanding, AND the server URL was shared for user parallel-verification. Any single `[BLOCKING]` or `[REQUIRED]` defect holds the flip.
- **User final gate**: for any ambiguous `[BLOCKING]` waiver, the user has final call. The release-gatekeeper does not grant `[BLOCKING]` waivers unilaterally.
- **Re-walk discipline**: on FAIL, there is no in-place verdict patching. A new branch pass produces a fresh `<run-timestamp>` walk + fresh scorecard. Superseded artifacts stay in the directory for audit.
- **Solaria Commit B explicit note**: per user instruction, Solaria Commit B (EN / FR / ES / AR authoring for the `solaria-coaching` template, currently paused on branch `phase-x4-wave2-solaria-coaching-v1` after `e8f38b5` / `6b70d56`) is NOT un-paused by this document. It remains paused until the archetype hardening pass closes — specifically until the 1100 + 720 responsive breakpoints land, the palette validator (or the equivalent discipline) is in place, and Pragma's retro-pack is scheduled. Nothing in this document authorizes proceeding with Solaria Commit B.

### 21.4 · Bottom line

Corporate-suite ships 3 templates today. The archetype works. Two structural gaps remain (AP1 enforceability, AP2 responsive coverage), both addressed by hardening work separate from this document. This document's role is to ensure that every future pilot — and every future walk of every current pilot — is measured against an explicit, evidence-backed bar. The bar is:

1. Every `[BLOCKING]` rule above is a ship-gate.
2. CLI green is a lower bound, never a ship signal.
3. The browser walk has the veto, always.
4. When in doubt, BLOCK.

— end of blocking rules —
