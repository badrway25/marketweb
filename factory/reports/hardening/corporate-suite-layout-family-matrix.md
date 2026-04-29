# Corporate-suite layout family matrix

**Status**: matrix v1 · **Date**: 2026-04-29
**Scope**: corporate-suite archetype only.
**Companion files**: `corporate-suite-layout-divergence-plan.md` (the why) · `corporate-suite-layout-variance-rules.md` (the rule book).
**How to read**: this file is the source of truth for *which sibling occupies which family* and *what L1–L9 tuple defines each family*. Every new sibling either picks an existing open family (LF-2, LF-6) or claims `LF-{NEW}` and adds a row.

---

## 0 · How to use this matrix

1. **At intake (workflow A.1)**: planner picks a layout family from §1 below. If the intended professional fit doesn't match any existing family, the planner files an addendum to §3 declaring `LF-{NEW}` with its L1–L9 tuple.
2. **At plan (workflow A.2)**: planner fills the new sibling's L1–L9 row in §2 and confirms ≥4 of 9 layout dimensions differ vs every existing column.
3. **At critique (workflow A.6)**: style-critic re-reads §1 row for the declared family and flags any cell where the build deviated.
4. **At walk (workflow A.7)**: browser-verifier classifies the live render's L1–L9 (per CS-LAYOUT-01..09 value sets) and writes the row into §2. Drift between declared and rendered = CS-LAYOUT-14 fail.
5. **At release**: release-gatekeeper confirms the final §2 row matches the planner's intent and that no two siblings share the full tuple.

This file grows monotonically — rows are added, not replaced. When a sibling moves between families (e.g., Continua: LF-3 → LF-5 per the divergence plan Step 3), the row is **annotated** with the migration date, not overwritten.

---

## 1 · Family definitions

Five claimed families (LF-1..LF-5) + one reserved slot (LF-6). Each row declares the family's L1–L9 tuple, the professional fit, and the cluster occupant.

### LF-1 · Boardroom Vertical
- **Reference shape for**: multi-partner advisory firms with NDA-anchored proof. Numeric KPIs are the badge of seriousness; partners are the firm's faces.
- **Voice gravity**: decisional · gatekept · enterprise-formal.
- **Mid-strip identity**: none (institutional pacing without a named cadence cell).
- **Cluster occupant**: **Pragma** (advisory). Reference shape; no migration.
- **L1–L9 tuple**:

| Dim | Value | Notes |
|---|---|---|
| L1 hero geometry | `split-55-45` | Serif h1 LEFT, full-bleed photo RIGHT, 1.3fr / 1fr split, min-height 620px. |
| L2 section sequence | `A` = `cs-hero · cs-pillars · cs-kpi-band · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta` | The "default" sequence the cluster started from. |
| L3 mid-strip slot | `absent` | No named cadence cell. The institution is the proof. |
| L4 pillars treatment | `numbered-grid` | 3-up `auto-fit minmax(220px, 1fr)`, numbered serif eyebrow, primary-coloured top-rule. |
| L5 KPI placement | `band-at-3` | Dark band at section-3 with 3–4 stats. |
| L6 leadership presence | `typographic-grid` | 3-card row, no portrait photos, role + name + 2-3 credentials. |
| L7 cases-preview shape | `list-row` | Numbered rows with thumb · title · category · year · arrow. |
| L8 navbar geometry | `sticky-top` | Sticky 76px primary nav, wordmark-L + 5-link inline + phone-R. |
| L9 footer structure | `3-col` | Brand + sitemap + contact. |

### LF-2 · Editorial Spread
- **Reference shape for**: portfolio-of-work-led firms (architecture studios, evidence-led legal practices, independent directorships, audit-led methodologies). Cases ARE the proof; the firm is the curator.
- **Voice gravity**: editorial · case-led · curatorial.
- **Mid-strip identity**: none. KPI is folded into the hero credit overlay.
- **Cluster occupant**: **OPEN** (reserved for the 5th sibling — see plan Step 6).
- **L1–L9 tuple**:

| Dim | Value | Notes |
|---|---|---|
| L1 hero geometry | `stacked-editorial` | Full-bleed editorial photo TOP with credit overlay; serif h1 + side-quoted intro BELOW (8-col / 4-col). |
| L2 section sequence | `B` = `cs-hero · cs-narrative · cs-sectors · cs-leadership · cs-cases-preview · cs-cta` | Pillars REPLACED by editorial-narrative band. KPI band absent. Trust marquee absent. |
| L3 mid-strip slot | `absent` | Narrative covers the cadence-cell role. |
| L4 pillars treatment | `essay-with-anchors` | Four-paragraph essay with pull quotes and a side-rail of anchor links to services / about. |
| L5 KPI placement | `hero-overlay` | KPI promoted into the hero photo's credit overlay (3 stats inline). No dark band. |
| L6 leadership presence | `single-portrait-feature` | One large portrait masthead (founding partner / principal / managing director) with 2-paragraph bio + credentials. |
| L7 cases-preview shape | `magazine-grid` | 3+1 grid: 1 hero card + 3 small. Each card carries a photo. |
| L8 navbar geometry | `split-wordmark-top` | Sticky-top primary nav but the wordmark sits split-line (firm-name above, descriptor below) like a publication masthead. |
| L9 footer structure | `4-col-with-whistleblowing` | Brand + sitemap + contact + offices/disclosures (whistleblowing column). |

### LF-3 · Compliance Calendar
- **Reference shape for**: deadline-anchored regulated practices (commercialista presidio, revisione legale, OAM-supervised brokerage, ANC-affiliated payroll). The firm's value lives in the calendar.
- **Voice gravity**: scadenze-first · documented · institutional-fiscal.
- **Mid-strip identity**: calendar-cadence cell at slot-4.
- **Cluster occupant**: **Fiscus** (commercialista). No migration.
- **L1–L9 tuple**:

| Dim | Value | Notes |
|---|---|---|
| L1 hero geometry | `split-55-45` | Same as LF-1 hero shape; differentiator is below. |
| L2 section sequence | `A+slot4` = `cs-hero · cs-pillars · cs-kpi-band · cs-cycle · cs-sectors · cs-trust · cs-leadership · cs-cases-preview · cs-cta` | LF-1 sequence with calendar cell inserted at slot-4. |
| L3 mid-strip slot | `slot-4` | `cs-cycle` between KPI band and sectors. Cells: (mese · scadenza · ambito) tuple, named "Calendario fiscale". |
| L4 pillars treatment | `numbered-grid` | 3-up. |
| L5 KPI placement | `band-at-3` | Dark band at position 3. |
| L6 leadership presence | `typographic-grid` | 4-card row of ODCEC iscritti with credential lines. |
| L7 cases-preview shape | `list-row` | Same as LF-1. |
| L8 navbar geometry | `sticky-top` | Same as LF-1. |
| L9 footer structure | `3-col` | Same as LF-1. |

### LF-4 · Manifesto-First
- **Reference shape for**: method-declared single-practitioner firms (executive coach, fiduciary, public-trust independent director, individual notary practice). The method-statement IS the value proposition; partners are not the unit of trust.
- **Voice gravity**: bounded · method-declared · adult-to-adult.
- **Mid-strip identity**: method-cadenza cell at slot-5.
- **Cluster occupant**: **Solaria** (executive coaching). No migration; the family slot retroactively names the shape Solaria already shipped.
- **L1–L9 tuple**:

