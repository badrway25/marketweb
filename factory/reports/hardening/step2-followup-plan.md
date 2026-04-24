# Corporate-suite Factory Hardening · Step 2 · Follow-up plan (post No-Go)

**Phase**: X.4a · **Branch**: `phase-x4a-corporate-factory-hardening-followup`
**Baseline tip at planning**: `0727aad` (Step 1D — responsive hardening + live walk closed).
**Scope**: factory-only. No `apps/editor`, `apps/projects`, `apps/commerce` edits. No new archetypes. No Solaria Commit B un-pause under any Step 2 activity.
**Solaria status**: paused per binding user instruction. This plan does not move Commit B; it prepares the archetype so Commit B can be re-opened later under a subsequent phase.

**Inputs consumed**:

- `factory/reports/hardening/step1-core-hardening.md` (Steps 1A · 1B · 1C · 1D)
- `factory/reports/browser-verification/x4a-hardening-round1.md` (Round 1 Playwright walk · IT LTR only)
- `factory/reports/browser-verification/x4a-step1d/20260424T2300Z/screenshots/*.png` (evidence)
- `factory/standards/corporate-suite-design-standard.md`
- `factory/standards/corporate-suite-imagery-standard.md`
- `factory/standards/corporate-suite-browser-rubric.md`
- `factory/standards/corporate-suite-blocking-rules.md`
- `factory/standards/corporate-suite-quality-scorecard.md`
- `factory/standards/corporate-suite-multi-agent-sop.md`
- `factory/references/template-inventory.md` (§7 systemic issues)
- `factory/references/anti-pattern-library.md` (AP1–AP12)
- `factory/references/pattern-library.md`
- `factory/agents/*.md` (10 agent prompts)

A file named `factory/reports/hardening/step1-readiness-verdict.md` was referenced in the Step 2 brief but is not present on disk at baseline tip `0727aad`. This plan reconstructs the No-Go reasoning from (a) the deferrals/deviations logged inside Step 1 reports and (b) the §7 preconditions in `template-inventory.md` that formally gate Solaria Commit B.

---

## 1 · Exact reasons for No-Go

The Step 1 work closed the four archetype-level risk classes that surfaced in Solaria Commit A (palette, chrome, editorial floor, responsive). Both the Step 1 hardening report and the Round 1 Playwright walk report `PASS` at their own scope. The No-Go verdict is **not** a reversal of either — it is the rubric-correct reading that their scope is **narrower than the ship gate** the standards define. Specifically:

### R1 · Browser walk coverage is a single LTR slice, not the rubric's full matrix

`corporate-suite-browser-rubric.md` §5 prescribes a walk of **5 locales × 6 pages × 8 viewports = 240 cells per template**. Round 1 walked **IT LTR only**, covering Pragma (5 pages) and Fiscus (1 page) at 8 viewports. That is roughly **6 % of the rubric's required surface for a two-template archetype** — the rest was waived under three `§ deviation` entries explicitly tagged *"deferred to X.4b"*. A PASS on 6 % of the matrix cannot clear the gate defined for 100 %.

- Deviation 1: RTL (AR) live walk deferred.
- Deviation 2: EN / FR / ES live walks deferred.
- Deviation 3: Pragma legacy imagery (AP3) not touched.
- Deviation 4 (implicit): BRWS-FEEL-05 voice anchor check is rubric-correct in IT only — not verified on the 4 other locales.

### R2 · Systemic-issue preconditions from `template-inventory.md §7` have not all closed

§7 enumerates seven systemic items; six carry the hard `⚠` flag that binds Solaria Commit B. Step 1 closes or partially closes three of those six (AP1 skin layer, AP2 responsive, AP7 dead-code). Three remain open (AP8 first end-to-end pipeline run, AP10 D-054 triangulation drift, AP12 reduced-motion JS verification), plus the soft AP3 precondition and the one-line documentation fix for the release-gatekeeper CRITICAL list.

### R3 · Two load-bearing Step 1 contracts are enforced at runtime only — no build-time failure surface

`apps/catalog/theme_safety.py` (AP1) and `apps/catalog/imagery_policy.py` (AP3 / CS-IMG-SRC-01) emit `UserWarning` on violation. `UserWarning` is visible during live render and in tests run with `-W error::UserWarning`, but it does **not** fail a default CI run. A regression re-introducing a cream `--primary` on a fourth corporate-suite palette would pass the current default CI green set the same way Solaria `e8f38b5` did. The archetype now *reports* the defect; it does not yet *refuse to ship* it.

### R4 · Two `[BLOCKING]`-adjacent content defects remain on the enrolled templates

- `.cs-foot` renders three `href="#"` placeholders for privacy / cookie / legal on both Pragma and Fiscus. `CS-CTA-04` requires real-route targets; these rendered into Round 1 without triggering a rubric failure only because the rubric treats them as footer-legal-copy, not CTAs. Any reviewer walk with the current blocking-rules text would flag them.
- The hero ghost CTA is 177 × 24 px at 390 width — below WCAG 2.1 SC 2.5.5 touch-target floor. The Round 1 report waived it under `CS-CTA-03` "ghost = typographic link, not button". That waiver is load-bearing and defensible, but it is a standing deviation, not a closed issue.

### R5 · Pragma legacy imagery (AP3) is still the archetype's one tolerated Unsplash exception

