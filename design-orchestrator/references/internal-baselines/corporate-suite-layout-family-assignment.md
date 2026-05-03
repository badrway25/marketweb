# Corporate-suite layout-family assignment

**Status**: assignment v2 · post-Cornice 5-column refresh · live state
**Date**: 2026-05-03 (refresh) · supersedes 2026-04-29 v1 (pre-Cornice · Continua "pending migration")
**Refresh source**: `corporate-suite-live-family-map.md` (5-sibling state · authoritative) + `cornice-lf2-reference-pack.md` (LF-2 detail) + `phase_x4_continua_public_flip.md` + `phase_x5_cornice_public_flip.md`.
**Scope**: corporate-suite archetype only.
**Companion files**: `corporate-suite-distinctness-matrix.md` (5-column refresh) · `corporate-suite-reference-pack.md` (5-column refresh) · `corporate-suite-live-family-map.md` (5-sibling map · authoritative for live state) · `cornice-lf2-reference-pack.md` (LF-2 second-occupant rules) · `factory/reports/hardening/corporate-suite-layout-{divergence-plan,variance-rules,family-matrix,family-backfill}.md`.

This is the orchestrator's single-page reference for *which sibling occupies which layout family*, and *what each sibling is locked to* until further notice. The factory hardening reports hold the full reasoning; this file is the short-form lookup. **Five layout-family slots are now CLAIMED (LF-1..LF-5); LF-6 reserved; LF-{NEW} open.**

---

## 1 · Sibling → family map (live · 5 siblings)

| Sibling | Slug | Family | L1–L9 tuple | Status |
|---|---|---|---|---|
| **Pragma** (corporate advisory) | `pragma-corporate-suite` | **LF-1 · Boardroom Vertical** | `split-55-45 · A · absent · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col` | **Active · published_live · 5 locales · IT/EN/FR/ES/AR + RTL** |
| **Cornice** (architecture studio) | `cornice-architettura` | **LF-2 · Editorial Spread** | `stacked-editorial · B · absent · essay-with-anchors · hero-overlay · single-portrait-feature · magazine-grid · split-wordmark-top · 4-col-with-whistleblowing` | **Active · published_live · 5 locales · IT/EN/FR/ES/AR + RTL · Naskh h1 LF-2-scoped** |
| **Fiscus** (commercialista presidio) | `fiscus-commercialista` | **LF-3 · Compliance Calendar** | `split-55-45 · A+slot4 · slot-4 · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col` | **Active · published_live · 5 locales · IT/EN/FR/ES/AR + RTL** |
| **Solaria** (executive coaching) | `solaria-coaching` | **LF-4 · Manifesto-First** | `split-55-45 · C · slot-5 · manifesto-replacement · band-at-5 · absent · list-row · sticky-top · 3-col` | **Active · published_live · 5 locales · IT/EN/FR/ES/AR + RTL** |
| **Continua** (stewardship · family-office) | `continua-stewardship` | **LF-5 · Stewardship Object-Hero** | `object-overlay · D · slot-2 · 2x2-with-image · band-at-4 · pillar-photo · timeline · condensed-minimal-top · 4-col-with-whistleblowing` | **Active · published_live · 5 locales · IT/EN/FR/ES/AR + RTL** |
| ~~Continua~~ (LF-3 superseded record) | ~~`continua-stewardship`~~ | ~~LF-3~~ | ~~`split-55-45 · A+slot4 · slot-4 · numbered-grid · band-at-3 · typographic-grid · list-row · sticky-top · 3-col`~~ | **Superseded** by LF-5 · migration completed and public-flipped 2026-04-30 (`phase_x4_continua_public_flip.md`) |

Per CS-LAYOUT-11 (no two siblings may share a layout family · cf. `factory/reports/hardening/corporate-suite-layout-variance-rules.md §2`): **LF-1, LF-2, LF-3, LF-4, LF-5 are all CLAIMED**. LF-6 is reserved for 6th–7th sibling. LF-{NEW} is open for any candidate that doesn't fit LF-1..LF-6.

The Continua LF-3 → LF-5 migration is closed (Continua public-flipped at LF-5 on 2026-04-30 · Cornice public-flipped at LF-2 on 2026-05-01). The original "pending migration" annotation has been retired.

---

## 2 · Why each sibling sits in its family