| Dim | Value | Notes |
|---|---|---|
| L1 hero geometry | `split-55-45` | Same hero shape as LF-1/LF-3. The differentiation is below. (LF-4 may at a later pass migrate L1 to a non-split geometry; not required.) |
| L2 section sequence | `C` = `cs-hero · cs-manifesto · cs-percorsi · cs-kpi-band · cs-cycle · cs-cases-preview · cs-cta` | Manifesto replaces pillars at section-2; percorsi enumeration at section-3; KPI shifts to section-4; method-cadenza-strip at section-5; **leadership omitted**; cases at section-6. |
| L3 mid-strip slot | `slot-5` | `cs-cycle` after KPI, named "Cadenza del metodo". Cells: (inizio · cadenza · fine) tuple. |
| L4 pillars treatment | `manifesto-replacement` | The pillars `<section>` is replaced by a `cs-manifesto` block (paragraph + voice-anchor h2 + supporting prose). |
| L5 KPI placement | `band-at-5` | Dark band shifts to post-percorsi position 4 — re-anchored from LF-1's slot-3 because the manifesto + percorsi already establish the propositional weight at slot-2..3. |
| L6 leadership presence | `absent` | Single-coach firm; no leadership grid. (Replaces the empty-grid debt today.) |
| L7 cases-preview shape | `list-row` | "Casi anonimizzati" with method-context per row. |
| L8 navbar geometry | `sticky-top` | Same as LF-1. |
| L9 footer structure | `3-col` | Same as LF-1. |

### LF-5 · Stewardship Object-Hero
- **Reference shape for**: custody / family-office / notarile / archive-led / continuity-driven practices. The object — the seal, the codex, the ledger, the deed — IS the proof. People are incidental.
- **Voice gravity**: custodial · longitudinal · stewardship-grade.
- **Mid-strip identity**: governance-cycle cell at slot-2 (promoted high in the cadence).
- **Cluster occupant**: **Continua** (stewardship) — **migration target**. Currently in LF-3 (DOM-identical to Fiscus); per the divergence plan Step 3, Continua moves to LF-5 in IT-only before its multilingual rollout.
- **L1–L9 tuple**:

| Dim | Value | Notes |
|---|---|---|
| L1 hero geometry | `object-overlay` | Full-bleed object-led photo (no people) with TWO credit-block overlays + serif h1 OVERLAID lower-third (no 55/45 split). Eyebrow + sub move into the credit overlays' frame. |
| L2 section sequence | `D` = `cs-hero · cs-cycle · cs-pillars · cs-kpi-band · cs-sectors · cs-leadership · cs-cases-preview · cs-cta` | Cycle promoted to slot-2 immediately after hero; pillars stay at slot-3 with 4-pillar matrix; KPI at slot-4 (post-cycle); sectors band carries whistleblowing surface; leadership at slot-6 (pillar-photo); cases timeline at slot-7; CTA tinted-cream at slot-8. |
| L3 mid-strip slot | `slot-2` | `cs-cycle` immediately post-hero, named "Ciclo di governance". Cells: (presidio · figura · orizzonte) tuple. |
| L4 pillars treatment | `2x2-with-image` | 4-pillar matrix in 2×2 layout (Custodia · Governance · Successione · Compliance), each with a small monochrome icon-image. |
| L5 KPI placement | `band-at-4` | Dark band at slot-4, after cycle and pillars. |
| L6 leadership presence | `pillar-photo` | 3-card row with environmental portraits (not portrait-headshot) — partner at the firm's archive vault, partner at the partner's-desk, partner at the boardroom-roundtable. |
| L7 cases-preview shape | `timeline` | Vertical timeline with year + mandate + horizon per row; clicking opens the case-study detail. |
| L8 navbar geometry | `condensed-minimal-top` | Sticky-top primary nav, but condensed (76px → 64px) with a tighter wordmark + 5-link row, no phone-right; the family's chrome reads as archive-room calm rather than boardroom presence. |
| L9 footer structure | `4-col-with-whistleblowing` | Brand + sitemap + contact + whistleblowing channel column (D.lgs. 24/2023 surfaced as a first-class element). |

### LF-6 · Rail-Side Chrome (RESERVED)
- **Reference shape for**: magazine-edited boutique firms — audit-led methodology, public-hearing law, conservation studios, longitudinal-research practices. The chrome itself reads as editorial.
- **Voice gravity**: editorial · methodological · long-form.
- **Mid-strip identity**: undecided at slot-6 (defaults to a methodology-stages cell).
- **Cluster occupant**: **OPEN** — held in reserve. Will activate when a real candidate enrolls.
- **L1–L9 tuple** (provisional — finalized when LF-6 first ships):