The imagery-policy gate treats `business-corporate` as `is_legacy_exempt = True` and stays silent on Pragma. `LEGACY_EXEMPT_KEYS = {business-corporate}`. Until a Pexels retro-pack replaces the 6 Unsplash URLs, the archetype carries a perpetual exception. SOP §10.3 framing — *"every pilot lands on rails that already caught a Solaria-class defect"* — is not true while that exception stands.

### R6 · Multi-agent pipeline has not run end-to-end once

SOP §4.1 defines a 10-agent pipeline (Planner → Curator → Copy → Builder → Style-critic → Contrast/Access → Responsive → Browser-verifier → Editor-fixer → Gatekeeper). Step 1 was executed *as one operator* by Claude, with the Playwright walk serving as the browser-verifier's work. No `build-report.md`, no sub-scorecards from style-critic / contrast / responsive agents, no release-gatekeeper aggregation. AP8 is unclosed.

### R7 · Release-gatekeeper prompt CRITICAL list is inconsistent with the authoritative scorecard

`factory/agents/release-gatekeeper.md` §1 lists CRITICAL dimensions as `(D1, D2, D4, D9, D10, D11, D12, D13, D14)`. `factory/standards/corporate-suite-quality-scorecard.md` §3 / §5 / §6 lists `(D1, D2, D3, D4, D10, D11, D12, D13, D14)`. The gatekeeper would currently apply the wrong Layer-2 floor on the archetype's first real run. One-line documentation fix; must land before a gatekeeper is ever invoked on a template on this archetype.

### R8 · No evidence that the static-file contract tests run under the project's CI floor for the hardening branch

Step 1A/1B/1C added `CorporateSuiteThemeSafetyTests` (7), `CorporateSuiteChromeContractTests` (7), `CorporateSuiteImageryPolicyTests` (6), `CorporateSuiteRhythmContractTests` (8). 28 new static tests. The report claims "32/32 green" but the Step 2 baseline does not include a recorded, dated `python manage.py test apps.catalog -v 2` transcript at tip `0727aad` under `factory/reports/`. The claim is not independently verifiable from factory-tree evidence alone. Step 2 must produce a canonical test transcript at the hardening-followup branch tip before any readiness claim holds.

---

## 2 · Archetype-level gaps still open (post Step 1)

Grouped by the standards anchor each gap rolls up to. Each row is archetype-level by construction; none are per-template defects.

