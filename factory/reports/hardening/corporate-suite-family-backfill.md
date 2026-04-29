# Corporate-suite family backfill — operational pass

**Status**: backfill v1 · **Date**: 2026-04-29 · **Branch**: `phase-x4b-corporate-suite-family-backfill`
**Scope**: corporate-suite archetype only. No application code in this pass.
**Purpose**: turn the layout-divergence diagnosis into an operational record of *who is what* and *what must hold still*, so the next pass can rebuild Continua at LF-5 without ambiguity.

**Inputs read**:
- `factory/reports/hardening/corporate-suite-layout-divergence-plan.md`
- `factory/reports/hardening/corporate-suite-layout-variance-rules.md`
- `factory/reports/hardening/corporate-suite-layout-family-matrix.md`
- `design-orchestrator/references/internal-baselines/corporate-suite-distinctness-matrix.md`
- `design-orchestrator/references/internal-baselines/corporate-suite-reference-pack.md`
- `factory/standards/corporate-suite-design-standard.md`
- `factory/standards/corporate-suite-blocking-rules.md`
- `factory/standards/corporate-suite-browser-rubric.md`
- live siblings: Pragma · Fiscus · Solaria · Continua
- shared chrome: `templates/live_templates/business/corporate-suite/{home,_base}.html`
- Continua content: `apps/catalog/template_content_continua.py`

**Output**:
- this report
- `design-orchestrator/references/internal-baselines/corporate-suite-layout-family-assignment.md`
- `design-orchestrator/references/internal-baselines/continua-lf5-migration-brief.md`

This pass is paperwork-only. No template, view, model, or registry changes. The next pass (Continua LF-5 rebuild, Step 3 of the divergence plan) is the first one that touches code.

---

## 1 · Final family assignment for each current sibling

Backfilled against the LF-1..LF-5 definitions in `corporate-suite-layout-family-matrix.md §1`. Annotated with the precise reason the sibling belongs there.

| # | Sibling | Family | Reference shape | Migration? |
|---|---|---|---|---|
| 1 | **Pragma** (advisory) | **LF-1 · Boardroom Vertical** | Multi-partner advisory firm with NDA-anchored proof; institution is the value. | None. Reference shape. |
| 2 | **Fiscus** (commercialista) | **LF-3 · Compliance Calendar** | Deadline-anchored regulated practice; calendar IS the value. | None. Slot-4 cycle is its identity. |
| 3 | **Solaria** (executive coaching) | **LF-4 · Manifesto-First** | Method-declared single-practitioner firm; method-statement IS the proposition. | None. The family slot retroactively names the shape Solaria already shipped. |
| 4 | **Continua** (stewardship) | **LF-3 today · LF-5 target** | Stewardship / family-office practice; the object (seal · codex · ledger · deed) IS the proof. | **Required**. IT-only rebuild before any further locale work. See `continua-lf5-migration-brief.md`. |

The first three rows close on annotation only. The fourth is the one that warrants a code pass.

### 1.1 · Why each sibling belongs there

Reasoning per sibling, in plain operational terms.

#### Pragma → LF-1
- Pragma's home is the literal reference shape the cluster grew from. Its L1–L9 tuple exactly matches the LF-1 row in the family matrix: `split-55-45 · A · absent · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col`.
- The professional fit (multi-partner advisory; partner names + ODCEC credentials carry the proof) matches what LF-1 was defined for in the family matrix §1.1.
- No mid-strip cadence cell — Pragma's pacing comes from the institution itself, not from a named cycle. That is exactly what L3=`absent` declares.
- All wireframe checks on Pragma already pass under the LF-1 declaration (it IS the declaration). No B-LAYOUT-1/2/3 work needed beyond filing the row.

#### Fiscus → LF-3
- Fiscus inherits LF-1's hero, pillars, KPI band, leadership, cases shape, navbar, and footer wholesale. Its single structural divergence is the `<section class="cs-cycle">` cell at slot-4 (`home.html:578`) carrying the (mese · scadenza · ambito) calendar tuple.
- That single cell is the family's identity — LF-3 is exactly "LF-1 plus a slot-4 calendar-cadence cell." The L1–L9 tuple matches `split-55-45 · A+slot4 · slot-4 · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col`.
- Professional fit (commercialista presidio · revisione legale · OAM brokerage · ANC payroll) matches the family's deadline-anchored profile.
- Fiscus's slot-4 cell shape is now a **claimed** mid-strip slot. The next sibling that wants a slot-4 cycle has to reshape the cell or pick a different slot.