Plain operational reasoning — what about the firm makes the family the right fit.

### Pragma → LF-1
Multi-partner advisory firm. Partners + ODCEC credentials carry the proof. Numeric KPIs are the badge of seriousness. Institution itself is the value — no named cadence cell needed. This is exactly LF-1's reference profile, and Pragma's home is the literal shape LF-1 was defined from.

### Cornice → LF-2
Single-principal Milanese architecture studio (Marta Roveri · STUDIO DI ARCHITETTURA · DAL 2008). The proof is the **case-bundle** (90 fascicoli · 38 menzioni · concorso wins · MIBAC restauro commissions), not the partner roster or the calendar or the KPI tuple. The home reads as a publication: stacked-editorial hero with KPI in photo overlay, rust-drop-cap narrative essay with 3 pull-quotes and a sticky 4-link side-rail, sectors ribbon (no trust marquee), single-portrait masthead (1 environmental portrait of the founder + 4 OAPPC/MIBAC credentials), 3+1 magazine grid of cases, hairline-bordered cream CTA closer. Chrome reads as editorial: cream-paper navbar with split-line masthead "CORNICE / studio di architettura" + filled-rust trailing CTA, 4-col footer with whistleblowing column. CS-TONE-03 demoted at the family level (zero dark bands on home · ratified at A.6 review-lock and re-ratified at workflow C/D/flip). AR h1 swaps to Noto Naskh Arabic via `body.cs-lf-lf-2` selector-scope (zero leakage to LF-1/LF-3/LF-4/LF-5 verified at Continua AR h1 probe). Voice anchor `argomento` recurs verbatim across 5 locales on hero h1 + CTA closer h2.

### Fiscus → LF-3
Commercialista presidio · revisione legale · OAM-supervised brokerage profile. The firm's value lives in deadlines (mese · scadenza · ambito calendar). The slot-4 cycle cell is **structurally** what makes this firm different from a general advisory — and that structural fact is precisely what LF-3 captures.

### Solaria → LF-4
Executive coaching · single-coach firm. The method-statement (manifesto + percorsi enumeration + method-cadenza) IS the proposition. There are no partners to display, so a leadership grid would be empty by construction — LF-4 declares L6=`absent` and turns the empty-grid debt into a designed feature. Solaria already shipped this shape; the family slot retroactively named it.

### Continua → LF-5
Stewardship · custody · family-office · multi-generational mandate. The proof is the **object** — the seal, the codex, the ledger, the deed — and the cadence is **governance**, not deadline. LF-5's object-overlay hero (library reading-room interior · zero people · interior-warm-mahogany horizontal partner-desk), slot-2 governance-cycle (presidio · figura · orizzonte), 4-pillar 2×2 custodia matrix (Custodia · Governance · Successione · Compliance with monochrome icon images), pillar-photo leadership (3 environmental portraits at vault · partner-desk · boardroom), and timeline cases (year + mandate + horizon) all map to the firm's shape. Voice anchor `generazioni` recurs across hero h1 + CTA closer + footer signature (3 surfaces · stewardship register requires the wider recurrence). Continua walked the LF-3 → LF-5 migration in IT-only at workflow A.5/A.6, then through workflow C multilingual + workflow D + public flip (all 5 locales · published_live since 2026-04-30).

---

## 3 · Per-sibling freeze list

All five live siblings are at full freeze; no migration is pending. The following surfaces are frozen against any incidental edit by the 6th-sibling enrollment.

### Pragma (LF-1) — full freeze
- `cs-hero` 55/45 grid (serif h1 LEFT + photo RIGHT, min-height 620px).
- `cs-pillars` 3-up `auto-fit minmax(220px, 1fr)` numbered grid.
- Dark KPI band at slot-3 (3–4 stats).
- Sectors ribbon · trust marquee at slots 4–5.
- Typographic 3-card leadership at slot-6.
- List-row cases at slot-7.
- Dark CTA closer at slot-8.
- Sticky-top primary nav with wordmark-L + 5-link inline + phone-R.
- 3-col footer (brand + sitemap + contact).
- `business-corporate` Unsplash imagery pool (grandfathered W001 · CS-IMG-SRC-01 retro-curation backlog · NOT a flip blocker).
- Wireframe regression budget: **0 px** vs post-Cornice baseline capture.