| # | Gap | Standards anchor | Step 1 status | Residual work |
|:-:|---|---|---|---|
| G1 | Build-time palette gate (AP1 → CI floor) | `CS-PAL-01` · `O1` · `D12` | Live-render `UserWarning` only | Add a `manage.py` check subclass OR a pre-commit hook that reads every enrolled `primary` via `theme_safety.is_primary_safe_on_cream` and exits non-zero on fail. Target: a regression that reintroduces `#F7F3EC` fails CI before review. |
| G2 | Build-time imagery-policy gate (AP3/CS-IMG-SRC-01 → CI floor) | `CS-IMG-SRC-01` · `O7` · `D11` | Live-render `UserWarning` only | Wrap `enforce_corporate_suite_imagery_policy` in a `manage.py check` or script that iterates every registered pool and flags non-Pexels URLs on non-legacy-exempt keys. Exit non-zero on fail. |
| G3 | AP3 Pragma Pexels retro-pack | `CS-IMG-SRC-01` legacy exception · `CS-IMG-COH-06` | GRANDFATHERED | Produce `docs/content-factory/imagery/packs/business-corporate.md` via `imagery-curator` (primary + reviewer pass). Swap the 6 Unsplash URLs in `preview_imagery.py` via `template-editor-fixer`. Shrink `LEGACY_EXEMPT_KEYS` to `{}`. |
| G4 | AP8 first end-to-end pipeline run on Fiscus (not Solaria) | SOP §4.1 · `CS-BROWSER-01..03` · `O18` | UNCLOSED — Step 1 ran as one operator | Re-walk Fiscus through the populated 10-agent pipeline; produce `build-report.md`, `style-critic.md`, `contrast-accessibility.md`, `responsive-auditor.md`, `verdict.md`, and the gatekeeper's final scorecard. Validates the pipeline before Solaria's 4 locales add 4× the surface area. |
| G5 | AP10 D-054 triangulation drift | `CS-EXEC-02` · `CS-BLOCK-12` · `O12` | UNCLOSED | Refresh Pragma + Fiscus module docstrings so each triangulates against **every** on-archetype sibling (Pragma ↔ Fiscus; both ↔ Solaria once it un-pauses). Content-side, planner-driven, zero skin edits. |
| G6 | AP12 reduced-motion JS verification (45 `[data-lm]` hooks × 6 pages) | `CS-RESPONSIVE-07` · `BRWS-FEEL-08` · `E2` | PARTIAL — CSS `@media (prefers-reduced-motion)` present; JS side not exhaustively verified | Audit `static/js/live-motion.js` behavior under `prefers-reduced-motion: reduce`. Every `[data-lm]` reveal must either (a) skip animation or (b) run instant-finalized. Live walk at the OS-level reduced-motion toggle confirms no opacity-0 frozen panels. |
| G7 | RTL (AR) live walk across full matrix | `CS-RESPONSIVE-07` · `BRWS-RESP-07` (strong) · `CS-BROWSER-01` | DEFERRED under Round 1 deviation 1 | Playwright walk at `?lang=ar` on Pragma (6 pages) and Fiscus (6 pages) at the 8-viewport §5 matrix. Confirm token stack carries; logical-property flips hold; Noto Kufi / Amiri metrics don't overflow nav at 768 or 390. |
| G8 | Multi-locale (EN / FR / ES) live walks | `BRWS-VIEW-01` · `BRWS-FEEL-05` | DEFERRED under Round 1 deviation 2 | Playwright walk on 3 additional locales × same page/viewport matrix. Closes BRWS-FEEL-05 (voice anchor verbatim) across the rubric's locale set. Risk of nav label wrap is already blunted by the 880 drawer breakpoint; walk confirms it. |
| G9 | Footer legal `href="#"` placeholders on enrolled templates | `CS-CTA-04` | UNCLOSED (pre-X.4a backlog called out in Step 1B §remaining weak points) | Route wiring in the `_base.html` footer block: `{% url %}` targets for privacy / cookie / legal, or the corresponding `site.privacy_url` / `site.cookie_url` / `site.legal_url` on the site-config primitive. Archetype-level: the routes must exist on every corporate-suite template. |
| G10 | Primary-CTA solid-filled variant on paper surfaces | `CS-CTA-01` · `CS-HERO-04` | DEFERRED (Step 1B §remaining weak points flagged it, 1D did not touch) | Add `.cs-btn-primary--solid` modifier OR a paper-scoped override keyed to `.cs-lead` / hero. Resolves the current outline-only primary on cream which reads as "placeholder", not "executive button". Must coexist with the `.cs-cta .cs-btn-primary` override on the dark CTA band. |
| G11 | Ghost CTA touch-target floor under 44 × 44 on mobile | `CS-CTA-03` · WCAG 2.1 SC 2.5.5 | DEVIATION (waived under `CS-CTA-03` ghost = text link) | Either (a) keep the deviation and codify it as a permanent footnote in `CS-CTA-03` language; or (b) promote the mobile-viewport ghost CTA to meet 44 × 44 via padding without changing desktop visuals. Decision point for Step 2, not an implementation. |
| G12 | Release-gatekeeper CRITICAL-dimension list inconsistency | `release-gatekeeper.md §1` vs `quality-scorecard.md §3/§5/§6` | UNCLOSED | One-line edit in the agent prompt to swap D9 for D3 in the CRITICAL list. Trivial, must land before any gatekeeper invocation on this archetype. |
| G13 | Canonical dated test transcript for the hardening contract tests | `factory/reports/build/` · evidence discipline | MISSING | Run `python manage.py test apps.catalog -v 2` on the followup branch tip; capture the transcript under `factory/reports/hardening/step2-ci/`. Closes R8 self-consistency. |
| G14 | Pack-file per-slot metadata enforcement (width / crop / caption-role-coherence 3-line) | `CS-IMG-COH-06` · `CS-IMG-CROP-02` | PARTIAL — Step 1C helper flags hero width < 1600 only | Extend `imagery_policy.py` validator to read the pack file (`docs/content-factory/imagery/packs/<cluster>.md`) and assert the 3-line record per URL + crop-aspect contract. Soft-warn until a cluster's pack is present; hard-fail for clusters where the pack is declared present. |
| G15 | Cross-cluster URL-reuse at the request-path layer | `CS-IMG-SRC-04` | NOT ENFORCED — only `scripts/check_imagery_pack.py` greps duplicates | Optional: add the duplicate-URL check to the `imagery_policy.py` enforcement at the archetype gate. Low priority; the pack-time grep is the authoritative layer. |
| G16 | Scrolled-state affordance for sticky nav (IntersectionObserver → `.cs-nav--scrolled`) | `CS-NAV-04` (aspirational) | DEFERRED in Step 1B § | Skin-scoped JS. Low priority; adds premium polish. Not a gate item. |

**Closed during Step 1 — no Step 2 work required**:
AP1 palette skin layer (1A) · AP2 responsive breakpoints IT/LTR (1D) · AP7 `--primary-2` dead code retired (1A) · AP11 dark-surface descendant cascade (1A) · CS-BLOCK-N-02 one-accent-in-nav (1B) · CS-HERO-01 3-stop overlay floor (1B) · CS-FOOT-02 footer legal AA (1A+1B) · CS-TYPE-04 type-scale ceiling (1C) · CS-RHYTHM-01 section-padding tokens (1C) · CS-IMG-SEC-01/02 pillars+KPI `display:none` guardrails (1C) · CS-RESPONSIVE-01..03 LTR @ 8 viewports (1D) · marquee phantom scroll via `overflow-x: clip` root guard (1D) · hamburger drawer at 880 (1D).

---

## 3 · Hardening tasks grouped by priority

Three priority bands. **P0** blocks any further readiness claim. **P1** blocks Solaria Commit B un-pause but can land after the P0 bundle clears. **P2** must land before the archetype's **next** pilot but is deferrable past Solaria.

### P0 · Unblocks the "ready to plan un-pause" verdict (all archetype-level, no template patching)

