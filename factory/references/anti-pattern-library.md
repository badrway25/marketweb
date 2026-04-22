# Anti-pattern Library · `corporate-suite` archetype

**Audit baseline**: 2026-04-21 · **Refined**: 2026-04-22
**Source**: repo evidence — commits, file state, bug diffs, documented incidents.

Each entry: **evidence** (file:line or commit), **how it failed**, **how to detect**, **how to prevent**, the **standards anchor** (the `CS-BLOCK-*` / `O<n>` / `D<n>` rules in `factory/standards/*.md` that codify the failure as ship-gate enforcement), the **detector / fixer agent(s)** from the multi-agent SOP, and a **reusability tag** under the four-bucket model.

The legacy `[S0] / [S1] / [S2] / [S3]` severity letters are preserved for back-reference but the unified severity model `[BLOCKING] / [REQUIRED] / [STRONG] / [GUIDELINE]` from the standards is now the source of truth. The mapping is:

- `[S0]` → `[BLOCKING]` (typically merge-block AND LIVE-block)
- `[S1]` → `[BLOCKING]` LIVE-block, sometimes merge-block depending on whether the diff introduces it
- `[S2]` → `[STRONG]` (allowed with `§ deviation`) or tracked as archetype-debt
- `[S3]` → `[GUIDELINE]`

Every anti-pattern below is **ANTI-PATTERN** by definition (the four-bucket reusability tag). The interesting question is "is the existing instance grandfathered, fixed, latent, or systemic" — that's recorded per entry under `Status as of 2026-04-22`.

---

## 0 · How to use this document

1. Anti-patterns are evidence-anchored failure modes. The standards in `factory/standards/*.md` enumerate what does not ship; this file enumerates *why* (the historical or counterfactual incident) and *who catches it now*.
2. **Status as of 2026-04-22** records the live state: `FIXED`, `GRANDFATHERED`, `LATENT-ARCHETYPE-WIDE`, or `RECURRENT-RISK` (a defect class that can re-emerge on any new pilot if the gate is bypassed).
3. **Detector / fixer agent(s)** maps each AP to the SOP roles (`corporate-suite-multi-agent-sop.md` §2). The agent listed under "Detected by" runs the check; the agent listed under "Fixed by" applies the remediation. Most APs are detected by an observation agent and fixed by `template-editor-fixer`.
4. **Systemic** APs are marked with a ⚠ — these must close at the archetype level before Solaria Commit B un-pauses (cross-reference `template-inventory.md` §7).

---

## AP1 [S0 → BLOCKING · ANTI-PATTERN · FIXED on Solaria · LATENT-ARCHETYPE-WIDE without enforcement] · ⚠ Palette polarity inversion — `--primary` set to a light color
**File**: `apps/catalog/management/commands/seed_templates.py` · **Commit that caused it**: `e8f38b5` (Solaria Commit A) · **Fix**: `6b70d56`.

**What happened**: Solaria was seeded with `primary=#F7F3EC` (cream) intending it as the background. The skin uses `--primary` as the **foreground text color** (h1-h5, nav text, KPI numbers, buttons). Every headline, intro, CTA, and section-heading on every page rendered cream-on-cream — near-invisible body text.

**Why it slipped through**:
- `manage.py check`: 0 issues.
- `manage.py test apps.catalog`: 131/131.
- `manage.py test apps`: 506/506.
- Live browser verification: caught it immediately via DOM inspection.
- The skin's "dark-foreground convention" (pattern B2) was an **unenforced invariant**. No validator checked that `primary` is dark.

**Status as of 2026-04-22**: FIXED on Solaria branch (`6b70d56`). LATENT for any future pilot until the Builder L\* self-check binding holds AND the live walk runs. A pre-commit palette validator is still pending — see `template-inventory.md` §7 issue #1.

**Standards anchor**: `CS-PAL-01` (`primary` L\* ≤ 40 on cream · `[BLOCKING]`) · `CS-HERO-03` (hero h1 AAA target) · `CS-BLOCK-01` / `O1` enforces · `D12` Contrast safety [CRITICAL].

