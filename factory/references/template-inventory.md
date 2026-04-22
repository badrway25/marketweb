# Template Inventory · `corporate-suite` archetype

**Audit baseline**: 2026-04-21 · **Refined**: 2026-04-22 (2nd pass · post-standards-drafting reconciliation) · **Branch**: `phase-x4a-corporate-factory-hardening-step0`
**Baseline tip**: `1e82294` (`docs: consolidate X.4 Wave 2 Pilot #1 post-merge state`)
**Source of truth**: repo evidence only. Nothing inferred from memory/summaries without a file pointer.

---

## 0 · Reusability legend

Every entry in this inventory is tagged with one of:

- **REUSABLE-NOW** — a downstream agent (`template-planner`, `template-builder`, `imagery-curator`, `copy-translation-agent`, etc.) may consume it directly on the next pilot without preparatory work. Cite as-is.
- **REUSABLE-AFTER-HARDENING** — usable after the X.4a hardening pass closes the dependency. Specifically: AP1 palette validator (or Builder L\* self-check binding), AP2 responsive breakpoints in `_base.html` + 6 page files, AP3 `business-corporate` Pexels retro-pack, AP12 reduced-motion JS verification.
- **LOCAL-ONLY** — the artifact exists only on a local branch (e.g., Solaria Commit A on `phase-x4-wave2-solaria-coaching-v1`). Not on `main`/integration; not visible to remote tooling.
- **ANTI-PATTERN** — see `anti-pattern-library.md`. Do not propagate; remediate or grandfather explicitly.

The four buckets are orthogonal to the unified severity tags (`[BLOCKING] / [REQUIRED] / [STRONG] / [GUIDELINE]`) used in `factory/standards/*.md`. A `REUSABLE-NOW` artifact may still trip a `[BLOCKING]` rule on a specific pilot — reusability is about availability, severity is about ship-readiness.

---

## 0.1 · Status of the supporting factory artifacts (delta since 2026-04-21)

| Artifact | 2026-04-21 status | 2026-04-22 status |
|---|---|---|
| `factory/standards/corporate-suite-design-standard.md` | empty stub | **POPULATED** · 19 sections · 80+ tagged rules (`CS-TONE-*`, `CS-PAL-*`, `CS-HERO-*`, `CS-NAV-*`, `CS-FOOT-*`, `CS-RHYTHM-*`, `CS-DENSITY-*`, `CS-CTA-*`, `CS-COMP-*`, `CS-EXEC-*`, `CS-MARKET-*`, `CS-RESPONSIVE-*`, `CS-BROWSER-*`) |
| `factory/standards/corporate-suite-imagery-standard.md` | empty stub | **POPULATED** · 19 sections · `CS-IMG-SRC/POOL/COH/PREM/DYN/PRO/CROP/COLOR/HERO/SEC/RHYTHM/AP/STOCK/BLOCK/BROWSER-*` |
| `factory/standards/corporate-suite-browser-rubric.md` | empty stub | **POPULATED** · §5 8-viewport matrix · §6 check roster (`BRWS-*`) · §7 evidence format · §11 verdict template |
| `factory/standards/corporate-suite-blocking-rules.md` | empty stub | **POPULATED** · 18 enumerated blockers `CS-BLOCK-01..18` 1:1 with scorecard overrides `O1..O18` · category-specific recipes |
| `factory/standards/corporate-suite-quality-scorecard.md` | empty stub | **POPULATED** · 15 dimensions D1-D15 · 9 CRITICAL · Layer 1/2/3 verdict logic |
| `factory/standards/corporate-suite-multi-agent-sop.md` | empty stub | **POPULATED** · 10-agent roster · pipeline + handoffs · standard report schema · final user-handshake gate |
| `factory/agents/*.md` (10 prompts) | empty stubs | **POPULATED** · all 10 prompt files written |

**Implication**: this inventory's §4 reusability list is now consumed by named agents per §6 below. A future pilot brief lands at `template-planner`; the template inventory is the planner's first read against `corporate-suite-multi-agent-sop.md` §3.1.

---

## 1 · Skin (shared shell · reused by every template on this archetype)