- **T-P0-1 · Build-time palette gate** — promote `theme_safety.is_primary_safe_on_cream` from `UserWarning` to a `django.core.checks` registration or a `manage.py check_corporate_suite_palettes` management command that exits non-zero on failure. Wire into the default CI floor. Closes G1. Anchor: `CS-PAL-01` / `O1` / `D12`. Scope: `apps/catalog/` (archetype-gated module only — no editor/projects/commerce). Evidence: a failing run log for the known-bad Solaria pre-fix palette, a passing run log for all three enrolled palettes, transcript captured under `factory/reports/hardening/step2-ci/`.
- **T-P0-2 · Build-time imagery-policy gate** — same promotion pattern for `enforce_corporate_suite_imagery_policy`. Iterates every key in `CORPORATE_SUITE_POOL_KEYS`, subtracts `LEGACY_EXEMPT_KEYS`, fails CI on any non-Pexels URL. Closes G2. Evidence under `factory/reports/hardening/step2-ci/`.
- **T-P0-3 · Release-gatekeeper CRITICAL list alignment** — edit `factory/agents/release-gatekeeper.md §1` to swap `D9` for `D3`. Closes G7 / G12. One-line diff; no scope creep into other sections. Archetype-level because the prompt is shared across every corporate-suite run.
- **T-P0-4 · AP12 reduced-motion JS verification walk** — trigger `prefers-reduced-motion: reduce` (OS-level or Playwright `browser_emulate_media`) and walk Pragma home + about + services + case-study list + case-study detail. Every `[data-lm]` element must render visible (no stuck opacity-0). Closes G6 / E2. Evidence: transcript + screenshots under `factory/reports/browser-verification/x4a-step2/<run-timestamp>/reduced-motion/`.
- **T-P0-5 · Footer `href="#"` resolution** — wire privacy / cookie / legal to real routes (either via `site.<x>_url` primitives or via the existing i18n legal page set). Closes G9 / `CS-CTA-04`. Scope confined to `_base.html` footer block + the site-config lookups.
- **T-P0-6 · Canonical dated test transcript** — execute `python manage.py test apps.catalog -v 2` on the `phase-x4a-corporate-factory-hardening-followup` branch tip; capture transcript verbatim under `factory/reports/hardening/step2-ci/test-run-<ISO>.txt`. Closes G13 / R8.

P0 total: 6 tasks. None requires `apps/editor`, `apps/projects`, or `apps/commerce` edits. None touches Solaria source.

### P1 · Unblocks Solaria Commit B un-pause

- **T-P1-1 · Multi-locale live walk (IT · EN · FR · ES) across full §5 matrix** — Pragma (6 pages) + Fiscus (6 pages) × 4 locales × 8 viewports = 384 cells. Playwright MCP, driven by `browser-verifier` agent. Closes G8. Evidence under `factory/reports/browser-verification/x4a-step2/<run-timestamp>/`.
- **T-P1-2 · RTL (AR) live walk across full §5 matrix** — same scope for AR. Confirms token stack survives `html[dir="rtl"]`; validates Kufi / Amiri metrics at 390 × 844; verifies logical-property flips. Closes G7 / `BRWS-RESP-07`.
- **T-P1-3 · AP8 first end-to-end multi-agent pipeline re-walk of Fiscus** — drive Fiscus through the populated 10-agent pipeline (`template-planner` retro read → `imagery-curator` reviewer pass → `copy-translation-agent` verbatim re-check → `template-builder` CI re-run → observation agents → `browser-verifier` → `release-gatekeeper`). Produces one instance of every SOP §6 report schema. Closes G4. Validates pipeline before Solaria's 4 new locales × 240 walk cells land on it.
- **T-P1-4 · AP10 D-054 triangulation refresh** — update `template_content_pragma.py` + `template_content_fiscus.py` module docstrings so each triangulates against every on-archetype sibling (and, when un-paused later, against Solaria). Content-side; planner-driven; zero skin edits. Closes G5 / `CS-BLOCK-12`.
- **T-P1-5 · Primary-CTA paper-surface solid variant decision** — adopt or reject `.cs-btn-primary--solid` (or a hero-scoped override). Documented decision lands in `factory/standards/corporate-suite-design-standard.md` as a `§ decision` entry regardless of direction chosen. Closes G10.

P1 total: 5 tasks. Expected cumulative duration dominated by T-P1-1 + T-P1-2 (the full multi-locale + RTL Playwright walk).

### P2 · Deferrable past Solaria

- **T-P2-1 · AP3 Pragma Pexels retro-pack** — curator (primary + reviewer pass) produces `docs/content-factory/imagery/packs/business-corporate.md`. Editor-fixer swaps the 6 Unsplash URLs. `LEGACY_EXEMPT_KEYS` shrinks to `{}`. Closes G3. Soft precondition for Solaria per `template-inventory.md §7 item 4`; hard precondition for the archetype's **next** pilot.
- **T-P2-2 · Pack-file 3-line metadata + crop validator** — extend `imagery_policy.py` to read the pack file and assert `CS-IMG-COH-06` per URL + `CS-IMG-CROP-02` crop-aspect contract. Closes G14. Uplift over the current "width ≥ 1600 soft-warn" floor.
- **T-P2-3 · Ghost CTA touch-target decision** — waiver permanent (codify under `CS-CTA-03` § footnote) OR promote to 44 × 44 mobile floor. Closes G11. Documented decision, trivial implementation either way.
- **T-P2-4 · Cross-cluster URL-reuse at the request-path layer** — optional, low priority. `scripts/check_imagery_pack.py` already covers pack-time. Closes G15.
- **T-P2-5 · Sticky-nav scrolled-state JS affordance** — optional polish. Adds `.cs-nav--scrolled` via IntersectionObserver; deeper shadow / tighter height. Closes G16.