**Detected by**:
- `template-builder` first-line defense — palette L\* self-check refuses to advance past `draft` if L\* > 40 (SOP §3.4 · `build-report.md` line `primary L*: <value> · CS-PAL-01 PASS/FAIL`). The Builder report is **incomplete** without this line.
- `contrast-accessibility-auditor` second-line defense — hard-veto authority for O1 (SOP §3.6). Any `h1..h5` with RGB distance < 120 OR WCAG < 4.5 = automatic FAIL · Override O1 in the scorecard, regardless of any other dimension's score.
- `browser-verifier` runs `BRWS-CONTRAST-01` snippet at 1440 × 900 on each page × each locale; records per-headline distance + ratio in `measurements.json`.

**Fixed by**: `template-editor-fixer` — single-line hex change in `seed_templates.py` (palette change requires Planner re-approval per SOP §3.9). Re-run CI floor; fresh Browser Verifier walk at a new `<run-timestamp>`.

**Detection recipe** (canonical · per `corporate-suite-blocking-rules.md` §4 CS-BLOCK-R-01):
```js
// Run via mcp__plugin_playwright_playwright__browser_evaluate
(() => {
  const toRGB = (c) => c.match(/\d+/g).map(Number);
  const dist = (a, b) => Math.hypot(a[0]-b[0], a[1]-b[1], a[2]-b[2]);
  const body = toRGB(getComputedStyle(document.body).backgroundColor);
  return Array.from(document.querySelectorAll('h1,h2,h3,h4,h5'))
    .map(h => ({ tag: h.tagName, text: h.textContent.slice(0, 40),
                 distance: dist(toRGB(getComputedStyle(h).color), body) }))
    .filter(r => r.distance < 120);
})()
```
Any row in the returned array = fail.

**⚠ Systemic**: yes. Must close before Solaria Commit B (the EN/FR/ES/AR locales would inherit the same exposure if the validator + walk are not in place).

---

## AP2 [S0 → BLOCKING · ANTI-PATTERN · LATENT-ARCHETYPE-WIDE] · ⚠ Skin has ~zero responsive breakpoints — layout breaks below 1400px
**File audit** (repo-confirmed):

| File | Media queries | Reality |
|---|---:|---|
| `_base.html` | 1 | `prefers-reduced-motion` only — NOT a viewport breakpoint |
| `home.html` | 8 matches | **0 actual `@media` breakpoints** (grep `@media` → 0) |
| `about.html` | 6 matches | **0 actual `@media` breakpoints** |
| `services.html` | 3 | **0 actual `@media` breakpoints** |
| `case_study_list.html` | 2 | **0 actual `@media` breakpoints** |
| `case_study_detail.html` | 3 | **0 actual `@media` breakpoints** |
| `contact.html` | 6 | **1 real breakpoint** · `@media (max-width: 880px) { ... }` on `.cs-form form` only |
| **Preview composition** | 0 | 0 |

**By contrast** — `templates/live_templates/agency/agency-creative-studio/_base.html:349,359` has breakpoints at 1100px and 720px. So the repo DOES know how to do this; corporate-suite just doesn't.

**Why it failed**: fixed `padding: 72px` horizontal + fixed `grid-template-columns: 1.3fr 1fr` (36 sites across the archetype). Below ~1100px viewport, horizontal scroll appears; below ~720px the hero split becomes unusable.

**Status as of 2026-04-22**: LATENT-ARCHETYPE-WIDE on `main`. Affects all three enrolled templates (Pragma + Fiscus LIVE, Solaria draft) simultaneously. The hardening pass adds the breakpoints once and unlocks all three.

**Standards anchor**: `CS-RESPONSIVE-01..08` (target state) · `CS-HERO-07` (hero stacks at ≤ 720) · `CS-NAV-05` (nav condenses at 1100, hamburger at 720) · `CS-FOOT-05` (footer stacks at 720) · `CS-BLOCK-02` / `O2` (horizontal scrollbar) · `CS-BLOCK-03` / `O3` (hero stack + nav collapse at ≤ 720) · `D13` Responsive quality [CRITICAL].

**Detected by**:
- `responsive-auditor` — drives the §5 viewport matrix (1920 / 1440 / 1280 / 1024 / 768 / 640 / 414 / 390); hard-veto authority for O2 + O3 (SOP §3.7).
- `browser-verifier` — `BRWS-VIEW-02..07` at every viewport.

