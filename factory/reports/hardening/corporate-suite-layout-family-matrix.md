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
| Continua (stewardship) | **LF-3** | split-55-45 | A+slot4 | slot-4 | numbered-grid | band-at-3 | typographic-grid | list-row | sticky-top | 3-col | 2026-04-29 | **superseded** — migration to LF-5 completed and public-flipped 2026-04-30 |
| Continua (stewardship) | **LF-5** | object-overlay | D | slot-2 | 2x2-with-image | band-at-4 | pillar-photo | timeline | condensed-minimal-top | 4-col-with-whistleblowing | 2026-04-30 | **active** · public-flipped (`phase_x4_continua_public_flip.md`) |
| Cornice (architecture studio) | **LF-2** | stacked-editorial | B | absent | essay-with-anchors | hero-overlay | single-portrait-feature | magazine-grid | split-wordmark-top | 4-col-with-whistleblowing | 2026-05-01 | **active** · public-flipped (`phase_x5_cornice_public_flip.md`) · 1st LF-2 occupant |

**Sibling-pair layout-distinctness scoring** (counting differences in L1–L9 tuple · 5 live siblings · 10 pairs · post-Cornice):

| Pair | L1–L9 differences | Verdict |
|---|---|---|
| Pragma (LF-1) vs Cornice (LF-2) | **9/9 different** | PASS · widest possible |
| Pragma (LF-1) vs Fiscus (LF-3) | **2/9 different** (L2, L3 only) | **PASS via § decision (in-family near-occupant · 2026-05-03 · CS-LAYOUT-12 reworded · see §6)** |
| Pragma (LF-1) vs Solaria (LF-4) | 5/9 different (L2, L3, L4, L5, L6) | PASS |
| Pragma (LF-1) vs Continua (LF-5) | **9/9 different** | PASS · widest possible |
| Cornice (LF-2) vs Fiscus (LF-3) | **9/9 different** | PASS · widest possible |
| Cornice (LF-2) vs Solaria (LF-4) | 8/9 different (L3=`absent` shared · different mechanism) | PASS · L3 collision is value-only, not cell-shape |
| Cornice (LF-2) vs Continua (LF-5) | 8/9 different (L9=`4-col-with-whistleblowing` shared · different content) | PASS · L9 collision is shape-shared by intent (D.lgs. 24/2023 compliance posture) |
| Fiscus (LF-3) vs Solaria (LF-4) | 5/9 different (L2, L3, L4, L5, L6) | PASS |
| Fiscus (LF-3) vs Continua (LF-5) | **8/9 different** (L8 close — both sticky-top variants) | PASS |
| Solaria (LF-4) vs Continua (LF-5) | **8/9 different** (L1, L2, L3, L4, L5, L6, L7, L9) | PASS |

**9 of 10 pairs ≥5/9.** The single 2/9 pair (Pragma↔Fiscus) is the cluster's documented in-family near-occupant pair · § decision filed 2026-05-03 · binding · single-exception ladder (a 2nd near-occupant pair triggers a § decision review on CS-LAYOUT-12 itself · see §6 below). The original "Continua vs Fiscus 0/9" and "Pragma vs Continua 2/9" failure states were closed by the Continua LF-3 → LF-5 migration (2026-04-30 public-flipped).

---

## 3 · Open territory for new siblings (post-Cornice · 5 LF claimed)

After Pragma=LF-1, **Cornice=LF-2** (2026-05-01 public-flipped · 1st LF-2 occupant), Fiscus=LF-3, Solaria=LF-4, Continua=LF-5 (2026-04-30 public-flipped · post-migration), the cluster's open layout-family territory is:

| Family | Status | Reserved for |
|---|---|---|
| LF-1 | **TAKEN by Pragma** | — |
| LF-2 | **TAKEN by Cornice** (1st occupant) · OPEN to second occupant under inheritance contract | 2nd LF-2 occupant: portfolio-of-work-led firm (evidence-led litigation · independent directorship case-bundle · audit-led methodology with published methodology pieces · longitudinal research with publications · inchiesta-led journalism · conservation studio with restoration case-bundle). Inherits LF-2 L1–L9 verbatim · differentiates inside cells per `design-orchestrator/references/internal-baselines/cornice-lf2-reference-pack.md §4 (anti-collapse rules)` and §9 (intake questions). |
| LF-3 | **TAKEN by Fiscus** | — |
| LF-4 | **TAKEN by Solaria** | — |
| LF-5 | **TAKEN by Continua** (post-migration · public-flipped 2026-04-30) | — |
| LF-6 | RESERVED | Magazine-edited boutiques (side-rail nav, collage cases). Activate on the 6th–7th sibling. Provisional E sequence in §1 above; first occupant binds the L1–L9 tuple. |
| LF-{NEW} | OPEN | Any candidate that doesn't fit LF-1..LF-6. Planner files an addendum declaring the new family's L1–L9 tuple before build. |