Location: `templates/live_templates/business/corporate-suite/`

| File | Lines | Role | Reusability |
|---|---:|---|---|
| `_base.html` | 549 | Shared chrome · tokens · nav · footer · RTL · editor-preview guards | **REUSABLE-AFTER-HARDENING** (AP2 responsive breakpoints + AP7 `--primary-2:20` dead-code deletion + AP12 motion JS verification pending) |
| `home.html` | 384 | Hero split + pillars + KPI band + sectors ribbon + leadership + cases + CTA | **REUSABLE-AFTER-HARDENING** (AP2 — 0 `@media` blocks) |
| `about.html` | 202 | Studio history timeline + values + team grid + coordinates | **REUSABLE-AFTER-HARDENING** (AP2 — 0 `@media`) |
| `services.html` | 131 | Services cards + process strip + inline CTA | **REUSABLE-AFTER-HARDENING** (AP2 — 0 `@media`) |
| `case_study_list.html` | 97 | Indexed row list of case studies | **REUSABLE-AFTER-HARDENING** (AP2 — 0 `@media`) |
| `case_study_detail.html` | 166 | Single case post · breadcrumb · kpi strip · team strip · next-case | **REUSABLE-AFTER-HARDENING** (AP2 — 0 `@media`) |
| `contact.html` | 235 | Form + office side column · **only file with 1 real `@media (max-width: 880px)`** | **REUSABLE-NOW** (form/coords stack reference for CS-COMP-05 / BRWS-VIEW-05) |
| **Total** | **1,764** | | |

Preview composition (used by `generate_previews.py` to render tile PNG):
- `templates/preview_compositions/business/corporate-suite.html` · 313 lines · **0 media queries** · **REUSABLE-AFTER-HARDENING** (composition reads pool slots by index — slot order in `CS-IMG-POOL-01` is the contract this file enforces)

---

## 2 · Enrolled templates on this archetype

### 2.1 · Pragma — Corporate Suite · `pragma-corporate-suite` · **LIVE**

| Fact | Value | Evidence | Reusability / notes |
|---|---|---|---|
| Status | `published_live` · featured | `TEMPLATE_REGISTRY.json` | REUSABLE-NOW as a sibling D-054 reference for new pilots |
| Locales | `it · en · fr · es · ar` + RTL | `template_content_pragma*.py` (5 files) | REUSABLE-NOW · 5-locale shape contract for new pilots |
| Session closed | 32 (2026-04-13) · pre-factory era | module docstring | predates the X.3 curation protocol |
| Palette | `primary=#1E293B` navy slate · `secondary=#3B82F6` blue · `accent=#10B981` emerald | `seed_templates.py:493` | Passes `CS-PAL-01` (L\* of `#1E293B` on cream cleanly ≤ 40) — REUSABLE-NOW as the cool/blue/emerald D-054 anchor |
| Typography | Merriweather (serif) + Inter (sans) | `template_dna.py:985` | Passes `CS-TYPE-01` (humanist/transitional serif + neutral sans) — REUSABLE-NOW |
| Imagery pool | `business-corporate` · 6 URLs · **Unsplash** (legacy) | `preview_imagery.py:312-322` | **ANTI-PATTERN AP3 · grandfathered** · single tolerated non-Pexels exception (CS-BLOCK-07 / O7 explicit grandfather) · REUSABLE-AFTER-HARDENING once `business-corporate` retro-pack lands |
| Imagery direction | `executive-boardroom` | `template_dna.py:982` | REUSABLE-NOW as the Pragma slot-by-slot intent reference |
| Voice anchor | "Dove si prendono le decisioni che contano." | `template_content_pragma.py` | REUSABLE-NOW · the F2 / `CS-EXEC-01` exemplar |
| IT content LOC | 867 | `wc -l template_content_pragma.py` | |
| Total content LOC (5 locales) | 4,293 | sum of `template_content_pragma*.py` | |
| D-054 diffed against | Elevate (startup-saas-landing) | module docstring lines 12-32 | **DRIFT vs `CS-EXEC-02` / `CS-BLOCK-12` / `O12`**: with Fiscus + Solaria now siblings, Pragma's docstring triangulates against ONE non-archetype sibling, not all on-archetype siblings. Refresh on next Pragma touch. |