#### Solaria → LF-4
- Solaria's home already replaces pillars with a manifesto block (`cs-manifesto`), enumerates a percorsi block, places the dark KPI band at slot-4 (after percorsi), inserts the method-cadenza strip at slot-5, **omits leadership** (the firm is single-coach), and closes with a list-row cases block + dark CTA.
- That sequence matches the LF-4 row exactly: `split-55-45 · C · slot-5 · manifesto-replacement · band-at-5 · absent · list-row · sticky-top · 3-col`.
- The empty-leadership debt the cluster had been carrying turns into a designed feature — LF-4's L6=`absent` makes the omission deliberate. F-LAYOUT-02 (empty-section debt) is closed for Solaria as soon as the registry row carries `layout_family=LF-4` and the shell respects it.
- Professional fit (executive coach · fiduciary · public-trust independent director · solo notary practice) matches the method-declared single-practitioner profile.

#### Continua → LF-3 today · LF-5 target
- Continua's current home shares Fiscus's full L1–L9 tuple. The matrix scoring confirms it: Fiscus vs Continua = **0/9 different** today, which is an F-LAYOUT-01 (skin-only differentiation collapse) failure waiting to be filed.
- The only structural divergence Continua has from Fiscus today is the cycle-strip's *copy* — (presidio · figura · orizzonte) instead of (mese · scadenza · ambito). Both are 3-cell `(eyebrow, figure, context)` tuples in the same `<section class="cs-cycle">` at slot-4. That is in-family variation, not a family difference.
- Continua's professional fit (stewardship · custody · family-office · notarile · archive-led continuity) is the LF-5 reference profile. The migration is corrective, not exploratory: the family slot was always the right home.
- Migration target tuple per the family matrix: `object-overlay · D · slot-2 · 2x2-with-image · band-at-4 · pillar-photo · timeline · condensed-minimal-top · 4-col-with-whistleblowing`. After the migration, Fiscus vs Continua = 8/9 different (only L8 stays close — both are sticky-top variants).

---

## 2 · What must stay unchanged per sibling

The backfill does not touch any sibling's source. This section is the **freeze list** — everything the backfill explicitly forbids the Continua-rebuild pass (or any incidental edit) from disturbing.

### 2.1 · Pragma (LF-1) — full freeze
No surface may change during the Continua rebuild. If the rebuild needs a refactor of `home.html` into `_layouts/{lf1..lf5}/home.html` (open question §7.1 of the divergence plan), Pragma's render at `_layouts/lf1/home.html` MUST be byte-equivalent to today's `home.html` for Pragma's `page_data`. Specifically:

- `cs-hero` 55/45 grid with serif-h1 LEFT + photo RIGHT, min-height 620px.
- `cs-pillars` 3-up `auto-fit minmax(220px, 1fr)` numbered grid.
- Dark KPI band at slot-3 with 3–4 stats.
- Sectors ribbon + trust marquee at slots 4–5.
- Typographic 3-card leadership at slot-6.
- List-row cases at slot-7.
- Dark CTA closer at slot-8.
- Sticky-top primary nav with wordmark-L + 5-link inline + phone-R.
- 3-col footer (brand + sitemap + contact).

Visual regression budget: **0 px** of bounding-box drift on the Pragma 1920px wireframe vs the pre-backfill capture.

### 2.2 · Fiscus (LF-3) — full freeze
Same freeze rule as Pragma. The `cs-cycle` cell at slot-4 with the (mese · scadenza · ambito) calendar tuple is **the family's identity** — moving it, reshaping it, or replacing the cell tuple shape breaks Fiscus's LF-3 occupancy and forces a re-classification. Specifically:

- Hero, pillars, KPI band, sectors, trust, leadership, cases, CTA, navbar, footer: identical to LF-1.
- `cs-cycle` at slot-4 with three `(eyebrow, figure, context)` cells. Eyebrow = month, figure = deadline date, context = scope phrase.
- 4-card typographic leadership (Fiscus is the 4-card variant of LF-1's typographic grid).

Visual regression budget: **0 px** of bounding-box drift on the Fiscus 1920px wireframe.

### 2.3 · Solaria (LF-4) — full freeze + state-lock
Solaria is in a multilingual + public-flip-held state (`phase_x4_solaria_passC_public_review` in MEMORY.md). The backfill MUST NOT:

- Change the `cs-manifesto` block at slot-2.
- Change the `cs-percorsi` enumeration at slot-3.
- Move the dark KPI band off slot-4.
- Re-introduce a `cs-leadership` section (L6=`absent` is the family's choice and the empty-grid debt is closed by the family declaration, not by adding content).
- Change the `cs-cycle` cell at slot-5 (method-cadenza, not calendar).
- Touch the `tier=draft` lock or the registry locale list.
- Touch the `?preview=1` propagation closed in `phase_x4_corporate_suite_case_parent_fix`.

Solaria's public-flip is held pending user authorization per R-SOL-8. The backfill does not touch that gate.

### 2.4 · Continua (LF-3 today) — preserved until rebuild lands
Continua is at draft tier with IT-only locale and `?preview=1` propagation working (`phase_x4_continua_pass1_5_review_lock` GREEN). The backfill MUST NOT:

- Touch Continua's existing `templates/live_templates/business/corporate-suite/home.html` shared file (any edit here cascades to Pragma + Fiscus + Solaria).
- Touch Continua's `apps/catalog/template_content_continua.py` page_data shape.
- Touch the cycle-strip copy in IT.
- Touch Continua's imagery pack — it is already object-led from Pass 1 and will carry into LF-5 unchanged.
- Add EN/FR/ES/AR locales (deferred until after LF-5 IT lands).
- Flip `tier=draft` → `tier=public`.

The next pass (the rebuild) is the first one allowed to touch Continua's render.

---

## 3 · Cluster-wide invariants the backfill protects

Independent of which family a sibling occupies, the cluster's brand contract holds. CS-LAYOUT-20 (in the variance rules) lists 12 domains of archetype-shared rules. The backfill does not relax any of them. The Continua rebuild MUST inherit them verbatim.

The non-negotiables:

1. Serif heading + sans body family · italic-`<em>` emphasis only · no bold · no uppercase headings.
2. Cream paper baseline · accent budget ≤3 hits per viewport.
3. h1 AAA contrast on cream · dark-section descendant contrast ≥ AA + ΔL ≥120.
4. Pexels-only imagery · zero URL overlap across siblings · 3-second subject check.
5. Locale-pill switcher · `lang` + `dir` per link · Latin wordmark + numerics in RTL · voice anchor verbatim across 5 locales.
6. 100×72 section padding · max-width 1400px · no extra inter-section margins.
7. Hero/pillar/KPI/leadership/cases density ceilings (CS-DENSITY-01..07).
8. One dark band per home (CS-TONE-03) — LF-5's band-at-4 satisfies this.
9. Reduced-motion honoured on every animated path.
10. Editor click-to-edit isolated by `body.mw-is-editor-preview`.
11. CTA contract — one primary per viewport · advisor-voice copy · real route hrefs.
12. `:focus-visible` gold ring (2px outline + 4px offset).
13. Whistleblowing legal-row entry where D.lgs. 24/2023 applies (LF-5 promotes this to a footer column at L9).
14. ≤720px responsive collapse — hero stacks, nav becomes hamburger drawer, footer collapses.

Any rebuild work that breaches one of these triggers a § decision per the variance rules §3.

---

## 4 · What the backfill is filing vs deferring

### 4.1 · Filed in this pass
- Per-sibling family assignment record (this report §1) with reasoning.
- Per-sibling freeze list (this report §2).
- Pointer document at `corporate-suite-layout-family-assignment.md` for the orchestrator's reference layer.
- Continua LF-5 migration brief at `continua-lf5-migration-brief.md` — implementation-ready hand-off.

### 4.2 · Deferred to the rebuild pass (Step 3)
- The shape of the `home.html` refactor — single file with template-tag dispatch vs split into `_layouts/{lf1..lf5}/home.html`. Recommendation: split. Decision binds at rebuild start.
- The registry surface for `layout_family` — `WebTemplate` column, `template_dna.py` field, or both. Recommendation: both. Decision binds at rebuild start.
- The Continua LF-5 page_data shape (cycle promoted to slot-2 · 4-pillar matrix · timeline cases · 4-col footer). The brief sketches it; the rebuild pass writes it.

### 4.3 · Deferred to later passes
- Continua multilingual rollout (5 locales + RTL) — only after LF-5 IT lands GREEN at the new browser gates.
- 5th sibling at LF-2 (Editorial Spread) — Step 6 of the divergence plan.
- LF-6 activation — held until a real candidate enrolls.
- Pragma↔Fiscus 2/9 audit per the divergence plan §10 Step 7. The backfill notes the score; no remediation runs in this pass.

---

## 5 · Order of operations for the Continua rebuild (next pass)

This section is the operational hand-off. It is written so the rebuild session can read directly from here without re-deriving anything.

1. **Confirm freeze**. Re-check git status for Pragma · Fiscus · Solaria — no drift since this report's date. The cluster is held still while LF-5 is built.
2. **Decide refactor shape**. Choose `_layouts/{lf1..lf5}/home.html` split vs single-file dispatch. Recommended: split (cleaner blast radius; one family rebuild touches one file).
3. **Add registry surface**. Add `layout_family` to `WebTemplate` (or equivalent registry path) with seed values: Pragma=LF-1, Fiscus=LF-3, Solaria=LF-4, Continua=LF-5. Migration runs once, idempotent.
4. **Move existing render**. Move today's `home.html` to `_layouts/lf1/home.html` byte-equivalent. Pragma/Fiscus/Solaria render through the same file with their existing page_data; Solaria/Fiscus pass `extends "_layouts/lf3/home.html"` / `_layouts/lf4/home.html` respectively, OR the router resolves at `_base.html` level.
5. **Build LF-3 and LF-4 layouts**. These are byte-equivalent renders for Fiscus and Solaria using their existing page_data. The point is to have files in the new shape so LF-5 can be added beside them, not to change Fiscus or Solaria visually. **Visual regression budget for these = 0 px**.
6. **Build LF-5 layout**. Implement `_layouts/lf5/home.html` per the family matrix LF-5 row. New section sequence D, new hero geometry, new cases shape, new footer.
7. **Update Continua's page_data**. `template_content_continua.py` adds the LF-5-specific shape — object-hero credit overlays, slot-2 cycle (governance), 4-pillar matrix (Custodia · Governance · Successione · Compliance), timeline cases, 4-col footer with whistleblowing column.
8. **IT-only walk**. Run the corporate-suite browser rubric on Continua at LF-5 in IT, **adding** the three new gates B-LAYOUT-1, B-LAYOUT-2, B-LAYOUT-3.
9. **Pragma/Fiscus/Solaria regression walk**. Re-run B-LAYOUT-1, B-LAYOUT-2, B-LAYOUT-3 on the three frozen siblings to confirm zero drift after the layout-router refactor.
10. **File evidence**. `factory/reports/scorecard/continua-pass2-lf5/` with build-report · style-critic · browser-verifier · responsive-auditor · contrast-accessibility · scorecard · summary. Wireframe captures pair-compared against Pragma · Fiscus · Solaria.
11. **Hold multilingual**. Continua tier stays `draft`. IT-only. Public-flip held. Multilingual deferred to a later workflow C pass.

---

## 6 · Browser checks that prove the backfill (and the rebuild)

The backfill itself has no live behaviour to verify — it is paperwork. The rebuild pass will run all of these.

| Gate | What it proves | Pass criterion |
|---|---|---|
| B-LAYOUT-1 (wireframe overlay) | Continua LF-5 wireframe is meaningfully different from Pragma · Fiscus · Solaria. | ≥30% bounding-box surface area differs vs each existing sibling. |
| B-LAYOUT-2 (DOM section list) | Continua's `<section class="cs-*">` list is not identical to any other sibling's. | List differs by ≥2 entries (insertions + deletions + re-orderings) vs every other sibling. |
| B-LAYOUT-3 (L1–L9 classification) | Live render matches the planner's declared family. | Classification = LF-5 exactly · ≥4 of 9 L-dimensions differ vs every existing sibling · no L1–L9 collision. |
| Pragma regression walk | Refactor did not drift Pragma's render. | 0 px wireframe diff vs pre-rebuild capture · all CS-* rules pass. |
| Fiscus regression walk | Refactor did not drift Fiscus's render. | 0 px wireframe diff · slot-4 cycle still renders. |
| Solaria regression walk | Refactor did not drift Solaria's render. | 0 px wireframe diff · manifesto + percorsi + omitted-leadership preserved. |
| Continua scorecard | Standard corporate-suite rubric still passes at LF-5. | Aggregate ≥4.50 · 0 BLOCKING · ≤3 STRONG. |

The first three gates are the new ones. The last four are the existing rubric applied to the four current siblings post-refactor.

---

## 7 · Risk acknowledgement

Risks the backfill is documenting so the rebuild session inherits them rather than discovering them mid-build. (See also the migration brief §6 for the top-5.)

- **Refactor blast radius**. Splitting `home.html` into `_layouts/{lf1..lf5}/` touches three currently-shipping siblings even though only one needs visual change. Mitigation: byte-equivalence regression walk on Pragma/Fiscus/Solaria.
- **Italic-em layout coupling**. CS-EXEC-01 / R7 places `<em>` on a specific word in the voice anchor. LF-5's hero overlays the h1 lower-third on the photo — italic word position interacts with the photo's bright/dark zone. This is a build-time choice and binds the LF-5 hero's photo selection.
- **Whistleblowing column compaction**. LF-5's L9=`4-col-with-whistleblowing` plus the ≤720px footer collapse rule must keep the whistleblowing channel surfaced even in stacked mobile (CS-FOOT-02). This is checked at responsive-auditor.
- **One-dark-band economy**. LF-5 places the band at slot-4 (post-cycle, post-pillars). The rebuild MUST NOT silently introduce a second dark band by re-tinting the cycle or sectors band.
- **Empty-grid regression**. If Continua's existing leadership data does not fit the LF-5 `pillar-photo` shape, the rebuild MUST NOT fall back to L6=`absent` — the family declares pillar-photo, and the data must support it. Otherwise the family declaration is wrong.

---

## 8 · Final sibling family map

For fast reference. Backfill state at this report's close.

```
Pragma   (advisory)       → LF-1 · Boardroom Vertical          · no migration · reference shape
Fiscus   (commercialista) → LF-3 · Compliance Calendar         · no migration · slot-4 calendar IS the family
Solaria  (coaching)       → LF-4 · Manifesto-First             · no migration · empty-leadership debt closed by L6=absent
Continua (stewardship)    → LF-3 today · LF-5 target           · MIGRATION REQUIRED · IT-only rebuild
```

```
Open territory after migration:
  LF-2 · Editorial Spread       · OPEN  · 5th sibling (architecture / evidence-led law / independent director)
  LF-6 · Rail-Side Chrome       · RESERVED · activates on 6th–7th sibling
  LF-{NEW}                      · OPEN  · planner-declared addendum on a non-fitting candidate
```

---

## 9 · Continua current vs target (one-screen summary)

| Dimension | Continua today (LF-3) | Continua target (LF-5) | Change required |
|---|---|---|---|
| L1 hero geometry | `split-55-45` (serif-L + photo-R) | `object-overlay` (full-bleed object photo + lower-third h1 + 2 credit overlays) | **CHANGE** — hero rebuilt |
| L2 section sequence | A+slot4 (cycle at 4) | D (cycle at 2) | **CHANGE** — sequence reordered |
| L3 mid-strip slot | `slot-4` (between KPI and sectors) | `slot-2` (immediately post-hero) | **CHANGE** — cycle promoted |
| L4 pillars treatment | `numbered-grid` (3-up) | `2x2-with-image` (4-pillar matrix: Custodia · Governance · Successione · Compliance) | **CHANGE** — 3 cards → 4 pillars + image |
| L5 KPI placement | `band-at-3` | `band-at-4` (post-cycle, post-pillars) | **CHANGE** — band moved one slot down |
| L6 leadership presence | `typographic-grid` | `pillar-photo` (3 environmental portraits — vault / desk / boardroom) | **CHANGE** — typographic → environmental photos |
| L7 cases-preview shape | `list-row` | `timeline` (year + mandate + horizon vertical) | **CHANGE** — list → timeline |
| L8 navbar geometry | `sticky-top` | `condensed-minimal-top` (76px → 64px · no phone-right) | **CHANGE** — minor; chrome compaction |
| L9 footer structure | `3-col` | `4-col-with-whistleblowing` (D.lgs. 24/2023 column) | **CHANGE** — 3-col → 4-col |
| Imagery pack | object-led (already from Pass 1) | object-led (carries through unchanged) | NO CHANGE |
| Voice anchor (IT) | "Continuità che attraversa generazioni" (or current IT anchor) | unchanged · italic-em re-anchored to overlaid h1 | re-target, not rewrite |
| Locales | IT only | IT only at this stage | NO CHANGE |
| Tier | `draft` | `draft` | NO CHANGE |
| Cycle copy | (presidio · figura · orizzonte) IT | unchanged tuple shape, slot moves | copy text preserved |

**9/9 layout dimensions move; 4/4 brand contract dimensions hold still.** The migration is structural, not skinning.

---

## 10 · Top 5 migration risks for Continua LF-5

Ordered by how much they could cost if not addressed at planning time.

1. **Refactor regression on Pragma · Fiscus · Solaria.** Splitting `home.html` cascades to three shipping templates. A byte-equivalence walk on each is mandatory before LF-5 build begins. Skipping this risks collateral damage on Solaria (currently held mid-public-flip) and Fiscus (currently shipped).
2. **L6 photo data shortfall.** LF-5's `pillar-photo` leadership requires environmental portraits (partner-at-archive · partner-at-desk · partner-at-boardroom). If Continua's current leadership content does not have such portraits, the rebuild blocks on a Pexels pack expansion AND a second style-critic on the new images. Plan the imagery before the build; do not discover it mid-pass.
3. **Italic-em re-anchoring on overlaid h1.** When the hero h1 moves into the photo's lower-third overlay, the `<em>` word lands on top of an image region whose luminance is unknown until the photo is final. CS-HERO-03 (h1 AAA contrast on cream) becomes h1 AAA contrast on a *darkened* photo overlay, which is a different proof. The image must be pre-graded for ≥AAA where the h1 sits, or a translucent dark plate placed under the overlay.
4. **Whistleblowing column dropping at ≤720px.** LF-5 promotes whistleblowing to a first-class footer column. The ≤720px stack must not collapse it into a sub-link of "contact" — that breaks CS-FOOT-02. Responsive-auditor must explicitly assert the whistleblowing channel is reachable in one tap on mobile.
5. **B-LAYOUT-3 drift between intake and walk.** Easiest failure mode: builder changes hero (L1) and leadership (L6) but leaves cases as `list-row` (L7) because timeline is "harder." Result: Continua walks as a hybrid LF-5/LF-3 and gets re-spec'd. Mitigation: B-LAYOUT-3 classification runs at build mid-point, not just at walk close.

---

## 11 · Exact next action

> **Open the Continua LF-5 rebuild session as Step 3 of the layout-divergence plan.** Read this report + `corporate-suite-layout-family-assignment.md` + `continua-lf5-migration-brief.md` in that order. Confirm cluster freeze (Pragma · Fiscus · Solaria untouched since 2026-04-29). Decide the `home.html` refactor shape (recommended: split into `_layouts/{lf1..lf5}/home.html`). Add `layout_family` to the registry with seed values for the four siblings. Move existing `home.html` → `_layouts/lf1/home.html` byte-equivalent. Build LF-3 and LF-4 byte-equivalent shells beside it. Build LF-5 fresh. Update Continua's `template_content_continua.py` page_data to the LF-5 shape. Walk Continua IT-only against B-LAYOUT-1/2/3 plus the standard corporate-suite browser rubric. Regression-walk Pragma · Fiscus · Solaria for 0 px wireframe drift. File evidence in `factory/reports/scorecard/continua-pass2-lf5/`. Hold multilingual.

That is the one action the next session takes. Everything else in §5 unfolds inside it.