The next intake's professional-fit determines which open slot to claim. If two open slots both fit (LF-2 second-occupant and LF-{NEW}), the planner prefers the one already declared — the matrix's open-but-declared slots are cheaper to ship than full new-family additions.

---

## 4 · Forbidden tuples (extending the prohibition list)

Lifted from the divergence plan §6 and bound here as match-able tuples for fast scan during plan and walk.

After the post-Cornice consolidation, the following L1–L9 tuples are **claimed** and may not be reused by any new sibling without DISTINCTNESS_RULES §5 escalation (LF-2 second-occupant inherits LF-2 verbatim under the contract at `cornice-lf2-reference-pack.md §4`):

```
LF-1 :: (split-55-45,     A,        absent, numbered-grid,         band-at-3,    typographic-grid,        list-row,       sticky-top,            3-col)
LF-2 :: (stacked-editorial, B,      absent, essay-with-anchors,    hero-overlay, single-portrait-feature, magazine-grid,  split-wordmark-top,    4-col-with-whistleblowing)
LF-3 :: (split-55-45,     A+slot4,  slot-4, numbered-grid,         band-at-3,    typographic-grid,        list-row,       sticky-top,            3-col)
LF-4 :: (split-55-45,     C,        slot-5, manifesto-replacement, band-at-5,    absent,                  list-row,       sticky-top,            3-col)
LF-5 :: (object-overlay,  D,        slot-2, 2x2-with-image,        band-at-4,    pillar-photo,            timeline,       condensed-minimal-top, 4-col-with-whistleblowing)
```

A new sibling whose declared L1–L9 tuple matches any of the above on ≥6 of 9 dimensions is treated as a duplicate of that family and must be re-spec — except for an LF-2 second occupant explicitly invoking the family-inheritance contract at intake (CS-LAYOUT-11 second-occupant exception).

The L1+L2+L7 sub-tuple is the highest-leverage anti-collision check (CS-LAYOUT-13 BLOCKING):

```
(L1, L2, L7) — at least one must differ vs every existing sibling
LF-1: (split-55-45,        A,       list-row)
LF-2: (stacked-editorial,  B,       magazine-grid)   ← differs from LF-1 on all three sub-axes
LF-3: (split-55-45,        A+slot4, list-row)        ← differs from LF-1 only on L2 · in-family near-occupant § decision applies
LF-4: (split-55-45,        C,       list-row)        ← differs from LF-1 on L2 only at this sub-tuple level
LF-5: (object-overlay,     D,       timeline)        ← differs from all four on all three sub-axes
```

Notice that LF-3 and LF-4 differ from LF-1 on **only L2** at the (L1, L2, L7) sub-tuple — they pass CS-LAYOUT-13 by virtue of L2 differing, but barely. LF-2's and LF-5's full (L1, L2, L7) divergence is the high-confidence shape future siblings should aim for. The Pragma↔Fiscus 2/9 outcome is the documented in-family near-occupant pair (§6 below) — single-exception ladder.

---

## 5 · Maintenance

- **Each new sibling adds rows to §2** at intake (declared row) and at walk (rendered row). If the rows differ, F-LAYOUT-06 fires.
- **Each layout-touching edit-pass appends a new row** to §2 with a new `Recorded` date. The prior row is annotated `superseded`.
- **§1 family rows are append-only** for new families (LF-7, LF-8, ...). Existing family definitions are revised only with explicit user approval — the family's tuple is its identity, and changing it mid-life renames the family.
- **§3 OPEN/RESERVED slots are updated** as siblings enroll.
- **§4 forbidden tuples list** is regenerated whenever §1 changes.
- **§6 in-family near-occupant § decisions are append-only** — each documented exception names a single pair, files its rationale, and remains binding until explicitly superseded by a fresh § decision.

This file is the orchestrator's mechanical source of truth for layout-family occupancy. The planner reads §1 and §3 at intake; the style-critic reads §1 at critique; the walk-verifier writes §2 at walk; the release-gatekeeper reads §2 and §4 at release; intake reads §6 to know which near-occupant pairs are accepted. Every gate has a row to look at.

---

## 6 · § decisions · in-family near-occupant pairs

CS-LAYOUT-12 originally read "**≥ 4 of 9 layout dimensions different between any pair**." The Pragma↔Fiscus pair scores **2/9** (differs on L2 = `A` vs `A+slot4` and L3 = `absent` vs `slot-4` only). This was deferred at every flip pass since the divergence plan (2026-04-29) and is now formally addressed.

### § decision · Pragma ↔ Fiscus · 2/9 · ACCEPT (Option C) · 2026-05-03

**Filed by**: post-Cornice reference hardening pass · `factory/reports/hardening/post-cornice-reference-hardening.md` · `factory/reports/scorecard/post-cornice-reference-hardening/release-gatekeeper.md`.