P2 total: 5 tasks. None gates Solaria. All gate the archetype's fourth-and-beyond pilot.

---

## 4 · What must be fixed before Solaria can re-enter

Binding list. All rows below must be green before any planner activity on Solaria Commit B starts. Solaria continuation remains user-authorized only.

1. **Every P0 task clears** (T-P0-1 through T-P0-6). In particular: the build-time palette gate must fail on the known-bad Solaria pre-fix palette `#F7F3EC` in a captured transcript. That transcript is the proof-of-guardrail.
2. **Every P1 task clears**, with two surfaces load-bearing:
   - T-P1-1 + T-P1-2 — the multi-locale + RTL walks produce rubric-PASS evidence across **at least Pragma + Fiscus × 5 locales × 6 pages × 8 viewports**. The standard is 240 cells per template; the Step 2 walks re-establish that bar on the two LIVE templates before Solaria adds its own 240.
   - T-P1-3 — the AP8 end-to-end Fiscus re-walk lands one instance of every SOP §6 report. The 10-agent pipeline has been exercised once on a known-good template before it is exercised on Solaria's 4 new locales.
3. **`LEGACY_EXEMPT_KEYS` status is documented**. T-P2-1 (AP3 retro-pack) is preferred but not binding for Solaria. If Solaria un-pauses while the legacy exemption stands, the release-gatekeeper must explicitly call the grandfather out in the final scorecard under `O7`.
4. **User explicit un-pause instruction**. The binding "Solaria paused" instruction is a user-owned lever. No Step 2 work un-pauses it implicitly.

If any row above is red, Solaria Commit B stays paused. No exceptions.

---

## 5 · What can wait until after Solaria

Items that do not gate Solaria Commit B continuation:

- **T-P2-1 Pragma Pexels retro-pack**. Pragma's 6 Unsplash URLs are license-permissive and visually approved at the Round 1 walk. The archetype can accept Solaria continuation with the grandfather in place as long as the gatekeeper cites it explicitly.
- **T-P2-2 Pack-file metadata validator uplift**. Current "hero width ≥ 1600 soft-warn" is sufficient for Solaria's own pool (authored via X.3 C3 protocol, already compliant).
- **T-P2-3 Ghost CTA touch-target decision**. Current waiver is load-bearing and defensible under `CS-CTA-03`.
- **T-P2-4 Cross-cluster URL-reuse request-path check**. Pack-time grep is authoritative; duplicates would be caught at Solaria's pack review, not at render time.
- **T-P2-5 Sticky-nav scrolled-state JS affordance**. Pure polish; no rubric rule requires it.
- **G16 (IntersectionObserver `.cs-nav--scrolled`)**. Same framing as T-P2-5.
- **Retroactive motion-audit of sibling archetypes** (outside corporate-suite). Out of factory scope.

The deferral is not a waiver. Each row stays tracked in `template-inventory.md §7` until closed; every archetype pilot after Solaria's un-pause must cite the tracked state in its planner brief.

---

## 6 · Required live browser verification for Step 2

Walks are driven by the `browser-verifier` agent (Playwright MCP). Evidence under `factory/reports/browser-verification/x4a-step2/<run-timestamp>/`. Each walk produces a `verdict.md` conformant to `corporate-suite-browser-rubric.md §11`.

### 6.1 · Walk V1 · Reduced-motion audit (P0 · T-P0-4)

- Driver: `responsive-auditor` + `browser-verifier`.
- Trigger: `prefers-reduced-motion: reduce` via Playwright `emulate_media`.
- Scope: Pragma (6 pages) + Fiscus (6 pages) at 1440 × 900 only. One viewport is sufficient because the contract under test is JS-side motion, not CSS layout.
- Checks:
  - Every `[data-lm]` element renders with its final opacity / transform applied at page-ready. No stuck opacity-0 panels.
  - No motion-triggered layout shift with reduced-motion on.
  - Console clean (0 errors, favicon 404 ignored).
- Expected evidence: 12 pages × 1 viewport = 12 full-viewport screenshots, 1 `verdict.md`, 1 `walk-log.md`.
- Exit criterion: zero `[data-lm]` stuck-invisible cases; BRWS-FEEL-08 PASS on both templates.

### 6.2 · Walk V2 · Multi-locale LTR walk (P1 · T-P1-1)

- Driver: `browser-verifier`.
- Scope: Pragma + Fiscus × (EN, FR, ES) × 6 pages × 8-viewport matrix = **288 cells per template**, **576 cells total**.
- Checks: every `BRWS-*` rubric check from `browser-rubric.md §6` runs at the sampled subset; BRWS-FEEL-05 voice-anchor verbatim runs on every page per locale.
- Evidence per locale: 24 screenshots (6 pages × 4 core viewports — wide / std / tablet-portrait / small-phone) per template = 48 total per locale × 3 locales × 2 templates = **288 screenshots minimum**. Rubric §7 baseline is 120/walk.
- Exit criterion: zero `[BLOCKING]` failures, zero `[REQUIRED]` failures, deviations logged with justification.