| Dim | Value | Notes |
|---|---|---|
| L1 hero geometry | `side-rail-photo` | Full-width-right photo + chrome-on-left rail. |
| L2 section sequence | `E` = `cs-hero · cs-pillars · cs-narrative · cs-kpi-band · cs-cycle · cs-cases-preview · cs-cta` | Pillars at slot-2; narrative at slot-3 (replaces sectors+trust); KPI at slot-4; cycle at slot-5; cases at slot-6. |
| L3 mid-strip slot | `slot-6` | Methodology-stages tuple. |
| L4 pillars treatment | `side-quote-with-cards` | Pull-quote on left rail, 3-card grid on right. |
| L5 KPI placement | `band-at-4` | Dark band post-narrative. |
| L6 leadership presence | `photo-grid` | 3–4 card photo grid. |
| L7 cases-preview shape | `collage-3+1` | Asymmetric collage of 4 cases. |
| L8 navbar geometry | `side-rail` | Vertical sidebar nav replaces sticky-top. |
| L9 footer structure | `condensed-single-row` | Single-row footer with crest + legal + contact inline. |

LF-6 stays reserved until a real candidate enrolls. The slot exists so the matrix has a known next family and so future intake decisions know that "side-rail nav" is on the menu but unclaimed.

---

## 2 · Per-sibling occupancy table

Append-only. Each row records a sibling's classification at one point in time. Migrations add a new row dated; the prior row is annotated `superseded`.

| Sibling | Family | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | Recorded | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pragma (advisory) | LF-1 | split-55-45 | A | absent | numbered-grid | band-at-3 | typographic-grid | list-row | sticky-top | 3-col | 2026-04-29 | active |
| Fiscus (commercialista) | LF-3 | split-55-45 | A+slot4 | slot-4 | numbered-grid | band-at-3 | typographic-grid | list-row | sticky-top | 3-col | 2026-04-29 | active |
| Solaria (coaching) | LF-4 | split-55-45 | C | slot-5 | manifesto-replacement | band-at-5 | absent | list-row | sticky-top | 3-col | 2026-04-29 | active |
| Continua (stewardship) | **LF-3** | split-55-45 | A+slot4 | slot-4 | numbered-grid | band-at-3 | typographic-grid | list-row | sticky-top | 3-col | 2026-04-29 | **superseded — migration to LF-5 planned** |
| Continua (stewardship) | **LF-5** | object-overlay | D | slot-2 | 2x2-with-image | band-at-4 | pillar-photo | timeline | condensed-minimal-top | 4-col-with-whistleblowing | 2026-04-29 (planned) | **target — pending Step 3 of the divergence plan** |

**Sibling-pair layout-distinctness scoring** (counting differences in L1–L9 tuple):

| Pair | Today (Continua at LF-3) | After Continua → LF-5 |
|---|---|---|
| Pragma vs Fiscus | 2/9 different (L2, L3) | 2/9 (unchanged) |
| Pragma vs Solaria | 5/9 different (L2, L3, L4, L5, L6) | 5/9 (unchanged) |
| Pragma vs Continua | 2/9 different (L2, L3) — **CS-LAYOUT-12 FAIL** | 9/9 different |
| Fiscus vs Solaria | 5/9 (L2, L3, L4, L5, L6) | 5/9 |
| Fiscus vs Continua | **0/9 different — F-LAYOUT-01 FAIL** | 8/9 different (L1, L2, L3, L4, L5, L6, L7, L9) |
| Solaria vs Continua | 5/9 (L2, L3, L4, L5, L6) | 8/9 (L1, L2, L3, L4, L5, L6, L7, L9) |

The Pragma↔Fiscus 2/9 score also flags — Pragma and Fiscus are too close on layout dimensions. They scrape past CS-LAYOUT-12 only by virtue of L7 (cases-preview) and L9 (footer) staying open and L3 (slot-4 cycle) being Fiscus's claim. **Step 7** of the divergence plan calls for an audit of Pragma's family fit; if the orchestrator decides Fiscus's slot-4 cycle is not enough wireframe-distinctness from Pragma, the next pass migrates one of them on L7 or L9. For now: hold the line and re-evaluate after Continua's migration lands.

---

## 3 · Open territory for new siblings