**Decision**: ACCEPT the Pragma↔Fiscus 2/9 score as a documented in-family near-occupant pair. CS-LAYOUT-12 is reworded (see §6.2 below) to "**≥ 4 of 9 different OR a documented in-family near-occupant relationship**." This pair is the first (and presently only) documented near-occupant pair.

**Rationale**:
1. **The argument is genuinely available**: Pragma and Fiscus *are* both institutional advisory chrome variants — multi-partner organisation · serif-h1-LEFT split-55-45 hero · 5-link sticky-top primary-bg navbar · 3-col primary-bg footer · NDA-anchored proof shape. A reader examining the two side by side at 1920 sees two corporate-advisory firms whose differentiator is the calendar, and that is the right read — Fiscus's slot-4 cycle IS LF-3's identity, and the 2/9 score is what that identity costs structurally vs LF-1.
2. **The original rule over-fits this case**: CS-LAYOUT-12 ≥4/9 was written before LF-3 was understood as "LF-1 + slot-4," and it over-fits when the family difference is precisely a single-cell addition (L2 sequence widened to insert slot-4 + L3 promotion of the slot-4 cycle to the named cadence cell).
3. **Option C closes the audit**. Options A (migrate Pragma's L7 from `list-row` to a different cases-shape) and B (migrate Fiscus's L9 from `3-col` to a `4-col-with-regulatory-disclosures` footer) re-open a sibling for a layout migration, which is itself a workflow A.5+ pass with frozen-sibling regression risk on the other 4 — exactly the multi-session diversion that the post-Cornice hardening pass is avoiding to unblock the 6th-sibling intake. Options A and B remain available later if the orchestrator decides Option C was wrong.
4. **The differentiation lives at the skin layer**: Pragma (navy + emerald) vs Fiscus (warm-neutral + blu-notte + gold) clear the 5-axes skin distinctness rule (DISTINCTNESS_RULES §1) at 5/5 — voice anchor, palette, hero photography, typography, and section rhythm all differ even though the layout shape is family-adjacent.

**Operational consequence**:
- A 6th sibling that scores 2/9 vs an existing sibling does **NOT** inherit the exception by default. The exception is named per-pair and requires its own § decision filed at this section, ratified at A.6 review-lock, and motivated on the same "intentionally adjacent professional fit · skin axes carry differentiation" grounds.
- The 6th sibling MUST score ≥ 4/9 vs each of the five live siblings unless the orchestrator files a fresh in-family near-occupant § decision at intake (workflow A.1) and ratifies it at A.6.
- Pragma↔Fiscus remains a single near-occupant pair. **Any 7th sibling that creates a second near-occupant pair triggers a § decision review on CS-LAYOUT-12 itself** — the rule's intent is a single-exception ladder (one validated cluster-level case), not a generalised relaxation.
- The release-gatekeeper at every future flip cites this § decision when asserting the layout-distinctness gate is GREEN. No silent waiver.

**Wireframe-level evidence**:
- 1920px wireframe overlay of Pragma vs Fiscus shows ~85% bounding-box surface area shared (above the B-LAYOUT-1 ≥30% difference threshold for new pairs · documented as accepted because of the in-family near-occupant relationship).
- Pragma's 5-section home (`hero · pillars · kpi-band · sectors · trust · leadership · cases · cta`) and Fiscus's 6-section home (same with `cycle` inserted at slot-4) are intentionally adjacent — the slot-4 calendar IS Fiscus's structural claim, not a defect.

### §6.2 · CS-LAYOUT-12 wording update

CS-LAYOUT-12 in `factory/reports/hardening/corporate-suite-layout-variance-rules.md §2` is reworded effective 2026-05-03 to:

> **CS-LAYOUT-12 [BLOCKING] · Sibling pairs must differ on ≥ 4 of 9 layout dimensions · OR a documented in-family near-occupant relationship**
>
> For every existing sibling, the new sibling's L1–L9 tuple must differ on ≥ 4 of 9 dimensions. The two-sibling pair otherwise scores layout-collision regardless of how the skin axes score.
>
> **Exception (in-family near-occupant)**: a pair that scores < 4/9 may be ACCEPTED if a § decision is filed at `factory/reports/hardening/corporate-suite-layout-family-matrix.md §6` documenting (a) the layout-shape adjacency is intentional (one family is structurally a single-cell addition to the other), (b) the differentiation is carried at the skin layer at ≥ 5/5 on the DISTINCTNESS_RULES §1 axes, and (c) the orchestrator ratifies the exception at A.6 review-lock. Currently filed: Pragma↔Fiscus (2026-05-03).
>
> **Single-exception ladder**: the in-family near-occupant exception is intended for a single validated pair per cluster. A second pair triggers a § decision review on CS-LAYOUT-12 itself.
>
> **Failure mode**: a new sibling shares 7 of 9 layout dimensions with Pragma and no § decision is filed. Plan re-spec required.

This is the layout analogue of the existing 4-of-5-axes rule in DISTINCTNESS_RULES §1, with a documented exception ladder.