### Cornice (LF-2) — full freeze
- `cs-hero` stacked-editorial geometry (full-bleed photo TOP · 8/4 below-fold split with serif h1 LEFT + side-quote RIGHT).
- KPI tuple in hero photo bottom-left credit-overlay frame (`(novanta fascicoli · 2008 · 38 menzioni)`).
- `cs-narrative` essay band at slot-2 (rust drop-cap on paragraph 1 + 3 pull-quotes + sticky 4-link side-rail).
- `cs-sectors-ribbon` at slot-3 (12-cell typology row · NO trust marquee).
- `cs-leadership-single` masthead at slot-4 (1 environmental portrait + 2-paragraph bio + 4 credentials · OAPPC Milano · MIBAC · monografia · concorsi).
- `cs-cases-magazine` 3+1 grid at slot-5 (1 hero card spans rows 1-3 + 3 small).
- `cs-cta-closer-cream` at slot-6 (cream paper + hairline rust borders + filled-rust CTA pill · NO dark band).
- `cs-nav--lf2` cream-paper navbar with split-line masthead "CORNICE / studio di architettura" + filled-rust trailing CTA · NO phone-right.
- 4-col footer with `cs-foot-col--whistleblowing` (D.lgs. 24/2023 architectural studio channel).
- Naskh AR h1 swap inside `body.cs-lf-lf-2` (`Noto Naskh Arabic` first in fontFamily computed-style).
- Voice anchor `argomento` verbatim on hero h1 + CTA closer h2 · em-on-the-noun across 5 locales (`argument` / `argument` / `argumento` / `حُجَّة`).
- Wireframe regression budget: **0 px** vs post-flip 2026-05-01 baseline capture.