**Fixed by**: NOT `template-editor-fixer` for this AP — the SOP §7.6 explicitly excludes shared-skin edits from per-pilot remediation. The fix is a **separate hardening step** scoped at the archetype (one diff to `_base.html` + the 6 page files modeled on `agency-creative-studio/_base.html:349,359`). Until that step lands, every walk on this archetype is expected to FAIL O2/O3 — the LATENT exposure, not a per-pilot defect.

**Detection** (per `corporate-suite-blocking-rules.md` §12 CS-BLOCK-V-01):
```js
browser_resize({ width: <W>, height: <H> });  // for each rubric matrix viewport
browser_evaluate(() => ({
  sw: document.documentElement.scrollWidth,
  cw: document.documentElement.clientWidth,
  overflows: document.documentElement.scrollWidth > document.documentElement.clientWidth,
}));
```

**⚠ Systemic**: yes. **Must close before Solaria Commit B.** Without the breakpoints, the EN/FR/ES/AR locales × 6 pages × 8 viewports = 240 walk cells per locale, every one expected to FAIL O2 today.

---

## AP3 [S1 → BLOCKING · ANTI-PATTERN · GRANDFATHERED on Pragma] · Imagery source inconsistency — Pragma on Unsplash, Fiscus/Solaria on Pexels
**Files**:
- `preview_imagery.py:312-322` — `business-corporate` (Pragma) uses 6× `images.unsplash.com` URLs.
- `preview_imagery.py:346-358` — `business-fiscal` (Fiscus) uses 6× `images.pexels.com` URLs.
- `preview_imagery.py:370-383` (on branch) — `business-coaching` (Solaria) uses 6× `images.pexels.com`.

**Why it's a problem**:
- Project instructions: **Pexels-only imagery**.
- `docs/content-factory/imagery/CURATION_PROTOCOL.md` §2: "Pexels Primary."
- Pragma pre-dates the X.3 curation protocol (Session 32 vs X.3 Session 78+) — its URLs never went through a pack.

**Impact**: Pragma's imagery is legacy-Unsplash with no audit trail. License risk is low (Unsplash is permissive) but the curator audit + caption metadata + dedup grep that Fiscus/Solaria enjoy do not exist for Pragma.

**Status as of 2026-04-22**: GRANDFATHERED for Pragma (single tolerated exception per `CS-IMG-SRC-01` legacy paragraph and `corporate-suite-blocking-rules.md` §3 CS-BLOCK-07 grandfather note). RECURRENT-RISK if any new pilot tries to introduce non-Pexels URLs. The grandfather closes when the `business-corporate` Pexels retro-pack lands.

**Standards anchor**: `CS-IMG-SRC-01` (Pexels-only · `[BLOCKING]`) · `CS-IMG-AP-01` · `CS-BLOCK-07` / `O7` enforces · `D11` Pexels-only compliance [CRITICAL].

**Detected by**:
- `imagery-curator` (primary pass) runs `grep -E 'unsplash|shutterstock|getty|adobestock|istockphoto|pixabay|freepik'` against the new pack and **blocks itself** on non-zero (SOP §3.2 / curator-report.md mandatory grep block).
- `imagery-curator` (reviewer pass) re-runs the grep independently.
- `template-builder` re-runs the grep on the post-wire `preview_imagery.py` block.
- `browser-verifier` audits live `<img>.src` for Pexels host (BRWS-IMG-02).
- `release-gatekeeper` Layer 1 override O7 acknowledges the Pragma grandfather explicitly in the scorecard.

**Fixed by**: NOT a per-pilot fix. The retro-pack is its own deliverable: a `docs/content-factory/imagery/packs/business-corporate.md` produced by `imagery-curator` (primary + reviewer pass) followed by a `template-editor-fixer` swap of the 6 URLs in `preview_imagery.py:312-322`. Pragma stays LIVE as-is until the swap.