### 2.2 · Fiscus — Studio Tributario · `fiscus-commercialista` · **LIVE** (X.4 Wave 2 Pilot #1)

| Fact | Value | Evidence | Reusability / notes |
|---|---|---|---|
| Status | `published_live` | commit `65c6dd6` · `TEMPLATE_REGISTRY.json` | REUSABLE-NOW · cleanest in-repo full-factory-pipeline reference |
| Locales | `it · en · fr · es · ar` + RTL | `template_content_fiscus*.py` (5 files) | REUSABLE-NOW |
| Session closed | 80 (2026-04-20) · first X.4 wave template | module docstring | first pilot through curated-pack workflow |
| Palette | `primary=#1F2937` charcoal · `secondary=#B58F4A` gold · `accent=#1C3D5A` navy | `seed_templates.py:553` | Passes `CS-PAL-01` — REUSABLE-NOW as the warm-gold D-054 anchor |
| Typography | IBM Plex Serif + IBM Plex Sans | `template_dna.py:1331` | Passes `CS-TYPE-01` — REUSABLE-NOW |
| Imagery pool | `business-fiscal` · 6 URLs · **Pexels** (curated via X.3 C3 protocol) | `preview_imagery.py:337-359` | REUSABLE-NOW · canonical example of `CS-IMG-SRC-01` + `CS-IMG-POOL-01` shape |
| Imagery pack | `docs/content-factory/imagery/packs/financial-services.md` | | REUSABLE-NOW · canonical example of `CS-IMG-COH-06` (per-URL caption + role + coherence statement) |
| Imagery direction | `fiscal-desk-documents` | `template_dna.py:1328` | REUSABLE-NOW |
| Voice anchor | "L'adempimento corretto, non la trovata." | `template_content_fiscus.py` | REUSABLE-NOW · the F2 / `CS-EXEC-01` exemplar across 5 locales |
| IT content LOC | 931 | `wc -l template_content_fiscus.py` | |
| Total content LOC (5 locales) | 4,729 | sum of `template_content_fiscus*.py` | |
| D-054 diffed against | Pragma (module docstring lines 14-40) | | **DRIFT vs `O12`**: Fiscus docstring triangulates against Pragma only; Solaria now exists as a third sibling. Refresh on next Fiscus touch. |
| Cluster blueprint | `docs/content-factory/cluster_blueprints/notary-commercialista.md` + `financial-services.md` | | REUSABLE-NOW |

### 2.3 · Solaria — Business Coaching · `solaria-coaching` · **DRAFT · LOCAL-ONLY · NOT MERGED · NOT PUSHED**

> **Solaria Commit B remains paused per binding user instruction.** Branch `phase-x4-wave2-solaria-coaching-v1` exists only locally. Per `factory/standards/corporate-suite-multi-agent-sop.md` §7.6 and `factory/standards/corporate-suite-blocking-rules.md` §21.4, no agent (planner, copy-translation, builder, browser-verifier, gatekeeper) may un-pause Commit B until the X.4a hardening pass closes — see §7 of this file for the explicit verdict.

