# Corporate-suite Factory Hardening · Step 0 · Master Audit

**Phase**: X.4a · **Audit baseline**: 2026-04-21 · **Refined**: 2026-04-22 · **Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Baseline tip**: `1e82294` (`docs: consolidate X.4 Wave 2 Pilot #1 post-merge state`)
**Scope constraint**: zero `apps/editor`, `apps/projects`, `apps/commerce` changes · zero new archetypes · factory files only.

---

## TL;DR

The `corporate-suite` archetype ships 3 templates: Pragma (LIVE since Session 32, pre-factory), Fiscus (LIVE since Session 80, X.4 Wave 2 Pilot #1, first full-factory-pipeline pilot), and Solaria (IT-only draft on branch `phase-x4-wave2-solaria-coaching-v1`, hit a **skin-convention bug** caught only by live browser verification).

The archetype is **content-scalable** (new template = 5 content files + 1 imagery pack + 1 DNA row + 1 palette row + 1 registry row) but has **two structural gaps** that a hardening pass must address:

1. **Unenforced skin invariant**: `--primary` is the foreground text color. Every new palette must pass a darkness check, or the template ships with invisible body text (Solaria `e8f38b5` → `6b70d56`).
2. **Near-zero responsive coverage**: 0 real viewport breakpoints in the shared skin, 1 breakpoint in `contact.html`. Sibling archetypes (agency-creative-studio) have breakpoints at 1100 and 720 px.

Both gaps slipped past `506/506` test suite runs. CLI green is a lower bound, not a ship signal.

**Sequencing verdict (binding · §7 below)**: X.4a hardening MUST precede Solaria Commit B. The standards/agents are now populated; the code-side hardening (responsive breakpoints + Pragma retro-pack + AP7/AP12 cleanup) and the first end-to-end pipeline run still need to land.

---

## 1 · Factory knowledge artifacts produced this step

| Path | Purpose | Status as of 2026-04-22 |
|---|---|---|
| `factory/references/template-inventory.md` | Skin layout + 3 enrolled templates + what's reusable + agent-mapping + systemic-issues | **REFINED 2026-04-22** · adds reusability-bucket tags, agent-mapping §6, systemic-issues §7 |
| `factory/references/pattern-library.md` | 8 pattern groups (A-H) · golden/acceptable patterns with evidence | **REFINED 2026-04-22** · adds standards-anchor + agent mapping per pattern, reusability tags, appendix cross-reference |
| `factory/references/anti-pattern-library.md` | 12 anti-patterns (AP1-AP12) with severity, detection, prevention | **REFINED 2026-04-22** · maps each AP to the standards rule (`CS-BLOCK-*` / `O<n>` / `D<n>`) and to the SOP detector/fixer agent; adds Status-as-of field + escalates AP11 to BLOCKING |
| `factory/reports/audits/corporate-suite-audit-master.md` | This file · master report | **REFINED 2026-04-22** · adds explicit X.4a-precedes-Solaria verdict + systemic-vs-per-pilot split + flag for the agent-prompt inconsistency |
| `factory/standards/corporate-suite-design-standard.md` | 19 sections · 80+ tagged rules (CS-TONE/PAL/HERO/NAV/FOOT/RHYTHM/DENSITY/CTA/COMP/EXEC/MARKET/RESPONSIVE/BROWSER) | **POPULATED** since 2026-04-21 |
| `factory/standards/corporate-suite-imagery-standard.md` | 19 sections · CS-IMG-* taxonomy | **POPULATED** since 2026-04-21 |
| `factory/standards/corporate-suite-browser-rubric.md` | §5 8-viewport matrix · §6 BRWS-* check roster · §7 evidence dir format · §11 verdict template | **POPULATED** since 2026-04-21 |
| `factory/standards/corporate-suite-blocking-rules.md` | 18 enumerated blockers `CS-BLOCK-01..18` · 1:1 with scorecard overrides O1..O18 · category recipes · merge-vs-LIVE matrix | **POPULATED** since 2026-04-22 |
| `factory/standards/corporate-suite-quality-scorecard.md` | 15 dimensions D1-D15 · 9 CRITICAL · Layer 1/2/3 verdict logic · §7 fillable template | **POPULATED** since 2026-04-22 |
| `factory/standards/corporate-suite-multi-agent-sop.md` | 10-agent roster · pipeline + handoffs · §6 standard report schema · §5.4 final user-handshake gate | **POPULATED** since 2026-04-22 |
| `factory/agents/*.md` (10 prompts) | Per-agent prompts: planner · curator · copy-translation · builder · style-critic · contrast · responsive · browser-verifier · editor-fixer · gatekeeper | **POPULATED** since 2026-04-22 |

The original audit (2026-04-21) marked the standards + agents as "out of scope Step 0 · empty stubs". They are no longer empty; this refinement updates the rest of the artifacts to consume them.

---

## 2 · Repo evidence · what was actually inspected

(Unchanged from 2026-04-21 audit · listed for traceability.)

### Skin (shared across every template)
- `templates/live_templates/business/corporate-suite/_base.html` · 549 lines · read
- `templates/live_templates/business/corporate-suite/home.html` · 384 lines · read
- `templates/live_templates/business/corporate-suite/about.html` · 202 lines · skimmed
- `templates/live_templates/business/corporate-suite/{services,case_study_list,case_study_detail,contact}.html` · grepped for `@media`, `grid-template-columns`, `color: var(--on-dark`
- `templates/preview_compositions/business/corporate-suite.html` · 313 lines · grepped

### Content
- `apps/catalog/template_content_pragma.py` · 867 LOC · read header
- `apps/catalog/template_content_fiscus.py` · 931 LOC · read ~250 lines
- `apps/catalog/template_content_solaria.py` · 949 LOC · read via `git show phase-x4-wave2-solaria-coaching-v1:...`
- Locale trees: 4× Pragma + 4× Fiscus · line counts via `wc -l`

### DNA · palette · imagery wiring
- `apps/catalog/template_dna.py` lines 972 (Pragma) + 1318 (Fiscus) · read
- `apps/catalog/management/commands/seed_templates.py` lines 473-558 · read
- `apps/catalog/preview_imagery.py` lines 312-383 · read
- `apps/editor/schema.py` lines 108-130 + 9838 + 10021 + 10630 · grepped

### Solaria bug trail
- Commit `e8f38b5` (Commit A draft · 1148 lines inserted)
- Commit `6b70d56` (palette polarity fix · 2 files, 11 insertions) — commit body is load-bearing documentation of the skin invariant
- `git diff e8f38b5 6b70d56 -- apps/catalog/management/commands/seed_templates.py` · read

### Content factory protocol
- `docs/content-factory/imagery/CURATION_PROTOCOL.md` · §1-3 read
- `docs/content-factory/imagery/blacklist.md` · §1-4 read
- `docs/content-factory/cluster_blueprints/coaching.md` · §1-5 read (Solaria blueprint)
- `docs/content-factory/imagery/packs/coaching.md` · first 60 lines read (23-URL Solaria pack)

### Standards + agents (added 2026-04-22)
- `factory/standards/corporate-suite-design-standard.md` · 666 lines · read in full
- `factory/standards/corporate-suite-blocking-rules.md` · 1206 lines · read in full
- `factory/standards/corporate-suite-imagery-standard.md` · 919 lines · read in full
- `factory/standards/corporate-suite-browser-rubric.md` · 848 lines · read in full
- `factory/standards/corporate-suite-multi-agent-sop.md` · 668 lines · read in full
- `factory/standards/corporate-suite-quality-scorecard.md` · 585 lines · read in full
- `factory/agents/template-planner.md` · 215 lines · read in full
- `factory/agents/imagery-curator.md` · skimmed top section (mission + outputs)
- `factory/agents/copy-translation-agent.md` · skimmed top section
- `factory/agents/template-builder.md` · skimmed top section
- `factory/agents/style-critic.md` · skimmed top section
- `factory/agents/contrast-accessibility-auditor.md` · skimmed top section
- `factory/agents/responsive-auditor.md` · skimmed top section
- `factory/agents/browser-verifier.md` · skimmed top section
- `factory/agents/template-editor-fixer.md` · skimmed top section
- `factory/agents/release-gatekeeper.md` · 254 lines · read in full

---

## 3 · Classification summary (refined against the populated standards)

### Golden / acceptable patterns (29 total · see `factory/references/pattern-library.md`)

Now mapped 1:1 to standards rules in the pattern-library appendix. Highlights:

- **B2 · Dark-foreground convention** → `CS-PAL-01` / `CS-BLOCK-01` / `O1` / `D12` [CRITICAL]. Load-bearing; defended by Builder L\* self-check + Contrast Auditor hard veto.
- **A4 · 6-slot imagery pool shape** → `CS-IMG-POOL-01` `[BLOCKING]`.
- **D1-D5 · RTL** → `CS-TYPE-06` (font swap) / `CS-NAV-06` + `CS-FOOT-03` (Latin wordmark + numerics) / `CS-RESPONSIVE-08` (RTL viewport tested) / `CS-TYPE-05` (letter-spacing flatten) / `CS-NAV-03` (locale switcher attrs).
- **E1 · Gold focus ring** → `CS-NAV-02` `[BLOCKING]`. **E2 · Reduced-motion** → `BRWS-FEEL-08` `[STRONG]` (REUSABLE-AFTER-HARDENING per AP12).
- **F1-F4 · Voice anchoring** → `CS-EXEC-01..04`. F2 + F4 are `[BLOCKING]` (`O11` / `O10`).
- **G1-G3 · Imagery** → `CS-IMG-SRC-01` (Pexels-only · `O7`) / `CS-IMG-SRC-04` (one URL = one cluster) / `CS-IMG-PREM-02` (resolution floor).

### Anti-patterns (12 total · see `factory/references/anti-pattern-library.md`)

Refined severity + status against the unified `[BLOCKING] / [REQUIRED] / [STRONG] / [GUIDELINE]` model:

`[BLOCKING]` · LATENT-ARCHETYPE-WIDE (must close before Solaria Commit B):
- **AP1** · Palette polarity inversion → `CS-BLOCK-01` / `O1` · ⚠ systemic, defenders in place, validator pending
- **AP2** · Zero viewport breakpoints → `CS-BLOCK-02` / `CS-BLOCK-03` / `O2` / `O3` · ⚠ systemic, hardening fix pending

`[BLOCKING]` · GRANDFATHERED:
- **AP3** · Pragma still on Unsplash → `CS-BLOCK-07` / `O7` · single tolerated exception · retro-pack pending

`[BLOCKING]` · RECURRENT-RISK on every new pilot:
- **AP4** · Category-mismatched imagery → `CS-BLOCK-05` / `O5` (3-second check fails)
- **AP5** · Generic stock fallback → `CS-BLOCK-IQ-02`
- **AP6** · Cross-cluster URL reuse → `CS-BLOCK-I-02`
- **AP8** · Tests pass ≠ ship-ready (cultural) → `CS-BLOCK-18` / `O18`
- **AP9** · Coaching cluster clichés → `CS-BLOCK-P-05` + `CS-BLOCK-10` / `O10` + `CS-IMG-AP-06`
- **AP11** · Dark-section default text color partial → `CS-BLOCK-17` / `O17` · **escalated from `[S2]` to `[BLOCKING]`** in the unified model

`[STRONG]` · LATENT-ARCHETYPE-WIDE:
- **AP7** · Hardcoded `--primary-2: #2c3e6b` → `CS-PAL-03` `[REQUIRED]` · `[STRONG]` archetype-debt
- **AP10** · Palette differentiation drift across siblings → `CS-PAL-02` / `CS-EXEC-02` / `O12` · current palettes pass; D-054 docstring drift on Pragma + Fiscus
- **AP12** · Reduced-motion JS path unverified → `CS-REQ-06` / `BRWS-FEEL-08`

### Before / After edits (repo-confirmed)
| Commit | File | Before | After | Caught by |
|---|---|---|---|---|
| `6b70d56` | `seed_templates.py:623-633` | `primary=#F7F3EC` (cream) | `primary=#2B2A28` (dark carbon) + 8-line comment | Live browser DOM inspection — the AP1 / AP8 incident that motivates the entire factory |
| `65c6dd6` | `TEMPLATE_REGISTRY.json` · `tests.py` · `preview` | Fiscus `draft`, no preview PNG | Fiscus `published_live`, preview regen via Playwright | Manual walk + regen script — the first full-factory pilot end-to-end |

### Responsive fixes — pending
None landed on this archetype yet. Agency-creative-studio (`_base.html:349,359`) is the reference implementation for what to copy. **AP2 systemic fix; pending hardening pass.**

### Contrast fixes — pending (validator only)
Solaria palette fix is the only one landed. The Builder L\* self-check (SOP §3.4) is the per-pilot defender; the `contrast-accessibility-auditor` agent (SOP §3.6) is the live-walk defender. A pre-commit palette validator is pending.

### Imagery fixes — pending
- Pragma needs a Pexels repack to match the factory protocol (AP3). Single tolerated exception.
- No semantic review of Pragma's 6 existing Unsplash URLs has been captured in the factory knowledge base.

---

## 4 · Systemic issues surfaced (must be fixed at archetype level before Solaria Commit B)

Each item below is **systemic** — fixing it fixes Pragma, Fiscus, and Solaria simultaneously. Numbered to align with `template-inventory.md` §7.

1. ⚠ **Unenforced skin invariant — palette polarity (AP1 / CS-PAL-01)**
   - The "primary is dark" rule lives at `seed_templates.py:623-633` and in the standards. Today's enforcement = Builder L\* self-check + Contrast Auditor hard veto + browser walk. Pre-commit palette validator is the still-pending complement.
   - **Fix direction**: lint / validator that refuses tier advance to `published_live` when `primary` lightness L\* > 40 on cream paper. Until then, the SOP enforcement holds.

2. ⚠ **Browser verification central, not optional (AP8 / CS-BROWSER-01..03)**
   - The repo has 506 apps tests + 131 catalog tests + 834 smoke rows. None catches AP1 / AP2 / AP4. Fixed by `browser-verifier` agent + Playwright MCP walk + binding rubric.
   - **Fix direction**: encoded; first end-to-end pipeline run still pending. Solaria un-pause must NOT be the pipeline's first run — re-walk Fiscus through the populated agents first to surface coordination defects (gate signals, evidence-directory naming, scorecard binding).

3. ⚠ **Responsive coverage is an archetype-level gap (AP2)**
   - 0 real `@media` blocks in `_base.html` + 6 page files. `contact.html` is the only file with a 880px breakpoint.
   - **Fix direction**: a single diff to `_base.html` adding `@media (max-width: 1100px)` and `@media (max-width: 720px)`, modeled on `agency-creative-studio/_base.html:349,359`. Plus the per-page collapse rules (hero stacks, nav hamburger, footer stacks). Smallest blast radius that fixes Pragma + Fiscus + Solaria simultaneously.

4. **Pragma predates the content factory protocol (AP3)**
   - Imagery is legacy-Unsplash with no pack, no caption log, no dedup grep. Single tolerated exception under `CS-IMG-SRC-01`.
   - **Fix direction**: retro-curate a `business-corporate` Pexels pack via `imagery-curator` (primary + reviewer pass), then `template-editor-fixer` swaps the 6 URLs in `preview_imagery.py:312-322`. Not a hard precondition for Solaria; close before next pilot lands.

5. ⚠ **D-054 is a 3-way triangle now (AP10 docstring drift)**
   - Pragma triangulates against Elevate (different archetype). Fiscus triangulates against Pragma only. Solaria's docstring triangulates against Pragma + Fiscus.
   - **Fix direction**: new pilots author against ALL three siblings via `template-planner`'s `d-054-triangulation.md`. Pragma + Fiscus docstrings refresh on next touch. The sibling-refresh is small (~10 lines per docstring) and can run as a `template-editor-fixer` follow-up.

6. **AP7 `--primary-2: #2c3e6b` hardcode + AP12 reduced-motion JS**
   - Both LATENT-ARCHETYPE-WIDE; both fix in the shared skin / global JS, outside per-pilot SOP scope (§7.6). Bundled with the AP2 hardening pass.

7. **Documentation drift in `factory/agents/release-gatekeeper.md` §1**
   - The gatekeeper prompt lists CRITICAL dimensions as `(D1, D2, D4, D9, D10, D11, D12, D13, D14)` whereas the authoritative scorecard (`corporate-suite-quality-scorecard.md` §3 + §5) lists `(D1, D2, D3, D4, D10, D11, D12, D13, D14)`. The gatekeeper prompt has D9 (Imagery quality, NON-CRITICAL) swapped for D3 (Modern professionalism, CRITICAL).
   - **Fix direction**: one-line fix to the gatekeeper prompt during the pipeline first end-to-end run. The scorecard is authoritative.

---

## 5 · Evidence confidence

| Finding | Repo-confirmed | Inferred |
|---|:-:|:-:|
| File counts, line counts, file paths | ✅ | |
| Palette hex values across 3 templates | ✅ | |
| Imagery pool URLs per template | ✅ | |
| Solaria palette bug root cause | ✅ (commit body) | |
| Zero responsive breakpoints in skin + 6/7 pages | ✅ (grep) | |
| Contact.html is the only file with a breakpoint | ✅ (grep) | |
| Agency archetype has 2 breakpoints | ✅ (grep) | |
| D-054 10-gate documented in docstrings | ✅ | |
| Browser walk caught Solaria invisible text | ✅ (commit body) | |
| Standards files populated 2026-04-21 → 2026-04-22 | ✅ (file mtimes + content) | |
| All 10 agent prompts populated 2026-04-22 | ✅ (file mtimes + content) | |
| Release-gatekeeper D3 ↔ D9 inconsistency | ✅ (text comparison · gatekeeper §1 vs scorecard §3 + §5) | |
| JS reduced-motion coverage for `[data-lm]` | | Inferred (not opened `live-motion.js`) |
| `--primary-2: #2c3e6b` footprint impact | Partial (value confirmed at line 20, usages not enumerated) | Inferred scope |
| Specific viewport widths where skin breaks | | Inferred from fixed 72px padding + 1400 max-width (not browser-verified yet) |

---

## 6 · What is still missing (for future hardening steps)

1. **Browser verification baseline** — no recorded Playwright MCP walk on Pragma, Fiscus, or Solaria. Pre-hardening pass should record screenshots at 1920/1440/1280/1024/768/640/414/390 viewports for each live template × 5 locales per `corporate-suite-browser-rubric.md` §5/§7.
2. **Contrast ratio per palette** — no WCAG AA/AAA report for any of the 3 palettes across the skin's surface classes.
3. **`business-corporate` Pexels repack** — Pragma's 6 Unsplash URLs have no curator pack.
4. **Responsive breakpoint code** — target viewports defined in standards (CS-RESPONSIVE-01..08); the actual `@media` blocks not yet in `_base.html` + 6 page files.
5. **Palette validator** — a pre-commit check that fails when `primary` L\* > 40 on cream, or when the secondary+accent pair fails the D-054 differentiation test. Builder L\* self-check is the closest existing layer.
6. **Pipeline first end-to-end run** — Fiscus re-walk through the 10-agent SOP would surface coordination defects (gate signals, evidence-dir naming, scorecard binding) before Solaria's 4 missing locales add 4× the surface area.
7. **Solaria locale authoring gate** — wait until items 1-6 close before un-pausing Commit B authoring (per binding user instruction · per `corporate-suite-blocking-rules.md` §21.4 · per `corporate-suite-multi-agent-sop.md` §7.6 · per `corporate-suite-design-standard.md` §19.8 · per `corporate-suite-browser-rubric.md` §12 · per `corporate-suite-quality-scorecard.md` §9).
8. **Local dev server live URL/port** — `corporate-suite-browser-rubric.md` §4 requires reporting URL/port during verification. Not started this audit step (audit-only).
9. **Release-gatekeeper agent prompt fix** — D3 ↔ D9 swap noted in §4 issue #7.

---

## 7 · Sequencing verdict — does X.4a precede Solaria Commit B?

**Yes. Binding. Cross-referenced in 5 standards documents.**

The X.4a hardening pass MUST close (at minimum) the systemic items below BEFORE the user un-pauses Solaria Commit B (the EN/FR/ES/AR locale authoring on `phase-x4-wave2-solaria-coaching-v1`):

| Precondition | Source | Why it's a precondition |
|---|---|---|
| AP1 enforcement layered (Builder L\* self-check binding ✓ + Contrast Auditor hard-veto agent ✓) plus pre-commit palette validator (PENDING) | `corporate-suite-design-standard.md` §19.7-19.8 · `corporate-suite-blocking-rules.md` §21.4 | Solaria's `e8f38b5` proves this is the dominant failure shape. Re-introducing it on the EN/FR/ES/AR locales is structurally impossible only if the validator + walk are both in place. |
| AP2 responsive coverage (1100 + 720 px breakpoints + per-page collapse rules) (PENDING) | `corporate-suite-design-standard.md` §19.7-19.8 · `corporate-suite-blocking-rules.md` §3 (CS-BLOCK-02/03 — the ✱ merge-block items) | Without breakpoints, EN/FR/ES/AR × 6 pages × 8 viewports = 240 walk cells per locale all expected to FAIL O2. The walk would FAIL Solaria not for content reasons but for inherited-skin reasons. |
| AP3 `business-corporate` Pexels retro-pack (PENDING · soft precondition) | `corporate-suite-design-standard.md` §19.8 · `corporate-suite-blocking-rules.md` §21.4 | Not strictly a Solaria precondition (Solaria uses `business-coaching` Pexels). Listed because the SOP §10.3 framing — "every pilot lands on rails that already caught a Solaria-class defect" — depends on Pragma not being a perpetual exception. |
| AP7 `--primary-2` decoupling (PENDING · soft) | `corporate-suite-design-standard.md` §19.7 · AP7 entry | Solaria warm-earth identity inherits a navy bias on every page edge until decoupled. Fix lands once. |
| AP12 reduced-motion JS audit (PENDING · soft) | `corporate-suite-design-standard.md` §19.7 · AP12 entry | Solaria's coaching audience includes motion-sensitive visitors; WCAG 2.3.3 claim must hold. |
| Multi-agent pipeline first end-to-end run (RECOMMENDED) | `template-inventory.md` §7 issue #7 | Solaria un-pause should not be the pipeline's first exercise. Re-walk Fiscus first to surface coordination defects without 4× surface-area. |
| `release-gatekeeper.md` D3 ↔ D9 fix (PENDING · trivial) | §4 issue #7 above | One-line documentation fix. Bundle with the pipeline first run. |
| User explicit un-pause | `corporate-suite-multi-agent-sop.md` §7.6 + §3.10 escalation rules | Even after all of the above closes, Solaria Commit B requires explicit user instruction. No agent (planner, copy-translation, builder, gatekeeper) has authority to un-pause. |

**Quotes from the standards (verbatim)**:

- `corporate-suite-design-standard.md` §19.8 (Summary):
  > "**Solaria Commit B** — explicitly paused per user instruction; un-pause only after (1)–(7) above are sufficient to guarantee the next pilot inherits a sturdier skin than Solaria did."

- `corporate-suite-blocking-rules.md` §21.4 (Bottom line):
  > "Solaria Commit B explicit note: per user instruction, Solaria Commit B (EN / FR / ES / AR authoring for the `solaria-coaching` template, currently paused on branch `phase-x4-wave2-solaria-coaching-v1` after `e8f38b5` / `6b70d56`) is NOT un-paused by this document. It remains paused until the archetype hardening pass closes — specifically until the 1100 + 720 responsive breakpoints land, the palette validator (or the equivalent discipline) is in place, and Pragma's retro-pack is scheduled."

- `corporate-suite-imagery-standard.md` §1 + §19:
  > "Pragma's legacy Unsplash pack (AP3) is a known gap and is scheduled for retro-curation; it is the **only** tolerated exception until the `business-corporate` Pexels pack lands."

- `corporate-suite-browser-rubric.md` §12:
  > "It does not unpause Solaria Commit B. Solaria remains on branch `phase-x4-wave2-solaria-coaching-v1` at `6b70d56` with IT-only content. The EN/FR/ES/AR authoring remains paused until the hardening pass closes per the binding user instruction."

- `corporate-suite-multi-agent-sop.md` §7.6 + §9:
  > "No continuation of Solaria Commit B — Solaria's EN/FR/ES/AR authoring remains paused on branch `phase-x4-wave2-solaria-coaching-v1` at `6b70d56`. The Copy/Translation Agent MUST refuse a task that targets Solaria's non-IT locales until the user explicitly un-pauses. This SOP does not grant that un-pause."

- `corporate-suite-quality-scorecard.md` §9:
  > "Does not unpause Solaria Commit B. Per binding user instruction, Solaria's EN/FR/ES/AR authoring remains paused until the hardening pass closes. When it resumes, Solaria will be the first template to pass through this scorecard end-to-end."

**The verdict is unanimous across the standards family.** X.4a precedes Solaria Commit B — both as a code precondition (responsive + palette enforcement) and as a process precondition (pipeline first end-to-end run on Fiscus before Solaria's 4× surface area).

---

## 8 · Next-step recommendations (suggested order)

These are recommendations, not commitments. The user drives the order.

1. **Fix the `release-gatekeeper.md` D3 ↔ D9 inconsistency** — one-line documentation edit. Bundle with #2.
2. **Re-walk Fiscus through the 10-agent pipeline end-to-end** — surfaces gate-signal coordination defects at low surface-area cost. Produces the first concrete evidence directory under `factory/reports/browser-verification/fiscus-commercialista/<run-timestamp>/` and the first scorecard under `factory/reports/quality-scorecards/fiscus-commercialista/<run-timestamp>-scorecard.md`. Confirms `corporate-suite-multi-agent-sop.md` §4 handoffs work as written.
3. **Land the AP2 hardening patch on `_base.html` + 6 page files** — one diff modeled on `agency-creative-studio/_base.html:349,359`. Adds `@media (max-width: 1100px)` and `@media (max-width: 720px)` plus per-page collapse rules. Re-walk Pragma + Fiscus to confirm both tighten cleanly at the new breakpoints.
4. **Land the AP7 + AP12 cleanups** — derive or drop `--primary-2`; verify `[data-lm]` reduced-motion JS path. Re-walk Pragma + Fiscus once more.
5. **Retro-curate `business-corporate` Pexels pack** — `imagery-curator` (primary + reviewer pass) produces the pack; `template-editor-fixer` swaps the 6 URLs in `preview_imagery.py:312-322`. Re-walk Pragma. AP3 closes; the single grandfathered exception ends.
6. **Optional · pre-commit palette validator** — codifies CS-PAL-01 as a CI gate. Builder self-check is the per-pilot enforcement; the validator is the pre-commit complement.
7. **Refresh Pragma + Fiscus D-054 docstrings** — small `template-editor-fixer` follow-up to triangulate against ALL three siblings. `template-inventory.md` §7 issue #6.
8. **Only then: user un-pauses Solaria Commit B** — Solaria becomes the first new-content pilot through the hardened pipeline. EN/FR/ES/AR authoring proceeds via `copy-translation-agent` against the brief; new browser walk records 5/5 locale × 6 pages × 8 viewports under `factory/reports/browser-verification/solaria-coaching/<run-timestamp>/`.

---

## 9 · Summary

**What was found**:
- Skin is well-architected at the CSS-token and RTL level (29 golden patterns) but has two structural gaps: `--primary` dark-foreground convention is unenforced (AP1), and viewport responsiveness is essentially absent (AP2).
- Content factory pipeline (cluster blueprint → curated Pexels pack → 10-gate D-054 → 5-locale tree) works cleanly for Fiscus. Pragma predates it. Solaria validated that the pipeline catches content issues — but also that it doesn't catch skin invariants.
- Solaria draft exposed a latent bug in 30 minutes of browser walk that 506/506 tests missed. This is the strongest evidence that **browser verification must be central, not optional**, matching the mandatory rule.
- Since 2026-04-21, all 6 standards and all 10 agent prompts are populated. The 4 reference/audit artifacts (this file + template-inventory + pattern-library + anti-pattern-library) are now refined to consume them — reusability tags, agent mappings, severity reclassification (AP11 escalated to BLOCKING), systemic-vs-per-pilot split, sequencing verdict.

**What is reusable for future agents** (4-bucket classification per file):
- 29 named patterns with standards anchors and per-agent consumption (`pattern-library.md`).
- 12 named anti-patterns with detector / fixer agent mapping (`anti-pattern-library.md`).
- A complete template inventory keyed by slug with reusability tags + agent-mapping table (`template-inventory.md`).
- A clear split between "repo-confirmed" and "inferred" evidence (this file).

**What is still missing**:
- Code-side hardening: AP2 responsive breakpoints; AP7 `--primary-2` decoupling; AP12 reduced-motion JS verification; AP3 Pragma Pexels retro-pack; optional pre-commit palette validator.
- Process-side: pipeline first end-to-end run (recommend Fiscus); Pragma + Fiscus D-054 docstring refresh; release-gatekeeper.md D3 ↔ D9 fix.
- Solaria Commit B remains explicitly paused per the unanimous binding user instruction across 5 standards documents (§7 verdict above).

**Sequencing verdict (binding)**: X.4a hardening MUST precede Solaria Commit B.