### Fiscus (LF-3) — full freeze
- All LF-1 surfaces, plus:
- `cs-cycle` at slot-4 with three `(eyebrow=mese, figure=scadenza, context=ambito)` cells.
- 4-card typographic leadership (Fiscus's variant).
- Wireframe regression budget: **0 px**.

### Solaria (LF-4) — full freeze
- `cs-manifesto` block at slot-2 (replaces pillars).
- `cs-percorsi` enumeration at slot-3.
- Dark KPI band at slot-4.
- `cs-cycle` at slot-5 with `(inizio · cadenza · fine)` method cells.
- Leadership section omitted (L6=`absent` is the family's choice; do not re-introduce).
- List-row cases at slot-6.
- Dark CTA closer at slot-7.
- 5-locale registry · `tier=published_live`.
- `?preview=1` propagation across chrome (closed in `phase_x4_corporate_suite_case_parent_fix`).
- Wireframe regression budget: **0 px**.

### Continua (LF-5) — full freeze
- `cs-hero` object-overlay geometry (full-bleed library reading-room photo · zero people · interior-warm-mahogany · h1 OVERLAID lower-third · 2 corner credit overlays splitting governance-cycle).
- `cs-cycle` at slot-2 with three `(presidio · figura · orizzonte)` cells labelled "Ciclo di governance".
- `cs-pillars` 4-pillar 2×2 matrix at slot-3 with monochrome icon images (Custodia · Governance · Successione · Compliance).
- Dark KPI band at slot-4.
- Sectors band carrying whistleblowing surface at slot-5.
- `cs-leadership-pillar-photo` at slot-6 (3 environmental portraits · vault · partner-desk · boardroom).
- `cs-cases-timeline` at slot-7 (vertical timeline · year + mandate + horizon columns).
- Dark CTA closer at slot-8.
- `cs-nav--lf5` condensed-minimal navbar (76px → 64px · tighter wordmark · 5-link inline · NO phone-right).
- 4-col footer with `cs-foot-col--whistleblowing` (D.lgs. 24/2023 stewardship-firm channel).
- AR h1 stays Noto Kufi Arabic (cluster default · NOT overridden by LF-2's `body.cs-lf-lf-2` Naskh selector-scope · verified anonymously after Cornice flip).
- Voice anchor `generazioni` verbatim on hero h1 + CTA closer + footer signature · em-on-the-noun across 5 locales (`generations` / `générations` / `generaciones` / `الأجيال`).
- Wireframe regression budget: **0 px** vs post-Cornice 2026-05-01 baseline capture.

---

## 4 · Cluster invariants (inherited by every family)

Per CS-LAYOUT-20. These hold across LF-1..LF-5 — and across LF-2 second-occupant, LF-6 first occupant, LF-{NEW} when they enroll. A family that proposes deviation triggers a § decision review.

- Serif heading + sans body family · italic-`<em>` emphasis · no bold · no uppercase headings.
- Cream paper baseline · accent budget ≤3 hits per viewport.
- h1 AAA contrast on cream · dark-section descendant contrast ≥ AA + ΔL ≥120.
- Pexels-only imagery · zero URL overlap across siblings · 3-second subject check.
- Locale-pill switcher · `lang` + `dir` per link · Latin wordmark + numerics in RTL · voice anchor verbatim across 5 locales.
- 100×72 section padding · max-width 1400px.
- Density ceilings (CS-DENSITY-01..07).
- One dark band per home (CS-TONE-03) **OR** an explicit family-level demotion declared at planner-brief and ratified at A.6 review-lock (LF-2 is the precedent · do not generalize without the same explicit argument).
- Reduced-motion honoured.
- Editor click-to-edit isolated by `body.mw-is-editor-preview`.
- CTA contract — one primary per viewport, advisor-voice, real route hrefs.
- `:focus-visible` gold ring (2px outline + 4px offset).
- Whistleblowing legal-row entry where D.lgs. 24/2023 applies (LF-2 + LF-5 promote it to a footer column).
- ≤720px responsive collapse — hero stacks · nav becomes hamburger drawer · footer collapses. X.4a Step 1D added @media 1280/1100/880/720/480 + CSS-only hamburger drawer at ≤880 + overflow-x:clip root guard.

---

## 5 · Sibling-pair distinctness scoring (live · 10 pairs)

Counting differences in L1–L9 tuple. CS-LAYOUT-12 requires **≥4 of 9 dimensions to differ between any two siblings · OR a documented in-family near-occupant § decision** (Pragma↔Fiscus is the first and presently only documented near-occupant pair · 2026-05-03 · see `corporate-suite-distinctness-matrix.md §4` and `factory/reports/hardening/corporate-suite-layout-family-matrix.md §6`).

| Pair | L1–L9 differences | Verdict |
|---|---|---|
| Pragma (LF-1) ↔ Cornice (LF-2) | **9/9 different** | PASS · widest possible |
| Pragma (LF-1) ↔ Fiscus (LF-3) | **2/9 different** (L2, L3 only) | **PASS via § decision** (in-family near-occupant · 2026-05-03 · CS-LAYOUT-12 reworded) |
| Pragma (LF-1) ↔ Solaria (LF-4) | 5/9 different (L2, L3, L4, L5, L6) | PASS |
| Pragma (LF-1) ↔ Continua (LF-5) | **9/9 different** | PASS · widest possible |
| Cornice (LF-2) ↔ Fiscus (LF-3) | **9/9 different** | PASS · widest possible |
| Cornice (LF-2) ↔ Solaria (LF-4) | 8/9 different (L3=absent shared · different mechanism) | PASS · L3 collision is value-only, not cell-shape |
| Cornice (LF-2) ↔ Continua (LF-5) | 8/9 different (L9=4-col-with-whistleblowing shared · different content) | PASS · L9 collision is shape-shared by intent (D.lgs. 24/2023 compliance) |
| Fiscus (LF-3) ↔ Solaria (LF-4) | 5/9 different (L2, L3, L4, L5, L6) | PASS |
| Fiscus (LF-3) ↔ Continua (LF-5) | **8/9 different** (L8 close — both sticky-top variants) | PASS |
| Solaria (LF-4) ↔ Continua (LF-5) | **8/9 different** (L1, L2, L3, L4, L5, L6, L7, L9) | PASS |

**9 of 10 pairs ≥5/9.** The single 2/9 pair (Pragma↔Fiscus) is the cluster's documented in-family near-occupant pair · § decision filed 2026-05-03 · binding · single-exception ladder (a 2nd near-occupant pair triggers a § decision review on CS-LAYOUT-12 itself).

---

## 6 · Open territory

After Pragma=LF-1, Cornice=LF-2, Fiscus=LF-3, Solaria=LF-4, Continua=LF-5, the cluster's remaining family slots:

| Family | Status | Next sibling profile |
|---|---|---|
| LF-1 · Boardroom Vertical | **TAKEN by Pragma** | — |
| LF-2 · Editorial Spread | **TAKEN by Cornice** (1st occupant) · OPEN to second occupant | 2nd LF-2 occupant: portfolio-of-work-led firm (evidence-led litigation · independent directorship case-bundle · audit-led methodology with published methodology pieces · longitudinal research with publications · inchiesta-led journalism · conservation studio with restoration case-bundle). Inherits LF-2 L1–L9 verbatim · differentiates inside cells per `cornice-lf2-reference-pack.md §4 (anti-collapse rules)` and §9 (intake questions). |
| LF-3 · Compliance Calendar | **TAKEN by Fiscus** | — |
| LF-4 · Manifesto-First | **TAKEN by Solaria** | — |
| LF-5 · Stewardship Object-Hero | **TAKEN by Continua** | — |
| LF-6 · Rail-Side Chrome | **RESERVED** (provisional E sequence in matrix) | Magazine-edited boutique · public-hearing law · conservation studio · 6th–7th sibling. Planner files an addendum to `corporate-suite-layout-family-matrix.md §1` finalising the L1–L9 tuple before build. The provisional tuple is `side-rail-photo · E · slot-6 · side-quote-with-cards · band-at-4 · photo-grid · collage-3+1 · side-rail · condensed-single-row` — the first occupant binds it. |
| LF-{NEW} | **OPEN** | Any candidate that doesn't fit LF-1..LF-6. Planner files an addendum declaring the new L1–L9 tuple before build. The tuple must score ≥4/9 different vs every existing column (LF-1..LF-5) · ≥4/9 vs LF-6 if the planner intends LF-6 to remain reserved. |

**LF-1, LF-3, LF-4, LF-5 are CLAIMED.** Re-use of an occupied family is permitted only via DISTINCTNESS_RULES §5 option 3 (variant demotion) with explicit user approval. **LF-2 is CLAIMED but open to a second occupant** under the inheritance contract specified at `cornice-lf2-reference-pack.md §4`.

---

## 7 · Authority and update protocol

- **The authoritative live state is `corporate-suite-live-family-map.md`.** This file (`corporate-suite-layout-family-assignment.md`) is the orchestrator's slot-occupancy reference and short-form lookup. Where the two diverge, the live family map wins.
- **The factory hardening report `corporate-suite-family-backfill.md`** is the authoritative record of *why* assignments hold.
- **The family matrix `factory/reports/hardening/corporate-suite-layout-family-matrix.md`** is the source of truth for *what each family declares* (L1–L9 tuple per family).
- **Each new sibling adds a row to §1** at intake (declared) and at walk (rendered). Drift between declared and rendered = CS-LAYOUT-14 fail.
- **Migrations annotate, not overwrite**. Continua's superseded LF-3 row stays in §1 as a struck-through historical record; the active LF-5 row is the live state.
- **The freeze list in §3 is enforced by every subsequent build session** — the next builder reads §3 before any code change and confirms regression walks at the end.
- **Refresh cadence**: this file is refreshed at every public flip in the same hardening window. The post-Cornice reference hardening pass (2026-05-03 · `factory/reports/hardening/post-cornice-reference-hardening.md`) is the binding precedent — if a public flip lands and this file is not refreshed within the same hardening window, the next intake is held until refresh closes.

---

## 8 · Precondition for the 6th-sibling intake

Per `factory/reports/hardening/post-cornice-next-candidate-readiness.md §2` and the post-Cornice reference hardening pass (2026-05-03 · all P1–P4 closed), the 6th-sibling intake may now open under the following preconditions which are **all green**:

- [x] **P1** · 5-column reference layer refreshed (this file + `corporate-suite-distinctness-matrix.md` + `corporate-suite-reference-pack.md`).
- [x] **P2** · Pragma↔Fiscus 2/9 § decision filed (Option C · formal acceptance · CS-LAYOUT-12 reworded).
- [x] **P3** · Booking-flag test re-cohorted (Continua added to Wave-2 booking-shaped set · suite reads 546/546).
- [x] **P4** · 45-route smoke + 5-sibling 1920px regression capture clean.

The 6th-sibling intake reads this file's §6 first to pick a layout family slot, then reads `cornice-lf2-reference-pack.md §9` if LF-2 second occupant is selected, then files a planner brief at workflow A.1.