| Fact | Value | Evidence | Reusability / notes |
|---|---|---|---|
| Status | `draft` · `live_preview=false` · IT-only | branch `phase-x4-wave2-solaria-coaching-v1` HEAD = `6b70d56` | **LOCAL-ONLY** |
| Locales | `it` only (EN/FR/ES/AR pending) | registry row on branch | EN/FR/ES/AR authoring is the paused work |
| Session opened | 81 (2026-04-21) · second X.4 wave template | module docstring | |
| Palette (pre-fix) | `primary=#F7F3EC` **cream** · inverted skin convention | commit `e8f38b5` · **AP1 · CS-BLOCK-01 · O1** | **ANTI-PATTERN** · the load-bearing incident behind every contrast standard in this factory |
| Palette (post-fix `6b70d56`) | `primary=#2B2A28` warm carbon · `secondary=#C8621A` ocra · `accent=#8B5A2B` caramel | commit `6b70d56` body | Passes `CS-PAL-01` post-fix — the warm-earth D-054 anchor. REUSABLE-NOW as a sibling D-054 reference (palette only); content is local-only |
| Typography | Fraunces + Inter | DNA on branch | Passes `CS-TYPE-01` |
| Imagery pool | `business-coaching` · 6 URLs · Pexels (curated via X.3 C3 protocol) | `preview_imagery.py:370-383` on branch | LOCAL-ONLY |
| Imagery pack | `docs/content-factory/imagery/packs/coaching.md` · 23 URLs curated | | REUSABLE-NOW (the pack itself lives on `main`) |
| Imagery direction | `coaching-1to1` | DNA on branch | LOCAL-ONLY |
| Voice anchor | "Il coaching non è terapia e non è consulenza." | module docstring | LOCAL-ONLY · 1/5 locales |
| IT content LOC | 949 | `wc -l` on branch | LOCAL-ONLY |
| Cluster blueprint | `docs/content-factory/cluster_blueprints/coaching.md` | | REUSABLE-NOW |

---

## 3 · Cross-template facts

- **Archetype wiring**: `apps/editor/schema.py:10021` maps archetype key `corporate-suite` → `PRAGMA_CORPORATE_SUITE_SCHEMA`. Same editor schema serves every template on this archetype. **REUSABLE-NOW** (out-of-scope to edit during X.4a per SOP §7.6).
- **DNA registry**: `apps/catalog/template_dna.py` records per-template DNA keyed by slug — `pragma-corporate-suite` (line 972), `fiscus-commercialista` (1318). Solaria DNA exists only on branch (LOCAL-ONLY).
- **Content module dispatcher**: `apps/catalog/template_content.py` maps slug → locale content module. The Solaria row exists only on branch (LOCAL-ONLY).
- **Preview imagery pool naming convention**: `business-<kind>` — `business-corporate`, `business-fiscal`, `business-coaching`. One pool per template, zero URL overlap (`CS-IMG-SRC-04`). **REUSABLE-NOW**.
- **Tier discipline**: `TEMPLATE_REGISTRY.json` is source of truth for tier · `published_live | draft`. `sync_template_tiers` applies the JSON into the DB. The D-102 2-commit cadence (Commit A draft-landing → Commit B LIVE flip) is now formalized in `corporate-suite-multi-agent-sop.md` §1.3 and `corporate-suite-blocking-rules.md` §2.2. **REUSABLE-NOW**.

---

## 4 · Reusable inheritance summary (what future pilots on this archetype inherit)

Each row tagged with the four-bucket reusability classification.