### 6.3 · Walk V3 · RTL (AR) full matrix (P1 · T-P1-2)

- Driver: `browser-verifier`.
- Scope: Pragma + Fiscus × AR × 6 pages × 8-viewport matrix = **96 cells per template**, **192 cells total**. (AR is a single locale so the matrix shrinks.)
- Load-bearing focuses: logical-property flips on chrome (nav, footer), RTL-Latin numeric cascade preserved, Kufi+Amiri glyph metrics at 390 × 844 do not overflow, focus-visible survives `dir="rtl"`.
- Evidence: ≥ 48 screenshots per template; `verdict.md`; per-cell scrollWidth/clientWidth table under `measurements.md`.
- Exit criterion: same as V2.

### 6.4 · Walk V4 · AP8 first end-to-end Fiscus re-walk (P1 · T-P1-3)

- Driver: full 10-agent SOP pipeline in re-walk mode.
- Scope: Fiscus IT only at first pass (the pipeline produces one instance of each agent report). If any observation agent surfaces a `[BLOCKING]` defect, the pipeline loops via `template-editor-fixer` before re-walk.
- Evidence directory: `factory/reports/build/fiscus-commercialista/` + `factory/reports/browser-verification/fiscus-commercialista/<run-timestamp>/` + `factory/reports/scorecard/fiscus-commercialista/<run-timestamp>-scorecard.md`.
- Exit criterion: full scorecard issued by `release-gatekeeper`, Layer 1 / 2 / 3 clear, parallel-verification handshake complete.

### 6.5 · Sampling rule for V2 + V3

The 8-viewport matrix runs **per page per locale**. A reduced "4 core viewports × 6 pages" subset is the evidence minimum per §7 of the rubric. A fuller 8-viewport sweep is the optimum. Deviations (e.g., a single viewport skipped because it replicates behavior) must be logged explicitly in `verdict.md` under `§ deviation`.

---

## 7 · Commit sequencing recommendation

Binding order. Each commit is archetype-level; no commit modifies more than one app scope (`apps/catalog`) or one archetype surface (`corporate-suite` skin + page files). Every commit carries its own `factory/reports/` evidence.

```
C-P0-1  Add build-time palette gate (T-P0-1)
         apps/catalog/{theme_safety.py,checks.py,apps.py,tests.py}
         factory/reports/hardening/step2-ci/palette-gate-<ISO>.log

C-P0-2  Add build-time imagery-policy gate (T-P0-2)
         apps/catalog/{imagery_policy.py,checks.py,tests.py}
         factory/reports/hardening/step2-ci/imagery-gate-<ISO>.log

C-P0-3  Release-gatekeeper CRITICAL list alignment (T-P0-3)
         factory/agents/release-gatekeeper.md

C-P0-4  AP12 reduced-motion walk V1 evidence (T-P0-4)
         factory/reports/browser-verification/x4a-step2/<run>/reduced-motion/...

C-P0-5  Footer legal href resolution (T-P0-5)
         templates/live_templates/business/corporate-suite/_base.html
         (+ site-config primitives if required)

C-P0-6  Canonical dated test transcript (T-P0-6)
         factory/reports/hardening/step2-ci/test-run-<ISO>.txt

--- P0 closure gate · no P1 commit lands before this line clears ---

C-P1-1  Walk V2 multi-locale LTR evidence (T-P1-1)
         factory/reports/browser-verification/x4a-step2/<run>/multi-locale-ltr/...

C-P1-2  Walk V3 RTL full matrix evidence (T-P1-2)
         factory/reports/browser-verification/x4a-step2/<run>/rtl-ar/...

C-P1-3  AP8 end-to-end Fiscus re-walk (T-P1-3)
         factory/reports/{build,browser-verification,scorecard}/fiscus-commercialista/...

C-P1-4  AP10 D-054 triangulation refresh (T-P1-4)
         apps/catalog/template_content_pragma.py (docstring only)
         apps/catalog/template_content_fiscus.py (docstring only)

C-P1-5  Primary-CTA paper-surface solid variant decision (T-P1-5)
         factory/standards/corporate-suite-design-standard.md (§ decision entry)
         templates/live_templates/business/corporate-suite/_base.html (if adopted)

--- P1 closure gate · Solaria Commit B re-entry is now a user decision, not a gate ---

C-P2-*  Deferrable items. Each as its own commit with its own evidence.
```

Rationale notes:

- **P0 bundle clears CI-surface risk first**. Every later walk is more trustworthy once palette + imagery gates are build-time, not runtime.
- **P0-3 (one-line gatekeeper fix)** can technically land anywhere; placed inside P0 because it is a prerequisite for any gatekeeper invocation in P1-3.
- **P1 commits C-P1-1 through C-P1-3 can run in parallel** across multiple Playwright sessions **iff** the P0 commits are already in place. Serial execution is the safer default — parallel walks share the dev server port and the risk of evidence collision is real.
- **C-P1-4 (D-054 triangulation refresh) lands after C-P1-3** because the Fiscus re-walk exercises the current docstrings as-is. Refreshing them before the re-walk would mix two changes and muddy the pipeline-validity signal.
- **Never squash P0 and P1**. The P0 gate needs to be provable-green before P1 starts.