**⚠ Systemic**: partially. Not a hard precondition for Solaria specifically (Solaria's `business-coaching` pool is already Pexels), but the SOP §10.3 framing requires that the archetype not carry a perpetual exception. Tracked in `template-inventory.md` §7 issue #3.

---

## AP4 [S0 → BLOCKING · ANTI-PATTERN · RECURRENT-RISK] · Category-mismatched imagery
**Documented incidents** (from `docs/content-factory/imagery/blacklist.md` §1, Session 31):
- PlayStation gamepad as "map of Rome" on a real-estate template.
- Bumble Bee tuna can as "artisan ingredients" on a bottega.
- Hairstylists' portraits as "before/after dermatology" on a medical template.
- Diamond ring as "oysterman's portrait" on a Luxe editorial tile.

All shipped to production before Session 31. Each survived the author's own review because the author trusted the URL without reading what it depicted.

**Status as of 2026-04-22**: NO occurrence on the three enrolled corporate-suite templates today (Pragma + Fiscus + Solaria all pass the 3-second check). RECURRENT-RISK — the defect class survives any pipeline that lacks the curator + reviewer + browser-walk three-layer read.

**Standards anchor**: `CS-IMG-COH-01` (subject match to profession · `[BLOCKING]`) · `CS-IMG-AP-02` · `CS-BLOCK-05` / `O5` enforces · `D10` Imagery coherence [CRITICAL].

**Detected by** (three layers per `corporate-suite-blocking-rules.md` §10):
- `imagery-curator` 3-second read per URL at authoring (CURATION_PROTOCOL §3.3).
- `imagery-curator` (reviewer pass) 3-second read per URL at review (CS-IMG-SRC-05).
- `imagery-curator` (live re-read pass during walk · SOP §4.1 step 6) on the live render — `BRWS-IMG-03`.

**Fixed by**: `imagery-curator` re-sources the failing URL from the cluster-matched search; `template-editor-fixer` swaps it one URL at a time in `preview_imagery.py` (never bulk-swap).

**Prevention** (binding per CURATION_PROTOCOL §3.3): URL-by-URL human semantic review. "Open each URL, look at the image for 3+ seconds, ask 'does a person in this profession recognize this as their world?'" No pack = no authoring.

**⚠ Systemic**: no — the prevention is per-pilot, the detector layers are now in place. Cite as the load-bearing reason `imagery-curator` exists.

---

## AP5 [S1 → BLOCKING · ANTI-PATTERN · RECURRENT-RISK] · Generic stock fallback
**Failure modes** (`imagery/blacklist.md` §2):
- "Generic laptop on clean white desk"
- "Smiling businesswoman shaking hands in vague office"
- "Chef holding a plate, looking at camera, perfectly lit"
- "Multi-ethnic team pointing at a whiteboard"

**Detection**: "if the image could slot into 10+ unrelated clusters without changing meaning, it's a generic stock fallback."

**Status as of 2026-04-22**: NO occurrence on the three enrolled templates. RECURRENT-RISK on every new pilot if the curator does not apply the 10-cluster interchangeability test.

**Standards anchor**: `CS-IMG-PREM-05` (specificity reads premium) · `CS-IMG-STOCK-01` (10-cluster interchangeability test · `[BLOCKING]`) · `CS-IMG-AP-03` · `CS-BLOCK-IQ-02` enforces · `D9` Imagery quality.

**Detected by**:
- `imagery-curator` applies CS-IMG-STOCK-01 during sourcing; pack reviewer re-applies before approval.
- `browser-verifier` BRWS-IMG-08 spot-check.

**Fixed by**: `imagery-curator` re-sources with a specific subject (actual documents, actual instruments, actual room).

**Prevention**: curator names each slot's role in the pack file (e.g., "portrait-coach-clipboard", "detail-open-notebook-desk"). Generic shots have no role, so they fail the §4 semantic check.

---

## AP6 [S1 → BLOCKING · ANTI-PATTERN · FIXED · RECURRENT-RISK] · Cross-cluster URL reuse
**Incident** (`imagery/blacklist.md` §3, Session 38):
`portfolio-photographer[0-1]` reused `restaurant-fine[0-1]` URLs under a "proven offline-safe" rationale. Fix: swapped all 6 URLs.

**Status as of 2026-04-22**: NO cross-cluster overlap on the three enrolled corporate-suite pools (Pragma `business-corporate`, Fiscus `business-fiscal`, Solaria `business-coaching` — confirmed via the `preview_imagery.py` comments at lines 337-345 / 361-368). RECURRENT-RISK on every new pilot if the dedup grep is skipped.

**Standards anchor**: `CS-IMG-SRC-04` (one URL = one cluster · `[BLOCKING]`) · `CS-IMG-AP-04` · `CS-BLOCK-I-02` enforces · `D11` Pexels-only compliance.

**Detected by**:
- `imagery-curator` runs the cross-cluster dedup grep against every peer pack (SOP §3.2 mandatory grep block).
- CI script `scripts/check_imagery_pack.py` (X.3 C3) — exit code non-zero on duplicate URLs.

**Fixed by**: `imagery-curator` re-sources one of the two URLs.

---

## AP7 [S2 → STRONG · ANTI-PATTERN · LATENT-ARCHETYPE-WIDE · footprint enumerated 2026-04-22 = DEAD-CODE in this archetype] · Hardcoded `--primary-2: #2c3e6b;` not derived from brand
**File**: `_base.html:20` (declaration site, single archetype-wide).

**Why it's a problem (revised after grep audit 2026-04-22)**: every other token derives from `{{ theme.primary }} / .secondary / .accent`, but `--primary-2` is a hex literal. The original concern was that the navy hex would bleed onto non-Pragma palettes (Solaria warm-carbon, Fiscus charcoal). **Grep audit on 2026-04-22 (`var(--primary-2)` across `templates/`, `static/`, `apps/` = 0 hits)** revises the finding: the token is **declared but never consumed** in this archetype — dead code, not a bias-injecting token. The defect is "fourth-token convention violation present even when unused" (CS-PAL-03 in spirit), not "navy bias rendered on every page edge".

**Evidence (refined 2026-04-22)**: the same dead-code pattern is repeated in 3 other archetype `_base.html` files (`startup-saas-landing` `#1a1f3a`, `lawyer/modern-transparent` `#1A202C`, `lawyer/classic-gold` `#232340`) — all 4 declarations, 0 references. Cross-archetype dead-code; not a corporate-suite-only finding.

**Status as of 2026-04-22**: LATENT-ARCHETYPE-WIDE (cleanup-style, not contrast-style). The original "Solaria warm-earth inherits navy edge bias" claim is INCORRECT given 0 usages — recorded for historical traceability.

**Standards anchor**: `CS-PAL-03` (three tokens only — no hardcoded fourth color · `[REQUIRED]`). Listed as a known `[STRONG]` archetype-debt drift in design-standard §17 non-blocking examples and §19.7. The hardening fix is now **trivially "delete the declaration line"** rather than "derive server-side OR drop".

**Detected by**:
- `style-critic` (cross-cuts D3 modern professionalism) — flags as `[STRONG]` drift in the sub-scorecard with a `§ deviation` note.
- A grep audit of `var(--primary-2)` consumers — already executed 2026-04-22, footprint = 0 lines. No additional grep needed before remediation.

**Fixed by**: NOT `template-editor-fixer` per SOP §7.6 (shared-skin). The fix is a 1-line deletion in `_base.html:20`. Rolled into the AP2 hardening diff at zero marginal cost.

---

## AP8 [S1 → BLOCKING · ANTI-PATTERN · RECURRENT-RISK · CULTURAL] · Tests pass ≠ ship-ready
**Commit body verbatim** (`6b70d56`, Solaria palette fix): "Tests before/after: 506/506 apps · 131/131 catalog. **Live browser verification pending (this turn) before Commit A can be accepted.**"

**Pattern**: CLI green is a lower bound, not a ship signal. The full ship gate for this archetype is:
1. `manage.py check` — 0 issues
2. `manage.py test apps.catalog` — 131/131
3. `manage.py test apps` — 506/506 (now 506+ post-Fiscus)
4. `generate_previews` successful
5. **Live browser walk** — cream-on-cream check, viewport breakpoint check, imagery semantic check, contrast check
6. **Cross-locale browser walk** (IT/EN/FR/ES/AR) — language switcher, RTL polarity, Latin wordmark preservation

**Status as of 2026-04-22**: This is a **cultural** anti-pattern about over-trusting CI. RECURRENT-RISK on every release decision. The new standards encode the prevention as a hard-blocking rule.

**Standards anchor**: `CS-BROWSER-01..03` (browser live verification — acceptance gate · `[BLOCKING]`) · `CS-BLOCK-18` / `O18` enforces (no live walk = automatic FAIL) · `D14` Browser live verification quality [CRITICAL]. The premise is restated in `corporate-suite-design-standard.md` §15, `corporate-suite-blocking-rules.md` §1.3 + §20, `corporate-suite-browser-rubric.md` §2, `corporate-suite-quality-scorecard.md` §1.1, and `corporate-suite-multi-agent-sop.md` §1.1.

**Detected by**:
- `browser-verifier` is the canonical defense — refuses to walk if CI floor is red AND its absence triggers O18.
- `release-gatekeeper` Layer 1 override O18 — refuses the LIVE flip without a recorded walk.

**Fixed by**: not a code fix; a process fix. Run the rubric walk per `corporate-suite-browser-rubric.md` §10.

**⚠ Systemic**: yes — but the system is now in place (browser-verifier prompt populated, rubric written). Solaria Commit B must un-pause through the new pipeline, not around it.

---

## AP9 [S1 → BLOCKING · ANTI-PATTERN · LATENT (Solaria branch encodes the prevention)] · Coaching cluster clichés (deprecated phrases / imagery)
**File**: `cluster_blueprints/coaching.md` §13 (anti-pattern list encoded verbatim into Solaria's module docstring lines 22-34).

**Banned phrases** (cross-locale):
- "Sblocca il tuo potenziale" / "Unlock your potential"
- "Trasforma la tua vita in X giorni"
- "Versione migliore di te" / "Best version of yourself"
- "Mindset vincente" / "Winning mindset"
- Einstein / Jung / Gandhi / Steve Jobs quotes

**Banned imagery**:
- Mountain-peak photography
- Drawn arrows on whiteboards
- "10.000 persone hanno trasformato la loro vita con me" social-proof

**Banned structural moves**:
- "Diagnosi gratuita in 10 domande"
- Fake certifications (only ICF, EMCC, AICP acceptable)
- Therapy-domain overlaps ("supero ansia", "stress", "depressione")

**Status as of 2026-04-22**: LATENT on Solaria branch (the `template_content_solaria.py` IT module already encodes the blueprint §13 list in its docstring). RECURRENT-RISK on the EN/FR/ES/AR locale authoring (translator drift · `CS-REQ-09`).

**Standards anchor**: `CS-EXEC-04` (no marketing hyperbole · `[REQUIRED]`) · `CS-EXEC-03` (verifiable credentials · `[BLOCKING]`) · `CS-EXEC-07` (no funnel-pattern sections · `[REQUIRED]`) · `CS-IMG-AP-06` (coaching-cluster imagery clichés · `[BLOCKING]`) · `CS-BLOCK-P-05` (banned marketing hyperbole) · `CS-BLOCK-10` / `O10` enforces (fake certifications) · `CS-REQ-09` (banned phrase grep returns 1 hit in FR/ES/AR · `[REQUIRED]`).

**Detected by**:
- `copy-translation-agent` (live re-read pass) — banned-phrase grep across 5 locales (`copy-live-audit.md`).
- `style-critic` — BRWS-FEEL-04 banned-phrase grep · BRWS-FEEL-06 verifiable credentials check.
- `imagery-curator` (live re-read pass) — confirms zero coaching-cliché imagery on the rendered render (CS-IMG-AP-06).

**Fixed by**: `template-editor-fixer` — single-line content edit to the offending locale module.

---

## AP10 [S1 → STRONG · ANTI-PATTERN · LATENT-ARCHETYPE-WIDE for D-054 docstring drift] · Palette differentiation drift across siblings
**File**: `seed_templates.py:493, 553, 628+`.

**Current state**:
- Pragma: `#1E293B` navy · `#3B82F6` blue · `#10B981` emerald (advisory / corporate-blue)
- Fiscus: `#1F2937` charcoal · `#B58F4A` gold · `#1C3D5A` navy (institutional / warm-gold)
- Solaria post-fix: `#2B2A28` warm carbon · `#C8621A` ocra · `#8B5A2B` caramel (coaching / warm-earth)

**Why it matters**: D-054 demands visual differentiation; three dark-primary cream-body sites on the same skin must feel DIFFERENT. The secondary+accent pair is the diff vector (cool blue/emerald · cool gold/navy · warm ocra/caramel).

**Status as of 2026-04-22**: The three palettes today actually pass the differentiation test (cool/cool-warm/warm-earth axis). The LATENT-ARCHETYPE-WIDE drift is in the **D-054 10-gate docstrings**: Pragma triangulates against Elevate (different archetype); Fiscus triangulates against Pragma only; Solaria's docstring (on branch) triangulates against Pragma + Fiscus. With three siblings extant, both Pragma + Fiscus are now drift cases under the new `CS-EXEC-02` triangulate-against-every-sibling rule.

**Standards anchor**: `CS-PAL-02` (secondary + accent are the D-054 differentiation vector · `[BLOCKING]`) · `CS-EXEC-02` (D-054 10-gate triangulation against EVERY sibling · `[BLOCKING]`) · `CS-BLOCK-12` / `O12` enforces · `CS-BLOCK-VI-06` (D-054 10-gate single-sibling-only).

**Detected by**:
- `template-planner` — produces `factory/reports/plans/<slug>/d-054-triangulation.md` triangulating against ALL existing siblings (SOP §3.1).
- `copy-translation-agent` — mirrors the table into the IT module docstring (CS-BLOCK-12 first line).
- `release-gatekeeper` — Layer 1 override O12 fails the scorecard if absent.

**Fixed by**: `template-editor-fixer` for new pilots; for Pragma + Fiscus refresh, the docstring update is a separate (small) `template-editor-fixer` follow-up that touches the content modules only.

**⚠ Systemic**: yes (the docstring triangulation drift is archetype-wide). Tracked in `template-inventory.md` §7 issue #6.

---

## AP11 [S2 → BLOCKING · ANTI-PATTERN · RECURRENT-RISK] · Dark-section CSS text defaults missing `color: var(--on-dark)` on child elements
**Evidence**: `_base.html:230-232` — sets `h2, h3, h4 { color: var(--on-dark); }` INSIDE `.cs-section.dark`. This covers headings but every new dark section that adds new child text elements must explicitly opt into `on-dark`.

**Failure mode**: adding `.cs-cta .new-text { color: var(--ink); }` on a dark section = dark text on dark navy. Same as AP1 but scoped.

**Status as of 2026-04-22**: NO occurrence on the three enrolled templates today (no new dark-section child rules have been added since the skin was authored). RECURRENT-RISK every time a new dark-section component is introduced.

**Note**: the original entry tagged AP11 as `[S2]`, but the standards now tag it `[BLOCKING]` (CS-PAL-04 / CS-BLOCK-17 / O17). The reclassification reflects the load-bearing nature: a dark-on-dark text pocket is functionally identical to AP1 from the visitor's perspective. Severity escalated for the unified model.

**Standards anchor**: `CS-PAL-04` (dark-section child text uses `--on-dark` variants · `[BLOCKING]`) · `CS-BLOCK-17` / `O17` enforces · `D12` Contrast safety [CRITICAL].

**Detected by**:
- `contrast-accessibility-auditor` — BRWS-CONTRAST-02 sweeps every text descendant of `.cs-section.dark`, `.cs-kpi-band`, `.cs-nav`, `.cs-foot`. Hard-veto authority for O17 (paired with O1).
- `browser-verifier` runs the sweep snippet at 1440 × 900.

**Fixed by**: `template-editor-fixer` — explicit `color: var(--on-dark-2)` or `var(--on-dark-3)` on the offending selector. `--ink` is for light-paper surfaces only.

---

## AP12 [S2 → STRONG · ANTI-PATTERN · LATENT-ARCHETYPE-WIDE · footprint enumerated 2026-04-22] · Reduced-motion coverage is partial
**Evidence**: `_base.html:299-301` disables transitions on buttons and button arrows. `data-lm="reveal"` reveal animations use the global `static/js/live-motion.js` — unclear from this skin's CSS whether those also respect `prefers-reduced-motion`.

**Footprint (grep audit 2026-04-22)**: `data-lm` appears **45 times across 6 files** in the corporate-suite skin — `_base.html:1`, `home.html:19`, `about.html:11`, `services.html:7`, `case_study_list.html:4`, `case_study_detail.html:3`. Every page in the archetype is affected. `contact.html` is the only page with zero `[data-lm]` hooks.

**Detection**: load the live page with OS-level reduced-motion enabled (or `matchMedia('(prefers-reduced-motion: reduce)')` emulation in Playwright MCP) and verify no entrance animation fires on any of the 5 affected pages × 5 locales.

**Status as of 2026-04-22**: LATENT-ARCHETYPE-WIDE. 5 of 6 pages affected (contact.html is the only exception — 0 `[data-lm]` hooks). Not yet measured on a live walk.

**Standards anchor**: `CS-RESPONSIVE-07` (`:focus-visible` and reduced-motion survive all viewports · `[REQUIRED]`) · `BRWS-FEEL-08` (reduced-motion respected · `[STRONG]`) · `CS-REQ-06` (reduced-motion JS path unverified · `[REQUIRED]`).

**Detected by**:
- `browser-verifier` — BRWS-FEEL-08 emulates `prefers-reduced-motion: reduce` via `browser_evaluate(matchMedia(...))` or OS-level emulation; reload home; confirm no entrance animation fires.
- `contrast-accessibility-auditor` — cross-cuts D3 modern professionalism.

**Fixed by**: NOT `template-editor-fixer` — the fix is JS-side in `static/js/live-motion.js`, outside the per-pilot SOP §7.6 scope. Separate hardening step: extend the reduced-motion check to the `[data-lm]` opacity/transform transitions.

---

## Systemic issues surfaced (Pragma · Fiscus · Solaria in aggregate)

Cross-reference `factory/reports/audits/corporate-suite-audit-master.md` §4 (refined) and `factory/references/template-inventory.md` §7 for the dependency graph. The systemic issues that close at the archetype level (and therefore must close before Solaria Commit B) are:

1. ⚠ **Skin convention invariants are not encoded** — the "primary is dark foreground" rule (B2 / CS-PAL-01) is now defended by the Builder L\* self-check (SOP §3.4) + the Contrast Auditor's hard veto (SOP §3.6) + the Browser Verifier walk. A pre-commit palette validator is the still-pending automated complement (template-inventory §7 issue #1). **Status: enforcement layered, validator pending.**

2. ⚠ **Browser verification is central, not optional** — encoded as `CS-BROWSER-01..03` / `CS-BLOCK-18` / `O18`, plus the 10-agent SOP makes browser-verifier the single source of truth for downstream scoring. **Status: encoded; first end-to-end run still pending** (Solaria un-pause should NOT be the first run — re-walk Fiscus first per template-inventory §7 issue #7).

3. ⚠ **Responsive coverage is an archetype-level gap** — AP2. Fix lands once on `_base.html` + 6 page files modeled on `agency-creative-studio/_base.html:349,359`. **Status: LATENT; hardening fix pending.**

4. **Legacy imagery (Pragma Unsplash) is an invisible liability** — AP3. Closes when the `business-corporate` Pexels retro-pack lands (template-inventory §7 issue #3). **Status: GRANDFATHERED with retro-pack pending.**

5. ⚠ **D-054 is a content+palette+imagery contract** — and now a 3-way triangle. New pilots author against ALL three siblings via planner; Pragma + Fiscus docstrings should refresh on next touch. **Status: encoded for new pilots; sibling refresh pending.**

6. **No CI gate for palette L\* / contrast ratio / viewport responsive** — all three failure modes are human-walk-only today. The Builder L\* self-check is the closest thing to a CI gate; the rest depend on the browser walk. **Status: walk-side enforcement complete; CI-side enforcement pending (palette validator only).**

7. **Release-gatekeeper agent prompt CRITICAL-dimension list inconsistency** — `factory/agents/release-gatekeeper.md` §1 lists CRITICAL dimensions as `(D1, D2, D4, D9, D10, D11, D12, D13, D14)` whereas the authoritative scorecard (`corporate-suite-quality-scorecard.md` §3 + §5) lists `(D1, D2, D3, D4, D10, D11, D12, D13, D14)`. The gatekeeper prompt has D9 swapped for D3. **Status: documentation drift; flag for one-line fix during pipeline first end-to-end run.** (D9 Imagery quality is non-critical; D3 Modern professionalism is critical. The scorecard is authoritative.)

The first six are addressed by the X.4a hardening pass; the seventh is a small documentation fix that should land alongside.