| # | Inheritance | Tag | Notes |
|:-:|---|---|---|
| 1 | The whole `templates/live_templates/business/corporate-suite/` shell | **REUSABLE-AFTER-HARDENING** | Skin works; AP2 responsive breakpoints + AP7 dead-code deletion (1 line) + AP12 motion JS verification still pending. New pilots inherit the responsive gap today; AP7/AP12 are cosmetic/rendering-neutral. |
| 2 | `PRAGMA_CORPORATE_SUITE_SCHEMA` editor schema (mutable lists for pillars, KPI, sectors, leadership, timeline, team, cases) | **REUSABLE-NOW** | Out-of-scope to modify in X.4a (SOP §7.6); inherits as-is. |
| 3 | The 6-slot imagery pool shape `[hero, feature, portrait, portrait, detail, ambient]` | **REUSABLE-NOW** | `CS-IMG-POOL-01` blocking rule. Curator authors against it. |
| 4 | The 6-page page-kind set: `home · about · services · case_study_list · case_study_detail · contact` | **REUSABLE-NOW** | `corporate-suite-browser-rubric.md` §10.2 walks all six. |
| 5 | RTL block + 5-locale content-file convention (`_it` default + `_en` · `_fr` · `_es` · `_ar`) | **REUSABLE-NOW** | Patterns D1-D5; copy-translation agent contract (SOP §3.3). |
| 6 | D-054 10-gate differentiation template (10 dimensions enumerated in module docstring) | **REUSABLE-AFTER-HARDENING** | `CS-EXEC-02` / `CS-BLOCK-12` / `O12` now require triangulation against EVERY sibling. Pragma + Fiscus docstrings predate the multi-sibling case and triangulate against one sibling each — **systemic drift**, refresh on next touch. New pilots author against all three siblings (planner → `factory/reports/plans/<slug>/d-054-triangulation.md`). |
| 7 | Fiscus as the cleanest reference implementation (post-factory, Pexels-only, full 5 locales, post-merge-validated) | **REUSABLE-NOW** | First read for every planner/curator/copy run on a new pilot. |
| 8 | The `business-corporate` Unsplash pool (Pragma legacy) | **ANTI-PATTERN** (AP3) · grandfathered for Pragma · forbidden on new pilots | `CS-IMG-SRC-01` legacy exception. Do not propagate; do not introduce new Unsplash URLs anywhere. |
| 9 | Solaria pre-fix `primary=#F7F3EC` palette at commit `e8f38b5` | **ANTI-PATTERN** (AP1) · fixed at `6b70d56` | The canonical incident; cite as the reason every contrast/blocking/scorecard standard exists. |
| 10 | Single working `@media (max-width: 880px)` block in `contact.html` | **REUSABLE-NOW** as the breakpoint pattern reference for `_base.html` hardening | The agency archetype's `_base.html:349,359` is the reference for the missing 1100/720 breakpoints. |

---

## 5 · What this inventory does NOT cover

- Editor schema refactor (blocked per SOP §7.6 · no `apps/editor` changes during X.4a).
- Commerce / projects changes (blocked per SOP §7.6).
- Adding new archetypes (blocked).
- Browser live verification artifacts for the three enrolled templates (none on disk yet at `factory/reports/browser-verification/<slug>/`; first walks land in Step N of the hardening pass per browser-rubric §11 template).

---

## 6 · Reuse-mapping to future agents

This section converts §1-§4 into the concrete agent contracts under `factory/agents/*.md` (per `corporate-suite-multi-agent-sop.md` §2-§3). Each row names what an agent reads from this inventory and what it must produce.