After Pragma=LF-1, Fiscus=LF-3, Solaria=LF-4, Continua=LF-5 (post-migration), the cluster's open layout-family territory is:

| Family | Status | Reserved for |
|---|---|---|
| LF-1 | TAKEN by Pragma | — |
| LF-2 | OPEN | Portfolio-led firms (architecture, evidence-led law, independent directorships, audit methodology). Ship at the 5th sibling enrollment per plan Step 6. |
| LF-3 | TAKEN by Fiscus | — |
| LF-4 | TAKEN by Solaria | — |
| LF-5 | TAKEN by Continua (post-migration) | — |
| LF-6 | RESERVED | Magazine-edited boutiques (side-rail nav, collage cases). Activate on the 6th–7th sibling. |
| LF-{NEW} | OPEN | Any candidate that doesn't fit LF-1..LF-6. Planner files an addendum declaring the new family's L1–L9 tuple before build. |

The next intake's professional-fit determines which open slot to claim. If two open slots both fit (LF-2 and LF-{NEW}), the planner prefers the one already declared — the matrix's open-but-declared slots are cheaper to ship than full new-family additions.

---

## 4 · Forbidden tuples (extending the prohibition list)

Lifted from the divergence plan §6 and bound here as match-able tuples for fast scan during plan and walk.

After the migration, the following L1–L9 tuples are **claimed** and may not be reused by any new sibling without DISTINCTNESS_RULES §5 escalation:

```
LF-1 :: (split-55-45, A,        absent, numbered-grid,           band-at-3, typographic-grid,        list-row,       sticky-top,            3-col)
LF-3 :: (split-55-45, A+slot4,  slot-4, numbered-grid,           band-at-3, typographic-grid,        list-row,       sticky-top,            3-col)
LF-4 :: (split-55-45, C,        slot-5, manifesto-replacement,   band-at-5, absent,                  list-row,       sticky-top,            3-col)
LF-5 :: (object-overlay, D,     slot-2, 2x2-with-image,          band-at-4, pillar-photo,            timeline,       condensed-minimal-top, 4-col-with-whistleblowing)
```

A new sibling whose declared L1–L9 tuple matches any of the above on ≥6 of 9 dimensions is treated as a duplicate of that family and must be re-spec.

The L1+L2+L7 sub-tuple is the highest-leverage anti-collision check (CS-LAYOUT-13 BLOCKING):

```
(L1, L2, L7) — at least one must differ vs every existing sibling
LF-1: (split-55-45, A,       list-row)
LF-3: (split-55-45, A+slot4, list-row)   ← differs from LF-1 only on L2
LF-4: (split-55-45, C,       list-row)   ← differs from LF-1 on L2 only at this sub-tuple level
LF-5: (object-overlay, D,    timeline)   ← differs from all three on all three sub-axes
```

Notice that LF-3 and LF-4 differ from LF-1 on **only L2** at the (L1, L2, L7) sub-tuple — they pass CS-LAYOUT-13 by virtue of L2 differing, but barely. LF-5's full (L1, L2, L7) divergence is what makes it the high-confidence migration target for Continua. Future siblings should aim for LF-5-class divergence on the (L1, L2, L7) sub-tuple, not LF-3-style "differ on L2 only."

---

## 5 · Maintenance

- **Each new sibling adds rows to §2** at intake (declared row) and at walk (rendered row). If the rows differ, F-LAYOUT-06 fires.
- **Each layout-touching edit-pass appends a new row** to §2 with a new `Recorded` date. The prior row is annotated `superseded`.
- **§1 family rows are append-only** for new families (LF-7, LF-8, ...). Existing family definitions are revised only with explicit user approval — the family's tuple is its identity, and changing it mid-life renames the family.
- **§3 OPEN/RESERVED slots are updated** as siblings enroll.
- **§4 forbidden tuples list** is regenerated whenever §1 changes.

This file is the orchestrator's mechanical source of truth for layout-family occupancy. The planner reads §1 and §3 at intake; the style-critic reads §1 at critique; the walk-verifier writes §2 at walk; the release-gatekeeper reads §2 and §4 at release. Every gate has a row to look at.