---

## 8 · Blocking conditions that remain unresolved

Independent of Step 2 work, the following conditions still pin the archetype and will remain until explicit action:

- **B1 · Solaria Commit B paused** — binding user instruction. Not a Step 2 lever. Remains until user un-pauses.
- **B2 · `LEGACY_EXEMPT_KEYS = {business-corporate}`** — Pragma's 6 Unsplash URLs remain the archetype's tolerated exception until T-P2-1 lands. Every walk must acknowledge.
- **B3 · `apps/editor`, `apps/projects`, `apps/commerce` edit ban** — per SOP §7.6. No Step 2 task is permitted to touch these paths.
- **B4 · No new archetypes during X.4a** — same anchor. Step 2 may not propagate corporate-suite contracts to sibling archetypes; propagation is a separate phase.
- **B5 · `BRWS-EVID-01..03` evidence discipline** — every walk must produce a `verdict.md` conformant to rubric §11. No implicit passes. No missing screenshots on critical cells.
- **B6 · `primary L*` binding** — any palette hex change on any enrolled corporate-suite template bypasses a Planner re-approval loop if it skips the Builder self-check. Step 2 must not un-bind this.
- **B7 · Preview-composition file** — `templates/preview_compositions/business/corporate-suite.html` (313 lines, 0 media queries) is out of scope for Step 1. It remains out of scope for Step 2 unless a specific rubric failure surfaces on it during V2 / V3. Tile PNGs are a separate quality surface.
- **B8 · Single dev-server port invariant** — parallel walks on the same port corrupt the evidence set. Either serialize or use distinct ports (`:8731`, `:8732`, …).

---

## 9 · Recommended agent usage for Step 2 execution

Each Step 2 task maps to one or more `factory/agents/*.md` roles. Agent prompts are already populated; Step 2 is the first test of whether those prompts are self-sufficient. When a prompt proves underspecified during execution, log the gap under `factory/reports/hardening/step2-ci/agent-gaps.md`; it becomes Step 3 work (prompt hardening), not Step 2 blocker.

| Task | Primary agent | Secondary / handoff |
|---|---|---|
| T-P0-1 palette build-time gate | `template-builder` (implements the check) | `release-gatekeeper` (verifies scorecard integration) |
| T-P0-2 imagery build-time gate | `template-builder` | `imagery-curator` (reviews coverage) · `release-gatekeeper` |
| T-P0-3 gatekeeper CRITICAL alignment | `release-gatekeeper` (self-edit) | user review (prompt diff) |
| T-P0-4 reduced-motion walk V1 | `responsive-auditor` + `browser-verifier` | `template-editor-fixer` (only if FAIL) |
| T-P0-5 footer `href` resolution | `template-editor-fixer` | `style-critic` (CS-CTA-04 spot check) |
| T-P0-6 test transcript | `template-builder` (CI execution) | none |
| T-P1-1 multi-locale LTR walk V2 | `browser-verifier` | `contrast-accessibility-auditor` (tracks BRWS-CONTRAST-* per locale) · `copy-translation-agent` (verifies BRWS-FEEL-05 verbatim) |
| T-P1-2 RTL walk V3 | `browser-verifier` | `responsive-auditor` (AR glyph metrics at narrow viewports) |
| T-P1-3 Fiscus end-to-end re-walk | full pipeline — `template-planner` retro read → `imagery-curator` reviewer → `copy-translation-agent` re-check → `template-builder` CI → `style-critic` → `contrast-accessibility-auditor` → `responsive-auditor` → `browser-verifier` → `release-gatekeeper` | sequenced strictly; no parallelism inside this task |
| T-P1-4 D-054 triangulation refresh | `template-planner` (authors the refreshed docstring triangulation) | `style-critic` (confirms the new docstring reads against all siblings) |
| T-P1-5 primary-CTA solid decision | `style-critic` (recommends) | `template-editor-fixer` (implements if adopted) · `release-gatekeeper` (documents decision) |
| T-P2-1 Pragma retro-pack | `imagery-curator` (primary + reviewer pass) | `template-editor-fixer` (URL swap) |
| T-P2-2 pack metadata validator | `template-builder` | `imagery-curator` (spec review) |
| T-P2-3 ghost CTA touch-target decision | `style-critic` + user | — |
| T-P2-4 cross-cluster URL-reuse check | `template-builder` | `imagery-curator` |
| T-P2-5 sticky-nav scrolled-state | `template-editor-fixer` (skin JS) | `style-critic` |

Agent-usage binding rules:

- **No agent may sign its own work.** `template-editor-fixer` never verifies the fix it applied — a downstream observation agent (`browser-verifier`, `style-critic`, `responsive-auditor`) does.
- **`release-gatekeeper` is aggregator-only** (SOP §2.1). It never re-runs an observation agent's check; it consumes their `verdict.md` / sub-scorecards.
- **`template-planner` does not author copy** even on a content-only task (T-P1-4). Docstring refresh is triangulation-metadata authorship, not copy authorship — acceptable under SOP §7.
- **Parallelism is bounded by SOP §4.1 pipeline order**. V2 and V3 can overlap (independent locales); P0 tasks must complete before P1 tasks start.

---

## 10 · Clear exit criteria · No-Go → Conditional-Go → Go

### 10.1 · Current state · **No-Go** (tip `0727aad`)