| Inventory artifact | Consumed by agent | At what step (SOP §4.1) | What the agent does with it |
|---|---|---|---|
| §1 skin file list + AP2 responsive gap | `template-planner` | Pre-Commit-A · §3.1 | Reads to scope the section plan against the 6-page set; cites AP2 as a known archetype gap so the brief notes that responsive coverage is inherited from the shared skin (not a per-pilot deliverable). |
| §2.1 / §2.2 / §2.3 sibling rows + palette + voice anchor | `template-planner` | Pre-Commit-A · §3.1 | Reads to author `d-054-triangulation.md` against ALL THREE existing siblings (`CS-BLOCK-12` / `O12`). Cites palette hexes verbatim for the gates row. |
| §2 voice anchors (Pragma + Fiscus + Solaria) | `copy-translation-agent` | Pre-Commit-A · §3.3 | Reads as the F2 / `CS-EXEC-01` exemplar; mirrors verbatim-translation discipline; greps own output to confirm the new pilot's anchor never collides with a sibling's. |
| §2.2 Fiscus pack file path + §3 pool naming convention | `imagery-curator` | Pre-Commit-A · §3.2 | Reads `docs/content-factory/imagery/packs/financial-services.md` as the canonical 3-field-record example (`CS-IMG-COH-06`); reuses the `business-<kind>` naming convention; runs cross-cluster dedup grep against this pack (`CS-IMG-SRC-04`). |
| §2.1 AP3 Unsplash grandfather + §4 row 8 | `imagery-curator` (reviewer pass) AND `release-gatekeeper` | Pre-Commit-A · §3.2 + Final gate · §3.10 | Curator: must grep its own pack for non-Pexels URLs and report `0 matches` (`CS-BLOCK-07`). Gatekeeper: scorecard Layer 1 explicitly acknowledges the Pragma grandfather; refuses the grandfather on any other slug. |
| §2 palette rows + §4 row 9 (AP1 incident) | `template-builder` | Build · §3.4 | Builder self-check computes `primary` L\* against cream and refuses to advance the template past `draft` if L\* > 40. Cites Solaria `e8f38b5` → `6b70d56` as the precedent. |
| §3 archetype wiring (`apps/editor/schema.py`, `template_dna.py`, `seed_templates.py`, `TEMPLATE_REGISTRY.json`) | `template-builder` | Build · §3.4 | These four files plus `preview_imagery.py` are the only `apps/*` write surface (SOP §3.4). |
| §1 / §2 page-kind set + skin file paths | `browser-verifier` | Walk · §3.8 | Walks the 6 pages × 5 locales × 8-viewport matrix per `corporate-suite-browser-rubric.md` §5. Records URL+port for every navigation. |
| §4 row 1 (skin reusable AFTER hardening — AP2 responsive gap) | `responsive-auditor` | Walk · §3.7 | Drives the §5 matrix; expects a hard-veto FAIL until the hardening pass adds 1100 + 720 px breakpoints to `_base.html` and the 6 page files. |
| §2 palette rows | `contrast-accessibility-auditor` | Walk · §3.6 | Hard-veto on any `h1..h5` distance < 120 / WCAG < 4.5. The AP1 incident is the reason this agent exists. |
| §1 skin scoped CSS prefix `cs-` + §2 sibling docstrings | `style-critic` | Walk · §3.5 | Reads sibling docstrings to validate the new pilot's tone/density/CTA against archetype norms (CS-TONE-* / CS-RHYTHM-* / CS-DENSITY-*). |
| §2 voice anchors + cluster blueprints | `copy-translation-agent` (live re-read pass) | Walk · §3.3 (downstream) | Greps each rendered locale page for the verbatim anchor (`CS-EXEC-01` / `BRWS-FEEL-05`); reports `5/5 verbatim` or escalates per `O11`. |
| §0.1 standards/agents status delta | `release-gatekeeper` | Final · §3.10 | Cites the unified severity model and the 18 overrides O1-O18 in the final scorecard; never grants a `[BLOCKING]` waiver unilaterally. |

---

## 7 · Systemic issues that must be fixed at archetype level before Solaria Commit B

Each item below is a **systemic** defect — fixing it fixes Pragma, Fiscus, and Solaria simultaneously. These are the items that the X.4a hardening pass must close. The Solaria Commit B un-pause is **explicitly conditional** on items #1-#6 closing; item #7 is a trivial documentation fix that must land by Solaria's first walk so the Gatekeeper operates on the correct CRITICAL floor set.

Numbering is **canonical across the three refined files** (this §7 · `anti-pattern-library.md` Systemic issues surfaced · `corporate-suite-audit-master.md` §4). A `⚠` marks items whose closure is a **hard** precondition for Solaria Commit B.

| # | Systemic issue | Anchor | Why it must precede Solaria Commit B |
|:-:|---|---|---|
| 1 | **⚠ AP1 · Palette polarity unenforced skin invariant** — `CS-PAL-01` is enforced today only by the Builder L\* self-check + the live browser walk. A pre-commit palette validator would be the automated belt-and-braces complement. | AP1 / CS-PAL-01 / O1 / D12 | Solaria's pre-fix palette (`#F7F3EC` at `e8f38b5`) is the originating incident. Re-introducing the same defect on the EN/FR/ES/AR locales is structurally impossible only if the validator (or the Builder self-check binding + browser walk) is in place. |
| 2 | **⚠ AP8 · Multi-agent pipeline first end-to-end run** — every standard in `factory/standards/*.md` is now populated and every agent prompt is populated, but no template has yet been walked end-to-end through the 10-agent pipeline (`SOP §4.1`). The first run will surface coordination defects (gate signals, evidence-directory naming, scorecard binding). | AP8 / SOP §4.1 / §10.2 / CS-BROWSER-01..03 / O18 | Solaria un-pause should not be the pipeline's first end-to-end exercise. A re-walk of Fiscus through the populated agents is the safer first run; that walk's `verdict.md` + scorecard validates the pipeline before Solaria's 4 missing locales add 4× the surface area. |
| 3 | **⚠ AP2 · Responsive coverage archetype-level gap** — `_base.html` + 6 page files carry **0 real `@media` blocks** today (only `contact.html` has one at 880px). `CS-RESPONSIVE-01` requires breakpoints at 1100 and 720 px; the pattern reference is `agency-creative-studio/_base.html:349,359`. | AP2 / CS-RESPONSIVE-01..08 / O2 / O3 / D13 | Adding EN/FR/ES/AR locales without responsive coverage means each of the 4 new locales × 6 pages × 8 viewports walks will FAIL the rubric per `BRWS-VIEW-02`. The hardening fix lands once and unlocks Solaria + retroactively hardens Pragma + Fiscus. |
| 4 | **AP3 · `business-corporate` Pexels retro-pack** — Pragma's 6 Unsplash URLs are grandfathered (`CS-IMG-SRC-01` legacy exception). Until the retro-pack lands, the archetype carries one tolerated non-Pexels exception. | AP3 / CS-IMG-SRC-01 / CS-BLOCK-07 / O7 / D11 | Not a hard precondition for Solaria specifically (Solaria uses `business-coaching` Pexels), but the SOP §10.3 framing — "every pilot lands on rails that already caught a Solaria-class defect" — depends on Pragma not being a perpetual exception. Soft precondition for Solaria; hard precondition for the archetype's next pilot. |
| 5 | **⚠ AP10 · D-054 10-gate triangulation drift** — Pragma triangulates against Elevate (different archetype); Fiscus triangulates against Pragma only; Solaria's docstring (on branch) triangulates against Pragma + Fiscus. | AP10 / `CS-EXEC-02` / `CS-BLOCK-12` / `O12` | This is a **content-side** systemic issue, not a skin issue. New pilots (planner-driven) must triangulate against ALL three siblings; Solaria when un-paused must include Pragma + Fiscus rows; Pragma + Fiscus docstrings should be refreshed on next touch. |
| 6 | **AP7 + AP12 cleanups · bundled** — AP7: `_base.html:20` `--primary-2: #2c3e6b` literal navy hex; grep audit 2026-04-22: `var(--primary-2)` = **0 hits** across `templates/`, `static/`, `apps/` → dead-code declaration, 1-line deletion. AP12: `[data-lm]` reveal animations driven by `static/js/live-motion.js`; grep audit 2026-04-22: **45 hooks across 6 files** (every page except `contact.html`); fix is JS-side. | AP7 / CS-PAL-03 / D3 · AP12 / CS-RESPONSIVE-07 / BRWS-FEEL-08 / E2 | AP7 is bundled into the AP2 hardening diff at zero marginal cost (0 consumers → 0 rendered impact). AP12 is the only remaining WCAG 2.3.3 exposure on the archetype — Solaria's coaching audience includes motion-sensitive visitors, so the archetype's WCAG claim must hold before the 4 missing locales ship. The original "Solaria inherits navy bias on every page edge" framing for AP7 is invalidated by the 0-usage enumeration. |
| 7 | **Release-gatekeeper agent prompt CRITICAL-dimension list inconsistency** — `factory/agents/release-gatekeeper.md` §1 lists CRITICAL dimensions as `(D1, D2, D4, D9, D10, D11, D12, D13, D14)` whereas the authoritative scorecard (`corporate-suite-quality-scorecard.md` §3 + §5 + §6) lists `(D1, D2, D3, D4, D10, D11, D12, D13, D14)`. The gatekeeper prompt has D9 (Imagery quality, NON-CRITICAL) swapped for D3 (Modern professionalism, CRITICAL). The scorecard is authoritative. | Gatekeeper §1 vs Scorecard §3/§5/§6 | One-line documentation fix. Must land before the pipeline's first end-to-end run (item #2) so the Gatekeeper applies the correct Layer 2 floor when it aggregates the observer sub-scorecards. |

**Sequencing verdict** (binding): X.4a hardening MUST precede Solaria Commit B. See `corporate-suite-audit-master.md` §7 for the full verdict statement and the dependency graph.

---