- Step 1A/1B/1C/1D PASS on their narrow scope.
- Full-rubric coverage is ≈ 6 % of the required surface (IT LTR only).
- Three of six `⚠`-tagged precondition items from `template-inventory.md §7` are unclosed.
- Two contract surfaces (palette, imagery) are runtime-only; no build-time failure.
- One documentation inconsistency (gatekeeper CRITICAL list) pins the first pipeline run.

### 10.2 · Conditional-Go · issued when P0 closes

Conditions, all required:

- Every P0 task green (T-P0-1 through T-P0-6).
- Canonical test transcript captured at hardening-followup branch tip (T-P0-6 / G13).
- Reduced-motion walk V1 PASS with BRWS-FEEL-08 green on both LIVE templates.
- Gatekeeper agent prompt CRITICAL list matches the scorecard.

Issuing authority: `release-gatekeeper` writes `factory/reports/hardening/step2-conditional-go.md` citing each row. The verdict is **Conditional-Go**, not Go — it unblocks Step 2 P1 work but does not un-pause Solaria.

### 10.3 · Go · issued when P1 closes

Conditions, all required (on top of Conditional-Go):

- Multi-locale LTR walk V2 PASS: zero `[BLOCKING]`, zero `[REQUIRED]` fails across the 4 locales × 6 pages × 4+ viewport core set per template.
- RTL walk V3 PASS at AR with the same bar, especially at 390 × 844.
- AP8 Fiscus end-to-end re-walk PASS: all SOP §6 reports present; scorecard Layer 1/2/3 clear; parallel-verification handshake signed.
- AP10 D-054 docstring refresh merged on both Pragma + Fiscus content modules.
- Primary-CTA paper-surface decision recorded (adopted or rejected).

Issuing authority: `release-gatekeeper` writes `factory/reports/hardening/step2-go.md` with the full scorecard aggregated. **Go means "archetype is ready to accept Solaria Commit B re-entry when the user un-pauses."** It does **not** itself un-pause Solaria.

### 10.4 · Failure modes on the path

- Any P0 walk FAIL → P0 loops via `template-editor-fixer` → re-walk at fresh `<run-timestamp>`. P1 does not start until P0 clears.
- Any P1 walk FAIL on a `[BLOCKING]` rule → pipeline loops via `template-editor-fixer` → re-walk. Solaria Commit B re-entry stays blocked.
- Any P1 walk PASS with `§ deviation` entries → each deviation must be either (a) waived with written justification accepted by `release-gatekeeper` OR (b) converted into a P2 task and tracked in `template-inventory.md §7`.
- Gatekeeper scorecard Layer-1 CRITICAL dimension below the floor → Go verdict refused regardless of other dimensions' scores.

---

## 11 · Boundaries honored by this plan

- No Solaria continuation — Commit B stays paused.
- No `apps/editor`, `apps/projects`, `apps/commerce` modification in any task above.
- No new archetypes introduced.
- Every written artifact lands inside `factory/*`.
- Every code artifact (T-P0-1, T-P0-2, T-P0-5, T-P1-4, T-P1-5) is confined to the `corporate-suite` archetype surface (the skin shell + page files) or the `apps/catalog/` archetype-gated helper modules that Step 1 already established.
- No template-local patching: every fix lands at the archetype (skin, `_base.html`, `apps/catalog/*` archetype-gated helpers, `factory/agents/*`, `factory/standards/*`, `factory/reports/*`).
- Evidence discipline: every task's completion requires a filesystem artifact under `factory/reports/`. Claims without artifacts are not closure.

---

## 12 · Final verdict · the hardening milestone Solaria must clear

**Solaria Commit B may re-enter the pipeline if and only if the Step 2 Go verdict of §10.3 is issued, with the full P0 + P1 bundle green and evidenced.**

Plain language: Solaria's un-pause is gated on a single named milestone — **Step 2 Go** — defined as:

1. Every archetype-level contract introduced in Step 1 is promoted from "warns at runtime" to "fails at CI" (T-P0-1, T-P0-2).
2. Every deferral logged in Step 1D Round 1 (RTL, EN/FR/ES, reduced-motion JS) is closed with live Playwright evidence (T-P0-4, T-P1-1, T-P1-2).
3. The multi-agent pipeline has run end-to-end once on a **known-good** template (Fiscus, not Solaria) and produced a full scorecard (T-P1-3).
4. The D-054 sibling triangulation on Pragma + Fiscus is refreshed to current-state reality (T-P1-4).
5. The documentation defects that would trip the first gatekeeper invocation (CRITICAL list, footer legal hrefs) are fixed (T-P0-3, T-P0-5).
6. A canonical dated CI-green transcript at the hardening-followup branch tip is committed as evidence (T-P0-6).

The absence of any one row above converts the milestone from Go to Conditional-Go (if P0 is complete) or No-Go (if P0 is incomplete) per §10. Solaria Commit B may not re-enter under Conditional-Go or No-Go.

Until **Step 2 Go** issues, the binding "Solaria paused" user instruction stands unchallenged, the `LEGACY_EXEMPT_KEYS` grandfather on Pragma's imagery stays acknowledged, and no further Solaria-scope work of any kind (content, imagery, skin, schema) is authorized by this plan.

— end of Step 2 follow-up plan —
